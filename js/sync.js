(function () {
"use strict";

/* Cloud sync.
   The cycle is always pull -> merge -> push, never overwrite. Because
   Store.merge is idempotent, a bad network moment or two devices writing
   at once can duplicate work but can never lose it.

   Adding a provider means adding one object to ADAPTERS with get() and
   put(). Nothing else in the app has to change. */

const S = window.Store;

/* Each adapter stores one JSON file per profile, named <profile>.json */
const ADAPTERS = {

  none: {
    label: "This device only",
    needs: [],
    async get(){ return null; },
    async put(){ return true; }
  },

  /* Generic REST/object store: GET and PUT a JSON file at url/<profile>.json
     with an optional bearer token. Works with most personal cloud APIs,
     S3-compatible buckets behind a signed endpoint, and tiny custom servers. */
  rest: {
    label: "REST / object storage",
    needs: ["url", "token"],
    async get(cfg, profile){
      const r = await fetch(file(cfg, profile), {
        headers: authHeaders(cfg), cache: "no-store"
      });
      if (r.status === 404) return null;
      if (!r.ok) throw new Error("HTTP " + r.status);
      return r.json();
    },
    async put(cfg, profile, data){
      const r = await fetch(file(cfg, profile), {
        method: "PUT",
        headers: Object.assign({ "Content-Type": "application/json" }, authHeaders(cfg)),
        body: JSON.stringify(data)
      });
      if (!r.ok) throw new Error("HTTP " + r.status);
      return true;
    }
  },

  /* Your own Pi. Same wire format as the rest adapter, but labelled for the
     t9-sync service in server/. Point url at the Tailscale HTTPS hostname:
     https://waleedcloud.<your-tailnet>.ts.net  — the browser will refuse a
     plain http:// address because the site itself is served over https. */
  t9: {
    label: "WaleedCloud (your own Pi)",
    needs: ["url", "token"],
    async get(cfg, profile){
      const r = await fetch(file(cfg, profile), { headers: authHeaders(cfg), cache: "no-store" });
      if (r.status === 404) return null;
      if (!r.ok) throw new Error("HTTP " + r.status);
      return r.json();
    },
    async put(cfg, profile, data){
      const r = await fetch(file(cfg, profile), {
        method: "PUT",
        headers: Object.assign({ "Content-Type": "application/json" }, authHeaders(cfg)),
        body: JSON.stringify(data)
      });
      if (!r.ok) throw new Error("HTTP " + r.status);
      return true;
    },
    async health(cfg){
      const base = String(cfg.url || "").replace(/\/+$/, "");
      const r = await fetch(base + "/health", { cache: "no-store" });
      if (!r.ok) throw new Error("HTTP " + r.status);
      return r.json();
    }
  },

  /* WebDAV — Nextcloud, ownCloud, Synology, most self-hosted personal clouds.
     Use an app password, never your account password. */
  webdav: {
    label: "WebDAV / Nextcloud",
    needs: ["url", "user", "token"],
    async get(cfg, profile){
      const r = await fetch(file(cfg, profile), {
        headers: { Authorization: basic(cfg) }, cache: "no-store"
      });
      if (r.status === 404) return null;
      if (!r.ok) throw new Error("HTTP " + r.status);
      return r.json();
    },
    async put(cfg, profile, data){
      const r = await fetch(file(cfg, profile), {
        method: "PUT",
        headers: { Authorization: basic(cfg), "Content-Type": "application/json" },
        body: JSON.stringify(data)
      });
      if (!r.ok) throw new Error("HTTP " + r.status);
      return true;
    }
  },

  /* A secret GitHub Gist. You already have a GitHub account, it costs nothing,
     it works from every device, and CORS is guaranteed to work.
     url = the gist id, token = a PAT with only the "gist" scope. */
  gist: {
    label: "GitHub secret gist",
    needs: ["url", "token"],
    async get(cfg, profile){
      const r = await fetch("https://api.github.com/gists/" + cfg.url.trim(), {
        headers: { Authorization: "Bearer " + cfg.token.trim(),
                   Accept: "application/vnd.github+json" },
        cache: "no-store"
      });
      if (r.status === 404) return null;
      if (!r.ok) throw new Error("HTTP " + r.status);
      const g = await r.json();
      const f = g.files && g.files[profile + ".json"];
      if (!f) return null;
      if (f.truncated && f.raw_url) return (await fetch(f.raw_url)).json();
      return JSON.parse(f.content);
    },
    async put(cfg, profile, data){
      const files = {};
      files[profile + ".json"] = { content: JSON.stringify(data, null, 1) };
      const r = await fetch("https://api.github.com/gists/" + cfg.url.trim(), {
        method: "PATCH",
        headers: { Authorization: "Bearer " + cfg.token.trim(),
                   Accept: "application/vnd.github+json",
                   "Content-Type": "application/json" },
        body: JSON.stringify({ files })
      });
      if (!r.ok) throw new Error("HTTP " + r.status);
      return true;
    }
  }
};

function file(cfg, profile){
  const base = String(cfg.url || "").replace(/\/+$/, "");
  // the t9-sync service serves files under /files/
  const path = (S.getSyncCfg().adapter === "t9") ? "/files/" : "/";
  return base + path + encodeURIComponent(profile) + ".json";
}
function authHeaders(cfg){
  return cfg.token ? { Authorization: "Bearer " + String(cfg.token).trim() } : {};
}
function basic(cfg){
  return "Basic " + btoa(String(cfg.user || "") + ":" + String(cfg.token || ""));
}

/* ----------------------------------------------------------- the engine */
let status = { state: "off", at: null, msg: "This device only", pending: false };
let listeners = [];
let pushTimer = null;
let busy = false;

function onStatus(fn){ listeners.push(fn); }
function emit(){ listeners.forEach(f => { try { f(status); } catch(e){} }); }
function setStatus(st, msg){
  status.state = st; status.msg = msg;
  if (st === "ok") status.at = new Date();
  emit();
}
function getStatus(){ return status; }

function adapter(){
  const cfg = S.getSyncCfg();
  return ADAPTERS[cfg.adapter] || ADAPTERS.none;
}
function isOn(){ return S.getSyncCfg().adapter !== "none"; }

function configured(){
  const cfg = S.getSyncCfg();
  const a = adapter();
  return a.needs.every(k => String(cfg[k] || "").trim().length > 0);
}

/* Pull the remote copy, merge it into what is on this device, push the result.
   Safe to call at any time; overlapping calls are collapsed. */
async function sync(reason){
  if (!isOn()) { setStatus("off", "This device only"); return false; }
  if (!configured()) { setStatus("error", "Sync is not configured"); return false; }
  if (!S.currentProfile()) return false;
  if (busy) { status.pending = true; return false; }

  busy = true;
  setStatus("syncing", reason === "boot" ? "Loading your progress…" : "Saving…");
  try {
    const cfg = S.getSyncCfg();
    const p = S.currentProfile();
    const remote = await adapter().get(cfg, p);
    if (remote) await S.applyMerged(remote);
    else await S.saveNow();
    await adapter().put(cfg, p, S.get());
    setStatus("ok", "Synced");
    busy = false;
    if (status.pending) { status.pending = false; return sync("queued"); }
    return true;
  } catch (e) {
    busy = false;
    const m = String(e && e.message || e);
    setStatus("error", m.includes("Failed to fetch")
      ? "Offline — saved on this device, will sync later"
      : "Sync failed: " + m);
    return false;
  }
}

/* Debounced: many small edits produce one upload. */
function schedulePush(){
  if (!isOn() || !S.getSyncCfg().auto) return;
  clearTimeout(pushTimer);
  pushTimer = setTimeout(() => sync("auto"), 4000);
}

/* Test a configuration before saving it, without touching real data. */
async function test(cfg, profile){
  const a = ADAPTERS[cfg.adapter];
  if (!a) throw new Error("Unknown provider");
  if (!a.needs.every(k => String(cfg[k] || "").trim())) throw new Error("Some fields are empty");
  const probe = "__connection-test__";
  await a.put(cfg, probe, { ok: true, at: Date.now() });
  const back = await a.get(cfg, probe);
  if (!back || !back.ok) throw new Error("Wrote a file but could not read it back");
  return true;
}

window.Sync = {
  ADAPTERS, sync, schedulePush, test, onStatus, getStatus, isOn, configured,
  list: () => Object.keys(ADAPTERS).map(k => ({ id: k, label: ADAPTERS[k].label, needs: ADAPTERS[k].needs }))
};
})();

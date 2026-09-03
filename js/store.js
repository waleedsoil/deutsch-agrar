(function () {
"use strict";

/* Storage + profiles + merge.
   Every learner gets a named profile. State is kept per profile in the
   browser, and - if sync is configured - mirrored to a cloud file.
   The merge below is the important part: it is idempotent and
   order-independent, so merging twice equals merging once and two
   devices can never destroy each other's work. */

const NS       = "deutsch-agrar";
const K_INDEX  = NS + ":profiles";
const K_LAST   = NS + ":last";
const K_SYNC   = NS + ":sync";
const K_STATE  = (p) => NS + ":state:" + p;

const backend = (typeof window !== "undefined" && window.storage && window.storage.get)
  ? { name: "claude",
      async get(k){ try { const r = await window.storage.get(k); return r ? r.value : null; } catch(e){ return null; } },
      async set(k, v){ try { await window.storage.set(k, v); return true; } catch(e){ return false; } } }
  : { name: "local",
      async get(k){ try { return localStorage.getItem(k); } catch(e){ return null; } },
      async set(k, v){ try { localStorage.setItem(k, v); return true; } catch(e){ return false; } } };

/* ------------------------------------------------------------ helpers -- */
function todayISO(d){
  const t = d || new Date();
  return t.getFullYear() + "-" + String(t.getMonth()+1).padStart(2,"0") + "-" + String(t.getDate()).padStart(2,"0");
}
function epochDay(iso){
  const d = iso ? new Date(iso + "T00:00:00") : new Date();
  return Math.floor(d.getTime() / 86400000);
}
function now(){ return Date.now(); }

/* A display name becomes a stable file-safe id: "Raj Patil" -> "raj-patil" */
function slug(name){
  return String(name || "").trim().toLowerCase()
    .replace(/[^a-z0-9\u0900-\u097F]+/g, "-")
    .replace(/^-+|-+$/g, "").slice(0, 40);
}

function blank(name){
  return {
    v: 2,
    name: name || "",
    started: todayISO(),
    updatedAt: now(),
    cursor: { w: 1, d: 1 },
    blocks: {},
    done: {},
    notes: {},
    srs: {},
    quiz: {},
    storyRead: {},
    errors: [],
    streak: { last: null, count: 0, longest: 0 },
    settings: { mode: 90, theme: "light", newPerDay: 12, mr: true, onboarded: false },
    log: {}
  };
}

/* Older saves stored notes as plain strings and srs without a timestamp. */
function migrate(s){
  const b = blank(s && s.name);
  const out = Object.assign(b, s || {});
  out.settings = Object.assign(blank().settings, (s && s.settings) || {});
  out.streak   = Object.assign(blank().streak, (s && s.streak) || {});
  out.cursor   = Object.assign({ w:1, d:1 }, (s && s.cursor) || {});
  const n = {};
  for (const k in (out.notes || {})) {
    const v = out.notes[k];
    n[k] = (typeof v === "string") ? { t: v, at: 0 } : v;
  }
  out.notes = n;
  for (const id in (out.srs || {})) if (out.srs[id].seen === undefined) out.srs[id].seen = 0;
  out.errors = (out.errors || []).map(e => Object.assign({ id: (e.ts || "") + "|" + (e.text || "") }, e));
  out.v = 2;
  return out;
}

/* --------------------------------------------------------------- merge -- */
/* Every rule is max / union / OR, so merge(merge(a,b),b) === merge(a,b). */
function merge(a, b){
  if (!a) return b; if (!b) return a;
  const out = blank(a.name || b.name);

  out.name      = a.name || b.name;
  out.started   = (a.started < b.started) ? a.started : b.started;
  out.updatedAt = Math.max(a.updatedAt || 0, b.updatedAt || 0);

  for (const k of new Set([...Object.keys(a.done||{}), ...Object.keys(b.done||{})])) {
    const x = (a.done||{})[k], y = (b.done||{})[k];
    out.done[k] = (!x) ? y : (!y) ? x : (x < y ? x : y);
  }

  for (const k of new Set([...Object.keys(a.blocks||{}), ...Object.keys(b.blocks||{})])) {
    const x = (a.blocks||{})[k] || [], y = (b.blocks||{})[k] || [];
    const len = Math.max(x.length, y.length);
    const arr = [];
    for (let i = 0; i < len; i++) arr.push(!!x[i] || !!y[i]);
    out.blocks[k] = arr;
  }

  for (const k of new Set([...Object.keys(a.notes||{}), ...Object.keys(b.notes||{})])) {
    const x = (a.notes||{})[k], y = (b.notes||{})[k];
    if (!x) { out.notes[k] = y; continue; }
    if (!y) { out.notes[k] = x; continue; }
    if ((x.at||0) === (y.at||0)) out.notes[k] = (x.t||"").length >= (y.t||"").length ? x : y;
    else out.notes[k] = (x.at||0) > (y.at||0) ? x : y;
  }

  for (const id of new Set([...Object.keys(a.srs||{}), ...Object.keys(b.srs||{})])) {
    const x = (a.srs||{})[id], y = (b.srs||{})[id];
    if (!x) { out.srs[id] = y; continue; }
    if (!y) { out.srs[id] = x; continue; }
    if ((x.seen||0) === (y.seen||0)) out.srs[id] = (x.reps||0) >= (y.reps||0) ? x : y;
    else out.srs[id] = (x.seen||0) > (y.seen||0) ? x : y;
  }

  for (const k of new Set([...Object.keys(a.quiz||{}), ...Object.keys(b.quiz||{})])) {
    const x = (a.quiz||{})[k] || {}, y = (b.quiz||{})[k] || {};
    out.quiz[k] = {
      best: Math.max(x.best || 0, y.best || 0),
      attempts: Math.max(x.attempts || 0, y.attempts || 0),
      last: (x.last !== undefined && y.last !== undefined) ? Math.max(x.last, y.last)
            : (x.last !== undefined ? x.last : y.last)
    };
  }

  Object.assign(out.storyRead, a.storyRead || {}, b.storyRead || {});

  const seen = {};
  for (const e of [...(a.errors||[]), ...(b.errors||[])]) {
    const id = e.id || ((e.ts || "") + "|" + (e.text || ""));
    if (!seen[id]) seen[id] = Object.assign({ id }, e);
  }
  out.errors = Object.values(seen).sort((p, q) => String(q.ts||"").localeCompare(String(p.ts||"")));

  for (const k of new Set([...Object.keys(a.log||{}), ...Object.keys(b.log||{})]))
    out.log[k] = Math.max((a.log||{})[k] || 0, (b.log||{})[k] || 0);

  const sa = a.streak || {}, sb = b.streak || {};
  const later = (String(sa.last||"") >= String(sb.last||"")) ? sa : sb;
  out.streak = { last: later.last || null, count: later.count || 0,
                 longest: Math.max(sa.longest || 0, sb.longest || 0) };

  const pa = (a.cursor||{w:1,d:1}), pb = (b.cursor||{w:1,d:1});
  out.cursor = ((pa.w*7 + pa.d) >= (pb.w*7 + pb.d)) ? Object.assign({}, pa) : Object.assign({}, pb);

  out.settings = Object.assign({}, blank().settings,
    ((a.updatedAt||0) >= (b.updatedAt||0) ? (a.settings||{}) : (b.settings||{})));

  return out;
}

/* ------------------------------------------------------------- profiles */
let index = [];
let profile = null;
let state = blank();
let saveTimer = null;
let onChange = null;

async function loadIndex(){
  const raw = await backend.get(K_INDEX);
  try { index = raw ? JSON.parse(raw) : []; } catch(e){ index = []; }
  return index;
}
function listProfiles(){ return index.slice(); }
async function lastProfile(){ return await backend.get(K_LAST); }

async function openProfile(name){
  const id = slug(name);
  if (!id) throw new Error("A profile needs a name");
  if (!index.some(p => p.id === id)) {
    index.push({ id, name: String(name).trim(), created: todayISO() });
    await backend.set(K_INDEX, JSON.stringify(index));
  }
  profile = id;
  await backend.set(K_LAST, id);
  const raw = await backend.get(K_STATE(id));
  if (raw) { try { state = migrate(JSON.parse(raw)); } catch(e){ state = blank(name); } }
  else state = blank(String(name).trim());
  state.name = state.name || String(name).trim();
  return state;
}

function closeProfile(){ profile = null; state = blank(); }

async function removeProfile(id){
  index = index.filter(p => p.id !== id);
  await backend.set(K_INDEX, JSON.stringify(index));
  await backend.set(K_STATE(id), "");
  if (profile === id) closeProfile();
}

/* ---------------------------------------------------------------- state */
function get(){ return state; }
function currentProfile(){ return profile; }
function currentName(){ return state.name || profile || ""; }

function save(){
  state.updatedAt = now();
  clearTimeout(saveTimer);
  saveTimer = setTimeout(async () => {
    if (!profile) return;
    await backend.set(K_STATE(profile), JSON.stringify(state));
    if (onChange) onChange();
  }, 200);
}

async function saveNow(){
  if (!profile) return false;
  state.updatedAt = state.updatedAt || now();
  clearTimeout(saveTimer);
  return backend.set(K_STATE(profile), JSON.stringify(state));
}

async function applyMerged(remote){
  state = merge(state, migrate(remote));
  await saveNow();
  return state;
}

function setOnChange(fn){ onChange = fn; }

/* --------------------------------------------------------------- streak */
function touchStreak(){
  const t = todayISO();
  const s = state.streak;
  if (s.last === t) return s;
  const gap = s.last ? epochDay(t) - epochDay(s.last) : 999;
  s.count = (gap === 1) ? s.count + 1 : 1;
  s.last = t;
  if (s.count > s.longest) s.longest = s.count;
  save();
  return s;
}

/* --------------------------------------------------- sync configuration */
let syncCfg = { adapter: "none", url: "", user: "", token: "", auto: true };

async function loadSyncCfg(){
  const raw = await backend.get(K_SYNC);
  if (raw) { try { syncCfg = Object.assign(syncCfg, JSON.parse(raw)); } catch(e){} }
  return syncCfg;
}
function getSyncCfg(){ return syncCfg; }
async function setSyncCfg(cfg){
  syncCfg = Object.assign(syncCfg, cfg);
  return backend.set(K_SYNC, JSON.stringify(syncCfg));
}

/* ------------------------------------------------------ export / import */
function exportJSON(){ return JSON.stringify(state, null, 1); }
async function importJSON(text){
  const parsed = JSON.parse(text);
  if (!parsed || typeof parsed !== "object" || !parsed.cursor) throw new Error("Not a progress file");
  state = merge(state, migrate(parsed));
  return saveNow();
}
async function reset(){
  state = blank(state.name);
  return saveNow();
}

window.Store = {
  backend: backend.name,
  get, save, saveNow, touchStreak, exportJSON, importJSON, reset,
  todayISO, epochDay, now, slug, merge, migrate, blank,
  loadIndex, listProfiles, lastProfile, openProfile, closeProfile, removeProfile,
  currentProfile, currentName, applyMerged, setOnChange,
  loadSyncCfg, getSyncCfg, setSyncCfg
};
})();

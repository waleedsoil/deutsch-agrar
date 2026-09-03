#!/usr/bin/env python3
"""
t9-sync — progress sync for the Deutsch für Agrar course.

Deliberately additive. It does not import, read, restart or reconfigure
anything in the existing WaleedCloud stack: it is a separate process on its
own port, writing to its own directory. Nothing already running is touched.

  GET    /health                 -> {"ok": true, ...}          (no auth)
  GET    /files/<profile>.json   -> the stored JSON, or 404
  PUT    /files/<profile>.json   -> stores it, 204
  OPTIONS anything               -> CORS preflight

Auth: Authorization: Bearer <token>
Config comes from the environment, so no secret is ever written into a file
that might get committed:

  T9_SYNC_TOKEN    required, the shared secret
  T9_SYNC_DIR      where the JSON lives   (default ~/waleedcloud/deutsch-sync)
  T9_SYNC_ORIGIN   allowed web origin(s), comma separated
                   (default https://waleedsoil.github.io)
  T9_SYNC_PORT     default 5051
  T9_SYNC_HOST     default 127.0.0.1

Run it behind `tailscale serve` so the browser gets real HTTPS. See install.md.
"""

import os, re, json, time, hmac, shutil, pathlib, logging
from urllib.parse import unquote
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

TOKEN   = os.environ.get("T9_SYNC_TOKEN", "").strip()
DIR     = pathlib.Path(os.environ.get("T9_SYNC_DIR",
            str(pathlib.Path.home() / "waleedcloud" / "deutsch-sync"))).expanduser()
ORIGINS = [o.strip() for o in os.environ.get(
            "T9_SYNC_ORIGIN", "https://waleedsoil.github.io").split(",") if o.strip()]
PORT    = int(os.environ.get("T9_SYNC_PORT", "5051"))
HOST    = os.environ.get("T9_SYNC_HOST", "127.0.0.1")

MAX_BODY   = 5 * 1024 * 1024      # a progress file is a few hundred KB at most
KEEP_BACKUPS = 30
# \w alone is not enough: Devanagari vowel signs such as U+093E are category Mc,
# which str.isalnum() reports as False, so "राज" would be rejected. The explicit
# Devanagari block covers the marks as well as the letters.
NAME_RE    = re.compile(r"^[\w\-\u0900-\u097F]{1,60}$", re.UNICODE)
DRAIN_CAP  = 25 * 1024 * 1024

logging.basicConfig(level=logging.INFO, format="%(asctime)s t9-sync %(message)s")
log = logging.getLogger("t9-sync")


def safe_name(raw):
    """Reject anything that could escape the sync directory.
    The path arrives percent-encoded, so a Devanagari profile name shows up
    as %E0%A4%B0... and has to be decoded before it is validated."""
    name = unquote(raw or "").strip()
    if name.endswith(".json"):
        name = name[:-5]
    if not NAME_RE.match(name) or name in (".", ".."):
        return None
    return name


def store_path(name):
    return DIR / (name + ".json")


def write_atomic(path, data):
    """Write to a temp file on the same filesystem, then rename. A power cut
    during a write leaves the previous good file intact, never a half file."""
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(".json.tmp")
    with open(tmp, "w", encoding="utf-8") as f:
        f.write(data)
        f.flush()
        os.fsync(f.fileno())
    os.replace(tmp, path)


def keep_backup(name, path):
    if not path.exists():
        return
    bdir = DIR / "backups" / name
    bdir.mkdir(parents=True, exist_ok=True)
    shutil.copy2(path, bdir / (time.strftime("%Y%m%d-%H%M%S") + ".json"))
    old = sorted(bdir.glob("*.json"))[:-KEEP_BACKUPS]
    for f in old:
        try:
            f.unlink()
        except OSError:
            pass


class Handler(BaseHTTPRequestHandler):
    server_version = "t9-sync/1.0"
    protocol_version = "HTTP/1.1"

    # ------------------------------------------------------------- helpers
    def _origin_ok(self):
        o = self.headers.get("Origin")
        return o if (o and o in ORIGINS) else None

    def _cors(self):
        o = self._origin_ok()
        if o:
            self.send_header("Access-Control-Allow-Origin", o)
            self.send_header("Vary", "Origin")
            self.send_header("Access-Control-Allow-Headers", "authorization, content-type")
            self.send_header("Access-Control-Allow-Methods", "GET, PUT, OPTIONS")
            self.send_header("Access-Control-Max-Age", "86400")

    def _send(self, code, payload=None, ctype="application/json"):
        body = b"" if payload is None else (
            payload if isinstance(payload, bytes) else payload.encode("utf-8"))
        self.send_response(code)
        if body:
            self.send_header("Content-Type", ctype)
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Cache-Control", "no-store")
        self._cors()
        self.end_headers()
        if body:
            self.wfile.write(body)

    def _authed(self):
        if not TOKEN:
            log.error("T9_SYNC_TOKEN is not set; refusing every request")
            return False
        got = self.headers.get("Authorization", "")
        if not got.startswith("Bearer "):
            return False
        return hmac.compare_digest(got[7:].strip(), TOKEN)

    def log_message(self, fmt, *args):
        log.info("%s %s", self.address_string(), fmt % args)

    # -------------------------------------------------------------- routes
    def do_OPTIONS(self):
        self._send(204)

    def do_GET(self):
        if self.path == "/health":
            self._send(200, json.dumps({
                "ok": True, "service": "t9-sync",
                "dir": str(DIR),
                "profiles": sorted(p.stem for p in DIR.glob("*.json")) if DIR.exists() else []
            }))
            return

        if not self._authed():
            self._send(401, json.dumps({"error": "bad or missing token"}))
            return

        m = re.match(r"^/files/(.+)$", self.path)
        if not m:
            self._send(404, json.dumps({"error": "no such endpoint"}))
            return
        name = safe_name(m.group(1))
        if not name:
            self._send(400, json.dumps({"error": "bad profile name"}))
            return

        p = store_path(name)
        if not p.exists():
            self._send(404, json.dumps({"error": "no file for this profile yet"}))
            return
        self._send(200, p.read_bytes())

    def do_PUT(self):
        if not self._authed():
            self._send(401, json.dumps({"error": "bad or missing token"}))
            return

        m = re.match(r"^/files/(.+)$", self.path)
        if not m:
            self._send(404, json.dumps({"error": "no such endpoint"}))
            return
        name = safe_name(m.group(1))
        if not name:
            self._send(400, json.dumps({"error": "bad profile name"}))
            return

        try:
            length = int(self.headers.get("Content-Length", "0"))
        except ValueError:
            length = 0
        if length <= 0:
            self._send(411, json.dumps({"error": "no body"}))
            return
        if length > MAX_BODY:
            # Read and throw away the body first, otherwise the client sees a
            # connection reset instead of the 413 explaining what went wrong.
            left = min(length, DRAIN_CAP)
            while left > 0:
                chunk = self.rfile.read(min(65536, left))
                if not chunk:
                    break
                left -= len(chunk)
            self.send_response(413)
            body = json.dumps({"error": "body too large", "max_bytes": MAX_BODY}).encode()
            self.send_header("Content-Type", "application/json")
            self.send_header("Content-Length", str(len(body)))
            self.send_header("Connection", "close")
            self._cors()
            self.end_headers()
            self.wfile.write(body)
            self.close_connection = True
            return

        raw = self.rfile.read(length)
        try:
            parsed = json.loads(raw.decode("utf-8"))
            if not isinstance(parsed, dict):
                raise ValueError("not an object")
        except Exception as e:
            self._send(400, json.dumps({"error": "not valid JSON: %s" % e}))
            return

        p = store_path(name)
        keep_backup(name, p)
        write_atomic(p, json.dumps(parsed, ensure_ascii=False, separators=(",", ":")))
        log.info("stored %s (%d bytes)", p.name, len(raw))
        self._send(204)


def main():
    if not TOKEN:
        raise SystemExit("T9_SYNC_TOKEN is not set. Refusing to start without a token.")
    DIR.mkdir(parents=True, exist_ok=True)
    log.info("serving %s on %s:%d", DIR, HOST, PORT)
    log.info("allowed origins: %s", ", ".join(ORIGINS))
    ThreadingHTTPServer((HOST, PORT), Handler).serve_forever()


if __name__ == "__main__":
    main()

#!/usr/bin/env bash
# check.sh — run this on the Pi. It changes nothing. It only looks.
# It tells you which of the four setup paths you are on, so you can skip
# straight to that section of SETUP.md.

set -uo pipefail
say()  { printf '\n\033[1m%s\033[0m\n' "$*"; }
ok()   { printf '  \033[32m+\033[0m %s\n' "$*"; }
no()   { printf '  \033[31m-\033[0m %s\n' "$*"; }
info() { printf '    %s\n' "$*"; }

PATH_CHOICE=""

say "1. What is already listening"
if command -v ss >/dev/null 2>&1; then
  LISTEN=$(sudo ss -tlnp 2>/dev/null || ss -tln 2>/dev/null)
  echo "$LISTEN" | awk 'NR==1 || /LISTEN/' | sed 's/^/    /' | head -25
else
  no "ss not available"
fi

say "2. Is port 5051 free for the sync service"
if echo "${LISTEN:-}" | grep -q ':5051 '; then
  no "something is already on 5051"
  info "change T9_SYNC_PORT later, or find what it is:  sudo ss -tlnp | grep 5051"
else
  ok "5051 is free"
fi

say "3. Is the sync service already installed"
if systemctl list-unit-files 2>/dev/null | grep -q '^t9-sync.service'; then
  ok "t9-sync.service exists"
  systemctl is-active t9-sync.service >/dev/null 2>&1 && ok "and it is running" || no "but it is not running"
  info "logs: journalctl -u t9-sync.service -n 30 --no-pager"
else
  no "not installed yet — that is step A in SETUP.md"
fi

say "4. Reverse proxies already running"
FOUND_PROXY=""
for s in caddy nginx apache2 traefik; do
  if systemctl is-active "$s" >/dev/null 2>&1; then ok "$s is running"; FOUND_PROXY="$s"; fi
done
[ -z "$FOUND_PROXY" ] && no "no caddy / nginx / apache / traefik running"

say "5. Tailscale"
HAVE_TS=""
if command -v tailscale >/dev/null 2>&1; then
  ok "tailscale is installed"
  HAVE_TS=1
  DNSNAME=$(tailscale status --json 2>/dev/null | grep -o '"DNSName":"[^"]*"' | head -1 | cut -d'"' -f4 | sed 's/\.$//')
  [ -n "${DNSNAME:-}" ] && info "this machine: $DNSNAME"
  echo "  serve/funnel status:"
  tailscale serve status 2>/dev/null | sed 's/^/    /' || info "(none configured)"
  if tailscale funnel status >/dev/null 2>&1; then
    tailscale funnel status 2>/dev/null | sed 's/^/    /'
  fi
else
  no "tailscale not installed"
fi

say "6. Cloudflare tunnel"
if command -v cloudflared >/dev/null 2>&1; then
  ok "cloudflared is installed"
  systemctl is-active cloudflared >/dev/null 2>&1 && ok "and running" || no "not running"
else
  no "cloudflared not installed"
fi

say "7. Disk and backup target"
df -h / /media/CloudMirror 2>/dev/null | sed 's/^/    /'
if systemctl list-unit-files 2>/dev/null | grep -qi 'mirror'; then
  ok "a mirror unit exists"
  systemctl list-unit-files | grep -i mirror | sed 's/^/    /'
else
  no "no mirror unit found by name — check what you call it"
fi

say "VERDICT — which path you are on"
if [ -n "$HAVE_TS" ]; then
  echo "    You have Tailscale. Use PATH 1: Tailscale Funnel."
  echo "    It gives a public https address with a real certificate and needs"
  echo "    nothing installed on Raj's laptop. Go to SETUP.md section C1."
  PATH_CHOICE="C1"
elif [ -n "$FOUND_PROXY" ]; then
  echo "    You already run $FOUND_PROXY. Use PATH 2: add one route to it."
  echo "    Go to SETUP.md section C2."
  PATH_CHOICE="C2"
else
  echo "    No Tailscale, no reverse proxy. Use PATH 3: Cloudflare Tunnel."
  echo "    Go to SETUP.md section C3."
  PATH_CHOICE="C3"
fi

say "Paste everything above if you get stuck."
echo

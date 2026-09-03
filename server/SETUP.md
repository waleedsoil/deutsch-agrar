# Setting up progress sync — the whole thing, start to finish

You do all of this once. After it, Raj opens a bookmark and studies, and you
never touch it again.

**Where this is going.** Your GitHub Pages site can only *serve* files, never
receive them, so it cannot store anyone's progress. Something has to accept an
upload. That something is a small service on your Pi, reachable over HTTPS. Raj's
browser talks to it directly. He installs nothing.

**What is not going to happen.** Nothing already running on the Pi is stopped,
edited, reconfigured or restarted. The Flask room API on 5000, `room-sensor`, the
HDMI dashboard, the mirror timer, your existing tokens — all untouched. This adds
one process on one new port writing to one new folder. If you abandon this
halfway through, everything that works today still works.

Total time: about twenty minutes.

---

## A. Find out which path you are on

Copy `server/check.sh` from the repo to the Pi and run it:

```bash
scp server/check.sh waleedcloud:~/
ssh waleedcloud
chmod +x ~/check.sh
./check.sh
```

It changes nothing — it only looks. At the bottom it prints a verdict naming the
section you should jump to in part C. Read the whole output anyway; it also tells
you whether port 5051 is free and whether your mirror covers the right folder.

If you already know you have Tailscale, you are on **path C1** and can read the
rest in order.

---

## B. Install the service (everyone does this)

### B1. Put the file on the Pi

```bash
scp server/t9_sync.py waleedcloud:~/
ssh waleedcloud
mkdir -p ~/apps/t9-sync ~/waleedcloud/deutsch-sync
mv ~/t9_sync.py ~/apps/t9-sync/
chmod +x ~/apps/t9-sync/t9_sync.py
```

Standard library only. No pip, no virtualenv, nothing to update later.

### B2. Make a token

This is a brand new secret used only by this service. It is not any password you
already have, and you should not reuse one.

```bash
python3 -c "import secrets; print(secrets.token_urlsafe(32))"
```

Copy the output somewhere for a minute — you will paste it twice.

### B3. Write the config

```bash
sudo install -m 600 /dev/null /etc/t9-sync.env
sudo nano /etc/t9-sync.env
```

Paste this, replacing the token and `YOURUSER`:

```
T9_SYNC_TOKEN=the-token-you-just-generated
T9_SYNC_DIR=/home/YOURUSER/waleedcloud/deutsch-sync
T9_SYNC_ORIGIN=https://waleedsoil.github.io
T9_SYNC_HOST=127.0.0.1
T9_SYNC_PORT=5051
```

Two of those lines are doing real security work:

`T9_SYNC_HOST=127.0.0.1` means the service is not reachable from your dorm LAN at
all. Only something running on the Pi itself can reach it. Whatever you set up in
part C is then the single, controlled way in. On a shared student network this
matters.

`T9_SYNC_ORIGIN` is the only website whose pages a browser will let call this
service. Even if someone learns your address, a page on another site cannot make
your browser talk to it.

The file is mode 600 and owned by root, so the token is not readable by other
accounts on the Pi.

### B4. Prove it starts

```bash
set -a; . /etc/t9-sync.env; set +a
python3 ~/apps/t9-sync/t9_sync.py
```

Leave it running. In a second terminal on the Pi:

```bash
curl -s localhost:5051/health
```

Expected:

```json
{"ok": true, "service": "t9-sync", "dir": "/home/YOURUSER/waleedcloud/deutsch-sync", "profiles": []}
```

Now test that it actually stores something:

```bash
TOKEN=$(sudo grep T9_SYNC_TOKEN /etc/t9-sync.env | cut -d= -f2)
curl -s -X PUT -H "Authorization: Bearer $TOKEN" \
     -H "Content-Type: application/json" \
     -d '{"hello":"world"}' localhost:5051/files/test.json
curl -s -H "Authorization: Bearer $TOKEN" localhost:5051/files/test.json
```

You should get `{"hello":"world"}` back. And confirm it refuses a bad token:

```bash
curl -s -o /dev/null -w '%{http_code}\n' \
     -H "Authorization: Bearer wrong" localhost:5051/files/test.json
```

That must print `401`. If it prints `200`, stop and tell me.

Ctrl-C to stop it. Clean up the test file:

```bash
rm ~/waleedcloud/deutsch-sync/test.json
```

### B5. Run it permanently

```bash
sudo nano /etc/systemd/system/t9-sync.service
```

```ini
[Unit]
Description=Deutsch fuer Agrar progress sync
After=network-online.target

[Service]
Type=simple
User=YOURUSER
EnvironmentFile=/etc/t9-sync.env
ExecStart=/usr/bin/python3 /home/YOURUSER/apps/t9-sync/t9_sync.py
Restart=on-failure
RestartSec=5
NoNewPrivileges=true
PrivateTmp=true
ProtectSystem=full
ProtectHome=read-only
ReadWritePaths=/home/YOURUSER/waleedcloud/deutsch-sync

[Install]
WantedBy=multi-user.target
```

Replace `YOURUSER` in all three places. Then:

```bash
sudo systemctl daemon-reload
sudo systemctl enable --now t9-sync.service
systemctl status t9-sync.service --no-pager
curl -s localhost:5051/health
```

`ProtectHome=read-only` with a single `ReadWritePaths` means that even in the
worst case, this service can only write into its own sync folder. It cannot touch
your room data, your reports, or anything else in your home directory.

---

## C. Give it an HTTPS address

This is the step that decides whether Raj can use it. Pick **one** section.

**The rule underneath all three:** your course site is served from
`https://waleedsoil.github.io`. A page loaded over HTTPS is not allowed to call a
plain `http://` address — the browser blocks it silently, with nothing useful in
the console. So the Pi must answer on `https://` with a certificate a browser
already trusts. All three options below produce exactly that.

### C1. Tailscale Funnel — use this if you have Tailscale

You already run Tailscale, so this needs no new software at all. `tailscale
serve` is private to your tailnet; **`tailscale funnel` is the public version**,
and public is what Raj needs, since he cannot install the Tailscale app.

Enable it:

```bash
sudo tailscale funnel --bg 5051
tailscale funnel status
```

If it complains that Funnel is not enabled for your tailnet, it prints a link.
Open it, approve Funnel for this machine, and run the command again. You may also
need to enable HTTPS certificates once, under DNS in the Tailscale admin console.

It prints something like:

```
https://waleedcloud.tailXXXX.ts.net
```

Test it from your Mac **with Tailscale turned off**, or from your phone on mobile
data — that is the only way to know it is genuinely public:

```bash
curl -s https://waleedcloud.tailXXXX.ts.net/health
```

If that returns the health JSON with Tailscale off, you are done. That hostname
is stable, it has a real certificate, and Raj needs nothing.

Funnel exposes port 5051 to the whole internet, so from here the token is the
only thing protecting your data. That is why step B2 generated a long random one
and why `T9_SYNC_ORIGIN` is set.

### C2. You already run a reverse proxy

If `check.sh` found Caddy, nginx or Traefik with a working certificate, add one
route and you are finished.

Caddy — add to your Caddyfile:

```
deutsch.yourdomain.com {
    reverse_proxy 127.0.0.1:5051
}
```

```bash
sudo systemctl reload caddy
```

nginx — a new server block:

```nginx
location /deutsch-sync/ {
    proxy_pass http://127.0.0.1:5051/;
    proxy_set_header Authorization $http_authorization;
}
```

```bash
sudo nginx -t && sudo systemctl reload nginx
```

That `proxy_set_header Authorization` line matters — some nginx configs strip the
header, and then every request comes back 401 and looks like a wrong token.

Test from outside your network, then use that URL in part D.

### C3. Cloudflare Tunnel — no Tailscale, no proxy

```bash
curl -fsSL https://pkg.cloudflare.com/cloudflare-main.gpg \
  | sudo tee /usr/share/keyrings/cloudflare-main.gpg >/dev/null
echo "deb [signed-by=/usr/share/keyrings/cloudflare-main.gpg] https://pkg.cloudflare.com/cloudflared any main" \
  | sudo tee /etc/apt/sources.list.d/cloudflared.list
sudo apt update && sudo apt install cloudflared
```

To prove it works in one command:

```bash
cloudflared tunnel --url http://127.0.0.1:5051
```

That prints a `trycloudflare.com` address. Use it to confirm the whole chain
works — but **do not give it to Raj**, because it changes every time it restarts
and his bookmark would break.

For a permanent hostname you need a free Cloudflare account with a domain on it:

```bash
cloudflared tunnel login
cloudflared tunnel create deutsch-sync
cloudflared tunnel route dns deutsch-sync deutsch.yourdomain.com

sudo mkdir -p /etc/cloudflared
sudo tee /etc/cloudflared/config.yml >/dev/null <<'EOF'
tunnel: deutsch-sync
credentials-file: /root/.cloudflared/deutsch-sync.json
ingress:
  - hostname: deutsch.yourdomain.com
    service: http://127.0.0.1:5051
  - service: http_status:404
EOF

sudo cloudflared service install
sudo systemctl enable --now cloudflared
curl -s https://deutsch.yourdomain.com/health
```

---

## D. Connect your own browser

Open `https://waleedsoil.github.io/deutsch-agrar/`, sign in with your name, then
**Progress → Sync across your devices**:

- Provider: **WaleedCloud (your own Pi)**
- Your Pi's HTTPS address: the hostname from part C, no trailing slash
- Token: the value of `T9_SYNC_TOKEN`
- Press **Save and test**

It writes a test file, reads it back, then uploads your real progress. Confirm on
the Pi:

```bash
ls -la ~/waleedcloud/deutsch-sync/
```

You should see a JSON file named after you.

---

## E. Set Raj up — the part where he does nothing

Still on that Progress page, scroll to **Set up someone else's device**.

Type `Raj`, press **Create setup link**, press **Copy link**.

Send him that link directly — a private message, not a group chat. Anyone holding
it can sync.

He opens it once, in whatever browser he already has. What happens:

1. The page reads the settings out of the link and saves them in his browser
2. It removes the link's payload from the address bar, so the token is not left
   sitting in his history or in the bookmark he is about to make
3. It opens his course, already under the name Raj
4. He bookmarks the page

From then on, every single day: **open bookmark, study, close.** No install, no
token, no settings page, no name to type. It reopens on the exact day he is on.

Check it landed:

```bash
ls -la ~/waleedcloud/deutsch-sync/
cat ~/waleedcloud/deutsch-sync/raj.json | head -c 200
```

His file is completely separate from yours. Different day, different flashcard
schedule, different error log.

---

## F. Make sure it is backed up

The sync folder is only as safe as your mirror. Find what your mirror unit
actually copies:

```bash
systemctl cat waleedcloud-mirror.service 2>/dev/null | grep -i 'ExecStart\|rsync'
```

If `~/waleedcloud/deutsch-sync` sits inside the source path, you are done. If it
does not, **move the sync folder into the covered path rather than editing the
mirror unit** — that keeps this whole thing additive, which was the point:

```bash
sudo systemctl stop t9-sync.service
mv ~/waleedcloud/deutsch-sync /path/that/is/already/mirrored/deutsch-sync
sudo nano /etc/t9-sync.env        # update T9_SYNC_DIR
sudo nano /etc/systemd/system/t9-sync.service   # update ReadWritePaths
sudo systemctl daemon-reload && sudo systemctl start t9-sync.service
```

The service also keeps its own history regardless: every upload copies the
previous version into `deutsch-sync/backups/<name>/`, keeping the last 30. So a
bad sync is recoverable within seconds, before the nightly mirror even runs.

---

## G. Add it to your `t9` command

Optional, and purely additive — one new case in your existing `t9` function:

```bash
deutsch)
    ssh waleedcloud '
      systemctl is-active t9-sync.service
      curl -s localhost:5051/health; echo
      ls -la ~/waleedcloud/deutsch-sync/*.json 2>/dev/null
      du -sh ~/waleedcloud/deutsch-sync
    '
    ;;
```

Then `t9 deutsch` shows you both learners' files and whether the service is
healthy.

---

## Troubleshooting

| Symptom | Cause |
|---|---|
| "Failed to fetch" in the browser | The address is `http://` not `https://`, or you gave Raj a `ts.net` **serve** address instead of a **funnel** one. Not a token problem. |
| Works for you, fails for Raj | Same thing: `tailscale serve` is private, `tailscale funnel` is public. Check `tailscale funnel status`. |
| 401 on every request | Token mismatch between the browser field and `/etc/t9-sync.env`. With nginx, also check the `proxy_set_header Authorization` line. |
| 404 on the first sync | Normal. No file exists for that name yet; the first upload creates it. |
| Service will not start | `T9_SYNC_TOKEN` is empty. It refuses to run without one, deliberately. `journalctl -u t9-sync.service -n 30 --no-pager` |
| Raj's link stopped working | The token changed, or you used a `trycloudflare.com` hostname that rotated. Issue a new setup link. |
| Both studied offline, worried about clashes | Nothing is lost. Sync merges rather than overwrites: days union, flashcards keep the most recent review, streaks keep the longest. Merging twice equals merging once. |

To revoke Raj's access entirely: change `T9_SYNC_TOKEN`, `sudo systemctl restart
t9-sync.service`, and generate a new setup link for yourself. His browser keeps
whatever it already downloaded but can no longer read or write the server.

## Removing all of it

```bash
sudo systemctl disable --now t9-sync.service
sudo rm /etc/systemd/system/t9-sync.service /etc/t9-sync.env
sudo systemctl daemon-reload
sudo tailscale funnel --https=443 off     # if you used C1
```

Progress stays in each browser and in `~/waleedcloud/deutsch-sync` until you
delete it. Nothing else on the Pi is affected, because nothing else was ever
touched.

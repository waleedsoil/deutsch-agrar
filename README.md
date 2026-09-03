# Deutsch für Agrar

A 48-week German course, A0 to B1, built for one specific person: an MSc student in Sustainable
International Agriculture who needs German for seminars, for the Bürgeramt, for field and warehouse
work, for the Führerschein, and for interviews where the technical questions come in German.

It is not a general beginners' course with farm words bolted on. The grammar spine is standard and
complete, but every reading text, speaking task and vocabulary deck is drawn from soil science, crop
production, university admin, German officialdom and hiring.

It is also built for a Marathi speaker specifically. English is the wrong middle language for German
grammar: English threw away grammatical gender, case endings, verb-final clauses and the तू/तुम्ही
distinction, and Marathi kept all four. Routing मराठी → English → German translates through the one
language that lacks exactly what German needs. Every week here carries a मराठीचा पूल note that maps the
German structure onto the Marathi one you already have — and says plainly where the bridge does not hold.

| Marathi | German | English |
|---|---|---|
| तीन लिंगं | der / die / das | nothing |
| षष्ठी — चा / ची / चे | Genitiv | 's, of |
| क्रियापद शेवटी | verb-final subordinate clauses | nothing |
| बेचाळीस = बे + चाळीस | zweiundvierzig | forty-two, reversed |
| तू / तुम्ही | du / Sie | you |
| मोठा, मोठी, मोठं | großer, große, großes | big |
| 'ने' in the transitive past | haben vs. sein | have only |
| कर्मणी: पेरला जातो | wird gesät | is sown |

**[SYLLABUS.md](SYLLABUS.md)** — the full week-by-week plan, readable without opening the site.
**[MARATHI.md](MARATHI.md)** — the Marathi bridge and all 48 weekly notes.
**[STORY.md](STORY.md)** — the sixteen story episodes and five model texts in full.
**[VOCABULARY.md](VOCABULARY.md)** — all 890 entries with articles, plurals, Marathi and examples.

---

## What the site does

- **Today** — opens on the exact day you are on. Tick the blocks, write notes, log the day, and the
  cursor moves on. Nothing to remember between sessions.
- **Syllabus** — all 48 weeks as a season strip; click any cell to read that week's plan day by day.
- **Vocabulary** — spaced repetition over 890 words in 14 decks. Decks unlock as you reach the week
  that uses them. Cards you fail come back the same session; cards you know come back in weeks.
- **कथा Story** — sixteen episodes following Nikhil, who arrives in Göttingen from Solapur with almost no
  German and spends a year getting to a job offer. Each episode is written at exactly the level you have
  reached and unlocks as you get there, with a glossary in English and Marathi, a note on the grammar it
  demonstrates, and two comprehension questions. Five fully worked model texts sit alongside it.
- **Tests** — a quiz for every week, ten cumulative checkpoints, and a der/die/das gender trainer.
- **Reference** — pronunciation notes written for a Marathi speaker, email templates, the interview
  question bank, connector tables, chart-description language, and the four German written text types.
- **Progress** — completion, streak, review-load forecast for the next 14 days, and the error log.

## Profiles and sync

The site opens by asking who is studying. Type a name — `Raj` opens Raj's course, `weed` opens yours.
Each name keeps its own day, its own flashcard schedule, its own error log. Capitalisation and spacing
do not matter: `Raj`, `raj` and ` RAJ ` are the same person.

By default a profile lives in one browser on one device. Turn on sync in **Progress → Sync across your
devices** and typing your name on any device picks up where you left off.

Sync never overwrites. Every cycle is pull → merge → push, and the merge is deliberately built so that
merging twice equals merging once:

| | rule |
|---|---|
| Completed days | union, keeping the earliest completion date |
| Ticked steps | OR together |
| Flashcards | the most recently reviewed copy wins |
| Quiz scores | best score and attempt count both take the max, never a sum |
| Notes | the most recent edit wins |
| Error log | union by entry |
| Streak | longest is a record and never drops; current belongs to whoever studied later |
| Cursor | whichever device is further into the course |

So if you study on the laptop and on the phone before either syncs, both days are kept. An empty or
brand-new remote file can never wipe local progress — that case is covered by a test.

### Providers

| Provider | Use when |
|---|---|
| This device only | the default, no network at all |
| WaleedCloud (your own Pi) | your own hardware, nothing leaves your tailnet. See [server/SETUP.md](server/SETUP.md) |
| GitHub secret gist | easiest — you already have a GitHub account, it is free, and CORS always works |
| WebDAV / Nextcloud | a self-hosted or personal cloud. Use an app password limited to one folder |
| REST / object storage | anything that will accept `GET` and `PUT` of a JSON file with a bearer token |

**One security fact you have to know.** This is a static site with no server, so any token you enter is
stored in your browser and sent from it. Anyone with access to the device can read it. Only ever use a
credential scoped to this one job — a gist-scope token, or a WebDAV app password limited to a single
folder — never your main account password, and revoke it if a device is lost. The token is stored per
device and is never written into this repo.

**If you sync to your own Pi, the address must be https.** The site is served from
`https://waleedsoil.github.io`, and a page loaded over HTTPS is not allowed to call `http://` — the
browser blocks it silently as mixed content. `tailscale serve` gives the Pi a real certificate and an
`https://…ts.net` address, which solves it. Every syncing device then has to be on the tailnet, phone
included. `server/SETUP.md` walks through it, and the service it installs is strictly additive: a new
process on a new port writing to a new folder, with nothing existing stopped or reconfigured.

If a connection test fails with "Failed to fetch", the server is refusing the browser rather than
refusing you: that is a CORS setting on the server side, not a wrong password. A secret gist avoids the
problem entirely.

---

## Put it on GitHub Pages

```bash
# 1. create an empty repo on github.com, then:
git init
git add .
git commit -m "German course"
git branch -M main
git remote add origin https://github.com/<your-username>/<repo>.git
git push -u origin main
```

Then on github.com: **Settings → Pages → Source: Deploy from a branch → Branch: `main`, folder: `/ (root)` → Save.**

A minute later it is live at `https://<your-username>.github.io/<repo>/`. Add that to your phone's home
screen and it opens like an app.

To run it locally instead:

```bash
python3 -m http.server 8000     # then open http://localhost:8000
```

It also works if you just double-click `index.html`, because the data is loaded as a plain script
rather than fetched.

---

## Repo layout

```
index.html            page shell
css/style.css         all styling
js/store.js           saving, streak, export and import
js/srs.js             the spaced-repetition scheduler
js/app.js             views and routing
data/kurs.js          generated course data, loaded by the page
data/kurs.json        the same data, readable and diffable
build/weeks.py        the 48 week specifications — edit this to change the course
build/vocab.py        the 14 vocabulary decks
build/quiz_bank.py    176 grammar questions, tagged by week
build/phrasebook.py   the reference pages
build/marathi.py      the Marathi bridge, 48 weekly notes, 301 Marathi glosses
build/story.py        16 story episodes and 5 model texts
server/t9_sync.py     optional sync service for your own machine (stdlib only)
server/SETUP.md     how to run it on the Pi behind Tailscale
build/gen.py          expands the specs into data/kurs.js
build/gen_docs.py     writes SYLLABUS.md and VOCABULARY.md
SYLLABUS.md           generated
MARATHI.md            generated
STORY.md              generated
VOCABULARY.md         generated
```

## Changing the course

Everything is authored in `build/`. Edit the Python, then regenerate:

```bash
cd build
python3 gen.py && python3 gen_docs.py
```

Commit the regenerated `data/` and `*.md` files along with your edit. Some things you will want to do:

- **Add words you meet in the wild.** Append lines to a deck in `build/vocab.py`, format
  `german | english | example sentence`. Nouns get their article and plural: `der Boden (Böden)`.
  This is the single highest-value edit — words you collected yourself are remembered better than
  words handed to you.
- **Fix my Marathi.** I wrote the Marathi in `build/marathi.py` and `build/story.py`. Where a phrasing
  reads stiffly or a gloss is off, change it — your ear is the authority, not mine, and a note in your
  own natural Marathi will stick better than one in someone else's.
- **Add a question you got wrong.** Append to `build/quiz_bank.py`, format
  `week | question | opt;opt;opt;opt | index_of_correct | explanation`.
- **Change a week.** Edit its entry in `build/weeks.py`. The seven day plans regenerate automatically
  from the weekly rhythm in `gen.py`.
- **Slow the course down.** If a week does not land, repeat it: on the Syllabus page open the week and
  press "Make this my current day".

## Backing up your progress

Progress lives in one browser. On the Progress page, **Download progress file** gives you a JSON
export. Commit it to this repo occasionally — you then have a dated history of the whole year, and
you can restore onto any machine with **Load a progress file**.

## Licence

The code and course structure here are yours to change and republish. External materials referenced in
the plan (Deutsche Welle, Goethe-Institut, telc, the Führerschein Fragenkatalog, agricultural
publications) belong to their publishers and are only linked to, never reproduced.

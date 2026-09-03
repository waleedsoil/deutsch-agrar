# -*- coding: utf-8 -*-
"""Builds data/*.js from the hand-authored specs."""

import json, os, sys, io, re

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)

from weeks import WEEKS
from vocab import DECKS, DECK_META
from quiz_bank import BANK
from phrasebook import PAGES
from marathi import BRIDGE, WEEK_MR, GLOSS
from story import EPISODES, ESSAYS

# ---------------------------------------------------------------- vocab ----
vocab = []
vid = 0
for deck, blob in DECKS.items():
    for line in blob.strip().splitlines():
        line = line.strip()
        if not line:
            continue
        parts = [p.strip() for p in line.split("|")]
        de, en = parts[0], parts[1]
        ex = parts[2] if len(parts) > 2 else ""
        art = ""
        m = re.match(r"^(der|die|das)\s+(.+)$", de)
        base = de
        if m:
            art, base = m.group(1), m.group(2)
        pl = ""
        m2 = re.search(r"\(([^)]*)\)\s*$", base)
        if m2:
            pl = m2.group(1)
            base = base[:m2.start()].strip()
        vid += 1
        vocab.append({
            "id": "v%d" % vid, "deck": deck, "art": art, "word": base,
            "pl": pl, "en": en, "ex": ex,
            "full": (art + " " + base).strip(),
            "mr": GLOSS.get(base, ""),
        })

deck_meta = {k: {"name": v[0], "desc": v[1], "level": v[2],
                 "count": sum(1 for x in vocab if x["deck"] == k)}
             for k, v in DECK_META.items()}

# ----------------------------------------------------------------- quiz ----
quiz = []
qid = 0
for line in BANK.strip().splitlines():
    line = line.strip()
    if not line:
        continue
    parts = [p.strip() for p in line.split("|")]
    if len(parts) < 5:
        raise SystemExit("bad quiz line: " + line)
    wk = int(parts[0])
    opts = [o.strip() for o in parts[2].split(";")]
    qid += 1
    quiz.append({"id": "q%d" % qid, "w": wk, "q": parts[1], "opts": opts,
                 "a": int(parts[3]), "why": parts[4]})

# ----------------------------------------------------------- day rhythm ----
# Each day: three core blocks (60 min) plus stretch blocks (up to 90 min).
def days_for(spec):
    w = spec["w"]
    decks = spec["decks"]
    d0, d1 = decks[0], decks[-1]
    g = spec["grammar"]

    def G(i):
        return g[i] if i < len(g) else g[-1]

    per = max(6, round(spec["newwords"] / 4))
    plan = [
    # --- Day 1 -------------------------------------------------------------
    ("Neue Struktur", "Meet this week's grammar cold and write your own rule card.", [
        ("Warm-up: review yesterday's flashcards until the queue is empty.", 15, True),
        ("Study the grammar point: %s. Write the rule in your own words, in English, in one sentence." % G(0), 25, True),
        ("Second point: %s. Make 6 example sentences of your own — all about your studies or your work." % G(1), 20, True),
        ("Read the third and fourth points below and mark anything you do not understand. Do not try to master them today.", 30, False),
    ]),
    # --- Day 2 -------------------------------------------------------------
    ("Drill", "Automate the structure until it is faster than thinking.", [
        ("Flashcard review.", 15, True),
        ("Grammar drill: transform 20 sentences using %s. Say each one out loud before you write it." % G(0), 25, True),
        ("Add %d new words from the %s deck. Read each example sentence aloud twice." % (per, d0), 20, True),
        ("Weekly quiz, attempt 1. Log every wrong answer in the error log — the reason, not just the answer.", 30, False),
    ]),
    # --- Day 3 -------------------------------------------------------------
    ("Hören", "Train your ear before your mouth. Input first.", [
        ("Flashcard review.", 15, True),
        ("Listen to a 5–8 minute German clip twice: once for the gist, once with the transcript. Mark 10 unknown words.", 25, True),
        ("Add %d new words from the %s deck." % (per, d1), 20, True),
        ("Shadowing: play 90 seconds of the clip and speak along, half a second behind, five times. Record the fifth attempt.", 30, False),
    ]),
    # --- Day 4 -------------------------------------------------------------
    ("Fachtext", "Read German written for Germans in your own subject.", [
        ("Flashcard review.", 15, True),
        ("Read a short professional text (200–400 words) on: %s" % spec["agrar"], 25, True),
        ("Pull 15 words and compound nouns out of the text. Split every compound into its parts before you translate it.", 20, True),
        ("Rewrite the three hardest sentences from the text in simpler German that you could actually say.", 30, False),
    ]),
    # --- Day 5 -------------------------------------------------------------
    ("Schreiben", "Produce something real that a German person could receive.", [
        ("Flashcard review.", 15, True),
        ("Writing task: %s" % spec["write"], 30, True),
        ("Self-correct with the checklist: verb position 2, verb-final in subordinate clauses, all nouns capitalised, every article checked, adjective endings checked.", 15, True),
        ("Add %d new words from the %s deck." % (per, d0), 30, False),
    ]),
    # --- Day 6 -------------------------------------------------------------
    ("Sprechen", "The only day that matters for interviews. No skipping.", [
        ("Flashcard review.", 15, True),
        ("Two-minute monologue, recorded, no notes, on: %s" % spec["uni"], 25, True),
        ("Role-play out loud, both parts: %s" % spec["alltag"], 20, True),
        ("Listen back to the recording. Count filler sounds. Re-record once and beat your own count.", 30, False),
    ]),
    # --- Day 7 -------------------------------------------------------------
    ("Wiederholung", "Consolidate. Do not learn anything new today.", [
        ("Full flashcard review, including everything the algorithm has queued.", 20, True),
        ("Weekly quiz, attempt 2. Aim for 90 percent.", 20, True),
        ("Read your error log for this week aloud. Say the correct version of each mistake three times.", 20, True),
        ("Free German: 20 minutes of anything you enjoy — a podcast, a video, a chat. No dictionary.", 30, False),
    ]),
    ]

    out = []
    for i, (label, sub, blocks) in enumerate(plan, start=1):
        out.append({
            "n": i, "label": label, "sub": sub,
            "blocks": [{"t": t, "min": m, "core": c} for (t, m, c) in blocks],
            "core": sum(m for (_, m, c) in blocks if c),
            "full": sum(m for (_, m, _c) in blocks),
        })
    return out


PHASE_NAME = {"A1": "Foundation", "A2": "Working German",
              "B1": "Professional German", "KONS": "Consolidation"}

curriculum = []
for spec in WEEKS:
    curriculum.append({
        "w": spec["w"],
        "phase": spec["phase"],
        "phaseName": PHASE_NAME[spec["phase"]],
        "title": spec["title"],
        "de": spec["de"],
        "goal": spec["goal"],
        "grammar": spec["grammar"],
        "decks": spec["decks"],
        "newwords": spec["newwords"],
        "tracks": {"uni": spec["uni"], "alltag": spec["alltag"],
                   "agrar": spec["agrar"], "job": spec["job"]},
        "cando": spec["cando"],
        "write": spec["write"],
        "res": spec["res"],
        "checkpoint": spec.get("checkpoint"),
        "mr": WEEK_MR.get(spec["w"], ""),
        "days": days_for(spec),
    })

checkpoints = []
for c in curriculum:
    if c["checkpoint"]:
        checkpoints.append({"n": c["checkpoint"], "w": c["w"], "title": c["title"],
                            "phase": c["phase"]})

data = {
    "meta": {
        "weeks": len(curriculum),
        "days": len(curriculum) * 7,
        "vocab": len(vocab),
        "quiz": len(quiz),
        "story": len(EPISODES),
        "essays": len(ESSAYS),
        "glossed": sum(1 for v in vocab if v["mr"]),
        "built": "generated by build/gen.py",
    },
    "curriculum": curriculum,
    "checkpoints": checkpoints,
    "vocab": vocab,
    "deckMeta": deck_meta,
    "quiz": quiz,
    "pages": [BRIDGE] + PAGES,
    "story": EPISODES,
    "essays": ESSAYS,
}

os.makedirs(os.path.join(ROOT, "data"), exist_ok=True)
js = "window.KURS = " + json.dumps(data, ensure_ascii=False, separators=(",", ":")) + ";\n"
with io.open(os.path.join(ROOT, "data", "kurs.js"), "w", encoding="utf-8") as f:
    f.write(js)
with io.open(os.path.join(ROOT, "data", "kurs.json"), "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=1)

print("weeks   ", len(curriculum))
print("days    ", len(curriculum) * 7)
print("vocab   ", len(vocab))
print("quiz    ", len(quiz))
print("pages   ", len(PAGES) + 1)
print("story   ", len(EPISODES), "episodes,", sum(len(e["text"].split()) for e in EPISODES), "German words")
print("essays  ", len(ESSAYS))
print("mr notes", len(WEEK_MR), "weeks")
print("mr gloss", data["meta"]["glossed"], "of", len(vocab), "words")
print("bytes   ", len(js))
missing = sorted({d for c in curriculum for d in c["decks"]} - set(DECKS))
print("missing decks:", missing if missing else "none")
qweeks = {q["w"] for q in quiz}
print("weeks without quiz items:", sorted(set(range(1, 49)) - qweeks))

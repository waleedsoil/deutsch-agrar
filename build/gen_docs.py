# -*- coding: utf-8 -*-
"""Writes the human-readable syllabus and word list from the same source data."""

import json, os, io

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
data = json.load(io.open(os.path.join(ROOT, "data", "kurs.json"), encoding="utf-8"))

C = data["curriculum"]
PHASES = [("A1", "Phase 1 — Foundation (weeks 1–10)",
           "From no German to handling a day: introducing yourself, times and prices, instructions, the accusative and dative, and the past tense. Ends with a full A1 mock exam."),
          ("A2", "Phase 2 — Working German (weeks 11–24)",
           "The phase that makes you employable in a field or warehouse job and functional at the Bürgeramt: adjective endings, subordinate clauses, the passive, polite writing. Ends with a full A2 mock exam."),
          ("B1", "Phase 3 — Professional German (weeks 25–44)",
           "Relative clauses, academic register, argument, presentations, the German application dossier, two full interview weeks and a Führerschein sprint."),
          ("KONS", "Phase 4 — Consolidation (weeks 45–48)",
           "Error surgery, a timed B1 mock in all four skills, unmodified professional texts, and the B2 plan.")]

out = []
w = out.append

w("# Syllabus — German A0 to B1 in 48 weeks\n")
w("Built for an MSc student in Sustainable International Agriculture: every week carries the same grammar spine, ")
w("but the vocabulary, texts and speaking tasks come from soil science, crop production, university life, ")
w("fieldwork, German officialdom and job interviews.\n")
w("\n## The numbers\n")
w("| | |\n|---|---|\n")
w("| Weeks | 48 |\n")
w("| Days | %d, seven days a week |\n" % data["meta"]["days"])
w("| Daily commitment | 60 minutes core, 90 minutes full |\n")
w("| Total hours | 336 at the 60-minute setting, 504 at 90 |\n")
w("| Vocabulary | %d entries across 14 decks, every noun with article and plural |\n" % data["meta"]["vocab"])
w("| Grammar questions | %d, tagged by week, reused cumulatively at checkpoints |\n" % data["meta"]["quiz"])
w("| Checkpoints | 10, at weeks 5, 10, 15, 20, 25, 30, 35, 40, 45 and 48 |\n")
w("| Story | %d episodes, %d words of German, one every three weeks |\n" % (data["meta"]["story"], sum(len(e["text"].split()) for e in data["story"])))
w("| Model texts | %d fully worked, with Marathi commentary |\n" % data["meta"]["essays"])
w("| मराठी | a bridge note for all 48 weeks, %d words glossed in Marathi |\n" % data["meta"]["glossed"])
w("\nThe Goethe-Institut estimates 350–650 teaching units of 45 minutes to reach B1 from zero. ")
w("At 60 minutes a day this course delivers 448 units; at 90 it delivers 672. The plan is therefore ")
w("realistic at the lower setting and comfortable at the higher one — provided the seven-day rhythm holds.\n")

w("\n## The daily rhythm\n\n")
w("| Day | Focus | What happens |\n|---|---|---|\n")
w("| 1 | Neue Struktur | Meet the week's grammar. Write the rule in your own words. No drilling yet. |\n")
w("| 2 | Drill | Twenty transformations, spoken before written. First quiz attempt. |\n")
w("| 3 | Hören | Listen twice, then shadow 90 seconds five times and record the fifth. |\n")
w("| 4 | Fachtext | An unmodified German text in your own subject. Compounds split before translated. |\n")
w("| 5 | Schreiben | Produce something a German person could actually receive. |\n")
w("| 6 | Sprechen | Recorded two-minute monologue plus a role-play. |\n")
w("| 7 | Wiederholung | Nothing new. Review, second quiz attempt, error log read aloud. |\n")
w("\nEvery day opens with a spaced-repetition review. Each day has three core blocks (60 minutes) ")
w("and one stretch block (a further 30).\n")

w("\n## मराठीतून, इंग्रजीतून नाही\n\n")
w("English is the wrong middle language for German grammar. English threw away grammatical gender, ")
w("case endings, verb-final clauses and the तू/तुम्ही distinction — Marathi kept all four. Every week ")
w("carries a मराठीचा पूल note that maps the German structure onto the Marathi one you already own, ")
w("and says plainly where the bridge does not hold. See MARATHI.md for the full map.\n\n")
w("| Marathi | German | English |\n|---|---|---|\n")
w("| तीन लिंगं | der / die / das | nothing |\n")
w("| कर्म (ला/स) | Akkusativ | nothing |\n")
w("| षष्ठी (चा/ची/चे) | Genitiv | 's, of |\n")
w("| क्रियापद शेवटी | verb-final subordinate clauses | nothing |\n")
w("| बेचाळीस = बे + चाळीस | zweiundvierzig | forty-two (reversed) |\n")
w("| तू / तुम्ही | du / Sie | you |\n")
w("| मोठा, मोठी, मोठं | großer, große, großes | big |\n")
w("| 'ने' in transitive past | haben vs. sein | have only |\n")
w("| कर्मणी: पेरला जातो | wird gesät | is sown |\n")
w("\n## The four parallel tracks\n\n")
w("| Track | Covers |\n|---|---|\n")
w("| Studies | Seminars, module handbooks, deadlines, supervisors, HiWi work, thesis language |\n")
w("| Daily life | Registration, housing, insurance, doctor, bank, phone calls, complaints |\n")
w("| Agriculture | Soil, crops, livestock, machinery, farm economics and policy |\n")
w("| Work and interviews | Field and warehouse instructions, applications, interviews, contracts |\n")

for code, heading, blurb in PHASES:
    w("\n---\n\n## %s\n\n%s\n" % (heading, blurb))
    for c in [x for x in C if x["phase"] == code]:
        cp = "  **Checkpoint %d.**" % c["checkpoint"] if c["checkpoint"] else ""
        w("\n### Week %d — %s\n" % (c["w"], c["title"]))
        w("*%s*%s\n\n" % (c["de"], cp))
        w("%s\n\n" % c["goal"])
        w("**Grammar**\n\n")
        for g in c["grammar"]:
            w("- %s\n" % g)
        w("\n**Tracks**\n\n")
        w("- Studies: %s\n" % c["tracks"]["uni"])
        w("- Daily life: %s\n" % c["tracks"]["alltag"])
        w("- Agriculture: %s\n" % c["tracks"]["agrar"])
        w("- Work: %s\n" % c["tracks"]["job"])
        w("\n**Vocabulary** — %d new words from: %s\n" %
          (c["newwords"], ", ".join(data["deckMeta"][d]["name"] for d in c["decks"])))
        w("\n**By Sunday**\n\n")
        for x in c["cando"]:
            w("- %s\n" % x)
        w("\n**Written output** — %s\n" % c["write"])
        w("\n**Resources** — %s\n" % "; ".join(c["res"]))
        if c.get("mr"):
            w("\n> **मराठीचा पूल** — %s\n" % c["mr"])
        for ep in data["story"]:
            if ep["w"] == c["w"]:
                w("\n> **कथा, भाग %d — %s** (%s) unlocks this week.\n" % (ep["n"], ep["title"], ep["mr_title"]))
        for es in data["essays"]:
            if es["w"] == c["w"]:
                w("\n> **Model text — %s** (%s) unlocks this week.\n" % (es["title"], es["kind"]))

w("\n---\n\n## Checkpoints\n\n")
w("Checkpoints are cumulative: checkpoint 6 draws on everything from week 1 to week 30, not just the last block. ")
w("Below 75 percent, repeat the phase's grammar days before continuing.\n\n")
w("| # | After week | Covers | Format |\n|---|---|---|---|\n")
fmt = {2: "Full A1 mock, four skills", 4: "Full A2 mock, four skills",
       7: "B1 mock, part 1", 9: "Grammar audit and error surgery", 10: "Final cumulative exam"}
for cp in data["checkpoints"]:
    w("| %d | %d | %s | %s |\n" % (cp["n"], cp["w"], cp["title"], fmt.get(cp["n"], "25 cumulative questions")))

io.open(os.path.join(ROOT, "SYLLABUS.md"), "w", encoding="utf-8").write("".join(out))

# ------------------------------------------------------------- MARATHI ----
bridge = data["pages"][0]
m = ["# %s\n\n%s\n" % (bridge["title"], bridge["intro"])]
for sec in bridge["sections"]:
    m.append("\n## %s\n\n" % sec["h"])
    if sec.get("rows"):
        m.append("| | |\n|---|---|\n")
        for r in sec["rows"]:
            m.append("| %s | %s |\n" % (r[0], r[1].replace("\n", " ")))
    if sec.get("text"):
        m.append("```\n%s\n```\n" % sec["text"])
m.append("\n## आठवड्यागणिक नोंदी — the week-by-week notes\n\n")
for c in C:
    m.append("**Week %d — %s**\n\n%s\n\n" % (c["w"], c["title"], c.get("mr", "")))
io.open(os.path.join(ROOT, "MARATHI.md"), "w", encoding="utf-8").write("".join(m))

# --------------------------------------------------------------- STORY ----
st = ["# कथा — Nikhil's year\n\nSixteen episodes, one every three weeks, each written at the level reached in that week. Episode 1 uses only the present tense; episode 16 uses everything up to B1. Read for the story first and the grammar second.\n\n"]
st.append("| # | Week | Title | मराठी | Level |\n|---|---|---|---|---|\n")
for e in data["story"]:
    st.append("| %d | %d | %s | %s | %s |\n" % (e["n"], e["w"], e["title"], e["mr_title"], e["level"]))
st.append("\n## Model texts\n\n| Week | Title | Kind |\n|---|---|---|\n")
for e in data["essays"]:
    st.append("| %d | %s | %s |\n" % (e["w"], e["title"], e["kind"]))
for e in data["story"]:
    st.append("\n---\n\n## Folge %d — %s (%s)\n\n*unlocks in week %d, level %s*\n\n%s\n\n**Wortschatz**\n\n| German | English | मराठी |\n|---|---|---|\n" % (
        e["n"], e["title"], e["mr_title"], e["w"], e["level"], e["text"]))
    for g in e["gloss"]:
        st.append("| %s | %s | %s |\n" % (g[0], g[1], g[2]))
    st.append("\n> **व्याकरणाची नोंद** — %s\n" % e["mr"])
for e in data["essays"]:
    st.append("\n---\n\n## Model text — %s (%s)\n\n*%s, unlocks in week %d*\n\n%s\n\n> **रचना** — %s\n\n**Phrases to lift wholesale**\n\n" % (
        e["title"], e["mr_title"], e["kind"], e["w"], e["text"], e["mr"]))
    for x in e["steal"]:
        st.append("- %s\n" % x)
io.open(os.path.join(ROOT, "STORY.md"), "w", encoding="utf-8").write("".join(st))
print("MARATHI.md    ", os.path.getsize(os.path.join(ROOT, "MARATHI.md")), "bytes")
print("STORY.md      ", os.path.getsize(os.path.join(ROOT, "STORY.md")), "bytes")

# ---------------------------------------------------------------- vocab ---
v = ["# Vocabulary\n\n%d entries. Nouns carry article and plural, because a noun learned without its article is a noun you will get wrong forever.\n" % data["meta"]["vocab"]]
for deck, meta in data["deckMeta"].items():
    v.append("\n## %s (%s, %d words)\n\n%s\n\n" % (meta["name"], meta["level"], meta["count"], meta["desc"]))
    v.append("| German | English | मराठी | Example |\n|---|---|---|---|\n")
    for e in data["vocab"]:
        if e["deck"] != deck:
            continue
        de = e["full"] + (" (%s)" % e["pl"] if e["pl"] else "")
        v.append("| %s | %s | %s | %s |\n" % (de, e["en"], e.get("mr", ""), e["ex"].replace("|", "/")))
io.open(os.path.join(ROOT, "VOCABULARY.md"), "w", encoding="utf-8").write("".join(v))

print("SYLLABUS.md   ", os.path.getsize(os.path.join(ROOT, "SYLLABUS.md")), "bytes")
print("VOCABULARY.md ", os.path.getsize(os.path.join(ROOT, "VOCABULARY.md")), "bytes")

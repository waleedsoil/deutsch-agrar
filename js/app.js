(function () {
"use strict";

const K = window.KURS;
const S = window.Store;
const R = window.SRS;
const $ = (s, r) => (r || document).querySelector(s);
const $$ = (s, r) => Array.from((r || document).querySelectorAll(s));

const esc = (t) => String(t == null ? "" : t)
  .replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;").replace(/"/g, "&quot;");

const VIEWS = [
  ["today",    "Today",      "the next thing to do"],
  ["plan",     "Syllabus",   "all 48 weeks"],
  ["vocab",    "Vocabulary", "flashcards"],
  ["story",    "कथा Story",  "16 episodes"],
  ["test",     "Tests",      "quizzes and checkpoints"],
  ["phrases",  "Reference",  "phrases and templates"],
  ["progress", "Progress",   "stats and error log"],
  ["guide",    "How to use", "method and resources"]
];

let view = "today";
let browseWeek = 1, browseDay = 1;

/* ------------------------------------------------------------ helpers -- */
const week = (n) => K.curriculum[n - 1];
const key = (w, d) => w + "-" + d;
const isDone = (w, d) => !!S.get().done[key(w, d)];

function unlockedDecks(uptoWeek) {
  const set = new Set();
  for (let i = 1; i <= Math.min(uptoWeek, K.curriculum.length); i++)
    week(i).decks.forEach(d => set.add(d));
  set.add("verben");
  return set;
}

function weekProgress(w) {
  let n = 0;
  for (let d = 1; d <= 7; d++) if (isDone(w, d)) n++;
  return n;
}

function totalDone() {
  return Object.keys(S.get().done).length;
}

function phaseClass(p) { return p.toLowerCase(); }

function toast(msg) {
  const el = document.createElement("div");
  el.className = "toast";
  el.textContent = msg;
  document.body.appendChild(el);
  setTimeout(() => el.remove(), 2200);
}

function advanceCursor() {
  const c = S.get().cursor;
  if (c.d < 7) c.d++;
  else if (c.w < K.curriculum.length) { c.w++; c.d = 1; }
  S.save();
}

/* --------------------------------------------------------------- rail -- */
function renderRail() {
  const nav = $("#railnav");
  nav.innerHTML = VIEWS.map(([id, label, tag]) =>
    `<button data-view="${id}" aria-current="${id === view}">
       <span>${esc(label)}</span><span class="tag">${esc(tag)}</span></button>`).join("");
  nav.onclick = (e) => {
    const b = e.target.closest("button[data-view]");
    if (!b) return;
    if (b.dataset.view === "test") { testTarget = null; quizState = null; }
    if (b.dataset.view === "phrases") pageId = null;
    if (b.dataset.view === "story") epOpen = null;
    go(b.dataset.view);
  };

  const st = S.get().streak;
  const done = totalDone();
  $("#streakbox").innerHTML =
    `<div><b>${st.count}</b><small>day streak &middot; best ${st.longest}</small></div>
     <div><b>${done}</b><small>of ${K.meta.days} days done</small></div>`;

  $("#whobox").innerHTML =
    `<span style="flex:1"><b>${esc(S.currentName())}</b></span>
     <button data-act="switch">switch</button>`;
  $("#whobox").onclick = (e) => {
    if (e.target.closest("[data-act=switch]")) {
      S.saveNow().then(() => { S.closeProfile(); renderGate(); });
    }
  };
  renderSyncBar();
}

/* -------------------------------------------------------- season strip - */
function renderStrip(host, activeWeek, onClick) {
  const cells = K.curriculum.map(c => {
    const p = weekProgress(c.w);
    const cls = ["cell", p === 7 ? "filled" : p > 0 ? "partial" : "",
                 c.w === activeWeek ? "here" : "", c.checkpoint ? "cp" : ""].join(" ");
    return `<button class="${cls}" data-phase="${c.phase}" data-w="${c.w}"
      title="Week ${c.w} — ${esc(c.title)} (${p}/7 days)"></button>`;
  }).join("");

  host.innerHTML = `<div class="strip-wrap">
    <div class="strip">${cells}</div>
    <div class="striplegend">
      <span><i style="background:var(--a1)"></i>A1, weeks 1–10</span>
      <span><i style="background:var(--a2)"></i>A2, weeks 11–24</span>
      <span><i style="background:var(--b1)"></i>B1, weeks 25–44</span>
      <span><i style="background:var(--kons)"></i>Consolidation, weeks 45–48</span>
      <span>A dot marks a checkpoint week.</span>
    </div></div>`;

  host.querySelector(".strip").onclick = (e) => {
    const b = e.target.closest(".cell");
    if (b && onClick) onClick(+b.dataset.w);
  };
}

/* -------------------------------------------------------------- TODAY -- */
function renderToday() {
  const st = S.get();
  const w = st.cursor.w, d = st.cursor.d;
  const c = week(w);
  const day = c.days[d - 1];
  const k = key(w, d);
  const ticks = st.blocks[k] || (st.blocks[k] = day.blocks.map(() => false));
  const mode = st.settings.mode;

  const blocks = day.blocks
    .map((b, i) => ({ b, i }))
    .filter(x => mode === 90 || x.b.core);

  const totalMin = blocks.reduce((a, x) => a + x.b.min, 0);
  const doneMin = blocks.reduce((a, x) => a + (ticks[x.i] ? x.b.min : 0), 0);
  const allTicked = blocks.every(x => ticks[x.i]);

  const cpBanner = c.checkpoint ? `
    <div class="flat" style="border-color:var(--clay);background:var(--ochre-soft);margin-bottom:16px">
      <b>Checkpoint week.</b> Checkpoint ${c.checkpoint} covers everything from week 1 to week ${w}.
      Sit it on day 7 and log the score.
      <div class="btnrow" style="margin-top:10px"><button class="btn ghost" data-act="gotest">Open checkpoint ${c.checkpoint}</button></div>
    </div>` : "";

  const showWelcome = !st.settings.onboarded && !isDone(w, d) && totalDone() === 0;

  $("#today").innerHTML = `
    ${showWelcome ? `
    <div class="card" style="border-color:var(--leaf);background:var(--leaf-soft);margin-bottom:18px">
      <h3 style="margin-bottom:8px">How this page works</h3>
      <p style="margin-bottom:6px">Everything below is <b>today's lesson</b> — nothing else to find, this is the whole thing.</p>
      <ol style="margin:0 0 10px 1.1em;padding:0;line-height:1.7">
        <li>Read the heading — that's today's topic.</li>
        <li>Work through the checklist in the card below, top to bottom. Tick each step as you finish it.</li>
        <li>Press <b>Finish this day</b> at the bottom of that card. That's what moves you to tomorrow.</li>
      </ol>
      <p style="margin-bottom:0;color:var(--ink-2)">The Marathi note further down explains today's grammar in Marathi terms.
        Vocabulary, कथा Story, and Tests are separate tabs on the left for when you want them —
        you don't need them to finish today.</p>
      <div class="btnrow"><button class="btn" data-act="dismiss-welcome">Got it, hide this</button></div>
    </div>` : ""}
    <div class="eyebrow">Week ${w} of 48 &middot; day ${d} of 7 &middot; ${esc(c.phaseName)}</div>
    <h1>${esc(day.label)}: ${esc(c.title)}</h1>
    <p class="lede">${esc(day.sub)} ${esc(c.goal)}</p>

    <div id="strip-today"></div>
    ${cpBanner}

    <div class="card">
      <div style="display:flex;justify-content:space-between;align-items:baseline;gap:12px;flex-wrap:wrap">
        <h2>${esc(c.de)}</h2>
        <span class="pill ${phaseClass(c.phase)}">${esc(c.phase)}</span>
      </div>
      <ul class="blocklist">
        ${blocks.map(x => `
          <li class="${x.b.core ? "" : "stretch"} ${ticks[x.i] ? "ticked" : ""}">
            <input type="checkbox" data-i="${x.i}" ${ticks[x.i] ? "checked" : ""}
                   aria-label="Mark step complete">
            <span class="txt">${esc(x.b.t)}</span>
            <span class="mins">${x.b.min} min</span>
          </li>`).join("")}
      </ul>
      <div class="bar" style="margin-top:14px"><i style="width:${Math.round(doneMin / totalMin * 100)}%"></i></div>
      <div class="btnrow">
        <button class="btn ${allTicked ? "leaf" : ""}" data-act="finish">
          ${isDone(w, d) ? "Day already logged — go to next day" : "Finish this day"}</button>
        <button class="btn ghost" data-act="vocab">Flashcards</button>
        <button class="btn ghost" data-act="quiz">Week ${w} quiz</button>
        <span style="color:var(--ink-3);font-size:.85rem">${doneMin} of ${totalMin} minutes ticked</span>
      </div>
    </div>

    <div class="sec">
      <h2>Notes for today</h2>
      <p class="lede">Sentences you built, words you could not remember, anything a German person corrected.</p>
      <textarea id="notes" placeholder="Write in German where you can.">${esc((st.notes[k] || {}).t || "")}</textarea>
      <div class="btnrow">
        <input type="text" id="errin" placeholder="A mistake you made today" style="flex:1;min-width:220px">
        <button class="btn ghost" data-act="adderr">Add to error log</button>
      </div>
    </div>

    <div class="sec">
      <h2>This week in context</h2>
      <div class="mrbox">
        <h4>मराठीचा पूल — week ${w}</h4>
        <div class="mr">${esc(c.mr)}</div>
      </div>
      <div class="card">
        <h3>Grammar</h3>
        <ul class="plain">${c.grammar.map(g => `<li>${esc(g)}</li>`).join("")}</ul>
      </div>
      <div class="card">
        <h3>The four tracks</h3>
        <div class="grid2" style="margin-top:10px">
          <div class="trackbox"><h4>Studies</h4>${esc(c.tracks.uni)}</div>
          <div class="trackbox"><h4>Daily life</h4>${esc(c.tracks.alltag)}</div>
          <div class="trackbox"><h4>Agriculture</h4>${esc(c.tracks.agrar)}</div>
          <div class="trackbox"><h4>Work and interviews</h4>${esc(c.tracks.job)}</div>
        </div>
      </div>
      <div class="card">
        <h3>By Sunday you can say</h3>
        <ul class="plain">${c.cando.map(x => `<li>${esc(x)}</li>`).join("")}</ul>
        <p style="margin-top:12px;color:var(--ink-2)"><b>Resources:</b> ${c.res.map(esc).join(" &middot; ")}</p>
      </div>
    </div>`;

  renderStrip($("#strip-today"), w, (n) => { browseWeek = n; browseDay = 1; go("plan"); });

  $("#today").onchange = (e) => {
    const cb = e.target.closest("input[type=checkbox][data-i]");
    if (cb) {
      ticks[+cb.dataset.i] = cb.checked;
      S.save();
      renderToday();
    }
  };

  const notes = $("#notes");
  notes.oninput = (() => { S.get().notes[k] = { t: notes.value, at: S.now() }; S.save(); });

  $("#today").onclick = (e) => {
    const b = e.target.closest("button[data-act]");
    if (!b) return;
    const a = b.dataset.act;
    if (a === "finish") {
      if (!isDone(w, d)) {
        S.get().done[k] = S.todayISO();
        S.touchStreak();
        toast("Day " + d + " of week " + w + " logged.");
      }
      advanceCursor();
      renderRail();
      renderToday();
      window.scrollTo(0, 0);
    }
    if (a === "vocab") go("vocab");
    if (a === "quiz") { quizState = null; testTarget = { kind: "week", w }; go("test"); }
    if (a === "gotest") { quizState = null; testTarget = { kind: "cp", n: c.checkpoint, w }; go("test"); }
    if (a === "dismiss-welcome") {
      S.get().settings.onboarded = true; S.save(); renderToday();
    }
    if (a === "adderr") {
      const v = $("#errin").value.trim();
      if (v) {
        S.get().errors.unshift({ id: S.now() + "|" + v, text: v, w, ts: S.todayISO() });
        S.save();
        $("#errin").value = "";
        toast("Added to the error log.");
      }
    }
  };
}

/* --------------------------------------------------------------- PLAN -- */
function renderPlan() {
  const c = week(browseWeek);
  $("#plan").innerHTML = `
    <div class="eyebrow">The whole route, A0 to B1</div>
    <h1>48 weeks, 336 days</h1>
    <p class="lede">Seven days a week at 60 minutes is 336 hours; at 90 minutes it is 504.
      That is the range the Goethe-Institut gives for reaching B1 from zero. Pick a cell to open the week.</p>
    <div id="strip-plan"></div>

    <div class="card" style="margin-top:20px">
      <div style="display:flex;justify-content:space-between;align-items:baseline;gap:10px;flex-wrap:wrap">
        <h2>Week ${c.w} &middot; ${esc(c.title)}</h2>
        <span>
          <span class="pill ${phaseClass(c.phase)}">${esc(c.phase)}</span>
          ${c.checkpoint ? `<span class="pill cp">Checkpoint ${c.checkpoint}</span>` : ""}
        </span>
      </div>
      <p style="color:var(--ink-3);margin:2px 0 10px">${esc(c.de)}</p>
      <p>${esc(c.goal)}</p>
      <div class="daytabs">${c.days.map(d =>
        `<button data-d="${d.n}" aria-current="${d.n === browseDay}"
          class="${isDone(c.w, d.n) ? "done" : ""}">Day ${d.n} &middot; ${esc(d.label)}</button>`).join("")}</div>
      <ul class="blocklist">
        ${c.days[browseDay - 1].blocks.map(b =>
          `<li class="${b.core ? "" : "stretch"}"><span class="txt">${esc(b.t)}</span>
           <span class="mins">${b.min} min</span></li>`).join("")}
      </ul>
      <div class="btnrow">
        <button class="btn ghost" data-act="jump">Make this my current day</button>
        <span style="color:var(--ink-3);font-size:.85rem">
          ${c.days[browseDay - 1].core} min core &middot; ${c.days[browseDay - 1].full} min full</span>
      </div>
    </div>

    <div class="sec">
      <h2>All weeks</h2>
      ${K.curriculum.map(x => `
        <div class="weekrow" data-w="${x.w}">
          <span class="wn">${x.w}</span>
          <span class="wt">${esc(x.title)}<small>${esc(x.de)}</small></span>
          <span class="pill ${phaseClass(x.phase)}">${esc(x.phase)}</span>
          <span style="color:var(--ink-3);font-size:.8rem;width:34px;text-align:right">${weekProgress(x.w)}/7</span>
        </div>`).join("")}
    </div>`;

  renderStrip($("#strip-plan"), browseWeek, (n) => { browseWeek = n; browseDay = 1; renderPlan(); });

  $("#plan").onclick = (e) => {
    const row = e.target.closest(".weekrow");
    if (row) { browseWeek = +row.dataset.w; browseDay = 1; renderPlan(); window.scrollTo(0, 0); return; }
    const tab = e.target.closest(".daytabs button");
    if (tab) { browseDay = +tab.dataset.d; renderPlan(); return; }
    const b = e.target.closest("button[data-act=jump]");
    if (b) {
      S.get().cursor = { w: browseWeek, d: browseDay };
      S.save();
      toast("Current day set to week " + browseWeek + ", day " + browseDay + ".");
      go("today");
    }
  };
}

/* -------------------------------------------------------------- VOCAB -- */
let session = null, cardIdx = 0, revealed = false, deckFilter = "auto";

function startSession() {
  const st = S.get();
  let decks;
  if (deckFilter === "auto") decks = unlockedDecks(st.cursor.w);
  else decks = new Set([deckFilter]);
  session = R.buildSession(K.vocab, decks, st.settings.newPerDay);
  cardIdx = 0;
  revealed = false;
}

function renderVocab() {
  const st = S.get();
  const decks = deckFilter === "auto" ? unlockedDecks(st.cursor.w) : new Set([deckFilter]);
  const cnt = R.counts(K.vocab, decks);

  const picker = `
    <div class="btnrow" style="margin-top:0">
      <label for="deckpick" style="color:var(--ink-2)">Deck</label>
      <select id="deckpick">
        <option value="auto"${deckFilter === "auto" ? " selected" : ""}>Everything unlocked so far (week ${st.cursor.w})</option>
        ${Object.keys(K.deckMeta).map(d =>
          `<option value="${d}"${deckFilter === d ? " selected" : ""}>${esc(K.deckMeta[d].name)} — ${K.deckMeta[d].count} words</option>`).join("")}
      </select>
      <label for="newcap" style="color:var(--ink-2)">New per day</label>
      <select id="newcap">${[6, 10, 12, 16, 20, 30].map(n =>
        `<option value="${n}"${st.settings.newPerDay === n ? " selected" : ""}>${n}</option>`).join("")}</select>
    </div>`;

  const st2 = S.get();
  if (!session) {
    $("#vocab").innerHTML = `
      <div class="eyebrow">Spaced repetition</div>
      <h1>Vocabulary</h1>
      <p class="lede">${K.meta.vocab} words across ${Object.keys(K.deckMeta).length} decks, every noun with its article and plural, and ${K.meta.glossed} of them glossed in मराठी.
        Cards you find hard come back tomorrow; cards you know come back in weeks. Do the review before you do anything else in a session.</p>
      ${picker}
      <div class="stats" style="margin-top:18px">
        <div class="stat"><b>${cnt.due}</b><small>due now</small></div>
        <div class="stat"><b>${cnt.fresh}</b><small>not yet seen</small></div>
        <div class="stat"><b>${cnt.learned}</b><small>in rotation</small></div>
        <div class="stat"><b>${cnt.mature}</b><small>held over 21 days</small></div>
      </div>
      <div class="btnrow">
        <button class="btn" data-act="start">Start review</button>
        <button class="btn ghost" data-act="gender">Gender trainer</button>
        <button class="btn ghost" data-act="browse">Browse the deck</button>
      </div>
      <div id="browsehost"></div>`;
  } else {
    const q = session.queue;
    if (cardIdx >= q.length) {
      $("#vocab").innerHTML = `
        <h1>Session finished</h1>
        <p class="lede">${q.length} cards reviewed. ${cnt.due} still due today.</p>
        <div class="btnrow"><button class="btn" data-act="again">Another round</button>
        <button class="btn ghost" data-act="stop">Back</button></div>`;
    } else {
      const v = q[cardIdx];
      const isNewCard = R.isNew(v.id);
      $("#vocab").innerHTML = `
        <div class="eyebrow">Card ${cardIdx + 1} of ${q.length} &middot;
          ${esc(K.deckMeta[v.deck].name)}${isNewCard ? " &middot; new word" : ""}</div>
        <div class="fc">
          <div class="front">${v.art ? `<span class="art">${esc(v.art)}</span> ` : ""}${esc(v.word)}</div>
          ${revealed && v.pl ? `<div class="pl">Plural: ${esc(v.pl)}</div>` : ""}
          ${revealed ? `<div class="back">
              <div class="en">${esc(v.en)}</div>
              ${v.mr && st.settings.mr ? `<div class="mr-inline" style="font-size:1.1rem;margin-top:4px">${esc(v.mr)}</div>` : ""}
              ${v.ex ? `<div class="ex">${esc(v.ex)}</div>` : ""}
            </div>` : `<div class="pl">Say it out loud, with the article, before you reveal.</div>`}
        </div>
        ${revealed ? `<div class="rate">
            <button class="g1" data-g="1">Again<small>same session</small></button>
            <button data-g="2">Hard<small>soon</small></button>
            <button data-g="3">Good<small>on schedule</small></button>
            <button class="g4" data-g="4">Easy<small>push it out</small></button>
          </div>` : `<div class="btnrow"><button class="btn" data-act="reveal">Show meaning</button>
            <button class="btn ghost" data-act="stop">End session</button></div>`}`;
    }
  }

  const dp = $("#deckpick");
  if (dp) dp.onchange = () => { deckFilter = dp.value; session = null; renderVocab(); };
  const nc = $("#newcap");
  if (nc) nc.onchange = () => { S.get().settings.newPerDay = +nc.value; S.save(); renderVocab(); };

  $("#vocab").onclick = (e) => {
    const g = e.target.closest("button[data-g]");
    if (g) {
      R.rate(session.queue[cardIdx].id, +g.dataset.g);
      if (+g.dataset.g === 1) session.queue.push(session.queue[cardIdx]);
      cardIdx++; revealed = false; renderVocab(); return;
    }
    const b = e.target.closest("button[data-act]");
    if (!b) return;
    const a = b.dataset.act;
    if (a === "start" || a === "again") { startSession(); renderVocab(); }
    if (a === "reveal") { revealed = true; renderVocab(); }
    if (a === "stop") { session = null; renderVocab(); }
    if (a === "gender") { quizState = null; testTarget = { kind: "gender" }; go("test"); }
    if (a === "browse") renderBrowse();
  };
}

function renderBrowse() {
  const st = S.get();
  const decks = deckFilter === "auto" ? unlockedDecks(st.cursor.w) : new Set([deckFilter]);
  const list = K.vocab.filter(v => decks.has(v.deck));
  const host = $("#browsehost");
  host.innerHTML = `
    <div class="sec">
      <h2>${list.length} words available to you now</h2>
      <div class="btnrow" style="margin-top:8px">
        <input type="search" id="vsearch" placeholder="Search German or English" style="flex:1;min-width:220px">
      </div>
      <div id="vlist"></div>
    </div>`;
  const draw = (q) => {
    const f = q ? list.filter(v =>
      (v.full + " " + v.en + " " + v.ex).toLowerCase().includes(q.toLowerCase())) : list;
    $("#vlist").innerHTML = `<table class="ref">${f.slice(0, 300).map(v =>
      `<tr><td>${v.art ? `<span style="color:var(--ochre)">${esc(v.art)}</span> ` : ""}${esc(v.word)}${
        v.pl ? ` <span style="color:var(--ink-3);font-weight:400">(${esc(v.pl)})</span>` : ""}</td>
      <td>${esc(v.en)}${v.mr ? ` <span class="mr-inline">&middot; ${esc(v.mr)}</span>` : ""}${
        v.ex ? `<br><span style="color:var(--ink-3);font-style:italic">${esc(v.ex)}</span>` : ""}</td></tr>`
      ).join("")}</table>${f.length > 300 ? `<p style="color:var(--ink-3)">Showing the first 300 of ${f.length}. Narrow the search to see more.</p>` : ""}`;
  };
  draw("");
  $("#vsearch").oninput = (e) => draw(e.target.value);
}


/* -------------------------------------------------------------- STORY -- */
let epOpen = null, epAnswers = {}, storyTab = "story";

function renderStory() {
  const st = S.get();
  const cur = st.cursor.w;

  if (epOpen === null) {
    const eps = K.story.map(e => {
      const open = cur >= e.w;
      const read = st.storyRead && st.storyRead[e.n];
      return `<button class="ep ${open ? "" : "locked"} ${read ? "read" : ""}" ${open ? `data-ep="${e.n}"` : "disabled"}>
        <small>Folge ${e.n} &middot; week ${e.w} &middot; ${esc(e.level)}</small>
        <b>${esc(e.title)}</b>
        <span class="mrt">${esc(e.mr_title)}</span>
        ${open ? (read ? `<small style="color:var(--leaf)">read</small>` : "") : `<small>unlocks in week ${e.w}</small>`}
      </button>`;
    }).join("");

    const essays = K.essays.map(e => {
      const open = cur >= e.w;
      return `<button class="ep ${open ? "" : "locked"}" ${open ? `data-essay="${e.id}"` : "disabled"}>
        <small>week ${e.w} &middot; ${esc(e.kind)}</small>
        <b>${esc(e.title)}</b>
        <span class="mrt">${esc(e.mr_title)}</span></button>`;
    }).join("");

    $("#story").innerHTML = `
      <div class="eyebrow">${K.meta.story} episodes &middot; ${K.meta.essays} model texts</div>
      <h1>कथा — Nikhil's year</h1>
      <p class="lede">One episode every three weeks, written at exactly the level you have reached.
        Episode 1 uses only the present tense; episode 16 uses everything. Nikhil arrives in Göttingen from
        Solapur with almost no German and spends a year getting to a job offer. Read for the story first
        and the grammar second — that is the order that makes it stick.</p>
      <div class="epgrid">${eps}</div>

      <div class="sec">
        <h2>Model texts to steal from</h2>
        <p class="lede">Full worked examples of the five things you will actually have to write, each with a
          Marathi note on why it is built that way and the phrases worth lifting wholesale.</p>
        <div class="epgrid">${essays}</div>
      </div>`;

    $("#story").onclick = (e) => {
      const b = e.target.closest("button[data-ep]");
      if (b) { epOpen = +b.dataset.ep; epAnswers = {}; renderStory(); return; }
      const x = e.target.closest("button[data-essay]");
      if (x) { epOpen = "essay:" + x.dataset.essay; renderStory(); }
    };
    return;
  }

  if (String(epOpen).startsWith("essay:")) {
    const e = K.essays.find(x => x.id === String(epOpen).slice(6));
    $("#story").innerHTML = `
      <div class="btnrow" style="margin:0 0 14px"><button class="btn ghost" data-act="back">All episodes</button></div>
      <div class="eyebrow">${esc(e.kind)} &middot; unlocks week ${e.w}</div>
      <h1>${esc(e.title)}</h1>
      <div class="card"><div class="prose">${esc(e.text)}</div></div>
      <div class="mrbox"><h4>${esc(e.mr_title)} — रचना</h4><div class="mr">${esc(e.mr)}</div></div>
      <div class="sec"><h2>Phrases to lift wholesale</h2>
        <ul class="steal">${e.steal.map(x => `<li>${esc(x)}</li>`).join("")}</ul></div>`;
    $("#story").onclick = (ev) => {
      if (ev.target.closest("[data-act=back]")) { epOpen = null; renderStory(); window.scrollTo(0, 0); }
    };
    return;
  }

  const e = K.story.find(x => x.n === epOpen);
  const read = st.storyRead && st.storyRead[e.n];
  $("#story").innerHTML = `
    <div class="btnrow" style="margin:0 0 14px"><button class="btn ghost" data-act="back">All episodes</button></div>
    <div class="eyebrow">Folge ${e.n} von ${K.story.length} &middot; ${esc(e.level)} &middot; week ${e.w}</div>
    <h1>${esc(e.title)}</h1>
    <p class="mr-inline" style="font-size:1.05rem;margin-top:-4px">${esc(e.mr_title)}</p>

    <div class="card"><div class="prose">${esc(e.text)}</div></div>

    <div class="sec"><h2>Wortschatz</h2>
      <table class="gl">${e.gloss.map(g =>
        `<tr><td>${esc(g[0])}</td><td>${esc(g[1])}</td><td>${esc(g[2])}</td></tr>`).join("")}</table></div>

    <div class="mrbox"><h4>व्याकरणाची नोंद</h4><div class="mr">${esc(e.mr)}</div></div>

    <div class="sec"><h2>Verständnisfragen</h2>
      ${e.q.map((q, qi) => {
        const a = epAnswers[qi];
        return `<div class="card"><p><b>${esc(q[0])}</b></p>
          ${q[1].map((o, oi) => {
            let cls = "qopt";
            if (a !== undefined) { if (oi === q[2]) cls += " right"; else if (oi === a) cls += " wrong"; }
            return `<button class="${cls}" data-q="${qi}" data-o="${oi}" ${a !== undefined ? "disabled" : ""}>${esc(o)}</button>`;
          }).join("")}
          ${a !== undefined ? `<div class="why">${esc(q[3])}</div>` : ""}</div>`;
      }).join("")}</div>

    <div class="btnrow">
      <button class="btn ${read ? "ghost" : ""}" data-act="read">${read ? "Marked as read" : "Mark as read"}</button>
      ${e.n < K.story.length && st.cursor.w >= K.story[e.n].w
        ? `<button class="btn ghost" data-act="next">Next episode</button>` : ""}
    </div>`;

  $("#story").onclick = (ev) => {
    const o = ev.target.closest("button.qopt");
    if (o && epAnswers[+o.dataset.q] === undefined) {
      epAnswers[+o.dataset.q] = +o.dataset.o; renderStory(); return;
    }
    const b = ev.target.closest("button[data-act]");
    if (!b) return;
    if (b.dataset.act === "back") { epOpen = null; renderStory(); window.scrollTo(0, 0); }
    if (b.dataset.act === "read") {
      if (!st.storyRead) st.storyRead = {};
      st.storyRead[e.n] = true; S.save(); renderStory();
    }
    if (b.dataset.act === "next") { epOpen = e.n + 1; epAnswers = {}; renderStory(); window.scrollTo(0, 0); }
  };
}

/* --------------------------------------------------------------- TEST -- */
let testTarget = null;   // {kind:'week',w} | {kind:'cp',n,w} | {kind:'gender'}
let quizState = null;    // {items,i,answers,label,id}

function makeGenderItems(n) {
  const st = S.get();
  const pool = K.vocab.filter(v => v.art && unlockedDecks(st.cursor.w).has(v.deck));
  const picked = shuffle(pool.slice()).slice(0, n);
  return picked.map((v, i) => ({
    id: "g" + i,
    q: "___ " + v.word + (v.en ? "  (" + v.en + ")" : ""),
    opts: ["der", "die", "das"],
    a: ["der", "die", "das"].indexOf(v.art),
    why: v.art + " " + v.word + (v.pl ? ", Plural: " + v.pl : "") + (v.ex ? " — " + v.ex : "")
  }));
}

function shuffle(a) {
  for (let i = a.length - 1; i > 0; i--) { const j = Math.floor(Math.random() * (i + 1)); [a[i], a[j]] = [a[j], a[i]]; }
  return a;
}

function buildQuiz(t) {
  if (t.kind === "gender") return { id: "gender", label: "Gender trainer", items: makeGenderItems(20) };
  if (t.kind === "week") {
    const items = K.quiz.filter(q => q.w === t.w);
    return { id: "w" + t.w, label: "Week " + t.w + " quiz", items: shuffle(items.slice()) };
  }
  const items = K.quiz.filter(q => q.w <= t.w);
  return { id: "cp" + t.n, label: "Checkpoint " + t.n + " — weeks 1 to " + t.w,
           items: shuffle(items.slice()).slice(0, Math.min(25, items.length)) };
}

function renderTest() {
  const st = S.get();
  if (!testTarget) {
    const cps = K.checkpoints.map(cp => {
      const rec = st.quiz["cp" + cp.n];
      const open = st.cursor.w >= cp.w;
      return `<div class="weekrow" ${open ? `data-cp="${cp.n}" data-w="${cp.w}"` : ""} style="${open ? "" : "opacity:.45;cursor:default"}">
        <span class="wn">${cp.n}</span>
        <span class="wt">Checkpoint ${cp.n} — after week ${cp.w}<small>${esc(cp.title)}</small></span>
        <span class="pill ${phaseClass(cp.phase)}">${esc(cp.phase)}</span>
        <span style="color:var(--ink-3);font-size:.8rem;width:70px;text-align:right">
          ${rec ? Math.round(rec.best * 100) + "%" : open ? "not sat" : "locked"}</span></div>`;
    }).join("");

    const wRec = st.quiz["w" + st.cursor.w];
    $("#test").innerHTML = `
      <div class="eyebrow">Retrieval beats rereading. Every time.</div>
      <h1>Tests</h1>
      <p class="lede">A short quiz every week, a cumulative checkpoint ten times across the course, and a
        gender trainer you can hit whenever you have four spare minutes. Checkpoints unlock as you reach their week.</p>
      <div class="card">
        <h2>This week</h2>
        <p>Week ${st.cursor.w} quiz — ${K.quiz.filter(q => q.w === st.cursor.w).length} questions on this week's grammar.
        ${wRec ? `Your best so far: ${Math.round(wRec.best * 100)}% over ${wRec.attempts} attempts.` : "Not attempted yet."}</p>
        <div class="btnrow">
          <button class="btn" data-act="week">Start week ${st.cursor.w} quiz</button>
          <button class="btn ghost" data-act="gender">Gender trainer, 20 nouns</button>
        </div>
      </div>
      <div class="sec"><h2>Checkpoints</h2>${cps}</div>`;

    $("#test").onclick = (e) => {
      const row = e.target.closest("[data-cp]");
      if (row) { testTarget = { kind: "cp", n: +row.dataset.cp, w: +row.dataset.w }; quizState = null; renderTest(); return; }
      const b = e.target.closest("button[data-act]");
      if (!b) return;
      if (b.dataset.act === "week") testTarget = { kind: "week", w: st.cursor.w };
      if (b.dataset.act === "gender") testTarget = { kind: "gender" };
      quizState = null; renderTest();
    };
    return;
  }

  if (!quizState) {
    const q = buildQuiz(testTarget);
    quizState = { id: q.id, label: q.label, items: q.items, i: 0, answers: [] };
  }
  const qs = quizState;

  if (!qs.items.length) {
    $("#test").innerHTML = `<h1>${esc(qs.label)}</h1>
      <div class="empty">No questions are tagged for this week yet.</div>
      <div class="btnrow"><button class="btn ghost" data-act="back">Back to tests</button></div>`;
    $("#test").onclick = (e) => { if (e.target.closest("[data-act=back]")) { testTarget = null; quizState = null; renderTest(); } };
    return;
  }

  if (qs.i >= qs.items.length) {
    const right = qs.answers.filter(a => a.ok).length;
    const score = right / qs.items.length;
    const rec = st.quiz[qs.id] || { best: 0, attempts: 0 };
    rec.attempts++; rec.best = Math.max(rec.best, score); rec.last = score;
    st.quiz[qs.id] = rec; S.save();

    const verdict = score >= 0.9 ? "Solid. Move on."
      : score >= 0.75 ? "Good enough to move on, but redo the misses tomorrow."
      : "Below the bar. Repeat this week's grammar day before you continue.";

    $("#test").innerHTML = `
      <div class="eyebrow">${esc(qs.label)}</div>
      <h1>${right} of ${qs.items.length} &middot; ${Math.round(score * 100)}%</h1>
      <p class="lede">${esc(verdict)}</p>
      ${qs.answers.filter(a => !a.ok).length ? `<div class="sec"><h2>What you missed</h2>
        ${qs.answers.filter(a => !a.ok).map(a => `
          <div class="card"><p><b>${esc(a.q)}</b></p>
          <p style="color:var(--alert)">You chose: ${esc(a.chose)}</p>
          <p style="color:var(--leaf)">Correct: ${esc(a.correct)}</p>
          <div class="why">${esc(a.why)}</div>
          <div class="btnrow"><button class="btn ghost" data-err="${esc(a.q)}">Add to error log</button></div>
          </div>`).join("")}</div>` : `<div class="card">Nothing missed.</div>`}
      <div class="btnrow">
        <button class="btn" data-act="retry">Try again</button>
        <button class="btn ghost" data-act="back">Back to tests</button>
      </div>`;

    $("#test").onclick = (e) => {
      const err = e.target.closest("button[data-err]");
      if (err) {
        S.get().errors.unshift({ id: S.now() + "|" + err.dataset.err, text: err.dataset.err, w: S.get().cursor.w, ts: S.todayISO() });
        S.save(); toast("Added to the error log."); return;
      }
      const b = e.target.closest("button[data-act]");
      if (!b) return;
      if (b.dataset.act === "retry") { quizState = null; renderTest(); }
      if (b.dataset.act === "back") { testTarget = null; quizState = null; renderTest(); }
    };
    return;
  }

  const item = qs.items[qs.i];
  const answered = qs.answers[qs.i];
  $("#test").innerHTML = `
    <div class="eyebrow">${esc(qs.label)} &middot; question ${qs.i + 1} of ${qs.items.length}</div>
    <div class="qprog"><i style="width:${Math.round(qs.i / qs.items.length * 100)}%"></i></div>
    <div class="card">
      <h2 style="font-size:1.25rem">${esc(item.q)}</h2>
      <div style="margin-top:16px">
        ${item.opts.map((o, i) => {
          let cls = "qopt";
          if (answered) {
            if (i === item.a) cls += " right";
            else if (i === answered.idx) cls += " wrong";
          }
          return `<button class="${cls}" data-i="${i}" ${answered ? "disabled" : ""}>${esc(o)}</button>`;
        }).join("")}
      </div>
      ${answered ? `<div class="why">${esc(item.why)}</div>
        <div class="btnrow"><button class="btn" data-act="next">
          ${qs.i + 1 === qs.items.length ? "See result" : "Next question"}</button></div>` : ""}
    </div>`;

  $("#test").onclick = (e) => {
    const o = e.target.closest("button.qopt");
    if (o && !qs.answers[qs.i]) {
      const idx = +o.dataset.i;
      qs.answers[qs.i] = {
        idx, ok: idx === item.a, q: item.q,
        chose: item.opts[idx], correct: item.opts[item.a], why: item.why
      };
      renderTest(); return;
    }
    if (e.target.closest("[data-act=next]")) { qs.i++; renderTest(); window.scrollTo(0, 0); }
  };
}

/* ----------------------------------------------------------- PHRASES --- */
let pageId = null;
function renderPhrases() {
  const p = pageId ? K.pages.find(x => x.id === pageId) : null;
  if (!p) {
    $("#phrases").innerHTML = `
      <div class="eyebrow">Always available, not tied to a week</div>
      <h1>Reference</h1>
      <p class="lede">The things you will look up again and again: how to pronounce German as a Marathi speaker,
        email skeletons, the interview bank, connector tables, chart language and the four written text types.</p>
      ${K.pages.map(x => `<div class="weekrow" data-p="${x.id}">
        <span class="wt"><b>${esc(x.title)}</b><small>${esc(x.intro.slice(0, 110))}…</small></span></div>`).join("")}`;
    $("#phrases").onclick = (e) => {
      const r = e.target.closest("[data-p]");
      if (r) { pageId = r.dataset.p; renderPhrases(); window.scrollTo(0, 0); }
    };
    return;
  }
  $("#phrases").innerHTML = `
    <div class="btnrow" style="margin:0 0 14px"><button class="btn ghost" data-act="back">All reference pages</button></div>
    <h1>${esc(p.title)}</h1>
    <p class="lede">${esc(p.intro)}</p>
    ${p.sections.map(s => `
      <div class="sec"><h2>${esc(s.h)}</h2>
      ${s.rows ? `<table class="ref">${s.rows.map(r =>
        `<tr><td>${esc(r[0])}</td><td>${esc(r[1])}</td></tr>`).join("")}</table>` : ""}
      ${s.text ? `<pre class="tpl">${esc(s.text)}</pre>` : ""}
      </div>`).join("")}`;
  $("#phrases").onclick = (e) => {
    if (e.target.closest("[data-act=back]")) { pageId = null; renderPhrases(); window.scrollTo(0, 0); }
  };
}

/* ---------------------------------------------------------- PROGRESS --- */
function renderProgress() {
  const st = S.get();
  const done = totalDone();
  const decks = unlockedDecks(st.cursor.w);
  const cnt = R.counts(K.vocab, decks);
  const fc = R.forecast(14);
  const maxF = Math.max(1, ...fc);
  const quizzes = Object.keys(st.quiz).map(k => ({ k, ...st.quiz[k] }));
  const avg = quizzes.length ? quizzes.reduce((a, q) => a + q.best, 0) / quizzes.length : 0;

  $("#progress").innerHTML = `
    <div class="eyebrow">Started ${esc(st.started)} &middot; saving to ${esc(S.backend === "local" ? "this browser" : "your Claude session")}</div>
    <h1>Progress</h1>
    <div class="stats">
      <div class="stat"><b>${done}</b><small>days completed of ${K.meta.days}</small>
        <div class="bar"><i style="width:${done / K.meta.days * 100}%"></i></div></div>
      <div class="stat"><b>${st.streak.count}</b><small>day streak, best ${st.streak.longest}</small></div>
      <div class="stat"><b>${cnt.learned}</b><small>words in rotation of ${K.meta.vocab}</small>
        <div class="bar"><i style="width:${cnt.learned / K.meta.vocab * 100}%"></i></div></div>
      <div class="stat"><b>${cnt.mature}</b><small>words held past 21 days</small></div>
      <div class="stat"><b>${quizzes.length ? Math.round(avg * 100) + "%" : "—"}</b><small>average best quiz score</small></div>
      <div class="stat"><b>W${st.cursor.w}</b><small>current week, ${esc(week(st.cursor.w).phase)}</small></div>
    </div>

    <div class="sec">
      <h2>Review load, next 14 days</h2>
      <p class="lede">If a bar is much taller than the others you skipped days; spread it by doing short extra sessions.</p>
      <div style="display:flex;align-items:flex-end;gap:5px;height:110px;margin-top:12px">
        ${fc.map((n, i) => `<div style="flex:1;text-align:center">
          <div title="${n} cards" style="background:var(--water);border-radius:2px;height:${Math.round(n / maxF * 86)}px;min-height:2px"></div>
          <small style="color:var(--ink-3);font-size:.65rem">${i === 0 ? "now" : "+" + i}</small></div>`).join("")}
      </div>
    </div>

    <div class="sec">
      <h2>Phase completion</h2>
      ${["A1", "A2", "B1", "KONS"].map(p => {
        const ws = K.curriculum.filter(c => c.phase === p);
        const d = ws.reduce((a, c) => a + weekProgress(c.w), 0);
        const t = ws.length * 7;
        return `<div class="flat" style="margin-bottom:8px">
          <div style="display:flex;justify-content:space-between"><b>${esc(ws[0].phaseName)} (${p})</b>
          <span style="color:var(--ink-3)">${d}/${t} days</span></div>
          <div class="bar"><i style="width:${d / t * 100}%"></i></div></div>`;
      }).join("")}
    </div>

    <div class="sec">
      <h2>Error log</h2>
      <p class="lede">The single highest-value page here. Read it out loud on every day 7.</p>
      ${st.errors.length ? `<table class="ref">${st.errors.slice(0, 80).map((e, i) =>
        `<tr><td style="width:auto">${esc(e.text)}</td>
         <td style="width:150px;color:var(--ink-3)">week ${e.w} &middot; ${esc(e.ts)}
         <button class="btn ghost" style="padding:2px 8px;font-size:.75rem;margin-left:6px" data-del="${i}">remove</button></td></tr>`
        ).join("")}</table>` : `<div class="empty">Nothing logged yet. Add mistakes from the Today page or after a quiz.</div>`}
    </div>

    <div class="sec">
      <h2>Sync across your devices</h2>
      <p class="lede">Without this, progress lives in one browser on one device. With it, typing your name
        on any device picks up exactly where you left off. Your progress is merged, never overwritten:
        if you study on the laptop and the phone before either syncs, both days are kept.</p>
      <div id="synccfg"></div>
    </div>

    <div class="sec">
      <h2>Your data</h2>
      <p class="lede">Progress is stored in this browser only. Export it before you switch computers or clear your browser data,
        and commit the file to your repo if you want a backup with a history.</p>
      <div class="btnrow">
        <button class="btn ghost" data-act="export">Download progress file</button>
        <button class="btn ghost" data-act="import">Load a progress file</button>
        <button class="btn ghost" data-act="reset" style="border-color:var(--alert);color:var(--alert)">Erase all progress</button>
        <input type="file" id="fileimp" accept="application/json" style="display:none">
      </div>
      <div class="btnrow">
        <label for="modepick" style="color:var(--ink-2)">Daily session length</label>
        <select id="modepick">
          <option value="60"${st.settings.mode === 60 ? " selected" : ""}>60 minutes, core steps only</option>
          <option value="90"${st.settings.mode === 90 ? " selected" : ""}>90 minutes, everything</option>
        </select>
        <label for="mrpick" style="color:var(--ink-2)">मराठी on flashcards</label>
        <select id="mrpick">
          <option value="1"${st.settings.mr !== false ? " selected" : ""}>Show</option>
          <option value="0"${st.settings.mr === false ? " selected" : ""}>Hide (year two)</option>
        </select>
        <label for="themepick" style="color:var(--ink-2)">Theme</label>
        <select id="themepick">
          <option value="light"${st.settings.theme === "light" ? " selected" : ""}>Light</option>
          <option value="dark"${st.settings.theme === "dark" ? " selected" : ""}>Dark</option>
        </select>
      </div>
    </div>`;

  renderSyncCfg();
  $("#mrpick").onchange = (e) => { st.settings.mr = e.target.value === "1"; S.save(); toast("Setting saved."); };
  $("#modepick").onchange = (e) => { st.settings.mode = +e.target.value; S.save(); toast("Session length set."); };
  $("#themepick").onchange = (e) => {
    st.settings.theme = e.target.value; S.save();
    document.documentElement.dataset.theme = e.target.value;
  };

  $("#progress").onclick = (e) => {
    const del = e.target.closest("button[data-del]");
    if (del) { st.errors.splice(+del.dataset.del, 1); S.save(); renderProgress(); return; }
    const b = e.target.closest("button[data-act]");
    if (!b) return;
    const a = b.dataset.act;
    if (a === "export") {
      const blob = new Blob([S.exportJSON()], { type: "application/json" });
      const url = URL.createObjectURL(blob);
      const link = document.createElement("a");
      link.href = url; link.download = "deutsch-agrar-progress-" + S.todayISO() + ".json";
      link.click(); URL.revokeObjectURL(url);
    }
    if (a === "import") $("#fileimp").click();
    if (a === "reset") {
      if (confirm("This erases every completed day, every flashcard schedule and the error log. There is no undo. Continue?")) {
        S.reset().then(() => { renderRail(); renderProgress(); toast("Progress erased."); });
      }
    }
  };

  $("#fileimp").onchange = (e) => {
    const f = e.target.files[0];
    if (!f) return;
    const rd = new FileReader();
    rd.onload = () => {
      try { S.importJSON(rd.result).then(() => { renderRail(); renderProgress(); toast("Progress loaded."); }); }
      catch (err) { toast("That file is not a progress export."); }
    };
    rd.readAsText(f);
  };
}


function renderSyncCfg() {
  const host = $("#synccfg");
  if (!host) return;
  const cfg = S.getSyncCfg();
  const providers = Sync.list();
  const a = Sync.ADAPTERS[cfg.adapter] || Sync.ADAPTERS.none;
  const needs = (k) => a.needs.includes(k);

  const labels = {
    url:   cfg.adapter === "gist" ? "Gist id"
         : cfg.adapter === "t9" ? "Your Pi's HTTPS address" : "Folder URL",
    user:  "Username",
    token: cfg.adapter === "gist" ? "Access token (gist scope only)"
         : cfg.adapter === "webdav" ? "App password"
         : cfg.adapter === "t9" ? "T9_SYNC_TOKEN from the Pi" : "Access token"
  };

  host.innerHTML = `
    <div class="card">
      <div class="field">
        <label for="provider">Where progress is stored</label>
        <select id="provider">${providers.map(p =>
          `<option value="${p.id}"${cfg.adapter === p.id ? " selected" : ""}>${esc(p.label)}</option>`).join("")}</select>
      </div>
      ${needs("url") ? `<div class="field"><label for="syncurl">${esc(labels.url)}</label>
        <input type="text" id="syncurl" value="${esc(cfg.url)}" placeholder="${
          cfg.adapter === "gist" ? "a1b2c3d4e5f6…" : "https://your-cloud.example/remote.php/dav/files/you/deutsch"}"></div>` : ""}
      ${needs("user") ? `<div class="field"><label for="syncuser">${esc(labels.user)}</label>
        <input type="text" id="syncuser" value="${esc(cfg.user)}"></div>` : ""}
      ${needs("token") ? `<div class="field"><label for="synctoken">${esc(labels.token)}</label>
        <input type="text" id="synctoken" value="${esc(cfg.token)}" autocomplete="off"></div>` : ""}
      ${cfg.adapter === "t9" ? `
        <div class="warn" style="border-left-color:var(--ochre);background:var(--ochre-soft)">
          <b>It must be https, and reachable without an app.</b> This site is served over HTTPS, so a
          request to <code>http://…</code> is blocked silently by the browser. A <code>ts.net</code> address
          only works on devices running Tailscale — fine for your own machines, no good for anyone who
          cannot install software. For those, use <code>tailscale funnel</code> (public, unlike <code>tailscale serve</code>)
          or a Cloudflare Tunnel address: public HTTPS, protected by the token below,
          nothing installed at the other end.
          See <code>server/SETUP.md</code>.
        </div>` : ""}
      ${cfg.adapter !== "none" ? `
        <div class="warn">
          <b>Read this before you paste a token.</b> This is a static site with no server, so the token is
          stored in this browser and sent from it. Anyone with access to this device can read it.
          Create a token that can do only this one job — a gist-scope token, or a WebDAV app password
          limited to one folder — never your main account password. Revoke it if the device is lost.
        </div>
        <div class="btnrow">
          <button class="btn" data-act="savesync">Save and test</button>
          <button class="btn ghost" data-act="syncnow">Sync now</button>
          <label style="color:var(--ink-2)"><input type="checkbox" id="autosync" ${cfg.auto ? "checked" : ""}> sync automatically</label>
        </div>
        <p id="syncmsg" style="margin-top:10px;color:var(--ink-2)"></p>

        <div style="border-top:1px solid var(--line);margin-top:16px;padding-top:14px">
          <h3 style="font-size:1rem">Set up someone else's device</h3>
          <p style="color:var(--ink-2);margin:4px 0 10px">
            This makes a one-time link that carries these settings. They open it once on their laptop,
            it configures itself, and they bookmark it. Nothing to install, no token to type, no settings
            to find. Send it privately — anyone holding the link can sync.</p>
          <div class="field">
            <label for="invname">Their name (optional, saves them typing it)</label>
            <input type="text" id="invname" placeholder="Raj">
          </div>
          <div class="btnrow" style="margin-top:0">
            <button class="btn ghost" data-act="makeinvite">Create setup link</button>
          </div>
          <div id="invout" style="margin-top:10px"></div>
        </div>` : `
        <div class="btnrow"><button class="btn" data-act="savesync">Save</button></div>`}
    </div>`;

  $("#provider").onchange = async (e) => {
    await S.setSyncCfg({ adapter: e.target.value });
    renderSyncCfg();
  };
  const auto = $("#autosync");
  if (auto) auto.onchange = () => S.setSyncCfg({ auto: auto.checked });

  host.onclick = async (e) => {
    const b = e.target.closest("button[data-act]");
    if (!b) return;
    const msg = $("#syncmsg");
    const draft = {
      adapter: $("#provider").value,
      url: ($("#syncurl") || {}).value || "",
      user: ($("#syncuser") || {}).value || "",
      token: ($("#synctoken") || {}).value || "",
      auto: auto ? auto.checked : true
    };
    if (b.dataset.act === "savesync") {
      await S.setSyncCfg(draft);
      if (draft.adapter === "none") { renderSyncCfg(); renderSyncBar(); toast("Saved."); return; }
      if (msg) msg.textContent = "Testing the connection…";
      try {
        await Sync.test(draft, "test");
        if (msg) msg.textContent = "Connected. Syncing your progress now.";
        await Sync.sync("manual");
        renderRail(); renderProgress();
      } catch (err) {
        if (msg) msg.innerHTML = "<span style=\"color:var(--alert)\">Could not connect: " +
          esc(String(err.message || err)) + "</span><br><span style=\"color:var(--ink-3)\">" +
          "If this says &quot;Failed to fetch&quot;, the server is refusing the browser rather than refusing you " +
          "— that is a CORS setting on the server side, not a wrong password.</span>";
      }
      return;
    }
    if (b.dataset.act === "makeinvite") {
      const link = makeInvite(($("#invname") || {}).value || "");
      const out = $("#invout");
      out.innerHTML = `<textarea readonly style="min-height:70px;font-size:.8rem">${esc(link)}</textarea>
        <div class="btnrow" style="margin-top:6px"><button class="btn ghost" data-act="copyinvite">Copy link</button>
        <span style="color:var(--ink-3);font-size:.8rem">Opens their course already synced.</span></div>`;
      return;
    }
    if (b.dataset.act === "copyinvite") {
      const ta = $("#invout textarea");
      if (ta) {
        ta.select();
        if (navigator.clipboard) navigator.clipboard.writeText(ta.value).then(() => toast("Link copied."));
        else { try { document.execCommand("copy"); toast("Link copied."); } catch (e) { toast("Select and copy the link above."); } }
      }
      return;
    }
    if (b.dataset.act === "syncnow") {
      if (msg) msg.textContent = "Syncing…";
      const ok = await Sync.sync("manual");
      if (msg) msg.textContent = ok ? "Synced." : Sync.getStatus().msg;
      renderRail(); renderProgress();
    }
  };
}

/* ------------------------------------------------------------- GUIDE --- */
function renderGuide() {
  $("#guide").innerHTML = `
    <div class="eyebrow">Read this once, then stop reading it</div>
    <h1>How this works</h1>
    <p class="lede">The plan assumes 60 to 90 minutes a day, seven days a week, for 48 weeks. Sixty minutes is the
      real commitment; the extra thirty is where the speed comes from. Miss a day and nothing breaks — the cursor
      waits for you. Miss a week and repeat the week.</p>

    <div class="sec">
      <h2>The daily rhythm</h2>
      <table class="ref">
        <tr><td>Day 1 — Neue Struktur</td><td>Meet the grammar. Write the rule in your own words. No drilling yet.</td></tr>
        <tr><td>Day 2 — Drill</td><td>Twenty transformations, said out loud before they are written. First quiz attempt.</td></tr>
        <tr><td>Day 3 — Hören</td><td>Input before output. Listen twice, then shadow ninety seconds five times.</td></tr>
        <tr><td>Day 4 — Fachtext</td><td>Real German in your own subject. Compound nouns split before translated.</td></tr>
        <tr><td>Day 5 — Schreiben</td><td>Produce something a German person could actually receive.</td></tr>
        <tr><td>Day 6 — Sprechen</td><td>Recorded monologue plus a role-play. The day interviews are won on.</td></tr>
        <tr><td>Day 7 — Wiederholung</td><td>Nothing new. Review, second quiz attempt, error log read aloud.</td></tr>
      </table>
    </div>

    <div class="mrbox">
      <h4>मराठीतून विचार करा, इंग्रजीतून नाही</h4>
      <div class="mr">जर्मन व्याकरणासाठी इंग्रजी चुकीची मधली भाषा आहे. इंग्रजीने लिंग, विभक्ती, क्रियापदाची शेवटची जागा आणि तू/तुम्ही — हे चारही सोडून दिलं. मराठीने चारही ठेवले. मराठी → इंग्रजी → जर्मन असा प्रवास म्हणजे नेमकी जी भाषा या गोष्टी हरवून बसली आहे तिच्यातून जाणं. दर आठवड्याला 'मराठीचा पूल' नोंद आहे — जिथे मराठी मदत करते तिथे कशी, आणि जिथे अडवते तिथे कुठे. Reference मधलं पहिलं पान पूर्ण नकाशा आहे.</div>
    </div>

    <div class="sec">
      <h2>Four rules that decide whether this works</h2>
      <table class="ref">
        <tr><td>Speak before you write</td><td>Every sentence you write, say first. This is the only way pronunciation and
          word order become automatic rather than calculated.</td></tr>
        <tr><td>Never learn a noun without its article</td><td>"Boden" is a word you will get wrong forever.
          "der Boden, die Böden" is a word you will get right. The cards are built this way on purpose.</td></tr>
        <tr><td>Log every mistake, not every word</td><td>A mistake you made is worth ten words you looked up.
          The error log is the part of this site you should reread most.</td></tr>
        <tr><td>Three lines, not two</td><td>मराठी वाक्य → रचना-ओळ (क्रियापद कुठे जाईल) → जर्मन वाक्य.
          Never write the English line. It hands you the wrong word order and no gender.</td></tr>
        <tr><td>Read the story before you feel ready</td><td>Each episode sits slightly ahead of what you can
          produce, which is exactly where a graded reader belongs. Read for what happens to Nikhil; let the
          grammar arrive on its own.</td></tr>
        <tr><td>Record yourself weekly</td><td>You cannot hear your own errors live. You can hear them on playback.
          Week 6 and week 41 recordings side by side are the proof the year worked.</td></tr>
      </table>
    </div>

    <div class="sec">
      <h2>Where the four tracks go</h2>
      <table class="ref">
        <tr><td>Studies</td><td>Seminars, module handbooks, deadlines, supervisors, HiWi work, thesis language.</td></tr>
        <tr><td>Daily life</td><td>Registration, housing, insurance, doctor, bank, phone calls, complaints.</td></tr>
        <tr><td>Agriculture</td><td>Soil, crops, livestock, machinery, farm economics and policy — the professional core.</td></tr>
        <tr><td>Work and interviews</td><td>Field and warehouse instructions, applications, the interview itself, the contract.</td></tr>
      </table>
      <p style="margin-top:12px">Week 43 is a dedicated Führerschein sprint, because the theory exam and the driving
        lessons are their own vocabulary and most agricultural adverts ask for Klasse B.</p>
    </div>

    <div class="sec">
      <h2>Free resources worth your time</h2>
      <table class="ref">
        <tr><td>DW — Nicos Weg</td><td>A1 to B1, free, video-based, the best free structured course there is.
          learngerman.dw.com</td></tr>
        <tr><td>VHS-Lernportal</td><td>Free German courses A1–B2 with corrected writing exercises. vhs-lernportal.de</td></tr>
        <tr><td>Nachrichtenleicht / DW Langsam gesprochene Nachrichten</td><td>News in simplified or slow German.
          Your day-3 listening from week 13 onward.</td></tr>
        <tr><td>Goethe and telc model exams</td><td>Free PDF and audio Modellsätze for A1, A2 and B1. Use them at
          checkpoints 2, 4 and in week 46.</td></tr>
        <tr><td>agrarheute, top agrar, proplanta</td><td>Professional agricultural news in German. Your day-4 texts.</td></tr>
        <tr><td>LfL Bayern, KTBL, Bundessortenamt, BLE</td><td>Factsheets, standards and variety lists — real professional
          German in your exact field.</td></tr>
        <tr><td>Official Führerschein Fragenkatalog</td><td>The real theory question bank. Week 43.</td></tr>
        <tr><td>Anki</td><td>If you ever outgrow the flashcards here, export and move to Anki. Same algorithm family.</td></tr>
      </table>
    </div>

    <div class="sec">
      <h2>The bigger timeline</h2>
      <p>Forty-eight weeks starting now lands B1 inside semester 5, which leaves semester 6 for a B2 push,
        the thesis and applications. If you sit a certificate, do it within a month of week 48 while the exam
        format is fresh. Put the certificate on the CV as "Deutsch B1 (Goethe-Zertifikat, [Monat Jahr])" —
        German employers read a level with a source very differently from a self-assessed one.</p>
    </div>`;
}


/* --------------------------------------------------------------- GATE -- */
function renderGate(mode) {
  const list = S.listProfiles();
  const g = $("#gate");
  g.classList.add("on");
  $("#shell").hidden = true;

  const known = list.length && mode !== "new" ? `
    <div style="margin-bottom:18px">
      ${list.map(p => `<button class="who" data-open="${esc(p.name)}">
        <span><b>${esc(p.name)}</b><small>started ${esc(p.created)}</small></span>
        <span style="color:var(--ink-3);font-size:.8rem">continue</span></button>`).join("")}
    </div>
    <div class="row"><button class="btn ghost" data-act="new" style="flex:1">Someone else</button></div>` : `
    <div class="field">
      <input type="text" id="whoname" placeholder="Your name" autocomplete="off" autofocus>
    </div>
    <div class="row">
      <button class="btn" data-act="go" style="flex:1">Open my course</button>
      ${list.length ? `<button class="btn ghost" data-act="back">Back</button>` : ""}
    </div>`;

  g.innerHTML = `<div class="gatecard">
    <h1>Deutsch für Agrar</h1>
    <p class="sub">Who is studying?</p>
    <p class="mr">कोण शिकतंय? नाव लिहा — तुमची प्रगती तिथून पुढे चालू होईल.</p>
    ${known}
    <p class="hint">Each name keeps its own progress: its own day, its own flashcard schedule,
      its own error log. Type the same name on any device to pick up where you left off,
      as long as sync is switched on in Progress.</p>
  </div>`;

  const enter = async (name) => {
    if (!S.slug(name)) { toast("Please type a name."); return; }
    await S.openProfile(name);
    await afterLogin();
  };

  g.onclick = (e) => {
    const w = e.target.closest("button[data-open]");
    if (w) { enter(w.dataset.open); return; }
    const b = e.target.closest("button[data-act]");
    if (!b) return;
    if (b.dataset.act === "new") renderGate("new");
    if (b.dataset.act === "back") renderGate();
    if (b.dataset.act === "go") enter($("#whoname").value);
  };
  const inp = $("#whoname");
  if (inp) inp.onkeydown = (e) => { if (e.key === "Enter") enter(inp.value); };
}

async function afterLogin() {
  const st = S.get();
  document.documentElement.dataset.theme = st.settings.theme || "light";
  $("#gate").classList.remove("on");
  $("#shell").hidden = false;
  browseWeek = st.cursor.w;
  session = null; epOpen = null; testTarget = null; quizState = null; pageId = null;
  go("today");
  if (window.Sync && Sync.isOn() && Sync.configured()) Sync.sync("boot").then(() => {
    browseWeek = S.get().cursor.w;
    go(view);
  });
}

/* ------------------------------------------------------------ sync bar -- */
function renderSyncBar() {
  const el = $("#syncbar");
  if (!el) return;
  const s = Sync.getStatus();
  const when = s.at ? s.at.toLocaleTimeString([], { hour: "2-digit", minute: "2-digit" }) : "";
  el.innerHTML = `<span class="dot ${esc(s.state)}"></span>
    <span style="flex:1">${esc(s.msg)}${s.state === "ok" && when ? " " + esc(when) : ""}</span>
    ${Sync.isOn() ? `<button data-act="syncnow">sync now</button>` : ""}`;
  el.onclick = (e) => {
    if (e.target.closest("[data-act=syncnow]")) Sync.sync("manual");
  };
}


/* ------------------------------------------------------------- INVITE -- */
/* A setup link carries the sync settings so the other person never types a
   token, installs anything, or opens Settings. They click once, bookmark it,
   and every day after that is just: open bookmark, study. */

function b64e(obj) {
  return btoa(unescape(encodeURIComponent(JSON.stringify(obj))))
    .replace(/\+/g, "-").replace(/\//g, "_").replace(/=+$/, "");
}
function b64d(str) {
  const s = String(str).replace(/-/g, "+").replace(/_/g, "/");
  return JSON.parse(decodeURIComponent(escape(atob(s))));
}

function makeInvite(name) {
  const c = S.getSyncCfg();
  const payload = { a: c.adapter, u: c.url, t: c.token };
  if (c.user) payload.s = c.user;
  if (name && name.trim()) payload.n = name.trim();
  const base = location.origin + location.pathname;
  return base + "#setup=" + b64e(payload);
}

/* Returns the name to pre-fill, or null. Never throws on a malformed link. */
async function applyInvite(raw) {
  try {
    const p = b64d(raw);
    if (!p || !p.a || !Sync.ADAPTERS[p.a]) return null;
    await S.setSyncCfg({
      adapter: p.a, url: p.u || "", token: p.t || "",
      user: p.s || "", auto: true
    });
    return p.n || null;
  } catch (e) {
    return null;
  }
}

/* -------------------------------------------------------------- router - */
function go(v) {
  view = v;
  $$(".view").forEach(el => el.classList.toggle("on", el.id === v));
  renderRail();
  if (v === "today") renderToday();
  if (v === "plan") renderPlan();
  if (v === "vocab") renderVocab();
  if (v === "story") renderStory();
  if (v === "test") renderTest();
  if (v === "phrases") renderPhrases();
  if (v === "progress") renderProgress();
  if (v === "guide") renderGuide();
  try { history.replaceState(null, "", "#" + v); } catch (e) {}
  window.scrollTo(0, 0);
}

async function boot() {
  await S.loadIndex();
  await S.loadSyncCfg();

  // A setup link is consumed once, then scrubbed from the address bar so the
  // token is not left sitting in the URL of a bookmark or in history.
  let invitedName = null;
  const m = (location.hash + location.search).match(/setup=([A-Za-z0-9_-]+)/);
  if (m) {
    invitedName = await applyInvite(m[1]);
    try { history.replaceState(null, "", location.pathname); } catch (e) {}
  }

  Sync.onStatus(() => renderSyncBar());
  S.setOnChange(() => Sync.schedulePush());

  const last = await S.lastProfile();
  const known = S.listProfiles();

  if (invitedName) {
    // the link named them: straight in, nothing to type
    await S.openProfile(invitedName);
    await afterLogin();
    toast("Synced device set up. Bookmark this page.");
  } else if (last && known.some(p => p.id === last)) {
    const p = known.find(x => x.id === last);
    await S.openProfile(p.name);
    await afterLogin();
  } else {
    renderGate();
  }

  window.addEventListener("beforeunload", () => { S.saveNow(); });
  // a tab regaining focus is the cheapest possible sync trigger
  document.addEventListener("visibilitychange", () => {
    if (!document.hidden && S.currentProfile() && Sync.isOn() && Sync.configured()) Sync.sync("focus");
  });
}

window.__test = { makeInvite, applyInvite, b64e, b64d };
boot();
})();

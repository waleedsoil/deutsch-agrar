(function(){
"use strict";
/* Spaced repetition.
   A trimmed SM-2: four ratings, ease factor between 1.3 and 2.8,
   intervals in whole days. Good enough to hold 900 words, simple
   enough that the scheduling is predictable to the learner. */

const get = () => window.Store.get();
const save = () => window.Store.save();
const epochDay = (x) => window.Store.epochDay(x);

const AGAIN = 1, HARD = 2, GOOD = 3, EASY = 4;

function card(id){
  const s = get();
  if (!s.srs[id]) s.srs[id] = { due: 0, ivl: 0, ease: 2.5, reps: 0, lapses: 0, seen: 0 };
  return s.srs[id];
}

function isNew(id){ return !get().srs[id]; }

function dueToday(id){
  const c = get().srs[id];
  return !!c && c.due <= epochDay();
}

function rate(id, grade){
  const c = card(id);
  const today = epochDay();

  if (grade === AGAIN){
    c.lapses++;
    c.reps = 0;
    c.ease = Math.max(1.3, c.ease - 0.2);
    c.ivl = 0;
    c.due = today;                       // comes back in the same session
  } else if (c.reps === 0){
    c.ivl = grade === HARD ? 1 : grade === GOOD ? 1 : 3;
    c.reps = 1;
    c.due = today + c.ivl;
  } else if (c.reps === 1){
    c.ivl = grade === HARD ? 3 : grade === GOOD ? 6 : 10;
    c.reps = 2;
    c.due = today + c.ivl;
  } else {
    if (grade === HARD) c.ease = Math.max(1.3, c.ease - 0.15);
    if (grade === EASY) c.ease = Math.min(2.8, c.ease + 0.1);
    const mult = grade === HARD ? 1.2 : c.ease;
    c.ivl = Math.max(1, Math.round(c.ivl * mult * (grade === EASY ? 1.3 : 1)));
    c.ivl = Math.min(c.ivl, 400);
    c.reps++;
    c.due = today + c.ivl;
  }
  c.seen = Date.now();   // the merge uses this to pick the newer review
  save();
  return c;
}

/* Builds a session: everything due, then new cards from the decks the
   learner has already reached, capped by the daily new-card setting. */
function buildSession(vocab, unlockedDecks, newCap){
  const s = get();
  const today = epochDay();
  const pool = vocab.filter(v => unlockedDecks.has(v.deck));

  const due = pool.filter(v => s.srs[v.id] && s.srs[v.id].due <= today);
  const fresh = pool.filter(v => !s.srs[v.id]).slice(0, newCap);

  due.sort((a, b) => (s.srs[a.id].due - s.srs[b.id].due));
  return { due, fresh, queue: due.concat(fresh) };
}

function counts(vocab, unlockedDecks){
  const s = get();
  const today = epochDay();
  let learned = 0, due = 0, fresh = 0, mature = 0;
  for (const v of vocab){
    const c = s.srs[v.id];
    if (c){
      learned++;
      if (c.due <= today) due++;
      if (c.ivl >= 21) mature++;
    } else if (unlockedDecks.has(v.deck)) fresh++;
  }
  return { learned, due, fresh, mature };
}

function forecast(days){
  const s = get();
  const today = epochDay();
  const out = new Array(days).fill(0);
  for (const id in s.srs){
    const d = s.srs[id].due - today;
    if (d >= 0 && d < days) out[d]++;
    else if (d < 0) out[0]++;
  }
  return out;
}

window.SRS = { AGAIN, HARD, GOOD, EASY, isNew, dueToday, rate, buildSession, counts, forecast };
})();

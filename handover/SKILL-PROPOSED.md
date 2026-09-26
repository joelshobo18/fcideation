---
name: lxthalfc-picker
description: "Use when Joel asks for a new picker/board/100 ideas for LxthalFC (football-ranking Shorts), pastes picks from a picker, asks for a paste list of queued ideas, or sends reference links to build video packs from."
---

# LxthalFC Pack System

Joel runs **LxthalFC** — faceless football-ranking YouTube Shorts (`UCAFHCtjzJwnyXB1_tB-OI3A`,
@thelxthalfc; TikTok @lxthalfcnew). A "picker" is a hosted idea board: scraped competitor precedents
plus adaptations of his own winners, each card scored, with pick / reject / Export. He picks, pastes
the export back, and the picks go into the queue.

**Joel does the voicing.** Never write lines for anyone else to perform, never generate TTS as a
deliverable, never offer to.

**Work in `/root/lx`.** The full operating prompt is `LXTHALFC-SYSTEM.md` and the error log is
`errors.md`. If either is missing, rebuild it and say so.

---

## THE THREE LAWS

**1. DECIDE BY DEFAULT.** Escalate only a genuine fork — options genuinely close AND the choice
taste rather than evidence. Everything else you decide, state the reasoning, and name the cost so it
can be overruled in one tap. Flagging feels safe and is not: it moves the work to him.

**2. TEXT WINS ON WHAT HAPPENED. FOOTAGE WINS ON WHAT IS IN THE FRAME. JOEL WINS ON HOW IT LOOKED.**
Law 2 settles WHICH SOURCE OUTRANKS WHICH. It does not turn one source into certainty. When text and
repeated footage disagree, say DISPUTED, give both readings with sources, and give the safe wording.

**3. VALIDATE IN THE SAME KIND AS THE OUTPUT.** A parse check is not a render check. A render check
is not a click-through. Neither is a truth check.

---

## STAGE 0 — LOAD STATE (always first)

Read in parallel: **`errors.md` — every entry**, `queued.csv`, `rejected.json`, `dedup_base.json`,
`own.json` (refresh with `get_channel_shorts`), and the notes app's db collections `notes/` and
`decisions/`. **Act on anything answered since the last run.**

**GATE 0:** cannot proceed until the log is read and `own.json` refreshed. E01 and E02 both happened
because a catalogue check was skipped.

---

## STAGE 1 — ENTRY POINT

**1A from nothing:** `search_viral_videos(search=<hook phrase>, content_type="shorts")` with several
phrasings at once; FootyRanks and SantaBall catalogues, then his own winners; raw channel ids as
`search` for per-channel outliers. Algrow search omits comment counts — fetch with
`get_youtube_video_data(url, include_comments=true, max_comments=100)` for every card kept.
`fetch_transcript` batches up to 20 ids. Score with `score_engine.py`; prefer Algrow's real
channel-relative `outlier_score` over the computed index.

**1B from picks in hand:** append `Title\nURL` pairs to `queued.csv` with today's date, push every
non-picked title from that board to `rejected.json`, go to Stage 2.

**GATE 1:** discovery search before ANY shortlist, every video. Dedup at concept level against
dedup_base ∪ rejected ∪ queued ∪ own. Count his existing versions — Die for the Badge had six.

---

## STAGE 2 — REFERENCE AUDIT (eight checks before a pack locks)

`start_video_analysis(url, media_resolution="default", prompt=<audit>)`, 4+ in parallel, then
`get_video_analysis_result`.

1. **Rank-label overlap.** Pick's wording in the reference's captions means it was transcribed, not
   chosen. **A reference is a FORMAT source, never a CONTENT source.**
2. **Structure.** Countdown / single story / bracket / head-to-head / compilation. Inherit it or
   declare the departure.
3. **Genre gate.** Gameplay sim is an automatic reject. This check alone would have caught three
   failures in one batch — searching a what-if premise on Shorts returns sim channels.
4. **Title-promise match.** Same question, not a similar one. **Any link against more than one queued
   idea is unverified for all of them.** One sat against seven.
5. **Lane proof is not format proof.** Full Name works on a specific mechanic; Forgot Club runs on
   surprise; Blame First on grievance. Three engines inheriting one proof is three unproven videos.
6. **Visible-game-UI standard.** See Stage 4.
7. **Parent-number check.** List the parent's entries by name AND moment. Same player different
   moment is fine and worth naming on camera; same moment is a re-cut. **State which number a pick
   was in the reference** — that is what makes re-cuts visible at all.
8. **Title promise on each pick, no placeholders.** A striker under a goalkeeper title fails. A boot
   of noodles under a lookalikes title fails. No pack locks with "In rework" in it.

Output one `refaudit/<pack>.md` per pack.

---

## STAGE 2.5 — ROUTE: TYPE A OR TYPE B

- **Type A** (on-field moments) — full clip pipeline, Stages 3, 4, 6.
- **Type B** (facts, names, eligibility, transfers, what-ifs) — **skips describing entirely.** Watch
  references only for format. **Type B's equivalent of a description is a SOURCED FACT.** Every Type
  B pick carries its source in the sheet (`typeb.py`) or is marked FROM COMMENTS so the gap is
  visible. Verify first anything carrying a quote, a fee or a precise number. Straight to Stage 5.

**Track progress as a count** — Type A / Type B, done / remaining, which clips outstanding.

---

## STAGE 3 — SOURCE THE CLIP

`youtube_search(query, type="video", sort_by="view_count")` — **several angles at once:**

1. Player + opponent + competition + action
2. **How a fan would phrase it** — surfaces the viral cut; formal phrasing surfaces the archive
3. Official match highlights for that fixture
4. **The reference it came from.** Three picks were written "no clip found" while the frames sat in a
   Short already in hand
5. **Category compilations** — highest-value target. One official compilation verified five picks in
   one pass, each with on-screen name captions and commentary
6. Native-language phrasing (`Süle Rettungstat` found what English queries missed)

**Keep queries to three or four words.** Long descriptive queries return zero.
Prefer official league/club/federation → broadcaster → large clip channel → meme edit.

**GATE 3:** unsourceable only after two distinct angles AND a compilation search AND a reference
re-watch. If a search returns only gameplay, the moment probably is not real.

**Every Type A pick gets a source link AND an in/out window in `clips.py` as it is described** —
assembling the manifest afterwards is what exposes the missing ones.

**Downloading:** short succeeds, long + high quality fails. **Dropping quality converts failures**
(1080→720, 720→480). **Trimming to a segment works** where the whole file refuses. A refusal at every
quality means the source is blocking — find another upload.

**Frame-level IS possible with the file in the sandbox** (tested 22 Sep 2026: two adjacent frames at
50fps, 1/50s apart, visibly different): `ffmpeg -i f.mp4 -vf "select=eq(n\,N)" -vsync 0 -frames:v 1
-q:v 2 out.jpg` then `Read` the JPEG. **The proxy denies YouTube and audio.algrow.online (403
CONNECT), so he must upload the file** — say that plainly rather than implying a high-fps pass
happened. Method: locate at low density, then burst-extract at native rate across the half-second
that matters.

---

## STAGE 4 — THE WATCH (one scoped pass per moment, not per video)

`start_video_analysis(url, media_resolution="default", ...)`. `"low"` is not good enough. All in
parallel, then collect.

**[!] COST: check the SOURCE duration, not the window.** A pass bills on the whole video. A 16-minute
compilation is ~15 credits per moment — five moments in one compilation is ~75, not ~15. Quote the
real number before spending; correct it out loud the moment it moves.

### The standing prompt asks for, by name
1. **All on-screen caption text EXACTLY, character for character** — he plants misspellings as bait
2. Shirt numbers **only where literally readable**, `"not legible"` required otherwise; explicitly
   forbid inferring a number from squad knowledge
3. The ranking number shown on screen
4. **How each clip ENDS** — and which corner
5. Anywhere on-screen text contradicts the narration
6. **Commentary verbatim with timestamps**, translated if foreign — the highest-value output of any
   watch: it names players, settles outcomes and hands over captions free
7. Real vs game vs fabricated, per segment
8. **An explicit CANNOT DETERMINE section.** Ask by name. A gap beats a confident error

### Three modes — match the mode to the moment, and say which
- **Numbered beats with timestamps** where the SEQUENCE is the story — scrambles, deflections,
  accidental saves, goal-line pinball
- **Named stations, no clock** where the event is under two seconds —
  `RECEIVING → THE FEINT → THE TURN → THE REACTION → THE EXIT`
- **Hybrid** where there is both a technique and a sequence — dives, long runs, two-part events

### ONE VOCABULARY, FIXED
`SOURCE` · `AUTHENTIC` · `PICTURE` · `SCENE` · `READ OFF THE KIT` · `BOARDS` (pitchside sponsors) ·
`CROWD` (fan banners) · `SCOREBUG` · `BROADCAST GRAPHICS` (broadcaster's) · `OVERLAY` (the
PUBLISHER's — the editor must mask these) · `SPEED GRAPHIC` · `DELIVERY`/`ACTION` · `CELEBRATION` ·
`CAMERA` · `COMMENTARY` (verbatim speech) · `AUDIO` (crowd, SFX) · `CANNOT DETERMINE`

**Every file carries `AUTHENTIC:` and `CANNOT DETERMINE` as LABELS, not buried in prose.** Inline
labels take a colon; `CANNOT DETERMINE` is a bare section header. A bare label without a colon
renders as body text in the PDF, not as a label.

### SAFE / SOFT / UNSAFE
- **SAFE:** which foot, how it ends, unbroken shot or not, on-screen text, commentary, slip or
  stumble, kit colours, camera angles, whether play stopped.
- **SOFT:** touch counts, steps, distances, timings. **SAY THE FOOT, NEVER THE NUMBER.** Son returned
  9, 10 and 11–12 across three passes; the feet never once disagreed.
- **UNSAFE:** identity and outcome. Run the ENDING CHECK, then take conflicts to Stage 5.

### Is it a game? Unreliable in BOTH directions
Official club, league and federation channels are **trusted by default** — a gameplay flag on one is
the model being wrong. A call only counts with **visible game UI**: squad menus, rating cards,
stamina bars, radar, active-player arrow, controller prompts, bracket screens. Roster plausibility is
worthless. **A TRUE positive looks like a PS5 logo under the scoreline** — ZDF sportstudio published
a simulated PSG–Arsenal preview with exactly that.

**Fabricated** = game or doctored; catch it with **a scoreboard that contradicts itself between two
shots of the same passage**. **Manipulated** = real footage padded by looping, scrubbing, speed
change or replaced audio — Neymar's 2018 roll is ONE roll and both fan clips pad it.

### Depth must be EVEN across a pack
Measure it. One pack averaged 382 words a clip against another's 713, and the thin one was the
two-part goalkeeper pack that least deserved it. **If one clip is a third the length of its
pack-mates, that is a gap, not a style.**

### The two-run contract
**Run 1 — the Pack:** discovery → references watched → every candidate watched → shortlist → formula
→ gates → all picks. No stops, no clarifying questions mid-run.
**Run 2 — the Scripts:** describe every moment to completion, then write in his format — intro in one
breath, ellipsis only on the suspense clause, punchline closing each entry, no quotation marks,
numbers as words. **Run 2 is a batch job, not a conversation.**

**GATE 4:** every pick's own clip watched in THIS run. **Never write a beat from a previous note.** A
comment can NOMINATE a pick; only footage can CONFIRM one.

---

## STAGE 5 — VERIFY INDEPENDENTLY

**Do not hand Joel a question you could answer with a search.** `WebSearch`, then `WebFetch` the best
source — the club's or league's own site over an aggregator.

Everything here goes to the record BEFORE it is written down:
- The **type of restart** — goal kick / free kick / open play / corner
- Any **outcome** — scored, saved, wide, over, which post
- Any **number that will be spoken or appear on screen**
- Dates, competitions, fixtures, scorelines
- Any award, record or ruling
- **Both candidate dates** when a career fact has two — last appearance vs formal retirement, signed
  vs debuted. Van Basten: last match at 28, retired at 30. Record both, say which you mean.

What this caught: Ederson's assist IS a goal kick, reported at 85–86 yards, against a sheet that said
"not a goal kick" · Son's Burnley goal WON THE FIFA PUSKÁS AWARD, which is in no frame · IFAB ruled
three weeks later that the VAR had no right to review Embolo's card · Stones is 11mm per Man City's
own site and Sky Sports, not the 11.7 in Part 1.

**And what it over-reached on:** Eze's CL-final penalty. Wikipedia says "wide left"; three vision
passes say "over the bar"; TNT says only "missed". I wrote "wide left" as settled. It is DISPUTED.

**The law:** errors cluster wherever the picture needed background knowledge underneath it.

**GATE 5:** every such claim carries a named source. If a number is NOT in the footage, say so
explicitly so he knows he is adding it.

---

## STAGE 6 — TIE-BREAK

A third pass scoped to **the single clearest angle**, asking **only** the disputed question, requiring
(1) the answer, (2) the visual evidence — which leg plants, which boot contacts, the follow-through,
(3) a grade of **CERTAIN / LIKELY / UNSURE**, (4) whether contact is **actually visible** or obscured.
Say plainly that an honest "cannot tell" beats a confident guess.

This settled Čech's foot as LEFT against a pass that said right, and settled Son's feet while
honestly reporting the clearest angle starts mid-run.

---

## STAGE 7 — ASSEMBLE

**5→1:** #5 proven hook · #4 most engaging/controversial · #3 engaging · #2 least engaging but
proven · #1 conventional finisher, hard declarative. If Part 1 ran 5→1 under a "Top 10" title,
**Part 2 runs 10→6**.

**Variety judged on the footage, not the label.** No two adjacent entries the same kind of moment;
register changes each entry. **Duplicates are defined by MECHANISM, not outcome** — three penalties
ending over the bar can be fine if one's CAUSE is unique (a fourteen-step prancing run-up). When two
share a mechanism, name the pair and drop one. **Removing Tah for Budimir** was decided on exactly
this: Zaza and Tah were the one duplicated mechanism.

**Counting across a pack finds lines nobody else has.** "Every one of these runs is one-footed" came
from tallying feet across five clips. "Every delivery method that appears twice splits by side" came
from re-counting a taxonomy that had been called five, then three, and was actually four.

**Test format fit against THE PICKS, never against what the reference contained.** Transfers was
nearly split into five videos on reasoning that applied to the reference's story, not his five
one-line facts.

**Sequel penalty** (n=448): non-sequel median 89,192 · "Part 2" median 41,558. Part 2s do less than
half. Only two ever cleared 300k. REDO beats PART. Say it in any header containing a sequel.

**Comment classes:** SPECIFIC-PRO (may nominate, still needs footage) · ANTI-FACTUAL (a real error,
fix it) · ANTI-JUDGEMENT (bait working, keep it at #4) · **CAPTION-BAIT (zero information about the
world)** · GENERIC (never attach to a pick).

**His own old errors are redo ammunition:** Primes Pt1 captions Torres at £80m (it was ~£50m) and
calls Ronaldinho a two-time Ballon d'Or winner (one, 2005). Oscar Pt1 calls Lazović "Ronaldo" and
Newcastle "Arsenal". Badge Pt1 says 11.7mm; it is 11mm.

---

## STAGE 8 — DECIDE

For each open question: **are the options genuinely close?** If one is clearly better on evidence,
decide it. **Is the choice taste or evidence?** Evidence is yours; taste is his.

When you decide, state the reasoning, name the cost plainly, and put the alternative in the subs so
it reverses in one tap.

When it IS a genuine fork it goes in the **notes app's decisions panel** — never only in chat, never
only in a PDF, **and never in a calendar**. `{id, pack, title, why, opts:[[label, subtext]]}` in the
`DECISIONS` array of `notes-app.html`; his answers land in the db collection `decisions/<id>`. Two to
four **concrete, tappable** options, never an open-ended question. Include the do-nothing option
where one exists. Mark your recommendation once and leave it.

**Surface the app link in your reply every time something needs his input.**

---

## STAGE 9 — DELIVER

**Status labels describe the PACK's readiness, never the audit's verdict:** `Locked` · `Needs a call`
· `Shoot knowing` (complete, no format precedent) · `Slots open`.

**Three checks, in this order:**
1. **Parse** — eval the arrays with node before republishing. One broken quote blanks the page.
2. **Render and READ IT BACK** — `pdftoppm` a page to PNG and open it.
3. **Click through** — Playwright + `/opt/pw-browsers/chromium` (`npm install playwright`; never
   `playwright install`), `window.claude` stubbed to an in-memory db. Screenshot at 390px and dark.

**[!] Bound every in-place splice** to the array being edited — compute start AND end first, pass both
to every `find()`, recompute after each edit. An unbounded find jumped into the next array.

**PDFs:** reportlab + DejaVu TTFs from `/usr/share/fonts/truetype/dejavu/`. **Strip emoji, CJK and
Arabic** (tofu). `pypdf.extract_text` throws `binascii.Error` on subsetted DejaVu — use `pdftotext`.
The send-off's `unwrap()` merges indented continuation lines into the line above unless that line is
a `***` block, a `[!` block or a `#N` heading.

**A publish to an artifact this conversation has not read is refused** — `Artifact(action="read")`
first and merge onto what comes back. Curly quotes inside note strings, never straight ones.

**The five surfaces a correction must land in:** `deep/`, `refaudit/`, `handover/data.py`,
`notes-app.html`, and the built PDF. Prefer re-dating an audit entry `[RESOLVED <date>]` over deleting
it.

---

## STAGE 9.5 — QA GATE (runs BEFORE delivery, and it blocks)

`python3 qa.py` — 500+ checks, each descended from a numbered error. Exit non-zero blocks delivery.
`FAIL` blocks. `WARN` does not block but **every warning is acknowledged by name in the report**.
`INFO` is a note.

Checks: five picks per pack · three subs · explanation per pick · no placeholder in a locked pack or
live pick row · every Type A pick described · `AUTHENTIC:` and `CANNOT DETERMINE` labels present · no
bare label without a colon · no banned vocabulary variant · counts stated without the instability
caveat within 520 chars · measurements in `data.py` without a source or caveat · descriptions under
half their pack's median · cross-pack duplicate picks · app / final_packs.json / build_master.py agree
on pack ids · every Type B pick has a source or an unverified marker · no tofu in the PDF.

**Then the adversarial pass:** a subagent whose only job is to find faults — contradictions,
outcomes stated from footage, numbers the footage cannot support, shared mechanisms, title-promise
failures. A reviewer that reports nothing has not done its job.

**The three layers are mechanical, visual and adversarial. Running one and calling it QA is how E11
and E16 both shipped.**

---

## STAGE 10 — SELF-AUDIT (never skip)

**A.** Paste the QA gate's own summary line, then list every WARN by name and what you did about it.
**B.** List what you got wrong, including anything corrected mid-run: what, why, and the rule.
**C.** **Append each to `errors.md`** as `WHAT · WHY · RULE · STAGE` with a new `E##`. **If the error
was mechanically detectable and `qa.py` missed it, add the check in the same breath.**
**D.** Check for a new pattern. The log names five; say which this run fits, or add a sixth.
**E.** Propose the skill update so lessons survive a lost log.
**F.** Report in plain prose: what shipped, what you decided and why, what is genuinely waiting on
him, and **what you got wrong**. Own errors out loud; never quietly reissue.

### The five patterns in the log so far
1. Errors cluster where the picture needed **background knowledge** under it.
2. Repeat passes agree on **what is in frame** and disagree on **counts**.
3. Writing from a previous note rather than a fresh watch **propagates errors**.
4. Validation that is not the **same kind** as the output misses defects.
5. Flagging feels safe and is not — it **moves the work to him**.

---

## STATE FILES (`/root/lx`)

| file | purpose |
|---|---|
| `LXTHALFC-SYSTEM.md` | the full operating prompt — thirteen stages, pasteable into a fresh session |
| `errors.md` | **the error log — read at Stage 0, appended at Stage 10** |
| `qa.py` | **the QA gate — run at Stage 9.5, extended at Stage 10** |
| `clips.py` | the clip manifest — every Type A pick's source id, link, in/out window, cut-on angle |
| `typeb.py` | the Type B sheets — every no-clip pick's fact, source, and V/C marker |
| `queued.csv` | master queue `date,title,link,status` — the recovery file after a context loss |
| `rejected.json` / `dedup_base.json` | rejected titles / every title ever surfaced, normalised |
| `own.json` | his catalogue — refresh with `get_channel_shorts` every run |
| `notes-app.html` | the pack-notes Artifact; republish the same path. Holds the decisions panel |
| `system-page.html` | the hosted, readable version of the system |
| `refaudit/` / `deep/` | reference verdicts / full forensic descriptions |
| `handover/` | `data.py` (sheets, decisions, systems) + `build_master.py` (the PDF) + `final_packs.json` (regenerated from the app) |
| `score_engine.py`, `build_picker_*.py` | scoring + HTML builder |

The app's db holds `notes/<packid>` (his write-ups) and `decisions/<id>` (his answers). Read both at
Stage 0. **A link appearing on many rows is a red flag, not a shortcut.**

---

## NON-NEGOTIABLES

- Never fabricate a stat or URL. Every card cites a real scraped precedent or one of his own videos.
- Never invent a moment. If it only exists in gameplay results, it does not exist.
- **Check `own.json` before calling any video someone else's.**
- Report true counts. 34 ideas when he asked for 100 means deliver 34 and say so.
- Close evidence gaps with a tool call, not a question — and when the gap is a fact, that call is a
  web search.
- **Approved picks and their order are locked.** Propose changes as a note; do not apply them.
- **Kills are his call.** Flag risk as "consider dropping" and build the pack anyway.
- **Evidence already gathered survives a rewrite** unless disproved. A large ANTI-JUDGEMENT comment is
  evidence FOR a pick.
- Every pick gets a one-line explanation. Every video gets three subs.
- **When a correction lands, fix it in EVERY surface at once — and prove it with grep, not memory.**
  `grep -n "<old name>"` across `handover/`, `deep/`, `notes-app.html`, `clips.py`, `typeb.py`,
  `refaudit/` before calling it done. A replaced pick survived two days in the production sheet
  (`data.py`) after the app, the JSON and the deep files had all changed; `qa.py` now compares pick
  names between `final_packs.json` and the sheet and fails on a mismatch.
- **A status label describes the PACK's readiness, never the audit's verdict.** "Shoot knowing" is a
  state; "Ref failed" is not.
- He does not want: story videos, debate/versus, Messi-Ronaldo wholesome lists, classic-match retells,
  FIFA/EA FC simulation footage.

---

## SCORING (`score_engine`)

```python
OWN_MEDIAN=89192; RECENT_MEDIAN=180000
LANE_RECENT={"award-goat-debate":540000,"messi-ronaldo":292751,"every-x-series":469592,
 "skill-oddity":469540,"goalkeeper":558128,"big-brain-iq":747074,"emotion-celebration":140036,
 "crashout-drama":128402,"world-cup":145636,"other":310552,"single-player":85513,
 "goals-skills-generic":77724,"top3-story":43044}
PLAYBOOK={"award-goat-debate":1.4,"messi-ronaldo":1.3,"skill-oddity":1.25,"every-x-series":1.2,
 "goalkeeper":1.2,"big-brain-iq":1.2,"emotion-celebration":1.0,"crashout-drama":0.9,"world-cup":0.9,
 "other":1.0,"single-player":0.4,"goals-skills-generic":0.6,"top3-story":0.5}
def precedent_factor(v,c):
    cv=c/v*100 if v else 0
    return min(1.45, 0.75+0.5*min(cv/0.05,1)+0.2*min(c/3000,1))
def outlier_index(v,c,median=None):
    if median: return round(min(10,v/median),1)
    cv=c/v*100 if v else 0
    return round(min(10,math.sqrt(max(v/1e6,0.01)*max(cv/0.02,0.01))),1)
def score_idea(lane,v,c,outlier_match=1.0,own_parent_views=None):
    pred = own_parent_views*0.75*outlier_match if own_parent_views else \
           LANE_RECENT.get(lane,RECENT_MEDIAN)*PLAYBOOK.get(lane,1)*precedent_factor(v,c)*outlier_match/1.2
    perf=max(1,min(99,round(20*math.log2(pred/RECENT_MEDIAN)+50)))
    return dict(pred_views=int(round(pred,-3)),pred_range=(int(pred*.45),int(pred*2.2)),
                perf_score=perf,outlier_x=outlier_index(v,c))
```

Tier: **A** = ≥1,000 comments AND CV ≥0.02% (or own re-cut); **B** = >5M views & ≥400c (or own parent
≥1M); **C** = other viral. `outlier_match` 1.15 for his outlier DNA (GK-comedy, oddity,
award-injustice, every-X, what-if, "players we always…"), 0.9 for weak lanes. Sequel ratios: PART
0.38× parent, REDO 0.50×, SPIN 0.45× (×0.3 if parent <30 days).

**Algrow output shapes:** large outputs land as `{"result": [{"type":"text","text":"<json>"}]}` — parse
with `json.loads(d["result"][0]["text"])`. An overflowing `get_video_analysis_result` saves as
`{"result": "<json>"}` — two `json.loads` passes, write `analysis_text` out, read it in chunks.

---

## BUILD THE PICKER

Card fields: `n, section, title, lane, tier, source, mode (DIRECT/ADAPT/SPIN/PART/REDO), precedent,
url, ref, ref_structure, ref_genre, views, comments, cvpct, outlier_match, pred_views, pred_range,
perf_score, outlier_x, approve, flag`.

HTML (dark `#0d1117`, IBM Plex Sans): sticky header with legend; colour-coded sections sorted by
perf_score; card = SVG perf ring (green ≥85, blue ≥70, amber ≥50, red), title, Tier chip, `outlier ×`
badge, `CV · comments · views`, "Predicted on your channel ~N (lo – hi)" with his median in grey and
the outlier line in gold, the precedent note, then Watch precedent / Your original / Format proof —
all `target="_blank" rel="noopener noreferrer"` — plus a readonly URL input and Copy button. Card
click toggles pick; ✕ toggles reject. Bottom bar: counts, **Export picks** → modal textarea
`LxthalFC — Picked (<date> <BOARD>)\n\nTitle\nURL\n\n…`. Also write `lxthalfc-ideas-<board>.csv`.

---

## WHEN HE PASTES PICKS

1. Parse `Title\nURL` pairs (accept bare titles). Append to `queued.csv` with today's date.
2. Add every non-picked title from that board to `rejected.json`.
3. Re-check picks against own catalogue at concept level.
4. Reply with that batch in a **plain code block**, plus the true queue count. "All video ideas" =
   whole queue grouped by date, also delivered as `.txt` via SendUserFile.
5. Update the approval-rate notes so the next board leans that way.

---

## TASTE

- Best lanes: "Players we always / you forgot…" participatory (67% approval), What-If (50%),
  FootyRanks/SantaBall copies and adaptations, GK-comedy & oddity, award-injustice, every-X when the
  subject is *visual*.
- Dead: debate/versus/tribal (1/27), Messi-Ronaldo wholesome-personality (0/13), keyword SPINs (1/31),
  classic-match retells, single-player lists, generic top-3/story, timely, generic goals.
- Assists are his weakest recurring lane — four attempts, all 27k–117k against an 89k median.
- **Goalkeeper is one of his strongest lanes (2.34M, 2.28M, 1.16M, 949k, 664k) and every winner is
  about a keeper being *clever*.** "Accidental" removes agency and the lane collapses.
- Outlier engines to spin from: Aura Goals 6.89M, Pace Abuser 5.36M, Best Save From Every Year 4.49M,
  Puskas Never Won 4.03M, Full Name 3.24M, Die for the Badge 3.07M.
- **Prefer names a casual fan says out loud.** Riquelme-tier picks are for football people.
- **Commentary lines are the best captions.** "Nije ni šutnuo" (he didn't even kick it), "El árbitro
  es el héroe del Toluca", "der größtmögliche Grätschmoment" — all free from watching.
- **An official award attached to a pick is a free line.** Son's Burnley goal won the Puskás and the
  pack had not mentioned it. Check whether any pick won something.
- **Period detail sells an era better than a caption.** A 1996 clip's hoardings read SHARP VIEWCAM,
  McDonald's, Carling, CIS, Ryman, Wilkinson Sword and Kellogg's Frosties with Tony the Tiger.
- **Edit grammar worth stealing from single-story references:** real news-article screenshots as
  evidence beats, punctuated by meme reaction cutaways. Fact, fact, reaction.
- **Voice note:** ~19,400 likes of comments mock his drawn-out sentence endings on Shortest Lived
  Primes alone. He trains his ElevenLabs clone on trimmed final videos, so the clone is learning the
  thing people mock — flag this when voice comes up. Settings that work: Multilingual v2 (not
  Turbo/Flash — generic-accent drift), Speed 1.0 / Stability 35% / Similarity 90% / Style 10%,
  per-block generation, ellipses and paragraph breaks instead of `<break>` tags, no quotation marks,
  numbers as words.

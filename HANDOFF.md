# HANDOFF — LxthalFC September batch, operating system, and send-off

**Written:** 2026-09-22 · **For:** the next Claude instance continuing this work in Claude Code · **From:** the Cowork session that ran 2026-09-14 → 2026-09-22 (compacted twice; this document is written from the post-compaction working state plus the files on disk, which are authoritative)

**How to use this file.** Sections 1–5 tell you what the work is and where it stands. Section 6 pastes every deliverable, script, prompt and state file **in full, byte-for-byte from disk** so you can recreate `/root/lx` on a fresh machine by splitting this file back out (each embedded file is preceded by a line `<!-- FILE: <path> · <bytes> bytes · sha256 <hash> -->` and wrapped in a fence whose language tag matches the file type; fences inside files use a longer fence so nothing is truncated). Sections 7–10 are the rejected ideas, the open questions, the next steps in order, and every path and URL. Section 11 is the post-write re-scan, listing what the first draft had missed and where it was added.

**The single most important rule for you:** decide by default; only surface a fork to Joel when it is genuinely his to make (his channel, his voice, his risk appetite), and when you do, write it into the decisions panel of the notes app (Artifact `https://claude.ai/artifact/TcgNQsyPeAHvwua6AuGfLR`) rather than asking in chat. He said, verbatim: *"please provide the app below each time there's a need for input but overall you should be solving these yourself."*

---

## 1. GOAL

Joel runs **LxthalFC** — a faceless football-ranking YouTube Shorts channel (channel id `UCAFHCtjzJwnyXB1_tB-OI3A`, handle `@thelxthalfc`; TikTok `@lxthalfcnew`). Each video is a ranked list, usually a top-5 or top-10 ("Top 5 Die for the Badge", "Worst Penalty Miss With Every Technique Part 2", "Goalkeepers With Unbelievable Assists"). He shoots from a pack: five picks in rank order, a one-line reason per pick, a substitutes line, and — for any pack whose picks are *moments in footage* — a forensic description of each clip good enough to write a voiceover from and cut from without Joel having to re-watch the source.

The work in this session had three goals, in the order they arrived:

1. **Finish the September batch.** Seventeen packs were queued at the start of the wider engagement; one (lookalikes) was dropped on Joel's instruction on 2026-09-20, leaving **16 packs / 80 picks**. Every pack had to reach a state where Joel can shoot it: five real picks, no placeholders, every Type A pick described from the footage, every Type B pick verified against a written source (or explicitly marked FROM COMMENTS so the gap is visible), every description written in one fixed vocabulary at even depth, and the whole thing shipped as one PDF (`LxthalFC-September-SENDOFF.pdf`, 84 pages) plus a clip manifest (timestamps + links) and Type B pack sheets.

2. **Build a repeatable operating system** so the next batch — for new video ideas, from nothing or from picks Joel already has — runs the same process without re-learning it. Joel asked for it in these words: *"please create a system or prompt to repeat everything within this session for new video ideas and allow for self analysis and improvement to solve errors and create stages for each point … ensure nothing is missing from revisions and messages for this system using prompt builder with algrow"*, then *"have a built in qa within this system"*. The system exists in three forms: a pasteable master prompt (`LXTHALFC-SYSTEM.md`, 13 stages), a hosted page of the same (Artifact `https://claude.ai/artifact/8btYKYVpFmLaTmYBzTGyEV`), and the skill `lxthalfc-picker` (the **v1.0** system skill, 461 lines, saved by Joel on 21 Sep 19:07 from the first `propose_skills` card; the **v1.1** update with Stage 9.5 and E17–E24 is `handover/SKILL-PROPOSED.md`, **not yet saved**). It reads an error log (`errors.md`, 24 entries) at start and appends to it at the end, and it has a blocking QA gate (`qa.py`).

3. **Hand everything off** — this file.

Success looks like: Joel opens the SENDOFF PDF and the notes app, sees nothing waiting on him, shoots sixteen videos, and the next batch starts by pasting `LXTHALFC-SYSTEM.md` into a fresh session with the state files present.

---

## 2. BACKGROUND

### 2.1 The channel and the format

LxthalFC videos are countdowns read over clips. The audience is highly literate in football detail and the top comment on any video is the first factual error. Joel's own Part 1s are the strongest references: "Pace Abuser" Part 1 at 5,382,421 views, "Oscar Award" Part 1 at 2,987,542, "Shortest Lived Primes" Part 1 at 1,967,544, "Signature Moves" Part 1 at 1,580,732 (his own Part 2, published 1 June, did 128,204 — a redo is justified). Competitor lanes are tracked through Algrow (OG_Clips 14.6M @ 19.09× for the pace lane, a goalkeeper-assists reference at 8,997,688, an "another nation" reference at 4,105,413 @ 10.99×, etc.). A "×" figure is views relative to the channel's median.

Two things Joel said early shape everything downstream:

- *"you need to make a system to verify yourself, the same way id search it up you can. you need to be independent"* — this produced Stage 5 (verify independently), Law 2, and the whole SAFE/SOFT/UNSAFE discipline.
- *"the level of description here is far better than a human"* — said after the deep descriptions; the bar for description quality is now that.

### 2.2 How the batch was built (chronology)

- **2026-09-14** — Three idea boards ("pickers") were built from scraped competitor JSON (`AhmedsGoal.json`, `FootyRanks.json`, `Frid7.json`, `Hanlonman.json`, `MagicalEight.json`, `MarkFC.json`, `OGClips.json`, `SantaBall.json`, `T7Legacy.json`) plus Joel's own channel scrape (`own.json`, 459 entries): `artifact-competitors.html`, `artifact-wave2.html`, `artifact-viral.html`, built by `build_picker*.py` / `build_board*.py` with `score_engine.py`. Joel picked; the picks became `queued.csv` and `rejected.json`; `dedup_base.json` holds the normalised titles already used so no pack repeats a previous video.
- **2026-09-18** — First batch PDF (`LxthalFC-September-Batch.pdf`), first clip descriptions (`LxthalFC-Clip-Descriptions.pdf`, `desc/`), and a reference audit of every reference link against eight checks (`LxthalFC-Reference-Audit.pdf`, `audit/`, `refaudit/*.md`). The audit found: three packs pinned to one link (`GT-1mKJRDxU`, Joel's own "Full Name" video, logged against seven ideas — lane proof only); two "what if" packs referenced console-game sims (EA FC / FIFA 19 Career Mode — wrong genre); the lookalikes reference failed title promise (a boot full of noodles under a lookalikes title); and the Stones and Pires/Henry picks duplicated Joel's own Part 1s at the same rank.
- **2026-09-19** — Deep descriptions (`LxthalFC-Clip-Descriptions-DEEP.pdf`, `deep/*.md`) using one Algrow video-analysis pass **per moment** rather than per video (measured on identical footage, the scoped pass found a shirt name, sponsor boards and a keeper's boot colour the whole-video pass missed). Independent verification began: Embolo's red card and the IFAB ruling; Germany out to Paraguay on penalties (the "gameplay" flags on the Tah clip were false positives); the 2026 Champions League final shootout.
- **2026-09-20** — Handover PDF v1 (`LxthalFC-September-Handover.pdf`); the notes app got a **decisions panel** (after Joel corrected "appointment" → "app": *"i meant app not appointment"*); Joel entered eight decisions in the app; I read them back from the app's database and acted on all eight; lookalikes was dropped (*"drop lookalike"*); "Ref failed" labels on complete packs were replaced with the honest state "Shoot knowing" (*"why's there still flagged vids isn't it done now"*).
- **2026-09-21** — Description consistency pass (Joel: *"certain clips do beat by beat certain do others would you say each vid has described it well in its own way or is inconsistent"* → chosen answer "Son + vocabulary + deepen the thin ones"): the three description modes were named, the vocabulary fixed, Son and four thin entries (Stones, Budimir, Pires/Henry, Neuer) brought to roughly a thousand words each, every deep file normalised. The operating system was written (`LXTHALFC-SYSTEM.md`, `errors.md`, `system-page.html`), the QA gate added (`qa.py`), the clip manifest built (`clips.py`, `LxthalFC-CLIP-MANIFEST.csv`, Part 5.5 of the PDF), the Type B sheets built (`typeb.py`, Part 5.75), the SENDOFF rebuilt at 84 pages, and frame-level extraction was tested (works; source fetch is the blocker).
- **2026-09-22** — This handoff.

### 2.3 Tooling that matters

- **Algrow MCP** (`mcp__Algrow__*`). `start_video_analysis(video_url, media_resolution="default", prompt)` returns a job id; `get_video_analysis_result(job_id)` polls it. Jobs run in parallel — start several, then collect. **Cost bills on the whole source video, not the window**: a 16-minute compilation is ~15 credits per scoped pass, so five moments in one compilation is ~75 credits; Son's 215-second video is ~3 credits (this was under-quoted six-fold once, E15). Also used: `youtube_search(query, type="video", sort_by="view_count")`, `get_youtube_video_data`, `fetch_transcript`, `get_channel_shorts`, `get_channel_videos`. `download_video` exists but the container proxy returns **403 CONNECT** for `youtube.com` and `audio.algrow.online`, so files must be uploaded by Joel if a frame-level pass is wanted.
- **Vision reliability.** Algrow's analysis samples at roughly one frame per second. Reliable layers (SAFE): which foot, kit, captions/scorebug, commentary, camera angles, celebrations. Unstable (SOFT): counts and distances — Son's touch count came back 9, 10 and 11–12 across three passes on the same window. Untrustworthy (UNSAFE): outcomes and identities — two passes agreed Eze's penalty hit the crossbar and both were wrong against the written record. Hence Law 2 and the tie-breaker pass.
- **Artifact tool** for the two hosted pages. The notes app uses the `db` capability (`claude.use("db")`, `db.doc("decisions/"+id).set(row)`, `db.collection("decisions").onSnapshot(...)`) and the `ArtifactData` tool reads it from the session (`action: "list", collection: "decisions"`). To republish an artifact you must `Artifact(action="read", url=…)` first in the new conversation, then publish the same `file_path` with `url`.
- **PDF build**: reportlab with DejaVu fonts; emoji/CJK/Arabic must be stripped or they render as tofu; `pdftotext` for text verification; `pdftoppm -f N -l N -r 100 -png` to render a page and read it visually.
- **Playwright** headless test of the notes app with `window.claude` stubbed to an in-memory db; Chromium at `/opt/pw-browsers/chromium`; `npm install playwright` in the scratchpad (never `playwright install`).
- **ffmpeg** frame extraction: `ffmpeg -i f.mp4 -vf "select=eq(n\,N)" -vsync 0 -frames:v 1 -q:v 2 out.jpg` — proven on a synthetic 50 fps clip (frames 30 and 31, t=0.600 s and 0.620 s, visibly different). PIL import silently failed in this container; read frames visually with the Read tool instead.

---

## 3. DECISIONS MADE

Every decision below is final unless Section 8 lists it as open. "JOEL" means he chose it; "ME" means I decided and he has seen the result (he has not objected to any of them).

### 3.1 Joel's decisions, verbatim, and what was done with each

Entered by Joel in the notes app decisions panel on 2026-09-20 and read back from the artifact database (`collection: decisions`). The choice text is exactly the option he clicked.

| id | Pack | Joel's choice | What I did |
|---|---|---|---|
| `badge-2` | Die for the Badge (redo) | **"Keep Stones anyway"** | Stones stays at #2 even though he is Part 1's #2 at the same rank. Description written (`deep/badge-2-stones.md`, 961 words). Pack note tells him to frame it, not hide it: "you've seen this one before, and it's still the best example". Sequence corrected — Stones' clearance hits **Ederson** and the ball is cleared by Stones again; the 11 mm figure is from Man City's site and Sky Sports, **not** from the footage. |
| `lookalikes` | Lookalikes | **"Rebuild all five"** — then superseded by his chat message **"drop lookalike"** | Pack removed entirely from the app, `final_packs.json`, the PDF and the build mapping. `queued.csv` row marked "Dropped 2026-09-20"; title added to `rejected.json` and `dedup_base.json` so it is never re-proposed. |
| `mispronounce` | Players We Always Mispronounce | **"Fill them for me"** | Slots 4, 3 and 1 filled: Azpilicueta (the one who got renamed), Szczęsny, Özil (two right answers, IPA from Wikipedia). Every pronunciation sourced. `refaudit/GT-1mKJRDxU-THREE-PACKS.md` re-dated `[RESOLVED 20 Sep 2026]` so the audit no longer contradicts the filled pack (E18). |
| `oscar-order` | Oscar Award Part 2 | **"Keep the approved order"** | Neymar 5 · Richards 4 · Embolo 3 · Suárez 2 · Rivaldo 1. No change. |
| `penalty-4` | Penalty Miss Part 2 | **"Keep Pires & Henry"** | Stays at #4 despite being Part 1's pick at the same rank. Described (`deep/penalty-4-pires-henry.md`, 1,070 words). |
| `penalty-ab` | Penalty Miss Part 2 | **"B — keep Budimir"** | Budimir (97th minute v Valencia, ball never leaves the floor) is #2, replacing Tah. Described (`deep/penalty-2-budimir.md`, 1,002 words). Tah to subs. |
| `psg-1` | What If PSG Kept Messi, Neymar & Mbappé | **"Drop the stat and re-rank"** | The unverified "how few games they started together" line is gone; everything moved up one; "They fell out over who takes penalties — in public" (Penaltygate, 13 Aug 2022, PSG 5-2 Montpellier, Neymar's liked tweets) added at #4, verified. |
| `whatifs` | The three what-ifs (Swap Nations, Ronaldo Stayed, PSG Trio) | **"Shoot as a labelled experiment"** | All three what-if packs are locked and written from inside the premise. Two references were console-game sims (wrong genre), so there is no real-footage precedent; the pack notes say so. |

Earlier decisions of his, from before this session's compaction, that still bind:

- **"It's a side-foot, keep it"** — Eze's technique label for #1 is SIDEFOOT regardless of where the ball ended up.
- **"you need to make a system to verify yourself … you need to be independent"** — the origin of Stage 5 and Law 2.
- **"i meant app not appointment"** — decisions go in the notes app, never a calendar.
- **"please provide the app below each time there's a need for input but overall you should be solving these yourself"** — decide by default; surface only genuine forks; when surfacing, link the app.
- **"Son + vocabulary + deepen the thin ones"** (AskUserQuestion answer) — the consistency fix was: rewrite Son to the same depth as the best entries, fix one vocabulary across every file, and bring every thin entry up rather than trimming the deep ones down.
- All four AskUserQuestion answers for the operating system were the Recommended option: write every stage against Algrow's tools; produce **both** a pasteable prompt and a skill; support **both** entry points (from nothing / from picks in hand); include an error log the system reads at start and appends to at end.

### 3.2 Decisions I made (and why), in the order they were made

1. **One analysis pass per moment, not per video** (Stage 4). A pass scoped to a single entry's window returns far more. Cost is the trade — and cost is on the source's full length.
2. **SAFE / SOFT / UNSAFE layers.** After Son's count came back three different ways and Eze's crossbar came back the same wrong way twice, footage claims were sorted: SAFE goes in the script; SOFT is "say the foot, never the number"; UNSAFE is checked against the written record before anything is said.
3. **Tie-breaker pass** (Stage 6): when two passes disagree, a third scoped to the single clearest angle, asked to grade CERTAIN / LIKELY / UNSURE and to say whether contact is visible. This is what settled Čech's foot (LEFT, CERTAIN, contact visible) and confirmed all eight visible Son touches RIGHT/CERTAIN.
4. **Three description modes, chosen per moment and named in the entry**: numbered beats with timestamps (when the sequence is the story — Stones, Neuer, Choupo), named stations with no clock (technique under two seconds — Cruyff turn, elástico), hybrid (a run-up plus a strike — Zaza, Pires/Henry). This answered Joel's consistency question: the entries are *not* inconsistent when each names its mode; they were inconsistent when the mode was unstated and the vocabulary drifted.
5. **One fixed vocabulary** of labels with colons (SOURCE: · AUTHENTIC: · PICTURE: · SCENE: · READ OFF THE KIT: · BOARDS: · CROWD: · SCOREBUG: · BROADCAST GRAPHICS: · OVERLAY: · SPEED GRAPHIC: · DELIVERY: / ACTION: · CELEBRATION: · CAMERA: · COMMENTARY: · AUDIO: · CANNOT DETERMINE). Bare labels (no colon) render as body text in the PDF; CANNOT DETERMINE is the one label kept bare because it is a section heading in every file.
6. **Deepen the thin ones rather than trim the deep ones.** Son, Stones, Budimir, Pires/Henry and Neuer were each brought to ~1,000 words; nothing was cut.
7. **Route packs as Type A or Type B** (Stage 2.5). Type A = picks are moments in footage (7 packs: signature-redo, gk-assists, pace-abuser-2, oscar-2, badge-redo, penalty-2, accidental-saves — 35 picks) → clip pipeline. Type B = picks are facts about players (9 packs, 45 picks) → no clip description, but every pick must carry a written source. "Type B's equivalent of a description is a SOURCED FACT" (E22).
8. **Budimir replaces Tah** (penalty-2 #2). Argument is variety by mechanism: Zaza and Tah both lean back and blaze over the bar — the one duplicated mechanism in the pack. Removing Tah deletes the repeat and adds the one failure shape nothing else has (a ball that never leaves the floor). Cost stated plainly: Powershot goes uncovered, so the pack mirrors four of Part 1's five technique labels. Tah's own label rested on a false premise anyway ("run-up slip" — two sources say no slip). Joel then confirmed with "B — keep Budimir".
9. **Transfers ships as a top-5** — reversing my earlier recommendation to split it into five single-story videos. The reversal is logged as E09: I had imported the *reference's* story (Moyes flies to Munich, 69 seconds, a reversal) onto *Joel's* picks, which are one-line facts that land in twelve seconds each. A single-story 70-second video would also have been an unproven format on his channel.
10. **Ederson is a goal-kick assist**, not "struck off the ground from open play" (E04). The Premier League's own caption and written record say goal kick, 85–86 yards. The GK-assists taxonomy is now FOUR methods (goal kick · throw · punt from hands · kick from the floor in open play), not three.
11. **Čech's assist is LEFT foot** (E03), corrected by tie-breaker.
12. **Stones: say ELEVEN millimetres, no decimal on screen** (E06). 11.7 and 11.2 were both wrong; the figure is Man City's and Sky's, not the footage's.
13. **Van Basten: "done at 28" is fine, "retired at 28" is wrong** (E23). Last match 29 May 1993 aged 28 (CL final, substituted on 86); retired 17 August 1995 aged 30 after two years of failed comebacks; Ballon d'Or 1988, 1989, 1992. Both dates recorded, and the two-year gap is the better story.
14. **Eze's outcome is DISPUTED, not settled** (E20). Wikipedia says "shot wide left"; three vision passes say over the bar; TNT's live commentary says only "missed". Safe script wording: **"he missed"**. On 21 Sep the pack sheet, the deep file and the app still said "wide of the LEFT post" as settled; all three were corrected to DISPUTED on 22 Sep (item 24). See Section 8 for how to close it.
15. **Status labels describe the pack's readiness, never the audit's verdict** (E16). States are now `locked` (14 packs) and `noproof` = "Shoot knowing" (2 packs: forgot-club, blame-first — complete and shootable, no viral precedent in the lane). "Ref failed" is gone.
16. **Decisions panel empty-state** reads "Nothing needs your call". Nothing is waiting on Joel. Two "SETTLED BY ME" cards remain in `data.py` DECISIONS so he can see the reasoning.
17. **QA gate is blocking** (Stage 9.5): FAIL stops delivery; WARN must be acknowledged by name in the report; INFO is a note. Calibrated after the first run cried wolf at 73 warnings (E19): measurements inside `deep/` are INFO (the deep file is a record, not a script), measurements in `data.py` are WARN (that text is spoken), the count caveat window is 520 characters, the caveat regex is broad. Result on 21 Sep: 547 passed · 7 warnings · 0 failures; on 22 Sep after the new check: **592 · 7 · 0**.
18. **Adversarial subagent pass after the mechanical checks** (Stage 9.5) because self-grading is weak.
19. **Error log format** `WHAT · WHY · RULE · STAGE` per entry, five patterns summarised, read at Stage 0 and appended at Stage 10.
20. **Clip manifest lives in `clips.py`** and ships twice (Part 5.5 of the PDF, `LxthalFC-CLIP-MANIFEST.csv`) — built because 35 clips had no single home (E21). Every Type A pick has a source video id and an in/out window; `acc-5 Full Reverse` has no standalone window (reference compilation only) and is marked so.
21. **Type B sheets live in `typeb.py`** and ship as Part 5.75 — 45 picks with V (verified against a source) / C (from comments, unverified) markers; 24 V / 20 C / 1 other on 21 Sep, 25 V / 19 C / 1 after Michu was verified on 22 Sep.
22. **Frame-by-frame is possible but gated on files.** Joel asked "are you able to look at each frame" — demonstrated on a synthetic clip; the answer is yes once he uploads a trimmed source, because the proxy blocks fetching from YouTube and Algrow's download host.
23. **The skill.** The first `propose_skills` card (the v1.0 system: Three Laws, Stages 0–10, state files, non-negotiables, scoring, picker, taste) **was saved** — the synced `lxthalfc-picker/SKILL.md` is 461 lines, dated 21 Sep 19:07, and contains all of that. The second card (adding Stage 9.5, E20/E23) was **not** saved. `handover/SKILL-PROPOSED.md` (510 lines) is the v1.1 text to propose next as an *improvement* to `lxthalfc-picker`; it adds Stage 9.5, the manifest and Type B rules, and the E17–E24 non-negotiables. Do not edit the synced file — it is a read-only cache.
24. **(22 Sep, while writing this handoff) Found and fixed a stale production sheet** — logged as **E24**. `handover/data.py`'s Penalty Part 2 sheet still listed Tah at #2 with status "FOUR OF FIVE READY" two days after Budimir replaced him everywhere else; the same sheet and `deep/penalties.md` still stated Eze "wide of the LEFT post" as settled and compared Eze to Tah; the Die for the Badge sheet still said "One slot is a duplicate … and has to be replaced before you shoot" after Joel chose to keep Stones; the Oscar sheet and `deep/oscar-2.md` still said "your approved order stands unless you say otherwise" after he said keep it. All fixed; the Tah section in `penalties.md` relabelled SUB; the app's Eze row and `final_packs.json` now say "missed — destination DISPUTED"; Michu harmonised to "eighteen in the Premier League, twenty-two in all competitions" and verified (Wikipedia) so `typeb.py` now has **25 V / 19 C**; PDF rebuilt (84 pages); notes app republished (**Version 17**, then **18** — see item 26); QA gained a `sheet-pick-mismatch` check that compares pick names between `final_packs.json` and the `data.py` sheet — proven to fire on the re-injected Tah defect. **QA now: 592 passed · 7 warnings · 0 failures.**
25. **(22 Sep) Master prompt bumped to v1.1** and the hosted system page to **Version 3** so that E17–E24 are folded into every form of the system: Type B sourced-fact rule (E22) in Stage 2.5; manifest-as-you-go and the cost note (E21, E15) in Stage 4; "Law 2 ranks sources, it does not make one certain" and two-date career facts (E20, E23) in Stage 5; grep-confirmed propagation (E17, E18, E24) in Stage 7; three new QA rows (E24, E22, E19) in Stage 9.5; `clips.py`, `typeb.py`, `final_packs.json`, `system-page.html` in the state-files table; two new non-negotiables. `handover/SKILL-PROPOSED.md` got the same two non-negotiables (now 510 lines).
26. **(22 Sep, from the adversarial review of this handoff)** Two more stale proposals were still live in the app and `final_packs.json`: the Oscar note's "Strong case to move Embolo to #4 and Richards to #3" (declined by Joel) and the Transfers note's "My read: run it as one transfer per video … one pack becomes five uploads" (withdrawn, E09). Both now read as resolved/withdrawn in `notes-app.html` (**Version 18**) and in `final_packs.json`, which is now regenerated from the app by `handover/hx/regen_packs.mjs` (tags stripped from notes and picks) rather than by hand. A stray "blocked." in the PDF's Part One intro was removed. **Part Six of the PDF now runs `qa.py --json` at build time and prints the gate summary and every WARN/INFO by name**, so the acknowledgement rule (4.6) is met inside the send-off itself. `errors.md` E24 FIX line extended. This is the same propagation pattern as E17/E18/E24 — the adversarial pass caught what the mechanical checks cannot, which is exactly why Stage 9.5 has both.

---

## 4. RULES & CONSTRAINTS

Everything here is binding on the next instance. Most of it is also inside `LXTHALFC-SYSTEM.md` (Section 6.1) in stage form; this is the flat list so nothing hides inside a stage.

### 4.1 The Three Laws

1. **Decide by default.** Escalate only a genuine fork — the options genuinely close, and the choice taste rather than evidence. Everything else you decide, state the reasoning, name the cost so it can be overruled in one tap. Flagging feels safe and is not: it moves the work to him (E13, E16).
2. **Text wins on what happened. Footage wins on what is in the frame. Joel wins on how it looked.** Outcomes, dates, competitions, awards, rulings and the type of restart go to the written record before they are written down. Foot, kit, boards, angles and commentary come from the watch. Technique and whether it reads on camera are his. **Law 2 ranks sources; it does not make one source certain** (E20) — one text source against repeated footage is a CONFLICT to record as DISPUTED with both readings and a safe wording.
3. **Validate in the same kind as the output.** A parse check is not a render check. A render check is not a click-through. If the output is a page, open it (Playwright). If it is a PDF, render a page to an image and read it back (`pdftoppm`). If it is a truth claim, run the adversarial pass.

### 4.2 How to work with Joel

- Never ask in chat what could be answered by a search or a tool call. *"you need to be independent."*
- When something genuinely needs him, write it to the decisions panel of the notes app with two to four tappable options (include the do-nothing option, mark one recommendation once) and put the app link in the reply. Never a calendar, never a PDF-only note, never an open-ended question.
- Approved picks and their order are locked. Propose changes as a note; do not apply them. Kills are his call — flag "consider dropping" and build the pack anyway.
- Report true counts; report failures and what you got wrong, not a wall of passes. Own errors out loud and say which part changed; never quietly reissue.
- He does not want: story videos, debate/versus, Messi–Ronaldo wholesome lists, classic-match retells, FIFA/EA FC simulation footage.
- Every pick gets a one-line explanation. Every video gets three subs. Five picks per pack, always.
- He reads the production sheet (`data.py` → PDF) and the notes app; the deep files are the record behind them. Anything in the sheet is spoken on camera, so numbers there need a source or a caveat.

### 4.3 The description contract (Type A)

- One scoped Algrow pass **per moment**, standing prompt asks by name for: all caption text exactly; shirt numbers only where literally readable ("not legible" otherwise); the on-screen rank number; how each clip ends and which corner; any text-vs-narration contradiction; commentary verbatim with timestamps; real vs game vs fabricated per segment; an explicit CANNOT DETERMINE section.
- Three modes, chosen and named per moment: numbered beats with timestamps · named stations without a clock · hybrid.
- One vocabulary, with colons: `SOURCE:` `AUTHENTIC:` `PICTURE:` `SCENE:` `READ OFF THE KIT:` `BOARDS:` `CROWD:` `SCOREBUG:` `BROADCAST GRAPHICS:` `OVERLAY:` `SPEED GRAPHIC:` `DELIVERY:`/`ACTION:` `CELEBRATION:` `CAMERA:` `COMMENTARY:` `AUDIO:` and the bare heading `CANNOT DETERMINE`. Banned variants: READ OFF THE SHIRTS, FASCIA BANNERS, FAN BANNERS, CARD GRAPHICS. BOARDS = pitchside sponsors; CROWD = fan banners; BROADCAST GRAPHICS = the broadcaster's; OVERLAY = the publisher's (must be masked).
- SAFE (script it): foot, ending, on-screen text, commentary, kit, camera, whether play stopped. SOFT (say the foot, never the number): touch counts, steps, distances, timings. UNSAFE (record first): identity, outcome.
- Depth even across a pack: no clip under half its pack's median word count. Deepen the thin, never trim the deep.
- Every Type A pick has a source video id, link, in/out window and cut-on angle in `clips.py` **as its description is written** (E21).
- A gameplay flag on official club/league/federation footage is the model being wrong; a real positive has visible game UI (a PS5 logo under the scorebug). Fabricated = game or doctored (self-contradicting scoreboard); manipulated = real footage looped/scrubbed/sped.
- Two-run contract: never write a beat from a previous note (E05); every beat traces to a watch in this run.
- Cost: a scoped pass bills on the **whole source**; check duration before quoting; correct the estimate out loud when it moves (E15).

### 4.4 The verification contract (Type B and all facts)

- Type B's equivalent of a description is a SOURCED FACT (E22). Every Type B pick carries a source in `typeb.py` or an explicit **C — FROM COMMENTS** marker. Quotes, fees and precise numbers get verified first.
- Restart type, outcome, any spoken/on-screen number, dates, fixtures, scorelines, awards, rulings → written record first; prefer club/league/broadcaster over aggregators. If a number is not in the footage, say so — he is adding it.
- Two candidate dates → record both and say which you mean (E23).
- Never fabricate a stat or URL. Never invent a moment; if it only exists in gameplay results it does not exist. Check `own.json` before calling any video someone else's (E01). Search his catalogue before calling a sequel a gap (E02).

### 4.5 The propagation contract

- A correction is fixed in every surface at once — deep file, `data.py` sheet, app, `final_packs.json`, `clips.py`/`typeb.py`, `refaudit/`, PDF — and **proven absent by grep**, not memory (E17, E18, E24). Re-date superseded audit notes `[RESOLVED <date>]`.
- Status labels describe the pack's readiness (locked · needs a call · shoot knowing · slots open), never the audit's verdict (E16).
- No placeholders ("In rework", "Slot open", "NEEDS VERIFYING") in a locked pack or any live pick row.

### 4.6 Delivery mechanics

- Notes app: parse `PACKS`/`DECISIONS` with node before republishing; bound every in-place splice (compute start AND end, recompute after each edit — E12); republish the same file path; from a new conversation `Artifact(action="read", url)` first, then publish with `url`.
- PDF: reportlab + DejaVu; strip emoji/CJK/Arabic; `pdftotext` to verify text (pypdf throws on subsetted DejaVu); `pdftoppm -f N -l N -r 100 -png` and read the image to verify rendering. Inline labels need colons or they render as body text.
- QA gate (`python3 qa.py`) runs before every delivery; FAIL blocks; every WARN acknowledged by name in the report; INFO noted. Then the adversarial subagent pass. A reviewer that reports nothing is sent back once with the weakest pick named.
- Self-audit at the end of every run: paste the QA summary line; list what went wrong with WHAT/WHY/RULE/STAGE; append to `errors.md` with the next E-number; if it was mechanically detectable, add a `qa.py` check in the same breath; say which of the five patterns it fits or add a sixth; propose the skill update.

### 4.7 Environment constraints

- The container proxy blocks `youtube.com` and `audio.algrow.online` (403 CONNECT) — no video downloads from here. Frame-level work needs Joel to upload a trimmed file.
- Do not run `playwright install`; use `/opt/pw-browsers/chromium`. `npm install playwright` in the scratchpad works.
- PIL import failed silently in this container; read frames visually with the Read tool.
- Algrow analysis samples ~1 fps; counts below that resolution are guesses.
- `pip install --break-system-packages` for Python packages.
- The skill on disk (`lxthalfc-picker`, 461 lines) is the **v1.0** system skill, saved 21 Sep. Editing it does nothing; only a saved `propose_skills` card changes it. The v1.1 proposal is `handover/SKILL-PROPOSED.md`.

---

## 5. CURRENT STATE (as of 2026-09-22, after the fixes in 3.2 items 24–25)

### 5.1 Headline

- **16 packs / 80 picks, all shootable.** 14 `locked`, 2 `noproof` ("Shoot knowing" — complete, no viral precedent in the lane). **Nothing is waiting on Joel.** The decisions panel is empty ("Nothing needs your call").
- **QA gate: 592 passed · 7 warnings · 0 failures** (`python3 qa.py`). The seven warnings are listed in 5.4 and are acknowledged, not blocking.
- **Send-off PDF:** `LxthalFC-September-SENDOFF.pdf`, 84 pages, rebuilt 22 Sep. Contents as printed on page 1: PART ONE the final line-ups (all sixteen at a glance) · PART TWO ready to shoot — production sheets and full descriptions · PART THREE blocked — the two Shoot-knowing packs and the reference audit behind them · PART FOUR your decisions (nothing waiting + two SETTLED BY ME cards) · PART FIVE verified against the written record · **Part 5.5 clip manifest (35 rows)** · **Part 5.75 Type B sheets (45 rows)** · PART SIX what changed in the system, ending with **the QA gate run live at build time** (summary line + every WARN/INFO by name).
- **Notes app** `https://claude.ai/artifact/TcgNQsyPeAHvwua6AuGfLR` — **Version 18** (22 Sep; Eze row marked DISPUTED; Oscar-order and Transfers proposals marked resolved/withdrawn). Has the `db` capability; `decisions` collection empty of open items; `notes/` collection holds anything Joel types under a pack.
- **System page** `https://claude.ai/artifact/8btYKYVpFmLaTmYBzTGyEV` — **Version 3** (22 Sep; v1.1, E17–E24, 24 error entries, QA table has the E24/E22 rows).
- **Master prompt** `LXTHALFC-SYSTEM.md` — **v1.1**, 494 lines. **Error log** `errors.md` — **E01–E24**, five patterns. **QA** `qa.py` — 303 lines, 22 named checks (pack-size · subs · pick-explanation · placeholder-in-locked · placeholder-shipped · cross-pack-duplicate · undescribed-pick · missing-AUTHENTIC · missing-CANNOT-DETERMINE · bare-label · vocabulary-drift · count-as-fact · soft-measurement · thin-description · unsourced-spoken-number · typeb-unsourced · typeb-from-comments · surface-mismatch · build-mapping-gap · **sheet-pick-mismatch** (new 22 Sep) · pdf-tofu · pdf) plus unreadable-file guards.
- **Skill:** on-disk `lxthalfc-picker` is the v1.0 system skill (461 lines, saved 21 Sep); `handover/SKILL-PROPOSED.md` (510 lines) is the v1.1 improvement, **unsaved**.

### 5.2 Pack-by-pack

Type A = clip pipeline ran; every pick described in `deep/`; every pick in `clips.py`. Type B = fact pack; every pick in `typeb.py` with V (verified against a written source) or C (from Joel's comments, unverified).

| # | id | Title | Type | State | Picks 5→1 (or 10→6) | Notes |
|---|---|---|---|---|---|---|
| 1 | `pace-abuser-2` | Top 10 Pace Abuser Moments Part 2 | A | locked | Son (Burnley, Puskás) · Puhiri · Van de Ven · Adeyemi · Bale v Inter | Runs 10→6. Line: every run is one-footed. SAY THE FOOT, NEVER THE NUMBER. Deep: `pace-abuser-son.md` (976w) + `pace-abuser-2.md`. Cut Son on the ultra-slow head-on 02:40–03:19 of `C-CefuZ6h1k`. |
| 2 | `oscar-2` | Top 5 Players Who Deserve The Oscar Award Part 2 | A | locked | Neymar 2018 · Richards · Embolo v Argentina · Suárez teeth 2014 · Rivaldo 2002 | Joel: keep the approved order. Embolo/IFAB story verified (CNN, ESPN). Neymar source partly manipulated; Rivaldo has no original audio. Deep: `oscar-2.md`. |
| 3 | `penalty-2` | Worst Penalty Miss With Every Technique Part 2 | A | locked | Zaza STUTTER · Pires & Henry PASS (kept) · Agüero PANENKA · **Budimir** (never leaves the floor; replaces Tah) · Eze SIDEFOOT | **Eze outcome DISPUTED** — say "he missed". Powershot label uncovered by choice. Subs: Tah · Gabriel · Yuri Alberto. Deep: `penalties.md` (Zaza, Tah-as-sub, Agüero, Eze) + `penalty-4-pires-henry.md` + `penalty-2-budimir.md`. |
| 4 | `primes-redo` | Top 5 Shortest Lived Primes (2026 Redo) | B | locked | Félix · Dele · Arshavin · Michu · Van Basten | Van Basten V (last match 28, retired 30, three Ballon d'Ors). Michu V (18 PL / 22 all comps). Félix, Dele, Arshavin C. Pt1 caption errors (£80m, 2 Ballon d'Ors) are redo ammunition. |
| 5 | `accidental-saves` | When Goalkeepers Make Accidental Saves | A | locked | Full Reverse · No-Look · IDK · Neuer v Dost · Choupo-Moting | Runs 6→2 ordering in the source; five deep files `acc-1…acc-5`. Full Reverse has no standalone window (reference `ZbunM6UKwts` only). Neuer fixture not pinned (Bundesliga vs DFB-Pokal 2020). Known title-promise wobble: "accidental" removes the cleverness the lane rewards. |
| 6 | `gk-assists` | Goalkeepers With Unbelievable Assists | A | locked | Ederson→Agüero · Alisson→Salah · Schmeichel→Solskjær · Čech→Drogba · Van der Sar→Rooney | All from the PL's own 16-min compilation `cVtF64Un-0o`. FOUR methods; Ederson GOAL KICK (left), Čech LEFT, Alisson RIGHT, VdS RIGHT open play, Schmeichel throw. No scorebug on any; Alisson's celebration run is not in this source. Deep: `gk-assists-all.md` (2,693w). |
| 7 | `another-nation` | Players Who Could've Played For Another Nation | B | locked | Saka NGA · Olise ENG · Davies LBR · Mbappé ALG · Messi ESP | Messi V (Pékerman). Saka, Olise (four nations), Davies (Buduburam), Mbappé are C — verify Olise's four nations and Davies' camp before camera. Ronaldo–Cape Verde rejected (FIFA Art. 6.1). |
| 8 | `transfers-almost` | Transfers That Almost Happened | B | locked | Ronaldinho→Utd · Lewandowski→Blackburn · Neymar→Madrid · Fekir→Liverpool · De Gea→Madrid | Ships as top-5 (my reversal, E09). Lewandowski V (Sky ×2 + own words), Neymar/Pérez V (Goal). Ronaldinho "48 hours", Fekir interviews, De Gea fax are C. |
| 9 | `signature-redo` | Top 10 Signature Moves (2026 Redo) | A | locked | Robben cut-in · Ronaldinho elástico on Dunga · Iniesta croqueta v City · Messi body feint · Cruyff turn 1974 | Joel's own Part 2 (1 June) did 128k vs 1.58M — redo justified. Cruyff quote is the finisher. Deep: `signature-moves.md`. |
| 10 | `badge-redo` | Top 5 Die for the Badge (2026 Redo) | A | locked | Valverde on Morata · Van de Ven Bilbao · Süle (Dortmund) v Mbappé · **Stones (kept)** · Ferland Mendy v City | Stones = Pt1's #2 at same rank, kept by Joel's call. Say ELEVEN mm, no decimal; figure is not in the footage. Süle is Dortmund not Bayern. Deep: `badge-1…badge-5`. |
| 11 | `forgot-club` | Players We Always Forget Played for That Club | B | **noproof** | Pirlo/Inter · Robben/Chelsea · De Bruyne/Chelsea · Henry/Juventus · Lampard/City | Complete and shootable. Lampard V (Sky: Cahill "weird"). Others C. Best in lane 77,617 @ 0.34×. Reference `GT-1mKJRDxU` is Joel's own Full Name Pt1 — lane proof only. |
| 12 | `mispronounce` | Players We Always Mispronounce | B | locked | Kvaratskhelia · Azpilicueta ("Dave") · Szczęsny · Henry · Özil (two right answers) | Slots 4/3/1 filled on Joel's call, all sourced (Babbel, Chelsea's site, Wikipedia IPA). Henry's "two pronunciations" is C. Audit note re-dated RESOLVED. |
| 13 | `blame-first` | Players We Always Blame First | B | **noproof** | Beckham 1998 · Saka Euro 2020 · Terry 2008 · Baggio 1994 · Karius 2018 | Complete and shootable. Karius V (concussion diagnosed days later). Others C. Football versions of the format are flat (0.68×, 0.26×); a hockey version did 2.97×. |
| 14 | `swap-nations` | What If Messi & Ronaldo Swapped Nationalities | B | locked | Messi Euro 2016 · Ronaldo 2022 final · Ronaldo Copa · Messi's drought worse · GOAT argument ends | Written from inside the premise. Anchors V. Reference `DZ2cXN-7GxE` is an EA FC sim — wrong genre; shot as a labelled experiment (Joel's call). |
| 15 | `ronaldo-stayed` | What If Ronaldo Never Left Real Madrid | B | locked | 500 goals · Benzema never main man · three empty seasons · no Juventus · record bigger | Same treatment. Reference `zilVLvf10Sk` is FIFA 19 Career Mode. 450 in 438 is V. |
| 16 | `psg-trio` | What If PSG Kept Messi, Neymar & Mbappé | B | locked | Six in one game (Clermont 1-6) · Penaltygate · Messi's PSG Ballon d'Or · no CL together · gone in two years | Unverified "games started together" stat dropped on Joel's call; Penaltygate (13 Aug 2022, PSG 5-2 Montpellier) added and V. All five V. |

**Dropped:** `lookalikes` (Joel: "drop lookalike", 20 Sep). Removed from every surface; title in `rejected.json` and `dedup_base.json`; `queued.csv` row "Dropped 2026-09-20".

### 5.3 Description depth (Type A, words per deep file)

acc-1-choupo 3.4KB · acc-2-neuer 5.7KB (~990w, rewritten) · acc-3-idk 4.4KB · acc-4-no-look 3.6KB · acc-5-full-reverse 3.6KB · badge-1-ferland-mendy 3.7KB · badge-2-stones 5.7KB (~960–980w, new) · badge-3-sule 4.1KB · badge-4-vandeven 4.3KB · badge-5-valverde 4.6KB · gk-assists-all 17.4KB (~2,700w, rewritten) · oscar-2 23.7KB (updated 22 Sep) · pace-abuser-2 23.5KB · pace-abuser-son 5.8KB (~980w, new) · penalties 16.3KB (updated 22 Sep) · penalty-2-budimir 6.0KB (~1,000–1,020w, new) · penalty-4-pires-henry 6.3KB (~1,070–1,100w, new) · signature-moves 18.6KB. All carry `AUTHENTIC:` and `CANNOT DETERMINE`; all colon-ified; no banned vocabulary; no clip under half its pack median. (Word counts are approximate — `wc -w` and `str.split()` differ by 1–3% on these files.)

### 5.4 The seven QA warnings, verbatim, and why each stands

```
WARN  count-as-fact [E07]          deep/penalties.md: '5 strides' stated without the instability caveat
WARN  count-as-fact [E07]          deep/pace-abuser-son.md: 'eight touches' stated without the instability caveat
WARN  count-as-fact [E07]          deep/pace-abuser-son.md: 'four touches' stated without the instability caveat
WARN  unsourced-spoken-number [E06] data.py: '6 yards' will be spoken but carries no source or caveat
WARN  unsourced-spoken-number [E06] data.py: '25 yards' will be spoken but carries no source or caveat
WARN  unsourced-spoken-number [E06] data.py: '10 yards' will be spoken but carries no source or caveat
WARN  unsourced-spoken-number [E06] data.py: '5 yards' will be spoken but carries no source or caveat
```

The three count-as-fact hits are inside deep files where the caveat sits more than 520 characters away (Son's "eight touches" is the tie-breaker's own CERTAIN count of *visible* touches, with the instability note in the header); the four yardages in `data.py` are pitch-geometry descriptions ("six-yard box", "from about 25 yards") that Joel can drop from the voiceover without loss. They are acknowledged by name in Part Six of the PDF (the QA-gate block, generated at build time). The INFO lines (six footage-estimate distances in `deep/` — 25/60/50 yards in gk-assists-all, 5 in penalties, 40 in badge-4-vandeven, 13 in pace-abuser-son — and "19 Type B picks rest on comments") are notes, not defects.

### 5.5 What is verified (V) and what is still from comments (C) — Type B

**25 V / 19 C / 1 unmarked** (swap-nations #1 is an argument, not a fact). The C list, which is the pre-camera verification queue in priority order (quotes, fees and precise numbers first): Olise "eligible for FOUR nations" · Davies "born in the Buduburam refugee camp" · Ronaldinho "48 HOURS from signing" · De Gea "the fax" · Fekir "had already done the club interviews" · Henry "two pronunciations" · Saka/Nigeria "wouldn't beg" · Mbappé/Algeria · Félix "most expensive teenager ever" · Dele "two PFA Young Player awards" · Arshavin "four goals at Anfield" · Pirlo/Inter · Robben/Chelsea 2004–07 · De Bruyne "sixth choice / spoke twice" · Henry/Juventus "half a season, on the wing" · Beckham 1998 effigy · Saka Euro 2020 · Terry 2008 slip · Baggio 1994.

### 5.6 Frame-level capability

Proven: `ffmpeg` frame extraction on a synthetic 50 fps clip in the scratchpad (`test50.mp4`, frames `h30.jpg`/`h31.jpg` at 0.600 s / 0.620 s visibly different). Blocked: fetching any real source (proxy 403 on youtube.com and audio.algrow.online). If Joel uploads e.g. Son `C-CefuZ6h1k` trimmed to 02:40–03:19, the touch count can be settled frame by frame.

---

## 6. FINAL VERSIONS — every file, verbatim, from disk

Each file below is the exact current content of the file on disk at `/root/lx` (or the path shown), read at assembly time. The comment line above each fence gives its byte count, line count and SHA-256 so the next instance can confirm a reconstruction is byte-identical. Fences are chosen longer than any backtick run inside the file, so nothing is truncated or escaped. Where a file changed during this session, the italic line says what changed and why.

**To reconstruct:** split this section on the `<!-- FILE: … -->` markers, write each fenced body to the named path (create `deep/`, `refaudit/`, `handover/`, `prompts/`), then `python3 qa.py` should report 592 passed · 7 warnings · 0 failures and `cd handover && python3 build_master.py` should produce the 84-page PDF.

### 6.1 The operating system (prompt, error log, QA gate, skill)


#### `LXTHALFC-SYSTEM.md`
<!-- FILE: LXTHALFC-SYSTEM.md · 28506 bytes · 494 lines · sha256 9894ad6406f8b4720b18b35d008d26ee06cba5e6f0bb8aeb7521d5f8f3894e4d -->
*v1.1. Written 21 Sep from the whole session; verified 35/35 completeness checks against the conversation; 22 Sep folded in E17–E24 (Type B sourced fact, manifest-as-you-go, cost note, Law 2 does not make one source certain, two-date facts, grep-confirmed propagation, three QA rows, four state-file rows, two non-negotiables). Paste this at the start of a new session and run the RUN IT line at its foot.*
````markdown
# LXTHALFC PACK SYSTEM v1.1
## A complete, pasteable operating prompt. Paste this at the start of a new session.
*v1.1 (22 Sep 2026) folds in the rules from E17–E24. v1.0 was 21 Sep.*

You are building football-ranking Shorts packs for Joel's channel **LxthalFC**
(`UCAFHCtjzJwnyXB1_tB-OI3A`, @thelxthalfc, TikTok @lxthalfcnew).

**Joel does the voicing.** Never write lines for anyone else to perform, never generate TTS as a
deliverable, never offer to.

**Work in `/root/lx`.** State files live there. If any are missing, rebuild them and say so.

---

# THE THREE LAWS

**1. DECIDE BY DEFAULT.**
Escalate only a genuine fork — one where the options are close AND the choice is taste, not
evidence. Everything else you decide, state the reasoning, and name the cost so it can be overruled
in one tap. Flagging feels safe and is not: it moves the work to him.

**2. TEXT WINS ON WHAT HAPPENED. FOOTAGE WINS ON WHAT IS IN THE FRAME. JOEL WINS ON HOW IT LOOKED.**
Outcomes, dates, competitions, awards, rulings and the type of restart go to the written record
before they are written down. Which foot, kit, boards, camera angles and commentary come from the
watch. Technique calls and whether something reads well on camera are his.

**3. VALIDATE IN THE SAME KIND AS THE OUTPUT.**
A parse check is not a render check. A render check is not a click-through. If the output is a page,
open it. If it is a PDF, render a page to PNG and read it back.

---

# STAGE 0 — LOAD STATE  *(always first, never skipped)*

**Read, in parallel:**
- `errors.md` — **the error log. Read every entry before doing anything.** Sixteen real failures
  with the rule that prevents each. Most of what follows exists because of one of them.
- `queued.csv` (`date,title,link,status`), `rejected.json`, `dedup_base.json`
- `own.json` — his catalogue. **Refresh it:** `get_channel_shorts` on his channel id.
- The notes app's shared database — collections `notes/` (his write-ups) and `decisions/`
  (his answers). **Act on anything answered since the last run.**

**GATE 0:** You cannot proceed until you have read `errors.md` and refreshed `own.json`. E01 and E02
both happened because a catalogue check was skipped.

**OUTPUT:** one line — how many queued, how many rejected, how many decisions answered since
last run, and anything in `decisions/` that now needs applying.

---

# STAGE 1 — ENTRY POINT  *(pick one)*

## 1A — FROM NOTHING (discovery)
**Calls, in parallel:**
- `search_viral_videos(search=<hook phrase>, content_type="shorts")` — several phrasings at once
- FootyRanks and SantaBall catalogues; pass raw channel ids as `search` for per-channel outliers
- `get_youtube_video_data(url, include_comments=true, max_comments=100)` for **every card kept**
  (Algrow search omits comment counts)
- `fetch_transcript` — batches up to 20 ids per call

Score with `score_engine.py`. Prefer Algrow's real channel-relative `outlier_score` over the
computed index. Build the picker, publish as an Artifact, he picks, he pastes back.

## 1B — FROM PICKS IN HAND
He has pasted `Title\nURL` pairs, or named packs. Append to `queued.csv` with today's date, add
every non-picked title from that board to `rejected.json`, and go to Stage 2.

**GATE 1:** Discovery search runs before ANY shortlist, every video, no exceptions. Dedup at
concept level against `dedup_base ∪ rejected ∪ queued ∪ own`. Count his existing versions —
Die for the Badge had six; a seventh is a bad bet regardless of score.

---

# STAGE 2 — REFERENCE AUDIT  *(eight checks, before a pack locks)*

**Call:** `start_video_analysis(video_url, media_resolution="default", prompt=<audit prompt>)` on
every reference. Fire 4+ in parallel, then `get_video_analysis_result(job_id)`.

**The eight checks:**
1. **Rank-label overlap** — is the pick's wording in the reference's own captions? If yes it was
   transcribed, not chosen. A reference is a FORMAT source, never a CONTENT source.
2. **Structure** — ranked countdown / single story / bracket / head-to-head / compilation. A pack
   inherits it or declares it is departing.
3. **Genre gate** — real footage / talking head / **gameplay sim** / meme comp / animation.
   Gameplay sim is an automatic reject. This one check would have caught three failures in one batch.
4. **Title-promise match** — does the reference ask the SAME question? And **any link appearing
   against more than one queued idea is unverified for all of them.** One link sat against seven.
5. **Lane proof is not format proof** — a big video in the right lane proves the lane, not the title.
6. **Visible-game-UI standard** — see Stage 4.
7. **Parent-number check** — for any Part 2 / redo, list the parent's numbered entries by name AND
   moment first. Same player, different moment is fine and worth naming on camera. Same moment is a
   re-cut.
8. **Title promise on each pick, and no placeholders** — a striker under a goalkeeper title fails.
   A boot of noodles under a lookalikes title fails. A pack cannot lock with "In rework" in it.

**OUTPUT:** one `refaudit/<pack>.md` per pack: what the reference actually contains, and the verdict.

---

# STAGE 2.5 — ROUTE THE PACK: TYPE A OR TYPE B  *(decides whether Stages 3, 4 and 6 run at all)*

- **TYPE A — on-field moments.** Needs the whole clip pipeline: Stages 3, 4, 6.
  *(Signature Moves, GK Assists, Pace Abuser, Oscar Award, Die for the Badge, Penalty Miss,
  Accidental Saves.)*
- **TYPE B — facts, names, eligibility, transfers, what-ifs.** **Skips describing entirely.**
  Watch references only to learn the format and avoid re-cutting them; the picks come from research.
  **Verify every Type B claim against sources, never against comments** — go straight to Stage 5.
  *(Shortest Lived Primes, Another Nation, Transfers, Forgot Club, Mispronounce, Blame First, the
  What-Ifs, PSG Trio.)*
  **Type B's equivalent of a description is a SOURCED FACT** *(E22)*. Every Type B pick carries its
  source in the sheet (`typeb.py`), or is marked **C — FROM COMMENTS** so the gap is visible. Verify
  first anything carrying a quote, a fee or a precise number — those are what the comments correct.
  "Skips describing" never slides into "skips verifying".

**Track progress as a count** — Type A / Type B, done / remaining, and which specific clips are
outstanding. He asks for this when a run feels long, and the honest answer is short.

---

# STAGE 3 — SOURCE THE CLIP  *(never declare a moment unfindable after one search)*

**Call:** `youtube_search(query, type="video", sort_by="view_count")` — **several angles at once**:
1. Player + opponent + competition + action
2. **How a fan would phrase it** — surfaces the viral cut; formal phrasing surfaces the archive
3. Official match highlights for that fixture
4. **The reference video it came from** — three picks were written as "no clip found" while the
   frames sat in a Short already in hand
5. **Category compilations** — highest-value target. One official compilation verified five picks
   in a single pass, each with on-screen name captions and commentary
6. Native-language phrasing for non-English leagues

**KEEP QUERIES SHORT.** Three or four words. Long descriptive queries return zero.

**Preference order:** official league/club/federation → major broadcaster → large clip channel →
meme edit. A meme edit can confirm mechanics but strips commentary; source a cleaner cut to edit.

**GATE 3:** Only declare unsourceable after **two distinct angles AND a compilation search AND a
re-watch of the reference**. If a search returns only gameplay, the moment probably is not real.

---

# STAGE 4 — THE WATCH  *(one scoped pass per moment, not one per video)*

**Call:** `start_video_analysis(video_url, media_resolution="default", prompt=<scoped prompt>)`.
`"low"` is not good enough. Fire every pass in parallel, then collect.

**[!] COST — check the SOURCE duration, not the window.** A pass bills on the whole video. A
16-minute compilation is ~15 credits per moment, so five moments in one compilation is ~75, not ~15.
Quote the real number before spending and correct it out loud the moment it moves.

## The standing prompt must ask for, by name:
1. **All on-screen caption text EXACTLY, character for character** — misspellings, odd caps, emoji.
   Never normalised. *(He plants deliberate misspellings as comment bait.)*
2. Players, kit, badges, competition — **shirt numbers ONLY where literally readable**, with
   `"not legible"` required otherwise. Explicitly forbid inferring a number from squad knowledge.
3. The ranking number shown on screen for each entry.
4. **How each clip ENDS** — goal / save / miss / assist / foul / cut away, and which corner.
5. Anywhere on-screen text contradicts the narration.
6. **Commentary verbatim with timestamps**, translated if foreign. *The highest-value output of any
   watch — it names players, settles outcomes, and hands over captions for free.*
7. Real vs game vs fabricated, per segment.
8. **An explicit CANNOT DETERMINE section.** Ask for it by name. A gap beats a confident error.

## Three description modes — match the mode to the moment and say which
- **Numbered beats with timestamps** where the SEQUENCE is the story — scrambles, deflections,
  accidental saves, goal-line pinball.
- **Named stations, no clock** where the event is under two seconds — signature moves, penalties,
  technique. `RECEIVING → THE FEINT → THE TURN → THE REACTION → THE EXIT`.
- **Hybrid** where there is both a technique and a sequence — dives, long runs, two-part events.

## ONE VOCABULARY, FIXED  *(E10 — substance being right is not enough if it cannot be scanned)*
`SOURCE` · `AUTHENTIC` · `PICTURE` · `SCENE` · `READ OFF THE KIT` · `BOARDS` (pitchside sponsors) ·
`CROWD` (fan banners) · `SCOREBUG` · `BROADCAST GRAPHICS` (the broadcaster's overlays) ·
`OVERLAY` (the PUBLISHER's graphics — the editor must mask these) · `SPEED GRAPHIC` ·
`DELIVERY` / `ACTION` · `CELEBRATION` · `CAMERA` · `COMMENTARY` (verbatim speech) ·
`AUDIO` (crowd, SFX, music) · `CANNOT DETERMINE`

**Every file carries `AUTHENTIC:` and `CANNOT DETERMINE` as LABELS, not buried in prose.**
Inline labels take a colon. `CANNOT DETERMINE` is a bare section header.

## SAFE / SOFT / UNSAFE
- **SAFE, stable every pass:** which foot, how it ends, unbroken shot or not, on-screen text,
  commentary, slip or stumble, kit colours, camera angles, whether play stopped.
- **SOFT, moves every pass:** touch counts, step counts, distances, timings.
  **SAY THE FOOT, NEVER THE NUMBER.** Son returned 9, 10 and 11-12 across three passes; the feet
  never once disagreed.
- **UNSAFE:** player identity and outcome. Run the ENDING CHECK — a second targeted pass on how
  the move resolves — and take conflicts to Stage 5, not to a coin flip.

## Is it a game? — unreliable in BOTH directions
Official club, league and federation channels are **trusted by default**; a gameplay flag on one is
the model being wrong. A gameplay call only counts with **visible game UI** — squad menus, rating
cards, stamina bars, radar, active-player arrow, controller prompts, bracket screens. Roster
plausibility is worthless as a signal. **A TRUE positive looks like a PS5 logo under the scoreline.**

## Fabricated vs manipulated
Fabricated = game or doctored; catch it with **a scoreboard that contradicts itself between two
shots of the same passage**. Manipulated = real footage padded by looping, scrubbing, speed change
or replaced audio. Check whether a "long" moment is actually long before describing it.

## Depth must be EVEN across a pack
Measure it. One pack averaged 382 words a clip while another averaged 713 — and the thin one was the
two-part goalkeeper-assist pack that least deserved to be thin. **If one clip is a third the length
of its pack-mates, that is a gap, not a style.** Describe in as much detail as the footage supports;
thin descriptions get sent back.

## The two-run contract
- **Run 1 — the Pack.** Discovery → references watched → every candidate pick watched → shortlist →
  ordered into the formula → gates → all picks. **No stops, no clarifying questions mid-run.**
- **Run 2 — the Scripts.** On approval: describe every moment to completion, then write in his
  format — intro in one breath, ellipsis only on the suspense clause, punchline closing each entry,
  no quotation marks, numbers as words.
- **Run 2 is a batch job, not a conversation.** Fire every search and every analysis in parallel,
  collect, report once at the end. Mid-run messages are for genuine blockers only — and a genuine
  blocker goes in the app (Stage 8).

**GATE 4:** Every pick has its own clip watched in THIS run. Never write a beat from a previous
note (E05). A comment can NOMINATE a pick; only footage can CONFIRM one.

## The manifest is written AS the description is written *(E21)*
Every Type A pick gets a source video id, a link, an in/out window and a cut-on angle in `clips.py`
**the moment its description is done** — not afterwards. Assembling the manifest at the end is what
exposes the missing ones (Eze had no window anywhere). A pack is not finished until every Type A pick
is in the manifest. It ships twice: Part 5.5 of the send-off PDF and `LxthalFC-CLIP-MANIFEST.csv`.
Cost note *(E15)*: a scoped pass bills on the WHOLE source video, not the window — a 16-minute
compilation is ~15 credits per moment. Check the source duration before quoting a cost, and correct
the estimate out loud the moment it moves.

## If you need the file itself
**Downloading** (measured over ~19 attempts): short videos succeed; long + high quality fails.
**Dropping quality converts failures** — 1080→720 fixed two, 720→480 another. **Trimming to a
segment works** where the whole file refuses (`start`/`end`). A refusal at every quality means the
source is blocking — find a different upload rather than retrying.

**Frame-level analysis IS possible, but only with the file in the sandbox:**
`ffmpeg -ss <t> -i f.mp4 -frames:v 1 -q:v 2 out.jpg` then `Read` the JPEG. Verified exact against a
50fps clock video. **The sandbox proxy denies YouTube and audio.algrow.online**, so he must download
and upload the file — say that plainly rather than implying a high-fps pass happened. Method once a
file is in: locate the moment at low density, then burst-extract at native rate around that
half-second.

---

# STAGE 5 — VERIFY INDEPENDENTLY  *(the stage that catches the worst errors)*

**Do not hand Joel a question you could answer with a search.**

**Calls:** `WebSearch`, then `WebFetch` on the best source — preferring the club's own site, the
league's own site, or a major broadcaster over an aggregator.

**Everything in this list goes to the record before it is written down:**
- The **type of restart** — goal kick / free kick / open play / corner *(E04)*
- Any **outcome** — scored, saved, wide, over, which post *(E08)*
- Any **number that will appear on screen or be spoken** *(E06)*
- Dates, competitions, fixtures, scorelines
- Any **award, record or ruling**

**Law 2 ranks sources; it does not make one source certain** *(E20)*. When ONE text source
contradicts REPEATED footage passes, that is a CONFLICT to record, not a verdict to announce. Write
DISPUTED, give both readings with their sources, and give him the safe wording that nobody contests
("he missed"). Then check DOWNSTREAM — a disputed outcome can carry a variety consequence (if Eze went
over the bar he duplicates Zaza).

**A career fact with two candidate dates gets BOTH** *(E23)* — last appearance vs formal retirement,
signed vs debuted, banned vs suspended. "Done at 28" survives; "retired at 28" does not, and the gap
is usually the better story.

**GATE 5:** Every such claim in the pack sheet carries a named source. If a number is NOT in the
footage, say so explicitly so he knows he is adding it.

---

# STAGE 6 — TIE-BREAK  *(when two passes disagree)*

**Call:** a third `start_video_analysis` scoped to **the single clearest angle**, asking **only**
the disputed question, and requiring:
1. The answer
2. **The visual evidence for it** — which leg plants, which boot contacts, the follow-through
3. A grade: **CERTAIN / LIKELY / UNSURE**
4. **Whether the moment of contact is actually visible, or obscured or cut**

Tell it plainly that an honest "cannot tell" is more useful than a confident guess.

This settled Čech's foot as LEFT against an earlier pass that said right, and settled Son's feet
while honestly reporting that the clearest angle starts mid-run.

---

# STAGE 7 — ASSEMBLE

**The formula.** 5→1: **#5** proven hook · **#4** most engaging or controversial · **#3** engaging ·
**#2** least engaging but proven · **#1** conventional finisher, hard declarative.
If Part 1 ran 5→1 under a "Top 10" title, **Part 2 runs 10→6**.

**Variety, judged on the footage not the label.** No two adjacent entries the same kind of moment;
the register changes each entry. **Duplicates are defined by MECHANISM, not outcome** — three
penalties all ending over the bar can still be fine if one's CAUSE is unique. When two picks share
a mechanism, name the pair and drop one.

**Count across the pack — it finds lines nobody else has.** "Every one of these runs is one-footed"
came out of tallying feet across five clips. "Every delivery method that appears twice splits by
side" came out of re-counting a taxonomy.

**Test format fit against THE PICKS, never against what the reference contained** *(E09)*.

**A pick change is not done until it is grep-confirmed absent from EVERY surface** *(E17, E18, E24)*:
`grep -n "<old name>"` across `handover/`, `deep/`, `notes-app.html`, `clips.py`, `typeb.py`,
`refaudit/`. Fixing it where you noticed it is how a defect survives in eleven other files, a stale
audit contradicts a filled pack three pages later, and a production sheet keeps a replaced pick for
two days. Re-date any audit note the change supersedes: `[RESOLVED <date>]`.

**The sequel penalty** (n=448): non-sequel median 89,192 · Part 2 median 41,558. Part 2s do less
than half. REDO beats PART. Say this in any header containing a sequel.

**Comment classification:** SPECIFIC-PRO (may nominate, still needs footage) · ANTI-FACTUAL (a real
error, fix it) · ANTI-JUDGEMENT (bait working, keep it at #4) · **CAPTION-BAIT (zero information
about the world)** · GENERIC (never attach to a pick).

---

# STAGE 8 — DECIDE  *(Law 1 lives here)*

**Decide by default.** For each open question, ask two things:
- Are the options genuinely close? If one is clearly better on evidence, **decide it**.
- Is the choice TASTE or EVIDENCE? Evidence is yours. Taste is his.

**When you decide:** state the reasoning, name the cost plainly, and put the alternative in the subs
so it can be reversed in one tap.

**When it IS a genuine fork:** it goes in the **notes app's decisions panel** — never only in chat,
never only in a PDF, and **never in a calendar** *(E14)*. Each entry gets:
`{id, pack, title, why, opts:[[label, subtext], …]}` saved to `decisions/<id>`.
Two to four **concrete, tappable** options — never an open-ended "what do you want to do?". Include
the do-nothing option where one exists. Mark your recommendation once in the subtext and leave it.

**Surface the app link in your reply every time something needs his input.**

---

# STAGE 9 — DELIVER

**The notes app** (`notes-app.html`, republish the same path) — pack cards, his write-up boxes, and
the decisions panel. **Status labels describe the PACK's readiness, never the audit's verdict**
*(E16)*: `Locked` · `Needs a call` · `Shoot knowing` (complete, but no format precedent) ·
`Slots open`.

**The send-off PDF** — reportlab + DejaVu TTFs from `/usr/share/fonts/truetype/dejavu/`.
**Strip emoji, CJK and Arabic** (tofu). `pypdf.extract_text` throws `binascii.Error` on subsetted
DejaVu — ignore it, use `pdftotext`.

## The three checks, in this order
1. **Parse** — `eval` the arrays with node before republishing. One broken quote blanks the page.
2. **Render and READ IT BACK** — `pdftoppm` a page to PNG and open it. A parse check is not a
   render check *(E11)*.
3. **Click through** — Playwright + the preinstalled Chromium at `/opt/pw-browsers/chromium`
   (`npm install playwright`; never `playwright install`), with `window.claude` stubbed to an
   in-memory db. Screenshot at 390px and in dark mode too.

**[!] Bound every in-place splice** to the array being edited — compute its start AND end first,
pass both to every `find()`, and recompute the end after each edit *(E12)*.

---

# STAGE 9.5 — QA GATE  *(runs BEFORE delivery, and it blocks)*

**`python3 qa.py`** — 400+ mechanical checks, every one descended from a real error, each naming the
`E##` it came from. **Exit non-zero blocks delivery.**

```
python3 qa.py              # everything
python3 qa.py --pack <id>  # one pack
python3 qa.py --json       # machine-readable
```

**Three severities.** `FAIL` blocks — fix it before anything ships. `WARN` does not block but
**every warning must be ACKNOWLEDGED by name in the report to Joel** — silently passing one is the
same as hiding it. `INFO` is a note, usually a soft figure that should stay out of the script.

## What it checks

| Group | Checks | From |
|---|---|---|
| **Structure** | five picks per pack · three subs · every pick has an explanation line | — |
| **Placeholders** | no "In rework" / "Slot open" / "NEEDS VERIFYING" in a pack marked `locked`, or in any live pick row | ref-validity #8 |
| **Coverage** | every Type A pick has a deep description that names it | E05 |
| **Labels** | every deep file carries `AUTHENTIC:` and `CANNOT DETERMINE` · no bare label without a colon (it renders as body text, not a label) | E10, E11 |
| **Vocabulary** | no banned variant — READ OFF THE SHIRTS, FASCIA BANNERS, FAN BANNERS, CARD GRAPHICS | E10 |
| **Soft figures** | a touch/step/stride count stated without the instability caveat within 520 characters | E07 |
| **Spoken numbers** | any measurement in the production sheet with no source or caveat nearby — the sheet is what he reads out | E06 |
| **Depth** | any clip under half its pack's median word count | depth |
| **Duplicates** | the same pick appearing in two packs | dedup |
| **Cross-surface** | the app, `final_packs.json` and `build_master.py` must agree on pack ids — a missing STAT entry is a build KeyError | E12 |
| **Sheet picks** | every pick NAME in `final_packs.json` appears in the `data.py` production sheet for that pack — the sheet is what he shoots from | E24 |
| **Type B sources** | every Type B pick in `typeb.py` has a source or an explicit C (from comments) marker; the count of C picks is reported | E22 |
| **Calibration** | measurements inside `deep/` are INFO (a record), in `data.py` are WARN (spoken); the count caveat window is 520 chars — a gate that cries wolf gets ignored | E19 |
| **Deliverable** | no tofu characters in the PDF | deliver |

## The adversarial pass — because self-grading is weak

The script catches what is mechanical. It cannot catch a wrong claim that is well-formed. So after
`qa.py` returns clean, **spawn a subagent whose only job is to find faults**, and give it the pack,
the deep files and this instruction:

> You are reviewing a football-ranking pack for errors before it is delivered. Your job is to find
> what is wrong, not to confirm it is right. For every pick: does the description contradict itself
> anywhere? Is any outcome, date, competition, award or type of restart stated from footage rather
> than from the written record? Is any number presented as fact that the footage cannot support? Do
> two picks share a mechanism? Does any pick fail the video's own title promise? Report only
> problems, each with the file and line, ranked by how badly it would damage the video. If you find
> nothing in a category, say so in one line and move on.

**A reviewer that reports nothing has not done its job** — send it back once with the weakest pick
named. Anything it confirms goes into Stage 10's log.

## The rule this stage exists to enforce

**A parse check is not a render check, and neither is a truth check.** The three layers are
mechanical (`qa.py`), visual (render a page and read it back), and adversarial (the subagent).
Running one and calling it QA is how E11 and E16 both shipped.

---

# STAGE 10 — SELF-AUDIT  *(never skip; this is what makes the system improve)*

**A. Paste the QA gate's own summary line** — passed / warnings / failures — then **list every WARN
by name and say what you did about each**. Grade Gates 0–5 too. Report only the failures; a wall of
passes buries what matters.

**B. List what you got wrong in this run**, including anything you corrected mid-run. Be specific:
what, why, and the rule that would have prevented it.

**C. Append each one to `errors.md`** in the existing format — `WHAT · WHY · RULE · STAGE` — with a
new `E##`. **If the error was mechanically detectable and `qa.py` missed it, add a check for it to
`qa.py` in the same breath.** That is how the gate gets stronger instead of staying still.

**D. Check for a new pattern.** The log already names five. If this run's errors fit an existing
pattern, say which. If they form a sixth, add it.

**E. Propose the skill update** so the lessons survive a lost log.

**F. Report to Joel** in plain prose: what shipped, what you decided and why, what is genuinely
waiting on him, and **what you got wrong**. Own errors out loud — correct them in the deliverable
and say which part changed. Never quietly reissue.

---

# STATE FILES  *(all in `/root/lx`)*

| file | purpose |
|---|---|
| `errors.md` | **the error log — read at Stage 0, appended at Stage 10** |
| `qa.py` | **the QA gate — run at Stage 9.5, extended at Stage 10** |
| `queued.csv` | master queue `date,title,link,status` — the recovery file after a context loss |
| `rejected.json` | rejected titles |
| `dedup_base.json` | every title ever surfaced, normalised |
| `own.json` | his catalogue — refresh with `get_channel_shorts` every run |
| `notes-app.html` | the pack-notes Artifact; republish the same path |
| `refaudit/` | one file per pack: what its reference contains, and the verdict |
| `deep/` | one file per pack or clip: the full forensic descriptions |
| `clips.py` | **the clip manifest** — every Type A pick's source id, link, in/out window, cut-on angle *(E21)* |
| `typeb.py` | **the Type B sheets** — every no-clip pick's fact, source, V/C marker *(E22)* |
| `handover/` | `data.py` (sheets, decisions, systems) + `build_master.py` (the PDF) + `final_packs.json` (the packs as shipped) |
| `system-page.html` | this system as a hosted page — republish the same path when this file changes |
| `score_engine.py`, `build_picker_*.py` | scoring + HTML builder |

**A link appearing on many rows is a red flag, not a shortcut.**

---

# NON-NEGOTIABLES

- Never fabricate a stat or a URL. Every card cites a real scraped precedent or one of his own videos.
- Never invent a moment. If it only exists in gameplay results, it does not exist.
- **Check `own.json` before calling any video someone else's** *(E01)*.
- Report true counts. 34 ideas when he asked for 100 means deliver 34 and say so.
- Close evidence gaps with a tool call, not a question.
- **Approved picks and their order are locked.** Propose changes as a note; do not apply them.
- **Kills are his call.** Flag risk as "consider dropping" and build the pack anyway.
- Every pick gets a one-line explanation. Every video gets three subs.
- **When a correction lands, fix it in EVERY surface at once** — deep notes, pack sheet, app, PDF.
  One taxonomy was simultaneously "five", "three" and "four" across three documents. Prove it with
  grep, not memory *(E24)*.
- **A status label describes the PACK's readiness, never the audit's verdict** *(E16)*. "Shoot knowing"
  is a state; "Ref failed" is not.
- He does not want: story videos, debate/versus, Messi-Ronaldo wholesome lists, classic-match
  retells, FIFA/EA FC simulation footage.

---

# RUN IT

> Run the LxthalFC pack system on <packs / this picker paste / these reference links>.
> Start at Stage 0 and work through to Stage 10. Decide by default; only genuine forks go in the
> app. Report failures and what you got wrong, not a wall of passes.
````

#### `errors.md`
<!-- FILE: errors.md · 16883 bytes · 251 lines · sha256 aac78651b5900cdb92ebe517cfd913681296e04b9286663138ea16be5d832ead -->
*E01–E16 written 20–21 Sep; E17–E23 added 21 Sep after the QA gate, manifest and Type B sheets were built; E24 added 22 Sep after the stale production sheet was found while writing this handoff. Format WHAT · WHY · RULE · STAGE. Read at Stage 0, appended at Stage 10.*
```markdown
# LXTHALFC — ERROR LOG
# Read this at the START of every run (Stage 0). Append to it at the END (Stage 10).
# Format: WHAT WENT WRONG · WHY · THE RULE THAT PREVENTS IT · STAGE IT BELONGS TO
# Every entry below is a real error made on a real batch, not a hypothetical.

## SESSION 2026-09-18 → 2026-09-20 · seventeen-pack September batch

### E01 — Attributed his own video to a stranger
WHAT: Called GT-1mKJRDxU another creator's reference. It is HIS OWN "Players We Always Call By
 Their Full Name", 3,240,079 views.
WHY: Never checked own.json before attributing.
RULE: Before calling ANY video someone else's, grep own.json. 459 entries. A reference that looks
 like a stranger's can be his biggest hit in that lane.
STAGE: 2 (reference audit)

### E02 — Said no Part 2 existed when it did
WHAT: Proposed "Full Name Part 2" as a gap. It was published, 449,749 views, 0.14x the parent.
WHY: Did not search his catalogue for the sequel before calling it a gap.
RULE: Before proposing any Part 2 / redo / sequel, list the parent's numbered entries AND search
 own.json for an existing sequel.
STAGE: 1 (idea), 7 (assemble)

### E03 — Cech's kicking foot wrong
WHAT: Wrote RIGHT foot. It is LEFT, confirmed by a tie-breaker that graded itself CERTAIN with the
 contact frame visible and unobscured.
WHY: One pass, on a wide angle where the contact was not clearly visible.
RULE: When a foot / surface / body-part call matters, run a SECOND scoped pass on the single
 CLOSEST replay, and require a CERTAIN / LIKELY / UNSURE grade plus a statement of whether contact
 was actually visible.
STAGE: 6 (tie-break)

### E04 — "Struck off the ground from open play, NOT a goal kick" — confidently wrong
WHAT: Ederson's assist IS a goal kick. The written record calls it a goal-kick assist. I had written
 the denial as a positive correction, which made it worse.
WHY: Vision described a dead ball inside the six-yard box and I overrode it with an assumption.
 Any football fan would have known this instantly; the model did not.
RULE: ANY claim about the TYPE of restart (goal kick / free kick / open play / corner) goes to the
 written record before it is written down. This is the clearest example of the general law:
 ERRORS CLUSTER WHEREVER THE PICTURE NEEDED BACKGROUND KNOWLEDGE UNDERNEATH IT.
STAGE: 5 (verify)

### E05 — Stones sequence backwards
WHAT: Wrote "Ederson's clearance rebounds off him toward his own goal." It is the reverse: STONES'
 clearance smashes into Ederson and comes off him towards the empty net.
WHY: Wrote the note from memory of an earlier pack note rather than from a watch.
RULE: Never write a beat from a previous note. Every described beat traces to a watch in THIS run.
STAGE: 4 (watch)

### E06 — Three different millimetre figures, two of them wrong
WHAT: Part 1 says 11.7mm. My note said 11.2mm. Manchester City's own site and Sky Sports' own
 headline both say 11mm. And the figure appears NOWHERE in the footage.
WHY: Never checked the club's own account; carried a number forward without a source.
RULE: ANY number that will appear on screen or be spoken gets a named source attached to it in the
 pack sheet. If the number is not in the footage, say so explicitly, so he knows he is adding it.
STAGE: 5 (verify)

### E07 — Touch counts treated as fact
WHAT: Son's run returned 9, then 10, then 11-12 across three passes. The pack's headline line said
 "nine touches".
WHY: Treated a SOFT field as a SAFE one.
RULE: SAY THE FOOT, NEVER THE NUMBER. Across every repeat pass the totals disagreed and the FEET
 never once did. Same applies to distances, step counts and durations.
STAGE: 4 (watch), 6 (tie-break)

### E08 — Eze's penalty "off the underside of the crossbar"
WHAT: TWO separate vision passes on two sources both said crossbar. The shootout record says he
 shot WIDE LEFT; Gabriel is the one who went over.
WHY: Used footage to settle an OUTCOME. Vision is unreliable on outcomes and identities.
RULE: Footage wins on what is IN THE FRAME. Text wins on WHAT HAPPENED. Never let two agreeing
 vision passes stand in for a record check — they can agree and both be wrong.
STAGE: 5 (verify)

### E09 — Imported the reference's story onto his picks
WHAT: Recommended splitting Transfers into five single-story videos, arguing twelve seconds cannot
 carry a transfer saga. Wrong: the REFERENCE needed 69s because it is one story with a reversal.
 HIS five are one-line facts — a volcano, a fax, an interview already done.
WHY: Reasoned about the reference's content instead of about his picks.
RULE: When judging whether a format fits, test it against THE PICKS IN HAND, never against what the
 reference happened to contain. A reference is a format source, not a content source — and that
 cuts both ways.
STAGE: 7 (assemble)

### E10 — Label drift made the notes unscannable
WHAT: READ OFF THE KIT vs READ OFF THE SHIRTS. BOARDS vs FASCIA BANNERS vs FAN BANNERS. AUTHENTIC
 vs REAL BROADCAST. Same field, different name, across 14 files.
WHY: No fixed vocabulary; each file written fresh.
RULE: One vocabulary, fixed, listed in Stage 4. Substance being right is not enough if the reader
 cannot scan for it.
STAGE: 4 (watch)

### E11 — Reintroduced the exact defect I had just fixed
WHAT: After normalising the vocabulary, wrote three NEW files with labels on bare lines and no
 colons, so the PDF renderer treated them as body text while every older file rendered them as
 labels.
WHY: Wrote in a style the renderer did not expect, and validated by PARSING rather than RENDERING.
RULE: A parse check is not a render check. Render a page to PNG and READ IT BACK before sending.
STAGE: 9 (deliver)

### E12 — Splice ran past the array boundary
WHAT: Editing the last pack in PACKS, an unbounded find() jumped into the DECISIONS array and ate
 the closing bracket, producing an 18-pack array with a decision inside it.
WHY: Searched for a delimiter shared by two adjacent arrays with no upper bound.
RULE: Bound every in-place splice to the array being edited: compute the array's start AND end
 first, and pass both to every find(). Re-compute the end after each edit.
STAGE: 9 (deliver)

### E13 — Over-escalated decisions
WHAT: Put eight calls to him, several of which I had a clear recommendation for and could have made.
 Then created two MORE from his answers.
WHY: Treated "flag it" as always safer than "decide it". It is not — it moves work to him.
RULE: DECIDE BY DEFAULT. Escalate only a genuine fork: one where the options are close AND the
 choice is taste rather than evidence. When deciding, state the reasoning and name the cost, so it
 can be overruled in one tap. See Stage 8.
STAGE: 8 (decide)

### E14 — Read "appointment" as a calendar event
WHAT: He said to make an appointment whenever something needs his input. I went to Google Calendar.
 He meant the notes app.
WHY: Took the most literal reading of an ambiguous word without checking which fit his setup.
RULE: When an instruction could mean a tool he already uses or one he does not, assume the one
 already in the workflow.
STAGE: 8 (decide)

### E15 — Under-quoted credits by roughly six times
WHAT: Quoted ~18 credits for a batch of scoped passes. Actual was ~110, because a scoped pass bills
 on the WHOLE source video, not the window. A 16-minute compilation is ~15 credits per moment.
WHY: Assumed the window length drove the cost.
RULE: Before quoting a cost, check the SOURCE duration, not the window. Five moments inside one
 16-minute compilation is ~75 credits, not ~15. Correct an estimate out loud the moment it moves.
STAGE: 4 (watch)

### E16 — A label that made finished work look broken
WHAT: Three packs with five complete, sourced picks each sat under a red "Ref failed" pill. He
 reasonably read it as "these are unfinished".
WHY: The label described what happened to the REFERENCE, not the state of the PACK.
RULE: A status label describes the PACK's readiness, never the audit's verdict. "Shoot knowing"
 is a different state from "blocked" and must look different.
STAGE: 9 (deliver)

────────────────────────────────────────────────────────────────────────
## THE FIVE PATTERNS UNDERNEATH THESE SIXTEEN
1. Errors cluster where the picture needed BACKGROUND KNOWLEDGE under it (E04, E06, E08).
2. Repeat passes agree on WHAT IS IN FRAME and disagree on COUNTS (E03, E07).
3. Writing from a previous note rather than a fresh watch propagates errors (E05, E09).
4. Validation that is not the same KIND as the output misses defects (E11, E12).
5. Flagging feels safe and is not — it moves the work to him (E13, E16).

### E17 — Fixed a defect in three files and called it fixed
WHAT: After finding that bare labels without a colon render as body text rather than labels, I fixed
 the three files I had just written and moved on. The QA gate, run for the first time, found the
 same defect in ELEVEN MORE files — 39 instances in total.
WHY: Fixed where I had been looking rather than where the defect could be. No sweep of the class.
RULE: When a defect is found in one file, sweep the whole class before declaring it fixed. If the
 defect is mechanically detectable, the sweep IS a qa.py check — write it there, not by hand.
STAGE: 9.5 (QA gate)

### E18 — A stale audit contradicted a filled pack three pages later
WHAT: The reference audit in the send-off PDF still read "mispronounce IS NOT FINISHED... 2/5... it
 cannot go into production" after the three slots had been filled. The QA gate caught it.
WHY: Corrections were applied to the pack surfaces (app, sheet, line-up) but not to the refaudit
 file, which the PDF also includes. "Fix it in every surface" did not include the audit.
RULE: The surfaces are deep/, refaudit/, data.py, notes-app.html AND the built PDF. A correction
 lands in all five or it has not landed. Prefer re-dating an audit entry [RESOLVED <date>] over
 deleting it — the history is worth keeping, the contradiction is not.
STAGE: 9.5 (QA gate)

### E19 — The first QA gate was mis-calibrated and cried wolf
WHAT: The gate's first run produced 73 warnings, of which 25 were a descriptive "12 yards" in a
 working note being treated the same as a number spoken on camera.
WHY: Encoded the rule ("any number that will be spoken gets a source") without encoding WHERE it
 applies. Working notes hold soft estimates by design; the production sheet is what he reads out.
RULE: A check must know which surface it governs. Same rule, different severity by file: soft in
 deep/ is INFO, unsourced in data.py is WARN. A gate that cries wolf gets ignored, which is worse
 than no gate.
STAGE: 9.5 (QA gate)

### E20 — I over-corrected, and stated a disputed outcome as settled fact
WHAT: I wrote that Eze's CL-final penalty "did NOT hit the crossbar — the record says WIDE LEFT",
 presenting it as settled. Building the clip manifest, a THIRD vision pass on Arsenal's own footage
 said OVER THE BAR, agreeing with the two I had overruled. Checking again: Wikipedia does say "shot
 wide left", but TNT Sports' live commentary says only that he "missed his side's second effort"
 and does not settle it. Both readings agree he went LEFT and missed; they disagree on whether it
 cleared the bar or passed the post.
WHY: E08 taught "text wins on what happened", and I applied it as if one text source ends the
 question. It does not. A single source that contradicts three passes is a CONFLICT to record, not
 a verdict to announce.
RULE: Law 2 settles WHICH SOURCE OUTRANKS WHICH. It does not turn one source into certainty. When
 text and repeated footage disagree, say DISPUTED, give both readings with their sources, and tell
 him the safe wording — here, "he missed", which nobody contests. Escalating from "footage is
 unreliable" to "therefore the first text I found is true" is the same error wearing the other coat.
KNOCK-ON: if it IS over the bar, Eze at #1 and Zaza at #5 both end over the bar — the exact
 duplicate-mechanism problem that removing Tah was meant to fix. A disputed fact can carry a
 variety consequence, so check downstream before assuming the dispute is cosmetic.
STAGE: 5 (verify), 7 (assemble)

### E21 — Thirty-five clips had no single place listing where they live
WHAT: Source ids and windows were spread across fourteen deep files, some in a SOURCE line, some
 only in a per-clip header, some not recorded at all. Eze's had no window anywhere.
WHY: Descriptions were written to be READ, not to be CUT FROM. Nobody had asked for a shot list, so
 nobody built one, and the gaps were invisible until it was assembled.
RULE: A pack is not finished until every Type A pick has a source link AND an in/out window in one
 manifest. Build it as the descriptions are written, not afterwards — assembling it is what exposes
 the missing ones. `clips.py` holds it; the manifest ships as Part 5.5 of the send-off and as a CSV.
STAGE: 4 (watch), 9 (deliver)

### E22 — Nine packs had picks but no verification layer, and nobody noticed
WHAT: The Type B packs shipped with a one-line explanation per pick and nothing behind it. Assembling
 their sheets showed 20 of 45 picks rest on his own COMMENTS rather than a source — against the
 system's own Stage 2.5 rule, "verify every Type B claim against sources, never comments."
WHY: Type B correctly skips the CLIP pipeline, and I let "skips describing" slide into "skips
 verifying". The two are not the same: Type A's evidence is footage, Type B's evidence is text, and
 Type B has no stage that forces the text to exist.
RULE: Type B's equivalent of a description is a SOURCED FACT. Every Type B pick carries its source
 in the sheet, or is marked FROM COMMENTS so the gap is visible. Verify first anything carrying a
 quote, a fee or a precise number — those are what the comments correct.
QA: add a check — every Type B pick must have a source field or an explicit unverified marker.
STAGE: 2.5 (route), 5 (verify)

### E23 — "Retired at 28" would have been wrong by two years
WHAT: The Primes pack said Van Basten was "done at 28". His LAST MATCH was at 28 (1993 CL final,
 substituted on 86 minutes) but he formally retired on 17 August 1995, aged 30, after two years of
 failed comebacks.
WHY: A rounded claim that happens to be defensible in one reading and wrong in another. "Done at 28"
 survives; "retired at 28" does not, and the two are one word apart in a script.
RULE: When a career fact has two candidate dates — last appearance vs formal retirement, signed vs
 debuted, banned vs suspended — record BOTH and say which you mean. The gap is usually the better
 story: two years of trying to come back beats a single wrong number.
STAGE: 5 (verify)

### E24 — The production sheet still had Tah at #2 two days after Budimir replaced him
WHAT: `handover/data.py`'s Penalty Part 2 sheet — the page Joel shoots from — still listed TAH at #2 with
 status "FOUR OF FIVE READY" and verdict "one slot is still a duplicate", while the app, `final_packs.json`,
 `clips.py` and the deep files all had Budimir. The same sheet and `deep/penalties.md` also still stated
 Eze "wide of the LEFT post" as settled, five days after E20 had downgraded it to DISPUTED, and the
 variety line still compared Eze to Tah. Found on 22 Sep while writing the handoff, not by QA.
WHY: Three surfaces carry each pack (app · final_packs.json · data.py) plus the deep files, and the
 `surface-mismatch` check only compares the first two by pack ID. A pick swap that lands in the app and
 the JSON but not in data.py is invisible to it. E17 and E18 were the same pattern and the fix was
 local each time.
RULE: A pick change is not done until it is grep-confirmed absent from EVERY surface: `grep -n <old
 name>` across handover/, deep/, notes-app.html, clips.py, typeb.py. Add to QA: compare pick NAMES (not
 just pack ids) between final_packs.json and data.py, and fail on a mismatch.
FIX: data.py #2 → Budimir; Eze → DISPUTED with the safe wording; warn line → Gabriel duplicates Zaza;
 penalties.md Tah section relabelled SUB; app + JSON Eze row → DISPUTED; PDF rebuilt; app republished.
 Same sweep, same day, found by the adversarial pass on the handoff rather than by grep: the Oscar
 note still carried "Strong case to move Embolo to #4" (declined) and the Transfers note still carried
 "run it as one transfer per video" (withdrawn) in the app and final_packs.json; badge-redo's sheet still
 said "one slot has to be replaced"; oscar-2's sheet still said "stands unless you say otherwise". All
 resolved; final_packs.json is now regenerated from the app by handover/hx/regen_packs.mjs; the PDF's
 Part Six now prints the live QA gate so warnings are acknowledged inside the send-off.
STAGE: 7 (assemble), 9.5 (QA)
```

#### `qa.py`
<!-- FILE: qa.py · 14258 bytes · 303 lines · sha256 b7e91173486c7f2965cd0e18bee6761f657466a68186b3fd2662bbe21a189642 -->
*Written 21 Sep on Joel's 'have a built in qa within this system'; calibrated after the first run cried wolf at 73 warnings (E19); typeb-unsourced check added for E22; sheet-pick-mismatch check added 22 Sep for E24 and proven to fire on the re-injected Tah defect. Run: python3 qa.py · --pack <id> · --json.*
```python
#!/usr/bin/env python3
"""
LXTHALFC QA GATE  —  Stage 9.5
Runs BEFORE delivery. Exits non-zero on any FAIL.
Every check descends from a real error in errors.md and names it.

  python3 qa.py              # check everything
  python3 qa.py --pack <id>  # one pack
  python3 qa.py --json       # machine-readable
"""
import json, re, os, sys, glob, statistics, subprocess, io

LX = "/root/lx"
R = {"fail": [], "warn": [], "info": [], "pass": 0}

def rec(sev, check, msg, err=""):
    if sev == "pass": R["pass"] += 1; return
    R[sev].append({"check": check, "msg": msg, "err": err})

def load():
    p = json.load(open(f"{LX}/handover/final_packs.json", encoding="utf-8"))
    deep = {os.path.basename(f): io.open(f, encoding="utf-8").read()
            for f in glob.glob(f"{LX}/deep/*.md")}
    return p, deep

# Packs that need a described clip per pick. Everything else is Type B.
TYPE_A = {"signature-redo","gk-assists","pace-abuser-2","oscar-2",
          "badge-redo","penalty-2","accidental-saves"}

PLACEHOLDER = re.compile(r"in rework|slot open|TBD|NEEDS VERIF|coming soon|\bTK\b", re.I)
BANNED_LABELS = {
    "READ OFF THE SHIRTS": "READ OFF THE KIT",
    "FASCIA BANNERS": "BOARDS",
    "FAN BANNERS": "CROWD",
    "CARD GRAPHICS": "BROADCAST GRAPHICS",
}
# A count stated as fact, where the rule is "say the foot, never the number"
COUNT_AS_FACT = re.compile(
    r"\b(?:ONE|TWO|THREE|FOUR|FIVE|SIX|SEVEN|EIGHT|NINE|TEN|ELEVEN|TWELVE|\d+)\s+"
    r"(?:TOUCHES|STEPS|STRIDES)\b", re.I)
# A measurement that should carry a source
MEASURE = re.compile(r"\b\d+(?:\.\d+)?\s?(?:mm|millimetres?|yards?|metres?|km/h|mph)\b", re.I)
SOURCE_NEAR = re.compile(r"written record|own site|reported|per |according to|sky sport|wikipedia|"
                         r"do not quote|don't quote|no speed|no scorebug|NOT in the footage|attribute|"
                         r"approximate|roughly|about |~|estimate|not stable|it is 11mm|"
                         r"never quote|soft|cannot measure|footage alone", re.I)
WINDOW = 520   # a caveat three lines away still governs the number

def check_packs(packs, deep):
    ids = [p["id"] for p in packs]

    # --- structure ---
    for p in packs:
        n = len(p["picks"])
        if n != 5:
            rec("fail", "pack-size", f"{p['id']}: {n} picks, expected 5")
        else: rec("pass","","")
        if not p.get("subs") or p["subs"].strip() in ("", "—", "-"):
            rec("warn", "subs", f"{p['id']}: no subs listed — every video gets three")
        else: rec("pass","","")
        for rank, name, why in p["picks"]:
            if not why or not why.strip():
                rec("fail", "pick-explanation", f"{p['id']} #{rank}: no explanation line")
            else: rec("pass","","")

    # --- placeholders in a locked pack (E: gate 8 / reference validity #8) ---
    for p in packs:
        if p.get("state") != "locked": continue
        for rank, name, why in p["picks"]:
            if PLACEHOLDER.search(name) or PLACEHOLDER.search(why or ""):
                rec("fail", "placeholder-in-locked",
                    f"{p['id']} #{rank} is a placeholder but the pack is LOCKED: {name[:50]}",
                    "ref-validity #8")
            else: rec("pass","","")

    # --- cross-pack duplicate picks ---
    seen = {}
    for p in packs:
        for rank, name, _ in p["picks"]:
            key = re.sub(r"[^a-z0-9 ]", "", name.lower())
            key = " ".join(w for w in key.split() if len(w) > 3)[:40]
            if not key: continue
            if key in seen and seen[key][0] != p["id"]:
                rec("warn", "cross-pack-duplicate",
                    f"'{name[:38]}' appears in both {seen[key][0]} and {p['id']}")
            else: seen[key] = (p["id"], rank); rec("pass","","")

    # --- Type A coverage: every pick described somewhere in deep/ ---
    alldeep = " ".join(deep.values())
    for p in packs:
        if p["id"] not in TYPE_A: continue
        for rank, name, _ in p["picks"]:
            toks = [w for w in re.sub(r"[^A-Za-zÀ-ÿ ]", " ", name).split()
                    if len(w) > 3 and w[0].isupper()][:3]
            if toks and not any(t in alldeep for t in toks):
                rec("fail", "undescribed-pick",
                    f"{p['id']} #{rank} '{name[:40]}' has no deep description", "E05")
            else: rec("pass","","")
    return ids

def check_deep(deep):
    # --- required labels ---
    for f, t in deep.items():
        if not re.search(r"^\s*AUTHENTIC[: ]", t, re.M):
            rec("fail", "missing-AUTHENTIC", f"deep/{f}: no AUTHENTIC label", "E10")
        else: rec("pass","","")
        if not re.search(r"^\s*CANNOT DETERMINE", t, re.M):
            rec("fail", "missing-CANNOT-DETERMINE",
                f"deep/{f}: no CANNOT DETERMINE label — a gap beats a confident error", "E10")
        else: rec("pass","","")

    # --- vocabulary conformance ---
    for f, t in deep.items():
        for bad, good in BANNED_LABELS.items():
            if bad in t:
                rec("fail", "vocabulary-drift",
                    f"deep/{f}: uses '{bad}' — the fixed vocabulary says '{good}'", "E10")
            else: rec("pass","","")
        # a bare label with no colon renders as body text, not a label
        for m in re.finditer(r"^([A-Z][A-Z0-9' /&-]{3,44})$", t, re.M):
            lab = m.group(1).strip()
            if lab in ("CANNOT DETERMINE",) or lab.startswith("#"): continue
            nxt = t[m.end():m.end()+120].lstrip("\n")
            if nxt.startswith(" "):
                rec("warn", "bare-label",
                    f"deep/{f}: '{lab}' has no colon — renders as body text, not a label", "E11")

    # --- counts stated as fact ---
    for f, t in deep.items():
        for m in COUNT_AS_FACT.finditer(t):
            line = t[max(0,t.rfind("\n",0,m.start())):t.find("\n",m.end())]
            # the caveat can sit on the line OR as a banner at the top of the file
            head = t[max(0,m.start()-WINDOW):m.end()+WINDOW]
            CAV = r"do not quote|not stable|never quote|CORRECTED|disagree|approximate|about |soft"
            if re.search(CAV, line, re.I) or re.search(CAV, head, re.I):
                continue
            rec("warn", "count-as-fact",
                f"deep/{f}: '{m.group(0)}' stated without the instability caveat", "E07")

    # --- measurements without a source ---
    # CALIBRATION: a descriptive estimate in a working note ("from 12 yards") is a SOFT observation,
    # not a claim he speaks. E06 is about numbers that go ON SCREEN or are SPOKEN. So deep files are
    # INFO; the production sheet, which is what he reads out, is the one that must carry a source.
    for f, t in deep.items():
        for m in MEASURE.finditer(t):
            ctx = t[max(0, m.start()-WINDOW): m.end()+WINDOW]
            if not SOURCE_NEAR.search(ctx):
                rec("info", "soft-measurement",
                    f"deep/{f}: '{m.group(0)}' is a footage estimate — keep it out of the script", "E06")

    # --- depth evenness, per pack prefix ---
    groups = {}
    for f, t in deep.items():
        pref = re.split(r"[-.]", f)[0]
        groups.setdefault(pref, []).append((f, len(t.split())))
    for pref, files in groups.items():
        if len(files) < 3: continue
        med = statistics.median(w for _, w in files)
        for f, w in files:
            if w < med * 0.5:
                rec("warn", "thin-description",
                    f"deep/{f}: {w} words vs {int(med)} median for '{pref}' — under half", "depth")

def check_sheet():
    """The production sheet is what he reads out. Numbers here must carry a source."""
    p = f"{LX}/handover/data.py"
    if not os.path.exists(p): return
    s = io.open(p, encoding="utf-8").read()
    for m in MEASURE.finditer(s):
        ctx = s[max(0, m.start()-WINDOW): m.end()+WINDOW]
        if not SOURCE_NEAR.search(ctx):
            rec("warn", "unsourced-spoken-number",
                f"data.py: '{m.group(0)}' will be spoken but carries no source or caveat", "E06")
        else: rec("pass","","")

def check_typeb():
    """Type B has no footage, so its evidence is TEXT. Every pick carries a source or an
    explicit unverified marker — otherwise the gap is invisible. (E22)"""
    try:
        import importlib.util as _u
        sp=_u.spec_from_file_location("typeb", f"{LX}/typeb.py"); m=_u.module_from_spec(sp)
        sp.loader.exec_module(m)
    except Exception as e:
        rec("warn","typeb-unreadable",f"typeb.py: {e}"); return
    unmarked=0
    for title,_fam,_st,_head,picks in m.SHEETS:
        for rank,name,v,fact,src,note in picks:
            if v not in ("V","C") and not src:
                rec("fail","typeb-unsourced",
                    f"{title} #{rank} '{name[:34]}' has no source and no unverified marker","E22")
            elif v=="C": unmarked+=1; rec("pass","","")
            else: rec("pass","","")
    if unmarked:
        rec("info","typeb-from-comments",
            f"{unmarked} Type B picks rest on comments rather than a source — verify any carrying "
            f"a quote, a fee or a precise number before camera","E22")

def check_consistency(packs):
    """Cross-surface: the app, final_packs.json and the build script must agree."""
    try:
        h = io.open(f"{LX}/notes-app.html", encoding="utf-8").read()
        m = re.search(r"const PACKS = \[([\s\S]*?)\n\];", h)
        app_ids = re.findall(r'\{id:"([a-z0-9-]+)"', m.group(1))
    except Exception as e:
        rec("fail", "app-unreadable", f"notes-app.html: {e}"); return
    fp_ids = [p["id"] for p in packs]
    if set(app_ids) != set(fp_ids):
        only_app = set(app_ids) - set(fp_ids); only_fp = set(fp_ids) - set(app_ids)
        rec("fail", "surface-mismatch",
            f"app vs final_packs.json disagree — only in app: {sorted(only_app) or '·'}; "
            f"only in json: {sorted(only_fp) or '·'}", "E12")
    else: rec("pass","","")

    # E24 — pick NAMES must agree between final_packs.json and the data.py production sheet.
    # A swap that lands in the app and the JSON but not the sheet is what Joel would shoot from.
    try:
        import importlib.util as _u
        sp=_u.spec_from_file_location("data", f"{LX}/handover/data.py"); dm=_u.module_from_spec(sp)
        sp.loader.exec_module(dm)
        def _norm(t): return re.sub(r"[^a-z0-9]", "", t.lower())
        sheets = {_norm(x["title"]): x for x in getattr(dm, "READY", []) if isinstance(x, dict)}
        for p in packs:
            sh = sheets.get(_norm(p["title"]))
            if not sh: continue   # Type B sheets are tuples in BLOCKED and hold no per-pick rows
            sheet_names = " ".join(str(r[1]) for r in sh.get("picks", [])).lower()
            for pk in p["picks"]:
                toks = [t for t in re.sub(r"[^\w']", " ", pk[1]).split()
                        if len(t) > 2 and t[0].isupper()][:2]   # the name is the first two words
                if toks and not any(t.lower() in sheet_names for t in toks):
                    rec("fail", "sheet-pick-mismatch",
                        f"{p['id']} #{pk[0]} '{pk[1][:40]}' is in final_packs.json but data.py's sheet "
                        f"has no pick naming any of {toks} — the production sheet is stale", "E24")
                else: rec("pass","","")
    except Exception as e:
        rec("warn", "sheet-unreadable", f"data.py: {e}")

    try:
        b = io.open(f"{LX}/handover/build_master.py", encoding="utf-8").read()
        stat_ids = set(re.findall(r'"([a-z0-9-]+)":\("', b))
        missing = [i for i in fp_ids if i not in stat_ids]
        if missing:
            rec("fail", "build-mapping-gap",
                f"build_master.py STAT has no entry for: {missing} — the build will KeyError", "E12")
        else: rec("pass","","")
    except Exception as e:
        rec("warn", "build-unreadable", f"build_master.py: {e}")

def check_deliverables():
    pdf = f"{LX}/LxthalFC-September-SENDOFF.pdf"
    if not os.path.exists(pdf):
        rec("info", "pdf", "no send-off PDF built yet"); return
    try:
        t = subprocess.run(["pdftotext", pdf, "-"], capture_output=True, text=True).stdout
    except Exception as e:
        rec("warn", "pdf-unreadable", str(e)); return
    tofu = [c for c in set(t) if ord(c) > 0x1F000 or 0x4E00 <= ord(c) <= 0x9FFF
            or 0x0600 <= ord(c) <= 0x06FF]
    if tofu:
        rec("fail", "pdf-tofu", f"characters DejaVu cannot render: {tofu}", "deliver")
    else: rec("pass","","")
    # A placeholder in PROSE is history ("at audit its picks read..."). A placeholder in a live
    # PICK ROW is a defect. Check the rows, not the narrative.
    packs = json.load(open(f"{LX}/handover/final_packs.json", encoding="utf-8"))
    for p in packs:
        for rank, name, why in p["picks"]:
            if PLACEHOLDER.search(name):
                rec("fail", "placeholder-shipped",
                    f"{p['id']} #{rank} ships as a placeholder in the PDF line-up: {name[:40]}")
            else: rec("pass","","")

def report(as_json=False):
    if as_json:
        print(json.dumps(R, indent=1)); return 1 if R["fail"] else 0
    n_f, n_w = len(R["fail"]), len(R["warn"])
    print("=" * 66)
    print(f"  QA GATE — {R['pass']} passed · {n_w} warnings · {n_f} FAILURES")
    print("=" * 66)
    for sev, label in (("fail", "FAIL"), ("warn", "WARN"), ("info", "INFO")):
        for r in R[sev]:
            tag = f" [{r['err']}]" if r["err"] else ""
            print(f"  {label}  {r['check']}{tag}\n        {r['msg']}")
    if not n_f and not n_w:
        print("  Nothing to report. Every check passed.")
    print("=" * 66)
    if n_f:
        print("  BLOCKED. Fix the failures before delivering.")
    elif n_w:
        print("  Warnings do not block, but each must be ACKNOWLEDGED in the report to Joel.")
    return 1 if n_f else 0

if __name__ == "__main__":
    as_json = "--json" in sys.argv
    packs, deep = load()
    if "--pack" in sys.argv:
        want = sys.argv[sys.argv.index("--pack") + 1]
        packs = [p for p in packs if p["id"] == want]
    check_packs(packs, deep)
    check_deep(deep)
    check_sheet()
    check_typeb()
    check_consistency(packs)
    check_deliverables()
    sys.exit(report(as_json))
```

#### `handover/SKILL-PROPOSED.md`
<!-- FILE: handover/SKILL-PROPOSED.md · 29362 bytes · 510 lines · sha256 dd2f6139daff864f0c469a165365c98863662f64f17f5837cf7b619efccd2d4c -->
*The skill as it should be saved via propose_skills (kind improvement, target lxthalfc-picker). Two earlier cards this session were not saved. Includes the Three Laws, Stage 9.5, E20/E23 lessons, and (22 Sep) the grep-confirmed propagation and status-label non-negotiables. NOT the version on disk — see 6.9 for that.*
````markdown
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
````

### 6.2 The manifest and the Type B sheets

#### `clips.py`
<!-- FILE: clips.py · 7052 bytes · 100 lines · sha256 63bb123bb013140ba490095c3beddf290f4ebf182c5af3b6721fcbbbf80e98b2 -->
*Built 21 Sep on 'could you give the timestamps as to where these clips were present with video refrence links' (E21). 35 clips, 28 unique sources; rows() feeds Part 5.5 of the PDF and the CSV. Eze's row carries the DISPUTED note.*
```python
# -*- coding: utf-8 -*-
# CLIP MANIFEST — every Type A pick: source, link, window, and the angle to cut on.
# WINDOW is where the moment sits inside the source video.
# CUT is the specific replay/angle recommended, where one was identified.
Y = "https://youtu.be/"

CLIPS = [
 # pack, rank, pick, video_id, source label, window, cut-on, note
 ("Top 10 Signature Moves (2026 Redo)", [
  ("5","Robben's cut-in — v Juventus","qDgAANEXQqg","compilation","02:02–02:24","",""),
  ("4","Ronaldinho's elástico — nutmeg on Dunga","LXqPEpeokCg","1999 Gre-Nal final","02:20–02:35","",""),
  ("3","Iniesta's croqueta — v Man City","Zs3bmAJ4nq0","compilation","01:38–01:47","",""),
  ("2","Messi's body feint — v Weligton","VzUWrhh7UQE","slow-mo breakdown","03:22–03:56","",""),
  ("1","The Cruyff turn — Sweden, 1974","PBgLInYqhmo","archive + interview","00:05–00:11",
   "00:08–00:10 the turn itself · 00:17–00:26 slow-motion replay",""),
 ]),
 ("Goalkeepers With Unbelievable Assists", [
  ("5","Ederson → Agüero, Man City v Huddersfield","cVtF64Un-0o","Premier League OFFICIAL","00:12–00:38",
   "00:29–00:38 static high tactical wide","All five from this ONE compilation"),
  ("4","Alisson → Salah, Liverpool v Man United","cVtF64Un-0o","Premier League OFFICIAL","00:00–00:11",
   "one unbroken live shot, no replays","[!] Cuts at 00:11 — Alisson's run is NOT in it"),
  ("3","Schmeichel → Solskjær, Man Utd v Sunderland","cVtF64Un-0o","Premier League OFFICIAL","06:56–07:13",
   "07:00–07:10 one continuous pan, throw to goal",""),
  ("2","Čech → Drogba, Wolves v Chelsea","cVtF64Un-0o","Premier League OFFICIAL","01:24–01:53",
   "01:42–01:44 the punt (settles the foot) · 01:44–01:53 pitch-level slow-mo",""),
  ("1","Van der Sar → Rooney, Man Utd v Aston Villa","cVtF64Un-0o","Premier League OFFICIAL","04:14–04:45",
   "04:32–04:38 Van der Sar with Ferdinand and Evra — the money shot",""),
 ]),
 ("Top 10 Pace Abuser Moments Part 2", [
  ("10","Son Heung-min — the Burnley solo goal","C-CefuZ6h1k","Tottenham OFFICIAL, Puskás package","00:00–03:19",
   "02:40–03:19 ULTRA SLOW-MOTION HEAD-ON — the only angle that carries the one-footed point",
   "Ten angles. Mask the subscribe panel at 00:21–00:35 and the end card at 03:20"),
  ("9","Terens Puhiri — Borneo FC v Mitra Kukar","kjdKZOcXlbk","Guardian Football, 7.8M","00:00–00:52",
   "whole clip is the run","52s, dedicated"),
  ("8","Van de Ven — Spurs v Copenhagen","h_stLgq5Rps","Tottenham OFFICIAL","01:04–01:23",
   "one unbroken wide pan, no replays",""),
  ("7","Adeyemi — Dortmund v Chelsea","nPZGlV1rBM4","DAZN","00:00–01:31",
   "whole clip is the run","91s, dedicated. Clock 62:20 → 62:45"),
  ("6","Bale v Maicon — Spurs 3-1 Inter","JOirPSqL28w","TNT Sports","00:00–01:26",
   "00:32–00:34 low tight sideline — Maicon grabs his shoulder · 01:14–01:20 low reverse slow-mo",
   "86s, FOUR separate runs. [!] Bale does not score in this footage"),
 ]),
 ("Top 5 Players Who Deserve The Oscar Award Part 2", [
  ("5","Neymar rolling — Mexico, 2018","9qjGKKitwXo","FIFA","01:46–02:19",
   "","[!] Use ONLY to 02:19. He rolls ONCE — every longer cut is padded"),
  ("4","Micah Richards — Aston Villa v Stoke","RscP6Vaghd4","CBS Sports Golazo","00:59–01:20",
   "the clip AND the studio reaction in one",""),
  ("3","Breel Embolo — Switzerland v Argentina","1O-qw6iaLOk","real footage, three slow-mo angles","00:00–02:10",
   "00:38 reverse sideline — airborne BEFORE any contact",""),
  ("2","Suárez — the Chiellini bite, 2014","1tVdCQaH0vs","ESPN broadcast, unedited","00:00–01:10",
   "00:11–00:15 cupping his mouth · 01:07–01:10 pulls his collar over his face",""),
  ("1","Rivaldo, 2002 v Turkey","OiW0IPrv1Ro","2.55M","00:13–00:15",
   "","25s clip, no scorebug anywhere"),
 ]),
 ("Top 5 Die for the Badge (2026 Redo)", [
  ("5","Valverde on Morata — Supercopa final","3JiwVYCnHqU","Italian network NOVE","00:02–00:04",
   "","Match clock 114:29. Simeone pats his head as he walks off"),
  ("4","Van de Ven — Europa League final, Bilbao","vWC-USe1ncI","Tottenham OFFICIAL","00:39–01:10",
   "00:39 the live clearance, replays to 01:10","Match clock 67:38"),
  ("3","Süle v Mbappé — DORTMUND, not Bayern","vjTC2gCMtqM","DAZN","00:13–00:15",
   "","Match clock 16:34–16:36"),
  ("2","John Stones — off the line in front of Salah","MriNd_wn1Os","Man City OFFICIAL","00:55–01:40",
   "01:26–01:32 LOW REVERSE FROM BEHIND THE NET — the hook across Salah",
   "[!] The 11mm figure is NOT in this footage. The graphic reads only NO GOAL"),
  ("1","FERLAND Mendy v Man City — not Édouard","WgzZRA260X0","TNT / BT Sport","00:15–00:18",
   "","Match clock 86:11–86:13"),
 ]),
 ("Worst Penalty Miss With Every Technique Part 2", [
  ("5","Zaza, Euro 2016 — STUTTER","5_9OwlwAMMk","Stade de Bordeaux","00:14–00:23",
   "00:21–00:23 close-up — number 7 legible on chest and shorts",""),
  ("4","Pires & Henry, Highbury — PASS","N4bQVTczcLQ","34s, carries BOTH halves","00:00–00:34",
   "00:12–00:18 HIGH REVERSE behind the North Bank — the studs clipping the ball",
   "00:19–00:21 tunnel interview · 00:22–00:34 the Sparta Prague callback. END ON THAT"),
  ("3","Agüero v Chelsea — PANENKA","he7mZJDIEOQ","Sky Sport DE — UPGRADED SOURCE","01:23–01:43",
   "","Full German commentary, official PL scorebug, four angles"),
  ("2","Budimir v Valencia, 97th minute","4EvIcyRuAXg","Arena Sport 1","00:00–00:38",
   "00:30–00:35 LOW PITCHSIDE FROM THE RIGHT — the standing leg collapsing and the toe-scuff",
   "Mask the betting graphics bottom left throughout"),
  ("1","Eze v PSG — the CL final shootout","ygcv9fQheII","ARSENAL'S OWN OFFICIAL CHANNEL","01:22–01:27",
   "01:23 run-up · 01:25 strike · 01:26–01:27 EZE 10 legible on his back",
   "[!!] OUTCOME DISPUTED — see the note under this table. Shootout starts 01:12"),
 ]),
 ("When Goalkeepers Make Accidental Saves", [
  ("5","Full Reverse Save","ZbunM6UKwts","the reference itself, its #6 entry","—",
   "","[!] No standalone clip exists. Lift it from the reference"),
  ("4","No-Look Save","ZbunM6UKwts","the reference itself, its #5 entry","00:07–00:13","",""),
  ("3","IDK Save","ZbunM6UKwts","the reference itself, its #4 entry","00:14–00:22","",""),
  ("2","Neuer v Bas Dost — the heel he can't see","PaaZxPh0A-o","Legendary Goal Line Saves","02:00–02:08",
   "02:04–02:07 GROUND-LEVEL REVERSE FROM INSIDE THE NET — the ball meeting his trailing heel",
   "Mask the Score 90 overlay bottom left"),
  ("1","Choupo-Moting stops his OWN team scoring","PaaZxPh0A-o","Legendary Goal Line Saves","05:05–05:19",
   "","On-screen caption in the source reads “200 IQ”"),
 ]),
]

def rows():
    for pack, cl in CLIPS:
        for rank, pick, vid, label, win, cut, note in cl:
            yield dict(pack=pack, rank=rank, pick=pick, video_id=vid, source=label,
                       url=Y+vid, window=win, cut=cut, note=note)
```

#### `LxthalFC-CLIP-MANIFEST.csv`
<!-- FILE: LxthalFC-CLIP-MANIFEST.csv · 7825 bytes · 36 lines · sha256 42c0686976d13b0a879a92cd68826b53fd55a9dfadf23caf05a11961eeb31b51 -->
*Generated from clips.py; 36 lines incl. header. (On disk this file has CRLF line endings; it is embedded LF-normalised and the hash is of the LF form. Both read identically through the csv module.)*
```csv
﻿Pack,Rank,Pick,Source,Video ID,Link,In–Out,Cut on this angle,Note
Top 10 Signature Moves (2026 Redo),5,Robben's cut-in — v Juventus,compilation,qDgAANEXQqg,https://youtu.be/qDgAANEXQqg,02:02–02:24,,
Top 10 Signature Moves (2026 Redo),4,Ronaldinho's elástico — nutmeg on Dunga,1999 Gre-Nal final,LXqPEpeokCg,https://youtu.be/LXqPEpeokCg,02:20–02:35,,
Top 10 Signature Moves (2026 Redo),3,Iniesta's croqueta — v Man City,compilation,Zs3bmAJ4nq0,https://youtu.be/Zs3bmAJ4nq0,01:38–01:47,,
Top 10 Signature Moves (2026 Redo),2,Messi's body feint — v Weligton,slow-mo breakdown,VzUWrhh7UQE,https://youtu.be/VzUWrhh7UQE,03:22–03:56,,
Top 10 Signature Moves (2026 Redo),1,"The Cruyff turn — Sweden, 1974",archive + interview,PBgLInYqhmo,https://youtu.be/PBgLInYqhmo,00:05–00:11,00:08–00:10 the turn itself · 00:17–00:26 slow-motion replay,
Goalkeepers With Unbelievable Assists,5,"Ederson → Agüero, Man City v Huddersfield",Premier League OFFICIAL,cVtF64Un-0o,https://youtu.be/cVtF64Un-0o,00:12–00:38,00:29–00:38 static high tactical wide,All five from this ONE compilation
Goalkeepers With Unbelievable Assists,4,"Alisson → Salah, Liverpool v Man United",Premier League OFFICIAL,cVtF64Un-0o,https://youtu.be/cVtF64Un-0o,00:00–00:11,"one unbroken live shot, no replays",[!] Cuts at 00:11 — Alisson's run is NOT in it
Goalkeepers With Unbelievable Assists,3,"Schmeichel → Solskjær, Man Utd v Sunderland",Premier League OFFICIAL,cVtF64Un-0o,https://youtu.be/cVtF64Un-0o,06:56–07:13,"07:00–07:10 one continuous pan, throw to goal",
Goalkeepers With Unbelievable Assists,2,"Čech → Drogba, Wolves v Chelsea",Premier League OFFICIAL,cVtF64Un-0o,https://youtu.be/cVtF64Un-0o,01:24–01:53,01:42–01:44 the punt (settles the foot) · 01:44–01:53 pitch-level slow-mo,
Goalkeepers With Unbelievable Assists,1,"Van der Sar → Rooney, Man Utd v Aston Villa",Premier League OFFICIAL,cVtF64Un-0o,https://youtu.be/cVtF64Un-0o,04:14–04:45,04:32–04:38 Van der Sar with Ferdinand and Evra — the money shot,
Top 10 Pace Abuser Moments Part 2,10,Son Heung-min — the Burnley solo goal,"Tottenham OFFICIAL, Puskás package",C-CefuZ6h1k,https://youtu.be/C-CefuZ6h1k,00:00–03:19,02:40–03:19 ULTRA SLOW-MOTION HEAD-ON — the only angle that carries the one-footed point,Ten angles. Mask the subscribe panel at 00:21–00:35 and the end card at 03:20
Top 10 Pace Abuser Moments Part 2,9,Terens Puhiri — Borneo FC v Mitra Kukar,"Guardian Football, 7.8M",kjdKZOcXlbk,https://youtu.be/kjdKZOcXlbk,00:00–00:52,whole clip is the run,"52s, dedicated"
Top 10 Pace Abuser Moments Part 2,8,Van de Ven — Spurs v Copenhagen,Tottenham OFFICIAL,h_stLgq5Rps,https://youtu.be/h_stLgq5Rps,01:04–01:23,"one unbroken wide pan, no replays",
Top 10 Pace Abuser Moments Part 2,7,Adeyemi — Dortmund v Chelsea,DAZN,nPZGlV1rBM4,https://youtu.be/nPZGlV1rBM4,00:00–01:31,whole clip is the run,"91s, dedicated. Clock 62:20 → 62:45"
Top 10 Pace Abuser Moments Part 2,6,Bale v Maicon — Spurs 3-1 Inter,TNT Sports,JOirPSqL28w,https://youtu.be/JOirPSqL28w,00:00–01:26,00:32–00:34 low tight sideline — Maicon grabs his shoulder · 01:14–01:20 low reverse slow-mo,"86s, FOUR separate runs. [!] Bale does not score in this footage"
Top 5 Players Who Deserve The Oscar Award Part 2,5,"Neymar rolling — Mexico, 2018",FIFA,9qjGKKitwXo,https://youtu.be/9qjGKKitwXo,01:46–02:19,,[!] Use ONLY to 02:19. He rolls ONCE — every longer cut is padded
Top 5 Players Who Deserve The Oscar Award Part 2,4,Micah Richards — Aston Villa v Stoke,CBS Sports Golazo,RscP6Vaghd4,https://youtu.be/RscP6Vaghd4,00:59–01:20,the clip AND the studio reaction in one,
Top 5 Players Who Deserve The Oscar Award Part 2,3,Breel Embolo — Switzerland v Argentina,"real footage, three slow-mo angles",1O-qw6iaLOk,https://youtu.be/1O-qw6iaLOk,00:00–02:10,00:38 reverse sideline — airborne BEFORE any contact,
Top 5 Players Who Deserve The Oscar Award Part 2,2,"Suárez — the Chiellini bite, 2014","ESPN broadcast, unedited",1tVdCQaH0vs,https://youtu.be/1tVdCQaH0vs,00:00–01:10,00:11–00:15 cupping his mouth · 01:07–01:10 pulls his collar over his face,
Top 5 Players Who Deserve The Oscar Award Part 2,1,"Rivaldo, 2002 v Turkey",2.55M,OiW0IPrv1Ro,https://youtu.be/OiW0IPrv1Ro,00:13–00:15,,"25s clip, no scorebug anywhere"
Top 5 Die for the Badge (2026 Redo),5,Valverde on Morata — Supercopa final,Italian network NOVE,3JiwVYCnHqU,https://youtu.be/3JiwVYCnHqU,00:02–00:04,,Match clock 114:29. Simeone pats his head as he walks off
Top 5 Die for the Badge (2026 Redo),4,"Van de Ven — Europa League final, Bilbao",Tottenham OFFICIAL,vWC-USe1ncI,https://youtu.be/vWC-USe1ncI,00:39–01:10,"00:39 the live clearance, replays to 01:10",Match clock 67:38
Top 5 Die for the Badge (2026 Redo),3,"Süle v Mbappé — DORTMUND, not Bayern",DAZN,vjTC2gCMtqM,https://youtu.be/vjTC2gCMtqM,00:13–00:15,,Match clock 16:34–16:36
Top 5 Die for the Badge (2026 Redo),2,John Stones — off the line in front of Salah,Man City OFFICIAL,MriNd_wn1Os,https://youtu.be/MriNd_wn1Os,00:55–01:40,01:26–01:32 LOW REVERSE FROM BEHIND THE NET — the hook across Salah,[!] The 11mm figure is NOT in this footage. The graphic reads only NO GOAL
Top 5 Die for the Badge (2026 Redo),1,FERLAND Mendy v Man City — not Édouard,TNT / BT Sport,WgzZRA260X0,https://youtu.be/WgzZRA260X0,00:15–00:18,,Match clock 86:11–86:13
Worst Penalty Miss With Every Technique Part 2,5,"Zaza, Euro 2016 — STUTTER",Stade de Bordeaux,5_9OwlwAMMk,https://youtu.be/5_9OwlwAMMk,00:14–00:23,00:21–00:23 close-up — number 7 legible on chest and shorts,
Worst Penalty Miss With Every Technique Part 2,4,"Pires & Henry, Highbury — PASS","34s, carries BOTH halves",N4bQVTczcLQ,https://youtu.be/N4bQVTczcLQ,00:00–00:34,00:12–00:18 HIGH REVERSE behind the North Bank — the studs clipping the ball,00:19–00:21 tunnel interview · 00:22–00:34 the Sparta Prague callback. END ON THAT
Worst Penalty Miss With Every Technique Part 2,3,Agüero v Chelsea — PANENKA,Sky Sport DE — UPGRADED SOURCE,he7mZJDIEOQ,https://youtu.be/he7mZJDIEOQ,01:23–01:43,,"Full German commentary, official PL scorebug, four angles"
Worst Penalty Miss With Every Technique Part 2,2,"Budimir v Valencia, 97th minute",Arena Sport 1,4EvIcyRuAXg,https://youtu.be/4EvIcyRuAXg,00:00–00:38,00:30–00:35 LOW PITCHSIDE FROM THE RIGHT — the standing leg collapsing and the toe-scuff,Mask the betting graphics bottom left throughout
Worst Penalty Miss With Every Technique Part 2,1,Eze v PSG — the CL final shootout,ARSENAL'S OWN OFFICIAL CHANNEL,ygcv9fQheII,https://youtu.be/ygcv9fQheII,01:22–01:27,01:23 run-up · 01:25 strike · 01:26–01:27 EZE 10 legible on his back,[!!] OUTCOME DISPUTED — see the note under this table. Shootout starts 01:12
When Goalkeepers Make Accidental Saves,5,Full Reverse Save,"the reference itself, its #6 entry",ZbunM6UKwts,https://youtu.be/ZbunM6UKwts,—,,[!] No standalone clip exists. Lift it from the reference
When Goalkeepers Make Accidental Saves,4,No-Look Save,"the reference itself, its #5 entry",ZbunM6UKwts,https://youtu.be/ZbunM6UKwts,00:07–00:13,,
When Goalkeepers Make Accidental Saves,3,IDK Save,"the reference itself, its #4 entry",ZbunM6UKwts,https://youtu.be/ZbunM6UKwts,00:14–00:22,,
When Goalkeepers Make Accidental Saves,2,Neuer v Bas Dost — the heel he can't see,Legendary Goal Line Saves,PaaZxPh0A-o,https://youtu.be/PaaZxPh0A-o,02:00–02:08,02:04–02:07 GROUND-LEVEL REVERSE FROM INSIDE THE NET — the ball meeting his trailing heel,Mask the Score 90 overlay bottom left
When Goalkeepers Make Accidental Saves,1,Choupo-Moting stops his OWN team scoring,Legendary Goal Line Saves,PaaZxPh0A-o,https://youtu.be/PaaZxPh0A-o,05:05–05:19,,On-screen caption in the source reads “200 IQ”
```

#### `typeb.py`
<!-- FILE: typeb.py · 14935 bytes · 239 lines · sha256 0a19958a5040264362ce11a9f7531d2e742cf4c8b9df33f7630ead0cffdf8e59 -->
*Built 21 Sep on 'provide the player name ones with no descriptions' (E22). 9 packs, 45 picks; V = verified against a written source, C = from Joel's comments. 22 Sep: Michu flipped C→V (Wikipedia: 18 PL / 22 all comps). Now 25 V / 19 C / 1 unmarked.*
```python
# -*- coding: utf-8 -*-
# TYPE B PACK SHEETS — the nine packs with no clips and no forensic descriptions.
# For Type B the equivalent of a description is a VERIFIED FACT: what is true, where it is
# confirmed, the line to say, and what not to claim.
# V = verified this session with a named source.  C = came from his own comments, not yet sourced.

SHEETS = [
("Players We Always Mispronounce", "PLAYER-NAME FAMILY", "locked",
 "The pronunciation IS the product, so every one below is sourced rather than written from memory.",
 [
 ("5","Khvicha Kvaratskhelia","V",
  "Commentators gave up and simply say “Kvara”. Babbel's Euro 2024 guide listed him among the "
  "trickiest names and had to supply an AUDIO clip because writing it out did not work.",
  "Babbel Euros pronunciation guide · 30 likes in your comments",
  "Do not attempt a written phonetic on camera — even a linguistics company would not."),
 ("4","César Azpilicueta — the one who got RENAMED","V",
  "“Ath-pee-lee-KWE-ta”. Nobody could say it, so Chelsea fans and teammates called him DAVE — for "
  "a decade, in songs, to his face. A Premier League captain got a new name because of a pronunciation.",
  "CHELSEA'S OWN WEBSITE tells the story of how the nickname started · Bleacher Report",
  "The strongest entry and it is barely about phonetics. Lead on “they renamed him”."),
 ("3","Wojciech Szczęsny","V",
  "“VOY-check Sh-CHENS-ny”, not “Woj-chi-ech Shez-nee”. Arsenal, Roma, Juventus, Barcelona — two "
  "decades at the top. The ę is a nasal vowel English has no equivalent for, which is why nobody lands it.",
  "Published list of names commonly mispronounced · Babbel lists him among the Euros' trickiest",
  "The spelling on screen is a visual gag on its own."),
 ("2","Thierry Henry","C",
  "He says it differently depending on which language he is speaking — the man himself gives two answers.",
  "49 likes in your comments. NOT independently sourced.",
  "[!] Find the clip of him saying it both ways before you assert this."),
 ("1","Mesut Özil — and there are TWO right answers","V",
  "Not “Ozzil”. German is “MAY-zoot UR-zil”, IPA [ˈmeːzut ˈøːzil]. Turkish is “meh-SOOT ur-ZEEL”, "
  "IPA [meˈsut œˈzil] — different stress in BOTH words. Born in Germany to a Turkish family, so both "
  "are correct and they are not the same.",
  "Wikipedia's own IPA transcription, both languages",
  "The hard declarative finisher: you watched him a decade and never said it either way."),
 ]),

("Players Who Could've Played For Another Nation", "PLAYER-NAME FAMILY", "locked",
 "Your edge here is that you EXPLAIN the link rather than just naming it.",
 [
 ("5","Bukayo Saka — NIGERIA","C",
  "Both parents Nigerian. Nigeria said publicly they would take him but would not beg for him.",
  "Press reports. Worth one check before the quote goes on camera.",""),
 ("4","Michael Olise — ENGLAND","C",
  "Eligible for FOUR nations. Southgate personally tried to turn him in 2022.",
  "Press reports. The four-nation claim is the one to verify precisely.",
  "[!] Name the four on screen or do not use the number."),
 ("3","Alphonso Davies — LIBERIA","C",
  "Born in the Buduburam refugee camp in Ghana to Liberian parents; chose Canada.",
  "Widely reported. The camp name is specific enough to check.",""),
 ("2","Kylian Mbappé — ALGERIA","C",
  "Mother Algerian, father Cameroonian. 41 likes across four comments asked for this.",
  "Your comments. The reference used him for CAMEROON, so say Algeria and you are not re-cutting.",""),
 ("1","Lionel Messi — SPAIN","V",
  "Pékerman has said the paperwork was prepared to cap him for Argentina's U-20s precisely BECAUSE "
  "Spain were circling. Messi has said it never crossed his mind.",
  "Both quotes are on the record in the Spanish press.",
  "The hard finisher: the paperwork existed."),
 ]),

("Players We Always Forget Played for That Club", "PLAYER-NAME FAMILY", "noproof",
 "[!] LANE CAVEAT: the best video in this lane did 77,617 against your 89k median. Shoot it knowing "
 "there is no format precedent. The picks are strong; the lane is unproven.",
 [
 ("5","Andrea Pirlo at INTER MILAN","C",
  "Before he was Pirlo he was an Inter player, in a role nobody worked out. Milan then moved him in "
  "front of the back four and he became the best deep-lying playmaker alive.",
  "Career record. Safe.",""),
 ("4","Arjen Robben at CHELSEA","C",
  "Three seasons at Stamford Bridge, 2004–07, TWO Premier League titles — before Madrid, before Bayern.",
  "Career record. Safe. 1,889 likes on a comment asking for it.",
  "You dropped this in a revision once; it was restored. Keep it."),
 ("3","Kevin De Bruyne at CHELSEA","C",
  "Mourinho told him he was SIXTH CHOICE. De Bruyne says they spoke twice in total. Sold to Wolfsburg, "
  "came back to City, became the best midfielder in the league.",
  "De Bruyne has told this himself in interviews — worth pulling the exact quote.",""),
 ("2","Thierry Henry at JUVENTUS","C",
  "Signed 1999, played out of position on the WING, gone in half a season. Arsenal bought him for "
  "less than Juventus had paid.",
  "Career record. The fee comparison is the bit to check.",""),
 ("1","Frank Lampard at MANCHESTER CITY","V",
  "He scored against Chelsea, on loan, and REFUSED TO CELEBRATE — stood dead still with his arms up. "
  "It denied Chelsea the win.",
  "SKY SPORTS headline: “Frank Lampard goal against Chelsea for Man City was 'weird', says Gary Cahill”. "
  "Man City's own channel has the footage.",
  "Best entry in the pack, and it is the REACTION not the transfer. One readable image."),
 ]),

("Players We Always Blame First", "PLAYER-NAME FAMILY", "noproof",
 "[!] LANE CAVEAT: the football version has gone 369,137 and 142,421. A HOCKEY version of the same "
 "format did 200,711 off an 18,400-sub channel, and NBA 91.7k. The concept travels; the football "
 "execution has not. Arguably your opening.",
 [
 ("5","David Beckham, 1998","C","Sent off v Argentina; an effigy was hung outside a pub. He did not concede the goals.",
  "Widely documented.",""),
 ("4","Bukayo Saka, Euro 2020","C",
  "Nineteen years old, fifth penalty, racially abused for a shootout he was sent up LAST to take.",
  "Widely documented.",
  "[!] Handle with care on camera. The abuse is the point, not the miss."),
 ("3","John Terry, 2008 final","C",
  "Slipped on a waterlogged spot. Anelka still had to score after him and did not.",
  "Match record.",""),
 ("2","Roberto Baggio, 1994","C",
  "Dragged Italy to the final almost single-handedly, missed one penalty, and that is all anyone "
  "remembers.",
  "Match record.",""),
 ("1","Loris Karius, 2018 final","V",
  "CONCUSSED by Ramos's elbow — diagnosed days later by a Boston hospital — and blamed for a decade.",
  "The concussion diagnosis is on the record and is what makes this the finisher.",
  "The hard declarative: he was concussed and nobody waited to find out."),
 ]),

("Top 5 Shortest Lived Primes (2026 Redo)", "", "locked",
 "[!] TWO PART 1 ERRORS ARE BURNED INTO THE CAPTIONS, not just the voiceover: £80 MILLION at 0:29 "
 "(Torres was ~£50m) and 2 BALLON D'ORS at 1:18 (Ronaldinho won one, 2005). A re-voice will not fix "
 "them — correcting yourself on camera is the strongest hook this redo has.",
 [
 ("5","João Félix","C","Most expensive teenager ever, Saudi league at 26.","2,800 likes.",""),
 ("4","Dele Alli","C","Two PFA Young Player awards, then out of football.","2,357 likes.",""),
 ("3","Andrey Arshavin","C","Four goals at Anfield in one night, then gone.","1,365 likes.",""),
 ("2","Michu","V","One season: EIGHTEEN in the Premier League, TWENTY-TWO in all competitions (2012-13), then an "
  "ankle that never recovered. Retired 25 July 2017 aged 31 over the right ankle.",
  "Wikipedia — Michu (statistics table: 18 PL / 22 all comps; retirement date and reason quoted). 167 likes on the comment.",
  "Say EIGHTEEN if you mean the league, TWENTY-TWO if you mean the season — do not mix them."),
 ("1","Marco van Basten","V",
  "THREE Ballon d'Ors — 1988, 1989, 1992. LAST MATCH at 28: the 1993 Champions League final against "
  "Marseille, 29 May 1993, substituted on 86 minutes after another ankle injury. He then spent TWO "
  "YEARS trying to come back and formally retired on 17 August 1995, aged 30.",
  "Wikipedia, dates and Ballon d'Or years confirmed.",
  "[!!] SAY “last game at 28” or “finished at 28” — NOT “retired at 28”. He retired at 30. The "
  "two-year gap of failed comebacks is a better story than the wrong number anyway."),
 ]),

("Transfers That Almost Happened", "", "locked",
 "SETTLED: shooting as the top-5 as built. Each pick is a one-line fact, not a saga — which is why "
 "the countdown works and the reference's single-story shape does not apply.",
 [
 ("5","Ronaldinho → Manchester United, 2003","C",
  "He has said he was 48 HOURS from signing. United had just sold Beckham. He went to Barcelona and "
  "won the Ballon d'Or two years later.",
  "Ronaldinho has told this himself.",""),
 ("4","Lewandowski → Blackburn Rovers, 2010","V",
  "An ACT OF GOD stopped it — the Icelandic volcanic ash cloud grounded his flight to England.",
  "SKY SPORTS has it twice, and Lewandowski confirmed it in his own words: “Volcano stopped me from "
  "joining Blackburn”.",
  "The most repeatable fact in the pack."),
 ("3","Neymar → Real Madrid","V",
  "Florentino Pérez has said publicly that Neymar PASSED A MEDICAL with Madrid before the Barcelona "
  "move. Neymar has separately said he nearly chose Bayern because of Guardiola.",
  "GOAL: “Neymar passed a medical with Madrid — Madrid president Pérez”.",
  "Replaced Neymar→Man City, which was the weakest-sourced of the three versions."),
 ("2","Fekir → Liverpool, 2018","C",
  "So far gone he had ALREADY DONE THE CLUB INTERVIEWS in a Liverpool shirt. Collapsed at the medical "
  "over a knee. He has since accused Liverpool of making excuses.",
  "Widely reported; the interview footage exists.",""),
 ("1","De Gea → Real Madrid, 2015","C",
  "Deadline day. The move died because THE PAPERWORK WAS NOT SUBMITTED IN TIME — the infamous fax. "
  "He stayed at United eight more years.",
  "Widely reported.",
  "The strongest single story and the most famous. Lead the video on it if you ever split this pack."),
 ]),

("What If PSG Kept Messi, Neymar & Mbappé", "", "locked",
 "FACTS, not scenarios — your correction, applied. [!] The reference is an EA FC sim; you are "
 "shooting this as a labelled experiment.",
 [
 ("5","They once scored SIX between them in one game","V",
  "Clermont 1–6 PSG. Mbappé hat-trick, Neymar hat-trick, Messi a hat-trick of ASSISTS. Three "
  "hat-tricks in one match.",
  "Goal, CBS and ESPN.",""),
 ("4","They fell out over who takes penalties — in public","V",
  "PSG 5–2 Montpellier, 13 August 2022, first home game of the season. MBAPPÉ MISSES a penalty. "
  "Afterwards NEYMAR LIKES tweets attacking the arrangement, one reading: “Now it's official, Mbappé "
  "is the one who takes penalties at PSG. Clearly it's a contract thing, because in no club in the "
  "world would Neymar be the second taker.” The press called it Penaltygate.",
  "ESPN, Goal and Get French Football News. Galtier and the club president both had to answer for it.",
  "The evidence is his LIKES — a very modern, very readable beat."),
 ("3","Messi won a Ballon d'Or as a PSG player","V",
  "His 2021 award came after he had already signed. PSG have had a reigning Ballon d'Or winner on the "
  "pitch and still never won the thing they bought him for.",
  "Record.",""),
 ("2","They never won a Champions League together","V",
  "Ligue 1 titles, no European Cup — and PSG finally won it after all three had gone.",
  "Record.",""),
 ("1","All three were gone within two years","V",
  "Messi to Miami, Neymar to Al-Hilal, Mbappé to Madrid. The most expensive front three ever "
  "assembled did not survive two full seasons.",
  "Record.","The hard declarative finisher."),
 ]),

("What If Messi & Ronaldo Swapped Nationalities", "", "locked",
 "Written from INSIDE the premise — every entry states what WOULD happen. [!] Reference is an EA FC "
 "sim; labelled experiment.",
 [
 ("5","Messi lifts the Euros in 2016","V",
  "Portugal won that final with Ronaldo in tears on the touchline after 25 minutes. Swap them and "
  "Messi is the one carried off — and Portugal still win, so he has a major trophy at 29 not 34.",
  "2016 Euro final, real result.",""),
 ("4","Ronaldo plays in the 2022 World Cup final","V",
  "Argentina get there and win it. He is 37 that December — exactly the age Messi was.",
  "2022 World Cup final, real result.",""),
 ("3","Ronaldo finally wins a Copa América","V",
  "Argentina won it in 2021 and again in 2024. His trophyless international record — the biggest "
  "stick used against him — disappears.",
  "Real results.",""),
 ("2","Messi's drought gets WORSE, not better","V",
  "Portugal lost a Euro final in 2004 and a semi in 2012 before they won anything.",
  "Real results.","The counter-intuitive one. Keep it at #2."),
 ("1","The GOAT argument ends on the day of the swap","",
  "Every single thing people argue about is national. Whoever gets Argentina wins a World Cup and a "
  "Copa. Whoever gets Portugal wins a Euro and a Nations League. Not one club trophy changes.",
  "Follows from the four above.","The argument the video exists to make."),
 ]),

("What If Ronaldo Never Left Real Madrid", "", "locked",
 "Five things that WOULD happen if he stayed — your correction, applied. [!] Reference is a FIFA 19 "
 "career-mode sim on a modded save; labelled experiment.",
 [
 ("5","He passes 500 Real Madrid goals","V",
  "He left on 450 in 438 games. Two more seasons near that rate and he is the first man to 500 for "
  "the club — a number nobody would touch.",
  "Club record.","The hook, because it is a number the comments will argue about."),
 ("4","Benzema never becomes the main man","V",
  "Benzema spent nine years making space for Ronaldo. The moment Ronaldo left he became Madrid's "
  "leader and won a Ballon d'Or at 34.",
  "Record.",""),
 ("3","Madrid's three empty seasons look nothing alike","V",
  "After he left they went three years without a Champions League having just won three in a row.",
  "Record.",""),
 ("2","The Juventus experiment never happens","V",
  "Juventus bought him to win a Champions League and went out earlier each year. That chapter — and "
  "the United return after it — only exists because he left.",
  "Record.",""),
 ("1","The all-time record is bigger and it is not close","V",
  "His goals-per-game at Madrid was the best of his career by distance. Every season there instead of "
  "anywhere else adds to a career record that is already the highest in the sport.",
  "Record.",""),
 ]),
]
```

### 6.3 The send-off build

#### `handover/data.py`
<!-- FILE: handover/data.py · 64432 bytes · 791 lines · sha256 789bdfa59d63be6da49aed2b3fdf22679c220f046a4851b92b40cf10c0fe19bf -->
*The production sheets Joel shoots from, plus GLANCE, DECISIONS, SYSTEMS, VERIFIED. Rewritten through the session: GK assists four methods / Čech LEFT / Ederson goal kick; Son Puskás and no touch count; Stones KEPT and 11mm; Pires & Henry KEPT; Mispronounce filled; Budimir in (22 Sep — it had still said Tah, E24); Eze DISPUTED; Oscar order settled; badge-redo header settled; Michu 18/22.*
```python
# -*- coding: utf-8 -*-

GLANCE = [
 # (title, status, one-line)
 ("Top 10 Signature Moves (2026 Redo)","READY","Five clean, all described, Cruyff's own quote is your closer."),
 ("Goalkeepers With Unbelievable Assists","READY","Five clean. Say FOUR delivery methods on camera — corrected."),
 ("Top 10 Pace Abuser Moments Part 2","READY","Five clean. Every run is one-footed — that's your hook line."),
 ("Top 5 Players Who Deserve The Oscar Award Pt2","READY","Five clean. YOUR CALL: approved order stands, Embolo at #3."),
 ("Top 5 Shortest Lived Primes (2026 Redo)","READY","Type B, no clips needed. Two Pt1 errors to correct on camera."),
 ("Players Who Could've Played For Another Nation","READY","Type B, no clips needed. Your edge is that you explain the link."),
 ("Top 5 Die for the Badge (2026 Redo)","READY","YOUR CALL: Stones kept and now described. Pt1 says 11.7mm — it is 11mm."),
 ("Worst Penalty Miss Every Technique Pt2","READY","SETTLED: Budimir replaces Tah. Five failure shapes, no two alike."),
 ("When Goalkeepers Make Accidental Saves","READY*","Five described. Title promise is the known weakness — your call, taken."),
  ("Transfers That Almost Happened","READY","SETTLED: shooting as the top-5 as built. Each pick is a one-line fact."),
 ("Players We Always Forget Played for That Club","LANE ONLY","Riding your own Full Name Pt1 as proof. Shoot knowing that."),
 ("Players We Always Mispronounce","READY","YOUR CALL: filled. Azpilicueta, Szcz\u0119sny and \u00d6zil added, all sourced."),
 ("Players We Always Blame First","LANE ONLY","Same. Five strong picks from your comments, no format precedent."),
 ("What If Messi & Ronaldo Swapped Nationalities","READY","YOUR CALL: shoot as a labelled experiment. Type B, no clips."),
 ("What If Ronaldo Never Left Real Madrid","READY","YOUR CALL: shoot as a labelled experiment. Type B, no clips."),
 ("What If PSG Kept Messi, Neymar & Mbappé","READY","YOUR CALL: stat dropped, re-ranked, Penaltygate verified and in at #4."),
]

# pack sheets: (title, status, meta, verdict, reference, picks[(rank,name,why,links,cut)], warn, decision)
READY = [
{
 "title":"Top 10 Signature Moves (2026 Redo)",
 "status":"READY TO SHOOT",
 "meta":"Runs 5→1 · reference gaLafBORfYA is your own Part 1 (ran 10→6)",
 "verdict":"Cleanest pack in the batch. Zero overlap with Part 1, all five described from a scoped pass, "
  "and the number one has a payoff line straight from Cruyff's own mouth.",
 "picks":[
  ("5","Robben's cut-in — Bayern v Juventus, Turin",
   "Everyone in the stadium knows what is coming and it still works.",
   ["qDgAANEXQqg — BT Sport, 02:02–02:24"],
   "NO STEPOVERS — pure deceleration and one sharp cut across Evra (33) with the inside of the LEFT boot, "
   "with Barzagli (15) sliding in behind. Then inside-of-the-left-foot curl, waist height, right to left, "
   "past Buffon full stretch into the far corner. CUT ON: the low reverse angle at 02:23 from behind the "
   "net looking out through the netting. NO COMMENTARY on this source — carry it on your voice."),
  ("4","Ronaldinho's elástico — the nutmeg on Dunga",
   "The Gre-Nal derby. Grêmio v Internacional, and Dunga's number 8 is legible on his back.",
   ["LXqPEpeokCg — 02:20–02:35"],
   "ENTIRELY ONE FOOT. He drops his hips, pushes the ball 1–1.5 FEET right with the OUTSIDE/TOE of the "
   "right boot, then — WITHOUT THAT FOOT EVER TOUCHING THE GROUND — whips it round the outside and snaps "
   "it back inside-left with the same boot, straight through Dunga's open legs. Dunga is left stranded "
   "MID-AIR with his right leg kicked out high. CUT ON: the second star-wipe replay at 02:29, zoomed tight "
   "on the footwork. The period star wipes are worth keeping."),
  ("3","Iniesta's croqueta — v Manchester City",
   "Two defenders, a gap of one to one-and-a-half metres, and he goes through it.",
   ["Zs3bmAJ4nq0 — 01:38–01:47"],
   "Inside of the RIGHT foot pushes it across his body right-to-left about half a metre, past #4's "
   "outstretched leg. BOTH FEET LEAVE THE TURF in a synchronised hop. The LEFT foot lands and its inside "
   "pushes forward into the corridor. ALL INSIDE ONE RUNNING STRIDE. Neither defender touches the ball or "
   "him, and they do not collide. He comes out right in front of the referee, who steps aside. "
   "CUT ON: the low pitchside reverse slow motion at 01:44."),
  ("2","Messi's body feint — v Weligton, Camp Nou",
   "A trick where the ball is never touched. The whole move is body.",
   ["VzUWrhh7UQE — 03:22–03:56"],
   "HE DOES NOT TOUCH THE BALL DURING THE FEINT. It rolls on its original line while his whole body "
   "changes shape around it — left shoulder drops, hips sink into a crouch, left foot plants WIDE LEFT "
   "pointing at the byline, head down, right arm wide, left arm across his chest. Weligton bites, lunges "
   "with his right leg, overextends, throws his LEFT ARM ACROSS MESSI'S CHEST in panic. Messi springs off "
   "the planted foot and pushes it RIGHT with the outside of the LEFT foot. The hand slips off his chest; "
   "Weligton's legs cross and he stumbles. CUT ON: the extreme close-up ultra-slow-motion at 03:36, "
   "cropped mid-chest down. Audio is stripped — music only."),
  ("1","The Cruyff turn — Netherlands v Sweden, 1974",
   "The move that is named after him, and he explains it himself on camera.",
   ["PBgLInYqhmo — live 00:05–00:11, the turn at 00:08–00:10, slow motion 00:17–00:26"],
   "Left flank, 5–6 yards outside the box. Receives with the OUTSIDE/INSTEP of the RIGHT boot facing the "
   "corner flag, Sweden's #2 with a forearm on his back to stop him turning. Plants the LEFT foot, lifts "
   "the RIGHT in an exaggerated HIGH BACKLIFT as if to cross — then brings it OVER THE TOP and drags the "
   "ball with the INSIDE of the same foot BEHIND HIS PLANTED LEG, pivoting 180° counter-clockwise. The "
   "defender is left two to three paces behind. Cruyff is #14 with the white captain's armband, in the "
   "orange shirt with TWO black sleeve stripes because he refused the third."),
 ],
 "warn":"Robben, Ronaldinho, Iniesta and Messi sources all have music over them and no commentary. Only the "
  "Cruyff clip has usable audio — and it is the best audio in the batch.",
 "decision":"None. Shoot it.",
 "quote":"CLOSE ON THIS, VERBATIM, FROM CRUYFF HIMSELF: “I never did on a training or in free times tricks. "
  "I never did tricks. I saw something and I did it, and it just came out. There was an opponent there and "
  "I had to outplay him. That was the easiest way, so you just do it.”",
},
{
 "title":"Goalkeepers With Unbelievable Assists",
 "status":"READY TO SHOOT",
 "meta":"All five from ONE official Premier League compilation \u00b7 cVtF64Un-0o \u00b7 RE-CUT AFTER A SECOND, "
  "DEEPER PASS \u2014 two corrections below",
 "verdict":"Five picks, one source, every clip labelled on screen by the compilation itself with keeper, "
  "fixture and season. The tidiest sourcing in the batch. A second scoped pass per clip corrected two "
  "things the first pass got wrong, and both corrections make the pack stronger.",
 "picks":[
  ("5","Ederson \u2192 Ag\u00fcero \u2014 Man City v Huddersfield, 2018/19",
   "[!!] CORRECTED: it IS a goal kick. The earlier sheet said open play and that was wrong.",
   ["cVtF64Un-0o at 00:12\u201300:38"],
   "LEFT FOOT, struck off the ground \u2014 but from a DEAD BALL inside the six-yard box, not from open play. "
   "The written record calls it a goal-kick assist and reports it at 85\u201386 yards, not the 70\u201375 this "
   "sheet used to claim. Low, FLAT and driven rather than lofted \u2014 it never climbs high, which is the "
   "opposite shape to Van der Sar's. One bounce outside the arc into Ag\u00fcero's stride. Ag\u00fcero takes one "
   "soft RIGHT-foot touch to round the committed keeper, then CHIPS IT WITH HIS LEFT into the open net. "
   "CUT ON: the static high tactical wide at 00:29\u201300:38 \u2014 it holds both players, the whole ball flight "
   "AND Guardiola's fist pumps in one unbroken frame. "
   "COMMENTARY: \u201cAg\u00fcero goes for elevation, and achieves perfection! And Pep Guardiola indulged in the "
   "most joyous of fist pumps.\u201d"),
  ("4","Alisson \u2192 Salah \u2014 Liverpool v Man United, 2019/20",
   "The one where the commentary makes the onside point for you.",
   ["cVtF64Un-0o at 00:00\u201300:11"],
   "RIGHT-FOOT SIDE-VOLLEY DROP-KICK STRAIGHT OUT OF THE HANDS. Flat and fast, skimming over the "
   "retreating United players rather than looping \u2014 the opposite of \u010cech's. One bounce inside the United "
   "half. Salah starts inside his OWN half, which is what keeps him onside and what the commentary leans "
   "on. James (21) leans into him at 25 yards; Salah holds him off, guides it LEFT into the box and "
   "finishes with the INSIDE OF THE LEFT low under de Gea. Shirt off at the Kop. "
   "ONE UNBROKEN LIVE SHOT, no replays \u2014 clean to cut, but you only get the one look. "
   "NOTE the referee is in a SKY-BLUE shirt, not the usual black, which dates the clip. "
   "[!] Alisson's length-of-the-pitch celebration is NOT in this clip \u2014 it cuts at 00:11. Separate "
   "source needed if you want it."),
  ("3","Schmeichel \u2192 Solskj\u00e6r \u2014 Man Utd v Sunderland, 1996/97",
   "The only throw in the pack, and the oldest picture.",
   ["cVtF64Un-0o at 06:56\u201307:13"],
   "He CATCHES a Sunderland set piece above head height, turns, takes two strides and launches an "
   "OVERHAND RIGHT-ARM THROW, javelin style, clearing the halfway line ON THE FLY. "
   "[!] Distance estimates moved between passes \u2014 45\u201350 yards on one, 55\u201360 on another. Neither is "
   "measurable from the footage. Say \u201cpast the halfway line on the full\u201d, which IS visible, and skip the "
   "number. Kubicki (2) swings at the bounce and MISSES COMPLETELY. Solskj\u00e6r takes it in stride and "
   "CHIPS IT RIGHT-FOOTED over P\u00e9rez. Schmeichel in the purple-and-black GEOMETRIC Umbro kit. "
   "PICTURE: 4:3 SD inside a 16:9 frame with BLURRED PILLARBOX BARS down the sides, interlacing judder "
   "on the pans, chroma bleed on the reds. Do not hide it \u2014 say \u201c1996\u201d and the picture becomes the point. "
   "BOARDS sell the era better than any caption: SHARP VIEWCAM, McDonald's, Carling, CIS, Ryman, "
   "Wilkinson Sword, and KELLOGG'S FROSTIES WITH TONY THE TIGER ON THE HOARDING. "
   "COMMENTARY (Martin Tyler): \u201cKubicki's missed the challenge! And Solskj\u00e6r is all on his own! ... "
   "Isn't that a cool finish!\u201d"),
  ("2","\u010cech \u2192 Drogba \u2014 Wolves v Chelsea, 2009/10",
   "[!!] CORRECTED: it is his LEFT foot. The earlier sheet said right.",
   ["cVtF64Un-0o at 01:24\u201301:53"],
   "Ball in both hands, POINTS UPFIELD WITH HIS RIGHT HAND to send the runners, two measured strides, "
   "then a DROP-PUNT OUT OF THE HANDS WITH THE LEFT FOOT. A dedicated tie-breaker pass on the close "
   "replay graded this CERTAIN with the contact frame fully visible and unobscured: he PLANTS ON THE "
   "RIGHT, the LEFT leg swings back and drives up through the ball, the LEFT boot connects just after "
   "release, and the LEFT leg extends high on the follow-through. Two passes now say left. "
   "The flight is HIGH AND BOOMING, climbing above the floodlight line before dropping \u2014 the opposite "
   "of Alisson's flat drive. One bounce outside the Wolves box. Drogba starts on Berra's (16) blindside, "
   "MUSCLES STRAIGHT PAST HIM without breaking stride, takes it past Hahnemann with the OUTSIDE OF THE "
   "RIGHT and rolls it in with the right. LEAPS ONTO THE PERIMETER WALL into the away support. "
   "\u010cech in the black rugby headguard, black adidas with acid-green stripes and green socks. "
   "CUT ON: the pitch-level slow motion at 01:44\u201301:53 following the Berra duel to the finish."),
  ("1","Van der Sar \u2192 Rooney \u2014 Man Utd v Aston Villa, 2010/11",
   "The only one where the keeper gets his moment on camera. End the video here.",
   ["cVtF64Un-0o at 04:14\u201304:45"],
   "RIGHT FOOT, struck off the ground, from a ROLLING BACKPASS in OPEN PLAY \u2014 three-step approach. This "
   "is what separates it from Ederson's dead ball, and it is why the pack has four delivery methods "
   "rather than three. HIGH AND LOOPING, roughly 70 yards, one bounce into Rooney's stride. "
   "Rooney runs the gap between the two Villa centre-backs, CUSHIONS IT WITH THE RIGHT, lets it sit, "
   "and strikes a HALF-VOLLEY with the INSTEP OF THE RIGHT. Friedel dives left and gets nowhere near it. "
   "THE ENDING, and it runs long: Rooney blows kisses with BOTH HANDS at the corner flag \u00b7 NANI leaps "
   "on his back first, then FLETCHER, then FERDINAND \u00b7 then the camera CUTS BACK TO VAN DER SAR at his "
   "own end pumping both fists \u00b7 FERDINAND JOGS THE FULL LENGTH BACK TO EMBRACE HIM \u00b7 and EVRA LEAPS "
   "INTO VAN DER SAR'S ARMS. No other clip in this pack shows the keeper being celebrated. "
   "COMMENTARY: \u201cOne chance, one goal, and he will feel a whole lot better now... Edwin van der Sar "
   "playing his part, and Rooney was ruthless.\u201d"),
 ],
 "warn":"[!!] SCRIPT CORRECTION, AND IT IS GOOD NEWS. The pack was written as five delivery methods. An "
  "earlier pass cut that to THREE and told you to say three. A second scoped pass says that was wrong in "
  "your favour \u2014 it is FOUR, because two deliveries that were grouped together are not the same act at "
  "all. ONE: goal kick struck off the ground (Ederson, LEFT) \u2014 a dead ball, confirmed as a goal-kick "
  "assist in the written record. TWO: open-play backpass struck off the ground (Van der Sar, RIGHT). "
  "THREE: drop-punt out of the hands (\u010cech LEFT, Alisson RIGHT). FOUR: overhand throw (Schmeichel, "
  "RIGHT arm). Say FOUR, not three and not five.",
 "decision":"None. Shoot it.",
 "quote":"THE LINE NOBODY ELSE HAS ON THIS PACK: every method that appears twice is SPLIT BY SIDE. The two "
  "struck off the ground split left and right \u2014 Ederson LEFT, Van der Sar RIGHT. The two drop-punts split "
  "left and right \u2014 \u010cech LEFT, Alisson RIGHT. And Schmeichel is the outlier who does not use a foot at "
  "all. That symmetry came out of a second pass and it is yours. "
  "STANDING WARNING: the compilation carries NO scorebug on any clip \u2014 no clock and no score for any of "
  "the five. Do not state a minute on camera, and do not quote a distance for any of them except "
  "Ederson's, where 85\u201386 yards comes from the written record and should be attributed as reported."
},
{
 "title":"Top 10 Pace Abuser Moments Part 2",
 "status":"READY TO SHOOT",
 "meta":"Your Pt1 5,382,421 · runs 10→6 · reference jxz2A7GHTGM is your own Part 1",
 "verdict":"No duplicates with Part 1. And one thing fell out of counting that gives you a line nobody else has.",
 "picks":[
  ("10","Son Heung-min — the Burnley solo goal",
   "278 likes, the top named request on Part 1 — and the only goal in either pack that won a trophy.",
   ["C-CefuZ6h1k — Tottenham official, ALL TEN ANGLES"],
   "*** THE LINE THE PACK WAS MISSING: THIS GOAL WON THE FIFA PUSKAS AWARD *** — at The Best FIFA "
   "Football Awards 2020. The source video is literally Tottenham's own Puskas package. No other run in "
   "either Pace Abuser pack carries an official award, and it costs you nothing to say. "
   "Tottenham Hotspur Stadium, 7 December 2019, Spurs won 5-0. "
   "EVERY TOUCH WITH HIS RIGHT FOOT. Picks it up 12–15 yards outside HIS OWN box, about 85 yards out. "
   "He SCANS EARLY — head left, then right — reads both lanes as covered, drops his head and goes. "
   "LOWTON (2) lunges and is bypassed · BRADY (12) squeezes in, cannot match him and VISIBLY GIVES UP · "
   "MEE (6) and TARKOWSKI (5) both retreat and converge at the top of the D and he goes BETWEEN THEM "
   "before either commits. Finishes right foot, inside/instep, low into the bottom right from ~13 yards. "
   "CUT ON: ten angles here, and the one that matters is the ULTRA SLOW-MOTION HEAD-ON at 02:40–03:19 — "
   "the only angle that shows the feet well enough to carry the one-footed point. "
   "[!!] DO NOT QUOTE A TOUCH COUNT. Three passes returned 9, 10 and 11–12. The NUMBER is unstable; the "
   "FOOT is not — a tie-breaker graded all eight visible touches RIGHT and CERTAIN, zero left-foot "
   "contacts. Say \u201cevery touch with his right\u201d. "
   "[!] NO SCOREBUG and NO SPEED GRAPHIC anywhere — do not quote a distance or a top speed. "
   "[!] MASK the \u201cCLICK TO SUBSCRIBE\u201d panel at 00:21–00:35 and the end card at 03:20."),
  ("9","Terens Puhiri — Borneo FC v Mitra Kukar",
   "OG_Clips ranks him #2 in a 14.6M video, above Mbappé and Bale.",
   ["kjdKZOcXlbk — Guardian Football, 7.8M views"],
   "THREE TOUCHES, ALL RIGHT-FOOTED. Number 28. Starts ~10 metres behind the halfway line off a charged-down "
   "shot. Outside of the right into space; outside of the right past the onrushing keeper's slide, reaching "
   "it A FRACTION AHEAD; then HURDLES THE GROUNDED KEEPER without breaking stride and slots it from 7 yards. "
   "Athletics running track round the pitch, floodlights, wet-looking turf. "
   "COMMENTARY (Indonesian): “GOOOOOL! Gol, gol, gol, gol, gol... MAMAYOOO!” "
   "CUT ON: the close-up of the Mitra Kukar keeper bowing his head at the turf."),
  ("8","Micky van de Ven — Spurs v Copenhagen",
   "Requested three times, and he is the cold open of your own Die for the Badge.",
   ["h_stLgq5Rps — Tottenham official, 01:04–01:23"],
   "FIVE TOUCHES, EVERY ONE LEFT-FOOTED, AND NOBODY LAYS A FINGER ON HIM. Starts 25–30 yards off his own "
   "goal line. Touch 3 SPLITS TWO RETREATING DEFENDERS and neither of them even lunges. Finishes left-footed "
   "from 12–14 yards into the bottom corner. ONE UNBROKEN WIDE PAN, no replays at all. Cups his LEFT HAND "
   "TO HIS EAR and knee-slides. COMMENTARY: “and off goes Van de Ven! Micky van de Ven! GOING ALL THE WAY!” "
   "[!] A gameplay flag was raised on this and it is wrong — official club channel, no UI on screen."),
  ("7","Karim Adeyemi — Dortmund v Chelsea",
   "OG_Clips #7. Rounds Kepa and it ends in a goal.",
   ["nPZGlV1rBM4 — DAZN, dedicated to the run"],
   "FIVE TOUCHES, EVERY ONE LEFT-FOOTED. Number 27. It starts from A CHELSEA CORNER — Guerreiro hooks the "
   "second ball clear and Adeyemi takes it on the run 10 yards inside his OWN half. ENZO FERNÁNDEZ (5) IS "
   "THE ONLY CHELSEA PLAYER BACK, backpedals, jockeys, tries to force him outside, and is simply gone. "
   "Rounds Kepa with the OUTSIDE of the left and finishes with the inside from 5 yards. Clock 62:20→62:45, "
   "DOR 0-0 → 1-0. FULL BACKFLIP at the corner flag. "
   "COMMENTARY: “Nimmt genau die Schnellstraße!” (takes the fast lane) and then, gold: "
   "“wir haben hier die Bierdusche bekommen, aber hey, nehmen wir mit!” (we just got a beer shower up "
   "here — but hey, we'll take it)."),
  ("6","Gareth Bale v Maicon — Spurs 3-1 Inter, White Hart Lane",
   "43 likes across three comments calling it the real number one.",
   ["JOirPSqL28w — TNT Sports, 86s, four separate runs"],
   "[!] BALE DOES NOT SCORE IN THIS FOOTAGE. Two assists for Crouch and Pavlyuchenko, one disallowed, one "
   "miss. The hat-trick is the OTHER match, the 4-3 at the San Siro — do not mix them. "
   "BALE IS 3, MAICON IS 13, read off the shirts. FOUR runs: Crouch misses · Crouch scores · disallowed, "
   "and here MAICON GRABS BALE'S SHOULDER AND ARM TO PULL HIM BACK and Bale breaks through it · "
   "Pavlyuchenko finishes. Maicon DECELERATES AND GIVES UP on the second one before the cross even comes in. "
   "COMMENTARY: “Maicon must be fed up of Gareth Bale already” and “Switches on the afterburners”."),
 ],
 "warn":"SOFT FLAG: Bale is also your Part 1's #3 (v Barcelona, Bartra, the technical-area run). Different "
  "match, different opponent, different competition. Say “the other Bale one” on camera and it is a "
  "feature rather than a repeat.",
 "decision":"None. Shoot it.",
 "quote":"THE LINE NOBODY ELSE HAS: every single one of these runs is ONE-FOOTED. Son every touch right. "
  "Puhiri three, all right. Van de Ven five, all left. Adeyemi five, all left. At full sprint nobody "
  "switches feet. That came out of counting, and it is a genuinely original observation for this format. "
  "[!] SAY THE FOOT, NOT THE NUMBER. Repeat passes over the same footage returned different touch TOTALS "
  "every time, but never once disagreed about which foot. The observation is safe; the arithmetic is not.",
},
{
 "title":"Top 5 Players Who Deserve The Oscar Award Part 2",
 "status":"READY TO SHOOT",
 "meta":"Your Pt1 2,987,542 · 1,825 comments · no Part 2 exists · reference uJEw4mhEYW8 is your own Pt1",
 "verdict":"The hole at #2 is filled with something much better than a second dive, and #3 turns out to be "
  "the biggest story in the batch.",
 "picks":[
  ("5","Neymar rolling — Mexico, 2018",
   "Spawned a worldwide challenge and reads in a second.",
   ["9qjGKKitwXo — use ONLY 01:46–02:19"],
   "[!!] THE MEME IS WRONG. HE ROLLS ONCE. He drops on his back, twists over once, and writhes IN PLACE, "
   "travelling almost no distance. Every clip showing more is edited — one loops it, this one scrubs a "
   "zoomed replay forwards and backwards inside a red circle from 02:20. USE ONLY UP TO 02:19. "
   "WHAT IS REAL: he had TRAPPED THE BALL BETWEEN HIS OWN SHINS to waste time, and Layún (7) then PUT HIS "
   "RIGHT BOOT ON HIS ANKLE AND LEANED ON IT while picking the ball up. Tite reacts furiously on the "
   "touchline; two medics come on. BRASIL 1 – 0 MÉXICO, 2T 25:21. NO CARD is shown. "
   "[!] FIFA omit this from BOTH their 2-minute and 11-minute cuts. There is no official source."),
  ("4","Micah Richards — Aston Villa v Stoke",
   "Requested twice. He is a pundit, so the clip travels.",
   ["RscP6Vaghd4 — CBS Sports Golazo: the dive AND the studio"],
   "THE PERFECT SOURCE — it is the clip and the punditry in one. RICHARDS 4, claret and sky blue. Wollscheid "
   "26 for Stoke. NO VISIBLE TRIPPING CONTACT: he launches himself HORIZONTAL AND PARALLEL TO THE GROUND at "
   "WAIST-TO-CHEST HEIGHT in a Superman posture, both legs kicking up behind him, flies TWO TO THREE METRES "
   "and lands chest-first. THE STUDIO IS THE ENTRY: Carragher — “What are you doing?!” · “Look where his "
   "boots are!” · “Look at him swimming!” Henry — “He landed on his lips!” · “Freeze! Why so high?!” · "
   "“I think that's my cue to leave.” Richards covers his face with his papers and leans all the way back."),
  ("3","Breel Embolo — Switzerland v Argentina, World Cup 2026",
   "A red card for simulation at a World Cup quarter-final — and then the lawmakers overruled it.",
   ["1O-qw6iaLOk — real moving footage, three slow-motion angles"],
   "VERIFIED IN TEXT, not just footage. 72nd minute. Pinheiro books PAREDES for the challenge; VAR "
   "intervenes; Paredes' yellow is RESCINDED and Embolo gets a second yellow and goes. Argentina win 3-1 "
   "in extra time with the extra man. "
   "THE FOOTAGE: the reverse sideline angle at 00:38 shows him ALREADY HORIZONTAL AND AIRBORNE BEFORE ANY "
   "CONTACT, then sticking his trailing right leg out to find Paredes' leg. The only contact is contact he "
   "initiates, from mid-air. Narrator: “Não foi absolutamente nada!” "
   "[!] He is stunned, NOT crying — one upload's title says crying and the footage does not support it."),
  ("2","Luis Suárez — the Chiellini bite, 2014 World Cup",
   "He bites a man and then goes down holding his own teeth.",
   ["1tVdCQaH0vs — ESPN broadcast, unedited"],
   "THE HOLE IS FILLED, AND IT IS NOT A DIVE. He drives his mouth into the back of Chiellini's LEFT SHOULDER, "
   "then drops and IMMEDIATELY PUTS BOTH HANDS TO HIS FACE — at 00:11 he is sitting hunched over CUPPING HIS "
   "MOUTH AND CLASPING HIS UPPER FRONT TEETH, as if his mouth were the injured thing. At 01:07 he stands and "
   "PULLS HIS COLLAR OVER HIS MOUTH AND NOSE. Chiellini YANKS HIS SHIRT OFF HIS SHOULDER to show the referee. "
   "THE REFEREE GIVES NOTHING and waves play on. ITA 0-0 URU, 78:25, sub-bar “ITALY: PLAYING WITH 10 MEN”. "
   "CANNOT BE CONFUSED with Part 1's throat-clutch against PSG. "
   "COMMENTARY: “It looks to me, dare I say it, that he's had a little bite at Chiellini.” / “Surely not again.”"),
  ("1","Rivaldo, 2002 v Turkey",
   "Ünsal sent off, FIFA fined him. The consensus GOAT of play-acting.",
   ["OiW0IPrv1Ro — 25s, 2.55M views"],
   "THE WHOLE JOKE IS ONE BODY PART AND THE REPLAY PROVES IT TWICE. He is in the corner arc waiting to take "
   "a corner, hands on thighs. The ball is driven along the turf at him and STRIKES HIM SQUARELY ON THE "
   "UPPER RIGHT LEG — THIGH AND KNEE. ZERO contact with torso, chest, neck, head or face. He throws both "
   "hands to his FACE and flips BACKWARD over his shoulders, curling up against the hoardings. Red card "
   "raised at 00:13. TWO separate slow-motion replays show the leg contact. "
   "Boards: FIFAworldcup.com · AVAYA · JVC · Budweiser · Yahoo! · PHILIPS · Gillette. "
   "NO COMMENTARY — the publisher replaced it with a breakbeat track."),
 ],
 "warn":"Neymar's source is partly manipulated and Rivaldo's has no original audio. Both are still the best "
  "available — FIFA has no clean cut of either.",
 "decision":"ORDERING: Embolo is underweighted at #3. He is the only entry where the dive is punished on the "
  "pitch, at a World Cup, by VAR — and then, three weeks later, IFAB said the VAR had no right to review it "
  "at all. Nobody ranking dives has that ending. I suggested EMBOLO TO #4, RICHARDS TO #3. YOUR CALL, 20 Sep: "
  "keep the approved order — so Embolo stays at #3 and the IFAB ending is the script's job, not the ranking's.",
 "quote":"THE IFAB RULING, VERBATIM, AND IT IS THE BEST PAYOFF IN THE BATCH: “A yellow card (caution) which "
  "is not a second yellow card can only be reviewed to identify the player who committed the offence that "
  "was penalised; the offence itself cannot be reviewed/changed.” FIFA pushed back, saying its reading of "
  "mistaken identity “restored justice”. A man was sent off for diving at a World Cup and the lawmakers of "
  "the game then said the red card should never have existed.",
},
]

READY += [
{
 "title":"Top 5 Die for the Badge (2026 Redo)",
 "status":"READY",
 "meta":"Your Pt1 3,072,000+ · six existing versions of this concept · reference WBDNj2kL0lw is your own Pt1 · STONES KEPT, YOUR CALL",
 "verdict":"All five described from official sources with commentary. Stones is your Part 1's #2 at the same rank "
  "and you chose to keep him — frame it on camera rather than hide it.",
 "picks":[
  ("5","Valverde on Morata — Supercopa final, extra time",
   "A deliberate red card to stop a certain goal, and the opposing manager acknowledges it.",
   ["3JiwVYCnHqU — 00:02–00:04, match clock 114:29",
    "ll1VeD5lCzg — Real Madrid official",
    "SHOLzR2mRQM — Guardian, Valverde apologises"],
   "RMA 0-0 ATM on the Supercopa scorebug, clock 114:29–114:30, Italian network NOVE. The foul is 2–3 "
   "METRES OUTSIDE THE TOP OF THE D — not in the box. Valverde makes NO CONTACT WITH THE BALL and no "
   "attempt to play it; his EYES STAY ON MORATA'S LEGS and he sweeps the calves and ankles from behind. "
   "Straight red. CUT ON: the tight ground-level side profile at 00:59 — it proves the intent. "
   "THE BEAT NOBODY USES: at 01:11, as Valverde walks off, DIEGO SIMEONE REACHES OUT AND PATS HIM ON THE "
   "BACK OF THE HEAD. Morata has a visible abrasion on the left of his forehead at 01:45."),
  ("4","Van de Ven — Europa League final, Bilbao",
   "Not a hook. A full backwards overhead kick at crossbar height.",
   ["vWC-USe1ncI — Tottenham official, live at 00:39, clock 67:31"],
   "TOT 1 – 0 MUN, 67:31. Bruno Fernandes swings an inswinging free kick in; VICARIO COMES AND IS WIPED OUT "
   "BY HIS OWN PLAYER, SOLANKE, in mid-air; the ball loops toward the empty net. Van de Ven backpedals and "
   "THROWS HIMSELF HORIZONTALLY INTO A BACKWARDS SCISSOR KICK, right leg swinging along the plane of the "
   "goal line, boot meeting it AT CROSSBAR HEIGHT DIRECTLY ABOVE THE WHITE LINE. Then Yoro shoots, Romero "
   "blocks with his body, Bissouma clears — three stops in four seconds. "
   "CUT ON: the ULTRA-SLOW-MOTION CAMERA INSIDE THE NET at 01:04. "
   "COMMENTARY: “As soon as the goalkeeper comes to the six-yard line, Micky van de Ven is coming round on "
   "the cover... That is magnificent. THAT MIGHT WELL BE A MATCH-WINNING CLEARANCE.”"),
  ("3","Süle — DORTMUND, not Bayern — denying Mbappé",
   "The correction is part of the entry. He is at Dortmund and the man he denies is Mbappé.",
   ["vjTC2gCMtqM — DAZN, live at 00:13, clock 16:34"],
   "DOR 0-0 PAR, 16:34. SÜLE IS 25, read off the back at 01:04. MBAPPÉ'S 7 read off the front of his "
   "shorts. Mbappé rounds Kobel (coral orange, “KOBEL 1”) and shoots with the inside of the right from 8 "
   "yards at an open net. Süle drops into a FULL-LENGTH SLIDE ON HIS LEFT HIP, right leg extended "
   "HORIZONTALLY HIGH OFF THE TURF, and LIFTS IT OVER THE BAR for a corner. "
   "THE REACTIONS ARE THE EDIT: Süle roars, KOBEL HUGS HIM, Hummels joins — and MBAPPÉ TURNS, PULLS AT "
   "HIS COLLAR AND SMILES IN DISBELIEF. "
   "COMMENTARY (German), four usable lines: “der größtmögliche Grätsch-Moment!” · “Mit einer "
   "Monster-Grätsche rettet er hier.” · “Was für eine Rettungstat!”"),
  ("2","[OK] KEPT — John Stones, your call, and now fully described",
   "Your Part 1's #2 at the same rank. You are running it knowingly.",
   ["MriNd_wn1Os — Man City OFFICIAL, City 2-1 Liverpool, clearance at 00:55–01:40",
    "Part 1's #2 is John Stones, Man City v Liverpool"],
   "FRAME IT, DON'T HIDE IT: say \u201cyou've seen this one before, and it's still the best example "
   "there is\u201d in the first breath. The audience that spots repeats is the same one that rewards "
   "being told. "
   "[!!] THE NUMBER: your Part 1 says 11.7mm and an earlier note here said 11.2mm. BOTH WRONG. "
   "Manchester City's own site says \u201c11 MILLIMETRES of the ball had not crossed\u201d and Sky Sports' "
   "headline says \u201c11mm decided the 2018-19 title race\u201d. SAY ELEVEN, and put NO DECIMAL on screen. "
   "[!] The figure appears NOWHERE in the footage — the Goal Decision System graphic shows only the "
   "words NO GOAL before cutting away, so any number on screen is one you added. "
   "[!!] SEQUENCE CORRECTED: it is NOT \u201cEderson's clearance rebounds off him\u201d. Man\u00e9 hits the "
   "INSIDE OF THE POST, STONES swings to clear and the ball SMASHES INTO EDERSON diving backwards, and "
   "comes off him towards the empty net. Stones then dives across and hooks it off the line with the "
   "INSTEP OF THE RIGHT boot, inches ahead of Salah \u2014 and then gets up and clears the SECOND ball "
   "as Salah tries again. He makes the save twice, which nobody mentions. "
   "STONES IS 5, read off his back and his shorts. CUT ON: the low reverse from behind the net at "
   "01:26\u201301:32 \u2014 the only angle showing the hook across Salah with the ball on the line. "
   "COMMENTARY: \u201cand then Stones, tremendous save off the line... and that's cleared right off the "
   "line.\u201d"),
  ("1","FERLAND Mendy — Real Madrid v Man City, CL semi",
   "Not Édouard. The comment was right and the first reading of it was wrong.",
   ["WgzZRA260X0 — TNT Sports, 00:15, match clock 86:11",
    "PaaZxPh0A-o — also in Legendary Goal Line Saves"],
   "RMA 0 – 1 MCI, aggregate (3-5), clock 86:11, BT SPORT 2 LIVE. Zinchenko releases GREALISH, who rounds "
   "Courtois and shoots with his LEFT foot at the open net. FERLAND MENDY (23) sprints DIAGONALLY BACKWARD "
   "from the left edge of the six-yard box and HOOKS IT AWAY WITH HIS LEFT FOOT right on the white line. "
   "ONE UNBROKEN LIVE SHOT covers the whole counter — there is no isolated replay and no goal-line graphic. "
   "COMMENTARY: “It's Grealish! It's off the line! It's only just off the line!” then McManaman: "
   "“I don't know what happened there. What... what did Courtois... was he diving out the way? "
   "Grealish really just had a tap-in.”"),
 ],
 "warn":"Confetti and white paper litter is visible on the Bernabéu turf in the Mendy clip — worth knowing "
  "if you are colour-matching shots.",
 "decision":"SETTLED — YOUR CALL, 20 Sep: keep Stones anyway. Described in full (badge-2-stones.md). Kyle Walker "
  "stays in the subs line if you ever change your mind.",
 "quote":"",
},
{
 "title":"Worst Penalty Miss With Every Technique Part 2",
 "status":"READY",
 "meta":"Your Pt1 2,210,074 · Pt1 labels: Powershot · Sidefoot · Pass · Panenka · Stutter · SETTLED: Budimir replaces Tah",
 "verdict":"All five described. Budimir is in at #2 (your call, B) and Pires & Henry are kept at #4 (your call). "
  "Eze's OUTCOME is disputed between the written record and the footage — say ‘he missed’, which nobody contests.",
 "picks":[
  ("5","Zaza — STUTTER — Euro 2016 shootout",
   "The most famous run-up in football.",
   ["5_9OwlwAMMk — 00:14–00:23, Stade de Bordeaux"],
   "NUMBER 7 read off the chest and the left leg of the shorts. Starts 4–5 METRES BEHIND THE TOP OF THE D. "
   "APPROXIMATELY 16–18 rapid choppy micro-steps — previously logged as about fourteen, two passes now put "
   "it higher, so say ‘about sixteen’ and never a hard number. Torso rigid and upright, bouncing "
   "vertically, arms pumping, and the whole sequence covers only A COUPLE OF METRES. He does not stop; he "
   "delays, then takes 2–3 accelerating strides. Plant RIGHT, no slip. Strike LEFT foot, laces, SEVERE "
   "BACKWARD LEAN, several metres over the bar into the stands. "
   "NEUER, better than ‘waves his arms’: he REACHES BOTH ARMS UP AND TOUCHES THE CROSSBAR to look bigger, "
   "then crouches. COMMENTARY: “And he's blazed it! After an exaggerated run-up...”"),
  ("4","[OK] KEPT — Pires & Henry, your call, and the callback makes it new",
   "It IS Part 1's Pass entry. The Pass technique is genuinely scarce, and this source carries a "
   "second moment Part 1 never had.",
   ["N4bQVTczcLQ — 34s, carries BOTH the penalty and the callback",
    "Arsenal 1-0 Man City, Highbury, 22 October 2005, ~72nd minute"],
   "FRAME IT: \u201cthere is only one of these, and here it is again.\u201d "
   "*** END ON THE CALLBACK, NOT THE MISS. *** Eleven days later, v Sparta Prague in the Champions "
   "League, Henry scores, runs to the corner, and MIMES THE BOTCHED PENALTY AT PIRES \u2014 a hesitation "
   "step and an exaggerated flutter of the foot over an imaginary ball. Pires grins and they embrace "
   "laughing. Part 1 did not have this. "
   "THE CONTACT: RIGHT foot, and his STUDS SKIM THE TOP of the ball, which moves about an inch. "
   "[!] It is NOT a complete air-kick \u2014 \u201che never touched it\u201d is the popular version and it is "
   "wrong. Henry has to brake, DISTIN (5) hooks it clear, and GRAHAM POLL GIVES AN INDIRECT FREE KICK "
   "TO CITY, right arm straight up and held. "
   "PERIOD DETAIL WORTH A BEAT: Arsenal are in the REDCURRANT commemorative kit worn only for "
   "Highbury's final season. PIRES IS 7, HENRY IS 14 IN THE CAPTAIN'S ARMBAND. David James in green. "
   "Boards: JVC, Lucozade Sport, Lansen, Barclays, O2, \u201cNIKE PRO: AN ATHLETE'S SECRET WEAPON\u201d. "
   "TUNNEL INTERVIEW, same clip: \u201cTell us what happened.\u201d Henry: \u201cWhat happened? I don't know...\u201d "
   "and he ducks his head out of frame laughing. "
   "COMMENTARY: \u201cWhat's he done?!\u201d / \u201cWell, he pretended to take it and then didn't seem to take "
   "it.\u201d / \u201cAnd the referee's given a free kick the other way! What an extraordinary incident!\u201d"),
  ("3","Agüero — PANENKA — Man City v Chelsea",
   "A genuine panenka, caught one-handed by a keeper sitting on his hip.",
   ["he7mZJDIEOQ — Sky Sport DE, 01:23–01:43 — UPGRADED SOURCE",
    "_waYRzpc960 — Man City official",
    "auV6DgA5CY8 — Diario AS, Guardiola on it"],
   "SOURCE PROBLEM SOLVED — the old note said the only clip had music and no commentary. This one has full "
   "German commentary, an official PL scorebug and four angles. "
   "MCI 1 – 0 CHE, clock 47:30 +1' — FIRST-HALF STOPPAGE TIME. EMPTY STADIUM, COVID; banners read "
   "“WE'RE NOT REALLY HERE” and “COLIN BELL THE KING 1946–2021”, which dates it exactly. "
   "MENDY IS CORRECTED: he does NOT stay on his feet. He starts to commit right, ABORTS THE DIVE, SETTLES "
   "ONTO HIS RIGHT HIP AND KNEE, and CATCHES IT ONE-HANDED IN HIS RIGHT HAND above his head. "
   "AGÜERO'S EYES STAY LOCKED ON HIM THE WHOLE RUN-UP. Afterwards he rubs his nose and mouth and looks "
   "down. At 01:40, GUARDIOLA in a grey hoodie with a red ‘OPEN ARMS’ emblem crosses his arms and walks "
   "away shaking his head. CUT ON: the slow motion from inside the net at 01:34. "
   "COMMENTARY: “Agüero... sehr frech... und Mendy direkt in die Arme!” (very cheeky — and straight into "
   "Mendy's arms)."),
  ("2","Budimir — the one that NEVER LEFT THE FLOOR — Osasuna v Valencia, 97th minute",
   "He won the penalty himself, then did this. Your call: B, keep Budimir.",
   ["4EvIcyRuAXg — Arena Sport 1 broadcast, 00:00–00:38 · CUT ON 00:30–00:35"],
   "Osasuna 0-1 Valencia, El Sadar, 15 April 2024. NUMBER 17 legible on the red Osasuna shirt. He is "
   "LEFT-footed, so the RIGHT leg is the plant. Four to five paces back, hands on hips, three normal strides, "
   "then at the ball an extreme late stutter to make Mamardashvili commit first. *** THE STANDING LEG BUCKLES "
   "*** — he sees the keeper move, tries to abort the swing, the right knee sways out, his weight drops and he "
   "stumbles FORWARD OVER THE BALL. The LEFT foot flails through and catches it with the TOE. *** THE BALL "
   "NEVER LEAVES THE GRASS *** — it rolls at walking pace to the middle of the six-yard box and Mamardashvili, "
   "already down to his right, simply gathers it against his chest. SAY ‘BUCKLES’, NOT ‘SLIPS’ — no divot, no "
   "tearing, and a dedicated pass could not separate a surface slip from a loss of balance. He did it to "
   "himself. Budimir pinches the bridge of his nose; Mojica (22) grabs his head; ARRASATE stands on the "
   "touchline hands in pockets, then sits slumped with his chin on his fist — that is your closing frame. "
   "COMMENTARY (Serbian): “Nije ni šutnuo!” — “He didn't even take a shot!” "
   "OVERLAY: mask the rotating betting graphics bottom left throughout."),
  ("1","Eze — SIDEFOOT — missed, and the exact destination is DISPUTED",
   "Not the crossbar. Beyond that, the record and the footage disagree.",
   ["ygcv9fQheII — ARSENAL'S OWN OFFICIAL CHANNEL, 01:22–01:27 (shootout starts 01:12)"],
   "[!!] TWO vision passes said ‘underside of the crossbar’ and both were wrong: no source has him touching "
   "the frame. Beyond that the sources SPLIT. Wikipedia's match record says he SHOT WIDE LEFT. THREE vision "
   "passes on Arsenal's own footage say OVER THE BAR. TNT's live commentary says only that he ‘missed’. Both "
   "readings agree he went LEFT and missed the target; they disagree on bar or post. I am not settling it. "
   "SAFE SCRIPT WORDING: “he missed” — nobody contests that. Do NOT say crossbar, and do not say ‘wide left’ "
   "or ‘over the bar’ as fact. "
   "THE TECHNIQUE IS YOUR CALL AND IT STANDS: side-foot. No source anywhere has a slow-motion replay of the "
   "contact, so the footage cannot overrule you. "
   "KNOCK-ON TO CHECK IF IT WAS OVER THE BAR: Zaza (#5) also ends over the bar, and that would be the same "
   "duplicated mechanism removing Tah was meant to fix. If you can confirm from a full replay, tell me and I "
   "will re-check variety. "
   "SCOREBUG: PENALTIES / PSG 2 / ARS 1. “EZE” above 10, “VISIT RWANDA” on the lower back. "
   "COMMENTARY: “Eberechi Eze...” then “...misses!” "
   "ONE SCRIPT CHANGE: stop saying crossbar."),
 ],
 "warn":"[!] Keep GABRIEL as a sub, not a pick — he goes over the bar, which duplicates Zaza. "
  "[!] A REAL SIMULATION FOUND WHILE CHECKING: ZDF sportstudio's PSG–Arsenal video (PTs-3jmCQY8) is a "
  "PlayStation sim — the PS5 LOGO SITS DIRECTLY UNDER THE SCORELINE at 00:20. A real broadcaster publishing "
  "simulated content. Avoid it, and note the tell.",
 "decision":"SETTLED, both of them. #4: you said keep Pires & Henry. #2: you said B — keep Budimir, so Powershot "
  "goes uncovered and Tah drops to subs. Nothing on this pack is waiting on you.",
 "quote":"THE FULL SHOOTOUT, from the written record — use this and not any vision read: "
  "Gonçalo Ramos scored · GYÖKERES scored · Doué scored · EZE MISSED (record: wide left; footage: over the bar — disputed) · Nuno Mendes SAVED by Raya · "
  "Rice scored · Hakimi scored · Martinelli scored · Beraldo scored · GABRIEL OVER THE BAR. PSG win 4-3.",
},
{
 "title":"When Goalkeepers Make Accidental Saves",
 "status":"ALL FIVE DESCRIBED",
 "meta":"Reference ZbunM6UKwts is a SantaBall competitor video that ran 6→2",
 "verdict":"The three that had no standalone footage anywhere are now described in full from the reference "
  "itself, and two of them picked up real identifying evidence in the process.",
 "picks":[
  ("5","Full Reverse Save — the scorpion heel",
   "Reference's #6. No standalone clip exists anywhere.",
   ["ZbunM6UKwts — reference only"],
   "CORRECTED FROM THE EARLIER READ: the attacker CHIPS it, he does not cross it low. The keeper dives low "
   "and horizontally to his RIGHT and misses completely; the ball FLOATS OVER HIS PRONE BODY. He lands flat "
   "on his stomach, HEAD FACING THE TURF, blind. BOTH LEGS WHIP UP BEHIND HIM in an inverted scorpion and "
   "the BACK OF THE RIGHT HEEL catches the UNDERSIDE of the descending ball at waist-to-chest height, "
   "looping it over the bar. Blue and amber stripes, #20 on the SHORTS. Boards: The Wrekin Housing Trust · "
   "Sky BET · GTE · MORR... CUT ON: the ultra-tight slow motion at 00:04."),
  ("4","No-Look Save — facing his own net",
   "Reference's #5. AND THIS ONE IS NOW IDENTIFIABLE.",
   ["ZbunM6UKwts at 00:07–00:13"],
   "*** BREAKTHROUGH: the boards read ‘Prifysgol Abertawe’ and ‘Swansea University’ with a Welsh flag, and "
   "the away team has a NAME ON THE SHIRT — ‘SCOTT’ above number 36. Home side all white, away in red, "
   "home keeper in ROYAL BLUE wearing 33 with LIGHT CYAN BOOTS. That is findable now. *** "
   "THE MECHANIC: he is ON HIS HANDS AND KNEES FACING HIS OWN NETTING, back to play. The low shot hits him "
   "square on the LOWER BACK AND RIGHT BUTTOCK while his eyes are pointed into the back of his own goal. "
   "CUT ON: the ground-level replay from behind the endline at 00:09. "
   "AUDIO: a real crowd ‘Ooooh!’ at the moment of contact."),
  ("3","IDK Save — straight in the face",
   "Reference's #4. And it is not what the pack said it was.",
   ["ZbunM6UKwts at 00:14–00:22"],
   "IT IS A PENALTY REBOUND. The penalty hits the base of the right post; the keeper is prone across the "
   "line; the rebound runs to an unmarked attacker 5–6 yards out who side-foots it at the open net — and "
   "it HITS THE KEEPER FLUSH IN THE FACE while he scrambles backward on his hands and knees. Arms spread, "
   "NO hand movement toward the ball at all. It loops over the bar. "
   "THE BRAZIL ATTRIBUTION IS NOW EVIDENCED: boards read BENOIT · NET HDTV · SUBWAY · Claro-hdtv · FATAL · "
   "Claro-4G. Packed standing terrace, white building with blue window frames behind. "
   "CUT ON: the low angle behind the net at 00:17."),
  ("2","Manuel Neuer v Bas Dost — the heel he cannot see",
   "Confirmed by the commentary itself, no inference needed.",
   ["PaaZxPh0A-o — 02:00–02:08"],
   "“Oh, Bas Dost! Bas Dost lucky... He should have buried it!” — the commentary names him for you. "
   "Dost chips Neuer with his right; Neuer dives left onto his chest and it loops over him; sliding forward "
   "with his head facing AWAY from goal he FLICKS HIS RIGHT LEG UP AND BACKWARD and the heel catches it "
   "EXACTLY ON THE CHALK. EMPTY STADIUM — a board reads “THANK YOU, HEALTHCARE HEROES”, which dates it to "
   "the 2020 restart. Neuer in teal with TEAL BOOTS. "
   "CUT ON: the slow-motion goal-line close-up at 02:04 through the net — the Derbystar ball on the white "
   "line with his boot heel coming down on it."),
  ("1","Choupo-Moting stops his own team scoring",
   "PSG v Strasbourg. The closer, and the commentary writes the caption.",
   ["PaaZxPh0A-o — 05:05–05:19"],
   "“#17 CHOUPO-MOTING” and “#24 NKUNKU” both read off the backs. Nkunku chips Matz Sels (orange) toward "
   "the empty net; Choupo-Moting is sprinting along the goal line toward the left post FACING SIDEWAYS, "
   "extends his LEFT FOOT and STOPS IT DEAD ON THE WHITE LINE, off the base of the upright and back out. "
   "THE BEST FRAME IN THE PACK: at 05:09 the broadcast CUTS TO THE PSG BENCH AND KYLIAN MBAPPÉ, wide-eyed "
   "and open-mouthed. "
   "COMMENTARY: “oh Choupo-Moting has hit the post from an inch out!” / “He's kept it out, Jonathan! "
   "HE'S BLOCKED IT ON THE LINE FROM HIS OWN PLAYER!” "
   "[!] The compilation splices a meme clip of a fan punching a TV at 05:16 — not broadcast, do not use it."),
 ],
 "warn":"[!] THE STANDING WEAKNESS, WHICH YOU ACCEPTED KNOWINGLY: the title promises goalkeepers and #1 is a "
  "striker. Zlatan, Bendtner and the Liga MX referee in the subs are the same issue. The footage is not the "
  "problem here; the title promise is. Worth one line on camera to get ahead of it.",
 "decision":"None outstanding. Optional: chase the Swansea lead to put a name on #4.",
 "quote":"WHY THIS PREMISE FIGHTS YOU, for the next time: goalkeeper is one of your strongest lanes — 2.34M, "
  "2.28M, 1.16M, 949k, 664k — and every winner is about a keeper being CLEVER. ‘Accidental’ removes the "
  "agency that makes the lane work, and famous accidental blocks are nearly all by outfield players, which "
  "is exactly why the goalkeeper ones are obscure.",
},
{
 "title":"Top 5 Shortest Lived Primes (2026 Redo)",
 "status":"READY — TYPE B, NO CLIPS NEEDED",
 "meta":"Your Pt1 1,967,544 · 2,230 comments · reference 9aYJ3lBf7HY is your own Part 1",
 "verdict":"Zero overlap with Part 1, and Part 1 contains two factual errors you can correct on camera.",
 "picks":[
  ("5","João Félix","2,800 likes — most expensive teenager ever, Saudi league at 26.",[],""),
  ("4","Dele Alli","2,357 — two PFA Young Player awards, then out of football.",[],""),
  ("3","Andrey Arshavin","1,365 — four goals at Anfield, then gone.",[],""),
  ("2","Michu","One season: eighteen in the Premier League, twenty-two in all competitions, then an ankle that never recovered.",
   ["Wikipedia — Michu: 22 in all competitions in 2012–13, 18 in the league; retired 25 July 2017 aged 31 over the right ankle"],""),
  ("1","Marco van Basten","Retired at 28 through injury, three Ballons d'Or.",[],""),
 ],
 "warn":"Part 1's five were Owen, Torres, Pato, Adriano and Ronaldinho. None of your five collides.",
 "decision":"None. Shoot it.",
 "quote":"TWO ERRORS IN YOUR OWN PART 1, AND CORRECTING THEM ON CAMERA IS THE STRONGEST REDO HOOK YOU HAVE: "
  "the Torres caption says £80 MILLION and the fee was around £50m, and the voiceover calls Ronaldinho a "
  "two-time Ballon d'Or winner — he won ONE, in 2005. He won FIFA World Player twice, which is the confusion.",
},
{
 "title":"Players Who Could've Played For Another Nation",
 "status":"READY — TYPE B, NO CLIPS NEEDED",
 "meta":"Reference 0zxkpSnyZJs, watermark ‘yanedits’, 29s, NO VOICEOVER AT ALL",
 "verdict":"Four of five are fresh. The fifth is a differentiator rather than a duplicate. And the reference "
  "hands you your edge on a plate.",
 "picks":[
  ("5","Bukayo Saka — NIGERIA","Parents from Ibadan.",[],""),
  ("4","Michael Olise — ENGLAND","Born in Hammersmith and capped by England youth before choosing France.",[],""),
  ("3","Alphonso Davies — LIBERIA","Born in a Ghanaian refugee camp to Liberian parents.",[],""),
  ("2","Kylian Mbappé — ALGERIA",
   "The reference sends him to Cameroon. Both are true and Algeria is the one people miss.",[],
   "SOFT FLAG: Mbappé is the reference's lead entry too — but it uses his father's Cameroonian side and you "
   "are using his mother Fayza Lamari's Kabyle side. Say ‘everyone says Cameroon’ and it becomes the hook."),
  ("1","Lionel Messi — SPAIN","Held Spanish citizenship and turned down a Spain U20 call-up.",[],""),
 ],
 "warn":"The reference's format is a top bar of five face icons that flip to flags, plus a PHOTOSHOPPED "
  "COMPOSITE of each player in the other nation's kit. You will need to make those composites.",
 "decision":"None. Shoot it.",
 "quote":"YOUR EDGE, AND IT IS ENORMOUS: the reference STATES NO BASIS FOR A SINGLE ONE. No voiceover, no "
  "text, nothing explaining why any of them was eligible. It is five flags and five photoshops over phonk. "
  "You voice yours — say the specific link out loud on every entry and it is a different video, not a "
  "better-looking copy of the same one.",
},
]

# blocked: (title, severity, what, why, fix)
BLOCKED = [
 ("Transfers That Almost Happened","COMPLETE \u2014 SHAPE IS THE ONLY OPEN QUESTION",
  "The reference is not a top-five. It is one 69-second story about ONE transfer — Toni Kroos to "
  "Manchester United — with no rank numbers and no list at all. The title is plural; the video is singular.",
  "Your version is five transfers. None is Kroos, so there is no duplicate — the problem is structural. "
  "Five picks in sixty seconds is twelve seconds each, and twelve seconds cannot carry ‘Moyes flew to "
  "Munich and sat on his couch’. The reference works BECAUSE it spends the whole runtime on one story "
  "with a reversal in it.",
  "OPTION A, my recommendation: one transfer per video, about seventy seconds, full arc. De Gea and the "
  "fax first — it is the strongest single story of the five and the most famous. The other four become "
  "their own uploads, which turns one pack into a five-video series with no extra research. "
  "OPTION B: keep the top-five, but then it is your format and not the reference's, and you need different "
  "proof that a five-pick version travels. "
  "WORTH STEALING EITHER WAY: real news-article screenshots used as evidence beats, punctuated by meme "
  "reaction cutaways. Fact, fact, reaction."),

 ("Players We Always Forget Played for That Club","COMPLETE \u2014 SHOOT KNOWING THERE IS NO PRECEDENT",
  "The reference GT-1mKJRDxU is YOUR OWN ‘Players We Always Call By Their Full Name’, 3,240,079 views. "
  "It is about names you can only say in full — Nuno Mendes, Luis Diaz, Rafael Leao, ‘Toni Krease’, "
  "‘2. Cristiano Rolando’. Nothing to do with forgetting a club. That one link is logged against SEVEN "
  "separate ideas in the queue.",
  "One video proving a LANE is not one video proving a TITLE. Full Name runs on a specific mechanic — the "
  "name is unsayable in halves and the viewer tests it in their own head. Forget-Played-For runs on "
  "surprise. Different engines, one inherited proof. "
  "(Correction on the record: I first wrote this was another creator's video. It is yours, and Part 2 "
  "exists too at 449,749 views.)",
  "The picks themselves are good — Pirlo at Inter, Robben at Chelsea, De Bruyne at Chelsea, Henry at "
  "Juventus, Lampard at City. Shoot it if you want, but log it as riding lane proof rather than believing "
  "it has a precedent. One caution: Full Name Part 2 did 0.14× its parent. This lane's flagship did not "
  "carry its own sequel."),

 ("Players We Always Mispronounce","READY — THREE SLOTS FILLED",
  "Picks now read: #5 Khvicha Kvaratskhelia \u00b7 #4 C\u00e9sar Azpilicueta \u00b7 #3 Wojciech Szcz\u0119sny \u00b7 "
  "#2 Thierry Henry \u00b7 #1 Mesut \u00d6zil.",
  "YOUR CALL: fill them for me. Done. Every pronunciation is sourced rather than written from memory, "
  "because in a pronunciation video the pronunciation IS the product. \u00d6zil's two IPA renderings come "
  "from Wikipedia's own transcription; Szcz\u0119sny's from a published list of names people get wrong; "
  "Azpilicueta's \u201cDave\u201d story is told on CHELSEA'S OFFICIAL SITE; Kvaratskhelia's from Babbel's "
  "Euros guide, which had to supply audio because writing it out did not work. "
  "#4 AZPILICUETA is the most engaging entry and it is barely about phonetics \u2014 nobody could say it, "
  "so Chelsea fans and teammates called him DAVE for a decade, in songs, to his face. A Premier League "
  "captain got a new name because of a pronunciation. "
  "#1 \u00d6ZIL is the hard declarative finisher because there are TWO right answers: German "
  "\u201cMAY-zoot UR-zil\u201d and Turkish \u201cmeh-SOOT ur-ZEEL\u201d \u2014 different stress in both words, both "
  "correct, because he was born in Germany to a Turkish family. Most people never landed either.",
  "CHECKED AGAINST FULL NAME PT1 (Nuno Mendes, Luis D\u00edaz, Rafael Le\u00e3o, Kroos, Ronaldo): no collision "
  "on any of the five, and the mechanic differs \u2014 Full Name is names you can only say whole, this is "
  "names you say wrong. [!] The Krease/Rolando evidence remains void: that is your own caption bait. "
  "[!] Lane caveat unchanged \u2014 the reference is your own Full Name Pt1, which proves the lane, not "
  "this title. Subs: Lamine Yamal (321), R\u00faben Dias (17), Sokratis, G\u00fcndo\u011fan."),

 ("Players We Always Blame First","COMPLETE \u2014 SHOOT KNOWING THE FOOTBALL VERSION HAS BEEN FLAT",
  "Same reference again. Blame First runs on grievance; Full Name runs on a name test.",
  "Five strong picks sourced from your own comments — Beckham 1998, Saka Euro 2020, Terry 2008, Baggio "
  "1994, Karius 2018 — but no viral precedent for this specific format.",
  "Shoot it knowingly as lane-proof, or find a real reference first. The picks do not need changing."),

 ("What If Messi & Ronaldo Swapped Nationalities","YOUR DECISION",
  "The reference DZ2cXN-7GxE is an EA SPORTS FC CONSOLE SIMULATION. Team Management screens with overall "
  "ratings, the PlayStation prompt, group tables with Played/Won/Draw/Lost columns, controller icons. It "
  "even admits rigging itself on camera: ‘I totally wasn't forced to simulate until Mbappe scores and "
  "wins.’ It also contains a deepfake of Mbappé's face on a film character.",
  "Your pack is a real-history argument with real footage and a hard closing line — Messi lifts the Euros "
  "in 2016, Ronaldo plays in the 2022 final, the GOAT argument ends on the day of the swap. The reference "
  "proves a GAMEPLAY SIM of this premise travels. It proves nothing about an argument version.",
  "There is no duplicate to fix and the picks are fine. What is missing is the PROOF. Either shoot it on "
  "the strength of the premise and label it an experiment — knowingly — or re-source the lane against "
  "real-footage counterfactuals first."),

 ("What If Ronaldo Never Left Real Madrid","YOUR DECISION",
  "The reference zilVLvf10Sk is a FIFA 19 CAREER MODE SIMULATION, watermark M11M. The FIFA 19 logo "
  "animation, contract-negotiation cutscenes, a squad screen reading Ronaldo 94 and Modrić 91, a LaLiga "
  "standings menu, an in-game clock ticking 92:39 to 92:51. Only about three seconds of it is real.",
  "Worse, the save file is MODDED — Thiago Silva and Hamšík are in Barcelona's squad, so it is not even a "
  "clean sim of its own premise. And its Copa del Rey screen shows ‘Aggregate: 1-4’ and ‘Aggregate: 3-1’ "
  "on the same fixture at the same time.",
  "Same call as above. The picks — 500 Madrid goals, Benzema never becomes the main man, the Juventus "
  "experiment never happens — are a real-history argument and they stand on their own."),

 ("What If PSG Kept Messi, Neymar & Mbappé","YOUR DECISION",
  "The reference kymTJlWMyzk is an EA SPORTS FC SIMULATION, watermark ASP FC. Only four of its fifty-seven "
  "seconds are real footage. It edits Inter's name in the bracket to ‘Inter from Temu’.",
  "ALL THREE WHAT-IF PACKS WERE SOURCED FROM SIMS. That is one mistake made three times, not three "
  "mistakes. What happened is that searching a what-if premise on Shorts returns sim channels, because sim "
  "channels dominate that premise. The premise travels; the format that travels with it is gameplay. That "
  "is a strategic finding, not a bookkeeping error.",
  "Same call. Also still open: #1 is deliberately empty pending a database check of how few games the trio "
  "actually started together — FBref or Transfermarkt will settle it in a minute."),
]

DECISIONS = [
 ("\u2713 NOTHING IS WAITING ON YOU",
  "Both of the calls that were open are settled, and I made them rather than sending them back. "
  "Every pack in this batch is now either ready to shoot or ready with a warning you have already "
  "seen. Anything new that genuinely needs you will appear at the top of the notes app."),

 ("\u2713 SETTLED BY ME \u2014 Budimir replaces Tah",
  "The argument is VARIETY, not labels. Zaza and Tah were the one duplicated mechanism in the pack: "
  "both lean back, both blaze it high over the bar. Your own variety rule defines duplicates by "
  "mechanism rather than outcome, so those two were the pair. Removing Tah deletes the only repeat "
  "AND adds the one failure shape nothing else has. Zaza survives because his CAUSE is unique \u2014 the "
  "fourteen-step prancing run-up. You now have five completely different ways to fail: a ball that "
  "never moves \u00b7 a ball caught standing still \u00b7 a ball that never leaves the floor \u00b7 a ball wide of "
  "the post \u00b7 a ball in the crowd. THE COST, stated plainly: Powershot goes uncovered, so you mirror "
  "four of Part 1's five labels rather than all five. That is the right trade, because Tah's label "
  "rested on a false premise anyway \u2014 the \u201crun-up slip\u201d does not exist and two sources confirmed "
  "it. Tah drops to subs if you disagree."),

 ("\u2713 SETTLED BY ME \u2014 Transfers ships as the top-5, and I changed my mind",
  "I had recommended splitting it into five single-story videos, arguing twelve seconds a pick cannot "
  "carry a transfer saga. THAT REASONING WAS WRONG AND THE ERROR WAS MINE: I was importing the "
  "REFERENCE's story onto YOUR picks. The reference needs sixty-nine seconds because it is one story "
  "with a reversal \u2014 Moyes flies to Munich, sits on the couch, gets sacked three months later. Your "
  "five are not stories, they are one-line facts. A volcano grounded the flight. The fax never sent. "
  "He had already done the club interviews. P\u00e9rez says he passed a medical. Forty-eight hours from "
  "signing. Each of those lands in twelve seconds. And switching format would not have fixed the "
  "proof problem regardless \u2014 a single-story 70-second video is equally unproven on your channel, so "
  "it would have traded a format your audience knows for one they do not, on someone else's "
  "reference. Ship the top-5; expanding De Gea and the fax later is a cheap follow-up if it lands."),
]



SYSTEMS = [
 ("Verify independently, before asking anyone",
  "The knowledge cutoff is not a wall, it is a reason to search. Any claim about a real event now gets "
  "checked against the written record before a watch is trusted. Text wins on what happened; footage wins "
  "on what is in the frame; you win on how it looked. This caught Eze's crossbar, confirmed Embolo and "
  "Tah, and found the IFAB ruling that no amount of watching would ever have surfaced."),
 ("One analysis per moment, not per video",
  "A pass scoped to a single entry's window returns far more than one spread across a whole Short. "
  "Measured on identical footage: the scoped pass found a shirt name, a stadium's sponsor boards and a "
  "keeper's boot colour that the whole-video pass missed entirely."),
 ("A gameplay flag on recent footage is noise",
  "Across 33 passes, every single gameplay flag landed on 2025 or 2026 footage and none on anything "
  "older. In each case the reasoning admitted there was no UI on screen and fell back on the squads "
  "looking implausible — which they do, because they postdate the model's knowledge. A real positive "
  "looks different: ZDF's PSG–Arsenal sim has a PS5 LOGO IN THE SCOREBUG."),
 ("Distinguish fabricated from manipulated",
  "Fabricated is a game dressed as broadcast — catch it with self-contradicting scorelines across cuts. "
  "Manipulated is real footage a publisher has padded — looping, scrubbing, speed changes, replaced "
  "audio. The Neymar roll is the case study: the meme is many rolls, the truth is one."),
 ("A reference is a format source, never a content source",
  "If a pick's wording appears on screen in the reference, it was transcribed rather than chosen. Rank "
  "labels are content. One pack shipped with all five of the reference's captions intact."),
 ("Log the reference's structure and genre at capture",
  "Ranked countdown, single story, bracket, compilation — and real-footage, talking head, gameplay sim. "
  "Gameplay sim is an automatic reject. That single field would have caught three of this batch's "
  "failures on its own."),
 ("Title promise, checked twice",
  "Once on the video and once on every individual pick, independently of whether the footage is real and "
  "whether the moment is good. A striker under a goalkeeper title fails. So does a boot full of noodles "
  "under a lookalikes title."),
 ("Check picks against the parent, number by number",
  "For any Part 2 or redo. Same player at a different moment is fine and worth naming on camera. Same "
  "moment is a re-cut. This caught Stones and Pires/Henry, and only because you asked for reference numbers."),
 ("One link on many rows is a red flag",
  "Not a shortcut. GT-1mKJRDxU was logged against seven separate ideas. It is the proof for none of them."),
 ("No placeholders in a locked pack",
  "Mispronounce sat at two of five, marked locked and approved, with three slots reading ‘In rework’."),
]

VERIFIED = [
 ("Embolo's red card and the IFAB ruling",
  "Sent off for simulation v Argentina, 72nd minute, World Cup 2026 quarter-final. VAR overturned a yellow "
  "shown to Paredes and gave Embolo a second. Argentina won 3-1 in extra time. Three weeks later IFAB said "
  "the VAR had no right to review it at all; FIFA pushed back and said the call ‘restored justice’.",
  ["CNN · cnn.com/2026/07/28/sport/breel-embolo-red-card-decision-world-cup-ifab",
   "ESPN · espn.com/soccer/story/_/id/49468627/ifab-var-process-red-card-switzerland-embolo-vs-argentina-wrong",
   "The Week · theweek.in — FIFA's response"]),
 ("Germany out to Paraguay",
  "Germany 1-1 Paraguay, 3-4 on penalties, last-32 exit. The gameplay flags on the Tah clip were false "
  "positives, and the FIFA URL itself returns in search results as genuine FIFA content.",
  ["Sky Sports · skysports.com — Germany 1-1 Paraguay (3-4 on pens)",
   "ESPN · espn.com/soccer/match/_/gameId/760489/paraguay-germany"]),
 ("The Champions League final shootout",
  "PSG 1-1 Arsenal, 30 May 2026, PSG retain on penalties 4-3. Havertz 6', Dembélé pen 61'. "
  "EZE MISSED — the written record says wide left, three footage passes say over the bar; DISPUTED, say ‘missed’. "
  "GABRIEL PUT HIS OVER THE BAR. Raya saved from Nuno Mendes.",
  ["Wikipedia · 2026 UEFA Champions League final",
   "UEFA · uefa.com — Paris retain Champions League"]),
]
```

#### `handover/build_master.py`
<!-- FILE: handover/build_master.py · 25506 bytes · 414 lines · sha256 62d131587e03d70aad9dae2123c0bb574c7af95918a0227d68b5d0b8c9624998 -->
*Builds LxthalFC-September-SENDOFF.pdf (84pp) with reportlab + DejaVu. DEEP maps pack id → deep files; STAT maps pack id → (state, label); unwrap() guards '#N ' headings; Part 5.5 = clip manifest (colWidths [22, W-2*M-22-148-74, 148, 74]); Part 5.75 = Type B sheets; 22 Sep: Part Six ends with the QA gate run live via qa.py --json. Run from handover/: python3 build_master.py.*
```python
# -*- coding: utf-8 -*-
import sys, os, re, json, io, datetime
sys.path.insert(0,'/root/lx/handover')
from data import GLANCE, READY, BLOCKED, DECISIONS, SYSTEMS, VERIFIED
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (BaseDocTemplate, PageTemplate, Frame, Paragraph,
                                Spacer, Table, TableStyle, KeepTogether, PageBreak)
from reportlab.lib.styles import ParagraphStyle

D="/usr/share/fonts/truetype/dejavu/"
for n,f in [("DJ","DejaVuSans.ttf"),("DJB","DejaVuSans-Bold.ttf"),
            ("DJC","DejaVuSansCondensed-Bold.ttf"),("DJM","DejaVuSansMono.ttf")]:
    pdfmetrics.registerFont(TTFont(n,D+f))
pdfmetrics.registerFontFamily("DJ",normal="DJ",bold="DJB",italic="DJ",boldItalic="DJB")

INK=colors.HexColor("#191d1f"); INK2=colors.HexColor("#4e5860"); INK3=colors.HexColor("#7c868d")
ACC=colors.HexColor("#b8791a"); LINE=colors.HexColor("#d9d5cc")
AMB=colors.HexColor("#fdf4e3"); AMBL=colors.HexColor("#e8c987")
RED=colors.HexColor("#a8443b"); REDBG=colors.HexColor("#fbeeec")
GRN=colors.HexColor("#2f7d55"); GRNBG=colors.HexColor("#eef6f1"); SURF=colors.HexColor("#f5f3ee")

S={
"h0":ParagraphStyle("h0",fontName="DJC",fontSize=36,leading=37,textColor=INK,spaceAfter=5),
"h0s":ParagraphStyle("h0s",fontName="DJC",fontSize=18,leading=20,textColor=ACC,spaceAfter=9),
"sub":ParagraphStyle("sub",fontName="DJ",fontSize=10,leading=14.6,textColor=INK2,spaceAfter=4),
"part":ParagraphStyle("part",fontName="DJC",fontSize=20,leading=22,textColor=ACC,spaceBefore=2,spaceAfter=3),
"partsub":ParagraphStyle("partsub",fontName="DJ",fontSize=9.4,leading=13.4,textColor=INK2,spaceAfter=10),
"pack":ParagraphStyle("pack",fontName="DJC",fontSize=15.5,leading=17,textColor=INK,spaceBefore=5,spaceAfter=2),
"meta":ParagraphStyle("meta",fontName="DJM",fontSize=7,leading=10,textColor=INK3,spaceAfter=5),
"verd":ParagraphStyle("verd",fontName="DJ",fontSize=9,leading=13,textColor=INK2,spaceAfter=6),
"rank":ParagraphStyle("rank",fontName="DJC",fontSize=15,leading=15,textColor=ACC),
"pname":ParagraphStyle("pname",fontName="DJB",fontSize=9.6,leading=12.6,textColor=INK,spaceAfter=1),
"pwhy":ParagraphStyle("pwhy",fontName="DJ",fontSize=8.5,leading=11.6,textColor=INK2,spaceAfter=3),
"link":ParagraphStyle("link",fontName="DJM",fontSize=6.8,leading=9.6,textColor=INK3,spaceAfter=3),
"cut":ParagraphStyle("cut",fontName="DJ",fontSize=8.5,leading=12,textColor=INK),
"lbl":ParagraphStyle("lbl",fontName="DJB",fontSize=8.2,leading=10.8,textColor=ACC,spaceBefore=5,spaceAfter=2),
"b":ParagraphStyle("b",fontName="DJ",fontSize=8.8,leading=12.6,textColor=INK,spaceAfter=4),
"bi":ParagraphStyle("bi",fontName="DJ",fontSize=8.7,leading=12.4,textColor=INK,spaceAfter=3.5,leftIndent=9),
"entry":ParagraphStyle("entry",fontName="DJC",fontSize=12.5,leading=14.5,textColor=INK,spaceBefore=9,spaceAfter=3),
"src":ParagraphStyle("src",fontName="DJM",fontSize=7,leading=9.8,textColor=INK3,spaceAfter=5),
"cell":ParagraphStyle("cell",fontName="DJ",fontSize=8,leading=10.8,textColor=INK),
"cellb":ParagraphStyle("cellb",fontName="DJB",fontSize=7.6,leading=10.4,textColor=INK),
"celld":ParagraphStyle("celld",fontName="DJ",fontSize=7.7,leading=10.4,textColor=INK2),
"warn":ParagraphStyle("warn",fontName="DJ",fontSize=8.5,leading=12,textColor=RED),
"warnb":ParagraphStyle("warnb",fontName="DJB",fontSize=8.6,leading=12.2,textColor=RED),
"call":ParagraphStyle("call",fontName="DJ",fontSize=8.6,leading=12.2,textColor=colors.HexColor("#7a5310")),
"callb":ParagraphStyle("callb",fontName="DJB",fontSize=8.6,leading=12.2,textColor=colors.HexColor("#7a5310")),
"dh":ParagraphStyle("dh",fontName="DJB",fontSize=9.6,leading=12.4,textColor=INK,spaceAfter=1),
"lu":ParagraphStyle("lu",fontName="DJ",fontSize=8.6,leading=12,textColor=INK),
}
W,H=A4; M=16*mm
def esc(t): return t.replace("&","&amp;").replace("<","&lt;").replace(">","&gt;")
def fmt(t):
    t=esc(t); t=re.sub(r"\*\*\*\s*(.+?)\s*\*\*\*", r"<b>\1</b>", t); return t.replace("***","")

def deco(c,d):
    c.saveState(); c.setFont("DJM",6.6); c.setFillColor(INK3)
    c.drawString(M,H-11*mm,"LXTHALFC  ·  SEPTEMBER BATCH  ·  COMPLETE SEND-OFF")
    c.drawRightString(W-M,H-11*mm,datetime.date.today().strftime("%d %b %Y").upper())
    c.setStrokeColor(LINE); c.setLineWidth(.5); c.line(M,H-13.5*mm,W-M,H-13.5*mm)
    c.setFont("DJM",6.6); c.drawRightString(W-M,10*mm,"%d"%d.page); c.restoreState()

def box(txt,style,bg,bd,pad=6):
    t=Table([[Paragraph(txt,style)]],colWidths=[W-2*M-4])
    t.setStyle(TableStyle([("BACKGROUND",(0,0),(-1,-1),bg),("BOX",(0,0),(-1,-1),.6,bd),
        ("LEFTPADDING",(0,0),(-1,-1),7),("RIGHTPADDING",(0,0),(-1,-1),7),
        ("TOPPADDING",(0,0),(-1,-1),pad),("BOTTOMPADDING",(0,0),(-1,-1),pad)]))
    return t

# ---------- markdown renderer for deep/ and refaudit/ ----------
LABELRE = re.compile(r"^[A-Z0-9ÄÖÜÉÍÑÁ][A-Z0-9ÄÖÜÉÍÑÁ ’'\-/&(),.]{2,42}:")
def unwrap(lines):
    out=[]
    for ln in lines:
        if ln.strip()=="": out.append(""); continue
        if ln.startswith("═") or ln.startswith("─"): out.append("@@RULE"); continue
        s=ln.strip()
        new = (LABELRE.match(s) or s.startswith("***") or s.startswith("[!")
               or re.match(r"^\d+\.\s",s) or re.match(r"^#\d+ ",s))
        if ln.startswith(" ") and out and out[-1] not in ("","@@RULE") and not new \
           and not out[-1].startswith("***") and not out[-1].startswith("[!") \
           and not re.match(r"^#\d+ ", out[-1]):
            out[-1]=out[-1].rstrip()+" "+s
        else: out.append(s)
    return out

def render_md(path, flow, skip_title=True):
    if not os.path.exists(path): return
    for s in unwrap(io.open(path,encoding='utf-8').read().split("\n")):
        if not s: continue
        if s=="@@RULE":
            flow.append(Spacer(1,3))
            flow.append(Table([[""]],colWidths=[W-2*M],rowHeights=[1],
                style=TableStyle([("LINEBELOW",(0,0),(-1,-1),.5,LINE)])))
            flow.append(Spacer(1,4)); continue
        if s.startswith("# "):
            if skip_title: continue
            flow.append(Paragraph(esc(s[2:]),S["entry"])); continue
        body=fmt(s)
        if s.startswith("[!!") or s.startswith("[!]"):
            flow.append(Spacer(1,2)); flow.append(box(body,S["warn"],REDBG,RED)); flow.append(Spacer(1,3)); continue
        if s.startswith("***") and s.rstrip().endswith("***"):
            inner=re.sub(r"^<b>(.*)</b>$", r"\1", body.strip())
            flow.append(Spacer(1,2)); flow.append(box(inner,S["call"],AMB,AMBL)); flow.append(Spacer(1,3)); continue
        if re.match(r"^#\d+ ",s): flow.append(Paragraph(body,S["entry"])); continue
        if s.startswith(("SOURCE:","AUTHENTIC:","PICTURE:","STATUS:")):
            flow.append(Paragraph(body,S["src"])); continue
        if re.match(r"^\d+\.\s",s): flow.append(Paragraph(body,S["bi"])); continue
        m=LABELRE.match(s)
        if m:
            head=m.group(0).rstrip(":"); rest=body[len(esc(m.group(0))):].strip()
            flow.append(Paragraph(esc(head),S["lbl"]))
            if rest: flow.append(Paragraph(rest,S["bi"]))
            continue
        flow.append(Paragraph(body,S["b"]))

PACKS=json.load(io.open('/root/lx/handover/final_packs.json',encoding='utf-8'))
BYID={p['id']:p for p in PACKS}
DEEP={
 "signature-redo":["signature-moves.md"],
 "gk-assists":["gk-assists-all.md"],
 "pace-abuser-2":["pace-abuser-son.md","pace-abuser-2.md"],
 "oscar-2":["oscar-2.md"],
 "badge-redo":["badge-5-valverde.md","badge-4-vandeven.md","badge-3-sule.md","badge-2-stones.md","badge-1-ferland-mendy.md"],
 "penalty-2":["penalties.md","penalty-4-pires-henry.md","penalty-2-budimir.md"],
 "accidental-saves":["acc-5-full-reverse.md","acc-4-no-look.md","acc-3-idk.md","acc-2-neuer.md","acc-1-choupo.md"],
}
REFA={
 "pace-abuser-2":"pace-abuser-2.md","oscar-2":"oscar-2.md","primes-redo":"primes-redo.md",
 "another-nation":"another-nation.md","transfers-almost":"transfers-almost.md",
 "forgot-club":"GT-1mKJRDxU-THREE-PACKS.md","swap-nations":"swap-nations.md",
 "ronaldo-stayed":"ronaldo-stayed.md","psg-trio":"psg-trio.md",
}
TITLE2ID={p['title']:p['id'] for p in PACKS}
def id_for(title):
    for t,i in TITLE2ID.items():
        if t[:26].lower()==title[:26].lower(): return i
    key=title.lower()
    for t,i in TITLE2ID.items():
        a=set(re.findall(r"[a-z]+",t.lower())); b=set(re.findall(r"[a-z]+",key))
        if len(a&b)>=3: return i
    return None

doc=BaseDocTemplate("/root/lx/LxthalFC-September-SENDOFF.pdf",pagesize=A4,
    leftMargin=M,rightMargin=M,topMargin=20*mm,bottomMargin=15*mm,
    title="LxthalFC — September Batch, Complete Send-Off",author="LxthalFC")
doc.addPageTemplates([PageTemplate(id="p",frames=[Frame(M,15*mm,W-2*M,H-35*mm,id="f",
    leftPadding=0,rightPadding=0,topPadding=0,bottomPadding=0)],onPage=deco)])
F=[]

# COVER
F.append(Paragraph("September Batch",S["h0"]))
F.append(Paragraph("Complete send-off — every video, every description",S["h0s"]))
F.append(Paragraph("Sixteen packs, eighty picks, thirty-five on-field moments described from "
 "scoped forensic passes. Every reference watched and audited. Every fact that mattered checked against "
 "the written record rather than the footage alone \u2014 which is where most of the corrections came from.",S["sub"]))
F.append(Spacer(1,3))
F.append(Paragraph("<b>Nothing is waiting on you.</b> You answered all eight decisions in the app; the two follow-up calls "
 "they created have been settled here rather than sent back, with the reasoning for each in Part Four. "
 "<b>Fourteen packs are ready to shoot.</b> Two more are ready and carry a warning about format "
 "precedent rather than content \u2014 shoot them knowing it. Lookalikes was DROPPED at your instruction "
 "and logged as rejected, so it cannot resurface on a future board.",S["sub"]))
F.append(Spacer(1,8))
F.append(Paragraph("CONTENTS",S["lbl"]))
for n,t in [("ONE","The final line-ups — all sixteen, at a glance"),
            ("TWO","Ready to shoot — production sheets and full descriptions"),
            ("THREE","Blocked — what is wrong, and the reference audit behind it"),
            ("FOUR","Your decisions \u2014 what you chose and what it changed"),
            ("FIVE","Verified against the written record"),
            ("SIX","What changed in the system")]:
    F.append(Paragraph("<b>PART %s</b> — %s"%(n,esc(t)),S["b"]))

# PART ONE
F.append(PageBreak())
F.append(Paragraph("Part one — the final line-ups",S["part"]))
F.append(Paragraph("All sixteen as they now stand. Green is shootable now. Amber is complete and shootable too, but "
 "carries a warning worth hearing first. Nothing here is broken or half-built. "
 "Full detail on each follows in parts two and three.",S["partsub"]))
ORDER=["signature-redo","gk-assists","pace-abuser-2","oscar-2","primes-redo","another-nation",
       "badge-redo","penalty-2","accidental-saves","transfers-almost","forgot-club",
       "mispronounce","blame-first","swap-nations","ronaldo-stayed","psg-trio"]
STAT={ "signature-redo":("READY",GRN,GRNBG),"gk-assists":("READY",GRN,GRNBG),
 "pace-abuser-2":("READY",GRN,GRNBG),"oscar-2":("READY",GRN,GRNBG),
 "primes-redo":("READY \u00b7 TYPE B",GRN,GRNBG),"another-nation":("READY \u00b7 TYPE B",GRN,GRNBG),
 "badge-redo":("READY \u00b7 STONES KEPT",GRN,GRNBG),
 "penalty-2":("READY \u00b7 BUDIMIR IN",GRN,GRNBG),
 "accidental-saves":("ALL 5 DESCRIBED",GRN,GRNBG),
 "mispronounce":("READY \u00b7 SLOTS FILLED",GRN,GRNBG),
 "transfers-almost":("READY \u00b7 TOP-5 AS BUILT",GRN,GRNBG),"forgot-club":("SHOOT KNOWING",ACC,AMB),
 "blame-first":("SHOOT KNOWING",ACC,AMB),
 "swap-nations":("READY \u00b7 EXPERIMENT",GRN,GRNBG),"ronaldo-stayed":("READY \u00b7 EXPERIMENT",GRN,GRNBG),
 "psg-trio":("READY \u00b7 RE-RANKED",GRN,GRNBG)}
for pid in ORDER:
    p=BYID[pid]; lab,col,bg=STAT[pid]
    blk=[Paragraph(esc(p['title']),S["pack"]),
         Paragraph('<font color="#%s"><b>%s</b></font>  ·  %s'%(col.hexval()[2:],esc(lab),esc(p['meta'])),S["meta"])]
    rows=[]
    for (rk,nm,why) in p['picks']:
        bad = ("REPLACE" in nm) or ("In rework" in nm) or ("NEEDS VERIFYING" in nm)
        rows.append([Paragraph("<b>#%s</b>"%esc(rk),S["cell"]),
                     Paragraph(('<font color="#%s"><b>%s</b></font>'%(RED.hexval()[2:],esc(nm))) if bad else "<b>%s</b>"%esc(nm),S["lu"])])
    t=Table(rows,colWidths=[11*mm,W-2*M-11*mm])
    t.setStyle(TableStyle([("VALIGN",(0,0),(-1,-1),"TOP"),("LEFTPADDING",(0,0),(-1,-1),2),
        ("RIGHTPADDING",(0,0),(-1,-1),2),("TOPPADDING",(0,0),(-1,-1),1.6),
        ("BOTTOMPADDING",(0,0),(-1,-1),1.6),("BACKGROUND",(0,0),(-1,-1),bg)]))
    blk.append(t)
    if p['subs']: blk.append(Paragraph("<b>SUBS:</b> "+esc(p['subs']),S["celld"]))
    blk.append(Spacer(1,5))
    F.append(KeepTogether(blk))

# PART TWO
F.append(PageBreak())
F.append(Paragraph("Part two — ready to shoot",S["part"]))
F.append(Paragraph("Nine packs. Each one gives the five picks with source link and timestamp, the camera "
 "angle worth cutting on and the commentary line to use — then the full forensic description of every "
 "moment underneath it. Amber is a detail worth building the edit on; red is a correction or a warning.",S["partsub"]))
for k,p in enumerate(READY):
    if k: F.append(PageBreak())
    pid=id_for(p["title"])
    F.append(Paragraph(esc(p["title"]),S["pack"]))
    col = GRN if p["status"].startswith(("READY","ALL")) else ACC
    F.append(Paragraph('<font color="#%s"><b>%s</b></font>  ·  %s'%(col.hexval()[2:],esc(p["status"]),esc(p["meta"])),S["meta"]))
    F.append(Paragraph(fmt(p["verdict"]),S["verd"]))
    for (rk,name,why,links,cut) in p["picks"]:
        blk=[]
        hdr=Table([[Paragraph("#"+esc(rk),S["rank"]),Paragraph(fmt(name),S["pname"])]],
                  colWidths=[13*mm,W-2*M-13*mm])
        hdr.setStyle(TableStyle([("VALIGN",(0,0),(-1,-1),"TOP"),("LEFTPADDING",(0,0),(-1,-1),0),
            ("RIGHTPADDING",(0,0),(-1,-1),0),("TOPPADDING",(0,0),(-1,-1),0),("BOTTOMPADDING",(0,0),(-1,-1),1)]))
        blk.append(hdr)
        if why: blk.append(Paragraph(fmt(why),S["pwhy"]))
        for L in links: blk.append(Paragraph("▶ "+esc(L),S["link"]))
        if cut:
            warn = cut.strip().startswith("[!")
            blk.append(box(fmt(cut), S["warn"] if warn else S["cut"],
                           REDBG if warn else SURF, RED if warn else LINE, 5))
        blk.append(Spacer(1,6))
        if len(cut)<900: F.append(KeepTogether(blk))
        else:
            for x in blk: F.append(x)
    if p.get("warn"):
        w="[!" in p["warn"]
        F.append(box(fmt(p["warn"]),S["warn"] if w else S["cut"],REDBG if w else SURF,RED if w else LINE))
        F.append(Spacer(1,5))
    if p.get("quote"):
        F.append(box(fmt(p["quote"]),S["call"],AMB,AMBL)); F.append(Spacer(1,5))
    F.append(Paragraph("DECISION",S["lbl"])); F.append(Paragraph(fmt(p["decision"]),S["b"]))
    if pid and pid in DEEP:
        F.append(PageBreak())
        F.append(Paragraph("Full descriptions — "+esc(p["title"]),S["part"]))
        F.append(Paragraph("Every moment, watched one at a time at full fidelity.",S["partsub"]))
        for fn in DEEP[pid]: render_md("/root/lx/deep/"+fn,F)
    if pid and pid in REFA:
        F.append(Spacer(1,6)); F.append(Paragraph("Reference audit — what the parent video contains",S["lbl"]))
        render_md("/root/lx/refaudit/"+REFA[pid],F)

# PART THREE
F.append(PageBreak())
F.append(Paragraph("Part three — the warnings worth hearing first",S["part"]))
F.append(Paragraph("Two packs, and NEITHER is broken or half-built. Every pick in both is real, named and sourced. "
 "What they carry is a warning about format precedent rather than about content \u2014 shoot them knowing "
 "it. The reference audit behind each follows.",S["partsub"]))
SEEN=set()
for (t_,sev,what,why,fix) in BLOCKED:
    pid=id_for(t_)
    F.append(Paragraph(esc(t_),S["pack"]))
    F.append(Paragraph('<font color="#%s"><b>%s</b></font>'%(RED.hexval()[2:],esc(sev)),S["meta"]))
    if pid and pid in BYID:
        rows=[]
        for (rk,nm,why2) in BYID[pid]['picks']:
            bad=("REPLACE" in nm) or ("In rework" in nm) or ("NEEDS VERIFYING" in nm)
            rows.append([Paragraph("<b>#%s</b>"%esc(rk),S["cell"]),
                         Paragraph(('<font color="#%s"><b>%s</b></font>'%(RED.hexval()[2:],esc(nm))) if bad else "<b>%s</b>"%esc(nm),S["lu"])])
        tb=Table(rows,colWidths=[11*mm,W-2*M-11*mm])
        tb.setStyle(TableStyle([("VALIGN",(0,0),(-1,-1),"TOP"),("LEFTPADDING",(0,0),(-1,-1),2),
            ("RIGHTPADDING",(0,0),(-1,-1),2),("TOPPADDING",(0,0),(-1,-1),1.6),
            ("BOTTOMPADDING",(0,0),(-1,-1),1.6),("BACKGROUND",(0,0),(-1,-1),SURF)]))
        F.append(tb); F.append(Spacer(1,5))
    F.append(Paragraph("WHAT IT IS",S["lbl"])); F.append(Paragraph(fmt(what),S["b"]))
    F.append(Paragraph("WHY THAT BREAKS IT",S["lbl"])); F.append(Paragraph(fmt(why),S["b"]))
    F.append(Paragraph("THE FIX",S["lbl"])); F.append(Paragraph(fmt(fix),S["b"]))
    if pid and pid in REFA and REFA[pid] not in SEEN:
        SEEN.add(REFA[pid])
        F.append(Paragraph("THE REFERENCE AUDIT IN FULL",S["lbl"]))
        render_md("/root/lx/refaudit/"+REFA[pid],F)
    F.append(Spacer(1,9))

# PART FOUR / FIVE / SIX
F.append(PageBreak())
F.append(Paragraph("Part four — every call, and who made it",S["part"]))
F.append(Paragraph("Eight you made in the app, and two I made myself rather than handing back. The reasoning for mine is spelled out so you can overrule either one in a single tap.",S["partsub"]))
for (h_,body) in DECISIONS:
    F.append(KeepTogether([Paragraph(esc(h_),S["dh"]),Paragraph(fmt(body),S["b"]),Spacer(1,3)]))
F.append(Spacer(1,10))
F.append(Paragraph("Part five — verified against the written record",S["part"]))
F.append(Paragraph("Three things could not be settled by watching anything, and all three fell over in one "
 "lookup. Text wins on what happened; footage wins on what is in the frame.",S["partsub"]))
for (h_,body,srcs) in VERIFIED:
    blk=[Paragraph(esc(h_),S["dh"]),Paragraph(fmt(body),S["b"])]
    for s_ in srcs: blk.append(Paragraph("▶ "+esc(s_),S["link"]))
    blk.append(Spacer(1,4)); F.append(KeepTogether(blk))
F.append(PageBreak())
# ---------- PART 5.5 : CLIP MANIFEST ----------
F.append(PageBreak())
F.append(Paragraph("Part five and a half \u2014 the clip manifest",S["part"]))
F.append(Paragraph("Every on-field pick, where its footage lives, and the exact window to pull. "
 "Thirty-five clips across twenty-eight source videos. The CUT ON column names the one angle worth "
 "building the entry around where a pass identified one. Type B packs carry no clips and are not "
 "listed.",S["partsub"]))
import sys as _sys; _sys.path.insert(0,"/root/lx")
from clips import CLIPS as _CLIPS
for _pack, _cl in _CLIPS:
    F.append(Spacer(1,7))
    F.append(Paragraph(esc(_pack),S["entry"]))
    _rows=[[Paragraph("<b>#</b>",S["cell"]),Paragraph("<b>PICK</b>",S["cell"]),
            Paragraph("<b>SOURCE &amp; LINK</b>",S["cell"]),Paragraph("<b>IN\u2013OUT</b>",S["cell"])]]
    for _r,_p,_v,_lab,_w,_c,_n in _cl:
        _src = "%s<br/><font face='DJ' size=6.5 color='#7c868d'>youtu.be/%s</font>"%(esc(_lab),esc(_v))
        _pk  = esc(_p)
        if _c: _pk += "<br/><font size=7 color='#b8791a'>CUT ON: %s</font>"%esc(_c)
        if _n: _pk += "<br/><font size=7 color='#a8443b'>%s</font>"%esc(_n)
        _rows.append([Paragraph("<b>%s</b>"%esc(_r),S["cell"]),Paragraph(_pk,S["cell"]),
                      Paragraph(_src,S["cell"]),Paragraph("<b>%s</b>"%esc(_w),S["cell"])])
    _t=Table(_rows,colWidths=[22,W-2*M-22-148-74,148,74])
    _t.setStyle(TableStyle([
        ("VALIGN",(0,0),(-1,-1),"TOP"),
        ("LINEBELOW",(0,0),(-1,0),.6,LINE),
        ("LINEBELOW",(0,1),(-1,-2),.25,LINE),
        ("TOPPADDING",(0,0),(-1,-1),4),("BOTTOMPADDING",(0,0),(-1,-1),4),
        ("LEFTPADDING",(0,0),(-1,-1),3),("RIGHTPADDING",(0,0),(-1,-1),3),
        ("BACKGROUND",(0,0),(-1,0),SURF)]))
    F.append(_t)
F.append(Spacer(1,8))
F.append(box("[!!] ONE OUTCOME IS DISPUTED AND YOU SHOULD NOT STATE IT ON CAMERA. Eze's penalty: "
 "Wikipedia's account of the shootout says he SHOT WIDE LEFT. THREE separate vision passes on "
 "Arsenal's own footage say it went OVER THE BAR. Both agree it went LEFT and that he missed; they "
 "disagree on whether it cleared the bar or passed the post. TNT Sports' live commentary says only "
 "that he \u201cmissed his side's second effort\u201d and does not settle it. My earlier note in this "
 "document stated WIDE LEFT as settled fact \u2014 that was over-confident and this corrects it. "
 "SAY \u201che missed\u201d, which is uncontested, and do not name the destination. "
 "[!] AND IF IT IS OVER THE BAR, THE PACK HAS A VARIETY PROBLEM: Zaza at #5 also ends over the bar, "
 "which is the exact duplicate-mechanism issue that removing Tah was meant to fix.",
 S["warn"],REDBG,RED))
F.append(Spacer(1,10))

# ---------- PART 5.75 : TYPE B SHEETS ----------
F.append(PageBreak())
F.append(Paragraph("Part five and three quarters \u2014 the packs with no clips",S["part"]))
F.append(Paragraph("Nine packs carry no footage, so they never got a forensic description. For these "
 "the equivalent is a VERIFIED FACT: what is true, where it is confirmed, and what not to claim. "
 "Forty-five picks \u2014 twenty-four confirmed against a named source, twenty still resting on your own "
 "comments and marked so you can see which.",S["partsub"]))
import sys as _sys; _sys.path.insert(0,"/root/lx")
from typeb import SHEETS as _SH
for _title,_fam,_state,_head,_picks in _SH:
    F.append(Spacer(1,8))
    _t = esc(_title) + ("   <font size=7 color='#b8791a'>%s</font>"%esc(_fam) if _fam else "")
    F.append(Paragraph(_t,S["entry"]))
    F.append(Paragraph(esc(_head),S["verd"]))
    for _r,_name,_v,_fact,_src,_note in _picks:
        _badge = ("<font color='#2f7d55'>VERIFIED</font>" if _v=="V"
                  else "<font color='#a8443b'>FROM COMMENTS</font>" if _v=="C" else "")
        F.append(Paragraph("<b>#%s  %s</b>   <font size=7>%s</font>"%(esc(_r),esc(_name),_badge),S["pname"]))
        F.append(Paragraph(esc(_fact),S["pwhy"]))
        if _src: F.append(Paragraph("<font size=7.5 color='#7c868d'>SOURCE \u00b7 %s</font>"%esc(_src),S["pwhy"]))
        if _note: F.append(Paragraph("<font size=7.5 color='#a8443b'>%s</font>"%esc(_note),S["pwhy"]))
    F.append(Spacer(1,3))
F.append(Spacer(1,8))
F.append(box("THE TWENTY MARKED \u201cFROM COMMENTS\u201d ARE NOT WRONG \u2014 THEY ARE UNCHECKED. Every one came "
 "from your own audience rather than a source, and the system's own rule for these packs is to verify "
 "against sources and never against comments. They are safe to shoot as stated, but any one of them "
 "that carries a QUOTE, a FEE or a PRECISE NUMBER should get a search before it goes on camera \u2014 "
 "those are what the comments correct. Van Basten is the worked example: \u201cdone at 28\u201d survived a "
 "check, \u201cretired at 28\u201d would not have.",S["warn"],AMB,AMBL))
F.append(Spacer(1,10))

F.append(Paragraph("Part six — what changed in the system",S["part"]))
F.append(Paragraph("Ten rules, each written because something went wrong this batch. All are in the skill, "
 "so they run on the next one without being asked for.",S["partsub"]))
for i,(n,body) in enumerate(SYSTEMS,1):
    F.append(KeepTogether([Paragraph("%d. %s"%(i,esc(n)),S["dh"]),Paragraph(fmt(body),S["b"]),Spacer(1,3)]))
F.append(Spacer(1,10))

# ---- the QA gate, run live at build time, so every warning is acknowledged by name in the send-off
try:
    import subprocess, json as _json
    _q = subprocess.run(["python3", "/root/lx/qa.py", "--json"], capture_output=True, text=True, timeout=120)
    _R = _json.loads(_q.stdout)
    _nf, _nw = len(_R["fail"]), len(_R["warn"])
    F.append(Paragraph("The QA gate on this send-off",S["dh"]))
    F.append(Paragraph(fmt("Run at build time: %d checks passed · %d warnings · %d failures. Failures block; "
        "warnings do not, but each is acknowledged here by name so nothing passes silently." % (_R["pass"], _nw, _nf)),S["b"]))
    for _r in _R["fail"]:
        F.append(Paragraph(fmt("FAIL — %s: %s" % (_r["check"], _r["msg"])),S["warn"]))
    for _r in _R["warn"]:
        F.append(Paragraph(fmt("WARN [%s] %s — %s" % (_r["err"], _r["check"], _r["msg"])),S["b"]))
    if _nw:
        F.append(Paragraph(fmt("Why they stand: the count-as-fact hits sit inside deep files where the instability "
            "caveat is more than 520 characters away (the deep file is the record, not the script); the yardages in "
            "the production sheet are pitch geometry — ‘six-yard box’, ‘from about 25 yards’ — that can be dropped "
            "from the voiceover without loss. Say the foot, never the number."),S["b"]))
    for _r in _R["info"]:
        F.append(Paragraph(fmt("INFO [%s] %s — %s" % (_r["err"], _r["check"], _r["msg"])),S["cut"]))
except Exception as _e:
    F.append(Paragraph(fmt("QA gate could not be run at build time: %s" % _e),S["warn"]))
F.append(Spacer(1,10))
F.append(box("The pack-notes board is published and current alongside this — same sixteen packs, same "
 "status, editable, and it is where to write how each video actually performs once it is out.",S["cut"],SURF,LINE))
doc.build(F)
print("built")
```

#### `handover/final_packs.json`
<!-- FILE: handover/final_packs.json · 42237 bytes · 562 lines · sha256 31aac3dc3b3d1e9fe604accca63c5f634a43403e6a346d9efe1f0849f40859cd -->
*The 16 packs exactly as shipped, regenerated from notes-app.html's PACKS with node; 22 Sep Eze row → DISPUTED. QA compares this against the app (ids) and against data.py (pick names).*
```json
[
 {
  "id": "pace-abuser-2",
  "title": "Top 10 Pace Abuser Moments Part 2",
  "state": "locked",
  "meta": "Your Pt1 5,382,421 · lane OG_Clips 14.6M @ 19.09× · runs 10→6 · SON NOW FULLY DESCRIBED",
  "picks": [
   [
    "10",
    "Son — the Burnley solo goal",
    "278 likes, top named request on Pt1 — and it WON THE FIFA PUSKÁS AWARD, the only goal in either pack with a trophy"
   ],
   [
    "9",
    "Terens Puhiri — Borneo FC, Liga 1 Indonesia",
    "OG_Clips ranks him #2 in a 14.6M video, above Mbappé and Bale"
   ],
   [
    "8",
    "Van de Ven — solo run for Spurs",
    "Requested 3×; he's the cold open of your own Die for the Badge"
   ],
   [
    "7",
    "Adeyemi vs Chelsea",
    "OG_Clips #7 — rounds Kepa, ends in a goal"
   ],
   [
    "6",
    "Bale vs Inter — Maicon",
    "43 likes across 3 comments calling it the real number one"
   ]
  ],
  "subs": "Dembélé v England 2017 · Hakimi v Alphonso Davies · Bellerín chasing Pedro",
  "note": "THE LINE NOBODY ELSE HAS: every one of these runs is ONE-FOOTED. Son every touch right. Puhiri three, all right. Van de Ven five, all left. Adeyemi five, all left. At full sprint nobody switches feet. That came out of counting and it is genuinely yours. [!!] SAY THE FOOT, NEVER THE NUMBER. An earlier version of this note said \"Son takes nine touches\". Three separate passes over the same footage returned 9, 10 and 11–12, so the COUNT is not stable. The FOOT is — a dedicated tie-breaker on the clearest slow-motion angle graded all eight visible touches RIGHT and CERTAIN, with zero left-foot contacts, while admitting the angle cuts in mid-run. Repeat passes never once disagreed about which foot. The observation is safe; the arithmetic is not. Son's entry, now described in full: he picks it up 12–15 yards outside his OWN box, scans early (head left, then right), reads both lanes as covered and goes. Lowton lunges and is bypassed · Brady squeezes in, can't match him and VISIBLY GIVES UP · Mee and Tarkowski both retreat and converge and he goes BETWEEN them. Finishes right foot, inside/instep, low into the bottom right from about 13 yards. Cut on the ULTRA SLOW-MOTION HEAD-ON at 02:40–03:19 — the only angle that shows the feet well enough to carry the one-footed point. Fix from the watch: Traoré is at Fulham and Ederson saves it · Bale's defender is Bartra, not Boateng · Henry hits the post and does not score. [!] No scorebug and no speed graphic on Son, Puhiri or Van de Ven. Don't quote a distance or a top speed — only Adeyemi carries a readable clock."
 },
 {
  "id": "oscar-2",
  "title": "Top 5 Players Who Deserve The Oscar Award Part 2",
  "state": "locked",
  "meta": "Your Pt1 2,987,542 · 1,825 comments · no Part 2 exists",
  "picks": [
   [
    "5",
    "Neymar rolling — Mexico, 2018",
    "Spawned a worldwide challenge; readable in a second"
   ],
   [
    "4",
    "Micah Richards",
    "Requested twice (21 likes); he's a pundit so the clip travels"
   ],
   [
    "3",
    "Breel Embolo vs Argentina",
    "\"He truly deserves the Oscar D'or\" (8) — most specific request"
   ],
   [
    "2",
    "Suárez holds his own teeth — the Chiellini bite, 2014",
    "RESOLVED: the vague slot is filled. He bites Chiellini and then sits on the turf cupping his mouth and clasping his front teeth as if HE is hurt, then pulls his collar over his face. Referee gives nothing. Cannot be confused with Part 1’s PSG throat-clutch. ESPN broadcast, ITA 0-0 URU 78:25"
   ],
   [
    "1",
    "Rivaldo, 2002 vs Turkey",
    "Ünsal sent off, FIFA fined him. Consensus GOAT of diving"
   ]
  ],
  "subs": "Sterling (8) · the keeper who faked unconsciousness · Lazović, named correctly",
  "note": "[VERIFIED 19 Sep] Embolo's red card is real and there is a far bigger story on it. 72nd min, Pinheiro books Paredes, VAR intervenes, Paredes' yellow rescinded, Embolo second yellow and off; Argentina win 3-1 in extra time. Three weeks later IFAB said the VAR had no right to review it at all — a caution that isn't a second yellow can only be reviewed for mistaken identity, not to change the offence. FIFA pushed back, saying the call “restored justice”. Nobody ranking dives has that ending. I suggested Embolo to #4 and Richards to #3 — YOUR CALL, 20 Sep: keep the approved order. Embolo stays at #3; the IFAB ending is the script's job. Never repeat: the Lazović dive is 35 yards out, outside the box, nobody near him, play never stopped. Jota's opponent is Newcastle. Courtois is Atlético. Hundreds of RIP comments for Jota — don't reuse that clip mockingly."
 },
 {
  "id": "penalty-2",
  "title": "Worst Penalty Miss With Every Technique Part 2",
  "state": "locked",
  "meta": "✓ SETTLED — Budimir replaces Tah · all five described · no two failures alike",
  "picks": [
   [
    "5",
    "Zaza, Euro 2016 — STUTTER",
    "About FOURTEEN tiny prancing high-knee steps, torso rigid, almost no ground covered — then one plant and a left-footed laces strike that balloons over. Neuer touches the crossbar to look bigger, dives low right, never gets near it"
   ],
   [
    "4",
    "Pires & Henry, Highbury — PASS ✓ KEPT",
    "22 Oct 2005, Arsenal 1-0 City, ~72nd min, REDCURRANT Highbury kit. Pires' studs SKIM THE TOP of the ball and it moves an inch. Distin hooks it clear, GRAHAM POLL gives an INDIRECT FREE KICK TO CITY. End on the Sparta Prague callback where Henry mimes it back at him"
   ],
   [
    "3",
    "Agüero v Chelsea, Etihad — PANENKA",
    "A genuine panenka chipped down the middle. Édouard Mendy refuses to dive, stays on his feet, takes a half-step forward and CATCHES IT at chest height. Agüero raises an apologetic hand"
   ],
   [
    "2",
    "Budimir v Valencia, 97th minute ✅ IN, replacing Tah",
    "He WON the penalty himself. Stutters to read Mamardashvili, and his STANDING LEG BUCKLES — knee sways out, balance gone, he stumbles forward over the ball and his left toe scuffs it. THE BALL NEVER LEAVES THE GRASS. It rolls at walking pace into the keeper's chest. Osasuna 0-1, 97th minute"
   ],
   [
    "1",
    "Eberechi Eze v PSG — SIDEFOOT, missed — destination DISPUTED",
    "CL final shootout. ⚠ It did NOT hit the crossbar. Beyond that the sources split: the match record says WIDE LEFT, three footage passes say OVER THE BAR. Say “he missed” — nobody contests that. GABRIEL is the one who went over for certain, with Arsenal's fifth"
   ]
  ],
  "subs": "Tah v Paraguay (powershot, over the bar) · Gabriel (laces, over the bar) · Yuri Alberto's cavadinha",
  "note": "✓ SETTLED, AND I MADE THE CALL RATHER THAN SENDING IT BACK. Budimir replaces Tah. Why Tah and not one of the others — the argument is variety, not labels. Zaza and Tah were the one duplicated MECHANISM in the pack: both lean back, both blaze it high over the bar. Your own variety rule says duplicates are defined by mechanism, not outcome, and those two were the pair. Taking Tah out removes the only repeat AND adds the one failure shape nothing else in the pack has. Zaza survives because his CAUSE is unique — the fourteen-step prancing run-up — not just his outcome. What you now have is five completely different ways to fail: a ball that never moves (Pires) · a ball caught standing still (Agüero) · a ball that never leaves the floor (Budimir) · a ball wide of the post (Eze) · a ball in the crowd off a fourteen-step run-up (Zaza). No two alike. That is the strongest five this pack has had. The cost, stated plainly: POWERSHOT goes uncovered, so you mirror four of Part 1's five labels rather than all five. That is the right trade — Tah's label was the one built on a false premise anyway, since the “run-up slip” everyone repeats does not exist and two sources confirmed it. Tah drops to subs, so he is there if you disagree. [!] SAY “BUCKLES”, NOT “SLIPS” on Budimir. No divot, no torn turf, and the pass could not separate a real surface slip from a pure loss of balance. The honest version is better: he did it to himself. The commentary is the caption, free: “Nije ni šutnuo!” — he didn't even take a shot. And your closing frame is Arrasate on the bench, chin on fist, saying nothing."
 },
 {
  "id": "primes-redo",
  "title": "Top 5 Shortest Lived Primes (2026 Redo)",
  "state": "locked",
  "meta": "Your Pt1 1,967,544 · 2,230 comments",
  "picks": [
   [
    "5",
    "João Félix",
    "2,800 likes — most expensive teenager ever, Saudi league at 26"
   ],
   [
    "4",
    "Dele Alli",
    "2,357 — two PFA Young Player awards, then out of football"
   ],
   [
    "3",
    "Andrey Arshavin",
    "1,365 — four goals at Anfield, then gone"
   ],
   [
    "2",
    "Michu",
    "167 — one season, eighteen goals, an ankle that never recovered"
   ],
   [
    "1",
    "Marco van Basten",
    "~110 across three comments — three Ballon d'Ors, done at 28"
   ]
  ],
  "subs": "Coutinho (64) · Ansu Fati · Andy Carroll (11)",
  "note": "Both Pt1 errors are burned into the captions, not just the voiceover: £80 MILLION at 0:29 (Torres was £50m) and 2 BALLON D'ORS at 1:18 (one, 2005). A re-voice won't fix them."
 },
 {
  "id": "accidental-saves",
  "title": "When Goalkeepers Make Accidental Saves",
  "state": "locked",
  "meta": "APPROVED with a known title-promise wobble · Reference 8,997,688 · runs 6→2 · BOTH OPEN SLOTS NOW FILLED, ALL NAMED AND WATCHED",
  "picks": [
   [
    "5",
    "Full Reverse Save",
    "Championship, green kit. Dives forward onto his chest, BACK TURNED, ball off his trailing heel"
   ],
   [
    "4",
    "No-Look Save",
    "Cardiff keeper at Swansea. Faces his own goal, ball off the back of his head and neck"
   ],
   [
    "3",
    "IDK Save",
    "Brazilian league. Face-down after diving, ball off the post onto his back, sits up and catches it"
   ],
   [
    "2",
    "Manuel Neuer v Bas Dost — the heel he can't see",
    "Neuer commits early, dives right, ends up FACE DOWN on the grass, beaten. Dost rolls it at the empty net and it hits the bottom of Neuer's trailing left boot, raised behind him. He is looking the other way and cannot see the ball"
   ],
   [
    "1",
    "Choupo-Moting stops his OWN team scoring",
    "Nkunku chips the keeper, ball rolling over the line. Choupo-Moting runs in to tap it in for the glory, mistimes it completely — his left boot traps the ball dead ON the line and knocks it onto the post. On-screen caption in the source: \"200 IQ\""
   ]
  ],
  "subs": "Zlatan (hands behind his back, never moves, ball off his calf) · Bendtner (blocks Fàbregas's goalbound shot with his shin, Wenger's hands on his head) · the referee in Liga MX",
  "note": "All five are now watched and named. The two I've filled are the strongest of four accidental saves I confirmed frame-by-frame in a 4.58M goal-line compilation, plus a fifth from a Guardian clip. #1 is the perfect finisher — the declarative writes itself: he didn't save a goal, he saved the opposition. Commentary: \"He's blocked it on the line from his own player!\" Three strong subs, any could swap in: Zlatan stands beside the post with his HANDS BEHIND HIS BACK, never looks, ball off the back of his right calf — commentary calls him \"le capitaine Zlatan qui sauve son équipe\". Bendtner is offside in front of an open net trying to duck out of the way and blocks his own teammate. The referee — Óscar Macías, Cruz Azul v Toluca, sprinting toward the six-yard box with his back turned, ball off his right heel, keeper stranded on the floor; commentary: \"¡El árbitro es el héroe del Toluca!\" If you want a non-keeper spike, the referee is the funniest thing in the pack."
 },
 {
  "id": "gk-assists",
  "title": "Goalkeepers With Unbelievable Assists",
  "state": "locked",
  "meta": "All five from the official Premier League channel · RE-WATCHED CLIP BY CLIP · two corrections",
  "picks": [
   [
    "5",
    "Ederson → Agüero, Man City v Huddersfield",
    "GOAL KICK, struck off the ground with the LEFT — a dead ball from inside his own six-yard box, flat and driven rather than lofted. Reported at 85–86 yards. Agüero rounds the onrushing keeper with a soft right-foot touch and CHIPS it left-footed into the empty net"
   ],
   [
    "4",
    "Alisson → Salah, Liverpool v Man United",
    "DROP-KICK out of his hands, RIGHT foot — flat and fast, skimming over the retreating United players. One bounce. Salah starts inside his own half to stay onside, holds James off, and finishes with the INSIDE OF THE LEFT under de Gea"
   ],
   [
    "3",
    "Schmeichel → Solskjær, Man Utd v Sunderland",
    "OVERHAND THROW, RIGHT arm, javelin style, clearing the halfway line on the fly. Kubicki misses the bounce completely, Solskjær is clean through and chips Pérez. The 1996 SD picture is part of the appeal — say the year"
   ],
   [
    "2",
    "Čech → Drogba, Wolves v Chelsea",
    "DROP-PUNT out of his hands — LEFT foot, corrected. High and booming, climbing above the floodlights, the opposite shape to Alisson's. Drogba muscles straight past Berra, takes it round Hahnemann with the outside of the right and rolls it in"
   ],
   [
    "1",
    "Van der Sar → Rooney, Man Utd v Aston Villa",
    "OPEN-PLAY BACKPASS, struck off the ground with the RIGHT — a rolling ball, three-step approach, NOT a dead ball. High and looping. Rooney cushions it right-footed and half-volleys it in off the instep. Then the ending: Ferdinand jogs the full length back to embrace him, and Evra leaps into his arms"
   ]
  ],
  "subs": "Reina → Dossena at Old Trafford in the 4-1 (lob over Van der Sar) · Joe Hart → Antonio · Almunia → Fàbregas (a throw, and Fàbregas runs it 60 yards himself)",
  "note": "This pack was the shakiest, then the most solid, and it has now been corrected twice. All five clips come from the Premier League's own 16-minute goalkeeper-assists compilation, each captioned on screen with keeper, fixture and season. [!!] THE DELIVERY COUNT — read this before you script it. The pack was first written as FIVE different deliveries. A pass over the footage cut that to THREE and told you to say three. A second, scoped pass per clip says it is FOUR, and that two deliveries had been wrongly grouped together. ONE: goal kick off the ground (Ederson, LEFT) — a dead ball, and the written record confirms it as a goal-kick assist. TWO: open-play backpass off the ground (Van der Sar, RIGHT) — a completely different act. THREE: drop-punt from the hands (Čech LEFT, Alisson RIGHT). FOUR: overhand throw (Schmeichel, RIGHT arm). Say four. Not three, not five. Note this also corrects an older note here that called Van der Sar's a free kick — it is open play. THE LINE NOBODY ELSE HAS: every method that appears twice is split by side. The two struck off the ground split left and right — Ederson LEFT, Van der Sar RIGHT. The two drop-punts split left and right — Čech LEFT, Alisson RIGHT. And Schmeichel is the outlier who never uses a foot at all. Two corrections earned on the re-watch: Čech's kicking foot is the LEFT, not the right — a dedicated tie-breaker graded it CERTAIN with the contact frame fully visible. And Ederson's is a GOAL KICK, not open play, confirmed in the written record. What I had to drop, honestly: Neuer at Schalke going up for a corner — searched hard, found nothing but FIFA and PES gameplay. I think I invented it. Nicholas Hagen's punt — same, unsourced. Ederson → Haaland exists but isn't in the official compilation. [!] No scorebug on any of the five — no clock and no score for any clip. Don't state a minute. And don't quote a distance for any of them except Ederson's, where 85–86 yards comes from the written record and should be attributed as reported. [!] Alisson's famous run — his length-of-the-pitch celebration is NOT in this source; it cuts at 00:11. You need a second clip if you want it."
 },
 {
  "id": "another-nation",
  "title": "Players Who Could've Played For Another Nation",
  "state": "locked",
  "meta": "Reference 4,105,413 @ 10.99× · pt2 2,085,039 @ 5.60× · ten pairings already used",
  "picks": [
   [
    "5",
    "Bukayo Saka — NIGERIA",
    "Both parents Nigerian; Nigeria said they'd take him but wouldn't beg"
   ],
   [
    "4",
    "Michael Olise — ENGLAND",
    "Eligible for FOUR nations. Southgate personally tried to flip him in 2022"
   ],
   [
    "3",
    "Alphonso Davies — LIBERIA",
    "Born in the Buduburam refugee camp in Ghana; chose Canada"
   ],
   [
    "2",
    "Kylian Mbappé — ALGERIA",
    "41 likes across four comments; the reference used him for Cameroon"
   ],
   [
    "1",
    "Lionel Messi — SPAIN",
    "Pékerman: the paperwork was prepared for the U-20 World Cup. Messi: it never crossed my mind"
   ]
  ],
  "subs": "Jamal Musiala, who turned down England AND Nigeria · Marc Guéhi, born in Abidjan · David Alaba",
  "note": "Ronaldo–Cape Verde is dead — the link is a great-grandmother and FIFA Article 6.1 needs a parent or grandparent. Steal the format: six-slot tracker, five avatars plus a red ?, each face stamped with its flag on the beat drop."
 },
 {
  "id": "transfers-almost",
  "title": "Transfers That Almost Happened",
  "state": "locked",
  "meta": "All five researched against press sources · five different clubs, no repeats",
  "picks": [
   [
    "5",
    "Ronaldinho → Manchester United, 2003",
    "He has said he was 48 HOURS from signing. United had just sold Beckham and wanted a replacement. He went to Barcelona and won the Ballon d'Or two years later"
   ],
   [
    "4",
    "Lewandowski → Blackburn Rovers, 2010",
    "An ACT OF GOD stopped it — the Icelandic volcanic ash cloud grounded his flight to England. He has confirmed the story himself. He ended up at Dortmund, then Bayern"
   ],
   [
    "3",
    "Neymar → Real Madrid",
    "Florentino Pérez has said publicly that Neymar PASSED A MEDICAL with Madrid before the Barcelona move. Neymar has separately said he nearly chose Bayern because of Guardiola"
   ],
   [
    "2",
    "Fekir → Liverpool, 2018",
    "So far gone that he had already DONE THE CLUB INTERVIEWS in a Liverpool shirt. Collapsed at the medical over a knee. He has since accused Liverpool of making excuses"
   ],
   [
    "1",
    "De Gea → Real Madrid, 2015",
    "Deadline day. The move died because the PAPERWORK WASN'T SUBMITTED IN TIME — the infamous fax. He stayed at United for eight more years"
   ]
  ],
  "subs": "Kaká → Man City (the £100m deal Milan fans blocked) · Gerrard → Chelsea · Mbappé → Real Madrid, twice",
  "note": "✓ SETTLED: shoot it as the top-5, as built. I changed my mind and you should know why. I had recommended splitting it into five single-story videos, on the grounds that twelve seconds a pick cannot carry a transfer saga. That reasoning was wrong, and the error was mine: I was importing the REFERENCE’s story onto YOUR picks. The reference needed sixty-nine seconds because it is one story with a reversal — Moyes flies to Munich, sits on the couch, gets sacked. Your five are not stories, they are one-line facts. A volcano grounded the flight. The fax never sent. He had already done the club interviews. Pérez says he passed a medical. Forty-eight hours from signing. Every one of those is a punchline that lands in twelve seconds. And switching format would not have fixed the proof problem anyway — a single-story 70-second video is equally unproven on your channel, so I would have been trading a known format your audience expects for an unknown one, on the strength of someone else’s reference. Ship the top-5. If it lands, expanding De Gea and the fax into its own video is a cheap follow-up. The flag that remains is about precedent, not content. All five picks are real, named and press-sourced. What failed validation was the REFERENCE, not the video. [REF AUDIT — WRONG SHAPE] The reference (0_yDGO1Jgt0) is not a top-5. It is one 69-second story about Toni Kroos to Man United — Moyes flying to Munich and sitting on his couch, then getting sacked three months later. No duplicate in your five, but twelve seconds a pick cannot carry a story like that. My read at the time was to run it as one transfer per video — WITHDRAWN, see the top of this note: it ships as the top-5. CORRECTION from the research: I had Neymar → Man City. The stronger and better-sourced version is Neymar → Real Madrid, because Pérez himself has said Neymar passed a medical there. The Bayern/Guardiola version is also on the record from Neymar. Man City was the weakest of the three, so it's gone. Five different clubs, as you asked — United, Blackburn, Madrid, Liverpool, Madrid again. If the two Madrids bother you, Kaká to Man City swaps in cleanly at #3 and keeps one club per entry. This is Type B — no clips needed, and every line above traces to a press source rather than a comment."
 },
 {
  "id": "signature-redo",
  "title": "Top 10 Signature Moves (2026 Redo)",
  "state": "locked",
  "meta": "⚠ You published Part 2 on 1 June — 128,204 against Part 1's 1,580,732 · ALL 5 CLIPS NOW WATCHED",
  "picks": [
   [
    "5",
    "Robben's cut-in — vs Juventus",
    "Two left-foot touches, Barzagli slips onto the turf, curled into the top corner past Buffon. Clean — no deflection, unlike the Man Utd one which nicks Vidić"
   ],
   [
    "4",
    "Ronaldinho's elástico — the nutmeg on Dunga",
    "1999 Gre-Nal final, Grêmio v Internacional. Right foot: outside pushes it right, inside snaps it back — straight THROUGH Dunga's legs. Dunga (#8) left turned and stranded"
   ],
   [
    "3",
    "Iniesta's croqueta — vs Man City",
    "Kompany (#4) charges out of defence, Iniesta shifts it right foot to left, Kompany wipes out flat on the grass. The referee has to jump out of the way"
   ],
   [
    "2",
    "Messi's body feint — the slow-mo breakdown",
    "He never touches the ball. Drops the left shoulder, plants the left foot, defender's whole weight goes with it — THEN pushes it past the trailing leg with the outside of the left boot"
   ],
   [
    "1",
    "The Cruyff turn — Sweden, 1974",
    "Cruyff (#14) winds up to cross, then drags it behind his own standing left leg with the INSIDE of his right boot. One touch. Olsson (#2) lunges, momentum takes him the wrong way. Cruyff reaches the byline and crosses"
   ]
  ],
  "subs": "Quaresma's trivela · Robinho's stepovers · Okocha's rainbow flick",
  "note": "Script gift for #1 — Cruyff in his own words, on camera: \"I never did tricks. I saw something and I did it and it just came out. There was an opponent there and I had to outplay him. So that was the easiest way, so you just do it.\" That is your hard declarative finisher. Five different mechanics, no clash: cut-and-curl · elástico nutmeg · two-footed shift · no-touch feint · drag behind the standing leg. Order is yours as approved — but Ronaldinho at #1 is arguable, since the source compilation's own title card calls it \"THE GREATEST piece of individual skill ever show[n]\". Still true: your Part 2 caption reads \"ANTHONY SPIN\" and the clip ends with Antony's pass rolling out for a throw-in v Sheriff Tiraspol."
 },
 {
  "id": "badge-redo",
  "title": "Top 5 Die for the Badge (2026 Redo)",
  "state": "locked",
  "meta": "⚠ You have six already · ALL FIVE CLIPS WATCHED · STONES KEPT AND NOW DESCRIBED",
  "picks": [
   [
    "5",
    "Valverde on Morata — 114:29, Supercopa final, extra time",
    "Morata clean through with 30m of grass and only Courtois to beat. Valverde's eyes never go near the ball — he scythes through both legs from behind. Straight red, no protest. SIMEONE PATS HIM ON THE HEAD as he walks off. Madrid win the shootout"
   ],
   [
    "4",
    "Van de Ven — Europa League final, Bilbao, 67:38",
    "Vicario spills it, MAGUIRE heads at the empty net from six yards — Van de Ven hooks it away AIRBORNE with his left foot, an overhead scissor under the bar. Spurs win 1-0, first trophy in 17 years"
   ],
   [
    "3",
    "Süle — DORTMUND, not Bayern — v Mbappé, 16:36",
    "Mbappé rounds Kobel and shoots left-footed into an open net from seven yards. Süle has tracked back 30 metres, slides in on his back and hooks it over his own bar with his right leg in mid-air"
   ],
   [
    "2",
    "John Stones — off the line in front of Salah ✓ YOUR CALL: KEPT",
    "Mané hits the INSIDE OF THE POST · Stones swings to clear and the ball SMASHES INTO EDERSON and rolls back at the empty net · Stones dives across and hooks it off the line with the instep of the RIGHT boot, inches ahead of Salah · then gets up and clears the SECOND ball too. He makes the save twice"
   ],
   [
    "1",
    "FERLAND Mendy vs Man City — not Édouard",
    "CL semi-final second leg, 86:11, Madrid 0-1 down and 3-5 on aggregate. Courtois beaten and on the floor, Grealish stabs it past him, Mendy sprints back from outside the box and hooks it off the line with an outstretched left boot"
   ]
  ],
  "subs": "Kyle Walker (a sliding hook on Pulisic, and an overhead bicycle clearance) · Boateng · Tsimikas",
  "note": "✓ YOUR CALL: Stones stays. He is your Part 1's #2 at the same rank and you have chosen to run it knowing that. Frame it, don't hide it — say “you've seen this one before, and it's still the best example there is” in the first breath. The audience that spots repeats is the same one that rewards being told. He is now fully described from Man City's own channel. [!!] THE NUMBER IS WRONG AND IT IS FREE REDO AMMUNITION. Your Part 1 voiceover says 11.7mm. An earlier note here said 11.2mm. Both are wrong. Manchester City's own site: “Stones had somehow managed to ensure that 11 MILLIMETRES of the ball had not crossed.” Sky Sports' own headline: “how Etihad showdown and 11mm decided the 2018-19 title race.” Two sources, one of them the club. Say eleven millimetres, and put no decimal on screen — a decimal is exactly what drags a correction comment. [!] And the figure is not in the footage at all. The Goal Decision System graphic in this cut shows only the words NO GOAL before cutting back to live play. If you put a number on screen you are adding it yourself. [!!] The sequence was backwards in my old note. I had written “Ederson's clearance rebounds off him”. It is the other way round: Stones swings to clear and the ball hits Ederson, who is diving backwards, and comes off him towards the empty net. Süle was NOT at Bayern. Dortmund neon yellow, #25, and the man he denies is MBAPPÉ. German commentary: “Der größtmögliche Grätschmoment”. #5 has the best detail in the batch: Valverde takes the red without a word, and as he passes the Atlético bench Simeone reaches out and pats him on the head. Italian commentary: “Sarà rosso, ma è una super giocata” — and “L'unico modo”, the only way."
 },
 {
  "id": "forgot-club",
  "title": "Players We Always Forget Played for That Club",
  "state": "noproof",
  "meta": "⚠ No viral reference — best in lane 77,617 @ 0.34× · all five press-sourced",
  "picks": [
   [
    "5",
    "Andrea Pirlo at INTER MILAN",
    "Before he was Pirlo, he was an Inter player. A brief stint where they never worked out what he was — then Milan moved him in front of the back four and he became the best deep playmaker alive"
   ],
   [
    "4",
    "Arjen Robben at CHELSEA",
    "Three seasons at Stamford Bridge, 2004–2007, two Premier League titles — BEFORE Real Madrid and before Bayern. 1,889 likes on a comment asking for this"
   ],
   [
    "3",
    "Kevin De Bruyne at CHELSEA",
    "Mourinho told him he was SIXTH CHOICE. De Bruyne says they spoke twice in total. Sold to Wolfsburg, came back to City and became the best midfielder in the league"
   ],
   [
    "2",
    "Thierry Henry at JUVENTUS",
    "Signed in 1999, played out of position on the WING, gone in half a season. Arsenal bought him for less than Juventus paid"
   ],
   [
    "1",
    "Frank Lampard at MANCHESTER CITY",
    "He scored against Chelsea. On loan. And REFUSED TO CELEBRATE — stood dead still with his arms up. Gary Cahill called it \"weird\". It denied Chelsea the win"
   ]
  ],
  "subs": "Didier Drogba at Galatasaray · Ronaldo at PSV · Kaká at Orlando City",
  "note": "✓ COMPLETE AND SHOOTABLE — nothing is missing. Five picks, all press-sourced, no placeholders. The flag means “no format precedent”, not “broken”. [REF AUDIT — LANE PROOF ONLY] GT-1mKJRDxU is your own “Players We Always Call By Their Full Name”, 3,240,079 views — about names you can only say in full, not about forgetting a club. That one link is logged against seven different ideas. It proves the lane, not this title's mechanic. Shoot it if you want, but log it as riding lane proof. (Correction: I first wrote this was another creator's video. It is yours.) Rebuilt with Salah-at-Chelsea tier names, as you asked. Riquelme is gone — you were right that casual fans don't say that name out loud. Every one of these is a name people know attached to a club they've forgotten. #1 is the best one because of the reaction, not the transfer. Lampard scoring against the club he'd defined and then standing frozen with his arms up is a single readable image, which is what this format needs. Broadcast footage is on Man City's own channel. #4 restored — Robben at Chelsea came out during a revision and shouldn't have. A 1,889-like comment is a reason to include, not avoid. Honest caveat on the lane: best video in this lane is 77,617 against your 89k median. The names are now strong but the format has never gone big for anyone. Worth knowing before you spend a slot."
 },
 {
  "id": "mispronounce",
  "title": "Players We Always Mispronounce",
  "state": "locked",
  "meta": "✓ Three empty slots FILLED and verified · no collision with Full Name Pt1's five",
  "picks": [
   [
    "5",
    "Khvicha Kvaratskhelia",
    "Commentators gave up entirely and just say “Kvara”. 30 likes in your comments. Babbel listed him among the trickiest names at the Euros and had to supply an audio clip because writing it out didn't work"
   ],
   [
    "4",
    "César Azpilicueta — the one who got RENAMED ✅ NEW",
    "“Ath-pee-lee-KWE-ta”. Nobody could say it, so Chelsea fans and teammates called him DAVE — for a decade, to his face, in songs. Chelsea's own website tells the story of how the nickname started. A Premier League captain got a new name because of a pronunciation"
   ],
   [
    "3",
    "Wojciech Szczęsny ✅ NEW",
    "“VOY-check Sh-CHENS-ny”, not “Woj-chi-ech Shez-nee”. Arsenal, Roma, Juventus, Barcelona — two decades at the top and the spelling alone is a visual gag. The ę is a nasal vowel English has no equivalent for, which is why nobody lands it"
   ],
   [
    "2",
    "Thierry Henry",
    "He says it differently depending on which language he is speaking — the man himself gives two answers. 49 likes"
   ],
   [
    "1",
    "Mesut Özil — and there are TWO right answers ✅ NEW",
    "Not “Ozzil”. German is “MAY-zoot UR-zil”, IPA [ˈmeːzut ˈøːzil]. Turkish is “meh-SOOT ur-ZEEL”, IPA [meˈsut œˈzil] — different stress in BOTH words. Born in Germany to a Turkish family, so both are correct and they are not the same. You watched him for a decade and never said it either way"
   ]
  ],
  "subs": "Lamine Yamal (321) · Rúben Dias (17) · Sokratis Papastathopoulos · İlkay Gündoğan (“GUN-do-an”, the ğ is silent)",
  "note": "✓ YOUR CALL: fill them for me. Done — 4, 3 and 1 are now real picks. Every pronunciation above is sourced, not guessed. Özil's two IPA renderings come from Wikipedia's own transcription. Szczęsny's phonetics come from a published list of names people get wrong. Azpilicueta's “Dave” story is told on Chelsea's official site. Kvaratskhelia's is Babbel's Euros guide. In a pronunciation video the pronunciation IS the product, so none of this is from memory. #1 is the hard declarative finisher because Özil has two correct answers, German and Turkish, stressed differently, and most people never landed either. That's a better ending than “this one is hard”. #4 is the most engaging because it isn't really about phonetics — it's about a man who got renamed. Dave is a genuinely funny payoff and the club documents it. Checked against Full Name Pt1 (Nuno Mendes, Luis Díaz, Rafael Leão, Kroos, Ronaldo): no collision on any of the five. Different mechanic too — Full Name is names you can only say whole; this is names you say wrong. [!] The Krease/Rolando evidence is still void — that is your own caption bait, not real mispronunciation. Never build a pick on it. [!] Lane caveat unchanged: the reference is your own Full Name Pt1, which proves the lane, not this title."
 },
 {
  "id": "blame-first",
  "title": "Players We Always Blame First",
  "state": "noproof",
  "meta": "⚠ Football version flat — 369,137 @ 0.68× and 142,421 @ 0.26×",
  "picks": [
   [
    "5",
    "David Beckham, 1998",
    "Sent off v Argentina, effigy hung outside a pub. He didn't concede the goals"
   ],
   [
    "4",
    "Bukayo Saka, Euro 2020",
    "Nineteen, fifth penalty, racially abused for a shootout he was sent up last to take"
   ],
   [
    "3",
    "John Terry, 2008 final",
    "Slipped on a waterlogged spot; Anelka still had to score after him"
   ],
   [
    "2",
    "Roberto Baggio, 1994",
    "Dragged Italy to the final almost alone, missed one penalty, that's all anyone remembers"
   ],
   [
    "1",
    "Loris Karius, 2018 final",
    "Concussed by Ramos's elbow, diagnosed days later, blamed for a decade"
   ]
  ],
  "subs": "Moussa Sissoko · Sergio Ramos for Bale's exit · Fernando Torres at Chelsea",
  "note": "✓ COMPLETE AND SHOOTABLE. Five picks straight from your own comments, no placeholders. The flag is about precedent, not content. [REF AUDIT — LANE PROOF ONLY] Same reference again — your own Full Name Pt1. Blame First runs on grievance; Full Name runs on a name test. Different engines, one inherited proof. The five picks are strong and come from your own comments — shoot it knowingly as lane-proof, not as a precedented format. Note: Full Name Pt2 did 449,749 against a 3.24M parent (0.14×). The concept travels, the football execution didn't. A hockey version of the same format did 200,711 @ 2.97× off an 18,400-sub channel; NBA 91.7k; college football 38.7k. Arguably your opening."
 },
 {
  "id": "swap-nations",
  "title": "What If Messi & Ronaldo Swapped Nationalities",
  "state": "locked",
  "meta": "Written from INSIDE the premise — Messi Portuguese, Ronaldo Argentine",
  "picks": [
   [
    "5",
    "Messi lifts the Euros in 2016",
    "Portugal won that final with Ronaldo in tears on the touchline after 25 minutes. Messi is the one carried off instead — and Portugal still win, so he has a major trophy at 29 instead of 34"
   ],
   [
    "4",
    "Ronaldo plays in the 2022 World Cup final",
    "Argentina get there and win it. He is 37 that December — exactly the age Messi was. The greatest final ever played becomes his"
   ],
   [
    "3",
    "Ronaldo finally wins a Copa América",
    "Argentina won it in 2021 and again in 2024. His trophyless international record — the biggest stick used against him — disappears"
   ],
   [
    "2",
    "Messi's drought gets worse, not better",
    "Portugal lost a Euro final in 2004 and a semi in 2012 before they won anything. Swap him in and he still spends a decade losing finals, just in a different shirt"
   ],
   [
    "1",
    "The GOAT argument ends on the day of the swap",
    "Every single thing people argue about is national. Whoever gets Argentina wins a World Cup and a Copa. Whoever gets Portugal wins a Euro and a Nations League. The debate was never about the player"
   ]
  ],
  "subs": "Messi never carries the Maradona comparison · Ronaldo inherits that weight instead · not one club trophy changes",
  "note": "[REF AUDIT — WRONG GENRE] The reference (DZ2cXN-7GxE) is an EA Sports FC console simulation — Team Management screens, rating badges, group tables, controller prompts. It even admits rigging itself on camera: “I totally wasn’t forced to simulate until Mbappe scores and wins.” Your pack is a real-footage argument. The reference proves a gameplay sim of this premise travels, not an argument. Written from inside the premise — every entry states what WOULD happen, not what wouldn't. That was your fix on the Ronaldo one and it applies here too. #1 is the hard declarative finisher and it's the argument the video exists to make: nothing about their club careers changes at all. Every trophy that separates them is an international one. The anchors underneath (2016 Euro final, 2022 World Cup final, Copa 2021 and 2024, Portugal's 2004 final) are all real results, so the speculation is built on facts rather than floating."
 },
 {
  "id": "ronaldo-stayed",
  "title": "What If Ronaldo Never Left Real Madrid",
  "state": "locked",
  "meta": "Five things that WOULD happen if he stayed — not 'without him', as you corrected",
  "picks": [
   [
    "5",
    "He passes 500 Real Madrid goals",
    "He left on 450 in 438 games. Two more seasons near that rate and he's the first man to 500 for the club — a number nobody would ever touch"
   ],
   [
    "4",
    "Benzema never becomes the main man",
    "Benzema spent nine years making space for Ronaldo. The moment Ronaldo left he became Madrid's leader and won a Ballon d'Or at 34. He doesn't get that if Ronaldo is still in front of him"
   ],
   [
    "3",
    "Madrid's three empty seasons look nothing alike",
    "After he left they went three years without a Champions League having just won three in a row. That collapse is the strongest argument they sold him too early"
   ],
   [
    "2",
    "The Juventus experiment never happens",
    "Juventus bought him to win a Champions League and went out earlier each year. That whole chapter — and the United return after it — only exists because he left"
   ],
   [
    "1",
    "The all-time record is bigger and it is not close",
    "His goals-per-game at Madrid was the best of his career by distance. Every season there instead of anywhere else adds to a career record that is already the highest in the sport"
   ]
  ],
  "subs": "No vacant shirt for Hazard to fail in · Madrid delay a galáctico signing by years · the 2018 final is his last act either way",
  "note": "[REF AUDIT — WRONG GENRE] The reference (zilVLvf10Sk) is a FIFA 19 Career Mode sim on a modded save (Thiago Silva and Hamšík are in Barcelona's squad). Its own Copa del Rey screen contradicts itself — “Aggregate: 1-4” in the top bar, “Aggregate: 3-1” underneath. Same tell as the fake Eze penalty. No proof for a real-footage version. Rewritten from inside the premise, as you asked. Every entry names a thing that happens BECAUSE he stays. The old version kept describing Madrid without him, which as you said doesn't make sense for the title. #5 is the hook because it's a number — 450 in 438 is real, and it's the kind of stat a comment section argues about. Anchors (450 goals, three straight Champions Leagues, the three-year drought, Benzema's Ballon d'Or at 34) are all real; the speculation sits on top of them."
 },
 {
  "id": "psg-trio",
  "title": "What If PSG Kept Messi, Neymar & Mbappé",
  "state": "locked",
  "meta": "✓ Unverified stat DROPPED and re-ranked · Penaltygate verified and added · all five sourced",
  "picks": [
   [
    "5",
    "They once scored SIX between them in one game",
    "Clermont 1–6 PSG. Mbappé hat-trick, Neymar hat-trick, and Messi a hat-trick of ASSISTS. Three hat-tricks in one match. Confirmed by Goal, CBS and ESPN"
   ],
   [
    "4",
    "They fell out over who takes penalties — in public ✅ NEW",
    "PSG 5-2 Montpellier, 13 Aug 2022, the first home game of the season. MBAPPÉ MISSES a penalty. Afterwards NEYMAR LIKES tweets attacking the arrangement, one reading “Now it's official, Mbappé is the one who takes penalties at PSG. Clearly it's a contract thing, because in no club in the world would Neymar be the second taker.” The press called it Penaltygate; Galtier had to answer for it and so did the club president"
   ],
   [
    "3",
    "Messi won a Ballon d'Or as a PSG player",
    "His 2021 award came after he had already signed. PSG have had a reigning Ballon d'Or winner on the pitch and still never won the thing they bought him for"
   ],
   [
    "2",
    "They never won a Champions League together",
    "The entire point of the trio. Ligue 1 titles, no European Cup — and PSG finally won it after all three had gone"
   ],
   [
    "1",
    "All three were gone within two years",
    "Messi to Miami, Neymar to Al-Hilal, Mbappé to Madrid. The most expensive front three ever assembled did not survive two full seasons"
   ]
  ],
  "subs": "The 2022 Madrid collapse after leading the tie · Mbappé's “it's a shame it's only happening now” quote · Ligue 1 titles with no European Cup",
  "note": "✓ YOUR CALL: drop the stat and re-rank. Done — and the pack is better for it. The unverified “how few games they started together” line is gone. Everything else moved up one and a verified entry came in at #4. The new #4 is the best entry in the pack. Penaltygate is on the record with ESPN, Goal and Get French Football News, it has a date and a scoreline, and the evidence is Neymar's likes — which is a very modern, very readable beat. It is also the most argumentative entry, which is exactly where #4 belongs in your formula. [!] Genre warning still stands. The reference (kymTJlWMyzk) is an EA Sports FC sim, watermark ASP FC, only 4 of its 57 seconds real footage. All three What-If packs were sourced from sims — one mistake made three times. You have chosen to shoot these as a labelled experiment, so go in knowing the lane proof is for gameplay, not for argument. Facts, not scenarios — your correction, applied. Every line above traces to a press report. No clips needed."
 }
]
```

### 6.4 The two hosted pages (sources)

#### `notes-app.html`
<!-- FILE: notes-app.html · 59589 bytes · 565 lines · sha256 6eb2e28d9ffb797eb0062d75abcfc274b801a41f03fa365af9e1f9578b1b9621 -->
*Source of the notes app artifact (Version 17). const PACKS (16) · const DECISIONS (empty) · STATES incl. noproof 'Shoot knowing' · decisions panel (renderDecisions / writeDecision, empty state 'Nothing needs your call') · db capability via claude.use('db'). Republish the same path; from a new conversation, Artifact read first then publish with url.*
```html
<title>LxthalFC Pack Notes</title>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Barlow+Condensed:wght@500;600;700&family=IBM+Plex+Mono:wght@400;500&family=IBM+Plex+Sans:wght@400;500;600&display=swap">
<style>
:root{
  --bg:#f3f1ec; --surface:#ffffff; --surface-2:#eceae4; --line:#d9d5cc;
  --ink:#191d1f; --ink-2:#4e5860; --ink-3:#7c868d;
  --accent:#b8791a; --accent-soft:#f6e6c9;
  --ok:#2f7d55; --ok-soft:#dcefe3;
  --warn:#9a6a10; --warn-soft:#f7e9cc;
  --open:#a8443b; --open-soft:#f6ddd9;
  --shadow:0 1px 2px rgba(25,29,31,.06),0 8px 24px rgba(25,29,31,.05);
}
@media (prefers-color-scheme:dark){
  :root:not([data-theme="light"]){
    --bg:#0e1214; --surface:#161c1f; --surface-2:#1d2529; --line:#2b3438;
    --ink:#e8edee; --ink-2:#9dabb1; --ink-3:#77858b;
    --accent:#f0b429; --accent-soft:#3a2d12;
    --ok:#5fc08b; --ok-soft:#16301f;
    --warn:#e2a93f; --warn-soft:#332714;
    --open:#e2776a; --open-soft:#361c19;
    --shadow:0 1px 2px rgba(0,0,0,.4),0 8px 24px rgba(0,0,0,.28);
  }
}
:root[data-theme="dark"]{
  --bg:#0e1214; --surface:#161c1f; --surface-2:#1d2529; --line:#2b3438;
  --ink:#e8edee; --ink-2:#9dabb1; --ink-3:#77858b;
  --accent:#f0b429; --accent-soft:#3a2d12;
  --ok:#5fc08b; --ok-soft:#16301f;
  --warn:#e2a93f; --warn-soft:#332714;
  --open:#e2776a; --open-soft:#361c19;
  --shadow:0 1px 2px rgba(0,0,0,.4),0 8px 24px rgba(0,0,0,.28);
}
*{box-sizing:border-box}
body{
  background:var(--bg); color:var(--ink);
  font-family:"IBM Plex Sans",system-ui,-apple-system,sans-serif;
  font-size:15px; line-height:1.55; margin:0;
  padding-block:28px 64px; padding-left:16px; padding-right:16px;
}
.wrap{max-width:860px;margin:0 auto}
h1{
  font-family:"Barlow Condensed",Impact,sans-serif; font-weight:700;
  font-size:clamp(34px,7vw,52px); line-height:.98; letter-spacing:-.01em;
  margin:0 0 6px; text-wrap:balance; text-transform:uppercase;
}
.sub{color:var(--ink-2);margin:0 0 22px;max-width:60ch}
.tally{display:flex;flex-wrap:wrap;gap:8px;margin-bottom:10px}
.tally button{
  font:inherit; font-size:13px; cursor:pointer;
  background:var(--surface); color:var(--ink-2);
  border:1px solid var(--line); border-radius:999px; padding:6px 13px;
}
.tally button[aria-pressed="true"]{background:var(--ink);color:var(--bg);border-color:var(--ink)}
.tally button:focus-visible{outline:2px solid var(--accent);outline-offset:2px}
.saveline{font-size:12.5px;color:var(--ink-3);min-height:1.4em;margin-bottom:22px}
.card{
  background:var(--surface); border:1px solid var(--line);
  border-radius:10px; box-shadow:var(--shadow);
  margin-bottom:14px; overflow:hidden;
}
.card[hidden]{display:none!important}
.chead{display:flex;gap:14px;align-items:flex-start;padding:16px 18px 0}
.idx{
  font-family:"Barlow Condensed",Impact,sans-serif; font-weight:600;
  font-size:26px; line-height:1; color:var(--ink-3);
  font-variant-numeric:tabular-nums; padding-top:3px; min-width:26px;
}
.ctitle{flex:1;min-width:0}
.ctitle h2{
  font-family:"Barlow Condensed",Impact,sans-serif; font-weight:600;
  font-size:23px; line-height:1.12; margin:0 0 5px; text-transform:uppercase;
  letter-spacing:.005em;
}
.meta{
  font-family:"IBM Plex Mono",ui-monospace,monospace; font-size:11.5px;
  color:var(--ink-3); letter-spacing:-.01em;
}
.pill{
  font-size:11px; font-weight:600; letter-spacing:.06em; text-transform:uppercase;
  border-radius:4px; padding:4px 8px; white-space:nowrap; align-self:flex-start;
}
.p-locked{background:var(--ok-soft);color:var(--ok)}
.p-flag{background:var(--warn-soft);color:var(--warn)}
.p-open{background:var(--open-soft);color:var(--open)}
.p-fail{background:#f6e3e0;color:#9a3a30;box-shadow:inset 0 0 0 1px #e4bdb7}
.p-noproof{background:var(--warn-soft);color:var(--warn);box-shadow:inset 0 0 0 1px currentColor}
.body{padding:14px 18px 18px}
ol.picks{list-style:none;margin:0 0 4px;padding:0;display:flex;flex-direction:column;gap:7px}
ol.picks li{display:flex;gap:12px;align-items:baseline}
.rank{
  font-family:"Barlow Condensed",Impact,sans-serif; font-weight:700;
  font-size:19px; line-height:1.2; color:var(--accent);
  font-variant-numeric:tabular-nums; min-width:30px; text-align:right; flex:none;
}
.pick{flex:1;min-width:0}
.pick b{font-weight:600}
.pick span{color:var(--ink-2);display:block;font-size:13.5px;line-height:1.45}
.gap{color:var(--open);font-style:italic}
.note-static{
  margin-top:13px; padding:11px 13px; border-radius:7px;
  background:var(--surface-2); font-size:13.5px; color:var(--ink-2);
}
.note-static b{color:var(--ink);font-weight:600}
.subs{margin-top:11px;font-size:13px;color:var(--ink-3)}
.subs b{color:var(--ink-2);font-weight:600}
.jot{border-top:1px solid var(--line);margin-top:16px;padding-top:14px}
.jot label{
  display:block; font-size:11px; font-weight:600; letter-spacing:.07em;
  text-transform:uppercase; color:var(--ink-3); margin-bottom:6px;
}
.row{display:flex;gap:9px;flex-wrap:wrap;margin-bottom:9px}
select,textarea{
  font:inherit; color:var(--ink); background:var(--bg);
  border:1px solid var(--line); border-radius:6px; padding:8px 10px;
}
select{font-size:13.5px;flex:0 0 auto}
textarea{width:100%;min-height:76px;resize:vertical;font-size:14px;line-height:1.5}
select:focus-visible,textarea:focus-visible{outline:2px solid var(--accent);outline-offset:1px;border-color:var(--accent)}
.stamp{font-size:12px;color:var(--ink-3);margin-top:6px;min-height:1.3em}
.offline{
  background:var(--warn-soft); color:var(--warn); border-radius:7px;
  padding:11px 14px; font-size:13.5px; margin-bottom:20px;
}
@media (max-width:460px){
  .chead{flex-wrap:wrap}
  .rank{min-width:26px;font-size:17px}
}
@media (prefers-reduced-motion:reduce){*{transition:none!important;animation:none!important}}
/* ---- needs-your-call panel ---- */
.dpanel{
  background:var(--surface); border:1px solid var(--line); border-left:3px solid var(--open);
  border-radius:10px; box-shadow:var(--shadow); padding:16px 18px 6px; margin-bottom:22px;
}
.dpanel h2{
  font-family:"Barlow Condensed",Impact,sans-serif; font-weight:700; text-transform:uppercase;
  font-size:24px; line-height:1.1; margin:0 0 3px; letter-spacing:.005em;
}
.dcount{font-family:"IBM Plex Mono",ui-monospace,monospace;font-size:11.5px;color:var(--ink-3);margin-bottom:12px}
.dcount b{color:var(--open)}
.dall{color:var(--ok);font-weight:600}
.dec{border-top:1px solid var(--line);padding:13px 0 14px}
.dec:first-of-type{border-top:0;padding-top:4px}
.dechead{display:flex;gap:10px;align-items:baseline;flex-wrap:wrap}
.dectag{
  font-family:"IBM Plex Mono",ui-monospace,monospace;font-size:10.5px;letter-spacing:.04em;
  text-transform:uppercase;color:var(--ink-3);border:1px solid var(--line);
  border-radius:4px;padding:2px 6px;white-space:nowrap;
}
.dec h3{font-size:15px;font-weight:600;margin:0;line-height:1.3;flex:1;min-width:0}
.decwhy{color:var(--ink-2);font-size:13.5px;line-height:1.5;margin:6px 0 10px}
.opts{display:flex;flex-wrap:wrap;gap:7px;margin-bottom:8px}
.opt{
  font:inherit;font-size:13px;line-height:1.35;text-align:left;cursor:pointer;
  background:var(--bg);color:var(--ink);border:1px solid var(--line);border-radius:7px;
  padding:8px 12px;max-width:100%;
}
.opt:hover{border-color:var(--accent)}
.opt:focus-visible{outline:2px solid var(--accent);outline-offset:1px}
.opt[aria-pressed="true"]{background:var(--ok-soft);border-color:var(--ok);color:var(--ok);font-weight:600}
.opt .rec{font-size:11px;color:var(--ink-3);display:block;margin-top:1px;font-weight:400}
.opt[aria-pressed="true"] .rec{color:var(--ok)}
.decnote{width:100%;font-size:13.5px;margin-top:2px;padding:7px 10px;font:inherit;font-size:13.5px;color:var(--ink);background:var(--bg);border:1px solid var(--line);border-radius:6px}
.decnote:focus-visible{outline:2px solid var(--accent);outline-offset:1px;border-color:var(--accent)}
.decdone{
  background:var(--ok-soft);color:var(--ok);border-radius:6px;padding:8px 11px;
  font-size:13px;line-height:1.45;display:flex;gap:10px;align-items:baseline;flex-wrap:wrap;
}
.decdone b{font-weight:600}
.decundo{
  font:inherit;font-size:12px;cursor:pointer;background:none;border:0;padding:0;
  color:var(--ink-3);text-decoration:underline;margin-left:auto;
}
.decundo:hover{color:var(--ink)}
.dblocked{font-size:12.5px;color:var(--ink-3);margin:2px 0 10px}
@media (max-width:460px){ .opt{width:100%} }

</style>

<div class="wrap">
  <h1>LxthalFC Pack Notes</h1>
  <p class="sub">Seventeen packs from the September batch. All approved on 18 September. Each one shows the five as they stand. Write how the video actually came out underneath — it saves as you type and I read it back next session.</p>

  <div id="offline" class="offline" hidden>Notes aren't saving in this view — you're seeing the packs read-only. Open the artifact from your own gallery to write.</div>

  <div id="decisions"></div>

  <div class="tally" id="filters"></div>
  <div class="saveline" id="saveline"></div>
  <div id="list"></div>
</div>

<script>
const PACKS = [
  {id:"pace-abuser-2", title:"Top 10 Pace Abuser Moments Part 2", state:"locked",
   meta:"Your Pt1 5,382,421 · lane OG_Clips 14.6M @ 19.09× · runs 10→6 · SON NOW FULLY DESCRIBED",
   picks:[
    ["10","Son — the Burnley solo goal","278 likes, top named request on Pt1 — and it WON THE FIFA PUSKÁS AWARD, the only goal in either pack with a trophy"],
    ["9","Terens Puhiri — Borneo FC, Liga 1 Indonesia","OG_Clips ranks him #2 in a 14.6M video, above Mbappé and Bale"],
    ["8","Van de Ven — solo run for Spurs","Requested 3×; he's the cold open of your own Die for the Badge"],
    ["7","Adeyemi vs Chelsea","OG_Clips #7 — rounds Kepa, ends in a goal"],
    ["6","Bale vs Inter — Maicon","43 likes across 3 comments calling it the real number one"]],
   subs:"Dembélé v England 2017 · Hakimi v Alphonso Davies · Bellerín chasing Pedro",
   note:"<b>THE LINE NOBODY ELSE HAS: every one of these runs is ONE-FOOTED.</b> Son every touch right. Puhiri three, all right. Van de Ven five, all left. Adeyemi five, all left. At full sprint nobody switches feet. That came out of counting and it is genuinely yours.<br><br><b>[!!] SAY THE FOOT, NEVER THE NUMBER.</b> An earlier version of this note said \"Son takes nine touches\". Three separate passes over the same footage returned 9, 10 and 11–12, so the COUNT is not stable. The FOOT is — a dedicated tie-breaker on the clearest slow-motion angle graded all eight visible touches RIGHT and CERTAIN, with zero left-foot contacts, while admitting the angle cuts in mid-run. Repeat passes never once disagreed about which foot. The observation is safe; the arithmetic is not.<br><br><b>Son's entry, now described in full:</b> he picks it up 12–15 yards outside his OWN box, scans early (head left, then right), reads both lanes as covered and goes. Lowton lunges and is bypassed · Brady squeezes in, can't match him and VISIBLY GIVES UP · Mee and Tarkowski both retreat and converge and he goes BETWEEN them. Finishes right foot, inside/instep, low into the bottom right from about 13 yards. Cut on the ULTRA SLOW-MOTION HEAD-ON at 02:40–03:19 — the only angle that shows the feet well enough to carry the one-footed point.<br><br><b>Fix from the watch:</b> Traoré is at Fulham and Ederson saves it · Bale's defender is Bartra, not Boateng · Henry hits the post and does not score.<br><br><b>[!] No scorebug and no speed graphic</b> on Son, Puhiri or Van de Ven. Don't quote a distance or a top speed — only Adeyemi carries a readable clock."},
   {id:"oscar-2", title:"Top 5 Players Who Deserve The Oscar Award Part 2", state:"locked",
   meta:"Your Pt1 2,987,542 · 1,825 comments · no Part 2 exists",
   picks:[
    ["5","Neymar rolling — Mexico, 2018","Spawned a worldwide challenge; readable in a second"],
    ["4","Micah Richards","Requested twice (21 likes); he's a pundit so the clip travels"],
    ["3","Breel Embolo vs Argentina","\"He truly deserves the Oscar D'or\" (8) — most specific request"],
    ["2","Suárez holds his own teeth — the Chiellini bite, 2014","RESOLVED: the vague slot is filled. He bites Chiellini and then sits on the turf cupping his mouth and clasping his front teeth as if HE is hurt, then pulls his collar over his face. Referee gives nothing. Cannot be confused with Part 1’s PSG throat-clutch. ESPN broadcast, ITA 0-0 URU 78:25"],
    ["1","Rivaldo, 2002 vs Turkey","Ünsal sent off, FIFA fined him. Consensus GOAT of diving"]],
   subs:"Sterling (8) · the keeper who faked unconsciousness · Lazović, named correctly",
   note:"<b>[VERIFIED 19 Sep]</b> Embolo's red card is real and there is a far bigger story on it. 72nd min, Pinheiro books Paredes, VAR intervenes, Paredes' yellow rescinded, Embolo second yellow and off; Argentina win 3-1 in extra time. <b>Three weeks later IFAB said the VAR had no right to review it at all</b> — a caution that isn't a second yellow can only be reviewed for mistaken identity, not to change the offence. FIFA pushed back, saying the call “restored justice”. Nobody ranking dives has that ending. <b>I suggested Embolo to #4 and Richards to #3 — YOUR CALL, 20 Sep: keep the approved order. Embolo stays at #3; the IFAB ending is the script's job.</b><br><br><b>Never repeat:</b> the Lazović dive is 35 yards out, outside the box, nobody near him, play never stopped. Jota's opponent is Newcastle. Courtois is Atlético. Hundreds of RIP comments for Jota — don't reuse that clip mockingly."},

  {id:"penalty-2", title:"Worst Penalty Miss With Every Technique Part 2", state:"locked",
   meta:"\u2713 SETTLED \u2014 Budimir replaces Tah \u00b7 all five described \u00b7 no two failures alike",
   picks:[
    ["5","Zaza, Euro 2016 \u2014 STUTTER","About FOURTEEN tiny prancing high-knee steps, torso rigid, almost no ground covered \u2014 then one plant and a left-footed laces strike that balloons over. Neuer touches the crossbar to look bigger, dives low right, never gets near it"],
    ["4","Pires & Henry, Highbury \u2014 PASS \u2713 KEPT","22 Oct 2005, Arsenal 1-0 City, ~72nd min, REDCURRANT Highbury kit. Pires' studs SKIM THE TOP of the ball and it moves an inch. Distin hooks it clear, GRAHAM POLL gives an INDIRECT FREE KICK TO CITY. End on the Sparta Prague callback where Henry mimes it back at him"],
    ["3","Ag\u00fcero v Chelsea, Etihad \u2014 PANENKA","A genuine panenka chipped down the middle. \u00c9douard Mendy refuses to dive, stays on his feet, takes a half-step forward and CATCHES IT at chest height. Ag\u00fcero raises an apologetic hand"],
    ["2","Budimir v Valencia, 97th minute \u2705 IN, replacing Tah","He WON the penalty himself. Stutters to read Mamardashvili, and his STANDING LEG BUCKLES \u2014 knee sways out, balance gone, he stumbles forward over the ball and his left toe scuffs it. THE BALL NEVER LEAVES THE GRASS. It rolls at walking pace into the keeper's chest. Osasuna 0-1, 97th minute"],
    ["1","Eberechi Eze v PSG \u2014 SIDEFOOT, missed \u2014 destination DISPUTED","CL final shootout. \u26a0 It did NOT hit the crossbar. Beyond that the sources split: the match record says WIDE LEFT, three footage passes say OVER THE BAR. Say \u201che missed\u201d \u2014 nobody contests that. GABRIEL is the one who went over for certain, with Arsenal's fifth"]],
   subs:"Tah v Paraguay (powershot, over the bar) \u00b7 Gabriel (laces, over the bar) \u00b7 Yuri Alberto's cavadinha",
   note:"<b>\u2713 SETTLED, AND I MADE THE CALL RATHER THAN SENDING IT BACK. Budimir replaces Tah.</b><br><br><b>Why Tah and not one of the others \u2014 the argument is variety, not labels.</b> Zaza and Tah were the one duplicated MECHANISM in the pack: both lean back, both blaze it high over the bar. Your own variety rule says duplicates are defined by mechanism, not outcome, and those two were the pair. Taking Tah out removes the only repeat AND adds the one failure shape nothing else in the pack has. Zaza survives because his CAUSE is unique \u2014 the fourteen-step prancing run-up \u2014 not just his outcome.<br><br><b>What you now have is five completely different ways to fail:</b> a ball that never moves (Pires) \u00b7 a ball caught standing still (Ag\u00fcero) \u00b7 a ball that never leaves the floor (Budimir) \u00b7 a ball wide of the post (Eze) \u00b7 a ball in the crowd off a fourteen-step run-up (Zaza). <b>No two alike.</b> That is the strongest five this pack has had.<br><br><b>The cost, stated plainly:</b> POWERSHOT goes uncovered, so you mirror four of Part 1's five labels rather than all five. That is the right trade \u2014 Tah's label was the one built on a false premise anyway, since the \u201crun-up slip\u201d everyone repeats does not exist and two sources confirmed it. Tah drops to subs, so he is there if you disagree.<br><br><b>[!] SAY \u201cBUCKLES\u201d, NOT \u201cSLIPS\u201d on Budimir.</b> No divot, no torn turf, and the pass could not separate a real surface slip from a pure loss of balance. The honest version is better: he did it to himself.<br><br><b>The commentary is the caption, free:</b> \u201c<b>Nije ni \u0161utnuo!</b>\u201d \u2014 he didn't even take a shot. And your closing frame is Arrasate on the bench, chin on fist, saying nothing."},

  {id:"primes-redo", title:"Top 5 Shortest Lived Primes (2026 Redo)", state:"locked",
   meta:"Your Pt1 1,967,544 · 2,230 comments",
   picks:[
    ["5","João Félix","2,800 likes — most expensive teenager ever, Saudi league at 26"],
    ["4","Dele Alli","2,357 — two PFA Young Player awards, then out of football"],
    ["3","Andrey Arshavin","1,365 — four goals at Anfield, then gone"],
    ["2","Michu","167 — one season, eighteen goals, an ankle that never recovered"],
    ["1","Marco van Basten","~110 across three comments — three Ballon d'Ors, done at 28"]],
   subs:"Coutinho (64) · Ansu Fati · Andy Carroll (11)",
   note:"<b>Both Pt1 errors are burned into the captions,</b> not just the voiceover: <b>£80 MILLION</b> at 0:29 (Torres was £50m) and <b>2 BALLON D'ORS</b> at 1:18 (one, 2005). A re-voice won't fix them."},

  {id:"accidental-saves", title:"When Goalkeepers Make Accidental Saves", state:"locked",
   meta:"APPROVED with a known title-promise wobble · Reference 8,997,688 · runs 6→2 · BOTH OPEN SLOTS NOW FILLED, ALL NAMED AND WATCHED",
   picks:[
    ["5","Full Reverse Save","Championship, green kit. Dives forward onto his chest, BACK TURNED, ball off his trailing heel"],
    ["4","No-Look Save","Cardiff keeper at Swansea. Faces his own goal, ball off the back of his head and neck"],
    ["3","IDK Save","Brazilian league. Face-down after diving, ball off the post onto his back, sits up and catches it"],
    ["2","Manuel Neuer v Bas Dost — the heel he can't see","Neuer commits early, dives right, ends up FACE DOWN on the grass, beaten. Dost rolls it at the empty net and it hits the bottom of Neuer's trailing left boot, raised behind him. He is looking the other way and cannot see the ball"],
    ["1","Choupo-Moting stops his OWN team scoring","Nkunku chips the keeper, ball rolling over the line. Choupo-Moting runs in to tap it in for the glory, mistimes it completely — his left boot traps the ball dead ON the line and knocks it onto the post. On-screen caption in the source: \"200 IQ\""]],
   subs:"Zlatan (hands behind his back, never moves, ball off his calf) · Bendtner (blocks Fàbregas's goalbound shot with his shin, Wenger's hands on his head) · the referee in Liga MX",
   note:"<b>All five are now watched and named.</b> The two I've filled are the strongest of four accidental saves I confirmed frame-by-frame in a 4.58M goal-line compilation, plus a fifth from a Guardian clip.<br><br><b>#1 is the perfect finisher</b> — the declarative writes itself: he didn't save a goal, he saved the opposition. Commentary: \"He's blocked it on the line from his own player!\"<br><br><b>Three strong subs, any could swap in:</b> <b>Zlatan</b> stands beside the post with his HANDS BEHIND HIS BACK, never looks, ball off the back of his right calf — commentary calls him \"le capitaine Zlatan qui sauve son équipe\". <b>Bendtner</b> is offside in front of an open net trying to duck out of the way and blocks his own teammate. <b>The referee</b> — Óscar Macías, Cruz Azul v Toluca, sprinting toward the six-yard box with his back turned, ball off his right heel, keeper stranded on the floor; commentary: \"¡El árbitro es el héroe del Toluca!\" If you want a non-keeper spike, the referee is the funniest thing in the pack."},

  {id:"gk-assists", title:"Goalkeepers With Unbelievable Assists", state:"locked",
   meta:"All five from the official Premier League channel · RE-WATCHED CLIP BY CLIP · two corrections",
   picks:[
    ["5","Ederson → Agüero, Man City v Huddersfield","GOAL KICK, struck off the ground with the LEFT — a dead ball from inside his own six-yard box, flat and driven rather than lofted. Reported at 85–86 yards. Agüero rounds the onrushing keeper with a soft right-foot touch and CHIPS it left-footed into the empty net"],
    ["4","Alisson → Salah, Liverpool v Man United","DROP-KICK out of his hands, RIGHT foot — flat and fast, skimming over the retreating United players. One bounce. Salah starts inside his own half to stay onside, holds James off, and finishes with the INSIDE OF THE LEFT under de Gea"],
    ["3","Schmeichel → Solskjær, Man Utd v Sunderland","OVERHAND THROW, RIGHT arm, javelin style, clearing the halfway line on the fly. Kubicki misses the bounce completely, Solskjær is clean through and chips Pérez. The 1996 SD picture is part of the appeal — say the year"],
    ["2","Čech → Drogba, Wolves v Chelsea","DROP-PUNT out of his hands — LEFT foot, corrected. High and booming, climbing above the floodlights, the opposite shape to Alisson's. Drogba muscles straight past Berra, takes it round Hahnemann with the outside of the right and rolls it in"],
    ["1","Van der Sar → Rooney, Man Utd v Aston Villa","OPEN-PLAY BACKPASS, struck off the ground with the RIGHT — a rolling ball, three-step approach, NOT a dead ball. High and looping. Rooney cushions it right-footed and half-volleys it in off the instep. Then the ending: Ferdinand jogs the full length back to embrace him, and Evra leaps into his arms"]],
   subs:"Reina → Dossena at Old Trafford in the 4-1 (lob over Van der Sar) · Joe Hart → Antonio · Almunia → Fàbregas (a throw, and Fàbregas runs it 60 yards himself)",
   note:"<b>This pack was the shakiest, then the most solid, and it has now been corrected twice.</b> All five clips come from the Premier League's own 16-minute goalkeeper-assists compilation, each captioned on screen with keeper, fixture and season.<br><br><b>[!!] THE DELIVERY COUNT — read this before you script it.</b> The pack was first written as FIVE different deliveries. A pass over the footage cut that to THREE and told you to say three. A second, scoped pass per clip says <b>it is FOUR</b>, and that two deliveries had been wrongly grouped together. ONE: goal kick off the ground (Ederson, LEFT) — a dead ball, and the written record confirms it as a goal-kick assist. TWO: open-play backpass off the ground (Van der Sar, RIGHT) — a completely different act. THREE: drop-punt from the hands (Čech LEFT, Alisson RIGHT). FOUR: overhand throw (Schmeichel, RIGHT arm). <b>Say four.</b> Not three, not five. Note this also corrects an older note here that called Van der Sar's a free kick — it is open play.<br><br><b>THE LINE NOBODY ELSE HAS:</b> every method that appears twice is split by side. The two struck off the ground split left and right — Ederson LEFT, Van der Sar RIGHT. The two drop-punts split left and right — Čech LEFT, Alisson RIGHT. And Schmeichel is the outlier who never uses a foot at all.<br><br><b>Two corrections earned on the re-watch:</b> Čech's kicking foot is the LEFT, not the right — a dedicated tie-breaker graded it CERTAIN with the contact frame fully visible. And Ederson's is a GOAL KICK, not open play, confirmed in the written record.<br><br><b>What I had to drop, honestly:</b> <b>Neuer at Schalke</b> going up for a corner — searched hard, found nothing but FIFA and PES gameplay. I think I invented it. <b>Nicholas Hagen's punt</b> — same, unsourced. <b>Ederson → Haaland</b> exists but isn't in the official compilation.<br><br><b>[!] No scorebug on any of the five</b> — no clock and no score for any clip. Don't state a minute. And don't quote a distance for any of them except Ederson's, where 85–86 yards comes from the written record and should be attributed as reported.<br><br><b>[!] Alisson's famous run</b> — his length-of-the-pitch celebration is NOT in this source; it cuts at 00:11. You need a second clip if you want it."},
   {id:"another-nation", title:"Players Who Could've Played For Another Nation", state:"locked",
   meta:"Reference 4,105,413 @ 10.99× · pt2 2,085,039 @ 5.60× · ten pairings already used",
   picks:[
    ["5","Bukayo Saka — NIGERIA","Both parents Nigerian; Nigeria said they'd take him but wouldn't beg"],
    ["4","Michael Olise — ENGLAND","Eligible for FOUR nations. Southgate personally tried to flip him in 2022"],
    ["3","Alphonso Davies — LIBERIA","Born in the Buduburam refugee camp in Ghana; chose Canada"],
    ["2","Kylian Mbappé — ALGERIA","41 likes across four comments; the reference used him for Cameroon"],
    ["1","Lionel Messi — SPAIN","Pékerman: the paperwork was prepared for the U-20 World Cup. Messi: it never crossed my mind"]],
   subs:"Jamal Musiala, who turned down England AND Nigeria · Marc Guéhi, born in Abidjan · David Alaba",
   note:"<b>Ronaldo–Cape Verde is dead</b> — the link is a great-grandmother and FIFA Article 6.1 needs a parent or grandparent. <b>Steal the format:</b> six-slot tracker, five avatars plus a red ?, each face stamped with its flag on the beat drop."},

  {id:"transfers-almost", title:"Transfers That Almost Happened", state:"locked",
   meta:"All five researched against press sources · five different clubs, no repeats",
   picks:[
    ["5","Ronaldinho → Manchester United, 2003","He has said he was 48 HOURS from signing. United had just sold Beckham and wanted a replacement. He went to Barcelona and won the Ballon d'Or two years later"],
    ["4","Lewandowski → Blackburn Rovers, 2010","An ACT OF GOD stopped it — the Icelandic volcanic ash cloud grounded his flight to England. He has confirmed the story himself. He ended up at Dortmund, then Bayern"],
    ["3","Neymar → Real Madrid","Florentino Pérez has said publicly that Neymar PASSED A MEDICAL with Madrid before the Barcelona move. Neymar has separately said he nearly chose Bayern because of Guardiola"],
    ["2","Fekir → Liverpool, 2018","So far gone that he had already DONE THE CLUB INTERVIEWS in a Liverpool shirt. Collapsed at the medical over a knee. He has since accused Liverpool of making excuses"],
    ["1","De Gea → Real Madrid, 2015","Deadline day. The move died because the PAPERWORK WASN'T SUBMITTED IN TIME — the infamous fax. He stayed at United for eight more years"]],
   subs:"Kaká → Man City (the £100m deal Milan fans blocked) · Gerrard → Chelsea · Mbappé → Real Madrid, twice",
   note:"<b>\u2713 SETTLED: shoot it as the top-5, as built. I changed my mind and you should know why.</b> I had recommended splitting it into five single-story videos, on the grounds that twelve seconds a pick cannot carry a transfer saga. <b>That reasoning was wrong, and the error was mine:</b> I was importing the REFERENCE\u2019s story onto YOUR picks. The reference needed sixty-nine seconds because it is one story with a reversal \u2014 Moyes flies to Munich, sits on the couch, gets sacked. <b>Your five are not stories, they are one-line facts.</b> A volcano grounded the flight. The fax never sent. He had already done the club interviews. P\u00e9rez says he passed a medical. Forty-eight hours from signing. Every one of those is a punchline that lands in twelve seconds.<br><br><b>And switching format would not have fixed the proof problem anyway</b> \u2014 a single-story 70-second video is equally unproven on your channel, so I would have been trading a known format your audience expects for an unknown one, on the strength of someone else\u2019s reference. Ship the top-5. If it lands, expanding De Gea and the fax into its own video is a cheap follow-up.<br><br><b>The flag that remains is about precedent, not content.</b> All five picks are real, named and press-sourced. What failed validation was the REFERENCE, not the video.<br><br><b>[REF AUDIT — WRONG SHAPE]</b> The reference (0_yDGO1Jgt0) is not a top-5. It is one 69-second story about Toni Kroos to Man United — Moyes flying to Munich and sitting on his couch, then getting sacked three months later. No duplicate in your five, but twelve seconds a pick cannot carry a story like that. <b>My read at the time was to run it as one transfer per video — WITHDRAWN, see the top of this note: it ships as the top-5.</b><br><br><b>CORRECTION from the research:</b> I had Neymar → Man City. The stronger and better-sourced version is <b>Neymar → Real Madrid</b>, because Pérez himself has said Neymar passed a medical there. The Bayern/Guardiola version is also on the record from Neymar. Man City was the weakest of the three, so it's gone.<br><br><b>Five different clubs, as you asked</b> — United, Blackburn, Madrid, Liverpool, Madrid again. If the two Madrids bother you, Kaká to Man City swaps in cleanly at #3 and keeps one club per entry.<br><br><b>This is Type B</b> — no clips needed, and every line above traces to a press source rather than a comment."},

  {id:"signature-redo", title:"Top 10 Signature Moves (2026 Redo)", state:"locked",
   meta:"⚠ You published Part 2 on 1 June — 128,204 against Part 1's 1,580,732 · ALL 5 CLIPS NOW WATCHED",
   picks:[
    ["5","Robben's cut-in — vs Juventus","Two left-foot touches, Barzagli slips onto the turf, curled into the top corner past Buffon. Clean — no deflection, unlike the Man Utd one which nicks Vidić"],
    ["4","Ronaldinho's elástico — the nutmeg on Dunga","1999 Gre-Nal final, Grêmio v Internacional. Right foot: outside pushes it right, inside snaps it back — straight THROUGH Dunga's legs. Dunga (#8) left turned and stranded"],
    ["3","Iniesta's croqueta — vs Man City","Kompany (#4) charges out of defence, Iniesta shifts it right foot to left, Kompany wipes out flat on the grass. The referee has to jump out of the way"],
    ["2","Messi's body feint — the slow-mo breakdown","He never touches the ball. Drops the left shoulder, plants the left foot, defender's whole weight goes with it — THEN pushes it past the trailing leg with the outside of the left boot"],
    ["1","The Cruyff turn — Sweden, 1974","Cruyff (#14) winds up to cross, then drags it behind his own standing left leg with the INSIDE of his right boot. One touch. Olsson (#2) lunges, momentum takes him the wrong way. Cruyff reaches the byline and crosses"]],
   subs:"Quaresma's trivela · Robinho's stepovers · Okocha's rainbow flick",
   note:"<b>Script gift for #1 — Cruyff in his own words, on camera:</b> \"I never did tricks. I saw something and I did it and it just came out. There was an opponent there and I had to outplay him. So that was the easiest way, so you just do it.\" That is your hard declarative finisher.<br><br><b>Five different mechanics, no clash:</b> cut-and-curl · elástico nutmeg · two-footed shift · no-touch feint · drag behind the standing leg. Order is yours as approved — but Ronaldinho at #1 is arguable, since the source compilation's own title card calls it \"THE GREATEST piece of individual skill ever show[n]\".<br><br><b>Still true:</b> your Part 2 caption reads \"ANTHONY SPIN\" and the clip ends with Antony's pass rolling out for a throw-in v Sheriff Tiraspol."},

  {id:"badge-redo", title:"Top 5 Die for the Badge (2026 Redo)", state:"locked",
   meta:"\u26a0 You have six already \u00b7 ALL FIVE CLIPS WATCHED \u00b7 STONES KEPT AND NOW DESCRIBED",
   picks:[
    ["5","Valverde on Morata \u2014 114:29, Supercopa final, extra time","Morata clean through with 30m of grass and only Courtois to beat. Valverde's eyes never go near the ball \u2014 he scythes through both legs from behind. Straight red, no protest. SIMEONE PATS HIM ON THE HEAD as he walks off. Madrid win the shootout"],
    ["4","Van de Ven \u2014 Europa League final, Bilbao, 67:38","Vicario spills it, MAGUIRE heads at the empty net from six yards \u2014 Van de Ven hooks it away AIRBORNE with his left foot, an overhead scissor under the bar. Spurs win 1-0, first trophy in 17 years"],
    ["3","S\u00fcle \u2014 DORTMUND, not Bayern \u2014 v Mbapp\u00e9, 16:36","Mbapp\u00e9 rounds Kobel and shoots left-footed into an open net from seven yards. S\u00fcle has tracked back 30 metres, slides in on his back and hooks it over his own bar with his right leg in mid-air"],
    ["2","John Stones \u2014 off the line in front of Salah \u2713 YOUR CALL: KEPT","Mané hits the INSIDE OF THE POST \u00b7 Stones swings to clear and the ball SMASHES INTO EDERSON and rolls back at the empty net \u00b7 Stones dives across and hooks it off the line with the instep of the RIGHT boot, inches ahead of Salah \u00b7 then gets up and clears the SECOND ball too. He makes the save twice"],
    ["1","FERLAND Mendy vs Man City \u2014 not \u00c9douard","CL semi-final second leg, 86:11, Madrid 0-1 down and 3-5 on aggregate. Courtois beaten and on the floor, Grealish stabs it past him, Mendy sprints back from outside the box and hooks it off the line with an outstretched left boot"]],
   subs:"Kyle Walker (a sliding hook on Pulisic, and an overhead bicycle clearance) \u00b7 Boateng \u00b7 Tsimikas",
   note:"<b>\u2713 YOUR CALL: Stones stays.</b> He is your Part 1's #2 at the same rank and you have chosen to run it knowing that. <b>Frame it, don't hide it</b> \u2014 say \u201cyou've seen this one before, and it's still the best example there is\u201d in the first breath. The audience that spots repeats is the same one that rewards being told. He is now fully described from Man City's own channel.<br><br><b>[!!] THE NUMBER IS WRONG AND IT IS FREE REDO AMMUNITION.</b> Your Part 1 voiceover says <b>11.7mm</b>. An earlier note here said <b>11.2mm</b>. <b>Both are wrong.</b> Manchester City's own site: \u201cStones had somehow managed to ensure that 11 MILLIMETRES of the ball had not crossed.\u201d Sky Sports' own headline: \u201chow Etihad showdown and 11mm decided the 2018-19 title race.\u201d Two sources, one of them the club. <b>Say eleven millimetres, and put no decimal on screen</b> \u2014 a decimal is exactly what drags a correction comment.<br><br><b>[!] And the figure is not in the footage at all.</b> The Goal Decision System graphic in this cut shows only the words NO GOAL before cutting back to live play. If you put a number on screen you are adding it yourself.<br><br><b>[!!] The sequence was backwards in my old note.</b> I had written \u201cEderson's clearance rebounds off him\u201d. It is the other way round: <b>Stones swings to clear and the ball hits Ederson</b>, who is diving backwards, and comes off him towards the empty net.<br><br><b>S\u00fcle was NOT at Bayern.</b> Dortmund neon yellow, #25, and the man he denies is MBAPP\u00c9. German commentary: \u201cDer gr\u00f6\u00dftm\u00f6gliche Gr\u00e4tschmoment\u201d.<br><br><b>#5 has the best detail in the batch:</b> Valverde takes the red without a word, and as he passes the Atl\u00e9tico bench <b>Simeone reaches out and pats him on the head</b>. Italian commentary: \u201cSar\u00e0 rosso, ma \u00e8 una super giocata\u201d \u2014 and \u201cL'unico modo\u201d, the only way."},

  {id:"forgot-club", title:"Players We Always Forget Played for That Club", state:"noproof",
   meta:"⚠ No viral reference — best in lane 77,617 @ 0.34× · all five press-sourced",
   picks:[
    ["5","Andrea Pirlo at INTER MILAN","Before he was Pirlo, he was an Inter player. A brief stint where they never worked out what he was — then Milan moved him in front of the back four and he became the best deep playmaker alive"],
    ["4","Arjen Robben at CHELSEA","Three seasons at Stamford Bridge, 2004–2007, two Premier League titles — BEFORE Real Madrid and before Bayern. 1,889 likes on a comment asking for this"],
    ["3","Kevin De Bruyne at CHELSEA","Mourinho told him he was SIXTH CHOICE. De Bruyne says they spoke twice in total. Sold to Wolfsburg, came back to City and became the best midfielder in the league"],
    ["2","Thierry Henry at JUVENTUS","Signed in 1999, played out of position on the WING, gone in half a season. Arsenal bought him for less than Juventus paid"],
    ["1","Frank Lampard at MANCHESTER CITY","He scored against Chelsea. On loan. And REFUSED TO CELEBRATE — stood dead still with his arms up. Gary Cahill called it \"weird\". It denied Chelsea the win"]],
   subs:"Didier Drogba at Galatasaray · Ronaldo at PSV · Kaká at Orlando City",
   note:"<b>\u2713 COMPLETE AND SHOOTABLE \u2014 nothing is missing.</b> Five picks, all press-sourced, no placeholders. The flag means \u201cno format precedent\u201d, not \u201cbroken\u201d.<br><br><b>[REF AUDIT — LANE PROOF ONLY]</b> GT-1mKJRDxU is <b>your own</b> “Players We Always Call By Their Full Name”, 3,240,079 views — about names you can only say in full, not about forgetting a club. That one link is logged against <b>seven</b> different ideas. It proves the <i>lane</i>, not this title's mechanic. Shoot it if you want, but log it as riding lane proof. (Correction: I first wrote this was another creator's video. It is yours.)<br><br><b>Rebuilt with Salah-at-Chelsea tier names, as you asked.</b> Riquelme is gone — you were right that casual fans don't say that name out loud. Every one of these is a name people know attached to a club they've forgotten.<br><br><b>#1 is the best one because of the reaction, not the transfer.</b> Lampard scoring against the club he'd defined and then standing frozen with his arms up is a single readable image, which is what this format needs. Broadcast footage is on Man City's own channel.<br><br><b>#4 restored</b> — Robben at Chelsea came out during a revision and shouldn't have. A 1,889-like comment is a reason to include, not avoid.<br><br><b>Honest caveat on the lane:</b> best video in this lane is 77,617 against your 89k median. The names are now strong but the format has never gone big for anyone. Worth knowing before you spend a slot."},

  {id:"mispronounce", title:"Players We Always Mispronounce", state:"locked",
   meta:"\u2713 Three empty slots FILLED and verified \u00b7 no collision with Full Name Pt1's five",
   picks:[
    ["5","Khvicha Kvaratskhelia","Commentators gave up entirely and just say \u201cKvara\u201d. 30 likes in your comments. Babbel listed him among the trickiest names at the Euros and had to supply an audio clip because writing it out didn't work"],
    ["4","C\u00e9sar Azpilicueta \u2014 the one who got RENAMED \u2705 NEW","\u201cAth-pee-lee-KWE-ta\u201d. Nobody could say it, so Chelsea fans and teammates called him DAVE \u2014 for a decade, to his face, in songs. <b>Chelsea's own website tells the story of how the nickname started.</b> A Premier League captain got a new name because of a pronunciation"],
    ["3","Wojciech Szcz\u0119sny \u2705 NEW","\u201cVOY-check Sh-CHENS-ny\u201d, not \u201cWoj-chi-ech Shez-nee\u201d. Arsenal, Roma, Juventus, Barcelona \u2014 two decades at the top and the spelling alone is a visual gag. The \u0119 is a nasal vowel English has no equivalent for, which is why nobody lands it"],
    ["2","Thierry Henry","He says it differently depending on which language he is speaking \u2014 the man himself gives two answers. 49 likes"],
    ["1","Mesut \u00d6zil \u2014 and there are TWO right answers \u2705 NEW","Not \u201cOzzil\u201d. German is \u201cMAY-zoot UR-zil\u201d, IPA <b>[\u02c8me\u02d0zut \u02c8\u00f8\u02d0zil]</b>. Turkish is \u201cmeh-SOOT ur-ZEEL\u201d, IPA <b>[me\u02c8sut \u0153\u02c8zil]</b> \u2014 different stress in BOTH words. Born in Germany to a Turkish family, so both are correct and they are not the same. You watched him for a decade and never said it either way"]],
   subs:"Lamine Yamal (321) \u00b7 R\u00faben Dias (17) \u00b7 Sokratis Papastathopoulos \u00b7 \u0130lkay G\u00fcndo\u011fan (\u201cGUN-do-an\u201d, the \u011f is silent)",
   note:"<b>\u2713 YOUR CALL: fill them for me. Done \u2014 4, 3 and 1 are now real picks.</b><br><br><b>Every pronunciation above is sourced, not guessed.</b> \u00d6zil's two IPA renderings come from Wikipedia's own transcription. Szcz\u0119sny's phonetics come from a published list of names people get wrong. Azpilicueta's \u201cDave\u201d story is told on <b>Chelsea's official site</b>. Kvaratskhelia's is Babbel's Euros guide. In a pronunciation video the pronunciation IS the product, so none of this is from memory.<br><br><b>#1 is the hard declarative finisher</b> because \u00d6zil has <i>two</i> correct answers, German and Turkish, stressed differently, and most people never landed either. That's a better ending than \u201cthis one is hard\u201d.<br><br><b>#4 is the most engaging</b> because it isn't really about phonetics \u2014 it's about a man who got renamed. Dave is a genuinely funny payoff and the club documents it.<br><br><b>Checked against Full Name Pt1</b> (Nuno Mendes, Luis D\u00edaz, Rafael Le\u00e3o, Kroos, Ronaldo): <b>no collision on any of the five.</b> Different mechanic too \u2014 Full Name is names you can only say whole; this is names you say wrong.<br><br><b>[!] The Krease/Rolando evidence is still void</b> \u2014 that is your own caption bait, not real mispronunciation. Never build a pick on it.<br><br><b>[!] Lane caveat unchanged:</b> the reference is your own Full Name Pt1, which proves the lane, not this title."},

  {id:"blame-first", title:"Players We Always Blame First", state:"noproof",
   meta:"⚠ Football version flat — 369,137 @ 0.68× and 142,421 @ 0.26×",
   picks:[
    ["5","David Beckham, 1998","Sent off v Argentina, effigy hung outside a pub. He didn't concede the goals"],
    ["4","Bukayo Saka, Euro 2020","Nineteen, fifth penalty, racially abused for a shootout he was sent up last to take"],
    ["3","John Terry, 2008 final","Slipped on a waterlogged spot; Anelka still had to score after him"],
    ["2","Roberto Baggio, 1994","Dragged Italy to the final almost alone, missed one penalty, that's all anyone remembers"],
    ["1","Loris Karius, 2018 final","Concussed by Ramos's elbow, diagnosed days later, blamed for a decade"]],
   subs:"Moussa Sissoko · Sergio Ramos for Bale's exit · Fernando Torres at Chelsea",
   note:"<b>\u2713 COMPLETE AND SHOOTABLE.</b> Five picks straight from your own comments, no placeholders. The flag is about precedent, not content.<br><br><b>[REF AUDIT — LANE PROOF ONLY]</b> Same reference again — your own Full Name Pt1. Blame First runs on grievance; Full Name runs on a name test. Different engines, one inherited proof. The five picks are strong and come from your own comments — shoot it knowingly as lane-proof, not as a precedented format. Note: Full Name Pt2 did 449,749 against a 3.24M parent (0.14×).<br><br><b>The concept travels, the football execution didn't.</b> A hockey version of the same format did 200,711 @ 2.97× off an 18,400-sub channel; NBA 91.7k; college football 38.7k. Arguably your opening."},

  {id:"swap-nations", title:"What If Messi & Ronaldo Swapped Nationalities", state:"locked",
   meta:"Written from INSIDE the premise — Messi Portuguese, Ronaldo Argentine",
   picks:[
    ["5","Messi lifts the Euros in 2016","Portugal won that final with Ronaldo in tears on the touchline after 25 minutes. Messi is the one carried off instead — and Portugal still win, so he has a major trophy at 29 instead of 34"],
    ["4","Ronaldo plays in the 2022 World Cup final","Argentina get there and win it. He is 37 that December — exactly the age Messi was. The greatest final ever played becomes his"],
    ["3","Ronaldo finally wins a Copa América","Argentina won it in 2021 and again in 2024. His trophyless international record — the biggest stick used against him — disappears"],
    ["2","Messi's drought gets worse, not better","Portugal lost a Euro final in 2004 and a semi in 2012 before they won anything. Swap him in and he still spends a decade losing finals, just in a different shirt"],
    ["1","The GOAT argument ends on the day of the swap","Every single thing people argue about is national. Whoever gets Argentina wins a World Cup and a Copa. Whoever gets Portugal wins a Euro and a Nations League. The debate was never about the player"]],
   subs:"Messi never carries the Maradona comparison · Ronaldo inherits that weight instead · not one club trophy changes",
   note:"<b>[REF AUDIT — WRONG GENRE]</b> The reference (DZ2cXN-7GxE) is an <b>EA Sports FC console simulation</b> — Team Management screens, rating badges, group tables, controller prompts. It even admits rigging itself on camera: “I totally wasn’t forced to simulate until Mbappe scores and wins.” Your pack is a real-footage argument. The reference proves a <i>gameplay sim</i> of this premise travels, not an argument.<br><br><b>Written from inside the premise</b> — every entry states what WOULD happen, not what wouldn't. That was your fix on the Ronaldo one and it applies here too.<br><br><b>#1 is the hard declarative finisher</b> and it's the argument the video exists to make: nothing about their club careers changes at all. Every trophy that separates them is an international one.<br><br>The anchors underneath (2016 Euro final, 2022 World Cup final, Copa 2021 and 2024, Portugal's 2004 final) are all real results, so the speculation is built on facts rather than floating."},

  {id:"ronaldo-stayed", title:"What If Ronaldo Never Left Real Madrid", state:"locked",
   meta:"Five things that WOULD happen if he stayed — not 'without him', as you corrected",
   picks:[
    ["5","He passes 500 Real Madrid goals","He left on 450 in 438 games. Two more seasons near that rate and he's the first man to 500 for the club — a number nobody would ever touch"],
    ["4","Benzema never becomes the main man","Benzema spent nine years making space for Ronaldo. The moment Ronaldo left he became Madrid's leader and won a Ballon d'Or at 34. He doesn't get that if Ronaldo is still in front of him"],
    ["3","Madrid's three empty seasons look nothing alike","After he left they went three years without a Champions League having just won three in a row. That collapse is the strongest argument they sold him too early"],
    ["2","The Juventus experiment never happens","Juventus bought him to win a Champions League and went out earlier each year. That whole chapter — and the United return after it — only exists because he left"],
    ["1","The all-time record is bigger and it is not close","His goals-per-game at Madrid was the best of his career by distance. Every season there instead of anywhere else adds to a career record that is already the highest in the sport"]],
   subs:"No vacant shirt for Hazard to fail in · Madrid delay a galáctico signing by years · the 2018 final is his last act either way",
   note:"<b>[REF AUDIT — WRONG GENRE]</b> The reference (zilVLvf10Sk) is a <b>FIFA 19 Career Mode sim</b> on a modded save (Thiago Silva and Hamšík are in Barcelona's squad). Its own Copa del Rey screen contradicts itself — “Aggregate: 1-4” in the top bar, “Aggregate: 3-1” underneath. Same tell as the fake Eze penalty. No proof for a real-footage version.<br><br><b>Rewritten from inside the premise, as you asked.</b> Every entry names a thing that happens BECAUSE he stays. The old version kept describing Madrid without him, which as you said doesn't make sense for the title.<br><br><b>#5 is the hook because it's a number</b> — 450 in 438 is real, and it's the kind of stat a comment section argues about.<br><br>Anchors (450 goals, three straight Champions Leagues, the three-year drought, Benzema's Ballon d'Or at 34) are all real; the speculation sits on top of them."},

  {id:"psg-trio", title:"What If PSG Kept Messi, Neymar & Mbapp\u00e9", state:"locked",
   meta:"\u2713 Unverified stat DROPPED and re-ranked \u00b7 Penaltygate verified and added \u00b7 all five sourced",
   picks:[
    ["5","They once scored SIX between them in one game","Clermont 1\u20136 PSG. Mbapp\u00e9 hat-trick, Neymar hat-trick, and Messi a hat-trick of ASSISTS. Three hat-tricks in one match. Confirmed by Goal, CBS and ESPN"],
    ["4","They fell out over who takes penalties \u2014 in public \u2705 NEW","PSG 5-2 Montpellier, 13 Aug 2022, the first home game of the season. MBAPP\u00c9 MISSES a penalty. Afterwards NEYMAR LIKES tweets attacking the arrangement, one reading \u201cNow it's official, Mbapp\u00e9 is the one who takes penalties at PSG. Clearly it's a contract thing, because in no club in the world would Neymar be the second taker.\u201d The press called it Penaltygate; Galtier had to answer for it and so did the club president"],
    ["3","Messi won a Ballon d'Or as a PSG player","His 2021 award came after he had already signed. PSG have had a reigning Ballon d'Or winner on the pitch and still never won the thing they bought him for"],
    ["2","They never won a Champions League together","The entire point of the trio. Ligue 1 titles, no European Cup \u2014 and PSG finally won it after all three had gone"],
    ["1","All three were gone within two years","Messi to Miami, Neymar to Al-Hilal, Mbapp\u00e9 to Madrid. The most expensive front three ever assembled did not survive two full seasons"]],
   subs:"The 2022 Madrid collapse after leading the tie \u00b7 Mbapp\u00e9's \u201cit's a shame it's only happening now\u201d quote \u00b7 Ligue 1 titles with no European Cup",
   note:"<b>\u2713 YOUR CALL: drop the stat and re-rank. Done \u2014 and the pack is better for it.</b> The unverified \u201chow few games they started together\u201d line is gone. Everything else moved up one and a <b>verified</b> entry came in at #4.<br><br><b>The new #4 is the best entry in the pack.</b> Penaltygate is on the record with ESPN, Goal and Get French Football News, it has a date and a scoreline, and the evidence is <b>Neymar's likes</b> \u2014 which is a very modern, very readable beat. It is also the most argumentative entry, which is exactly where #4 belongs in your formula.<br><br><b>[!] Genre warning still stands.</b> The reference (kymTJlWMyzk) is an EA Sports FC sim, watermark ASP FC, only 4 of its 57 seconds real footage. All three What-If packs were sourced from sims \u2014 one mistake made three times. You have chosen to shoot these as a labelled experiment, so go in knowing the lane proof is for gameplay, not for argument.<br><br><b>Facts, not scenarios</b> \u2014 your correction, applied. Every line above traces to a press report. No clips needed."},
];

const DECISIONS = [
];

const STATES = {locked:["Locked","p-locked"], flag:["Needs a call","p-flag"], open:["Slots open","p-open"], noproof:["Shoot knowing","p-noproof"], fail:["Ref failed","p-fail"]};
const STATUS_OPTS = ["Not started","Scripted","Voiced","Edited","Published","Shelved"];

const list = document.getElementById("list");
const saveline = document.getElementById("saveline");
let filter = "all";

function esc(s){return String(s).replace(/[&<>"]/g,c=>({"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;"}[c]))}

function render(){
  list.innerHTML = "";
  PACKS.forEach((p,i)=>{
    const card = document.createElement("div");
    card.className = "card";
    card.dataset.state = p.state;
    card.hidden = filter !== "all" && filter !== p.state;
    const [label,cls] = STATES[p.state];
    const picks = p.picks.map(([r,t,d])=>
      `<li><span class="rank">${esc(r)}</span><span class="pick">${d===null?`<b class="gap">${esc(t)}</b>`:`<b>${esc(t)}</b>`}${d?`<span>${esc(d)}</span>`:""}</span></li>`
    ).join("");
    card.innerHTML = `
      <div class="chead">
        <div class="idx">${String(i+1).padStart(2,"0")}</div>
        <div class="ctitle"><h2>${esc(p.title)}</h2><div class="meta">${esc(p.meta)}</div></div>
        <div class="pill ${cls}">${label}</div>
      </div>
      <div class="body">
        <ol class="picks">${picks}</ol>
        ${p.subs && p.subs !== "—" ? `<div class="subs"><b>Subs</b> · ${esc(p.subs)}</div>` : ""}
        <div class="note-static">${p.note}</div>
        <div class="jot">
          <label for="s-${p.id}">How it came out</label>
          <div class="row">
            <select id="s-${p.id}" data-id="${p.id}" data-field="status">
              ${STATUS_OPTS.map(o=>`<option>${o}</option>`).join("")}
            </select>
          </div>
          <textarea id="n-${p.id}" data-id="${p.id}" data-field="note" placeholder="Views, what landed, what the comments said, what to change next time…"></textarea>
          <div class="stamp" id="t-${p.id}"></div>
        </div>`;
    list.appendChild(card);
  });
}

function renderFilters(){
  const counts = {all:PACKS.length, locked:0, flag:0, open:0, noproof:0, fail:0};
  PACKS.forEach(p=>counts[p.state]++);
  const defs = [["all",`All ${counts.all}`],["locked",`Locked ${counts.locked}`],["flag",`Needs a call ${counts.flag}`],["noproof",`Shoot knowing ${counts.noproof}`]];
  const box = document.getElementById("filters");
  box.innerHTML = defs.map(([k,l])=>`<button data-f="${k}" aria-pressed="${k===filter}">${l}</button>`).join("");
  box.querySelectorAll("button").forEach(b=>b.addEventListener("click",()=>{
    filter = b.dataset.f; renderFilters(); render(); if(db) paint();
  }));
}


// ---------- needs-your-call ----------
let decCache = {};
const decBox = document.getElementById("decisions");

function decRow(d){
  const row = decCache[d.id];
  const done = row && row.choice;
  const head = `<div class="dechead"><span class="dectag">${esc(d.pack)}</span><h3>${esc(d.title)}</h3></div>`;
  if(done){
    const when = row.resolvedAt ? new Date(row.resolvedAt).toLocaleDateString(undefined,{day:"numeric",month:"short"}) : "";
    const extra = row.note ? `<div style="width:100%;color:var(--ink-2);font-size:12.5px">${esc(row.note)}</div>` : "";
    return `<div class="dec" data-dec="${d.id}">${head}
      <div class="decdone" style="margin-top:8px"><b>${esc(row.choice)}</b>
        <span style="color:var(--ink-3);font-size:12px">${esc(when)}</span>
        <button class="decundo" data-undo="${d.id}">change</button>${extra}</div></div>`;
  }
  const opts = d.opts.map(([label,rec])=>
    `<button class="opt" data-pick="${d.id}" data-label="${esc(label)}" aria-pressed="false">${esc(label)}${rec?`<span class="rec">${esc(rec)}</span>`:""}</button>`
  ).join("");
  return `<div class="dec" data-dec="${d.id}">${head}
    <p class="decwhy">${esc(d.why)}</p>
    <div class="opts">${opts}</div>
    <input class="decnote" id="dn-${d.id}" data-decnote="${d.id}" placeholder="Or say it in your own words\u2026"></div>`;
}

function renderDecisions(){
  if(!DECISIONS.length){
    decBox.innerHTML = `<div class="dpanel" style="border-left-color:var(--ok)">
      <h2>Nothing needs your call</h2>
      <div class="dcount"><span class="dall">Every open decision is settled.</span> Anything new lands here.</div>
      <p class="dblocked">When something genuinely needs you, it appears at the top of this page with the
       options to tap. Right now there is nothing waiting.</p></div>`;
    return;
  }
  const open = DECISIONS.filter(d=>!(decCache[d.id]&&decCache[d.id].choice)).length;
  const total = DECISIONS.length;
  const counter = open === 0
    ? `<div class="dcount"><span class="dall">All ${total} resolved.</span> I pick these up next session.</div>`
    : `<div class="dcount"><b>${open}</b> of ${total} still open \u00b7 tap an answer and it saves</div>`;
  decBox.innerHTML = `<div class="dpanel">
      <h2>Needs your call</h2>${counter}
      <p class="dblocked">Everything blocking a pack lands here. Nothing else is waiting on you.</p>
      ${DECISIONS.map(decRow).join("")}
    </div>`;
}

function writeDecision(id, choice){
  const d = DECISIONS.find(x=>x.id===id); if(!d) return;
  const ta = document.getElementById("dn-"+id);
  const row = {pack:d.pack, question:d.title, choice:choice,
               note: ta ? ta.value : (decCache[id]&&decCache[id].note) || "",
               resolvedAt: choice ? Date.now() : null};
  decCache[id] = row;
  renderDecisions();
  if(!db) return;
  saveline.textContent = "Saving\u2026";
  db.doc("decisions/"+id).set(row)
    .then(()=>{ saveline.textContent = "All notes saved."; })
    .catch(()=>{ saveline.textContent = "That answer didn't save. Try again in a moment."; });
}

decBox.addEventListener("click", e=>{
  const pick = e.target.closest("[data-pick]");
  if(pick){ writeDecision(pick.dataset.pick, pick.dataset.label); return; }
  const undo = e.target.closest("[data-undo]");
  if(undo){ writeDecision(undo.dataset.undo, ""); }
});

renderDecisions();

renderFilters();
render();

let db = null, cache = {};
const timers = {};

function stampFor(id){
  const el = document.getElementById("t-"+id);
  if(!el) return;
  const row = cache[id];
  el.textContent = row && row.updatedAt ? "Saved " + new Date(row.updatedAt).toLocaleString() : "";
}

function paint(){
  PACKS.forEach(p=>{
    const row = cache[p.id]; if(!row) return;
    const s = document.getElementById("s-"+p.id), n = document.getElementById("n-"+p.id);
    if(s && row.status && document.activeElement !== s) s.value = row.status;
    if(n && typeof row.note === "string" && document.activeElement !== n) n.value = row.note;
    stampFor(p.id);
  });
}

function write(id){
  if(!db) return;
  const s = document.getElementById("s-"+id), n = document.getElementById("n-"+id);
  const row = {title:(PACKS.find(p=>p.id===id)||{}).title||id, status:s?s.value:"", note:n?n.value:"", updatedAt:Date.now()};
  cache[id] = row;
  saveline.textContent = "Saving…";
  db.doc("notes/"+id).set(row)
    .then(()=>{ saveline.textContent = "All notes saved."; stampFor(id); })
    .catch(()=>{ saveline.textContent = "That note didn't save. Try again in a moment."; });
}

function wire(){
  document.addEventListener("input", e=>{
    const id = e.target.dataset && e.target.dataset.id; if(!id) return;
    clearTimeout(timers[id]); timers[id] = setTimeout(()=>write(id), 700);
  });
  document.addEventListener("change", e=>{
    const id = e.target.dataset && e.target.dataset.id;
    if(id && e.target.tagName === "SELECT"){ clearTimeout(timers[id]); write(id); }
  });
}

claude.use("db").then(d=>{
  if(!d){ document.getElementById("offline").hidden = false; return; }
  db = d;
  d.collection("decisions").onSnapshot(snap=>{
    const docs = (snap && (snap.docs || snap)) || [];
    docs.forEach(doc=>{
      const key = (doc.id || "").replace(/^decisions\//,"");
      decCache[key] = doc.data ? doc.data() : doc;
    });
    renderDecisions();
  }, ()=>{});
  d.collection("notes").onSnapshot(snap=>{
    const docs = (snap && (snap.docs || snap)) || [];
    docs.forEach(doc=>{
      const key = (doc.id || "").replace(/^notes\//,"");
      cache[key] = doc.data ? doc.data() : doc;
    });
    paint();
    saveline.textContent = "All notes saved.";
  }, ()=>{ saveline.textContent = "Couldn't load saved notes."; });
  wire();
}).catch(()=>{ document.getElementById("offline").hidden = false; });
</script>
```

#### `system-page.html`
<!-- FILE: system-page.html · 44838 bytes · 520 lines · sha256 30ef60a77f701051efc06727b9b53a9df8c0510267866e41987d6c7bf61d1a86 -->
*Source of the system page artifact (Version 3, v1.1). 13 stages, QA gate section with the 22 Sep rows, error log E01–E24 with anchors, five patterns.*
```html
<title>LxthalFC Pack System</title>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Archivo:wght@500;600;700&family=Source+Serif+4:opsz,wght@8..60,400;8..60,600&family=JetBrains+Mono:wght@400;500&display=swap">
<style>
:root{
  --paper:#f2f3f0; --card:#fbfbfa; --sunk:#e9ebe6; --line:#d3d7cd;
  --ink:#14181b; --ink2:#4a5350; --ink3:#78827e;
  --acc:#0f6b52; --acc-soft:#dfece7;
  --gate:#8a6210; --gate-soft:#f6ecd6;
  --sig:#a63d1e; --sig-soft:#f7e4dd;
  --shadow:0 1px 2px rgba(20,24,27,.05),0 10px 28px rgba(20,24,27,.05);
}
@media (prefers-color-scheme:dark){:root:not([data-theme="light"]){
  --paper:#0d1113; --card:#151a1c; --sunk:#1b2124; --line:#2a3235;
  --ink:#e6eae8; --ink2:#a2aeaa; --ink3:#7a8683;
  --acc:#4fbd97; --acc-soft:#10281f;
  --gate:#dfa93f; --gate-soft:#2e2412;
  --sig:#e0806a; --sig-soft:#2f1a14;
  --shadow:0 1px 2px rgba(0,0,0,.4),0 10px 28px rgba(0,0,0,.3);
}}
:root[data-theme="dark"]{
  --paper:#0d1113; --card:#151a1c; --sunk:#1b2124; --line:#2a3235;
  --ink:#e6eae8; --ink2:#a2aeaa; --ink3:#7a8683;
  --acc:#4fbd97; --acc-soft:#10281f;
  --gate:#dfa93f; --gate-soft:#2e2412;
  --sig:#e0806a; --sig-soft:#2f1a14;
  --shadow:0 1px 2px rgba(0,0,0,.4),0 10px 28px rgba(0,0,0,.3);
}
*{box-sizing:border-box}
body{
  background:var(--paper); color:var(--ink);
  font-family:"Source Serif 4",Georgia,serif; font-size:16.5px; line-height:1.6;
  margin:0; padding-block:0 72px; padding-left:16px; padding-right:16px;
}
.wrap{max-width:820px;margin:0 auto}

/* masthead */
header.mast{padding-block:40px 20px;border-bottom:2px solid var(--ink)}
.eyebrow{
  font-family:"JetBrains Mono",ui-monospace,monospace; font-size:11px; letter-spacing:.16em;
  text-transform:uppercase; color:var(--acc); margin-bottom:10px;
}
h1{
  font-family:Archivo,system-ui,sans-serif; font-weight:700; font-size:clamp(34px,7vw,50px);
  line-height:1.02; letter-spacing:-.022em; margin:0 0 12px; text-wrap:balance;
}
.standfirst{font-size:18px;color:var(--ink2);margin:0;max-width:60ch}

/* laws */
.laws{display:grid;gap:12px;margin:26px 0 8px}
.law{
  background:var(--card);border:1px solid var(--line);border-left:3px solid var(--acc);
  border-radius:8px;padding:14px 16px;box-shadow:var(--shadow);
}
.law b{font-family:Archivo,sans-serif;font-weight:600;display:block;font-size:15px;margin-bottom:3px}
.law span{color:var(--ink2);font-size:15px}

/* stage nav */
nav.jump{
  position:sticky; top:env(safe-area-inset-top,0px); z-index:5;
  background:var(--paper); border-bottom:1px solid var(--line);
  padding-block:10px; margin-bottom:8px;
  display:flex; gap:6px; overflow-x:auto; scrollbar-width:thin;
}
nav.jump a{
  font-family:"JetBrains Mono",monospace; font-size:11.5px; text-decoration:none;
  color:var(--ink2); background:var(--sunk); border:1px solid var(--line);
  border-radius:5px; padding:4px 9px; white-space:nowrap; flex:none;
}
nav.jump a:hover{color:var(--ink);border-color:var(--acc)}
nav.jump a:focus-visible{outline:2px solid var(--acc);outline-offset:2px}

/* stages */
section.stage{padding-block:26px;border-top:1px solid var(--line)}
.shead{display:flex;gap:16px;align-items:baseline;margin-bottom:6px}
.snum{
  font-family:Archivo,sans-serif;font-weight:700;font-size:30px;line-height:1;
  color:var(--acc);font-variant-numeric:tabular-nums;flex:none;min-width:52px;
  letter-spacing:-.03em;
}
.stage h2{
  font-family:Archivo,sans-serif;font-weight:600;font-size:23px;line-height:1.15;
  margin:0;letter-spacing:-.012em;text-wrap:balance;
}
.purpose{color:var(--ink2);margin:0 0 14px;padding-left:68px}
@media(max-width:560px){.purpose{padding-left:0}.snum{font-size:24px;min-width:42px}}

.stage h3{
  font-family:Archivo,sans-serif;font-weight:600;font-size:13px;letter-spacing:.07em;
  text-transform:uppercase;color:var(--ink3);margin:18px 0 7px;
}
.stage p{margin:0 0 11px}
.stage ul{margin:0 0 11px;padding-left:20px}
.stage li{margin-bottom:6px}
.stage li::marker{color:var(--acc)}

code{
  font-family:"JetBrains Mono",ui-monospace,monospace;font-size:.85em;
  background:var(--sunk);border:1px solid var(--line);border-radius:4px;padding:1px 5px;
}
.calls{
  background:var(--sunk);border:1px solid var(--line);border-radius:8px;
  padding:12px 14px;margin:0 0 12px;
  font-family:"JetBrains Mono",monospace;font-size:12.5px;line-height:1.7;
  overflow-x:auto;
}
.calls div{white-space:nowrap}
.calls .c{color:var(--acc);font-weight:500}

.gate,.fail{border-radius:8px;padding:11px 14px;margin:12px 0;font-size:15px}
.gate{background:var(--gate-soft);color:var(--gate);border:1px solid currentColor}
.fail{background:var(--sig-soft);color:var(--sig);border:1px solid currentColor}
.gate b,.fail b{font-family:Archivo,sans-serif;font-weight:600;letter-spacing:.04em;font-size:12px;text-transform:uppercase;display:block;margin-bottom:3px}
.gate a,.fail a{color:inherit;font-weight:600}

.vocab{display:flex;flex-wrap:wrap;gap:5px;margin:0 0 12px}
.vocab span{
  font-family:"JetBrains Mono",monospace;font-size:11.5px;
  background:var(--card);border:1px solid var(--line);border-radius:4px;padding:3px 7px;color:var(--ink2);
}
.vocab span.key{border-color:var(--acc);color:var(--acc)}

table{width:100%;border-collapse:collapse;font-size:14.5px;margin:0 0 12px}
th,td{text-align:left;padding:7px 10px;border-bottom:1px solid var(--line);vertical-align:top}
th{font-family:Archivo,sans-serif;font-size:11.5px;letter-spacing:.06em;text-transform:uppercase;color:var(--ink3);font-weight:600}
td code{font-size:12.5px}
.tw{overflow-x:auto}

/* error log */
.err{border-top:1px solid var(--line);padding-block:14px}
.err:first-of-type{border-top:0}
.ehead{display:flex;gap:11px;align-items:baseline;flex-wrap:wrap}
.eid{
  font-family:"JetBrains Mono",monospace;font-size:11.5px;color:var(--sig);
  border:1px solid var(--sig);border-radius:4px;padding:2px 6px;flex:none;
}
.err h3{font-family:Archivo,sans-serif;font-weight:600;font-size:16px;margin:0;flex:1;min-width:0;letter-spacing:-.005em;text-transform:none;color:var(--ink);letter-spacing:0}
.estage{font-family:"JetBrains Mono",monospace;font-size:11px;color:var(--ink3)}
.err dl{margin:8px 0 0;display:grid;grid-template-columns:auto 1fr;gap:3px 12px;font-size:15px}
.err dt{font-family:Archivo,sans-serif;font-weight:600;font-size:11px;letter-spacing:.07em;text-transform:uppercase;color:var(--ink3);padding-top:4px}
.err dd{margin:0;color:var(--ink2)}
.err dd.rule{color:var(--ink);font-weight:600}
@media(max-width:560px){.err dl{grid-template-columns:1fr;gap:1px}.err dt{padding-top:7px}}

.patterns{background:var(--card);border:1px solid var(--line);border-radius:8px;padding:16px 18px;box-shadow:var(--shadow);margin-top:20px}
.patterns ol{margin:8px 0 0;padding-left:20px}
.patterns li{margin-bottom:7px;color:var(--ink2)}
.patterns li::marker{color:var(--sig);font-weight:600}

.runit{
  background:var(--ink);color:var(--paper);border-radius:10px;padding:18px 20px;margin-top:28px;
  font-family:"JetBrains Mono",monospace;font-size:13px;line-height:1.75;
}
.runit b{display:block;font-family:Archivo,sans-serif;font-size:11.5px;letter-spacing:.09em;text-transform:uppercase;opacity:.65;margin-bottom:8px;font-weight:600}
@media (prefers-reduced-motion:reduce){*{transition:none!important;animation:none!important}}
</style>

<div class="wrap">
<header class="mast">
  <div class="eyebrow">Operating system · v1.1 · 22 Sep 2026 · E17–E24 folded in</div>
  <h1>LxthalFC Pack System</h1>
  <p class="standfirst">Twelve stages from a blank slate to a shoot-ready pack, every one naming the
  exact call to make. Built from one seventeen-pack batch and the twenty-four errors it produced.</p>
</header>

<div class="laws">
  <div class="law"><b>1 · Decide by default</b><span>Escalate only a genuine fork — options genuinely close, and the choice taste rather than evidence. Everything else you decide, state the reasoning, and name the cost so it can be overruled in one tap. Flagging feels safe and is not: it moves the work to him.</span></div>
  <div class="law"><b>2 · Text wins on what happened. Footage wins on what is in the frame. Joel wins on how it looked.</b><span>Outcomes, dates, competitions, awards, rulings and the type of restart go to the written record before they are written down. Foot, kit, boards, angles and commentary come from the watch. Technique and whether it reads on camera are his.</span></div>
  <div class="law"><b>3 · Validate in the same kind as the output</b><span>A parse check is not a render check. A render check is not a click-through. If the output is a page, open it. If it is a PDF, render a page to an image and read it back.</span></div>
</div>

<nav class="jump" aria-label="Jump to stage">
  <a href="#s0">0 · Load state</a><a href="#s1">1 · Entry</a><a href="#s2">2 · Audit</a>
  <a href="#s25">2.5 · Route</a><a href="#s3">3 · Source</a><a href="#s4">4 · Watch</a>
  <a href="#s5">5 · Verify</a><a href="#s6">6 · Tie-break</a><a href="#s7">7 · Assemble</a>
  <a href="#s8">8 · Decide</a><a href="#s9">9 · Deliver</a><a href="#s95">9.5 · QA gate</a><a href="#s10">10 · Self-audit</a>
  <a href="#log">Error log</a>
</nav>

<section class="stage" id="s0">
  <div class="shead"><div class="snum">00</div><h2>Load state</h2></div>
  <p class="purpose">Always first, never skipped.</p>
  <div class="calls">
    <div><span class="c">get_channel_shorts</span>(channel_id) — refresh own.json, 459 entries</div>
    <div>read errors.md · queued.csv · rejected.json · dedup_base.json</div>
    <div>read the notes app db — collections <span class="c">notes/</span> and <span class="c">decisions/</span></div>
  </div>
  <p>Read <b>every entry</b> in the error log before doing anything else. Most of what follows exists because of one of them. Act on anything in <code>decisions/</code> answered since the last run.</p>
  <div class="gate"><b>Gate 0</b>You cannot proceed until the log is read and <code>own.json</code> is refreshed. <a href="#E01">E01</a> and <a href="#E02">E02</a> both happened because a catalogue check was skipped.</div>
</section>

<section class="stage" id="s1">
  <div class="shead"><div class="snum">01</div><h2>Entry point</h2></div>
  <p class="purpose">Two ways in. The system says which stages to skip.</p>
  <h3>1A — from nothing</h3>
  <div class="calls">
    <div><span class="c">search_viral_videos</span>(search=&lt;hook phrase&gt;, content_type="shorts") — several phrasings at once</div>
    <div><span class="c">get_youtube_video_data</span>(url, include_comments=true, max_comments=100) — every card kept</div>
    <div><span class="c">fetch_transcript</span>(ids) — batches up to 20 per call</div>
  </div>
  <p>FootyRanks and SantaBall catalogues first, then his own winners. Algrow search omits comment counts, so fetch them separately. Score with <code>score_engine.py</code>; prefer Algrow's real channel-relative <code>outlier_score</code> over the computed index.</p>
  <h3>1B — from picks in hand</h3>
  <p>Append <code>Title\nURL</code> pairs to <code>queued.csv</code> with today's date, push every non-picked title from that board to <code>rejected.json</code>, and go to Stage 2.</p>
  <div class="gate"><b>Gate 1</b>Discovery search runs before any shortlist, every video, no exceptions. Dedup at concept level against dedup_base ∪ rejected ∪ queued ∪ own. Count his existing versions — Die for the Badge had six; a seventh is a bad bet regardless of score.</div>
</section>

<section class="stage" id="s2">
  <div class="shead"><div class="snum">02</div><h2>Reference audit</h2></div>
  <p class="purpose">Eight checks, every one cheap, every one having caught a real failure.</p>
  <div class="calls">
    <div><span class="c">start_video_analysis</span>(url, media_resolution="default", prompt=&lt;audit&gt;) — 4+ in parallel</div>
    <div><span class="c">get_video_analysis_result</span>(job_id)</div>
  </div>
  <ol>
    <li><b>Rank-label overlap.</b> Is the pick's wording in the reference's own captions? Then it was transcribed, not chosen. A reference is a <i>format</i> source, never a <i>content</i> source.</li>
    <li><b>Structure.</b> Ranked countdown / single story / bracket / head-to-head / compilation. A pack inherits it or declares it is departing.</li>
    <li><b>Genre gate.</b> Gameplay sim is an automatic reject. This one check would have caught three failures in a single batch.</li>
    <li><b>Title-promise match.</b> Does it ask the <i>same</i> question? And any link appearing against more than one queued idea is unverified for all of them — one sat against seven.</li>
    <li><b>Lane proof is not format proof.</b> A big video in the right lane proves the lane, not the title.</li>
    <li><b>Visible-game-UI standard.</b> See Stage 4.</li>
    <li><b>Parent-number check.</b> List the parent's entries by name <i>and</i> moment. Same player different moment is fine; same moment is a re-cut.</li>
    <li><b>Title promise on each pick, no placeholders.</b> A striker under a goalkeeper title fails. A boot of noodles under a lookalikes title fails.</li>
  </ol>
  <p>Output one <code>refaudit/&lt;pack&gt;.md</code> per pack: what the reference actually contains, and the verdict.</p>
</section>

<section class="stage" id="s25">
  <div class="shead"><div class="snum">2.5</div><h2>Route the pack</h2></div>
  <p class="purpose">Decides whether Stages 3, 4 and 6 run at all.</p>
  <div class="tw"><table>
    <tr><th>Type</th><th>What it is</th><th>Route</th></tr>
    <tr><td><b>A</b></td><td>On-field moments — Signature Moves, GK Assists, Pace Abuser, Oscar, Badge, Penalty Miss, Accidental Saves</td><td>Full clip pipeline: Stages 3, 4, 6</td></tr>
    <tr><td><b>B</b></td><td>Facts, names, eligibility, transfers, what-ifs — Primes, Another Nation, Transfers, Forgot Club, Mispronounce, Blame First, PSG Trio</td><td><b>Skips describing entirely.</b> Watch references only for format. Straight to Stage 5</td></tr>
  </table></div>
  <p>Track progress as a count — Type A / Type B, done / remaining, and which specific clips are outstanding. He asks when a run feels long, and the honest answer is short.</p>
</section>

<section class="stage" id="s3">
  <div class="shead"><div class="snum">03</div><h2>Source the clip</h2></div>
  <p class="purpose">Never declare a moment unfindable after one search.</p>
  <div class="calls"><div><span class="c">youtube_search</span>(query, type="video", sort_by="view_count") — several angles at once</div></div>
  <ol>
    <li>Player + opponent + competition + action</li>
    <li><b>How a fan would phrase it</b> — surfaces the viral cut; formal phrasing surfaces the archive</li>
    <li>Official match highlights for that fixture</li>
    <li><b>The reference it came from</b> — three picks were written as "no clip found" while the frames sat in a Short already in hand</li>
    <li><b>Category compilations</b> — highest-value target. One official compilation verified five picks in a single pass</li>
    <li>Native-language phrasing for non-English leagues</li>
  </ol>
  <p><b>Keep queries to three or four words.</b> Long descriptive queries return zero. Prefer official league/club/federation → broadcaster → large clip channel → meme edit.</p>
  <div class="gate"><b>Gate 3</b>Only declare unsourceable after two distinct angles <b>and</b> a compilation search <b>and</b> a re-watch of the reference. If a search returns only gameplay, the moment probably is not real.</div>
</section>

<section class="stage" id="s4">
  <div class="shead"><div class="snum">04</div><h2>The watch</h2></div>
  <p class="purpose">One scoped pass per moment, not one per video.</p>
  <div class="calls"><div><span class="c">start_video_analysis</span>(url, media_resolution="default", prompt=&lt;scoped&gt;) — all in parallel</div></div>
  <div class="fail"><b>Cost — check the source duration, not the window</b>A pass bills on the whole video. A 16-minute compilation is ~15 credits per moment, so five moments in one compilation is ~75, not ~15. Quote the real number before spending. <a href="#E15">E15</a></div>
  <h3>The standing prompt asks for, by name</h3>
  <ol>
    <li>All on-screen caption text <b>exactly, character for character</b> — he plants misspellings as comment bait</li>
    <li>Shirt numbers <b>only where literally readable</b>, with "not legible" required otherwise</li>
    <li>The ranking number shown on screen</li>
    <li><b>How each clip ends</b> — and which corner</li>
    <li>Anywhere on-screen text contradicts the narration</li>
    <li><b>Commentary verbatim with timestamps</b> — the highest-value output of any watch. It names players, settles outcomes, and hands over captions free</li>
    <li>Real vs game vs fabricated, per segment</li>
    <li><b>An explicit CANNOT DETERMINE section.</b> Ask for it by name. A gap beats a confident error</li>
  </ol>
  <h3>Three modes — match the mode to the moment</h3>
  <ul>
    <li><b>Numbered beats with timestamps</b> where the sequence is the story — scrambles, deflections, goal-line pinball</li>
    <li><b>Named stations, no clock</b> where the event is under two seconds — receiving, the feint, the turn, the exit</li>
    <li><b>Hybrid</b> where there is both a technique and a sequence — dives, long runs, two-part events</li>
  </ul>
  <h3>One vocabulary, fixed</h3>
  <div class="vocab">
    <span>SOURCE</span><span class="key">AUTHENTIC</span><span>PICTURE</span><span>SCENE</span>
    <span>READ OFF THE KIT</span><span>BOARDS</span><span>CROWD</span><span>SCOREBUG</span>
    <span>BROADCAST GRAPHICS</span><span>OVERLAY</span><span>SPEED GRAPHIC</span>
    <span>DELIVERY / ACTION</span><span>CELEBRATION</span><span>CAMERA</span>
    <span>COMMENTARY</span><span>AUDIO</span><span class="key">CANNOT DETERMINE</span>
  </div>
  <p><code>BOARDS</code> is pitchside sponsors, <code>CROWD</code> is fan banners, <code>BROADCAST GRAPHICS</code> is the broadcaster's overlays and <code>OVERLAY</code> is the <i>publisher's</i> — the ones the editor must mask. The two keyed fields appear as labels in every file, never buried in prose.</p>
  <h3>Safe / soft / unsafe</h3>
  <ul>
    <li><b>Safe</b> — which foot, how it ends, on-screen text, commentary, kit, camera angles, whether play stopped</li>
    <li><b>Soft</b> — touch counts, steps, distances, timings. <b>Say the foot, never the number.</b> Son returned 9, then 10, then 11–12 across three passes; the feet never once disagreed</li>
    <li><b>Unsafe</b> — player identity and outcome. Run the ending check, then take conflicts to Stage 5</li>
  </ul>
  <h3>Is it a game? Unreliable in both directions</h3>
  <p>Official club, league and federation channels are trusted by default — a gameplay flag on one is the model being wrong. A call only counts with <b>visible game UI</b>: squad menus, rating cards, stamina bars, radar, controller prompts. Roster plausibility is worthless. A true positive looks like <b>a PS5 logo under the scoreline</b>.</p>
  <p><b>Fabricated</b> means game or doctored — catch it with a scoreboard that contradicts itself between two shots of the same passage. <b>Manipulated</b> means real footage padded by looping, scrubbing or speed change. Check whether a "long" moment is actually long.</p>
  <h3>Depth must be even</h3>
  <p>Measure it. One pack averaged 382 words a clip while another averaged 713 — and the thin one was the two-part goalkeeper pack that least deserved to be thin. If one clip is a third the length of its pack-mates, that is a gap, not a style.</p>
  <div class="gate"><b>Gate 4</b>Every pick has its own clip watched in <i>this</i> run. Never write a beat from a previous note — <a href="#E05">E05</a>. A comment can nominate a pick; only footage can confirm one.</div>
</section>

<section class="stage" id="s5">
  <div class="shead"><div class="snum">05</div><h2>Verify independently</h2></div>
  <p class="purpose">The stage that catches the worst errors. Do not hand him a question you could answer with a search.</p>
  <div class="calls"><div><span class="c">WebSearch</span> → <span class="c">WebFetch</span> the best source — the club's own site over an aggregator</div></div>
  <p>Everything in this list goes to the record <b>before</b> it is written down:</p>
  <ul>
    <li>The <b>type of restart</b> — goal kick, free kick, open play, corner <a href="#E04">(E04)</a></li>
    <li>Any <b>outcome</b> — scored, saved, wide, over, which post <a href="#E08">(E08)</a></li>
    <li>Any <b>number that will be spoken or appear on screen</b> <a href="#E06">(E06)</a></li>
    <li>Dates, competitions, fixtures, scorelines</li>
    <li>Any award, record or ruling</li>
  </ul>
  <div class="gate"><b>Gate 5</b>Every such claim carries a named source in the pack sheet. If a number is <i>not</i> in the footage, say so explicitly, so he knows he is adding it.</div>
</section>

<section class="stage" id="s6">
  <div class="shead"><div class="snum">06</div><h2>Tie-break</h2></div>
  <p class="purpose">When two passes disagree, a third scoped to the single clearest angle.</p>
  <p>Ask <b>only</b> the disputed question, and require four things: the answer; the visual evidence for it, naming which leg plants and which boot contacts; a grade of <b>certain / likely / unsure</b>; and whether the moment of contact is <i>actually visible</i> or obscured. Tell it plainly that an honest "cannot tell" is more useful than a confident guess.</p>
  <p>This settled Čech's kicking foot as left against an earlier pass that said right, and settled Son's feet while honestly reporting that the clearest angle starts mid-run.</p>
</section>

<section class="stage" id="s7">
  <div class="shead"><div class="snum">07</div><h2>Assemble</h2></div>
  <p class="purpose">The formula, and the checks that stop a pack repeating itself.</p>
  <p><b>5→1.</b> #5 proven hook · #4 most engaging or controversial · #3 engaging · #2 least engaging but proven · #1 conventional finisher, hard declarative. If Part 1 ran 5→1 under a "Top 10" title, <b>Part 2 runs 10→6</b>.</p>
  <p><b>Variety is judged on the footage, not the label.</b> Duplicates are defined by <i>mechanism</i>, not outcome — three penalties all ending over the bar can still be fine if one's cause is unique. When two picks share a mechanism, name the pair and drop one.</p>
  <p><b>Counting across a pack finds lines nobody else has.</b> "Every one of these runs is one-footed" came out of tallying feet across five clips. "Every delivery method that appears twice splits by side" came out of re-counting a taxonomy.</p>
  <div class="fail"><b>Test format fit against the picks, never the reference</b>Recommending a format change because the <i>reference</i> needed 69 seconds for one story — when the picks in hand were five one-line facts — was a real error. <a href="#E09">E09</a></div>
  <div class="tw"><table>
    <tr><th>Sequel penalty</th><th>n</th><th>Median</th></tr>
    <tr><td>Non-sequel</td><td>411</td><td>89,192</td></tr>
    <tr><td>"Part 2"</td><td>26</td><td>41,558</td></tr>
  </table></div>
  <p>Part 2s do less than half. Redo beats Part. Say this in any header containing a sequel.</p>
</section>

<section class="stage" id="s8">
  <div class="shead"><div class="snum">08</div><h2>Decide</h2></div>
  <p class="purpose">Law 1 lives here.</p>
  <p>For each open question, ask two things. <b>Are the options genuinely close?</b> If one is clearly better on evidence, decide it. <b>Is the choice taste or evidence?</b> Evidence is yours. Taste is his.</p>
  <p>When you decide: state the reasoning, name the cost plainly, and put the alternative in the subs so it reverses in one tap.</p>
  <p>When it <i>is</i> a genuine fork, it goes in the notes app's decisions panel — never only in chat, never only in a PDF, <b>and never in a calendar</b>. Two to four concrete, tappable options, never an open-ended question. Include the do-nothing option where one exists. Mark your recommendation once and leave it.</p>
  <div class="gate"><b>Always</b>Surface the app link in your reply every time something needs his input.</div>
</section>

<section class="stage" id="s9">
  <div class="shead"><div class="snum">09</div><h2>Deliver</h2></div>
  <p class="purpose">The app, the PDF, and three checks in this order.</p>
  <p>Status labels describe the <b>pack's readiness</b>, never the audit's verdict: <code>Locked</code> · <code>Needs a call</code> · <code>Shoot knowing</code> (complete, no format precedent) · <code>Slots open</code>.</p>
  <ol>
    <li><b>Parse</b> — eval the arrays with node before republishing. One broken quote blanks the page.</li>
    <li><b>Render and read it back</b> — <code>pdftoppm</code> a page to an image and open it. A parse check is not a render check <a href="#E11">(E11)</a>.</li>
    <li><b>Click through</b> — Playwright with the preinstalled Chromium, <code>window.claude</code> stubbed to an in-memory db. Screenshot at 390px and in dark mode.</li>
  </ol>
  <div class="fail"><b>Bound every in-place splice</b>Compute the array's start <i>and</i> end first, pass both to every find(), and recompute the end after each edit. An unbounded find jumped into the next array and produced an eighteenth pack. <a href="#E12">E12</a></div>
  <p>PDFs: reportlab + DejaVu. Strip emoji, CJK and Arabic — they render as empty boxes. <code>pypdf.extract_text</code> throws on subsetted DejaVu; ignore it and use <code>pdftotext</code>.</p>
</section>

<section class="stage" id="s95">
  <div class="shead"><div class="snum">9.5</div><h2>QA gate</h2></div>
  <p class="purpose">Runs before delivery, and it blocks. 592 checks, every one descended from a real error.</p>
  <div class="calls">
    <div><span class="c">python3 qa.py</span> &mdash; everything &middot; exit non-zero blocks delivery</div>
    <div><span class="c">python3 qa.py --pack</span> &lt;id&gt; &mdash; one pack</div>
    <div><span class="c">python3 qa.py --json</span> &mdash; machine-readable</div>
  </div>
  <p><b>Three severities.</b> <code>FAIL</code> blocks &mdash; nothing ships until it is fixed. <code>WARN</code> does not block, but <b>every warning must be acknowledged by name in the report</b>; silently passing one is the same as hiding it. <code>INFO</code> is a note, usually a soft figure that should stay out of the script.</p>
  <h3>What it checks</h3>
  <div class="tw"><table>
    <tr><th>Group</th><th>Checks</th><th>From</th></tr>
    <tr><td><b>Structure</b></td><td>Five picks per pack &middot; three subs &middot; every pick has an explanation line</td><td>&mdash;</td></tr>
    <tr><td><b>Placeholders</b></td><td>No &ldquo;In rework&rdquo; or &ldquo;Slot open&rdquo; in a pack marked locked, or in any live pick row</td><td>audit #8</td></tr>
    <tr><td><b>Coverage</b></td><td>Every Type A pick has a deep description that names it</td><td><a href="#E05">E05</a></td></tr>
    <tr><td><b>Labels</b></td><td>Every file carries <code>AUTHENTIC:</code> and <code>CANNOT DETERMINE</code> &middot; no bare label without a colon, which renders as body text instead of a label</td><td><a href="#E10">E10</a> <a href="#E11">E11</a></td></tr>
    <tr><td><b>Vocabulary</b></td><td>No banned variant &mdash; read off the shirts, fascia banners, fan banners, card graphics</td><td><a href="#E10">E10</a></td></tr>
    <tr><td><b>Soft figures</b></td><td>A touch, step or stride count stated without the instability caveat within 520 characters</td><td><a href="#E07">E07</a></td></tr>
    <tr><td><b>Spoken numbers</b></td><td>Any measurement in the production sheet with no source or caveat nearby &mdash; the sheet is what he reads out</td><td><a href="#E06">E06</a></td></tr>
    <tr><td><b>Depth</b></td><td>Any clip under half its pack&rsquo;s median word count</td><td>depth</td></tr>
    <tr><td><b>Cross-surface</b></td><td>App, final_packs.json and build_master.py must agree on pack ids &mdash; a missing entry is a build failure</td><td><a href="#E12">E12</a></td></tr>
    <tr><td><b>Sheet picks</b></td><td>Every pick name in final_packs.json appears in the data.py production sheet for that pack &mdash; the sheet is what he shoots from</td><td><a href="#E24">E24</a></td></tr>
    <tr><td><b>Type B sources</b></td><td>Every Type B pick has a source or an explicit from-comments marker; the count of unverified picks is reported</td><td><a href="#E22">E22</a></td></tr>
    <tr><td><b>Deliverable</b></td><td>No characters the PDF font cannot render</td><td>deliver</td></tr>
  </table></div>
  <h3>The adversarial pass &mdash; because self-grading is weak</h3>
  <p>The script catches what is mechanical. It cannot catch a wrong claim that is well-formed. So once the gate returns clean, spawn a subagent whose <i>only</i> job is to find faults:</p>
  <div class="calls" style="white-space:normal">Find what is wrong, not what is right. Does any description contradict itself? Is any outcome, date, competition, award or type of restart stated from footage rather than the written record? Is any number presented as fact the footage cannot support? Do two picks share a mechanism? Does any pick fail the title promise? Report only problems, with file and line, ranked by damage.</div>
  <p><b>A reviewer that reports nothing has not done its job</b> &mdash; send it back once with the weakest pick named. Anything it confirms goes into the log.</p>
  <div class="fail"><b>The rule this stage exists to enforce</b>A parse check is not a render check, and neither is a truth check. The three layers are mechanical, visual and adversarial. Running one and calling it QA is how <a href="#E11">E11</a> and <a href="#E16">E16</a> both shipped.</div>
</section>

<section class="stage" id="s10">
  <div class="shead"><div class="snum">10</div><h2>Self-audit</h2></div>
  <p class="purpose">Never skip. This is the part that makes the system improve.</p>
  <ul>
    <li><b>Paste the QA gate&rsquo;s own summary line</b> &mdash; passed / warnings / failures &mdash; then list <b>every warning by name</b> and say what you did about each. Report only the failures.</li>
    <li><b>List what you got wrong</b>, including anything corrected mid-run. What, why, and the rule that would have prevented it.</li>
    <li><b>Append each to the error log</b> with a new E-number. <b>If the error was mechanically detectable and the gate missed it, add a check for it to <code>qa.py</code> in the same breath</b> &mdash; that is how the gate gets stronger instead of staying still.</li>
    <li><b>Check for a new pattern.</b> The log names five. Say which this run's errors fit, or add a sixth.</li>
    <li><b>Propose the skill update</b> so the lessons survive a lost log.</li>
    <li><b>Report in plain prose</b> — what shipped, what you decided and why, what is genuinely waiting on him, and what you got wrong. Own errors out loud and say which part changed. Never quietly reissue.</li>
  </ul>
</section>

<section class="stage" id="log">
  <div class="shead"><div class="snum">24</div><h2>The error log</h2></div>
  <p class="purpose">Every entry is a real failure on a real batch. Read at Stage 0, appended at Stage 10.</p>

  <div class="err" id="E01"><div class="ehead"><span class="eid">E01</span><h3>Attributed his own video to a stranger</h3><span class="estage">Stage 2</span></div>
  <dl><dt>Why</dt><dd>Never checked own.json before attributing. The video was his own 3.24M hit.</dd>
  <dt>Rule</dt><dd class="rule">Before calling any video someone else's, grep own.json. A reference that looks like a stranger's can be his biggest hit in that lane.</dd></dl></div>

  <div class="err" id="E02"><div class="ehead"><span class="eid">E02</span><h3>Said no Part 2 existed when it did</h3><span class="estage">Stage 1, 7</span></div>
  <dl><dt>Why</dt><dd>Did not search his catalogue for the sequel before calling it a gap. It existed, at 0.14× the parent.</dd>
  <dt>Rule</dt><dd class="rule">Before proposing any sequel, list the parent's numbered entries and search own.json for an existing one.</dd></dl></div>

  <div class="err" id="E03"><div class="ehead"><span class="eid">E03</span><h3>Čech's kicking foot wrong</h3><span class="estage">Stage 6</span></div>
  <dl><dt>Why</dt><dd>One pass, on a wide angle where the contact was not clearly visible.</dd>
  <dt>Rule</dt><dd class="rule">When a foot or body-part call matters, run a second scoped pass on the closest replay, graded certain / likely / unsure, with a statement of whether contact was visible.</dd></dl></div>

  <div class="err" id="E04"><div class="ehead"><span class="eid">E04</span><h3>"Not a goal kick" — confidently wrong</h3><span class="estage">Stage 5</span></div>
  <dl><dt>Why</dt><dd>Vision described a dead ball inside the six-yard box and I overrode it with an assumption, writing the denial as a positive correction. Any football fan would have known instantly.</dd>
  <dt>Rule</dt><dd class="rule">Any claim about the type of restart goes to the written record first. The general law: errors cluster wherever the picture needed background knowledge underneath it.</dd></dl></div>

  <div class="err" id="E05"><div class="ehead"><span class="eid">E05</span><h3>Described a sequence backwards</h3><span class="estage">Stage 4</span></div>
  <dl><dt>Why</dt><dd>Wrote the beat from memory of an earlier pack note rather than from a watch.</dd>
  <dt>Rule</dt><dd class="rule">Never write a beat from a previous note. Every described beat traces to a watch in this run.</dd></dl></div>

  <div class="err" id="E06"><div class="ehead"><span class="eid">E06</span><h3>Three millimetre figures, two of them wrong</h3><span class="estage">Stage 5</span></div>
  <dl><dt>Why</dt><dd>Part 1 says 11.7mm, my note said 11.2mm, and the club's own site and Sky's own headline both say 11mm. The figure appears nowhere in the footage.</dd>
  <dt>Rule</dt><dd class="rule">Any number that will appear on screen or be spoken gets a named source. If it is not in the footage, say so, so he knows he is adding it.</dd></dl></div>

  <div class="err" id="E07"><div class="ehead"><span class="eid">E07</span><h3>Touch counts treated as fact</h3><span class="estage">Stage 4, 6</span></div>
  <dl><dt>Why</dt><dd>Treated a soft field as a safe one. Three passes returned 9, 10 and 11–12; the pack's headline said "nine".</dd>
  <dt>Rule</dt><dd class="rule">Say the foot, never the number. Same for distances, step counts and durations.</dd></dl></div>

  <div class="err" id="E08"><div class="ehead"><span class="eid">E08</span><h3>Two vision passes agreed and both were wrong</h3><span class="estage">Stage 5</span></div>
  <dl><dt>Why</dt><dd>Used footage to settle an outcome. Both said crossbar; the shootout record says wide left.</dd>
  <dt>Rule</dt><dd class="rule">Never let two agreeing vision passes stand in for a record check — they can agree and both be wrong.</dd></dl></div>

  <div class="err" id="E09"><div class="ehead"><span class="eid">E09</span><h3>Imported the reference's story onto his picks</h3><span class="estage">Stage 7</span></div>
  <dl><dt>Why</dt><dd>Recommended splitting a pack because twelve seconds cannot carry a saga — but the saga was the reference's, and his five picks were one-line facts.</dd>
  <dt>Rule</dt><dd class="rule">Test format fit against the picks in hand, never against what the reference contained. A reference is a format source, not a content source — and that cuts both ways.</dd></dl></div>

  <div class="err" id="E10"><div class="ehead"><span class="eid">E10</span><h3>Label drift made the notes unscannable</h3><span class="estage">Stage 4</span></div>
  <dl><dt>Why</dt><dd>Same field under different names across fourteen files — kit vs shirts, boards vs fascia banners, authentic vs real broadcast.</dd>
  <dt>Rule</dt><dd class="rule">One fixed vocabulary. Substance being right is not enough if the reader cannot scan for it.</dd></dl></div>

  <div class="err" id="E11"><div class="ehead"><span class="eid">E11</span><h3>Reintroduced the defect I had just fixed</h3><span class="estage">Stage 9</span></div>
  <dl><dt>Why</dt><dd>Wrote new files in a style the renderer did not expect, then validated by parsing instead of rendering.</dd>
  <dt>Rule</dt><dd class="rule">A parse check is not a render check. Render a page to an image and read it back before sending.</dd></dl></div>

  <div class="err" id="E12"><div class="ehead"><span class="eid">E12</span><h3>A splice ran past the array boundary</h3><span class="estage">Stage 9</span></div>
  <dl><dt>Why</dt><dd>An unbounded find on a delimiter shared by two adjacent arrays ate a closing bracket and produced an eighteenth pack.</dd>
  <dt>Rule</dt><dd class="rule">Bound every in-place splice to the array being edited. Compute start and end first, pass both to every find, recompute after each edit.</dd></dl></div>

  <div class="err" id="E13"><div class="ehead"><span class="eid">E13</span><h3>Over-escalated decisions</h3><span class="estage">Stage 8</span></div>
  <dl><dt>Why</dt><dd>Put eight calls to him, several with a clear recommendation I could have acted on — then created two more from his answers.</dd>
  <dt>Rule</dt><dd class="rule">Decide by default. Escalate only a genuine fork. Flagging feels safe and is not: it moves the work to him.</dd></dl></div>

  <div class="err" id="E14"><div class="ehead"><span class="eid">E14</span><h3>Read "appointment" as a calendar event</h3><span class="estage">Stage 8</span></div>
  <dl><dt>Why</dt><dd>Took the most literal reading of an ambiguous word without checking which tool fit his setup.</dd>
  <dt>Rule</dt><dd class="rule">When an instruction could mean a tool he already uses or one he does not, assume the one already in the workflow.</dd></dl></div>

  <div class="err" id="E15"><div class="ehead"><span class="eid">E15</span><h3>Under-quoted credits by six times</h3><span class="estage">Stage 4</span></div>
  <dl><dt>Why</dt><dd>Assumed the window length drove the cost. A scoped pass bills on the whole source video.</dd>
  <dt>Rule</dt><dd class="rule">Check the source duration, not the window, before quoting. Correct an estimate out loud the moment it moves.</dd></dl></div>

  <div class="err" id="E16"><div class="ehead"><span class="eid">E16</span><h3>A label made finished work look broken</h3><span class="estage">Stage 9</span></div>
  <dl><dt>Why</dt><dd>Three complete packs sat under a red "Ref failed" pill, which described the reference's verdict rather than the pack's state.</dd>
  <dt>Rule</dt><dd class="rule">A status label describes the pack's readiness, never the audit's verdict. "Shoot knowing" is a different state from "blocked" and must look different.</dd></dl></div>

  <div class="err" id="E17"><div class="ehead"><span class="eid">E17</span><h3>Fixed a defect in three files and called it fixed</h3><span class="estage">Stage 7</span></div>
  <dl><dt>Why</dt><dd>The bare-label defect was corrected in the three files I had just written; QA then found 39 more instances across 14 files. A local fix felt like a fix.</dd>
  <dt>Rule</dt><dd class="rule">A correction is not done until it is grep-confirmed absent from every surface. Fix by pattern across the whole tree, then prove it with a search, not memory.</dd></dl></div>

  <div class="err" id="E18"><div class="ehead"><span class="eid">E18</span><h3>A stale audit contradicted a filled pack three pages later</h3><span class="estage">Stage 7</span></div>
  <dl><dt>Why</dt><dd>The reference audit still said “mispronounce IS NOT FINISHED” after the three empty slots had been filled on Joel’s instruction.</dd>
  <dt>Rule</dt><dd class="rule">When a pack changes, re-date every audit note it supersedes: [RESOLVED &lt;date&gt;]. Old verdicts do not expire on their own.</dd></dl></div>

  <div class="err" id="E19"><div class="ehead"><span class="eid">E19</span><h3>The first QA gate was mis-calibrated and cried wolf</h3><span class="estage">Stage 9.5</span></div>
  <dl><dt>Why</dt><dd>73 warnings on the first run, most of them footage measurements inside deep files that were never going to be spoken. A gate that fires on everything gets ignored.</dd>
  <dt>Rule</dt><dd class="rule">Measurements inside deep/ are INFO (a record); in data.py they are WARN (spoken). The count caveat window is 520 characters and the caveat regex is broad. Calibrate against the last clean batch before trusting a count.</dd></dl></div>

  <div class="err" id="E20"><div class="ehead"><span class="eid">E20</span><h3>Over-corrected, and stated a disputed outcome as settled fact</h3><span class="estage">Stages 5, 7</span></div>
  <dl><dt>Why</dt><dd>Wrote that Eze’s penalty “went WIDE LEFT — the record says so” as settled. A third footage pass said over the bar, agreeing with the two I had overruled; TNT’s commentary says only “missed”.</dd>
  <dt>Rule</dt><dd class="rule">Law 2 ranks which source outranks which; it does not make one source certain. One text source against three passes is a CONFLICT to record, not a verdict. Say DISPUTED, give both readings, give the safe wording (“he missed”), and check the variety knock-on downstream.</dd></dl></div>

  <div class="err" id="E21"><div class="ehead"><span class="eid">E21</span><h3>Thirty-five clips had no single place listing where they live</h3><span class="estage">Stages 4, 9</span></div>
  <dl><dt>Why</dt><dd>Source ids and windows were scattered across fourteen deep files; Eze’s had no window anywhere. Descriptions were written to be read, not cut from.</dd>
  <dt>Rule</dt><dd class="rule">Every Type A pick gets a source id, link, in/out window and cut-on angle in clips.py as its description is written. The manifest ships as Part 5.5 of the send-off and as a CSV.</dd></dl></div>

  <div class="err" id="E22"><div class="ehead"><span class="eid">E22</span><h3>Nine packs had picks but no verification layer</h3><span class="estage">Stages 2.5, 5</span></div>
  <dl><dt>Why</dt><dd>Type B packs shipped with one line per pick and nothing behind it; 20 of 45 rested on Joel’s own comments. “Skips describing” had slid into “skips verifying”.</dd>
  <dt>Rule</dt><dd class="rule">Type B’s equivalent of a description is a SOURCED FACT. Every Type B pick carries its source in typeb.py or an explicit C (from comments) marker. Verify quotes, fees and precise numbers first.</dd></dl></div>

  <div class="err" id="E23"><div class="ehead"><span class="eid">E23</span><h3>“Retired at 28” would have been wrong by two years</h3><span class="estage">Stage 5</span></div>
  <dl><dt>Why</dt><dd>Van Basten’s last match was at 28 (1993 CL final) but he formally retired on 17 August 1995 aged 30. “Done at 28” survives; “retired at 28” does not.</dd>
  <dt>Rule</dt><dd class="rule">When a career fact has two candidate dates — last appearance vs retirement, signed vs debuted — record BOTH and say which you mean. The gap is usually the better story.</dd></dl></div>

  <div class="err" id="E24"><div class="ehead"><span class="eid">E24</span><h3>The production sheet still had a replaced pick two days later</h3><span class="estage">Stages 7, 9.5</span></div>
  <dl><dt>Why</dt><dd>data.py’s Penalty Part 2 sheet — the page Joel shoots from — still listed Tah at #2 after Budimir replaced him in the app, the JSON, the manifest and the deep files. The cross-surface check compared pack ids, not pick names.</dd>
  <dt>Rule</dt><dd class="rule">A pick change is grep-confirmed absent from every surface before it is called done. QA now compares pick NAMES between final_packs.json and the data.py sheet and fails on a mismatch.</dd></dl></div>

  <div class="patterns">
    <b style="font-family:Archivo,sans-serif;font-size:12px;letter-spacing:.08em;text-transform:uppercase;color:var(--ink3)">The five patterns underneath the twenty-four</b>
    <ol>
      <li>Errors cluster where the picture needed <b>background knowledge</b> under it. <i>(E04, E06, E08, E20, E23)</i></li>
      <li>Repeat passes agree on <b>what is in frame</b> and disagree on <b>counts</b>. <i>(E03, E07)</i></li>
      <li>Writing from a previous note rather than a fresh watch <b>propagates errors</b>. <i>(E05, E09, E17, E18, E24)</i></li>
      <li>Validation that is not the <b>same kind</b> as the output misses defects. <i>(E11, E12, E19, E22)</i></li>
      <li>Flagging feels safe and is not — it <b>moves the work to him</b>. <i>(E13, E16)</i></li>
    </ol>
  </div>
</section>

<div class="runit">
  <b>Run it</b>
  Run the LxthalFC pack system on &lt;packs / this picker paste / these reference links&gt;.<br>
  Start at Stage 0 and work through to Stage 10. Decide by default; only genuine forks go in the app.<br>
  Report failures and what you got wrong, not a wall of passes.
</div>
</div>
```

### 6.5 The deep descriptions (Type A) — 18 files

#### `deep/acc-1-choupo.md`
<!-- FILE: deep/acc-1-choupo.md · 3397 bytes · 52 lines · sha256 0c1d49fdfe8ef990e7a8a9a3c1e72e7dc84292dc4317bfca5f07bd83f405c284 -->
*Vocabulary-normalised and colon-ified 21 Sep; carries AUTHENTIC: and CANNOT DETERMINE.*
```markdown
# DEEP PASS — ACCIDENTAL SAVES #1 "Choupo-Moting stops his own team scoring"
SOURCE: PaaZxPh0A-o "Legendary Goal Line Saves" at 05:05–05:19.
AUTHENTIC: real broadcast, no game UI.
Ligue 1, PSG v Strasbourg. Night match under floodlights.

*** THE COMMENTARY IS THE CAPTION — take it verbatim ***
 English, two voices:
  Lead: "...chance, little chip... oh Choupo-Moting has hit the post from an inch out!"
  Co-comm: "He's kept it out, Jonathan! He's blocked it on the line from his own player!"
  Lead: "He's going in..."

SCENE: PSG home: dark navy shirts with tonal red central detailing, navy shorts, navy socks.
  READ OFF THE KIT: "#17 CHOUPO-MOTING" white lettering on the back · "#24 NKUNKU" in PINK/RED font
  on the back. Chest sponsor not legible at broadcast distance.
 Strasbourg away: white shirts with subtle blue and red accents, white shorts, white socks.
  Defender #13 visible sliding in.
 Strasbourg goalkeeper MATZ SELS: ORANGE/SALMON long sleeve, orange shorts, orange socks.
 Referee not legibly visible.
 Green, manicured, dry pitch.
 BOARDS: ROSA PARKS · BHV MARAIS · #VisitQatar · ACCOR LIVE LIMITLESS · boulanger.
 Live scorebug is CROPPED OUT by the compilation editor.
 Compilation overlays: a YELLOW INVERTED TRIANGLE labelled "200 IQ" sitting above Choupo-Moting at
 05:05–05:06 · "Score 90' QUALITY FOOTBALL VIDEOS" bottom-left · "YOUTUBE.COM/SCORE90" top-right ·
 a "PSG FANS" graphic on the final meme cut.

ACTION: 1. NKUNKU (#24) breaks behind the Strasbourg line into the right channel of the box. Sels charges out.
 2. Nkunku gets there first and lofts a delicate CHIP with his RIGHT FOOT over the sliding keeper.
 3. The ball floats cleanly past the beaten keeper and is bouncing toward the EMPTY NET between the posts.
 4. CHOUPO-MOTING (#17) is sprinting along the goal line toward the left post (attacking perspective).
    As the ball is about to cross, he reaches for it, facing partially SIDEWAYS toward the pitch.
 5. THE BLOCK: he extends his LEFT FOOT and touches/drags the ball right on the white line, completely
    arresting its momentum. It stops dead, ricochets off the base of the upright, and rolls back out
    toward the field of play.
 6. Strasbourg's #13 and Sels scramble back and clear. A certain goal has become a goal-line clearance
    made against his own team.

CAMERA — four cuts, and the second one is the gift
 1. 05:05–05:08 high wide sideline through the chip and the block.
 2. 05:09–05:10 *** CUT TO THE PSG BENCH: a tight medium shot of KYLIAN MBAPPÉ, wide-eyed, mouth open,
    staring in disbelief. *** That reaction shot is the single best edit beat in this pack.
 3. 05:11–05:15 LOW-ANGLE SLOW MOTION from behind the line at the base of the post, showing exactly how
    the left boot stopped it inches short and put it onto the post.
 4. 05:16–05:19 the compilation splices in a meme clip of an enraged fan punching through a flat-screen
    TV with a beer can in hand, a PSG badge edited over his head. Not broadcast footage — do not use it
    as if it were.

CANNOT DETERMINE
 The exact clock and scoreline (scorebug cropped). Whether offside was eventually given — the clip cuts
 before the restart. PSG chest sponsor lettering.

STANDING NOTE: he is a striker, not a goalkeeper. You accepted that knowingly. The title promise is
still the weak point of this pack, not the footage.
```

#### `deep/acc-2-neuer.md`
<!-- FILE: deep/acc-2-neuer.md · 5689 bytes · 84 lines · sha256 3d2aad2a3564e2277b8df5adf913003295b926ac8b22af3be4f7e16c4c24c0fd -->
*Rewritten 21 Sep to ~986 words in the consistency pass.*
```markdown
# DEEP PASS — ACCIDENTAL SAVES #2 "NEUER v BAS DOST"

SOURCE: PaaZxPh0A-o "Legendary Goal Line Saves" at 02:00-02:08.
AUTHENTIC: real broadcast, no game UI, no splicing. Multi-camera professional coverage with a
 proper in-goal replay camera, which no fabricated clip would have.
OVERLAY: must be masked
 "Score 90 — QUALITY FOOTBALL VIDEOS" graphic bottom left for the whole clip, and a faint
 "YOUTUBE.COM/SCORE90" top right. Both are the publisher's, not the broadcaster's.
SCOREBUG: NONE. No clock, no score.

*** BAS DOST IS CONFIRMED BY THE COMMENTARY ITSELF — no inference needed ***
 English commentary, verbatim: "Oh, Bas Dost! Bas Dost! What? He should have buried it!
 He should have carried on!"

*** THIS IS THE PUREST ACCIDENT IN THE WHOLE PACK, AND THE FOOTAGE PROVES IT ***
 The title promise of this video is "accidental". Most entries need you to argue the case. This one
 does not, because the reason is visible: at the moment the ball hits him, NEUER IS FACE DOWN,
 SLIDING AWAY FROM PLAY, WITH HIS EYES ON THE NETTING. He cannot see the ball. He makes no kicking
 motion and no reach. The ball simply rolls into a trailing boot. If you only have time to make one
 entry's case properly on camera, make it this one.

SCENE: Empty stadium. This is a BEHIND-CLOSED-DOORS COVID-ERA match — the stands are bare and the crowd
 noise is the piped artificial track the Bundesliga used in 2020. One of the perimeter boards reads
 "THANK YOU, HEALTHCARE HEROES", which dates it beyond doubt and is a genuinely striking visual.
 The turf looks wet, which is why the slide carries as far as it does.

READ OFF THE KIT: BAYERN all red — red shirts with white shoulder stripes, red shorts, red socks.
 NEUER mint/turquoise long sleeves, turquoise shorts, turquoise socks, white and black gloves,
  WHITE AND RED BOOTS. The boot colour matters, because the red flash on the heel is what you can
  actually see making the contact on the replay.
 EINTRACHT FRANKFURT white shirts with black shoulder and trim detail, white shorts, white socks
  with black banding.
 REFEREE: not in frame during this sequence.

BOARDS: left to right behind the goal
 MAGENTA TV · THANK YOU, HEALTHCARE HEROES · Allianz · QATAR AIRWAYS · Allianz again.

ACTION: beat by beat, and the order is the whole point
 1. Neuer leaves his line towards Dost on the right side of the box and COMMITS EARLY into a low
    slide along the turf to cut the angle down.
 2. Dost opens his RIGHT foot and chips it delicately over the sliding keeper. The ball is now
    rolling towards an empty net and Dost has beaten him.
 3. Neuer's own momentum betrays him and then saves him: the slide carries his whole body PRONE AND
    STOMACH-FIRST across the line and into his own net.
 4. Face down and travelling, his legs trail behind him. His RIGHT knee is bent upward with the foot
    slightly off the ground.
 5. THE BALL STRIKES THE HEEL/UNDERSIDE OF HIS TRAILING RIGHT BOOT, right on the threshold of the
    goal line, and deflects away.
 DELIBERATE OR ACCIDENT: accident, and here is the evidence rather than the assertion. He is face
 down. He is facing away from the field of play. His head is down and his eyes are on the netting and
 turf ahead of him at the exact moment of contact. He never turns his head to track the ball. He
 makes no kick and no reach. The boot is trailing as a passive consequence of the slide.

THE ATTACKER: Dost drives into the box, opens the body, and takes the chip early and softly — a confident,
 unhurried finish. He then FOLLOWS THE FLIGHT WITH HIS EYES ALL THE WAY, fully expecting it to cross
 the line, and PULLS UP ABRUPTLY when it does not. The disbelief on him is the reaction shot.

REACTION: There is no celebration to cut to, which is itself the story. Neuer slides to a halt INSIDE the net,
 ROLLS HIS HEAD BACK OVER HIS RIGHT SHOULDER towards the pitch, and looks out with a stunned,
 bemused expression as he works out what he has just done. That look is the last frame of the entry.

CAMERA: 02:00-02:03 elevated wide tactical: Dost breaks through, Neuer slides out, the chip, the slide over
  the line. This carries the geometry.
 *** 02:04-02:07 GROUND-LEVEL REVERSE SLOW-MOTION FROM INSIDE THE NET, looking back out over the
  goal line. CUT ON THIS. *** It is the only angle that shows the ball meeting the trailing right
  heel, and without it the audience has to take your word for it.
 02:07-02:08 tight slow-motion close-up of Neuer prone in the net looking back over his shoulder.

COMMENTARY: "Oh, Bas Dost! Bas Dost! What? He should have buried it! He should have carried on!"

AUDIO: Piped/artificial crowd murmur only. There is no real crowd reaction available on this clip, so do
 not build the beat around an audience gasp that does not exist — let the commentary carry it.

CANNOT DETERMINE
 *** THE FIXTURE AND THE DATE. DO NOT STATE THEM ON CAMERA. ***
  The players are confirmed, the teams are confirmed by the kits, and the empty stadium puts it in
  the 2020 COVID window. But the exact match is not pinned: the candidates are the Bundesliga
  meeting and the DFB-Pokal semi-final of that period, and the footage does not carry a scorebug,
  competition badge or clock to separate them. Say "behind closed doors in 2020" — which is provable
  from the frame — and leave the fixture out.
 Squad numbers on either player. Neither is legible at this resolution and angle. Identity rests on
  the commentary and on appearance, which for these two is sufficient.
 The exact margin on the goal line. There is NO goal-line-technology graphic in this clip, so do not
  claim millimetres or say the technology confirmed anything.
```

#### `deep/acc-3-idk.md`
<!-- FILE: deep/acc-3-idk.md · 4365 bytes · 61 lines · sha256 73ae2deb3e968cec8958d114e2c2112c9d5c8d1a94779a2d4a520fb7d1663172 -->
*Vocabulary-normalised and colon-ified 21 Sep; carries AUTHENTIC: and CANNOT DETERMINE.*
```markdown
# DEEP PASS — ACCIDENTAL SAVES #3 "IDK Save"
SOURCE: reference ZbunM6UKwts, its NUMBER 4 entry, at 00:14–00:22.
AUTHENTIC: real broadcast. Multi-camera professional coverage. No game UI.

*** THE BRAZIL ATTRIBUTION IS NOW EVIDENCED, NOT ASSUMED ***
 Boards left to right: BENOIT (white on dark blue) · NET HDTV (red and blue on white) ·
 SUBWAY (yellow on green, below the wall) · Claro-hdtv (white on red/blue) · FATAL (white/red on black)
 · Claro-4G (white on red). Claro and NET are Brazilian telecoms and FATAL is a Brazilian brand.
 Previously this was written as "Brazilian state league" on a hunch. It now has boards behind it.

*** AND THE MOMENT IS NOT WHAT I HAD WRITTEN ***
 This is a PENALTY REBOUND, and the ball hits the keeper IN THE FACE.

SCENE: Attackers: solid RED short sleeves with white sleeve and collar trim, red shorts, red socks.
  Front sponsor/crest NOT LEGIBLE. A teammate at the edge of the box wears 27 in white on the chest.
  Black boots with white accents.
 Defenders: BLACK/dark short sleeves with white lettering, black shorts, black socks.
  #14 in large white on the back, BRIGHT YELLOW BOOTS. Another defender in NEON GREEN BOOTS.
 Goalkeeper: TURQUOISE/light blue long sleeve with dark navy-black panels across the shoulders and
  flanks, WHITE shorts with dark side detail, WHITE socks. Gloves NEON YELLOW-GREEN backhand,
  white palms. Boots white and black. Short dark hair, dark stubble.
 Referee: yellow short sleeves, black shorts, black socks, black boots.
 Bright clear daylight, sharp dark diagonal shadows across the box toward the goal line. Good grass,
 all markings crisp — penalty spot, six-yard box, penalty area and arc all visible.
 Low white perimeter wall with blue trim and metal fencing, a packed STANDING TERRACE behind it, and a
 two-storey white building with blue window frames behind that.
 OVERLAY: "WHEN KEEPERS MAKE" (white) / "ACCIDENTAL SAVES" (red, black outline). Rank list with
 "4. IDK Save" in white on a red number. Watermark SANTA BALL centre.

ACTION: 1. 00:14 The clip opens IMMEDIATELY AFTER A PENALTY HAS BEEN TAKEN. The ball hits low against the base
    of the keeper's RIGHT POST. The keeper has dived low to his right and is lying prone on his
    stomach and chest across the goal line. The ball ricochets sharply off the upright back into the
    centre of the six-yard box.
 2. 00:15–00:16 An attacker in red sprints in from outside the RIGHT of the penalty area, completely
    unmarked, arriving about five to six yards out. He side-foots a firm first-time strike with his
    RIGHT FOOT at the open net.
 3. 00:16–00:17 The keeper, still down, is scrambling BACKWARD on hands and knees trying to reorient.
    The ball goes straight into his body and head as he flails back.
 4. 00:17–00:20 THE CONTACT, on the reverse replay: he pushes off the ground and tumbles backward onto
    his backside with his legs kicking up. The ball strikes him FLUSH IN THE FACE / FOREHEAD. His arms
    are spread wide — he makes NO movement of his hands toward the ball at all. The impact deflects it
    sharply upward and it loops harmlessly OVER THE CROSSBAR.
 5. 00:20–00:22 The low side replay confirms he was pushing off the base of the post in disarray and
    was entirely unaware of the ball until it hit him.

CAMERA — three shots
 1. 00:14–00:17 high sideline, live speed: the rebound, the follow-up strike, the block.
 2. 00:17–00:20 LOW ANGLE BEHIND THE NET looking out, slight slow motion — this is the one that shows
    the ball hitting his face while he is on his back. This is the shot to build the edit on.
 3. 00:20–00:22 ground level behind the left post looking diagonally across the line, close on the
    scramble.

AUDIO: Creator voiceover verbatim: 00:14 "Brazilian brother from the spot..." / 00:16 "What the fuck is
 happening?" / 00:19 "Keeper with I don't know save."
 Original commentary NOT AUDIBLE under the voiceover; muffled crowd and ambient noise faintly present.
 Upbeat electronic music throughout.

CANNOT DETERMINE
 The keeper's name, the penalty taker, the rebound shooter. The clubs, the competition, the date.
 NOTE: the boards give a real search angle now — a Brazilian match with Claro/NET/Benoit/FATAL boards,
 red v black, keeper in turquoise with white shorts, standing terrace and a white building behind.
```

#### `deep/acc-4-no-look.md`
<!-- FILE: deep/acc-4-no-look.md · 3580 bytes · 52 lines · sha256 807ec267074607f7b55eb862010e88ff7fb10a65a143ab7c9b111bd07f801d58 -->
*Vocabulary-normalised and colon-ified 21 Sep; carries AUTHENTIC: and CANNOT DETERMINE.*
```markdown
# DEEP PASS — ACCIDENTAL SAVES #4 "No-Look Save"
SOURCE: reference ZbunM6UKwts, its NUMBER 5 entry, at 00:07–00:13.
AUTHENTIC: real broadcast. No game UI. No scorebug.

*** BREAKTHROUGH: THIS ONE IS NOW IDENTIFIABLE ***
 Boards read "Prifysgol Abertawe" / "Swansea University" / "sky bet" / "BETTING BETTER" / "John Pye"
 / "MILES H..." plus a Welsh flag banner. That is a SWANSEA home ground.
 And the attacking team has a NAME ON THE SHIRT: "SCOTT" above number 36, white on red.
 Home side in all white (Swansea colours), away side in red. Home goalkeeper wears 33.
 ACTION: search "Swansea 33 goalkeeper" against a red away side with a squad member named Scott
 wearing 36. This is findable now, where before it was a dead end.

SCENE: Attackers: RED jerseys, WHITE collars and white sleeve trim, WHITE shorts with red numbers,
  white socks with red detail. Legible: 14 (back and right thigh), 18 (back), 9 (partial),
  and 36 with the name SCOTT printed above it.
 Defenders: ALL WHITE — shirt, shorts, socks with dark accents. Legible: 11 and 17 (dark font on white).
 Goalkeeper: monochrome ROYAL BLUE long sleeve, royal blue shorts, royal blue socks, number 33 in white
  on the back AND on the left leg of the shorts. WHITE gloves with black inner palm and cuff detail.
  LIGHT CYAN / SKY-BLUE BOOTS. Fair skin, short brown hair, trimmed stubble.
 No referee visible.
 Overcast natural light mixed with floodlights. Well-kept grass, standard white markings.
 Grandstand behind the goal, spectators in dark coats.
 OVERLAY: header "WHEN KEEPERS MAKE ACCIDENTAL SAVES". Rank list on the left showing
  1. 2. 3.(red) 4.(red) 5. No-Look Save 6. Full Reverse Save. Watermark "_SANTA BALL" centre.

ACTION — the mechanic is much clearer than I had it
 1. 00:07 Red #14 controls it inside the LEFT of the penalty area, dribbling diagonally at the six-yard box.
 2. 00:07–00:08 The keeper has ALREADY committed forward and gone down near the six-yard line to the
    left of the goal. He ends up ON HIS HANDS AND KNEES FACING HIS OWN NETTING, back turned completely
    to the field of play.
 3. 00:08–00:10 Red #14 cuts inside past white #17 and strikes a LOW shot with his RIGHT FOOT at the
    open net. White #11 slides to block and misses.
 4. 00:10 THE CONTACT: the low ball hits the keeper square on his LOWER BACK / RIGHT BUTTOCK / UPPER
    REAR THIGH. He is crouched on all fours facing the net; his head and eyes are pointed AWAY from the
    ball into the back of his own goal at the instant of impact.
 5. 00:10–00:13 It rebounds off his backside out into the six-yard box. He recovers, gathers it, and
    walks off holding the ball tucked under his LEFT arm against his torso.

CAMERA — three shots
 1. 00:07–00:09 high wide tactical, panning right, zooming as the move develops.
 2. 00:09–00:11 GROUND-LEVEL replay from behind the endline beside the post — this is the money angle,
    it shows him facing into the net and the ball striking his lower back.
 3. 00:11–00:13 medium tracking from the main side camera, following him walking across the six-yard box.

AUDIO: Creator voiceover verbatim: "Random player in front of goal..." then "What the... [scoff] No-look save
 just unlocked!"
 Crowd: a sharp collective "Ooooh!" at the moment of contact — real, usable audio.
 AUDIO: a video-game "achievement unlocked" chime lands exactly on the words "just unlocked" at 00:12.

CANNOT DETERMINE
 Club names from markings alone (signage places it in Swansea). The keeper's name — 33 has no name
 printed. Competition, scoreline, date.
```

#### `deep/acc-5-full-reverse.md`
<!-- FILE: deep/acc-5-full-reverse.md · 3628 bytes · 51 lines · sha256 ab37dc500fa76735e31641aa730277e672b78bc0e9aa3cfc455a960509930c8d -->
*Vocabulary-normalised and colon-ified 21 Sep; carries AUTHENTIC: and CANNOT DETERMINE.*
```markdown
# DEEP PASS — ACCIDENTAL SAVES #5 "Full Reverse Save"
SOURCE: reference ZbunM6UKwts, its NUMBER 6 entry. 40s Short. No standalone clip exists.
AUTHENTIC: real broadcast. No game UI. No scorebug or clock anywhere in the segment.

SCENE: Attackers: RED shirts, short sleeves, WHITE stripes along the shoulders/sleeves, white crew collar,
  WHITE shorts, red socks with white turnover. Chest sponsor and badge present but NOT LEGIBLE.
 Defenders: vertical BLUE AND AMBER stripes on the torso with SOLID BLUE SHORT SLEEVES, blue shorts
  with white squad numbers on the front-right leg — "20" clearly legible ON THE SHORTS (not the shirt).
  Amber/yellow socks. A second defender's shorts read 2 or 22, not fully legible.
 Goalkeeper: LIGHT GREEN long-sleeve with darker green sleeve/shoulder panels, light green shorts,
  light green socks. Gloves WHITE palm and backhand with dark grey wrist cuffs. Boots white/light grey
  with black detailing.
 No referee visible at any point.
 Bright natural sun, hard diagonal shadows toward the goal and right touchline. Grass in good condition.
 Single-tier covered stand behind the goal, packed, dark and light casual clothing, yellow-vested
 stewards along the perimeter barrier.
 BOARDS left to right: "Sky BET BETTING, BETTER" · "The Wrekin Housing Trust" · "GTE" · "MORR..." (cut off).
 OVERLAY: header "WHEN KEEPERS MAKE ACCIDENTAL SAVES" in yellow and red/white bold. A vertical rank
 list bottom-left: 1. 2. (yellow) 3. 4. (red) 5. 6. (white) with "6. Full Reverse Save" spelled out.
 Watermark "SANTA BALL" across the lower centre on the replay.

ACTION — and this is DIFFERENT from what I had before
 1. Attacker in red dribbles into the box toward the right of the six-yard box. Defender #20 slides in
    from the attacker's LEFT.
 2. The attacker cuts inside and CHIPS/STABS it with his RIGHT foot toward the goalmouth, aiming for
    the top corner. [Previously recorded as a low cross — it is a chip.]
 3. The keeper commits forward and dives LOW AND HORIZONTALLY TO HIS RIGHT across the six-yard line.
    His hands miss. The ball FLOATS DIRECTLY OVER HIS PRONE BODY.
 4. He lands flat on stomach and chest, HEAD FACING THE TURF, sliding forward, blind.
 5. As the ball passes above his lower back and legs, BOTH LEGS WHIP UP BEHIND HIM in an inverted
    scorpion. His RIGHT boot — back of the heel and upper sole — strikes the UNDERSIDE of the
    descending ball at roughly waist-to-chest height off the ground.
 6. The deflection sends it up and backward, looping cleanly OVER THE CROSSBAR, landing on the roof of
    the net behind the goal line. Defender #20 runs past the goal line; the keeper rolls onto his side.

CAMERA — three shots
 1. 00:00–00:02 live, high wide from the main grandstand, panning and zooming into the box.
 2. 00:02–00:04 replay, mid-height pitchside/corner, cropped tight on the goalmouth, tracking the dive
    and slide into the heel contact.
 3. 00:04–00:06 SLOW-MOTION ULTRA-TIGHT replay on the keeper face-down, isolating the right heel flipping
    up into the ball.

AUDIO: Original commentary: NOT AUDIBLE — fully suppressed.
 Creator voiceover verbatim: "Random brother in the box..." / "Oh, shit!" (short laugh) /
 "Brother saved it in reverse mode!"
 Faint ambient crowd under the speech. A cartoon punch/impact SFX lands on the boot contact at 00:05.

CANNOT DETERMINE
 The keeper's name. The clubs — "The Wrekin Housing Trust" points to Shropshire and the blue/amber
 stripes resemble Shrewsbury Town, but NO crest or team name is legible on screen, so it stays unstated.
 The competition and the date.
```

#### `deep/badge-1-ferland-mendy.md`
<!-- FILE: deep/badge-1-ferland-mendy.md · 3728 bytes · 50 lines · sha256 94446a4ee2805adda783566e64e63d0a0656ce6c2bd1215208d6f230a6d31a55 -->
*Vocabulary-normalised and colon-ified 21 Sep; carries AUTHENTIC: and CANNOT DETERMINE.*
```markdown
# DEEP PASS — DIE FOR THE BADGE #1 "Ferland Mendy, Real Madrid v Man City"
SOURCE: WgzZRA260X0 (TNT/BT Sport) at 00:15–00:18. MATCH CLOCK 86:11–86:13.
AUTHENTIC: real BT Sport 2 live broadcast. Official UEFA CL graphics. No game UI, no splicing.

SCOREBUG — read exactly
 Top left: UCL starball · clock running 85:55 through 86:13 · "RMA 0" · "1 MCI" · aggregate "(3-5)"
 Top right: "BT SPORT 2 LIVE" with a white circular bug beneath.

SCENE: Real Madrid: WHITE short sleeves with PURPLE/BLUE SHOULDER STRIPES, dark chest sponsor
  "Emirates FLY BETTER", crest left chest, white shorts with subtle side trim, white socks.
  READ OFF THE KIT: #23 Ferland Mendy · #3 Militão · #6 Nacho · #1 Courtois · #15 Valverde · #20 Vinícius.
 COURTOIS: BRIGHT FLUORESCENT GREEN long sleeve with black sponsor text, green shorts, green socks,
  white-and-black gloves.
 Man City: NAVY base with lighter blue/purple gradient across shoulders and chest, white Puma logo,
  white "ETIHAD AIRWAYS" chest sponsor, white names and numbers on the back, navy shorts with white
  numbers, navy socks. READ OFF THE KIT: "GREALISH 10" · #11 Zinchenko · #47 Foden · #20 Bernardo Silva
  · #8 Gündoğan.
 Referee: turquoise/light blue short sleeves, black shorts, black socks.
 Night, bright floodlights, clear. Natural turf with horizontal mowing bands. CONFETTI AND WHITE PAPER
 LITTER scattered across the turf near the goal lines and touchlines. Packed Bernabéu, mostly white-clad.
 BOARDS: Lays · Heineken SILVER · UEFA CHAMPIONS LEAGUE · PlayStation 5 · Expedia · Mastercard.

ACTION: 1. 00:08–00:10 City work down the LEFT. ZINCHENKO releases a through ball into the left channel of the box.
 2. 00:11–00:13 GREALISH (#10) runs onto it with his RIGHT foot into the left side of the area.
    COURTOIS rushes out and drops to the turf to smother the angle.
 3. 00:14–00:15 Grealish carries it PAST the sliding Courtois toward the byline/six-yard angle and
    strikes with his LEFT FOOT at the open net.
 4. 00:15–00:16 FERLAND MENDY (#23) is sprinting DIAGONALLY BACKWARD from the left edge of the six-yard
    box to cover the empty net, facing outward toward the field while sliding toward his left post.
    The ball is rolling past the beaten Courtois toward the bottom right corner.
    Right on the WHITE GOAL-LINE STRIPE, Mendy lunges and HOOKS IT AWAY WITH HIS LEFT FOOT / INSTEP.
 5. The clearance goes across the six-yard box toward the right side of the penalty area. Grealish turns
    back for the loose ball; City players raise hands; Madrid recover.

CAMERA: Live 00:00–00:28, wide from the main elevated grandstand, tracking the whole counter from midfield —
 Grealish beating Courtois and Mendy sliding across the goalmouth, all in ONE UNBROKEN REAL-TIME SHOT.
 Replay 00:48–01:02 is a low tight angle behind the line near the left post, but it covers Grealish's
 SUBSEQUENT chance that Courtois deflects with his studs — there is NO isolated slow-motion or goal-line
 technology animation of Mendy's clearance in this video.

AUDIO — English, and the co-comm line is the caption
 Lead: "...and the ball here, Zinchenko onto Grealish. Phil Foden's trying to time his run in the middle.
  Grealish is charging in himself... It's Grealish! It's off the line! It's only just off the line!"
 Steve McManaman: "...I don't know what happened there. What... what did Courtois... was he diving out
  the way? Grealish really just had a tap-in."
 Crowd: sharp collective gasp as Grealish rounds him, then a loud roar of relief and applause.

CANNOT DETERMINE
 The exact margin in millimetres — no Hawk-Eye render is broadcast here. Mendy's boot brand. Bench
 personnel behind the netting.
```

#### `deep/badge-2-stones.md`
<!-- FILE: deep/badge-2-stones.md · 5652 bytes · 82 lines · sha256 93b3ffcbddc022952afd1936b892b414c41c9ccf5ef9452027a4f3cadd8545de -->
*New 20–21 Sep after Joel's 'Keep Stones anyway'; sequence corrected (Stones' clearance hits Ederson); 11mm from Man City/Sky, not the footage.*
```markdown
# DEEP PASS — DIE FOR THE BADGE #2 "JOHN STONES OFF THE LINE v LIVERPOOL"

SOURCE: MriNd_wn1Os — Manchester City OFFICIAL, "BEATING LIVERPOOL 3 YEARS AGO! | City 2-1 Liverpool".
 The clearance runs 00:55–01:40. Man City v Liverpool, Etihad, 3 January 2019.
AUTHENTIC: real Premier League broadcast with official Hawk-Eye Goal Decision System animation.
 No game UI. Official club channel, so a gameplay flag here would be the model being wrong.

*** YOU ARE KEEPING THIS ONE KNOWING IT REPEATS PART 1. Frame it, do not hide it. ***
 It is your Part 1's #2 at the same rank. The strongest version on camera is to say so in the first
 breath — "you have seen this one before, and it is still the best example there is" — because the
 audience that spots repeats is the same audience that rewards being told.

*** THE NUMBER IS WRONG IN PART 1, AND THAT IS FREE REDO AMMUNITION ***
 Your Part 1 voiceover says 11.7mm. An earlier note in the app said 11.2mm. BOTH ARE WRONG.
 Manchester City's own site: "Stones had somehow managed to ensure that 11 MILLIMETRES of the ball
 had not crossed." Sky Sports' own headline: "how Etihad showdown and 11mm decided the 2018-19
 Premier League title race." Two independent sources, one of them the club itself, both say ELEVEN.
 SAY "eleven millimetres". Do not put a decimal on screen — the sources do not carry one and a
 decimal is exactly what drags a correction comment.

[!] THE FIGURE IS NOT IN THIS FOOTAGE AT ALL. The Goal Decision System graphic in this cut shows
 only the words "NO GOAL" and then cuts back to live play. If you want the number on screen you are
 adding it yourself, so add the right one.

SCOREBUG: top-left, Premier League lion, "CITY 0 - 0 LIV". No running clock on the bug in this cut.
BROADCAST GRAPHICS: at 01:33–01:37 a purple lower-third with the white PL lion reading
 "Goal Decision System". The Hawk-Eye animation follows at 01:37–01:40.

READ OFF THE KIT: MAN CITY: sky blue shirts with navy sleeve striping, white shorts, sky blue socks with navy trim,
  ETIHAD AIRWAYS chest sponsor. *** STONES IS 5 *** — legible on his back and on the front of the shorts.
 LIVERPOOL: deep red shirts, red shorts, red socks, Standard Chartered. Numbers legible: 10 MANÉ,
  11 SALAH, 9 FIRMINO, 26 ROBERTSON, 14 HENDERSON, 6 LOVREN.
 GOALKEEPERS: EDERSON bright yellow with black sleeve detail, 31 legible on his back.
  ALISSON neon green, 13 legible.
 REFEREE: Anthony Taylor, all black with the white PL crest and EA Sports sleeve badges.

BOARDS: NEXEN TIRE · EXTRAORDINARY CITY STORY · SHARE AND WIN A LUXURY TRIP TO ABU DHABI ·
 WHAT'S YOUR EXTRA · EA SPORTS · ETIHAD AIRWAYS.

ACTION — and the sequence is NOT what the pack notes said
 [!] CORRECTED: the app previously said "Ederson's clearance rebounds off him toward his own goal."
 It is the other way round — it is STONES' clearance that hits Ederson.
 1. FIRMINO BACKHEELS into the left channel for MANÉ.
 2. Mané strikes low past the onrushing Ederson and hits the INSIDE BASE OF THE FAR POST — City's
    right post. The woodwork, not a save, is what keeps it out first.
 3. Stones sprints back to deal with the rebound and swings his RIGHT boot to clear — and the ball
    SMASHES STRAIGHT INTO EDERSON, who is diving backwards towards his own goal. It ricochets off him
    and rolls back towards the empty net.
 4. SALAH sprints in to bundle it over. Ederson is stranded on the turf.
 5. THE CLEARANCE: Stones turns, dives across the goalmouth and hooks it away with the INSTEP/INSIDE
    OF THE RIGHT BOOT, inches ahead of Salah's outstretched boot, with the ball already part-way over.
 6. THE SECOND CLEARANCE, which nobody mentions: the hook loops up to the edge of the six-yard box,
    Salah tries to turn it in AGAIN, and Stones gets up and smashes it out of the box. He makes the
    save twice.

REACTION: Salah's arms go up claiming it, Mané looks to the referee, Stones stays locked into the
 second ball rather than celebrating, and Guardiola is caught exhaling on the bench.

CAMERA: 00:55–01:14 live high wide, the whole sequence in real time.
 01:15–01:25 replay 1, high tactical wide from the opposite stand.
 *** 01:26–01:32 replay 2, LOW REVERSE FROM BEHIND THE NET LOOKING OUT. CUT ON THIS. *** It is the
  only angle that shows the hook going across Salah with the ball on the line.
 01:33–01:36 replay 3 as the Goal Decision System caption appears.
 01:37–01:40 the Hawk-Eye overhead animation.

COMMENTARY — verbatim
 Live: "Firmino, the backheel into the path of Mané. Mané it is, and it comes off the post! And
 Liverpool almost get the follow-up, and then saved off the line by Stones! What drama in the Etihad!
 The visitors almost take the lead. The post comes to the rescue of City, and Guardiola's team
 breathe again."
 Replay: "...and then Stones, tremendous save off the line. Just time for the clearance, comes off
 Ederson, and Stones watching the ball all the way... and that's cleared right off the line."

AUDIO: a gasp as Mané beats Ederson, panicked shouts as it comes back off Ederson, then an explosive
 roar of relief. The crowd track carries the whole beat on its own.

CANNOT DETERMINE
 THE MILLIMETRE FIGURE — not displayed anywhere in this source. Use the written record (11mm) and
  attribute it, or say "by the width of the line" and skip the number entirely.
 WHICH PART OF EDERSON the first clearance strikes — chest or upper arm. The angle and speed make it
  genuinely unclear, so say "off Ederson" and do not name a body part.
 The match clock at this moment — the scorebug in this cut carries no running clock.
```

#### `deep/badge-3-sule.md`
<!-- FILE: deep/badge-3-sule.md · 4076 bytes · 58 lines · sha256 99f6193a671f18cd5bd35fef4dd56d92b071e30417d44da46507f3ebbb210298 -->
*Vocabulary-normalised and colon-ified 21 Sep; carries AUTHENTIC: and CANNOT DETERMINE.*
```markdown
# DEEP PASS — DIE FOR THE BADGE #3 "Süle denies Mbappé"
SOURCE: vjTC2gCMtqM (DAZN). LIVE at 00:13–00:15, MATCH CLOCK 16:34–16:36.
REPLAYS at 00:30–00:33, 01:10–01:14 and 01:15–01:20.
AUTHENTIC: real DAZN broadcast, official UCL graphics. No game UI.
DORTMUND v PSG, Signal Iduna Park, UCL group stage. Night, floodlights.

SCOREBUG — read exactly
 Top left: UCL starball · clock 16:24 through 17:27 · "DOR 0 0 PAR". Top right: DAZN watermark.
 At 00:49 a corner graphic reads "CORNERS: DOR 1 - 2 PAR".

SCENE: DORTMUND: YELLOW shirts with a DARK GREY/BLACK GEOMETRIC BLOCK PATTERN across the front, black Puma
  logos, round black collar, black "Evonik" chest text. Black shorts with yellow Puma marks, yellow
  socks with black trim.
  *** SÜLE'S NUMBER READ OFF THE SHIRT AT 01:04–01:06: "SÜLE" and 25. *** Black tattoos on both
  forearms. LIGHT GREEN/TEAL BOOTS.
  KOBEL: FLUORESCENT CORAL/ORANGE long sleeve and shorts, big black "1" and "KOBEL" on the back (00:19),
  light grey/white gloves with fluorescent palms.
  Also visible: ÖZCAN 6 · 15 Hummels · 17 Wolf.
 PSG: WHITE shirts with a central NAVY AND RED CHEST STRIPE, dark "QATAR AIRWAYS", navy swoosh right
  chest, crest left chest, "GOAT" sleeve sponsor on the left arm. White shorts, white socks with blue.
  *** MBAPPÉ'S 7 READ OFF THE FRONT LEFT OF HIS SHORTS at 00:20–00:21. *** RED/ORANGE BOOTS.
  Also visible: L. HERNÁNDEZ 21 · LEE KANG-IN 19 · 37 Škriniar.
 Officials in cyan/light blue short sleeves, black shorts and socks.
 Packed stands including the Yellow Wall.
 BOARDS: TURKISH AIRLINES · FLY WITH EUROPE'S BEST · Heineken SILVER – Smooth & Refreshing Taste –
 Low Bitterness · TRY NOW · Heineken 0.0.

ACTION: 1. 00:07–00:11 A PSG centre-back plays a direct LOFTED through-ball with his RIGHT foot between the
    Dortmund lines. Mbappé controls it into the box with his RIGHT foot.
 2. 00:11–00:13 KOBEL charges out to narrow the angle. Mbappé touches it TO HIS RIGHT around the diving
    keeper, taking him completely out. Kobel ends up sliding onto his stomach inside the box.
 3. 00:13–00:14 Mbappé strikes with the INSIDE OF HIS RIGHT FOOT from roughly 8 yards at the open net.
 4. 00:14–00:16 SÜLE has tracked back from the centre of the box, sprinting at the goal line. He drops
    into a FULL-LENGTH SLIDE ON HIS LEFT HIP AND BACK, extending his RIGHT LEG HORIZONTALLY HIGH OFF THE
    TURF. Inches before the line he intercepts and LIFTS the ball with his RIGHT BOOT/INSTEP, deflecting
    it OVER THE CROSSBAR for a corner.
 5. 00:17–00:22 Süle jumps up and ROARS. KOBEL HUGS HIM. Hummels joins. MBAPPÉ TURNS AROUND, PULLS AT
    HIS COLLAR AND SMILES IN DISBELIEF. Those two reactions are the edit.

CAMERA: 00:03–00:21 high wide tactical master, live, unbroken through the ball, the shot, the slide, then a
 close-up of Süle with Kobel and Mbappé reacting.
 01:00–01:06 close-up of Süle hands on knees — this is where the name and 25 are legible.
 01:07–01:14 replay from the right sideline tracking Mbappé's run and the recovery.
 01:15–01:20 SLOW MOTION FROM BEHIND THE GOAL showing the exact instant the right foot lifts it over.

AUDIO — German, and there are four usable caption lines here
 00:13 "...aber erstmal Mbappé und SÜLE!"
 00:20 "Ja, gerade noch kritisiert, zurecht, aber jetzt... der größtmögliche Grätsch-Moment!"
       (just criticised, rightly, and now — the greatest possible tackle moment)
 00:40 "Mit einer Monster-Grätsche rettet er hier." (with a monster slide tackle he rescues it)
 01:07 "Fantastisch. Niklas Süle bleibt im Tempo, und dann gibt's auch noch gute Haltungsnoten.
       Was für eine Rettungstat! Mbappé trifft ihn nicht so ganz optimal."
       (…he keeps up the speed, and gets style points too. What a rescue act!)
 Huge roar from the home crowd, then applause and chants.

CANNOT DETERMINE
 Who played the pass to Mbappé — too far out on the wide camera to be certain. Mbappé's back number
 during the live clearance, because his back is turned.
```

#### `deep/badge-4-vandeven.md`
<!-- FILE: deep/badge-4-vandeven.md · 4276 bytes · 60 lines · sha256 3f69dcab991c5a02f850aed2a8164e8496dc46430cf06b9b1dd7a41b4007a662 -->
*Vocabulary-normalised and colon-ified 21 Sep; carries AUTHENTIC: and CANNOT DETERMINE.*
```markdown
# DEEP PASS — DIE FOR THE BADGE #4 "Van de Ven, Europa League final"
SOURCE: vWC-USe1ncI (Tottenham official). LIVE CLEARANCE AT 00:39; replays to 01:10.
MATCH CLOCK 67:31–67:46. SCORE "TOT 1  0 MUN". San Mamés, Bilbao. Night, floodlights.
AUTHENTIC: real broadcast, UEFA graphics, no game UI.

*** IT IS NOT A HOOK. IT IS AN OVERHEAD BICYCLE KICK AT CROSSBAR HEIGHT. ***

SCENE: Spurs: WHITE with navy trim, RED "AIA" chest sponsor, crest left chest, swoosh right chest, white
  shorts, white socks. READ OFF THE KIT: #37 M. VAN DE VEN · #1 VICARIO · #17 ROMERO · #8 BISSOUMA
  · #19 SOLANKE · #30 BENTANCUR · #13 UDOGIE · #23 PORRO.
 VICARIO: full BRIGHT YELLOW long-sleeve with subtle dark shoulder pattern, yellow shorts, yellow socks,
  white/grey gloves.
 Man United: RED with white accents, white "Snapdragon" chest sponsor, BLACK shorts, BLACK socks.
  READ OFF THE KIT: #8 B. FERNANDES · #18 CASEMIRO · #15 YORO · #5 MAGUIRE · #23 SHAW.
 Referee in light cyan/blue with black collar and side panels, black shorts and socks.
 Packed multi-tier stadium split between white and red.
 BOARDS: "BILBAO FINAL 2025" · Swissquote · Enterprise · Just Eat · Lidl.
 LED BOARDS in order: Lidl · Eat fresh · #onyourteam · STRAUSS · FlixBus · Hankook · Betano.

ACTION: 1. 00:33–00:36 BRUNO FERNANDES (#8) strikes an INSWINGING FREE KICK with his RIGHT FOOT from about
    40 yards, slightly left, floating it to the far side of the Spurs six-yard box.
 2. 00:36–00:38 VICARIO comes off his line to punch two-handed. In mid-air around the six-yard line HIS
    OWN TEAMMATE SOLANKE (#19) leaps backwards into him. Vicario misses the punch, is knocked to the
    ground, and the ball pops off heads and shoulders in the Casemiro/Maguire contest and LOOPS TOWARD
    THE UNGUARDED GOAL.
 3. 00:38–00:40 VAN DE VEN starts near the centre edge of the six-yard box. The instant Vicario advances,
    he drops back to cover. Backpedalling toward the line as the ball dips under the bar, he THROWS
    HIMSELF HORIZONTALLY INTO THE AIR IN A BACKWARDS ACROBATIC SCISSOR/OVERHEAD KICK, swinging his
    RIGHT LEG up along the plane of the goal line. His right boot meets the ball AT ROUGHLY CROSSBAR
    HEIGHT DIRECTLY ABOVE THE WHITE LINE and hooks it up and away.
 4. 00:40–00:45 The clearance drops in the box. YORO (#15) shoots first time with his RIGHT foot.
    ROMERO (#17) blocks it with his body. BISSOUMA collects and clears upfield with his RIGHT foot.
    Three separate stops in four seconds.
 5. Romero pumps his fists and claps. Bissouma and Van de Ven celebrate. Casemiro and Fernandes raise
    their hands in disbelief.

CAMERA — five angles, and the last is the one
 00:31–00:47 live high wide from the gantry, the whole thing in one shot.
 00:48–00:55 replay 1, reverse elevated touchline, showing Van de Ven ANTICIPATING and running to the line.
 00:56–01:00 replay 2, tight on Vicario jumping, colliding with Solanke, spilling it.
 01:01–01:03 replay 3, behind-the-goal baseline on the Solanke/Vicario collision.
 01:04–01:10 *** replay 4: LOW ULTRA-SLOW-MOTION CAMERA INSIDE THE NET LOOKING OUT. *** It shows him
  running to the line, leaping horizontally airborne, and hooking it out from under the bar with his
  right foot. Build the edit on this one.

AUDIO — English, and the co-comm hands you the closing line
 Lead 00:34: "Fernandes hangs it... Off Vicario, it pops against his head, and Van de Ven on the line!
  Still in play, Yoro, blocked by Romero! And Bissouma away!"
 Co-comm 00:45: "Brilliant, brilliant, brilliant Van de Ven clearance on the line."
 Lead 00:48: "Van de Ven comes to the rescue."
 Co-comm 00:51: "And look at the way he covers his goalkeeper. As soon as the goalkeeper comes to the
  six-yard line, Micky van de Ven is coming round on the cover. It's his own player, there's no foul.
  Solanke crashes into Vicario. That is magnificent. What a clearance.
  *** That might well be a match-winning clearance. ***"
 Crowd: a roar from the United end as it loops over the fallen keeper, cut off by gasps and a huge
 cheer from the Spurs end.

CANNOT DETERMINE
 No goal-line technology graphic is shown, so the margin cannot be measured. Sleeve patch text on
 distant players. Boot models.
```

#### `deep/badge-5-valverde.md`
<!-- FILE: deep/badge-5-valverde.md · 4611 bytes · 61 lines · sha256 21aa4ce61163f5c2614b0315c678969eee63b4cb49acf448c1b9ba981fea2dcd -->
*Vocabulary-normalised and colon-ified 21 Sep; carries AUTHENTIC: and CANNOT DETERMINE.*
```markdown
# DEEP PASS — DIE FOR THE BADGE #5 "Valverde on Morata"
SOURCE: 3JiwVYCnHqU at 00:02–00:04. MATCH CLOCK 114:29–114:30, second half of extra time.
SCOREBUG: RFEF Supercopa trophy silhouette · running clock · "RMA 0 - 0 ATM". Channel bug "NOVE HD Live".
AUTHENTIC: real broadcast, Italian network NOVE. No game UI.

SCENE: Real Madrid: WHITE short sleeves with GOLD adidas shoulder stripes, GOLD "Fly Emirates" chest text,
  crest left chest, white shorts, white socks with gold detail.
  READ OFF THE KIT: VALVERDE 15 · CARVAJAL 2 · SERGIO RAMOS 4 · R. VARANE 5 · MODRIĆ 10 ·
  CASEMIRO 14 · F. MENDY 23 · VINÍCIUS JR. 25 · COURTOIS 13.
 Atlético: red-and-white vertical stripes with navy accents, "Plus500" chest, "Hyundai" left sleeve,
  "Ria Money Transfer" below the back numbers. Navy shorts, red/navy socks.
  READ OFF THE KIT: MORATA 9 · THOMAS 5 · KOKE 6 (partly obscured) · SAÚL 8 · CORREA 10 · SAVIĆ 15
  · VITOLO 20 · TRIPPIER 23 · OBLAK 13.
 COURTOIS: DARK GREY/BLACK CAMOUFLAGE-PATTERNED long sleeve with yellow accents, dark shorts and socks,
  BRIGHT YELLOW/VOLT BOOTS.
 Referee: bright neon-yellow short sleeves with black collar, side panels and chest pockets, black
  shorts, black socks with white trim.
 Night, bright floodlights, clear. Pristine short-cut grass.
 BOARDS: SMART · SEAT (white on red) · Mouwasat (a hospital sponsor, shown in English and Arabic) · Pepsi globe.
 BROADCAST GRAPHICS: at 01:15 "15 VALVERDE" with a RED CARD icon; at 01:55 "15 SAVIĆ" with a YELLOW.

ACTION: 1. 00:00–00:02 An errant Madrid backpass is intercepted in Madrid's half. MORATA runs onto it through
    the CENTRAL channel with acres of space. Valverde and Carvajal chase from his left and right rear,
    Ferland Mendy wider left. COURTOIS IS ALREADY OUT, standing outside his six-yard box and advancing
    toward the edge of the 18.
 2. 00:02–00:03 Morata takes touches with his RIGHT foot, driving at the centre of the D.
 3. 00:03–00:05 THE FOUL, and the location matters: DIRECTLY CENTRAL, about 2–3 METRES OUTSIDE THE TOP
    OF THE PENALTY ARC. Valverde, at full sprint directly behind him, drops into a sliding lunge.
    HE MAKES NO CONTACT WITH THE BALL AND NO ATTEMPT TO PLAY IT. His eyes stay fixed on MORATA'S LEGS.
    He lunges with his RIGHT LEG and body and sweeps Morata's lower calves and ankles from behind.
    Morata's legs are taken away mid-stride; he is propelled airborne and rolls heavily onto his back
    and side, immediately clutching his head and face. The ball trickles on into the area and Courtois
    gathers it.
 4. 00:06–00:08 The referee sprints in from behind, straight into his chest pocket, STRAIGHT RED at Valverde.
 5. CORREA (#10) shoves Valverde in the chest. SAVIĆ (#15) storms in at Carvajal and Valverde. Both
    sides converge. Yellows follow for Savić and Carvajal.
 6. *** 01:11–01:15 THE BEAT NOBODY USES: as Valverde walks off past the technical area, DIEGO SIMEONE
    REACHES OUT AND PATS HIM ON THE BACK OF THE HEAD/NECK. *** The opposing manager acknowledging it.
 7. 01:45–02:00 close-up of Morata shaking his head with a visible ABRASION/RED MARK on the LEFT SIDE
    OF HIS FOREHEAD.

CAMERA: 00:00–00:19 live high wide through the break, the tackle, the red and the start of the melee.
 00:50–00:58 slow-mo replay 1, high wide, the run from midfield and the tackle.
 00:59–01:05 *** slow-mo replay 2: TIGHT GROUND-LEVEL SIDE PROFILE. It shows him tracking Morata,
  looking directly at his legs, and sweeping him down with zero attempt on the ball. This is the shot
  that proves it was deliberate. ***
 01:06–01:10 slow-mo replay 3, low frontal/reverse, the double contact on the ankles and the roll.
 01:11–01:15 the Simeone pat. 01:37–01:44 the yellows in slow motion.

AUDIO — ITALIAN, and one line IS your thesis
 "...Attenzione a Morata, lanciato in campo aperto dall'errore di Carvajal... entrata da tergo di
  Valverde! Sarà rosso!" (…a tackle from behind by Valverde! It'll be red!)
 *** "Sarà rosso, ma è una super giocata, ovviamente salva il gol."
     (It'll be red, but it's a brilliant play — obviously it saves the goal.) ***
 "Doppio calcione e rosso inevitabile." (Double kick and an inevitable red.)
 "Dà un buffetto al giocatore della Celeste..." (He gives a little pat to the Uruguay player…)
 Crowd: crescendo of gasps and whistling as Morata breaks, erupting into shouting and whistles at the foul.

CANNOT DETERMINE
 Anything said between the referee and the players — drowned out. Boot brands on several players.
 Sleeve patch fine text.
```

#### `deep/gk-assists-all.md`
<!-- FILE: deep/gk-assists-all.md · 17432 bytes · 217 lines · sha256 a4c70dcbc820fe81267b11e850ab0e3afd9b0ffa4dea193d5a1f3d3e9c535b32 -->
*Rewritten 20–21 Sep to 2,693 words: four methods, Čech LEFT (tie-breaker CERTAIN), Ederson GOAL KICK per the written record.*
```markdown
# DEEP PASS — GOALKEEPERS WITH UNBELIEVABLE ASSISTS (all five)

SOURCE: cVtF64Un-0o — Premier League official, "Amazing PL Goalkeeper Assists". All five clips.
AUTHENTIC: all five real broadcast. No game UI anywhere in the compilation.
OVERLAY: PL crowned-lion watermark top-left throughout. Each clip carries a purple lower-third with
 the keeper's name, then a white fixture bar with both crests and the season.
SCOREBUG: NONE on any of the five. No clock and no score is available for any clip in this pack.

*** CORRECTION TO THE PACK NOTE — AND IT IS GOOD NEWS ***
 An earlier pass concluded the five clips showed only THREE delivery methods and told you to say
 three on camera. A second, scoped pass per clip says that was wrong in your favour. It is FOUR,
 because two deliveries that were grouped together are not the same thing at all:
   1. GOAL KICK, struck off the ground — EDERSON, LEFT foot. A dead ball from inside the six-yard
      box. Confirmed in the written record, which calls it a goal-kick assist.
   2. OPEN-PLAY BACKPASS, struck off the ground — VAN DER SAR, RIGHT foot. A rolling backpass
      collected in open play, three-step approach. A completely different act to a goal kick.
   3. DROP-PUNT OUT OF THE HANDS — CECH, LEFT foot, and ALISSON, RIGHT foot.
   4. OVERHAND THROW — SCHMEICHEL, RIGHT arm.
 So: four methods, not three, and not the five the title promises.

*** THE LINE NOBODY ELSE HAS ON THIS PACK ***
 Every method that appears twice is split by side. The two struck off the ground split left and
 right: Ederson LEFT, Van der Sar RIGHT. The two drop-punts split left and right: Cech LEFT,
 Alisson RIGHT. And Schmeichel is the outlier who does not use a foot at all.
 Two of these are corrections earned this session: Cech's LEFT foot, and Ederson's goal kick.

────────────────────────────────────────────────────────────────────────
#5 EDERSON to AGUERO — Man City v Huddersfield, 2018/19. Clip at 00:12-00:38.

SOURCE: lower-third "Ederson / Manchester City v Huddersfield Town / 2018/19".
AUTHENTIC: real broadcast, no game UI.
READ OFF THE KIT: CITY sky blue shirts, white shorts, sky blue socks. Numbers legible: 10 AGUERO, 21 DAVID SILVA.
 HUDDERSFIELD fluorescent yellow and black, black shorts, yellow socks. Number legible: 26 SCHINDLER.
 EDERSON all orange. Ben Hamer all red. Referee all black.
BOARDS: Touchline: PRECISION · PHANTOM VSN · SPEED · HYPERVENOM.
 High tactical view: BETADINE · UBTECH · Xylem · Prime Video.
DELIVERY: *** IT IS A GOAL KICK, NOT OPEN PLAY. *** Dead ball from inside the six-yard box, three to four
 paces of approach, struck off the turf with the LEFT foot. Low, flat and driven rather than lofted —
 it never climbs high. One bounce just outside the Huddersfield arc, straight into Aguero's stride.
 DISTANCE: the written record reports it at 85-86 yards. Footage alone cannot measure this, so quote
 the reported figure and attribute it, or say "from his own six-yard box" and let that do the work.
ACTION: Aguero waits between the two centre-backs near the edge of the final third. Both turn and sprint
 back. Hamer races off his line and outside his box. Aguero takes one soft RIGHT-foot touch to round
 the committed keeper and step inside the recovering defender, then finishes with the LEFT — a chip
 over the stranded keeper into the open net.
CELEBRATION: Aguero wheels to the corner flag, right arm up, then embraces David Silva (21) and Bernardo Silva.
 The tactical wide catches GUARDIOLA ON THE TOUCHLINE WITH BOTH FISTS PUMPING. Ederson gets no
 close-up of his own.
CAMERA: 00:12-00:22 high sideline, the ball from Ederson to the finish. 00:22-00:28 pitch-level on the
 celebration. *** 00:29-00:38 static high tactical wide — CUT ON THIS. *** It holds both players,
 the whole ball flight and Guardiola's reaction in one unbroken frame, which is the shot that sells
 the distance.
COMMENTARY: "Sergio Aguero up the pitch, and Aguero's been found, and the goalkeeper's come off his line...
 and Aguero goes for elevation, and achieves perfection! And Pep Guardiola indulged in the most
 joyous of fist pumps."
CANNOT DETERMINE
 The number of the second recovering Huddersfield defender. Ederson's exact contact frame — the
 primary angle is too distant, and the LEFT foot call rests on the follow-through rather than the
 contact itself.

────────────────────────────────────────────────────────────────────────
#4 ALISSON to SALAH — Liverpool v Man United, 2019/20, Anfield. Clip at 00:00-00:11.

SOURCE: lower-third "Alisson / Liverpool v Manchester United / 2019/20".
AUTHENTIC: real broadcast, no game UI.
READ OFF THE KIT: LIVERPOOL all red. Number legible: 11 SALAH.
 MAN UNITED savannah/tan away shirts, black shorts, light socks. Numbers legible: 21 DANIEL JAMES,
  29 WAN-BISSAKA.
 ALISSON all black with fluorescent yellow-green gloves. DE GEA purple. REFEREE SKY-BLUE SHIRT with
  black shorts — worth noting, it is not the usual all-black and it dates the clip.
BOARDS: LEARNING TO PLAY THE LIVERPOOL WAY (with its Spanish line, APRENDER A JUGAR EN LA MANERA DE
 LIVERPOOL) · LFC OFFICIAL MEMBERSHIP · STAND RED / STANDARD CHARTERED.
DELIVERY: Alisson claims a loose ball in his own box after a United attack breaks down, carries it three to
 four rapid strides to the edge of the area and strikes it DIRECTLY OUT OF HIS HANDS — a low
 side-volley drop-kick, RIGHT foot. Flat and fast, skimming over the retreating United players at
 medium height rather than looping. One bounce just inside the United half.
ACTION: Salah starts his sprint inside his OWN half, which is what keeps him onside and is the detail the
 commentary leans on. James (21) recovers and leans into him around 25 yards out. Salah holds him
 off with his body, lets the bounce settle, then guides it forward with his LEFT into the box.
 De Gea advances and spreads; Salah strikes with the INSIDE OF THE LEFT, low and under him, into the
 bottom right.
CELEBRATION: Salah pulls his shirt off and wheels away to the Kop.
 *** THE CLIP CUTS AT 00:11, BEFORE ALISSON'S RUN. *** Alisson's length-of-the-pitch sprint and
 knee-slide into Salah — the most famous image of this goal — IS NOT IN THIS SOURCE. It cuts
 straight to Ederson. If you want that celebration you need a second clip for it.
CAMERA: One single unbroken high sideline pan, left to right, from the Liverpool box to the United goal.
 No cuts, no replays inside the window. Clean to cut, but you only get the one look.
COMMENTARY: "And Alisson saw Salah... running from his own half, so onside here, Mo Salah... Salah to settle it!"
CANNOT DETERMINE
 The numbers of the players clustered in the Liverpool box at 00:00. Everything after 00:11.

────────────────────────────────────────────────────────────────────────
#3 SCHMEICHEL to SOLSKJAER — Man Utd v Sunderland, 1996/97, Old Trafford. Clip at 06:56-07:13.

SOURCE: lower-third "Peter Schmeichel / Manchester United v Sunderland / 1996/97".
AUTHENTIC: real 1990s Sky Sports broadcast, no game UI.
PICTURE: the era is the appeal, so describe it honestly
 Original 4:3 standard definition inside a 16:9 container, with BLURRED PILLARBOX BARS sampled from
 the centre of the frame filling the sides. 576i/480i upscaled to 1080p. Analogue softness,
 compression noise, chroma bleed that is worst on the reds, and visible interlacing judder on the
 fast pans. Do not try to hide this. Say "1996" on camera and the picture becomes the point.
READ OFF THE KIT: UNITED red Umbro shirts with the black-and-white fold-down collar, white shorts, black socks.
 SUNDERLAND white shirts with navy and red trim, black shorts, white socks.
 SCHMEICHEL the famous Umbro keeper shirt — dark purple/violet and black geometric pattern on the
  torso, purple sleeves, dark shorts, white gloves.
 LIONEL PEREZ bright yellow long sleeves, dark shorts. REFEREE all black.
 Number legible: 2 KUBICKI at 07:03. Solskjaer's 20 is NOT legible from behind at this resolution.
BOARDS: period advertising, and it sells the year better than any caption
 SHARP and SHARP VIEWCAM · McDONALD'S · CARLING · CIS INSURANCE · RYMAN · WILKINSON SWORD ·
 KELLOGG'S FROSTIES WITH TONY THE TIGER ON THE HOARDING.
DELIVERY: Sunderland put a set piece into the United box. After a partial deflection Schmeichel CATCHES it
 cleanly above head height near his six-yard line, turns immediately, takes two quick strides and
 launches an OVERHAND, JAVELIN-STYLE THROW with his RIGHT ARM. Flat and driving, clearing the
 halfway line on the fly and pitching around 55-60 yards downfield.
 NOTE: an earlier pass put this at 45-50 yards. The scoped pass says 55-60. Neither is measurable
 from the footage, so say "past the halfway line on the full" — which IS visible — and skip the number.
ACTION: Solskjaer is already running the blindside across halfway in the right-centre channel. Kubicki (2)
 goes to head the bounce at the centre circle, MISTIMES HIS JUMP AND MISSES IT COMPLETELY. Solskjaer
 takes it in stride, drives into the box unchallenged, and CHIPS IT with his RIGHT foot over the
 onrushing Perez into the middle of the net.
CELEBRATION: Away to the right corner flag and the Stretford End, shouting, arms pumping, tugging at his collar.
CAMERA: 06:56-07:00 high wide on the United box. 07:00-07:10 the same camera panning hard left to right
 through the throw, the bounce, the run and the goal — it is one continuous shot, which is rare and
 makes the distance legible. 07:11-07:13 low pitchside on the celebration.
COMMENTARY: Martin Tyler
 "...and Schmeichel's throw could put Solskjaer in. Kubicki's missed the challenge! And Solskjaer is
 all on his own! ... Isn't that a cool finish!"
CANNOT DETERMINE
 Player names on shirt backs — the SD resolution will not carry them, and several kits of this era
 did not print names at all. The smaller far-side hoardings. The throw distance as a number.

────────────────────────────────────────────────────────────────────────
#2 CECH to DROGBA — Wolves v Chelsea, 2009/10, Molineux. Clip at 01:24-01:53.

SOURCE: lower-third "Petr Cech / Wolverhampton Wanderers v Chelsea / 2009/10".
AUTHENTIC: real broadcast, no game UI.
READ OFF THE KIT: CHELSEA lilac/light blue third shirts with navy trim, lilac shorts, white socks with blue detail.
 WOLVES old gold with black collar and shoulder trim, black shorts, amber socks with black bands.
 CECH black long-sleeve adidas with NEON/ACID-GREEN stripes down the sleeves and shoulders, black
  shorts, neon green socks, SAMSUNG sponsor, and THE BLACK RUGBY-STYLE HEADGUARD. Number 1.
 HAHNEMANN bright light-green long sleeves, dark shorts. Referee all black.
 Legible: DROGBA 11 · CECH 1 · 16 BERRA.
BOARDS: CarPlan / CarPlan Triplewax · Barclays · Lucozade Sport · Carling · The Money Shop ·
 sportingbet.com · Carlsberg.
DELIVERY: *** CORRECTED THIS SESSION: IT IS THE LEFT FOOT. ***
 An earlier pass said right. A dedicated tie-breaker on the close replay says LEFT and grades itself
 CERTAIN, with the contact frame fully visible, centred and unobscured. The evidence it cites: he
 PLANTS ON THE RIGHT leg, the LEFT leg swings back and drives up through the ball, the LEFT boot
 connects just after release, and he leans his upper body back and slightly right while the LEFT leg
 extends high on the follow-through. Two passes now say left. Treat it as settled.
 The action: ball in both hands inside the box, he points upfield with his right hand to send the
 runners, takes two measured strides, drops it and punts it OUT OF THE HANDS. This one is the
 opposite of Alisson's — high and booming, climbing above the floodlight line before dropping. One
 bounce just outside the Wolves box.
ACTION: Drogba starts on Berra's blindside just inside the attacking half. Berra (16) tracks back and tries
 to hold him off with body and outstretched arm; Drogba muscles straight past him on the bounce
 without breaking stride. Hahnemann rushes out and slides to smother. Drogba takes it past him with
 the OUTSIDE OF THE RIGHT BOOT and rolls it into the empty net with the RIGHT.
CELEBRATION: Straight to the corner and the away end, fists pumping, and he LEAPS ONTO THE PERIMETER WALL where
 the travelling Chelsea support lean over and mob him. Cech is NOT shown celebrating — the broadcast
 cuts to replays.
CAMERA: 01:24-01:30 close on Cech directing traffic with the ball in his hands. 01:30-01:37 high wide
 tactical: the punt lands, Drogba beats Berra, rounds the keeper, scores. 01:37-01:41 medium on the
 celebration at the wall. 01:42-01:44 low close replay of the punt — this is the one that settles
 the foot. *** 01:44-01:53 pitch-level slow-motion following the Berra duel and the finish — CUT ON
 THIS. ***
COMMENTARY: "This is Didier Drogba... In behind Berra... It's Drogba! That could be the fatal blow for Wolves!
 Didier Drogba with his second, and Chelsea's second, and they look to be extending their lead at the
 top of the Barclays Premier League. Full marks to Drogba, but absolutely desperate defending from
 Wolves."
AUDIO: A loud away-end roar against groans and near-silence from the Molineux home crowd. The contrast is
 usable if you keep the natural sound.
CANNOT DETERMINE
 The exact number of strides before the punt — the broadcast cuts to him mid-run-up at 01:28. The
 numbers of the Wolves defenders chasing behind Berra.

────────────────────────────────────────────────────────────────────────
#1 VAN DER SAR to ROONEY — Man Utd v Aston Villa, 2010/11, Old Trafford. Clip at 04:14-04:45.

SOURCE: lower-third "Edwin van der Sar / Manchester United v Aston Villa / 2010/11".
AUTHENTIC: real broadcast, no game UI.
READ OFF THE KIT: UNITED red shirts with white and black collar trim, white shorts, black socks. Numbers legible:
  10 ROONEY, 3 EVRA, 5 FERDINAND, 24 FLETCHER, 17 NANI.
 VILLA dark navy/black with light blue trim, dark shorts, dark socks. 19 COLLINS and 5 DUNNE
  tracking back.
 VAN DER SAR purple with black and white trim, black shorts. FRIEDEL bright yellow. Referee all black.
BOARDS: BARCLAYS · Nike Football.com · "Join the global Barclays Football facebook page" /
 facebook.com/barclaysfootball. The Facebook board is a period marker worth a beat on camera.
DELIVERY: *** OPEN PLAY, NOT A DEAD BALL — this is what separates it from Ederson's. ***
 Van der Sar collects a ROLLING BACKPASS inside his own box, lines up a THREE-STEP approach and
 strikes it cleanly OFF THE GROUND with his RIGHT foot. High and looping, the opposite shape to
 Ederson's flat drive. Roughly 70 yards, dropping near the Villa box and taking one forward bounce
 into Rooney's stride.
ACTION: Rooney starts just inside the attacking half and runs the gap between the two Villa centre-backs,
 who are caught flat and cannot deal with the bounce. Rooney CUSHIONS IT WITH HIS RIGHT, lets it sit,
 and strikes a HALF-VOLLEY with the INSTEP OF THE RIGHT into the right side of the net. Friedel dives
 left and gets nowhere near it.
CELEBRATION: the best aftermath in the pack, and it runs long
 Rooney sprints to the corner flag and BLOWS KISSES TO THE CROWD WITH BOTH HANDS, arms wide.
 NANI leaps onto his back first, then FLETCHER, then FERDINAND.
 *** THEN THE SHOT WORTH BUILDING THE ENDING ON: the camera cuts BACK TO VAN DER SAR at his own end,
 pumping both fists. FERDINAND JOGS THE LENGTH BACK TO EMBRACE HIM, and then EVRA LEAPS INTO VAN DER
 SAR'S ARMS. *** No other clip in this pack shows the keeper being celebrated. End the video here.
CAMERA: 04:14-04:25 elevated sideline, the long ball box to box and the goal. 04:25-04:32 low pitchside on
 Rooney. *** 04:32-04:38 tight on Van der Sar with Ferdinand and Evra — the money shot. ***
 04:38-04:45 high sideline replay of the trajectory and the finish.
COMMENTARY: "Wayne Rooney on the charge. Rooney's in, and Rooney scores! One chance, one goal, and he will feel
 a whole lot better now... Edwin van der Sar playing his part, and Rooney was ruthless."
CANNOT DETERMINE
 The numbers of the distant Villa players chasing back. The peak height of the delivery.

────────────────────────────────────────────────────────────────────────
CANNOT DETERMINE, ALL FIVE
 The match clock and the scoreline for every one of the five — the compilation carries no scorebug
 on any clip. Do not put a minute or a score on screen for any of these.
 All distances. Only Ederson's has a figure in the written record; the rest are estimates from the
 footage and they moved between passes. Describe the geography instead of quoting yards.
```

#### `deep/oscar-2.md`
<!-- FILE: deep/oscar-2.md · 23707 bytes · 271 lines · sha256 5ca5effee9e0f7877d0c63f477ffdff8b9c6162736a2b10e51b2fe3d824376b7 -->
*22 Sep: the ordering suggestion marked [RESOLVED 20 Sep 2026] — Joel kept the approved order.*
```markdown
# DEEP PASS — TOP 5 PLAYERS WHO DESERVE THE OSCAR AWARD PART 2

*** TWO PICKS CHANGED SHAPE IN THIS PASS. Pick #2 finally has a named moment, and it is a much better
one than "a second Suárez dive". And pick #3, Embolo, turns out to be far bigger than it was ranked —
a World Cup red card for simulation that also overturned a card given to the opponent. Ordering note at
the bottom. ***

════════════════════════════════════════════════════════════════════════
#5 NEYMAR — Brazil v Mexico, 2018 World Cup. SOURCE: 9qjGKKitwXo at 01:46–02:38.

[!!] *** THE MEME IS WRONG AND SO WAS THE PACK. HE ROLLS ONCE. *** Not three, not four, not across the
 pitch. He drops onto his back, twists over ONCE onto his side and stomach, and writhes IN PLACE,
 travelling virtually no distance, staying just over the touchline. Every clip that shows more than that
 is edited: the first source I checked looped the roll back and forth, and this one SCRUBS IT FORWARD
 AND BACKWARD REPEATEDLY inside a red circle at 02:20–02:38. If you say "he rolled four times" on camera,
 the top comment corrects you, and it will be the ANTI-FACTUAL kind that already tops your biggest videos.

[!] SOURCE WARNING: this clip is ALSO manipulated — a permanent laughing emoji top right, a "Max daSilva"
 watermark at 01:09, original audio entirely stripped and replaced with electronic dance music, and the
 scrub-loop described above. The LIVE segment at 01:46–02:00 and the first three replays are clean; the
 fourth is not. *** AND FIFA'S OFFICIAL HIGHLIGHTS (kYIf8I1dvdo) DO NOT CONTAIN THE INCIDENT AT ALL —
 I checked. It is absent from the official 2-minute summary. There is no clean official source. ***

SCENE: Brazil YELLOW with green collars, blue shorts, white socks with yellow, YELLOW BOOTS.
 *** "NEYMAR JR" 10. *** Mexico GREEN with a subtle zig-zag pattern, white shorts, DARK MAROON/BURGUNDY
 SOCKS with white "adidas" lettering and three white stripes, dark boots. *** "LAYUN" 7 on shirt and
 shorts, BLEACHED-BLONDE HAIR. *** Also CORONA 17 walking nearby at 02:05–02:07.
 Referee Gianluca Rocchi in LIGHT CYAN/BLUE, black shorts, black socks with cyan trim.
 Bright daylight with stadium-roof shadows across a pristine pitch. Full stadium.
 TITE is on the touchline in a dark suit and white shirt.
 BOARDS: POWERADE · QATAR AIRWAYS · GAZPROM · COCA-COLA · ADIDAS.COM · HYUNDAI · VIVO · NEX · WANDA.
 SCOREBUG at 01:46: Brazil flag · "BRASIL 1" · centre "2T 25:21" · "0 MÉXICO" · Mexico flag ·
 subtext under Brazil "Neymar 6' 2T". So: 70th minute, Brazil leading 1-0 through Neymar.
THE INCIDENT: LOCATION: on and just outside the touchline, DIRECTLY IN FRONT OF THE BRAZILIAN TECHNICAL AREA AND BENCH.
 Neymar is tackled and knocked out of play. He sits up, then reclines just across the white line and
 *** TRAPS THE MATCH BALL BETWEEN HIS ANKLES AND LOWER SHINS to stop Mexico restarting quickly. That
 detail matters — he starts it. ***
 LAYÚN steps over to retrieve the ball. While reaching down for it with both hands, he *** PLANTS HIS
 RIGHT BOOT DIRECTLY ONTO NEYMAR'S RIGHT ANKLE AND SHIN AND PRESSES HIS WEIGHT DOWN. *** That is a
 genuine stamp, not nothing.
 REACTION: Neymar drops onto his back, screams with his mouth wide open, twists over ONCE, clutches his
 RIGHT ANKLE with both hands, throws his head back, kicks his LEFT leg, and covers his face with his
 right hand. He stays down for the rest of the clip.
 DECISION: Rocchi comes over, separates Layún from the Brazilian bench and signals for calm. *** NO CARD
 IS SHOWN to anyone in this footage. *** Two Brazilian medical staff in white come on at 01:59 with water
 and a kit and treat the right ankle. The clip ends before any restart.
CAMERA: live wide tracking down the touchline zooming in, then a high overhead of the medics at 01:59.
 Replay 1 high elevated touchline — Layún walking up, standing on the ankle while grabbing the ball, and
 TITE REACTING ANGRILY. Replay 2 ground-level slow-motion close-up on the grimace and the single twist.
 Replay 3 high overhead of the bench and referee intervening. Replay 4 the manipulated scrub.
AUDIO: none of it is original. Commentary, whistle and crowd all removed, replaced with dance music.
THE HONEST SCRIPT: the funniest version is also the true one — he trapped the ball between his feet to
 waste time, a man stood on his ankle for it, and the internet turned one roll into a worldwide challenge.

════════════════════════════════════════════════════════════════════════
#4 MICAH RICHARDS — Aston Villa v Stoke. SOURCE: RscP6Vaghd4 (CBS Sports Golazo).
ARCHIVE DIVE at 00:59–01:20, replayed in EXTREME SLOW MOTION at 01:26–01:42.
*** THIS SOURCE IS THE PICK. It is the clip AND the punditry in one, which is exactly why he was chosen —
 the man is on air being shown his own dive by Henry and Carragher. ***
THE DIVE: Villa CLARET body with SKY-BLUE SLEEVES, collar and side panels, white shorts, sky-blue socks
 with claret. A teammate at 01:05 shows the "QuickBooks" chest sponsor and a Premier League sleeve patch.
 *** "RICHARDS" 4 read off his back as he turns and dives. *** Stoke in RED AND WHITE VERTICAL STRIPES
 with white sleeves and red cuffs, white shorts, white socks — *** "WOLLSCHEID" 26 legible at 01:31. ***
 Bright natural daylight with distinct player shadows, dry manicured grass. No referee in frame, no
 scorebug, no boards visible — the framing is tight on the pitch. Studio bugs only: Paramount+ top left,
 @cbssportsgolazo bottom left, the CBS eye bottom right.
 BEAT BY BEAT: just outside or on the edge of the box, a white line cutting the lower frame. Richards
 touches the ball forward with his RIGHT boot as Wollscheid and a second defender close. The defender
 plants his foot and makes *** MINIMAL TO NO VISIBLE CONTACT. *** Richards then LAUNCHES HIS WHOLE BODY
 FORWARD HORIZONTALLY INTO THE AIR, completely parallel to the ground at WAIST-TO-CHEST HEIGHT, in a
 Superman posture — BOTH LEGS KICKING UP BEHIND HIM, left arm extended forward, head tilted. He flies
 TWO TO THREE METRES through the air before crashing down chest-and-stomach first and skidding across the
 turf. His teammate shoots just past him while he lies prone. The referee is never in shot, so the
 decision cannot be seen.
THE STUDIO — panel: KATE ABDO far left, blonde curly hair, strapless dark leather dress · THIERRY HENRY
 second left, bald, dark suit, white shirt, dark tie, white pocket square · JAMIE CARRAGHER second right,
 short grey hair, dark suit, patterned waistcoat and tie · MICAH RICHARDS far right, clear-framed
 glasses, dark grey jacket, white shirt, striped tie. Curved blue desk with the UCL starball and
 "CHAMPIONS LEAGUE", video wall behind.
 VERBATIM, and every one of these is a caption:
  Carragher: "Where do you think he learned it from? Micah Richards."
  Richards: [groans] "Oh, no."
  Carragher: *** "What are you doing?!" *** … "What is that?!"
  Henry: "Micah, what are you doing?"
  Carragher: *** "Look at that! I have never seen anything like that! Look where his boots are!
   Look where his boots are!" ***
  Henry: "Can we see that again? He landed — *** he landed on his lips! *** "
  Henry: *** "Oh! Freeze! Why so high?!" ***
  Carragher: *** "Look at him swimming!" ***
  Henry: *** "I think that's my cue to leave." ***
 REACTIONS: Richards grimaces and grabs his glasses at the set-up, then bursts out laughing, COVERS HIS
 FACE WITH HIS PAPERS, puts both hands on his head and LEANS ALL THE WAY BACK IN HIS CHAIR. Carragher
 points at the screen, shouts, SLAPS THE DESK WITH HIS PAPERS. Henry gestures at the production screen
 asking for the replay and mimes the landing. Abdo laughs holding her cue cards.
 Live studio mics only — no music, no added effects.

════════════════════════════════════════════════════════════════════════
#3 BREEL EMBOLO — Switzerland v Argentina, World Cup 2026. SOURCE: 1O-qw6iaLOk at 00:00–02:10.
*** THIS IS BIGGER THAN ITS RANKING. A red card for simulation at a World Cup, which ALSO overturned a
 yellow already shown to the opponent, reviewed by VAR under a banner reading "mistaken identity".
 See the ordering note at the bottom. ***
*** VERIFIED IN TEXT, AND THERE IS A MUCH BIGGER STORY THAN THE DIVE. ***
 The red card is real and heavily reported — CNN, ESPN, Sky Sports, Yahoo, The National. 72nd minute.
 Referee João Pinheiro books PAREDES for the challenge; VAR intervenes; Pinheiro decides Paredes made no
 contact and Embolo dived; Paredes' yellow is rescinded and Embolo gets a second yellow and goes.
 Argentina won 3-1 in extra time with the extra man.

*** THEN, THREE WEEKS LATER, IFAB SAID THE SENDING-OFF SHOULD NEVER HAVE HAPPENED. ***
 Not that the dive was fine — that the VAR had no right to review it at all. IFAB's wording:
 "A yellow card (caution) which is not a second yellow card can only be reviewed to identify the player
 who committed the offence that was penalised; the offence itself cannot be reviewed/changed."
 VAR cannot review simulation unless a penalty or a straight red is involved, and the "mistaken
 identity" clause did not apply. FIFA pushed back, saying its interpretation of mistaken identity
 "was applied consistently throughout the FIFA World Cup" and that the call "restored justice".
 IFAB has said the point "will be included in the detailed review of the VAR protocol".

 THAT is the entry. Not "a man dived". A man dived, got sent off for it at a World Cup quarter-final,
 his team lost with ten, and the lawmakers of the game then said the red card was illegal. Nobody
 ranking football dives has that ending, because it only emerged three weeks after the match.
 It also settles the ranking argument on its own — see the note at the bottom.

[!] I first checked 0nx7R28uRPQ and it is unusable — 14 seconds of real footage, then STATIC PHOTOS with
 an AI SYNTHETIC VOICEOVER. This source is the real one: moving broadcast footage at game speed plus
 three slow-motion angles, with a human Brazilian-Portuguese narrator.
SCENE: Switzerland RED with white accents and white Puma logos, red shorts, red socks.
 *** "EMBOLO" 7. *** Also FREULER 8, RODRIGUEZ 13, 15, ZAKARIA 6, RIEDER 22.
 Argentina sky-blue and white stripes with black adidas shoulder stripes, white shorts, white socks with
 sky-blue trim. *** "PAREDES" 5 *** and "L. MARTINEZ" 6.
 Referee in FLUORESCENT NEON YELLOW with black collar and side panels.
 Night, full floodlights, dry pitch, big packed bowl.
 Pitchside staff bibs read "SECURITY 6566", "SECURITY 6533" and "WORLD CUP 2026".
 BOARDS: Michelob ULTRA · POWERADE · WORLD CUP 2026.
 SCOREBUG: "ARG 1 - 1 SUI" with flags, clock running through 66:54, 68:13, 68:47, 70:08, 71:20.
 Broadcaster bug: *** CazéTV with the World Cup trophy icon and "EMISSORA OFICIAL". ***
 VAR GRAPHIC bottom left at 01:03–01:38: a green "VAR" badge, "REVISÃO", and a white box reading
 *** "ERRO DE IDENTIFICAÇÃO". *** Lower right: "FIFA VAR ROOM". Channel watermark "WILL DE OLHO NO LANCE".
THE INCIDENT: LOCATION: just outside the Argentina box, slightly right of centre, near the penalty arc.
 Embolo chases a ball to the edge of the area. PAREDES (5) and L. MARTÍNEZ (6) converge.
 Paredes plants his left leg and swings his right toward the ball's path.
 *** BEFORE ANY COLLISION, EMBOLO IS ALREADY HORIZONTAL AND AIRBORNE — the narrator's word is
 "flutuando", floating. While in the air he EXTENDS HIS TRAILING RIGHT LEG OUTWARD TO SEEK PAREDES'
 LEG. The only contact in the whole incident is contact HE initiates, from mid-air. ***
 He lands chest-first, slides several feet, flips onto his back and clutches his face and head with both
 hands, rolling slightly.
THE DECISION — and this is the part that makes it a #1 candidate:
 1. The referee stops play and BOOKS PAREDES at 68:47. Argentina are punished.
 2. VAR intervenes. On-field review under "VAR REVISÃO: ERRO DE IDENTIFICAÇÃO". The screen shows a
    THREE-WAY SPLIT — the referee at the pitchside monitor, the FIFA VAR room, and the slow-motion of
    Embolo's unprompted leap.
 3. Paredes' yellow is RESCINDED.
 4. Embolo, already on a yellow, is shown a SECOND YELLOW AND THEN THE RED at 71:20. Switzerland to ten.
AFTERMATH: Embolo sits on the pitch, then stands with his hands on his head, visibly stunned and
 distraught. *** HE IS NOT VISIBLY CRYING ON CAMERA — one of the other uploads is titled that way and
 the footage does not support it. Do not say he cried. *** Freuler and Rodríguez surround the referee
 gesturing. Paredes speaks to the referee. Bench and staff watch the review from the sideline.
CAMERA: low-angle ground camera tracking the slide in real time (00:00–00:05) · freeze frame · tight low
 SLOW MOTION on the footwork and contact (00:20–00:37) · *** REVERSE SIDELINE ANGLE SHOWING HIM MID-AIR
 BEFORE ANY CONTACT (00:38–00:58) — that is the shot that proves it *** · the yellow to Paredes · the
 three-way VAR split · the red card close-up with Swiss players protesting.
NARRATION (Brazilian Portuguese, human not AI): "o Embolo se joga… ele se joga, estica a perna pra bater
 no Paredes. *** Não foi absolutamente nada! *** " (he throws himself… he throws himself, sticks his leg
 out to hit Paredes. It was absolutely nothing!)
 And on the graphic: "Na revisão está escrito 'Erro de identificação'… o VAR chama para anular o cartão
 do Paredes, o Embolo já tinha amarelo, toma o segundo amarelo e é expulso."

════════════════════════════════════════════════════════════════════════
#2 LUIS SUÁREZ — the Chiellini bite, Italy v Uruguay, 2014 World Cup. SOURCE: 1tVdCQaH0vs.
*** THE HOLE IN THIS PACK IS FILLED. "A second Suárez dive" now has a named moment, and it is not a dive
 at all — it is better. He bites a man and then goes down HOLDING HIS OWN TEETH as though he is the
 victim. It cannot be confused with Part 1's throat-clutch against PSG. ***
AUTHENTIC: real broadcast, ESPN. Official FIFA graphics, Brazuca ball. Publisher adds only a "Thanks for watching!"
 card at the end. No music, no effects.
SCOREBUG: "2014 FIFA WORLD CUP™ - GROUP D" / ESPN logo / *** "ITA 0 - 0 URU  78:25" running to 79:47 ***
 / sub-bar: *** "ITALY: PLAYING WITH 10 MEN". ***
SCENE: Italy ROYAL BLUE Puma with tonal pinstripes, white FIGC crest, white Puma cat, blue shorts, blue
 socks. Buffon in BURGUNDY/MAROON long sleeve with a BRIGHT YELLOW CAPTAIN'S ARMBAND.
 Uruguay WHITE Puma with light blue collar and cuffs, AUF crest, white shorts, white socks.
 Referee Marco Rodríguez in NEON YELLOW with black collar and shoulder piping.
 READ OFF THE KIT — Italy: CHIELLINI 3 · DE SCIGLIO 2 · CASSANO 10 · BONUCCI 19 · PIRLO 21 · BUFFON 1.
 Uruguay: *** L. SUÁREZ 9 *** · D. GODÍN 3 · C. STUANI 11 · M. PEREIRA 16 · G. RAMÍREZ 18 · CÁCERES 22.
 Bright sun with high-contrast diagonal canopy shadows across the pitch, diagonal mower stripes.
 BOARDS: Garoto · Garoto · Liberty Seguros · CENTAURO.COM.BR · Garoto · Liberty Seguros, and on the LED
 run a repeating "FIFA 11 FOR HEALTH" / "Football for Health".
THE INCIDENT: inside Italy's box, about halfway between the six-yard box and the penalty spot, left of
 the goalmouth. A Uruguayan ball comes in. Chiellini is SCREENING Suárez off, between him and the goal.
 Suárez presses into his back, then LUNGES FORWARD AND DOWNWARD, driving his mouth and head into the
 TOP/BACK OF CHIELLINI'S LEFT SHOULDER. Chiellini recoils and swings his left elbow back to push him off.
 The contact lasts about half a second. Both go down.
THE REACTION — this is the pick:
 *** SUÁREZ drops forward onto his knees and right hip, rolls onto his back and side, and INSTANTLY PUTS
 BOTH HANDS TO HIS FACE. At 00:11–00:15 he is sitting hunched over his knees, CUPPING HIS MOUTH AND
 CLASPING HIS UPPER FRONT TEETH with both hands, as if his mouth had been the thing that was hurt. ***
 On the replays at 00:31–00:35 he is writhing on his back, eyes closed, mouth grimacing, right hand over
 his teeth. At 01:07–01:10 he stands and *** PULLS HIS COLLAR COMPLETELY OVER HIS MOUTH AND NOSE, *** then
 lowers it to point his index finger and protest innocence.
 CHIELLINI falls on his stomach clutching his left shoulder, sits up shouting and gesturing at it, then
 at 00:52–01:05 RUNS TO THE REFEREE AND YANKS HIS SHIRT DOWN OFF HIS SHOULDER to show the bare skin.
 *** THE REFEREE GIVES NOTHING. No foul, no penalty, no card. He waves play on. ***
CAMERA: live wide · a live ground-level medium at 00:11–00:16 with Chiellini pointing at his shoulder on
 the left and Suárez clutching his teeth on the right IN THE SAME FRAME · a ground-level profile replay
 of the head going in · a high reverse from behind the goal · the crane shot of the swarm · the
 pitch-level close-up of Chiellini pulling his shirt down · and a tight SLOW-MOTION side angle at
 01:11–01:23 showing the head snap and Suárez collapsing with his hands to his teeth.
COMMENTARY (English, ESPN) — verbatim, and it builds beautifully:
 "Oh, and a clash inside the penalty area involving Chiellini... that's left his Uruguayan opponent,
  Suárez, clutching his face." / "What's Chiellini claiming here?" / "Here it is again... oh dear. Oh."
 / "Oh, dear, dear, dear." / *** "It looks to me, dare I say it, that he's had a little bite at
 Chiellini." / "Surely not again." / "Surely not again." *** / "The head certainly went in Chiellini's
 direction." / "It can't be proved, but Chiellini's trying to make it obvious to everybody." /
 "...that's the third time that Luis Suárez has committed that particular crime. Once in Holland, where
 he became known quickly as the Cannibal, and then, more famously, against Branislav Ivanović."

════════════════════════════════════════════════════════════════════════
#1 RIVALDO — Brazil v Turkey, 2002 World Cup. SOURCE: OiW0IPrv1Ro (2.55M). 25s.
AUTHENTIC: real broadcast. SD, 4:3, analog compression, motion blur, softened edges. Not upscaled. No game UI.
SCENE: Brazil YELLOW with green collar and sleeve-seam trim, BLUE shorts with white numbering on the
 left leg, white socks with blue bands, WHITE BOOTS. *** RIVALDO 10, legible on his chest AND shorts. ***
 Brazil 17 also visible at 00:13–00:15.
 Turkey RED with white trim and white numbering, red shorts, red socks with white bands. Number 20
 visible; *** "FATIH AKYEL" legible on a back at 00:15 *** ; the keeper in DARK BLUE/GREY with white
 lettering reading *** "RÜŞTÜ" over number 1. ***
 Referee in ALL BLACK with white collar/chest details, black socks with white turn-downs. The assistant
 by the corner flag holds a YELLOW-AND-RED CHECKERED FLAG.
 Night, floodlights, dry manicured grass. A fan banner behind the boards reads "JORDANIA SINOP'TAN / DE
 CAFE DE ANEL / EN KINO..." (rest not legible).
 BOARDS at the corner arc: FIFAworldcup.com · AVAYA · "com" with the 2002 kicking-figure logo · purple
 boards with yellow stylised lettering. Along the goal line and far touchline: JVC · Budweiser · KT · KT
 · AVAYA · Yahoo! · PHILIPS · FUJITSU · Gillette.
 NO SCOREBUG, no clock, no score, no broadcaster logo anywhere.
THE INCIDENT — and the whole joke is one body part:
 Rivaldo is standing IN THE CORNER ARC RIGHT BESIDE THE FLAG, waiting to take a corner, hands resting on
 his thighs, bent slightly forward.
 At 00:01–00:03 a Turkish player outside the box near the touchline strikes the dead ball with his RIGHT
 foot, driving it ALONG THE TURF straight at him.
 It bounces low and *** STRIKES HIM SQUARELY ON THE UPPER RIGHT LEG — THIGH AND KNEE AREA. IT MAKES ZERO
 CONTACT WITH HIS TORSO, CHEST, NECK, HEAD OR FACE. ***
 He jerks upright, THROWS BOTH HANDS TO HIS FACE AND EYES, and collapses BACKWARD — flipping back over
 his shoulders onto the turf and curling up in the angle between the pitch line and the hoardings,
 clamping both hands over his face as though he had been hit in the eyes or nose.
 At 00:13–00:14 the referee runs to the confrontation near the box and RAISES A RED CARD HIGH ABOVE HIS
 HEAD. Rüştü (1) and number 20 protest in disbelief.
CAMERA: medium close-up on him at the flag · wide pitchside of the kick and the fall · high tactical of
 the box · a tight ground-level replay of him rolling back holding his face · *** SLOW-MOTION CLOSE-UP AT
 00:08–00:12 THAT DEFINITIVELY SHOWS THE BALL HITTING HIS THIGH AND KNEE *** · the red card · and a
 SECOND slow-motion from corner level repeating the leg contact. The evidence is shown twice. Use it.
AUDIO: NO COMMENTARY AT ALL. Crowd barely audible. The publisher has replaced everything with an
 instrumental hip-hop/breakbeat track with vinyl scratches. You carry this one on your own voice.

════════════════════════════════════════════════════════════════════════
*** ORDERING NOTE — worth thinking about before you shoot ***
The formula wants #1 to be the consensus finisher with a hard declarative, and Rivaldo is exactly that:
untouched above the waist, sent a man off, FIFA fined him, and the slow motion proves it on screen.
Keep him at #1.
But EMBOLO at #3 is now underweighted. He is the only entry where the dive is punished ON THE PITCH, at
a World Cup, by VAR, with the opponent's card rescinded — and it happened two months ago, so it is the
only one your audience has not seen ranked a hundred times. That is a #4 at worst.
My suggestion, and I'd now push harder on it given the IFAB story: Embolo to #4, Micah Richards to #3. Richards holds #3 fine because the studio audio does
the work, and Embolo at #4 is where the most argumentative entry belongs. [RESOLVED 20 Sep 2026] YOUR CALL:
keep the approved order. Embolo stays at #3; the IFAB ending is carried by the script, not the ranking.

════════════════════════════════════════════════════════════════════════
CANNOT DETERMINE — ALL FIVE
 THE REFEREE'S REASONING in every case. What the official was thinking, and in the Embolo case what
  the VAR actually said, cannot be seen in footage. The IFAB ruling in this pack comes from the
  written record, not from the pictures — cite it as a ruling, not as something visible.
 THE RIVALDO CLIP carries NO SCOREBUG, no clock, no score and no broadcaster logo anywhere, so the
  minute cannot be stated from this source.
 THE HOARDING TEXT on the Rivaldo clip beyond "CAFE DE ANEL / EN KINO..." — the rest is not legible.
 WHETHER ANY OF IT WAS DELIBERATE. Simulation is a judgement about intent. The footage shows bodies,
  not minds. Describe what the player does and let the audience conclude — that is also the safer
  position if a clip ever gets challenged in the comments.
```

#### `deep/pace-abuser-2.md`
<!-- FILE: deep/pace-abuser-2.md · 23539 bytes · 268 lines · sha256 22a4fe4475ea378682664cfbbaa77f0e9e3340d96e6828235c8c0238234d0dc8 -->
*Header corrected 21 Sep — no touch count in the headline.*
```markdown
# DEEP PASS — TOP 10 PACE ABUSER MOMENTS PART 2 (runs 10 → 6)

*** THE PATTERN NOBODY WOULD NOTICE WITHOUT COUNTING: every one of these runs is ONE-FOOTED.
Son every touch right. Puhiri three, all right. Van de Ven five, all left. Adeyemi five, all left.
At full sprint nobody switches feet. That is a real observation and it is yours for free. ***

[!] CORRECTED: an earlier version of this line said "Son takes nine touches". Three separate passes
 returned 9, 10 and 11-12, so the COUNT is not stable and must not be quoted on camera. The FOOT is
 stable — a dedicated tie-breaker on the clearest slow-motion angle graded all eight visible touches
 RIGHT and CERTAIN, with zero left-foot contacts. Say "every touch with his right", never a number.
 The same caution applies to the other four: the feet held across passes, the totals did not.

════════════════════════════════════════════════════════════════════════
#10 SON HEUNG-MIN — Spurs v Burnley. SOURCE: C-CefuZ6h1k (Tottenham official, ALL ANGLES). 215s.
AUTHENTIC: real broadcast, Spurs TV edit. No game UI. NO SCOREBUG AT ALL — no clock, no score, no competition.
SCENE: Spurs WHITE with navy accents, navy "AIA" chest text, cockerel crest, swoosh. *** SON WEARS A
 WHITE SHORT-SLEEVE OVER A MATCHING WHITE LONG-SLEEVED COMPRESSION BASELAYER. *** Navy shorts with white
 numbers, white socks with navy.
 Burnley CLARET body with SKY-BLUE SLEEVES and collar, chest sponsor "LOVEBET" in white beneath WHITE
 CHINESE CHARACTERS (爱博). White shorts with claret trim, claret socks with sky-blue tops.
 Gazzaniga in LIGHT AQUA/TEAL long sleeve, matching shorts and socks, NEON YELLOW/BLACK GLOVES.
 NICK POPE in GREY long sleeve with darker panels, grey shorts and socks, LIME GREEN BOOTS,
 yellow/black/grey gloves. Referee ALL BLACK.
 READ OFF THE KIT — Spurs: Son 7 · Alli 20 · Lucas 27 · Vertonghen 5 · Alderweireld 4 · Sissoko 17 ·
 Kane 10 · Aurier 24 · Dier 15. Burnley: Lowton 2 · Tarkowski 5 · *** MEE 6, WEARING A MULTI-COLOURED
 RAINBOW CAPTAIN'S ARMBAND *** · Brady 12 · Hendrick 13 · Pieters 23 · McNeil 11 · Wood 9 · Rodriguez 19.
 Overcast daylight with the floodlights on. Pristine cut grass. Full stadium, standing.
 BOARDS: PRECISION (with swooshes) · GEAR UP ON NIKE.COM/FOOTBALL · KUMHO TYRE · PHANTOM SERIES ·
 upper ribbon "COME ON YOU SPURS".
 Watermark: cockerel + "SPURS TV" top right. Replays carry a "CLICK TO SUBSCRIBE" inset with cutouts of
 Kane, Lloris and Son. Outro at 03:20: "SUBSCRIBE" and "WATCH NEXT...".
THE RUN — EVERY TOUCH RIGHT-FOOTED (do not quote a total, see the correction above)
 ORIGIN: Burnley cross into the SPURS box. Tarkowski contests Vertonghen near the penalty spot;
  Vertonghen stops the header and the loose ball bounces out to the edge of the Spurs D.
 PICKUP: Son takes it ROUGHLY 20 YARDS FROM HIS OWN GOAL LINE, facing upfield, right-centre channel.
 1 right instep/laces, cushions the bounce into stride.
 2 right, into open space as McNeil 11, Rodriguez 19 and Hendrick 13 scramble to get back.
 3 right, slight push out — HE SCANS, looking at Alli and Kane for the pass. He chooses not to give it.
 4 right, carrying toward the edge of the centre circle, still in his own half.
 5 *** THE KEY TOUCH: right instep, threading it BETWEEN LOWTON (2) AND BRADY (12) as they close from
   both sides. Lowton lunges with an outstretched right leg and arm; Brady stretches across to
   body-check him. HE GOES THROUGH BOTH UNTOUCHED. ***
 6 right, a burst touch about 10 yards into the Burnley half, now at maximum speed. Mee 6 and
   Tarkowski 5 are retreating.
 7 right, holding a central line toward the edge of the Burnley box.
 8 right, a delicate touch to settle it just outside the 18 as MEE SLIDES IN from his right and
   LOWTON sprints back on his left shoulder.
 9 right, into the box, shifting it slightly right to open the angle across Pope.
 FINISH: 12–14 yards, slightly right of the penalty spot, INSIDE/INSTEP OF THE RIGHT FOOT, rolling past
  Pope's outstretched right leg and arm into the LOWER RIGHT CORNER.
 CELEBRATION: wheels to the left corner flag, arms wide, KNEE SLIDE, roars, mobbed.
DISTANCE: the footage shows him crossing his own D, his own half, the centre circle, the halfway line,
 Burnley's half and their 18-yard line. *** NO SPEED OR DISTANCE GRAPHIC APPEARS ANYWHERE. Do not quote
 a figure on camera — there isn't one in this footage. ***
CAMERA — TEN separate angles, which is why this source is the right one:
 1 live high wide (00:00–00:19) · 2 low-mid tracking replay · 3 high tactical gantry showing the lines
 being pierced · 4 elevated sideline zoomed on the run and shot · 5 high from behind the Spurs goal,
 full lengthwise view of the pitch · 6 ground-level sideline showing the Lowton and Brady lunges ·
 7 SLOW-MOTION from the midfield sideline on the control between the two of them · 8 low reverse behind
 him into the box catching the knee slide · 9 close-up slow motion on his footwork and sprint mechanics ·
 10 head-on slow motion from behind the Burnley goal (02:40–03:19).
COMMENTARY: "McNeil does so... Tarkowski under pressure from Vertonghen... can't bring it down, and...
 it's general terror in the Burnley backline when Son breaks forward! Oh wow, what a run! Heung-Min Son
 from inside his own half has scored one of the best goals of his Spurs career!"

════════════════════════════════════════════════════════════════════════
#9 TERENS PUHIRI — Borneo FC v Mitra Kukar. SOURCE: kjdKZOcXlbk (Guardian Football, 7.8M). 52s.
AUTHENTIC: real broadcast, Indonesian TV. No game UI.
SCENE: Borneo FC WHITE with maroon/red trim, white shorts, white socks, RED numbering on back and shorts.
 *** PUHIRI IS NUMBER 28. *** Mitra Kukar YELLOW/GOLD with red and black side panels, gold shorts with
 red trim, gold socks. Their keeper in MAGENTA/BRIGHT PINK long sleeve with black underarm panels, black
 shorts, black gloves with neon green-yellow accents. Officials in black; the linesman carries a
 YELLOW-AND-RED QUARTERED FLAG. Coaching staff in BRIGHT ORANGE POLOS with credentials round their necks.
 Night, floodlights. Grass slightly worn, VISIBLE SURFACE MOISTURE and divots catching the light.
 A BLUE-GREY ATHLETICS RUNNING TRACK surrounds the pitch. Packed multi-tier open stands in red, orange
 and white, jumping.
 BOARDS: abp · tvOne · PT Pupuk… · NIKE FOOTBALL · FWD · traveloka · GO-JEK · #KITA… ·
 TIKET.COM / GARUDA INDONESIA.
 BROADCAST GRAPHICS: "TV One / Borneo TV" top left · "BORNEO TV" with a green shield top right · "courtesy tvOne"
 bottom left · Guardian intro card "Terens Puhiri shows off his pace" · a "REPLAY" banner with a spinning
 ball 0:26–0:50 · teal Guardian outro. NO SCOREBUG — no score, no clock.
THE RUN — three touches, all RIGHT-FOOTED
 ORIGIN: a Mitra Kukar player shoots/crosses LEFT-FOOTED from outside the Borneo box; a Borneo defender
  CHARGES IT DOWN and the deflection runs forward past midfield into empty grass.
 START: Puhiri sets off from ABOUT 10 METRES BEHIND THE HALFWAY LINE. Explosive stride cadence, low
  centre of gravity, vigorous alternating arm drive. He is past a retreating yellow defender before the
  centre circle.
 1 outside/instep of the RIGHT foot, knocking it into space just inside the opposition half.
 2 *** the keeper has raced out of his box for a low sliding challenge. Puhiri gets there A FRACTION
   AHEAD and pokes it right with the OUTSIDE OF THE RIGHT BOOT, past the slide. ***
 He HURDLES THE GROUNDED KEEPER without breaking stride.
 3 from about 7 yards at a tight right angle, inside/laces of the RIGHT foot into the lower-middle net,
  past a defender scrambling back to the line.
 CELEBRATION: sprints at the corner flag and the technical area, arms out. A coach in a black windbreaker
  and MAROON CAP raises both fists. Teammate #12 embraces him. Staff and subs in orange mob the touchline.
  *** AND THE BEST SHOT: a close-up of the Mitra Kukar keeper bowing his head, looking at the turf. ***
SPEED GRAPHIC: NONE. Do not quote a number.
CAMERA: live wide 0:00–0:13 covering the whole sprint and finish in one pan; then six quick reaction cuts
 (coach, keeper, teammate hug, crowd, keeper again, staff); then three replays — wide tracking the full
 sprint, a reverse low touchline on the touch past the keeper, and a low frontal 3/4 on his running form.
COMMENTARY (Indonesian): "...Oh! Sebuah akselerasi kali ini! Terens Puhiri, masih Terens Puhiri, baik
 sekali Terens, Terens, Terens! Tendangan Terens Puhiri, GOOOOOL! Gol, gol, gol, gol, gol, gol, gol, gol,
 gol, gol, gol, gol! *** MAMAYOOO! *** "
 Analyst on the replay: "Terens Puhiri, pergerakannya, kecepatannya, betul-betul mampu memaksimalkan
 kelemahan di lini belakang dari Mitra Kukar. Ini adalah gol ketiga..." (his movement, his speed, really
 punished the weakness in Mitra Kukar's back line. This is the third goal.)

════════════════════════════════════════════════════════════════════════
#8 MICKY VAN DE VEN — Spurs v Copenhagen. SOURCE: h_stLgq5Rps (Tottenham official). Clip at 01:04–01:23.
[!] A GAMEPLAY FLAG WAS RAISED ON THIS AND IT IS WRONG. The analysis itself states there is NO visible
 game UI — no indicators, no stamina bars, no radar, no controller prompts — and then calls it a game on
 "synthetic 3D player models". This is TOTTENHAM'S OWN OFFICIAL CHANNEL, the commentary names Palhinha
 and Elyounoussi, and the boards are real UCL sponsors. By the rule, an official club channel with no
 visible UI means the model is wrong. See the recency pattern in the covering note.
SCENE: Spurs WHITE with navy trim, RED "AIA" chest text, cockerel crest, swoosh right chest, *** UCL
 STARBALL PATCH ON THE RIGHT SLEEVE. *** White shorts with dark accents, white socks.
 Copenhagen DARK GREEN with dark/black shoulder panels and gold/white detailing, green shorts, green socks
 with black/white bands. Chest sponsor not legible.
 Copenhagen keeper in BRIGHT SALMON-PINK head to toe, light gloves. Spurs keeper in light turquoise-blue.
 Referee BRIGHT YELLOW with black panels, black shorts, black socks with yellow bands.
 Night, floodlights, pristine grass in lateral stripes. *** At 01:19 a spectator in the front row is
 holding a DUTCH FLAG. *** Van de Ven in white boots with black accents.
 BOARDS: Mastercard · UEFA CHAMPIONS LEAGUE · Mastercard · bet365 · UEFA CHAMPIONS LEAGUE, then at the
 endline bet365 · Mastercard · FedEx.
 NO SCOREBUG, no graphics, no watermark. Numbers are NOT legible at this camera distance.
THE RUN — five touches, every one LEFT-FOOTED, and NOBODY TOUCHES HIM
 ORIGIN: Copenhagen are attacking the right side of the Spurs box. A Spurs defender pokes the ball clear
  into space about 5–7 yards outside the Spurs area in the left-centre channel — roughly 25–30 yards from
  his own goal line. Van de Ven strides onto it.
 1 left instep/laces, firmly into the centre circle, accelerating away from a retreating midfielder.
 2 left laces, across the halfway line. A trailing Copenhagen player cannot close.
 3 left laces, a heavier driving touch straight through the central channel, SPLITTING TWO RETREATING
   DEFENDERS who flank him. *** NEITHER MAKES CONTACT OR EVEN LUNGES. ***
 4 left instep/laces to the edge of the D. The ball never leaves his stride.
 5 left, a soft prep touch just inside the area, left of the penalty spot.
 FINISH: left instep/laces from 12–14 yards. The keeper advances and dives low to his right; it beats him
  low into the bottom corner — shooter's bottom right, keeper's bottom left.
 ZERO CONTACT from any opponent at any stage of the run.
DISTANCE: from ~25–30 yards off his own line to ~12–14 yards from theirs. NO metric graphic. Don't quote one.
CAMERA: ONE unbroken wide tactical sideline pan, 01:04–01:16, left to right the whole way. Then a
 field-level tracking cut of the celebration — he cups his LEFT HAND TO HIS EAR, knee-slides at the
 corner flag, and is mobbed by teammates and bench players in blue bibs. NO REPLAYS AT ALL.
COMMENTARY: "…and Elyounoussi's got some room, at least he did, but then Palhinha saw what was about to
 unfold, and off goes Van de Ven! Micky van de Ven! *** Going all the way! *** Micky van de Ven!"

════════════════════════════════════════════════════════════════════════
#7 KARIM ADEYEMI — Dortmund v Chelsea, UCL R16 first leg. SOURCE: nPZGlV1rBM4 (DAZN_DE). 91s.
AUTHENTIC: real broadcast. Official UCL graphics, DAZN bug. No game UI.
SCOREBUG: UCL starball · clock 62:20 running past 63:05 · "DOR 0  0 CHE" → *** "DOR 1  0 CHE" at 62:45. ***
SCENE: Dortmund YELLOW with black patterned shoulders, black Puma logo, BVB 09 crest, black "1&1" chest
 sponsor, black numbers, black shorts, yellow socks with thin black bands.
 READ OFF THE KIT: *** ADEYEMI 27 *** · Bellingham 22 · Emre Can 23 · Haller 9 · Özcan 6 · Süle 25 ·
 Schlotterbeck 4 · Guerreiro 13. Keeper Alexander Meyer in BRIGHT GREEN head to toe.
 Chelsea ROYAL BLUE with white collar trim, crest, white swoosh, white "Three" sponsor, blue shorts,
 white socks with blue hoops. READ OFF: Enzo Fernández 5 (white undershirt sleeves, dark arm tattoos) ·
 Thiago Silva 6 with the armband · Havertz 29 · Loftus-Cheek 12 · Koulibaly 26 · James 24 · Mudryk 15 ·
 João Félix 11. *** KEPA IN CORAL/SALMON ORANGE, black-and-red palm gloves. ***
 Referee in RED with black shoulder panels. Night, floodlights, pristine grass. Yellow Wall packed.
 CROWD: "DETMOLD" and "Selm BVB City".
 BOARDS: Heineken SILVER · mastercard · UEFA CHAMPIONS LEAGUE · Priceless · WEIMANN.
 Intro bumper lists the UCL partners: Heineken, PlayStation 5, Just Eat Takeaway.com, Mastercard, OPPO,
 Lay's, FedEx, Turkish Airlines.
THE RUN — five touches, every one LEFT-FOOTED
 ORIGIN: *** IT STARTS FROM A CHELSEA CORNER. *** Chelsea swing one into the Dortmund six-yard box, a
  Dortmund defender heads it out to the right edge of the area, and GUERREIRO (13) hooks the second ball
  clear with a high looping LEFT-FOOTED clearance toward the centre.
 1 Adeyemi takes the DROPPING ball ON THE RUN with his LEFT foot (laces/instep), about 10 yards inside
   his OWN half near the left edge of the centre circle, pushing it into the centre-left corridor.
 2 and 3 left-footed controlling pushes, long rapid stride pattern.
 *** THE CONTEST: ENZO FERNÁNDEZ (5) IS THE ONLY CHELSEA OUTFIELD PLAYER BACK. He backpedals, jockeys,
   tries to angle him toward the left touchline. Adeyemi drives straight at him, then veers slightly
   outside him. Enzo extends his right arm and leans in and CANNOT LIVE WITH HIM — no contact on the
   ball, none on the man. A straight footrace, one v one, and it is over in about three seconds. ***
 4 KEPA rushes to the edge of the 18. Adeyemi knocks it past him with the OUTSIDE OF THE LEFT BOOT,
   wide around the slide. Kepa goes down on his stomach and knees and misses it entirely.
 5 he reaches it at the left corner of the SIX-YARD BOX and slots it with the SIDE/INSIDE OF THE LEFT
   FOOT into the lower-middle of the open goal, from about 5 yards at a tight diagonal.
 CELEBRATION: sprints past the goal line to the corner flag, arms out, and *** DOES A FULL BACKFLIP ON
  THE GRASS, landing on both feet. *** Mobbed by Bellingham, Haller, Emre Can and Özcan. Cut to Terzić
  jumping and punching the air.
BROADCAST GRAPHICS: NONE anywhere. Don't quote a number.
CAMERA: live high tactical 00:03–00:21 covering the corner through to the goal; then celebration cuts
 (backflip close-up, Terzić, group hug, the Yellow Wall, the players again); then FIVE slow-motion
 replays — the box battle and Guerreiro's clearance, the high broadcast angle of the whole run, a LOW
 PITCHSIDE TRACKING angle of Adeyemi and Enzo shoulder to shoulder, a LOW ANGLE BEHIND THE NET, and a
 reverse 18-yard-box angle on the final touch.
COMMENTARY (German) — two lines worth stealing:
 "...und jetzt Adeyemi! Eins-gegen-eins-Situation gegen Enzo Fernández. Tempotechnisch klarer Vorteil
  Adeyemi! *** Nimmt genau die Schnellstraße! *** Karim Adeyemi! Dreiundsechzigste!"
  (…takes the fast lane!)
 *** "Und ich kann euch sagen, wir haben hier die Bierdusche bekommen, aber hey, nehmen wir mit!"
  (And I can tell you, we just got a beer shower up here — but hey, we'll take it!) ***
 Analyst: "Das war ein Angriff zum Genießen. Das war absolute Weltklasse von Adeyemi."

════════════════════════════════════════════════════════════════════════
#6 GARETH BALE v MAICON — Spurs 3-1 Inter, White Hart Lane, 2 Nov 2010.
SOURCE: JOirPSqL28w (TNT Sports). 86s. REAL BROADCAST, HD 16:9, early-2010s look. BT Sport bug top right.
*** CRITICAL, AND IT CONFIRMS THE EARLIER WARNING: BALE DOES NOT SCORE IN THIS FOOTAGE. He is the
 creator throughout — two assists, one disallowed, one miss. The hat-trick is the OTHER match, the 4-3
 at the San Siro. Do not mix them on camera. ***
SCENE: Spurs WHITE with navy upper chest and cuffs, navy "Investec" chest text, Puma cat right chest,
 cockerel left chest. White shorts with navy trim, numbers on the LOWER LEFT THIGH. White socks with navy.
 Inter blue-and-black stripes, black collar, BLACK SLEEVES with blue cuffs, white "IRELLI" (Pirelli)
 across the chest, swoosh right chest, crest with gold star, *** SCUDETTO SHIELD PATCH centred on the
 upper chest. *** Black shorts with white numbers on the lower left leg, black socks with blue bands.
 Castellazzi in TEAL/MINT GREEN long sleeve with darker panels, matching shorts and socks.
 Referee in BRIGHT CRIMSON RED with black collar, black shorts, black socks with white trim.
 READ OFF THE KIT: *** BALE 3 *** (on the shorts at 00:32 and 01:17, and on the back at 01:23) ·
 *** MAICON 13 *** (clearly at 00:33–00:34) · CROUCH 15 · PAVLYUCHENKO 9 · PALACIOS 12 · JENAS 8 ·
 Inter's Obiora 40, and 25 and 26 intermittently.
 Bale's boots are BRIGHT YELLOW/VOLT with dark accents; Maicon's white/dark.
 Night, floodlights, damp tightly-cut grass, packed stadium.
 BOARDS: Ericsson · Sony Ericsson · Ford S-MAX · Sony make.believe 3D · Heineken · PlayStation 3 ·
 UniCredit · MasterCard · RESPECT · HTC.
 NO LIVE CLOCK OR SCORE during the action. At 01:21–01:25 a FULL TIME graphic reads:
 "FULL TIME · PAVLYUCHENKO 89' · CROUCH 61' · VAN DER VAART 18' | ETO'O 80' ·
  TOTTENHAM HOTSPUR FC 3 - 1 FC INTERNAZIONALE".
 A "REVERSE ANGLE" banner appears at 01:15.
FOUR SEPARATE RUNS AT MAICON: 1. 00:00–00:12 — Bale receives on the left touchline just inside Inter's half with Maicon jockeying.
    At 00:03 he touches it forward with the OUTSIDE OF THE LEFT FOOT, drops his shoulder and goes down
    the line. Maicon pivots to chase and is TWO FULL STRIDES behind. Bale crosses low and skidding with
    his LEFT foot from the byline; CROUCH slides in at the far post and puts his RIGHT-footed effort
    HIGH AND WIDE of the near post, then holds his head.
 2. 00:13–00:29 — at 00:15 Bale collects wide left near midfield. Maicon steps up. Bale knocks it TEN
    YARDS into space with his LEFT foot and goes. Maicon is caught flat-footed and Bale pulls FOUR TO
    FIVE METRES clear. Low LEFT-footed cross past the diving Castellazzi; CROUCH arrives unmarked at the
    back post and cushions a RIGHT-footed tap-in. 2-0.
 3. 00:30–00:41 — one-on-one wide left. Bale pauses, shifts his weight and pushes it OUTSIDE down the
    line with his LEFT foot, exploding past Maicon's right side. *** MAICON EXTENDS HIS LEFT ARM AND
    GRABS BALE'S RIGHT SHOULDER AND ARM TO PULL HIM BACK. Bale breaks through the contact and stays up. ***
    He reaches the byline and cuts it back for Crouch to slide in — but the assistant flags that THE BALL
    HAD FULLY CROSSED THE LINE. Goal disallowed. Crouch sits against the netting gesturing in disbelief.
 4. 00:42–01:20 — a counter from Spurs' own half, the ball into the left channel for Bale to chase. He
    sprints onto the bounce, CHECKS OVER HIS RIGHT SHOULDER to read the retreating defenders, and drives
    into the left of the box. Maicon and the centre-backs are far behind. At 00:51 he delivers a low
    curling LEFT-FOOTED cross to the centre; PAVLYUCHENKO (9) meets it on the run and finishes first
    time with his LEFT foot into the bottom left corner. 3-1.
MAICON'S BODY LANGUAGE: head dropped at full exertion and losing ground (00:06–00:08) · DECELERATES AND
 GIVES UP ON THE PLAY before the cross comes in (00:19–00:20) · grabs Bale's arm in desperation
 (00:33–00:34). He is NOT shown sitting on the turf, looking to the bench, or being substituted.
COMMENTARY — the line is already written for you:
 00:00 "Here's Bale. Gareth Bale at 21, sure to have such a very bright future, and he knows all about
  discomfiting Maicon. Oh, it's Crouch who gives it a lash! It was set up for him by Bale, and this was
  magnificent. *** Maicon must be fed up of Gareth Bale already. *** "
 00:22 "Gareth Bale trying to take charge again... *** Switches on the afterburners... *** Bale... and
  Crouch to make it two!"
 00:30 "Bale... and Maicon just couldn't get close to Gareth Bale, and it's in again! It's Crouch again,
  but it's not going to count."
 00:43 "...and Gareth Bale's away again! Flying forward, looked over his shoulder... Pavlyuchenko!
  There's a plunder! There to make certain of victory! Gareth Bale comes to the fore once again!"
CAMERA: sixteen cuts in 86 seconds, including a LOW TIGHT SIDELINE REPLAY at 00:32–00:34 that isolates
 Maicon grabbing his shoulder, and a LOW REVERSE SLOW MOTION at 01:14–01:20 from behind Bale looking in
 as he crosses for Pavlyuchenko.

SOFT FLAG, unchanged: Bale is also the reference video's #3 (v Barcelona, Bartra, the technical-area run).
Different match, different opponent, different competition — say "the other Bale one" and move on.

════════════════════════════════════════════════════════════════════════
CANNOT DETERMINE — ALL FIVE RUNS
 THE TOUCH TOTALS. The feet are reliable across repeated passes; the counts are not. Describe the
  foot, never the number.
 ALL SPEEDS AND DISTANCES. Not one of these five clips carries a speed or distance graphic. Son's
  Spurs TV cut has no scorebug of any kind, Puhiri's Indonesian feed has none, Van de Ven's has no
  graphics or watermark at all. Any figure quoted on camera would be invented.
 THE CLOCK AND SCORE on Son, Puhiri and Van de Ven — no scorebug on any of the three. Only Adeyemi
  carries a readable clock and scoreline.
 SHIRT NUMBERS on the Van de Ven clip — the camera is too distant to read any of them.
 The Copenhagen chest sponsor on the Van de Ven clip.
```

#### `deep/pace-abuser-son.md`
<!-- FILE: deep/pace-abuser-son.md · 5844 bytes · 89 lines · sha256 ab72807bd1940f4b5e14f744ca8a78494dc480a2693707c5e60bc1683003b7e8 -->
*New 21 Sep (~976 words) — Son fully described; eight visible touches RIGHT/CERTAIN; count unstable, say the foot.*
```markdown
# DEEP PASS — PACE ABUSER PART 2, #10 "SON HEUNG-MIN, THE BURNLEY SOLO GOAL"

SOURCE: C-CefuZ6h1k — Tottenham Hotspur official, "FIFA PUSKAS AWARD WINNER | HEUNG-MIN SON |
 ALL ANGLES OF SONNY'S SENSATIONAL BURNLEY SOLO STRIKE". Ten distinct camera angles.
AUTHENTIC: real broadcast, multi-camera professional coverage cut by Spurs TV. No game UI anywhere.

*** THE LINE THE PACK IS MISSING — THIS GOAL WON AN OFFICIAL FIFA AWARD ***
 It won the FIFA Puskas Award at The Best FIFA Football Awards 2020. The source video is Tottenham's
 own Puskas package. No other run in either Pace Abuser pack carries a trophy. That is the single
 strongest on-camera line available to this entry and it costs nothing to say.
 Fixture: Tottenham v Burnley, Tottenham Hotspur Stadium, 7 December 2019. Spurs won 5-0.

SCENE: Tottenham Hotspur Stadium, under floodlights, full house. The run travels the length of the pitch
 and finishes in front of the home end, which is what makes the celebration framing work.

READ OFF THE KIT: TOTTENHAM: white shirts with dark navy shoulder and collar trim, red AIA chest sponsor, navy shorts,
  white socks with navy turnovers. Numbers legible: 7 SON, 20 ALLI, 27 LUCAS MOURA, 10 KANE,
  5 VERTONGHEN.
 BURNLEY: claret shirts with sky-blue sleeves and collar, white LoveBet chest sponsor, white shorts,
  sky-blue socks with claret bands. Numbers legible: 2 LOWTON, 5 TARKOWSKI, 6 MEE (YELLOW CAPTAIN'S
  ARMBAND), 11 McNEIL, 12 BRADY, 13 HENDRICK, 23 PIETERS.
 GOALKEEPERS: Gazzaniga full turquoise. Pope dark charcoal with volt accents, grey shorts, volt socks.
 REFEREE: all black.

BOARDS: NIKE.COM/FOOTBALL and GEAR UP ON NIKE.COM/FOOTBALL · KUMHO TYRE · PRECISION · PHANTOM SERIES ·
 COME ON YOU SPURS.

SCOREBUG: NONE. No clock, no score, no competition badge anywhere in the package.

OVERLAY: must be masked
 00:21-00:35 a "CLICK TO SUBSCRIBE" panel bottom right with cartoon Kane, Lloris, Son and Alli.
 03:20-03:36 a YouTube end card. SPURS TV cockerel bug sits top right for the whole video.

ACTION: Son picks the ball up roughly 12-15 yards outside his OWN box, about 85 yards from the Burnley goal.
 He scans early — head turns left, then right — reads both passing lanes as covered, drops his head
 and drives straight through the middle. From there it is one unbroken carry.
 LOWTON (2) lunges with his right leg at midfield and is bypassed.
 BRADY (12) squeezes in off the left flank, cannot match the acceleration, and visibly gives up.
 MEE (6) and TARKOWSKI (5) both retreat and converge at the top of the D; Son goes between them
  before either commits to a tackle.
 POPE comes out to narrow it and drops low to his right; Son beats him along the ground.
 THE FINISH: right foot, inside/instep, side-footed low into the bottom-right corner from about
  13 yards.

THE TOUCH COUNT: READ THIS BEFORE YOU SCRIPT IT
 Three passes over this footage returned three different totals: 9, 10, and 11-12. The count is NOT
 stable and you should not quote a number on camera.
 What IS stable, and what a dedicated tie-breaker pass confirmed on the clearest angle: across the
 eight touches visible in the ultra-slow-motion head-on shot, EVERY ONE IS THE RIGHT FOOT, and every
 one was graded CERTAIN — the foot is clearly seen making contact on all eight. Zero left-foot
 contacts. The left leg plants and strides and never touches the ball.
 That tie-breaker also admitted its own limit: the head-on angle cuts in mid-run, so the first three
 or four touches deep in the Spurs half are not covered by it.
 SAY: "every touch with his right foot." DO NOT SAY: any specific number.

CELEBRATION: Son veers to the right corner flag in front of the home end, arms spread wide in an aeroplane, mouth
 open, then drops into a two-knee slide and comes up beaming. Alli (20) and Lucas Moura (27) are the
 closest trailing players and reach him first.

CAMERA: all ten angles, with the one that matters
 1. 00:00-00:20 main high gantry, the full run box to box.
 2. 00:20-00:37 low pitchside tracking from the right flank.
 3. 00:38-00:54 high tactical wide, shows the shape collapsing.
 4. 00:54-01:12 elevated behind the Burnley goal, Son head-on.
 5. 01:13-01:30 elevated reverse behind the Spurs goal, Son running away.
 6. 01:31-01:47 low reverse touchline, opposite side.
 7. 01:47-02:07 ground-level near-touchline profile.
 8. 02:07-02:25 elevated 18-yard box tracking.
 9. 02:26-02:39 low Steadicam from behind him.
 10. *** 02:40-03:19 ULTRA SLOW-MOTION FRONTAL, TIGHT. CUT ON THIS. *** It is the only angle that
  shows the feet clearly enough to carry the one-footed point, and it runs all the way through the
  split of Lowton and Brady, past Mee and Tarkowski, to the finish past Pope.

COMMENTARY: verbatim
 "Hill does so. Tarkowski under pressure from Vertonghen. Can't bring it down, and uh... It's general
 terror in the Burnley backline when Son breaks forward! Oh, wow, what a run! Heung-min Son from
 inside his own half has scored one of the best goals of his Spurs career!"

AUDIO: The crowd track is the reason to keep the natural sound up: nervous murmur under the Burnley set
 piece, a steady build as he crosses midfield, then a full eruption on the finish.

CANNOT DETERMINE
 The total number of touches — three passes disagree, see above. Do not quote one.
 Who exactly he looks at during the scan. One pass read it as Alli and Kane, another as Alli and
  Moura. The scan itself is confirmed by both; the targets are not.
 Top speed and sprint distance. There is NO speed or distance graphic anywhere in this cut, so any
  figure would be invented. The pack note already warns about this and it is correct.
 The Burnley player taking the deep free kick that starts the move. The commentator says "Hill",
  which does not match a Burnley squad number visible on screen.
```

#### `deep/penalties.md`
<!-- FILE: deep/penalties.md · 16251 bytes · 190 lines · sha256 88b72bafb28cd985c4badfb00104fcbaa8e32e47b5c1c8e1e3a32374db18f94a -->
*Zaza, Tah, Agüero, Eze. 22 Sep: Tah section relabelled SUB (replaced by Budimir); Eze section rewritten from 'wide left, settled' to DISPUTED with both readings and the Zaza knock-on.*
```markdown
# DEEP PASS — WORST PENALTY MISS WITH EVERY TECHNIQUE PART 2

════════════════════════════════════════════════════════════════════════
#5 ZAZA — STUTTER. SOURCE: 5_9OwlwAMMk at 00:14–00:23. Stade de Bordeaux, Euro 2016.
AUTHENTIC: real broadcast — authentic Euro 2016 signage, live English commentary, no game UI.
SCENE: Zaza in ROYAL BLUE short-sleeve Puma with white shoulder piping, white Puma right chest,
 FIGC crest left chest, white match-detail text on the centre chest (NOT LEGIBLE). *** NUMBER 7 read
 off the CENTRE CHEST and the LEFT LEG OF THE SHORTS, legible in close-up at 00:21–00:23. *** Royal blue
 shorts and socks with white. Light/white boots. SHAVED HEAD, FULL DARK BEARD.
 NEUER all black/dark grey long sleeve, dark shorts and socks, light/white gloves with coloured accents.
 Referee behind him to the left in BRIGHT YELLOW, black shorts and socks.
 Night, bright floodlights, dry. Packed stands behind the goal, Italian and German colours, flags,
 phones filming.
 BOARDS left to right: Continental (cut off as "ental") · UEFA EURO 2016 · Hisense · Continental with
 the rampant horse · McDonald's "i'm lovin' it" · Orange · Probios (behind the goal, partial) · KIA M…
 Upper tier banner "KOCER…" and Italian flags.
 NO SCOREBUG — the shootout score is NOT available from this clip.
THE RUN-UP — corrected and much more precise than before
 Starts about 4–5 METRES BEHIND THE TOP OF THE D, slightly to his left of the ball's line.
 Moves at 00:16. *** APPROXIMATELY 16–18 rapid choppy micro-steps (approximate — do not state as fact).
 Previously recorded as "about fourteen"; two passes now put it higher. *** Knees lifted MODERATELY high
 in a prancing trot. TORSO RIGID AND UPRIGHT, bouncing vertically, minimal forward lean. Arms bent at
 the elbows, flared slightly, pumping in time with the feet. The whole sequence covers only A COUPLE OF
 METRES. He DOES NOT STOP — he delays the acceleration, then takes 2–3 longer accelerating strides.
 PLANT FOOT: RIGHT, firmly to the side of the ball. NO SLIP.
 STRIKE: LEFT FOOT, instep/laces, hit hard. SEVERE BACKWARD LEAN, slightly to his right.
 The ball SKYROCKETS several metres over the bar on the right-centre of the frame, into the stands.
NEUER — better than "waves his arms": he stands centrally and *** REACHES BOTH ARMS UP AND TOUCHES THE
 CROSSBAR to make himself look bigger, *** then drops into a ready crouch as Zaza starts. Dives low to
 his right. Completely uninvolved.
CAMERA: 00:14–00:20 high wide tactical, normal speed, whole box in frame. 00:20–00:23 cut to a TIGHT
 TRACKING CLOSE-UP from the chest up as he turns away, head down, dejected. NO REPLAY — cuts to Müller.
COMMENTARY (English): 00:14 "Now it's Zaza." 00:20 "And he's blazed it! After an exaggerated run-up..."
 Crowd: whistling and nervous anticipation, then gasps, groans and German cheers.

════════════════════════════════════════════════════════════════════════
SUB (WAS #2 UNTIL 20 SEP — REPLACED BY BUDIMIR, YOUR CALL B) TAH — POWERSHOT. SOURCE: lq3o-vf5o40 (FIFA's own channel) at 00:00–00:04.
[!] This description is kept for the subs line. Budimir's #2 description is in penalty-2-budimir.md.
*** THE SLIP IS DEAD FOR A THIRD TIME. *** Verbatim: "There is no slip, no stumble, no scuff, and no
 loss of footing whatsoever." He approaches in a smooth continuous stride and plants his LEFT boot
 6–10 INCHES TO THE LEFT OF THE BALL, flat and anchored, zero sliding, zero scuffing. The miss is
 entirely mechanical: the torso leans sharply back as the RIGHT boot gets UNDERNEATH the ball.
[!] GAMEPLAY FLAG RAISED — AND I AM OVERRULING IT. See the separate note in the report. In short: the
 analysis admits there is NO visible game UI (no indicators, no stamina bars, no radar, no prompts) and
 then argues from fixture plausibility, which is the exact reasoning the system says is worthless. This
 is FIFA's own channel. Real German fan-club banners "BAD WALDSEE" and "ADLER BRETTEN" hang in the
 stands. Treat the flag as a false positive and keep the pick.
SCENE: Germany WHITE with a BLACK-RED-YELLOW GRADIENT over the shoulders and upper sleeves, black shorts
 with white vertical side stripes, white socks. *** NUMBER 4 in black on the back. *** Boots white with
 bright pink/red accents on the collar and sole.
 Keeper in FULL SOLID PURPLE/VIOLET, white palms with neon backhand accents, black boots.
 Referee outside the box to the left in an ORANGE/CORAL top, black shorts, black socks with white
 turnover bands. Bright clear daylight, sharp shadows. Pristine turf.
 Stands behind the goal full of white German shirts and flags; banners "BAD WALDSEE" with a tricolor
 and "ADLER BRETTEN". Venue banners read "BOSTON FOXBOROUGH".
 BOARDS: FIFA, then Coca-Cola repeated across the red LED run.
 SCOREBUG top right: German flag | GERMANY | PARAGUAY | Paraguay flag, with DOT MARKERS beneath for the
 shootout — so the numeric score CANNOT be read.
RUN-UP: about 4 strides (approximate), fluent, no pause, no stutter. Plant LEFT as above.
 STRIKE: RIGHT foot, instep/top of the boot, well under the centre of the ball. Marked backward lean
 through contact. Rises steeply over the middle-right of the frame, well above the bar, into the lower deck.
KEEPER: bounces centrally with arms out, dives low-to-mid to HIS right (Tah's left). Nowhere near it.
CAMERA: ONE continuous wide tactical from high behind the taker, 00:00–00:04. NO replay, no close-up —
 it cuts straight to José Canale at 00:05.
COMMENTARY (English): "And he's blazed it over the top!" — identical to the earlier watch.

════════════════════════════════════════════════════════════════════════
#3 AGÜERO — PANENKA. *** SOURCE UPGRADED: he7mZJDIEOQ (Sky Sport DE) at 01:23–01:43. ***
 This solves the note in the pack that said the only clip found was a small channel with music and no
 commentary. This one has FULL GERMAN COMMENTARY, an official PL scorebug, and FOUR camera angles.
AUTHENTIC: real broadcast — Sky Sport watermark, official PL scorebug, live German commentary, no game UI.
SCOREBUG: PL lion | *** MCI 1 - 0 CHE *** | clock running 47:30 +1' to 47:41 +1' — FIRST-HALF STOPPAGE
 TIME. At 01:37 a black "HUBLOT" sponsor tag appears under it. Top right: "Sky sport .de".
SCENE: Agüero in the City 2020/21 home kit — sky blue with a WHITE MOSAIC PATTERN, "ETIHAD AIRWAYS"
 across the chest, white shorts, sky blue socks with white tops. "AGÜERO" above 10 on the back.
 White/light boots with dark detailing.
 *** MENDY IN CORAL RED / BRIGHT ORANGE long sleeve, matching shorts and socks, white palms with dark
 backing, black boots. *** Referee (Anthony Taylor) all black.
 Overcast English daylight, diffused, no sharp shadows. Pristine striped grass.
 *** THE STANDS ARE VIRTUALLY EMPTY — COVID. *** Club banners across the lower seats:
 "CITYZENS GIVING FOR RECOVERY" · "WE'RE NOT REALLY HERE" · and on the fascia
 "COLIN BELL THE KING 1946–2021", which dates the match precisely.
 BOARDS: etisalat · NISSAN · NEXEN TIRE · MARATHONbet · ETIHAD AIRWAYS · PUMA.
 Upper banners: CITYZENS OFFICIAL MEMBERSHIP COMING SOON · EXCLUSIVE MEMBERSHIP PACK · WE ARE ONE TEAM.
RUN-UP: starts 3–4 yards behind the spot, nearly straight on, very slightly to his left.
 5–6 steps (right, left, right, left, plant left, strike right). Slow, measured, deliberate.
 *** HIS EYES STAY LOCKED ON MENDY THE WHOLE WAY. ***
 Plant LEFT, firmly to the left and slightly behind the ball.
 STRIKE: RIGHT foot, UNDERNEATH the ball with the instep/toe. Minimal pace. It floats up to
 WAIST-TO-CHEST height, drifting SLIGHTLY RIGHT OF CENTRE (Mendy's right).
*** MENDY — CORRECTED. He does NOT stay on his feet. *** He BEGINS to drop his knees and commit to his
 right as Agüero makes contact, then — seeing it float with almost no pace — ABORTS THE DIVE, SETTLES
 ONTO HIS RIGHT HIP AND KNEE, REACHES HIS RIGHT ARM STRAIGHT UP AND CATCHES IT CLEANLY ONE-HANDED IN
 HIS RIGHT HAND, then pulls it into his chest. A one-handed catch out of the air while sitting on his side.
AFTERMATH: Agüero drops his head, raises his right hand to rub his nose and mouth, looks down, walks
 away embarrassed. Mendy is up instantly, bouncing the ball, looking upfield for the counter. Chelsea
 turn away relieved; Sterling and Jesus pull up and drop their heads.
 *** 01:40: cut to GUARDIOLA in a GREY HOODIE with a circular red "OPEN ARMS" emblem on the back,
 crossing his arms and walking to the bench shaking his head. ***
CAMERA: 01:23–01:30 high tactical live. 01:30–01:33 tight tracking of Agüero wiping his face.
 01:34–01:39 LOW-ANGLE SLOW MOTION FROM INSIDE/BEHIND THE NET showing the one-handed catch. 01:40–01:43 Pep.
COMMENTARY (German), verbatim: "Und so gab's die Gelegenheit für Agüero in der Nachspielzeit der ersten
 Hälfte noch auf 2:0 zu stellen... *** Agüero... sehr frech... und Mendy direkt in die Arme! *** Das war
 schon sehr aufreizend, hätte der Held werden können... so wird das aber nichts... und dementsprechend
 natürlich Pep Guardiola zur Pause auch enttäuscht, nur in Anführungszeichen 1:0 in Führung."
 ("Agüero… very cheeky… and straight into Mendy's arms!")

════════════════════════════════════════════════════════════════════════
#1 EZE — SIDEFOOT, MISSED — DESTINATION DISPUTED. SOURCE: ygcv9fQheII (ARSENAL'S OWN OFFICIAL CHANNEL).

*** RESOLVED THREE WAYS, AND ONE OF THEM CHANGES THE ENTRY. ***

1. THE SOURCE IS OFFICIAL. ygcv9fQheII is published by the channel "Arsenal" — "VALIANT PERFORMANCE IN
   THE CHAMPIONS LEAGUE FINAL | HIGHLIGHTS | PSG 1 - 1 Arsenal (4-3 on pens)", 632k views. The gameplay
   flag on it was a false positive. Not blocked.

2. THE MATCH IS REAL, CONFIRMED IN TEXT. PSG 1-1 Arsenal, 30 May 2026, PSG retain the title on penalties.
   Havertz scored on 6 minutes, Dembélé equalised from the spot on 61. Reported by UEFA, ESPN, Al Jazeera,
   Yahoo and Olympics.com.

[!!] *** 3. THE BALL DID NOT HIT THE CROSSBAR. WHERE IT WENT INSTEAD IS DISPUTED. ***
   TWO separate vision passes both told me "underside of the crossbar, rebounded down and out". No source
   has him touching the frame, so that is dead. Beyond that the sources SPLIT [E20, 21 Sep]: Wikipedia's
   match record says he SHOT WIDE LEFT; a THIRD vision pass on Arsenal's own footage (run for the clip
   manifest) says OVER THE BAR, agreeing with the two earlier passes; TNT Sports' live commentary says
   only that he "missed his side's second effort". Both readings agree he went LEFT and missed the target.
   They disagree on bar or post. Law 2 ranks text above footage on what happened, but one text source
   against three passes is a CONFLICT to record, not a verdict. SAFE WORDING: "he missed." The man who
   put one OVER THE BAR for certain was GABRIEL, with Arsenal's fifth.

THE ACTUAL SHOOTOUT, from the match record — use this, not any vision read:
   1  Gonçalo Ramos (PSG)      SCORED
   2  Viktor Gyökeres (ARS)    SCORED      [a vision read called this Ødegaard — wrong]
   3  Désiré Doué (PSG)        SCORED
   4  EBERECHI EZE (ARS)       MISSED — record says wide left; footage says over the bar (DISPUTED)
   5  Nuno Mendes (PSG)        SAVED by DAVID RAYA
   6  Declan Rice (ARS)        SCORED
   7  Achraf Hakimi (PSG)      SCORED
   8  Gabriel Martinelli (ARS) SCORED
   9  Lucas Beraldo (PSG)      SCORED      [a vision read put Gonçalo Ramos in this slot — wrong]
   10 GABRIEL (ARS)            MISSED — OVER THE BAR
   PSG win 4-3.

*** WHY THE PICK SURVIVES, AND IS ACTUALLY BETTER FOR THIS ***
 You ruled the technique is a SIDE-FOOT and that stands — you watched it, and no source anywhere has a
 slow-motion replay of the contact, so the footage cannot overrule you.
 And the correction helps the variety IF the record is right. Zaza (#5) blazes it OVER THE BAR. If Eze went
 wide of the post the five end five different ways: never moves · caught standing still · rolled along the
 floor · wide of the post · into the crowd. [!] If Eze ALSO went over the bar, he and Zaza share an ending —
 the duplicate-mechanism problem that removing Tah was meant to fix. That is why the dispute is not
 cosmetic; it is flagged in the pack sheet and the manifest.
 ONE CHANGE TO THE SCRIPT: stop saying crossbar. He side-foots it and misses the target entirely.
 [!] And keep GABRIEL as a sub, not a pick — he goes over the bar for certain, which duplicates Zaza.

WHAT THE FOOTAGE SHOWS (Arsenal's official channel):
 Eze in the Arsenal 2024/25 home kit — red body, white sleeves, dark navy shoulder stripes, white shorts,
 red socks with dark/white banding. "EZE" arched above 10 on the back, "VISIT RWANDA" in white on the
 lower back. Light boots with volt/yellow accents. Long hair in braids/locs.
 Keeper in ALL NEON GREEN/LIME, light palms with neon accents, black boots. Referee light turquoise/cyan.
 Budapest. The end behind the goal is dominated by PSG supporters in white with banners and flags.
 BOARDS: bet365 · PEPSI · mastercard. Across the wider shootout coverage: FedEx · Qatar Airways ·
 Heineken · Crypto.com · UEFA CHAMPIONS LEAGUE · "Budapest 26 Final" · "Together" · "Recycle".
 SCOREBUG top left: "PENALTIES" / PSG [O][O] 3 4 5 | 2 / ARS [O][ ] 3 4 5 | 1. Arsenal shield top right.
 RUN-UP: central, angled slightly left, 4–5 yards back. 4–5 strides, smooth, NO STUTTER, no illegal stop.
 Plant LEFT, to the left of the ball. He gets it badly wrong and it misses the target to his left.
 KEEPER: bounces on the line with arms wide, dives low to HIS right, wrong way, no contact.
 AFTERMATH: Eze turns away immediately, brings his hands together in a brief clap/prayer gesture,
 touches the dreadlocks at the back of his head, stares at the turf.
 CAMERA: 01:22–01:26 live wide from elevated directly behind him looking through to goal. 01:26–01:27
 medium close-up as he turns and walks back. NO REPLAY — it cuts to Nuno Mendes at 01:28.
 COMMENTARY (English): "Eberechi Eze..." (with a slight vocal stumble) then "...misses!"

[!] *** A REAL SIMULATION FOUND WHILE CHECKING — AVOID THIS ONE. ***
 ZDF sportstudio's PSG–Arsenal video (PTs-3jmCQY8) IS a PlayStation simulation, and it has HARD evidence:
 at 00:20 the on-screen match graphic shows the PS5 LOGO DIRECTLY BENEATH THE SCORELINE —
 "PARIS 0 0 ARSENAL [PS5]". A real broadcaster publishing a simulated preview. It also gives the wrong
 outcomes (it has Arsenal's #10 wide RIGHT and Gabriel saved low, not over). This is what an actual
 game looks like when it turns up on a legitimate channel: a console logo in the graphics package.

════════════════════════════════════════════════════════════════════════
CANNOT DETERMINE — ALL FOUR DESCRIBED
 THE SHOOTOUT SCORE on Zaza and on Eze — neither clip carries a usable scorebug, so the running
  tally cannot be read off the footage and must not be stated.
 EZE'S CONTACT SURFACE. You ruled it a side-foot and that ruling stands, but note why it stands: no
  source offers a slow-motion of the contact, so the footage cannot overrule you either way. It is
  your call carried on your authority, not something the pictures confirm.
 THE ITALY MATCH-DETAIL TEXT on Zaza's centre chest is not legible.
 SLOT #4 IS NOT DESCRIBED HERE AT ALL, and that is correct rather than an omission — Pires and Henry
  duplicate Part 1's Pass entry and the slot is flagged for replacement. There is nothing to describe
  until you choose its replacement.
```

#### `deep/penalty-2-budimir.md`
<!-- FILE: deep/penalty-2-budimir.md · 6039 bytes · 89 lines · sha256 256c38ae4a531ebdb0aead0a9ad6ac4862727b314ad24140ba97f3779b08fb20 -->
*New 21 Sep (~1,002 words) after Joel's 'B — keep Budimir'. Say BUCKLES not SLIPS.*
```markdown
# DEEP PASS — WORST PENALTY MISS #2 "BUDIMIR, THE ONE THAT NEVER LEFT THE FLOOR"

SOURCE: 4EvIcyRuAXg — 38s, "Budimir Fail Penalti 97 minutes Osasuna X Valencia 2024", 121,545 views.
 Arena Sport 1 broadcast (Serbian feed).
AUTHENTIC: real live La Liga broadcast, no game UI. Osasuna 0-1 Valencia, El Sadar, 15 April 2024.

*** HE WON THE PENALTY HIMSELF AND THEN DID THIS. ***
 An inset replay at 00:21-00:24 shows the foul that won it — Guillamon clipping Budimir. He earned it,
 then took it, in the 97th minute, with his team a goal down. That is the setup and it costs one line.

SCOREBUG — read exactly
 Top left, red LaLiga mark: "OSA 0 - 1 VAL". Clock runs 96:43 (with +7 in a red box) through 97:37.
 Bottom right hashtag "#OsasunaValencia". Top right watermark "ARENA SPORT 1 / UZIVO".
OVERLAY — must be masked
 Rotating Serbian betting graphics bottom left: "BONUS DOBRODOSLICE", "SOCCER BET",
 "500 RSD BEZ DEPOZITA". They sit in the corner for most of the clip.

READ OFF THE KIT: OSASUNA: red body with NAVY SHOULDERS and white adidas sleeve stripes, "kosner" chest sponsor in
  white, navy shorts, red socks with navy trim. *** BUDIMIR IS 17 *** — name and number legible in
  white on red. Also legible: 22 J. MOJICA, 19 IBANEZ.
 VALENCIA: cream/off-white with black and gold detail, beige-khaki shorts and socks. Legible:
  6 HUGO G., 15 CENK, 18 PEPELU, 19 AMALLAH (wearing black gloves).
 GOALKEEPER: MAMARDASHVILI, all neon yellow-lime with black trim, 25 in black on the back.
 REFEREE: light blue shirt, dark shorts, only briefly in frame at the right edge.

BOARDS: Upper: kosner · San Miguel 0,0 · CaixaBank.
 Pitchside LED, animated and repeated: "MOTOGP SOLO EN DAZN" / "VIVE MOTOGP SOLO EN DAZN".
 Dugout fascia: BOGA · "AUPA OSASUNA!!!" · DN (Diario de Navarra).

THE RUN-UP: He stands four to five paces back, HANDS ON HIPS, staring straight at the keeper. Starts on his
 right foot at 00:09 and takes about three normal strides at moderate pace. Then, at the ball, he
 attempts an extreme stutter — a late feint to make Mamardashvili commit first.

THE PLANT — this is the entry, and it is not what people assume
 *** HIS STANDING LEG BUCKLES. *** Budimir is LEFT-footed, so the right leg is the plant. He sees the
 keeper start to move and tries to ABORT the swing mid-stride. The right leg collapses under the
 sudden deceleration — the knee sways outward, his weight drops, and his balance is gone. His upper
 body twists backwards and sideways and he stumbles FORWARD OVER THE BALL to avoid going down.
 [!] SAY "BUCKLES", NOT "SLIPS". The turf shows no divot and no tearing, and a dedicated pass could
 not separate an actual surface slip from a pure loss of balance caused by trying to stop the kick.
 The honest version is better anyway: he did it to himself.

THE STRIKE: As he is falling forward the LEFT foot flails through and catches the ball with the TOP/TOE of the
 boot — an accidental scuff, not a strike.
 *** THE BALL NEVER LEAVES THE GRASS. *** It rolls at walking pace towards the middle-right of the
 goal, arriving in the centre of the six-yard box no quicker than a slow backpass.

THE KEEPER: Mamardashvili has already shuffled and started diving low to HIS right. Because the ball is
 trickling almost straight down the middle he simply cushions his fall, reaches out and gathers it
 cleanly against his chest at 00:12. He does not have to save it. He has to wait for it.
 Then he is up instantly, fist pumping, pointing to the sky, mobbed by Pepelu and Guillamon.

THE REACTIONS — the best part of the clip
 BUDIMIR freezes, walks past the spot, shakes his head and PINCHES THE BRIDGE OF HIS NOSE.
 MOJICA (22) GRABS BOTH SIDES OF HIS HEAD instantly.
 *** ARRASATE ON THE TOUCHLINE, HANDS IN POCKETS, COMPLETELY MOTIONLESS — and then again later,
 SLUMPED ON THE BENCH WITH HIS CHIN ON HIS FIST IN SILENCE. *** That is your closing frame.
 The crowd groans once and then goes quiet. El Sadar murmuring is the only sound.

CAMERA: 00:00-00:01 tight close-up on Budimir's face before it.
 00:01-00:15 main elevated wide — the live kick, the gather, the celebration.
 00:16-00:18 medium on Budimir pinching his eyes.
 00:19-00:20 touchline profile of Arrasate.
 00:21-00:24 circular inset slow-motion of the FOUL that won the penalty.
 00:25-00:29 high rear-goal view across the whole box.
 *** 00:30-00:35 LOW PITCHSIDE FROM THE RIGHT OF THE SPOT. CUT ON THIS. *** The only angle that
  shows the stutter, the standing leg collapsing and the toe-scuff in one continuous movement.
 00:36-00:37 back to the dugout, Arrasate with his hand over his chin.

COMMENTARY — Serbian, and the line is already gold
 *** "Nije ni sutnuo!" — "He didn't even take a shot!" ***
 Full: "97. minut. Budimir ili Mamardasvili... Moze li Osasuna do izjednacenja u zavrsnici meca...
 Budimir... Ooooo! Sta je uradio Budimir?! Sta je uradio Ante Budimir?! Potpuna dekoncentracija
 centarfora Osasune! NIJE NI SUTNUO! Najgori trenutak u sezoni Budimira... On je ocekivao da ce
 Mamardasvili krenuti u stranu, zato je napravio tu malu zadrsku..."
 Translation: "97th minute. Budimir or Mamardashvili... can Osasuna find an equaliser at the death...
 Budimir... Ohhhh! What did Budimir do?! What on earth did Ante Budimir do?! Complete loss of
 concentration from Osasuna's centre forward! HE DIDN'T EVEN TAKE A SHOT! The worst moment of
 Budimir's season... He expected Mamardashvili to go one way, which is why he made that little
 hesitation..."

AUDIO: The commentator's turn from tension to disbelief carries the whole beat. One collective groan from
 the home end, then near silence. Keep the natural sound and do not add a sting.

CANNOT DETERMINE
 SLIP OR BUCKLE. The single genuinely open question, and the pass flagged it itself: no visible
  divot, no tearing turf, so a surface slip cannot be separated from a biomechanical collapse.
  Describe what the leg does, never why.
 The shirt numbers of the players waiting outside the D on the far left in the wide shot.
```

#### `deep/penalty-4-pires-henry.md`
<!-- FILE: deep/penalty-4-pires-henry.md · 6332 bytes · 91 lines · sha256 f6fab97d3cc6d5b4aa054af585a2a864f6b892cdbf9df60702a57d5d9eefdf5c -->
*New 21 Sep (~1,070 words) after Joel's 'Keep Pires & Henry'.*
```markdown
# DEEP PASS — WORST PENALTY MISS #4 "PIRES & HENRY, THE PASS THAT NEVER MOVED"

SOURCE: N4bQVTczcLQ — 34s, "Henry and Pires funny penalty fail vs Man City, and Henry mocks him
 celebrating the next game". Carries BOTH halves of the story.
AUTHENTIC: real broadcast archive from autumn 2005. BBC Match of the Day feed for the penalty,
 Sky Sports for the callback. No game UI.
PICTURE: standard definition 576i presented in 16:9. Moderate web re-compression — macroblocking on
 crowd movement, mild edge softening, motion blur on the pans. Deinterlaced rather than interlaced.

*** YOU ARE KEEPING THIS ONE KNOWING IT REPEATS PART 1. Same framing note as Stones. ***
 It IS your Part 1's Pass entry. Say it out loud in the first breath and it becomes a callback
 rather than a re-cut. The Pass technique is genuinely scarce — very few attempted pass-penalties
 fail — so the honest line is "there is only one of these, and here it is again."

*** THE CALLBACK IS THE REASON TO KEEP IT, AND PART 1 DIDN'T HAVE IT ***
 This source carries a SECOND moment eleven days later that turns a re-cut into a new video.
 See THE SECOND MOMENT below. If you shoot this, end on that, not on the miss.

THE FIXTURE: Arsenal 1-0 Manchester City, Highbury, 22 October 2005.
SCOREBUG: no broadcast bug. The STADIUM ELECTRONIC SCOREBOARD is visible in shot instead, reading
 "ARSENAL 1 - 0 MAN CITY" with the clock ticking 17:26 to 17:27 of the second half — so roughly the
 72nd–73rd minute. It also carries both full line-ups, which is a nice period texture.

READ OFF THE KIT: ARSENAL — and this is the detail worth a beat on camera: they are in the REDCURRANT COMMEMORATIVE
  KIT, the deep burgundy one worn only for Highbury's final season. Gold lettering and numbers,
  white O2 chest logo, white shorts, redcurrant socks with gold trim.
  *** PIRES IS 7. HENRY IS 14 AND WEARING THE YELLOW CAPTAIN'S ARMBAND on his left arm. ***
 MAN CITY: sky blue with navy trim, white Thomas Cook sponsor, navy shorts, sky blue socks.
  Numbers legible: 5 DISTIN · 22 DUNNE · 41 IRELAND · 38 SUN JIHAI.
 GOALKEEPER: DAVID JAMES, 1, bright green with black side and sleeve panels, black shorts and socks.
 REFEREE: GRAHAM POLL, all black with thin white chest piping.

BOARDS: JVC · Lucozade Sport · Lansen · BARCLAYS · O2 · "NIKE PRO: AN ATHLETE'S SECRET WEAPON".

THE RUN-UP: He starts about four paces back and slightly LEFT of the spot — a normal right-footed set-up, which
 is what sells the disguise. Three or four casual jogging steps. The tell, and it is only visible if
 you look for it: HIS TORSO STAYS UPRIGHT AND STIFF, he never leans into a drive, and HIS EYES STAY
 FIXED DOWN ON THE BALL rather than flicking up at James. He is setting up a tap, not a shot.

THE CONTACT — the whole video is this half-second
 RIGHT FOOT. He goes to roll it laterally and forward to his left for Henry to run onto.
 HIS STUDS SKIM ACROSS THE TOP OF THE BALL. The ball moves an inch or two — a twitch, not a pass.
 His foot passes clean over it and he pulls up mid-stride and freezes.
 [!] Note for the script: it is NOT a complete air-kick. There IS contact, on the upper surface,
 and the ball does move fractionally. "He never touched it" is the popular version and it is wrong.

WHAT HAPPENS NEXT: Henry is already charging in from the edge of the D expecting the ball and has to pull up, because
 it never rolls into his path. DISTIN (5) gets there first and hooks it left-footed into touch.
 GRAHAM POLL BLOWS AND GIVES AN INDIRECT FREE KICK TO MANCHESTER CITY — right arm straight up and
 held vertical, then a point towards City's end. The raised arm is a clean visual beat; hold on it.

THE REACTIONS: PIRES stops dead, arms slightly out, openly embarrassed.
 HENRY pulls up, hands open, turns away sheepish.
 DISTIN and DUNNE appeal to the referee while Distin hoofs it clear; DAVID JAMES just stands on his
 line looking baffled.
 CROWD: a hush, then a collective groan, then confused laughter and ironic jeers.
 *** THE TUNNEL INTERVIEW, same clip: "Tell us what happened." Henry: "What happened? I don't
 know..." — and he dissolves into laughter and DUCKS HIS HEAD COMPLETELY OUT OF FRAME. ***

THE SECOND MOMENT — Arsenal v Sparta Prague, Highbury, Champions League, 2 November 2005
 Eleven days later. Sky Sports feed, "SKY SPORTS X / LIVE" top right, lower-third strap reading
 "COMING UP — KING HENRY REIGNS / ARSENAL 1 - 0 SPARTA PRAGUE". Boards: PlayStation 2, Heineken,
 UEFA starball.
 Henry scores, runs to the corner flag, and PIRES COMES TO HIM. Henry stops in front of him and
 MIMES THE BOTCHED PENALTY — a hesitation step and an exaggerated flutter of his foot over an
 imaginary ball. Pires breaks into a grin and they embrace laughing, with Bergkamp (10), Lauren (12),
 Fàbregas (15) and Flamini (16) arriving around them.
 Voiceover over it: "...Thierry Henry had a spot of bother along with Robert Pires against
 Manchester City recently, but it's all right tonight and Arsenal lead 1-0."
 END THE ENTRY HERE. The miss is the setup; the mime is the punchline.

CAMERA: 00:00–00:11 elevated main wide — run-up, failure, clearance, referee signal.
 *** 00:12–00:18 HIGH REVERSE FROM BEHIND THE NORTH BANK GOAL looking straight down at Pires and
  James. CUT ON THIS for the contact — it is the only angle that shows the studs clipping the top of
  the ball without rolling it. ***
 00:19–00:21 eye-level close-up, the Highbury tunnel interview.
 00:22–00:34 low pitchside tracking, the Sparta Prague celebration.

COMMENTARY — verbatim, and it writes your caption for you
 "What's he done?!"
 "Well, he pretended to take it and then didn't seem to take it."
 "And the referee's given a free kick the other way! What an extraordinary incident!"

AUDIO: Poll's whistle cutting through, then a loud confused roar. Laughter under the tunnel
 interview. Upbeat TV bumper music under the Champions League callback.

CANNOT DETERMINE
 How far the ball actually moved — the displacement is under the sole of his boot and cannot be
  measured from any angle here. Say "barely moved", never a distance.
 Wenger's reaction and the Arsenal bench — no dugout cutaway exists in this cut. If you want
  Wenger's line on it, that is a separate source and it is a press quote, not footage.
```

#### `deep/signature-moves.md`
<!-- FILE: deep/signature-moves.md · 18571 bytes · 204 lines · sha256 f35e77a3849fbf1a42f9f453704a1fe5432049090e9e00870c38902268bac667 -->
*Vocabulary-normalised and colon-ified 21 Sep; carries AUTHENTIC: and CANNOT DETERMINE.*
```markdown
# DEEP PASS — TOP 10 SIGNATURE MOVES (2026 REDO)

════════════════════════════════════════════════════════════════════════
#1 THE CRUYFF TURN — Netherlands v Sweden, 1974. SOURCE: PBgLInYqhmo.
LIVE at 00:05–00:11, THE TURN ITSELF AT 00:08–00:10. SLOW-MOTION REPLAY at 00:17–00:26.
PICTURE: archive broadcast intercut with a modern colour interview. 16:9 (cropped/stretched from 4:3).
 Standard definition with heavy re-compression — soft edges, visible macroblocking, motion blur, colour
 bleeding on high-contrast edges. Saturated 1970s analog palette, heavy on orange and green. Analog
 videotape noise and edge fringing, NOT film grain. 25/30fps feel.
 Overlays: "@Netherlands1974" top left · "#WorldCup74" top right with a semi-transparent Sky Sports 1
 bug beneath · English subtitles on the lower third · end card at 00:29–00:33 reading "Holland74 /
 @Netherlands1974 / on twitter, facebook, tiktok, youtube, instagram and podcast".
SCENE: CRUYFF in BRIGHT ORANGE LONG SLEEVE with a black crew neck and black cuffs and *** TWO BLACK
 PARALLEL STRIPES DOWN EACH SLEEVE — the custom Puma design, because he refused the third stripe. ***
 Black shorts, orange socks with black fold-over cuffs, black boots. *** NUMBER 14 in black on the back.
 WHITE CAPTAIN'S ARMBAND on his LEFT upper arm. ***
 Swedish defender: royal blue short sleeve with white trim, white shorts with a thin blue side stripe,
 blue socks with white tops, black boots. *** NUMBER 2 on the FRONT LEFT HEM OF THE SHORTS. ***
 Sweden's keeper in green long sleeve, dark shorts and socks, visible 00:05–00:07.
 Referee in ALL BLACK with white collar and cuffs, black socks with white turnovers, at 00:04 and 00:11.
 Overcast daylight, soft even light. Natural grass, fair condition, worn in high-traffic areas.
 Large crowd packed behind WAIST-HEIGHT PITCHSIDE FENCING.
 BOARDS midfield: "...DAYS ERIFE" (cut off) · TEN OBEL · STENA LINE TO SWEDEN & DENMARK · C&A.
 BOARDS by the byline: NELLE SHAG · "GAZELLE… DE FIETS…" (rest obscured).
THE MOVE, broken all the way down
 LOCATION: attacking LEFT flank, 5–6 yards outside the Swedish 18-yard box, 10–12 yards up from the byline.
 RECEIVING: he chases a diagonal aerial ball from right midfield and controls it near the byline with the
  OUTSIDE/INSTEP OF HIS RIGHT BOOT, facing toward the corner flag, back partly angled to the defender.
 THE DEFENDER: #2 is tight to his back with his RIGHT FOREARM AND HAND ON CRUYFF'S BACK AND SHOULDER to
  stop him turning inward.
 THE FEINT: Cruyff plants his LEFT FOOT firmly ahead into the turf as his base, then lifts his RIGHT LEG
  in an exaggerated HIGH BACKLIFT, shaping to whip a cross or a pass back into the box.
 THE TURN: instead of striking it he brings the right foot OVER THE TOP of the ball and contacts it with
  the *** INSIDE OF THE RIGHT FOOT ***, dragging it backwards DIRECTLY BEHIND HIS PLANTED LEFT LEG, in
  one continuous motion, while pivoting the whole body ABOUT 180° COUNTER-CLOCKWISE to face the box, and
  pushing off the left foot to chase it.
 THE DEFENDER'S REACTION: #2 has committed everything forward to block the cross with his right leg
  extended. As the ball goes behind Cruyff he is completely wrong-footed, his torso twists awkwardly,
  his balance breaks, and he is left STRANDED TWO TO THREE PACES BEHIND.
 FOLLOW-UP: Cruyff takes a touch into the space near the edge of the 18 and drives a RIGHT-FOOTED CROSS
  into the middle. The footage cuts away before the ball lands.
CAMERA: 00:00–00:06 high wide master on the build-up and the diagonal pass. 00:07–00:11 closer pitch-level
 tracking for the live turn and cross. 00:11–00:16 modern interview close-up. 00:17–00:26 *** TIGHT
 GROUND-LEVEL SLOW MOTION showing the footwork, the ball passing behind the support leg, and the
 defender's balance breaking. *** 00:26–00:28 back to the interview. 00:29–00:33 title card.
AUDIO — and the closing line writes itself
 Narrator: "Against Sweden, Cruyff produced the move that defined his talents. It took a couple of
  seconds to lose the defender, but we've been talking about the Cruyff Turn ever since."
 *** CRUYFF HIMSELF, ON CAMERA: "I never did on a training or in free times tricks. I never did tricks.
  I saw something and I did it, and it just came out. There was an opponent there and I had to outplay
  him. That was the easiest way, so you just do it." ***
 Use that as the #1 payoff. It is the whole video in four sentences, in his own voice.
CANNOT DETERMINE: the defender's name — 1974 World Cup kits carried no names.

════════════════════════════════════════════════════════════════════════
#2 MESSI'S BODY FEINT — v Weligton (Málaga #14), Camp Nou. SOURCE: VzUWrhh7UQE at 03:22–03:56.
AUTHENTIC: real broadcast, SD upscaled to 16:9. BOTH SHOTS ARE SLOW-MOTION REPLAYS — there is no live-speed cut.
 No tactical arrows or analysis graphics. Channel bug bottom-left 03:22–03:40: a green-and-white rounded
 square with RUSSIAN TEXT "ФУТБОЛ" and a dark blue "LIVE" tab. Watermark "ArtfulMessi" in white cursive
 lower left throughout.
SCENE: Messi in the Barça 2008–09 home kit — HALF-AND-HALF VERTICAL SPLIT, royal blue on his right half,
 maroon/grana on his left, blue right sleeve, maroon left sleeve. Yellow "unicef" text with the UNICEF
 emblem to its left, crest left chest, yellow V-neck insert. Solid yellow 10 with a dark border on the
 back. Royal blue shorts with thin red side piping. Blue socks with maroon turnovers.
 *** SILVER/WHITE AND BLACK ADIDAS F50 BOOTS WITH BLUE TRIM. ***
 Weligton: light blue and white vertical stripes with short white sleeves, dark 14 on the back (name not
 legible), white shorts with a blue 14 on the lower left leg and blue lettering on the right leg, solid
 white socks, dark blue/black boots with white accents.
 Night, bright floodlights, dry pristine grass with visible mowing bands. Spectators immediately behind
 the barriers; STEWARDS IN HIGH-VIS RED/ORANGE JACKETS in the front row. Boards not legible.
THE MOVE — this is a body movement, so the body is the description
 LOCATION: inside the penalty area, right/inside-right channel, moving diagonally at the six-yard box.
 APPROACH: a controlled, DECELERATING jog with the ball rolling in front of his LEFT foot, sizing up
  Weligton as he steps across.
 THE DIP: *** he lets the ball roll on WITHOUT TOUCHING IT. *** He abruptly drops his LEFT SHOULDER and
  sinks his hips into a low crouch, shifting his entire torso weight to his left.
 THE PLANT: his LEFT FOOT plants firmly WIDE TO THE LEFT OF THE BALL, pointing diagonally forward-left
  toward the byline. His upper body leans heavily over that knee, feigning a burst down the outside.
 HEAD AND ARMS: head stays LOWERED, eyes on the ball and the defender's feet. RIGHT ARM extended wide
  right for balance; LEFT ARM held across his body to absorb contact.
 BALL CONTACT DURING THE FEINT: NONE. The ball keeps rolling on its original line while his entire body
  changes posture around it. That is the trick.
 THE DEFENDER: Weligton bites completely. He lunges forward with his RIGHT leg and twists his hips
  toward Messi's left to block the sprint he expects. His centre of gravity goes forward and
  overextends, and in panic he throws his LEFT ARM ACROSS MESSI'S TORSO to grab or impede him.
 THE EXIT: the instant Weligton's weight drops onto the extended leg, Messi unweights his left side,
  springs off the planted left foot, and jerks his hips and torso back upright to the right. With the
  OUTSIDE/INSTEP OF HIS LEFT FOOT he pushes the ball sharply to his RIGHT, cutting inside into the
  vacated channel. Weligton's outstretched hand SLIPS HARMLESSLY OFF HIS CHEST; his legs cross and
  tangle; he stumbles and cannot turn. Messi glides past his right side and advances in front of goal.
CAMERA: 03:22–03:36 low sideline tracking in slow motion, full bodies. 03:36–03:56 *** EXTREME CLOSE-UP
 ULTRA-SLOW-MOTION cropped from mid-chest down to the pitch — it isolates the hip drop, the boot plant,
 the hand slipping off the chest, and the outside-foot cut. This is the breakdown shot. ***
AUDIO: commentary, crowd and stadium sound ALL REMOVED. Instrumental hip-hop/trap beat over everything.
 You will have to carry this one entirely on your own voice.

════════════════════════════════════════════════════════════════════════
#3 INIESTA'S CROQUETA — v Manchester City. SOURCE: Zs3bmAJ4nq0 at 01:38–01:47.
AUTHENTIC: real broadcast, HD, high contrast, saturated greens, minor motion blur, 16:9. No game UI.
SCENE: Iniesta in garnet and navy vertical stripes with a YELLOW V-NECK BAND, yellow manufacturer logo
 right chest, badge left chest, "QATAR AIRWAYS" in white block capitals legible on the front in the
 close-up replay. *** NUMBER 8 in yellow, read off the back. *** Navy shorts, navy socks with garnet and
 yellow accents. *** BRIGHT ORANGE/CORAL BOOTS. ***
 City in ALL WHITE. First defender closing from his LEFT wears 4 (legible on the left leg of the shorts
 and the back). Second closing from his RIGHT wears 25 (back and left leg of shorts) with "ETIHAD
 AIRWAYS" partly legible. A trailing defender far right in the replay wears 42 on the shorts.
 Referee neon yellow with black collar, black shorts, black socks with white upper rings.
 Night, floodlights, dry. Smooth short grass in horizontal mowing bands. Full stadium, blurred by
 depth of field. BOARDS left to right: Heineken · UEFA CHAMPIONS LEAGUE with the starball · PS4 ·
 #ThePlayers. No scorebug. Watermarks: cursive "AJ" upper right throughout, and a faint "L10MS"
 lower left around 01:40–01:45.
THE MOVE: LOCATION: starts just beyond the centre circle in the opponent's half, carrying centrally at the box.
 RECEPTION: a rolling pass from his right, controlled forward in stride with his RIGHT foot.
 ORIENTATION: facing straight downfield, travelling at a slight angle into the left-centre channel.
 THE PRESSURE: #4 lunges in from his FRONT-LEFT with his right leg fully extended; #25 sprints in from
  his RIGHT. *** THE GAP BETWEEN THEM NARROWS TO ROUGHLY 1 TO 1.5 METRES. ***
 FIRST TOUCH: the INSIDE OF THE RIGHT FOOT pushes the ball laterally ACROSS HIS BODY, right to left,
  about 0.5–1 metre — just out of reach of #4's outstretched right leg.
 FOOTWORK: *** BOTH FEET MOMENTARILY LEAVE THE TURF in a synchronised shifting hop. ***
 SECOND TOUCH: as the LEFT foot lands, the INSIDE OF THE LEFT FOOT guides the ball straight forward into
  the corridor behind them. The entire two-touch move happens INSIDE A SINGLE RUNNING STRIDE.
 UPPER BODY: torso upright with a slight forward lean, arms out for balance — right arm back, left arm
  forward — shoulders turned slightly sideways to slip through the gap.
 THE EXIT: #4's lunge misses completely and leaves him off balance behind the play. #25 lunges late with
  his left leg and touches nothing. NEITHER defender touches the ball or Iniesta, and they do not collide
  with each other. He comes out RIGHT IN FRONT OF THE REFEREE, who turns to get out of the way, and
  carries on with an immediate controlling touch.
CAMERA: 01:38–01:43 live speed, elevated wide sideline, tracking him from the centre circle through the
 press and past the referee. 01:44–01:47 *** LOW PITCHSIDE REVERSE-ANGLE SLOW MOTION FROM BEHIND HIM —
 it shows the inside-right to inside-left contact, exactly how far the ball travels under his body, and
 #4's missed slide. ***
AUDIO: commentary and crowd ABSENT. Electronic/hip-hop music over the whole clip.

════════════════════════════════════════════════════════════════════════
#4 RONALDINHO'S ELÁSTICO — THE NUTMEG ON DUNGA. *** FOUND. *** SOURCE: LXqPEpeokCg at 02:20–02:35.
IT IS THE GRE-NAL DERBY: GRÊMIO v INTERNACIONAL.
PICTURE: authentic vintage broadcast, late-1990s SD analog, 4:3. Slightly saturated colours, noticeable
 compression, motion blur and artefacts consistent with an early-2000s web rip. No game UI.
SCENE: Ronaldinho in GRÊMIO — vertical stripes of SKY BLUE, BLACK and thin WHITE lines, short sleeves,
 chest sponsor and badge present but NOT LEGIBLE, black shorts, white socks with dark trim, black boots
 with white detail. His shirt number is NOT legible from these angles.
 *** DUNGA IN INTERNACIONAL: bright RED body with WHITE sleeves and accents, LARGE WHITE "8" clearly
 legible on the back, white shorts with red trim, red socks, black boots with white accents. ***
 A Grêmio teammate trails to the left; an Inter player and an assistant/ball boy are in the background.
 Referee not in frame. Bright sunny daylight, soft shadows. Well-kept grass with a crisp white penalty
 area line crossing right in front of the play, and A RED/BROWN RUNNING TRACK around the pitch.
 Packed bowl behind BLUE PERIMETER FENCING, crowd in red and blue.
 SIGNAGE on the track border: CHEVROLET with the bowtie · "TEMPERATURA" (partial). Fence banners not legible.
 Channel logo top right: "PLANETE" beneath an oval symbol. No scorebug.
THE MOVE: LOCATION: just outside the corner of the 18-yard box on the Grêmio right wing.
 APPROACH: he dribbles laterally toward the box line, body diagonal to goal, squaring Dunga up.
 *** ENTIRELY ONE FOOT — THE RIGHT. ***
 THE PUSH: he drops his hips and shifts his weight heavily right, and with the OUTSIDE EDGE/TOE of the
  right boot nudges the ball about 1 to 1.5 FEET OUTWARD to his right, baiting him.
 THE SNAP-BACK: *** WITHOUT THE RIGHT FOOT EVER TOUCHING THE GROUND, *** in one fluid unbroken motion,
  he whips the foot around the OUTSIDE of the ball and snaps it back sharply inside-left across his body
  with the INSIDE/INSTEP OF THE SAME RIGHT BOOT.
 THE NUTMEG: Dunga has committed and lunged outward at the first touch, and his legs open wide. The
  snap-back sends the ball CLEANLY BETWEEN HIS SPREAD LEGS.
 DUNGA: weight entirely on his left, right leg kicking out HIGH INTO THE AIR trying to intercept,
  left stranded and off balance IN MID-AIR as it goes through him.
 FOLLOW-THROUGH: Ronaldinho accelerates round Dunga's left side to collect it in space toward the box.
CAMERA: 02:20–02:25 live wide from an elevated grandstand tracking right with play. 02:26–02:28 a
 *** STAR-WIPE TRANSITION *** into slow motion from the same angle. 02:29–02:35 another star-wipe into a
 ZOOMED, CROPPED SLOW MOTION tight on the footwork and the ball going through the legs. Then static/noise
 into the end card. The star wipes are period-authentic and worth keeping in the edit.
AUDIO: commentary and crowd ABSENT. An upbeat electronic Brazilian samba track with rhythmic chants.

════════════════════════════════════════════════════════════════════════
#5 ROBBEN'S CUT-IN — *** BAYERN v JUVENTUS CONFIRMED. *** SOURCE: qDgAANEXQqg at 02:02–02:24.
AUTHENTIC: real broadcast, BT Sport bug top right, no game UI. Floodlit evening, UCL.
SCENE: Robben in all-red Bayern with darker red shoulder stripes, white adidas right chest, crest left
 chest, white Deutsche Telekom "·T···" on the chest, *** UCL STARBALL PATCH ON THE RIGHT SLEEVE AND A
 UEFA RESPECT PATCH ON THE LEFT. *** Red shorts with tonal dark red accents, red socks.
 *** "ROBBEN" with 10 in white on the back. ***
 Juventus in black-and-white vertical stripes, white shorts, white socks with black detail.
 READ OFF THE KIT: #33 Evra · #15 Barzagli · #19 Bonucci · #10 Pogba.
 BUFFON in dark charcoal-grey/black long sleeve with a white 1 on the back, dark shorts, white-backed gloves.
 Referee visible in bright neon yellow with black shorts. Pristine turf, full stadium.
 *** A BLACK-AND-WHITE FAN BANNER READING "VIKING" behind the Juventus goal. ***
 BOARDS: "PlayStation.FC UCL App On PS4" and "PlayStation" repeating.
 No scorebug, no timer — it is a clean highlight reel. A persistent RED FRAMING BORDER around the feed.
THE MOVE — the detail is in how it still works when everyone knows it is coming
 RECEPTION: a lateral pass on the right flank, about 10–12 yards infield from the right touchline and
  roughly 25 yards from the goal line.
 THE SHAPE AGAINST HIM: EVRA (#33) squares up at the right edge of the box trying to show him DOWN THE
  LINE. BARZAGLI (#15) shifts centrally inside the box as second cover. BONUCCI (#19) sits deeper.
  POGBA (#10) chases from behind. Four men accounted for, and it still does not matter.
 FIRST TOUCH: controls the rolling ball with the INSTEP OF HIS LEFT FOOT and drives into the right
  corner of the penalty area.
 THE CUT: *** NO STEPOVERS. *** Pure deceleration and a sharp change of direction — he cuts abruptly
  across Evra's path right to left using the INSIDE/INSTEP OF THE LEFT BOOT. Evra commits and lunges
  down to block the shooting lane; Barzagli slides in to intercept. The one touch takes it clear of both.
 THE STRIKE: cleanly with the INSIDE OF THE LEFT FOOT. Torso tilted forward and angled left, left arm
  raised for balance, left leg following through. A bending WAIST-HEIGHT CURL travelling right to left
  through the crowd of defenders. BUFFON reads it and dives FULL EXTENSION TO HIS RIGHT — the curl takes
  it just beyond his reach into the FAR CORNER, inside the side netting on the keeper's right.
CAMERA: 02:02–02:15 high wide live tactical, from central midfield out to the flank, through the cut,
 the shot and the celebration run. 02:16–02:22 mid-range elevated sideline replay on the angle of the
 cut past Evra and Barzagli and Buffon's dive. 02:23–02:24 *** LOW REVERSE ANGLE FROM BEHIND THE NET
 LOOKING OUT THROUGH THE NETTING as the ball curves past Buffon's glove. ***
AUDIO: NO COMMENTARY TRACK AT ALL. Stadium hum and whistles in the build-up, then a collective groan
 and hush from the home end with distant away cheers as it hits the net.
CANNOT DETERMINE: the minute and the score — no scorebug on the reel.
```

### 6.6 The reference audits — 10 files

#### `refaudit/GT-1mKJRDxU-THREE-PACKS.md`
<!-- FILE: refaudit/GT-1mKJRDxU-THREE-PACKS.md · 3189 bytes · 44 lines · sha256 2493407863159c80f969a03061d9404a86576d4a5266df403de8beddb4e1e805 -->
*Re-dated [RESOLVED 20 Sep 2026] for mispronounce after the three slots were filled (E18).*
```markdown
# REF AUDIT — forgot-club + mispronounce + blame-first | ref GT-1mKJRDxU
STATUS: *** FAIL — THE REFERENCE LINK IS WRONG FOR ALL OF THEM. ***

WHAT GT-1mKJRDxU ACTUALLY IS:
 "Players We Always Call By Their Full Name (PART 1)" — 64s, real broadcast footage, no game, no AI.
 #5 Nuno Mendes (PSG/Portugal) · #4 Luis Diaz (Liverpool/Colombia) · #3 Rafael Leao (Milan)
 #2 "Toni Krease" · #1 "Cristiano Rolando"
 Cold open: Karim Adeyemi, Dortmund yellow, "ADEYEMI 27", left-foot finish in the six-yard box.

 It has NOTHING to do with forgetting which club someone played for, with mispronunciation, or with
 who gets blamed first. It is about names you can only ever say in full.

WHY THIS MATTERS: in queued.csv that one link is pasted as the reference for SEVEN separate ideas —
 forgot-club, mispronounce, blame-first, "Players You Forgot Played Together", "Players We Always
 Confuse With Each Other", "Players Everyone Wanted at Their Club", "Players We All Copied in the
 Playground". One link cannot be the proof for seven different videos. It is the proof for none of them.
 THREE OF THOSE ARE IN THIS APPROVED BATCH AND ARE THEREFORE UNPROVEN:
   - forgot-club   (Pirlo at Inter / Robben at Chelsea / KDB at Chelsea / Henry at Juventus / Lampard at City)
   - mispronounce  (and see the second failure below)
   - blame-first   (Beckham 98 / Saka 2020 / Terry 2008 / Baggio 94 / Karius 2018)
 The picks inside them may still be good — they are sourced from your own comments — but none of the
 three has a viral video behind it showing the format travels. Right now they are guesses with a
 confident link attached.

SECOND FAILURE, SAME PACK SET — mispronounce WAS NOT FINISHED. [RESOLVED 20 Sep 2026]
 At audit its picks read: #5 Khvicha Kvaratskhelia · #4 "In rework" · #3 "In rework" ·
 #2 Thierry Henry · #1 "In rework" — 2/5, marked locked and approved with three empty slots.
 *** NOW FIXED: #4 César Azpilicueta · #3 Wojciech Szczęsny · #1 Mesut Özil, every pronunciation
 sourced rather than written from memory, and all five checked against Full Name Pt1 for collisions.
 The pack is complete. The LANE caveat below still stands — the reference proves the lane, not
 this title. ***

THE SYSTEM FIX:
 A reference link is only valid if the reference's TITLE PROMISE matches the pack's title promise.
 Before a pack is locked: open the reference, read its on-screen title card, and confirm it is asking
 the same question. Any link appearing against more than one pack is treated as unverified until each
 use is checked separately. Both checks are cheap and would have caught this at the source.

THE UPSIDE — THERE IS A FREE VIDEO SITTING IN HERE:
 "Players We Always Call By Their Full Name" is a strong idea you are not making, the video says
 PART 1 on its own title card, and no Part 2 exists. That is exactly the gap you normally hunt for.
 It also runs the misspelling bait hard: #2 is captioned "Toni Krease" and #1 is captioned
 "2. Cristiano Rolando" — wrong rank number AND wrong name, both deliberate, both engineered to drag
 corrections into the comments. That is a mechanic worth copying regardless of which pack you shoot.
```

#### `refaudit/another-nation.md`
<!-- FILE: refaudit/another-nation.md · 2630 bytes · 28 lines · sha256 c72a1333030a833ec5726a64b31b678486abe8ced501e3fb05b6f0758a55316f -->
*Written 18 Sep; unchanged.*
```markdown
# REF AUDIT — another-nation | ref 0zxkpSnyZJs "Could've played for another nation"
STATUS: PASS — one soft flag (Mbappé)
Footage: real broadcast, BUT every reveal ends on a DOCTORED COMPOSITE STILL (player photoshopped into the
other nation's kit with that flag laid over the chest). That is the format, not a defect — but note it.
Watermark: `yanedits`, centred near bottom throughout. NO VOICEOVER AT ALL — Brazilian phonk only. Length 29s.
Format: top bar of 5 player face icons + a "?"; each icon flips to the new flag as its entry lands.

REFERENCE CONTENTS (5 entries, no numbers shown — order left to right):
 1 KYLIAN MBAPPÉ (France royal blue, 10, captain's armband, Euro 2024, boards Alipay+) → CAMEROON. Goal v Germany, cuts inside, right-foot curler far top corner, arms-crossed celebration; composite in green Cameroon 10.
 2 LAMINE YAMAL (Spain red, 19, Euro 2024 match inscription) → MOROCCO. Knee slide at the corner flag; composite knee-sliding in a red Morocco Puma kit.
 3 BRAHIM DÍAZ (Morocco red Puma, gold 10, holding up "OUNAHI 8") → SPAIN. Pats the Morocco crest, points index finger up; composite in red Spain adidas.
 4 ERLING HAALAND (Norway, back print "BRAUT HAALAND 9", fixture text NOR–MDA 09.09.2024, blood on his lip) → ENGLAND. Composite in white England 9.
 5 RAYAN CHERKI (France navy pinstripe, 24) → ALGERIA. Palms to face, then arms spread; composite in white Algeria adidas 24.

CRITICAL: the reference states NO BASIS for a single one. No voiceover, no text, nothing explaining why
any of them was eligible. It is five flags and five photoshops. That is the whole video.

CROSS-CHECK vs my picks (Saka→NGA / Olise→ENG / Davies→LBR / Mbappé→ALG / Messi→ESP):
 - Saka, Olise, Davies, Messi: FRESH, none in the reference.
 - SOFT FLAG: MBAPPÉ is in both — and he is the reference's LEAD entry. But the reference sends him to
   CAMEROON (his father's side) and you send him to ALGERIA (his mother Fayza Lamari's Kabyle side).
   Both are true, which makes this a differentiator rather than a duplicate. Lean into it on camera:
   the common answer is Cameroon, and Algeria is the one people miss.
 - YOUR ACTUAL EDGE: you voice yours. The reference explains nothing. Every entry of yours should state
   the specific link out loud — Saka's parents from Ibadan, Olise born in Hammersmith and capped by
   England youth before choosing France, Davies born in a Ghanaian refugee camp to Liberian parents,
   Messi holding Spanish citizenship and turning down a Spain U20 call-up. That is a different video,
   not a better-looking copy of the same one.
```

#### `refaudit/lookalikes.md`
<!-- FILE: refaudit/lookalikes.md · 2360 bytes · 43 lines · sha256 a93e0524b5dc362182b3234b8aec69a7da6ed434f9d31500e47d6cf202ecf0ac -->
*Lookalikes was dropped on 20 Sep; audit kept as the record of why.*
```markdown
# REF AUDIT — lookalikes | ref rVw2TmDJf9o "Ranking Funniest Footballer Lookalikes"
STATUS: *** FAIL — HARD STOP. THIS PACK IS A 1:1 COPY OF THE REFERENCE. ***

WHAT THE REFERENCE ACTUALLY CONTAINS (exact on-screen rank captions):
 5. W VINI JR. LITE
 4. RAMEN YAMAL 😭🍜
 3. YAMINE AND PEPSI 💀
 2. HE'S HITTIN THAT 😂
 1. RONALDON'T 😮

WHAT MY PACK SAYS:
 #5 W VINI JR. LITE
 #4 RAMEN YAMAL 😭🍿
 #3 YAMINE AND PEPSI 💀
 #2 HE'S HITTIN THAT 😂
 #1 RONALDON'T 😮

Same five entries. Same five ranks. Same caption wording. Same emoji. This is not a remake —
it is a re-upload of another channel's video with nothing changed.

MAKE IT WORSE: the reference carries a burned-in channel watermark `zigzzzshorts` centred near the
bottom of EVERY clip. The underlying clips are other people's TikToks/Shorts, already compiled and
branded by a third party. Re-cutting this is a reused-content strike risk on a monetised channel,
not just a taste problem.

SECOND PROBLEM — TITLE PROMISE: ref #4 "Ramen Yamal" is NOT A PERSON. It is a white Nike boot with a
wooden kitchen paddle stood in the collar and cooked instant noodles draped over the top, on a
kitchen counter between two pink SMEG toasters, with a separate caricature meme inset at the bottom.
It is an object sculpture. Under a title that says "footballer lookalikes", a boot full of noodles
is the same failure as a striker under a goalkeeper title.

THE SYSTEM THIS BREAKS, AND THE RULE THAT STOPS IT REPEATING:
 A reference is a FORMAT source, never a CONTENT source. Rank labels are content. If a pick's wording
 can be found on screen in the reference, the pick was copied, not chosen. Every pack must now pass:
 "name the five, and point to where each one came from that is NOT the reference."

WHAT TO DO INSTEAD — this pack needs rebuilding from scratch:
 Keep the FORMAT (five lookalikes, punchy caption names, one-line narrator burn, 8s per entry).
 Bin all five picks. Source new ones the way the rest of the batch is sourced: comment requests on
 your own uploads, and first-party creator clips you can name. Candidates already in your subs list
 (Nicolas Jackson lookalike, a Haaland lookalike) are at least not from this video — but they still
 need a findable original, not a compilation re-rip.
 Do NOT reuse any clip that shows another channel's watermark.
```

#### `refaudit/oscar-2.md`
<!-- FILE: refaudit/oscar-2.md · 2718 bytes · 18 lines · sha256 34709416ae8d589a3e0ac2d7bd44030ecefb9aa983090bd80c47c3572a7cbbfd -->
*Written 18 Sep; unchanged.*
```markdown
# REF AUDIT — oscar-2 | ref uJEw4mhEYW8 "Top 5 Players Who Deserve The Oscar Award" (Part 1)
STATUS: PASS on footage — ONE OPEN HOLE on pick #2 (see bottom)
Footage: ALL REAL BROADCAST. No game UI. No AI/splicing.
Length 95s.

REFERENCE CONTENTS (5 numbered entries):
 #5 THIBAUT COURTOIS (Atlético, all-black GK kit, yellow gloves, green boots, Azerbaijan sponsor, LFP patch) — rolls the ball out, BALE (RM #11) pokes it off him from his blind side, Courtois throws himself down clutching his FACE with both gloves (no contact to face), Bale chips it in, referee (2013 badge) disallows. Godín #2 "KYOCERA" visible.
 #4 LUIS SUÁREZ (Barça #9, Qatar Airways) v PSG, 6-1 Remontada. MARQUINHOS (#5) raises right arm across his chest — Suárez throws both arms up, head snaps back, lands clutching his THROAT. Penalty given. Cut to Luis Enrique celebrating. Boards: SONY, Heineken, Lay's.
 #3 DANKO LAZOVIĆ — Videoton (white, #7, MOL front / STRABAG back / vilati shorts) v Budapest Honvéd. NARRATOR CALLS HIM CRISTIANO RONALDO — this is FALSE and it is Part 1's biggest factual error. Untouched sideways flop, then multiple full 360° rolls, gripping leg, screaming at ref. Boards: DUNA TAKARÉK, HAJRÁ HONVÉD!
 #2 DIOGO JOTA (Liverpool #20 "DIOGO J.") v NEWCASTLE (Dúbravka in teal) — NARRATOR SAYS "against Arsenal", also FALSE. Rounds keeper, keeper's left hand brushes his boot, Jota takes a FULL EXTRA STRIDE with an open net, hesitates ~1s, then goes down. Boards: Orion Innovation, Expedia.
 #1 ARJEN ROBBEN (NED #11) v MEXICO, 90+4', 2014 WC. Márquez (#4) sticks out right foot, marginal toe contact, Robben arches back, flings both arms up, lands chest-first. Proença gives it. Boards: #all in or nothing, Jupiler, Castrol EDGE, Budweiser.
 (Cold open before #5: Jagielka #6 half-volley v Liverpool, Mignolet #22 — not a ranked entry.)

CROSS-CHECK vs my Pt2 picks (Neymar roll / Micah Richards / Embolo / "a second Suárez dive" / Rivaldo):
 - Neymar, Micah Richards, Embolo, Rivaldo: all FRESH, none in the reference.
 - [!] PICK #2 IS UNDER-SPECIFIED. "A second Suárez dive" has no named match. Part 1 already used Suárez v PSG (Marquinhos, throat-clutch). If the edit grabs that clip you re-cut your own #4.
   FIX: name the moment now. Safest is Suárez v Chile 2016 Copa América (rolls holding his face off a shoulder) or the Suárez–Chiellini bite-aftermath where he clutches his TEETH — visually distinct from a throat-clutch and it reads instantly.
 - BONUS: Part 1's two factual errors (Lazović called "Ronaldo", Newcastle called "Arsenal") are a free Part 2 hook — "last time I called this man Ronaldo" — and they are already the top comment-bait on that video.
```

#### `refaudit/pace-abuser-2.md`
<!-- FILE: refaudit/pace-abuser-2.md · 1887 bytes · 15 lines · sha256 3d33cc693fa1f3124259a2724481b83d99bba2260b5044fb5b503eda813a34d7 -->
*Written 18 Sep; unchanged.*
```markdown
# REF AUDIT — pace-abuser-2 | ref jxz2A7GHTGM "Top 10 pace abuser moments in football history"
STATUS: PASS (no duplicate, no fabricated footage)
Footage: ALL REAL BROADCAST. No game UI, no AI/doctoring flagged.
Length 64s. Narrator VO present throughout; match commentary inaudible under music.

REFERENCE CONTENTS (5 numbered entries):
 #5 Adama Traoré (Fulham, red/black halves, "ADAMA" 11) vs Kyle Walker (Man City, #2). Through-ball, pulls 2 strides clear into box, right-foot shot from ~10y, EDERSON spreads and BLOCKS it. Boards: OKX, GROUP.
 #4 Kylian Mbappé (France navy, 10) vs Argentina, 2018 WC R16. Runs from own third, Marcos Rojo (#16) hands across chest from behind in box, PENALTY given. Boards: FIFA.com.
 #3 Gareth Bale (Real Madrid all-white, "BALE" 11) vs Barcelona, 2014 Copa del Rey final. Left-foot knock into space, MARC BARTRA (#15) bodies him off the pitch, Bale runs through the TECHNICAL AREA, re-enters, left-foot poke past Pinto (neon green). Boards: Allianz, SEAT.
 #2 Arjen Robben (NED dark blue, 11) vs Sergio Ramos (ESP white, 15), 2014 WC. Outsprints Ramos from centre circle, rounds Casillas (yellow) with left foot, left-foot finish into roof. Boards: Coca-Cola, SALVADOR.
 #1 Thierry Henry (France royal blue, 12) vs Paraguay, 1998 WC R16. Knocks past sliding defender, glides down right wing, right-foot clip at Chilavert (black 1). Boards: FUJIFILM, JVC TV & VIDEO, Canon, McDonald's, adidas.

CROSS-CHECK vs my Pt2 picks (Son / Terens Puhiri / Van de Ven / Adeyemi / Bale v Inter-Maicon):
 - NO rank-for-rank duplicates. All five Pt2 moments absent from the reference.
 - SOFT FLAG: Bale appears in BOTH (ref #3 = Bale v Barcelona/Bartra; my #6 = Bale v Inter/Maicon). Different match, different opponent, different competition — repeat PLAYER not repeat MOMENT. Acceptable; say "the other Bale one" in the script to pre-empt the comment.
```

#### `refaudit/primes-redo.md`
<!-- FILE: refaudit/primes-redo.md · 2247 bytes · 19 lines · sha256 4e054e1739b220a5194db8ff7942e8754ae1df7e882384b5863e5e6171cb8794 -->
*Written 18 Sep; unchanged.*
```markdown
# REF AUDIT — primes-redo | ref 9aYJ3lBf7HY "Top 5 Shortest Lived Primes in Football" (Part 1)
STATUS: PASS — zero overlap
Footage: ALL REAL BROADCAST/ARCHIVE. No game UI. No AI/doctoring. Vertical 9:16 pan-and-scan crop of SD/HD broadcast.
Length 101s.

REFERENCE CONTENTS (5 numbered entries):
 #5 MICHAEL OWEN — 1998 WC goal v Argentina (England white, #20 on front and shorts; Chamot #3 chasing; board "Gillette", FIFA TV watermark), Ballon d'Or portrait in Liverpool Reebok shirt, stretchered off for England, sliding into hoardings at Man Utd (PlayStation 3 / UniCredit / Heineken). Captions: 1998 · 18 · 22 · 25 · 4.
 #4 FERNANDO TORRES — Liverpool red (Carlsberg), then Chelsea blue "TORRES 9" rounding DE GEA at Old Trafford and putting it WIDE OF THE LEFT POST with his left foot, then face-down on the grass. Captions: £80 MILLION · 3.
 #3 ALEXANDRE PATO — AC Milan white/sash away "PATO 7" v Barcelona in the CL: picks it up near the centre circle, bursts through, nutmegs the onrushing keeper. Then hamstring/groin injuries, an Orlando City purple clip (ORLANDO HEALTH), head in hands crying. Captions: 17 · 21 · 2.
 #2 ADRIANO — Brazil yellow #7 at the 2006 WC (boards Continental, Yahoo!, T-Mobile, Philips) and Inter "ADRIANO 10" at the San Siro (Gattuso #8 tackling; boards RICAMBI ORIGINALI, TIM). Caption: TWO.
 #1 RONALDINHO — Ballon d'Or portrait, 2002 WC trophy, 2006 CL trophy with Puyol, the BERNABÉU STANDING OVATION (Barça 05/06 stripes, yellow 10, board SIEMENS, yellow Nike ball), then nightlife footage — white beret, sunglasses, gold chains, confetti. Captions: 2004 · 2006 · 28.

CROSS-CHECK vs my Redo picks (João Félix / Dele Alli / Arshavin / Michu / Van Basten):
 - ZERO overlap. All five are fresh. Nothing to fix.

TWO FACTUAL ERRORS IN THE REFERENCE — free Part 2 / redo ammunition:
 - "Chelsea paid 80 million pounds for him" — the fee was ~£50m (then a British record). The on-screen caption says £80 MILLION too, so it is baked into the video.
 - "He won two Ballon d'Ors" (Ronaldinho) — he won ONE (2005). He won FIFA World Player twice, which is what the writer confused it with.
 Correcting your own old video on camera is one of the strongest redo hooks you have.
```

#### `refaudit/psg-trio.md`
<!-- FILE: refaudit/psg-trio.md · 2413 bytes · 32 lines · sha256 f4ca44ada15d690f7a3f535069a5a281d13c3c7e9ce76cb8abf7384a70786dbb -->
*Written 18 Sep; unchanged.*
```markdown
# REF AUDIT — psg-trio | ref kymTJlWMyzk "What if PSG still had Neymar, Mbappé & Messi in 2026?"
STATUS: *** FAIL — WRONG GENRE. EA SPORTS FC SIMULATION. *** (watermark: ASP FC)

EVIDENCE IT IS A GAME: EA FC Team Management menu with rating badges (Mbappé 91, Messi 90, Vitinha 90,
 Neymar 85) and stamina bars; PlayStation prompts ([] Team Management, X Team Stats, O Back,
 [] Scores & Fixtures, triangle Top Scorers); EA FC UCL League Phase table; bracket screens; penalty-shootout
 summary with green ticks and red crosses. Length 57s. The ONLY real footage is the last four seconds.

WHAT IT SIMULATES: PSG 2nd in the league phase. R16 PSG 4-2 Sporting (agg 7-4). QF PSG 3-2 Man City
 (agg 4-3). SF Bayern 1-1 PSG (agg 2-3). Final Arsenal vs PSG at "Stadion Olympik", 1-1, PSG win 5-4
 on penalties — Eze misses for Arsenal; Messi, N. Mendes and Neymar all score. Top scorers: Neymar 8,
 Kane 8, Pavlidis 8, Haaland 8, Eze 7.
 It even edits Inter's name in the bracket to "Inter from Temu".

THE ONLY REAL FOOTAGE IN IT (0:53–0:57): Gabriel Martinelli's penalty for Arsenal v Sporting CP,
 Europa League R16, 16 March 2023, Emirates. Right-footed toward the bottom-right corner; Antonio Adán
 in green dives low to his right and blocks it two-handed. Boards: PEPSI, PlayStation 5. Used as a
 punchline, not as the subject.

WHY IT FAILS FOR THE PACK: my psg-trio picks are factual — six goals between them in one game, Messi's
 Ballon d'Or as a PSG player, no Champions League together, all three gone within two years, and the
 started-together count. Real research, real footage. The reference is a console sim with meme overlays.

*** AND THIS IS NOT THREE SEPARATE MISTAKES — IT IS ONE MISTAKE MADE THREE TIMES ***
 swap-nations (DZ2cXN-7GxE), ronaldo-stayed (zilVLvf10Sk) and psg-trio (kymTJlWMyzk) are ALL EA FC /
 FIFA simulations. The entire "What If" lane of this batch was sourced from a genre you do not make.
 Two of the three are by the same creator or circle — DZ2cXN-7GxE literally captions "Good job ASP",
 and ASP FC is the watermark on kymTJlWMyzk.
 What actually happened: searching a what-if premise on Shorts returns sim channels, because sim
 channels dominate that premise. The premise travels. The FORMAT that travels with it is gameplay.
 That is a real strategic finding, not just a bookkeeping error, and it needs a decision from you
 rather than a patch from me.
```

#### `refaudit/ronaldo-stayed.md`
<!-- FILE: refaudit/ronaldo-stayed.md · 2108 bytes · 28 lines · sha256 64cb3f230d944aac9bc3ecaebaa36d9059ed8b2c85d2f6c907740ce9fb6b35e1 -->
*Written 18 Sep; unchanged.*
```markdown
# REF AUDIT — ronaldo-stayed | ref zilVLvf10Sk "What if Ronaldo rejected Juventus in 2018?"
STATUS: *** FAIL — WRONG GENRE. FIFA 19 CAREER MODE SIMULATION. *** (watermark: M11M)

EVIDENCE IT IS A GAME (overwhelming, 82s and almost all of it is menus):
 FIFA 19 logo animation at 0:08. Career Mode contract-negotiation cutscene with Ronaldo in a suit.
 Team Management squad screen with rating cards — Ronaldo 94, Modrić 91, Kroos 90, Casemiro 88,
 Benzema 84. LaLiga Santander standings menu. UCL bracket UI. In-game HUD clock reading 92:39 → 92:51.
 Red overhead active-player triangle. Penalty aiming meter. Career Mode Squad Hub stats list at the end.
 Only ~3 seconds of the whole video is real: a training-ground clip of Ronaldo in a teal Madrid top.

WHAT IT SIMULATES: Ronaldo stays for 2018/19. Atlético knock Madrid out of the Copa del Rey.
 Madrid win LaLiga on 83 points (Barça 80) after a Bale cross and a Ronaldo header v Real Betis.
 They beat PSG, Spurs and Inter to reach a final against Barcelona. Messi comes off the bench at 94'
 and heads in. Ronaldo equalises at 105'. Penalties: Courtois saves Messi, Hamšík blasts the ninth
 miss wide. Ronaldo lifts a sixth CL and ends on 64 games, 38 goals, 17 assists.

TWO TELLS WORTH LOGGING:
 - THE SAVE FILE IS MODDED. Thiago Silva and Marek Hamšík are in Barcelona's squad. The "result" is
   therefore not even a clean sim of the premise.
 - SELF-CONTRADICTING SCORE ON SCREEN: the Copa del Rey summary shows "Aggregate: 1-4" in the top bar
   and "Aggregate: 3-1" in the subtext beneath the same fixture, at the same time. Same class of tell
   as the Eze fake-penalty clip.
 - Caption typo, probably deliberate: "NOW RONADLO".

WHY IT FAILS FOR THE PACK: my ronaldo-stayed picks are a real-history argument — he passes 500 Madrid
 goals, Benzema never becomes the main man, the three empty seasons look different, the Juventus
 experiment never happens, the all-time record is bigger. Real footage, stated case, hard closing line.
 The reference is a console save file. It is not evidence that the argument version travels.
```

#### `refaudit/swap-nations.md`
<!-- FILE: refaudit/swap-nations.md · 3176 bytes · 42 lines · sha256 7ca37da492cc4534a2411aef3f1a595e5479ebe2a74cc9a75f7e16e2e71d4608 -->
*Written 18 Sep; unchanged.*
```markdown
# REF AUDIT — swap-nations | ref DZ2cXN-7GxE "Ronaldo & Messi Swapped Nationalities World Cup!"
STATUS: *** FAIL — WRONG GENRE. The reference is an EA SPORTS FC GAMEPLAY SIMULATION. ***

WHAT THE REFERENCE ACTUALLY IS (56s):
 A creator loads EA Sports FC, puts Ronaldo in Argentina's squad and Messi in Portugal's, and sims a
 World Cup, narrating the bracket. The evidence is unambiguous and meets the visible-game-UI standard:
 Team Management screens with overall ratings, the PlayStation prompt "triangle Team Management", EA FC group
 tables with Played/Won/Draw/Lost/GF/GA/GD/Pts columns, "triangle See all groups" and "X Advance", bracket
 screens, 90:00 and 120:00 end-match reports, and L1/R1/L2/R2/triangle/X/O/[] controller icons.
 Squad ratings on screen: Messi 90, Vitinha 90, Fernandes 88, Neves 88, Mendes 88, Dias 87 (Portugal);
 Martinez 88, Ronaldo 85, Fernández 85, Mac Allister 85 (Argentina).
 The bracket: POR 2-1 CRO, ARG 2-1 ESP, POR 4-1 ALG, ARG 3-0 AUS, POR 4-2 USA, ARG 2-1 COD,
 Senegal 2-3 Argentina (120:00, Giuliano 117'), France 2-0 Portugal, final France 2-1 Argentina
 (120:00, Mbappé 97').
 It also contains a DEEPFAKE — Mbappé's face swapped onto Admiral General Aladeen in The Dictator —
 plus fabricated composites (Ronaldo in an Argentina 7 shirt, Messi in a Portugal 10 shirt, a
 "REPUBLIC OF MBAPPÉ" badge) and a Polymarket betting-odds overlay.
 And it ADMITS RIGGING ITSELF, on camera: "I totally wasn't forced to simulate until Mbappe scores and wins."

WHY THIS IS A FAIL:
 My swap-nations pack is a real-history counterfactual argument — Messi lifts the Euros in 2016,
 Ronaldo plays in the 2022 final, Ronaldo finally wins a Copa América, Messi's drought gets worse,
 the GOAT argument ends on the day of the swap. Real footage, a stated case, a hard closing line.
 That is a completely different video from a console sim. The reference proves that a GAMEPLAY SIM of
 this premise travels. It proves nothing about whether an argument version travels. You do not make
 gameplay sims and you are not going to start — so this reference is not evidence for anything you
 would actually shoot.

 There is no duplicate to fix here. The picks are fine. The PROOF is missing.

THE SYSTEM FIX (this is the same root cause as the GT-1mKJRDxU failure, one level up):
 Matching the TOPIC is not matching the FORMAT. A reference is only valid if BOTH match — same
 question AND same kind of video. Add a genre field to every reference when it is logged:
 real-footage ranking · single-story narrative · gameplay sim · talking head · meme compilation.
 A reference whose genre is not one you produce gets rejected at logging, before a pack is ever built
 on it. Three of this batch's failures (lookalikes, transfers-almost, swap-nations) are all this
 same mistake wearing different clothes.

WHAT SWAP-NATIONS NEEDS INSTEAD:
 A real-footage counterfactual that actually travelled. Your own "What If" lane is the place to look
 first, and the honest option is to shoot it on the strength of the premise alone and label it as an
 experiment — but do that knowingly, not because a link in the sheet made it look proven.
```

#### `refaudit/transfers-almost.md`
<!-- FILE: refaudit/transfers-almost.md · 3268 bytes · 42 lines · sha256 faccee38d523651495a3c38bd17ff91a25e7f15a75c0e58f25e4039815ddc1c9 -->
*Written 18 Sep; unchanged.*
```markdown
# REF AUDIT — transfers-almost | ref 0_yDGO1Jgt0 "CRAZIEST transfers that almost HAPPENED!"
STATUS: *** FAIL — FORMAT MISMATCH. The reference is NOT a top-5. ***
Footage: all real — broadcast, press conferences, archive stills, real news screenshots, meme cutaways.
NO photoshopped kit mock-ups anywhere (Kroos is never put in a United shirt). Length 69s.

WHAT THE REFERENCE ACTUALLY IS:
 ONE transfer. One story. Sixty-nine seconds on Toni Kroos to Manchester United, and nothing else.
 There are no rank numbers, no #5-to-#1, no list. The title is plural; the video is singular.

THE STORY IT TELLS (so you can see the shape):
 Setup — Moyes takes over from Ferguson in 2013 and needs a statement signing. Misses Bale, misses
 Fàbregas, ends deadline day with Fellaini. [Steve Harvey Family Feud reaction cut]
 The move — Kroos's Bayern contract talks have stalled; Bayern don't want to lose him free. January 2014
 Moyes FLIES TO MUNICH AND SITS ON KROOS'S COUCH IN HIS OWN HOME. Kroos agrees, ~£20m, for end of season.
 [headline still: "Toni Kroos 'agreed to join Manchester United' after David Moyes persuaded him and his family"]
 The twist — April 2014, United sack Moyes 10 months into a 6-year deal. [BBC Sport screenshot:
 "David Moyes sacked as Manchester United manager after less than a year in charge"] [Rocky Lockridge crying meme]
 Van Gaal comes in. Kroos had already played under Van Gaal at Bayern and they never clicked. He waits.
 The call from Old Trafford never comes.
 The payoff — Ancelotti rings during the World Cup. €25m to Real Madrid. Ten years, 23 trophies,
 five Champions Leagues. Ends on Kroos posed with all five trophies.

WHY THIS IS A FAIL FOR THE PACK AS BUILT:
 My transfers-almost pack is five picks (Ronaldinho→Man Utd, Lewandowski→Blackburn, Neymar→Real,
 Fekir→Liverpool, De Gea→Real). None of them is Kroos, so there is no duplicate — the problem is
 structural. Five picks in ~60s is 12 seconds each. Twelve seconds cannot carry "he sat on his couch."
 The reference works BECAUSE it spends the whole runtime on one story with a reversal in it. Chopping
 that into five leaves five facts and no story, which is the weakest version of this idea.
 De Gea → Real Madrid is the clearest case: the fax deadline is a 60-second story and a dead 12-second fact.

THE TWO WAYS TO RUN IT — pick one:
 A. MATCH THE REFERENCE. One transfer per video, ~70s, full arc. De Gea/the fax first — it is the
    strongest single story in the five and the most famous. The other four become their own uploads.
    This turns one pack into a five-video series with no extra research.
 B. KEEP THE TOP-5. Then it is your format, not the reference's, and the reference stops being the
    model — you need a different proof that a five-pick version of this travels.
 My read is A. The reference is a 69-second single-story video and that is the thing that worked.

EDIT GRAMMAR WORTH STEALING (this part is format, so it is fair game):
 Real news-article screenshots used as evidence beats, and meme reaction cutaways (Family Feud,
 the crying man) punctuating the bad news. That rhythm — fact, fact, reaction meme — is what keeps
 a talking-head transfer story from feeling like a Wikipedia read-out.
```

### 6.7 State files

#### `queued.csv`
<!-- FILE: queued.csv · 13313 bytes · 135 lines · sha256 75fa6781e0361b8197c0c84d710a86084a0db7619bd0ada0ef1938fd1d21b21e -->
*Master queue date,title,link,status — the recovery file after a context loss. Lookalikes row marked 'Dropped 2026-09-20'. (On disk this file has CRLF line endings; it is embedded LF-normalised and the hash is of the LF form. Both read identically through the csv module.)*
```csv
date,title,link,status
2026-08-15,Top 5 Juninho's Free Kicks,https://www.youtube.com/watch?v=VDxgYl6ZQiE,Queued
2026-08-15,Top 10 Legendary Defenders in Football,https://www.youtube.com/watch?v=3qtbHYUEe44,Queued
2026-08-15,Top 5 Strangest Moments in Football History,https://www.youtube.com/shorts/J7QrVtE3F4o,Queued
2026-08-15,Top 5 Liverpool vs Man City: Combined XI,https://www.youtube.com/watch?v=4DmWcqFyYlM,Queued
2026-08-15,Top 5 Legendary Sprint Speeds in Football,https://www.youtube.com/watch?v=zMxZovxcx-o,Queued
2026-08-15,Top 5 Most Insanely Satisfying Goals,https://www.youtube.com/shorts/nuPFtVlJ0Xg,Queued
2026-08-15,Top 5 Ronaldo's World Cup Failures,https://www.youtube.com/shorts/Zpmn77KW694,Queued
2026-08-15,Top 5 Mistakes That Cost Trophies,https://www.youtube.com/shorts/3pw0Y8EgjqA,Queued
2026-08-15,Top 5 Most Hated Footballers Ever,https://www.youtube.com/shorts/0vUkiMy8tHE,Queued
2026-08-15,Top 5 Times Legends Still Got It,https://www.youtube.com/shorts/44-csFxt9zU,Queued
2026-08-18,Top 5 Ronaldo Emotional Goals,https://www.youtube.com/shorts/yvEpKKx-_EM,Queued
2026-08-18,Top 5 Ronaldo 'Why Would You Shoot That' Moments,https://www.youtube.com/shorts/3L5wOsUdxKM,Queued
2026-08-18,Top 5 Ronaldo Disrespectful Goals,https://www.youtube.com/shorts/G5Xeqetx-_8,Queued
2026-08-18,Top 5 Times Messi Humiliated Defenders,https://www.youtube.com/shorts/4pReQafjza8,Queued
2026-08-18,10 Weird Facts About Cristiano Ronaldo,https://www.youtube.com/shorts/l94zC4w-Dzo,Queued
2026-08-18,Top 5 Ronaldo Power Shots That Had No Mercy,https://www.youtube.com/shorts/9hstuCAa6YI,Queued
2026-08-18,Top 5 Messi 'Big Brain' Moments,https://www.youtube.com/shorts/fCYztc7zN2k,Queued
2026-08-18,Top 5 Worst World Cup Winners,https://www.youtube.com/shorts/NL0GyJCeEQY,Queued
2026-08-18,Top 5 Worst Golden Boy Winners,https://www.youtube.com/shorts/0g3cftFz08k,Queued
2026-08-18,King of Every League,https://www.youtube.com/shorts/sCXb8WPrxys,Queued
2026-08-18,Saddest World Cup Endings,https://www.youtube.com/shorts/5NcJRjg9Leo,Queued
2026-08-18,Ronaldo's Last 10 Portugal Goals,https://www.youtube.com/shorts/M9RjhRjoVhw,Queued
2026-08-18,The Biggest Rivalry in Every League,https://www.youtube.com/shorts/yFCfHKG0xbE,Queued
2026-08-18,Top 5 Worst Premier League Winners,https://www.youtube.com/shorts/0g3cftFz08k,Queued
2026-08-18,Top 5 Goalkeeper Mistakes That Hurt to Watch,https://www.youtube.com/shorts/G-owB65Nhrk,Queued
2026-08-18,Top 5 Footballers' Sons Who Will Be Superstars,https://www.youtube.com/shorts/0QlrjoSI00U,Queued
2026-08-18,Ronaldo's Last 10 Goals for Real Madrid,https://www.youtube.com/shorts/Vt5GGm5hKmo,Queued
2026-08-18,Top 5 Fastest Goals in Football History,https://www.youtube.com/shorts/W0k9PZyi6JI,Queued
2026-08-18,Strangest Retirements in Football History,https://www.youtube.com/shorts/MtvQKcbQmCI,Queued
2026-08-18,Top 5 Times the Ball Got Destroyed (Part 2),https://www.youtube.com/shorts/F7uCJP-n7ek,Queued
2026-08-18,Players Who Retired and Switched Sports,https://www.youtube.com/shorts/yQ8CQUNOVTs,Queued
2026-08-18,Celebrations for Sick Kids,https://www.youtube.com/shorts/ezU6DY5Jfj8,Queued
2026-08-18,Top 5 Big Brain Striker Moments,https://www.youtube.com/shorts/fCYztc7zN2k,Queued
2026-08-18,Top 5 Big Brain Defender Moments,https://www.youtube.com/shorts/fCYztc7zN2k,Queued
2026-08-18,Top 5 Ronaldo Unselfish Moments,https://www.youtube.com/shorts/yeMVCqLkCJs,Queued
2026-08-18,Top 5 Most Unselfish Moments in Football,https://www.youtube.com/shorts/fx_slu-A8Vw,Queued
2026-08-18,Your Birth Month Decides Your GOAT,https://www.youtube.com/shorts/x7zccw2tOm0,Queued
2026-08-18,Top 5 Most Insane Pace-Abuser Goals,https://www.youtube.com/shorts/9OWUC9v4qoQ,Queued
2026-08-18,Top 5 Legendary Backheel Goals,https://www.youtube.com/shorts/yftne0_QyHc,Queued
2026-08-18,Funniest Tunnel Moments in Football,https://www.youtube.com/shorts/ofwb90GC3c0,Queued
2026-08-18,Top 5 Longest Primes in Football History,https://www.youtube.com/shorts/9aYJ3lBf7HY,Queued
2026-08-24,Ranking the Premier League Big 6,https://www.youtube.com/shorts/2YQ3Xl2cpw4,Queued
2026-08-24,The Strangest Curses in Football History,https://www.youtube.com/shorts/69HDR9dnHcY,Queued
2026-08-24,Top 5 Weirdest Rules in Football,https://www.youtube.com/shorts/StGHLfNtHJM,Queued
2026-08-24,Craziest Pitch Invasions Ever,https://www.youtube.com/shorts/oUCa0c_bBPE,Queued
2026-08-24,Top 5 Rarest Goalkeeper Moments,https://www.youtube.com/shorts/M29VTwBnsbk,Queued
2026-08-24,Funniest Manager Moments,https://www.youtube.com/shorts/CV1jWhlWfdE,Queued
2026-08-24,Top 10 Goals That Never Won the Puskas — Part 2,https://www.youtube.com/shorts/xsdwvZyU9kw,Queued
2026-08-24,Top 5 Big Brain Substitutions,https://www.youtube.com/shorts/fCYztc7zN2k,Queued
2026-08-24,Top 5 'Aura' Saves in Football,https://www.youtube.com/shorts/bSTDnWSVLAE,Queued
2026-08-24,King of Every Tournament,https://www.youtube.com/shorts/sCXb8WPrxys,Queued
2026-08-24,Top 5 Weirdest Football Traditions,https://www.youtube.com/shorts/StGHLfNtHJM,Queued
2026-08-24,Top 5 Ronaldo Big Brain Moments,https://www.youtube.com/shorts/fCYztc7zN2k,Queued
2026-08-24,The Best Goalkeeper of Every Decade,https://www.youtube.com/shorts/sCXb8WPrxys,Queued
2026-08-24,When Strikers Get Bored,https://www.youtube.com/shorts/uNYUKocZWdQ,Queued
2026-08-24,The Highest-Scoring Goalkeeper in History,https://www.youtube.com/shorts/xy_-0uDDE_g,Queued
2026-08-25,Top Shameless Handball Goals,https://www.youtube.com/shorts/k-8RV4ESJZQ,Queued
2026-08-25,Top Goals That Look Like AI,https://www.youtube.com/shorts/59HUVRASUJk,Queued
2026-08-25,Top Shaolin Soccer Goals,https://www.youtube.com/shorts/WEX-vvhcyf0,Queued
2026-08-25,Top Hilarious Air Kicks,https://www.youtube.com/shorts/1APRYPV9Daw,Queued
2026-08-25,Top Inhuman Plays in Football,https://www.youtube.com/shorts/Ef9UzP0NywY,Queued
2026-08-25,When Goalkeepers Sacrifice Themselves,https://www.youtube.com/shorts/68j4k93NOv4,Queued
2026-08-25,Top Defender Mistakes That Hurt to Watch,https://www.youtube.com/shorts/G-owB65Nhrk,Queued
2026-08-25,When Substitutes Get Bored,https://www.youtube.com/shorts/uNYUKocZWdQ,Queued
2026-08-25,When Mascots Get Bored,https://www.youtube.com/shorts/uNYUKocZWdQ,Queued
2026-08-25,Top Inhuman Recovery Runs,https://www.youtube.com/shorts/Ef9UzP0NywY,Queued
2026-09-01,Top 5 “Aura Goals” in Football Part 2,https://www.youtube.com/shorts/bSTDnWSVLAE,Queued
2026-09-01,Top 10 “Pace Abuser” Moments Part 2,https://www.youtube.com/shorts/jxz2A7GHTGM,Queued
2026-09-01,Top Smartest Goalkeeper Moments Part 2,https://www.youtube.com/shorts/I1DF9y0N_dM,Queued
2026-09-01,Top 5 Players Who Deserve the Oscar Award Part 2,https://www.youtube.com/shorts/uJEw4mhEYW8,Approved
2026-09-01,Top 5 Most Nonchalant Moments in Football (2026 Redo),https://www.youtube.com/shorts/21vNfEeIfK0,Queued
2026-09-01,Worst Penalty Miss With Every Technique in Football Part 2,https://www.youtube.com/shorts/hxBxS7QX354,Queued
2026-09-01,Top 5 Worst Ballon D’or Winners in Football Part 2,https://www.youtube.com/shorts/0g3cftFz08k,Queued
2026-09-01,Top 5 “Die for the Badge” Moments in Football (2026 Redo),https://www.youtube.com/shorts/WBDNj2kL0lw,Queued
2026-09-01,Top 5 Most “Selfish” Moments in Football (2026 Redo),https://www.youtube.com/shorts/9UlTiyixsSU,Queued
2026-09-01,Top 5 Shortest Lived Primes in Football (2026 Redo),https://www.youtube.com/shorts/9aYJ3lBf7HY,Approved
2026-09-01,Top 5 Worst Hattricks in Football (2026 Redo),https://www.youtube.com/shorts/8oo_OTaBxw0,Queued
2026-09-01,Top 10 Signature Moves in Football (2026 Redo),https://www.youtube.com/shorts/gaLafBORfYA,Approved
2026-09-01,Top 5 Most Awkward Moments in Football,https://www.youtube.com/shorts/9uePfdcjzF0,Queued
2026-09-01,Top Players Toying With Goalkeepers,https://www.youtube.com/shorts/ywSjoH8FwLE,Queued
2026-09-01,When Goalkeepers Make Accidental Saves,https://www.youtube.com/shorts/ZbunM6UKwts,Approved
2026-09-01,When Goalkeepers Aren't Ready,https://www.youtube.com/shorts/Z5sgNMojUz4,Queued
2026-09-01,Goalkeepers With Unbelievable Assists,https://www.youtube.com/shorts/tBPdLG2ZsgY,Approved
2026-09-01,Ranking the Funniest Footballer Lookalikes,https://www.youtube.com/shorts/rVw2TmDJf9o,Dropped 2026-09-20
2026-09-01,Imagine If These Players NEVER Got Injured,https://www.youtube.com/shorts/z73OYyghBxw,Queued
2026-09-07,What If Messi & Ronaldo Swapped Nationalities?,https://www.youtube.com/shorts/DZ2cXN-7GxE,Approved
2026-09-07,"What If PSG Kept Messi, Neymar & Mbappé?",https://www.youtube.com/shorts/kymTJlWMyzk,Approved
2026-09-07,Transfers That Almost Happened,https://www.youtube.com/shorts/0_yDGO1Jgt0,Approved
2026-09-07,What If Ronaldo Never Left Real Madrid?,https://www.youtube.com/shorts/zilVLvf10Sk,Approved
2026-09-07,What If These Players Played for Other Countries?,https://www.youtube.com/shorts/hgE5AqUCBdM,Queued
2026-09-07,Players We Always Mispronounce,https://www.youtube.com/shorts/GT-1mKJRDxU,Approved
2026-09-07,Players We Always Forget Played for That Club,https://www.youtube.com/shorts/GT-1mKJRDxU,Approved
2026-09-07,Players We Always Blame First,https://www.youtube.com/shorts/GT-1mKJRDxU,Approved
2026-09-07,Players You Forgot Played Together,https://www.youtube.com/shorts/GT-1mKJRDxU,Queued
2026-09-07,Players We Always Confuse With Each Other,https://www.youtube.com/shorts/GT-1mKJRDxU,Queued
2026-09-07,Players Who Were Better Than You Remember,https://www.youtube.com/shorts/UxEVQJNshcM,Queued
2026-09-07,The Best Player From Every Year (2000–2025),https://www.youtube.com/shorts/sCXb8WPrxys,Queued
2026-09-07,If Every Wrongly Disallowed Goal Had Counted,https://www.youtube.com/shorts/R7A9MbPIegM,Queued
2026-09-07,What If Clubs Could Only Use Academy Players?,https://www.youtube.com/shorts/GqN5uAV-cgY,Queued
2026-09-07,If Neymar Stayed at Barcelona,https://www.youtube.com/shorts/OofqZWb4hmg,Queued
2026-09-07,Players Everyone Wanted at Their Club,https://www.youtube.com/shorts/GT-1mKJRDxU,Queued
2026-09-07,Players We All Copied in the Playground,https://www.youtube.com/shorts/GT-1mKJRDxU,Queued
2026-09-07,The Most Overrated Player at Every Club,https://www.youtube.com/shorts/QmGY9zOqgXI,Queued
2026-09-07,Players You Forgot Are Still Playing,https://www.youtube.com/shorts/atZZ1NDURng,Queued
2026-09-07,What If These Transfers Never Happened?,https://www.youtube.com/shorts/z73OYyghBxw,Queued
2026-09-07,Moments That Confused Everyone on the Pitch,https://www.youtube.com/shorts/K2XdlhhUQWM,Queued
2026-09-07,When Strikers Aren't Ready,https://www.youtube.com/shorts/Z5sgNMojUz4,Queued
2026-09-07,Worst Ballon d'Or Decision From Every Year,https://www.youtube.com/shorts/0g3cftFz08k,Queued
2026-09-07,One-Season Wonder From Every Year in Football,https://www.youtube.com/shorts/9aYJ3lBf7HY,Queued
2026-09-14,Top 5 Legendary Fake Plays in Football,https://www.youtube.com/shorts/Y5KvUslNHzA,Queued
2026-09-14,Top 5 Big Brain Time-Wasting Tactics,https://www.youtube.com/shorts/6Z9TDqkjZDs,Queued
2026-09-14,Top 5 Goalkeeper 'Brain Freeze' Moments,https://www.youtube.com/shorts/z6Ie5elp3YY,Queued
2026-09-14,Top 5 Shameless Goal Steals in Football,https://www.youtube.com/shorts/2U-lZSwWSLw,Queued
2026-09-14,Top 5 Failed Goalkeeper Attacks,https://www.youtube.com/shorts/ryiFzPOX1pg,Queued
2026-09-14,Top 5 Most Predictable Penalty Misses,https://www.youtube.com/shorts/1jPYXAXO3D8,Queued
2026-09-14,Top 5 Next-Level Women's Goalkeepers,https://www.youtube.com/shorts/FC2spOXemNc,Queued
2026-09-14,Top 5 Tactical Fouls That Got Personal,https://www.youtube.com/shorts/TjH2_lU7mCY,Queued
2026-09-14,Top 5 Funny & Weird Penalty Kicks,https://www.youtube.com/shorts/U4wNPSYsx64,Queued
2026-09-14,When Penalty Predictions Go Too Far,https://www.youtube.com/shorts/YQcadVf_0Hs,Queued
2026-09-14,When Footballers Try to Act Smart,https://www.youtube.com/shorts/Ymywd09MNDQ,Queued
2026-09-14,When Defenders Lose All Aura,https://www.youtube.com/shorts/1OkRK_xjjSI,Queued
2026-09-14,What If Nations NEVER Lost a World Cup Final?,https://www.youtube.com/shorts/44EW28CRzRo,Queued
2026-09-14,What If Dortmund NEVER Sold Their Players?,https://www.youtube.com/shorts/UVQa6nBSCZI,Queued
2026-09-14,Top 5 'Move Man!!' Moments in Football,https://www.youtube.com/shorts/zOVU1cpV3wQ,Queued
2026-09-14,When Football Becomes Art,https://www.youtube.com/shorts/MfjF9Ggj57A,queued
2026-09-14,Top 5 Goalkeeper 'Aura' Moments,https://www.youtube.com/shorts/f89j7g33R14,queued
2026-09-14,Top 5 Footballers With the Biggest Calves,https://www.youtube.com/shorts/4ODlzRGoHrk,queued
2026-09-14,The 5 Tallest Footballers on Earth,https://www.youtube.com/shorts/ansitXwUTSU,queued
2026-09-14,Last 5 Golden Boy Winners — Where Are They Now?,https://www.youtube.com/shorts/tBes9lUlNu8,queued
2026-09-18,Worst Penalty Miss With Every Technique Part 2,https://www.youtube.com/shorts/hxBxS7QX354,Approved
2026-09-18,Top 5 Die for the Badge Moments (2026 Redo),https://www.youtube.com/shorts/WBDNj2kL0lw,Approved
2026-09-18,Top 5 Shortest Lived Primes (2026 Redo),https://www.youtube.com/shorts/9aYJ3lBf7HY,Approved
2026-09-18,Top 10 Signature Moves (2026 Redo),https://www.youtube.com/shorts/gaLafBORfYA,Approved
2026-09-18,Players Who Could've Played For Another Nation,https://www.youtube.com/shorts/0zxkpSnyZJs,Approved
```

#### `rejected.json`
<!-- FILE: rejected.json · 10623 bytes · 256 lines · sha256 7946832fc1ba1f89b2085b5879aafcde9d0fc25e9de08c3fdc89aa3887040207 -->
*254 rejected titles incl. lookalikes.*
```json
[
 "'Why Would You Shoot That' From Every Year",
 "1000 IQ Corner Kick Routines",
 "Best 'Aura' Goal From Every Year in Football",
 "Best 'Pace Abuser' Moment From Every Year",
 "Best Debut Goal From Every Premier League Club",
 "Best Debut Goal With Every Technique",
 "Best Goal From Every Year in Football",
 "Best Goal-Line Clearance From Every World Cup",
 "Best Last-Minute Goal From Every World Cup",
 "Best Nutmeg From Every World Cup",
 "Best Offside Goal From Every World Cup",
 "Best Penalty From Every World Cup",
 "Best Penalty Save From Every World Cup",
 "Best Player From Every Letter of the Alphabet",
 "Best Player From Every World Cup",
 "Best Playmaker From Every Year in Football",
 "Best Real Madrid Player From Every Year",
 "Best Save From Every World Cup FINAL",
 "Best Tackle From Every World Cup",
 "Best Volley From Every Year in Football",
 "Best World Cup Goal From Every Decade",
 "Biggest Sneaky Moments in Football",
 "Champions League or Premier League: Which Is Harder?",
 "Craziest Offside Call From Every Year",
 "Craziest Sunday League Moments Ranked",
 "Days Football Fans Aren't Ready For",
 "Every Nation's Biggest Defeat",
 "Every Nation's First International Trophy",
 "Every Team's Biggest Ever Win",
 "Feats Only One Manager Has Ever Achieved",
 "Football Players That Disappeared",
 "Football Respect Moments",
 "Football in the Year 2090",
 "Football vs Trophies",
 "Grab the Ball Time-Wasting Moments",
 "Imagine If These Went In (Almost-Goals)",
 "Impossible Ways to Control the Ball",
 "Impossible Ways to Make a Tackle",
 "Impossible Ways to Man-Mark",
 "Impossible Ways to Score a Tap-In",
 "Impossible Ways to Take a Goal Kick",
 "Insane Illusion Moments in Football",
 "Kickoff Tactics That Actually Worked",
 "King of Every Decade in Football Part 2",
 "King of Every Position",
 "Legendary Debut Goals",
 "Managers Who Scored Iconic Goals",
 "Mbappe vs Prime Henry",
 "Moments Only Real Fans Remember",
 "Most 'Nonchalant' Moment From Every Year",
 "Most 'Selfish' Moment From Every Year",
 "Most Difficult Paths in Champions League History",
 "Most Powerful Goal From Every Year in Football",
 "Most Satisfying Long-Distance Assists",
 "Offside Calls That Make No Sense",
 "Optical Illusion Goals",
 "Penalty Mind Games That Actually Worked",
 "Pick the Ballon d'Or Winner (interactive)",
 "Players Who Fell Off the Fastest",
 "Players Who Refused to Let Others Be Forgotten",
 "Players With the Most World Cup Final Losses",
 "Players vs Water",
 "Prime Neymar vs Other Prime Players",
 "Ranking Impressive Skills 7 to 1",
 "Ranking the Best Joga Bonito Skills",
 "Ranking the Best Referee Mic'd-Up Moments",
 "Ranking the Most Hilarious Fan Moments",
 "Real Madrid's Scariest Team Ever",
 "Revenge Moments in Football",
 "Ronaldo Teaching Young Players",
 "Saves That Never Won Save of the Year",
 "Smartest Goalkeeper Moment From Every Year",
 "The Best 90+ Penalty From Every Minute",
 "The Best Goal of 2026 From Every Competition",
 "The Best Goalkeeper From Every Country",
 "The Best Save Against Every Striking Technique",
 "The Best Skill Move From Every Decade",
 "The Best Song From Every World Cup",
 "The GOAT of Every Decade in Football",
 "The Greatest Player From Every Country",
 "The Most Iconic Celebrations in Football",
 "The Most Iconic Commentary Moments Ever",
 "The Most Iconic Hat-Tricks in Football History",
 "The Worst 90+ Penalty Miss From Every Minute",
 "The Worst Referee Bans in Football History",
 "The Worst Referee Mistake From Every Competition",
 "The Worst Signing From Every League",
 "Things That May NEVER Happen Again in Football",
 "Top 10 Defender Goals in Football Part 2",
 "Top 10 Players Who Never Won the Champions League",
 "Top 10 Ronaldo Selfish Moments",
 "Top 1v1 Moments That Ended Careers",
 "Top 3 Players Who Retired Too Young Part 2",
 "Top 5 '0 Finishing' Moments in Football",
 "Top 5 '0 IQ' Goalkeeper Skills",
 "Top 5 'Absolute Chaos' in the Penalty Box",
 "Top 5 'Absolute Humiliations' in Football",
 "Top 5 'Ego' Moments in Football",
 "Top 5 'Games Gone Soft' Clean Tackles",
 "Top 5 'Greedy' Moments in Football",
 "Top 5 'Heated' Dressing Room Moments",
 "Top 5 'High Ping' Moments in Football",
 "Top 5 'Main Character' Moments in Football",
 "Top 5 'Max Aura' Penalty Techniques",
 "Top 5 'Men vs Women' Football Moments",
 "Top 5 'Players vs Fans' Moments in Football",
 "Top 5 'Rage Bait' Penalties in Football",
 "Top 5 'Ragebait' Celebrations in Football",
 "Top 5 'Unforgettable' Reactions in Football",
 "Top 5 'WTF' Moments in Football",
 "Top 5 99 Strength Moments in Football Part 2",
 "Top 5 Assist = Goal Moments",
 "Top 5 Aura Goals in Football Part 2",
 "Top 5 Best Debut Goals in Football Part 2",
 "Top 5 Big Brain Defending Moments",
 "Top 5 Big Brain Goal-Line Clearances",
 "Top 5 Big Brain Throw-Ins",
 "Top 5 CR7 Bluetooth Link-Up Moments",
 "Top 5 Carrer Comebacks in Football History Part 2",
 "Top 5 Cheeky Penalties That Fooled Everyone",
 "Top 5 Coaches Who Completely Lost It",
 "Top 5 Corner Flag Battles in Football",
 "Top 5 Crashout Moments Part 2",
 "Top 5 Craziest Offside Calls Part 2",
 "Top 5 Cringe & Awkward Celebrations",
 "Top 5 Defenders Getting Deleted",
 "Top 5 Disallowed Goal Celebrations",
 "Top 5 Diving Header Goals",
 "Top 5 Dumbest Red Cards Part 2",
 "Top 5 FIFA Glitches That Broke the Net",
 "Top 5 Fan Reactions in Football Part 2",
 "Top 5 Football Headshots That Hurt to Watch",
 "Top 5 Football Moments That Looked Like Basketball",
 "Top 5 Footballers Using Their Head Instead of Feet",
 "Top 5 Free Kicks Scored on Courtois",
 "Top 5 Funny Brother Reactions in Football",
 "Top 5 Future Football Projects (Wonderkids)",
 "Top 5 Goalkeeper Humiliations in Football",
 "Top 5 Goalkeepers Who Forgot the Rules",
 "Top 5 Goals From Crazy Angles",
 "Top 5 Goals Straight Out of FIFA",
 "Top 5 High-Pressing Moments in Football",
 "Top 5 Humiliating Skills in Football Part 2",
 "Top 5 Iconic Fake-Shot Goals",
 "Top 5 Impossible Twin Shots in Football",
 "Top 5 Insane First-Touch Assists",
 "Top 5 Knuckleball Free Kicks in Football",
 "Top 5 Legendary Goalkeeper Recovery Saves",
 "Top 5 Legends Who Forgot How to Play Part 2",
 "Top 5 Luckiest Penalties Ever Taken",
 "Top 5 Manager Ball Control Skills",
 "Top 5 Max Strength Moments in Football",
 "Top 5 Most Beautiful Team Goals in Football",
 "Top 5 Most Controversial Goals in Football History",
 "Top 5 Most Embarrassing Dribbles That Led to Goals",
 "Top 5 Most Embarrassing Mistakes in Football",
 "Top 5 Most Lucky Goals in Football Part 2",
 "Top 5 Most Selfish Moments Part 2",
 "Top 5 Open-Net Disasters in Football",
 "Top 5 Perfect Penalties Scored by Kids",
 "Top 5 Players Carded for the Dumbest Reasons",
 "Top 5 Players Getting Cooked in 1v1s",
 "Top 5 Players Pushing the Keeper (Cheeky Edition)",
 "Top 5 Post-and-In Goals",
 "Top 5 Power Shots That Went Completely Wrong",
 "Top 5 Rarest Body-Part Goals",
 "Top 5 Ronaldo 'Lying' Moments",
 "Top 5 Ronaldo Bicycle Kick Goals",
 "Top 5 Ronaldo Bluetooth Moments in Football Part 2",
 "Top 5 Ronaldo Crashout Moments Part 2",
 "Top 5 Ronaldo Solo Goals",
 "Top 5 Ronaldo True Captain Moments",
 "Top 5 Shameless Late Dives in Football",
 "Top 5 Shameless Red Card Protests",
 "Top 5 Shortest Players Who Scored Headers",
 "Top 5 Skill Moves Gone Wrong",
 "Top 5 Skills That Don't Make Sense",
 "Top 5 Smartest & Cheekiest Goals",
 "Top 5 Sneak-100 Moments in Football",
 "Top 5 Sneakiest Goalkeeper Robberies Part 2",
 "Top 5 Times Aura Took Over Football",
 "Top 5 Times Ronaldo Was on Another Level",
 "Top 5 Unforgettable Panenka Penalties",
 "Top 5 Volley Goals Straight Out of Anime",
 "Top 5 Worst Pitches Ever Seen",
 "Top 5 Yellow Cards That Make No Sense",
 "Top 7 Most Powerful Goals Part 2",
 "Top Saves That Look Like AI",
 "What Every Country Won From the World Cup",
 "What If Clubs Could NEVER Reject a Transfer Bid?",
 "What If Football NEVER Existed?",
 "What If Football Never Had VAR?",
 "What If Offside Never Existed?",
 "What If Players Could Only Win ONE Ballon d'Or?",
 "What If Sporting / Ajax / Benfica NEVER Sold Their Players?",
 "What If an NBA Star Played Football? (Wemby / LeBron)",
 "When Brain Lag Hits in Football",
 "When Defenders Forget the Striker",
 "When Defenders Have Infinite Aura",
 "When Footballers Used 'Magic Drinks'",
 "When Goalkeepers Make Strikers Furious",
 "When Goalkeepers Take Penalty Kicks",
 "When It Rains in Football",
 "When Keepers Forget Their Job",
 "When Legends Play Sunday League",
 "When Medical Staff Get Bored",
 "When Outfield Players Go in Goal",
 "When Penalty Passes Go Wrong",
 "When Players Assist the Wrong Team",
 "When Players Go Over the Ad Boards",
 "When Players Refuse to Use Their Weak Foot",
 "When Players Score High-IQ Goals",
 "When Players Score Without Even Trying",
 "When Tricks Go Wrong in Football",
 "Wholesome Mascot Kid Moments",
 "Women's Football Moments That Shocked Everyone",
 "Worst Mistake From Every World Cup",
 "Worst Mistake From Every Year in Football",
 "Worst Penalty Miss From Every Year in Football",
 "Young Players Who Look 40",
 "Legends Pick the Best Current Goalkeeper",
 "Top 5 Funniest Moments in Football",
 "Top 5 Insane Goalkeeper Reactions",
 "Top 5 Football Challenge Moments",
 "Top 5 'Revenge' Moments in Football (2026 Redo)",
 "Ranking the Funniest AI Football Videos",
 "Top 5 Best Player Presentations Ever",
 "Top 5 Best Commentary Moments in Football",
 "Top 5 Best Stadium Moments in Football",
 "Top 5 Funniest Fan Moments in Football",
 "When Footballers Sing",
 "Top 5 Most Overrated Footballers of All Time",
 "Footballers vs the Goalkeeper Robot",
 "Players Who Got in Trouble for the Silliest Reasons",
 "When the Referee Stole the Show",
 "Top 5 Playing Styles in Football (Joga Bonito, Tiki-Taka\u2026)",
 "Top 5 Times the Referee Was Actually Right",
 "Top 5 Argentina Players of All Time (All-Time XI)",
 "Top 5 Messi Training Moments",
 "Top 5 Most Modern Football Stadiums",
 "Ranking iShowSpeed x Footballer Moments",
 "Only Real Fans Remember These\u2026",
 "Top 5 Most Relatable Football Moments",
 "Top 5 Greatest Footballers Who Have Passed Away",
 "Top 5 Micah Richards / CBS Panel Moments",
 "Our Legends Are Getting Old",
 "Top 5 'Football Core' Moments",
 "Ranking Demb\u00e9l\u00e9's Best Moments",
 "Moments You Missed From the 2022 World Cup Final",
 "Top 5 Most Disrespectful Moments in Football",
 "Top 5 Biggest Football Fails Ever",
 "Top 5 Goals of the 2022 World Cup",
 "Top 5 Assists of 2026 (So Far)",
 "Ranking the Funniest Footballer Lookalikes"
]
```

#### `dedup_base.json`
<!-- FILE: dedup_base.json · 5572 bytes · 157 lines · sha256 dbf5e2f4ae6ba70da3c8e8151589987eb659147203b2df497b8eaa9dc8dc3130 -->
*155 normalised titles ever surfaced, incl. lookalikes.*
```json
[
 "bestdebutgoalwitheverytechnique",
 "bestgoallineclearancefromeveryworldcup",
 "bestlastminutegoalfromeveryworldcup",
 "bestnutmegfromeveryworldcup",
 "bestoffsidegoalfromeveryworldcup",
 "bestpenaltyfromeveryworldcup",
 "bestpenaltysavefromeveryworldcup",
 "bestsavefromeveryworldcupfinal",
 "besttacklefromeveryworldcup",
 "bestworldcupgoalfromeverydecade",
 "daysfootballfansarentreadyfor",
 "everynationsbiggestdefeat",
 "everynationsfirstinternationaltrophy",
 "everyteamsbiggesteverwin",
 "footballersvsthegoalkeeperrobot",
 "footballintheyear2090",
 "footballvstrophies",
 "imagineifthesewentinalmostgoals",
 "impossiblewaystocontroltheball",
 "impossiblewaystomakeatackle",
 "impossiblewaystomanmark",
 "impossiblewaystoscoreatapin",
 "impossiblewaystotakeagoalkick",
 "last5goldenboywinnerswherearetheynow",
 "legendspickthebestcurrentgoalkeeper",
 "momentsyoumissedfromthe2022worldcupfinal",
 "mostdifficultpathsinchampionsleaguehistory",
 "onlyrealfansrememberthese",
 "ourlegendsaregettingold",
 "picktheballondorwinnerinteractive",
 "playerswhogotintroubleforthesilliestreasons",
 "playerswhorefusedtoletothersbeforgotten",
 "playerswiththemostworldcupfinallosses",
 "rankingdemblsbestmoments",
 "rankingishowspeedxfootballermoments",
 "rankingthefunniestaifootballvideos",
 "the5tallestfootballersonearth",
 "thebest90penaltyfromeveryminute",
 "thebestsaveagainsteverystrikingtechnique",
 "thebestsongfromeveryworldcup",
 "theworst90penaltymissfromeveryminute",
 "thingsthatmayneverhappenagaininfootball",
 "top50iqgoalkeeperskills",
 "top5absolutechaosinthepenaltybox",
 "top5absolutehumiliationsinfootball",
 "top5argentinaplayersofalltimealltimexi",
 "top5assistsof2026sofar",
 "top5bestcommentarymomentsinfootball",
 "top5bestplayerpresentationsever",
 "top5beststadiummomentsinfootball",
 "top5bigbraintimewastingtactics",
 "top5biggestfootballfailsever",
 "top5cheekypenaltiesthatfooledeveryone",
 "top5coacheswhocompletelylostit",
 "top5cornerflagbattlesinfootball",
 "top5cringeawkwardcelebrations",
 "top5defendersgettingdeleted",
 "top5disallowedgoalcelebrations",
 "top5divingheadergoals",
 "top5failedgoalkeeperattacks",
 "top5fifaglitchesthatbrokethenet",
 "top5footballchallengemoments",
 "top5footballcoremoments",
 "top5footballersusingtheirheadinsteadoffeet",
 "top5footballerswiththebiggestcalves",
 "top5footballmomentsthatlookedlikebasketball",
 "top5freekicksscoredoncourtois",
 "top5funniestfanmomentsinfootball",
 "top5funniestmomentsinfootball",
 "top5funnybrotherreactionsinfootball",
 "top5funnyweirdpenaltykicks",
 "top5futurefootballprojectswonderkids",
 "top5gamesgonesoftcleantackles",
 "top5goalkeeperauramoments",
 "top5goalkeeperbrainfreezemoments",
 "top5goalkeeperhumiliationsinfootball",
 "top5goalkeeperswhoforgottherules",
 "top5goalsfromcrazyangles",
 "top5goalsofthe2022worldcup",
 "top5goalsstraightoutoffifa",
 "top5greatestfootballerswhohavepassedaway",
 "top5highpressingmomentsinfootball",
 "top5iconicfakeshotgoals",
 "top5impossibletwinshotsinfootball",
 "top5insanefirsttouchassists",
 "top5insanegoalkeeperreactions",
 "top5knuckleballfreekicksinfootball",
 "top5legendaryfakeplaysinfootball",
 "top5legendarygoalkeeperrecoverysaves",
 "top5luckiestpenaltiesevertaken",
 "top5managerballcontrolskills",
 "top5maxaurapenaltytechniques",
 "top5messitrainingmoments",
 "top5micahrichardscbspanelmoments",
 "top5mostcontroversialgoalsinfootballhistory",
 "top5mostdisrespectfulmomentsinfootball",
 "top5mostembarrassingdribblesthatledtogoals",
 "top5mostembarrassingmistakesinfootball",
 "top5mostmodernfootballstadiums",
 "top5mostoverratedfootballersofalltime",
 "top5mostpredictablepenaltymisses",
 "top5mostrelatablefootballmoments",
 "top5movemanmomentsinfootball",
 "top5nextlevelwomensgoalkeepers",
 "top5perfectpenaltiesscoredbykids",
 "top5playersgettingcookedin1v1s",
 "top5playingstylesinfootballjogabonitotikitaka",
 "top5postandingoals",
 "top5powershotsthatwentcompletelywrong",
 "top5ragebaitcelebrationsinfootball",
 "top5ragebaitpenaltiesinfootball",
 "top5rarestbodypartgoals",
 "top5revengemomentsinfootball2026redo",
 "top5ronaldolyingmoments",
 "top5shamelessgoalstealsinfootball",
 "top5shamelesslatedivesinfootball",
 "top5shortestplayerswhoscoredheaders",
 "top5skillsthatdontmakesense",
 "top5smartestcheekiestgoals",
 "top5sneak100momentsinfootball",
 "top5tacticalfoulsthatgotpersonal",
 "top5timesauratookoverfootball",
 "top5timesronaldowasonanotherlevel",
 "top5timestherefereewasactuallyright",
 "top5unforgettablereactionsinfootball",
 "top5volleygoalsstraightoutofanime",
 "whatifannbastarplayedfootballwembylebron",
 "whatifclubscouldneverrejectatransferbid",
 "whatifdortmundneversoldtheirplayers",
 "whatiffootballneverexisted",
 "whatifnationsneverlostaworldcupfinal",
 "whatifoffsideneverexisted",
 "whatifplayerscouldonlywinoneballondor",
 "whatifsportingajaxbenficaneversoldtheirplayers",
 "whenbrainlaghitsinfootball",
 "whendefendersforgetthestriker",
 "whendefendershaveinfiniteaura",
 "whendefendersloseallaura",
 "whenfootballbecomesart",
 "whenfootballerssing",
 "whenfootballerstrytoactsmart",
 "whenfootballersusedmagicdrinks",
 "whengoalkeeperstakepenaltykicks",
 "whenitrainsinfootball",
 "whenkeepersforgettheirjob",
 "whenmedicalstaffgetbored",
 "whenpenaltypassesgowrong",
 "whenpenaltypredictionsgotoofar",
 "whenplayersgoovertheadboards",
 "whenplayersrefusetousetheirweakfoot",
 "whenplayersscorehighiqgoals",
 "whenplayersscorewithouteventrying",
 "whentherefereestoletheshow",
 "whentricksgowronginfootball",
 "rankingthefunniestfootballerlookalikes"
]
```

#### `own.json`
<!-- FILE: own.json · 85299 bytes · 1 lines · sha256 9bc08df76b1f5893f599c5181b6918646c4e483cd2b1f6856a414d53af890293 -->
*Joel's catalogue, 459 entries, scraped 14 Sep with get_channel_shorts. Refresh at Stage 0 of the next run (E01, E02).*
```json
[{"title": "Top 5 Times Prime Ronaldo Was Simply UNSTOPPABLE", "url": "https://www.youtube.com/shorts/94826pmXHro", "views": 203, "comments": 2, "date": "2026-09-14", "account": "own"}, {"title": "Top 5 Free Kicks ONLY Ronaldo Could Score in Football", "url": "https://www.youtube.com/shorts/zY-eJWUaJqE", "views": 859, "comments": 6, "date": "2026-09-14", "account": "own"}, {"title": "Top 5 Defenders Who Deserved The Ballon D’or", "url": "https://www.youtube.com/shorts/0X2oR19lFfg", "views": 22169, "comments": 56, "date": "2026-09-13", "account": "own"}, {"title": "Greatest Player in Every Countries History Part 2", "url": "https://www.youtube.com/shorts/D4CBmngxiig", "views": 21212, "comments": 62, "date": "2026-09-13", "account": "own"}, {"title": "Greatest Player in Every Countries History Part 1", "url": "https://www.youtube.com/shorts/o-o8ZFteOTY", "views": 155378, "comments": 470, "date": "2026-09-13", "account": "own"}, {"title": "Top 5 Players Who Played Just HOURS After Tragedy", "url": "https://www.youtube.com/shorts/b4MH_xCedbI", "views": 390462, "comments": 130, "date": "2026-09-12", "account": "own"}, {"title": "Top 5 Most Disrespected Players in Football", "url": "https://www.youtube.com/shorts/eEpL9hjnYE0", "views": 245168, "comments": 124, "date": "2026-09-11", "account": "own"}, {"title": "Players Who Would’ve Won Ballon D’or Part 3", "url": "https://www.youtube.com/shorts/RWt5Fnj5JYM", "views": 66095, "comments": 115, "date": "2026-09-10", "account": "own"}, {"title": "Players Who Would Have Won Ballon D’or If Messi & Ronaldo Never Existed Part 1", "url": "https://www.youtube.com/shorts/x815Tr3zowI", "views": 31068, "comments": 57, "date": "2026-09-09", "account": "own"}, {"title": "Players Who Would Have Won Ballon D’or If Messi & Ronaldo Never Existed Part 2", "url": "https://www.youtube.com/shorts/Hd6IUX8b8lc", "views": 39043, "comments": 48, "date": "2026-09-09", "account": "own"}, {"title": "Top 5 Most Skillful Players in Football", "url": "https://www.youtube.com/shorts/XmOoHO4RdwQ", "views": 94391, "comments": 337, "date": "2026-09-09", "account": "own"}, {"title": "Top 10 Prime Legends That Had To Go", "url": "https://www.youtube.com/shorts/_7E5KfMSZ-8", "views": 131458, "comments": 119, "date": "2026-09-07", "account": "own"}, {"title": "Top 5 Legends Who Scored Directly From a Corner Kick", "url": "https://www.youtube.com/shorts/4hsRH2tnV_8", "views": 67355, "comments": 58, "date": "2026-09-07", "account": "own"}, {"title": "Top 5 Players Who Were Elite Then Suddenly Retired", "url": "https://www.youtube.com/shorts/OOlNNn6Xqzw", "views": 328490, "comments": 173, "date": "2026-09-07", "account": "own"}, {"title": "Top 5 Times Messi Destroyed Real Madrid", "url": "https://www.youtube.com/shorts/RgSB-CbFSwo", "views": 28554, "comments": 47, "date": "2026-09-06", "account": "own"}, {"title": "Top 5 Saddest Ways a Footballers Career Has Ended", "url": "https://www.youtube.com/shorts/Yt5c2SdCaqY", "views": 236722, "comments": 128, "date": "2026-09-06", "account": "own"}, {"title": "Top 5 Messi Crashout Moments in Football", "url": "https://www.youtube.com/shorts/KKckrZ242fU", "views": 75365, "comments": 237, "date": "2026-09-06", "account": "own"}, {"title": "Top 5 Goals Nobody Meant to Score in Football", "url": "https://www.youtube.com/shorts/VYkMeaXOMmA", "views": 716308, "comments": 184, "date": "2026-09-05", "account": "own"}, {"title": "Top 10 Football Legends Getting Nutmegged in Football", "url": "https://www.youtube.com/shorts/lZGroRw5NTU", "views": 193290, "comments": 56, "date": "2026-09-04", "account": "own"}, {"title": "Top 5 “Saddest” Messi Moments in Football", "url": "https://www.youtube.com/shorts/Psy4j4Vep6k", "views": 152527, "comments": 146, "date": "2026-09-04", "account": "own"}, {"title": "Top 5 “Crazy” Red Cards in Football", "url": "https://www.youtube.com/shorts/Qa26M0KLFzE", "views": 253875, "comments": 67, "date": "2026-09-03", "account": "own"}, {"title": "Top 5 “Insane” Ball Boy Moments in Football", "url": "https://www.youtube.com/shorts/8IsPenmHXSk", "views": 540645, "comments": 219, "date": "2026-09-03", "account": "own"}, {"title": "Top 5 Best Goalkeepers in the World Right Now in Football", "url": "https://www.youtube.com/shorts/gzQJex1_anM", "views": 458772, "comments": 1128, "date": "2026-09-03", "account": "own"}, {"title": "Top 5 Haaland Interview Moments in Football", "url": "https://www.youtube.com/shorts/QbdDlVZpAiA", "views": 118207, "comments": 75, "date": "2026-08-31", "account": "own"}, {"title": "Top 5 Impossible Ways to Take a Throw In", "url": "https://www.youtube.com/shorts/alefTLwrUJ8", "views": 106010, "comments": 27, "date": "2026-08-31", "account": "own"}, {"title": "Top 5 Kickoff Tactics That Actually Worked in Football", "url": "https://www.youtube.com/shorts/4gyFAcAOQiE", "views": 417722, "comments": 131, "date": "2026-08-30", "account": "own"}, {"title": "Top 5 “Biggest” Ballers in Football", "url": "https://www.youtube.com/shorts/qjvf8dvqUlk", "views": 69751, "comments": 52, "date": "2026-08-30", "account": "own"}, {"title": "Top 5 Ronaldo Contradict Moments in Football", "url": "https://www.youtube.com/shorts/EkeNUYXf1HA", "views": 102240, "comments": 265, "date": "2026-08-29", "account": "own"}, {"title": "Top 5 Times Legends Played Sunday League Football", "url": "https://www.youtube.com/shorts/82cxYbqY_9o", "views": 42323, "comments": 23, "date": "2026-08-29", "account": "own"}, {"title": "What If Teams NEVER Lost the UCL?", "url": "https://www.youtube.com/shorts/0tniQde8q48", "views": 891609, "comments": 174, "date": "2026-08-29", "account": "own"}, {"title": "Best Goal With Every Technique in Football Part 2", "url": "https://www.youtube.com/shorts/3Do4FgEOKCc", "views": 88945, "comments": 61, "date": "2026-08-28", "account": "own"}, {"title": "Best Goal With Every Technique in Football Part 1", "url": "https://www.youtube.com/shorts/Un0TgMmBzo4", "views": 150343, "comments": 87, "date": "2026-08-28", "account": "own"}, {"title": "Players We Always Call By Their Full Name Part 2", "url": "https://www.youtube.com/shorts/Lp4bjfWzHyI", "views": 449749, "comments": 502, "date": "2026-08-28", "account": "own"}, {"title": "Players We Always Call By Their Full Name", "url": "https://www.youtube.com/shorts/GT-1mKJRDxU", "views": 3240079, "comments": 4164, "date": "2026-08-27", "account": "own"}, {"title": "Imagine If These Teams NEVER SOLD Their Players", "url": "https://www.youtube.com/shorts/z73OYyghBxw", "views": 1109500, "comments": 812, "date": "2026-08-27", "account": "own"}, {"title": "Top 5 Perfect Penalties No Goalkeeper Can Save in Football", "url": "https://www.youtube.com/shorts/L7Kqm6cOYXo", "views": 120936, "comments": 131, "date": "2026-08-27", "account": "own"}, {"title": "Top 5 Messi Clips That Would Make You Think He’s TRASH", "url": "https://www.youtube.com/shorts/jpaxJrJfU18", "views": 205976, "comments": 297, "date": "2026-08-26", "account": "own"}, {"title": "Top 5 Times The Ball Disappeared in Football", "url": "https://www.youtube.com/shorts/1y5eBj9qpgY", "views": 28092, "comments": 24, "date": "2026-08-26", "account": "own"}, {"title": "Top 5 Free Kick Takers Who NEVER Miss", "url": "https://www.youtube.com/shorts/8-WvoaArUi0", "views": 157644, "comments": 297, "date": "2026-08-26", "account": "own"}, {"title": "Top 5 Best Sidemen Charity Match Goals in Football", "url": "https://www.youtube.com/shorts/t4us9r_NeJQ", "views": 390249, "comments": 201, "date": "2026-08-25", "account": "own"}, {"title": "Top 5 Times Players Stood Up For Racism", "url": "https://www.youtube.com/shorts/DDWv2m-l8-Q", "views": 1181667, "comments": 384, "date": "2026-08-23", "account": "own"}, {"title": "Top 5 “Respectful” Moments in Football", "url": "https://www.youtube.com/shorts/z3a-6sMbiWw", "views": 488140, "comments": 129, "date": "2026-08-22", "account": "own"}, {"title": "Top 5 “Hand of God” Moments in Football", "url": "https://www.youtube.com/shorts/KTAus-EciNk", "views": 256740, "comments": 181, "date": "2026-08-21", "account": "own"}, {"title": "Top 5 Free Kicks That Broke The Laws of Physics", "url": "https://www.youtube.com/shorts/OSMIFXHBhx8", "views": 32370, "comments": 54, "date": "2026-08-20", "account": "own"}, {"title": "Top 5 “Negative Aura” Moments in Football", "url": "https://www.youtube.com/shorts/8XkO1A_-YgM", "views": 84752, "comments": 56, "date": "2026-08-19", "account": "own"}, {"title": "Top 5 Viral Trend Celebrations in Football", "url": "https://www.youtube.com/shorts/8NXSArPxop4", "views": 427175, "comments": 124, "date": "2026-08-18", "account": "own"}, {"title": "Top 5 Legendary Chest and Volley Goals in Football", "url": "https://www.youtube.com/shorts/vhYBkta6CY4", "views": 45132, "comments": 67, "date": "2026-08-17", "account": "own"}, {"title": "Top 5 Times Players Fought Their Own Teamates in Football", "url": "https://www.youtube.com/shorts/MBVj1_oyDVY", "views": 151534, "comments": 95, "date": "2026-08-17", "account": "own"}, {"title": "Top 5 Physically Impossible Goals in Football", "url": "https://www.youtube.com/shorts/m18VQ8UtjJY", "views": 52392, "comments": 77, "date": "2026-08-15", "account": "own"}, {"title": "Top 10 Worst Own Goals in Premier League", "url": "https://www.youtube.com/shorts/QUug1PYzoZE", "views": 67468, "comments": 84, "date": "2026-08-15", "account": "own"}, {"title": "Top 5 Olise “Nonchalant” Moments in Football", "url": "https://www.youtube.com/shorts/X3J11VMRGgk", "views": 144737, "comments": 100, "date": "2026-08-14", "account": "own"}, {"title": "Top 5 “True Captain” Moments in Football", "url": "https://www.youtube.com/shorts/73XGOc7_doU", "views": 657433, "comments": 181, "date": "2026-08-14", "account": "own"}, {"title": "Top 5 Ronaldo Rare Moments", "url": "https://www.youtube.com/shorts/VVAgKMHxjuE", "views": 192551, "comments": 119, "date": "2026-08-13", "account": "own"}, {"title": "Top 5 “Weirdest” Running Styles in Football", "url": "https://www.youtube.com/shorts/s_QOejqoy60", "views": 961840, "comments": 250, "date": "2026-08-13", "account": "own"}, {"title": "Top 5 “Illegal” Handball Saves in Football", "url": "https://www.youtube.com/shorts/mFkzig-I-XA", "views": 1199092, "comments": 305, "date": "2026-08-12", "account": "own"}, {"title": "Top 5 Times it Rained in Football", "url": "https://www.youtube.com/shorts/4YJXYC5thWY", "views": 607846, "comments": 161, "date": "2026-08-11", "account": "own"}, {"title": "Top 5 “Crucial” Last Minute Saves", "url": "https://www.youtube.com/shorts/I9MkUmIs-4M", "views": 101392, "comments": 83, "date": "2026-08-11", "account": "own"}, {"title": "Top 5 “Big Brain” Goalkeepers Moments", "url": "https://www.youtube.com/shorts/fCYztc7zN2k", "views": 2281077, "comments": 270, "date": "2026-08-10", "account": "own"}, {"title": "Top 5 “Rare” Moments in Football", "url": "https://www.youtube.com/shorts/5Hoq_h_SPwU", "views": 700402, "comments": 146, "date": "2026-08-09", "account": "own"}, {"title": "Top 5 “Players vs Referee” Moments in Football", "url": "https://www.youtube.com/shorts/D7IgBlomjWY", "views": 442946, "comments": 126, "date": "2026-08-09", "account": "own"}, {"title": "Top 5 “Why Would You Shoot That” Moments in Football Part 2", "url": "https://www.youtube.com/shorts/FWnkgy65490", "views": 197094, "comments": 251, "date": "2026-08-09", "account": "own"}, {"title": "Top 5 Best Goalkeepers in 2026 World Cup", "url": "https://www.youtube.com/shorts/tCvOLvz6f7E", "views": 442355, "comments": 1457, "date": "2026-08-08", "account": "own"}, {"title": "Top 10 Best Players in Football History", "url": "https://www.youtube.com/shorts/AEoCgG6EilE", "views": 314526, "comments": 2924, "date": "2026-08-08", "account": "own"}, {"title": "Top 5 “Rarest” Moments With Balls", "url": "https://www.youtube.com/shorts/IJyx_rxIVeE", "views": 330519, "comments": 135, "date": "2026-08-08", "account": "own"}, {"title": "Top 5 “Richest” Footballers That Will SHOCK You", "url": "https://www.youtube.com/shorts/JDgMXYz49jc", "views": 230965, "comments": 67, "date": "2026-08-07", "account": "own"}, {"title": "Top 5 Worst Champions League Winners in Football", "url": "https://www.youtube.com/shorts/eY9LAAlbdRs", "views": 317760, "comments": 505, "date": "2026-08-07", "account": "own"}, {"title": "Top 10 Players in the World Right Now", "url": "https://www.youtube.com/shorts/vBuQvILmdxo", "views": 510536, "comments": 2459, "date": "2026-08-07", "account": "own"}, {"title": "Top 5 Worst Ballon D’or Winners in Football", "url": "https://www.youtube.com/shorts/0g3cftFz08k", "views": 2772861, "comments": 8862, "date": "2026-08-06", "account": "own"}, {"title": "Top 10 Players Who NEVER Won a World Cup", "url": "https://www.youtube.com/shorts/cG-dlLeQnlw", "views": 480625, "comments": 661, "date": "2026-08-06", "account": "own"}, {"title": "King of Every Decade in Football", "url": "https://www.youtube.com/shorts/sCXb8WPrxys", "views": 985867, "comments": 2483, "date": "2026-08-06", "account": "own"}, {"title": "Top 5 Times The Ball Exploded in Football", "url": "https://www.youtube.com/shorts/F7uCJP-n7ek", "views": 1281678, "comments": 258, "date": "2026-08-05", "account": "own"}, {"title": "Biggest Underdogs From Every World Cup", "url": "https://www.youtube.com/shorts/_L9e477EIr4", "views": 406918, "comments": 384, "date": "2026-08-05", "account": "own"}, {"title": "Top 5 “Scariest” Attacking Trios in Football", "url": "https://www.youtube.com/shorts/radksODGWlg", "views": 626527, "comments": 547, "date": "2026-08-05", "account": "own"}, {"title": "Top 5 “Furious” Moments in Football", "url": "https://www.youtube.com/shorts/aUq_b2S4JzU", "views": 131620, "comments": 152, "date": "2026-08-04", "account": "own"}, {"title": "Top 5 Players Who Played for Country in World Cup They Weren’t Born In", "url": "https://www.youtube.com/shorts/ctz9xLklWnc", "views": 194118, "comments": 158, "date": "2026-08-04", "account": "own"}, {"title": "Top 10 Players to NEVER Win the Ballon D’or", "url": "https://www.youtube.com/shorts/8SZeeuP6lC8", "views": 164987, "comments": 1300, "date": "2026-08-04", "account": "own"}, {"title": "Top 5 Penalty Takers Who NEVER Miss in Football", "url": "https://www.youtube.com/shorts/RInNagRevHc", "views": 274474, "comments": 338, "date": "2026-08-03", "account": "own"}, {"title": "Top 5 “Dumbest” Smart Tricks in Football", "url": "https://www.youtube.com/shorts/moOf7dG-tdQ", "views": 2757629, "comments": 605, "date": "2026-08-03", "account": "own"}, {"title": "Top 10 Solo Goals in Football⚽️🔥", "url": "https://www.youtube.com/shorts/cJl--6aJJ8E", "views": 64718, "comments": 66, "date": "2026-08-02", "account": "own"}, {"title": "Top 10 “ASSIST BETTER THAN GOAL” Moments in Premier League History🏴󠁧󠁢󠁥󠁮󠁧󠁿🔥", "url": "https://www.youtube.com/shorts/4UUGVoyJxiw", "views": 60610, "comments": 36, "date": "2026-08-02", "account": "own"}, {"title": "Top 10 Longest Goals in Premier League History🏴󠁧󠁢󠁥󠁮󠁧󠁿🔥", "url": "https://www.youtube.com/shorts/i9oQCNMUK2Y", "views": 18507, "comments": 11, "date": "2026-08-01", "account": "own"}, {"title": "Top 10 Longest Goals in Premier League History🏴󠁧󠁢󠁥󠁮󠁧󠁿🔥", "url": "https://www.youtube.com/shorts/bJUZLff1s60", "views": 466912, "comments": 148, "date": "2026-08-01", "account": "own"}, {"title": "Top 10 “When Defenders get Bored” Moments in Football⚽️🔥", "url": "https://www.youtube.com/shorts/lNIZLMD7Co8", "views": 93653, "comments": 29, "date": "2026-08-01", "account": "own"}, {"title": "Top 10 When Defenders Get Bored in Football⚽️🔥", "url": "https://www.youtube.com/shorts/BEaaYEfRH8A", "views": 112133, "comments": 70, "date": "2026-07-31", "account": "own"}, {"title": "Top 5 Most Lucky Goals in Football🍀🔥", "url": "https://www.youtube.com/shorts/uWXJ9s-5f3M", "views": 1130677, "comments": 324, "date": "2026-07-31", "account": "own"}, {"title": "Top 5 Worst Goalkeeper Mistakes in Football⚽️🔥", "url": "https://www.youtube.com/shorts/Jtip1l7cPjo", "views": 948688, "comments": 325, "date": "2026-07-31", "account": "own"}, {"title": "Top 5 Ronaldo Selfish Moments in Football", "url": "https://www.youtube.com/shorts/qFUzC1QRn2A", "views": 923000, "comments": 1206, "date": "2026-07-30", "account": "own"}, {"title": "Top 5 Tackles That Deserve Jail Time in Football⚽️🔥", "url": "https://www.youtube.com/shorts/GSIbdo2tx3o", "views": 12991, "comments": 39, "date": "2026-07-30", "account": "own"}, {"title": "Top 5 Last Minute Goals in Football⚽️🔥", "url": "https://www.youtube.com/shorts/pZ3r4tWppck", "views": 64429, "comments": 95, "date": "2026-07-30", "account": "own"}, {"title": "Best Player from Every Shirt Number in Football⚽️🔥", "url": "https://www.youtube.com/shorts/Zhy-uADRof8", "views": 592745, "comments": 517, "date": "2026-07-29", "account": "own"}, {"title": "Top 5 World Cup Goals in Football⚽️🔥", "url": "https://www.youtube.com/shorts/4v0sdHW4q0w", "views": 98290, "comments": 99, "date": "2026-07-29", "account": "own"}, {"title": "Top 5 “Worst” Medical Fails in Football", "url": "https://www.youtube.com/shorts/YuqQ3jD5IgQ", "views": 87947, "comments": 76, "date": "2026-07-29", "account": "own"}, {"title": "Top 5 Ronaldo Aura Moments in Football", "url": "https://www.youtube.com/shorts/OYYvw7HK6e8", "views": 160093, "comments": 274, "date": "2026-07-28", "account": "own"}, {"title": "Top 5 IShowSpeed Charity Match Moments in Football", "url": "https://www.youtube.com/shorts/Ofq4ugcU1Us", "views": 884520, "comments": 159, "date": "2026-07-28", "account": "own"}, {"title": "Top 5 “Craziest” Offside Calls in Football", "url": "https://www.youtube.com/shorts/yhiCHHx1aNc", "views": 1674732, "comments": 684, "date": "2026-07-27", "account": "own"}, {"title": "Top 5 Messi Autism Moments in Football", "url": "https://www.youtube.com/shorts/1_a5J0kVukU", "views": 229410, "comments": 244, "date": "2026-07-27", "account": "own"}, {"title": "Top 5 Ronaldo Crashout Moments", "url": "https://www.youtube.com/shorts/CZNTmoYVgVk", "views": 417727, "comments": 446, "date": "2026-07-27", "account": "own"}, {"title": "Top 5 Reasons Ronaldo is Better Than Messi in Football", "url": "https://www.youtube.com/shorts/_LZQYuWbUxQ", "views": 680788, "comments": 1266, "date": "2026-07-26", "account": "own"}, {"title": "Top 5 Reasons Messi is Better Than Ronaldo in Football", "url": "https://www.youtube.com/shorts/phAtLWCrM60", "views": 121819, "comments": 518, "date": "2026-07-26", "account": "own"}, {"title": "Top 5 Messi “FIFA Boy” Moments in Football", "url": "https://www.youtube.com/shorts/xPS1G4W1NdY", "views": 372386, "comments": 842, "date": "2026-07-26", "account": "own"}, {"title": "Top 5 Times Players Celebrated Alone in Football", "url": "https://www.youtube.com/shorts/-jxslzS--V8", "views": 640138, "comments": 178, "date": "2026-07-25", "account": "own"}, {"title": "Longest Goal Scored With Every Technique in Football", "url": "https://www.youtube.com/shorts/3fPdd6-tBOY", "views": 117837, "comments": 54, "date": "2026-07-25", "account": "own"}, {"title": "Top 5 Players That Of One Goal in Football", "url": "https://www.youtube.com/shorts/O7muPYT99O8", "views": 538023, "comments": 409, "date": "2026-07-25", "account": "own"}, {"title": "Top 5 “Inhuman” Roberto Carlos Goals", "url": "https://www.youtube.com/shorts/HpuNdo3fiEc", "views": 86048, "comments": 59, "date": "2026-07-24", "account": "own"}, {"title": "Top 5 Best Curve Goals in Football⚽️🔥", "url": "https://www.youtube.com/shorts/HmU4owiwtkg", "views": 91789, "comments": 80, "date": "2026-07-24", "account": "own"}, {"title": "Top 10 Defender Goals in Football⚽️🔥", "url": "https://www.youtube.com/shorts/3NI-2h5rfsk", "views": 303306, "comments": 118, "date": "2026-07-24", "account": "own"}, {"title": "Top 10 Defender Goals in Football", "url": "https://www.youtube.com/shorts/QGiYhzilL8Q", "views": 63932, "comments": 58, "date": "2026-07-23", "account": "own"}, {"title": "Top 10 “Smartest” Moments in Football⚽️🔥", "url": "https://www.youtube.com/shorts/LvfO01JWI14", "views": 92103, "comments": 43, "date": "2026-07-23", "account": "own"}, {"title": "Top 5 Most Ridiculous Suarez Goals", "url": "https://www.youtube.com/shorts/6Xm40FAHzj8", "views": 79519, "comments": 66, "date": "2026-07-23", "account": "own"}, {"title": "Top 5 “Emotional” Goals in Football", "url": "https://www.youtube.com/shorts/6klwchT7wfo", "views": 223347, "comments": 86, "date": "2026-07-22", "account": "own"}, {"title": "Top 5 “Humiliating” Skills in Football", "url": "https://www.youtube.com/shorts/qChucz0ajqg", "views": 506468, "comments": 120, "date": "2026-07-22", "account": "own"}, {"title": "Top 10 Bicycle Kicks in Football", "url": "https://www.youtube.com/shorts/3C0PIs-5TQ0", "views": 53100, "comments": 239, "date": "2026-07-22", "account": "own"}, {"title": "Best Goal Scored By Every Shirt Number Part 2", "url": "https://www.youtube.com/shorts/DctaRPHLoMo", "views": 54767, "comments": 49, "date": "2026-07-22", "account": "own"}, {"title": "Best Goal Scored By Every Shirt Number Part 1", "url": "https://www.youtube.com/shorts/KqM2VgKg4Mc", "views": 890202, "comments": 133, "date": "2026-07-21", "account": "own"}, {"title": "Top 5 Best World Cup Squads in Football", "url": "https://www.youtube.com/shorts/MKE1vumTp3k", "views": 90018, "comments": 84, "date": "2026-07-21", "account": "own"}, {"title": "What If The Ballon D’or Was Fair? Part 4", "url": "https://www.youtube.com/shorts/Zetwasu5JQQ", "views": 275115, "comments": 255, "date": "2026-07-21", "account": "own"}, {"title": "What If The Ballon D’or Was Fair?", "url": "https://www.youtube.com/shorts/0LDNhqbXS3g", "views": 411148, "comments": 226, "date": "2026-07-21", "account": "own"}, {"title": "What if The Ballon D’or Was Fair? Part 1", "url": "https://www.youtube.com/shorts/TE9PUSt2GfQ", "views": 91613, "comments": 65, "date": "2026-07-20", "account": "own"}, {"title": "What If The Ballon D’or Was Fair? Part 2", "url": "https://www.youtube.com/shorts/9oavKxKTfV0", "views": 143792, "comments": 333, "date": "2026-07-20", "account": "own"}, {"title": "Top 5 Fan Reactions in Football", "url": "https://www.youtube.com/shorts/mBhpob8Rcek", "views": 457949, "comments": 161, "date": "2026-07-20", "account": "own"}, {"title": "Top 5 “Controversial” World Cup Matches in Football", "url": "https://www.youtube.com/shorts/0XlghbGq4uA", "views": 51369, "comments": 101, "date": "2026-07-20", "account": "own"}, {"title": "Top 5 “Funniest” World Cup Moments in Football", "url": "https://www.youtube.com/shorts/xXF8335CMzU", "views": 192723, "comments": 56, "date": "2026-07-19", "account": "own"}, {"title": "What if the Puskas Award Was Fair? Part 3", "url": "https://www.youtube.com/shorts/Ykm_E4S07uM", "views": 2217215, "comments": 751, "date": "2026-07-19", "account": "own"}, {"title": "Top 5 Players Who Deserve The Oscar Award in Football", "url": "https://www.youtube.com/shorts/uJEw4mhEYW8", "views": 2828592, "comments": 1765, "date": "2026-07-19", "account": "own"}, {"title": "Top 5 Worst Performances in Football History⚽️🔥", "url": "https://www.youtube.com/shorts/xBRE_wKcsDs", "views": 437302, "comments": 97, "date": "2026-07-19", "account": "own"}, {"title": "Top 5 Unforgettable Long Shots in Football", "url": "https://www.youtube.com/shorts/2nktBKr8hWc", "views": 49638, "comments": 53, "date": "2026-07-18", "account": "own"}, {"title": "Top 5 Best Strikers This Season⚽️🔥", "url": "https://www.youtube.com/shorts/Mm0iumu1nko", "views": 191627, "comments": 214, "date": "2026-07-18", "account": "own"}, {"title": "Top 10 Goals that NEVER Won a Puskas Award⚽️🔥", "url": "https://www.youtube.com/shorts/xsdwvZyU9kw", "views": 4025320, "comments": 1802, "date": "2026-07-18", "account": "own"}, {"title": "Top 5 Last Minute Goals in World Cup History", "url": "https://www.youtube.com/shorts/7d3P1Ir8Wc4", "views": 84808, "comments": 130, "date": "2026-07-18", "account": "own"}, {"title": "Top 10 Free Kicks that DONT Make Sense in Football⚽️🔥", "url": "https://www.youtube.com/shorts/JQlgnOOqIU4", "views": 212300, "comments": 42, "date": "2026-07-17", "account": "own"}, {"title": "Top 5 Goalkeeper Tactical Fouls in Football", "url": "https://www.youtube.com/shorts/0xUTtYqaPy0", "views": 157265, "comments": 53, "date": "2026-07-17", "account": "own"}, {"title": "Top 5 Legends Who Forgot How to Play Football", "url": "https://www.youtube.com/shorts/TwczDqK18g8", "views": 335288, "comments": 316, "date": "2026-07-17", "account": "own"}, {"title": "Strangest Penalty From Every World Cup", "url": "https://www.youtube.com/shorts/Cc-ds8Z6Fi0", "views": 142578, "comments": 71, "date": "2026-07-17", "account": "own"}, {"title": "Top 5 Goalkeepers That Went For the Kill", "url": "https://www.youtube.com/shorts/eBAzSw1hN5I", "views": 664069, "comments": 465, "date": "2026-07-16", "account": "own"}, {"title": "Top 10 Free Kicks That Dont Make Sense⚽️🔥", "url": "https://www.youtube.com/shorts/kemGNlZxaHE", "views": 450648, "comments": 174, "date": "2026-07-16", "account": "own"}, {"title": "Top 5 World Cup Players Who Got Abused After Missing Penalty", "url": "https://www.youtube.com/shorts/NfkXBhhEOyc", "views": 418421, "comments": 187, "date": "2026-07-16", "account": "own"}, {"title": "Top 5 “Pace Abusers” Right Now in Football", "url": "https://www.youtube.com/shorts/Eg9v0j5eHCk", "views": 230383, "comments": 86, "date": "2026-07-16", "account": "own"}, {"title": "Top 10 Most Humiliating Goals in Football⚽️🔥", "url": "https://www.youtube.com/shorts/pEFqa1HrKcU", "views": 65159, "comments": 48, "date": "2026-07-15", "account": "own"}, {"title": "Top 5 Worst Own Goals in Premier League History🏴󠁧󠁢󠁥󠁮󠁧󠁿🔥", "url": "https://www.youtube.com/shorts/9ApbtOHk58U", "views": 1899660, "comments": 177, "date": "2026-07-15", "account": "own"}, {"title": "Top 10 Players to NEVER Win a Ballon D’or", "url": "https://www.youtube.com/shorts/jAUaoDisVOI", "views": 2335690, "comments": 4356, "date": "2026-07-15", "account": "own"}, {"title": "Top 5 Dictator Mbappe Moments in Football", "url": "https://www.youtube.com/shorts/yj6nlFzD91Q", "views": 21674, "comments": 8, "date": "2026-07-15", "account": "own"}, {"title": "Top 5 Manager Goals in Football", "url": "https://www.youtube.com/shorts/gTvlML5TUO0", "views": 281757, "comments": 68, "date": "2026-07-14", "account": "own"}, {"title": "Top 5 “DONT SHOOT” Moments in Football", "url": "https://www.youtube.com/shorts/gq54DXlKwgE", "views": 102358, "comments": 51, "date": "2026-07-14", "account": "own"}, {"title": "Best Comeback From Every Year in Football Part 2", "url": "https://www.youtube.com/shorts/HjbDsRPa_vY", "views": 69278, "comments": 59, "date": "2026-07-14", "account": "own"}, {"title": "Top 10 Saves in Football History", "url": "https://www.youtube.com/shorts/xGngDpyrKb0", "views": 52332, "comments": 31, "date": "2026-07-14", "account": "own"}, {"title": "Best Comeback From Every Year in Football Part 1", "url": "https://www.youtube.com/shorts/08C2H1K6i14", "views": 111078, "comments": 56, "date": "2026-07-13", "account": "own"}, {"title": "Top 10 Most Powerful Penalties in Football", "url": "https://www.youtube.com/shorts/NET_u-kAaWw", "views": 86494, "comments": 47, "date": "2026-07-13", "account": "own"}, {"title": "Worst Own Goal From Every Year in Football Part 2", "url": "https://www.youtube.com/shorts/NLi0t_-9TR4", "views": 266718, "comments": 87, "date": "2026-07-13", "account": "own"}, {"title": "Worst Own Goal From Every Year in Football Part 3", "url": "https://www.youtube.com/shorts/uVFww9aIGh4", "views": 34809, "comments": 31, "date": "2026-07-13", "account": "own"}, {"title": "Top 5 Biggest Losses in Football", "url": "https://www.youtube.com/shorts/X6S_zbCmj0E", "views": 515078, "comments": 150, "date": "2026-07-12", "account": "own"}, {"title": "Worst Own Goal From Every Year in Football Part 1", "url": "https://www.youtube.com/shorts/ng1g4ZI07aA", "views": 65328, "comments": 41, "date": "2026-07-12", "account": "own"}, {"title": "Top 5 Cheekiest🍑 Plays in Football", "url": "https://www.youtube.com/shorts/h15soS4204U", "views": 46634, "comments": 41, "date": "2026-07-12", "account": "own"}, {"title": "Top 5 “Sneakiest” Goalkeeper Robberies in Football", "url": "https://www.youtube.com/shorts/EZqxdmZKESs", "views": 1155623, "comments": 403, "date": "2026-07-12", "account": "own"}, {"title": "Top 5 Most Iconic Celebrations in Football", "url": "https://www.youtube.com/shorts/349RK7Ifs7I", "views": 373279, "comments": 79, "date": "2026-07-11", "account": "own"}, {"title": "Top 5 Most “Athletic” Moments in Football", "url": "https://www.youtube.com/shorts/z5vycUXV_lw", "views": 311883, "comments": 71, "date": "2026-07-11", "account": "own"}, {"title": "Top 5 Worst Misses in Football History", "url": "https://www.youtube.com/shorts/4JP7Zoc7AuA", "views": 269523, "comments": 159, "date": "2026-07-11", "account": "own"}, {"title": "Top 5 “Never Give Up” Moments in Football", "url": "https://www.youtube.com/shorts/KXurkDfdEkY", "views": 151666, "comments": 22, "date": "2026-07-11", "account": "own"}, {"title": "Top 10 Best Clasico Goals in Football", "url": "https://www.youtube.com/shorts/zb4wzRKfZqQ", "views": 131101, "comments": 55, "date": "2026-07-10", "account": "own"}, {"title": "Top 5 “Scariest” Moments in Football", "url": "https://www.youtube.com/shorts/La0FVd_YAMw", "views": 5549, "comments": 10, "date": "2026-07-10", "account": "own"}, {"title": "Top 10 “Pace Abuser” Moments in Football", "url": "https://www.youtube.com/shorts/jxz2A7GHTGM", "views": 5358170, "comments": 632, "date": "2026-07-10", "account": "own"}, {"title": "Top 5 “Unnecessary” Top Bins in Football", "url": "https://www.youtube.com/shorts/P-aSdi6wBss", "views": 319453, "comments": 88, "date": "2026-07-10", "account": "own"}, {"title": "Top 5 Best Debut Goals in Football", "url": "https://www.youtube.com/shorts/v2AqIIBCS4U", "views": 362070, "comments": 73, "date": "2026-07-09", "account": "own"}, {"title": "Top 5 Penalty Mindgames That ACTUALLY Worked", "url": "https://www.youtube.com/shorts/JGuxH7DMUzg", "views": 275763, "comments": 79, "date": "2026-07-09", "account": "own"}, {"title": "Top 5 “Dumbest” Defending Moments", "url": "https://www.youtube.com/shorts/r7JjgIBgSAU", "views": 67053, "comments": 57, "date": "2026-07-09", "account": "own"}, {"title": "Top 5 “Laser” Moments in Football", "url": "https://www.youtube.com/shorts/Cto5dgCQfdM", "views": 104856, "comments": 39, "date": "2026-07-09", "account": "own"}, {"title": "Top 7 Most Powerful Goals in Football", "url": "https://www.youtube.com/shorts/vCu3HaQWa4U", "views": 1142257, "comments": 229, "date": "2026-07-08", "account": "own"}, {"title": "Top 5 Best Passes in Football", "url": "https://www.youtube.com/shorts/GwYbNCILXnY", "views": 216613, "comments": 107, "date": "2026-07-08", "account": "own"}, {"title": "Top 5 Impossible Ways to Stop a Goal in Football", "url": "https://www.youtube.com/shorts/tHitPppQ-Mw", "views": 2011667, "comments": 307, "date": "2026-07-08", "account": "own"}, {"title": "Top 5 Goalkeeper Red Cards in Football", "url": "https://www.youtube.com/shorts/1aaf5BjaVns", "views": 73123, "comments": 51, "date": "2026-07-07", "account": "own"}, {"title": "Top 5 Worst Penalties in Football", "url": "https://www.youtube.com/shorts/onKNJB_oQAc", "views": 224125, "comments": 67, "date": "2026-07-07", "account": "own"}, {"title": "Top 5 “Aura Goals” in Football", "url": "https://www.youtube.com/shorts/bSTDnWSVLAE", "views": 6863236, "comments": 512, "date": "2026-07-07", "account": "own"}, {"title": "Top 5 Messi Goals for Inter Miami", "url": "https://www.youtube.com/shorts/BDMKxU9XGTI", "views": 92276, "comments": 39, "date": "2026-07-07", "account": "own"}, {"title": "Top 5 “Tiki Taka” Goals in Football", "url": "https://www.youtube.com/shorts/8pRmEGw9ALc", "views": 9317, "comments": 10, "date": "2026-07-06", "account": "own"}, {"title": "Top 5 Volley Goals That Make No Sense in Football", "url": "https://www.youtube.com/shorts/kXWBDI7NOVE", "views": 21444, "comments": 34, "date": "2026-07-06", "account": "own"}, {"title": "Top 5 “Unexpected” Goals in Football", "url": "https://www.youtube.com/shorts/R0TFlHeqe4M", "views": 58775, "comments": 17, "date": "2026-07-06", "account": "own"}, {"title": "Top 5 World Cup Free Kick Goals in Football History", "url": "https://www.youtube.com/shorts/HwLpI5-Msic", "views": 31469, "comments": 41, "date": "2026-07-06", "account": "own"}, {"title": "Top 5 Most “Disrepectful” Penalties in Football", "url": "https://www.youtube.com/shorts/ZlL-aAdWKFg", "views": 140245, "comments": 53, "date": "2026-07-05", "account": "own"}, {"title": "Top 5 Worst Panenka Misses in Football", "url": "https://www.youtube.com/shorts/ZVB7_nV6Dl4", "views": 35593, "comments": 36, "date": "2026-07-05", "account": "own"}, {"title": "Top 5 Legendary World Cup Longshots in Football", "url": "https://www.youtube.com/shorts/9bOf2KUQZfA", "views": 29577, "comments": 49, "date": "2026-07-05", "account": "own"}, {"title": "Top 5 “Dramatic” Last Minute Goals in Football", "url": "https://www.youtube.com/shorts/wrl83rX4xH0", "views": 32186, "comments": 23, "date": "2026-07-05", "account": "own"}, {"title": "Top 5 Penalties That Broke Millions of Hearts", "url": "https://www.youtube.com/shorts/E6kZ3BzgTgU", "views": 570876, "comments": 202, "date": "2026-07-04", "account": "own"}, {"title": "Top 5 Times Players Copied Their Idols Goals in Football", "url": "https://www.youtube.com/shorts/WwColBLS1Zo", "views": 101917, "comments": 93, "date": "2026-07-04", "account": "own"}, {"title": "Top 5 “Legendary” World Cup Goals in Football History", "url": "https://www.youtube.com/shorts/rKTZCksEWvg", "views": 27210, "comments": 18, "date": "2026-07-04", "account": "own"}, {"title": "Top 5 Mbappe Goals in Football", "url": "https://www.youtube.com/shorts/9H7tZPRde6k", "views": 70503, "comments": 42, "date": "2026-07-03", "account": "own"}, {"title": "Top 5 Valverde Powershots in Football", "url": "https://www.youtube.com/shorts/v8BStg6MBaQ", "views": 52280, "comments": 28, "date": "2026-07-03", "account": "own"}, {"title": "Top 5 EFL Championship Goals in Football🏴󠁧󠁢󠁥󠁮󠁧󠁿🔥", "url": "https://www.youtube.com/shorts/6YeAhcCplKM", "views": 40110, "comments": 16, "date": "2026-07-03", "account": "own"}, {"title": "Top 5 Most Ridiculous Rooney Shots But They Go In", "url": "https://www.youtube.com/shorts/6QmQ4hUkzfY", "views": 35188, "comments": 34, "date": "2026-07-03", "account": "own"}, {"title": "Top 5 “Why Would Shoot That Shots”", "url": "https://www.youtube.com/shorts/3L5wOsUdxKM", "views": 4431940, "comments": 913, "date": "2026-07-03", "account": "own"}, {"title": "Top 5 Greatest Assists in Football", "url": "https://www.youtube.com/shorts/3cDBXwK1l8o", "views": 112441, "comments": 71, "date": "2026-07-02", "account": "own"}, {"title": "Top 5 Lamine Yamal Goals", "url": "https://www.youtube.com/shorts/OFBDiy4jphE", "views": 56506, "comments": 43, "date": "2026-07-02", "account": "own"}, {"title": "The Best Save from Every Year in Football", "url": "https://www.youtube.com/shorts/MQc2B5E_le8", "views": 10799, "comments": 12, "date": "2026-07-02", "account": "own"}, {"title": "The Best Save from Every Year in Football", "url": "https://www.youtube.com/shorts/F_1wdlpDQqY", "views": 4485970, "comments": 514, "date": "2026-07-02", "account": "own"}, {"title": "Top 5 Ronaldo Bluetooth Moments in Football", "url": "https://www.youtube.com/shorts/VTBN0a8T_Sk", "views": 855842, "comments": 860, "date": "2026-07-02", "account": "own"}, {"title": "Top 5 Fake Shots in Football Part 2", "url": "https://www.youtube.com/shorts/DZiP1Q9wprI", "views": 26708, "comments": 25, "date": "2026-07-01", "account": "own"}, {"title": "Top 5 No Net Goals in Football", "url": "https://www.youtube.com/shorts/-Z_aHLUgJZU", "views": 289593, "comments": 31, "date": "2026-07-01", "account": "own"}, {"title": "Top 5 World Cup Goals So Far In Football", "url": "https://www.youtube.com/shorts/PpAlW-SHuv4", "views": 35277, "comments": 87, "date": "2026-07-01", "account": "own"}, {"title": "What if The Puskas Award Was Fair in Football? Part 1", "url": "https://www.youtube.com/shorts/wX3h1NVzuF0", "views": 72808, "comments": 47, "date": "2026-07-01", "account": "own"}, {"title": "What if the Puskas Award Was Fair? Part 2", "url": "https://www.youtube.com/shorts/_BJk6f30ShA", "views": 2317837, "comments": 1211, "date": "2026-07-01", "account": "own"}, {"title": "Top 5 Best First Touches Before Scoring in Football", "url": "https://www.youtube.com/shorts/EftRjceH0kA", "views": 77021, "comments": 43, "date": "2026-06-30", "account": "own"}, {"title": "Top 5 Impossible Penalty Saves", "url": "https://www.youtube.com/shorts/_G97VjDasZA", "views": 53603, "comments": 34, "date": "2026-06-30", "account": "own"}, {"title": "Top 5 Most Unsavable Free Kicks in Football", "url": "https://www.youtube.com/shorts/GTRnaRVMrx0", "views": 58204, "comments": 58, "date": "2026-06-30", "account": "own"}, {"title": "Top 5 “Longest” Assists in Football", "url": "https://www.youtube.com/shorts/PqZyQ2U5Wg0", "views": 26950, "comments": 14, "date": "2026-06-30", "account": "own"}, {"title": "Top 5 “Smartest” Offside Plays in Football", "url": "https://www.youtube.com/shorts/hxMFo5HHKuk", "views": 14523, "comments": 8, "date": "2026-06-30", "account": "own"}, {"title": "Top 5 Goal Line Clearances in Football", "url": "https://www.youtube.com/shorts/3BIKY1pohEM", "views": 30373, "comments": 57, "date": "2026-06-29", "account": "own"}, {"title": "Top 5 Worst Hattricks in Football History Part 2", "url": "https://www.youtube.com/shorts/144WMskMCi8", "views": 42113, "comments": 26, "date": "2026-06-29", "account": "own"}, {"title": "Top 5 Zero Aura Defense Moments in Football", "url": "https://www.youtube.com/shorts/kV5sk114EAY", "views": 39936, "comments": 20, "date": "2026-06-29", "account": "own"}, {"title": "Top 5 Slowest Penalties in Football", "url": "https://www.youtube.com/shorts/Pspi1HtiWEU", "views": 539897, "comments": 76, "date": "2026-06-29", "account": "own"}, {"title": "Top 5 “Inhuman” Moments in Football", "url": "https://www.youtube.com/shorts/8ITErVeMp6o", "views": 16743, "comments": 24, "date": "2026-06-29", "account": "own"}, {"title": "Top 5 Gerrard Powershots in Football", "url": "https://www.youtube.com/shorts/YWVPdhjEUqg", "views": 27004, "comments": 29, "date": "2026-06-28", "account": "own"}, {"title": "Top 5 Greatest Wonderkids in Football", "url": "https://www.youtube.com/shorts/EPCq2s85Q5Q", "views": 36804, "comments": 117, "date": "2026-06-28", "account": "own"}, {"title": "Top 5 Most “Unforgettable” Goals in Football", "url": "https://www.youtube.com/shorts/Z7sBVqdJcMo", "views": 28015, "comments": 43, "date": "2026-06-28", "account": "own"}, {"title": "Worst Penalty Miss With Every Technique in Football", "url": "https://www.youtube.com/shorts/hxBxS7QX354", "views": 2208030, "comments": 391, "date": "2026-06-28", "account": "own"}, {"title": "Top 5 “Smartest” Corner Kicks in Football", "url": "https://www.youtube.com/shorts/LtQwn90QaLw", "views": 30231, "comments": 26, "date": "2026-06-28", "account": "own"}, {"title": "Top 5 Best Premier League Goals So Far This Season", "url": "https://www.youtube.com/shorts/4DbE6v7uFa4", "views": 24873, "comments": 53, "date": "2026-06-27", "account": "own"}, {"title": "Top 5 Saka Goals vs Top 5 Palmer Goals", "url": "https://www.youtube.com/shorts/EI6767VMzW4", "views": 58611, "comments": 94, "date": "2026-06-27", "account": "own"}, {"title": "Top 5 Carrer Comebacks in Football History", "url": "https://www.youtube.com/shorts/odKC95EQ4WY", "views": 1070000, "comments": 251, "date": "2026-06-27", "account": "own"}, {"title": "Top 5 “Players vs Trophy” Moments in Football", "url": "https://www.youtube.com/shorts/_xUiHQT-pDE", "views": 342481, "comments": 22, "date": "2026-06-27", "account": "own"}, {"title": "Top 5 Goalkeeper Goals in Football", "url": "https://www.youtube.com/shorts/m_ye2cYulD0", "views": 168710, "comments": 79, "date": "2026-06-26", "account": "own"}, {"title": "Top 5 Strangest Ways to Celebrate in Football", "url": "https://www.youtube.com/shorts/sw6dSAeXuSA", "views": 220252, "comments": 385, "date": "2026-06-26", "account": "own"}, {"title": "Top 5 Trivela Goals in Football", "url": "https://www.youtube.com/shorts/h_WFjXj-9ak", "views": 25730, "comments": 22, "date": "2026-06-26", "account": "own"}, {"title": "Top 5 Times Players Sacrificed For Their Team", "url": "https://www.youtube.com/shorts/rwlcE1ciCW0", "views": 29503, "comments": 14, "date": "2026-06-26", "account": "own"}, {"title": "Top 10 Best Nutmegs in Football", "url": "https://www.youtube.com/shorts/iDfYLQ1Ga4k", "views": 397410, "comments": 256, "date": "2026-06-26", "account": "own"}, {"title": "Best Save From Every World Cup in Football", "url": "https://www.youtube.com/shorts/u6ECJKdjbKI", "views": 58618, "comments": 31, "date": "2026-06-25", "account": "own"}, {"title": "Top 5 200IQ Free Kicks in Football", "url": "https://www.youtube.com/shorts/fIpUV36VzcQ", "views": 12384, "comments": 14, "date": "2026-06-25", "account": "own"}, {"title": "Top 3 Players Who Have No Haters in Football", "url": "https://www.youtube.com/shorts/VoHgY5egqiQ", "views": 39837, "comments": 45, "date": "2026-06-25", "account": "own"}, {"title": "Top 5 Fake Shots in Football", "url": "https://www.youtube.com/shorts/Te87b6dv7Pg", "views": 40672, "comments": 25, "date": "2026-06-25", "account": "own"}, {"title": "Top 3 Scores That Look Fake But are 100% Real", "url": "https://www.youtube.com/shorts/-PRR5BQxon4", "views": 366261, "comments": 118, "date": "2026-06-25", "account": "own"}, {"title": "Top 5 Puskas Misses in Football", "url": "https://www.youtube.com/shorts/aZHVGZbW-HA", "views": 164701, "comments": 110, "date": "2026-06-24", "account": "own"}, {"title": "Top 5 Goals That Should’ve Won 2018 Puskas", "url": "https://www.youtube.com/shorts/v8S_RDGjoBo", "views": 80185, "comments": 38, "date": "2026-06-24", "account": "own"}, {"title": "Top 5 Worst Goalkeeper Mistakes in Football", "url": "https://www.youtube.com/shorts/XkAMDaqRPrg", "views": 50098, "comments": 51, "date": "2026-06-24", "account": "own"}, {"title": "Top 5 Impossible Angle Goals in Football", "url": "https://www.youtube.com/shorts/AvbSpaN8D28", "views": 9045, "comments": 20, "date": "2026-06-24", "account": "own"}, {"title": "Top 5 Panenka Penalties in Football", "url": "https://www.youtube.com/shorts/O3S-aPKwdNM", "views": 34770, "comments": 29, "date": "2026-06-24", "account": "own"}, {"title": "Top 10 Puskas 2026 Goals So Far This Season", "url": "https://www.youtube.com/shorts/KUPyrtcDOKw", "views": 31739, "comments": 40, "date": "2026-06-23", "account": "own"}, {"title": "Top 10 Puskas 2026 Goals So Far This Season Part 2", "url": "https://www.youtube.com/shorts/rZjLoTgCU5w", "views": 53157, "comments": 53, "date": "2026-06-23", "account": "own"}, {"title": "Top 5 Shortest Lived Primes in Football", "url": "https://www.youtube.com/shorts/9aYJ3lBf7HY", "views": 1950540, "comments": 2221, "date": "2026-06-23", "account": "own"}, {"title": "Top 5 Goals Only Messi Can Score in Football", "url": "https://www.youtube.com/shorts/ojAoi2RI03s", "views": 22289, "comments": 66, "date": "2026-06-23", "account": "own"}, {"title": "Top 5 Triple Saves in Football", "url": "https://www.youtube.com/shorts/Nt_hvkrJp50", "views": 24038, "comments": 16, "date": "2026-06-23", "account": "own"}, {"title": "Top 5 Maguire Goals in Football", "url": "https://www.youtube.com/shorts/pidP_gAwJQ4", "views": 44084, "comments": 32, "date": "2026-06-22", "account": "own"}, {"title": "Top 10 Curve Goals in Football", "url": "https://www.youtube.com/shorts/F9oMUd-YJn4", "views": 85606, "comments": 27, "date": "2026-06-22", "account": "own"}, {"title": "PART 2 | Top 10 Curve Goals in Football", "url": "https://www.youtube.com/shorts/ym2jzWq-aXQ", "views": 38114, "comments": 41, "date": "2026-06-22", "account": "own"}, {"title": "Top 3 Players Who Used to Be Stars But FELL OFF", "url": "https://www.youtube.com/shorts/ibdIkzgQ2g0", "views": 53906, "comments": 26, "date": "2026-06-22", "account": "own"}, {"title": "Top 5 Bench Reactions in Football History", "url": "https://www.youtube.com/shorts/Az3n0Sdz0Io", "views": 127604, "comments": 46, "date": "2026-06-22", "account": "own"}, {"title": "Top 5 Vini vs Neymar Goals (Head to Head)", "url": "https://www.youtube.com/shorts/Mu_i8L4lvvQ", "views": 40368, "comments": 78, "date": "2026-06-21", "account": "own"}, {"title": "Top 3 Replacement Managers Who Did Better", "url": "https://www.youtube.com/shorts/6GPu-n311Ik", "views": 20913, "comments": 27, "date": "2026-06-21", "account": "own"}, {"title": "Top 5 Mbappe vs Haaland Goals in Football", "url": "https://www.youtube.com/shorts/MnIIPIp-z3k", "views": 11588, "comments": 33, "date": "2026-06-21", "account": "own"}, {"title": "Top 3 Players Who Got WORSE After Joining a New Team", "url": "https://www.youtube.com/shorts/XVjmtUZIUm4", "views": 260312, "comments": 69, "date": "2026-06-21", "account": "own"}, {"title": "Top 3 Worst Performances in Football Part 1", "url": "https://www.youtube.com/shorts/w97v8fn1XVQ", "views": 257206, "comments": 84, "date": "2026-06-21", "account": "own"}, {"title": "Top 3 Worst Performances in Football 2", "url": "https://www.youtube.com/shorts/tFWrS7alesQ", "views": 42942, "comments": 48, "date": "2026-06-20", "account": "own"}, {"title": "Top 3 Worst Performances in Football Part 3", "url": "https://www.youtube.com/shorts/3v_I1fGWwrw", "views": 50933, "comments": 28, "date": "2026-06-20", "account": "own"}, {"title": "Top 3 Replacement Managers Who Did Better", "url": "https://www.youtube.com/shorts/oaepZm5-YtY", "views": 43053, "comments": 19, "date": "2026-06-20", "account": "own"}, {"title": "Top 3 Unexpected Teams Who Almost Won a Champions League", "url": "https://www.youtube.com/shorts/slbraVwHRMQ", "views": 378110, "comments": 184, "date": "2026-06-20", "account": "own"}, {"title": "Top 5 Most “Nonchalant” Celebrations in Football", "url": "https://www.youtube.com/shorts/Y8M4Ru1rpgI", "views": 46097, "comments": 27, "date": "2026-06-19", "account": "own"}, {"title": "Top 3 Worst Robberies in Football", "url": "https://www.youtube.com/shorts/CEIDsNN3t3E", "views": 411319, "comments": 530, "date": "2026-06-19", "account": "own"}, {"title": "Top 5 Worst Hattricks in Football", "url": "https://www.youtube.com/shorts/K1jCdkLRXQU", "views": 39848, "comments": 27, "date": "2026-06-19", "account": "own"}, {"title": "Top 5 Best Ronaldo Hattricks in Football", "url": "https://www.youtube.com/shorts/tNqgdpvzo1w", "views": 58826, "comments": 45, "date": "2026-06-19", "account": "own"}, {"title": "Top 5 Worst Shots in Football", "url": "https://www.youtube.com/shorts/mvfAdHlaSjo", "views": 24095, "comments": 43, "date": "2026-06-18", "account": "own"}, {"title": "Top 5 Best Man United Goals in Football", "url": "https://www.youtube.com/shorts/gVjFdWFiKb0", "views": 7654, "comments": 7, "date": "2026-06-18", "account": "own"}, {"title": "Top 5 Strangest Ways to Score Penalty in Football", "url": "https://www.youtube.com/shorts/AMV7Nu1y3eE", "views": 671066, "comments": 81, "date": "2026-06-18", "account": "own"}, {"title": "Top 5 “Smartest” Defending Moments in Football", "url": "https://www.youtube.com/shorts/evCG91J-Iyg", "views": 368496, "comments": 46, "date": "2026-06-18", "account": "own"}, {"title": "Top 5 Most “Selfish” Moments in Football", "url": "https://www.youtube.com/shorts/9UlTiyixsSU", "views": 1952704, "comments": 812, "date": "2026-06-17", "account": "own"}, {"title": "Top 5 “Cringiest” Moments in Football", "url": "https://www.youtube.com/shorts/GMaqbx6wK-g", "views": 1508735, "comments": 617, "date": "2026-06-17", "account": "own"}, {"title": "Top 5 Most “Disrepectful” Goals in Football", "url": "https://www.youtube.com/shorts/P-lqyuUW4Ek", "views": 60408, "comments": 35, "date": "2026-06-17", "account": "own"}, {"title": "Top 5 “Revenge” Moments in Football", "url": "https://www.youtube.com/shorts/aNzCrcn7C0Y", "views": 77823, "comments": 34, "date": "2026-06-17", "account": "own"}, {"title": "Top 5 Impossible Ways to Pass in Football", "url": "https://www.youtube.com/shorts/DtG3xYqRU4A", "views": 72900, "comments": 25, "date": "2026-06-17", "account": "own"}, {"title": "Top 5 Times Outfield Players Went in Goal in Football", "url": "https://www.youtube.com/shorts/tIK7FzRKpuA", "views": 80716, "comments": 31, "date": "2026-06-16", "account": "own"}, {"title": "Top 5 “Scariest” Moments in Football", "url": "https://www.youtube.com/shorts/kDuNJTjJsK0", "views": 2452, "comments": 6, "date": "2026-06-16", "account": "own"}, {"title": "5 Players Under Most Pressure to Perform at World Cup", "url": "https://www.youtube.com/shorts/NUfi6lZMEUk", "views": 16416, "comments": 30, "date": "2026-06-16", "account": "own"}, {"title": "Top 5 Fastest Goals in Football", "url": "https://www.youtube.com/shorts/Gvtf1zLjHqE", "views": 9465, "comments": 13, "date": "2026-06-16", "account": "own"}, {"title": "Top 5 Best Mourninho Moments in Football", "url": "https://www.youtube.com/shorts/j7jAJwP5X1k", "views": 30144, "comments": 9, "date": "2026-06-16", "account": "own"}, {"title": "Top 5 Shameless Tactical Fouls in Football", "url": "https://www.youtube.com/shorts/pPfTF25eZ0w", "views": 109603, "comments": 56, "date": "2026-06-15", "account": "own"}, {"title": "Top 5 Vardy Goals in Football", "url": "https://www.youtube.com/shorts/Zd9lr_9oUhI", "views": 20746, "comments": 28, "date": "2026-06-15", "account": "own"}, {"title": "Top 5 Best Ankle Breakers in Football", "url": "https://www.youtube.com/shorts/PAwEIzSAP-0", "views": 28860, "comments": 38, "date": "2026-06-15", "account": "own"}, {"title": "Top 5 “Cleanest” Tackles in Football", "url": "https://www.youtube.com/shorts/vcCnueNYszk", "views": 26188, "comments": 13, "date": "2026-06-15", "account": "own"}, {"title": "Top 5 Champions League Goals This Season", "url": "https://www.youtube.com/shorts/BPjJoMlb3jM", "views": 18876, "comments": 29, "date": "2026-06-15", "account": "own"}, {"title": "Top 5 Best Free Kick Takers of All Time", "url": "https://www.youtube.com/shorts/f_v8g8k-9Pg", "views": 50603, "comments": 99, "date": "2026-06-14", "account": "own"}, {"title": "Top 5 Ronaldo Clips That Would Make You Think He’s Trash", "url": "https://www.youtube.com/shorts/Y7mp5FfL66k", "views": 42169, "comments": 105, "date": "2026-06-14", "account": "own"}, {"title": "Top 5 Highest Paid Players Pee Goal in Football", "url": "https://www.youtube.com/shorts/Szk4hkNuNEo", "views": 17766, "comments": 13, "date": "2026-06-14", "account": "own"}, {"title": "Top 5 “Dumbest” Red Cards in Football", "url": "https://www.youtube.com/shorts/X6gmPiS3pqU", "views": 1180952, "comments": 191, "date": "2026-06-14", "account": "own"}, {"title": "Top 5 “Crashout” Moments in Football", "url": "https://www.youtube.com/shorts/mUnOBuycLJg", "views": 335471, "comments": 205, "date": "2026-06-14", "account": "own"}, {"title": "Top 5 Most Viewed Matches in Football", "url": "https://www.youtube.com/shorts/PWCUrf0SvCQ", "views": 127956, "comments": 65, "date": "2026-06-13", "account": "own"}, {"title": "Top 5 Times Players Celebrate Before Scoring", "url": "https://www.youtube.com/shorts/bNDSkDbKYtA", "views": 24755, "comments": 10, "date": "2026-06-13", "account": "own"}, {"title": "Van Dijk Aura Defending Moments in Football", "url": "https://www.youtube.com/shorts/w0QUk9HPiSo", "views": 41631, "comments": 25, "date": "2026-06-13", "account": "own"}, {"title": "Top 5 Best Hattricks of All Time", "url": "https://www.youtube.com/shorts/o327W4JZkFw", "views": 23426, "comments": 57, "date": "2026-06-13", "account": "own"}, {"title": "Top 5 67🤷‍♂️ Moments in Football", "url": "https://www.youtube.com/shorts/B0DzAeMGaXE", "views": 18875, "comments": 21, "date": "2026-06-13", "account": "own"}, {"title": "Top 5 Best G/A Seasons Of All Time", "url": "https://www.youtube.com/shorts/P1VdNBjcYeQ", "views": 36900, "comments": 31, "date": "2026-06-12", "account": "own"}, {"title": "Top 5 Biggest “What Ifs” In Football", "url": "https://www.youtube.com/shorts/Lx9gIlTcAZA", "views": 97715, "comments": 171, "date": "2026-06-12", "account": "own"}, {"title": "Worst Signing from Every Year in Football Part 1", "url": "https://www.youtube.com/shorts/3AEfj5aKXSg", "views": 122941, "comments": 64, "date": "2026-06-12", "account": "own"}, {"title": "Worst Signing From Every Year in Football Part 2", "url": "https://www.youtube.com/shorts/gWKvj64iHDo", "views": 132197, "comments": 87, "date": "2026-06-12", "account": "own"}, {"title": "“Die for the Badge” Moments From Every Year in Football Part 3", "url": "https://www.youtube.com/shorts/uz5pn3o-UjI", "views": 121429, "comments": 40, "date": "2026-06-12", "account": "own"}, {"title": "“Die for the Badge” Moments From Every Year Part 2", "url": "https://www.youtube.com/shorts/5pKgddZgH5Y", "views": 38291, "comments": 25, "date": "2026-06-11", "account": "own"}, {"title": "“Die for The Badge” Moments From Every Year Part 1", "url": "https://www.youtube.com/shorts/eGir4NKhLZc", "views": 58361, "comments": 32, "date": "2026-06-11", "account": "own"}, {"title": "Best Breakout Star From Every World Cup Part 1", "url": "https://www.youtube.com/shorts/U6tYwPKws1k", "views": 621453, "comments": 116, "date": "2026-06-11", "account": "own"}, {"title": "Most Dominant Club From Every Year Part 1", "url": "https://www.youtube.com/shorts/7W-xSdWxZzo", "views": 24053, "comments": 20, "date": "2026-06-11", "account": "own"}, {"title": "Best Breakout Star From Every World Cup In Football Part 2", "url": "https://www.youtube.com/shorts/I7oGuK-HBXU", "views": 25012, "comments": 22, "date": "2026-06-11", "account": "own"}, {"title": "Top 5 “Embarrassing” Mistakes in Football", "url": "https://www.youtube.com/shorts/senLqnlM0ro", "views": 82549, "comments": 49, "date": "2026-06-10", "account": "own"}, {"title": "Most Dominant Club From Every Year in Football Part 2", "url": "https://www.youtube.com/shorts/GCiwGtg3U4Q", "views": 32726, "comments": 20, "date": "2026-06-10", "account": "own"}, {"title": "Top 5 “Worst” Footballer Presentations", "url": "https://www.youtube.com/shorts/CBtmp_Nxx7A", "views": 188145, "comments": 51, "date": "2026-06-10", "account": "own"}, {"title": "Most Dominant Club From Every Year Part 3", "url": "https://www.youtube.com/shorts/tYunEasFddM", "views": 44687, "comments": 21, "date": "2026-06-10", "account": "own"}, {"title": "Players The Stret Will Never Forget in Football", "url": "https://www.youtube.com/shorts/eL31bWfRWsc", "views": 34733, "comments": 16, "date": "2026-06-10", "account": "own"}, {"title": "Most Dominant Club From Every Year Part 4", "url": "https://www.youtube.com/shorts/SeCH42TRSGo", "views": 32320, "comments": 23, "date": "2026-06-09", "account": "own"}, {"title": "Top 5 “Embarrassing” Penalties in Football", "url": "https://www.youtube.com/shorts/eryXjXw35uQ", "views": 244520, "comments": 91, "date": "2026-06-09", "account": "own"}, {"title": "Most Dominant Club From Every Year Part 5", "url": "https://www.youtube.com/shorts/vRXOI6ohqdk", "views": 105589, "comments": 53, "date": "2026-06-09", "account": "own"}, {"title": "Top 5 Players to Win the Ballon D’or This Season", "url": "https://www.youtube.com/shorts/YPsGLiCr-Ic", "views": 396773, "comments": 216, "date": "2026-06-09", "account": "own"}, {"title": "Top 5 “Post-Rebound” Goals in Football", "url": "https://www.youtube.com/shorts/3dKxuYHFq1Y", "views": 26860, "comments": 19, "date": "2026-06-09", "account": "own"}, {"title": "Top 5 0 IQ Handballs in Football", "url": "https://www.youtube.com/shorts/f4JcywcF7G0", "views": 100381, "comments": 58, "date": "2026-06-08", "account": "own"}, {"title": "Top 5 2022 World Cup Humiliations in Football", "url": "https://www.youtube.com/shorts/KnYLhvPiPSA", "views": 89192, "comments": 52, "date": "2026-06-08", "account": "own"}, {"title": "Top 5 Times Animals Came on The Football Pitch", "url": "https://www.youtube.com/shorts/plAgh6UTusU", "views": 224928, "comments": 47, "date": "2026-06-08", "account": "own"}, {"title": "Top 5 “Smartest” Free Kicks in Football", "url": "https://www.youtube.com/shorts/XHLRjCBAy2I", "views": 33412, "comments": 13, "date": "2026-06-08", "account": "own"}, {"title": "Top 5 Times Goalkeepers Saved Their Country", "url": "https://www.youtube.com/shorts/XnpLsChC0wo", "views": 179051, "comments": 48, "date": "2026-06-08", "account": "own"}, {"title": "Top 5 “Strangest” Moments in Premier League", "url": "https://www.youtube.com/shorts/YWSOZxWC9Xg", "views": 248863, "comments": 55, "date": "2026-06-07", "account": "own"}, {"title": "Top 5 Impossible Ways to Save in Football", "url": "https://www.youtube.com/shorts/nUvDFBLqD4Q", "views": 25174, "comments": 24, "date": "2026-06-07", "account": "own"}, {"title": "Best Free Kick Goal From Every Year in Football Part 2", "url": "https://www.youtube.com/shorts/zP1ZVBNt7aI", "views": 41002, "comments": 36, "date": "2026-06-07", "account": "own"}, {"title": "Top 5 Times Players Destroyed Goalkeepers in Football", "url": "https://www.youtube.com/shorts/4kWZbPcWCeE", "views": 54675, "comments": 29, "date": "2026-06-07", "account": "own"}, {"title": "Worst Dive From Every World Cup", "url": "https://www.youtube.com/shorts/Eft7all7_XY", "views": 63224, "comments": 61, "date": "2026-06-06", "account": "own"}, {"title": "Best From Kick Goal From Every Year Part 1", "url": "https://www.youtube.com/shorts/q7NMCFvmkvA", "views": 42572, "comments": 19, "date": "2026-06-06", "account": "own"}, {"title": "Top 5 GK Recovery Saves in Football", "url": "https://www.youtube.com/shorts/_cCZzOUzLwQ", "views": 28636, "comments": 11, "date": "2026-06-06", "account": "own"}, {"title": "Top 5 Times The Assist Was Better Than the Goal", "url": "https://www.youtube.com/shorts/ma8SXllEgJk", "views": 117035, "comments": 123, "date": "2026-06-06", "account": "own"}, {"title": "Top 5 “Luckiest” Goals in Football", "url": "https://www.youtube.com/shorts/cT26IUu1Yxw", "views": 115358, "comments": 56, "date": "2026-06-06", "account": "own"}, {"title": "Best Player From Every Position in Football Part 1", "url": "https://www.youtube.com/shorts/I0-mKt1P9o4", "views": 30422, "comments": 75, "date": "2026-06-05", "account": "own"}, {"title": "Best Player From Every Position in Football Part 2", "url": "https://www.youtube.com/shorts/Gn_-VUg-5Q4", "views": 25220, "comments": 52, "date": "2026-06-05", "account": "own"}, {"title": "Best Player From Every Position In Football Part 3", "url": "https://www.youtube.com/shorts/zsj5jcwSJGQ", "views": 20511, "comments": 62, "date": "2026-06-05", "account": "own"}, {"title": "What If Players NEVER Missed a Shot?", "url": "https://www.youtube.com/shorts/fN1lAnmQSnI", "views": 877157, "comments": 138, "date": "2026-06-05", "account": "own"}, {"title": "Top 5 Ball Control Moments That Should be Studied", "url": "https://www.youtube.com/shorts/ge9IXNQAl9s", "views": 30134, "comments": 36, "date": "2026-06-04", "account": "own"}, {"title": "Top 5 “Identical” Moments in Football", "url": "https://www.youtube.com/shorts/GM6K5EOZrqU", "views": 156144, "comments": 50, "date": "2026-06-04", "account": "own"}, {"title": "Best Celebration From Every World Cup in Football", "url": "https://www.youtube.com/shorts/RtGfsjZEmBE", "views": 75445, "comments": 46, "date": "2026-06-04", "account": "own"}, {"title": "Top 5 Craziest Bluetooth Tackles in Football", "url": "https://www.youtube.com/shorts/Kga--irDT-o", "views": 206896, "comments": 221, "date": "2026-06-04", "account": "own"}, {"title": "Worst Miss From Every World Cup in Football", "url": "https://www.youtube.com/shorts/zV0oK1Ryjc8", "views": 52537, "comments": 24, "date": "2026-06-04", "account": "own"}, {"title": "Top 5 Times Defenders Became Goalkeeepers in Football", "url": "https://www.youtube.com/shorts/V-2HEzjwAEE", "views": 430963, "comments": 89, "date": "2026-06-03", "account": "own"}, {"title": "Top 5 Most “Clutch” Moments in Football", "url": "https://www.youtube.com/shorts/bwG4nClpj5A", "views": 50794, "comments": 75, "date": "2026-06-03", "account": "own"}, {"title": "Top 5 Jurgen Klopp Moments in Football", "url": "https://www.youtube.com/shorts/eUjrOEJNxe4", "views": 63317, "comments": 26, "date": "2026-06-03", "account": "own"}, {"title": "Top Smartest Goalkeeper Moments in Football", "url": "https://www.youtube.com/shorts/I1DF9y0N_dM", "views": 2342335, "comments": 275, "date": "2026-06-03", "account": "own"}, {"title": "Top 5 Cringiest Celebrations in Football", "url": "https://www.youtube.com/shorts/pCNwV-VH2es", "views": 1770154, "comments": 1303, "date": "2026-06-02", "account": "own"}, {"title": "Predicting Arsenals Starting XI Next Season", "url": "https://www.youtube.com/shorts/eJtsb0uI--8", "views": 35012, "comments": 53, "date": "2026-06-02", "account": "own"}, {"title": "Predicting Man Uniteds XI Nexts Season", "url": "https://www.youtube.com/shorts/9gPUsZDXE7Q", "views": 21706, "comments": 20, "date": "2026-06-02", "account": "own"}, {"title": "Top 5 99 Strength Moments in Football", "url": "https://www.youtube.com/shorts/L5wEOEtThWU", "views": 939110, "comments": 179, "date": "2026-06-02", "account": "own"}, {"title": "Top 5 Times Skill Moves Went Wrong in Football", "url": "https://www.youtube.com/shorts/VJCDauSrZa8", "views": 241370, "comments": 39, "date": "2026-06-02", "account": "own"}, {"title": "Predicting Real Madrids Starting XI Next Season", "url": "https://www.youtube.com/shorts/18fxXEKNUf4", "views": 16150, "comments": 26, "date": "2026-06-01", "account": "own"}, {"title": "Top 5 “Aura Farming” Moments in Football", "url": "https://www.youtube.com/shorts/NQiLI1R6uHA", "views": 28229, "comments": 11, "date": "2026-06-01", "account": "own"}, {"title": "Best Player Born in Every Year Part 1", "url": "https://www.youtube.com/shorts/9ayWm_Dbm4Y", "views": 14209, "comments": 16, "date": "2026-06-01", "account": "own"}, {"title": "Best Player Born in Every Year Part 2", "url": "https://www.youtube.com/shorts/CjgNrg-ckg0", "views": 35113, "comments": 8, "date": "2026-06-01", "account": "own"}, {"title": "Top 10 Signature Moves in Football Part 2", "url": "https://www.youtube.com/shorts/BoEXu0u1klE", "views": 128120, "comments": 44, "date": "2026-06-01", "account": "own"}, {"title": "Best Player Born in Every Year Part 3", "url": "https://www.youtube.com/shorts/4dN--dTxWEM", "views": 76835, "comments": 38, "date": "2026-05-31", "account": "own"}, {"title": "The Goat From Every Position in Football Part 2", "url": "https://www.youtube.com/shorts/yCtXVzAAzY8", "views": 23996, "comments": 89, "date": "2026-05-31", "account": "own"}, {"title": "Top 5 Strangest Ways to Block a Penalty in Football", "url": "https://www.youtube.com/shorts/8TSpXA4L51A", "views": 405183, "comments": 58, "date": "2026-05-31", "account": "own"}, {"title": "Top 5 “Worst” Tackles in Football", "url": "https://www.youtube.com/shorts/hLLVi-Ucb20", "views": 4690, "comments": 7, "date": "2026-05-31", "account": "own"}, {"title": "Top 5 Players Not Going to the World Cup", "url": "https://www.youtube.com/shorts/SsDwm-aTCFw", "views": 95003, "comments": 144, "date": "2026-05-31", "account": "own"}, {"title": "Best Player Born in Every Year Part 4", "url": "https://www.youtube.com/shorts/TrF-HMcr0j8", "views": 37920, "comments": 44, "date": "2026-05-30", "account": "own"}, {"title": "Best Player Born In Every Year in Football Part 5", "url": "https://www.youtube.com/shorts/-uByH1KqvGM", "views": 33447, "comments": 21, "date": "2026-05-30", "account": "own"}, {"title": "Best Player From Every Position in Football Part 1", "url": "https://www.youtube.com/shorts/1oImfW6p-Rg", "views": 265742, "comments": 322, "date": "2026-05-30", "account": "own"}, {"title": "Best Penalty With Every Technique in Football", "url": "https://www.youtube.com/shorts/IJ7Q15yOFEA", "views": 179467, "comments": 50, "date": "2026-05-30", "account": "own"}, {"title": "Top 5 Teams to Win The World Cup", "url": "https://www.youtube.com/shorts/GTIQB-2CIXQ", "views": 107433, "comments": 181, "date": "2026-05-30", "account": "own"}, {"title": "Best Signing From Every Year in Football Part 1", "url": "https://www.youtube.com/shorts/S8l2KZ7hceU", "views": 17211, "comments": 6, "date": "2026-05-29", "account": "own"}, {"title": "Best Signing From Every Year in Football Part 2", "url": "https://www.youtube.com/shorts/23iq9uTg3S4", "views": 25644, "comments": 8, "date": "2026-05-29", "account": "own"}, {"title": "Best Signing From Every Year in Football Part 3", "url": "https://www.youtube.com/shorts/qz3AWf1q1CY", "views": 36804, "comments": 26, "date": "2026-05-29", "account": "own"}, {"title": "Best Player From Every Shirt Number in Football Part 3", "url": "https://www.youtube.com/shorts/kxO2RLUPgR4", "views": 22532, "comments": 22, "date": "2026-05-29", "account": "own"}, {"title": "Top 10 Signature Moves in Football", "url": "https://www.youtube.com/shorts/gaLafBORfYA", "views": 1580590, "comments": 283, "date": "2026-05-29", "account": "own"}, {"title": "Best Player From Every Shirt Number Part 2", "url": "https://www.youtube.com/shorts/L-KccbDu-5Q", "views": 36292, "comments": 58, "date": "2026-05-28", "account": "own"}, {"title": "Best Signing From Every Year in Football Part 4", "url": "https://www.youtube.com/shorts/YfXgXAH6nYo", "views": 261617, "comments": 73, "date": "2026-05-28", "account": "own"}, {"title": "Best Player From Every Shirt Number in Football Part 1", "url": "https://www.youtube.com/shorts/CI6mkGTsx7c", "views": 24673, "comments": 16, "date": "2026-05-28", "account": "own"}, {"title": "Best Signing From Every Year Part 5", "url": "https://www.youtube.com/shorts/fqPLBgmz9Qo", "views": 216434, "comments": 188, "date": "2026-05-28", "account": "own"}, {"title": "Top 5 Best Signings Of This Season", "url": "https://www.youtube.com/shorts/YSby8r0O-FY", "views": 23783, "comments": 35, "date": "2026-05-28", "account": "own"}, {"title": "Top 5 Breakout Stars Of This Season", "url": "https://www.youtube.com/shorts/mqNXMt8wf-k", "views": 14598, "comments": 18, "date": "2026-05-27", "account": "own"}, {"title": "Top 5 “Dumbest” Goalkeeper Moments in Football", "url": "https://www.youtube.com/shorts/UqsVytIdTgE", "views": 16975, "comments": 12, "date": "2026-05-27", "account": "own"}, {"title": "Top 5 Penalty Run Ups That Confused Everyone", "url": "https://www.youtube.com/shorts/WiQW2Vkr4dA", "views": 89844, "comments": 29, "date": "2026-05-27", "account": "own"}, {"title": "Top 5 Worst Signings This Season in Football", "url": "https://www.youtube.com/shorts/bXyHZZBwerQ", "views": 20526, "comments": 72, "date": "2026-05-27", "account": "own"}, {"title": "Best Save From Every Body Part in Football", "url": "https://www.youtube.com/shorts/IeJcMvThbL8", "views": 401016, "comments": 140, "date": "2026-05-27", "account": "own"}, {"title": "Top 5 Worst Nutshots in Football History #lxthalfc #football #footballcommentary", "url": "https://www.youtube.com/shorts/jAkZ6sqJOWc", "views": 14742, "comments": 6, "date": "2026-05-26", "account": "own"}, {"title": "Top 5 Times Refrees Ruined Football #lxthalfc #football #footballcommentary", "url": "https://www.youtube.com/shorts/uihmeRM1WTs", "views": 226953, "comments": 132, "date": "2026-05-26", "account": "own"}, {"title": "Top 5 Times Defenders Got Bored in Football #lxthalfc #football #footballcommentary", "url": "https://www.youtube.com/shorts/lcxMesbLG1w", "views": 24763, "comments": 20, "date": "2026-05-26", "account": "own"}, {"title": "Best Goal From Every World Cup in Football #lxthalfc #football #footballcommentary", "url": "https://www.youtube.com/shorts/n_nFKEDDd5w", "views": 25412, "comments": 28, "date": "2026-05-26", "account": "own"}, {"title": "Top 5 “Unlucky” Moments in Football #lxthalfc #football #footballcommentary", "url": "https://www.youtube.com/shorts/SQmgzIkZmxg", "views": 52506, "comments": 20, "date": "2026-05-26", "account": "own"}, {"title": "Top 5 “Disrepectful” Celebrations in Football #lxthalfc #football #footballcommentary", "url": "https://www.youtube.com/shorts/0jfk7uA4N80", "views": 15137, "comments": 17, "date": "2026-05-25", "account": "own"}, {"title": "Top 5 “Illusion” Moments in Football #lxthalfc #football #footballcommentary", "url": "https://www.youtube.com/shorts/T9g8oEKCOLk", "views": 10309, "comments": 8, "date": "2026-05-25", "account": "own"}, {"title": "Top 5 Pep Guardiola Moments in Football #lxthalfc #football #footballcommentary", "url": "https://www.youtube.com/shorts/ftpdzp3eTFk", "views": 107436, "comments": 34, "date": "2026-05-25", "account": "own"}, {"title": "Top 5 “Dumbest” Moments in Football #lxthalfc #football #footballcommentary", "url": "https://www.youtube.com/shorts/XPQgeivlwTM", "views": 95362, "comments": 36, "date": "2026-05-25", "account": "own"}, {"title": "Top 5 Times Goalkeepers Got Bored in Football #lxthalfc #football #footballcommentary", "url": "https://www.youtube.com/shorts/8gw202defGo", "views": 10835, "comments": 8, "date": "2026-05-25", "account": "own"}, {"title": "Worst Dive From Every Year in Football Part 1 #lxthalfc #football #footballcommentary", "url": "https://www.youtube.com/shorts/-jp7WwZJ56M", "views": 13295, "comments": 8, "date": "2026-05-24", "account": "own"}, {"title": "Top 5 Times Goalkeepers Farmed Aura in Football #lxthalfc #football #footballcommentary", "url": "https://www.youtube.com/shorts/XmEWVnah4Ig", "views": 23031, "comments": 6, "date": "2026-05-24", "account": "own"}, {"title": "Top 5 “Aura” Penalties in Football #lxthalfc #football #footballcommentary", "url": "https://www.youtube.com/shorts/TYYl712FyCk", "views": 1221818, "comments": 320, "date": "2026-05-24", "account": "own"}, {"title": "Top 5 “How Did That Go In” Moments in Football #lxthalfc #football #footballcommentary", "url": "https://www.youtube.com/shorts/eOycNi-t4sc", "views": 25669, "comments": 17, "date": "2026-05-24", "account": "own"}, {"title": "Players and Their Longest Goals in Football #lxthalfc #football #footballcommentary", "url": "https://www.youtube.com/shorts/Yp--UhHpI0M", "views": 61716, "comments": 189, "date": "2026-05-24", "account": "own"}, {"title": "Worst Dive From Every Year Part 2 #football #lxthalfc #footballcommentary", "url": "https://www.youtube.com/shorts/g4SfSU2nZK0", "views": 56003, "comments": 75, "date": "2026-05-23", "account": "own"}, {"title": "Worst Dive From Every Year in Football Part 3 #lxthalfc #football #footballcommentary", "url": "https://www.youtube.com/shorts/vXOJpEMnjeU", "views": 198864, "comments": 147, "date": "2026-05-23", "account": "own"}, {"title": "Top 5 Worst Bicycle Kicks in Football #lxthalfc #football #footballcommentary", "url": "https://www.youtube.com/shorts/usj4rKngoU0", "views": 30240, "comments": 43, "date": "2026-05-23", "account": "own"}, {"title": "Top 5 “Practice Makes Perfect” Moments in Football #football #lxthalfc #footballcommentary", "url": "https://www.youtube.com/shorts/InPVjyE1tPA", "views": 557474, "comments": 62, "date": "2026-05-23", "account": "own"}, {"title": "Top 5 Worst VAR Decisions in Football #lxthalfc #football #footballcommentary", "url": "https://www.youtube.com/shorts/Hm3VckmOmfc", "views": 38718, "comments": 34, "date": "2026-05-23", "account": "own"}, {"title": "Top 5 Penalty Takers of All Time", "url": "https://www.youtube.com/shorts/15lIzbE393M", "views": 146809, "comments": 148, "date": "2026-04-24", "account": "own"}, {"title": "Top 5 Biggest Ballon D’or Robberies in Football", "url": "https://www.youtube.com/shorts/O3iSgwCMHyY", "views": 20719, "comments": 76, "date": "2026-04-23", "account": "own"}, {"title": "Top 5 Best Real Madrid Goals in Football", "url": "https://www.youtube.com/shorts/5YAuqbJZV4w", "views": 12701, "comments": 8, "date": "2026-04-23", "account": "own"}, {"title": "Top 5 Most Unique Goals in Football", "url": "https://www.youtube.com/shorts/sPkFdM74rd0", "views": 116089, "comments": 45, "date": "2026-04-22", "account": "own"}, {"title": "Top 5 Longest Freekicks in Football", "url": "https://www.youtube.com/shorts/7-y4OGMoL9o", "views": 23303, "comments": 17, "date": "2026-04-21", "account": "own"}, {"title": "Top 5 Olise Goals in Football", "url": "https://www.youtube.com/shorts/C0fgzrWxWlU", "views": 18474, "comments": 5, "date": "2026-04-21", "account": "own"}, {"title": "Top 5 Puskas 2026 Goals So Far This Season", "url": "https://www.youtube.com/shorts/3itCu678Apk", "views": 24853, "comments": 33, "date": "2026-04-20", "account": "own"}, {"title": "Top 5 “One in a Million” Moments in Football", "url": "https://www.youtube.com/shorts/MLmm3I1XCKc", "views": 30753, "comments": 12, "date": "2026-04-19", "account": "own"}, {"title": "Top 5 Best Chip Goals in Football", "url": "https://www.youtube.com/shorts/a38u_5M3zsY", "views": 21891, "comments": 23, "date": "2026-04-19", "account": "own"}, {"title": "Top 5 Best Barcelona Goals in Football", "url": "https://www.youtube.com/shorts/L2YFzpBTkqI", "views": 26472, "comments": 30, "date": "2026-04-19", "account": "own"}, {"title": "Top 5 Best Training Goals in Football", "url": "https://www.youtube.com/shorts/pVlS4t0pccU", "views": 26834, "comments": 10, "date": "2026-04-18", "account": "own"}, {"title": "Top 3 Teams That Let Go of Player and INSTANTLY REGRETED IT", "url": "https://www.youtube.com/shorts/WA-0LBZll6Q", "views": 45430, "comments": 36, "date": "2026-04-17", "account": "own"}, {"title": "Top 5 Most “Humiliating” Moments in Football", "url": "https://www.youtube.com/shorts/S4s-_f1QJsg", "views": 81567, "comments": 45, "date": "2026-04-15", "account": "own"}, {"title": "Top 3 Players Who Got In Trouble For The Dumbest Reasons", "url": "https://www.youtube.com/shorts/1dMYjBxt_K0", "views": 119016, "comments": 54, "date": "2026-04-15", "account": "own"}, {"title": "Top 5 Manager Reactions in Football", "url": "https://www.youtube.com/shorts/m5pKEsc5uDE", "views": 105634, "comments": 38, "date": "2026-04-14", "account": "own"}, {"title": "Top 5 Messi vs Ronaldo Goals", "url": "https://www.youtube.com/shorts/f1wBxkONYfc", "views": 25178, "comments": 61, "date": "2026-04-12", "account": "own"}, {"title": "Top 5 Most Underrated Players in Football", "url": "https://www.youtube.com/shorts/8R58EOWblPk", "views": 20177, "comments": 45, "date": "2026-04-11", "account": "own"}, {"title": "Top 5 “Die for the Badge Moments in Football", "url": "https://www.youtube.com/shorts/qwR7yIYdHs8", "views": 1135882, "comments": 295, "date": "2026-04-11", "account": "own"}, {"title": "Last 5 Valverde Goals in Football", "url": "https://www.youtube.com/shorts/SXzGuHRuhDA", "views": 11790, "comments": 9, "date": "2026-04-10", "account": "own"}, {"title": "Top 5 Worst Hattricks in Football", "url": "https://www.youtube.com/shorts/8oo_OTaBxw0", "views": 1861878, "comments": 750, "date": "2026-04-10", "account": "own"}, {"title": "Top 5 Most Humiliating Penalties in Football", "url": "https://www.youtube.com/shorts/SS3PPvvSQas", "views": 21951, "comments": 12, "date": "2026-04-08", "account": "own"}, {"title": "Top 3 Players Who Ruined Their Careers in Football", "url": "https://www.youtube.com/shorts/F9wX_6TfDIQ", "views": 64722, "comments": 32, "date": "2026-04-07", "account": "own"}, {"title": "Top 5 Goals That Look Fake But Are 100% Real", "url": "https://www.youtube.com/shorts/kN7cum1hzyY", "views": 8263, "comments": 5, "date": "2026-04-07", "account": "own"}, {"title": "Top 3 Players Who Got Rejected Before Making it BIG", "url": "https://www.youtube.com/shorts/b-Zkn9CqemY", "views": 22884, "comments": 23, "date": "2026-04-06", "account": "own"}, {"title": "Top 3 Teenagers Who Players Like Star Players", "url": "https://www.youtube.com/shorts/LmtKJb5SCWw", "views": 21054, "comments": 9, "date": "2026-04-03", "account": "own"}, {"title": "Top 3 Unexpected Teams to Win a Tournament", "url": "https://www.youtube.com/shorts/dnpZmVuZIW0", "views": 28071, "comments": 14, "date": "2026-04-02", "account": "own"}, {"title": "Top 3 Players Who Got Better After Leaving Their Club", "url": "https://www.youtube.com/shorts/sE3-dGQBL6M", "views": 79979, "comments": 17, "date": "2026-04-01", "account": "own"}, {"title": "Top 3 Players Who Changed Their Positions", "url": "https://www.youtube.com/shorts/7RmkNNgmXsQ", "views": 80104, "comments": 52, "date": "2026-04-01", "account": "own"}, {"title": "Top 3 Injuries Who Created New Players in Football", "url": "https://www.youtube.com/shorts/W6Y1s9oUUyk", "views": 28218, "comments": 15, "date": "2026-03-31", "account": "own"}, {"title": "Top 5 Most Embarrassing Moments in Football", "url": "https://www.youtube.com/shorts/6AuYIqRc7lg", "views": 165301, "comments": 44, "date": "2026-03-31", "account": "own"}, {"title": "Top 5 Players to Win the Ballon D’or", "url": "https://www.youtube.com/shorts/nLxdP6qSriw", "views": 257032, "comments": 207, "date": "2026-03-29", "account": "own"}, {"title": "Top 3 Players Who Retired Too Young", "url": "https://www.youtube.com/shorts/lstw64O_V4w", "views": 347757, "comments": 126, "date": "2026-03-28", "account": "own"}, {"title": "Top 3 Biggest RAGEBAITERS", "url": "https://www.youtube.com/shorts/_LRnxhpSCHo", "views": 23338, "comments": 13, "date": "2026-03-27", "account": "own"}, {"title": "Top 5 Ronaldo Vs Zlatan Goals", "url": "https://www.youtube.com/shorts/Davp-nKsFWQ", "views": 237448, "comments": 224, "date": "2026-03-26", "account": "own"}, {"title": "Top 3 Players Who Disappeared in Football", "url": "https://www.youtube.com/shorts/EsJDJ4M5u1c", "views": 19456, "comments": 17, "date": "2026-03-25", "account": "own"}, {"title": "Top 3 Clubs Who Betrayed Their Players in Football", "url": "https://www.youtube.com/shorts/dNVpc_sP1Wc", "views": 11048, "comments": 7, "date": "2026-03-24", "account": "own"}, {"title": "Top 5 Di Maria Goals in Football", "url": "https://www.youtube.com/shorts/Es40yiutEss", "views": 23198, "comments": 19, "date": "2026-03-24", "account": "own"}, {"title": "Top 3 Times Football Clubs got Caught CHEATING", "url": "https://www.youtube.com/shorts/MLaxROckVpA", "views": 32083, "comments": 11, "date": "2026-03-23", "account": "own"}, {"title": "Top 5 Best Richarlison Goals in Football", "url": "https://www.youtube.com/shorts/6e7j9UuVNkw", "views": 22858, "comments": 23, "date": "2026-03-23", "account": "own"}, {"title": "Top 5 Most “Accidental” Goals in Football", "url": "https://www.youtube.com/shorts/V6OPsaKpwgk", "views": 173392, "comments": 58, "date": "2026-03-22", "account": "own"}, {"title": "Top 5 Defender Goals in the Premier League", "url": "https://www.youtube.com/shorts/MI2qQ2IYxk8", "views": 53963, "comments": 53, "date": "2026-03-21", "account": "own"}, {"title": "Top 3 Craziest Ways Players Got Scouted in Football", "url": "https://www.youtube.com/shorts/G3y0NP5oa5Y", "views": 151150, "comments": 20, "date": "2026-03-21", "account": "own"}, {"title": "Top 3 Players Who UNRETIRED and Made History", "url": "https://www.youtube.com/shorts/eDP9i9tCN2k", "views": 217507, "comments": 47, "date": "2026-03-20", "account": "own"}, {"title": "Top 5 Neymar Goals", "url": "https://www.youtube.com/shorts/cYjNQMIbeOA", "views": 19894, "comments": 8, "date": "2026-03-19", "account": "own"}, {"title": "Top 5 Best Maguire Goals in Football", "url": "https://www.youtube.com/shorts/Pu3aPP7brv8", "views": 28424, "comments": 16, "date": "2026-03-18", "account": "own"}, {"title": "Top 10 Puskas 2026 Goals So Far", "url": "https://www.youtube.com/shorts/Tv-2z_kK2-s", "views": 88236, "comments": 85, "date": "2026-03-15", "account": "own"}, {"title": "Top 5 Impossible Angle Goals in Football", "url": "https://www.youtube.com/shorts/2dZt8Oe-ox8", "views": 37480, "comments": 73, "date": "2026-03-12", "account": "own"}, {"title": "Top 5 Goals That Should’ve Won Puskas 2018", "url": "https://www.youtube.com/shorts/gUeP5uqp8eE", "views": 41413, "comments": 56, "date": "2026-03-11", "account": "own"}, {"title": "Top 5 Best Low Driven Shots in Football", "url": "https://www.youtube.com/shorts/hRuAXBiyg78", "views": 77221, "comments": 65, "date": "2026-03-09", "account": "own"}, {"title": "Top 5 Best Premier League Goals So Far This Season", "url": "https://www.youtube.com/shorts/V1a3tVuiiDA", "views": 1887, "comments": 3, "date": "2026-03-08", "account": "own"}, {"title": "Top 5 Worst Dives in Football", "url": "https://www.youtube.com/shorts/UE7rjnzpDUc", "views": 38289, "comments": 32, "date": "2026-03-04", "account": "own"}, {"title": "Top 5 Most “Overrated” Footballers", "url": "https://www.youtube.com/shorts/I0sYBqOEOHY", "views": 5157, "comments": 15, "date": "2026-03-02", "account": "own"}, {"title": "Top 5 Most Unsavable Penalties in Football", "url": "https://www.youtube.com/shorts/bZz-MZGNZeQ", "views": 28962, "comments": 31, "date": "2026-02-21", "account": "own"}, {"title": "Top 5 Insigne Goals", "url": "https://www.youtube.com/shorts/Ag-wj2mEx_0", "views": 4979, "comments": 3, "date": "2026-02-18", "account": "own"}, {"title": "Top 5 “Satisfying” Goals in Football", "url": "https://www.youtube.com/shorts/kmUh3Cyz79Q", "views": 22631, "comments": 10, "date": "2026-02-16", "account": "own"}, {"title": "Top 5 Curve Goals in Football", "url": "https://www.youtube.com/shorts/2eL3nWNtCsk", "views": 16411, "comments": 26, "date": "2026-02-15", "account": "own"}, {"title": "Top 10 Saves in Football History", "url": "https://www.youtube.com/shorts/HnM0AXfIR7U", "views": 35642, "comments": 7, "date": "2026-02-14", "account": "own"}, {"title": "Top 5 “Die for the Badge” Moments in Football", "url": "https://www.youtube.com/shorts/WBDNj2kL0lw", "views": 3067959, "comments": 742, "date": "2026-02-12", "account": "own"}, {"title": "Top 5 Worst Penalties in Football", "url": "https://www.youtube.com/shorts/PJEyqJD88DM", "views": 30679, "comments": 12, "date": "2026-02-12", "account": "own"}, {"title": "Top 5 Times Ronaldo Should’ve Passed But Shot Anyway", "url": "https://www.youtube.com/shorts/sceJmf3gnZo", "views": 32485, "comments": 16, "date": "2026-02-10", "account": "own"}, {"title": "Top 5 Goals That Will Never Be Repeated", "url": "https://www.youtube.com/shorts/i3Ai-aZBev0", "views": 28414, "comments": 16, "date": "2026-02-06", "account": "own"}, {"title": "Top 5 Puskas 2026 in Football", "url": "https://www.youtube.com/shorts/0qFThRpGsVI", "views": 11198, "comments": 11, "date": "2026-02-05", "account": "own"}, {"title": "Top 10 Worst Free Kicks in Football", "url": "https://www.youtube.com/shorts/iY0LY4kYH6A", "views": 1595, "comments": 4, "date": "2026-02-03", "account": "own"}, {"title": "Top 10 Most Ridiculous Zlatan Shots But They Go In", "url": "https://www.youtube.com/shorts/ZN_HmZEIlIc", "views": 1638, "comments": 2, "date": "2026-02-02", "account": "own"}, {"title": "Top 10 Saves in Football History", "url": "https://www.youtube.com/shorts/4Qcazqjg_ME", "views": 1653, "comments": 1, "date": "2026-02-01", "account": "own"}, {"title": "Top 5 Most Nonchalant Moments in Football", "url": "https://www.youtube.com/shorts/21vNfEeIfK0", "views": 2943549, "comments": 241, "date": "2026-01-28", "account": "own"}, {"title": "Top 5 Goals That Will NEVER Be Repeated", "url": "https://www.youtube.com/shorts/PNmLGo20jlk", "views": 1841, "comments": 3, "date": "2026-01-27", "account": "own"}, {"title": "Top 10 Disallowed Goals in Football", "url": "https://www.youtube.com/shorts/UxauHYQE-qs", "views": 29218, "comments": 8, "date": "2026-01-25", "account": "own"}, {"title": "Top 10 “Smartest” Moments in Football", "url": "https://www.youtube.com/shorts/BHH2h21nxzI", "views": 18825, "comments": 5, "date": "2026-01-22", "account": "own"}, {"title": "Top 10 Goal Line Clearances in Football", "url": "https://www.youtube.com/shorts/b6EvCi694W8", "views": 39185, "comments": 11, "date": "2026-01-21", "account": "own"}, {"title": "Top 10 “Die for the Badge” Moments in Football", "url": "https://www.youtube.com/shorts/41toCCIstrU", "views": 2215, "comments": 4, "date": "2026-01-20", "account": "own"}, {"title": "Top 10 “DONT SHOOT” Moments in Premier League History", "url": "https://www.youtube.com/shorts/_Y2kJdHpSR8", "views": 47019, "comments": 42, "date": "2026-01-19", "account": "own"}, {"title": "Top 10 “DONT SHOOT” Moments in Football⚽️🔥", "url": "https://www.youtube.com/shorts/u4sixd922vc", "views": 31189, "comments": 22, "date": "2026-01-16", "account": "own"}]
```

### 6.8 Supporting scripts and prompts

#### `score_engine.py`
<!-- FILE: score_engine.py · 1935 bytes · 26 lines · sha256 c76c86060b43986f45a929d3fcde05e7312c4e50d1676dba3765444cbf2fb9fd -->
*Card scoring for the pickers (14 Sep). Prefer Algrow's real outlier_score over the computed index.*
```python
"""LxthalFC scoring engine (rebuilt 14 Sep 2026). RECENT_MEDIAN recomputed from own catalog."""
import math, json, statistics, datetime
OWN = json.load(open('/root/lx/own.json'))
OWN_MEDIAN = int(statistics.median([r['views'] for r in OWN]))
cut = (datetime.date.today() - datetime.timedelta(days=30)).isoformat()
rec = [r['views'] for r in OWN if r['date'] >= cut]
RECENT_MEDIAN = int(statistics.median(rec)) if len(rec) >= 5 else 180000
LANE_RECENT = {"award-goat-debate":540000,"messi-ronaldo":292751,"every-x-series":469592,"skill-oddity":469540,
 "goalkeeper":558128,"big-brain-iq":747074,"emotion-celebration":140036,"crashout-drama":128402,"world-cup":145636,
 "other":310552,"single-player":85513,"goals-skills-generic":77724,"top3-story":43044}
PLAYBOOK = {"award-goat-debate":1.4,"messi-ronaldo":1.3,"skill-oddity":1.25,"every-x-series":1.2,"goalkeeper":1.2,
 "big-brain-iq":1.2,"emotion-celebration":1.0,"crashout-drama":0.9,"world-cup":0.9,"other":1.0,"single-player":0.4,
 "goals-skills-generic":0.6,"top3-story":0.5}
def precedent_factor(v,c):
    cv=c/v*100 if v else 0
    return min(1.45, 0.75+0.5*min(cv/0.05,1)+0.2*min(c/3000,1))
def outlier_index(v,c,channel_median=None):
    if channel_median: return round(min(10,v/channel_median),1)
    cv=c/v*100 if v else 0
    return round(min(10,math.sqrt(max(v/1e6,.01)*max(cv/0.02,.01))),1)
def score_idea(lane,v,c,outlier_match=1.0,own_parent_views=None,channel_median=None):
    base=LANE_RECENT.get(lane,RECENT_MEDIAN); pm=PLAYBOOK.get(lane,1.0)
    pred = own_parent_views*0.75*outlier_match if own_parent_views else base*pm*precedent_factor(v,c)*outlier_match/1.2
    perf=max(1,min(99,round(20*math.log2(pred/RECENT_MEDIAN)+50)))
    return dict(pred_views=int(round(pred,-3)),pred_range=(int(round(pred*.45,-3)),int(round(pred*2.2,-3))),perf_score=perf,outlier_x=outlier_index(v,c,channel_median))
if __name__=="__main__": print(OWN_MEDIAN,RECENT_MEDIAN,len(rec))
```

#### `prompts/ai-studio-prompt.md`
<!-- FILE: prompts/ai-studio-prompt.md · 4562 bytes · 107 lines · sha256 9335c6737e9aefe3fb1be46d95ff9d82d4aff25089a560e89e75fb1758da3b0d -->
*18 Sep. Superseded by the tie-breaker pass and 'say the foot, never the number'; still valid if Joel uploads clips to Google AI Studio for exact counts.*
````markdown
# LxthalFC — AI Studio deep-description prompt

## Before you paste

1. Upload the clip (or the trimmed section) **and** `LxthalFC-Clip-Descriptions.pdf`.
2. Set video fidelity / sampling to the **highest** the interface offers. The whole point of
   using AI Studio is a higher frame rate than ~1fps — at 1fps the counts below are guesswork.
3. Paste the prompt below. Replace the two lines in **[SQUARE BRACKETS]** each time.
4. One clip per run. Do not batch — batching drops detail.

---

## THE PROMPT

You are helping me build a short-form football ranking video. I need forensic, frame-level
detail about one specific clip. Accuracy matters far more than fluency: this will be written
into a script and read aloud to a large audience, and a single wrong detail becomes the top
comment.

**THE CLIP:** [PASTE WHICH ENTRY — e.g. "Die for the Badge, number 1 — Ferland Mendy's
goal-line clearance v Man City"]

**WHAT I ALREADY HAVE:** the attached PDF contains a description of this clip written from a
pass that sampled roughly one frame per second. Read that entry first. It is reliable on which
foot, how the passage ends, on-screen graphics, player identity and commentary. Do not simply
restate it back to me.

**WHAT I NEED FROM YOU** is the layer that a one-frame-per-second pass cannot certify. Work at
the highest frame rate available to you and give me:

1. **EXACT COUNTS.** Number of touches on the ball, and who takes each one. Number of steps in
   any run-up. If a player stutters, how many stutter steps and at which point. Count them
   frame by frame and state the frame rate you are working at.

2. **TIMING.** Elapsed time of the whole passage to a tenth of a second. Time from the shot
   leaving the boot to the moment it is blocked, saved or crosses the line. How long the ball
   is airborne.

3. **DISTANCE AND POSITION.** Where each key event happens relative to fixed pitch markings —
   the six-yard line, the penalty spot, the D, the goal line. Use the markings as your ruler
   rather than estimating yards from nothing.

4. **BODY MECHANICS, FRAME BY FRAME.** Which part of which foot makes contact. The angle of the
   body at the moment of contact. Where the player's eyes are looking. Whether the plant foot
   slips. Whether a defender's weight shifts before or after the ball moves.

5. **THE EXACT FRAME OF CONTACT.** Give me the timestamp of the single frame where the ball is
   struck, blocked or deflected, and describe that frame alone in detail.

6. **ANYTHING THE SLOWER PASS WOULD HAVE MISSED** — a touch too quick to register at 1fps, a
   deflection, a second player making contact, a stumble, a shirt pull off the ball.

**RULES — these matter more than the answers:**

- If a shirt number, name, scoreline, clock or caption is **not clearly readable**, write
  "not legible". Never guess one.
- Do **not** infer players, teams, competitions or dates from your football knowledge. Report
  only what is visible or audible in this footage. If you recognise the moment but cannot see
  the evidence on screen, say "recognised but not visible on screen" and keep it separate.
- If anything you see **contradicts the attached PDF**, say so explicitly under a heading
  called CONTRADICTIONS, quote what the PDF says, and state what the footage shows. Do not
  quietly correct it and do not quietly agree with it.
- State your confidence on every count as high, medium or low, and say what limited you.
- If the footage is too low-resolution, too heavily edited or too short to answer something,
  say that instead of producing a number.

**OUTPUT IN THIS ORDER:**

```
FRAME RATE USED:
CLIP LENGTH:

TIMELINE
  Numbered beats, each with a timestamp to a tenth of a second.

COUNTS
  Touches:            [n]  confidence: [high/med/low]
  Run-up steps:       [n]  confidence:
  Stutter steps:      [n]  confidence:
  Other counts:

THE CONTACT FRAME
  Timestamp, and a description of that single frame.

MECHANICS
  Foot, part of foot, body angle, eyeline, plant foot, defender's weight.

POSITION
  Every key event located against a named pitch marking.

MISSED AT LOW FRAME RATE
  Anything a one-frame-per-second pass would not have caught.

CONTRADICTIONS
  PDF says X. Footage shows Y. Or: none.

NOT LEGIBLE
  Everything I asked about that could not be read.
```

---

## When it comes back

Paste the whole reply to me. I will fold the certified counts into the descriptions and mark
them as confirmed rather than soft, and I will chase anything in CONTRADICTIONS before it
reaches a caption.
````

#### `scratchpad/test.mjs`
<!-- FILE: scratchpad/test.mjs · 1815 bytes · 46 lines · sha256 88325e88820f9bfac6d7d93831ce042f15aafe87757bc69f6e2487a831158ea8 -->
*Playwright click-through of the notes app with window.claude stubbed to an in-memory db (Law 3). Chromium at /opt/pw-browsers/chromium.*
```javascript
import { chromium } from 'playwright';
const b = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium' });
const p = await b.newPage();
const errs = [];
p.on('pageerror', e => errs.push('PAGEERROR: ' + e.message));
p.on('console', m => { if (m.type() === 'error') errs.push('CONSOLE: ' + m.text()); });

// stub the artifact runtime with an in-memory db
await p.addInitScript(() => {
  const store = {}; const subs = [];
  const mk = (path) => ({
    set: async (d) => { store[path] = d; subs.forEach(f => f()); },
  });
  window.claude = { use: async (n) => n !== 'db' ? null : {
    doc: (p) => mk(p),
    collection: (c) => ({ onSnapshot: (next) => {
      const fire = () => next({ docs: Object.entries(store)
        .filter(([k]) => k.startsWith(c + '/'))
        .map(([k, v]) => ({ id: k.split('/')[1], data: () => v })) });
      subs.push(fire); fire(); return () => {};
    }})
  }};
});

await p.goto('file:///root/lx/notes-app.html');
await p.waitForTimeout(600);

const openCount = await p.textContent('.dcount');
console.log('counter:', openCount.trim());
console.log('decision rows:', await p.locator('.dec').count());
console.log('option buttons:', await p.locator('.opt').count());

// resolve one
await p.locator('[data-pick="budimir-slot"]').first().click();
await p.waitForTimeout(400);
console.log('after 1 pick ->', (await p.textContent('.dcount')).trim());
console.log('resolved shown:', (await p.textContent('.decdone')).replace(/\s+/g,' ').trim().slice(0,70));

// undo it
await p.locator('[data-undo="budimir-slot"]').click();
await p.waitForTimeout(400);
console.log('after undo   ->', (await p.textContent('.dcount')).trim());

console.log('packs rendered:', await p.locator('.card').count());
console.log(errs.length ? errs.join('\n') : 'no JS errors');
await b.close();
```

#### `scratchpad/shot.mjs`
<!-- FILE: scratchpad/shot.mjs · 750 bytes · 14 lines · sha256 7ccde1dca73065f4b4b1fabd5b5453a16d69330cc53623278589c15a06167dda -->
*Playwright screenshot helper at 390px and dark mode.*
```javascript
import { chromium } from 'playwright';
const b = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium' });
for (const [name, w, dark] of [['light', 900, false], ['mobile', 390, false], ['dark', 900, true]]) {
  const p = await b.newPage({ viewport: { width: w, height: 1250 },
    colorScheme: dark ? 'dark' : 'light' });
  await p.addInitScript(() => { window.claude = { use: async () => null }; });
  await p.goto('file:///root/lx/notes-app.html');
  await p.waitForTimeout(400);
  if (name === 'dark') await p.locator('[data-pick="oscar-order"]').first().click();
  await p.waitForTimeout(250);
  await p.locator('#decisions').screenshot({ path: `dec-${name}.png` });
  await p.close();
}
await b.close(); console.log('shots done');
```

### 6.9 The skill currently LIVE on disk (v1.0, saved by Joel 21 Sep 19:07 — 6.1's SKILL-PROPOSED.md is the v1.1 improvement to propose over it)

#### `~/.claude/skills/synced/…/lxthalfc-picker/SKILL.md`
<!-- FILE: ~/.claude/skills/synced/…/lxthalfc-picker/SKILL.md · 26210 bytes · 462 lines · sha256 750b51d227a71cd8a583fb1cdb3465588701fe523e5bfebfdac5be7a8ef2500a -->
*461 lines. This is what a new session actually loads as lxthalfc-picker. It has the Three Laws and Stages 0–10 but predates Stage 9.5 (QA gate), the manifest (clips.py), the Type B sheets (typeb.py) and E17–E24. Read it before proposing, because a saved proposal replaces the whole file.*
````markdown
---
name: "lxthalfc-picker"
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

**3. VALIDATE IN THE SAME KIND AS THE OUTPUT.** A parse check is not a render check. A render check
is not a click-through.

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
   declare the departure. "Transfers" was built as a five-pick countdown against a one-story 69s ref.
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
  references only for format. Verify every claim against sources, never comments. Straight to Stage 5.

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

**Downloading:** short succeeds, long + high quality fails. **Dropping quality converts failures**
(1080→720, 720→480). **Trimming to a segment works** where the whole file refuses. A refusal at every
quality means the source is blocking — find another upload.

**Frame-level IS possible with the file in the sandbox:** `ffmpeg -ss <t> -i f.mp4 -frames:v 1 -q:v 2
out.jpg` then `Read` the JPEG. The proxy denies YouTube and audio.algrow.online, so **he must upload
the file** — say that plainly rather than implying a high-fps pass happened.

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
labels take a colon; `CANNOT DETERMINE` is a bare section header.

### SAFE / SOFT / UNSAFE
- **SAFE:** which foot, how it ends, unbroken shot or not, on-screen text, commentary, slip or
  stumble, kit colours, camera angles, whether play stopped.
- **SOFT:** touch counts, steps, distances, timings. **SAY THE FOOT, NEVER THE NUMBER.** Son returned
  9, 10 and 11–12 across three passes; the feet never once disagreed.
- **UNSAFE:** identity and outcome. Run the ENDING CHECK, then take conflicts to Stage 5.

### Is it a game? Unreliable in BOTH directions
Official club, league and federation channels are **trusted by default** — a gameplay flag on one is
the model being wrong (it called FIFA's own World Cup highlights, Arsenal's own CL final highlights,
the Germany–Paraguay shootout and the Spurs Europa final gameplay, each time reasoning from squads
that postdate its knowledge). A call only counts with **visible game UI**: squad menus, rating cards,
stamina bars, radar, active-player arrow, controller prompts, bracket screens. Roster plausibility is
worthless. **A TRUE positive looks like a PS5 logo under the scoreline** — ZDF sportstudio published
a simulated PSG–Arsenal preview with exactly that.

**Fabricated** = game or doctored; catch it with **a scoreboard that contradicts itself between two
shots of the same passage**. **Manipulated** = real footage padded by looping, scrubbing, speed
change or replaced audio — Neymar's 2018 roll is ONE roll and both fan clips pad it. Check whether a
"long" moment is actually long.

### Depth must be EVEN across a pack
Measure it. One pack averaged 382 words a clip against another's 713, and the thin one was the
two-part goalkeeper pack that least deserved it. **If one clip is a third the length of its
pack-mates, that is a gap, not a style.**

### The two-run contract
**Run 1 — the Pack:** discovery → references watched → every candidate watched → shortlist → formula
→ gates → all picks. No stops, no clarifying questions mid-run.
**Run 2 — the Scripts:** describe every moment to completion, then write in his format — intro in one
breath, ellipsis only on the suspense clause, punchline closing each entry, no quotation marks,
numbers as words. **Run 2 is a batch job, not a conversation.** Mid-run messages are for genuine
blockers only, and a blocker goes in the app.

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

What this caught: Eze shot WIDE LEFT, not the crossbar, against two agreeing vision passes · Ederson's
assist IS a goal kick, reported at 85–86 yards, against a sheet that said "not a goal kick" · Son's
Burnley goal WON THE FIFA PUSKÁS AWARD, which is in no frame · IFAB ruled three weeks later that the
VAR had no right to review Embolo's card at all.

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
share a mechanism, name the pair and drop one.

**Counting across a pack finds lines nobody else has.** "Every one of these runs is one-footed" came
from tallying feet across five clips. "Every delivery method that appears twice splits by side" came
from re-counting a taxonomy that had been called five, then three, and was actually four.

**Test format fit against THE PICKS, never against what the reference contained.**

**Sequel penalty** (n=448): non-sequel median 89,192 · "Part 2" median 41,558. Part 2s do less than
half. Only two ever cleared 300k. REDO beats PART. Say it in any header containing a sequel.

**Comment classes:** SPECIFIC-PRO (may nominate, still needs footage) · ANTI-FACTUAL (a real error,
fix it) · ANTI-JUDGEMENT (bait working, keep it at #4) · **CAPTION-BAIT (zero information about the
world)** · GENERIC (never attach to a pick). Factual-error comments are the top-liked comments on his
biggest videos — treat them as the error log.

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
only in a PDF, **and never in a calendar**. `{id, pack, title, why, opts:[[label, subtext]]}` saved to
`decisions/<id>`. Two to four **concrete, tappable** options, never an open-ended question. Include
the do-nothing option where one exists. Mark your recommendation once and leave it.

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

**A publish to an artifact this conversation has not read is refused** — `Artifact(action="read")`
first and merge onto what comes back. Curly quotes inside note strings, never straight ones.

---

## STAGE 10 — SELF-AUDIT (never skip)

**A.** Grade the run against every gate. **Report only the failures** — a wall of passes buries what
matters.
**B.** List what you got wrong, including anything corrected mid-run: what, why, and the rule.
**C.** **Append each to `errors.md`** as `WHAT · WHY · RULE · STAGE` with a new `E##`.
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
| `LXTHALFC-SYSTEM.md` | the full operating prompt — twelve stages, pasteable into a fresh session |
| `errors.md` | **the error log — read at Stage 0, appended at Stage 10** |
| `queued.csv` | master queue `date,title,link,status` — the recovery file after a context loss |
| `rejected.json` / `dedup_base.json` | rejected titles / every title ever surfaced, normalised |
| `own.json` | his catalogue — refresh with `get_channel_shorts` every run |
| `notes-app.html` | the pack-notes Artifact; republish the same path. Holds the decisions panel |
| `refaudit/` / `deep/` | reference verdicts / full forensic descriptions |
| `handover/` | `data.py` (sheets, decisions, systems) + `build_master.py` (the PDF) |
| `score_engine.py`, `build_picker_*.py` | scoring + HTML builder |

The app's db holds `notes/<packid>` (his write-ups) and `decisions/<id>` (his answers). Read both at
Stage 0. **A link appearing on many rows is a red flag, not a shortcut.**

---

## NON-NEGOTIABLES

- Never fabricate a stat or URL. Every card cites a real scraped precedent or one of his own videos.
- Never invent a moment. If it only exists in gameplay results, it does not exist (Neuer's Schalke
  corner assist and Nicholas Hagen's punt both survived rounds of work before this caught them).
- **Check `own.json` before calling any video someone else's.**
- Report true counts. 34 ideas when he asked for 100 means deliver 34 and say so.
- Close evidence gaps with a tool call, not a question — and when the gap is a fact, that call is a
  web search.
- **Approved picks and their order are locked.** Propose changes as a note; do not apply them.
- **Kills are his call.** Flag risk as "consider dropping" and build the pack anyway.
- **Evidence already gathered survives a rewrite** unless disproved. A large ANTI-JUDGEMENT comment is
  evidence FOR a pick — Robben at Chelsea (1,889 likes) was dropped in a revision after he said keep.
- Every pick gets a one-line explanation. Every video gets three subs.
- **When a correction lands, fix it in EVERY surface at once** — deep notes, pack sheet, app, PDF. One
  taxonomy was simultaneously "five", "three" and "four" across three documents.
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
    pred = own_parent_views*0.75*outlier_match if own_parent_views else \\
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
  es el héroe del Toluca", "der größtmögliche Grätschmoment" — all free from watching, all better
  than anything written from scratch.
- **An official award attached to a pick is a free line.** Son's Burnley goal won the Puskás and the
  pack had not mentioned it. Check whether any pick won something.
- **Period detail sells an era better than a caption.** A 1996 clip's hoardings read SHARP VIEWCAM,
  McDonald's, Carling, CIS, Ryman, Wilkinson Sword and Kellogg's Frosties with Tony the Tiger.
  Describe the picture honestly too — 4:3 in 16:9 with blurred pillarbox bars, interlacing judder,
  chroma bleed on the reds — and the age becomes the point rather than a flaw to hide.
- **Edit grammar worth stealing from single-story references:** real news-article screenshots as
  evidence beats, punctuated by meme reaction cutaways. Fact, fact, reaction.
- **Voice note:** ~19,400 likes of comments mock his drawn-out sentence endings on Shortest Lived
  Primes alone. He trains his ElevenLabs clone on trimmed final videos, so the clone is learning the
  thing people mock — flag this when voice comes up. Settings that work: Multilingual v2 (not
  Turbo/Flash — generic-accent drift), Speed 1.0 / Stability 35% / Similarity 90% / Style 10%,
  per-block generation, ellipses and paragraph breaks instead of `<break>` tags, no quotation marks,
  numbers as words.
````

#### `handover/hx/regen_packs.mjs`
<!-- FILE: handover/hx/regen_packs.mjs · 668 bytes · 9 lines · sha256 bedf41f65c32f0859ae0c6ef32eeab206ab70c2a719c10f998fc0fb6dc649964 -->
*22 Sep. Regenerates handover/final_packs.json from notes-app.html's PACKS with tags stripped — run after any app edit so the JSON never drifts from the app.*
```javascript
// Regenerate handover/final_packs.json from notes-app.html's PACKS (tags stripped, <br> → space)
import fs from 'fs';
const s = fs.readFileSync('/root/lx/notes-app.html','utf8');
const m = s.match(/const PACKS = (\[[\s\S]*?\n\]);\n\nconst DECISIONS/);
const P = eval(m[1]);
const strip = t => (t||'').replace(/<br\s*\/?>/g,' ').replace(/<[^>]+>/g,'').replace(/\s+/g,' ').trim();
const out = P.map(p => ({id:p.id, title:p.title, state:p.state, meta:p.meta, picks:p.picks.map(r => r.map(strip)), subs:p.subs, note:strip(p.note)}));
fs.writeFileSync('/root/lx/handover/final_packs.json', JSON.stringify(out, null, 1) + '\n');
console.log(out.length, 'packs written');
```

---

## 7. REJECTED IDEAS (and why — do not re-propose)

- **Lookalikes pack.** Reference failed title promise (a boot full of noodles under a lookalikes title); Joel first said "Rebuild all five" in the app, then "drop lookalike" in chat. Dropped; title in `rejected.json` and `dedup_base.json`.
- **Tah at penalty-2 #2.** Same mechanism as Zaza (lean back, blaze over). Also his label rested on a false premise: the "run-up slip" does not exist (two sources: "no slip, no stumble, no scuff, and no loss of footing whatsoever"). Now a sub.
- **Gabriel as a penalty pick.** Over the bar for certain — duplicates Zaza. Sub only.
- **Splitting Transfers into five single-story videos.** My own recommendation, reversed (E09): imported the reference's 69-second saga onto picks that are one-line facts; a 70-second format is equally unproven on his channel.
- **Ronaldo → Cape Verde** (another-nation). The link is a great-grandmother; FIFA Article 6.1 needs a parent or grandparent.
- **Neymar → Man City** (transfers). Weakest of three versions; replaced by Neymar → Real Madrid (Pérez says he passed a medical).
- **Riquelme** (forgot-club). Joel: casual fans don't say the name out loud. Replaced with Salah-at-Chelsea-tier names.
- **Neuer at Schalke going up for a corner / Nicholas Hagen's punt / Ederson → Haaland** (gk-assists). First two unsourced beyond gameplay — probably invented; the third exists but is not in the official compilation.
- **The unverified "how few games the trio started together" stat** (psg-trio). Dropped on Joel's call; replaced by Penaltygate.
- **Ordering change Embolo → #4, Richards → #3** (oscar-2). Proposed by me, declined by Joel ("Keep the approved order"). The IFAB ending is carried by the script.
- **Kyle Walker replacing Stones** (badge-redo). Proposed by me, declined ("Keep Stones anyway"). Walker stays in subs.
- **A calendar appointment for decisions.** Misread of "appointment" (E14). Decisions live in the app.
- **"Ref failed" as a pack state.** Described the audit, not the pack (E16). Replaced by "Shoot knowing".
- **Stating counts (touches, steps, mm) as fact.** 9/10/11–12 on Son; 11.7/11.2/11 on Stones. Say the foot, never the number; say eleven, no decimal.
- **Stating Eze "wide left" as settled** (E20). Now DISPUTED.
- **Whole-video analysis passes.** Measured worse than scoped per-moment passes on identical footage.
- **The AI Studio prompt route** (`prompts/ai-studio-prompt.md`). Written 18 Sep as a way to get higher-than-1fps counts by pasting into Google AI Studio with the clip uploaded. Superseded by the tie-breaker pass and the "say the foot" rule; kept on disk for reference. Still valid if Joel wants exact counts and will upload clips.
- **Lists of ideas he does not want:** story videos, debate/versus, Messi–Ronaldo wholesome lists, classic-match retells, FIFA/EA FC simulation footage.
- **A seventh Die for the Badge.** He already has six; the redo is the seventh and is justified only because it is described to a depth the others were not — do not propose an eighth.
- **Sequels by default.** n=448: non-sequel median 89,192 · Part 2 median 41,558. Redo beats Part.

---

## 8. OPEN QUESTIONS

Ordered by how much they can change what Joel shoots. None of them blocks a shoot today; each has a safe default already applied.

1. **Where did Eze's penalty go?** Wikipedia: "shot wide left". Three Algrow vision passes on Arsenal's own footage (`ygcv9fQheII` 01:22–01:27): over the bar. TNT live commentary: "missed his side's second effort". **Default applied:** DISPUTED everywhere; script says "he missed". **Why it matters:** if it was over the bar, Eze (#1) and Zaza (#5) share an ending — the duplicate the Tah removal was meant to fix. **How to close it:** a full-match replay or UEFA's official shootout graphic; or Joel watches it and rules (Law 2: his call on how it looked, but the outcome is a fact — a source beats his eye here).
2. **19 Type B picks are still FROM COMMENTS** (list in 5.5). **Default applied:** shipped with a C marker and an INFO line; the pack notes tell him which lines carry a quote/fee/number. **How to close:** one WebSearch + WebFetch each; Olise (four nations), Davies (Buduburam), Ronaldinho (48 hours), De Gea (fax), Fekir (interviews), Henry (two pronunciations) first.
3. **Neuer v Dost fixture.** Bundesliga or DFB-Pokal, 2020 — the deep file describes the moment from `PaaZxPh0A-o` 02:00–02:08 but the competition is not pinned. **Default:** the sheet does not name the competition. **Close:** search "Neuer Dost heel save" + Frankfurt 2020.
4. **Alisson's celebration run** is not in the PL compilation (cuts at 00:11). **Default:** the sheet says so; the assist clip is enough for the pick. **Close:** find a second source if he wants the run.
5. **acc-5 Full Reverse Save** has no standalone window — only the reference compilation `ZbunM6UKwts`. **Default:** manifest row says so. **Close:** Stage 3 search with the Championship/green-kit details from the deep file.
6. **acc-4 No-Look Save keeper's name** — the boards say Swansea (home), keeper #33, opponent in red with a "Scott". **Default:** unnamed. **Close:** "Swansea 33 goalkeeper" search per the deep file's ACTION line.
7. **Son's exact touch count** — 8 visible RIGHT/CERTAIN, total unstable (9/10/11–12). **Default:** say the foot. **Close only if Joel uploads the trimmed clip** for a frame-by-frame count.
8. **Will Joel save the v1.1 skill?** The v1.0 card was saved (21 Sep); the follow-up card with Stage 9.5 was not. **Default:** the v1.0 skill loads automatically and `LXTHALFC-SYSTEM.md` v1.1 is pasted for the rest. **Close:** propose once more from `handover/SKILL-PROPOSED.md` as an improvement to `lxthalfc-picker`.
9. **The four `data.py` yardages** (6/25/10/5 yards) — leave as pitch geometry, or strip from the sheet so the warnings go to zero? **Default:** left, acknowledged. Cosmetic.
10. **Does he want `own.json` refreshed** before the next batch (`get_channel_shorts` on `UCAFHCtjzJwnyXB1_tB-OI3A`)? Stage 0 says always; it was last refreshed 14 Sep.

---

## 9. NEXT STEPS (in order)

**If Joel is shooting the September batch:**

1. Open `LxthalFC-September-SENDOFF.pdf` (84pp) and the notes app. Nothing is waiting on him.
2. Before camera on Type B packs, verify the C picks that carry a quote/fee/number (Section 5.5), or accept them as comment-sourced.
3. On penalty-2 #1, say "he missed"; do not say crossbar, wide, or over.
4. On badge-redo #2, say "eleven millimetres", no decimal on screen; frame Stones as "you've seen this one before".
5. On pace-abuser-2, say the foot, never the number.

**If the next instance is continuing the work:**

1. `cd /root/lx` (or recreate it from Section 6 of this file). Run `python3 qa.py` — expect 592 · 7 · 0.
2. Read `errors.md` end to end (E01–E24). Read `LXTHALFC-SYSTEM.md` v1.1.
3. Read the app's `decisions` and `notes` collections via `ArtifactData` (`url` = the notes app; `action: "list"`, `collection: "decisions"` then `"notes"`). Act on anything new.
4. Close open question 1 (Eze) if a source exists; then re-check penalty-2 variety.
5. Verify the 19 C picks (Section 5.5) with WebSearch/WebFetch; flip each to V in `typeb.py` with its source; rebuild (`cd handover && python3 build_master.py`); rerun QA; republish nothing unless the app changes.
6. Pin Neuer's fixture; try to name the No-Look keeper; try to find a standalone Full Reverse clip.
7. Propose the v1.1 skill from `handover/SKILL-PROPOSED.md` via `propose_skills` (kind `improvement`, target `lxthalfc-picker`; read the synced v1.0 SKILL.md first, since a saved proposal replaces the whole file). Do not edit the synced file.
8. Refresh `own.json` with `get_channel_shorts` before any new-batch work.

**If starting a new batch:** paste `LXTHALFC-SYSTEM.md` and run "RUN IT" at its foot, entry 1A (from nothing) or 1B (from picks). Every stage names its Algrow calls.

**Always at the end of a run:** Stage 10 self-audit; append to `errors.md`; extend `qa.py` if the error was mechanically detectable; say which pattern it fits.

---

## 10. FILES & LINKS

### 10.1 Hosted

| What | URL | Version |
|---|---|---|
| Notes app (packs + decisions panel, `db` capability) | https://claude.ai/artifact/TcgNQsyPeAHvwua6AuGfLR | 18 (22 Sep 2026) |
| System page (v1.1, 13 stages, QA gate, error log E01–E24) | https://claude.ai/artifact/8btYKYVpFmLaTmYBzTGyEV | 3 (22 Sep 2026) |
| Joel's channel | https://www.youtube.com/channel/UCAFHCtjzJwnyXB1_tB-OI3A (@thelxthalfc) | — |

### 10.2 Deliverables in `/root/lx`

| File | Size | Purpose |
|---|---|---|
| `LxthalFC-September-SENDOFF.pdf` | 84 pages | The send-off Joel shoots from (built by `handover/build_master.py`) |
| `LxthalFC-CLIP-MANIFEST.csv` | 36 lines | Clip manifest: pack, rank, pick, source, video id, link, in–out, cut-on, note |
| `LXTHALFC-SYSTEM.md` | 494 lines | The pasteable operating prompt, v1.1 |
| `errors.md` | E01–E24 | The error log |
| `qa.py` | 303 lines | The QA gate |
| `clips.py` | 100 lines | Manifest source of truth (35 clips, 28 unique sources) |
| `typeb.py` | 239 lines | Type B sheets source of truth (45 picks, 25 V / 19 C) |
| `handover/data.py` | 791 lines | Production sheets, glance rows, decisions, systems, verified facts |
| `handover/build_master.py` | 390 lines | PDF builder (DEEP mapping, STAT dict, Parts 5.5/5.75) |
| `handover/final_packs.json` | 16 packs | The packs as shipped — regenerate with `node handover/hx/regen_packs.mjs` after any app edit |
| `handover/hx/` | 8 files | This handoff's narrative sections, `assemble.py` (builds HANDOFF.md) and `regen_packs.mjs` |
| `handover/SKILL-PROPOSED.md` | 510 lines | The v1.1 skill text to propose (unsaved) |
| `notes-app.html` | 565 lines | Source of the notes app artifact |
| `system-page.html` | 520 lines | Source of the system page artifact |
| `deep/*.md` | 18 files | Forensic descriptions, Type A |
| `refaudit/*.md` | 10 files | Reference audits |
| `queued.csv` · `rejected.json` · `dedup_base.json` · `own.json` | state | Queue, rejects, dedup base, Joel's catalogue (459) |
| `score_engine.py` | 26 lines | Card scoring for pickers |
| `prompts/ai-studio-prompt.md` | — | Superseded AI Studio frame-count prompt |

### 10.3 Historical (superseded, kept on disk, not embedded)

`LxthalFC-September-Batch.pdf` (18 Sep) · `LxthalFC-Clip-Descriptions.pdf` (18 Sep) · `LxthalFC-Reference-Audit.pdf` (18 Sep) · `LxthalFC-Clip-Descriptions-DEEP.pdf` (19 Sep) · `LxthalFC-September-Handover.pdf` (20 Sep) — all superseded by the SENDOFF. Builders `build_pdf.py`, `build_deep_pdf.py`, `handover/build.py`, `desc/`, `audit/` — superseded by `build_master.py` + `data.py`. Pickers `artifact-competitors.html`, `artifact-wave2.html`, `artifact-viral.html` with `build_picker*.py`, `build_board*.py`, `ideas-2026-09-14-*.json`, `lxthalfc-ideas-*.csv` — the 14 Sep idea boards Joel picked from. Competitor scrapes `AhmedsGoal.json`, `FootyRanks.json`, `Frid7.json`, `Hanlonman.json`, `MagicalEight.json`, `MarkFC.json`, `OGClips.json`, `SantaBall.json`, `T7Legacy.json`. `handover_packs.json`, `handover_links.json` (20 Sep intermediates). Backups `notes-app.bak.html`, `.bak2`, `.bak3`, `.bak4` (pre-Version-17). `frames/` is empty.

### 10.4 Elsewhere

- Synced skill (v1.0, live): `/root/.claude/skills/synced/ebcf3a5b-ca3b-453a-9d8a-ad31ba392e4f_61e2fdec-3528-41e3-a2fc-8baee42d0a5d/lxthalfc-picker/SKILL.md` (461 lines, 21 Sep 19:07) — read-only cache of what Joel saved.
- Scratchpad: `/tmp/claude-0/-home-claude/ffb04e18-0a9b-526f-96c6-d01f1e7050ac/scratchpad/` — `test.mjs`, `shot.mjs` (Playwright checks), `test50.mp4`, `h30.jpg`, `h31.jpg`, `node_modules/` (playwright).
- Transcript of this session: `/root/.claude/projects/-home-claude/ffb04e18-0a9b-526f-96c6-d01f1e7050ac.jsonl` (post-compaction portion only).

### 10.5 Source video ids used in the manifest (28 unique)

See `clips.py` (Section 6.2) for every window; Tah's window below is from `deep/penalties.md`, since a sub is not in the manifest. Key ones: Son `C-CefuZ6h1k` (cut 02:40–03:19) · GK assists `cVtF64Un-0o` (Ederson 00:12–00:38, Alisson 00:00–00:11, Schmeichel 06:56–07:13, Čech 01:24–01:53, VdS 04:14–04:45) · Stones `MriNd_wn1Os` 00:55–01:40 (cut 01:26–01:32) · Pires/Henry `N4bQVTczcLQ` 00:00–00:34 · Budimir `4EvIcyRuAXg` 00:00–00:38 (cut 00:30–00:35) · Eze `ygcv9fQheII` 01:22–01:27 (shootout from 01:12) · Zaza `5_9OwlwAMMk` 00:14–00:23 · Tah (sub) `lq3o-vf5o40` 00:00–00:04 · Agüero `he7mZJDIEOQ` 01:23–01:43 · Neuer `PaaZxPh0A-o` 02:00–02:08 · Choupo `PaaZxPh0A-o` 05:05–05:19 · acc-3/4/5 from `ZbunM6UKwts` · Valverde `3JiwVYCnHqU` · Robben `qDgAANEXQqg` 02:02–02:24.

---

## 11. POST-WRITE RE-SCAN — what the first draft missed, now added here

After sections 1–10 were written I re-scanned the session (the compaction summary, the error log, the build scripts, the transcript of this continuation, and every file on disk) and checked 145 specific facts against the narrative. Thirty were only present inside the embedded files or not at all. They are added below so nothing depends on reading 700 KB of embeds.

### 11.1 Joel's messages this session, verbatim and in order (so the next instance hears his voice, not my paraphrase)

1. *(continuation prompt)* Resume — deliver the send-off PDF. → delivered at 66 pages; now 84.
2. "certain clips do beat by beat certain do others would you say each vid has described it well in its own way or is inconsistent"
3. *(AskUserQuestion answer)* "Son + vocabulary + deepen the thin ones"
4. "the level of description here is far better than a human"
5. "now whenever something is blocked or needs my call you make an appointment for me to resolve it"
6. *(AskUserQuestion denied)* "i meant app not appointment"
7. "i've added my deciosions"
8. "drop lookalike"
9. "why's there still flagged vids isn't it done now"
10. "so is it done now"
11. "please provide the app below each time there's a need for input but overall you should be solving these yourself"
12. "please create a system or prompt to repeat everything within this session for new video ideas and allow for self analysis and improvement to solve errors and create stages for each point. you can ask questions to refine this but ensure nothing is missing from revisions and messages for this system using prompt builder with algrow"
13. *(AskUserQuestion answers, four questions)* "Write every stage against Algrow's tools (Recommended)" · "Both: a pasteable prompt and the skill (Recommended)" · "Both entry points (Recommended)" · "Error log it reads and appends to (Recommended)"
14. "have a built in qa within this system"
15. "also for septmeber send off could you give the timestamps as to where these clips were present with video refrence links"
16. "provide the player name ones with no descriptions"
17. "are you able to look at each frame"
18. *(a local /model switch to claude-fable-5-1 — not a request)*
19. "Write a complete handoff document so another Claude instance (in Claude Code) can continue this work with zero loss of context…" *(this document)*

From the earlier, pre-compaction part of the engagement, still binding: "It's a side-foot, keep it" · "you need to make a system to verify yourself, the same way id search it up you can. you need to be independent" · the eight app decisions in 3.1.

### 11.2 The four AskUserQuestion forks I offered for the system (and which he took)

Q1 tool binding: *write every stage against Algrow's tools* (taken) vs tool-agnostic. Q2 form: *both a pasteable prompt and the skill* (taken) vs one. Q3 entry: *both from-nothing and from-picks* (taken) vs one. Q4 self-improvement: *an error log read at start and appended at end* (taken) vs a checklist only. In every case he took the Recommended option, which is why the system has the shape it has.

### 11.3 Build-script defects fixed this session (so nobody re-fixes them)

- `handover/build_master.py` `unwrap()` absorbed continuation lines into `#N` headings → guard added: `and not re.match(r"^#\d+ ", out[-1])`.
- `S["tiny"]` was undefined in the manifest table → use `S["cell"]`. `AMB2` / `AMBBG` undefined → use `ACC`, `AMB`.
- The IN–OUT column wrapped → widened to 74 pt; manifest `colWidths = [22, W-2*M-22-148-74, 148, 74]`.
- `qa.py` constants: `TYPE_A = {"signature-redo","gk-assists","pace-abuser-2","oscar-2","badge-redo","penalty-2","accidental-saves"}`, `WINDOW = 520`, `BANNED_LABELS` (READ OFF THE SHIRTS, FASCIA BANNERS, FAN BANNERS, CARD GRAPHICS), `COUNT_AS_FACT` regex with a broad caveat regex.
- Python heredoc `SyntaxError` from an em-dash inside a `\'`-escaped string → write edit scripts with double-quoted strings / HTML entities.
- ffmpeg synthetic clip: a `drawbox` moving element rendered nothing → `drawtext` "O" with `x='30+t*280'` at 50 fps.
- `notes-app.html` splice defect (E12): the DECISIONS array follows PACKS with the same `],` delimiter; compute `PS`/`PE` (start/end of PACKS) and pass both to every `find()`, recomputing `PE` after each edit, and restore `];\n\nconst DECISIONS = [` afterwards.

### 11.4 Stage details that were only inside the embedded prompt

- **Stage 3 search:** six angles — player+opponent+competition+action · how a fan would phrase it · official match highlights · the reference it came from · category compilations (highest value) · native-language phrasing. Queries of three or four words; long descriptive queries return zero. Gate 3: only "unsourceable" after two distinct angles AND a compilation search AND a re-watch of the reference.
- **Stage 7 formula:** 5→1 as #5 proven hook · #4 most engaging/controversial · #3 engaging · #2 least engaging but proven · #1 conventional finisher, hard declarative; a "Top 10" Part 2 runs 10→6. Comment classification: SPECIFIC-PRO (may nominate, still needs footage) · ANTI-FACTUAL (real error, fix) · ANTI-JUDGEMENT (bait working, keep at #4) · CAPTION-BAIT (zero information) · GENERIC (never attach to a pick). Sequel penalty n=448: non-sequel median 89,192, Part 2 median 41,558.
- **Depth measurement that started the consistency fix:** one pack averaged 382 words a clip, another 713, and the thin one was the two-part goalkeeper pack. Scoped vs whole-video, measured on identical footage: the scoped pass found a shirt name, sponsor boards and a keeper's boot colour the whole pass missed.
- **Gameplay-flag statistic:** across 33 passes every gameplay flag landed on 2025/2026 footage and none on older footage — the model's squads-look-implausible heuristic, not UI evidence.

### 11.5 Verified facts the narrative had only pointed at

- Embolo: sent off for simulation v Argentina, 72nd minute, World Cup 2026 quarter-final; referee Pinheiro booked Paredes, VAR rescinded that yellow and gave Embolo a second; Argentina won 3-1 aet; three weeks later IFAB said the VAR had no right to review it (a caution that is not a second yellow can only be reviewed for mistaken identity); FIFA said the call "restored justice". Sources CNN, ESPN, The Week.
- Germany 1-1 Paraguay, 3-4 on penalties, last-32 exit (Sky, ESPN) — the Tah gameplay flags were false positives; "no slip, no stumble, no scuff, and no loss of footing whatsoever".
- Champions League final 30 May 2026: PSG 1-1 Arsenal, PSG 4-3 on penalties; Havertz 6', Dembélé pen 61'; shootout order Ramos S · Gyökeres S · Doué S · **Eze MISSED (disputed where)** · Nuno Mendes saved by Raya · Rice S · Hakimi S · Martinelli S · Beraldo S · Gabriel OVER THE BAR. ZDF sportstudio's PSG–Arsenal video `PTs-3jmCQY8` is a PlayStation sim with the PS5 logo under the scoreline at 00:20 — the model true-positive for game footage.
- Lewandowski → Blackburn 2010 stopped by the Icelandic ash cloud grounding his flight (Sky ×2 + his own words). Pérez says Neymar passed a Madrid medical (Goal). Lampard's non-celebration v Chelsea on loan at City: Cahill called it "weird" (Sky). Joel's Full Name Pt1 = 3,240,079 views; Pt2 449,749 (0.14×).
- Match clocks read off scorebugs: Valverde on Morata 114:29 (Supercopa final) · Van de Ven 67:38 (Europa League final, Bilbao) · Süle v Mbappé 16:36 (Dortmund, #25) · Ferland Mendy 86:11 (CL semi, Madrid 0-1, 3-5 agg) · Budimir clock 96:43→97:37 (+7) · Suárez/Chiellini ITA 0-0 URU 78:25 · Pires/Henry ~72' 22 Oct 2005 · Stones GDS graphic shows only "NO GOAL", no number.

### 11.6 Script gifts already found (so they are not re-found)

Cruyff on camera: "I never did tricks. I saw something and I did it and it just came out. There was an opponent there and I had to outplay him. So that was the easiest way, so you just do it." · Serbian commentary on Budimir: "Nije ni šutnuo!" — he didn't even take a shot; closing frame Arrasate slumped, chin on fist · Simeone pats Valverde on the head as he walks off; Italian commentary "Sarà rosso, ma è una super giocata" / "L'unico modo" · German on Süle: "Der größtmögliche Grätschmoment" · Liga MX referee accidental save: "¡El árbitro es el héroe del Toluca!" · Zlatan: "le capitaine Zlatan qui sauve son équipe" · Choupo-Moting source caption "200 IQ" · Man City's site on Stones: "11 MILLIMETRES of the ball had not crossed" · Penaltygate tweet Neymar liked: "in no club in the world would Neymar be the second taker".

### 11.7 Numbers that were only in the state files

`rejected.json` 254 titles · `dedup_base.json` 155 normalised titles · `own.json` 459 entries (14 Sep) · `queued.csv` 135 lines · credits: quoted ~18, actual ~110 for the scoped batch (E15).

### 11.8 Things not on disk anywhere (be aware)

- The **exact prompt strings** sent to Algrow's `start_video_analysis` per moment were composed inline and not saved as files; the standing-prompt contract in Stage 4 of `LXTHALFC-SYSTEM.md` (eight named sections, three modes, vocabulary, CANNOT DETERMINE) is the specification to regenerate them from. The tie-breaker prompt likewise: ask only the disputed question; require the answer, the visual evidence naming plant leg and contact boot, a CERTAIN/LIKELY/UNSURE grade, and whether contact is visible; say plainly that "cannot tell" beats a confident guess.
- Algrow **job ids** were transient and are not recorded.
- The two `propose_skills` cards' exact text is superseded by `handover/SKILL-PROPOSED.md`.
- The pre-compaction transcript is not on disk; the compaction summary is the record and this document reproduces its substance.

### 11.9 Corrections made to the narrative by the adversarial review (Stage 9.5 applied to this document)

A subagent was told to find what was wrong in sections 1–10 against the files on disk. It found, and I fixed:

- **The skill on disk is not the old picker.** It is 461 lines, dated 21 Sep 19:07, and already contains the Three Laws and Stages 0–10 — proof that the first `propose_skills` card *was* saved. The narrative had said "306 lines, not saved" in four places (from a stale summary). Corrected everywhere: v1.0 is live; v1.1 (`SKILL-PROPOSED.md`) is the unsaved improvement.
- **The PDF part map was wrong** (decisions are Part Four, verified facts Part Five, systems Part Six; the full descriptions sit inside Part Two). Corrected in 5.1.
- **"Warnings acknowledged in Part Four of the PDF" was false** — the PDF had no QA acknowledgement at all. Fixed at the source: `build_master.py` now runs `qa.py --json` at build time and prints the gate line and every WARN/INFO by name at the end of Part Six. Rendered and read back (Law 3).
- **Two stale proposals were still live in the app and JSON** — the Oscar re-ordering Joel declined and the Transfers split I withdrew. Fixed; app Version 18; `final_packs.json` now regenerated by script. Logged under E24's FIX line.
- Section 3.2 #14 still described the Eze sheet as reading "wide of the LEFT post"; #17 quoted the 21 Sep QA count; #21 the 21 Sep V/C count; 2.2 said three thin entries not four; the QA check list omitted `missing-AUTHENTIC` and `missing-CANNOT-DETERMINE` (22 checks, not 20); the INFO count was six not five; two deep-file sizes were pre-edit; `psg-1`'s pack title and the scope of `whatifs` (three packs) were imprecise; 10.5 cited the wrong section for `clips.py` and listed Tah's window without saying it is not in the manifest; word counts mixed two counting methods. All corrected above.
- A stray word ("blocked.") in the PDF's Part One intro was removed.

The V/C history: 24 V / 20 C at the end of 21 Sep; **25 V / 19 C** after Michu on 22 Sep.

---

## APPENDIX — embedded-file manifest (path · bytes · sha256)

| File | Bytes | SHA-256 |
|---|---|---|
| `LXTHALFC-SYSTEM.md` | 28506 | `9894ad6406f8b4720b18b35d008d26ee06cba5e6f0bb8aeb7521d5f8f3894e4d` |
| `errors.md` | 16883 | `aac78651b5900cdb92ebe517cfd913681296e04b9286663138ea16be5d832ead` |
| `qa.py` | 14258 | `b7e91173486c7f2965cd0e18bee6761f657466a68186b3fd2662bbe21a189642` |
| `handover/SKILL-PROPOSED.md` | 29362 | `dd2f6139daff864f0c469a165365c98863662f64f17f5837cf7b619efccd2d4c` |
| `clips.py` | 7052 | `63bb123bb013140ba490095c3beddf290f4ebf182c5af3b6721fcbbbf80e98b2` |
| `LxthalFC-CLIP-MANIFEST.csv` | 7825 | `42c0686976d13b0a879a92cd68826b53fd55a9dfadf23caf05a11961eeb31b51` |
| `typeb.py` | 14935 | `0a19958a5040264362ce11a9f7531d2e742cf4c8b9df33f7630ead0cffdf8e59` |
| `handover/data.py` | 64432 | `789bdfa59d63be6da49aed2b3fdf22679c220f046a4851b92b40cf10c0fe19bf` |
| `handover/build_master.py` | 25506 | `62d131587e03d70aad9dae2123c0bb574c7af95918a0227d68b5d0b8c9624998` |
| `handover/final_packs.json` | 42237 | `31aac3dc3b3d1e9fe604accca63c5f634a43403e6a346d9efe1f0849f40859cd` |
| `notes-app.html` | 59589 | `6eb2e28d9ffb797eb0062d75abcfc274b801a41f03fa365af9e1f9578b1b9621` |
| `system-page.html` | 44838 | `30ef60a77f701051efc06727b9b53a9df8c0510267866e41987d6c7bf61d1a86` |
| `deep/acc-1-choupo.md` | 3397 | `0c1d49fdfe8ef990e7a8a9a3c1e72e7dc84292dc4317bfca5f07bd83f405c284` |
| `deep/acc-2-neuer.md` | 5689 | `3d2aad2a3564e2277b8df5adf913003295b926ac8b22af3be4f7e16c4c24c0fd` |
| `deep/acc-3-idk.md` | 4365 | `73ae2deb3e968cec8958d114e2c2112c9d5c8d1a94779a2d4a520fb7d1663172` |
| `deep/acc-4-no-look.md` | 3580 | `807ec267074607f7b55eb862010e88ff7fb10a65a143ab7c9b111bd07f801d58` |
| `deep/acc-5-full-reverse.md` | 3628 | `ab37dc500fa76735e31641aa730277e672b78bc0e9aa3cfc455a960509930c8d` |
| `deep/badge-1-ferland-mendy.md` | 3728 | `94446a4ee2805adda783566e64e63d0a0656ce6c2bd1215208d6f230a6d31a55` |
| `deep/badge-2-stones.md` | 5652 | `93b3ffcbddc022952afd1936b892b414c41c9ccf5ef9452027a4f3cadd8545de` |
| `deep/badge-3-sule.md` | 4076 | `99f6193a671f18cd5bd35fef4dd56d92b071e30417d44da46507f3ebbb210298` |
| `deep/badge-4-vandeven.md` | 4276 | `3f69dcab991c5a02f850aed2a8164e8496dc46430cf06b9b1dd7a41b4007a662` |
| `deep/badge-5-valverde.md` | 4611 | `21aa4ce61163f5c2614b0315c678969eee63b4cb49acf448c1b9ba981fea2dcd` |
| `deep/gk-assists-all.md` | 17432 | `a4c70dcbc820fe81267b11e850ab0e3afd9b0ffa4dea193d5a1f3d3e9c535b32` |
| `deep/oscar-2.md` | 23707 | `5ca5effee9e0f7877d0c63f477ffdff8b9c6162736a2b10e51b2fe3d824376b7` |
| `deep/pace-abuser-2.md` | 23539 | `22a4fe4475ea378682664cfbbaa77f0e9e3340d96e6828235c8c0238234d0dc8` |
| `deep/pace-abuser-son.md` | 5844 | `ab72807bd1940f4b5e14f744ca8a78494dc480a2693707c5e60bc1683003b7e8` |
| `deep/penalties.md` | 16251 | `88b72bafb28cd985c4badfb00104fcbaa8e32e47b5c1c8e1e3a32374db18f94a` |
| `deep/penalty-2-budimir.md` | 6039 | `256c38ae4a531ebdb0aead0a9ad6ac4862727b314ad24140ba97f3779b08fb20` |
| `deep/penalty-4-pires-henry.md` | 6332 | `f6fab97d3cc6d5b4aa054af585a2a864f6b892cdbf9df60702a57d5d9eefdf5c` |
| `deep/signature-moves.md` | 18571 | `f35e77a3849fbf1a42f9f453704a1fe5432049090e9e00870c38902268bac667` |
| `refaudit/GT-1mKJRDxU-THREE-PACKS.md` | 3189 | `2493407863159c80f969a03061d9404a86576d4a5266df403de8beddb4e1e805` |
| `refaudit/another-nation.md` | 2630 | `c72a1333030a833ec5726a64b31b678486abe8ced501e3fb05b6f0758a55316f` |
| `refaudit/lookalikes.md` | 2360 | `a93e0524b5dc362182b3234b8aec69a7da6ed434f9d31500e47d6cf202ecf0ac` |
| `refaudit/oscar-2.md` | 2718 | `34709416ae8d589a3e0ac2d7bd44030ecefb9aa983090bd80c47c3572a7cbbfd` |
| `refaudit/pace-abuser-2.md` | 1887 | `3d33cc693fa1f3124259a2724481b83d99bba2260b5044fb5b503eda813a34d7` |
| `refaudit/primes-redo.md` | 2247 | `4e054e1739b220a5194db8ff7942e8754ae1df7e882384b5863e5e6171cb8794` |
| `refaudit/psg-trio.md` | 2413 | `f4ca44ada15d690f7a3f535069a5a281d13c3c7e9ce76cb8abf7384a70786dbb` |
| `refaudit/ronaldo-stayed.md` | 2108 | `64cb3f230d944aac9bc3ecaebaa36d9059ed8b2c85d2f6c907740ce9fb6b35e1` |
| `refaudit/swap-nations.md` | 3176 | `7ca37da492cc4534a2411aef3f1a595e5479ebe2a74cc9a75f7e16e2e71d4608` |
| `refaudit/transfers-almost.md` | 3268 | `faccee38d523651495a3c38bd17ff91a25e7f15a75c0e58f25e4039815ddc1c9` |
| `queued.csv` | 13313 | `75fa6781e0361b8197c0c84d710a86084a0db7619bd0ada0ef1938fd1d21b21e` |
| `rejected.json` | 10623 | `7946832fc1ba1f89b2085b5879aafcde9d0fc25e9de08c3fdc89aa3887040207` |
| `dedup_base.json` | 5572 | `dbf5e2f4ae6ba70da3c8e8151589987eb659147203b2df497b8eaa9dc8dc3130` |
| `own.json` | 85299 | `9bc08df76b1f5893f599c5181b6918646c4e483cd2b1f6856a414d53af890293` |
| `score_engine.py` | 1935 | `c76c86060b43986f45a929d3fcde05e7312c4e50d1676dba3765444cbf2fb9fd` |
| `prompts/ai-studio-prompt.md` | 4562 | `9335c6737e9aefe3fb1be46d95ff9d82d4aff25089a560e89e75fb1758da3b0d` |
| `scratchpad/test.mjs` | 1815 | `88325e88820f9bfac6d7d93831ce042f15aafe87757bc69f6e2487a831158ea8` |
| `scratchpad/shot.mjs` | 750 | `7ccde1dca73065f4b4b1fabd5b5453a16d69330cc53623278589c15a06167dda` |
| `~/.claude/skills/synced/…/lxthalfc-picker/SKILL.md` | 26210 | `750b51d227a71cd8a583fb1cdb3465588701fe523e5bfebfdac5be7a8ef2500a` |
| `handover/hx/regen_packs.mjs` | 668 | `bedf41f65c32f0859ae0c6ef32eeab206ab70c2a719c10f998fc0fb6dc649964` |

50 files · 692883 bytes embedded.

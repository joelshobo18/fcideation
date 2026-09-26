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

### E25 — Four of nineteen comment-sourced facts were wrong, and "DISPUTED" sat on a closable question for five days
WHAT: Verifying the 19 C (FROM COMMENTS) Type B picks on 26 Sep found four lines that would have been
 spoken wrong: Henry/Juventus "Arsenal bought him for LESS than Juventus paid" (false — ~£11m vs £10.5m,
 Arsenal paid slightly more); Félix "most expensive teenager ever" (second, behind Mbappé) and "Saudi
 league at 26" (25); Dele "out of football" (a free agent trying to return, not retired); De Gea "the
 infamous fax" (the record says paperwork reached La Liga minutes after midnight, each club blaming the
 other). Separately, Eze's penalty had been left DISPUTED since 21 Sep on one text source vs three vision
 passes; a proper search found UEFA.com, Arsenal.com, PSG's Opta commentary and Wikipedia all saying WIDE
 (two say left), none over the bar — the vision passes were wrong. The clip-manifest CSV also went stale
 when clips.py changed, and nothing checked it.
WHY: C picks were shipped with an INFO line on the theory that comment-sourced facts are "probably right".
 Superlatives, comparisons and ages are exactly where memory and comments drift. On Eze, "DISPUTED" was
 treated as an end state instead of a to-do: the source search that closes it took one agent two minutes.
RULE: A C marker is a queue, not a status — clear it before the batch ships. Superlatives ("most", "first",
 "ever"), comparisons ("less than", "more than") and ages are verified FIRST. A DISPUTED outcome gets a
 multi-source search (governing body, both clubs, Opta/match centre, a major outlet) before it is allowed
 to stay disputed. Any derived file (CSV, JSON, PDF) is regenerated in the same step as its source.
FIX: 18 of 19 C picks flipped to V with written sources (typeb.py 43 V / 1 C / 1 unmarked — Henry's
 "two pronunciations" has no written source and stays C with a "show footage or drop it" note; the
 unmarked row is swap-nations #1, an argument rather than a fact). Corrections propagated to typeb.py, data.py,
 notes-app.html, final_packs.json (regenerated), refaudit untouched (historical reasoning). Eze RESOLVED
 WIDE LEFT across deep/penalties.md, data.py, clips.py, the CSV, build_master.py and the app. New QA check
 `manifest-stale` compares LxthalFC-CLIP-MANIFEST.csv row by row with clips.py and FAILS on drift — proven
 to fire on the pre-fix CSV.
STAGE: 5 (verify), 7 (assemble), 9.5 (QA). Pattern 1 (background knowledge under the claim) — and a
 sixth, now named: 6. "Flagged" is not "done" — a C marker or a DISPUTED label is a queue to clear, not a state to ship.

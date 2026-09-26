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

# -*- coding: utf-8 -*-
# Builds LxthalFC-Scriptwriter-Handbook-v4.pdf from the v3 text plus the v4 additions below.
# v3 body text is parsed from handbook-v3.txt (pdftotext -layout of the v3 PDF); v3's own NEW tags are
# dropped and only v4 additions are tagged. Run: python3 build_v4.py
import re, os
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.colors import HexColor
from reportlab.platypus import (BaseDocTemplate, PageTemplate, Frame, Paragraph, Spacer, Table,
                                TableStyle, KeepTogether, PageBreak)
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

HERE = os.path.dirname(os.path.abspath(__file__))
D = "/usr/share/fonts/truetype/dejavu/"
pdfmetrics.registerFont(TTFont("DJ", D + "DejaVuSans.ttf"))
pdfmetrics.registerFont(TTFont("DJB", D + "DejaVuSans-Bold.ttf"))
pdfmetrics.registerFont(TTFont("DJM", D + "DejaVuSansMono.ttf"))

RED, INK, GREY, GREEN, LINE, SOFT = (HexColor(c) for c in
    ("#b0182f", "#1c1c1c", "#6b6b6b", "#1f7a3a", "#d6d6d6", "#f4f4f2"))
TAG = '<font name="DJB" size="6.5" color="#1f7a3a">NEW v4</font> '

S = {
 "h1": ParagraphStyle("h1", fontName="DJB", fontSize=24, leading=28, textColor=INK, spaceAfter=6),
 "intro": ParagraphStyle("intro", fontName="DJ", fontSize=8.8, leading=12.2, textColor=GREY, spaceAfter=10),
 "h2": ParagraphStyle("h2", fontName="DJB", fontSize=13.5, leading=17, textColor=RED, spaceBefore=10, spaceAfter=5),
 "h3": ParagraphStyle("h3", fontName="DJB", fontSize=9.6, leading=13, textColor=INK, spaceBefore=5, spaceAfter=3),
 "p": ParagraphStyle("p", fontName="DJ", fontSize=8.8, leading=12.2, textColor=INK, spaceAfter=4),
 "b": ParagraphStyle("b", fontName="DJ", fontSize=8.8, leading=12.2, textColor=INK, leftIndent=11,
                     bulletIndent=1, spaceAfter=2.5),
 "cell": ParagraphStyle("cell", fontName="DJ", fontSize=8.2, leading=10.8, textColor=INK),
 "cellb": ParagraphStyle("cellb", fontName="DJB", fontSize=8.2, leading=10.8, textColor=INK),
 "mono": ParagraphStyle("mono", fontName="DJM", fontSize=7.6, leading=10.2, textColor=INK),
 "box": ParagraphStyle("box", fontName="DJ", fontSize=8.8, leading=12.2, textColor=INK),
}

def esc(t):
    return t.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

# ---------------------------------------------------------------- parse v3
SUBHEADS = ["Type A — Clip / moment videos", "Type B — Facts / stats / list videos",
            "Name / story lists (no number in the title)", "Step 1 — Moment-focus or player-focus?",
            "Step 2 — Finding the clip", "Step 3 — Picking the best version",
            "Step 4 — Struggling? / Step 5 — Last resort"]

def parse_v3():
    raw = [l.rstrip() for l in open(os.path.join(HERE, "handbook-v3.txt"), encoding="utf-8")]
    raw = [l for l in raw if not l.strip().startswith("LxthalFC Scriptwriter Handbook v3 —")]
    secs, cur = {}, None
    for l in raw:
        m = re.match(r"^(\d{1,2})\. (\S.*)$", l)
        if m and 1 <= int(m.group(1)) <= 15 and not l.startswith("1. Are"):
            n = int(m.group(1)); cur = {"title": m.group(2), "lines": []}; secs[n] = cur; continue
        if l.startswith("Appendix A"): cur = None
        if cur is not None: cur["lines"].append(l)
    out = {}
    for n, s in secs.items():
        if n == 13: continue            # checklist is rebuilt by hand below
        items, para = [], None
        lines = s["lines"]
        if n == 12:                     # cut section 12 before the checklist
            lines = lines[:next(i for i, l in enumerate(lines) if "Pre-Submission" in l) ] if any(
                "Pre-Submission" in l for l in lines) else lines
        for l in lines:
            st = l.strip()
            if not st: para = None; continue
            if st in SUBHEADS: items.append(["h3", st]); para = None; continue
            if st.startswith("•"):
                items.append(["b", st[1:].strip()]); para = None; continue
            if l.startswith("  ") and items and items[-1][0] == "b":
                items[-1][1] += " " + st; continue
            if para is not None: para[1] += " " + st
            else: para = ["p", st]; items.append(para)
        for it in items:
            it[1] = re.sub(r"(^|(?<=\. ))NEW\s+", "", it[1])
        out[n] = {"title": s["title"], "items": items}
    return out

# ---------------------------------------------------------------- v4 additions
# (section, anchor substring of an existing v3 item or None for end of section, kind, text)
ADD = [
 # 2 — Type B and name lists
 (2, "Lists must follow reality", "b",
  "Shortlist on virality, order on the numbers. Pick the 5 from viral candidates first (the fastest goal "
  "isn't always the viral one: Gündoğan's was), then put those 5 in chronological or numeric order. "
  "Virality decides who is in; the numbers decide where they sit."),
 (2, "Prefer recent, renowned players", "b",
  "Every name list needs at least one rage-bait pick: a player who didn't win the Ballon d'Or, or a team "
  "that is good but not great, placed at #4. A list of only obvious winners “can't be trusted” and gives "
  "nobody anything to argue about. Space it per Section 3."),
 (2, "Prefer recent, renowned players", "b",
  "The premise must be true of every name. “Forgotten” means actually forgotten: nobody has forgotten Messi, "
  "and nobody is talking about Pogba right now. Don't take names from viral videos that already show these "
  "players together; that defeats the point of the video."),
 (2, "Once viral references are exhausted, use Claude", "b",
  "Claude on name lists is a last resort, not a shortcut. Search YouTube first (exact title, then rotated "
  "keywords), and when you do use Claude, write in the explanation that you did and why no reference "
  "existed. Joel rejected name lists on 23 Sep that went straight to Claude."),
 # 3 — Viral formula
 (3, "Space out bait / wrong picks", "b",
  "Vary the picks. Never two players from the same club back to back (two Real Madrid players in a row "
  "was sent back), never three players in the same position in a row (three defenders “gets repetitive "
  "for the viewer”), and never two versions of the same technique in one video (a chip and a Panenka)."),
 (3, "When the notes give a joke pick", "b",
  "#2 still needs a reason to be in the video. “It's the least engaging” is where it sits, not why it's "
  "there. Joel stopped accepting that line on 23 Sep."),
 # 4 — Sourcing
 (4, "Safest play:", "b",
  "Narrow topic or wide topic? Narrow (one player, one match, one named trend): take the best 5 from the one "
  "viral reference and reorder. Wide (a whole category: smartest moments, disrespectful goals, best "
  "throws, Puskás-level goals): shortlist 15–20 from at least three viral references plus “top 5/top 10” "
  "searches, then pick the best 5. For a wide topic “each vid should be a banger”; one reference's five is "
  "not the best five."),
 (4, "Safest play:", "b",
  "Stay on the reference's theme. If the viral reference is about one player, every pick is about that "
  "player."),
 (4, "Think like the editor", "b",
  "Every link must open. A private or deleted video can't be approved. If a video is region-locked, say "
  "“UK VPN” next to it."),
 # 6 — Title
 (6, "Fails = moments", "b",
  "Smart / 200 IQ = a clever decision on the pitch. A header, a cross or a normal finish is not smart. "
  "Accidental = the player didn't mean it. A skill he chose to do is not an accident."),
 (6, "Fails = moments", "b",
  "“Right now” and current titles: check every player's current club and this season's status before writing "
  "(“he's no longer at Man City”). Anything older than the last 1–2 seasons needs a reason to be there "
  "(“too old”)."),
 # 8 — AI
 (8, "You decide. AI assists.", "b",
  "Type A in one line: Claude is for player and team names only. Never the picks, never the proven hook, "
  "never the order, never what happens in the clip. Joel on 23 Sep: “you dont use claude for these type of "
  "videos. period. only for player names.”"),
 (8, "Claude can't open links", "b",
  "AI invents moves. Rainbow flicks, fake passes and backheels that weren't in the clip all came from AI "
  "descriptions. If a move isn't clearly visible, don't name it."),
 # 9 — Descriptions
 (9, "A club never plays a nation", "b",
  "Check the kit before you name the match. Ronaldo in an Al Nassr shirt is not Portugal; Leeds v Newcastle "
  "is not Brazil. The kit is the quickest proof of team, era and competition."),
 (9, "Don't miss the beat", "b",
  "Describe the thing the title is about, specifically. Say which gesture it was (hands together in prayer, "
  "a finger to the lips) and how the run-up went (a stutter). Describe the dance when the dance is the "
  "moment. “Not good enough” came back on every description that stayed vague."),
 # 11 — Explanations
 (11, "Paste the comments you relied on", "b",
  "If a comment is your reason, paste the comment and its likes. “It's mentioned in the comments” with no "
  "comment pasted counts as no explanation."),
 # 12 — Process
 (12, "Check your own work before submitting", "b",
  "The checklist line goes under every video (template in Appendix C). Joel skips any video without it. "
  "Between 10 and 23 Sep no video in the doc had one, and 59 comment threads from that period are still open."),
 (12, "Check your own work before submitting", "b",
  "Clean the video up before you submit: no leftover drafts, old clips, stray references or notes to "
  "yourself. A messy entry can't be reviewed (“just clean vid up so I can review properly”)."),
 # 14 — Failures
 (14, None, "b", "Same club, same position or same technique back to back."),
 (14, None, "b", "No rage-bait pick in a name list; premise not true of every name."),
 (14, None, "b", "Claude used on a Type A video after v3 said not to."),
 (14, None, "b", "Checklist line missing, so the same mistakes reach review again."),
]

def apply_additions(secs):
    for n, anchor, kind, text in ADD:
        items = secs[n]["items"]
        new = [kind, TAG + esc(text), True]
        if anchor is None:
            items.append(new); continue
        idx = [i for i, it in enumerate(items) if anchor in it[1]]
        assert idx, (n, anchor)
        i = idx[0] + 1
        while i < len(items) and len(items[i]) > 2: i += 1   # keep several additions in order
        items.insert(i, new)
    return secs

# ---------------------------------------------------------------- checklist (13)
CHECK = [
 ("BEFORE SEARCHING", [
  ("I read all new comments on every week, replied to each, and did revisions before starting this video.", 0),
  ("I have decided if this is Type A (clip → viral formula), Type B (facts/numbers → chronological/numeric) or a Name/story list.", 0),
  ("I have defined the key word in the title (tournament, leagues, legends, primes, smart, accidental, etc.) and it matches what I made.", 0),
  ("I have read the Notes field and followed every instruction in it (including “use Claude”).", 0),
  ("I searched the exact title on YouTube first and watched the full reference video.", 0),
  ("I decided whether the topic is narrow (one reference) or wide (three or more references, 15–20 shortlisted).", 1)]),
 ("SOURCING", [
  ("Every reference is viral (100k+ views, ideally 500k+), about the title, and linked in the reference section. I judged videos on views, not likes.", 0),
  ("I sourced from Shorts where possible; any long-form clip has link + timestamp next to it.", 0),
  ("Every clip is a banger. I did not fill a slot with a weak clip — if I couldn't find one, I asked Joel.", 0),
  ("The most recent edition / current season is included where the title needs it, and every player's current club is right.", 1),
  ("Every link opens (none private or deleted); region-locked ones say “UK VPN”.", 1),
  ("The editor can realistically find and clean every clip (no heavy watermarks, grain, pop-ups, or too-old footage).", 0)]),
 ("ORDER", [
  ("Type A: #5 is a proven hook from the start of the most viral reference, not a comment pick. If not, the reason is in the explanation.", 0),
  ("Type A: proven hooks were weighed before comments; comment-based picks sit at #4/#3; #1 is a notable #1, not just “the best”.", 0),
  ("Type A: bait picks are spaced out; Messi and Ronaldo are not together at the start.", 0),
  ("No same club, same position or same technique back to back.", 1),
  ("Name lists: at least one rage-bait pick, and the title's premise is true of every name.", 1),
  ("Type B: shortlisted on virality, then ordered chronologically or numerically, starting at 5, in the direction the notes say, following real editions.", 0),
  ("I did not copy the reference's exact order without a reason, and I didn't reorder because commenters asked.", 0)]),
 ("DESCRIPTIONS", [
  ("Every entry is Player vs Team. The video's subject player is named in every clip.", 0),
  ("No “unnamed”, “unknown”, “vs opponent”, kit colours, or “stats unavailable”.", 0),
  ("No club vs nation, no wrong match, no player who wasn't there that year. Every fact checked, including the kit against the match.", 0),
  ("Each description serves the title, includes the key beat, and says where on the pitch / which part of the goal.", 0),
  ("Terminology is correct: nutmeg, touch, corner, box, intercept, dummy. “Kick” not used. Any term I was unsure of, I looked up. No move named that isn't clearly in the clip.", 0),
  ("Simple English in Joel's reading tone, no tangents, no suggestions or notes to Joel inside the description.", 0),
  ("Requested stats, years/seasons, left/right are included where asked or needed.", 0)]),
 ("EXPLANATIONS", [
  ("One full-phrase line per number, with data (reference views, comment text + likes, or ordering rule). #2 says why it is in the video.", 0),
  ("The explanations are my reasoning, not pasted from AI, and say why each clip is IN the video.", 0),
  ("I stated where and how I used AI on this video. On a Type A video, only for names.", 0)]),
 ("BEFORE SUBMITTING", [
  ("No duplicate clips, no blank sections, no leftover drafts, spelling checked, every word intentional.", 0),
  ("Template followed; parts separated as X.1, X.2 if needed; checklist line pasted under the video.", 0),
  ("Highlight/reference links are correct (source links added after approval per the SOP).", 0),
  ("I checked my other pending videos for any mistake Joel corrected this week.", 0),
  ("I have added anything new I learned to my notes doc.", 0)]),
]

TEMPLATE = """Video [no.]
Title - [title] (anray)
Type - A (viral formula) / B (chronological or numeric) / Names
Clips
5. [Player] vs [Team], [year] - [second-by-second description] [clip link + timestamp]
4. ...
3. ...
2. ...
1. ...
Reference Videos (viral only, views next to each):
Explanation of Each Clip Selected:
Number 5: [full sentence + data]
Number 4: [full sentence + data, paste the comment and its likes]
Number 3:
Number 2: [why it is IN the video]
Number 1:
AI used for: [nothing / names / list / dates / grammar]
Checklist: all [n] passed / failed: [which]
Audio File -
Notes -
Script Approval Time -
Video Highlight Links for Clips Selected (after approval):
Number 5:
Number 4:
Number 3:
Number 2:
Number 1:
Rough Script (refer to this when fixing subtitles)"""

CHECKLINE = ("Checklist: type decided · title key word defined · notes followed · exact title searched · "
             "references viral + linked · every clip a banger · links open · #5 proven hook (A) / real "
             "chronology (B) · no same club/position/technique back to back · rage-bait in name lists · "
             "Player vs Team everywhere · kit checked · terms checked · one sentence + data per number · "
             "AI use stated · no leftovers · other pending videos checked")

# ---------------------------------------------------------------- render
def bullets(items):
    F = []
    for it in items:
        kind, text = it[0], it[1]
        body = text if len(it) > 2 else esc(text)
        if kind == "h3": F.append(Paragraph(body, S["h3"]))
        elif kind == "p": F.append(Paragraph(body, S["p"]))
        else: F.append(Paragraph(body, S["b"], bulletText="•"))
    return F

def build():
    secs = apply_additions(parse_v3())
    out = os.path.join(HERE, "LxthalFC-Scriptwriter-Handbook-v4.pdf")
    W, H = A4; M = 42
    def footer(c, d):
        c.saveState(); c.setFont("DJ", 7); c.setFillColor(GREY)
        c.drawString(M, 24, "LxthalFC Scriptwriter Handbook v4 — 26 Sept 2026")
        c.drawRightString(W - M, 24, f"Page {d.page}"); c.restoreState()
    doc = BaseDocTemplate(out, pagesize=A4, leftMargin=M, rightMargin=M, topMargin=40, bottomMargin=44,
                          title="LxthalFC Scriptwriter Handbook v4", author="LxthalFC")
    doc.addPageTemplates([PageTemplate(frames=[Frame(M, 44, W - 2 * M, H - 84, id="f")], onPage=footer)])
    F = [Paragraph("LxthalFC Scriptwriter Handbook v4", S["h1"]),
         Paragraph("Updated 26 Sept 2026. Replaces v3 (10 Sept) and everything before it. v4 keeps every v3 "
                   "rule and adds what Joel wrote in the doc comments from 10 to 23 Sept: 111 comment threads, "
                   "59 still open when this was written. Lines tagged " + TAG +
                   "are the additions. Almost every open comment repeats a rule v3 already had, so the biggest "
                   "change is Appendix C: the checklist now goes under every video, and Joel skips any video "
                   "without it. Keep this open next to you for every video.", S["intro"])]
    for n in range(1, 16):
        if n == 13:
            F += checklist(); continue
        s = secs[n]
        F.append(Paragraph(f"{n}. {esc(s['title'])}", S["h2"]))
        F += bullets(s["items"])
    F += appendices()
    doc.build(F)
    return out

def checklist():
    F = [Paragraph("13. Pre-Submission Checklist", S["h2"]),
         Paragraph("Any “No” = do not submit. Fix it first. Joel does not review videos that haven't passed "
                   "this. Go through it in full for every video, then paste the one-line version from "
                   "Appendix C under the video to show you did.", S["p"]),
         Paragraph("Video no.: ________   Title: ______________________________   Type: A / B / Names   "
                   "Date: ________", S["p"])]
    rows = [[Paragraph("Check", S["cellb"]), Paragraph("Yes", S["cellb"]), Paragraph("No", S["cellb"])]]
    style = [("GRID", (0, 0), (-1, -1), 0.4, LINE), ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
             ("BACKGROUND", (0, 0), (-1, 0), SOFT), ("TOPPADDING", (0, 0), (-1, -1), 3),
             ("BOTTOMPADDING", (0, 0), (-1, -1), 3)]
    for head, items in CHECK:
        r = len(rows)
        rows.append([Paragraph(head, S["cellb"]), "", ""])
        style += [("SPAN", (0, r), (-1, r)), ("BACKGROUND", (0, r), (-1, r), SOFT)]
        for text, new in items:
            rows.append([Paragraph((TAG if new else "") + esc(text), S["cell"]), "", ""])
    W = A4[0] - 84
    t = Table(rows, colWidths=[W - 60, 30, 30], repeatRows=1); t.setStyle(TableStyle(style))
    F.append(t)
    F.append(Spacer(1, 8))
    F.append(KeepTogether([Paragraph("Joel's 8 questions before you send any pack", S["h3"]),
        Paragraph("1. Are the selected clips actually relevant to the topic? 2. Are they strong enough for the "
                  "video? 3. Do the descriptions clearly explain what happens? 4. Do they match the clip "
                  "accurately? 5. Is the ranking/order optimised? 6. Are the highlight/reference links correct? "
                  "7. Have you followed all notes on the doc? 8. Have you applied feedback from previous "
                  "scripts?", S["p"]),
        Paragraph("Signed off by scriptwriter: ______________________   AI used for: "
                  "______________________________", S["p"])]))
    return F

def appendices():
    F = [PageBreak(), Paragraph("Appendix A — Role terms (from 3 Aug message)", S["h2"])]
    for t in [
     "Pay: $4 per approved script pack. Workload: 3–5 approved packs per day depending on posting volume "
     "(minimum 5 new scripts/day currently expected).",
     "A full approved pack: 7–10 clips researched, final 5 selected, correct order 5 → 1, clear description of "
     "each clip, source link for each clip, title/topic included, ready for scripting/editing.",
     "Approved only if clips are strong, the final 5 make sense, the order fits the format, descriptions are "
     "clear, and source links are included. Weak clips, vague descriptions, or missing links = revise before "
     "it counts.",
     "Examples: 4/day × 30 = 120 packs = $480; 5/day × 30 = 150 packs = $600 before bonuses. Realistic with "
     "normal bonuses ~$700/month; up to ~$900–1,000 with high workload and strong performance."]:
        F.append(Paragraph(esc(t), S["b"], bulletText="•"))
    rows = [["YouTube Shorts views (7 days after posting)", "Bonus"], ["100k", "$1"], ["250k", "$3"],
            ["500k", "$5"], ["1M", "$10"], ["2M+", "$20"]]
    t = Table([[Paragraph(a, S["cellb" if i == 0 else "cell"]), Paragraph(b, S["cellb" if i == 0 else "cell"])]
               for i, (a, b) in enumerate(rows)], colWidths=[260, 80])
    t.setStyle(TableStyle([("GRID", (0, 0), (-1, -1), 0.4, LINE), ("BACKGROUND", (0, 0), (-1, 0), SOFT)]))
    F += [Spacer(1, 4), t, Spacer(1, 6)]
    for t in [
     "Bonuses: YouTube Shorts views only; highest tier only, no stacking; only when your approved pack was used. "
     "A different idea, different clips, or a completely different order may void the bonus.",
     "Pay period: work approved between payment dates is paid on the next one. Payment date: the first Sunday "
     "after the 15th of each month; bonuses paid on the next date after they're confirmed.",
     "Reviewed on quality, speed, consistency, usability of packs, and account performance.",
     "Repeated errors that waste review time may lead to penalties (Section 12)."]:
        F.append(Paragraph(esc(t), S["b"], bulletText="•"))

    F.append(Paragraph("Appendix B — Essential football terms", S["h2"]))
    F.append(Paragraph("Learn these first. Skills: nutmeg, elastico, step-over, La Croqueta, roulette, Cruyff "
        "turn. Shots: trivela, rabona, knuckleball, chip, Panenka, bicycle kick. Passing: through ball, killer "
        "pass, no-look pass, reverse pass, line-breaking pass. Movement: overlap, underlap, run in behind, "
        "blindside run, decoy run. Tactics: counterattack, high press, low block, counter-press, overload, "
        "half-space. Positions: Number 6, Number 8, Number 10, false 9, winger, wing-back. Script vocabulary: "
        "worldie, screamer, clinical, cooked, sent, pocketed, silky, outrageous, unplayable.", S["p"]))
    TERMS = [
     ("Skill moves", "Nutmeg, elastico, step-over, La Croqueta, roulette, Cruyff turn, heel-to-heel, rainbow flick, fake shot, body feint, drag-back, ball roll"),
     ("Shooting", "Trivela, rabona, knuckleball, finesse shot, power shot, chip, dink, Panenka, volley, half-volley, bicycle kick, backheel"),
     ("Finishing", "Clinical finish, first-time finish, tap-in, near-post / far-post finish, round the keeper, slot it home, bury it"),
     ("Goal descriptions", "Screamer, worldie, banger, thunderbolt, wondergoal, solo goal, late winner"),
     ("Passing", "Through ball, killer pass, no-look pass, reverse pass, trivela pass, one-two, layoff, switch of play, line-breaking pass, weighted pass"),
     ("Crossing", "Whipped, driven, floated, low, cut-back, early, back-post cross"),
     ("First touch", "First touch, cushion touch, chest control, trap, half-turn, take it in stride, kill the ball"),
     ("Heading", "Header, diving header, bullet header, glancing header, flick-on"),
     ("Goalkeeping", "Save, reflex save, parry, smother, punch, claim, rush off the line, clean sheet"),
     ("Defending", "Tackle, slide tackle, interception, block, clearance, jockey, press, mark, recovery tackle"),
     ("Defensive mistakes", "Blunder, howler, ball-watching, lost his man, caught sleeping, overcommitted, caught in possession"),
     ("Attacking movement", "Run in behind, overlap, underlap, blindside run, diagonal run, decoy run, late run, drop deep, attack the space"),
     ("Beating a defender", "Take on, skip past, burst past, skin, cook, send, sit down, wrong-foot, leave for dead"),
     ("Pace", "Pace, acceleration, burst, sprint, change of pace, recovery speed"),
     ("Possession", "Keep possession, build-up, recycle, progress the ball, carry the ball, control the tempo"),
     ("Attacking tactics", "Counterattack, transition, overload, isolation, combination play, link-up play, width, half-space, between the lines"),
     ("Defensive tactics", "Low block, high press, counter-press, high line, offside trap, man marking, zonal marking, compactness"),
     ("Areas", "Half-space, channel, pocket, final third, Zone 14, six-yard box, edge of the box, near post, back post"),
     ("Set pieces", "Free kick, corner, penalty, throw-in, short corner, inswinger, outswinger"),
     ("Free kicks", "Knuckleball, curler, dipping, trivela, under-the-wall free kick"),
     ("Penalties", "Panenka, stutter-step, send the keeper the wrong way, penalty shootout"),
     ("Fouls", "Tactical foul, professional foul, late challenge, handball, high boot, yellow card, red card"),
     ("Offside", "Offside, onside, offside trap, beat the offside trap, time the run"),
     ("Midfield roles", "Number 6, Number 8, Number 10, box-to-box, defensive midfielder, deep-lying playmaker, playmaker, pivot"),
     ("Attacking roles", "Striker, centre-forward, Number 9, false 9, target man, poacher, winger, inside forward"),
     ("Defensive roles", "Centre-back, full-back, wing-back, ball-playing defender, sweeper, sweeper-keeper"),
     ("Physical play", "50/50, aerial duel, shoulder-to-shoulder, shield the ball, outmuscle, hold off"),
     ("Flair", "Flair, showboating, tekkers, silky, filthy, audacious, outrageous"),
     ("Slang", "Megged, skinned, cooked, sent, pocketed, top bins, banger, worldie, bottled it"),
     ("Misses", "Sitter, open-goal miss, skied it, dragged wide, scuffed it, hit the post, hit the bar"),
     ("Match terms", "Equaliser, winner, opener, comeback, clean sheet, added time, extra time"),
     ("Performance", "Masterclass, unplayable, clinical, composed, dominant, ran the show, pocketed, disasterclass"),
     ("Technical", "Close control, vision, composure, press resistance, scanning, ball progression, chance creation, final ball, weight of pass"),
     ("Stats", "Big chance, shot on target, assist, key pass, xG, xA, goal contribution, progressive pass, progressive carry")]
    W = A4[0] - 84
    t = Table([[Paragraph(a, S["cellb"]), Paragraph(b, S["cell"])] for a, b in TERMS],
              colWidths=[110, W - 110], repeatRows=0)
    t.setStyle(TableStyle([("GRID", (0, 0), (-1, -1), 0.4, LINE), ("VALIGN", (0, 0), (-1, -1), "TOP"),
                           ("TOPPADDING", (0, 0), (-1, -1), 2.5), ("BOTTOMPADDING", (0, 0), (-1, -1), 2.5)]))
    F.append(t)

    F += [PageBreak(), Paragraph("Appendix C — Doc template with the checklist line " + TAG, S["h2"]),
          Paragraph("Replace the Template section of the LxthalFC Scripts doc with this. Three fields are new "
                    "against the old template: <b>Type</b>, <b>AI used for</b> and <b>Checklist</b>. Clip links "
                    "sit next to each clip; the reference section is for viral references only.", S["p"])]
    tb = Table([[Paragraph(esc(TEMPLATE).replace("\n", "<br/>"), S["mono"])]], colWidths=[W])
    tb.setStyle(TableStyle([("BOX", (0, 0), (-1, -1), 0.5, LINE), ("BACKGROUND", (0, 0), (-1, -1), SOFT),
                            ("LEFTPADDING", (0, 0), (-1, -1), 8), ("TOPPADDING", (0, 0), (-1, -1), 7),
                            ("BOTTOMPADDING", (0, 0), (-1, -1), 7)]))
    F += [tb, Spacer(1, 8), Paragraph("The one-line checklist (paste under the video, then write "
          "“all passed” or name what failed)", S["h3"])]
    tc = Table([[Paragraph(esc(CHECKLINE), S["box"])]], colWidths=[W])
    tc.setStyle(TableStyle([("BOX", (0, 0), (-1, -1), 0.8, GREEN), ("LEFTPADDING", (0, 0), (-1, -1), 8),
                            ("TOPPADDING", (0, 0), (-1, -1), 6), ("BOTTOMPADDING", (0, 0), (-1, -1), 6)]))
    F += [tc, Spacer(1, 8),
          Paragraph("The line is a promise that you went through Section 13 in full, not a substitute for it. "
                    "A video whose line says “all passed” and then fails one of these gets sent back whole.",
                    S["p"])]
    return F

if __name__ == "__main__":
    print(build())

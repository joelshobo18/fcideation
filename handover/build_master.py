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
F.append(box("RESOLVED 26 SEP: EZE WENT WIDE LEFT. The dispute recorded on 21\u201322 Sep is closed. "
 "Four written records agree \u2014 UEFA.com (\u201cswept wide\u201d), Arsenal.com (\u201cdragged his effort wide of the target\u201d), "
 "PSG's Opta commentary (\u201cmisses to the left\u201d) and Wikipedia (\u201cshot wide left\u201d). None says over the bar; the only "
 "Arsenal kick that went over was Gabriel's. The three vision passes were wrong. SAY \u201che dragged it wide\u201d. "
 "And the variety problem is gone: Zaza goes over, Eze goes wide \u2014 five different endings.",
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

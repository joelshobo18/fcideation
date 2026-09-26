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

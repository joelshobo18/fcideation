# LxthalFC — September batch workspace

Restored from `HANDOFF.md` (2026-09-22). All 50 embedded files split out and SHA-256 verified.

Scripts hardcode `/root/lx`; point it at this checkout first:

    ln -sfn "$PWD" /root/lx
    pip install --break-system-packages reportlab
    apt-get install -y fonts-dejavu-extra poppler-utils
    (cd handover && python3 build_master.py)   # -> LxthalFC-September-SENDOFF.pdf (84 pp)
    python3 qa.py                              # expect 592 passed · 7 warnings · 0 failures

Start with `HANDOFF.md` §1–5 and §9, then `LXTHALFC-SYSTEM.md` and `errors.md`.
`synced-skill/` is a copy of the live v1.0 skill for reference; `handover/SKILL-PROPOSED.md` is the unsaved v1.1.

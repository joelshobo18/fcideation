// Regenerate handover/final_packs.json from notes-app.html's PACKS (tags stripped, <br> → space)
import fs from 'fs';
const s = fs.readFileSync('/root/lx/notes-app.html','utf8');
const m = s.match(/const PACKS = (\[[\s\S]*?\n\]);\n\nconst DECISIONS/);
const P = eval(m[1]);
const strip = t => (t||'').replace(/<br\s*\/?>/g,' ').replace(/<[^>]+>/g,'').replace(/\s+/g,' ').trim();
const out = P.map(p => ({id:p.id, title:p.title, state:p.state, meta:p.meta, picks:p.picks.map(r => r.map(strip)), subs:p.subs, note:strip(p.note)}));
fs.writeFileSync('/root/lx/handover/final_packs.json', JSON.stringify(out, null, 1) + '\n');
console.log(out.length, 'packs written');

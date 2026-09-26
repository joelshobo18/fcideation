import { chromium } from 'playwright';
const b = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium' });
const p = await b.newPage({viewport:{width:390,height:800}});
const errs = []; p.on('pageerror', e => errs.push(e.message)); p.on('console', m => { if (m.type()==='error' && !/fonts\.g/.test(m.text())) errs.push(m.text()); });
await p.addInitScript(() => { const store = {}; const subs = [];
  window.claude = { use: async n => n!=='db'?null:{ doc: path => ({ set: async d => { store[path]=d; subs.forEach(f=>f()); } }),
    collection: c => ({ onSnapshot: next => { const fire=()=>next({docs:Object.entries(store).filter(([k])=>k.startsWith(c+'/')).map(([k,v])=>({id:k.split('/')[1],data:()=>v}))}); subs.push(fire); fire(); return ()=>{}; } }) } };
  window.__store = store; });
await p.goto('file:///home/user/fcideation/notes-app.html'); await p.waitForTimeout(500);
const body = await p.textContent('body');
console.log('cards', await p.locator('.card').count(), '| panel:', (await p.textContent('.dpanel h2')).trim());
for (const s of ['Sixteen packs','dragged WIDE LEFT','about £11m','Saudi league at 25','PAPERWORK REACHED LA LIGA','England, France, Nigeria, Algeria']) console.log(body.includes(s)?'OK ':'MISSING ', s);
for (const s of ['DISPUTED','less than Juventus','infamous fax','Seventeen']) console.log(body.includes(s)?'STALE ':'gone ', s);
await p.fill('#n-penalty-2','test'); await p.waitForTimeout(1000);
console.log('note saved:', JSON.stringify(await p.evaluate(()=>window.__store['notes/penalty-2']?.note)), '|', await p.textContent('#saveline'));
console.log('hscroll:', await p.evaluate(()=>document.documentElement.scrollWidth>innerWidth));
console.log(errs.length?errs.join('\n'):'no JS errors'); await b.close();

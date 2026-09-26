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

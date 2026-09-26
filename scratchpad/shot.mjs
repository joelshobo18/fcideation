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

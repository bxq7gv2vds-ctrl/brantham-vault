import { chromium } from 'playwright';
import { fileURLToPath } from 'url';
import path from 'path';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const files = [
  'post-01-top5-secteurs.html',
  'post-02-checklist-rj.html',
  'post-03-vrai-prix.html',
];

const browser = await chromium.launch();
const ctx = await browser.newContext({
  viewport: { width: 1080, height: 1080 },
  deviceScaleFactor: 2,
});
const page = await ctx.newPage();

for (const f of files) {
  const url = 'file://' + path.join(__dirname, f);
  await page.goto(url, { waitUntil: 'networkidle' });
  await page.waitForTimeout(800); // ensure web fonts settle
  const card = await page.locator('.post').first();
  const out = path.join(__dirname, f.replace('.html', '.png'));
  await card.screenshot({ path: out, omitBackground: false });
  console.log('rendered', out);
}

await browser.close();

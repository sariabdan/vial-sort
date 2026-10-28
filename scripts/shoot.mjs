// Screenshots of the built site for review, light and dark, desktop and phone width.
//   npx astro preview --port 4321 &   then   node scripts/shoot.mjs <out dir> [page path ...]
// Also reports console errors and any horizontal scroll (the page must fit a 390 px phone).
import { chromium } from 'playwright';

const [out, ...rest] = process.argv.slice(2);
const paths = rest.length ? rest : ['', 'results/', 'training/', 'datasets/', 'paper/'];
const base = process.env.BASE ?? 'http://localhost:4321/vial-sort/';
const browser = await chromium.launch();
for (const scheme of ['light', 'dark']) {
  for (const [width, height, tag] of [[1280, 900, 'desk'], [390, 844, 'phone']]) {
    const page = await browser.newPage({ viewport: { width, height }, colorScheme: scheme });
    page.on('console', (m) => m.type() === 'error' && console.log(`console error: ${m.text()}`));
    page.on('pageerror', (e) => console.log(`page error: ${e.message}`));
    for (const p of paths) {
      await page.goto(base + p, { waitUntil: 'networkidle' });
      await page.waitForTimeout(700);
      const scroll = await page.evaluate(() => document.documentElement.scrollWidth);
      if (scroll > width) console.log(`horizontal scroll on /${p} at ${width}px: ${scroll}px wide`);
      const name = (p || 'home').replace(/\/$/, '').replace(/\//g, '_');
      await page.screenshot({ path: `${out}/${name}_${tag}_${scheme}.png`, fullPage: true });
    }
    await page.close();
  }
}
await browser.close();

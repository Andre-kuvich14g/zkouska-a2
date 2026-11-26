// Рендер мультяшних сцен дня в PNG (відновлено 26.11.2026).
// node tools/yt/scenes.js 19   -> бере tools/yt/days/day19.js і пише tools/yt/scenes/<key>.png (+ full/<id>.svg для обкладинок)
// day-файл експортує { SC: {key: fn}, PN: {key: fn}, OPT: {key: fn} } — fn() повертає повний SVG 1280x720 (kit.svg).
//   SC  -> бічна сцена 720x720 (ділянка x 560–1280) + повна сцена для обкладинки (scenes/full/<key>.svg)
//   PN  -> панель 16:9 для Mluvení 3 (1080x608, ділянка 100 30 1080 608)
//   OPT -> квадратна картка варіанту Mluvení 4 (ділянка 280 60 720 720 -> 360x360)
const { chromium } = require('playwright'); const fs = require('fs'); const path = require('path');
const DIR = path.join(__dirname, 'scenes'); const FULL = path.join(DIR, 'full');
fs.mkdirSync(FULL, { recursive: true });
const day = process.argv[2]; const D = require(path.join(__dirname, 'days', `day${day}.js`));
const vb = (s, box, w, h) => s.replace('viewBox="0 0 1280 720" width="1280" height="720"', `viewBox="${box}" width="${w}" height="${h}"`);
(async () => {
  const b = await chromium.launch(); const pg = await b.newPage({ viewport: { width: 1280, height: 720 } });
  const shot = async (key, svgStr, w, h) => {
    const f = path.join(DIR, key + '.svg'); fs.writeFileSync(f, svgStr);
    await pg.setViewportSize({ width: w, height: h });
    await pg.setContent(`<html><body style="margin:0">${svgStr}</body></html>`); await pg.waitForTimeout(60);
    await pg.screenshot({ path: path.join(DIR, key + '.png'), clip: { x: 0, y: 0, width: w, height: h } }); fs.unlinkSync(f);
  };
  let n = 0;
  for (const [k, fn] of Object.entries(D.SC || {})) { const s = fn(); fs.writeFileSync(path.join(FULL, k + '.svg'), s); await shot(k, vb(s, '560 0 720 720', 720, 720), 720, 720); n++; }
  for (const [k, fn] of Object.entries(D.PN || {})) { await shot(k, vb(fn(), '100 30 1080 608', 1080, 608), 1080, 608); n++; }
  for (const [k, fn] of Object.entries(D.OPT || {})) { await shot(k, vb(fn(), '280 0 720 720', 360, 360), 360, 360); n++; }
  await b.close(); console.log('scenes', n);
})();

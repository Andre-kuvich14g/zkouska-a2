// Обкладинки збірок (A/B-тест, 3 варіанти): node tools/yt/thumb_om.js om3_3 '#c2410c' 'Sbírka 3 · příběhy 11–15 · 8 min' bg1.png:HEAD|line1|line2 bg2.png:... bg3.png:...
// -> yt-upload/thumb_test/<key>_a|b|c.jpg і yt-upload/thumb3/<key>.jpg (= варіант a)
const { chromium } = require('playwright'); const fs = require('fs'); const path = require('path');
const [key, col, foot, ...vs] = process.argv.slice(2); const Y = path.join(__dirname, '..', '..', 'yt-upload');
const esc = s => s.replace(/&/g, '&amp;').replace(/</g, '&lt;');
const html = (bg, head, l1, l2) => `<!doctype html><html><head><meta charset="utf-8"><style>*{margin:0;box-sizing:border-box}body{width:1280px;height:720px;position:relative;overflow:hidden;font-family:Inter,sans-serif;color:#fff}
.bg{position:absolute;right:0;top:0;height:720px;width:1280px;object-fit:cover;object-position:right}
.p{position:absolute;inset:0;background:linear-gradient(90deg,${col} 0,${col} 620px,transparent 820px)}
.c{position:absolute;left:52px;top:44px;bottom:44px;width:640px;display:flex;flex-direction:column}
.t{align-self:flex-start;background:#ffd500;color:#16203a;font-weight:900;font-size:30px;padding:6px 16px;border-radius:10px}
.h{margin-top:auto;font-size:104px;font-weight:900;color:#ffd500;letter-spacing:-3px;line-height:1;text-shadow:0 6px 0 rgba(0,0,0,.3);white-space:nowrap}
.l{font-size:50px;font-weight:900;line-height:1.12;margin-top:12px;text-shadow:0 4px 0 rgba(0,0,0,.25)}
.f{margin-top:auto;font-size:30px;font-weight:900;color:#ffd500}</style></head><body><img class="bg" src="data:image/png;base64,${fs.readFileSync(bg).toString('base64')}"><div class="p"></div>
<div class="c"><div class="t">ZKOUŠKA A2 · TRVALÝ POBYT</div><div class="h" id="h">${esc(head)}</div><div class="l">${esc(l1)}<br>${esc(l2)}</div><div class="f">${esc(foot)}</div></div>
<script>document.fonts.ready.then(()=>{const h=document.getElementById('h');let f=104;while(h.scrollWidth>640&&f>60){f-=2;h.style.fontSize=f+'px'}})</script></body></html>`;
(async () => { const b = await chromium.launch(); const pg = await b.newPage({ viewport: { width: 1280, height: 720 } });
  for (let i = 0; i < vs.length; i++) { const k = vs[i].indexOf(':'); const bg = vs[i].slice(0, k), txt = vs[i].slice(k + 1); const [h, l1, l2] = txt.split('|');
    await pg.setContent(html(path.resolve(bg), h, l1, l2)); await pg.waitForTimeout(400);
    const out = path.join(Y, 'thumb_test', `${key}_${'abc'[i]}.jpg`); await pg.screenshot({ path: out, type: 'jpeg', quality: 90 });
    if (i === 0) fs.copyFileSync(out, path.join(Y, 'thumb3', `${key}.jpg`)); }
  await b.close(); console.log('ok', vs.length); })();

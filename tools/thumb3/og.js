// OG-зображення сайту (прев'ю посилань у Telegram/Facebook) у мультяшному бренд-стилі. 1200x630, 4 мови.
const { chromium } = require('playwright'); const fs = require('fs'); const S = require('./scenes2.js');
const L = {
 '': { h: ['Пробний іспит A2', 'з чеської —'], y: 'безкоштовно', b: ['20 варіантів нового формату 2026', 'Живі голоси, таймер і бали як на іспиті', 'Пояснення українською'] },
 ru: { h: ['Пробный экзамен A2', 'по чешскому —'], y: 'бесплатно', b: ['20 вариантов нового формата 2026', 'Живые голоса, таймер и баллы как на экзамене', 'Пояснения на русском'] },
 en: { h: ['Czech A2 practice', 'exam —'], y: 'free', b: ['20 full tests, new 2026 format', 'Real voices, timer and scoring', 'Explanations in English'] },
 vi: { h: ['Thi thử A2', 'tiếng Séc —'], y: 'miễn phí', b: ['20 đề theo định dạng mới 2026', 'Giọng thật, hẹn giờ và chấm điểm', 'Giải thích bằng tiếng Việt'] },
};
const html = x => `<!doctype html><html><head><meta charset="utf-8"><style>*{box-sizing:border-box;margin:0}body{width:1200px;height:630px;font-family:Inter,sans-serif;position:relative;overflow:hidden;color:#fff}
.sc{position:absolute;left:-90px;top:-60px;width:1280px;height:720px}.panel{position:absolute;inset:0;background:linear-gradient(90deg,#1f4e9c 0,#1f4e9c 600px,rgba(31,78,156,0) 760px)}
.c{position:absolute;left:52px;top:44px;width:640px}.tp{display:flex;gap:12px;align-items:center;font-size:22px;font-weight:800}.a2{background:#ffd500;color:#16203a;font-size:26px;font-weight:900;padding:4px 14px;border-radius:10px}
h1{margin-top:26px;font-size:58px;line-height:1.05;font-weight:900;letter-spacing:-1px;text-shadow:0 4px 0 rgba(0,0,0,.25)}h1 b{color:#ffd500}
ul{list-style:none;margin-top:24px;font-size:25px;font-weight:700;line-height:1.5}ul li:before{content:'✓ ';color:#ffd500;font-weight:900}
.url{position:absolute;left:52px;bottom:40px;background:#ffd500;color:#16203a;font-size:34px;font-weight:900;padding:10px 26px;border-radius:999px;box-shadow:0 5px 0 rgba(0,0,0,.2)}
.z{position:absolute;right:34px;top:30px;background:#16203a;color:#ffd500;font-weight:900;font-size:30px;padding:6px 20px;border-radius:12px}</style></head><body>
<div class="sc">${S.promo()}</div><div class="panel"></div><div class="z">ZDARMA</div>
<div class="c"><div class="tp"><span class="a2">A2</span>ZKOUŠKA · TRVALÝ POBYT 2026</div><h1>${x.h.join('<br>')}<br><b>${x.y}</b></h1><ul>${x.b.map(t => `<li>${t}</li>`).join('')}</ul></div>
<div class="url">zkouska-a2.cz</div></body></html>`;
(async () => { const b = await chromium.launch(); const pg = await b.newPage({ viewport: { width: 1200, height: 630 } });
 for (const [k, x] of Object.entries(L)) { fs.writeFileSync('/tmp/claude-0/og.html', html(x)); await pg.goto('file:///tmp/claude-0/og.html'); await pg.waitForTimeout(150);
  await pg.screenshot({ path: `/home/claude/yt/ab2/og/og-image${k ? '-' + k : ''}.jpg`, type: 'jpeg', quality: 88 }); }
 await b.close(); console.log('ok'); })();

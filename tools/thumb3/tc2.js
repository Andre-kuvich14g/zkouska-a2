// Обкладинка v3 «мультяшна сцена»: ілюстрація на весь фон + кольорова панель úlohy зліва (флекс-верстка, автопідгін шрифту).
// node tc2.js list.json outDir [ids...]
const { chromium } = require('playwright'); const fs = require('fs'); const S = require('./scenes2.js');
const C = { f: '#15803d', p: '#0f8a43', m: '#1f5fbf', d: '#0f766e', v: '#c2410c', r: '#6d3fc0', l: '#be185d', w: '#1f4e9c', t: '#1f5fbf' };
const esc = s => String(s).replace(/&/g, '&amp;').replace(/</g, '&lt;');
const html = x => `<!doctype html><html><head><meta charset="utf-8"><style>*{box-sizing:border-box;margin:0}body{width:1280px;height:720px;font-family:Inter,sans-serif;position:relative;overflow:hidden;color:#fff}
.sc{position:absolute;inset:0}.panel{position:absolute;left:0;top:0;bottom:0;width:600px;background:linear-gradient(90deg,${C[x.sec]} 0,${C[x.sec]} 470px,transparent 600px)}
.col{position:absolute;left:44px;top:38px;bottom:30px;width:500px;display:flex;flex-direction:column;align-items:flex-start}
.top{display:flex;gap:12px;align-items:center}.a2{background:#ffd500;color:#16203a;font-weight:900;font-size:32px;padding:5px 16px;border-radius:12px}.tp{font-size:25px;font-weight:800;letter-spacing:.3px}
.lab{margin-top:20px;font-size:60px;font-weight:900;letter-spacing:-2px;line-height:1;white-space:nowrap;text-shadow:0 5px 0 rgba(0,0,0,.25)}
.hk{margin-top:10px;font-weight:900;line-height:1.0;letter-spacing:-1px;color:#ffd500;text-shadow:0 6px 0 rgba(0,0,0,.3)}.hk div{white-space:nowrap}
.cz{margin-top:22px;font-size:34px;font-weight:800;background:#fff;color:#16203a;padding:7px 18px;border-radius:14px;max-width:500px;line-height:1.15;box-shadow:0 6px 0 rgba(0,0,0,.18)}
.ua{margin-top:16px;font-size:32px;font-weight:800;line-height:1.15;max-width:500px;text-shadow:0 2px 0 rgba(0,0,0,.25)}.foot{margin-top:auto;display:flex;flex-direction:column;align-items:flex-start}.badge{font-size:30px;font-weight:900;background:#16203a;color:#ffd500;padding:7px 16px;border-radius:12px}
.url{margin-top:14px;font-size:36px;font-weight:900;color:#ffd500;text-shadow:0 3px 0 rgba(0,0,0,.3)}
.num{position:absolute;right:36px;top:34px;background:#16203a;color:#ffd500;font-weight:900;font-size:40px;padding:5px 20px;border-radius:14px;box-shadow:0 4px 0 rgba(0,0,0,.2)}
.cc{position:absolute;right:32px;bottom:28px;font-size:23px;font-weight:800;background:rgba(22,32,58,.72);padding:6px 14px;border-radius:10px}</style></head><body>
<div class="sc">${S[x.id]()}</div><div class="panel"></div>
<div class="col"><div class="top"><span class="a2">A2</span><span class="tp">ZKOUŠKA · TRVALÝ POBYT</span></div>
<div class="lab">${esc(x.lab)}</div><div class="hk" id="hk">${x.hook.map(h => `<div>${esc(h)}</div>`).join('')}</div>
${x.ua ? `<div class="ua">${esc(x.ua)}</div>` : ''}${x.topic ? `<div class="cz">${esc(x.topic)}</div>` : ''}<div class="foot">${x.badge ? `<div class="badge">${esc(x.badge)}</div>` : ''}<div class="url">zkouska-a2.cz</div></div></div>
${x.num ? `<div class="num">${esc(x.num)}</div>` : ''}<div class="cc">CZ + titulky UA · RU · EN · VI</div>
<script>const hk=document.getElementById('hk');let fs=${x.hfs || 112};const fit=()=>{hk.style.fontSize=fs+'px';return [...hk.children].every(d=>d.scrollWidth<=500)};while(!fit()&&fs>40)fs-=2;
const col=document.querySelector('.col');while(col.scrollHeight>col.clientHeight+2&&fs>44){fs-=2;hk.style.fontSize=fs+'px'}
const lab=document.querySelector('.lab');let lf=60;while(lab.scrollWidth>500&&lf>44){lf-=2;lab.style.fontSize=lf+'px'}</script></body></html>`;
(async () => { const L = JSON.parse(fs.readFileSync(process.argv[2], 'utf8')); const out = process.argv[3]; const only = process.argv.slice(4);
 const b = await chromium.launch(); const pg = await b.newPage({ viewport: { width: 1280, height: 720 } }); let n = 0;
 for (const x of L) { if (only.length && !only.includes(x.id)) continue; fs.writeFileSync('/tmp/claude-0/tc2.html', html(x)); await pg.goto('file:///tmp/claude-0/tc2.html'); await pg.waitForTimeout(120);
  await pg.screenshot({ path: `${out}/${x.id}.jpg`, type: 'jpeg', quality: 90 }); n++; }
 await b.close(); console.log('ok', n); })();

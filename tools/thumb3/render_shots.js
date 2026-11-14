const { chromium } = require('playwright'); const fs = require('fs');
const G = '/home/claude/yt/guide'; const D = JSON.parse(fs.readFileSync(G + '/shots.json', 'utf8'));
const N = D.names.length;
const short = n => n.replace(/^Розділ \d+\.\s*/, '').replace('Холодний старт і гачок', 'Вступ').replace('Фінал і заклики до дії', 'Фінал');
const prog = ch => `<div class="pg">${D.names.map((n, i) => `<i class="${i < ch ? 'dn' : i === ch ? 'cu' : ''}"></i>`).join('')}</div>`;
const css = `*{box-sizing:border-box;margin:0}body{width:1920px;height:1080px;overflow:hidden;font-family:Inter,Arial,sans-serif;position:relative;background:#16203a}
.sc{position:absolute;left:300px;top:96px;width:1320px;height:743px;border-radius:28px;box-shadow:0 12px 0 rgba(0,0,0,.25)}
.badge{position:absolute;left:36px;top:30px;background:#16203a;color:#fff;font-weight:900;font-size:30px;padding:12px 24px;border-radius:16px;display:flex;gap:14px;align-items:center;box-shadow:0 6px 0 rgba(0,0,0,.2)}.badge b{background:#ffd500;color:#16203a;padding:2px 12px;border-radius:8px}
.chap{position:absolute;right:36px;top:30px;background:#ffd500;color:#16203a;font-weight:900;font-size:30px;padding:12px 24px;border-radius:16px;box-shadow:0 6px 0 rgba(0,0,0,.2)}
.cap{position:absolute;left:120px;right:120px;top:868px;height:178px;display:flex;align-items:center;justify-content:center;background:#fff;border-radius:26px;padding:16px 40px;font-size:46px;line-height:1.28;font-weight:700;color:#16203a;text-align:center;box-shadow:0 10px 0 rgba(0,0,0,.18);border-left:14px solid var(--c)}
.cap b{color:#c2410c;font-weight:900}
.pg{position:absolute;left:0;right:0;bottom:0;height:16px;display:flex;gap:4px}.pg i{flex:1;background:rgba(255,255,255,.35)}.pg i.dn{background:#22b14c}.pg i.cu{background:#ffd500}
.card{position:absolute;inset:0;display:flex;flex-direction:column;align-items:center;justify-content:center;background:linear-gradient(#1f4e9c,#16203a);color:#fff}
.card .k{font-size:44px;color:#ffd500;font-weight:900;margin-bottom:20px}.card .t{font-size:84px;font-weight:900;text-align:center;padding:0 80px}.card .s{margin-top:30px;font-size:40px;color:#c8d0e0}`;
(async () => { const b = await chromium.launch({ args: ['--allow-file-access-from-files'] }); const pg = await b.newPage({ viewport: { width: 1920, height: 1080 } });
 const list = [];
 for (let i = 0; i < D.shots.length; i++) { const s = D.shots[i]; const out = `${G}/shots/s${String(i).padStart(3, '0')}.jpg`;
  if (s.kind === 'img') { list.push([s.img, s.dur]); continue; }
  let body;
  if (s.kind === 'card') body = `<div class="card"><div class="k">▶ ${short(D.names[s.ch])}</div><div class="t">${s.title}</div><div class="s">Говоріть уголос разом з уроком</div></div>${prog(s.ch)}`;
  else body = `<img class="sc" src="file://${s.scene}"><div class="badge"><b>A2</b>Іспит від А до Я</div><div class="chap">${short(D.names[s.ch])}</div><div class="cap" style="--c:${s.who === 'Michaela' ? '#6d3fc0' : '#1f4e9c'}">${s.cap}</div>${prog(s.ch)}`;
  fs.writeFileSync(G + '/shot.html', `<!doctype html><html><head><meta charset="utf-8"><style>${css}</style></head><body>${body}</body></html>`);
  await pg.goto('file://' + G + '/shot.html'); await pg.waitForTimeout(30);
  await pg.screenshot({ path: out, type: 'jpeg', quality: 88 }); list.push([out, s.dur]); }
 fs.writeFileSync(G + '/concat.txt', list.map(([f, d]) => `file '${f}'\nduration ${d.toFixed(3)}`).join('\n') + `\nfile '${list[list.length - 1][0]}'\n`);
 await b.close(); console.log('rendered', list.length); })();

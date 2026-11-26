// Short 1080x1920 з готового уроку (відновлено 26.11.2026): кольоровий фон, напис зверху, урок 16:9 посередині, гачок + адреса знизу.
// node tools/yt/short.js d19 "V hotelu" "4 otázky v hotelu – zvládnete to? 🏨"   -> yt-upload/s_d19.mp4 (+ s_d19.cs.srt = субтитри уроку)
const { chromium } = require('playwright'); const fs = require('fs'); const path = require('path'); const { execFileSync } = require('child_process');
const [id, topic, hook] = process.argv.slice(2); const Y = path.join(__dirname, '..', '..', 'yt-upload');
const C = { f: '#15803d', p: '#15803d', m: '#1f5fbf', d: '#0f766e', v: '#c2410c', r: '#6d3fc0' };
const LAB = { f: 'PSANÍ 1', p: 'PSANÍ 2', m: 'MLUVENÍ 1', d: 'MLUVENÍ 2', v: 'MLUVENÍ 3', r: 'MLUVENÍ 4' };
const esc = s => String(s).replace(/&/g, '&amp;').replace(/</g, '&lt;');
const html = `<!doctype html><html><head><meta charset="utf-8"><style>*{margin:0;box-sizing:border-box}body{width:1080px;height:1920px;background:${C[id[0]]};font-family:Inter,sans-serif;color:#fff;position:relative}
.top{position:absolute;top:170px;left:60px;right:60px;display:flex;flex-direction:column;align-items:center;gap:18px}
.b{background:#ffd500;color:#16203a;font-weight:900;font-size:46px;padding:8px 28px;border-radius:14px}
.l{font-size:110px;font-weight:900;letter-spacing:-2px;line-height:1;text-shadow:0 6px 0 rgba(0,0,0,.2)}
.t{background:#fff;color:#16203a;font-weight:800;font-size:54px;padding:14px 30px;border-radius:20px;width:100%;text-align:center}
.bot{position:absolute;top:1300px;left:50px;right:50px;display:flex;flex-direction:column;align-items:center;gap:40px;text-align:center}
.h{font-size:58px;font-weight:800;line-height:1.2}.u{background:#ffd500;color:#16203a;font-weight:900;font-size:68px;padding:16px 50px;border-radius:999px}.s{font-size:44px;font-weight:700;opacity:.95}</style></head><body>
<div class="top"><div class="b">ZKOUŠKA A2 · TRVALÝ POBYT</div><div class="l">${LAB[id[0]]}</div><div class="t">${esc(topic)}</div></div>
<div class="bot"><div class="h">${esc(hook)}</div><div class="u">zkouska-a2.cz</div><div class="s">Celá cvičná zkouška zdarma 🔗 v profilu</div></div></body></html>`;
(async () => {
  const tmp = require('os').tmpdir(); const bg = path.join(tmp, `short_${id}.png`);
  const b = await chromium.launch(); const pg = await b.newPage({ viewport: { width: 1080, height: 1920 } });
  await pg.setContent(html); await pg.waitForTimeout(150); await pg.screenshot({ path: bg }); await b.close();
  execFileSync('ffmpeg', ['-v', 'error', '-y', '-loop', '1', '-i', bg, '-i', path.join(Y, `${id}.mp4`), '-filter_complex',
    '[1:v]scale=1080:608[v];[0:v][v]overlay=0:648:shortest=1,format=yuv420p[o]', '-map', '[o]', '-map', '1:a', '-c:v', 'libx264', '-preset', 'veryfast', '-crf', '21',
    '-c:a', 'aac', '-b:a', '160k', '-r', '30', '-movflags', '+faststart', path.join(Y, `s_${id}.mp4`)]);
  for (const l of ['cs', 'uk', 'ru', 'en', 'vi']) { const f = path.join(Y, `${id}.${l}.srt`); if (fs.existsSync(f)) fs.copyFileSync(f, path.join(Y, `s_${id}.${l}.srt`)); }
  console.log('ok s_' + id);
})();

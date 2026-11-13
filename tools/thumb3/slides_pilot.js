// Render each unique slide of a plan to JPEG (1920x1080) with Playwright.
const { chromium } = require('playwright');
const fs = require('fs');
const OM = '/home/claude/zkouska-a2/img/om/';
const ICON = '/home/claude/zkouska-a2/img/app/icon-192.png';
const SITE = 'zkouska-a2.cz';
const esc = s => String(s).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
const css = `
*{box-sizing:border-box;margin:0}
body{width:1920px;height:1080px;font-family:Inter,sans-serif;background:#eef1f6;color:#16203a;position:relative;overflow:hidden}
.hd{position:absolute;inset:0 0 auto 0;height:110px;background:#1f4e9c;display:flex;align-items:center;padding:0 60px;gap:22px;color:#fff}
.hd img{width:64px;height:64px;border-radius:14px}
.hd b{font-size:38px;font-weight:800;letter-spacing:.2px}
.hd .badge{margin-left:auto;font-size:28px;font-weight:800;padding:12px 26px;border-radius:999px;background:var(--c);color:#fff;letter-spacing:1px}
.ft{position:absolute;inset:auto 0 0 0;height:84px;display:flex;align-items:center;justify-content:space-between;padding:0 60px;font-size:34px;color:#5b6680;border-top:2px solid #d9dfea;background:#fff}
.ft b{color:#16203a}
.main{position:absolute;top:110px;bottom:84px;left:0;right:0;display:flex;flex-direction:column;justify-content:center;align-items:center;padding:40px 110px;text-align:center}
.chip{display:inline-block;font-size:34px;font-weight:800;color:var(--c);background:var(--cs);padding:10px 28px;border-radius:999px;margin-bottom:28px}
.title{font-size:120px;font-weight:800;line-height:1.05}
.sub{font-size:46px;color:#5b6680;margin-top:26px}
.tr{font-size:38px;color:#8a93a8;margin-top:34px}
.card{background:#fff;border:3px solid #d9dfea;border-radius:32px;padding:50px 70px;max-width:1600px;box-shadow:0 10px 30px rgba(22,32,58,.08)}
.qn{font-size:32px;font-weight:800;color:var(--c);margin-bottom:22px;letter-spacing:1px}
.q{font-size:84px;font-weight:800;line-height:1.15}
.qs{font-size:46px;font-weight:700;color:#5b6680;margin-bottom:36px}
.ans{border-color:#15803d;background:#f3fbf5}
.al{font-size:30px;font-weight:800;color:#15803d;margin-bottom:18px;letter-spacing:1px}
.a{font-size:64px;font-weight:700;line-height:1.25}
.wait{margin-top:46px;display:flex;align-items:center;gap:36px;font-size:52px;font-weight:800;color:#c4342b}
.cd{width:150px;height:150px;border-radius:50%;border:10px solid #c4342b;display:grid;place-items:center;font-size:84px;font-weight:800;color:#c4342b;background:#fff}
.url{font-size:62px;font-weight:800;color:#1f4e9c;background:#fff;border:4px solid #1f4e9c;border-radius:999px;padding:22px 56px;margin:36px 0}
.sit{font-size:52px;font-weight:700;line-height:1.25;max-width:1650px}
.to{font-size:32px;color:#5b6680;margin-top:16px}
.pics{display:flex;gap:28px;margin-top:44px}
.pic{width:270px;background:#fff;border:3px solid #d9dfea;border-radius:26px;padding:22px 14px;display:flex;flex-direction:column;align-items:center;gap:14px}
.pic img{width:130px;height:130px}
.pic span{font-size:30px;font-weight:800;line-height:1.2}
.model{position:absolute;top:140px;bottom:114px;left:60px;right:60px;display:flex;gap:40px}
.side{width:300px;display:flex;flex-direction:column;gap:14px;justify-content:center}
.side .pic{width:100%;flex-direction:row;padding:12px 16px;gap:14px;text-align:left}
.side .pic img{width:70px;height:70px}
.side .pic span{font-size:23px}
.mail{flex:1;background:#fff;border:3px solid #d9dfea;border-radius:28px;padding:36px 48px;font-size:39px;line-height:1.45;text-align:left;overflow:hidden}
.mh{font-size:30px;color:#5b6680;border-bottom:2px solid #e5e9f1;padding-bottom:14px;margin-bottom:18px}
.mh b{color:#16203a}
.s{border-radius:10px;padding:0 6px}
.s.on{background:#ffe9a8;box-shadow:0 0 0 4px #ffe9a8}
.s.gr{opacity:.45}
.cl{margin-top:16px;white-space:pre-line}
.subs{margin-top:30px;font-size:46px;font-weight:800;color:#fff;background:#c4342b;padding:16px 44px;border-radius:999px}
.flist{text-align:left;font-size:40px;line-height:1.5;margin-top:30px}
.field{background:#fff;border:3px solid #d9dfea;border-radius:22px;padding:30px 40px;width:1500px;text-align:left}
.field .lbl{font-size:44px;font-weight:800;margin-bottom:18px}
.field .box{min-height:120px;border:3px dashed #c5ccda;border-radius:14px;padding:18px 24px;font-size:48px;font-weight:600;line-height:1.3;color:#16203a}
.field .box.ok{border-style:solid;border-color:#15803d;background:#f3fbf5}
.wc{font-size:32px;font-weight:800;color:#15803d;margin-top:14px;text-align:right}
.cues{display:flex;gap:24px;margin-top:40px}
.cue{font-size:46px;font-weight:800;background:#fff;border:3px solid #d9dfea;border-radius:20px;padding:20px 30px}
.cue.on{border-color:var(--c);background:var(--cs);color:var(--c)}
.goal{font-size:46px;color:#5b6680;margin-top:14px}
.bub{max-width:1400px;border-radius:30px;padding:24px 40px;font-size:54px;line-height:1.3;text-align:left;margin:10px 0}
.bub.t{background:#fff;border:3px solid #d9dfea;align-self:flex-start}
.bub.u{background:var(--c);color:#fff;align-self:flex-end;font-weight:700}
.bub small{display:block;font-size:28px;font-weight:800;opacity:.7;margin-bottom:6px;letter-spacing:1px}
.chat{position:absolute;top:130px;bottom:104px;left:120px;right:120px;display:flex;flex-direction:column;justify-content:flex-end;overflow:hidden}
.opts{display:flex;gap:40px;margin-top:44px}
.opt{width:340px;background:#fff;border:3px solid #d9dfea;border-radius:26px;padding:26px;display:flex;flex-direction:column;align-items:center;gap:16px;font-size:40px;font-weight:800}
.opt img{width:170px;height:170px}
.p4{display:grid;grid-template-columns:repeat(4,1fr);gap:24px;margin-top:36px;width:1700px}
.p4 .pic{width:auto}
.p4 .pic span{font-size:26px;font-weight:600}
.story{position:absolute;top:130px;bottom:104px;left:60px;right:60px;display:flex;gap:36px}
.story .side{width:330px}
.story .mail{font-size:38px}
.pv{color:#c4342b;font-weight:800;text-decoration:underline;text-decoration-color:#c4342b;text-decoration-thickness:5px;text-underline-offset:8px}
.s.gr .pv{color:inherit}
.pvl{float:right;color:#c4342b;font-weight:800;font-size:24px}
.tips{text-align:left;font-size:54px;font-weight:700;line-height:1.7}
.tips div::before{content:'✓ ';color:#15803d}

.lo{display:grid;gap:18px;margin-top:30px;width:1500px;text-align:left}
.lo.c2{grid-template-columns:1fr 1fr}
.lo .o{background:#fff;border:3px solid #d9dfea;border-radius:20px;padding:18px 28px;font-size:46px;font-weight:700;display:flex;gap:22px;align-items:center}
.lo .o b{display:inline-grid;place-items:center;min-width:64px;height:64px;border-radius:14px;background:var(--cs);color:var(--c);font-size:40px}
.lo .o.ok{border-color:#15803d;background:#f3fbf5}.lo .o.ok b{background:#15803d;color:#fff}
.lo .o.dim{opacity:.35}
.lo.ic{grid-template-columns:repeat(3,1fr)}
.lo.ic .o{flex-direction:column;font-size:32px;padding:8px;gap:6px}
.lo.ic .o img{width:78px;height:78px}
.lo.ic .o b{height:50px;min-width:50px;font-size:32px}
.lq{font-size:62px;font-weight:800;line-height:1.15;max-width:1650px}
.lnum{font-size:34px;font-weight:800;color:var(--c);letter-spacing:1px;margin-bottom:14px}
.play{margin-top:26px;font-size:46px;font-weight:800;color:#fff;background:var(--c);padding:14px 40px;border-radius:999px}
.scr{margin-top:22px;font-size:30px;color:#5b6680;max-width:1650px;line-height:1.35;text-align:left;background:#fff;border-radius:16px;padding:14px 22px;border:2px solid #e5e9f1}
.wait.sm{margin-top:24px;font-size:40px}.wait.sm .cd{width:110px;height:110px;font-size:60px;border-width:8px}
.ff{display:grid;gap:14px;width:1500px;margin-top:24px;text-align:left}
.ff .r{display:flex;gap:20px;align-items:center;background:#fff;border:3px solid #d9dfea;border-radius:16px;padding:14px 24px;font-size:38px;font-weight:700}
.ff .r span{flex:1}.ff .r i{font-style:normal;min-width:520px;border-bottom:3px dashed #c5ccda;color:#15803d;font-weight:800}

.agenda{display:flex;gap:18px;margin-top:40px;flex-wrap:wrap;justify-content:center}
.agenda div{background:#fff;border:3px solid #d9dfea;border-radius:20px;padding:16px 26px;font-size:34px;font-weight:800}
.agenda div i{font-style:normal;color:var(--c);margin-right:10px}
.stats{display:flex;gap:40px;margin-top:20px}
.stat{background:#fff;border:3px solid #d9dfea;border-radius:30px;width:420px;padding:40px 20px}
.stat b{display:block;font-size:150px;font-weight:900;color:var(--c);line-height:1}
.stat span{font-size:44px;font-weight:800}
.uk{margin-top:40px;font-size:40px;font-weight:700;color:#1f4e9c;background:#fff8d6;border-radius:18px;padding:16px 34px;max-width:1650px}
.tns{display:flex;flex-direction:column;gap:20px;margin-top:20px;text-align:left}
.tns div{font-size:54px;font-weight:700;background:#fff;border:3px solid #d9dfea;border-radius:20px;padding:16px 34px}
.tns div b{color:var(--c)}
.tag{display:inline-block;font-size:28px;font-weight:800;color:#fff;background:#5b6680;border-radius:999px;padding:6px 20px;margin-left:16px;vertical-align:middle}
.tag.minulý{background:#c2410c}.tag.budoucí{background:#6d3fc0}.tag.přítomný{background:#0f766e}.tag.přání{background:#be185d}
.big{font-size:150px;line-height:1}
.tp{font-size:78px;font-weight:900;color:var(--c);margin-bottom:26px}
.bad{font-size:60px;font-weight:700;color:#c4342b;text-decoration:line-through;text-decoration-thickness:5px}
.good{font-size:66px;font-weight:800;color:#15803d}
.erow{display:flex;align-items:center;gap:30px;margin:14px 0}
.erow .ic{font-size:70px}
.prog{position:absolute;top:110px;left:0;right:0;height:12px;background:#d9dfea}.prog i{display:block;height:100%;background:var(--c)}
.dots{display:flex;gap:18px;margin-top:40px}.dots i{width:34px;height:34px;border-radius:50%;background:#d9dfea}.dots i.ok{background:#15803d}.dots i.on{background:var(--c);box-shadow:0 0 0 6px var(--cs)}
`;
const CSS2 = `.sideimg{position:absolute;left:60px;top:203px;width:680px;height:680px;border-radius:34px;box-shadow:0 10px 0 rgba(0,0,0,.12);border:6px solid #fff}
body.hasside .main,body.hasside .chat{left:760px !important;right:40px !important;padding-left:30px !important;padding-right:30px !important}
body.hasside .title{font-size:68px !important}body.hasside .sit{font-size:44px}body.hasside .card{max-width:1080px;padding:40px 50px}
body.hasside .cues,body.hasside .pics{flex-wrap:wrap;justify-content:center}body.hasside .pics .pic{width:190px}
.opt.sc{width:360px;padding:0;overflow:hidden;gap:0}.opt.sc img{width:360px;height:360px;display:block}.opt.sc span{padding:14px}

body.hasside .field{width:100% !important;max-width:1060px !important}body.hasside .main>*{max-width:100%}
body.hasside .x-out .title,body.hasside .title.out{font-size:60px !important}
body.hasside .bub{max-width:960px;font-size:44px}
body.hasside .pics{flex-wrap:nowrap !important;gap:14px}body.hasside .pics .pic{width:196px;padding:14px 8px}body.hasside .pics .pic img{width:90px;height:90px}body.hasside .pics .pic span{font-size:21px}
.cg{display:grid;grid-template-columns:1fr 1fr;gap:18px 26px;margin-top:22px}
.cp{position:relative;width:560px;border-radius:22px;overflow:hidden;border:5px solid #fff;box-shadow:0 6px 0 rgba(0,0,0,.12);background:#fff}
.cp img{width:100%;display:block}
.cp b{position:absolute;left:14px;top:12px;width:58px;height:58px;border-radius:50%;background:var(--c);color:#fff;font-size:36px;display:grid;place-items:center}
.cp span{display:block;font-size:27px;font-weight:700;padding:8px 14px;text-align:left;background:#fff}
.waitov{width:380px;display:flex;flex-direction:column;align-items:center;gap:22px;font-size:40px;font-weight:800;color:#c4342b;background:#fff;padding:30px 24px;border-radius:28px;box-shadow:0 6px 0 rgba(0,0,0,.12);text-align:center}.prow{display:flex;align-items:center;gap:40px;margin-top:16px}.prow .cg{margin-top:0}
.waitov .cd{width:150px;height:150px;font-size:84px}
.story2{position:absolute;top:130px;bottom:104px;left:60px;right:60px;display:flex;gap:36px}
.bp{width:860px;display:flex;flex-direction:column;gap:14px}
.bp .big{position:relative;border-radius:24px;overflow:hidden;border:5px solid var(--c)}
.bp .big img{width:100%;display:block}.bp .big b{position:absolute;left:16px;top:14px;width:66px;height:66px;border-radius:50%;background:var(--c);color:#fff;font-size:40px;display:grid;place-items:center}
.bp .cap{font-size:30px;font-weight:800;text-align:left}
.bp .th{display:flex;gap:12px}.bp .th img{width:200px;border-radius:12px;border:4px solid #d9dfea;opacity:.55}.bp .th img.on{border-color:var(--c);opacity:1}
.story2 .mail{font-size:38px}
.intro2{position:absolute;top:110px;bottom:84px;left:0;right:0;display:flex;align-items:center;gap:60px;padding:0 90px}
.intro2 img{width:900px;border-radius:30px;box-shadow:0 10px 0 rgba(0,0,0,.12)}
.intro2 .tx{flex:1;text-align:left}
`;
const SEC = {
  m: ['#1f5fbf', '#e4edfb', 'MLUVENÍ · ÚLOHA 1', 'Téma'], p: ['#15803d', '#e3f4e8', 'PSANÍ · ÚLOHA 2', 'E-mail'],
  f: ['#15803d', '#e3f4e8', 'PSANÍ · ÚLOHA 1', 'Formulář'], d: ['#0f766e', '#dcf2ef', 'MLUVENÍ · ÚLOHA 2', 'Karta'],
  v: ['#c2410c', '#fdeadf', 'MLUVENÍ · ÚLOHA 3', 'Příběh'], r: ['#6d3fc0', '#eee6fb', 'MLUVENÍ · ÚLOHA 4', 'Situace'],
  l: ['#be185d', '#fce7f3', 'POSLECH · CELÝ TEST', 'Test'] };
function frame(p, s, body) {
  const k = s.sec || s.kind[0]; const [c, cs, badge, lab] = SEC[k];
  const nm = s.name || s.cz || s.subj;
  const left = s.sb ? `${s.sbu || 'Mluvení 1'} · <b>Velké opakování ${s.sb}</b> · ${s.sbr || 'témata'} ${5*s.sb-4}–${5*s.sb}` : k === 'l' ? `Poslech · test <b>${s.n}/20</b>${s.u ? ` · úloha <b>${s.u}</b>` : ''}` : `${lab} <b>${s.n}/40</b> · ${esc(nm)}`;
  const badge2 = s.sb ? `${(s.sbu || 'Mluvení 1').toUpperCase()} · OPAKOVÁNÍ` : k === 'l' && s.u ? `POSLECH · ÚLOHA ${s.u}` : badge;
  return `<!doctype html><html><head><meta charset="utf-8"><style>${css}${CSS2} :root{--c:${c};--cs:${cs}}</style></head><body class="${s.side ? 'hasside' : ''}">${s.side ? `<img class="sideimg" src="file://${s.side}">` : ''}
<div class="hd"><img src="file://${ICON}"><b>Zkouška A2 nanečisto</b><span class="badge">${badge2}</span></div>${body}
<div class="ft"><span>${left}</span><span style="color:#1f4e9c;font-weight:800">🌐 ${SITE}</span></div></body></html>`;
}
const PAST_X = new Set('fotbal fotbalu kostel hotel mobil michal pavel karel pavla karla anil kolo kola kole kolem skola skolu skoly skole skolka stul stolu stole sul hotel hotelu ale mala malo male mali maly cela celo cely celi dila dilo vila sila zela'.split(' '));
const fold = w => w.normalize('NFD').replace(/[\u0300-\u036f]/g, '').toLowerCase();
const isPast = w => w.length > 2 && /(l|la|lo|li|ly)$/.test(w) && !PAST_X.has(w) && !/(ell|all|ill)$/.test(w);
const pastMark = t => esc(t).replace(/[A-Za-zÀ-ž]+/g, w => isPast(fold(w)) ? `<span class="pv">${w}</span>` : w);
const pic = (x) => `<div class="pic"><img src="file://${OM}${x.om[0]}.svg"><span>${esc(x.q)}</span></div>`;
function body(p, s) {
  switch (s.kind) {



    case 'sb-intro2': return `<div class="main"><span class="chip">${esc(s.chip)}</span><div class="title" style="font-size:104px">${s.title}</div><div class="sub">${s.topics.map(esc).join(' · ')}</div><div class="agenda">${s.agenda.map((a, i) => `<div><i>${i + 1}</i>${esc(a)}</div>`).join('')}</div></div>`;
    case 'sb-stats': return `<div class="main"><div class="title" style="font-size:80px;margin-bottom:30px">${esc(s.t)}</div><div class="stats">${s.stats.map(([n, l]) => `<div class="stat"><b>${n}</b><span>${esc(l)}</span></div>`).join('')}</div><div class="uk">🇺🇦 ${esc(s.uk)}</div></div>`;
    case 'sb-list': return `<div class="main"><div class="title" style="font-size:${s.fs || 72}px;margin-bottom:22px">${esc(s.t)}</div><div class="tns" style="font-size:48px">${s.items.map(x => `<div>${x}</div>`).join('')}</div><div class="uk">🇺🇦 ${esc(s.uk)}</div></div>`;
    case 'sb-topic': return `<div class="main"><span class="chip">${s.chip || "TÉMA"} ${s.i} / 5</span><div class="title" style="font-size:130px">${esc(s.top)}</div><div class="sub">${s.subt || "10 otázek · 7 sekund na odpověď · pak vzorová odpověď"}</div><div class="tr" style="color:#1f4e9c;font-weight:700">🇺🇦 ${esc(s.uk)}</div><div class="dots">${[1,2,3,4,5].map(k => `<i class="${k < s.i ? 'ok' : (k === s.i ? 'on' : '')}"></i>`).join('')}</div></div>`;
    case 'sb-sum': return `<div class="main"><div class="title" style="font-size:78px;margin-bottom:24px">Shrnutí: 4 pravidla na plný počet bodů</div><div class="tns" style="font-size:48px"><div>1️⃣ <b>Celá věta</b> – nejlépe dvě věty</div><div>2️⃣ <b>Stejný čas</b> jako v otázce</div><div>3️⃣ <b>Pády:</b> z Ukrajiny · v Praze</div><div>4️⃣ <b>Konkrétně:</b> čísla, místa, jména</div></div><div class="uk">🇺🇦 Повне речення · той самий час · відмінки після z і v · конкретика</div></div>`;
    case 'sb-cta': return `<div class="main"><div class="big">💬 👍</div><div class="title" style="font-size:84px;margin-top:20px">${s.t || "Které téma je pro vás nejtěžší?"}</div><div class="sub">Napište do komentáře · dejte like, pokud vám video pomohlo</div><div class="uk">🇺🇦 ${s.uk || "Яка тема для вас найважча? Напишіть у коментарях — і поставте лайк 👍"}</div></div>`;
    case 'sb-intro': return `<div class="main"><span class="chip">VELKÉ OPAKOVÁNÍ ${s.sb} · TÉMATA ${s.a}–${s.b}</span><div class="title" style="font-size:104px">Mluvení 1:<br>všech 50 otázek</div><div class="sub">${s.topics.map(esc).join(' · ')}</div><div class="agenda"><div><i>1</i>Jak to funguje</div><div><i>2</i>5 témat × 10 otázek</div><div><i>3</i>12 frází</div><div><i>4</i>5 chyb</div><div><i>5</i>Shrnutí</div></div></div>`;
    case 'sb-how1': return `<div class="main"><div class="title" style="font-size:80px;margin-bottom:30px">Jak úloha 1 funguje</div><div class="stats"><div class="stat"><b>2</b><span>témata</span></div><div class="stat"><b>8</b><span>otázek (2 × 4)</span></div><div class="stat"><b>8</b><span>bodů · 1 za otázku</span></div></div><div class="uk">🇺🇦 Екзаменатор обирає 2 теми і ставить по 4 питання. Кожна відповідь = 1 бал.</div></div>`;
    case 'sb-how2': return `<div class="main"><div class="title" style="font-size:72px;margin-bottom:20px">Celá věta + správný čas</div><div class="tns"><div>Co <b>děláte</b>? → přítomný čas</div><div>Co jste <b>dělal</b>? → minulý čas</div><div>Co <b>budete dělat</b>? → budoucí čas</div></div><div class="uk">🇺🇦 Теми відомі заздалегідь, питання — ні. Відповідайте повним реченням (краще двома) і в тому ж часі, що й питання.</div></div>`;
    case 'sb-round': return `<div class="main"><span class="chip">${s.test ? 'TEST BEZ NÁPOVĚDY' : 'ZKOUŠKA NANEČISTO ' + s.r}</span><div class="title" style="font-size:96px">${s.test ? 'Odpovězte sami' : s.tops.map(esc).join(' + ')}</div><div class="sub">8 otázek · ${s.secs} sekund na odpověď${s.test ? ' · odpovědi na webu' : ' · pak vzorová odpověď'}</div><div class="uk">🇺🇦 ${s.test ? 'Тест без підказок: 8 питань, по 10 секунд. Відповіді — на сайті.' : 'Як на справжньому іспиті: 2 теми × 4 питання. Відповідайте вголос.'}</div></div>`;
    case 'sb-q': case 'sb-q-w': return `<div class="main"><div class="card"><div class="prog"><i style="width:${(100 * s.k / s.n).toFixed(1)}%"></i></div><div class="qn">${s.r === 0 ? 'TÉMA ' + esc(s.top) + ' · ' + s.tk + '/10 · CELKEM ' + s.k + '/' + s.n : (s.r === 3 ? 'TEST' : 'ZKOUŠKA ' + s.r) + ' · OTÁZKA ' + s.k + ' / ' + s.n + ' · ' + esc(s.top)}<span class="tag ${s.t.split(' ')[0]}">${s.t}</span></div><div class="q">${esc(s.q)}</div></div>${s.kind === 'sb-q-w' ? `<div class="wait"><div class="cd">${s.c}</div>${esc(s.msg)}</div>` : '<div class="tr">🎧 Zkoušející se ptá…</div>'}</div>`;
    case 'sb-a': return `<div class="main"><div class="qs">${s.k}. ${esc(s.q)}</div><div class="card ans"><div class="al">VZOROVÁ ODPOVĚĎ · 1 BOD</div><div class="a">${esc(s.a)}</div></div></div>`;
    case 'sb-score': return `<div class="main"><div class="big">${s.r === 3 ? '✅' : '🏆'}</div><div class="title" style="font-size:84px;margin-top:20px">${s.r === 3 ? 'Kolik otázek jste zvládli?' : 'Kolik máte bodů z 8?'}</div><div class="sub">Napište výsledek do komentáře 💬</div></div>`;
    case 'sb-sec': return `<div class="main"><div class="big">${s.ic}</div><div class="title" style="font-size:100px;margin-top:20px">${esc(s.t)}</div><div class="uk">🇺🇦 ${esc(s.uk)}</div></div>`;
    case 'sb-ph': case 'sb-ph-w': return `<div class="main"><div class="qn">FRÁZE ${s.i} / ${s.n}</div><div class="tp">${esc(s.tp)}</div><div class="card ans"><div class="a">${esc(s.ex)}</div></div><div class="tr" style="color:#1f4e9c;font-weight:700">🇺🇦 ${esc(s.uk)}</div>${s.kind === 'sb-ph-w' ? `<div class="wait sm"><div class="cd">${s.c}</div>${esc(s.msg)}</div>` : ''}</div>`;
    case 'sb-er': return `<div class="main"><div class="qn">CHYBA ${s.i} / 5</div><div class="qs">${esc(s.q)}</div><div class="card" style="text-align:left"><div class="erow"><span class="ic">❌</span><span class="bad">${esc(s.bad)}</span></div>${s.ok ? `<div class="erow"><span class="ic">✅</span><span class="good">${esc(s.good)}</span></div>` : ''}</div>${s.ok ? `<div class="uk">🇺🇦 ${esc(s.uk)}</div>` : '<div class="tr">Kde je chyba? 🤔</div>'}</div>`;
    case 'sb-outro': return `<div class="main"><div class="title" style="font-size:80px">${s.t || "Všech 50 otázek s odpověďmi"}</div><div class="url">${SITE}</div><div class="sub">Web poslouchá vaši odpověď a kontroluje výslovnost · zdarma · odkaz v popisu</div><div class="subs">🔔 Odebírejte kanál – každý den nové video</div><div class="tr" style="font-size:40px;color:var(--c);font-weight:700">${s.next || "Zítra: Mluvení 2 – velké opakování"}</div></div>`;

    case 'l-intro': return `<div class="main"><span class="chip">Cvičný test ${s.n} / 20</span><div class="title">Poslech A2<br>nanečisto</div><div class="sub">5 úloh · 25 otázek · každá nahrávka 2× · 25 bodů</div><div class="tr">Připravte si papír a tužku ✍️ · nový formát 2026</div></div>`;
    case 'l-task': return `<div class="main"><span class="chip">Úloha ${s.u} / 5</span><div class="title" style="font-size:96px">${esc(s.lab)}</div><div class="sub" style="max-width:1500px">${esc(s.ins)}</div></div>`;
    case 'l-q': case 'l-read': case 'l-play': case 'l-gap': case 'l-wait': case 'l-ans': {
      const ok = s.kind === 'l-ans';
      const ops = `<div class="lo ${s.u === 4 ? 'ic' : (s.opts.length > 4 ? 'c2' : '')}">${s.opts.map(([k, t, om]) => `<div class="o ${ok ? (k === s.ans ? 'ok' : 'dim') : ''}"><b>${k}</b>${om ? `<img src="file://${OM}${om}.svg">` : ''}<span>${esc(t)}</span></div>`).join('')}</div>`;
      const head = `<div class="lnum">OTÁZKA ${s.num}${s.who ? ' · ' + esc(s.who) : ''}</div><div class="lq" style="font-size:${s.u === 3 || s.u === 4 ? 52 : 62}px">${esc(s.q)}</div>`;
      const st = s.kind === 'l-read' ? `<div class="wait sm"><div class="cd">${s.c}</div>Přečtěte si možnosti</div>` : s.kind === 'l-play' ? `<div class="play">🔊 ${s.rep}. poslech</div>` : s.kind === 'l-gap' ? `<div class="play" style="background:#5b6680">⏸ Ještě jednou…</div>` : s.kind === 'l-wait' ? `<div class="wait sm"><div class="cd">${s.c}</div>Vyberte odpověď</div>` : ok ? `<div class="scr">${esc(s.script).replace(/\[(.+?)\]:/g, '<b>$1:</b>').replace(/\n/g, '<br>')}</div>` : '';
      return `<div class="main" style="padding-top:20px;padding-bottom:20px">${head}${ops}${st}</div>`; }
    case 'l5-read': case 'l5-play': case 'l5-gap': case 'l5-wait': case 'l5-ans': {
      const ok = s.kind === 'l5-ans';
      const st = s.kind === 'l5-read' ? `<div class="wait sm"><div class="cd">${s.c}</div>Přečtěte si formulář</div>` : s.kind === 'l5-play' ? `<div class="play">🔊 ${s.rep}. poslech</div>` : s.kind === 'l5-gap' ? `<div class="play" style="background:#5b6680">⏸ Ještě jednou…</div>` : s.kind === 'l5-wait' ? `<div class="wait sm"><div class="cd">${s.c}</div>Doplňte informace</div>` : '';
      return `<div class="main"><div class="lq" style="font-size:52px">${esc(s.intro)}</div><div class="ff">${s.fields.map((f, i) => `<div class="r"><span>${21 + i}. ${esc(f)}</span><i>${ok ? esc(s.ans[i]) : (s.pre && s.pre[i] ? esc(s.pre[i]) + ' …' : '')}</i></div>`).join('')}</div>${st}</div>`; }
    case 'l-outro': return `<div class="main"><div class="title" style="font-size:84px">Kolik máte bodů? 💬</div><div class="sub">Napište svůj výsledek do komentáře · orientačně 15 z 25 = 60 %</div><div class="url">${SITE}</div><div class="sub">Celá cvičná zkouška A2 zdarma · odkaz v popisu</div><div class="subs">🔔 Odebírejte kanál – každý den nové video</div></div>`;
    case 'x-intro': if (s.tscn) return `<div class="intro2"><img src="file://${s.tscn}"><div class="tx"><span class="chip">${esc(s.chip)}</span><div class="title" style="font-size:96px">${esc(s.title)}</div><div class="sub" style="font-size:38px">${esc(s.sub)}</div></div></div>`;
      return `<div class="main"><span class="chip">${esc(s.chip)}</span><div class="title" style="font-size:${s.title.length > 26 ? 88 : 112}px">${esc(s.title)}</div><div class="sub">${esc(s.sub)}</div></div>`;
    case 'x-outro': return `<div class="main"><div class="title" style="font-size:76px">${esc(s.line)}</div><div class="url">${SITE}</div><div class="sub">Odkaz v popisu videa · ${esc(s.sub)}</div><div class="subs">🔔 Odebírejte kanál – každý den nové video</div>${s.nxt ? `<div class="tr" style="font-size:40px;color:var(--c);font-weight:700">Zítra: ${esc(s.nxtlab)} – ${esc(s.nxt)}</div>` : ''}</div>`;
    case 'f-q': case 'f-q-wait': case 'f-a': return `<div class="main"><div class="sit" style="font-size:38px;margin-bottom:30px">${esc(s.sit)}</div><div class="field"><div class="lbl">${s.k}. ${esc(s.q)}</div><div class="box ${s.kind === 'f-a' ? 'ok' : ''}">${s.kind === 'f-a' ? esc(s.a) : ''}</div>${s.kind === 'f-a' ? `<div class="wc">✓ ${s.wc} slov (minimum 10)</div>` : ''}</div>${s.kind === 'f-q-wait' ? `<div class="wait"><div class="cd">${s.c}</div>${esc(s.msg)}</div>` : ''}</div>`;
    case 'd-card': return `<div class="main"><div class="sit">${esc(s.sit)}</div><div class="goal">${esc(s.goal)}</div><div class="cues">${s.cues.map(c => `<div class="cue">${esc(c)}</div>`).join('')}</div></div>`;
    case 'd-cue-wait': case 'd-chat': { const ln = (s.lines || []).map(([r, t]) => `<div class="bub ${r === 'U' ? 'u' : 't'}"><small>${r === 'U' ? 'VY' : 'ZKOUŠEJÍCÍ'}</small>${esc(t)}</div>`).join('');
      return `<div class="main" style="justify-content:flex-start;padding-top:30px"><div class="sit" style="font-size:44px">${esc(s.sit)} ${esc(s.goal)}</div><div class="cues" style="margin-top:22px">${s.cues.map((c, i) => `<div class="cue ${i === s.k - 1 ? 'on' : ''}" style="font-size:32px;padding:12px 22px">${esc(c)}</div>`).join('')}</div><div style="display:flex;flex-direction:column;width:1550px;margin-top:20px">${ln}</div>${s.kind === 'd-cue-wait' ? `<div class="wait" style="margin-top:20px"><div class="cd">${s.c}</div>${esc(s.msg)}</div>` : ''}</div>`; }
    case 'v-pics': case 'v-pics-wait': if (s.scn) return `<div class="main" style="justify-content:flex-start;padding-top:18px"><div class="sit" style="font-size:46px">${esc(s.q)}</div><div class="prow"><div class="cg">${s.pics.map((x, i) => `<div class="cp"><img src="file://${s.scn[i]}"><b>${i + 1}</b><span>${esc(x.t)}</span></div>`).join('')}</div>${s.kind === 'v-pics-wait' ? `<div class="waitov"><div class="cd">${s.c}</div>${esc(s.msg)}</div>` : ''}</div></div>`;
      return `<div class="main"><div class="sit">${esc(s.q)}</div><div class="p4">${s.pics.map((x, i) => `<div class="pic"><img src="file://${OM}${x.om}.svg"><span>${i + 1}. ${esc(x.t)}</span></div>`).join('')}</div>${s.kind === 'v-pics-wait' ? `<div class="wait"><div class="cd">${s.c}</div>${esc(s.msg)}</div>` : ''}</div>`;
    case 'v-model': if (s.scn) { const MP = [0, 0, 0, 1, 1, 2, 2, 3, 3, 3]; const j = MP[Math.max(0, s.hi)] ?? 3;
      return `<div class="story2"><div class="bp"><div class="big"><img src="file://${s.scn[j]}"><b>${j + 1}</b></div><div class="cap">${esc(s.pics[j].t)}</div><div class="th">${s.scn.map((f, i) => `<img class="${i === j ? 'on' : ''}" src="file://${f}">`).join('')}</div></div><div class="mail"><div class="mh"><b>${esc(s.q)}</b><span class="pvl">podtrženo = minulý čas</span></div>${s.sents.map((t, k) => `<span class="s ${k === s.hi ? 'on' : (k > s.hi ? 'gr' : '')}">${pastMark(t)}</span>`).join(' ')}</div></div>`; }
      return `<div class="story"><div class="side">${s.pics.map(x => `<div class="pic"><img src="file://${OM}${x.om}.svg"><span>${esc(x.t)}</span></div>`).join('')}</div><div class="mail"><div class="mh"><b>${esc(s.q)}</b><span class="pvl">podtrženo = minulý čas</span></div>${s.sents.map((t, k) => `<span class="s ${k === s.hi ? 'on' : (k > s.hi ? 'gr' : '')}">${pastMark(t)}</span>`).join(' ')}</div></div>`;
    case 'r-task': case 'r-task-wait': return `<div class="main"><div class="sit">${esc(s.sit)}</div><div class="opts">${s.opts.map(o => o.scn ? `<div class="opt sc"><img src="file://${o.scn}"><span>${esc(o.t)}</span></div>` : `<div class="opt"><img src="file://${OM}${o.om}.svg">${esc(o.t)}</div>`).join('')}</div>${s.kind === 'r-task-wait' ? `<div class="wait"><div class="cd">${s.c}</div>${esc(s.msg)}</div>` : ''}</div>`;
    case 'r-dialog': return `<div class="chat">${s.lines.slice(-5).map(([r, t]) => `<div class="bub ${r === 'U' ? 'u' : 't'}"><small>${r === 'U' ? 'VY' : 'ZKOUŠEJÍCÍ'}</small>${esc(t)}</div>`).join('')}</div>`;
    case 'm-intro': return `<div class="main"><span class="chip">Téma ${s.n} / 40</span><div class="title">${esc(s.cz)}</div><div class="sub">10 otázek · poslouchejte a odpovězte nahlas</div><div class="tr">${esc(p.uk)} · ${esc(p.ru)} · ${esc(p.en)} · ${esc(p.vi)}</div></div>`;
    case 'm-q': return `<div class="main"><div class="card"><div class="qn">OTÁZKA ${s.k} / 10</div><div class="q">${esc(s.q)}</div></div></div>`;
    case 'm-wait': return `<div class="main"><div class="card"><div class="qn">OTÁZKA ${s.k} / 10</div><div class="q">${esc(s.q)}</div></div><div class="wait"><div class="cd">${s.c}</div>Teď vy! Odpovězte nahlas.</div></div>`;
    case 'm-a': return `<div class="main"><div class="qs">${s.k}. ${esc(s.q)}</div><div class="card ans"><div class="al">VZOROVÁ ODPOVĚĎ</div><div class="a">${esc(s.a)}</div></div></div>`;
    case 'm-outro': return `<div class="main"><div class="title" style="font-size:84px">Procvičte si téma ${s.n} na webu</div><div class="url">${SITE}</div><div class="sub">Odkaz v popisu videa · web poslouchá a kontroluje vaši odpověď · zdarma</div><div class="subs">🔔 Odebírejte kanál – každý den nové video</div>${s.nxt ? `<div class="tr" style="font-size:40px;color:#1f5fbf;font-weight:700">Zítra: Téma ${s.n + 1} – ${esc(s.nxt)}</div>` : ''}</div>`;
    case 'p-intro': return `<div class="main"><span class="chip">E-mail ${s.n} / 40</span><div class="title">${esc(s.subj)}</div><div class="sub">Psaní · úloha 2 · minimálně 35 slov · 12 bodů</div></div>`;
    case 'p-task': return `<div class="main"><div class="sit">${esc(s.sit)}</div><div class="to">Komu: ${esc(s.to)}</div><div class="pics">${s.pr.map(pic).join('')}</div></div>`;
    case 'p-wait': return `<div class="main"><div class="sit" style="font-size:44px">${esc(s.sit)}</div><div class="pics">${s.pr.map(pic).join('')}</div><div class="wait"><div class="cd">${s.c}</div>Zastavte video a napište e-mail.</div></div>`;
    case 'p-model': {
      const ss = s.sents.map((t, k) => `<span class="s ${k === s.hi ? 'on' : (s.hi >= 0 && k > s.hi ? 'gr' : '')}">${esc(t)}</span>`).join(' ');
      return `<div class="model"><div class="side">${s.pr.map(pic).join('')}</div><div class="mail"><div class="mh">Komu: <b>${esc(s.to)}</b> · Předmět: <b>${esc(s.subj)}</b></div><div class="${s.hi === -1 ? 's on' : ''}" style="display:inline-block">${esc(s.greet)}</div><div>${ss}</div><div class="cl ${s.hi >= 0 && s.hi < s.sents.length - 1 ? 's gr' : ''}">${esc(s.close)}</div></div></div>`;
    }
    case 'p-tip': return `<div class="main"><div class="tips"><div>${s.wc} slov (minimum je 35)</div><div>1 věta na každý obrázek</div><div>Pozdrav na začátku i na konci</div></div></div>`;
    case 'p-outro': return `<div class="main"><div class="title" style="font-size:84px">Napište svůj e-mail na webu</div><div class="url">${SITE}</div><div class="sub">Odkaz v popisu videa · web počítá slova a kontroluje e-mail · zdarma</div><div class="subs">🔔 Odebírejte kanál – každý den nové video</div>${s.nxt ? `<div class="tr" style="font-size:40px;color:#15803d;font-weight:700">Zítra: E-mail ${s.n + 1} – ${esc(s.nxt)}</div>` : ''}</div>`;
  }
}
(async () => {
  const b = await chromium.launch();
  const pg = await b.newPage({ viewport: { width: 1920, height: 1080 } });
  for (const id of process.argv.slice(2)) {
    const dir = `${process.env.YT_OUT || '/home/claude/yt/out'}/${id}`;
    const p = JSON.parse(fs.readFileSync(`${dir}/plan.json`, 'utf8'));
    const seen = {};
    for (let i = 0; i < p.segs.length; i++) {
      const s = p.segs[i].slide; const key = JSON.stringify(s);
      if (seen[key]) { p.segs[i].img = seen[key]; continue; }
      const f = `${dir}/slide${String(i).padStart(3, '0')}.jpg`;
      fs.writeFileSync(`${dir}/tmp.html`, frame(p, s, body(p, s)));
      await pg.goto(`file://${dir}/tmp.html`); await pg.waitForTimeout(80);
      await pg.screenshot({ path: f, type: 'jpeg', quality: 92 });
      p.segs[i].img = f; seen[key] = f;
    }
    fs.writeFileSync(`${dir}/plan.json`, JSON.stringify(p));
    console.log(id, Object.keys(seen).length, 'slides');
  }
  await b.close();
})();

// OG-картка сайту 1200x630 (22.11.2026). Шрифти IBM Plex Sans Bold/SemiBold з github.com/IBM/plex → /tmp/claude-0/og/, hero.svg з img/home/. Вихід: og-card*.jpg → img/og/ і og-image*.jpg
const {chromium}=require('playwright');const fs=require('fs');
const T={
 '':{t:['Іспит A2 з чеської','для ПМЖ —'],y:'безкоштовно',l:['20 повних варіантів нового формату','Голоси, таймер і бали як на іспиті','Відеоуроки щодня · 4 мови'],c:'Почати тест'},
 en:{t:['Czech A2 exam for','permanent residence'],y:'free practice',l:['20 full tests in the 2026 format','Real voices, timer and scoring','Daily video lessons · 4 languages'],c:'Start the test'},
 ru:{t:['Экзамен A2','по чешскому —'],y:'бесплатно',l:['20 полных вариантов нового формата','Голоса, таймер и баллы как на экзамене','Видеоуроки каждый день · 4 языка'],c:'Начать тест'},
 vi:{t:['Thi A2 tiếng Séc','cho thường trú —'],y:'miễn phí',l:['20 đề thi đầy đủ định dạng 2026','Giọng đọc thật, hẹn giờ, chấm điểm','Video bài học mỗi ngày · 4 ngôn ngữ'],c:'Bắt đầu thi'}};
const svg=fs.readFileSync('hero.svg','utf8');
(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:1200,height:630}});
for(const [k,v] of Object.entries(T)){
const html=`<html><head><style>
@font-face{font-family:P;src:url(file:///tmp/claude-0/og/IBMPlexSans-Bold.ttf);font-weight:700}
@font-face{font-family:P;src:url(file:///tmp/claude-0/og/IBMPlexSans-SemiBold.ttf);font-weight:600}
*{margin:0;box-sizing:border-box}body{width:1200px;height:630px;font-family:P;color:#fff;overflow:hidden;
background:radial-gradient(circle,rgba(255,255,255,.09) 2px,transparent 2.5px) 0 0/28px 28px,linear-gradient(160deg,#0a2a63 0%,#123f94 100%);position:relative}
.l{position:absolute;left:64px;top:58px;width:640px}
.chip{display:inline-flex;align-items:center;gap:12px;padding:8px 18px 8px 8px;border-radius:999px;background:rgba(255,255,255,.12);border:1.5px solid rgba(255,255,255,.25);font-weight:600;font-size:22px;letter-spacing:.04em}
.chip b{background:#ffd23f;color:#0a2a63;border-radius:999px;padding:3px 12px;font-weight:700}
h1{margin-top:30px;font-weight:700;font-size:${k==='en'?54:58}px;line-height:1.08;letter-spacing:-.01em}
h1 .y{color:#ffd23f;display:block}
ul{list-style:none;padding:0;margin-top:26px;font-weight:600;font-size:25px;line-height:1.55;color:#dbe6ff}
li:before{content:'✓';font-family:'DejaVu Sans';color:#ffd23f;font-weight:700;margin-right:14px}
.cta{position:absolute;left:64px;bottom:52px;display:flex;gap:18px;align-items:center}
.btn{background:#ffd23f;color:#0a2a63;font-weight:700;font-size:28px;padding:14px 30px;border-radius:16px;box-shadow:0 6px 0 #c9a200}
.url{font-weight:700;font-size:28px;color:#fff;opacity:.95}
.art{position:absolute;right:-10px;top:40px;width:600px;height:525px}
.bar{position:absolute;left:0;right:0;bottom:0;height:12px;background:linear-gradient(90deg,#fff 0 33.3%,#d7141a 33.3% 66.6%,#11457e 66.6%)}
</style></head><body>
<div class="art">${svg.replace('<svg ','<svg style="width:100%;height:100%" ')}</div>
<div class="l"><div class="chip"><b>A2</b>ZKOUŠKA · TRVALÝ POBYT · 2026</div>
<h1>${v.t.join('<br>')}<span class="y">${v.y}</span></h1>
<ul>${v.l.map(x=>'<li>'+x+'</li>').join('')}</ul></div>
<div class="cta"><span class="btn">▶ ${v.c}</span><span class="url">zkouska-a2.cz</span></div><div class="bar"></div></body></html>`;
fs.writeFileSync('og'+(k?'-'+k:'')+'.html',html);
await p.goto('file:///tmp/claude-0/og/og'+(k?'-'+k:'')+'.html');await p.waitForTimeout(400);
await p.screenshot({path:'og-card'+(k?'-'+k:'')+'.jpg',type:'jpeg',quality:88});}
await b.close()})();

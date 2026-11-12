"""Генерує faq/ для en і vi з шаблону ru/faq/index.html (той самий дизайн). python3 tools/faq_gen.py"""
import json, re, os
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TPL = open(os.path.join(ROOT, 'ru/faq/index.html'), encoding='utf8').read()
OFF = 'https://cestina-pro-cizince.cz/trvaly-pobyt/a2/online-prihlaska/'
YT = 'https://www.youtube.com/channel/UCpkz24CVlceUnyC8PIF9KMA?sub_confirmation=1'

L = {
'en': dict(
 title='Czech A2 exam for permanent residence (trvalý pobyt): price, registration, points — FAQ',
 desc='Everything about the Czech A2 exam for permanent residence in 2026: new format, 4 parts, pass marks 42/70 and 24/40, price 3,200 CZK, registration, documents, results. Free mock exam.',
 og='Czech A2 exam for permanent residence: FAQ', ogd='Price, registration, points, documents and results — short answers with links to official sources.',
 back='← Zkouška A2 nanečisto · mock exam', h1='Czech A2 exam for permanent residence: frequently asked questions',
 lead='A short guide to the new exam format (from 11 April 2026), points, price, registration and results. Checked against the official website cestina-pro-cizince.cz (November 2026).',
 b1='▶ Take a free mock exam', b2='📚 Speaking and Writing lessons', b3='🔔 YouTube: a new video every day', b4='▶ Test yourself: A2 mock exam',
 src='Sources', srcn='Rules may change — check the official website before registering. Unofficial website',
 qa=[
  ('What is the A2 exam for permanent residence (trvalý pobyt)?', 'It is a Czech language exam at level A2. You submit the certificate together with your application for permanent residence in the Czech Republic. Since 11 April 2026 the exam has a <b>new format</b>.'),
  ('What parts does the exam have?', '<ul><li><b>Čtení</b> (reading) — 40 minutes, 25 points</li><li><b>Psaní</b> (writing) — 25 minutes, 20 points</li><li><b>Poslech</b> (listening) — about 40 minutes, 25 points</li><li><b>Mluvení</b> (speaking) — 15 minutes, 40 points</li></ul>Everything takes place on one day: the written part lasts almost 2 hours, the oral part about 15 minutes.'),
  ('How many points do I need to pass?', 'Written part (Čtení + Psaní + Poslech): at least <b>42 of 70</b> points (60 %). Oral part (Mluvení): at least <b>24 of 40</b> (60 %). If you fail even one part, you have to retake the whole exam.'),
  ('How much does the exam cost?', '<b>3,200 CZK</b>. The school must receive the payment no later than 8 days before the exam.'),
  ('How do I register?', f'Through the online application on the official website <a href="{OFF}" rel="noopener">cestina-pro-cizince.cz</a> or in person at one of the exam schools. The school will tell you when a place is available. You have to check and sign the application in person at the school, so your data must be accurate.'),
  ('When and where is the exam held?', 'At accredited schools all over the Czech Republic (list at cestina-pro-cizince.cz), usually on <b>Wednesday or Saturday from 9:00</b>. The number of places and dates is gradually increasing.'),
  ('What should I bring?', 'A <b>valid passport</b> (cestovní doklad). The school does not accept other documents.'),
  ('When will I get the result and the certificate?', 'The result comes by e-mail or SMS <b>within 9 days</b>. You can collect the certificate (Osvědčení o znalosti českého jazyka) in person within 30 days after the exam or receive it by post — as chosen in your application. The certificate is valid <b>indefinitely</b>.'),
  ('Can I cancel or move the exam?', 'At least 15 days before — e-mail the school with your full name, date of birth, passport number (and registration code, if you have one). Later you can cancel only because of illness or another serious reason with a document.'),
  ('How long should I prepare?', 'Officially at least <b>50 hours</b> of a course or self-study are recommended. On our website you can take 20 mock exams in the new format, study Speaking and Writing lessons with audio and watch a new video lesson on YouTube every day.'),
  ('Does everyone have to take this exam?', 'No. Some people are exempt (for example because of age or health) — the exact rules are in Nařízení vlády č. 31/2016 Sb. If in doubt, call the Ministry of the Interior info line: <b>+420 974 801 801</b> (Mon–Thu 8–16, Fri 8–12).'),
  ('Who made this website?', '“Zkouška A2 nanečisto” is an <b>unofficial free</b> learning project made by Andre, a Ukrainian living in the Czech Republic. No ads, no registration. The website is not connected with the exam organisers, so always check the current rules on the official website before registering.')]),
'vi': dict(
 title='Kỳ thi tiếng Séc A2 để xin thường trú (trvalý pobyt): lệ phí, đăng ký, điểm — Câu hỏi thường gặp',
 desc='Tất cả về kỳ thi tiếng Séc A2 để xin thường trú năm 2026: định dạng mới, 4 phần, điểm đạt 42/70 và 24/40, lệ phí 3.200 Kč, đăng ký, giấy tờ, kết quả. Thi thử miễn phí.',
 og='Kỳ thi A2 để xin thường trú ở Séc: câu hỏi thường gặp', ogd='Lệ phí, đăng ký, điểm, giấy tờ và kết quả — ngắn gọn, có liên kết tới nguồn chính thức.',
 back='← Zkouška A2 nanečisto · thi thử', h1='Kỳ thi tiếng Séc A2 để xin thường trú: câu hỏi thường gặp',
 lead='Tóm tắt về định dạng thi mới (từ 11/4/2026), điểm, lệ phí, đăng ký và kết quả. Đã đối chiếu với trang chính thức cestina-pro-cizince.cz (tháng 11/2026).',
 b1='▶ Thi thử miễn phí', b2='📚 Bài học Nói và Viết', b3='🔔 YouTube: mỗi ngày một video mới', b4='▶ Tự kiểm tra: thi thử A2',
 src='Nguồn', srcn='Quy định có thể thay đổi — hãy kiểm tra trang chính thức trước khi đăng ký. Trang không chính thức',
 qa=[
  ('Kỳ thi A2 để xin thường trú (trvalý pobyt) là gì?', 'Đây là kỳ thi tiếng Séc trình độ A2. Chứng chỉ được nộp cùng hồ sơ xin thường trú tại Séc. Từ ngày 11/4/2026 kỳ thi có <b>định dạng mới</b>.'),
  ('Kỳ thi gồm những phần nào?', '<ul><li><b>Čtení</b> (đọc) — 40 phút, 25 điểm</li><li><b>Psaní</b> (viết) — 25 phút, 20 điểm</li><li><b>Poslech</b> (nghe) — khoảng 40 phút, 25 điểm</li><li><b>Mluvení</b> (nói) — 15 phút, 40 điểm</li></ul>Tất cả diễn ra trong một ngày: phần viết gần 2 giờ, phần nói khoảng 15 phút.'),
  ('Cần bao nhiêu điểm để đỗ?', 'Phần viết (Čtení + Psaní + Poslech): tối thiểu <b>42/70</b> điểm (60 %). Phần nói (Mluvení): tối thiểu <b>24/40</b> (60 %). Nếu trượt dù chỉ một phần, bạn phải thi lại toàn bộ.'),
  ('Lệ phí thi bao nhiêu?', '<b>3.200 Kč</b>. Trường phải nhận được tiền chậm nhất 8 ngày trước kỳ thi.'),
  ('Đăng ký thi như thế nào?', f'Qua đơn trực tuyến trên trang chính thức <a href="{OFF}" rel="noopener">cestina-pro-cizince.cz</a> hoặc trực tiếp tại một trường tổ chức thi. Trường sẽ báo khi có chỗ trống. Bạn phải kiểm tra và ký đơn trực tiếp tại trường, vì vậy thông tin phải chính xác.'),
  ('Thi khi nào và ở đâu?', 'Tại các trường được công nhận trên khắp nước Séc (danh sách trên cestina-pro-cizince.cz), thường vào <b>thứ Tư hoặc thứ Bảy từ 9:00</b>. Số chỗ và ngày thi đang dần tăng lên.'),
  ('Cần mang theo gì?', '<b>Hộ chiếu còn hạn</b> (cestovní doklad). Trường không chấp nhận giấy tờ khác.'),
  ('Khi nào có kết quả và chứng chỉ?', 'Kết quả được gửi qua e-mail hoặc SMS <b>trong vòng 9 ngày</b>. Chứng chỉ (Osvědčení o znalosti českého jazyka) có thể nhận trực tiếp trong vòng 30 ngày sau kỳ thi hoặc qua bưu điện — theo lựa chọn trong đơn. Chứng chỉ có giá trị <b>vô thời hạn</b>.'),
  ('Có thể hủy hoặc dời ngày thi không?', 'Chậm nhất 15 ngày trước — gửi e-mail cho trường với họ tên, ngày sinh, số hộ chiếu (và mã đăng ký nếu có). Sau đó chỉ có thể hủy vì bệnh hoặc lý do nghiêm trọng khác có giấy tờ.'),
  ('Cần chuẩn bị bao lâu?', 'Chính thức khuyến nghị tối thiểu <b>50 giờ</b> học khóa hoặc tự học. Trên trang của chúng tôi bạn có thể làm 20 bài thi thử theo định dạng mới, học bài Nói và Viết có âm thanh và mỗi ngày xem video bài học mới trên YouTube.'),
  ('Ai cũng phải thi kỳ thi này?', 'Không. Một số người được miễn (ví dụ vì tuổi hoặc sức khỏe) — quy định chính xác trong Nařízení vlády č. 31/2016 Sb. Nếu chưa chắc, hãy gọi đường dây thông tin của Bộ Nội vụ: <b>+420 974 801 801</b> (T2–T5 8–16, T6 8–12).'),
  ('Ai làm trang web này?', '«Zkouška A2 nanečisto» là dự án học tập <b>không chính thức, miễn phí</b> do Andre — một người Ukraina sống ở Séc — thực hiện. Không quảng cáo, không đăng ký. Trang web không liên quan đến đơn vị tổ chức thi, vì vậy hãy luôn kiểm tra quy định hiện hành trên trang chính thức trước khi đăng ký.')]),
}

ALT = ''.join(f'<link rel="alternate" hreflang="{h}" href="https://zkouska-a2.cz/{p}faq/">\n' for h, p in [('uk', ''), ('ru', 'ru/'), ('en', 'en/'), ('vi', 'vi/')]) + '<link rel="alternate" hreflang="x-default" href="https://zkouska-a2.cz/faq/">\n'
SW = lambda me: ' · '.join(f'<a href="/{p}faq/" hreflang="{h}">{n}</a>' for h, p, n in [('uk', '', 'UA'), ('ru', 'ru/', 'RU'), ('en', 'en/', 'EN'), ('vi', 'vi/', 'VI')] if h != me)
strip = lambda h: re.sub('<[^>]+>', '', h)

def head_alts(html):
    return re.sub(r'(<link rel="alternate"[^>]*>\n)+', ALT, html, count=1)

for lang, d in L.items():
    ld = {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": strip(a)}} for q, a in d['qa']]}
    qa = '\n'.join(f'<details class="qa"{" open" if i < 3 else ""}><summary>{q}</summary><div>{a}</div></details>' for i, (q, a) in enumerate(d['qa']))
    style = TPL[TPL.index('<style>'):TPL.index('</style>') + 8]
    html = f'''<!doctype html>
<html lang="{lang}">
<head>
<script>if(/github\\.io$/.test(location.hostname)){{location.replace("https://zkouska-a2.cz"+location.pathname.replace(/^\\/zkouska-a2/,"")+location.search+location.hash);}}</script>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{d["title"]}</title>
<meta name="description" content="{d["desc"]}">
<link rel="canonical" href="https://zkouska-a2.cz/{lang}/faq/">
{ALT}<link rel="icon" type="image/png" sizes="32x32" href="/img/app/favicon-32.png">
<meta property="og:title" content="{d["og"]}">
<meta property="og:description" content="{d["ogd"]}">
<meta property="og:image" content="https://zkouska-a2.cz/og-image-{lang}.jpg">
<meta property="og:url" content="https://zkouska-a2.cz/{lang}/faq/">
<script type="application/ld+json">{json.dumps(ld, ensure_ascii=False)}</script>
{style}
</head>
<body>
<main>
<p><a href="/{lang}/">{d["back"]}</a> · {SW(lang)}</p>
<h1>{d["h1"]}</h1>
<p class="lead">{d["lead"]}</p>
<div class="cta"><a class="btn y" href="/{lang}/?utm_source=faq">{d["b1"]}</a><a class="btn" href="/learn/?lang={lang}">{d["b2"]}</a><a class="btn r" href="{YT}" rel="noopener" target="_blank">{d["b3"]}</a></div>
{qa}

<div class="cta"><a class="btn y" href="/{lang}/?utm_source=faq">{d["b4"]}</a></div>
<p class="src">{d["src"]}: <a href="https://cestina-pro-cizince.cz/trvaly-pobyt/a2/" rel="noopener">cestina-pro-cizince.cz/trvaly-pobyt/a2</a> (NPI ČR / MŠMT), <a href="https://cestina-pro-cizince.cz/trvaly-pobyt/a2/informace-ke-zkousce/" rel="noopener">Informace ke zkoušce</a>. {d["srcn"]} · <a href="/ochrana-osobnich-udaju.html">Ochrana osobních údajů</a></p>
</main>
</body>
</html>
'''
    os.makedirs(os.path.join(ROOT, lang, 'faq'), exist_ok=True)
    open(os.path.join(ROOT, lang, 'faq', 'index.html'), 'w', encoding='utf8').write(html)

# uk + ru: hreflang на всі 4 мови і перемикач
for p, me in [('faq/index.html', 'uk'), ('ru/faq/index.html', 'ru')]:
    f = os.path.join(ROOT, p); h = open(f, encoding='utf8').read()
    h = head_alts(h)
    h = re.sub(r'(<p><a href="/(?:ru/)?">[^<]*</a> · ).*?(</p>)', lambda m: m.group(1) + SW(me) + m.group(2), h, count=1)
    open(f, 'w', encoding='utf8').write(h)
print('ok')

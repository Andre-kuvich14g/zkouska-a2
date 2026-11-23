# Окремі сторінки тем для Google (23.11.2026, Search Console): 6 úloh × 40 тем + 6 хабів.
# python3 tools/topics/build_topics.py  ->  temata/<úloha>/<NN-slug>/index.html, temata/<úloha>/index.html, temata/index.html
import json, os, re, sys, html, unicodedata
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, os.path.join(ROOT, 'tools', 'learn'))
from u1_a import U1_A; from u1_b import U1_B; from u1_c import U1_C; from u1_d import U1_D
import u2, u3, u4
from w12 import W1, W2
BASE = 'https://zkouska-a2.cz/'
E = lambda s: html.escape(str(s), quote=True)
IDS = json.load(open(os.path.join(ROOT, 'yt-upload', 'ids.json'), encoding='utf-8'))
META = json.load(open(os.path.join(ROOT, 'yt-upload', 'meta.json'), encoding='utf-8'))
U1 = U1_A + U1_B + U1_C + U1_D

def slug(s):
    s = unicodedata.normalize('NFKD', s).encode('ascii', 'ignore').decode().lower()
    return re.sub(r'[^a-z0-9]+', '-', s).strip('-')[:60]

def gz(t):  # чоловіча/жіноча форма: «přijel/a» -> «přijel(a)» для читабельності
    return re.sub(r'(\w+)/(\w+)', lambda m: m.group(1) + '/' + m.group(2), t)

# (ключ, slug розділу, назва CZ, назва UA, літера відео, хеш /learn, бали, опис úlohy UA, опис CZ)
SEC = [
 ('w1', 'psani-1-formular', 'Psaní 1 – Formulář', 'Письмо 1 – формуляр', 'f', 'w1', 8,
  'Три питання у формулярі: відповідайте повним реченням, мінімум 10 слів у кожній відповіді.', 'Tři otázky ve formuláři, odpovědi celou větou (min. 10 slov).'),
 ('w2', 'psani-2-email', 'Psaní 2 – E-mail', 'Письмо 2 – e-mail', 'p', 'w2', 12,
  'E-mail за 5 картинками: мінімум 35 слів, одне речення до кожної картинки, привітання й підпис.', 'E-mail podle 5 obrázků, min. 35 slov, ke každému obrázku jedna věta.'),
 ('u1', 'mluveni-1-otazky', 'Mluvení 1 – Otázky k tématu', 'Мовлення 1 – питання до теми', 'm', 'u1', 8,
  'Екзаменатор вибирає 2 теми і ставить по 4 питання. Відповідайте повним реченням, краще двома.', 'Zkoušející vybere 2 témata a položí 4 otázky. Odpovídejte celou větou.'),
 ('u2', 'mluveni-2-karta', 'Mluvení 2 – Karta: ptejte se', 'Мовлення 2 – картка: поставте питання', 'd', 'u2', 12,
  'Картка з ситуацією: поставте 4 питання (останнє — своє) і відреагуйте на відповіді.', 'Karta se situací: položte 4 otázky (poslední vlastní).'),
 ('u3', 'mluveni-3-pribeh', 'Mluvení 3 – Příběh podle obrázků', 'Мовлення 3 – розповідь за картинками', 'v', 'u3', 10,
  'Розкажіть історію за 4 картинками в минулому часі.', 'Vyprávějte příběh podle 4 obrázků v minulém čase.'),
 ('u4', 'mluveni-4-situace', 'Mluvení 4 – Řešení situace', 'Мовлення 4 – розв\'язання ситуації', 'r', 'u4', 7,
  'Домовтеся з екзаменаторкою (на «ти»): виберіть 1 з 3 варіантів і поясніть чому.', 'Domluvte se se zkoušející, vyberte 1 ze 3 možností a řekněte proč.'),
]

def items(key):
    if key == 'u1': return [dict(cz=cz, uk=tr[0], qa=qa) for cz, tr, qa in U1]
    if key == 'u2': return [dict(cz=x['cz'], uk='', d=x) for x in u2.U2]
    if key == 'u3': return [dict(cz=x['title'], uk=x['t'][0], d=x) for x in u3.U3]
    if key == 'u4': return [dict(cz=x['cz'], uk='', d=x) for x in u4.U4]
    if key == 'w1': return [dict(cz=x['cz'], uk='', d=x) for x in W1]
    if key == 'w2': return [dict(cz=x['cz'], uk='', d=x) for x in W2]

def body(key, it):
    d = it.get('d')
    if key == 'u1':
        return '<h2>10 otázek a vzorové odpovědi</h2><ol class="qa">' + ''.join(f'<li><b>{E(q)}</b><br><span>{E(gz(a))}</span></li>' for q, a in it['qa']) + '</ol>'
    if key == 'u2':
        h = f'<h2>Situace</h2><p class="card"><b>{E(d["situation"])}</b> {E(d["goal"])}</p><h2>4 otázky (vzor)</h2><ol class="qa">'
        h += ''.join(f'<li><b>{E(k)}</b><br><span>{E(v)}</span></li>' for k, v in d['pairs']) + '</ol>'
        h += '<h2>Vzorový dialog</h2><div class="dlg">' + ''.join(f'<p class="{"t" if s == "T" else "u"}"><b>{"Zkoušející" if s == "T" else "Vy"}:</b> {E(x)}</p>' for s, x in d['dialog']) + '</div>'
        return h
    if key == 'u3':
        h = f'<h2>Zadání</h2><p class="card"><b>{E(d["q"])}</b> Vyprávějte v minulém čase.</p><ol class="qa">' + ''.join(f'<li>{E(p)}</li>' for p in d['pictures']) + '</ol>'
        return h + f'<h2>Vzorové vyprávění</h2><p class="model">{E(gz(d["model"]))}</p>'
    if key == 'u4':
        h = f'<h2>Situace</h2><p class="card"><b>{E(d["situation"])}</b></p><p>Možnosti: ' + ' · '.join(f'<b>{E(o["label"])}</b>' for o in d['options']) + '</p>'
        return h + '<h2>Vzorový dialog</h2><div class="dlg">' + ''.join(f'<p class="{"t" if s == "T" else "u"}"><b>{"Zkoušející" if s == "T" else "Vy"}:</b> {E(x)}</p>' for s, x in d['dialog']) + '</div>'
    if key == 'w1':
        return f'<h2>Zadání</h2><p class="card">{E(d["situation"])}</p><h2>Otázky a vzorové odpovědi</h2><ol class="qa">' + ''.join(f'<li><b>{E(q)}</b><br><span>{E(gz(a))}</span> <small>({len(a.split())} slov)</small></li>' for q, a in d['qa']) + '</ol>'
    if key == 'w2':
        h = f'<h2>Zadání</h2><p class="card">{E(d["situation"])}</p><ol class="qa">' + ''.join(f'<li>{E(p["q"].capitalize())}</li>' for p in d['prompts']) + '</ol>'
        m = d['model']; return h + f'<h2>Vzorový e-mail ({len(m.split())} slov)</h2><p class="model">{E(gz(m)).replace(chr(10), "<br>")}</p>'

CSS = """:root{--bg:#eef1f6;--sheet:#fff;--ink:#15213a;--muted:#59647a;--rule:#d5dbe6;--accent:#1f4e9c;--y:#ffd400;color-scheme:light}
@media (prefers-color-scheme: dark){:root{--bg:#0d121c;--sheet:#151c2a;--ink:#e5e9f1;--muted:#9aa4b8;--rule:#29334a;--accent:#7ea4ff;color-scheme:dark}}
*{box-sizing:border-box}body{margin:0;background:var(--bg);color:var(--ink);font:17px/1.6 "Segoe UI",Roboto,Arial,sans-serif;padding:16px 16px 48px}
main{max-width:780px;margin:0 auto;background:var(--sheet);border:1px solid var(--rule);border-radius:16px;padding:clamp(16px,4vw,32px)}
h1{font-size:clamp(1.35rem,4vw,1.85rem);line-height:1.2;margin:6px 0 8px}h2{font-size:1.15rem;margin:22px 0 8px}
a{color:var(--accent)}.lead,.bc,small{color:var(--muted)}.bc{font-size:.92rem}
.card{border-left:4px solid var(--accent);padding:8px 12px;background:rgba(31,78,156,.07);border-radius:8px}
.qa li{margin:0 0 10px}.qa span{display:inline-block;margin-top:2px}.model{white-space:normal;background:rgba(255,212,0,.12);border-radius:10px;padding:12px}
.dlg p{margin:4px 0;padding:6px 10px;border-radius:10px}.dlg .t{background:rgba(31,78,156,.08)}.dlg .u{background:rgba(34,177,76,.10)}
.vid{display:block;position:relative;border-radius:12px;overflow:hidden;margin:12px 0}.vid img{width:100%;height:auto;display:block;aspect-ratio:16/9;object-fit:cover}
.vid b{position:absolute;inset:auto 12px 12px auto;background:#e1251b;color:#fff;padding:8px 14px;border-radius:10px}
.cta{display:flex;flex-wrap:wrap;gap:10px;margin:18px 0}.btn{display:inline-block;text-decoration:none;font-weight:800;border-radius:12px;padding:11px 16px;border:1px solid var(--rule);color:var(--ink);background:var(--sheet)}
.btn.y{background:var(--y);color:#1b1b1b;border-color:#c9a800}.btn.r{background:#e1251b;color:#fff;border-color:#e1251b}.btn.tg{background:#229ed9;color:#fff;border-color:#229ed9}
.nav{display:flex;justify-content:space-between;gap:10px;margin-top:20px;border-top:1px solid var(--rule);padding-top:12px}.list{columns:2;padding-left:1.2em}@media(max-width:560px){.list{columns:1}}"""

def page(title, desc, canon, h1, inner, ld):
    return f'''<!doctype html>
<html lang="cs">
<head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{E(title)}</title>
<meta name="description" content="{E(desc)}">
<link rel="canonical" href="{canon}">
<link rel="icon" type="image/png" sizes="32x32" href="/img/app/favicon-32.png">
<meta property="og:title" content="{E(title)}"><meta property="og:description" content="{E(desc)}"><meta property="og:url" content="{canon}"><meta property="og:type" content="article"><meta property="og:image" content="{BASE}img/og/og-card.jpg">
<style>{CSS}</style>
<script type="application/ld+json">{json.dumps(ld, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")}</script>
</head>
<body><main>
{inner}
</main></body></html>
'''

def cta(sec, n):
    return (f'<div class="cta"><a class="btn y" href="/?utm_source=temata&amp;utm_content={sec}-{n}">▶ Cvičná zkouška A2 zdarma / Безкоштовний пробний іспит</a>'
            f'<a class="btn" href="/learn/?utm_source=temata#{sec}-{n - 1}">🎧 Procvičit s audiem</a>'
            f'<a class="btn r" href="https://www.youtube.com/channel/UCpkz24CVlceUnyC8PIF9KMA?sub_confirmation=1" rel="noopener">🔔 YouTube</a>'
            f'<a class="btn tg" href="https://t.me/zkouska_A2_cz" rel="noopener">✈ Telegram</a></div>')

def build():
    out = os.path.join(ROOT, 'temata'); urls = []
    hub_links = []
    for key, sslug, cz, uk, vl, lh, pts, d_uk, d_cz in SEC:
        its = items(key); links = []
        for i, it in enumerate(its):
            n = i + 1; ps = f'{n:02d}-{slug(it["cz"])}'; links.append((n, it, ps))
        for n, it, ps in links:
            url = f'{BASE}temata/{sslug}/{ps}/'
            vid = IDS.get(f'{vl}{n:02d}'); vm = META.get(f'{vl}{n:02d}', {})
            topic = it['cz'] + (f' ({it["uk"]})' if it['uk'] else '')
            title = f'{cz.split(" – ")[0]} {n}/40: {it["cz"]} – vzor na plný počet bodů | Zkouška A2 trvalý pobyt'
            if len(title) > 95: title = f'{cz.split(" – ")[0]} {n}/40: {it["cz"]} – vzor | Zkouška A2'
            desc = f'{cz}, téma {n}/40 „{it["cz"]}“: zadání a vzorová odpověď na plný počet bodů ({pts} b.). {uk}: зразок відповіді до іспиту A2 на ПМП (trvalý pobyt).'
            inner = f'<p class="bc"><a href="/">Zkouška A2 nanečisto</a> › <a href="/temata/">Témata</a> › <a href="/temata/{sslug}/">{E(cz)}</a> › {n}/40</p>'
            inner += f'<h1>{E(cz.split(" – ")[0])} · {n}/40: {E(topic)}</h1>'
            inner += f'<p class="lead">{E(d_cz)} <b>{pts} bodů.</b><br>{E(d_uk)}</p>'
            ld = [{'@context': 'https://schema.org', '@type': 'BreadcrumbList', 'itemListElement': [
                {'@type': 'ListItem', 'position': 1, 'name': 'Zkouška A2 nanečisto', 'item': BASE},
                {'@type': 'ListItem', 'position': 2, 'name': 'Témata', 'item': BASE + 'temata/'},
                {'@type': 'ListItem', 'position': 3, 'name': cz, 'item': f'{BASE}temata/{sslug}/'},
                {'@type': 'ListItem', 'position': 4, 'name': it['cz'], 'item': url}]}]
            if isinstance(vid, str) and os.path.exists(os.path.join(ROOT, 'learn', 'yt', vid + '.jpg')):
                inner += f'<a class="vid" href="https://www.youtube.com/watch?v={vid}" rel="noopener"><img src="/learn/yt/{vid}.jpg" alt="{E(vm.get("title", it["cz"]))}" width="640" height="360" loading="lazy"><b>▶ Video lekce</b></a>'
                if vm.get('date'):
                    ld.append({'@context': 'https://schema.org', '@type': 'VideoObject', 'name': vm['title'][:100], 'description': desc[:300],
                               'thumbnailUrl': f'{BASE}learn/yt/{vid}.jpg', 'uploadDate': vm['date'] + 'T' + vm.get('time', '12:00') + ':00+01:00',
                               'embedUrl': f'https://www.youtube.com/embed/{vid}', 'url': f'https://www.youtube.com/watch?v={vid}', 'inLanguage': 'cs'})
            inner += body(key, it) + cta(lh, n)
            prev = links[n - 2] if n > 1 else None; nxt = links[n] if n < len(links) else None
            inner += '<div class="nav">' + (f'<a href="../{prev[2]}/">← {prev[0]}. {E(prev[1]["cz"])}</a>' if prev else '<span></span>') + (f'<a href="../{nxt[2]}/">{nxt[0]}. {E(nxt[1]["cz"])} →</a>' if nxt else '') + '</div>'
            p = os.path.join(out, sslug, ps); os.makedirs(p, exist_ok=True)
            open(os.path.join(p, 'index.html'), 'w', encoding='utf-8').write(page(title, desc, url, '', inner, ld)); urls.append(url)
        # хаб úlohy
        hurl = f'{BASE}temata/{sslug}/'
        inner = f'<p class="bc"><a href="/">Zkouška A2 nanečisto</a> › <a href="/temata/">Témata</a> › {E(cz)}</p><h1>{E(cz)}: všech 40 témat se vzory</h1>'
        inner += f'<p class="lead">{E(d_cz)} <b>{pts} bodů.</b><br>{E(uk)}: {E(d_uk)}</p>'
        inner += '<ol class="list">' + ''.join(f'<li><a href="{ps}/">{E(it["cz"])}</a>{" · " + E(it["uk"]) if it["uk"] else ""}</li>' for n, it, ps in links) + '</ol>' + cta(lh, 1)
        open(os.path.join(out, sslug, 'index.html'), 'w', encoding='utf-8').write(page(f'{cz}: 40 témat se vzorovými odpověďmi | Zkouška A2 trvalý pobyt',
            f'{cz} – všech 40 témat zkoušky A2 pro trvalý pobyt se vzorovými odpověďmi. {uk}: 40 тем зі зразками.', hurl, '', inner,
            [{'@context': 'https://schema.org', '@type': 'CollectionPage', 'name': cz, 'url': hurl}]))
        urls.append(hurl); hub_links.append((sslug, cz, uk))
    inner = '<p class="bc"><a href="/">Zkouška A2 nanečisto</a> › Témata</p><h1>Zkouška A2 (trvalý pobyt): všechna témata Psaní a Mluvení se vzory</h1>'
    inner += '<p class="lead">240 témat nového formátu zkoušky (od 11. 4. 2026) – zadání a vzorové odpovědi na plný počet bodů.<br>Усі 240 тем письмової та усної частини іспиту A2 на ПМП зі зразками відповідей.</p><ul>'
    inner += ''.join(f'<li><a href="{s}/"><b>{E(c)}</b></a> · {E(u)} · 40 témat</li>' for s, c, u in hub_links) + '</ul>' + cta('u1', 1)
    open(os.path.join(out, 'index.html'), 'w', encoding='utf-8').write(page('Témata zkoušky A2 pro trvalý pobyt: Psaní a Mluvení se vzory (240 témat)',
        'Všech 240 témat Psaní a Mluvení zkoušky A2 pro trvalý pobyt se vzorovými odpověďmi. 240 тем іспиту A2 на ПМП зі зразками.', BASE + 'temata/', '', inner,
        [{'@context': 'https://schema.org', '@type': 'CollectionPage', 'name': 'Témata zkoušky A2', 'url': BASE + 'temata/'}]))
    urls.insert(0, BASE + 'temata/')
    json.dump(urls, open(os.path.join(HERE, 'urls.json'), 'w'), indent=0)
    print('pages:', len(urls))

if __name__ == '__main__': build()

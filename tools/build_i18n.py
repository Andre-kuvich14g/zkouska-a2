# Збирає мовні версії сайту з українського index.html:  python3 tools/build_i18n.py
# Створює en/index.html, ru/index.html, vi/index.html і оновлює sitemap.xml.
import json, re, sys, os, datetime
sys.path.insert(0, os.path.dirname(__file__))
from i18n_extract import segments, CYR
from i18n_tr import T, KEEP
from why_tr import X
BASE = 'https://andre-kuvich14g.github.io/zkouska-a2/'
LANGS = {'en': (0, 'en_US'), 'ru': (1, 'ru_RU'), 'vi': (2, 'vi_VN')}
DATA_RE = re.compile(r'(<script type="application/json" id="exam-data">)(.*?)(</script>)', re.S)

def blob(d): return json.dumps(d, ensure_ascii=False, separators=(',', ':')).replace('</', '<\\/')

def build(src, lang):
    col, locale = LANGS[lang]
    table = {t[0]: t[1 + col].replace("'", '’') for t in T}
    segs = segments(src)
    miss = [x for x in segs if x not in table and x not in KEEP]
    if miss: raise SystemExit('Немає перекладу для: ' + repr(miss[:5]))
    m = DATA_RE.search(src); tpl = src[:m.start(2)] + '@@DATA@@' + src[m.end(2):]
    # захищаємо рядки, які мають лишитись як є
    for i, k in enumerate(KEEP): tpl = tpl.replace(k, f'@@KEEP{i}@@')
    pat = re.compile('|'.join(re.escape(k) for k in sorted(table, key=len, reverse=True)))
    tpl = pat.sub(lambda m: table[m.group(0)], tpl)  # один прохід: перекладене не перекладається вдруге
    for i, k in enumerate(KEEP): tpl = tpl.replace(f'@@KEEP{i}@@', k)
    if lang != 'ru':
        left = [l for l in tpl.split('\n') if CYR.search(l) and not any(k in l for k in KEEP)]
        if left: raise SystemExit(f'[{lang}] залишився український текст: ' + left[0][:200])
    left = [x for x in segs if x not in KEEP and table[x] != x and x in tpl and not any(x in v for v in table.values())]
    if left: raise SystemExit(f'[{lang}] не перекладено: ' + repr(left[:5]))
    url = BASE + lang + '/'
    rep = [('<html lang="uk">', f'<html lang="{lang}">'),
           (f'<link rel="canonical" href="{BASE}">', f'<link rel="canonical" href="{url}">'),
           (f'<meta property="og:url" content="{BASE}">', f'<meta property="og:url" content="{url}">'),
           ('content="uk_UA"', f'content="{locale}"'),
           (BASE + 'og-image.jpg', BASE + f'og-image-{lang}.jpg'),
           (f"url = '{BASE}'", f"url = '{url}'"),
           ('src="img/om/', 'src="../img/om/'), ('`img/om/', '`../img/om/'), ('"img/om/', '"../img/om/'),
           ('href="ochrana-osobnich-udaju.html"', 'href="../ochrana-osobnich-udaju.html"'),
           ('href="zdroje-obrazku.html"', 'href="../zdroje-obrazku.html"')]
    for a, b in rep: tpl = tpl.replace(a, b)
    d = json.load(open('data-variants.json', encoding='utf-8'))
    for v in d['variants']:
        R, L = v['reading'], v['listening']
        seq = R['t2']['items'] + L['t1']['items'] + L['t2']['items'] + L['t3']['items'] + L['t4']['items']
        for i, it in enumerate(seq):
            k = (v['id'], i)
            if k in X: it['why'] = X[k][col]
            elif CYR.search(it.get('why', '')): raise SystemExit(f'немає перекладу пояснення {k}')
    return tpl.replace('@@DATA@@', blob(d))

def sitemap():
    today = datetime.date.today().isoformat()
    alts = ''.join(f'<xhtml:link rel="alternate" hreflang="{h}" href="{BASE}{p}"/>' for h, p in [('uk', ''), ('en', 'en/'), ('ru', 'ru/'), ('vi', 'vi/'), ('x-default', '')])
    urls = ''.join(f'  <url><loc>{BASE}{p}</loc><lastmod>{today}</lastmod>{alts}</url>\n' for p in ['', 'en/', 'ru/', 'vi/'])
    open('sitemap.xml', 'w', encoding='utf-8').write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">\n' + urls + '</urlset>\n')

if __name__ == '__main__':
    src = open('index.html', encoding='utf-8').read()
    # дата «оновлено» в блоці «Що нового» ставиться автоматично під час кожного збирання
    try:
        from zoneinfo import ZoneInfo
        d = datetime.datetime.now(ZoneInfo('Europe/Prague')).date()
    except Exception:
        d = datetime.date.today()
    src2 = re.sub(r'<time id="updDate" datetime="[^"]*">[^<]*</time>',
                  f'<time id="updDate" datetime="{d.isoformat()}">{d.day:02d}.{d.month:02d}.{d.year}</time>', src)
    if src2 != src: open('index.html', 'w', encoding='utf-8').write(src2); src = src2
    for lang in LANGS:
        os.makedirs(lang, exist_ok=True)
        open(f'{lang}/index.html', 'w', encoding='utf-8').write(build(src, lang))
        print('OK', lang)
    sitemap(); print('OK sitemap')

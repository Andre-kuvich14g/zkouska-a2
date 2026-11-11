# Збирає сторінку «Вчимо Mluvení»: python3 tools/learn/build_learn.py  ->  learn/index.html
import json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
ROOT = os.path.dirname(os.path.dirname(HERE))
from ui import UI
from theory import THEORY
import theory_en, theory_ru, theory_vi, theory_w  # noqa: F401 (доповнюють THEORY)
from w12 import W1, W2
from u1_a import U1_A; from u1_b import U1_B; from u1_c import U1_C; from u1_d import U1_D

def opt(mod, name):
    try: return getattr(__import__(mod), name)
    except Exception: return []

# Лише відео нашого каналу @zkouska-a2cz (чужі відео прибрано 11.11.2026).
# Відео до тем беруться з yt-upload/ids.json + yt-upload/meta.json (поле link «#u1-4» -> тема).
CHANNEL = 'UCpkz24CVlceUnyC8PIF9KMA'
PLAYLISTS = {'w1': 'PLUQqjJU0hPfs', 'w2': 'PLEbZM6bcfLsA', 'u1': 'PLMPSqjkk5Axw', 'u2': 'PLZ9QkvIdNGFg',
             'u3': 'PLQZcneUaebBI', 'u4': 'PLK-4mNG0zlrk', 'l': 'PLDXeIemVzXw8', 'w': 'PLROyJEw4bAqA'}

def yt_data():
    ids = json.load(open(os.path.join(ROOT, 'yt-upload', 'ids.json'), encoding='utf-8'))
    meta = json.load(open(os.path.join(ROOT, 'yt-upload', 'meta.json'), encoding='utf-8'))
    secs = {u: {'pl': PLAYLISTS[u], 'v': {}} for u in ('u1', 'u2', 'u3', 'u4', 'w1', 'w2')}
    for key, vid in ids.items():  # мініатюра 640×360 для сайту з yt-upload/thumb2/<key>.jpg (якщо ще нема)
        src, dst = os.path.join(ROOT, 'yt-upload', 'thumb2', key + '.jpg'), os.path.join(ROOT, 'learn', 'yt', str(vid) + '.jpg')
        if isinstance(vid, str) and not key.startswith('s_') and os.path.exists(src) and not os.path.exists(dst):
            from PIL import Image
            os.makedirs(os.path.dirname(dst), exist_ok=True)
            Image.open(src).convert('RGB').resize((640, 360), Image.LANCZOS).save(dst, quality=80, optimize=True, progressive=True)
    for key, m in meta.items():
        vid = ids.get(key)
        if not vid or not isinstance(vid, str) or not os.path.exists(os.path.join(ROOT, 'learn', 'yt', vid + '.jpg')): continue
        link = m.get('link', '')
        h = link.split('#')[1] if '#' in link else ''
        if h.count('-') == 1 and h.split('-')[1].isdigit():
            u, i = h.split('-')
            if u in secs: secs[u]['v'][int(i)] = [vid, m['title'].replace('Zkouška A2 – ', '')]
    home = [[ids[k], meta[k]['title'].replace('Zkouška A2 – ', ''), PLAYLISTS[k[0]]] for k in ('w01', 'l02', 'l01') if k in ids and k in meta]
    return {'ch': CHANNEL, 'sec': secs, 'home': home}

def topics(rows): return [{'cz': cz, 't': tr, 'qa': [list(x) for x in qa]} for cz, tr, qa in rows]

def build():
    data = {
        'ui': UI, 'theory': THEORY, 'yt': yt_data(),
        'u1': topics(U1_A + U1_B + U1_C + U1_D),
        'u2': opt('u2', 'U2'), 'u3': [dict(x, cz=x['title']) for x in opt('u3', 'U3')], 'u4': opt('u4', 'U4'),
        'w1': W1, 'w2': W2,
    }
    blob = json.dumps(data, ensure_ascii=False, separators=(',', ':')).replace('</', '<\\/')
    tpl = open(os.path.join(HERE, 'template.html'), encoding='utf-8').read()
    os.makedirs(os.path.join(ROOT, 'learn'), exist_ok=True)
    open(os.path.join(ROOT, 'learn', 'index.html'), 'w', encoding='utf-8').write(tpl.replace('@@DATA@@', blob))
    print('OK learn/index.html', len(blob) // 1024, 'KB data;', {k: len(data[k]) for k in ('u1', 'u2', 'u3', 'u4', 'w1', 'w2')})

if __name__ == '__main__': build()

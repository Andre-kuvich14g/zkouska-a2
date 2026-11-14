"""Звірка YouTube ↔ сайт (правило Андре 14.11): кожне опубліковане відео з yt-upload/ids.json має бути на сайті (learn/),
а замінене відео — прибране. Запуск після кожної публікації/заміни: python3 tools/sync_check.py  (після build_learn.py)."""
import json, os, re, sys
R = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ids = json.load(open(f'{R}/yt-upload/ids.json', encoding='utf-8'))
site = ''.join(open(os.path.join(dp, f), encoding='utf-8', errors='ignore').read()
               for dp, _, fs in os.walk(f'{R}/learn') for f in fs if f.endswith(('.html', '.js', '.json')))
site += open(f'{R}/index.html', encoding='utf-8').read()
miss, stale = [], []
for k, v in ids.items():
    if not isinstance(v, str): continue
    if 'old' in k or 'unlisted' in k:          # замінені відео не повинні лишатися на сайті
        if v in site: stale.append((k, v))
        continue
    if k.startswith('s_') or k in ('t01', 'promo'):  # Shorts, трейлер і промо — тільки YouTube
        continue
    if v not in site: miss.append((k, v))
print(f'YouTube-відео: {len(ids)} · немає на сайті: {len(miss)} · застарілі на сайті: {len(stale)}')
for k, v in miss: print('  НЕМАЄ', k, v)
for k, v in stale: print('  ЗАМІНИТИ', k, v)
sys.exit(1 if miss or stale else 0)

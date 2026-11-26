"""Перекладені субтитри uk/ru/en/vi з <id>.cs.srt (відновлено 26.11.2026).

python3 tools/yt/srt_tr.py days/day19_srt.json f19 p19 ...
JSON-словник: {"чеський рядок": {"uk": "...", "ru": "...", "en": "...", "vi": "..."}, ...} — спільний для всього дня.
Без --write лише показує рядки, яких бракує у словнику (щоб дописати переклад).
"""
import json, os, re, sys
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
Y = os.path.join(ROOT, 'yt-upload')


def blocks(path):
    out = []
    for b in re.split(r'\n\s*\n', open(path, encoding='utf-8').read().strip()):
        ln = b.split('\n')
        if len(ln) >= 3: out.append((ln[0], ln[1], ' '.join(ln[2:])))
    return out


if __name__ == '__main__':
    args = [a for a in sys.argv[1:] if not a.startswith('--')]
    dp = args[0] if os.path.isabs(args[0]) else os.path.join(os.path.dirname(os.path.abspath(__file__)), args[0])
    D = json.load(open(dp, encoding='utf-8')) if os.path.exists(dp) else {}
    miss = []
    for id in args[1:]:
        B = blocks(f'{Y}/{id}.cs.srt')
        miss += [t for _, _, t in B if t not in D and t not in miss]
        if '--write' in sys.argv and not miss:
            for lang in ('uk', 'ru', 'en', 'vi'):
                open(f'{Y}/{id}.{lang}.srt', 'w', encoding='utf-8').write('\n'.join(f'{n}\n{tc}\n{D[t][lang]}\n' for n, tc, t in B))
            print(id, 'ok', len(B))
    if miss:
        print(json.dumps({t: {"uk": "", "ru": "", "en": "", "vi": ""} for t in miss}, ensure_ascii=False, indent=1))
        print('MISSING', len(miss))

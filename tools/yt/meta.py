"""meta.json (чеською) і tr.json (uk/ru/en/vi) для дня N — клонуванням записів попереднього дня (відновлено 26.11.2026).

python3 tools/yt/meta.py 19 2026-11-26
Назви тем іншими мовами: tools/yt/days/dayNN_tr.json  {"f19": {"uk": "...", "ru": "...", "en": "...", "vi": "..."}, ...}
tr.json ЗЛИВАЄТЬСЯ з наявним (нічого не перезаписує, крім ключів цього дня).
"""
import json, os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
ROOT = os.path.dirname(os.path.dirname(HERE))
import gen

SLOT = dict(f='14:00', p='15:00', m='16:00', d='17:00', v='18:00', r='19:00')


def names(D, k, n):
    e = D[k][n - 1]
    if k == 'm': return e[0], e[1][0]
    if k == 'p': return e['subject'], None
    if k == 'v': return e['title'], e['t'][0]
    return e['cz'], None


def renum(s, a, b):
    s = re.sub(rf'(?<![\d.]){a}(?![\d])', str(b), s)
    return re.sub(rf'#(\w\d)-{a - 1}\b', lambda m: f'#{m.group(1)}-{b - 1}', s)


def run(n, date):
    D = gen.data()
    mp = os.path.join(ROOT, 'yt-upload', 'meta.json'); tp = os.path.join(ROOT, 'yt-upload', 'tr.json')
    meta = json.load(open(mp, encoding='utf-8')); tr = json.load(open(tp, encoding='utf-8'))
    trn = json.load(open(os.path.join(HERE, 'days', f'day{n}_tr.json'), encoding='utf-8'))
    for k in 'fpmdvr':
        old, new = f'{k}{n - 1:02d}', f'{k}{n:02d}'
        (c0, u0), (c1, u1) = names(D, k, n - 1), names(D, k, n)
        x = json.loads(json.dumps(meta[old], ensure_ascii=False))
        for f in ('title', 'desc', 'link'):
            s = x[f].replace(c0, '\0C').replace(u0 or '\0\0', '\0U')
            s = renum(s, n - 1, n).replace('\0C', c1).replace('\0U', u1 or '')
            x[f] = s
        if len(x['title']) > 100: x['title'] = x['title'][:97].rstrip() + '…'
        x.update(id=new, date=date, time=SLOT[k]); meta[new] = x
        t = json.loads(json.dumps(tr[old], ensure_ascii=False))
        for lang in t:
            ti = t[lang]['title']; head = re.match(r'^(.*?/40)', ti).group(1)
            t[lang]['title'] = renum(head, n - 1, n) + ': ' + trn[new][lang]
            t[lang]['desc'] = renum(t[lang]['desc'], n - 1, n)
        tr[new] = t
        print(new, '|', x['title'], '|', t['uk']['title'])
    json.dump(meta, open(mp, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    json.dump(tr, open(tp, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)


if __name__ == '__main__':
    run(int(sys.argv[1]), sys.argv[2])

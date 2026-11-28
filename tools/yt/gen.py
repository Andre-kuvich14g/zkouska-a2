"""Плани денних уроків f/p/m/d/v/r (відновлено 26.11.2026 за опублікованими відео дня 18).

python3 tools/yt/gen.py 19            -> out/<id>/plan.json для f19 p19 m19 d19 v19 r19 + список відсутніх голосів
python3 tools/yt/gen.py 19 f19 v19    -> тільки вибрані
Сцени беруться з tools/yt/scenes/<id>*.png (генерує scenes_dayNN.js).
"""
import json, os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
ROOT = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, os.path.join(ROOT, 'tools', 'learn'))
import voice
from voice import EL_M, EL_F

OUT = os.environ.get('YT_OUT', '/home/claude/yt/out')
SCN = os.path.join(HERE, 'scenes')
FPS = 30
END = ' Odkaz najdete v popisu videa. A odebírejte kanál, každý den je tu nové video.'
NUM = {1: 'jedna', 2: 'dvě', 3: 'tři', 4: 'čtyři', 5: 'pět', 6: 'šest', 7: 'sedm', 8: 'osm', 9: 'devět', 10: 'deset',
       11: 'jedenáct', 12: 'dvanáct', 13: 'třináct', 14: 'čtrnáct', 15: 'patnáct', 16: 'šestnáct', 17: 'sedmnáct',
       18: 'osmnáct', 19: 'devatenáct', 20: 'dvacet'}


def cznum(n):
    if n in NUM: return NUM[n]
    t = {2: 'dvacet', 3: 'třicet', 4: 'čtyřicet'}[n // 10]
    return t + (' ' + NUM[n % 10] if n % 10 else '')


def fr(x): return round(x * FPS) / FPS


FIX = {  # ручні правки тексту для чоловічого голосу / без справжніх імен родини
    'p15': [('jsem byla', 'jsem byl'), ('Chtěla bych', 'Chtěl bych'), ('Marija Koval', 'Andrij Koval')],
    'p20': [('jsem udělala', 'jsem udělal'), ('Chtěla bych', 'Chtěl bych'), ('Julija', 'Andrij')],
}


def masc(s):
    """Чоловічий рід для голосу Daniel: «rád/a» -> «rád», «šel/šla» -> «šel», «nepřišel/nepřišla» -> «nepřišel»."""
    s = s.replace('manžel/ka', 'manželka').replace('Manžel/ka', 'Manželka')  # мовець-чоловік → дружина
    return re.sub(r'([^\W\d]+)/([^\W\d]+)', lambda m: m.group(1), s)


def fem(s):
    """Жіночий рід для екзаменаторки: «šel/šla» -> «šla», «rád/a» -> «ráda»."""
    def r(m):
        a, b = m.group(1), m.group(2)
        return b if len(b) > 2 else a + b
    return re.sub(r'([^\W\d]+)/([^\W\d]+)', r, s)


def spoken(s):
    return re.sub(r'\s+', ' ', s).strip()


def words(s): return len(re.findall(r"[\wÀ-ž]+", s))


def scene(name):
    p = os.path.join(SCN, name + '.png')
    return p if os.path.exists(p) else None


def data():
    import build_learn as b
    from w12 import W1, W2
    U1 = b.U1_A + b.U1_B + b.U1_C + b.U1_D
    return dict(f=W1, p=W2, m=U1, d=b.opt('u2', 'U2'), v=b.opt('u3', 'U3'), r=b.opt('u4', 'U4'))


class Plan:
    def __init__(self, id):
        self.id = id; self.k = id[0]; self.n = int(id[1:]); self.segs = []
        self.side = scene(id); self.sides = {}

    def add(self, slide, text=None, v=EL_M, pad=0.8, dur=None, side=None):
        sl = dict(slide, sec=self.k, n=self.n)
        sd = side if side is not None else self.side
        if sd: sl['side'] = sd
        if text:
            t = spoken(text); path, d = voice.say(v, t)
            self.segs.append(dict(slide=sl, dur=dur or fr(d + pad + 0.2), audio=path, adur=d, sub=t))
        else:
            self.segs.append(dict(slide=sl, dur=dur or 1.0, audio=None, sub=None))

    def wait(self, slide, n, msg, side=None):
        for c in range(n, 0, -1):
            self.add(dict(slide, kind=slide['kind'] + '-wait', c=c, msg=msg, tick=1, ding=int(c == 1)), side=side)

    def dump(self, extra):
        d = f'{OUT}/{self.id}'; os.makedirs(d, exist_ok=True)
        p = dict(id=self.id, n=self.n, segs=self.segs, **extra)
        p['duration'] = round(sum(s['dur'] for s in self.segs), 2)
        json.dump(p, open(f'{d}/plan.json', 'w'), ensure_ascii=False)
        return p


INTRO_TAG = '⏱ Do 2 minut: vzor na plný počet bodů'


def f_lesson(D, n):
    e = D['f'][n - 1]; P = Plan(f'f{n:02d}'); nm = e['cz']
    P.add(dict(kind='x-intro', chip=f'Formulář {n} / 40', title=nm, sub='Psaní · úloha 1 · 3 otázky · celé věty, minimálně 10 slov · 8 bodů', tag=INTRO_TAG, name=nm),
          f"Psaní, úloha jedna. Formulář číslo {n}. {masc(e['situation'])} Odpovězte celou větou, minimálně deset slov.", pad=0.7)
    for k, (q, a) in enumerate(e['qa'], 1):
        a = masc(a); sd = scene(f'{P.id}_q{k}') or P.side
        base = dict(kind='f-q', sit=e['situation'], k=k, q=q, name=nm)
        P.add(base, q, pad=0.5, side=sd)
        P.wait(base, 10, 'Zastavte video a napište odpověď.', side=sd)
        P.add(dict(base, kind='f-a', a=a, wc=words(a)), a, pad=0.9, side=sd)
    nx = D['f'][n]['cz'] if n < 40 else ''
    P.add(dict(kind='x-outro', line=f'Vyplňte formulář {n} na webu Zkouška A2 nanečisto.', sub='Web počítá slova v každé odpovědi · zdarma', nxt=nx, nxtlab=f'Formulář {n + 1}', name=nm),
          f'Vyplňte formulář {n} na webu Zkouška A2 nanečisto.' + END, pad=2.0, side=scene('outro'))
    return P.dump(dict(name=nm))


def p_lesson(D, n):
    e = D['p'][n - 1]; P = Plan(f'p{n:02d}'); subj = e['subject']
    sit = masc(e['situation'])
    pr = [dict(q=masc(x['q']), om=x['om']) for x in e['prompts']]
    P.add(dict(kind='x-intro', chip=f'E-mail {n} / 40', title=subj, sub='Psaní · úloha 2 · minimálně 35 slov · 12 bodů', tag=INTRO_TAG, subj=subj),
          f'Psaní, úloha dvě. E-mail číslo {n}: {subj}.', pad=0.7)
    base = dict(kind='p-task', subj=subj, sit=sit, to=e['to'], pr=pr)
    P.add(base, f'{sit} Napište e-mail, minimálně třicet pět slov. Ke každému obrázku napište jednu větu.', pad=0.7)
    P.wait(base, 8, 'Zastavte video a napište e-mail.')
    mod = e['model']
    for a, b in FIX.get(P.id, []): mod = mod.replace(a, b)
    lines = masc(mod).split('\n')
    greet, close = lines[0], '\n'.join(lines[-2:])
    body = ' '.join(lines[1:-2])
    sents = [s.strip() for s in re.split(r'(?<=[.!?])(?<![0-9]\.)\s+(?=[A-ZÁČĎÉĚÍŇÓŘŠŤÚŮÝŽ])', body) if s.strip()]
    mb = dict(kind='p-model', subj=subj, to=e['to'], greet=greet, sents=sents, close=close, pr=pr)
    P.add(dict(mb, hi=-1), greet, pad=0.1, side='')
    for k, s in enumerate(sents):
        P.add(dict(mb, hi=k), s, pad=0.1, side='')
    wc = words(masc(mod))
    P.add(dict(kind='p-tip', subj=subj, wc=wc), f'Tento e-mail má {wc} slov. Na každý obrázek je jedna věta. Nezapomeňte na pozdrav na začátku a na konci.', pad=0.9)
    nx = D['p'][n]['subject'] if n < 40 else ''
    P.add(dict(kind='x-outro', line='Napište svůj e-mail na webu', sub='web počítá slova a kontroluje e-mail · zdarma', nxt=nx, nxtlab=f'E-mail {n + 1}', subj=subj),
          'Napište svůj e-mail na webu Zkouška A2 nanečisto, odkaz najdete v popisu videa. A odebírejte kanál, každý den je tu nové video.', pad=2.0, side=scene('outro'))
    return P.dump(dict(subj=subj))


def m_lesson(D, n):
    cz, tr, qa = D['m'][n - 1]; P = Plan(f'm{n:02d}')
    P.add(dict(kind='x-intro', chip=f'Téma {n} / 40', title=cz, sub='10 otázek · poslouchejte a odpovězte nahlas', tr=' · '.join(tr), tag=INTRO_TAG, cz=cz),
          f'Mluvení, úloha jedna. Téma {n}: {cz}. Deset otázek. Poslouchejte otázku a odpovězte nahlas.', pad=0.7)
    for k, (q, a) in enumerate(qa, 1):
        q, a = masc(q), masc(a); sd = scene(f'{P.id}_q{k}') or P.side
        base = dict(kind='m-q', k=k, q=q, cz=cz)
        P.add(base, q, pad=0.5, side=sd)
        P.wait(dict(base, kind='m'), 5, 'Teď vy! Odpovězte nahlas.', side=sd)
        P.add(dict(base, kind='m-a', a=a), a, pad=0.7, side=sd)
    nx = D['m'][n][0] if n < 40 else ''
    P.add(dict(kind='x-outro', line=f'Procvičte si téma {n} na webu', sub='web poslouchá a kontroluje vaši odpověď · zdarma', nxt=nx, nxtlab=f'Téma {n + 1}', cz=cz),
          f'Výborně! Procvičte si téma {n} na webu Zkouška A2 nanečisto, odkaz najdete v popisu videa. A odebírejte kanál, každý den je tu nové video.', pad=2.0, side=scene('outro'))
    return P.dump(dict(cz=cz, uk=tr[0], en=tr[1], ru=tr[2], vi=tr[3]))


def d_lesson(D, n):
    e = D['d'][n - 1]; P = Plan(f'd{n:02d}'); nm = e['cz']
    sit, goal = e['situation'], e['goal']; cues = [c for c, _ in e['pairs']]
    P.add(dict(kind='x-intro', chip=f'Karta {n} / 40', title=nm, sub='Mluvení · úloha 2 · položte 4 otázky · 3 podle nápovědy + 1 vlastní', tag=INTRO_TAG, name=nm),
          f'Mluvení, úloha dvě. Karta číslo {n}. {sit} {goal} Položte čtyři otázky.', pad=0.7)
    P.add(dict(kind='d-card', sit=sit, goal=goal, cues=cues, name=nm), f'{sit} {goal}', pad=0.7)
    dl = e['dialog']; lines = []
    # 1. привітання екзаменаторки
    lines.append(['T', fem(dl[0][1])]); P.add(dict(kind='d-chat', sit=sit, goal=goal, cues=cues, k=0, lines=list(lines), name=nm), fem(dl[0][1]), v=EL_F, pad=0.5)
    i = 1; k = 0
    while i < len(dl):
        r, t = dl[i]
        if r == 'U' and k < 4:
            k += 1
            P.wait(dict(kind='d-cue', sit=sit, goal=goal, cues=cues, k=k, lines=[], name=nm), 5, 'Teď vy! Zeptejte se.')
            lines = [['U', masc(t)]]
            P.add(dict(kind='d-chat', sit=sit, goal=goal, cues=cues, k=k, lines=list(lines), name=nm), masc(t), pad=0.4)
        else:
            t2 = fem(t) if r == 'T' else masc(t); lines.append([r, t2]); lines = lines[-3:]
            P.add(dict(kind='d-chat', sit=sit, goal=goal, cues=cues, k=k, lines=list(lines), name=nm), t2, v=EL_F if r == 'T' else EL_M, pad=0.5)
        i += 1
    nx = D['d'][n]['cz'] if n < 40 else ''
    P.add(dict(kind='x-outro', line=f'Procvičte si kartu {n} na webu Zkouška A2 nanečisto.', sub='Web poslouchá vaše otázky · zdarma', nxt=nx, nxtlab=f'Karta {n + 1}', name=nm),
          f'Procvičte si kartu {n} na webu Zkouška A2 nanečisto.' + END, pad=2.0, side=scene('outro'))
    return P.dump(dict(name=nm))


def v_lesson(D, n):
    e = D['v'][n - 1]; P = Plan(f'v{n:02d}'); nm = e['title']
    pics = [dict(t=re.sub(r'^[^A-Za-zÀ-ž]+', '', x).strip(), om=(e.get('om') or [[None]] * 4)[i][0]) for i, x in enumerate(e['pictures'])]
    scn = [scene(f'{P.id}_{j}') for j in range(1, 5)]
    scn = scn if all(scn) else None
    P.add(dict(kind='x-intro', chip=f'Příběh {n} / 40', title=nm, sub='Mluvení · úloha 3 · vyprávění podle 4 obrázků · v minulém čase · 10 bodů', tag=INTRO_TAG, name=nm),
          f"Mluvení, úloha tři. Příběh číslo {n}: {nm}. {e['q']} Vyprávějte podle obrázků v minulém čase.", pad=0.7)
    base = dict(kind='v-pics', q=e['q'], pics=pics, scn=scn, name=nm)
    P.add(base, e['q'], pad=0.5, side='')
    P.wait(base, 20, 'Teď vy! Vyprávějte v minulém čase.', side='')
    sents = [s.strip() for s in re.split(r'(?<=[.!?])(?<![0-9]\.)\s+(?=[A-ZÁČĎÉĚÍŇÓŘŠŤÚŮÝŽ])', masc(e['model'])) if s.strip()]
    mp = [min(3, i * 4 // len(sents)) for i in range(len(sents))]
    for k, s in enumerate(sents):
        P.add(dict(kind='v-model', q=e['q'], pics=pics, scn=scn, sents=sents, hi=k, map=mp, name=nm), s, pad=0.0, side='')
    nx = D['v'][n]['title'] if n < 40 else ''
    P.add(dict(kind='x-outro', line=f'Vyprávějte příběh {n} na webu Zkouška A2 nanečisto.', sub='Web poslouchá a kontroluje minulý čas · zdarma', nxt=nx, nxtlab=f'Příběh {n + 1}', name=nm),
          f'Vyprávějte příběh {n} na webu Zkouška A2 nanečisto.' + END, pad=2.0, side=scene('outro'))
    return P.dump(dict(name=nm, uk=e['t'][0]))


def r_lesson(D, n):
    e = D['r'][n - 1]; P = Plan(f'r{n:02d}'); nm = e['cz']
    opts = [dict(t=o['label'], om=o['om'][0], scn=scene(f'{P.id}_o{i + 1}')) for i, o in enumerate(e['options'])]
    P.add(dict(kind='x-intro', chip=f'Situace {n} / 40', title=nm, sub='Mluvení · úloha 4 · vyberte 1 ze 3 možností a řekněte proč · 7 bodů', tag=INTRO_TAG, name=nm),
          f'Mluvení, úloha čtyři. Situace číslo {n}. Zkoušející vám řekne situaci. Domluvte se s ní, vyberte jednu možnost a řekněte proč.', pad=0.7)
    dl = e['dialog']; t0 = fem(dl[0][1])
    base = dict(kind='r-task', sit=e['situation'], opts=opts, name=nm)
    P.add(base, t0, v=EL_F, pad=0.5, side='')
    P.wait(base, 8, 'Teď vy! Co navrhnete?', side='')
    lines = [['T', t0]]
    for r, t in dl[1:]:
        t2 = fem(t) if r == 'T' else masc(t); lines.append([r, t2])
        P.add(dict(kind='r-dialog', lines=list(lines[-5:]), name=nm), t2, v=EL_F if r == 'T' else EL_M, pad=0.3)
    nx = D['r'][n]['cz'] if n < 40 else ''
    P.add(dict(kind='x-outro', line=f'Procvičte si situaci {n} na webu Zkouška A2 nanečisto.', sub='Web hraje roli zkoušející · zdarma', nxt=nx, nxtlab=f'Situace {n + 1}', name=nm),
          f'Procvičte si situaci {n} na webu Zkouška A2 nanečisto.' + END, pad=2.0, side=scene('outro'))
    return P.dump(dict(name=nm))


FN = dict(f=f_lesson, p=p_lesson, m=m_lesson, d=d_lesson, v=v_lesson, r=r_lesson)

if __name__ == '__main__':
    day = int(sys.argv[1]); only = sys.argv[2:] or [f'{k}{day:02d}' for k in 'fpmdvr']
    D = data(); res = []
    for id in only:
        p = FN[id[0]](D, int(id[1:])); res.append((id, p['duration'], len(p['segs'])))
    n, ch = voice.save_missing(os.path.join(ROOT, 'tools', 'el', f'miss_d{day:02d}.json'))
    print(res); print('відсутні голоси:', n, 'фраз,', ch, 'символів')

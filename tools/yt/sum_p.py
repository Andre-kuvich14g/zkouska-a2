"""Psaní 1+2 – Sbírka C (5 formulářů + 5 e-mailů): python3 tools/yt/sum_p.py 3 -> $YT_OUT/sb_p3/plan.json
Відновлено 28.11.2026 за структурою опублікованих sb_p1/sb_p2: титул (6 с) → формуляри A–B (уроки f без аутро, окрім першого)
→ e-maily A–B (уроки p без аутро, окрім останнього). Голоси — з кешу / опублікованих уроків (YT_REUSE=1)."""
import sys, os, json
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
os.environ.setdefault('YT_REUSE', '1')
import gen

C = int(sys.argv[1]) if len(sys.argv) > 1 else 1
T0 = (C - 1) * 5; A, B = T0 + 1, T0 + 5
KEY = f'sb_p{C}'; OUT = f'{gen.OUT}/{KEY}'; os.makedirs(OUT, exist_ok=True)
D = gen.data()
FR = dict(sb=C, sbu='Psaní 1 + 2', sbr='formuláře a e-maily')
segs = []; chapters = []
def chap(t): chapters.append((round(sum(s['dur'] for s in segs), 2), t))

FN = [D['f'][n - 1]['cz'] for n in range(A, B + 1)]
PN = [D['p'][n - 1]['subject'] for n in range(A, B + 1)]
chap('Úvod')
segs.append(dict(slide=dict(kind='sb-intro2', sec='f', chip=f'SBÍRKA {C} · ÚLOHY {A}–{B}', title='Psaní 1 + 2:<br>5 formulářů + 5 e-mailů',
                            topics=FN[:3] + PN[:2], agenda=['5 formulářů (8 bodů)', '5 e-mailů (12 bodů)', 'Čas na vaši odpověď', 'Vzor na plný počet bodů'],
                            hook='✍️ Zastavte video a pište s námi', **FR), dur=6.0, audio=None, sub=None))
for kind, names, fn in (('f', FN, gen.FN['f']), ('p', PN, gen.FN['p'])):
    for i, n in enumerate(range(A, B + 1)):
        chap(f"{'Formulář' if kind == 'f' else 'E-mail'} {n}: {names[i]}")
        keep_outro = (kind == 'f' and i == 0) or (kind == 'p' and i == 4)
        for s in fn(D, n)['segs']:
            k = s['slide']['kind']
            if k == 'x-intro' and s['slide'].get('n') is None: pass
            if k == 'x-outro' and not keep_outro: continue
            sl = dict(s['slide'], **FR); segs.append(dict(s, slide=sl))
T = sum(s['dur'] for s in segs)
json.dump(dict(id=KEY, segs=segs, chapters=chapters, duration=round(T, 1)), open(f'{OUT}/plan.json', 'w'), ensure_ascii=False)
print(KEY, f'{int(T // 60)}:{int(T % 60):02d}', [c[1] for c in chapters][:3], 'missing', len(gen.voice.MISSING) if hasattr(gen, 'voice') else '?')

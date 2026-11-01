# Збирає сторінку «Вчимо Mluvení»: python3 tools/learn/build_learn.py  ->  learn/index.html
import json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
ROOT = os.path.dirname(os.path.dirname(HERE))
from ui import UI
from theory import THEORY
import theory_en, theory_ru, theory_vi  # noqa: F401 (доповнюють THEORY)
from u1_a import U1_A; from u1_b import U1_B; from u1_c import U1_C; from u1_d import U1_D

def opt(mod, name):
    try: return getattr(__import__(mod), name)
    except Exception: return []

VIDEOS = {
 'home': [('NmmVbgWpIfo', 'Zkouška pro trvalý pobyt A2: Co se mění v dubnu 2026?'), ('dZe4_xv6QkM', 'Zkouška pro trvalý pobyt A2: Mluvení – jak vypadá a jak se připravit')],
 'u1': [('a8i-TWtrAwE', 'Mluvení – umíte odpovědět na otázky?'), ('VJ_1cz6DowY', 'Czech Language Exam A2: Common Questions and Answers from the Examiner'), ('3P7Bb-JSggo', 'Zkouška pro trvalý pobyt A2: Moje rodina (mluvení)')],
 'u2': [('8h3rjTZHzr8', 'Mluvení, úloha 2 – další příklady'), ('ojyeYcwEgM4', 'Czech A2 exam – speaking (roleplays)'), ('yEhP3U98glw', 'Czech A2 Exam Speaking 2026 – BIG Overview with Examples')],
 'u3': [('2ZiLJaTHIQ8', 'Learn Czech Past Tense for the A2 Exam'), ('wM-i8G-a_aE', 'Mluvení – úlohy 3 a 4'), ('kgWPlOsxKNs', 'Nová zkouška z češtiny A2 2026: Jak zvládnout mluvení bez stresu')],
 'u4': [('evQzRMJIfYA', 'Mluvení, nová úloha 4 – další cvičení'), ('m558l91RI54', 'Mluvení, nová úloha 4 – cvičení')],
}

def topics(rows): return [{'cz': cz, 't': tr, 'qa': [list(x) for x in qa]} for cz, tr, qa in rows]

def build():
    data = {
        'ui': UI, 'theory': THEORY, 'videos': {k: [list(v) for v in vs] for k, vs in VIDEOS.items()},
        'u1': topics(U1_A + U1_B + U1_C + U1_D),
        'u2': opt('u2', 'U2'), 'u3': [dict(x, cz=x['title']) for x in opt('u3', 'U3')], 'u4': opt('u4', 'U4'),
    }
    blob = json.dumps(data, ensure_ascii=False, separators=(',', ':')).replace('</', '<\\/')
    tpl = open(os.path.join(HERE, 'template.html'), encoding='utf-8').read()
    os.makedirs(os.path.join(ROOT, 'learn'), exist_ok=True)
    open(os.path.join(ROOT, 'learn', 'index.html'), 'w', encoding='utf-8').write(tpl.replace('@@DATA@@', blob))
    print('OK learn/index.html', len(blob) // 1024, 'KB data;', {k: len(data[k]) for k in ('u1', 'u2', 'u3', 'u4')})

if __name__ == '__main__': build()

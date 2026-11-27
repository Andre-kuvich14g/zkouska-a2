"""Díl 0 · Cesta ke zkoušce (27.11.2026): аудіо з першого відео g01 (чеська озвучка) + нові зв'язки ведучого.
python3 tools/yt/prod_d0.py -> $YT_OUT/prod_d0/plan.json (+ tools/el/miss_prod_d0.json)"""
import json, os, re, subprocess, sys
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import gen, voice
from gen import fr
from voice import EL_M
ROOT = gen.ROOT; OUT = f'{gen.OUT}/prod_d0'; CUT = f'{OUT}/cut'; os.makedirs(CUT, exist_ok=True)

def secs(t): h, m, s = t.strip().replace(',', '.').split(':'); return int(h) * 3600 + int(m) * 60 + float(s)
B = []
for b in re.split(r'\n\s*\n', open(f'{ROOT}/yt-upload/g01.cs.srt', encoding='utf-8').read().strip()):
    l = b.split('\n'); a, z = l[1].split('-->'); B.append(dict(n=int(l[0]), a=secs(a), z=secs(z), t=' '.join(l[2:])))

N = {  # заміни: номер блоку -> новий текст (None = вирізати)
    16: 'Tohle je nultý díl kurzu Zkouška A2 do sluchátek. Poslouchejte v klidu – a potom začněte s lekcemi.',
    17: None, 18: None, 19: None, 21: None,
    47: 'Takže udělejte tři věci.',
    86: 'Kde trénovat? Máte k tomu tento kurz do sluchátek: šest částí – Mluvení jedna až čtyři a Psaní jedna a dvě. Každá část má osm bloků po pěti tématech a po každém bloku dvanáct důležitých frází. Poslouchejte jeden blok denně – v tramvaji, v práci, při vaření. A cvičné zkoušky s časomírou najdete zdarma na webu Zkouška A2 nanečisto.',
    **{k: None for k in range(87, 101)}, 85: None,
    109: 'Úkol na dnes: udělejte jednu cvičnou zkoušku na webu a zapište si body. Za šest týdnů to zkuste znovu.',
    110: None, 111: None, 112: None,
    126: 'Ano, to je ta jedna minuta ze začátku.',
    233: 'V tomto kurzu je čtyřicet formulářů a čtyřicet e-mailů se vzory – to jsou části Psaní jedna a Psaní dvě.',
    255: None, 257: None, 258: None,
    312: 'V tomto kurzu má každá ze čtyř úloh vlastní část – čtyřicet témat s pauzou na vaši odpověď a se vzory.',
    313: None,
    355: 'Pamatujete si člověka ze začátku, který přišel o minutu pozdě?',
    358: 'Teď tři kroky, které můžete udělat hned. První – udělejte na webu Zkouška A2 nanečisto první cvičnou zkoušku. Druhý – zapište si do kalendáře datum registrace, platby a zkoušky. Třetí – pusťte si první část kurzu: Mluvení jedna, blok jedna.',
    **{k: None for k in range(359, 367)},
}
CH = {1: 'Úvod', 22: '1. Registrace', 51: '2. Platba', 75: '3. Příprava', 114: '4. Den zkoušky', 166: '5. Čtení',
      194: '6. Psaní', 236: '7. Poslech', 259: '8. Ústní část', 316: '9. Deset chyb', 345: '10. Výsledek a osvědčení', 355: 'Závěr'}
UK = {'Úvod': 'Вступ', '1. Registrace': 'Реєстрація', '2. Platba': 'Оплата', '3. Příprava': 'Підготовка', '4. Den zkoušky': 'День іспиту',
      '5. Čtení': 'Читання', '6. Psaní': 'Письмо', '7. Poslech': 'Аудіювання', '8. Ústní část': 'Усна частина', '9. Deset chyb': '10 помилок',
      '10. Výsledek a osvědčení': 'Результат і сертифікат', 'Závěr': 'Підсумок'}
PROD = '🎧 Zkouška A2 do sluchátek · <b>Díl 0 · Cesta ke zkoušce</b>'
segs = []; chapters = []; cur = 'Úvod'; mp4 = f'{ROOT}/yt-upload/g01.mp4'
for i, b in enumerate(B):
    if b['n'] in CH:
        cur = CH[b['n']]; chapters.append((round(sum(s['dur'] for s in segs), 2), cur))
        if b['n'] > 1:
            segs.append(dict(slide=dict(kind='pr-item', sec='m', prod=PROD, chip='DÍL 0 · CESTA KE ZKOUŠCE', t=cur, uk=UK[cur]), dur=1.6, audio=None, sub=None))
    sl = dict(kind='pr-txt', sec='m', prod=PROD, chip=cur.upper())
    if b['n'] in N:
        t = N[b['n']]
        if t is None: continue
        p, d = voice.say(EL_M, t)
        segs.append(dict(slide=dict(sl, t=t), dur=fr(d + 0.6), audio=p, adur=d, sub=t)); continue
    nxt = B[i + 1]['a'] if i + 1 < len(B) else b['z'] + 0.5
    z = min(b['z'] + 0.3, nxt); f = f"{CUT}/b{b['n']:03d}.wav"
    if not os.path.exists(f):
        subprocess.run(['ffmpeg', '-v', 'error', '-y', '-ss', f"{b['a']:.3f}", '-t', f"{z - b['a']:.3f}", '-i', mp4, '-vn', '-ac', '1', '-ar', '44100', f], check=True)
    d = z - b['a']
    segs.append(dict(slide=dict(sl, t=b['t']), dur=fr(d + 0.25), audio=f, adur=d, sub=b['t']))
T = sum(s['dur'] for s in segs)
json.dump(dict(id='prod_d0', segs=segs, chapters=chapters, duration=round(T, 1)), open(f'{OUT}/plan.json', 'w'), ensure_ascii=False)
voice.save_missing(f'{ROOT}/tools/el/miss_prod_d0.json')
print('d0', f'{int(T // 60)}:{int(T % 60):02d}', 'missing', len(voice.MISSING), sum(len(m['t']) for m in voice.MISSING))

"""Велике повторення Mluvení 4 (situace): python3 tools/yt/sum_m4.py 3 -> $YT_OUT/om4_3/plan.json
Відновлено 27.11.2026: голоси уроків і повторювані фрази — з опублікованих відео (YT_REUSE=1); сцени rNN.png — tools/yt/scenes."""
import sys, os, json, wave
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
os.environ.setdefault('YT_REUSE', '1')
import gen, voice
from gen import fr, spoken
from voice import EL_M, EL_F
def el_say(v, t, path=None): return voice.say(v, t)

C = int(sys.argv[1]) if len(sys.argv) > 1 else 1
T0 = (C - 1) * 5; A, B = T0 + 1, T0 + 5
KEY = f'om4_{C}'
OUT = f"{gen.OUT}/{KEY}"; os.makedirs(OUT, exist_ok=True)
SC = gen.SCN + '/'
TR = json.load(open(gen.ROOT + '/yt-upload/tr.json'))
_D = gen.data(); LP = [gen.r_lesson(_D, T0 + i + 1) for i in range(5)]
NAMES = [p['segs'][0]['slide']['name'] for p in LP]
UKN = [TR[f'r{T0 + i + 1:02d}']['uk']['title'].split(': ', 1)[1] for i in range(5)]
MAPS = {1: [0, 0, 0, 1, 1, 1, 2, 2, 3, 3, 3], 2: [0, 0, 0, 1, 1, 2, 2, 3, 3, 3], 3: [0, 0, 1, 1, 1, 2, 2, 3, 3, 3],
        4: [0, 0, 1, 1, 2, 3, 3, 3], 5: [0, 0, 0, 0, 1, 1, 1, 2, 2, 2, 3, 3]}
FR = dict(sb=C, sbu='Mluvení 4', sbr='situace')
sc = lambda n: f'{SC}r{n:02d}.png'

segs = []; chapters = []
def dur_of(p): return voice.dur(p)
def add(slide, text=None, voice=EL_M, name=None, pad=0.8, audio=None, dur=None, side=None):
    if audio: d, path = dur_of(audio), audio
    elif text: path, d = el_say(voice, spoken(text))
    else: d, path = 0, None
    sl = dict(slide, sec='r', **FR)
    if side: sl['side'] = side
    segs.append(dict(slide=sl, dur=dur or fr(d + pad + 0.2), audio=path, adur=d, sub=spoken(text) if text else None))
def wait(slide, n, msg, side=None):
    for c in range(n, 0, -1):
        sl = dict(slide, kind=slide['kind'] + ('-w' if slide['kind'] == 'sb-ph' else '-wait'), c=c, msg=msg, sec='r', **FR)
        if side: sl['side'] = side
        segs.append(dict(slide=sl, dur=1.0, audio=None, sub=None))
def chap(t): chapters.append((sum(s['dur'] for s in segs), t))

# 1. Вступ
chap('Úvod')
add(dict(kind='sb-intro2', chip=f'VELKÉ OPAKOVÁNÍ {C} · SITUACE {A}–{B}', title='Mluvení 4:<br>všech 5 situací', topics=NAMES,
         agenda=['Jak to funguje', '5 situací s dialogem', '12 frází pro dohodu', '5 chyb', 'Shrnutí'], hook='⏱ 5 dialogů na plný počet bodů'),
    f'Všech pět situací z lekcí {gen.cznum(A)} až {gen.cznum(B)} – vždy tři možnosti a celý vzorový dialog se zkoušející. A navíc dvanáct frází, se kterými se domluvíte v každé situaci, a pět chyb, kvůli kterým lidé ztrácejí body. Připravte se a mluvte nahlas!',
    name='n_intro', pad=1.2, side=sc(T0 + 3))

# 2. Як працює
chap('Jak úloha funguje')
add(dict(kind='sb-stats', t='Jak úloha 4 funguje', stats=[['3', 'možnosti'], ['1', 'dialog'], ['7', 'bodů']],
         uk='Екзаменаторка описує ситуацію і 3 варіанти. Ви пропонуєте, вона заперечує — ви пропонуєте інше. Наприкінці пояснюєте «чому». Разом 7 балів.'),
    'Jak úloha čtyři funguje? Zkoušející vám řekne situaci a ukáže tři možnosti. Vy navrhnete jednu. Ona většinou řekne, že se jí to nelíbí – a vy navrhnete jinou. Nakonec se dohodnete a řeknete proč. Za tuto úlohu můžete dostat sedm bodů.', name='n_how1', pad=1.2, side=sc(T0 + 3))
add(dict(kind='sb-list', t='Dialog krok za krokem',
         items=['1️⃣ <b>Navrhněte:</b> Můžeme jít do kina.', '2️⃣ Ona: <i>To se mi nechce.</i>', '3️⃣ <b>Jiný návrh:</b> Tak půjdeme do divadla.', '4️⃣ <b>Proč?</b> Protože …'],
         uk='Пропозиція → заперечення → нова пропозиція → «чому?» → «тому що…»'),
    'Dialog má jednoduchý plán. Navrhnete jednu možnost. Zkoušející řekne, proč ne. Vy klidně navrhnete jinou možnost. A když se zeptá proč, odpovíte: protože. Teď si projdeme všech pět situací. Nejdřív mluvte sami, pak uslyšíte vzor.',
    name='n_how2', pad=1.2, side=sc(T0 + 5))

# 3. Усі 5 ситуацій
SECS = 12
for i in range(5):
    n = T0 + i + 1; les = LP[i]
    chap(f'Situace {n}: {NAMES[i]}')
    add(dict(kind='sb-topic', chip='SITUACE', i=i + 1, top=NAMES[i], uk=UKN[i], subt='3 možnosti · navrhněte, reagujte, řekněte proč · pak vzor'),
        f'Situace {gen.cznum(n)}: {NAMES[i]}.', name=f'n_s{n}', pad=0.6, side=sc(n))
    waited = False
    for s in les['segs']:
        k = s['slide']['kind']
        if k in ('x-intro', 'x-outro'): continue
        sl = {kk: v for kk, v in s['slide'].items() if kk != 'sec'}
        if k == 'r-dialog': sl['side'] = sc(n)
        if k.endswith('-wait'):
            if not waited:
                waited = True; wait(dict(sl, kind=k[:-5]), SECS, 'Teď vy! Navrhněte jednu možnost.')
            continue
        add(sl, s['sub'], audio=s['audio'], dur=s['dur']) if s['audio'] else add(sl, s['sub'], pad=0.3)

# 4. 12 фраз
PH = [('Můžeme …', 'Můžeme jít do kina.', 'Можемо …'),
      ('Co kdybychom …?', 'Co kdybychom jeli na hory?', 'А що, якби ми …?'),
      ('A co třeba …?', 'A co třeba pizza?', 'А як щодо …?'),
      ('Tak …', 'Tak půjdeme do restaurace.', 'Тоді …'),
      ('Dobře, tak …', 'Dobře, tak uvaříme guláš.', 'Добре, тоді …'),
      ('Máš pravdu.', 'Máš pravdu, divadlo je drahé.', 'Ти маєш рацію.'),
      ('To je škoda.', 'To je škoda, ale nevadí.', 'Шкода.'),
      ('Já bych radši …', 'Já bych radši jel k moři.', 'Я б краще …'),
      ('Protože …', 'Protože plavání je zdravé.', 'Тому що …'),
      ('… je levné / blízko', 'Kino je levné a je blízko.', '… дешево / близько'),
      ('Souhlasím.', 'Souhlasím, to je dobrý nápad.', 'Погоджуюсь.'),
      ('Bude to …', 'Bude to legrace.', 'Це буде …')]
PHS = [sc(T0 + x) for x in [2, 3, 4, 2, 4, 3, 1, 3, 5, 2, 5, 1]]
chap('12 frází pro dohodu')
add(dict(kind='sb-sec', t='12 frází pro dohodu', uk='12 фраз, щоб пропонувати, погоджуватись і пояснювати — слухайте й повторюйте', ic='🗣️'),
    'Teď dvanáct frází, se kterými se domluvíte v každé situaci. Poslouchejte a opakujte nahlas.', name='n_ph', pad=1.0, side=sc(T0 + 3))
for j, (tp, ex, uk) in enumerate(PH):
    base = dict(kind='sb-ph', i=j + 1, n=len(PH), tp=tp, ex=ex, uk=uk)
    add(base, ex, name=f'ph{j}', pad=0.5, side=PHS[j])
    wait(base, 3, 'Opakujte!', side=PHS[j])

# 5. Помилки
ER = [('Jen jedno slovo', 'Kino.', 'Co kdybychom šli do kina?', 'Navrhujte celou větou: Můžeme…, Co kdybychom…', 'Пропонуйте цілим реченням, не одним словом.', sc(T0 + 2)),
      ('Zkoušející řekne ne', 'Ale já chci do kina!', 'Dobře, tak půjdeme do divadla.', 'Když zkoušející nesouhlasí, navrhněte jinou možnost.', 'Якщо екзаменаторка проти — запропонуйте інший варіант, не сперечайтесь.', sc(T0 + 4)),
      ('A proč?', 'Protože ano.', 'Protože plavání je zdravé a bazén je blízko.', 'Na konci řekněte konkrétní důvod: protože…', 'Наприкінці — конкретна причина: protože…', sc(T0 + 5)),
      ('Kamarádka – ty', 'Chcete jet na hory?', 'Chceš jet na hory?', 'V úloze 4 mluvíte s kamarádkou: tykejte – máš, chceš, můžeš.', 'В úloze 4 говорите з подругою на «ти»: máš, chceš.', sc(T0 + 3)),
      ('do + 2. pád', 'Půjdeme do kino.', 'Půjdeme do kina.', 'Po do je 2. pád: do kina, do divadla, do restaurace.', 'Після do — родовий відмінок: do kina, do divadla.', sc(T0 + 2))]
chap('5 typických chyb')
add(dict(kind='sb-sec', t='5 typických chyb', uk='5 типових помилок, через які втрачають бали', ic='⚠️'),
    'Pět typických chyb, kvůli kterým lidé ztrácejí body.', name='n_er', pad=1.0, side=sc(T0 + 3))
for j, (q, bad, good, rule, uk, sd) in enumerate(ER):
    base = dict(kind='sb-er', i=j + 1, q=q, bad=bad, good=good, rule=rule, uk=uk, ok=False)
    add(base, None, dur=2.5, side=sd)
    add(dict(base, ok=True), f'Správně: {good} {rule}', name=f'er{j}', pad=1.5, side=sd)

# 6. Висновок
chap('Shrnutí: 4 pravidla na plný počet bodů')
add(dict(kind='sb-list', fs=70, t='Shrnutí: 4 pravidla na plný počet bodů',
         items=['1️⃣ <b>Celá věta:</b> Můžeme… / Co kdybychom…', '2️⃣ <b>Ne? Jiný návrh:</b> Tak…', '3️⃣ <b>Důvod:</b> protože…', '4️⃣ <b>Tykání:</b> máš, chceš'],
         uk='Ціле речення · нова пропозиція після «ні» · причина з protože · на «ти»'),
    'Shrnutí. Za prvé: navrhujte celou větou. Za druhé: když zkoušející nesouhlasí, navrhněte jinou možnost. Za třetí: na konci řekněte důvod – protože. A za čtvrté: s kamarádkou si tykáte.', name='n_sum', pad=1.5, side=sc(T0 + 5))
add(dict(kind='sb-cta', t='Kterou možnost byste vybrali vy?', uk='Яка ситуація для вас найважча? Напишіть у коментарях, що б ви запропонували, — і підпишіться на канал 🔔', sub='Napište do komentáře · odebírejte kanál – každý den nové video'),
    'A co vy? Která situace z dnešního videa je pro vás nejtěžší? Napište do komentáře celou větou, co byste navrhli, a řekněte proč. A jestli vám video pomáhá, odebírejte kanál – každý den je tu nové video.', name='n_cta', pad=1.5, side=sc(T0 + 3))

# 7. Фінал
chap('Co dál')
add(dict(kind='sb-outro', t='Všech 40 situací na webu', next='Zítra: Psaní 1 a 2 – velké opakování'),
    'Na webu Zkouška A2 nanečisto si můžete všechny situace procvičit zdarma – web hraje roli zkoušející. Odkaz je v popisu. Zítra: velké opakování Psaní, formulář i e-mail. Odebírejte kanál, ať vám nic neuteče.', name='n_out', pad=2.5, side=SC + 'outro.png')

# прогрес-смуга з розділами
T = sum(s['dur'] for s in segs); ch = [c[0] for c in chapters] + [T]; t = 0
bw = [(ch[i + 1] - ch[i]) / T for i in range(len(ch) - 1)]
for s in segs:
    c = max(i for i in range(len(ch) - 1) if ch[i] <= t + 0.01)
    s['slide']['prog'] = dict(b=bw, c=c, f=round(min(1, (t + s['dur'] - ch[c]) / (ch[c + 1] - ch[c])), 3)); t += s['dur']

json.dump(dict(id=KEY, segs=segs, chapters=chapters, n=C), open(f'{OUT}/plan.json', 'w'), ensure_ascii=False)
voice.save_missing(gen.ROOT + f'/tools/el/miss_{KEY}.json')
tot = sum(s['dur'] for s in segs)
print(KEY, 'segs', len(segs), 'dur', round(tot), 'missing', voice.MISSING)
for t, c in chapters: print(f'{int(t // 60)}:{int(t % 60):02d} {c}')

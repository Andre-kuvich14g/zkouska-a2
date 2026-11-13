"""Велике повторення Mluvení 3 (příběhy) з уроків v01..v05, з мультяшними сценами. YT_EL=1 python3 sum_m3.py 1"""
import sys, os, json, wave
sys.path.insert(0, '/home/claude/yt')
os.environ.setdefault('YT_EL', '1')
import gen
from gen import el_say, fr, spoken, EL_M, EL_F, EL_MISSING

C = int(sys.argv[1]) if len(sys.argv) > 1 else 1
T0 = (C - 1) * 5; A, B = T0 + 1, T0 + 5
KEY = f'om3_{C}'
OUT = f'/home/claude/yt/out_pilot/{KEY}'; os.makedirs(OUT, exist_ok=True)
LES = '/home/claude/yt/out_el'
SC = '/home/claude/yt/ab2/om3/'; D7 = '/home/claude/yt/ab2/day7/'
TR = json.load(open('/home/claude/zkouska-a2/yt-upload/tr.json'))
LP = [json.load(open(f'{LES}/v{T0 + i + 1:02d}/plan.json')) for i in range(5)]
NAMES = [p['segs'][0]['slide']['name'] for p in LP]
UKN = [TR[f'v{T0 + i + 1:02d}']['uk']['title'].split(': ', 1)[1] for i in range(5)]
MAPS = {1: [0, 0, 0, 1, 1, 1, 2, 2, 3, 3, 3], 2: [0, 0, 0, 1, 1, 2, 2, 3, 3, 3], 3: [0, 0, 1, 1, 1, 2, 2, 3, 3, 3],
        4: [0, 0, 1, 1, 2, 3, 3, 3], 5: [0, 0, 0, 0, 1, 1, 1, 2, 2, 2, 3, 3]}
FR = dict(sb=C, sbu='Mluvení 3', sbr='příběhy')
scn = lambda n: [f'{SC}v{n:02d}_{j}.png' for j in range(1, 5)]

segs = []; chapters = []
def dur_of(p):
    w = wave.open(p); d = w.getnframes() / w.getframerate(); w.close(); return d
def add(slide, text=None, voice=EL_M, name=None, pad=0.8, audio=None, dur=None, side=None):
    if audio: d, path = dur_of(audio), audio
    elif text: path = f'{OUT}/{name}.wav'; d = el_say(voice, spoken(text), path)
    else: d, path = 0, None
    sl = dict(slide, sec='v', **FR)
    if side: sl['side'] = side
    segs.append(dict(slide=sl, dur=dur or fr(d + pad), audio=path, sub=text))
def wait(slide, n, msg, side=None):
    for c in range(n, 0, -1):
        sl = dict(slide, kind=slide['kind'] + ('-w' if slide['kind'] == 'sb-ph' else '-wait'), c=c, msg=msg, sec='v', **FR)
        if side: sl['side'] = side
        segs.append(dict(slide=sl, dur=1.0, audio=None, sub=None))
def chap(t): chapters.append((sum(s['dur'] for s in segs), t))

# 1. Вступ
chap('Úvod')
add(dict(kind='sb-intro2', chip=f'VELKÉ OPAKOVÁNÍ {C} · PŘÍBĚHY {A}–{B}', title='Mluvení 3:<br>všech 5 příběhů', topics=NAMES,
         agenda=['Jak to funguje', '5 příběhů × 4 obrázky', '12 frází pro vyprávění', '5 chyb', 'Shrnutí']),
    f'Všech pět příběhů z lekcí {gen.cznum(A)} až {gen.cznum(B)} – vždy čtyři obrázky a celé vzorové vyprávění v minulém čase. A navíc dvanáct frází, se kterými zvládnete každý příběh, a pět chyb, kvůli kterým lidé ztrácejí body. Připravte se a vyprávějte nahlas!',
    name='n_intro', pad=1.2, side=SC + 'om3_t.png')

# 2. Як працює
chap('Jak úloha funguje')
add(dict(kind='sb-stats', t='Jak úloha 3 funguje', stats=[['4', 'obrázky'], ['1', 'příběh'], ['10', 'bodů']],
         uk='4 картинки — одна історія. Розповідаєте в минулому часі: що сталося. Разом 10 балів.'),
    'Jak úloha tři funguje? Dostanete čtyři obrázky, které dohromady tvoří jeden příběh. Vy vyprávíte, co se stalo – v minulém čase. Za tuto úlohu můžete dostat deset bodů.', name='n_how1', pad=1.2, side=SC + 'om3_t.png')
add(dict(kind='sb-list', t='Minulý čas: -l, -la, -li',
         items=['👨 on <b>šel</b>, <b>měl</b>, <b>byl</b>', '👩 ona <b>šla</b>, <b>měla</b>, <b>byla</b>', '👨‍👩‍👧 oni <b>šli</b>, <b>měli</b>, <b>byli</b>', '🙋 já <b>jsem šel / šla</b>'],
         uk='Минулий час: чоловік -l, жінка -la, кілька людей -li. Про себе — з «jsem».'),
    'Nejdůležitější je minulý čas. Muž: šel, měl, byl. Žena: šla, měla, byla. Více lidí: šli, měli, byli. A když mluvíte o sobě, nezapomeňte jsem: šel jsem, šla jsem. Teď si projdeme všech pět příběhů. Nejdřív vyprávějte sami, pak uslyšíte vzor.',
    name='n_how2', pad=1.2, side=SC + 'v05_1.png')

# 3. Усі 5 історій
SECS = 12
for i in range(5):
    n = T0 + i + 1; les = LP[i]
    chap(f'Příběh {n}: {NAMES[i]}')
    add(dict(kind='sb-topic', chip='PŘÍBĚH', i=i + 1, top=NAMES[i], uk=UKN[i], subt='4 obrázky · vyprávějte v minulém čase · pak vzor'),
        f'Příběh {gen.cznum(n)}: {NAMES[i]}.', name=f'n_p{n}', pad=0.6, side=scn(n)[0])
    waited = False
    for s in les['segs']:
        k = s['slide']['kind']
        if k in ('x-intro', 'x-outro'): continue
        sl = {kk: v for kk, v in s['slide'].items() if kk != 'sec'}
        sl['scn'] = scn(n)
        if k == 'v-model': sl['map'] = MAPS[n]
        if k.endswith('-wait'):
            if not waited:
                waited = True; wait(dict(sl, kind=k[:-5]), SECS, 'Teď vy! Vyprávějte v minulém čase.')
            continue
        add(sl, s['sub'], audio=s['audio'], dur=s['dur'])

# 4. 12 фраз
PH = [('Včera ráno …', 'Včera ráno jsem vstal v sedm hodin.', 'Вчора вранці …'),
      ('Nejdřív …', 'Nejdřív jsem se nasnídal.', 'Спочатку …'),
      ('Potom / Pak …', 'Potom jsem šel do práce.', 'Потім …'),
      ('Najednou …', 'Najednou začalo pršet.', 'Раптом …'),
      ('Nakonec …', 'Nakonec jsme šli domů.', 'Нарешті, зрештою …'),
      ('… protože …', 'Byl unavený, protože hodně pracoval.', '… тому що …'),
      ('… a proto …', 'Neměli deštník, a proto byli mokří.', '… і тому …'),
      ('Bylo …', 'Bylo hezké počasí.', 'Було … (погода, ситуація)'),
      ('šel / šla / šli', 'Odpoledne šla na policii.', 'пішов / пішла / пішли'),
      ('měl / měla', 'Marie měla narozeniny.', 'мав / мала'),
      ('musel / musela', 'Pan Tichý musel zůstat doma.', 'мусив / мусила'),
      ('Večer …', 'Večer přišli kamarádi.', 'Увечері …')]
PHS = [SC + 'v01_1.png', SC + 'v01_2.png', SC + 'v01_3.png', SC + 'v02_3.png', SC + 'v01_4.png', SC + 'v03_1.png', SC + 'v02_3.png', SC + 'v02_2.png', SC + 'v04_4.png', SC + 'v05_2.png', SC + 'v03_4.png', SC + 'v05_3.png']
chap('12 frází pro vyprávění')
add(dict(kind='sb-sec', t='12 frází pro vyprávění', uk='12 фраз, з якими ви розповісте будь-яку історію — слухайте й повторюйте', ic='🗣️'),
    'Teď dvanáct frází, se kterými zvládnete každý příběh. Poslouchejte a opakujte nahlas.', name='n_ph', pad=1.0, side=SC + 'om3_t.png')
for j, (tp, ex, uk) in enumerate(PH):
    base = dict(kind='sb-ph', i=j + 1, n=len(PH), tp=tp, ex=ex, uk=uk)
    add(base, ex, name=f'ph{j}', pad=0.5, side=PHS[j])
    wait(base, 3, 'Opakujte!', side=PHS[j])

# 5. Помилки
ER = [('Obrázek 1: Olga leží v posteli', 'Olga leží v posteli.', 'Olga ležela v posteli.', 'Vyprávějte v minulém čase: ležela, šla, koupila.', 'Розповідаємо в минулому часі, не в теперішньому.', '/home/claude/yt/ab2/pilot/v07_1.png'),
      ('Marie (žena)', 'Marie pekl dort.', 'Marie pekla dort.', 'Žena: -la. Muž: -l. Více lidí: -li.', 'Жінка — закінчення -la, чоловік — -l.', SC + 'v05_1.png'),
      ('Mluvíte o sobě', 'Včera šel do práce.', 'Včera jsem šel do práce.', 'Když mluvíte o sobě, nezapomeňte jsem.', 'Про себе — обов’язково «jsem»: šel jsem, šla jsem.', SC + 'v03_1.png'),
      ('4 obrázky', 'Obrázek jedna: auto. Obrázek dvě: krabice.', 'Ráno balili věci a potom přijelo auto.', 'Nepopisujte obrázky. Vyprávějte příběh se spojkami: nejdřív, potom, nakonec.', 'Не описуйте картинки — розкажіть історію зі сполучниками.', SC + 'v01_2.png'),
      ('Příliš krátce', 'Jel na kole. Spadl.', 'Jel na kole do práce. Najednou vyběhl pes a on spadl.', 'Ke každému obrázku řekněte dvě až tři věty: kdo, kde, co a proč.', 'До кожної картинки 2–3 речення: хто, де, що і чому.', SC + 'v03_2.png')]
chap('5 typických chyb')
add(dict(kind='sb-sec', t='5 typických chyb', uk='5 типових помилок, через які втрачають бали', ic='⚠️'),
    'Pět typických chyb, kvůli kterým lidé ztrácejí body.', name='n_er', pad=1.0, side=SC + 'v02_3.png')
for j, (q, bad, good, rule, uk, sd) in enumerate(ER):
    base = dict(kind='sb-er', i=j + 1, q=q, bad=bad, good=good, rule=rule, uk=uk, ok=False)
    add(base, None, dur=2.5, side=sd)
    add(dict(base, ok=True), f'Správně: {good} {rule}', name=f'er{j}', pad=1.5, side=sd)

# 6. Висновок
chap('Shrnutí: 4 pravidla na plný počet bodů')
add(dict(kind='sb-list', fs=70, t='Shrnutí: 4 pravidla na plný počet bodů',
         items=['1️⃣ <b>Minulý čas</b> – šel, měla, byli', '2️⃣ <b>Spojky:</b> nejdřív, potom, nakonec', '3️⃣ <b>2–3 věty</b> ke každému obrázku', '4️⃣ <b>Rod:</b> on šel – ona šla'],
         uk='Минулий час · сполучники · 2–3 речення на картинку · правильний рід'),
    'Shrnutí. Za prvé: vyprávějte v minulém čase. Za druhé: spojujte věty – nejdřív, potom, nakonec. Za třetí: ke každému obrázku řekněte dvě až tři věty. A za čtvrté: pozor na rod – on šel, ona šla.', name='n_sum', pad=1.5, side=SC + 'om3_t.png')
add(dict(kind='sb-cta', t='Který příběh je pro vás nejtěžší?', uk='Яка історія для вас найважча? Напишіть у коментарях — і поставте лайк 👍'),
    'Který příběh je pro vás nejtěžší? Napište to do komentáře – a zkuste tam napsat první dvě věty v minulém čase. A pokud vám video pomohlo, dejte like.', name='n_cta', pad=1.5, side=SC + 'v05_4.png')

# 7. Фінал
chap('Co dál')
add(dict(kind='sb-outro', t='Všech 40 příběhů na webu', next='Zítra: Mluvení 4 – velké opakování'),
    'Na webu Zkouška A2 nanečisto si můžete všechny příběhy procvičit zdarma – web vás poslouchá a kontroluje minulý čas. Odkaz je v popisu. Zítra: velké opakování Mluvení, úloha čtyři. Odebírejte kanál, ať vám nic neuteče.', name='n_out', pad=2.5, side=D7 + 'outro.png')

json.dump(dict(id=KEY, segs=segs, chapters=chapters, n=C), open(f'{OUT}/plan.json', 'w'), ensure_ascii=False)
json.dump(EL_MISSING, open('/home/claude/el/missing.json', 'w'), ensure_ascii=False)
tot = sum(s['dur'] for s in segs)
print(KEY, 'segs', len(segs), 'dur', round(tot), 'missing', len(EL_MISSING), sum(len(x['t']) for x in EL_MISSING))
for t, c in chapters: print(f'{int(t // 60)}:{int(t % 60):02d} {c}')

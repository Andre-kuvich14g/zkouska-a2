"""Велике повторення Mluvení 3 (příběhy): python3 tools/yt/sum_m3.py 3  -> $YT_OUT/om3_3/plan.json
Відновлено 26.11.2026: голоси уроків і повторювані фрази вирізаються з опублікованих відео (YT_REUSE=1),
картинки історій — tools/yt/scenes/vNN_1..4.png (extract_panels.py або сцени дня)."""
import sys, os, json, wave
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
os.environ.setdefault('YT_REUSE', '1')
import gen, voice
from gen import fr, spoken
from voice import EL_M, EL_F
def el_say(v, t, path=None): return voice.say(v, t)

C = int(sys.argv[1]) if len(sys.argv) > 1 else 1
T0 = (C - 1) * 5; A, B = T0 + 1, T0 + 5
KEY = f'om3_{C}'
OUT = f"{gen.OUT}/{KEY}"; os.makedirs(OUT, exist_ok=True)
SC = gen.SCN + '/'
TR = json.load(open(gen.ROOT + '/yt-upload/tr.json'))
_D = gen.data(); LP = [gen.v_lesson(_D, T0 + i + 1) for i in range(5)]
NAMES = [p['segs'][0]['slide']['name'] for p in LP]
UKN = [TR[f'v{T0 + i + 1:02d}']['uk']['title'].split(': ', 1)[1] for i in range(5)]
MAPS = {1: [0, 0, 0, 1, 1, 1, 2, 2, 3, 3, 3], 2: [0, 0, 0, 1, 1, 2, 2, 3, 3, 3], 3: [0, 0, 1, 1, 1, 2, 2, 3, 3, 3],
        4: [0, 0, 1, 1, 2, 3, 3, 3], 5: [0, 0, 0, 0, 1, 1, 1, 2, 2, 2, 3, 3]}
FR = dict(sb=C, sbu='Mluvení 3', sbr='příběhy')
scn = lambda n: [f'{SC}v{n:02d}_{j}.png' for j in range(1, 5)]

segs = []; chapters = []
def dur_of(p): return voice.dur(p)
def add(slide, text=None, voice=EL_M, name=None, pad=0.8, audio=None, dur=None, side=None):
    if audio: d, path = dur_of(audio), audio
    elif text: path, d = el_say(voice, spoken(text))
    else: d, path = 0, None
    sl = dict(slide, sec='v', **FR)
    if side: sl['side'] = side
    segs.append(dict(slide=sl, dur=dur or fr(d + pad + 0.2), audio=path, adur=d, sub=spoken(text) if text else None))
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
    name='n_intro', pad=1.2, side=scn(T0 + 3)[3])

# 2. Як працює
chap('Jak úloha funguje')
add(dict(kind='sb-stats', t='Jak úloha 3 funguje', stats=[['4', 'obrázky'], ['1', 'příběh'], ['10', 'bodů']],
         uk='4 картинки — одна історія. Розповідаєте в минулому часі: що сталося. Разом 10 балів.'),
    'Jak úloha tři funguje? Dostanete čtyři obrázky, které dohromady tvoří jeden příběh. Vy vyprávíte, co se stalo – v minulém čase. Za tuto úlohu můžete dostat deset bodů.', name='n_how1', pad=1.2, side=scn(T0 + 3)[3])
add(dict(kind='sb-list', t='Minulý čas: -l, -la, -li',
         items=['👨 on <b>šel</b>, <b>měl</b>, <b>byl</b>', '👩 ona <b>šla</b>, <b>měla</b>, <b>byla</b>', '👨‍👩‍👧 oni <b>šli</b>, <b>měli</b>, <b>byli</b>', '🙋 já <b>jsem šel / šla</b>'],
         uk='Минулий час: чоловік -l, жінка -la, кілька людей -li. Про себе — з «jsem».'),
    'Nejdůležitější je minulý čas. Muž: šel, měl, byl. Žena: šla, měla, byla. Více lidí: šli, měli, byli. A když mluvíte o sobě, nezapomeňte jsem: šel jsem, šla jsem. Teď si projdeme všech pět příběhů. Nejdřív vyprávějte sami, pak uslyšíte vzor.',
    name='n_how2', pad=1.2, side=scn(T0 + 5)[0])

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
        if k.endswith('-wait'):
            if not waited:
                waited = True; wait(dict(sl, kind=k[:-5]), SECS, 'Teď vy! Vyprávějte v minulém čase.')
            continue
        add(sl, s['sub'], audio=s['audio'], dur=s['dur']) if s['audio'] else add(sl, s['sub'], pad=0.0)

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
PHS = [scn(T0 + 1)[0], scn(T0 + 1)[1], scn(T0 + 1)[2], scn(T0 + 2)[2], scn(T0 + 1)[3], scn(T0 + 3)[0], scn(T0 + 2)[2], scn(T0 + 2)[1], scn(T0 + 4)[3], scn(T0 + 5)[1], scn(T0 + 3)[3], scn(T0 + 5)[2]]
chap('12 frází pro vyprávění')
add(dict(kind='sb-sec', t='12 frází pro vyprávění', uk='12 фраз, з якими ви розповісте будь-яку історію — слухайте й повторюйте', ic='🗣️'),
    'Teď dvanáct frází, se kterými zvládnete každý příběh. Poslouchejte a opakujte nahlas.', name='n_ph', pad=1.0, side=scn(T0 + 3)[3])
for j, (tp, ex, uk) in enumerate(PH):
    base = dict(kind='sb-ph', i=j + 1, n=len(PH), tp=tp, ex=ex, uk=uk)
    add(base, ex, name=f'ph{j}', pad=0.5, side=PHS[j])
    wait(base, 3, 'Opakujte!', side=PHS[j])

# 5. Помилки
ER = [('Obrázek 1: Olga leží v posteli', 'Olga leží v posteli.', 'Olga ležela v posteli.', 'Vyprávějte v minulém čase: ležela, šla, koupila.', 'Розповідаємо в минулому часі, не в теперішньому.', scn(T0 + 2)[0]),
      ('Marie (žena)', 'Marie pekl dort.', 'Marie pekla dort.', 'Žena: -la. Muž: -l. Více lidí: -li.', 'Жінка — закінчення -la, чоловік — -l.', scn(T0 + 5)[0]),
      ('Mluvíte o sobě', 'Včera šel do práce.', 'Včera jsem šel do práce.', 'Když mluvíte o sobě, nezapomeňte jsem.', 'Про себе — обов’язково «jsem»: šel jsem, šla jsem.', scn(T0 + 3)[0]),
      ('4 obrázky', 'Obrázek jedna: auto. Obrázek dvě: krabice.', 'Ráno balili věci a potom přijelo auto.', 'Nepopisujte obrázky. Vyprávějte příběh se spojkami: nejdřív, potom, nakonec.', 'Не описуйте картинки — розкажіть історію зі сполучниками.', scn(T0 + 1)[1]),
      ('Příliš krátce', 'Jel na kole. Spadl.', 'Jel na kole do práce. Najednou vyběhl pes a on spadl.', 'Ke každému obrázku řekněte dvě až tři věty: kdo, kde, co a proč.', 'До кожної картинки 2–3 речення: хто, де, що і чому.', scn(T0 + 3)[1])]
chap('5 typických chyb')
add(dict(kind='sb-sec', t='5 typických chyb', uk='5 типових помилок, через які втрачають бали', ic='⚠️'),
    'Pět typických chyb, kvůli kterým lidé ztrácejí body.', name='n_er', pad=1.0, side=scn(T0 + 2)[2])
for j, (q, bad, good, rule, uk, sd) in enumerate(ER):
    base = dict(kind='sb-er', i=j + 1, q=q, bad=bad, good=good, rule=rule, uk=uk, ok=False)
    add(base, None, dur=2.5, side=sd)
    add(dict(base, ok=True), f'Správně: {good} {rule}', name=f'er{j}', pad=1.5, side=sd)

# 6. Висновок
chap('Shrnutí: 4 pravidla na plný počet bodů')
add(dict(kind='sb-list', fs=70, t='Shrnutí: 4 pravidla na plný počet bodů',
         items=['1️⃣ <b>Minulý čas</b> – šel, měla, byli', '2️⃣ <b>Spojky:</b> nejdřív, potom, nakonec', '3️⃣ <b>2–3 věty</b> ke každému obrázku', '4️⃣ <b>Rod:</b> on šel – ona šla'],
         uk='Минулий час · сполучники · 2–3 речення на картинку · правильний рід'),
    'Shrnutí. Za prvé: vyprávějte v minulém čase. Za druhé: spojujte věty – nejdřív, potom, nakonec. Za třetí: ke každému obrázku řekněte dvě až tři věty. A za čtvrté: pozor na rod – on šel, ona šla.', name='n_sum', pad=1.5, side=scn(T0 + 3)[3])
add(dict(kind='sb-cta', t='Který příběh je pro vás nejtěžší?', uk='Яка історія для вас найважча? Напишіть у коментарях — і підпишіться на канал 🔔', sub='Napište do komentáře · odebírejte kanál – každý den nové video'),
    'Který příběh je pro vás nejtěžší? Napište to do komentáře – a zkuste tam napsat první dvě věty v minulém čase. A jestli vám video pomáhá, odebírejte kanál – každý den je tu nové video.', name='n_cta', pad=1.5, side=scn(T0 + 5)[3])

# 7. Фінал
chap('Co dál')
add(dict(kind='sb-outro', t='Všech 40 příběhů na webu', next='Zítra: Mluvení 4 – velké opakování'),
    'Na webu Zkouška A2 nanečisto si můžete všechny příběhy procvičit zdarma – web vás poslouchá a kontroluje minulý čas. Odkaz je v popisu. Zítra: velké opakování Mluvení, úloha čtyři. Odebírejte kanál, ať vám nic neuteče.', name='n_out', pad=2.5, side=SC + 'outro.png')

json.dump(dict(id=KEY, segs=segs, chapters=chapters, n=C), open(f'{OUT}/plan.json', 'w'), ensure_ascii=False)
voice.save_missing(gen.ROOT + f'/tools/el/miss_{KEY}.json')
tot = sum(s['dur'] for s in segs)
print(KEY, 'segs', len(segs), 'dur', round(tot), 'missing', voice.MISSING)
for t, c in chapters: print(f'{int(t // 60)}:{int(t % 60):02d} {c}')

"""Аудіокурс «Zkouška A2 do sluchátek» (27.11.2026): python3 tools/yt/prod.py m1 [m2 m3 m4 p1 p2]
-> $YT_OUT/prod_<part>/plan.json (+ список відсутніх голосів tools/el/miss_prod_<part>.json)

Структура (ТЗ Андре 27.11): прев'ю ЧЕСЬКОЮ («так звучить ваш іспит» + 3 приклади) → вступ «як працювати»
→ 8 блоків × 5 тем (уроки gen.py без інтро/аутро) → після кожного блоку 12 фраз саме до цих 5 тем (prod_phrases.py)
→ мотивація → підсумок «4 правила» → фінал. Уся озвучка чеською: Daniel – ведучий/кандидат, Michaela – екзаменаторка.
Голоси: кеш відео, сайт (learn/audio), YT_XCACHE (вивантаження з Завантажень), YT_REUSE (вирізки з опублікованих відео).
"""
import json, math, os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import gen, voice
from gen import fr, spoken, cznum, masc
from voice import EL_M, EL_F
from prod_phrases import PH

K = dict(m1='m', m2='d', m3='v', m4='r', p1='f', p2='p')
NAME = dict(m1='Mluvení 1', m2='Mluvení 2', m3='Mluvení 3', m4='Mluvení 4', p1='Psaní 1', p2='Psaní 2')
UNITS = dict(m1=('Téma', 'Témata', 'témat'), m2=('Karta', 'Karty', 'karet'), m3=('Příběh', 'Příběhy', 'příběhů'),
             m4=('Situace', 'Situace', 'situací'), p1=('Formulář', 'Formuláře', 'formulářů'), p2=('E-mail', 'E-maily', 'e-mailů'))
INTRO = {
    'm1': 'Zkouška A2 do sluchátek. Mluvení, úloha jedna. Čtyřicet témat, čtyři sta otázek a ke každé vzorová odpověď. Po každých pěti tématech dvanáct důležitých frází. Nasaďte si sluchátka a mluvte nahlas.',
    'm2': 'Zkouška A2 do sluchátek. Mluvení, úloha dvě. Čtyřicet karet: na každé kartě se zeptáte na čtyři věci a uslyšíte celý dialog se zkoušející. Po každých pěti kartách dvanáct důležitých otázek. Nasaďte si sluchátka a mluvte nahlas.',
    'm3': 'Zkouška A2 do sluchátek. Mluvení, úloha tři. Čtyřicet příběhů podle obrázků v minulém čase. Po každých pěti příbězích dvanáct důležitých frází. Nasaďte si sluchátka a mluvte nahlas.',
    'm4': 'Zkouška A2 do sluchátek. Mluvení, úloha čtyři. Čtyřicet situací: domluvíte se se zkoušející, vyberete jednu ze tří možností a řeknete proč. Po každých pěti situacích dvanáct důležitých frází. Nasaďte si sluchátka a mluvte nahlas.',
    'p1': 'Zkouška A2 do sluchátek. Psaní, úloha jedna. Čtyřicet formulářů, sto dvacet otázek a ke každé vzorová odpověď celou větou. Po každých pěti formulářích dvanáct důležitých frází. Připravte si papír a tužku.',
    'p2': 'Zkouška A2 do sluchátek. Psaní, úloha dvě. Čtyřicet e-mailů a ke každému vzorový e-mail na plný počet bodů. Po každých pěti e-mailech dvanáct důležitých frází. Připravte si papír a tužku.',
}
HOW = {
    'm1': 'Jak s kurzem pracovat? Zkoušející se zeptá. Pak máte pár sekund na vlastní odpověď – mluvte nahlas a celou větou. Potom uslyšíte vzorovou odpověď na plný počet bodů.',
    'm2': 'Jak s kurzem pracovat? Uslyšíte situaci a nápovědu. Pak máte pár sekund – zeptejte se celou otázkou a vykejte. Potom uslyšíte vzorovou otázku a odpověď zkoušející.',
    'm3': 'Jak s kurzem pracovat? Uslyšíte otázku a popis čtyř obrázků. Pak máte dvacet sekund – vyprávějte příběh nahlas v minulém čase. Potom uslyšíte vzorové vyprávění.',
    'm4': 'Jak s kurzem pracovat? Zkoušející řekne situaci a tři možnosti. Pak máte pár sekund – navrhněte jednu možnost. Potom uslyšíte celý vzorový dialog.',
    'p1': 'Jak s kurzem pracovat? Uslyšíte otázku z formuláře. Zastavte si nahrávku a napište odpověď, minimálně deset slov. Potom uslyšíte vzor na plný počet bodů.',
    'p2': 'Jak s kurzem pracovat? Uslyšíte zadání e-mailu. Zastavte si nahrávku a napište vlastní e-mail, minimálně třicet pět slov. Potom uslyšíte vzorový e-mail.',
}
HOW_UK = {
    'm1': 'Питання екзаменатора → пауза: відповідайте вголос цілим реченням → зразок на повний бал.',
    'm2': 'Ситуація й підказка → пауза: запитайте цілим реченням на «ви» → зразок питання й відповідь.',
    'm3': 'Питання й 4 картинки → 20 секунд: розкажіть історію в минулому часі → зразок.',
    'm4': 'Ситуація й 3 варіанти → пауза: запропонуйте один → увесь зразковий діалог.',
    'p1': 'Питання з формуляра → зупиніть запис і напишіть відповідь (мін. 10 слів) → зразок.',
    'p2': 'Завдання e-mailу → зупиніть запис і напишіть e-mail (мін. 35 слів) → зразковий e-mail.',
}
SUM = {  # «4 правила» — тексти з опублікованих збірок (є готова озвучка)
    'm1': 'Shrnutí. Za prvé: odpovídejte celou větou, nejlépe dvěma větami. Za druhé: poslouchejte čas v otázce a odpovězte ve stejném čase. Za třetí: pozor na pády – z Ukrajiny, v Praze. A za čtvrté: mluvte konkrétně – čísla, místa, jména.',
    'm2': 'Shrnutí. Za prvé: z nápovědy udělejte celou otázku. Za druhé: vykejte – máte, můžete. Za třetí: tázací slovo dejte na začátek. A za čtvrté: vlastní otázku mějte připravenou předem.',
    'm3': 'Shrnutí. Za prvé: vyprávějte v minulém čase. Za druhé: spojujte věty – nejdřív, potom, nakonec. Za třetí: ke každému obrázku řekněte dvě až tři věty. A za čtvrté: pozor na rod – on šel, ona šla.',
    'm4': 'Shrnutí. Za prvé: navrhujte celou větou. Za druhé: když zkoušející nesouhlasí, navrhněte jinou možnost. Za třetí: na konci řekněte důvod – protože. A za čtvrté: s kamarádkou si tykáte.',
    'p1': 'Shrnutí. Za prvé: odpovídejte celou větou, minimálně deset slov. Za druhé: použijte slova z otázky. Za třetí: odpovězte na všechno, na co se otázka ptá. A za čtvrté: pište konkrétně – kdy, kde, kolik.',
    'p2': 'Shrnutí. Za prvé: pozdrav na začátku a na konci. Za druhé: ke každému obrázku jedna věta. Za třetí: minimálně třicet pět slov. A za čtvrté: úřadu a firmě vykejte, kamarádovi tykejte.',
}
SUM_LIST = {
    'm1': (['1️⃣ <b>Celá věta</b> – nejlépe dvě', '2️⃣ <b>Stejný čas</b> jako v otázce', '3️⃣ <b>Pády:</b> z Ukrajiny · v Praze', '4️⃣ <b>Konkrétně:</b> čísla, místa, jména'], 'Повне речення · той самий час · відмінки · конкретика'),
    'm2': (['1️⃣ <b>Celá otázka</b> z nápovědy', '2️⃣ <b>Vykání:</b> máte, můžete', '3️⃣ <b>Tázací slovo</b> na začátek', '4️⃣ <b>Vlastní otázka</b> připravená'], 'Ціле питання · на «ви» · питальне слово спочатку · своє питання наготові'),
    'm3': (['1️⃣ <b>Minulý čas</b>', '2️⃣ <b>Spojky:</b> nejdřív, potom, nakonec', '3️⃣ <b>2–3 věty</b> ke každému obrázku', '4️⃣ <b>Rod:</b> on šel, ona šla'], 'Минулий час · сполучники · 2–3 речення на картинку · рід'),
    'm4': (['1️⃣ <b>Celá věta:</b> Můžeme… / Co kdybychom…', '2️⃣ <b>Ne? Jiný návrh:</b> Tak…', '3️⃣ <b>Důvod:</b> protože…', '4️⃣ <b>Tykání:</b> máš, chceš'], 'Ціле речення · нова пропозиція після «ні» · причина · на «ти»'),
    'p1': (['1️⃣ <b>Celá věta</b> – min. 10 slov', '2️⃣ <b>Slova z otázky</b>', '3️⃣ <b>Odpověď na všechno</b>', '4️⃣ <b>Konkrétně:</b> kdy, kde, kolik'], 'Ціле речення · слова з питання · відповідь на все · конкретика'),
    'p2': (['1️⃣ <b>Pozdrav</b> na začátku i na konci', '2️⃣ <b>1 věta</b> ke každému obrázku', '3️⃣ <b>Min. 35 slov</b>', '4️⃣ <b>Vy / ty</b> podle adresáta'], 'Привітання · речення на кожну картинку · мін. 35 слів · «ви»/«ти»'),
}
HOOK = 'Takhle zní vaše zkouška.'
PH_INTRO = 'Teď dvanáct důležitých frází k tomuto bloku. Poslouchejte a opakujte nahlas.'
MOT = ['Výborně! První blok máte za sebou.', 'Skvělé, dva bloky hotové. Jen tak dál!', 'Už máte za sebou tři bloky. Pokračujeme.',
       'Polovina je hotová! Udělejte si krátkou pauzu a pokračujte.', 'Pět bloků za vámi. Vaše čeština je každým dnem lepší.',
       'Šest bloků hotovo. Už jste blízko cíle.', 'Ještě poslední blok. Do toho!']
FINAL = 'To je celý kurz. Opakujte jeden blok denně a za osm dní budete mít všechno zopakované. Další části kurzu a cvičné zkoušky zdarma najdete na webu Zkouška A2 nanečisto. Hodně štěstí u zkoušky!'
PREVIEW_FROM = [1, 13, 27]  # уроки, з яких беремо 3 приклади для прев'ю


def build(part):
    k = K[part]; D = gen.data(); U1, U2, U3 = UNITS[part]
    PROD = f'🎧 Zkouška A2 do sluchátek · <b>{NAME[part]}</b>'
    segs = []; chapters = []

    def say(v, t): return voice.say(v, spoken(t))

    def add(slide, text=None, v=EL_M, pad=0.8, dur=None, audio=None, adur=None):
        sl = dict(slide); sl.setdefault('sec', k); sl.setdefault('prod', PROD)
        if text and not audio:
            audio, adur = say(v, text)
        if text:
            segs.append(dict(slide=sl, dur=dur or fr((adur or 1) + pad + 0.2), audio=audio, adur=adur, sub=spoken(text)))
        else:
            segs.append(dict(slide=sl, dur=dur or 1.0, audio=None, sub=None))

    def wait(slide, n, msg):
        for c in range(n, 0, -1):
            add(dict(slide, kind=slide['kind'] + '-w', c=c, msg=msg), dur=1.0)

    def chap(t): chapters.append((round(sum(s['dur'] for s in segs), 2), t))

    def lesson(n):
        p = gen.FN[k](D, n); out = []
        for s in p['segs']:
            kd = s['slide']['kind']
            if kd in ('x-intro', 'x-outro'): continue
            s = dict(s); s['slide'] = dict(s['slide'])
            if kd == 'm-q':  # питання читає екзаменаторка (є озвучка сайту)
                a, d = voice.find(EL_F, masc(s['sub'])), None
                if a: s['audio'], s['adur'] = a, voice.dur(a); s['dur'] = fr(s['adur'] + 0.7)
            out.append(s)
            # аудіо без картинок: озвучити те, що видно лише на слайді
            if k == 'v' and kd == 'v-pics' and s['audio']:
                for i, x in enumerate(s['slide']['pics']):
                    t = f"Obrázek {cznum(i + 1)}. {x['t']}"
                    a, d = say(EL_F, t)
                    out.append(dict(slide=dict(s['slide'], hi=i), dur=fr(d + 0.5), audio=a, adur=d, sub=t))
            if k == 'r' and kd == 'r-task' and s['audio']:
                o = [x['t'] for x in s['slide']['opts']]
                t = f"Možnosti: {', '.join(o[:-1])}, nebo {o[-1]}."
                a, d = say(EL_F, t)
                out.append(dict(slide=s['slide'], dur=fr(d + 0.5), audio=a, adur=d, sub=t))
        if k == 'd':  # підказка вголос перед кожною паузою «Teď vy! Zeptejte se.»
            res = []; seen = set()
            for s in out:
                sl = s['slide']
                if sl['kind'] == 'd-cue-wait' and sl['k'] not in seen:
                    seen.add(sl['k']); cue = sl['cues'][sl['k'] - 1]
                    t = 'Vaše vlastní otázka.' if '(' in cue else cue
                    a, d = say(EL_F, t)
                    res.append(dict(slide=dict(sl, kind='d-chat', lines=[]), dur=fr(d + 0.4), audio=a, adur=d, sub=t))
                res.append(s)
            out = res
        # Psaní 2: якщо речення e-mailу не озвучені — один сегмент з повним e-mailом (озвучка сайту)
        if k == 'p' and any(s['slide']['kind'] == 'p-model' and not s['audio'] for s in out):
            e = D['p'][n - 1]; full = gen.masc(e['model']).strip()
            a = voice.find(EL_M, full)
            first = next(i for i, s in enumerate(out) if s['slide']['kind'] == 'p-model')
            sl = dict(out[first]['slide'], hi=-1)
            rest = [s for s in out if s['slide']['kind'] != 'p-model']
            if a:
                seg = dict(slide=sl, dur=fr(voice.dur(a) + 0.8), audio=a, adur=voice.dur(a), sub=re.sub(r'\s+', ' ', full))
            else:
                ap, d = say(EL_M, re.sub(r'\s+', ' ', full)); seg = dict(slide=sl, dur=fr(d + 0.8), audio=ap, adur=d, sub=re.sub(r'\s+', ' ', full))
            out = rest[:first] + [seg] + rest[first:]
        return out

    def item_title(n):
        if k == 'm': return D['m'][n - 1][0], D['m'][n - 1][1][0]
        if k == 'v': return D['v'][n - 1]['title'], D['v'][n - 1]['t'][0]
        if k == 'p': return D['p'][n - 1]['subject'], None
        return D[k][n - 1]['cz'], None

    def header_text(n, nm):
        if k in ('m', 'v', 'p'): return f'{U1} {cznum(n)}: {nm}.'
        return f'{U1} {cznum(n)}.'

    # 0. Прев'ю
    chap('Úvod · Takhle zní vaše zkouška')
    add(dict(kind='pr-hook', t=HOOK, sub=f'Zkouška A2 do sluchátek · {NAME[part]}'), HOOK, pad=0.6)
    for n in PREVIEW_FROM:
        L = [s for s in lesson(n) if s['audio'] and not s['slide']['kind'].endswith(('-w', '-wait'))]
        take = L[:2] if k in ('m', 'f') else L[:3]
        for s in take: segs.append(dict(s, dur=fr(s['adur'] + 0.4)))
    add(dict(kind='sb-intro2', chip='ZKOUŠKA A2 DO SLUCHÁTEK', title=f'{NAME[part]}:<br>40 {U3} + 96 frází',
             topics=[f'8 bloků · 40 {U3} · po každém bloku 12 frází'],
             agenda=['Jak to funguje', f'8 bloků × 5 {U3}', '12 frází po každém bloku', '4 pravidla'], hook=''),
        INTRO[part], pad=1.0)
    add(dict(kind='sb-list', t='Jak s kurzem pracovat', items=['1️⃣ Poslouchejte zadání', '2️⃣ <b>Teď vy!</b> – mluvte / pište sami', '3️⃣ Vzor na plný počet bodů', '4️⃣ 12 frází – opakujte nahlas'], uk=HOW_UK[part]),
        HOW[part], pad=1.2)

    # 1–8. Блоки
    for b in range(8):
        a = b * 5 + 1; z = a + 4
        names = [item_title(n)[0] for n in range(a, z + 1)]
        chap(f'Blok {b + 1}: {U2} {a}–{z}')
        add(dict(kind='pr-block', b=b + 1, a=a, t=f'{U2} {a}–{z}', names=names, prod=f'{PROD} · blok {b + 1}/8'),
            f'Blok {cznum(b + 1)}. {U2} {cznum(a)} až {cznum(z)}.', pad=1.0)
        for n in range(a, z + 1):
            nm, uk = item_title(n)
            chap(f'{U1} {n}: {nm}')
            add(dict(kind='pr-item', chip=f'{U1.upper()} {n} / 40 · BLOK {b + 1}', t=nm, uk=uk, prod=f'{PROD} · blok {b + 1}/8'),
                header_text(n, nm), pad=0.6)
            for s in lesson(n):
                s['slide']['prod'] = f'{PROD} · blok {b + 1}/8 · {U1.lower()} {n}/40'
                segs.append(s)
        chap(f'Blok {b + 1}: 12 frází')
        add(dict(kind='sb-sec', t=f'12 frází · blok {b + 1}', uk='12 фраз до цих 5 тем — слухайте й повторюйте вголос', ic='🗣️', prod=f'{PROD} · blok {b + 1}/8'),
            PH_INTRO, pad=0.8)
        for j, (tp, ex, uk) in enumerate(PH[part][b]):
            base = dict(kind='sb-ph', i=j + 1, n=12, tp=tp, ex=ex, uk=uk, prod=f'{PROD} · blok {b + 1}/8 · fráze {j + 1}/12')
            add(base, ex, pad=0.4)
            wait(base, max(3, math.ceil(segs[-1]['adur'] or 2) + 1), 'Opakujte!')
        if b < 7:
            add(dict(kind='pr-mot', t=MOT[b], b=b + 1, ic='💪' if b % 2 else '🎉', prod=PROD), MOT[b], pad=1.0)

    # Фінал
    chap('Shrnutí: 4 pravidla')
    it, uk = SUM_LIST[part]
    add(dict(kind='sb-list', fs=70, t='Shrnutí: 4 pravidla na plný počet bodů', items=it, uk=uk), SUM[part], pad=1.5)
    chap('Konec')
    add(dict(kind='sb-outro', t='Zkouška A2 do sluchátek', next='Další části kurzu a cvičné zkoušky zdarma na webu'), FINAL, pad=2.5)

    # прогрес-смуга по розділах блоків
    T = sum(s['dur'] for s in segs)
    out = f'{gen.OUT}/prod_{part}'; os.makedirs(out, exist_ok=True)
    json.dump(dict(id=f'prod_{part}', segs=segs, chapters=chapters, duration=round(T, 1)), open(f'{out}/plan.json', 'w'), ensure_ascii=False)
    return T, chapters


if __name__ == '__main__':
    voice.CACHE = os.environ.get('YT_VCACHE', voice.CACHE); os.makedirs(voice.CACHE, exist_ok=True)
    for part in sys.argv[1:]:
        b0 = len(voice.MISSING)
        T, ch = build(part)
        P = json.load(open(f'{gen.OUT}/prod_{part}/plan.json'))
        used = {(s['sub']) for s in P['segs'] if s.get('sub') and not s.get('audio')}
        miss = [m for m in voice.MISSING[b0:] if m['t'] in used]
        os.makedirs(gen.ROOT + '/tools/el', exist_ok=True)
        json.dump(miss, open(gen.ROOT + f'/tools/el/miss_prod_{part}.json', 'w'), ensure_ascii=False, indent=0)
        print(part, f'{int(T // 3600)}:{int(T % 3600 // 60):02d}:{int(T % 60):02d}', 'chapters', len(ch), 'missing', len(miss), sum(len(m['t']) for m in miss))

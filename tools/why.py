# Automatické „Proč je to správně“ pro režim Тренування: klíčová věta z textu/nahrávky + pasti.
import json, re, unicodedata, sys
STOP = set('a i v ve na do se je to že ale jsem jste jsme mám máte bude budu není pro po od za ze ke k s z u o já ty on ona my vy oni tak taky ještě už jen moc prosím dobrý den děkuju promiňte ano ne tady tam kde kdy co jak proč kolik který která které nebo když jsou byl byla bylo jeho její vás nám vám mi mě si jako'.split())
def fold(s): return ''.join(c for c in unicodedata.normalize('NFD', s.lower()) if unicodedata.category(c) != 'Mn')
NUM = {'jedna':1,'jeden':1,'dva':2,'dvě':2,'tři':3,'čtyři':4,'pět':5,'šest':6,'sedm':7,'osm':8,'devět':9,'deset':10,'jedenáct':11,'dvanáct':12,'patnáct':15,'dvacet':20,'třicet':30,'čtyřicet':40,'padesát':50,'sto':100}
def toks(s):
    out = set()
    for w in re.findall(r'\w+', s.lower()):
        if w in STOP: continue
        if w in NUM: out.add('#%d' % NUM[w]); continue
        if w.isdigit(): out.add('#%d' % int(w)); continue
        if len(w) < 3: continue
        out.add(fold(w)[:5] if len(w) > 5 else fold(w)[:4])
    return out
def sents(text):
    res = []
    for line in text.split('\n'):
        who = ''
        m = re.match(r'^\[(.+?)\]:\s*(.*)$', line)
        if m: who, line = m.group(1), m.group(2)
        for s in re.findall(r'[^.!?]+[.!?]*', line):
            if len(s.strip()) > 3: res.append((who, s.strip()))
    return res
def best(text, good, bad, q='', late=True):
    ss = sents(text); g = toks(good); qq = toks(q); b = set().union(*[toks(x) for x in bad]) if bad else set()
    sc = []
    for i, (who, s) in enumerate(ss):
        t = toks(s)
        v = 3*len(t & (g - b)) + len(t & qq) - 1.5*len(t & (b - g)) + (0.2*i/len(ss) if late else 0)
        sc.append((v, i))
    v, i = max(sc)
    return (ss[i][0] + ': ' if ss[i][0] else '') + ss[i][1], v
def traps(text, bad):
    t = toks(text); return [x for x in bad if toks(x) and (toks(x) - {'#'}) <= t]
d = json.load(open('data-variants.json', encoding='utf-8'))
low = []
for v in d['variants']:
    R, L = v['reading'], v['listening']
    for it in R['t2']['items']:
        o = it['options']; bad = [o[k] for k in o if k != it['answer']]
        it['why'], sc = best(R['t2']['text'], o[it['answer']], bad, it['q'], late=False)
        if sc < 3: low.append((v['id'], 'r2', it['n'], it['q'], o[it['answer']], it['why']))
    for key in ('t1', 't2'):
        for it in L[key]['items']:
            o = it['options']; bad = [o[k] for k in o if k != it['answer']]
            it['why'], sc = best(it['script'], o[it['answer']], bad, it['q'])
            it['traps'] = traps(it['script'], bad)
            if sc < 3: low.append((v['id'], 'l'+key[1], it['n'], it['q'], o[it['answer']], it['why']))
    for it in L['t3']['items']:
        o = L['t3']['options']; bad = [o[k] for k in o if k != it['answer']]
        it['why'], sc = best(it['script'], o[it['answer']], bad)
        it['traps'] = traps(it['script'], bad)
        if sc < 3: low.append((v['id'], 'l3', it['n'], '', o[it['answer']], it['why']))
    for it in L['t4']['items']:
        o = L['t4']['options']; lab = lambda k: o[k]['label']; bad = [lab(k) for k in o if k != it['answer']]
        it['why'], sc = best(it['script'], lab(it['answer']), bad, late=False)
        it['traps'] = traps(it['script'], bad)
        if sc < 3: low.append((v['id'], 'l4', it['n'], '', lab(it['answer']), it['why']))
    for it in L['t5']['items']:
        it['why'], sc = best(L['t5']['script'], ' '.join(it['answers']), [], it['q'], late=False)
        if sc < 3: low.append((v['id'], 'l5', it['n'], it['q'], it['answers'][0], it['why']))
    for it in R['t5']['items']:
        src = R['t5']['text'] + '\n' + '\n'.join(' – '.join(r) + '.' for r in R['t5']['table'])
        it['why'], sc = best(src, ' '.join(it['answers']), [], it['sentence'], late=False)
        if sc < 3: low.append((v['id'], 'r5', it['n'], it['sentence'], it['answers'][0], it['why']))
json.dump(d, open(sys.argv[1] if len(sys.argv) > 1 else '/tmp/why.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
for x in low: print(x)
print('LOW', len(low))

# Psaní: 20 formulářů a 20 e-mailů z variant + 20 + 20 nových
import json, os, re
from w1_new import NEWF
from w2_new import NEWE
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(os.path.dirname(HERE))
d = json.load(open(os.path.join(ROOT, 'data-variants.json'), encoding='utf-8'))
W1, W2 = [], []
for v in d['variants']:
    t1 = v['writing']['t1']; t2 = v['writing']['t2']
    W1.append({'cz': t1['form'], 'situation': t1['situation'], 'qa': [[q, a] for q, a in zip(t1['questions'], t1['models'])]})
    W2.append({'cz': t2['subject'], 'situation': t2['situation'], 'to': t2['to'], 'subject': t2['subject'],
               'prompts': [{'q': p['q'], 'om': p.get('om', [])} for p in t2['prompts']], 'model': t2['model']})
for sit, form, qa in NEWF:
    W1.append({'cz': form, 'situation': sit, 'qa': [list(x) for x in qa]})
for e in NEWE:
    W2.append(dict(e, cz=e['subject']))
for x in W1 + W2: x['t'] = [x['situation']] * 4

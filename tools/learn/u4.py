# Úloha 4: 20 situací z variant + 20 nových
import json, os
from u4_new import NEW4
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(os.path.dirname(HERE))
d = json.load(open(os.path.join(ROOT, 'data-variants.json'), encoding='utf-8'))
U4 = []
for s in [v['speaking']['t4'] for v in d['variants']] + NEW4:
    title = s['situation'].split('. ')[0].rstrip('.?')
    U4.append({'cz': title, 't': [s['situation']] * 4, 'situation': s['situation'],
               'options': [{'label': o['label'], 'om': o.get('om', [])} for o in s['options']], 'dialog': s['dialog']})

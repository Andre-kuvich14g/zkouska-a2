# Úloha 2: 40 karet z variant (data-variants.json), u každé dialog s tazatelem
import json, os
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(os.path.dirname(HERE))
d = json.load(open(os.path.join(ROOT, 'data-variants.json'), encoding='utf-8'))
U2 = []
for v in d['variants']:
    for c in v['speaking']['t2']:
        us = [x[1] for x in c['dialog'] if x[0] == 'U']
        pairs = [[p, us[k] if k < len(us) else ''] for k, p in enumerate(c['points'])]
        U2.append({'cz': c['situation'].rstrip('.'), 't': [c['goal']] * 4, 'situation': c['situation'], 'goal': c['goal'],
                   'pairs': pairs, 'dialog': c['dialog']})

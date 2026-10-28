import json,sys
d=json.load(open('data-variants.json',encoding='utf-8'))['variants']
a,b=int(sys.argv[1]),int(sys.argv[2])
for v in d[a-1:b]:
    R,L=v['reading'],v['listening']; print('######## V',v['id'])
    print('R2 TEXT:',R['t2']['text'].replace('\n',' '))
    for it in R['t2']['items']: print(' R2.%d %s | %s | =%s'%(it['n'],it['q'],' / '.join(k+')'+x for k,x in it['options'].items()),it['answer']))
    for t in ('t1','t2'):
        for it in L[t]['items']: print(' L%s.%d %s | %s | =%s || %s'%(t[1],it['n'],it['q'],' / '.join(k+')'+x for k,x in it['options'].items()),it['answer'],it['script'].replace('\n',' ')))
    o=L['t3']['options']; print(' L3 Q:',L['t3']['q'],'|',' / '.join(k+')'+x for k,x in o.items()))
    for it in L['t3']['items']: print(' L3.%d =%s(%s) || %s'%(it['n'],it['answer'],o[it['answer']],it['script'].replace('\n',' ')))
    o=L['t4']['options']; print(' L4 Q:',L['t4']['q'])
    for it in L['t4']['items']: print(' L4.%d =%s || %s'%(it['n'],o[it['answer']]['label'],it['script'].replace('\n',' ')))

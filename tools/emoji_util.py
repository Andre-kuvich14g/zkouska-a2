import os
SV='/home/claude/openmoji/color/svg/'
HAVE=set(f[:-4] for f in os.listdir(SV)) if os.path.isdir(SV) else set()
def graphemes(s):
    out=[]; cur=''
    chars=list(s); i=0
    while i<len(chars):
        c=chars[i]; o=ord(c)
        if cur and (o in (0x200D,0xFE0F,0x20E3) or 0x1F3FB<=o<=0x1F3FF or (cur and ord(cur[-1])==0x200D)):
            cur+=c
        else:
            if cur: out.append(cur)
            cur=c
        i+=1
    if cur: out.append(cur)
    return [g for g in out if any(ord(ch)>0x2000 for ch in g) and g.strip()]
def openmoji_name(g):
    cps=[f'{ord(c):04X}' for c in g]
    for cand in ['-'.join(cps), '-'.join(c for c in cps if c!='FE0F'), '-'.join(cps)+'-FE0F']:
        if cand in HAVE: return cand
    return None

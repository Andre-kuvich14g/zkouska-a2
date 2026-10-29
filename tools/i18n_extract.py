# Витягує українські фрагменти інтерфейсу з index.html (без вбудованих даних).
import re, json, sys
CYR = re.compile('[А-Яа-яІіЇїЄєҐґ]')
SPLIT = re.compile(r"[<>`\"{}$\n]|(?<![А-Яа-яІіЇїЄєҐґA-Za-z])'|'(?![А-Яа-яІіЇїЄєҐґA-Za-z])")
def template(s):
    return re.sub(r'(<script type="application/json" id="exam-data">).*?(</script>)', r'\1\2', s, flags=re.S)
def segments(s):
    out = []
    for p in SPLIT.split(template(s)):
        if p and CYR.search(p):
            t = p.strip()
            if t not in out: out.append(t)
    return out
if __name__ == '__main__':
    segs = segments(open('index.html', encoding='utf-8').read())
    known = {}
    try: known = json.load(open('tools/i18n.json', encoding='utf-8'))
    except FileNotFoundError: pass
    missing = [x for x in segs if x not in known]
    print(len(segs), 'segments,', len(missing), 'missing')
    for x in missing: print(json.dumps(x, ensure_ascii=False))

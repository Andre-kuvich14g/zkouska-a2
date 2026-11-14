"""Великий ролик «Іспит A2 від А до Я»: біти сценарію (озвучка Flash uk/cs) + приклади з уроків дня 8."""
import json, re, wave, struct, os, subprocess, html
G = '/home/claude/yt/guide'; SR = 44100
beats = json.load(open(f'{G}/beats.json'))
EX = {50: 'f08', 54: 'p08', 67: 'm08', 69: 'd08', 71: 'v08', 73: 'r08'}
EXL = {'f08': 'Приклад: формуляр (Psaní 1)', 'p08': 'Приклад: e-mail (Psaní 2)', 'm08': 'Тренування: 10 питань (Mluvení 1)', 'd08': 'Приклад: картка (Mluvení 2)', 'v08': 'Приклад: розповідь (Mluvení 3)', 'r08': 'Приклад: ситуація (Mluvení 4)'}
CH = []  # (start, title)
shots = []  # dict(img|html, dur)
audio = []  # list of (path or None, dur)
def wav_dur(p):
    w = wave.open(p); d = w.getnframes() / w.getframerate(); w.close(); return d
t = 0.0; cur_ch = None
chap_names = []
for i, b in enumerate(beats):
    ch = re.sub(r'\s*\(.*\)$', '', b['chap'])
    if ch != cur_ch:
        cur_ch = ch; CH.append((t, ch)); chap_names.append(ch)
    # речення: uk-частини ділимо на речення, час пропорційно довжині; cs-частини приклеюємо до поточного речення
    sents = []  # [html, dur]
    cur = ['', 0.0]
    nparts = len(b['parts'])
    for pi, p in enumerate(b['parts']):
        gap = 0.14 if pi < nparts - 1 else 0.75
        audio.append((f"{G}/aud/{p['k']}.wav", p['d'])); audio.append((None, gap))
        if p['l'] == 'cs':
            cur[0] += f'<b>{html.escape(p["t"])}</b> '; cur[1] += p['d'] + gap; continue
        ss = [x for x in re.split(r'(?<=[.?!…])\s+', p['t']) if x.strip()]
        tot = sum(len(x) for x in ss) or 1
        for si, x in enumerate(ss):
            cur[0] += html.escape(x) + ' '; cur[1] += p['d'] * len(x) / tot + (gap if si == len(ss) - 1 else 0)
            if re.search(r'[.?!…]$', x.strip()) and (si < len(ss) - 1 or pi < nparts - 1):
                sents.append(cur); cur = ['', 0.0]
    if cur[0].strip(): sents.append(cur)
    # дуже короткі речення (<1.6 c) зливаємо з наступним
    merged = []
    for x in sents:
        if merged and merged[-1][1] < 1.6: merged[-1] = [merged[-1][0] + x[0], merged[-1][1] + x[1]]
        else: merged.append(list(x))
    for capt, d in merged:
        shots.append(dict(kind='g', scene=f'/home/claude/yt/ab2/guide/b{i:02d}.png', cap=capt.strip(), who=b['who'], ch=len(CH) - 1, dur=d)); t += d
    if i in EX:
        k = EX[i]; pl = json.load(open(f'/home/claude/yt/out_pilot/{k}/plan.json'))
        audio.append((None, 0.4)); shots.append(dict(kind='card', title=EXL[k], ch=len(CH) - 1, dur=2.2)); audio.append((None, 1.8)); t += 2.2
        for s in pl['segs']:
            if s['slide']['kind'].endswith(('intro', 'outro')): continue
            if s.get('audio'):
                ad = wav_dur(s['audio']); audio.append((s['audio'], ad)); audio.append((None, max(0, s['dur'] - ad)))
            else: audio.append((None, s['dur']))
            shots.append(dict(kind='img', img=s['img'], ch=len(CH) - 1, dur=s['dur'])); t += s['dur']
json.dump(dict(shots=shots, chapters=CH, names=chap_names), open(f'{G}/shots.json', 'w'), ensure_ascii=False)
# audio
out = wave.open(f'{G}/guide.wav', 'wb'); out.setnchannels(1); out.setsampwidth(2); out.setframerate(SR)
for p, d in audio:
    if p:
        w = wave.open(p); assert w.getframerate() == SR and w.getnchannels() == 1, p; out.writeframes(w.readframes(w.getnframes())); w.close()
    else: out.writeframes(b'\0\0' * int(round(d * SR)))
out.close()
print('shots', len(shots), 'video', round(sum(s['dur'] for s in shots) / 60, 2), 'audio', round(wav_dur(f'{G}/guide.wav') / 60, 2))
for a, c in CH: print(f'{int(a // 60)}:{int(a % 60):02d} {c}')

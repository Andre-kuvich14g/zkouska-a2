"""План -> MP4 1920x1080 + <id>.cs.srt (відновлено 26.11.2026).

python3 tools/yt/build.py f19 p19 ...      (спершу node tools/yt/slides.js <id>... — або --slides, щоб зробити це тут)
Аудіо: голос кожного сегмента з +0.2 с, у паузах «тік» щосекунди і «дзвіночок» наприкінці. Знизу — смужка прогресу.
Результат: $YT_OUT/<id>/<id>.mp4, <id>.cs.srt; з --copy ще й у yt-upload/.
"""
import json, os, shutil, subprocess, sys, wave
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
OUT = os.environ.get('YT_OUT', '/home/claude/yt/out')
SR = 44100
COL = dict(f='#15803d', p='#15803d', m='#1f5fbf', d='#0f766e', v='#c2410c', r='#6d3fc0', l='#be185d')


def pcm(path):
    raw = subprocess.run(['ffmpeg', '-v', 'error', '-i', path, '-ac', '1', '-ar', str(SR), '-f', 's16le', '-'], capture_output=True).stdout
    return np.frombuffer(raw, np.int16).astype(np.float32) / 32768


TICK = pcm(os.path.join(HERE, 'sfx', 'tick.wav'))
DING = pcm(os.path.join(HERE, 'sfx', 'ding.wav'))


def ts(x):
    h = int(x // 3600); m = int(x % 3600 // 60); s = x % 60
    return f'{h:02d}:{m:02d}:{s:06.3f}'.replace('.', ',')


def build(id, copy=False):
    d = f'{OUT}/{id}'; p = json.load(open(f'{d}/plan.json'))
    segs = p['segs']; total = sum(s['dur'] for s in segs)
    audio = np.zeros(int(total * SR) + SR, np.float32)
    srt = []; t = 0.0; lst = []
    for s in segs:
        sl = s['slide']; i0 = int(t * SR)
        if s.get('audio'):
            a = pcm(s['audio']); j = i0 + int(0.2 * SR); audio[j:j + len(a)] += a[:len(audio) - j]
            st = t + 0.2; en = min(t + s['dur'], st + s.get('adur', len(a) / SR) + 0.05)
            srt.append(f'{len(srt) + 1}\n{ts(st)} --> {ts(en)}\n{s["sub"]}\n')
        elif s.get('sub'):
            st = t + 0.2; srt.append(f'{len(srt) + 1}\n{ts(st)} --> {ts(t + s["dur"] - 0.1)}\n{s["sub"]}\n')
        if sl.get('tick') or (sl.get('c') is not None and str(sl.get('kind', '')).endswith(('-wait', '-w'))):
            audio[i0:i0 + len(TICK)] += TICK * 0.9
        if sl.get('ding') or (sl.get('c') == 1 and str(sl.get('kind', '')).endswith(('-wait', '-w'))):
            j = i0 + int(0.55 * SR); audio[j:j + len(DING)] += DING
        lst.append(f"file '{s['img']}'\nduration {s['dur']:.4f}")
        t += s['dur']
    lst.append(f"file '{segs[-1]['img']}'")
    open(f'{d}/list.txt', 'w').write('\n'.join(lst) + '\n')
    pk = np.abs(audio).max()
    if pk > 0.98: audio *= 0.98 / pk
    w = wave.open(f'{d}/audio.wav', 'wb'); w.setnchannels(1); w.setsampwidth(2); w.setframerate(SR)
    w.writeframes((audio[:int(total * SR)] * 32767).astype(np.int16).tobytes()); w.close()
    open(f'{d}/{id}.cs.srt', 'w', encoding='utf-8').write('\n'.join(srt))
    col = COL.get(id[0], '#1f4e9c')
    fc = (f"color=c={col}:s=1920x10:r=30[bar];[0:v]fps=30,format=yuv420p[v0];"
          f"[v0][bar]overlay=x='-W+W*t/{total:.3f}':y=H-84-10:shortest=1[v]")
    cmd = ['ffmpeg', '-v', 'error', '-y', '-f', 'concat', '-safe', '0', '-i', f'{d}/list.txt', '-i', f'{d}/audio.wav',
           '-filter_complex', fc,
           '-map', '[v]', '-map', '1:a', '-c:v', 'libx264', '-preset', 'veryfast', '-crf', '20', '-pix_fmt', 'yuv420p',
           '-c:a', 'aac', '-b:a', '160k', '-ac', '2', '-t', f'{total:.3f}', '-movflags', '+faststart', f'{d}/{id}.mp4']
    subprocess.run(cmd, check=True)
    if copy:
        for ext in ('mp4', 'cs.srt'):
            shutil.copy(f'{d}/{id}.{ext}', f'{ROOT}/yt-upload/{id}.{ext}')
    return round(total, 1)


if __name__ == '__main__':
    args = [a for a in sys.argv[1:] if not a.startswith('--')]
    if '--slides' in sys.argv:
        subprocess.run(['node', os.path.join(HERE, 'slides.js')] + args, check=True, env=dict(os.environ, YT_OUT=OUT))
    for id in args:
        print(id, build(id, '--copy' in sys.argv), 's')

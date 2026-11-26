"""Відновлення 4 картинок історії Mluvení 3 з опублікованого уроку vNN.mp4 (для збірок, коли SVG-сцен немає).

python3 tools/yt/extract_panels.py 11 12 13 14 15  -> tools/yt/scenes/vNN_1..4.png (1080x608)
Береться великий кадр зліва в частині «vzor» (x 65–915, y 135–613), номер картинки — за підсвіченою мініатюрою;
старий кружечок з номером зафарбовується фоном праворуч від нього (новий слайд малює свій).
"""
import os, subprocess, sys
import numpy as np
from PIL import Image
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(os.path.dirname(HERE))
TH = [62, 274, 486, 698]   # ліві краї мініатюр


def frames(mp4, t0, t1, step=0.5):
    for t in np.arange(t0, t1, step):
        raw = subprocess.run(['ffmpeg', '-v', 'error', '-ss', f'{t:.2f}', '-i', mp4, '-frames:v', '1', '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-'],
                             capture_output=True).stdout
        if len(raw) == 1920 * 1080 * 3:
            yield np.frombuffer(raw, np.uint8).reshape(1080, 1920, 3)


def srt_start(path, i):
    tc = [l for l in open(path, encoding='utf-8').read().split('\n') if '-->' in l][i].split(' --> ')[0]
    h, m, s = tc.replace(',', '.').split(':'); return int(h) * 3600 + int(m) * 60 + float(s)


def run(n):
    mp4 = f'{ROOT}/yt-upload/v{n:02d}.mp4'; srt = f'{ROOT}/yt-upload/v{n:02d}.cs.srt'
    t0 = srt_start(srt, 2); nb = sum(1 for l in open(srt, encoding='utf-8') if '-->' in l); t1 = srt_start(srt, nb - 1)
    got = {}
    for f in frames(mp4, t0 + 0.3, t1):
        red = [abs(int(f[780, x + 1, 0]) - 194) + abs(int(f[780, x + 1, 1]) - 65) + abs(int(f[780, x + 1, 2]) - 12) for x in TH]
        j = int(np.argmin(red))
        if red[j] > 90 or j in got: continue
        c = f[135:613, 65:915].copy()
        c[12:84, 12:86] = c[12:84, 90:164]      # прибрати старий номер
        got[j] = c
        if len(got) == 4: break
    for j, c in got.items():
        Image.fromarray(c).resize((1080, 608), Image.LANCZOS).save(f'{HERE}/scenes/v{n:02d}_{j + 1}.png')
    return sorted(k + 1 for k in got)


if __name__ == '__main__':
    for a in sys.argv[1:]:
        print(f'v{int(a):02d}', run(int(a)))

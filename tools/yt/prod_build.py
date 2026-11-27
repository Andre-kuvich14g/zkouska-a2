"""Збірка аудіокурсу: python3 tools/yt/prod_build.py m1 ...  (після prod.py)
slides.js -> build.py (MP4 + audio.wav) -> MP4 з розділами, MP3 (-16 LUFS, розділи ID3), zmist.txt"""
import json, os, subprocess, sys
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import build
OUT = os.environ.get('YT_OUT', '/home/claude/yt/out')
NAMES = dict(m1='Mluveni_1', m2='Mluveni_2', m3='Mluveni_3', m4='Mluveni_4', p1='Psani_1', p2='Psani_2')


def hms(t): return f'{int(t // 3600)}:{int(t % 3600 // 60):02d}:{int(t % 60):02d}'


for part in sys.argv[1:]:
    id = f'prod_{part}'; d = f'{OUT}/{id}'
    subprocess.run(['node', os.path.join(HERE, 'slides.js'), id], check=True, env=dict(os.environ, YT_OUT=OUT))
    total = build.build(id)
    P = json.load(open(f'{d}/plan.json')); ch = P['chapters']
    meta = [';FFMETADATA1', f'title=Zkouška A2 do sluchátek · {NAMES[part].replace("_", " ").replace("Mluveni", "Mluvení").replace("Psani", "Psaní")}', 'artist=Zkouška A2 nanečisto']
    for i, (t, name) in enumerate(ch):
        end = ch[i + 1][0] if i + 1 < len(ch) else total
        meta += ['[CHAPTER]', 'TIMEBASE=1/1000', f'START={int(t * 1000)}', f'END={int(end * 1000)}', f'title={name}']
    open(f'{d}/meta.txt', 'w').write('\n'.join(meta) + '\n')
    base = f'Zkouska_A2_do_sluchatek_{NAMES[part]}'
    subprocess.run(['ffmpeg', '-v', 'error', '-y', '-i', f'{d}/{id}.mp4', '-i', f'{d}/meta.txt', '-map_metadata', '1', '-map_chapters', '1', '-c', 'copy', f'{d}/{base}.mp4'], check=True)
    subprocess.run(['ffmpeg', '-v', 'error', '-y', '-i', f'{d}/audio.wav', '-i', f'{d}/meta.txt', '-map_metadata', '1', '-map_chapters', '1',
                    '-af', 'loudnorm=I=-16:TP=-1.5:LRA=11', '-ar', '44100', '-ac', '1', '-b:a', '96k', '-id3v2_version', '3', f'{d}/{base}.mp3'], check=True)
    open(f'{d}/{base}_obsah.txt', 'w', encoding='utf-8').write(
        f'Zkouška A2 do sluchátek · {NAMES[part]} — obsah / зміст\n\n' + '\n'.join(f'{hms(t)}  {n}' for t, n in ch) + '\n')
    print(part, hms(total), os.path.getsize(f'{d}/{base}.mp4') // 2**20, 'MB mp4', os.path.getsize(f'{d}/{base}.mp3') // 2**20, 'MB mp3')

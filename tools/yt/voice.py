"""Голоси ElevenLabs для відео (відновлено 26.11.2026).

Кеш: ключ = sha1(voice|text)[:16] — той самий, що й у learn/audio сайту.
Порядок пошуку: tools/yt/voice/<k>.mp3 (кеш відео, у git) → learn/audio/<k>.mp3 (сайт) → ElevenLabs API
(лише якщо в оточенні є ELEVEN_KEY; ключ ніде не зберігається). Чого немає — потрапляє в MISSING
(тоді кліп тимчасово мовчить, а список зберігається для озвучки).
"""
import hashlib, json, os, subprocess, urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
CACHE = os.path.join(ROOT, 'tools', 'yt', 'voice')
SITE = os.path.join(ROOT, 'learn', 'audio')
EL_M = 'e36pGtHFyzkf4HTb9rQG'   # Daniel – ведучий / кандидат
EL_F = 'vdZa6jplen8RQdIWzOGX'   # Michaela – екзаменаторка
EL_P = 'eqq8WgtBRP5bj6X669PV'   # Petr – друга чоловіча роль
MODEL = 'eleven_multilingual_v2'
MISSING = []
os.makedirs(CACHE, exist_ok=True)


def key(voice, text):
    return hashlib.sha1(f'{voice}|{text}'.encode()).hexdigest()[:16]


def find(voice, text):
    k = key(voice, text)
    for d in (CACHE, SITE, *[x for x in os.environ.get('YT_XCACHE', '').split(':') if x]):
        p = os.path.join(d, k + '.mp3')
        if os.path.exists(p) and os.path.getsize(p) > 500:
            return p
    return None


def fetch(voice, text):
    """Озвучити через API (потрібен ELEVEN_KEY в оточенні)."""
    api = os.environ.get('ELEVEN_KEY')
    if not api:
        return None
    body = json.dumps({'text': text, 'model_id': MODEL,
                       'voice_settings': {'stability': 0.5, 'similarity_boost': 0.75}}).encode()
    req = urllib.request.Request(f'https://api.elevenlabs.io/v1/text-to-speech/{voice}?output_format=mp3_44100_128',
                                 data=body, headers={'xi-api-key': api, 'Content-Type': 'application/json'})
    data = urllib.request.urlopen(req, timeout=120).read()
    p = os.path.join(CACHE, key(voice, text) + '.mp3')
    open(p, 'wb').write(data)
    return p


def dur(path):
    out = subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', path],
                         capture_output=True, text=True).stdout.strip()
    return float(out or 0)


_IDX = None


def reuse(voice, text):
    """YT_REUSE=1: вирізати ту саму фразу з уже опублікованого відео (yt-upload/*.mp4 + .cs.srt).
    Голос не перевіряється — тільки для збірок, де фрази повторюють уроки/попередні збірки."""
    global _IDX
    if os.environ.get('YT_REUSE') != '1': return None
    if _IDX is None:
        import glob, re
        _IDX = {}
        for srt in sorted(glob.glob(os.path.join(ROOT, 'yt-upload', '*.cs.srt'))):
            mp4 = srt[:-7] + '.mp4'
            if not os.path.exists(mp4) or os.path.basename(srt).startswith('s_'): continue
            for b in re.split(r'\n\s*\n', open(srt, encoding='utf-8').read().strip()):
                ln = b.split('\n')
                if len(ln) < 3 or '-->' not in ln[1]: continue
                a, z = [sum(float(x) * m for x, m in zip(t.strip().replace(',', '.').split(':'), (3600, 60, 1))) for t in ln[1].split('-->')]
                _IDX.setdefault(' '.join(ln[2:]).strip(), (mp4, a, z))
    hit = _IDX.get(text)
    if not hit: return None
    mp4, a, z = hit; p = os.path.join(CACHE, key(voice, text) + '.mp3')
    subprocess.run(['ffmpeg', '-v', 'error', '-y', '-ss', f'{a:.3f}', '-t', f'{z - a:.3f}', '-i', mp4, '-vn', '-ac', '1', '-ar', '44100',
                    '-af', 'areverse,silenceremove=start_periods=1:start_threshold=-45dB,areverse',
                    '-b:a', '128k', p], check=True)
    return p


def say(voice, text):
    """-> (mp3 path | None, duration). Якщо озвучки немає — оцінка тривалості 14 символів/с."""
    p = find(voice, text) or reuse(voice, text) or fetch(voice, text)
    if p:
        return p, dur(p)
    if not any(m['k'] == key(voice, text) for m in MISSING):
        MISSING.append(dict(k=key(voice, text), v=voice, t=text))
    return None, max(1.2, len(text) / 14)


def save_missing(path):
    json.dump(MISSING, open(path, 'w'), ensure_ascii=False, indent=0)
    return len(MISSING), sum(len(m['t']) for m in MISSING)

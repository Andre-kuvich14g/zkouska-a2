#!/bin/sh
# Перевірка перед завантаженням відео на YouTube: є mp4, фірмова обкладинка (1280x720, стиль ab2/out3), 5 субтитрів, meta і tr.
id=$1; d=$(dirname "$0")/../yt-upload; ok=1
for f in $id.mp4 $id.jpg $id.cs.srt $id.uk.srt $id.ru.srt $id.en.srt $id.vi.srt; do [ -f "$d/$f" ] || { echo "НЕМАЄ $f"; ok=0; }; done
python3 -c "import json,sys;m=json.load(open('$d/meta.json'));t=json.load(open('$d/tr.json'));sys.exit(0 if '$id' in m and '$id' in t else 1)" || { echo "НЕМАЄ meta/tr для $id"; ok=0; }
[ -f "$d/$id.jpg" ] && python3 -c "from PIL import Image;im=Image.open('$d/$id.jpg');assert im.size==(1280,720),im.size" || ok=0
[ $ok = 1 ] && echo "OK $id: можна завантажувати" || { echo "СТОП: $id не готовий"; exit 1; }

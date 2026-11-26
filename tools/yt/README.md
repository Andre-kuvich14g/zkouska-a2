# Інструменти відео YouTube (відновлено 26.11.2026)

Усе потрібне для щоденних уроків, збірок і Shorts — тут, у git. Тимчасові файли — у `$YT_OUT` (за замовчуванням /home/claude/yt/out).

## День N (f/p/m/d/v/r)
1. Сцени: `days/dayNN.js` (SC — бічна сцена + обкладинка, PN — 4 картинки Mluvení 3, OPT — варіанти Mluvení 4, TH — тексти обкладинок) → `node tools/yt/scenes.js NN`
2. Плани + список відсутніх голосів: `python3 tools/yt/gen.py NN` → `tools/el/miss_dNN.json`
3. Озвучка відсутніх фраз: `ELEVEN_KEY=… python3 tools/yt/gen.py NN` (ключ лише в оточенні, ніде не зберігається) — кліпи падають у `tools/yt/voice/`
4. Відео + чеські субтитри: `python3 tools/yt/build.py --slides --copy f19 p19 …` → `yt-upload/<id>.mp4`, `<id>.cs.srt`
5. Обкладинки: `node tools/yt/thumb.js NN` → `yt-upload/thumb3/<id>.jpg`
6. Назви/описи: `days/dayNN_tr.json` → `python3 tools/yt/meta.py NN YYYY-MM-DD` (meta.json + злиття tr.json)
7. Субтитри uk/ru/en/vi: `days/dayNN_srt.json` → `python3 tools/yt/srt_tr.py days/dayNN_srt.json <ids> --write`
8. Short: `node tools/yt/short.js d19 "V hotelu" "гачок"` → `yt-upload/s_d19.mp4`

## Збірки
- Mluvení 3: `python3 tools/yt/sum_m3.py C` (голоси уроків і повторювані фрази вирізаються з опублікованих відео, YT_REUSE=1;
  картинки історій без SVG — `python3 tools/yt/extract_panels.py 11 12 …`), далі `build.py --slides om3_C`.

## Голоси
`voice.py`: кеш `tools/yt/voice/<sha1(voice|text)[:16]>.mp3` → звуки сайту `learn/audio/` → (YT_REUSE) опубліковані відео → ElevenLabs API.

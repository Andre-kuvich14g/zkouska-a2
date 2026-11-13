"""Субтитри cs/uk/ru/en/vi для om1_N. Переклади питань/відповідей — з уроків m01..m40, нарація — словник нижче."""
import sys, json, re, wave, glob
sys.path.insert(0, '/home/claude/yt')
KEY = sys.argv[1] if len(sys.argv) > 1 else 'om3_1'
D = f'/home/claude/yt/out_pilot/{KEY}'
LANGS = ['uk', 'ru', 'en', 'vi']

def rd(p):
    bl = [b for b in open(p, encoding='utf8').read().strip().split('\n\n') if b.strip()]
    return [' '.join(b.split('\n')[2:]) for b in bl]
TR = {}
for cs in sorted(glob.glob('/home/claude/zkouska-a2/yt-upload/v[0-9][0-9].cs.srt')):
    base = cs[:-7]; c = rd(cs)
    for L in LANGS:
        try: t = rd(f'{base}.{L}.srt')
        except FileNotFoundError: continue
        if len(t) != len(c): continue
        for a, b in zip(c, t): TR.setdefault(a, {})[L] = b


N = {
 'Všech pět příběhů z lekcí jedna až pět – vždy čtyři obrázky a celé vzorové vyprávění v minulém čase. A navíc dvanáct frází, se kterými zvládnete každý příběh, a pět chyb, kvůli kterým lidé ztrácejí body. Připravte se a vyprávějte nahlas!': [
  'Усі п’ять історій з уроків 1–5 — щоразу чотири картинки й повна зразкова розповідь у минулому часі. А ще дванадцять фраз, з якими ви впораєтеся з будь-якою історією, і п’ять помилок, через які люди втрачають бали. Приготуйтеся й розповідайте вголос!',
  'Все пять историй из уроков 1–5 — каждый раз четыре картинки и полный образец рассказа в прошедшем времени. А ещё двенадцать фраз, с которыми вы справитесь с любой историей, и пять ошибок, из-за которых теряют баллы. Приготовьтесь и рассказывайте вслух!',
  'All five stories from lessons 1–5 — four pictures each and a full model story in the past tense. Plus twelve phrases that work for any story and five mistakes that cost people points. Get ready and tell the stories out loud!',
  'Cả năm câu chuyện từ bài 1–5 — mỗi chuyện bốn bức tranh và bài kể mẫu đầy đủ ở thì quá khứ. Thêm mười hai cụm từ dùng cho mọi câu chuyện và năm lỗi khiến mọi người mất điểm. Hãy chuẩn bị và kể thành tiếng!'],
 'Jak úloha tři funguje? Dostanete čtyři obrázky, které dohromady tvoří jeden příběh. Vy vyprávíte, co se stalo – v minulém čase. Za tuto úlohu můžete dostat deset bodů.': [
  'Як працює завдання 3? Ви отримуєте чотири картинки, які разом складають одну історію. Ви розповідаєте, що сталося, — у минулому часі. За це завдання можна отримати десять балів.',
  'Как устроено задание 3? Вы получаете четыре картинки, которые вместе составляют одну историю. Вы рассказываете, что произошло, — в прошедшем времени. За это задание можно получить десять баллов.',
  'How does task 3 work? You get four pictures that together tell one story. You tell what happened — in the past tense. You can get ten points for this task.',
  'Bài 3 diễn ra thế nào? Bạn nhận bốn bức tranh tạo thành một câu chuyện. Bạn kể lại chuyện gì đã xảy ra — ở thì quá khứ. Bài này được tối đa mười điểm.'],
 'Nejdůležitější je minulý čas. Muž: šel, měl, byl. Žena: šla, měla, byla. Více lidí: šli, měli, byli. A když mluvíte o sobě, nezapomeňte jsem: šel jsem, šla jsem. Teď si projdeme všech pět příběhů. Nejdřív vyprávějte sami, pak uslyšíte vzor.': [
  'Найважливіше — минулий час. Чоловік: šel, měl, byl. Жінка: šla, měla, byla. Кілька людей: šli, měli, byli. А коли говорите про себе, не забудьте jsem: šel jsem, šla jsem. Тепер пройдемо всі п’ять історій. Спершу розкажіть самі, потім почуєте зразок.',
  'Самое важное — прошедшее время. Мужчина: šel, měl, byl. Женщина: šla, měla, byla. Несколько людей: šli, měli, byli. А когда говорите о себе, не забудьте jsem: šel jsem, šla jsem. Теперь пройдём все пять историй. Сначала расскажите сами, потом услышите образец.',
  'The most important thing is the past tense. Man: šel, měl, byl. Woman: šla, měla, byla. Several people: šli, měli, byli. And when you talk about yourself, don’t forget jsem: šel jsem, šla jsem. Now we go through all five stories. First tell it yourself, then you hear the model.',
  'Quan trọng nhất là thì quá khứ. Nam: šel, měl, byl. Nữ: šla, měla, byla. Nhiều người: šli, měli, byli. Khi nói về bản thân, đừng quên jsem: šel jsem, šla jsem. Bây giờ chúng ta đi qua cả năm câu chuyện. Hãy tự kể trước, sau đó nghe bài mẫu.'],
 'Příběh jedna: Stěhování.': ['Історія 1: Переїзд.', 'История 1: Переезд.', 'Story 1: Moving house.', 'Câu chuyện 1: Chuyển nhà.'],
 'Příběh dva: Výlet na hory.': ['Історія 2: Поїздка в гори.', 'История 2: Поездка в горы.', 'Story 2: A trip to the mountains.', 'Câu chuyện 2: Chuyến đi lên núi.'],
 'Příběh tři: Nehoda na kole.': ['Історія 3: Аварія на велосипеді.', 'История 3: Авария на велосипеде.', 'Story 3: A bike accident.', 'Câu chuyện 3: Tai nạn xe đạp.'],
 'Příběh čtyři: Ztracená peněženka.': ['Історія 4: Загублений гаманець.', 'История 4: Потерянный кошелёк.', 'Story 4: A lost wallet.', 'Câu chuyện 4: Chiếc ví bị mất.'],
 'Příběh pět: Narozeniny.': ['Історія 5: День народження.', 'История 5: День рождения.', 'Story 5: A birthday.', 'Câu chuyện 5: Sinh nhật.'],
 'Teď dvanáct frází, se kterými zvládnete každý příběh. Poslouchejte a opakujte nahlas.': ['Тепер дванадцять фраз, з якими ви впораєтеся з будь-якою історією. Слухайте й повторюйте вголос.', 'Теперь двенадцать фраз, с которыми вы справитесь с любой историей. Слушайте и повторяйте вслух.', 'Now twelve phrases that work for any story. Listen and repeat out loud.', 'Bây giờ là mười hai cụm từ dùng cho mọi câu chuyện. Hãy nghe và nhắc lại.'],
 'Včera ráno jsem vstal v sedm hodin.': ['Вчора вранці я встав о сьомій.', 'Вчера утром я встал в семь часов.', 'Yesterday morning I got up at seven.', 'Sáng hôm qua tôi dậy lúc bảy giờ.'],
 'Nejdřív jsem se nasnídal.': ['Спочатку я поснідав.', 'Сначала я позавтракал.', 'First I had breakfast.', 'Đầu tiên tôi ăn sáng.'],
 'Potom jsem šel do práce.': ['Потім я пішов на роботу.', 'Потом я пошёл на работу.', 'Then I went to work.', 'Sau đó tôi đi làm.'],
 'Najednou začalo pršet.': ['Раптом почався дощ.', 'Вдруг пошёл дождь.', 'Suddenly it started to rain.', 'Đột nhiên trời đổ mưa.'],
 'Nakonec jsme šli domů.': ['Зрештою ми пішли додому.', 'В конце концов мы пошли домой.', 'In the end we went home.', 'Cuối cùng chúng tôi về nhà.'],
 'Byl unavený, protože hodně pracoval.': ['Він був утомлений, бо багато працював.', 'Он был уставшим, потому что много работал.', 'He was tired because he worked a lot.', 'Anh ấy mệt vì làm việc nhiều.'],
 'Neměli deštník, a proto byli mokří.': ['У них не було парасольки, і тому вони були мокрі.', 'У них не было зонта, и поэтому они были мокрые.', 'They had no umbrella, so they were wet.', 'Họ không có ô, vì vậy họ bị ướt.'],
 'Bylo hezké počasí.': ['Була гарна погода.', 'Была хорошая погода.', 'The weather was nice.', 'Thời tiết đẹp.'],
 'Odpoledne šla na policii.': ['Після обіду вона пішла в поліцію.', 'После обеда она пошла в полицию.', 'In the afternoon she went to the police.', 'Buổi chiều cô ấy đến đồn cảnh sát.'],
 'Marie měla narozeniny.': ['У Марії був день народження.', 'У Марии был день рождения.', 'Marie had a birthday.', 'Marie có sinh nhật.'],
 'Pan Tichý musel zůstat doma.': ['Пан Тіхий мусив залишитися вдома.', 'Пан Тихий должен был остаться дома.', 'Mr Tichý had to stay at home.', 'Ông Tichý phải ở nhà.'],
 'Večer přišli kamarádi.': ['Увечері прийшли друзі.', 'Вечером пришли друзья.', 'In the evening friends came.', 'Buổi tối bạn bè đến.'],
 'Pět typických chyb, kvůli kterým lidé ztrácejí body.': ['П’ять типових помилок, через які люди втрачають бали.', 'Пять типичных ошибок, из-за которых люди теряют баллы.', 'Five typical mistakes that cost people points.', 'Năm lỗi thường gặp khiến mọi người mất điểm.'],
 'Správně: Olga ležela v posteli. Vyprávějte v minulém čase: ležela, šla, koupila.': ['Правильно: Olga ležela v posteli. Розповідайте в минулому часі: ležela, šla, koupila.', 'Правильно: Olga ležela v posteli. Рассказывайте в прошедшем времени: ležela, šla, koupila.', 'Correct: Olga ležela v posteli. Tell the story in the past tense: ležela, šla, koupila.', 'Đúng: Olga ležela v posteli. Hãy kể ở thì quá khứ: ležela, šla, koupila.'],
 'Správně: Marie pekla dort. Žena: -la. Muž: -l. Více lidí: -li.': ['Правильно: Marie pekla dort. Жінка: -la. Чоловік: -l. Кілька людей: -li.', 'Правильно: Marie pekla dort. Женщина: -la. Мужчина: -l. Несколько людей: -li.', 'Correct: Marie pekla dort. Woman: -la. Man: -l. Several people: -li.', 'Đúng: Marie pekla dort. Nữ: -la. Nam: -l. Nhiều người: -li.'],
 'Správně: Včera jsem šel do práce. Když mluvíte o sobě, nezapomeňte jsem.': ['Правильно: Včera jsem šel do práce. Коли говорите про себе, не забудьте jsem.', 'Правильно: Včera jsem šel do práce. Когда говорите о себе, не забудьте jsem.', 'Correct: Včera jsem šel do práce. When you talk about yourself, don’t forget jsem.', 'Đúng: Včera jsem šel do práce. Khi nói về bản thân, đừng quên jsem.'],
 'Správně: Ráno balili věci a potom přijelo auto. Nepopisujte obrázky. Vyprávějte příběh se spojkami: nejdřív, potom, nakonec.': ['Правильно: Ráno balili věci a potom přijelo auto. Не описуйте картинки. Розповідайте історію зі сполучниками: nejdřív, potom, nakonec.', 'Правильно: Ráno balili věci a potom přijelo auto. Не описывайте картинки. Рассказывайте историю с союзами: nejdřív, potom, nakonec.', 'Correct: Ráno balili věci a potom přijelo auto. Don’t describe the pictures. Tell a story with linking words: nejdřív, potom, nakonec.', 'Đúng: Ráno balili věci a potom přijelo auto. Đừng mô tả tranh. Hãy kể chuyện với từ nối: nejdřív, potom, nakonec.'],
 'Správně: Jel na kole do práce. Najednou vyběhl pes a on spadl. Ke každému obrázku řekněte dvě až tři věty: kdo, kde, co a proč.': ['Правильно: Jel na kole do práce. Najednou vyběhl pes a on spadl. До кожної картинки скажіть два-три речення: хто, де, що і чому.', 'Правильно: Jel na kole do práce. Najednou vyběhl pes a on spadl. К каждой картинке скажите два-три предложения: кто, где, что и почему.', 'Correct: Jel na kole do práce. Najednou vyběhl pes a on spadl. Say two or three sentences for each picture: who, where, what and why.', 'Đúng: Jel na kole do práce. Najednou vyběhl pes a on spadl. Mỗi bức tranh hãy nói hai đến ba câu: ai, ở đâu, làm gì và tại sao.'],
 'Shrnutí. Za prvé: vyprávějte v minulém čase. Za druhé: spojujte věty – nejdřív, potom, nakonec. Za třetí: ke každému obrázku řekněte dvě až tři věty. A za čtvrté: pozor na rod – on šel, ona šla.': ['Підсумок. Перше: розповідайте в минулому часі. Друге: з’єднуйте речення — nejdřív, potom, nakonec. Третє: до кожної картинки два-три речення. І четверте: увага на рід — on šel, ona šla.', 'Итог. Первое: рассказывайте в прошедшем времени. Второе: связывайте предложения — nejdřív, potom, nakonec. Третье: к каждой картинке два-три предложения. И четвёртое: внимание на род — on šel, ona šla.', 'Summary. First: tell the story in the past tense. Second: link your sentences — nejdřív, potom, nakonec. Third: two or three sentences for each picture. And fourth: watch the gender — on šel, ona šla.', 'Tóm tắt. Thứ nhất: kể ở thì quá khứ. Thứ hai: nối câu — nejdřív, potom, nakonec. Thứ ba: mỗi tranh hai đến ba câu. Và thứ tư: chú ý giống — on šel, ona šla.'],
 'Který příběh je pro vás nejtěžší? Napište to do komentáře – a zkuste tam napsat první dvě věty v minulém čase. A pokud vám video pomohlo, dejte like.': ['Яка історія для вас найважча? Напишіть у коментарях — і спробуйте написати там перші два речення в минулому часі. А якщо відео допомогло, поставте лайк.', 'Какая история для вас самая трудная? Напишите в комментариях — и попробуйте написать там первые два предложения в прошедшем времени. А если видео помогло, поставьте лайк.', 'Which story is the hardest for you? Write it in the comments — and try to write the first two sentences in the past tense. And if the video helped, give it a like.', 'Câu chuyện nào khó nhất với bạn? Hãy viết vào bình luận — và thử viết hai câu đầu ở thì quá khứ. Nếu video có ích, hãy bấm thích.'],
 'Na webu Zkouška A2 nanečisto si můžete všechny příběhy procvičit zdarma – web vás poslouchá a kontroluje minulý čas. Odkaz je v popisu. Zítra: velké opakování Mluvení, úloha čtyři. Odebírejte kanál, ať vám nic neuteče.': ['На сайті Zkouška A2 nanečisto можна безкоштовно потренувати всі історії — сайт слухає вас і перевіряє минулий час. Посилання в описі. Завтра: велике повторення Mluvení, завдання 4. Підписуйтеся на канал, щоб нічого не пропустити.', 'На сайте Zkouška A2 nanečisto можно бесплатно потренировать все истории — сайт слушает вас и проверяет прошедшее время. Ссылка в описании. Завтра: большое повторение Mluvení, задание 4. Подписывайтесь на канал.', 'On the Zkouška A2 nanečisto website you can practise all stories for free — it listens and checks your past tense. Link in the description. Tomorrow: big review of Speaking task 4. Subscribe so you don’t miss anything.', 'Trên trang Zkouška A2 nanečisto bạn có thể luyện tất cả câu chuyện miễn phí — trang web nghe và kiểm tra thì quá khứ. Liên kết trong mô tả. Ngày mai: ôn tập lớn phần Nói, bài 4. Hãy đăng ký kênh.'],
}
for k, v in N.items(): TR[k] = dict(zip(LANGS, v))

p = json.load(open(f'{D}/plan.json'))
def ts(x):
    h = int(x // 3600); m = int(x % 3600 // 60); s = x % 60
    return f'{h:02d}:{m:02d}:{s:06.3f}'.replace('.', ',')
cues = []; t = 0.0
for s in p['segs']:
    if s['sub']:
        w = wave.open(s['audio']); d = w.getnframes() / w.getframerate(); w.close()
        cues.append((t + 0.2, min(t + s['dur'], t + 0.2 + d + 0.3), s['sub']))
    t += s['dur']
miss = sorted({c for _, _, c in cues if c not in TR or len(TR[c]) < 4})
print('missing', miss)
for L in ['cs'] + LANGS:
    out = []
    for i, (a, b, c) in enumerate(cues, 1):
        txt = c if L == 'cs' else TR.get(c, {}).get(L, c)
        out.append(f'{i}\n{ts(a)} --> {ts(b)}\n{txt}\n')
    open(f'{D}/{KEY}.{L}.srt', 'w', encoding='utf8').write('\n'.join(out))
ch = p['chapters']
print('\n'.join(f'{int(a // 60)}:{int(a % 60):02d} {c}' for a, c in ch), round(t))

"""Субтитри cs/uk/ru/en/vi для om1_N. Переклади питань/відповідей — з уроків m01..m40, нарація — словник нижче."""
import sys, json, re, wave, glob
sys.path.insert(0, '/home/claude/yt')
KEY = sys.argv[1] if len(sys.argv) > 1 else 'om4_1'
D = f'/home/claude/yt/out_pilot/{KEY}'
LANGS = ['uk', 'ru', 'en', 'vi']

def rd(p):
    bl = [b for b in open(p, encoding='utf8').read().strip().split('\n\n') if b.strip()]
    return [' '.join(b.split('\n')[2:]) for b in bl]
TR = {}
for cs in sorted(glob.glob('/home/claude/zkouska-a2/yt-upload/r[0-9][0-9].cs.srt')):
    base = cs[:-7]; c = rd(cs)
    for L in LANGS:
        try: t = rd(f'{base}.{L}.srt')
        except FileNotFoundError: continue
        if len(t) != len(c): continue
        for a, b in zip(c, t): TR.setdefault(a, {})[L] = b


N = {
 'Všech pět situací z lekcí jedna až pět – vždy tři možnosti a celý vzorový dialog se zkoušející. A navíc dvanáct frází, se kterými se domluvíte v každé situaci, a pět chyb, kvůli kterým lidé ztrácejí body. Připravte se a mluvte nahlas!': [
  'Усі п’ять ситуацій з уроків 1–5 — щоразу три варіанти й повний зразковий діалог з екзаменаторкою. А ще дванадцять фраз, з якими ви домовитеся в будь-якій ситуації, і п’ять помилок, через які втрачають бали. Готуйтеся й говоріть уголос!',
  'Все пять ситуаций из уроков 1–5 — каждый раз три варианта и полный образец диалога с экзаменатором. А ещё двенадцать фраз, с которыми вы договоритесь в любой ситуации, и пять ошибок, из-за которых теряют баллы. Готовьтесь и говорите вслух!',
  'All five situations from lessons 1–5 — three options each and a full model dialogue with the examiner. Plus twelve phrases to reach agreement in any situation and five mistakes that cost people points. Get ready and speak out loud!',
  'Cả năm tình huống từ bài 1–5 — mỗi tình huống ba phương án và hội thoại mẫu đầy đủ với giám khảo. Thêm mười hai cụm từ để thỏa thuận trong mọi tình huống và năm lỗi khiến mọi người mất điểm. Hãy chuẩn bị và nói thành tiếng!'],
 'Jak úloha čtyři funguje? Zkoušející vám řekne situaci a ukáže tři možnosti. Vy navrhnete jednu. Ona většinou řekne, že se jí to nelíbí – a vy navrhnete jinou. Nakonec se dohodnete a řeknete proč. Za tuto úlohu můžete dostat sedm bodů.': [
  'Як працює завдання 4? Екзаменаторка описує ситуацію й показує три варіанти. Ви пропонуєте один. Вона зазвичай каже, що їй це не подобається, — і ви пропонуєте інший. Наприкінці ви домовляєтеся й кажете чому. За це завдання можна отримати сім балів.',
  'Как устроено задание 4? Экзаменатор описывает ситуацию и показывает три варианта. Вы предлагаете один. Она обычно говорит, что ей это не нравится, — и вы предлагаете другой. В конце вы договариваетесь и говорите почему. За это задание можно получить семь баллов.',
  'How does task 4 work? The examiner describes a situation and shows three options. You suggest one. She usually says she doesn’t like it — and you suggest another. In the end you agree and say why. You can get seven points for this task.',
  'Bài 4 diễn ra thế nào? Giám khảo nêu tình huống và đưa ra ba phương án. Bạn đề xuất một. Cô ấy thường nói không thích — và bạn đề xuất phương án khác. Cuối cùng hai người thống nhất và bạn nói lý do. Bài này được tối đa bảy điểm.'],
 'Dialog má jednoduchý plán. Navrhnete jednu možnost. Zkoušející řekne, proč ne. Vy klidně navrhnete jinou možnost. A když se zeptá proč, odpovíte: protože. Teď si projdeme všech pět situací. Nejdřív mluvte sami, pak uslyšíte vzor.': [
  'Діалог має простий план. Ви пропонуєте один варіант. Екзаменаторка каже, чому ні. Ви спокійно пропонуєте інший. А коли вона спитає чому, відповідаєте: protože. Тепер пройдемо всі п’ять ситуацій. Спочатку говоріть самі, потім почуєте зразок.',
  'У диалога простой план. Вы предлагаете один вариант. Экзаменатор говорит, почему нет. Вы спокойно предлагаете другой. А когда она спросит почему, отвечаете: protože. Теперь пройдём все пять ситуаций. Сначала говорите сами, потом услышите образец.',
  'The dialogue has a simple plan. You suggest one option. The examiner says why not. You calmly suggest another. And when she asks why, you answer: protože. Now let’s go through all five situations. Speak yourself first, then you hear the model.',
  'Hội thoại có kế hoạch đơn giản. Bạn đề xuất một phương án. Giám khảo nói vì sao không. Bạn bình tĩnh đề xuất phương án khác. Khi cô hỏi tại sao, bạn trả lời: protože. Bây giờ đi qua cả năm tình huống. Hãy tự nói trước, sau đó nghe mẫu.'],
 'Situace jedna: Kamarádka bude mít narozeniny.': ['Ситуація 1: У подруги буде день народження.', 'Ситуация 1: У подруги будет день рождения.', 'Situation 1: A friend’s birthday is coming.', 'Tình huống 1: Sắp sinh nhật bạn gái.'],
 'Situace dva: V sobotu večer chceme jít spolu ven.': ['Ситуація 2: У суботу ввечері хочемо кудись піти разом.', 'Ситуация 2: В субботу вечером хотим куда-то пойти вместе.', 'Situation 2: Going out together on Saturday night.', 'Tình huống 2: Tối thứ Bảy muốn đi chơi cùng nhau.'],
 'Situace tři: V létě chceme spolu jet na dovolenou.': ['Ситуація 3: Улітку хочемо разом поїхати у відпустку.', 'Ситуация 3: Летом хотим вместе поехать в отпуск.', 'Situation 3: A summer holiday together.', 'Tình huống 3: Mùa hè muốn đi nghỉ cùng nhau.'],
 'Situace čtyři: V sobotu k nám přijdou kamarádi.': ['Ситуація 4: У суботу до нас прийдуть друзі.', 'Ситуация 4: В субботу к нам придут друзья.', 'Situation 4: Friends are coming on Saturday.', 'Tình huống 4: Thứ Bảy bạn bè đến nhà.'],
 'Situace pět: Chceme spolu začít sportovat.': ['Ситуація 5: Хочемо разом почати займатися спортом.', 'Ситуация 5: Хотим вместе начать заниматься спортом.', 'Situation 5: Starting a sport together.', 'Tình huống 5: Muốn cùng nhau bắt đầu chơi thể thao.'],
 'Teď dvanáct frází, se kterými se domluvíte v každé situaci. Poslouchejte a opakujte nahlas.': ['Тепер дванадцять фраз, з якими ви домовитеся в будь-якій ситуації. Слухайте й повторюйте вголос.', 'Теперь двенадцать фраз, с которыми вы договоритесь в любой ситуации. Слушайте и повторяйте вслух.', 'Now twelve phrases to reach agreement in any situation. Listen and repeat out loud.', 'Bây giờ là mười hai cụm từ để thỏa thuận trong mọi tình huống. Hãy nghe và nhắc lại thành tiếng.'],
 'Můžeme jít do kina.': ['Можемо піти в кіно.', 'Можем пойти в кино.', 'We could go to the cinema.', 'Chúng ta có thể đi xem phim.'],
 'Co kdybychom jeli na hory?': ['А що, якби ми поїхали в гори?', 'А что, если бы мы поехали в горы?', 'What if we went to the mountains?', 'Hay là chúng ta đi lên núi?'],
 'A co třeba pizza?': ['А як щодо піци?', 'А как насчёт пиццы?', 'How about pizza?', 'Còn pizza thì sao?'],
 'Tak půjdeme do restaurace.': ['Тоді підемо в ресторан.', 'Тогда пойдём в ресторан.', 'Then let’s go to a restaurant.', 'Vậy chúng ta đi nhà hàng.'],
 'Dobře, tak uvaříme guláš.': ['Добре, тоді зваримо гуляш.', 'Хорошо, тогда сварим гуляш.', 'OK, then we’ll cook goulash.', 'Được, vậy nấu goulash.'],
 'Máš pravdu, divadlo je drahé.': ['Маєш рацію, театр дорогий.', 'Ты прав, театр дорогой.', 'You’re right, the theatre is expensive.', 'Bạn nói đúng, nhà hát đắt.'],
 'To je škoda, ale nevadí.': ['Шкода, але нічого.', 'Жаль, но ничего.', 'That’s a pity, but never mind.', 'Tiếc thật, nhưng không sao.'],
 'Já bych radši jel k moři.': ['Я б краще поїхав на море.', 'Я бы лучше поехал на море.', 'I’d rather go to the seaside.', 'Tôi thích đi biển hơn.'],
 'Protože plavání je zdravé.': ['Бо плавання корисне для здоров’я.', 'Потому что плавание полезно для здоровья.', 'Because swimming is healthy.', 'Vì bơi lội tốt cho sức khỏe.'],
 'Kino je levné a je blízko.': ['Кіно дешеве й близько.', 'Кино дешёвое и близко.', 'The cinema is cheap and close.', 'Rạp phim rẻ và gần.'],
 'Souhlasím, to je dobrý nápad.': ['Погоджуюся, це гарна ідея.', 'Согласен, это хорошая идея.', 'I agree, that’s a good idea.', 'Tôi đồng ý, ý hay đấy.'],
 'Bude to legrace.': ['Буде весело.', 'Будет весело.', 'It’ll be fun.', 'Sẽ vui lắm.'],
 'Pět typických chyb, kvůli kterým lidé ztrácejí body.': ['П’ять типових помилок, через які люди втрачають бали.', 'Пять типичных ошибок, из-за которых люди теряют баллы.', 'Five typical mistakes that cost people points.', 'Năm lỗi thường gặp khiến mọi người mất điểm.'],
 'Správně: Co kdybychom šli do kina? Navrhujte celou větou: Můžeme…, Co kdybychom…': ['Правильно: Co kdybychom šli do kina? Пропонуйте цілим реченням: Můžeme…, Co kdybychom…', 'Правильно: Co kdybychom šli do kina? Предлагайте целым предложением: Můžeme…, Co kdybychom…', 'Correct: Co kdybychom šli do kina? Make suggestions in full sentences: Můžeme…, Co kdybychom…', 'Đúng: Co kdybychom šli do kina? Hãy đề xuất bằng câu đầy đủ: Můžeme…, Co kdybychom…'],
 'Správně: Dobře, tak půjdeme do divadla. Když zkoušející nesouhlasí, navrhněte jinou možnost.': ['Правильно: Dobře, tak půjdeme do divadla. Коли екзаменаторка не погоджується, запропонуйте інший варіант.', 'Правильно: Dobře, tak půjdeme do divadla. Когда экзаменатор не согласен, предложите другой вариант.', 'Correct: Dobře, tak půjdeme do divadla. When the examiner disagrees, suggest another option.', 'Đúng: Dobře, tak půjdeme do divadla. Khi giám khảo không đồng ý, hãy đề xuất phương án khác.'],
 'Správně: Protože plavání je zdravé a bazén je blízko. Na konci řekněte konkrétní důvod: protože…': ['Правильно: Protože plavání je zdravé a bazén je blízko. Наприкінці назвіть конкретну причину: protože…', 'Правильно: Protože plavání je zdravé a bazén je blízko. В конце назовите конкретную причину: protože…', 'Correct: Protože plavání je zdravé a bazén je blízko. At the end give a concrete reason: protože…', 'Đúng: Protože plavání je zdravé a bazén je blízko. Cuối cùng hãy nêu lý do cụ thể: protože…'],
 'Správně: Chceš jet na hory? V úloze 4 mluvíte s kamarádkou: tykejte – máš, chceš, můžeš.': ['Правильно: Chceš jet na hory? У завданні 4 ви говорите з подругою: на «ти» — máš, chceš, můžeš.', 'Правильно: Chceš jet na hory? В задании 4 вы говорите с подругой: на «ты» — máš, chceš, můžeš.', 'Correct: Chceš jet na hory? In task 4 you talk to a friend: use the informal “ty” — máš, chceš, můžeš.', 'Đúng: Chceš jet na hory? Ở bài 4 bạn nói với bạn bè: xưng «ty» — máš, chceš, můžeš.'],
 'Správně: Půjdeme do kina. Po do je 2. pád: do kina, do divadla, do restaurace.': ['Правильно: Půjdeme do kina. Після do — родовий відмінок: do kina, do divadla, do restaurace.', 'Правильно: Půjdeme do kina. После do — родительный падеж: do kina, do divadla, do restaurace.', 'Correct: Půjdeme do kina. After do use the genitive: do kina, do divadla, do restaurace.', 'Đúng: Půjdeme do kina. Sau do dùng cách 2: do kina, do divadla, do restaurace.'],
 'Shrnutí. Za prvé: navrhujte celou větou. Za druhé: když zkoušející nesouhlasí, navrhněte jinou možnost. Za třetí: na konci řekněte důvod – protože. A za čtvrté: s kamarádkou si tykáte.': ['Підсумок. Перше: пропонуйте цілим реченням. Друге: коли екзаменаторка не погоджується, пропонуйте інший варіант. Третє: наприкінці скажіть причину — protože. І четверте: з подругою ви на «ти».', 'Итог. Первое: предлагайте целым предложением. Второе: когда экзаменатор не согласен, предлагайте другой вариант. Третье: в конце скажите причину — protože. И четвёртое: с подругой вы на «ты».', 'Summary. First: make suggestions in full sentences. Second: when the examiner disagrees, suggest another option. Third: at the end give a reason — protože. And fourth: with a friend you use “ty”.', 'Tóm tắt. Thứ nhất: đề xuất bằng câu đầy đủ. Thứ hai: khi giám khảo không đồng ý, hãy đề xuất phương án khác. Thứ ba: cuối cùng nêu lý do — protože. Và thứ tư: với bạn bè thì xưng «ty».'],
 'A co vy? Kam byste jeli na dovolenou – k moři, na hory, nebo do města? Napište to do komentáře celou větou a řekněte proč. A pokud vám video pomohlo, dejte like.': ['А ви? Куди б ви поїхали у відпустку — на море, в гори чи до міста? Напишіть у коментарях цілим реченням і скажіть чому. А якщо відео допомогло, поставте лайк.', 'А вы? Куда бы вы поехали в отпуск — на море, в горы или в город? Напишите в комментариях целым предложением и скажите почему. А если видео помогло, поставьте лайк.', 'And you? Where would you go on holiday — the seaside, the mountains or a city? Write it in the comments as a full sentence and say why. And if the video helped, give it a like.', 'Còn bạn? Bạn sẽ đi nghỉ ở đâu — biển, núi hay thành phố? Hãy viết câu đầy đủ vào bình luận và nói lý do. Nếu video có ích, hãy bấm thích.'],
 'Na webu Zkouška A2 nanečisto si můžete všechny situace procvičit zdarma – web hraje roli zkoušející. Odkaz je v popisu. Zítra: velké opakování Psaní, formulář i e-mail. Odebírejte kanál, ať vám nic neuteče.': ['На сайті Zkouška A2 nanečisto можна безкоштовно потренувати всі ситуації — сайт грає роль екзаменаторки. Посилання в описі. Завтра: велике повторення Psaní — формуляр і e-mail. Підписуйтеся на канал, щоб нічого не пропустити.', 'На сайте Zkouška A2 nanečisto можно бесплатно потренировать все ситуации — сайт играет роль экзаменатора. Ссылка в описании. Завтра: большое повторение Psaní — формуляр и e-mail. Подписывайтесь на канал.', 'On the Zkouška A2 nanečisto website you can practise all situations for free — the site plays the examiner. Link in the description. Tomorrow: big review of Writing — the form and the e-mail. Subscribe so you don’t miss anything.', 'Trên trang Zkouška A2 nanečisto bạn có thể luyện tất cả tình huống miễn phí — trang web đóng vai giám khảo. Liên kết trong mô tả. Ngày mai: ôn tập lớn phần Viết — mẫu đơn và e-mail. Hãy đăng ký kênh.'],
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

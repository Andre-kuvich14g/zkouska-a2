# Úloha 3: 20 příběhů z variant (data-variants.json) + 20 nových
import json, os
from u3_new import NEW3
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(os.path.dirname(HERE))
TR = {
 "Stěhování": ["Переїзд", "Moving house", "Переезд", "Chuyển nhà"],
 "Výlet na hory": ["Поїздка в гори", "A trip to the mountains", "Поездка в горы", "Chuyến đi lên núi"],
 "Nehoda na kole": ["Аварія на велосипеді", "A bike accident", "Авария на велосипеде", "Tai nạn xe đạp"],
 "Ztracená peněženka": ["Загублений гаманець", "A lost wallet", "Потерянный кошелёк", "Chiếc ví bị mất"],
 "Narozeniny": ["День народження", "A birthday", "День рождения", "Sinh nhật"],
 "Ztracený klíč": ["Загублений ключ", "A lost key", "Потерянный ключ", "Chiếc chìa khóa bị mất"],
 "U lékaře": ["У лікаря", "At the doctor's", "У врача", "Ở chỗ bác sĩ"],
 "Pracovní den": ["Робочий день", "A working day", "Рабочий день", "Một ngày làm việc"],
 "Na úřadě": ["В установі", "At the office", "В учреждении", "Ở cơ quan"],
 "Vánoce": ["Різдво", "Christmas", "Рождество", "Giáng sinh"],
 "Nehoda na parkovišti": ["ДТП на парковці", "An accident in a car park", "ДТП на парковке", "Va chạm ở bãi đỗ xe"],
 "Záchranka": ["Швидка допомога", "The ambulance", "Скорая помощь", "Xe cấp cứu"],
 "Nový byt": ["Нова квартира", "A new flat", "Новая квартира", "Căn hộ mới"],
 "Zkouška z češtiny": ["Іспит з чеської", "The Czech exam", "Экзамен по чешскому", "Kỳ thi tiếng Séc"],
 "Oprava kola": ["Ремонт велосипеда", "Fixing a bike", "Ремонт велосипеда", "Sửa xe đạp"],
 "Voda v koupelně": ["Вода у ванній", "Water in the bathroom", "Вода в ванной", "Nước trong phòng tắm"],
 "Návštěva babičky": ["У гостях у бабусі", "Visiting grandma", "В гостях у бабушки", "Thăm bà"],
 "Stěhování do Česka": ["Переїзд до Чехії", "Moving to Czechia", "Переезд в Чехию", "Chuyển đến Séc"],
 "Policejní kontrola": ["Поліцейська перевірка", "A police check", "Полицейская проверка", "Cảnh sát kiểm tra"],
 "Den zkoušky": ["День іспиту", "Exam day", "День экзамена", "Ngày thi"],
}
d = json.load(open(os.path.join(ROOT, 'data-variants.json'), encoding='utf-8'))
OLD = []
for v in d['variants']:
    s = dict(v['speaking']['t3']); s['t'] = TR.get(s['title'], [s['title']] * 4); OLD.append(s)
U3 = OLD + NEW3

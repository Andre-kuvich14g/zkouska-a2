from theory import THEORY
THEORY['w1'] = {}; THEORY['w2'] = {}

THEORY['w1']['uk'] = {
'how': '''
<p>Ви заповнюєте короткий <b>формуляр</b> (анкету, заявку) і відповідаєте на <b>3 питання</b>. На кожне — <b>цілим реченням, мінімум 10 слів</b>. Завдання дає <b>8 балів</b>, на весь Psaní є 25 хвилин.</p>
<ul>
<li>З квітня 2026 це не «ім'я, адреса, дата», а справжні питання: <span class="cz">Proč se hlásíte do kurzu? Kde nejčastěji mluvíte česky?</span></li>
<li>Оцінюють: чи ви відповіли саме на питання, чи є 10 слів, чи речення зрозуміле і граматично правильне.</li>
<li>Відповідь менше 10 слів втрачає бали, навіть якщо вона правильна.</li>
</ul>''',
'grammar': '''
<h4>Формула: питання → відповідь</h4>
<p class="formula">Дієслово з питання <span>+</span> відповідь <span>+</span> деталь або <span class="cz">protože…</span></p>
<div class="tblw"><table class="tbl">
<tr><th>Питання</th><th>Початок відповіді</th></tr>
<tr><td><span class="cz">Proč chcete…?</span></td><td><span class="cz">Chci…, protože…</span></td></tr>
<tr><td><span class="cz">Kdy máte čas?</span></td><td><span class="cz">Čas mám v pondělí a ve středu od…</span></td></tr>
<tr><td><span class="cz">Jak jste se učil/a česky?</span></td><td><span class="cz">Česky jsem se učil/a v kurzu a…</span></td></tr>
<tr><td><span class="cz">Kde nejčastěji…?</span></td><td><span class="cz">Nejčastěji… v práci a v obchodě.</span></td></tr>
<tr><td><span class="cz">S kým…?</span></td><td><span class="cz">…s manželem a se synem.</span></td></tr>
<tr><td><span class="cz">Co byste chtěl/a…?</span></td><td><span class="cz">Chtěl/a bych…</span></td></tr>
</table></div>
<h4>Як «дотягнути» до 10 слів</h4>
<p>Коротко: <span class="cz">Mám čas večer.</span> (3 слова) → Добре: <span class="cz">Na cvičení mám čas hlavně večer po práci, od šesti hodin.</span> (10 слів)</p>
<p>Додайте <b>коли</b> (<span class="cz">v pondělí, ráno, od šesti</span>), <b>де</b> (<span class="cz">v práci, doma, v parku</span>), <b>з ким</b> (<span class="cz">s rodinou</span>) або <b>чому</b> (<span class="cz">protože…</span>).</p>
<h4>Корисні з'єднання</h4>
<p><span class="cz">a</span> · <span class="cz">ale</span> · <span class="cz">protože</span> · <span class="cz">také</span> · <span class="cz">hlavně</span> · <span class="cz">nejčastěji</span> · <span class="cz">většinou</span> · <span class="cz">někdy</span></p>''',
'tips': '''
<ul>
<li><b>Рахуйте слова</b> одразу після кожної відповіді. Краще 12–15 слів, ніж рівно 10.</li>
<li><b>Не повторюйте питання дослівно</b> замість відповіді: беріть з нього лише дієслово.</li>
<li><b>Пишіть прості речення</b>, які точно знаєте. Довге речення з помилками гірше.</li>
<li><b>Перевірте háčky й čárky</b> і велику літеру на початку речення.</li>
<li>Відповідь не мусить бути правдою, головне — правильна й зрозуміла.</li>
</ul>''',
}
THEORY['w2']['uk'] = {
'how': '''
<p>Ви пишете <b>e-mail</b> за ситуацією, наприклад <span class="cz">Chcete pozvat sousedy na grilování.</span> На картинках <b>5 питань</b> (<span class="cz">KDY TO BUDE? KDE TO BUDE?…</span>), і на <b>кожне</b> треба відповісти хоча б одним реченням. <b>Мінімум 35 слів, інакше 0 балів.</b> Завдання дає <b>12 балів</b>.</p>
<ul>
<li>Оцінюють: чи є відповідь на всі 5 картинок, чи лист має звертання, мету й прощання, чи зрозуміла граматика.</li>
<li>Добрий лист має 45–60 слів: так ви точно не впадете нижче 35.</li>
<li>Пишіть до того адресата, який є в завданні: до фірми офіційно, до друга неформально.</li>
</ul>''',
'grammar': '''
<h4>Каркас листа</h4>
<div class="tblw"><table class="tbl">
<tr><th>Частина</th><th>Офіційно (фірма, школа, лікар)</th><th>Неформально (друг, сусід, колега)</th></tr>
<tr><td>Звертання</td><td><span class="cz">Dobrý den,</span> · <span class="cz">Vážená paní Nováková,</span></td><td><span class="cz">Ahoj Petře,</span> · <span class="cz">Milá Jano,</span></td></tr>
<tr><td>Мета</td><td><span class="cz">Píšu vám, protože…</span> · <span class="cz">Chtěl/a bych…</span></td><td><span class="cz">Píšu ti, protože…</span> · <span class="cz">Chci tě pozvat…</span></td></tr>
<tr><td>5 картинок</td><td colspan="2">по одному реченню на кожну картинку, по черзі</td></tr>
<tr><td>Кінець</td><td><span class="cz">Děkuji za odpověď.</span> · <span class="cz">S pozdravem</span></td><td><span class="cz">Těším se.</span> · <span class="cz">Měj se</span> · <span class="cz">Ahoj</span></td></tr>
<tr><td>Підпис</td><td colspan="2">ім'я (і прізвище в офіційному листі)</td></tr>
</table></div>
<h4>Звертання: 5-й відмінок (vokativ)</h4>
<p><span class="cz">Petr → Petře</span> · <span class="cz">Tomáš → Tomáši</span> · <span class="cz">Pavel → Pavle</span> · <span class="cz">Jana → Jano</span> · <span class="cz">Eva → Evo</span> · <span class="cz">paní Nováková → paní Nováková</span> (не змінюється)</p>
<h4>Дати й час</h4>
<p><span class="cz">v sobotu</span> · <span class="cz">v sobotu 12. června</span> · <span class="cz">v 18 hodin</span> · <span class="cz">od 10 do 12</span> · <span class="cz">příští týden</span> · <span class="cz">do středy</span> (до середи)</p>
<h4>Готові фрази</h4>
<p><span class="cz">Chtěl/a bych se zeptat, …</span> · <span class="cz">Můžete mi prosím napsat, …?</span> · <span class="cz">Prosím o odpověď do pátku.</span> · <span class="cz">Bohužel nemůžu přijít, protože…</span> · <span class="cz">Moc děkuju za…</span></p>''',
'tips': '''
<ul>
<li><b>Спершу план</b>: випишіть 5 коротких відповідей на картинки, потім зробіть з них речення.</li>
<li><b>Відповідайте по порядку картинок</b>: так легко перевірити, що нічого не пропущено.</li>
<li><b>Порахуйте слова</b> в кінці. Менше 35 — це 0 балів за весь лист.</li>
<li><b>Не забудьте підпис</b> і прощання: це частина оцінки.</li>
<li><b>«Ви» чи «ти»?</b> Фірма, школа, лікар — <span class="cz">vám, můžete</span>. Друг, сусід — <span class="cz">ti, můžeš</span>. Не змішуйте в одному листі.</li>
</ul>''',
}

THEORY['w1']['en'] = {
'how': '''
<p>You fill in a short <b>form</b> (questionnaire, application) and answer <b>3 questions</b>. Each answer must be a <b>full sentence of at least 10 words</b>. The task is worth <b>8 points</b>; the whole Psaní part has 25 minutes.</p>
<ul>
<li>Since April 2026 it is not “name, address, date” but real questions: <span class="cz">Proč se hlásíte do kurzu? Kde nejčastěji mluvíte česky?</span></li>
<li>They assess whether you answered the actual question, whether there are 10 words and whether the sentence is clear and correct.</li>
<li>An answer with fewer than 10 words loses points even if it is correct.</li>
</ul>''',
'grammar': '''
<h4>The formula: question → answer</h4>
<p class="formula">The verb from the question <span>+</span> the answer <span>+</span> a detail or <span class="cz">protože…</span></p>
<div class="tblw"><table class="tbl">
<tr><th>Question</th><th>The answer starts</th></tr>
<tr><td><span class="cz">Proč chcete…?</span></td><td><span class="cz">Chci…, protože…</span></td></tr>
<tr><td><span class="cz">Kdy máte čas?</span></td><td><span class="cz">Čas mám v pondělí a ve středu od…</span></td></tr>
<tr><td><span class="cz">Jak jste se učil/a česky?</span></td><td><span class="cz">Česky jsem se učil/a v kurzu a…</span></td></tr>
<tr><td><span class="cz">Kde nejčastěji…?</span></td><td><span class="cz">Nejčastěji… v práci a v obchodě.</span></td></tr>
<tr><td><span class="cz">S kým…?</span></td><td><span class="cz">…s manželem a se synem.</span></td></tr>
<tr><td><span class="cz">Co byste chtěl/a…?</span></td><td><span class="cz">Chtěl/a bych…</span></td></tr>
</table></div>
<h4>How to reach 10 words</h4>
<p>Short: <span class="cz">Mám čas večer.</span> (3 words) → Good: <span class="cz">Na cvičení mám čas hlavně večer po práci, od šesti hodin.</span> (10 words)</p>
<p>Add <b>when</b> (<span class="cz">v pondělí, ráno, od šesti</span>), <b>where</b> (<span class="cz">v práci, doma, v parku</span>), <b>with whom</b> (<span class="cz">s rodinou</span>) or <b>why</b> (<span class="cz">protože…</span>).</p>
<h4>Useful linking words</h4>
<p><span class="cz">a</span> · <span class="cz">ale</span> · <span class="cz">protože</span> · <span class="cz">také</span> · <span class="cz">hlavně</span> · <span class="cz">nejčastěji</span> · <span class="cz">většinou</span> · <span class="cz">někdy</span></p>''',
'tips': '''
<ul>
<li><b>Count the words</b> right after each answer. 12–15 words is safer than exactly 10.</li>
<li><b>Don't copy the question</b> instead of answering: take only its verb.</li>
<li><b>Write simple sentences</b> you are sure of. A long sentence with mistakes is worse.</li>
<li><b>Check háčky and čárky</b> and the capital letter at the start.</li>
<li>Your answer doesn't have to be true; it has to be correct and clear.</li>
</ul>''',
}
THEORY['w2']['en'] = {
'how': '''
<p>You write an <b>e-mail</b> for a situation, for example <span class="cz">Chcete pozvat sousedy na grilování.</span> The pictures show <b>5 questions</b> (<span class="cz">KDY TO BUDE? KDE TO BUDE?…</span>) and you must answer <b>each</b> with at least one sentence. <b>At least 35 words, otherwise 0 points.</b> The task is worth <b>12 points</b>.</p>
<ul>
<li>They assess: an answer to all 5 pictures, a greeting, a purpose and a closing, and clear grammar.</li>
<li>A good e-mail has 45–60 words, so you never fall below 35.</li>
<li>Write to the addressee in the task: formally to a company, informally to a friend.</li>
</ul>''',
'grammar': '''
<h4>The e-mail frame</h4>
<div class="tblw"><table class="tbl">
<tr><th>Part</th><th>Formal (company, school, doctor)</th><th>Informal (friend, neighbour, colleague)</th></tr>
<tr><td>Greeting</td><td><span class="cz">Dobrý den,</span> · <span class="cz">Vážená paní Nováková,</span></td><td><span class="cz">Ahoj Petře,</span> · <span class="cz">Milá Jano,</span></td></tr>
<tr><td>Purpose</td><td><span class="cz">Píšu vám, protože…</span> · <span class="cz">Chtěl/a bych…</span></td><td><span class="cz">Píšu ti, protože…</span> · <span class="cz">Chci tě pozvat…</span></td></tr>
<tr><td>5 pictures</td><td colspan="2">one sentence per picture, in order</td></tr>
<tr><td>Closing</td><td><span class="cz">Děkuji za odpověď.</span> · <span class="cz">S pozdravem</span></td><td><span class="cz">Těším se.</span> · <span class="cz">Měj se</span> · <span class="cz">Ahoj</span></td></tr>
<tr><td>Signature</td><td colspan="2">your name (and surname in a formal e-mail)</td></tr>
</table></div>
<h4>Addressing someone: the vocative</h4>
<p><span class="cz">Petr → Petře</span> · <span class="cz">Tomáš → Tomáši</span> · <span class="cz">Pavel → Pavle</span> · <span class="cz">Jana → Jano</span> · <span class="cz">Eva → Evo</span> · <span class="cz">paní Nováková → paní Nováková</span> (no change)</p>
<h4>Dates and times</h4>
<p><span class="cz">v sobotu</span> · <span class="cz">v sobotu 12. června</span> · <span class="cz">v 18 hodin</span> · <span class="cz">od 10 do 12</span> · <span class="cz">příští týden</span> · <span class="cz">do středy</span> (by Wednesday)</p>
<h4>Ready-made phrases</h4>
<p><span class="cz">Chtěl/a bych se zeptat, …</span> · <span class="cz">Můžete mi prosím napsat, …?</span> · <span class="cz">Prosím o odpověď do pátku.</span> · <span class="cz">Bohužel nemůžu přijít, protože…</span> · <span class="cz">Moc děkuju za…</span></p>''',
'tips': '''
<ul>
<li><b>Plan first</b>: jot down 5 short answers to the pictures, then make sentences from them.</li>
<li><b>Answer in the order of the pictures</b>: it is easy to check nothing is missing.</li>
<li><b>Count the words</b> at the end. Fewer than 35 means 0 points for the whole e-mail.</li>
<li><b>Don't forget the closing and signature</b>: they are part of the score.</li>
<li><b>“Vy” or “ty”?</b> Company, school, doctor: <span class="cz">vám, můžete</span>. Friend, neighbour: <span class="cz">ti, můžeš</span>. Don't mix them in one e-mail.</li>
</ul>''',
}

THEORY['w1']['ru'] = {
'how': '''
<p>Вы заполняете короткий <b>формуляр</b> (анкету, заявку) и отвечаете на <b>3 вопроса</b>. На каждый — <b>полным предложением, минимум 10 слов</b>. Задание даёт <b>8 баллов</b>, на весь Psaní есть 25 минут.</p>
<ul>
<li>С апреля 2026 это не «имя, адрес, дата», а настоящие вопросы: <span class="cz">Proč se hlásíte do kurzu? Kde nejčastěji mluvíte česky?</span></li>
<li>Оценивают: ответили ли вы именно на вопрос, есть ли 10 слов, понятно ли и грамматически правильно ли предложение.</li>
<li>Ответ меньше 10 слов теряет баллы, даже если он правильный.</li>
</ul>''',
'grammar': '''
<h4>Формула: вопрос → ответ</h4>
<p class="formula">Глагол из вопроса <span>+</span> ответ <span>+</span> деталь или <span class="cz">protože…</span></p>
<div class="tblw"><table class="tbl">
<tr><th>Вопрос</th><th>Начало ответа</th></tr>
<tr><td><span class="cz">Proč chcete…?</span></td><td><span class="cz">Chci…, protože…</span></td></tr>
<tr><td><span class="cz">Kdy máte čas?</span></td><td><span class="cz">Čas mám v pondělí a ve středu od…</span></td></tr>
<tr><td><span class="cz">Jak jste se učil/a česky?</span></td><td><span class="cz">Česky jsem se učil/a v kurzu a…</span></td></tr>
<tr><td><span class="cz">Kde nejčastěji…?</span></td><td><span class="cz">Nejčastěji… v práci a v obchodě.</span></td></tr>
<tr><td><span class="cz">S kým…?</span></td><td><span class="cz">…s manželem a se synem.</span></td></tr>
<tr><td><span class="cz">Co byste chtěl/a…?</span></td><td><span class="cz">Chtěl/a bych…</span></td></tr>
</table></div>
<h4>Как «дотянуть» до 10 слов</h4>
<p>Коротко: <span class="cz">Mám čas večer.</span> (3 слова) → Хорошо: <span class="cz">Na cvičení mám čas hlavně večer po práci, od šesti hodin.</span> (10 слов)</p>
<p>Добавьте <b>когда</b> (<span class="cz">v pondělí, ráno, od šesti</span>), <b>где</b> (<span class="cz">v práci, doma, v parku</span>), <b>с кем</b> (<span class="cz">s rodinou</span>) или <b>почему</b> (<span class="cz">protože…</span>).</p>
<h4>Полезные связки</h4>
<p><span class="cz">a</span> · <span class="cz">ale</span> · <span class="cz">protože</span> · <span class="cz">také</span> · <span class="cz">hlavně</span> · <span class="cz">nejčastěji</span> · <span class="cz">většinou</span> · <span class="cz">někdy</span></p>''',
'tips': '''
<ul>
<li><b>Считайте слова</b> сразу после каждого ответа. Лучше 12–15 слов, чем ровно 10.</li>
<li><b>Не повторяйте вопрос дословно</b> вместо ответа: берите из него только глагол.</li>
<li><b>Пишите простые предложения</b>, в которых уверены. Длинное предложение с ошибками хуже.</li>
<li><b>Проверьте háčky и čárky</b> и заглавную букву в начале предложения.</li>
<li>Ответ не обязан быть правдой, главное — правильный и понятный.</li>
</ul>''',
}
THEORY['w2']['ru'] = {
'how': '''
<p>Вы пишете <b>e-mail</b> по ситуации, например <span class="cz">Chcete pozvat sousedy na grilování.</span> На картинках <b>5 вопросов</b> (<span class="cz">KDY TO BUDE? KDE TO BUDE?…</span>), и на <b>каждый</b> нужно ответить хотя бы одним предложением. <b>Минимум 35 слов, иначе 0 баллов.</b> Задание даёт <b>12 баллов</b>.</p>
<ul>
<li>Оценивают: есть ли ответ на все 5 картинок, есть ли обращение, цель и прощание, понятна ли грамматика.</li>
<li>Хорошее письмо — 45–60 слов: так вы точно не опуститесь ниже 35.</li>
<li>Пишите тому адресату, который указан в задании: в фирму официально, другу неформально.</li>
</ul>''',
'grammar': '''
<h4>Каркас письма</h4>
<div class="tblw"><table class="tbl">
<tr><th>Часть</th><th>Официально (фирма, школа, врач)</th><th>Неформально (друг, сосед, коллега)</th></tr>
<tr><td>Обращение</td><td><span class="cz">Dobrý den,</span> · <span class="cz">Vážená paní Nováková,</span></td><td><span class="cz">Ahoj Petře,</span> · <span class="cz">Milá Jano,</span></td></tr>
<tr><td>Цель</td><td><span class="cz">Píšu vám, protože…</span> · <span class="cz">Chtěl/a bych…</span></td><td><span class="cz">Píšu ti, protože…</span> · <span class="cz">Chci tě pozvat…</span></td></tr>
<tr><td>5 картинок</td><td colspan="2">по одному предложению на каждую картинку, по порядку</td></tr>
<tr><td>Конец</td><td><span class="cz">Děkuji za odpověď.</span> · <span class="cz">S pozdravem</span></td><td><span class="cz">Těším se.</span> · <span class="cz">Měj se</span> · <span class="cz">Ahoj</span></td></tr>
<tr><td>Подпись</td><td colspan="2">имя (и фамилия в официальном письме)</td></tr>
</table></div>
<h4>Обращение: звательный падеж (vokativ)</h4>
<p><span class="cz">Petr → Petře</span> · <span class="cz">Tomáš → Tomáši</span> · <span class="cz">Pavel → Pavle</span> · <span class="cz">Jana → Jano</span> · <span class="cz">Eva → Evo</span> · <span class="cz">paní Nováková → paní Nováková</span> (не меняется)</p>
<h4>Даты и время</h4>
<p><span class="cz">v sobotu</span> · <span class="cz">v sobotu 12. června</span> · <span class="cz">v 18 hodin</span> · <span class="cz">od 10 do 12</span> · <span class="cz">příští týden</span> · <span class="cz">do středy</span> (до среды)</p>
<h4>Готовые фразы</h4>
<p><span class="cz">Chtěl/a bych se zeptat, …</span> · <span class="cz">Můžete mi prosím napsat, …?</span> · <span class="cz">Prosím o odpověď do pátku.</span> · <span class="cz">Bohužel nemůžu přijít, protože…</span> · <span class="cz">Moc děkuju za…</span></p>''',
'tips': '''
<ul>
<li><b>Сначала план</b>: выпишите 5 коротких ответов на картинки, потом сделайте из них предложения.</li>
<li><b>Отвечайте по порядку картинок</b>: так легко проверить, что ничего не пропущено.</li>
<li><b>Посчитайте слова</b> в конце. Меньше 35 — это 0 баллов за всё письмо.</li>
<li><b>Не забудьте подпись</b> и прощание: это часть оценки.</li>
<li><b>«Вы» или «ты»?</b> Фирма, школа, врач — <span class="cz">vám, můžete</span>. Друг, сосед — <span class="cz">ti, můžeš</span>. Не смешивайте в одном письме.</li>
</ul>''',
}

THEORY['w1']['vi'] = {
'how': '''
<p>Bạn điền một <b>mẫu đơn</b> ngắn (phiếu hỏi, đơn đăng ký) và trả lời <b>3 câu hỏi</b>. Mỗi câu trả lời phải là <b>câu đầy đủ, ít nhất 10 từ</b>. Bài này được <b>8 điểm</b>; cả phần Psaní có 25 phút.</p>
<ul>
<li>Từ tháng 4/2026 không còn là «tên, địa chỉ, ngày» mà là câu hỏi thật: <span class="cz">Proč se hlásíte do kurzu? Kde nejčastěji mluvíte česky?</span></li>
<li>Giám khảo đánh giá: bạn có trả lời đúng câu hỏi không, có đủ 10 từ không, câu có rõ ràng và đúng ngữ pháp không.</li>
<li>Câu trả lời dưới 10 từ bị mất điểm dù nội dung đúng.</li>
</ul>''',
'grammar': '''
<h4>Công thức: câu hỏi → câu trả lời</h4>
<p class="formula">Động từ trong câu hỏi <span>+</span> câu trả lời <span>+</span> chi tiết hoặc <span class="cz">protože…</span></p>
<div class="tblw"><table class="tbl">
<tr><th>Câu hỏi</th><th>Câu trả lời bắt đầu</th></tr>
<tr><td><span class="cz">Proč chcete…?</span></td><td><span class="cz">Chci…, protože…</span></td></tr>
<tr><td><span class="cz">Kdy máte čas?</span></td><td><span class="cz">Čas mám v pondělí a ve středu od…</span></td></tr>
<tr><td><span class="cz">Jak jste se učil/a česky?</span></td><td><span class="cz">Česky jsem se učil/a v kurzu a…</span></td></tr>
<tr><td><span class="cz">Kde nejčastěji…?</span></td><td><span class="cz">Nejčastěji… v práci a v obchodě.</span></td></tr>
<tr><td><span class="cz">S kým…?</span></td><td><span class="cz">…s manželem a se synem.</span></td></tr>
<tr><td><span class="cz">Co byste chtěl/a…?</span></td><td><span class="cz">Chtěl/a bych…</span></td></tr>
</table></div>
<h4>Cách viết đủ 10 từ</h4>
<p>Ngắn: <span class="cz">Mám čas večer.</span> (3 từ) → Tốt: <span class="cz">Na cvičení mám čas hlavně večer po práci, od šesti hodin.</span> (10 từ)</p>
<p>Thêm <b>khi nào</b> (<span class="cz">v pondělí, ráno, od šesti</span>), <b>ở đâu</b> (<span class="cz">v práci, doma, v parku</span>), <b>với ai</b> (<span class="cz">s rodinou</span>) hoặc <b>tại sao</b> (<span class="cz">protože…</span>).</p>
<h4>Từ nối hữu ích</h4>
<p><span class="cz">a</span> · <span class="cz">ale</span> · <span class="cz">protože</span> · <span class="cz">také</span> · <span class="cz">hlavně</span> · <span class="cz">nejčastěji</span> · <span class="cz">většinou</span> · <span class="cz">někdy</span></p>''',
'tips': '''
<ul>
<li><b>Đếm từ</b> ngay sau mỗi câu. 12–15 từ an toàn hơn đúng 10 từ.</li>
<li><b>Đừng chép lại câu hỏi</b> thay cho câu trả lời: chỉ lấy động từ của nó.</li>
<li><b>Viết câu đơn giản</b> mà bạn chắc chắn. Câu dài có lỗi còn tệ hơn.</li>
<li><b>Kiểm tra háčky và čárky</b> và chữ hoa đầu câu.</li>
<li>Câu trả lời không cần đúng sự thật; quan trọng là đúng và rõ ràng.</li>
</ul>''',
}
THEORY['w2']['vi'] = {
'how': '''
<p>Bạn viết một <b>e-mail</b> theo tình huống, ví dụ <span class="cz">Chcete pozvat sousedy na grilování.</span> Các tranh có <b>5 câu hỏi</b> (<span class="cz">KDY TO BUDE? KDE TO BUDE?…</span>) và bạn phải trả lời <b>từng câu</b> ít nhất bằng một câu. <b>Ít nhất 35 từ, nếu không được 0 điểm.</b> Bài này được <b>12 điểm</b>.</p>
<ul>
<li>Giám khảo đánh giá: có trả lời đủ 5 tranh không, có lời chào, mục đích và lời kết không, ngữ pháp có rõ không.</li>
<li>Một e-mail tốt có 45–60 từ, như vậy bạn không bao giờ dưới 35.</li>
<li>Viết đúng người nhận trong đề: trang trọng với công ty, thân mật với bạn bè.</li>
</ul>''',
'grammar': '''
<h4>Khung e-mail</h4>
<div class="tblw"><table class="tbl">
<tr><th>Phần</th><th>Trang trọng (công ty, trường, bác sĩ)</th><th>Thân mật (bạn, hàng xóm, đồng nghiệp)</th></tr>
<tr><td>Lời chào</td><td><span class="cz">Dobrý den,</span> · <span class="cz">Vážená paní Nováková,</span></td><td><span class="cz">Ahoj Petře,</span> · <span class="cz">Milá Jano,</span></td></tr>
<tr><td>Mục đích</td><td><span class="cz">Píšu vám, protože…</span> · <span class="cz">Chtěl/a bych…</span></td><td><span class="cz">Píšu ti, protože…</span> · <span class="cz">Chci tě pozvat…</span></td></tr>
<tr><td>5 tranh</td><td colspan="2">mỗi tranh một câu, theo thứ tự</td></tr>
<tr><td>Lời kết</td><td><span class="cz">Děkuji za odpověď.</span> · <span class="cz">S pozdravem</span></td><td><span class="cz">Těším se.</span> · <span class="cz">Měj se</span> · <span class="cz">Ahoj</span></td></tr>
<tr><td>Chữ ký</td><td colspan="2">tên của bạn (và họ trong e-mail trang trọng)</td></tr>
</table></div>
<h4>Gọi tên: cách hô cách (vokativ)</h4>
<p><span class="cz">Petr → Petře</span> · <span class="cz">Tomáš → Tomáši</span> · <span class="cz">Pavel → Pavle</span> · <span class="cz">Jana → Jano</span> · <span class="cz">Eva → Evo</span> · <span class="cz">paní Nováková → paní Nováková</span> (không đổi)</p>
<h4>Ngày và giờ</h4>
<p><span class="cz">v sobotu</span> · <span class="cz">v sobotu 12. června</span> · <span class="cz">v 18 hodin</span> · <span class="cz">od 10 do 12</span> · <span class="cz">příští týden</span> · <span class="cz">do středy</span> (trước thứ Tư)</p>
<h4>Câu viết sẵn</h4>
<p><span class="cz">Chtěl/a bych se zeptat, …</span> · <span class="cz">Můžete mi prosím napsat, …?</span> · <span class="cz">Prosím o odpověď do pátku.</span> · <span class="cz">Bohužel nemůžu přijít, protože…</span> · <span class="cz">Moc děkuju za…</span></p>''',
'tips': '''
<ul>
<li><b>Lập dàn ý trước</b>: ghi 5 câu trả lời ngắn cho các tranh, rồi viết thành câu.</li>
<li><b>Trả lời theo thứ tự tranh</b>: dễ kiểm tra không bỏ sót.</li>
<li><b>Đếm từ</b> ở cuối. Dưới 35 từ là 0 điểm cho cả e-mail.</li>
<li><b>Đừng quên lời kết và chữ ký</b>: chúng được tính điểm.</li>
<li><b>«Vy» hay «ty»?</b> Công ty, trường, bác sĩ: <span class="cz">vám, můžete</span>. Bạn bè, hàng xóm: <span class="cz">ti, můžeš</span>. Đừng trộn lẫn trong một e-mail.</li>
</ul>''',
}

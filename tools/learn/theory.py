# Пояснення до úloh. THEORY[úloha][мова] = {'how': html, 'grammar': html, 'tips': html}
# Чеські приклади пишуться в <span class="cz">…</span> (їх можна озвучити кліком).
THEORY = {'u1': {}, 'u2': {}, 'u3': {}, 'u4': {}}

THEORY['u1']['uk'] = {
'how': '''
<p>Екзаменатор називає <b>тему</b> і ставить <b>4 питання</b>. Потім друга тема і ще 4 питання. Разом 8 питань, близько 3 хвилин, <b>8 балів</b>. Питань ви заздалегідь не бачите, лише чуєте.</p>
<ul>
<li>Питання прості, про ваше життя: де живете, що робите, що робили вчора, що будете робити.</li>
<li>У кожній темі зазвичай є питання в <b>різних часах</b>: теперішньому, минулому, майбутньому, а часто й «що б ви хотіли».</li>
<li>Оцінюють, чи ви зрозуміли питання, чи відповіли <b>цілим реченням</b>, чи правильний час і чи достатньо слів.</li>
</ul>''',
'grammar': '''
<h4>Формула доброї відповіді</h4>
<p class="formula">Відповідь цілим реченням <span>+</span> одна деталь <span>+</span> <span class="cz">protože…</span> / <span class="cz">a…</span> / <span class="cz">ale…</span></p>
<p>Не <span class="cz">V Kralupech.</span>, а <span class="cz">Bydlím v Kralupech, je to malé město blízko Prahy.</span></p>
<h4>Головний секрет: беріть дієслово з питання</h4>
<table class="tbl">
<tr><th>Питання</th><th>Відповідь починається так</th><th>Час</th></tr>
<tr><td><span class="cz">Kde bydlíte?</span></td><td><span class="cz">Bydlím…</span></td><td>теперішній</td></tr>
<tr><td><span class="cz">Co děláte ve volném čase?</span></td><td><span class="cz">Ve volném čase dělám / čtu / chodím…</span></td><td>теперішній</td></tr>
<tr><td><span class="cz">Co jste dělal/a včera?</span></td><td><span class="cz">Včera jsem dělal/a…</span></td><td>минулий</td></tr>
<tr><td><span class="cz">Kde jste byl/a na dovolené?</span></td><td><span class="cz">Na dovolené jsem byl/a…</span></td><td>минулий</td></tr>
<tr><td><span class="cz">Co budete dělat o víkendu?</span></td><td><span class="cz">O víkendu budu…</span> / <span class="cz">pojedu…</span> / <span class="cz">půjdu…</span></td><td>майбутній</td></tr>
<tr><td><span class="cz">Co byste chtěl/a…?</span></td><td><span class="cz">Chtěl/a bych…</span></td><td>«хотів би»</td></tr>
</table>
<h4>Теперішній час: закінчення «я»</h4>
<p><span class="cz">bydlet → bydlím</span> · <span class="cz">dělat → dělám</span> · <span class="cz">mít → mám</span> · <span class="cz">být → jsem</span> · <span class="cz">pracovat → pracuju</span> · <span class="cz">jít → jdu</span> · <span class="cz">jet → jedu</span></p>
<h4>Минулий час: дієслово на -l + jsem</h4>
<p><span class="cz">dělat → dělal jsem</span> (чоловік) / <span class="cz">dělala jsem</span> (жінка). У питанні «ви»: <span class="cz">Co jste dělal/a?</span> Відповідь «я»: <span class="cz">Dělal/a jsem…</span></p>
<p>Часті неправильні: <span class="cz">být → byl/a</span> · <span class="cz">jít → šel / šla</span> · <span class="cz">jet → jel/a</span> · <span class="cz">mít → měl/a</span> · <span class="cz">jíst → jedl/a</span> · <span class="cz">vidět → viděl/a</span></p>
<h4>Майбутній час</h4>
<p><span class="cz">budu + інфінітив</span>: <span class="cz">budu pracovat, budu se učit</span>. Рух: <span class="cz">pojedu</span> (поїду), <span class="cz">půjdu</span> (піду). Коли: <span class="cz">zítra, o víkendu, příští týden, příští rok</span>.</p>
<h4>«Хотів би»</h4>
<p><span class="cz">Chtěl bych</span> (чоловік) / <span class="cz">Chtěla bych</span> (жінка) + інфінітив: <span class="cz">Chtěla bych mít větší byt.</span></p>''',
'tips': '''
<ul>
<li><b>Не зрозуміли питання?</b> Попросіть повторити: <span class="cz">Promiňte, můžete to zopakovat?</span> Це нормально, балів за це не знімають.</li>
<li><b>Не відповідайте одним словом.</b> «Ano» чи «V sobotu» майже нічого не дає. Додайте речення.</li>
<li><b>Слухайте, в якому часі питання</b>: <span class="cz">jste dělal/a</span> — минулий, <span class="cz">budete</span> — майбутній.</li>
<li><b>Не знаєте слова?</b> Скажіть простіше: замість <span class="cz">účetní</span> — <span class="cz">pracuju v kanceláři s čísly</span>.</li>
<li><b>Підготуйте розповідь про себе</b> на 1 хвилину: ім'я, звідки ви, сім'я, робота, хобі. Її шматки підходять до багатьох тем.</li>
<li>Відповідь не мусить бути правдою. Головне, щоб вона була правильна й зрозуміла.</li>
</ul>''',
}

THEORY['u3']['uk'] = {
'how': '''
<p>Ви бачите <b>4 картинки</b> і питання, наприклад <span class="cz">Co včera dělali muž a žena?</span> Ваше завдання — розповісти історію <b>в минулому часі</b>, використавши <b>всі 4 картинки</b>. На іспиті на це є <b>1 хвилина</b>, завдання дає <b>10 балів</b>.</p>
<ul>
<li>Оцінюють: чи є всі 4 картинки, чи правильний минулий час, чи розповідь зв'язна (слова «потім», «нарешті») і чи вистачає слів саме з цієї ситуації.</li>
<li>Добра розповідь має 60–90 слів: по 2–3 речення на картинку.</li>
<li>У новому форматі ситуації практичні: поліція, лікар, пошта, поломка, переїзд. Тому важливо знати конкретні слова.</li>
</ul>''',
'grammar': '''
<h4>Як утворити минулий час</h4>
<p>Беремо інфінітив, відкидаємо <b>-t</b> і додаємо <b>-l</b>. Закінчення залежить від того, <b>хто</b> робив:</p>
<div class="tblw"><table class="tbl">
<tr><th>Хто</th><th>dělat</th><th>koupit</th><th>být</th></tr>
<tr><td>він (muž, pan Novák)</td><td><span class="cz">dělal</span></td><td><span class="cz">koupil</span></td><td><span class="cz">byl</span></td></tr>
<tr><td>вона (žena, paní Nová)</td><td><span class="cz">dělala</span></td><td><span class="cz">koupila</span></td><td><span class="cz">byla</span></td></tr>
<tr><td>воно (dítě, auto)</td><td><span class="cz">dělalo</span></td><td><span class="cz">koupilo</span></td><td><span class="cz">bylo</span></td></tr>
<tr><td>вони (muž a žena, rodina → oni)</td><td><span class="cz">dělali</span></td><td><span class="cz">koupili</span></td><td><span class="cz">byli</span></td></tr>
</table></div>
<p>У розповіді про <b>інших людей</b> слово <span class="cz">jsem</span> не потрібне: <span class="cz">Muž šel do obchodu.</span> Про <b>себе</b> додаємо <span class="cz">jsem</span> або <span class="cz">jsme</span>: <span class="cz">Šel jsem do obchodu. Byli jsme v Praze.</span></p>
<h4>Неправильні дієслова, які трапляються найчастіше</h4>
<p><span class="cz">jít → šel, šla</span> · <span class="cz">jet → jel</span> · <span class="cz">přijít → přišel</span> · <span class="cz">najít → našel</span> · <span class="cz">mít → měl</span> · <span class="cz">chtít → chtěl</span> · <span class="cz">moct → mohl</span> · <span class="cz">říct → řekl</span> · <span class="cz">vzít → vzal</span> · <span class="cz">jíst → jedl</span> · <span class="cz">pít → pil</span> · <span class="cz">číst → četl</span> · <span class="cz">začít → začal</span> · <span class="cz">spát → spal</span> · <span class="cz">zapomenout → zapomněl</span></p>
<h4>Зворотні дієслова: se / si на другому місці</h4>
<p><span class="cz">Muž se probudil.</span> · <span class="cz">Žena si koupila boty.</span> · <span class="cz">Ráno se oblékl a umyl.</span></p>
<h4>Каркас розповіді</h4>
<div class="tblw"><table class="tbl">
<tr><th>Частина</th><th>Слова-зв'язки</th><th>Приклад</th></tr>
<tr><td>Початок: коли, хто, де</td><td><span class="cz">Včera ráno…</span> · <span class="cz">Minulou sobotu…</span></td><td><span class="cz">Včera ráno jel pan Novák do práce.</span></td></tr>
<tr><td>Картинка 1</td><td><span class="cz">Nejdřív…</span> · <span class="cz">Na začátku…</span></td><td><span class="cz">Nejdřív si koupil kávu.</span></td></tr>
<tr><td>Картинки 2–3</td><td><span class="cz">Potom…</span> · <span class="cz">Pak…</span> · <span class="cz">Když…</span> · <span class="cz">Najednou…</span></td><td><span class="cz">Najednou začalo pršet.</span></td></tr>
<tr><td>Картинка 4, кінець</td><td><span class="cz">Nakonec…</span> · <span class="cz">Večer…</span></td><td><span class="cz">Nakonec šel domů a byl unavený.</span></td></tr>
</table></div>
<p>Додайте почуття: <span class="cz">byl šťastný</span>, <span class="cz">byla nervózní</span>, <span class="cz">byli unavení</span>, і причину: <span class="cz">protože…</span></p>''',
'tips': '''
<ul>
<li><b>Не описуйте картинку в теперішньому часі</b> («Na obrázku je muž…»). Розповідайте історію: <span class="cz">Muž šel…</span></li>
<li><b>Дайте людям імена</b>: <span class="cz">pan Novák, paní Nová</span>. Так легше говорити й не плутатися.</li>
<li><b>Не пропускайте жодної картинки</b>: за кожну пропущену втрачаються бали.</li>
<li><b>Не знаєте слова?</b> Опишіть інакше: замість <span class="cz">pokuta</span> — <span class="cz">musel zaplatit peníze policii</span>.</li>
<li><b>Слідкуйте за родом</b>: жінка — <span class="cz">šla, byla, koupila</span>, чоловік — <span class="cz">šel, byl, koupil</span>.</li>
<li>Тренуйтеся з таймером на 1 хвилину: спочатку з текстом, потім лише з картинками.</li>
</ul>''',
}

THEORY['u2']['uk'] = {
'how': '''
<p>Ви отримуєте <b>2 картки</b> з ситуацією, наприклад <span class="cz">Jste na recepci hotelu.</span> На картці <b>3 короткі підказки</b> (<span class="cz">Volný pokoj?</span> · <span class="cz">Kč za noc?</span> · <span class="cz">Hodina snídaně?</span>) і четвертий пункт <span class="cz">…? (vaše otázka)</span>, де питання треба придумати самому. Разом 8 питань, <b>12 балів</b>.</p>
<ul>
<li><b>Питаєте ви</b>, екзаменатор відповідає, як працівник готелю, пошти чи магазину.</li>
<li>Оцінюють, чи з підказки вийшло <b>повне правильне питання</b>, чи ви говорите ввічливо на <b>«Ви»</b> і чи четверте питання підходить до ситуації.</li>
<li>Добрий порядок: привітання і мета → 4 питання → подяка й прощання.</li>
</ul>''',
'grammar': '''
<h4>З підказки робимо питання</h4>
<div class="tblw"><table class="tbl">
<tr><th>Підказка</th><th>Питання</th></tr>
<tr><td><span class="cz">Volný pokoj?</span></td><td><span class="cz">Máte volný pokoj?</span></td></tr>
<tr><td><span class="cz">Kč za noc?</span> / <span class="cz">Cena?</span></td><td><span class="cz">Kolik stojí jedna noc?</span> · <span class="cz">Kolik to stojí?</span></td></tr>
<tr><td><span class="cz">Hodina snídaně?</span></td><td><span class="cz">V kolik hodin je snídaně?</span></td></tr>
<tr><td><span class="cz">Otevírací doba?</span></td><td><span class="cz">Od kolika do kolika máte otevřeno?</span></td></tr>
<tr><td><span class="cz">Platba kartou?</span></td><td><span class="cz">Můžu platit kartou?</span></td></tr>
<tr><td><span class="cz">Doba opravy?</span></td><td><span class="cz">Jak dlouho bude oprava trvat?</span></td></tr>
<tr><td><span class="cz">Parkování?</span></td><td><span class="cz">Je u vás parkoviště?</span> · <span class="cz">Kde můžu parkovat?</span></td></tr>
<tr><td><span class="cz">Sleva?</span></td><td><span class="cz">Máte nějakou slevu?</span></td></tr>
</table></div>
<h4>Питальні слова</h4>
<p><span class="cz">Kolik?</span> скільки · <span class="cz">Kdy? V kolik hodin?</span> коли · <span class="cz">Kde?</span> де · <span class="cz">Jak dlouho?</span> як довго · <span class="cz">Jaký? Která?</span> який · <span class="cz">Proč?</span> чому · <span class="cz">Od kolika do kolika?</span> з якої до якої години</p>
<h4>Питання «так / ні»: дієслово на початку</h4>
<p><span class="cz">Máte…?</span> (у вас є) · <span class="cz">Můžu…? / Můžete…?</span> (можна / можете) · <span class="cz">Musím…?</span> (мушу) · <span class="cz">Je možné…?</span> (чи можна) · <span class="cz">Je tam…?</span> (чи там є)</p>
<h4>Ввічливо на «Ви»</h4>
<p>Правильно: <span class="cz">máte, můžete, víte, potřebujete</span>. Неправильно в цьому завданні: <span class="cz">máš, můžeš, víš</span>. Початок: <span class="cz">Dobrý den, chtěl/a bych…</span> або <span class="cz">Prosím vás, …</span>. Кінець: <span class="cz">Děkuju, na shledanou.</span></p>
<h4>Четверте питання: універсальні варіанти</h4>
<p><span class="cz">Můžu platit kartou?</span> · <span class="cz">Musím se objednat předem?</span> · <span class="cz">Je tam parkoviště?</span> · <span class="cz">Máte slevu pro děti?</span> · <span class="cz">Kde to najdu?</span> · <span class="cz">Máte otevřeno i v sobotu?</span></p>''',
'tips': '''
<ul>
<li><b>Не читайте підказку вголос</b> («Cena?»): з неї треба зробити речення-питання.</li>
<li><b>Слухайте відповідь екзаменатора</b> і не питайте того самого двічі.</li>
<li>Четверте питання має <b>стосуватися ситуації</b>: у готелі про сніданок чи паркування, а не про погоду.</li>
<li>Якщо відповідь незрозуміла: <span class="cz">Promiňte, můžete to zopakovat?</span></li>
<li>Наприкінці подякуйте: <span class="cz">Děkuju za informace. Na shledanou.</span></li>
</ul>''',
}

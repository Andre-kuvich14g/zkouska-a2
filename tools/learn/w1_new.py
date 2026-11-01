# Psaní – úloha 1 (formulář): 20 nových formulářů, odpovědi min. 10 slov
NEWF = [
("Chcete dát dítě do mateřské školy. Odpovězte na otázky v přihlášce.", "Mateřská škola Sluníčko – přihláška", [
 ("Kolik let má vaše dítě a co rádo dělá?", "Moje dcera má čtyři roky a ráda kreslí, zpívá a hraje si venku."),
 ("Proč chcete dát dítě do naší školky?", "Chci ji dát do vaší školky, protože je blízko domu a má velkou zahradu."),
 ("Kdy může dítě do školky chodit?", "Dítě může chodit do školky každý den od sedmi ráno do čtyř odpoledne.")]),
("Chcete se registrovat u nového zubaře. Vyplňte dotazník.", "Zubní ordinace MUDr. Malá – registrace", [
 ("Proč hledáte nového zubaře?", "Hledám nového zubaře, protože jsem se přestěhoval/a a starý zubař je daleko."),
 ("Máte nějaké problémy se zuby?", "Teď mě bolí jeden zub vlevo dole, hlavně když piju studenou vodu."),
 ("Kdy můžete přijít na první prohlídku?", "Na první prohlídku můžu přijít v úterý nebo ve čtvrtek ráno před prací.")]),
("Měl/a jste malou nehodu autem. Vyplňte formulář pro pojišťovnu.", "Pojišťovna Jistota – hlášení škody", [
 ("Kde a kdy se nehoda stala?", "Nehoda se stala včera odpoledne na parkovišti u supermarketu v Kralupech."),
 ("Co se stalo?", "Když jsem couval/a, narazil/a jsem do jiného auta a rozbil/a jsem mu světlo."),
 ("Kdo byl u nehody a byl někdo zraněný?", "U nehody jsem byl/a já a majitel druhého auta, nikdo nebyl zraněný.")]),
("Chcete si udělat řidičský průkaz. Vyplňte přihlášku do autoškoly.", "Autoškola Volant – přihláška", [
 ("Proč chcete řidičský průkaz?", "Chci řidičský průkaz, protože potřebuju jezdit do práce a vozit děti do školy."),
 ("Řídil/a jste už někdy auto?", "Ano, trochu jsem řídil/a s otcem na vesnici, ale nemám žádnou zkoušku."),
 ("Kdy můžete chodit na jízdy?", "Na jízdy můžu chodit odpoledne po práci, nejlépe v pondělí a ve středu.")]),
("Chcete si založit účet v bance. Odpovězte na otázky ve formuláři.", "Banka Plus – nový účet", [
 ("Proč si chcete založit účet?", "Chci si založit účet, protože mi zaměstnavatel bude posílat výplatu na účet."),
 ("Jak budete účet nejčastěji používat?", "Účet budu nejčastěji používat na placení kartou v obchodě a na nájem."),
 ("Chcete také internetové bankovnictví a proč?", "Ano, chci internetové bankovnictví, protože můžu platit z domova a vidět platby.")]),
("Hledáte práci. Vyplňte dotazník na úřadu práce.", "Úřad práce – dotazník uchazeče", [
 ("Jakou práci jste dělal/a naposledy?", "Naposledy jsem pracoval/a tři roky jako prodavač/ka v obchodě s oblečením."),
 ("Jakou práci teď hledáte?", "Teď hledám práci ve skladu nebo v kuchyni na plný úvazek."),
 ("Co umíte a jaké jazyky znáte?", "Umím pracovat s počítačem, mám řidičský průkaz a mluvím ukrajinsky, rusky a trochu česky.")]),
("Nakoupil/a jste v e-shopu. Vyplňte dotazník spokojenosti.", "E-shop Domov – dotazník", [
 ("Co jste u nás koupil/a?", "U vás jsem koupil/a nový vysavač a dvě lampy do obývacího pokoje."),
 ("Byl/a jste spokojený/á s doručením?", "S doručením jsem byl/a spokojený/á, balík přišel za dva dny a byl v pořádku."),
 ("Co bychom měli zlepšit?", "Měli byste mít víc informací o zboží v jiných jazycích a levnější dopravu.")]),
("Chcete přihlásit syna na kurz plavání. Vyplňte přihlášku.", "Plavecká škola Delfín – přihláška", [
 ("Umí vaše dítě trochu plavat?", "Můj syn trochu plave, ale bojí se vody, když nemá nohy na zemi."),
 ("Proč chcete dítě přihlásit na kurz?", "Chci ho přihlásit na kurz, protože v létě jedeme k moři a chci, aby byl v bezpečí."),
 ("Který den mu kurz vyhovuje?", "Kurz mu vyhovuje ve středu nebo v pátek odpoledne po škole.")]),
("Chcete poslat dítě na letní tábor. Odpovězte na otázky.", "Letní tábor Bobr – přihláška", [
 ("Co vaše dítě rádo dělá?", "Moje dítě rádo hraje fotbal, plave a chodí na výlety do přírody."),
 ("Má dítě nějakou alergii nebo bere léky?", "Dítě má alergii na ořechy, jinak je zdravé a nebere žádné léky."),
 ("Jak se s vámi můžeme spojit?", "Můžete mi volat na telefon nebo psát na e-mail, odpovídám každý den.")]),
("Chcete si pronajmout byt. Vyplňte žádost pro majitele.", "Žádost o pronájem bytu", [
 ("Kdo bude v bytě bydlet?", "V bytě budu bydlet já, můj manžel a naše dcera, která má sedm let."),
 ("Kde pracujete?", "Pracuju jako kuchař/ka v hotelu v Praze a manžel pracuje ve skladu."),
 ("Proč se chcete stěhovat?", "Chceme se stěhovat, protože náš byt je malý a je daleko od školy.")]),
("Chcete jet na výlet s cestovní kanceláří. Vyplňte objednávku.", "Cestovní kancelář Svět – objednávka", [
 ("Kam chcete jet a kdy?", "Chceme jet na tři dny do Vídně na konci listopadu."),
 ("Kolik osob pojede?", "Pojedou čtyři osoby: já, manželka a dvě děti, kterým je osm a deset let."),
 ("Co chcete na výletě vidět?", "Na výletě chceme vidět zámek, vánoční trhy a velkou zoo.")]),
("Chcete chodit do tanečního kurzu. Vyplňte přihlášku.", "Taneční studio Rytmus – přihláška", [
 ("Tančil/a jste už někdy?", "Tančil/a jsem jen na svatbách, ale v kurzu jsem nikdy nebyl/a."),
 ("Proč chcete chodit do tanečního kurzu?", "Chci chodit do kurzu, protože chci víc sportovat a poznat nové lidi."),
 ("S kým budete do kurzu chodit?", "Do kurzu budu chodit s manželem, protože spolu chceme tančit na plese.")]),
("Škola se ptá rodičů na obědy. Vyplňte dotazník.", "Základní škola – dotazník o obědech", [
 ("Chodí vaše dítě na obědy do školní jídelny?", "Ano, můj syn chodí na obědy do školní jídelny každý den."),
 ("Jak mu jídlo chutná?", "Jídlo mu většinou chutná, ale nemá rád polévky a ryby."),
 ("Co byste chtěl/a v jídelně změnit?", "Chtěl/a bych, aby v jídelně bylo víc ovoce a zeleniny.")]),
("Nefunguje vám pračka. Vyplňte objednávku opravy.", "Servis Pračky – objednávka", [
 ("Jaký problém má vaše pračka?", "Moje pračka nevypouští vodu a dělá velký hluk, když pere."),
 ("Kdy problém začal?", "Problém začal minulý týden v pondělí, když jsem pral/a ručníky."),
 ("Kdy může technik přijít?", "Technik může přijít v sobotu dopoledne nebo ve všední den po páté hodině.")]),
("Chcete se svým týmem hrát fotbalový turnaj. Vyplňte registraci.", "Městský fotbalový turnaj – registrace", [
 ("Kolik hráčů má váš tým?", "Náš tým má osm hráčů, všichni jsou kolegové z práce."),
 ("Jak dlouho spolu hrajete?", "Spolu hrajeme asi rok, trénujeme každou středu večer na hřišti."),
 ("Proč chcete hrát v turnaji?", "Chceme hrát v turnaji, protože je to zábava a chceme poznat nové lidi.")]),
("Chcete chodit na kurz první pomoci. Vyplňte přihlášku.", "Červený kříž – kurz první pomoci", [
 ("Proč chcete kurz první pomoci?", "Chci kurz první pomoci, protože mám malé děti a chci jim umět pomoct."),
 ("Pomáhal/a jste někdy někomu, kdo byl zraněný?", "Jednou jsem pomáhal/a kolegovi, který se v práci řízl do ruky."),
 ("Kdy máte čas na kurz?", "Na kurz mám čas o víkendu, nejlépe v sobotu od rána.")]),
("Chcete registrovat psa u veterináře. Vyplňte formulář.", "Veterinární klinika – nový pacient", [
 ("Jaké zvíře máte a kolik má let?", "Mám psa, je to hnědý labrador a jsou mu tři roky."),
 ("Proč jdete k veterináři?", "Jdu k veterináři, protože pes potřebuje očkování a nechce moc jíst."),
 ("Jak se o psa staráte?", "Se psem chodím ven třikrát denně a dávám mu dobré granule.")]),
("Chcete rezervovat pokoj v hotelu. Vyplňte rezervační formulář.", "Hotel Slunce – rezervace", [
 ("Kdy přijedete a kdy odjedete?", "Přijedeme v pátek dvanáctého července a odjedeme v neděli čtrnáctého."),
 ("Jaký pokoj potřebujete?", "Potřebujeme pokoj pro dva dospělé a jedno dítě, nejlépe s balkonem."),
 ("Máte nějaké další přání?", "Prosíme o snídani do pokoje a parkování pro naše auto.")]),
("Chcete v létě pracovat na brigádě. Vyplňte přihlášku.", "Brigáda v létě – přihláška", [
 ("Jakou práci chcete dělat?", "Chci pracovat v kuchyni nebo jako pomocník v obchodě s ovocem."),
 ("Kdy můžete pracovat?", "Pracovat můžu celý červenec a první dva týdny v srpnu."),
 ("Proč chcete brigádu?", "Chci brigádu, protože potřebuju peníze na dovolenou a chci mluvit víc česky.")]),
("Město dělá průzkum o dopravě. Vyplňte dotazník.", "Město Kralupy – průzkum o dopravě", [
 ("Jak jezdíte po městě?", "Po městě jezdím nejčastěji autobusem a někdy jezdím na kole."),
 ("Co se vám na dopravě ve městě nelíbí?", "Nelíbí se mi, že autobusy večer jezdí málo a často mají zpoždění."),
 ("Co by ve městě pomohlo?", "Ve městě by pomohly nové cyklostezky a víc parkovacích míst u nádraží.")]),
]

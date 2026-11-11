#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Minhāj — Upgrade GT→main : leçon 13738 (tafsir-tanawi-2, Sourate al-Isrāʾ
99-100, leçon 25 du manuel — al-Muḥarrar al-wajīz d'Ibn ʿAṭiyya).

Vérifications et restitutions (source : texte du Muḥarrar al-wajīz sur
quranpedia.net/surah/1/17/book/350 — confrontation mot à mot ; corpus
canonique pour les versets) :
- Bloc d'ouverture (17:99-100) : <p> vide → 2 versets restaurés du
  quran-cache.
- Lexique (الفهم) : les 4 GLOSES sont intactes mais les VEDETTES sont
  perdues — restituées du vocabulaire des versets (الأجل/خزائن/لأمسكتم/
  قتورا) ; l'en-tête الشرح (perdu) restitué d'après la structure du
  manuel.
- Citations inline perdues :
  * v99 : citation perdue après « رد الله تعالى عليهم بقوله » —
    restaurée du quran-cache ;
  * « أولم يروا » (le hamza réprobatif) — restitué du verset ;
  * « قادر على أن يخلق مثلهم » — restitué du verset ;
  * « وإن تتولوا يستبدل قوما غيركم » [محمد: 38 — réf CONFORME] —
    restauré du corpus ;
  * « فأبى » VÉRIFIÉ sur le texte d'Ibn ʿAṭiyya (« وقوله ﴿فأبى﴾ عبارة
    عن تكسبهم وجنوحهم ») ;
  * « وجعل لهم أجلا لا ريب فيه » — restauré du verset (« الأجل » est
    imprimé) ;
  * le pendant d'Aḥqāf « أولم يروا أن الله الذي خلق السماوات والأرض
    ولم يعي بخلقهن بقادر على أن يحيي الموتى » — le manuel imprime
    [الأحقاف: 32] : la référence canonique est 46:33 (11e réf
    d'adjacence erronée notée) ;
  * le pendant de Yā-Sīn « أوليس الذي خلق السماوات والأرض بقادر على
    أن يخلق مثلهم » — le manuel imprime [يس: 80] : la référence
    canonique est 36:81 (12e réf d'adjacence erronée notée) ;
  * v100 : citation perdue — restaurée du quran-cache ; « لو » (la
    règle) VÉRIFIÉ ; « أنتم » (le nominatif) VÉRIFIÉ ; la phrase de
    restitution désordonnée par perte OCR — réordonnée sur le texte
    d'Ibn ʿAṭiyya (« فالتقدير هنا قل لو تملكون خزائن ف﴿أنتم﴾ رفع على
    تبع الضمير »), noté ;
  * « الرحمة » et « الإنفاق » VÉRIFIÉS (« و ﴿الإنفاق﴾ المعروف ذهاب
    المال ») ; « قتورا » VÉRIFIÉ (l'édition en ligne porte « فتورا » —
    coquille, le verset lit قتورا) ;
  * « أم لهم نصيب من الملك إذا لا يؤتون الناس نقيرا » — le manuel
    imprime [النساء: 52] : la référence canonique est 4:53 (13e réf
    d'adjacence erronée notée) ;
  * « إن الإنسان خلق هلوعا… إلا المصلين » [المعارج: 19-22 — réf
    CONFORME] — restauré du corpus ;
  * le hadith d'Abū Hurayra (la main de Dieu pleine) INTACT — Bukhārī,
    Livre de l'Unicité (le « عنه » de رضي الله عنه élidé par l'OCR,
    rendu normalement) ;
  * la finalité 1 : citation [الروم: 26] — la référence canonique du
    verset sur la recréation (« وهو الذي يبدأ الخلق ثم يعيده وهو أهون
    عليه ») est 30:27 (14e réf d'adjacence erronée notée) ;
  * l'istithmār : la citation d'Ibn ʿĀshūr [al-Taḥrīr wa-l-tanwīr
    15/222] INTACTE ;
  * iʿdād : 5 vedettes restituées du vocabulaire des versets 101-104
    (la leçon 26 du manuel — v. 101-104 — ne figure pas dans le corpus
    du site : les documents suivants du livre sont l'index et la
    bibliographie)."""

import json

BOOK = "/home/z/my-project/content/books/tafsir-tanawi-2.json"

HTML_FR = """<h1>La sourate al-Isrāʾ — <em>al-Muḥarrar al-wajīz</em> d’Ibn ʿAṭiyya, versets 99 et 100</h1>
<p>Leçon d’exégèse de la sourate al-Isrāʾ, versets 99 et 100, du livre du Tafsīr à travers <em>al-Muḥarrar al-wajīz fī tafsīr al-kitāb al-ʿazīz</em> du cadi Abū Muḥammad Ibn ʿAṭiyya, à l’intention des élèves de la deuxième année de l’enseignement secondaire traditionnel (<em>taʿlīm ʿatīq</em>), phase 2 (leçon 25).</p>
<h3>Les objectifs de la leçon</h3>
<ul>
<li>Connaître les arguments par lesquels Dieu, le Glorifié, confronta les négateurs de la résurrection.</li>
<li>Conclure la cause de la qualification de l’homme par Dieu, le Très-Haut, d’avarice et de pingrerie.</li>
<li>Prendre guide sur le noble Coran en la dépense de mon bien, en ce qui satisfait Dieu, le Très-Haut.</li>
</ul>
<h3>Introduction (tamhīd)</h3>
<p>Après la réfutation, par Dieu, le Glorifié et Très-Haut, aux versets précédents, des négateurs de la prophétie, Il exposa en ces deux versets la nullité de leur croyance en la résurrection, la prouvant par l’analogie de représentation : ils tenaient pour invraisemblable la recréation de l’homme après qu’il fût devenu terre et poussière — et Dieu, le Puissant, le Majestueux, répondit à cette illusion chancelante : qui a pu créer les cieux et la terre — ce qui est plus grand que la création de l’homme — peut les restituer en leurs identités.</p>
<p>Comment Dieu, le Très-Haut, répondit-Il aux négateurs de la résurrection ? Et quel est le dessein de leur qualification d’avarice et de pingrerie ?</p>
<h3>Les versets</h3>
<p>Allah, le Très-Haut, a dit :</p>
<p>« N’ont-ils point vu que Dieu, qui a créé les cieux et la terre, est capable de créer leurs semblables ? Et Il leur a donné un terme en quoi nul doute — mais les injustes n’ont refusé que d’être renieurs. (100) Dis : “ Si c’est vous qui possédiez les trésors de la miséricorde de mon Seigneur, vous les retiendriez alors, par crainte de la dépense — et l’homme fut créé avare. ” » (al-Isrāʾ, 99-100)</p>
<p>[Citations coraniques restaurées d’après le corpus canonique : l’emplacement imprimé correspondant est vide dans la source numérisée — perte OCR.]</p>
<h3>La compréhension</h3>
<h4>Explication des termes</h4>
<ul>
<li><em>al-ajal</em> (ٱلْأَجَل) : un temps établi pour terme, qu’on atteint en toute circonstance — et son application à la vie devint courante.</li>
<li><em>khazāʾin</em> (خَزَآئِنَ) : les provisions — les trésors d’approvisionnement.</li>
<li><em>la-amskatum</em> (لَّأَمْسَكْتُمْ) : vous auriez retenu — vous auriez été avares.</li>
<li><em>qatūran</em> (قَتُورًۭا) : outrancier en l’avarice.</li>
</ul>
<p>[Gloses imprimées intactes ; vedettes restituées du vocabulaire des versets (les emplacements imprimés sont vides — perte OCR) ; en-tête « Explication des termes » restitué d’après la structure du manuel.]</p>
<h3>Extraction des idées des versets</h3>
<ul>
<li>Qui Dieu, le Glorifié, réfuta-t-Il en ces versets ? Et par quoi ?</li>
<li>De quoi Dieu, le Très-Haut, qualifia-t-Il l’homme en ces versets ?</li>
</ul>
<h3>Le commentaire (tafsīr)</h3>
<p>Ces versets comprennent ce qui suit :</p>
<h3>Premièrement : la réfutation, par Dieu le Glorifié, des négateurs de la résurrection, par les arguments tranchants</h3>
<p>Quand les associateurs eurent nié la résurrection aux versets précédents, Dieu, le Très-Haut, les réfuta en disant :</p>
<p>« N’ont-ils point vu que Dieu, qui a créé les cieux et la terre, est capable de créer leurs semblables ? Et Il leur a donné un terme en quoi nul doute — mais les injustes n’ont refusé que d’être renieurs. » (al-Isrāʾ, 99)</p>
<p>Le <em>hamza</em> en Sa parole : ﴿ <em>a-wa-lam yaraw</em> ﴾ (“ et n’ont-ils point vu ”) est d’interrogation réprobative, et il entre sur un élément élidé. Et la “ vision ” ici est vision du cœur.</p>
<p>[Citation coranique (v. 99) et « a-wa-lam yaraw » restaurées d’après le corpus canonique : les emplacements imprimés sont vides — perte OCR.]</p>
<p>Et Sa parole, le Glorifié :</p>
<p>“ …est capable de créer leurs semblables… ” (al-Isrāʾ, 99 — extrait)</p>
<p>— il se peut que le visé soit : capable de les créer une seconde fois — Il exprima cela par le vocable de “ semblable ” ; et il se peut que le visé soit : capable de créer d’autres serviteurs qui L’unifient et L’adorent — comme en Sa parole :</p>
<p>“ …et si vous vous détournez, Il remplace un peuple autre que vous… ” (Muḥammad, 47:38 — extrait)</p>
<p>[Citations « qādirun ʿalā an yakhluqa mithlahum » et « wa-in tatawallaw yastabdil qawman ghayrakum » restaurées d’après le corpus canonique : les emplacements imprimés sont vides — perte OCR ; la référence imprimée « Muḥammad 47:38 » est conforme.]</p>
<p>Ce verset est un argument contre eux en ce qu’ils tinrent pour invraisemblable — la résurrection : ils reconnaissent la création de Dieu, le Très-Haut, et Son invention de cet ensemble dont l’humanité est une part — ils ne nient point cela. Comment leur serait-il donc valable de reconnaître Sa création du tout, et Son extraction de l’obscurité du néant, et de nier Sa restitution de la part ? L’affaire revint donc à l’espace du possible — et le Véridique, dont les indices d’inimitabilité sont établis, informa de la survenance de ce possible.</p>
<p>Et le pendant de ce verset, Sa parole :</p>
<p>“ N’ont-ils point vu que Dieu, qui a créé les cieux et la terre sans lassitude en leur création, est capable de vivifier les morts ? ” (al-Aḥqāf, 46:33 — extrait)</p>
<p>Et Sa parole, le Glorifié :</p>
<p>“ Et n’est-ce pas Lui qui a créé les cieux et la terre, capable de créer leurs semblables ? ” (Yā-Sīn, 36:81 — extrait)</p>
<p>[Citations restaurées d’après le corpus canonique : les emplacements imprimés sont vides — perte OCR ; le manuel imprime « al-Aḥqāf 46:32 » — la référence canonique est 46:33, et « Yā-Sīn 36:80 » — la référence canonique est 36:81 (écarts de numérotation notés).]</p>
<p>Quand Dieu, le Glorifié, eut exposé qu’Il est capable de la résurrection et qu’elle est d’existence possible, Il y ajouta l’exposé que sa survenance a un temps connu. Le Glorifié dit :</p>
<p>“ …et Il leur a donné un terme en quoi nul doute… ” (al-Isrāʾ, 99 — extrait)</p>
<p>﴿ <em>al-ajal</em> ﴾ (“ le terme ”) : il se peut qu’Il veuille par lui la Résurrection, et il se peut qu’Il veuille le terme de la mort ; et sur cette interprétation c’est un nom de genre, car Il le posa en la place des termes. Et le dessein de ce discours : l’exposé de la puissance de Dieu, le Puissant, le Majestueux, et de Sa royauté sur Sa création — et par l’établissement de cela s’affermi le caractère possible de leur résurrection quand Il veut : il n’est de dieu que Lui.</p>
<p>[Citation « wa-jaʿala lahum ajalan lā rayba fīhi » restaurée d’après le corpus canonique : l’emplacement imprimé est vide — perte OCR ; le commentaire est conforme au texte d’Ibn ʿAṭiyya.]</p>
<p>Et Sa parole : ﴿ <em>fa-abā</em> ﴾ (“ mais il a refusé ”) : expression de leur acquisition [de la dénégation] et de leur inclinaison.</p>
<p>[Citation « fa-abā » restaurée d’après le texte d’Ibn ʿAṭiyya (« وقوله ﴿فأبى﴾ عبارة عن تكسبهم وجنوحهم ») : l’emplacement imprimé est vide — perte OCR.]</p>
<h3>Deuxièmement : l’avarice, des tempéraments et des traits naturels de l’homme</h3>
<p>Après l’exposé par Dieu, le Très-Haut, du traitement de menteurs infligé aux dénégateurs en la résurrection et le rassemblement, Il y ajouta l’exposé de leur avarice — quand même ils posséderaient les trésors des cieux et de la terre. Le Glorifié dit :</p>
<p>« Dis : “ Si c’est vous qui possédiez les trésors de la miséricorde de mon Seigneur, vous les retiendriez alors, par crainte de la dépense — et l’homme fut créé avare. ” » (al-Isrāʾ, 100)</p>
<p>La règle de ﴿ <em>law</em> ﴾ (“ si ”) : que la suive le verbe, soit explicite, soit élidé et expliqué par l’explicite après cela — et ﴿ <em>antum</em> ﴾ (“ vous ”) est au nominatif par un verbe qu’explique ce qui suit, comme la parole du tayyite Ḥātim : “ Si une femme au bracelet de joyaux me giflait… ”. Et la restitution ici : “ Dis : si vous possédez — vous — les trésors… ” : ﴿ <em>antum</em> ﴾ est au nominatif en tant que suivant le pronom [de <em>tamlikūna</em>].</p>
<p>[Citation coranique (v. 100) et « law », « antum » restaurées d’après le corpus canonique et le texte d’Ibn ʿAṭiyya : les emplacements imprimés sont vides — perte OCR ; la phrase de restitution imprimée est désordonnée par perte OCR (« لو تملكون أنتم تملكون خزائن ») — réordonnée sur le texte d’Ibn ʿAṭiyya (« فالتقدير هنا قل لو تملكون خزائن ف﴿أنتم﴾ رفع على تبع الضمير »), noté.]</p>
<p>Et ﴿ <em>al-raḥma</em> ﴾ (“ la miséricorde ”) en ce verset : le bien et les grâces dispensés aux provisions — et de cela fut-elle nommée “ miséricorde ”. Et ﴿ <em>al-infāq</em> ﴾ (“ la dépense ”) : le sens connu — le départ du bien, qui conduit à l’indigence : le sens est donc la crainte de la suite de la dépense. Et dirent certains linguistes : <em>anfaqa l-rajul</em> (“ l’homme dépensa ”) — son sens : il s’appauvrit, comme tu dis : <em>ataraba</em> (“ il s’avanilla ”) et <em>aqtara</em> (“ il s’endetta ”).</p>
<p>[Vedettes « al-raḥma » et « al-infāq » restaurées d’après le texte d’Ibn ʿAṭiyya (« و«الرحمة» في هذه الآية… و﴿الإنفاق﴾ المعروف ذهاب المال ») : les emplacements imprimés sont vides — perte OCR.]</p>
<p>Et Sa parole : ﴿ <em>qatūran</em> ﴾ (“ avare ”) : retenant — Il veut que, en son naturel et au terme de son regard, les choses s’achèvent et périssent : s’il possédait les trésors de la miséricorde de Dieu, il retiendrait, par crainte de l’indigence — comme dit Dieu, le Très-Haut :</p>
<p>“ …ou ont-ils part au pouvoir ? — alors ils ne donneraient pas aux gens le plus petit poids… ” (an-Nisāʾ, 4:53 — extrait)</p>
<p>et comme dit le Glorifié :</p>
<p>“ Oui, l’homme fut créé d’impatience : quand le mal le touche, il s’affole ; et quand le bien le touche, il retient — hormis ceux qui prient. ” (al-Maʿārij, 70:19-22)</p>
<p>[Citation « qatūran » restaurée d’après le texte d’Ibn ʿAṭiyya (l’édition en ligne porte « فتورا » en ce lieu — coquille : le verset lit قتورا) ; citations « am lahum naṣībun mina l-mulki… » et « inna l-insāna khuliqa halūʿā… » restaurées d’après le corpus canonique : les emplacements imprimés sont vides — perte OCR ; le manuel imprime « an-Nisāʾ 4:52 » — la référence canonique est 4:53 (écart de numérotation noté) ; la référence « al-Maʿārij 70:19-22 » est conforme.]</p>
<p>De même il estime que la puissance de Dieu, le Très-Haut, s’arrête devant la résurrection — et la chose n’est point telle : Sa puissance ne s’achève point. Il invente de la création ce qu’Il veut, et invente de la miséricorde les provisions : Il ne craint point l’épuisement des trésors de Sa miséricorde.</p>
<p>Et attestent Sa générosité et Sa largesse, le Glorifié, ce qui vint en le hadith d’Abū Hurayra — qu’Allah l’agrée — : le Messager de Dieu — paix et bénédiction sur lui — dit : “ La main de Dieu est pleine : nulle dépense ne la tarit, ruisselante nuit et jour. Et Il dit : avez-vous vu ce qu’Il a dépensé depuis qu’Il créa les cieux et la terre ? Cela n’a point diminué ce qui est en Sa main. ” [Ṣaḥīḥ al-Bukhārī, Livre de l’Unicité, chapitre de Sa parole : ﴿ <em>lammā khalaqtu bi-yadayya</em> ﴾ (“ quand Je l’ai créé de Mes deux mains ”)]</p>
<p>[Hadith d’Abū Hurayra intact (le « ʿanhu » de <em>raḍiya llāhu ʿanhu</em> élidé par l’OCR — rendu normalement) ; réf. imprimée conforme.]</p>
<h3>Troisièmement : les finalités des versets</h3>
<p>Ces versets visent la réalisation d’une somme de finalités éducatives, dont :</p>
<ul>
<li>L’affirmation, par Dieu le Glorifié, de la survenance de la résurrection, par l’exposé que, comme Il a pu créer les cieux et la terre et l’homme la première fois — ce que les associateurs reconnaissent —, Il est, le Glorifié, capable de recréer l’homme et de le vivifier après sa mort, comme dit le Glorifié :</li>
</ul>
<p>“ …et c’est Lui qui commence la création puis la répète — et cela Lui est plus aiséré… ” (ar-Rūm, 30:27 — extrait)</p>
<ul>
<li>La grâce de Dieu, le Très-Haut, en Ses bienfaits sur Ses serviteurs, quand Il les patiente jusqu’à un terme connu — par miséricorde envers eux, et faveur de Sa part, le Glorifié, et espoir de leur droiture et de leur repentir.</li>
<li>Le rappel par Dieu, le Très-Haut, à Ses serviteurs, de Sa puissance qui ne s’achève point : Il invente de la miséricorde et des provisions ce qu’Il veut, comme Il invente de la création ce qu’Il veut.</li>
</ul>
<p>[Citation « wa-huwa lladhī yabdaʾu l-khalqa thumma yuʿīduhu wa-huwa ahwanu ʿalayhi » restaurée d’après le corpus canonique : l’emplacement imprimé est vide — perte OCR ; le manuel imprime « ar-Rūm 30:26 » — la référence canonique est 30:27 (écart de numérotation noté).]</p>
<h3>L’évaluation (taqwīm)</h3>
<ul>
<li>J’argumens à partir des deux versets de la survenance de la résurrection, exposant les illusions des associateurs à son sujet.</li>
<li>Quelle est la face de l’intensif en la qualification de l’homme d’avarice ?</li>
<li>Quel est l’effet de la foi en la résurrection et le compte, en la purification de l’âme et le profit d’autrui ?</li>
</ul>
<h3>L’investissement (istithmār)</h3>
<p>Al-Ṭāhir b. ʿĀshūr — Dieu lui fasse miséricorde — dit, en le commentaire de la parole de Dieu, le Très-Haut :</p>
<p>“ ﴿ al-ajal ﴾ (“ le terme ”) est ici susceptible de vouloir le temps qui fut établi, en la science de Dieu le Très-Haut, pour la survenance de la résurrection. Et la face de cette institution pour eux : qu’ils entrent en ce terme, car ils sont du nombre de ceux qui seront ressuscités alors — leur particularisation par la mention est qu’ils sont ceux qui nièrent la résurrection (…). Et il est loisible que le terme soit le terme de la vie — c’est-à-dire : et il fut donné à leur vie un terme — ce serait une seconde inférence de la résurrection : n’ont-ils point vu qu’Il leur donna un terme à leur vie ? Ce n’est que parce qu’Il les restituera à une autre vie qu’Il les fit être et vivifia, et donna à leur vie un terme — sinon, Il ne les eût point anéantis après les avoir vivifiés : car la sagesse exige que ce que fait être le Sage, Il s’attache à sa permanence et à sa non-péritnité. Cette pérition certaine ne fut donc qu’une pérition accidentelle, en vue d’un être plus grand que cet être-ci, et plus durable. ” [al-Taḥrīr wa-l-tanwīr, d’al-Ṭāhir Ibn ʿĀshūr : 15/222 — réf. imprimée « 15/222 », conforme]</p>
<p>[Citation d’Ibn ʿĀshūr intégrale et conforme.]</p>
<p>Je contemple le texte et réponds à ce qui suit :</p>
<ul>
<li>J’extrais du texte le sens du terme.</li>
<li>Comment peut-on arguer de la survenance de la résurrection à partir du texte ?</li>
</ul>
<h3>La préparation (iʿdād)</h3>
<p>Je contemple les versets 101 à 104 de la sourate al-Isrāʾ et réponds à ce qui suit :</p>
<ul>
<li>Je recherche la portée des expressions suivantes :</li>
</ul>
<p><em>bayyinātin</em> (بَيِّنَٰتٍ — manifestes, claires).</p>
<p><em>masḥūran</em> (مَسْحُورًۭا — ensorcelé).</p>
<p><em>baṣāʾira</em> (بَصَآئِرَ — preuves éclairantes).</p>
<p><em>mathbūran</em> (مَثْبُورًۭا — perdu, ruiné).</p>
<p><em>lafīfan</em> (لَفِيفًۭا — foule assemblée : groupe mêlé).</p>
<p>[Vedettes restituées du vocabulaire des versets 101-104 (gloses reconstituées d’après le lexique) : les emplacements imprimés sont vides — perte OCR. La leçon suivante du manuel (versets 101-104, leçon 26) ne figure pas dans le corpus du site : les documents suivants du livre sont l’index des figures et la bibliographie.]</p>
<ul>
<li>Les associateurs sont-ils touchés par les miracles dont Dieu, le Glorifié, soutient Ses messagers ?</li>
<li>Quel est le dessein de la mention, par Dieu le Très-Haut, de l’anéantissement de Pharaon et des siens, après qu’ils eurent traité de mensonge les miracles de Moïse ?</li>
</ul>"""


def main():
    with open(BOOK, "r", encoding="utf-8") as fh:
        d = json.load(fh)
    hit = 0
    for l in d["lessons"]:
        if l.get("docId") == "13738":
            l["htmlFr"] = HTML_FR
            hit += 1
    if hit != 1:
        raise SystemExit(f"ERREUR: {hit} leçons 13738 trouvées (attendu 1)")
    with open(BOOK, "w", encoding="utf-8") as fh:
        json.dump(d, fh, ensure_ascii=False, indent=1)
    print(f"OK — leçon 13738 upgradée main: FR {len(HTML_FR)} car")


if __name__ == "__main__":
    main()

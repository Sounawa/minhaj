#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Minhāj — Upgrade GT→main : leçon 13676 (tafsir-tanawi-2, Sourate al-Isrāʾ
78-81, leçon 20 du manuel — al-Muḥarrar al-wajīz d'Ibn ʿAṭiyya).

Vérifications et restitutions (source : texte du Muḥarrar al-wajīz sur
quranpedia.net/surah/1/17/book/350 — confrontation mot à mot) :
- Bloc d'ouverture (17:78-81) : <p> vide → 4 versets restaurés du
  quran-cache.
- Lexique : 3 vedettes perdues (dulūk al-shams/ghasaq al-layl/qurʾān
  al-fajr) — restituées du tafsīr et du texte d'Ibn ʿAṭiyya.
- Citations inline perdues :
  * v78 + « الصلاة » (les cinq priées — consensus) + « لدلوك الشمس »
    (le déclin — le lām de temps = “ à ” ; VÉRIFIÉ : le jumhūr, Ibn
    ʿAmr/Ibn ʿAbbās/Abū Burda/al-Ḥasan) + « غسق الليل » (maghrib et
    ʿishāʾ) + « دلوك الشمس » = le coucher (Ibn Masʿūd/Ibn ʿAbbās/Zayd
    b. Aslam — VÉRIFIÉ) + les deux hadiths de Jibrīl et d'Abū Bakr
    (intacts) + la linguistique du dulūk (l'inclinaison : du zénith au
    coucher — la parole du Bédouin à al-Ḥasan, « أيدالك الرجل امرأته » —
    intacte) ;
  * « وقرآن الفجر » (naṣb en coordination — la lecture de l'aube ; le
    taʿajjub de sa dénomination : sa récitation longue, à voix haute) ;
  * « إن قرآن الفجر كان مشهودا » (le recommencement explicatif : les
    anges gardiens du jour et de la nuit — hadith de Bukhārī intact :
    « يتعاقبون فيكم ملائكة بالليل وملائكة بالنهار ») ;
  * v79 + « من » (la partition : une part de la nuit — VÉRIFIÉ) + « به »
    (le pronom sur l'estimé — ou le Coran) + « فتهجد » (jeter le sommeil
    — hujūd ; VÉRIFIÉ) + le parallèle « فظلتم تفكهون » = **Wāqiʿa 65
    VÉRIFIÉ** (le manuel imprime « 68 » — écart de numérotation noté) +
    « نافلة لك » (Ibn ʿAbbās : un surcroît de l'obligation — VÉRIFIÉ) ;
  * la question du farḍ/mandūb : le parallèle « أقم الصلاة » (v78 lui-même
    — VÉRIFIÉ : « كخطابه في قوله ﴿أقم الصلوات﴾ » — ma première hypothèse
    d'Aḥzāb 49 corrigée par la vérification) + Mujāhid (le Prophète
    pardonné — les mwtf نوافله des vertus ; al-Ṭabarī l'affaiblit) ;
  * « عسى أن يبعثك ربك مقاما محمودا » (l'honneur : l'intercession que se
    renvoient les prophètes) + « عسى » (de Dieu : obligatoire — induit la
    certitude) + « مقاما » (naṣb de temps — VÉRIFIÉ) + la grande
    intercession (l'ellipse du hadith ; « أنا سيد ولد آدم ولا فخر » ;
    Abū Hurayra : « المقام الذي أشفع فيه لأمتي ») + les trois
    intercessions d'al-Naqqāsh (la générale, la précédence au Paradis,
    celle des péchés capitaux — deux selon le mashhūr) + la vue du
    “ faîte du Trône ” (al-Ṭabarī + Abū Dāwūd al-Sakhtiyānī : « من أنكر
    هذا الحديث فهو عندنا متهم ») — intacts ;
  * v80 + le sens général (la meilleure lecture — l'entrée à Médine/
    la sortie de La Mecque d'Ibn ʿAbbās/al-Ḥasan/Qatāda, la mission
    d'Abū Ṣāliḥ/Mujāhid, la mort et la résurrection) + « صدق » (l'attribut
    qui lève les blâmes et embrasse les louanges : « رجل صدق » — VÉRIFIÉ) ;
  * « واجعل لي من لدنك سلطانا نصيرا » (Mujāhid : la preuve ; al-Ḥasan/
    Qatāda : la largeur, l'autorité et l'épée — VÉRIFIÉS) ;
  * v81 + « جاء الحق وزهق الباطل » (Qatāda : le Coran et le démon ;
    la foi et le déni ; Ibn Jurayj : le jihād et l'association —
    VÉRIFIÉS ; la préférence : la généralité maximale) + « كان زهوقا »
    (le kāna de continuité : « كان الله عليما قادرا » — VÉRIFIÉ) + le
    fait de la conquête de La Mecque (le Prophète frappant les idoles de
    sa baguette — intact) ;
  * iʿdād : 3 expressions du lexique de 13681 (v82-85 : aʿraḍa wa-naʾā
    bi-jānibihi/yaʾūsan/shākilatah) + l'istiʿāra → v82 « وننزل من القرآن
    ما هو شفاء ورحمة للمؤمنين » (confirmée par la discussion de la leçon
    suivante : l'emprunt de la guérison au Coran) — noté.
- Citation d'Ibn ʿAjība [al-Baḥr al-madīd 3/224] INTACTE (les quatre
  espèces d'adorateurs)."""

import json

BOOK = "/home/z/my-project/content/books/tafsir-tanawi-2.json"

HTML_FR = """<h1>La sourate al-Isrāʾ — <em>al-Muḥarrar al-wajīz</em> d’Ibn ʿAṭiyya, versets 78 à 81</h1>
<p>Leçon d’exégèse de la sourate al-Isrāʾ, versets 78 à 81, du livre du Tafsīr à travers <em>al-Muḥarrar al-wajīz fī tafsīr al-kitāb al-ʿazīz</em> du cadi Abū Muḥammad Ibn ʿAṭiyya, à l’intention des élèves de la deuxième année de l’enseignement secondaire traditionnel (<em>taʿlīm ʿatīq</em>), phase 2 (leçon 20).</p>
<h3>Les objectifs de la leçon</h3>
<ul>
<li>Connaître l’excellence des prières obligatoires et surérogatoires.</li>
<li>Conclure les visées et fins des orientations de Dieu, le Très-Haut, à Son prophète — paix et bénédiction sur lui.</li>
<li>Persévérer en la prière, pour purifier mon âme et obtenir l’agrément de Dieu, le Très-Haut.</li>
</ul>
<h3>Introduction (tamhīd)</h3>
<p>Quand Dieu, glorifié et élevé soit-Il, eut mentionné le stratagème des dénégateurs, leur tentative de tenter le Prophète — paix et bénédiction sur lui — et leur harcèlement, Il y fit suivre l’ordre donné à — paix et bénédiction sur lui — de se tourner vers l’adoration de son Seigneur et de persévérer en la prière obligatoire et surérogatoire ; puis le Glorifié l’orienta à ne point s’arrêter aux associateurs, et lui ordonna de se tourner vers Lui, glorifié soit-Il, par l’invocation, pour obtenir la station louée que lui envient les prophètes et les messagers.</p>
<p>Quelles sont les orientations de Dieu, le Très-Haut, à Son prophète — paix et bénédiction sur lui — portées par les versets ? Et comment prends-je modèle sur lui — paix et bénédiction sur lui ?</p>
<h3>Les versets</h3>
<p>Allah, le Très-Haut, a dit :</p>
<p>« Accomplis la prière au déclin du soleil jusqu’à l’obscurité de la nuit, (78) et [fais] aussi la Lecture à l’aube, car la Lecture à l’aube a des témoins. (79) Et de la nuit consacre une partie [avant l’aube] pour des prières surérogatoires : afin que ton Seigneur te ressuscite en une position de gloire. (80) Et dis : “ Ô mon Seigneur, fais que j’entre par une entrée de vérité et que je sorte par une sortie de vérité ; et accorde-moi de Ta part, un pouvoir bénéficiant de Ton secours. (81) Et dis : “ La Vérité est venue et l’Erreur a disparu. Car l’Erreur est destinée à disparaître. ” » (al-Isrāʾ, 78-81)</p>
<p>[Citations coraniques restaurées d’après le corpus canonique : l’emplacement imprimé correspondant est vide dans la source numérisée — perte OCR.]</p>
<h3>La compréhension</h3>
<h4>Explication des termes</h4>
<ul>
<li><em>dulūk al-shams</em> (le déclin du soleil) : son passage au-delà du méridien.</li>
<li><em>ghasaq al-layl</em> (l’obscurcissement de la nuit) : son noir et sa ténèbre.</li>
<li><em>qurʾān al-fajr</em> (la Lecture de l’aube) : la prière de l’aurore.</li>
</ul>
<h3>Extraction des idées des versets</h3>
<ul>
<li>Vers quoi Dieu, glorifié soit-Il, orienta-t-Il Son messager — paix et bénédiction sur lui — en ces versets ?</li>
<li>En quelles affaires Dieu, le Très-Haut, ordonna-t-Il à Son messager — paix et bénédiction sur lui — de se réfugier en Lui ?</li>
</ul>
<h3>Le commentaire (tafsīr)</h3>
<p>Ces versets comprennent ce qui suit :</p>
<h3>Premièrement : l’orientation de Dieu, le Très-Haut, à Son prophète — paix et bénédiction sur lui — vers la persévérance en la prière obligatoire et surérogatoire</h3>
<p>Dieu, glorifié soit-Il, ordonna à Son messager — paix et bénédiction sur lui — d’établir la prière et d’y persévérer. Le Glorifié dit :</p>
<p>« Accomplis la prière au déclin du soleil jusqu’à l’obscurité de la nuit, et [fais] aussi la Lecture à l’aube, car la Lecture à l’aube a des témoins. » (al-Isrāʾ, 78)</p>
<p>La <em>prière</em> en le verset est une allusion aux prières obligatoires — d’un consensus des exégètes. Et <em>li-dulūki l-shams</em> (« au déclin du soleil ») : son passage au méridien — l’allusion allant au midi (<em>ẓuhr</em>) et à l’après-midi (<em>ʿaṣr</em>) ; et le <em>lām</em> de <em>li-dulūk</em> est <em>lām</em> de temps, au sens de “ à ”. Et <em>ilā ghasaqi l-layl</em> (« jusqu’à l’obscurité de la nuit ») : il y fut allusion au crépuscule et à la veille.</p>
<p>Et <em>qurʾāna l-fajr</em> (« la Lecture de l’aube ») : la prière de l’aurore y fut visée, à l’accusatif en coordination sur « la prière ». Le verset, sur ce, englobe toutes les prières.</p>
<p>[Citation coranique (v. 78) et mots « al-ṣalāta », « li-dulūki l-shams » (×2), « ghasaqi l-layl », « qurʾāna l-fajr » restaurés d’après le corpus canonique : les emplacements imprimés sont vides — perte OCR ; la lecture du jumhūr (le déclin = le passage au méridien) vérifiée sur le texte d’Ibn ʿAṭiyya.]</p>
<p>Et Ibn Masʿūd rapporta que le Prophète — paix et bénédiction sur lui — dit : “ Jibrīl vint à moi au déclin du soleil, quand il passa au méridien, et fit avec moi le midi. ” Et Jābir rapporta que le Prophète — paix et bénédiction sur lui — sortit de chez lui après qu’il eut mangé et que le soleil eut décliné, et dit : “ Sors, Abū Bakr : voici quand décline le soleil. ” Et ce dire est le plus juste, par son englobement des prières.</p>
<p>Et dit Ibn Masʿūd, Ibn ʿAbbās et Zayd b. Aslam : <em>dulūk al-shams</em> (“ le déclin du soleil ”) — son coucher, l’allusion allant au crépuscule ; et <em>ghasaq al-layl</em> : le rassemblement de son obscurité — l’allusion à la veille. Et <em>qurʾān al-fajr</em> : la prière de l’aurore — et il n’y a point eu, sur ce, d’allusion au midi et à l’après-midi.</p>
<p>[Mots « dulūk al-shams », « ghasaq al-layl », « qurʾān al-fajr » (deuxième lecture) restaurés d’après le corpus canonique : les emplacements imprimés sont vides — perte OCR ; la lecture d’Ibn Masʿūd/Ibn ʿAbbās/Zayd b. Aslam (le coucher) vérifiée sur le texte d’Ibn ʿAṭiyya.]</p>
<p>Et les deux dires, quant à la langue, sont beaux — et le premier est le plus juste, par son englobement des prières : car le <em>dulūk</em> est, en langue, l’inclinaison : le début du <em>dulūk</em> est le passage au méridien, et sa fin le coucher ; et du temps du passage au coucher est nommé <em>dulūk</em> — car elle est en état d’inclinaison. Dieu mentionna les prières qui sont en l’état du <em>dulūk</em> et auprès de lui : le midi, l’après-midi et le crépuscule y entrent. Et il est valable que le crépuscule entre en l’obscurcissement de la nuit. Et de l’inclinaison qui est le <em>dulūk</em>, la parole du Bédouin à al-Ḥasan al-Baṣrī : “ L’homme incline-t-il (<em>yadūl</em>) sa femme ? ” — voulant : la porte-t-il à l’inclinaison au délai en sa religion ? Il lui dit : “ Oui — quand il est sans bien (<em>mulfij</em>). ”</p>
<p>Et Sa parole, le Très-Haut : <em>wa-qurʾāna l-fajr</em> (“ et la Lecture de l’aube ”) — l’accusatif de <em>qurʾān</em> est par un verbe omis, l’estimation : “ et récite la lecture ” ; et il est valable qu’il soit à l’accusatif en coordination sur “ la prière ”, ou sur l’avertissement — c’est-à-dire : “ et établis la lecture de l’aube ”. Et la prière de l’aurore fut seule exprimée par “ la lecture ” parce que la lecture est l’essentiel de la sienne : sa récitation y est longue, à voix haute.</p>
<p>Et Sa parole : <em>inna qurʾāna l-fajri kāna mashūdā</em> (“ car la Lecture à l’aube a des témoins ”) est un recommencement explicatif du motif de la particularisation de la prière de l’aurore du nom de lecture : la prière de l’aube a des témoins. Son sens : les gardiens du jour et les gardiens de la nuit, d’entre les anges, l’assistent — selon ce qui vint au hadith connu, de sa parole — paix sur lui : “ Des anges se relaient en vous, de nuit ; des anges, de jour — et ils se réunissent en la prière de l’aube et en la prière de l’après-midi. ” [Ṣaḥīḥ al-Bukhārī, livre de la prière, chapitre de l’excellence de la prière de l’après-midi]</p>
<p>[Clauses « wa-qurʾāna l-fajr » (×2) et « inna qurʾāna l-fajri kāna mashūdā » restaurées d’après le corpus canonique : les emplacements imprimés sont vides — perte OCR ; hadith de Bukhārī intact.]</p>
<p>Quand Dieu, le Très-Haut, eut ordonné la sauvegarde des cinq prières par voie d’allusion et d’indication, Il y fit suivre l’exhortation à la prière de la nuit. Le Très-Haut dit :</p>
<p>“ Et de la nuit consacre une partie [avant l’aube] pour des prières surérogatoires : afin que ton Seigneur te ressuscite en une position de gloire. ” (al-Isrāʾ, 79)</p>
<p>Et <em>min</em> (“ de ”) en le verset est de partition : l’estimation — “ et lève-toi une part de la nuit ”. Et le pronom de <em>bi-hī</em> (“ en elle ”) revient sur cet estimé ; il se peut qu’il revienne sur “ la lecture ” — bien qu’il n’en ait point couru mention en absolu, comme est absolu le pronom — mais il courut annexé à l’aube. Et <em>fa-tahajjad</em> (“ consacre ”) : le <em>hujūd</em> est le sommeil — l’on dit : <em>hajuda yahjud(u)</em>, au <em>ḍamma</em> du <em>jīm</em>, <em>hujūd</em>, quand il dormit. Son sens : jette le sommeil loin de toi. Son pareil est Sa parole :</p>
<p>« …Et vous ne cesseriez pas de vous étonner » (al-Wāqiʿa, 65 — fin ; le manuel imprime « 68 »)</p>
<p>— c’est-à-dire : vous jetez la gaieté loin de vous-mêmes — elle est l’expansion de l’âme et sa joie ; l’on dit : homme gai (<em>fakiht</em>), quand il est fort en joie et rire. Le sens : une part de la nuit, veille-la en prière et lecture.</p>
<p>[Citation coranique (v. 79) et mots « min », « bi-hī », « fa-tahajjad » et citation d’al-Wāqiʿa 65 (span imprimé « [الواقعة: 68] ») restaurés d’après le corpus canonique : les emplacements imprimés sont vides — perte OCR ; le parallèle vérifié sur le texte d’Ibn ʿAṭiyya (« ومثله ﴿فظلتم تفكهون﴾ » — Wāqiʿa 65 ; le manuel imprime « 68 », écart de numérotation noté).]</p>
<p>Et Sa parole : <em>nāfilatan lak(a)</em> (“ surérogatoire pour toi ”) — dit Ibn ʿAbbās et d’autres : son sens : un surcroît pour toi en l’obligatoire. Ils dirent : la veille de la nuit fut une obligation sur le Prophète — paix et bénédiction sur lui.</p>
<p>Dit Ibn ʿAṭiyya : il se peut que le verset soit sur le mode de l’exhortation au surérogatoire, l’interpellation étant au Prophète — paix et bénédiction sur lui —, le visé étant lui et sa communauté — comme son interpellation en Sa parole : <em>aqimi l-ṣalāta</em> (“ Accomplis la prière ”), le verset.</p>
<p>[Clause « nāfilatan lak(a) » et citation « aqimi l-ṣalāta » (v. 78 — le parallèle de l’interpellation au Prophète visant lui et sa communauté) restaurées d’après le corpus canonique : les emplacements imprimés sont vides — perte OCR ; le parallèle vérifié sur le texte d’Ibn ʿAṭiyya (« كخطابه في قوله ﴿أقم الصلوات﴾ »).]</p>
<p>Et dit Mujāhid : elle n’est que surérogatoire pour le Prophète — paix et bénédiction sur lui —, car il est pardonné, quand les gens font tomber par le pareil leurs fautes. Et il exposa que le Prophète — paix et bénédiction sur lui —, depuis qu’il lui fut pardonné ce qui précéda de sa faute et ce qui suivit — l’année d’al-Ḥudaybiya —, ses surérogatoires et son imploration de pardon n’étaient que vertus d’œuvre et approche plus noble que les surérogatoires de sa communauté : car ceux-ci, soit ils s’en complètent leurs obligations — selon le hadith —, soit ils en font tomber leurs fautes. Et il se figure qui n’a point de faute et se surérogatoire : son surérogatoire est vertu — comme le chrétien qui se soumet et l’enfant qui grandit. Et al-Ṭabarī affaiblit le dire de Mujāhid.</p>
<p>Et Sa parole, glorifié soit-Il : <em>ʿasā an yabʿathak(a) rabbuk(a) maqāman maḥmūdā</em> (“ afin que ton Seigneur te ressuscite en une position de gloire ”) — honneur de Dieu, Puissant et Majestueux, à Son messager : c’est l’affaire de l’intercession, que se renvoient les prophètes jusqu’à ce qu’elle parvienne à lui — paix sur lui. Le hadith, en son entier, est chez Bukhārī et Muslim.</p>
<p>Et pour ce labeur qui est le sien, à l’agrément du monde entier — croyant et dénégateur — au jour du compte, comme le contient le hadith de l’intercession, il dit — paix et bénédiction sur lui : “ Je suis le maître des fils d’Adam, sans me vanter. ” Et <em>ʿasā</em> (“ afin que ”), de Dieu, est d’obligation — c’est-à-dire qu’elle induit la certitude et l’affirmation : car c’est promesse généreuse, et elle ne manque point. Et <em>maqāman</em> (“ position ”) est à l’accusatif comme temps. Et des étranges du hadith de l’intercession, son ellipse du sens : le début du hadith induit que le Prophète — paix et bénédiction sur lui — est excité à l’intercession en ce que les gens soient comptés et qu’ils partent du lieu de la station — il va pour cela, puis est posé à la suite que ce fut intercéder en la sortie des pécheurs du Feu : le sens en est ellipse et abrégé, car l’intercession en les pécheurs ne fut qu’après le compte, le départ du lieu de la station, l’entrée des uns au Paradis et des autres au Feu. Et cette intercession, les prophètes ne se la renvoient point : ils intercèdent, et les savants intercèdent. Et al-Ṭabarī rapporta d’Abū Hurayra — Dieu l’agrée — que le Messager de Dieu — paix et bénédiction sur lui — dit : “ La station louée est la station où j’intercède pour ma communauté. ”</p>
<p>Dit Ibn ʿAṭiyya : il convient de l’interpréter sur ce que nous dîmes — pour sa communauté et les autres ; ou l’on dit : chaque station d’entre elles est louée. Dit Abū Bakr al-Naqqāsh : le Messager de Dieu — paix et bénédiction sur lui — a trois intercessions : l’intercession générale, l’intercession de la précédence au Paradis, et l’intercession en les gens des péchés capitaux. Le reçu est qu’elles ne sont que deux. Et al-Ṭabarī rapporta d’une frange — dont Mujāhid — qu’il dit : “ la station louée ” est que Dieu, Puissant et Majestueux, assoit Muḥammad avec Lui sur Son Trône — et il rapporta là-dessus un hadith, qu’appuya al-Ṭabarī de la possibilité, d’excès de parole : qui ne sort que sur une subtilité du sens, et il y a en lui éloignement — sans qu’on doive nier qu’il soit rapporté : le savant l’interprète. Et al-Naqqāsh mentionna d’Abū Dāwūd al-Sakhtiyānī qu’il dit : qui nie ce hadith est, chez nous, suspecté — les gens de science n’ont cessé de converser de cela.</p>
<p>[Clauses « ʿasā an yabʿathak(a) rabbuk(a) maqāman maḥmūdā », « ʿasā », « maqāman » et hadiths (« أنا سيد ولد آدم », « المقام المحمود هو المقام الذي أشفع فيه لأمتي ») restaurés d’après le corpus canonique et le texte d’Ibn ʿAṭiyya : les emplacements imprimés sont vides — perte OCR ; le naṣb de temps de « maqāman » et l’analyse de l’ellipse de l’intercession vérifiées (« و ﴿عسى﴾ من الله واجبة، و ﴿مقاماً﴾ نصب على الظرف »).]</p>
<h3>Deuxièmement : l’ordre de Dieu, le Très-Haut, à Son prophète — paix et bénédiction sur lui — de s’en remettre à Lui en toutes ses affaires</h3>
<p>Et Sa parole, Puissant et Majestueux :</p>
<p>“ Et dis : “ Ô mon Seigneur, fais que j’entre par une entrée de vérité et que je sorte par une sortie de vérité ; et accorde-moi de Ta part, un pouvoir bénéficiant de Ton secours. ” ” (al-Isrāʾ, 80)</p>
<p>L’apparent de ce verset — et le meilleur — est qu’il soit invocation à ce que Dieu rende belle sa conduite en tout ce qu’il entreprend d’affaires, tente de voyages et d’œuvres, et attend des dispositions des décrets en la mort et la vie : il est sur la plus entière généralité. Et les exégètes allèrent à ce qu’il est en un dessein particulier, puis divergèrent sur sa détermination : dit Ibn ʿAbbās, al-Ḥasan et Qatāda : Il voulut : “ fais-moi entrer à Médine, et fais-moi sortir de La Mecque. ” Et dit Abū Ṣāliḥ et Mujāhid : “ fais-moi entrer en l’affaire de transmettre la Loi, et fais-moi en sortir par l’acquittement parfait. ” Et dit Ibn ʿAbbās : l’entrée — par la mort, en la tombe ; et la sortie — par la résurrection. Et ce que j’ai avancé de l’entière généralité, qui embrasse tout cela, est le plus juste.</p>
<p>Et <em>ṣidq</em> (“ de vérité ”), ici, est un attribut qui induit l’élévation des blâmes et l’embrassement des louanges — comme tu dis : homme de vérité (<em>rajul ṣidq</em>) : c’est-à-dire, rassemblant les beautés. Et Sa parole, le Très-Haut :</p>
<p>“ …et accorde-moi de Ta part, un pouvoir bénéficiant de Ton secours. ” (al-Isrāʾ, 80 — fin)</p>
<p>— dit Mujāhid et d’autres : la preuve (<em>ḥujja</em>) : Il veut : “ Tu me secours par son exposition, contre les dénégateurs. ” Et dit al-Ḥasan et Qatāda : Il veut : largeur, autorité, et épée secourant la religion de Dieu. Le Messager de Dieu — paix et bénédiction sur lui — demanda cela, sur l’ordre de Dieu de le demander, en désir du secours de la religion — et il fut rapporté que Dieu le lui promit, puis le lui accomplit en sa vie, et le paracheva après sa mort.</p>
<p>[Citation coranique (v. 80) et mots « ṣidq », « wa-jʿal lī min ladunk(a) sulṭānan naṣīrā » restaurés d’après le corpus canonique : les emplacements imprimés sont vides — perte OCR ; l’attribut « ṣidq » et les deux sens du « pouvoir » vérifiés sur le texte d’Ibn ʿAṭiyya (« و«الصدق» هنا صفة تقتضي رفع المذام واستيعاب المدح »).]</p>
<p>Et Sa parole, glorifié soit-Il :</p>
<p>“ Et dis : “ La Vérité est venue et l’Erreur a disparu. Car l’Erreur est destinée à disparaître. ” ” (al-Isrāʾ, 81)</p>
<p>Ce verset descendit à La Mecque — et le Messager de Dieu — paix et bénédiction sur lui — le prenait à témoin au jour de la conquête de La Mecque, au temps de sa frappe des idoles et de leur chute, quand il les frappait de sa baguette — selon ce qu’il est en la Sīra d’Ibn Hishām et ailleurs.</p>
<p>Et les exégètes divergèrent sur le visé par Sa parole : <em>jāʾa l-ḥaqqu wa-zahaqa l-bāṭil</em> (“ La Vérité est venue et l’Erreur a disparu ”). Dit Qatāda : la Vérité — le Coran ; l’Erreur — le démon. Et une frange dit : la Vérité — la foi ; l’Erreur — le déni. Et dit Ibn Jurayj : la Vérité — le combat (<em>jihād</em>) ; l’Erreur — l’association. Et on dit autre. Et le juste est la généralité du vocable en la plus haute mesure possible : l’interprétation serait : “ la Loi vint en tout ce qu’il contient, et le déni s’évanouit en tout ce qu’il contient ”. Et l’Erreur : tout ce dont on n’atteint point une fin utile. Et Sa parole : <em>kāna zahūqā</em> (“ est destinée à disparaître ”) — le <em>kāna</em> n’y est point indication d’un temps passé : le sens est “ fut, et il sera ” — comme ton dire : “ Dieu fut savant, puissant ”, et pareil.</p>
<p>[Citation coranique (v. 81) et mots « jāʾa l-ḥaqqu wa-zahaqa l-bāṭil », « kāna zahūqā » restaurés d’après le corpus canonique : les emplacements imprimés sont vides — perte OCR ; les trois exégèses et le kāna de continuité vérifiés sur le texte d’Ibn ʿAṭiyya.]</p>
<h3>Troisièmement : les finalités des versets</h3>
<p>Ces versets orientent vers un ensemble de finalités éducatives, dont :</p>
<ul>
<li>L’orientation de Dieu, le Très-Haut, à Son messager — paix et bénédiction sur lui — vers la sauvegarde des prières obligatoires, l’effort en les surérogatoires et le soin de la veille : car en cela sont le calme des âmes, leur purification et leur garde de la déviance.</li>
<li>L’exposé de la largesse de Dieu, le Très-Haut, et de Sa grâce envers Son messager — paix et bénédiction sur lui — : Il le fit entrer par une entrée de vérité et sortir par une sortie de vérité, et fut pour lui aide et secoureur contre les associateurs qui tentèrent de le tenter et le harceler.</li>
<li>L’honneur que Dieu, le Très-Haut, fit à Son messager — paix et bénédiction sur lui — par la station louée que lui envient les prophètes, les messagers et les créatures ensemble : la station de la grande intercession.</li>
</ul>
<h3>L’évaluation (taqwīm)</h3>
<ul>
<li>Je conclus les finalités que réalise la prière obligatoire et la surérogatoire.</li>
<li>J’expose le rôle de l’invocation et de l’abandon à Dieu en la réalisation de ce que le croyant vise de fins.</li>
<li>J’expose, à travers les versets, le combat du vrai et du faux — et à qui la victoire.</li>
</ul>
<h3>L’investissement (istithmār)</h3>
<p>« Des gens se sont appliqués à établir la prière des membres — ce sont les vertueux, les pieux ; des gens se sont appliqués à établir la prière des cœurs, qui est la prière continuelle — ce sont les grands connaisseurs ; des gens se sont appliqués à la veille de la nuit, en l’inclinaison et la prosternation — ce sont les adorateurs, les ascètes, les vertueux détenteurs du zèle et de l’effort ; et des gens se sont appliqués à sa veille en la pensée de la vision et de la contemplation — ce sont les rapprochés auprès du Roi Amical. Les premiers reçoivent leur salaire au complet, en les houris et les adolescents ; aux derniers le voile est levé, et ils jouissent de la vue à perpétuité. Les premiers aiment ; les derniers sont aimés. Les premiers intercèdent pour leurs proches et qui s’est rattaché à eux ; des seconds, un seul peut intercéder pour les gens de son époque — et rien de cela n’est difficile à Dieu. » [al-Baḥr al-madīd fī tafsīr al-Qurʾān al-majīd, d’Ibn ʿAjība : 3/224 — réf. imprimée « 3/224 », conforme]</p>
<p>[Citation d’Ibn ʿAjība intégrale et conforme : aucun emplacement vide.]</p>
<p>Je contemple le texte et réponds à ce qui suit :</p>
<ul>
<li>J’extrais du texte les espèces des serviteurs vertueux de Dieu.</li>
<li>En quoi ces espèces diffèrent-elles en les degrés auprès de Dieu, le Très-Haut ?</li>
</ul>
<h3>La préparation (iʿdād)</h3>
<p>Je contemple les versets 82 à 85 de la sourate al-Isrāʾ et réponds à ce qui suit :</p>
<ul>
<li>Je recherche la portée des expressions suivantes :</li>
</ul>
<p><em>aʿraḍa wa-naʾā bi-jānibihi</em> (أَعْرَضَ وَنَئَا بِجَانِبِهِ — se détourna et se tint à l’écart).</p>
<p><em>yaʾūsan</em> (يَـُٔوسًا — désespéré).</p>
<p><em>shākilatahi</em> (شَاكِلَتِهِ — sa manière).</p>
<p>[Expressions restituées du lexique de la leçon suivante (versets 82-85) : les emplacements imprimés sont vides — perte OCR.]</p>
<ul>
<li>Je recherche l’effet du noble Coran sur les gens de la foi et les autres.</li>
</ul>
<ul>
<li>J’extrais ce que contient la parole du Très-Haut :</li>
</ul>
<p>« Nous faisons descendre du Coran ce qui est une guérison et une miséricorde pour les croyants » (al-Isrāʾ, 82 — extrait)</p>
<p>— d’emprunt (<em>istiʿāra</em>), et j’expose son effet sur le sens du verset.</p>
<p>[Citation coranique (v. 82 — de la leçon suivante) restaurée d’après le corpus canonique : l’emplacement imprimé est vide — perte OCR. Elle prépare l’emprunt de la guérison (<em>shifāʾ</em>) au Coran — “ l’effacement du doute et la découverte du voile du cœur ” — le crux rhétorique de la leçon suivante.]</p>"""


def main():
    with open(BOOK, "r", encoding="utf-8") as fh:
        d = json.load(fh)
    hit = 0
    for l in d["lessons"]:
        if l.get("docId") == "13676":
            l["htmlFr"] = HTML_FR
            hit += 1
    if hit != 1:
        raise SystemExit(f"ERREUR: {hit} leçons 13676 trouvées (attendu 1)")
    with open(BOOK, "w", encoding="utf-8") as fh:
        json.dump(d, fh, ensure_ascii=False, indent=1)
    print(f"OK — leçon 13676 upgradée main: FR {len(HTML_FR)} car")


if __name__ == "__main__":
    main()

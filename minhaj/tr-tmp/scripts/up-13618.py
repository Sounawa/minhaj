#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Minhāj — Upgrade GT→main : leçon 13618 (tafsir-tanawi-2, Sourate al-Isrāʾ
45-48, leçon 13 du manuel — al-Muḥarrar al-wajīz d'Ibn ʿAṭiyya).

Vérifications et restitutions (source : texte du Muḥarrar al-wajīz sur
quranpedia.net/surah/1/17/book/350 — confrontation mot à mot) :
- Bloc d'ouverture (17:45-48) : <p> vide après « الآيات » → restauré du
  quran-cache (4 versets).
- Citations inline perdues par l'OCR :
  * v45 complet après « قال تعالى : » (1er § du tafsīr) ;
  * clause « وإذا قرأت القرآن » (glossée : « شرعت وتلبست بقراءة القرآن ») ;
  * mot « مستورا » (naʿt du voile / بمعنى ساتر / المبالغة — الأخفش et
    l'objection du cadi Abū Muḥammad) ;
  * v46 complet après « قال تعالى : » (2e section) ;
  * « أن يفقهوه » (maṣdar mawʾūl : كراهة أن / منع أن — VÉRIFIÉ en ligne :
    « وقوله ﴿أن يفقهوه﴾ ﴿أن﴾ نصب على المفعول ») ;
  * clause « وإذا ذكرت ربك في القرآن وحده ولووا على أدبارهم نفورا »
    (l'histoire d'Abū Ṭālib et « قولوا لا إله إلا الله تملكون بها العرب ») ;
  * mot « نفورا » (maṣdar en ḥāl ou pluriel de nāfir — VÉRIFIÉ) ;
  * « ولوا على أدبارهم نفورا » (la lecture des démons rapportée d'al-Ṭabarī
    — VÉRIFIÉ : « إنما عنى بقوله ﴿ولوا على أدبارهم نفوراً﴾ الشياطين ») ;
  * « نحن أعلم بما يستمعون به » (v47a) + « به » (pronom renvoyant à « ما »
    au sens de « الذي » — VÉRIFIÉ) + « ما » ;
  * « إذ » (l'opérateur du premier إذ et du conjoint = le premier
    « يستمعون » — VÉRIFIÉ) ;
  * « وإذ هم نجوى » ×2 (description par le maṣdar comme « قوم رضا وعدل » ;
    le sens : la tenue de conseil en Dār al-Nadwa — VÉRIFIÉ ×2) ;
  * « مسحورا » (de siḥr par kasra) + « به جنة » = Muʾminūn 25 (VÉRIFIÉ :
    « شبيهة بقول بعضهم ﴿به جنة﴾ [المؤمنون: ٢٥] ») ;
  * v48 complet (« ثم قال تعالى ») ;
  * « فلا يستطيعون سبيلا » (les deux sens) + span [الإسراء: 46] rempli de
    « وجعلنا على قلوبهم أكنة » (l'édition en ligne imprime à tort
    [الأنعام: ٢٥] — la note du texte en ligne renvoie à Isrāʾ 46 : le manuel
    a la réf correcte) ;
  * istithmār : v179 al-Aʿrāf (le <p> vide + le span [الأعراف: 179]) ;
  * iʿdād : 4 expressions restituées du lexique de la leçon suivante
    (13619, v49-55 : rufātan/jadīdan/fatarakum/al-nazgh) ; citation à
    expliciter → v53 (le différend Sībawayh/al-Akhfash sur « يقولوا » —
    crux grammatical de la leçon suivante) — noté.
- Hadith « إذا نودي بالصلاة أدبر الشيطان له حصاص » : intact dans la source
  (Bukhārī/Muslim — le ḥiṣāṣ : le trot véloce, dit aussi le vent, note)."""

import json

BOOK = "/home/z/my-project/content/books/tafsir-tanawi-2.json"

HTML_FR = """<h1>La sourate al-Isrāʾ — <em>al-Muḥarrar al-wajīz</em> d’Ibn ʿAṭiyya, versets 45 à 48</h1>
<p>Leçon d’exégèse de la sourate al-Isrāʾ, versets 45 à 48, du livre du Tafsīr à travers <em>al-Muḥarrar al-wajīz fī tafsīr al-kitāb al-ʿazīz</em> du cadi Abū Muḥammad Ibn ʿAṭiyya, à l’intention des élèves de la deuxième année de l’enseignement secondaire traditionnel (<em>taʿlīm ʿatīq</em>), phase 2 (leçon 13).</p>
<h3>Les objectifs de la leçon</h3>
<ul>
<li>Connaître l’égarement des associateurs et le scellement de leurs cœurs contre le profit du noble Coran.</li>
<li>Conclure comment les associateurs raillaient le Livre de Dieu et calomniaient Son messager.</li>
<li>Incarner les enseignements du noble Coran — doctrine, culte et conduite.</li>
</ul>
<h3>Introduction (tamhīd)</h3>
<p>Après que Dieu, Puissant et Majestueux, eut exposé ce que le Coran apporte des fondements de la doctrine, des capitales des œuvres, et ce qui s’y entremêle d’exhortations et de leçons, Il avertit ici de la protection que Dieu, le Très-Haut, accorde à Son prophète, du détour des associateurs envers le Coran, de leur non-profit de sa guidance et de ses exhortations, de leur répulsion envers lui et de leurs moqueries : ils frappèrent au Prophète — paix et bénédiction sur lui — des paraboles, disant de lui tantôt : c’est un sorcier ; tantôt : c’est un possédé ; tantôt : c’est un poète — parce que Dieu scella leurs cœurs et leur ouïe, et plaça sur leurs yeux une pellicule.</p>
<p>Quel fut donc l’attitude des associateurs envers le noble Coran ? Et pourquoi n’y crurent-ils point et ne se guidèrent-ils point de sa guidance ?</p>
<h3>Les versets</h3>
<p>Allah, le Très-Haut, a dit :</p>
<p>« Et quand tu lis le Coran, (45) Nous plaçons, entre toi et ceux qui ne croient pas en l’au-delà, un voile invisible. (46) Nous avons mis des voiles sur leurs cœurs, de sorte qu’ils ne le comprennent pas : et dans leurs oreilles, une lourdeur. Et quand, dans le Coran, tu évoques Ton Seigneur l’Unique, ils tournent le dos par répulsion. (47) Nous savons très bien ce qu’ils écoutent. Quand ils t’écoutent et qu’ils chuchotent entre eux, les injustes disent : “ Vous ne suivez qu’un homme ensorcelé ”. (48) Vois ce à quoi ils te comparent ! Ils s’égarent donc et sont incapables de trouver un chemin [vers la vérité]. » (al-Isrāʾ, 45-48)</p>
<p>[Citations coraniques restaurées d’après le corpus canonique : l’emplacement imprimé correspondant est vide dans la source numérisée — perte OCR.]</p>
<h3>La compréhension</h3>
<h4>Explication des termes</h4>
<ul>
<li><em>ḥijāban</em> (un voile) : ce qui sépare et couvre.</li>
<li><em>mastūran</em> (invisible) : voilé aux regards, nul ne le voit ; on dit aussi : au sens de voilant.</li>
<li><em>akinnatan</em> (des enveloppes) : pluriel de <em>kinān</em> — ce qui couvre la chose.</li>
<li><em>waqran</em> (une lourdeur) : le <em>waqr</em> est la surdité et le poids dans les oreilles, qui empêche d’entendre.</li>
<li><em>masḥūran</em> (un ensorcelé) : l’esprit fêlé par l’effet du sort qu’il a subi.</li>
<li><em>fa-ḍallū</em> (ils se sont égarés) : ils se sont écartés du droit chemin visé.</li>
</ul>
<h3>Extraction des idées des versets</h3>
<ul>
<li>Comment Dieu, Puissant et Majestueux, a-t-Il protégé Son prophète du mal des associateurs ?</li>
<li>Pourquoi les associateurs ne tirent-ils pas profit du noble Coran pour y croire ?</li>
</ul>
<h3>Le commentaire (tafsīr)</h3>
<p>Ces versets comprennent ce qui suit :</p>
<h3>Premièrement : la protection accordée par Dieu à Son prophète du mal des associateurs, par un voile invisible</h3>
<p>Après que le discours eut établi la divinité, vint ensuite l’établissement de la prophétie, et la mention de quelques états de ceux qui la nient. Le Très-Haut a dit :</p>
<p>« Et quand tu lis le Coran, Nous plaçons, entre toi et ceux qui ne croient pas en l’au-delà, un voile invisible. » (al-Isrāʾ, 45)</p>
<p>[Citation coranique (v. 45) restaurée d’après le corpus canonique : l’emplacement imprimé est vide — perte OCR.]</p>
<p>Le sens de <em>wa-idhā qaraʾta l-Qurʾān</em> (« et quand tu lis le Coran ») : quand tu t’emploieras et te livreras à la lecture du Coran — et son sens n’est pas : quand tu en auras fini la lecture. Et le Coran visé n’est pas sa totalité : le visé est tout ce que le nom recouvre, peu ou beaucoup — car tu dis de qui lit quelque partie du Coran : “ celui-ci lit le Coran ”.</p>
<p>[Clause « wa-idhā qaraʾta l-Qurʾān » restaurée d’après le corpus canonique : l’emplacement imprimé est vide — perte OCR.]</p>
<p>Ce verset comporte deux sens :</p>
<ul>
<li>Le premier : Dieu, le Très-Haut, informa Son prophète qu’Il le protège des associateurs de La Mecque, qui l’importunaient au temps de sa lecture du Coran et de sa prière en la mosquée et voulaient porter la main sur lui — et qu’Il le voile d’eux. Renforce ce sens ce qui fut rapporté de la cause de la descente du verset : il descendit au sujet de gens qui importunaient le Messager de Dieu — paix et bénédiction sur lui — quand il lisait le Coran aux gens. Et il fut rapporté que — paix et bénédiction sur lui —, chaque fois qu’il lisait le Coran, se tenaient à sa droite deux hommes, et à sa gauche deux autres, des descendants de Quṣayy, qui battaient des mains et sifflaient, et mêlaient à sa lecture des poèmes.</li>
</ul>
<ul>
<li>Le second : Il l’informa qu’Il place entre les dénégateurs et l’intelligence de ce que lit Muḥammad — paix et bénédiction sur lui — du Coran un voile : ils ne le comprendront point et n’en tireront point profit. Le sens du voile est alors le scellement et l’empreinte que Dieu créa en leurs cœurs, qui les empêche de saisir les subtilités du Coran, ses beautés et ses utilités. Sur cette interprétation, le verset concorde avec le sens du suivant ; sur la première, le sens des deux versets diffère.</li>
</ul>
<p>Et Sa parole : <em>mastūran</em> (« invisible ») — ce qu’il y a de plus apparent est qu’il soit un adjectif du voile : voilé aux yeux des créatures, nul ne le perçoit en vision, comme les autres voiles : il ne relève que de la puissance de Dieu, de Sa sauvegarde et de Son égarement, selon les deux interprétations susdites. On dit : l’estimation est “ voilé par lui ”, avec effacement du pronom de rappel. Et dit al-Akhfash : <em>mastūran</em> est au sens de <em>sātir</em> (voilant), comme <em>mashūm</em> et <em>maymūn</em>, qui sont au sens de <em>shāʾim</em> et <em>yāmun</em>. Dit le cadi Abū Muḥammad [Ibn ʿAṭiyya] : cela est sans raison qui y appelle — forcerie ; et son exemple ne tient pas. On dit : c’est par voie d’intensité, comme l’on dit “ poème de poète ” — ce qui est discuté en ceci que l’intensité n’advient jamais que par le nom d’agent et du premier vocable : s’Il avait dit “ un voile voilant ” (<em>ḥijāban ḥājiban</em>), la comparaison eût été correcte.</p>
<p>[Mot « mastūran » restauré d’après le corpus canonique : l’emplacement imprimé est vide — perte OCR.]</p>
<h3>Deuxièmement : l’empreinte des cœurs des associateurs, qui ne tirent pas profit du Coran</h3>
<p>Le Très-Haut a dit :</p>
<p>« Nous avons mis des voiles sur leurs cœurs, de sorte qu’ils ne le comprennent pas : et dans leurs oreilles, une lourdeur. Et quand, dans le Coran, tu évoques Ton Seigneur l’Unique, ils tournent le dos par répulsion. » (al-Isrāʾ, 46)</p>
<p>[Citation coranique (v. 46) restaurée d’après le corpus canonique : l’emplacement imprimé est vide — perte OCR.]</p>
<p>Les <em>akinnatan</em> (enveloppes) sont pluriel de <em>kinān</em>, comme <em>aʿinatan</em> de <em>ʿinān</em> : ce qui couvre la chose et la voile — dont le fourreau des flèches (<em>kinānat al-nabl</em>). Et le <em>waqr</em> : le poids dans l’oreille qui empêche l’ouïe. Tout cela sont des métaphores de l’égarement dont Dieu les enveloppa : Il exprima son abondance et son ampleur en ce qu’ils sont comme celui dont le cœur fut couvert et l’oreille rendue sourde — Dieu, le Très-Haut, plaça en leurs cœurs ce qui les occupe de comprendre le Coran, et en leurs oreilles ce qui empêche d’entendre sa voix : empêchés d’en saisir le sens et d’en atteindre la réalité, leurs cœurs se détournent de le comprendre et leurs oreilles s’en rebutent ; aussi, pour s’être refusés à en accepter les preuves, sont-ils devenus comme s’il s’était dressé entre eux et ces preuves un voile couvrant.</p>
<p>Et Sa parole : <em>an yafqahūhu</em> (« de sorte qu’ils ne le comprennent pas ») — l’infinitif dérivé (<em>maṣdar mawʾūl</em>) de <em>an</em> et du verbe, à l’accusatif comme objet — l’estimation : “ par répulsion de ce ” (<em>karāhati an</em>) ou “ par empêchement de ce ” (<em>manʿi an</em>) — et le pronom de <em>yafqahūhu</em> renvoie au Coran.</p>
<p>Et Sa parole, le Très-Haut :</p>
<p>« Et quand, dans le Coran, tu évoques Ton Seigneur l’Unique, ils tournent le dos par répulsion. » (al-Isrāʾ, 46 — seconde partie)</p>
<p>— c’est-à-dire : quand viendront, en ta lecture, les lieux de l’unicité dans le Coran, les associateurs de La Mecque fuiront l’audition de cela, par négation et horreur de lui : il y a, en effet, rejet de leurs divinités et non-reconnaissance d’elles. Leur tournant le dos vient alors de la colère qu’on garde le silence sur leurs divinités et qu’on n’en fasse aucun cas : ils savent, en effet, qu’on ne s’est tu sur leurs divinités que par non-reconnaissance d’elles. Et dit une partie des savants : un groupe de Quraysh entra chez Abū Ṭālib en visite auprès de lui ; le Messager de Dieu — paix et bénédiction sur lui — entra auprès d’eux et lut, passant par l’unicité ; puis il dit : “ Compagnons de Quraysh, dites : nul dieu sinon Dieu — vous dominez par elle les Arabes, et les non-Arabes vous seront redevables ”. Ils tournèrent le dos et s’enfuirent : le verset descendit.</p>
<p>[Clause « wa-idhā dhakarta rabbaka fī l-Qurʾāni waḥdahu wa-wallaw ʿalā adbhārihim nufūran » restaurée d’après le corpus canonique : l’emplacement imprimé est vide — perte OCR.]</p>
<p>Et Sa parole : <em>nufūran</em> (« par répulsion ») — il se peut qu’il soit un infinitif en position d’état (<em>ḥāl</em>), et il se peut qu’il soit un pluriel de <em>nāfir</em>, comme <em>shāhid/shuhūd</em> : car <em>faʿūl</em> est des schèmes de <em>fāʿil</em> en les attributs — sa mise à l’accusatif est comme état : “ en fuyants ”.</p>
<p>[Mot « nufūran » restauré d’après le corpus canonique : l’emplacement imprimé est vide — perte OCR.]</p>
<p>Et al-Ṭabarī rapporta d’un groupe qu’il dit : le visé par Sa parole : « ils tournent le dos par répulsion » est les démons — qui fuient la lecture du Coran — voulant que le sens les indique, bien qu’il ne soit point fait d’eux mention en l’expression. Et cela est pareil au dire du Prophète — paix et bénédiction sur lui : « Quand l’appel à la prière retentit, le démon s’en va, au trot véloce (<em>ḥiṣāṣ</em>) ».</p>
<p>[Clause « wa-wallaw ʿalā adbhārihim nufūran » restaurée d’après le corpus canonique : l’emplacement imprimé est vide — perte OCR. Le <em>ḥiṣāṣ</em> : le galop véloce — dit aussi : le vent — que les commentateurs du hadith (Bukhārī, Muslim) expliquent par le fardeau de l’appel sur le démon.]</p>
<p>Puis le Très-Haut dit :</p>
<p>« Nous savons très bien ce qu’ils écoutent. » (al-Isrāʾ, 47 — ouverture)</p>
<p>— c’est-à-dire : Nous connaissons le mieux la manière dont ils écoutent — le mépris, la raillerie, la moquerie et la dénégation, au temps de leur écoute du Coran. C’est comme tu dis : un tel écoute par avidité et empressement, ou par détour, feinte et mépris. Le pronom de Sa parole : <em>bi-hī</em> (« de ce ” qu’ils écoutent ») renvoie à <em>mā</em> (« ce ”), qui est au sens de “ ce qui ” ; le visé par “ ce qui ” est ce que nous avons dit — le mépris et le détour. C’est comme s’Il avait dit : Nous connaissons le mieux le mépris et la raillerie dont ils usent en écoutant — il est leur inséparable : Dieu, par ce verset, démasqua leur secret.</p>
<p>[Citation coranique (v. 47, ouverture) et mots « bi-hī » et « mā » restaurés d’après le corpus canonique : les emplacements imprimés sont vides — perte OCR.]</p>
<p>Et l’opérateur du premier <em>idh</em> (« quand ») et de ce qui lui est conjoint est le premier <em>yastamiʿūna</em> (« ils écoutent »).</p>
<p>[Mot « idh » restauré d’après le texte d’Ibn ʿAṭiyya (« والعامل في ﴿إذ﴾ الأولى وفي المعطوفة عليها ﴿يستمعون﴾ الأول ») : l’emplacement imprimé est vide — perte OCR.]</p>
<p>Et Sa parole, glorifié soit-Il : <em>wa-idh hum najwā</em> (« et quand ils chuchotent entre eux ») les décrit par l’infinitif (<em>maṣdar</em>), comme l’on dit : gens de contentement et d’équité. On dit : le visé par Sa parole : <em>wa-idh hum najwā</em> est leur tenue de conseil en la maison al-Nadwa, puis ce qui s’en répandit.</p>
<p>[Clause « wa-idh hum najwā » restaurée d’après le corpus canonique (deux occurrences) : les emplacements imprimés sont vides — perte OCR.]</p>
<p>Et Sa parole : <em>masḥūran</em> (« un homme ensorcelé ») — ce qu’il y a de plus apparent est qu’il soit de <em>siḥr</em> (la sorcellerie) : ils comparèrent le dérèglement qui est en lui — selon leur prétention — à ce qui advient de l’ensorcelé dont le sort a fêlé l’esprit et corrompu le propos. Le verset est alors semblable au dire de certains : « en lui est une folie » (al-Muʾminūn, 25) et ce qui s’en approche.</p>
<p>Et dit Abū ʿUbayda : <em>masḥūran</em> est au sens de “ possesseur d’un <em>saḥr</em> ” — le poumon, dit aussi <em>suḥr</em> au <em>ḍamma</em> ; d’où la parole de ʿĀʾisha — Dieu l’agrée : “ Le Messager de Dieu — paix et bénédiction sur lui — mourut entre mon <em>saḥr</em> et mon <em>naḥr</em> ” (entre ma poitrine et ma gorge). D’où aussi leur dire au lâche : “ son <em>saḥr</em> s’est gonflé ” — car l’épouvanté a le poumon qui s’enfle. Le propos des associateurs vise, par ceci, d’indiquer qu’il est un homme, doué d’un poumon.</p>
<p>Et le verset qui suit ceci renforce que le vocable du verset est de <em>siḥr</em> (la sorcellerie), au <em>kasra</em> du <em>sīn</em> : car le porter sur cela est ce qui s’accorde avec le fait qu’on lui frappe la parabole ; quant à le tenir du <em>saḥr</em> qui est le poumon et à ce que l’indication soit qu’il est un homme — on ne lui frappa point, en cela, de parabole : c’est un attribut de vérité pour lui.</p>
<p>[Mots « masḥūran » et citation « en lui est une folie » (al-Muʾminūn, 25) restaurés d’après le corpus canonique : les emplacements imprimés sont vides — perte OCR ; identification vérifiée sur le texte d’Ibn ʿAṭiyya : « شبيهة بقول بعضهم ﴿به جنة﴾ [المؤمنون: ٢٥] ».]</p>
<p>Puis le Très-Haut dit :</p>
<p>« Vois ce à quoi ils te comparent ! Ils s’égarent donc et sont incapables de trouver un chemin [vers la vérité]. » (al-Isrāʾ, 48)</p>
<p>La parabole qu’on lui frappe est leur dire : ensorcelé, sorcier, possédé, devin — car il n’était point, à leurs yeux, avéré qu’il fût l’un de ces caractères : ce n’était de leur part que par voie de comparaison. Puis al-Walīd b. al-Mughīra vit que le plus proche de ces états est qu’il soit sorcier ; puis Dieu prononça sur eux l’égarement.</p>
<p>[Citation coranique (v. 48) restaurée d’après le corpus canonique : l’emplacement imprimé est vide — perte OCR.]</p>
<p>Et Sa parole, le Très-Haut : <em>fa-lā yastaṭīʿūna sabīlā</em> (« ils sont incapables de trouver un chemin ») comporte deux sens :</p>
<p>Le premier : ils ne peuvent un chemin vers la guidance et la considération qui mène à la foi — le verset court alors le cours de Sa parole :</p>
<p>« Nous avons mis des voiles sur leurs cœurs, de sorte qu’ils ne le comprennent pas : et dans leurs oreilles, une lourdeur. » (al-Isrāʾ, 46)</p>
<p>et ce qui s’en approche. Le second : ils ne peuvent un chemin pour corrompre ta affaire et éteindre la lumière de Dieu en toi — par les paraboles qu’ils te frappent et les ruses qu’ils poursuivent en ta direction. Et al-Ṭabarī rapporta que ce verset descendit au sujet d’al-Walīd b. al-Mughīra et ses compagnons.</p>
<p>[Mots « fa-lā yastaṭīʿūna sabīlā » et citation de Isrāʾ 46 (span imprimé « [الإسراء: 46] ») restaurés d’après le corpus canonique : les emplacements imprimés sont vides — perte OCR. Note : l’édition en ligne du Muḥarrar imprime ici « [الأنعام: ٢٥] » — coquille corrigée par sa propre note (« الآية ٤٦ من هذه السورة ») ; le manuel porte la référence correcte.]</p>
<h3>Troisièmement : les finalités des versets</h3>
<p>Ces versets orientent vers la réalisation d’un ensemble de finalités éducatives, dont :</p>
<ul>
<li>La largesse de Dieu et Ses bienfaits abondants envers les croyants — au premier rang desquels Il leur envoya ce noble messager et fit descendre sur eux ce Livre explicite, rempli d’exhortations, de sagesses et de règles, pour faire sortir les gens des ténèbres de la dénégation vers la lumière de la foi.</li>
<li>La protection de Dieu, le Très-Haut, envers Son prophète contre toutes les machinations et intrigues que montèrent les associateurs — Il le voila d’eux par Son soin et Sa sauvegarde, jusqu’à ce qu’il délivrât Son message et transmît Sa religion.</li>
<li>Dieu empêche les associateurs de comprendre le Coran et d’en tirer profit : car ils l’écoutent par moquerie et raillerie, non en visant la foi et la guidance.</li>
</ul>
<h3>L’évaluation (taqwīm)</h3>
<ul>
<li>Que signifie le voile invisible en les versets ?</li>
<li>Pourquoi les associateurs tournent-ils le dos par répulsion ?</li>
<li>Comment les associateurs écoutent-ils le noble Coran ?</li>
<li>Pourquoi les associateurs se sont-ils égarés du chemin ?</li>
</ul>
<h3>L’investissement (istithmār)</h3>
<p>Allah, le Très-Haut, a dit :</p>
<p>« Nous avons destiné beaucoup de djinns et d’hommes pour l’Enfer. Ils ont des cœurs, mais ne comprennent pas. Ils ont des yeux, mais ne voient pas. Ils ont des oreilles, mais n’entendent pas. Ceux-là sont comme les bestiaux, même plus égarés encore. Tels sont les insouciants. » (al-Aʿrāf, 179)</p>
<p>[Citation coranique (al-Aʿrāf, 179 — span imprimé « [الأعراف: 179] ») restaurée d’après le corpus canonique : l’emplacement imprimé est vide — perte OCR.]</p>
<p>Dit Abū Ḥayyān, en son commentaire de ce verset : « Quand ils ne méditent rien des signes, ne les regardent d’un regard d’avertissement et ne les écoutent d’une écoute de réflexion, ils furent faits comme s’ils avaient perdu la compréhension par les cœurs, la vue par les yeux et l’ouïe par les oreilles. Le visé n’est pas la négation de ces perceptions en ces sens : le visé est la négation du profit qu’on en tire, en ce qui fut demandé d’eux — la foi. » [al-Baḥr al-Muḥīṭ, d’Abū Ḥayyān : 5/228 — réf. imprimée « 228/5 », ordre inversé]</p>
<p>Je contemple le texte et réponds à ce qui suit :</p>
<ul>
<li>J’explicite les sens métaphoriques contenus dans le verset, en m’aidant de mes acquisitions en science de la rhétorique.</li>
<li>Comment l’homme se délivre-t-il de ces empêchements pour tirer profit du Coran et goûter la douceur de la foi ?</li>
</ul>
<h3>La préparation (iʿdād)</h3>
<p>Je contemple les versets 49 à 55 de la sourate al-Isrāʾ et réponds à ce qui suit :</p>
<ul>
<li>Je recherche la portée des expressions suivantes :</li>
</ul>
<p><em>rufātan</em> (رُفَاتًا — des débris).</p>
<p><em>jadīdan</em> (جَدِيدًا — nouveau).</p>
<p><em>fatarakum</em> (فَطَرَكُمْ — qui vous a fait exister).</p>
<p><em>al-nazgh</em> (ٱلنَّزْغُ — la sollicitation du démon).</p>
<p>[Expressions restituées du lexique de la leçon suivante (versets 49-55) : les emplacements imprimés sont vides — perte OCR.]</p>
<ul>
<li>Je recherche le dire des négateurs de la résurrection, et comment Dieu leur répondit à travers les versets.</li>
</ul>
<ul>
<li>J’explicite le sens de la parole du Très-Haut :</li>
</ul>
<p>« Et dis à Mes serviteurs d’exprimer les meilleures paroles, car le Diable sème la discorde parmi eux. Le Diable est certes, pour l’homme, un ennemi déclaré. » (al-Isrāʾ, 53)</p>
<p>— avec le parsing du verset et l’exposé de ses subtilités rhétoriques.</p>
<p>[Citation coranique (v. 53, de la leçon suivante) restaurée d’après le corpus canonique : l’emplacement imprimé est vide — perte OCR. Elle prépare le différend des grammairiens (Sībawayh / al-Akhfash) sur « yaqūlū » — le crux grammatical de la leçon suivante.]</p>"""


def main():
    with open(BOOK, "r", encoding="utf-8") as fh:
        d = json.load(fh)
    hit = 0
    for l in d["lessons"]:
        if l.get("docId") == "13618":
            l["htmlFr"] = HTML_FR
            hit += 1
    if hit != 1:
        raise SystemExit(f"ERREUR: {hit} leçons 13618 trouvées (attendu 1)")
    with open(BOOK, "w", encoding="utf-8") as fh:
        json.dump(d, fh, ensure_ascii=False, indent=1)
    print(f"OK — leçon 13618 upgradée main: FR {len(HTML_FR)} car")


if __name__ == "__main__":
    main()

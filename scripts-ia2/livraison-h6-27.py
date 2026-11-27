#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# IA-2 — livraison-h6-27 : traduction française (htmlFr) de la leçon 27
# «دعم وتطبيق» de hadith-6ep — docId pdf-mut23h3b-707 (pp.142-145 du tirage,
# cartouche «دَعْمٌ وَتَطْبِيق» NON numéroté). Dernière séance de soutien et
# d'application de la matière (avant لائحة المصادر والمراجع, slot 708).
# Transcription établie ce tour (Z2-63) sur rendus 1200 dpi + OCR psm 4
# (tessdata_best) + microcrops 2400/4800 dpi : cartouche sans numéro ;
# item 1 «أَكْمِلُ مَا يَأْتِي: قَالَ اللهُ تَعَالَى: «مَنْ عَادَى لِي وَلِيًّا
# فَقَدْ ....................»» (matn wilāya Bukhārī 6502, L20/L22) ;
# item 3 cloze «كُنْ فِي الدُّنْيَا .... الصَّبَاحُ .... لِمَوْلَاكَ» (glyphes
# 4800 dpi : كُنْ, الدُّنْيَا, الصَّبَاحُ, لِمَوْلَاكَ avec kāf final — N.d.T.
# contre «لِمَوْتِكَ» du texte de la L24) ; item 4 signification 2
# «قَبُولُنَا التَّوْحِيدُ وَالاسْتِغْفَارُ مِنْ أَسْبَابِ الْفَوْزِ...» (4800 dpi) ;
# item 5 «عَبْدُ اللهِ بْنُ عُمَرَ - عَبْدُ اللهِ بْنُ عَمْرٍو بْنُ الْعَاصِ،
# رَضِيَ اللهُ عَنْهُمَا.» (4800 dpi : pas de «عَزَّهُمُ اللهُ», erreur de
# lecture basse résolution corrigée) ; النشاط 2 : Baqara 184 fragment
# «فَمَنْ كَانَ مِنْكُمْ مَرِيضًا أَوْ عَلَى سَفَرٍ فَعِدَّةٌ مِنْ أَيَّامٍ
# أُخَرَ» + Nisāʾ 43 «فَلَمْ تَجِدُوا مَاءً فَتَيَمَّمُوا صَعِيدًا طَيِّبًا»
# (canon web ; rendus FR conformes au corpus : fiqh-6ep «Quiconque d'entre
# vous est malade ou en voyage [jeûnera un nombre égal] d'autres jours»,
# usul-fiqh-waraqat «vous ne trouvez point d'eau, alors lustration de terre
# saine») ; hadith «نِعْمَتَانِ مَغْبُونٌ فِيهِمَا كَثِيرٌ مِنَ النَّاسِ:
# الصِّحَّةُ وَالْفَرَاغُ» [صحيح البخاري، كتاب الرقاق، باب: اللهم لا عيش إلا
# عيش الآخرة] (canon web : hdith.com, surahquran, islamweb, shamela) ;
# «لَا يُؤْمِنُ أَحَدُكُمْ حَتَّى يُحِبَّ لِأَخِيهِ مَا يُحِبُّ لِنَفْسِهِ»
# [رواه البخاري] (Nawawi n° 13 canonique ; distinct du 41e du manuel =
# hadith du هوى L25) ; poème d'Ibn ʿĀšir : le tirage imprime la VARIANTE
# documentée «بِشَرْطِ الِإِقْلَاعِ وَنَفْيِ الْإِصْرَارِ *** وَالتَّلَافِ
# مُمْكِنًا ذَا اسْتِغْفَارُ» (arrabita.ma : «ونفي الإصرار», «ذا استغفار») —
# N.d.T. canon «al-qaṭʿ li-l-iṣrār / bi-stigfār» consigné ; النشاط 3 :
# tableau valeurs الْيُسْرُ/الْمَحَبَّةُ × آثار حضورها/غيابها (4800 dpi :
# يُسْرُ deux points sous la dent) ; tableau des 12 moeurs avec السَّخْرِيَّةُ
# (4800 dpi, contre OCR المحبة) ; النشاط 4 : بطاقة «مَظَاهِرِ الْيُسْرِ فِي
# الإِسْلَامِ» (4800 dpi) ; PAS de إعداد قبلي (fin de matière).
import re, os

HTML = """<h1>Consolidation et application</h1>
<p>Vingt-septième leçon du manuel « Le hadith tiré du livre des <em>Arba’ūn</em> nawawiyya de l’imam <em>al-Nawawī</em>, avec le commentaire d’Ibn <em>Daqīq</em> al-’<em>Īd</em> », à l’intention des élèves de sixième année de l’enseignement primaire traditionnel (<em>ta’līm ʾatīq</em>). Leçon de consolidation et d’application (<em>daʿmun wa-t-taṭbīq</em> <span dir="rtl" lang="ar">(دَعْمٌ وَتَطْبِيق)</span>), elle récapitule la matière des dernières leçons — les fruits de la proximité divine (wilāya) et de Son amour, l’indulgence envers celui qui faute, oublie ou agit sous contrainte, faire provision pour l’au-delà, un signe de la foi, l’étendue du pardon de Dieu, exalté soit-Il —, et, remontant jusqu’au hadith sacré du rang des amis de Dieu présenté à la vingtième leçon, au travers de quatre activités : des exercices menés dans le cahier — la complétion du hadith sacré de la prise d’ennemi contre l’ami de Dieu, la citation d’un hadith attestant que l’islam est religion de la facilité et de la levée de la contrainte, le comblement d’un pointillé qui réassemble le hadith d’Ibn <em>ʿUmar</em> et ses paroles répétées, l’apport de la preuve à l’appui de deux contenus — la conformité du désir à ce qu’a apporté la Loi, et l’acceptation du monothéisme et de la demande de pardon parmi les causes du succès dans le pardon de Dieu —, et la présentation des deux nobles Compagnons <em>ʿAbd Allāh</em> b. <em>ʿUmar</em> et <em>ʿAbd Allāh</em> b. <em>ʿAmr</em> b. <em>al-ʿĀṣ</em> — ; puis la contemplation de quatre textes — le verset de la dispense du jeûneur malade ou en voyage, le verset du lustrage de terre saine faute d’eau, le hadith des deux bienfaits que bien des gens négligent, le hadith du signe de l’accomplissement de la foi, et deux vers du <em>Muḫtaṣar</em> d’Ibn <em>ʿĀšir</em> sur le repentir et ses conditions —, suivie de cinq questions ; l’exploitation des acquis au moyen du tableau des valeurs — la facilité et l’amour, avec les effets de leur présence et de leur absence sur l’individu et la société — et du tableau de tri des douze moeurs en présence ; enfin la réalisation, en coopération avec les amis de la classe, de la carte de présentation « les manifestations de la facilité en islam », dont le tirage imprime le cadre ouvert — versets coraniques, hadiths prophétiques, modèles des applications du Messager ﷺ en ses paroles et en ses actes, modèles des applications de la facilité dans la vie quotidienne —, avec proposition d’une forme pratique pour son exploitation dans le milieu scolaire et social. Dernière séance de la matière, elle ne comporte pas de préparation préalable : la liste des sources et références fait suite aussitôt. N.d.T. : leçon d’activités non numérotée du tirage, comme la vingt-et-unième ; la numérotation interne du manuel ne compte pas les leçons d’activités non numérotées, alors que le sommaire officiel compte la présente leçon comme la vingt-septième de la matière.</p>
<h2>Objectifs des activités (<em>ʾahdāfu l-ʾanšiṭa</em> <span dir="rtl" lang="ar">(أَهْدَافُ الْأَنْشِطَةِ)</span>)</h2>
<ol>
<li>Que j’évalue mes acquisitions de savoir des leçons précédentes (<em>ʾan ʾuqawwima muktasabātī l-maʿrifiyyata mina d-durūsi s-sābiqa</em> <span dir="rtl" lang="ar">(أَنْ أُقَوِّمَ مُكْتَسَبَاتِي الْمَعْرِفِيَّةَ مِنَ الدُّرُوسِ السَّابِقَةِ.)</span>).</li>
<li>Que je m’exerce à comprendre les textes de la Loi et à les analyser (<em>ʾan ʾatadarraba ʿalà fahmi n-nuṣūši š-šarʿiyyati wa-taḥlīlihā</em> <span dir="rtl" lang="ar">(أَنْ أَتَدَرَّبَ عَلَى فَهْمِ النُّصُوصِ الشَّرْعِيَّةِ وَتَحْلِيلِهَا.)</span>).</li>
<li>Que j’emploie mes acquisitions de savoir et d’habileté dans de nouvelles situations (<em>ʾan ʾuwaẓẓifa muktasabātī l-maʿrifiyyata wa-l-mahāriyyata fī waḍʿiyyātin ǧadīda</em> <span dir="rtl" lang="ar">(أَنْ أُوَظِّفَ مُكْتَسَبَاتِي الْمَعْرِفِيَّةَ وَالْمَهَارِيَّةَ فِي وَضْعِيَّاتٍ جَدِيدَةٍ.)</span>).</li>
</ol>
<h2>Activité 1 : je réalise dans mon cahier (<em>an-nišāṭ 1 : ʾunǧizu fī daftarī</em> <span dir="rtl" lang="ar">(النشاط 1 - أُنْجِزُ فِي دَفْتَرِي:)</span>)</h2>
<ol>
<li>Je complète ce qui suit : le Très-Haut a dit : « quiconque prend pour ennemi un mien ami, J’ai … » (<em>ʾukmilu mā yaʾtī : qāla llāhu taʿālà : «man ʿādà lī waliyyan faqad ....................»</em> <span dir="rtl" lang="ar">(أَكْمِلُ مَا يَأْتِي: قَالَ اللهُ تَعَالَى: «مَنْ عَادَى لِي وَلِيًّا فَقَدْ ....................»)</span>) — le tirage imprime un pointillé que l’élève complète par la clause d’ouverture du hadith sacré du rang des amis de Dieu (<em>al-Buḫārī</em> n° 6502, présenté à la vingtième leçon) : «J’ai déclaré la guerre à celui-là».</li>
<li>L’islam est religion de la facilité et de la levée de la contrainte ; je mentionne le hadith qui l’atteste (<em>al-ʾislāmu dīnu l-yusri wa-rafʿi l-ḥaraǧ, ʾaḏkuru ḥadītan yadullu ʿalà ḏālik</em> <span dir="rtl" lang="ar">(الإِسْلَامُ دِينُ الْيُسْرِ وَرَفْعُ الْحَرَجِ، أَذْكُرُ حَدِيثًا يَدُلُّ عَلَى ذَلِكَ.)</span>).</li>
<li>Je comble le blanc dans mon cahier comme il convient ; le Messager de Dieu ﷺ a dit : « sois en ce bas-monde … le matin … pour ton Seigneur » (<em>ʾamlaʾu l-farāġa fī daftarī bimā yunāsib, qāla ﷺ : «kun fī d-dunyā .................... ṣ-ṣabāḥu .................... li-mawlāk».</em> <span dir="rtl" lang="ar">(أَمْلَا الْفَرَاغَ فِي دَفْتَرِي بِمَا يُنَاسِبُ، قَالَ ﷺ: «كُنْ فِي الدُّنْيَا .................... الصَّبَاحُ .................... لِمَوْلَاكَ».)</span>) — le tirage imprime un pointillé double qui réassemble la matière de la vingt-quatrième leçon : l’ouverture du hadith d’Ibn <em>ʿUmar</em> — «sois en ce bas-monde comme si tu étais un étranger ou un passant» (<em>al-Buḫārī</em> n° 6416) — et ses paroles répétées, «quand tu passes la soirée, n’attends pas le matin». N.d.T. : le segment final imprimé «pour ton Seigneur» (<em>li-mawlāk</em>) fait pendant au «pour ta mort» (<em>li-mawtik</em>) qui achève ces paroles dans la leçon en cause ; l’écart est consigné sans correction.</li>
<li>Je convoque ce que je garde en mémoire des textes, et j’en cite la preuve pour les contenus suivants (<em>ʾastadillu li-l-maʿānī l-ʾātiyati bimā yunāsib</em> <span dir="rtl" lang="ar">(أَسْتَدِلُّ لِلْمَعَانِي الآتِيَةِ بِمَا يُنَاسِبُ:)</span>) :
<ul>
<li>par la conformité du désir à ce qu’a apporté la Loi, la foi s’accomplit (<em>bimuwāfaqati l-hawà limā ǧāʾa bihi š-šarʿu yaktamilu l-ʾīmān</em> <span dir="rtl" lang="ar">(بِمُوَافَقَةِ الْهَوَى لِمَا جَاءَ بِهِ الشَّرْعُ يَكْتَمِلُ الإِيمَانُ.)</span>) — le hadith visé est celui de la vingt-cinquième leçon : «aucun d’entre vous n’est croyant tant que son désir suit ce que je suis venu apporter» ;</li>
<li>notre acceptation du monothéisme et de la demande de pardon est parmi les causes du succès dans le pardon de Dieu (<em>qabūlunā t-tawḥīdu wa-l-ʾistigfāru min ʾasbābi l-fawzi bimaġfirati llāh</em> <span dir="rtl" lang="ar">(قَبُولُنَا التَّوْحِيدُ وَالاسْتِغْفَارُ مِنْ أَسْبَابِ الْفَوْزِ بِمَغْفِرَةِ اللهِ.)</span>) — les voies du pardon établies à la vingt-sixième leçon : l’invocation et l’espérance, la demande de pardon, la sincérité de l’adoration.</li>
</ul>
</li>
<li>Je présente les deux nobles Compagnons : <em>ʿAbd Allāh</em> b. <em>ʿUmar</em> et <em>ʿAbd Allāh</em> b. <em>ʿAmr</em> b. <em>al-ʿĀṣ</em> — que Dieu les agrée (<em>ʾuʿarrifu bi-ṣ-ṣaḥābiyyayni l-ǧalīlayni : ʿAbdu llāhi bnu ʿUmar - ʿAbdu llāhi bnu ʿAmrin bni l-ʿĀṣ, raḍiya llāhu ʿanhumā</em> <span dir="rtl" lang="ar">(أُعَرِّفُ بِالصَّحَابِيَّيْنِ الْجَلِيلَيْنِ: عَبْدُ اللهِ بْنُ عُمَرَ - عَبْدُ اللهِ بْنُ عَمْرٍو بْنُ الْعَاصِ، رَضِيَ اللهُ عَنْهُمَا.)</span>) — la notice du transmetteur de la vingt-quatrième leçon présente Ibn <em>ʿUmar</em>, celle de la vingt-cinquième présente Ibn <em>ʿAmr</em> b. <em>al-ʿĀṣ</em>.</li>
</ol>
<h2>Activité 2 (<em>an-nišāṭ 2</em> <span dir="rtl" lang="ar">(النشاط 2)</span>)</h2>
<p>Le Très-Haut a dit : « … quiconque d’entre vous est malade ou en voyage [jeûnera un nombre égal] d’autres jours… » <span dir="rtl" lang="ar">[البقرة 184]</span> (<em>qāla llāhu taʿālà : (famai kāna minkum marīḍan aw ʿalà safarin fa-ʿidda-tun min ʾayyāmin ʾuḫrà) [al-Baqara 184]</em> <span dir="rtl" lang="ar">(قَالَ اللهُ تَعَالَى: (فَمَنْ كَانَ مِنْكُمْ مَرِيضًا أَوْ عَلَى سَفَرٍ فَعِدَّةٌ مِنْ أَيَّامٍ أُخَرَ) [البقرة 184])</span>).</p>
<p>Et il a dit, gloire à Lui : « … vous ne trouvez point d’eau, alors lustration de terre saine, pure… » <span dir="rtl" lang="ar">[النساء 43]</span> (<em>wa-qāla subḥānah : (falami taǧidū māʾan fa-tayammamū ṣaʿīdan ṭayyibā) [an-Nisāʾ 43]</em> <span dir="rtl" lang="ar">(وَقَالَ سُبْحَانَهُ: (فَلَمْ تَجِدُوا مَاءً فَتَيَمَّمُوا صَعِيدًا طَيِّبًا) [النساء 43])</span>).</p>
<p>Et le Messager de Dieu ﷺ a dit : « deux bienfaits que bien des gens négligent : la santé et le loisir » <span dir="rtl" lang="ar">[صحيح البخاري، كتاب الرقاق، باب: اللهم لا عيش إلا عيش الآخرة]</span> (<em>wa-qāla ﷺ : «niʿmatāni maġbūnun fīhimā kaṯīrun mina n-nās : aṣ-ṣiḥḥatu wa-l-farāġ» [ṣaḥīḥu l-Buḫārī, kitābi r-riqāq, bāb : Allāhumma lā ʿayša ʾillā ʿayšu l-ʾāḫira]</em> <span dir="rtl" lang="ar">(وَقَالَ ﷺ: «نِعْمَتَانِ مَغْبُونٌ فِيهِمَا كَثِيرٌ مِنَ النَّاسِ: الصِّحَّةُ وَالْفَرَاغُ» [صحيح البخاري، كتاب الرقاق، باب: اللهم لا عيش إلا عيش الآخرة])</span>).</p>
<p>Et il a dit ﷺ : « aucun d’entre vous n’est croyant tant qu’il n’aime pas pour son frère ce qu’il aime pour lui-même » <span dir="rtl" lang="ar">[رواه البخاري]</span> (<em>wa-qāla ﷺ : «lā yuʾminu ʾaḥadukum ḥattà yuḥibba li-ʾaḫīhi mā yuḥibbu li-nafsih» [ruwiyahu l-Buḫārī]</em> <span dir="rtl" lang="ar">(وَقَالَ ﷺ: «لَا يُؤْمِنُ أَحَدُكُمْ حَتَّى يُحِبَّ لِأَخِيهِ مَا يُحِبُّ لِنَفْسِهِ» [رواه البخاري])</span>). N.d.T. : le treizième hadith des Quarante canoniques d’<em>al-Nawawī</em> (<em>al-Buḫārī</em> n° 13, Muslim n° 45), distinct du quarante-et-unième hadith porté par la vingt-cinquième leçon.</p>
<p>Et <em>ʿAbd al-Wāḥid</em> b. <em>ʿĀšir</em> — que Dieu lui fasse miséricorde — a dit : « et le repentir de tout péché commis *** est dû immédiatement, sans restriction : c’est le regret ; sous la condition de l’abandon [du péché] et de la négation de l’obstination *** et de la réparation de ce qui est réparable, par la demande de pardon » (<em>wa-qāla ʿAbdu l-Wāḥidi bnu ʿĀširin raḥimahu llāhu : «wa-tawba-tun min kulli ḏanbin yuǧtaramu *** taǧibu fawran muṭlaqan wa-hiya n-nadamu ; bi-šarṭi l-iqlāʿi wa-nafyi l-iṣrāri *** wa-t-talāfi mumkinan ḏā stigfār»</em> <span dir="rtl" lang="ar">(وَقَالَ عَبْدُ الْوَاحِدِ بْنُ عَاشِرٍ رَحِمَهُ اللهُ: «وَتَوْبَةٌ مِنْ كُلِّ ذَنْبٍ يُجْتَرَمُ *** تَجِبُ فَوْرًا مُطْلَقًا وَهْيَ النَّدَمُ؛ بِشَرْطِ الِإِقْلَاعِ وَنَفْيِ الْإِصْرَارِ *** وَالتَّلَافِ مُمْكِنًا ذَا اسْتِغْفَارُ»)</span>). N.d.T. : vers du chapitre du repentir dans le <em>Muḫtaṣar</em> (Alfiyya) d’Ibn <em>ʿĀšir</em> ; le canon des éditions courantes porte «l’abandon et la rupture de l’obstination» (<em>al-iqlāʿ wa-l-qaṭʿ li-l-iṣrār</em>) et «par la demande de pardon» (<em>bi-stigfār</em>) — le tirage suit une variante attestée («l’abandon et la négation de l’obstination», <em>wa-nafyi l-iṣrār</em>) ; l’écart est consigné sans correction.</p>
<h2>Je contemple les textes ci-dessus et je réponds aux questions dans mon cahier (<em>ʾatʾammili n-nuṣūṣa l-ʾātiyata, wa-ʾaǧību ʿani l-ʾasʾilati fī daftarī</em> <span dir="rtl" lang="ar">(أَتَأَمَّلِ النُّصُوصَ الآتِيَةَ، وَأَجِبْ عَنِ الأسْئِلَةِ فِي دَفْتَرِي:)</span>)</h2>
<ol>
<li>Je fais voir, des deux versets, les manifestations de la facilité et de la levée de la contrainte en islam (<em>ʾastaḫriǧu mina l-ʾāyati l-ʾūlà wa-ṯ-ṯāniyati maẓāhira l-yusri wa-rafʿi l-ḥaraǧi fī l-ʾislām</em> <span dir="rtl" lang="ar">(أَسْتَخْرِجُ مِنَ الآيَةِ الأُولَى وَالثَّانِيَةِ مَظَاهِرَ الْيُسْرِ وَرَفْعِ الْحَرَجِ فِي الإِسْلَامِ.)</span>).</li>
<li>Je dégage du premier hadith la conséquence du délaissement du temps et de la santé (<em>ʾastaḫliṣu mina l-ḥadīṯi l-ʾawwali ʿāqibata t-tafrīṭi fī l-waqti wa-ṣ-ṣiḥḥa</em> <span dir="rtl" lang="ar">(أَسْتَخْلِصُ مِنَ الْحَدِيثِ الأَوَّلِ عَاقِبَةَ التَّفْرِيطِ فِي الوَقْتِ وَالصِّحَّةِ.)</span>).</li>
<li>Je fais voir du second hadith le signe de l’accomplissement de la foi et de son incomplétude (<em>ʾastaḫriǧu mina l-ḥadīṯi ṯ-ṯānī ʿalāmata kamāli l-ʾīmāni wa-naqṣānih</em> <span dir="rtl" lang="ar">(أَسْتَخْرِجُ مِنَ الْحَدِيثِ الثَّانِي عَلَامَةَ كَمَالِ الإِيمَانِ وَنَقْصَانِهِ.)</span>).</li>
<li>Je fais voir des propos d’Ibn <em>ʿĀšir</em> le statut du repentir et ses conditions (<em>ʾastaḫriǧu min kalāmi bni ʿĀširin ḥukma t-tawbati wa-šurūṭahā</em> <span dir="rtl" lang="ar">(أَسْتَخْرِجُ مِنْ كَلامِ ابْنِ عَاشِرٍ حُكْمَ التَّوْبَةِ وَشُرُوطَهَا.)</span>).</li>
<li>Je recherche la sagesse du maintien de la porte du repentir ouverte devant le pécheur (<em>ʾabḥaṯu ʿani l-ḥikmati min baqāʾi bābi t-tawbati maftūḥan ʾamāma l-ʿāṣī</em> <span dir="rtl" lang="ar">(أَبْحَثُ عَنِ الْحِكْمَةِ مِنْ بَقَاءِ بَابِ التَّوْبَةِ مَفْتُوحًا أَمَامَ الْعَاصِي.)</span>).</li>
</ol>
<h2>Activité 3 (<em>an-nišāṭ 3</em> <span dir="rtl" lang="ar">(النشاط 3)</span>)</h2>
<p>Je comble le tableau suivant après l’avoir recopié dans mon cahier, comme il convient (<em>ʾamlaʾu l-ǧadwula l-ʾātī baʿda naqlihi ʾilà daftarī bimā yunāsib</em> <span dir="rtl" lang="ar">(أَمْلَا الْجَدْوُلَ الآتِي بَعْدَ نَقْلِهِ إِلَى دَفْتَرِي بِمَا يُنَاسِبُ:)</span>) — le tirage imprime, sous la consigne, un tableau à trois colonnes au corps ouvert, que l’élève recopie et remplit dans son cahier ; la première colonne donne deux valeurs en présence :
<table>
<thead>
<tr><th>La valeur (<em>al-qīma</em> <span dir="rtl" lang="ar">(الْقِيمَةُ)</span>)</th><th>Les effets de sa présence sur l’individu et la société (<em>ʾāṯāru ḥuḍūrihā ʿalà l-fardi wa-l-muǧtamaʿ</em> <span dir="rtl" lang="ar">(آثَارُ حُضُورِهَا عَلَى الْفَرْدِ وَالْمُجْتَمَعِ)</span>)</th><th>Les effets de son absence sur l’individu et la société (<em>ʾāṯāru ġiyābihā ʿalà l-fardi wa-l-muǧtamaʿ</em> <span dir="rtl" lang="ar">(آثَارُ غِيَابِهَا عَلَى الْفَرْدِ وَالْمُجْتَمَعِ)</span>)</th></tr>
</thead>
<tbody>
<tr><td>la facilité (<em>al-yusr</em> <span dir="rtl" lang="ar">(الْيُسْرُ)</span>)</td><td>…</td><td>…</td></tr>
<tr><td>l’amour (<em>al-maḥabba</em> <span dir="rtl" lang="ar">(الْمَحَبَّةُ)</span>)</td><td>…</td><td>…</td></tr>
</tbody>
</table>
</p>
<p>Je distingue les moeurs qui s’accordent avec la purification de l’âme de celles qui la contredisent (<em>ʾumayyizu l-ʾaḫlāqa llatī tantasibu maʿa tazkiyati n-nafsi wallatī tatanāḍu maʿahā</em> <span dir="rtl" lang="ar">(أُمَيِّزُ الأَخْلَاقَ الَّتِي تَنْتَاسِبُ مَعَ تَزْكِيَةِ النَّفْسِ وَالَّتِي تَتَنَاقَضُ مَعَهَا:)</span>) — le tirage imprime un tableau à trois colonnes : la première énumère les douze moeurs en présence ; l’élève porte chacune dans la colonne qui convient :
<table>
<thead>
<tr><th>Les moeurs (<em>al-ʾaḫlāq</em> <span dir="rtl" lang="ar">(الأَخْلَاقُ)</span>)</th><th>Ce qui s’accorde avec la purification de l’âme (<em>mā yantasibu maʿa tazkiyati n-nafs</em> <span dir="rtl" lang="ar">(مَا يَنْتَاسِبُ مَعَ تَزْكِيَةِ النَّفْسِ)</span>)</th><th>Ce qui contredit la purification de l’âme (<em>mā yatanāḍu maʿa tazkiyati n-nafs</em> <span dir="rtl" lang="ar">(مَا يَتَنَاقَضُ مَعَ تَزْكِيَةِ النَّفْسِ)</span>)</th></tr>
</thead>
<tbody>
<tr><td>la tolérance (<em>at-tasāmuḥ</em> <span dir="rtl" lang="ar">(التَّسَامُحُ)</span>) — l’espérance (<em>ar-raǧāʾ</em> <span dir="rtl" lang="ar">(الرَّجَاءُ)</span>)</td><td>…</td><td>…</td></tr>
<tr><td>l’envie (<em>al-ḥasad</em> <span dir="rtl" lang="ar">(الْحَسَدُ)</span>) — le renoncement (<em>az-zuhd</em> <span dir="rtl" lang="ar">(الزُّهْدُ)</span>)</td><td>…</td><td>…</td></tr>
<tr><td>la véracité (<em>aṣ-ṣidq</em> <span dir="rtl" lang="ar">(الصِّدْقُ)</span>) — le colportage médisant (<em>an-namīma</em> <span dir="rtl" lang="ar">(النَّمِيمَةُ)</span>)</td><td>…</td><td>…</td></tr>
<tr><td>la moquerie (<em>as-saḫrīya</em> <span dir="rtl" lang="ar">(السَّخْرِيَّةُ)</span>) — l’invocation (<em>ad-duʿāʾ</em> <span dir="rtl" lang="ar">(الدَّعَاءُ)</span>)</td><td>…</td><td>…</td></tr>
<tr><td>l’espionnage (<em>at-taǧassus</em> <span dir="rtl" lang="ar">(التَّجَسُّسُ)</span>) — l’orgueil (<em>al-kibr</em> <span dir="rtl" lang="ar">(الكِبْرُ)</span>)</td><td>…</td><td>…</td></tr>
<tr><td>la demande de pardon (<em>al-ʾistigfār</em> <span dir="rtl" lang="ar">(الاسْتِغْفَارُ)</span>) — la foi (<em>al-ʾīmān</em> <span dir="rtl" lang="ar">(الإِيمَانُ)</span>)</td><td>…</td><td>…</td></tr>
</tbody>
</table>
</p>
<h2>Activité 4 : j’exploite mes acquis et je coopère avec mes amis pour réaliser la carte de présentation « les manifestations de la facilité en islam », et je propose une forme pratique pour son exploitation dans le milieu scolaire et social, en m’aidant de la carte suivante (<em>an-nišāṭ 4 : ʾastathmiru muktasabātī wa-ʾatatawwanu maʿa ʾaṣdiqāʾī li-ʾinǧāzi bīṭāqati t-taʿrīfi bi-«maẓāhiri l-yusri fī l-ʾislām», wa-ʾaqtariḥu ṣīġatan ʿamaliyyatan li-stiṯmārihā fī wāqiʿi l-madrasati wa-l-ʾiǧtimāʿī mustaʿīnan bil-bīṭāqati l-ʾātiya</em> <span dir="rtl" lang="ar">(النشاط 4 - أَسْتَثْمِرُ مُكْتَسَبَاتِي وَأَتَعَاوَنُ مَعَ أَصْدِقَائِي لِإِنْجَازِ بِطَاقَةِ التَّعْرِيفِ بِـ: «مَظَاهِرِ الْيُسْرِ فِي الإِسْلَامِ»، وَأَقْتَرِحُ صِيغَةً عَمَلِيَّةً لِاسْتِثْمَارِهَا فِي وَاقِعِ الْمَدْرَسَةِ وَالاجْتِمَاعِيِّ مُسْتَعِينًا بِالبَطَاقَةِ الآتِيَةِ:)</span>)</h2>
<p>Le tirage imprime, au corps ouvert, la carte à compléter avec les amis de la classe :</p>
<table>
<thead>
<tr><th>Des versets coraniques (<em>ʾāyātun qurʾāniyya</em> <span dir="rtl" lang="ar">(آيَاتٌ قُرْآنِيَّةٌ)</span>)</th><th>Des hadiths prophétiques (<em>ʾaḥādīṯun nabawiyya</em> <span dir="rtl" lang="ar">(أَحَادِيثٌ نَبَوِيَّةٌ)</span>)</th></tr>
</thead>
<tbody>
<tr><td>…</td><td>…</td></tr>
</tbody>
</table>
<p><strong>Des modèles des applications du Messager ﷺ de la facilité (<em>namāḏiǧu min taṭbīqāti r-Rasūli ﷺ li-l-yusr</em> <span dir="rtl" lang="ar">(نَمَاذِجُ مِنْ تَطْبِيقَاتِ الرَّسُولِ ﷺ لِلْيُسْرِ:)</span>) :</strong></p>
<table>
<thead>
<tr><th>En ses paroles ﷺ (<em>fī ʾaqwālih ﷺ</em> <span dir="rtl" lang="ar">(فِي أَقْوَالِهِ ﷺ:)</span>)</th><th>En ses actes ﷺ (<em>fī ʾafʿālih ﷺ</em> <span dir="rtl" lang="ar">(فِي أَفْعَالِهِ ﷺ:)</span>)</th></tr>
</thead>
<tbody>
<tr><td>…</td><td>…</td></tr>
<tr><td>…</td><td>…</td></tr>
</tbody>
</table>
<p><strong>Des modèles des applications de la facilité dans la vie quotidienne (<em>namāḏiǧu min taṭbīqāti l-yusri fī l-ḥayāti l-yawmiyya</em> <span dir="rtl" lang="ar">(نَمَاذِجُ مِنْ تَطْبِيقَاتِ الْيُسْرِ فِي الْحَيَاةِ الْيَوْمِيَّةِ)</span>) :</strong></p>
<table>
<tbody>
<tr><td>…</td><td>…</td></tr>
<tr><td>…</td><td>…</td></tr>
</tbody>
</table>
"""

# --- normalisation typographique (espaces fines U+202F hors spans arabes) ---
SPAN = re.compile(r'(<span dir="rtl" lang="ar">.*?</span>)', re.S)

def normalize(html):
    out = []
    for part in SPAN.split(html):
        if part.startswith('<span dir="rtl"'):
            out.append(part)
            continue
        p = part
        p = re.sub(r' +([;:?!»])', '\u202f\\1', p)
        p = re.sub(r'(«) +', '\\1\u202f', p)
        out.append(p)
    return "".join(out)

def controls(html):
    assert "'" not in html, "apostrophe droite résiduelle"
    outside = []
    for seg in SPAN.split(html):
        if seg.startswith('<span dir="rtl"') or seg.endswith('</span>'):
            continue
        if re.search(r'[\u0621-\u064A]', seg) and 'ﷺ' not in seg:
            outside.append(seg[:60])
    assert not outside, f"arabe hors span: {outside[:3]}"
    assert html.count('«') == html.count('»'), f"guillemets déséquilibrés {html.count('«')}/{html.count('»')}"
    for tag in ["h1", "h2", "h3", "h4", "p", "ul", "ol", "li", "table", "tr", "td", "th", "strong", "em"]:
        o = len(re.findall(rf"<{tag}[ >]", html))
        c = len(re.findall(rf"</{tag}>", html))
        assert o == c, f"balise {tag}: {o}o/{c}f"
    print(f"contrôles OK — U+202F ×{html.count(chr(0x202f))}, guillemets {html.count('«')}, {len(html)} caractères")

if __name__ == "__main__":
    HTML = normalize(HTML)
    controls(HTML)
    out = "/home/z/my-project/minhaj/tr-tmp/pdf-mut23h3b-707.html"
    os.makedirs(os.path.dirname(out), exist_ok=True)
    open(out, "w", encoding="utf-8").write(HTML)
    print("écrit :", out)

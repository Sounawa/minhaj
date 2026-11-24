#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# IA-2 — livraison-h6-24 : traduction française (htmlFr) de la leçon 24
# «التزود للآخرة» de hadith-6ep — docId pdf-mut23h3b-704 (pp.127-130 du
# tirage, cartouche الدرس ٢٢). Hadith n° 40 des Quarante d'al-Nawawī
# (Ibn ʿUmar, «كن في الدنيا كأنك غريب أو عابر سبيل» + la tatomma d'Ibn
# ʿUmar «إذا أمسيت فلا تنتظر الصباح...» — al-Bukhārī 6416 ; canon web
# vérifié : sunnah.com/nawawi40:40, hadeethenc 4704). Transcription établie
# ce tour (Z2-60) : rendus 600/1200 dpi + microcrops 1200 dpi PIL x3-x6 +
# tesseract ara_best psm 4 en appoint + canons web.
# Arbitrages documentés au worklog : تمهيد «اِفْتَقَدْتُ حِكْمَةَ اللهِ»
# (contre OCR اقتضت — lettre-à-lettre 2400 dpi) ; nisba de la tarjama
# «الْعَدَوِيِّ» + «رَضِيَ اللهُ عَنْهُ» singulier (2400 dpi) ; «أَقْوَى
# النَّاسِ سَنَّتَيْنِ سَنَةً» tel qu'imprimé (fragment non retrouvé tel
# quel dans Tahdhīb/Iṣāba — N.d.T.) ; «وَعَاشَ» avec wasla (contre OCR
# عائش — canon Iṣāba عاش ابن عمر في زمان) ; «تَحِبُّهُ» du استثمار
# (contre OCR تجبه — conforme au canon d'Abū ʿUbayd via le Fatḥ) ;
# «يَشْرَعْ» (2400 dpi, contre OCR يشرح) ; «فَمَنْ سَلِمَ مِنْ ذَلِكَ
# لَمْ يُكَلَّفْ بِإِزَالَتِهِ» (remaniement couvert par بتصرف) ;
# «فَإِنَّ الْيَوْمَ عَمَلٌ» de la citation d'ʿAlī (conforme au texte du
# chapitre الرقاق du Bukhārī) ; citation «هَذَا الْإِنْسَانُ، وَهَذَا
# الْأَمَلُ، وَهَذَا الْأَجَلُ، فَبَيْنَمَا هُوَ كَذَلِكَ إِذْ جَاءَ
# الْخَطُّ الْأَقْرَبُ» attribuée au tirage à Ibn Masʿūd alors que le
# canon Bukhārī 6417 (Ibn Masʿūd) est la version du tracé quadrillé et
# que la version «خطوطاً...الخط الأقرب» est celle d'Anas (Bukhārī 6418) —
# N.d.T. consignée, tirage non corrigé ; «يُرْشِدُ الْحَدِيثُ إِلَى
# الرَّحْلِ فِي الدُّنْيَا» (arbitrage glyptique lettre-à-lettre, contre
# OCR الرَّهْد) ; «لِيَأْخُذَ الْبَلَّغَةَ مِنْهَا وَالْكَفَافَ» conforme
# au شرح الأربعين d'Ibn Daqīq al-ʿĪd (via ʿAlī b. Ḫalaf, shamela 11244/122)
# ; «الْبَلَّغَةَ» contre OCR والكفاف (ce dernier étant la suite de la
# phrase) ; «الْمُؤْمِنُ» de «كَذَلِكَ لَا يَحْتَاجُ الْمُؤْمِنُ» (contre
# OCR الموّتي) ; «يَسْتَعِدُّ أَبَدًا لِلْمَوْتِ» (contre OCR يستعذ ليوما).
# Aucun verset coranique cité dans cette leçon. إعداد قبلي unique annonce
# L25 705 «علامة الإيمان» (لا يؤمن أحدكم حتى يكون هواه تبعا لما جئت به).
import re, sys

BOOK = "/home/z/my-project/minhaj/content/books/hadith-6ep.json"
IDX = 24  # lessons[24] = pdf-mut23h3b-704

HTML = """<h1>Faire provision pour l’au-delà</h1>
<p>Vingt-quatrième leçon du manuel «\u202fLe hadith tiré du livre des <em>Arba’ūn</em> nawawiyya de l’imam <em>al-Nawawī</em>, avec le commentaire d’Ibn <em>Daqīq</em> al-’<em>Īd</em>\u202f», à l’intention des élèves de sixième année de l’enseignement primaire traditionnel (<em>ta’līm ʾatīq</em>). Elle porte le titre <em>at-tazawwudi li-l-āḫira</em> <span dir="rtl" lang="ar">(التَّزَوُّدُ لِلْآخِرَةِ)</span> et présente le quarantième hadith des Quarante d’<em>al-Nawawī</em>, rapporté par <em>Ibn ʿUmar</em> — que Dieu les agrée —\u202f: l’Envoyé de Dieu ﷺ l’a saisi par l’épaule en lui disant\u202f: «\u202fsois en ce bas-monde comme si tu étais un étranger ou un passant\u202f», suivi des paroles qu’<em>Ibn ʿUmar</em> se plaisait à répéter\u202f: «\u202fquand tu passes la soirée, n’attends pas le matin\u202f; quand tu passes le matin, n’attends pas le soir\u202f; prends de ta santé pour ta maladie, et de ta vie pour ta mort\u202f». La leçon établit que le bas-monde est un moyen d’accéder à l’au-delà et un champ où l’on sème pour y récolter, expose la manière de saisir les temps à travers quatre dispositions du croyant envers son temps et sa santé, rapporte les paroles de <em>ʿAlī</em> et le tracé des traits par <em>Ibn Masʿūd</em>, énumère ce que le hadith enseigne, puis fait étudier la définition de l’espérance (<em>ʾamal</em>) et la part qui en est louée ou blâmée d’après le <em>Fatḥ al-Bārī</em> d’<em>Ibn Ḥaǧar</em>, et prépare la leçon qui vient, sur le signe de la foi. N.d.T.\u202f: le cartouche du tirage imprime <span dir="rtl" lang="ar">(الدَّرْسُ ٢٢)</span>\u202f; la numérotation interne du manuel ne compte pas les leçons d’activités non numérotées, alors que le sommaire officiel compte la présente leçon comme la vingt-quatrième de la matière. Ce hadith est le quarantième des Quarante d’<em>al-Nawawī</em> (<em>al-Bukhārī</em> n°\u202f6416).</p>
<h2>Objectifs (<em>ahdāf ad-dars</em> <span dir="rtl" lang="ar">(أَهْدَافُ الدَّرْسِ)</span>)</h2>
<ol>
<li>Que je reconnaisse que le bas-monde est un champ pour l’au-delà (<em>ʾan ʾataʿarrafa ʾanna d-dunyā mazraʿatun li-l-āḫira</em> <span dir="rtl" lang="ar">(أَنْ أَتَعَرَّفَ أَنَّ الدُّنْيَا مَزْرَعَةٌ لِلْآخِرَةِ.)</span>).</li>
<li>Que je saisisse la valeur du temps dans ma vie (<em>ʾan ʾudrika qīmata l-waqti fī ḥayātī</em> <span dir="rtl" lang="ar">(أَنْ أُدْرِكَ قِيمَةَ الْوَقْتِ فِي حَيَاتِي.)</span>).</li>
<li>Que je m’applique à exploiter mes temps en ce qui m’est utile (<em>ʾan ʾuḥriṣa ʿalà stiġlāli ʾawqātī fīmā yufīdunī</em> <span dir="rtl" lang="ar">(أَنْ أُحْرِصَ عَلَى اسْتِغْلَالِ أَوْقَاتِي فِيمَا يُفِيدُنِي.)</span>).</li>
</ol>
<h2>Introduction (<em>tamhīd</em> <span dir="rtl" lang="ar">(تَمْهِيد)</span>)</h2>
<p>J’ai observé la sagesse de Dieu, puissant et majestueux, d’avoir donné à l’homme une première vie en ce bas-monde et une seconde vie dans l’au-delà, chacune des deux ayant une mission qui la distingue de l’autre\u202f: la première, Il en a fait une étape de passage, de semailles, d’occasions à saisir et de provision à faire\u202f; la seconde, une station où demeurer et de rétribution. Comment donc franchirai-je les étapes de la vie de ce bas-monde\u202f? Comment en tirerai-je profit et comment en ferai-je un champ pour l’au-delà\u202f? (<em>ʾiftaqadtu ḥikmata llāhi ʿazz wa-ǧall ʾan yaǧʿala li-l-ʾinsāni ḥayātan ūlà fī hāḏihī d-dunyā, wa-ḥayātan ṯāniyatan fī l-āḫira, wa-li-kullin minhumā muhimmatun taḫtaṣṣu bihā ʿani l-ʾuḫrà, fa-ǧaʿala l-ūlà marḥalata ʿubūrin wa-zirʿin wa-ġtināmin wa-tazawwudin, wa-ǧaʿala ṯ-ṯāniyata maḥaṭṭati stiqrārin wa-ǧazāʾ. fa-kayfa ʾaʿburu marāḥila l-ḥayāti d-dunyā? wa-kayfa ʾaġnamuhā wa-ʾaǧʿaluhā mazraʿatan li-l-āḫira?</em> <span dir="rtl" lang="ar">(اِفْتَقَدْتُ حِكْمَةَ اللهِ عَزَّ وَجَلَّ أَنْ يَجْعَلَ لِلْإِنْسَانِ حَيَاةً أُولَى فِي هَذِهِ الدُّنْيَا، وَحَيَاةً ثَانِيَةً فِي الْآخِرَةِ، وَلِكُلٍّ مِنْهُمَا مُهِمَّةٌ تَخْتَصُّ بِهَا عَنِ الْأُخْرَى، فَجَعَلَ الْأُولَى مَرْحَلَةَ عُبُورٍ وَزِرْعٍ وَاغْتِنَامٍ وَتَزَوُّدٍ، وَجَعَلَ الثَّانِيَةَ مَحَطَّةَ اسْتِقْرَارٍ وَجَزَاءٍ. فَكَيْفَ أَعْبُرُ مَرَاحِلَ الْحَيَاةِ الدُّنْيَا؟ وَكَيْفَ أَغْنَمُهَا وَأَجْعَلُهَا مَزْرَعَةً لِلْآخِرَةِ؟)</span>)</p>
<h2>Le hadith</h2>
<p>D’après <em>Ibn ʿUmar</em> — que Dieu les agrée —, qui a dit\u202f: l’Envoyé de Dieu ﷺ m’a saisi par l’épaule et a dit\u202f: «\u202fsois en ce bas-monde comme si tu étais un étranger ou un passant\u202f». Et <em>Ibn ʿUmar</em> — que Dieu les agrée — se plaisait à dire\u202f: «\u202fquand tu passes la soirée, n’attends pas le matin\u202f; quand tu passes le matin, n’attends pas le soir\u202f; prends de ta santé pour ta maladie, et de ta vie pour ta mort\u202f» [rapporté par <em>al-Bukhārī</em>] (<em>ʿan ’Ibni ʿUmarin raḍiya llāhu ʿanhumā qāla: ʾaḫaḏa rasūla llāhi ﷺ bi-mankibī, fa-qāla: «kun fī d-dunyā ka-ʾannaka ġarībun ʾaw ʿābiru sabīl». wa-kāna ’Ibnu ʿUmarin raḍiya llāhu ʿanhumā yaqūlu: «ʾiḏā ʾamsayta fa-lā tantaẓiri ṣ-ṣabāḥa, wa-ʾiḏā ʾaṣbaḥta fa-lā tantaẓiri l-masāʾa, wa-ḫuḏ min ṣiḥḥatika li-maraḍika, wa-min ḥayātika li-mawtik». [rawāhu l-Buḫārī]</em> <span dir="rtl" lang="ar">(عَنْ ابْنِ عُمَرَ رَضِيَ اللهُ عَنْهُمَا قَالَ: أَخَذَ رَسُولُ اللهِ ﷺ بِمَنْكِبِي، فَقَالَ: «كُنْ فِي الدُّنْيَا كَأَنَّكَ غَرِيبٌ أَوْ عَابِرُ سَبِيلٍ». وَكَانَ ابْنُ عُمَرَ رَضِيَ اللهُ عَنْهُمَا يَقُولُ: «إِذَا أَمْسَيْتَ فَلَا تَنْتَظِرِ الصَّبَاحَ، وَإِذَا أَصْبَحْتَ فَلَا تَنْتَظِرِ الْمَسَاءَ، وَخُذْ مِنْ صِحَّتِكَ لِمَرَضِكَ، وَمِنْ حَيَاتِكَ لِمَوْتِكَ». [رَوَاهُ الْبُخَارِيُ]</span>).</p>
<h2>Notice du transmetteur (<em>tarǧamat ar-rāwī</em> <span dir="rtl" lang="ar">(تَرْجَمَةُ الرَّاوِي)</span>)</h2>
<p><em>ʿAbdallāh</em> b. <em>ʿUmar</em> b. <em>al-Khaṭṭāb</em> al-’<em>ʿAdawī</em> — que Dieu l’agrée\u202f: Compagnon éminent\u202f; il intervenait de lui-même, au grand jour, au nom de la vérité, et fut le plus fort des hommes pendant deux années. On a dit de lui, après sa mort\u202f: <em>Ibn ʿUmar</em> est mort, lui qui était semblable à <em>ʿUmar</em> par le mérite\u202f; <em>ʿUmar</em> avait, en son temps, des égaux, tandis qu’<em>Ibn ʿUmar</em> vécut son temps sans que nul ne lui fût pareil. Il est décédé en l’an\u202f73 de l’Hégire (<em>ʿAbdu llāhi bnu ʿUmarin bnu l-Ḫaṭṭābi l-ʿAdawiyyu raḍiya llāhu ʿanhu; ṣaḥābiyyun ǧalīlun, kāna ǧarriyyan ǧuhayran bi-l-ḥaqqi, ʾaqwà n-nāsi sannatayni sanatan. qīla fīhi baʿda mawtihi: māta ’Ibnu ʿUmar, wa-huwa miṯlu ʿUmarin fī l-faḍli, wa-kāna ʿUmaru fī zamānihi lahu fīhi nuẓarāʾ, wa-ʿāša ’Ibnu ʿUmarin fī zamānihi laysa lahu fīhi naẓīr. tuwuffiya sanata: «73h».</em> <span dir="rtl" lang="ar">(عَبْدُ اللهِ بْنُ عُمَرَ بْنُ الْخَطَّابِ الْعَدَوِيِّ رَضِيَ اللهُ عَنْهُ؛ صَحَابِيٌّ جَلِيلٌ، كَانَ جَرِّيًّا جُهَّيْرًا بِالْحَقِّ، أَقْوَى النَّاسِ سَنَّتَيْنِ سَنَةً. قِيلَ فِيهِ بَعْدَ مَوْتِهِ: مَاتَ ابْنُ عُمَرَ، وَهُوَ مِثْلُ عُمَرَ فِي الْفَضْلِ، وَكَانَ عُمَرُ فِي زَمَانِهِ لَهُ فِيهِ نُظَرَاءُ، وَعَاشَ ابْنُ عُمَرَ فِي زَمَانِهِ لَيْسَ لَهُ فِيهِ نَظِيرٌ. تُوُفِّيَ سَنَةَ: «73هـ».)</span>).</p>
<p>N.d.T.\u202f: le tirage imprime <span dir="rtl" lang="ar">(رَضِيَ اللهُ عَنْهُ)</span> au singulier en tête de la notice, alors que le sanad du hadith porte <span dir="rtl" lang="ar">(عَنْهُمَا)</span> — doublet conservé tel quel. La séquence <span dir="rtl" lang="ar">(كَانَ جَرِّيًّا جُهَّيْرًا بِالْحَقِّ، أَقْوَى النَّاسِ سَنَّتَيْنِ سَنَةً)</span> n’a pas été retrouvée telle quelle dans les biographies classiques consultées\u202f; l’<em>ʾIṣāba</em> rapporte d’<em>Abū Salama</em> b. <em>ʿAbd al-Raḥmān</em>\u202f: <span dir="rtl" lang="ar">(مَاتَ ابْنُ عُمَرَ، وَهُوَ مِثْلُ عُمَرَ فِي الْفَضْلِ، وَكَانَ عُمَرُ فِي زَمَانٍ لَهُ فِيهِ نُظَرَاءُ، وَعَاشَ ابْنُ عُمَرَ فِي زَمَانٍ لَيْسَ لَهُ فِيهِ نَظِيرٌ)</span> — le tirage imprime <span dir="rtl" lang="ar">(فِي زَمَانِهِ)</span> là où le canon lit <span dir="rtl" lang="ar">(فِي زَمَانٍ)</span>, écart grammatical consigné sans correction du tirage.</p>
<h2>L’explication (<em>aš-šarḥ</em> <span dir="rtl" lang="ar">(الشَّرْحُ)</span>)</h2>
<ul>
<li><em>bi-mankibī</em> <span dir="rtl" lang="ar">(بِمَنْكِبِي)</span> — «\u202fpar mon épaule\u202f»\u202f: <em>al-mankib</em> <span dir="rtl" lang="ar">(الْمَنْكِبُ)</span>, le lieu où se rejoignent la tête de l’omoplate et le bras (<em>muǧtamaʿu raʾsi l-katifi wa-l-ʿaḍud</em> <span dir="rtl" lang="ar">(مُجْتَمَعُ رَأْسِ الكَتِفِ وَالْعَضَدِ.)</span>)\u202f;</li>
<li><em>ʿābiru sabīl</em> <span dir="rtl" lang="ar">(عَابِرُ سَبِيلٍ)</span> — «\u202fun passant\u202f»\u202f: celui qui chemine sur la route et le voyageur (<em>huwa l-māru bi-ṭ-ṭarīqi wa-l-musāfiru</em> <span dir="rtl" lang="ar">(هُوَ الْمَارُ بِالطَّرِيقِ وَالْمُسَافِرُ.)</span>).</li>
</ul>
<h2>L’extraction des idées (<em>istiḫlāṣ al-maḍāmīn</em> <span dir="rtl" lang="ar">(اسْتِخْلَاصُ الْمَضَامِينِ)</span>)</h2>
<ol>
<li>Par quoi l’Envoyé de Dieu ﷺ a-t-il ordonné dans ce hadith\u202f? (<em>bi-mā ʾamara r-rasūlu ﷺ fī hāḏā l-ḥadīṯ?</em> <span dir="rtl" lang="ar">(بِمَ أَمَرَ الرَّسُولُ ﷺ فِي هَذَا الْحَدِيثِ؟)</span>).</li>
<li>Quelle est la recommandation qu’<em>Ibn ʿUmar</em> — que Dieu l’agrée — a transmise\u202f? (<em>mā l-waṣiyyatu llatī qaddamahā ’Ibnu ʿUmarin raḍiya llāhu ʿanhu?</em> <span dir="rtl" lang="ar">(مَا الوَصِيَّةُ التِي قَدَّمَهَا ابْنُ عُمَرَ رَضِيَ اللهُ عَنْهُ؟)</span>).</li>
</ol>
<h2>L’analyse (<em>at-taḥlīl</em> <span dir="rtl" lang="ar">(التَّحْلِيلُ)</span>)</h2>
<p>Le hadith guide vers le départ en ce bas-monde, vers l’abandon de la préoccupation qu’on lui accorde au détriment de l’au-delà, vers la recherche des œuvres pieuses en ce bas-monde pour faire provision pour l’au-delà, et vers l’application à saisir les temps avant qu’ils ne se perdent\u202f; le propos s’en tiendra à ce qui suit (<em>yuršidu l-ḥadīṯu ʾilà r-raḥli fī d-dunyā, wa-tarki l-inšiġāli bihā ʿani l-āḫira, wa-ṭalabi l-ʾaʿmāli ṣ-ṣāliḥati fīhā li-t-tazawwudi li-l-āḫira, wa-l-ḥarṣi ʿalà ġtināmi l-ʾawqāti qabla fawātihā, wa-l-kalāmu fī ḏālika ʿalà mā yaʾtī:</em> <span dir="rtl" lang="ar">(يُرْشِدُ الْحَدِيثُ إِلَى الرَّحْلِ فِي الدُّنْيَا، وَتَرْكِ الاِنْشِغَالِ بِهَا عَنِ الْآخِرَةِ، وَطَلْبِ الْأَعْمَالِ الصَّالِحَةِ فِيهَا لِلتَّزَوُّدِ لِلْآخِرَةِ، وَالْحَرْصِ عَلَى اِغْتِنَامِ الْأَوْقَاتِ قَبْلَ فَوَاتِهَا، وَالكَلَامُ فِي ذَلِكَ عَلَى مَا يَأْتِي:)</span>)</p>
<h3>Premièrement\u202f: le bas-monde est un moyen d’accéder à l’au-delà (<em>ʾawwalan: ad-dunyā wasīlatun li-l-āḫira</em> <span dir="rtl" lang="ar">(أَوَّلًا: الدُّنْيَا وَسِيلَةٌ لِلْآخِرَةِ)</span>)</h3>
<p>Guide vers cela la parole du Prophète ﷺ\u202f: «\u202fsois en ce bas-monde comme si tu étais un étranger ou un passant\u202f»\u202f: de sorte que l’homme doit se tenir en ce bas-monde à la manière de l’étranger qui a débarqué dans une terre d’exil\u202f; de même que l’étranger ne s’appuie sur personne, il ne s’appuie pas sur le bas-monde\u202f; de même que l’étranger ne fait pas du pays d’exil sa patrie, il ne fait pas du bas-monde une patrie\u202f; et qu’il se contente, pour ses besoins en ce bas-monde, de la mesure de quoi l’étranger se contente dans le pays d’exil. Ceci indique l’ascétisme à l’égard du bas-monde, pour n’en prendre que le nécessaire et le suffisant\u202f; de même que le passant n’a besoin de rien de plus que ce qui le mène au terme de son voyage, de même le croyant n’a besoin, en ce bas-monde, de rien de plus que ce qui le mène (<em>yuršidu qawluhu ﷺ: «kun fī d-dunyā ka-ʾannaka ġarībun ʾaw ʿābiru sabīlin» ʾilà ʾani l-ʾinsānu yanbaġī ʾan yaǧʿala nafsahu fī d-dunyā bi-manzilati l-ġarībi llaḏī ḥalla bi-dāri ġurbatin, fa-lā yarkanu ʾilà d-dunyā kamā lā yarkanu l-ġarību ʾilà ʾaḥad, wa-lā yattaḫiḏu d-dunyā waṭanan kamā lā yattaḫiḏu l-ġarību dāra l-ġurbati waṭanan, wa-lyaktafi min ḥāǧatihi fī d-dunyā bi-qadri mā yaktafī bihi l-ġarību fī dāri l-ġurbati. wa-hāḏà yadullu ʿalà z-zuhdi fī d-dunyā li-yaʾḫuḏa l-ballāġata minhā wa-l-kafāfa; fa-kamā lā yaḥtāǧu ʿābiru s-sabīli ʾilà ʾakṯari mimmā yubliġuhu ʾilà ġāyati safarih, ka-ḏàlika lā yaḥtāǧu l-muʾminu fī d-dunyā ʾilà ʾakṯari mimmā yubliġuh.</em> <span dir="rtl" lang="ar">(يُرْشِدُ قَوْلُهُ ﷺ: «كُنْ فِي الدُّنْيَا كَأَنَّكَ غَرِيبٌ أَوْ عَابِرُ سَبِيلٍ» إِلَى أَنِ الْإِنْسَانُ يَنْبَغِي أَنْ يَجْعَلَ نَفْسَهُ فِي الدُّنْيَا بِمَنْزِلَةِ الْغَرِيبِ الَّذِي حَلَّ بِدَارِ غُرْبَةٍ، فَلَا يَرْكَنُ إِلَى الدُّنْيَا كَمَا لَا يَرْكَنُ الْغَرِيبُ إِلَى أَحَدٍ، وَلَا يَتَّخِذُ الدُّنْيَا وَطَنًا كَمَا لَا يَتَّخِذُ الْغَرِيبُ دَارَ الْغُرْبَةِ وَطَنًا، وَلْيَكْتَفِ مِنْ حَاجَتِهِ فِي الدُّنْيَا بِقَدْرِ مَا يَكْتَفِي بِهِ الْغَرِيبُ فِي دَارِ الْغُرْبَةِ. وَهَذَا يَدُلُّ عَلَى الزُّهْدِ فِي الدُّنْيَا لِيَأْخُذَ الْبَلَّغَةَ مِنْهَا وَالْكَفَافَ؛ فَكَمَا لَا يَحْتَاجُ عَابِرُ السَّبِيلِ إِلَى أَكْثَرِ مِمَّا يُبْلِغُهُ إِلَى غَايَةِ سَفَرِهِ، كَذَلِكَ لَا يَحْتَاجُ الْمُؤْمِنُ فِي الدُّنْيَا إِلَى أَكْثَرِ مِمَّا يُبْلِغُهُ.</span>))</p>
<h3>Deuxièmement\u202f: la manière de saisir les temps (<em>ṯāniyan: kayfiyyatu ġtināmi l-ʾawqāt</em> <span dir="rtl" lang="ar">(ثَانِيًا: كَيْفِيَّةُ اغْتِنَامِ الْأَوْقَاتِ)</span>)</h3>
<p>La parole d’<em>Ibn ʿUmar</em> — que Dieu les agrée —\u202f: «\u202fquand tu passes la soirée, n’attends pas le matin\u202f; quand tu passes le matin, n’attends pas le soir\u202f; prends de ta santé pour ta maladie, et de ta vie pour ta mort\u202f» renferme quatre recommandations qui s’incarnent dans le fait que le croyant (<em>yataḍammanu qawlu ’Ibni ʿUmarin raḍiya llāhu ʿanhumā: «ʾiḏā ʾamsayta fa-lā tantaẓiri ṣ-ṣabāḥa, wa-ʾiḏā ʾaṣbaḥta fa-lā tantaẓiri l-masāʾa, wa-ḫuḏ min ṣiḥḥatika li-maraḍika, wa-min ḥayātika li-mawtik» ʾarbaʿa waṣāya tatamattaṯalu fī ʾanna l-muʾmina:</em> <span dir="rtl" lang="ar">(يَتَضَمَّنُ قَوْلُ ابْنِ عُمَرَ رَضِيَ اللهُ عَنْهُمَا: «إِذَا أَمْسَيْتَ فَلَا تَنْتَظِرِ الصَّبَاحَ، وَإِذَا أَصْبَحْتَ فَلَا تَنْتَظِرِ الْمَسَاءَ، وَخُذْ مِنْ صِحَّتِكَ لِمَرَضِكَ، وَمِنْ حَيَاتِكَ لِمَوْتِكَ» أَرْبَعَ وَصَايَا تَتَمَثَّلُ فِي أَنَّ الْمُؤْمِنَ:)</span>)</p>
<ul>
<li>il se tient en tout temps prêt pour la mort par l’œuvre pieuse, se hâtant vers l’action avant qu’elle ne se perde (<em>yastaʿiddu ʾabadan li-l-mawti bi-l-ʿamali ṣ-ṣāliḥi, fa-yubādiru bi-l-ʿamali qabla l-fawāt</em> <span dir="rtl" lang="ar">(يَسْتَعِدُّ أَبَدًا لِلْمَوْتِ بِالْعَمَلِ الصَّالِحِ، فَيُبَادِرُ بِالْعَمَلِ قَبْلَ الْفَوَاتِ.)</span>)\u202f;</li>
<li>il fait de courtes espérances, sans différer l’action au matin quand le soir tombe, ni au soir quand le matin se lève (<em>yuqaṣṣiru l-ʾamala, fa-lā yuʾaḫḫiru l-ʿamala li-ṣ-ṣabāḥi ʾiḏā ʾamsà, wa-lā li-l-layli ʾiḏā ʾaṣbaḥ</em> <span dir="rtl" lang="ar">(يُقَصِّرُ الْأَمَلَ، فَلَا يُؤَخِّرُ الْعَمَلَ لِلصَّبَاحِ إِذَا أَمْسَى، وَلَا لِلَّيْلِ إِذَا أَصْبَحَ.)</span>)\u202f;</li>
<li>il fait bon usage du temps de sa santé, craignant qu’une maladie ne survienne qui l’empêcherait d’agir (<em>yaġtanimu waqta ṣiḥḥatihi ḫawfan min ḫulūli maraḍin yamnaʿuhu mina l-ʿamal</em> <span dir="rtl" lang="ar">(يَغْتَنِمُ وَقْتَ صِحَّتِهِ خَوْفًا مِنْ خُلُولِ مَرَضٍ يَمْنَعُهُ مِنَ الْعَمَلِ.)</span>)\u202f;</li>
<li>il fait bon usage des jours de sa vie, craignant que la mort ne survienne, que son œuvre ne soit rompue et que son regret ne s’accroisse (<em>yaġtanimu ʾayyāma ḥayātihi ḫawfan min ḫulūli l-mawti fa-yinqaṭiʿa ʿamaluhu, wa-taʿẓuma ḥasratuh</em> <span dir="rtl" lang="ar">(يَغْتَنِمُ أَيَّامَ حَيَاتِهِ خَوْفًا مِنْ خُلُولِ الْمَوْتِ فَيَنْقَطِعُ عَمَلُهُ، وَتَعْظُمُ حَسْرَتُهُ.)</span>).</li>
</ul>
<p><em>ʿAlī</em> — que Dieu l’agrée — a dit\u202f: «\u202fle bas-monde s’en est allé tournant le dos, et l’au-delà s’en vient tournant vers nous\u202f; chacune des deux a des fils\u202f: soyez des fils de l’au-delà, et non des fils du bas-monde\u202f; aujourd’hui, l’œuvre sans le calcul\u202f; demain, le calcul sans l’œuvre\u202f» [<em>Ṣaḥīḥ al-Bukhārī</em>, chapitre sur l’espérance et sa longueur] (<em>waqāla ʿAliyyun raḍiya llāhu ʿanhu: «irtaḥalati d-dunyā mudbiratan, wa-irtaḥalati l-āḫiratu muqbilatan, wa-li-kulli wāḥidatin minhumā bunūn, fa-kūnū min ʾabnāʾi l-āḫira, wa-lā takūnū min ʾabnāʾi d-dunyā; fa-ʾinna l-yawma ʿamalun wa-lā ḥisāb, wa-ġadan ḥisābun wa-lā ʿamal». [Ṣaḥīḥu l-Buḫārīyy, bābun fī l-ʾamali wa-ṭūlihi]</em> <span dir="rtl" lang="ar">(وَقَالَ عَلِيٌّ رَضِيَ اللهُ عَنْهُ: «اِرْتَحَلَتِ الدُّنْيَا مُدْبِرَةً، وَارْتَحَلَتِ الْآخِرَةُ مُقْبِلَةً، وَلِكُلِّ وَاحِدَةٍ مِنْهُمَا بُنُونَ، فَكُونُوا مِنْ أَبْنَاءِ الْآخِرَةِ، وَلَا تَكُونُوا مِنْ أَبْنَاءِ الدُّنْيَا؛ فَإِنَّ الْيَوْمَ عَمَلٌ وَلَا حِسَابٌ، وَغَدًا حِسَابٌ وَلَا عَمَلٌ». [صَحِيحُ الْبُخَارِيِّ، بَابٌ فِي الْأَمَلِ وَطُولِهِ]</span>)).</p>
<p><em>Ibn Masʿūd</em> — que Dieu l’agrée — a dit\u202f: le Prophète ﷺ traça des traits et dit\u202f: «\u202fvoici l’homme, voici l’espérance, voici le terme\u202f; et tandis qu’il en était ainsi, voici que vint le trait le plus proche\u202f» [<em>Ṣaḥīḥ al-Bukhārī</em>, <em>Kitāb ar-riqāq</em>, chapitre sur l’espérance et sa longueur]\u202f; c’est le terme qui l’enserre. Que le croyant rende donc son âme consentante à l’action, et qu’il lutte contre son âme\u202f: elle est contrainte par l’espérance (<em>waqāla ’Ibnu Masʿūdin raḍiya llāhu ʿanhu: ḫaṭṭa n-nabiyyu ﷺ ḫuṭūṭan fa-qāla: «hāḏà l-ʾinsānu, wa-hāḏà l-ʾamalu, wa-hāḏà l-ʾaǧalu, fa-baynamā huwa ka-ḏàlika ʾiḏ ǧāʾa l-ḫaṭṭu l-ʾaqrabu» [Ṣaḥīḥu l-Buḫārīyy, Kitābu r-Riqāq, bābun fī l-ʾamali wa-ṭūlihi], wa-huwa l-ʾaǧalu l-muḥīṭu bih. fa-lyarḍa l-muʾminu nafsahu ʿalà l-ʿamali, wa-lyuǧāhid nafsahu, fa-ʾinnahā maǧbūlatun ʿalà l-ʾamal.</em> <span dir="rtl" lang="ar">(وَقَالَ ابْنُ مَسْعُودٍ رَضِيَ اللهُ عَنْهُ: خَطَّ النَّبِيُّ ﷺ خُطُوطًا فَقَالَ: «هَذَا الْإِنْسَانُ، وَهَذَا الْأَمَلُ، وَهَذَا الْأَجَلُ، فَبَيْنَمَا هُوَ كَذَلِكَ إِذْ جَاءَ الْخَطُّ الْأَقْرَبُ» [صَحِيحُ الْبُخَارِيِّ، كِتَابُ الرِّقَاقِ، بَابٌ فِي الْأَمَلِ وَطُولِهِ]، وَهُوَ الْأَجَلُ الْمُحِيطُ بِهِ. فَلْيَرْضَ الْمُؤْمِنُ نَفْسَهُ عَلَى الْعَمَلِ، وَلْيُجَاهِدْ نَفْسَهُ، فَإِنَّهَا مَجْبُولَةٌ عَلَى الْأَمَلِ.</span>)). N.d.T.\u202f: le tirage attribue ces paroles à <em>Ibn Masʿūd</em> sous la forme <span dir="rtl" lang="ar">(خَطَّ النَّبِيُّ ﷺ خُطُوطًا... «هَذَا الْإِنْسَانُ، وَهَذَا الْأَمَلُ، وَهَذَا الْأَجَلُ...»)</span> — dans le <em>Ṣaḥīḥ al-Bukhārī</em> reçu, la version des traits simples (<span dir="rtl" lang="ar">(هَذَا الْإِنْسَانُ وَهَذَا أَجَلُهُ فَبَيْنَمَا هُوَ كَذَلِكَ إِذْ جَاءَ الْخَطُّ الْأَقْرَبُ</span>, n°\u202f6418) est rapportée d’<em>ʾAnas</em>, tandis qu’<em>Ibn Masʿūd</em> rapporte la version du tracé quadrillé (n°\u202f6417)\u202f; la mention <span dir="rtl" lang="ar">(وَهَذَا الْأَمَلُ)</span> n’y figure pas — écarts consignés, tirage non corrigé.</p>
<h2>Ce que le hadith enseigne (<em>mimmā yustafādu min hāḏà l-ḥadīṯ</em> <span dir="rtl" lang="ar">(مِمَّا يُسْتَفَادُ مِنْ هَذَا الْحَدِيثِ:)</span>)</h2>
<ul>
<li>le discernement du bas-monde comme demeure d’œuvre et de passage, et de l’au-delà comme demeure de rétribution et de séjour (<em>ʾiʿtibāru d-dunyā dāra ʿamalin wa-ntiqāl, wa-l-āḫirata dāra ǧazāʾin wa-stiqrār</em> <span dir="rtl" lang="ar">(إِعْتِبَارُ الدُّنْيَا دَارَ عَمَلٍ وَانْتِقَالٍ، وَالْآخِرَةُ دَارَ جَزَاءٍ وَاسْتِقْرَارٍ.)</span>)\u202f;</li>
<li>le raccourcissement de l’espérance, la course vers le repentir et l’œuvre, et la provision pour la demeure de l’au-delà (<em>taqṣīru l-ʾamal, wa-l-musāraʿatu ʾilà t-tawbati wa-l-ʿamal, wa-t-tazawwudi li-d-dāri l-āḫira</em> <span dir="rtl" lang="ar">(تَقْصِيرُ الْأَمَلِ، وَالْمُسَارَعَةُ إِلَى التَّوْبَةِ وَالْعَمَلِ، وَالتَّزَوُّدُ لِلدَّارِ الْآخِرَةِ.)</span>)\u202f;</li>
<li>l’application à saisir les temps, et la garde contre d’en négliger la mise en valeur (<em>l-ḥarṣu ʿalà ġtināmi l-ʾawqāt, wa-l-ḥaḏaru mina t-tafrīṭi fīhā bi-taḍyīʿihā</em> <span dir="rtl" lang="ar">(اِلْحَرْصُ عَلَى اِغْتِنَامِ الْأَوْقَاتِ، وَالْحَذَرُ مِنَ التَّفْرِيطِ فِيهَا بِتَضْيِيعِهَا.)</span>)\u202f;</li>
<li>la lutte contre l’âme jusqu’à ce qu’elle ne s’appuie pas sur le bas-monde, de crainte que l’œuvre ne se perde dans le mirage de l’espérance (<em>muǧāhadatu n-nafsi ḥattà lā tarkanu ʾilà d-dunyā, fa-yaḍīʿa l-ʿamalu bi-sarābi l-ʾamal</em> <span dir="rtl" lang="ar">(مُجَاهَدَةُ النَّفْسِ حَتَّى لَا تَرْكَنَ إِلَى الدُّنْيَا، فَيَضِيعَ الْعَمَلُ بِسَرَابِ الْأَمَلِ.)</span>).</li>
</ul>
<h2>L’évaluation (<em>at-taqwīm</em> <span dir="rtl" lang="ar">(التَّقْوِيمُ)</span>)</h2>
<ol>
<li>Quelle utilité tires-tu de ce passage\u202f: «\u202fsois en ce bas-monde comme si tu étais un étranger ou un passant\u202f»\u202f? (<em>māḏā tastafīdu min hāḏà l-maqṭaʿi: «kun fī d-dunyā ka-ʾannaka ġarībun ʾaw ʿābiru sabīl»?</em> <span dir="rtl" lang="ar">(مَاذَا تَسْتَفِيدُ مِنْ هَذَا الْمَقْطَعِ: «كُنْ فِي الدُّنْيَا كَأَنَّكَ غَرِيبٌ أَوْ عَابِرُ سَبِيلٍ»؟)</span>).</li>
<li>Je classe dans un schéma les cas de non-exploitation du temps (<em>ʾuṣannifu fī ḫuṭṭāṭatin ʾafrāda ʿadami stiġlāli l-waqt</em> <span dir="rtl" lang="ar">(أُصَنِّفُ فِي خُطَّاطَةٍ أَفْرَادَ عَدَمِ اسْتِغْلَالِ الْوَقْتِ.)</span>).</li>
<li>Je propose des conduites pour tirer profit de mon temps et de ma santé, et je remplis le tableau, dans mon cahier, de ce qui suit (<em>ʾaqteriḥu sulūkātin li-ġtināmi waqtī wa-ṣiḥḥatī, wa-ʾamlaʾu l-ǧadwala fī dafṭarī bi-mā yaʾtī:</em> <span dir="rtl" lang="ar">(أَقْتَرِحُ سُلُوكَاتٍ لِاغْتِنَامِ وَقْتِي وَصِحَّتِي، وَأَمْلَأُ الْجَدْوَلَ فِي دَفْتَرِي بِمَا يَأْتِي:)</span>)</li>
</ol>
<table>
<thead>
<tr><th>Le point (<em>an-nuqṭa</em> <span dir="rtl" lang="ar">(النُّقْطَةُ)</span>)</th><th>Proposer des conduites pour en tirer profit (<em>iqterāḥu sulūkātin li-ġtināmihā</em> <span dir="rtl" lang="ar">(اِقْتِرَاحُ سُلُوكَاتٍ لِاغْتِنَامِهَا)</span>)</th></tr>
</thead>
<tbody>
<tr><td>Le temps (<em>al-waqt</em> <span dir="rtl" lang="ar">(الْوَقْتُ)</span>)</td><td></td></tr>
<tr><td>La santé (<em>aṣ-ṣiḥḥa</em> <span dir="rtl" lang="ar">(الصِّحَّةُ)</span>)</td><td></td></tr>
</tbody>
</table>
<h2>L’enrichissement (<em>al-istithmār</em> <span dir="rtl" lang="ar">(الاسْتِثْمَارُ)</span>)</h2>
<p>L’espérance\u202f: c’est l’attente de ce que l’âme aime, comme la longueur de la vie et l’accroissement de la richesse\u202f; elle est proche, par le sens, du souhait... Et l’espérance est innée chez tous les fils d’Adam, et l’espérance recèle un secret délicat\u202f: car sans l’espérance, nul ne prendrait goût à la vie, et son âme ne se complairait pas à s’engager dans une œuvre d’entre les œuvres du bas-monde\u202f; ce qui est blâmable en elle, c’est le relâchement qui s’y installe et l’absence de préparation à l’affaire de l’au-delà\u202f; celui qui est épargné par cela n’est pas chargé de sa suppression [<em>Fatḥ al-Bārī</em> d’<em>Ibn Ḥaǧar</em>, <em>Kitāb ar-riqāq</em>, chapitre sur l’espérance et sa longueur, avec remaniement] (<em>al-ʾamalu, huwa raǧāʾu mā tuḥibbuhu n-nafsu min ṭūli ʿumrin wa-zīyādati ġinàn, wa-huwa qarībun al-maʿnà mina t-tamannī... wa-l-ʾamalu maṭbūʿun fī ǧamīʿi banī ʾĀdam, wa-fī l-ʾamali sarrun laṭīf; li-ʾannahu lawlā l-ʾamalu mā tahannā ʾaḥadun bi-ʿayšin, wa-lā ṭābat nafsuhu ʾan yašraʿ fī ʿamalin min ʾaʿmāli d-dunyā, wa-ʾinnamā l-maḏmūmu minhu l-istirsālu fīh, wa-ʿadamu l-istiʿdādi li-ʾamri l-āḫira, fa-man salima min ḏālika lam yukallaf bi-ʾizālatih. [Fatḥu l-Bārī li-ʾIbni Ḥaǧar, Kitābu r-Riqāq, bābun fī l-ʾamali wa-ṭūlihi, bi-taṣrif]</em> <span dir="rtl" lang="ar">(الْأَمَلُ، هُوَ رَجَاءُ مَا تَحِبُّهُ النَّفْسُ مِنْ طُولِ عُمْرٍ وَزِيَادَةِ غِنًى، وَهُوَ قَرِيبٌ الْمَعْنَى مِنَ التَّمَنِّي... وَالْأَمَلُ مَطْبُوعٌ فِي جَمِيعِ بَنِي آدَمَ، وَفِي الْأَمَلِ سَرٌّ لَطِيفٌ؛ لِأَنَّهُ لَوْلَا الْأَمَلُ مَا تَهَنَّى أَحَدٌ بِعَيْشٍ، وَلَا طَابَتْ نَفْسُهُ أَنْ يَشْرَعْ فِي عَمَلٍ مِنْ أَعْمَالِ الدُّنْيَا، وَإِنَّمَا الْمَذْمُومُ مِنْهُ الِاسْتِرْسَالُ فِيهِ، وَعَدَمُ الِاسْتِعْدَادِ لِأَمْرِ الْآخِرَةِ، فَمَنْ سَلِمَ مِنْ ذَلِكَ لَمْ يُكَلَّفْ بِإِزَالَتِهِ. [فَتْحُ الْبَارِي لِابْنِ حَجَر، كِتَابُ الرِّقَاقِ، بَابٌ فِي الْأَمَلِ وَطُولِهِ، بِتَصْرِف]</span>)). N.d.T.\u202f: la définition de l’espérance citée par <em>Ibn Ḥaǧar</em> d’après <em>Abū ʿUbayd</em> est conforme au texte reçu (<span dir="rtl" lang="ar">(رَجَاءُ مَا تُحِبُّهُ النَّفْسُ مِنْ طُولِ عُمْرٍ وَزِيَادَةِ غِنًى، وَهُوَ قَرِيبُ الْمَعْنَى مِنَ التَّمَنِّي)</span>)\u202f; les points de suspension du tirage marquent l’omission du développement lexicographique intermédiaire, et la phrase finale <span dir="rtl" lang="ar">(فَمَنْ سَلِمَ مِنْ ذَلِكَ لَمْ يُكَلَّفْ بِإِزَالَتِهِ)</span> est remaniée par rapport au passage du <em>Ḡarīb al-ḥadīṯ</em> — remaniement couvert par la mention <span dir="rtl" lang="ar">(بِتَصْرِف)</span> du tirage.</p>
<ol>
<li>J’extrais du texte la définition de l’espérance (<em>ʾastḫriǧu mina n-naṣṣi taʿrīfa l-ʾamal</em> <span dir="rtl" lang="ar">(أَسْتَخْرِجُ مِنَ النَّصِّ تَعْرِيفَ الْأَمَلِ.)</span>).</li>
<li>J’extrais du texte ce qui est loué de l’espérance et ce qui en est blâmé (<em>ʾastḫriǧu mina n-naṣṣi mā yuḥmadu mina l-ʾamal, wa-mā yuḏammu minhu</em> <span dir="rtl" lang="ar">(أَسْتَخْرِجُ مِنَ النَّصِّ مَا يُحْمَدُ مِنَ الْأَمَلِ، وَمَا يُذَمُّ مِنْهُ.)</span>).</li>
</ol>
<h2>La préparation préalable (<em>al-iʾdād al-qablī</em> <span dir="rtl" lang="ar">(الْإِعْدَادُ الْقَبْلِيُّ)</span>)</h2>
<p>Je mémorise le hadith de la leçon qui vient, et j’en extrais le signe de la foi (<em>ʾaḥfaẓu ḥadīṯa d-darsi l-muwālī, wa-ʾastḫriǧu minhu ʿalāmata l-ʾīmān</em> <span dir="rtl" lang="ar">(أَحْفَظُ حَدِيثَ الدَّرْسِ الْمُوَالِي، وَأَسْتَخْرِجُ مِنْهُ عَلَامَةَ الْإِيمَانِ.)</span>).</p>
"""

SPAN = re.compile(r'(<span dir="rtl" lang="ar">.*?</span>)', re.S)

# --- normalisation typographique (espaces fines U+202F hors spans arabes) ---
out = []
for part in SPAN.split(HTML):
    if part.startswith('<span dir="rtl"'):
        out.append(part)
        continue
    p = part
    p = re.sub(r' +([;:?!»])', '\u202f\\1', p)
    p = re.sub(r'(«) +', '\\1\u202f', p)
    out.append(p)
HTML = "".join(out)

# --- contrôles FR-seule ---
assert "'" not in HTML, "apostrophe droite résiduelle"
outside = []
for seg in SPAN.split(HTML):
    if seg.startswith('<span dir="rtl"') or seg.endswith('</span>'):
        continue
    if re.search(r'[\u0621-\u064A]', seg) and 'ﷺ' not in seg:
        outside.append(seg[:60])
outside = [s for s in outside if re.search(r'[\u0621-\u064A]', s)]
assert not outside, f"arabe hors span: {outside[:3]}"
assert HTML.count('«') == HTML.count('»'), f"guillemets déséquilibrés {HTML.count('«')}/{HTML.count('»')}"
narrow = HTML.count('\u202f')
print(f"contrôles OK — U+202F ×{narrow}, guillemets {HTML.count('«')}")

if "--write" in sys.argv:
    import json
    d = json.load(open(BOOK))
    slot = d["lessons"][IDX]
    assert slot["docId"] == "pdf-mut23h3b-704", slot["docId"]
    if (slot.get("htmlFr") or "").strip():
        print("note : slot déjà rempli — régénération par le même script de livraison")
    slot["htmlFr"] = HTML
    json.dump(d, open(BOOK, "w"), ensure_ascii=False, indent=2)
    print("OK — htmlFr livré pour", slot["docId"], ":", len(HTML), "caractères")
else:
    print("mode contrôle seul (ajouter --write pour livrer) —", len(HTML), "caractères")

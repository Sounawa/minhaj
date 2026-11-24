#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# IA-2 — livraison-h6-21 : traduction française (htmlFr) de la leçon 21
# «دعم وتطبيق» de hadith-6ep — docId pdf-mut23h3b-701 (pp.115-117).
# Leçon d'activités (3e du manuel après 687/694) récapitulant les leçons 15-20.
# Transcription établie ce tour (Z2-57) : couche _text + tesseract 600/1200/2400
# psm 4/6/7/8/13 (tessdata_best ara) + VLM adjudiqué (microcrops une-mot, rondes
# multiples) + canons internes (leçons 695-700 du même livre, matns déjà livrés)
# + cache Quran scripts-translate/quran-cache.json (sourate 49 vv. 12-13).
# Arbitrages documentés au worklog : أُتَمِّمُ (tesseract ×2 contre VLM أَتْلُو) ;
# أُعَرِّفُ (tesseract 2400 + VLM + canon 687 «أُعَرِّفُ بِالصَّحَابِيَّيْنِ» contre VLM
# isolé أَعْرِفْ) ; أَبِي هُرَيْرَةَ kasra (VLM ×2) ; ابْنِ عَبَّاسٍ (tanwīn kasr, VLM ×2
# contre une passe sans tanwīn) ; التَّحَلِّي (tesseract psm7/8/13 4800 + VLM 4800
# «sommet dépourvu de point» + canon 694 «ثَمَرَاتُ التَّحَلِّي», contre psm4 ligne
# et VLM 3x lisant خ) ; التَّعَايُش (VLM lettre-à-lettre : ʿayn ouverte + yāʾ 2 points
# + šīn, contre tesseract التحابش) ; السَّلَمُ SANS alif (tesseract ×4 stable + analyse
# des composantes : 3 hampes, mīm lié au lām — VLM «السلام» écarté, VLM instable
# dans cette cellule : الماء/والآخرة/والكرام) ; shadda+fatha sur le sīn, damma sur
# le mīm final (composantes identiques à la damma du nūn final d'الأمان) ;
# التعاون (conf tesseract 92.9, contre VLM التعارف) ; الأسس (tesseract ×3, contre
# VLM الأساسي/الأسباب) ; للتعاون (tesseract + VLM lettre wāw, contre VLM page
# للتعارف) ; أَتَأَمَّلُ...وَأُجِيبُ aoriste (canon 687/694, contre VLM impératif) ;
# أَعْرِفُ الْغِيبَةَ forme I (tesseract sans shadda, canon interne أُعَرِّفُ n'ayant pas
# d'objet direct ici) ; الطُّمَأْنِينَةِ damma (canon 698) ; الْقِيمَةُ/مَا يَدُلُّ عَلَيْهَا
# مِنَ الْأَحَادِيثِ (tesseract + VLM, colonne 2 nette) ; versets Ḥuǧurāt 12-13
# conformes au cache Quran (orthographe imlāʾī du tirage, الله développé) ;
# réf [الحجرات: الآيتان ١٢ - ١٣] ; et l'astuce (ةِ) du tirage rendue (ةِ) comme
# en 700.
import re, sys

BOOK = "/home/z/my-project/minhaj/content/books/hadith-6ep.json"
IDX = 21  # lessons[21] = pdf-mut23h3b-701

HTML = """<h1>Consolidation et application</h1>
<p>Vingt-et-unième leçon du manuel «\u202fLe hadith tiré du livre des <em>Arba’ūn</em> nawawiyya de l’imam <em>al-Nawawī</em>, avec le commentaire d’Ibn <em>Daqīq</em> al-’<em>Īd</em>\u202f», à l’intention des élèves de sixième année de l’enseignement primaire traditionnel (<em>ta’līm ’atīq</em>). Leçon de consolidation et d’application (<em>daʿmun wa-t-taṭbīq</em> <span dir="rtl" lang="ar">(دَعْمٌ وَتَطْبِيقٌ)</span>), elle récapitule les six leçons précédentes — la réforme du répréhensible et ses degrés, la fraternité islamique en ses deux parties, des actes vertueux et leur récompense, la générosité de Dieu dans la rétribution des œuvres, l’adoration, moyen de proximité et d’amour [divin] — au travers de quatre activités : des exercices menés dans le cahier — la complétion du hadith sacré de l’inscription des bonnes et des mauvaises actions, le hadith attestant les degrés de la réforme du répréhensible, la complétion du hadith de la fraternité, la preuve à l’appui du fruit de la réunion coranique et du rapprochement par les obligations, la présentation des deux nobles Compagnons <em>Abū Hurayra</em> et <em>Ibn ʿAbbās</em> —\u202f; puis l’étude des deux versets d’<em>al-Ḥuǧurāt</em> — la mise en garde contre la conjecture, l’espionnage et la médisance, et la noblesse de la piété —, suivie de six questions ; l’exploitation des acquis au moyen du tableau des valeurs — fraternité, coopération et solidarité, vivre-ensemble, paix et sûreté —\u202f; enfin la tenue, en classe, du forum «\u202fl’importance de la quête du savoir\u202f» préparé à la leçon précédente, et la préparation de la leçon à venir, sur les fruits de l’amitié et de l’amour de Dieu pour le serviteur. N.d.T.\u202f: leçon d’activités non numérotée du tirage, à l’instar de ses deux devancières de la matière (septième et quatorzième)\u202f; le sommaire officiel compte la présente leçon comme la vingt-et-unième.</p>
<h2>Objectifs des activités (<em>’ahdāfu l-’anšiṭa</em> <span dir="rtl" lang="ar">(أَهْدَافُ الْأَنْشِطَةِ)</span>)</h2>
<ol>
<li>Que j’évalue mes acquisitions de savoir des leçons précédentes (<em>’an ’uqawwima muktasabātī l-maʿrifiyyata mina d-durūsi s-sābiqa</em> <span dir="rtl" lang="ar">(أَنْ أُقَوِّمَ مُكْتَسَبَاتِي الْمَعْرِفِيَّةَ مِنَ الدُّرُوسِ السَّابِقَةِ.)</span>).</li>
<li>Que je m’exerce à comprendre les textes de la Loi et à les analyser (<em>’an ’atadarraba ʿalà fahmi n-nuṣūši š-šarʿiyyati wa-taḥlīlihā</em> <span dir="rtl" lang="ar">(أَنْ أَتَدَرَّبَ عَلَى فَهْمِ النُّصُوصِ الشَّرْعِيَّةِ وَتَحْلِيلِهَا.)</span>).</li>
<li>Que j’emploie mes acquisitions de savoir et d’habileté dans de nouvelles situations (<em>’an ’uwaẓẓifa muktasabātī l-maʿrifiyyata wa-l-mahāriyyata fī waḍʿiyyātin ǧadīda</em> <span dir="rtl" lang="ar">(أَنْ أُوَظِّفَ مُكْتَسَبَاتِي الْمَعْرِفِيَّةَ وَالْمَهَارِيَّةَ فِي وَضْعِيَّاتٍ جَدِيدَةٍ.)</span>).</li>
</ol>
<h2>Activité 1\u202f: je réalise dans mon cahier (<em>an-nišāṭ 1: unǧiz fī daftarī</em> <span dir="rtl" lang="ar">(النشاط 1 - أُنْجِزُ فِي دَفْتَرِي:)</span>)</h2>
<ol>
<li>Je complète ce qui suit\u202f: le Messager de Dieu ﷺ a dit\u202f: «\u202fDieu a inscrit les bonnes actions et les mauvaises actions …\u202f» (<em>’utammimu mā ya’tī: qāla ﷺ: «’inna llāha kataba l-ḥasanāti wa-s-sayyi’āti .......»</em> <span dir="rtl" lang="ar">(أُتَمِّمُ مَا يَأْتِي: قَالَ ﷺ: «إِنَّ اللهَ كَتَبَ الْحَسَنَاتِ وَالسَّيِّئَاتِ .......»)</span>) — le tirage imprime un pointillé que l’élève complète par la suite du hadith sacré d’<em>Ibn ʿAbbās</em> (Bukhārī n° 6491, Muslim n° 131 — dix-neuvième leçon)\u202f: «\u202fPuis Il en a exposé le détail\u202f: quiconque forme l’intention d’une bonne action sans l’accomplir, Dieu la lui inscrit auprès de Lui comme bonne action complète\u202f».</li>
<li>L’incitation au convenable et la prohibition du répréhensible admettent des degrés\u202f; je mentionne le hadith qui l’atteste (<em>li-l-’amri bi-l-maʿrūfi wa-n-nahyi ʿani l-munkari marātib; ’aḏkuru l-ḥadīṯa d-dālla ʿalà ḏālik</em> <span dir="rtl" lang="ar">(لِلْأَمْرِ بِالْمَعْرُوفِ وَالنَّهْيِ عَنِ الْمُنْكَرِ مَرَاتِبُ؛ أَذْكُرُ الْحَدِيثَ الدَّالَّ عَلَى ذَلِكَ.)</span>) — le hadith visé est celui d’<em>Abū Saʿīd al-Ḫudrī</em> (Muslim n° 49 — quinzième leçon)\u202f: «\u202fQuiconque d’entre vous voit un répréhensible, qu’il le change de sa main\u202f».</li>
<li>Je comble le blanc comme il convient\u202f: le Messager de Dieu ﷺ a dit\u202f: «\u202fNe vous enviez pas … la piété est ici … et son honneur\u202f» (<em>’amla’u l-farāġa bi-mā yunāsib; qāla ﷺ: «lā taḥāsadū ....... at-taqwà hāhunā ....... wa-ʿirḍuh»</em> <span dir="rtl" lang="ar">(أَمْلَأُ الْفَرَاغَ بِمَا يُنَاسِبُ؛ قَالَ ﷺ: «لَا تَحَاسَدُوا ....... التَّقْوَى هَاهُنَا ....... وَعِرْضُهُ»)</span>) — le tirage imprime deux pointillés encadrant «\u202fla piété est ici\u202f»\u202f: l’élève y reporte les clauses intermédiaires du hadith de la fraternité d’<em>Abū Hurayra</em> (Muslim n° 2564 — seizième et dix-septième leçons), et le segment final «\u202fet son honneur\u202f» achève «\u202ftout le musulman est interdit au musulman\u202f: son sang, ses biens …\u202f».</li>
<li>Je convoque ce que je garde en mémoire des hadiths, et j’en cite la preuve pour les contenus suivants (<em>’astaḥḍiru mā ’aḥfaẓuhu mina l-’aḥādīṯi wa-’astadillu li-l-maḍāmīni l-’ātiya</em> <span dir="rtl" lang="ar">(أَسْتَحْضِرُ مَا أَحْفَظُهُ مِنَ الْأَحَادِيثِ وَأَسْتَدِلُّ لِلْمَضَامِينِ الْآتِيَةِ:)</span>)\u202f:
<ul>
<li>parmi les fruits de la réunion pour la récitation du Coran et la méditation de ses versets\u202f: l’obtention de la tranquillité et la descente de la sérénité (<em>min fawā’idi l-iǧtimāʿi ʿalà tilāwati l-qur’āni wa-tadabburi ’āyātih: ḥuṣūlu ṭ-ṭuma’nīnati wa-tanazzuli s-sakīnati</em> <span dir="rtl" lang="ar">(مِنْ فَوَائِدِ الِاجْتِمَاعِ عَلَى تِلَاوَةِ الْقُرْآنِ وَتَدَبُّرِ آيَاتِهِ: حُصُولُ الطُّمَأْنِينَةِ وَتَنَزُّلُ السَّكِينَةِ.)</span>) — le hadith d’<em>Abū Hurayra</em>, Muslim n° 2699, dix-huitième leçon\u202f;</li>
<li>le rapprochement de Dieu par les obligations est cause d’obtenir l’amour de Dieu et Son amitié (<em>at-taqarrubu ’ilà llāhi bi-l-farā’iḍi sababun li-nayli maḥabbati llāhi wa-wilāyatih</em> <span dir="rtl" lang="ar">(التَّقَرُّبُ إِلَى اللهِ بِالْفَرَائِضِ سَبَبٌ لِنَيْلِ مَحَبَّةِ اللهِ وَوِلَايَتِهِ.)</span>) — le hadith sacré du rang des amis de Dieu, Bukhārī n° 6502, vingtième leçon.</li>
</ul>
</li>
<li>Je présente les deux nobles Compagnons\u202f: <em>Abū Hurayra</em> et <em>Ibn ʿAbbās</em> — que Dieu les agrée (<em>’uʿarrifu bi-ṣ-ṣaḥābiyyayni l-ǧalīlayn: ’Abī Hurayrata - bni ʿAbbāsin - raḍiya llāhu ʿanhumā</em> <span dir="rtl" lang="ar">(أُعَرِّفُ بِالصَّحَابِيَّيْنِ الْجَلِيلَيْنِ: أَبِي هُرَيْرَةَ - ابْنِ عَبَّاسٍ - رَضِيَ اللهُ عَنْهُمَا.)</span>).</li>
</ol>
<h2>Activité 2 (<em>an-nišāṭ 2</em> <span dir="rtl" lang="ar">(النشاط 2)</span>)</h2>
<p>Dieu le Très-Haut a dit\u202f: «\u202fÔ vous qui croyez\u202f! Évitez beaucoup de conjectures\u202f: de la conjecture, il en est qui est péché\u202f; et ne vous espionnez pas, et ne médisez pas les uns des autres. L’un de vous aimerait-il manger la chair de son frère mort\u202f? — cela vous répugnerait. — Et craignez Dieu\u202f: Dieu est, Lui, Grand Accueillant au repentir, Très Miséricordieux. Ô les gens\u202f! Nous vous avons créés d’un mâle et d’une femelle, et Nous avons fait de vous des peuples et des tribus pour que vous vous connaissiez mutuellement. Le plus noble d’entre vous, auprès de Dieu, est le plus pieux d’entre vous\u202f; Dieu, certes, est savant, parfaitement informé\u202f» <span dir="rtl" lang="ar">[الحجرات: الآيتان ١٢ - ١٣]</span> (<em>qāla llāhu taʿālà: (yā ’ayyuhā lladhīna ’āmanū ṯ-taǧtanibū kaṯīran mina ḏ-ẓanni ’inna baʿḍa ḏ-ẓanni ’iṯm, wa-lā taǧassasū wa-lā yagtab baʿḍukum baʿḍan; ’a-yuḥibbu ’aḥadukum ’an ya’kula laḥma ’aḫīhi maytan fa-karihtumūh? wa-ttaqū llāha ’inna llāha tawwābun raḥīm. yā ’ayyuhā n-nāsu ’innā ḫalaqnākum min ḏakarin wa-unṯà wa-ǧaʿalnākum šuʿūban wa-qabā’ila li-taʿārafū; ’inna ’akramakum ʿinda llāhi ’atqākum, ’inna llāha ʿalīmun ḫabīr) [al-ḥuǧurāt: al-’āyatāni 12-13]</em> <span dir="rtl" lang="ar">(قَالَ اللهُ تَعَالَى: (يَا أَيُّهَا الَّذِينَ آمَنُوا اجْتَنِبُوا كَثِيرًا مِنَ الظَّنِّ إِنَّ بَعْضَ الظَّنِّ إِثْمٌ وَلَا تَجَسَّسُوا وَلَا يَغْتَبْ بَعْضُكُمْ بَعْضًا أَيُحِبُّ أَحَدُكُمْ أَنْ يَأْكُلَ لَحْمَ أَخِيهِ مَيْتًا فَكَرِهْتُمُوهُ وَاتَّقُوا اللهَ إِنَّ اللهَ تَوَّابٌ رَحِيمٌ. يَا أَيُّهَا النَّاسُ إِنَّا خَلَقْنَاكُمْ مِنْ ذَكَرٍ وَأُنْثَى وَجَعَلْنَاكُمْ شُعُوبًا وَقَبَائِلَ لِتَعَارَفُوا إِنَّ أَكْرَمَكُمْ عِنْدَ اللهِ أَتْقَاكُمْ إِنَّ اللهَ عَلِيمٌ خَبِيرٌ) [الحجرات: الآيتان ١٢ - ١٣])</span>).</p>
<h2>Je contemple les deux versets ci-dessus et je réponds aux questions (<em>’ata’ammalu l-’āyatayni ’aʿlāhu wa-’uǧību ʿani l-’as’ilati l-’ātiya</em> <span dir="rtl" lang="ar">(أَتَأَمَّلُ الْآيَتَيْنِ أَعْلَاهُ وَأُجِيبُ عَنِ الْأَسْئِلَةِ الْآتِيَةِ:)</span>)</h2>
<ol>
<li>Je fais voir ce que Dieu a interdit dans le premier verset (<em>’ubayyinu mā nahà llāhu ʿanhu fī l-’āyati l-’ūlà</em> <span dir="rtl" lang="ar">(أُبَيِّنُ مَا نَهَى اللهُ عَنْهُ فِي الْآيَةِ الْأُولَى.)</span>).</li>
<li>Je fais connaître la médisance (<em>’aʿrifu l-ġība</em> <span dir="rtl" lang="ar">(أَعْرِفُ الْغِيبَةَ.)</span>).</li>
<li>À quoi Dieu a-t-Il assimilé le médisant dans le verset (<em>bi-ma šabbaha llāhu l-muġtāba fī l-’āya</em> <span dir="rtl" lang="ar">(بِمَ شَبَّهَ اللهُ الْمُغْتَابَ فِي الْآيَةِ؟)</span>)\u202f?</li>
<li>Je fais voir les effets de la médisance sur les valeurs de la fraternité (<em>’ubayyinu ’āṯāra l-ġībati ʿalà qīmi l-’uḫuwwa</em> <span dir="rtl" lang="ar">(أُبَيِّنُ آثَارَ الْغِيبَةِ عَلَى قِيَمِ الْأُخُوَّةِ.)</span>).</li>
<li>Dans le second verset, Dieu s’adresse aux hommes tous ensemble\u202f; je fais voir le contenu de cette adresse (<em>fī l-’āyati ṯ-ṯāniyati yuḫāṭibu llāhu n-nāsa kāffa; ’ubayyinu maḍmūna hāḏà l-ḫaṭāb</em> <span dir="rtl" lang="ar">(فِي الْآيَةِ الثَّانِيَةِ يُخَاطِبُ اللهُ النَّاسَ كَافَّةً؛ أُبَيِّنُ مَضْمُونَ هَذَا الْخِطَابِ.)</span>).</li>
<li>Je propose deux moyens pratiques de coopérer avec autrui (<em>’aqtariḥu wasīlatayni ʿamaliyyatayni li-t-taʿāwuni maʿa l-’āḫar</em> <span dir="rtl" lang="ar">(أَقْتَرِحُ وَسِيلَتَيْنِ عَمَلِيَّتَيْنِ لِلتَّعَاوُنِ مَعَ الْآخَرِ.)</span>).</li>
</ol>
<h2>Activité 3 (<em>an-nišāṭ 3</em> <span dir="rtl" lang="ar">(النشاط 3)</span>)</h2>
<p>Les hadiths des leçons précédentes ont contenu les plus importantes des assises pour l’édification d’une société humaine cohérente\u202f; j’emploie mes acquis et je remplis le tableau dans mon cahier (<em>aštamilat ’aḥādīṯu d-durūsi s-sābiqa ʿalà ’ahammi l-’ususi li-binā’i muǧtamaʿin ’insāniyyin mutamāsik; ’uwaẓẓifu muktasabātī wa-’amla’u l-ǧadwala fī daftarī</em> <span dir="rtl" lang="ar">(اشْتَمَلَتْ أَحَادِيثُ الدُّرُوسِ السَّابِقَةِ عَلَى أَهَمِّ الْأُسُسِ لِبِنَاءِ مُجْتَمَعٍ إِنْسَانِيٍّ مُتَمَاسِكٍ؛ أُوَظِّفُ مُكْتَسَبَاتِي وَأَمْلَأُ الْجَدْوَلَ فِي دَفْتَرِي:)</span>) — le tirage imprime, sous la consigne, un tableau à trois colonnes au corps ouvert, que l’élève recopie et remplit dans son cahier\u202f:
<table>
<thead>
<tr><th>La valeur (<em>al-qīma</em> <span dir="rtl" lang="ar">(الْقِيمَةُ)</span>)</th><th>Ce qui l’atteste des hadiths (<em>mā yadullu ʿalayhā mina l-’aḥādīṯ</em> <span dir="rtl" lang="ar">(مَا يَدُلُّ عَلَيْهَا مِنَ الْأَحَادِيثِ)</span>)</th><th>Les effets de s’en parer (<em>’āṯāru t-taḥallī bi-hāḏihī l-qīma</em> <span dir="rtl" lang="ar">(آثَارُ التَّحَلِّي بِهَذِهِ الْقِيمَةِ)</span>)</th></tr>
</thead>
<tbody>
<tr><td>la fraternité (<em>al-’uḫuwwa</em> <span dir="rtl" lang="ar">(الْأُخُوَّةُ)</span>)</td><td>…</td><td>…</td></tr>
<tr><td>la coopération et la solidarité (<em>at-taʿāwunu wa-t-taḍāmun</em> <span dir="rtl" lang="ar">(التَّعَاوُنُ وَالتَّضَامُنُ)</span>)</td><td>…</td><td>…</td></tr>
<tr><td>le vivre-ensemble (<em>at-taʿāyuš</em> <span dir="rtl" lang="ar">(التَّعَايُشُ)</span>)</td><td>…</td><td>…</td></tr>
<tr><td>la paix et la sûreté (<em>as-salāmu wa-l-’amānu</em> <span dir="rtl" lang="ar">(السَّلَمُ وَالْأَمَانُ)</span>)</td><td>…</td><td>…</td></tr>
</tbody>
</table>
</p>
<h2>Activité 4\u202f: la tenue du forum «\u202fl’importance de la quête du savoir\u202f», en prenant part avec mes amis de la classe à ce qui suit (<em>an-nišāṭ 4: ’inǧāzu nadwatin fī mawḍūʿi: «’ahammiyyatu ṭalabi l-ʿilm», wa-’ušāriku maʿa ’aṣdiqā’ī fī l-faṣli li-’inǧāzi mā ya’tī</em> <span dir="rtl" lang="ar">(النشاط 4: إِنْجَازُ نَدْوَةٍ فِي مَوْضُوعِ: «أَهَمِّيَّةُ طَلَبِ الْعِلْمِ»، وَأُشَارِكُ مَعَ أَصْدِقَائِي فِي الْفَصْلِ لِإِنْجَازِ مَا يَأْتِي:)</span>)</h2>
<ul>
<li>la présentation des axes du forum devant l’enseignant(e) et mes amis (<em>ʿarḍu maḥāwiri n-nadwati ’amāma l-’ustāḏ(i) wa-’aṣdiqā’ī</em> <span dir="rtl" lang="ar">(عَرْضُ مَحَاوِرِ النَّدْوَةِ أَمَامَ الْأُسْتَاذِ(ةِ) وَأَصْدِقَائِي.)</span>)\u202f;</li>
<li>la discussion des axes présentés (<em>munāqašatu l-maḥāwiri l-muqaddamah</em> <span dir="rtl" lang="ar">(مُنَاقَشَةُ الْمَحَاوِرِ الْمُقَدَّمَةِ.)</span>)\u202f;</li>
<li>la consignation des conclusions auxquelles on est parvenu, en de points concentrés (<em>tadwīnu l-ḫulāṣāti llatī tamma t-tawaṣṣulu ’ilayhā fī šakli niqāṭin murakkazah</em> <span dir="rtl" lang="ar">(تَدْوِينُ الْخُلَاصَاتِ الَّتِي تَمَّ التَّوَصُّلُ إِلَيْهَا فِي شَكْلِ نِقَاطٍ مُرَكَّزَةٍ.)</span>).</li>
</ul>
<h2>La préparation préalable (<em>al-i’dād al-qablī</em> <span dir="rtl" lang="ar">(الْإِعْدَادُ الْقَبْلِيُّ)</span>)</h2>
<p>Je me prépare pour la leçon qui vient, et j’extrais du hadith les effets de l’amour de Dieu le Très-Haut pour le serviteur (<em>’astaʿiddu li-d-darsi l-muwālī wa-’astaḫliṣu mina l-ḥadīṯi ’āṯāra maḥabbati llāhi taʿālà li-l-ʿabd</em> <span dir="rtl" lang="ar">(أَسْتَعِدُّ لِلدَّرْسِ الْمُوَالِي وَأَسْتَخْلِصُ مِنَ الْحَدِيثِ آثَارَ مَحَبَّةِ اللهِ تَعَالَى لِلْعَبْدِ.)</span>).</p>
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
    assert slot["docId"] == "pdf-mut23h3b-701", slot["docId"]
    if (slot.get("htmlFr") or "").strip():
        print("note : slot déjà rempli — régénération par le même script de livraison")
    slot["htmlFr"] = HTML
    json.dump(d, open(BOOK, "w"), ensure_ascii=False, indent=2)
    print("OK — htmlFr livré pour", slot["docId"], ":", len(HTML), "caractères")
else:
    print("mode contrôle seul (ajouter --write pour livrer) —", len(HTML), "caractères")

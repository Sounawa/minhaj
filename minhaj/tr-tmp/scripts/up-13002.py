#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Minhāj — Upgrade GT→main : leçon 13002 (hadith-1es, ce qui vint sur
la prière nocturne, l'witr et l'aube — Muwaṭṭaʾ n° 309/311/312/316/319/
321/326/331/332/333/337/338/339/340/341 + Ibn Abī Shayba + Muslim +
Abū Dāwūd + Ibn ʿAdī).

Conventions main (cf. 12875-13001 du même livre) :
- h1 = titleFr officiel « Ce qui a été mentionné à propos des prières
  nocturnes, du Witr et du Fajr » + translit. (mā jāʾa fī ṣalāt
  al-layl wa-l-witr wa-l-fajr), 26e leçon.
- Préambule : Dieu loua les pieux qui revivifient la nuit — **2
  VERSETS RESTAURÉS** (spans vides OCR) : Dhāriyāt 51 : 17 (« ils ne
  dormaient qu'une petite partie de la nuit » — lecture Ḥafṣ « mā
  yahjaʿūn » rendue) ; Isrāʾ 17 : 79 (« et de la nuit, veille par
  elle en prière... une station louée » — le tahajjud) ; numérotation
  imprimée = standard, aucune divergence.
- Hadiths : 309 (Muḥammad b. al-Munkadir/Saʿīd b. Jubayr/un homme en
  qui il avait confiance/ʿĀʾisha : « nul homme n'a une prière
  nocturne que le sommeil domine, sans que Dieu lui écrive la
  récompense de sa prière — et son sommeil est une aumône pour lui »)
  ; 316 (onze rakʿas, witr d'une, puis couché sur le flanc droit) ;
  321 (Ibn ʿUmar : « la prière nocturne deux par deux ; si l'un de
  vous craint l'aube, qu'il prie une rakʿa qui rend impair ce qu'il
  a prié ») ; 338 (Ḥafṣa : quand le muezzin s'est tu de l'adhān de
  l'aube — 2 rakʿas légères avant l'iqāma).
- Lexique : nawmuhu ṣadaqa, yūtir (witr kasra = l'impair ; conclure
  par une rakʿa), iḍṭajaʿa, khashiya l-ṣubḥ.
- Taḥlīl I : vertu — Ibn Abī Shayba (l'homme + l'épouse réveillant
  les siens) ; le wird dominé par le sommeil = récompense de qui pria
  ; al-Bājī (2 cas) ; Ibn ʿAbd al-Barr (récompensé sur l'intention,
  faveur divine) ; la clémence de la Loi — 311 (« si l'un de vous
  somnole, qu'il dorme » — « il va demander pardon et se maudit ») ;
  312 (« Dieu ne se lasse pas jusqu'à ce que vous vous lassiez :
  chargez-vous de l'œuvre dont vous avez la force »).
- Taḥlīl II : witr — Abū Ḥanīfa : obligatoire (« l'witr est un
  droit ; qui n'y procède pas n'est pas des nôtres » Abū Dāwūd ;
  « Dieu est impair et aime l'impair : rendez impairs, gens du
  Coran » Aṣḥāb al-Sunan) ; 316 + la divergence de transmission (les
  compagnons d'Ibn Shihāb : le repos APRÈS les 2 rakʿas de l'aube —
  Ibn ʿAbd al-Barr préfère la narration du Muwaṭṭaʾ) ; 326 (crainte
  de dormir → witr au préalable ; espoir de veiller → différéré) ;
  331 (witr au début + lever → 2 par 2) ; qaḍāʾ : 332 (Ibn ʿAbbās
  aveugle — « le peuple a fini l'aube » → se leva, fit l'witr, pria
  l'aube) + 333 (Ibn ʿAbbās/ʿUbāda/al-Qāsim/Ibn ʿĀmir après l'aube)
  + 337 (que qui dormit de l'witr — nul ne le délibère).
- Taḥlīl III : 2 rakʿas de l'aube (raghībatā al-fajr) — « rien de
  plus assidu » (Bukhārī/Muslim/Abū Dāwūd) ; 339 (« je me disais :
  a-t-il récité la Mère du Coran ou non ? » — al-Qurṭubī :
  comparaison avec sa prolongation coutumière, non doute) ; ne pas
  dépasser la Fātiḥa (Mālik) vs Kāfirūn+Ikhlāṣ (jumhūr, Muslim) ;
  iqāma faite → nulle prière sinon l'écrite (Muslim+Sunan ; Ibn
  ʿAdī chaîne bonne : « pas même les deux de l'aube ? — pas même
  les deux de l'aube ») ; 340 (« deux prières ensemble ? deux
  prières ensemble ? » — négation et blâme, Ibn ʿAbd al-Barr) ; qaḍāʾ
  après le lever du soleil (341 Ibn ʿUmar ; Ibn ʿAbd al-Barr :
  sunna confirmée) vs Shāfiʿī/ʿAṭāʾ/ʿAmr b. Dīnār (après le salut
  de l'imam) vs Mālik+jumhūr (interdit après l'aube).
- Istimḥār : 319 (Ibn ʿAbbās chez Maymūna : en travers de l'oreiller
  ; mi-nuit ou un peu avant/après ; essuya le sommeil de son visage ;
  LES DIX DERNIERS VERSETS D'ĀL ʿIMRĀN ; le shann suspendu ; l'witr
  à 11 ; la main sur ma tête et mon oreille droite tordue ; 2
  rakʿas légères au muezzin) + 2 questions.
- Préparation préalable : leçon SUIVANTE 13004 (prière en commun —
  zèle des Compagnons ; sa vertu).
"""

import json

BOOK = "/home/z/my-project/content/books/hadith-1es.json"

HTML_FR = """<h1>Ce qui a été mentionné à propos des prières nocturnes, du <em>Witr</em> et du <em>Fajr</em> (<em>mā jāʾa fī ṣalāt al-layl wa-l-witr wa-l-fajr</em>)</h1>
<p>Leçon sur ce qui vint de la prière nocturne, de l’<em>witr</em> et de l’aube, matière Ḥadīth, sur la base du <em>Muwaṭṭaʾ</em> de l’imam Mālik avec le commentaire de l’imam al-Zarqānī, à l’intention des élèves de la première année de l’enseignement secondaire traditionnel (<em>ʿatīq</em>) — la vingt-sixième leçon.</p>
<ol>
<li>Connaître la description de la prière nocturne du Prophète — paix et bénédiction sur lui.</li>
<li>Comprendre les vertus de l’<em>witr</em> et de l’aube.</li>
<li>Veiller sur les deux rakʿas désirables de l’aube.</li>
</ol>
<h2>Préambule</h2>
<p>Dieu — Exalté — loua en Son Livre Ses serviteurs pieux, et les décrivit comme revivifiant la nuit par la prière, disant :</p>
<p>« Ils ne dormaient qu’une petite partie de la nuit. » (adh-Dhāriyāt, 51 : 17)</p>
<p>[Verset restauré d’après le corpus canonique : l’emplacement imprimé correspondant est vide dans la source numérisée — perte OCR.]</p>
<p>. Et Il commanda à Son Prophète — paix et bénédiction sur lui — de veiller (<em>tahajjud</em>), et Dieu — Exalté — dit :</p>
<p>« Et de la nuit, veille par elle en prière, en surérogation pour toi : peut-être ton Seigneur te ressuscitera-t-il en une station louée. » (al-Isrāʾ, 17 : 79)</p>
<p>[Verset restauré d’après le corpus canonique : l’emplacement imprimé correspondant est vide dans la source numérisée — perte OCR.]</p>
<p>. Aussi le Prophète — paix et bénédiction sur lui — persévérait-il en la station de la nuit, concluant sa prière par la rakʿa de l’<em>witr</em> et la sunna de l’aube après l’appel du point du jour.</p>
<p>Comment donc était la prière nocturne du Prophète — paix et bénédiction sur lui — et son <em>witr</em> ? Et quel est le rang de l’<em>witr</em> et des deux rakʿas de l’aube parmi les sunnas ?</p>
<h2>Les hadiths</h2>
<ul>
<li>D’après Mālik, d’après Muḥammad ibn al-Munkadir, d’après Saʿīd ibn Jubayr, d’après un homme en qui il avait confiance, qui l’informa : « que ʿĀʾisha, épouse du Prophète — paix et bénédiction sur lui —, l’informa : que le Messager de Dieu — paix et bénédiction sur lui — dit : Il n’est d’homme qui ait une prière nocturne que le sommeil domine, sans que Dieu ne lui écrive la récompense de sa prière — et son sommeil est une aumône pour lui. » [Muwaṭṭaʾ, n° 309]</li>
<li>D’après Mālik, d’après Ibn Shihāb, d’après ʿUrwa ibn al-Zubayr, d’après ʿĀʾisha, épouse du Prophète — paix et bénédiction sur lui — : « que le Messager de Dieu — paix et bénédiction sur lui — priait de la nuit onze rakʿas, y faisant son <em>witr</em> d’une seule ; quand il avait fini, il se couchait sur son flanc droit. » [Muwaṭṭaʾ, n° 316]</li>
<li>D’après Mālik, d’après Nāfiʿ et ʿAbd Allāh ibn Dīnār, d’après ʿAbd Allāh ibn ʿUmar : « qu’un homme interrogea le Messager de Dieu — paix et bénédiction sur lui — sur la prière nocturne, et le Messager de Dieu — paix et bénédiction sur lui — dit : La prière nocturne est deux par deux (<em>mathnā mathnā</em>) ; quand l’un de vous craint le point du jour, qu’il prie une rakʿa unique, qui rend impair ce qu’il aura prié. » [Muwaṭṭaʾ, n° 321]</li>
<li>D’après Mālik, d’après Nāfiʿ, d’après ʿAbd Allāh ibn ʿUmar : « que Ḥafṣa, épouse du Prophète — paix et bénédiction sur lui —, l’informa : que le Messager de Dieu — paix et bénédiction sur lui —, quand le muezzin s’était tu de l’appel à la prière du point du jour, priait deux rakʿas légères avant que la prière ne fût instituée. » [Muwaṭṭaʾ, n° 338]</li>
</ul>
<h3>Explication lexicale</h3>
<ul>
<li><em>kāna nawmuhu ʿalayhi ṣadaqatan</em> (« son sommeil est une aumône pour lui ») : il n’est pas interrogé sur son sommeil, et la récompense de qui pria lui est écrite — en récompense de son intention.</li>
<li><em>yūtir</em> (« il fait son witr ») : <em>al-witr</em>, avec kasra du <em>wāw</em> : l’impair ; le sens, dans le hadith : conclure par une rakʿa unique.</li>
<li><em>iḍṭajaʿa</em> (« il se couchait ») : il se reposa sur son flanc, de la longueur de la station.</li>
<li><em>khashiya aḥadukumu l-ṣubḥ</em> (« l’un de vous craint le point du jour ») : il craint que le point du jour ne l’atteigne, lui échappant le temps de l’<em>witr</em> et sa vertu.</li>
</ul>
<h3>Extraction des contenus</h3>
<ul>
<li>Explicite le voulu par la station de la nuit.</li>
<li>Quelle est la vertu de la prière de l’<em>witr</em> et de l’aube ?</li>
<li>Pourquoi écrit-on à qui résolut la station de la nuit puis fut dominé par le sommeil la récompense de qui s’en tint debout ?</li>
</ul>
<h2>L’analyse</h2>
<h3>Premièrement : la vertu de la prière nocturne</h3>
<p>La prière nocturne compte parmi les meilleures surérogations de bien recommandées et désirées. Il vient au hadith : “Que Dieu fasse miséricorde à un homme qui se tint debout de la nuit et pria, puis réveilla sa famille et elle pria ! Que Dieu fasse miséricorde à une femme qui se tint debout de la nuit et pria, puis réveilla son époux et il pria !” [Rapporté par Ibn Abī Shayba dans son <em>Muṣannaf</em>]</p>
<p>Et si l’homme a une règle (<em>wird</em>) de prière dont il a coutume chaque nuit, puis l’assoupissement le domine après qu’il résolut de se tenir debout : la récompense de qui pria lui est écrite, en salaire de sa bonne intention. Le Messager de Dieu — paix et bénédiction sur lui — dit : « Il n’est d’homme qui ait une prière nocturne que le sommeil domine, sans que Dieu ne lui écrive la récompense de sa prière — et son sommeil est une aumône pour lui. » [Muwaṭṭaʾ, n° 309] Al-Bājī dit, en explicitant le sens du hadith : il est en deux cas — l’un, que le sommeil l’emporte sans qu’il s’éveille ; le deuxième, qu’il s’éveille mais que la domination du sommeil l’empêche de prier : sa règle est qu’il dorme jusqu’à ce que s’en aille ce qui l’empêche par le sommeil.</p>
<p>Et le sens de sa parole : “il lui écrit la récompense de sa prière” : en récompense de son intention et de son bon dessein. Il n’est pas interrogé sur son sommeil : la récompense de qui pria lui est écrite. Ibn ʿAbd al-Barr dit, en la matière : l’homme est rétribué de ce qu’il voulait de bien sans l’accomplir, comme s’il l’accomplissait — de la faveur de Dieu — Exalté —, quand aucune occupation de ce bas monde ne le retint et que ce qui l’empêchait procédait de Dieu ; et qu’on est gratifié sur l’intention comme on est gratifié sur l’œuvre, quand viennent entre lui et cette œuvre le sommeil, l’oubli ou autre de ce qui empêche. Et de la clémence de la Loi : qu’elle commanda de ne point charger l’âme de ce qui lui pèse — il vint en la Sunna l’ordre du Prophète — paix et bénédiction sur lui — à l’orant que le sommeil dominait, de se plonger dans le sommeil : « Quand l’un de vous somnole en sa prière, qu’il dorme jusqu’à ce que le sommeil s’en aille de lui : quand l’un de vous prie en somnolant, il ne sait — peut-être s’en va-t-il demander pardon, et il se maudit soi-même. » [Muwaṭṭaʾ, n° 311] Et l’appuie aussi sa parole — paix et bénédiction sur lui — : « Dieu — Béni et Exalté — ne se lasse point jusqu’à ce que vous ne vous lassiez : chargez-vous de l’œuvre dont vous avez la force. » [Muwaṭṭaʾ, n° 312]</p>
<h3>Deuxièmement : la sunna de l’witr</h3>
<h4>La vertu de la sunna de l’witr et la persévérance du Prophète — paix et bénédiction sur lui — en elle</h4>
<p>Les savants comptèrent la prière de l’<em>witr</em> parmi les plus fermes des sunnas — l’imam Abū Ḥanīfa la tint même pour obligatoire, c’est-à-dire proche du devoir : car l’obligatoire, en son usage, vient après le devoir — à cause du hadith de l’Envoyé de Dieu — paix et bénédiction sur lui — : “L’<em>witr</em> est un droit : quiconque n’y procède pas n’est pas des nôtres.” [Rapporté par Abū Dāwūd dans ses <em>Sunan</em>] Et il dit — paix et bénédiction sur lui — : “Dieu est impair (<em>witr</em>) et aime l’impair : rendez impairs, ô gens du Coran !” [Rapporté par les auteurs des <em>Sunan</em>]</p>
<p>L’Envoyé — paix et bénédiction sur lui — y persévéra et exhorta sa communauté. Mālik rapporta par sa chaîne jusqu’à ʿĀʾisha — que Dieu soit satisfait d’elle — : « que le Messager de Dieu — paix et bénédiction sur lui — priait de la nuit onze rakʿas, y faisant son <em>witr</em> d’une seule ; quand il avait fini, il se couchait sur son flanc droit. » [Muwaṭṭaʾ, n° 316] — et son repos — sur lui la paix — n’était que de la longueur de la station. Les transmetteurs du <em>Muwaṭṭaʾ</em> s’accordèrent sur cette narration ; quant aux compagnons d’Ibn Shihāb, ils transmirent de lui ce hadith par sa chaîne — plaçant le repos après les deux rakʿas de l’aube, non après l’<em>witr</em>. Ibn ʿAbd al-Barr préféra la narration du <em>Muwaṭṭaʾ</em>, vu le rang de l’imam Mālik, sa rétention, sa maîtrise et sa science du hadith de son shaykh Ibn Shihāb.</p>
<p>Mālik rapporta qu’il lui parvint qu’ʿĀʾisha, épouse du Prophète — paix et bénédiction sur lui —, disait : « Que quiconque craint de dormir jusqu’au matin fasse son <em>witr</em> avant de dormir ; et quiconque espère s’éveiller en la fin de la nuit diffère son <em>witr</em>. » [Muwaṭṭaʾ, n° 326] Et si l’orant fait son <em>witr</em> au début de la nuit puis dort puis se lève : il peut prier deux par deux — de la parole de Mālik : « Quiconque fait son <em>witr</em> au début de la nuit, puis dort, puis se lève, et il lui vient de prier — qu’il prie deux par deux : c’est ce que j’en ai entendu de plus aimé. » [Muwaṭṭaʾ, n° 331]</p>
<h4>Le rattrapage de la sunna de l’witr</h4>
<p>Si l’orant ne peut accomplir l’<em>witr</em>, le temps de l’aube l’ayant atteint, il peut le prier après le lever de l’aube, avant de prier le point du jour. Mālik rapporta par sa chaîne : « que ʿAbd Allāh ibn ʿAbbās dormit puis s’éveilla et dit à son serviteur : Regarde ce qu’ont fait les gens — c’était au temps où sa vue s’en était allée. Le serviteur partit puis revint et dit : “Les gens en ont fini du point du jour.” ʿAbd Allāh ibn ʿAbbās se leva alors, fit son <em>witr</em>, puis pria le point du jour. » [Muwaṭṭaʾ, n° 332] Et Mālik dit : « qu’il lui parvint que ʿAbd Allāh ibn ʿAbbās, ʿUbāda ibn al-Ṣāmit, al-Qāsim ibn Muḥammad et ʿAbd Allāh ibn ʿĀmir ibn Rabīʿa avaient fait leur <em>witr</em> après l’aube. » [Muwaṭṭaʾ, n° 333] Yaḥyā a dit : Mālik dit : « Ce n’est que celui qui dormit de son <em>witr</em> qui le fait après l’aube ; et il ne sied à quiconque de le faire délibérément, jusqu’à placer son <em>witr</em> après l’aube. » [Muwaṭṭaʾ, n° 337]</p>
<h3>Troisièmement : la sunna de l’aube</h3>
<h4>La vertu des deux rakʿas de l’aube et leur récitation</h4>
<p>Les deux rakʿas de l’aube comptent parmi les plus fermes des sunnas, venant au rang après la prière de l’<em>witr</em> ; on les nomme les deux désirables (<em>raghībatā al-fajr</em>). D’après ʿĀʾisha — que Dieu soit satisfait d’elle — : “Le Prophète — paix et bénédiction sur lui — n’avait sur aucune des surérogations une assiduité plus grande que sur les deux rakʿas de l’aube.” [Rapporté par al-Bukhārī, Muslim et Abū Dāwūd]</p>
<p>Le temps de ces deux rakʿas est le lever de l’aube ; il est recommandé de les avancer au début du temps et de les alléger — car Mālik rapporta, d’après Yaḥyā ibn Saʿīd : « que ʿĀʾisha, épouse du Prophète — paix et bénédiction sur lui —, dit : Le Messager de Dieu — paix et bénédiction sur lui — allégeait tant les deux rakʿas de l’aube, que je me disais : a-t-il récité la Mère du Coran, ou non ? » [Muwaṭṭaʾ, n° 339] Al-Qurṭubī a dit : son sens n’est pas qu’elle douta de la récitation de la Fātiḥa ; son sens : il prolongeait la récitation aux surérogations — quand il allégea la récitation de l’aube, ce fut comme s’il n’avait point récité, en comparaison des autres prières. Il y a aussi : qu’il n’ajoute, aux deux rakʿas de l’aube, rien au-delà de la Fātiḥa — c’est la parole de Mālik et d’une troupe ; le <em>jumhūr</em> dit : il est recommandé de réciter <em>al-Kāfirūn</em> et <em>al-Ikhlāṣ</em> — du fait de ce qui est chez Muslim, que le Messager de Dieu — paix et bénédiction sur lui — les y récita.</p>
<p>Et il est notoire que, quand la prière du point du jour est instituée, il n’est pas permis à l’orant de fléchir les deux rakʿas de l’aube : car la prière du point du jour est un devoir, et les deux rakʿas de l’aube une sunna ; et parce que le Prophète — paix et bénédiction sur lui — dit : “Quand la prière est instituée, nulle prière sinon l’écrite” [Rapporté par Muslim et les auteurs des <em>Sunan</em>] ; et dans la narration d’Ibn ʿAdī, par une chaîne bonne : “On dit : ô Messager de Dieu — pas même les deux rakʿas de l’aube ? Il dit : Pas même les deux rakʿas de l’aube.” C’est pourquoi Mālik rapporta par sa chaîne, jusqu’à Abū Salama ibn ʿAbd al-Raḥmān : « qu’il dit : Des gens entendirent l’institution de la prière et se levèrent pour prier ; le Messager de Dieu — paix et bénédiction sur lui — sortit vers eux et dit : Deux prières ensemble ? Deux prières ensemble ? — et c’était en la prière du point du jour, pour les deux rakʿas d’avant le point du jour. » [Muwaṭṭaʾ, n° 340] En la parole du Prophète — paix et bénédiction sur lui — : “Deux prières ensemble ?” il y a négation et blâme — preuve de la non-permission, comme le mentionna aussi Ibn ʿAbd al-Barr : il n’est permis à quiconque de rien prier de surérogatoire en la mosquée quand l’écrite s’est dressée.</p>
<h4>Le rattrapage des deux rakʿas de l’aube</h4>
<p>Si la prière est instituée et que l’orant n’a pu prier les deux rakʿas de l’aube, il peut les rattraper après le lever du soleil : Mālik rapporta « qu’il lui parvint que les deux rakʿas de l’aube échappèrent à ʿAbd Allāh ibn ʿUmar, et qu’il les rattrapa après le lever du soleil » [Muwaṭṭaʾ, n° 341]. Et le rattrapage d’Ibn ʿUmar, après le lever du soleil, est une preuve — comme dit Ibn ʿAbd al-Barr — qu’elles sont des sunnas confirmées. Al-Shāfiʿī, ʿAṭāʾ et ʿAmr ibn Dīnār permirent de les rattraper après le salut de l’imam du point du jour ; Mālik et la plupart des savants le refusèrent — à cause de l’interdiction de prier après le point du jour jusqu’à ce que le soleil se lève.</p>
<h2>L’évaluation</h2>
<ol>
<li>Pourquoi l’Envoyé — paix et bénédiction sur lui — commanda-t-il de s’empresser vers la prière de l’<em>witr</em> au dernier tiers de la nuit ?</li>
<li>Quelle était la prière du Prophète — paix et bénédiction sur lui — pour les deux rakʿas de l’aube ?</li>
<li>Résume la divergence survenue sur le rattrapage des deux rakʿas de l’aube.</li>
</ol>
<h2>L’exploitation</h2>
<p>Mālik, d’après Mukhrama ibn Sulaymān, d’après Kurayb, affranchi d’Ibn ʿAbbās : « que ʿAbd Allāh ibn ʿAbbās l’informa : qu’il passa une nuit chez Maymūna, épouse du Prophète — paix et bénédiction sur lui —, et elle était sa tante. Il dit : je me couchai en travers de l’oreiller, et le Messager de Dieu — paix et bénédiction sur lui — et sa famille se couchèrent en sa longueur. Le Messager de Dieu — paix et bénédiction sur lui — dormit jusqu’à ce que la nuit fût à sa moitié, ou un peu avant, ou un peu après ; le Messager de Dieu — paix et bénédiction sur lui — s’éveilla, s’assit et essuya le sommeil de son visage de sa main, puis récita les dix derniers versets de la sūra d’Āl ʿImrān, puis se leva vers une outre suspendue, en fit ses ablutions et les fit bien, puis se tint debout pour prier. Ibn ʿAbbās dit : je me levai et fis comme il avait fait, puis m’en allai me tenir à son flanc ; le Messager de Dieu — paix et bénédiction sur lui — posa sa main droite sur ma tête, prit mon oreille droite et la tordait. Il pria deux rakʿas, puis deux rakʿas, puis deux rakʿas, puis deux rakʿas, puis deux rakʿas, puis deux rakʿas — puis fit son <em>witr</em> ; puis se coucha jusqu’à ce que le muezzin vînt à lui ; il pria deux rakʿas légères, puis sortit et pria le point du jour. » [Muwaṭṭaʾ, n° 319]</p>
<ol>
<li>Extrais du hadith les sunnas venues de l’Envoyé — paix et bénédiction sur lui — en la station de la nuit.</li>
<li>Qu’indique le geste du Compagnon Ibn ʿAbbās — que Dieu soit satisfait de lui ?</li>
</ol>
<h2>La préparation préalable</h2>
<ol>
<li>Extrais des hadiths de la prochaine leçon ce qui indique le zèle des Compagnons pour assister à la prière en commun.</li>
<li>Recherche la vertu de la prière en commun.</li>
</ol>"""


def main():
    with open(BOOK, "r", encoding="utf-8") as fh:
        d = json.load(fh)
    hit = 0
    for l in d["lessons"]:
        if l.get("docId") == "13002":
            l["htmlFr"] = HTML_FR
            hit += 1
    if hit != 1:
        raise SystemExit(f"ERREUR: {hit} leçons 13002 trouvées (attendu 1)")
    with open(BOOK, "w", encoding="utf-8") as fh:
        json.dump(d, fh, ensure_ascii=False, indent=1)
    print(f"OK — leçon 13002 upgradée main: FR {len(HTML_FR)} car")


if __name__ == "__main__":
    main()

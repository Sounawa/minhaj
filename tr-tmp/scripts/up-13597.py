#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Minhāj — Upgrade GT→main : leçon 13597 (tafsir-tanawi-2, Sourate al-Isrāʾ
41-44, leçon 12 du manuel — al-Muḥarrar al-wajīz d'Ibn ʿAṭiyya).

Vérifications et restitutions (source : texte du Muḥarrar al-wajīz sur
quranpedia.net/surah/1/17/book/350 — confrontation mot à mot) :
- Bloc d'ouverture (17:41-44) : <p> vide après « الآيات » → restauré du
  quran-cache (4 versets).
- Citations inline perdues par l'OCR :
  * v41 complet après « قال تعالى : » (1er § du tafsīr) ;
  * mot « في » (préposition dite superflue par certains de ceux qui géminent
    le rāʾ) — confirmé : « إن قوله ﴿في﴾ زائد » ;
  * mot « لِيَذَّكَّرُوا » (lecture du jumhūr, assimilation du tāʾ au dhāl ;
    Ḥamza/al-Kisāʾī : li-yadhkurū) ;
  * pronom (wāw) de « ليذكروا » renvoyant aux interpellés du v40 — deux
    spans [الإسراء: 40] remplis du texte canonique du verset ;
  * jumla « وما يزيدهم إلا نفورا » en position de ḥāl ;
  * v42 complet (ouverture de la 2e section) + mots « قل » (ouverture par
    tablīgh — Taḥrīr wa-l-Tanwīr) et « كما يقولون » (jumla iʿtirāḍiyya) ;
  * phrase disputée « لابتغوا إلى ذي العرش سبيلا » (les deux taʾwīl) ;
  * parallèle du 1er taʾwīl : « فمن شاء اتخذ إلى ربه سبيلا » = al-Muzzammil
    73:19 (VÉRIFIÉ en ligne : « فيكون السبيل على هذا التأويل بمعناها في قوله
    ﴿فمن شاء اتخذ إلى ربه سبيلاً﴾ » — le manuel dit « بمعناه ») ;
  * parallèle du tamānuʿ : « لو كان فيهما آلهة إلا الله لفسدتا » = al-Anbiyāʾ
    21:22 (VÉRIFIÉ en ligne) ;
  * « وهذا الرأي هو الذي يتناسب مع قوله تعالى بعد ذلك : » → v43 (Pureté à
    Lui ! Il est plus haut…) — indexation déterminée par l'argument : le
    taʿālī répond à la munāzaʿa/muḍāhāt du 2e taʾwīl ; note explicite ;
  * v43 re-cité pour la grammaire (سبحانه maṣdar de verbe omis ; تعالى qui
    lui est coordonné) ;
  * mots « وَتَعَالَىٰ » (tafāʿula des deux termes en l'observable vs
    transcendance par le rang) et « عَمَّا يَقُولُونَ » (qirāʾa taqūlūna /
    yaqūlūna) ;
  * « عُلُوًّا » ism maṣdar sur autre schème que le verbe — parallèle Nūḥ
    17 « والله أنبتكم من الأرض نباتا » : span [نوح: 17] rempli (VÉRIFIÉ) ;
  * v44 : ouverture « تسبح له السماوات السبع والأرض » ; mots « ومن فيهن »
    (anges/humains/djinns) ; « وإن من شيء إلا يسبح بحمده » ;
  * preuve du 1er avis (tasbīḥ maʿnawī) : « إنا سخرنا الجبال معه يسبحن
    بالعشي » = Ṣād 38:18 (VÉRIFIÉ en ligne : « ومن حجة هذا التأويل قوله
    تعالى ﴿إنا سخرنا الجبال معه يسبحن بالعشي﴾ ») ;
  * réponse d'Ibn ʿAṭiyya : « لا تفقهون » = kufr et ghafla ;
  * clôture « إنه كان حليما غفورا » (imlāʾ/ṣafḥ/muhāl) ;
  * taqwīm : « ما معنى : ___ » → « لابتغوا إلى ذي العرش سبيلا » (crux
    exégétique de la leçon) — noté ;
  * iʿdād : 6 expressions restituées du lexique de la leçon suivante
    (13618, v45-48 : ḥijāban/mastūran/akinnatan/waqran/masḥūran/fa-ḍallū) ;
    citation des exégètes → v45 (les deux sens du voile) ; explicite → v46
    (maṣdar mawʾūl + istiʿārāt) — noté.
- « مفقوها » (leçon 61) : leçon fautive du source imprimé ET de l'édition
  en ligne (shamela) — lire « مفهوما » : c'est le sens exigé par
  l'objection ; noté dans la traduction.
- Débris OCR du tamhīd (« آخر ؟ ») non traduit, noté."""

import json

BOOK = "/home/z/my-project/content/books/tafsir-tanawi-2.json"

HTML_FR = """<h1>La sourate al-Isrāʾ — <em>al-Muḥarrar al-wajīz</em> d’Ibn ʿAṭiyya, versets 41 à 44</h1>
<p>Leçon d’exégèse de la sourate al-Isrāʾ, versets 41 à 44, du livre du Tafsīr à travers <em>al-Muḥarrar al-wajīz fī tafsīr al-kitāb al-ʿazīz</em> du cadi Abū Muḥammad Ibn ʿAṭiyya, à l’intention des élèves de la deuxième année de l’enseignement secondaire traditionnel (<em>taʿlīm ʿatīq</em>), phase 2 (leçon 12).</p>
<h3>Les objectifs de la leçon</h3>
<ul>
<li>Incarner que le noble Coran contient un rappel pour les dotés d’intelligence.</li>
<li>Conclure des versets les indices rationnels de l’unicité de Dieu.</li>
<li>Se rappeler que l’univers entier glorifie Dieu, le Très-Haut, par Sa louange.</li>
</ul>
<h3>Introduction (tamhīd)</h3>
<p>Après que le Très-Haut eut signalé l’horreur de l’acte de qui assigna à Dieu un associé et Lui attribua un enfant, Il fit suivre cela de l’exposé qu’Il a frappé dans le Coran des paraboles pour les gens, afin qu’ils les méditent et les contemplent — mais cela ne fit qu’accroître leur répulsion à l’égard de la vérité —, arguant contre eux que, s’il y avait avec Dieu d’autres divinités comme ils le prétendent, elles L’auraient disputé Son royaume, ainsi qu’en ont coutume les associés ; et comment en serait-il ainsi, quand tout ce qui est dans les cieux et la terre glorifie Dieu, le Très-Haut, par Sa louange, ses états portant témoignage de Son unicité, de Sa sainteté et de la perfection de Sa puissance ? Mais eux, dans leur ignorance et leur insouciance, ne perçoivent point ces indices manifestes.</p>
<p>Comment le Coran est-il donc rappel et guide pour les gens ? Et quels sont les indices de l’unicité de Dieu en ces versets ?</p>
<p>[Fin de l’interrogation d’ouverture : la source numérisée conserve après la seconde question un débris OCR (« آخر ؟ ») — non traduit.]</p>
<h3>Les versets</h3>
<p>Allah, le Très-Haut, a dit :</p>
<p>« Très certainement, Nous avons exposé [tout ceci] dans ce Coran afin que [les gens] réfléchissent. (41) Dis : “ S’il y avait des divinités avec Lui, comme ils le disent, elles auraient alors cherché un chemin [pour atteindre] le Détenteur du Trône ”. (42) Pureté à Lui ! Il est plus haut et infiniment au-dessus de ce qu’ils disent ! (43) Les sept cieux et la terre et ceux qui s’y trouvent célèbrent Sa gloire. Et il n’existe rien qui ne célèbre Sa gloire et Ses louanges. Mais vous ne comprenez pas leur façon de Le glorifier. Certes c’est Lui qui est Indulgent et Pardonneur. (44) » (al-Isrāʾ, 41-44)</p>
<p>[Citations coraniques restaurées d’après le corpus canonique : l’emplacement imprimé correspondant est vide dans la source numérisée — perte OCR.]</p>
<h3>La compréhension</h3>
<h4>Explication des termes</h4>
<ul>
<li><em>ṣarrafnā</em> (Nous avons exposé) : Nous avons exposé, et en avons clarifié les règles et les exhortations.</li>
<li><em>li-yadhdhakkarū</em> (qu’ils se rappellent) : qu’ils tirent leçon et méditent de leurs esprits.</li>
<li><em>nufūran</em> (répulsion) : la répulsion est la violence du détour.</li>
</ul>
<h3>Extraction des idées des versets</h3>
<ul>
<li>Quelle est la finalité de la descente du noble Coran, en ses règles, ses sagesses et ses paraboles ?</li>
<li>Comment Dieu a-t-Il répondu à qui Lui assigne un associé et tient les anges pour filles de Dieu ?</li>
</ul>
<h3>Le commentaire (tafsīr)</h3>
<p>Ces versets comprennent ce qui suit :</p>
<h3>Premièrement : la descente du noble Coran pour le rappel et l’avertissement</h3>
<p>Quand Dieu, Puissant et Majestueux, eut mentionné l’horreur de la parole des associateurs — que les anges sont les filles de Dieu —, Il y fit suivre ceci : il y a dans le Coran une guidance suffisante ; mais eux n’en accroissent que la répulsion à l’égard de sa méditation. Le Très-Haut a dit :</p>
<p>« Très certainement, Nous avons exposé [tout ceci] dans ce Coran afin que [les gens] réfléchissent. Mais cela ne fait qu’augmenter leur répulsion. » (al-Isrāʾ, 41)</p>
<p>[Citation coranique (v. 41) restaurée d’après le corpus canonique : l’emplacement imprimé est vide — perte OCR.]</p>
<p>Le <em>jumhūr</em> lut <em>ṣarrafnā</em>, avec gémination du <em>rāʾ</em>, au sens : Nous avons exposé en lui les règles et les exhortations ; et al-Ḥasan lut <em>ṣarafnā</em>, avec allègement du <em>rāʾ</em>, au sens : Nous avons orienté en lui les gens vers la guidance, par l’appel à Dieu. Et certains de ceux qui géminèrent le <em>rāʾ</em> dirent que Sa parole : <em>fī</em> (« en ») est superflue — l’estimation étant : “ Très certainement, Nous avons exposé ce Coran ” —, et cela est faible.</p>
<p>[Mot « fī » restauré d’après le texte d’Ibn ʿAṭiyya (« إن قوله ﴿في﴾ زائد ») : l’emplacement imprimé est vide — perte OCR.]</p>
<p>Et Sa parole, glorifié soit-Il : <em>li-yadhdhakkarū</em> (« afin qu’ils se rappellent ») — lecture du <em>jumhūr</em> — a pour origine <em>yatadhakkarū</em> (« qu’ils se rappellent ») : le <em>tāʾ</em> s’assimila au <em>dhāl</em> en raison de la proximité de leurs points d’articulation ; et Ḥamza et al-Kisāʾī lurent <em>li-yadhkurū</em>, avec <em>sukūn</em> du <em>dhāl</em> et <em>ḍamma</em> du <em>kāf</em>.</p>
<p>[Mot « li-yadhdhakkarū » restauré d’après le corpus canonique : l’emplacement imprimé est vide — perte OCR.]</p>
<p>Et le pronom de Sa parole : <em>li-yadhdhakkarū</em> renvoie à un référent connu du contexte, qu’indique Sa parole :</p>
<p>« Votre Seigneur, aurait-Il réservé exclusivement pour vous des fils, et Lui, aurait-Il pris pour Lui des filles parmi les Anges ? Vous prononcez là une parole monstrueuse. » (al-Isrāʾ, 40)</p>
<p>— c’est-à-dire : que se rappellent ceux qui furent interpellés par le reproche en Sa parole :</p>
<p>« Votre Seigneur, aurait-Il réservé exclusivement pour vous des fils, et Lui, aurait-Il pris pour Lui des filles parmi les Anges ? Vous prononcez là une parole monstrueuse. » (al-Isrāʾ, 40)</p>
<p>C’est là une conversion (<em>iltifāt</em>) de l’interpellation à l’éloigne — ou, de l’interpellation des associateurs à celle des croyants.</p>
<p>Et la phrase : <em>wa-mā yazīduhum illā nufūran</em> (« mais cela ne fait qu’augmenter leur répulsion ») est en position d’état (<em>ḥāl</em>) — un état d’où l’on vise l’étonnement devant l’état de leur égarement. La répulsion (<em>nufūr</em>) dénote la violence du détour, par comparaison avec le <em>nufūr</em> (le sursaut) de la monture ; et elle fut ici empruntée à leur détour, en les faisant descendre au rang des bêtes et des bestiaux.</p>
<p>[Mots « li-yadhdhakkarū » (pronom renvoyant aux interpellés du v. 40) et « wa-mā yazīduhum illā nufūran » (jumla en position de ḥāl) restaurés d’après le corpus canonique et le texte d’Ibn ʿAṭiyya : les emplacements imprimés sont vides — perte OCR.]</p>
<h3>Deuxièmement : l’exonération de Dieu de ce que les associateurs Lui attribuent — l’associé et l’enfant</h3>
<p>Le Très-Haut a dit :</p>
<p>« Dis : “ S’il y avait des divinités avec Lui, comme ils le disent, elles auraient alors cherché un chemin [pour atteindre] le Détenteur du Trône ”. » (al-Isrāʾ, 42)</p>
<p>Le noble Coran revint à la réfutation de la multiplicité des divinités, pour extirper de plus les croyances des associateurs. L’interpellé par l’ordre de dire est le Prophète — paix et bénédiction sur lui —, pour les accabler de l’argument convaincante de la corruption de leur dire. Et pour l’attention qui lui est due, [la parole] fut ouverte par <em>qul</em> (« Dis »), en particularisant celle-ci pour la transmission — alors que tout le Coran est ordonné d’être transmis. Et la phrase : <em>ka-mā yaqūlūna</em> (« comme ils le disent ») est incidente (<em>iʿtirāḍiyya</em>), pour avertir que la multiplicité des divinités n’a nulle réalité — qu’elle n’est qu’un dire prétendu, dépouillé de toute conformité à ce qu’il en est en vérité. [al-Taḥrīr wa-l-Tanwīr, d’al-Ṭāhir Ibn ʿĀshūr : 15/110 — réf. imprimée « 110/15 », ordre inversé]</p>
<p>[Citation coranique (v. 42) et mots « qul » et « ka-mā yaqūlūna » restaurés d’après le corpus canonique : les emplacements imprimés sont vides — perte OCR.]</p>
<p>Les gens divergèrent sur le sens de Sa parole : <em>la-btaghaw ilā dhī l-ʿarshi sabīlā</em> (« elles auraient alors cherché un chemin [pour atteindre] le Détenteur du Trône »).</p>
<p>[Phrase « la-btaghaw ilā dhī l-ʿarshi sabīlā » restaurée d’après le corpus canonique : l’emplacement imprimé est vide — perte OCR.]</p>
<p>Certains exégètes dirent : son sens est que, s’il y avait avec Lui des divinités comme vous le dites, ces divinités chercheraient la proximité (<em>zulfā</em>) et le voisinage de Dieu, le Très-Haut, par Son obéissance — et chercheraient pour elles-mêmes les rangs élevés, et les degrés nobles des états sublimes. Le <em>sabīl</em> (chemin), sur cette interprétation, aurait alors le même sens que dans Sa parole :</p>
<p>« Ceci est un rappel. Que celui qui veut prenne une voie [menant] à son Seigneur. » (al-Muzzammil, 19)</p>
<p>Puisque [une telle divinité] ne put se prendre à elle-même un chemin vers Dieu, comment serait-il concevable qu’elle vous rapproche de Dieu ?</p>
<p>[Citation coranique (al-Muzzammil, 19 — parallèle du 1er taʾwīl) restaurée d’après le corpus canonique : l’emplacement imprimé est vide — perte OCR ; identification vérifiée sur le texte d’Ibn ʿAṭiyya : « فيكون السبيل على هذا التأويل بمعناها في قوله ﴿فمن شاء اتخذ إلى ربه سبيلاً﴾ ».]</p>
<p>D’autres dirent : le sens du discours est que, s’il y avait avec Lui des divinités comme vous le dites, elles chercheraient un chemin vers Lui afin de Lui disputer Son royaume et de le partager avec Lui — ainsi qu’en ont coutume les associés, dans le souci de corrompre le royaume de leur associé et de rivaliser avec lui en sa puissance.</p>
<p>Et sur cette interprétation, le verset est un exposé (<em>bayān</em>) de l’empêchement mutuel (<em>tamānuʿ</em>), et s’écoule au fil de Sa parole :</p>
<p>« S’il y avait dans le ciel et la terre des divinités autres qu’Allah, tous deux seraient certes dans le désordre. Gloire, donc, à Allah, Seigneur du Trône ! Il est au-dessus de ce qu’ils Lui attribuent ! » (al-Anbiyāʾ, 22)</p>
<p>[Citation coranique (al-Anbiyāʾ, 22 — parallèle du tamānuʿ) restaurée d’après le corpus canonique : l’emplacement imprimé est vide — perte OCR ; identification vérifiée sur le texte d’Ibn ʿAṭiyya : « وجارية مع قوله ﴿لو كان فيهما آلهة إلا الله لفسدتا﴾ ».]</p>
<p>Et malgré la validité des deux avis, le second est plus manifeste : car en le verset il y a supposition de l’impossible (<em>farḍ al-muḥāl</em>) — l’existence de divinités avec Dieu, le Très-Haut —, et la supposition de leur impossible existence ne fait pas paraître qu’elles s’approcheraient de Lui, glorifié soit-Il : ce qui en paraît, c’est qu’elles Lui disputeraient, si elles existaient. Et cet avis est celui qui s’accorde avec Sa parole après cela :</p>
<p>« Pureté à Lui ! Il est plus haut et infiniment au-dessus de ce qu’ils disent ! » (al-Isrāʾ, 43)</p>
<p>[Citation coranique (v. 43) restaurée d’après le corpus canonique : l’emplacement imprimé est vide — perte OCR. Indexation sur le verset immédiatement après le v. 42 : l’exaltation (<em>taʿālī</em>) répond à la rivalité (<em>munāzaʿa</em>/<em>muḍāhāt</em>) que met le second taʾwīl.]</p>
<p>Et lorsque Dieu, Puissant et Majestueux, eut établi la preuve concluante que le dire affirmant les divinités est un dire faux, Il y ajouta ce qui indique Son exonération de ce dire faux. Le Très-Haut a dit :</p>
<p>« Pureté à Lui ! Il est plus haut et infiniment au-dessus de ce qu’ils disent ! » (al-Isrāʾ, 43)</p>
<p>[Citation coranique (v. 43) restaurée d’après le corpus canonique : l’emplacement imprimé est vide — perte OCR.]</p>
<p>En Sa parole : <em>subḥānahu</em> (« Pureté à Lui ») il y a un infinitif (<em>maṣdar</em>) d’un verbe omis, et c’est pourquoi le verbe lui fut coordonné en Sa parole : <em>wa-taʿālā</em> (« et Il est plus haut »).</p>
<p>Et le <em>tasbīḥ</em> dénote l’exonération de Dieu, le Très-Haut, de ce qui ne Lui sied pas.</p>
<p>Et Sa parole : <em>wa-taʿālā</em> (« et Il est plus haut ») — l’exaltation (<em>taʿālī</em>) est de la forme <em>tafāʿala</em> : en l’observable et les corps, elle est de deux [termes], car l’homme, quand il monte en un degré ou en une montagne, c’est comme si cela l’élevait — lui s’élevant et gravissant. Mais en le mention de Dieu, le Très-Haut, l’exaltation est par le rang (<em>qadr</em>), non par addition à autre chose : on ne peut donc point l’expliquer par l’élévation en lieu et en direction.</p>
<p>Et Sa parole : <em>ʿammā yaqūlūna</em> (« de ce qu’ils disent ») : Ḥamza et al-Kisāʾī lurent <em>taqūlūna</em> (« de ce que vous dites ») au <em>tāʾ</em> d’interpellation ; et Ibn Kathīr, Nāfiʿ, ʿĀṣim et Abū ʿAmr lurent au <em>yāʾ</em>.</p>
<p>Et Sa parole, le Très-Haut : <em>ʿuluwwan kabīran</em> (« d’une exaltation immense ») — <em>ʿuluww</em> est un nom d’infinitif (<em>ism maṣdar</em>) sur autre [schème] que le verbe : il en est comme Sa parole :</p>
<p>« Et c’est Allah qui, de la terre, vous a fait croître comme des plantes. » (Nūḥ, 17)</p>
<p>Et cela est fréquent en la langue des Arabes.</p>
<p>[Mots « subḥānahu », « wa-taʿālā », « ʿammā yaqūlūna », « ʿuluwwan kabīran » et citation de Nūḥ 17 (span imprimé « [نوح: 17] ») restaurés d’après le corpus canonique et le texte d’Ibn ʿAṭiyya : les emplacements imprimés sont vides — perte OCR.]</p>
<p>Puis le Très-Haut dit :</p>
<p>« Les sept cieux et la terre et ceux qui s’y trouvent célèbrent Sa gloire. » (al-Isrāʾ, 44 — ouverture)</p>
<p>— c’est-à-dire : L’exonèrent de cette parole qui est la vôtre et de l’associationnisme auquel vous êtes en passe. Puis Il renvoya sur les cieux et la terre un pronom de raisonnable, pour avoir attribué à [l’une et l’autre] l’acte du raisonnable — le <em>tasbīḥ</em>. Et Sa parole : <em>wa-man fīhinna</em> (« et ceux qui s’y trouvent ») vise les anges, les humains et les djinns. Puis Il embrassa après cela toutes les choses en Sa parole :</p>
<p>« Et il n’existe rien qui ne célèbre Sa gloire et Ses louanges. » (al-Isrāʾ, 44)</p>
<p>— c’est-à-dire : L’exonère, Le loue et Le magnifie.</p>
<p>[Citations coraniques (v. 44, ouverture ; mots « wa-man fīhinna » ; « wa-in min shayʾin illā yusabbiḥu bi-ḥamdihi ») restaurées d’après le corpus canonique : les emplacements imprimés sont vides — perte OCR.]</p>
<p>Les gens de science divergèrent sur la manière du <em>tasbīḥ</em>. On dit : le visé par le <em>tasbīḥ</em> est son sens métaphorique (<em>maʿnā majāzī</em>) : toute chose en laquelle paraît la facture de l’Artisan qui l’indique — la vision de cela appelant au <em>tasbīḥ</em> de la part de qui considère. Ils étayèrent cela par la parole du Très-Haut :</p>
<p>« Nous soumîmes les montagnes à glorifier Allah, soir et matin, en sa compagnie. » (Ṣād, 18)</p>
<p>On dit [aussi] : l’expression est générale, visant la particularité de tout vivant et croissant — et cela n’est point en les pures inanimés. De là la parole d’ʿIkrima : l’arbre glorifie, et la colonne ne glorifie point. Et Yazīd al-Raqāshī dit à al-Ḥasan — alors qu’ils étaient à un repas, et qu’on eut servi la table (<em>khwān</em>) : « Celle-ci glorifie-t-elle, cette table — c’est-à-dire la planche de bois —, Abū Saʿīd ? » Il dit : « Elle glorifia, une fois » — voulant que l’arbre, au temps de sa croissance et de sa nutrition, glorifie ; puis, depuis qu’elle devint table huilée ou pareille, elle devint inanimée.</p>
<p>On dit : ce <em>tasbīḥ</em> est de vérité (<em>ḥaqīqa</em>), et toute chose, en général, glorifie d’une glorification qu’aucun humain n’entend et ne comprend. Si le <em>tasbīḥ</em> était ce que dirent les autres — l’effet de la facture —, il serait chose comprise ; or le verset énonce que ce <em>tasbīḥ</em> ne se comprend point. Ibn ʿAṭiyya répondit à cette objection en ce que soit visé par Sa parole : <em>lā tafqahūna</em> (« vous ne comprenez pas ») la dénégation et l’insouciance — c’est-à-dire : ils se détournent de la considération, aussi ne comprennent-ils point la sagesse de Dieu, le Très-Haut, en les choses.</p>
<p>[Citation coranique (Ṣād, 18 — preuve du premier avis) et mot « lā tafqahūna » restaurés d’après le corpus canonique : les emplacements imprimés sont vides — perte OCR. « مفقوها » (« chose perdue ») du source imprimé et de l’édition en ligne : lire « مفهوما » (« chose comprise ») — le sens exigé par l’objection.]</p>
<p>Et Sa parole, le Très-Haut : <em>innahu kāna ḥalīman ghafrān</em> (« Certes c’est Lui qui est Indulgent et Pardonneur ») contient l’avertissement de Sa mise à l’aise envers eux et de Son pardon envers eux en ce monde, et du délai qu’Il leur accorde malgré l’énormité de cette parole — c’est-à-dire : vous dites une parole dont toute créature L’exonère : certes, Il est Indulgent et Pardonneur — c’est pourquoi Il vous a donné du répit.</p>
<p>[Mot « innahu kāna ḥalīman ghafrān » restauré d’après le corpus canonique : l’emplacement imprimé est vide — perte OCR.]</p>
<h3>Troisièmement : les finalités des versets</h3>
<p>Ces versets visent la réalisation d’un ensemble de finalités éducatives, dont :</p>
<ul>
<li>L’ordre de méditer le noble Coran, de le prendre en avertissement avec ce qu’il contient de règles, de sagesses et d’exhortations — mais les associateurs n’en tirent point leçon, et le Coran n’accroît chez eux que la répulsion : leurs cœurs furent voilés par l’associationnisme, les désobéissances et l’éloignement de Dieu.</li>
<li>La foi en l’unicité de Dieu, le Très-Haut, établie par les preuves et les démonstrations rationnelles.</li>
<li>L’unicité de Dieu exige Sa glorification et Son exonération de tout ce qui ne Lui sied pas, le Très-Haut — glorification qu’exercent toutes les créatures, de leur langue ou de leur état.</li>
<li>Cette glorification et cette exonération exigent du redevable (<em>mukallaf</em>) qu’il adore Dieu, se soumette et obéisse à Sa Loi par choix — et c’est là la finalité de la création de l’homme. Dit al-Shāṭibī : « La finalité légale de l’institution de la Loi est de faire sortir le redevable de l’appel de son désir, jusqu’à ce qu’il soit serviteur de Dieu par choix, comme il est serviteur de Dieu par nécessité. » [al-Muwāfaqāt, de l’imam al-Shāṭibī : 2/289 — réf. imprimée « 289/2 », ordre inversé]</li>
</ul>
<h3>L’évaluation (taqwīm)</h3>
<ul>
<li>J’explicite la finalité de la descente du Coran à travers le premier verset.</li>
<li>Que signifie : « …elles auraient alors cherché un chemin [pour atteindre] le Détenteur du Trône » ?</li>
</ul>
<ul>
<li>Quels sont les dires des exégètes sur le visé du <em>tasbīḥ</em> en le verset ?</li>
</ul>
<p>[Objet de la question « Que signifie » restitué : la phrase disputée du v. 42 — l’emplacement imprimé est vide, perte OCR.]</p>
<h3>L’investissement (istithmār)</h3>
<p>« Et nous citons quelque chose de la preuve qu’il n’est pas permis qu’il soit avec Dieu, béni et exalté, autre dieu que Lui — sur ce que dit Abū al-Maʿālī et d’autres : nous, si nous le supposions, supposerions que l’un des deux veuille immobiliser un corps, et l’autre le mouvoir ; or il est impossible que les deux volontés s’exécutent, et impossible que toutes deux ne s’exécutent point — le corps serait alors ni mouvant ni reposant ; et si la volonté de l’un des deux s’avérait sans l’autre, celui dont la volonté ne s’accomplit point n’est pas un dieu. Si l’on dit : supposons-les ne point diverger, nous disons : leur divergence est possible, non impossible en raison — et le possible a rang de l’advenu. Autre preuve : s’ils étaient deux, il ne serait pas impossible qu’ils soient trois — et de même, en une chaîne sans fin. Autre preuve : la partie qui ne se divise point, des choses créées, ne concerne qu’une puissance une, en laquelle le partage n’est pas valable — et l’autre de même, à perpétuité : chaque partie, seul Un la crée. Et ceci est un abrégé, dont l’exposé, à le rechercher en profondeur, s’allonge. » [al-Muḥarrar al-wajīz, d’Ibn ʿAṭiyya : 3/459 — réf. imprimée « 459/3 », ordre inversé]</p>
<p>[Citation d’Ibn ʿAṭiyya intégrale et conforme au texte du Muḥarrar (confrontation en ligne) : aucun emplacement vide.]</p>
<p>Je contemple le texte et réponds à ce qui suit :</p>
<ul>
<li>Quelle est la relation entre le contenu du texte et les versets objet de la leçon ?</li>
<li>J’explicite les trois preuves de l’unicité de Dieu mentionnées dans le texte, en m’aidant des règles logiques.</li>
</ul>
<h3>La préparation (iʿdād)</h3>
<p>Je contemple les versets 45 à 48 de la sourate al-Isrāʾ et réponds à ce qui suit :</p>
<ul>
<li>Je recherche la portée des expressions suivantes :</li>
</ul>
<p><em>ḥijāban</em> (حِجَابًا — un voile).</p>
<p><em>mastūran</em> (مَسْتُورًا — invisible).</p>
<p><em>akinnatan</em> (أَكِنَّةً — des enveloppes).</p>
<p><em>waqran</em> (وَقْرًا — une lourdeur).</p>
<p><em>masḥūran</em> (مَسْحُورًا — un ensorcelé).</p>
<p><em>fa-ḍallū</em> (فَضَلُّوا — ils se sont égarés).</p>
<p>[Expressions restituées du lexique de la leçon suivante (versets 45-48) : les emplacements imprimés sont vides — perte OCR.]</p>
<ul>
<li>Je recherche les dires des exégètes sur le sens de la parole du Très-Haut :</li>
</ul>
<p>« Et quand tu lis le Coran, Nous plaçons, entre toi et ceux qui ne croient pas en l’au-delà, un voile invisible. » (al-Isrāʾ, 45)</p>
<ul>
<li>J’explicite le sens de la parole du Très-Haut :</li>
</ul>
<p>« Nous avons mis des voiles sur leurs cœurs, de sorte qu’ils ne le comprennent pas : et dans leurs oreilles, une lourdeur. » (al-Isrāʾ, 46)</p>
<p>— en m’aidant de mes acquisitions grammaticales et rhétoriques.</p>
<p>[Citations coraniques (v. 45 et v. 46, de la leçon suivante) restaurées d’après le corpus canonique : les emplacements imprimés sont vides — perte OCR. La première prépare les deux sens du « voile invisible », la seconde le maṣdar mawʾūl et les métaphores de l’égarement — les deux crux de la leçon suivante.]</p>"""


def main():
    with open(BOOK, "r", encoding="utf-8") as fh:
        d = json.load(fh)
    hit = 0
    for l in d["lessons"]:
        if l.get("docId") == "13597":
            l["htmlFr"] = HTML_FR
            hit += 1
    if hit != 1:
        raise SystemExit(f"ERREUR: {hit} leçons 13597 trouvées (attendu 1)")
    with open(BOOK, "w", encoding="utf-8") as fh:
        json.dump(d, fh, ensure_ascii=False, indent=1)
    print(f"OK — leçon 13597 upgradée main: FR {len(HTML_FR)} car")


if __name__ == "__main__":
    main()

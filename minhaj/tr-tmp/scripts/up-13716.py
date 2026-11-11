#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Minhāj — Upgrade GT→main : leçon 13716 (tafsir-tanawi-2, Sourate al-Isrāʾ
90-93, leçon 23 du manuel — al-Muḥarrar al-wajīz d'Ibn ʿAṭiyya).

Vérifications et restitutions (source : texte du Muḥarrar al-wajīz sur
quranpedia.net/surah/1/17/book/350 — confrontation mot à mot ; corpus
canonique pour les versets) :
- Bloc d'ouverture (17:90-93) : <p> vide → 4 versets restaurés du
  quran-cache.
- Lexique (الفهم) : les 6 GLOSES sont intactes mais les VEDETTES sont
  perdues — restituées du vocabulaire des versets (ينبوعا/جنة/كسفا/قبلا/
  زخرفا/ترقى — NB : la 6e vedette est ترقى, non سلما : la glose « تصعد
  في السماء على السلم » définit l'ascension de v93) ; l'en-tête الشرح
  (perdu) restitué d'après la structure du manuel.
- Citations inline perdues :
  * les 6 citations des « six espèces de miracles » (v90/v91/v92/v92b/
    v93a/v93b) — restaurées du quran-cache ;
  * « تُفَجِّرَ » (Ibn Kathīr, Nāfiʿ, Abū ʿAmr, Ibn ʿĀmir) VÉRIFIÉ sur
    le texte d'Ibn ʿAṭiyya (« حتى تُفجّر ») ;
  * « فانفجرت » VÉRIFIÉ — le manuel imprime [البقرة: 59] : la référence
    canonique est 2:60 (10e réf d'adjacence erronée notée) ;
  * « ينبوعا » et « الأرض » VÉRIFIÉS ;
  * « فتفجّر », « وغلقت الأبواب » [يوسف: 23 — réf CONFORME] et
    « خلالها » VÉRIFIÉS ;
  * « كما زعمت » + « إن نشأ نخسف بهم الأرض أو نسقط عليهم كسفا من
    السماء » [سبأ: 9 — réf CONFORME] VÉRIFIÉS ;
  * « كسفا » VÉRIFIÉ ; « السماء » (l'antécédent du ḥāl) restitué ;
  * « قبيلا » VÉRIFIÉ (×2) ;
  * « حتى إذا أخذت الأرض زخرفها » VÉRIFIÉ [يونس: 24 — réf CONFORME] ;
  * « ترقى » et « في السماء » VÉRIFIÉS (l'édition en ligne porte
    « من السماء » — variante d'édition notée) ;
  * « قل سبحان ربي هل كنت إلا بشرا رسولا » VÉRIFIÉ ;
  * « سبحان ربي » et « أو تأتي بالله والملائكة قبيلا » (fin du bloc
    al-Rāzī) restitués du verset ;
  * l'attribution : les paragraphes 1-3 de la 2e section sont le texte
    d'Ibn ʿAṭiyya (vérifié en ligne) ; les 2 derniers (« وقد نزهت هذه
    الآية… » et « وتقرير هذا الجواب… ») forment la citation d'al-Rāzī
    [Mafātīḥ 21/409-410 — l'imprimé inverse l'ordre « 21/410-409 »] ;
  * le hadith des six demandes (ʿUtba et Shayba…) INTACT (vérifié) ;
  * la Sīra d'Ibn Hishām [1/262-263 — l'imprimé inverse « 1/263-262 »]
    INTACTE ;
  * iʿdād : 4 vedettes restituées du vocabulaire des versets 94-98 (la
    leçon 24 du manuel — v. 94-98 — ne figure pas dans le corpus du
    site ; la leçon suivante du livre couvre v. 99-100) + la question du
    yāʾ élidé de « المهتدي » (v97 — le rasm du muṣḥaf écrit المهتد sans
    yāʾ) + la citation v97 restaurée."""

import json

BOOK = "/home/z/my-project/content/books/tafsir-tanawi-2.json"

HTML_FR = """<h1>La sourate al-Isrāʾ — <em>al-Muḥarrar al-wajīz</em> d’Ibn ʿAṭiyya, versets 90 à 93</h1>
<p>Leçon d’exégèse de la sourate al-Isrāʾ, versets 90 à 93, du livre du Tafsīr à travers <em>al-Muḥarrar al-wajīz fī tafsīr al-kitāb al-ʿazīz</em> du cadi Abū Muḥammad Ibn ʿAṭiyya, à l’intention des élèves de la deuxième année de l’enseignement secondaire traditionnel (<em>taʿlīm ʿatīq</em>), phase 2 (leçon 23).</p>
<h3>Les objectifs de la leçon</h3>
<ul>
<li>Connaître les prodiges matériels et les absurdités que demandèrent les associateurs au Prophète — paix et bénédiction sur lui.</li>
<li>Conclure des versets la méthode de sagesse en la réponse du Prophète — paix et bénédiction sur lui — à leur demande.</li>
<li>Suivre l’exemple du Prophète — paix et bénédiction sur lui — en l’entretien de qui me contredit en opinion.</li>
</ul>
<h3>Introduction (tamhīd)</h3>
<p>Après l’impuissance des associateurs d’Arabie à venir avec la semblance du noble Coran, ils se mirent à tergiverser et à proposer d’autres signes — par obstination et perplexité : ils demandèrent au Prophète — paix et bénédiction sur lui — l’une de six espèces de signes, en preuve de la véracité de sa mission. Dieu, le Très-Haut, lui ordonna de les réfuter et de rejeter leurs demandes : car il n’est qu’un mortel, qu’envoya Dieu pour leur transmettre Son appel — il ne dispose point du gouvernement de l’univers.</p>
<p>Qu’est-ce qui poussa les associateurs à demander au Prophète — paix et bénédiction sur lui — ces signes ? Et comment Dieu, le Très-Haut, répondit-Il à leurs demandes ?</p>
<h3>Les versets</h3>
<p>Allah, le Très-Haut, a dit :</p>
<p>« Et ils dirent : “ Nous ne croirons en toi que lorsque tu feras jaillir de terre, pour nous, une source ; (91) ou qu’il y ait pour toi un jardin de palmiers et de vignes, où tu feras jaillir les rivières en abondance ; (92) ou que tu fasses tomber sur nous le ciel, en morceaux, comme tu le prétends ; ou que tu viennes avec Dieu et les anges, en vue frontale ; (93) ou qu’il y ait pour toi une maison d’ornement ; ou que tu montes au ciel. Et nous ne croirons point en ton ascension, jusqu’à ce que tu fasses descendre sur nous un écrit que nous lisions. ” Dis : “ Gloire à mon Seigneur ! Ne suis-je qu’un mortel, un envoyé ? ” » (al-Isrāʾ, 90-93)</p>
<p>[Citations coraniques restaurées d’après le corpus canonique : l’emplacement imprimé correspondant est vide dans la source numérisée — perte OCR.]</p>
<h3>La compréhension</h3>
<h4>Explication des termes</h4>
<ul>
<li><em>yanbūʿan</em> (يَنۢبُوعًا) : une source dont l’eau ne s’épuise point.</li>
<li><em>jannatan</em> (جَنَّةٍ) : un jardin d’arbres nombreux.</li>
<li><em>kisfan</em> (كِسَفًا) : en morceaux — pluriel de <em>kusfa</em>, comme <em>qiṭʿa</em>.</li>
<li><em>qabīlan</em> (قَبِيلًا) : en vue frontale — pour les voir de leurs yeux.</li>
<li><em>min zukhrufin</em> (مِن زُخْرُفٍ) : d’or.</li>
<li><em>tarqā</em> (تَرْقَىٰ) : monter au ciel par l’échelle.</li>
</ul>
<p>[Gloses imprimées intactes ; vedettes restituées du vocabulaire des versets (les emplacements imprimés sont vides — perte OCR) ; en-tête « Explication des termes » restitué d’après la structure du manuel.]</p>
<h3>Extraction des idées des versets</h3>
<ul>
<li>Que demandèrent les associateurs au Prophète — paix et bénédiction sur lui — en ces versets ?</li>
<li>De quoi Dieu, le Très-Haut, proclama-t-Il l’exemption en ces versets ?</li>
</ul>
<h3>Le commentaire (tafsīr)</h3>
<p>Ces versets comprennent ce qui suit :</p>
<h3>Premièrement : la demande des associateurs au Prophète — paix et bénédiction sur lui — de prodiges matériels, en preuve de sa véracité</h3>
<p>Les associateurs ne reconnurent point que leur impuissance à venir avec la semblance du noble Coran attestât que c’est là parole de Dieu, et attestât la prophétie de Son messager — paix et bénédiction sur lui : après que l’argument les eut réduits au silence et qu’ils furent incapables de la réponse convaincante, ils glissèrent vers la demande au Prophète — paix et bénédiction sur lui — de faire descendre l’un de six signes, pour qu’ils crussent en lui.</p>
<p>Il fut rapporté, au sujet de leur demande, un long hadith dont voici la substance : ʿUtba et Shayba, les deux fils de Rabīʿa, ʿAbdallāh b. Abī Umayya, al-Naḍr b. al-Ḥārith et d’autres des anciens et des chefs de Quraysh s’assemblèrent, et lui proposèrent — paix et bénédiction sur lui — de le faire roi s’il voulait la royauté, ou de rassembler pour lui l’abondante richesse s’il voulait l’aisance, ou de le soigner s’il avait quelque mal — et pareilles propositions. Le Messager de Dieu — paix et bénédiction sur lui — les appela alors à Dieu, et dit : “ Je ne suis venu à vous de par Dieu qu’avec une affaire où réside le salut de votre religion et de votre monde : si vous entendez et obéissez, tant mieux ; sinon, je patienterai en l’ordre de Dieu, jusqu’à ce que Dieu juge entre moi et vous ce qu’Il veut. ” Ils lui dirent alors : Si ce que tu prétends est véridique, fais jaillir pour nous une source et nous croirons en toi ; et qu’il y ait pour toi un jardin — et le reste de ce dont ils le chargèrent. Le Messager de Dieu — paix et bénédiction sur lui — leur dit : “ Tout cela appartient à Dieu : ceci ne m’incombe pas, ni autre chose — je ne suis qu’un soumis à l’ordre de Dieu. ” Tel est le sens du hadith ; et il y a divergence en les termes, et des récits ramifiés qu’il serait long de rapporter tout entiers — c’est pourquoi je l’ai abrégé.</p>
<p>[Hadith des six demandes intact (vérifié sur le texte d’Ibn ʿAṭiyya).]</p>
<p>Il est rapporté que l’auteur de cette parole est ʿAbdallāh b. Abī Umayya : il dit au Messager de Dieu — paix et bénédiction sur lui : “ Je ne croirai en toi que lorsque tu viendras avec un écrit que je verrais descendre avec toi, où il serait écrit de Dieu, le Puissant, le Majestueux, à ʿAbdallāh b. Abī Umayya. ” Et il est rapporté que leur groupe lui demanda pareil.</p>
<p>Et ce que les associateurs demandèrent au Prophète — paix et bénédiction sur lui — fut de six espèces de miracles :</p>
<p><strong>La première</strong>, Sa parole :</p>
<p>« Et ils dirent : “ Nous ne croirons en toi que lorsque tu feras jaillir de terre, pour nous, une source. ” » (al-Isrāʾ, 90)</p>
<p>Ibn Kathīr, Nāfiʿ, Abū ʿAmr et Ibn ʿĀmir lurent ﴿ <em>tufajjira</em> ﴾ — <em>ḍamma</em> du <em>tāʾ</em>, <em>fatḥa</em> du <em>fāʾ</em>, et <em>šadda</em> du <em>jīm</em> au <em>kasra</em>. Et ʿĀṣim, Ḥamza et al-Kisāʾī lurent ﴿ <em>tafjura</em> ﴾ — <em>fatḥa</em> du <em>tāʾ</em> et <em>ḍamma</em> du <em>jīm</em>. Et il y a en le Coran :</p>
<p>“ …et elle jaillit… ” (al-Baqara, 2:60 — extrait)</p>
<p>— et <em>infaʿjara</em> (“ jaillir ”) est dérivé de <em>fajara</em>, indice de la condescendance du verbe à son agent : ce qui affermit la seconde lecture ; quant à la première, elle exige l’intensification en l’épanchement. Et l’expression par le mot ﴿ <em>yanbūʿan</em> ﴾ (“ une source ”) marque qu’ils ne veulent pas seulement de l’eau qui leur suffise, mais une eau abondante qui ne diminue en aucun temps : c’est un adjectif d’intensité, qui n’échoit qu’à l’eau abondante. Quraysh demandèrent ceci au Messager de Dieu — paix et bénédiction sur lui — à La Mecque, et c’est elle qu’ils visèrent par ﴿ <em>al-arḍi</em> ﴾ (“ la terre ”) : la définition y est celle de la chose connue (<em>al-ʿahd</em>).</p>
<p>[Citations « tufajjira » et « fanfajarat » restaurées d’après le texte d’Ibn ʿAṭiyya et le corpus canonique : les emplacements imprimés sont vides — perte OCR ; la référence imprimée « al-Baqara 2:59 » correspond canoniquement à 2:60 (écart de numérotation noté) ; « yanbūʿan » et « al-arḍi » restaurés, vérifiés sur le texte d’Ibn ʿAṭiyya.]</p>
<p><strong>La deuxième</strong>, Sa parole, le Glorifié :</p>
<p>« …ou qu’il y ait pour toi un jardin de palmiers et de vignes, où tu feras jaillir les rivières en abondance… » (al-Isrāʾ, 91)</p>
<p>Ils proposèrent que le jardin fût à La Mecque — vu l’impossibilité de cela en elle ; sinon, en les autres pays, cela eût été possible : mais ils demandèrent que ce fût par ordre divin, en ce lieu de disette. Et Sa parole : ﴿ <em>fa-tufajjira</em> ﴾ (“ tu feras jaillir ”) : redoublement d’intensif, non de transitivation — comme :</p>
<p>“ …et elle ferma les portes… ” (Yūsuf, 12:23 — extrait)</p>
<p>Et ﴿ <em>khilālahā</em> ﴾ (“ à travers lui ”) : un adverbe de lieu, dont le sens : au milieu de lui, et en son dedans.</p>
<p>[Citations « fa-tufajjira », « wa-ghallaqati l-abwāba » et « khilālahā » restaurées d’après le texte d’Ibn ʿAṭiyya et le corpus canonique : les emplacements imprimés sont vides — perte OCR ; la référence imprimée « Yūsuf 12:23 » est conforme.]</p>
<p><strong>La troisième</strong>, Sa parole :</p>
<p>« …ou que tu fasses tomber sur nous le ciel, en morceaux, comme tu le prétends… » (al-Isrāʾ, 92)</p>
<p>Sa parole : ﴿ <em>kamā zaʿamta</em> ﴾ (“ comme tu le prétends ”) fait signe à ce qui leur fut récité auparavant, en la parole du Puissant, le Majestueux :</p>
<p>“ …si Nous voulons, Nous engloutissons la terre sous eux, ou faisons tomber sur eux un morceau de ciel… ” (Sabaʾ, 34:9 — extrait)</p>
<p>Et Sa parole : ﴿ <em>kisfan</em> ﴾ (“ en morceaux ”) est un état (<em>ḥāl</em>) de ﴿ <em>al-samāʾi</em> ﴾ (“ le ciel ”) ; et le sens : ou tu ferais tomber sur nous le ciel, d’une chute semblable à ce dont tu nous as menacés — que le pouvoir de ton Seigneur, le Glorifié, est de faire descendre sur nous, du ciel, un châtiment morcelé.</p>
<p>[Citations « kamā zaʿamta » et « in nachaʾ nakhkuf bihimu l-arḍa… » restaurées d’après le texte d’Ibn ʿAṭiyya et le corpus canonique : les emplacements imprimés sont vides — perte OCR ; la référence imprimée « Sabaʾ 34:9 » est conforme ; « kisfan » vérifié ; l’antécédent « al-samāʾi » restitué (reconstruction grammaticale : le complément d’état qualifie l’objet « le ciel », conformément au sens qui suit).]</p>
<p><strong>La quatrième</strong>, Sa parole :</p>
<p>“ …ou que tu viennes avec Dieu et les anges, en vue frontale… ” (al-Isrāʾ, 92 — fin)</p>
<p>Sa parole : ﴿ <em>qabīlā</em> ﴾ — il fut dit : son sens — en face, et à vue ; il fut dit : son sens — garant et répondant de ta véracité — de lui la <em>qibāla</em>, qui est le cautionnement, et le <em>qabīl</em> et le <em>mutaqabbil</em> : le garant ; il fut dit : son sens — une espèce et un genre qui n’a point de semblable chez nous.</p>
<p>[Citation « qabīlā » restaurée d’après le texte d’Ibn ʿAṭiyya : l’emplacement imprimé est vide — perte OCR.]</p>
<p><strong>La cinquième</strong>, Sa parole :</p>
<p>“ …ou qu’il y ait pour toi une maison d’ornement… ” (al-Isrāʾ, 93 — extrait)</p>
<p>Dirèrent les interprètes : ﴿ <em>al-zukhruf</em> ﴾ (“ l’ornement ”) : l’or, en cet endroit ; et le <em>zukhruf</em> : ce dont on pare — fût-ce d’or ou d’autre. Et de lui :</p>
<p>“ …jusqu’à ce que la terre eût pris son parure… ” (Yūnus, 10:24 — extrait)</p>
<p>Et en la lecture de ʿAbdallāh b. Masʿūd : “ ou qu’il y ait pour toi une maison d’or ”. Dit Mujāhid : nous ne savions pas ce qu’est le <em>zukhruf</em>, jusqu’à ce que nous lussions, en le <em>ḥarf</em> de ʿAbdallāh : “ d’or ”.</p>
<p>[Citation « ḥattā idhā akhadhati l-arḍu zukhrufahā » restaurée d’après le texte d’Ibn ʿAṭiyya et le corpus canonique : l’emplacement imprimé est vide — perte OCR ; la référence imprimée « Yūnus 10:24 » est conforme.]</p>
<p><strong>La sixième</strong>, Sa parole :</p>
<p>“ …ou que tu montes au ciel — et nous ne croirons point en ton ascension, jusqu’à ce que tu fasses descendre sur nous un écrit que nous lisions… ” (al-Isrāʾ, 93)</p>
<p>Sa parole : ﴿ <em>tarqā</em> ﴾ (“ tu montes ”) : son sens — tu gravis les degrés du ciel : le complément est élidé. Et la <em>ruqyā</em> : l’ascension. Et Sa parole : ﴿ <em>fī l-samāʾi</em> ﴾ (“ au ciel ”) : Il veut — dans l’air, en haut ; et les Arabes nomment l’air “ ciel ” (<em>samāʾ</em>), pour ce qu’il est en l’espace de la hauteur. Et il se peut qu’ils visent le ciel connu — et c’est le plus apparent : car il leur informa que le Dieu de la création y est, et que sa nouvelle lui vient.</p>
<p>[Citations « tarqā » et « fī l-samāʾi » restaurées d’après le texte d’Ibn ʿAṭiyya : les emplacements imprimés sont vides — perte OCR ; l’édition en ligne d’Ibn ʿAṭiyya porte « min al-samāʾi » en ce lieu — variante d’édition notée.]</p>
<h3>Deuxièmement : la proclamation de l’exemption de Dieu, le Très-Haut, des demandes des associateurs</h3>
<p>Après l’exposé des versets — les demandes précédentes des associateurs —, Dieu, le Puissant, le Majestueux, interpellà Son Messager — paix et bénédiction sur lui — en disant :</p>
<p>« Dis : “ Gloire à mon Seigneur ! Ne suis-je qu’un mortel, un envoyé ? ” » (al-Isrāʾ, 93 — fin)</p>
<p>L’interrogation est ici de négation : c’est-à-dire : tu ne fus qu’un envoyé comme le reste des envoyés, et un mortel comme eux.</p>
<p>[Citation « qul subḥāna rabbī hal kuntu illā basharan rasūlā » restaurée d’après le texte d’Ibn ʿAṭiyya : l’emplacement imprimé est vide — perte OCR.]</p>
<p>Et le sens : dis — gloire à mon Seigneur, et proclamation d’exemption de Lui : de venir avec les anges en vue frontale, d’être interpellé par vous en un écrit comme vous l’avez voulu, et de ce que je propose moi-même sur Lui ces choses. Je ne suis qu’un mortel comme le reste des mortels, et un envoyé comme le reste des envoyés, envoyé à vous avec la Loi : il ne m’incombe que la transmission, seulement.</p>
<p>Et Ibn Kathīr et Ibn ʿĀmir lurent “ il dit : gloire à mon Seigneur ” — sur le sens du compte rendu du Messager de Dieu — paix et bénédiction sur lui —, qu’il glorifia lors de leur dire.</p>
<p>[Ce qui précède est le texte d’Ibn ʿAṭiyya, conforme à l’édition en ligne ; la lecture d’Ibn Kathīr et d’Ibn ʿĀmir est intacte.]</p>
<p>“ Ce verset a proclamé Dieu, le Glorifié et Très-Haut, exempt de toute chose inconvenante à Lui, ou qu’on Lui attribua de ce qui précéda. Or il n’y a, en ce qui précéda, rien d’inconvenant à Dieu sinon leur parole : “ ou que tu viennes avec Dieu ”. Cela atteste que Sa parole “ gloire à mon Seigneur ” est proclamation d’exemption de Dieu de la venue et de l’aller — et cela atteste la corruption du dire des assimilateurs (<em>Mushabbiha</em>), que Dieu, le Très-Haut, irait et viendrait. Que s’ils disent : pourquoi ne serait-il pas permis que le visé fût l’exemption de Dieu, le Très-Haut, de ce que les présomptueux L’imposent en la proposition des choses ? — nous répondons : le peuple n’a point imposé sur Dieu : ils dirent au Messager — paix et bénédiction sur lui — : si tu es prophète véridique, demande à Dieu qu’Il t’honore de ces miracles. Le peuple imposa sur le Messager, et n’imposa point sur Dieu : il ne convient donc pas de construire Sa parole “ gloire à mon Seigneur ” sur ce sens — et il fallut la construire sur leur parole : “ ou que tu viennes avec Dieu et les anges, en vue frontale ”.</p>
<p>Et la formulation de cette réponse est de dire : ou bien votre dessein, en cette proposition, fut que vous demandiez la venue de ces choses de chez moi-même ; ou bien vous demandâtes de moi que je demande à Dieu, le Très-Haut, de les manifester par ma main, pour attester que je suis un envoyé véritable, de par Dieu. Le premier est nul : car je suis un mortel, et le mortel n’a nul pouvoir sur ces choses. Et le second aussi est nul : car je vous suis déjà venu avec un miracle unique — le Coran ; demander ces miracles, c’est demander ce dont nul besoin ni nulle nécessité : leur demande tient donc de l’obstination et de l’imposition — et je suis un serviteur ordonné, à qui il n’appartient point d’imposer sur Dieu. ” [Mafātīḥ al-ghayb, d’al-Fakhr al-Dīn al-Rāzī : 21/409-410 — l’imprimé inverse l’ordre des pages (« 21/410-409 »), noté]</p>
<p>[Citations « subḥāna rabbī » et « aw taʾtiya bi-llāhi wa-l-malāʾikati qabīlā » restaurées du verset : les emplacements imprimés sont vides — perte OCR. Les deux derniers paragraphes forment la citation d’al-Rāzī (la réfutation des assimilateurs et la formulation de la réponse) ; l’attribution suit la place de la référence imprimée en fin de citation.]</p>
<h3>Troisièmement : les finalités des versets</h3>
<p>Ces versets visent la réalisation de finalités éducatives multiples, dont :</p>
<ul>
<li>L’exposé de la véracité de la mission du Prophète — paix et bénédiction sur lui —, qui appelle à l’unicité de Dieu, le Très-Haut, et guide les gens à Son adoration : Lui seul la mérite.</li>
<li>Le soutien que Dieu, le Très-Haut, prête à Son Messager — paix et bénédiction sur lui — par le noble Coran, dont les Arabes furent impuissants à venir la semblance, et qui fut le plus grand indice de la véracité de ce dont il fut envoyé — paix et bénédiction sur lui — en sa prétention à la prophétie.</li>
<li>La multiplicité et la succession des miracles n’est point condition de la véracité de la prophétie : si cette porte s’ouvrait, les gens exigeraient de tout messager venu avec un miracle qu’il leur en apportât un autre — et ainsi l’affaire ne s’arrêterait à nulle limite où arbitrent les gens de raison, ni où finit l’obstination des obstinés.</li>
</ul>
<h3>L’évaluation (taqwīm)</h3>
<ul>
<li>Pourquoi Dieu, le Très-Haut, n’accéda-t-Il pas à la demande des associateurs — d’affermir la véracité de Son Messager, paix et bénédiction sur lui ?</li>
<li>Je conclus des versets la sagesse du Prophète — paix et bénédiction sur lui — en son traitement des associateurs.</li>
<li>Comment suivrai-je l’exemple du Prophète — paix et bénédiction sur lui — en mon traitement des contradicteurs ?</li>
</ul>
<h3>L’investissement (istithmār)</h3>
<p>Quand les associateurs eurent demandé au Messager de Dieu — paix et bénédiction sur lui — ce dont il est fait mention aux versets objet de la leçon, il leur répondit : “ Cela appartient à Dieu : s’Il veut le faire de vous, Il le fait. ” Ils dirent : “ Muḥammad ! Ton Seigneur ne sait-Il donc pas que nous nous assiérons avec toi, t’interrogerons de ce que nous t’avons interrogé, et te demanderons ce que nous demandons — puis Il s’avancera et t’enseignera ce dont tu nous feras retour, et t’informera de ce qu’Il fera alors de nous, puisque nous n’avons pas accepté de toi ce avec quoi tu nous es venu ? Il nous est parvenu que ce n’est qu’un homme, en al-Yamāma, qu’on appelle al-Raḥmān, qui t’enseigne ceci — et par Dieu, nous ne croirons jamais en al-Raḥmān ! Nous nous sommes excusés envers toi, Muḥammad : par Dieu, nous ne te laisserons pas — ni ce que tu es devenu chez nous — jusqu’à ce que nous te perdions, ou que tu nous perdes. ” Et l’un d’eux dit : “ Nous adorons les anges — elles sont les filles de Dieu. ” Et l’un d’eux dit : “ Nous ne croirons en toi que lorsque tu nous auras amené Dieu et les anges, en vue frontale. ” Quand ils eurent dit cela au Messager de Dieu — paix et bénédiction sur lui —, il se leva de chez eux ; et se leva avec lui ʿAbdallāh b. Abī Umayya, fils d’al-Mughīra (…), qui lui dit : “ Muḥammad, ton peuple t’a proposé ce qu’il t’a proposé — tu ne l’as pas accepté d’eux ; puis ils te demandèrent, pour eux-mêmes, des affaires par lesquelles connaître ton rang auprès de Dieu, comme tu dis — et te croire et te suivre : tu ne l’as pas fait ; puis ils te demandèrent de prendre pour toi-même ce par quoi ils connaîtraient ta prééminence sur eux et ton rang auprès de Dieu — tu ne l’as pas fait ; puis ils te demandèrent de hâter pour eux quelque part du châtiment dont tu les menaces — tu ne l’as pas fait ” — ou comme il lui dit. “ Par Dieu, je ne croirai jamais en toi, jusqu’à ce que tu fasses, vers le ciel, une échelle, puis que tu y montes sous mes yeux, jusqu’à ce que tu l’atteignes, et que tu viennes avec quatre des anges, témoins pour toi que tu es comme tu dis — par Dieu, quand même tu ferais cela, je ne pense pas que je te croirais ! ” Puis il se détourna du Messager de Dieu — paix et bénédiction sur lui —, et le Messager de Dieu — paix et bénédiction sur lui — s’en retourna vers les siens, chagriné et affligé de ce qui lui avait échappé de ce qu’il espérait de son peuple quand il l’appela, et de ce qu’il vit de leur éloignement de lui. ” [al-Sīra al-nabawiyya, d’Ibn Hishām : 1/262-263 — l’imprimé inverse l’ordre des pages (« 1/263-262 »), noté]</p>
<p>[Citation de la Sīra intégrale et conforme.]</p>
<p>Je contemple le texte et réponds à ce qui suit :</p>
<ul>
<li>J’expose, à travers le texte, l’effronterie des associateurs envers Dieu, le Très-Haut, et Son Messager — paix et bénédiction sur lui.</li>
<li>J’expose la sagesse du non-hâtivement châtier par Dieu, le Très-Haut, en rétribution de leur effronterie.</li>
</ul>
<h3>La préparation (iʿdād)</h3>
<p>Je contemple les versets 94 à 98 de la sourate al-Isrāʾ et réponds à ce qui suit :</p>
<ul>
<li>Je recherche la portée des expressions suivantes :</li>
</ul>
<p><em>a-baʿatha</em> (أَبَعَثَ — a-t-on envoyé : le miracle serait-il l’envoi d’un mortel ?).</p>
<p><em>muṭmaʾinnīna</em> (مُطْمَئِنِّينَ — tranquilles, établis : apaisés en elle et y demeurant).</p>
<p><em>kafā bi-llāhi shahīdā</em> (كَفَىٰ بِٱللَّهِ شَهِيدًۢا — Il suffit, comme témoin).</p>
<p><em>ʿiẓāman wa-rufātan</em> (عِظَٰمًۭا وَرُفَٰتًا — ossements et poussière).</p>
<p>[Vedettes restituées du vocabulaire des versets 94-98 (gloses reconstituées d’après le lexique et le commentaire d’Ibn ʿAṭiyya) : les emplacements imprimés sont vides — perte OCR. La leçon suivante du manuel (versets 94-98, leçon 24) ne figure pas dans le corpus du site : la leçon qui suit dans le présent livre couvre les versets 99-100.]</p>
<ul>
<li>Comment Dieu, le Très-Haut, réfuta-t-Il les associateurs et annula-t-Il leurs prétentions ?</li>
<li>Quelle est la cause de l’élision du <em>yāʾ</em> de ﴿ <em>al-muhtadī</em> ﴾ en Sa parole, le Glorifié :</li>
</ul>
<p>“ …Et quiconque Dieu guide, c’est lui le bien guidé… ” (al-Isrāʾ, 97 — extrait)</p>
<p>[Citation (v. 97) restaurée d’après le corpus canonique : l’emplacement imprimé est vide — perte OCR ; l’élision du <em>yāʾ</em> de <em>al-muhtadī</em> suit le rasm du muṣḥaf (orthographe coranique : المهتد, sans <em>yāʾ</em> final).]</p>"""


def main():
    with open(BOOK, "r", encoding="utf-8") as fh:
        d = json.load(fh)
    hit = 0
    for l in d["lessons"]:
        if l.get("docId") == "13716":
            l["htmlFr"] = HTML_FR
            hit += 1
    if hit != 1:
        raise SystemExit(f"ERREUR: {hit} leçons 13716 trouvées (attendu 1)")
    with open(BOOK, "w", encoding="utf-8") as fh:
        json.dump(d, fh, ensure_ascii=False, indent=1)
    print(f"OK — leçon 13716 upgradée main: FR {len(HTML_FR)} car")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Minhāj — Upgrade GT→main : leçon 13619 (tafsir-tanawi-2, Sourate al-Isrāʾ
49-55, leçon 14 du manuel — al-Muḥarrar al-wajīz d'Ibn ʿAṭiyya).

Vérifications et restitutions (source : texte du Muḥarrar al-wajīz sur
quranpedia.net/surah/1/17/book/350 — confrontation mot à mot) :
- Bloc d'ouverture (17:49-55) : seul le titre « سورة الإسراء الآيات 49-55 »
  survit — les versets restaurés du quran-cache (7 versets).
- Lexique : 3 vedettes perdues par l'OCR (rufātan/jadīdan/fatarakum) —
  restituées du corps du tafsīr et du texte d'Ibn ʿAṭiyya (﴿جديداً﴾ صفة
  لما قرب حدوثه) ; al-nazgh intacte.
- Citations inline perdues :
  * v49, v50, v51a, v51b (فسينغضون/متى هو/عسى أن يكون قريبا) après leurs
    « قال تعالى / وقوله تعالى / ثم قال تعالى » ;
  * mot « عسى » (de Dieu = obligation — al-Ṭabarī/Ibn Sallām ; la réponse
    d'Ibn ʿAṭiyya : parole du Prophète par ordre de Dieu) ;
  * v52 + iʿrāb de « يوم » : badal du pronom caché de « يكون » de Sa parole
    « عسى أن يكون قريبًا » (fatḥa de construction — annexé à la clause
    verbale) ou ẓarf de « يكون » (fatḥa d'accusatif) — reconstruit d'après
    la grammaire ; l'original porte « بدل من قوله ﴿قريباً﴾ » ;
  * « يدعوكم » (l'appel : la souffle du cor) ;
  * « فتستجيبون » et « بحمد ربكم » ×3 (Ibn ʿAbbās/Ibn Jurayj : bi-amrihi ;
    Qatāda : bi-ṭāʿatihi ; les deux lectures d'Ibn ʿAṭiyya — VÉRIFIÉ) ;
  * « وتظنون إن لبثتم إلا قليلا » + preuve de Ṭabarī : Muʾminūn 113-114
    (span imprimé « [المؤمنون: 113-114] » — l'original cite 112-113 avec
    « أبو » pour « أو » : coquille notée) ;
  * v53 + « يقولوا » (Sībawayh : jawāb sharṭ muqaddar — VÉRIFIÉ ;
    al-Akhfash : jawāb al-amr) + « التي هي أحسن » (la shahāda selon une
    frange vs la muḥāwara ḥusnā du jumhūr — VÉRIFIÉ) + « لعبادي » ×2
    (VÉRIFIÉ : « ويلزم على هذا أن يكون قوله ﴿لعبادي﴾... » / « وقوله
    ﴿لعبادي﴾ خاص بالمؤمنين ») ;
  * « إن الشيطان ينزغ بينهم » (la motivation) + « إن الشيطان كان للإنسان
    عدوا مبينا » (la cause : l'inimitié ancienne) + spans [الأعراف: 16] et
    [الحجر → imprime « الحشر »: 16] — Ḥashr 16 RESTAURÉ (كمثل الشيطان
    إذ قال للإنسان اكفر) ;
  * v54 (le sceau : « ربكم أعلم بكم... وما أرسلناك عليهم وكيلا ») + « ربكم
    أعلم بكم » (l'interpellation des Quraysh — VÉRIFIÉ) + « وما أرسلناك
    عليهم وكيلا » (la preuve par le passage à la 3e personne — VÉRIFIÉ) +
    « يرحمكم » (VÉRIFIÉ : Ibn Jurayj — par le repentir) ;
  * v55 + « بمن في السماوات والأرض » (le bāʾ selon Abū ʿAlī al-Fārisī vs
    « أعلم » — Ibn ʿAṭiyya : cela ne s'impose pas) + « فضلنا بعض النبيين »
    + « زبورا » (la lecture du jumhūr au fatḥa — faʿūl bi-maʿnā mafʿūl) ;
  * taqwīm 3 : « يوم يدعوكم فتستجيبون بحمد ربكم » (le crux du §) ;
  * maqṣid 4 : « بل تقول: ___ » → Sabāʾ 24 (إنا أو إياكم لعلى هدى أو في
    ضلال مبين) — identifié par le contexte (ne pas trancher du sort) ;
  * istithmār : ʿImrān 159, Ṭā-Hā 43-44 (réf imprimée « 43 » — le couplet
    restitué, la parole douce au v. 44), Anʿām 108 (réf imprimée « 109 » —
    erreur d'adjacence notée ; le contenu = la défense de ne pas injurier
    les idoles), Naḥl 125 (le <p> vide + le span) ;
  * iʿdād : 4 expressions du lexique de 13620 (v56-60 : yabtaghūna/
    al-wasīla/maḥdhūran/masṭūran) + citation → v57 (la doctrine de la
    wasīla — crux de la leçon suivante) — noté.
- Hadiths : « بعثت أنا والساعة كهاتين » ; Bukhārī « وكونوا عباد الله
  إخوانا » ; Muslim (Abū Hurayra) « لا يشير أحدكم إلى أخيه بالسلاح... » ;
  Muslim « وأهل النار خمسة: الضعيف الذي لا زبر له » — tous intacts."""

import json

BOOK = "/home/z/my-project/content/books/tafsir-tanawi-2.json"

HTML_FR = """<h1>La sourate al-Isrāʾ — <em>al-Muḥarrar al-wajīz</em> d’Ibn ʿAṭiyya, versets 49 à 55</h1>
<p>Leçon d’exégèse de la sourate al-Isrāʾ, versets 49 à 55, du livre du Tafsīr à travers <em>al-Muḥarrar al-wajīz fī tafsīr al-kitāb al-ʿazīz</em> du cadi Abū Muḥammad Ibn ʿAṭiyya, à l’intention des élèves de la deuxième année de l’enseignement secondaire traditionnel (<em>taʿlīm ʿatīq</em>), phase 2 (leçon 14).</p>
<h3>Les objectifs de la leçon</h3>
<ul>
<li>Connaître les indices de la puissance de Dieu sur la résurrection, et la réfutation des objections de ses négateurs.</li>
<li>Conclure des versets quelques convenances du discours et la belle conduite envers les gens.</li>
<li>Affermir ma foi en la résurrection et la sortie des tombes, pour me munir des œuvres vertueuses en vue de la vie dernière.</li>
</ul>
<h3>Introduction (tamhīd)</h3>
<p>Après que le Vrai, glorifié soit-Il, eut parlé des divinités et des prophéties, Il parle en ces versets de quelques questions transmises : Il expose certaines objections des négateurs de la résurrection et les réfute par les démonstrations rationnelles concluantes qui attestent sa venue — orientant Ses serviteurs croyants à disputer avec les autres et à débattre avec eux avec douceur, sans rudesse envers eux dans la parole : car la bonne parole attire les âmes et les incline à la conviction.</p>
<p>Comment le noble Coran a-t-il réfuté les objections des négateurs de la résurrection ? Et quelles sont les convenances de l’islam dans l’adresse aux gens en général, et aux divergents en religion en particulier ?</p>
<h3>Les versets</h3>
<p>Allah, le Très-Haut, a dit :</p>
<p>« Et ils disent : “ Quand nous serons ossements et poussière, serons-nous ressuscités en une nouvelle création ? ” (49) Dis : “ Soyez pierre ou fer, (50) ou toute autre créature que vous puissiez concevoir. ” Ils diront alors : “ Qui donc nous fera revenir ? ” — Dis : “ Celui qui vous a créés la première fois. ” Ils secoueront vers toi leurs têtes et diront : “ Quand cela ? ” — Dis : “ Il se peut que ce soit proche : (52) le jour où Il vous appellera, vous Lui répondrez en Le glorifiant. Vous penserez cependant que vous n’êtes restés [sur terre] que peu de temps ! (53) Et dis à Mes serviteurs d’exprimer les meilleures paroles, car le Diable sème la discorde parmi eux. Le Diable est certes, pour l’homme, un ennemi déclaré. (54) Votre Seigneur vous connaît mieux. S’Il veut, Il vous fera miséricorde, et s’Il veut, Il vous châtiera. Et Nous ne t’avons pas envoyé pour que tu sois leur protecteur. (55) Et ton Seigneur est plus Connaisseur de ceux qui sont dans les cieux et sur la terre. Et parmi les prophètes, Nous avons donné à certains plus de faveurs qu’à d’autres. Et à David Nous avons donné le Zabûr. ” » (al-Isrāʾ, 49-55)</p>
<p>[Citations coraniques restaurées d’après le corpus canonique : l’emplacement imprimé correspondant est vide dans la source numérisée — perte OCR.]</p>
<h3>La compréhension</h3>
<h4>Explication des termes</h4>
<ul>
<li><em>rufātan</em> (des débris) : ce qui, de toute chose, se brisa et se défit — comme les miettes.</li>
<li><em>jadīdan</em> (nouveau) : attribut de ce qui, des choses, est proche d’advenir.</li>
<li><em>fatarakum</em> (qui vous a fait exister) : Il vous a créés.</li>
<li><em>al-nazgh</em> (la sollicitation) : le mouvement véloce du démon, pour produire la corruption.</li>
</ul>
<h3>Extraction des idées des versets</h3>
<ul>
<li>Quelle fut l’attitude des associateurs envers la résurrection ? Et quelle est la réponse coranique qui leur fut faite ?</li>
<li>Qu’est-ce que Dieu ordonna aux croyants dans leur conduite avec les gens ?</li>
</ul>
<h3>Le commentaire (tafsīr)</h3>
<p>Ces versets comprennent ce qui suit :</p>
<h3>Premièrement : les objections des négateurs de la résurrection, et la réfutation que Dieu en fait par les démonstrations concluantes</h3>
<p>Le Très-Haut a dit :</p>
<p>« Et ils disent : “ Quand nous serons ossements et poussière, serons-nous ressuscités en une nouvelle création ? ” » (al-Isrāʾ, 49)</p>
<p>Ce verset concerne la négation, par les dénégateurs de Quraysh, de la résurrection : c’est de leur part étonnement, négation et tenue pour lointaine de la revivification après la mort.</p>
<p>[Citation coranique (v. 49) restaurée d’après le corpus canonique : l’emplacement imprimé est vide — perte OCR.]</p>
<p>Le <em>rufāt</em> (débris) est ce sur quoi le temps passa jusqu’à lui faire atteindre l’extrême décrépitude et le rapprocher de l’état de poussière — l’on dit : <em>rafta rufātan</em>, comme <em>ḥiṭām</em> et <em>fatāt</em>. Dit Ibn ʿAbbās : <em>rufātan</em> : poussière. Et dit Mujāhid : terre. Et <em>jadīdan</em> (nouveau) est attribut de ce qui, des choses, est proche d’advenir — il décrit par lui le masculin et le féminin.</p>
<p>[Vedettes « rufātan » et « jadīdan » restaurées du lexique (têtes perdues — perte OCR) ; gloses conformes au texte d’Ibn ʿAṭiyya.]</p>
<p>Ce verset atteste leur négation de la résurrection et du compte, et leur tenue pour lointaine de sa venue : car ils tiennent pour lointain que la vie revienne aux ossements décrépits, pour qu’en soit créée une création nouvelle.</p>
<p>Et Dieu ordonna à Son prophète de répondre à ces négateurs de la résurrection par Sa parole :</p>
<p>« Dis : “ Soyez pierre ou fer ”. » (al-Isrāʾ, 50)</p>
<p>— c’est-à-dire : dis-leur, Muḥammad : soyez non point seulement ossements et débris, mais soyez pierre ou fer — si vous pouvez être ces choses rudes, dont l’avènement est impossible : votre résurrection est inévitable, car Dieu est puissant à vous revivifier de nouveau.</p>
<p>[Citation coranique (v. 50) restaurée d’après le corpus canonique : l’emplacement imprimé est vide — perte OCR.]</p>
<p>Et Sa parole, le Très-Haut :</p>
<p>« …ou toute autre créature que vous puissiez concevoir. » (al-Isrāʾ, 51)</p>
<p>On dit : le visé par la création qui « prend du volume en vos poitrines » est les cieux et la terre et les montagnes. On dit : le visé est la mort. On dit : toute chose que les gens tiennent pour grande, plus grande que la pierre et le fer — au sens que Dieu, Puissant et Majestueux, vous ressuscitera inévitablement, quelles que soient les choses, rebelles à la vie, que vous vous supposiez être. Et c’est ce qu’al-Ṭabarī préféra — et c’est le plus juste : car Il commença par une chose dure, la pierre, puis mentionna, par voie d’ascension, la plus dure qu’elle, le fer, puis renvoya à ce qu’ils supposent en leur pensée et qui traverse leur esprit des choses plus dures que le fer : il n’y a pas lieu de particulariser une chose plutôt qu’une autre — c’est-à-dire : supposez vos êtres quelque chose de celles-ci, votre résurrection vous est inévitable, en quelque état que vous soyez. [al-Baḥr al-Muḥīṭ, d’Abū Ḥayyān : 7/63 — réf. imprimée « 63/7 », ordre inversé]</p>
<p>[Citation coranique (v. 51, ouverture) restaurée d’après le corpus canonique : l’emplacement imprimé est vide — perte OCR.]</p>
<p>Et Sa parole, le Très-Haut :</p>
<p>« Ils diront alors : “ Qui donc nous fera revenir ? ” — Dis : “ Celui qui vous a créés la première fois. ” » (al-Isrāʾ, 51)</p>
<p>— c’est-à-dire : ils disent, par voie de négation : qui nous fera revenir, si nous sommes pierre, ou fer, ou quelque autre création rude ? Dieu, Puissant et Majestueux, leur objecta la première création, sur la possibilité de la seconde. Dit Ibn Kathīr : c’est-à-dire : Celui qui vous créa — quand vous n’étiez rien de mentionnable — puis que vous devîntes des humains qui se propagent, est puissant à vous retourner, dussiez-vous tomber en quelque état :</p>
<p>« Et c’est Lui qui commence la création puis la refait ; et cela Lui est plus facile. Il a la transcendance absolue dans les cieux et sur la terre. C’est Lui le Tout Puissant, le Sage. » (ar-Rūm, 27)</p>
<p>[Citation coranique (v. 51, milieu) et citation d’ar-Rūm 27 (span imprimé « [الروم: 27] ») restaurées d’après le corpus canonique : les emplacements imprimés sont vides — perte OCR.] [Tafsīr al-Qurʾān al-ʿaẓīm, d’Ibn Kathīr : 5/85]</p>
<p>Puis le Très-Haut dit :</p>
<p>« Ils secoueront vers toi leurs têtes et diront : “ Quand cela ? ” — Dis : “ Il se peut que ce soit proche ”. » (al-Isrāʾ, 51 — fin)</p>
<p>— c’est-à-dire : ils la remueront : ils l’élèveront et l’abaisseront, par manière de dénégation et de raillerie — “ quand la résurrection ? ” : cela aussi, ils le dirent par raillerie. Dit al-Ṭabarī et Ibn Sallām : <em>ʿasā</em> (« il se peut »), de Dieu, induit l’obligation — au sens que la résurrection est proche. Dit Ibn ʿAṭiyya : et celle-ci n’est que [la parole] du Prophète — paix sur lui —, mais par l’ordre de Dieu : cela la rapproche de l’obligation. De même dit — paix et bénédiction sur lui : “ Je fus envoyé, moi et l’Heure, comme ces deux-là ” — et l’expression contient, en son sein, une menace pour eux.</p>
<p>[Citation coranique (v. 51, fin) et mot « ʿasā » restaurés d’après le corpus canonique : les emplacements imprimés sont vides — perte OCR.]</p>
<p>Puis le Très-Haut dit :</p>
<p>« Le jour où Il vous appellera, vous Lui répondrez en Le glorifiant. Vous penserez cependant que vous n’êtes restés [sur terre] que peu de temps ! » (al-Isrāʾ, 52)</p>
<p>Sa parole : <em>yawma</em> (« le jour ») est substitut (<em>badal</em>) du pronom caché en <em>yakūna</em> (« que ce soit ») de Sa parole : <em>ʿasā an yakūna qarīban</em> (« il se peut que ce soit proche ») ; sa <em>fatḥa</em> est une <em>fatḥa</em> de construction, parce qu’il est annexé à la clause verbale ; et il se peut qu’il soit adverbe (<em>ẓarf</em>) de <em>yakūna</em> — l’estimation : ce sera le jour où Il vous appellera — sa <em>fatḥa</em> étant une <em>fatḥa</em> d’accusatif, pour l’adverbialité.</p>
<p>Et Sa parole : <em>yadʿūkum</em> (« Il vous appellera ») — son sens : Il vous appellera de vos tombes, par le souffle du cor, pour le lever de l’Heure.</p>
<p>[Citation coranique (v. 52) et mots « yakūna » (×2), « ʿasā an yakūna qarīban » et « yadʿūkum » restaurés d’après le corpus canonique et reconstruits d’après la grammaire : les emplacements imprimés sont vides — perte OCR. L’original d’Ibn ʿAṭiyya porte : « ﴿يوم﴾ بدل من قوله ﴿قريباً﴾ » — badal de « qarīban » ; le manuel détaille l’iʿrāb par le pronom caché de « yakūna ».]</p>
<p>Et Sa parole, glorifié soit-Il : <em>fa-tastajībūna</em> (« vous Lui répondrez ») — c’est-à-dire : par le lever, le retour et le surgissement vers l’appel. Et Sa parole : <em>bi-ḥamdi rabbikum</em> (« en Le glorifiant ») : al-Ṭabarī rapporta d’Ibn ʿAbbās qu’il dit : son sens est “ par Son ordre ” (<em>bi-amrihi</em>) ; de même dit Ibn Jurayj. Et dit Qatāda : son sens est “ par Son obéissance et Sa connaissance ” (<em>bi-ṭāʿatihi wa-maʿrifatihi</em>). Tout cela est interprétation que l’expression ne donne pas ; nul doute que tout cela est par l’ordre de Dieu, le Très-Haut — mais le sens de <em>bi-ḥamdi rabbikum</em> est : ou bien tous les êtres du monde se lèvent — comme dit [Ibn] Jubayr — louant Dieu et Le glorifiant pour ce que leur paraît de Sa puissance ; ou bien Sa parole : <em>bi-ḥamdi rabbikum</em> est comme tu dis à un homme que tu as contredit et avec qui tu as débattu en science : “ tu t’es trompé — à la louange de Dieu ” (<em>bi-ḥamdi Allāh</em>) — c’est comme si le Prophète — paix et bénédiction sur lui — leur disait, en ces versets : il se peut que l’Heure soit proche — le jour où vous serez appelés et vous vous lèverez autrement que ce que vous tenez maintenant, et ce, à la louange de Dieu sur la véracité de ma nouvelle. Al-Ṭabarī suivit ce penchant.</p>
<p>[Mots « fa-tastajībūna » et « bi-ḥamdi rabbikum » (×3) restaurés d’après le corpus canonique et le texte d’Ibn ʿAṭiyya : les emplacements imprimés sont vides — perte OCR.]</p>
<p>Et Sa parole, le Très-Haut : <em>wa-taẓunnūna in labithtum illā qalīlā</em> (« vous penserez… que peu de temps ») comporte deux sens :</p>
<p>Le premier : Il informa que, quand ils furent ramenés à l’état de vie et au mouvement des corps, il leur advint la pensée qu’ils ne s’étaient séparés de l’état du monde que depuis peu — parce que la science de la quantité du temps leur est dérobée : celui qui est en l’au-delà ne mesure pas le temps du monde, car il est, à n’en pas douter, plus séparé de lui que les dormants. C’est sur cette interprétation qu’al-Ṭabarī s’appuya, étayée par la parole du Très-Haut :</p>
<p>« Ils diront : “ Nous y avons demeuré un jour, ou une partie d’un jour. Interroge donc ceux qui comptent. ” (113) Il dira : “ Vous n’y avez demeuré que peu [de temps], si seulement vous saviez ! ” » (al-Muʾminūn, 113-114)</p>
<p>[Citation coranique (al-Muʾminūn, 113-114 — span imprimé « [المؤمنون: 113-114] ») restaurée d’après le corpus canonique : l’emplacement imprimé est vide — perte OCR. Le texte d’Ibn ʿAṭiyya cite Muʾminūn 112-113, avec « يوماً أبو بعض يوم » — coquille pour « أو » (ou), notée.]</p>
<p>Le second : que le <em>ẓann</em> (la pensée) soit au sens de la certitude (<em>yaqīn</em>) — c’est comme s’Il leur avait dit : le jour où vous serez appelés et répondrez, à la louange de Dieu, et vous saurez de certitude que vous n’êtes demeurés que peu, du fait que [ce peu] est achevé et délimité. C’est comme l’on dit du monde entier : “ jouissance de peu ” — comme qui dirait petitesse d’estimation. Que le <em>ẓann</em> soit au sens de la certitude est faible ici : car il porte sur une chose advenue — or le <em>ẓann</em> au sens de certitude ne vient que pour ce qui n’est pas encore sorti à l’être et l’existence.</p>
<p>En la parole il y a affermissement de la résurrection — c’est comme s’Il disait : toi, dénégateur du rassemblement, qui tiens que tu ne seras jamais ressuscité : inévitablement tu seras appelé à la résurrection, tu te lèveras, et tu verras que tu n’es demeuré que peu, achevé et consommé. Et al-Ṭabarī rapporta de Qatāda que, quand ils virent l’horreur du Jour de la résurrection, ils méprisèrent le monde et pensèrent qu’ils n’y avaient demeuré que peu.</p>
<p>[Mots « wa-taẓunnūna in labithtum illā qalīlā » restaurés d’après le corpus canonique : l’emplacement imprimé est vide — perte OCR.]</p>
<h3>Deuxièmement : l’ordre de Dieu aux croyants de la belle conduite et de la parole adoucie</h3>
<p>Après le rapport des paroles des associateurs et de leur égarement doctrinal, Il ordonna aux croyants de dire une parole belle, qui exprime la pureté de leur doctrine et la bonté de leur secret. Le Très-Haut a dit :</p>
<p>« Et dis à Mes serviteurs d’exprimer les meilleures paroles, car le Diable sème la discorde parmi eux. Le Diable est certes, pour l’homme, un ennemi déclaré. » (al-Isrāʾ, 53)</p>
<p>[Citation coranique (v. 53) restaurée d’après le corpus canonique : l’emplacement imprimé est vide — perte OCR.]</p>
<p>Les grammairiens divergèrent sur Sa parole : <em>yaqūlū</em> (« qu’ils disent »). L’école de Sībawayh : c’est la réponse d’une condition estimée — l’estimation : et dis à Mes serviteurs : si tu leur dis, ils diront — sur son principe que l’impératif n’a point de réponse, et que ce qui lui répond est une condition estimée. L’école d’al-Akhfash : l’impératif a une réponse, et Sa parole ici est réponse de <em>qul</em> (« dis »).</p>
<p>[Mot « yaqūlū » restauré d’après le corpus canonique : l’emplacement imprimé est vide — perte OCR ; le différend Sībawayh/al-Akhfash vérifié sur le texte d’Ibn ʿAṭiyya.]</p>
<p>Et les gens divergèrent sur <em>allatī hiya aḥsan</em> (« les meilleures paroles »). Un groupe dit : c’est “ nul dieu sinon Dieu ” (<em>lā ilāha illā Allāh</em>) — et il s’ensuit, en ce cas, que Sa parole : <em>li-ʿibādī</em> (« à Mes serviteurs ») vise la création entière, car toute la création est appelée à “ nul dieu sinon Dieu ” ; et Sa parole ensuite ne vient point convenir au sens — sauf à faire de “ entre eux ” (baynahum) le sens de “ parmi eux ”, et du <em>nazgh</em> le sens de la suggestion et de l’égarement. Et dit le <em>jumhūr</em> : ce sont les échanges les plus beaux selon le sens — dit al-Ḥasan : c’est dire : “ que Dieu te pardonne, que Dieu te fasse miséricorde ”.</p>
<p>Et Sa parole : <em>li-ʿibādī</em> (« à Mes serviteurs ») est spécifique aux croyants — le verset est alors au sens du dire de — paix sur lui : “ Soyez, serviteurs de Dieu, des frères ”. [Ṣaḥīḥ al-Bukhārī, livre des convenances, chapitre de l’interdiction de l’envie et du reniement]</p>
<p>[Mots « allatī hiya aḥsan » et « li-ʿibādī » (×2) restaurés d’après le corpus canonique et le texte d’Ibn ʿAṭiyya : les emplacements imprimés sont vides — perte OCR.]</p>
<p>Puis ils divergèrent. Un groupe dit : Dieu ordonna aux croyants, entre eux, la belle conduite, l’abaissement de l’aile, l’adoucissement de la parole, et le rejet des sollicitations du démon. Un groupe dit : Dieu n’ordonna, en ce verset, aux croyants que l’adoucissement de la parole envers les associateurs de La Mecque. Le pareil de ce verset est Sa parole :</p>
<p>« Par la sagesse et la bonne exhortation appelle (les gens) au sentier de ton Seigneur. Et discute avec eux de la meilleure façon. Car c’est ton Seigneur qui connaît le mieux celui qui s’égare de Son sentier et c’est Lui qui connaît le mieux ceux qui sont bien guidés. » (an-Naḥl, 125)</p>
<p>et Sa parole :</p>
<p>« Et ne discutez que de la meilleure façon avec les gens du Livre, sauf ceux d’entre eux qui sont injustes. Et dites : “ Nous croyons en ce qu’on a fait descendre vers nous et descendre vers vous, tandis que notre Dieu et votre Dieu est le même, et c’est Lui que nous obéissons. ” » (al-ʿAnkabūt, 46)</p>
<p>[Citations coraniques (an-Naḥl, 125 et al-ʿAnkabūt, 46 — spans imprimés « [النحل: 125] » et « [العنكبوت: 46] ») restaurées d’après le corpus canonique : les emplacements imprimés sont vides — perte OCR.]</p>
<p>Puis Il motiva l’ordre de dire les meilleures paroles par Sa parole : <em>inna l-shayṭāna yanzaġu baynahum</em> (« car le Diable sème la discorde parmi eux »). Le visé de cette motivation : qu’ils ne prennent point à la légère les paroles corrompues — car elles excitent des corruptions de l’œuvre du démon, qui jette entre eux la corruption et incite les uns contre les autres : il advient entre eux l’inimitié et la haine — car le <em>nazgh</em> est le mouvement véloce du démon pour produire la corruption. D’Abū Hurayra — Dieu l’agrée : le Messager de Dieu — paix et bénédiction sur lui — dit : “ Que nul de vous ne pointe son frère d’une arme : nul de vous ne sait — peut-être le démon sollicitera-t-il sa main, et il tombera dans une fosse du Feu ”. [Ṣaḥīḥ Muslim, livre de la piété filiale et des convenances, chapitre de l’interdiction de pointer l’arme contre un musulman]</p>
<p>[Clause « inna l-shayṭāna yanzaġu baynahum » restaurée d’après le corpus canonique : l’emplacement imprimé est vide — perte OCR.]</p>
<p>Puis Il exposa la cause de la sollicitation du démon envers l’homme par Sa parole : <em>inna l-shayṭāna kāna li-l-insāni ʿaduwwan mubīnā</em> (« Le Diable est certes, pour l’homme, un ennemi déclaré ») — c’est-à-dire : entre le démon et l’homme est une inimitié ancienne, enracinée — comme dit le Très-Haut, rapportant du démon :</p>
<p>« Puisque Tu m’as mis en erreur, dit [Satan], je m’assoirai pour eux sur Ton droit chemin. » (al-Aʿrāf, 16)</p>
<p>Et Il dit :</p>
<p>« [ils sont] semblables au Diable quand il dit à l’homme : “ Sois incrédule. ” Puis quand il a mécru, il dit : “ Je te désavoue car je redoute Allah, le Seigneur de l’Univers ”. » (al-Ḥashr, 16)</p>
<p>[Clause « inna l-shayṭāna kāna li-l-insāni ʿaduwwan mubīnā » et citations d’al-Aʿrāf 16 et al-Ḥashr 16 (spans imprimés « [الأعراف: 16] » et « [الحشر: 16] ») restaurées d’après le corpus canonique : les emplacements imprimés sont vides — perte OCR.]</p>
<p>Puis Dieu, le Très-Haut, scella ce verset de ce qui, en lui, affermit et motive ce qui précède, par Sa parole :</p>
<p>« Votre Seigneur vous connaît mieux. S’Il veut, Il vous fera miséricorde, et s’Il veut, Il vous châtiera. Et Nous ne t’avons pas envoyé pour que tu sois leur protecteur. » (al-Isrāʾ, 54)</p>
<p>Ce verset renforce que le précédent concerne ce qui est entre les serviteurs croyants et les dénégateurs de La Mecque : l’interpellation de Sa parole : <em>rabbukum aʿlamu bikum</em> (« Votre Seigneur vous connaît mieux ») est aux dénégateurs de La Mecque — preuve en Sa parole : <em>wa-mā arsalnāka ʿalayhim wakīlā</em> (« Et Nous ne t’avons pas envoyé pour que tu sois leur protecteur »). C’est comme si Dieu, Puissant et Majestueux, avait ordonné aux croyants de n’être point rudes aux dénégateurs en la religion — puis dit aux dénégateurs : Il les connaît le mieux, leur donna espoir et les menaça. Et le sens de <em>yarḥamkum</em> (« Il vous fera miséricorde ») : par le repentir sur vous du déni — dit Ibn Jurayj et d’autres. Puis Il dit au Prophète — paix et bénédiction sur lui : <em>wa-mā arsalnāka ʿalayhim wakīlā</em> (« Et Nous ne t’avons pas envoyé pour que tu sois leur protecteur ») — sur toi est seulement la transmission : tu n’es point tuteur de leur foi, à n’en pas douter — et les versets se coordonnent sur cette interprétation.</p>
<p>[Citations coraniques (v. 54 complet ; mots « rabbukum aʿlamu bikum », « wa-mā arsalnāka ʿalayhim wakīlā » (×2) et « yarḥamkum ») restaurées d’après le corpus canonique et le texte d’Ibn ʿAṭiyya : les emplacements imprimés sont vides — perte OCR.]</p>
<h3>Troisièmement : l’excellence de certains prophètes, et le Zabûr de David</h3>
<p>Puis le Béni, le Très-Haut, dit à Son prophète — paix et bénédiction sur lui :</p>
<p>« Et ton Seigneur est plus Connaisseur de ceux qui sont dans les cieux et sur la terre. Et parmi les prophètes, Nous avons donné à certains plus de faveurs qu’à d’autres. Et à David Nous avons donné le Zabûr. » (al-Isrāʾ, 55)</p>
<p>Sa parole : <em>bi-man fī s-samāwāti wa-l-arḍi</em> (« de ceux qui sont dans les cieux et la terre ») : le <em>bāʾ</em> se rattache à un verbe estimé — “ Il connaît (ʿalima) ceux qui sont dans les cieux ” : Abū ʿAlī al-Fārisī y alla — car s’il le rattachait à <em>aʿlamu</em> (« plus Connaisseur »), il induirait qu’Il n’est pas plus connaisseur d’autre chose. Dit Ibn ʿAṭiyya : cela ne s’ensuit pas — et le rattachement à <em>aʿlamu</em> est valable, sans égard à l’inférence du contraire.</p>
<p>Et Sa parole, le Très-Haut : <em>wa-la-qad faḍḍalnā baʿḍa l-nabiyyīna ʿalā baʿḍ</em> (« parmi les prophètes, Nous avons donné à certains plus de faveurs ») — c’est-à-dire : c’est Lui qui préféra certains prophètes à d’autres, selon Sa science d’eux. C’est une allusion à Muḥammad — paix et bénédiction sur lui — et au tenir-pour-lointain de Quraysh que le messager soit un humain. Le sens : ne tenez pas l’affaire de Muḥammad à l’étrange — paix sur lui — quand il reçut un Coran : les prophètes avant lui furent préférés, et David reçut un Zabûr — Dieu sait le mieux où Il dépose Ses messages.</p>
<p>Et la préférence de certains messagers est : ou bien par cette annonce globale, sans nommer le préféré — et sur ce [principe], il nous est loisible de dire : Muḥammad — paix et bénédiction sur lui — est le meilleur des humains ; et il interdit — prière et salut sur lui — de désigner qui que ce soit d’entre eux, en l’histoire de Moïse et de Jonas. Ou bien la préférence est répartie en eux : à Moïse fut donné l’entretien (<em>taklīm</em>) ; à Muḥammad — paix et bénédiction sur lui —, les cinq [prières] ; à Jésus, la revivification (<em>iḥyāʾ</em>) : tous sont préférés sur un point, préférés absolument.</p>
<p>Et le <em>jumhūr</em> lut : <em>zabūran</em>, au <em>fatḥa</em> du <em>zāy</em> — schème <em>faʿūl</em> au sens de <em>mafʿūl</em> (objet), chose rare qui ne vint qu’en <em>qudūh</em>, <em>rukūb</em> et <em>ḥalūb</em>. Et Ḥamza, Yaḥyā et al-Aʿmash lurent <em>zubūran</em>, au <em>ḍamma</em> du <em>zāy</em> — ce qui a deux faces :</p>
<ul>
<li>La première : qu’il soit pluriel de <em>zabūr</em> avec effacement de l’ajouté, comme l’on dit au pluriel de <em>ẓarīf</em> : <em>ẓurūf</em>.</li>
<li>La seconde : qu’il soit pluriel de <em>zibr</em>, comme <em>qishr/qushūr</em> — au sens de <em>mazbūr</em> (ce qui fut écrit) : comme si ce que David reçut eût été divisé en parts, chaque part étant un <em>zibr</em> — nommé du maṣdar de <em>zabara yazbiru</em>, puis ces parts réunies en <em>zubūr</em> : c’est comme s’Il avait dit : Nous donnâmes à David des écritures. Il se peut aussi que ce soit le pluriel du <em>zabr</em> qui est la raison et la justesse du jugement (<em>al-ʿaql wa-sinādat al-naẓar</em>) : car David reçut quantité d’exhortations et d’admonitions. De là la parole du Prophète — paix et bénédiction sur lui —, en la fin du livre de Muslim : “ les gens du Feu sont cinq : le faible qui n’a point de <em>zabr</em> (raison) ”. [Ṣaḥīḥ Muslim, livre du Paradis, chapitre des traits par lesquels on reconnaît en ce monde les gens du Paradis et les gens du Feu] Dit Qatāda : le Zabûr de David est exhortations, sagesse et invocation — il n’y a pas en lui de permis ni d’interdit.</li>
</ul>
<p>[Citations coraniques (v. 55 complet ; mots « bi-man fī s-samāwāti wa-l-arḍi », « aʿlamu » (×2), « wa-la-qad faḍḍalnā baʿḍa l-nabiyyīna ʿalā baʿḍ » et « zabūran ») restaurées d’après le corpus canonique : les emplacements imprimés sont vides — perte OCR.]</p>
<h3>Les finalités des versets</h3>
<p>Ces versets orientent vers la réalisation d’un ensemble de finalités éducatives, dont :</p>
<ul>
<li>L’affirmation de la venue de la résurrection et de la revivification des gens après la mort, par les preuves et les démonstrations — et la réfutation des objections de ses négateurs, qui tiennent pour lointaine la revivification de qui n’est plus que débris : leurs intelligences ne l’admettent pas, par analogie sur la puissance limitée des créatures.</li>
<li>L’établissement de la résurrection n’est pas visé pour lui-même : il l’est pour ce qui suit de la croyance en lui — le redressement de la conduite, la réforme des membres, et l’avance des œuvres de bien et des obéissances en vue de ce jour immense.</li>
<li>L’ordre de la convenance en la parole avec les gens, de l’abaissement de l’aile et de l’adoucissement de la parole envers eux — tant dans leur traitement mutuel que dans leur débat avec les associateurs.</li>
<li>Parmi les orientations coraniques dans le traitement du divergent en religion : ne point porter atteinte à sa religion, ni injurier son adoré, ni lui trancher son sort en l’au-delà — mais dire :</li>
</ul>
<p>« C’est nous ou bien vous qui sommes sur une bonne voie, ou dans un égarement manifeste. » (Sabāʾ, 24)</p>
<p>Nul doute que ce style d’adresse est un style sage : il contribue au rapprochement et à l’écoute, affermit la confiance et aide à l’appel à Dieu et à la diffusion de Sa religion.</p>
<p>[Citation coranique (Sabāʾ, 24) restituée d’après le corpus canonique : l’emplacement imprimé est vide — perte OCR ; identification par le contexte (la formule de la disjonction sans trancher du sort de l’interlocuteur).]</p>
<h3>L’évaluation (taqwīm)</h3>
<ul>
<li>J’extrais l’objection sur laquelle les associateurs s’appuyèrent pour nier la résurrection.</li>
<li>Je conclus des versets les indices de la venue de la résurrection et de la sortie des tombes.</li>
<li>Que signifient l’appel et la réponse en la parole du Très-Haut : « Le jour où Il vous appellera, vous Lui répondrez en Le glorifiant » ?</li>
</ul>
<p>[Citation coranique (v. 52 — objet de la troisième question) restaurée d’après le corpus canonique : l’emplacement imprimé est vide — perte OCR.]</p>
<h3>L’investissement (istithmār)</h3>
<p>Le Très-Haut a dit :</p>
<p>« C’est par quelque miséricorde de la part d’Allah que tu (Muhammad) as été si doux envers eux ! Mais si tu étais rude, au cœur dur, ils se seraient enfuis de ton entourage. Pardonne-leur donc, et implore pour eux le pardon (d’Allah). Et consulte-les à propos des affaires ; puis, une fois que tu t’es décidé, confie-toi donc à Allah. Car Allah aime, en vérité, ceux qui Lui font confiance. » (Āl ʿImrān, 159)</p>
<p>Et le Très-Haut dit à Moïse et Aaron quand Il les envoya vers Pharaon :</p>
<p>« Allez vers Pharaon : il s’est vraiment rebellé. (43) Puis, parlez-lui gentiment ; peut-être se rappellera-t-il ou [Me] craindra-t-il ? » (Ṭā-Hā, 43-44)</p>
<p>Et le Glorifié dit :</p>
<p>« N’injuriez pas ceux qu’ils invoquent, en dehors d’Allah, car par agressivité, ils injurieraient Allah, dans leur ignorance. De même, Nous avons enjolivé (aux yeux) de chaque communauté sa propre action. Ensuite, c’est vers leur Seigneur que sera leur retour, et Il les informera de ce qu’ils œuvraient. » (al-Anʿām, 108)</p>
<p>Et le Très-Haut dit :</p>
<p>« Par la sagesse et la bonne exhortation appelle (les gens) au sentier de ton Seigneur. Et discute avec eux de la meilleure façon. Car c’est ton Seigneur qui connaît le mieux celui qui s’égare de Son sentier et c’est Lui qui connaît le mieux ceux qui sont bien guidés. » (an-Naḥl, 125)</p>
<p>[Citations coraniques (Āl ʿImrān, 159 ; Ṭā-Hā, 43-44 ; al-Anʿām, 108 ; an-Naḥl, 125) restaurées d’après le corpus canonique : les emplacements imprimés sont vides — perte OCR. Réfs imprimées : « [طه: 43] » — le couplet 43-44 restitué, la parole douce étant au v. 44 ; « [الأنعام: 109] » — le contenu est celui du v. 108 (l’interdit d’injurier les adorés), erreur d’adjacence notée ; « [النحل: 125] » conforme.]</p>
<p>Je contemple les versets et réponds à ce qui suit :</p>
<ul>
<li>Quel est le rapport des versets avec le sujet de la leçon ?</li>
<li>Quels sont les effets de la convenance en la parole entre les musulmans — et entre eux et les autres ?</li>
</ul>
<h3>La préparation (iʿdād)</h3>
<p>Je contemple les versets 56 à 60 de la sourate al-Isrāʾ et réponds à ce qui suit :</p>
<ul>
<li>Je recherche la portée des expressions suivantes :</li>
</ul>
<p><em>yabtaghūna</em> (يَبْتَغُونَ — ils cherchent).</p>
<p><em>al-wasīla</em> (ٱلْوَسِيلَةَ — le moyen d’approche).</p>
<p><em>maḥdhūran</em> (مَحْذُورًا — redouté).</p>
<p><em>masṭūran</em> (مَسْطُورًا — écrit).</p>
<p>[Expressions restituées du lexique de la leçon suivante (versets 56-60) : les emplacements imprimés sont vides — perte OCR.]</p>
<ul>
<li>Je recherche la sagesse pour laquelle Dieu, le Très-Haut, ne particularisa point Quraysh d’un signe de Ses signes, à la différence des communautés antérieures.</li>
</ul>
<ul>
<li>J’explicite le sens de la parole du Très-Haut :</li>
</ul>
<p>« Ceux qu’ils invoquent, cherchent [eux-mêmes], à qui mieux, le moyen de se rapprocher le plus de leur Seigneur. Ils espèrent Sa miséricorde et craignent Son châtiment. Le châtiment de ton Seigneur est vraiment redouté. » (al-Isrāʾ, 57)</p>
<p>— en m’aidant de mes acquisitions cognitives.</p>
<p>[Citation coranique (v. 57, de la leçon suivante) restaurée d’après le corpus canonique : l’emplacement imprimé est vide — perte OCR. Elle prépare la doctrine de la <em>wasīla</em> — le crux de la leçon suivante.]</p>"""


def main():
    with open(BOOK, "r", encoding="utf-8") as fh:
        d = json.load(fh)
    hit = 0
    for l in d["lessons"]:
        if l.get("docId") == "13619":
            l["htmlFr"] = HTML_FR
            hit += 1
    if hit != 1:
        raise SystemExit(f"ERREUR: {hit} leçons 13619 trouvées (attendu 1)")
    with open(BOOK, "w", encoding="utf-8") as fh:
        json.dump(d, fh, ensure_ascii=False, indent=1)
    print(f"OK — leçon 13619 upgradée main: FR {len(HTML_FR)} car")


if __name__ == "__main__":
    main()

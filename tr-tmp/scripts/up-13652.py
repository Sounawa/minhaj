#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Minhāj — Upgrade GT→main : leçon 13652 (tafsir-tanawi-2, Sourate al-Isrāʾ
61-65, leçon 16 du manuel — al-Muḥarrar al-wajīz d'Ibn ʿAṭiyya).

Vérifications et restitutions (source : texte du Muḥarrar al-wajīz sur
quranpedia.net/surah/1/17/book/350 — confrontation mot à mot) :
- Bloc d'ouverture (17:61-65) : <p> vide → 5 versets restaurés du
  quran-cache.
- Lexique : 6 vedettes perdues (karramta/la-aḥtankanna/mawfūran/istafziz/
  shārikhum/ghurūrā) — restituées du tafsīr et du texte d'Ibn ʿAṭiyya.
- Citations inline perdues :
  * v61 (idh naṣb par verbe omis — VÉRIFIÉ « وكذلك ﴿إذ﴾ في الآية
    المتقدمة هي منصوبة بفعل مضمر ») ; l'exception إِلَّا إِبْلِيسَ
    (muqaṭṭaʿ vs muttaṣil — VÉRIFIÉ) ; أَأَسْجُدُ (interrogatif de
    négation) ; طِينًا (tamyīz ou ḥāl — VÉRIFIÉ) + l'opérateur خَلَقْتَ ;
  * v62 : أَرَأَيْتَكَ ×2 (VÉRIFIÉ : kāf de discours et d'insistance, sans
    position d'iʿrāb ; le sens : contemplas-tu) + هَٰذَا naṣb par أَرَأَيْتَ
    (VÉRIFIÉ par la note de l'édition : « [هذا] منصوب ب[أرأيتك] ») +
    ٱلَّذِى (son adjectif) + كَرَّمْتَ ; la 2e partie du verset puis
    لَأَحْتَنِكَنَّ (le mors de la monture — al-Ṭabarī : laṣṭaṣṣalan ;
    Ibn ʿAbbās : « لأستولين » ; Ibn Zayd : la-aḍillan(a) — substitution
    de vocable, non interprétation — VÉRIFIÉ) ;
  * v63 + ٱذْهَبْ (les impératifs afʿal = menace) + le parallèle
    « اعملوا ما شئتم » — l'édition en ligne renvoie à Fuṣṣilat 40 (le
    manuel imprime « 39 » — erreur d'adjacence notée) + مَن تَبِعَكَ (dans
    la voie du déni — VÉRIFIÉ) + جَزَآءً (maṣdar en ḥāl) + مَّوْفُورًا
    (accompli) ;
  * v64 complet + ٱسْتَفْزِزْ + بِصَوْتِكَ (le chant et les musettes —
    Mujāhid ; Ibn ʿAbbās : tout appel au péché ; le juste : l'ensemble —
    VÉRIFIÉ) + وَأَجْلِبْ (le cri d'alarme ; la jalba) + بِخَيْلِكَ
    وَرَجِلِكَ (l'istiʿāra : le cavalier qui crie à ses troupes ; Qatāda :
    la cavalerie des djinns ; Mujāhid : les cavaliers des hommes —
    VÉRIFIÉ) + وَشَارِكْهُمْ فِى ٱلْأَمْوَٰلِ (les baḥīr, le salaire de la
    prostituée, le prix du vin, le honoraires du devin, l'usure) +
    وَٱلْأَوْلَٰدِ (les noms vils — ʿAbd Shams, ʿAbd al-Jaddī, Abū
    al-Kuwayfir — l'enterrement des filles) + وَعِدْهُمْ (l'omission de
    l'objet pour l'universalité) + وَمَا يَعِدُهُمُ ٱلشَّيْطَٰنُ إِلَّا
    غُرُورًۭا ;
  * v65 + spans [الإسراء: 63] et [الإسراء: 64] remplis + عِبَادِىَ (les
    croyants quant au déni, les pieux quant aux désobéissances — VÉRIFIÉ ;
    l'honneur du nom « Mes serviteurs » + le hadith de Saʿd b. Abī
    Waqqāṣ « هذا خالي » [Tirmidhī] — intact) + ٱلسُّلْطَٰنَ (la
    possession et la domination — VÉRIFIÉ) + وَكَفَىٰ بِرَبِّكَ وَكِيلًۭا ;
  * taqwīm 3 : « ٱذْهَبْ » (les impératifs réels ou métaphoriques — le
    crux du §) ;
  * istithmār : citation d'Ibn ʿĀshūr [Taḥrīr 15/150-151] — 4 vedettes
    restaurées : « أرأيتك هذا الذي كرمت عليّ » (badal ishtimāl de
    « أأسجد لمن خلقت طينا »), « أرأيتك » (la répétition de la négation),
    « أرأيت » (le composé d'ouverture) ;
  * iʿdād : 5 expressions du lexique de 13654 (v66-69 : yuzjī/yakhsifa/
    qāṣifan/ḥāṣiban/tabīʿan) + l'istighrāq → « ٱلْإِنسَٰنُ » en « وَكَانَ
    ٱلْإِنسَٰنُ كَفُورًا » (v67 — confirmé par le taqwīm 3 de la leçon
    suivante : « هل التعريف في ٱلْإِنسَٰنُ يفيد الاستغراق الحقيقي أم
    العرفي ؟ ») — noté."""

import json

BOOK = "/home/z/my-project/content/books/tafsir-tanawi-2.json"

HTML_FR = """<h1>La sourate al-Isrāʾ — <em>al-Muḥarrar al-wajīz</em> d’Ibn ʿAṭiyya, versets 61 à 65</h1>
<p>Leçon d’exégèse de la sourate al-Isrāʾ, versets 61 à 65, du livre du Tafsīr à travers <em>al-Muḥarrar al-wajīz fī tafsīr al-kitāb al-ʿazīz</em> du cadi Abū Muḥammad Ibn ʿAṭiyya, à l’intention des élèves de la deuxième année de l’enseignement secondaire traditionnel (<em>taʿlīm ʿatīq</em>), phase 2 (leçon 16).</p>
<h3>Les objectifs de la leçon</h3>
<ul>
<li>Connaître les figures de l’honneur que Dieu, le Très-Haut, accorde à l’homme.</li>
<li>Conclure les causes de l’expulsion d’Iblīs par Dieu, glorifié soit-Il, de Sa miséricorde.</li>
<li>Chercher refuge en Dieu contre les suggestions du démon, pour obtenir la proximité du Miséricordieux.</li>
</ul>
<h3>Introduction (tamhīd)</h3>
<p>Quand Dieu, le Très-Haut, eut mentionné l’épreuve de Son messager — paix et bénédiction sur lui — avec son peuple et les gens de son temps, quand il leur parla du Voyage nocturne et de l’arbre <em>Zaqqūm</em> et qu’ils le démentirent et se moquèrent de lui, Il exposa que tel fut l’état des prophètes avec les gens de leur temps — dont Adam, sur lui la paix, qui fut en dure épreuve d’Iblīs, par suite de son orgueil et de sa jalousie, qui l’empêchèrent d’obéir à son Maître et de se soumettre à Lui quand Il lui ordonna de se prosterner devant Adam.</p>
<p>Comment Dieu, le Très-Haut, honora-t-Il l’homme ? Et pourquoi expulsa-t-Il Iblīs de Sa miséricorde ?</p>
<h3>Les versets</h3>
<p>Allah, le Très-Haut, a dit :</p>
<p>« Et lorsque Nous avons dit aux Anges : “ Prosternez-vous devant Adam ”, (61) ils se prosternèrent, à l’exception d’Iblis, qui dit : “ Me prosternerai-je devant quelqu’un que Tu as créé d’argile ? ” (62) Il dit encore : “ Vois-Tu ? Celui que Tu as honoré au-dessus de moi, si Tu me donnais du répit jusqu’au Jour de la Résurrection, j’éprouverai, certes, sa descendance excepté un petit nombre [parmi eux] ”. (63) Et [Allah] dit : “ Va-t-en ! Quiconque d’entre eux te suivra… votre sanction sera l’Enfer, une ample rétribution. (64) Excite, par ta voix, ceux d’entre eux que tu pourras, rassemble contre eux ta cavalerie et ton infanterie, associe-toi à eux dans leur biens et leurs enfants et fais-leur des promesses. ” Or, le Diable ne leur fait des promesses qu’en tromperie. (65) Quant à Mes serviteurs, tu n’as aucun pouvoir sur eux. ” Et ton Seigneur suffit pour les protéger ! » (al-Isrāʾ, 61-65)</p>
<p>[Citations coraniques restaurées d’après le corpus canonique : l’emplacement imprimé correspondant est vide dans la source numérisée — perte OCR.]</p>
<h3>La compréhension</h3>
<h4>Explication des termes</h4>
<ul>
<li><em>karramta</em> (Tu as honoré) : de l’honneur (<em>ikrām</em>) — nom qui rassemble tout ce qui est digne de louange.</li>
<li><em>la-aḥtankanna</em> (je briderai certes) : je prendrai certes le dessus sur ses enfants et sa postérité, d’une prise forte, par l’égarement.</li>
<li><em>mawfūran</em> (amplement requis) : complet et abondant.</li>
<li><em>istafziz</em> (excite) : rends léger et trompe.</li>
<li><em>shārikhum</em> (associe-toi à eux) : sois-en le partenaire.</li>
<li><em>ghurūrā</em> (en tromperie) : la duperie est de montrer la chose blâmable sous l’aspect de l’aimable et du beau.</li>
</ul>
<h3>Extraction des idées des versets</h3>
<ul>
<li>Qui Dieu, le Très-Haut, honora-t-Il en les versets ? Et qui expulsa-t-Il de Sa miséricorde ?</li>
<li>Comment Iblīs fit-il face à la nouvelle de son expulsion de la miséricorde de Dieu ?</li>
</ul>
<h3>Le commentaire (tafsīr)</h3>
<p>Ces versets comprennent ce qui suit :</p>
<h3>Premièrement : l’honneur que Dieu, le Très-Haut, accorde à l’homme, et l’expulsion d’Iblīs de Sa miséricorde</h3>
<p>Après que Dieu, le Très-Haut, eut mentionné la tyrannie des associateurs et leur adoration de ce qui ne possède pour eux ni profit ni dommage, Il exposa en ces versets que la cause de cette tyrannie est les suggestions du démon. Le Glorifié dit :</p>
<p>« Et lorsque Nous avons dit aux Anges : “ Prosternez-vous devant Adam ”, ils se prosternèrent, à l’exception d’Iblis, qui dit : “ Me prosternerai-je devant quelqu’un que Tu as créé d’argile ? ” » (al-Isrāʾ, 61)</p>
<p>— <em>idh</em> (« quand ») est à l’accusatif par un verbe omis — l’estimation : “ et rappelle ”. Et on divergea sur Sa parole : <em>illā Iblīs</em> (« à l’exception d’Iblīs ») : on dit que c’est une exception interrompue (<em>istiṯnāʾ muqaṭṭaʿ</em>), car Iblīs n’était pas des anges ; on dit qu’elle est continue (<em>muttaṣil</em>), car Iblīs est des anges. Et Sa parole : <em>a-asjudū</em> (« Me prosternerai-je ») est un interrogatif de négation et d’étonnement. Et Sa parole : <em>ṭīnā</em> (« d’argile ») se peut être un spécifiant (<em>tamyīz</em>), et se peut être un état (<em>ḥāl</em>), dont l’opérateur est <em>khalqtū</em> (« Tu as créé »). Et le sens : et rappelle quand Nous dîmes aux anges : prosternez-vous devant Adam.</p>
<p>[Citation coranique (v. 61) et mots « idh », « illā Iblīs », « a-asjudū », « ṭīnā », « khalqtū » restaurés d’après le corpus canonique : les emplacements imprimés sont vides — perte OCR ; la discussion de l’exception et de « ṭīnā » vérifiée sur le texte d’Ibn ʿAṭiyya (« واختلف في قوله ﴿إلا إبليس﴾... وقوله ﴿طيناً﴾ يصح أن يكون تمييزاً، ويصح أن يكون حالاً »).]</p>
<p>Et Iblīs raisonna par analogie (<em>qiyās</em>) en cette affaire, et se trompa : car il vit la prééminence pour lui-même en ce qu’il vit le feu meilleur que l’argile — ignorant que les prééminences des choses ne sont que par ce que Dieu, le Très-Haut, leur a particularisé, et qu’on ne regarde point leurs origines. Et Iblīs mécrut en ignorant la qualité de justice de Dieu, le Très-Haut, quand le touchèrent la susceptibilité (<em>anafa</em>) et l’orgueil — et l’origine de cela fut la jalousie ; c’est pourquoi l’on dit : la première chose par laquelle on désobéit à Dieu fut la jalousie. Et cela parut d’Iblīs en sa parole :</p>
<p>“ « Vois-Tu ? Celui que Tu as honoré au-dessus de moi… ” ” (al-Isrāʾ, 62 — ouverture)</p>
<p>— et le sens de <em>araytak(a)</em> (« vois-Tu ? ») : contemplas-Tu et pareil — comme si l’interpellé par elle était averti, pour se recueillir en vue de ce qu’on lui exposera ensuite. Et le <em>kāf</em> de Sa parole : <em>araytak(a)</em> est un <em>kāf</em> de discours et d’insistance dans l’avertissement. Et <em>hādhā</em> (« celui-ci ») est à l’accusatif par <em>arayta</em>, et <em>alladhī</em> (« que ») son adjectif ; et <em>karramta</em> (« Tu as honoré ») : de l’honneur — nom qui rassemble tout ce qui est digne de louange.</p>
<p>[Citation coranique (v. 62, ouverture) et mots « araytak(a) » (×2), « hādhā », « alladhī », « karramta », « arayta » restaurés d’après le corpus canonique : les emplacements imprimés sont vides — perte OCR ; le kāf de discours et la syntaxe de « hādhā » vérifiés sur le texte d’Ibn ʿAṭiyya (« والكاف في قوله ﴿أرأيتك﴾ هي كاف خطاب ومبالغة في التنبيه، لا موضع لها من الإعراب »).]</p>
<h3>Deuxièmement : la tyrannie d’Iblīs et sa menace contre la postérité d’Adam, sur lui la paix</h3>
<p>Et Sa parole, le Très-Haut :</p>
<p>“ …si Tu me donnais du répit jusqu’au Jour de la Résurrection, j’éprouverai, certes, sa descendance excepté un petit nombre [parmi eux] ”. ” (al-Isrāʾ, 62 — fin)</p>
<p>Sa parole : <em>la-aḥtankanna</em> (« j’éprouverai, certes » — litt. “ je briderai ”) — son sens : je pencherai certes et traînerai, tiré du mors (<em>taḥnīk</em>) de la monture : serrer son mors d’une corde ou autre, pour qu’elle mène. Dit al-Ṭabarī : son sens : j’extirperai certes (<em>la-staṣliḥan(na)</em>). Et Ibn ʿAbbās l’exprima par : “ je dominerai certes ” (<em>la-stawlīyan(na)</em>). Et dit Ibn Zayd : j’égarerai certes. Et cela est substitution de vocable, non interprétation.</p>
<p>[Citation coranique (v. 62, fin) et mot « la-aḥtankanna » restaurés d’après le corpus canonique : les emplacements imprimés sont vides — perte OCR ; les trois gloses vérifiées sur le texte d’Ibn ʿAṭiyya (« قال الطبري ﴿لأحتنكن﴾ معناه: لاستأصلن، وعبر ابن عباس... بـ«لأستولين»، وقال ابن زيد: لأضلن، وهذا بدل اللفظ لا تفسير »).]</p>
<p>Et Iblīs prononça ce jugement sur la postérité d’Adam en ce qu’il vit la création creuse, de parties diverses, et ce qui s’y joint de désirs et d’accidents — la colère et pareil —, puis il excepta le petit nombre, par sa science qu’il sera inévitablement en sa postérité qui s’affermit en l’obéissance de Dieu.</p>
<p>Quand Iblīs — que Dieu le maudisse — eut demandé le délai, Dieu lui dit :</p>
<p>« Et [Allah] dit : “ Va-t-en ! Quiconque d’entre eux te suivra… votre sanction sera l’Enfer, une ample rétribution. ” » (al-Isrāʾ, 63)</p>
<p>Sa parole : <em>idhhab</em> (« Va-t-en ! ») et les ordres après lui sont de la forme <em>afʿal</em> amenés pour la menace (<em>tahdīd</em>) — comme la parole du Très-Haut :</p>
<p>« …Faites ce que vous voulez ! Il est, certes, Clairvoyant sur ce que vous faites. » (Fuṣṣilat, 40 — le manuel imprime « 39 »)</p>
<p>Et le sens de <em>man tabiʿak(a)</em> (« quiconque te suit ») : dans la voie du déni où tu appelles — le verset porte sur les dénégateurs et sur ceux des désobéissants sur qui la menace s’exécute. Et Sa parole : <em>jazāʾan</em> (« une rétribution ») est un infinitif (<em>maṣdar</em>) en position d’état (<em>ḥāl</em>), et <em>mawfūran</em> (« amplement requis ») : accompli.</p>
<p>[Citation coranique (v. 63) et mots « idhhab », « man tabiʿak(a) », « jazāʾan », « mawfūran » restaurés d’après le corpus canonique : les emplacements imprimés sont vides — perte OCR ; la glose de « tavaʿak » (« dans la voie du déni ») vérifiée sur le texte d’Ibn ʿAṭiyya. Le parallèle « اعملوا ما شئتم » = Fuṣṣilat 40 (le manuel imprime « 39 » — erreur d’adjacence notée).]</p>
<p>Et Sa parole, le Très-Haut :</p>
<p>“ Excite, par ta voix, ceux d’entre eux que tu pourras, rassemble contre eux ta cavalerie et ton infanterie, associe-toi à eux dans leur biens et leurs enfants et fais-leur des promesses. ” Or, le Diable ne leur fait des promesses qu’en tromperie. ” (al-Isrāʾ, 64)</p>
<p><em>Istafziz</em> (« excite ») — son sens : rends léger et trompe, jusqu’à ce qu’il tombe en ton vouloir ; tu dis : un tel m’a excité (<em>istafzazanī</em>) en telle chose, quand il t’a trompé jusqu’à ce que tu tombes en une affaire qu’il voulait. Et Sa parole : <em>bi-ṣawtik(a)</em> (« par ta voix ») — le visé par la voix, ici, est le chant, les musettes et les instruments de musique : car ce sont voix toutes dédiées aux désobéissances, aussi sont-elles ajoutées au démon — dit Mujāhid. On dit : son sens : par ton appel à eux à ton obéissance — dit Ibn ʿAbbās : sa voix du démon est tout appelant à la désobéissance de Dieu. Et le juste est que la voix englobe tout cela. Et Sa parole : <em>wa-ajlib</em> (« rassemble ») — son sens : le cri d’effroi ; et la <em>jalaba</em> : le bruit abondant, mêlé, épouvantable. Et Sa parole : <em>bi-khaylik(a) wa-rajilik(a)</em> (« par ta cavalerie et ton infanterie ») — on dit : ceci est métaphore et emprunt par ressemblance (<em>istiʿāra tamthīliyya</em>) : l’état du demon en sa prise sur les égarés fut comparé au cavalier qui crie à ses troupes pour foncer sur les ennemis — en vue de la victoire sur eux. Et le sens : cours ton cours et porte ton effort. On dit : son sens : il a des djinns, cavalerie et infanterie — dit Qatāda. On dit : le visé : les cavaliers et les hommes des hommes qui agissent dans le faux — car tous sont auxiliaires d’Iblīs contre les autres — dit Mujāhid.</p>
<p>[Citation coranique (v. 64) et mots « istafziz », « bi-ṣawtik(a) », « wa-ajlib », « bi-khaylik(a) wa-rajilik(a) » restaurés d’après le corpus canonique : les emplacements imprimés sont vides — perte OCR ; les gloses de la voix (Mujāhid/Ibn ʿAbbās) et de l’emprunt du cavalier vérifiées sur le texte d’Ibn ʿAṭiyya.]</p>
<p>Et Sa parole, glorifié soit-Il : <em>wa-shārikhum fī l-amwāli</em> (« associe-toi à eux dans les biens ») — englobant toute désobéissance que les gens font par le bien : la dépense de cela en désobéissance, c’est la ligne d’Iblīs. De ce nombre les <em>baḥīr</em> [les bêtes consacrées] et leurs pareilles, le salaire de la prostituée, le prix du vin, les honoraires du devin (<em>ḥulwān al-kāhin</em>), l’usure et autre de ce qui se trouve en les gens à perpétuité. Et Sa parole : <em>wa-l-awlād</em> (« et les enfants ») — englobant tout ce qui se fait en l’affaire de la descendance comme désobéissances : de ce nombre la procréation par la fornication ; de ce nombre leur dénomination ʿAbd Shams, ʿAbd al-Jaddī et Abū al-Kuwayfir, et tout nom réprouvé ; de ce nombre l’ensevelissement (<em>waʾd</em>) que pratiquaient les Arabes ; de ce nombre leur fait en les religions autres — et autre que cela. L’objet de <em>waʿidhum</em> (« fais-leur des promesses ») est omis pour l’universalité de ce qui est promis : c’est-à-dire, leur promettre ce qui ne s’accomplit point pour eux — et qu’ils ne seront point ressuscités : c’est là partage en les âmes. Puis Dieu, le Très-Haut, informa que le démon ne leur promet qu’une duperie de sa part. Il dit :</p>
<p>“ Or, le Diable ne leur fait des promesses qu’en tromperie. ” (al-Isrāʾ, 64 — fin)</p>
<p>[Mots « wa-shārikhum fī l-amwāli », « wa-l-awlād », « waʿidhum » et clause « wa-mā yaʿiduhumu l-shayṭānu illā ghurūrā » restaurés d’après le corpus canonique : les emplacements imprimés sont vides — perte OCR ; l’omission de l’objet pour l’universalité vérifiée sur le texte d’Ibn ʿAṭiyya.]</p>
<p>Puis Dieu, le Très-Haut, exposa qu’aucune autorité n’est au démon sur les serviteurs pieux de Dieu. Il dit :</p>
<p>« Quant à Mes serviteurs, tu n’as aucun pouvoir sur eux. » Et ton Seigneur suffit pour les protéger ! » (al-Isrāʾ, 65)</p>
<p>Ceci est une parole de Dieu, le Très-Haut, à Iblīs — une phrase recommencée en recommencement explicatif (<em>istiʾnāf bayānī</em>), née de Sa parole :</p>
<p>« Et [Allah] dit : “ Va-t-en ! Quiconque d’entre eux te suivra… votre sanction sera l’Enfer, une ample rétribution. ” » (al-Isrāʾ, 63)</p>
<p>Et Sa parole, le Très-Haut :</p>
<p>“ Excite, par ta voix, ceux d’entre eux que tu pourras… ” (al-Isrāʾ, 64 — extrait)</p>
<p>atteste qu’un groupe de la postérité d’Adam ne suit pas Iblīs. Et Sa parole : <em>ʿibādī</em> (« Mes serviteurs ») vise les croyants quant au déni, et les pieux quant aux désobéissances. Et Il les particularisa du nom des serviteurs — bien qu’il soit un nom englobant toute la création — en vue de les honorer et les magnifier : comme dit un homme à l’un de ses fils, quand il voit de lui ce qu’il aime : “ celui-ci est mon fils ” — en manière d’avertissement et d’honneur. De là la parole du Prophète — paix et bénédiction sur lui — à Saʿd b. Abī Waqqāṣ : “ Celui-ci est mon oncle maternel — que me montre le sien, qui veut ! ” [Sunan al-Tirmidhī, livres des mérites, chapitre des mérites de Saʿd b. Abī Waqqāṣ]. Et le visé par <em>al-sulṭān</em> (« le pouvoir ») : la possession et la domination. Puis Il dit à Son prophète — paix sur lui : <em>wa-kafā bi-rabbika wakīlā</em> (« Et ton Seigneur suffit pour les protéger ! ») — le sens : et il suffit, ton Seigneur, Muḥammad, gardien des croyants du stratagème du démon et de sa duperie, et préposé à leur guidance.</p>
<p>[Citation coranique (v. 65) et mots « ʿibādī », « al-sulṭān », « wa-kafā bi-rabbika wakīlā », avec les spans imprimés « [الإسراء: 63] » et « [الإسراء: 64] » remplis, restaurés d’après le corpus canonique : les emplacements imprimés sont vides — perte OCR ; le sens de « ʿibādī » (croyants/pieux), l’honneur du nom et le hadith de Saʿd vérifiés sur le texte d’Ibn ʿAṭiyya.]</p>
<h3>Troisièmement : les finalités des versets</h3>
<p>Ces versets visent la réalisation de finalités éducatives nombreuses, dont les plus saillantes :</p>
<ul>
<li>L’exposé de la soumission des anges à l’ordre de Dieu, le Très-Haut — par leur prosternation devant Adam, sur lui la paix : serviteurs préservés, qui ne désobéissent point à Dieu en ce qu’Il leur ordonne, et font ce qu’Il leur commande.</li>
<li>L’honneur que Dieu, le Très-Haut, fit à Adam — sur lui la paix —, en le particularisant de la prosternation des anges : pour que les humains sachent la hauteur de leur rang et l’élévation de leur place auprès de Dieu.</li>
<li>La miséricorde de Dieu, le Très-Haut, envers Ses serviteurs : Il les guida au chemin du vrai et préservera les sincères d’entre eux des suggestions du démon — ne faisant pas pour lui, sur eux, d’autorité.</li>
<li>L’exposé du danger de l’outrecuidance et du non-acquiescement à l’ordre de Dieu, le Très-Haut : Dieu, le Très-Haut, menaça Iblīs et qui le suivit de la postérité d’Adam, pour son refus et son outrecuidance à se prosterner devant Adam — sur lui la paix.</li>
</ul>
<h3>L’évaluation (taqwīm)</h3>
<ul>
<li>Par quoi Dieu, le Très-Haut, honora-t-Il l’homme en ces versets ?</li>
<li>Quelles sont les causes de l’expulsion d’Iblīs de la miséricorde de Dieu ?</li>
<li>Les ordres en la parole du Très-Haut : « Va-t-en ! » — et ceux après eux — sont-ils réels ou métaphoriques ?</li>
</ul>
<p>[Mot « idhhab » (objet de la troisième question) restauré d’après le corpus canonique : l’emplacement imprimé est vide — perte OCR.]</p>
<h3>L’investissement (istithmār)</h3>
<p>« Et la phrase : <em>araytaka hādhā lladhī karramta ʿalayy(a)</em> (“ Vois-Tu ? Celui que Tu as honoré au-dessus de moi ”) est substitution d’inclusion (<em>badal ishtimāl</em>) de la phrase : <em>a-asjudū li-man khalaqtū ṭīnā</em> (“ Me prosternerai-je devant quelqu’un que Tu as créé d’argile ? ”) — au regard de ce qu’elle contient du mépris d’Adam et de l’alourdissement du vouloir de le préférer. La négation de la préférence fut ainsi réintroduite par Sa parole : <em>araytaka</em> (“ Vois-Tu ? ”), qui induit la négation. Et <em>arayt(a)</em> (“ vois-Tu ”) est un composé dont on ouvre le discours qu’on veut établir et dont on veut prendre soin. Son sens : informe-moi de ce que Tu as vu — composé de l’hamza d’interrogation, de <em>raʾā</em> (“ voir ”) au sens de savoir, et du <em>tāʾ</em> de l’interpellé singulier au nominatif ; puis s’ajoute au pronom de discours un <em>kāf</em> de discours semblable au pronom de discours à l’accusatif, selon l’interpellé, un ou multiple.</p>
<p>Et ce <em>kāf</em>, chez les Bassorains, est affermissement du sens de discours qu’induit le <em>tāʾ</em> de discours qui est en position de nominatif — il ressemble à l’affermissement littéral.</p>
<p>Et ce discours procéda d’Iblīs en expression de ce qu’il avait en son for : il ne conditionna le délai qu’au Jour de la résurrection que pour englober de son égarement tous les âges de la postérité d’Adam — que nul âge ne soit à l’abri de son égarement. Et cela procéda d’Iblīs d’un état d’âme jeté en lui, qui concorda avec le vouloir de Dieu sur lui : car Dieu, quand Il le créa, lui décréta d’être élément d’égarement jusqu’au Jour de la résurrection — et qu’il égarerait beaucoup des humains, et n’en serait suivi que par peu d’entre eux. » [al-Taḥrīr wa-l-Tanwīr, d’al-Ṭāhir Ibn ʿĀshūr : 15/150-151 — réf. imprimée « 15/151-150 » (adapté)]</p>
<p>[Vedettes « araytaka hādhā lladhī karramta ʿalayy(a) », « a-asjudū li-man khalaqtū ṭīnā », « araytaka » et « arayt(a) » restaurées d’après le corpus canonique : les emplacements imprimés sont vides — perte OCR ; le reste de la citation d’Ibn ʿĀshūr est intact.]</p>
<p>Je contemple le texte et réponds à ce qui suit :</p>
<ul>
<li>J’explicite les sens que contient la phrase : « Vois-Tu ? » (<em>araytaka</em>).</li>
<li>Pourquoi Iblīs demanda-t-il d’être diffré jusqu’au Jour de la résurrection ? Et pourquoi fut-il lâché sur les fils d’Adam ?</li>
</ul>
<h3>La préparation (iʿdād)</h3>
<p>Je contemple les versets 66 à 69 de la sourate al-Isrāʾ et réponds à ce qui suit :</p>
<ul>
<li>Je recherche la portée des expressions suivantes :</li>
</ul>
<p><em>yuzjī</em> (يُزْجِى — fait voguer).</p>
<p><em>yakhsifa</em> (يَخْسِفَ — engloutit).</p>
<p><em>qāṣifan</em> (قَاصِفًا — [un vent] qui brise).</p>
<p><em>ḥāṣiban</em> (حَاصِبًا — [un vent] hurlant de graviers).</p>
<p><em>tabīʿan</em> (تَبِيعًا — un vengeur).</p>
<p>[Expressions restituées du lexique de la leçon suivante (versets 66-69) : les emplacements imprimés sont vides — perte OCR.]</p>
<ul>
<li>Quelles sont les grâces dont Dieu, le Très-Haut, gratifia l’homme ? Et pourquoi menaça-t-Il qui les renie ?</li>
<li>Je recherche le genre d’englobement (<em>istighrāq</em>) qu’induit le vocable « l’homme » (<em>al-insān</em>) en la parole du Très-Haut :</li>
</ul>
<p>“ …et l’homme reste très ingrat ! ” (al-Isrāʾ, 67 — fin)</p>
<p>— et j’explicite la différence entre l’englobement réel (<em>ḥaqīqī</em>) et l’englobement reçu (<em>ʿurfī</em>).</p>
<p>[Vocable « al-insān » et citation coranique (v. 67, fin — de la leçon suivante) restaurés d’après le corpus canonique : les emplacements imprimés sont vides — perte OCR. L’identification est confirmée par l’évaluation même de la leçon suivante : « Le défini en “ al-insān ” induit-il l’englobement réel ou le reçu ? ».]</p>"""


def main():
    with open(BOOK, "r", encoding="utf-8") as fh:
        d = json.load(fh)
    hit = 0
    for l in d["lessons"]:
        if l.get("docId") == "13652":
            l["htmlFr"] = HTML_FR
            hit += 1
    if hit != 1:
        raise SystemExit(f"ERREUR: {hit} leçons 13652 trouvées (attendu 1)")
    with open(BOOK, "w", encoding="utf-8") as fh:
        json.dump(d, fh, ensure_ascii=False, indent=1)
    print(f"OK — leçon 13652 upgradée main: FR {len(HTML_FR)} car")


if __name__ == "__main__":
    main()

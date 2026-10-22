#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Minhāj — Upgrade GT→main : leçon 13654 (tafsir-tanawi-2, Sourate al-Isrāʾ
66-69, leçon 17 du manuel — al-Muḥarrar al-wajīz d'Ibn ʿAṭiyya).

Vérifications et restitutions (source : texte du Muḥarrar al-wajīz sur
quranpedia.net/surah/1/17/book/350 — confrontation mot à mot) :
- Bloc d'ouverture (17:66-69) : <p> vide → 4 versets restaurés du
  quran-cache.
- Lexique : 5 vedettes perdues (yuzjī/yakhsifa/qāṣifan/ḥāṣiban/tabīʿan) —
  restituées du tafsīr et du texte d'Ibn ʿAṭiyya.
- Citations inline perdues :
  * v66 + yuzjī (la marche lourde ; les chameaux faibles ; la marchandise
    conduite) + le parallèle « ألم تر أن الله يزجي سحابا » — **Nūr 43
    VÉRIFIÉ** (« ومنه قوله تعالى ﴿ألم تر أن الله يزجي سحاباً﴾ » — le
    manuel imprime « [النور: 42] », erreur d'adjacence notée) + al-Baḥr
    (le pluriel) + « البحر » (l'eau abondante) + « لتبتغوا من فضله »
    (englobant le commerce et la quête du salaire) + la citation d'Abū
    Ḥayyān hmm — [Anwār al-tanzīl d'al-Bayḍāwī 3/261] ;
  * v67 + « الضر » (l'englobant : la peur du naufrage, l'entrave à la
    marche) + « ضل » (perte et disparition — l'expression du mépris des
    prétendus dieux) + le sens (les idoles n'agissent pas dans les
    grandes détresses) + « أعرضتم » + « الإنسان » (le genre, l'englobement
    — VÉRIFIÉ) + « كفورا » ;
  * v68 + « أفأمنتم » (l'hamza de négation) + « يخسف » + « الحاصب » (le
    grain de grêle ; celui du peuple de Loth) + « الوكيل » + les lectures :
    Nāfiʿ/ʿĀṣim/Ibn ʿĀmir/Ḥamza/Kisāʾī « يخسف » au yāʾ (= Dieu engloutit)
    — **VÉRIFIÉ** (« وكذلك «يرسل» و«يعيد» و«يرسل» و«يغرق» ») + Abū
    Jaʿfar/Mujāhid « تغرقكم » au tāʾ (le vent) ;
  * v69 + « أم » (interrompue = bal + hamza) + « القاصف » + « تارة »
    (tārāt/tīr) + « بما كفرتم » (le bāʾ causal, le mā nominale) +
    « التبيع » (le vengeur) + le hadith de Muslim « إذا أتبع أحدكم على
    مليء فليتبع » (intact) ;
  * taqwīm 3 : « الإنسان » (l'englobement réel ou reçu — le crux du §) ;
  * istithmār : citation d'Ibn ʿĀshūr [Taḥrīr 15/161] — le mulāʾim/munāfir
    (intact) + **Fuṣṣilat 50 restauré** (فبعد ضراء مسسته... فإن الإنسان
    كفور — le parallèle du remerciement manqué) + « أفأمنتم » (v68) +
    **Ibrāhīm 7 restauré** (لئن شكرتم لأزيدنكم) ;
  * iʿdād : 4 expressions du lexique de 13659 (v70-72 : karramnā/
    bi-imāmihim/fatīlan/aḍalla sabīlā) + le bāʾ de « يوم ندعو كل أناس
    بإمامهم » (v71 — confirmé par la discussion même de la leçon suivante
    sur le taʿalluq du bāʾ) — noté.
- Objectif 3 du source : coquille CMS « أن تمثل » — lu « أن أتمثل »."""

import json

BOOK = "/home/z/my-project/content/books/tafsir-tanawi-2.json"

HTML_FR = """<h1>La sourate al-Isrāʾ — <em>al-Muḥarrar al-wajīz</em> d’Ibn ʿAṭiyya, versets 66 à 69</h1>
<p>Leçon d’exégèse de la sourate al-Isrāʾ, versets 66 à 69, du livre du Tafsīr à travers <em>al-Muḥarrar al-wajīz fī tafsīr al-kitāb al-ʿazīz</em> du cadi Abū Muḥammad Ibn ʿAṭiyya, à l’intention des élèves de la deuxième année de l’enseignement secondaire traditionnel (<em>taʿlīm ʿatīq</em>), phase 2 (leçon 17).</p>
<h3>Les objectifs de la leçon</h3>
<ul>
<li>Connaître la finalité de l’énumération par Dieu, le Très-Haut, de Ses grâces envers l’homme.</li>
<li>Conclure le visé de la menace de Dieu, glorifié soit-Il, à l’homme renieur.</li>
<li>Incarner les grâces de Dieu envers moi, pour Le remercier d’elles.</li>
</ul>
<h3>Introduction (tamhīd)</h3>
<p>Quand Dieu, le Très-Haut, eut mentionné, aux versets précédents, l’histoire d’Iblīs, le Glorifié exposa en ces versets quelques-unes de Ses grâces envers l’homme, et établit des preuves claires de Sa puissance et de Son immense autorité ; puis Il exposa que l’homme est pétri de répondre aux grâces de son Seigneur par la négation et le reniement : quand un mal le touche, il invoque son Seigneur et se réfugie en Lui ; et quand Il écarte de lui son mal, il se plonge dans les désirs et oublie l’obéissance de son Seigneur.</p>
<p>Quelles sont les grâces dont Dieu, glorifié soit-Il, gratifia l’homme ? Et quelle est la fin de qui répond à ces grâces par reniement et négation ?</p>
<h3>Les versets</h3>
<p>Allah, le Très-Haut, a dit :</p>
<p>« Votre Seigneur est Celui qui fait voguer le vaisseau pour vous en mer, (66) afin que vous alliez à la recherche de quelque grâce de Sa part. Certes Il est Miséricordieux envers vous. (67) Et quand le mal vous touche en mer, ceux que vous invoquiez en dehors de Lui se perdent. Puis, quand Il vous sauve et vous ramène à terre, vous vous détournez. L’homme reste très ingrat ! (68) Etes-vous à l’abri de ce qu’Il vous fasse engloutir par un pan de terre, ou qu’Il envoie contre vous un ouragan [avec pluie en pierres] et que vous ne trouverez alors aucun protecteur ? (69) Ou êtes-vous à l’abri de ce qu’Il vous y ramène (en mer) une autre fois, qu’Il déchaîne contre vous un de ces vents à tout casser, puis qu’Il vous fasse noyer à cause de votre mécréance ? Et alors, vous ne trouverez pour vous, contre Nous, aucun secours à en tirer. » (al-Isrāʾ, 66-69)</p>
<p>[Citations coraniques restaurées d’après le corpus canonique : l’emplacement imprimé correspondant est vide dans la source numérisée — perte OCR.]</p>
<h3>La compréhension</h3>
<h4>Explication des termes</h4>
<ul>
<li><em>yuzjī</em> (fait voguer) : conduit d’une conduite à la marche lourde.</li>
<li><em>yakhsifa</em> (engloutit) : fait disparaître en la terre.</li>
<li><em>qāṣifan</em> (un [vent] qui brise) : un vent violent.</li>
<li><em>ḥāṣiban</em> (un [vent] de graviers) : un vent au bruit violent.</li>
<li><em>tabīʿan</em> (un secours) : un défenseur qui poursuit une vengeance.</li>
</ul>
<h3>Extraction des idées des versets</h3>
<ul>
<li>Quelles sont les grâces de Dieu, le Très-Haut, envers l’homme que contiennent les versets ?</li>
<li>Qu’est-ce que l’homme renia-t-il en ces versets ?</li>
</ul>
<h3>Le commentaire (tafsīr)</h3>
<p>Ces versets comprennent ce qui suit :</p>
<h3>Premièrement : les grâces de Dieu, le Très-Haut, envers l’homme en la mer</h3>
<p>Quand Dieu, le Très-Haut, eut fait courir le discours des versets précédents sur l’avertissement et la mise en garde, Il apporta en ces versets une preuve de la justesse de cela. Le Glorifié dit :</p>
<p>« Votre Seigneur est Celui qui fait voguer le vaisseau pour vous en mer, afin que vous alliez à la recherche de quelque grâce de Sa part. Certes Il est Miséricordieux envers vous. » (al-Isrāʾ, 66)</p>
<p>[Citation coranique (v. 66) restaurée d’après le corpus canonique : l’emplacement imprimé est vide — perte OCR.]</p>
<p>Sa parole : <em>yuzjī</em> (« fait voguer ») — conduire d’une conduite à la marche lourde, soit par faiblesse, soit par lourdeur de charge, soit autre : les chameaux faibles sont conduits (<em>tuzjā</em>) — et de là la parole du Très-Haut :</p>
<p>« N’as-tu pas vu qu’Allah pousse les nuages ? » (an-Nūr, 43 — le manuel imprime « 42 »)</p>
<p>— et la marchandise conduite (<em>al-biḍāʿa al-muzjāt</em>) est celle qui requiert, pour sa déficience, d’être conduite par intercession et poussée par aide, vers qui la reçoit. Et le conduire du vaisseau : le faire aller d’un lieu à un lieu par le vent doux et les avirons ; et <em>al-fulk</em> (« le vaisseau ») est ici pluriel, non singulier. Et <em>al-baḥr</em> (« la mer ») : l’eau abondante, douce ou salée — et le nom prévalut sur la saline, la connue. Et Sa parole, le Très-Haut : <em>li-tabtaghū min faḍlih</em> (« afin que vous alliez à la recherche de quelque grâce de Sa part ») est un vocable englobant le commerce et la quête du salaire, en pèlerinage et pareil. Et ce verset est un arrêt sur les bienfaits de Dieu et Sa faveur sur Ses serviteurs : “ Il vous a préparé ce dont vous avez besoin, et vous a facilité ce qui se rendait difficile de ses moyens ”. [Anwār al-tanzīl wa-asrār al-taʾwīl, d’al-Bayḍāwī : 3/261 — réf. imprimée « 261/3 », ordre inversé]</p>
<p>[Mots « yuzjī », « al-baḥr », « li-tabtaghū min faḍlih » et citation d’an-Nūr 43 (span imprimé « [النور: 42] ») restaurés d’après le corpus canonique : les emplacements imprimés sont vides — perte OCR ; le parallèle du nuage poussé vérifié sur le texte d’Ibn ʿAṭiyya (« ومنه قوله تعالى ﴿ألم تر أن الله يزجي سحاباً﴾ » — Nūr 43). Citation d’al-Bayḍāwī intacte.]</p>
<p>Et après que Dieu, le Très-Haut, eut accablé les associateurs de la preuve de Son droit, le Très-Haut, à la divinité, Il y fit suivre l’exposé de leur aveu de Son unicité, glorifié soit-Il, en la disposition, au temps de leur détresse — puis S’étonna, glorifié soit-Il, de leur contradiction d’eux-mêmes à leur sauvetage et au départ de leur détresse. Le Glorifié dit :</p>
<p>« Et quand le mal vous touche en mer, ceux que vous invoquiez en dehors de Lui se perdent. » (al-Isrāʾ, 67 — ouverture)</p>
<p>— le <em>ḍurr</em> (« le mal ») : vocable englobant la peur du naufrage et l’entrave à la marche ; et le plus épouvantable de ses états : son trouble et son houle. Et Sa parole : <em>ḍalla</em> (« se perdent ») — son sens : perte et disparition : expression de mépris de qui prétend un dieu en dehors de Dieu. Et le sens en ce verset : les dénégateurs ne croient de leurs idoles qu’elles sont intercessrices et ont une faveur — et chacun d’eux sait, de science innée dont il ne peut se défendre, que les idoles n’ont point d’action dans les détresses immenses : Dieu les arrêta, en cela, sur l’état de la mer.</p>
<p>[Citation coranique (v. 67, ouverture) et mots « al-ḍurr », « ḍalla » restaurés d’après le corpus canonique : les emplacements imprimés sont vides — perte OCR ; les gloses vérifiées sur le texte d’Ibn ʿAṭiyya.]</p>
<p>Puis Dieu, le Très-Haut, mentionna leur état quand Il découvrit d’eux ces détresses, les sauva, les soulagea et les fit parvenir au rivage — [et leur] détournement de Lui et leur reniement de la grâce du sauvetage de la noyade. Il dit :</p>
<p>“ …Puis, quand Il vous sauve et vous ramène à terre, vous vous détournez. L’homme reste très ingrat ! ” (al-Isrāʾ, 67 — fin)</p>
<p>Sa parole : <em>aʿraḍtum</em> (« vous vous détournez ») — c’est-à-dire : vous ne méditâtes point l’œuvre de Dieu au temps de votre besoin de Lui. Et <em>al-insān</em> (« l’homme »), ici, est pour le genre — englobant : car chacun ne s’acquitte guère de la gratitude de Dieu, le Très-Haut, comme il se doit. Et Sa parole : <em>kafūrā</em> (« très ingrat ») — c’est-à-dire : renieur des grâces.</p>
<p>[Citation coranique (v. 67, fin) et mots « aʿraḍtum », « al-insān », « kafūrā » restaurés d’après le corpus canonique : les emplacements imprimés sont vides — perte OCR ; l’englobement de « al-insān » vérifié sur le texte d’Ibn ʿAṭiyya (« و ﴿الإنسان﴾ هنا للجنس، وكل أحد لا يكاد يؤدي شكر الله تعالى كما يجب »).]</p>
<h3>Deuxièmement : le reniement par l’homme des grâces de Dieu</h3>
<p>Après que Dieu, glorifié soit-Il, eut exposé la faiblesse des intelligences des dénégateurs — arrivés au rivage et sauvés de l’horreur de la mer, ils retournent à leur déni, en sûreté du châtiment de Dieu —, Il les effraya de Sa puissance immense. Le Glorifié dit :</p>
<p>« Etes-vous à l’abri de ce qu’Il vous fasse engloutir par un pan de terre, ou qu’Il envoie contre vous un ouragan [avec pluie en pierres] et que vous ne trouverez alors aucun protecteur ? » (al-Isrāʾ, 68)</p>
<p>L’hamza en <em>a-fa-amintum</em> (« Etes-vous à l’abri ? ») est de négation. Et <em>yakhsifa</em> (« engloutir ») : faire disparaître en la terre. Le <em>ḥāṣib</em> (« l’ouragan de pierres ») : l’averse lançant grêle et pierres et pareil — dont le <em>ḥāṣib</em> qui frappa le peuple de Loth ; et le <em>ḥaṣb</em> : le lancer du gravier, qui est les petites pierres. Et le <em>wakīl</em> (« protecteur ») : le préposé aux affaires.</p>
<p>[Citation coranique (v. 68) et mots « a-fa-amintum », « yakhsifa », « al-ḥāṣib », « al-wakīl » restaurés d’après le corpus canonique : les emplacements imprimés sont vides — perte OCR ; les gloses vérifiées sur le texte d’Ibn ʿAṭiyya.]</p>
<p>Et le sens : êtes-vous à l’abri, vous les détournants, oublieux de la dureté, quand vous fûtes à l’aisance, que Dieu fasse engloutir en vous votre place de la terre ferme — quand vous êtes en la poigne de la Puissance, en mer comme à terre ?</p>
<p>Et Nāfiʿ, ʿĀṣim, Ibn ʿĀmir, Ḥamza et al-Kisāʾī lurent <em>yakhsifa</em> au <em>yāʾ</em> — au sens : Dieu fait engloutir — de même <em>yursila</em> (« envoie ») et <em>yughrīkum</em> (« fasse noyer ») ; et Abū Jaʿfar et Mujāhid lurent <em>tughrikum</em> (« [le vent] vous noie ») au <em>tāʾ</em> de discours, rapporté au vent.</p>
<p>[Mots « yakhsifa », « yursila », « yughrikum » et lecture « tughrikum » restitués d’après le corpus canonique et le texte d’Ibn ʿAṭiyya (« وقرأ نافع وعاصم... «يخسف» بالياء على معنى يخسف الله، وكذلك «يرسل» و«يعيد» و«يرسل» و«يغرق»... وقرأ أبو جعفر ومجاهد «تغرقكم» بالتاء أي الريح ») : les emplacements imprimés sont vides — perte OCR.]</p>
<p>Et Sa parole, le Très-Haut :</p>
<p>« Ou êtes-vous à l’abri de ce qu’Il vous y ramène (en mer) une autre fois, qu’Il déchaîne contre vous un de ces vents à tout casser, puis qu’Il vous fasse noyer à cause de votre mécréance ? Et alors, vous ne trouverez pour vous, contre Nous, aucun secours à en tirer. » (al-Isrāʾ, 69)</p>
<p>L’<em>am</em> (« ou ») en Sa parole est interrompue (<em>munqaṭiʿa</em>), estimée par “ <em>bal</em> et l’hamza ” : elle est de la transition (<em>iḍrāb intiqālī</em>) — c’est-à-dire : “ plutôt : êtes-vous à l’abri ? ”. Et le <em>qāṣif</em> (« qui brise ») : ce qui rompt tout ce qu’il rencontre et le brise. Et <em>tāratan</em> (« une fois ») — son pluriel : <em>tārāt</em> et <em>tīr</em> —, son sens : une autre fois. Et le <em>bāʾ</em> en <em>bi-mā kafartum</em> (« à cause de votre mécréance ») est causal, et <em>mā</em> nominale — c’est-à-dire : par cause de votre déni antérieur de vous. Le <em>tabīʿ</em> (« secours ») : le défenseur qui poursuit vengeance ou dette. Et de ce vocable, la parole du Prophète — paix sur lui : “ Quand l’un de vous fait suivre [une créance] à un solvable, qu’il la fasse suivre ”. [Ṣaḥīḥ Muslim, livre de l’arrosage, chapitre de l’interdit de faire traîner le solvable…] — le sens : vous ne trouverez pas qui fasse suivre Notre fait à votre égard et poursuive votre secours.</p>
<p>[Citation coranique (v. 69) et mots « am », « al-qāṣif », « tāratan », « bi-mā kafartum », « al-tabīʿ » restaurés d’après le corpus canonique : les emplacements imprimés sont vides — perte OCR ; les gloses et le hadith vérifiés — hadith de Muslim intact.]</p>
<h3>Troisièmement : les finalités des versets</h3>
<p>Ces versets orientent vers la réalisation de finalités éducatives, qu’on peut résumer ainsi :</p>
<ul>
<li>L’affirmation par Dieu, glorifié soit-Il, de Son unicité et de Son droit à l’adoration sans autre que Lui : le visé suprême du noble Coran est d’établir les preuves de l’unicité.</li>
<li>Le rappel aux serviteurs que Dieu est Celui qui garantit la sûreté de l’homme et son intégrité en la terre ferme et la mer, quand il se réfugie en Lui par l’imploration et l’invocation, sans autre que Lui.</li>
<li>L’exposé de la faveur de Dieu, le Très-Haut, et de Sa largesse envers Ses serviteurs : Il ne les châtie point de ce dont Il châtia ceux avant eux.</li>
</ul>
<h3>L’évaluation (taqwīm)</h3>
<ul>
<li>Pourquoi Dieu, le Très-Haut, gratifia-t-Il l’homme de Ses grâces et bienfaits ?</li>
<li>J’explicite le visé de la menace de Dieu, le Très-Haut, à l’homme renieur.</li>
<li>Le défini en « l’homme » (<em>al-insān</em>) induit-il l’englobement réel (<em>ḥaqīqī</em>) ou le reçu (<em>ʿurfī</em>) ? Et cela a-t-il un effet sur le sens du verset ?</li>
</ul>
<p>[Vocable « al-insān » (objet de la troisième question) restauré d’après le corpus canonique : l’emplacement imprimé est vide — perte OCR.]</p>
<h3>L’investissement (istithmār)</h3>
<p>« Et comme la gratitude de la grâce est suspendue au rappel de la grâce, ses occupations, qui l’éloignent du rappel des grâces passées, furent couvrantes sur elles — et parce que les perçus des sens sont, d’entre eux, le conforme (<em>mulāʾim</em>) à l’âme — et c’est le prévalent —, et d’entre eux le répugnant (<em>munāfir</em>) à elle : l’homme, quand il perçoit le conforme, ne sent point de valeur en lui, tant se répète sa venue qu’il devint habitude — et il oublia le bien qui est en lui ; mais quand il perçoit le répugnant, il se rappelle l’absence du conforme : clame et impatience. Et c’est le sens de la parole du Très-Haut :</p>
<p>« Et si nous lui faisons goûter une miséricorde de Notre part, après qu’une détresse l’ait touché, il dit certainement : “ Cela m’est dû ! Et je ne pense pas que l’Heure se lèvera [un jour]. ” » (Fuṣṣilat, 50 — extrait)</p>
<p>Et c’est pourquoi dirent les sages : la santé (<em>ʿāfiya</em>) est une couronne sur les têtes des bien-portants, que ne voient que les malades. Et cette considération est celle à quoi alluda le verset [al-Isrāʾ, 67], avec celui après lui, qui est : <em>a-fa-amintum</em> (« Etes-vous à l’abri ? ») [al-Isrāʾ, 68]. Et pour cela, des convenances de l’âme en la Loi est de lui rappeler les grâces de Dieu. Dit le Très-Haut :</p>
<p>« Et lorsque votre Seigneur proclama : “ Si vous êtes reconnaissants, très certainement J’augmenterai [Mes bienfaits] pour vous. Mais si vous êtes ingrats, Mon châtiment sera terrible ”. » (Ibrāhīm, 7)</p>
<p>— pour que le rappel de la grâce tienne lieu de son pacte. » [al-Taḥrīr wa-l-Tanwīr, d’al-Ṭāhir Ibn ʿĀshūr : 15/161 — réf. imprimée « 15/161 » (adapté)]</p>
<p>[Citations coraniques (Fuṣṣilat 50 — réf. imprimée « فصلت الآية 50 » ; Ibrāhīm 7 — span imprimé « [إبراهيم: 7] ») et mot « a-fa-amintum » (v. 68 — span imprimé « [الإسراء: 68] ») restaurés d’après le corpus canonique : les emplacements imprimés sont vides — perte OCR ; le reste de la citation d’Ibn ʿĀshūr est intact.]</p>
<h4>Je contemple le texte et réponds à ce qui suit :</h4>
<ul>
<li>Qu’entend-on par “ le conforme ” (<em>mulāʾim</em>) et “ le répugnant ” (<em>munāfir</em>) en le texte ? Et quel est leur rapport à la gratitude des grâces ?</li>
<li>Quel est l’effet du rappel des grâces de Dieu, le Très-Haut, sur la purification de l’âme ?</li>
</ul>
<h3>La préparation (iʿdād)</h3>
<p>Je contemple les versets 70 à 72 de la sourate al-Isrāʾ et réponds à ce qui suit :</p>
<ul>
<li>Je recherche la portée des expressions suivantes :</li>
</ul>
<p><em>karramnā</em> (كَرَّمْنَا — Nous avons honoré).</p>
<p><em>bi-imāmihim</em> (بِإِمَٰمِهِمْ — par leur guide).</p>
<p><em>fatīlā</em> (فَتِيلًا — d’un futfīl).</p>
<p><em>aḍalla sabīlā</em> (أَضَلَّ سَبِيلًا — plus égaré en voie).</p>
<p>[Expressions restituées du lexique de la leçon suivante (versets 70-72) : les emplacements imprimés sont vides — perte OCR.]</p>
<ul>
<li>Comment Dieu, le Très-Haut, honora-t-Il l’homme ? Et pourquoi le préféra-t-Il à l’autre ?</li>
<li>À quoi se rattache le <em>bāʾ</em> en la parole du Très-Haut :</li>
</ul>
<p>« Le jour où Nous appellerons chaque groupement d’hommes par leur chef » (al-Isrāʾ, 71)</p>
<p>— et quel est le profit de déterminer ce rattachement en l’éclaircissement du sens du verset ?</p>
<p>[Citation coranique (v. 71, de la leçon suivante) restaurée d’après le corpus canonique : l’emplacement imprimé est vide — perte OCR. Elle prépare la discussion du <em>bāʾ</em> de « bi-imāmihim » (rattaché à “ Nous appellerons ” : par le nom de leur guide ; ou : avec leur guide) — le crux grammatical de la leçon suivante.]</p>"""


def main():
    with open(BOOK, "r", encoding="utf-8") as fh:
        d = json.load(fh)
    hit = 0
    for l in d["lessons"]:
        if l.get("docId") == "13654":
            l["htmlFr"] = HTML_FR
            hit += 1
    if hit != 1:
        raise SystemExit(f"ERREUR: {hit} leçons 13654 trouvées (attendu 1)")
    with open(BOOK, "w", encoding="utf-8") as fh:
        json.dump(d, fh, ensure_ascii=False, indent=1)
    print(f"OK — leçon 13654 upgradée main: FR {len(HTML_FR)} car")


if __name__ == "__main__":
    main()

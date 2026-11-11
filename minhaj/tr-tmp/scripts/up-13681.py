#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Minhāj — Upgrade GT→main : leçon 13681 (tafsir-tanawi-2, Sourate al-Isrāʾ
82-85, leçon 21 du manuel — al-Muḥarrar al-wajīz d'Ibn ʿAṭiyya).

Vérifications et restitutions (source : texte du Muḥarrar al-wajīz sur
quranpedia.net/surah/1/17/book/350 — confrontation mot à mot) :
- Bloc d'ouverture (17:82-85) : <p> vide → 4 versets restaurés du
  quran-cache.
- Lexique : 3 vedettes perdues (aʿraḍa wa-naʾā bi-jānibihi/yaʾūsan/
  shākilatahi) — restituées du tafsīr.
- Citations inline perdues :
  * v82 + « من القرآن » et « من » (×2 : le début de la fin, le genre —
    VÉRIFIÉ ; la partition défendue par Ibn ʿAṭiyya : la descente
    elle-même est par parts) + « رحمة » + l'emprunt de la guérison (l'effacement
    du doute, la découverte du voile du cœur — ou la guérison des maladies
    par les incantations) + la citation d'al-Rāzī [Mafātīḥ 21/390] intacte
    (le cercle : l'audition accroît la rage → les actes faux → les caractères
    corrompus) ;
  * v83 + la particularisation de « l'homme » (les dénégateurs — comme « pas
    de bien dans les amis » : la généralité d'exagération) + l'hypothèse du
    genre + le hadith « فأعرض فأعرض الله عنه » + « أعرض » et « نئا بجانبه »
    (l'emprunt : il fait les actes du détourné éloigné) ;
  * les lectures naʾā/nāʾa (Ibn ʿĀmir seul « وناء » = se dressa — ou
    l'inversion de l'hamza, langue comme رأى/راء) + le vers du tireur
    (« حتى إذا ما التأمت مفاصله ** وناء في شق الشمال كاهله » — intact) +
    la distinction d'Ibn ʿAṭiyya (nāʾa = le particularisme et
    l'isolement ; naʾā = l'éloignement) ;
  * v84 + « قل » (l'ordre au Prophète) + « شاكلته » (Mujāhid : sa nature /
    sa hardiesse ; Ibn ʿAbbās : son côté ; Qatāda : son côté et ce qu'il
    vise ; Ibn Zayd : sa religion — Ibn ʿAbbās/Qatāda préférés) + la glose
    de Bayḍāwī [3/265] « أسد طريقا وأبين منهجا » ;
  * v85 + le span [الإسراء: 84] rempli + les deux histoires (les Juifs
    d'Ibn Masʿūd — « demande-lui de l'Esprit : s'il répond, il n'est pas
    prophète » ; l'appui sur la palme, la pause de la révélation ;
    Quraysh/al-Naḍr b. al-Ḥārith et ʿUqba — les trois questions (les gens
    de la Caverne, Dhū l-Qarnayn, l'Esprit) + « غدا أخبركم » sans « si
    Dieu veut » — quinze jours de retenue de la révélation) — intacts ;
  * la dispute de l'Esprit (le jumhūr : l'esprit des vivants — le genre,
    le plus juste ; Qatāda : Jibrīl ; une frange : Jésus ; une frange : le
    Coran) + « من أمر ربي » (le genre des affaires de Dieu — l'ajout de
    créature à Créateur ; ou le maṣdar : Il commanda qu'il fût et il fut) ;
  * les lectures « وما أوتوا » (Ibn Masʿūd/al-Aʿmash) / « وما أوتيتم »
    (jumhūr) + les destinataires (les demandeurs / les Juifs / le monde
    entier — le juste) + « قل الروح من أمر ربي » (le commandement du dire à
    tout le monde) ;
  * taqwīm intact ; istithmār : Ibn ʿAjība [3/227] intact + v83 restauré
    (le <p> vide + le span [الإسراء 83]) ;
  * iʿdād : 4 expressions du lexique de 13688 (v86-89 : ẓahīran/wa-la-qad
    ṣarrafnā/min kulli mathalin/kafūran) + les trois anecdotes d'éloquence
    arabe (intactes : le Farazdaq ; « عز فحكم فقطع » ; le Bédouin et
    al-Aṣmaʿī) + l'exception → v86-87 « إلا رحمة من ربك » (confirmée par
    la discussion de la leçon suivante : منقطع) — noté."""

import json

BOOK = "/home/z/my-project/content/books/tafsir-tanawi-2.json"

HTML_FR = """<h1>La sourate al-Isrāʾ — <em>al-Muḥarrar al-wajīz</em> d’Ibn ʿAṭiyya, versets 82 à 85</h1>
<p>Leçon d’exégèse de la sourate al-Isrāʾ, versets 82 à 85, du livre du Tafsīr à travers <em>al-Muḥarrar al-wajīz fī tafsīr al-kitāb al-ʿazīz</em> du cadi Abū Muḥammad Ibn ʿAṭiyya, à l’intention des élèves de la deuxième année de l’enseignement secondaire traditionnel (<em>taʿlīm ʿatīq</em>), phase 2 (leçon 21).</p>
<h3>Les objectifs de la leçon</h3>
<ul>
<li>Connaître l’effet du noble Coran sur les croyants et les autres.</li>
<li>Conclure des versets ce qui atteste l’étendue de la science de Dieu, le Très-Haut, et la limite de la science de l’homme.</li>
<li>Méditer le noble Coran, pour purifier mon âme et la nettoyer des contrariants.</li>
</ul>
<h3>Introduction (tamhīd)</h3>
<p>Quand Dieu, le Très-Haut, eut détaillé aux versets précédents les divinités, les prophéties, le rassemblement, la résurrection, l’établissement du décret et de la destinée, et ordonné la prière en avertissant de ses secrets — Il affirma en ces versets que le noble Coran est guérison et miséricorde pour les gens de la foi, et perte pour les gens de l’injustice et de la tyrannie ; et que l’homme renieur méconnaît les grâces de Dieu et ne reconnaît point le bienfait, désespère et prend de mauvais augures au mal ; puis Dieu, le Très-Haut, exposa que la réalité de l’Esprit relève de Lui seul — preuve de l’étendue de Sa science, glorifié soit-Il, et de la limite de la science de l’homme, qui se resserre aux sensibles, hors les intelligibles cachés.</p>
<p>En quoi consiste la guérison du noble Coran ? Et qu’est-ce qui atteste l’étendue de la science de Dieu, le Très-Haut ?</p>
<h3>Les versets</h3>
<p>Allah, le Très-Haut, a dit :</p>
<p>« Nous faisons descendre du Coran, (82) ce qui est une guérison et une miséricorde pour les croyants. Cependant, cela ne fait qu’accroître la perdition des injustes. (83) Et quand Nous comblons l’homme de bienfaits, il se détourne et se replie sur lui-même ; et quand un mal le touche, le voilà profondément désespéré. (84) Dis : “ Chacun agit selon sa méthode, alors que votre Seigneur connaît mieux qui suit la meilleure voie. (85) Et ils t’interrogent au sujet de l’âme. — Dis : “ L’âme relève de l’Ordre de mon Seigneur. ” Et on ne vous a donné que peu de connaissance. ” » (al-Isrāʾ, 82-85)</p>
<p>[Citations coraniques restaurées d’après le corpus canonique : l’emplacement imprimé correspondant est vide dans la source numérisée — perte OCR.]</p>
<h3>La compréhension</h3>
<h4>Explication des termes</h4>
<ul>
<li><em>aʿraḍa wa-naʾā bi-jānibihi</em> (il se détourne et se replie) : il tourna le dos, s’en alla et s’éloigna.</li>
<li><em>yaʾūsan</em> (profondément désespéré) : en dure désespérance de la miséricorde de Dieu.</li>
<li><em>ʿalā shākilatahi</em> (selon sa méthode) : selon sa voie et son école, qui ressemble à son état en la guidée ou l’égarement.</li>
</ul>
<h3>Extraction des idées des versets</h3>
<ul>
<li>Quel est l’effet du noble Coran sur les croyants et les autres ?</li>
<li>De quoi Dieu, le Très-Haut, s’est-Il réservé la connaissance en ces versets ?</li>
</ul>
<h3>Le commentaire (tafsīr)</h3>
<p>Ces versets comprennent ce qui suit :</p>
<h3>Premièrement : le noble Coran, guérison et miséricorde pour les gens de la foi</h3>
<p>Le Très-Haut a dit :</p>
<p>« Nous faisons descendre du Coran, ce qui est une guérison et une miséricorde pour les croyants. » (al-Isrāʾ, 82)</p>
<p>Sa parole : <em>min al-Qurʾān</em> (« du Coran ») — il est valable que <em>min</em> soit du commencement de la fin, et valable qu’elle soit pour l’exposition du genre — comme s’Il avait dit : “ Nous faisons descendre ce en quoi il y a guérison, du Coran. ” Et un parti des interprètes refusa que <em>min</em> fût de partition, car il s’ensuivrait qu’une part de lui n’a point de guérison. Dit Ibn ʿAṭiyya : cela ne lui s’ensuit pas — il est valable qu’elle soit de partition, en ce que sa descente, elle, se fait par parts : comme s’Il avait dit : “ Nous faisons descendre du Coran, chose à chose, ce en quoi il y a tout entier guérison. ”</p>
<p>[Citation coranique (v. 82) et mots « min al-Qurʾān », « min » (×2) restaurés d’après le corpus canonique : les emplacements imprimés sont vides — perte OCR ; les trois valeurs de « min » vérifiées sur le texte d’Ibn ʿAṭiyya (« يصح أن تكون ﴿من﴾ لابتداء الغاية، ويصح أن تكون لبيان الجنس »).]</p>
<p>Et l’emprunt de la guérison au Coran est selon l’effacement qu’il fait du doute et la découverte qu’il fait du voile du cœur, pour comprendre les merveilles et les choses qui attestent Dieu, le Très-Haut, et établissent Sa Loi ; il se peut que par “ la guérison ” soit visé son profit des maladies, par les incantations et les amulettes et pareil. Et qu’il soit <em>miséricorde</em> est apparent.</p>
<p>[Mot « raḥmatan » restauré d’après le corpus canonique : l’emplacement imprimé est vide — perte OCR ; l’emprunt de la guérison vérifié sur le texte d’Ibn ʿAṭiyya.]</p>
<p>Puis, quand Dieu, le Très-Haut, eut exposé que le Coran est guérison et miséricorde pour les croyants, Il exposa qu’il est cause de perte et d’égarement au droit des injustes associateurs. Le Glorifié dit :</p>
<p>« Cependant, cela ne fait qu’accroître la perdition des injustes. » (al-Isrāʾ, 82 — fin)</p>
<p>— le sens : il est sur eux aveuglement, car ils se détournent, comme l’état de qui ne comprend point et n’est point instruit. “ Et cela ne fut que parce que l’audition du Coran accroît en eux rage, colère, rancune et jalousie. Et ces caractères blâmables les appellent aux œuvres vaines, et accroissent la force de ces caractères corrompus en les substances de leurs âmes ; puis le caractère vil de l’âme ne cesse de porter aux œuvres corrompues, et la venue de ces œuvres fortifie ces caractères : par cette voie, le Coran devient cause de l’accroissement de ces associateurs égarés en les degrés de la honte, de l’égarement, de la corruption et du châtiment. ” [Mafātīḥ al-ghayb, d’al-Rāzī : 21/390 — réf. imprimée « 21/390 », conforme]</p>
<p>[Citation coranique (v. 82, fin) restaurée d’après le corpus canonique : l’emplacement imprimé est vide — perte OCR ; citation d’al-Rāzī intégrale et conforme.]</p>
<p>Puis le Glorifié mentionna que l’amour du bas-monde, le désir d’amasser le bien, et la croyance que cela vient du gain de l’homme, sont cause de la chute de ces associateurs en l’égarement et la perte. Le Très-Haut dit :</p>
<p>« Et quand Nous comblons l’homme de bienfaits, il se détourne et se replie sur lui-même ; et quand un mal le touche, le voilà profondément désespéré. » (al-Isrāʾ, 83)</p>
<p>— il n’est pas visé par “ l’homme ” en ce verset l’englobement : n’en est visé qu’une part — les dénégateurs. Il en est comme tu dis en colère : “ pas de bien dans les amis, point de loyauté dans les gens ” — tu englobes par exagération, et ton visé est la part. Et cela est selon la mention des injustes, et de la “ perte ” au verset précédent : la mention des dénégateurs s’y rattache.</p>
<p>[Citation coranique (v. 83) restaurée d’après le corpus canonique : l’emplacement imprimé est vide — perte OCR.]</p>
<p>Il se peut que “ l’homme ” en ce verset soit général au genre — au sens que ce caractère blâmable est en son naturel : le dénégateur excelle au détournement, et le désobéissant prend sa part de lui. Et le Messager de Dieu — paix et bénédiction sur lui — dit d’un croyant : “ il se détourna, et Dieu se détourna de lui. ” Et le sens de <em>aʿraḍ(a)</em> (“ il se détourne ”) : il Nous tourna son côté. Et <em>naʾā bi-jānibihi</em> (“ se replie sur lui-même ”) : il s’éloigna — et ceci est emprunt : car il fait les actes du détourné éloigné, en son renoncement à la foi en Dieu et à la gratitude de Ses grâces sur lui.</p>
<p>[Mots « aʿraḍ(a) » et « naʾā bi-jānibihi » restaurés d’après le corpus canonique : les emplacements imprimés sont vides — perte OCR ; hadith du croyant intact.]</p>
<p>Et Ibn ʿĀmir seul lut <em>wa-nāʾ(a)</em>, dont le sens : il se dressa — c’est-à-dire, s’éloignant : tel un parti. Et un autre dit : c’est l’inversion de l’hamza après l’alif de <em>naʾā</em> lui-même — langue comme <em>raʾā/rāʾa</em>. Et de ce vocable, la parole du poète en la description d’un tireur :</p>
<p>“ Puis, quand ses articulations se ressoudèrent / il se dressa sur le flanc gauche, son épaule. ”</p>
<p>— son sens : il se dressa, accoudé sur sa gauche. Et ce qui est chez Ibn ʿAṭiyya : <em>nāʾa</em> et <em>naʾā</em> sont deux verbes distincts. <em>Nāʾa bi-jānibihi</em> est expression du particularisme et de l’isolement ; et <em>naʾā</em>, expression de l’éloignement et de la séparation.</p>
<p>[Lectures « wa-nāʾ(a) » et vers du tireur intacts (traduits) ; la distinction d’Ibn ʿAṭiyya conforme.]</p>
<p>Puis Il décrivit les dénégateurs : quand les touche un mal — maladie, ou sinistre en un bien ou autre — ils désespèrent, du fait qu’ils ne croient point en Dieu et n’attendent rien du cours de Ses décrets. Le Très-Haut dit :</p>
<p>“ …et quand un mal le touche, le voilà profondément désespéré. ” (al-Isrāʾ, 83 — fin)</p>
<p>[Clause « wa-idhā massahu l-sharru kāna yaʾūsā » restaurée d’après le corpus canonique : l’emplacement imprimé est vide — perte OCR.]</p>
<p>Puis le Puissant, le Majestueux, dit :</p>
<p>« Dis : “ Chacun agit selon sa méthode, alors que votre Seigneur connaît mieux qui suit la meilleure voie. ” » (al-Isrāʾ, 84)</p>
<p>— l’ordre de <em>qul</em> (“ Dis ”) est au Prophète — paix et bénédiction sur lui — : c’est-à-dire : dis, Muḥammad. Dit Mujāhid : <em>shākilatahi</em> (“ sa méthode ”) — son sens : selon sa nature. Il dit aussi : son sens : selon sa hardiesse. Et dit Ibn ʿAbbās : son sens : selon son côté. Et dit Qatāda : son sens : selon son côté, et selon ce qu’il vise. Et dit Ibn Zayd : son sens : selon sa religion. Et le plus fort de ces expressions est le dire d’Ibn ʿAbbās et Qatāda.</p>
<p>Et ce verset atteste de l’évidence que “ l’homme ” — premièrement — n’y fut pas visé par l’englobement : les dénégateurs sont sur ces caractères, et les croyants sur leur contraire — et chacun d’eux œuvre selon ce qui lui sied.</p>
<p>Et Sa parole :</p>
<p>“ …alors que votre Seigneur connaît mieux qui suit la meilleure voie. ” (al-Isrāʾ, 84 — fin)</p>
<p>— c’est-à-dire : “ le plus ferme en chemin, le plus clair en route ”. [Anwār al-tanzīl wa-asrār al-taʾwīl, d’al-Bayḍāwī : 3/265 — réf. imprimée « 3/265 », conforme]</p>
<p>[Citations coraniques (v. 84 ; v. 84, fin) et mots « qul », « shākilatahi » restaurés d’après le corpus canonique : les emplacements imprimés sont vides — perte OCR ; citation d’al-Bayḍāwī intacte.]</p>
<h3>Deuxièmement : Ce dont Il s’est réservé la science — la réalité de l’Esprit</h3>
<p>Quand Dieu, le Très-Haut, eut clos le verset précédent par Sa parole :</p>
<p>« Dis : “ Chacun agit selon sa méthode, alors que votre Seigneur connaît mieux qui suit la meilleure voie. ” » (al-Isrāʾ, 84 — requoté)</p>
<p>— et qu’aux esprits est un rôle dans les actes advenant de l’homme —, Dieu, le Très-Haut, exposa l’Esprit, et fit savoir qu’Il s’est réservé, glorifié soit-Il, la science de sa réalité. Le Puissant, le Majestueux, dit :</p>
<p>« Et ils t’interrogent au sujet de l’âme. — Dis : “ L’âme relève de l’Ordre de mon Seigneur. ” Et on ne vous a donné que peu de connaissance. » (al-Isrāʾ, 85)</p>
<p>Le pronom de <em>yasʾalūnak(a)</em> (“ ils t’interrogent ”) — on dit qu’il est pour les Juifs, et que le verset est médinois. ʿAbd Allāh b. Masʿūd rapporta qu’il était avec le Messager de Dieu — paix et bénédiction sur lui —, et qu’ils passèrent auprès d’une culture à Médine — on rapporte : auprès de ruines — où était un groupe de Juifs. Certains d’entre eux dirent : “ Demandez-lui de l’Esprit : s’il y répond, vous saurez qu’il n’est pas prophète ” — car il était chez eux, en la Torah, que l’Esprit est de ce dont Dieu s’est réservé seul la science, dont Il n’informe aucun de Ses serviteurs. Dit Ibn Masʿūd : et certains dirent : “ ne lui demandez pas, de peur qu’il n’y apporte une chose qui vous déplaise ” — voulant, et Dieu sait le mieux, qu’il ne l’exposera point, et que la preuve de sa prophétie se fortifiera sur eux. Il dit : on la lui demanda ; le Messager de Dieu — paix et bénédiction sur lui — s’arrêta, appuyé sur une palme, et je pensai qu’il lui était révélé ; puis il leur récita le verset.</p>
<p>On dit : le verset est mecquois, et le pronom pour Quraysh — car ils dirent : “ Nous interrogerons sur Muḥammad les gens du Livre, des Juifs ”, et envoyèrent à Médine al-Naḍr b. al-Ḥārith et ʿUqba b. Abī Muʿayṭ. Les Juifs leur dirent : “ Mettez-le à l’épreuve par trois questions : demandez-lui des gens de la Caverne, de Dhū l-Qarnayn, et de l’Esprit — s’il expose les trois, c’est un menteur ; s’il se tait sur l’Esprit, c’est un prophète. ” Quraysh l’interrogèrent de l’Esprit — et il fut rapporté que le Prophète — paix et bénédiction sur lui — leur dit : “ Demain je vous l’annonce ”, sans dire “ si Dieu veut ” : la révélation se retint sur lui quinze jours, en reproche de sa promesse sans exception ; puis ce verset descendit.</p>
<p>[Citations coraniques (v. 84 requoté — span imprimé « [الإسراء: 84] » ; v. 85) et mot « yasʾalūnak(a) » restaurés d’après le corpus canonique : les emplacements imprimés sont vides — perte OCR ; les deux histoires (Ibn Masʿūd, al-Naḍr b. al-Ḥārith) intégralement intactes.]</p>
<p>Et les gens divergèrent sur l’Esprit demandé : quel esprit est-il ?</p>
<p>Dit le <em>jumhūr</em> : la question porta sur l’esprit qui est dans les corps vivants — qu’est-il ? L’Esprit est, sur ce, un nom de genre : et c’est le juste — la chose problématique, qui n’a point d’explication.</p>
<p>Et dit Qatāda : l’Esprit demandé est Jibrīl — dit-il, et Ibn ʿAbbās le taisait. Et une frange dit : Jésus, fils de Marie. Et une frange dit : l’Esprit est le Coran. Et tout cela sont dires exposés — le premier est le plus apparent et le plus juste.</p>
<p>Et Sa parole : <em>min amri rabbī</em> (“ relève de l’Ordre de mon Seigneur ”) comporte deux interprétations :</p>
<ul>
<li>La première : que “ l’Ordre ” (<em>amr</em>) soit un nom de genre des affaires — c’est-à-dire : l’Esprit est du nombre des affaires de Dieu dont Il s’est réservé la science : c’est l’ajout de créature à Créateur.</li>
<li>La seconde : qu’il soit un infinitif (<em>maṣdar</em>) de <em>amara yaʾmuru</em> (“ ordonner ”) — c’est-à-dire : l’Esprit est de ce qu’Il ordonna d’un ordre d’être — et il fut.</li>
</ul>
<p>Et Ibn Masʿūd et al-Aʿmash lurent <em>wa-mā ūtū</em> (“ et il ne leur fut donné ”) — Ibn Masʿūd la rapporta du Prophète. Et le <em>jumhūr</em> lut <em>wa-mā ūtītum</em> (“ et il ne vous fut donné ”). Et on divergea sur qui fut interpellé : une frange dit : les seuls demandeurs ; un parti dit : les Juifs en leur totalité — et sur ce, la lecture d’Ibn Masʿūd ; une frange dit : le monde entier — et c’est le juste : car la parole de Dieu à lui :</p>
<p>“ Dis : “ L’âme relève de l’Ordre de mon Seigneur. ” ” (al-Isrāʾ, 85 — extrait requoté)</p>
<p>n’est qu’un commandement du dire à tout le monde entier — car telles sont toutes Ses paroles ; et sur cela le verset s’achève en l’interpellation de tous. Il se peut aussi que ce soit une interpellation de Dieu au Prophète — paix et bénédiction sur lui — et à tous les gens. Et ce qui est chez tous les gens de science se décrit par la petitesse, à l’ajouter à la science de Dieu, Puissant et Majestueux, qui embrasse toute chose.</p>
<p>[Mots « min amri rabbī » (×2), « wa-mā ūtū », « wa-mā ūtītum », « quli l-rūḥu min amri rabbī » (requoté) restaurés d’après le corpus canonique : les emplacements imprimés sont vides — perte OCR ; les deux interprétations de « amr » et les lectures vérifiées sur le texte d’Ibn ʿAṭiyya.]</p>
<h3>Troisièmement : les finalités des versets</h3>
<p>Ces versets visent la réalisation de finalités éducatives nombreuses, dont :</p>
<ul>
<li>La grâce de Dieu, le Très-Haut, envers l’homme, par le noble Coran — guérison des maladies des cœurs et miséricorde pour les croyants.</li>
<li>L’orientation de Dieu, le Très-Haut, à Son messager — paix et bénédiction sur lui — et aux croyants, vers le procédé de se dégager du débat vain et du dialogue infécond : Il les guida au détournement de cela, et à rapporter à Dieu, le Très-Haut, la science de cela.</li>
<li>L’affirmation que les gens ne marchent que selon leurs penchants et leurs natures, issues de leur éducation et leurs mœurs — et qu’il est de leur nature, le plus souvent, d’outrecuider et s’éloigner du vrai quand ils obtiennent un bien et une grâce, et de désespérer et dénier quand les touche un mal et une rigueur.</li>
</ul>
<h3>L’évaluation (taqwīm)</h3>
<ul>
<li>Pourquoi le noble Coran est-il guérison et miséricorde pour les croyants, et perte pour les injustes associateurs ?</li>
<li>Quelle est la sagesse du détournement de Dieu, le Très-Haut, de répondre aux associateurs sur la réalité de l’Esprit ?</li>
<li>Comment ces versets agissent-ils sur la santé psychique des musulmans ?</li>
</ul>
<h3>L’investissement (istithmār)</h3>
<p>Dit Ibn ʿAjība — Dieu lui fasse miséricorde —, en [son commentaire de] la parole du Très-Haut :</p>
<p>« Et quand Nous comblons l’homme de bienfaits, il se détourne et se replie sur lui-même ; et quand un mal le touche, le voilà profondément désespéré. » (al-Isrāʾ, 83 — requoté)</p>
<p>« Il convient au croyant soucieux de lui-même de pousser au fond le regard en la parole de son Maître : s’il Le trouve louant un peuple pour une œuvre, qu’il s’empresse de la faire ; ou pour un caractère, qu’il s’empresse de s’en parer ; et s’il Le trouve blâmant un peuple pour cause d’une œuvre, qu’il s’en éloigne de tout son effort ; ou pour un caractère, qu’il s’en purifie absolument. Le Vrai, le Très-Haut, blâma ici qui fut insensible à la grâce et négligent à se tenir en sa gratitude — et qui s’affola au sinistre et désespéra de son départ. Le croyant ne sera point au rebours de cela : si l’atteint un sinistre ou une épreuve, il implore son Maître et espère Sa faveur et Son don ; et si l’atteint une grâce, de ce monde ou de la religion, il en double la gratitude. » [al-Baḥr al-madīd fī tafsīr al-Qurʾān al-majīd, d’Ibn ʿAjība : 3/227 — réf. imprimée « 3/227 », conforme]</p>
<p>[Citation coranique (v. 83 — le <em>p</em> vide + le span imprimé « [الإسراء 83] ») restaurée d’après le corpus canonique : l’emplacement imprimé est vide — perte OCR ; citation d’Ibn ʿAjība intégrale et conforme.]</p>
<p>Je contemple le texte et réponds à ce qui suit :</p>
<ul>
<li>Comment le croyant traite-t-il ce que Dieu aime et ce qu’Il blâme ?</li>
<li>J’expose, à travers le texte, ce qui m’aide à remercier Dieu, le Très-Haut, et à purifier mon âme.</li>
</ul>
<h3>La préparation (iʿdād)</h3>
<p>Je contemple les versets 86 à 89 de la sourate al-Isrāʾ et réponds à ce qui suit :</p>
<p>Je recherche la portée des expressions suivantes :</p>
<p><em>ẓahīran</em> (ظَهِيرًا — auxiliaires).</p>
<p><em>wa-la-qad ṣarrafnā</em> (وَلَقَدْ صَرَّفْنَا — Nous avons exposé).</p>
<p><em>min kulli mathalin</em> (مِن كُلِّ مَثَلٍۢ — de toute sorte).</p>
<p><em>kafūran</em> (كَفُورًا — renieur).</p>
<p>[Expressions restituées du lexique de la leçon suivante (versets 86-89) : les emplacements imprimés sont vides — perte OCR.]</p>
<p>— J’expose ce dont Ibn ʿAṭiyya — Dieu lui fasse miséricorde — prit à témoin de l’éloquence des Arabes et leur sagacité, en ce qui suit :</p>
<ul>
<li>La compréhension par al-Farazdaq du poème de Jarīr en le poème de Dhū l-Rumma : “ يعد الناسبون إلى تميم ”.</li>
<li>La parole du Bédouin : “ Puissant — il jugea, il tranche. ”</li>
<li>La parole du Bédouin à al-Aṣmaʿī : “ Qui rend le généreux le plus besoin de jurer ? ”</li>
</ul>
<p>— L’exception en la parole du Glorifié :</p>
<p>“ …Et si Nous voulions, Nous emporterions certes ce que Nous t’avons révélé… (86) …sauf comme miséricorde de ton Seigneur ” (al-Isrāʾ, 86-87 — extrait)</p>
<p>— est-elle interrompue (<em>munqaṭiʿ</em>) ou continue (<em>muttaṣil</em>) ? Et quelle est la différence des deux ? Et cela a-t-il un effet sur l’interprétation du verset ?</p>
<p>[Citations coraniques (v. 86-87 — de la leçon suivante) restaurées d’après le corpus canonique : l’emplacement imprimé est vide — perte OCR. Elle prépare la divergence sur l’exception de « illā raḥmatan min rabbik(a) » — interrompue selon la leçon suivante (“ mais : une miséricorde de ton Seigneur la retient sur toi ”) — le crux grammatical de la leçon suivante. Les trois anecdotes d’éloquence sont intactes dans la source et préparées par l’introduction d’Ibn ʿAṭiyya à la sourate.]</p>"""


def main():
    with open(BOOK, "r", encoding="utf-8") as fh:
        d = json.load(fh)
    hit = 0
    for l in d["lessons"]:
        if l.get("docId") == "13681":
            l["htmlFr"] = HTML_FR
            hit += 1
    if hit != 1:
        raise SystemExit(f"ERREUR: {hit} leçons 13681 trouvées (attendu 1)")
    with open(BOOK, "w", encoding="utf-8") as fh:
        json.dump(d, fh, ensure_ascii=False, indent=1)
    print(f"OK — leçon 13681 upgradée main: FR {len(HTML_FR)} car")


if __name__ == "__main__":
    main()

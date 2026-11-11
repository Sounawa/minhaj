#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Minhāj — Upgrade GT→main : leçon 13620 (tafsir-tanawi-2, Sourate al-Isrāʾ
56-60, leçon 15 du manuel — al-Muḥarrar al-wajīz d'Ibn ʿAṭiyya).

Vérifications et restitutions (source : texte du Muḥarrar al-wajīz sur
quranpedia.net/surah/1/17/book/350 — confrontation mot à mot) :
- Bloc d'ouverture (17:56-60) : seul le titre survit — 5 versets restaurés
  du quran-cache.
- Lexique : 4 vedettes perdues (yabtaghūna/al-wasīla/maḥdhūran/masṭūran) —
  restituées du tafsīr et du texte d'Ibn ʿAṭiyya (« والوسيلة هي القربة »).
- Citations inline perdues :
  * v56 (les ʿabida : démons de Khuzāʿa, ʿUzayr/Christ/sa mère, anges,
    astres — Ibn Masʿūd/Ibn ʿAbbās) ;
  * mot « يدعون » avec l'iʿrāb d'Abū Ḥayyān (pronom caché = المفعول
    Premier, second objet omis : « زعمتموهم آلهة ») [Baḥr 7/70] ;
  * v57 : « أولئك » (les adorés — mubtada' de khabar « يبتغون ») et les
    pronoms (« يدعون » = les dénégateurs ; « يبتغون » = les adorés) —
    VÉRIFIÉ sur l'original ; « الوسيلة » + vers d'ʿAntara + hadith de la
    wasīla ; « أيهم »/« أقرب » ; la lecture d'Ibn Fūrak (retour aux
    prophètes du v. 55 : « يدعون » = prêcher, pronoms de « يدعون » et
    « يبتغون ») — VÉRIFIÉ ;
  * v58 : « من » (pour la détermination du genre — VÉRIFIÉ ; Abū Ḥayyān
    s'interroge en note sur cette glose), « مهلكوها » (le pronom = la
    ville, et en son sein les habitants), « معذبوها » (élision d'un
    complément : on ne châtie que les habitants), « في الكتاب » (le décret
    antérieur, la Plume sur la Table gardée), « مسطورا » (écrit) ;
  * v59a (« وما منعنا أن نرسل بالآيات إلا أن كذب بها الأولون » — la
    première en position d'accusatif, la seconde de nominatif — VÉRIFIÉ) ;
    v59b (« وآتينَا ثمود الناقة مبصرة فظلموا بها » — l'argument de
    Thamûd) ; « مبصرة » (sur le mode de la relation : « avec elle une
    vue ») + span [الإسراء: 12] rempli de « آية النهار مبصرة » (VÉRIFIÉ :
    le parallèle du v. 12) ; les lectures mubṣira/mabṣara (al-Zajjāj,
    Qatāda) + le vers d'ʿAntara (intact) ; « فظلموا بها » ;
    v59c (« وما نرسل بالآيات إلا تخويفا ») ;
  * v60a (« وإذ قلنا لك إن ربك أحاط بالناس » ×2 — VÉRIFIÉ : l'original
    le requote pour le sens « en leur égarement et leur guidée ») ;
    v60b (« وما جعلنا الرؤيا التي أريناك إلا فتنة للناس ») ; la shajara :
    « الملعونة » + « في القرآن » (l'affermissement d'Ibn ʿAṭiyya —
    VÉRIFIÉ) + la coordination de « الشجرة الملعونة في القرآن » sur
    « الرؤيا » (VÉRIFIÉ : « معطوفة على قوله ﴿الرؤيا﴾ ») ; v60c (« ونخوفهم
    فما يزيدهم إلا طغيانا كبيرا ») ;
  * taqwīm 2 : la question du pronom → v57 (l'objet de la divergence
    jumhūr/Ibn Fūrak) ;
  * istithmār : la citation d'al-Alūsī est INTACTE ; span [الأنفال: 23]
    restauré (وَلَوْ عَلِمَ اللهُ فِيهِمْ خَيْرًا لَّأَسْمَعَهُمْ) ;
  * iʿdād : 6 expressions du lexique de 13652 (v61-65 : karramta/
    la-aḥtankanna/mawfūran/istafziz/shārikhum/ghurūrā) + citation → v64a
    (l'istiʿāra tamthīliyya du cavalier — crux rhétorique de la leçon
    suivante) — noté.
- Histoires intactes : al-Ṣafā d'or + les montagnes + « بل تستأني بهم يا
  رب » ; le tremblement de terre de Kūfa (Ibn Masʿūd : « إن ربكم
  يستعتبكم فأعتبوه ») ; l'éclipse (« فافزعوا إلى الصلاة ») ; la caravane
  de deux mois ; la Ḥudaybiya (Ibn ʿAbbās)."""

import json

BOOK = "/home/z/my-project/content/books/tafsir-tanawi-2.json"

HTML_FR = """<h1>La sourate al-Isrāʾ — <em>al-Muḥarrar al-wajīz</em> d’Ibn ʿAṭiyya, versets 56 à 60</h1>
<p>Leçon d’exégèse de la sourate al-Isrāʾ, versets 56 à 60, du livre du Tafsīr à travers <em>al-Muḥarrar al-wajīz fī tafsīr al-kitāb al-ʿazīz</em> du cadi Abū Muḥammad Ibn ʿAṭiyya, à l’intention des élèves de la deuxième année de l’enseignement secondaire traditionnel (<em>taʿlīm ʿatīq</em>), phase 2 (leçon 15).</p>
<h3>Les objectifs de la leçon</h3>
<ul>
<li>Connaître ce que sont les adorés dont Dieu, glorifié soit-Il, interdit l’adoration.</li>
<li>Conclure la sagesse pour laquelle Dieu, le Très-Haut, ne particularisa point Quraysh d’un de Ses signes.</li>
<li>Incarner les principes de l’unicité vers lesquels les versets orientent.</li>
</ul>
<h3>Introduction (tamhīd)</h3>
<p>Dieu, glorifié soit-Il, expose en ces versets ce qu’adoraient les associateurs en dehors de Dieu, puis établit que la propagation de l’injustice est cause de l’extirpation des communautés, et que ce qui empêche de particulariser Quraysh par les miracles est le beliement, par les communautés avant eux, de leurs pareilles ; puis Il rassura Son messager — paix et bénédiction sur lui — : Il le protège de son peuple, le secourra et le soutiendra, en Lui exposant qu’Il a fait l’affaire du Voyage nocturne (<em>isrāʾ</em>) et de l’arbre <em>Zaqqūm</em> une épreuve pour les gens et une mise à l’épreuve.</p>
<p>Qui sont ceux dont Dieu, le Très-Haut, interdit l’adoration ? Et quelle est la sagesse du non-accord à Quraysh d’un signe miraculeux, à la différence des communautés antérieures ?</p>
<h3>Les versets</h3>
<p>Allah, le Très-Haut, a dit :</p>
<p>« Dis : “ Invoquez ceux que vous prétendez, (être des divinités) en dehors de Lui. Ils ne possèdent ni le moyen de dissiper votre malheur ni de le détourner. ” (56) Ceux qu’ils invoquent, cherchent [eux-mêmes], à qui mieux, le moyen de se rapprocher le plus de leur Seigneur. Ils espèrent Sa miséricorde et craignent Son châtiment. Le châtiment de ton Seigneur est vraiment redouté. (57) Il n’est point de cité [injuste] que Nous ne fassions périr avant le Jour de la Résurrection, ou que Nous ne punissions d’un dur châtiment. Cela est bien tracé dans le Livre [des décrets immuables]. (58) Rien ne Nous empêche d’envoyer les miracles, si ce n’est que les Anciens les avaient traités de mensonges. Nous avions apporté aux Thamûd la chamelle qui était un miracle visible : mais ils lui firent du tort. En outre, Nous n’envoyons de miracles qu’à titre de menace. (59) Et lorsque Nous te disions que ton Seigneur cerne tous les gens (par Sa puissance et Son savoir). Quant à la vision que Nous t’avions montrée, Nous ne l’avons faite que pour éprouver les gens, tout comme l’arbre maudit mentionné dans le Coran. Nous les menaçons, mais cela ne fait qu’augmenter leur grande transgression. (60) » (al-Isrāʾ, 56-60)</p>
<p>[Citations coraniques restaurées d’après le corpus canonique : l’emplacement imprimé correspondant est vide dans la source numérisée — perte OCR.]</p>
<h3>La compréhension</h3>
<h4>Explication des termes</h4>
<ul>
<li><em>yabtaghūna</em> (ils cherchent) : ils demandent.</li>
<li><em>al-wasīla</em> (le moyen d’approche) : la proximité, et le moyen d’atteindre le but.</li>
<li><em>maḥdhūran</em> (redouté) : dont il est un devoir de se garder et de se prémunir.</li>
<li><em>masṭūran</em> (tracé) : dans le décret antérieur — ce que la Plume traça sur la Table gardée.</li>
</ul>
<h3>Extraction des idées des versets</h3>
<ul>
<li>De quoi Dieu, le Très-Haut, a-t-Il interdit en ces versets ?</li>
<li>Quelle est la sagesse que contiennent les versets ?</li>
<li>Par quoi Dieu, le Très-Haut, a-t-Il rassuré Son prophète — paix et bénédiction sur lui — en les versets ?</li>
</ul>
<h3>Le commentaire (tafsīr)</h3>
<p>Ces versets comprennent ce qui suit :</p>
<h3>Premièrement : l’interdit d’adorer autre que Dieu, le Très-Haut</h3>
<p>Les versets poursuivent l’exposé de la vanité de ce que les associateurs adorent en dehors de Dieu. Le Très-Haut a dit :</p>
<p>« Dis : “ Invoquez ceux que vous prétendez, (être des divinités) en dehors de Lui. Ils ne possèdent ni le moyen de dissiper votre malheur ni de le détourner. ” » (al-Isrāʾ, 56)</p>
<p>[Citation coranique (v. 56) restaurée d’après le corpus canonique : l’emplacement imprimé est vide — perte OCR.]</p>
<p>Et ceux à qui Dieu ordonna à Son messager — paix et bénédiction sur lui — de s’adresser en ce verset ne sont pas les adorateurs d’idoles : ce sont les adorateurs d’êtres doués de raison. Dit Ibn Masʿūd : il descendit au sujet des adorateurs des démons — les Khuzāʿa, qui s’étaient soumis [à l’islam] et étaient restés à adorer les démons. Et dit Ibn ʿAbbās : au sujet de ʿUzayr, du Messie et de sa mère. Et de lui aussi, d’Ibn Masʿūd, d’Ibn Zayd et d’al-Ḥasan : au sujet des adorateurs des anges ; et d’Ibn ʿAbbās : au sujet des adorateurs du soleil, de la lune, des astres, de ʿUzayr, du Messie et de sa mère.</p>
<p>Et en Sa parole : <em>yadʿūna</em> (« ceux qu’ils invoquent ») — [Abū Ḥayyān :] “ un pronom omis renvoyant à <em>alladhīna</em>, qui est le premier objet ; et le second objet est omis, l’estimation : <em>vous les alléguâtes dieux en dehors de Dieu</em> ”. [al-Baḥr al-Muḥīṭ fī l-tafsīr, d’Abū Ḥayyān : 7/70 — réf. imprimée « 7/70 », conforme]</p>
<p>[Mot « yadʿūna » restauré d’après le corpus canonique : l’emplacement imprimé est vide — perte OCR ; citation d’Abū Ḥayyān intacte.]</p>
<p>Et le sens du verset : dis à ces associateurs : invoquez, aux détresses et au mal, ces adorés — ils ne possèdent ni d’en dissiper [le mal] ni de le détourner de vous. Puis Il les informa — sur la lecture d’Ibn Masʿūd et de Qatāda : <em>tadʿūna</em> (“ vous invoquez ”), au <em>tāʾ</em> — ou informa le Prophète — paix sur lui —, sur la lecture du <em>jumhūr</em>, au <em>yāʾ</em> : ces adorés cherchent le rapprochement de Dieu et l’approche de Lui — et tel est le véritable état des choses.</p>
<p>Et Sa parole, glorifié soit-Il : <em>ulāʾika</em> (“ ceux-là ”) — il est visé par elle les adorés ; c’est un <em>mubtadaʾ</em> dont le prédicat est <em>yabtaghūna</em> (“ cherchent ”) ; et le pronom de <em>yadʿūna</em> (“ ils invoquent ”) est aux dénégateurs, celui de <em>yabtaghūna</em> aux adorés. Et <em>al-wasīla</em> (“ le moyen d’approche ”) est la proximité et le moyen d’atteindre le but : <em>tawassala</em> l’homme, quand il chercha le proche et l’obtention de quelque chose. Dit ʿAntara : “ les hommes ont, certes, vers toi un moyen d’approche ” — et de là la parole du Prophète — paix et bénédiction sur lui : “ quiconque demande à Dieu la <em>wasīla</em> pour moi ”, et le hadith [continue].</p>
<p>[Mots « ulāʾika », « yabtaghūna » (×2), « yadʿūna » (×2) et « al-wasīla » restaurés d’après le corpus canonique : les emplacements imprimés sont vides — perte OCR ; répartition des pronoms vérifiée sur le texte d’Ibn ʿAṭiyya : « والضمير في ﴿يدعون﴾ للكفار، وفي ﴿يبتغون﴾ للمعبودين ».]</p>
<p>Et <em>ayyuhum</em> (“ lequel d’eux ”) est un <em>mubtadaʾ</em>, et <em>aqrabu</em> (“ le plus proche ”) son prédicat ; et <em>ayy</em> est interrogatif — l’estimation : ils observent et s’assurent lequel d’eux est le plus proche, et se rapprochent par lui. Et dit Ibn Fūrak et d’autres : le discours, depuis Sa parole : <em>ulāʾika lladhīna yadʿūna</em> (“ ceux-là, ceux qu’ils invoquent ”), retourne aux prophètes dont le mention précéda [au v. 55] — <em>yadʿūna</em> est alors de l’appel : c’est-à-dire ils appellent les gens à la religion de Dieu ; et le pronom élevé de <em>yadʿūna</em> et de <em>yabtaghūna</em> revient à eux aussi.</p>
<p>[Mots « ayyuhum », « aqrabu », « ulāʾika lladhīna yadʿūna », « yadʿūna » et « yabtaghūna » restaurés d’après le corpus canonique : les emplacements imprimés sont vides — perte OCR ; la lecture d’Ibn Fūrak vérifiée sur le texte d’Ibn ʿAṭiyya.]</p>
<p>Et Sa parole, le Très-Haut : <em>min</em> (“ de ”) est pour la détermination du genre ; et le pronom de <em>muhlikūhā</em> (“ que Nous faisons périr ”) revient sur la ville — et, en son sein, sur les habitants. Et Sa parole : <em>muʿadhdhibūhā</em> (“ que Nous punissons ”) est sur l’élision d’un complément : on ne châtie que les habitants. Et Sa parole : <em>fī l-kitābi</em> (“ dans le Livre ”) veut dire : dans le décret antérieur, et ce que la Plume traça sur la Table gardée. Et <em>masṭūran</em> (“ tracé ”) : écrit.</p>
<p>[Mots « min », « muhlikūhā », « muʿadhdhibūhā », « fī l-kitābi » et « masṭūran » restaurés d’après le corpus canonique : les emplacements imprimés sont vides — perte OCR. La glose de « min » — “ pour la détermination du genre ” — suit le texte d’Ibn ʿAṭiyya ; Abū Ḥayyān s’y interroge en note (peut-être « pour l’englobement du genre »), noté.]</p>
<p>Et le sens du verset : il n’est pas de ville des villes qui ne soit périe avant le Jour de la résurrection — par la mort et le dépérissement, prise part à part — ou qui ne soit châtiée, saisie d’une seule fois : c’est là un englobement pour toute ville. On dit : le visé est la particularité — c’est-à-dire : “ il n’est pas de ville injustice ”. Le su est que toute ville périt : soit du côté de la sécheresse et de l’effondrement, en submersion ; soit des discordes, soit des deux. Les formes de cela sont nombreuses, que Dieu, Puissant et Majestueux, seul connaît : quant à ce qui périt par la discorde, c’est par injustice, à n’en pas douter — soit en déni, soit en désobéissances, soit en défaillance de défense et de rigueur ; quant à la sécheresse, Dieu en frappe qui Il veut, et de même l’effondrement.</p>
<h3>Deuxièmement : la sagesse pour laquelle Dieu, le Très-Haut, ne particularisa point Quraysh d’un de Ses signes</h3>
<p>Dieu, le Très-Haut, expose la sagesse du non-accord à Quraysh d’un miracle de Ses miracles. Le Glorifié dit :</p>
<p>« Rien ne Nous empêche d’envoyer les miracles, si ce n’est que les Anciens les avaient traités de mensonges. » (al-Isrāʾ, 59 — première partie)</p>
<p>La première [des deux clauses <em>an</em>] est en position d’accusatif, la seconde en position de nominatif — l’estimation : ce qui Nous empêcha d’envoyer fut seulement le beliement. Il y a en la parole une omission, et le sens : rien ne Nous empêcha d’envoyer les signes qu’ils demandèrent, sinon qu’ils les belieraient et périraient, comme il advint de ceux qui furent avant eux. Et Dieu, le Très-Haut, nomma Son décret antérieur — belier qui belia et châtier qui châtia — un “ empêchement ”, sur l’apparent de ce que comprennent les Arabes.</p>
<p>[Citation coranique (v. 59, première partie) restaurée d’après le corpus canonique : l’emplacement imprimé est vide — perte OCR ; l’analyse des deux <em>an</em> vérifiée sur le texte d’Ibn ʿAṭiyya (« وأن الأولى في موضع نصب، والثانية في موضع رفع »).]</p>
<p>Et la cause de la descente de ce verset : Quraysh demandèrent au Messager de Dieu — paix et bénédiction sur lui — de leur faire de al-Ṣafā de l’or ; certains demandèrent qu’Il déplace d’eux les montagnes, pour qu’ils cultivent la terre. Dieu révéla à Muḥammad — prière et salut sur lui : si tu veux que Je fasse cela pour eux — s’ils reculent de la foi, le châtiment les surprendra ; et si tu veux, Je userai de patience avec eux, peut-être élirai-Je d’eux des croyants. Le Messager de Dieu — paix et bénédiction sur lui — dit : “ Non : use de patience avec eux, Seigneur ”. Et Dieu, le Très-Haut, différa le châtiment des associateurs de Quraysh, par Sa science qu’il est en eux qui croira, et en eux qui naîtra croyant.</p>
<p>Et quand Dieu, le Très-Haut, sut que les associateurs diraient : “ si nous était venu un signe de ce que nous avons demandé, nous aurions cru ” — Dieu, le Très-Haut, leur objecta et leur rappela l’affaire de Thamûd. Il dit :</p>
<p>« Nous avions apporté aux Thamûd la chamelle qui était un miracle visible : mais ils lui firent du tort. » (al-Isrāʾ, 59 — seconde partie)</p>
<p>Sa parole : <em>mubṣiratan</em> (“ de vue claire ”) est sur le mode de la relation (<em>naṣab al-nisba</em>) : c’est-à-dire, avec elle une vue — comme Il dit :</p>
<p>« …et Nous fîmes le signe du jour de vue [claire] » (al-Isrāʾ, 12 — extrait)</p>
<p>c’est-à-dire, avec elle une vue de qui regarde : c’est l’expression de l’éclaircissement de son affaire et de la clarté de sa nature miraculeuse. Et des gens lurent <em>mubṣira</em>, au <em>ḍamma</em> du <em>mīm</em> et au <em>fatḥa</em> du <em>ṣād</em> — al-Zajjāj le rapporta —, son sens : manifeste. Et Qatāda lut <em>mabṣara</em>, au <em>fatḥa</em> du <em>mīm</em> et du <em>ṣād</em> : c’est un schème <em>mafʿala</em> de la vue — tel le dire d’ʿAntara :</p>
<p>“ On m’a informé qu’ʿAmr ne rend grâce de mon bienfait — / et l’ingratitude est corruption pour l’âme du bienfaiteur. ”</p>
<p>Et Sa parole : <em>fa-ẓalamū bihā</em> (“ ils lui firent du tort ”) — c’est-à-dire : ils posèrent l’acte hors de son lieu, quand ils l’immolèrent ; on dit : par le déni en son affaire. Et le sens : Dieu, le Très-Haut, donna aux Thamûd la chamelle, signe manifeste de Ses signes — ils la nièrent et l’immolèrent : ne vous fiez point [à croire] que vous ne commettriez pas d’injustice envers le signe que vous avez demandé, comme Thamûd commit l’injustice envers la chamelle.</p>
<p>[Citations coraniques (v. 59, seconde partie ; mots « mubṣiratan », « fa-ẓalamū bihā ») et extrait d’al-Isrāʾ 12 (span imprimé « [الإسراء: 12] ») restaurés d’après le corpus canonique : les emplacements imprimés sont vides — perte OCR ; le parallèle du v. 12 vérifié sur le texte d’Ibn ʿAṭiyya (« كما قال: ﴿آية النهار مبصرة﴾ »). Vers d’ʿAntara intact (traduit).]</p>
<p>Puis Dieu, le Très-Haut, informa qu’Il n’envoie de signes — non demandés — qu’en effroi des serviteurs. Le Glorifié dit :</p>
<p>« En outre, Nous n’envoyons de miracles qu’à titre de menace. » (al-Isrāʾ, 59 — fin)</p>
<p>Ces signes sont des signes avec délai, non sans délai : de ce nombre l’éclipse, le tonnerre, la secousse, la mort soudaine et autre. Il fut rapporté que Kūfa trembla au temps d’ʿAbd Allāh b. Masʿūd, qui dit : “ gens ! votre Seigneur vous invite à réparer : réparez ”. Et de ce nombre le dire du Prophète — paix et bénédiction sur lui — en l’éclipse : “ hâtez-vous à la prière ”, et le hadith [continue]. Et les signes de Dieu dont on tire leçon sont de trois classes : une classe englobante en toute chose — où que tu poses ton regard, tu trouves un signe : c’est là la réflexion des savants ; une classe coutumière, occasionnelle (<em>ghabbā</em>) — le tonnerre, l’éclipse et pareils : c’est là la réflexion des ignorants seulement ; et une classe rompant la coutume, éteinte avec l’extinction de la prophétie — on n’en tire leçon que par supposition de ce qui s’en est passé.</p>
<p>[Citation coranique (v. 59, fin) restaurée d’après le corpus canonique : l’emplacement imprimé est vide — perte OCR.]</p>
<h3>Troisièmement : la protection que Dieu, le Très-Haut, accorde à Son prophète — paix et bénédiction sur lui — contre les associateurs</h3>
<p>Le Glorifié dit :</p>
<p>« Et lorsque Nous te disions que ton Seigneur cerne tous les gens (par Sa puissance et Son savoir). » (al-Isrāʾ, 60 — ouverture)</p>
<p>— c’est-à-dire : et rappelle, Muḥammad, quand Nous t’informâmes que Dieu cerne les gens — en ta protection, ta sauvegarde et ta préservation : délivre donc le message de ton Seigneur, et ne redoute nul des créatures. Le verset l’informe qu’il est gardé des dénégateurs, en sûreté d’être tué ou atteint d’un grand mal.</p>
<p>Et Sa parole, le Très-Haut :</p>
<p>« Quant à la vision que Nous t’avions montrée, Nous ne l’avons faite que pour éprouver les gens, tout comme l’arbre maudit mentionné dans le Coran. » (al-Isrāʾ, 60 — milieu)</p>
<p>Les gens divergèrent sur la <em>ruʾyā</em> (la vision). Dit le <em>jumhūr</em> : c’est vision de l’œil et en veille — ce que le Messager de Dieu — paix et bénédiction sur lui — vit en la nuit du Voyage nocturne. Ils dirent : quand le Messager de Dieu — paix et bénédiction sur lui — eut informé, au matin du Voyage, des merveilles qu’il avait vues cette nuit-là, les dénégateurs dirent : “ voilà qui est étrange — les chameliers poussent jusqu’à Jérusalem deux mois, aller et retour, et Muḥammad prétend y être allé d’une nuit et en être revenu ! ” Des faibles des musulmans s’égaraient à cette confusion et apostasièrent ; cela affligea le Messager de Dieu — paix et bénédiction sur lui —, et ces versets descendirent.</p>
<p>Sur ce, il est beau que le sens de Sa parole :</p>
<p>« Et lorsque Nous te disions que ton Seigneur cerne tous les gens » (al-Isrāʾ, 60 — ouverture, requoté)</p>
<p>soit : en leur égarement et leur guidée — et que chacun est affermi en ce pour quoi il fut créé — c’est-à-dire : ne te soucie point de qui a nié, ni ne t’afflige sur eux : il t’a été dit que Dieu les cerne, Maître de leur affaire, et qu’Il a fait ta vision cette épreuve, pour que mécroie celui sur qui la mécréance a précédé. Et dit Ibn ʿAbbās : la vision en ce verset est la vision du Messager de Dieu — paix et bénédiction sur lui — qu’il entrerait à La Mecque : il s’empressa en l’année d’al-Ḥudaybiya et en fut repoussé — les musulmans s’en égarèrent, et les versets descendirent.</p>
<p>[Citations coraniques (v. 60, ouverture ×2 et milieu) restaurées d’après le corpus canonique : les emplacements imprimés sont vides — perte OCR ; la requotation de l’ouverture vérifiée sur le texte d’Ibn ʿAṭiyya (« يحسن أن يكون معنى قوله ﴿وإذا قلنا لك إن ربك أحاط بالناس﴾ »).]</p>
<p>Et Sa parole, le Très-Haut :</p>
<p>« …tout comme l’arbre maudit mentionné dans le Coran. » (al-Isrāʾ, 60)</p>
<p>L’arbre, ici, au dire du <em>jumhūr</em>, est l’arbre <em>Zaqqūm</em> ; il fut décrit de “ maudit ” et il fut visé par cela : maudit qui le mange — car il n’en fut pas fait mention dans le Coran sinon en cet endroit. Dit Ibn ʿAṭiyya : et il est valable qu’il vise <em>al-malʿūna</em> (“ la maudite ”) ici — et Il affermit l’affaire par Sa parole : <em>fī l-Qurʾāni</em> (“ dans le Coran ”). Et un groupe dit : “ la maudite ”, l’éloignée, la réprouvée — car Dieu, le Très-Haut, la maudit du terme de malédiction reçu, et ce qui pousse à la racine du gouffre est à l’extrême éloignement de la miséricorde de Dieu. « …et l’arbre maudit mentionné dans le Coran » est coordonné à « la vision » — c’est-à-dire : Nous fîmes de la vision et de l’arbre une épreuve.</p>
<p>[Mots « al-malʿūna », « fī l-Qurʾāni » et coordination de « wa-l-shajarata l-malʿūnata fī l-Qurʾāni » sur « al-ruʾyā » restaurés d’après le corpus canonique : les emplacements imprimés sont vides — perte OCR ; la coordination vérifiée sur le texte d’Ibn ʿAṭiyya (« معطوفة على قوله ﴿الرؤيا﴾ »).]</p>
<p>Et Sa parole, glorifié soit-Il :</p>
<p>« Nous les menaçons, mais cela ne fait qu’augmenter leur grande transgression. » (al-Isrāʾ, 60 — fin)</p>
<p>— c’est-à-dire : Nous effrayons ces dénégateurs — les dénégateurs de La Mecque — des effrois de ce monde et de l’autre, et les menaçons des châtiments : c’est-à-dire, l’effroi n’augmente en eux que l’obstination en ce qu’ils sont dedans de déni et d’égarement.</p>
<p>[Citation coranique (v. 60, fin) restaurée d’après le corpus canonique : l’emplacement imprimé est vide — perte OCR.]</p>
<h3>Les finalités des versets</h3>
<p>Ces versets visent la réalisation d’un ensemble de finalités éducatives, dont :</p>
<p>• L’appel à l’unicité de Dieu, le Très-Haut, qui seul mérite l’adoration — et la réponse aux associateurs qui adorent ce qui ne possède pour eux ni profit ni dommage.</p>
<p>• L’exposé de la faveur de Dieu, le Très-Haut, et de Sa grâce envers les musulmans : le délai qu’Il leur accorde et le différé de leur châtiment, pour le repentir et la droiture — comme Il gracia Son prophète de Sa protection de son peuple, pour l’autoriser à transmettre le message dont Puissant et Majestueux l’a chargé.</p>
<h3>L’évaluation (taqwīm)</h3>
<ul>
<li>Je conclus les traits de faiblesse et de défaillance en ce que les gens adorent en dehors de Dieu.</li>
<li>Je montre l’effet de la divergence sur le retour du pronom, en le sens de Sa parole : « Ceux qu’ils invoquent, cherchent [eux-mêmes], à qui mieux, le moyen de se rapprocher le plus de leur Seigneur » ?</li>
<li>Pourquoi Dieu n’établit-Il pas la preuve contre les associateurs de Quraysh par un des signes qu’ils demandèrent ?</li>
</ul>
<p>[Citation coranique (v. 57 — objet de la deuxième question, la divergence des pronoms) restaurée d’après le corpus canonique : l’emplacement imprimé est vide — perte OCR.]</p>
<h3>L’investissement (istithmār)</h3>
<p>Dit al-Alūsī — Dieu lui fasse miséricorde —, en son commentaire de Sa parole : <em>wa-mā manaʿanā an nursila bi-l-āyāti</em> (“ Rien ne Nous empêche d’envoyer les miracles ”) :</p>
<p>« Et mentionna certains des vérificateurs que le beliement des premiers — qui entraîne l’extirpation et implique le beliement des derniers, conduisant à la venue du fléau — contredit l’envoi des signes demandés, vu l’inévitabilité du beliement, lequel appelle ce qui contredit la sagesse du différé du châtiment de cette communauté : aussi fut exprimée cette contradiction par “ l’empêchement ”, sur le mode de l’emprunt (<em>istiʿāra</em>), pour avertir de la solidarité des principes de l’envoi — non comme ils le prétendirent : que le Très-Haut ne voudrait point fortifier Son messager — paix et bénédiction sur lui — de miracles. Et c’est le secret de la préférence de “ l’envoi ” (<em>irsāl</em>) sur “ la donation ” (<em>ītāʾ</em>) : en lui se fait sentir les signes se presser de descendre — n’eût été la main du décret qui les retient. Et l’attribution de l’empêchement au beliement des premiers, non à Sa science, le Très-Haut, de ce que seront des derniers demandeurs — comme en Sa parole :</p>
<p>« Et si Allah avait reconnu en eux quelque bien, Il aurait fait qu’ils entendent. Mais, même s’Il les faisait entendre, ils tourneraient [sûrement] le dos en s’éloignant. » (al-Anfāl, 23)</p>
<p>— c’est pour établir contre eux la preuve par l’exhibition du modèle, et pour avertir que le pivot du non-acquiescement à la donation de leur demande n’est autre que leur propre fait. » [Rūḥ al-Maʿānī, d’al-Alūsī : 8/99 — réf. imprimée « 99/8 », ordre inversé — (adapté)]</p>
<p>[Citation coranique (al-Anfāl, 23 — span imprimé « [الأنفال: 23] ») restaurée d’après le corpus canonique : l’emplacement imprimé est vide — perte OCR ; citation d’al-Alūsī intégrale et conforme.]</p>
<p>Je contemple le texte et réponds à ce qui suit :</p>
<p>— J’expose, à travers le texte, la cause de l’expression des versets par “ l’empêchement ” (<em>manʿ</em>) et “ l’envoi ” (<em>irsāl</em>).</p>
<h3>La préparation (iʿdād)</h3>
<p>Je contemple les versets 61 à 65 de la sourate al-Isrāʾ et réponds à ce qui suit :</p>
<ul>
<li>Je recherche la portée des expressions suivantes :</li>
</ul>
<p><em>karramta</em> (كَرَّمْتَ — Tu as honoré).</p>
<p><em>la-aḥtankanna</em> (لَأَحْتَنِكَنَّ — je briderai certes).</p>
<p><em>mawfūran</em> (مَّوْفُورًا — amplement requis).</p>
<p><em>istafziz</em> (ٱسْتَفْزِزْ — aiguillonne).</p>
<p><em>shārikhum</em> (شَارِكْهُمْ — partage-les).</p>
<p><em>ghurūrā</em> (غُرُورًا — duperie).</p>
<p>[Expressions restituées du lexique de la leçon suivante (versets 61-65) : les emplacements imprimés sont vides — perte OCR.]</p>
<p>— Quels sont les traits de l’honneur que Dieu, le Très-Haut, accorde à l’homme en les versets ?</p>
<ul>
<li>Je recherche le style rhétorique en la parole du Très-Haut :</li>
</ul>
<p>« Excite, par ta voix, ceux d’entre eux que tu pourras, rassemble contre eux ta cavalerie et ton infanterie » (al-Isrāʾ, 64)</p>
<p>— et j’expose son effet sur le sens.</p>
<p>[Citation coranique (v. 64, de la leçon suivante) restaurée d’après le corpus canonique : l’emplacement imprimé est vide — perte OCR. Elle prépare l’emprunt par ressemblance (<em>istiʿāra tamthīliyya</em>) du cavalier et de ses troupes — le crux rhétorique de la leçon suivante.]</p>"""


def main():
    with open(BOOK, "r", encoding="utf-8") as fh:
        d = json.load(fh)
    hit = 0
    for l in d["lessons"]:
        if l.get("docId") == "13620":
            l["htmlFr"] = HTML_FR
            hit += 1
    if hit != 1:
        raise SystemExit(f"ERREUR: {hit} leçons 13620 trouvées (attendu 1)")
    with open(BOOK, "w", encoding="utf-8") as fh:
        json.dump(d, fh, ensure_ascii=False, indent=1)
    print(f"OK — leçon 13620 upgradée main: FR {len(HTML_FR)} car")


if __name__ == "__main__":
    main()

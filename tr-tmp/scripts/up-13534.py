#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Minhāj — Upgrade GT→main : leçon 13534 (tafsir-tanawi-2, Sourate al-Isrāʾ
23-25, leçon 7 du manuel — al-Muḥarrar al-wajīz d'Ibn ʿAṭiyya).

Vérifications et restitutions :
- Bloc d'ouverture (17:23-25) : l'emplacement est un <h3> VIDE après
  « الآيات » (artefact OCR) → versets restaurés du quran-cache (3 versets),
  guillemets imbriqués convertis en “ ”.
- Citations inline perdues par l'OCR, identifiées par l'exégèse :
  * v23 p1 « وَقَضَىٰ رَبُّكَ أَلَّا تَعْبُدُوٓا۟ إِلَّآ إِيَّاهُ » après
    « فقال : » ; mot « قَضَىٰ » cité 2× dans les gloses (أمر/قدر) ;
  * pronom de « ألا تعبدوا » visant les croyants (discussion qadar) ;
  * « وَبِٱلْوَٰلِدَيْنِ إِحْسَٰنًا » coordonné à la première (iʿrāb) —
    « الأولى » imprimé, citation restituée ;
  * suite de v23 (vieillesse → parole généreuse) après « فصّل ما يجب » ;
  * discussion qirāʾique يَبْلُغَنَّ/يَبْلُغَانِ : lectures d'Ibn Kathīr,
    Nāfiʿ, Abū ʿAmr, ʿĀṣim, Ibn ʿĀmir (+ Ibn Dhakwān nūn allégé) vs
    Ḥamza/al-Kisāʾī (duel) ; fāʿil = أَحَدُهُمَا, maʿṭūf = أَوْ كِلَاهُمَا,
    badal distributif au duel — vers d'exemple (ذي رجلين) traduit ;
    langue « أكلوني البراغيث » + Sībawayh ;
  * « أُفٍّ » (lectures multiples, nom-verbe, mafHūm al-khiṭāb) ;
  * « وَلَا تَنْهَرْهُمَا », « وَقُل لَّهُمَا قَوْلًۭا كَرِيمًۭا » ;
  * v24 p1 (aile de l'humilité) + re-citation avant l'istiʿāra ;
  * parallèle Shuʿarāʾ : le manuel imprime « 214 », le contenu cité
    (وَٱخْفِضْ جَنَاحَكَ لِمَنِ ٱتَّبَعَكَ) = 26:215 du décompte canonique
    (214 = وأنذر عشيرتك) → doctrine R115 : canonique en principal + note ;
  * v24 p2 (رب ارحمهما) ; v25 en 2 citations (عِلْم des âmes / غفور
    للأوابين) ; « الأوّابين » cité 3× dans la discussion lexicale.
- Heading « ثانيا : أمر الله بالإحسان للوالدين… » FUSIONNÉ dans le
  <p> précédent par l'OCR → restitué en h3 propre.
- Réfs inversées corrigées : Qurṭubī « 244/10 » → 10/244 ; Rāzī « 321/20 »
  → 20/321 (doctrine R113).
- iʿdād (versets 26-30) : la leçon SUIVANTE (26-30) est ABSENTE du livre
  CMS (trou du manuel numérisé — la table des matières imprimée de 12579 la
  porte comme leçon 8) → les 5 expressions restituées des versets
  canoniques 26-30 : حَقَّهُ / المِسْكِين / ابن السبيل / تَبْذِيرًا /
  قَوْلًا مَّيْسُورًا ; la citation « نكتة بلاغية » = v29 (métaphore de la
  main enchaînée / trop étendue) ; note explicite de la restitution.
- Anomalies : « الغاضب،. » double ponctuation ; « ابن المسيب » (Saʿīd ibn
  al-Musayyab) ; le <p>&nbsp;</p> orphelin (image perdue) non rendu.
- GT non copié ; hadiths (Muslim « رغم أنف » ×3, Rāzī « من لم يشكر
  الناس ») traduits intégralement, réfs fidèles.
"""

import json

BOOK = "/home/z/my-project/content/books/tafsir-tanawi-2.json"

HTML_FR = """<h1>La sourate al-Isrāʾ — <em>al-Muḥarrar al-wajīz</em> d’Ibn ʿAṭiyya, versets 23 à 25</h1>
<p>Leçon d’exégèse de la sourate al-Isrāʾ, versets 23 à 25, du livre du Tafsīr à travers <em>al-Muḥarrar al-wajīz fī tafsīr al-kitāb al-ʿazīz</em> du cadi Abū Muḥammad Ibn ʿAṭiyya, à l’intention des élèves de la deuxième année de l’enseignement secondaire traditionnel (<em>taʿlīm ʿatīq</em>), phase 2 (leçon 7).</p>
<h3>Les objectifs de la leçon</h3>
<ul>
<li>Reconnaître l’obligation de réserver à Dieu seul l’adoration, et la bonté envers les parents.</li>
<li>Conclure des versets les convenances du commerce avec les parents et la bonté à leur égard.</li>
<li>Persévérer dans l’adoration de Dieu seul, et me conformer aux enseignements du Coran dans le commerce avec mes parents.</li>
</ul>
<h3>Introduction (tamhīd)</h3>
<p>Après que Dieu, le Très-Haut, eut exposé que la foi et l’œuvre pie sont le fondament du succès au bonheur éternel, et montré le plus grand pilier de la foi — l’unicité de Dieu et l’abstention du polythéisme —, Il fit suivre cela de l’énoncé d’un ensemble de charges légales qu’exige l’unicité : Il commença par réserver au Vrai, glorifié soit-Il, l’adoration et la préservation d’adorer autre que Dieu, le Très-Haut, puis enchaîna sur la bonté envers les parents.</p>
<p>Quelle est la finalité de l’adoration de Dieu ? Et comment être bon envers les parents ?</p>
<h3>Les versets</h3>
<p>Allah, le Très-Haut, a dit :</p>
<p>« Et ton Seigneur a décrété : “ N’adorez que Lui ; et (marquez) de la bonté envers les père et mère : si l’un d’eux ou tous deux doivent atteindre la vieillesse auprès de toi, alors ne leur dis point “ Fi ! ” et ne les brusque pas, mais adresse-leur des paroles respectueuses. (24) et par miséricorde, abaisse pour eux l’aile de l’humilité, et dis : “ Ô mon Seigneur, fais-leur, à tous deux, miséricorde comme ils m’ont élevé tout petit ”. (25) Votre Seigneur connaît mieux ce qu’il y a dans vos âmes. Si vous êtes bons, Il est certes Pardonneur pour ceux qui Lui reviennent se repentant. ” (al-Isrāʾ, 23-25)</p>
<p>[Citations coraniques restaurées d’après le corpus canonique : l’emplacement imprimé correspondant est vide dans la source numérisée — perte OCR.]</p>
<h3>La compréhension</h3>
<h4>Explication des termes</h4>
<ul>
<li><em>wa-qāḍā</em> (et ton Seigneur a décrété) : on a dit — du décret au sens d’ordre et d’injonction ; on a dit — du décret et de la prédestination.</li>
<li><em>uf</em> (Fi !) : je m’irrite, ou j’éprouve du dégoût, ou j’ai de l’aversion, ou ce qui s’en approche.</li>
<li><em>lā tanhurhumā</em> (ne les brusque pas) : l’<em>intihār</em> est la manifestation de la colère dans la voix et l’énoncé.</li>
<li><em>qawlan karīman</em> (des paroles respectueuses) : une parole douce, aisée, belle.</li>
<li><em>li-l-awwābīna</em> (pour ceux qui reviennent) : les repentants, ou ceux qui reviennent à l’obéissance de Dieu.</li>
</ul>
<h4>Extraction des idées des versets</h4>
<ul>
<li>Par quoi Dieu, Puissant et Majestueux, a-t-Il ordonné aux gens au début des versets ?</li>
<li>Qu’est-ce que Dieu a rendu obligatoire aux enfants en droit de leurs parents ?</li>
</ul>
<h3>Le commentaire (tafsīr)</h3>
<p>Ces versets comprennent ce qui suit :</p>
<h3>Premièrement : l’ordre donné par Dieu d’adorer Lui seul</h3>
<p>Après que Dieu, glorifié soit-Il, eut mentionné que le fondement de l’acceptation des actions est la foi en Dieu seul et l’abstention de Lui associer, Il fit suivre cela de ce qu’exige la foi en fait d’adoration et de commerce. Il dit :</p>
<p>« Et ton Seigneur a décrété : “ N’adorez que Lui ”</p>
<p>Le sens de <em>qāḍā</em> (a décrété) en ce verset peut être : Il a ordonné, imposé et rendu obligatoire sur vous — et non le décret-prédestination : car s’il était du décret-prédestination, nul n’adorerait autre que Dieu, il ne se pouvant pas que Dieu prédestine une chose qui n’advienne pas de beaucoup de gens. Ibn ʿAbbās, al-Ḥasan et Qatāda ont dit : “ Celui-ci n’est pas un décret de jugement : c’est un décret d’ordre. ” Et dans le <em>muṣḥaf</em> d’Ibn Masʿūd : “ Et ton Seigneur a recommandé ” (<em>wa-waṣṣā rabbuka</em>).</p>
<p>[Citation coranique (v. 23, début) restaurée d’après le corpus canonique : l’emplacement imprimé est vide — perte OCR.]</p>
<p>Il se peut aussi que soit visé le décret-prédestination : le décret s’attache alors à l’ordre d’adorer Dieu, non à l’adoration elle-même — c’est-à-dire : ton Seigneur a décrété Son ordre que vous n’adoriez que Lui. Ou bien le pronom en Sa parole : “ … que vous n’adoriez que Lui ” vise les croyants parmi les hommes à l’exclusion des autres ; et par là <em>qāḍā</em> demeure en son acception reçue, qui est le décret-prédestination.</p>
<h3>Deuxièmement : l’ordre donné par Dieu d’être bon envers les parents et d’observer les convenances en leur commerce</h3>
<p>Après que le Vrai, glorifié soit-Il, eut ordonné de Le réserver seul à l’adoration, Il y adjoignit l’ordre d’être bon envers les parents. Il dit :</p>
<p>« et (marquez) de la bonté envers les père et mère »</p>
<p>Sur la première interprétation du sens de <em>qāḍā</em> — l’ordre et l’injonction —, Sa parole : “ et (marquez) de la bonté envers les père et mère ” est coordonnée à la première : “ … que vous n’adoriez que Lui ” — c’est-à-dire : Dieu a ordonné que vous n’adoriez que Lui, et que vous soyez bons envers les parents en bonté.</p>
<p>[Citations coraniques partielles (v. 23) restaurées d’après le corpus canonique : les emplacements imprimés sont vides — perte OCR.]</p>
<p>Et sur la seconde interprétation du sens de <em>qāḍā</em> — le décret-prédestination —, Sa parole : “ et (marquez) de la bonté envers les père et mère ” est coupée de la première : c’est comme s’Il les informait du décret de Dieu, puis leur ordonnait la bonté envers les parents.</p>
<p>Puis Il détailla ce qui est obligatoire de bonté envers eux, par Sa parole :</p>
<p>« … si l’un d’eux ou tous deux doivent atteindre la vieillesse auprès de toi, alors ne leur dis point “ Fi ! ” et ne les brusque pas, mais adresse-leur des paroles respectueuses. »</p>
<p>[Citation coranique (v. 23, suite) restaurée d’après le corpus canonique : l’emplacement imprimé est vide — perte OCR.]</p>
<p>Ibn Kathīr, Nāfiʿ, Abū ʿAmr, ʿĀṣim et Ibn ʿĀmir ont lu <em>yabluganna</em> (doivent atteindre — <em>nūn</em> doublé) ; d’Ibn Dhakwān fut rapporté <em>yablugan</em>, à <em>nūn</em> allégé. Sur les deux lectures, Sa parole : “ l’un d’eux ” (<em>aḥaduhumā</em>) est l’agent (<em>fāʿil</em>), et Sa parole : “ ou tous deux ” (<em>aw kilāhumā</em>) lui est coordonnée.</p>
<p>Ḥamza et al-Kisāʾī ont lu <em>yablugāni</em> — au <em>nūn</em> lourd après l’<em>alif</em> de duel. Sur cette lecture, Sa parole : “ l’un d’eux ” est une apposition (<em>badal</em>) du pronom en <em>yablugāni</em> — apposition distributive (<em>badal muqassam</em>) —, comme le dit le poète :</p>
<p>« J’étais tel celui de deux jambes : une jambe saine, ** et une jambe où le temps décocha — et elle se paralyse. »</p>
<p>Il est loisible aussi que “ l’un d’eux ” soit l’agent, et Sa parole : “ ou tous deux ” lui soit coordonnée — cela selon la langue de ceux qui disent : “ <em>akalūnī l-barāghīth</em> ” (les puces m’ont mangé). Tel grammairien a mentionné cela en ce verset ; Sībawayh, lui, ne voit nulle place pour cette langue dans le Coran.</p>
<p>Et Sa parole, glorifié soit-Il : “ Fi ! ” (<em>uf</em>) porte plusieurs lectures, et son sens est : ne dis pas “ je me suis irrité ” ni “ je m’irrite ”. <em>Uf</em> est un nom-verbe (<em>ism fiʿl</em>) : celui qui voudrait dire “ je m’irrite ”, “ je me plains ”, “ j’ai de l’aversion ” ou ce qui s’en approche, s’exprime par abréviation en ce mot, qui reçoit alors le sens du verbe dit. Dieu, le Très-Haut, a fait de ce mot l’exemple de tout ce dont on pourrait riposter aux parents parmi ce qu’ils honnissent : le visé n’est pas ce mot en soi — il est l’exemple du plus grand que lui comme du moindre. Tel est le compris du discours (<em>mafHūm al-khiṭāb</em>) : ce qu’on tait a le statut de ce qu’on dit.</p>
<p>Et Sa parole, le Très-Haut : “ et ne les brusque pas ” — l’<em>intihār</em> est la manifestation de la colère dans la voix et l’énoncé.</p>
<p>Puis le Très-Haut dit : “ mais adresse-leur des paroles respectueuses ”. La parole généreuse est celle qui rassemble les beautés — douceur, excellence du sens, contenu de piété filiale —, comme tu dis : “ un vêtement généreux ”, voulant qu’il cumule les beautés. On interrogea Saʿīd ibn al-Musayyab sur la parole généreuse ; il dit : c’est la parole du serviteur coupable au maître rude.</p>
<p>Puis le Très-Haut ordonna l’extrême en humilité avec eux. Il dit :</p>
<p>« et par miséricorde, abaisse pour eux l’aile de l’humilité, »</p>
<p>[Citation coranique (v. 24, début) restaurée d’après le corpus canonique : l’emplacement imprimé est vide — perte OCR.]</p>
<p>« abaisse pour eux l’aile de l’humilité » : métaphore (<em>istiʿāra</em>) — l’humilité y est comparée à un oiseau pourvu d’une aile ; puis l’oiseau est omis, et désigné par un de ses attributs, l’aile — c’est-à-dire : coupe-leur le côté d’humilité de toi, et adoucis pour eux ton âme et ton caractère. L’humilité est poussée ici jusqu’à être dite, alors qu’elle ne l’est pas en Sa parole :</p>
<p>« Et abaisse ton aile [sois bienveillant] pour les croyants qui te suivent. » (ash-Shuʿarāʾ, 215 — le manuel imprime « 214 »)</p>
<p>— à proportion de la grandeur du droit, ici. La <em>dhalūl</em> (docilité), chez les bêtes, est le contraire de la rétivité — d’où le chameau docile (<em>jamal dhalūl</em>) ; les sens se touchent. En vertu de ce verset, il sied que l’homme se tienne avec ses deux parents en la meilleure humilité — en ses paroles, son effacement, son regard —, et qu’il ne darde pas vers eux son regard : c’est celui de l’irrité. Témoin le hadith où l’Envoyé de Dieu — paix et bénédiction sur lui — dit : “ Qu’il ait le nez en poussière — puis qu’il ait le nez en poussière — puis qu’il ait le nez en poussière ! ” On dit : Qui donc, ô Envoyé de Dieu ? Il dit : “ Celui qui atteint ses parents dans leur grand âge, l’un des deux ou tous deux, et n’entre pas au Paradis. ” [Ṣaḥīḥ Muslim, Livre de la piété filiale, du lien et des convenances, chapitre : qu’il ait le nez en poussière, celui qui atteint ses parents ou l’un d’eux dans leur grand âge et n’entre pas au Paradis].</p>
<p>[Citations coraniques partielles (v. 24 et parallèle ash-Shuʿarāʾ) restaurées d’après le corpus canonique : les emplacements imprimés sont vides — perte OCR.]</p>
<p>Sa parole : “ par ” (<em>min</em>) : la miséricorde est ici explicative du genre — c’est-à-dire que cet abaissement procède de la miséricorde tapie en l’âme, non qu’il en soit un emploi de convention ; et il est recevable qu’il marque le point de départ (de la miséricorde).</p>
<p>Puis Dieu ordonna à Ses serviteurs la miséricorde envers les parents, et leur rappela Son bienfait sur eux en l’éducation — afin que le souvenir de cet état accroisse chez l’homme l’attendrissement et la tendresse pour eux. Le Très-Haut dit :</p>
<p>« et dis : “ Ô mon Seigneur, fais-leur, à tous deux, miséricorde comme ils m’ont élevé tout petit ”. »</p>
<p>[Citation coranique (v. 24, fin) restaurée d’après le corpus canonique : l’emplacement imprimé est vide — perte OCR.]</p>
<p>Al-Qurṭubī a dit : “ Le Très-Haut ordonna à Ses serviteurs la miséricorde envers leurs pères et l’invocation pour eux — que ta miséricorde sur eux soit comme la leur sur toi, et ta douceur comme leur douceur : ils t’eurent en charge petit, ignorant, nécessiteux, et te préférèrent à eux-mêmes ; ils veillèrent leurs nuits et connurent la faim, et te nourrirent ; ils se dévêtirent et te vêtirent. Tu ne les en rétribueras qu’en ce qu’ils parviennent, du grand âge, à la limite où tu fus, toi, de la petitesse : tu auras alors d’eux la charge qu’ils eurent de toi — et leur appartiendra alors l’antériorité du mérite. ” [al-Ǧāmiʿ li-aḥkām al-Qurʾān, d’al-Qurṭubī : 10/244 — réf. imprimée « 244/10 », ordre inversé]</p>
<p>Puis Dieu, le Très-Haut, mit Ses serviteurs en garde contre la tiédeur en la piété filiale. Il dit :</p>
<p>« Votre Seigneur connaît mieux ce qu’il y a dans vos âmes. »</p>
<p>c’est-à-dire : votre Seigneur sait mieux ce que renferment vos âmes — croyance en la miséricorde due aux parents et inclina pour eux, ou autre chose. La piété filiale apparente, quand l’habite la sincérité, n’est pas ostentation : Dieu, le Très-Haut, est informé de ce qu’il y a en vos âmes, et sait mieux vos états apparents et intimes.</p>
<p>[Citation coranique (v. 25, début) restaurée d’après le corpus canonique : l’emplacement imprimé est vide — perte OCR.]</p>
<p>Puis, en la fin du verset, Il promit le pardon, à condition de droiture et de retours réitérés à l’obéissance de Dieu. Il dit :</p>
<p>« Si vous êtes bons, Il est certes Pardonneur pour ceux qui Lui reviennent se repentant. »</p>
<p>[Citation coranique (v. 25, fin) restaurée d’après le corpus canonique : l’emplacement imprimé est vide — perte OCR.]</p>
<p>On divergea sur le visé par “ ceux qui reviennent ” (<em>al-awwābīn</em>) en ce verset. Un parti dit : ce sont les réformateurs. Ibn ʿAbbās dit : ce sont ceux qui glorifient ; il dit aussi : ce sont les obéissants bienfaisants. Ibn al-Munkadir dit : ce sont ceux qui font les prières de l’<em>ʿishāʾ</em> et du <em>maghrib</em>. ʿAwn al-ʿAqīlī dit : ce sont ceux qui font la prière de la mi-journée (<em>ḍuḥā</em>). La réalité du mot : il vient de <em>āba yaʾūbu</em>, “ revenir ” — et tous ceux-là ne cessent de revenir à l’obéissance de Dieu, le Très-Haut. Ibn [Saʿīd] al-Musayyab : c’est le serviteur qui se repent, puis pèche, puis se repent, puis pèche, puis se repent. La foule des docteurs interpréta “ ceux qui reviennent ” par : ceux qui reviennent au bien. Ibn Jubayr dit : il visait, par Sa parole “ pour ceux qui reviennent ”, la chute et le lapsus qui peuvent survenir de l’homme envers l’un de ses deux parents — alors qu’il n’y a point persisté en son cœur, et ne l’a point fait savoir à Dieu de lui-même.</p>
<h3>Troisièmement : les finalités des versets</h3>
<p>Ces versets orientent vers un ensemble de finalités éducatives, dont :</p>
<ul>
<li>L’ordre d’adorer Dieu seul et de Lui réserver la servitude à l’exclusion de tout autre — cette adoration qui est la finalité de l’existence de l’homme en cette vie.</li>
<li>C’est la persévérance dans l’adoration de Dieu qui réalise pour l’homme sa liberté plénière : la servitude pure envers Dieu est la liberté même, et le chemin de la vraie souveraineté.</li>
<li>Le rappel des nombreux bienfaits de Dieu sur l’homme — dont le plus grand est le bienfait des parents, que Dieu fit cause de l’existence de l’homme, disposa au service de sa petitesse et en fit en eux un instinct ; comme Il disposa l’enfant au service de ses parents dans leur grand âge, et lui ordonna la bonté et le soin envers eux.</li>
<li>L’insistance sur la bonté envers les parents, en rétribution de ce qu’ils ont prodigué à leurs enfants d’efforts, de dons et de services — bonté qui se renforce en leur grand âge et leur impuissance. La bonté est matérielle — la dépense sur eux, obligatoire ou bénévole — et spirituelle : abaisser l’aile, adoucir la parole, obéir hors désobéissance.</li>
</ul>
<h3>L’évaluation (taqwīm)</h3>
<ul>
<li>Que signifie la parole du Très-Haut : “ Et ton Seigneur a décrété ” (<em>wa-qāḍā rabbuka</em>) ?</li>
<li>Quel est le secret de l’adjonction de l’ordre d’adorer Dieu à la bonté envers les parents, en maints versets ?</li>
<li>Qu’indique, en son dit et son compris, la parole du Très-Haut : “ Votre Seigneur connaît mieux ce qu’il y a dans vos âmes ” ?</li>
<li>J’explicite le sens de Sa parole : “ abaisse pour eux l’aile de l’humilité ” (<em>wa-khfiḍ lahumā janāḥa l-dhill</em>), à l’aide des règles de rhétorique.</li>
</ul>
<h3>L’investissement (istithmār)</h3>
<p>Fakhr al-Dīn al-Rāzī — que Dieu lui fasse miséricorde — a dit : “ Sache que le Très-Haut ordonna d’adorer Sa personne, puis y fit suivre l’ordre de la piété filiale. L’exposé du rapport entre l’ordre d’adorer Dieu, le Très-Haut, et l’ordre de la piété filiale tient en des faces :<br>
Première face : la cause véritable de l’existence de l’homme est la création et la production par Dieu, le Très-Haut ; la cause apparente est les deux parents. Il ordonna donc la magnification de la cause véritable, puis y fit suivre l’ordre de magnifier la cause apparente.<br>
Seconde face : l’existant est ou éternel ou adventice ; il se doit que le commerce de l’homme avec l’Éternel soit magnification et servitude, et avec l’adventice, manifestation de tendresse — ce que vise sa parole sur lui le salut : “ La magnification est pour l’ordre de Dieu, la tendresse pour la création de Dieu. ” Et nulle créature ne mérite plus qu’on lui porte la tendresse que les deux parents, tant est grand leur bienfait sur l’homme. Sa parole : “ … que vous n’adoriez que Lui ” est une allusion à la magnification de l’ordre de Dieu, et Sa parole : “ et (marquez) de la bonté envers les père et mère ”, une allusion à la tendresse pour la création de Dieu.<br>
Troisième face : l’occupation à rendre grâce au Bienfaiteur est obligatoire ; or le Bienfaiteur véritable est le Créateur, glorifié et exalté soit-Il. Il peut être qu’un créé soit bienfaiteur envers toi — sa gratitude est pareillement obligatoire, en vertu de sa parole sur lui le salut : “ Qui ne remercie pas les gens ne remercie pas Dieu. ” Et nul des êtres n’a sur l’homme un bienfait pareil à celui des parents. ” [Mafātīḥ al-ghayb, de Fakhr al-Dīn al-Rāzī : 20/321 — réf. imprimée « 321/20 », ordre inversé]</p>
<p>Je contemple le texte et réponds à ce qui suit :</p>
<ul>
<li>Quel est le secret de l’ordre de la piété filiale aussitôt après l’ordre d’adorer Dieu ?</li>
<li>Que signifie que les parents soient cause de l’existence de l’homme ?</li>
</ul>
<h3>La préparation (iʿdād)</h3>
<p>Je contemple les versets 26 à 30 de la sourate al-Isrāʾ et réponds à ce qui suit :</p>
<ul>
<li>Je recherche la portée des expressions suivantes :</li>
</ul>
<p><em>ḥaqqahu</em> (حَقَّهُ — ce qui lui est dû).</p>
<p><em>al-miskīn</em> (ٱلْمِسْكِين — le pauvre).</p>
<p><em>ibn al-sabīl</em> (ٱبْنُ ٱلسَّبِيلِ — le voyageur en détresse).</p>
<p><em>tabdhīran</em> (تَبْذِيرًا — le gaspillage outrancier).</p>
<p><em>qawlan maysūran</em> (قَوْلًۭا مَّيْسُورًا — une parole aisée).</p>
<p>[Expressions restituées des versets canoniques 26-30 : la leçon suivante (versets 26-30) figure au manuel imprimé mais est absente du livre numérisé — les emplacements correspondants sont vides dans la source.]</p>
<ul>
<li>Je recherche les voies légales de l’acquisition de l’argent et de sa dépense.</li>
</ul>
<p>J’explicite le sens de la parole du Très-Haut :</p>
<p>« Ne porte pas ta main enchaînée à ton cou [par avarice], et ne l’étend pas non plus trop largement, sinon tu te trouveras blâmé et chagriné. » (al-Isrāʾ, 29)</p>
<ul>
<li>avec l’exposé de la finesse rhétorique qu’elle renferme.</li>
</ul>
<p>[Citation coranique (v. 29, de la leçon suivante) restaurée d’après le corpus canonique : l’emplacement imprimé est vide — perte OCR.]</p>"""


def main():
    with open(BOOK, "r", encoding="utf-8") as fh:
        d = json.load(fh)
    hit = 0
    for l in d["lessons"]:
        if l.get("docId") == "13534":
            l["htmlFr"] = HTML_FR
            hit += 1
    if hit != 1:
        raise SystemExit(f"ERREUR: {hit} leçons 13534 trouvées (attendu 1)")
    with open(BOOK, "w", encoding="utf-8") as fh:
        json.dump(d, fh, ensure_ascii=False, indent=1)
    print(f"OK — leçon 13534 upgradée main: FR {len(HTML_FR)} car")


if __name__ == "__main__":
    main()

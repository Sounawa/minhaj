#!/usr/bin/env python3
# build-13585.py — leçon 13585 « Sourate An-Nahl, versets 60-62 » (tafsir-tanawi-1, lessons[15], badge Leçon 17/32)
# Trame 13584 (R280). ZÉRO script arabe dans tout le htmlFr (auto-vérif ; U+FDFA exempté — convention du fil).
# VINGT-DEUX restaurations coraniques (cache) : bloc principal 60-62 (section vide entière, 11e cas) + 21 citations perdues
# SANS emplacement ni span (état de corruption neuf : appels perdus, étiquettes textuelles résiduelles) ;
# SEPT mots-glosses rétablis (règle (y), classe de 13537) dont 1 à caution (sāʾa) ;
# 2 lectures tranchées (mufraṭūna fatḥa / mufriṭūna kasra) ; 2 mots-glosses du fil restaurés (mā yakrahūna, al-ḥusnā) ;
# Muḥarrar original consulté en ligne (quran-tafsir.net/atia, sura16 aya60-62 — fetch 3/3 OK).
import json, os, re

FR1 = '''<h1>La sourate an-Naḥl — <em>al-Muḥarrar al-wajīz</em> d'Ibn ʿAṭiyya, versets 60 à 62</h1>
<p>Leçon de tafsīr — sourate an-Naḥl, versets (60-62) — tirée du livre <em>al-Tafsīr min khilāl al-Muḥarrar al-wajīz fī tafsīr al-Kitāb al-ʿazīz</em> d'Ibn ʿAṭiyya, au profit des élèves de la première année de l'enseignement secondaire ancien, première étape (leçon 12 du manuel — la quinzième du fil consacré au Naḥl).</p>
<ol>
<li>Me familiariser avec le sens des mots et des versets, et en déterminer les contenus.</li>
<li>Réaliser la perfection d'Allah, Gloire et pureté à Lui, le Très-Haut, et Sa transcendance au-dessus des attributs de l'imperfection.</li>
<li>Ressentir l'étendue de la miséricorde d'Allah et Sa mansuétude envers Ses serviteurs.</li>
</ol>
<h2>Introduction</h2>
<p>Lorsque Allah, le Très-Haut, a mentionné un ensemble des laideurs des associateurs et de leurs positions associationnistes — dont faisaient partie leur prétention que les anges étaient des femelles et qu'elles étaient les filles d'Allah, ainsi que leur ensevelissement des filles —, sont venues ces versets pour exposer que le pivot de leur attribution de toutes ces laideurs est leur mécréance au jour de l'au-delà, et que ce qu'ils ont attribué à Allah, le Très-Haut, d'attributs de l'imperfection, et de manifestations du besoin et de l'impuissance, est l'attribut qui leur sied à eux. Quant à Allah, le Très-Haut, à Lui appartient l'exemple suprême, et à Lui l'attribut éclatant et admirable.</p>
<p>Et les versets ont signalé la sunna d'Allah, le Très-Haut, dans l'octroi de répit aux désobéissants et aux associateurs, et le non-hâtement du châtiment, par miséricorde envers eux, dans l'espoir qu'ils se repentent et reviennent avant que ne leur vienne l'échéance qui ne s'avance ni ne retarde.</p>
<p>Quel est donc le sens du mauvais qualificatif et du qualificatif suprême cités dans les versets ? Et comment tirons-nous profit des versets pour ne point se laisser séduire par la sunna d'Allah, le Très-Haut, qui accorde du répit aux désobéissants et aux criminels ?</p>
'''

FR2 = '''<h2>Les versets</h2>
<p>Allah, le Très-Haut, a dit :</p>
<p>« (60) C'est à ceux qui ne croient pas en l'au-delà que revient le mauvais qualificatif (qu'ils ont attribué à Allah). Tandis qu'à Allah [Seul] est le qualificatif suprême. Et c'est Lui le Tout Puissant, le Sage. (61) Si Allah s'en prenait aux gens pour leurs méfaits, Il ne laisserait sur cette terre aucun être vivant. Mais Il les renvoie jusqu'à un terme fixé. Puis, quand leur terme vient, ils ne peuvent ni le retarder d'une heure ni l'avancer. (62) Et ils assignent à Allah ce qu'ils détestent [pour eux-mêmes]. Et leurs langues profèrent un mensonge quand ils disent que la plus belle récompense leur sera réservée. C'est le Feu, sans nul doute, qui leur sera réservé et ils y seront envoyés, les premiers. » (an-Naḥl, 60-62)</p>
<p>[Citation coranique (an-Naḥl, 60-62 — le bloc entier des versets de la leçon) restaurée d'après le corpus canonique et vérifiée au cache coranique du corpus : la section imprimée « Les versets » est vide dans la source numérisée, le bloc versical tout entier ayant disparu à la numérisation — perte OCR — onzième cas consécutif du fil.]</p>
<p><span>an-Naḥl : 60 - 62</span></p>
<h3>L'explication des mots</h3>
<p>[Les sept explications subsistantes de la source numérisée ne portaient AUCUN de leurs mots-glosses — les mots des versets qu'elles expliquent ayant disparu à la numérisation ; classe récurrente du fil (règle (y), déjà rencontrée en la leçon 13537) — les têtes sont rétablies par l'ordre des versets et l'appariement mot pour mot au commentaire du manuel et au <em>Muḥarrar</em> original, la sixième étant au double gloss du fil (voir plus bas) — toute identification à caution est signalée à sa place.]</p>
<ul>
<li>« le mauvais qualificatif » (<em>mathal as-sawʾ</em>) : l'attribut du mal (<em>ṣifat as-sawʾ</em>) — le groupe des exégètes lisant <em>mathal</em> au sens d'attribut.</li>
<li>« le lexème <em>sāʾa</em> » — identification restaurée à caution : l'explication subsistante porte « masdar de <em>sāʾa</em>, c'est-à-dire qu'il lui fit du mal » ; c'est le lexème que le liminaire du commentaire appelle le « jugement mauvais » (an-Naḥl, 59, la clôture : « Combien est mauvais leur jugement »), le muṣḥaf portant <em>bi-ẓulmihim</em> à l'āya 61.</li>
<li>« Il les saisit en compte » (<em>yuʾākhidhuhum</em>) : Il punit, Il rétribue.</li>
<li>« une créature » (<em>dābba</em>) : toute créature se mouvant sur la terre.</li>
<li>« un terme fixé » (<em>ajal musammā</em>) : un terme délimité pour eux.</li>
<li>« la plus belle récompense » (<em>al-ḥusnā</em>) : le Paradis.</li>
<li>« ils y seront envoyés, les premiers » (<em>al-mufraṭūna</em>) : hâtifs vers le Feu, y avançant. Et le <em>fāriṭ</em> : celui qui devance, à l'abreuvoir, ceux qui viennent s'abreuver.</li>
</ul>
<h3>L'extraction des contenus des versets</h3>
<ol>
<li>Par quoi Allah, le Très-Haut, a-t-Il qualifié ceux qui ne croient pas en l'au-delà ?</li>
<li>Explique la sagesse de la sunna d'Allah, le Très-Haut, dans l'octroi de répit aux désobéissants.</li>
<li>Qu'ont attribué les associateurs à Allah ? Et quel est leur châtiment ?</li>
</ol>
'''

FR3 = '''<h2>Le tafsīr</h2>
<p>Les versets ont comporté ce qui suit :</p>
<h3>Premièrement : Allah, le Très-Haut, informe les associateurs qu'à Lui appartient l'exemple suprême</h3>
<p>Allah, le Très-Haut, a dit :</p>
<p>« C'est à ceux qui ne croient pas en l'au-delà que revient le mauvais qualificatif (qu'ils ont attribué à Allah). » (an-Naḥl, 60 — l'ouverture)</p>
<p>[Citation coranique (an-Naḥl, 60 — l'ouverture) restaurée d'après le corpus canonique et vérifiée au cache coranique du corpus : la citation imprimée après l'appel est entièrement disparue dans la source numérisée, SANS emplacement ni span subsistant — l'état de corruption neuf de cette leçon, les appels perdus n'ayant laissé qu'un espacement résiduel — perte OCR.]</p>
<p>Autrement dit : aux associateurs qui ne croient pas au retour, à la récompense ni au châtiment revient l'attribut du mal — un attribut laid : ils ont, en effet, décrit Allah de l'imperfection et du besoin d'un enfant, alors qu'ils méritent davantage d'être décrits par cela, leur vie étant suspendue à l'enfant et à la considération pour lui s'il est mâle — et s'il est femelle, ils en dédaignent et le jettent à la terre ; et cela est un signe de leur impuissance et de leur avarice.</p>
<p>Et la parole du Très-Haut :</p>
<p>« Tandis qu'à Allah [Seul] est le qualificatif suprême. » (an-Naḥl, 60 — le milieu)</p>
<p>[Citation coranique (an-Naḥl, 60 — le milieu) restaurée d'après le corpus canonique et vérifiée au cache coranique du corpus : la citation imprimée est disparue dans la source numérisée, SANS emplacement ni span subsistant — perte OCR.]</p>
<p>Autrement dit : à Allah, le Très-Haut, appartient la description suprême, dans la perfection qui se suffit de toute imperfection ; et Lui, Gloire à Lui, est le détenteur de la puissance absolue et de la sagesse enveloppante, transcendant au-dessus de l'enfant — c'est Allah, point de divinité que Lui — et à Lui les attributs de la perfection et de la majesté, de la puissance, de la science et de la volonté, et analogue.</p>
<p>Et Sa parole :</p>
<p>« Et c'est Lui le Tout Puissant, le Sage. » (an-Naḥl, 60 — la clôture)</p>
<p>[Citation coranique (an-Naḥl, 60 — la clôture) restaurée d'après le corpus canonique et vérifiée au cache coranique du corpus : la citation imprimée est disparue dans la source numérisée, SANS emplacement ni span subsistant — perte OCR.]</p>
<p>Autrement dit : Il est l'invaincu par Sa grandeur et Sa majesté — nul ne le subjugue —, et Il est le Sage qui ne fait que ce qu'exige la sagesse consummée.</p>
<p>Un groupe a dit : le « <em>mathal</em> » dans cette āya est au sens d'attribut — c'est-à-dire : ceux-là ont l'attribut du mal, et à Allah la description la plus haute.</p>
<p>[Citation coranique (an-Naḥl, 60 — le mot « mathal », cité par le groupe d'exégètes) restaurée d'après le <em>Muḥarrar</em> original consulté en ligne (« Un groupe a dit : {mathal}, dans cette āya, au sens d'attribut ») : la citation imprimée est disparue dans la source numérisée, SANS emplacement ni span subsistant — perte OCR.]</p>
<p>Le qāḍī Abū Muḥammad Ibn ʿAṭiyya a dit : et ceci n'est pas une nécessité, car c'est une sortie hors du libellé ; bien plutôt, Sa parole est sur son bāb, à sa face même. Et cela parce que, lorsqu'ils dirent : « les filles sont à Allah », ils Lui firent une parabole, celle d'un père de filles parmi les humains — et la multitude des filles est, chez eux, blâmable et méprisable.</p>
<p>N.d.T. — L'ouverture du commentaire (« aux associateurs qui ne croient pas au retour, à la récompense ni au châtiment ») et les deux paraphrases du qualificatif suprême sont propres au manuel : le <em>Muḥarrar</em> original n'ouvre pas ainsi, mais entre directement par le gloss du groupe — « le <em>mathal</em> au sens d'attribut » — suivi du verdict du qāḍī Abū Muḥammad. Le <em>Muḥarrar</em> conserve, et le manuel tronque, la suite du verdict : le mauvais exemple est attribué aux associateurs « non pas dans les seules filles, mais dès lors qu'ils en firent le lieu de leur parabole, Allah le leur rendit en toute généralité, en tout mal — et rien ne va plus loin que le châtiment du Feu » ; le <em>Muḥarrar</em> ajoute la gloss de Qatāda — le qualificatif suprême : « pas de divinité qu'Allah » — et la parole « {et à Allah l'exemple suprême} : sur le mode de la généralité aussi, dans la perfection qui se suffit ». Le manuel expose enfin l'āya en trois appels (l'ouverture, le milieu, la clôture) là où le <em>Muḥarrar</em> ne glose que les deux premières tranches — l'expansion pédagogique est du manuel.</p>
'''

FR4 = '''<h3>Deuxièmement : la sunna d'Allah, le Très-Haut, dans l'octroi de répit aux désobéissants</h3>
<p>Lorsque Allah, le Très-Haut, eut réprimandé les associateurs d'avoir assigné les filles à Allah alors qu'ils s'en affligeaient pour eux-mêmes, et après avoir qualifié leur acte de « jugement mauvais », et après leur avoir fait connaître leur croyance la plus spécifique, à savoir qu'ils ne croient pas en l'au-delà, Il suivit cela par le warning. Il a dit, le Très-Haut :</p>
<p>« Si Allah s'en prenait aux gens pour leurs méfaits, Il ne laisserait sur cette terre aucun être vivant. Mais Il les renvoie jusqu'à un terme fixé. Puis, quand leur terme vient, ils ne peuvent ni le retarder d'une heure ni l'avancer. » (an-Naḥl, 61)</p>
<p>[Citation coranique (an-Naḥl, 61) restaurée d'après le corpus canonique et vérifiée au cache coranique du corpus : la citation imprimée après l'appel est entièrement disparue dans la source numérisée, SANS emplacement ni span subsistant — perte OCR.]</p>
<p>Allah, le Très-Haut, montre ici Sa bienveillance envers Sa création malgré leur injustice, et qu'Il leur accorde du répit à l'égard du châtiment, en manifestation de Sa grâce et de Sa miséricorde — car s'Il les saisissait en compte de ce que leurs mains ont acquis, Il ne laisserait sur le dos de la terre nulle créature. Quant à l'injuste, il sera saisi pour son injustice ; quant à l'autre, pour son infortune — comme a dit le Très-Haut :</p>
<p>« Et craignez une calamité qui n'affligera pas exclusivement les injustes d'entre vous. » (al-Anfāl, 25)</p>
<p>[Citation coranique (al-Anfāl, 25 — le tronçon de la calamité) restaurée d'après le corpus canonique et vérifiée au cache coranique du corpus, la forme du tronçon coïncidant à celle du <em>Muḥarrar</em> original : la citation imprimée est disparue dans la source numérisée, SANS emplacement ni span, l'étiquette textuelle « al-Anfāl, 25 » subsistant seule — perte OCR.]</p>
<p>mais Il, Gloire à Lui, fait miséricorde et couvre qui Il veut, et accorde du répit à qui Il veut, jusqu'à un terme dénommé.</p>
<p>Et Sa parole : « …Il ne laisserait sur elle nulle créature » (<em>min dābba</em>) — le <em>min</em> y est entré : pour l'englobement du genre tout entier. [<em>Tafsīr aṯ-Ṯaʿālibī</em>, III/429]</p>
<p>[Citation coranique (an-Naḥl, 61 — le tronçon « min dābba », appuyant la note lexicale du <em>min</em>) restaurée d'après le <em>Muḥarrar</em> original consulté en ligne (« Sa parole : {min dābba} — le min y est entré, pour l'englobement du genre ») : la citation imprimée après « et Sa parole » est disparue dans la source numérisée, un seul fragment de la glose subsistant au sein de la phrase, le reste laissé à l'espacement — perte OCR ; l'attribution imprimée au <em>Tafsīr</em> d'aṯ-Ṯaʿālibī, III/429, est conservée telle quelle.]</p>
<p>Et Sa parole : « Il les saisit en compte » — c'est la forme du concurrentiel (<em>mufāʿala</em>) de <em>akhadha</em>, comme si l'un des deux associés prenait de l'autre : Allah saisit les gens en compte de leurs désobéissances, et les créatures se saisissent l'une l'autre de la nuisance réciproque.</p>
<p>Et cette āya indique que si Allah était saisissant en compte les créatures de leur association, Il les aurait anéanties, et anéanti avec elles les bêtes — mais Il ne les a pas saisies en compte.</p>
<p>Le pronom dans « sur elle » revient à la terre : c'est une métonymie du non-mentionné, mais il est indiqué par [le fait que] la créature ne se meut que sur la terre — ou bien il n'en fut pas fait de mention pour sa renommée, l'indication à elle étant possible ; et c'est comme la parole du Très-Haut :</p>
<p>« …jusqu'à ce que [le soleil] se soit caché derrière son voile. » (Ṣād, 32)</p>
<p>[Citation coranique (Ṣād, 32 — le tronçon du voile) restaurée d'après le corpus canonique et vérifiée au cache coranique du corpus, la forme du tronçon étant celle du <em>Muḥarrar</em> original (« jusqu'à ce qu'il se cachât derrière le voile — et il n'en fut pas fait de mention pour le soleil ») : la citation imprimée est disparue dans la source numérisée, SANS emplacement ni span, l'étiquette textuelle « sūra "Ṣād", 32 » subsistant seule — perte OCR.]</p>
<p>et il n'en fut pas fait de mention pour le soleil.</p>
<p>Dans le <em>Ṣaḥīḥ</em> [d'al-Bukhārī], il fut dit au Prophète ﷺ : « Sommes-nous détruits pendant que les vertueux sont parmi nous ? » Il dit : « Lorsque le mauvais sera multiplié. » [Ṣaḥīḥ al-Bukhārī, le livre du vendredi, le chapitre de celui qui attend d'être enseveli]</p>
<p>car l'innocent est injuste envers lui-même par son silence, à ne point prodiguer le conseil, ou en marchant avec eux dans leur conduite.</p>
'''

FR5 = '''<h3>Troisièmement : les associateurs attribuent à Allah ce qu'ils détestent pour eux-mêmes</h3>
<p>Allah, le Très-Haut, a dit :</p>
<p>« Et ils assignent à Allah ce qu'ils détestent [pour eux-mêmes]. Et leurs langues profèrent un mensonge quand ils disent que la plus belle récompense leur sera réservée. C'est le Feu, sans nul doute, qui leur sera réservé et ils y seront envoyés, les premiers. » (an-Naḥl, 62)</p>
<p>[Citation coranique (an-Naḥl, 62) restaurée d'après le corpus canonique et vérifiée au cache coranique du corpus : la citation imprimée après l'appel est entièrement disparue dans la source numérisée, SANS emplacement ni span subsistant — perte OCR.]</p>
<p>Autrement dit : ces associateurs attribuent à Allah, Gloire à Lui, ce qu'ils détestent pour eux-mêmes — des filles, et des associés dans la direction —, et prétendent malgré cela qu'ils entreront au Paradis — comme tu dirais à un homme : tu désobéis à Allah et tu prétends être sauvé — cela est, avec ce que tu es, d'une atteinte lointaine. Puis Il les a jugés, après cela, au Feu.</p>
<p>Et cette attribution enveloppe deux caractéristiques des caractères de l'association : attribuer la filiation à Allah, le Très-Haut, et Lui attribuer le pire des enfants à leur vue. La première fut spécifiée par la mention en Sa parole :</p>
<p>« Et ils assignent à Allah des filles. Gloire et pureté à Lui ! Et à eux-mêmes, cependant, (ils assignent) ce qu'ils désirent (des fils). » (an-Naḥl, 57)</p>
<p>[Citation coranique (an-Naḥl, 57) restaurée d'après le corpus canonique et vérifiée au cache coranique du corpus : la citation imprimée est disparue dans la source numérisée, SANS emplacement ni span subsistant — perte OCR ; identification raisonnable soumise à caution : le verset mentionne l'assignation des filles (la filiation) avec l'allusion à leur haine, par « et à eux-mêmes ce qu'ils désirent » — la première caractéristique étant ainsi spécifiée « avec l'allusion à leur haine des filles, comme cela est venu précédemment », et la seconde par la mention explicite de la haine en l'āya 62.]</p>
<p>avec l'allusion à leur haine des filles, comme cela est venu précédemment. Et celle-ci fut spécifiée par la mention de la haine, explicitement.</p>
<p>Et le relatif peut être pour la généralité, signalant qu'ils attribuèrent à Allah des choses qu'ils détestaient pour eux-mêmes — comme l'associé dans la direction —, et des choses qu'ils n'agréeaient pas pour leurs divinités et attribuèrent à Allah, comme l'indique Sa parole, le Très-Haut :</p>
<p>« Et c'est ainsi que leurs divinités ont enjolivé à beaucoup d'associateurs le meurtre de leurs enfants » (al-Anʿām, 137)</p>
<p>[Citation coranique (al-Anʿām, 137 — le tronçon de l'embellissement du meurtre des enfants) restaurée d'après le corpus canonique et vérifiée au cache coranique du corpus : la citation imprimée est disparue dans la source numérisée, SANS emplacement ni span, l'étiquette textuelle « sūrat al-Anʿām : 137 » subsistant seule — perte OCR.]</p>
<p>Et Sa parole : « ce qu'ils détestent » : il veut dire les filles ; et « la plus belle récompense » (<em>al-ḥusnā</em>) — Muǧāhid a dit : les mâles de la progéniture — et c'est le plus conforme au sens de l'āya ; un groupe a dit : le Paradis.</p>
<p>[Citation coranique (an-Naḥl, 62 — les deux mots-glosses du fil, « mā yakrahūna » puis « al-ḥusnā ») restaurée d'après le <em>Muḥarrar</em> original consulté en ligne (« Sa parole : {mā yakrahūna} : il veut dire les filles — et le {mā} en cet endroit est, pour qui possède la raison, du genre de l'espèce… et {al-ḥusnā} — Muǧāhid et Qatāda ont dit : les mâles de la progéniture, et c'est le plus conforme au sens de l'āya ; un groupe a dit : le Paradis ») : les citations imprimées sont disparues dans la source numérisée, le fil passant du premier gloss au second sans le mot-tête subsistant — perte OCR ; le manuel omet aussi Qatāda, associé à Muǧāhid dans le <em>Muḥarrar</em> — signalé plus bas.]</p>
<p>Ibn ʿAṭiyya a dit : et ceci — la lecture du Paradis — est appuyé par Sa parole, le Très-Haut :</p>
<p>« C'est le Feu, sans nul doute, qui leur sera réservé » (an-Naḥl, 62 — le tronçon de la sentence)</p>
<p>[Citation coranique (an-Naḥl, 62 — le tronçon de la sentence) restaurée d'après le corpus canonique et vérifiée au cache coranique du corpus, la forme du tronçon coïncidant à celle du <em>Muḥarrar</em> original (« Le qāḍī Abū Muḥammad a dit : et ceci est appuyé par Sa parole : {lā jarama anna lahum an-nāra} ») : la citation imprimée après « Sa parole, le Très-Haut » est disparue dans la source numérisée, le point de clôture seul subsistant — perte OCR.]</p>
<p>Et les sept, sauf Nāfiʿ, ont lu : « <em>mufraṭūna</em> » — avec fatha du rāʾ et son allègement —, son sens : avancés vers le Feu et le châtiment ; et cela fut aussi narré de Nāfiʿ ; c'est tiré du <em>farṭ</em> de l'eau : les gens qui s'avancent vers les eaux pour raccommoder les seaux et les cuirs du puits — et de là la parole du Prophète, que la prière et la paix d'Allah soient sur lui : « Je suis votre <em>farṭ</em> au <em>ḥawḍ</em>, au bassin » [Ṣaḥīḥ al-Bukhārī, le livre des apparentements de l'atténuation, le chapitre du bassin]</p>
<p>[Citation coranique (an-Naḥl, 62 — la lecture « mufraṭūna », avec fatha du rāʾ) restaurée d'après le <em>Muḥarrar</em> original consulté en ligne : la citation imprimée après « les sept, sauf Nāfiʿ, ont lu » est disparue dans la source numérisée, SANS emplacement ni span subsistant — perte OCR ; la citation du hadith du bassin est, elle, subsistante dans la source ; le <em>Muḥarrar</em> ajoute que la lecture est celle d'al-Ḥasan, d'al-Aʿraj et des compagnons d'Ibn ʿAbbās — signalé plus bas.]</p>
<p>Et Nāfiʿ a lu, seul : « <em>mufriṭūna</em> » — avec kasra du rāʾ et son allègement — c'est-à-dire : ils dépassent la limite dans la désobéissance à Allah, le Puissant et Majestueux.</p>
<p>[Citation coranique (an-Naḥl, 62 — la lecture « mufriṭūna », avec kasra du rāʾ, celle d'Ibn Masʿūd, d'Ibn ʿAbbās, d'Abū Ruǧāʾ, de Šayba b. Niṣāḥ et de la plupart des gens de Médine, d'après le <em>Muḥarrar</em>) restaurée d'après le <em>Muḥarrar</em> original consulté en ligne : la citation imprimée après « Nāfiʿ a lu, seul » est disparue dans la source numérisée — perte OCR.]</p>
<p>Et ces versets ont signalé un dessein immense parmi les desseins que l'islam est venu réaliser et auxquels ramener la considération : le dessein de l'égalité des hommes dans la dignité humaine, dans le vivre et la vie, dans la jouissance de l'autonomie et l'affranchissement de la dépendance, de l'oppression et de la servitude. Et c'est pour cela que l'islam a combattu ce à quoi s'étaient habitués les gens de la Jāhiliyya, du mépris de la femme et de l'abaissement de sa valeur, et l'empêchement de son droit le plus noble — le droit à la vie —, où ils ensevelissaient les filles, vivantes et petites ; Allah, donc, les a interdits, et a purifié la société de cette méchante apparition.</p>
<p>N.d.T. — Le <em>Muḥarrar</em> conserve, et le manuel omet, pour ces deux āyāt, des matières amples : la citation du vers de Labīd, tiré de la <em>muʿallaqa</em>, pour illustrer la renommée permettant l'indication au non-mentionné ; l'analogie du scarabée — « le <em>juʿal</em> faillit périr par les péchés des fils d'Adam », rapportée d'aṭ-Ṭabarī ; le hadith « Allah, en vérité, fait gambler le poisson dans l'eau et l'oiseau dans l'air, par les péchés des désobéissants » ; l'épisode d'Abū Hurayra reprenant l'homme qui disait « l'injuste ne périt que lui-même » : « si — Allah fait périr, en son nid, la <em>ḥubārā</em> outarde, par les péchés des injustes » ; la spécialisation, par un groupe, du « nulle créature » aux seuls oppresseurs — avec pour argument « nulle porteuse ne porte le fardeau d'une autre » (al-Anʿām, 164) ; les lectures de « à eux » (la fatḥa de la hamza de la majorité, le sens pendants selon le <em>ğarm</em> estimé, et la kasra d'al-Ḥasan et de ʿĪsā b. ʿUmrān) ; les lectures de « le mensonge » (al-Ḥasan au sukūn de la nūn, la majorité à la kasra de la ḏāl, Muʿāḏ b. Jabal et certains Syriens à la ḍamma — sur la qualité des langues) ; les autres visages de « <em>mufraṭūna</em> » — abandonnés, laissés dans le Feu, oubliés (Saʿīd b. Ğubayr, Muǧāhid, Ibn Abī Hind), ou éloignés dans le Feu — et la lecture d'Abū Ğaʿfar b. al-Qaʿqaʿ « <em>mufarriṭūna</em> », à la kasra et à la gémination : « diminués dans l'obéissance d'Allah » ; le vers d'al-Qaṭṭāmī : « et attendez-nous avec hâte — ils furent de nos compagnons, comme se hâte le <em>farrāṭ</em> devant l'abreuveur » ; et l'appariement de la lecture au fatha aux trois groupes d'al-Ḥasan, d'al-Aʿraj et des compagnons d'Ibn ʿAbbās. La sentence du qāḍī Abū Muḥammad — « ceci est appuyé par Sa parole : le Feu, sans nul doute, leur sera réservé » — appuie la lecture du Paradis, le verset enchaînant leur prétention à la sentence du Feu.</p>
'''

FR6 = '''<h2>Le bilan</h2>
<ol>
<li>Déduis des versets les attributs de la perfection qui sont dus à Allah.</li>
<li>Quelle est la sunna d'Allah, le Très-Haut, envers les désobéissants et les gens d'injustice ?</li>
<li>Explique le jugement d'Allah, le Très-Haut, envers ceux qui attribuent à Allah des filles.</li>
</ol>
<h2>L'exploitation</h2>
<p>L'imam aš-Šanqīṭī, qu'Allah lui fasse miséricorde, a dit — à propos de la parole de Dieu — Puissant et Haut — en cette āya généreuse :</p>
<p>« Si Allah s'en prenait aux gens pour leurs méfaits, Il ne laisserait sur cette terre aucun être vivant. Mais Il les renvoie jusqu'à un terme fixé. Puis, quand leur terme vient, ils ne peuvent ni le retarder d'une heure ni l'avancer. » (an-Naḥl, 61)</p>
<p>[Citation coranique (an-Naḥl, 61 — le verset cité par aš-Šanqīṭī) restaurée d'après le corpus canonique et vérifiée au cache coranique du corpus : la citation imprimée est disparue dans la source numérisée, SANS emplacement ni span, l'étiquette textuelle « an-Naḥl : 61 » subsistant seule — perte OCR ; la teneur exacte du texte d'aš-Šanqīṭī n'étant pas conservée, le verset est rétabli au texte du muṣḥaf, la prose-paraphrase du manuel subsistant après lui.]</p>
<p>Autrement dit : si Il s'avançait sur les créatures par le châtiment, Il aurait anéanti tous ceux de la terre ; mais Il est le <em>ḥalīm</em>, qui ne se hâte pas du châtiment — car la hâte est le fait de qui craint que l'occasion ne lui échappe, et le Seigneur des cieux et de la terre, rien de ce qu'Il a voulu ne Lui échappe. Et il a mentionné ce sens en d'autres endroits, comme Sa parole, Puissant et Majestueux, en la fin de la sūrat Fāṭir :</p>
<p>« Et si Allah s'en prenait aux gens pour ce qu'ils acquièrent, Il ne laisserait à la surface [de la terre] aucun être vivant. Mais Il leur donne un délai jusqu'à un terme fixé. Puis quand leur terme viendra... (Il se saisira d'eux) car Allah est Très Clairvoyant sur Ses serviteurs. » (al-Fāṭir, 45)</p>
<p>[Citation coranique (al-Fāṭir, 45 — le verset entier, l'āya finale de la sourate) restaurée d'après le corpus canonique et vérifiée au cache coranique du corpus : la citation imprimée est disparue dans la source numérisée, SANS emplacement ni span, l'étiquette textuelle « Fāṭir : 45 » subsistant seule — perte OCR.]</p>
<p>Et Sa parole, le Très-Haut :</p>
<p>« Quel pire injuste que celui à qui on a rappelé les versets de son Seigneur et qui en détourna le dos en oubliant ce que ses deux mains ont commis? Nous avons placé des voiles sur leurs cœurs, de sorte qu'ils ne comprennent pas (le Coran), et mis une lourdeur dans leurs oreilles. Même si tu les appelles vers la bonne voie, jamais ils ne pourront donc se guider. » (al-Kahf, 57)</p>
<p>[Citation coranique (al-Kahf, 57) restaurée d'après le corpus canonique et vérifiée au cache coranique du corpus : la citation imprimée est disparue dans la source numérisée, SANS emplacement ni span, l'étiquette textuelle « al-Kahf, 57 » subsistant seule — perte OCR.]</p>
<p>— cependant Il, le Très-Haut, accorde le répit et ne néglige point, et Il a éclairci cela en d'autres endroits, comme Sa parole :</p>
<p>« Et avertis les gens du jour où le châtiment les atteindra et ceux qui auront été injustes diront: «O notre Seigneur accorde-nous un court délai, nous répondrons à Ton appel et suivrons les messagers». - N'avez-vous pas juré auparavant que vous ne deviez jamais disparaître? » (Ibrāhīm, 44)</p>
<p>[Citation coranique (Ibrāhīm, 44) restaurée d'après le corpus canonique et vérifiée au cache coranique du corpus : la citation imprimée est disparue dans la source numérisée, SANS emplacement ni span, l'étiquette textuelle « Ibrāhīm : 44 » subsistant seule — perte OCR.]</p>
<p>Et Sa parole, le Très-Haut :</p>
<p>« Et ils te demandent de hâter [la venue] du châtiment. S'il n'y avait pas eu un terme fixé, le châtiment leur serait certes venu. Et assurément, il leur viendra soudain, sans qu'ils en aient conscience. » (al-ʿAnkabūt, 53)</p>
<p>[Citation coranique (al-ʿAnkabūt, 53) restaurée d'après le corpus canonique et vérifiée au cache coranique du corpus : la citation imprimée est disparue dans la source numérisée, SANS emplacement ni span, l'étiquette textuelle « al-ʿAnkabūt : 53 » subsistant seule — perte OCR.]</p>
<p>Montre, à travers les versets, la sagesse d'Allah, le Très-Haut, dans le report du châtiment aux criminels.</p>
<p>N.d.T. — L'exploitation ne conserve de la citation d'aš-Šanqīṭī, dans la source numérisée, que les cinq étiquettes textuelles et la prose-paraphrase qui les enchaîne : aucun emplacement, aucun span, aucune mise en page citationnelle. Les cinq versets sont rétablis au texte du muṣḥaf, vérifiés au cache coranique du corpus ; les extraits exacts choisis par aš-Šanqīṭī ne sont pas conservés — le verset entier étant retenu, à l'exception du premier, qui est l'āya même que la leçon expose. La chaîne du sens demeure lisible dans la paraphrase subsistante : l'āya du Naḥl pose le <em>ḥalīm</em> qui ne se hâte pas ; la finale de Fāṭir répète le même tableau ; la sourate la Caverne montre le voilement des cœurs qui n'empêche pas le répit ; Ibrāhīm et al-ʿAnkabūt fixent le terme dénommé — Il accorde le répit, et ne néglige point.</p>
<h2>La préparation préalable</h2>
<p>Lis les versets (63-67) de la sourate an-Naḥl et réponds à ce qui suit :</p>
<ul>
<li>Explique les mots suivants :</li>
</ul>
<p>[Liste de la préparation préalable perdue à la numérisation : les cinq emplacements imprimés sous « Explique les mots suivants » sont vides dans la source numérisée — neuvième occurrence du fil ; d'après les versets 63-67 — la parole jurée par l'éternité d'Allah, l'envoi des messagers aux communautés passées, la descente du Livre pour clarifier, la croissance de la terre, le retour et la sortie, le lait et le raisin — la liste proposait vraisemblablement les mots de cette portion, mais aucun indice subsistant n'en permet le rétablissement.]</p>
<ul>
<li>Extrais des versets la preuve de la puissance d'Allah, le Très-Haut, à la résurrection.</li>
<li>Signale les versets cosmiques indiquant la puissance d'Allah et Sa grandeur.</li>
</ul>
'''

# === ASSEMBLAGE ===
html = FR1 + FR2 + FR3 + FR4 + FR5 + FR6

# Post-traitement : apostrophes droites -> courbes (convention chantier)
html = html.replace("'", "\u2019")

# Auto-vérifs pré-QA
AR = re.compile(r"[\u0600-\u06FF\u0750-\u077F\u08A0-\u08FF\uFB50-\uFDF9\uFDFB-\uFDFF\uFE70-\uFEFF]")
issues = []
if AR.search(html):
    issues.append('ARABE résiduel: ' + repr(AR.findall(html)[:5]))
if html.count('«') != html.count('»'):
    issues.append(f"guillemets non appariés: {html.count('«')}/{html.count('»')}")
if "'" in html:
    issues.append(f"apostrophes droites restantes: {html.count(chr(39))}")
for ch, name in [('\u0430', 'cyrillique'), ('\uFD3E', 'crochet ornement gauche'), ('\uFD3F', 'crochet ornement droit')]:
    if ch in html:
        issues.append(f'{name} présent')
bal = ['h1', 'h2', 'h3', 'p', 'ol', 'ul', 'li', 'em', 'span']
types = sum(1 for b in bal if f'<{b}>' in html)
n_notes = html.count('[Citation coranique') + html.count('[Liste de la préparation')
n_ndt = html.count('N.d.T.')
print(f'caractères: {len(html)}')
print(f'types de balises: {types}/9')
print(f'notes de restauration: {n_notes}')
print(f'paragraphes N.d.T.: {n_ndt}')
print(f'guillemets: {html.count("«")}/{html.count("»")}')
if issues:
    print('PROBLÈMES:')
    for i in issues:
        print(' -', i)
    raise SystemExit(1)
if len(html) < 12000:
    print('TROP COURT (< 12 000 car) — rédaction insuffisante')
    raise SystemExit(1)

out = '/home/z/my-project/tr-tmp/13585.html'
open(out, 'w').write(html)
print('écrit:', out)

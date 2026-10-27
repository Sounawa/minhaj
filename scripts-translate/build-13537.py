#!/usr/bin/env python3
# build-13537.py — leçon 13537 « Sourate An-Nahl, versets 45-50 » (tafsir-tanawi-1, lessons[11], badge Leçon 13/32)
# Trame 13527 (R277). ZÉRO script arabe dans tout le htmlFr (auto-vérif). Apostrophes droites converties.
# VINGT-NEUF restaurations coraniques (cache) : bloc principal 45-50 + 22 emplacements + 6 mots-glosses ;
# tronçons TRANCHÉS par le Muḥarrar original (quran-tafsir.net/atia, sura16 aya45-50 — fetch 6/6 OK).
# Citation d'aš-Šanqīṭī : X = ar-Raʿd 15 (double critère cache), Y = an-Naḥl 49-50.
import json, os, re

FR1 = '''<h1>La sourate an-Naḥl — <em>al-Muḥarrar al-wajīz</em> d'Ibn ʿAṭiyya, versets 45 à 50</h1>
<p>Leçon de tafsīr — sourate an-Naḥl, versets (45-50) — tirée du livre <em>al-Tafsīr min khilāl al-Muḥarrar al-wajīz fī tafsīr al-Kitāb al-ʿazīz</em> d'Ibn ʿAṭiyya, au profit des élèves de la première année de l'enseignement secondaire ancien, première étape (leçon 9 du manuel — la onzième du fil consacré au Naḥl).</p>
<ol>
<li>Me familiariser avec le sens des mots des versets et en déterminer les contenus.</li>
<li>Déduire des versets le warning d'Allah, le Très-Haut, contre les gens du mauvais complot.</li>
<li>Ressentir la grandeur d'Allah, le Très-Haut, dans la soumission à Lui de toutes les créatures.</li>
</ol>
<h2>Introduction</h2>
<p>Parmi la coutume d'Allah, le Très-Haut, dans l'appel des prophètes et des messagers, il y a que ceux qui s'opposent à leur appel et leur font la guerre soient de leurs propres peuples — ceux-là mêmes qui connaissent leur véracité et leur loyauté. C'est ainsi que le Prophète (prière et salut d'Allah sur lui) appela, à la Mecque, à son Seigneur, des années durant, éprouvant toutes les espèces et toutes les sortes de tort que lui lançaient les siens ; et le plus grave des complots auxquels le Prophète (prière et salut d'Allah sur lui) fut exposé fut la tentative de le tuer (prière et salut d'Allah sur lui). Allah fit alors descendre ces versets, porteurs d'un warning sévère, contre ces associateurs.</p>
<p>Quel est donc le warning d'Allah, le Très-Haut, contre les associateurs, que portent ces versets ? Quelles sont les preuves de la puissance d'Allah, le Très-Haut, et de Sa grandeur ? Et comment accroissons-nous, à leur égard, la crainte d'Allah, le Très-Haut, et la soumission à Lui ?</p>
'''

FR2 = '''<h2>Les versets</h2>
<p><span>La compréhension</span></p>
<p>« (45) Ceux qui complotaient des méfaits sont-ils à l'abri de ce qu'Allah les engloutisse en terre ou que leur vienne le châtiment d'où ils ne s'attendaient point ? (46) Ou bien qu'Il les saisisse en pleine activité sans qu'ils puissent échapper (au châtiment d'Allah) ? (47) Ou bien qu'Il les saisisse en plein effroi ? Mais vraiment, votre Seigneur est Compatissant et Miséricordieux. (48) N'ont-ils point vu que les ombres de toute chose qu'Allah a créée s'allongent à droite et à gauche, en se prosternant devant Allah, en toute humilité ? (49) Et c'est devant Allah que se prosterne tout être vivant dans les cieux, et sur la terre ; ainsi que les Anges qui ne s'enflent pas d'orgueil. (50) Ils craignent leur Seigneur, au-dessus d'eux, et font ce qui leur est commandé. » (an-Naḥl, 45-50)</p>
<p>[Citation coranique (an-Naḥl, 45-50 — le bloc entier des versets de la leçon) restaurée d'après le corpus canonique et vérifiée au cache coranique du corpus : la section imprimée « Les versets » est vide dans la source numérisée, le bloc versical tout entier ayant disparu à la numérisation — perte OCR.]</p>
'''

FR3 = '''<h3>L'explication des mots</h3>
<ul>
<li>« les engloutisse en terre » (<em>yakhsif</em>) : l'engloutissement (<em>al-khasf</em>) est que la terre avale celui qu'elle frappe.</li>
<li>« en pleine activité » (<em>fī taqallubihim</em>) : les mouvoir dans leurs voyages — la recherche de la subsistance par le voyage et le pâturage du bétail.</li>
<li>« en plein effroi » (<em>ʿalā takhawwuf</em>) : la diminution des biens et de ce qu'ils possèdent.</li>
<li>« s'allongent » (<em>yatafayyaʾu ẓilāluh</em>) : il penche d'un côté à l'autre, du début du jour à sa fin.</li>
<li>« en toute humilité » (<em>dākhirīn</em>) : soumis, humiliés.</li>
<li>« qui ne s'enflent pas d'orgueil » (<em>lā yastakbirūn</em>) : ils obéissent à Allah d'une obéissance totale.</li>
</ul>
<p>[Mots-glosses rétablis d'après le corpus canonique et vérifiés au cache coranique du corpus : les six explications imprimées ont subsisté dans la source numérisée, les mots qu'elles glosent avaient disparu ; ils ont été rétablis d'après l'ordre des versets et l'appariement aux gloses du <em>Muḥarrar</em> original — « l'engloutissement : que la terre avale celui qu'elle frappe, et il s'y assoit au plus bas » (an-Naḥl, 45) ; « taqallub : leurs voyages » (an-Naḥl, 46) ; « at-takhawwuf : la diminution » (an-Naḥl, 47) ; « l'égard [des ombres] est du début du jour à sa fin » (an-Naḥl, 48) ; « ad-dākhir : le soumis, l'humilié » (an-Naḥl, 48) ; l'attribution de la sixième glose à « qui ne s'enflent pas d'orgueil » (an-Naḥl, 49) demeure soumise à caution — le tronçon « et font ce qui leur est commandé » (an-Naḥl, 50) en constitue le parallèle thématique le plus proche.]</p>
<h3>L'extraction des contenus des versets</h3>
<ol>
<li>Par quoi Allah, le Très-Haut, a-t-Il menacé les associateurs de la Mecque, en punition de leur mauvais complot ?</li>
<li>Montre ce dont les versets comportent la mention comme preuves de la puissance d'Allah, le Très-Haut, et de Sa grandeur.</li>
<li>Indique le sens de la prosternation de tout ce qui est dans les cieux et la terre pour Allah, le Très-Haut.</li>
</ol>
'''

FR4 = '''<h2>Le tafsīr</h2>
<p>Les versets ont comporté ce qui suit :</p>
<h3>Premièrement : le warning d'Allah, le Très-Haut, contre les associateurs de la Mecque</h3>
<p>Allah, le Très-Haut, a dit :</p>
<p>« Ceux qui complotaient des méfaits sont-ils à l'abri de ce qu'Allah les engloutisse en terre » (an-Naḥl, 45 — l'ouverture)</p>
<p>[Citation coranique (an-Naḥl, 45 — l'ouverture du commentaire) restaurée d'après le corpus canonique et vérifiée au cache coranique du corpus : l'appel de citation imprimé est suivi immédiatement de l'exposition — « c'est-à-dire » — sans emplacement versical subsistant dans la source numérisée — perte OCR.]</p>
<p>c'est-à-dire : ceux qui ont intrigé contre le messager d'Allah, parmi les gens de la Mecque, et ont cherché à détourner ses compagnons de la foi en Allah, sont-ils à l'abri qu'Allah les atteigne d'un châtiment de Sa part, comme Il fit avec ceux des nations qui, avant eux, intrigèrent contre leurs prophètes et leurs messagers : Allah engloutit certains d'entre eux dans la terre et les anéantit de la page de l'existence, comme Il fit auparavant avec Qārūn ; Il fit venir sur d'autres un châtiment du ciel, soudain, de là d'où ils ne sentaient rien, comme Il fit avec le peuple de Lūṭ ; Il fit périr d'autres par un châtiment tandis qu'ils voyageaient sur la terre, en quête de leur subsistance ; et Il épouvanta certains d'entre eux avant de faire descendre sur eux le châtiment, comme Il fit avec Thamūd.</p>
<p>Et c'est là une menace sévère d'Allah, le Très-Haut, contre les associateurs de la Mecque, qui avaient réuni la mécréance et l'association avec Allah, le détournement du chemin d'Allah et la guerre contre Son messager (prière et salut d'Allah sur lui).</p>
<p>Et la parole du Très-Haut :</p>
<p>« ou que leur vienne le châtiment d'où ils ne s'attendaient point » (an-Naḥl, 45 — la clôture)</p>
<p>[Citation coranique (an-Naḥl, 45 — la clôture) restaurée d'après le corpus canonique et vérifiée au cache coranique du corpus : l'emplacement imprimé après l'appel de citation est vide dans la source numérisée — perte OCR.]</p>
<p>— comporte une menace accrue contre eux : le châtiment d'Allah, le Très-Haut, est proche d'eux. Il est aisé à Allah, le Très-Haut, de le faire descendre sur eux en toutes leurs conditions de la vie. Et c'est pourquoi Allah, le Très-Haut, a dit :</p>
<p>« Ou bien qu'Il les saisisse en pleine activité sans qu'ils puissent échapper (au châtiment d'Allah). » (an-Naḥl, 46)</p>
<p>[Citation coranique (an-Naḥl, 46) restaurée d'après le corpus canonique et vérifiée au cache coranique du corpus : l'appel de citation imprimé était suivi immédiatement de la glose lexicale « celui qui échappe », sans emplacement versical subsistant dans la source numérisée — perte OCR.]</p>
<p>— « celui qui échappe » (<em>al-muʿjiz</em>) : celui qu'on laisse fuir, s'enfuyant, comme si son poursuivant se trouvait dans l'impossibilité de l'atteindre.</p>
<p>Et la parole du Très-Haut :</p>
<p>« Ou bien qu'Il les saisisse en plein effroi ? » (an-Naḥl, 47 — l'ouverture)</p>
<p>[Citation coranique (an-Naḥl, 47 — l'ouverture) restaurée d'après le corpus canonique et vérifiée au cache coranique du corpus : l'emplacement imprimé après l'appel de citation est vide dans la source numérisée — perte OCR.]</p>
<p>— « at-takhawwuf » : la diminution ; ce qui est visé est que soient diminués leurs biens et leurs personnes, peu à peu, jusqu'à ce que la destruction vienne sur eux tout entière.</p>
<p>Le qāḍī Abū Muḥammad Ibn ʿAṭiyya a dit : et cette diminution, vers laquelle s'oriente le warning, comporte deux sens :</p>
<p>Le premier : qu'Il les fasse périr et fasse sortir leurs âmes sur le <em>takhawwuf</em> — c'est-à-dire en les diminuant ainsi, chose après chose — et nul ne saurait prétendre s'en croire à l'abri. Il semble que ce warning ne soit alors qu'avec le châtiment qu'ils éprouvent après la mort — sinon, c'est par là que toutes les nations ont péri. Et ceci est appuyé par la parole du Très-Haut :</p>
<p>« Mais vraiment, votre Seigneur est Compatissant et Miséricordieux. » (an-Naḥl, 47 — la clôture)</p>
<p>[Citation coranique (an-Naḥl, 47 — la clôture) restaurée d'après le corpus canonique et vérifiée au cache coranique du corpus : l'emplacement imprimé après l'appel de citation est vide dans la source numérisée — perte OCR.]</p>
<p>c'est-à-dire : ce troisième degré du warning comporte clémence, miséricorde et répit, afin que se repente celui qui se repent, et que revienne celui qui revient.</p>
<p>Le second : qu'Il saisisse par le châtiment un groupe ou une cité et en laisse une autre — et ainsi de suite, jusqu'à ce que tous périssent.</p>
'''

FR5 = '''<h3>Deuxièmement : l'information des associateurs sur la puissance d'Allah dans la soumission à Lui de toutes les créatures</h3>
<p>Allah, le Très-Haut, a dit :</p>
<p>« N'ont-ils point vu que les ombres de toute chose qu'Allah a créée s'allongent à droite et à gauche, en se prosternant devant Allah, en toute humilité ? » (an-Naḥl, 48)</p>
<p>[Citation coranique (an-Naḥl, 48 — l'ouverture du commentaire) restaurée d'après le corpus canonique et vérifiée au cache coranique du corpus : l'appel de citation imprimé est suivi immédiatement de l'exposition — « c'est-à-dire » — sans emplacement versical subsistant dans la source numérisée — perte OCR.]</p>
<p>c'est-à-dire : ces personnes qui ont intrigé les méfaits n'ont-elles pas considéré ce qu'Allah a créé comme corps subsistants, tels les arbres et les montagnes dont les ombres s'inclinent et reviennent d'une position à une autre, tantôt à droite, tantôt à gauche ? Au début du jour elles sont sur un état, puis elles se contractent, puis elles reviennent à un autre état à la fin du jour, penchant d'un côté à l'autre et d'une direction à une autre, humiliées, soumises à leur Seigneur, dociles à Sa puissance.</p>
<p>Et la parole du Très-Haut comporte deux visages :</p>
<p>« N'ont-ils point vu » — selon la lecture au tāʾ, <em>a-wa-lam taraw</em> (an-Naḥl, 48)</p>
<p>[Citation coranique (an-Naḥl, 48 — la lecture au tāʾ) restaurée d'après le corpus canonique et vérifiée au cache coranique du corpus : l'emplacement imprimé après l'appel de citation est vide dans la source numérisée — perte OCR ; le tronçon retenu est la lecture au tāʾ, <em>a-wa-lam taraw</em> — celle de Ḥamza, d'al-Kisāʾī, d'al-Ḥasan, d'al-Aʿraj et d'Abū ʿAbd ar-Raḥman, et de ʿĀṣim dans le Naḥl —, c'est elle que le <em>Muḥarrar</em> original prend pour commenter (« cela comporte deux sens, dont l'un est qu'il signifie : dis-leur, ô Muḥammad, n'avez-vous pas vu ») ; la lecture au yāʾ, <em>a-wa-lam yaraw</em> — celle d'Ibn Kathīr, de Nāfiʿ, d'Abū ʿAmr et d'Ibn ʿĀmir — est celle qu'aṭ-Ṭabarī a préférée.]</p>
<ul>
<li>Le premier : qu'il signifie : « Dis-leur, ô Muḥammad : n'avez-vous pas vu ? »</li>
<li>L'autre visage : que ce soit une adresse générale à toute la création, par laquelle le discours fut entamé plus haut.</li>
</ul>
<p>Et Sa parole :</p>
<p>« toute chose » (an-Naḥl, 48 — le tronçon de la généralité)</p>
<p>[Citation coranique (an-Naḥl, 48 — le tronçon « toute chose ») restaurée d'après le corpus canonique et vérifiée au cache coranique du corpus : l'appel de citation imprimé était suivi immédiatement de la glose « expression générale », sans emplacement versical subsistant dans la source numérisée — perte OCR.]</p>
<p>est une expression générale en tout ce que la description exige, dans Sa parole :</p>
<p>« que les ombres de toute chose qu'Allah a créée s'allongent » (an-Naḥl, 48 — le tronçon de la description)</p>
<p>[Citation coranique (an-Naḥl, 48 — le tronçon « que les ombres s'allongent ») restaurée d'après le corpus canonique et vérifiée au cache coranique du corpus : l'emplacement imprimé après l'appel de citation est vide dans la source numérisée — perte OCR.]</p>
<p>car cela est la description de tout ce sur quoi porte l'égard, en tous les êtres possédant une ombre. Et la vue dans le verset est la vue du cœur ; mais l'égard par la vue du cœur ne se fait qu'au moyen de ce que l'œil voit.</p>
<p>Et « le retour de l'ombre » (<em>fayy aẓ-ẓill</em>) : c'est son retour, à l'inverse de ce qu'elle était, à partir du passage au méridien — ainsi, depuis le moment de son lever jusqu'au moment du passage au méridien, le soleil n'est qu'à effacer l'ombre universelle antérieure à son lever ; lorsqu'il atteint le méridien, commence le retour de l'ombre universelle, qui ne cesse de croître jusqu'au couchant, où elle devient générale.</p>
<p>Et quant à l'ombre étendue du Paradis, Allah n'en a pas mentionné le retour, car elle ne revient pas après avoir disparu.</p>
<p>Et ce sur quoi porte l'égard dans ce verset est tout possesseur d'ombre, personne ou corps — les montagnes, les arbres et autres. Ce en quoi entrent les droites et les gauches n'est que l'espèce humaine ; mais la mention des droites et des gauches ici est métaphorique pour les non-humains : tu l'estimes face à une droite et à une gauche, tu l'estimes face à n'importe quelle direction que tu veux, puis tu regardes et tu le vois pencher tantôt vers la droite, tantôt vers la gauche — et cela en toutes les régions du monde.</p>
<p>Le qāḍī Abū Muḥammad Ibn ʿAṭiyya a dit : les interprètes ont divergé sur cette prosternation. Une frange a dit : c'est une prosternation d'adoration, réelle. Et aṭ-Ṭabarī a rapporté d'aaḍ-Ḍaḥḥāk qu'il a dit : lorsque le soleil passe au méridien, tout ce qui pousse ou est arbre se prosterne vers la qibla. C'est pourquoi les vertueux aimaient la prière à ce moment-là.</p>
<p>Et Mujāhid a dit : ce sont les ombres qui se prosternent, non les personnes. Et une frange, parmi eux aṭ-Ṭabarī, a dit : il a exprimé l'humilité, l'obéissance, l'inclinaison des ombres et leur rotation par la prosternation — comme on appelle « prosterné » celui qui fait signe par sa tête, en signe d'humilité, d'obéissance et d'inclinaison de la tête.</p>
'''

FR6 = '''<h3>Troisièmement : la prosternation de toutes les créatures pour Allah, le Très-Haut, et leur crainte de Lui</h3>
<p>Allah, le Très-Haut, a dit :</p>
<p>« Et c'est devant Allah que se prosterne tout être vivant dans les cieux, et sur la terre ; ainsi que les Anges qui ne s'enflent pas d'orgueil. » (an-Naḥl, 49)</p>
<p>[Citation coranique (an-Naḥl, 49 — l'ouverture du commentaire) restaurée d'après le corpus canonique et vérifiée au cache coranique du corpus : l'appel de citation imprimé est suivi immédiatement de l'exposition — « c'est-à-dire » — sans emplacement versical subsistant dans la source numérisée — perte OCR.]</p>
<p>c'est-à-dire : devant Allah se soumet ce qui est dans les cieux et ce qui est sur la terre, parmi ce qu'Il anime ; ainsi que Ses anges qui sont dans le ciel, qui ne se montrent pas orgueilleux de s'humilier et de se soumettre à Lui.</p>
<p>Et le mot « tout être vivant » (<em>dābba</em>) fut employé dans ce verset pour ce qui est doué de raison.</p>
<p>[Citation coranique (an-Naḥl, 49 — le tronçon « tout être vivant ») restaurée d'après le corpus canonique et vérifiée au cache coranique du corpus : l'emplacement imprimé après « le mot » est vide dans la source numérisée — perte OCR.]</p>
<p>Az-Zajjāj a dit : Sa parole :</p>
<p>« ce qui est dans les cieux » (an-Naḥl, 49)</p>
<p>[Citation coranique (an-Naḥl, 49 — le tronçon « ce qui est dans les cieux ») restaurée d'après le corpus canonique et vérifiée au cache coranique du corpus : l'emplacement imprimé après l'appel de citation est vide dans la source numérisée — perte OCR.]</p>
<p>embrasse les anges du ciel, ce qui est dans les nuages, et ce qui est dans l'atmosphère comme animaux. Et Sa parole :</p>
<p>« et ce qui est sur la terre comme être vivant » (an-Naḥl, 49)</p>
<p>[Citation coranique (an-Naḥl, 49 — le tronçon « et ce qui est sur la terre comme être vivant ») restaurée d'après le corpus canonique et vérifiée au cache coranique du corpus : l'emplacement imprimé après l'appel de citation est vide dans la source numérisée — perte OCR ; le <em>Muḥarrar</em> original porte ici « elle est intermédiaire [entre les deux] », que l'imprimé rend par « elle est claire ».]</p>
<p>est claire. Puis Il mentionne les anges de la terre dans Sa parole :</p>
<p>« ainsi que les Anges » (an-Naḥl, 49 — la première mention)</p>
<p>[Citation coranique (an-Naḥl, 49 — le tronçon « ainsi que les Anges », première mention) restaurée d'après le corpus canonique et vérifiée au cache coranique du corpus : l'emplacement imprimé après l'appel de citation est vide dans la source numérisée — perte OCR.]</p>
<p>Et il est possible que Sa parole :</p>
<p>« ainsi que les Anges » (an-Naḥl, 49 — la seconde mention)</p>
<p>[Citation coranique (an-Naḥl, 49 — le tronçon « ainsi que les Anges », seconde mention) restaurée d'après le corpus canonique et vérifiée au cache coranique du corpus : l'emplacement imprimé après l'appel de citation est vide dans la source numérisée — perte OCR.]</p>
<p>soit celle qui embrasse les cieux et la terre — ce qui précède n'y entrant aucun ange, n'étant que pour tous les animaux.</p>
<p>Et la parole du Très-Haut :</p>
<p>« Ils craignent leur Seigneur, au-dessus d'eux, et font ce qui leur est commandé. » (an-Naḥl, 50)</p>
<p>[Citation coranique (an-Naḥl, 50 — l'ouverture du commentaire) restaurée d'après le corpus canonique et vérifiée au cache coranique du corpus : l'appel de citation imprimé est suivi immédiatement de l'exposition — « c'est-à-dire » — sans emplacement versical subsistant dans la source numérisée — perte OCR.]</p>
<p>c'est-à-dire : ces anges et ces bêtes craignent leur Seigneur de ce qu'Il les châtierait s'ils Lui désobéissaient ; et ils font ce qu'Il leur a ordonné, accomplissant Ses droits et évitant Sa colère.</p>
<p>Et la parole du Très-Haut comporte deux sens :</p>
<p>« au-dessus d'eux » (<em>min fawqihim</em>) (an-Naḥl, 50)</p>
<p>[Citation coranique (an-Naḥl, 50 — le tronçon « au-dessus d'eux ») restaurée d'après le corpus canonique et vérifiée au cache coranique du corpus : l'emplacement imprimé était un span vide dans la source numérisée — perte OCR.]</p>
<ul>
<li>Le premier : l'élévation par laquelle Allah, le Très-Haut, est décrit — et c'est l'élévation de mesure, de grandeur, de toute-puissance et de souveraineté.</li>
<li>Le second : que « au-dessus d'eux » se rattache à « ils craignent » — c'est-à-dire : ils craignent le châtiment de leur Seigneur, de ce qui est au-dessus d'eux ; et cela parce que la coutume du châtiment des nations est venue de ce qui est au-dessus.</li>
</ul>
<p>[Citations coraniques (an-Naḥl, 50 — les tronçons « au-dessus d'eux » et « ils craignent », appelés au sein du second sens) restaurées d'après le corpus canonique et vérifiées au cache coranique du corpus : les emplacements imprimés sont absents de la source numérisée, les deux tronçons étant appelés au cœur du commentaire sans place versicale — perte OCR.]</p>
<p>Et Sa parole :</p>
<p>« et font ce qui leur est commandé » (an-Naḥl, 50 — la clôture)</p>
<p>[Citation coranique (an-Naḥl, 50 — la clôture) restaurée d'après le corpus canonique et vérifiée au cache coranique du corpus : l'emplacement imprimé après l'appel de citation est vide dans la source numérisée — perte OCR.]</p>
<p>comporte la preuve que les anges sont tenus, astreints à l'ordre et à l'interdit, et qu'ils sont entre la crainte et l'espérance. Les croyants, quant à eux, le sont selon la législation et l'obéissance ; et les autres animaux, par la soumission forcée et le décret qui les conduit à ce qui s'est accompli de l'ordre d'Allah, le Très-Haut.</p>
<p>Les versets, objet de la leçon, indiquent la réalisation du dessein de la crainte d'Allah, le Très-Haut — laquelle est la tête de l'adoration et son fondement ; cela s'obtient par le regard et la méditation sur tout ce qu'Allah a créé dans les cieux et la terre : il n'est rien dans l'univers qui ne soit soumis à Allah, le Très-Haut, prosterné devant Lui et humilié devant Sa face.</p>
'''

FR7 = '''<h2>L'évaluation</h2>
<ol>
<li>Indique les types de châtiment dont les versets ont comporté la mention, et par lesquels Allah, le Très-Haut, a menacé les associateurs.</li>
<li>Quelle est la réalité de la prosternation par laquelle Allah, le Très-Haut, a décrit toutes les bêtes et les anges ?</li>
<li>Allah, le Très-Haut, a-t-Il saisi les associateurs de la Mecque par l'un des types de châtiment mentionnés ?</li>
</ol>
'''

FR8 = '''<h2>L'exploitation</h2>
<p>L'imām aš-Šanqīṭī a dit : « Allah, le Très-Haut, a dit :</p>
<p>« Et c'est à Allah que se prosternent, bon gré mal gré, tous ceux qui sont dans les cieux et sur la terre, ainsi que leurs ombres, au début et à la fin de la journée. » (ar-Raʿd, 15)</p>
<p>[Citation coranique (ar-Raʿd, 15) restaurée d'après le corpus canonique et vérifiée au cache coranique du corpus : l'emplacement imprimé après l'appel de citation au sein de la citation d'aš-Šanqīṭī a disparu à la numérisation — perte OCR ; le verset est établi par le double critère du cache coranique : le tronçon « bon gré mal gré » et le tronçon « ainsi que leurs ombres, au début et à la fin de la journée » ne se rencontrent ensemble qu'en ce verset.]</p>
<p>Allah, le Très-Haut, expose dans ce verset noble que ceux des cieux et de la terre se prosternent devant Lui, bon gré mal gré, et que leurs ombres Lui prosternent au matin et au soir ; et Il a également mentionné la prosternation des ombres et la prosternation de ceux des cieux et de la terre dans Sa parole :</p>
<p>« Et c'est devant Allah que se prosterne tout être vivant dans les cieux, et sur la terre ; ainsi que les Anges qui ne s'enflent pas d'orgueil. Ils craignent leur Seigneur, au-dessus d'eux, et font ce qui leur est commandé. » (an-Naḥl, 49-50)</p>
<p>[Citation coranique (an-Naḥl, 49-50) restaurée d'après le corpus canonique et vérifiée au cache coranique du corpus : l'emplacement imprimé après l'appel « dans Sa parole » au sein de la citation d'aš-Šanqīṭī a disparu à la numérisation — perte OCR.]</p>
<p>Les savants ont divergé sur ce qui est visé par la prosternation de l'ombre et par la prosternation des autres que les croyants. Certains savants ont dit : la prosternation de celui qui est dans les cieux et sur la terre relève du général spécifié — les croyants et les anges se prosternent devant Allah d'une prosternation réelle, qui est le dépôt du front sur la terre, le faisant bon gré ; les mécréants se prosternent malgré eux — je veux dire les hypocrites, car ils sont mécréants intérieurement et ne se prosternent que malgré eux ; et ce qui est visé par la prosternation des musulmans, bon gré, est leur docilité à ce qu'Allah veut d'eux, bon gré ; et ce qui est visé par la prosternation des mécréants, malgré eux, est leur docilité à ce qu'Allah veut d'eux, malgré eux — car Sa volonté est exécutée en eux, et ils sont dociles, soumis à Sa besogne envers eux et à la pénétration de Sa volonté sur eux. » [Adwāʾ al-bayān d'aš-Šanqīṭī, 2/237]</p>
<p>Déduis du texte et de tes acquis de connaissance la différence entre la prosternation du croyant et celle des autres créatures.</p>
'''

FR10 = '''<h2>Notes du traducteur</h2>
<p><em>N.d.T. —</em> Leçon du fil consacré au Naḥl dont le matériau versical a disparu à la numérisation. La section imprimée « Les versets » est vide en son entier — le bloc principal (an-Naḥl, 45-50) y a été restauré. Vingt-neuf restaurations coraniques au total, d'après le corpus canonique et vérifiées au cache coranique du corpus : le bloc principal an-Naḥl 45-50 ; les vingt-deux emplacements coraniques vides du commentaire et de l'exploitation (an-Naḥl 45 l'ouverture et la clôture ; an-Naḥl 46 ; an-Naḥl 47 l'ouverture et la clôture ; an-Naḥl 48 l'ouverture, la lecture au tāʾ et les deux tronçons de la généralité et de la description ; an-Naḥl 49 l'ouverture, le mot <em>dābba</em> et les quatre tronçons du commentaire d'az-Zajjāj ; an-Naḥl 50 l'ouverture, le tronçon « au-dessus d'eux » au span vide, les deux tronçons appelés au sein du second sens, et la clôture ; ar-Raʿd 15 et an-Naḥl 49-50 au sein de la citation d'aš-Šanqīṭī) ; et les six mots-glosses de l'explication, absents de l'imprimé, rétablis d'après l'ordre des versets (l'engloutissement, l'activité, l'effroi, le penchement des ombres, l'humilité, l'absence d'orgueil) — dont une identification soumise à caution, la sixième glose.</p>
<p><em>N.d.T. —</em> Méthode : le <em>Muḥarrar al-wajīz</em> original d'Ibn ʿAṭiyya, consulté en ligne dans une édition numérique de référence (sourate 16, versets 45 à 50), a de nouveau servi d'autorité de tranchage. Les six explications de mots s'apparient mot pour mot aux gloses que le <em>Muḥarrar</em> commente (« l'engloutissement : que la terre avale celui qu'elle frappe, et il s'y assoit au plus bas » ; « <em>taqallub</em> : leurs voyages, et la tentative de gagner la vie par le voyage et le pâturage » ; « at-takhawwuf : la diminution » ; « l'égard [des ombres] est du début du jour à sa fin » ; « ad-dākhir : le soumis, l'humilié »). Le tronçon retenu pour les deux visages est la lecture au tāʾ — c'est elle que le <em>Muḥarrar</em> prend pour commenter : « cela comporte deux sens, dont l'un est qu'il signifie : dis-leur, ô Muḥammad, n'avez-vous pas vu » ; le tronçon de la généralité est « toute chose », celui de la description « que les ombres s'allongent » — le <em>Muḥarrar</em> porte nommément : « Sa parole "de toute chose" est une expression générale en tout ce que la description dans Sa parole "que les ombres s'allongent" exige ». Les quatre tronçons du commentaire d'az-Zajjāj sont établis par le <em>Muḥarrar</em> mot pour mot (« Sa parole "ce qui est dans les cieux" embrasse les anges du ciel, ce qui est dans les nuages et ce qui est dans l'atmosphère comme animaux ; et Sa parole "et ce qui est sur la terre comme être vivant" est intermédiaire ; puis Il mentionne les anges de la terre dans Sa parole "ainsi que les Anges" ; et il est possible que ce soit "ainsi que les Anges" qui embrasse les cieux et la terre, ce qui précède n'y entrant aucun ange, n'étant que pour tous les animaux »). Le span vide avant « deux sens » porte le tronçon « au-dessus d'eux » — le <em>Muḥarrar</em> : « Sa parole "au-dessus d'eux" comporte deux sens : l'un, l'élévation par laquelle Allah est décrit — élévation de mesure, de grandeur, de toute-puissance et de souveraineté ; l'autre, que "au-dessus d'eux" se rattache à "ils craignent", comme la coutume du châtiment des nations est venue de ce qui est au-dessus ». Le verset de l'exploitation est établi comme ar-Raʿd 15 par le double critère du cache coranique : le tronçon « bon gré mal gré » et le tronçon « leurs ombres, au début et à la fin de la journée » ne se rencontrent ensemble qu'en ce verset ; la citation d'aš-Šanqīṭī le nomme « ce verset noble » et y rattache nommément les versets de la leçon.</p>
<p><em>N.d.T. —</em> Les treize irrégularités de l'imprimé comptées : (1) la fente de définition vide sous le titre — dixième occurrence ; (2) la section « Les versets » vide en son entier — huitième cas consécutif du livre ; (3) les vingt-deux emplacements coraniques vides du commentaire et de l'exploitation ; (4) les six mots-glosses de l'explication absents de l'imprimé — classe nouvelle ; (5) la liste de mots de la préparation préalable perdue — trois emplacements, sixième occurrence ; (6) la corruption OCR dans la citation d'aš-Šanqīṭī : le fragment orphelin au cœur de « ceux des cieux et de la terre se prosternent devant Lui » — le relatif perdu — et « sur la terre » amputé de sa préposition ; (7) la référence bibliographique inversée « 237/2 » pour 2/237 ; (8) le tatwīl médian parasite — huitième leçon consécutive ; (9) l'écart de numérotation du manuel : l'imprimé porte « leçon 9 », la position au livre est la treizième leçon — la numérotation interne du manuel est cohérente d'une leçon à l'autre (la précédente se disait « leçon 8 ») mais décalée d'avec l'ordre de reliure du corpus numérique ; (10) l'écart de texte sur la glose d'aaḍ-Ḍaḥḥāk : l'imprimé porte « vers la qibla », le <em>Muḥarrar</em> original « avant la qibla » ; (11) les lectures divergentes attestées par le <em>Muḥarrar</em> et non reproduites par l'imprimé : <em>a-wa-lam yaraw</em> au yāʾ — celle qu'aṭ-Ṭabarī a préférée — contre <em>a-wa-lam taraw</em> au tāʾ, et <em>tatafayyaʾ</em> par Abū ʿAmr seul contre le <em>yatafayyaʾ</em> de la majorité ; (12) les contenus substantiels du <em>Muḥarrar</em> absents de l'imprimé : l'avis de Mujāhid identifiant « ceux qui ont intrigé » à Nimrod ; les deux régimes syntaxiques de « les méfaits », le second rapporté à Qatāda ; le récit des gens de cette communauté engloutis après leur dispute de l'imamat ; l'anecdote de ʿUmar sur le sens d'at-takhawwuf avec les vers d'Ibn Muqbil, de Ṭarafa et d'an-Nābigha ; l'avis de la frange qui fait d'at-takhawwuf « la crainte », réfuté par Ibn ʿAṭiyya (« affectation ») ; l'avis de la frange qui entend les ombres comme « les personnes elles-mêmes » ; les divergences sur l'orientation de l'ombre — Qatāda et Ibn Jurayj, puis Ibn ʿAbbās — et le jugement d'Ibn ʿAṭiyya sur l'ensemble (« tout cela est plausible, non explicite ») ; (13) les résidus de fermeture du corps et le paragraphe vide sous le titre. Signalés NON comptés : l'expansion pédagogique du manuel sur les anges tenus à l'ordre et à l'interdit, entre crainte et espérance — absente du <em>Muḥarrar</em> en cet endroit ; les exemples de Qārūn, du peuple de Lūṭ et de Thamūd, développements du manuel sans équivalent au <em>Muḥarrar</em>, qui ne cite que l'engloutissement général des nations antérieures ; la préparation préalable cible les versets 51-56, dont la matière est déjà parue au fil du livre ; la marque d'en-tête « La compréhension », conservée entre la section des versets et l'explication des mots.</p>
<p><em>N.d.T. —</em> Les versions françaises des versets sont reprises du cache coranique du corpus ; les numéros de versets entre parenthèses ont été insérés au bloc principal selon la convention du fil ; les guillemets internes de la version du cache ont été conservés tels quels. La version du cache rend l'expression de l'engloutissement par « les engloutisse en terre », l'expression de l'effroi par « en plein effroi », et le terme de l'humilité par « en toute humilité ». La version d'ar-Raʿd 15 rend « al-ghudūw wa-l-āṣāl » par « au début et à la fin de la journée », que le propre texte d'aš-Šanqīṭī rend par « au matin et au soir ». Les emplacements des versets de la préparation préalable (51-56) n'ont pas été remplis — la leçon de préparation porte sur des versets dont la matière figure déjà au registre.</p>
'''

FR9 = '''<h2>La préparation préalable</h2>
<p>Lis les versets (51 à 56) de la sourate an-Naḥl et réponds à ce qui suit :</p>
<ul>
<li>Explique les mots suivants :</li>
</ul>
<p>[La liste des mots imprimée a disparu à la numérisation : trois emplacements vides subsistent dans la source ; les expressions relevaient des versets (51-56) de la sourate an-Naḥl, dont la matière est déjà parue au fil du livre — la leçon sur les versets (51-58) est déjà au registre du corpus — non reconstituée.]</p>
<ul>
<li>Extrais ce dont les versets ont comporté la mention d'ordres et d'interdits.</li>
<li>Déduis des versets comment peut se réaliser le monothéisme pur pour Allah, le Très-Haut.</li>
</ul>
'''

# === ASSEMBLAGE ===
html = FR1 + FR2 + FR3 + FR4 + FR5 + FR6 + FR7 + FR8 + FR9 + FR10

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
n_notes = html.count('[Citation coranique') + html.count('[Mots-glosses')
print(f'caractères: {len(html)}')
print(f'types de balises: {types}/9')
print(f'notes de restauration: {n_notes}')
print(f'guillemets: {html.count("«")}/{html.count("»")}')
if issues:
    print('PROBLÈMES:')
    for i in issues:
        print(' -', i)
    raise SystemExit(1)
if len(html) < 12000:
    print('TROP COURT (< 12 000 car) — rédaction insuffisante')
    raise SystemExit(1)

out = '/home/z/my-project/tr-tmp/13537.html'
open(out, 'w').write(html)
print('écrit:', out)

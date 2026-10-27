#!/usr/bin/env python3
# build-13587.py — leçon 13587 « Sourate An-Nahl, versets 68-70 » (tafsir-tanawi-1, lessons[17], badge Leçon 19/32)
# Trame 13585 (R281). ZÉRO script arabe dans tout le htmlFr (auto-vérif ; U+FDFA exempté — convention du fil).
# ONZE restaurations coraniques (cache) : bloc principal 68-70 (section vide entière, 12ᵉ cas) + 10 emplacements vides
# du commentaire (dont la question 4 du bilan, identification à caution) ; SIX mots-têtes rétablis (règle (y), 3ᵉ occurrence)
# dont 1 à caution (les demeures) ; DEUX hadiths subsistants INTACTS (rareté favorable du fil) ;
# OCR « االعسل » tranché → « العسل » ; Muḥarrar original consulté en ligne (quran-tafsir.net/atia, sura16 aya68-70 — fetch 3/3 OK).
import json, os, re

FR1 = '''<h1>La sourate an-Naḥl — <em>al-Muḥarrar al-wajīz</em> d'Ibn ʿAṭiyya, versets 68 à 70</h1>
<p>Leçon de tafsīr — sourate an-Naḥl, versets (68-70) — tirée du livre <em>al-Tafsīr min khilāl al-Muḥarrar al-wajīz fī tafsīr al-Kitāb al-ʿazīz</em> d'Ibn ʿAṭiyya, au profit des élèves de la première année de l'enseignement secondaire ancien, première étape (leçon 14 du manuel — la dix-septième du fil consacré au Naḥl).</p>
<ol>
<li>Me familiariser avec le sens des mots des āyāt, et en déterminer les contenus.</li>
<li>Exposer les preuves de la puissance d'Allah, le Très-Haut, dans la création de l'abeille.</li>
<li>Conscientiser la valeur de la vie et la sagesse d'Allah dans la diversité des âges.</li>
</ol>
<h2>Introduction</h2>
<p>Après que les āyāt de la leçon précédente ont signalé quelques-uns des signes cosmiques d'Allah et leur effet sur l'homme, et ce qu'Allah y a déposé de graces, elles ont suivi cela par l'exposé d'un autre signe parmi Ses signes, et d'une manifestation parmi les manifestations de Sa puissance : le signe de la création de l'abeille et de Son inspiration à elle, quant à la manière de gérer ses affaires dans la vie. De même, les āyāt ont attiré l'attention sur l'exposé de la sunna d'Allah, le Très-Haut, dans la diversité des âges, de la mort et de la vie, et la sagesse d'Allah, le Très-Haut, en tout cela.</p>
<p>Quelles sont donc les manifestations de la grandeur d'Allah dans la création de l'abeille et Son inspiration à son égard ? Et quelle est la sagesse de la sunna d'Allah dans la diversité des échéances et des âges ? Et comment tirons-nous profit des āyāt pour affermir notre foi en Allah, le Très-Haut ?</p>
'''

FR2 = '''<h2>Les versets</h2>
<p>Allah, le Très-Haut, a dit :</p>
<p>« [Et voilà] ce que ton Seigneur révéla aux abeilles : "Prenez des demeures dans les montagnes, les arbres, et les treillages que [les hommes] font. Puis mangez de toute espèce de fruits, et suivez les sentiers de votre Seigneur, rendus faciles pour vous. De leur ventre, sort une liqueur, aux couleurs variées, dans laquelle il y a une guérison pour les gens. Il y a vraiment là une preuve pour des gens qui réfléchissent. Allah vous a créés ! Puis Il vous fera mourir. Tel parmi vous sera reconduit jusqu'à l'âge le plus vil, de sorte qu'après avoir su, il arrive à ne plus rien savoir. Allah est, certes, Omniscient et Omnipotent. » (an-Naḥl, 68-70)</p>
<p>[Citation coranique (an-Naḥl, 68-70 — le bloc entier des versets de la leçon) restaurée d'après le corpus canonique et vérifiée au cache coranique du corpus : la section imprimée « Les versets » est vide dans la source numérisée, le bloc versical tout entier ayant disparu à la numérisation — perte OCR — douzième cas consécutif du fil.]</p>
<p><span>an-Naḥl : 68 - 70</span></p>
<h3>L'explication des mots</h3>
<p>[Les six explications subsistantes de la source numérisée ne portaient AUCUN de leurs mots-têtes — les mots des versets qu'elles expliquent ayant disparu à la numérisation ; classe récurrente du fil (règle (y), déjà rencontrée aux leçons 13537 et 13585) — les têtes sont rétablies par l'ordre des versets et l'appariement mot pour mot au commentaire du manuel et au <em>Muḥarrar</em> original consulté en ligne, la seconde étant à caution (voir sa place) — toute identification à caution est signalée.]</p>
<ul>
<li>« et Il révéla » (<em>wa-aḥā</em> — le lexème de la révélation, <em>al-waḥy</em>) : c'est-à-dire « et Il inspira ». La révélation est ce qu'Allah, le Très-Haut, crée d'initiative dans le cœur, sans cause apparente.</li>
<li>« des demeures » (<em>buyūtan</em>) — identification restaurée à caution : sans le mot-tête subsistant, l'appariement s'appuie sur l'ordre des versets et le sens ; l'explication subsistante porte « elles bâtissent avec les branches des arbres et leurs ramilles » — la paraphrase décrivant le bâtir des demeures au moyen des branches.</li>
<li>« ce qu'elles forment en treille » (<em>yaʿrišūna</em>) : on dit <em>ʿaraša yaʿriš</em> — il préparait, il aménagea.</li>
<li>« les sentiers de ton Seigneur » (<em>subula rabbiki</em>) : chemine sur les voies de ton Seigneur pour chercher la subsistance en tout lieu.</li>
<li>« rendus faciles » (<em>ḏululan</em>) : docile, aisée dans ses passages.</li>
<li>« l'âge le plus vil » (<em>arḏal al-ʿumri</em>) : la période de la sénescence et de la vieillesse.</li>
</ul>
<h3>L'extraction des contenus des versets</h3>
<ol>
<li>Montre la belle œuvre d'Allah dans la création de l'abeille.</li>
<li>Quelles sont les choses qu'Allah a révélées à l'abeille ?</li>
<li>Éclaircis la sagesse de la sunna d'Allah dans la diversité des échéances et des âges.</li>
</ol>
'''

FR3 = '''<h2>Le tafsīr</h2>
<p>Les āyāt ont comporté ce qui suit :</p>
<h3>Premièrement : la belle œuvre d'Allah dans la création de l'abeille</h3>
<p>La belle œuvre d'Allah et Son inimitabilité dans la création de l'abeille se manifestent à travers Son inspiration à elle d'accomplir les choses suivantes :</p>
<p>— L'inspiration d'Allah à l'abeille de prendre ses demeures des montagnes, des arbres et des treilles : Allah, le Très-Haut, a dit :</p>
<p>« [Et voilà] ce que ton Seigneur révéla aux abeilles : "Prenez des demeures dans les montagnes, les arbres, et les treillages que [les hommes] font." » (an-Naḥl, 68)</p>
<p>[Citation coranique (an-Naḥl, 68) restaurée d'après le corpus canonique et vérifiée au cache coranique du corpus : la citation imprimée après l'appel est entièrement disparue dans la source numérisée, SANS emplacement ni span subsistant — perte OCR.]</p>
<p>Autrement dit : Allah, le Très-Haut, a inspiré l'abeille par une révélation d'inspiration et de facilitation, afin qu'elle prenne ses demeures de ces trois types : soit des montagnes, soit des arbres, soit de ce que les gens forment en treille — les treillis <em>ǧibāḥ</em> et leurs semblables.</p>
<p>Et Sa parole : « et Il révéla » — le lexème de la révélation (<em>al-waḥy</em>) : la révélation, dans la langue, est la jauge du sens de la part de celui qui révèle vers celui à qui il est révélé, dans le secret. Parmi cela : la révélation aux prophètes par la mission de l'ange ; parmi cela la révélation du songe ; parmi cela la révélation au sens de l'ordre ; et parmi cela la révélation au sens de l'inspiration (<em>ilhām</em>) — c'est celle-ci en cette āya, à l'accord des exégètes.</p>
<p>[Citation coranique (an-Naḥl, 68 — le lexème de la révélation, <em>al-waḥy</em>, au cœur de « et Il révéla ») restaurée d'après le <em>Muḥarrar</em> original consulté en ligne (« Sa parole : {et ton Seigneur révéla aux abeilles} — l'āya — la révélation, dans la langue des Arabes, est la jauge du sens... et la révélation aussi au sens de l'ordre ») : la citation imprimée après « et Sa parole » est disparue dans la source numérisée, SANS emplacement ni span subsistant — perte OCR.]</p>
<p>Et Sa parole, le Très-Haut : « et ce qu'ils forment en treille » — on dit <em>ʿaraša yaʿriš</em>, avec kasra du rāʾ et sa ḍamma ; son sens : il prépara. Et il est la plupart du temps employé pour ce qui vient de la perfection des rameaux et du bois, et l'agencement de leur ombre. De là le <em>ʿarīš</em> qui fut dressé pour le Messager d'Allah ﷺ au jour de Badr.</p>
<p>[Citation coranique (an-Naḥl, 68 — le mot « yaʿrišūna ») restaurée d'après le <em>Muḥarrar</em> original consulté en ligne (« et "ʿaraš" son sens est : il prépara, et il est la plupart du temps employé pour ce qui vient de la perfection des rameaux et du bois, et l'agencement de leur ombre — de là lʿarīš qui fut dressé pour le Messager d'Allah, que la prière et la paix d'Allah soient sur lui, au jour de Badr ») : la citation imprimée après « Sa parole, le Très-Haut » est disparue dans la source numérisée, SANS emplacement ni span subsistant — perte OCR.]</p>
<p>— L'inspiration d'Allah à l'abeille de manger de tous les fruits : Allah, le Très-Haut, a dit :</p>
<p>« Puis mangez de toute espèce de fruits, et suivez les sentiers de votre Seigneur, rendus faciles pour vous. » (an-Naḥl, 69 — l'ouverture)</p>
<p>[Citation coranique (an-Naḥl, 69 — l'ouverture) restaurée d'après le corpus canonique et vérifiée au cache coranique du corpus : la citation imprimée après l'appel est entièrement disparue dans la source numérisée, SANS emplacement ni span subsistant — perte OCR.]</p>
<p>Ceci est de l'inspiration d'Allah pour l'abeille : qu'elle mange de tous les fruits, de leur doux et de leur amer ; et qu'elle parcoure toutes les voies qu'Allah lui a facilitées, afin de quêter les fruits et les fleurs — de sorte qu'aucune voie ne lui soit rude, quelque difficile qu'elle soit, et qu'elle ne s'égare point sur le chemin au retour, fussent les distances très lointaines.</p>
<p>Et Sa parole, le Très-Haut :</p>
<p>« De leur ventre, sort une liqueur, aux couleurs variées, dans laquelle il y a une guérison pour les gens. » (an-Naḥl, 69 — le milieu)</p>
<p>[Citation coranique (an-Naḥl, 69 — le milieu) restaurée d'après le corpus canonique et vérifiée au cache coranique du corpus : la citation imprimée après l'appel est entièrement disparue dans la source numérisée, SANS emplacement ni span subsistant — perte OCR.]</p>
<p>Ceci est un dénombrement de la part d'Allah, le Très-Haut, de la grâce, et une mise en garde sur l'exemple. Et la multitude des gens est sur ce que le miel sort des bouches des abeilles. Et le miel fut nommé « boisson » parce qu'il se boit avec l'eau et avec d'autres choses. Et le fait qu'il soit de couleurs variées — c'est-à-dire qu'il en existe de blanc, de jaune et de rouge — est dû à la variété de ce qui est mangé des fruits, de leur nūr et de leurs fleurs, selon la variété des abeilles et des pâturages — comme le goût du miel varie selon la variété des lieux : il en est de doux et d'amer.</p>
<p>Et les gens ont pris connaissance, en ce siècle, au moyen des moyens modernes de photographie, des merveilles de la puissance d'Allah, le Très-Haut, dans l'affaire de l'abeille : l'abeille aspire le nectar des fleurs ; il descend et se rassemble dans un sac au sein de son ventre ; puis il se mêle d'une sécrétion spéciale et se transforme en miel ; puis l'abeille revient à la ruche et sécrète le miel de sa bouche, dans les cellules de cire destinées au stockage du miel ; et chaque fois qu'une cellule s'emplit, elle la couvre d'une couche de cire, et passe à une autre demeure.</p>
<p>Et Sa parole : « dans laquelle il y a une guérison pour les gens » : le pronom revient au miel. Et la multitude est sur ce que le discours ne requiert pas la généralité en toute maladie et en tout homme ; mais c'est une information selon laquelle il guérit, comme guérissent d'autres remèdes, en certaines maladies sans d'autres. La portée de l'āya est donc une information mettant en évidence le fait qu'il est un remède.</p>
<p>[Citation coranique (an-Naḥl, 69 — le tronçon de la guérison) restaurée d'après le corpus canonique et vérifiée au cache coranique du corpus : la citation imprimée après « et Sa parole » est disparue dans la source numérisée, SANS emplacement ni span subsistant — perte OCR.]</p>
'''

FR4 = '''<p>Il nous fut rapporté d'Abū Saʿīd al-Khuḍrī — qu'Allah l'agrée — qu'un homme vint trouver le Prophète ﷺ et dit : « Mon frère a le ventre relâché ». Le messager d'Allah ﷺ dit : « Fais-le boire de miel ». Il le fit boire. Puis il revint et dit : « Je lui ai fait boire du miel, mais cela n'a fait qu'accentuer son relâchement ». Il lui dit cela trois fois — puis il vint une quatrième fois, et il lui dit : « Fais-le boire de miel » — et il répondit : « Je lui ai fait boire, mais cela n'a fait qu'accentuer son relâchement ». Le messager d'Allah ﷺ dit : « Allah a dit vrai, et le ventre de ton frère a menti ». Il le fit boire, et il fut guéri. [Ṣaḥīḥ Muslim, le livre de la paix, le chapitre du traitement par l'abreuvement de miel]</p>
<p>Et al-Bukhārī rapporte d'Ibn ʿAbbās — qu'Allah les agrée — que le Messager d'Allah ﷺ a dit : « Le remède est en trois choses : dans l'entaille de la ventouse, dans une gorgée de miel, ou dans une cautérisation au feu — et moi j'interdis à ma communauté la cautérisation ». [Ṣaḥīḥ al-Bukhārī, le livre de la médecine, le chapitre du remède en trois]</p>
<p>Et Sa parole, le Très-Haut :</p>
<p>« Il y a vraiment là une preuve pour des gens qui réfléchissent. » (an-Naḥl, 69 — la clôture)</p>
<p>[Citation coranique (an-Naḥl, 69 — la clôture) restaurée d'après le corpus canonique et vérifiée au cache coranique du corpus : la citation imprimée après l'appel est entièrement disparue dans la source numérisée, SANS emplacement ni span subsistant — perte OCR.]</p>
<p>Autrement dit : il y a, dans ce qui fut mentionné de l'affaire de l'abeille, une indication claire sur la puissance d'Allah, le Très-Haut, et la perfection de Sa belle œuvre, pour qui réfléchit à l'affaire de l'abeille et médite son étonnant ordre.</p>
<h3>Deuxièmement : la sagesse d'Allah dans la mort et la vie, et la diversité des âges des serviteurs</h3>
<p>Allah, le Très-Haut, a dit :</p>
<p>« Allah vous a créés ! Puis Il vous fera mourir. Tel parmi vous sera reconduit jusqu'à l'âge le plus vil, de sorte qu'après avoir su, il arrive à ne plus rien savoir. » (an-Naḥl, 70 — l'ouverture)</p>
<p>[Citation coranique (an-Naḥl, 70 — l'ouverture) restaurée d'après le corpus canonique et vérifiée au cache coranique du corpus : la citation imprimée après l'appel est entièrement disparue dans la source numérisée, SANS emplacement ni span subsistant — perte OCR.]</p>
<p>Allah, le Très-Haut, expose en cette āya la perfection de Sa puissance, qui se manifeste dans la création de l'homme après qu'il n'était rien de mentionné ; et que Lui, Gloire et transcendance à Lui, tient en Sa main la vie de ce dernier — Il est, seul, capable de le faire mourir et de saisir son âme —, et capable de prolonger son âge jusqu'à parvenir à la fin de l'âge, où il grisonne et vieillit.</p>
<p>Et l'exemple, en ce grand tableau parmi les tableaux de la puissance d'Allah, est que cet homme ne sied point à lui de s'enorgueillir contre son Maître, ni de s'immiscer dans son aveuglement et son désir — car sa vie et sa mort sont dans la main d'Allah, et son ordre retourne à Allah.</p>
<p>Et l'âge le plus vil n'est pas confiné à une durée déterminée : maint homme est fils de cinquante années et se trouve dans l'âge le plus vil ; et maint homme est fils de cent-vingt années et n'y est point.</p>
<p>Et Sa parole, le Très-Haut :</p>
<p>« Allah est, certes, Omniscient et Omnipotent. » (an-Naḥl, 70 — la clôture)</p>
<p>[Citation coranique (an-Naḥl, 70 — la clôture) restaurée d'après le corpus canonique et vérifiée au cache coranique du corpus : la citation imprimée après l'appel est entièrement disparue dans la source numérisée, SANS emplacement ni span subsistant — perte OCR.]</p>
<p>Autrement dit : Allah est savant de ce qu'Il fait en Sa création, selon ce qu'exige Sa sagesse ; et Il est puissant — rien ne Lui fait défaut.</p>
<p>Et ces āyāt signalent l'exposé de la faveur d'Allah, le Très-Haut, envers Ses serviteurs par les graces variées qu'Allah, le Très-Haut, a dénombrées pour l'homme et sa jouissance des fruits de l'univers ; et ce dénombrement contient l'induction des manifestations de la puissance d'Allah, Gloire à Lui, et l'affirmation de Son existence et de Son unicité — car la création des graces et des autres actes émanant de l'homme n'est que d'Allah, le Très-Haut, non des idoles ni des tyrans des simulacres et des objets d'adoration à côté d'Allah : ils sont créés, non créateurs, et impuissants à quoi que ce soit de l'invention et de la création.</p>
<p>N.d.T. — Pour l'āya 70, le <em>Muḥarrar</em> conserve, et le manuel omet : la portée d'ouverture — « ceci est une mise en garde sur l'exemple dans notre existence après le néant, et notre mort après cela, puis il s'interrompt par celui des gens qui l'annule, car ils sont le lieu de l'exemple » ; la gloss de l'âge le plus vil — « sa fin où les sens se corrompent et où la parole s'embrouille » — avec la discussion de la spécialisation de la vileté à la vieillesse, l'enfance étant « le commencement », les espérances « y étant fermes » ; la prétention rapportée d'ʿAlī — « le premier de l'âge le plus vil est soixante-quinze ans » — tempérée par le qāḍī Abū Muḥammad : « ceci est dans le plus grand nombre, et cela ne se confine pas à une durée déterminée — c'est selon l'homme, homme par homme » ; la lecture du <em>lām</em> de « afin que » comme <em>lām</em> de la conversion — « que son ordre devienne, après la science des choses, tel qu'il ne sache rien » —, sa modération : « ceci est l'expression de la rareté de sa science, non qu'il ne sache rien du tout », et la remarque que le <em>lām</em> « peut être superflu » ; la clôture du passage — « puis le Très-Haut a établi Sa science et Sa puissance, qui ne se transforment point, que les accidents ne portent pas, et qui ne changent pas » ; et la note lexicale du retour à la vileté — « on dit : Allah courbe quelqu'un dans l'âge : Il prolonge son âge jusqu'à l'âge le plus vil, et il retourne à l'état de l'enfance en faiblesse et en impuissance » — appuyée du vers « de qui Nous prolongeons la vie, Nous courbons la création », que la note présente comme du Descendement alors que le muṣḥaf ne le porte pas (vérifié au cache coranique du corpus — vers de la poésie ancienne en réalité) : le tout absent du manuel.</p>
<p>N.d.T. — Le <em>Muḥarrar</em> conserve, et le manuel omet, des matières amples pour ces trois āyāt : la lecture de Yaḥyā b. Waththāb « vers l'abeille » à la fatha du ḥāʾ, avec l'<em>an</em> explicatif ; les trois types de demeures précisés au <em>Muḥarrar</em> — « les montagnes et leurs creux, l'intérieur creusé des arbres, et ce que le fils d'Adam forme en treille des <em>ǧibāḥ</em>, les treillis et leurs semblables » — accompagnées de la note lexicale du <em>ǧabaḥ</em> (« le lieu où l'abeille prend miel quand il n'est pas façonné », avec le vers du Ṭarmaḥ) ; les lectures de « qu'ils forment en treille » — Ibn ʿĀmir à la ḍamma, la multitude à la kasra, le désaccord d'ʿĀṣim, et Abū ʿAbd ar-Raḥmān avec ʿUbayd b. Naḍla à la ḍamma ; l'opinion d'Ibn Zayd — « ce qu'ils forment en treille » : les vignes — et celle d'aṭ-Ṭabarī — « ce qu'ils bâtissent des toits » — tranchée par le qāḍī Abū Muḥammad : « et ceci, des deux, est une interprétation non maîtrisée » ; pour l'āya 69, la distinction des sens de « rendus faciles » — docilité de l'essaim ou aplanissement des voies, selon Qatāda et Muǧāhid — avec le verset de Yā-Sīn lu par Ibn Zayd (« Ne voient-ils pas que Nous avons créé pour eux des bêtes, de ce que Nos mains ont façonné — elles leur sont soumises, et Nous les leur avons rendues dociles ; d'elles ils montent, et d'elles ils mangent ») ; la parole de ʿAlī — « le plus noble des vêtements pour le fils d'Adam en ce monde est la bave du ver, et le plus noble de ses breuvages est le jus de l'abeille » — appuyant la sortie du miel hors des bouches ; l'histoire de Zaynab — « son abeille a but lʿurfuṭ quand il compara son haleine à celle du <em>maġāfīr</em> » et le hadith du Maghāfīr consigné dans le <em>Ṣaḥīḥ</em> d'al-Bukhārī ; le traitement d'Ibn ʿUmar par le miel en toute maladie ; la lecture de Muǧāhid — le pronom au Coran — et celle explicite « une guérison pour les gens », sur laquelle le qāḍī Abū Muḥammad remarque qu'elle « requiert qu'il voie la guérison en universalité » ; et l'anecdote des gens de l'ignorance prétendant que l'āya visait les gens de la maison — au conseil d'al-Manṣūr Abū Jaʿfar l'Abbasside, où la sottise de la prétention fut exposée. L'expansion pédagogique du manuel sur la photographie moderne du cycle du miel est une addition du manuel absente du <em>Muḥarrar</em> — signalée non comptée.</p>
'''

FR5 = '''<h2>Le bilan</h2>
<ol>
<li>Quel est le sens de la révélation (<em>waḥy</em>) mentionnée dans les āyāt ?</li>
<li>Déduis des āyāt les preuves de la puissance d'Allah, le Très-Haut, dans la création de l'abeille et Son inspiration à son égard.</li>
<li>Montre la sunna d'Allah, le Très-Haut, dans la vie et la mort, et la diversité des âges.</li>
<li>Qu'en retires-tu de Sa parole, le Très-Haut :</li>
</ol>
<p>« Tel parmi vous sera reconduit jusqu'à l'âge le plus vil, de sorte qu'après avoir su, il arrive à ne plus rien savoir. » (an-Naḥl, 70 — le tronçon de l'âge le plus vil)</p>
<p>[Citation coranique (an-Naḥl, 70 — le tronçon de l'âge le plus vil, cité par la question 4 du bilan) restaurée d'après le corpus canonique et vérifiée au cache coranique du corpus : la citation imprimée après « de Sa parole » est disparue dans la source numérisée, SANS emplacement ni span subsistant — perte OCR ; identification raisonnable soumise à caution : la question suivant immédiatement celle sur la sunna d'Allah dans la vie et la mort et la diversité des âges, le tronçon retenu est celui de l'âge le plus vil — la leçon en ayant, précisément, exposé le dessein.]</p>
<h2>L'exploitation</h2>
<p>L'imam al-Ghazālī, qu'Allah lui fasse miséricorde, a dit :</p>
<p>« Regarde l'abeille, comment Allah lui a révélé, si bien qu'elle a pris des demeures dans les montagnes. Puis, si tu contemples les merveilles de son affair — sa saisie des fleurs et des éclats, son évitement des impuretés et des souillures, son obéissance à l'un d'entre eux, le plus grand d'entre eux en personne, qui est son émir —, puis ce qu'Allah a soumis à son émir d'équité et de justice parmi elles, au point qu'il tue, à la porte de la sortie, toute celle qui toucha à une impureté — alors tu contemples, si tu es clairvoyant sur toi-même, et détaché du souci de ton ventre, de ta partie honteuse, et des passions de ton âme, l'hostilité envers tes associés et l'alliance envers tes frères. » [Iḥyāʾ ʿulūm ad-dīn d'al-Ghazālī, avec retouche, IV/319]</p>
<p>Montre, à travers le texte et tes acquis antérieurs, quelques aspects de la grandeur dans la création de l'abeille par Allah.</p>
'''

FR6 = '''<h2>La préparation préalable</h2>
<p>Lis les āyāt (71-74) de la sourate an-Naḥl et réponds à ce qui suit :</p>
<ul>
<li>Explique les mots suivants :</li>
</ul>
<p>[Liste de la préparation préalable perdue à la numérisation : les cinq emplacements imprimés sous « Explique les mots suivants » sont vides dans la source numérisée — dixième occurrence du fil ; d'après les versets 71-74 — la préférence dans la subsistance, les épouses et les enfants, le mariage entre les serviteurs, les bonnes choses, la foi au faux et le reniement de la grâce d'Allah — la liste proposait vraisemblablement les mots de cette portion, mais aucun indice subsistant n'en permet le rétablissement.]</p>
<ul>
<li>Extrais des versets les graces dont Allah, le Très-Haut, a fait le rappel.</li>
<li>Montre comment Allah, le Très-Haut, a réprimandé les associateurs pour l'adoration des idoles et des simulacres.</li>
</ul>
<p>N.d.T. — État de la source numérisée de cette leçon : la section « Les versets » est vide entière — douzième cas consécutif du fil ; dix emplacements coraniques du commentaire sont perdus sans emplacement ni span, à l'exception notable des deux hadiths du remède — qu'Abū Saʿīd al-Khuḍrī rapporte de Muslim, qu'Ibn ʿAbbās rapporte d'al-Bukhārī — qui subsistent INTACTS et diacrités, rareté favorable après trois leçons consécutives de spans erronés ; la citation d'al-Ghazālī subsiste elle aussi entière, l'étiquette imprimée signalant « avec retouche » — l'adaptation pédagogique du manuel étant conservée telle quelle. Les six gloses de l'explication des mots subsistaient sans leurs mots-têtes — troisième occurrence de la règle (y) ; la liste des mots de la préparation préalable est perdue — dixième occurrence ; la fente liminaire <em>dl/dt/dd</em> est vide — quatorzième ; le tatwīl du <em>fī</em> court à travers le titre — douzième leçon consécutive ; l'OCR effondrait le <em>lām</em> du chapitre du hadith de Muslim (« l'abreuvement de al-ʿasal » pour « du miel ») — tranché d'après la collation ; une espace manque entre « signalent » et « ces āyāt » ; et l'écart de numérotation persiste — leçon 14 au manuel, badge 19/32 du fil (treizième occurrence).</p>
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

out = '/home/z/my-project/tr-tmp/13587.html'
open(out, 'w').write(html)
print('écrit:', out)


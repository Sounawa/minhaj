#!/usr/bin/env python3
# build-13647.py — leçon 13647 « Sourate An-Nahl, versets 115-119 » (tafsir-tanawi-1, lessons[26], badge Leçon 28/32)
# Trame 13639 (R287). ZÉRO script arabe dans tout le htmlFr (auto-vérif ; U+FDFA exempté — convention du fil).
# VINGT emplacements perdus (cache) : bloc principal 115-119 (section vide entière, 18e cas) + 19 emplacements du
# commentaire et de la préparation — QUATRE avec span subsistant (al-Anʿām 146 — CORRECT ; al-Māʾida 4 — CORRECT ;
# Luqmān 23 — CORRECT ; al-Anʿām 147 — ERRONÉ TRANCHÉ à 146, 10e cas du fil (aa), l'édition en ligne du Muḥarrar
# citant expressément « {وعلى الذين هادوا حرمنا كل ذي ظفر} [الأنعام: 146] » ET sa note 7442 disant « في الآية (146) »)
# et QUINZE sans span ; DIX-NEUF restitutions coraniques + le bloc ; TROIS hadiths SUBSISTANTS entiers diacrités
# (Ibn Masʿūd [Maǧmaʿ az-zawāʾid] ; l'invocation de refuge [Nasāʾī, al-kubrā] ; la fatwā de Mālik [Muwaṭṭaʾ — OCR
# « كتا الحج »]) ; citation du cadi Ibn ʿAṭiyya (figures du manger de la bête morte) SUBSISTANTE ; gloses du الشرح
# AVEC leurs mots (6/6 — aucune règle (y)) ; fente dl/dt/dd REMPLIE d'une date (1ʳᵉ du fil) ; التعليم الثانوي bien
# orthographié ; Muḥarrar original consulté en ligne (sura16 aya115..119 — fetch 5/5 OK).
import json, os, re

FR1 = '''<h1>La sourate an-Naḥl — <em>al-Muḥarrar al-wajīz</em> d'Ibn ʿAṭiyya, versets 115 à 119</h1>
<p>Leçon de tafsīr — sourate an-Naḥl, versets (115-119) — tirée du livre <em>al-Tafsīr min khilāl al-Muḥarrar al-wajīz fī tafsīr al-Kitāb al-ʿazīz</em> d'Ibn ʿAṭiyya, au profit des élèves de la première année de l'enseignement secondaire ancien, première étape (leçon 26 du manuel — la vingt-sixième du fil consacré au Naḥl).</p>
<ol>
<li>Me familiariser avec le sens des mots des āyāt, et en déterminer les contenus.</li>
<li>Déduire des āyāt quelques-uns des interdits, et ce qui en est licité en cas de contrainte.</li>
<li>Ressentir la gravité de la présomption contre Allah, le Très-Haut, sans science.</li>
</ol>
<h2>Introduction</h2>
<p>Allah, le Très-Haut, a licité les bonnes choses utiles, et interdit les immondes nuisibles ; et Il a fait le cercle du licite beaucoup plus large que celui de l'interdit. Allah, le Très-Haut, n'a interdit une chose à Ses serviteurs que lorsqu'elle comporte préjudice pour la santé de l'homme, son entendement et sa religion — et nul n'est plus savant qu'Allah, le Très-Haut, de cet homme, et de ce qui le réforme ou le corrompt. C'est pourquoi l'acte de liciter et d'interdire demeure l'attribut propre d'Allah, le Très-Haut : il n'appartient à personne de liciter ou d'interdire quoi que ce soit par son avis et sa passion — comme le faisaient les Arabes de la Gāhiliyya.</p>
<p>Quelles sont donc les espèces d'aliments interdits que ces āyāt embrassent ? Et comment tirer leçon de la fin de celui qui a osé liciter et interdire par présomption contre Allah, sans science ?</p>
'''

FR2 = '''<h2>Les versets</h2>
<p>Allah, le Très-Haut, a dit :</p>
<p>« Il vous a, en effet, interdit la bête morte, le sang, la chair du porc, et ce sur quoi on a invoqué un autre nom que celui d'Allah. Quiconque donc est contraint — sans être rebelle ni transgresseur — alors Allah est Pardonneur et Miséricordieux. Et ne dites pas, pour ce que décrivent vos langues mensonge : ceci est licite, et cela est interdit — pour forger le mensonge contre Allah. Ceux qui forgent le mensonge contre Allah ne réussiront pas : une jouissance brève — et pour eux un châtiment douloureux. Aux Juifs, Nous avons interdit ce que Nous t'avons déjà relaté ; Nous ne leur avons fait aucun tort — mais ils se faisaient du tort à eux-mêmes. Puis ton Seigneur — envers ceux qui ont commis le mal par ignorance, puis se sont repentis après cela et ont amélioré leur conduite : ton Seigneur, après cela, est certes Pardonneur et Miséricordieux. » (an-Naḥl, 115-119)</p>
<p>[Citation coranique (an-Naḥl, 115-119 — le bloc entier des versets de la leçon) restaurée d'après le corpus canonique et vérifiée au cache coranique du corpus : la section imprimée « Les versets » est vide dans la source numérisée, le bloc versical tout entier ayant disparu à la numérisation — perte OCR — dix-huitième cas consécutif du fil ; l'étiquette subsistante « an-Naḥl : 115 - 119 » est correcte et suivie telle quelle.]</p>
<p><span>an-Naḥl : 115 - 119</span></p>
<h3>L'explication des mots</h3>
<p>[Les six explications subsistantes de la source numérisée portaient TOUTES leurs mots-têtes — exception favorable du fil : à la différence des occurrences de la règle (y) (leçons 13537, 13585 et 13587), aucune tête ne manque ici ; les mots expliqués ont été appariés à l'ordre des versets et au commentaire du manuel et du <em>Muḥarrar</em> original consulté en ligne.]</p>
<ul>
<li>« la bête morte » (<em>al-mayta</em>) : ce qui est mort de l'animal du désert sans immolation rituelle.</li>
<li>« et ce sur quoi on a invoqué un autre qu'Allah » (<em>wa-mā uhilla li-ghayri llāhi bihi</em>) : ce que l'on a présenté comme offrande à un autre qu'Allah.</li>
<li>« rebelle » (<em>bāghin</em>) : mangeant l'interdit sans contrainte.</li>
<li>« transgresseur » (<em>ʿādin</em>) : franchissant la borne de la nécessité.</li>
<li>« ceux qui sont juifs » (<em>alladhīna hādū</em>) : les Juifs.</li>
<li>« par ignorance » (<em>bi-ghahāla</em>) : par sottise, et sans considération des conséquences.</li>
</ul>
<h3>L'extraction des contenus des versets</h3>
<ol>
<li>Déduis des āyāt les espèces d'aliments interdits.</li>
<li>Précise contre quoi Allah, le Très-Haut, a mis en garde dans ces āyāt.</li>
</ol>
'''

FR3 = '''<h2>Le commentaire</h2>
<p>Les āyāt ont comporté ce qui suit :</p>
<h3>Premièrement : l'exposé par Allah, le Très-Haut, des interdits parmi les aliments</h3>
<p>Lorsqu'Allah, le Très-Haut, eut ordonné, dans les āyāt précédentes, de manger du revenu licite et bon, Il a fait suivre cela de l'exposé des interdits parmi les aliments, et le Très-Haut a dit :</p>
<p>« Il vous a, en effet, interdit la bête morte, le sang, la chair du porc, et ce sur quoi on a invoqué un autre nom que celui d'Allah. » (an-Naḥl, 115 — le tronçon des interdits)</p>
<p>[Citation coranique (an-Naḥl, 115 — le tronçon des interdits) restaurée d'après le corpus canonique et vérifiée au cache coranique du corpus : l'emplacement imprimé après « et le Très-Haut a dit : » est vide dans la source numérisée, SANS span subsistant — perte OCR ; le tronçon retenu est celui que la glose imprimée du manuel (« c'est-à-dire : votre Seigneur n'a interdit à vous que de manger la bête morte, le sang, la chair du porc, et ce qui a été immolé en approche vers un autre qu'Allah — des idoles et des simulacres ») commente — la clause de l'interdit de l'āya, la clause de la contrainte venant plus bas dans le commentaire.]</p>
<p>c'est-à-dire : votre Seigneur n'a interdit à vous que de manger la bête morte, le sang, la chair du porc, et ce qui a été immolé en approche vers un autre qu'Allah — des idoles et des simulacres.</p>
<p>Et cette āya a CONFINÉ — par le vocable « seuls » (<em>innamā</em>) — les aliments jugés interdits au temps où l'āya descendit ; puis, après cela, descendirent d'autres āyāt exposant ce qui fut interdit ensuite. Et ce confinement aux quatre espèces d'aliments se répète dans Sa parole, le Très-Haut :</p>
<p>« Aux Juifs, Nous avons interdit toute bête à ongle. Des bovins et des ovins, Nous leur avons interdit les graisses, sauf ce que portent leur dos, leurs entrailles, ou ce qui est mêlé à l'os — Nous les avons ainsi rétribués de leur rébellion, et Nous sommes bien véridiques. » (al-Anʿām, 146)</p>
<p>[Citation coranique (al-Anʿām, 146) restaurée d'après le corpus canonique et vérifiée au cache coranique du corpus : l'emplacement imprimé après « se répète dans Sa parole, le Très-Haut : » n'offre AUCUN emplacement vide — le seul span subsistant « al-Anʿām : 146 » est collé au deux-points, la citation ayant disparu à la numérisation ; le span est CORRECT et suivi tel quel — l'āya, adressée aux Juifs, énumère les catégories d'interdits alimentaires et se referme sur « Nous les avons ainsi rétribués de leur rébellion » ; la portée du « confinement répété » demeure la thèse imprimée du manuel.]</p>
<p>et ce qu'Allah, le Très-Haut, a mentionné dans la sourate de la Table servie, dans Sa parole :</p>
<p>« Ils t'interrogent sur ce qui leur est licité. Dis : vous sont licitées les bonnes choses, ainsi que ce que capturent les carnassiers que vous dressez, en leur apprenant ce qu'Allah vous a appris — mangez donc de ce qu'elles capturent pour vous et prononcez sur elles le nom d'Allah ; et craignez Allah : Allah est prompt au compte. » (al-Māʾida, 4)</p>
<p>[Citation coranique (al-Māʾida, 4) restaurée d'après le corpus canonique et vérifiée au cache coranique du corpus : l'emplacement imprimé après « dans Sa parole : » est vide dans la source numérisée ; le span subsistant « al-Māʾida : 4 » est CORRECT et suivi tel quel — l'āya restituée entière d'après le corpus canonique et vérifiée au cache : c'est elle qui ouvre l'énumération du licit (« vous sont licitées les bonnes choses ») par laquelle le manuel illustre le passage du résumé au détail.]</p>
<ul>
<li>Cela tient de la manière du détail, pour ce qui fut résumé en cette āya et en l'āya d'al-Anʿām — le reste des mentions étant des espèces de la bête morte.</li>
<li>La bête morte interdite : ce qui est mort de l'animal du désert sans immolation rituelle.</li>
<li>Le sang répandu : le sang fluide ; quant à ce qui s'est mêlé à la chair et s'y est logé, il est licite, permis.</li>
<li>La chair du porc : y est visé l'interdit de la chair, de la graisse et de l'ensemble des membres du porc ; et si Allah, le Très-Haut, a spécifié la chair à la mention, c'est qu'elle est, en général, ce qu'on vise à manger.</li>
<li>Et ce sur quoi on a invoqué un autre qu'Allah : c'est ce qu'on a visé d'immoler en approche vers un autre qu'Allah. Les Arabes, lorsqu'ils menaient une bête à immoler vers une idole, criaient au nom de cette idole — l'expression courut alors sous le vocable de l'« énonciation » (<em>istihlāl</em>), qui est l'élévation de la voix.</li>
</ul>
<p>Et Sa parole, le Très-Haut :</p>
<p>« Quiconque donc est contraint » (an-Naḥl, 115 — le tronçon de la contrainte)</p>
<p>[Citation coranique (an-Naḥl, 115 — le tronçon de la contrainte) restaurée d'après le corpus canonique et vérifiée au cache coranique du corpus : l'emplacement imprimé après « Et Sa parole, le Très-Haut : » est vide dans la source numérisée, SANS span subsistant — perte OCR ; le tronçon retenu est celui que le <em>Muḥarrar</em> original attache expressément à la parole de la majorité (« la majorité a dit : au sens que la faim et le besoin l'ont contraint »), que le commentaire imprimé du manuel paraphrase immédiatement après.]</p>
<p>c'est-à-dire : quiconque se trouve contraint à consommer une chose de ces interdits, par une famine qui lui est survécue, ou par une nécessité qui l'a poussé à en prendre — sans être rebelle envers les autres gens, ni dépassant, en son manger, la mesure de la nécessité et du maintien du souffle — Allah ne le sanctionne point de cela ; Il est Celui qui couvre les inadvertances que commettent les serviteurs, et Il est plus miséricordieux envers eux que de les sanctionner de semblable chose.</p>
<p>Et Sa parole :</p>
<p>« sans être rebelle » (an-Naḥl, 115 — le tronçon du rebelle)</p>
<p>[Citation coranique (an-Naḥl, 115 — le tronçon du rebelle) restaurée d'après le corpus canonique et vérifiée au cache coranique du corpus : l'emplacement imprimé après « Et Sa parole : » est réduit, dans la source numérisée, à un simple saut de ligne vide, SANS span subsistant — perte OCR ; le tronçon retenu est celui que le <em>Muḥarrar</em> original cite MOT POUR MOT à la parole de la majorité (« Sa parole : sans être rebelle — au sens : celui qui n'use pas de ces interdits, alors que d'autres existent »), que le manuel reproduit mot à mot.]</p>
<p>au sens : celui qui n'use pas de ces interdits, alors que d'autres choses existent.</p>
<p>« ni transgresseur » (an-Naḥl, 115 — le tronçon du transgresseur)</p>
<p>[Citation coranique (an-Naḥl, 115 — le tronçon du transgresseur) restaurée d'après le corpus canonique et vérifiée au cache coranique du corpus : l'emplacement imprimé à la suite est vide dans la source numérisée, SANS span subsistant — perte OCR ; le tronçon retenu est celui que le <em>Muḥarrar</em> original cite MOT POUR MOT à la parole de la majorité (« et sans être transgresseur — au sens : il ne dépasse pas les bornes d'Allah en cela »), que le manuel reproduit mot à mot.]</p>
<p>au sens : il ne dépasse pas les bornes d'Allah en cela.</p>
<p>Le cadi Ibn ʿAṭiyya, qu'Allah lui fasse miséricorde, a dit : les gens ont divergé sur la figure du manger de la bête morte : une fraction a dit que n'en est licite que ce qui retient le souffle ; une fraction a dit : mais la réplétion complète est permise ; une fraction d'entre eux — Mālik, qu'Allah lui fasse miséricorde — a dit : sont permises la réplétion et la provision de route.</p>
<p>Et Sa parole, le Très-Haut :</p>
<p>« alors Allah est Pardonneur et Miséricordieux » (an-Naḥl, 115 — le tronçon du pardon)</p>
<p>[Citation coranique (an-Naḥl, 115 — le tronçon du pardon) restaurée d'après le corpus canonique et vérifiée au cache coranique du corpus : l'emplacement imprimé après « Et Sa parole, le Très-Haut : » est vide dans la source numérisée, SANS span subsistant — perte OCR ; le tronçon retenu est celui que le <em>Muḥarrar</em> original attache expressément à la glose du manuel (« Sa parole : alors Allah est Pardonneur et Miséricordieux — vocable d'où s'entend la licéité pour le contraint »).]</p>
<p>vocable d'où s'entend la licéité pour le contraint. Et la licéité ici est conditionnée par la contrainte — c'est sur cette base que se tient le pardon d'Allah au contraint.</p>
'''

FR4 = '''<h3>Deuxièmement : l'exposé de la fin du liciter et de l'interdire selon la passion</h3>
<p>Le Très-Haut a dit :</p>
<p>« Et ne dites pas, pour ce que décrivent vos langues mensonge : ceci est licite, et cela est interdit — pour forger le mensonge contre Allah. » (an-Naḥl, 116 — le tronçon de la parole interdite)</p>
<p>[Citation coranique (an-Naḥl, 116 — le tronçon de la parole interdite) restaurée d'après le corpus canonique et vérifiée au cache coranique du corpus : l'emplacement imprimé après « Le Très-Haut a dit : » est vide dans la source numérisée, SANS span subsistant — perte OCR ; le tronçon retenu est celui que la glose imprimée du manuel (« c'est-à-dire : et ne dites pas, ceci est licite et cela est interdit, par l'opinion et la passion ») commente dès la ligne suivante.]</p>
<p>c'est-à-dire : et ne dites pas : ceci est licite, et cela est interdit — par l'opinion et la passion. Comme ils disaient, en ce qu'Allah, le Très-Haut, relate d'eux :</p>
<p>« Perdus, certes, sont ceux qui tuèrent leurs enfants par sottise, sans science, et qui interdirent ce qu'Allah leur avait attribué, forgeant le mensonge contre Allah — ils se sont égarés, et ils ne furent point guidés. » (al-Anʿām, 140)</p>
<p>[Citation coranique (al-Anʿām, 140) restaurée d'après le corpus canonique et vérifiée au cache coranique du corpus : l'emplacement imprimé après « relate d'eux : » n'offre AUCUN emplacement vide — le seul span subsistant « al-Anʿām : 140 » est collé au deux-points, la citation ayant disparu à la numérisation ; le span est CORRECT et suivi tel quel : l'āya porte expressément le fait d'interdire ce qu'Allah a attribué, forgeant le mensonge contre Allah — précisément ce que le commentaire imprimé rapporte des associateurs.]</p>
<p>Et cette āya s'adresse aux mécréants qui interdirent la <em>baḥīra</em> et la <em>sāʾiba</em>, et licitèrent ce qu'il y a dans les ventres des bestiaux, fût-ce de la bête morte ; et l'āya vaut pour tout ce qui fut le leur, de liciter et d'interdire — tout cela est forgerie de leur part ; et parmi cela, ce qu'ils rendirent interdit selon les mois.</p>
<p>Et Sa parole, le Très-Haut :</p>
<p>« pour forger le mensonge contre Allah » (an-Naḥl, 116 — le tronçon de la forgerie)</p>
<p>[Citation coranique (an-Naḥl, 116 — le tronçon de la forgerie) restaurée d'après le corpus canonique et vérifiée au cache coranique du corpus : l'emplacement imprimé après « Et Sa parole, le Très-Haut : » est vide dans la source numérisée, SANS span subsistant — perte OCR ; le tronçon retenu est celui que la glose imprimée du manuel (« c'est-à-dire : pour que vous mentiiez sur Allah… ») commente mot à mot — le <em>Muḥarrar</em> original y voyant aussi une indication du propos rapporté d'eux en l'āya d'al-Aʿrāf, citée en note de l'édition en ligne.]</p>
<p>c'est-à-dire : pour que vous mentiiez sur Allah, en rapportant à Allah, mensongèrement, ce que vous avez licité et ce que vous avez interdit — cela n'étant point d'Allah en vérité. Allah n'a point interdit ce que vous avez interdit, ni licité beaucoup de ce que vous avez licité ; car l'acte du licite et de l'interdit est confié à Allah, le Très-Haut.</p>
<p>Et Ibn Masʿūd a dit : « Il est à craindre qu'un homme dise : Allah a ordonné telle chose, ou a interdit telle chose — et qu'Allah, Puissant et Glorieux, lui dise : tu as menti ; ou qu'il dise : Allah a interdit telle chose et licité telle chose — et qu'Allah lui dise : tu as menti. » [le <em>Maǧmaʿ az-zawāʾid</em>, livre de la science, chapitre de celui qui tient pour licite l'interdit, ou interdit le licite, ou délaisse la sunna]</p>
<p>[Hadith subsistant ENTIER et diacrité dans la source numérisée — traduit in extenso ; la double supposition (« a ordonné… ou a interdit » / « a interdit… et licité ») et la double réplique divine (« tu as menti ») sont portées par la lettre même de la source ; c'est pourquoi l'acte du licite et de l'interdit demeure suspendu à la volonté d'Allah.]</p>
<p>Et Sa parole, le Très-Haut :</p>
<p>« Ceux qui forgent le mensonge contre Allah ne réussiront pas. » (an-Naḥl, 116 — le tronçon de la clôture)</p>
<p>[Citation coranique (an-Naḥl, 116 — le tronçon de la clôture) restaurée d'après le corpus canonique et vérifiée au cache coranique du corpus : l'emplacement imprimé après « Et Sa parole, le Très-Haut : » est vide dans la source numérisée, SANS span subsistant — perte OCR ; le tronçon retenu est celui que la glose imprimée du manuel (« c'est-à-dire : ceux qui inventent le mensonge sur Allah… ne remportent aucun bien ») commente — la clôture de l'āya.]</p>
<p>c'est-à-dire : ceux qui inventent le mensonge sur Allah, en leurs affaires petites et grandes, ne remportent aucun bien et n'atteignent pas ce qu'ils visaient en mentant ; car dès qu'ils sont connus pour le mensonge, les gens les dédaignent et s'en détournent, et ils vivent avilis, honnis. Allah en a fait des proverbes de bassesse et d'infériorité, pour ce qui les atteindra d'ignominie et de fléau au Jour de la Résurrection.</p>
<p>Et Sa parole, le Très-Haut :</p>
<p>« Une jouissance brève — et pour eux un châtiment douloureux. » (an-Naḥl, 117)</p>
<p>[Citation coranique (an-Naḥl, 117) restaurée d'après le corpus canonique et vérifiée au cache coranique du corpus : l'emplacement imprimé après « Et Sa parole, le Très-Haut : » est vide dans la source numérisée, SANS span subsistant — perte OCR ; l'āya retenue est celle que la glose imprimée du manuel (« c'est-à-dire : les bénéfices qui peuvent leur advenir de leur mensonge en ce monde… ») commente dès la ligne suivante — l'āya entière de la jouissance et du châtiment.]</p>
<p>c'est-à-dire : les bénéfices qui peuvent leur advenir de leur mensonge en ce monde ne pèsent rien, si on les compare aux préjudices qui les atteignent dans l'au-delà ; la jouissance d'ici-bas périt vite, et le châtiment douloureux demeure pour eux dans l'au-delà. Semblable āya est Sa parole, le Très-Haut :</p>
<p>« Celui qui a mécru — que sa mécréance ne t'afflige point : c'est vers Nous que sera leur retour, et Nous les informerons de ce qu'ils faisaient. Allah connaît le contenu des poitrines. » (Luqmān, 23)</p>
<p>[Citation coranique (Luqmān, 23) restaurée d'après le corpus canonique et vérifiée au cache coranique du corpus : l'emplacement imprimé après « Semblable āya est Sa parole, le Très-Haut : » est vide dans la source numérisée ; le span subsistant « Luqmān : 23. » est CORRECT et suivi tel quel — le point final du span étant porté par la source ; l'āya restituée entière d'après le corpus canonique et vérifiée au cache : le parallèle de la jouissance brève et de l'informateur dernier des œuvres.]</p>
'''

FR5 = '''<p>Et Sa parole, le Très-Haut :</p>
<p>« Aux Juifs, Nous avons interdit ce que Nous t'avons déjà relaté. » (an-Naḥl, 118 — le tronçon de l'interdit)</p>
<p>[Citation coranique (an-Naḥl, 118 — le tronçon de l'interdit) restaurée d'après le corpus canonique et vérifiée au cache coranique du corpus : l'emplacement imprimé après « Et Sa parole, le Très-Haut : » est vide dans la source numérisée, SANS span subsistant — perte OCR ; le tronçon retenu est celui que la glose imprimée du manuel (« c'est-à-dire : Nous avons interdit aux Juifs ce que Nous t'avons annoncé auparavant, dans la sourate d'al-Anʿām… ») commente — le premier hémistiche de l'āya, la clôture venant plus bas.]</p>
<p>c'est-à-dire : Nous avons interdit aux Juifs ce que Nous t'avons annoncé auparavant, dans la sourate d'al-Anʿām, là où le Très-Haut a dit :</p>
<p>« Aux Juifs, Nous avons interdit toute bête à ongle. » (al-Anʿām, 146 — le tronçon cité)</p>
<p>[Citation coranique (al-Anʿām, 146 — le tronçon cité) restaurée d'après la lettre du <em>Muḥarrar</em> original et vérifiée au cache coranique du corpus : l'emplacement imprimé après « là où le Très-Haut a dit : » n'offre AUCUN emplacement vide — le seul span subsistant « al-Anʿām : 147 » s'est révélé ERRONÉ et a été tranché — le <em>Muḥarrar</em> original ouvre le commentaire de cette āya du Naḥl en citant expressément « Sa parole : aux Juifs, Nous avons interdit toute bête à ongle » [al-Anʿām : 146], et sa note à l'āya précédente porte : « en Sa parole, à l'āya (146) : aux Juifs, Nous avons interdit toute bête à ongle et des bovins et des ovins leurs graisses » ; l'āya 147, elle, ne porte AUCUN interdit juif — « s'ils te traitent de menteur, dis : votre Seigneur est Détenteur d'une immense miséricorde » ; SPAN ERRONÉ signalé, dixième cas du fil, tranché à l'édition en ligne elle-même ET au cache — jamais corrigé dans le sens d'une lecture canonique inventée.]</p>
<p>Allah expose en cette āya que Son interdit sur les Juifs de ces choses mentionnées dans la sourate d'al-Anʿām ne comporte aucune injustice envers eux : car ils furent eux-mêmes la cause de cet interdit, par ce qu'ils altérèrent et falsifièrent des législations d'Allah, le Très-Haut. Cet interdit fut donc une sanction contre leur injustice et leur rébellion. Et par ce sens se précise la différence entre les Juifs et les autres en matière d'interdit : ce fut sanction contre eux, et avantage pour les autres.</p>
<p>Et Sa parole, le Très-Haut :</p>
<p>« Nous ne leur avons fait aucun tort — mais ils se faisaient du tort à eux-mêmes. » (an-Naḥl, 118 — le tronçon de la clôture)</p>
<p>[Citation coranique (an-Naḥl, 118 — le tronçon de la clôture) restaurée d'après le corpus canonique et vérifiée au cache coranique du corpus : l'emplacement imprimé après « Et Sa parole, le Très-Haut : » est vide dans la source numérisée, SANS span subsistant — perte OCR ; le tronçon retenu est celui que le <em>Muḥarrar</em> original commente (« Sa parole : Nous ne les avons point lésés — au sens : Nous n'avons pas placé la sanction de l'interdit de ces choses hors de leur lieu, mais ils ont eux-mêmes creusé vers cela, et de leur faute de désobéissances est venue la chose qui l'a imposé »), que le commentaire imprimé paraphrase.]</p>
<p>Et Sa parole, le Très-Haut :</p>
<p>« Puis ton Seigneur — envers ceux qui ont commis le mal par ignorance, puis se sont repentis après cela et ont amélioré leur conduite : ton Seigneur, après cela, est certes Pardonneur et Miséricordieux. » (an-Naḥl, 119)</p>
<p>[Citation coranique (an-Naḥl, 119) restaurée d'après le corpus canonique et vérifiée au cache coranique du corpus : l'emplacement imprimé après « Et Sa parole, le Très-Haut : » est vide dans la source numérisée, SANS span subsistant — perte OCR ; l'āya retenue est celle que la glose imprimée du manuel (« cette āya fait connaître qu'Allah, le Très-Haut, est d'ample miséricorde et de grand pardon… ») commente dès la ligne suivante — la clôture du bloc.]</p>
<p>cette āya fait connaître qu'Allah, le Très-Haut, est d'ample miséricorde et de grand pardon envers celui dont l'état s'est redressé et dont le repentir a été sincère ; et que le Très-Haut a passé outre, à l'égard de ceux-ci, à ce qu'ils avaient commis avant le repentir de désobéissances, par suite de l'ignorance qui les portait à enfreindre les inviolabilités de la religion — comme le meurtre par jalousie, ou par esprit de clan. Et il a été rapporté du Prophète, que la bénédiction d'Allah et la paix soient sur lui, qu'il disait dans son invocation : « Ô Allah, je cherche refuge auprès de Toi : d'être humilié, ou d'être égaré, ou d'être lésé, ou de léser, ou d'être ignorant, ou que l'on agisse avec ignorance envers moi. » [le <em>Sunan al-kubrā</em> d'an-Nasāʾī, livre de la recherche de refuge, la recherche de refuge contre l'égarement]</p>
<p>[Hadith subsistant ENTIER et diacrité dans la source numérisée — traduit in extenso ; les six volets de l'invocation (« humilié — égaré — lésé — lésant — ignorant — traité avec ignorance ») sont portés par la lettre même de la source ; le sceau prophétique de la source numérisée est rendu par la formule française usuelle du fil ; le <em>Muḥarrar</em> original cite en note, à l'āya 119, la même famille du hadith — dont la version d'Umm Salama au sortir de la maison, rapportée par les cinq — et le vers d'ʿAmr b. Kulṯūm que le cadi y attache.]</p>
<p>En cette āya est un adoucissement pour tous les gens : Allah, le Très-Haut, y annonce qu'Il pardonne à ceux qui se repentent, quelque étendue que soient leurs fautes et leurs désobéissances ; Sa miséricorde, glorifié soit-Il, est plus ample que la désobéissance de tout désobéissant, et que la faute de tout fautif.</p>
<p>Et ces āyāt signalent un des desseins de la législation islamique : lever la gêne d'avec les gens, et faciliter ce qui leur est pénible. C'est pourquoi Allah, le Très-Haut, a relié Son ordre et Son interdiction à la capacité et à la force des serviteurs. Et en ces āyāt est aussi une des manifestations de la miséricorde d'Allah, le Très-Haut, envers Ses serviteurs : Il a levé d'eux la charge en état de nécessité — cela se figure dans la permission donnée à l'homme de manger de la bête morte interdite, s'il est contraint et ne trouve autre chose.</p>
'''

FR6 = '''<h2>L'évaluation</h2>
<ol>
<li>Les interdits parmi les aliments se limitent-ils aux quatre espèces mentionnées ?</li>
<li>Déduis des āyāt la règle de fiqh de la licéité de l'interdit.</li>
<li>Expose la gravité de laisser courir la langue à l'avis religieux, en la religion, sans science.</li>
<li>Déduis des āyāt les expressions signalant l'ampleur de la miséricorde d'Allah et Son pardon.</li>
</ol>
<h2>L'exploitation</h2>
<p>Il est rapporté dans le <em>Muwaṭṭaʾ</em> : on interrogea Mālik au sujet de l'homme qui se trouve contraint de manger de la bête morte, alors qu'il est en état d'ihram — chasse-t-il le gibier et en mange-t-il, ou mange-t-il de la bête morte ? Il dit : « Il mange plutôt de la bête morte — et cela parce qu'Allah, Béni et Très-Haut, n'a point accordé de dispense au muḥrim pour manger du gibier, ni pour le prendre, en aucun état des états ; et Il a accordé dispense pour la bête morte, en état de nécessité. » [le <em>Muwaṭṭaʾ</em>, livre du ḥaǧǧ, chapitre de ce dont le manger n'est pas licite parmi le gibier]</p>
<p>[Hadith subsistant ENTIER et diacrité dans la source numérisée — traduit in extenso ; la question posée à Mālik, le statut du muḥrim, le gibier et la bête morte sont portés par la lettre même de la source ; l'OCR du span de référence a perdu le <em>bāʾ</em> de « livre » — « kitāb al-ḥaǧǧ » imprimé sans lui — altération connue du fil, restituée au français sans changer la source.]</p>
<ol>
<li>Expose comment l'imam Mālik, qu'Allah lui fasse miséricorde, a argumenté la licéité, pour le muḥrim contraint, de manger de la bête morte.</li>
<li>Détermine la règle de fiqh retenue dans cette fatwā.</li>
</ol>
'''

FR7 = '''<h2>La préparation préalable</h2>
<p>Lis les āyāt (120-124) de la sourate an-Naḥl, et réponds à ce qui suit :</p>
<ul>
<li>Explique les mots suivants :</li>
</ul>
<p>[Liste de la préparation préalable NON restituée : la liste imprimée des mots à expliquer est perdue dans la source numérisée — QUATRE emplacements vides à la suite de « Explique les mots suivants : » — seizième occurrence du fil ; conformément à la convention du fil, elle n'est JAMAIS reconstituée par conjecture, les mots de l'iʿdād de la leçon suivante (an-Naḥl, 120-124) demeurant à chercher directement dans le texte coranique lui-même.]</p>
<ul>
<li>Précise le sens de la <em>ḥanīfiyya</em> dans Sa parole, le Très-Haut :</li>
</ul>
<p>« Abraham fut une communauté obéissante envers Allah, ḥanīf — et il ne fut point du nombre des polythéistes. » (an-Naḥl, 120 — le tronçon de la <em>ḥanīfiyya</em>)</p>
<p>[Citation coranique (an-Naḥl, 120 — le tronçon de la <em>ḥanīfiyya</em>) restaurée d'après le corpus canonique et vérifiée au cache coranique du corpus : l'emplacement imprimé après « dans Sa parole, le Très-Haut : » est vide dans la source numérisée, SANS span subsistant — perte OCR ; la question imprimée (« précise le sens de la <em>ḥanīfiyya</em> dans Sa parole ») renvoie nécessairement à l'āya du Naḥl qui porte le vocable du <em>ḥanīf</em> — restituée à son emplacement selon la logique du commentaire.]</p>
<ul>
<li>Déduis des āyāt les qualités dont Allah a loué notre maître Abraham, sur lui la paix.</li>
</ul>
<p>N.d.T. — Le <em>Muḥarrar</em> original d'Ibn ʿAṭiyya, consulté en ligne (collation des cinq āyāt 115-119, réussite cinq sur cinq), comporte pour ces versets des matières que le manuel n'a pas retenues, et qui complètent utilement la leçon. Pour l'āya 115 : une fraction a lu le vocable de la contrainte à la sonorisation de la nūn et de la ṭāʾ, et une autre à l'ouverture des deux — l'origine étant un déplacement de la voyelle du rāʾ à la ṭāʾ, avec l'assimilation du rāʾ dans le rāʾ ; le <em>Muḥarrar</em> consigne les sens des deux limites : la « rébellion » comme dissidence contre l'imam, ou brigandage sur les routes — en somme le voyage de la désobéissance —, et le « transgresseur » comme qui vise la désobéissance ; une fraction porte les deux vocables sur la réplétion et la provision de route ; et des grammairiens y relèvent la figure du mot retourné de son participe — à la façon de la corde qui rompt et du jour qui revient, comme au vers du poète. Le <em>Muḥarrar</em> porte encore que la licéité fut formulée en ces vocables de la façon la plus resserrée, pour signifier la gravité de ces interdits — la fin du permis au contraint étant le pardon d'Allah, qui le décharge du péché que la nécessité aurait imposé ; et le cadi relève que cet interdit se laisse entendre des Arabes par le seul vocable, sans être dans le sens même — pure allusion —, comme en un autre lieu la fin du permis n'est que l'absence de péché, alors même qu'il n'y a point de péché [l'édition en ligne cite en note l'āya de la Vache : « point de péché sur lui » — al-Baqara, 173, le doublet des interdits]. Pour l'āya 116 : « ceci est licite » y est une indication des bêtes mortes des ventres des bestiaux et de tout ce qu'ils licitèrent ; « cela est interdit », des <em>baḥāʾir</em> et des <em>saʾāʾib</em> et de tout ce qu'ils interdirent ; « pour forger le mensonge » y indique leur propos sur leurs turpitudes — « nous l'avons trouvé chez nos pères, et Allah nous en donne l'ordre » [al-Aʿrāf, 28 — citée en note] ; et le cadi ajoute que leur législation était pour être suivis en des sunnas qu'Allah n'agrée point, forgées contre Lui — car celui qui légifère une affaire dit en effet à ses suivants : ceci est le vrai, et ceci est la volonté d'Allah ; « la réussite » y est l'atteinte de l'espérance — tantôt dans la durée de la vie, comme le vers d'ʿUbayd b. al-ʿAbraṣ qu'il cite [l'édition en ligne en porte la note : l'un des vers les plus excellents du poète, de sa Muʿallaqa]. Pour l'āya 117 : la « jouissance » y est une indication de leur vie en ce monde, et le « châtiment », après cela, dans l'au-delà ; et le commentaire de l'āya 118 y relève la sagesse : lorsque Allah eut relaté aux croyants ce qu'Il leur avait interdit, Il les informa aussi de ce qu'Il avait interdit aux Juifs — pour exposer leur falsification de la législation, en ce qu'ils licitèrent et interdirent de leur propre chef ; et la note porte que cela démontre que la sourate d'al-Anʿām descendit avant la sourate du Naḥl. Pour l'āya 119 : l'āya y est dite « adoucissement pour tout le monde » — Allah y annonce le pardon au repentant ; et l'āya est une indication des mécréants qui forgèrent le mensonge sur Allah et firent les œuvres mentionnées : s'ils se repentent de leur mécréance par la foi, et réforment leurs actes par les œuvres de l'islam, Allah leur pardonne — l'āya embrassant ensuite tout contraint sous son vocable, mécréant ou désobéissant ; une fraction tient « l'ignorance » pour l'outrance ; et le cadi : l'« ignorance » en ce lieu n'est pas le contraire de la science, mais le dépassement de la mesure et le chevauchement de l'outrecuidance — d'où le hadith prophétique « ou que je fasse preuve d'ignorance, ou que l'on en fasse preuve envers moi » [rapporté par Ibn Māǧa dans les invocations, Abū Dāwūd dans les mœurs, at-Tirmiḏī dans les demandes, an-Nasāʾī dans la recherche de refuge, et Aḥmad dans son Musnad — l'édition en ligne en porte la version d'Umm Salama au sortir de la maison] ; la « non-science » contraire accompagne souvent celle-ci, mais l'outrecuidant en sort — car on trouve rarement parmi les désobéissants qui n'ait été averti du danger de la désobéissance où il court ; et le pronom de « après elle » renvoie au repentir.</p>
<p>N.d.T. — État de la source numérisée de cette leçon : la section « Les versets » est vide entière — dix-huitième cas consécutif du fil ; VINGT emplacements porteurs de pertes : le bloc principal (portant son étiquette subsistante « an-Naḥl : 115 - 119 », correcte et suivie telle quelle) et DIX-NEUF emplacements du commentaire et de la préparation — QUATRE avec span subsistant (al-Anʿām 146 — CORRECT ; al-Māʾida 4 — CORRECT ; Luqmān 23 — CORRECT ; al-Anʿām 147 — ERRONÉ et tranché à 146, dixième cas du fil) et QUINZE sans aucun span — perte OCR ; DIX-NEUF restitutions coraniques. Exceptions favorables marquantes du fil : TROIS hadiths subsistants ENTIERS et diacrités — le propos d'Ibn Masʿūd sur le mensonge religieux [le <em>Maǧmaʿ az-zawāʾid</em>, livre de la science], l'invocation prophétique de refuge [le <em>Sunan al-kubrā</em> d'an-Nasāʾī, livre de la recherche de refuge], et la fatwā de Mālik sur le muḥrim contraint [le <em>Muwaṭṭaʾ</em>, livre du ḥaǧǧ] — tous trois traduits in extenso ; la citation du cadi Ibn ʿAṭiyya sur les figures du manger de la bête morte (le maintien du souffle, la réplétion complète, la réplétion et la provision de route chez Mālik) subsiste entière et reprend MOT POUR MOT le <em>Muḥarrar</em> original ; les SIX gloses de l'explication des mots subsistaient avec leurs mots-têtes — aucune occurrence de la règle (y) dans cette leçon. EXCEPTION FAVORABLE INÉDITE : la fente liminaire <em>dl/dt/dd</em>, vide en dix-neuf leçons du fil, est ICI REMPLIE — elle porte la date imprimée de la leçon (lundi 22 juillet 2019), première occurrence du fil ; et le nom de l'enseignement secondaire ancien y est correctement orthographié — l'altération OCR de l'alef dédoublé, connue des leçons précédentes, est absente ici. Le tatwīl du <em>fī</em> court à travers le titre — dix-huitième leçon consécutive ; l'étiquette d'adresse du tutoiement demeure dénaturée (le <em>yāʾ</em> de « Lis », « Déduis », « Précise », « Expose ») — connue du fil ; l'écart de numérotation persiste — leçon 26 au manuel, badge 28/32 du fil — dix-neuvième occurrence ; des <em>div</em> de fermeture subsistent en queue.</p>
<p>N.d.T. — Précisions de restitution : le bloc principal (an-Naḥl, 115-119) et les āyāt entières citées (al-Anʿām 146, al-Māʾida 4, al-Anʿām 140, Luqmān 23, an-Naḥl 117, an-Naḥl 119, an-Naḥl 120) ont été restituées d'après le corpus canonique et vérifiées au cache coranique du corpus, les gloses imprimées du manuel les commentant chacune dès la ligne qui suit leur emplacement ; les tronçons de l'āya 115 — des interdits, de la contrainte, du rebelle, du transgresseur, du pardon — d'après les gloses imprimées et la lettre du <em>Muḥarrar</em>, qui attache expressément la parole de la majorité au tronçon de la contrainte (« la faim et le besoin l'ont contraint ») et le « vocable d'où s'entend la licéité pour le contraint » au tronçon du pardon ; les tronçons de l'āya 116 — de la parole interdite, de la forgerie, de la clôture — d'après les gloses imprimées ; le tronçon d'al-Anʿām 146 cité dans le commentaire de l'āya 118 d'après la lettre du <em>Muḥarrar</em> — SPAN ERRONÉ « al-Anʿām : 147 » tranché à l'āya 146 par l'édition en ligne elle-même (double citation express, au commentaire et en note) ET au cache — l'écart signalé en note à son emplacement, jamais corrigé dans le sens d'une lecture canonique inventée ; les DEUX citations collées au deux-points sans emplacement vide (al-Anʿām 146 du confinement, al-Anʿām 140 du propos rapporté) restituées selon leurs spans ; la citation de la <em>ḥanīfiyya</em> restituée selon la logique de la question imprimée ; la date de la fente liminaire rendue pour information, sans figer la leçon à cette date ; le span de Luqmān portant un point final — « Luqmān : 23. » — suivi tel quel.</p>
'''

html = FR1 + FR2 + FR3 + FR4 + FR5 + FR6 + FR7
html = html.replace("'", chr(0x2019))

issues = []
AR = re.compile('[' + ''.join(chr(a) + '-' + chr(b) for a, b in [(0x0600, 0x06FF), (0x0750, 0x077F), (0x08A0, 0x08FF), (0xFB50, 0xFDF9), (0xFDFB, 0xFDFF), (0xFE70, 0xFEFF)]) + ']')
ar = AR.findall(html)
if ar:
    issues.append("caractères arabes résiduels: " + str(len(ar)) + " : " + ''.join(sorted(set(ar)))[:50])
if html.count("«") != html.count("»"):
    issues.append(f"guillemets non appariés: {html.count('«')} / {html.count('»')}")
if "'" in html:
    issues.append(f"apostrophes droites restantes: {html.count(chr(39))}")
for cp, name in [(0x0430, 'cyrillique'), (0xFD3E, 'crochet ornement gauche'), (0xFD3F, 'crochet ornement droit')]:
    if chr(cp) in html:
        issues.append(f'{name} présent')
bal = ['h1', 'h2', 'h3', 'p', 'ol', 'ul', 'li', 'em', 'span']
types = sum(1 for b in bal if f'<{b}>' in html)
n_notes = html.count('[Citation coranique') + html.count('[Liste de la préparation') + html.count('[Restauration NON coranique') + html.count('[Hadith subsistant')
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

out = '/home/z/my-project/tr-tmp/13647.html'
open(out, 'w').write(html)
print('écrit:', out)

#!/usr/bin/env python3
# savant(fiqh-1es/11439) — L'imāmat de la prière et ses règles
# Leçon 14 — Risāla d'Ibn Abī Zayd al-Qayrawānī, comm. Kifāyat aṭ-ṭālib ar-rabbānī (Abū al-Ḥasan), ḥāshiya al-ʿAdawī
#
# Vérifications dorar.net (sunnah.com bloqué Turnstile — cf. R82/R83) :
#  - Muwaṭṭaʾ « من أدرك ركعة من الصلاة فقد أدرك الصلاة » : parallèles Bukhārī 579 / Muslim 608
#    (version ṣubḥ/ʿaṣr), Ibn Ḥibbān 1557 — citation Muwaṭṭaʾ (bāb) exacte.
#  - Ibn ʿUmar « صلاة الجماعة تفضل صلاة الفذ بسبع وعشرين درجة » : Bukhārī 645 / Muslim 650 — EXACT.
#  - ʿUmar « ليس على من خلف الإمام سهو… والإمام كافيه » : Dāraquṭnī 1/377, Bayhaqī 4050
#    (dorar : Ibn ʿAbd al-Hādī « ليس له إسناد » — réserve documentée, citation telle qu'imprimée).
#  - Abū Hurayra « أما يخشى الذي يرفع رأسه قبل الإمام أن يحول الله رأسه رأس حمار » : Bukhārī 691 /
#    Muslim 427 — EXACT.
#  - Ibn ʿAbbās (nuit chez Maymūna) : Bukhārī 699 / Muslim 763 — EXACT (variante « تناولني من خلف
#    ظهره » = Muslim ; dorar affiche la variante Bukhārī « فأخذ برأسه »).
#  - Jābir / Jabbār b. Ṣakhr : Muslim 3010 — EXACT (texte long complet sur dorar).
#  - Anas « صليت أنا ويتيم في بيتنا خلف النبي وأمي أم سليم خلفنا » : Bukhārī 727 / Muslim 658 — EXACT.
#  - Anas « صلى به وبأمه أو خالته فأقامني عن يمينه وأقام المرأة خلفنا » : Muslim 660 — EXACT
#    (min afrād Muslim).
#  - « إنما جعل الإمام ليؤتم به فلا تختلفوا عليه » (enrichissement, al-Muʿawna 1/252) : Ibn Mājah 846,
#    Aḥmad 8435/8889 — asluhu fī aṣ-Ṣaḥīḥayn : Bukhārī 689 / Muslim 417.
#
# Zone corrompue du CMS restaurée PAR DOCTRINE :
#  - le verset-source de la lecture avec l'imām (le CMS n'en garde que « الأعراف: 204 ») :
#    [verset reproduit en image dans le manuel : « Et quand le Coran est récité… » — al-Aʿrāf (7) : 204]
#    (guillemet warsh du quran-cache : وَإِذَا قُرِئَ الْقُرْءَانُ فَاسْتَمِعُوا لَهُ وَأَنصِتُوا لَعَلَّكُمْ تُرْحَمُونَ).
import json, re, sys

BOOK = 'content/books/fiqh-1es.json'
DOC = '11439'

html_fr = """
<h1>L'imāmat de la prière et ses règles (al-imāma wa-aḥkāmuhā) — leçon de fiqh de la Risāla d'Ibn Abī Zayd al-Qayrawānī avec le commentaire Kifāyat aṭ-ṭālib ar-rabbānī</h1>
<p>Leçon sur l'imāmat et ses règles, matière Fiqh, sur la base de la <em>Risāla</em> d'Ibn Abī Zayd al-Qayrawānī avec le commentaire d'Abū al-Ḥasan, <em>Kifāyat aṭ-ṭālib ar-rabbānī</em>, en marge de la <em>ḥāshiya</em> d'al-ʿAdawī — livre de l'élève (kitāb at-tilmīdh wa-t-talmīdha) de la première année de l'enseignement secondaire traditionnel (<em>ʿatīq</em>) — la quatorzième leçon.</p>
<p>Objectifs de la leçon :</p>
<ol>
<li>Connaître le rang de l'imāmat et les règles de l'imām et du suivi (<em>maʾmūm</em>).</li>
<li>Distinguer les règles de la prière en commun (<em>jamāʿa</em>).</li>
<li>Incarner les règles de la prière en commun dans mes prières.</li>
</ol>
<p>L'islam a pris soin du choix de l'exemplaire pieux et bon : il n'a pas confié la conduite des gens, et leur précédence dans la prière, à la noblesse de la lignée ni à la puissance de la richesse — il ne l'a confiée qu'à celui qui l'emporte sur les gens par son fiqh et sa science, sa droiture et sa piété.<br>
Qu'est-ce que l'imāmat, et quel est son rang ? Quelles sont les conditions de l'imāmat dans la prière ? Quelles sont les bornes du suivi du <em>maʾmūm</em> envers son imām ? Et quelle est la règle de l'imāmat de la femme ?</p>
<h2>Le texte (matn)</h2>
<p>Ibn Abī Zayd — que Dieu lui fasse miséricorde — a dit : « Chapitre de l'imāmat, et de la règle de l'imām et du suivi : »</p>
<p>« C'est le meilleur des gens, et le plus versé en fiqh, qui les conduit dans la prière ; la femme ne conduit ni une obligation ni une surérogation, ni des hommes ni des femmes. On récite avec l'imām dans ce qui se récite en secret ; on ne récite pas avec lui dans ce qui se récite à voix haute. Quiconque rejoint une rakʿa ou plus a atteint la prière en commun : qu'il acquitte, après la salutation de l'imām, ce qui lui a échappé, sur le mode de ce qu'a fait l'imām pour la récitation ; quant à la station et à l'assise, son agir est comme l'agir du reste. Quiconque a prié isolément peut répéter en commun, pour le mérite qu'il y a en cela — le maghrib seule exceptée ; quiconque a rejoint une rakʿa ou plus de la prière en commun ne la répète pas en commun ; et quiconque n'a rejoint que le tashahhud ou la prosternation peut la répéter en commun. »</p>
<p>« L'homme seul avec l'imām se tient à sa droite ; deux hommes ou plus se tiennent derrière lui. S'il y a une femme avec eux deux, elle se tient derrière eux deux ; s'il y a avec eux un homme, il prie à la droite de l'imām et la femme derrière eux deux. Quiconque prie avec son épouse : elle se tient derrière lui. L'enfant qui prie avec un homme unique derrière l'imām : tous deux se tiennent derrière lui — pourvu que l'enfant soit en âge de discerner : qu'il ne s'en aille pas et ne délaisse pas celui qui se tient avec lui. L'imām titulaire, s'il prie isolément, se tient à la place de la prière en commun ; il est blâmable, en toute mosquée ayant un imām titulaire, que la prière y soit célébrée deux fois ; et quiconque a prié une prière n'y conduit personne. »</p>
<p>« Quand l'imām omet et se prosterne pour son omission, que le suive, parmi ceux derrière lui, celui qui n'a pas omis avec lui. Nul ne relève sa tête avant l'imām, nul n'agit qu'après son acte : on n'ouvre qu'après lui, on ne se relève de l'assise des deux [rakʿa] qu'après son relèvement, on ne salue qu'après sa salutation ; tout le reste, il est loisible de le faire avec lui — et le faire après lui est plus beau. »</p>
<p>« Et toute omission qu'a commise le suivi, l'imām la porte pour lui — sauf une rakʿa, une prosternation, le takbīr d'ouverture, la salutation, ou la conviction de l'intention de l'obligation. Quand l'imām a salué, qu'il ne demeure pas après sa salutation et qu'il s'écarte — sauf s'il est en son lieu : c'est là une latitude. »</p>
<h2>La compréhension</h2>
<h3>Explication lexicale</h3>
<ul>
<li><em>yaʾummu</em> : conduire les gens — et avec les gens — dans la prière : les précéder et leur être imām.</li>
<li><em>yaʿqilu</em> : comprendre les règles de la prière et sa récompense.</li>
</ul>
<h3>Extraction des contenus du matn</h3>
<ul>
<li>Extrais du matn les règles de l'imāmat, de l'imām et du suivi.</li>
<li>Établis, à partir du matn, ce qui indique les règles de la prière en commun.</li>
<li>Détermine, au fil du matn, la règle de la répétition de la prière en commun.</li>
</ul>
<h2>L'analyse</h2>
<p>Cette leçon embrasse, des règles relatives à la prière en commun, ce qui suit :</p>
<h3>Premièrement : l'imāmat et les règles de l'imām et du suivi</h3>
<p>L'imāmat visé ici est l'imāmat de la prière : une charge légale (<em>manṣab sharʿī</em>) dont le titulaire tient lieu, pour l'affaire de la prière et les règles qui s'y rapportent, du commandant suprême (<em>al-imām al-aʿẓam</em>) ; et celui qui l'exerce obtient, à droit de sa charge, l'immense récompense. Les règles qui s'y rapportent :</p>
<h4>a. Les règles de l'imām</h4>
<p>L'imāmat a des conditions de validité et des conditions de perfection ; parmi elles, l'auteur mentionne que l'imām soit :</p>
<ul>
<li>un homme : l'imāmat de la femme n'est pas valable — ni dans une obligation ni dans une surérogation, ni pour des hommes ni pour des femmes ; quiconque l'a suivie, sa prière est à refaire à perpétuité selon l'école ;</li>
<li>responsable (<em>mukallaf</em>) : l'imāmat de l'enfant n'est pas valable, faute de majorité, ni celui de l'aliéné ni de l'ivre, faute de raison ;</li>
<li>capable, non incapable : l'imāmat de qui est incapable de certains piliers de la prière n'est pas valable [à la tête] de qui en est capable ;</li>
<li>connaisseur des règles fiqhiques touchant l'œuvre de la prière — l'ignorance à distinguer les obligations des sunna [de la prière] ne l'en empêche pas ;</li>
<li>préservé (<em>mastūr</em>) quant à la religion, non dépravé (<em>fāsiq</em>) ; il est nul de prier derrière un corrupteur de croyance ;</li>
<li>ne suivant pas un autre imām : il n'est pas valable qu'un retardataire ou un rejoignant suive un rejoignant. En cela, parole de l'auteur : « C'est le meilleur des gens, et le plus versé en fiqh, qui les conduit dans la prière ; la femme ne conduit ni une obligation ni une surérogation, ni des hommes ni des femmes. »</li>
</ul>
<h4>b. Les règles du suivi</h4>
<p>Des règles propres sont attachées au suivi ; parmi elles :</p>
<ul>
<li>le suivi récite avec l'imām dans la prière en secret, et ne récite pas avec lui dans [la prière] à voix haute ; s'il récite avec lui, sa prière n'est pas nulle. La source en est la parole de Dieu Très-Haut : [verset reproduit en image dans le manuel : « Et quand le Coran est récité, écoutez-le attentivement et observez le silence — peut-être vous sera-t-il fait miséricorde. » — al-Aʿrāf (7) : 204] ;</li>
<li>s'il rejoint, de la prière obligatoire, une rakʿa ou plus avec l'imām, il a atteint la prière en commun — atteint son mérite — en vertu de ce qu'il y a dans le Muwaṭṭaʾ de sa parole — paix et bénédiction sur lui — : « Quiconque rejoint une rakʿa de la prière a atteint la prière. » [Muwaṭṭaʾ, « chapitre de qui rejoint une rakʿa de la prière »] ;</li>
<li>s'il est de ceux qui rejoignent la prière en cours (<em>masbūq</em>), il acquitte ce qui lui a échappé après la salutation de son imām, sur le mode de ce qui lui a échappé, pour la récitation et le reste : là où l'imām a récité Umm al-Qurʾān et une sourate, il y récite de même ; là où l'imām a récité à voix haute, il récite à voix haute ; là où il a récité en secret, il récite en secret. Et il bâtit sur les actes : il fait de ce qu'il a rejoint avec l'imām le début de sa prière, et bâtit dessus. En tout cela, parole de l'auteur : « On récite avec l'imām dans ce qui se récite en secret… jusqu'à : son agir est comme l'agir du reste. » ;</li>
<li>s'il a prié isolément une obligation sans être imām titulaire, il lui est recommandé de la répéter en commun — sauf la prière du maghrib, et l'ʿishāʾ pour qui a prié le <em>witr</em>. Il la répète pour obtenir le mérite transmis en cela, en l'intention de s'en remettre à Dieu Très-Haut ; le Prophète — paix et bénédiction sur lui — a dit : « La prière en commun surpasse la prière de l'isolé (<em>al-fadhdh</em>) de vingt-sept degrés. » [Ṣaḥīḥ d'al-Bukhārī, « chapitre du mérite de la prière en commun ».] S'il a rejoint une rakʿa ou plus avec le groupe, il ne la répète pas dans un autre groupe ; et s'il n'a rejoint que le tashahhud ou la prosternation, il peut la répéter. En cela, parole de l'auteur : « Quiconque a prié isolément peut répéter en commun… jusqu'à : ou la prosternation — il peut la répéter en commun. » ;</li>
<li>il suit l'imām quand celui-ci omet dans sa prière, et se prosterne avec lui pour son omission, même sans avoir commis l'omission avec lui — pour ce qui est parvenu de ʿUmar, du Prophète — paix et bénédiction sur lui — : « Nulle omission sur qui est derrière l'imām : si l'imām omet, l'omission est sur lui et sur ceux derrière lui ; et si celui derrière l'imām omet, nulle omission sur lui : l'imām lui suffit. » [Sunan ad-Dāraquṭnī, « chapitre : nulle omission sur le suiveur ; sur lui, l'omission de l'imām »] ;</li>
<li>il ne relève pas sa tête de l'inclinaison ou de la prosternation avant l'imām — pour ce qui est dans les deux Ṣaḥīḥ de sa parole — paix et bénédiction sur lui — : « Ne craint-il pas, celui qui relève sa tête avant l'imām, que Dieu ne transforme sa tête en tête d'âne ? » [Ṣaḥīḥ de Muslim, « chapitre de l'interdiction de précéder l'imām dans l'inclinaison, la prosternation et leurs semblables »] ;</li>
<li>il lui est obligatoire, pour l'ouverture (<em>iḥrām</em>) et la salutation, de suivre son imām : dès qu'il le précède, ou l'égale en cela, sa prière est nulle ;</li>
<li>l'imām porte pour lui toute omission qu'il a commise en l'état de sa suite de l'imām — sauf les obligations : il ne les porte pas pour lui. En cela, parole de l'auteur : « Quand l'imām omet et se prosterne pour son omission, que le suive… jusqu'à : sauf une rakʿa, une prosternation, le takbīr d'ouverture, la salutation, ou la conviction de l'intention de l'obligation. »</li>
</ul>
<h3>Deuxièmement : les règles de la prière en commun</h3>
<p>La prière en commun dans les cinq [prières] est une sunna instante ; selon la Loi, elle commence à deux ; et le lieu de station du suivi varie selon le nombre des suivis, et selon qu'ils sont hommes ou femmes, comme suit :</p>
<ul>
<li>s'il n'y a avec l'imām qu'un homme, il se tient à sa droite — pour ce qui est parvenu d'Ibn ʿAbbās : « al-ʿAbbās m'envoya au Prophète — paix et bénédiction sur lui — alors qu'il était en la demeure de ma tante Maymūna ; je passai avec lui cette nuit-là. Il se leva pour prier une partie de la nuit ; je me levai à sa gauche ; il me prit par-derrière et me plaça à sa droite. » [Ṣaḥīḥ de Muslim, « chapitre de l'invocation dans la prière nocturne et de sa station »] ;</li>
<li>s'il y a avec lui deux hommes ou plus, ils se tiennent derrière lui — pour ce qui est parvenu de Jābir : « … Je vins et me tins à la gauche du Messager de Dieu — paix et bénédiction sur lui — ; il me prit par la main et me fit tourner jusqu'à me placer à sa droite. Puis Jabbār b. Ṣakhr vint, fit ses ablutions, puis vint se tenir à la gauche du Messager de Dieu — paix et bénédiction sur lui — ; le Messager de Dieu — paix et bénédiction sur lui — nous prit tous deux par les mains et nous poussa jusqu'à nous placer derrière lui. » [Ṣaḥīḥ de Muslim, « chapitre du long récit de Jābir et de l'histoire d'Abū al-Yasar »] ;</li>
<li>s'il y a une femme avec les deux hommes, elle se tient derrière eux — pour ce qui est dans le Ṣaḥīḥ d'Anas b. Mālik : « Moi et un orphelin, dans notre demeure, avons prié derrière le Prophète — paix et bénédiction sur lui —, et ma mère, Umm Sulaym, derrière nous. » [Ṣaḥīḥ d'al-Bukhārī, « chapitre : la femme seule forme un rang »] ;</li>
<li>s'il y a avec l'imām et la femme un homme, ou un enfant discernant, il prie à la droite de l'imām et la femme prie derrière eux — pour ce qui est parvenu d'Anas b. Mālik : « Le Messager de Dieu — paix et bénédiction sur lui — pria avec lui et sa mère ou sa tante. Il dit : il me plaça à sa droite, et plaça la femme derrière nous. » [Ṣaḥīḥ de Muslim, « chapitre de la permission de la prière en commun dans la surérogation, et de la prière sur une natte »].</li>
</ul>
<p>En cela, parole de l'auteur : « L'homme seul avec l'imām se tient à sa droite… jusqu'à : l'imām titulaire, s'il prie isolément, se tient à la place de la prière en commun. »</p>
<p>Il est blâmable, en toute mosquée ayant un imām titulaire, que la prière y soit célébrée deux fois — avant l'imām titulaire, avec lui ou après lui — car cela conduit à la haine et aux querelles. De même, il est blâmable à l'imām de demeurer au lieu de la prière dans la posture de la prière ; il lui est permis de le faire en sa demeure.</p>
<p>Et il n'est pas permis au prieur d'obligation de suivre le prieur de surérogation, faute d'égalité en la description de la prière. En cela, parole de l'auteur : « Il est blâmable, en toute mosquée ayant un imām titulaire, que la prière y soit célébrée deux fois… et quand l'imām a salué… jusqu'à : et qu'il s'écarte — sauf s'il est en son lieu : c'est là une latitude. »</p>
<p>Parmi les visées de l'institution de la prière en commun : la présence à l'esprit du principe de l'unité, et le mérite du rassemblement sur le bien — l'imām et le suivi s'entre-complètent au-dedans de la prière : l'imām dit « ni des égarés », et le suivi dit « āmīn » ; l'imām dit « Dieu entend qui Le loue », et le suivi dit « Notre Seigneur, à Toi la louange » ; le suivi omet dans sa prière, et l'imām la porte pour lui, comme au texte du hadith : « l'imām lui suffit ».</p>
<h2>L'évaluation</h2>
<ul>
<li>Établis la règle de l'omission du suivi derrière son imām.</li>
<li>Détermine quand l'enfant est pris en compte dans la prière en commun.</li>
<li>Explicite le lieu de station de la femme quand il n'y a qu'un homme avec l'imām.</li>
</ul>
<h2>L'enrichissement</h2>
<p>Le qāḍī ʿAbd al-Wahhāb — que Dieu lui fasse miséricorde — a dit :</p>
<p>« La divergence d'intention entre l'imām et le suivi a effet d'empêcher de le suivre. Si l'imām prie en surérogation, il n'est pas permis qu'on prie derrière lui une obligation ; il est permis au prieur de surérogation de suivre le prieur d'obligation. Si tous deux sont en une prière obligatoire, et que les deux obligations diffèrent, il n'est pas permis de le suivre. Ash-Shāfiʿī a dit, en tout cela : le suivre est permis. Notre preuve est sa parole — paix et bénédiction sur lui — : “L'imām n'a été institué que pour être suivi : ne divergez pas de lui” — et le texte est général. »</p>
<p>(<em>Al-Muʿawna</em>, t. I, p. 252.)</p>
<p>Résume les questions que tu as retirées de ce texte.</p>
<h2>La préparation préalable</h2>
<p>Lis le matn de la prochaine leçon et accomplis ce qui suit :</p>
<ul>
<li>Établis ce qui suffit à la femme, du vêtement, dans la prière.</li>
<li>Que fait le prieur s'il ajoute ou s'il retranche dans la prière ?</li>
<li>Quelle est la règle de celui chez qui se sont réunies, dans sa prière, l'addition et le retranchement ?</li>
</ul>
"""

# Typographie française : espaces fines insécables (U+202F) dans les guillemets
# et avant : ; ? ! — convention du corpus (leçons récentes).
html_fr = html_fr.replace('« ', '«\u202f').replace(' »', '\u202f»')
html_fr = re.sub(r' ([;?!])', '\u202f\\1', html_fr)
html_fr = html_fr.replace(' :', '\u202f:')
html_fr = html_fr.strip()

book = json.load(open(BOOK))
found = False
for d in book['lessons']:
    if d['docId'] == DOC:
        d['htmlFr'] = html_fr
        d['titleFr'] = "L'imāmat de la prière et ses règles"
        found = True
        print(f"OK: {DOC} -> htmlFr ({len(html_fr)} car), titleFr mis à jour")
if not found:
    sys.exit(f"ERREUR: {DOC} introuvable dans {BOOK}")
json.dump(book, open(BOOK, 'w'), ensure_ascii=False, indent=2)
print(f"{BOOK} réécrit.")

# Registre savant : ajout de 11439 à hand[]
REG = 'scripts-translate/savant-registry.json'
reg = json.load(open(REG))
if DOC not in reg['hand']:
    reg['hand'].append(DOC)
    json.dump(reg, open(REG, 'w'), ensure_ascii=False, indent=2)
    print(f"Registre: {DOC} ajouté à hand ({len(reg['hand'])} entrées)")
else:
    print(f"Registre: {DOC} déjà présent")

# Contrôle qualité immédiat
arabic = re.findall(r'[\u0600-\u06FF]+', html_fr)
print('Caractères arabes résiduels:', len(arabic), arabic[:5] if arabic else '')
print('Guillemets « :', html_fr.count('«'), '| » :', html_fr.count('»'))

#!/usr/bin/env python3
"""R736 — ajoute les commentaires pédagogiques des leçons 9-10 de hadith-tanawi-1
(12981 أحكام الظهار — les dispositions du ẓihār, la quatorzième du manuel ;
12990 أحكام الصداق والحباء — les décisions de la dot et du ḥibāʾ, la dixième
du livre, étiquetée « (leçon 3) » par le manuel)
à content/commentaires/hadith-tanawi-1.json.
Vague 20 : les slots exacts 12981=leçon 9 et 12990=leçon 10 (le SUIVANT de
R735, vérifié dans l'ordre des lessons du registre : 12925, 12934, 12936,
12957, 12959, 12966, 12967, 12971, puis 12981 et 12990). Même protocole que
comm-r735.py : normalisation de la ponctuation FR (U+202F avant ; : ! ? » et
après «, apostrophe courbée) sur les entrées nouvelles seulement — opération
idempotente. Rédaction d'après la lecture complète des deux leçons (htmlFr
intégral, 28 505 et 16 199 caractères, extraction non lossy
scripts/extrait-r736.py, couche arabe lue pour les formes du vocabulaire et
pour l'éclairage des termes que la couche FR de la leçon 12990 rend
mécaniquement — le ḥibāʾ par « l'amour », « l'ami », « l'amant » ; consigné
au worklog, règle 5 : la zone est celle d'IA-3). Les numéros du Muwaṭṭaʾ
(1646, 1647, 1650, 1653, 1654, 1655 ; 1752, 1753, 1756, 1757, 1759, 1760),
les citations (Khawla bint Thaʿlaba, ʿUmar, al-Qāsim ibn Muḥammad,
Sulaymān ibn Yasār, Ibn ʿArafa, le Qāḍī Abū Muḥammad, ʿAbd al-Malik, Ibn
al-Mawwāz, la Mudawwana, Barwaʿ bint Wāshiq, al-Masīs, « cherche même un
anneau de fer », ʿUmar ibn ʿAbd al-ʿAzīz, Ibn al-Qāsim, al-Mujādila 1-4,
4:20, 4:24-25, la sourate al-Baqara verset 235), les statuts et les
estimations (dīnār 4,25 g, quart 1,0625 g d'or, dirham 2,975 g ou 3,12 g
d'argent, mudd ≈ trois quarts de litre) sont cités tels qu'ils figurent dans
les leçons (règle 2 de LISEZ-MOI.md : aucune invention). Les formes arabes
du vocabulaire sont posées au squelette standard SANS harakat, reprises de
la couche arabe des leçons ; aucune harakat n'est inventée (règle 2). Les ʿ
et ʾ (U+02BF / U+02BE) sont posés directement dans les champs FR pour les
noms propres et les fragments de translittération — la normalisation ne les
touche pas."""
import json, re

CHEMIN = 'content/commentaires/hadith-tanawi-1.json'

E_12981 = {
    "auteur": "IA-1, tour R736",
    "resume": ("Guide de lecture de la leçon 9 (أحكام الظهار — les dispositions du ẓihār), la quatorzième du manuel : deux hadiths du Muwaṭṭaʾ "
               "arment le fond (le n° 1752 — al-Qāsim ibn Muḥammad rapporte la sentence de ʿUmar ibn al-Khaṭṭāb sur l'homme qui fit d'une femme "
               "« ce qui est sur lui comme le dos de sa mère, à la condition de l'épouser » : « s'il l'épouse, qu'il ne la touche point jusqu'à ce "
               "qu'il s'acquitte de l'expiation du ẓāhir » — le ẓihār suspendu au mariage tient lieu du ẓihār réalisé ; le n° 1760 — le dire compilé "
               "de Mālik sur le verset 3 : la résolution de garder et de toucher fait tomber l'expiation à sa charge, la répudiation sans résolution "
               "n'en demande point — « s'il l'épouse après cela, qu'il ne la touche point jusqu'à ce qu'il s'acquitte »), le n° 1753 les prolonge "
               "(al-Qāsim et Sulaymān ibn Yasār sur le ẓihār fait avant l'épouse), et trois textes d'exploitation (n° 1756, 1757 et 1759) règlent la "
               "multiplication de l'expiation, l'attouchement avant elle et la négation du ẓihār des femmes. Le préambule enracine la leçon dans le "
               "récit de Khawla bint Thaʿlaba — qu'Allah l'agrée — : son mari, ʿAwf ibn aṣ-Ṣāmit (l'imprimé porte « Aws »), homme âgé au caractère "
               "gâté, lui dit « Tu es pour moi comme le dos de ma mère » — « et voici que, par là, il voulait mon éloignement de lui » ; elle sortit, "
               "vint au Messager de Dieu — paix et bénédiction sur lui — et se mit à se plaindre du mauvais caractère qu'elle subissait ; le Prophète "
               "lui dit « Ô Khawla, le fils de ton oncle paternel est un homme âgé ; crains donc Dieu à son sujet » ; elle insista : « Par Dieu, je ne "
               "cessai point jusqu'à ce que le Coran descendît sur moi » — l'ouverture de la sourate al-Mujādila (versets 1-4), reproduite en image "
               "dans le manuel et restaurée verbatim au cache coranique (la référence imprimée, « versets 1-4 », concorde ; le partage restauré — "
               "versets 1-2, puis 3-4 — reconstruit d'après la mise en page de l'imprimé) : « Allah a bien entendu la parole de celle qui discutait "
               "avec toi à propos de son époux et se plaignait à Allah » (verset 1), la condamnation — « ils prononcent certes une parole blâmable et "
               "mensongère » (verset 2) — et l'expiation graduée — affranchir un esclave, jeûner deux mois consécutifs, nourrir soixante pauvres "
               "(versets 3-4). C'est de l'appel de Khawla — « celle qui discutait » (al-mujādila) — que la sourate porte son nom ; le récit est "
               "rapporté par l'imam Aḥmad dans son Musnad. Trois objectifs : reconnaître le concept du ẓihār et ses formules, distinguer ce que "
               "dénote chacune des formules, m'appliquer à éviter tout ce qui conduit au ẓihār. L'analyse déroule la doctrine en deux mouvements. Le "
               "concept : en langue, le maṣdar de figure muʿāfaṭa dérivé du dos (aẓ-ẓahr) — faire face son dos à son dos au propre, se mettre en "
               "colère, appuyer (« il a fortifié son dos » pour dire qu'on l'a secouru), interposer un dos entre deux vêtements ; en terme, la "
               "description que fait le ẓāhir — celui dont la cohabitation avec elle est licite — de sa femme comme étant sur lui comme le dos de sa "
               "mère ; Ibn ʿArafa l'a défini — « la comparaison de l'épouse en titre, ou de l'esclave concubine dont la cohabitation lui est licite, à "
               "l'un de ses interdits, ou au dos d'une étrangère, dans la jouissance qu'il en prend — la partie tient lieu du tout, et le suspendu "
               "tient lieu du réalisé » : deux règles du raisonnement analogique (qiyās) qui armeront le ẓihār conditionnel. Les formules : "
               "l'originaire — « tu es pour moi comme le dos de ma mère » — fait l'unanimité ; elle se spécialise par la mère et par le dos, et le "
               "détour se fait selon trois faces : l'organe de la mère autre que le dos (Mālik : ẓāhir en tout — le Qāḍī Abū Muḥammad : « quiconque "
               "compare une femme à un organe de sa mère est ẓāhir » ; ash-Shāfiʿī : point de ẓihār sinon par le dos ; Abū Ḥanīfa : un organe dont le "
               "regard sur lui est interdit) ; le dos d'une autre que la mère (interdite : ẓāhir selon Mālik ; étrangère : ẓāhir qu'elle ait ou non un "
               "époux, contre ʿAbd al-Malik qui en fait divorce — « cette interdiction n'advient que par la levée du contrat de licéité, et cette "
               "levée n'advient que par le divorce » — et contre Abū Ḥanīfa et ash-Shāfiʿī : ni divorce ni ẓihār) ; autre que le dos, d'une autre que "
               "la mère (interdite par lignage, alliance ou allaitement : ẓihār au statut du précédent ; l'étrangère : de même). Les dispositions "
               "ouvrent par le ẓihār avant le mariage — conditionnel (« si je t'épouse... ») il oblige s'il l'épouse, nu il n'oblige point (al-Qāsim "
               "et Sulaymān ibn Yasār, n° 1753 ; ash-Shāfiʿī et ath-Thawrī : point de ẓihār qui l'oblige dans les deux faces). L'expiation est de "
               "trois espèces graduées — la deuxième ne dispense que si incapable de la première, la troisième que si incapable de la deuxième — le "
               "jeûne de deux mois consécutifs (la continuité (tatābuʿ) : Ibn al-Mawwāz — rompu en voyage, recommencé à neuf ; rompu pour maladie, "
               "rebâti une fois guéri ; ash-Shāfiʿī fait recommencer aussi l'oublieux et le malade — la réponse : « on ne peut s'en garantir, et il "
               "n'advient point par son choix », comme la pollution nocturne ; l'abstention de l'épouse dont le ẓihār a été fait et l'expiation avant "
               "l'attouchement — cohabitation de jour, avec elle ou avec une autre : recommence ; la Mudawwana contre ash-Shāfiʿī : « s'il la touche "
               "de nuit, son jeûne n'est point rompu »), la nourriture de soixante pauvres (un mudd et deux tiers chacun, du mudd du Prophète — paix "
               "et bénédiction sur lui ; Abū Ḥanīfa : un seul pauvre soixante jours, « soixante trous » — la réponse : Dieu a spécifié le nombre des "
               "pauvres, « le texte explicite n'est point délaissé pour un sens qu'on en tire » — « une branche qui retourne à sa racine en nullité : "
               "elle est plus digne encore de la nullité »), et l'affranchissement du cou — « il n'en demeure plus rien ; car l'Islam, depuis sa "
               "venue, s'est fait un zèle d'affranchir les gens et d'en finir avec la servitude ». L'exploitation imprime les n° 1756 (les conseils "
               "séparés : point sur lui qu'une seule expiation ; après acquittement, l'expiation « pareillement »), 1757 (qui la touche avant "
               "acquittement : une seule expiation, qu'il se retienne et demande pardon — Mālik : « et cela est le plus beau que j'aie entendu ») et "
               "1759 (« et point de ẓihār sur les femmes »). La préparation annonce le khulʿ — le ghiṣl (al-ghils) et « quelle est ta situation ? » "
               "(mā shaʾnuk) — déjà rencontré à la leçon du divorce de la femme investie du commandement d'elle-même."),
    "explication": [
        ("La leçon 9 (la quatorzième du manuel) traite les dispositions du ẓihār — la comparaison de l'épouse au dos de la mère. Le préambule "
         "enracine la question dans le récit de Khawla bint Thaʿlaba — qu'Allah l'agrée — : « C'est en moi — par Dieu — et en ʿAwf ibn aṣ-Ṣāmit que "
         "Dieu fit descendre le début (ṣadr) de la sourate al-Mujādila » ; elle décrit : un homme âgé, dont le caractère s'était gâté, qui entra "
         "chez elle, se fâcha et dit « Tu es pour moi comme le dos de ma mère » — « et voici que, par là, il voulait mon éloignement de lui » ; elle "
         "sortit, vint au Messager de Dieu — paix et bénédiction sur lui — et se mit à se plaindre du mauvais caractère qu'elle subissait de sa "
         "part ; le Prophète lui dit : « Ô Khawla, le fils de ton oncle paternel est un homme âgé ; crains donc Dieu à son sujet » — le « fils de "
         "ton oncle paternel » (ibn ʿammik) en fait le cousin paternel de Khawla ; elle insista : « Par Dieu, je ne cessai point jusqu'à ce que le "
         "Coran descendît sur moi » — l'ouverture de la sourate al-Mujādila, reproduite en image dans le manuel et restaurée verbatim au cache "
         "coranique (la référence imprimée sous les images, « la sourate al-Mujādila, versets 1-4 », concorde) : « Allah a bien entendu la parole de "
         "celle qui discutait avec toi à propos de son époux et se plaignait à Allah » (verset 1), puis la condamnation — « Ceux d'entre vous qui "
         "répudient leurs femmes, en déclarant qu'elles sont pour eux comme le dos de leurs mères, alors qu'elles ne sont nullement leurs mères... "
         "Ils prononcent certes une parole blâmable et mensongère. Allah cependant est Indulgent et Pardonneur » (verset 2) — puis l'expiation — "
         "affranchir un esclave avant tout contact, jeûner deux mois consécutifs, nourrir soixante pauvres (versets 3-4). C'est de l'appel de "
         "Khawla — « celle qui discutait » (al-mujādila) — que la sourate porte son nom : la plainte de l'épouse ẓāhira a ouvert la sourate tout "
         "entière ; le récit est rapporté par l'imam Aḥmad ibn Ḥanbal dans son Musnad. Trois objectifs : reconnaître le concept du ẓihār et ses "
         "formules ; distinguer ce que dénote chacune des formules ; m'appliquer à éviter tout ce qui conduit au ẓihār."),
        ("Les hadiths arment les règles du fond. Le n° 1752 — Saʿīd ibn ʿAmr ibn Sulaym az-Zuraqī, Successeur médinois, interroge al-Qāsim ibn "
         "Muḥammad — petit-fils du premier calife et neveu de ʿĀʾisha — : « Un homme fit d'une femme ce qui est sur lui comme le dos de sa mère, à "
         "la condition de l'épouser ; ʿUmar ibn al-Khaṭṭāb — qu'Allah l'agrée — lui ordonna, s'il l'épousait, de ne point l'approcher jusqu'à ce "
         "qu'il s'acquitte de l'expiation du ẓāhir » — le ẓihār suspendu au mariage tient lieu du ẓihār réalisé dès que le mariage survient : c'est "
         "la seconde règle de la définition d'Ibn ʿArafa. Le n° 1760 — le dire compilé de Mālik sur la parole du Très Haut « ceux qui comparent "
         "leurs femmes au dos de leurs mères puis reviennent sur ce qu'ils ont dit » (verset 3) : « J'ai entendu l'interprétation de cela : que "
         "l'homme fasse ẓihār de son épouse, puis se résolve sur le fait de la garder et de la toucher ; s'il se résout sur cela, l'expiation tombe "
         "à sa charge ; et s'il la répudie et ne se résout pas, après son ẓihār d'elle, sur le fait de la garder et de la toucher, point d'expiation "
         "sur lui » — la résolution de garder et de toucher est le moment qui déclenche l'expiation ; et Mālik de conclure : « S'il l'épouse après "
         "cela, qu'il ne la touche point jusqu'à ce qu'il s'acquitte de l'expiation du ẓāhir ». Le n° 1753 réunit al-Qāsim ibn Muḥammad et "
         "Sulaymān ibn Yasār — l'autre grand jurisconsulte médinois du cercle des affranchis du Prophète — paix et bénédiction sur lui — au sujet "
         "d'un homme qui fit ẓihār de son épouse avant de l'épouser : « s'il l'épouse, qu'il ne la touche point jusqu'à ce qu'il s'acquitte de "
         "l'expiation du ẓāhir »."),
        ("Le concept répond à la première question. En langue : le maṣdar de figure muʿāfaṭa, dérivé du dos (aẓ-ẓahr) ; il peut viser des sens "
         "divers, tous ramenés au dos en signification et en forme, selon la diversité des buts. On dit ẓāhartu fulānan quand on a fait face son "
         "dos à son dos, au sens propre, et aussi quand on s'est mis en colère contre lui ; on dit qu'on l'a appuyé quand on l'a secouru — « il a "
         "fortifié son dos » pour dire qu'il l'a secouru ; on dit qu'il a fait ẓihār de son épouse quand il lui a dit « tu es pour moi comme le dos "
         "de ma mère » ; et on dit qu'il a interposé un dos entre deux vêtements quand il en a porté l'un sur l'autre. En terme : la description "
         "que fait le ẓāhir — celui dont la cohabitation avec elle est licite — de sa femme comme étant sur lui comme le dos de sa mère. Ibn ʿArafa "
         "— Aḥmad ibn Muḥammad ibn ʿArafa al-Wargammī, mort en 803/1400, le dernier des grands mālikites maghrébins, auteur des Muntakhabāt — l'a "
         "défini : « la comparaison de l'épouse en titre, ou de l'esclave concubine dont la cohabitation lui est licite, à l'un de ses interdits, "
         "ou au dos d'une étrangère, dans la jouissance qu'il en prend — la partie tient lieu du tout, et le suspendu tient lieu du réalisé » "
         "(al-juʾz ka-l-kull wa-l-muʿallaq ka-l-ḥāṣil) : deux règles du raisonnement analogique (qiyās) — la comparaison à une partie de la "
         "personne interdite tient lieu de la comparaison à sa personne entière, et la comparaison suspendue à une condition (« si je t'épouse ») "
         "tient lieu de la comparaison réelle dès que la condition se remplit ; c'est cette seconde règle qui fonde le statut du ẓihār avant le "
         "mariage."),
        ("Les formules répondent à la seconde question. La formule originaire du ẓihār est le dire du ẓāhir « tu es pour moi comme le dos de ma "
         "mère » — l'origine en est la parole du Très High — et les jurisconsultes s'accordent qu'elle dénote le ẓihār sans dispute ; quant aux "
         "autres formules, on a divergé sur leur dénotation. La formule se spécialise par deux choses : par la mère, et par le dos. Si l'on s'en "
         "détourne, le détour se fait selon trois faces. La première — la comparaison suspendue à un organe de la mère autre que le dos : l'imam "
         "Mālik tient qu'il est ẓāhir, comme s'il disait « tu es pour moi comme la tête de ma mère », ou « le ventre », « la vulve », « le pied », "
         "« la cuisse », « le haut du bras » — « dans la Mudawwana, il est ẓāhir en tout cela » ; le Qāḍī Abū Muḥammad — ʿAbd al-Malik ibn "
         "al-Mājishūn, mort en 212/827, qāḍī de La Mecque, l'un des plus éminents compagnons de Mālik — : « quiconque compare une femme à un organe "
         "de sa mère est ẓāhir », et la preuve : « c'est un organe d'une personne interdite dont il a établi à son épouse le statut ; il faut donc "
         "qu'il soit ẓāhir comme le dos » ; ash-Shāfiʿī : il n'est point ẓāhir sinon par la comparaison au dos ; Abū Ḥanīfa : il n'y a de ẓihār que "
         "dans la comparaison à un organe de sa mère dont le regard sur lui est interdit."),
        ("La deuxième face — la comparaison suspendue au dos d'une autre que la mère : si la femme nommée est du nombre de ses interdits, il est "
         "ẓāhir selon Mālik ; si elle est une étrangère, Mālik : il est ẓāhir, qu'elle ait ou non un époux ; ʿAbd al-Malik : c'est divorce — « la "
         "voie du dire de ʿAbd al-Malik sur le ẓihār tient à ce que cela ne se rapporte qu'à l'interdiction permanente ; or cette interdiction "
         "n'advient que par la levée du contrat de licéité, et cette levée n'advient que par le divorce » — l'avis que l'analyse rapporte au nom de "
         "ʿAbd al-Malik est celui du Qāḍī Abū Muḥammad lui-même, qui en donne aussi la preuve : « il a comparé son épouse au dos d'une femme qui "
         "lui est interdite, et le statut du ẓihār l'a suivi — son origine est son dire : “comme le dos de ma mère” » ; Abū Ḥanīfa et ash-Shāfiʿī : "
         "ce n'est ni divorce ni ẓihār. La troisième face — la comparaison suspendue à autre que le dos, d'une autre que la mère : rapportée à une "
         "personne interdite par lignage, par alliance ou par allaitement, cela est ẓihār, au statut qui a précédé en la comparaison au dos d'une "
         "autre que la mère ; et il en va de même de l'étrangère. Les dispositions ouvrent par le ẓihār avant le mariage : s'il dit « si je "
         "t'épouse, tu es pour moi comme le dos de ma mère », voilà celle dont le ẓihār l'oblige, s'il l'épouse ; s'il dit « tu es pour moi comme "
         "le dos de ma mère » sans ajouter cela au fait de l'épouser, rien ne l'oblige — la preuve : celui-ci a ajouté le ẓihār à l'état de "
         "mariage, il faut donc qu'il l'oblige quand l'état de mariage existe, l'origine en étant le cas où il le dit à son épouse ; al-Qāsim ibn "
         "Muḥammad et Sulaymān ibn Yasār : « s'il l'épouse, qu'il ne la touche point jusqu'à ce qu'il s'acquitte de l'expiation du ẓāhir » (n° "
         "1753) ; ash-Shāfiʿī et ath-Thawrī : point de ẓihār qui l'oblige dans les deux faces."),
        ("L'expiation déroule la seconde partie. Le dire de Mālik dans le hadith — « s'il l'épouse après cela, qu'il ne la touche point jusqu'à ce "
         "qu'il s'acquitte de l'expiation du ẓāhir » — dénote l'obligation de l'expiation sur le ẓāhir ; elle est de trois espèces, dans un ordre "
         "tel que la deuxième ne le dispense que s'il a été incapable de la première, et la troisième que s'il a été incapable de la deuxième — "
         "cela est explicite du Coran (versets 3-4). Le jeûne de deux mois consécutifs porte deux règles. La première, la continuité (tatābuʿ) : "
         "que le jeûne des deux mois se tienne d'un trait, sans qu'une rupture quelconque s'y interpose — rupture sans excuse ; Ibn al-Mawwāz : "
         "« celui qui rompt le jeûne en son voyage, dans le jeûne du ẓihār, recommence à neuf ; s'il rompt pour maladie, il rebâtit une fois "
         "guéri » — la différence entre les deux : au voyageur, la rupture n'a point été rendue licite pour incapacité, mais pour alléger la gêne "
         "— or la continuité est du chapitre de la gêne, et elle lui a été posée comme condition ; quant au malade, la rupture ne lui a été permise "
         "que pour incapacité de jeûner, comme la menstruée ; et de même celui qui rompt par oubli, car l'oublieux est excusé. ash-Shāfiʿī : s'il "
         "rompt par oubli ou par maladie, il recommence le jeûne à neuf ; on lui a répondu : on ne peut s'en garantir, et il n'advient point par "
         "son choix — il ne rompt donc point la continuité, comme la pollution nocturne."),
        ("La deuxième règle : que les deux mois soient exempts de la cohabitation de l'épouse dont le ẓihār a été fait, et que l'expiation précède "
         "cela — cela exige que le jeûne s'accomplisse tout entier avant l'attouchement ; s'il cohabite, au cours de son jeûne, de nuit ou de jour, "
         "avec celle dont le ẓihār a été fait — ou avec une autre, de jour —, il recommence le jeûne à neuf ; la Mudawwana, contre ash-Shāfiʿī, "
         "dit : « s'il la touche de nuit, son jeûne n'est point rompu » ; la preuve du premier dire : le verset en a fait une condition du jeûne "
         "qui lui est dû et par lequel il se délivre du statut du ẓihār. Si le ẓāhir n'est point capable de jeûner, il nourrit soixante pauvres "
         "avant que tous deux ne se touchent — emportant l'absolu sur le restreint —, pour chaque pauvre un mudd et deux tiers, du mudd du Prophète "
         "— paix et bénédiction sur lui —, la mesure de grain de Médine dont l'estimation reçue en l'école est de l'ordre de trois quarts de litre. "
         "Il n'est point de désaccord chez les Mālikites que ce nombre est pris en compte, et que rien au-dessous ne dispense — fût-il le montant "
         "de la nourriture des soixante : c'est le dire d'ash-Shāfiʿī ; Abū Ḥanīfa : « s'il nourrit un seul pauvre soixante jours, cela le "
         "dispense, car il a rempli soixante trous — soixante bouches —, et c'est cela que la Loi vise » — le « trou » (khalla) est la bouche ; on "
         "lui a répondu : Dieu — le Très Haut — a spécifié le nombre des pauvres ; « le texte explicite n'est point délaissé pour un sens qu'on en "
         "tire, car c'est une branche qui retourne à sa racine en nullité : elle est plus digne encore de la nullité ». Quant à l'affranchissement "
         "du cou, il n'en demeure plus rien : « l'Islam, depuis sa venue, s'est fait un zèle d'affranchir les gens et d'en finir avec la servitude "
         "» — la première marche de l'échelle est aujourd'hui sans cause, l'esclavage étant aboli."),
        ("L'exploitation imprime trois textes qui règlent l'application. Le n° 1756 — l'homme qui fait ẓihār de son épouse en des conseils "
         "séparés : « point sur lui qu'une seule expiation ; s'il fait ẓihār, puis s'acquitte, puis fait ẓihār après s'être acquitté, l'expiation "
         "est sur lui pareillement » — l'expiation se multiplie par la répétition du ẓihār après acquittement, non par la répétition de la formule "
         "avant lui. Le n° 1757 — celui qui la touche avant de s'acquitter : « point sur lui qu'une seule expiation ; qu'il se retienne d'elle "
         "jusqu'à ce qu'il s'acquitte, et qu'il demande pardon à Dieu » ; Mālik : « et cela est le plus beau que j'aie entendu » — l'attouchement "
         "avant l'expiation n'oblige point une seconde expiation, mais la retenue jusqu'à l'acquittement. Le n° 1759 : « et point de ẓihār sur les "
         "femmes » — l'expiation est l'office du ẓāhir. La préparation annonce le khulʿ — la leçon suivante du manuel : expliquer le ghiṣl "
         "(al-ghils — le reste de l'obscurité de la nuit) et « quelle est ta situation ? » (mā shaʾnuk — « quel est ton ordre et ton état ? »), et "
         "extraire des hadiths de la leçon quelques décisions du khulʿ — déjà rencontré à la leçon du divorce de la femme investie du commandement "
         "d'elle-même (ṭalāq al-mumallaka), où figuraient « je suis libérée de toi » et la contrepartie."),
    ],
    "points": [
        ("Fil de révision : trois objectifs (le concept et ses formules ; ce que dénote chacune ; s'appliquer à éviter ce qui conduit au ẓihār) → "
         "préambule (Khawla bint Thaʿlaba, ʿAwf ibn aṣ-Ṣāmit, al-Mujādila 1-4 — la sourate nommée d'elle)."),
        ("Les versets : la condamnation (verset 2 — « une parole blâmable et mensongère ») et l'expiation graduée (versets 3-4) ; l'imprimé porte "
         "« à partir du verset 3 » pour la formule originaire — le verset de la comparaison littérale est le verset 2 ; le texte du Muwaṭṭaʾ porte "
         "la forme V (yu-ẓāhhirūna) là où le muṣḥaf porte la forme III (yu-ẓāhirūna) — variante du même lexème, sans portée sur le sens."),
        ("Le concept : en langue maṣdar de figure muʿāfaṭa dérivé du dos — face à face au propre, colère, secours (« il a fortifié son dos »), "
         "interposition entre deux vêtements ; en terme la description du ẓāhir ; la définition d'Ibn ʿArafa (m. 803/1400, les Muntakhabāt) — "
         "« la partie tient lieu du tout, et le suspendu tient lieu du réalisé »."),
        ("Détour (1) — organe de la mère autre que le dos : Mālik ẓāhir en tout (la Mudawwana) ; le Qāḍī Abū Muḥammad (ʿAbd al-Malik ibn "
         "al-Mājishūn, m. 212/827) — « un organe d'une personne interdite dont il a établi à son épouse le statut » ; ash-Shāfiʿī — le dos seul ; "
         "Abū Ḥanīfa — l'organe au regard interdit."),
        ("Détour (2) — dos d'une autre que la mère : interdite → ẓāhir selon Mālik ; étrangère → ẓāhir (Mālik, épouse ou non), divorce "
         "(ʿAbd al-Malik — l'interdiction permanente n'advient que par la levée du contrat de licéité, laquelle n'advient que par le divorce), ni "
         "divorce ni ẓihār (Abū Ḥanīfa, ash-Shāfiʿī)."),
        ("Détour (3) — autre que le dos, d'une autre que la mère : interdite (lignage, alliance, allaitement) → ẓihār au statut du précédent ; "
         "l'étrangère de même."),
        ("Le ẓihār avant le mariage : conditionnel → oblige s'il l'épouse (le suspendu tient lieu du réalisé ; n° 1753 — al-Qāsim et Sulaymān ibn "
         "Yasār) ; nu → rien ; ash-Shāfiʿī et ath-Thawrī : rien dans les deux faces."),
        ("L'expiation : trois espèces graduées — l'affranchissement (aujourd'hui sans cause — « le zèle de l'Islam d'affranchir les gens et d'en "
         "finir avec la servitude »), le jeûne de deux mois consécutifs, la nourriture de soixante pauvres à un mudd et deux tiers chacun."),
        ("Le jeûne : la continuité (tatābuʿ) — voyage → à neuf (dispense pour la gêne, la continuité en fait partie), maladie → rebâtit une fois "
         "guéri (incapacité, comme la menstruée), l'oublieux excusé — contre ash-Shāfiʿī qui fait recommencer (« comme la pollution nocturne ») ; "
         "la seconde règle — abstention de l'épouse, expiation avant attouchement — cohabitation de jour → recommence ; la Mudawwana : « la nuit "
         "ne rompt point » ; soixante pauvres — Abū Ḥanīfa « soixante trous » (khalla) — « une branche qui retourne à sa racine en nullité »."),
        ("L'exploitation : n° 1756 — la multiplication après acquittement ; n° 1757 — l'attouchement avant l'expiation : une seule, se retenir, "
         "demander pardon — « et cela est le plus beau que j'aie entendu » ; n° 1759 — « et point de ẓihār sur les femmes » ; la préparation "
         "annonce le khulʿ (ghiṣl, mā shaʾnuk)."),
    ],
    "vocabulaire": [
        {"ar": "الظهار", "translit": "al-ẓihār",
         "fr": "la comparaison de l'épouse au dos de la mère — en langue maṣdar de figure muʿāfaṭa dérivé du dos ; en terme la description que fait le ẓāhir de sa femme comme étant sur lui comme le dos de sa mère"},
        {"ar": "الظهر", "translit": "aẓ-ẓahr",
         "fr": "le dos — la racine du ẓihār : faire face son dos à son dos au propre, se mettre en colère, secourir (« il a fortifié son dos »), interposer un dos entre deux vêtements"},
        {"ar": "مفاعلة", "translit": "muʿāfaṭa",
         "fr": "la figure du maṣdar (ẓāhara) — le ẓihār se mesure sur muʿāfaṭa, tous les sens ramenés au dos « en signification et en forme, selon la diversité des buts »"},
        {"ar": "المتظاهر", "translit": "al-mutaẓāhir",
         "fr": "celui qui a fait ẓihār — l'expiation est posée sur lui : « s'il l'épouse, qu'il ne la touche point jusqu'à ce qu'il s'acquitte de l'expiation du ẓāhir » (n° 1752)"},
        {"ar": "كفارة", "translit": "kaffāra",
         "fr": "l'expiation — trois espèces graduées : l'affranchissement (aujourd'hui sans cause), le jeûne de deux mois consécutifs, la nourriture de soixante pauvres ; la seconde ne dispense que si incapable de la première, la troisième que si incapable de la deuxième"},
        {"ar": "التتابع", "translit": "at-tatābuʿ",
         "fr": "la continuité — « du chapitre de la gêne » : le jeûne des deux mois se tient d'un trait, sans rupture sans excuse ; rompu en voyage → recommence à neuf ; rompu pour maladie → rebâtit une fois guéri"},
        {"ar": "شهرين متتابعين", "translit": "shahrayni mutatābiʿayni",
         "fr": "deux mois consécutifs — l'origine en est le verset 4 de la sourate al-Mujādila ; les deux mois exempts de la cohabitation de l'épouse dont le ẓihār a été fait, et l'expiation avant l'attouchement"},
        {"ar": "ستين مسكينا", "translit": "sittīna miskīnan",
         "fr": "soixante pauvres — pour chaque pauvre un mudd et deux tiers, du mudd du Prophète — paix et bénédiction sur lui ; le nombre est spécifié par le texte explicite — rien au-dessous ne dispense, fût le montant de la nourriture des soixante"},
    ],
    "avertissement": "Ce commentaire est un guide de lecture du manuel ; en cas de divergence d'expression, le manuel et sa traduction savante font foi.",
}

E_12990 = {
    "auteur": "IA-1, tour R736",
    "resume": ("Guide de lecture de la leçon des décisions de la dot et du ḥibāʾ (أحكام الصداق والحباء — aḥkām aṣ-ṣadāq wa-l-ḥibāʾ), la dixième du "
               "livre — le manuel l'étiquette « (leçon 3) » : trois textes du Muwaṭṭaʾ arment le fond (le n° 1646 — la fille dʿUbayd Allāh ibn ʿUmar, "
               "sa mère étant la fille de Zayd ibn al-Khaṭṭāb, mariée à un fils dʿAbd Allāh ibn ʿUmar, dont le mari mourut sans consommer et sans "
               "désigner de dot ; l'arbitrage de Zayd ibn Thābit : « point de dot pour elle, et à elle l'héritage » ; le n° 1653 — la sentence "
               "dʿUmar : « si les rideaux sont relâchés, la dot est obligée » ; le n° 1647 — la lettre de ʿUmar ibn ʿAbd al-ʿAzīz à l'un de ses "
               "ouvriers : tout ce que stipule celui qui marie, père ou autre, « de ḥibāʾ ou de karama », c'est à la femme si elle le demande). La "
               "traduction de la leçon rend le ḥibāʾ par « l'amour », « l'ami » ou « l'amant » — lire toutes ces occurrences sur le fil arabe : le "
               "ḥibāʾ est le don sans compensation. L'analyse déroule la doctrine en deux parties. Première — les décisions de la dot : celle dont "
               "le mari est décédé avant consommation et sans désignation (deux dires : pas de dot, mais l'héritage par le contrat — ʿAlī et la "
               "majorité des Compagnons ; ou la dot — ash-Shāfiʿī, favorisé par Ibn al-ʿArabī d'après Barwaʿ bint Wāshiq : « la dot des femmes de "
               "son semblable et l'héritage » — un dire shādh chez nous ; Mālik : « on n'agit point sur cela ») ; l'obligation de la dot par le "
               "relâchement des rideaux (irkhāʾ as-sutūr — la prise de solitude (at-takhlīya) : la solitude de l'orientation (khilwa al-ihtidāʾ), "
               "chacun des deux époux s'apaise et se calme en l'autre, contre la solitude de la visite (khilwa az-ziyāra) — l'épouse confirmée par "
               "serment : ʿUmar (n° 1653), Zayd ibn Thābit (n° 1654) ; en la solitude de visite, le visiteur confirmé selon la maison — chez lui il "
               "est confirmé, chez elle de même, « le prédominant est qu'il n'y a point d'activité chez elle » — le cas d'al-Masīs (n° 1655)) ; le "
               "montant — pas de maximum (Ibn ʿAbd al-Barr : « nul calibrage ni spécification du maximum de la dot, par consensus »), le minimum "
               "diverge — Mālik le borne au quart de dīnār (« je ne considère point qu'une femme soit mariée pour moins d'un quart de dīnār » ; "
               "estimé à notre époque 1,0625 grammes d'or, le dīnār pesant 4,25 grammes), seul selon ʿIyāḍ, en égards aux versets 24 et 25 de la "
               "sourate des Femmes — « de l'argent qui a valeur » ; les savants du Ḥijāz, d'Égypte et de Syrie : le mariage selon ce que les deux "
               "époux agréent, fût sa valeur moindre qu'un dirham d'argent (2,975 grammes, ou 3,12 selon une autre estimation) — « cherche même un "
               "anneau de fer » et ses deux interprétations fragilisées (al-Zawāwī : « ce qui semble être que ce qui est demandé, c'est la totalité "
               "de la dot ») ; la polémique — al-Abī juge le dire d'Ibn Wahb plus probable contre le hadith de Muslim (« qui s'approprie la richesse "
               "d'un musulman par serment... » fût-ce « un bâton d'arāk ») — la réponse : l'appel est pour le zergeur ; ʿIyāḍ : le consensus — ce "
               "qui n'est ni monnaie ni a valeur n'est point dot — rompu par Ibn Ḥazm (« tout ce qui s'appelle quelque chose, fût-ce un grain "
               "d'orge ») ; la preuve d'Ibn ʿAbd al-Barr : Dieu mentionna la dot sans borner ni l'un ni l'autre — « la borne ne vaut que par un "
               "Livre ou une Sunna établie sans opposition, ou un consensus ». Deuxième — les décisions du ḥibāʾ : le don sans compensation (le "
               "ḥubāʾ de la femme est son mahr ; en terme : ce que le tuteur de l'épouse stipule pour lui-même sur le mari) — avant l'inviolabilité "
               "('iṣma) du mariage : à la femme si elle le demande, et elle peut le laisser à son père ou à son frère (la lettre de ʿUmar ibn "
               "ʿAbd al-ʿAzīz ; le hadith d'Abū Dāwūd : « tout ce qui vient après l'inviolabilité du mariage appartient à celui à qui il a été "
               "donné, et le plus digne de ce dont un homme a été honoré est sa fille ou sa sœur ») ; après l'iṣma : à son tuteur, nul droit pour "
               "l'épouse — sauf si la stipulation était condition de la validité du mariage (Mālik) ; donné après : « une karama dont il l'a "
               "honoré » (Ibn al-Qāsim) ; au divorce avant consommation : partagé en deux moitiés — il est de la dot, laquelle se partage. "
               "L'exploitation imprime le n° 1650 — le père qui remet la moitié de la dot de la vierge répudiée avant consommation : permis au "
               "mari « en ce dont il dispensa » ; les trois imams : celui en la main duquel est le nœud du mariage est le mari — sa remise complète "
               "la dot ; l'abrogation par le tuteur de ce qui est à sa pupille « contre les principes » (al-Zarqānī, 193/3). La préparation annonce "
               "le muḥallil et l-ʿasīla — les termes de la leçon suivante."),
    "explication": [
        ("La leçon (la dixième du livre ; le manuel l'étiquette « (leçon 3) ») traite les décisions de la dot (aṣ-ṣadāq) et du ḥibāʾ — le don. Le "
         "préambule pose : la dot et le ḥibāʾ adviennent tous deux à l'occasion du mariage ; ils ont un ensemble de décisions dont ils s'accordent "
         "sur les unes et divergent sur les autres, comme ils s'accordent sur certains objectifs. Trois objectifs : connaître les décisions de la "
         "dot et du ḥibāʾ ; les distinguer en certaines décisions ; comprendre l'application des décisions de la dot à des cas de jurisprudence. "
         "Note de lecture : la couche française de cette leçon rend le ḥibāʾ par « l'amour », « l'ami » ou « l'amant », et imprime « Préparation "
         "tribale » pour la rubrique de la préparation préalable — lire toutes ces occurrences sur le fil de l'arabe : le ḥibāʾ est le don sans "
         "compensation, et la préparation préalable annonce la leçon suivante, celle du muḥallil."),
        ("Le premier hadith (n° 1646 — Nāfiʿ) arme la première décision : la dot de celle dont le mari est décédé avant la consommation et la "
         "désignation. La fille dʿUbayd Allāh ibn ʿUmar — sa mère étant la fille de Zayd ibn al-Khaṭṭāb — était mariée à un fils dʿAbd Allāh ibn "
         "ʿUmar ; il mourut sans consommer et sans désigner de dot ; sa mère voulut sa dot ; ʿAbd Allāh dit qu'elle n'a point de dot — « si elle en "
         "avait eu une, nous ne l'aurions point retenue et ne lui aurions point fait de tort » ; la mère refusa d'accepter cela ; ils prirent pour "
         "arbitre Zayd ibn Thābit, et il « a statué : point de dot pour elle, et à elle l'héritage ». La question pose : si un homme contracte avec "
         "une femme en ne lui désignant point de dot (tafwīḍ), puis meurt avant la consommation et la désignation — doit-elle recevoir la dot ou "
         "non ? Deux dires. Le premier : pas de dot pour elle, mais l'héritage par le contrat — c'est le dire dʿAlī et de la majorité des "
         "Compagnons, démontré par le n° 1646."),
        ("Le second avis : la dot est due — al-Zarqānī rapporte qu'un groupe dit la dot obligée par la mort, et ash-Shāfiʿī le dit ; « c'est un "
         "dire shādh (isolé) chez nous », mais Ibn al-ʿArabī et d'autres l'ont favorisé, d'après le hadith rapporté dans Abū Dāwūd et at-Tirmidhī "
         "— qui l'a dit ḥasan ṣaḥīḥ — sous l'autorité de Maʿqil ibn Yasār : Barwaʿ bint Wāshiq s'était mariée sans dot, et son mari mourut avant de "
         "la lui désigner ; le Prophète — paix et bénédiction sur lui — décida pour elle la dot des femmes de son semblable et l'héritage. Mais "
         "Mālik : « on n'agit point sur cela » — la retenue de l'école devant un texte reçu hors des voies du Muwaṭṭaʾ."),
        ("L'obligation de la dot par le relâchement des rideaux (irkhāʾ as-sutūr) arme la seconde question. Le relâchement des rideaux est la "
         "prise de solitude (at-takhlīya) entre l'homme et la femme, même sans rideau à relâcher ni porte à fermer — ce que les jurisconsultes "
         "nomment la solitude de l'orientation (khilwa al-ihtidāʾ), parce que chacun des deux époux s'apaise et se calme en l'autre ; cela "
         "contraste avec la solitude de la visite (khilwa az-ziyāra). Si le relâchement des rideaux s'établit et que l'épouse revendique le coït "
         "et que l'homme nie, elle est confirmée par serment, et sa confirmation entraîne l'obligation de la dot — ʿUmar ibn al-Khaṭṭāb « a statué "
         "dans l'affaire de la femme que l'homme épouse : si les rideaux sont relâchés, la dot est obligée » (n° 1653), et Zayd ibn Thābit de même "
         "(n° 1654). En la solitude de la visite, la règle se répartit selon la maison : si c'est elle qui l'a visité et entré chez lui, il est "
         "confirmé — « l'essentiel de son activité se déroule à la maison » ; s'il est entré chez elle et qu'elle revendique le coït et qu'il nie, "
         "il est confirmé — « le prédominant est qu'il n'y a point d'activité chez elle » ; le visiteur, de l'un des deux, est confirmé par "
         "serment, contrairement à la solitude de l'orientation où la femme est confirmée par son serment — parce que la solitude de la visite "
         "n'excite point les âmes. Mālik l'applique au cas d'al-Masīs : entré chez elle et qu'elle dise « il m'a touché », lui « je ne l'ai point "
         "touchée » — elle est confirmée contre lui (n° 1655)."),
        ("Le montant règle la troisième question. Pas de maximum — la parole du Très Haut (la sourate des Femmes, verset 20) — et Ibn ʿAbd al-Barr : "
         "« nul calibrage ni spécification du maximum de la dot, par consensus ». Le minimum diverge : l'imam le borne au quart de dīnār — « je ne "
         "considère point qu'une femme soit mariée pour moins d'un quart de dīnār » — estimé à notre époque à 1,0625 grammes d'or, le dīnār pesant "
         "4,25 grammes ; ʿIyāḍ dit que Mālik est seul en cela, en égards aux versets 24 et 25 de la sourate des Femmes — « de l'argent qui a "
         "valeur ». Les savants du Ḥijāz, d'Égypte, de Syrie et d'autres s'accordent sur le mariage selon ce que les deux époux agréent, fût sa "
         "valeur moindre qu'un dirham d'argent — le dirham pesant 2,975 grammes, ou 3,12 grammes selon une autre estimation. Ceux qui le permettent "
         "sur toute richesse à bénéfice invoquent « cherche même un anneau de fer » ; ʿIyāḍ rapporte deux interprétations — une hyperbole pour "
         "déconseiller la réduction, ou la demande de ce qu'il offre avant la consommation, non de la totalité de la dot — et al-Zawāwī fragilise "
         "la seconde : le hadith ne montre point la demande d'une avance, mais « ce qui semble être que ce qui est demandé, c'est la totalité de "
         "la dot, non une partie »."),
        ("La polémique se noue sur le terrain du hadith. al-Abī juge le dire d'Ibn Wahb plus probable et l'oppose à ce dont Mālik a fait argument — "
         "le hadith de Muslim : « qui s'approprie la richesse d'un musulman par serment — Dieu lui interdit le Paradis et l'admet en Enfer », "
         "fût-ce « un bâton d'arāk » — l'appel « argent » est donc absolu ; on lui répond que cet appel est permis au dessein de déconseiller "
         "l'appropriation de la richesse du musulman et le serment faux. ʿIyāḍ : le consensus — ce qui n'est ni monnaie ni a valeur n'est point "
         "dot ; le Ḥāfiẓ : si ce consensus s'établit, Ibn Ḥazm l'a rompu — « tout ce qui s'appelle quelque chose, fût-ce un grain d'orge ». Ibn "
         "ʿAbd al-Barr donne la preuve des permissifs : Dieu mentionna la dot sans borner son maximum ni son minimum — s'il y avait eu une borne, "
         "le Prophète — paix et bénédiction sur lui — l'eût précisée, « parce que la borne ne vaut que par un Livre ou une Sunna établie sans "
         "opposition, ou un consensus »."),
        ("Le ḥibāʾ ouvre la seconde partie. En langue : le don sans compensation — il a donné à son semblable sans compensation ; le ḥubāʾ de la "
         "femme est son mahr ; al-ḥibāʾ est un nom de pluriel (aḥbiyya). En terme : ce que le tuteur de l'épouse stipule pour lui-même sur le "
         "mari — un don, ou tout ce dont le tuteur est honoré (karama). Ses décisions se répartissent en trois. Avant l'inviolabilité ('iṣma) du "
         "mariage : le ḥibāʾ est à la femme si elle le demande, et elle peut le laisser à son père ou à son frère — la lettre de ʿUmar ibn "
         "ʿAbd al-ʿAzīz en son califat à l'un de ses ouvriers (n° 1647) : tout ce que stipule celui qui marie, père ou autre, « de ḥibāʾ ou de "
         "karama », c'est à la femme si elle le demande ; et le hadith d'Abū Dāwūd — via Ibn Jurayj, ʿAmr ibn Shuʿayb, de son père et de son "
         "grand-père : « tout ce qui vient après l'inviolabilité du mariage appartient à celui à qui il a été donné, et le plus digne de ce dont "
         "un homme a été honoré est sa fille ou sa sœur ». Après l'inviolabilité : le ḥibāʾ est à son tuteur, nul droit pour l'épouse — Mālik : le "
         "père qui marie et stipule dans son ḥibāʾ ce par quoi le mariage vaut : c'est à sa fille si elle le demande, non si elle le laisse à son "
         "père ; l'ajout d'Ibn al-Qāsim : « s'il le donne après l'avoir mariée, ce n'est qu'une karama dont il l'a honoré — nulle part pour sa "
         "fille dans cela ». Au divorce avant la consommation : le ḥibāʾ se partage — moitié au mari, moitié à la femme — parce qu'il est de la "
         "dot, laquelle se partage au divorce avant consommation."),
        ("L'exploitation imprime le n° 1650 — Mālik sur l'homme qui répudia sa femme avant consommation, elle étant vierge, et son père remit la "
         "moitié de la dot : cela est permis au mari de la part du père « en ce dont il dispensa » — « alors elles sont les femmes avec lesquelles "
         "on a coïté » (la parole du Très Haut, la sourate al-Baqara, verset 235) — « fa-huwa l-abū fī ibnatihi l-bikr » (le n° 1650). Les trois "
         "imams : celui en la main duquel est le nœud du mariage est le mari, et sa remise complète la dot ; un groupe et les imams ont porté "
         "chacun des deux dires ; les imams argumentent par le rapporté du Prophète — paix et bénédiction sur lui — et par ce que l'abrogation par "
         "le tuteur de ce qui est à sa pupille est contre les principes (al-Zarqānī, Sharḥ al-Muwaṭṭaʾ, 193/3). Les questions : détailler qui peut "
         "remettre la moitié de la dot ; qui est « celui en la main duquel est le nœud du mariage », avec raison et preuve. La préparation annonce "
         "la leçon du muḥallil et de l-ʿasīla : ce que l'on entend par les deux termes, et quand il est permis à une femme d'épouser son premier "
         "mari dans le divorce dissolvant (al-ṭalāq al-bāṭ)."),
    ],
    "points": [
        ("Fil de révision : trois objectifs (les décisions de la dot et du ḥibāʾ ; leur distinction ; l'application aux cas) → préambule (tous "
         "deux à l'occasion du mariage — accord et divergence) ; note de lecture : la couche française rend le ḥibāʾ par « l'amour », « l'ami », "
         "« l'amant » — lire sur le fil arabe, le don sans compensation."),
        ("Le n° 1646 : la fille dʿUbayd Allāh ibn ʿUmar (sa mère, la fille de Zayd ibn al-Khaṭṭāb) — mariée à un fils dʿAbd Allāh ibn ʿUmar, mort "
         "sans consommation ni désignation — ʿAbd Allāh : « si elle en avait eu une, nous ne l'aurions point retenue et ne lui aurions point fait "
         "de tort » — l'arbitre Zayd ibn Thābit : « point de dot pour elle, et à elle l'héritage » — le premier avis (ʿAlī et la majorité des "
         "Compagnons)."),
        ("Le second avis : la dot obligée par la mort (ash-Shāfiʿī) — favorisé par Ibn al-ʿArabī sur Barwaʿ bint Wāshiq (Abū Dāwūd, at-Tirmidhī — "
         "ḥasan ṣaḥīḥ — la dot des femmes de son semblable et l'héritage) — « un dire shādh chez nous » ; Mālik : « on n'agit point sur cela »."),
        ("Le relâchement des rideaux (irkhāʾ as-sutūr) : la prise de solitude (at-takhlīya) — la solitude de l'orientation (khilwa al-ihtidāʾ) "
         "contre la solitude de la visite (khilwa az-ziyāra) ; ʿUmar : « si les rideaux sont relâchés, la dot est obligée » (n° 1653) ; Zayd ibn "
         "Thābit de même (n° 1654)."),
        ("La preuve du coït : en l'orientation, la femme confirmée par son serment ; en la visite, le visiteur confirmé selon la maison — chez "
         "lui : il est confirmé (l'essentiel de son activité) ; chez elle : de même (le prédominant — point d'activité chez elle) — le cas "
         "d'al-Masīs (n° 1655)."),
        ("Le montant : pas de maximum (le consensus, Ibn ʿAbd al-Barr) ; le minimum — Mālik : le quart de dīnār (1,0625 g d'or, le dīnār à 4,25 g), "
         "seul selon ʿIyāḍ (versets 4:24-25 — « de l'argent qui a valeur ») ; les savants du Ḥijāz, d'Égypte, de Syrie : ce que les deux époux "
         "agréent, fût-ce moins qu'un dirham (2,975 g, ou 3,12 g d'argent) — « cherche même un anneau de fer » et ses deux interprétations "
         "fragilisées (al-Zawāwī)."),
        ("La polémique du minimum : al-Abī (le dire d'Ibn Wahb) contre le hadith de Muslim (« fût-ce un bâton d'arāk ») — la réponse : l'appel est "
         "pour le zergeur ; ʿIyāḍ : le consensus — point de dot sans monnaie ni valeur — rompu par Ibn Ḥazm (« un grain d'orge ») ; la preuve "
         "d'Ibn ʿAbd al-Barr : Dieu n'a borné ni maximum ni minimum."),
        ("Le ḥibāʾ : le don sans compensation — le ḥubāʾ de la femme est son mahr ; en terme ce que le tuteur stipule pour lui-même sur le mari — "
         "un don ou tout ce dont le tuteur est honoré (karama) ; le ḥibāʾ est un nom de pluriel (aḥbiyya)."),
        ("Les trois statuts du ḥibāʾ : avant l'iṣma → à la femme si elle le demande (n° 1647 — la lettre de ʿUmar ibn ʿAbd al-ʿAzīz ; le hadith "
         "d'Abū Dāwūd — « le plus digne... sa fille ou sa sœur ») ; après l'iṣma → au tuteur (sauf condition de la validité — Mālik ; après : "
         "« une karama dont il l'a honoré » — Ibn al-Qāsim) ; divorce avant consommation → partagé en deux moitiés (il est de la dot)."),
        ("L'exploitation (n° 1650) : le père remet la moitié de la dot de la vierge répudiée avant consommation — permis « en ce dont il "
         "dispensa » ; les trois imams — le nœud du mariage en la main du mari ; l'abrogation par le tuteur « contre les principes » (al-Zarqānī, "
         "193/3) ; la préparation annonce le muḥallil et l-ʿasīla."),
    ],
    "vocabulaire": [
        {"ar": "الصداق", "translit": "aṣ-ṣadāq",
         "fr": "la dot — ce que le mari doit à son épouse ; pas de maximum par consensus, et le minimum diverge : le quart de dīnār chez Mālik, toute richesse à valeur chez les autres savants"},
        {"ar": "الحباء", "translit": "al-ḥibāʾ",
         "fr": "le don sans compensation — le ḥubāʾ de la femme est son mahr ; en terme : ce que le tuteur de l'épouse stipule pour lui-même sur le mari, un don ou tout ce dont le tuteur est honoré (karama) — la couche française de la leçon le rend par « l'amour » ou « l'ami »"},
        {"ar": "أرخيت السطور", "translit": "irkhiyat as-sutūr",
         "fr": "« les rideaux furent relâchés » — le relâchement (irkhāʾ as-sutūr) : la sentence dʿUmar — « si les rideaux sont relâchés, la dot est obligée » (n° 1653)"},
        {"ar": "التخلية", "translit": "at-takhlīya",
         "fr": "la prise de solitude entre les deux époux — même sans rideau à relâcher ni porte à fermer ; elle se répartit en solitude de l'orientation et solitude de la visite"},
        {"ar": "خلوة الاهتداء", "translit": "khilwa al-ihtidāʾ",
         "fr": "la solitude de l'orientation — chacun des deux époux s'apaise et se calme en l'autre ; la femme y est confirmée par son serment quand elle revendique le coït"},
        {"ar": "خلوة الزيارة", "translit": "khilwa az-ziyāra",
         "fr": "la solitude de la visite — elle n'excite point les âmes ; le visiteur de l'un des deux y est confirmé selon la maison où s'est tenue la rencontre (n° 1655 — le cas d'al-Masīs)"},
        {"ar": "الكرامة", "translit": "al-karāma",
         "fr": "ce dont on honore — synonyme du ḥibāʾ en la leçon : « de ḥibāʾ ou de karama » ; le don fait après le mariage est « une karama dont il l'a honoré » (Ibn al-Qāsim)"},
        {"ar": "العصمة", "translit": "al-iʿṣma",
         "fr": "l'inviolabilité du mariage — le ḥibāʾ antérieur à l'iṣma est à la femme si elle le demande ; ce qui vient après l'iṣma appartient à qui il a été donné"},
    ],
    "avertissement": "Ce commentaire est un guide de lecture du manuel ; en cas de divergence d'expression, le manuel et sa traduction savante font foi.",
}

def norme_fr(s):
    s = s.replace('\'', '’')
    s = re.sub(r'\s+([;:!?»])', '\u202f\\1', s)
    s = s.replace('« ', '«\u202f')
    return s

def norme_entree(e):
    e['resume'] = norme_fr(e['resume'])
    e['avertissement'] = norme_fr(e['avertissement'])
    e['explication'] = [norme_fr(x) for x in e['explication']]
    e['points'] = [norme_fr(x) for x in e['points']]
    for v in e.get('vocabulaire', []):
        v['fr'] = norme_fr(v['fr'])
    return e

data = json.load(open(CHEMIN, encoding='utf-8'))
com = data['commentaires']
DOCIDS = ('12981', '12990')
deja = [d for d in DOCIDS if d in com]
if deja:
    print(f'!! déjà présent : {deja} — rien de fait')
    raise SystemExit(1)
com['12981'] = norme_entree(E_12981)
com['12990'] = norme_entree(E_12990)

with open(CHEMIN, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
    f.write('\n')

# Validation : relecture + volume + ponctuation FR + arabes hors champ ar + guillemets appariés
data2 = json.load(open(CHEMIN, encoding='utf-8'))
print('entrées au total :', len(data2['commentaires']))
motif_ar = re.compile(r'[\u0600-\u06FF\u0750-\u077F\u08A0-\u08FF\uFDFA]')
mauvais = 0
for DOCID in DOCIDS:
    e = data2['commentaires'][DOCID]
    mots = sum(len(x.split()) for x in [e['resume']] + e['explication'] + e['points'])
    print(f'{DOCID} : {mots} mots (resume+explication+points), vocab {len(e["vocabulaire"])}')
    textes = [e['resume'], e['avertissement']] + e['explication'] + e['points'] + [v['fr'] for v in e['vocabulaire']] + [v['translit'] for v in e['vocabulaire']]
    for t in textes:
        hors_parenth = re.sub(r'\([^)]*[\u0600-\u06FF][^)]*\)', '()', t).replace('ﷺ', '')
        if "'" in t or re.search(r' [;:!?»]', t) or re.search(r'« ', t):
            mauvais += 1
            print('   ponctuation à revoir dans :', t[:60])
        if motif_ar.search(hors_parenth):
            mauvais += 1
            print('   caractère arabe hors parenthèses :', t[:60])
        if t.count('«') != t.count('»'):
            mauvais += 1
            print('   guillemets non appariés :', t[:60])
    for v in e['vocabulaire']:
        if not motif_ar.search(v['ar'].replace(' ', '')):
            mauvais += 1
            print('   vocab ar non arabe :', v['ar'])
        if re.search(r'[\u064B-\u0652\u0670]', v['ar']):
            mauvais += 1
            print('   vocab ar avec harakat :', v['ar'])
print('contrôle ponctuation/arabe FR :', 'PASS' if mauvais == 0 else f'ÉCHEC ({mauvais})')

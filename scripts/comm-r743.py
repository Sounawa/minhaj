#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""R743 — commentaires des leçons 5-6 hadith-5ep : pdf-5 (les piliers de l'islām —
le troisième hadith des Quarante, « L'islām est bâti sur cinq », rapporté par
ʿAbdullāh ibn ʿUmar) et pdf-6 (les phases de la création de l'homme — le
quatrième hadith des Quarante, rapporté par ʿAbdullāh ibn Masʿūd : les trois
phases, le souffle vital, les quatre paroles inscrites, le Livre le devance).
Troisième vague du livre (SUIVANT de R742, leçons 5-6 précisées ; livre RESPECTÉ :
hadith-tanawi-1 au livreur concurrent, non touché ; IA-2 livre les transcriptions).
Rédaction d'après la lecture complète FR des deux leçons (extraction non lossy
scripts/extrait-r743.py). Aucune invention (règle 2) : hadiths, versets, citations
et attributions tels que la leçon les donne — sans numéros de pages (l'htmlFr de
ce manuel n'en porte pas).
NB consignés hors commentaire (journal worklog, zones IA-2/IA-3) : ① pdf-5 — la
rubrique glossaire n'est rendue que par son titre, sans entrées ; ② pdf-5 — la
balise d'unanimité imprime « muttaqun ʿalayhi » (forme correcte : muttafaqun
ʿalayhi) ; ③ pdf-5 — l'ordre des piliers du hadīth imprimé place le pèlerinage
avant le jeûne, l'analyse suit l'ordre du hadīth de Jibrīl ; ④ pdf-6 — la rubrique
daʿm wa-taṭbīq annoncée par l'iʿdād n'est pas rendue, et les quatre paroles
inscrites et les deux scènes du « Livre le devance » ne sont pas développées par
l'analyse (le commentaire les reprend du texte même du hadīth) ; ⑤ pdf-6 — la
glose d'al-ʿalaqa imprime « de l'accrochement (ḫalāq) » (racique attendu :
ʿalāq — ʿaliqa/yaʿliqu).
Garde-fous de comm-r742.py repris (typographie FR, arabe entre parenthèses
seulement, vocab ar sans harakat, guillemets appariés — imbriqués courbes)."""
import json, re, os

CHEMIN = 'content/commentaires/hadith-5ep.json'

E_5 = {
    "auteur": "IA-1, tour R743",
    "resume": ("Guide de lecture de la leçon 5 (les piliers de l'islām — 'arkān al-'islām "
               "(أركان الإسلام)) : le troisième hadith des Quarante, rapporté par ʿAbdullāh "
               "ibn ʿUmar — « L'islām est bâti sur cinq » —, fait l'unanimité. La leçon répond "
               "à la préparation de la leçon 4 : méditer « les piliers de l'islām et "
               "l'importance de chacun d'eux ». Le tamhīd donne le cadre : Allah a légiféré "
               "l'islām comme religion pour les serviteurs et n'agrée d'elle, comme religion, "
               "aucune autre ; Son Messager — paix et bénédiction sur lui — a expliqué que "
               "l'islām comporte des piliers « énoncés explicitement », sur lesquels il est "
               "bâti — « les plus importantes obligations de la religion et ses imposants "
               "devoirs ». Le hadīth énumère : le témoignage qu'il n'est de dieu qu'Allah et "
               "que Muḥammad est le Messager d'Allah, l'accomplissement de la prière, "
               "l'acquittement de l'aumône, le pèlerinage de la Maison, et le jeûne du "
               "ramadan. L'analyse développe pilier par pilier, chacun avec sa définition et "
               "son importance : les deux témoignages — « la clef de l'entrée dans l'islām », "
               "« nul acte n'est accepté sans eux » (l'envoi de Muʿāḏ au Yémen) ; la prière — "
               "l'attention pleine et complète, « le plus grand des piliers de l'islām après "
               "les deux témoignages », « le principe premier est l'islām, et son pilier [est] "
               "la prière » ; l'aumône — l'adoration pécuniaire dosée par la Loi ; le jeûne — "
               "s'abstenir des appétits, avec l'intention (al-Baqara 183) ; le pèlerinage — "
               "pour quiconque en a le chemin (Āl ʿImrān 97), l'expiation de ʿArafa. "
               "L'exploitation imprime la lettre d'ʿUmar ibn ʿAbd al-ʿAzīz à ʿAdī ibn ʿAdī, et "
               "la préparation ouvre les phases de la création (leçon 6)."),
    "explication": [
        ("La leçon pose trois objectifs : identifier les piliers de l'islām ; distinguer les "
         "piliers « et la prééminence de certains d'entre eux sur d'autres » ; incarner les "
         "piliers « dans mes principes, mes adorations et ma conduite ». Le tamhīd donne le "
         "cadre : Allah — le Puissant et le Majestueux — « a légiféré l'islām comme religion "
         "pour les serviteurs, et Il n'agrée d'elle, comme religion, aucune autre » ; Son "
         "Messager — paix et bénédiction sur lui — « a expliqué que l'islām comporte des "
         "piliers énoncés explicitement, sur lesquels il est bâti ; ils sont les plus "
         "importantes obligations de la religion et ses imposants devoirs ». Deux questions "
         "d'ouverture — quels sont les piliers de l'islām ? quelle est l'importance de chacun "
         "d'eux ? — et l'extraction des contenus en un item : quels sont les piliers de "
         "l'islām ? La préparation de la leçon 4 déjà mémorisait ce hadīth et demandait de "
         "méditer « les piliers de l'islām et l'importance de chacun d'eux » — la présente "
         "leçon y répond. La rubrique glossaire de la couche française n'est rendue que par "
         "son titre — « Le vocabulaire du hadīth et ses balises de sens » — sans aucune "
         "entrée : les définitions des piliers viennent de l'analyse (consigné au journal)."),
        ("Le hadīth d'abord, avec sa balise de ṣaḥīḥa : « Fait l'unanimité » — la double "
         "transmission dans les deux Ṣaḥīḥ, d'al-Buḫārī et de Muslim ; c'est l'exemple même "
         "de la ṣiḥḥa donnée en leçon 1 comme troisième raison de la makāna du livre (la "
         "plupart des Quarante dans les deux Ṣaḥīḥ) — et le troisième hadith rejoint ainsi "
         "le premier (les intentions, leçon 2) sous la même balise, là où le deuxième (le "
         "hadīth de Jibrīl, leçon 3) fut imprimé chez Muslim seul. Le hadīth ouvre sur "
         "l'image de l'édifice : « L'islām est bâti sur cinq » — les piliers sont « ses "
         "soutiens sur lesquels il est bâti », dit l'analyse. Le transmetteur : ʿAbdullāh ibn "
         "ʿUmar ibn al-Khaṭṭāb, Abū ʿAbd ar-Raḥmān, al-Fārūqī, al-ʿAdawī, Mecquois puis "
         "Médinois — « l'imam, le modèle (qudwa), le doyen de l'islām » ; il embrassa "
         "l'islām alors qu'il était jeune, fut du nombre de ceux qui prêtèrent serment sous "
         "l'arbre, rapporta « un savoir abondant et utile » du Prophète — paix et bénédiction "
         "sur lui —, de son père, d'Abū Bakr, de ʿUṯmān, de ʿAlī et d'autres ; il mourut en "
         "l'an 73 de l'Hégire. La notice relie ainsi la chaîne des trois premiers hadiths du "
         "recueil : le père (ʿUmar, leçon 2) a rapporté les intentions, le fils rapporte le "
         "« bâti sur cinq ». Une observation d'ordre : le hadīth du manuel énumère « le "
         "pèlerinage de la Maison, et le jeûne du ramadan » — le pèlerinage avant le jeûne — "
         "là où le hadīth de Jibrīl (leçon 3) plaçait le jeûne avant le pèlerinage ; "
         "l'analyse de la présente leçon reprend l'ordre du hadīth de Jibrīl (le jeûne en "
         "quatrième, le pèlerinage en cinquième) — l'ordre des piliers varie d'une version à "
         "l'autre du hadīth ; la leçon l'expose sans y insister (consigné au journal), le "
         "commentaire suit l'analyse."),
        ("Les deux témoignages : « que le serviteur témoigne qu'il n'est de dieu qu'Allah et "
         "que Muḥammad est le Messager d'Allah ; le proclamant par sa langue, le croyant par "
         "son cœur qu'il n'est d'adoré en toute vérité qu'Allah » — langue et cœur, les deux "
         "faces de l'attestation ; puis « confirmant la prophétie de notre seigneur Muḥammad "
         "— paix et bénédiction sur lui — et sa mission, et suivant ce par quoi il est venu "
         "de direction droite et de lumière ». L'importance : « qu'ils sont la clef de "
         "l'entrée dans l'islām, et que tout ce qui les suit, du reste des piliers, en "
         "dépend ; l'entrée dans l'islām ne s'opère point sans eux, et nul acte n'est "
         "accepté sans eux » — la preuve est le hadīth de l'envoi de Muʿāḏ au Yémen : « "
         "Appelle-les au témoignage qu'il n'est de dieu qu'Allah et que je suis le Messager "
         "d'Allah ; s'ils t'obéissent en cela, informe-les qu'Allah leur a prescrit cinq "
         "prières » (Ṣaḥīḥ de al-Buḫārī) — l'ordre pédagogique de l'appel calque la "
         "hiérarchie des piliers. La prière : « l'attention qu'on lui porte, pleine et "
         "complète, embrassant tous ses piliers et ses bonnes conditions, comme le takbīr, "
         "le taslīm, l'inclination, la prosternation, l'équilibre et la quiétude, son "
         "accomplissement en son temps et en communautaire, et ses significations "
         "intérieures, comme la sincérité, la présence du cœur en elle et l'humilité » — "
         "l'iqāma n'est pas la seule validité de l'acte, mais l'acte accompli au-dehors et "
         "au-dedans. Son importance en deux : elle est « le plus grand des piliers de "
         "l'islām après les deux témoignages » — « le principe premier est l'islām, et son "
         "pilier [est] la prière » (Sunan d'at-Tirmiḏī) —, et elle est « le moyen "
         "d'attacher le serviteur à son Seigneur, de sorte qu'il n'oublie pas Son obéissance "
         "dans ce qu'Il ordonne et ce qu'Il interdit, et en toutes ses situations »."),
        ("L'aumône : « une adoration pécuniaire, dosée par la Loi ; son acquittement consiste "
         "à la donner à ceux qui y ont droit, parmi les catégories qu'Allah — le Puissant et "
         "le Majestueux — a mentionnées, au premier rang desquels les pauvres et les "
         "démunis » — l'adoration du bien, à l'image de la prière, adoration du corps. Son "
         "importance en trois : « qu'elle réalise la couverture des besoins d'existence pour "
         "les catégories éprouvées de la société » ; « qu'elle veille à l'affection, au "
         "ralliement et à la solidarité entre les membres de la société et ses catégories » "
         "; « qu'elle figure parmi les causes de la droiture, de la dignité et de la "
         "générosité » — de l'utilité sociale à la vertu morale. Le jeûne : « s'abstenir des "
         "appétits du ventre et du sexe et de tout ce qui rompt le jeûne, du lever de l'aube "
         "au coucher du soleil, avec l'intention » ; son caractère obligatoire « ressort de "
         "la parole du Très-Haut » : « Ô vous qui avez cru, le jeûne vous est prescrit, "
         "comme il fut prescrit à ceux qui vous ont précédés — peut-être craindriez-vous. "
         "Des jours comptés » (al-Baqara 183) ; l'importance : « l'exploitation de nombreux "
         "bienfaits psychiques et corporels, au premier rang desquels l'élévation de l'âme "
         "vers un degré élevé de piété, de résolution et de force de volonté » — la piété "
         "que le verset donne pour fruit du jeûne, nommée dans le fruit que la leçon en "
         "tire."),
        ("Le pèlerinage : « un pilier de l'islām pour quiconque en a le chemin » — la "
         "capacité, annoncée par le hadīth de Jibrīl (« si tu en as le chemin », leçon 3), "
         "reposée ici sur la parole d'Allah : « C'est un devoir, envers Allah, envers les "
         "gens, le pèlerinage de la Maison, pour quiconque en a le chemin » (Āl ʿImrān 97), "
         "et sur la formule même du hadīth de la leçon : « et le pèlerinage de la Maison ». "
         "L'importance en trois : « l'assistance à cette immense assemblée, que les "
         "musulmans ne peuvent connaître tout au long de leur vie qu'en accomplissant ce "
         "grand pilier » ; « l'obtention des bénédictions et la prise de connaissance des "
         "vertus, en le lieu de la descente de la Révélation, berceau de l'appel de "
         "l'islām » ; « l'expiation de toutes les fautes, le vendredi immense, sur le site "
         "de ʿArafa, de sorte que le pèlerin revienne de ses péchés comme le jour où sa "
         "mère l'enfanta ». L'évaluation retourne au fil en trois items : le sens de « "
         "L'islām est bâti sur cinq » ; le sens de chaque pilier ; l'importance de chaque "
         "pilier. L'exploitation imprime le dire d'al-Buḫārī : ʿUmar ibn ʿAbd al-ʿAzīz "
         "écrivit à ʿAdī ibn ʿAdī : « la foi comporte des obligations, des lois, des limites "
         "et des coutumes prophétiques ; quiconque les complète a complété la foi, et "
         "quiconque ne les complète pas n'a pas complété la foi ; si je vis, je vous les "
         "demanderai en compte, jusqu'à ce que vous œuvriez par elles ; et si je meurs, je "
         "ne suis point, pour votre fréquentation, une bouffée d'air » (Ṣaḥīḥ de al-Buḫārī) "
         "— le compte rendu de la foi, à l'image du « bâti sur cinq » du hadīth ; l'exercice "
         "demande d'en inférer l'exposé du contenu « de mes propres ressources ». La "
         "préparation ouvre la leçon 6 : le hadīth d'ʿAbdullāh ibn Masʿūd — « J'explique le "
         "sens des phases (ʾaṭwār), et je précise le sens de : “le Livre le devance” » et « "
         "Qu'est-ce qu'Allah inscrit sur l'homme après sa création, durant les phases ? » — "
         "posée dans la même vague."),
    ],
    "points": [
        ("Fil de révision : trois objectifs (identifier ; distinguer et prééminence ; "
         "incarner dans les principes, les adorations et la conduite) → tamhīd (une religion "
         "légiférée, aucune autre agréée ; des piliers énoncés explicitement) → le hadīth "
         "fait l'unanimité → cinq piliers, chacun avec définition et importance → évaluation "
         "en trois items → istithmār (la lettre d'ʿUmar ibn ʿAbd al-ʿAzīz) → iʿdād de la "
         "leçon 6."),
        ("La balise de ṣaḥīḥa : « fait l'unanimité » — la double transmission dans les deux "
         "Ṣaḥīḥ ; l'exemple même de la ṣiḥḥa donnée en leçon 1 comme raison de la makāna du "
         "livre ; le troisième hadith rejoint le premier (les intentions) sous la même "
         "balise, le deuxième (Jibrīl) fut imprimé chez Muslim seul."),
        ("L'image de l'édifice : « bâti sur cinq » — les piliers sont « ses soutiens » ; la "
         "prééminence annoncée par le second objectif se lit dans l'importance propre de "
         "chaque pilier : les témoignages clef et condition de tout acte, la prière « le "
         "plus grand des piliers » après eux."),
        ("Les deux témoignages : proclamés par la langue, crus par le cœur ; « la clef de "
         "l'entrée dans l'islām », « nul acte n'est accepté sans eux » ; la preuve par "
         "l'envoi de Muʿāḏ au Yémen — l'ordre de l'appel calque la hiérarchie des piliers."),
        ("L'iqāmat aṣ-ṣalāh : l'attention pleine et complète — piliers et conditions "
         "(takbīr, taslīm, inclination, prosternation, équilibre, quiétude), temps et "
         "communautaire, significations intérieures (sincérité, présence du cœur, "
         "humilité) ; « le principe premier est l'islām, et son pilier [est] la prière » "
         "(at-Tirmiḏī) ; le moyen de ne pas oublier Son obéissance en toutes situations."),
        ("L'ītāʾ az-zakāh : l'adoration pécuniaire dosée par la Loi, donnée aux catégories "
         "nommées par Allah — les pauvres et les démunis au premier rang ; couverture des "
         "besoins, affection et solidarité, causes de droiture, de dignité et de "
         "générosité."),
        ("Le ṣawm et le ḥaǧǧ : s'abstenir des appétits du ventre et du sexe, du lever de "
         "l'aube au coucher du soleil, avec l'intention (al-Baqara 183 — piété, résolution, "
         "force de volonté) ; le pèlerinage pour quiconque en a le chemin (Āl ʿImrān 97) — "
         "l'immense assemblée, le lieu de la descente de la Révélation, l'expiation de "
         "ʿArafa : « comme le jour où sa mère l'enfanta »."),
        ("L'ordre des piliers : le hadīth du manuel place le pèlerinage avant le jeûne, "
         "l'analyse suit l'ordre du hadīth de Jibrīl (jeûne en quatrième) — l'ordre varie "
         "d'une version à l'autre (consigné au journal) ; l'exploitation : la lettre d'ʿUmar "
         "ibn ʿAbd al-ʿAzīz — « la foi comporte des obligations, des lois, des limites et "
         "des coutumes prophétiques », « quiconque les complète a complété la foi » — et "
         "l'iʿdād annonce les phases d'Ibn Masʿūd et « le Livre le devance » (leçon 6, posée "
         "dans la même vague)."),
    ],
    "vocabulaire": [
        {"ar": "بني على خمس", "translit": "buniya ʿalā ḫams",
         "fr": "« est bâti sur cinq » — l'image de l'édifice qui ouvre le hadīth ; les piliers sont les soutiens sur lesquels l'islām se dresse"},
        {"ar": "المتفق عليه", "translit": "muttafaq ʿalayhi",
         "fr": "« fait l'unanimité » — la balise qui signale la double transmission du hadīth dans les deux Ṣaḥīḥ, d'al-Buḫārī et de Muslim"},
        {"ar": "الشهدتان", "translit": "aš-šahādatān",
         "fr": "les deux témoignages — « la clef de l'entrée dans l'islām » ; proclamés par la langue, crus par le cœur ; nul acte n'est accepté sans eux"},
        {"ar": "اقامة الصلاة", "translit": "ʾiqāmat aṣ-ṣalāh",
         "fr": "l'accomplissement de la prière — l'attention pleine et complète : piliers et conditions, temps et communautaire, sincérité, présence du cœur et humilité"},
        {"ar": "ايتاء الزكاة", "translit": "ʾītāʾ az-zakāh",
         "fr": "l'acquittement de l'aumône — l'adoration pécuniaire dosée par la Loi, donnée aux catégories qu'Allah a mentionnées, les pauvres et les démunis au premier rang"},
        {"ar": "صوم رمضان", "translit": "ṣawm ramaḍān",
         "fr": "le jeûne du ramadan — s'abstenir des appétits du ventre et du sexe, du lever de l'aube au coucher du soleil, avec l'intention"},
        {"ar": "حج بيت الله الحرام", "translit": "ḥaǧǧ bayt Allāh al-ḥarām",
         "fr": "le pèlerinage de la Maison sacrée d'Allah — pour quiconque en a le chemin ; l'immense assemblée et l'expiation de ʿArafa"},
        {"ar": "القدوة", "translit": "al-qudwa",
         "fr": "le modèle — le rang donné à ʿAbdullāh ibn ʿUmar dans sa notice : « l'imam, le modèle, le doyen de l'islām »"},
    ],
    "avertissement": "Ce commentaire est un guide de lecture du manuel ; en cas de divergence d'expression, le manuel et sa traduction savante font foi.",
}

E_6 = {
    "auteur": "IA-1, tour R743",
    "resume": ("Guide de lecture de la leçon 6 (أطوار خلق الإنسان — les phases de la création "
               "de l'homme) : le quatrième hadith des Quarante, rapporté par ʿAbdullāh ibn "
               "Masʿūd — « le véridique confirmé ». Le tamhīd invite à la contemplation de la "
               "création : elle est « rassemblée dans le ventre de sa mère, en trois "
               "ténèbres », puis l'homme « passe d'une phase à une autre jusqu'à sortir sous "
               "une création bien formée » — et le Très-Haut a appelé à cette contemplation "
               "par le verset de Nūḥ (« Allah vous a fait pousser de la terre comme une "
               "végétation »). Le hadīth déroule : « la création de l'un d'entre vous est "
               "rassemblée dans le ventre de sa mère pendant quarante jours, [comme] une "
               "goutte ; puis il est un caillot pendant autant ; puis il est une masse de "
               "chair pendant autant » ; puis « l'ange est envoyé vers lui » qui « souffle en "
               "lui le souffle vital », et il reçoit l'ordre de quatre paroles : « "
               "l'inscription de sa subsistance, son terme, son œuvre, [et s'il sera] "
               "malheureux ou heureux » ; puis les deux scènes de l'œuvre et du Livre — "
               "« jusqu'à ce qu'il n'y ait entre lui et elle qu'une coudée, alors le Livre le "
               "devance ». Le glossaire fixe six termes (le véridique, celui dont la véracité "
               "est confirmée, la goutte, le caillot, la masse de chair, le souffle vital). "
               "L'analyse lit le rassemblement — « l'unification du dispersé » — puis les "
               "phases : « il passe ainsi cent vingt jours en trois phases » ; al-Muʾminūn "
               "12-14 précise la suite du parcours — os, puis chair, puis « une autre "
               "création ». Les utilités en trois : la contemplation de sa création, "
               "l'argument de la Résurrection, la preuve de la prophétie. L'exploitation "
               "imprime al-Ḥaǧǧ 5, et la préparation demande la rubrique du soutien et de "
               "l'application."),
    "explication": [
        ("La leçon pose trois objectifs : identifier le sens du rassemblement de la création "
         "de l'homme ; saisir les phases de la création « dans le ventre de sa mère » ; "
         "affermir la foi en la grandeur d'Allah et en Sa puissance, « par la contemplation "
         "des phases de la création ». Le tamhīd enracine : parmi ce qui atteste la grandeur "
         "de Sa puissance, « notre contemplation de la création de l'homme : sa création est "
         "rassemblée dans le ventre de sa mère, en trois ténèbres, puis il passe d'une phase "
         "à une autre jusqu'à sortir sous une création bien formée » ; le Très-Haut a appelé "
         "à la contemplation de cela « en des versets », parmi lesquels : « Et Allah vous a "
         "fait pousser de la terre comme une végétation ; puis Il vous y fera retourner et "
         "Il vous en fera sortir d'une manière extraordinaire » (Nūḥ 17-18). Trois questions "
         "d'ouverture — le sens du rassemblement dans l'utérus, quand cela s'accomplit, "
         "quelles sont les phases — et l'extraction des contenus en deux items (quand la "
         "création est-elle rassemblée ; citer les phases). La préparation de la leçon 5 "
         "déjà mémorisait ce hadīth et demandait « le sens des phases » et le sens de « le "
         "Livre le devance » — la présente leçon y répond."),
        ("Le hadīth s'ouvre sur un double sceau : « le Messager d'Allah — paix et bénédiction "
         "sur lui —, le véridique confirmé (aṣ-ṣādiq al-maṣdūq), nous a narré » — le "
         "glossaire le décompose : le véridique est « celui qui informe d'une parole droite "
         "», celui dont la véracité est confirmée est « celui dont on confirme ce qu'il "
         "apporte de la Révélation » — l'attestation du narrateur prépare la réception de ce "
         "que le hadīth rapporte de l'invisible ; la balise porte Ṣaḥīḥ de al-Buḫārī et "
         "Muslim. Le transmetteur : ʿAbdullāh ibn Masʿūd — al-Huḏalī, Abū ʿAbd ar-Raḥmān ; "
         "il embrassa l'islām « aux premiers temps », émigra lors des deux émigrations, "
         "assista à Badr, « resta constamment auprès du Prophète — paix et bénédiction sur "
         "lui —, fut le porteur de ses sandales, et fut le premier à réciter le Coran à voix "
         "haute à La Mecque » ; le Prophète — paix et bénédiction sur lui — dit au sujet de "
         "sa récitation : « Quiconque se réjouit de réciter le Coran frais comme il fut "
         "descendu, qu'il récite selon la récitation d'Ibn Umm ʿAbd » (Musnad d'Ibn Abī "
         "Šayba) — Ibn Umm ʿAbd est la kunya d'Ibn Masʿūd lui-même, d'après sa mère : le "
         "Prophète fait son éloge ; il mourut en l'an 32 ou 33 de l'Hégire."),
        ("Le rassemblement d'abord : « le rassemblement est l'unification du dispersé : la "
         "réunion des éléments et des parties les unes aux autres » — « que l'eau se trouve "
         "dans l'utérus, dispersée, et qu'Allah — le Très-Haut — la rassemble, en le lieu de "
         "la naissance, depuis l'utérus, en ses phases : une phase de goutte, une phase de "
         "caillot, une phase de masse de chair ; puis il prend son chemin dans le reste des "
         "phases, jusqu'à la naissance ». Le glossaire arme le lexique du hadīth : la goutte "
         "(an-nuṭfa) — « le sperme ; son origine est l'eau peu abondante et limpide » ; le "
         "caillot (al-ʿalaqa) — « de l'accrochement ; car l'embryon, après le stade de la "
         "goutte, s'accroche à la paroi de l'utérus » ; la masse de chair (al-muḍġa) — « un "
         "morceau de chair doté de la capacité de ce que mâche le mangeur » — l'image de la "
         "mastication ; le souffle vital (ar-rūḥ) — « par quoi l'homme vit ; il relève de "
         "l'ordre d'Allah — le Puissant et le Majestueux »."),
        ("Les phases ensuite. « Allah a créé le premier homme d'une extraction d'argile ; "
         "puis ses individus se formèrent par la génération et la progéniture, par la voie "
         "du mariage entre le mâle et la femelle. » Le hadīth a explicité les phases — « il "
         "est une goutte dans la première, un caillot dans la seconde, puis une masse de "
         "chair dans la troisième ; après quoi il est devenu prêt à ce que l'on souffle en "
         "lui le souffle vital ; il passe ainsi cent vingt jours en trois phases » — la "
         "leçon fait l'arithmétique : quarante, puis quarante, puis quarante. Et elle "
         "réconcilie le hadīth avec le verset : Allah « a mentionné ces trois phases, sans "
         "en fixer la durée, en plusieurs sourates » ; al-Muʾminūn 12-14 est imprimé en "
         "entier — « Nous avons certes créé l'homme d'une extraction d'argile ; puis Nous en "
         "fîmes une goutte dans un reposoir ferme ; puis Nous fîmes de la goutte un caillot, "
         "et Nous fîmes du caillot une masse de chair, et Nous fîmes de la masse de chair "
         "des os, et Nous revêtîmes les os de chair ; puis Nous l'engendrâmes comme une "
         "autre création — béni soit Allah, le meilleur des créateurs » — et la leçon note "
         "elle-même : « en ces versets, que la masse de chair devient des os avant le "
         "souffle du souffle vital » — les trois phases du hadīth sont le premier tiers du "
         "parcours, et le souffle suit la complétion que le verset décrit : le hadīth et le "
         "Coran se lisent l'un par l'autre. Le fruit : « de la contemplation de l'origine de "
         "sa création et des phases de sa création, on prend conscience de la grandeur "
         "d'Allah, de Sa puissance et de la prodigieuse finesse de Son ouvrage » — « et l'on "
         "voit, dans le miracle de la création, de quoi éblouir les intellects et affermir "
         "les âmes »."),
        ("Ce que le hadīth porte et que l'analyse ne développe pas : « l'ange est envoyé vers "
         "lui et il souffle en lui le souffle vital, et il reçoit l'ordre de quatre paroles : "
         "l'inscription de sa subsistance, son terme, son œuvre, [et s'il sera] malheureux "
         "ou heureux » — l'écriture qui précède l'entrée au monde, l'écho du décret de la "
         "leçon 3 (la foi au décret, « l'écriture dans la Table gardée ») ; et les deux "
         "scènes du Livre : « l'un de vous œuvrera certes selon l'œuvre des gens du Paradis, "
         "jusqu'à ce qu'il n'y ait entre lui et elle qu'une coudée, alors le Livre le "
         "devance, et il œuvre selon l'œuvre des gens du Feu et il y entre » — et son "
         "inverse ; la préparation de la leçon 5 les avait demandées ; la leçon ne les "
         "développe pas dans son analyse — consigné au journal, le commentaire les reprend "
         "du texte même du hadīth. Les utilités en trois : « l'orientation de l'homme à "
         "contempler sa création et les phases qu'il traverse, pour qu'il prenne conscience "
         "de la réalité de son moi » ; « l'argument en faveur de la véracité de la "
         "Résurrection » — « quiconque est capable de rassembler l'homme dans la première "
         "création, puis de souffler en lui le souffle vital, est capable de rassembler ses "
         "parties après qu'il est devenu poussière » ; et la preuve de la prophétie — « le "
         "véridique confirmé informe de semblables réalités de l'invisible, auxquelles nul "
         "accès que par la voie de la Révélation ». L'évaluation en deux items retourne au "
         "fil. L'exploitation imprime al-Ḥaǧǧ 5 en entier — « c'est Nous qui vous avons créés de "
         "poussière, puis d'une goutte, puis d'un caillot, puis d'une masse de chair formée "
         "et informée, pour vous donner une démonstration » — la naissance (« Nous vous "
         "faisons sortir à l'état de nourrisson »), la maturité, la mort, le décrépit ; la "
         "terre inerte qui « frémit, gonfle et fait germer de chaque couple une belle "
         "végétation » ; deux questions — les phases « dans la création et après la "
         "création », et « Qu'apporte le lien entre les phases de la création de l'homme et "
         "le verdissement de la terre ? » — la poussière et la végétation, l'image de la "
         "Résurrection déjà posée par le tamhīd (Nūḥ 17-18). La préparation demande la "
         "rubrique du soutien et de l'application (ad-daʿm wa-t-taṭbīq), rendue au titre "
         "seul dans la couche française — consigné au journal."),
    ],
    "points": [
        ("Fil de révision : trois objectifs (le sens du rassemblement ; les phases ; "
         "affermir la foi par la contemplation) → tamhīd (trois ténèbres ; Nūḥ 17-18) → le "
         "hadīth et le double sceau → le rassemblement, « l'unification du dispersé » → les "
         "phases et le compte de cent vingt jours → al-Muʾminūn 12-14 et la suite du "
         "parcours → les quatre paroles et le Livre le devance (texte du hadīth) → "
         "utilités en trois → évaluation en deux items → al-Ḥaǧǧ 5 → iʿdād (le soutien et "
         "l'application)."),
        ("Le double sceau aṣ-ṣādiq al-maṣdūq : « celui qui informe d'une parole droite » et "
         "« celui dont on confirme ce qu'il apporte de la Révélation » — l'attestation du "
         "narrateur prépare la réception des réalités de l'invisible ; la balise porte les "
         "deux Ṣaḥīḥ."),
        ("Le rassemblement : « l'unification du dispersé » — l'eau dispersée que Allah "
         "rassemble « en le lieu de la naissance, depuis l'utérus, en ses phases », jusqu'à "
         "la naissance."),
        ("Le glossaire du hadīth : la goutte (l'eau peu abondante et limpide), le caillot "
         "(de l'accrochement — l'embryon s'accroche à la paroi de l'utérus), la masse de "
         "chair (l'image de la mastication), le souffle vital (par quoi l'homme vit ; il "
         "relève de l'ordre d'Allah)."),
        ("Les phases : quarante, puis quarante, puis quarante — « il passe ainsi cent vingt "
         "jours en trois phases », puis il est « prêt à ce que l'on souffle en lui le "
         "souffle vital » ; al-Muʾminūn 12-14 : de la masse de chair, les os, puis la "
         "chair, puis « une autre création » — « la masse de chair devient des os avant le "
         "souffle du souffle vital » : le hadīth et le verset se lisent l'un par l'autre."),
        ("Les quatre paroles inscrites (la subsistance, le terme, l'œuvre, malheureux ou "
         "heureux) et les deux scènes du « Livre le devance » à la coudée : portées par le "
         "texte du hadīth, non développées par l'analyse (consigné au journal) ; l'écho du "
         "décret et de « l'écriture dans la Table gardée » (leçon 3)."),
        ("Les utilités : contempler sa création « pour qu'il prenne conscience de la "
         "réalité de son moi » ; l'argument de la Résurrection — la première création "
         "garantie de la seconde (« après qu'il est devenu poussière ») ; la preuve de la "
         "prophétie — des réalités « auxquelles nul accès que par la voie de la "
         "Révélation »."),
        ("L'exploitation : al-Ḥaǧǧ 5 imprimé en entier — les phases « dans la création et "
         "après la création » (poussière, goutte, caillot, masse de chair « formée et "
         "informée » ; nourrisson, maturité, mort, décrépit) et le lien avec le "
         "verdissement de la terre — la même image que le tamhīd (Nūḥ 17-18) ; l'iʿdād "
         "demande le soutien et l'application (rendu au titre seul — consigné)."),
    ],
    "vocabulaire": [
        {"ar": "اطوار خلق الانسان", "translit": "ʾaṭwār ḫalq al-ʾinsān",
         "fr": "les phases de la création de l'homme — la goutte, le caillot, la masse de chair ; cent vingt jours en trois phases"},
        {"ar": "الصادق المصدوق", "translit": "aṣ-ṣādiq al-maṣdūq",
         "fr": "le véridique confirmé — le double sceau du Prophète à l'ouverture du hadīth : celui qui informe d'une parole droite, celui dont on confirme ce qu'il apporte de la Révélation"},
        {"ar": "النطفة", "translit": "an-nuṭfa",
         "fr": "la goutte — « le sperme ; son origine est l'eau peu abondante et limpide » ; la première phase, quarante jours"},
        {"ar": "العلقة", "translit": "al-ʿalaqa",
         "fr": "le caillot — de l'accrochement : l'embryon, après le stade de la goutte, s'accroche à la paroi de l'utérus ; la deuxième phase"},
        {"ar": "المضغة", "translit": "al-muḍġa",
         "fr": "la masse de chair — « un morceau de chair doté de la capacité de ce que mâche le mangeur » ; la troisième phase"},
        {"ar": "الروح", "translit": "ar-rūḥ",
         "fr": "le souffle vital — « par quoi l'homme vit ; il relève de l'ordre d'Allah » ; soufflé par l'ange envoyé vers l'embryon"},
        {"ar": "جمع الخلق في الرحم", "translit": "ǧamʿ al-ḫalq fī ar-raḥim",
         "fr": "le rassemblement de la création dans l'utérus — « l'unification du dispersé : la réunion des éléments et des parties les unes aux autres »"},
        {"ar": "مراحل خلق الانسان في بطن امه", "translit": "marāḫil ḫalq al-ʾinsān fī baṭn ʾummihi",
         "fr": "les étapes de la création de l'homme dans le ventre de sa mère — la rubrique de la deuxième section de l'analyse"},
    ],
    "avertissement": "Ce commentaire est un guide de lecture du manuel ; en cas de divergence d'expression, le manuel et sa traduction savante font foi.",
}

ENTREES = [('pdf-5', E_5), ('pdf-6', E_6)]

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
bloque = [d for d, _ in ENTREES if d in com]
if bloque:
    print(f'!! déjà présent : {bloque} — rien de fait')
    raise SystemExit(1)
for docid, e in ENTREES:
    com[docid] = norme_entree(e)

with open(CHEMIN, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
    f.write('\n')

# Garde-fous : volume + ponctuation FR + arabes hors parenthèses + guillemets appariés
data2 = json.load(open(CHEMIN, encoding='utf-8'))
print('entrées au total :', len(data2['commentaires']), sorted(data2['commentaires'].keys()))
motif_ar = re.compile(r'[\u0600-\u06FF\u0750-\u077F\u08A0-\u08FF\uFDFA]')
mauvais = 0
for DOCID in ('pdf-5', 'pdf-6'):
    e = data2['commentaires'][DOCID]
    mots = sum(len(x.split()) for x in [e['resume']] + e['explication'] + e['points'])
    print(f'{DOCID} : {mots} mots (resume+explication+points), vocab {len(e["vocabulaire"])}')
    textes = [e['resume'], e['avertissement']] + e['explication'] + e['points'] \
             + [v['fr'] for v in e['vocabulaire']] + [v['translit'] for v in e['vocabulaire']]
    for t in textes:
        hors_parenth = re.sub(r'\([^)]*[\u0600-\u06FF][^)]*\)', '()', t)
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
        if motif_ar.search(v['fr']):
            mauvais += 1
            print('   vocab fr contient de l arabe :', v['fr'][:60])
print('contrôle ponctuation/arabe FR :', 'PASS' if mauvais == 0 else f'ÉCHEC ({mauvais})')

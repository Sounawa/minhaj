#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""R747 — commentaires des leçons 7-8 hadith-5ep : pdf-7 (دعم وتطبيق —
la leçon de consolidation : synthèse écrite sur l'intention, quatre versets,
six questions d'analyse régressives, brochure et fruits éducatifs) et pdf-8
(القضاء والقدر — la suite du quatrième hadīth des Quarante : les quatre
paroles inscrites, les deux scènes du Livre, les ultimes aboutissements).
Quatrième vague du livre (SUIVANT de R744, leçons 7-8 précisées ; hadith-5ep
6/29 au départ). Rédaction d'après la lecture complète FR des deux leçons
(extraction non lossy scripts/extrait-r747.py). Aucune invention (règle 2) :
hadiths, versets, citations et attributions tels que la leçon les donne.
NB de lecture consigné (zone IA-2, journal worklog) : les références imprimées
du tirage portent al-Māʾida 91, at-Tawba 14 et al-Muʾminūn 61 — les versets
qui portent ces paroles sont le 89, le 18 et le 60 (numérotation courante) ;
le commentaire le dit en langage lecteur, comme en R742 pour al-Baqara 194/195.
Garde-fous de comm-r742.py repris (typographie FR, arabe entre parenthèses
seulement, vocab ar sans harakat, guillemets appariés) + fenêtre de mots
1700-2400 (resume+explication+points) par entrée."""
import json, re, os, sys

CHEMIN = 'content/commentaires/hadith-5ep.json'

E_7 = {
    "auteur": "IA-1, tour R747",
    "resume": ("Guide de lecture de la leçon 7 (le renforcement et l'application — daʿm "
               "wa-t-taṭbīq (دعم وتطبيق)) : la leçon de consolidation du manuel — la première "
               "du livre (la 14, la 20 et la 28 portent le même titre) —, qui n'installe "
               "aucun hadīth nouveau mais récapitule les leçons précédentes : « les actes "
               "valent aux intentions (la bonne intention, an-niyya), l'islām et l'īmān, "
               "l'excellence (iḥsān) avec le hadīth de Ǧibrīl, les cinq piliers de l'islām "
               "et les phases de la création de l'homme ». Le texte de la leçon n'est pas un "
               "hadīth du recueil mais une synthèse écrite sur l'intention — « le fondement "
               "même dans l'appréciation des actes et de leur non-prise en compte » —, appuyée "
               "de quatre versets, de la frivolité des serments (al-Māʾida) à l'entretien des "
               "mosquées (at-Tawba). La compréhension fait tourner cinq expressions et trois "
               "contraires ; l'analyse pose six questions qui relient toutes le texte aux "
               "leçons 1 à 6 ; l'application demande une brochure sur les piliers et les "
               "fruits éducatifs des deux premiers hadīths du manuel ; la préparation ouvre "
               "la leçon 8 — le décret et la prédestination — par « l'inscription de sa "
               "subsistance » et « le Livre le devance »."),
    "explication": [
        ("La leçon interrompt le fil des Quarante pour mesurer ce qui a été acquis. Sa "
         "présentation la nomme « la leçon de consolidation du manuel » et énumère le bagage "
         "à réviser : les actes et les intentions, l'islām et l'īmān, l'excellence avec le "
         "hadīth de Ǧibrīl, les cinq piliers de l'islām, les phases de la création de "
         "l'homme — fondée comme les précédentes sur « le hadith tiré du livre des Arbaʾūn "
         "nawawiyya de l'imam al-Nawawī, avec le commentaire d'Ibn Daqīq al-ʿĪd », à "
         "l'intention des élèves de cinquième année de l'enseignement traditionnel (taʾlīm "
         "ʾatīq). Trois objectifs formulent le contrat pédagogique : « Évaluer mes "
         "acquisitions de savoir dans les leçons précédentes » ; « Éprouver mes capacités à "
         "comprendre les hadīths et à les analyser » ; « Incarner les valeurs de la foi "
         "(īmān) et les valeurs morales dans ma vie » — savoir évalué, capacité d'analyse "
         "éprouvée, valeur incarnée : la consolidation ne répète pas, elle met à l'épreuve. "
         "La leçon répond aussi à la préparation de la leçon 6, qui demandait déjà la "
         "rubrique du soutien et de l'application (ad-daʿm wa-t-taṭbīq) — posée d'avance."),
        ("Le texte (an-naṣṣ) est ici une synthèse écrite, non un hadīth du recueil. Son "
         "premier mouvement pose le principe : « L'intention représente le fondement même "
         "dans l'appréciation des actes et de leur non-prise en compte » — l'appréciation "
         "(iʿtibār al-aʿmāl) et sa suspension relèvent toutes deux de ce qui a été eu en "
         "vue. C'est pourquoi « la Loi islamique (aš-šarīʾa al-islāmiyya) a accordé une "
         "attention extrême au dessein du sujet obligé (al-mukallaf) et à son intention, "
         "que l'affaire concerne les engagements contractés, les actes d'adoration, les "
         "transactions ou autre » : le hadīth des intentions (leçon 2) s'étend ici à tout le "
         "champ de la Loi — les cultes, les engagements, les transactions —, et le dessein "
         "du sujet obligé devient le premier critère d'examen. Deux versets attestent d'emblée "
         "ce rang : « Allah ne vous tiendra pas rigueur de la frivolité dans vos serments ; "
         "mais Il vous tiendra rigueur de ce que vos serments ont contracté » (Sourate "
         "al-Māʾida — la référence imprimée porte le verset 91 ; le verset qui porte ces "
         "paroles est le 89) — la rigueur s'attache au serment sérieusement contracté, non à "
         "la frivolité qui n'a pas été eu en vue ; et « On ne leur a cependant ordonné que "
         "d'adorer Allah, Lui vouant un culte pur, en monothéistes purs » (Sourate al-Bayyina "
         "— verset 5) — l'adoration se définit par la pureté du dessein et la pureté du "
         "monothéisme (ḥunafāʾ)."),
        ("Le second mouvement élève l'intention dans la religion : « elle occupe en outre une "
         "place élevée », « par ce qu'elle éduque comme effets excellents sur les paroles de "
         "l'homme et ses actes, dans toutes les affaires de la religion : prière, zakāt, "
         "jeûne, pèlerinage, et autres affaires de l'islām, règles de l'īmān et degrés de "
         "l'iḥsān ». La phrase fait revenir en une seule ligne les trois leçons de doctrine "
         "du manuel — les affaires de l'islām, les règles de l'īmān, les degrés de l'iḥsān — "
         "et la distinction qu'elles ont apprise est suspendue à l'intention : « ce qui "
         "distingue entre l'islām et l'īmān, ce ne sont pas les paroles, mais les intentions "
         "et ce sur quoi les cœurs se sont arrêtés » — exactement ce que le hadīth de Ǧibrīl "
         "avait enseigné terme à terme, et que l'analyse interrogera par le verset des "
         "Bédouins. Deux versets appuient encore ce rang : « Sers-Moi donc, et accomplis la "
         "prière en Mon souvenir » (Sourate Ṭāhā — verset 14) — l'adoration ordonnée et son "
         "dessein ; et « Certes, n'entretient les mosquées d'Allah que celui qui croit en "
         "Allah et au Jour dernier, accomplît la prière, acquitte la zakāt et ne craint "
         "qu'Allah ; ceux-là, il se peut qu'ils soient parmi les bien-guidés » (Sourate "
         "at-Tawba — la référence imprimée porte le verset 14 ; le verset qui porte ces "
         "paroles est le 18) — l'œuvre extérieure ne se soutient que par la foi qui "
         "l'alimente : l'entretien des mosquées est donné à la croyance, à la prière, à "
         "l'aumône et à la crainte réunies."),
        ("La compréhension fait d'abord tourner cinq expressions du texte : « iʿtibār "
         "al-aʿmāl wa-ʿadam iʿtibārihā (l'appréciation des actes et leur non-prise en "
         "compte) » — le double registre ouvert dès la première phrase ; « awlat ihtimāman "
         "bālighan (elle a accordé une attention extrême) » ; « ʿaqqadtum al-aymāna (vous "
         "avez contracté les serments) » — l'expression même du verset d'al-Māʾida ; "
         "« ḥunafāʾ (en monothéistes purs) » ; et « lā yultikum min aʿmālikum šayʾan (Il ne "
         "vous fera perdre rien de vos œuvres) ». Le vocabulaire de la leçon relie ainsi les "
         "versets à la thèse qu'ils portent. Trois contraires sont demandés — « al-lafẓ (l'énoncé) », "
         "« ḥunafāʾ (le monothéiste pur) », « āṯārun ḥamīda (des effets excellents) » — "
         "l'exercice qui apprend à penser par opposition, dans la ligne des leçons "
         "précédentes. Enfin l'extraction : « Extraire du texte ce qu'il contient de valeurs "
         "découlant de la prophétie véridique (an-nubuwwa aṣ-ṣādiqa) » — montrer que ces "
         "enseignements sur l'intention descendent de la prophétie même : le texte cite la "
         "Loi et le Coran, et le fil vers le hadīth « Les actes ne valent qu'aux intentions » "
         "que la première question d'analyse rattachera au verset d'al-Māʾida."),
        ("L'analyse porte six questions, toutes régressives vers les leçons précédentes. La "
         "première demande de « montrer le lien entre ce verset et le hadīth : “Les actes ne "
         "valent qu'aux intentions” » : la rigueur attachée au serment contracté — non à la "
         "frivolité — est l'attestation coranique du principe prophétique. La seconde met en "
         "balance : « Le sujet obligé (al-mukallaf) répond-il de son intention, ou de ses "
         "actes et de ses paroles ? » — la question des deux registres que le texte a séparés "
         "(le dessein, et les paroles-actes qu'il éduque). La troisième assemble le tout : "
         "« Extraire du texte ce qui atteste : la prophétie véridique — l'islām — l'īmān — "
         "l'iḥsān » — les quatre rangs que les leçons 1 à 6 ont successivement installés, "
         "maintenant réunis dans un seul exercice d'extraction. La quatrième rouvre la "
         "doctrine : « Parmi les piliers de l'īmān : la foi en les anges et en les "
         "messagers ; citer pour chaque pilier une preuve de la Loi appropriée » — deux des "
         "six piliers appris en leçon 3, à prouver chacun par la Loi. La cinquième relie deux "
         "sources : « Quel est le lien entre la parole d'Allah — le Très-Haut — : “Les "
         "Bédouins ont dit : Nous avons cru. Dis : Vous n'avez pas cru ; dites plutôt : Nous "
         "nous sommes islamisés — la foi n'a pas encore pénétré vos cœurs.” (Sourate "
         "al-Ḥuǧurāt — verset 14) et le hadīth de Ǧibrīl — sur lui le salut — dans les "
         "leçons précédentes ? » — le verset qui dit l'islām des bouches et la foi absente "
         "des cœurs est la déclaration même de la distinction enseignée par l'interrogatoire "
         "de Ǧibrīl. La sixième remonte au fruit : « Extraire du texte les fruits et les "
         "visées qui relient le croyant à son Créateur — le Puissant et le Majestueux »."),
        ("L'application porte la consolidation hors du cahier. Première production : « Je "
         "confectionne une brochure (maṭwiyya) consacrée aux piliers de l'islām et de "
         "l'īmān » — les piliers de la foi (leçon 3) et de l'islām (leçon 5) remontés de la "
         "main même de l'élève : ce qui avait été reçu exposé devient un objet fabriqué, "
         "rangé, relisible. Seconde production : « Je dégage les fruits éducatifs des deux "
         "hadīths suivants, en montrant leur effet dans le renforcement de la foi et la "
         "droiture des mœurs » — le hadīth « Les actes ne valent qu'aux intentions... » "
         "(leçon 2) et le hadīth « Tandis que nous étions assis auprès du Messager d'Allah — "
         "prière et salut d'Allah sur lui —... » (leçons 3-4, le hadīth de Ǧibrīl) : les "
         "deux premiers hadīths du recueil appris dans le manuel, l'un sur l'intention qui "
         "gouverne l'acte, l'autre sur les trois degrés de la religion — leur effet conjoint "
         "est exactement le programme de la leçon : renforcement de la foi, droiture des "
         "mœurs."),
        ("La préparation de la leçon suivante convoque le chapitre qui vient : « Je mémorise "
         "le hadīth de la leçon qui vient, et j'accomplis ce qui suit » : « Expliquer le sens "
         "de : bi-kitbi rizqihi (l'inscription de sa subsistance) — faysbiqu ʿalayhi al-kitāb "
         "(le Livre le devance) » et « Montrer la visée des quatre paroles dans le hadīth de "
         "la leçon ». Ces demandes reprennent un fil ancien : la préparation de la leçon 5 "
         "avait déjà posé de préciser « le Livre le devance » et de dire ce qu'Allah inscrit "
         "sur l'homme après sa création ; la leçon 6 avait lu les phases du hadīth "
         "d'ʿAbdullāh ibn Masʿūd sans développer ces questions dans son analyse ; la "
         "consolidation les reprend à son compte et les porte vers la leçon 8, consacrée au "
         "décret et à la prédestination — les quatre paroles inscrites (la subsistance, le "
         "terme, l'œuvre, malheureux ou heureux) et les deux scènes du Livre y recevront "
         "leur leçon entière."),
    ],
    "points": [
        ("Fil de révision : trois objectifs (évaluer ses acquisitions ; éprouver la "
         "compréhension et l'analyse des hadīths ; incarner les valeurs de la foi et les "
         "valeurs morales) → un texte-synthèse sur l'intention appuyé de quatre versets → "
         "cinq expressions et trois contraires → six questions d'analyse régressives vers "
         "les leçons 1 à 6 → deux productions (brochure ; fruits éducatifs de deux hadīths) "
         "→ préparation (leçon 8, les quatre paroles)."),
        ("Le texte n'est pas un hadīth du recueil mais une synthèse écrite : « l'intention "
         "représente le fondement même dans l'appréciation des actes et de leur non-prise en "
         "compte » — la Loi « a accordé une attention extrême au dessein du sujet obligé », "
         "dans « les engagements contractés, les actes d'adoration, les transactions ou "
         "autre »."),
        ("Les quatre versets : la rigueur attachée au serment contracté, non à la frivolité "
         "(al-Māʾida) ; le culte pur des monothéistes purs (al-Bayyina 5) ; « Sers-Moi donc, "
         "et accomplis la prière en Mon souvenir » (Ṭāhā 14) ; l'entretien des mosquées donné "
         "à celui qui croit, prie, acquitte et ne craint qu'Allah (at-Tawba)."),
        ("La distinction d'islām et d'īmān suspendue à l'intention : « ce ne sont pas les "
         "paroles, mais les intentions et ce sur quoi les cœurs se sont arrêtés » — la "
         "formule qui raccorde le texte-synthèse au hadīth de Ǧibrīl et au verset des "
         "Bédouins (al-Ḥuǧurāt 14)."),
        ("Six questions d'analyse régressives : lien verset-hadīth ; le sujet obligé répond-il "
         "de son intention ou de ses actes et paroles ; ce qui atteste prophétie véridique, "
         "islām, īmān, iḥsān ; preuves de la Loi pour la foi en les anges et en les "
         "messagers ; Ḥuǧurāt 14 et le hadīth de Ǧibrīl ; les fruits qui relient le croyant "
         "à son Créateur."),
        ("L'application produit : la brochure (maṭwiyya) des piliers de l'islām et de l'īmān — "
         "la leçon reçue devient un objet fabriqué par l'élève ; et les fruits éducatifs des "
         "deux premiers hadīths du recueil « en montrant leur effet dans le renforcement de "
         "la foi et la droiture des mœurs »."),
        ("La préparation repose un fil ancien : « le Livre le devance » et l'inscription après "
         "la création, demandés dès la préparation de la leçon 5, non développés par "
         "l'analyse de la leçon 6, repris ici pour la leçon 8 — le décret et la "
         "prédestination."),
        ("Le vocabulaire consolide le lexique des leçons précédentes : l'appréciation des "
         "actes et sa suspension, l'attention extrême, les serments contractés, les "
         "monothéistes purs — et l'exercice des trois contraires demandés (al-lafẓ, ḥunafāʾ, "
         "āṯārun ḥamīda)."),
    ],
    "vocabulaire": [
        {"ar": "دعم وتطبيق", "translit": "daʿm wa-t-taṭbīq",
         "fr": "le renforcement et l'application — la leçon de consolidation du manuel, qui met à l'épreuve les acquisitions des leçons précédentes avant d'ouvrir un nouveau chapitre."},
        {"ar": "اعتبار الاعمال", "translit": "iʿtibār al-aʿmāl",
         "fr": "l'appréciation des actes — la prise en compte de l'acte selon l'intention qui l'a porté ; le texte en fait « le fondement même dans l'appréciation des actes et de leur non-prise en compte »."},
        {"ar": "المكلف", "translit": "al-mukallaf",
         "fr": "le sujet obligé — l'homme chargé par la Loi des obligations religieuses ; la Loi s'attache à « son dessein et à son intention », dans les adorations comme dans les transactions."},
        {"ar": "عقدتم الايمان", "translit": "ʿaqqadtum al-aymāna",
         "fr": "vous avez contracté les serments — l'expression du verset d'al-Māʾida cité par la leçon : le serment sérieusement contracté engage, quand la frivolité n'est pas prise en compte."},
        {"ar": "حنفاء", "translit": "ḥunafāʾ",
         "fr": "les monothéistes purs — ceux qui vouent à Allah « un culte pur », selon le verset d'al-Bayyina cité dans la leçon ; l'une des trois expressions dont un contraire est demandé."},
        {"ar": "النبوة الصادقة", "translit": "an-nubuwwa aṣ-ṣādiqa",
         "fr": "la prophétie véridique — la leçon demande d'extraire du texte « ce qu'il contient de valeurs découlant de la prophétie véridique »."},
        {"ar": "المتوية", "translit": "al-maṭwiyya",
         "fr": "la brochure — la production demandée en application : une brochure consacrée aux piliers de l'islām et de l'īmān, confectionnée par l'élève lui-même."},
        {"ar": "الاعداد القبلية", "translit": "al-iʿdād al-qabliyya",
         "fr": "la préparation de la leçon suivante — la rubrique qui clôt chaque leçon ; ici elle annonce le hadīth de la leçon 8 et ses quatre paroles."},
    ],
    "avertissement": "Ce commentaire est un guide de lecture du manuel ; en cas de divergence d'expression, le manuel et sa traduction savante font foi.",
}

E_8 = {
    "auteur": "IA-1, tour R747",
    "resume": ("Guide de lecture de la leçon 8 (le décret et la prédestination — al-qaḍāʾ "
               "wa-l-qadar (القضاء والقدر)) : la suite du quatrième hadīth des Quarante, "
               "rapporté par ʿAbdullāh ibn Masʿūd — la leçon 6 avait lu les phases de la "
               "création, la présente lit ce que l'ange écrit au moment où l'âme est soufflée "
               "dans l'embryon : « l'inscription de sa subsistance, son terme, son œuvre, [et "
               "s'il sera] malheureux ou heureux », puis les deux scènes où « le Livre le "
               "devance » à une coudée du terme. Le tamhīd part du mauvais usage de la "
               "croyance : penser que ni « le choix du serviteur, ni son œuvre, ni le sceau "
               "qu'il reçoit à cet égard » n'ont d'effet. L'analyse répond en trois stations : "
               "ce qu'est le décret (avec al-Samʿānī — la voie du Livre et de la Sunna, sans "
               "analogie ni raison), ce qui est inscrit (les quatre paroles une à une, "
               "d'après le Ǧāmiʿ al-ʿUlūm wa-l-Ḥikam), et les actes par leurs ultimes "
               "aboutissements — la belle fin demandée à Allah plutôt que la confiance dans "
               "l'apparence. L'exploitation imprime le hadīth de ʿAlī : « Agissez, car chacun "
               "est facilité », et la préparation ouvre la leçon 9 : la biographie de ʿĀʾiša "
               "et le sens de « ar-rad » (le rejet)."),
    "explication": [
        ("La leçon 8 rouvre le quatrième hadīth des Quarante — celui dʿAbdullāh ibn Masʿūd, "
         "« le Véridique confirmé dans sa véracité (aṣ-ṣādiq al-maṣdūq) » — pour en lire la "
         "suite : la leçon 6 avait suivi les phases de la création dans le ventre ; la "
         "présente prend le "
         "hadīth au moment où « on lui envoie l'ange, qui souffle en lui le souffle vital, et "
         "il reçoit l'ordre de quatre paroles », puis les deux scènes du Livre. Elle répond "
         "à la préparation de la leçon 7 : mémoriser le hadīth qui vient, "
         "expliquer « bi-kitbi rizqihi (l'inscription de sa subsistance) » et « faysbiqu "
         "ʿalayhi al-kitāb (le Livre le devance) », « montrer la visée des quatre paroles "
         "dans le hadīth de la leçon ». Trois objectifs : "
         "« Que je me familiarise avec le sens du décret (qaḍāʾ), et avec ce qui est inscrit "
         "par le décret » ; « Que je saisisse que c'est aux ultimes aboutissements (ḫawātīm) "
         "que se mesure l'exemple à tirer des actes » ; « Que je croie qu'Allah, le Très-Haut, "
         "est Agissant et libre de choisir (fāʾil muḫtār), faisant ce qu'Il veut »."),
        ("Le tamhīd part du mauvais usage de la croyance : la foi au décret et à la "
         "prédestination figure « parmi les grandes croyances de la foi (īmān) », « mais "
         "combien sont nombreux ceux qui en comprennent mal le sens, au point de penser que "
         "l'heureux l'est par le décret, que le malheureux l'est par le décret, et que ni le "
         "choix du serviteur, ni son œuvre, ni le sceau qu'il reçoit à cet égard n'ont "
         "d'effet ». La doctrine posée en leçon 3 comme sixième pilier de la foi reçoit ici "
         "son avertissement. "
         "Les trois questions de l'exorde — « Quel est donc le sens du décret (qaḍāʾ) ? Et "
         "qu'est-ce qui est inscrit par le décret ? Et quelle est la relation du décret aux "
         "ultimes aboutissements des actes ? » — dessinent la carte de l'analyse, trois "
         "sections pour trois questions."),
        ("Le texte rend le hadīth en entier [Ṣaḥīḥ de al-Buḫārī et Muslim] : la création "
         "« rassemblée dans le ventre de sa mère pendant quarante jours, à l'état de goutte "
         "de semence (nuṭfa) » ; « puis on lui envoie l'ange, qui souffle en lui le "
         "souffle vital, et il reçoit l'ordre de quatre paroles : l'inscription de sa "
         "subsistance, son terme, son œuvre, [et s'il sera] malheureux ou heureux » ; puis "
         "les deux scènes symétriques — « l'un de vous œuvrera certes selon l'œuvre des gens "
         "du Paradis, jusqu'à ce qu'il n'y ait entre lui et elle qu'une coudée (dirāʾ) ; "
         "alors le Livre le devance, et il œuvre selon l'œuvre des gens du Feu et il y entre », "
         "et son inverse. La notice du transmetteur renvoie à la biographie déjà donnée en "
         "leçon 6. Le glossaire fixe deux gloses : « jusqu'à ce qu'il n'y ait entre lui et elle qu'une "
         "coudée » — « que son terme se rapproche » ; et « le Livre le devance » — « "
         "l'inscription est arrêtée en sa faveur ». L'extraction des contenus pose trois "
         "travaux — « l'attestation du décret et de la prédestination » ; "
         "« ce qu'Allah inscrit sur l'homme, après sa création, au fil de ses phases » ; et "
         "la question qui porte toute la leçon : « Où se situe le rapport entre ce qui est "
         "inscrit sur l'homme et son œuvre ? »"),
        ("La première section de l'analyse répond à la première question du tamhīd. Dans la "
         "parole du Prophète — prière et salut d'Allah sur lui —, les quatre paroles « il y a "
         "une preuve de l'affirmation de la prédestination (qadar), conformément à la doctrine "
         "des gens de la Sunna, et du fait que tous les événements s'accomplissent par le "
         "décret d'Allah le Très-Haut et Sa prédestination, leur bien et leur mal, leur "
         "utilité et leur nuisance » — « Il ne sera pas interrogé sur ce qu'Il fait, tandis "
         "qu'eux-mêmes seront interrogés » (Sourate al-Anbiyāʾ — verset 23) : « Il fait dans "
         "Sa royauté ce qu'Il veut. » L'analyse imprime ensuite l'imam al-Samʿānī — qu'Allah "
         "lui fasse miséricorde — (Fatḥ al-Bārī) : « la voie pour connaître ce chapitre "
         "consiste à s'en tenir au Livre et à la Sunna, sans y mêler l'analogie (qiyās) ni "
         "la raison (ʿaql) » ; « quiconque s'écarte, en la matière, de l'attitude d'attente "
         "(tawaqquf) s'égare et erre dans les mers de l'égarement (ḥayra) » ; « le décret en "
         "effet est un secret parmi les secrets d'Allah le Très-Haut » — « aucun prophète "
         "envoyé ni ange rapproché ne l'a emporté ». De ce caractère caché procède la règle "
         "pratique : les hadīths « interdisent de délaisser l'œuvre en s'appuyant sur ce qui "
         "a précédé de la prédestination », rendent « obligatoire l'agir selon les charges "
         "religieuses (takālīf) auxquelles l'ordre est parvenu, car celui-ci est un apparent », "
         "quand le décret est « un invisible que seul Allah le Très-Haut connaît » — "
         "l'apparent agi, l'invisible jamais plaidé."),
        ("La seconde section inventorie ce qui est inscrit : « ce décret (qadar) qu'Allah a "
         "décrété avant que le monde n'existe, et qu'Il a fait paraître à un ange auquel Il a "
         "ordonné de l'écrire et de l'exécuter au moment où l'âme est soufflée dans "
         "l'embryon ; c'est le décret propre à chaque individu, dont la quintessence tient en "
         "ces quatre paroles » — le Ǧāmiʿ al-ʿUlūm wa-l-Ḥikam (avec adaptations) les "
         "détaille une à une. La subsistance (rizq) : « ce dont l'homme tire profit » ; son "
         "inscription est « son estimation, en peu ou en abondance » ; « on l'appelle "
         "subsistance même si l'homme l'acquiert par une voie illicite (ḥarām), mais il en "
         "rendra compte ». L'échéance (aǧal) : « la durée "
         "de la vie de l'homme en ce bas-monde » ; « sa longueur ou sa brèveté relève de "
         "l'estimation d'Allah le Très-Haut, non de la santé du corps ou de sa maladie ». "
         "L'œuvre (ʿamal) : « les paroles, les actes, les croyances et les dispositions que "
         "l'homme acquiert » ; son inscription : « sa description et le jugement qu'il est "
         "bon ou corrompu ». Le malheur ou le bonheur (šaqāwa / saʿāda) : « on entend par eux "
         "l'islām et la mécréance (kufr) ; ce sont les deux voies vers le Paradis et le Feu » — "
         "c'est la « visée des quatre paroles » que la préparation demandait de montrer."),
        ("La troisième section répond à la question des ultimes aboutissements. D'abord la "
         "crainte : « Il incombe à l'homme de ne pas se sentir à l'abri d'une mauvaise fin, "
         "quelle que soit son œuvre, même si l'ensemble des gens l'a loué tout au long de sa "
         "vie : il demeure un homme craintif et tremblant. » Puis le portrait de l'heureux : "
         "« celui à qui Allah a réuni le bel agir, la mauvaise opinion de lui-même par "
         "crainte, et la belle opinion de son Seigneur par espérance » — « Ceux qui dépensent "
         "ce qu'ils ont dépensé, les cœurs saisis de crainte... » (Sourate al-Muʾminūn — la "
         "référence imprimée porte le verset 61 ; le verset qui porte ces paroles est le 60). "
         "Et « la bienveillance (luṭf) d'Allah — gloire à Lui — et l'étendue de Sa "
         "miséricorde » : « la "
         "transition des gens du mal vers le bien est fréquente, et du bien vers le mal, rare "
         "et peu nombreuse » ; surtout : « la mauvaise fin n'échoit pas à celui qui a "
         "persévéré dans l'obéissance et rendu sain son apparent ; elle n'échoit qu'à celui "
         "qui porte en lui-même une corruption, un doute ou une faille intérieure, qui s'est "
         "entêté dans les grands péchés (kabāʾir) et a bravé les interdits (maḥārim) » — "
         "« l'autre narration du hadīth » l'atteste : « L'homme, certes, œuvre selon l'œuvre "
         "des gens du Paradis tant que paraît son apparence aux gens, alors qu'il est du "
         "nombre des gens du Feu » (al-Buḫārī et Muslim)."),
        ("Ce qu'il faut retirer du hadīth en trois : « l'absence de dépendance aux moyens "
         "(asbāb), tout en rendant obligatoire de les prendre, en s'en remettant à la "
         "générosité d'Allah le Très-Haut et à Sa miséricorde » ; « l'incitation au "
         "contentement (qanāʿa) : la subsistance a déjà fait l'objet d'une estimation, et "
         "son acquisition a été ordonnée par la Loi » — « elle fait en effet partie des "
         "moyens dont il nous a été ordonné de prendre » ; et ne jamais « se fier à "
         "l'apparence de sa situation présente, Allah ayant fait de l'ultime aboutissement la "
         "fin dernière » — « de là a été ordonné l'appel (duʿāʾ) à la constance (ṯabāt) dans "
         "la religion et à la belle fin ». L'exploitation imprime le hadīth de ʿAlī — qu'Allah "
         "l'agrée — [Ṣaḥīḥ de al-Buḫārī] : le Prophète — prière et salut d'Allah sur lui —, "
         "un bâton à la main, dit : « Il n'est pas un seul "
         "d'entre vous dont la place n'ait été inscrite, dans le Feu ou dans le Paradis » ; "
         "un homme de l'assistance demande : « ne nous y fierons-nous donc pas, ô Messager "
         "d'Allah ? » — réponse : « Non. Agissez, car chacun est facilité », et la récitation "
         "d'al-Layl (versets 5 à 10) — la voie à la facilité pour celui qui donne, craint et "
         "déclare vraie la plus belle récompense ; la voie à la difficulté pour celui qui est "
         "avare et traite de mensonge la plus belle récompense. Deux questions d'exploitation — "
         "que retirer de « Agissez, car chacun est facilité », et peut-on plaider le décret "
         "pour délaisser l'œuvre ? — et l'évaluation en "
         "trois items retourne au fil (l'inscription de la subsistance et de l'échéance ; le "
         "rôle de la raison ; la licéité de délaisser l'œuvre)."),
        ("La préparation ouvre la leçon suivante : « Je mémorise le hadīth de la leçon qui "
         "vient, et j'accomplis ce qui suit » : « Je recherche la biographie de la mère des "
         "croyants ʿĀʾiša — qu'Allah l'agrée » ; « Je détermine le sens de “ar-rad” (le "
         "rejet) dans le hadīth » — la notice de la transmettrice et le mot du hadīth, pour "
         "la leçon 9 consacrée aux innovations (bidʿa) dans la religion."),
    ],
    "points": [
        ("Fil de révision : trois objectifs (familiariser avec le sens du décret et ce qui "
         "est inscrit ; mesurer l'exemple des actes aux ultimes aboutissements ; croire "
         "qu'Allah est Agissant et libre de choisir) → tamhīd (le malentendu visé ; trois "
         "questions) → le hadīth en entier (phases, souffle, quatre paroles, deux scènes) → "
         "analyse en trois stations → trois utilités → exploitation (ʿAlī) → préparation "
         "(ʿĀʾiša, ar-rad)."),
        ("La continuité du fil : la préparation de la leçon 5 avait posé « le Livre le "
         "devance » et l'inscription après la création ; la leçon 6 a lu les phases sans "
         "développer ces questions ; la préparation de la leçon 7 les repose — la leçon 8 y "
         "répond."),
        ("La méthode d'al-Samʿānī (Fatḥ al-Bārī) : s'en tenir au Livre et à la Sunna « sans "
         "y mêler l'analogie (qiyās) ni la raison (ʿaql) » ; l'attitude d'attente (tawaqquf) "
        " ; le décret « un secret parmi les secrets d'Allah » — et la règle pratique qui en "
         "découle : l'apparent (les charges religieuses) agi, l'invisible (le décret) jamais "
         "plaidé."),
        ("Les quatre paroles une à une (Ǧāmiʿ al-ʿUlūm wa-l-Ḥikam, avec adaptations) : la "
         "subsistance estimée « en peu ou en abondance » — même acquise par voie illicite, "
         "« il en rendra compte » ; l'échéance liée à « l'estimation d'Allah », non à la "
         "santé du corps ; l'œuvre décrite et jugée « bon ou corrompu » ; l'islām et la "
         "mécréance comme les deux voies du bonheur et du malheur."),
        ("Les ultimes aboutissements : la crainte jusqu'au terme — « ne pas se sentir à "
         "l'abri d'une mauvaise fin, quelle que soit son œuvre » ; l'heureux réunit « le bel "
         "agir, la mauvaise opinion de lui-même par crainte, et la belle opinion de son "
         "Seigneur par espérance » (al-Muʾminūn — référence imprimée 61, verset porteur 60)."),
        ("La bienveillance (luṭf) d'Allah : du mal vers le bien la transition est fréquente, "
         "du bien vers le mal rare — la mauvaise fin n'échoit qu'à celui qui porte « une "
         "corruption, un doute ou une faille intérieure », attestée par l'autre narration « "
         "tant que paraît son apparence aux gens »."),
        ("Le hadīth de ʿAlī comme clef d'exploitation : la place inscrite « dans le Feu ou "
         "dans le Paradis », la question « ne nous y fierons-nous donc pas, ô Messager "
         "d'Allah ? » et la réponse "
         "« Non. Agissez, car chacun est facilité » avec al-Layl 5-10 — le décret ne dispense "
         "pas, il facilite l'agir."),
        ("La double absence d'excuse : ni la subsistance estimée (le contentement qanāʿa sans "
         "quitter les moyens obligatoires), ni la place inscrite (agir sans se fier à "
         "l'apparence) — « de là a été ordonné l'appel (duʿāʾ) à la constance (ṯabāt) dans "
         "la religion et à la belle fin »."),
    ],
    "vocabulaire": [
        {"ar": "القضاء والقدر", "translit": "al-qaḍāʾ wa-l-qadar",
         "fr": "le décret et la prédestination — la croyance que la leçon installe : ce qu'Allah a décrété « avant que le monde n'existe », fait paraître à un ange qui l'écrit et l'exécute « au moment où l'âme est soufflée dans l'embryon »."},
        {"ar": "اربع كلمات", "translit": "ʾarbaʿ kalimāt",
         "fr": "les quatre paroles — l'ordre reçu par l'ange : « l'inscription de sa subsistance, son terme, son œuvre, [et s'il sera] malheureux ou heureux » ; la préparation de la leçon en demandait la visée."},
        {"ar": "الرزق", "translit": "ar-rizq",
         "fr": "la subsistance — première des quatre paroles : « ce dont l'homme tire profit », estimé « en peu ou en abondance » ; appelée subsistance même si l'homme l'acquiert par une voie illicite — « mais il en rendra compte »."},
        {"ar": "الاجل", "translit": "al-aǧal",
         "fr": "l'échéance — « la durée de la vie de l'homme en ce bas-monde » ; « sa longueur ou sa brèveté relève de l'estimation d'Allah le Très-Haut, non de la santé du corps ou de sa maladie »."},
        {"ar": "العمل", "translit": "al-ʿamal",
         "fr": "l'œuvre — « les paroles, les actes, les croyances et les dispositions que l'homme acquiert » ; son inscription porte « sa description et le jugement qu'il est bon ou corrompu »."},
        {"ar": "الذراع", "translit": "ad-dirāʿ",
         "fr": "la coudée — l'espace restant « entre lui et elle » quand le terme se rapproche ; la glose du glossaire de la leçon : « que son terme se rapproche »."},
        {"ar": "الخواتيم", "translit": "al-ḫawātīm",
         "fr": "les ultimes aboutissements — « c'est à eux que se mesure l'exemple à tirer des actes » (second objectif de la leçon) ; de là l'appel (duʿāʾ) « à la constance (ṯabāt) dans la religion et à la belle fin »."},
        {"ar": "الشقاوة والسعادة", "translit": "aš-šaqāwa wa-s-saʿāda",
         "fr": "le malheur et le bonheur — la quatrième parole inscrite : « on entend par eux l'islām et la mécréance (kufr) », « les deux voies vers le Paradis et le Feu »."},
    ],
    "avertissement": "Ce commentaire est un guide de lecture du manuel ; en cas de divergence d'expression, le manuel et sa traduction savante font foi.",
}

ENTREES = [('pdf-7', E_7), ('pdf-8', E_8)]


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

# Garde-fous : volume (1700-2400 mots) + ponctuation FR + arabes hors parenthèses + guillemets
data2 = json.load(open(CHEMIN, encoding='utf-8'))
print('entrées au total :', len(data2['commentaires']), sorted(data2['commentaires'].keys()))
motif_ar = re.compile(r'[\u0600-\u06FF\u0750-\u077F\u08A0-\u08FF\uFDFA]')
mauvais = 0
for DOCID in ('pdf-7', 'pdf-8'):
    e = data2['commentaires'][DOCID]
    mots = sum(len(x.split()) for x in [e['resume']] + e['explication'] + e['points'])
    fenetre = 'PASS' if 1700 <= mots <= 2400 else 'HORS FENETRE'
    print(f'{DOCID} : {mots} mots (resume+explication+points), vocab {len(e["vocabulaire"])} — fenêtre 1700-2400 : {fenetre}')
    if fenetre != 'PASS':
        mauvais += 1
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
        if not re.search(r'[\u02BE\u02BF]', v['translit']):
            print('   note : translit sans ʾ/ʿ :', v['translit'])
print('contrôle ponctuation/arabe FR :', 'PASS' if mauvais == 0 else f'ÉCHEC ({mauvais})')
if mauvais:
    sys.exit(1)

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""R750 — commentaires des leçons 11-12 hadith-5ep : pdf-11 (إصلاح القلب —
la correction du cœur : la clôture du sixième hadīth, le cœur émir des
organes, ce qui l'amende et ce qui le corrompt, ar-rān) et pdf-12
(الدين النصيحة — le septième hadīth, Tamīm ad-Dārī : la naṣīḥa, son sens,
son immense rang, les cinq destinataires). Sixième vague du livre (SUIVANT
de R749, leçons 9-10 ; hadith-5ep 10/29 au départ). Rédaction d'après la
lecture complète FR des deux leçons (extraction non lossy
scripts/extrait-r750.py). Aucune invention (règle 2) : hadiths, versets,
citations et attributions tels que la leçon les donne.
NB de lecture consigné (zone IA-2, journal worklog) : les références
imprimées du tirage portent al-Ḥaǧǧ 44 et al-Ḥadīd 15 (pdf-11), al-Aʿrāf 20
et 78 et al-Qaṣaṣ 19 (pdf-12) — les versets qui portent ces paroles sont le
46 (al-Ḥaǧǧ), le 16 (al-Ḥadīd), le 21 et le 79 (al-Aʿrāf) et le 20
(al-Qaṣaṣ), vérifiés web ; le commentaire le dit en langage lecteur, comme
en R742/R747/R749. Correct dans le tirage : al-Muṭaffifīn 14.
NB consigné (SUIVANT de R749-b) : la annonce de vague « leçon 11 (le cœur,
septième hadīth) » était imprécise — le cœur est la CLÔTURE du sixième
hadīth (leçon 11) ; le septième hadīth (la naṣīḥa) est la leçon 12 — vague 6
= les deux, dans l'ordre du manuel.
Garde-fous de comm-r747/comm-r749 repris (typographie FR, arabe entre
parenthèses seulement, vocab ar sans harakat, guillemets appariés) +
fenêtre de mots 1700-2400 (resume+explication+points) par entrée."""
import json, re, os, sys

CHEMIN = 'content/commentaires/hadith-5ep.json'

E_11 = {
    "auteur": "IA-1, tour R750",
    "resume": ("Guide de lecture de la leçon 11 (la correction du cœur — iṣlāḥ al-qalb "
               "(إِصْلَاحُ الْقَلْبِ)) : la clôture du sixième hadīth des Quarante de "
               "l'imam al-Nawawī — les derniers « sachez-le » d'an-Nuʿmān ibn Bašīr — "
               "qu'Allah soit satisfait de lui — : « Sachez-le : dans le corps il y a un "
               "morceau de chair qui, s'il est sain, rend sain tout le corps, et s'il est "
               "corrompu, corrompt tout le corps — sachez-le : c'est le cœur » [Ṣaḥīḥ de "
               "al-Buḫārī et Muslim]. La leçon répond mot pour mot à la préparation de la "
               "leçon 10 — « J'explique l'importance du cœur parmi les membres du corps », "
               "« Je précise l'effet du cœur sur la droiture de l'œuvre ou sur sa corruption "
               "» — et l'analyse suit exactement ces deux stations. La première montre le "
               "cœur émir des organes : l'animal perçoit par lui ses intérêts, l'homme a en "
               "sus la raison (al-ʿaql), et « ce qui s'y est affermi paraît sur eux » "
               "[Ǧāmiʿ al-ʿulūm wa-l-ḥikam — adapté]. La seconde fait témoigner les œuvres : "
               "ce qui amende le cœur — de la récitation avec méditation à la fréquentation "
               "des justes, le sommet étant « l'acquisition de tout gain licite, et "
               "l'abstention des choses douteuses » — et ce qui le corrompt, avec le hadīth "
               "de at-Tirmiḏī de la tache noire et de la rouille (ar-rān, al-Muṭaffifīn 14). "
               "L'exploitation relit « leurs cœurs se sont endurcis » (al-Ḥadīd — la "
               "référence imprimée porte le verset 15 ; le verset qui porte ces paroles est "
               "le 16), et la préparation ouvre la leçon 12 : Tamīm ad-Dārī et la "
               "recommandation sincère."),
    "explication": [
        ("La leçon 11 est la station du pourquoi. La leçon 10 avait dressé la carte du "
         "licite, de l'illicite et des choses ambiguës, et s'était achevée sur l'iʿdād qui "
         "annonçait la dernière clause du même hadīth : « J'explique l'importance du cœur "
         "parmi les membres du corps », « Je précise l'effet du cœur sur la droiture de "
         "l'œuvre ou sur sa corruption ». La leçon 11 tient ces deux demandes — ce sont "
         "littéralement ses deux stations d'analyse. Trois objectifs l'encadrent : « Que "
         "je me familiarise avec la position du cœur parmi les organes » ; « Que je "
         "mentionne l'effet du cœur sur la droiture de l'œuvre ou sa corruption » ; « Que "
         "je m'emploie à corriger mon cœur selon la guidée du Prophète — prière et salut "
         "d'Allah sur lui » — connaître, juger, agir."),
        ("Le tamhīd pose d'abord la position. Le cœur « détient une position immense que "
         "le reste des membres ne saurait éluder » : il est « la forteresse de la foi "
         "(maḥkamu al-īmān) », « le lieu du regard du Miséricordieux (maḥallu naẓari "
         "ar-Raḥmān) », « le siège du devoir religieux (manāṭu at-taklīf) » et « le lieu "
         "de l'honneur (mawḍiʿu at-tašrīf) », et il est « celui qui est consulté dans la "
         "plupart des questions épineuses ». Allah l'a mentionné « dans plusieurs āyāt du "
         "noble Coran, en raison de son effet sur l'œuvre ». Les deux questions du tamhīd "
         "fixent le plan : « Quelle est donc la position du cœur parmi les organes ? Et "
         "quel est son effet sur la droiture de l'œuvre ou sa corruption ? »"),
        ("Le texte rend le hadīth entier — du licite évident aux choses ambiguës, du "
         "berger au gardien de la réserve — et s'arrête sur sa clôture : « Sachez-le : "
         "dans le corps il y a un morceau de chair qui, s'il est sain, rend sain tout le "
         "corps, et s'il est corrompu, corrompt tout le corps — sachez-le : c'est le "
         "cœur » [Ṣaḥīḥ de al-Buḫārī et Muslim]. La notice du transmetteur est d'une "
         "économie volontaire : an-Nuʿmān ibn Bašīr — qu'Allah soit satisfait de lui — "
         "« sa notice biographique a déjà été donnée (à la dixième leçon) ». Le glossaire "
         "n'a qu'une glose, mais elle porte tout le poids de la leçon : « le cœur "
         "(al-qalb) » est « à l'origine, nom verbal (maṣdar) de “il a retourné” (qalaba) "
         "» ; c'est « le nom d'un organe intérieur, caché dans le corps, dont dépend la "
         "condition de l'homme », et il fut appelé ainsi « en raison de la rapidité des "
         "pensées (ḫawāṭir) qui le traversent et de leur va-et-vient sur lui ». "
         "L'extraction ne demande qu'un travail : « J'en extrais ce qui indique "
         "l'importance du cœur et son effet sur la droiture de l'œuvre ou sa "
         "corruption »."),
        ("Première station — l'importance du cœur parmi les membres. Le cœur est « "
         "l'émir des organes, celui qui les dirige : ils s'amendent par son amendement "
         "et se corrompent par sa corruption » ; il en va ainsi « des volitions "
         "psychiques et des mouvements du corps » : « si de lui émane une volonté saine, "
         "le corps bouge d'un mouvement sain ; si de lui émane une volonté corrompue, le "
         "corps bouge d'un mouvement corrompu » [Ǧāmiʿ al-ʿulūm wa-l-ḥikam — adapté]. La "
         "hiérarchie des vivants suit : Allah a accordé ce privilège « à l'espèce animale "
         "» — « tu trouves les bêtes percevant par lui leurs intérêts et distinguant "
         "leurs dépenses de leurs profits » — puis « a réservé à l'espèce humaine, en sus "
         "du cœur, la raison (al-ʿaql) »."),
        ("La preuve coranique de la station première : « N'ont-ils donc pas parcouru la "
         "terre, qu'ils aient des cœurs pour comprendre, ou des oreilles pour entendre ? "
         "Ce ne sont pas les yeux qui s'aveuglent, mais ce sont les cœurs dans les "
         "poitrines qui s'aveuglent » (Sourate al-Ḥaǧǧ — la référence imprimée porte le "
         "verset 44 ; le verset qui porte ces paroles est le 46). Allah « a soumis les "
         "organes, obéissants envers lui : ce qui s'y est affermi paraît sur eux, et ils "
         "agissent selon son exigence » — telle est la portée du hadīth lui-même. "
         "L'équation est posée deux fois : « la droiture du cœur est la plus grande des "
         "sources de bien, et sa corruption la plus grande des maux »."),
        ("Seconde station — l'effet du cœur sur la droiture de l'œuvre ou sa corruption. "
         "Le critère est testimonial : « lorsque l'homme accomplit avec ses organes les "
         "actes d'obéissance et œuvre en bien, cela témoigne de la droiture de son cœur ; "
         "et s'il commet les désobéissances et se livre aux actes répréhensibles, cela "
         "témoigne de la corruption de son cœur ». Suit la double liste des savants. Ce "
         "qui amende : « la récitation du noble Coran avec méditation, l'évocation "
         "d'Allah le Très-Haut, la prière, la mention du Prophète — prière et salut "
         "d'Allah sur lui, l'invocation, l'aumône, l'approfondissement de la religion, la "
         "crainte d'Allah et Sa belle surveillance, la veille nocturne, l'imploration aux "
         "dernières heures de la nuit, la piété filiale, la fréquentation des justes, "
         "l'humilité, l'assistance aux funérailles, la visite des tombes » — et le "
         "sommet : « Le plus grand de tout cela : l'acquisition de tout gain licite, et "
         "l'abstention des choses douteuses ». Ce sommet boucle la leçon 10 : le "
         "gardien de la réserve d'Allah est le cœur."),
        ("Ce qui corrompt, en miroir : « le délaissement du noble Coran, la négligence "
         "de l'évocation d'Allah le Très-Haut, l'abandon de la prière, l'ignorance de la "
         "religion, la volubilité du propos et du regard, l'excès de sommeil, de "
         "nourriture et d'étourderie, l'oubli de l'évocation de l'au-delà, et la "
         "commission des désobéissances ». La preuve prophétique est le hadīth de "
         "at-Tirmiḏī, d'après Abū Hurayra — qu'Allah soit satisfait de lui — : « Lorsque "
         "le serviteur commet une faute, une tache noire est inscrite sur son cœur » ; "
         "« s'il se détourne, implore le pardon et se repent, son cœur en est poli » (la "
         "leçon explique le mot suqqa, forme dialectale de “polir”) ; « s'il y "
         "retourne, elle grandit encore, jusqu'à recouvrir le cœur » — « et c'est la rouille "
         "(ar-rān) qu'Allah a mentionnée : “Nullement ! Bien au contraire, leurs cœurs "
         "sont couverts de la rouille de leurs acquisitions” » (Sourate al-Muṭaffifīn — "
         "verset 14) [Sunan at-Tirmiḏī] — la tache s'efface par le pardon, la rouille ne se "
         "détache plus quand la faute s'est répétée."),
        ("Ce qu'il faut retirer du hadīth, en trois : « L'immense effet du cœur sur les "
         "organes, et l'incitation à le corriger » ; « La recherche du gain licite est "
         "une cause de droiture et d'illumination du cœur » ; « La droiture du cœur est "
         "la plus grande des droitures, et sa corruption la plus grande des corruptions "
         "». L'évaluation retourne sur les trois arcs de la leçon : « Pourquoi le cœur "
         "est-il celui qui commande aux organes ? », « Explique l'effet du cœur sur la "
         "droiture de la conduite ou sa corruption », et la question d'assemblage : « "
         "Pourquoi le hadīth a-t-il mentionné le cœur après le licite et l'illicite ? » — "
         "elle invite à relire l'ordre du texte : « Sachez-le : tout roi possède une "
         "réserve » ; « sachez-le : la réserve d'Allah, ce sont Ses interdictions » — et "
         "seulement alors le morceau de chair : le cœur est nommé en dernier parce que "
         "c'est lui le gardien de la réserve."),
        ("L'exploitation relit une seule āya, mais elle est le contrepoids exact du "
         "tamhīd : « Le temps n'est-il pas venu pour ceux qui ont cru, que leurs cœurs "
         "s'humilient à l'évocation d'Allah et devant ce qui est descendu de la vérité ? "
         "Et qu'ils ne soient pas pareils à ceux qui ont reçu le Livre avant eux : le "
         "terme s'étant prolongé, leurs cœurs se sont endurcis, et beaucoup d'entre eux "
         "sont pervers » (Sourate al-Ḥadīd — la référence imprimée porte le verset 15 ; "
         "le verset qui porte ces paroles est le 16). Le commentaire demandé porte sur « "
         "leurs cœurs se sont endurcis » (فَقَسَتْ قُلُوبُهُمْ), et l'exercice en tire la "
         "règle de vie : « Je déduis de l'āya l'effet de la droiture du cœur ou sa "
         "corruption sur la conduite de l'individu » — le cœur qui se durcit se lit sur "
         "la conduite, exactement comme « ce qui s'y est affermi paraît sur eux »."),
        ("La préparation ouvre la leçon suivante : « Je mémorise le hadīth de la leçon "
         "qui vient », « Je recherche la notice biographique de Tamīm ad-Dārī — qu'Allah "
         "soit satisfait de lui », « Je connais la recommandation sincère (an-naṣīḥa) et "
         "j'explique ses types ». La trajectoire du livre est nette : après le cœur "
         "corrigé, la leçon 12 dépliera le septième hadīth des Quarante — la religion "
         "tout entière comme conseil sincère, envers Allah, Son Livre, Son Messager, les "
         "dirigeants des musulmans et leur ensemble."),
    ],
    "points": [
        ("Fil de révision : trois objectifs (familiariser avec la position du cœur ; "
         "mentionner son effet sur la droiture de l'œuvre ; s'employer à corriger son "
         "cœur) → tamhīd (quatre qualifications du cœur + deux questions) → le hadīth "
         "entier avec sa clôture → analyse en deux stations (l'importance ; l'effet sur "
         "l'œuvre) → trois utilités → exploitation (une āya, un commentaire, une "
         "déduction) → préparation (Tamīm ad-Dārī, la naṣīḥa et ses types)."),
        ("La continuité exacte : la préparation de la leçon 10 demandait « J'explique "
         "l'importance du cœur parmi les membres du corps » et « Je précise l'effet du "
         "cœur sur la droiture de l'œuvre ou sur sa corruption » — la leçon 11 les tient "
         "comme ses deux stations, dans le même ordre."),
        ("Les quatre qualifications du tamhīd : « la forteresse de la foi (maḥkamu "
         "al-īmān) », « le lieu du regard du Miséricordieux (maḥallu naẓari ar-Raḥmān) "
         "», « le siège du devoir religieux (manāṭu at-taklīf) », « le lieu de l'honneur "
         "(mawḍiʿu at-tašrīf) » — plus « celui qui est consulté dans la plupart des "
         "questions épineuses »."),
        ("La glose du glossaire, toute la leçon en un mot : al-qalb, maṣdar de « il a "
         "retourné » (qalaba) ; « un organe intérieur, caché dans le corps, dont dépend "
         "la condition de l'homme » ; nommé « en raison de la rapidité des pensées "
         "(ḫawāṭir) qui le traversent et de leur va-et-vient sur lui »."),
        ("La hiérarchie des stations : l'animal perçoit par le cœur « leurs intérêts », "
         "l'homme a « en sus du cœur, la raison (al-ʿaql) » ; « ce qui s'y est affermi "
         "paraît sur eux » ; al-Ḥaǧǧ — référence imprimée 44, verset porteur 46 : « Ce "
         "ne sont pas les yeux qui s'aveuglent, mais ce sont les cœurs dans les poitrines "
         "qui s'aveuglent »."),
        ("Les deux listes symétriques et leur sommet : ce qui amende — récitation avec "
         "méditation, évocation, prière, mention du Prophète, invocation, aumône, "
         "approfondissement de la religion, crainte et belle surveillance, veille "
         "nocturne, imploration aux dernières heures, piété filiale, fréquentation des "
         "justes, humilité, funérailles, visite des tombes — et « Le plus grand de tout "
         "cela : l'acquisition de tout gain licite, et l'abstention des choses "
         "douteuses » ; en miroir, ce qui corrompt, du « délaissement du noble Coran » "
         "à « la commission des désobéissances »."),
        ("Le hadīth de at-Tirmiḏī et son mécanisme : faute → « une tache noire est "
         "inscrite sur son cœur » ; détour, pardon, repentir → « son cœur en est poli » "
         "(suqqa, forme dialectale de “polir”, glose du texte) ; retour → « elle grandit "
         "encore, jusqu'à recouvrir le cœur » → ar-rān, « la rouille (ar-rān) qu'Allah a "
         "mentionnée » (al-Muṭaffifīn 14, correct dans le tirage) [Sunan at-Tirmiḏī]."),
        ("L'exploitation : al-Ḥadīd — référence imprimée 15, verset porteur 16 — « "
         "leurs cœurs se sont endurcis » (فَقَسَتْ قُلُوبُهُمْ) ; la conduite de "
         "l'individu lit l'état du cœur — le contrepoids de « l'incitation à le "
         "corriger »."),
    ],
    "vocabulaire": [
        {"ar": "اصلاح القلب", "translit": "iṣlāḥ al-qalb",
         "fr": "la correction du cœur — titre de la leçon et clôture du sixième hadīth : « Sachez-le : dans le corps il y a un morceau de chair qui, s'il est sain, rend sain tout le corps, et s'il est corrompu, corrompt tout le corps — sachez-le : c'est le cœur » [Ṣaḥīḥ de al-Buḫārī et Muslim]."},
        {"ar": "القلب", "translit": "al-qalb",
         "fr": "le cœur — « à l'origine, nom verbal (maṣdar) de “il a retourné” (qalaba) » ; organe intérieur caché « dont dépend la condition de l'homme »."},
        {"ar": "الخواطر", "translit": "ḫawāṭir",
         "fr": "les pensées qui traversent le cœur — le nom qalb fut donné « en raison de la rapidité des pensées (ḫawāṭir) qui le traversent et de leur va-et-vient sur lui »."},
        {"ar": "اهمية القلب بين اعضاء الجسد", "translit": "ahammiyyat al-qalb bayna aʿḍāʾ al-ǧasad",
         "fr": "l'importance du cœur parmi les membres — première station : « Le cœur est l'émir des organes, celui qui les dirige : ils s'amendent par son amendement et se corrompent par sa corruption » [Ǧāmiʿ al-ʿulūm wa-l-ḥikam — adapté]."},
        {"ar": "اثر القلب في صلاح العمل وفساده", "translit": "aṯar al-qalb fī ṣalāḥ al-ʿamal wa-fasādih",
         "fr": "l'effet du cœur sur la droiture de l'œuvre ou sa corruption — seconde station : les actes d'obéissance — « cela témoigne de la droiture de son cœur » —, les désobéissances — « cela témoigne de la corruption de son cœur »."},
        {"ar": "الران", "translit": "ar-rān",
         "fr": "la rouille — dans le hadīth de at-Tirmiḏī : la tache qui grandit « jusqu'à recouvrir le cœur — et c'est la rouille (ar-rān) qu'Allah a mentionnée : “Nullement ! Bien au contraire, leurs cœurs sont couverts de la rouille de leurs acquisitions” » (al-Muṭaffifīn 14)."},
        {"ar": "التوبة", "translit": "at-tawba",
         "fr": "la repentance — « s'il se détourne, implore le pardon et se repent, son cœur en est poli » ; la leçon explique suqqa, « forme dialectale de “polir” »."},
        {"ar": "فقسنت قلوبهم", "translit": "fa-qasat qulūbuhum",
         "fr": "« leurs cœurs se sont endurcis » — l'āya de l'exploitation (al-Ḥadīd — la référence imprimée porte le verset 15 ; le verset qui porte ces paroles est le 16) : le cœur durci se lit sur la conduite."},
    ],
    "avertissement": "Ce commentaire est un guide de lecture du manuel ; en cas de divergence d'expression, le manuel et sa traduction savante font foi.",
}

E_12 = {
    "auteur": "IA-1, tour R750",
    "resume": ("Guide de lecture de la leçon 12 (la religion, c'est le conseil — ad-dīn "
               "an-naṣīḥa (الدِّينُ النَّصِيحَةُ)) : le septième hadīth des Quarante de "
               "l'imam al-Nawawī, rapporté par Abū Ruqayya Tamīm ibn Aws ad-Dārī — qu'Allah "
               "soit satisfait de lui — : « La religion, c'est le conseil sincère. » Nous "
               "dîmes : « Envers qui, ô Messager d'Allah ? » Il dit : « Envers Allah, envers "
               "Son Livre, envers Son Messager, envers les dirigeants des musulmans et leur "
               "ensemble » [Ṣaḥīḥ de Muslim]. Le tamhīd élargit le mot : le conseil ne se "
               "réduit pas à l'avis rendu à celui qui consulte — il « s'étend jusqu'à "
               "englober la religion tout entière ». L'analyse suit trois stations : le "
               "sens (la pureté exclusive — « j'ai purifié le miel (naṣaḥtu l-ʿasal) »), "
               "l'importance (un mot « englobant » auquel aucun mot isolé de la langue des "
               "Arabes ne suffit), et les cinq "
               "destinataires du conseil, chacun avec sa forme propre. La notice fait "
               "découvrir Tamīm ad-Dārī : converti en l'an neuf avec son frère Nuʿaym, "
               "premier à allumer les lampes de la mosquée, fabricant du minbar du "
               "Prophète, mort en l'an quarante ; et "
               "l'exploitation relit trois āyāt du « sincère conseiller » (al-Aʿrāf — "
               "imprimée 20, porteur 21 et imprimée 78, porteur 79 ; al-Qaṣaṣ — imprimée "
               "19, porteur 20 ; vérifiés web)."),
    "explication": [
        ("La leçon 12 ouvre un nouveau hadīth : après la clôture du sixième — le cœur, "
         "gardien de la réserve d'Allah —, le septième des Quarante déplie un mot unique : "
         "an-naṣīḥa. La leçon répond à la préparation de la leçon 11 : « Je recherche la "
         "notice biographique de Tamīm ad-Dārī — qu'Allah soit satisfait de lui », « Je "
         "connais la recommandation sincère (an-naṣīḥa) et j'explique ses types ». Trois "
         "objectifs : « Que je connaisse la recommandation sincère, son statut juridique "
         "et son rang » ; « Que je distingue à qui s'adresse la recommandation sincère, "
         "et sous quelle forme » ; « Que je m'applique à suivre la Sunna dans le conseil "
         "et la consultation »."),
        ("Le tamhīd commence par défaire un faux réflexe : « On pourrait croire que la "
         "recommandation sincère se réduit au conseil que la personne consultée donne à "
         "celle qui l'a consultée au sujet d'une affaire ; or son sens est plus ample que "
         "cela : elle s'étend jusqu'à englober la religion tout entière ». Le champ se "
         "déplie aussitôt : « Ainsi est-il conseillé dans ses transactions par la fidélité "
         "aux promesses, le respect des contrats et la belle moralité », car « le principe "
         "de la fraternité entre croyants exige le conseil mutuel et l'acceptation du "
         "conseil ». Cinq questions ouvrent le chemin — le sens, "
         "le statut, l'importance, les destinataires, la forme."),
        ("Le texte donne le dialogue entier [Ṣaḥīḥ de Muslim] : « La religion, c'est le "
         "conseil sincère. » Nous dîmes : « Envers qui, ô Messager d'Allah ? » Il dit : « "
         "Envers Allah, envers Son Livre, envers Son Messager, envers les dirigeants des "
         "musulmans et leur ensemble. » La question des Compagnons fait partie du hadīth : "
         "c'est elle qui déplie le mot en cinq destinataires. La notice fait découvrir le transmetteur annoncé par "
         "la préparation : Tamīm ibn Aws ibn Ḫāriǧa ad-Dārī al-Laḫmī — Benū ad-Dār « est "
         "un clan de la tribu Laḫm » — arrivé « auprès du Prophète — prière et salut "
         "d'Allah sur lui — avec son frère Nuʿaym », l'islam embrassé « en l'an neuf de "
         "l'Hégire »."),
        ("La notice tient toutes les promesses de l'iʿdād : « Il fut le premier à allumer "
         "les lampes dans la mosquée » ; « le premier à faire le récit édifiant (qaṣaṣ — "
         "exhorter au moyen des récits des anciens) au temps de ʿUmar — qu'Allah l'agrée "
         "—, dont il fut l'initiateur » ; « il fabriqua le minbar du Prophète — prière et "
         "salut d'Allah sur lui » ; renommé « pour son adoration et sa récitation du "
         "Coran » — « l'ascète (rāhib) des gens de Palestine » ; "
         "« Il mourut en l'an quarante de l'Hégire et fut enterré dans un village des "
         "environs d'al-Ḫalīl, en Palestine ». Et la signature du grand hadīth : « Il ne "
         "rapporte dans le Ṣaḥīḥ de Muslim que ce seul hadīth » — un seul texte, de la "
         "taille de la religion."),
        ("Le glossaire éclaire les deux derniers destinataires : « les dirigeants des "
         "musulmans (aʾimmat al-muslimīn) » — « aʾimma » est le pluriel de « imām », « ce "
         "sont les détenteurs de l'autorité de leurs affaires » — et « l'ensemble des "
         "musulmans (ʿāmmat al-muslimīn) » — « la communauté tout entière ». L'extraction "
         "pose les deux travaux de la leçon : le sens général, puis les destinataires "
         "et la forme."),
        ("Première station — le sens. Au sens linguistique : « la pureté exclusive "
         "(al-ʾiḫlāṣ) ». Le miel en donne l'image : « On dit : “j'ai purifié le miel "
         "(naṣaḥtu l-ʿasal)” quand on l'a débarrassé de sa cire : il y a là purification "
         "et pureté dans la parole et dans l'acte — le conseiller sincère purifie donc sa "
         "parole de la fraude, comme le miel est purifié de sa cire ». Et « “je lui ai "
         "voué un conseil sincère (naṣaḥtu lahu)” : je lui ai réservé une pureté sans "
         "réserve ». Dans l'acception coutumière : « la pureté de l'avis et sa "
         "purification de toute fraude envers celui qui consulte » — « le conseiller sincère veut ainsi que celui qu'il conseille "
         "obtienne tout le bien et se préserve de tout le mal »."),
        ("Seconde station — l'importance. Le mot conseil sincère est « un mot englobant "
         "(ǧāmiʿa) » — et « il n'existe pas, dans la langue des "
         "Arabes, de mot isolé qui suffise à exprimer le sens de ce mot ». La mesure du "
         "mot est donnée par la phrase du hadīth elle-même : « la phrase “La religion, "
         "c'est le conseil sincère” » — « dans le hadīth prophétique, indique l'immense "
         "rang de la recommandation sincère et son importance : elle vaut la religion tout "
         "entière, et la religion se trouve contenue en elle, tant elle est générale et "
         "englobante ». Sa dimension finale : « elle embrasse ce qui est entre le "
         "serviteur et son Seigneur, et ce qui est entre le serviteur et les hommes tous "
         "ensemble » — les deux versants du dīn."),
        ("Troisième station — les cinq destinataires, sous quelle forme se donne le "
         "conseil. Envers Allah : « croire en Lui, à ne rien Lui associer — glorifié soit-"
         "Il —, à Le décrire par les attributs de perfection et de majesté, à Le déclarer "
         "exempt de tout manquement, à Lui obéir et à s'abstenir de Ses interdits, à "
         "aimer et à détester à cause de Lui », « à Lui vouer la pureté exclusive dans "
         "toutes les affaires, et à appeler les gens à tout cela » — et la leçon tourne la direction du regard : "
         "« La recommandation sincère envers Allah revient, en vérité, à un conseil que le "
         "serviteur se donne à lui-même, car Allah peut se passer du conseil des "
         "conseillers »."),
        ("Envers le Livre : « croire qu'il est la parole d'Allah, que rien de la parole "
         "des hommes ne lui ressemble et qu'aucune des créatures n'est capable de produire "
         "son pareil », puis les travaux du lecteur — « l'exalter et le réciter », « le "
         "mémoriser et l'enseigner », « certifier ce qu'il renferme », « s'arrêter à ses "
         "limites et à ses prescriptions », « comprendre ses sciences », « méditer ses "
         "merveilles », « œuvrer selon ses versets catégoriques et croire à ses versets "
         "allégoriques », « appeler les gens à lui et le leur faire aimer ». Envers le "
         "Messager : « croire en sa véracité », « lui obéir dans son ordre et son "
         "interdit », « lui porter secours vivant et mort », « vivifier sa Sunna », "
         "« s'abstenir d'y plonger sans science », « se parer de "
         "ses morales — prière et salut d'Allah sur lui », « suivre son exemple dans sa "
         "conduite, et aimer les membres de sa famille et ses Compagnons »."),
        ("Envers les dirigeants : « leur obéir en dehors de la désobéissance à Allah le "
         "Très-Haut », « les avertir et leur "
         "rappeler avec douceur et ménagement », « s'abstenir de se soulever contre eux », "
         "et « invoquer Allah pour leur droiture » — l'obéissance a sa limite, le rappel a "
         "sa manière. Envers l'ensemble des musulmans — « tous ceux autres que les "
         "détenteurs de l'autorité » : « abaisser l'aile pour eux (humilité) », « voiler "
         "leurs défauts », « s'appliquer à les conseiller en privé, sans dénonciation "
         "publique ni déshonneur », « repousser ce qui leur nuit et à leur attirer ce qui "
         "leur profite », « à souhaiter pour eux le "
         "bien que l'on souhaite pour soi-même, et à détester pour eux le mal que l'on "
         "déteste pour soi-même »."),
        ("Ce qu'il faut retirer du hadīth, en trois : « La recommandation sincère porte "
         "le nom de religion et d'islam » ; « La recommandation sincère est une obligation "
         "pour tout musulman envers son frère musulman, en toute situation, en tout temps "
         "et en tout lieu, dans la mesure de sa capacité » ; « Elle exige d'aimer le bien "
         "pour celui que l'on conseille ; le conseil sincère se donne à lui avec douceur, "
         "ménagement et sagesse ». L'exploitation relit trois āyāt du conseiller sincère : "
         "« Et il leur fit serment : “Oui, je suis pour vous un sincère conseiller.” » "
         "(Sourate al-Aʿrāf — la référence imprimée porte le verset 20 ; le verset qui "
         "porte ces paroles est le 21) ; « Il se détourna d'eux et dit : “Ô mon peuple, je "
         "vous ai bien transmis le message de mon Seigneur, et je vous ai conseillé "
         "sincèrement ; mais vous n'aimez pas les sincères conseillers.” » (Sourate "
         "al-Aʿrāf — la référence imprimée porte le verset 78 ; le verset qui porte ces "
         "paroles est le 79) ; « “…je suis pour toi un sincère conseiller.” » (Sourate "
         "al-Qaṣaṣ — la référence imprimée porte le verset 19 ; le verset qui porte ces "
         "paroles est le 20) — l'exercice demande de nommer le conseiller "
         "sincère dans chacune. La préparation ouvre la leçon 13 : le sens de la "
         "facilité (al-yusr) dans l'islam et certains des effets qui en découlent."),
    ],
    "points": [
        ("Fil de révision : trois objectifs (connaître la naṣīḥa, son statut et son "
         "rang ; distinguer à qui elle s'adresse et sous quelle forme ; suivre la Sunna "
         "dans le conseil et la consultation) → tamhīd (le faux réflexe défait) → le "
         "dialogue du hadīth → trois stations (le sens ; l'importance ; les cinq "
         "destinataires) → trois utilités → exploitation (trois āyāt du conseiller "
         "sincère) → préparation (le yusr dans l'islam — leçon 13). L'évaluation : « Je "
         "définis la recommandation sincère et j'explicite son statut juridique », « Sous "
         "quelle forme la recommandation sincère s'adresse-t-elle à l'ensemble des "
         "musulmans ? »"),
        ("La continuité exacte : la préparation de la leçon 11 demandait « Je recherche "
         "la notice biographique de Tamīm ad-Dārī — qu'Allah soit satisfait de lui » et « "
         "Je connais la recommandation sincère (an-naṣīḥa) et j'explique ses types » — la "
         "leçon 12 les tient : la notice complète et les cinq destinataires comme types "
         "du conseil."),
        ("Le tamhīd contre le rétrécissement du mot : le conseil « se réduit » "
         "peut-être au conseil consultatif, mais « son sens est plus ample que cela : elle s'étend "
         "jusqu'à englober la religion tout entière » ; les transactions en relèvent « par "
         "la fidélité aux promesses, le respect des contrats et la belle moralité » ; « le "
         "principe de la fraternité entre croyants exige le conseil mutuel et "
         "l'acceptation du conseil »."),
        ("La langue du sens : la naṣīḥa est « la pureté exclusive (al-ʾiḫlāṣ) » — « "
         "j'ai purifié le miel (naṣaḥtu l-ʿasal) » de sa cire ; « je lui ai voué un "
         "conseil sincère (naṣaḥtu lahu) » : « une pureté sans réserve » ; « le conseiller "
         "sincère purifie donc sa parole de la fraude, comme le miel est purifié de sa "
         "cire »."),
        ("La mesure du mot : « un mot englobant (ǧāmiʿa) » auquel aucun mot isolé de "
         "la langue des Arabes ne suffit ; « elle vaut la religion tout entière, et la "
         "religion se trouve contenue en elle » ; elle embrasse « ce qui est entre le "
         "serviteur et son Seigneur, et ce qui est entre le serviteur et les hommes tous "
         "ensemble »."),
        ("Les cinq destinataires et la règle d'or : Allah — et « un conseil que le "
         "serviteur se donne à lui-même, car Allah peut se passer du conseil des "
         "conseillers » ; le Livre — « certifier ce qu'il renferme », "
         "« œuvrer selon ses versets catégoriques » ; le Messager — « vivifier sa Sunna "
         "», « aimer les membres de sa famille et ses Compagnons » ; les dirigeants — "
         "« leur obéir en dehors de la désobéissance à Allah » ; l'ensemble — « conseiller "
         "en privé, sans dénonciation publique ni déshonneur »."),
        ("La notice de Tamīm ad-Dārī : Benū ad-Dār, clan de Laḫm ; l'islam « en l'an "
         "neuf de l'Hégire » avec son frère Nuʿaym ; « le premier à allumer les lampes "
         "dans la mosquée » ; « le premier à faire le récit édifiant » au temps "
         "de ʿUmar ; « il fabriqua le minbar du Prophète » ; “l'ascète (rāhib) des gens "
         "de Palestine” ; mort « en l'an quarante » ; « Il ne rapporte dans le Ṣaḥīḥ de "
         "Muslim que ce seul hadīth »."),
        ("Les trois āyāt du conseiller sincère, avec les références imprimées du tirage "
         "et les versets porteurs (vérifiés web) : al-Aʿrāf — imprimée 20, porteur 21 ; "
         "al-Aʿrāf — imprimée 78, porteur 79 (le reproche « mais vous n'aimez pas les "
         "sincères conseillers ») ; al-Qaṣaṣ — imprimée 19, porteur 20. L'exercice : « "
         "j'explicite qui est le conseiller sincère dans chacune d'elles ». La "
         "préparation ouvre le yusr (leçon 13) : « Je mentionne le sens de la facilité "
         "(al-yusr) dans l'islam et certaines de ses manifestations »."),
    ],
    "vocabulaire": [
        {"ar": "الدين النصيحة", "translit": "ad-dīn an-naṣīḥa",
         "fr": "« La religion, c'est le conseil sincère » — le septième hadīth des Quarante, ouvert par le dialogue des Compagnons : « Envers qui, ô Messager d'Allah ? » [Ṣaḥīḥ de Muslim]."},
        {"ar": "النصيحة", "translit": "an-naṣīḥa",
         "fr": "la recommandation sincère — au sens linguistique « la pureté exclusive (al-ʾiḫlāṣ) » : « j'ai purifié le miel (naṣaḥtu l-ʿasal) » quand on l'a débarrassé de sa cire ; « le conseiller sincère purifie donc sa parole de la fraude, comme le miel est purifié de sa cire »."},
        {"ar": "معنى النصيحة", "translit": "maʿnā an-naṣīḥa",
         "fr": "le sens de la recommandation sincère — première station de l'analyse : le sens linguistique (la pureté) et l'acception coutumière (« la pureté de l'avis et sa purification de toute fraude envers celui qui consulte, et le privilège donné à son intérêt »)."},
        {"ar": "لمن النصيحة وبم تكون", "translit": "li-man an-naṣīḥa wa-bi-mā takūn",
         "fr": "à qui s'adresse la recommandation sincère et sous quelle forme — troisième station : cinq destinataires (Allah, Son Livre, Son Messager, les dirigeants des musulmans, l'ensemble des musulmans)."},
        {"ar": "نصيحة كتاب الله", "translit": "naṣīḥat kitāb Allāh",
         "fr": "la recommandation sincère envers le Livre d'Allah — « croire qu'il est la parole d'Allah », « le mémoriser et l'enseigner », « s'arrêter à ses limites et à ses prescriptions », « œuvrer selon ses versets catégoriques et croire à ses versets allégoriques »."},
        {"ar": "نصيحة رسول الله", "translit": "naṣīḥat rasūl Allāh",
         "fr": "la recommandation sincère envers le Messager — « croire en sa véracité », « lui porter secours vivant et mort », « vivifier sa Sunna », « se parer de ses morales », « suivre son exemple dans sa conduite, et aimer les membres de sa famille et ses Compagnons »."},
        {"ar": "ائمة المسلمين", "translit": "aʾimmat al-muslimīn",
         "fr": "les dirigeants des musulmans — « aʾimma » est le pluriel de « imām » ; « ce sont les détenteurs de l'autorité de leurs affaires » ; leur conseil : « leur obéir en dehors de la désobéissance à Allah le Très-Haut », « les avertir et leur rappeler avec douceur et ménagement », « s'abstenir de se soulever contre eux »."},
        {"ar": "القصص", "translit": "qaṣaṣ",
         "fr": "le récit édifiant — Tamīm ad-Dārī fut « le premier à faire le récit édifiant (qaṣaṣ — exhorter au moyen des récits des anciens) au temps de ʿUmar », et « le premier à allumer les lampes dans la mosquée »."},
    ],
    "avertissement": "Ce commentaire est un guide de lecture du manuel ; en cas de divergence d'expression, le manuel et sa traduction savante font foi.",
}


ENTREES = [('pdf-11', E_11), ('pdf-12', E_12)]


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
for DOCID in ('pdf-11', 'pdf-12'):
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

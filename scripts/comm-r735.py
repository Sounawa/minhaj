#!/usr/bin/env python3
"""R735 — ajoute les commentaires pédagogiques des leçons 7-8 de hadith-tanawi-1
(12967 طلاق المملكة — le divorce de la femme investie du commandement
d'elle-même, la douzième du livre ;
12971 أحكام الإيلاء — les dispositions de l'īlāʾ, la treizième du livre)
à content/commentaires/hadith-tanawi-1.json.
Vague 19 : les slots exacts 12967=leçon 7 et 12971=leçon 8 (le SUIVANT de
R734, vérifié dans l'ordre des lessons du registre : 12925, 12934, 12936,
12957, 12959, 12966, puis 12967 et 12971). Même protocole que comm-r734.py
(qui réutilisait comm-r731.py) : normalisation de la ponctuation FR (U+202F
avant ; : ! ? » et après «, apostrophe courbée) sur les entrées nouvelles
seulement — opération idempotente. Rédaction d'après la lecture complète des
deux leçons (htmlFr intégral, 21 640 et 22 676 caractères, extraction non
lossy scripts/extrait-r735.py, couche arabe lue pour les formes du
vocabulaire). Les numéros du Muwaṭṭaʾ (1733, 1735, 1738, 1741, 1745, 1748),
les citations (Ibn ʿUmar, l'homme de Thaqīf, « ta bouche est pierre », Marwān
ibn al-Ḥakam, « ce n'est point divorce », ʿAlī, le vers d'al-Aʿshā, Ibn
al-Mundhir, ash-Shāfiʿī, « Zayd vint, puis ʿAmr », « la parole est la parole
de l'époux », Muwaṭṭaʾ 1748), les statuts et les articles du Code de la
famille (89 et 112) sont cités tels qu'ils figurent dans les leçons (règle 2
de LISEZ-MOI.md : aucune invention). Les formes arabes du vocabulaire sont
posées au squelette standard SANS harakat, reprises de la couche arabe des
leçons ; aucune harakat n'est inventée (règle 2). Les ʿ et ʾ (U+02BF /
U+02BE) sont posés directement dans les champs FR pour les noms propres et
les fragments de translittération — la normalisation ne les touche pas."""
import json, re

CHEMIN = 'content/commentaires/hadith-tanawi-1.json'

E_12967 = {
    "auteur": "IA-1, tour R735",
    "resume": ("Guide de lecture de la leçon 7 (طلاق المملكة) : trois textes du Muwaṭṭaʾ (n° 1733, 1735 et 1738) arment le divorce de la femme "
               "investie du commandement d’elle-même — le transfert (at-tamlīk) par lequel le mari rend à son épouse le commandement d’elle-même, "
               "en sorte qu’elle devient propriétaire de son attache (ʿiṣma). Le n° 1733 — Ibn ʿUmar : « quand un homme investit son épouse du "
               "commandement d’elle-même, le sort est ce qu’elle en décidera — sauf qu’il désavoue sur elle, en disant : “Je n’ai voulu qu’une seule” "
               "— il jure de cela, et il garde sur elle ce qu’elle avait en délai (ʿidda) » — arme la règle du fond : le sort est la décision de "
               "l’investie, contrebalancée par le désaveu juré du mari, qui la borne à la répudiation qu’il a visée. Le n° 1735 — l’homme de Thaqīf : "
               "elle dit « tu es le divorce », il se tut ; elle le répète, il répond « ta bouche est pierre » (bi-fīki al-ḥajr) ; elle le répète "
               "encore, même réponse ; plaidoirie devant Marwān ibn al-Ḥakam, qui le fit jurer — « tu ne lui as donné en investiture que l’unique » "
               "— et il la lui rendit — arme le statut du divorce de l’investie : révocable, contre celui qui fait tomber à elle les trois et celui "
               "qui en fait une seule dissociante ; al-Qāsim ibn Muḥammad « aimait ce jugement et le tenait pour le plus beau qu’il eût entendu en "
               "cela », et Mālik de sceller : « et c’est le plus beau que j’aie entendu en cela, et le plus cher à moi ». Le n° 1738 — Ibn ʿUmar et "
               "Abū Hurayra interrogés ensemble sur l’homme qui investit son épouse et qu’elle lui rend cela sans rien y décider : « ce n’est point "
               "divorce » — arme la règle du rendu : nul divorce ne requiert, ni n’oblige, et de sa part ni acceptation ni retour ne requièrent. "
               "L’analyse déroule la doctrine : le concept — les formules du transfert (« je t’ai déjà investi de ton affaire », « ton affaire est "
               "en ta main », « ton divorce t’appartient », « tu es répudiée si tu veux » — transfert pur, maḥḍ, en le Kitāb d’Ibn al-Mawwāz et chez "
               "Ibn al-Qāsim) ; la durée — le conseil (majlis), au prédominant chez les Mālikites, borné par deux limites : que le mari ne se hâte "
               "pas de se lever, et que l’investie ne dise pas « j’ai accepté » — sinon le transfert persiste jusqu’à décision, ou jusqu’à ce qu’elle "
               "donne à son mari la possibilité de la toucher (son droit tombe), ou jusqu’au juge, qui l’oblige à déclarer sa position et n’accorde "
               "point de délai, fût le mari lui-même la durée de l’investiture (« ton affaire est en ta main pour une année ») ; le conseil prolongé "
               "au-delà de l’usage — deux dires : la Mudawwana (la majeure partie du jour, et la sortie connue — annulé) contre Ashhab (en sa main "
               "tant qu’ils demeurent au conseil) ; la formule « j’ai répudié moi-même » (ṭallaqtu nafsī) — le divorce oblige, mais l’interrogatoire "
               "diverge : le mashhūr l’interroge de crainte qu’elle ne revendique plus d’une seule — qu’on la désavoue ou qu’on passe ; Ibn al-Qāsim "
               "ne l’interroge point — elle est une seule en l’investiture, et revendiquer davantage serait « reprendre une revendication » ; le "
               "transfert avec contrepartie — « je suis libérée de toi » (bariʾtu minka) : une seule, car c’est le khulʿ, semblable à la "
               "non-consommée ; au remariage, on la fait jurer « je ne t’ai investi de ton affaire que d’une seule » (le Mabsūṭ) — dissociante à "
               "cause de la contrepartie ; l’investiture de la non-astreinte — si elle a raisonné l’investiture, c’est un divorce quand elle atteint "
               "le degré du coït (Ibn al-Qāsim) ou un degré où elle connaît ce qu’on lui a donné (ʿĪsā) ; ʿAbd al-Malik et Saḥnūn : de même s’il met "
               "le commandement d’elle en la main d’un garçon ; révocable ou dissociant — Mālik et ash-Shāfiʿī : révocable (le divorce vise toujours "
               "le sunnī ; le silence à la première, le désaveu quand elle dépasse, Marwān qui la lui rend), Abū Ḥanīfa : dissociant — sinon le "
               "divorce de l’investie serait « vide de l’utilité qu’elle avait visée en demandant l’investiture et en choisissant le divorce » ; la "
               "contravention du mari — la visée borne : s’il a visé une seule ou deux, elle décide selon sa visée ; si elle en fait tomber trois "
               "alors qu’il avait visé une seule, une seule l’oblige (Mālik, Ibn ʿUmar — « car il lui est loisible de la désavouer »), contre ʿAlī "
               "et Saʿīd ibn al-Musayyab (le sort selon ce qu’elle a décidé, le désaveu ne profite point) — les Mālikites répondent : elle n’a cela "
               "en sa main que par le don du mari, et il lui a donné une seule répudiation, non davantage ; la divergence après le conseil — la "
               "parole est à l’épouse tant qu’il la reconnaît investie, édifié sur ce qu’elle n’a point de choix après le conseil, « comme "
               "l’étranger à qui l’on délègue le divorce, puis qui revendique n’avoir point répudié » (la Mudawwana, d’après la narration d’Ibn "
               "al-Qāsim). L’exploitation imprime l’article 89 du Code de la famille : la femme investie use de son droit par la voie d’une demande "
               "déposée devant le tribunal (articles 79-80), qui vérifie les conditions du transfert convenues entre les époux et s’efforce de les "
               "réconcilier (articles 81-82) — le droit marocain requiert l’intervention judiciaire là où le fiqh classique tenait le divorce du "
               "transfert pour tombé par le seul acte de l’épouse."),
    "explication": [
        ("La leçon 7 (la douzième du livre) traite le divorce de la femme investie du commandement d’elle-même "
         "(ṭalāq al-mumallaka) — l’application du transfert (at-tamlīk) au divorce. Le préambule enracine le tout : "
         "le mari est le premier responsable de la famille en l’entretien et le logement, et la Loi islamique a mis le "
         "divorce en sa main — pour autant qu’il n’inflige point de détriment à l’épouse ; mais s’il veut délaisser ce "
         "droit au profit de son épouse, il en a la faculté : « par cela, l’épouse devient propriétaire de son propre "
         "sort ». Le transfert est ainsi posé comme l’exception qui confie à l’épouse ce que la loi confie d’ordinaire "
         "au mari — et la leçon en tire ses trois objectifs : reconnaître le concept du transfert et sa durée, "
         "distinguer le transfert avec contrepartie du transfert sans contrepartie, saisir la sagesse du transfert."),
        ("Les trois hadiths arment les trois règles du fond. Le n° 1733 — la voie va de Nāfiʿ à Ibn ʿUmar — pose le "
         "principe et sa borne : le sort est ce qu’elle en décidera, « sauf qu’il désavoue sur elle » — et le désaveu "
         "est juré (« je n’ai voulu qu’une seule »), tandis que le mari garde sur elle ce qu’elle avait en délai : la "
         "révocabilité affleure dès le principe. Le n° 1735 — la voie va d’ʿAbd ar-Raḥmān ibn al-Qāsim — le fils — "
         "d’après son père al-Qāsim ibn Muḥammad ibn Abī Bakr, l’arrière-petit-fils du calife, compté parmi les sept "
         "juristes de Médine — : le récit de l’homme de Thaqīf donne à la règle son visage vivant — le silence à la "
         "première, « ta bouche est pierre » à la deuxième et à la troisième, puis la plaidoirie devant Marwān ibn "
         "al-Ḥakam, gouverneur umayyade de Médine : il le fit jurer — « tu ne lui as donné en investiture que "
         "l’unique » — et il la lui rendit ; le double éloge — al-Qāsim l’aimait et le tenait pour le plus beau qu’il "
         "eût entendu, Mālik : « et c’est le plus beau que j’aie entendu en cela, et le plus cher à moi » — scelle le "
         "jugement. Le n° 1738 — Ibn ʿUmar et Abū Hurayra interrogés ensemble — règle le rendu : « ce n’est point "
         "divorce »."),
        ("Le concept répond à la première question. « il investit » (mallaka) : du transfert — rendre une chose "
         "propriété d’autrui, en sorte qu’il en fasse ce qu’il veut ; le visé ici : rendre à l’épouse le commandement "
         "d’elle-même, en sorte qu’elle devient propriétaire de son attache (ʿiṣma). Les formules sont recueillies par "
         "l’école : « je t’ai déjà investi de ton affaire », ou « ton affaire est en ta main » ; en le Kitāb d’Ibn "
         "al-Mawwāz — de même « je t’ai déjà investie », s’il ne dit point « ton affaire » ni « toi-même » ; de même "
         "« ton divorce t’appartient » ou « en ta main » ; Ibn al-Qāsim ajoute « ton affaire est en ta main, si tu "
         "veux » et « tu es répudiée si tu veux » — tout cela est transfert pur (maḥḍ). Le transfert est ainsi une "
         "formule parmi les formules par lesquelles le divorce tombe, si la femme l’accepte et le fait tomber."),
        ("La durée répond à la suite. Le prédominant chez les Mālikites : la durée du transfert est la durée du "
         "maintien des deux époux au conseil — la sortie du conseil, sans qu’elle y ait rien décidé qui annule son "
         "droit, ne l’annule pas. Deux bornes l’encadrent : que le mari ne se hâte pas de se lever de ce conseil — "
         "sinon le droit lui demeure durant le temps où il lui est possible de décider ce qu’elle voudra ; et que "
         "l’investie ne dise pas, au moment du transfert, « j’ai accepté » ou « j’en suis satisfaite » ou autre chose "
         "dénotant qu’elle répondra à son mari — sinon ce transfert lui demeure jusqu’à ce qu’elle décide ce qu’elle "
         "voudra, ou jusqu’à ce qu’elle donne à son mari la possibilité de la toucher : son droit tombe alors — ou "
         "jusqu’à ce que l’affaire soit portée au juge : il l’oblige alors à déclarer sa position, sinon il juge la "
         "chute de son droit — « et le juge ne lui accorde point de délai, fût le mari lui-même la durée de "
         "l’investiture : comme s’il lui avait dit : ton affaire est en ta main pour une année »."),
        ("Le conseil prolongé au-delà de l’usage ouvre deux dires. L’un — en la Mudawwana, de Mālik : si le conseil a "
         "duré la majeure partie du jour, et que l’on sache qu’ils ont quitté cela et sont sortis de ce qu’ils étaient "
         "en vers autre chose — le transfert est annulé. L’autre — Ashhab : cela est en sa main tant qu’ils demeurent "
         "au conseil. Le visage du premier : le conseil de l’offre, et la prise en une telle chose, est chose "
         "coutumière ; si le conseil se prolonge d’une augmentation manifeste, par laquelle on sait la sortie de cette "
         "affaire et l’abandon de son examen, ce qui lui revient d’acceptation s’annule — comme si elle s’était levée "
         "du conseil. Le visage de la seconde : ce dont Ashhab s’est fondé — le hadith d’Ibn ʿUmar : cela lui est "
         "donné tant qu’ils demeurent au conseil ; et le conseil, fût-il long, elle n’a point quitté la condition où "
         "l’expectative fut rendue licite — « et il se peut que ce regard et cette expectative aient besoin de plus "
         "que le montant du conseil coutumier »."),
        ("Les dispositions de la formule arment le corps doctrinal. Si l’investie dit « j’ai répudié moi-même » "
         "(ṭallaqtu nafsī), le divorce oblige — mais l’interroge-t-on d’abord sur ce qu’elle a voulu ? Le mashhūr de "
         "l’école : oui — de crainte qu’elle ne revendique plus d’une seule, et qu’on la désavoue, ou qu’on passe. "
         "Rapporté d’Ibn al-Qāsim : non — elle est une seule en l’investiture ; car le mot est souvent employé pour la "
         "répudiation unique : quand elle prononce ce mot qu’on emploie généralement pour l’unique, sa revendication "
         "d’en avoir voulu davantage n’est pas acceptée — « ce serait reprendre une revendication, comme si elle "
         "disait : je me suis répudiée une seule, puis disait : j’en ai voulu davantage, et j’en veux davantage "
         "maintenant ». Le transfert avec contrepartie (le Mabsūṭ) : si elle lui dit « je suis libérée de toi » "
         "(bariʾtu minka), c’est une seule — car c’est le khulʿ, et elle est semblable à celle avec qui il n’a pas "
         "consommé ; s’il veut l’épouser d’un nouveau mariage, on la fait jurer par Allah : « je ne t’ai investi de "
         "ton affaire que d’une seule » — le sens : il l’a investie d’un mot qui porte l’ambiguïté, puis l’a "
         "désavouée — elle est donc dissociante à cause de la contrepartie. Et l’investiture de la non-astreinte : si "
         "elle a raisonné l’investiture — en la Muwāziyya, Mālik au sujet de qui donne le choix à son épouse avant "
         "qu’elle ait atteint [l’âge] et avant la consommation, et elle a choisi elle-même : c’est un divorce ; Ibn "
         "al-Qāsim : « quand elle atteint le degré du coït » ; ʿĪsā : « quand elle atteint un degré où elle connaît ce "
         "qu’on lui a donné » ; ʿAbd al-Malik et Saḥnūn : de même s’il met le commandement d’elle en la main d’un "
         "garçon."),
        ("Le statut du divorce de l’investie divise : Mālik et ash-Shāfiʿī — révocable, au mari de la reprendre "
         "pendant son délai si elle n’est point la troisième ; car le divorce vise toujours le divorce sunnī — et le "
         "hadith le dénote : quand l’investie dit « tu es le divorce », il se tut — et il ne se tut qu’à la première, "
         "parce que son investiture la requiert ; quand elle dépassa ce qu’il tenait du divorce, il la désavoua ; "
         "« ta bouche est pierre » à la troisième est aussi un désaveu ; Marwān le fit jurer et la lui rendit — elle "
         "était révocable, il lui permit de la reprendre : elle est donc chez lui selon ce qui lui restait de "
         "répudiations — contre le dire de celui qui fait tomber à elle les trois, et le dire de celui qui en fait "
         "une seule dissociante. Abū Ḥanīfa — dissociant : « car le voulu de la femme s’accomplit par cela » ; s’il "
         "était révocable, son divorce serait vide de l’utilité qu’elle avait visée. La contravention du mari : s’il "
         "a visé une seule ou deux, elle décide selon sa visée — cela l’oblige et ne l’oblige point au-delà ; si elle "
         "en fait tomber trois alors qu’il n’avait visé qu’une seule — une seule l’oblige (Mālik, Ibn ʿUmar) — contre "
         "ʿAlī ibn Abī Ṭālib et Saʿīd ibn al-Musayyab (le sort selon ce qu’elle a décidé, le désaveu ne profite "
         "point) : les Mālikites répondent qu’elle n’a cela en sa main que par le don du mari — « et il lui a donné "
         "une seule répudiation, non davantage : elle n’avait donc point à en faire tomber plus ». La divergence après "
         "le conseil : la parole est le dire de l’épouse tant qu’il la reconnaît investie — édifié sur ce qu’elle n’a "
         "point de choix après le conseil — « comme l’étranger à qui l’on délègue le divorce, puis qui revendique "
         "n’avoir point répudié ». Le rendu de l’investiture : nul divorce ne requiert, ni n’oblige — et il faut "
         "ensuite qu’on l’interroge, elle ; de sa part, ni acceptation ni retour ne requièrent."),
        ("L’évaluation retourne au fil : définir le transfert et sa durée ; éclaircir le fondement de Mālik — la "
         "femme investie n’a qu’une seule répudiation quand ils divergent ; donner la règle du rendu. L’exploitation "
         "imprime l’article 89 du Code de la famille : « si le mari investit son épouse du droit de faire tomber le "
         "divorce, elle a la faculté d’user de ce droit par la voie d’une demande déposée devant le tribunal, "
         "conformément aux dispositions des articles 79 et 80. Le tribunal vérifie la présence des conditions du "
         "transfert convenues entre les époux, et s’efforce de les réconcilier conformément aux dispositions des "
         "articles 81 et 82 » — la demande, la vérification des conditions, la réconciliation : le droit marocain "
         "requiert ainsi l’intervention judiciaire là où le fiqh classique tenait le divorce du transfert pour tombé "
         "par le seul acte de l’épouse — une des articulations du Code entre la doctrine mālikite et l’ordre public "
         "contemporain, comme en l’article 112 pour l’īlāʾ (la leçon suivante). La préparation préalable annonce "
         "celle-ci : expliquer l’īlāʾ — « il suspend » (yūqaf), « il réintègre » (yafīʾ) — et déduire la règle du "
         "retour dans l’īlāʾ."),
    ],
    "points": [
        ("Fil de révision : trois objectifs (concept et durée du transfert ; avec contrepartie / sans contrepartie ; "
         "sagesse du transfert) → préambule (le mari premier responsable en l’entretien et le logement ; le divorce "
         "en sa main sans détriment à l’épouse ; le délaissement du droit au profit de l’épouse — « l’épouse devient "
         "propriétaire de son propre sort »)."),
        ("Le concept : « il investit » (mallaka) — rendre une chose propriété d’autrui en sorte qu’il en fasse ce "
         "qu’il veut ; ici : rendre à l’épouse le commandement d’elle-même — elle devient propriétaire de son attache "
         "(ʿiṣma) ; formules (« je t’ai déjà investi de ton affaire » / « ton affaire est en ta main » / « ton divorce "
         "t’appartient » / « tu es répudiée si tu veux » — transfert pur, maḥḍ : le Kitāb d’Ibn al-Mawwāz, Ibn "
         "al-Qāsim)."),
        ("La durée : le prédominant — la durée du maintien des deux époux au conseil ; deux bornes (le mari ne se "
         "hâte pas de se lever ; « j’ai accepté » → jusqu’à décision, ou possibilité de toucher — chute du droit, ou "
         "juge — déclaration obligée, nul délai : « fût le mari lui-même la durée de l’investiture », « ton affaire "
         "est en ta main pour une année »)."),
        ("Le conseil prolongé : deux dires — la Mudawwana (la majeure partie du jour et la sortie connue → annulé ; "
         "le visage : le conseil de l’offre est coutumier — la prolongation manifeste = « comme si elle s’était levée "
         "du conseil ») contre Ashhab (en sa main tant qu’ils demeurent ; le visage : le hadith d’Ibn ʿUmar — "
         "l’expectative « peut avoir besoin de plus que le montant du conseil coutumier »)."),
        ("« j’ai répudié moi-même » (ṭallaqtu nafsī) : le divorce oblige ; l’interrogatoire diverge — le mashhūr "
         "interroge (crainte de la revendication au-delà de l’unique ; désaveu ou passe) ; Ibn al-Qāsim non — elle "
         "est une seule en l’investiture : revendiquer davantage serait « reprendre une revendication »."),
        ("La contrepartie : « je suis libérée de toi » (bariʾtu minka) — une seule ; le khulʿ ; semblable à la "
         "non-consommée ; serment au remariage (« je ne t’ai investi de ton affaire que d’une seule » — le Mabsūṭ) : "
         "mot ambigu puis désavoué → dissociante à cause de la contrepartie."),
        ("La non-astreinte : si elle a raisonné l’investiture — divorce quand elle atteint le degré du coït (Ibn "
         "al-Qāsim) ou un degré où elle connaît ce qu’on lui a donné (ʿĪsā) ; le garçon auquel on met le commandement "
         "d’elle en la main — de même (ʿAbd al-Malik, Saḥnūn ; la Muwāziyya)."),
        ("Révocable ou dissociant : Mālik et ash-Shāfiʿī — révocable (le divorce vise toujours le sunnī ; le silence "
         "à la première, le désaveu quand elle dépasse, Marwān qui la rend — l’éloge d’al-Qāsim et de Mālik) ; Abū "
         "Ḥanīfa — dissociant (« le voulu de la femme s’accomplit par cela » — sinon vide de l’utilité visée)."),
        ("La contravention : la visée borne (une seule ou deux — elle décide selon la visée ; trois tombées contre "
         "une visée d’une seule — une seule l’oblige : Mālik, Ibn ʿUmar) contre ʿAlī et Saʿīd ibn al-Musayyab (le "
         "sort selon sa décision, désaveu ne profite point) — réponse des Mālikites (le don du mari — « une seule "
         "répudiation, non davantage ») ; la divergence post-conseil — la parole à l’épouse tant qu’il reconnaît "
         "l’investiture (analogie de l’étranger délégué) ; le rendu — « ce n’est point divorce » (Ibn ʿUmar, Abū "
         "Hurayra), ni acceptation ni retour ne requièrent d’elle."),
        ("L’exploitation (article 89) : la demande déposée devant le tribunal (79-80), la vérification des "
         "conditions convenues entre les époux, la réconciliation (81-82) — la voie judiciaire là où le fiqh tenait "
         "le divorce tombé par le seul acte de l’épouse ; la préparation annonce l’īlāʾ (yūqaf — yafīʾ)."),
    ],
    "vocabulaire": [
        {"ar": "طلاق المملكة", "translit": "ṭalāq al-mumallaka",
         "fr": "le divorce de la femme investie du commandement d’elle-même — l’application du transfert au divorce : elle fait tomber par son mot ce que le mari lui a donné de son propre droit"},
        {"ar": "التمليك", "translit": "at-tamlīk",
         "fr": "le transfert — rendre une chose propriété d’autrui en sorte qu’il en fasse ce qu’il veut ; ici : rendre à l’épouse le commandement d’elle-même, en sorte qu’elle devient propriétaire de son attache (ʿiṣma)"},
        {"ar": "بفيك الحجر", "translit": "bi-fīki al-ḥajr",
         "fr": "« ta bouche est pierre » — trois sens chez al-Zarqānī : la déconvenue de l’invocateur, à qui l’on ne note de sa demande que les pierres ; la perdition de celui à qui on la dit ; la colère impuissante — dans le récit, le démenti du mari : tu n’as que l’unique que je t’ai donnée"},
        {"ar": "طلقت نفسي", "translit": "ṭallaqtu nafsī",
         "fr": "« j’ai répudié moi-même » — la formule par laquelle l’investie fait tomber le divorce ; le mashhūr l’interroge sur ce qu’elle a voulu, Ibn al-Qāsim non — elle est une seule en l’investiture"},
        {"ar": "برئت منك", "translit": "bariʾtu minka",
         "fr": "« je suis libérée de toi » — la formule du transfert avec contrepartie : le khulʿ, une seule, semblable à la non-consommée — dissociante à cause de la contrepartie (le Mabsūṭ)"},
        {"ar": "مجلس التعارض", "translit": "majlis al-muʿāraḍ",
         "fr": "le conseil de l’offre — où le mari investit son épouse ; la durée du transfert est, au prédominant, la durée du maintien des deux époux au conseil"},
        {"ar": "تمليك محض", "translit": "tamlīk maḥḍ",
         "fr": "le transfert pur — les formules dénuées de condition : « ton affaire est en ta main, si tu veux », « tu es répudiée si tu veux » (Ibn al-Qāsim)"},
        {"ar": "مدونة الأسرة", "translit": "Mudawwanat al-usra",
         "fr": "le Code de la famille (Maroc, 2004) — l’article 89 codifie le transfert : demande déposée devant le tribunal (articles 79-80), vérification des conditions convenues entre les époux, réconciliation (articles 81-82)"},
    ],
    "avertissement": "Ce commentaire est un guide de lecture du manuel ; en cas de divergence d’expression, le manuel et sa traduction savante font foi.",
}

E_12971 = {
    "auteur": "IA-1, tour R735",
    "resume": ("Guide de lecture de la leçon 8 (أحكام الإيلاء) : deux textes du Muwaṭṭaʾ (n° 1741 et 1745) et un texte "
               "d’exploitation (n° 1748) arment l’īlāʾ — le vœu d’abstention de l’époux. Le n° 1741 — la chaîne va à ʿAlī ibn Abī "
               "Ṭālib par Jaʿfar ibn Muḥammad et son père, la voie médine du lignage du Prophète — paix et bénédiction sur lui — : "
               "« quand un homme fait vœu d’abstention (ālā) de son épouse, nul divorce ne tombe sur lui ; et si les quatre mois "
               "s’écoulent jusqu’à ce qu’il soit suspendu (yūqaf), alors, ou il répudie, ou il réintègre (yafīʾ) » — et Mālik de "
               "sceller : « et telle est l’affaire chez nous » — arme la portée du verset (2:226-227) : l’attente de quatre mois, la "
               "réintégration et la résolution sur le divorce y tiennent ensemble — le divorce ne tombe pas par le seul écoulement, "
               "mais au choix, après la suspension devant le gouverneur. Le n° 1745 — le dire compilé de Mālik lui-même : l’homme "
               "suspendu qui répudie à l’expiration des quatre mois puis reprend son épouse — s’il ne la touche pas jusqu’à ce que "
               "son délai s’achève, « il n’a point d’accès à elle, ni de retour sur elle — sauf s’il a une excuse de maladie, ou de "
               "prison, ou quelque chose de semblable parmi les excuses : alors sa reprise d’elle est établie sur elle » ; et si son "
               "délai s’écoule puis qu’il l’épouse : s’il ne la touche pas jusqu’à l’expiration des quatre mois, il est suspendu "
               "aussi ; s’il ne réintègre pas, le divorce tombe par le premier vœu d’abstention — « et il n’a point de retour sur "
               "elle ; car il l’a épousée, puis l’a répudiée avant de la toucher : il n’y a donc point de délai sur elle, ni de "
               "retour » — arme la condition de validité du retour dans l’īlāʾ : le coït dans le délai, sauf excuse. L’analyse "
               "déroule la doctrine : le concept — en langue le serment, d’origine l’abstention d’une chose, spécialisé quand "
               "l’abstention a pour cause le serment — le vers d’al-Aʿshā (« je jurai : je ne servirai point pour elle d’héritier "
               "d’une kalāla, ni d’un orphelin, jusqu’à ce que tu rencontres Muḥammad ») montre l’usage ancien ; en terme : le "
               "serment de l’époux astreint, capable du coït à l’habitude, de s’abstenir du coït avec sa femme une durée excédant "
               "quatre mois, avec la visée de la nuire ; la durée — la Jāhiliyya laissait l’épouse « suspendue, distraite, non "
               "répudiée et non épouse, tandis que lui-même en épousait une autre », le Coran a mis une borne : la majorité — plus "
               "de quatre mois ; les ḥanafites — le minimum quatre mois ; ʿIyāḍ : nul désaccord que le divorce ne tombe point avant "
               "les quatre mois, et qu’il tombe si l’âme viole le serment avant leur achèvement ; à l’écoulement — les Kufiens : le "
               "divorce tombe ; le reçu de Mālik et de ses compagnons (al-kāffa) : il ne tombe point par l’écoulement, mais quand le "
               "gouverneur le suspend — la portée du verset : « s’ils réintègrent durant elles » (Kufiens) / « après elles » "
               "(majorité), ce à quoi ʿAlī a fait allusion dans le hadith de la leçon ; l’article 112 du Code de la famille codifie : "
               "l’épouse porte son affaire devant le tribunal, qui accorde un délai de quatre mois, puis prononce la répudiation à "
               "défaut de réintégration ; la synthèse — la divergence remonte au fīʾ : la réintégration avant l’écoulement "
               "(ḥanafites — la durée est de quatre mois) ou après (majorité — elle excède quatre mois) ; le statut après "
               "l’expiration — Abū Ḥanīfa et les Kufiens : à l’écoulement des quatre mois, un divorce unique avec retour tant qu’elle "
               "est dans son délai (avec eux Ibn Shihāb, concordant l’avis de son maître Ibn al-Musayyab) ; la majorité avec Ibn "
               "al-Mundhir : « nous n’avons rien trouvé en quelque preuve que la résolution sur le divorce soit un divorce — et si "
               "cela était permis, la résolution sur la réintégration serait une réintégration, et nul ne le dit » — et la "
               "coordination par la fāʾ dénote que le choix est après l’écoulement ; ash-Shāfiʿī : le sens apparent du Livre — "
               "quatre mois pour terme, puis deux statuts : réintégrer ou répudier ; certains ḥanafites répondent : la fāʾ produit "
               "la suite mémorielle (adh-dhikrī), non la suite réelle — « Zayd vint, puis ʿAmr » — chacun des deux ordres est permis "
               "en le verset ; la condition du retour — Mālik : la reprise licite à condition de la toucher avant l’expiration de "
               "son délai, sauf excuse (maladie, prison) ; si l’excuse disparaît, qu’on lui en facilite l’accès et qu’il refuse le "
               "coït — deux cas selon que le délai s’était écoulé ou non (la Mudawwana et le Mabsūṭ ; ʿAbd al-Malik : dissociante "
               "dès le jour où le délai s’est écoulé) ; l’argument des Mālikites : il n’avait répudié que pour son abstention du "
               "coït alors que l’īlāʾ persistait — si cela annule le mariage validement établi, « empêcher la validité du retour "
               "est plus digne encore » ; la divergence « je l’ai touchée » / « il ne l’a point touchée » — « la parole est la "
               "parole de l’époux », comme celui qui s’y oppose ; et le second mariage : suspendu à nouveau, divorce par le premier "
               "vœu d’abstention, point de délai ni de retour (33:49) ; ash-Shāfiʿī : sa reprise est valide, fût-ce sans qu’il ne la "
               "touche. L’exploitation imprime le n° 1748 : qui jure de ne point toucher sa femme un jour ou un mois, puis demeure "
               "jusqu’à ce que plus de quatre mois s’écoulent — cela n’est point īlāʾ : « ne fait l’objet de la suspension dans "
               "l’īlāʾ que celui qui jure au-delà de quatre mois », car « quand arrive le terme auprès duquel on suspend, il sort de "
               "son serment — et il n’y a point de suspension sur lui » — le serment borné se dissout de soi à son terme, la "
               "suspension requiert un serment sans borne."),
    "explication": [
        ("La leçon 8 (la treizième du livre) traite les dispositions de l’īlāʾ — le vœu d’abstention. Le préambule "
         "enracine : parmi les droits réciproques des deux époux, le droit de la cohabitation — il est du devoir de "
         "chacun de œuvrer à la satisfaction de l’autre et de le rendre capable d’atteindre son désir dans l’union "
         "charnelle ; l’abstention de l’un des deux époux du coït avec l’autre est donc une espèce de nuisance faite "
         "à celui-ci ; le Coran noble a nommé l’abstention de la femme la rébellion (nushūz), comme il a nommé "
         "l’abstention de l’homme accompagnée de serment l’īlāʾ — « pour ceux qui font le serment de se priver de "
         "leurs femmes, il y a un délai d’attente de quatre mois. Et s’ils reviennent (de leur serment), celui-ci "
         "sera annulé, car Allah est certes Pardonneur et Miséricordieux ! Mais s’ils se décident au divorce, "
         "(celui-ci devient exécutoire), car Allah est certes Audient et Omniscient » (2:226-227). Le verset est "
         "reproduit en image dans le manuel et restauré verbatim au cache coranique : l’imprimé porte « la sourate "
         "(2) : 224-225 » — l’écart d’étiquetage de la série al-Baqara, 41ᵉ écart cumulé du registre des versets ; "
         "les versets imprimés « 224-225 » traitent, eux, du serment en général, nullement du vœu d’abstention. "
         "Trois objectifs : reconnaître le concept de l’īlāʾ et sa durée, déduire ses dispositions et ses "
         "conditions, saisir les enseignements du Coran et de la Sunna en l’īlāʾ."),
        ("Les deux hadiths arment les deux règles du fond. Le n° 1741 — la chaîne va à ʿAlī ibn Abī Ṭālib par Jaʿfar "
         "ibn Muḥammad (aṣ-Ṣādiq) et son père Muḥammad (al-Bāqir), la voie médine du lignage du Prophète — paix et "
         "bénédiction sur lui — : nul divorce sur l’ālā ; si les quatre mois s’écoulent « jusqu’à ce qu’il soit "
         "suspendu (yūqaf) », alors, ou il répudie, ou il réintègre (yafīʾ) — et Mālik : « et telle est l’affaire "
         "chez nous » : la décision d’ʿAlī est le madhab même. Le n° 1745 — le dire compilé de Mālik, qui recueille "
         "l’école sur la question — : le suspendu qui répudie à l’expiration des quatre mois puis reprend son "
         "épouse ; la condition du coït dans le délai, les excuses (maladie, prison), le second mariage et la "
         "répétition du cycle, le divorce par le premier vœu d’abstention, nul délai ni retour. Le « suspendu » est "
         "retenu devant le gouverneur, qui le contraint de réintégrer le foyer conjugal ou de répudier : tel est "
         "l’office de la suspension (al-waqf) en l’école — la borne du verset exécutée par l’autorité."),
        ("Le concept répond à la première question. En langue : le serment — et son origine est l’abstention d’une "
         "chose ; on dit « il a fait serment » (ālaitu), « il fait serment » (ʿūlī), « un vœu d’abstention » (īlāʾ) "
         "et « une abstention » (īlā) ; puis le mot fut employé lorsque l’abstention a pour cause le serment : on "
         "rattacha le serment à l’abstention, et l’īlāʾ devint le serment. Al-Aʿshā — Maymūn ibn Qays, mort vers "
         "7/629, le poète mukhaḍram, contemporain du Prophète, qui le loua après l’avoir rencontré — a dit dans la "
         "qasīda par laquelle il le loua : « je jurai : je ne servirai point pour elle d’héritier d’une kalāla, ni "
         "d’un orphelin, jusqu’à ce que tu rencontres Muḥammad — un prophète qui voit ce que ne voient point [les "
         "hommes] » — la kalāla est la succession du défunt sans ascendant ni descendant directs ; le « je jurai » "
         "(fa-ālaitu) dans le vers signifie « j’ai juré » — l’usage linguistique ancien de ālā pour le serment "
         "quelconque, avant la spécialisation juridique du terme. En terme : le serment de l’époux astreint, capable "
         "du coït à l’habitude, de s’abstenir du coït avec sa femme une durée excédant quatre mois, avec la visée de "
         "la nuire — la définition aligne cinq éléments : l’astreinte, la capacité, l’abstention, la durée, la "
         "visée."),
        ("La durée arme la seconde. En la Jāhiliyya, quand l’homme détestait sa femme et voulait la nuire, il jurait "
         "de ne plus l’approcher — et il la laissait « suspendue, distraite, non répudiée et non épouse, tandis que "
         "lui-même en épousait une autre » ; le Coran a mis une borne à ce que faisaient les gens en la Jāhiliyya : "
         "la majorité — l’époux jure de ne point coïter avec sa femme au-delà de quatre mois ; les ḥanafites — le "
         "minimum de la durée est quatre mois, fût-ce davantage ; s’il jure sur trois mois ou sur quatre, il n’est "
         "point fait vœu d’abstention chez la majorité. ʿIyāḍ — al-Qāḍī ʿIyāḍ, mort 544/1149, l’imam mālikite de "
         "Sabta, auteur de l’Ikmāl sur Muslim et des Tanbīhāt sur les questions divergées de l’école — : nul "
         "désaccord que le divorce ne tombe point avant les quatre mois, et qu’il tombe si son âme viole le serment "
         "avant leur achèvement. À l’écoulement : les Kufiens — l’école d’Abū Ḥanīfa en Kūfa — disent que le divorce "
         "tombe, et il en est rapporté de même de Mālik ; mais le reçu de lui et de ses compagnons — l’avis de la "
         "totalité (al-kāffa), l’équivalent du jumhūr des savants — est qu’il ne tombe point par leur écoulement, "
         "mais seulement quand le gouverneur le suspend : alors il réintègre, ou l’on répudie sur lui. La portée du "
         "verset : « s’ils réintègrent durant elles » chez les Kufiens, « s’ils réintègrent après elles » chez la "
         "majorité — et c’est ce à quoi ʿAlī a fait allusion dans le hadith de la leçon. L’article 112 du Code de la "
         "famille stipule en propre : « si l’époux fait vœu d’abstention de son épouse, ou l’abandonne, l’épouse a la "
         "faculté de porter son affaire devant le tribunal ; le tribunal lui accorde un délai de quatre mois ; s’il "
         "ne réintègre pas après le terme, le tribunal prononce la répudiation d’elle sur lui » — l’intervention "
         "judiciaire borne le serment sans borne de la Jāhiliyya, et met la sortie du mariage sous la voie "
         "judiciaire, comme en l’article 89 pour le transfert (la leçon précédente). La synthèse : la cause de la "
         "divergence remonte au fīʾ — la réintégration de la proximité de l’épouse : avant ou après l’écoulement des "
         "quatre mois ? Les ḥanafites : le fīʾ a lieu avant l’écoulement — la durée de l’īlāʾ est quatre mois ; la "
         "majorité : après l’écoulement — la durée excède quatre mois."),
        ("Le statut après l’expiration ouvre la troisième question : quand les quatre mois s’écoulent, leur "
         "écoulement compte-t-il d’abord un divorce ? Abū Ḥanīfa et les Kufiens : à l’écoulement des quatre mois, "
         "cela est un divorce unique, et il a sur elle le retour tant qu’elle est dans son délai — Mālik note que sur "
         "cela était l’avis d’Ibn Shihāb, concordant l’avis de son maître Ibn al-Musayyab : avec l’école de Kūfa, les "
         "deux plus grands juristes des Suivants à Médine. La majorité : l’écoulement des quatre mois ne compte point "
         "un divorce — Ibn al-Mundhir a rapporté de certains imams : « nous n’avons rien trouvé en quelque preuve "
         "que la résolution sur le divorce soit un divorce ; et si cela était permis, la résolution sur la "
         "réintégration serait une réintégration — et nul ne le dit ; et il n’y a rien en la langue : le serment par "
         "lequel on n’intend point le divorce n’exige point le divorce » ; et la coordination par la fāʾ sur les "
         "quatre mois dénote que le choix est après l’écoulement de la durée. ash-Shāfiʿī : « le sens apparent du "
         "Livre d’Allah dénote qu’il a quatre mois ; celui qui a quatre mois pour terme n’a point d’accès à elle "
         "jusqu’à ce que les quatre mois s’achèvent — comme si tu m’accordais un délai de quatre mois : tu n’aurais "
         "point à prendre ton droit de moi jusqu’à ce que les quatre mois s’achèvent » ; écoulés, il est entre deux "
         "statuts : réintégrer ou répudier — le divorce ne l’oblige point par l’écoulement seul, jusqu’à ce que "
         "survienne une réintégration ou un divorce. Certains ḥanafites répondent sur le terrain de la grammaire : "
         "la fāʾ est pour la suite du sens dans le temps, en la coordination du nom singulier — « Zayd vint, puis "
         "ʿAmr » — et la phrase s’insère pour détailler un global qui la précède : elle ne produit point la suite "
         "réelle, mais la suite mémorielle (adh-dhikrī) — que le détail soit mentionné après le global, fût-il d’une "
         "autre affaire, comme « Zayd vint, puis ʿAmr se leva » ; chacun des deux ordres est donc permis en le "
         "verset : le sensuel, relativement à l’īlāʾ — « s’ils réintègrent après l’īlāʾ » — et le mémoriel : quand "
         "Allah le Très Haut a mentionné qu’il leur est donné, de leurs femmes, de s’attendre quatre mois sans "
         "divorce et sans coït, ce fut le lieu du détail des deux ordres ; le visé de « s’ils réintègrent » — ils "
         "reviennent de ce sur quoi ils avaient persisté par le coït durant la durée — est alors en suite de "
         "l’īlāʾ (mémoriel), ou après elle, en suite de l’attente (at-tarabbuṣ) — « car Allah est Pardonneur, "
         "Miséricordieux », quand survint d’eux le serment sur l’injustice et la fermeture du cœur."),
        ("La condition de validité du retour arme le troisième axe. Mālik : si celui qui a fait vœu d’abstention est "
         "suspendu, et répudie après l’expiration de la durée, il lui est loisible de reprendre son épouse — mais à "
         "condition de la toucher avant l’expiration de son délai ; s’il ne la touche pas jusqu’à ce que son délai "
         "s’achève, il n’a point d’accès à elle ni de retour sur elle — sauf s’il a une excuse de maladie, ou de "
         "prison, ou quelque chose de semblable parmi les excuses qui l’empêchent du coït : alors sa reprise d’elle "
         "est établie sur elle. Si l’excuse disparaît — par son retour de voyage, sa guérison de maladie, sa sortie "
         "de prison — et qu’on lui en facilite l’accès et qu’il refuse le coït, on distingue les deux cas selon que "
         "le délai s’était écoulé ou non — Mālik l’a dit en la Mudawwana et en le Mabsūṭ ; ʿAbd al-Malik : elle est "
         "alors dissociante de lui dès le jour où le délai s’est écoulé. L’argument des Mālikites : il n’a répudié "
         "sur lui que pour son abstention du coït alors que l’īlāʾ persistait — et ce sens est présent en l’état du "
         "retour ; si donc cela annule le mariage qui s’était validement établi et dont le statut s’était confirmé, "
         "empêcher la validité du retour est plus digne encore ; et l’on ne parle de retour que pour la "
         "réintégration (al-fīʾa) : s’il se rend menteur par son abstention durant le délai, le retour est annulé et "
         "n’acquiert point de statut."),
        ("La divergence sur le coït règle l’application : si l’époux dit « je l’ai touchée », et que l’épouse dit "
         "« il ne l’a point touchée » — Mālik : la parole est la parole de l’époux ; le visage : dès que l’époux "
         "revendique le coït pour repousser par lui la séparation, la parole est la sienne, comme celui qui s’y "
         "oppose. Le second mariage de l’épouse dont le délai s’était écoulé : s’il ne la touche pas jusqu’à "
         "l’écoulement des quatre mois, il est suspendu aussi ; s’il ne réintègre pas, le divorce tombe sur lui par "
         "le premier vœu d’abstention quand les quatre mois s’écoulent — et il n’a point de retour sur elle : « car "
         "il l’a épousée, puis l’a répudiée avant de la toucher : il n’y a donc point de délai sur elle, ni de "
         "retour » — la parole du Très Haut exclut le délai de la répudiée avant consommation : « O vous qui "
         "croyez ! Quand vous vous mariez avec des croyantes et qu’ensuite vous divorcez d’avec elles avant de les "
         "avoir touchées, vous ne pouvez leur imposer un délai d’attente » (33:49). ash-Shāfiʿī : sa reprise est "
         "valide, fût-ce sans qu’il ne la touche."),
        ("L’évaluation retourne au fil : rapporter le concept et sa durée ; montrer l’avis de la majorité et ses "
         "preuves — l’écoulement des quatre mois ne compte point un divorce ; rapporter le madhab de Mālik et sa "
         "preuve au statut du retour. L’exploitation imprime le n° 1748 : « quiconque jure de ne point toucher sa "
         "femme un jour ou un mois, puis demeure jusqu’à ce que plus de quatre mois s’écoulent — cela n’est point "
         "īlāʾ ; ne fait l’objet de la suspension dans l’īlāʾ que celui qui jure au-delà de quatre mois. Quant à "
         "celui qui jure de ne point toucher sa femme quatre mois, ou moins que cela, je ne vois point d’īlāʾ sur "
         "lui : car quand arrive le terme auprès duquel on suspend, il sort de son serment — et il n’y a point de "
         "suspension sur lui » — le serment borné se dissout de soi à son terme : la suspension requiert un serment "
         "sans borne, d’où la définition, « une durée excédant quatre mois ». La préparation préalable annonce le "
         "ẓihār : expliquer « comme le dos de sa mère » et « il l’a touchée » (aṣābahā), définir le ẓihār en langue "
         "et en terme, extraire des hadiths de la leçon les mots du ẓihār et montrer la dénotation de chacun."),
    ],
    "points": [
        ("Fil de révision : trois objectifs (concept et durée ; dispositions et conditions ; les enseignements du "
         "Coran et de la Sunna) → préambule (le droit réciproque de la cohabitation ; l’abstention = nuisance ; la "
         "rébellion (nushūz) de la femme, l’īlāʾ de l’homme jurant)."),
        ("Le verset de l’īlāʾ (2:226-227) : les trois pivots — l’attente de quatre mois, la réintégration (al-fīʾ), "
         "la résolution sur le divorce (al-ʿazm) ; l’imprimé porte « 224-225 » (41ᵉ écart cumulé du registre des "
         "versets) — les versets imprimés traitent du serment en général."),
        ("Le concept : en langue le serment — l’origine l’abstention d’une chose (ālaitu, ʿūlī, īlāʾ, īlā), "
         "spécialisé quand l’abstention a pour cause le serment (al-Aʿshā : fa-ālaitu) ; en terme cinq éléments "
         "(astreinte, capacité du coït à l’habitude, abstention, durée excédant quatre mois, visée de nuire)."),
        ("La durée : la Jāhiliyya — l’épouse « suspendue, distraite, non répudiée et non épouse » ; le Coran borne : "
         "majorité (au-delà de quatre mois) / ḥanafites (le minimum quatre) ; ʿIyāḍ : nul divorce avant les quatre "
         "mois ; divorce si l’âme viole le serment avant l’achèvement."),
        ("À l’écoulement : Kufiens — le divorce tombe (rapporté aussi de Mālik) ; le reçu de Mālik et de ses "
         "compagnons (al-kāffa) — nul divorce par l’écoulement seul, mais à la suspension devant le gouverneur — "
         "« s’ils réintègrent durant elles » / « après elles » — ce à quoi ʿAlī a fait allusion."),
        ("L’article 112 du Code de la famille : l’épouse au tribunal, délai de quatre mois, à défaut de "
         "réintégration le tribunal prononce la répudiation — l’intervention judiciaire borne le serment sans borne "
         "de la Jāhiliyya (comme l’article 89 pour le transfert)."),
        ("Le statut après expiration : Abū Ḥanīfa et les Kufiens — un divorce unique avec retour (avec eux Ibn "
         "Shihāb, concordant Ibn al-Musayyab) ; la majorité (Ibn al-Mundhir) — « la résolution sur le divorce n’est "
         "pas un divorce » (la symétrie : la résolution sur la réintégration serait réintégration — nul ne le dit ; "
         "la langue : le serment qui n’intend point le divorce ne l’exige point ; la fāʾ — le choix après "
         "l’écoulement) ; ash-Shāfiʿī — le sens apparent : deux statuts après l’écoulement ; la réponse des "
         "ḥanafites : la suite mémorielle (adh-dhikrī) — « Zayd vint, puis ʿAmr » — chacun des deux ordres permis en "
         "le verset."),
        ("La condition du retour : le coït avant l’expiration du délai, sauf excuse (maladie, prison) ; l’excuse "
         "disparue, accès facilité, refus — deux cas selon que le délai s’était écoulé (la Mudawwana et le Mabsūṭ ; "
         "ʿAbd al-Malik : dissociante dès le jour où le délai s’est écoulé) ; l’argument — répudié pour "
         "l’abstention même : « empêcher la validité du retour est plus digne encore » (le retour n’est parlé que "
         "pour la réintégration, al-fīʾa)."),
        ("La divergence du coït : « la parole est la parole de l’époux » — comme celui qui s’y oppose ; le second "
         "mariage : suspendu à nouveau, divorce par le premier vœu d’abstention, point de délai ni de retour "
         "(33:49) ; ash-Shāfiʿī : la reprise valide fût-ce sans toucher."),
        ("L’exploitation (n° 1748) : qui jure un jour ou un mois puis demeure au-delà de quatre mois — point "
         "d’īlāʾ ; la suspension requiert un serment au-delà de quatre mois — « quand arrive le terme auprès duquel "
         "on suspend, il sort de son serment » ; la préparation annonce le ẓihār (« comme le dos de sa mère », "
         "aṣābahā)."),
    ],
    "vocabulaire": [
        {"ar": "الإيلاء", "translit": "al-īlāʾ",
         "fr": "le vœu d’abstention — en langue le serment, d’origine l’abstention d’une chose ; en terme : le serment de l’époux astreint, capable du coït à l’habitude, de s’abstenir une durée excédant quatre mois, avec la visée de la nuire"},
        {"ar": "آلا", "translit": "ālā",
         "fr": "« il fait vœu d’abstention » — l’īlāʾ et le taʿlī, le serment et le jurement ; le vers d’al-Aʿshā (fa-ālaitu) montre l’usage ancien du mot pour le serment quelconque"},
        {"ar": "يوقف", "translit": "yūqaf",
         "fr": "« qu’il soit suspendu » — qu’il soit retenu et empêché, placé devant le gouverneur : l’office de la suspension (al-waqf) est de le contraindre à réintégrer le foyer ou à répudier"},
        {"ar": "يفيء", "translit": "yafīʾ",
         "fr": "« il réintègre » — il revient, c’est-à-dire qu’elle revient (au foyer conjugal) ; le fīʾ — la réintégration de la proximité de l’épouse — est le pivot de la divergence sur la durée"},
        {"ar": "يصيبها", "translit": "yuṣibhā",
         "fr": "« il la touche » — il coïte avec elle ; le coït dans le délai est la condition de validité du retour dans l’īlāʾ"},
        {"ar": "الفيء", "translit": "al-fīʾ",
         "fr": "la réintégration — le retour à la proximité de l’épouse : avant l’écoulement des quatre mois chez les ḥanafites (la durée de l’īlāʾ est de quatre mois), après chez la majorité (elle excède quatre mois)"},
        {"ar": "التعقيب الذكري", "translit": "at-taʾqīb adh-dhikrī",
         "fr": "la suite mémorielle — la fāʾ coordonne l’ordre de la mention, non celui des faits ; les ḥanafites en tirent la lecture du verset : « Zayd vint, puis ʿAmr » — l’écoulement des quatre mois ne fait point tomber le divorce de soi"},
        {"ar": "الرجعة", "translit": "ar-rajʿa",
         "fr": "le retour — la reprise de l’épouse après répudiation ; dans l’īlāʾ, condition de validité : le coït avant l’expiration du délai, sauf excuse — « s’il se rend menteur par son abstention durant le délai, le retour est annulé »"},
    ],
    "avertissement": "Ce commentaire est un guide de lecture du manuel ; en cas de divergence d’expression, le manuel et sa traduction savante font foi.",
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
DOCIDS = ('12967', '12971')
deja = [d for d in DOCIDS if d in com]
if deja:
    print(f'!! déjà présent : {deja} — rien de fait')
    raise SystemExit(1)
com['12967'] = norme_entree(E_12967)
com['12971'] = norme_entree(E_12971)

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

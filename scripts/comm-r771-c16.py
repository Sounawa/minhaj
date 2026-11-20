#!/usr/bin/env python3
"""R771 — ajoute le commentaire pédagogique de la leçon 16 de hadith-tanawi-1
(13114 طلاق الحائض والعدة بالأقراء — le divorce de la réglée et la retraite
comptée par les cycles, « Le divorce prononcé durant les menstrues et la
retraite comptée en cycles (qurūʾ) (ṭalāq al-ḥāʾiḍ wa-l-ʿidda bi-l-qurūʾ) »
dans la traduction du manuel, la seizième du livre, étiquetée « leçon 22 »
par l'imprimé (الدرس 22) — le SUIVANT de R770, 13101, annoncé dès
R768/R769/R770)
à content/commentaires/hadith-tanawi-1.json.

Même protocole que comm-r770-c15.py : normalisation de la ponctuation FR
(U+202F avant ; : ! ? » et après «, apostrophe courbée) sur l'entrée
nouvelle seulement — opération idempotente. Rédaction d'après la lecture
complète de la leçon (htmlFr intégral, ~28 000 caractères débalisés — la
plus longue leçon du livre ; couche arabe lue en entier pour l'étiquette de
l'imprimé « (الدرس 22) », la date imprimée en tête (الإثنين 22 يوليو 2019),
les emplacements coraniques de la couche arabe — trois étiquettes seules
(سورة البقرة الآية: 226), un emplacement muet au maḥall al-khilāf, la
parenthèse vide du verset de aṭ-Ṭalāq et l'étiquette 196 du verset du
pèlerinage — et les particularités typographiques de la couche arabe :
point initial dans la question de la retraite, (لماذ) sans hamza dans
l'exploitation, numérotation « 2ــ » absente de la couche française).
Règle 2 de LISEZ-MOI.md : aucune invention — les numéros du Muwaṭṭaʾ
(1823, 1824, 1826, 1827, 1832), les attributions (ʿAbdallāh ibn ʿUmar,
ʿUmar b. al-Khaṭṭāb, ʿĀʾisha, Ḥafṣa bint ʿAbd ar-Raḥmān, ʿAmra bint
ʿAbd ar-Raḥmān, al-Qāsim ibn Muḥammad, Sālim ibn ʿAbdallāh, Abū Bakr ibn
ʿAbd ar-Raḥmān, Sulaymān ibn Yasār, Ibn Shihāb az-Zuhrī, Muʿāwiya ibn Abī
Sufyān, Zayd ibn Thābit, Yaḥyā ibn Saʿīd al-Makhzūmī, Mālik, ash-Shāfiʿī,
Abū Ḥanīfa, Aḥmad, ad-Dāraquṭnī, Ibn ʿAbbās) et les références (la
Mudawwana — Code de la famille — article 136 ; al-Baqara 226, 228, 197 ;
aṭ-Ṭalāq 2) sont cités tels qu'ils figurent dans la leçon.

Garde-fous (convention des vagues R765-R770) :
- verif-citations intégrée : chaque fragment « » de l'entrée doit être
  retrouvé verbatim dans le htmlFr de la leçon (0 manquant, abort sinon) ;
- recoupements : ancres vérifiées dans les leçons voisines (13101 — la
  leçon précédente du registre, le mafqūd et la Mudawwana classique ;
  12992 — le muḥallil, dont la leçon a établi le régime de la bāʾin ;
  12966 — le ẓihār, la voix conjointe de l'école médinoise déjà
  rencontrée ; 12971 — l'īlāʾ, dont le verset [al-Baqara 226] est
  l'argument des disputants d'ʿĀʾisha ; 13115 — la leçon suivante du
  registre, le logement et la pension de la répudiée).
"""
import json, re, sys
import html as H

CHEMIN = 'content/commentaires/hadith-tanawi-1.json'
LIVRE = 'content/books/hadith-tanawi-1.json'
DOCID = '13114'

E_13114 = {
    "auteur": "IA-1, tour R771",
    "resume": (
        "Guide de lecture de la leçon 16 (طلاق الحائض والعدة بالأقراء — le divorce "
        "de la réglée et la retraite comptée par les cycles ; la traduction du "
        "manuel porte « Le divorce prononcé durant les menstrues et la retraite "
        "comptée en cycles (qurūʾ) (ṭalāq al-ḥāʾiḍ wa-l-ʿidda bi-l-qurūʾ) »), la "
        "seizième du livre, étiquetée leçon 22 par l'imprimé (الدرس 22) : le n° 1823 "
        "du Muwaṭṭaʾ arme le fond — ʿAbdallāh ibn ʿUmar « répudia sa femme alors "
        "qu'elle était en ses menstrues, du temps du Messager de Dieu », ʿUmar ibn "
        "al-Khaṭṭāb interrogea le Prophète, et l'ordre tomba : « Ordonne-lui de la "
        "reprendre (fal-yurājiʿhā), puis de la retenir (yumsikuhā) jusqu'à ce "
        "qu'elle se purifie, puis qu'elle menstrue, puis qu'elle se purifie ; "
        "ensuite, s'il veut, qu'il la retienne, et s'il veut, qu'il la répudie avant "
        "de la toucher : telle est la retraite (ʿidda) par laquelle Dieu a ordonné "
        "de répudier les femmes. » Le n° 1824 borne le compte : ʿĀʾisha avait fait "
        "passer Ḥafṣa bint ʿAbd ar-Raḥmān « à sa demeure de retraite quand elle "
        "entra dans le sang de la troisième menstruation » ; des disputants "
        "l'avaient objecté le verset de l'īlāʾ (le verset 226), et "
        "elle répondit : « Vous avez dit vrai ; mais savez-vous ce que sont les "
        "qurūʾ ? Les qurūʾ ne sont que les périodes de pureté (al-aṭhār). » Le n° "
        "1827 transporte la règle au terme : « Quand la répudiée entre dans le sang "
        "de la troisième menstruation, elle est séparée (bānat) de son mari : entre "
        "eux n'est héritage, et il n'a point de reprise (rajʿa) sur elle. » — le "
        "dire compilé des cinq maîtres de Médine (al-Qāsim ibn Muḥammad, Sālim ibn "
        "ʿAbdallāh, Abū Bakr ibn ʿAbd ar-Raḥmān, Sulaymān ibn Yasār et Ibn Shihāb). "
        "Le tamhīd fonde le tout : Allah « a légiféré le divorce (ṭalāq) lorsque la "
        "poursuite de la vie conjugale devient impossible », et le Prophète a "
        "montré les manières légales du divorce — « Ces manières sont au nombre de "
        "trois : que le divorce tombe au temps d'une période de pureté (ṭuhr) ; "
        "qu'il ne touche point la femme dans cette pureté, c'est-à-dire qu'il n'ait "
        "point consommé avec elle ; et qu'il s'agisse d'une seule répudiation "
        "(ṭalāqa wāḥida), non réitérée. » Deux questions ordonnent la leçon : « "
        "Quel est donc le statut du divorce placé au temps des menstrues, ou dans "
        "une pureté où l'on a touché l'épouse ? Et par quoi la répudiée compte-t-"
        "elle sa retraite (ʿidda) ? » Les termes : « Puis il la retient » — « il "
        "prolonge le fait de la retenir », « la reprise et la retenue ne sont qu'un "
        "seul acte vu sous deux faces » ; « Il la touche » — « il la possède "
        "sexuellement (yujāmiʿuhā) », « le toucher désigne ici la consommation, "
        "non le contact ordinaire » ; « Elle fit passer Ḥafṣa » — « elle transféra "
        "Ḥafṣa de la maison de la retraite » ; « Elle est quitte de lui et il est "
        "quitte d'elle » — « la dissolution "
        "mutuelle du conjugal et de l'héréditaire ». L'analyse déplie le statut : "
        "le divorce au temps des menstrues est « illicite (muḥarram) par l'accord "
        "des savants (bi-l-ijmāʾ), contraire à la Sunna » ; et l'ordre de reprendre "
        "est « une preuve manifeste (dallīl bayyin) que ce divorce est advenu et "
        "lie (lāzim) » — « impossible (muḥāl) d'ordonner la reprise de ce qui n'a "
        "point été rompu ». La profondeur : le divorce « n'est point des "
        "actes par lesquels on se rapproche d'Allah (taqarrub) », il est « la levée "
        "de l'inviolabilité (zawāl ʿiṣma) en un droit d'un homme » — « s'il le "
        "place hors de sa manière, il pèche, et ce qu'il en a placé le lie » ; « Il "
        "est en effet impossible que le divorce lie l'obéissant qui suit la Sunna "
        "et ne lie point le désobéissant contrevenant » — « l'ordre du licite "
        "retournerait en privilège de l'illicite » ; l'appui d'ad-Dāraquṭnī : « Ô "
        "Messager de Dieu, cette répudiation est-elle comptée (yuḥtasab) ? » — « "
        "oui. » — « La faute engage l'acte ; l'acte engage le compte », mais « le "
        "compte n'est point la récompense : il est la charge de ce que la main a "
        "placé ». La deuxième manière (la pureté sans contact) évite « la "
        "perplexité (al-labs) » : « elle ne sait si elle est enceinte — elle "
        "compterait alors sa retraite par la mise au monde (waḍʾ al-ḥaml) — ou non "
        "— elle compterait par les qurūʾ » — « Le délai n'est point une cruauté ; "
        "il est la fenêtre par laquelle la certitude entre dans le jugement ». Le "
        "diffèrement à la deuxième pureté reçoit trois justifications : la "
        "menstruation du divorce et la pureté qui suit « valent un seul qurʾ » "
        "(sinon « deux répudiations placées dans un seul qurʾ », « ce qui est "
        "contraire à la Sunna ») ; la punition — « il l'a puni en différant le "
        "divorce, pour aggraver (taghliẓ) sur lui le châtiment » — objection (« ce "
        "qui ne sied point à son rang ») et réponse (« il était négligent "
        "(mufarriṭ) d'avoir laissé la question de côté », « dissuasion (zajr) pour "
        "ceux qui viendraient après lui ») ; et "
        "l'écartement du préjudice (« du sens du préjudice (iḍrār) interdit ») — "
        "« la tentation d'un retour trop prompt, qui n'est point réconciliation "
        "mais possession surprise ». La contrainte à la reprise : Mālik et ses "
        "compagnons portent l'ordre sur « l'obligation (wujūb) » — « est contraint "
        "(yujbaru) à la reprendre tant qu'elle est en sa retraite » — appuyés sur "
        "« telle est la retraite par laquelle Dieu a ordonné de répudier les "
        "femmes » et sur la lecture d'Ibn ʿUmar « répudiez-les à la réception de "
        "leur retraite » — « c'est-à-dire en réceptionnant leur retraite » ; les "
        "trois imams portent l'ordre sur « la recommandation (nadb) » par le verset "
        "de aṭ-Ṭalāq 2 (« Puis quand elles atteignent le terme prescrit, retenez-"
        "les de façon convenable, ou séparez-vous d'elles de façon convenable ») — "
        "« sur la même échelle du choix (takhyīr) » ; la réponse : « le principe "
        "(aṣl) dans l'ordre est l'obligation », et l'on « spécialise (takhṣīṣ) la "
        "généralité des versets pour celui qui n'a point répudié en période de "
        "menstrues » — « les versets parlent du divorce réglé, le hadith du divorce "
        "déréglé ». La retraite : quatre cas — « la grossesse compte par la mise au "
        "monde, l'absence de consommation ne compte point de retraite, la "
        "ménopausée par trois mois, et la réglée — celle qui a ses menstrues "
        "(muʿtāda) — par trois qurūʾ », « à la lettre manifeste du Coran » (le "
        "verset 228 : « Et les femmes divorcées doivent observer un délai d'attente "
        "de trois menstrues »). Le qurʾ, « nom partagé (mushtarak) entre la pureté "
        "et les menstrues », divise les écoles : Mālik et ash-Shāfiʿī soutiennent "
        "que « les qurūʾ sont les périodes de pureté (al-aṭhār) » — « c'est le dire "
        "rapporté d'ʿĀʾisha » et « de la plupart des savants de Médine » — preuve : "
        "le hadith d'Ibn ʿUmar (« une explicitation (bayān) » de la réception) et "
        "l'interdit (« elle ne réceptionne point sa retraite dans cette "
        "menstruation-ci »), selon l'accord du jumhūr ; Abū Ḥanīfa, et Aḥmad "
        "« dans un de ses deux dits », soutiennent que « les qurūʾ sont les "
        "menstrues » — « le dire rapporté d'un groupe des Compagnons et des "
        "Successeurs » — l'argument : la « pureté du divorce » compterait, « de "
        "sorte que sa retraite serait de deux qurūʾ et un demi », quand les "
        "menstrues donnent « trois qurūʾ pleins » ; réponses : « le qurʾ est le "
        "passage d'un état à un autre (al-intiqāl min ḥāl ilā ḥāl) » — « la retraite "
        "ne se trouve donc placée que par trois puretés complètes » — et « rien "
        "n'écarte de nommer deux et un tiers — ou deux et une part du troisième » "
        "trois, comme le "
        "pèlerinage « des mois connus » (le verset 197) « n'est que de deux mois et "
        "dix jours ». Le lieu de la divergence : « la femme est-elle libérée (taḥill) "
        "par son entrée dans le sang de la troisième menstruation, ou par "
        "l'expiration de celui-ci ? » — les tenants des puretés : « elle n'est "
        "libérée que par son entrée dans le sang », car « l'entrée du sang scelle "
        "la complétude de la troisième pureté » — le récit de Ḥafṣa, « le verset "
        "même des qurūʾ » objecté puis explicité par ʿĀʾisha ; la lettre de "
        "Muʿāwiya à "
        "Zayd ibn Thābit (n° 1826) : « Quand elle entre dans le sang de la troisième "
        "menstruation, elle est quitte de lui et il est quitte d'elle : elle "
        "n'hérite pas de lui et il n'hérite pas d'elle. » — « la frontière du "
        "conjugal et de l'héréditaire au jour précis où le troisième sang coule » ; "
        "la Mudawwana — « le Code de la famille » — l'adopte à son article 136 : « "
        "La non-enceinte compte ce qui suit : trois périodes de pureté complètes "
        "pour celles qui ont des menstrues. » La sagesse de l'interdiction : la "
        "considération de « l'état psychologique de l'épouse durant les menstrues » "
        "— « comment porterait-elle le divorce, qui engage le cours de sa vie et "
        "l'avenir de ses enfants ? » — et l'allègement : pendant la retraite elle "
        "est « interdite de mariage », et le divorce en menstrues « la fait attendre "
        "la pureté pour commencer seulement sa retraite » — « la Loi règle "
        "l'ouverture du compte sur le corps même de celle qui le compte, non sur le "
        "caprice de celui qui rompt ». L'exploitation (n° 1832) : l'auxiliaire à qui "
        "sa femme « demanda le divorce » règle l'instant — « Quand tu menstrues, "
        "préviens-moi. », « Quand tu te purifies, préviens-moi. » — et il la répudia "
        "; Mālik : « C'est la plus belle chose que j'aie entendue en cela. » ; la "
        "leçon y lit « la demande de la femme demande elle-même le temps juste » — "
        "Mālik « n'a "
        "point loué une Sentence, il a loué une manière » — « l'école se reconnaît "
        "à ce qu'elle choisit de célébrer » — le divorce demandé n'est pas « un "
        "marché forcé, mais un rendez-vous réglé par les cycles que Dieu a mis dans "
        "les corps ». La préparation préalable annonce la leçon suivante : « Lire "
        "les hadiths de la leçon suivante, et répondre à ce qui suit » — « le "
        "statut du logement de la répudiée dans sa retraite » et « Sur qui la "
        "pension (nafaqa) de la répudiée en sa retraite est-elle obligatoire ? » — "
        "la dix-septième du livre. NB "
        "consignés (sans correction, règle 5) : (1) l'étiquette de l'imprimé (الدرس "
        "22) — la leçon est la seizième du livre selon l'ordre du registre ; (2) la "
        "couche arabe porte en tête la date imprimée (الإثنين 22 يوليو 2019) — "
        "artefact unique dans le livre (aucune autre leçon du manuel n'en porte) ; "
        "(3) les emplacements coraniques : la couche arabe porte trois étiquettes "
        "seules (سورة البقرة الآية: 226) — dont deux requièrent en réalité « le "
        "verset qui porte le mot même de qurūʾ », 2:228 — et un emplacement "
        "muet au maḥall al-khilāf (« parenthèse muette dans l'original »), plus la "
        "parenthèse vide de aṭ-Ṭalāq (سورة الطلاق الآية:2) et l'étiquette "
        "196 pour le verset du "
        "pèlerinage réellement en 197 (le texte partiel الْحَجُّ أَشْهُرٌ مَعْلُومَاتٌ) ; "
        "la couche française restitue les textes "
        "(2:226 concordant ; 2:228 aux deux emplacements de l'analyse, étiquette "
        "corrigée ; 2:228 rétabli au maḥall "
        "al-khilāf ; 65:2 restauré ; 2:197 corrigé) et consigne « des écarts "
        "d'étiquetage » 44ᵉ, 45ᵉ et 46ᵉ du "
        "registre ; (4) le tamhīd de la couche française porte le paragraphe « Ces "
        "manières ne sont point des ornements surajoutés » et la maxime « abghaḍ "
        "al-ḥalāl ilā llāh », sans équivalent imprimé dans la couche arabe ; (5) la "
        "« Mudawwana » de cette leçon est le Code de la famille marocain (2004), à "
        "distinguer de la Mudawwana classique du fiqh malikite citée à la leçon "
        "précédente (13101) — même mot, deux réalités ; (6) le n° 1825 du Muwaṭṭaʾ "
        "est laissé de côté par la sélection du manuel (1823, 1824, 1826, 1827, "
        "1832 cités) ; (7) la couche arabe porte (بماذا تعتد المطلقة التي تحيض؟) "
        "avec un point initial déplacé et (لماذ) sans hamza dans l'exploitation, et "
        "numérote la question de la contrainte à la reprise dans la couche arabe, "
        "sans numéro dans la couche française."),
    "explication": [
        ("La leçon 16 succède au mafqūd (leçon 15, n° 1819-1822) et ouvre le temps "
         "du corps : les numéros 1823-1827 du Muwaṭṭaʾ — plus la lettre du n° 1826 "
         "et l'exploitation du n° 1832 — succèdent aux 1819-1822, dans le même "
         "livre du mariage. Le fil passe du disparu — le temps qui court sur "
         "l'absence — au divorce placé hors de son temps — les menstrues — et au "
         "compte qui le répare : la leçon précédente réglait l'attente de l'épouse "
         "du disparu ; celle-ci règle l'instant licite de la "
         "rupture et l'ouverture du compte de la répudiée réglée. Les chaînes "
         "s'ancrent à Médine : Nāfiʿ, « l'affranchi d'Ibn ʿUmar (m. 117/735) », « le "
         "canal médinois du Muwaṭṭaʾ par excellence » ; le n° 1824 court par Ibn "
         "Shihāb az-Zuhrī, ʿUrwa ibn az-Zubayr et ʿĀʾisha, avec la confirmation "
         "d'ʿAmra bint ʿAbd ar-Raḥmān — « ʿUrwa a dit vrai. » — « un témoignage de "
         "juriste, non une simple courtoisie familiale ». Trois objectifs posés à "
         "l'ouverture : le statut du divorce au temps des menstrues ; "
         "l'entendu des qurūʾ dans la parole du Très-Haut ; la sagesse qui fonde "
         "l'interdiction."),
        ("Le tamhīd donne la boussole : le divorce n'est pas supprimé mais réglé — "
         "légiféré « lorsque la poursuite de la vie conjugale devient impossible », "
         "il reste entouré de manières légales qui « protègent l'épouse du "
         "précipité de l'homme, lui laissent le temps de l'apaisement et de la "
         "réconciliation, et préservent le lignage d'une confusion qui le "
         "troublerait ». Et la couche française d'ajouter la maxime : « Le divorce, "
         "dans l'ordre des actes licites, est le plus détestable des licites » — "
         "la Loi « n'a point voulu qu'il fût "
         "l'occasion d'un second préjudice : aussi le renvoie-t-elle à l'instant où "
         "le corps de la femme est le plus net de ses altérations, et le jugement "
         "le plus libre de ses brouillards ». La méthode du chapitre se lit dans ce "
         "renvoi : le statut de l'acte ne se sépare pas du temps du corps où l'acte "
         "tombe."),
        ("Le statut d'abord. Le divorce au temps des menstrues est « illicite "
         "(muḥarram) par l'accord des savants (bi-l-ijmāʾ), contraire à la Sunna » "
         "; le Prophète « l'a désapprouvé sur ʿAbdallāh ibn ʿUmar ». La leçon tire "
         "de l'ordre prophétique une preuve de statut : ordonner la reprise "
         "établit que le divorce « est advenu et lie (lāzim) » — on ne dit pas « "
         "reprends-la » à un homme qui n'a point séparé de sa femme. La profondeur "
         "du raisonnement : le divorce « n'est point des "
         "actes par lesquels on se rapproche d'Allah (taqarrub) comme la prière et "
         "le jeûne », lesquels « ne se produisent que selon leur manière propre "
         "(sunnatuhā) » ; il est « la levée de l'inviolabilité (zawāl ʿiṣma) en un "
         "droit d'un homme » — placé hors de sa manière, il pèche, mais il lie ; "
         "sinon « l'ordre du licite retournerait en privilège de l'illicite ». "
         "Ad-Dāraquṭnī fournit l'appui : ʿUmar demande si la répudiation « est-elle "
         "comptée (yuḥtasab) », réponse : « oui. » — « La faute engage l'acte ; "
         "l'acte engage le compte », mais « le compte n'est point la récompense : "
         "il est la charge de ce que la main a placé »."),
        ("La deuxième manière (la pureté sans contact) protège de « la perplexité "
         "(al-labs) » : répudiée dans une pureté où elle a été touchée, la femme "
         "« ne sait si elle est enceinte — elle compterait alors sa retraite par "
         "la mise au monde (waḍʾ al-ḥaml) — ou non — elle compterait par les "
         "qurūʾ » ; la leçon y voit « la sagesse même de la parole prophétique » : « "
         "Le délai n'est point une cruauté ; il est la fenêtre par laquelle la "
         "certitude entre dans le jugement ». Le diffèrement à la deuxième pureté "
         "(« jusqu'à ce qu'elle se purifie, puis qu'elle menstrue, puis qu'elle se "
         "purifie ») reçoit trois justifications en divergence : (a) la "
         "menstruation du divorce et la pureté qui suit « valent un seul qurʾ » — "
         "répudier dans la première pureté serait « comme deux répudiations "
         "placées dans un seul qurʾ », « ce qui est contraire à la Sunna » ; (b) "
         "la punition — « il l'a puni en différant le divorce, pour aggraver "
         "(taghliẓ) sur lui le châtiment » — objection : cela requiert qu'Ibn ʿUmar "
         "fût savant de l'interdiction, « ce qui ne sied point à son rang » ; "
         "réponse : « il était négligent (mufarriṭ) d'avoir laissé la question de "
         "côté », « dissuasion (zajr) pour ceux qui viendraient "
         "après lui » ; (c) l'écartement du préjudice — « afin que la reprise ne "
         "devienne point le simple objet du désir du divorce » — répudier au début "
         "de la première pureté serait « du sens du préjudice (iḍrār) interdit » : "
         "« la Loi écarte de l'homme qui rompt la tentation d'un retour trop "
         "prompt, qui n'est point réconciliation mais possession surprise »."),
        ("La contrainte à la reprise partage l'école. Mālik et ses compagnons "
         "portent l'ordre sur « l'obligation (wujūb) » : le répudié en menstrues « "
         "est contraint (yujbaru) à la reprendre tant qu'elle est en sa retraite » "
         "— l'appui : « telle est la retraite par laquelle Dieu a ordonné de "
         "répudier les femmes » — « le divorce légal a son temps prescrit, et "
         "l'homme qui l'a manqué répare en reprenant ce qu'il a rompu hors du "
         "temps » ; par le sens, il a « anticipé sur le prolongement de la "
         "retraite », la retraite de la femme « se trouva allongée » — le Prophète "
         "« interdit de l'allonger sur elle » et ordonne de ne répudier qu'à sa "
         "réception — la lecture d'Ibn ʿUmar « répudiez-"
         "les à la réception de leur retraite », « c'est-à-dire en réceptionnant "
         "leur retraite ». Les trois imams — Abū Ḥanīfa, ash-Shāfiʿī et Aḥmad — "
         "portent l'ordre sur « la recommandation (nadb) » : le verset de aṭ-Ṭalāq "
         "2 (« Puis quand elles atteignent le terme prescrit, retenez-les de façon "
         "convenable, ou séparez-vous d'elles de façon convenable ») met la "
         "retenue et la séparation « sur la même échelle du choix (takhyīr) ». La "
         "réponse malikite : « le principe (aṣl) dans l'ordre est l'obligation » ; "
         "et l'on « spécialise (takhṣīṣ) la généralité des versets pour celui qui "
         "n'a point répudié en période de menstrues » — « les versets parlent du "
         "divorce réglé, le hadith du divorce déréglé »."),
        ("La retraite ensuite. Quatre cas : « la grossesse compte par la mise au "
         "monde, l'absence de consommation ne compte point de retraite, la "
         "ménopausée par trois mois, et la réglée — celle qui a ses menstrues "
         "(muʿtāda) — par trois qurūʾ » — sur la réglée consommée, « les savants "
         "ne divergent point », c'est « à la lettre manifeste du Coran » (le "
         "verset 228 : « Et les femmes divorcées doivent observer un délai "
         "d'attente de trois menstrues »). Mais le qurʾ est « nom partagé "
         "(mushtarak) entre la pureté et les menstrues », et l'entendu du verset "
         "divise : Mālik et ash-Shāfiʿī soutiennent que « les qurūʾ sont les "
         "périodes de pureté (al-aṭhār) », « c'est le dire rapporté d'ʿĀʾisha » et "
         "« de la plupart des savants de Médine » — preuve : le hadith d'Ibn ʿUmar "
         "(« une explicitation (bayān) » de la réception) et "
         "l'interdit (« elle ne réceptionne point sa retraite dans cette "
         "menstruation-ci »), selon l'accord du jumhūr ; Abū Ḥanīfa, et Aḥmad « dans "
         "un de ses deux dits », soutiennent que « les qurūʾ sont les menstrues » "
         "— « le dire rapporté d'un groupe des Compagnons et des Successeurs » — "
         "l'argument : compter « la pureté du divorce » rendrait la retraite « de "
         "deux qurūʾ et un demi » au lieu de trois, quand les menstrues donnent « "
         "trois qurūʾ pleins » ; réponses malikites : « le qurʾ est le passage "
         "d'un état à un autre (al-intiqāl min ḥāl ilā ḥāl) » — « la retraite ne "
         "se trouve donc placée que par "
         "trois puretés complètes » — et « rien n'écarte de nommer deux et un "
         "tiers — ou deux et une part du troisième » trois, comme le pèlerinage « "
         "des mois connus » (le "
         "verset 197) « n'est que de deux mois et dix jours ». Le lieu de la "
         "divergence achève le compte : « la femme est-elle libérée (taḥill) par "
         "son entrée dans le sang de la troisième menstruation, ou par "
         "l'expiration de celui-ci ? » — les tenants des puretés : « elle n'est "
         "libérée que par son entrée dans le sang », car « l'entrée du sang scelle "
         "la complétude de la troisième pureté » — le récit de Ḥafṣa, « le verset "
         "même des qurūʾ » objecté puis explicité par ʿĀʾisha ; la lettre de "
         "Muʿāwiya à Zayd ibn Thābit — la consultation écrite (istiftāʾ) du calife "
         "au savant — tranche le cas de la bāʾin, "
         "« la répudiation dissolvante » dont « la leçon du muḥallil a établi le "
         "régime » : « Quand elle entre dans le sang de la troisième menstruation, "
         "elle est quitte de lui et il est quitte d'elle : elle n'hérite pas de "
         "lui et il n'hérite pas d'elle. » — « la frontière du conjugal et de "
         "l'héréditaire au jour précis où le troisième sang coule » ; la Mudawwana "
         "— « le Code de la famille » — l'adopte à son article 136 : « La "
         "non-enceinte compte ce qui suit : trois périodes de pureté complètes "
         "pour celles qui ont des menstrues. » — « l'école malikite comme droit "
         "positif du royaume »."),
        ("La sagesse ferme le chapitre. Deux considérations : « l'état "
         "psychologique de l'épouse durant les menstrues » — la femme y est "
         "« atteinte d'un malaise qui ne lui permet point de porter des choses "
         "faciles » — « comment porterait-elle le divorce, qui engage le cours de "
         "sa vie et l'avenir de ses enfants ? » — la décision ne doit pas être « "
         "l'écho d'un moment de fatigue » ; et l'allègement — pendant la retraite "
         "la femme est « interdite de mariage », et le divorce en menstrues « la "
         "fait attendre la pureté pour commencer seulement sa retraite » — « la "
         "Loi règle l'ouverture du compte sur le corps même de celle qui le "
         "compte, non sur le caprice de celui qui rompt ». L'exploitation (n° "
         "1832) donne la manière accomplie : l'auxiliaire à qui sa femme « demanda "
         "le divorce » règle l'instant — « Quand tu menstrues, préviens-moi. », "
         "puis « Quand tu te purifies, préviens-moi. » — et il la répudia ; Mālik : "
         "« C'est la plus belle chose que j'aie entendue en cela. » — « la demande "
         "de la femme demande elle-même le temps juste », « l'homme auxiliaire "
         "n'a point refusé la séparation demandée » ; l'école « n'a point loué "
         "une Sentence, il a loué une manière » — « l'école se reconnaît à ce "
         "qu'elle choisit de célébrer » — le divorce demandé n'est pas « un marché "
         "forcé, mais un rendez-vous réglé par les cycles que Dieu a mis dans les "
         "corps ». La préparation préalable annonce la leçon suivante : « Lire les "
         "hadiths de la leçon suivante, et répondre à ce qui suit » — « le statut "
         "du logement de la répudiée dans sa retraite » et « Sur qui la pension "
         "(nafaqa) de la répudiée en sa retraite est-elle obligatoire ? » — la "
         "dix-septième du livre."),
    ],
    "points": [
        ("Fil de révision : trois objectifs (le statut du divorce au temps des "
         "menstrues ; l'entendu des qurūʾ dans la parole du Très-Haut ; la sagesse "
         "de l'interdiction) → tamhīd (le divorce légiféré quand la vie conjugale "
         "devient impossible, trois manières sunnites) → trois textes (n° 1823, "
         "1824, 1827) + la lettre (n° 1826) + l'exploitation (n° 1832)."),
        ("Le tamhīd : le divorce légiféré « lorsque la poursuite de la vie "
         "conjugale devient impossible » ; les manières légales au nombre de trois "
         "(une pureté, sans contact, une seule répudiation) ; « le plus détestable "
         "des licites »."),
        ("Le n° 1823 : Ibn ʿUmar répudia en ses menstrues ; l'ordre : reprendre, "
         "retenir, purifier, menstruer, purifier, puis retenir ou répudier « avant "
         "de la toucher » — « telle est la retraite par laquelle Dieu a ordonné de "
         "répudier les femmes »."),
        ("Le n° 1824 : Ḥafṣa installée « à sa demeure de retraite quand elle entra "
         "dans le sang de la troisième menstruation » ; les disputants et le "
         "verset de l'īlāʾ ; ʿĀʾisha : « savez-vous ce que sont les qurūʾ ? Les "
         "qurūʾ ne sont que les périodes de pureté (al-aṭhār) »."),
        ("Le n° 1827 (les cinq maîtres de Médine) : à la troisième menstruation, « "
         "elle est séparée (bānat) de son mari » — plus d'héritage, plus de "
         "reprise ; le n° 1826 (Zayd à Muʿāwiya) : « elle est quitte de lui et il "
         "est quitte d'elle »."),
        ("Le statut : « illicite (muḥarram) par l'accord des savants (bi-l-ijmāʾ) "
         "» ; l'ordre de reprendre prouve que le divorce lie (le muḥāl d'ordonner "
         "la reprise de ce qui n'a point été rompu) ; taqarrub contre zawāl ʿiṣma "
         "(le pêcheur lie, sinon « l'ordre du licite retournerait en privilège de "
         "l'illicite ») ; ad-Dāraquṭnī : la répudiation « est-elle comptée "
         "(yuḥtasab) » — « oui. »"),
        ("La deuxième pureté : la perplexité (enceinte — la mise au monde — ou "
         "non — les qurūʾ) ; « Le délai n'est point une cruauté ; il est la "
         "fenêtre par laquelle la certitude entre dans le jugement » ; trois "
         "justifications du diffèrement (un seul qurʾ ; le taghliẓ, avec l'objection "
         "et la réponse du mufarriṭ et du zajr ; l'iḍrār écarté — « possession "
         "surprise »)."),
        ("La contrainte à la reprise : Mālik — l'obligation (wujūb : « est "
         "contraint (yujbaru) à la reprendre tant qu'elle est en sa retraite » ; la "
         "retraite prescrite ; la lecture d'Ibn ʿUmar) ; les trois "
         "imams — la recommandation (nadb : aṭ-Ṭalāq 2, le takhyīr) ; la réponse : "
         "« le principe (aṣl) dans l'ordre est l'obligation » et le takhṣīṣ — « les "
         "versets parlent du divorce réglé, le hadith du divorce déréglé »."),
        ("Les qurūʾ : quatre cas de retraite (grossesse, absence de "
         "consommation, ménopause, trois qurūʾ) ; « à la lettre manifeste du "
         "Coran » pour la réglée ; le mushtarak divise — les puretés (Mālik, "
         "ash-Shāfiʿī, ʿĀʾisha, la plupart des savants de Médine) contre les "
         "menstrues (Abū Ḥanīfa, Aḥmad dans un de ses deux dits) ; l'argument du « "
         "deux qurūʾ et un demi » contre les « trois qurūʾ pleins » ; réponses : "
         "l'intiqāl min ḥāl ilā ḥāl et le pèlerinage (le verset 197)."),
        ("Le maḥall al-khilāf : libérée par l'entrée dans le sang — « l'entrée du "
         "sang scelle la complétude de la troisième pureté » (Ḥafṣa ; Zayd à "
         "Muʿāwiya, n° 1826 ; la bāʾin et la sortie mutuelle du conjugal et de "
         "l'héréditaire) — la Mudawwana (le Code de la famille, article 136) : « "
         "trois périodes de pureté complètes pour celles qui ont des menstrues »."),
        ("La sagesse et l'exploitation : l'état psychologique et l'allègement (« "
         "la Loi règle l'ouverture du compte sur le corps même de celle qui le "
         "compte, non sur le caprice de celui qui rompt ») ; l'auxiliaire (n° "
         "1832) — « C'est la plus belle chose que j'aie entendue en cela », la "
         "manière louée plutôt que la sentence ; la préparation annonce le "
         "logement et la pension de la répudiée (leçon suivante)."),
    ],
    "vocabulaire": [
        {"ar": "الحائض", "translit": "al-ḥāʾiḍ",
         "fr": "la réglée : celle qui a ses menstrues (muʿtāda) — le sujet du titre (ṭalāq al-ḥāʾiḍ) ; son divorce est « illicite (muḥarram) par l'accord des savants (bi-l-ijmāʾ), contraire à la Sunna », et sa retraite se compte « par trois qurūʾ »"},
        {"ar": "القرء", "translit": "al-qurʾ",
         "fr": "le cycle : « nom partagé (mushtarak) entre la pureté et les menstrues » — le pivot lexical de tout le chapitre ; la réponse malikite : « le qurʾ est le passage d'un état à un autre (al-intiqāl min ḥāl ilā ḥāl) »"},
        {"ar": "الأقراء", "translit": "al-aqrāʾ",
         "fr": "les cycles du compte : « savez-vous ce que sont les qurūʾ ? Les qurūʾ ne sont que les périodes de pureté (al-aṭhār) » — le dire d'ʿĀʾisha qui fonde la thèse des puretés, adoptée par la Mudawwana à son article 136"},
        {"ar": "الطهر", "translit": "al-ṭuhr",
         "fr": "la pureté : première des manières sunnites — « que le divorce tombe au temps d'une période de pureté (ṭuhr) » ; la deuxième exige une pureté où il ne l'a point touchée, sinon « la perplexité (al-labs) »"},
        {"ar": "الرجعة", "translit": "ar-rajʿa",
         "fr": "la reprise : « il n'a point de reprise (rajʿa) sur elle » à la troisième menstruation ; l'ordre « Ordonne-lui de la reprendre » ouvre le débat — contrainte chez Mālik, recommandation chez les trois imams"},
        {"ar": "الوجوب", "translit": "al-wujūb",
         "fr": "l'obligation : le port de l'ordre chez Mālik et ses compagnons — le répudié « est contraint (yujbaru) à la reprendre tant qu'elle est en sa retraite » ; « le principe (aṣl) dans l'ordre est l'obligation »"},
        {"ar": "الندب", "translit": "al-nadb",
         "fr": "la recommandation : le port de l'ordre chez Abū Ḥanīfa, ash-Shāfiʿī et Aḥmad — les versets de aṭ-Ṭalāq 2 mettent retenue et séparation « sur la même échelle du choix (takhyīr) » ; la leçon répond par le takhṣīṣ (les versets du divorce réglé, le hadith du divorce déréglé)"},
        {"ar": "مدونة الأسرة", "translit": "Mudawwana al-usra",
         "fr": "le Code de la famille : son article 136 reprend la thèse des puretés — « La non-enceinte compte ce qui suit : trois périodes de pureté complètes pour celles qui ont des menstrues. » — « l'école malikite comme droit positif du royaume », à distinguer de la Mudawwana classique citée à la leçon précédente"},
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


def texte_corpus():
    """htmlFr débalisé : frontières de blocs -> espace, tags inline -> ''."""
    d = json.load(open(LIVRE, encoding='utf-8'))
    e = [x for x in d['lessons'] if x['docId'] == DOCID][0]
    raw = e['htmlFr']
    t = re.sub(r'</?(p|h[1-6]|li|dd|dt|blockquote|div|tr|td|th|ul|ol|dl|section)[^>]*>', ' ', raw, flags=re.I)
    t = re.sub(r'<[^>]+>', '', t)
    t = H.unescape(t)
    t = t.replace('\u00a0', ' ').replace('\u202f', ' ')
    return re.sub(r'\s+', ' ', t).strip()


def norme_cmp(s):
    s = s.replace('\u202f', ' ').replace('\u00a0', ' ')
    return re.sub(r'\s+', ' ', s)


# ---------- fusion ----------
data = json.load(open(CHEMIN, encoding='utf-8'))
com = data['commentaires']
if DOCID in com:
    print(f'!! {DOCID} déjà présent — rien de fait')
    raise SystemExit(1)
com[DOCID] = norme_entree(E_13114)

with open(CHEMIN, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
    f.write('\n')

# ---------- validation ----------
data2 = json.load(open(CHEMIN, encoding='utf-8'))
print('entrées au total :', len(data2['commentaires']))
motif_ar = re.compile(r'[\u0600-\u06FF\u0750-\u077F\u08A0-\u08FF\uFDFA]')
mauvais = 0
e = data2['commentaires'][DOCID]
mots = sum(len(x.split()) for x in [e['resume']] + e['explication'] + e['points'])
print(f'{DOCID} : {mots} mots (resume+explication+points), vocab {len(e["vocabulaire"])}')
for t in [e['resume'], e['avertissement']] + e['explication'] + e['points'] + [v['fr'] for v in e['vocabulaire']] + [v['translit'] for v in e['vocabulaire']]:
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
    if not motif_ar.search(v['ar']):
        mauvais += 1
        print('   vocab ar non arabe :', v['ar'])
    if re.search(r'[\u064B-\u0652\u0670]', v['ar']):
        mauvais += 1
        print('   vocab ar avec harakat :', v['ar'])

# ---------- verif-citations (fragments « » verbatim dans le htmlFr) ----------
corpus = norme_cmp(texte_corpus())
textes = [e['resume']] + e['explication'] + e['points'] + [v['fr'] for v in e['vocabulaire']]
fragments = []
for t in textes:
    fragments += re.findall(r'«([^«»]+)»', t)
manquants = []
for f in fragments:
    fc = norme_cmp(f).strip(' …\u202f\u00a0')
    if fc and fc not in corpus:
        manquants.append(f)
print(f'verif-citations : {len(fragments)} fragments « », {len(manquants)} manquant(s)')
for f in manquants:
    print('   MANQUE :', f[:100])
if manquants:
    mauvais += len(manquants)

# ---------- recoupements ----------
an = json.load(open(LIVRE, encoding='utf-8'))['lessons']
def fr(docid):
    x = [y for y in an if y['docId'] == docid][0]
    t = re.sub(r'</?(p|h[1-6]|li|dd|dt|blockquote|div|tr|td|th|ul|ol|dl|section)[^>]*>', ' ', x['htmlFr'], flags=re.I)
    t = re.sub(r'<[^>]+>', '', t)
    t = H.unescape(t)
    return re.sub(r'\s+', ' ', t)

ancres = [
    ('13101 — la leçon précédente du registre (le mafqūd et la Mudawwana classique)', 'mafqūd' in fr('13101') and 'Mudawwana' in fr('13101')),
    ('12992 — le muḥallil, dont la leçon a établi le régime de la bāʾin', 'bāʾin' in fr('12992')),
    ('12966 — le ẓihār, la voix conjointe de l’école médinoise déjà rencontrée', 'ẓihār' in fr('12966')),
    ('12971 — l’īlāʾ, dont le verset [al-Baqara 226] est l’argument des disputants d’ʿĀʾisha', '226' in fr('12971')),
    ('13115 — la leçon suivante du registre (le logement et la pension de la répudiée)', 'logement' in fr('13115') and 'nafaqa' in fr('13115')),
    ('13114 — le qurʾ, pivot lexical de la leçon (mushtarak)', 'mushtarak' in corpus),
]
ok = 0
for nom, b in ancres:
    print('recoupement :', 'PASS' if b else 'ÉCHEC', '—', nom)
    ok += 1 if b else 0
if ok != len(ancres):
    mauvais += len(ancres) - ok

print('contrôle ponctuation/arabe FR + citations + recoupements :', 'PASS' if mauvais == 0 else f'ÉCHEC ({mauvais})')
if mauvais:
    sys.exit(1)

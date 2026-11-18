#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""R751 — commentaires des leçons 13-14 hadith-5ep : pdf-13 (يسر الدين
الإسلام — la facilité de la religion : le neuvième hadīth « Éloignez-vous
de ce que je vous ai interdit », les manifestations du yusr, ses effets,
les mises en garde contre la divergence et la multiplication des questions)
et pdf-14 (دعم وتطبيق — la seconde consolidation : synthèse de la chaîne,
de la création honorée au devenir entre les mains d'Allah). Septième vague
du livre (SUIVANT de R750-b, leçons 11-12 ; hadith-5ep 12/29 au départ).
Rédaction d'après la lecture complète FR des deux leçons (extraction non
lossy scripts/extrait-r751.py) ET du tirage arabe du livre
(content/textbooks-src/hadith-5-ibtidai_text.pdf, lignes 3320-3800).
Aucune invention (règle 2) : hadiths, versets, citations et attributions
tels que la leçon les donne.
NB de lecture consigné (zone IA-2, journal worklog) : les références
imprimées du tirage portent al-Ḥaǧǧ 76 (pdf-13) et ar-Rūm 19 et Muḥammad
20 (pdf-14) — les versets qui portent ces paroles sont le 78 (al-Ḥaǧǧ),
le 20 (ar-Rūm) et le 19 (Muḥammad), vérifiés web (quran.com,
surahquran.com) ; le commentaire le dit en langage lecteur, comme en
R742/R747/R749/R750. Corrects dans le tirage : al-Baqara 286,
at-Taġābun 16, Āl ʿImrān 103, al-Anbiyāʾ 7, ash-Shuʿarāʾ 88-89.
NB consigné (SUIVANT de R750-b) : l'annonce de vague « leçon 13 = le
huitième hadīth « أنا بعثت بالحنيفية السهلة » » était fausse — la leçon
13 est le NEUVIÈME hadīth (« Éloignez-vous de ce que je vous ai
interdit... ») ; le huitième n'apparaît pas dans les leçons 1-14 (la
numérotation du manuel : 1ᵉʳ intentions, 2ᵉ Jibrīl, 3ᵉ piliers,
4ᵉ décret, 5ᵉ innovations, 6ᵉ licite+cœur, 7ᵉ naṣīḥa, 9ᵉ yusr — le 8ᵉ est
hors de la sélection du manuel ; « ḥanīfiyya » ne se trouve que dans la
leçon 3).
NB consigné (vigilance, zone IA-2) : l'introduction FR de la leçon 15
(pdf-15) fait rapporter le dixième hadīth par Abū Hurayra ʿAbd ar-Raḥmān
ibn Ṣaḫr — les recueils usuels le donnent par Abū Masʿūd al-Anṣārī ;
vigilance pour le futur commentateur de la leçon 15.
Garde-fous de comm-r747/comm-r749/comm-r750 repris (typographie FR,
arabe entre parenthèses seulement, vocab ar sans harakat, guillemets
appariés) + fenêtre de mots 1700-2400 (resume+explication+points) par
entrée."""
import json, re, os, sys

CHEMIN = 'content/commentaires/hadith-5ep.json'

E_13 = {
    "auteur": "IA-1, tour R751",
    "resume": ("Guide de lecture de la leçon 13 (la facilité de la religion islamique — al-yusr "
               "(يُسْرُ الْإِسْلَامِ)) : le neuvième hadīth des Quarante de l'imam al-Nawawī, rapporté "
               "par Abū Hurayra ʿAbd ar-Raḥmān ibn Ṣaḫr — qu'Allah soit satisfait de lui — : "
               "« Éloignez-vous de ce que je vous ai interdit, et accomplissez de ce que je vous ai "
               "ordonné ce que vous pouvez ; car ce sont seulement les questions excessives et les "
               "divergences envers leurs prophètes qui ont fait périr ceux qui étaient avant vous » "
               "[Ṣaḥīḥ de al-Buḫārī et Muslim]. La préparation de la leçon 12 annonçait les deux "
               "chantiers — le sens et les manifestations, les effets — et l'analyse les tient en "
               "deux sections : les manifestations (les interdits laissés en leur généralité, les "
               "commandements conditionnés par la capacité) et les effets (la levée de la gêne, "
               "l'élan vers l'obéissance, la permission de l'interdit par nécessité — « Les "
               "nécessités autorisent les interdits »), et deux mises en garde : la divergence et la "
               "multiplication des questions. La scène de Muslim — « Chaque année, ô Messager d'Allah ? » — donne "
               "à la règle son visage, et l'exploitation la fait descendre dans le corps : « Prie "
               "debout ; si tu ne le peux, assis ; et si tu ne le peux, sur le flanc. »"),
    "explication": [
        ("La leçon 13 ouvre un nouveau hadīth : après la naṣīḥa — le septième des Quarante —, elle est "
         "« consacrée à la facilité » — al-yusr (يُسْرُ الْإِسْلَامِ) — et au « neuvième hadīth "
         "des Quarante de l'imam al-Nawawī, rapporté par Abū Hurayra ʿAbd ar-Raḥmān ibn Ṣaḫr — qu'Allah "
         "soit satisfait de lui ». La préparation de la leçon 12 avait posé les deux chantiers — "
         "le sens, les manifestations, les effets —, que la leçon tient en trois "
         "objectifs : « Que je connaisse la facilité de l'islam et certaines de ses "
         "manifestations », « Que je saisisse les effets de la facilité dans l'islam », « Que je "
         "m'applique à incarner le principe de facilité et la levée de la gêne dans mon culte et mes "
         "transactions »."),
        ("Le tamhīd pose la thèse : « La facilité et la levée de la gêne comptent parmi les principes "
         "majeurs sur lesquels repose l'islam dans ses manifestations variées, et c'est par elle qu'il "
         "se distingue par des effets manifestes, tant dans la relation de l'homme avec son Seigneur "
         "que dans sa relation avec lui-même ou avec son semblable. » Les trois relations dessinent le "
         "champ du yusr : le culte, la morale, l'équité — le troisième objectif y ajoutera les "
         "transactions. Deux questions fixent le plan "
         "de l'analyse : « Quelles sont donc les manifestations de la facilité de l'islam ? Et quels "
         "sont ses effets ? »"),
        ("Le texte rend le hadīth entier [Ṣaḥīḥ de al-Buḫārī et Muslim] : « Éloignez-vous de ce que je "
         "vous ai interdit, et accomplissez de ce que je vous ai ordonné ce que vous pouvez ; car ce "
         "sont seulement les questions excessives et les divergences envers leurs prophètes qui ont "
         "fait périr ceux qui étaient avant vous. » La notice du transmetteur : Abū Hurayra "
         "est ʿAbd ar-Raḥmān ibn Ṣaḫr ad-Dawsī, resté célèbre « sous la kunya d'Abū Hurayra, celle dont "
         "le Messager d'Allah — prière et salut d'Allah sur lui — l'a affublé » ; il embrassa l'islam l'année de Ḫaybar, fréquenta le Prophète « d'une fréquentation assidue », et devint « le "
         "Compagnon — qu'Allah soit satisfait "
         "d'eux — qui mémorisa le mieux le hadīth prophétique » ; ʿUmar le nomma gouverneur d'al-Baḥrayn, "
         "puis il assuma « le gouvernement de Médine la Illuminée » ; il mourut en 57 ou 58 de l'Hégire, "
         "à soixante-dix-huit ans, et « fut enterré au al-Baqīʾ »."),
        ("Le glossaire déplie les trois clés du hadīth : « éloignez-vous en (fajtanibūhu) » — « écartez-vous "
         "de cela, et n'en approchez rien » : l'interdit se fuit, il ne se traverse pas ; « ce que vous "
         "pouvez (mā staṭaʾtum) » — « ce dont vous avez la capacité et le pouvoir » : la clé de voûte de "
         "toute la leçon ; « leurs divergences envers leurs prophètes (ḫtilāfuhum ʿalā anbiyāʾihim) » — "
         "« leur opposition et leur désobéissance à leurs prophètes » : la divergence est définie comme "
         "une désobéissance. L'extraction demande deux travaux : « Je mentionne ce qui, "
         "dans le hadīth, indique la facilité de l'islam » et « J'extrais ce que le Prophète — prière et "
         "salut d'Allah sur lui — a ordonné et ce dont il a averti dans le hadīth »."),
        ("Première section — les manifestations. La formule de la leçon : « L'islam est venu avec des "
         "ordres et des interdits qu'il faut observer ; mais il a laissé les interdits en leur "
         "généralité, et conditionné les commandements par la capacité. » L'interdit vaut pour tout ce "
         "que la Loi prohibe — « propos et actes, apparents ou intérieurs » — et « doit être délaissé "
         "et évité, en acte d'obéissance et de soumission à Allah et à Son Messager » : « Éloignez-vous "
         "de ce que je vous ai interdit. » Pour le commandement, « l'absence de capacité peut en effet "
         "empêcher certains assujettis d'obtempérer ». La raison de l'asymétrie : "
         "« C'est que l'interdit est une demande d'abandon, et l'abandon est à la portée de chacun : "
         "voilà pourquoi il n'a pas été conditionné par la capacité ; quant au commandement, il est "
         "tantôt réalisable et tantôt irréalisable : voilà pourquoi il a été conditionné par la "
         "capacité. »"),
        ("Les exemples rendent la règle concrète : « il prie selon ce qu'il peut en "
         "accomplir » ; « il lave ce qui lui est possible » ; et pour les répréhensibles : « si l'on "
         "ne peut les supprimer en totalité, on supprime ce qui est en son pouvoir ». L'exploitation : d'après ʿImrān ibn Ḥuṣayn — qu'Allah soit satisfait de lui — "
         "qui souffrait d'hémorroïdes (bawāsīr) : « Prie debout ; si tu ne le peux, assis ; et si tu "
         "ne le peux, sur le flanc. » [Ṣaḥīḥ de al-Buḫārī] — « les manifestations de l'obligation "
         "mesurée à la capacité dans ce hadīth » que l'exercice demande d'expliciter."),
        ("Seconde section — les effets. « Parmi les effets de la facilité de l'islam : la levée de la "
         "gêne qui pèse sur l'assujetti, son élan vers l'obéissance, et la possibilité qui lui est "
         "donnée d'obtempérer en toute circonstance. » Quand la Loi ordonne, « l'obligation porte sur "
         "ce que l'on peut endurer et accomplir » — trois āyāt : « Allah n'impose à une âme "
         "que ce qu'elle peut porter » (Sourate al-Baqara — verset 286), « Craignez Allah autant que "
         "vous le pouvez » (Sourate at-Taġābun — verset 16), « Il ne vous a imposé aucune gêne dans la "
         "religion » (Sourate al-Ḥaǧǧ — la référence imprimée porte le verset 76 ; le verset qui porte "
         "ces paroles est le 78) — et le sommet : « l'un des plus grands aspects de la facilité de l'islam est la permission de "
         "l'interdit par nécessité, comme la consommation de charogne pour préserver la vie », avec "
         "« parmi les règles de la Loi : “Les nécessités autorisent les interdits.” »"),
        ("Le yusr devient une éthique de transmission : « Il est obligatoire de respecter les "
         "principes de la facilité et de les appliquer dans l'accomplissement des obligations "
         "islamiques : par ménagement de l'assujetti, en rendant l'obéissance aisée, pour donner à "
         "aimer la pratique religieuse » — et le triple péril : « en évitant de rendre "
         "les choses difficiles tout comme la divergence, qui mènent à la gêne, à l'adversité et à la "
         "scission ». D'où le pivot : « C'est pourquoi le Prophète — prière et salut d'Allah sur lui — "
         "a averti, dans ce hadīth, de la divergence et de la multiplication des questions » — et "
         "voici les deux mises en garde."),
        ("Première mise en garde — la divergence, menacée de perdition : « la divergence est "
         "en effet cause de division et de faiblesse », et Allah « a ordonné l'unité et interdit la "
         "scission et la divergence » : « Attachez-vous tous ensemble au câble d'Allah, et ne vous "
         "divisez pas » (Sourate Āl ʿImrān — verset 103). Le tirage ajoute une lecture fine du mot : "
         "« wa-ḫtilāfuhum » (وَاخْتِلَافُهُمْ) « se prononce avec ḍamma sur le hāʾ, et non avec kasra » — "
         "il est « coordonné à “kathra” (l'abondance) » : « l'abondance de leurs questions les a fait "
         "périr, et leur divergence les a fait périr ; ce second sens est le plus expressif, car la "
         "perdition naquit de la divergence elle-même, non de son ampleur. »"),
        ("Seconde mise en garde — la multiplication des questions. « Les savants ont réparti la question "
         "en deux catégories. » La première — « ce qui relève de la pratique, parmi ce dont on a besoin "
         "dans les affaires de la religion » — elle « est demandée » : « Interrogez donc les gens "
         "du rappel, si vous ne savez pas » (Sourate al-Anbiyāʾ — verset 7) ; « c'est de ce genre que "
         "relèvent les questions des Compagnons sur les butins, la succession calale et les novas, "
         "entre autres » [Fatḥ al-Bārī d'Ibn Ḥaǧar] — « la succession calale » est la kalāla (le cas de "
         "succession le plus débattu), « les novas » (les nawāfil) les "
         "actes surérogatoires. La seconde — « ce qui relève de la contestation, de l'affectation et de "
         "l'indiscrétion ; c'est là ce qui est interdit » — « la multiplication des questions peut "
         "engendrer la multiplication des réponses, et il y a là gêne et peine »."),
        ("La « cause de la révélation du hadīth figure dans le Ṣaḥīḥ de Muslim » : lors d'un sermon, "
         "« Ô gens ! Le pèlerinage vous a été prescrit : accomplissez-le. » ; un homme demanda : "
         "« Chaque année, ô Messager d'Allah ? » ; « Il garda le silence jusqu'à ce que l'homme eut "
         "répété trois fois » ; puis : « Si je disais oui, ce serait obligatoire, et vous ne le "
         "pourriez pas. » Puis : « Laissez-moi ce que je vous ai "
         "laissé : car ce sont les questions excessives et les divergences envers leurs prophètes qui "
         "ont fait périr ceux qui étaient avant vous. Quand je vous ordonne une chose, accomplissez-en "
         "ce que vous pouvez : et quand je vous interdis une chose, délaissez-la. » [Ṣaḥīḥ de Muslim]"),
        ("Ce qu'il faut retirer du hadīth, en deux : « L'islam est religion de facilité et d'unité, non "
         "religion de gêne et de scission » ; « La guidance du Prophète — prière et salut d'Allah sur "
         "lui — comporte la facilité dans les affaires de la religion et du monde ». L'évaluation : "
         "« Pourquoi le commandement a-t-il été conditionné par la "
         "capacité, et l'interdit "
         "ne l'a-t-il pas été ? », « Pourquoi le Prophète — prière et salut d'Allah sur lui — a-t-il "
         "mis en garde contre la divergence et la multiplication des questions ? » La préparation ouvre la leçon 14 : "
         "« Je lis les textes de la leçon qui vient, mettant à profit les acquis de mon savoir dans les "
         "leçons précédentes pour répondre aux questions liées au texte »."),
    ],
    "points": [
        ("Fil de révision : trois objectifs (connaître le yusr et ses manifestations ; saisir ses effets ; "
         "incarner la facilité et la levée de la gêne dans le culte et les transactions) → tamhīd "
         "(principes majeurs ; deux questions) → le hadīth entier → notice d'Abū "
         "Hurayra → glossaire (trois gloses) → deux sections (les manifestations ; les effets) → deux "
         "mises en garde (la divergence ; la multiplication des questions) → deux utilités → istiṯmār (ʿImrān ibn Ḥuṣayn) → iʿdād. L'évaluation : « Pourquoi le "
         "commandement a-t-il été conditionné par la capacité, et l'interdit ne l'a-t-il pas été ? »"),
        ("La continuité exacte : la préparation de la leçon 12 demandait « Je mentionne le sens de la "
         "facilité (al-yusr) dans l'islam et certaines de ses manifestations » et « J'expose certains "
         "des effets qui découlent de la facilité de l'islam » — la leçon 13 les tient : manifestations "
         "puis effets."),
        ("La formule de la facilité : « il a laissé les interdits en leur généralité, et conditionné les "
         "commandements par la capacité » ; l'asymétrie s'explique : « l'interdit est une demande "
         "d'abandon, et l'abandon est à la portée de chacun », le commandement « tantôt réalisable et "
         "tantôt irréalisable »."),
        ("Les trois gloses du glossaire : fajtanibūhu — « écartez-vous de cela, et n'en approchez rien » ; "
         "mā staṭaʾtum — « ce dont vous avez la capacité et le pouvoir » ; ḫtilāfuhum ʿalā anbiyāʾihim — "
         "« leur opposition et leur désobéissance à leurs prophètes »."),
        ("Les effets du yusr : « la levée de la gêne qui pèse sur l'assujetti, son élan vers "
         "l'obéissance, et la possibilité qui lui est donnée d'obtempérer en toute circonstance » ; "
         "trois āyāt (al-Baqara 286 ; at-Taġābun 16 ; al-Ḥaǧǧ — imprimée 76, porteur 78, vérifié web) ; "
         "la règle « Les nécessités autorisent les interdits »."),
        ("L'éthique du ménagement : « par ménagement de l'assujetti, en rendant l'obéissance aisée, pour "
         "donner à aimer la pratique religieuse » ; les deux ennemies du yusr — rendre les choses "
         "difficiles et la divergence — mènent « à la gêne, à l'adversité et à la scission »."),
        ("La lecture linguistique du tirage : « wa-ḫtilāfuhum » « se prononce avec ḍamma sur le hāʾ, et "
         "non avec kasra », coordonné à kathra ; « la perdition naquit de la divergence elle-même, non "
         "de son ampleur »."),
        ("Les deux catégories de questions [Fatḥ al-Bārī d'Ibn Ḥaǧar] : la question pratique (al-Anbiyāʾ "
         "7 ; les butins, « la succession calale » — la kalāla —, « les novas ») et la question de "
         "contestation ; la scène de Muslim (« Chaque année, ô Messager d'Allah ? », « Si je disais "
         "oui, ce serait obligatoire, et vous ne le pourriez pas », « Laissez-moi ce que je vous ai "
         "laissé » ; le questionneur était al-ʿAqraʿ ibn Ḥābis) ; la notice d'Abū Hurayra : mémorisation "
         "exemplaire, gouverneur d'al-Baḥrayn puis de Médine, mort en 57/58 ; l'iʿdād vers la "
         "consolidation (leçon 14)."),
    ],
    "vocabulaire": [
        {"ar": "يسر الاسلام", "translit": "al-yusr",
         "fr": "la facilité de l'islam — titre de la leçon et « principes majeurs sur lesquels repose "
               "l'islam dans ses manifestations variées » : les interdits laissés en leur généralité, "
               "les commandements conditionnés par la capacité, l'interdit permis par nécessité."},
        {"ar": "اثار يسر الاسلام", "translit": "ʾāṯāru yusri al-islām",
         "fr": "les effets de la facilité dans l'islam — seconde section de l'analyse : « la levée de "
               "la gêne qui pèse sur l'assujetti, son élan vers l'obéissance, et la possibilité qui "
               "lui est donnée d'obtempérer en toute circonstance »."},
        {"ar": "رفع الحرج", "translit": "rafʿ al-ḥarǧ",
         "fr": "la levée de la gêne — premier effet du yusr : Allah n'impose à une âme « que ce "
               "qu'elle peut porter » (al-Baqara 286) et « aucune gêne dans la religion » (al-Ḥaǧǧ — "
               "porteur 78)."},
        {"ar": "فاجتنبوه", "translit": "faǧtanibūhu",
         "fr": "« éloignez-vous en » — « écartez-vous de cela, et n'en approchez rien » : l'interdit "
               "est une demande d'abandon totale, et « l'abandon est à la portée de chacun » — voilà "
               "pourquoi il n'est pas conditionné par la capacité."},
        {"ar": "ما استطعتم", "translit": "mā staṭaʾtum",
         "fr": "« ce que vous pouvez » — « ce dont vous avez la capacité et le pouvoir » : la clé de "
               "voûte du hadīth ; le commandement, « tantôt réalisable et tantôt irréalisable », est "
               "conditionné par elle."},
        {"ar": "اختلافهم على انبيائهم", "translit": "ḫtilāfuhum ʿalā anbiyāʾihim",
         "fr": "« leurs divergences envers leurs prophètes » — « leur opposition et leur désobéissance "
               "à leurs prophètes » ; la divergence « est en effet cause de division et de faiblesse » "
               "— Allah « a ordonné l'unité et interdit la scission et la divergence » (Āl ʿImrān 103)."},
        {"ar": "النهي عن كثرة السؤال", "translit": "an-nahyu ʿan kathrati s-suʾāl",
         "fr": "la mise en garde contre la multiplication des questions — seconde sous-section : deux "
               "catégories de savants (la question pratique, demandée ; la question de contestation, "
               "interdite) ; « la multiplication des questions peut engendrer la multiplication des "
               "réponses, et il y a là gêne et peine »."},
        {"ar": "الضرورات تبيح المحظورات", "translit": "aḍ-ḍarūrāt tubīḥ al-maḥẓūrāt",
         "fr": "« Les nécessités autorisent les interdits » — « l'on compte parmi les règles de la "
               "Loi » ; « l'un des plus grands aspects de la facilité de l'islam est la permission de "
               "l'interdit par nécessité, comme la consommation de charogne pour préserver la vie »."},
    ],
    "avertissement": "Ce commentaire est un guide de lecture du manuel ; en cas de divergence d'expression, le manuel et sa traduction savante font foi.",
}


E_14 = {
    "auteur": "IA-1, tour R751",
    "resume": ("Guide de lecture de la leçon 14 (le soutien et l'application — daʿm wa-t-taṭbīq "
               "(دَعْمٌ وَتَطْبِيقٌ)) : la seconde consolidation du manuel (la leçon 7 portait le même "
               "titre) — aucun hadīth nouveau n'est installé, mais « leçon de synthèse des leçons "
               "précédentes ». Le texte récapitule la chaîne entière : l'honneur de la création — "
               "« L'homme est une créature honorée auprès d'Allah le Très-Haut », créé de terre, d'une "
               "« extraction d'eau vile », « dans trois ténèbres » —, puis l'âge de la responsabilité "
               "religieuse, où Allah commande la foi et l'obéissance et guide « vers le soin du cœur, "
               "qui est la source de son bonheur et de son malheur » (ash-Shuʿarāʾ 88-89), puis les "
               "grands chantiers des leçons précédentes — « Il a interdit l'usure », les choses "
               "douteuses, « les innovations et les répréhensibles », « le conseil sincère », "
               "« l'attachement à la Sunna » (« mordez-y avec les dents molaires » [Ǧāmiʿ bayān "
               "al-ʿilm wa-faḍlihi d'Ibn ʿAbd al-Barr]) — et ferme sur le devenir entre les mains "
               "d'Allah : « Allah l'a décrété, et ce qu'Il a voulu, Il l'a fait », car « le “si "
               "seulement” ouvre l'œuvre de Satan » [Ṣaḥīḥ de Muslim]. La préparation ouvre la leçon "
               "15 : l'invocation (ad-duʿāʾ) et « le rapport entre la consommation du licite et "
               "l'invocation » — le dixième hadīth des Quarante."),
    "explication": [
        ("La leçon 14 est la seconde consolidation du manuel — le soutien et l'application "
         "(daʿm wa-t-taṭbīq (دَعْمٌ وَتَطْبِيقٌ)), « leçon de synthèse des leçons précédentes ». Elle "
         "n'installe aucun hadīth des Quarante : son texte est une page de synthèse écrite par les "
         "auteurs du manuel, et ses trois objectifs sont des objectifs de bilan — « Que j'évalue mes "
         "acquis dans les leçons précédentes », « Que je repère mes capacités dans l'analyse », "
         "« Que je mette mes acquis à profit dans des situations nouvelles ». La préparation de la "
         "leçon 13 l'avait annoncée : « Je lis les textes de la leçon qui vient, mettant à profit les "
         "acquis de mon savoir dans les leçons précédentes pour répondre aux questions liées au "
         "texte » — la leçon qui vient est la consolidation."),
        ("Le texte part de l'origine : « L'homme est une créature honorée auprès d'Allah le Très-Haut. "
         "Il l'a créé — glorifié soit-Il — de terre, puis a fait son lignage d'une extraction d'eau "
         "vile ; il vient ensuite, création après création, dans trois ténèbres, jusqu'à paraître en "
         "une autre création ; et béni soit Allah, le meilleur des créateurs. » L'āya citée porte la "
         "même trajectoire : « Il est de Ses signes qu'Il vous a créés de terre ; puis, voici que vous "
         "êtes des hommes qui se répandent sur la terre » (Sourate ar-Rūm — la référence imprimée "
         "porte le verset 19 ; le verset qui porte ces paroles est le 20). La compréhension demande "
         "d'expliquer « vous vous répandez » (tantashirūn) — le verbe même de l'āya : de la terre "
         "muette à l'homme qui se répand, la trace de l'honneur. Pour les « trois ténèbres », l'élève "
         "peut convoquer l'āya qui les nomme ensemble (az-Zumar, verset 6) ; pour les étapes du "
         "développement embryonnaire que l'analyse demande d'exposer, la leçon 6 — « les phases de la "
         "création de l'homme » — reste la réserve du manuel."),
        ("Vient l'âge du devoir : « Et lorsqu'il atteint l'âge de la responsabilité religieuse, Il lui "
         "commande la foi en Lui et l'obéissance, et le guide vers le soin du cœur, qui est la source "
         "de son bonheur et de son malheur. » L'āya citée tranche : « …un jour où ni les biens ni les "
         "enfants ne seront d'aucune utilité, sauf celui qui vient à Allah avec un cœur sain » "
         "(Sourate ash-Shuʿarāʾ — versets 88-89). C'est la boucle exacte de la leçon 11 : le cœur, "
         "émir des organes, « la droiture du cœur est la plus grande des sources de bien, et sa "
         "corruption la plus grande des maux » — et l'analyse demande « comment l'expliques-tu ? » : "
         "les œuvres témoignent de la droiture ou de la corruption du cœur."),
        ("Le texte passe ensuite les chantiers en revue : « Il lui a permis certaines choses et lui en "
         "a interdit d'autres : Il a interdit l'usure, l'a exhorté à la piété de prudence et à l'écart "
         "des choses douteuses, l'a détourné des innovations et des répréhensibles, lui a rendu "
         "obligatoire le conseil sincère en vertu de la fraternité de foi, et lui a commandé "
         "l'attachement à la Sunna. » Chaque clause rouvre une leçon : le permis et l'interdit — la "
         "leçon 10 ; « la piété de prudence » face aux douteux — la leçon 10 encore ; « les innovations "
         "et les répréhensibles » — la leçon 9 ; « le conseil sincère en vertu de la fraternité de "
         "foi » — la leçon 12 ; « l'attachement à la Sunna » — la clause qui suit. La compréhension "
         "demande les contraires de trois mots — « la foi (al-ʾīmān) », « la piété de prudence "
         "(al-waraʾ) », « les bien guidés (al-mahdiyyūn) » — face à la foi, la mécréance ; face aux "
         "bien guidés, les égarés."),
        ("Le commandement de la Sunna vient avec sa preuve : « Attachez-vous à ma Sunna et à la Sunna "
         "des califes bien guidés qui viendront après moi : mordez-y avec les dents molaires. » "
         "[Ǧāmiʿ bayān al-ʿilm wa-faḍlihi d'Ibn ʿAbd al-Barr] L'image des dents molaires (an-nawāǧiḏ) "
         "dit l'arrimage ferme : ne pas lâcher la prise de la Sunna du Prophète — prière et salut "
         "d'Allah sur lui — ni de celle des califes bien guidés ; le vocabulaire retient les « bien "
         "guidés » (al-mahdiyyūn), les califes de la guidée dont la conduite fait corps avec la "
         "Sunna."),
        ("Le texte ferme sur la main d'Allah : « Et en tout cela, Il a placé son devenir entre Ses "
         "mains » — « …Il connaît vos mouvements et vos lieux de repos » (Sourate Muḥammad — la "
         "référence imprimée porte le verset 20 ; le verset qui porte ces paroles est le 19). La "
         "preuve prophétique suit : « Et s'il t'arrive une chose, ne dis pas : “si seulement j'avais "
         "fait telle et telle chose”, mais dis : “Allah l'a décrété, et ce qu'Il a voulu, Il l'a "
         "fait”, car le “si seulement” ouvre l'œuvre de Satan » [Ṣaḥīḥ de Muslim]. C'est la boucle de "
         "la leçon 8 (le décret et la prédestination) : le décret n'annule pas le devoir, il en "
         "décharge le regret — le « si seulement » est une porte que Satan ouvre, la formule du "
         "décret une porte que le serviteur ferme."),
        ("La compréhension demande d'expliquer quatre mots : « l'âge de la responsabilité religieuse » "
         "(quand l'homme devient assujetti), « les choses douteuses », « les répréhensibles », et "
         "« vous vous répandez » (tantashirūn). L'analyse déroule les questions de bilan : « L'homme "
         "est une créature honorée auprès d'Allah le Très-Haut : j'appuie cela d'un texte religieux » "
         "— l'āya du haut honneur, Nous avons honoré les fils d'Adam (al-Isrāʾ, verset 70), est la "
         "plus proche ; « Le cœur est la source du bonheur de l'homme et de son malheur : comment "
         "l'expliques-tu ? » — la leçon 11 en réponse ; « Pourquoi la Loi a-t-elle exhorté à la piété "
         "de prudence face aux choses douteuses ? » — parce que le douteux précipite vers l'illicite "
         "(la leçon 10) ; et l'extraction double : « que l'issue finale appartient à Allah le "
         "Très-Haut », « l'importance du cœur », « l'attachement à la Sunna »."),
        ("L'application traduit le bilan en conduite. Le soin du cœur : « Le soin du cœur, l'effort "
         "vers sa santé et son élévation comptent parmi les plus impérieuses des obligations : je "
         "formule des orientations pour le soin du cœur et sa correction » — les orientations "
         "attendues viennent des listes de la leçon 11, ce qui amende le cœur et ce qui le corrompt. "
         "Puis : « Je propose des conseils à un camarade qui veut savoir comment éviter de tomber "
         "dans les innovations et les répréhensibles » — la sincérité et la conformité à la Sunna de "
         "la leçon 9, « Voici Mon chemin, qui est droit ». Enfin : « Je propose des orientations et "
         "des conseils utiles pour l'éducation de l'âme et son accoutumance aux principes de l'islam "
         "et à ses enseignements de tolérance » — la tolérance boucle la facilité de la leçon 13 : "
         "une religion de facilité et de levée de la gêne ne s'apprend pas dans la contrainte."),
        ("La préparation ouvre la leçon 15 : « Je mémorise le hadīth de la leçon qui vient », puis "
         "deux recherches — « Je recherche l'importance de l'invocation (ad-duʿāʾ) dans l'islam » et "
         "« Je mentionne le rapport entre la consommation du licite et l'invocation » — l'annonce du "
         "dixième hadīth des Quarante, celui du licite et de l'exaucement de l'invocation. Le fil de "
         "lecture est posé : l'homme honoré garde son cœur sain, mange licite, invoque — et est "
         "exaucé. Ce que la consolidation teste : la mémoire du fil (intentions, islām-īmān-iḥsān, "
         "décret, innovations, licite et douteux, cœur, conseil, facilité), l'habileté d'analyse "
         "(expliquer, extraire, appuyer d'un texte), et la mise en situation (conseiller un camarade, "
         "éduquer son âme)."),
    ],
    "points": [
        ("Fil de révision : trois objectifs (évaluer ses acquis ; repérer ses capacités dans "
         "l'analyse ; mettre ses acquis dans des situations nouvelles) → le texte de synthèse "
         "(l'origine : la création honorée) → l'âge de la responsabilité religieuse (foi, obéissance, "
         "soin du cœur) → le bilan des chantiers (usure, douteux, innovations, conseil sincère, "
         "Sunna) → le devenir entre les mains d'Allah → compréhension (expliquer ; contraires) → "
         "analyse (appuyer, expliquer, extraire) → application (orientations, conseils) → iʿdād "
         "(l'invocation et le licite — leçon 15). L'évaluation intégrée à l'analyse : « Pourquoi la "
         "Loi a-t-elle exhorté à la piété de prudence face aux choses douteuses ? »"),
        ("La continuité exacte : la préparation de la leçon 13 demandait « Je lis les textes de la "
         "leçon qui vient, mettant à profit les acquis de mon savoir dans les leçons précédentes pour "
         "répondre aux questions liées au texte » — la leçon 14 est cette lecture : une synthèse, "
         "pas un hadīth nouveau."),
        ("La trajectoire de la création : « de terre, puis a fait son lignage d'une extraction d'eau "
         "vile », « création après création, dans trois ténèbres, jusqu'à paraître en une autre "
         "création » ; ar-Rūm — imprimée 19, porteur 20 (vérifié web) ; « vous vous répandez » "
         "(tantashirūn) ; az-Zumar nomme les trois ténèbres, la leçon 6 expose les étapes "
         "embryonnaires."),
        ("La chaîne des chantiers rouverte clause par clause : « Il a interdit l'usure » ; « l'a "
         "exhorté à la piété de prudence et à l'écart des choses douteuses » (leçon 10) ; « l'a "
         "détourné des innovations et des répréhensibles » (leçon 9) ; « lui a rendu obligatoire le "
         "conseil sincère en vertu de la fraternité de foi » (leçon 12) ; « lui a commandé "
         "l'attachement à la Sunna » (la clause suivante) — la leçon 10 a fait du douteux le seuil "
         "de l'illicite."),
        ("La Sunna arrimée : « Attachez-vous à ma Sunna et à la Sunna des califes bien guidés qui "
         "viendront après moi : mordez-y avec les dents molaires » [Ǧāmiʿ bayān al-ʿilm wa-faḍlihi "
         "d'Ibn ʿAbd al-Barr] — les dents molaires (an-nawāǧiḏ) disent l'arrimage ferme ; les "
         "contraires demandés : la mécréance face à la foi, les égarés face aux bien guidés."),
        ("Le devenir et le décret : « Il a placé son devenir entre Ses mains » ; Muḥammad — imprimée "
         "20, porteur 19 (vérifié web) ; le hadīth de Muslim — « Allah l'a décrété, et ce qu'Il a "
         "voulu, Il l'a fait » — boucle la leçon 8 (qaḍāʾ et qadar) : le décret décharge du regret, "
         "« le “si seulement” ouvre l'œuvre de Satan »."),
        ("Le cœur au centre : « le soin du cœur, qui est la source de son bonheur et de son malheur » "
         "(ash-Shuʿarāʾ 88-89 — référence correcte dans le tirage) ; l'application en fait « les plus "
         "impérieuses des obligations » — les orientations viennent des listes de la leçon 11 (ce "
         "qui amende et ce qui corrompt)."),
        ("La portée de la consolidation : trois objectifs de bilan ; une chaîne récapitulée de "
         "l'honneur de la création à l'attachement à la Sunna ; l'iʿdād qui unit déjà licite et "
         "invocation (« Je mentionne le rapport entre la consommation du licite et l'invocation ») — "
         "la leçon 15 unira ce que la chaîne a séparé."),
    ],
    "vocabulaire": [
        {"ar": "دعم وتطبيق", "translit": "daʿm wa-t-taṭbīq",
         "fr": "le soutien et l'application — le tirage ouvre « Leçon de consolidation et "
               "d'application » ; installée aux leçons 7, 14, 20 et 28 du manuel : « leçon de synthèse "
               "des leçons précédentes », aucun hadīth nouveau, mais la chaîne relue et mise à "
               "l'épreuve."},
        {"ar": "مخلوق مكرم", "translit": "maḫlūq mukarram",
         "fr": "une créature honorée — « L'homme est une créature honorée auprès d'Allah le "
               "Très-Haut », créé de terre puis d'une « extraction d'eau vile » ; l'analyse demande "
               "d'appuyer l'honneur d'un texte religieux."},
        {"ar": "الورع", "translit": "al-waraʿ",
         "fr": "la piété de prudence — « l'a exhorté à la piété de prudence et à l'écart des choses "
               "douteuses » ; la compréhension demande son contraire — la leçon 10 a fait du douteux "
               "le seuil de l'illicite."},
        {"ar": "الشبهات", "translit": "aš-šubahāt",
         "fr": "les choses douteuses — la compréhension demande de les expliquer ; la leçon 10 les a "
               "définies comme le non-tranché entre le licite évident et l'illicite évident, où la "
               "conduite reste une : l'abstention."},
        {"ar": "المهديون", "translit": "al-mahdiyyūn",
         "fr": "les bien guidés — « la Sunna des califes bien guidés qui viendront après moi » ; la "
               "compréhension demande leur contraire — les égarés."},
        {"ar": "النواجذ", "translit": "an-nawāǧiḏ",
         "fr": "les dents molaires — l'image du hadīth de la Sunna : « mordez-y avec les dents "
               "molaires » — l'arrimage ferme à la Sunna du Prophète — prière et salut d'Allah sur "
               "lui — et à celle des califes bien guidés."},
        {"ar": "قدر الله وماشاء فعل", "translit": "qadara llāhu wa-mā šāʾa faʿal",
         "fr": "« Allah l'a décrété, et ce qu'Il a voulu, Il l'a fait » — la formule qui remplace le "
               "regret : dire le décret au lieu du « si seulement », « car le “si seulement” ouvre "
               "l'œuvre de Satan » [Ṣaḥīḥ de Muslim]."},
        {"ar": "تنتشرون", "translit": "tantaširūn",
         "fr": "vous vous répandez — le verbe de l'āya d'ar-Rūm (imprimée 19, porteur 20) : de la "
               "terre à « des hommes qui se répandent sur la terre », l'honneur se lit dans le "
               "verbe."},
    ],
    "avertissement": "Ce commentaire est un guide de lecture du manuel ; en cas de divergence d'expression, le manuel et sa traduction savante font foi.",
}


ENTREES = [('pdf-13', E_13), ('pdf-14', E_14)]


def norme_fr(s):
    s = s.replace('\'', '\u2019')
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
for DOCID in ('pdf-13', 'pdf-14'):
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

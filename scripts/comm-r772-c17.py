#!/usr/bin/env python3
"""R772 — ajoute le commentaire pédagogique de la leçon 17 de hadith-tanawi-1
(13115 عدة المرأة في بيتها ونفقة المطلقة — la retraite dans sa demeure et la
pension de la répudiée, « La retraite dans sa demeure et la pension de la
répudiée (ʿiddat al-marʾa fī baytihā wa-nafaqat al-muṭallaqa) » dans la
traduction du manuel, la dix-septième du livre, étiquetée « leçon 23 » par
l'imprimé (الدرس 23) — le SUIVANT de R771, 13114, annoncé dès R768/R769/R770/R771)
à content/commentaires/hadith-tanawi-1.json.

Même protocole que comm-r771-c16.py : normalisation de la ponctuation FR
(U+202F avant ; : ! ? » et après «, apostrophe courbée) sur l'entrée
nouvelle seulement — opération idempotente. Rédaction d'après la lecture
complète de la leçon (htmlFr intégral, ~30 000 caractères débalisés ; couche
arabe lue en entier pour l'étiquette de l'imprimé « (الدرس 23) » et la date
imprimée en tête (الإثنين 20 ماي 2019)). Règle 2 de LISEZ-MOI.md : aucune
invention — les numéros du Muwaṭṭaʾ (1833, 1834, 1835, 1836, 1837, 1838),
les attributions (Yaḥyā ibn Saʿīd ibn al-ʿĀṣ, ʿAbd ar-Raḥmān ibn al-Ḥakam,
ʿĀʾisha, Marwān ibn al-Ḥakam, Fatima bint Qays, Abū ʿAmr ibn Ḥafṣ, Umm
Sharīk, ʿAbdallāh ibn Umm Maktūm, Muʿāwiya ibn Abī Sufyān, Abū Jahl ibn
Hishām, Usāma ibn Zayd, ʿAbdallāh ibn ʿUmar, Ḥafṣa, Nāfiʿ, la fille de
Saʿīd ibn Zayd, ʿAbdallāh ibn ʿAmr ibn ʿUthmān, Saʿīd ibn al-Musayyab, Yaḥyā
ibn Saʿīd al-Makhzūmī, al-Qāsim ibn Muḥammad, Sulaymān ibn Yasār, Ibn Shihāb
az-Zuhrī, ʿUmar ibn al-Khaṭṭāb, Mālik, ash-Shāfiʿī, Abū Ḥanīfa, Muslim) et
les références (aṭ-Ṭalāq 1 et 6 ; la Mudawwana ; Muslim) sont cités tels
qu'ils figurent dans la leçon.

Garde-fous (convention des vagues R765-R771) :
- verif-citations intégrée : chaque fragment « » de l'entrée doit être
  retrouvé verbatim dans le htmlFr de la leçon (0 manquant, abort sinon) ;
- recoupements : ancres vérifiées dans les leçons voisines (13114 — la
  leçon précédente du registre, les qurūʾ et les cinq maîtres de Médine ;
  13117 — la leçon suivante du registre, le recueil de la retraite du
  divorce, objet de la préparation ; 12992 — la leçon du muḥallil, où la
  forme mubattā fut notée en son temps ; 13649 — la leçon des illicites du
  mariage, où Saʿīd ibn al-Musayyab fut déjà rencontré).
"""
import json, re, sys
import html as H

CHEMIN = 'content/commentaires/hadith-tanawi-1.json'
LIVRE = 'content/books/hadith-tanawi-1.json'
DOCID = '13115'

E_13115 = {
    "auteur": "IA-1, tour R772",
    "resume": (
        "Guide de lecture de la leçon 17 (عدة المرأة في بيتها ونفقة المطلقة — la "
        "retraite de la femme dans sa demeure et la pension de la répudiée ; la "
        "traduction du manuel porte « La retraite dans sa demeure et la pension "
        "de la répudiée (ʿiddat al-marʾa fī baytihā wa-nafaqat al-muṭallaqa) »), "
        "la dix-septième du livre, étiquetée leçon 23 par l'imprimé (الدرس 23) : "
        "trois hadiths du Muwaṭṭaʾ portent la matière — le n° 1833 est le procès "
        "du déplacement : Yaḥyā ibn Saʿīd ibn al-ʿĀṣ avait répudié la fille de "
        "ʿAbd ar-Raḥmān ibn al-Ḥakam « de la répudiation dissolvante (al-batta) », "
        "et son beau-père la fit passer ; ʿĀʾisha, la mère des croyants, envoya à "
        "Marwān ibn al-Ḥakam, alors gouverneur de Médine : « Crains Allah, et "
        "renvoie la femme à sa maison. » ; quand Marwān objecta « Ne t'est-il "
        "point parvenu le cas de Fatima bint Qays ? », ʿĀʾisha répondit « Il ne "
        "te nuit point de ne point mentionner le hadith de Fatima » — et Marwān "
        "de conclure « Si le mal est en toi, il te suffit, du mal, ce qui est "
        "entre ces deux ». Le n° 1835 est le tableau du scrupule : "
        "ʿAbdallāh ibn ʿUmar répudia une femme de ses femmes « dans la demeure de "
        "Ḥafṣa », qui était son chemin vers la mosquée — « il prit alors l'autre "
        "voie, par les derrières des maisons, par répugnance à lui demander "
        "l'autorisation, jusqu'à ce qu'il la reprenne ». Le n° 1837, pilier du "
        "chapitre (rapporté par Muslim), donne la doctrine : Fatima bint Qays, "
        "répudiée de la répudiation dissolvante alors que son mari était absent "
        "en Syrie, reçut du fondé de pouvoir de l'orge et s'en mécontenta — "
        "devant le Prophète — paix et bénédiction sur lui — la règle tomba : « "
        "Nulle pension (nafaqa) sur lui » — avec l'ordre de compter sa retraite "
        "chez Umm Sharīk, puis « compte ta retraite chez ʿAbdallāh ibn Umm "
        "Maktūm, l'homme aveugle : tu y déposeras tes habits ; quand tu seras "
        "libre (ḥalalti), préviens-moi » ; et sur les deux demandes reçues : « "
        "Quant à Abū (أَبُو) Jahl, il ne quitte point son bâton de son épaule ; "
        "quant à "
        "Muʿāwiya, c'est un ṣuʿlūk sans bien ; épouse Usāma ibn Zayd » — elle "
        "épousa Usāma, et « Dieu y mit du bien, et j'en fus réjouie ». "
        "Le préambule fonde le tout : la retraite est « la durée pendant "
        "laquelle la femme se trouve interdite de mariage après le prononcé du "
        "divorce », en vue de « la vérification légale de la pureté du sein "
        "(barāʾat ar-raḥim) » — et « par considération du droit "
        "du mari, qui peut reprendre son épouse si la répudiation est de la "
        "sorte de la reprise » ; mais « la femme y demeure un être de droits — "
        "logée, nourrie, honorée », et « le temps de l'attente est réglé par la "
        "Loi comme l'est celui du contrat ». La double question de la leçon : "
        "« sur qui sont la demeure et la pension de la femme durant cette durée "
        "? » et « a-t-elle le droit d'y renoncer, comme elle renonce à la "
        "pension qui la précède ? » ; la clef du chapitre est donnée d'emblée : "
        "la Loi « distingue ici, comme ailleurs, ce qui appartient à la femme de "
        "ce qui appartient à Dieu — distinction qui est le secret de tout le "
        "chapitre ». "
        "Première partie — la demeure. L'accord : la « répudiée de la "
        "répudiation de la reprise (rajʿiyya) a la demeure et la pension » — "
        "« car elle est en la position de l'épouse », « tant qu'elle n'a point "
        "quitté l'inviolabilité (ʿiṣma) ». La divergence porte sur la mubtūta — "
        "la répudiée de la troisième : Mālik, ash-Shāfiʿī et la plupart des gens "
        "du Ḥijāz lui donnent la demeure, par le verset 6 de aṭ-Ṭalāq — « Et "
        "faites que ces femmes habitent où vous habitez, et suivant vos moyens. "
        "Et ne cherchez pas à leur nuire en les contraignant à vivre à "
        "l'étroit. » — où « l'ordre est pour l'obligation (wujūb) », et "
        "l'entendu vise « celles qui se sont séparées de leurs maris », toutes "
        "les répudiées et non les seules enceintes. Le régime du séjour : pas de déplacement ni de nuit ailleurs, mais « il lui est permis "
        "de sortir le jour, contrairement à Abū (أَبُو) Ḥanīfa » — « la demeure "
        "est une garde, non une prison ; la Loi enferme le mouvement de la nuit "
        "et laisse le jour aux nécessités de la vie ». L'épisode dʿĀʾisha et de "
        "Marwān prouve que le séjour est contraignable : « la mère des croyants "
        "n'aurait point mobilisé l'autorité publique pour ce qui ne serait "
        "qu'une recommandation » ; le hadith de Fatima y est explicité comme "
        "sorti pour cause — « la sortie de Fatima ne fut licite que parce "
        "qu'elle était en un lieu effrayant, et l'on craignit pour elle » — d'où "
        "la règle : « l'exception nommée par le Prophète est une cause, et la "
        "cause se raisonne ; là où la cause se retrouve, l'exception la suit ». "
        "Deux confirmations : le n° 1834 — la fille de Saʿīd ibn Zayd qui se "
        "déplaça sans excuse : « le reproche d'Ibn ʿUmar vise l'absence de "
        "cause, non le mouvement lui-même » ; le n° 1836 — Saʿīd ibn "
        "al-Musayyab au loyer de la maison de retraite : « sur son mari », puis "
        "« sur elle », puis « sur l'émir » — « le dernier garant est l'État, "
        "jamais le vide ». Et le fondement dernier : la demeure est « un droit "
        "d'Allah » "
        "au verset 1 — « Ne les faites pas sortir de leurs maisons, et qu'elles "
        "n'en sortent pas, à moins qu'elles n'aient commis une turpitude "
        "prouvée. Telles sont les lois d'Allah. » — « le séjour est une borne "
        "(ḥadd (حَدٌّ)) dressée par le Législateur, et les bornes de Dieu ne se "
        "négocient point » ; elles « gardent les honneurs des femmes et la "
        "pureté des lignages, qui sont des biens de la communauté tout "
        "entière ». La leçon ajoute le statut de l'entrée du mari chez la "
        "répudiée de la reprise : dans la Mudawwana, « point de mal à ce qu'il "
        "entre auprès d'elle et mange avec elle s'il y a auprès d'elle quelqu'un "
        "qui veille sur elle », puis le retrait jusqu'à la reprise ; le n° 1835 "
        "devient « la photographie vivante du waraʾ médinois » : « la loi "
        "autorisait, le cœur choisit le plus scrupuleux » — « la permission "
        "n'est point l'invite ». "
        "Deuxième partie — la pension. Point de divergence pour la rajʿiyya : "
        "« la répudiée de la répudiation de la reprise a la pension et les "
        "autres charges sur son mari, enceinte qu'elle fût ou non » ; toute la divergence "
        "porte sur la mubtūta non enceinte : les Mālikites et les Shāfiʿites la "
        "refusent par l'implicite contraire (mafhūm mukhālaf) du verset 6 — la "
        "demeure ordonnée d'une face générale, la pension spécialisée aux "
        "enceintes — « la demeure lui demeure, l'entretien s'envole avec le "
        "lien qui le fondait » — et par le « texte établi (naṣṣ thābit) que la "
        "mubtūta n'a point de pension sur son mari qui l'a répudiée de la "
        "troisième, si elle n'est point enceinte » : « la mubtūta a le toit, non "
        "le blé » ; les Ḥanafites l'accordent — « qu'elle est retenue (maḥbūsa) "
        "à cause de lui », l'analogie sur la demeure, et la parole dʿUmar ibn "
        "al-Khaṭṭāb rapportée par Muslim : « nous ne laisserons point le Livre "
        "de Dieu et la Sunna de notre Prophète pour la parole d'une femme — "
        "nous ne savons si elle a conservé ou oublié ». Les réponses malikites "
        "déplient la méthode : la chaîne dʿUmar est récusée — la « Sunna » "
        "alléguée n'est point conservée (ghayr maḥfūẓ) —, « la prudence ne "
        "transforme point l'implicite du Livre » ; l'analogie est « une analogie "
        "avec différence présente (qiyās (قياس) maʿa l-fāriq) » — « la cause de "
        "la pension est la maîtrise (tamkīn), et elle est nulle ici », « la "
        "cause de la demeure est la retenue hors du mouvement (al-ḥabs ʿan "
        "at-taṣarruf), et elle est présente » — « La pension paie la possession "
        "perdue ; la demeure paie la garde encore due », et « l'analogie qui "
        "les confond raisonne sur les mots et néglige les causes » ; l'épouse "
        "n'est point retenue à cause du mari — « elle s'est déjà séparée de lui "
        "(bānat minh) » — mais « elle est retenue pour le lignage (an-nasab) ». "
        "Et la distinction mère de tout le "
        "chapitre : la pension est un droit de l'épouse — « elle a le droit d'y "
        "renoncer avant le divorce et après » ; point de renoncement pour la "
        "demeure, « un droit d'Allah » — « la pension suit la personne et se "
        "négocie ; la demeure suit la borne divine et se garde. La femme peut "
        "pardonner l'or qu'on lui doit ; elle ne peut point défaire la garde "
        "que Dieu a dressée autour de son honneur et de celui des "
        "générations. » "
        "Le hadith de Fatima verse enfin quatre jugements au chapitre : la "
        "licéité de l'allusion par la demande en mariage (taʿrīḍ) dans la "
        "retraite — « quand tu seras libre, préviens-moi », et dans une version "
        "« ne me manque point de toi-même » — car « l'allusion est permise là "
        "où l'explicite troublerait » ; la considération du bien du mari — « la "
        "Loi ne méprise point le pain dans le mariage » ; la licéité de la demande sur la demande si elle n'est "
        "point conclue (murākana) — « la demande n'est point un lien tant que "
        "le consentement n'a point figé l'engagement » ; et la licéité de "
        "mentionner les défauts de l'homme pour la nécessité du conseil, hors "
        "médisance (ghība) — « la dureté d'Abū (أَبُو) Jahl est dite non pour "
        "l'abaisser, mais pour guider la femme qui s'apprête à lui confier sa "
        "vie », « la vérité utile au conseil n'est point la médisance "
        "interdite, et le besoin d'y voir clair légitime le mot dur ». "
        "L'exploitation scelle le tout par le n° 1838 : Ibn Shihāb az-Zuhrī — « "
        "La mubtūta ne sort point de sa maison jusqu'à ce qu'elle devienne "
        "libre, et elle n'a point de pension — sauf qu'elle soit enceinte : on "
        "l'entretient alors jusqu'à ce qu'elle mette au monde son fardeau » — "
        "et Mālik : « et cet ordre est le nôtre » ; « la parole du Successeur "
        "médinois devient la lettre de l'école », et l'équilibre du droit se "
        "résume : « protégée dans son séjour, mesurée dans son entretien » — "
        "« le toit est une garde divine, le blé suit la possession perdue ou le "
        "fardeau porté ». La préparation ouvre la leçon suivante (13117, le "
        "recueil de la retraite du divorce) : expliquer « ses menstrues se sont "
        "levées » (rafʿat ḥayḍatuhā) et « la répudiée de la troisième » (battu "
        "ṭalāqihā), et indiquer par quoi compte celle qui ne menstrue point. "
        "Les notes du traducteur : cinq emplacements de versets en image, tous "
        "vides au scan et restaurés verbatim au cache coranique, les références "
        "imprimées toutes concordantes ; le lemme « celles qui se sont séparées "
        "de leurs maris » suivi contre la version anglaise ; la glose nommant "
        "la femme déplacée ʿAmra bint ʿAbd ar-Raḥmān rendue par « la fille de "
        "ʿAbd ar-Raḥmān », sans étendre l'erreur du lemme ; les chaînes — "
        "Yaḥyā ibn Saʿīd al-Makhzūmī, le juge de Médine, d'al-Qāsim ibn "
        "Muḥammad et de Sulaymān ibn Yasār, deux des cinq maîtres — et la "
        "terminologie (mubtūta, la forme juste du texte arabe)."
    ),
    "explication": [
        "La leçon 17 succède aux qurūʾ (leçon 16, n° 1823-1832) et déplace la caméra : la précédente réglait le temps du compte — les cycles qui mesurent la retraite —, celle-ci règle le lieu et l'entretien — le toit sous lequel la répudiée compte et le blé dont elle vit. Le titre double — la demeure, la pension — annonce la structure : deux statuts, une même question du droit. La vingt-troisième leçon de l'imprimé (الدرس 23) poursuit le fil — connaître le statut du logement et de la pension, saisir le dire de Mālik et sa preuve, comprendre les droits légaux de la femme.",
        "Le préambule donne la double sagesse de la retraite : « la durée pendant laquelle la femme se trouve interdite de mariage après le prononcé du divorce » sert d'abord « la vérification légale de la pureté du sein (barāʾat ar-raḥim) » — « qu'aucune grossesse ne soit dissimulée dans un lignage qui ne serait point le sien » — puis « par considération du droit du mari, qui peut reprendre son épouse si la répudiation est de la sorte de la reprise ». Mais l'attente n'est pas un vide juridique : « la femme y demeure un être de droits — logée, nourrie, honorée », et « le temps de l'attente est réglé par la Loi comme l'est celui du contrat ». La clef du chapitre est posée d'emblée : la Loi « distingue ici, comme ailleurs, ce qui appartient à la femme de ce qui appartient à Dieu — distinction qui est le secret de tout le chapitre ».",
        "Le n° 1833 est un procès en règle : Yaḥyā ibn Saʿīd ibn al-ʿĀṣ — de la maison omeyyade, gendre dʿAbd ar-Raḥmān ibn al-Ḥakam — avait répudié sa femme « de la répudiation dissolvante (al-batta) », et le beau-père « la fit passer » ; ʿĀʾisha écrit à Marwān — le père du répudié lui-même et l'oncle de la femme déplacée — « Crains Allah, et renvoie la femme à sa maison » : l'autorité publique est récusée dans sa propre maison ; quand Marwān objecte le précédent de Fatima bint Qays, ʿĀʾisha refuse la généralisation — « Il ne te nuit point de ne point mentionner le hadith de Fatima » — et Marwān retourne l'argument : « Si le mal est en toi, il te suffit, du mal, ce qui est entre ces deux » — « l'excuse que la leçon reconnaît à l'une vaut à l'autre ». La leçon tire la règle de l'échange : le hadith de Fatima fut pour une cause (li-ʿilla) — « la sortie de Fatima ne fut licite que parce qu'elle était en un lieu effrayant, et l'on craignit pour elle » — et la cause se raisonne : « l'exception nommée par le Prophète est une cause, et la cause se raisonne ; là où la cause se retrouve, l'exception la suit ».",
        "Le même échange prouve le port juridique du logement : la mère des croyants n'aurait point mobilisé le gouverneur de Médine pour une recommandation — « la mère des croyants n'aurait point mobilisé l'autorité publique pour ce qui ne serait qu'une recommandation ». Le logement de la retraite est donc une obligation exécutable, non un souhait pieux. Le n° 1834 le confirme par le négatif : la fille de Saʿīd ibn Zayd — mariée à ʿAbdallāh ibn ʿAmr ibn ʿUthmān ibn ʿAffān, répudiée de la batta , qui se déplaça sans excuse — récit porté par Nāfiʿ — porte le reproche d'Ibn ʿUmar: « le reproche d'Ibn ʿUmar vise l'absence de cause, non le mouvement lui-même ». Le n° 1836 le confirme par l'économie : interrogé sur le loyer d'une maison où le mari répudia sa femme, Saʿīd ibn al-Musayyab répond « sur son mari », puis « sur elle », puis « sur l'émir » — la gradation trace « la chaîne des garanties : le mari, la femme, le trésor public — le dernier garant est l'État, jamais le vide » ; et celui qui oblige au loyer ne tient point le séjour pour une recommandation — « la femme répudiée ne se trouve jamais sans toit payé ».",
        "Le statut, ensuite. L'accord des savants : la « répudiée de la répudiation de la reprise (rajʿiyya) a la demeure et la pension » — « car elle est en la position de l'épouse », « tant qu'elle n'a point quitté l'inviolabilité (ʿiṣma) » ; la reprise reste possible, le foyer demeure ce qu'il était. La divergence porte sur la mubtūta — la répudiée de la troisième : Mālik, ash-Shāfiʿī et la plupart des gens du Ḥijāz lui donnent la demeure, à la parole du Très-Haut « Et faites que ces femmes habitent où vous habitez, et suivant vos moyens. Et ne cherchez pas à leur nuire en les contraignant à vivre à l'étroit. » [la sourate aṭ-Ṭalāq, verset 6] — « l'ordre est pour l'obligation (wujūb) », principe déjà traversé à la leçon précédente ; et l'entendu du verset vise « celles qui se sont séparées de leurs maris » — toutes les répudiées, non les seules enceintes : le lemme lexical est ici un pilier doctrinal, et les notes du traducteur le sauvegardent contre la version anglaise.",
        "Deuxième partie — la pension. L'accord d'abord : « la répudiée de la répudiation de la reprise a la pension et les autres charges sur son mari, enceinte qu'elle fût ou non ». La divergence porte sur la mubtūta non enceinte. Les Mālikites et les Shāfiʿites la refusent : le verset 6 ordonne la demeure d'une face générale et spécialise la pension aux enceintes — l'implicite contraire (mafhūm mukhālaf) dénote la non-pension de la non-enceinte — « la demeure lui demeure, l'entretien s'envole avec le lien qui le fondait » ; et le hadith de Fatima est « texte établi (naṣṣ thābit) que la mubtūta n'a point de pension sur son mari qui l'a répudiée de la troisième, si elle n'est point enceinte » : la demande de Fatima était juste en son instinct, et le Prophète la redresse en fixant la règle — « la mubtūta a le toit, non le blé ».",
        "Les Ḥanafites accordent la pension : « qu'elle est retenue (maḥbūsa) à cause de lui » — l'analogie porte de la demeure à la pension — et la parole dʿUmar ibn al-Khaṭṭāb rapportée par Muslim : « nous ne laisserons point le Livre de Dieu et la Sunna de notre Prophète pour la parole d'une femme — nous ne savons si elle a conservé ou oublié ». Les réponses malikites déplient la méthode du fiqh : la chaîne alléguée n'est point conservée (ghayr maḥfūẓ) et « la prudence ne transforme point l'implicite du Livre » ; l'analogie est « une analogie avec différence présente (qiyās (قياس) maʿa l-fāriq) » — « la cause de la pension est la maîtrise (tamkīn), et elle est nulle ici », « la cause de la demeure est la retenue hors du mouvement (al-ḥabs ʿan at-taṣarruf), et elle est présente » : « La pension paie la possession perdue ; la demeure paie la garde encore due », et « l'analogie qui les confond raisonne sur les mots et néglige les causes » ; l'épouse n'est point retenue à cause du mari — « elle s'est déjà séparée de lui (bānat minh) » — mais « elle est retenue pour le lignage (an-nasab) ».",
        "Le hadith de Fatima verse enfin quatre jugements au chapitre : la licéité de l'allusion par la demande en mariage (taʿrīḍ) dans la retraite — « quand tu seras libre, préviens-moi », et dans une version « ne me manque point de toi-même » — car « l'allusion est permise là où l'explicite troublerait » ; la considération du bien du mari au mariage — « la Loi ne méprise point le pain dans le mariage » ; la licéité de la demande sur la demande si elle n'est point conclue (murākana) — « la demande n'est point un lien tant que le consentement n'a point figé l'engagement » ; et la licéité de mentionner les défauts de l'homme pour la nécessité du conseil, hors médisance (ghība) — « la dureté d'Abū (أَبُو) Jahl est dite non pour l'abaisser, mais pour guider la femme qui s'apprête à lui confier sa vie » : « la vérité utile au conseil n'est point la médisance interdite, et le besoin d'y voir clair légitime le mot dur ».",
        "L'exploitation scelle : le n° 1838 rassemble la doctrine en deux phrases d'Ibn Shihāb az-Zuhrī — « La mubtūta ne sort point de sa maison jusqu'à ce qu'elle devienne libre, et elle n'a point de pension — sauf qu'elle soit enceinte : on l'entretient alors jusqu'à ce qu'elle mette au monde son fardeau » — et Mālik la fait sienne : « et cet ordre est le nôtre » ; « la parole du Successeur médinois devient la lettre de l'école ». L'équilibre du droit de la femme en retraite se résume : « protégée dans son séjour, mesurée dans son entretien » — « le toit est une garde divine, le blé suit la possession perdue ou le fardeau porté ». La préparation ouvre la leçon suivante (13117, le recueil de la retraite du divorce) : expliquer « ses menstrues se sont levées » (rafʿat ḥayḍatuhā) et « la répudiée de la troisième » (battu ṭalāqihā), et indiquer par quoi compte celle qui ne menstrue point. Les notes du traducteur sauvegardent l'appareil : cinq emplacements de versets en image, tous vides au scan et restaurés verbatim au cache coranique ; les références imprimées (aṭ-Ṭalāq 6 à trois emplacements, aṭ-Ṭalāq 1 à deux) toutes concordantes — aucun écart nouveau au registre ; le lemme « celles qui se sont séparées de leurs maris » suivi contre la version anglaise ; la glose du manuel nommant la femme déplacée ʿAmra bint ʿAbd ar-Raḥmān — que le n° 1833 ne nomme point — rendue par « la fille de ʿAbd ar-Raḥmān », sans étendre l'erreur du lemme ; les chaînes (Yaḥyā ibn Saʿīd al-Makhzūmī, le juge de Médine, d'al-Qāsim ibn Muḥammad et de Sulaymān ibn Yasār — deux des cinq maîtres de Médine) ; la terminologie enfin — mubtūta, la forme juste du texte arabe, là où la leçon du muḥallil notait mubattā ; al-batta, la répudiation dissolvante ; rajʿiyya et bāʾin, déjà établies.",
    ],
    "points": [
        "Fil du livre : après le temps du compte (leçon 16, les qurūʾ), le lieu et l'entretien — le titre double (la demeure, la pension) annonce deux statuts et une seule question du droit : ce qui appartient à la femme se renonce, ce qui appartient à Dieu se garde.",
        "Le préambule : la retraite est « la durée pendant laquelle la femme se trouve interdite de mariage après le prononcé du divorce » — pour « la vérification légale de la pureté du sein (barāʾat ar-raḥim) » ; « la femme y demeure un être de droits — logée, nourrie, honorée ».",
        "Le n° 1833 : le procès du déplacement — ʿĀʾisha à Marwān « Crains Allah, et renvoie la femme à sa maison » ; la réplique « Il ne te nuit point de ne point mentionner le hadith de Fatima » ; la balance « Si le mal est en toi, il te suffit, du mal, ce qui est entre ces deux » ; la règle du chapitre : « l'exception nommée par le Prophète est une cause, et la cause se raisonne ; là où la cause se retrouve, l'exception la suit ».",
        "Le n° 1835 : le waraʾ médinois — la demeure de Ḥafṣa était le chemin de mosquée d'Ibn ʿUmar ; « il prit alors l'autre voie, par les derrières des maisons, par répugnance à lui demander l'autorisation, jusqu'à ce qu'il la reprenne » ; « la loi autorisait, le cœur choisit le plus scrupuleux » — « la permission n'est point l'invite ».",
        "Le n° 1837 : Fatima bint Qays — répudiée de la batta, l'orge du fondé de pouvoir refusée, la règle « Nulle pension (nafaqa) sur lui » ; le déplacement pour cause (Umm Sharīk, puis « compte ta retraite chez ʿAbdallāh ibn Umm Maktūm, l'homme aveugle ») ; le conseil sur les prétendants — « il ne quitte point son bâton de son épaule », « c'est un ṣuʿlūk sans bien » — et le mariage avec Usāma ibn Zayd ; rapporté par Muslim, contesté par Abū Ḥanīfa.",
        "La demeure : ijmāʿ pour la rajʿiyya (« car elle est en la position de l'épouse ») ; Mālik, ash-Shāfiʿī et la plupart des gens du Ḥijāz donnent la demeure à la mubtūta par le verset 6 — « l'ordre est pour l'obligation (wujūb) », visant « celles qui se sont séparées de leurs maris » ; sortie du jour permise — « la demeure est une garde, non une prison ».",
        "Les confirmations : le n° 1834 (le reproche d'Ibn ʿUmar — « l'absence de cause, non le mouvement lui-même ») ; le n° 1836 (la gradation de Saʿīd ibn al-Musayyab — « sur son mari », « sur elle », « sur l'émir » : « le dernier garant est l'État, jamais le vide »).",
        "La borne divine : la demeure est « un droit d'Allah » au verset 1 — « Ne les faites pas sortir de leurs maisons, et qu'elles n'en sortent pas, à moins qu'elles n'aient commis une turpitude prouvée. Telles sont les lois d'Allah. » — « le séjour est une borne (ḥadd (حَدٌّ)) dressée par le Législateur, et les bornes de Dieu ne se négocient point » ; réponse au contrôle : la femme ne renonce point à la demeure.",
        "La pension : accord pour la rajʿiyya (« enceinte qu'elle fût ou non ») ; divergence pour la mubtūta non enceinte — Mālikites et Shāfiʿites la refusent (mafhūm mukhālaf du verset 6 ; le naṣṣ thābit de Fatima : « la mubtūta a le toit, non le blé »), Ḥanafites l'accordent (maḥbūsa à cause de lui ; la parole dʿUmar rapportée par Muslim).",
        "Les réponses malikites : la chaîne dʿUmar récusée (ghayr maḥfūẓ) — « la prudence ne transforme point l'implicite du Livre » ; le qiyās maʿa l-fāriq — « la cause de la pension est la maîtrise (tamkīn), et elle est nulle ici », « la cause de la demeure est la retenue hors du mouvement (al-ḥabs ʿan at-taṣarruf), et elle est présente » — « La pension paie la possession perdue ; la demeure paie la garde encore due ».",
        "La distinction mère du chapitre : la pension, droit de l'épouse, « elle a le droit d'y renoncer avant le divorce et après » ; la demeure, droit d'Allah, ne se renonce point — « la pension suit la personne et se négocie ; la demeure suit la borne divine et se garde. La femme peut pardonner l'or qu'on lui doit ; elle ne peut point défaire la garde que Dieu a dressée autour de son honneur et de celui des générations. »",
        "Les quatre jugements du hadith de Fatima : l'allusion (taʿrīḍ) permise dans la retraite ; la considération du bien du mari — « la Loi ne méprise point le pain dans le mariage » ; la demande sur la demande non conclue (murākana) ; la vérité utile au conseil hors médisance (ghība) — « le besoin d'y voir clair légitime le mot dur ».",
        "L'exploitation : le n° 1838 (Ibn Shihāb az-Zuhrī) rassemble la doctrine — la mubtūta tenue à la maison, libérée de la pension, sauf l'enceinte entretenue jusqu'à la mise au monde — et Mālik : « et cet ordre est le nôtre » ; « le toit est une garde divine, le blé suit la possession perdue ou le fardeau porté » ; la préparation ouvre 13117 (le recueil de la retraite du divorce).",
    ],
    "vocabulaire": [
        {"ar": "العدة", "translit": "al-ʿidda",
         "fr": "la retraite : « la durée pendant laquelle la femme se trouve interdite de mariage après le prononcé du divorce » — pour « la vérification légale de la pureté du sein (barāʾat ar-raḥim) » et « par considération du droit du mari, qui peut reprendre son épouse si la répudiation est de la sorte de la reprise » ; « le temps de l'attente est réglé par la Loi comme l'est celui du contrat »"},
        {"ar": "السكنى", "translit": "as-suknā",
         "fr": "le logement : le premier statut de la leçon — l'accord pour la rajʿiyya, la preuve malikite par le verset 6 : « Et faites que ces femmes habitent où vous habitez, et suivant vos moyens. Et ne cherchez pas à leur nuire en les contraignant à vivre à l'étroit. » — « l'ordre est pour l'obligation (wujūb) », visant « celles qui se sont séparées de leurs maris » ; « la demeure est une garde, non une prison »"},
        {"ar": "النفقة", "translit": "an-nafaqa",
         "fr": "la pension : « Nulle pension (nafaqa) sur lui » — la mubtūta non enceinte n'a point de pension chez les Mālikites et les Shāfiʿites ; « La pension paie la possession perdue ; la demeure paie la garde encore due » ; droit de l'épouse — « elle a le droit d'y renoncer avant le divorce et après »"},
        {"ar": "الرجعية", "translit": "ar-rajʿiyya",
         "fr": "la répudiée de la reprise : « la répudiée de la répudiation de la reprise (rajʿiyya) a la demeure et la pension » — « car elle est en la position de l'épouse », « tant qu'elle n'a point quitté l'inviolabilité (ʿiṣma) » ; le foyer demeure ce qu'il était, la reprise reste possible"},
        {"ar": "البائن", "translit": "al-bāʾin",
         "fr": "la dissolvante : la répudiée du divorce détachant, dont la leçon du muḥallil a établi le régime ; la mubtūta — la répudiée de la troisième — est la bāʾin en sa retraite : elle a le toit, non le blé ; la forme mubattā, notée en son temps à la leçon du muḥallil, est ici corrigée en la forme juste mubtūta"},
        {"ar": "الورع", "translit": "al-waraʾ",
         "fr": "la piété scrupuleuse : « la photographie vivante du waraʾ médinois » — le détour d'Ibn ʿUmar par les derrières des maisons pendant sa retraite dans la demeure de Ḥafṣa ; « la loi autorisait, le cœur choisit le plus scrupuleux » — « la permission n'est point l'invite »"},
        {"ar": "الحبس", "translit": "al-ḥabs",
         "fr": "la retenue : « la cause de la demeure est la retenue hors du mouvement (al-ḥabs ʿan at-taṣarruf), et elle est présente » — et l'épouse n'est point retenue à cause du mari : « elle s'est déjà séparée de lui (bānat minh) » ; « elle est retenue pour le lignage (an-nasab) »"},
        {"ar": "التمكين", "translit": "at-tamkīn",
         "fr": "la maîtrise : « la cause de la pension est la maîtrise (tamkīn), et elle est nulle ici » — la possession conjugale que le divorce a levée ; son implicite contraire au verset 6 fonde la spécialisation de la pension aux enceintes"},
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
com[DOCID] = norme_entree(E_13115)

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
    ('13114 — la leçon précédente du registre (les qurūʾ et les cinq maîtres de Médine)', 'qurūʾ' in fr('13114') and 'cinq maîtres' in fr('13114')),
    ('13117 — la leçon suivante du registre (le recueil de la retraite du divorce, objet de la préparation)', 'menstrue' in fr('13117')),
    ('12992 — la leçon du muḥallil, où la forme mubattā fut notée en son temps', 'muḥallil' in fr('12992')),
    ('13649 — la leçon des illicites du mariage, où Saʿīd ibn al-Musayyab fut déjà rencontré', 'Musayyab' in fr('13649')),
    ('13115 — le logement et la nafaqa dans la leçon même', 'logement' in corpus and 'nafaqa' in corpus),
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

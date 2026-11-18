#!/usr/bin/env python3
"""R739 — ajoute les commentaires pédagogiques des leçons 11-12 de hadith-tanawi-1
(12991 الصداق: حُكمه ومقاصده — la sagesse et les objectifs de la dot, la onzième
du livre, étiquetée « (leçon 2) » par l'imprimé ;
12992 ما لا يجوز في الزواج من الشروط ونكاح المحلل — les conditions illicites dans
le mariage et le nikāḥ al-muḥallil, la douzième du livre, étiquetée « la
quatrième leçon » par l'imprimé)
à content/commentaires/hadith-tanawi-1.json.
Vague 21 : les slots exacts 12991=leçon 11 et 12992=leçon 12 (le SUIVANT de
R737, vérifié dans l'ordre des lessons du registre : 12925, 12934, 12936,
12957, 12959, 12966, 12967, 12971, 12981, 12990, puis 12991 et 12992). Même
protocole que comm-r736.py : normalisation de la ponctuation FR (U+202F avant
; : ! ? » et après «, apostrophe courbée) sur les entrées nouvelles seulement —
opération idempotente. Rédaction d'après la lecture complète des deux leçons
(htmlFr intégral, 13 913 et 14 972 caractères ; extraction non lossy
scripts/extrait-r739.py, couche arabe lue pour les formes du vocabulaire et
pour les rubriques que la couche FR de la leçon 12992 ne rend pas — التقويم,
الاستثمار et الإعداد القبلي absents de la couche FR, consigné au worklog,
règle 5 : la zone est celle d'IA-3). Les numéros du Muwaṭṭaʾ (1643, 1644,
1645 ; 1659, 1660, 1661, 1663, 1664), les citations (Sahl ibn Saʿd as-Sāʿidī,
Abū Ḥāzim ibn Dīnār, ʿUmar, az-Zurqānī, Abū ʿUbayd, al-Māzarī, ʿIyāḍ,
aṭ-Ṭaḥāwī, al-Abharī, al-Layth, Makḥūl, Abū an-Nuʿmān al-Azdī, Ibn Masʿūd,
Saʿīd ibn al-Musayyab, Ibn ʿAbd al-Barr, ʿAlī, Rifāʿa ibn Simwāl, Tamīma bint
Wahb, ʿAbd ar-Raḥmān ibn az-Zubayr, la houppette, « je la secoue comme on
secoue le cuir tanné », al-Ḥasan, Abū ʿUmar, Ibn al-ʿArabī, al-Ubbī,
al-Qāsim ibn Muḥammad, Umm Bishr bint al-Barrāʾ, aṭ-Ṭabarānī, Muḥammad ibn
ʿArafa, al-Mujādila 1-4, an-Nisāʾ 4, 4:19, 4:21, la sourate al-Māʾida
« verset 6 » imprimée, al-Baqara 228 imprimé restauré au 230), les statuts et
les dits sont cités tels qu'ils figurent dans les leçons (règle 2 de
LISEZ-MOI.md : aucune invention). Les formes arabes du vocabulaire sont
reprises de la couche arabe, sans harakat (règle 3).
"""
import json, re

CHEMIN = 'content/commentaires/hadith-tanawi-1.json'

E_12991 = {
    "auteur": "IA-1, tour R739",
    "resume": (
        "Guide de lecture de la leçon 11 (الصداق: حُكمه ومقاصده — la sagesse et les objectifs de la dot), "
        "la onzième du livre, étiquetée « (leçon 2) » par l'imprimé : un hadith du Muwaṭṭaʾ arme le fond — "
        "le n° 1643, que Mālik rapporte d'Abū Ḥāzim ibn Dīnār, d'après Sahl ibn Saʿd as-Sāʿidī : une femme "
        "vint au Prophète ﷺ et dit « Ô Messager d'Allah, je me dédie (te voue) à toi » ; le Prophète ﷺ "
        "« resta assis un long moment » ; un homme se leva et dit « Ô Messager d'Allah, marie-la à moi, si "
        "tu n'en as pas besoin » ; le Prophète ﷺ demanda « As-tu quelque chose que tu pourrais lui donner "
        "en dot ? » ; l'homme « Je n'ai que ce saroual (vêtement inférieur) » ; le Prophète ﷺ « Si tu lui "
        "donnes cela, tu resteras sans saroual. Cherche donc quelque chose » ; l'homme « Je ne trouve "
        "rien » ; « Cherche, même une bague de fer » ; l'homme chercha sans trouver ; « As-tu quelque "
        "chose du Coran avec toi ? » — « telles et telles sourates qu'il nomma » ; et la sentence « Je "
        "t'ai mariée à elle avec ce que tu as du Coran ». Le tamhīd enracine la leçon : Allah a institué "
        "la dot dans le mariage afin d'honorer l'épouse, de satisfaire son cœur et d'être un témoignage "
        "de la sincérité du mari dans son projet de mariage — « c'est une donation (ḥadaqa) dont le but "
        "est d'établir le lien conjugal sur la base de l'affection (mawadda) et de la miséricorde "
        "(raḥma) » — et cite le verset fondateur « Et donnez aux femmes leurs dot (al-ṣadāqāt) par bonne "
        "grâce » (la sourate an-Nisāʾ, verset 4). L'analyse se déroule en quatre temps. Premièrement, la "
        "définition : la leçon recense les formes du mot dans cinq langues (le pluriel ṣuduq ; la langue "
        "du Ḥijāz ṣadaqa, pluriel ṣadaqāt ; la langue de Tamīm ṣadaqa, pluriel ṣadaqāt « comme ghurfah "
        "(chambre) et ghurafāt (chambres) » ; la cinquième ṣadaqa, pluriel ṣadāq, « comme qaryah "
        "(village) et qurā (villages) » — « le plus correct de ces termes, avec un alif »), puis fixe le "
        "terme : al-ḥibāʾ « signifie le don sans contrepartie », et la dot « est dérivée du mot aṣ-ṣidq "
        "(sincérité) » — « la dot est donc ce que le mari offre à son épouse en raison du mariage, et "
        "c'est un pilier (rukn) de celui-ci ». Deuxièmement, le statut : pilier attesté par « cherche, "
        "même une bague de fer » et par le « marie-la à moi » de l'homme — c'est-à-dire avec une dot : "
        "« il n'a pas dit : “Donne-la-moi en cadeau”, c'est-à-dire marie-la à moi sans dot, car cela "
        "relève des prérogatives du Prophète ﷺ. Il est donc indispensable pour les autres d'avoir une "
        "dot » ; le verset an-Nisāʾ 4 appuie, avec la glose d'Abū ʿUbayd — « “Par bonne grâce” signifie "
        "par le contentement de l'âme pour cette prescription qu'Allah a établie » — et la seconde "
        "citation coranique de la leçon (imprimée « la sourate al-Māʾida, verset 6 ») porte la glose « il "
        "entend par “dot” ici leurs dots » ; az-Zurqānī résout la formule de la femme : « La réalité "
        "n'est pas ce qui est compris » — une personne libre ne peut être possédée, « donc la donatrice "
        "a dit en réalité : “Je me marie à toi sans dot” ». Le cœur technique de la leçon est la face de "
        "la préposition bi dans « avec ce que tu as du Coran » : elle « indique la contrepartie, comme "
        "dans “je te vends mon vêtement contre un dīnār” » — « il ne signifie pas qu'il l'a mariée à "
        "cause de sa mémorisation du Coran » ; al-Māzarī : la bi est causale en l'honneur du Coran, et "
        "l'épouse devient en la valeur de la mariée sans dot — « cela n'est permis qu'à lui, le Prophète "
        "ﷺ ». ʿIyāḍ : « la plus manifeste » des deux faces est que le Prophète ﷺ « lui enseigne ce qu'il "
        "a du Coran, ou une partie de celui-ci, et que son enseignement constitue sa dot » — "
        "interprétation rapportée de Mālik et « utilisée comme argument par ceux qui disent que les "
        "avantages issus de biens peuvent constituer une dot » (Muslim : « Va et enseigne-lui du Coran » "
        "; Abū Dāwūd : « ...enseigne-lui vingt versets »). Le premier avis — aṭ-Ṭaḥāwī, al-Abharī, "
        "al-Layth, Makḥūl : « Ceci est spécifique au Prophète ﷺ », et la bi a ici le sens de la lām — "
        "« pour ce que tu as mémorisé du Coran et que tu es devenu son égal en religion » — rapporté "
        "aussi d'Abū Ḥanīfa, d'Aḥmad et de Mālik ; sa preuve est ce qu'ont rapporté Saʿīd ibn Manṣūr et "
        "Ibn as-Sukn d'Abū an-Nuʿmān al-Azdī, le Compagnon : « Le Prophète ﷺ a marié une femme sur une "
        "sourate du Coran et a dit : “Après toi, il ne sera permis à personne d'avoir une dot.” » Le "
        "deuxième avis — Mālik, ash-Shāfiʿī et d'autres — « autorise de faire de la dot des avantages, "
        "conformément à l'apparent du hadith ». ʿIyāḍ ouvre encore : la dot laissée sans mention — en "
        "compensation (« comme il a expié pour celui qui commet l'acte sexuel en Ramadan et a indemnisé "
        "le tué à Khaybar ») ou par délégation, « afin qu'il s'attache à l'apprentissage du Coran, à la "
        "prééminence de ceux qui le connaissent et à l'intercession par son intermédiaire » — et "
        "conclut : « puisque toutes ces possibilités sont admises, cela ne constitue pas une preuve pour "
        "l'interdiction du mariage sans dot ou avec ce qui n'a pas de valeur » ; le hadith d'Ibn Masʿūd "
        "(ad-Dāraqutnī) — « Je t'ai mariée à elle à la condition que tu l'ensesignes et que tu "
        "l'instruis, et si Allah te fait parvenir des biens, tu la dédommages » — renforce l'hypothèse, "
        "et « le hadith autorise de percevoir une rétribution pour l'enseignement du Coran, et c'est "
        "l'avis de la majorité et des trois Imams ». Troisièmement, les objectifs de la dot, au nombre "
        "de cinq : signifier la noblesse du contrat de mariage ; honorer la femme et préparer "
        "l'établissement du mariage sur la base de l'affection et de l'amour ; être un témoignage de la "
        "sincérité du mari — ce que son nom, dérivé d'aṣ-ṣidq, indique ; aider l'épouse à assumer "
        "certaines nécessités du mariage dont elle a besoin ; distinguer le mariage des relations "
        "illicites. Quatrièmement, les objectifs du hadith : éducatifs — « la considération du plus "
        "âgé pour les intérêts de la communauté et son orientation, par la bienveillance qu'il leur "
        "témoigne » ; dans « Si tu n'en as pas besoin », « la beauté de la bonne conduite envers le "
        "Prophète ﷺ » ; juridiques — « l'épouse ne peut être possédée » (la ḥaqīqa n'est pas voulue) et "
        "« la dot dans le mariage est un droit d'Allah, le Très-Haut, et il n'est pas permis de "
        "s'entendre pour y renoncer ». L'évaluation demande le statut de la dot avec sa preuve et ses "
        "objectifs. L'istiṯmār arme la leçon de deux textes du Muwaṭṭaʾ : le n° 1644 — ʿUmar ibn "
        "al-Khaṭṭāb, d'après Saʿīd ibn al-Musayyab (par Yaḥyā ibn Saʿīd) : « Quiconque se marie une "
        "femme atteinte de folie, de lèpre ou de lèpre blanche, et qu'il a eu des relations avec elle, a "
        "droit à sa dot en totalité. Et cela est une dette pour son mari envers son tuteur (walī) » ; le "
        "n° 1645 — Mālik limite le ghurm au cas où le tuteur qui l'a mariée « est son père, son frère ou "
        "celui qui est considéré comme étant au courant de son état » ; sinon « il n'est pas redevable » "
        "— « et cette femme doit rendre ce qu'elle a reçu comme dot, et on laisse pour elle ce qui peut "
        "être licitement consommé » ; l'exercice demande le statut de la dot quand le vice est "
        "inconnu. La préparation préalable — « Connais le don gratuit (al-ḥibāʾ) » — annonce la leçon de "
        "la dot et du ḥibāʾ : étiquetée leçon 3 du manuel mais placée avant celle-ci dans le livre — le "
        "chaînage interne de l'imprimé suit son propre ordre (leçon 2 → leçon 3 → leçon 4), et chaque "
        "préparation préalable appelle la leçon suivante du manuel, non la leçon suivante du livre."),
    "explication": [
        ("La leçon 11 — la onzième du livre, étiquetée « (leçon 2) » par l'imprimé — porte la sagesse et "
         "les objectifs de la dot (الصداق: حُكمه ومقاصده). Trois objectifs l'ouvrent : connaître le "
         "statut de la dot (al-ṣadāq) dans le mariage ; distinguer le concept de la dot de celui du don "
         "gratuit (al-ḥibāʾ) ; comprendre les objectifs de la dot. Le tamhīd donne le sens général : "
         "« Allah, le Très-Haut, a institué la dot dans le mariage afin d'honorer l'épouse, de satisfaire "
         "son cœur et d'être un témoignage de la sincérité du mari dans son projet de mariage » — « c'est "
         "une donation (ḥadaqa) dont le but est d'établir le lien conjugal sur la base de l'affection "
         "(mawadda) et de la miséricorde (raḥma) » — et cite le verset fondateur : « Et donnez aux femmes "
         "leurs dot (al-ṣadāqāt) par bonne grâce » (la sourate an-Nisāʾ, verset 4). Le tamhīd se clôt sur "
         "les deux questions que l'analyse va traiter : « Alors, qu'est-ce que la dot ? Quel est son "
         "statut et quels sont ses objectifs ? »"),
        ("Le texte fondateur est le hadith de Sahl ibn Saʿd as-Sāʿidī, que Mālik rapporte d'Abū Ḥāzim ibn "
         "Dīnār (Muwaṭṭaʾ n° 1643). Une femme vint au Prophète ﷺ et dit : « Ô Messager d'Allah, je me "
         "dédie (te voue) à toi » — le Prophète ﷺ « resta assis un long moment ». Un homme se leva : « Ô "
         "Messager d'Allah, marie-la à moi, si tu n'en as pas besoin. » La question du Prophète ﷺ revient "
         "comme un seuil : « As-tu quelque chose que tu pourrais lui donner en dot ? » L'homme : « Je "
         "n'ai que ce saroual (vêtement inférieur). » — « Si tu lui donnes cela, tu resteras sans "
         "saroual. Cherche donc quelque chose. » — « Je ne trouve rien. » — « Cherche, même une bague de "
         "fer. » L'homme chercha sans trouver. Alors la dernière question : « As-tu quelque chose du "
         "Coran avec toi ? » — « Oui, telles et telles sourates qu'il nomma » — et la sentence : « Je "
         "t'ai mariée à elle avec ce que tu as du Coran. » Le récit monte en gradation — le vêtement dont "
         "il resterait dépourvu en le donnant, le fer le plus humble, enfin le bien qui n'est pas un "
         "bien : le Coran — et chaque degré dit la même chose : le mariage ne se conclut pas sans dot ; "
         "quand rien ne reste à donner, la parole apprise tient lieu de dot."),
        ("L'analyse ouvre par la note lexicographique : la leçon recense les formes du mot dans cinq "
         "langues — un pluriel ṣuduq ; la langue du Ḥijāz ṣadaqa avec le dāl marqué, pluriel ṣadaqāt ; "
         "la langue de Tamīm ṣadaqa, pluriel ṣadaqāt « comme ghurfah (chambre) et ghurafāt (chambres) » ; "
         "la cinquième ṣadaqa, pluriel ṣadāq, « comme qaryah (village) et qurā (villages) » — « le plus "
         "correct de ces termes, avec un alif, est de lui donner sa dot ». Face à la dot, le terme "
         "al-ḥibāʾ « signifie le don sans contrepartie » ; et la dot « est dérivée du mot al-ṣidq "
         "(sincérité) » — d'où la définition en terme : « la dot est donc ce que le mari offre à son "
         "épouse en raison du mariage, et c'est un pilier (rukn) de celui-ci ». La dérivation n'est pas "
         "un ornement : elle fait du nom même l'attestation du premier objectif — la dot témoigne de la "
         "sincérité du mari dans son projet de mariage."),
        ("Deuxièmement, le statut. La leçon tire la rukniya du hadith lui-même : « Cherche, même une "
         "bague de fer » établit l'obligation de quelque chose à donner ; et le « marie-la à moi » de "
         "l'homme — « c'est-à-dire avec une dot. Il n'a pas dit : “Donne-la-moi en cadeau”, c'est-à-dire "
         "marie-la à moi sans dot, car cela relève des prérogatives du Prophète ﷺ. Il est donc "
         "indispensable pour les autres d'avoir une dot » — le mariage sans dot est une exception "
         "réservée à celui que le Coran nomme. Le verset appuie : « Et donnez aux femmes leurs dot "
         "(al-ṣadāqāt) par bonne grâce » ; Abū ʿUbayd : « “Par bonne grâce” signifie par le contentement "
         "de l'âme pour cette prescription qu'Allah a établie. » La seconde citation coranique de la "
         "leçon — imprimée « la sourate al-Māʾida, verset 6 » dans les deux couches — porte la glose « il "
         "entend par “dot” ici leurs dots » : la prescription est une, de la première à la seconde "
         "citation. Sur la formule de la femme, az-Zurqānī : « La réalité n'est pas ce qui est compris » "
         "— une personne libre ne peut être possédée ; « donc la donatrice a dit en réalité : “Je me "
         "marie à toi sans dot” » — la langue de l'offrande déplace la chose offerte."),
        ("Le cœur technique de la leçon est la face de la préposition bi dans « avec ce que tu as du "
         "Coran ». La bi « indique la contrepartie, comme dans “je te vends mon vêtement contre un "
         "dīnār” » — et « il ne signifie pas qu'il l'a mariée à cause de sa mémorisation du Coran ». "
         "Al-Māzarī donne la face délicate : « la préposition bi (par) est causale, en l'honneur du "
         "Coran » — dans ce sens l'épouse devient en la valeur de la muwahhaba, la mariée sans dot, et "
         "« cela n'est permis qu'à lui, le Prophète ﷺ ». La nuance est fine : même si l'on lit la bi "
         "comme cause, la cause n'est pas un prix ; et si l'on lit l'épouse comme mariée sans dot, la "
         "seule pareille est celle que le Prophète ﷺ épousait sans dot — la licence ne passe pas aux "
         "autres, d'où l'obligation de la dot pour eux."),
        ("ʿIyāḍ a dit : « Cela peut se comprendre de deux manières. La plus manifeste est qu'il lui "
         "enseigne ce qu'il a du Coran, ou une partie de celui-ci, et que son enseignement constitue sa "
         "dot » — « cette interprétation a été rapportée de Mālik et a été utilisée comme argument par "
         "ceux qui disent que les avantages issus de biens peuvent constituer une dot » ; Muslim : « Va "
         "et enseigne-lui du Coran » ; Abū Dāwūd : « ...enseigne-lui vingt versets ». Face à cela, le "
         "premier avis — aṭ-Ṭaḥāwī, al-Abharī, « ainsi que d'autres comme al-Layth et Makḥūl » : « Ceci "
         "est spécifique au Prophète ﷺ, et la préposition bi (par) a ici le sens de la lām (pour), "
         "c'est-à-dire : pour ce que tu as mémorisé du Coran et que tu es devenu son égal en religion » "
         "— « cela nécessite une preuve », dit-il ; il a été rapporté aussi d'Abū Ḥanīfa, d'Aḥmad et de "
         "Mālik, deux dits préférés dans leur madhhab. Sa preuve est ce qu'ont rapporté Saʿīd ibn Manṣūr "
         "et Ibn as-Sukn d'Abū an-Nuʿmān al-Azdī, le Compagnon : « Le Prophète ﷺ a marié une femme sur "
         "une sourate du Coran et a dit : “Après toi, il ne sera permis à personne d'avoir une dot.” » "
         "Le deuxième avis — Mālik, ash-Shāfiʿī et d'autres — « autorise de faire de la dot des "
         "avantages, conformément à l'apparent du hadith »."),
        ("ʿIyāḍ élargit encore : « il est possible qu'il l'ait mariée à cet homme à cause de ce qu'il "
         "avait du Coran, en le considérant comme une dot pour elle, et que le sujet de la dot soit "
         "resté sans mention, soit parce qu'il l'a donnée en compensation, comme il a expié pour celui "
         "qui commet l'acte sexuel en Ramadan et a indemnisé le tué à Khaybar... ou soit parce qu'il a "
         "laissé la dot à sa charge et l'a mariée par délégation, jusqu'à ce qu'il trouve une dot ou "
         "qu'il l'acquière avec ce qu'il a du Coran, afin qu'il s'attache à l'apprentissage du Coran, à "
         "la prééminence de ceux qui le connaissent et à l'intercession par son intermédiaire ». "
         "Conclusion de l'analyse : « puisque toutes ces possibilités sont admises, cela ne constitue "
         "pas une preuve pour l'interdiction du mariage sans dot ou avec ce qui n'a pas de valeur, fin "
         "de citation ». Le hadith d'Ibn Masʿūd, rapporté par ad-Dāraqutnī, renforce : « Je t'ai mariée "
         "à elle à la condition que tu l'ensesignes et que tu l'instruis, et si Allah te fait parvenir "
         "des biens, tu la dédommages » — « l'homme s'est donc marié à elle sur cette condition » ; et "
         "« le hadith autorise de percevoir une rétribution pour l'enseignement du Coran, et c'est "
         "l'avis de la majorité et des trois Imams »."),
        ("Troisièmement, les objectifs de la dot, cinq : signifier la noblesse du contrat de mariage ; "
         "honorer la femme et préparer l'établissement du mariage sur la base de l'affection et de "
         "l'amour ; être un témoignage de la sincérité du mari — ce que son nom, dérivé d'aṣ-ṣidq, "
         "indique ; aider l'épouse à assumer certaines nécessités du mariage dont elle a besoin ; "
         "distinguer le mariage des relations illicites. Quatrièmement, les objectifs du hadith : "
         "éducatifs — « la considération du plus âgé pour les intérêts de la communauté et son "
         "orientation, par la bienveillance qu'il leur témoigne, que ce soit en s'occupant de leurs "
         "affaires ou en facilitant leurs besoins et en trouvant des solutions à leurs problèmes » ; et "
         "dans « Si tu n'en as pas besoin », « la beauté de la bonne conduite envers le Prophète ﷺ » ; "
         "juridiques — « l'épouse ne peut être possédée » (la ḥaqīqa n'est pas voulue) et « la dot dans "
         "le mariage est un droit d'Allah, le Très-Haut, et il n'est pas permis de s'entendre pour y "
         "renoncer ». L'évaluation demande le statut de la dot avec la preuve qui l'établit et ses "
         "objectifs. L'istiṯmār arme la leçon : le n° 1644 — ʿUmar ibn al-Khaṭṭāb, d'après Saʿīd ibn "
         "al-Musayyab, par Yaḥyā ibn Saʿīd : « Quiconque se marie une femme atteinte de folie, de lèpre "
         "ou de lèpre blanche, et qu'il a eu des relations avec elle, a droit à sa dot en totalité. Et "
         "cela est une dette pour son mari envers son tuteur (walī) » ; le n° 1645 — Mālik : le ghurm "
         "n'est que si le tuteur qui l'a mariée « est son père, son frère ou celui qui est considéré "
         "comme étant au courant de son état » ; sinon « il n'est pas redevable » — « et cette femme "
         "doit rendre ce qu'elle a reçu comme dot, et on laisse pour elle ce qui peut être licitement "
         "consommé » ; l'exercice demande le statut de la dot quand le vice est inconnu, et qui doit "
         "payer la dot au mari en cas de nullité. La préparation préalable — « Connais le don gratuit "
         "(al-ḥibāʾ) » — annonce la leçon de la dot et du ḥibāʾ : étiquetée leçon 3 du manuel mais "
         "placée avant celle-ci dans le livre — le chaînage de l'imprimé suit son propre ordre (leçon 2 "
         "→ leçon 3 → leçon 4), et chaque préparation préalable appelle la leçon suivante du manuel, "
         "non celle du livre."),
    ],
    "points": [
        ("Fil de révision : trois objectifs (le statut de la dot ; distinguer la dot du ḥibāʾ ; les "
         "objectifs de la dot) → tamhīd (la dot instituée pour honorer l'épouse et témoigner de la "
         "sincérité du mari — an-Nisāʾ 4) → le hadith de Sahl ibn Saʿd as-Sāʿidī (n° 1643)."),
        ("Le récit du hadith : la femme qui se voue (« je me dédie (te voue) à toi »), l'homme qui se "
         "lève (« si tu n'en as pas besoin »), les quatre degrés — le saroual (« tu resteras sans "
         "saroual »), « cherche donc quelque chose », « cherche, même une bague de fer », enfin le "
         "Coran : « Je t'ai mariée à elle avec ce que tu as du Coran »."),
        ("La définition : la dot dérivée d'aṣ-ṣidq (la sincérité) — ce que le mari offre à son épouse en "
         "raison du mariage, et un pilier (rukn) du contrat ; al-ḥibāʾ = l'octroi sans contrepartie ; "
         "les cinq langues du mot recensées par la leçon (ṣuduq ; ṣadaqa du Ḥijāz ; ṣadaqa de Tamīm "
         "« comme ghurfah et ghurafāt » ; ṣadaqa/ṣadāq « comme qaryah et qurā »)."),
        ("Le statut : pilier attesté par l'insistance du Prophète ﷺ (« cherche, même une bague de fer ») "
         "; « marie-la à moi » avec dot — le mariage sans dot réservé aux prérogatives du Prophète ﷺ "
         "(« il n'a pas dit : “Donne-la-moi en cadeau” ») ; an-Nisāʾ 4 et la glose d'Abū ʿUbayd — « par "
         "bonne grâce » signifie par le contentement de l'âme pour cette prescription qu'Allah a établie."),
        ("La glose d'az-Zurqānī sur « je me dédie à toi » : « la réalité n'est pas ce qui est compris » "
         "— une personne libre ne peut être possédée — « donc la donatrice a dit en réalité : “Je me "
         "marie à toi sans dot” » ; la seconde citation coranique de la leçon porte la glose « il entend "
         "par “dot” ici leurs dots »."),
        ("La préposition bi de compensation : « je te vends mon vêtement contre un dīnār » — « il ne "
         "signifie pas qu'il l'a mariée à cause de sa mémorisation du Coran » ; la bi causale en "
         "l'honneur du Coran (al-Māzarī) — l'épouse en la valeur de la mariée sans dot, « cela n'est "
         "permis qu'à lui, le Prophète ﷺ »."),
        ("ʿIyāḍ : « la plus manifeste » des deux faces — l'enseignement du Coran comme dot (rapporté de "
         "Mālik ; l'argument des partisans des avantages ; Muslim « va et enseigne-lui du Coran », Abū "
         "Dāwūd « ...enseigne-lui vingt versets »)."),
        ("Les deux avis : le premier — spécifique au Prophète ﷺ (aṭ-Ṭaḥāwī, al-Abharī, al-Layth, Makḥūl "
         "— la bi en valeur de la lām ; l'égalité en religion ; rapporté d'Abū Ḥanīfa, d'Aḥmad et de "
         "Mālik ; la preuve d'Abū an-Nuʿmān al-Azdī — « après toi, il ne sera permis à personne d'avoir "
         "une dot ») ; le deuxième — Mālik, ash-Shāfiʿī : les avantages comme dot selon l'apparent du "
         "hadith."),
        ("Les cinq objectifs de la dot : la noblesse du contrat ; l'honneur de la femme et l'affection ; "
         "le témoignage de sincérité (le nom dérivé d'aṣ-ṣidq) ; l'aide à l'épouse dans les nécessités "
         "du mariage ; la distinction d'avec les relations illicites — et les objectifs du hadith : la "
         "considération du plus âgé, l'adab de « si tu n'en as pas besoin », l'épouse non possédée, la "
         "dot droit d'Allah que nul accord ne peut supprimer."),
        ("L'istiṯmār (n° 1644-1645) : la folie, la lèpre, la lèpre blanche — la dot entière au mari "
         "touché et le ghurm sur le walī ; le ghurm lié au walī au courant (père, frère, ou celui qui "
         "est censé connaître) ; sinon la femme rend sa dot, « et on laisse pour elle ce qui peut être "
         "licitement consommé » ; la préparation annonce le ḥibāʾ (leçon 3 du manuel)."),
    ],
    "vocabulaire": [
        {"ar": "الصداق", "translit": "aṣ-ṣadāq",
         "fr": "la dot — ce que le mari présente à son épouse à l'occasion du mariage ; un pilier (rukn) du contrat ; dérivé d'aṣ-ṣidq, la sincérité — le nom même porte le témoignage que la dot rend sur la sincérité du mari"},
        {"ar": "الحباء", "translit": "al-ḥibāʾ",
         "fr": "l'octroi sans contrepartie — le don sans compensation ; en ce hadith il désigne le mariage sans dot, réservé aux prérogatives du Prophète ﷺ"},
        {"ar": "وهبت نفسي لك", "translit": "wahabtu nafsī lak",
         "fr": "« je me dédie (te voue) à toi » : mot de la femme au Prophète ﷺ — la ḥaqīqa n'est pas voulue, une personne libre ne peut être possédée ; comme si elle avait dit : je te marie sans dot"},
        {"ar": "خاتم من حديد", "translit": "khātim min ḥadīd",
         "fr": "« une bague de fer » : le plancher que le Prophète ﷺ assigne au prétendant dépourvu de biens, avant le recours au Coran"},
        {"ar": "الباء للعوض", "translit": "al-bāʾ li-l-ʿiwāḍ",
         "fr": "la préposition « par » en valeur de compensation : « je te vends mon vêtement contre un dīnār » ; dans « avec ce que tu as du Coran », la bi est causale en l'honneur du Coran (al-Māzarī), ou en valeur de la lām (aṭ-Ṭaḥāwī et ceux qui l'ont suivi)"},
        {"ar": "منافع الأعيان", "translit": "manāfiʿ al-aʿyān",
         "fr": "les avantages issus de biens : l'enseignement du Coran donné en dot fonde ceux qui rendent licite d'en faire une dot — dire de Mālik et d'ash-Shāfiʿī sur l'apparent du hadith"},
        {"ar": "الغرم", "translit": "al-ghurm",
         "fr": "la charge : ce que le mari d'une épouse touchée atteinte de folie, de lèpre ou de lèpre blanche reprend sur le walī qui l'a mariée en connaissance de son état — limité par Mālik au walī au courant (n° 1644-1645)"},
        {"ar": "الركن", "translit": "ar-rukn",
         "fr": "le pilier : la dot est un des piliers du mariage — son caractère obligatoire est attesté par l'insistance du Prophète ﷺ (« cherche, même une bague de fer ») et par le verset an-Nisāʾ 4"},
    ],
    "avertissement": "Ce commentaire est un guide de lecture du manuel ; en cas de divergence d'expression, le manuel et sa traduction savante font foi.",
}

E_12992 = {
    "auteur": "IA-1, tour R739",
    "resume": (
        "Guide de lecture de la leçon 12 (ما لا يجوز في الزواج من الشروط ونكاح المحلل — les conditions "
        "illicites dans le mariage et le nikāḥ al-muḥallil), la douzième du livre, étiquetée « la "
        "quatrième leçon » par l'imprimé : trois textes du Muwaṭṭaʾ arment le fond — le n° 1659 : il lui "
        "parvint que « Saʿīd ibn al-Musayyab fut interrogé au sujet de la femme qui stipule à son mari "
        "qu'il ne la fasse point sortir de son pays » ; Saʿīd ibn al-Musayyab : « il la fera sortir, "
        "s'il veut » ; le n° 1660 — Mālik : si l'homme stipule à la femme, fût-ce au contrat du mariage, "
        "« je n'épouserai point sur toi, et je ne m'infiltrerai point », « cela n'est point de chose, "
        "sauf s'il y a en cela un serment par divorce ou par affranchissement ; alors cela lui incombe "
        "et le lie » ; le n° 1661 — Rifāʿa ibn Simwāl répudia son épouse Tamīma bint Wahb trois fois du "
        "vivant du Messager de Dieu — paix et bénédiction sur lui ; elle épousa ʿAbd ar-Raḥmān ibn "
        "az-Zubayr, « qui se heurta contre elle et ne put la toucher, puis la sépara » ; quand Rifāʿa "
        "voulut l'épouser, le Prophète ﷺ l'interdit : « elle ne te sera point licite jusqu'à ce que tu "
        "aies goûté la ʿusayla ». L'analyse se déroule en deux temps. Premièrement, le statut des "
        "conditions dans le mariage, réparties en trois espèces : celles que le contrat ne requiert "
        "point et ne contredit point (le sujet du n° 1659 — deux dits : pas de devoir d'accomplir, chez "
        "Saʿīd ibn al-Musayyab, reçu en chaîne continue et d'un groupe des Anciens « au-dessus d'eux "
        "ʿAlī ibn Abī Ṭālib » — qui, saisi de la demeure stipulée, dit « la condition de Dieu avant sa "
        "condition [ou : sa propre condition] » et « ne lui accorda rien », « et pourtant le préférable "
        "demeure l'accomplissement de la condition » ; le devoir, chez ʿUmar ibn al-Khaṭṭāb — « à elle "
        "sa condition, et les musulmans sont à leurs conditions » — appuyé par le hadith des deux "
        "Cheikhs « le plus droit des conditions : que vous accomplissiez ce par quoi vous avez rendu "
        "licites les sexes », porté chez Mālik et ses pareils sur la recommandation (nadb) afin "
        "d'accorder les deux preuves) ; celles que le contrat requiert et ne contredit point (la belle "
        "cohabitation — « et cohabitez avec elles selon la bienséance », an-Nisāʾ 4:19 — et la demeure "
        "commune : « elle ne fait que rappeler ce que le contrat impose déjà de soi ») ; celles qui "
        "contredisent ce que le contrat requiert (le divorce en sa main, l'absence d'héritage : "
        "« nul ne dispose de ce que Dieu a disposé »). Deuxièmement, le statut du mariage du muḥallil : "
        "avec l'intention d'analyser — « vicié et nullement confirmé », la dot si attouchement, le "
        "mariage nouveau après rupture (n° 1664) — « La Loi a ainsi rendu nul le fruit même que le "
        "ruseur poursuit : l'intention d'analyser disloque le second mariage, sans ouvrir la licéité "
        "qu'il visait » ; sans l'intention — deux cas : s'il a goûté la ʿusayla, fût-ce une fois, et la "
        "répudie de lui-même, elle redevient licite au premier mari après l'ʿidda de trois règles — "
        "« l'accord des deux maris pour la rendre licite sans consommation réelle n'y fait rien, car le "
        "verset a suspendu la licéité au goût, non à l'entente » (le manṭūq du verset — l'āya "
        "reproduite en image dans le manuel et restaurée verbatim au cache coranique : la référence "
        "imprimée porte « la sourate al-Baqara, verset 228 », le verset qui porte la licéité du "
        "muḥallil est le 230 — cf. les notes du traducteur) ; s'il n'a point goûté, elle ne redevient "
        "point licite (le mafhūm de l'āya — le hadith de Rifāʿa ; dans une version des deux Cheikhs : "
        "« et ce qu'il a, c'est comme la houppette » — elle prit alors une houppette de son jilbāb ; "
        "al-Bukhārī : « elle a menti — par Dieu — je la secoue comme on secoue le cuir tanné »). Le "
        "commentaire lexical sur la ʿusayla — diminutif d'ʿasal, le miel, métaphore du coït — occupe la "
        "fin de la leçon : le féminin du diminutif (les deux genres du miel, ou l'intention du plaisir, "
        "ou la goutte — « l'émission n'est point requise, d'accord des savants » ; al-Ḥasan : la ʿusayla "
        "est l'émission) ; Abū ʿUmar et les deux visages de « point licite jusqu'à » ; Ibn al-ʿArabī — "
        "« la disparition de la gland, voilà la ʿusayla ; quant à l'émission, voilà la dabīla » — « il a "
        "commencé par la jouissance et fini par la douleur » ; al-Ubbī — « ce qui précède l'émission est "
        "plus délicieux que l'heure de l'émission » ; et « notre cheikh Abū ʿAbdallāh — c'est Muḥammad "
        "ibn ʿArafa — a dit : qui a du goût connaît cela ». La couche française de la leçon s'arrête à "
        "ce dire d'Ibn ʿArafa : les rubriques de l'évaluation (التقويم), de l'istiṯmār (الاستثمار) et "
        "de la préparation préalable (الإعداد القبلي) ne sont rendues que dans la couche arabe — "
        "consigné ; le commentaire qui suit les reprend d'elle. L'istiṯmār arme deux textes : le n° "
        "1663 — al-Qāsim ibn Muḥammad, interrogé au sujet d'un homme qui répudia son épouse de la "
        "batta, qu'un autre épousa après lui et qui mourut sans la toucher : « il n'est pas licite au "
        "premier mari de la reprendre » ; et le hadith rapporté "
        "par aṭ-Ṭabarānī dans aṣ-Ṣaghīr par un isnād ḥasan : le Prophète ﷺ demanda Umm Bishr bint "
        "al-Barrāʾ ibn Maʿrūr en mariage ; elle dit « j'ai stipulé à mon mari de ne point me marier "
        "après lui » ; il dit : « cela ne convient point » — l'exercice demande de comparer les deux "
        "hadiths (l'accord dans le statut, la différence dans la forme) et de placer le second dans "
        "l'une des espèces de conditions. La préparation préalable — « cherche dans le prochain cours "
        "les illicites dans le mariage » et la question « le zinā rend-il licite ce qui est licite ? » "
        "— annonce la leçon des illicites dans le mariage (al-muḥarramāt fī z-zawāj), la cinquième du "
        "manuel."),
    "explication": [
        ("La leçon 12 — la douzième du livre, étiquetée « la quatrième leçon » par l'imprimé — porte ce "
         "qui n'est point permis dans le mariage au titre des conditions, et le mariage du muḥallil. "
         "Trois objectifs l'ouvrent : reconnaître le statut des conditions dans le mariage et celui du "
         "mariage du muḥallil ; distinguer le mariage après lequel l'épouse redevient licite des autres "
         "mariages ; saisir les finalités de l'interdiction du mariage du muḥallil et de certaines "
         "conditions dans le mariage. Le préambule donne la clef : « L'Islam a légiféré le mariage pour "
         "un ensemble de finalités, et afin de les réaliser il a entouré le mariage d'un ensemble de "
         "conditions et de dispositions » — parmi elles, l'interdiction de certaines conditions « qui "
         "ont pour effet de contredire les visées du mariage et ses finalités », et l'interdiction du "
         "mariage « qui a pour effet de toucher la dignité de ce lien, qui demeure un engagement "
         "solennel (mīthāq ghalīẓ) — c'est ainsi que le Très Haut l'a nommé : “comment prendriez-vous "
         "cet engagement, alors que vous avez déjà goûté l'un de l'autre et qu'elles ont obtenu de vous "
         "un engagement ferme ?” (an-Nisāʾ 4:21) — et qui ne se rompt que selon ses règles propres »."),
        ("Les hadiths s'ouvrent par le cas de la condition sans effet : « Saʿīd ibn al-Musayyab fut "
         "interrogé au sujet de la femme qui stipule à son mari qu'il ne la fasse point sortir de son "
         "pays » — « il la fera sortir, s'il veut » (n° 1659). L'analyse range cette condition dans la "
         "première espèce — « toute condition qui ne contredit point le contrat et ne contient point un "
         "de ses effets » — et rapporte deux dits. Le premier : « il n'y a point de devoir "
         "d'accomplir cette condition » — le dit de Saʿīd ibn al-Musayyab ; Ibn ʿAbd al-Barr atteste sa "
         "transmission « en chaîne continue — Abū Bakr ibn Abī Shayba l'a rapporté d'Ibn al-Mubārak, "
         "d'al-Ḥārith ibn ʿAbd ar-Raḥmān, de Muslim ibn Yasār, de Saʿīd ibn al-Musayyab », et d'un "
         "groupe des Anciens « au-dessus d'eux ʿAlī ibn Abī Ṭālib » : un homme avait épousé une femme "
         "et stipulé pour elle sa demeure ; l'affaire fut portée à ʿAlī, qui dit « la condition de Dieu "
         "avant sa condition [ou : sa propre condition] » et « ne lui accorda rien » — « et pourtant le "
         "préférable demeure l'accomplissement de la condition »."),
        ("Le deuxième dit : « le devoir d'accomplir cette condition » — reçu d'un groupe des Anciens "
         "« au-dessus d'eux ʿUmar ibn al-Khaṭṭāb — qu'Allah l'agrée —, qui a dit : “à elle sa condition, "
         "et les musulmans sont à leurs conditions.” » L'appuie le hadith des deux Cheikhs : « le plus "
         "droit des conditions : que vous accomplissiez ce par quoi vous avez rendu licites les sexes. » "
         "— « mais cela est porté, chez Mālik et ses pareils, sur la recommandation (nadb), afin "
         "d'accorder les deux preuves : le devoir n'est point établi, et la condition demeure cependant "
         "digne d'être tenue. » Le n° 1660 fixe la doctrine de la condition sans effet et de son "
         "exception : si l'homme stipule à la femme, fût-ce au contrat du mariage, « je n'épouserai "
         "point sur toi, et je ne m'infiltrerai point », « cela n'est point de chose, sauf s'il y a en "
         "cela un serment par divorce ou par affranchissement ; alors cela lui incombe et le lie » — la "
         "promesse nue ne lie pas ; le serment lie."),
        ("La deuxième espèce — « les conditions que le contrat requiert et ne contredit point » — « c'est "
         "toute condition qui réalise les finalités du contrat et ses effets — comme que l'épouse "
         "stipule sur lui la belle cohabitation (al-muʿāshara al-ḥasana), ou qu'il stipule sur elle "
         "qu'elle demeure avec lui dans sa demeure » : « cette espèce de conditions n'est qu'une "
         "confirmation des effets du contrat lui-même — la belle cohabitation est déjà un devoir du "
         "Très Haut : “et cohabitez avec elles selon la bienséance” (an-Nisāʾ 4:19) —, et la demeure "
         "commune un effet du mariage établi par la Sunna ; c'est pourquoi il y a, à son sujet, devoir "
         "d'accomplir : elle ne fait que rappeler ce que le contrat impose déjà de soi. » La troisième "
         "espèce — « les conditions qui contredisent ce que le contrat requiert » — « comme que "
         "l'épouse stipule sur l'époux que son divorce soit en sa main, ou que l'époux stipule sur "
         "l'épouse qu'elle n'hérite point de lui. Ces conditions-là sont nulles : elles détruisent un "
         "effet que Dieu a établi dans le contrat, et nul ne dispose de ce que Dieu a disposé » — la "
         "leçon renvoie l'examen détaillé de la condition du divorce en sa main à la leçon de la femme "
         "investie du commandement d'elle-même."),
        ("Deuxièmement, le mariage du muḥallil. Celui qui épouse « la femme répudiée de la troisième "
         "(al-mubattā) avec l'intention d'analyser » — dans le dessein qu'après lui elle redevienne "
         "licite à son premier mari — contracte un mariage « vicié et nullement confirmé (fāsid wa-lā "
         "yuqarr ʿalayhi) » ; s'il la touche, elle a sa dot « semblable à celui de sa pareille, comme "
         "l'épouse touchée de tout mariage vicié » ; et après la rupture « il peut se porter vers un "
         "mariage nouveau — car la rupture du vicié lève toute attache entre les deux, et l'empêchement "
         "qui portait sur elle retombe ». Mālik l'a fixé : « il ne demeure point sur ce mariage-là "
         "jusqu'à ce qu'il se porte vers un mariage nouveau » (n° 1664). Le commentaire de la leçon "
         "éclaire la sagesse de la règle : « La Loi a ainsi rendu nul le fruit même que le ruseur "
         "poursuit : l'intention d'analyser disloque le second mariage, sans ouvrir la licéité qu'il "
         "visait. »"),
        ("Sans l'intention d'analyser, l'affaire se détaille en deux cas. Premier cas : le second mari "
         "« a goûté sa ʿusayla, fût-ce une fois, puis qu'il la répudie de lui-même, sans accord avec le "
         "premier mari — alors elle redevient licite au premier mari, s'il veut l'épouser de nouveau, "
         "après que le second l'a répudiée et qu'elle a accompli son ʿidda — l'ʿidda de trois règles, "
         "comme toute épouse touchée puis séparée » ; et « l'accord des deux maris pour la rendre "
         "licite sans consommation réelle n'y fait rien, car le verset a suspendu la licéité au goût, "
         "non à l'entente » — « c'est le dit apparent (manṭūq) du verset ». Le manuel reproduit l'āya "
         "en image ; la référence imprimée porte « la sourate al-Baqara, verset 228 », le verset qui "
         "porte la licéité du muḥallil est le 230 — l'āya est restaurée verbatim au cache coranique "
         "(cf. les notes du traducteur) : « s'il la répudie la troisième fois, le mariage avec elle "
         "n'est point licite de la part du premier mari jusqu'à ce qu'elle épouse un autre, et que "
         "celui-ci la répudie »."),
        ("Deuxième cas : « que le second mari n'ait point goûté sa ʿusayla, et qu'il la répudie — alors "
         "elle ne redevient point licite à son premier mari. C'est l'implicite (mafhūm) de l'āya : la "
         "licéité suppose le “goût” que le verset nomme. » C'est le hadith de la leçon : Rifāʿa ibn "
         "Simwāl répudia son épouse Tamīma bint Wahb trois fois ; elle épousa ʿAbd ar-Raḥmān ibn "
         "az-Zubayr, « qui se heurta contre elle et ne put la toucher, puis la sépara » ; quand Rifāʿa "
         "voulut l'épouser, le Messager de Dieu l'interdit : « elle ne te sera point licite jusqu'à ce "
         "que tu aies goûté la ʿusayla » (n° 1661). Dans une version des deux Cheikhs : « et ce qu'il "
         "a, c'est comme la houppette » — « elle prit alors une houppette de son jilbāb » ; le Prophète "
         "ﷺ « la comparut ainsi pour la petitesse de son membre, ou pour sa mollesse — et c'est le plus "
         "apparent des deux dits : il est loin que l'homme en demeure au degré où disparaît la gland ». "
         "Dans al-Bukhārī, il répondit : « elle a menti — par Dieu — je la secoue comme on secoue le "
         "cuir tanné » (anfuḍuhā naḍf al-adīm)."),
        ("La fin de la leçon donne l'image de la ʿusayla : « l'homme a fait similitude de sa jouissance "
         "avec la douceur et la suavité du miel, et a emprunté pour elle un goût » — le diminutif est "
         "féminin : le miel « porte les deux genres », ou le féminin est « sur l'intention du plaisir "
         "(ar-raghba fī al-ladhdha) », ou — un dire — « sur l'intention de la goutte (an-nuṭfa) : car "
         "l'émission n'est point requise, d'accord des savants » ; « al-Ḥasan a singularisé contre "
         "cela : la ʿusayla est l'émission (al-inzāl), suivant le sens du nom ». Abū ʿUmar lit les deux "
         "visages de « point licite jusqu'à » : si elle est comme elle a décrit, « il n'y a point de "
         "chemin vers le goût de la ʿusayla » ; sinon, « il lui a dit cela en espérance — et il se "
         "peut que ce soit ». Ibn al-ʿArabī : « la disparition de la gland, voilà la ʿusayla ; quant à "
         "l'émission, voilà la dabīla » — l'homme demeure « dans la jouissance de l'ébatte », et « il a "
         "commencé par la jouissance et fini par la douleur » ; al-Ubbī en tire « que ce qui précède "
         "l'émission est plus délicieux que l'heure de l'émission » ; et « notre cheikh Abū ʿAbdallāh — "
         "c'est Muḥammad ibn ʿArafa — a dit : qui a du goût connaît cela ». Les rubriques finales ne "
         "sont rendues que par la couche arabe de la leçon — la couche française s'arrête au dire "
         "d'Ibn ʿArafa (consigné) : l'évaluation propose deux situations à statuer avec leur cause (la "
         "condition de ne point la voyager hors du Maroc avec la demeure stipulée d'elle ; la répudiée "
         "trois fois d'un autre que le second a répudiée avant consommation, le premier mari voulant "
         "l'épouser) ; l'istiṯmār arme le n° 1663 — al-Qāsim ibn Muḥammad : l'épouse répudiée de la "
         "batta qu'un autre a épousée et qui est morte sans être touchée — « il n'est pas licite au "
         "premier mari de la reprendre » — et le hadith d'Umm Bishr bint al-Barrāʾ ibn Maʿrūr "
         "(aṭ-Ṭabarānī dans aṣ-Ṣaghīr, isnād ḥasan) : « j'ai stipulé à mon mari de ne point me marier "
         "après lui » — « cela ne convient point » ; la préparation préalable — « cherche dans le "
         "prochain cours les illicites dans le mariage » — annonce la leçon des illicites dans le "
         "mariage (al-muḥarramāt fī z-zawāj), avec sa question : le zinā rend-il licite ce qui est "
         "licite ?"),
    ],
    "points": [
        ("Fil de révision : trois objectifs (le statut des conditions et du muḥallil ; distinguer le "
         "mariage après lequel l'épouse redevient licite ; saisir les finalités des interdictions) → "
         "préambule (le mīthāq ghalīẓ — an-Nisāʾ 4:21) → trois hadiths du Muwaṭṭaʾ (n° 1659, 1660, 1661)."),
        ("Les trois espèces de conditions : ce que le contrat ne requiert point et ne contredit point ; "
         "ce qu'il requiert et ne contredit point ; ce qui contredit ce que le contrat requiert."),
        ("La première espèce — les deux dits (Saʿīd ibn al-Musayyab : « il la fera sortir, s'il veut » ; "
         "ʿUmar : « à elle sa condition, et les musulmans sont à leurs conditions ») et l'accord des "
         "preuves : le devoir porté sur la recommandation (nadb) chez Mālik et ses pareils — « la "
         "condition demeure cependant digne d'être tenue »."),
        ("ʿAlī et la demeure stipulée : « la condition de Dieu avant sa condition [ou : sa propre "
         "condition] » — « ne lui accorda rien » — « et pourtant le préférable demeure "
         "l'accomplissement de la condition » ; la chaîne continue d'Ibn ʿAbd al-Barr."),
        ("Le n° 1660 : « je n'épouserai point sur toi, et je ne m'infiltrerai point » — « cela n'est "
         "point de chose » — l'exception du serment par divorce ou par affranchissement : « alors cela "
         "lui incombe et le lie »."),
        ("La deuxième espèce — confirmation des effets (la belle cohabitation — an-Nisāʾ 4:19 ; la "
         "demeure commune — effet établi par la Sunna) ; la troisième espèce — nulle (le divorce en sa "
         "main ; l'absence d'héritage) — « nul ne dispose de ce que Dieu a disposé »."),
        ("Le muḥallil avec intention : fāsid, nullement confirmé ; la dot si attouchement ; le mariage "
         "nouveau après rupture (n° 1664) — « l'intention d'analyser disloque le second mariage, sans "
         "ouvrir la licéité qu'il visait »."),
        ("Le muḥallil sans intention — le manṭūq du verset (la référence imprimée porte « la sourate "
         "al-Baqara, verset 228 » ; le verset qui porte la licéité du muḥallil est le 230 — restauré "
         "verbatim au cache coranique) : le goût réel, non l'entente des deux maris ; l'ʿidda de trois "
         "règles."),
        ("Le mafhūm de l'āya : sans goût de la ʿusayla, elle ne redevient point licite — le cas de "
         "Rifāʿa ibn Simwāl, de Tamīma bint Wahb et de ʿAbd ar-Raḥmān ibn az-Zubayr ; la houppette (les "
         "deux Cheikhs) et le démenti d'al-Bukhārī (« je la secoue comme on secoue le cuir tanné »)."),
        ("L'image de la ʿusayla : le diminutif du miel, la métaphore du coït ; les deux visages d'Abū "
         "ʿUmar ; Ibn al-ʿArabī — la ʿusayla et la dabīla ; al-Ḥasan dissident (l'émission) ; Ibn ʿArafa "
         "— « qui a du goût connaît cela » ; l'istiṯmār (n° 1663 — la veuve non touchée, pas de "
         "murājaʿa ; Umm Bishr — « cela ne convient point ») ; la préparation annonce les illicites "
         "dans le mariage."),
    ],
    "vocabulaire": [
        {"ar": "الشرط في النكاح", "translit": "ash-sharṭ fī n-nikāḥ",
         "fr": "la condition dans le mariage : trois espèces selon son rapport au contrat — ce qu'il ne requiert point et ne contredit point, ce qu'il requiert, ce qui contredit ses effets"},
        {"ar": "العسيلة", "translit": "al-ʿusayla",
         "fr": "diminutif d'ʿasal, le miel : métaphore du coït — « elle ne te sera point licite jusqu'à ce que tu aies goûté la ʿusayla » (n° 1661)"},
        {"ar": "نكاح المحلل", "translit": "nikāḥ al-muḥallil",
         "fr": "le mariage du muḥallil : épouser la mubattā dans le dessein qu'elle redevienne licite à son premier mari — vicié et nullement confirmé"},
        {"ar": "المبتوت", "translit": "al-mubattā",
         "fr": "la répudiée de la troisième : celle que trois répudiations séparent de son mari et qui ne lui redevient licite que par le goût d'un autre mariage"},
        {"ar": "اليمن بالطلاق أو العتاق", "translit": "al-yamīn bi-ṭalāq aw ʿitāqa",
         "fr": "le serment par divorce ou par affranchissement : l'exception qui lie l'homme conditionnant « je n'épouserai point sur toi, et je ne m'infiltrerai point » (n° 1660)"},
        {"ar": "المنطوق", "translit": "al-manṭūq",
         "fr": "le dit apparent du verset : la licéité suspendue au goût réel, non à l'entente des deux maris"},
        {"ar": "المفهوم", "translit": "al-mafhūm",
         "fr": "l'implicite de l'āya : sans le goût que le verset nomme, elle ne redevient point licite au premier mari — le cas de Rifāʿa et de Tamīma bint Wahb"},
        {"ar": "الدبيلة", "translit": "ad-dabīla",
         "fr": "l'émission : opposée à la ʿusayla par Ibn al-ʿArabī — « il a commencé par la jouissance et fini par la douleur » ; l'émission n'est point requise d'accord des savants"},
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
DOCIDS = ('12991', '12992')
deja = [d for d in DOCIDS if d in com]
if deja:
    print(f'!! déjà présent : {deja} — rien de fait')
    raise SystemExit(1)
com['12991'] = norme_entree(E_12991)
com['12992'] = norme_entree(E_12992)

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

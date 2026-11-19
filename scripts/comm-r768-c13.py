#!/usr/bin/env python3
"""R768 — ajoute le commentaire pédagogique de la leçon 13 de hadith-tanawi-1
(13074 أحكام الخلع — les dispositions du khulʿ, la treizième du livre,
étiquetée « leçon 15 » par l'imprimé — le SUIVANT de R739, 12992, dans
l'ordre des leçons du registre : 12925 … 12992, puis 13074)
à content/commentaires/hadith-tanawi-1.json.

Même protocole que comm-r739.py : normalisation de la ponctuation FR
(U+202F avant ; : ! ? » et après «, apostrophe courbée) sur l'entrée
nouvelle seulement — opération idempotente. Rédaction d'après la lecture
complète de la leçon (htmlFr intégral, ~22 000 caractères après
débalisage ; couche arabe lue pour les formes du vocabulaire et pour
l'étiquette de l'imprimé « (الدرس 15) » et les trois objectifs arabes).
Règle 2 de LISEZ-MOI.md : aucune invention — les numéros du Muwaṭṭaʾ
(1776, 1778, 1781, 1782, 1783 ; récit de Muḥammad ibn al-Ḥasan), les
attributions (La Sunan al-Kubrā de al-Bayhaqī), le Code de la famille
article 120, les dits (Ḥabība, Thābit, Saʿīd ibn al-Musayyab, Mālik,
ash-Shāfiʿī, Ibn ʿAbbās, ʿUthmān, Abū ʿUmar, al-Bājī) sont cités tels
qu'ils figurent dans la leçon. Les formes arabes du vocabulaire sont
reprises de la couche arabe ou dérivées des translittérations de la
leçon, sans harakat (règle 3).

Garde-fous ajoutés (convention des vagues hadith-5ep R765-R767) :
- verif-citations intégrée : chaque fragment « » de l'entrée doit être
  retrouvé verbatim dans le htmlFr de la leçon (0 manquant, abort sinon) ;
- recoupements : ancres vérifiées dans les leçons voisines (12991 — la
  dot, pilier ; 12992 — l’ʿidda de trois règles ; 13079 — le liʿān).
"""
import json, re
import html as H

CHEMIN = 'content/commentaires/hadith-tanawi-1.json'
LIVRE = 'content/books/hadith-tanawi-1.json'
DOCID = '13074'

E_13074 = {
    "auteur": "IA-1, tour R768",
    "resume": (
        "Guide de lecture de la leçon 13 (أحكام الخلع — les dispositions du khulʿ), "
        "la treizième du livre, étiquetée leçon 15 par l'imprimé (الدرس 15) : un hadīth du "
        "Muwaṭṭaʾ arme le fond — le n° 1776, que Mālik rapporte de Yaḥyā ibn Saʿīd, "
        "d'après ʿAmra bint ʿAbd ar-Raḥmān, qu'elle lui rapporta de Ḥabība bint Sahl "
        "al-Anṣāriyya, épouse de Thābit ibn Qays ibn Shammās : le Messager de Dieu — "
        "paix et bénédiction sur lui — « sortit pour la prière de l'aube et trouva "
        "Ḥabība bint Sahl à sa porte, dans le reste de l'obscurité (fī l-ghalas) » ; "
        "il demanda « qui est-ce ? » — « je suis Ḥabība bint Sahl, ô Messager de "
        "Dieu. » ; puis « quelle est ta situation ? » (mā shaʾnuk) — elle dit « ni "
        "moi ni Thābit ibn Qays. » ; quand son mari vint, le Messager de Dieu lui "
        "dit : « voici Ḥabība bint Sahl, elle a mentionné ce qu'Allah a voulu "
        "qu'elle mentionne. » ; Ḥabība : « ô Messager de Dieu, tout ce qu'il m'a "
        "donné, je le tiens. » ; le Messager de Dieu dit à Thābit ibn Qays : "
        "« prends-le d'elle. » — « Il le prit d'elle, et elle s'assit dans sa "
        "famille. » Mālik dit, au sujet de la rachetante (al-mufḍiyya) : « elle ne "
        "retourne à son mari que par un mariage nouveau ; s'il l'épouse, puis la "
        "quitte avant de la toucher, il n'y a point sur elle d'ʿidda de l'autre "
        "divorce, et elle demeure sur son ʿidda première » — « et c'est le plus beau "
        "que j'aie entendu en cela » [n° 1782]. Le préambule donne la double "
        "finalité : la femme peut désirer le divorce « alors même que ce mari "
        "accomplit ses devoirs conjugaux et que rien en lui ne lui donne le droit de "
        "demander la répudiation », son mobile pouvant être « le sentiment "
        "d'aversion qu'elle éprouve à l'égard de ce mari, ou à l'égard du mariage "
        "lui-même » — l'Islam a légiféré le khulʿ « afin que le mari ne perde pas ce "
        "qu'il a dépensé pour son épouse en mahr et en autres biens, et afin que le "
        "lien conjugal ne demeure pas une attache au cou de l'épouse, un carcan dont "
        "elle ne peut briser le sceau » ; et les deux questions d'ouverture — "
        "« Quel est donc le divorce par khulʿ ? Et quelles en sont les dispositions ? » "
        "— distribuent l'analyse en deux temps. Premièrement, le concept du khulʿ : "
        "en langue, l'éloignement (al-izāla) — il est dérivé du « retrait du "
        "vêtement » (khilʿat th-thawb), quand on le dépouille et l'écarte ; puisque "
        "« chacun des deux époux est un habit pour l'autre » — « elles sont un "
        "vêtement pour vous et vous êtes un vêtement pour elles » (2:187 ; l'imprimé "
        "porte « verset 186 », 42ᵉ écart d'étiquetage de la série al-Baqara, déjà "
        "consigné par la traduction) — il a convenu de nommer khulʿ « l'achèvement "
        "du lien conjugal par la voie du versement d'une contrepartie au mari », "
        "chacun des deux époux retirant et dépouillant de lui l'attache (ʿiṣma) du "
        "mariage ; en terme, « une disposition juridique (ṣifa ḥukmiyya) qui lève la "
        "licéité de la jouissance de l'épouse, moyennant une contrepartie versée au "
        "titre du divorce ». Le statut : la licéité — pour preuve la parole du Très "
        "Haut (2:227, « Mais s'ils se décident au divorce… », référence imprimée "
        "concordante) : nul grief n'incombe à l'épouse de payer de son bien ni au "
        "mari d'accepter cela afin de la répudier ; le hadīth de Ḥabība atteste — le "
        "dire « tout ce qu'il m'a donné, je le tiens » signifie qu'elle offrit ce "
        "bien à son mari à condition qu'il se séparât d'elle, dit expressément dans "
        "le hadīth dʿIkrima, d'après Ibn ʿAbbās : « lui rendras-tu son jardin ? » — "
        "« oui. » [La Sunan al-Kubrā de al-Bayhaqī] ; et l'argument requiert le "
        "verset du rachat — l'emplacement du verset est vide dans l'imprimé après "
        "« et le Très Haut a dit », reconstruction raisonnée 2:229 (… alors ils ne "
        "commettent aucun péché si la femme se rachète avec quelque bien…) — cf. "
        "les notes du traducteur. Deuxièmement, les dispositions. La quantité de la "
        "contrepartie — divergence des jurisconsultes : un groupe dit qu'il ne lui "
        "est point permis de prendre d'elle davantage que ce qu'il lui a donné "
        "(rapporté de Ṭāwūs, de ʿAṭāʾ, d'az-Zuhrī et de ʿAmr ibn Shuʿayb ; "
        "désapprobation de Saʿīd ibn al-Musayyab, d'al-Ḥasan, d'ash-Shaʿbī, "
        "d'al-Ḥakam et de Ḥammād — et tel est le dire d'Aḥmad, d'Isḥāq et d'Abū "
        "ʿUbayd) — Saʿīd ibn al-Musayyab : « je ne voie point qu'il prenne d'elle "
        "tout ce qu'il lui a donné, mais qu'il lui laisse quelque chose » ; "
        "d'autres, qu'il lui est licite de prendre davantage lorsque la rébellion "
        "(nushūz) et la nuisance viennent d'elle (ʿIkrima, Mujāhid, Ibrāhīm, "
        "Qubayṣa ibn Ẕuʾayb — et tel est le dire de Mālik et d'ash-Shāfiʿī, et Abū "
        "Thawr l'a dit aussi). Le khulʿ pour nuisance [n° 1778] : Mālik — « quant à "
        "la rachetante qui se rachète de son mari — si l'on sait que son mari lui a "
        "fait nuisance, l'a contrainte, et que l'on sait qu'il est injuste envers "
        "elle, le divorce a suivi son cours, et il lui a rendu son bien » — "
        "« c'est ce que j'entendais, et ce sur quoi est l'affaire des gens chez "
        "nous » ; si la nuisance vient de l'épouse, point de désaccord sur la "
        "licéité ; si elle vient des deux à la fois, quelques-uns des anciens "
        "(al-qarawiyyūn) tiennent qu'il ne convient point de khulʿer l'épouse sur "
        "cela en prenant d'elle quelque chose — « reçu textuellement de ceux de nos "
        "savants qui ont précédé » (cf. notes) ; et ce cas n'est point comme la "
        "question des deux arbitres (al-ḥakamayn) — le qāḍī Abū l-Walīd (al-Bājī, "
        "cf. notes) : « si cela est licite dans la question des deux arbitres, "
        "alors il est plus digne encore qu'il soit licite aux deux [époux], "
        "lorsqu'ils s'accordent dessus ». L’ʿidda de la femme khulʿée : ʿAbdallāh ibn "
        "ʿUmar — « son ʿidda est l’ʿidda de la répudiée » — l’ʿidda du divorce ne "
        "varie point avec la variation du divorce ; dans le Muwaṭṭaʾ [n° 1781], "
        "Saʿīd ibn al-Musayyab, Sulaymān ibn Yasār et Ibn Shihāb : « l’ʿidda de la "
        "femme khulʿée est comme l’ʿidda de la répudiée : trois ʿiddas de règles "
        "(qurūʾ) » — pour celle qui est du nombre des réglées (dhāt al-aqrāʾ) ; et "
        "elle équivaut la répudiée dans l’ʿidda de la grossesse, celle des mois et "
        "celle de la douteuse (al-murātaba). Le khulʿ est-il divorce ou rupture ? "
        "Les Mālikites : divorce — le mari a pris une contrepartie sur l'envoi de "
        "ce qu'il possède, et celui qui possède le divorce, non la rupture (faskh) ; "
        "toute séparation pour laquelle demeure valide le maintien du mariage avec "
        "sa cause est divorce — la séparation des copropriétaires (al-ʾinān) et "
        "celle du miséreux (al-muʿsir) par la pension. Ash-Shāfiʿī : rupture, et il "
        "n'est point divorce — et tel est le dire d'Ibn ʿAbbās, interrogé par "
        "Ibrāhīm ibn Saʿd ibn Abī Waqqāṣ au sujet de l'homme qui répudia son épouse "
        "de deux répudiations puis se laissa khulʿer d'elle : « oui — qu'il "
        "l'épouse ; le khulʿ n'est point divorce. Dieu a mentionné le divorce au "
        "début de l'āya et à sa fin, et le khulʿ se tient entre les deux — le khulʿ "
        "n'est donc point de cela » (lecture de 2:227 et de 2:228 — références "
        "imprimées concordantes). Abū ʿUmar rapporte quʿUthmān et des compagnons "
        "l'ont contredit : le khulʿ est une répudiation unique, sauf s'il entend "
        "par elle davantage — alors il est ce qu'il a voulu et nommé ; le "
        "Muwaṭṭaʾ, récit de Muḥammad ibn al-Ḥasan, porte le cas d'Umm Bakr "
        "al-Aslamiyya, qu'elle se khulʿa de son mari ʿAbdallāh ibn Usayd — "
        "ʿUthmān : « c'est une répudiation, sauf si elle a nommé quelque chose — "
        "alors c'est ce qu'elle a nommé » ; Abū ʿUmar en tire qu'elle n'a ni nommé "
        "ni voulu — et Dieu sait mieux. L'exploitation arme deux textes : le "
        "n° 1783 — Mālik : le khulʿ contre un divorce « suivi, successif "
        "(mutatābiʿan nasqan) » est établi sur le mari ; « s'il y a entre cela des "
        "silences (ṣumāt), ce qu'il a suivi après les silences n'est point de "
        "chose » ; et le Code de la famille, article 120 — « si les époux "
        "s'accordent sur le principe du khulʿ et divergent sur la contrepartie, "
        "l'affaire est portée au tribunal, en vue de tenter la réconciliation "
        "entre eux ; si la réconciliation s'avère impossible, le tribunal juge le "
        "khulʿ exécutoire après en avoir estimé la contrepartie, en tenant compte "
        "du montant de la dot, de la durée du mariage, des motifs de la demande de "
        "khulʿ et de la situation matérielle de l'épouse » ; les exercices "
        "demandent d'extraire du premier hadīth le statut du divorce par khulʿ et "
        "d'expliciter, à partir du texte du Code, ce qui doit être observé dans "
        "l'estimation de la contrepartie. La préparation préalable — « Définis le "
        "liʿān en langue et en terme », « Quel est le statut de l'un des deux "
        "époux qui refuse le liʿān ? », « Explique la manière du liʿān » — annonce "
        "la leçon 14 du livre (Dispositions pour maudire), celle du liʿān : le "
        "serment d'anathème des sourates an-Nūr, versets 6-9, par lequel chacun "
        "des deux époux atteste quatre fois par Dieu sa parole et invoque, à la "
        "cinquième, la malédiction de Dieu sur le menteur (cf. notes)."
    ),
    "explication": [
        ("La leçon 13 — la treizième du livre, étiquetée leçon 15 par l'imprimé "
         "(الدرس 15) — porte les dispositions du khulʿ : la libération de l'épouse "
         "moyennant une contrepartie. Trois objectifs l'ouvrent : reconnaître le "
         "concept du khulʿ et son statut dans la Loi ; distinguer le divorce par "
         "khulʿ des autres divorces ; s'appliquer à saisir la sagesse du divorce par "
         "khulʿ. Le préambule pose la situation : la femme peut désirer, après le "
         "mariage, obtenir le divorce « alors même que ce mari accomplit ses "
         "devoirs conjugaux et que rien en lui ne lui donne le droit de demander la "
         "répudiation » — le mobile pouvant être « le sentiment d'aversion qu'elle "
         "éprouve à l'égard de ce mari, ou à l'égard du mariage lui-même ». La "
         "double finalité fonde l'institution : « afin que le mari ne perde pas ce "
         "qu'il a dépensé pour son épouse en mahr et en autres biens, et afin que "
         "le lien conjugal ne demeure pas une attache au cou de l'épouse, un carcan "
         "dont elle ne peut briser le sceau, l'Islam a légiféré le divorce par "
         "khulʿ » — le mahr, dont la leçon 11 a fixé le statut de pilier, est ici "
         "la mesure naturelle de la contrepartie. Les deux questions d'ouverture — "
         "« Quel est donc le divorce par khulʿ ? Et quelles en sont les "
         "dispositions ? » — distribuent l'analyse en deux temps : le concept, "
         "puis les dispositions."),
        ("Le texte fondateur est le hadīth de Ḥabība bint Sahl al-Anṣāriyya, "
         "épouse de Thābit ibn Qays ibn Shammās (Muwaṭṭaʾ n° 1776), que Mālik "
         "rapporte de Yaḥyā ibn Saʿīd, d'après ʿAmra bint ʿAbd ar-Raḥmān, qu'elle "
         "lui rapporta de Ḥabība. Les notes du traducteur identifient les deux "
         "intermédiaires : ʿAmra — « l'une des plus savantes transmettrices "
         "médinoises de la génération des Successeurs, héritière de la maison de "
         "ʿĀʾisha » — et Yaḥyā ibn Saʿīd ibn Qays al-Makhzūmī, « juge (qāḍī) de "
         "Médine ». La scène : le Messager de Dieu — paix et bénédiction sur lui — "
         "« sortit pour la prière de l'aube et trouva Ḥabība bint Sahl à sa porte, "
         "dans le reste de l'obscurité (fī l-ghalas) » — Ḥabība attendait dès le "
         "dernier tiers de la nuit. « qui est-ce ? » — « je suis Ḥabība bint Sahl, "
         "ô Messager de Dieu. » « quelle est ta situation ? » (mā shaʾnuk) — "
         "« ni moi ni Thābit ibn Qays. » La formule elliptique dit l'essentiel : "
         "aucune communion ne demeure entre eux deux, ni contentement ni aversion "
         "même — elle demande à être libérée sans qu'aucun tort lui soit imputable. "
         "Quand son mari vint, le Messager de Dieu lui dit : « voici Ḥabība bint "
         "Sahl, elle a mentionné ce qu'Allah a voulu qu'elle mentionne. » — la "
         "formule prophétique ménage la discrétion de l'épouse sans dévoiler sa "
         "plainte devant le mari. Ḥabība : « ô Messager de Dieu, tout ce qu'il m'a "
         "donné, je le tiens. » — et la sentence : « prends-le d'elle. » — "
         "« Il le prit d'elle, et elle s'assit dans sa famille. » Le statut du "
         "khulʿ est établi par le fait prophétique lui-même : le Messager de Dieu "
         "— paix et bénédiction sur lui — a accepté la contrepartie et séparé les "
         "époux."),
        ("Le commentaire mālikite de la leçon ajoute le sort de la rachetante "
         "(al-mufḍiyya) : « elle ne retourne à son mari que par un mariage "
         "nouveau ; s'il l'épouse, puis la quitte avant de la toucher, il n'y a "
         "point sur elle d’ʿidda de l'autre divorce, et elle demeure sur son ʿidda "
         "première » — « et c'est le plus beau que j'aie entendu en cela » "
         "[n° 1782] — la règle empêche le cumul : la khulʿée rompue par un second "
         "divorce d'un second mari ne sert point deux ʿiddas. La compréhension "
         "s'ouvre par l'explication lexicale : « le reste de l'obscurité » "
         "(al-ghalas) — « ce qui demeure de la nuit — l'obscurité de son dernier "
         "tiers » ; « quelle est ta situation ? » (mā shaʾnuk) — « quel est ton "
         "ordre et ton état ? » ; les notes consignent que l'imprimé duplique les "
         "deux entrées lexicales — « résidu de mise en page du manuel, dédupliqué "
         "en traduction » — et que le ghalas situe la scène avant l'aube : Ḥabība "
         "attendait à la porte du Messager de Dieu — paix et bénédiction sur lui — "
         "dès le dernier tiers de la nuit."),
        ("Premier temps de l'analyse : le concept. Le khulʿ en langue — "
         "l'éloignement (al-izāla) ; il est dérivé du « retrait du vêtement » "
         "(khilʿat th-thawb), quand on le dépouille et l'écarte. L'assonance fonde "
         "le nom, comme l'établit la leçon : puisque « chacun des deux époux est "
         "un habit pour l'autre » — « elles sont un vêtement pour vous et vous "
         "êtes un vêtement pour elles » (2:187) — il a convenu de nommer khulʿ "
         "« l'achèvement du lien conjugal par la voie du versement d'une "
         "contrepartie au mari », car chacun des deux époux retire et dépouille "
         "de lui l'attache (ʿiṣma) du mariage. NB consigné sans correction : la "
         "référence imprimée sous l'image porte la sourate al-Baqara, verset 186, "
         "verset qui porte le vêtement réciproque des époux est le 187 — c'est "
         "l'écart d'étiquetage de la série al-Baqara, 42ᵉ écart cumulé du registre "
         "des versets, déjà consigné par la traduction elle-même ; l'āya est "
         "restaurée verbatim au cache coranique ; le verset 186 imprimé est celui "
         "de l'invocation. Le khulʿ en terme : « une disposition juridique (ṣifa "
         "ḥukmiyya) qui lève la licéité de la jouissance de l'épouse, moyennant "
         "une contrepartie versée au titre du divorce »."),
        ("Le statut du khulʿ est la licéité — pour preuve la parole du Très Haut "
         "reproduite en image dans le manuel : « Mais s'ils se décident au "
         "divorce, (celui-ci devient exécutoire) car Allah est certes Audient et "
         "Omniscient. » (2:227 — la référence imprimée concorde). Le sens : nul "
         "grief n'incombe à l'épouse de payer de son bien pour obtenir le divorce, "
         "ni au mari d'accepter cela afin de la répudier. Le hadīth de Ḥabība "
         "atteste : « ô Messager de Dieu, tout ce qu'il m'a donné, je le tiens » — "
         "et le commentaire explique que ce dire signifie qu'elle offrit ce bien à "
         "son mari à condition qu'il se séparât d'elle ; cela a été dit "
         "expressément dans le hadīth dʿIkrima, d'après Ibn ʿAbbās : « lui "
         "rendras-tu son jardin ? » — « oui. » [La Sunan al-Kubrā de al-Bayhaqī]. "
         "L'argument requiert ensuite le verset du rachat — et les notes du "
         "traducteur consignent un vide : l'emplacement du verset est vide dans "
         "l'imprimé après « et le Très Haut a dit » ; la reconstruction raisonnée "
         "retient le verset 229 — « alors ils ne commettent aucun péché si la "
         "femme se rachète avec quelque bien » — le verset du rachat (al-iftād) "
         "que tout l'argument requiert : c'est sur le fait qu'il n'y a point de "
         "grief sur les deux, en ce dont elle se rachète, que l'école fonde la "
         "licéité de la contrepartie ; et c'est son rachat que l'analyse appelle "
         "« entre les deux mentions du divorce » au paragraphe suivant."),
        ("Deuxièmement, les dispositions — et d'abord la quantité de la "
         "contrepartie. Les jurisconsultes ont divergé sur la quantité de ce "
         "qu'il est licite au mari de prendre de son épouse pour se laisser "
         "khulʿer d'elle. Un premier dit : il ne lui est point permis de prendre "
         "d'elle davantage que ce qu'il lui a donné, sur l'apparent du hadīth de "
         "Thābit et du dire de son épouse ; cela a été rapporté de Ṭāwūs, de "
         "ʿAṭāʾ, d'az-Zuhrī et de ʿAmr ibn Shuʿayb ; Saʿīd ibn al-Musayyab, "
         "al-Ḥasan, ash-Shaʿbī, al-Ḥakam et Ḥammād ont désapprouvé qu'il prenne "
         "d'elle davantage — et tel est le dire d'Aḥmad, d'Isḥāq et d'Abū ʿUbayd ; "
         "Saʿīd ibn al-Musayyab porte la mesure de la retenue jusqu'au bout : "
         "« je ne voie point qu'il prenne d'elle tout ce qu'il lui a donné, mais "
         "qu'il lui laisse quelque chose. » Un second dit : il lui est licite de "
         "prendre d'elle davantage lorsque la rébellion (nushūz) et la nuisance "
         "viennent d'elle — parmi ceux qui l'ont dit : ʿIkrima, Mujāhid, Ibrāhīm "
         "et Qubayṣa ibn Ẕuʾayb, et tel est le dire de Mālik et d'ash-Shāfiʿī, et "
         "Abū Thawr l'a dit aussi. Les notes identifient les autorités : Ibrāhīm "
         "ibn al-Nakhaʿī, le grand Kufien ; Qubayṣa ibn Ẕuʾayb (m. 86/705, le "
         "savant ḥarūrī) ; Ḥammād ibn Abī Sulaymān (m. 120/738, le maître Kufien "
         "d'Abū Ḥanīfa) ; al-Ḥakam ibn ʿUyayna, le Baṣrien ; ʿAmr ibn Shuʿayb "
         "(d'après son père, d'après son grand-père) ; Abū Thawr — Ibrāhīm ibn "
         "Khālid (m. 240/854), compagnon d'ash-Shāfiʿī ; Abū ʿUbayd — al-Qāsim ibn "
         "Sallām (m. 224/838) ; Isḥāq — ibn Rāhawayh (m. 238/853)."),
        ("Le khulʿ pour nuisance. Mālik dit : « quant à la rachetante qui se "
         "rachète de son mari — si l'on sait que son mari lui a fait nuisance, "
         "l'a contrainte, et que l'on sait qu'il est injuste envers elle, le "
         "divorce a suivi son cours, et il lui a rendu son bien » — « c'est ce "
         "que j'entendais, et ce sur quoi est l'affaire des gens chez nous » "
         "[n° 1778]. La leçon ordonne ensuite les trois cas. Lorsque la nuisance "
         "vient de l'épouse et l'aversion du côté du mari : point de désaccord "
         "sur la licéité du khulʿ. Lorsqu'elle vient des deux à la fois : "
         "quelques-uns des anciens (al-qarawiyyūn) l'ont dit — il ne convient "
         "point que l'on khulʿe l'épouse sur cela, en prenant d'elle quelque "
         "chose — et c'est, dit-il, ce qui est reçu textuellement des savants qui "
         "nous ont précédés ; les notes observent que la nisba peut viser les "
         "juristes de Qayrawān ou les hommes des premières générations, mais que "
         "la suite — « reçu textuellement de ceux de nos savants qui ont "
         "précédé » — favorise le sens des autorités anciennes. Ce cas n'est "
         "point comme la question des deux arbitres (al-ḥakamayn) : quand la "
         "nuisance vient d'elle, cela y est licite — car l'examen de la question "
         "des deux arbitres appartient aux deux arbitres, et leur sentence s'y "
         "exécute (an-Nisāʾ, verset 35, cf. notes). Le qāḍī Abū l-Walīd — qu'Allah "
         "l'agrée — a dit : « si cela est licite dans la question des deux "
         "arbitres, alors il est plus digne encore qu'il soit licite aux deux "
         "[époux], lorsqu'ils s'accordent dessus » — al-Bājī (m. 474/1081, cf. "
         "notes), auteur du Muntaqā, le commentaire mālikite du Muwaṭṭaʾ."),
        ("L’ʿidda de la femme khulʿée : ʿAbdallāh ibn ʿUmar a dit — son ʿidda est "
         "l’ʿidda de la répudiée ; preuve que la femme khulʿée observe l’ʿidda comme "
         "l'observe la répudiée — il veut la répudiée qui n'a point reçu de "
         "contrepartie en échange ; le sens en est que l’ʿidda du divorce ne varie "
         "point avec la variation du divorce : elle est identique dans le divorce "
         "par khulʿ moyennant contrepartie et dans le divorce originaire sans "
         "contrepartie. Dans le Muwaṭṭaʾ, Mālik rapporte qu'il lui est parvenu "
         "que Saʿīd ibn al-Musayyab, Sulaymān ibn Yasār et Ibn Shihāb disaient : "
         "« l’ʿidda de la femme khulʿée est comme l’ʿidda de la répudiée : trois "
         "ʿiddas de règles (qurūʾ) » [n° 1781] — pour celle qui est du nombre des "
         "réglées (dhāt al-aqrāʾ) ; et ils n'ont point voulu dire par là qu'elle "
         "ne lui équivaut que dans les règles, mais elle lui équivaut dans l’ʿidda "
         "de la grossesse, celle des mois et celle de la douteuse (al-murātaba), "
         "comme elle lui équivaut dans l'observation des règles — la mesure "
         "recoupe celle posée à la leçon 12 pour toute épouse touchée puis "
         "séparée. Puis le débat qui clôt l'analyse : le khulʿ est-il divorce ou "
         "rupture ? Les Mālikites ont dit : le khulʿ est divorce — le mari a pris "
         "une contrepartie sur l'envoi de ce qu'il possède, et celui qui possède "
         "le divorce, non la rupture (faskh) ; et une autre face : toute "
         "séparation pour laquelle demeure valide le maintien du mariage avec sa "
         "cause est divorce — comme la séparation des copropriétaires (al-ʾinān) "
         "et celle du miséreux (al-muʿsir) par la pension. Ash-Shāfiʿī a dit le "
         "contraire — le khulʿ est rupture, et il n'est point divorce — et tel "
         "est le dire d'Ibn ʿAbbās ; l'argument, rapporté par Ibn ʿUyayna "
         "d'après ʿAmr ibn Dīnār, d'après Ṭāwūs : Ibrāhīm ibn Saʿd ibn Abī Waqqāṣ "
         "l'interrogea — un homme a répudié son épouse de deux répudiations, puis "
         "elle s'est khulʿée de lui ; peut-il l'épouser ? « oui — qu'il l'épouse ; "
         "le khulʿ n'est point divorce. Dieu a mentionné le divorce au début de "
         "l'āya et à sa fin, et le khulʿ se tient entre les deux — le khulʿ n'est "
         "donc point de cela. » — puis il lut 2:227 et 2:228, références imprimées "
         "concordantes. Abū ʿUmar rapporte quʿUthmān et des compagnons l'ont "
         "contredit et ont dit : le khulʿ est une répudiation unique, sauf s'il "
         "entend par elle davantage — alors il est ce qu'il a voulu et nommé ; le "
         "Muwaṭṭaʾ, récit de Muḥammad ibn al-Ḥasan, porte le cas d'Umm Bakr "
         "al-Aslamiyya, qu'elle se khulʿa de son mari ʿAbdallāh ibn Usayd — tous "
         "deux vinrent à ʿUthmān ibn ʿAffān qui dit : « c'est une répudiation, "
         "sauf si elle a nommé quelque chose — alors c'est ce qu'elle a nommé » ; "
         "Abū ʿUmar en tire que la femme khulʿée de ce hadīth n'a ni nommé divorce "
         "ni voulu — et Dieu sait mieux ; si elle avait nommé ou voulu, on "
         "n'aurait point eu besoin de dire que le khulʿ est une répudiation."),
        ("L'exploitation arme deux textes. Le premier est mālikite : « si la "
         "femme se rachète de son mari contre quelque chose, à condition qu'il la "
         "répudie, et qu'il la répudie d'un divorce suivi, successif (mutatābiʿan "
         "nasqan), cela est établi sur lui ; s'il y a entre cela des silences "
         "(ṣumāt), ce qu'il a suivi après les silences n'est point de chose » "
         "[n° 1783] — les répudiations enchaînées sans intervalle s'imputent au "
         "khulʿ ; ce qui suit les pauses n'entre point dans la contrepartie "
         "convenue ; les notes explicitent les termes — le mutatābiʿan nasqan, "
         "les répudiations enchaînées sans intervalle ; les ṣumāt, les pauses qui "
         "s'y intercalent. Le second est moderne : « si les époux s'accordent sur "
         "le principe du khulʿ et divergent sur la contrepartie, l'affaire est "
         "portée au tribunal, en vue de tenter la réconciliation entre eux ; si "
         "la réconciliation s'avère impossible, le tribunal juge le khulʿ "
         "exécutoire après en avoir estimé la contrepartie, en tenant compte du "
         "montant de la dot, de la durée du mariage, des motifs de la demande de "
         "khulʿ et de la situation matérielle de l'épouse » [Code de la famille, "
         "article 120] — les exercices demandent d'extraire du premier hadīth le "
         "statut du divorce par khulʿ et d'expliciter, à partir du texte du Code, "
         "ce qui doit être observé dans l'estimation de la contrepartie. "
         "L'évaluation fixe les trois questions de révision : la quantité de ce "
         "dont l'épouse se libère de son mari ; les dits des jurisconsultes sur "
         "le khulʿ, divorce ou rupture ; le dire dʿAbdallāh ibn ʿUmar — « son "
         "ʿidda est l’ʿidda de la répudiée ». La préparation préalable tourne la "
         "page : « Définis le liʿān en langue et en terme » ; « Quel est le "
         "statut de l'un des deux époux qui refuse le liʿān ? » ; « Explique la "
         "manière du liʿān » — les notes renvoient au serment d'anathème des "
         "sourates an-Nūr, versets 6-9, par lequel chacun des deux époux atteste "
         "quatre fois par Dieu sa parole et invoque, à la cinquième, la "
         "malédiction de Dieu sur le menteur ; c'est la leçon 14 du livre "
         "(Dispositions pour maudire) qui porte ces dispositions — la boucle "
         "d'iʿdād du livre tenue."),
    ],
    "points": [
        ("Fil de révision : trois objectifs (reconnaître le concept du khulʿ et son "
         "statut dans la Loi ; distinguer le divorce par khulʿ des autres divorces ; "
         "saisir la sagesse du divorce par khulʿ) → préambule (la femme qui désire le "
         "divorce sans tort du mari — « afin que le mari ne perde pas ce qu'il a "
         "dépensé pour son épouse en mahr », et que le lien ne demeure pas « une "
         "attache au cou de l'épouse, un carcan dont elle ne peut briser le sceau »)."),
        ("Le n° 1776 : la scène du ghalas avant l'aube — « quelle est ta situation ? » "
         "— « ni moi ni Thābit ibn Qays » — « elle a mentionné ce qu'Allah a voulu "
         "qu'elle mentionne » — « tout ce qu'il m'a donné, je le tiens » — "
         "« prends-le d'elle » — « Il le prit d'elle, et elle s'assit dans sa "
         "famille »."),
        ("Le commentaire mālikite [n° 1782] : la rachetante « ne retourne à son mari "
         "que par un mariage nouveau » — pas de double ʿidda si rompu avant "
         "attouchement — « le plus beau que j'aie entendu en cela »."),
        ("Le lexique : al-ghalas — « ce qui demeure de la nuit — l'obscurité de son "
         "dernier tiers » ; mā shaʾnuk — « quel est ton ordre et ton état ? » ; "
         "duplication des deux entrées dans l'imprimé, dédupliquée en traduction."),
        ("Le concept : en langue l'éloignement, du « retrait du vêtement » — les "
         "époux « un habit pour l'autre » (2:187 ; l'imprimé porte « verset 186 », "
         "42ᵉ écart de la série al-Baqara, consigné par la traduction) ; en terme la "
         "ṣifa ḥukmiyya qui lève la licéité moyennant contrepartie."),
        ("Le statut : la licéité — 2:227 (référence imprimée concorde) ; nul grief "
         "sur l'épouse qui paie ni sur le mari qui accepte ; le jardin d'Ibn ʿAbbās "
         "[La Sunan al-Kubrā de al-Bayhaqī] ; le verset du rachat — vide au scan, "
         "reconstruction raisonnée 2:229."),
        ("La quantité : un dit — pas davantage que le mahr (Saʿīd ibn al-Musayyab : "
         "« qu'il lui laisse quelque chose ») ; un autre — davantage si nushūz et "
         "nuisance viennent d'elle (Mālik, ash-Shāfiʿī, Abū Thawr)."),
        ("Le khulʿ pour nuisance [n° 1778] : injustice du mari — divorce suivi de "
         "son cours et bien rendu ; nuisance d'elle — accord ; nuisance des deux — "
         "réticence des anciens (al-qarawiyyūn) ; al-Bājī : à plus forte raison les "
         "deux époux d'accord (analogie des deux arbitres — an-Nisāʾ 35)."),
        ("L’ʿidda [n° 1781] : « l’ʿidda de la femme khulʿée est comme l’ʿidda de la "
         "répudiée : trois ʿiddas de règles » (la réglée) — équivalence grossesse, "
         "mois, murātaba ; divorce ou rupture : Mālikites divorce / ash-Shāfiʿī et "
         "Ibn ʿAbbās rupture (« le khulʿ se tient entre les deux ») / ʿUthmān "
         "répudiation unique (Umm Bakr)."),
        ("L'exploitation : n° 1783 — mutatābiʿan nasqan, les ṣumāt annulent ce qui "
         "suit ; Code de la famille article 120 — tribunal, réconciliation, "
         "contrepartie estimée (dot, durée du mariage, motifs, situation de "
         "l'épouse) ; l'iʿdād annonce le liʿān — la leçon 14 du livre."),
    ],
    "vocabulaire": [
        {"ar": "الخلع", "translit": "al-khulʿ",
         "fr": "le divorce par khulʿ : en langue l'éloignement, du retrait du vêtement — chacun des deux époux retire et dépouille de lui l'attache (ʿiṣma) du mariage moyennant une contrepartie"},
        {"ar": "الغلس", "translit": "al-ghalas",
         "fr": "le reste de l'obscurité : ce qui demeure de la nuit, l'obscurité de son dernier tiers — Ḥabība attendait à la porte du Messager de Dieu dès le dernier tiers de la nuit"},
        {"ar": "ما شأنك", "translit": "mā shaʾnuk",
         "fr": "« quelle est ta situation ? » : quel est ton ordre et ton état — la question prophétique qui ouvre l'entretien de Ḥabība"},
        {"ar": "المفدية", "translit": "al-mufḍiyya",
         "fr": "la rachetante : la femme qui se rachète de son mari — « elle ne retourne à son mari que par un mariage nouveau » (n° 1782)"},
        {"ar": "النشوز", "translit": "an-nushūz",
         "fr": "la rébellion : quand elle vient de l'épouse, la contrepartie peut excéder le mahr donné — le dire de Mālik et d'ash-Shāfiʿī"},
        {"ar": "قروء", "translit": "qurūʾ",
         "fr": "les règles : la mesure de l’ʿidda — « l’ʿidda de la femme khulʿée est comme l’ʿidda de la répudiée : trois ʿiddas de règles » (n° 1781, pour la réglée)"},
        {"ar": "الفسخ", "translit": "al-faskh",
         "fr": "la rupture : la résiliation de la racine du contrat, opposée au ṭalāq, la prérogative du mari — ash-Shāfiʿī tient le khulʿ rupture, les Mālikites divorce"},
        {"ar": "الصمات", "translit": "aṣ-ṣumāt",
         "fr": "les silences : les pauses entre répudiations enchaînées — « ce qu'il a suivi après les silences n'est point de chose » (n° 1783)"},
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
com[DOCID] = norme_entree(E_13074)

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
    print('   MANQUE :', f[:80])
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
    ('12991 — la dot, pilier', fr('12991').count('pilier') >= 2),
    ('12992 — l’ʿidda de trois règles', 'l’ʿidda de trois règles' in fr('12992')),
    ('13079 — le liʿān', 'liʿān' in fr('13079')),
    ('13074 — lʿattache (ʿiṣma) du mariage', 'l’attache (ʿiṣma) du mariage' in corpus),
]
ok = 0
for nom, b in ancres:
    print('recoupement :', 'PASS' if b else 'ÉCHEC', '—', nom)
    ok += 1 if b else 0
if ok != len(ancres):
    mauvais += len(ancres) - ok

print('contrôle ponctuation/arabe FR + citations + recoupements :', 'PASS' if mauvais == 0 else f'ÉCHEC ({mauvais})')

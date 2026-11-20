#!/usr/bin/env python3
"""R769 — ajoute le commentaire pédagogique de la leçon 14 de hadith-tanawi-1
(13079 أحكام اللعان — les dispositions du liʿān, « Dispositions pour maudire »,
la quatorzième du livre, étiquetée « leçon 18 » par l'imprimé (الدرس 18) —
le SUIVANT de R768, 13074, selon l'ordre des leçons du registre :
12925 … 12992, 13074, puis 13079)
à content/commentaires/hadith-tanawi-1.json.

Même protocole que comm-r768-c13.py : normalisation de la ponctuation FR
(U+202F avant ; : ! ? » et après «, apostrophe courbée) sur l'entrée
nouvelle seulement — opération idempotente. Rédaction d'après la lecture
complète de la leçon (htmlFr intégral, ~11 500 caractères après débalisage ;
couche arabe lue en entier pour l'étiquette de l'imprimé « (الدرس 18) »,
les références coraniques de la couche arabe — سورة النور من الآية 8 et
سورة النور الآية 6-9, sans texte de verset imprimé — et les sections non
traduites en français : كيفية اللعان (les quatre attestations), هل اللعان
فسخ أو طلاق؟, أثر تكذيب الملاعن نفسه (لحوق الولد et التفرقة أو عدمها),
التقويم, الاستثمار (n° 1788) et الإعداد القبلي).
Règle 2 de LISEZ-MOI.md : aucune invention — les numéros du Muwaṭṭaʾ
(1784, 1787 ; et 1788 dans la couche arabe), les attributions (Ibn Shihāb,
as-Sahl ibn Saʿd as-Sāʿidī, Uwaymir al-ʿAjlānī, ʿĀsim ibn ʿAdīy al-Anṣārī,
Ibn ʿArifa, « Al-Muḥallib ibn ʿAbd al-Barr », ʿUthmān al-Battī, an-Nawawī,
Sahnūn, Ishāq, Abū Thawr, Ibn Masʿūd, al-Layth, Saʿīd ibn Ǧubayr, Ibn ʿUmar,
ʿĪsā d'Ibn al-Qāsim), les rapports (Muslim, Abū Dāwūd, al-Bayhaqī, al-Buḫārī)
sont cités tels qu'ils figurent dans la leçon. Les formes arabes du
vocabulaire sont reprises de la couche arabe ou dérivées des
translittérations de la leçon, sans harakat (règle 3).

Garde-fous (convention des vagues R765-R768) :
- verif-citations intégrée : chaque fragment « » de l'entrée doit être
  retrouvé verbatim dans le htmlFr de la leçon (0 manquant, abort sinon) ;
- recoupements : ancres vérifiées dans les leçons voisines (13074 — la
  préparation préalable annonce le liʿān et porte le débat divorce/rupture
  du khulʿ ; 12992 — le muḥallil, l'autre mariage à jamais interdit ;
  13101 — la leçon suivante du registre).
"""
import json, re, sys
import html as H

CHEMIN = 'content/commentaires/hadith-tanawi-1.json'
LIVRE = 'content/books/hadith-tanawi-1.json'
DOCID = '13079'

E_13079 = {
    "auteur": "IA-1, tour R769",
    "resume": (
        "Guide de lecture de la leçon 14 (أحكام اللعان — les dispositions du liʿān, "
        "« Dispositions pour maudire »), la quatorzième du livre, étiquetée leçon 18 "
        "par l'imprimé (الدرس 18) : le hadīth d'Uwaymir al-ʿAjlānī arme le fond — le "
        "n° 1784, que Mālik rapporte d'Ibn Shihāb, qu'as-Sahl ibn Saʿd as-Sāʿidī lui "
        "a rapporté — Uwaymir al-ʿAjlānī vint chez ʿĀsim ibn ʿAdīy al-Anṣārī et lui "
        "dit : « Ô ʿĀsim, qu'en penses-tu d'un homme qui trouve un homme avec sa "
        "femme ? Doit-il le tuer, et le tuez-vous ? Ou comment doit-il s'y prendre ? » ; "
        "ʿĀsim interrogea le Messager de Dieu — paix et bénédiction sur lui —, qui "
        "détesta les questions, les blâma, jusqu'à ce que ce qu'ʿĀsim entendit lui "
        "parût lourd ; Uwaymir — « Par Allah, je n'arrêterai pas tant que je ne "
        "l'aurai pas interrogé à ce sujet. » — s'avança alors en pleine assemblée, et "
        "le Messager de Dieu dit : « Une révélation a été descendue en toi et en ton "
        "épouse. Va donc et amène-la. » ; as-Sahl rapporte la mutuelle maudiction "
        "devant les gens — et lorsque les deux eurent achevé, Uwaymir dit : « Je "
        "mens sur elle, ô Messager d'Allah, si je la reprends. » — « Il la répudia "
        "donc trois fois » avant même que l'ordre prophétique ne lui en soit donné ; "
        "Ibn Shihāb : « Cela devint par la suite la coutume des personnes qui se "
        "maudissent mutuellement. » [n° 1784] — le numéro qui succède directement "
        "aux numéros du khulʿ (1776-1783) de la leçon 13. Le second texte fonde la "
        "coutume madhabite [n° 1787] : « Notre coutume est que les personnes qui se "
        "maudissent mutuellement ne peuvent jamais se marier. S'il accuse faussement "
        "sa propre personne, il est fouetté de la peine légale, l'enfant est "
        "rattaché à lui, et elle ne peut jamais revenir à lui. » — « C'est sur "
        "cette coutume, qui ne fait aucun doute et ne prête à aucune divergence, "
        "que repose notre pratique. » Le tamhīd fonde l'institution : "
        "l'établissement de l'adultère par quatre témoins intègres est extrêmement "
        "difficile — Dieu a donc institué « pour l'époux un cas exceptionnel "
        "particulier lui permettant d'intenter une action en adultère contre son "
        "épouse s'il la surprend en flagrant délit, sans être astreint à produire "
        "des témoins, et sans encourir la peine de la calomnie ». La définition : "
        "en langue, une dérivée de laʿana (maudire), l'éloignement et le rejet ; en "
        "terme, « des paroles déterminées qui ont été établies comme preuve pour "
        "celui qui est contraint de calomnier celui qui a souillé son lit et lui a "
        "apporté la honte, ou pour un enfant » ; Ibn ʿArifa la resserre ; la raison "
        "de l'appellation — « nom du tout par une partie », et chacun des deux "
        "maudisseurs éloigne l'autre par cela — « le mariage est interdit à jamais » "
        "— le choix du terme plutôt que le témoignage ou la colère, « une chose est "
        "publiée sous ce qui y est d'étranger ». Le statut : le liʿān « n'est permis "
        "qu'en cas de certitude » ; obligatoire quand il « vise à nier la grossesse, "
        "il est obligatoire » — le rattachement d'un enfant à un père qui n'est pas "
        "le sien — « le changement des droits et des dispositions dans l'héritage et "
        "le mariage » ; préférable d'éviter pour l'accusation d'adultère, « par "
        "prudence pour le voile » — le Prophète se détourne quatre fois de celui qui "
        "s'accuse (« J'ai commis l'adultère », Rapporté par Muslim dans son Sahih) et "
        "dit à celui qui avait ordonné à un homme de s'accuser : « Si tu l'avais "
        "couvert de ton vêtement, cela aurait été meilleur pour toi. » (Rapporté par "
        "Abū Dāwūd dans son Sunan). Les dispositions déploient les divergences : la "
        "séparation — l'école de Mālik la fait tomber « par le maudissement de la "
        "femme » ; le Shafiʿite et Sahnūn dès que l'époux a fini de maudire — « car "
        "le maudissement de la femme n'a été institué que pour lui éviter la peine "
        "légale » ; Abū Ḥanīfa seulement par le jugement du juge — « une séparation "
        "par répudiation » — deux rapports d'Aḥmad ; ʿUthmān al-Battī par l'acte de "
        "l'époux seul — réfuté : « que c'est un avis que nul des Compagnons ne lui a "
        "précédé dans son adoption » — an-Nawawī lit la triple répudiation d'Uwaymir "
        "comme une volonté d'« interdire à perpétuité ». Le lieu : la grande mosquée, "
        "« ne peut avoir lieu qu'en présence du souverain », le délégué « tient lieu "
        "d'Imam ». Les refusants : l'époux qui refuse — « s'il refuse de maudir, il "
        "est frappé de la peine légale » (le liʿān « est une acquittement pour "
        "l'époux, comme le témoignage pour un étranger ») ; l'épouse — Mālik, le "
        "Shafiʿite, Ishāq, Abū Thawr et la majorité des Salaf la font frapper de la "
        "peine légale, pour preuve le verset cité ; Abū Ḥanīfa : « Si elle refuse de "
        "maudir, elle sera détenue à perpétuité jusqu'à ce qu'elle maudisse. » La "
        "procédure s'ouvre sur « le verset d'Allah, le Très-Haut ». NB consignés "
        "(sans correction, règle 5) : (1) les deux emplacements coraniques de la "
        "leçon portent en couche française un même texte de verset — celui du verset "
        "du fouet (an-Nūr 2) — sous l'étiquette « verset 8 » pour l'argument du "
        "refus de l'épouse (arabe : سورة النور من الآية 8) et sous l'étiquette "
        "« versets 6-9 » pour l'origine de la procédure (arabe : سورة النور الآية "
        "6-9 — les versets du liʿān) : la couche arabe ne porte aucun texte de "
        "verset, la première étiquette est vraisemblablement écartée (le texte du "
        "hadd porte le verset 2), la seconde est juste mais l'emplacement est rempli "
        "du texte du hadd au lieu des versets du liʿān ; (2) la traduction rend "
        "« Al-Muḥallib ibn ʿAbd al-Barr » là où l'arabe porte (ابن عبد البر — Ibn ʿAbd "
        "al-Barr), et la définition d'Ibn ʿArifa est rendue « L'épux jure par Allah "
        "sur l'adultère de son épouse ou sur le fait qu'elle nie sa grossesse, ce "
        "qui l'oblige à répudier » — l'arabe porte (حلف الزوج) — six occurrences de "
        "« l'épux » pour l'époux, « une acquittement », « maudissement mutuelle », "
        "« ce divergent apparait » ; (3) la couche française s'arrête à l'ouverture "
        "même de la procédure du liʿān — la couche arabe poursuit et complète : la "
        "forme du liʿān (كيفية اللعان) — quatre attestations du mari, la cinquième "
        "porte la malédiction s'il est du nombre des menteurs ; quatre attestations "
        "de l'épouse, la cinquième porte la colère si l'époux est du nombre des "
        "véridiques — variante d'al-Layth ; le débat faskh/ṭalāq (هل اللعان فسخ أو "
        "طلاق؟) — le qāḍī Abū l-Ḥasan rupture (l'interdit à jamais, comme le "
        "rachât), le qāḍī Abū l-Walīd répudiation (l'abolition à jamais tient à sa "
        "cause), avec une seconde rédaction attribuant au même qāḍī l'argument "
        "contraire — consignée sans correction ; l'effet de la rétraction du "
        "maudisseur (أثر تكذيب الملاعن نفسه) — l'enfant rattaché avant comme après, "
        "ʿĪsā d'Ibn al-Qāsim dans l'ʿUtbiyya (la pension de grossesse, le salaire de "
        "l'allaitement, l'entretien à suivre), la rétraction avant l'achèvement "
        "châtiée sur le mariage selon Mālik, après l'achèvement — jamais elle ne "
        "redevient licite — contre Abū Ḥanīfa qui lève l'interdit, les Mālikites "
        "arguant du hadīth d'Ibn ʿUmar rapporté par al-Buḫārī (le Prophète dit au "
        "mari qu'il n'y a point de voie pour lui sur elle) ; l'évaluation (التقويم) "
        "demande le statut avec preuve, la forme, et le débat rupture ou répudiation "
        "— le même que la leçon 13 posait du khulʿ ; l'exploitation (الاستثمار) "
        "porte le n° 1788 — le liʿān après la séparation irrévocable, le déni de "
        "grossesse et la durée de doute ; la préparation préalable (الإعداد القبلي) "
        "annonce les mots (ملكها) et (البتة), le statut de la triple répudiée avant "
        "l'attouchement et le jugement de l'héritage de la répudiée malade."
    ),
    "explication": [
        ("La leçon 14 — la quatorzième du livre, étiquetée leçon 18 par l'imprimé "
         "(الدرس 18) — porte les dispositions du liʿān : la procédure par laquelle, "
         "lorsque le mari accuse son épouse d'adultère sans pouvoir établir sa "
         "preuve, chacun des deux époux atteste quatre fois par Dieu sa parole et "
         "invoque, à la cinquième, la malédiction de Dieu sur le menteur. Elle "
         "répond point par point à la préparation préalable de la leçon 13, qui "
         "demandait de définir le liʿān en langue et en terme, de donner le statut "
         "de l'un des deux époux qui refuse le liʿān et d'expliquer la manière du "
         "liʿān — la boucle annoncée par l'iʿdād du khulʿ est ici bouclée. Trois "
         "objectifs l'ouvrent : connaître les dispositions du liʿān et la raison de "
         "son appellation ; comprendre ses causes et « la sagesse divine "
         "sous-jacente » ; s'efforcer d'expliquer aux gens la gravité des causes "
         "qui mènent au liʿān. Le texte est tiré du Livre du hadīth du Muwaṭṭaʾ de "
         "l'imam Mālik avec le commentaire d'az-Zurqānī — la première année de "
         "l'enseignement secondaire traditionnel (ʿatīq), première phase."),
        ("Le tamhīd pose la situation de départ : l'établissement de l'adultère par "
         "quatre témoins intègres — « attestant avoir vu tel ou telle en flagrant "
         "délit d'adultère » — est extrêmement difficile, et « il est rare qu'il se "
         "produise eu égard aux conditions requises » ; Dieu a donc institué pour "
         "l'époux « un cas exceptionnel particulier lui permettant d'intenter une "
         "action en adultère contre son épouse s'il la surprend en flagrant délit, "
         "sans être astreint à produire des témoins, et sans encourir la peine de "
         "la calomnie » — ce cas exceptionnel est le liʿān. Les deux questions "
         "d'ouverture — « Quelles sont ses dispositions ? » — distribuent "
         "l'analyse : d'abord la définition et le statut, puis les dispositions."),
        ("Le texte fondateur est le hadīth d'Uwaymir al-ʿAjlānī (Muwaṭṭaʾ n° 1784), "
         "que Mālik rapporte d'Ibn Shihāb, qu'as-Sahl ibn Saʿd as-Sāʿidī lui a "
         "rapporté. La scène s'ouvre sur la question d'Uwaymir à ʿĀsim ibn ʿAdīy "
         "al-Anṣārī : « Ô ʿĀsim, qu'en penses-tu d'un homme qui trouve un homme "
         "avec sa femme ? Doit-il le tuer, et le tuez-vous ? Ou comment doit-il "
         "s'y prendre ? » — demander d'abord s'il doit tuer, puis comment s'y "
         "prendre ; et « Interroge-moi, ô ʿĀsim, à ce sujet » le Messager de Dieu. "
         "ʿĀsim interrogea — et le Messager de Dieu — paix et bénédiction sur lui "
         "— « détesta les questions, les blâma », jusqu'à ce que ce qu'ʿĀsim "
         "entendit lui parût lourd. Lorsqu'ʿĀsim retourna auprès des siens, "
         "Uwaymir vint le trouver et lui demanda ce que le Messager de Dieu avait "
         "dit ; ʿĀsim : « Tu n'apportes pas de bonnes nouvelles. » Uwaymir — "
         "« Par Allah, je n'arrêterai pas tant que je ne l'aurai pas interrogé à "
         "ce sujet. » — et l'insistance porte le cas devant l'assemblée : la "
         "sentence prophétique tombe — « Une révélation a été descendue en toi et "
         "en ton épouse. Va donc et amène-la. » As-Sahl, présent auprès des gens, "
         "rapporte la mutuelle maudiction ; et lorsque les deux eurent achevé "
         "leur maudiction, Uwaymir dit : « Je mens sur elle, ô Messager d'Allah, "
         "si je la reprends. » — « Il la répudia donc trois fois » avant même que "
         "l'ordre prophétique ne lui en soit donné : la répudiation triple, "
         "anticipée, que l'analyse des dispositions cherchera à situer. Et la "
         "sunna d'Ibn Shihāb : « Cela devint par la suite la coutume des "
         "personnes qui se maudissent mutuellement. » — la pratique née du fait "
         "prophétique lui-même."),
        ("La compréhension s'ouvre par l'explication du premier terme : le "
         "Messager de Dieu a détesté les questions — trois lectures sont "
         "proposées : « soit parce qu'il détestait que l'homme calomnie sa femme "
         "sans preuve, par crainte de la peine légale » ; « soit parce qu'il "
         "détestait la question en raison de la gravité de l'affaire et de la "
         "violation du voile du musulman » ; « soit parce qu'il avait interdit de "
         "poser trop de questions ». Les trois lectures se rangent sous le même "
         "principe : le voile du musulman vaut mieux que l'ouverture d'une "
         "accusation, et la question d'Uwaymir touchait aux trois — le libelle "
         "sans preuve, la gravité de l'affaire, l'excès des questions."),
        ("Le second hadīth fixe la coutume (Muwaṭṭaʾ n° 1787) : « Notre coutume "
         "est que les personnes qui se maudissent mutuellement ne peuvent jamais "
         "se marier. S'il accuse faussement sa propre personne, il est fouetté de "
         "la peine légale, l'enfant est rattaché à lui, et elle ne peut jamais "
         "revenir à lui. » — la triple conséquence de la rétraction : le fouet du "
         "libelle (il accuse sa propre personne faussement, le hadd de la "
         "calomnie s'impose), le rattachement de l'enfant, l'interdiction à "
         "jamais du retour ; et la fermeture : « C'est sur cette coutume, qui ne "
         "fait aucun doute et ne prête à aucune divergence, que repose notre "
         "pratique. » — la coutume madhabite ne souffle aucune divergence, là où "
         "les dispositions vont déploier divergences sur divergences : le texte "
         "installe le socle certain avant d'ouvrir le champ du débat."),
        ("L'analyse commence par la définition. En langue, le liʿān est une "
         "dérivée de laʿana (maudire), « qui est l'éloignement et le rejet » — "
         "on dit atalaʿana pour celui qui se maudit lui-même et laʿana pour "
         "celui qui maudit un autre, l'épouse l'a maudit mulāʿinatan wa laʿanan, "
         "ils se sont maudits mutuellement. En terme, le liʿān est « des paroles "
         "déterminées qui ont été établies comme preuve pour celui qui est "
         "contraint de calomnier celui qui a souillé son lit et lui a apporté la "
         "honte, ou pour un enfant » — la preuve ouverte à celui qui est "
         "contraint, et pour un enfant : la définition embrasse d'entrée les "
         "deux motifs, l'accusation d'adultère et la négation de grossesse. Ibn "
         "ʿArifa la resserre : « L'épux jure par Allah sur l'adultère de son "
         "épouse ou sur le fait qu'elle nie sa grossesse, ce qui l'oblige à "
         "répudier » — et son épouse jure pour qu'il soit un menteur (NB : "
         "l'arabe porte حلف الزوج — la rédaction française est approximative et "
         "porte « l'épux », consigné sans correction). La raison de "
         "l'appellation : le liʿān contient le mot laʿna, « nom du tout par une "
         "partie », et chacun des deux maudisseurs éloigne l'autre par cela — "
         "« le mariage est interdit à jamais ». Et le choix du terme plutôt que "
         "le témoignage ou la colère, « bien que les paroles les contiennent "
         "aussi » — car la maudiction est « un terme étranger dans la "
         "constitution des preuves que sont les témoignages et les serments » — "
         "« une chose est publiée sous ce qui y est d'étranger » : le nom "
         "étranger dit lui-même le cas extraordinaire."),
        ("Le statut : il est établi que le liʿān « n'est permis qu'en cas de "
         "certitude » — sinon, il est interdit. Trois temps règlent les cas. Si "
         "le liʿān « vise à nier la grossesse, il est obligatoire » : son "
         "omission entraînerait « le rattachement d'un enfant à un père qui "
         "n'est pas le sien » — « le changement des droits et des dispositions "
         "dans l'héritage et le mariage » — le droit successoral et le droit "
         "matrimonial tout entiers basculeraient. Quant au cas où il vise à "
         "accuser l'épouse d'adultère, « il est préférable de l'éviter, par "
         "prudence pour le voile » : le Prophète — paix et bénédiction sur lui — "
         "s'est détourné de celui qui vint à lui en disant « J'ai commis "
         "l'adultère », jusqu'à ce qu'il le renvoie quatre fois — Rapporté par "
         "Muslim dans son Sahih — et il dit à celui qui avait ordonné à un homme "
         "de s'accuser d'adultère : « Si tu l'avais couvert de ton vêtement, "
         "cela aurait été meilleur pour toi. » — Rapporté par Abū Dāwūd dans son "
         "Sunan — « C'est-à-dire : tu l'as ordonné à couvrir » : la couverture "
         "du musulman prime la châtiment du fautif."),
        ("Les dispositions ouvrent sur le motif de la séparation entre les deux "
         "maudisseurs — dès la fin de leur maudiction mutuelle, ou de l'un "
         "d'eux, ou après le jugement. L'école de Mālik : la prohibition a lieu "
         "par le maudissement de la femme — la coutume d'Ibn Shihāb relue : « ce "
         "qui les rend interdits l'un pour l'autre à perpétuité, de manière "
         "apparente et cachée, que l'accusation soit vraie ou fausse » ; le "
         "hadīth d'al-Bayhaqī — « Les personnes qui se maudissent mutuellement "
         "ne peuvent jamais se réunir. » — son sens apparent requiert la "
         "mutuelle maudiction, mais Mālik tient la prohibition par le "
         "maudissement de l'épouse. Le Shafiʿite et Sahnūn : la prohibition dès "
         "que l'époux a fini de maudire — « car le maudissement de la femme "
         "n'a été institué que pour lui éviter la peine légale, contrairement "
         "à l'homme, pour qui s'ajoutent en plus la négation de la filiation, "
         "le rattachement de l'enfant et la rupture du lien conjugal » — et "
         "l'utilité de la divergence apparaît « dans l'héritage si l'un d'eux "
         "mourait après que l'homme eut achevé sa maudiction », et dans la "
         "répudiation suspendue à une autre séparation. Abū Ḥanīfa : la "
         "séparation n'a lieu que lorsque le juge l'ordonne — « une séparation "
         "par répudiation » — et « Il y a deux rapports concernant Aḥmad ». "
         "ʿUthmān al-Battī la fait tenir à l'acte de l'époux seul — le sens "
         "apparent du hadīth d'Uwaymir — « La séparation entre les personnes "
         "qui se maudissent n'a lieu que par l'acte de l'épux » — et soutient "
         "que « la séparation n'est pas mentionnée dans le Coran » ; la "
         "réfutation vient d'« Al-Muḥallib ibn ʿAbd al-Barr » (NB : l'arabe "
         "porte ابن عبد البر — consigné sans correction) : « que c'est un avis "
         "que nul des Compagnons ne lui a précédé dans son adoption » ; et "
         "l'argument interne : al-Battī recommande la répudiation après le "
         "liʿān, point avant — « a déjà produit un jugement ». An-Nawawī commente "
         "le dire d'Uwaymir — « est une phrase indépendante » — et sa répudiation "
         "« c'est-à-dire qu'il a ensuite suivi cela par sa répudiation » — car "
         "il a pensé que le liʿān ne l'interdisait pas à perpétuité, et « il a "
         "voulu l'interdire à perpétuité par la triple répudiation » : la "
         "triple répudiation d'Uwaymir, anticipée, redouble l'interdit déjà né "
         "du liʿān."),
        ("Le lieu du liʿān : les savants sont unanimes — « ne peut avoir lieu "
         "que dans la grande mosquée » — car le Messager de Dieu procéda au "
         "liʿān entre les maudisseurs dans sa mosquée, « ce qui est conservé "
         "dans le hadith d'Ibn Masʿūd et d'autres » ; et « ne peut avoir lieu "
         "qu'en présence du souverain » ; ils ne divergent pas sur celui que "
         "l'Imam a investi des jugements — « qu'il soit juge ou tout autre "
         "magistrat » — « tient lieu d'Imam » si les plaideurs s'y réfèrent. "
         "Le sort des refusants : l'époux qui refuse après avoir affirmé avoir "
         "vu l'acte ou après l'avoir calomniée — Mālik, le Shafiʿite et la "
         "majorité des juristes : « s'il refuse de maudir, il est frappé de la "
         "peine légale » — leur argument : le liʿān « est une acquittement "
         "pour l'époux, comme le témoignage pour un étranger » (NB : la faute "
         "d'accord, consignée sans correction) ; l'épouse qui refuse après "
         "que l'époux l'a maudie — Mālik, le Shafiʿite, Ishāq, Abū Thawr et "
         "la majorité des Salaf : « si elle refuse de maudir, elle est frappée "
         "de la peine légale » — pour preuve le verset cité (NB : le texte "
         "imprimé est celui du verset du fouet — an-Nūr 2 — sous l'étiquette "
         "« verset 8 », consigné sans correction) ; Abū Ḥanīfa et ses "
         "compagnons : « Si elle refuse de maudir, elle sera détenue à "
         "perpétuité jusqu'à ce qu'elle maudisse. » — la détention remplace "
         "le fouet chez l'école du raʾy. Et la procédure s'ouvre — « est le "
         "verset d'Allah, le Très-Haut » — référencé « versets 6-9 » (NB : "
         "l'emplacement est rempli du même texte du verset du fouet au lieu "
         "des versets du liʿān — consigné sans correction), puis la couche "
         "française s'arrête."),
        ("La couche arabe poursuit là où la traduction s'interrompt — NB "
         "majeur consigné. La forme du liʿān (كيفية اللعان) : le mari atteste "
         "quatre fois par Dieu avoir vu son épouse commettre l'adultère et "
         "porte, à la cinquième, la malédiction de Dieu sur lui s'il est du "
         "nombre des menteurs ; l'épouse atteste de même quatre fois qu'il ne "
         "l'a point vue et porte, à la cinquième, la colère de Dieu sur elle "
         "si l'époux est du nombre des véridiques — la malédiction pour le "
         "menteur, la colère pour le véridique ; al-Layth porte la variante "
         "des attestations — c'est la manière que la préparation de la leçon "
         "13 demandait d'expliquer. La couche arabe rouvre ensuite le débat "
         "(هل اللعان فسخ أو طلاق؟) : le qāḍī Abū l-Ḥasan fait de la séparation "
         "des mutalāʿinayn une rupture — l'interdit est à jamais, comme le "
         "rachât ; le qāḍī Abū l-Walīd la fait répudiation — le faskh ne "
         "s'abolit point de lui-même, l'abolition à jamais tient à sa cause, "
         "comme le rachât — avec, à l'appui, le hadīth de Saʿīd ibn Ǧubayr "
         "d'après Ibn ʿUmar rapporté par al-Buḫārī : le Prophète dit au mari "
         "des mutalāʿinayn qu'il n'y a point de voie pour lui sur elle — puis "
         "une seconde rédaction attribue au même qāḍī Abū l-Walīd l'argument "
         "contraire (ils sont vaincus par la séparation sans acte effectué, "
         "et la répudiation ne se produit que par l'acte d'un répudiateur) — "
         "rédaction consignée sans correction. L'effet de la rétraction du "
         "maudisseur (أثر تكذيب الملاعن نفسه) occupe deux sections non "
         "traduites : l'enfant est rattaché au maudisseur rétracté avant ou "
         "après le liʿān — avant la mutuelle maudiction, il est châtié et "
         "n'avait point le droit de maudire ; après sa maudiction mais avant "
         "celle de l'épouse, il est châtié et le liʿān d'elle tombe — et la "
         "couche arabe ajoute, d'après ʿĪsā d'Ibn al-Qāsim dans l'ʿUtbiyya, la "
         "pension de la grossesse, le salaire de l'allaitement et l'entretien "
         "à suivre ; la séparation — si la rétraction précède l'achèvement du "
         "liʿān, Mālik châtie les deux sur leur mariage : le liʿān n'est pas "
         "achevé, ils demeurent sur le statut de la conjugalité, et la "
         "séparation ne se produit que par l'achèvement — une fois le liʿān "
         "accompli, elle est à jamais interdite ; si la rétraction suit "
         "l'achèvement, jamais elle ne lui redeviendra licite — et Abū Ḥanīfa "
         "lève l'interdit et permet le remariage, contre les Mālikites qui "
         "arguent du hadīth d'Ibn ʿUmar rapporté par al-Buḫārī. L'évaluation "
         "(التقويم) demande le statut du liʿān avec preuve, sa forme, et les "
         "dits des jurisconsultes sur la rupture ou la répudiation — le même "
         "débat que la leçon 13 posait du khulʿ, désormais transporté au "
         "liʿān. L'exploitation (الاستثمار) porte le n° 1788 : le mari qui a "
         "séparé sa femme par une séparation irrévocable sans retour, puis "
         "nie sa grossesse et la maudit — la grossesse ressemble à être de "
         "lui tant qu'elle le réclame avant que la durée de doute ne soit "
         "écoulée — le manuel demande d'en extraire les conditions de la "
         "mutuelle maudiction après divorce et son rapport aux hadīths de la "
         "leçon. Et la préparation préalable (الإعداد القبلي) annonce la leçon "
         "suivante de l'imprimé : les mots (ملكها) et (البتة), le statut de la "
         "triple répudiée avant l'attouchement, et le jugement de l'héritage "
         "de la répudiée en cas de maladie — la traduction française de la "
         "leçon s'arrête donc à l'ouverture même de la procédure, et ce "
         "silence de la traduction est consigné sans correction."),
    ],
    "points": [
        ("Fil de révision : trois objectifs (connaître les dispositions du liʿān et "
         "la raison de son appellation ; comprendre ses causes et la sagesse divine "
         "sous-jacente ; expliquer aux gens la gravité des causes qui mènent au "
         "liʿān) → tamhīd (quatre témoins rares → « cas exceptionnel » sans "
         "témoins ni peine de calomnie) → deux questions (définition, dispositions)."),
        ("Le n° 1784 : la scène — la question d'Uwaymir à ʿĀsim, la répugnance "
         "prophétique, « Tu n'apportes pas de bonnes nouvelles. », l'insistance en "
         "pleine assemblée, « Une révélation a été descendue en toi et en ton "
         "épouse », la mutuelle maudiction, « Je mens sur elle, ô Messager d'Allah, si je la reprends » "
         "— « Il la répudia donc trois fois » avant l'ordre ; la sunna d'Ibn "
         "Shihāb."),
        ("Le n° 1787 : « ne peuvent jamais se marier » ; la rétraction — fouet de "
         "la peine légale, l'enfant rattaché, jamais de retour ; « coutume, qui ne "
         "fait aucun doute et ne prête à aucune divergence »."),
        ("Les termes : trois lectures de la répugnance prophétique (la calomnie "
         "sans preuve et la crainte du hadd / la gravité et le voile / l'interdit "
         "des questions multiples)."),
        ("La définition : langue — l'éloignement et le rejet (laʿana) ; terme — "
         "« des paroles déterminées » pour celui qui est contraint, « ou pour un "
         "enfant » ; Ibn ʿArifa (NB « L'épux ») ; appellation — « nom du tout par "
         "une partie », « le mariage est interdit à jamais » ; le choix vs "
         "témoignage et colère — « une chose est publiée sous ce qui y est "
         "d'étranger »."),
        ("Le statut : certitude seule ; obligatoire pour la négation de grossesse "
         "(« le changement des droits et des dispositions dans l'héritage et le "
         "mariage ») ; préférable d'éviter pour l'accusation — « par prudence pour "
         "le voile » — Muslim (détourné quatre fois), Abū Dāwūd (« Si tu l'avais "
         "couvert de ton vêtement »)."),
        ("La séparation : Mālik (le maudissement de la femme) / le Shafiʿite et "
         "Sahnūn (la fin du maudissement de l'époux — la négation de filiation en "
         "plus) / Abū Ḥanīfa (le juge — une répudiation) / al-Battī (l'acte de "
         "l'époux — réfuté : nul Compagnon ne l'a précédé) / an-Nawawī (la triple "
         "répudiation pour interdire à perpétuité)."),
        ("Le lieu : la grande mosquée (unanimité — la mosquée prophétique, Ibn "
         "Masʿūd), le souverain, le délégué « tient lieu d'Imam »."),
        ("Les refusants : l'époux — peine légale (l'acquittement « comme le "
         "témoignage pour un étranger ») ; l'épouse — peine légale (Mālik, le "
         "Shafiʿite, Ishāq, Abū Thawr) / Abū Ḥanīfa : détenue à perpétuité "
         "jusqu'à maudire ; les deux emplacements de verset portent le texte du "
         "fouet — étiquettes « verset 8 » / « versets 6-9 » — écarts consignés."),
        ("La couche arabe non traduite : la forme (quatre attestations + cinquième "
         "— malédiction du menteur / colère sur le véridique ; al-Layth), le débat "
         "rupture/répudiation (Abū l-Ḥasan / Abū l-Walīd — rédaction double "
         "consignée), l'effet de la rétraction (l'enfant rattaché — ʿUtbiyya ; les "
         "deux châtiés sur leur mariage si avant l'achèvement), l'évaluation, "
         "l'exploitation (n° 1788 — la séparation irrévocable puis le déni de "
         "grossesse), la préparation (ملكها, البتة, la triple répudiée avant "
         "attouchement, l'héritage de la répudiée malade)."),
    ],
    "vocabulaire": [
        {"ar": "اللعان", "translit": "al-liʿān",
         "fr": "l'institution : en langue l'éloignement et le rejet, dérivée de laʿana (maudire) ; en terme « des paroles déterminées » établies comme preuve pour celui qui est contraint de calomnier celui qui a souillé son lit, ou pour un enfant"},
        {"ar": "الملاعنة", "translit": "al-mulāʿana",
         "fr": "la mutuelle maudiction des deux époux dans l'assemblée du juge — « Ils se maudirent mutuellement » (n° 1784), devant les gens et « ne peut avoir lieu qu'en présence du souverain »"},
        {"ar": "اللعن", "translit": "al-laʿna",
         "fr": "la maudiction : en langue « l'éloignement et le rejet » — « nom du tout par une partie », chaque maudisseur éloignant l'autre par cela"},
        {"ar": "التعان", "translit": "at-taʿān",
         "fr": "la maudiction de l'épouse : seule à faire tomber la prohibition selon l'école de Mālik — d'après la couche arabe (التعان المرأة)"},
        {"ar": "الشهادة", "translit": "ash-shahāda",
         "fr": "le témoignage : terme écarté au profit du liʿān — la maudiction est « un terme étranger dans la constitution des preuves que sont les témoignages et les serments »"},
        {"ar": "الغضب", "translit": "al-ghaḍab",
         "fr": "la colère : second terme écarté ; à la cinquième attestation de l'épouse la couche arabe porte la colère de Dieu si l'époux est du nombre des véridiques"},
        {"ar": "القذف", "translit": "al-qadhf",
         "fr": "la calomnie : l'accusation sans preuve — l'époux du liʿān « sans encourir la peine de la calomnie », le rétracté fouetté pour avoir accusé faussement sa propre personne"},
        {"ar": "الحد", "translit": "al-ḥadd",
         "fr": "la peine légale : le fouet du libelle — celui de l'époux qui refuse de maudir, celui de l'épouse qui refuse (Mālik, le Shafiʿite, Ishāq, Abū Thawr), la détention à perpétuité chez Abū Ḥanīfa"},
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
com[DOCID] = norme_entree(E_13079)

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
    ('13074 — la préparation préalable annonce le liʿān', 'Définis le liʿān en langue et en terme' in fr('13074')),
    ('13074 — le débat divorce ou rupture du khulʿ, repris ici pour le liʿān', 'khulʿ est-il divorce ou rupture' in fr('13074')),
    ('13079 — le hadīth d’Uwaymir al-ʿAjlānī', 'Uwaymir al-ʿAjlānī' in corpus),
    ('13079 — le verset du fouet aux deux emplacements', 'fouettez chacun d’eux cent coups' in corpus),
    ('12992 — le muḥallil, l’autre mariage à jamais interdit', 'muḥallil' in fr('12992')),
    ('13101 — la leçon suivante du registre (l’idda de la veuve)', 'ʿidda' in fr('13101')),
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

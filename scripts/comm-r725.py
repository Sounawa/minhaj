#!/usr/bin/env python3
"""R725 — ajoute les commentaires pédagogiques de la leçon 13 (pdf-mut23h2x-402,
les rites du jour de ʿArafa) et de la leçon 12 (pdf-mut23h2x-401, les règles du
saʿy entre Ṣafā et Marwa) à content/commentaires/hadith-3es.json.
Vague 9 : remontée du manuel (le SUIVANT de R724).
Même protocole que comm-r724.py : normalisation de la ponctuation FR (U+202F
avant ; : ! ? » et après «, apostrophe courbée) sur les entrées nouvelles
seulement — opération idempotente. Rédaction d'après la lecture complète des
deux leçons (htmlFr intégral, extraction non lossy en blocs complets,
scripts/extrait-r725.py). Les numéros du Muwaṭṭaʾ et les āyās sont cités tels
qu'ils figurent dans les leçons (règle 2 de LISEZ-MOI.md : aucune invention).
Les formes arabes du vocabulaire sont posées au squelette standard SANS
harakat — ces deux leçons ne portent pas les formes vocalisées du lexique dans
leur couche française (les gloses y sont rendues en translittération ; seuls
des artefacts de transcription vocalisés : tamhīd, fiqh, noms propres, comme
aux vagues 5-8) ; aucune harakat n'est inventée (règle 2)."""
import json, re

CHEMIN = 'content/commentaires/hadith-3es.json'

E_402 = {
    "auteur": "IA-1, tour R725",
    "resume": "Guide de lecture de la leçon 13 (أعمال يوم عرفة) : le jour le plus dense du pèlerinage se règle en trois temps — le stationnement ('Arafa tout entière lieu de station, hors le fond de la vallée d'ʿUrnā, du déclin du neuvième jusqu'à l'aube, pilier qu'aucune compensation n'acquitte), les convenances du jour (départ au plus tôt, pureté recommandée, rupture du jeûne), puis la prière récitée à voix basse derrière un sermon écourté à Namīra — le tout porté par la meilleure des invocations et clos par la petitesse du diable le jour de 'Arafa.",
    "explication": [
        "La page d'ouverture (p.90) fixe trois objectifs : reconnaître les règles du stationnement (wuqūf) à ʿArafa, reconnaître les règles de la prière et de la sermon à ʿArafāt, saisir les finalités religieuses du stationnement. La préparation reçue de la leçon 12 — les règles de la prière et du sermon à ʿArafa, le jeûne du jour de ʿArafa — se résout ici question par question. Le tamhīd pose le jour sous son meilleur titre : Ṭalḥa b. ʿUbaydallāh b. Kryz rapporte que le Messager de Dieu ﷺ a dit « la meilleure des invocations est l'invocation du jour de ʿArafa ; et la meilleure de ce que j'ai dit, moi et les prophètes avant moi : il n'est de dieu qu'Allah, seul, sans associé » (n° 1271) — la formule finale est la profession de foi, non une āya étiquetée : la leçon ne porte aucune citation coranique. La double question d'ouverture — « quelles sont les règles du stationnement à ʿArafa, et quels sont les actes de ce jour ? » — commande tout le plan : les règles d'abord, les actes ensuite.",
        "Les trois textes font chacun une lame. Le premier (n° 1157) fixe la limite : ʿAbdallāh b. ʿUmar disait que quiconque n'a pas stationné à ʿArafa avant que l'aube ne se lève, dans la nuit de al-Muzdalifa, a manqué le pèlerinage, et quiconque stationne avant cette aube l'a atteint — l'apparat consigne l'inversion des conclusions entre les deux couches du manuel (p.90 et p.93), rendue d'après p.90, le sens assuré par la doctrine du cours lui-même : l'aube de cette nuit est la limite du stationnement. Le second (n° 1100) tranche par l'acte : les gens disputaient du jeûne du Messager de Dieu ﷺ le jour de ʿArafa, Umm al-Faḍl lui envoya une coupe de lait alors qu'il était debout sur sa monture à ʿArafa — et il but. Le troisième (n° 1188) met la sunna au-dessus du pouvoir : ʿAbd al-Malik b. Marwān écrivit à al-Ḥajjāj de ne point contredire ʿAbdallāh b. ʿUmar en rien de l'affaire du pèlerinage ; au jour de ʿArafa, Ibn ʿUmar l'appelle dès le déclin du soleil à son pavillon — « le départ au plus tôt, si tu veux la sunna » ; « à cette heure ? » — « oui » — et la leçon finale, donnée par le fils Sālim : « si tu veux que nous atteignions la sunna aujourd'hui : écourte la sermon et hâte la prière » — l'approbation d'Ibn ʿUmar scelle tout : « il a dit vrai ». Les notices arment les témoins : Umm al-Faḍl, Lubāba al-Kubrā, mère des six nobles fils d'al-ʿAbbās, morte sous le califat de ʿUthmān avant son époux ; Sālim b. ʿAbdallāh, petit-fils du calife ʿUmar, le plus ressemblant aux vertueux disparus selon Mālik, mort en 106.",
        "Première partie du fiqh : le lieu. « ʿArafa tout entière est stationnement : quiconque stationne en quelque partie que ce soit vient avec la sunna d'Ibrāhīm » — « tenez-vous à l'écart du fond de la vallée d'ʿUrnā » (n° 1152), lieu entre Minā et ʿArafāt ; le meilleur est de stationner auprès des rochers près desquels le Prophète ﷺ stationna. An-Nawāwī découpe la règle : ce qui s'est notoire parmi le commun, le soin de l'ascension de la montagne de la miséricorde, « est une erreur » — la vérité est la permission du stationnement en toute partie ; l'ascension n'est pas un rite, la proximité des rochers une préférence, non une condition.",
        "Deuxième partie : le temps et les convenances. Le stationnement commence au déclin du soleil du neuvième jour et s'étend jusqu'à l'approche de l'aube du jour du sacrifice ; il faut un stationnement après le coucher du soleil, ne serait-ce qu'un bref moment, pour la prise du pilier — le stationnement est le pilier du pèlerinage qu'aucune compensation n'acquitte (le n° 1157 re-cité) ; qui a manqué le stationnement de la nuit sort de la sacralisation par une ʿumra et doit l'accomplissement différé l'année suivante. Les convenances suivent en trois points : la hâte du départ de Minā relève de la sunna — le récit n° 1188 l'atteste pas à pas, jusqu'à l'ablution différée d'al-Ḥajjāj que le Compagnon accepte d'attendre ; la pureté — recommandée pour l'acte, mais rien ne pèse sur qui la délaisse : Mālik tranche par le parallèle de la femme menstruée (n° 1155) — tout acte qu'elle accomplit de l'affaire du pèlerinage, l'homme l'accomplit en état d'impureté sans que rien ne pèse sur lui ; le meilleur est la pureté, seule la délibération est blâmable ; la rupture du jeûne — par la coupe de lait (n° 1100), la rupture fut la meilleure pour le pèlerin, car elle relève du choix du Prophète ﷺ pour sa propre personne ; la jumhūr la recommande fût-il robuste. ʿĀ'icha ne tenait pas la rupture recommandable — al-Qāsim la vit, au soir de ʿArafa, demeurer debout jusqu'à ce que la foule fût écoulée, puis appeler une boisson et rompre (n° 1101) : la sunna du Prophète ﷺ fonde la recommandation, la lecture d'ʿĀ'icha borne la rigueur.",
        "Troisième partie : la prière et la sermon. L'affaire sur quoi il n'y a pas de divergence chez Mālik : l'imam ne récite pas à voix haute dans le ẓuhr du jour de ʿArafa — le ẓuhr est à récitation discrète —, il harangue les gens à la mosquée de Namīra en les enseignant de ce qu'ils feront ensuite, et la prière du jour n'est que ẓuhr ; si elle tombe un vendredi, elle n'est que ẓuhr écourté en raison du voyage, la prière du vendredi n'étant pas célébrée — il n'y a pas de vendredi pour le voyageur (n° 1190) ; et aucun groupement de deux prières en aucun de ces jours (n° 1191) — le contrepoint exact de la leçon suivante, où Muzdalifa joint le Maghrib à l'Ishāʾ. La hâte de la prière et la brièveté de la sermon se tirent de la parole de Sālim à al-Ḥajjāj (n° 1188) ; et le cours en tire la finalité : l'islam est la religion de l'unité et de la communauté rassemblée sur la guidance — le rassemblement d'ʿArafa montre les plus hautes manifestations de l'unité et de l'égalité entre les gens.",
        "L'évaluation verrouille le tout : le jugement du jeûne du pèlerin avec preuve (n° 1100, borné par n° 1101) ; deux cas à preuve et motivation — celui qui s'en retourne avant le coucher vers al-Muzdalifa n'a pas satisfait au pilier : l'obligation du bref stationnement après le coucher est la clé de la motivation ; celui qui stationne en état d'impureté : l'acte est valide (n° 1155), mais il ne convient pas de le faire délibérément. L'exploitation boucle le tamhīd (n° 1270) : le diable n'a jamais vu de jour où il fût plus petit, plus chassé, plus abaissé, plus hors de lui de rage que le jour de ʿArafa — et cela n'est que pour ce qu'il a vu de la descente de la miséricorde et du pardon des immenses péchés — excepté le jour de Badr, où il vit Jibrīl rangeant les anges ; la consigne de diffusion au sein de la famille fait de l'élève le relais du mérite du jour. La préparation annonce la leçon 14 : le repos de la nuit à Muzdalifa, la description du jamʿ et sa cause.",
    ],
    "points": [
        "Fil de révision : trois objectifs → double question du tamhīd → trois textes (n° 1157, n° 1100, n° 1188) → fiqh en trois parties (lieu et temps, convenances en trois points, prière et sermon en deux points) → évaluation en deux items → exploitation par le hadith n° 1270.",
        "Le lieu : ʿArafa tout entière lieu de station, hors le fond de la vallée d'ʿUrnā (n° 1152) ; l'ascension de la montagne, notoire parmi le commun, « est une erreur » chez an-Nawāwī ; les rochers une préférence, non une condition.",
        "Le temps : du déclin du soleil du neuvième jusqu'à l'approche de l'aube du jour du sacrifice ; un stationnement après le coucher obligatoire, ne fût-ce bref — le pilier qu'aucune compensation n'acquitte (n° 1157) ; manqué — taḥallul par ʿumra et accomplissement différé l'année suivante.",
        "Les convenances : départ au plus tôt sunna (n° 1188 — « le départ au plus tôt, si tu veux la sunna ») ; pureté recommandée non condition — le parallèle de la femme menstruée fait autorité (n° 1155) ; rupture du jeûne recommandée au pèlerin par l'acte du Prophète ﷺ (n° 1100), la lecture d'ʿĀ'icha borne la rigueur (n° 1101).",
        "Prière et sermon : ẓuhr à récitation discrète, sermon à la mosquée de Namīra, prière écourtée si vendredi — pas de vendredi pour le voyageur (n° 1190) ; aucun groupement de deux prières ces jours-là (n° 1191) — le contrepoint de Muzdalifa ; la finalité du jour — l'unité et l'égalité.",
        "L'exploitation (n° 1270) : le diable plus petit que jamais le jour de ʿArafa — la descente de la miséricorde et le pardon des immenses péchés ; l'exception de Badr — Jibrīl rangeant les anges ; l'élève relais du mérite du jour au sein de sa famille.",
    ],
    "vocabulaire": [
        {"ar": "الوقوف", "translit": "al-wuqūf", "fr": "le stationnement à ʿArafa — pilier du ḥajj qu'aucune compensation n'acquitte ; ʿArafa tout entière lieu de station hors le fond de la vallée d'ʿUrnā (n° 1152), du déclin du neuvième à l'aube"},
        {"ar": "الرواح", "translit": "ar-rawāḥ", "fr": "le départ au plus tôt de Minā vers ʿArafa — sunna que le récit d'Ibn ʿUmar et d'al-Ḥajjāj installe pas à pas : « le départ au plus tôt, si tu veux la sunna » (n° 1188)"},
        {"ar": "تماروا", "translit": "tamārawā", "fr": "« ils divergèrent » — les gens disputaient du jeûne du Messager de Dieu ﷺ le jour de ʿArafa, jusqu'à ce que la coupe de lait tranchât (glose du n° 1100)"},
        {"ar": "سرادق", "translit": "surādiq", "fr": "ce qui entoure la tente et a une porte par laquelle on y entre — le pavillon d'al-Ḥajjāj auprès duquel Ibn ʿUmar appelle à voix haute (n° 1188)"},
        {"ar": "معصفر", "translit": "muʾaṣfara", "fr": "grand pagne teint avec le carthame (ʿuṣfur) — la tenue d'al-Ḥajjāj au matin du départ : le gouverneur cède au Compagnon, la sunna commande au pouvoir"},
        {"ar": "نمرة", "translit": "Namīra", "fr": "la mosquée où l'imam harangue les pèlerins le jour de ʿArafa et leur enseigne ce qu'ils feront ensuite — le ẓuhr y est à récitation discrète (n° 1190)"},
    ],
    "avertissement": "Ce commentaire est un guide de lecture du manuel ; en cas de divergence d'expression, le manuel et sa traduction savante font foi.",
}

E_401 = {
    "auteur": "IA-1, tour R725",
    "resume": "Guide de lecture de la leçon 12 (أحكام السعي بين الصفا والمروة) : le parcours entre Ṣafā et Marwa est un pilier du ḥajj que ni le sang ni autre chose ne compense — l'āya de Ṣafā ne délie pas, elle lève une gêne (« kallā », répond ʿĀ'icha) ; l'obligation se tire de l'assiduité prophétique et de « prenez vos rites de moi » ; la description suit les hadiths de Jābir et d'Ibn ʿUmar (départ par Ṣafā, invocations sans limite, accélération au fond du vallon), et la casuistique tranche le chevauchement, l'arrêt pour parler et l'erreur d'ordre.",
    "explication": [
        "La page d'ouverture (p.84) fixe deux objectifs : reconnaître les règles du saʿy entre Ṣafā et Marwa et sa description, suivre la guidance du Prophète ﷺ dans ces règles. Le tamhīd pose d'emblée la thèse du manuel : le saʿy est un pilier parmi les piliers du ḥajj qu'il n'est pas permis de délaisser en aucune manière, et qui n'est pas compensé par le sang — la sagesse qui s'y attache est l'obéissance à l'ordre d'Allah et l'imitation du Prophète ﷺ. La lecture « non compensé par le sang » est tranchée sur l'image et convergente avec la démonstration interne du cours ; la couche qui portait le contraire fut récusée par preuve image et par la doctrine du cours lui-même — récusation documentée, jamais devinée. La question d'ouverture ouvre sur les deux textes.",
        "Les deux textes font chacun une lame. Le premier (n° 1093) est une scène de méthode : ʿUrwa, jeune d'âge, interroge ʿĀ'icha sur l'apparent de l'āya de Ṣafā — « aṣ-Ṣafā et al-Marwa sont parmi les rites sacrés d'Allah ; quiconque accomplit le pèlerinage de la Maison ou fait la ʿumra ne commet aucun péché en faisant le parcours entre ces deux monts » (imprimé « l'āya 157 » en lecture warch — rendue du cache ḥafṣ, āya 158, écart consigné) : n'y a-t-il rien pour l'homme à ne pas faire le parcours ? Elle répond « kallā » — non ! — et rapporte la cause de révélation : les Anṣār se consacraient à Manāt, située en face de Qudayd, et trouvaient gênant de faire le parcours entre Ṣafā et Marwa que l'idolâtrie avait délégitimé à leurs yeux ; l'āya vint lever ce scrupule hérité de la Gāhiliyya. Le second (n° 1094) donne le contre-point narratif : Sawda bint ʿAbdallāh, femme lourde, étire son circuit à pied jusqu'à l'annonce du premier moment du matin plutôt que de chevaucher ; ʿUrwa, quand il voyait les gens faire le parcours montés, les en défendait avec la plus grande fermeté — leurs prétextes médicaux n'étaient que pudeur : « ceux-ci ont perdu et ils sont perdants ». La notice du transmetteur est brève — « ʿUrwa : sa notice a déjà précédé » : le manuel ne donne qu'une fois la biographie des grands transmetteurs ; les deux chaînes passent par le fils, Hishām b. ʿUrwa.",
        "Première section : le jugement du saʿy. Le faux départ d'ʿUrwa est réglé : du sens apparent de l'āya, il avait compris que le saʿy n'est pas obligatoire — lever la dispense suppose l'autorisation ; ʿĀ'icha l'a corrigé par son « kallā ». Le commentaire du manuel précise la portée : le propos littéral de l'āya reste silencieux sur l'obligation et son absence, explicite seulement sur l'absence de péché pour l'agent ; quant à l'obligation, elle se tire d'un autre indice — l'assiduité (muwāṭana) du Prophète ﷺ à l'accomplir dans son ḥajj et sa ʿumra, avec sa parole « prenez de moi vos rites de pèlerinage » (Ṣaḥīḥ Muslim). Et voilà la finesse de compréhension d'ʿĀ'icha et sa connaissance des règles par les formules : l'āya n'a jamais été accompagnée de son apparent que pour lever la gêne de qui parcourt entre les deux — si elle avait été un texte sur la chute de l'obligation, elle aurait dit « qu'il ne fasse pas le parcours ». L'analogie du ẓuhr scelle la méthode : l'homme qui se figure sa prière non licite au moment du coucher du soleil a demandé, et on lui a répondu « rien ne t'empêche de la prier » — la réponse est correcte et ne vaut pas preuve que l'obligation du ẓuhr est suspendue sur lui. La section se clôt sur le consensus : la masse des savants, parmi les Compagnons, les Tābiʿīn et ceux qui les ont suivis, a retenu que le saʿy est un pilier sans lequel le ḥajj n'est pas valide, non compensé par le sang ni autre chose.",
        "Deuxième section : la description du saʿy, en trois points. Le départ par Ṣafā — Jābir entend le Messager de Dieu ﷺ, se dirigeant vers Ṣafā, dire « il a commencé par ce par quoi Allah a commencé » (n° 1090) : Allah a commencé par Ṣafā dans l'āya, et Ṣafā est plus proche de la Maison. Les invocations à Ṣafā et à Marwa sont sunna selon la majorité : le Prophète ﷺ faisait face à la qibla, disait trois fois « Allāhu akbar » et la formule « point de dieu qu'Allah, seul, sans associé : à Lui la royauté, à Lui la louange » (n° 1091) ; il n'y a pas de limite au rappel et à l'invocation chez aucun des savants — Nāfiʾ entend ainsi Ibn ʿUmar sur Ṣafā invoquer par le verset « Appelez-Moi, Je vous répondrai » (Ghāfir 60, même numéro dans les deux lectures) : « je Te demande, comme Tu m'as guidé à l'islam, de ne pas me l'arracher jusqu'à ce que Tu me fasses mourir musulman » (n° 1092). L'accélération au fond du vallon — le Prophète ﷺ marchait jusqu'à ce que ses pieds eussent pris pente au fond du vallon, puis courût (n° 1098) ; la glose du manuel : « prendre pente » du pied, c'est son enfoncement en pente ; « le fond du vallon » (aṣ-ṣabb), le lieu en pente.",
        "Troisième et quatrième sections : les exceptions et l'erreur d'ordre. La marche à pied est obligatoire pour celui qui en est capable — par le faire du Prophète ﷺ, par Sawda qui n'achevait son circuit qu'entre al-ʿichāʾ et l'adhān du matin sans chevaucher, et par la fermeté d'ʿUrwa contre les cavaliers ; l'arrêt pour parler pendant le saʿy — interrogé, Mālik dit « je n'aime pas cela pour lui » (n° 1096) : c'est blâmé, parce que ce qui est requis alors, c'est le rappel et l'invocation. Celui qui, par ignorance, a commencé le saʿy avant le ṭawāf est comme celui qui n'a pas fait le saʿy — faire précéder le ṭawāf est une condition de la validité du saʿy ; la décision de Mālik proportionne la sanction : qu'il revienne, tourne autour de la Maison, puis fasse le saʿy ; s'il a ignoré jusqu'à sortir de La Mecque et s'en éloigner, qu'il revienne ; si c'était une femme, qu'elle complète ce qui lui reste de cette ʿumra dans l'ordre corrigé, puis il lui doit une seconde ʿumra et l'offrande (n° 1099) — le saʿy antérieur ne se rachète pas par un symbole, il se refait.",
        "L'évaluation verrouille le tout : deux cas à preuve et motivation — la femme au pas lent qui a chevauché pendant son saʿy (la règle « la marche obligatoire pour le capable » et l'exception de l'incapacité) ; le pèlerin qui a fait précéder le saʿy sur le ṭawāf (la décision n° 1099) ; et le jugement des invocations (sunna selon la majorité, sans limite fixée au rappel et à l'invocation). L'exploitation (istichhād) couronne le chapitre par l'athar encadré de Mālik (n° 1097) : quiconque a oublié une partie de son ṭawāf, ou a douté, et n'y a songé qu'en plein saʿy — qu'il coupe son saʿy, complète son ṭawāf selon ce dont il est certain, accomplit les deux rakʿa du ṭawāf, puis recommence son saʿy ; l'oubli ne corrompt pas ce qui est certain, il demande la reprise de ce qui manque. La préparation annonce la leçon 13 : les règles de la prière et du sermon à ʿArafa, et le jeûne du jour de ʿArafa pour le pèlerin.",
    ],
    "points": [
        "Fil de révision : deux objectifs → tamhīd (pilier non compensable par le sang) → deux textes (n° 1093, n° 1094) → fiqh en quatre sections (jugement, description en trois points, chevauchement et arrêt, erreur d'ordre) → évaluation en deux cas et le jugement des invocations → exploitation par l'athar n° 1097.",
        "Le jugement : l'āya de Ṣafā lève une gêne, elle ne délie pas — « kallā » (ʿĀ'icha, n° 1093, cause de révélation : les Anṣār et Manāt) ; l'obligation se tire de l'assiduité prophétique et de « prenez de moi vos rites » ; consensus des jamāhīr — pilier, ḥajj invalide sans lui, ni sang ni autre chose ne le compense.",
        "La méthode : « rien ne t'empêche de la prier » ne suspend pas l'obligation (analogie du ẓuhr au coucher du soleil) — distinguer la levée de la gêne et la chute du jugement, la finesse de compréhension d'ʿĀ'icha dans la connaissance des règles par les formules.",
        "La description : départ par Ṣafā — « il a commencé par ce par quoi Allah a commencé » (n° 1090) ; invocations sunna sans limite fixée — takbīr triple face à la qibla (n° 1091), l'invocation d'Ibn ʿUmar par Ghāfir 60 (n° 1092) ; accélération au fond du vallon (n° 1098).",
        "La casuistique : marche obligatoire pour le capable, le chevauchement exception de l'incapacité (n° 1094 — Sawda, la fermeté d'ʿUrwa) ; l'arrêt pour parler blâmé — le temps du saʿy appartient au dhikr (n° 1096) ; le saʿy avant le ṭawāf refait dans l'ordre — pour la femme, seconde ʿumra et offrande (n° 1099).",
        "L'oubli et le doute (n° 1097) : couper le saʿy, compléter le ṭawāf selon le certain, deux rakʿa, recommencer le saʿy — la hiérarchie pilier, condition, dispense gouverne tout le chapitre.",
    ],
    "vocabulaire": [
        {"ar": "السعي", "translit": "as-saʿy", "fr": "le parcours entre Ṣafā et Marwa — pilier du ḥajj que ni le sang ni autre chose ne compense (tamhīd ; consensus des jamāhīr) ; sept allers-retours commençant par Ṣafā"},
        {"ar": "الركن", "translit": "ar-rukn", "fr": "le pilier — sans lequel l'acte d'adoration n'est pas valide ; le saʿy posé pilier du ḥajj, comme le stationnement dʿArafa de la leçon suivante — la différence tenant à la compensation"},
        {"ar": "مناة", "translit": "Manāt", "fr": "une idole de la Gāhiliyya — les Anṣār s'y consacraient et trouvaient gênant le parcours Ṣafā-Marwa ; la cause de révélation de l'āya de Ṣafā (n° 1093)"},
        {"ar": "قديد", "translit": "Qudayd", "fr": "localité proche entre La Mecque et Médine, abondante en eau — Manāt était en face (ḥadw) de Qudayd, d'où le scrupule des Anṣār"},
        {"ar": "ثقيلة", "translit": "thaqīla", "fr": "« lourde » — l'antonyme de légère, allusion à la corpulence ou à la lenteur de la marche de Sawda, qui étire son circuit jusqu'à l'annonce du matin (n° 1094)"},
        {"ar": "الصب", "translit": "aṣ-ṣabb", "fr": "le fond du vallon, le lieu en pente entre les deux monts — où la sunna est d'accélérer (n° 1098) ; « prendre pente » du pied : son enfoncement en pente"},
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
for docid, entree in (('pdf-mut23h2x-402', E_402), ('pdf-mut23h2x-401', E_401)):
    if docid in com:
        print(f'!! {docid} déjà présent — rien de fait')
        raise SystemExit(1)
    com[docid] = norme_entree(entree)

with open(CHEMIN, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
    f.write('\n')

# Validation : relecture + volume + ponctuation FR + arabes hors champ ar
data2 = json.load(open(CHEMIN, encoding='utf-8'))
print('entrées au total :', len(data2['commentaires']))
motif_ar = re.compile(r'[\u0600-\u06FF\u0750-\u077F\u08A0-\u08FF\uFDFA]')
mauvais = 0
for docid in ('pdf-mut23h2x-402', 'pdf-mut23h2x-401'):
    e = data2['commentaires'][docid]
    mots = sum(len(x.split()) for x in [e['resume']] + e['explication'] + e['points'])
    print(f'{docid} : {mots} mots (resume+explication+points), vocab {len(e["vocabulaire"])}')
    textes = [e['resume'], e['avertissement']] + e['explication'] + e['points'] + [v['fr'] for v in e['vocabulaire']] + [v['translit'] for v in e['vocabulaire']]
    for t in textes:
        # l'arabe entre parenthèses (titres du manuel) est échappé au build
        # en balises RTL (LISEZ-MOI.md §3.3) — hors parenthèses : 0 arabe
        hors_parenth = re.sub(r'\([^)]*[\u0600-\u06FF][^)]*\)', '()', t).replace('ﷺ', '')
        if "'" in t or re.search(r' [;:!?»]', t) or re.search(r'« ', t):
            mauvais += 1
            print('   ponctuation à revoir dans :', t[:60])
        if motif_ar.search(hors_parenth):
            mauvais += 1
            print('   caractère arabe hors parenthèses :', t[:60])
print('contrôle ponctuation/arabe FR :', 'PASS' if mauvais == 0 else f'ÉCHEC ({mauvais})')

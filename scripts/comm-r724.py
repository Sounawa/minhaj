#!/usr/bin/env python3
"""R724 — ajoute les commentaires pédagogiques de la leçon 15 (pdf-mut23h2x-404,
les rites des journées à Minā (1)) et de la leçon 14 (pdf-mut23h2x-403, les
règles du séjour à Muzdalifa) à content/commentaires/hadith-3es.json.
Vague 8 : remontée du manuel (le SUIVANT de R723).
Même protocole que comm-r723.py : normalisation de la ponctuation FR (U+202F
avant ; : ! ? » et après «, apostrophe courbée) sur les entrées nouvelles
seulement — opération idempotente. Rédaction d'après la lecture complète des
deux leçons (htmlFr intégral, extraction non lossy en blocs complets, scripts/
extrait-r724.py). Les numéros du Muwaṭṭaʾ et les āyās sont cités tels qu'ils
figurent dans les leçons (règle 2 de LISEZ-MOI.md : aucune invention). Les
formes arabes du vocabulaire sont posées au squelette standard SANS harakat —
ces deux leçons ne portent pas les formes vocalisées du lexique (seuls des
artefacts de transcription vocalisés : tamhīd, fiqh, noms propres, comme aux
vagues 5-7) ; aucune harakat n'est inventée (règle 2)."""
import json, re

CHEMIN = 'content/commentaires/hadith-3es.json'

E_404 = {
    "auteur": "IA-1, tour R724",
    "resume": "Guide de lecture de la leçon 15 (أعمال أيام منى (1)) : après la nuit de Muzdalifa, les journées de Minā se règlent en trois actes légaux — jeûne interdit par consensus, takbīr prescrit aux suites des prières, prière réduite même pour le Mecquois — le fil des « jours comptés » de l’āya d’ouverture les tenant ensemble, jusqu’à la réduction posée rite cultuel et sunna non abrogée.",
    "explication": [
        "La page d’ouverture (p.104) fixe trois objectifs : reconnaître les actes des jours de Minā, s’attacher à la sunna dans le jeûne, la prière et le takbīr ces jours-là, saisir les desseins du lieu sacré (machʿar) de Minā. La préparation reçue de la leçon 14 — le jeûne des jours de Minā, le takbīr de ces jours, le raccourcissement de la prière — se résout ici question par question. Le tamhīd pose le cadre : le ḥajj est une adoration à piliers et obligations, parmi lesquelles le séjour (mabīt) à Minā après le retour de ʿArafa — deux nuits pour le pressé, trois pour le non-pressé — et l’ordre divin d’invoquer Allah ces jours-là : « wa-dhkurū llāha fī ayyāmin maʿdūdāt — invoquez Allah pendant des jours comptés » (imprimé « l’āya 201 » — al-Baqara 203 du cache ḥafṣ, la forme condensée sans « fī », écart consigné). Trois questions en découlent, qui déroulent exactement les trois sections de la recherche légale.",
        "Les trois textes font chacun une lame. Le premier (n° 1105) réunit en une scène domestique l’interdit et l’ordre : ʿAbdallāh b. ʿAmr b. al-ʿĀṣ entre chez son père ʿAmr et le trouve en train de manger ; « je suis en état de jeûne », dit le fils ; « voici les jours dont le Messager de Dieu ﷺ nous a interdit le jeûne et dont il nous a ordonné la rupture », répond le père — et Mālik ajoute : « ce sont les jours de tashrīq ». Le second (n° 1197) échelonne quatre générations : le Prophète ﷺ, Abū Bakr et ʿUmar prièrent à Minā deux rakʿa, ʿUthmān deux rakʿa pendant une moitié de son émirat puis complétait ensuite — la réduction comme conduite constante du début de l’islam, le changement comme l’événement même que la troisième section jugera. Le troisième (n° 1204) dédouble le concerné du takbīr : hommes et femmes, groupe ou seul, à Minā ou dans les horizons — « tout cela obligatoire » —, l’extension tenant à l’émir du pèlerinage, et le non-pèlerin qui n’y prend part que dans le takbīr des jours de tashrīq ; la remarque finale de Mālik identifie les « jours comptés » de l’āya aux jours de tashrīq, nouant le texte à l’ouverture de la leçon.",
        "La notice du transmetteur arme le premier texte : ʿAbdallāh b. ʿAmr b. al-ʿĀṣ, Quraychite du clan de Sahm, kunya Abū Muḥammad, l’un des « ʿAbdallāh » dont le nom même portait la servitude, Compagnon fils de Compagnon, converti avant l’Hégire, mort à Chām en 65 — sa longue transmission du Prophète ﷺ, d’ʿUmar, d’Abū ad-Dardāʾ et de Muʿādh explique la large diffusion de ses récits parmi les Tābiʿīn. Les deux gloses se répondent : Minā, vallée entourée de montagnes à l’est de Makka sur le chemin vers ʿArafa — la géographie que la leçon précédente a décrite — et ayyām Minā, les jours du lancer des jimār, deux pour le pressé et trois pour le non-pressé — la distinction mutaʿajjil / non-pressé posée d’emblée, qui traversera tout le cours.",
        "Première section : le jeûne. Il n’est pas licite de jeûner les jours de Minā en surérogatoire, par consensus : Salamān b. Yasār rapporte que le Prophète ﷺ a interdit de jeûner ces jours (n° 1102) ; Ibn Shihāb rapporte l’envoi de ʿAbdallāh b. Ḥudhāfa faire proclamer « ce ne sont que des jours de manger, de boire et d’invoquer Allah » (n° 1103). La sagesse de l’interdit suit : après le manger et le boire vient l’invocation d’Allah, de peur que le serviteur ne se laisse absorber par les plaisirs de son âme et n’oublie les droits d’Allah ; et les prédécesseurs ont blâmé qui rend visite à Allah tout en étant dans Son hospitalité ces jours-là, et jeûne sans la permission de celui qui l’a reçu. L’exception est au même mouvement : le jeûne du mutamattiʿ qui n’a pas trouvé d’offrande est licite — le réputé chez Mālik — par la parole du Très-Haut « fa-ṣiyāmu thalāthati ayyāmin fī l-ḥajji wa-sabʿatin idhā rajaʾtum » (imprimé « l’āya 195 » — al-Baqara 196 du cache ḥafṣ, écart d’une unité conforme à la doctrine).",
        "Deuxième section : le takbīr, en trois rubriques. Le temps — Mālik spécifie le takbīr des jours de tashrīq aux suites des prières et l’étend à chaque type de prière : l’obligatoire et la surérogatoire, celle faite à son temps et celle rattrapée — « l’ordre chez nous est que le takbīr pendant les jours de tashrīq suit les prières » (n° 1203) ; Ibn al-Ḥadīb déroule les trois stations d’ʿUmar — au début de la journée, à l’élévation du soleil, au déclin (al-Muntaqā l-Bājī, 4/81) — et le récit de Yaḥyā b. Saʿīd fait de la répétition la pédagogie même du rite : ʿUmar sortit trois fois, chaque fois takbīr et les gens avec lui, « jusqu’à ce que le takbīr fût fait continu et l’intention se fût manifestée, de sorte qu’on reconnût qu’ʿUmar était sorti pour lancer les cailloux » (n° 1202). L’initiation et la fin — derrière le ẓuhr du jour du sacrifice, jusqu’au ṣubḥ du dernier jour de tashrīq puis interruption (n° 1203) — s’appuient sur l’argument par la pratique, car rien n’est rapporté en hadith. La description et les concernés — « Allāhu akbar » trois fois (al-Muntaqā, 4/82), l’invitation de Salmān à multiplier l’exaltation d’Allah, l’ajout d’al-Chāfiʿī sans tort pour qui ajoute ou retranche, le takbīr à voix haute selon Mālik — tandis que le n° 1204 imprimé « obligatoire » est rendu par la doctrine recommandé (mandūb) pour les hommes et les femmes, l’isolé et le groupe, à Minā ou aux horizons.",
        "Troisième section : la réduction à Minā — recommandée au pèlerin même s’il est Mecquois tant qu’il s’y trouve : les gens de Makka firent le pèlerinage avec le Prophète ﷺ et réduisirent avec lui à Minā sans qu’il leur dise « complétez » — la réduction est un rite cultuel (qaṣr nusk wa-ʿibāda), nulle distance de réduction entre Makka et Minā. Le n° 1198 fait d’ʿUmar la preuve vivante : venu à Makka il pria avec eux deux rakʿa en disant « complétez votre prière, nous sommes un peuple en voyage », puis pria deux rakʿa sans rien dire aux gens — les califes l’imitèrent à Minā selon la sunna de la réduction, « et ce jugement n’a pas été abrogé ». L’évaluation verrouille les trois sections — dont le cas motivé de l’homme de Minā dont l’argument reproduit mot pour mot la démonstration du cours. L’exploitation fait travailler le texte d’interrogation n° 1200 : gens de Makka à ʿArafa et à Minā tant qu’ils y séjournent — deux rakʿa chacune ; l’émir du pèlerinage s’il est Mecquois réduit aussi ; et qui demeure en résident (sākin muqīm) complète — le séjour au lieu sacré ne fait pas du pèlerin un résident au sens légal. La préparation annonce la leçon 16 : le séjour hors de Minā les jours du lancer et la description du lancer.",
    ],
    "points": [
        "Fil de révision : trois objectifs → trois questions du tamhīd → trois textes → trois sections du fiqh (jeûne, takbīr, réduction) → évaluation en trois items → exploitation par le texte d’interrogation n° 1200.",
        "Le jeûne des jours de Minā : non licite en surérogatoire par consensus (n° 1102, n° 1103 — « des jours de manger, de boire et d’invoquer Allah ») ; l’hospitalité d’Allah exige la rupture, l’invité ne jeûne sans la permission de son hôte ; le jeûne du mutamattiʿ sans offrande demeure licite — le réputé chez Mālik (al-Baqara 196 du cache, imprimé « 195 »).",
        "Le takbīr : aux suites des prières — l’obligatoire et la rattrapée incluses (n° 1203) —, du ẓuhr du jour du sacrifice au ṣubḥ du dernier jour de tashrīq, « Allāhu akbar » trois fois, à voix haute selon Mālik ; concernés — hommes et femmes, isolé et groupe, Minā et horizons (n° 1204) — recommandé dans la doctrine là où l’imprimé dit « obligatoire ».",
        "La pédagogie d’ʿUmar (n° 1202, Ibn al-Ḥadīb 4/81) : trois sorties par jour — élévation du soleil, après le lever, au déclin — jusqu’à rendre le takbīr continu et l’intention manifestée : la répétition institue la communauté dans le rite.",
        "La réduction à Minā : rite cultuel et sunna non abrogée — même le Mecquois la réduit tant qu’il y séjourne, et ʿUmar à Makka réduit en renvoyant les Mecquois à leur prière complète (n° 1198) ; nulle distance de réduction entre Makka et Minā.",
        "Le texte d’exploitation (n° 1200) : deux rakʿa à ʿArafa et à Minā tant qu’on y séjourne — même pour l’émir Mecquois ; le résident véritable complète : la résidence au sens légal, non la géographie, décide de la prière.",
    ],
    "vocabulaire": [
        {"ar": "التشريق", "translit": "at-tachrīq", "fr": "les jours de tashrīq — ceux du lancer des jimār à Minā : « des jours de manger, de boire et d’invoquer Allah » (n° 1103) ; Mālik les identifie aux « jours comptés » de l’āya d’ouverture (n° 1204)"},
        {"ar": "التكبير", "translit": "at-takbīr", "fr": "l’exaltation « Allah est le plus grand » des jours de tashrīq — aux suites des prières, à voix haute, du ẓuhr du jour du sacrifice au ṣubḥ du dernier jour de tashrīq (n° 1203)"},
        {"ar": "القصر", "translit": "al-qaṣr", "fr": "la réduction de la prière de quatre rakʿa à deux — un rite cultuel (qaṣr nusk wa-ʿibāda) : à Minā même pour le Mecquois, nulle distance de réduction entre Makka et Minā ; sunna non abrogée"},
        {"ar": "المتعجل", "translit": "al-mutaʿajjil", "fr": "le pressé — deux nuits à Minā au lieu de trois : la distinction posée par la glose des jours de Minā et par le tamhīd, traversant jeûne, takbīr et lancer"},
        {"ar": "المتمنتع", "translit": "al-mutamattiʿ", "fr": "celui qui joint la ʿumra au ḥajj en jouissance — son jeûne de trois jours pendant le pèlerinage est licite quand il n’a pas trouvé d’offrande (le réputé chez Mālik)"},
        {"ar": "المشعر", "translit": "al-machʿar", "fr": "le lieu sacré — Minā comme mashʿar dont les desseins sont à saisir (troisième objectif) : des jours d’invocation d’Allah, non d’ascèse"},
    ],
    "avertissement": "Ce commentaire est un guide de lecture du manuel ; en cas de divergence d’expression, le manuel et sa traduction savante font foi.",
}

E_403 = {
    "auteur": "IA-1, tour R724",
    "resume": "Guide de lecture de la leçon 14 (أحكام مزدلفة) : la nuit du dixième se règle du départ d’ʿArafa au lancer de l’aube — cheminer en sérénité et presser dans les ouvertures, joindre le Maghrib à l’Ishāʾ à Muzdalifa comme une unique prière, descendre au mesure du déchargement des bagages, veiller au Mashʿar al-Ḥarām jusqu’à l’isfār — et la dispense des femmes, des enfants et des porteurs d’excuses fait de la nuit un rite à géométrie variable.",
    "explication": [
        "La page d’ouverture (p.97) fixe deux objectifs : reconnaître les règles de la nuit du dixième de Dhū l-Ḥijja, reconnaître le jugement de l’invocation et de l’évocation la nuit à Muzdalifa et lors du stationnement au Mashʿar al-Ḥarām. La préparation reçue de la leçon 13 — le jugement du bivouac et du stationnement, la description du jamʿ et sa cause — se résout ici article par article. Le tamhīd fait du nom même le dessein du rite : Muzdalifa, emplacement entre ʿArafāt et Minā, se nomme du rapprochement d’Allah (yutaqarrab), du rassemblement au plus près de Minā après l’ifāḍa, du cheminement dans une portion (zulfah) de la nuit — la glose du nom : « elle avance et se rapproche ». Trois questions en découlent : la manière du cheminement vers Muzdalifa, les règles du bivouac et de la prière, le jugement du stationnement au Mashʿar al-Ḥarām.",
        "Les deux textes font chacun une lame. Le premier (n° 1165) règle le régime du mouvement : interrogé par ʿUrwa alors qu’il était assis avec lui, Usāma b. Zayd rapporte que le Prophète ﷺ cheminait à l’al-ʿanaq — l’allure entre le lent et le rapide — et pressait l’an-nass, plus rapide, quand il trouvait une ouverture dans la foule. Le second (n° 1193) déroule la chronologie complète du départ : au col, descente, urination et ablutions sans les compléter ; « la prière, ô Messager d’Allah ! » — « la prière est devant toi » ; parvenu à Muzdalifa, ablutions complétées, iqāmah, Maghrib ; chacun plie les genoux de sa monture à son campement ; iqāmah de l’Ishāʾ, prière — sans rien prier entre les deux. La notice arme le témoin commun aux deux textes : Usāma b. Zayd, l’aimé du Messager d’Allah ﷺ et le fils de son aimé, né du temps de la Prédication, abondant en piété, mort à Médine en 59 — le cheminement et le jamʿ rapportés depuis l’intimité même du Prophète ﷺ.",
        "Première section : le départ vers Muzdalifa et le stationnement. Après le coucher du soleil au jour de ʿArafāt, l’imam et les gens repartent en sérénité (sakīnah) et recueillement (waqār) ; si l’espace s’ouvre, ils accélèrent par hâte pour la prière — le Maghrib ne se prie qu’avec l’Ishāʾ en jointure. Le n° 1165 prouve l’ajournement du Maghrib après le crépuscule ; la manière équilibre l’utilité du recueillement au milieu de la foule et la prévention de l’attroupement ; et ʿUmar pressait sa monture à travers Baṭn Muḥaṣṣir (n° 1166) — le vallon proche de Muzdalifa que les Mecquois appellent le Vallon du Feu, où la sunna veut qu’on ne s’attarde pas. Le stationnement suit : Muzdalifa tout entière est lieu de stationnement, sauf Baṭn Muḥaṣṣir — « al-Muzdalifatu kulluhā mawqifun, wa-rtafiʿū ʿan Baṭni Muḥaṣṣir » (n° 1152) ; le hadith de Jābir (« j’ai stationné ici, et Muzdalifa tout entière est stationnement », chez Abū Dāwūd) ; et le Mukhtaṣar de Khalīl (p. 79) rattache la station du Mashʿar à son horizon temporel propre : « au Mashʿar al-Ḥarām, on magnifie et on invoque jusqu’à l’isfār ».",
        "Deuxième section : les règles de Muzdalifa, en quatre lames. La prière jointe — la sunna après le départ d’ʿArafāt est d’ajourner le Maghrib et de le joindre à l’Ishāʾ à Muzdalifa, un jamʿ sur lequel il y a accord : le Prophète ﷺ « a prié le Maghrib et l’Ishāʾ à Muzdalifa, ensemble » (n° 1192) et Ibn ʿUmar priait les deux ensemble (n° 1195) ; qui prie le Maghrib avant l’entrée du temps de l’Ishāʾ — Ibn al-Qāsim transmet qu’il doit la répétition, le jumhūr tient la prière valide. La description du jamʿ et sa cause — descente de al-Qaṣwāʾ, ablutions à l’eau de Zamzam, iqāmah et Maghrib avant le déchargement des bagages ; chacun plie les genoux de sa monture par ménagement pour les bêtes ; Ishāʾ sans prière surérogatoire entre les deux — parce que le jamʿ entre elles les fait comme l’unique prière, dont l’accomplissement complet s’impose ; et ce jamʿ, chez les Mālikites, est une pure dévotion dont le sens ne se saisit pas rationnellement.",
        "L’adhān et l’iqāmah — l’apparent du hadith d’Usāma est l’iqāmah seule ; chez al-Bukhārī et an-Nasāʾī, Ibn Masʿūd rapporte l’adhān puis l’iqāmah pour chacune des deux prières — « j’ai vu le Prophète ﷺ le faire » — et la licéité des deux est ce que Mālik a retenu et al-Bukhārī a choisi. La descente et la dispense — la descente à Muzdalifa est obligatoire au mesure du déchargement des bagages ; qui ne descend pas encourt le sang selon l’avis le plus répandu ; le bivouac est de sunna, la nuit vivifiée par l’adoration, le Ṣubḥ à son premier temps ; station au Mashʿar al-Ḥarām tourné vers la qibla, le Mashʿar à sa gauche (tel que imprimé, divergence avec la sunna communément rapportée de la droite consignée), takbīr et invocation jusqu’à l’isfār ; sept cailloux ramassés depuis Muzdalifa pour la Jamrah de al-ʿAqabah, puis départ vers Minā. La dispense aux femmes, aux enfants et aux porteurs d’excuses — par crainte de la gêne et de l’attroupement — s’appuie sur trois athars convergents : Ibn ʿUmar envoyait sa famille et ses enfants de Muzdalifa à Minā jusqu’à prier le Ṣubḥ à Minā et lapider, « le plus matinal des gens » (n° 1160) ; la cliente d’Asmāʾ bt. Abī Bakr — arrivées aux ténèbres de l’aube, « nous faisions ainsi avec celui qui est meilleur que toi » (n° 1161) ; Ṭalḥa b. ʿUbaydallāh envoyait ses femmes et ses enfants de Muzdalifa à Minā (n° 1162).",
        "L’évaluation verrouille la leçon : le cheminement, la description du jamʿ, puis deux cas à preuve — le pèlerin certain d’arriver après l’Ishāʾ qui prie le Maghrib en route relève du différend d’Ibn al-Qāsim contre le jumhūr ; le pèlerin qui rejoint Minā sans descendre à Muzdalifa encourt le sang, la descente étant obligatoire au mesure du déchargement. L’exploitation fait travailler le tafsīr de Mālik à rebours (n° 1154) : le rafth — les rapports charnels aux femmes (al-Baqara 187 du cache, imprimé « 186 ») ; le fusūq — l’immolation pour les anṣāb, les pierres-idoles (al-Anʿām 145 du cache, imprimé « 146 », écart au sens inverse consigné) ; le jidāl — la dispute des Ḥums de Quraych campés à Quzayḥ contre les Arabes stationnant à ʿArafāt, chacun disant « nous sommes dans le vrai », tranchée par le verset qui assigne à chaque communauté son rite (al-Ḥajj 67 du cache, imprimé « 65 ») — la leçon de Muzdalifa, lieu où la communauté réunit les deux stations, est la réponse vivante du Prophète ﷺ à cette dispute. La préparation annonce la leçon 15 : le jeûne des jours de Minā, le takbīr de ces jours, le raccourcissement de la prière à Minā.",
    ],
    "points": [
        "Fil de révision : deux objectifs → trois questions du tamhīd → deux textes → deux sections du fiqh (départ et stationnement, règles du lieu) → évaluation en trois items → tafsīr d’exploitation n° 1154.",
        "Le régime du cheminement : l’al-ʿanaq de base, l’an-nass dans les ouvertures (n° 1165), la presse ciblée d’ʿUmar à travers Baṭn Muḥaṣṣir (n° 1166) — le tout subordonné à la prière jointe, qui n’est pas priée avant le lieu (« la prière est devant toi », n° 1193).",
        "Le stationnement : Muzdalifa tout entière lieu de stationnement sauf Baṭn Muḥaṣṣir (n° 1152) ; le jamʿ du Maghrib et de l’Ishāʾ sur lequel il y a accord (n° 1192, n° 1195) — comme une unique prière, sans surérogatoire entre les deux ; pure dévotion chez les Mālikites.",
        "La prière en route : Ibn al-Qāsim — la répétition ; le jumhūr — la validité ; l’adhān et l’iqāmah pour chacune licites — Mālik les retient, al-Bukhārī les choisit (Ibn Masʿūd).",
        "La descente obligatoire au mesure du déchargement — le sang selon l’avis le plus répandu pour qui ne descend pas ; le bivouac de sunna, la nuit vivifiée, le Ṣubḥ à son premier temps, la station du Mashʿar jusqu’à l’isfār, les sept cailloux de l’aube.",
        "La dispense des femmes, des enfants et des porteurs d’excuses (n° 1160, 1161, 1162) : les valides y veillent, les faibles partent de nuit — la force des pèlerins, non le seul texte, module l’exécution du rite.",
    ],
    "vocabulaire": [
        {"ar": "مزدلفة", "translit": "al-Muzdalifa", "fr": "l’emplacement entre ʿArafāt et Minā — nommé du rapprochement d’Allah, du rassemblement au plus près de Minā après l’ifāḍa, du cheminement en portion de nuit ; « elle avance et se rapproche »"},
        {"ar": "الجمع", "translit": "al-jamʿ", "fr": "la jointure du Maghrib et de l’Ishāʾ à Muzdalifa — un jamʿ sur lequel il y a accord : le tout comme l’unique prière, sans surérogatoire entre les deux ; pure dévotion chez les Mālikites"},
        {"ar": "المشعر الحرام", "translit": "al-Machʿar al-Ḥarām", "fr": "le lieu sacré du stationnement — takbīr et invocation jusqu’à l’isfār, la qibla en face (Mukhtaṣar de Khalīl, p. 79) ; sept cailloux pour la Jamrah de al-ʿAqabah ensuite"},
        {"ar": "المبيت", "translit": "al-mabīt", "fr": "le bivouac à Muzdalifa — de sunna, nuit vivifiée par l’adoration, Ṣubḥ à son premier temps ; dispensé aux femmes, aux enfants et aux porteurs d’excuses"},
        {"ar": "النزول", "translit": "an-nuzūl", "fr": "la descente à Muzdalifa — obligatoire au mesure du déchargement des bagages ; qui ne descend pas encourt le sang selon l’avis le plus répandu"},
        {"ar": "الجدال", "translit": "al-jidāl", "fr": "la dispute dans le pèlerinage — celle des Ḥums de Quraych campés à Quzayḥ contre les Arabes d’ʿArafāt, tranchée par le verset du rite de chaque communauté (n° 1154) : point de jidāl fī l-ḥajj"},
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
for docid, entree in (('pdf-mut23h2x-404', E_404), ('pdf-mut23h2x-403', E_403)):
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
for docid in ('pdf-mut23h2x-404', 'pdf-mut23h2x-403'):
    e = data2['commentaires'][docid]
    mots = sum(len(x.split()) for x in [e['resume']] + e['explication'] + e['points'])
    print(f'{docid} : {mots} mots (resume+explication+points), vocab {len(e["vocabulaire"])}')
    textes = [e['resume'], e['avertissement']] + e['explication'] + e['points'] + [v['fr'] for v in e['vocabulaire']] + [v['translit'] for v in e['vocabulaire']]
    for t in textes:
        # l’arabe entre parenthèses (titres du manuel) est échappé au build
        # en balises RTL (LISEZ-MOI.md §3.3) — hors parenthèses : 0 arabe
        hors_parenth = re.sub(r'\([^)]*[\u0600-\u06FF][^)]*\)', '()', t).replace('ﷺ', '')
        if "'" in t or re.search(r' [;:!?»]', t) or re.search(r'« ', t):
            mauvais += 1
            print('   ponctuation à revoir dans :', t[:60])
        if motif_ar.search(hors_parenth):
            mauvais += 1
            print('   caractère arabe hors parenthèses :', t[:60])
print('contrôle ponctuation/arabe FR :', 'PASS' if mauvais == 0 else f'ÉCHEC ({mauvais})')

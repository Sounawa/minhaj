#!/usr/bin/env python3
"""R723 — ajoute les commentaires pédagogiques de la leçon 17 (pdf-mut23h2x-406,
les règles de la bête d'offrande (hady) (1)) et de la leçon 16 (pdf-mut23h2x-405,
les rites des journées à Minā (2)) à content/commentaires/hadith-3es.json.
Vague 7 : remontée du manuel (le SUIVANT de R722).
Même protocole que comm-r722.py : normalisation de la ponctuation FR (U+202F
avant ; : ! ? » et après «, apostrophe courbée) sur les entrées nouvelles
seulement — opération idempotente. Rédaction d'après la lecture complète des
deux leçons (htmlFr intégral, extraction non lossy en blocs complets). Les
numéros du Muwaṭṭaʾ et les āyās sont cités tels qu'ils figurent dans les
leçons (règle 2 de LISEZ-MOI.md : aucune invention). Les formes arabes du
vocabulaire sont posées au squelette standard SANS harakat — ces deux leçons
ne portent pas les formes vocalisées du lexique (seuls des artefacts de
transcription vocalisés : tamhīd, fiqh, noms propres, comme aux vagues 5-6) ;
aucune harakat n'est inventée (règle 2)."""
import json, re

CHEMIN = 'content/commentaires/hadith-3es.json'

E_406 = {
    "auteur": "IA-1, tour R723",
    "resume": "Guide de lecture de la leçon 17 (أحكام الهدي (1)) : la bête d’offrande — rite du ḥajj et chaʾāʾir d’entre ses rites — se règle en trois lames : ce qui est licite (les espèces et leurs âges, l’aisé), la conduite (glorification, parure, marquage), le profit (montée, lait, chair) ; tout se tient dans les desseins : glorifier les rites d’Allah, honorer les hôtes du Miséricordieux, alléger les pauvres de La Mecque.",
    "explication": [
        "La page d’ouverture (p.116) porte l’invite reçue de la leçon 16 — trois termes techniques du hady à expliquer (le premier porte une coquille d’impression jamais résolue), le garlanding, le marquage, le sens de l’« istaysar » — et la page d’objectifs (p.117) en fixe deux : reconnaître les règles du hady dans le ḥajj, saisir ses desseins. Le tamhīd énonce le cadre : Allah a fait du hady vers le Ḥaram un rite du ḥajj et une de ses chaʾāʾir — Āl ʿImrān 97 du cache ḥafṣ, bloc calligraphique composite qui lui joint le matériel du Ḥajj — puis quatre questions : la sunna mūjazza, la conduite, le profit, les desseins. Le fil conducteur est posé d’emblée : la glorification — la conduite et le profit de la bête ne se règlent que par ce dessein.",
        "Les quatre textes font chacun une lame. Le premier (n° 1111) étend la piété du sacrifice à la descendance : la bête immolée ne laisse pas derrière elle un petit qui meurt sans immolation — téter jusqu’à être immolé avec elle, ou porté sur le dos de la mère. Le second (n° 1141) fixe une règle d’orientation : de la bête immolée, ce qui fait face au sacrificateur est le mouton — la chaîne familiale ʿAlī → Muḥammad al-Bāqir → Jaʿfar aṣ-Ṣādiq relie la parole à la maison du Prophète ﷺ. Le troisième (n° 1113), colonne vertébrale du cours : la conduite complète de l’offrande de Médine — sandales au cou et marquage à Dhī l-Ḥulayfa, garlanding avant marquage, un même lieu vers la qibla, flanc gauche ; immobilisée à ʿArafa avec les gens ; immolée à Minā le matin du jour du sacrifice avant toute coupe, de sa propre main, debout face à la qibla — puis il mangeait et il nourrissait. Le quatrième (n° 1106) rapporte le chameau qui fut à Abū Jahl b. Hishām, offert dans un ḥajj ou une ʿumra : le hady se prend de tout bien devenu licite — même du bien de l’un des pires ennemis de l’islam.",
        "Les notices servent leurs textes : ʿAlī b. Abī Ṭālib, quatrième calife, mort en 40 ; ʿAbdallāh b. Abī Bakr b. Muḥammad b. ʿAmr b. Ḥazm, Anṣārī tābiʿī mort en 135, compté parmi les gens du maghāzī. Les gloses arment le lexique : le terme-tête à coquille défini « elle a été posée » ; quaddahu — deux sandales au cou, le signe visible du hady ; achʾarah — fendu la bosse du flanc gauche. Le résumé en trois items annonce les trois sections de la recherche légale.",
        "Première section : ce qui est licite. La sunna mūjazza (n° 1118) — « le thanī et ce qui est au-dessus » — se déroule dans le tableau des quatre espèces : le jadʾ du mouton d’une année lunaire révolue (né le jour du sacrifice, valable dans sa deuxième année de l’année suivante) ; le thanī du bouc entré dans la deuxième d’une entrée claire d’un mois ; le thanī de la vache entré dans la quatrième après trois années ; le thanī du chameau entré dans la sixième après cinq années — et la fāʾida : le mâle et la femelle se valent. Puis l’offrande de ce qui est aisé — fā-mā istaysara mina l-hady (imprimé « al-Baqara, l’āya 195 » = cache ḥafṣ 196) : Ibn ʿUmar lit « une chamelle à sacrifier ou une vache » (n° 1144) ; ʿAlī et Ibn ʿAbbās « un mouton » (n° 1142) — la lecture que Mālik aime le plus entendre. La clause du n° 1143 descend la hiérarchie : ce qui n’atteint pas le chameau se juge par la vache, ce qui n’atteint pas la vache par le mouton, ce qui n’atteint pas le mouton est une expiation — jeûne ou nourriture de pauvres.",
        "Deuxième section : la conduite. La glorification — quiconque glorifie les rites d’Allah, cela vient de la piété des cœurs (al-Ḥajj, imprimé « l’āya 30 » = cache ḥafṣ 32) ; les chaʾāʾir sont le hady et les bêtes marquées — glorification, engraissement (tasmīn), zèle ; ʿUrwa à son fils : « ce qui n’est pas offert en offrande, Allah l’offre — que ce soit alors de Sa générosité, ce qu’elle a de plus noble » (n° 1120). L’usage reprend le n° 1113 et complète par le n° 1114 : la lance dans la bosse au marquage en disant « bismi llāhi wa-llāhu akbar », en suivi de « afin que vous magnifiiez Allah pour ce qu’Il vous a guidés » (le renvoi imprimé « al-Baqara, l’āya 184 » porte le texte du Ḥajj 37 du cache, erreur consignée) : conduire l’offrande est déjà un acte de louange. Troisième section : le profit. La montée — « monte-la, malheur à toi » (n° 1107) mais le jumhūr et Mālik dans le réputé la blâment par choix sauf nécessité ; le lait — blâmé par choix, même le surplus du petit : retour sur l’aumône, amende où il y a préjudice, licence de la contrainte (n° 1112 : le petit s’en rassasie, à l’immolation fais manger son petit avec elle) ; la chair — le réputé autorise de toute offrande ayant atteint son terme, excepté trois : la rançon de la chasse, l’expiation du préjudice, le voué aux pauvres (n° 1126).",
        "La clôture tire les desseins : la shariʾa noble est fondée sur la facilité — le tamattuʿ de la ʿumra jusqu’au ḥajj par une offrande, en glorification des rites, en honneur des hôtes du Miséricordieux, en facilité pour les pauvres de Makka. L’évaluation verrouille les sections une et trois — deux items, un cours à moitié : la leçon 18 portera la seconde. L’exploitation fait travailler l’athar final (n° 1108, ʿAbdallāh b. Dīnār) : Ibn ʿUmar offrait au ḥajj deux chamelles — badnatayn badnatayn — et à la ʿumra une, immolée debout dans la maison de Khālid b. ʿAsīd, la lance de la fosse du cou jusqu’à sortir sous l’omoplate — le nombre au-dessus du minimum du tableau, le lieu libre (la demeure même du pèlerin), l’expertise du pèlerin immolant de sa propre main. La préparation annonce la leçon 18 : celui qui a manqué le ḥajj, celui qui a touché son épouse en état de sacralisation.",
    ],
    "points": [
        "Fil de révision : deux objectifs → quatre questions du tamhīd → quatre textes → trois sections du fiqh (licite, conduite, profit) → évaluation en deux items → athar d’exploitation n° 1108.",
        "La sunna mūjazza (n° 1118) : le jadʾ du mouton (une année révolue), le thanī du bouc (entrée claire d’un mois), de la vache (quatrième après trois ans), du chameau (sixième après cinq ans) — mâle et femelle se valent.",
        "L’aisé (īhdāʾ mā istaysar) : chamelle ou vache pour Ibn ʿUmar (n° 1144), mouton pour ʿAlī et Ibn ʿAbbās (n° 1142) — la lecture que Mālik aime le plus entendre ; la hiérarchie descend jusqu’à l’expiation (jeûne ou nourriture de pauvres) (n° 1143).",
        "La conduite (n° 1113) : parure et marquage à Dhī l-Ḥulayfa vers la qibla, garlanding avant marquage, flanc gauche ; immobilisée à ʿArafa ; immolée à Minā avant toute coupe, de sa propre main, debout face à la qibla — puis manger et nourrir ; la lance et le takbīr au marquage (n° 1114).",
        "Le profit : la montée blâmée par choix sauf nécessité (n° 1107) ; le lait blâmé — retour sur l’aumône, amende où il y a préjudice, licence de la contrainte (n° 1112) ; la chair — le réputé autorise sauf trois exceptions : rançon de la chasse, expiation du préjudice, voué aux pauvres (n° 1126).",
        "Les desseins : glorifier les rites d’Allah (la piété des cœurs, n° 1120), honorer les hôtes du Miséricordieux, faciliter aux pauvres de Makka — la shariʾa fondée sur la facilité ; conduire l’offrande est déjà un acte de louange (n° 1114).",
    ],
    "vocabulaire": [
        {"ar": "الهدي", "translit": "al-hady", "fr": "la bête d’offrande — un rite du ḥajj et une de ses chaʾāʾir : l’espèce et l’âge en première section, la conduite en deuxième, le profit en troisième"},
        {"ar": "السنة المؤجزة", "translit": "as-sunna al-mūjazza", "fr": "le seuil réductible de l’offrande — « le thanī et ce qui est au-dessus » (n° 1118) : l’âge en deçà duquel la bête ne vaut pas de hady"},
        {"ar": "الاستيسار", "translit": "al-istaysar", "fr": "l’aisé du hady — ce qui t’est aisé d’offrir : chamelle ou vache chez Ibn ʿUmar (n° 1144), mouton chez ʿAlī et Ibn ʿAbbās (n° 1142)"},
        {"ar": "السوق", "translit": "as-sūq", "fr": "la conduite de l’offrande — parure, marquage, marche de Dhī l-Ḥulayfa à ʿArafa puis Minā, immolation de sa propre main (ṣifat sūq al-hady, n° 1113)"},
        {"ar": "الشعائر", "translit": "ach-chaʾāʾir", "fr": "les rites d’Allah — ici le hady et les bêtes marquées : leur glorification, leur engraissement et le zèle mis en elles viennent de la piété des cœurs"},
        {"ar": "القلائد", "translit": "al-qalāʾid", "fr": "les colliers — la parure du cou nommée avec l’offrande dans la āya de la Kaʾba (al-Māʾida 97) ; le garlanding de deux sandales (quaddahu) en est la forme du cours"},
    ],
    "avertissement": "Ce commentaire est un guide de lecture du manuel ; en cas de divergence d’expression, le manuel et sa traduction savante font foi.",
}

E_405 = {
    "auteur": "IA-1, tour R723",
    "resume": "Guide de lecture de la leçon 16 (أعمال أيام منى (2)) : après les œuvres du jour de l’Immolation, le séjour et le jet — trois nuits à Minā ou deux pour l’hâtif, un hady par nuit manquée ; le jet réglé en temps, lieu, caillou, pureté et marche ; et l’excuse qui reporte le jet de al-ʿAqaba sans le détruire — le hady recommandé gardant le respect du temps manqué.",
    "explication": [
        "La page d’ouverture (p.110) fixe trois objectifs : reconnaître la règle du séjour à Minā les jours du jet des jamarāt, reconnaître la manière du jet et ses règles, observer les règles de savoir-vivre islamiques au jet et au séjour. La préparation reçue de la leçon 15 se résout ici entrée par entrée — les cinq entrées lexicales tranchées par les gloses imprimées p.111-112. Le tamhīd nomme le jet des jamarāt rite d’entre les rites du pèlerinage et sunna des sunnas : accompli en quête de la proximité d’Allah, en imitation du Prophète ﷺ, puis rappel de la qissa d’Ibrāhīm, sur lui le salut — et pose trois questions : la manière du jet, ses règles de savoir-vivre, la règle du séjour à Minā.",
        "Les quatre textes font chacun une lame. Le premier (n° 1209) pose la borne spatiale : on prétend que ʿUmar b. al-Khaṭṭāb a dit — « que personne des pèlerins ne passe les nuits de Minā de derrière al-ʿAqaba ». Le second (n° 1221) donne la première licence : le Prophète ﷺ a accordé aux bouviers de séjourner hors de Minā — jetant au jour de l’Immolation, puis le lendemain, puis deux jours après le lendemain, puis au jour du départ : le compte entier des jets, un jour décalé. Le troisième (n° 1212) décrit le savoir-vivre : Ibn ʿUmar se tenait debout longuement aux deux jamarāt — magnifiant Allah, Le glorifiant, Le louant, L’invoquant — sans s’arrêter à la Jamra de al-ʿAqaba. Le quatrième (n° 1224) règle l’excuse : la nièce de Ṣafiyya bint Abī ʿUbayd, accouchée à al-Muzdalifa, arrivée à Minā après le coucher du soleil du jour de l’Immolation — Ibn ʿUmar ordonna de jeter la Jamra à leur arrivée, et ne vit contre elles nulle chose. La notice de Nāfiʿ — mawlā d’Ibn ʿUmar, imam des tābiʿūn médinois, mort en 117 : « quand Nāfiʿ dit une chose, scelle-la », la plus saine de toutes les chaînes selon al-Bukhārī — arme la lecture.",
        "La première partie règle le séjour. Trois nuits pour qui ne se hâte pas, deux pour l’hâtif — wājib des wājibāt du ḥajj ; qui le quitte en tête ou délaisse une nuit entière doit un hady par nuit ; la preuve — Hichām d’ʿUrwa d’après son père : « que personne ne passe la nuit sinon à Minā » (n° 1210). Le séjour incombe même en nécessité — la maladie, la crainte pour ses biens ; qui est retenu à La Mecque doit le hady, hormis celui que le Prophète ﷺ a dispensé. La licence des bouviers s’étend à tous les détenteurs d’excuse hors de la pâture ; le tafsīr de Mālik (n° 1223) déroule le calendrier du jour manqué : « nul ne rattrape une chose avant qu’elle ne lui incombe » — la dette naît au lever du soleil ; le bouvier jette au premier jour du départ pour le jour passé, puis pour son jour propre — deux jets en un jour, l’ordre de la dette respecté.",
        "La deuxième partie règle le jet. Le temps : les jamarāt ne sont pas jetées les trois jours — deux pour l’hâtif — avant que le soleil ne décline (n° 1220) ; le jet recommandé avant aẓ-ẓuhr ; jeté avant le déclin, il se réitère selon les quatre imams. Le lieu de la Jamra de al-ʿAqaba : al-Qāsim jetait « d’où elles se dispersent » (min ḥaythu tachattara, n° 1217) — le Prophète ﷺ ayant jeté du fond de la vallée ; quatre singularités : réservée au jour de l’Immolation, nul arrêt, au matin de préférence, du point bas en recommandé. La manière : le pèlerin part à pied, en état de pureté, vingt-et-un cailloux en main — la première Jamra jetée face à la qibla avec invocation ; la centrale puis l’avancée au nord avec invocation ; al-ʿAqaba de sept cailloux sans arrêt ; le tout répété les trois jours ; l’hâtif jette son jour à la condition de sortir avant le coucher du soleil du troisième jour — sinon la quatrième nuit et le jet lui incombent. Les attestations de la maison d’ʿUmar font de l’invocation la moitié du jet : ʿUmar arrêté longuement « jusqu’à ce que l’homme debout fût rassasié de son arrêt » (n° 1211), Ibn ʿUmar magnifiant à chaque caillou (n° 1213).",
        "Les règles d’accompagnement nouent le geste : le caillou semblable au caillou de fronde, Mālik préférant un peu plus grand, et ne suffit pas ce qui ne mérite pas le nom de pierre (n° 1214) ; la pureté recommandée sans exigence — « je ne juge pas de réitération pour celui qui jette les jamarāt… sans être en état de pureté : mais qu’il ne s’y attache pas à dessein » (n° 1219) ; la marche à pied, pratique des Compagnons, la monture de Muʿāwiya b. Abī Sufyān — premier cavalier — encaissée dans la nécessité (n° 1216) ; le jet par délégation pour le garçon et le malade quand le port est impossible — le malade guette le moment, magnifie en son logis ; guéri dans les jours du tachrīq, celui qui jetait pour lui rejette et offre (n° 1218). Troisième partie : le report pour excuse — l’accouchée re-citée (n° 1224) : elles avaient atteint le temps du rattrapage, l’excuse les avait retenues — jet à l’arrivée, nulle chose de plus ; mais Mālik recommande le hady pour qui rencontre ce qu’elle rencontra : l’excuse lève l’obligation, non le respect du temps.",
        "L’évaluation demande la manière du jet puis deux cas à preuve : le pèlerin qui remonte chaque soir à La Mecque délaisse les nuits requises — chaque nuit manquée en entier appelle un hady, la nuit, non le jour, étant la matière du devoir (n° 1210) ; le wudūʾ rompu au cours du jet de la centrale — la pureté recommandée non exigée, le jet valide n’est point réitéré, le dessein seul est blâmé (n° 1219). L’exploitation encadre la fatwā de l’oubli d’une jamra (n° 1225) : qu’il revienne à toute heure où il se la rappelle, de nuit ou de jour, comme il accomplit la ṣalāt quand il l’a oubliée ; si le rappel advient après le départ — à La Mecque ou en sortant — le hady sur lui ; l’invite d’examen demande le type de preuve : l’analogie du rite au rite et la graduation territoriale. La préparation (p.116) annonce la leçon 17 : les trois entrées lexicales du hady — natadjjatha, at-taqlīd, al-ichʾār — et le sens de l’al-mustaysar : le hady, qui a couru sous trois formes dans le présent cours (la bête des nuits manquées, le hady recommandé de l’accouchée, le hady de l’oubli au-delà de La Mecque), passe de la sanction implicite au statut plein.",
    ],
    "points": [
        "Fil de révision : trois objectifs → trois questions du tamhīd → quatre textes → trois parties (le séjour, le jet, le report) → deux cas à preuve → fatwā de l’oubli d’une jamra.",
        "Le séjour : trois nuits pour le non-hâtif, deux pour l’hâtif — wājib des wājibāt du ḥajj ; un hady par nuit manquée en tête ou en entier, même en nécessité sauf licence prophétique (n° 1210) — la nuit, non le jour, est la matière du devoir.",
        "La licence : les bouviers hors de Minā, jetant au jour de l’Immolation, puis le lendemain, puis deux jours après, puis au jour du départ (n° 1221) ; le calendrier de Mālik — la dette naît au lever du soleil, deux jets en un jour, l’ordre respecté (n° 1223) ; étendue à toute excuse hors de la pâture.",
        "Le jet : les jamarāt après le déclin du soleil, avant aẓ-ẓuhr recommandé, réitérées selon les quatre imams (n° 1220) ; al-ʿAqaba d’où la foule se disperse, le fond de la vallée prophétique, quatre singularités (n° 1217) ; vingt-et-un cailloux face à la qibla — invocation aux deux premières, nul arrêt à al-ʿAqaba.",
        "Le savoir-vivre : le caillou de fronde ou un peu plus grand (n° 1214), la pureté recommandée non exigée (n° 1219), la marche à pied — Muʿāwiya premier cavalier par nécessité (n° 1216), l’arrêt long et le takbīr à chaque caillou (n° 1211, n° 1213) ; le jet par délégation pour le garçon et le malade (n° 1218).",
        "L’excuse : l’accouchée jette à son arrivée, nulle chose de plus (n° 1224) — mais le hady recommandé pour le temps manqué ; la jamra oubliée se rattrape comme la ṣalāt oubliée, le hady au-delà de La Mecque (n° 1225).",
    ],
    "vocabulaire": [
        {"ar": "المبيت", "translit": "al-mabīt", "fr": "le séjour nocturne à Minā — trois nuits pour le non-hâtif, deux pour l’hâtif, wājib des wājibāt du ḥajj ; un hady par nuit manquée (n° 1210)"},
        {"ar": "الرمي", "translit": "ar-ramy", "fr": "le jet des jamarāt — un rite du pèlerinage et une sunna des sunnas, réglé en temps (n° 1220), lieu (n° 1217), caillou (n° 1214) et manière"},
        {"ar": "الجمرات", "translit": "al-jamār", "fr": "pluriel de jamra — le petit caillou et le tas réuni de cailloux : trois jamarāt à Minā, sept cailloux chacune"},
        {"ar": "العقبة", "translit": "al-ʿAqaba", "fr": "le lieu de la bayʾa des Anṣār au Prophète ﷺ sur l’émigration — le nom de mémoire porté par la dernière des jamarāt : jetée sans arrêt, du fond de la vallée"},
        {"ar": "يوم التفتر", "translit": "yawm at-tafarr", "fr": "le jour du départ de Minā — le dernier jet : le bouvier qui demeure joint son retard au jet de la communauté, l’hâtif sort avant le coucher du soleil"},
    ],
    "avertissement": "Ce commentaire est un guide de lecture du manuel ; en cas de divergence d’expression, le manuel et sa traduction savante font foi.",
}


def norme_fr(s):
    s = s.replace('\'', '’')
    s = re.sub(r'\s+([;:!?»])', '\u202f\\1', s)
    s = s.replace('« ', '«\u202f')
    return s


def norme_entree(e):
    for cle in ('resume', 'avertissement'):
        if cle in e:
            e[cle] = norme_fr(e[cle])
    e['explication'] = [norme_fr(x) for x in e['explication']]
    e['points'] = [norme_fr(x) for x in e['points']]
    for v in e.get('vocabulaire', []):
        v['fr'] = norme_fr(v['fr'])
    return e


data = json.load(open(CHEMIN, encoding='utf-8'))
com = data['commentaires']
for docid, entree in (('pdf-mut23h2x-406', E_406), ('pdf-mut23h2x-405', E_405)):
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
for docid in ('pdf-mut23h2x-406', 'pdf-mut23h2x-405'):
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

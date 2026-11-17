#!/usr/bin/env python3
"""R718 — ajoute les commentaires pédagogiques des leçons 26 (pdf-mut23h2x-415)
et 27 (pdf-mut23h2x-416) à content/commentaires/hadith-3es.json.
Normalise la ponctuation FR (U+202F avant ; : ! ? » et après «) sur les
entrées nouvelles seulement — opération idempotente."""
import json, re

CHEMIN = 'content/commentaires/hadith-3es.json'

E_415 = {
    "auteur": "IA-1, tour R718",
    "resume": "Guide de lecture de la leçon 26 (أحكام الذبيحة والعقيقة) : du nom prononcé sur la bête à l’instrument de l’urgence, puis aux cinq exigences de la ʿaqīqa — comment chaque rubrique du manuel répond aux trois objectifs posés en ouverture.",
    "explication": [
        "La page d’ouverture (p.170) fixe trois objectifs : connaître les règles de la ḏabīḥa et de la ʿaqīqa, distinguer ce qui se mange d’elle de ce qui ne se mange pas, et représenter les adāb de la loi dans l’une et l’autre. Le tamhīd en donne la racine : Allah précise à l’homme le jugement de tous ses actes et dispositions, même occasionnels — rien de ce qui touche la bête égorgée n’est laissé au hasard. Les trois questions d’ouverture (فَمَا مَفْهُومُ الذَّبِيحَةِ ؟ وَمَا آدَابُ الشَّرْعِ فِيهَا ؟ وَمَا أَحْكَامُ الْعَقِيقَةِ ؟) dessinent les trois blocs du fiqh final : c’est la carte de révision de la leçon.",
        "Les trois textes font chacun un travail précis. Le premier tranche le doute de la nomination : la viande arrive de la bādiya, hors de toute audition — le Prophète ﷺ n’exige ni annulation ni enquête, il ordonne de prononcer le nom au moment de manger. Le deuxième pose l’instrument de l’urgence : la luqaḥa d’Uḥud, sans couteau à portée, létégie au šiẓāẓ — le bâton de berger à bout affûté — et le verdict : (لَيْسَ بِهَا بَأْسٌ فَكُلُوهَا). Le troisième est la sentence de Mālik (n° 1375) : une brebis pour le garçon comme pour la fille chez Mālik, et le canon (فَإِنَّمَا هِيَ بِمَنْزِلَةِ النُّسُكِ وَالضَّحَايَا) — la ʿaqīqa obéit aux mêmes interdits de vices que l’offrande. La notice du transmetteur éclaire le deuxième texte : ʿaṭāʾ b. yasār, juge médinois qui fait autorité dans la cité du Muwaṭṭaʾ, transmetteur des grands Compagnons.",
        "Le cœur du fiqh : la nomination et l’instrument. La tasmīya est obligatoire sur le ḏākir capable — non sur l’oubliieux, le contraint ou le muet (preuve de la sourate al-anʿām citée en leçon) ; l’oubliieux n’est pas fisq. La ḏabīḥa du musulman dont la nomination est inconnue se mange — mais la tasmīya au moment du manger ne remplace pas celle manquée au ḏabḥ, et la parole prêtée à Mālik (le cas des premiers temps de l’islam) est jugée faible par le manuel : le hadith lui-même ordonne la tasmīya. Qui laisse le nom à dessein : sa bête ne se mange pas. L’instrument, ensuite : toute muḥaddid qui fait couler le sang par rupture des awdāj — le fer affûté est le recommandé, le šiẓāẓ admis par nécessité ; deux signes de vie après le geste (mouvement des membres, mouvement du regard) suivent l’école de zayd b. thābit — sur elle la majorité ; le fœtus suit la ḏakāh de sa mère chez Mālik, sauf s’il sort vivant.",
        "La ʿaqīqa clôt la leçon. Sens : le poil de la tête du nouveau-né, ou la rupture des awdāj de la bête. Statut : recommandée, non obligatoire — le texte dit (فَأَحَبَّ أَنْ يَنْسُكَ) : le manuel argue que l’obligatoire ne dépend pas de l’amour du père ; et le Prophète ﷺ a immolé pour al-ḥasan et al-ḥusayn un bélier chacun. Les cinq exigences du rite (chacune appuyée sur la parole de Mālik du n° 1375) : la salubrité des vices, comme pour l’aḍḥiyya ; manger de sa viande et donner en aumône sans rien vendre, ni la peau ; que les os soient brisés ; que le bébé ne soit pas touché de son sang ; raser le poil de sa tête et donner son poids en or ou en argent. Les deux dernières marquent l’opposition explicite à la ǧāhiliyya — elle qui épargnait les os par crainte pour l’enfant et enduisait sa tête du sang pour l’auspice du courage — et la dernière s’appuie sur fāṭima pesant les cheveux de ses enfants pour en donner l’équivalent en argent."
    ],
    "points": [
        "Trois objectifs en ouverture → trois questions du tamhīd → trois blocs du fiqh : nomination et instrument, fœtus, ʿaqīqa — suivre ce fil pour réviser.",
        "Doute sur le nom (viande de la bādiya) : manger licite, nom au moment de manger ; le nom au manger ne remplace pas celui manqué au ḏabḥ.",
        "Tasmīya : obligatoire sur le capable ; l’oubliieux n’est pas fisq ; qui laisse le nom à dessein rend sa bête immangeable.",
        "Instrument : toute muḥaddid par rupture des awdāj ; fer affûté recommandé ; šiẓāẓ par nécessité (la luqaḥa) ; signes de vie : membres et regard (école de zayd b. thābit, la majorité).",
        "Fœtus : la ḏakāh de la mère suffit chez Mālik si le fœtus est mort-né ; s’il sort vivant, sa propre ḏakāh est requise.",
        "ʿaqīqa : recommandée, non obligatoire ; une brebis pour le garçon et la fille chez Mālik ; cinq exigences dont deux contre la ǧāhiliyya (os brisés, pas de sang sur le bébé) ; poids du cheveu donné en or ou en argent."
    ],
    "vocabulaire": [
        {"ar": "الذَّبِيحَة", "translit": "ḏabīḥa", "fr": "la bête égorgée — objet de la première moitié de la leçon"},
        {"ar": "الذَّكَاة", "translit": "ḏakāh", "fr": "en langue : l’achèvement ; en loi : le moyen qui rend licite l’animal sauvage"},
        {"ar": "التَّسْمِيَة", "translit": "tasmīya", "fr": "prononcer le nom d’Allah sur la bête au moment de l’égorgement"},
        {"ar": "لُقَحَة", "translit": "luqaḥa", "fr": "chamelle en lait — la bête du deuxième texte, paissant vers Uḥud"},
        {"ar": "شِظَاظ", "translit": "šiẓāẓ", "fr": "bâton de berger à bout affûté — l’instrument admis par nécessité"},
        {"ar": "الأَوْدَاج", "translit": "awdāj", "fr": "veines jugulaires — leur rupture fait couler le sang et valide l’égorgement"},
        {"ar": "عَقِيقَة", "translit": "ʿaqīqa", "fr": "sacrifice de naissance — du poil de la tête du nouveau-né, ou de la rupture des awdāj"}
    ],
    "avertissement": "Ce commentaire est un guide de lecture du manuel ; en cas de divergence d’expression, le manuel et sa traduction savante font foi."
}

E_416 = {
    "auteur": "IA-1, tour R718",
    "resume": "Guide de lecture de la leçon 27 (أحكام الصيد) : cinq textes du Muwaṭṭaʾ qui tracent la frontière entre tir légitime et outil écrasant, entre chasseur seul et chasse aidée — jusqu’à la licence la plus large du cours, celle de la mer.",
    "explication": [
        "Les objectifs (p.177) reprennent le couple habituel du manuel : connaître les règles de la chasse, distinguer ce qui se mange du gibier de ce qui ne se mange pas, et représenter les valeurs qu’elles portent. Le tamhīd ouvre par la licitation divine : la sourate al-māʾida pour le gibier terrestre (أُحِلَّ لَكُمُ الطَّيِّبَاتُ), la sourate an-naḥl pour la mer (لِتَأْكُلُوا مِنْهُ لَحْمًا طَرِيًّا) ; puis le partage naturel — du ṣayd, ce qui est salubre et ce qui est nocif. D’où les deux questions qui commandent toute la leçon : quand le gibier terrestre se mange-t-il, et quel statut pour le gibier de la mer ?",
        "Les cinq textes dessinent la frontière du licite. Le double récit de Nāfiʿ rejette d’abord le gibier qui meurt entre les mains du chasseur : l’oiseau atteint du tir depuis l’éperon (al-ǧuruf) n’est pas tombé par l’effet du trait — Ibn ʿUmar le jette. La sentence de Mālik écarte ensuite le muʿaẓẓāḍ — le bâton à tête durcie, avec ou sans fer — même quand le trait s’est planté (ḫasaq) jusqu’à la profondeur de l’affût (al-maġāthil). Le troisième texte règle le gibier aidé : l’eau ou un chien non dressé entrelacent deux causes de mort — le gibier ne se mange que si la flèche du tireur a donné la mort certaine ou atteint la profondeur qui n’admet plus le répit. La parole d’Ibn ʿUmar étend la licence à la bête dressée : (كُلُّ مَا أَمْسَكَ عَيْنُكَ) — tout ce que l’œil du maître a suivi jusqu’à la prise. Le cinquième texte, porté par Abū Salama, donne la mer : Abū Hurayra et Ibn ʿabbās ne voient pas de nuisance dans le poisson que la mer rejette mort — elle n’a pas les voies de corruption de la terre.",
        "La notice du transmetteur ancre ce dernier texte : Abū Salama b. ʿabd ar-Raḥmān, fils du Compagnon ʿabd ar-Raḥmān b. ʿawf, faqīh tābiʿī mort à Médine en 94 H — l’un des maîtres de la cité du Muwaṭṭaʾ, auprès duquel Nāfiʿ et les grands rapportent. Et la glose tient le vocabulaire de la leçon : al-ǧuruf (lieu près de Médine), al-muʿaẓẓāḍ (l’outil), ḫasaq (le trait fixé) — trois mots à savoir rendre.",
        "Le fiqh répartit la matière en deux moitiés. Ce qui ne se mange pas : l’outil frappant — l’argumentation relie le geste d’Ibn ʿUmar, le Livre (أَوْفُوا بِالْعُقُودِ) et le hadith d’ʿadī, la limite passant au bord de l’outil : la part atteinte par la tranche dure est licite, celle frappée par le plat qui écrase non ; le gibier à double cause de mort, tant que la cause demeure incertaine ; le gibier perdu retrouvé après une nuit — le critère joint la durée et la trace, et la nuit passée renverse la licence en réprobation pesante (karāhat taḥrīm, sur le hadith d’Abū Thaʿlaba). Ce qui se mange : la chasse par bêtes dressées — le taʿlīm est condition de toute chasse par ǧawāriḥ (وَمَا عَلَّمْتُمْ مِنَ الْجَوَارِحِ) ; ce que la bête saisit vivant est licite, l’animal repris vivant dans sa main et non délivré ne l’est pas ; ce dont elle a mangé ne change rien chez Mālik — le manuel concilie avec le hadith d’ʿadī (فَإِنَّهُ أَذْكَى عَلَى نَفْسِهِ) en portant l’interdit sur la réprobation. Et le ṣayd al-baḥr clôt le cours par la licence universelle : ni dressage, ni nomination, ni immolation, ni chasseur croyant ne s’y lie — portée par zayd b. thābit et Abū Hurayra, étendue par Ibn ʿabbās au gibier chassé en mer par les infidèles."
    ],
    "points": [
        "Cinq textes, cinq frontières : la mort entre les mains du chasseur, l’outil écrasant, l’aide de l’eau ou du chien non dressé, la bête dressée, la mer.",
        "Muʿaẓẓāḍ : pas de ḏakāh — même trait planté jusqu’au maġāthil ; la frontière passe entre la tranche dure (licite) et le plat qui écrase (non).",
        "Gibier aidé (eau, chien non dressé) : immangeable tant que la cause de mort est incertaine ; licite si la flèche a donné la mort certaine.",
        "Gibier perdu : intervalle court sans soupçon de mélange + trace (flèche ou chien) → licite ; une nuit passée → karāhat taḥrīm (hadith d’Abū Thaʿlaba).",
        "Bête dressée : le taʿlīm condition de toute chasse par ǧawāriḥ ; ce dont elle a mangé reste licite chez Mālik (conciliation portée sur la réprobation).",
        "Gibier de mer : licence universelle — aucun des critères du gibier terrestre ne s’y lie."
    ],
    "vocabulaire": [
        {"ar": "الصَّيْد", "translit": "ṣayd", "fr": "le gibier, la chasse — terrestre ou maritime"},
        {"ar": "الْمُعَزَّاض", "translit": "al-muʿaẓẓāḍ", "fr": "bâton à tête durcie, avec ou sans fer — l’outil frappant qui ne donne pas la ḏakāh"},
        {"ar": "خَسَق", "translit": "ḫasaq", "fr": "le trait qui s’est planté et reste fixé dans la cible"},
        {"ar": "الْجُرْف", "translit": "al-ǧuruf", "fr": "lieu près de Médine — la scène de chasse de Nāfiʿ"},
        {"ar": "الْمُعَلَّم", "translit": "al-muʿallam", "fr": "la bête dressée — entraînée à prendre le gibier"},
        {"ar": "كَرَاهَة تَحْرِيم", "translit": "karāhat taḥrīm", "fr": "réprobation pesante proche de l’interdit — le statut du gibier perdu une nuit"}
    ],
    "avertissement": "Ce commentaire est un guide de lecture du manuel ; en cas de divergence d’expression, le manuel et sa traduction savante font foi."
}

def norme_fr(s):
    """Ponctuation FR : U+202F avant ; : ! ? » et après « ; apostrophe ’."""
    s = s.replace("'", "’")
    for p in (';', ':', '!', '?', '»'):
        s = re.sub(r' ' + re.escape(p), '\u202f' + p, s)
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
for docid, entree in (('pdf-mut23h2x-415', E_415), ('pdf-mut23h2x-416', E_416)):
    if docid in com:
        print(f'!! {docid} déjà présent — rien de fait')
        raise SystemExit(1)
    com[docid] = norme_entree(entree)

with open(CHEMIN, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
    f.write('\n')

# Validation : relecture + volume
data2 = json.load(open(CHEMIN, encoding='utf-8'))
print('entrées au total :', len(data2['commentaires']))
for docid in ('pdf-mut23h2x-415', 'pdf-mut23h2x-416'):
    e = data2['commentaires'][docid]
    mots = sum(len(x.split()) for x in [e['resume']] + e['explication'] + e['points'])
    arabes = sum(c.isascii() is False and '\u0600' <= c <= '\u06FF' for c in e['explication'][0])
    print(f'{docid} : {mots} mots (resume+explication+points), vocab {len(e["vocabulaire"])}')
# contrôle : pas d’apostrophe droite ni d’espace ordinaire avant ; : ! ? » dans le FR des nouvelles entrées
mauvais = 0
for docid in ('pdf-mut23h2x-415', 'pdf-mut23h2x-416'):
    e = data2['commentaires'][docid]
    textes = [e['resume'], e['avertissement']] + e['explication'] + e['points'] + [v['fr'] for v in e['vocabulaire']]
    for t in textes:
        if "'" in t or re.search(r' [;:!?»]', t) or re.search(r'« ', t):
            mauvais += 1
print('contrôle ponctuation FR :', 'PASS' if mauvais == 0 else f'ÉCHEC ({mavais})')

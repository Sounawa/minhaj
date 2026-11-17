#!/usr/bin/env python3
"""R719 — ajoute les commentaires pédagogiques des leçons 28 (pdf-mut23h2x-417)
et 29 (pdf-mut23h2x-418) à content/commentaires/hadith-3es.json.
Même protocole que comm-r718.py : normalisation de la ponctuation FR
(U+202F avant ; : ! ? » et après «, apostrophe courbée) sur les entrées
nouvelles seulement — opération idempotente."""
import json, re

CHEMIN = 'content/commentaires/hadith-3es.json'

E_417 = {
    "auteur": "IA-1, tour R719",
    "resume": "Guide de lecture de la leçon 28 (ما يجوز من أكل الحيوان وما لا يجوز) : de la canine qui interdit à la destination qui destine — cinq textes p.184-185, quatre appels au Livre pour les bêtes de somme, et le double statut de la bête morte : peau exploitée dès le tannage, manger réservé au contraint.",
    "explication": [
        "La page d’ouverture (p.184) fixe deux objectifs : reconnaître ce qui se mange de l’animal et ce qui ne se mange pas, et saisir la sagesse de l’interdit. Le tamhīd en donne la racine : Allah a honoré l’homme (كَرَّمَ اللهُ الْإِنْسَانَ) et l’a préféré aux autres créatures — l’alimentation ne lui est pas laissée au hasard. Trois questions d’ouverture tracent la carte du fiqh : que manger ; quand se mange la bête morte ; quel est le statut de l’exploitation de sa peau.",
        "Les cinq textes font chacun un travail précis. Le hadith d’Abū Ṯaʿlaba (n° 1407) fixe l’interdit par la qualité animale — « tout pourvu de canines parmi les bêtes féroces » — la transmission portant les deux teneurs, déclarative chez Yaḥyā (isolée) et interdite chez les rapporteurs. La sentence de Mālik sur le cheval, le mulet et l’âne (n° 1409) s’appuie sur quatre appels au Livre : l’Abeille destine ces animaux au chevauchement et à la parure ; le Pardonneur destine les bestiaux au chevauchement et au manger ; le Pèlerinage lie l’immolation au nom d’Allah et au manger ; la coordination (لِتَرْكَبُوهَا وَزِينَةً) écarte le manger de la destination du cheval — où le manger n’est pas nommé, il n’est pas destiné. Le récit du mouton mort (n° 1410) sépare l’interdit du manger de l’exploitation de la peau ; le hadith du tannage (n° 1411) purifie l’ihāb ; la sentence du contraint (n° 1413) mesure sa licence : satiété, provision, jeter dès l’autre nourriture.",
        "Première section du fiqh : la canine et les bêtes de somme. Le « pourvu de canines » est nommé par son organe d’attaque — l’animal dressé qui porte la canine sans déchirer par nature (le dāb) sort du sens : l’interdit lie à la pente du déchirement, non au seul organe. L’apparent du madhab est l’interdit, refermé sur le hadith d’Abū Hurayra (forme déclarative) et attesté par « c’est l’état des choses chez nous ». La majorité et Mālik interdisent l’âne domestique et le mulet ; le cheval reste sous le refus par l’apparent, avec quatre voies : la lām d’explication destine exclusivement au chevauchement et à la parure ; la coordination des mulets et des ânes au cheval — récits de licence ponctuels, licence de Khaibar qui prouve l’interdit par son exception ; la voie de la gratitude — le manger des bestiaux est déjà nommé au même chapitre ; enfin la perte de l’avantage du chevauchement et de la parure si le manger était licite.",
        "Deuxième section : la peau et le contraint. La majorité permet l’exploitation de la peau de la bête morte par le particularisateur : le verset interdit la mayta entière, le hadith réduit l’interdit au manger. L’objection de ceux qui interdisent toute exploitation est triée par le vocabulaire : l’écrit interdit l’ihāb brut, et la peau tannée porte d’autres noms (adīm, suḫyān). Mālik étend la purification par le tannage à toute peau : généralité de la lettre contre la restriction par la cause — et chez lui la purification est de langue, non de loi : propreté pratique, sans lever l’impureté légale.",
        "Le contraint : le seuil n’exige ni certitude absolue ni agonie ; Ibn Abī Ǧamra inverse la mesure — la faim doit porter un venin plus violent que celui de la mayta, et à ce degré le manger ne nuit plus. Mālik ouvre jusqu’à satiété et provisionnement, les deux disciples restreignent au seuil de survie. L’istithmār (n° 1414) donne la pente préférable : être cru sur sa nécessité — sans passer pour voleur — et manger sur place sans emporter ; la bête morte reste l’issue quand le crédit est refusé ou redouté."
    ],
    "points": [
        "Fil de révision : deux objectifs → trois questions du tamhīd → deux sections du fiqh (ce qui se mange ; la peau et le contraint) → trois questions de l’évaluation qui reviennent au même fil.",
        "« Pourvu de canines » : organe d’attaque nommé pour sa fonction ; l’animal dressé (dāb) sort du sens — l’interdit vise la pente du déchirement, non le seul organe.",
        "Statut : l’apparent du madhab est l’interdit, refermé sur le hadith d’Abū Hurayra (forme déclarative) et attesté par « c’est l’état des choses chez nous ».",
        "Cheval, mulet, âne : interdits chez la majorité et Mālik (âne domestique et mulet) ; le cheval sous le refus par l’apparent — quatre voies d’argument dont la comparaison des listes coraniques : là où le manger n’est pas nommé, il n’est pas destiné.",
        "Peau de la mayta : exploitée dès le tannage chez la majorité (particularisateur) ; l’écrit n’interdit que l’ihāb brut — adīm et suḫyān sortent de la lettre ; chez Mālik toute peau se tanne et s’exploite, et la purification est de langue, non de loi.",
        "Contraint : ni certitude absolue ni agonie ; le venin de la faim doit dépasser le venin de la mayta (Ibn Abī Ǧamra) ; Mālik ouvre jusqu’à satiété et provision, les disciples restreignent au seuil de survie ; devant les biens d’autrui : le crédit sur place d’abord, manger sans emporter."
    ],
    "vocabulaire": [
        {"ar": "النَّاب", "translit": "an-nāb", "fr": "la canine — la dent qui suit la quatrième ; c’est elle qui nomme l’interdit du hadith"},
        {"ar": "السِّبَاع", "translit": "as-sibāʿ", "fr": "les bêtes féroces, qui déchirent leur proie par nature"},
        {"ar": "الإِهَاب", "translit": "al-ihāb", "fr": "la peau — c’est l’ihāb brut que l’écrit prophétique interdit d’exploiter"},
        {"ar": "الدِّبَاغ", "translit": "ad-dibāġ", "fr": "le tannage — tout ce qui préserve la peau de la corruption"},
        {"ar": "الْأَدِيم", "translit": "al-adīm", "fr": "la peau tannée — avec suḫyān, l’un des noms qui la sortent de la lettre de l’écrit"},
        {"ar": "الْحُمُر الْأَهْلِيَّة", "translit": "al-ḥumūr al-ahlīyya", "fr": "l’âne domestique — son manger est interdit par la majorité et par Mālik"},
        {"ar": "الِاضْطِرَار", "translit": "al-iḍṭirār", "fr": "la contrainte — la licence de la bête morte se mesure à sa nécessité"}
    ],
    "avertissement": "Ce commentaire est un guide de lecture du manuel ; en cas de divergence d’expression, le manuel et sa traduction savante font foi."
}

E_418 = {
    "auteur": "IA-1, tour R719",
    "resume": "Guide de lecture de la leçon 29 (لائحة المصادر والمراجع) : la dernière pièce du livre n’enseigne pas de règles — elle ouvre l’atelier : le muṣḥaf en Warš, sept livres de ḥadīth, quatre commentaires, deux exégèses, quatre manuels de fiqh mālikī, quatre dictionnaires, trois recueils de biographies — vingt-quatre entrées en six rubriques.",
    "explication": [
        "La liste p.191-194 est la bibliothèque de travail du manuel : chaque élément des vingt-huit leçons — texte du Muwaṭṭaʾ, glose, verset, point de fiqh, notice de transmetteur — y retrouve son outil. L’entrée du Coran ouvre la liste, sans numéro et précédée d’un tiret : le Muṣḥaf al-Muḥammadī, en riwāyat Warš ʿan Nāfiʿ min ṭarīq al-Azraq — la lecture coranique qui fait autorité au Maroc. Vient ensuite la série numérotée : vingt-quatre entrées en chiffres occidentaux, rangées sous six rubriques vertes.",
        "Les livres de ḥadīth (1-7) : le Ṣaḥīḥ d’al-Buḫārī, les Sunan d’Abū Dāwūd, d’at-Tirmiḏī et d’an-Nasāʾī — ce dernier deux fois, la Kubrā et la Muǧtabā —, le Ṣaḥīḥ de Muslim, et le Muwaṭṭaʾ en riwāyat Yaḥyā b. Yaḥyā al-Layṯī, édition du Conseil scientifique supérieur (1434 H / 2013) — l’édition même qui porte les numéros d’ordre cités dans les leçons ([al-Muwaṭṭaʾ n° …]). Les commentaires du ḥadīth (8-11) : al-Istiḏkār d’Ibn ʿAbd al-Barr, le Šarḥ d’az-Zarqānī — le commentaire qui porte chaque leçon du livre —, le Fatḥ al-Bārī d’Ibn Ḥaǧar et al-Muntaqā d’al-Bāǧī. Les exégèses (12-13) : al-Ǧāmiʿ li-aḥkām al-Qurʾān d’al-Qurṭubī et al-Muḥarrar al-Waǧīz d’Ibn ʿAṭiyya — derrière chaque verset cité dans le cours.",
        "Les livres de fiqh (14-17) dessinent l’échelle de l’école mālikī : al-Muršid al-Muʿīn d’Ibn ʿĀšir avec le šarḥ d’al-Mīyāra — le catéchisme du Maroc —, le Muḫtaṣar de Ḫalīl — le code de la madhab —, puis les deux grandes marges, la ḥāšiyya d’ad-Dasūqī sur aš-Šarḥ al-Kabīr d’ad-Dardīr et celle d’al-ʿAdawī sur la Risāla d’Ibn Abī Zayd. Les dictionnaires de langue (18-21) servent la rubrique ach-charḫ : aṣ-Ṣiḥāḥ d’al-Ǧawharī, al-Qāmūs d’al-Fīrūzābādī, Lisān al-ʿArab d’Ibn Manẓūr, les Maqāyīs d’Ibn Fāris. Les biographies (22-24) servent la tarjamat ar-rāwī : al-Iṣāba et Taḥḏīb at-Taḥḏīb d’Ibn Ḥaǧar, le Sīr d’aḏ-Ḏahabī.",
        "Comment lire la liste ? Elle fait correspondre à chaque rubrique du manuel son instrument : le texte vient de la rangée des kutub al-ḥadīth, sa lecture des šurūḥ, les versets des tafsīr, les points de fiqh des manuels mālikī, les gloses lexicales des maʿāǧim, les notices des kutub at-tarāğim. Elle apprend aussi, par ses mentions d’édition, à citer un livre : maison, ville, tirage, année hégirienne ou grégorienne — de Dār Ṣādir à Beyrouth à la Dāʾirat al-Maʿārif de l’Inde (Taḥḏīb at-Taḥḏīb, 1326 H). Le lecteur qui veut prolonger une leçon sait désormais où chercher."
    ],
    "points": [
        "La leçon ne donne aucune règle nouvelle : elle outille — à chaque rubrique du manuel correspond une rangée de la bibliothèque.",
        "Le muṣḥaf de référence est en riwāyat Warš ʿan Nāfiʿ par la voie d’al-Azraq — la transmission coranique marocaine.",
        "Le Muwaṭṭaʾ (riwāyat Yaḥyā, édition du Conseil scientifique supérieur, 1434 H / 2013) est le livre-mère : ses numéros d’ordre structurent toutes les leçons.",
        "az-Zarqānī est l’outil quotidien des leçons ; al-Istiḏkār, al-Muntaqā et Fatḥ al-Bārī complètent l’étagère des šurūḥ.",
        "La rangée de fiqh suit l’échelle de l’école : catéchisme (Ibn ʿĀšir avec al-Mīyāra), code (Muḫtaṣar Ḫalīl), gloses (ad-Dasūqī, al-ʿAdawī).",
        "Dictionnaires (aṣ-Ṣiḥāḥ, al-Qāmūs, Lisān al-ʿArab, Maqāyīs) pour ach-charḫ ; biographies (al-Iṣāba, Taḥḏīb at-Taḥḏīb, Sīr Aʿlām an-Nubalāʾ) pour la tarjamat ar-rāwī."
    ],
    "vocabulaire": [
        {"ar": "لَائِحَة الْمَصَادِر وَالْمَرَاجِع", "translit": "lāʾiḥat al-maṣādir wa-l-marāğiʿ", "fr": "la liste des sources et références — la dernière pièce du livre"},
        {"ar": "الرِّوَايَة", "translit": "ar-riwāya", "fr": "la transmission — coranique pour le muṣḥaf (Warš), textuelle pour le Muwaṭṭaʾ (Yaḥyā b. Yaḥyā)"},
        {"ar": "وَرْش", "translit": "Warš", "fr": "la lecture coranique transmise de Nāfiʿ par la voie d’al-Azraq — la lecture du Maroc"},
        {"ar": "الشَّرْح", "translit": "aš-šarḥ", "fr": "le commentaire d’un livre-mère — az-Zarqānī sur le Muwaṭṭaʾ, al-Mīyāra sur le Muršid"},
        {"ar": "الْحَاشِيَة", "translit": "al-ḥāšiyya", "fr": "la glose de marge qui accompagne un šarḥ — ad-Dasūqī sur ad-Dardīr, al-ʿAdawī sur la Risāla"},
        {"ar": "التَّحْقِيق", "translit": "at-taḥqīq", "fr": "l’édition critique — le travail du muḥaqqiq cité à presque chaque entrée"},
        {"ar": "مَعْجَم لُغَوِيّ", "translit": "maʿǧam luġawī", "fr": "dictionnaire de langue — l’atelier de la rubrique ach-charḫ"}
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
for docid, entree in (('pdf-mut23h2x-417', E_417), ('pdf-mut23h2x-418', E_418)):
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
for docid in ('pdf-mut23h2x-417', 'pdf-mut23h2x-418'):
    e = data2['commentaires'][docid]
    mots = sum(len(x.split()) for x in [e['resume']] + e['explication'] + e['points'])
    print(f'{docid} : {mots} mots (resume+explication+points), vocab {len(e["vocabulaire"])}')
# contrôle : pas d’apostrophe droite ni d’espace ordinaire avant ; : ! ? » dans le FR des nouvelles entrées
mauvais = 0
for docid in ('pdf-mut23h2x-417', 'pdf-mut23h2x-418'):
    e = data2['commentaires'][docid]
    textes = [e['resume'], e['avertissement']] + e['explication'] + e['points'] + [v['fr'] for v in e['vocabulaire']]
    for t in textes:
        if "'" in t or re.search(r' [;:!?»]', t) or re.search(r'« ', t):
            mauvais += 1
print('contrôle ponctuation FR :', 'PASS' if mauvais == 0 else f'ÉCHEC ({mauvais})')

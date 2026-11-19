# -*- coding: utf-8 -*-
"""R767 — pose du commentaire pdf-29 (leçon 29, لائحة المصادر والمراجع — Liste des
sources et références, vingt-neuvième et dernière leçon du manuel) dans
content/commentaires/hadith-5ep.json.
Spans ARABES : tirés du corpus (verbatim par construction) ; translit : écrit à
la convention ʾ/ʿ (U+02BE/U+02BF) du corpus ; fragments FR « » hardcodés puis
vérifiés verbatim contre le corpus élargi (pdf-29 + pdf-1/2/3/4/6/9/10/16/17/
18/19/22/23/25/26/27/28).
Gardes : fenêtre 1700-2400 mots (resume+explication+points), typographie FR
(’ « » U+202F), zéro arabe hors parenthèses, vocab 8 sans harakat, recoupements,
comptes des rubriques (1/19/17/3 = 39) recomputés depuis le texte.
Abort si un garde échoue. AUCUNE modification de content/books (zone d'un autre
ouvrier)."""
import json, pathlib, re, sys

DEPOT = pathlib.Path('/home/z/my-project/minhaj')
books = json.loads((DEPOT / 'content/books/hadith-5ep.json').read_text(encoding='utf-8'))
comms = json.loads((DEPOT / 'content/commentaires/hadith-5ep.json').read_text(encoding='utf-8'))

def plain(lesson):
    t = re.sub(r'<br\s*/?>', '\n', lesson.get('htmlFr') or '')
    t = re.sub(r'</(p|h1|h2|h3|h4|div|li)>', '\n', t)
    t = re.sub(r'<[^>]+>', '', t)
    return re.sub(r'[ \t]+', ' ', t).strip()

L = {l['docId']: plain(l) for l in books['lessons']}
S29 = L['pdf-29']
S1, S2, S3, S4 = L['pdf-1'], L['pdf-2'], L['pdf-3'], L['pdf-4']
S6, S9, S10, S16 = L['pdf-6'], L['pdf-9'], L['pdf-10'], L['pdf-16']
S17, S18, S19, S22 = L['pdf-17'], L['pdf-18'], L['pdf-19'], L['pdf-22']
S23, S25, S26, S27, S28 = L['pdf-23'], L['pdf-25'], L['pdf-26'], L['pdf-27'], L['pdf-28']
T29 = [l['titleFr'] for l in books['lessons'] if l['docId'] == 'pdf-29'][0]
CORPUS = '\n'.join([S29, S1, S2, S3, S4, S6, S9, S10, S16, S17, S18, S19,
                    S22, S23, S25, S26, S27, S28, T29])

def pull(src, start, end_marker):
    i = src.find(start)
    if i < 0:
        raise SystemExit(f'PULL start introuvable: {start[:60]}')
    j = src.find(end_marker, i)
    if j < 0:
        raise SystemExit(f'PULL end introuvable: {end_marker[:60]}')
    return src[i:j + len(end_marker)]

def chk(frag, src, lbl=''):
    if frag not in src:
        raise SystemExit(f'CHK absent ({lbl or frag[:60]})')
    return frag

NB = '\u202f'
FR = lambda s: '«' + NB + s + NB + '»'

def typ(s):
    """Normalisation typographique FR : NB avant ; : ! ? » et après «."""
    for a, b in ((' :', NB + ':'), (' ;', NB + ';'), (' ?', NB + '?'),
                 (' !', NB + '!'), (' »', NB + '»'), ('« ', '«' + NB)):
        s = s.replace(a, b)
    return s

# ---- comptes des rubriques recomputés depuis le texte de la leçon
lignes29 = [x for x in S29.split('\n')]
hdr = [i for i, x in enumerate(lignes29)
       if re.match(r'^(Le Coran \(|Les livres de hadith \(|Les commentaires de hadith \(|Autres références \()', x)]
cnts = []
for k, i in enumerate(hdr):
    end = hdr[k + 1] if k + 1 < len(hdr) else len(lignes29)
    cnts.append(sum(1 for y in lignes29[i + 1:end] if y.strip()))
if cnts != [1, 19, 17, 3]:
    raise SystemExit(f'COMPTES rubriques inattendus : {cnts}')
if sum(cnts[1:]) != 39:
    raise SystemExit('COMPTES : la somme des rubriques 2-4 ne fait pas 39')

# ---- citations « » tirées du corpus (verbatim par construction)
Q_APPAREIL = pull(S29, 'tels qu’imprimés', 'de l’édition')
Q_RUBRIQUES = pull(S29, 'en quatre rubriques', 'd’autres références —')
Q_NUMERO = pull(S29, 'La première rubrique', 'les trois rubriques restantes')
Q_WARSH = pull(S29, 'selon la lecture de Warš', 'd’al-Azraq')
Q_BUH_SS = pull(S29, 'le Recueil authentique continu', 'de ses journées')
Q_BUH_VERIF = pull(S29, 'professeur du hadith', 'université de Damas')
Q_BUH_ED = chk('Dār Ibn Kaṯīr, al-Yamāma - Beyrouth, 3e éd., 1407 H / 1987', S29, 'Buḫārī éd.')
Q_MALIK_ED = chk('édition du Conseil scientifique supérieur', S29, 'Conseil scientifique')
Q_ABUDAWUD1 = pull(S29, 'vérification de Muḥammad Muḥyī d-Dīn ’Abd al-Ḥamīd', 'Dār al-Fikr')
Q_MUJTABA_ED = chk('Maktab al-Maṭbū’āt al-Islāmiyya - Alep', S29, 'Alep')
Q_KUBRA_ED = chk('Dār al-Kutub al-’Ilmiyya, Beyrouth, 3e éd., 1424 H / 2003', S29, 'kubrā éd.')
Q_MANUEL = chk('Le hadith tiré du livre des Arba’ūn nawawiyya de l’imam al-Nawawī, '
               'avec le commentaire d’Ibn Daqīq al-’Īd', S29, 'titre du manuel')
Q_INTENTION = chk('à l’intention des élèves de cinquième année de l’enseignement '
                  'primaire traditionnel', S29, 'intention')
Q_MUHAMMADIEN = chk('muḥammadien', S29, 'muḥammadien')
Q_FONDATION = chk('publié par la Fondation Mohammed VI pour l’édition du Noble Coran',
                  S29, 'fondation')
Q_MAGA = chk('Māǧa est le nom de son père', S29, 'Māǧa père')
Q_MUJTABA = chk('al-Muǧtabā min as-sunan', S29, 'muǧtabā')
Q_MINORES = chk('les Sunan mineures d’an-Nasā’ī', S29, 'sunan mineures')
Q_BAYY = chk('connu comme Ibn al-Bayy’', S29, 'Ibn al-Bayy’')
Q_TURKI = chk('et d’autres, sous la supervision de Dr ’Abd Allāh ibn ’Abd al-Muḥsin at-Turkī',
              S29, 'supervision Turkī')
Q_MANUEL_TIRE = chk('le commentaire dont le présent manuel est tiré', S29, 'manuel tiré')
Q_DAQIQ = chk('Taqīy d-Dīn Abī l-Fatḥ Muḥammad ibn ’Alī ibn Wahb ibn Muṭī’ al-Qašayrī, '
              'connu comme Ibn Daqīq al-’Īd', S29, 'Ibn Daqīq')
Q_MS = chk('manuscrit, de la main de Muḥammad ’Arz ibn Riḍwān al-Walīlī', S29, 'manuscrit')
Q_FATH_MUBIN = chk('L’ouverture manifeste, commentaire des Quarante', S29, 'fatḥ mubīn')
Q_OPEN_OCTROY = chk('Les ouvertures octroyées', S29, 'ouvertures octroyées')
Q_FATH_NUM = chk('numérotation de ses livres, chapitres et hadiths par Muḥammad Fu’ād '
                 '’Abd al-Bāqī', S29, 'numérotation Fu’ād')
Q_FATH_SUP = chk('corrigé et imprimé sous la supervision de Muḥibb d-Dīn al-Ḫaṭīb',
                 S29, 'supervision al-Ḫaṭīb')
Q_CORDOUE = chk('savant du hadith originaire de Cordoue, mort en l’an 449 H', S29, 'Cordoue')
Q_UMDAT = chk('L’appui du lecteur, commentaire du Ṣaḥīḥ d’al-Buḫārī', S29, 'ʿumdat')
Q_IKMAL = chk('Achèvement de l’enseignant par les profits de Muslim', S29, 'ikmāl')
Q_MINHAJ = chk('al-Minhāǧ šarḥ Ṣaḥīḥ Muslim ibn al-Ḥaǧǧāǧ', S29, 'minhāǧ')
Q_MUZAYN = chk('connu comme Ibn al-Muzayn, mort en 656 H', S29, 'Ibn al-Muzayn')
Q_SUYUTI_G = chk('Le petit recueil des hadiths de l’annonciateur et de l’avertisseur',
                 S29, 'Ǧāmi’ ṣaġīr glose')
Q_SUYUTI_D = chk('849 - 911 H', S29, 'as-Suyūṭī dates')
Q_TAYSIR = chk('La facilitation, commentaire du Petit recueil', S29, 'taysīr')
Q_FAYD = chk('L’abondance du Tout-Puissant, commentaire du Petit recueil', S29, 'fayḍ')
Q_DALIL = chk('Le guide des réussissants vers les voies des Jardins des vertueux',
              S29, 'dalīl')
Q_ADAB = chk('Les règles de comportement', S29, 'ʾādāb')
Q_ILM = chk('Le compendium de l’exposé de la science et de son mérite', S29, 'ǧāmi’ ʿilm')
Q_TAFSIR = chk('Le commentaire coranique d’Ibn Abī Ḥātim', S29, 'tafsīr glose')
Q_TAFSIR_D = chk('mort en l’an 327 de l’hégire', S29, 'Ibn Abī Ḥātim date')
Q_6ED = chk('6e éd., 1424 H', S29, '6e éd.')
Q_NUL_L27 = chk('L’œuvre de nul d’entre vous ne le sauvera', S27, 'œuvre de nul L27')
Q_IKMAM_L4 = chk('Ikmāl ikmām al-mu’allim', S4, 'ikmām L4')

resume = (
    "Guide de lecture de la leçon 29 (Liste des sources et références — "
    "lāʾiḥat al-maṣādir wa-l-marāǧiʿ (لائحة المصادر والمراجع)) : la "
    "vingt-neuvième et dernière leçon du manuel « " + Q_MANUEL + " » — aucun "
    "hadīth des Quarante ici : la liste « ferme le volume ». "
    "Elle dresse, " + Q_RUBRIQUES + ", « les trente-neuf ouvrages mobilisés par "
    "les auteurs du manuel », avec " + Q_APPAREIL + NB + ". Première entrée, hors "
    "numérotation : le Noble Coran " + Q_WARSH + " — le muṣḥaf « " +
    Q_MUHAMMADIEN + " » publié par la Fondation Mohammed VI — puis dix-neuf "
    "livres de hadith (1-19), dix-sept commentaires (20-36) ouverts par celui "
    "d’Ibn Daqīq al-’Īd — « le commentaire dont le présent manuel est tiré » — "
    "et trois autres références (37-39). Les étiquettes d’attribution "
    "rencontrées leçon après leçon retrouvent ici leurs recueils ; l’unique "
    "« manuscrit » de la liste est le commentaire des Quarante d’aš-Šubraḫītī, "
    "entendu à la leçon 27."
)

explication = [
    # P1 — place et définition
    ("La leçon 29 n’installe aucun hadīth des Quarante : son texte est la liste "
     "elle-même, et elle « ferme le volume ». Elle s’ouvre par la définition du "
     "manuel — « " + Q_MANUEL + " » — " + Q_INTENTION + " : le recueil des "
     "Quarante de l’imam an-Nawawī, glosé par Ibn Daqīq al-’Īd — la formule que "
     "porte chacune des vingt-neuf leçons, la leçon 27 y comprise, mot à mot. "
     "Ici, elle gouverne une page d’appareil : rien ne se cite, tout se "
     "répertorie — « ferme le volume »."),
    # P2 — l’appareil de chaque entrée, et le « cas échéant »
    ("La liste dresse « les trente-neuf ouvrages mobilisés par les auteurs du "
     "manuel » " + Q_RUBRIQUES + ", et chaque entrée porte " + Q_APPAREIL + NB +
     ". Le « cas échéant » "
     "gouverne la page : là où l’imprimé se tait, la liste se tait — Abū Dāwūd "
     "sans date de mort à sa première entrée, « mort en 275 H » à la seconde, "
     "« autre édition » ; Fayḍ al-Qadīr « 1re éd., 1356 », millésime sans H."),
    # P3 — le Coran, hors rang
    (Q_NUMERO + ". Une seule entrée hors rang — le Livre avant tout rang : le "
     "Noble Coran " + Q_WARSH + ", le muṣḥaf « " + Q_MUHAMMADIEN + " » " +
     Q_FONDATION + NB + ". La précision « par la voie d’al-Azraq » relève la "
     "discipline de la transmission : la riwāya de Warš passe par deux ṭuruq, "
     "al-Azraq et al-Aṣbahānī."),
    # P4 — kutub : les Deux Ṣaḥīḥs et le Muwaṭṭaʿ
    ("La deuxième rubrique — les livres de hadith (kutub al-ḥadīṯ (كتب الحديث)) — "
     "s’ouvre sur le Ṣaḥīḥ d’al-Buḫārī, « mort en 256 H », dont la liste donne le "
     "sous-titre intégral — « " + Q_BUH_SS + " » —, " + Q_BUH_ED + NB + ". Puis "
     "le Ṣaḥīḥ de Muslim, « mort en 261 H », vérifié par Muḥammad Fu’ād ’Abd "
     "al-Bāqī. Puis al-Muwaṭṭa’ de l’imam Mālik, "
     "« transmission de Yaḥyā ibn Yaḥyā al-Layṯī », " + Q_MALIK_ED + ", 1re éd., "
     "1434 H / 2013."),
    # P5 — les Sunan et le doublon d’Abū Dāwūd
    ("Suivent les Sunan : d’at-Tirmiḏī, d’Ibn Māǧa « mort en 273 H » avec la "
     "précision généalogique « " + Q_MAGA + " », d’an-Nasā’ī « mort en 303 H » "
     "présenté « " + Q_MUJTABA + " », « " + Q_MINORES + " » — vérifié par "
     "’Abd al-Fattāḥ Abū Ġadda — et al-Sunan al-kubrā d’al-Bayhaqī « mort en "
     "458 H », " + Q_KUBRA_ED + NB + ". Et un doublon assumé : Abū "
     "Dāwūd revient deux fois — d’abord sans date de mort (" + Q_ABUDAWUD1 + NB +
     "), puis « autre édition », « mort en 275 H » : deux entrées pour un même "
     "recueil, telles qu’imprimées."),
    # P6 — le corpus élargi des kutub
    ("Le corpus s’élargit : Ṣaḥīḥ Ibn Ḥibbān « mort en 354 H » ; al-Mustadrak "
     "d’al-Ḥākim « mort en 405 H », « " + Q_BAYY + " » — la voie blanche de la "
     "leçon 28 portait cette attribution ; le Musnad de "
     "l’imam ’Aḥmad ibn Ḥanbal « mort en 241 H », vérifié par Šu’ayb "
     "al-’Arnā’ūṭ ; les trois Mu’ǧams d’aṭ-Ṭabarānī — "
     "« mort en 360 H » aux trois entrées : al-kabīr, al-awsaṭ, aṣ-ṣaġīr — ; "
     "Šu’ab al-’īmān d’al-Bayhaqī, second titre du même auteur ; le Musnad "
     "d’Abī Ya’lā « mort en 307 H » ; aš-Šamā’il d’at-Tirmiḏī et Faḍā’il "
     "aṣ-Ṣaḥāba d’ibn Ḥanbal, second titres des deux Sunan/Musnad : les grands "
     "noms reviennent, chaque fois avec leur date."),
    # P7 — šurūḥ : la racine du manuel
    ("La troisième rubrique — les commentaires de hadith (šurūḥ al-ḥadīṯ "
     "(شروح الحديث)) — s’ouvre sur la racine même du manuel : Šarḥ al-’Arba’īn "
     "an-nawawiyya de « " + Q_DAQIQ + " » — « " + Q_MANUEL_TIRE + " » — "
     "Mu’assasat ar-Rayyān, " + Q_6ED + ", sans date de mort : « le cas "
     "échéant ». La boucle est parfaite — le manuel s’était défini par ce "
     "commentaire ; sa liste s’ouvre par lui."),
    # P8 — la famille des Quarante, et le manuscrit
    ("Deux commentaires des Quarante suivent : al-Fatḥ al-mubīn d’Ibn Ḥaǧar "
     "al-Haytamī — « " + Q_FATH_MUBIN + " » — et al-Futūḥāt al-wahbiyya "
     "d’Ibrāhīm ibn Mur’ī aš-Šubrāḫītī — « " + Q_OPEN_OCTROY + " » — et "
     "l’exception de la liste : « " + Q_MS + " ». Et la leçon 27 avait déjà "
     "entendu ce commentaire : son "
     "istiṯmār citait aš-Šubraḫītī — « " + Q_NUL_L27 + " » — sous l’étiquette "
     "complète [al-Futūḥāt al-wahbiyya d’aš-Šubraḫītī, avec le choix d’une "
     "autre narration du hadith, différant quelque peu] : l’entrée « manuscrit » "
     "de la liste est déjà un personnage du cours."),
    # P9 — les quatre commentaires du Ṣaḥīḥ d’al-Buḫārī
    ("Sur le Ṣaḥīḥ d’al-Buḫārī, quatre commentaires. Fatḥ al-Bārī d’Ibn Ḥaǧar "
     "al-’Asqalānī — « " + Q_FATH_NUM + " », Dār al-Ma’rifa, 1379 H. Fatḥ "
     "al-Bārī d’Ibn Raǧab « mort en 795 H » — même titre, deux auteurs : la "
     "liste ne confond pas, chaque entrée porte le sien. Šarḥ Ibn Baṭṭāl "
     "li-Ṣaḥīḥ al-Buḫārī — Ibn Baṭṭāl, « " + Q_CORDOUE +
     " » — dont la leçon 16 portait l’étiquette [Šarḥ Ṣaḥīḥ al-Buḫārī d’Ibn "
     "Baṭṭāl, adapté]. Et ’Umdat al-qārī d’al-’Aynī, « mort en 855 H » — « " +
     Q_UMDAT + " »."),
    # P10 — les quatre commentaires du Ṣaḥīḥ de Muslim
    ("Sur le Ṣaḥīḥ de Muslim, quatre commentaires aussi. Ikmāl al-mu’lim du cadi "
     "’Iyāḍ ibn Mūsā ibn ’Iyāḍ al-Yaḥṣubī as-Sabtī, « mort en 544 H » — « " +
     Q_IKMAL + " ». Šarḥ an-Nawawī ’alā Muslim — « " + Q_MINHAJ + " » — l’imam "
     "des Quarante en commentateur de Muslim. Al-Mufhim li-mā ’aškala min "
     "talkīṣ kitāb Muslim — « " + Q_MUZAYN + " ». Et Ikmāl Ikmāl al-mu’lim "
     "d’al-Waštānī « mort en 827 H » — "
     "le titre qui achève l’achèvement ; la leçon 4 avait porté « " + Q_IKMAM_L4 +
     " » : autre forme imprimée — consignée, non corrigée."),
    # P11 — la chaîne du Ǧāmiʿ ṣaġīr, et al-Bayhaqī par trois portes
    ("Une chaîne s’écrit à trois noms : al-Ǧāmi’ aṣ-ṣaġīr de l’imam as-Suyūṭī — "
     "« " + Q_SUYUTI_D + " » — « " + Q_SUYUTI_G + " » ; puis at-Taysīr "
     "d’al-Munāwī, « mort en 1031 H » — « " + Q_TAYSIR + " » ; puis Fayḍ "
     "al-Qadīr du même al-Munāwī — « " + Q_FAYD + " » — mais en quatrième "
     "rubrique : le même commentateur, deux entrées, deux rubriques. Entre eux : "
     "Dalīl al-fāliḥīn d’Ibn ’Allān, « mort en 1057 H » — « " + Q_DALIL + " » —, "
     "Ǧāmi’ al-’ulūm wa-l-ḥikam d’Ibn Raǧab et al-’Ādāb d’al-Bayhaqī — « " +
     Q_ADAB + " » : al-Bayhaqī entre dans la liste par trois portes."),
    # P12 — marāǧiʾ uḫrā
    ("La quatrième rubrique — Autres références (marāǧi’ uḫrā (مراجع أخرى)) — "
     "trois entrées, 37 à 39. Ǧāmi’ bayān al-’ilm wa-faḍlih d’Ibn ’Abd al-Barr — "
     "« " + Q_ILM + " » —, entrée silencieuse : ni vérificateur ni maison "
     "d’édition, « 1re éd., 1414 H ». Tafsīr Ibn ’Abī Ḥātim — « " + Q_TAFSIR +
     " » —, l’unique tafsīr de la liste, « " + Q_TAFSIR_D + " ». Et Fayḍ "
     "al-Qadīr, « 1re éd., 1356 » — l’al-Munāwī de la chaîne, millésime sans H."),
    # P13 — la résolution des étiquettes
    ("La liste résout les étiquettes : ce que les leçons portaient entre "
     "crochets retrouve ici son entrée — les Ṣaḥīḥs d’al-Buḫārī et de Muslim "
     "dès les leçons 19 et 2, le Muwaṭṭa’ et les Sunan d’at-Tirmiḏī et d’Ibn "
     "Māǧa, al-Sunan al-kubrā, Ṣaḥīḥ Ibn Ḥibbān, al-Mustadrak, le Musnad de "
     "l’imam Aḥmad, al-Mu’ǧam al-kabīr d’aṭ-Ṭabarānī — déjà étiqueté leçon 2 —, "
     "Šu’ab al-Īmān d’al-Bayhaqī — dès la leçon 1 —, le Šarḥ az-Zarqānī — leçon "
     "17 — et [al-Futūḥāt al-wahbiyya d’aš-Šubraḫītī…] — l’entrée « manuscrit », "
     "déjà entendue leçon 27. NB de lecture, consigné sans correction : quelques "
     "étiquettes n’ont pas d’entrée correspondante — [Musnad d’Ibn Abī Šayba] "
     "(leçon 6), [al-I’tiṣām] (leçon 9) — et des formes varient (« Ikmāl ikmām "
     "al-mu’allim » leçon 4, « Ikmāl Ikmāl al-mu’lim » ici ; « Šu’ab al-Īmān » "
     "leçon 1, « Šu’ab al-’īmān » ici) : la liste recense les ouvrages « "
     "mobilisés par les auteurs du manuel », tels qu’imprimés."),
    # P14 — clôture
    ("Pas d’iʿdād : la leçon 28 s’était achevée sans préparation, celle-ci "
     "s’achève sans suite — « ferme le volume ». La liste enseigne par son seul "
     "ordre : le Livre sans rang, les recueils de 1 à 19, leurs commentaires de "
     "20 à 36, le reste de 37 à 39 — et, dans chaque entrée, la chaîne du savoir "
     "transmis : l’auteur, sa mort, le vérificateur qui relit, la maison qui "
     "imprime. Avec cette page, la série des commentaires du livre s’achève — "
     "vingt-neuf leçons, vingt-neuf entrées — le commentaire se clôt comme la "
     "leçon : en renvoyant, jamais en corrigeant."),
]

points = [
    ("La place : vingt-neuvième et dernière leçon ; aucun hadīth des Quarante ; "
     "la liste « ferme le volume » — quatre rubriques, le Coran « sans "
     "numérotation », puis « la numérotation continue de 1 à 39 couvre ensuite "
     "les trois rubriques restantes »."),
    ("L’appareil : chaque entrée porte « tels qu’imprimés : le titre, l’auteur "
     "et, le cas échéant, sa date de mort, le vérificateur, la maison "
     "d’édition, le lieu, le rang et le millésime de l’édition » ; là où "
     "l’imprimé se tait, la liste se tait — Abū Dāwūd sans date, puis « autre "
     "édition » avec « mort en 275 H » ; Fayḍ al-Qadīr « 1re éd., 1356 », "
     "sans H."),
    ("Le muṣḥaf : « selon la lecture de Warš d’après Nāfi’, par la voie "
     "d’al-Azraq » — le muṣḥaf « muḥammadien », « publié par la Fondation "
     "Mohammed VI pour l’édition du Noble Coran » — l’unique entrée de la "
     "première rubrique, hors numérotation."),
    ("Les livres de hadith (1-19) : al-Buḫārī « mort en 256 H », Muslim "
     "« mort en 261 H », al-Muwaṭṭa’ (« transmission de Yaḥyā ibn Yaḥyā "
     "al-Layṯī »), les Sunan — at-Tirmiḏī, Ibn Māǧa « mort en 273 H » "
     "(« Māǧa est le nom de son père »), an-Nasā’ī « mort en 303 H » "
     "(« al-Muǧtabā min as-sunan »), Abū Dāwūd deux fois (« autre édition », "
     "« mort en 275 H »), al-Sunan al-kubrā d’al-Bayhaqī « mort en 458 H » — "
     "puis Ibn Ḥibbān (354 H), al-Mustadrak (405 H), le Musnad d’Aḥmad "
     "(241 H), les trois Mu’ǧams (360 H), Šu’ab al-’īmān, Abī Ya’lā (307 H), "
     "aš-Šamā’il, Faḍā’il aṣ-Ṣaḥāba."),
    ("Les commentaires (20-36) : Ibn Daqīq al-’Īd d’abord — « le commentaire "
     "dont le présent manuel est tiré » ; les Quarante trois fois (al-Fatḥ "
     "al-mubīn ; al-Futūḥāt al-wahbiyya, « manuscrit ») ; sur al-Buḫārī "
     "quatre fois (Fatḥ al-Bārī d’Ibn Ḥaǧar et d’Ibn Raǧab — 795 H —, Ibn "
     "Baṭṭāl — 449 H —, ’Umdat al-qārī — 855 H) ; sur Muslim quatre fois "
     "(Ikmāl al-mu’lim du cadi ’Iyāḍ — 544 H —, an-Nawawī, al-Mufhim — 656 H "
     "—, Ikmāl Ikmāl al-mu’lim — 827 H) ; az-Zarqānī ; Ǧāmi’ al-’ulūm d’Ibn "
     "Raǧab ; la chaîne du Ǧāmi’ ṣaġīr (as-Suyūṭī, 849 - 911 H, al-Munāwī "
     "1031 H) ; Dalīl al-fāliḥīn (1057 H) ; al-’Ādāb."),
    ("Les autres références (37-39) : la science d’Ibn ’Abd al-Barr (sans "
     "vérificateur ni maison), l’unique tafsīr — Tafsīr Ibn ’Abī Ḥātim (« mort "
     "en l’an 327 de l’hégire ») —, Fayḍ al-Qadīr d’al-Munāwī (« 1re éd., "
     "1356 », sans H) : le second al-Munāwī de la liste."),
    ("La résolution : les crochets des leçons retrouvent leurs entrées — "
     "[Ṣaḥīḥ d’al-Buḫārī] (19-22, 25), [Ṣaḥīḥ de Muslim] (2-27), [al-Muwaṭṭa’] "
     "(17, 22-23, 26-27), [Sunan d’at-Tirmiḏī] (3-26), [Sunan d’Ibn Māǧa] (16, "
     "22), [Sunan al-Bayhaqī al-kubrā] (10) et [Sunan d’al-Bayhaqī] (28), "
     "[Ṣaḥīḥ d’Ibn Ḥibbān] (17-18), [al-Mustadrak d’al-Ḥākim] (25, 28), "
     "[Musnad de l’imam Aḥmad] (21, 26-27), [al-Mu’ǧam al-kabīr] (2, 19), "
     "[Šu’ab al-Īmān] (1), [Šarḥ az-Zarqānī] (17), [Ǧāmi’ al-’ulūm] (9-10), "
     "[al-Futūḥāt al-wahbiyya] (27) — NB consigné sans correction : quelques "
     "étiquettes sans entrée ([Musnad d’Ibn Abī Šayba] leçon 6, [al-I’tiṣām] "
     "leçon 9), formes variables (Ikmāl ikmām / Ikmāl Ikmāl)."),
    ("La clôture : sans iʿdād, sans hadīth nouveau, sans application ; « ferme "
     "le volume » — vingt-neuf leçons, vingt-neuf commentaires ; la liste "
     "demeure comme l’appareil du livre."),
]

vocabulaire = [
    {"ar": "لائحة المصادر والمراجع", "translit": "lāʾiḥat al-maṣādir wa-l-marāǧiʿ",
     "fr": "la liste des sources et références — le titre de la leçon ; elle "
           "« ferme le volume » : quatre rubriques, le Coran hors rang, puis "
           "« la numérotation continue de 1 à 39 »."},
    {"ar": "المصحف المحمدي", "translit": "al-muṣḥaf al-Muḥammadī",
     "fr": "le muṣḥaf « muḥammadien » — l’édition du Noble Coran « selon la "
           "lecture de Warš d’après Nāfi’, par la voie d’al-Azraq », publiée "
           "par la Fondation Mohammed VI ; l’unique entrée de la première "
           "rubrique, hors numérotation."},
    {"ar": "كتب الحديث", "translit": "kutub al-ḥadīṯ",
     "fr": "les livres de hadith — la deuxième rubrique, entrées 1 à 19 : des "
           "Deux Ṣaḥīḥs aux Faḍā’il aṣ-Ṣaḥāba, avec l’« autre édition » "
           "d’Abū Dāwūd."},
    {"ar": "شروح الحديث", "translit": "šurūḥ al-ḥadīṯ",
     "fr": "les commentaires de hadith — la troisième rubrique, entrées 20 à "
           "36, ouverte par Ibn Daqīq al-’Īd, « le commentaire dont le présent "
           "manuel est tiré »."},
    {"ar": "مراجع أخرى", "translit": "marāǧiʾ uḫrā",
     "fr": "d’autres références — la quatrième rubrique, entrées 37 à 39 : la "
           "science d’Ibn ’Abd al-Barr, l’unique tafsīr (Ibn Abī Ḥātim), le "
           "Fayḍ al-Qadīr d’al-Munāwī."},
    {"ar": "فتح الباري", "translit": "Fatḥ al-Bārī",
     "fr": "le commentaire du Ṣaḥīḥ d’al-Buḫārī porté par la liste sous un même "
           "titre par deux auteurs — Ibn Ḥaǧar al-’Asqalānī et Ibn Raǧab (mort "
           "en 795 H) : « tels qu’imprimés », la liste ne confond pas."},
    {"ar": "الفتوحات الوهبية", "translit": "al-Futūḥāt al-wahbiyya",
     "fr": "« Les ouvertures octroyées », commentaire des Quarante "
           "d’aš-Šubraḫītī — l’unique « manuscrit » de la liste, « de la main "
           "de Muḥammad ’Arz ibn Riḍwān al-Walīlī » ; le commentaire déjà "
           "entendu à la leçon 27."},
    {"ar": "شعب الإيمان", "translit": "Šuʾab al-ʾīmān",
     "fr": "les rameaux de la foi (« Les rameaux de la foi »), d’al-Bayhaqī — "
           "« mort en 458 H » : le second titre de l’auteur d’al-Sunan al-kubrā "
           "dans la liste ; son étiquette ouvre le manuel (leçon 1)."},
]

avertissement = ("Ce commentaire est un guide de lecture du manuel ; en cas de "
                 "divergence d’expression, le manuel et sa traduction savante font foi.")

entree = {"auteur": "IA-1, tour R767",
          "resume": typ(resume),
          "explication": [typ(p) for p in explication],
          "points": [typ(p) for p in points],
          "vocabulaire": [{**v, "fr": typ(v["fr"])} for v in vocabulaire],
          "avertissement": typ(avertissement)}

# ============================ GARDES ============================
FULL = json.dumps(entree, ensure_ascii=False)
body = entree['resume'] + ' ' + ' '.join(entree['explication']) + ' ' + ' '.join(entree['points'])
n_words = len(body.split())
ok = True

if not (1700 <= n_words <= 2400):
    print(f'FAIL mots = {n_words} hors 1700-2400'); ok = False
else:
    print(f'PASS mots = {n_words}')

def strip_parens(s):
    prev = None
    while prev != s:
        prev = s
        s = re.sub(r'\([^()]*\)', ' ', s)
    return s

hors_parens = strip_parens(FULL)
AR_RE = re.compile(r'[\u0600-\u06FF\u0750-\u077F]')
hors_np = hors_parens
for v in vocabulaire:
    hors_np = hors_np.replace(json.dumps(v['ar'], ensure_ascii=False), '""')
hors_np = re.sub(r'"[a-zA-Z]+": ', '"K": ', hors_np)
m_ar2 = AR_RE.findall(hors_np)
if m_ar2:
    print(f'FAIL arabe hors parenthèses : {len(m_ar2)}')
    mt = re.search(r'.{40}[\u0600-\u06FF]+.{20}', hors_np)
    if mt: print('   ', mt.group(0)[:100])
    ok = False
else:
    print('PASS arabe entre parenthèses seulement')

if "'" in hors_np:
    print('FAIL apostrophe droite dans le texte FR'); ok = False
else:
    print('PASS apostrophes typographiques')
n_o, n_f = FULL.count('«'), FULL.count('»')
n_O, n_F = FULL.count('“'), FULL.count('”')
if n_o == n_f and n_O == n_F:
    print(f'PASS guillemets appariés (« {n_o}/{n_f} · “ {n_O}/{n_F} »)')
else:
    print(f'FAIL guillemets (« {n_o} vs » {n_f} · “ {n_O} vs ” {n_F} )'); ok = False

bad = []
for pat, lbl in [(r' [;:!?»]', 'esp avant'), (r'« ', 'esp après')]:
    for mt in re.finditer(pat, hors_np):
        frag = hors_np[max(0, mt.start()-30):mt.end()+15]
        if re.search(r'"(K|fr|ar|translit|resume|explication|points|auteur|avertissement|vocabulaire)"', frag):
            continue
        bad.append((lbl, frag))
if bad:
    print(f'FAIL espaces fines : {len(bad)}'); ok = False
    for lbl, frag in bad[:8]:
        print('   ', lbl, '…', repr(frag.replace('\n', '¶')))
else:
    print('PASS espaces fines (U+202F avant ;:!?\u202f» et après «)')

# citations vérifiées sur le texte HORS parenthèses
FULL_HP = strip_parens(FULL)
frags = re.findall(r'«([^«»]+)»', FULL_HP) + re.findall(r'“([^“”]+)”', FULL_HP)
manq = [f for f in frags if f.strip() not in CORPUS]
if manq:
    print(f'FAIL citations verbatim : {len(manq)}/{len(frags)} manquantes')
    for f in manq[:10]:
        print('   MISSING:', f[:120])
    ok = False
else:
    print(f'PASS citations verbatim : {len(frags)}/{len(frags)}')

HAR = re.compile(r'[\u064B-\u0652\u0670\u0640]')
if len(vocabulaire) != 8:
    print(f'FAIL vocab = {len(vocabulaire)} ≠ 8'); ok = False
else:
    print('PASS vocab = 8')
har_hit = [v['ar'] for v in vocabulaire if HAR.search(v['ar'])]
if har_hit:
    print(f'FAIL harakat : {har_hit}'); ok = False
else:
    print('PASS vocab ar sans harakat')

rec = [
    ('titre L29', T29, T29),
    ('kubrā (L29)', 'al-Sunan al-kubrā', S29),
    ('Mustadrak (L29)', 'al-Mustadrak ’alā ṣ-ṣaḥīḥayn', S29),
    ('Ibn Māǧa (L29)', 'Les Sunan d’Ibn Māǧa', S29),
    ('Warš (L29)', 'selon la lecture de Warš d’après Nāfi’', S29),
    ('39 ouvrages (L29)', 'les trente-neuf ouvrages mobilisés par les auteurs du manuel', S29),
    ('Zarqānī (L29)', 'Šarḥ az-Zarqānī ’alā Muwaṭṭa’ al-imām Mālik', S29),
    ('Šu’ab (L29)', 'Šu’ab al-’īmān', S29),
    ('Šu’ab al-Īmān (L1)', '[Šu’ab al-Īmān d’al-Bayhaqī]', S1),
    ('Mu’ǧam kabīr (L2)', '[al-Mu’ǧam al-kabīr d’aṭ-Ṭabarānī]', S2),
    ('Fatḥ al-Bārī (L3)', '[Fatḥ al-Bārī – Taḥrīr al-matn – al-Musnad de l’imam Aḥmad]', S3),
    ('Ikmāl ikmām (L4)', 'Ikmāl ikmām al-mu’allim', S4),
    ('Ibn Abī Šayba (L6, NB)', '[Musnad d’Ibn Abī Šayba]', S6),
    ('al-I’tiṣām (L9, NB)', '[al-I’tiṣām]', S9),
    ('Ǧāmi’ al-’Ulūm (L9)', 'Ǧāmi’ al-’Ulūm wa-l-Ḥikam', S9),
    ('Bayhaqī kubrā (L10)', '[Sunan al-Bayhaqī al-kubrā]', S10),
    ('Ǧāmi’ al-’ulūm (L10)', '[Ǧāmi’ al-’ulūm wa-l-ḥikam]', S10),
    ('voie blanche (L16)', 'Je vous ai laissés sur la voie blanche', S16),
    ('Ibn Māǧa (L16)', '[Sunan d’Ibn Māǧa]', S16),
    ('Ibn Baṭṭāl (L16)', '[Šarḥ Ṣaḥīḥ al-Buḫārī d’Ibn Baṭṭāl, adapté]', S16),
    ('Ibn Māǧa (L22)', '[Sunan d’Ibn Māǧa]', S22),
    ('Muwaṭṭa’ (L23)', '[Muwaṭṭa’]', S23),
    ('vertus (L23)', 'Je n’ai été envoyé que pour parfaire les vertus', S23),
    ('Buḫārī (L25)', '[Ṣaḥīḥ d’al-Buḫārī]', S25),
    ('Tirmiḏī (L25)', '[Sunan d’at-Tirmiḏī]', S25),
    ('Mustadrak (L25)', '[al-Mustadrak d’al-Ḥākim]', S25),
    ('Muslim (L26)', '[Ṣaḥīḥ de Muslim]', S26),
    ('Muwaṭṭa’ (L26)', '[al-Muwaṭṭa’]', S26),
    ('Muslim (L27)', '[Ṣaḥīḥ de Muslim]', S27),
    ('Muwaṭṭa’ (L27)', '[al-Muwaṭṭa’]', S27),
    ('Musnad Aḥmad (L27)', '[Musnad de l’imam Aḥmad]', S27),
    ('Futūḥāt (L27)', '[al-Futūḥāt al-wahbiyya d’aš-Šubraḫītī, avec le choix d’une autre narration du hadith, différant quelque peu]', S27),
    ('aš-Šubraḫītī (L27)', 'Aš-Šubraḫītī — que Dieu lui fasse miséricorde', S27),
    ('œuvre de nul (L27)', 'L’œuvre de nul d’entre vous ne le sauvera', S27),
    ('An-Nawawī (L27)', 'An-Nawawī — que Dieu lui fasse miséricorde', S27),
    ('formule manuel (L27)', 'Le hadith tiré du livre des Arba’ūn nawawiyya de l’imam al-Nawawī, avec le commentaire d’Ibn Daqīq al-’Īd', S27),
    ('Bayhaqī (L28)', '[Sunan d’al-Bayhaqī]', S28),
    ('Mustadrak (L28)', '[al-Mustadrak d’al-Ḥākim]', S28),
]
for lbl, frag, src in rec:
    if frag in src:
        print(f'PASS recoupement : {lbl}')
    else:
        print(f'FAIL recoupement : {lbl} — introuvable'); ok = False

if 'pdf-29' in comms['commentaires']:
    print('FAIL pdf-29 déjà présent — abandon (pas d’écrasement)'); ok = False

if not ok:
    sys.exit(1)

# ============================ POSE ============================
trié = {}
for k in sorted(comms['commentaires'].keys(), key=lambda x: int(x.replace('pdf-', ''))):
    trié[k] = comms['commentaires'][k]
trié['pdf-29'] = entree
comms['commentaires'] = trié
out = json.dumps(comms, ensure_ascii=False, indent=2) + '\n'
(DEPOT / 'content/commentaires/hadith-5ep.json').write_text(out, encoding='utf-8')
print(f'\nPOSE OK : pdf-29 → content/commentaires/hadith-5ep.json ({n_words} mots, {len(FULL)} car JSON)')
print('NB consigné : aucun NB de verset cette vague — aucune référence coranique dans la leçon 29 ; '
      'l’unique entrée coranique est le muṣḥaf lui-même (précédent R761)')
print('NB consigné : quelques étiquettes de la traduction sans entrée dans la لائحة '
      '([Musnad d’Ibn Abī Šayba] L6, [al-I’tiṣām] L9) et formes variables (Ikmāl ikmām/ikmāl, '
      'Šu’ab al-Īmān/al-’īmān, as-Siǧistānī/as-Suǧistānī) — consignées, non corrigées')

# -*- coding: utf-8 -*-
"""R766 — pose du commentaire pdf-28 (leçon 28, دعم وتطبيق — Consolidation et
application, quatrième consolidation, dernière leçon d'enseignement) dans
content/commentaires/hadith-5ep.json.
Spans ARABES : tirés du corpus (verbatim par construction) ; translit : écrit à
la convention ʾ/ʿ (U+02BE/U+02BF) du corpus ; fragments FR « » hardcodés puis
vérifiés verbatim contre les leçons pdf-28/pdf-16/pdf-21/pdf-22/pdf-23/pdf-25/
pdf-26/pdf-27/pdf-29 (corpus élargi).
Gardes : fenêtre 1700-2400 mots (resume+explication+points), typographie FR
(’ « » U+202F), zéro arabe hors parenthèses, vocab 8 sans harakat, recoupements.
Abort si un garde échoue. AUCUNE modification de content/books (zone d'un autre
ouvrier) — le NB de lecture (al-ʾAnbiyāʾ 106 → porteur 107) est consigné ici et
dans le worklog."""
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
S28 = L['pdf-28']
S16, S21, S22, S23, S25, S26, S27, S29 = (L['pdf-16'], L['pdf-21'], L['pdf-22'],
    L['pdf-23'], L['pdf-25'], L['pdf-26'], L['pdf-27'], L['pdf-29'])
T29 = [l['titleFr'] for l in books['lessons'] if l['docId'] == 'pdf-29'][0]
CORPUS = '\n'.join([S28, S16, S21, S22, S23, S25, S26, S27, S29, T29])

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

# ---- citations « » tirées du corpus (verbatim par construction)
Q_MAKARIM = pull(S28, '«' + NB + 'Je n’ai été envoyé que pour parfaire les nobles caractères', 'caractères' + NB + '»')
Q_BAYDA   = pull(S28, '«' + NB + 'Je vous ai laissés sur la voie blanche', 'le perdu' + NB + '»')
Q_RAHMA   = pull(S28, '«' + NB + 'Et Nous ne t’avons envoyé qu’en miséricorde pour les mondes', 'mondes' + NB + '»')
Q_PARFAIRE = chk('«' + NB + 'pour parfaire' + NB + '»', S28, 'pour parfaire')
Q23_VERTUS = FR(chk('Je n’ai été envoyé que pour parfaire les vertus', S23, 'variante vertus L23'))
Q21_LAGH = FR(chk('Ne te mets pas en colère', S21, 'lā taġḍab L21'))
Q22_IHSAN = FR(chk('Dieu Très-Haut a prescrit l’excellence en toute chose', S22, 'iḥsān L22'))

# ---- spans arabes tirés du corpus (verbatim par construction)
AR_TITLE  = chk('دَعْمٌ وَتَطْبِيقٌ', S28, 'titre')
AR_AHD    = chk('أَهْدَافُ الدَّرْسِ', S28, 'objectifs')
AR_OBJ1   = chk('أَنْ أُقَوِّمَ مُكْتَسَبَاتِي الْمَعْرِفِيَّةَ فِي الدُّرُوسِ السَّابِقَةِ', S28, 'obj1')
AR_OBJ2   = chk('أَنْ أَذْكُرَ قُدُرَاتِي فِي الِاسْتِيعَابِ وَالْفَهْمِ وَالتَّحْلِيلِ', S28, 'obj2')
AR_OBJ3   = chk('أَنْ أَعْمَلَ عَلَى تَطْبِيقِ ذَلِكَ مِنْ خِلَالِ وَضْعِيَّاتٍ جَدِيدَةٍ', S28, 'obj3')
AR_AQIDA  = chk('عَقِيدَةً وَعِبَادَةً', S28, 'aqīda/ʿibāda')
AR_MAKARIM = chk('إِنَّمَا بُعِثْتُ لِأُتَمِّمَ مَكَارِمَ الْأَخْلَاقِ', S28, 'makārim')
AR_ATHMAR = chk('أَثْمَرَ ذَلِكَ اسْتِقَامَةَ أَخْلَاقِهِ', S28, 'aṯmara')
AR_GHADAB = chk('الْغَضَبُ لِغَيْرِ اللهِ عَزَّ وَجَلَّ', S28, 'ġaḍab')
AR_HAYA_TXT = chk('الْحَيَاءِ الْمَشْرُوعِ', S28, 'ḥayāʾ (texte)')
AR_MASALIK = chk('فِي مَسَالِكِ الْمُحْسِنِينَ', S28, 'masālik')
AR_BAYDA_AR = chk('قَدْ تَرَكْتُكُمْ عَلَى الْبَيْضَاءِ، لَيْلُهَا كَنَهَارِهَا، لَا يَزِيغُ عَنْهَا بَعْدِي إِلَّا هَالِكٌ', S28, 'bayḍāʾ')
AR_MUHSINUN = chk('الْمُحْسِنُونَ', S28, 'muḥsinūn')
AR_HAYA_FHM = chk('الْحَيَاءُ الْمَشْرُوعُ', S28, 'ḥayāʾ (fahm)')
AR_MAHAJJA = chk('الْمَحَجَّةُ الْبَيْضَاءُ', S28, 'maḥajja')
AR_MADHMUM = chk('الْغَضَبُ الْمَذْمُومُ', S28, 'ġaḍab maḏmūm')
AR_MUNHARIF = chk('سُلُوكٌ مُنْحَرِفٌ', S28, 'sulūk munḥarif')
AR_NUSUS  = chk('بِنُصُوصٍ شَرْعِيَّةٍ', S28, 'nuṣūṣ')
AR_LIUTM  = chk('لِأُتَمِّمَ', S28, 'li-ʾutammima')
AR_UWAẒ   = chk('أُوَظِّفُ مُكْتَسَبَاتِي لِلْإِجَابَةِ عَمَّا يَأْتِي', S28, 'uwaẓẓif')
AR_ASUGH  = chk('أَصُوغُ تَوْجِيهَاتٍ لِحِمَايَةِ حُقُوقِ الْأَطْفَالِ', S28, 'aṣūġ')
AR_UQADDIM = chk('أُقَدِّمُ ثَلَاثَ نَصَائِحَ لِلتَّخَلُّقِ بِخُلُقِ الْإِحْسَانِ فِيْمَا يَأْتِي', S28, 'uqaddim')
AR_MUAMALA = chk('فِي مُعَامَلَةِ الْأَوْلَادِ لِآبَائِهِمْ وَأُمَّهَاتِهِمْ', S28, 'muʿāmala')
AR_ALAQAT  = chk('فِي عَلَاقَةِ الْفَرْدِ بِمُجْتَمَعِهِ', S28, 'ʿalāqa')
AR_DUAT    = chk('الرُّسُلَ دُعَاةً', S23, 'duʾāt L23')
AR_TAHALLI = chk('وَالتَّحَلِّي بِمَكَارِمِ الْأَخْلَاقِ', S23, 'taḥallī L23')
AR_NUBUWWA = chk('مِنْ كَلَامِ النُّبُوَّةِ الْأُولَى', S25, 'nubuwwa L25')

resume = (
    "Guide de lecture de la leçon 28 (Consolidation et application — "
    "daʿm wa-taṭbīq (دعم وتطبيق)) : la quatrième consolidation du manuel — après "
    "les leçons 7, 14 et 20, qui portaient le même titre — et la dernière leçon "
    "d’enseignement : aucun hadīth des Quarante n’y est installé — « leçon-bilan, "
    "elle conduit l’élève à mobiliser, dans des situations nouvelles, les acquis "
    "des leçons précédentes ». "
    "Trois objectifs de bilan : les acquis cognitifs, l’état des "
    "capacités « dans l’assimilation, la compréhension et l’analyse », la mise en "
    "application « à travers des situations nouvelles ». Le texte pose la thèse "
    "qui gouverne le bilan : « L’islam est venu éduquer l’homme, en sa croyance "
    "et en son culte », en vue de « la droiture de sa moralité et de sa conduite » "
    f"— preuve d’emblée\u202f: {Q_MAKARIM} [Sunan d’al-Bayhaqī]. La foi réalisée et les "
    "adorations saines « porte comme fruit la droiture de ses caractères » : "
    "retenu « de la colère pour autre qu’Allah, Puissant et Majestueux », paré "
    "« de la pudeur licite », élevé « dans les voies des bienfaiteurs », "
    "miséricorde « pour lui-même et pour tout ce qui existe dans l’univers », "
    "préservé « de la déviance intellectuelle et comportementale » ; l’envers — "
    "torts à autrui, non-respect « des droits des enfants » — « est le fruit "
    "d’une colère blâmable, ou d’un défaut de pudeur, ou d’une pensée et d’une "
    f"conduite déviantes et non droites », et le second hadīth scelle la page\u202f: "
    f"{Q_BAYDA} [al-Mustadrak d’al-Ḥākim]. La compréhension tourne cinq expressions "
    "et deux contraires et demande « dix mots qui indiquent les caractères "
    "positifs » ; l’analyse ouvre six chantiers — des prédécesseurs de « "
    "l’appel aux nobles caractères », le caractère « connu des nations "
    "antérieures », les fruits appuyés « de textes scripturaires », les effets "
    "sociaux, et le rapport entre la miséricorde [al-’Anbiyā’\u202f: 106] et "
    f"{Q_PARFAIRE} ; l’application demande « des orientations pour la protection "
    "des droits des enfants » et « trois conseils » de bienfaisance — envers les "
    "parents, dans la société."
)

explication = [
    # P1 — place : quatrième consolidation
    ("La leçon 28 est la quatrième consolidation du manuel : après les leçons 7, 14 "
     "et 20, elle porte de nouveau le titre de soutien et d’application "
     f"(daʿm wa-taṭbīq ({AR_TITLE})) — « leçon-bilan, elle conduit l’élève à "
     "mobiliser, dans des situations nouvelles, les acquis des leçons précédentes » "
     "— et elle ferme l’enseignement : « Dernière leçon d’enseignement du manuel, "
     "elle en précède immédiatement la liste des sources et références ». Aucun "
     "hadīth des Quarante n’y est installé ; son texte est une page de synthèse, "
     "consacrée à « l’éducation de l’homme par "
     "l’islam » — croyance, culte, moralité, conduite : les vingt-sept leçons "
     "condensées en une page."),
    # P2 — objectifs de bilan
    ("Les objectifs (" + AR_AHD + ") sont trois bilans, alignés sur le "
     "titre : « Que je fasse le bilan de mes acquis cognitifs des leçons "
     f"précédentes » ({AR_OBJ1}), « Que je fasse état de mes capacités dans "
     f"l’assimilation, la compréhension et l’analyse » ({AR_OBJ2}), « Que je mette "
     f"tout cela en application à travers des situations nouvelles » ({AR_OBJ3}) — "
     "évaluer, mesurer, appliquer : la grammaire des consolidations "
     "précédentes."),
    # P3 — le texte : la thèse + premier hadīth
    ("Le texte pose d’emblée la thèse : « L’islam est venu éduquer l’homme, en sa "
     f"croyance et en son culte » (ʾaqīdatan wa-ʾibādatan ({AR_AQIDA})), en vue de "
     "« la droiture de sa moralité et de sa conduite » — et l’appuie de la parole "
     "du Prophète — prière et salut d’Allah sur lui : "
     f"{Q_MAKARIM} ({AR_MAKARIM}) [Sunan d’al-Bayhaqî]."),
    # P4 — recoupement L23 : le hadīth déjà rencontré
    ("Le hadīth n’est pas nouveau dans le manuel : le tamhīd de la leçon 23 "
     f"l’installait déjà — Dieu « a envoyé les Messagers comme prédicateurs » ({AR_DUAT}) "
     "« à la parure des "
     f"nobles caractères » ({AR_TAHALLI}) — avec la variante {Q23_VERTUS} "
     "[Muwaṭṭa’]. La leçon 28 reprend la parole au bilan : « les nobles "
     "caractères » (makārim al-aḫlāq) contre « les vertus » (ṣāliḥ al-aḫlāq), et "
     "autre attribution — [Sunan d’al-Bayhaqī] — dont le recueil, al-Sunan "
     "al-kubrā, figure dans la liste des sources (leçon 29). Attributions "
     "consignées telles quelles : le commentaire ne corrige pas la "
     "leçon."),
    # P5 — la chaîne des causes et des fruits
    ("Vient la chaîne des causes et des fruits : « Et lorsque la foi de "
     "l’individu se réalise et que ses adorations deviennent saines, cela porte "
     f"comme fruit la droiture de ses caractères » ({AR_ATHMAR}). Quatre fruits "
     "s’égrènent : « cela le retient de la colère pour autre qu’Allah, Puissant "
     f"et Majestueux » ; il se pare « de la pudeur licite » ({AR_HAYA_TXT}) ; "
     f"« il progresse et s’élève dans les voies des bienfaiteurs » ({AR_MASALIK}), "
     "« dans ses adorations comme dans ses transactions » ; il « est ainsi, de ce "
     "fait, miséricorde pour lui-même et pour tout ce qui existe dans "
     "l’univers ». Et la clôture scelle la chaîne : « préservé de la déviance "
     "intellectuelle et comportementale, et de toute obliquité en cela »."),
    # P6 — chaque fruit nomme une leçon (21, 25, 22, 26)
    ("Chaque fruit nomme une leçon. La colère retenue — la leçon 21, « "
     f"L’interdiction de la colère »\u202f: {Q21_LAGH} (lā taġḍab), l’interdiction de "
     "laisser s’exécuter la colère. La pudeur licite — la leçon 25, « La pudeur "
     "fait partie de la foi ». Les voies des bienfaiteurs — la leçon 22, "
     f"l’excellence (iḥsān) en toute chose\u202f: {Q22_IHSAN}. La droiture des "
     "caractères — la leçon 26 et son « équilibre dans l’obéissance à Dieu ». "
     "La synthèse tisse les leçons 21-26 "
     "en une seule chaîne de causes : chaque fruit du texte est le fruit d’une "
     "leçon étudiée."),
    # P7 — l'envers + second hadīth
    ("L’envers de la chaîne n’est pas oublié : « Quant à ce qui peut survenir, en "
     "revanche, de comportements mauvais, de torts causés à autrui et de "
     "non-respect des droits des enfants, c’est le fruit d’une colère blâmable, "
     "ou d’un défaut de pudeur, ou d’une pensée et d’une conduite déviantes et "
     "non droites » — le diagnostic à trois branches, miroir exact des trois "
     f"fruits. Et le second hadīth scelle la page\u202f: {Q_BAYDA} ({AR_BAYDA_AR}) "
     "[al-Mustadrak d’al-Ḥākim] — la voie unique, sa clarté continue, et le seul "
     "risque : le détournement après lui."),
    # P8 — recoupement L16 : la voie blanche déjà citée
    ("Cette parole aussi est un déjà-vu : la leçon 16 — la circonspection envers "
     "le douteux — la citait déjà, avec l’attribution [Sunan d’Ibn Māǧa] et la "
     "variante « sa nuit en est comme le jour » ; la leçon 28 la reprend avec "
     "[al-Mustadrak d’al-Ḥākim] et « sa nuit est comme son jour ». Deux recueils, "
     "deux éditions de la même parole — le manuel n’arbitre pas, et la liste des "
     "sources (leçon 29) nomme les deux\u202f: Les Sunan d’Ibn Māǧa, al-Mustadrak "
     f"ʾalā ṣ-ṣaḥīḥayn. La compréhension fera tourner « la voie blanche "
     f"éclatante » ({AR_MAHAJJA})."),
    # P9 — la compréhension
    ("La compréhension tourne les mots de la synthèse : cinq expressions à "
     "expliquer — « la droiture de ses caractères », les bienfaiteurs "
     f"({AR_MUHSINUN}), « la colère pour autre qu’Allah, Puissant et Majestueux » "
     f"({AR_GHADAB}), « la pudeur licite » ({AR_HAYA_FHM}), « la voie blanche "
     "éclatante » ; puis deux contraires demandés — la colère blâmable "
     f"({AR_MADHMUM}) et une conduite déviante ({AR_MUNHARIF}) — et l’extraction "
     "de « dix mots qui indiquent les caractères positifs » : lire la synthèse "
     "comme un catalogue."),
    # P10 — l'analyse : les questions d'histoire
    ("L’analyse ouvre sur une observation philologique : « Il ressort de sa "
     f"parole — prière et salut d’Allah sur lui — {Q_PARFAIRE} qu’il a existé des "
     "hommes qui inaugurèrent l’appel aux nobles caractères avant lui » "
     f"({AR_LIUTM}) — le sens exclusif de « que pour » suppose un précédent : on "
     "ne parfait que ce qui a commencé. D’où deux questions d’histoire : « Qui "
     "sont ceux qui appelèrent aux nobles caractères avant lui » — le tamhīd de "
     "la leçon 23 répond : les Messagers, « prédicateurs » envoyés « à la parure "
     "des nobles caractères » ; « Et quel est ce caractère dont tu as étudié "
     "qu’il fut connu des nations antérieures » — la leçon 25 a déjà répondu : "
     "la pudeur, « parmi les paroles de la prophétie première que les hommes ont "
     f"retenues » ({AR_NUBUWWA}), ce que la leçon 25 nommait « les législations "
     "des prophètes antérieurs »."),
    # P11 — l'analyse : fruits scripturaires, société, la liaison + NB
    ("Deux chantiers suivent : « J’extrais du texte les fruits du bon caractère, "
     f"et je les appuie de textes scripturaires » ({AR_NUSUS}) — au fruit, son "
     "verset ou son hadīth, le geste même du commentaire ; « Je détermine les "
     "effets positifs que la pudeur, la droiture et l’absence de colère laissent "
     "dans la société » — du caractère aux effets collectifs. Et la "
     "question de liaison met en regard les deux paroles : « Et Nous ne t’avons "
     "envoyé qu’en miséricorde pour les mondes » [al-’Anbiyā’\u202f: 106] et « Je "
     "n’ai été envoyé que pour parfaire les nobles caractères » — même "
     "construction, deux plans : le dessein établi par Dieu "
     "— la miséricorde —, le moyen par lequel il passe — les caractères. NB de "
     "lecture : la référence imprimée porte le verset 106 ; le verset qui porte "
     "ces paroles est le 107 de la sourate al-ʾAnbiyāʾ (vérifié web) — le même "
     "décalage systématique que les vagues précédentes."),
    # P12 — l'application
    ("L’application ferme la leçon : « Je mobilise mes acquis pour répondre à ce "
     f"qui suit » ({AR_UWAẒ}) — deux chantiers de production. D’abord : « Je "
     f"formule des orientations pour la protection des droits des enfants » "
     f"({AR_ASUGH}) — la question qui traversait le texte devient une tâche "
     "d’élève : "
     "passer du diagnostic à la proposition. Ensuite : « J’offre trois conseils "
     f"pour se parer du caractère de la bienfaisance » ({AR_UQADDIM}) dans deux "
     f"situations : « dans la manière dont les enfants traitent leurs pères et "
     f"leurs mères » ({AR_MUAMALA}) et « dans la relation de l’individu avec sa "
     f"société » ({AR_ALAQAT}) — l’excellence de la leçon 22 descend du principe "
     "au cas concret : la famille d’abord, la société ensuite."),
    # P13 — boucles + clôture
    ("Les boucles : l’iʿdād de la leçon 27 enjoignait « Je lis le texte de la "
     "consolidation et de l’application, et je réponds aux questions » — la "
     "leçon 28 la tient mot à mot : elle se lit et se répond. Et elle s’achève "
     "sans préparation : pas d’iʿdād après l’application — le manuel s’achève — "
     "la leçon 29, « Liste des sources et références », n’attend aucun hadīth "
     "nouveau : « les trente-neuf ouvrages mobilisés par les auteurs du manuel », "
     "le Noble Coran « selon la lecture de Warš d’après Nāfi’ » en tête, puis les "
     "recueils que cette page a cités — al-Sunan al-kubrā d’al-Bayhaqī, "
     "al-Mustadrak ʾalā ṣ-ṣaḥīḥayn d’al-Ḥākim — l’annexe inventorie les preuves "
     "que le bilan a reçues."),
]

points = [
    ("La place : quatrième consolidation du manuel — les leçons 7, 14, 20 puis 28 "
     "portent le même titre (daʿm wa-taṭbīq) ; aucun hadīth des Quarante ; trois "
     "objectifs de bilan ; « Dernière leçon d’enseignement du manuel » avant la "
     "liste des sources et références (leçon 29)."),
    ("La continuité : l’iʿdād de la leçon 27 — « Je lis le texte de la "
     "consolidation et de l’application, et je réponds aux questions » — est "
     "tenue ; la leçon s’achève sans iʿdād : le manuel s’achève."),
    ("La thèse : « L’islam est venu éduquer l’homme, en sa croyance et en son "
     "culte », en vue de « la droiture de sa moralité et de sa conduite » ; "
     "preuve : « Je n’ai été envoyé que pour parfaire les nobles caractères » "
     "[Sunan d’al-Bayhaqī]."),
    ("La chaîne des fruits : foi réalisée et adorations saines → « la droiture de "
     "ses caractères » ; quatre fruits : la colère pour autre qu’Allah retenue, "
     "la pudeur licite, les voies des bienfaiteurs — adorations et transactions —, "
     "la miséricorde pour soi et pour l’univers ; clôture : préservé « de la "
     "déviance intellectuelle et comportementale, et de toute obliquité en cela »."),
    ("L’envers : torts à autrui et « non-respect des droits des enfants » = fruit "
     "« d’une colère blâmable, ou d’un défaut de pudeur, ou d’une pensée et "
     "d’une conduite déviantes et non droites » ; preuve : « Je vous ai laissés "
     "sur la voie blanche » [al-Mustadrak d’al-Ḥākim] — « sa nuit est comme son "
     "jour », « ne s’en détourne après moi que le perdu »."),
    ("Les déjà-vus : les nobles caractères déjà au tamhīd de la leçon 23 (« les "
     "vertus », [Muwaṭṭa’]) ; la voie blanche déjà à la leçon 16 ([Sunan d’Ibn "
     "Māǧa], « sa nuit en est comme le jour ») — attributions et variantes "
     "consignées sans correction ; les deux recueils figurent dans la liste des "
     "sources (leçon 29)."),
    ("Les chantiers d’analyse : « pour parfaire » → des prédécesseurs — les "
     "Messagers, « prédicateurs » « à la parure des nobles caractères » (tamhīd "
     "de la leçon 23) ; le caractère « connu des nations antérieures » → la "
     "pudeur, « prophétie première » (leçon 25) ; fruits appuyés « de textes "
     "scripturaires » ; effets sociaux ; rapport entre « Et Nous ne t’avons "
     "envoyé qu’en miséricorde pour les mondes » [al-’Anbiyā’\u202f: 106] et "
     "« pour parfaire » — NB de lecture : porteur 107 (vérifié web)."),
    ("L’application : « des orientations pour la protection des droits des "
     "enfants » ; « trois conseils » de bienfaisance — « dans la manière dont "
     "les enfants traitent leurs pères et leurs mères », « dans la relation de "
     "l’individu avec sa société » — l’excellence de la leçon 22 au cas concret."),
]

vocabulaire = [
    {"ar": "دعم وتطبيق", "translit": "daʿm wa-taṭbīq",
     "fr": "le soutien et l’application — le titre des quatre consolidations du "
           "manuel (leçons 7, 14, 20 et 28) : soutenir les acquis et les appliquer "
           "dans des situations nouvelles."},
    {"ar": "مكارم الاخلاق", "translit": "makārim al-aḫlāq",
     "fr": "les nobles caractères — « Je n’ai été envoyé que pour parfaire les "
           "nobles caractères » [Sunan d’al-Bayhaqī] : la preuve de la thèse ; "
           "variante « les vertus » au tamhīd de la leçon 23 [Muwaṭṭa’]."},
    {"ar": "المحجة البيضاء", "translit": "al-maḥajja al-bayḍāʾ",
     "fr": "la voie blanche éclatante — « sa nuit est comme son jour » ; « ne "
           "s’en détourne après moi que le perdu » [al-Mustadrak d’al-Ḥākim] ; "
           "déjà citée leçon 16 [Sunan d’Ibn Māǧa]."},
    {"ar": "الحياء المشروع", "translit": "al-ḥayāʾ al-mašrūʿ",
     "fr": "la pudeur licite — l’un des fruits de la foi réalisée ; le fruit de "
           "la leçon 25, où elle appartenait à la foi elle-même."},
    {"ar": "الغضب المذموم", "translit": "al-ġaḍab al-maḏmūm",
     "fr": "la colère blâmable — le premier contraire demandé par la compréhension ; "
           "le fruit des comportements mauvais, en miroir de la leçon 21."},
    {"ar": "حقوق الاطفال", "translit": "ḥuqūq al-ʾaṭfāl",
     "fr": "les droits des enfants — leur non-respect parmi les fruits de la "
           "déviance ; l’application en demande la protection : « des orientations »."},
    {"ar": "مسالك المحسنين", "translit": "masālik al-muḥsinīn",
     "fr": "les voies des bienfaiteurs — en adorations comme en transactions ; le "
           "fruit de la leçon 22, l’excellence (iḥsān) en toute chose."},
    {"ar": "استقامة اخلاقه", "translit": "istiqāmatu ʾaḫlāqih",
     "fr": "la droiture de ses caractères — ce que « porte comme fruit » la foi "
           "réalisée et les adorations saines ; l’écho de la leçon 26 dans la "
           "synthèse du bilan."},
]

avertissement = ("Ce commentaire est un guide de lecture du manuel ; en cas de "
                 "divergence d’expression, le manuel et sa traduction savante font foi.")

entree = {"auteur": "IA-1, tour R766",
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
    ('variante vertus (L23)', 'Je n’ai été envoyé que pour parfaire les vertus', S23),
    ('Muwaṭṭa’ (L23)', '[Muwaṭṭa’]', S23),
    ('Messagers prédicateurs (L23)', 'a envoyé les Messagers comme prédicateurs', S23),
    ('parure des nobles caractères (L23)', 'à la parure des nobles caractères', S23),
    ('prophétie première (L25)', 'parmi les paroles de la prophétie première que les hommes ont retenues', S25),
    ('prophètes antérieurs (L25)', 'les législations des prophètes antérieurs', S25),
    ('voie blanche (L16)', 'Je vous ai laissés sur la voie blanche', S16),
    ('Sunan d’Ibn Māǧa (L16)', 'Sunan d’Ibn Māǧa', S16),
    ('variante nuit L16', 'sa nuit en est comme le jour', S16),
    ('colère (L21)', 'Ne te mets pas en colère', S21),
    ('excellence (L22)', 'Dieu Très-Haut a prescrit l’excellence en toute chose', S22),
    ('équilibre (L26)', 'équilibre dans l’obéissance à Dieu', S26),
    ('iʿdād L27 → consolidation', 'Je lis le texte de la consolidation et de l’application, et je réponds aux questions', S27),
    ('Sunan kubrā (L29)', 'al-Sunan al-kubrā', S29),
    ('Mustadrak (L29)', 'al-Mustadrak ’alā ṣ-ṣaḥīḥayn', S29),
    ('Ibn Māǧa (L29)', 'Les Sunan d’Ibn Māǧa', S29),
    ('Warš (L29)', 'selon la lecture de Warš d’après Nāfi’', S29),
    ('39 ouvrages (L29)', 'les trente-neuf ouvrages mobilisés par les auteurs du manuel', S29),
    ('titre L29', T29, T29),
]
for lbl, frag, src in rec:
    if frag in src:
        print(f'PASS recoupement : {lbl}')
    else:
        print(f'FAIL recoupement : {lbl} — introuvable'); ok = False

if 'pdf-28' in comms['commentaires']:
    print('FAIL pdf-28 déjà présent — abandon (pas d’écrasement)'); ok = False

if not ok:
    sys.exit(1)

# ============================ POSE ============================
trié = {}
for k in sorted(comms['commentaires'].keys(), key=lambda x: int(x.replace('pdf-', ''))):
    trié[k] = comms['commentaires'][k]
trié['pdf-28'] = entree
comms['commentaires'] = trié
out = json.dumps(comms, ensure_ascii=False, indent=2) + '\n'
(DEPOT / 'content/commentaires/hadith-5ep.json').write_text(out, encoding='utf-8')
print(f'\nPOSE OK : pdf-28 → content/commentaires/hadith-5ep.json ({n_words} mots, {len(FULL)} car JSON)')
print('NB consigné : al-’Anbiyā’ imprimé 106 → porteur 107 (vérifié web) — '
      'même décalage systématique que pdf-24 (Ġāfir 13→14, Fuṣṣilat 29→30)')

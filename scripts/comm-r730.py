#!/usr/bin/env python3
"""R730 — ajoute le commentaire pédagogique de la leçon 3 (pdf-mut23h2x-392,
تطيب المحرم — l'usage du parfum avant la consécration) à
content/commentaires/hadith-3es.json.
Vague 14 (première livraison) : remontée hadith-3es (le SUIVANT de R729-b,
slot précisé). Même protocole que comm-r729.py : normalisation de la
ponctuation FR (U+202F avant ; : ! ? » et après «, apostrophe courbée) sur
l'entrée nouvelle seulement — opération idempotente. Rédaction d'après la
lecture complète de la leçon (htmlFr intégral, 41 329 caractères, extraction
non lossy). Les numéros du Muwaṭṭaʾ et les formules sont cités tels qu'ils
figurent dans la leçon (règle 2 de LISEZ-MOI.md : aucune invention). Les
formes arabes du vocabulaire sont posées au squelette standard SANS harakat
(situation des vagues 5-13 : les gloses de ces leçons sont rendues en
translittération dans la couche FR) ; aucune harakat n'est inventée (règle 2).
Les ʿ et ʾ (U+02BF / U+02BE) sont posés directement dans les champs FR pour
les noms propres et les fragments de translittération — la normalisation ne
les touche pas."""
import json, re

CHEMIN = 'content/commentaires/hadith-3es.json'

E_392 = {
    "auteur": "IA-1, tour R730",
    "resume": "Guide de lecture de la leçon 3 (تطيب المحرم) : le parfum n'est pas suspect en lui-même — il faisait partie des choses aimées du Messager de Dieu (que la prière et la paix soient sur lui), et la mère des croyants ʿĀʾicha le parfumait à son état libre ; c'est l'état de consécration qui en déplace le statut. La leçon organise le statut du taṣyīb du corps en trois fenêtres : permis — et recommandé — avant l'iḥrām, interdit pendant la consécration, redevenu permis après le lancer de la jamrat al-ʿAqaba (avec la réserve de détestabilité de Mālik avant l'ifāḍa). Le vêtement est traité en deux cas : la non-recommandation d'unanimité de parfumer les habits au moment de l'intention d'iḥrām, puis la distinction capitale entre la senteur — qui s'enfuit et l'interdit avec elle — et la teinture de safran ou de wars, qui demeure visible et prolonge l'interdit même quand l'odeur n'est plus. Le pivot herméneutique est le taʾwīl du hadith de ʿĀʾicha, établi par la conduite dʿUmar et appuyé par la riwāya de Muslim. La clôture spirituelle (khulāṣa) donne la finalité de l'interdiction — quitter le taraffuh et recueiller le cœur devant la Présence — et l'exploitation règle le cas de la nourriture au safran : ce que le feu a touché ne nuit pas au muḥrim, ce que le feu n'a pas touché ne se mange pas.",
    "explication": [
        "La page d'ouverture (p.25) pose trois objectifs : connaître le statut juridique du taṣyīb du muḥrim pour son corps et pour son vêtement, distinguer les situations dans lesquelles le parfum est permis de celles dans lesquelles il ne l'est pas, et saisir la finalité (maqṣūd) que la Loi poursuit en interdisant au consacré le parfum parmi les choses aimées. Le tamhīd pose le décor avant les textes : le parfum faisait partie des choses aimées du Messager de Dieu, et ʿĀʾicha le parfumait à son état libre — le parfum n'est donc pas en lui-même suspect, c'est l'état de consécration qui en change le statut, et la leçon va précisément délimiter où s'arrête le permis et où commence l'interdit. Les trois questions d'ouverture ordonnent la leçon entière : le statut du taṣyīb du muḥrim pour son corps et son vêtement, les règles qui en découlent, la finalité de l'interdiction — et le bloc de synthèse (istikhlāṣ al-muḍmīn) la ramasse en deux items : le statut du taṣyīb du corps et du vêtement, puis le cas particulier de la nourriture qui contient du parfum.",
        "Les textes du corps arment chaque fenêtre. Le n° 923 est la matrice : ʿĀʾicha dit « j'avais coutume de parfumer le Messager de Dieu pour son iḥrām avant qu'il ne se consacre, et pour son ḥall avant qu'il ne se rase » — deux moments symétriques qui ouvrent la fenêtre d'avant la consécration et la fenêtre d'après la jamra. Le n° 925 est l'interdit du dedans : ʿUmar sent le parfum sur Muʿāwiya encore odorant à ash-Shajara et lui ordonne « j'ai pris la résolution que tu retourneras vers elle et que tu la laveras » — preuve que le taṣyīb ne convient pas au muḥrim et que le parfum reçu avant l'iḥrām doit au besoin être enlevé. Le n° 928 donne la matière licite et le temps licite : rien ne reproche de se huiler d'une huile sans parfum, et de se consacrer après le lancer de la jamra avant de verser (qayḍ) de Minā. Le n° 927 introduit la divergence qui armera la troisième fenêtre : al-Walīd b. ʿAbd al-Malik interroge Sālim et Khārija sur le parfum après le lancer et le rasage, avant l'ifāḍa — Sālim l'interdit (par détestabilité), Khārija le permet.",
        "Le vêtement repose sur le n° 924 : l'homme du désert venu interroger le Messager de Dieu sur sa 'umra portait une chemise marquée d'une trace de jaune (ṣufr) — le safran, selon la gloss — et l'ordre prophétique est triple : « enlève ta chemise, lave cette couleur jaune de toi, et fais dans ta 'umra ce que tu fais dans ton ḥajj ». Le manuel en tire d'abord la règle générale — il n'est pas recommandé, d'unanimité, de parfumer les vêtements au moment de l'intention d'iḥrām — puis la règle de l'oubli : celui que le parfum atteint par oubli ou par ignorance, puis qui apprend et se hâte de l'enlever, n'encourt pas d'expiation ; Mālik ajoute : si cela tarde sur lui, le lavage devient obligatoire — la leçon enseigne une conduite, pas seulement un statut. Le n° 914 clôt le cas : le vêtement que le parfum a touché mais dont la senteur s'est enfuie supporte l'iḥrām — tant qu'il n'y a pas dedans de teinture (ṣibāgh) de safran ou de wars ; la distinction tient tout : la senteur disparaît et l'interdit avec elle, la teinture demeure visible et prolonge l'interdit même quand l'odeur n'est plus.",
        "La scène de la charrah (n° 926) montre l'application concrète de la première fenêtre : Kathīr b. aṣ-Ṣalt avait mis de la teinte sur sa tête (labītu raʾsī) pour rassembler le cheveu — il s'apprêtait à se raser et à entrer en iḥrām — et ʿUmar ne lui reproche pas le parfum : il lui indique la manière de le porter jusqu'à la consécration sans que la trace ne s'épande, la charrah étant cette fosse du pied du palmier où le parfum macère avec le cheveu. Vient ensuite le pivot herméneutique de la leçon : Mālik, az-Zuhrī et un groupe de Compagnons et de suivistes interdisaient le taṣyīb à l'iḥrām quand la senteur persiste, et ʿIyāḍ rapporte leur taʾwīl du hadith de ʿĀʾicha — un parfum qui ne laisse pas de senteur après lui, ou dont le lavage avant l'iḥrām a fait disparaître la trace ; le second sens est appuyé par la riwāya de Muslim (« j'ai parfumé le Messager de Dieu au moment de son iḥrām, puis il rendit visite à ses épouses, puis il devint muḥrim »). Le chāriḥ en tire l'établissement du taʾwīl par la conduite dʿUmar lui-même : il n'a pas pris le hadith selon son apparent, il a récusé devant un grand rassemblement deux Compagnons et un suivantiste qui portaient beaucoup le parfum, et personne n'a récusé sa récusation — l'un des indices les plus forts.",
        "Le fiqh du chāriḥ range le corps en trois situations nettes. Avant l'iḥrām : le taṣyīb est permis — même recommandé au moment de l'intention d'iḥrām, la riwāya d'an-Nasāʾī le disant explicitement (« lorsqu'il voulut se consacrer ») —, la persistance de sa couleur et de ses odeurs ne nuit pas, et c'est son commencement dans l'iḥrām qui est interdit : c'est la doctrine des trois imams et du jumhūr, contre celle de Mālik, az-Zuhrī et du groupe qui interdisent quand la senteur persiste. Pendant l'iḥrām : pas permis, par le n° 925 — et les huiles qui ne sont pas parfumées restent licites (l'huile de dhikn chez Mālik), ce qui existe d'huiles contenant du parfum ayant le statut de l'usage du parfum. Après la jamrat al-ʿAqaba : permis d'après la totalité des savants — attestation du n° 923, le parfum du ḥall avant le rasage, donc avant le ṭawāf al-ifāḍa —, excepté que Mālik a trouvé cela détestable avant l'ifāḍa, d'après la divergence du n° 927 : Sālim par karāha, Khārija soit par licéité sans détestabilité, soit parce que le détestable fait partie du licite.",
        "La khulāṣa répond à la troisième question d'ouverture : le but de l'interdiction du parfum au muḥrim est de s'éloigner de la flaînerie (at-taraffuh) et de la parure du monde et de ses jouissances, de recueillir toute l'attention pour les finalités de l'au-delà et de revêtir le caractère de l'humble recueilli (al-khāshiʿ) — qu'il se rappelle la Présence devant son Seigneur, soit au plus proche de Sa vigilance (murāqaba) et de son abstention des interdits. L'évaluation retourne au fil en deux questions : exposer le statut du taṣyīb du corps et du vêtement avec les indices (le permis avant l'iḥrām et après la jamra — n° 923 et 927 ; l'interdit dans l'iḥrām — n° 924 et 925 ; l'huile sans parfum — n° 928 ; le vêtement lavé de sa senteur — n° 914), puis trancher trois situations imprimées : la femme consacrée qui porte un vêtement parfumé ; l'homme consacré atteint par ignorance puis averti ; la femme qui se parfume après la jamrat al-ʿAqaba et avant le ṭawāf al-ifāḍa. L'exploitation imprime le n° 929 : la nourriture au safran — ce que le feu a touché ne nuit pas au muḥrim de le manger, ce que le feu n'a pas touché il ne le mange pas ; trois questions de lecture, dont la recherche sur l'aliment qui est lui-même parfum (la pomme, le cédrat), renvoient l'élève au commentaire d'az-Zarqānī. La préparation préalable annonce la leçon 4 (anwāʿ al-iḥrām), déjà livrée au registre.",
    ],
    "points": [
        "Fil de révision : trois objectifs (statut du taṣyīb du corps et du vêtement ; situations du permis et de l'interdit ; finalité de la Loi) → tamhīd (le parfum, chose aimée du Messager) → huit textes (n° 923, 924, 926, 925, 928, 927, 914, 929) → notice de Kathīr b. aṣ-Ṣalt → gloses (athar ṣufr, charrah, labītu raʾsī) → fiqh (trois situations du corps ; deux cas du vêtement) → khulāṣa (la sagesse de l'interdiction) → évaluation en deux items → exploitation de la nourriture au safran.",
        "Les trois fenêtres du corps : permis et recommandé avant l'iḥrām (n° 923 — riwāya d'an-Nasāʾī : « lorsqu'il voulut se consacrer » ; la persistance de couleur et d'odeur ne nuit pas) ; interdit pendant l'iḥrām (n° 925 — doctrine des trois imams et du jumhūr ; Mālik, az-Zuhrī et le groupe : interdit quand la senteur persiste) ; permis après la jamrat al-ʿAqaba (n° 923 et 927 — totalité des savants, excepté la détestabilité de Mālik avant l'ifāḍa).",
        "Le taʾwīl du hadith de ʿĀʾicha : établi par la conduite dʿUmar (il n'a pas pris le texte selon son apparent ; sa récusation devant l'assemblée n'a pas été récusée), appuyé par ʿIyāḍ (un parfum sans senteur persistante, ou lavé avant l'iḥrām) et par la riwāya de Muslim (le parfum, puis la visite aux épouses, puis la consécration).",
        "Le vêtement : non-recommandation d'unanimité au moment de l'intention d'iḥrām (n° 924) ; l'oubli ou l'ignorance puis l'avertissement — se hâter d'enlever, pas d'expiation ; si cela tarde, le lavage devient obligatoire (Mālik) ; la senteur enfuie laisse l'iḥrām permis, la teinture de safran ou de wars l'interdit encore (n° 914) — la senteur s'enfuit avec l'interdit, la teinture demeure.",
        "La nourriture au safran (n° 929) : ce que le feu a touché est licite — le feu retire la senteur persistante, qui seule est interdite au muḥrim ; ce que le feu n'a pas touché ne se mange pas ; l'aliment qui est lui-même parfum (la pomme, le cédrat) reste matière de recherche, réponse chez az-Zarqānī.",
        "La sagesse (khulāṣa) : quitter le taraffuh et la parure du monde, recueiller l'attention pour les finalités de l'au-delà, la revêture de l'humble recueilli (al-khāshiʿ), la vigilance (murāqaba) et l'abstention des interdits devant la Présence du Seigneur.",
    ],
    "vocabulaire": [
        {"ar": "تطيب المحرم", "translit": "taṭyīb al-muḥrim", "fr": "l'usage du parfum du consacré — la leçon en délimite les fenêtres : recommandé avant l'iḥrām, interdit pendant la consécration, redevenu permis après la jamrat al-ʿAqaba (excepté la détestabilité de Mālik avant l'ifāḍa)"},
        {"ar": "الحل", "translit": "al-ḥall", "fr": "la désacralisation — « pour son ḥall avant qu'il ne se rase » (n° 923) : la seconde fenêtre licite du parfum, avant le rasage et le ṭawāf al-ifāḍa"},
        {"ar": "جمرة العقبة", "translit": "jamrat al-ʿAqaba", "fr": "le lancer qui ouvre la troisième fenêtre — après lui le taṣyīb du corps redevient permis, avant le ṭawāf al-ifāḍa, et l'iḥrām reste valide avant le versement (n° 923, 927, 928)"},
        {"ar": "الشرة", "translit": "ash-charrah", "fr": "la fosse (ḥafīra) au pied du palmier, une cuvette grande comme une marmite (qidār), où l'on rassemble le parfum avec le cheveu pour que les cheveux ne s'éparsillent pas dans l'iḥrām (n° 926)"},
        {"ar": "الصباغ", "translit": "aṣ-ṣibāgh", "fr": "la teinture de safran ou de wars — elle demeure visible sur l'étoffe et prolonge l'interdit même quand la senteur s'est enfuie ; la senteur, elle, s'enfuit et l'interdit avec elle (n° 914)"},
        {"ar": "القيد", "translit": "al-qayḍ", "fr": "le versement de Minā — se consacrer après le lancer de la jamra et avant de verser demeure valide, et l'huile sans parfum reste licite (n° 928)"},
        {"ar": "الترفه", "translit": "at-taraffuh", "fr": "la flaînerie — ce dont l'interdiction du parfum éloigne le consacré, avec la parure du monde et ses jouissances (khulāṣa)"},
        {"ar": "المراقبة", "translit": "al-murāqaba", "fr": "la vigilance — le consacré proche de la Présence (al-qudūm) devant son Seigneur, abstenu de commettre les interdits (khulāṣa)"},
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
DOCID = 'pdf-mut23h2x-392'
if DOCID in com:
    print(f'!! {DOCID} déjà présent — rien de fait')
    raise SystemExit(1)
com[DOCID] = norme_entree(E_392)

with open(CHEMIN, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
    f.write('\n')

# Validation : relecture + volume + ponctuation FR + arabes hors champ ar + guillemets appariés
data2 = json.load(open(CHEMIN, encoding='utf-8'))
print('entrées au total :', len(data2['commentaires']))
motif_ar = re.compile(r'[\u0600-\u06FF\u0750-\u077F\u08A0-\u08FF\uFDFA]')
mauvais = 0
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

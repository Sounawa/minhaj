#!/usr/bin/env python3
# build-19726.py — 19726 « Le rasm et le ḍabṭ : le chapitre du bāʾ »
# (rasm-wa-dabt-4ep, lessons[6], badge Leçon 8/30) — TROISIÈME document
# hand du livre (présentation 13995 R328 ; lessons[5] 19725 R329 — la
# préparation préalable de 19725 renvoyait aux vv. 22-27 = le matn ici).
# Matn = 6 bayts d'al-Wadghīrī sur le ḥaḏaf de l'alif après le bāʾ :
# tubāširū/bāširū (2:187, formes III — les DEUX dans le même verset),
# bāsiṭ 2 positions (13:14 + 18:18 ; garde : bāsiṭū 6:93 alif pleine),
# kayfa bāligh muṭlaq (singulier/pluriel), insib ḥusbān (accusatif ;
# garde : le génitif demeure — corpus 3× alif pleine 6:96/18:40/55:5 =
# divergence maghrébine), kabāʾira al-iṯm annexé (42:37 + 53:32 ;
# élision-signal vers le singulatif kabīra), bāṭil muṭlaq (25× élidé),
# arfaʿ anbāʾa bi-lā lām (NON vérifiable au corpus — 8× pleine, renvoi
# aš-Šuʿarāʾ 26:5 sans objet), bāḫiʿ (18:6 + 26:3), ruhbān bimīm (9:31
# élidé ; garde contre la nisba 57:27 ; 5:82/9:34 pleine = divergence),
# mubārak muṭlaq (6×, dont 38:29 marfūʿ mufrad ; troncature « wa-wa »),
# rabāʾib (tronqué), kayfa adbar + ṯumma idbar (kasra ; élision-signal
# vers wa-adbar ; 52:49), bāʿid (34:19 l'unique contre 25 baʿīd),
# aḥibbāʾuhu (5:18), al-asbāb (38:10 + 40:36), al-ḫabāʾiṯ (7:157 +
# 21:74), al-albāb (16×), ġaḍbān al-Aʿrāf + Ṭāhā (7:150 + 20:86),
# rubāʿ (4:3 + 35:1). Pluriels sains : féminin ṭayyibāt (20× ; mağrūr
# sans article 5:87 = vocalisation du naẓẓām ; renvoi appareil 89
# sans le mot), muʿaqqibāt (13:11), al-bāqiyāt (18:46 + 19:76),
# tāʾibāt + thayyibāt (66:5) ; masculin rabbāniyyīn/rabbāniyyūn
# (3:79 ; 5:44/5:63) + barizūn (40:16). Iʿdād → vv. 28-34 (leçon
# suivante) ; ʿibād élidé 19:65/38:45/43:19/89:29. Convention : au
# chapitre du bāʾ l'élision est GRAPHIQUE — l'alif suscrite reste
# récité (bāsiṭ, rabbāniyyūn), contre la hamza où elle emportait la
# longueur (qurʾanan). ONZIÈME tour sans protocole triple ; at-taʿbīm
# absent (compte : 26).
import re

parts = []
for i in range(1, 6):
    parts.append(open(f'/home/z/my-project/tr-tmp/fr19726_{i}.html').read())
html = ''.join(parts).strip()
html = html.replace("'", chr(0x2019))

issues = []
AR = re.compile('[' + ''.join(chr(a) + '-' + chr(b) for a, b in [
    (0x0600, 0x06FF), (0x0750, 0x077F), (0x08A0, 0x08FF),
    (0xFB50, 0xFDF9), (0xFDFB, 0xFDFD), (0xFE70, 0xFEFF)]) + ']')
ar = AR.findall(html)
if ar:
    ar = [c for c in ar if c != chr(0xFDFA)]
if ar:
    issues.append("caractères arabes résiduels: " + str(len(ar)) + " : " + ''.join(sorted(set(ar)))[:50])
if html.count("«") != html.count("»"):
    issues.append(f"guillemets non appariés: {html.count('«')} / {html.count('»')}")
if "'" in html:
    issues.append(f"apostrophes droites restantes: {html.count(chr(39))}")
for cp, name in [(0x0430, 'cyrillique'), (0xFD3E, 'crochet ornement gauche'), (0xFD3F, 'crochet ornement droit')]:
    if chr(cp) in html:
        issues.append(f'{name} présent')
for tag in ['h1', 'h2', 'h3', 'h4', 'p', 'ul', 'ol', 'li', 'em', 'span', 'dl', 'dt', 'dd', 'br', 'table', 'tbody', 'tr', 'td']:
    o = len(re.findall(f'<{tag}[ >]', html))
    c = html.count(f'</{tag}>')
    if tag in ('br',):
        if o and c:
            issues.append(f'balise {tag} fermante inattendue')
        continue
    if o != c:
        issues.append(f'balises {tag}: {o} ouvertes / {c} fermées')

norm = lambda s: s.replace("'", chr(0x2019))
probes = [
    "Le rasm et le ḍabṭ : le chapitre du bāʾ",
    "Nous avons éclairci — par la louange de Dieu — tous les mots qui sont venus avec l'élision de l'alif dans le chapitre de la hamza ; nous voici à présent, avec le naẓẓām, dans le chapitre du bāʾ.",
    "Après le chapitre de la hamza, qui ouvrait la série des lettres par la première d'entre elles, l'ouvrage avance d'un cran dans l'alphabet chez les Maghrébins : le bāʾ prend à son tour la parole, et c'est l'alif qui se tient après lui — élidée ou maintenue — qui en constitue la matière.",
    "Le naẓẓām prolonge ainsi, verset après verset, son dessein de mise en vers : déclarer le ḥaḏaf — ce qui fut élidé — parmi les mots du Coran, lettre après lettre, jusqu'au terme de l'alphabet.",
    "Quelles sont donc les mots élidées dans ce chapitre ?",
    "Et quelles sont les causes de leur élision ?",
    "Leçon figurant parmi les deux leçons du chapitre du bāʾ, de la matière du rasm et du ḍabṭ tirée de l'arjūza",
    "sur le jugement du ḥaḏaf dans le Coran, d'Idrīs al-Wadghīrī, destinée aux élèves de la quatrième année de l'enseignement primaire ancestral, la sixième leçon, le chapitre du bāʾ.",
    "1. Que je me familiarise avec certains des mots élidés dans le chapitre du bāʾ.",
    "2. Que je m'arrête aux applications du ḥaḏaf du pluriel sain dans le chapitre du bāʾ.",
    "3. Que je fasse éprouver à mon âme la grandeur du noble Coran à travers son rasm et son ḍabṭ.",
    "L'Imam Idrīs al-Wadghīrī — que Dieu lui fasse miséricorde — a dit :",
    "et bāsiṭ, en ar-Raʿd, puis en al-Kahf —",
    "tubāširū et bāširū, à l'élision !",
    "rubāʿ ; comment bāligh ? insib ḥusbān —",
    "et barizūn, bāḫiʿ, et ġaḍbān ;",
    "et al-bāqiyāt, tāʾibāt, thayyibāt ;",
    "et ṭayyibāt, bāṭil, muʿaqqibāt ;",
    "sans lām ; et ruhbān, bimīm, s'éclaire —",
    "kabāʾira al-iṯm : arfaʿ anbāʾa bi-lā [lām] ;",
    "baʿid, aḥibbāʾuhu, rabbāniyyīn —",
    "mubārak — comment ? — et rabbāniyyūn ;",
    "ḫabāʾiṯ al-albāb, puis idbar —",
    "rabāʾib al-asbāb — comment adbar ?",
    "Ces six vers déroulent, au fil de la rime, la nomenclature du chapitre",
    "et l'analyse qui suit, dans cette leçon même, revient sur chaque appel pour le déplier en règles, en exceptions et en restrictions.",
    "c'est-à-dire : [l'élision] en absolu, qu'il fût singulier ou pluriel.",
    "c'est-à-dire élède",
    "[dessiné] à l'accusatif.",
    "[au] nominatif, privé de la lām d'identification.",
    "c'est-à-dire l'élision s'est manifestée dans",
    "uni au mīm du pluriel.",
    "1. Je tire du matn les mots qui sont venus avec l'élision de l'alif.",
    "2. Quelles sont les deux positions où",
    "est venu avec l'élision ?",
    "3. Quelle est la restriction par laquelle le naẓẓām a cerné l'élision du mot",
    "Premièrement : les mots élidés dans le chapitre du bāʾ",
    "Le naẓẓām a rassemblé dans ces vers les mots dont l'alif fut élidée après le bāʾ, et il en a mentionné : le mot",
    "c'est-à-dire dans Son dire — transcendé — [exemple imprimé non porté par le document] ; et le mot",
    "en deux positions : ar-Raʿd, dans Son dire — transcendé —",
    "et en al-Kahf, dans Son dire",
    "il s'en est gardé à l'égard d'un cas semblable à",
    "car celui-là demeure fixé selon le qiyās.",
    "», c'est-à-dire : avec l'élision, en absolu — qu'il fût",
    "qu'il fût singulier, comme [exemple imprimé non porté par le document], ou pluriel sain, comme [exemple imprimé non porté par le document].",
    "l'accusatif, comme [exemple imprimé non porté par le document] — et ce qui est autre que lui demeure fixé selon le qiyās, comme [exemple imprimé non porté par le document].",
    "—, et ce sont deux positions : l'une en aš-Šūrā [exemple imprimé non porté par le document], l'autre en an-Nağm [exemple imprimé non porté par le document] — et c'est une élision-signal, vers la lecture de celui qui lit",
    "au singulatif.",
    "avec l'élision, en absolu, comme",
    "le nominatif, privé de la lām d'identification, en al-Anʿām, comme [exemple imprimé non porté par le document], et en aš-Šuʿarāʾ [le document porte le renvoi : aš-Šuʿarāʾ, verset 5]. Et il s'en est gardé par la lām, contre [exemple imprimé non porté par le document].",
    "— et en aš-Šuʿarāʾ également.",
    "l'élision s'est manifestée dans",
    "uni au mīm du pluriel, comme",
    "— et il s'en est gardé contre [exemple imprimé non porté par le document].",
    "c'est-à-dire : il s'élide en absolu, comme [exemple imprimé non porté par le document] — la fin de la phrase est tronquée dans la numérisation.",
    "— [le propos du document est tronqué] — et son dire",
    "c'est-à-dire : en absolu, comme [exemple imprimé non porté par le document]. Et son dire",
    "c'est-à-dire : avec la kasra de la hamza, comme [exemple imprimé non porté par le document] — et c'est une élision-signal, vers la lecture",
    "», dans Son dire [exemple imprimé non porté par le document] — et c'est une élision-signal. Et de même",
    "», dans Son dire [exemple imprimé non porté par le document]. Et de même",
    "», comme [exemple imprimé non porté par le document]. Et de même",
    "», en al-Aʿrāf et en Ṭāhā, comme [exemple imprimé non porté par le document]. Et",
    "», comme [exemple imprimé non porté par le document].</p>",
    "Deuxièmement : les mots qui sont venus à la forme du pluriel sain dans ce chapitre",
    "Le pluriel sain du féminin",
    "l'appareil du document porte le renvoi : al-Māʾida, verset 89], et de même",
    "comme [exemple imprimé non porté par le document], et de même",
    "le pluriel sain du masculin",
    "— la numérisation interrompt ici le fil — et de même",
    "» en [la suite du renvoi est tronquée dans la numérisation] ; 2.",
    "1. Je tire du matn les mots qui furent dessinés avec l'élision de l'alif.",
    "3. Je précise les restrictions de l'élision dans les mots suivants :",
    "Je remplis le tableau par ce qui convient des mots suivants :",
    "[Le tableau à remplir n'est pas porté par le document.]",
    "Je lis les vers restants dans le chapitre du bāʾ, du vers 28 au vers 34, et je réponds à ce qui suit :",
    "1. Je tire de ces vers les mots qui sont venus avec l'élision de l'alif.",
    "2. Je détermine les positions où",
    "3. Quel est le jugement de l'alif mutaṭarrifa après le bāʾ ?",
    "Notes du traducteur",
    "l'étiquette de la source machine, « Dessin et réglage : Chapitre B », écrase le vocabulaire technique du livre",
    "le document porte « la sixième leçon » de l'imprimé — les trois objectifs et le fil des leçons la confirment — tandis que le badge du site, comptant depuis la présentation du livre, s'affichera « Leçon 8 / 30 »",
    "la règle f est une formule, non une constante, et la leçon précédente, cinquième de l'imprimé, s'affiche « Leçon 7 / 30 ».",
    "le document se déclare « une leçon parmi les deux leçons du chapitre du bāʾ »",
    "la préparation de la leçon précédente renvoyait précisément aux vers 22 à 27, qui forment le matn de celle-ci — les deux positions de",
    "le livre source citait ses versets en images, que la numérisation ne porte pas — les emplacements « comme » ou « dans Son dire » suivent vides ;",
    "les deux formes élidées cohabitent dans le même verset d'al-Baqara",
    "wa-antum ʿākifūna fī l-masāğid » — formes de",
    ": l'alif élidée au rasm reste récité ; le corpus madanite la dessine suscrite en ces deux seuls lieux de toute l'Écriture, doublement vérifié.",
    "— les deux positions : 13:14 « illā",
    "kaffayhi ilā l-māʾ » et 18:18 « wa-kalbuhum",
    "» ; le garde du naẓẓām est confirmé de première main au corpus :",
    "(6:93, « al-malāʾika bāsiṭū aydīhim ») y garde l'alif pleine — c'est l'un des six mots mêmes de la mise en œuvre.",
    "— les deux sourates nommées par le texte : 7:150 « wa-lammā rağaʿa Mūsā ilā qawmihi",
    "asifan » et 20:86 « fa-rağaʿa Mūsā ilā qawmihi",
    "— mêmes contextes, même rasm élidé, vérifié de part et d'autre.",
    "— la restriction par l'annexé : les deux positions sont 42:37 et 53:32, « allaḏīna yağtanibūna",
    "l-iṯmi wa-l-fawāḥiš » — le mot n'y vient qu'annexé à",
    ", exactement la restriction du naẓẓām ; et l'élision-signal sert la lecture au singulatif : celui qui lit",
    "retrouve dans l'alif repliée la place de sa lecture.",
    "— divergence de rasm : le corpus madanite garde l'alif pleine aux trois occurrences — 6:96 « wa-š-šamsu wa-l-qamaru",
    "» et 18:40 « wa-yursila ʿalayhā",
    "(les deux accusatifs), 55:5 « bi-",
    "» (génitif) — alors que la prescription du naẓẓām, élider l'accusatif, relève de la convention maghrébine ; le garde, lui, se confirme : la forme autre que l'accusatif demeure au thubūt, et la divergence est portée, non corrigée.",
    "— le critère du mīm : l'élision se porte au corpus en 9:31 seul (« aḫbārahum wa-",
    "arbāban ») ; le garde se lit contre la nisba, 57:27 «",
    "» à l'alif pleine ; mais les deux autres occurrences au mīm — 5:82 « qissīsīna wa-",
    "» et 9:34 « al-aḫbāri wa-r-",
    "» — gardent l'alif pleine dans le rasm madanite : le critère du naẓẓām vaut pour la convention maghrébine, la divergence du corpus est signalée.",
    "— position non vérifiable : le corpus ne porte aucune",
    "élidée (huit occurrences, toutes à l'alif pleine — génitivales, ou définies en 28:66 et 54:4) ; ni al-Anʿām ni aš-Šuʿarāʾ n'y contiennent le mot, et le renvoi que porte l'appareil du document (« aš-Šuʿarāʾ, verset 5 ») n'y place aucune telle occurrence ; l'identification proposée n'est donc pas vérifiable au corpus — lacune signalée, non rétablie, comme pour al-Isrāʾ et Fuṣṣilat à la leçon précédente.",
    "— vingt-cinq positions élidées au corpus, dont « al-bāṭilu » marfūʿ (22:62, 31:30, 34:49) ;",
    "— 18:6 « fa-laʿallaka bāḫiʿun nafsaka », et aš-Šuʿarāʾ « également », comme le dit le texte : 26:3 « laʿallaka bāḫiʿun nafsaka » ;",
    "— six positions élidées, dont 38:29 « kitābun anzalnāhu ilayka",
    "», le nominatif mufrad même que le naẓẓām appelle, la fin de la phrase étant tronquée (« wa-wa » — jambe de numérisation) ;",
    "— 34:19 « rabbanā",
    "bayna asfārinā », l'unique élidé du corpus contre vingt-cinq",
    "— 5:18 « naḥnu",
    "llāhi wa-",
    "», où la même élision touche les deux mots du verset ;",
    "— 38:10 « fa-l-yartaqū fī l-asbābi » et 40:36 « abluğu l-asbāba » ;",
    "— 7:157 et 21:74 ;",
    "— seize positions élidées, toutes les occurrences de",
    "— 4:3 et 35:1, dans la paire fixe « wa-ṯalāṯa wa-",
    "— vingt positions élidées ; la forme mağrūr sans article, «",
    "» (5:87, « lā tuḥarrimū ṭayyibāti mā aḥalla llāhu lakum »), porte exactement la vocalisation du naẓẓām, tandis que le renvoi de l'appareil (« al-Māʾida, verset 89 ») ne contient pas le mot au corpus — décalage de renvoi porté ;",
    "— 13:11 « lahū",
    "», unique ;",
    "— 18:46 et 19:76, « wa-l-bāqiyātu ṣ-ṣāliḥātu », le mot même du naẓẓām avec son wāw ;",
    "— toutes deux en 66:5, dans l'énumération des épouses : « muslimāt muʾmināt qānitāt",
    "ʿābidāt sāʾiḥāt",
    "— 40:16 « yawma hum",
    "— 3:79 « kūnū",
    "» (accusatif), 5:44 et 5:63 « ar-rabbāniyyūna » (nominatif avec la lām), tous élidés au corpus.",
    "au chapitre du bāʾ, l'élision est graphique — l'alif élidée, suscrite dans le corpus et non tracée dans la convention maghrébine, demeure récité :",
    "gardent leur longueur ; au chapitre de la hamza, en revanche, l'élision emportait la longueur elle-même (",
    ") — la distinction gouverne le rendu des deux chapitres, et la traduction la maintient.",
    "le naẓẓām nomme deux fois le ḥaḏf « signal » — pour",
    ", vers la lecture au singulatif",
    " ; pour ",
    ", vers la lecture « wa-adbar » ; le corpus porte 52:49 « fa-sabbiḥhu wa-",
    "n-nuğūmi » — kasra de la hamza et alif suscrite — et ne livre pas l'appareil des lectures ; le mot du naẓẓām est rendu tel quel, la divergence d'appareil n'étant pas rétablie.",
    "est écrit dans l'imprimé avec la hamza portée par le wāw avant l'alif de prolongement —",
    ", ordre maghrébin des porteurs — tandis que la mise en œuvre écrit le même mot avec le madda sur l'alif ; la traduction suit la prononciation (",
    "le tableau à remplir n'est pas porté par la numérisation ; les six mots proposés se vérifient ainsi au corpus —",
    "(5:82, à l'alif pleine dans le rasm madanite),",
    "(le mot est donné avec alif, 13:14 l'ayant élidée au rasm),",
    "(jamais élidée au corpus),",
    "(55:5, alif pleine),",
    "(6:93, alif pleine),",
    "(52:49, élidée) — matière du tri que le tableau demandait.",
    "les vers 28 à 34 du chapitre du bāʾ ne sont pas portés par ce document — ils relèvent de la leçon suivante, comme le fil des leçons l'annonce ; les positions élidées de",
    "se vérifient au corpus en quatre lieux : 19:65 « li-ʿibādatihi », 38:45 «",
    "Ibrāhīma », 43:19 «",
    "r-Raḥmāni » — elidée bien qu'avec la lām — et 89:29 « fī",
    "» ; et la troisième question, sur l'alif mutaṭarrifa après le bāʾ, applique au bāʾ la règle de l'extrême final que la leçon précédente établissait après la hamza — l'ouvrage avance dans l'alphabet sans abandonner ce qu'il a établi.",
    "aucun verset coranique n'est cité au fil du document — les citations imprimées étaient des images, absentes de la numérisation ; onzième tour sans le protocole triple, mais vérification faite au corpus coranique de chaque mot du rasm que le texte nomme, et des positions restituées en note, toutes croisées avec la leçon du document (élision ou thubūt, mīm ou lām, singulier ou pluriel) ; at-taʿbīm est absent de ce document — le compte demeure à vingt-six.",
]

missing = [p for p in probes if norm(p) not in html]
for p in missing:
    issues.append("SONDE ABSENTE: " + p[:80])

if issues:
    print("BUILD ÉCHOUÉ — " + str(len(issues)) + " problème(s) :")
    for it in issues:
        print("  -", it)
    raise SystemExit(1)

out = '/home/z/my-project/tr-tmp/19726.html'
with open(out, 'w') as f:
    f.write(html)
print(f"OK — {out} : {len(html)} caractères, sondes: {len(probes)}/{len(probes)}")

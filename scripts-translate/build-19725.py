#!/usr/bin/env python3
# build-19725.py — 19725 « Le rasm et le ḍabṭ : le chapitre de la hamza »
# (rasm-wa-dabt-4ep, lessons[5], badge Leçon 7/30) — PREMIÈRE LEÇON du
# corps du cours (présentation 13995 livrée R328 ; lessons 1-4 déjà LLM).
# Deuxième leçon hand du NOUVEAU livre rasm-wa-dabt-4ep. Matn = 5 bayts
# d'al-Wadghīrī sur le ḥaḏaf de l'alif après la hamza : les mots élidés en
# absolu (sawʾat multiple 5×, munšaʾat unique ar-Raḥmān 55:24, ḫaṭīʾat
# mufrad 2:81/pluriel 71:25, burʾaʾū 60:4, alif al-idḫāl de ilan en
# Qālūn/Warš sauf al-Jinn 72:9, ʾāāmantum/ʾāālihatunā + Ibn al-Qāḍī
# (ṣūra à la deuxième, attache de la troisième) + al-Ḫarrāz + Nuṣrat
# al-kuttāb v.27, ǧāʾana + ḥaḏf al-muṯannā) ; l'élipté de deux occurrences
# seules (qurʾanan aux ouvertures de Yūsuf 12:2 et az-Zuḫruf 43:3,
# muḥtaraẓ de hāḏā l-qurʾān 12:3 et lawlā nuzzila 43:31) ; le thubūt seul
# (raʾā en quelque cas) ; l'extrême final (naʾā = bināʾan 2:22, exceptions
# an-Najm 53:11/53:18 avec yāʾ, as-suwʾā avec yāʾ selon le rūm). Analyse :
# ḥaḏf attaché (alif/wāw/yāʾ/nūn) = rouge au muṣḥaf, fin šiqq al-qalam aux
# planches — Ibn aṭ-Ṭayyib as-Siğilmāsī, Nuṣrat al-kuttāb p.54 (vv.22-23)
# cité en 2 bayts ; madhhab Abū Dāwūd (fusha comme al-ʿālamīn) ; l'alif
# droite et dressée toujours. Fentes : AUCUNE (0 āya / 0 hadīth cités —
# DIXIÈME tour sans protocole triple) — les exemples imprimés du livre
# source étaient des IMAGES, absentes de la numérisation : lacunes portées
# + restitution vérifiée au quran-cache en N.d.T. (12:2, 43:3, 12:3,
# 43:31, 55:24, 7:20-27, 20:121, 60:4, 2:81, 71:25, 53:11, 53:18, 72:9,
# 2:22). Exploitation = Tamhīd aṭ-ṭarīq p.18 texte 15 (table 3 bayts du
# rasm de ʾāāmantum : hamza dans la ligne, alif fixé, pointe au-dessus,
# alif élidée après) ; préparation préalable → chapitre du bāʾ (vv.22-27,
# basiṭ) = 19726. Convention translittération : élision = absence de
# longueur (qurʾanan vs qurʾān) ; double-alif maghrébin = ʾāā-.
import re

parts = []
for i in range(1, 6):
    parts.append(open(f'/home/z/my-project/tr-tmp/fr19725_{i}.html').read())
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
for tag in ['h1', 'h2', 'h3', 'h4', 'p', 'ul', 'ol', 'li', 'em', 'span', 'dl', 'dt', 'dd', 'br']:
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
    "Le rasm et le ḍabṭ : le chapitre de la hamza",
    "Après la présentation, le naẓẓām s'engagera dans les vers qui suivent sur le dessein de sa mise en vers",
    "la déclaration du ḥaḏaf — de ce qui fut élidé — parmi les mots du Coran",
    "ordonnés selon l'ordre des lettres de l'alphabet chez les Maghrébins",
    "il commence donc par le propos sur l'alif élidé après la hamza, parce qu'elle est la première des lettres",
    "Quels sont donc les mots élidés dans le chapitre de la hamza ?",
    "Et quelle est la manière de l'attache de l'alif élidé ?",
    "d'Idrīs al-Wadghīrī, destinée aux élèves de la quatrième année de l'enseignement primaire ancestral",
    "la cinquième leçon",
    "1. Que je me familiarise avec les mots au ḥaḏaf dans le chapitre de la hamza.",
    "2. Que je m'exerce à la manière de ménager la fusha et d'y attacher l'alif élidé.",
    "3. Que j'accoutume mon âme à préserver le rasm du noble Coran et son ḍabṭ.",
    "L'Imam Idrīs al-Wadghīrī — que Dieu lui fasse miséricorde — a dit",
    "Au commencement de Yūsuf et au commencement d'az-Zuḫruf",
    "sawʾat, munšaʾat, qurʾanan — ôte [l'alif] !",
    "et à la droite du lām, attache — c'est l'éclaircissement ;",
    "et l'alif d'insertion, hors celui d'al-Jinn : celui de ilan ;",
    "de même ʾāāmantum [et] ʾāālihatunā",
    "ainsi que burʾaʾū et ḫaṭīʾat — sois perspicace !",
    "de même l'extrême final, comme naʾā ;",
    "avec l'élision de ǧāʾana, et établis [celle de] raʾā !",
    "et non comme as-suwʾā — digne, avec yāʾ ;",
    "hormis raʾā : avec yāʾ, celui qui a [un] min",
    "c'est-à-dire au début de la sourate Yūsuf.",
    "c'est-à-dire au début de la sourate az-Zuḫruf.",
    "c'est-à-dire un alif que l'on insère entre la hamza et le tasḥīl dans la riwāya de Qālūn.",
    "l'attache est l'écriture de la lettre élidée en tracé fin, ou à l'encre rouge.",
    "c'est-à-dire saisis cela et comprends-le — de la fiṭna au sens d'intelligence.",
    "c'est-à-dire celle qui est à la fin du mot.",
    "c'est-à-dire véritable et méritant.",
    "1. Je clarifie les mots qui sont venus avec l'élision de l'alif après la hamza.",
    "2. Où rencontre-t-on le mot qurʾanan avec l'élision de l'alif ?",
    "3. Quel est le jugement de l'alif après la hamza à l'extrémité du mot ?",
    "L'élision est de deux sortes : tantôt elle est attachée, tantôt elle ne s'attache point.",
    "Et chacune des deux est conventionnelle, non analogique.",
    "son jugement est d'être attaché dans le muṣḥaf à l'encre rouge",
    "et dans les planches, il s'attache en tracé fin avec la fente du calame",
    "et sache : laisse-lui une fusha dans la planche ;",
    "le ḥaḏf attaché se trace avec la fente du calame,",
    "et relie-le à la ligne avec elle — tu feras justice.",
    "et écris-le à l'encre rouge dans les muṣḥafs.",
    "d'Abū ʿAbd Allāh Muḥammad at-Tihāmī Ibn aṭ-Ṭayyib as-Siğilmāsī, p. 54 (les deux vers 22-23).",
    "Et le madhhab d'Abū Dāwūd est de ménager une fusha entre la lettre qui précède l'attaché et celle qui le suit",
    "l'alif, en absolu — fixée, ou attachée, ou porteuse de la hamza, ou superflue —, se tient droite et dressée",
    "Et ces vers ont contenu ce qui suit :",
    "Premièrement : les mots qui sont venus avec l'élision de l'alif après la hamza",
    "1. L'élipté en absolu, sans exception",
    "leur alif s'élide par abréviation dans le pluriel du féminin sain, et par économie dans ce qui est autre que lui",
    "il est multiple, comme [exemples imprimés non portés par le document]",
    "est unique dans la sourate ar-Raḥmān",
    "se varie vers l'annexé du singulier masculin",
    "et vers le pluriel, comme [exemples imprimés non portés par le document]",
    ", dans Son dire [exemple imprimé non porté par le document].",
    "l'alif inséré entre la hamza et le tasḥīl, et cela dans la riwāya de Qālūn d'après Nāfiʿ",
    ", le rasm de « maintenant », s'élide aussi dans la riwāya de Qālūn",
    "quant à Warš, il a pour elle le naql — le report —, hors celle qui est dans la sourate al-Jinn",
    "laquelle est au thubūt, selon le qiyās",
    "attache l'alif à la droite du lām de",
    ", non à la gauche",
    "et le naẓẓām en reviendra au chapitre du lām",
    "Ibn al-Qāḍī a dit : « Le fameux dans les deux est de donner la forme — la ṣūra — à la deuxième et d'attacher la troisième. »",
    "Et il la faut faire atteindre la ligne ici : al-Ḫarrāz l'a explicité dans son ḍabṭ",
    "et le rattachement est plus digne ici",
    "[le vers 27 de la",
    "mais elle est avec la fente du calame dans les planches, et à l'encre rouge dans le muṣḥaf",
    "avec l'élision de ǧāʾana —, c'est-à-dire : élède l'alif après la hamza",
    "Et cela selon la règle de l'élision du duel.",
    "2. L'élipté dont deux occurrences seules furent élidées, son reste au thubūt",
    "en deux positions : la première au début de la sourate Yūsuf — sur lui le salut —,",
    "— muḥtaraẓ — contre «",
    "hāḏā l-qurʾāna",
    "lawlā nuzzila hāḏā l-qurʾānu",
    "dans la même sourate — car ces deux-là sont avec l'alif",
    "Deuxièmement : le dessiné au seul maintien de l'alif",
    "en quelque état qu'il fût, au masculin comme [exemple imprimé non porté par le document]",
    "ou au féminin comme [exemple imprimé non porté par le document]",
    "ou à l'interlocuteur comme [exemple imprimé non porté par le document]",
    "Troisièmement : le jugement de l'alif après la hamza à l'extrémité du mot",
    "quand le naẓẓām eut achevé l'élipté, et le fixé que l'on prolonge en pleine ligne, il pointa l'extrême final",
    "fixe l'alif extrême après la hamza en absolu, indiquant le duel",
    "ou une lāma pour le mot, comme [exemple imprimé non porté par le document] — dans al-Isrāʾ, et dans Fuṣṣilat aussi",
    "hormis raʾā : avec yāʾ, celui qui a min, ou mā",
    "dans Son dire — transcendant — dans la sourate an-Najm [exemple imprimé non porté par le document]",
    "car ces deux-là sont avec la yāʾ",
    "c'est-à-dire : selon le rūm, elle se dessine avec la yāʾ, de même",
    "1. Quelle est la manière de l'attache de l'alif élidé ?",
    "2. Comment se dessine le mot ʾāāmantum selon le fameux ?",
    "3. Je précise les positions où raʾā est venu avec la yāʾ à l'extrémité.",
    "Un texte qui clarifie le rasm de ʾāāmantum et de ʾāālihatunā :",
    "ʾāāmantum : une hamza dans la ligne,",
    "et d'un alif fixé — la science en rend compte ;",
    "et d'une pointe tracée au-dessus d'elle,",
    "et d'un alif élidé après elle ;",
    "et sa longueur est comme la longueur du premier.",
    "ainsi ʾāālihatunā dans l'exemple ;",
    "vers la connaissance des textes coraniques par l'enseignement ancestral : le rasm et le ḍabṭ, p. 18, texte 15.]",
    "J'explique comment se dessine l'alif élidé après le tasḥīl, à travers ce que j'ai étudié en cette leçon",
    "La préparation préalable",
    "Je lis les vers 22 à 27 dans le chapitre du bāʾ et je réponds à ce qui suit :",
    "1. Quels sont les mots qui sont venus avec l'élision dans ces vers ?",
    "2. Je cite les deux positions où basiṭ est venu avec l'élision de l'alif.",
    "Notes du traducteur",
    "— fait foi : « le rasm et le ḍabṭ : le chapitre de la hamza »",
    "ordre des lettres « chez les Maghrébins »",
    "), dit le document",
    "« la cinquième leçon »",
    "le badge du site compte autrement : la présentation du livre porte « Leçon 2 / 30 », et cette leçon s'affichera « Leçon 7 / 30 »",
    "la règle f est une formule, non une constante",
    "le document numérisé ne les porte pas — les emplacements « comme » ou « dans Son dire » suivent vides",
    "cinq occurrences, toutes au rasm élidé : quatre en la sourate al-Aʿrāf (7:20, 7:22, 7:26, 7:27) et une en la sourate Tāhā (20:121)",
    "unique dans ar-Raḥmān — 55:24",
    "annexée au singulier masculin — 2:81",
    "et au pluriel — 71:25",
    "— 60:4 « innā burʾāʾu minkum », la sourate al-Mumtaḥana",
    "élidé aux deux ouvertures — 12:2",
    "le corpus dessinant le mot avec l'alif suscrit en ces deux seuls lieux",
    "le thubūt vérifié de même — 12:3 « hāḏā l-qurʾāni » et 43:31 « lawlā nuzzila hāḏā l-qurʾānu »",
    "72:9 « fa-man yastamiʿi l-ʾāna yağid lahu šihāban raṣadan », la sourate al-Jinn portant l'alif pleine",
    "exactement l'exception de Warš que l'arjūza documente",
    "53:11 « mā kaḏaba l-fuʾādu mā raʾā » (précédé de mā)",
    "53:18 « laqad raʾā min āyāti rabbihī l-kubrā » (avec min)",
    "le corpus madanite ne livre aucun mot terminé par hamza et alif dans ces deux sourates",
    "la lacune est signalée, non rétablie",
    "s'y trouve au pluriel seul",
    "le rūm, terme technique que le contexte ne définit pas davantage, est laissé translittéré sans être forcé",
    "l'absence de longueur —",
    "élidé contre",
    "2:22 « wa-s-samāʾa bināʾan » — vérifié, le corpus portant l'alif pleine après la hamza",
    "le rasm double-alif de l'ā maghrébin se rend ʾāā- (",
    "la hamza dans la ligne, l'alif fixé, la pointe au-dessus, l'alif élidé après, la longueur du premier",
    "est l'encre rouge des muṣḥafs",
    "avec la fente du calame (",
    "« comme al-ʿālamīn » tel que la graphie l'allonge",
    "avec une kasra déplacée là où le sens commande",
    ", le naẓẓām — nous suivons la lecture du sens et signalons la graphie",
    "— jambe de composition, que la traduction sépare",
    "la préparation préalable renvoie aux vers 22-27 du chapitre du bāʾ",
    "avec l'élision de l'alif : le fil annoncé d'une leçon à l'autre se poursuit",
    "dixième tour sans le protocole triple",
    "vérification faite au corpus coranique de chaque mot du rasm que le texte nomme",
    "toutes croisées avec la leçon du document (élision ou thubūt, alif ou yāʾ)",
]

missing = [p for p in probes if norm(p) not in html]
for p in missing:
    issues.append("SONDE ABSENTE: " + p[:80])

if issues:
    print("BUILD ÉCHOUÉ — " + str(len(issues)) + " problème(s) :")
    for it in issues:
        print("  -", it)
    raise SystemExit(1)

out = '/home/z/my-project/tr-tmp/19725.html'
with open(out, 'w') as f:
    f.write(html)
print(f"OK — {out} : {len(html)} caractères, sondes: {len(probes)}/{len(probes)}")

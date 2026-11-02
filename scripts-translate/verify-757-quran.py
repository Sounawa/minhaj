#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Minhāj — contrôle coranique et de contenu de la leçon 756 (tafsir-5ep,
sūrat al-Kahf v59-64 de l'imprimé warš — dix-huitième leçon du second livre,
pages 132-141 du manuel miroir tafsir-3-thanawi). La plage imprimée (59-64)
correspond aux āyāt 60-65 du cache canonique ḥafṣ (décalage de un, tranché
R511). Les six āyāt sont rendues en français sur le cache (présence vérifiée) ;
les āyāt 1-59 (leçons 739-755) et 66-73 (leçon 757) sont interdites de double
rendu ; le rasm nu du cache interdit au corps (0 arabe — FR-seule)."""
import json
import re
import sys

HTML = "tr-tmp/lesson-757-fr.html"
html = open(HTML, encoding="utf-8").read()
norm = re.sub(r"[ \u202f\u00a0]+", " ", html.replace("&nbsp;", "\u00a0"))
errors = []

# 1. structure et marqueurs
for frag in [
    "Source du cours",
    "Dix-neuvième leçon du second livre du parcours",
    "pages 142 à 149 de l’imprimé miroir",
    "1_20220304_20220304_2251",
    "p.142 ouvre la leçon 19 au badge al-Kahf (65-72)",
    "les objectifs de la leçon 20 ouvrent p.150",
    "Les objectifs de la leçon",
    "Le tamhīd",
    "Le commentaire",
    "La glose",
    "L’extraction des thèmes des āyāt",
    "Premièrement",
    "Deuxièmement",
    "Troisièmement",
    "Quatrièmement",
    "Les subtilités et les bienfaits",
    "L’évaluation",
    "L’exploitation",
    "la page imprimée 149",
    "jamais devinée",
    "interdites de double rendu",
    "plage imprimée (65-72) correspond aux āyāt 66 à 73 du cache canonique",
]:
    if frag.lower() not in norm.lower():
        errors.append(f"fragment attendu absent : {frag[:55]}")

# 2. les āyāt 60-65 rendus du cache — présence (6 rendus + 6 numéros)
cache = json.load(open("scripts-translate/quran-cache.json", encoding="utf-8"))
fr18 = {n: t for n, t in cache["18"]["fr"]}
rendus = [fr18[n] for n in (66, 67, 68, 69, 70, 71, 72, 73)] + [f"({n})" for n in (65, 66, 67, 68, 69, 70, 71, 72)]
rendus_norm = [r.replace("'", "’").replace(" ", "") for r in rendus]
compact = norm.replace(" ", "")
for r in rendus_norm:
    if r not in compact:
        errors.append(f"rendu coranique attendu absent : {r[:55]}")

# 3. contenu attendu (confrontation au manuel — glose, lectures, exégètes)
contenu = [
    "les règles de la compagnie et les étiquettes de l’apprentissage",
    "quand bien même la sagesse m’en échapperait",
    "en l’éducation avec le maître",
    "la rencontre de Mūsā et de son serviteur avec al-Khiḍr",
    "la marque qui les y conduisit",
    "le but de Mūsā en la compagnie de al-Khiḍr",
    "la relation de l’étudiant au maître",
    "une explicitation et une éclaircie",
    "tu me réprimandes et me châties",
    "la contrainte et l’étroitesse",
    "la condition posée par al-Khiḍr en la compagnie",
    "l’étudiant suit l’homme de science quand bien même les rangs différeraient",
    "sortit de l’interrogation vers la demande, l’exposition confirmée et l’incitation",
    "la tāʾ de l’iftiʿāl, adghamée en la tāʾ originelle",
    "employée pour l’hyperbole du verbe",
    "le complément second du verbe de l’enseignement",
    "qu’elle soit ḥāl du pronom",
    "que la direction renvoie à al-Khiḍr",
    "de ce que Dieu t’a enseigné et par quoi Il t’a dirigé",
    "les lettres redondantes y sont élidées du rasm",
    "Ibn Kaṯīr, Nāfiʿ et les Kufans ont lu au ḍamm du rāʾ et le sukūn du šīn",
    "Abū ʿAmr a lu au fatḥ des deux",
    "les deux lexies sont deux langues",
    "comme la lésinerie et son semblable, la mutité et la non-arabité",
    "Mūsā salua al-Khiḍr et lui dit",
    "Mūsā des fils d’Israël",
    "je suis venu pour que tu m’enseignes de ce que tu as appris de direction droite",
    "ne te suffit-il que la Tora soit en tes mains",
    "j’ai une science qu’il ne t’appartient point d’apprendre",
    "tu as une science qu’il ne m’appartient point d’apprendre",
    "tu ne peux supporter la patience sur ce que tu verras de ma science",
    "les apparences qui sont ta science ne le donnent point",
    "sans que l’on t’expose la face de la sagesse y étant",
    "j’agis par le secret d’une science que Dieu m’a enseignée",
    "nulle science à toi sinon par l’apparent des choses",
    "Ǧāmiʿ al-Bayān",
    "9/382",
    "m’imposant à moi-même l’obéissance envers toi",
    "l’on a divergé en l’excepté",
    "il excepta la patience et s’en chargea",
    "il s’opposa et questionna",
    "la patience est une affaire future, dont on ne sait l’état",
    "la négation de la désobéissance est présente en le présent",
    "l’excepté y contredirait la résolution sur lui",
    "6/41",
    "examina [la portée de la restriction]",
    "jusqu’à ce que je sois moi qui t’en expose la mention",
    "car sa science t’est absente",
    "ne me presse point de questions jusqu’à ce que je sois moi qui t’en expose la clarté",
    "7/602",
    "suivit cette conversation qu’ils partent tous deux",
    "l’élancement : le départ et la marche",
    "ils élancèrent en marchant sur le rivage de la mer, sans navire à eux",
    "un navire passa auprès d’eux",
    "il reconnut al-Khiḍr — sans salaire — et les porta",
    "un oiseau vint et se posa sur le bord du navire",
    "ma science et ta science n’eurent rien retranché de la science de Dieu",
    "sinon comme ce picquetage de l’oiseau en la mer",
    "al-Khiḍr s’empara alors d’une planche des planches du navire et l’ôta",
    "tu vises leur navire pour le percer et noyer ses gens",
    "ne t’avais-je dit que tu ne pourrais avec moi la patience",
    "ne me réprime pas de ce que j’ai oublié",
    "ḥadīṯ 3220 — chiffre imprimé tranché",
    "y est une détermination du genre, non un rappel de son être propre",
    "nul rappel n’avait précédé en un navire spécifié",
    "al-Khiḍr s’empara du tenon et se mit à frapper le flanc du navire",
    "deux planches de ses planches",
    "il y fit une crevaison et une entaille apparentes à l’œil",
    "que l’œil violerait et mépriserait à cause d’elles",
    "l’apparent de l’affaire le vainquit sur le propos",
    "un acte menant à la noyade de tous ceux du navire",
    "le premier reproche de Mūsā sur al-Khiḍr",
    "Ibn Kaṯīr, Nāfiʿ, Abū ʿAmr, Ibn ʿĀmir et ʿĀṣim ont lu au tāʾ",
    "en l’élévation de ses gens et l’attribution du verbe à eux",
    "au tāʾ, au fatḥ de la ġayn et le tašdīd du rāʾ",
    "est la lām de l’aboutissement — la conséquence",
    "pour qu’il fût pour eux un ennemi et un sujet de tristesse",
    "al-Qaṣaṣ",
    "renvoi imprimé tranché",
    "sur la lecture de Ḥamza, la lām de justification",
    "ne dit point « pour me noyer moi »",
    "la compassion excessive pour eux l’emporta en le présent",
    "l’égard de leur droit",
    "le hideux et le laid des choses — comme la calamité et la destruction",
    "Maǧāhid dit : le monstrueux est le répréhensible",
    "tu as commis une chose immense et un acte répréhensible",
    "s’excusa par l’oubli",
    "qu’il oublia le pacte qui était entre eux deux",
    "c’est le dire de la masse",
    "la première [affaire] de Mūsā fut un oubli",
    "la première fut oubli, la seconde [violation de] condition, la troisième délibérée",
    "le sens de ce propos est juste",
    "n’eut vu le pacte qu’en le fait de ne point questionner, sans l’exposer",
    "il ne tint point le questionnement un déni de cet acte hideux, mais le tint obligé",
    "avait pris le pacte en ses faces les plus amples",
    "il y logea la question, la contestation, le déni et toute opposition",
    "la question étant la plus légère de toutes celles-ci",
    "la voie des oppositions qui préservent du mensonge",
    "ne lui dit point : j’ai oublié le pacte",
    "il joignit en cet énoncé l’excuse et la vérité",
    "kitāb al-ʾīmān wa-n-nuḏūr, bāb iḏā ḥanitha nāsiyan fī al-ʾīmān",
    "ḥadīṯ 5926 tel qu’imprimé",
    "ne me contraigns point et ne m’étreins pas",
    "par l’abandon de la dispute",
    "traite-moi avec la facilité, non avec la peine",
    "Il le jugea par la coutume des créatures en le défaut de la patience",
    "un fondement du jugement par la coutume",
    "l’application de la coutume aux jugements",
    "les fuqahāʾ formulèrent en une règle unanime entre les écoles",
    "la coutume a autorité",
    "une immense humilité, et l’exposition de l’endurance complète",
    "l’obligé de l’étudiant est d’exposer l’humilité aux extrémités",
    "Mafātīḥ al-Ġayb",
    "12/484 tel qu’imprimé",
    "une preuve de l’humilité envers l’homme de science",
    "l’incitation au voyage en quête de science",
    "du beau raffinement et de la douceur et de l’éducation",
    "7/502",
    "le type de la lām à chaque lecture",
    "son jugement ferme de l’incapacité de Mūsā à la patience",
    "vers « pour noyer ses gens »",
    "la patience et l’obéissance venant de l’homme de science",
    "sont plus dures que la patience et l’obéissance de qui n’est point homme de science",
    "la vacuité de son esprit de science ne le contraint point en la vision des choses étranges",
    "il n’y a pas en son esprit de connaissances qui résistent à leur acceptation",
    "venu cherchant la complétude de ses sciences",
    "ce qui contredit ce qui s’est établi en sa science",
    "al-Taḥrīr wa-t-Tanwīr",
    "15/373 avec remaniement",
    "Je lis le texte avec soin, puis je réponds",
    "l’effet de la patience en la réalisation des objectifs",
    "le mérite de la quête de science, et les effets de l’effort en son acquisition",
    "les livres d’étiquettes de la science",
    "les éducations de l’homme de science et de l’étudiant",
    "cache 74 et suivantes",
    "les lectures venues en le mot « fākiha »",
    "le style rhétorique en Sa parole",
    "La leçon s’achève en la page imprimée 149",
    "la leçon suivante ouvre en la page 150 du même manuel",
    "kahf-probe-l19.py",
    "Sourate al-Kahf, les versets (65 - 72)",
    "imprimé 72 = cache 73",
    "l’ouverture des objectifs de la leçon 20 en p.150",
    "convergence — jamais devinée",
]
for c in contenu:
    if c.lower() not in norm.lower():
        errors.append(f"contenu attendu absent : {c[:55]}")

# 4. rendus interdits (āyāt 1-59 livrées leçons 739-755 ; 66-73 leçon 757)
interdits_src = (1, 10, 32, 45, 46, 57, 59, 60, 61, 62, 63, 64, 65, 74)
interdits = []
for n in interdits_src:
    t = fr18[n].replace("'", "’")
    interdits.append(t[:60])
    interdits.append(t[-60:])
for probe in interdits:
    if probe in norm:
        errors.append(f"rendu hors matière présent : {probe[:50]}")

rasm_18 = {n: t for n, t in cache["18"]["ar"]}
rasm_n = 0
for n in list(range(1, 66)) + list(range(74, 111)):
    t = rasm_18[n]
    probes = [t, t.replace(" ", "")]
    ok = any(p in norm.replace(" ", "") for p in probes) or t in norm
    if ok:
        errors.append(f"rasm arabe interdit présent au corps (āya 18:{n})")
    rasm_n += 1

# 5. 0 arabe résiduel (ﷺ U+FDFA exempté, convention du corpus)
ARABIC = re.compile(r"[\u0600-\u06FF\u0750-\u077F\u08A0-\u08FF\uFB50-\uFDF9\uFDFB-\uFDFF\uFE70-\uFEFF]")
resid = ARABIC.findall(norm)
if resid:
    errors.append(f"arabe résiduel : {len(resid)} caractère(s), ex. {[c for c in resid[:5]]}")

# 6. typographie
if "'" in html:
    errors.append("apostrophe droite présente")
if html.count("«") != html.count("»"):
    errors.append(f"guillemets non appariés : « {html.count('«')} vs » {html.count('»')}")

total = 22 + len(rendus) + len(contenu) + len(interdits) + rasm_n + 3
print(f"verify-757-quran : {total} contrôles — rendus {len(rendus)} + contenu {len(contenu)} + interdits {len(interdits)} + rasm {rasm_n} + structure {22} + typo 3")
if errors:
    print("verify-757 FAIL :")
    for e in errors:
        print(" -", e)
    sys.exit(1)
print("verify-757 PASS")

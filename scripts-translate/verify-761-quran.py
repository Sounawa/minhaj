#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Minhāj — contrôle coranique et de contenu de la leçon 761 (tafsir-5ep,
sūrat al-Kahf v85-91 de l'imprimé warš — vingt-troisième leçon du second livre,
pages 171-178 du manuel miroir tafsir-3-thanawi). La plage imprimée (85-91)
correspond aux āyāt 86-92 du cache canonique ḥafṣ (décalage de un, tranché
R511 ; badge p.171 relu sur rendu image par R524 ET par la sonde indépendante
de l'ouvrier B R522 — convergence double). Les sept āyāt sont rendues en
français sur le cache (présence vérifiée) ; les āyāt 1-85 (leçons 739-760) et
93-110 (leçon 24+) sont interdites de double rendu — les fragments coraniques
hors plage cités par le manuel (entre-les-deux-barrières, plainte, affermisse-
ment) sont rendus en TRADUCTION LIBRE déclarée, jamais mot à mot du cache ;
le rasm nu du cache est interdit au corps (0 arabe — FR-seule)."""
import json
import re
import sys

HTML = "tr-tmp/lesson-761-fr.html"
html = open(HTML, encoding="utf-8").read()
norm = re.sub(r"[ \u202f\u00a0]+", " ", html.replace("&nbsp;", "\u00a0"))
errors = []

# 1. structure et marqueurs
for frag in [
    "Source du cours",
    "Vingt-troisième leçon du second livre du parcours",
    "pages 171 à 178 de l’imprimé miroir",
    "1_20220304_20220304_2251",
    "p.171 ouvre la leçon 23 au badge al-Kahf (85-91)",
    "sonde indépendante de l’ouvrier B (R522, lecture grossie 3,2×)",
    "révision de l’exégèse des āyāt 92 à 97 de la leçon suivante",
    "les objectifs de la leçon 24 ouvrent p.179",
    "Les objectifs de la leçon",
    "Le tamhīd",
    "Le commentaire",
    "La glose",
    "L’extraction des thèmes des āyāt",
    "Premièrement",
    "Deuxièmement",
    "Troisièmement",
    "Les subtilités et les bienfaits",
    "L’évaluation",
    "L’exploitation",
    "la page imprimée 178",
    "la leçon suivante ouvre en la page 179",
    "jamais devinée",
    "interdites de double rendu",
    "plage imprimée (85-91) correspond aux āyāt 86 à 92 du cache canonique",
    "rendus en traduction libre déclarée",
    "tranché R511",
]:
    if frag.lower() not in norm.lower():
        errors.append(f"fragment attendu absent : {frag[:55]}")

# 2. les āyāt 86-92 rendues du cache — présence (7 rendus + 7 numéros imprimés)
cache = json.load(open("scripts-translate/quran-cache.json", encoding="utf-8"))
fr18 = {n: t for n, t in cache["18"]["fr"]}
rendus = [fr18[n] for n in (86, 87, 88, 89, 90, 91, 92)] + [f"({n})" for n in (85, 86, 87, 88, 89, 90, 91)]
rendus_norm = [r.replace("'", "’").replace(" ", "") for r in rendus]
compact = norm.replace(" ", "")
for r in rendus_norm:
    if r not in compact:
        errors.append(f"rendu coranique attendu absent : {r[:55]}")

# 3. contenu attendu (confrontation au manuel — glose, lectures, exégètes)
contenu = [
    "d’autres détails du récit de Dhū al-Qarnayn",
    "la droiture et de la réforme en la terre",
    "les valeurs de la coopération et de l’entraide d’autrui",
    "atteint le couchant du soleil",
    "un peuple mécréant",
    "sa méthode — celle dont il promit l’application",
    "quand il atteignit le levant du soleil",
    "l’entre-les-deux-barrières",
    "il revient à Dieu au Jour de la Résurrection",
    "Il m’a donné force et faveur",
    "De qui le peuple établi entre les deux barrières se plaignit-il à Dhū al-Qarnayn",
    "Quelle solution Dhū al-Qarnayn résolut-il de mettre en œuvre",
    "au sens de mécréance",
    "il menaça les mécréants de son châtiment avant le châtiment de Dieu",
    "le plus proche, celui qui est sensible pour eux",
    "la félicité que Dieu — Très-Haut — a promise aux croyants",
    "la mention de Sa faveur, en la parole de la facilité",
    "la manifestation de sa mécréance et l’espoir de sa conversion à la foi",
    "il ne se hâte point de les faire périr pour leur injustice",
    "le dur, l’immense",
    "le châtié en les deux demeures",
    "la généralité des lecteurs la lut avec l’élévation",
    "l’annexion y est explicative",
    "les croyants n’ont point de récompense sinon la plus belle",
    "Ḥafṣ, Ḥamza et al-Kisāʾī lurent",
    "détachée de l’annexion",
    "complément du verbe absolu",
    "Il les récompense de la récompense du Paradis",
    "al-Farrāʾ la dit",
    "spécification",
    "6/36 — chiffres imprimés inversés",
    "les œuvres salutaires",
    "celui d’entre eux qui crut Dieu en vérité",
    "Nous lui ordonnons ce qui lui est aisé des charges",
    "une parole de douceur et de facilité",
    "Tā-Hā",
    "44 — fragment et renvoi imprimés altérés, tranchés",
    "7/222 tel qu’imprimé",
    "l’extrémité de l’horizon, du côté de l’orient",
    "l’éloignement de la marche de Dhū al-Qarnayn avec son armée",
    "l’extrême couchant du soleil à son extrême levant",
    "Le pronom en « d’elle » renvoie au soleil",
    "il fut dit — les arbres",
    "il fut dit — les montagnes",
    "des tunnels creusés à eux",
    "ils retournaient à leurs gages et leurs cultures",
    "ni par caverne de montagne, ni par maison",
    "comme il parvint au couchant du soleil, il parvint à son levant",
    "comme Nous te l’avons raconté",
    "son lever est semblable à son coucher",
    "l’information de l’embrassement de Dieu",
    "de tout ce que détenait Dhū al-Qarnayn",
    "la troisième étape du voyage de Dhū al-Qarnayn",
    "l’établissement que Dieu lui donna",
    "l’aplanissement qu’il fit des confins de la terre",
    "de l’extrême Occident à l’extrême Orient",
    "La mise à l’accusatif du mot « voie »",
    "al-Anʿām",
    "97 — verset comparatif imprimé altéré",
    "l’élévation de « votre demeure »",
    "Nāfiʿ, Ibn ʿĀmir et ʿĀṣim la lexie des « deux barrières » avec le ḍamm du sīn",
    "Ḥafṣ d’après ʿĀṣim avec le fatḥ",
    "Ibn Kaṯīr « les deux barrières » avec le fatḥ du sīn",
    "al-Kisāʾī dit : ce sont deux langues",
    "Ibn al-Aʿrabī",
    "tout ce qui te fait face, dont ce qui est derrière est obstrué",
    "à l’exemple de la faiblesse à ses deux voyelles",
    "Abū ʿUbayda et Abū ʿAmr b. al-ʿAlāʾ",
    "si elle est de la création de Dieu",
    "de l’ouvrage des serviteurs",
    "rapporté d’ʿIkrima",
    "ce qui s’interpose entre toi et la chose",
    "la membrane de l’œil",
    "ce que tes deux yeux voient est au ḍamm",
    "deux montagnes obstruant les issues de cette contrée de la terre",
    "Dhū al-Qarnayn parcourut les pays, revenant du levant du soleil",
    "un peuple derrière deux montagnes",
    "Yaʾǧūǧ et Maʾǧūǧ les atteignaient, semant la corruption en leur terre",
    "renvoie aux deux montagnes",
    "l’éloignement de leur langue des langues des hommes",
    "une paronomase imparfaite",
    "Ḥamza et al-Kisāʾī « ils font comprendre »",
    "ils n’exposent point aux autres un discours",
    "au sens de savoir",
    "nous ne saisissons point grande chose de ce que tu dis",
    "Hūd",
    "91 — chiffre imprimé inversé « 19 », tranché",
    "un peuple qui n’entend point les autres ni n’en est entendu",
    "la langue d’eux-mêmes",
    "la généralité des lecteurs « Yaʾǧūǧ et Maʾǧūǧ » avec la hamza",
    "l’alléger en la muant en alif",
    "indéclinables, du fait du nom propre et de la non-arabité",
    "la plainte du peuple établi aux deux barrières",
    "lui proposèrent un tribut",
    "reconnu sa puissance, comme il avait reconnu sa droiture",
    "le sauveur de ce qu’ils souffraient de l’hostilité de leurs voisins",
    "leur propagation de la corruption en leur direction",
    "Ibn ʿAṭiyya",
    "l’injustice, la rapacité, le meurtre",
    "Nāfiʿ, Ibn Kaṯīr, Abū ʿAmr et ʿĀṣim « tribut » [au sukūn]",
    "Ḥamza et al-Kisāʾī « tribut » [avec l’alif]",
    "ce que mon Seigneur m’a affermi en quoi est meilleur",
    "d’élever ce qui les protège de Yaʾǧūǧ et Maʾǧūǧ sans exiger de rétribution",
    "conciliation et secours pour eux",
    "acquittement du devoir envers la gouvernance",
    "meilleur que votre tribut et vos biens",
    "aidez-moi de la force des corps",
    "au plus profitable et au plus pur",
    "nul d’entre eux ne l’eût assisté",
    "rivaliserait de durée avec l’ouvrage",
    "la barrière est tout ce dont on obstrue",
    "la pose de la chose sur la chose",
    "pierres, ou terre, ou semblable",
    "quand Dieu lui donna les causes",
    "la complétude de sa confiance en Dieu",
    "prendre les causes de l’établissement, de la victoire et du progrès",
    "l’établissement et la gloire en la terre",
    "l’établissement qu’Il lui donna dans la royauté et l’élargissement en la richesse",
    "la mobilisation générale",
    "une politique sage où il mit à profit leur ardeur",
    "bien commun dont le profit reviendrait aux générations",
    "les associer à la protection de leur pays",
    "les éduquer au travail et au non-repos sur autrui",
    "de leur poser une barrière, et il leur promit d’élever pour eux un rempart",
    "la différence entre la barrière et le rempart",
    "aidez-moi de force",
    "il regarde en leurs affaires et se charge de leurs intérêts",
    "garder leur quartier, obstruer leur brèche et réparer leur trou",
    "les événements firent paraître des chefs qui se sacrifièrent eux-mêmes avant leurs biens",
    "dépensés du meilleur gouvernement",
    "je n’ai nul besoin de lui",
    "servez avec moi de vos personnes",
    "les biens sont auprès de moi, et les hommes auprès de vous",
    "le dévouement au service des corps fut le plus droit",
    "3/342 tel qu’imprimé",
    "Je reformule les teneurs du texte en mon style propre",
    "quelques droits de la communauté sur son pasteur",
    "protéger la sûreté de ses patries",
    "la révision de l’exégèse des āyāt 92 à 97",
    "badge p.179 relu sur rendu image R523",
    "convergence double",
    "STARTS +171 (R522) et +179 (R523)",
]
for c in contenu:
    if c.lower() not in norm.lower():
        errors.append(f"contenu attendu absent : {c[:55]}")

# 4. rendus interdits (āyāt 1-85 livrées leçons 739-760 ; 93-110 leçon 24+)
interdits_src = (1, 10, 32, 45, 46, 57, 59, 60, 62, 65, 66, 71, 72, 73, 74,
                 78, 79, 82, 83, 84, 85, 93, 94, 95, 98, 102, 110)
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
for n in list(range(1, 86)) + list(range(93, 111)):
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

total = 25 + len(rendus) + len(contenu) + len(interdits) + rasm_n + 3
print(f"verify-761-quran : {total} contrôles — rendus {len(rendus)} + contenu {len(contenu)} + interdits {len(interdits)} + rasm {rasm_n} + structure {25} + typo 3")
if errors:
    print("verify-761 FAIL :")
    for e in errors:
        print(" -", e)
    sys.exit(1)
print("verify-761 PASS")

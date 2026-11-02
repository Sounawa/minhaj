#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Minhāj — contrôle coranique et de contenu de la leçon 758 (tafsir-5ep,
sūrat al-Kahf v73-77 de l'imprimé warš — vingtième leçon du second livre,
pages 150-156 du manuel miroir tafsir-3-thanawi). La plage imprimée (73-77)
correspond aux āyāt 74-78 du cache canonique ḥafṣ (décalage de un, tranché
R511). Les cinq āyāt sont rendues en français sur le cache (présence vérifiée) ;
les āyāt 1-73 (leçons 739-757) et 79-110 (leçons suivantes) sont interdites de
double rendu ; le rasm nu du cache interdit au corps (0 arabe — FR-seule)."""
import json
import re
import sys

HTML = "tr-tmp/lesson-758-fr.html"
html = open(HTML, encoding="utf-8").read()
norm = re.sub(r"[ \u202f\u00a0]+", " ", html.replace("&nbsp;", "\u00a0"))
errors = []

# 1. structure et marqueurs
for frag in [
    "Source du cours",
    "Vingtième leçon du second livre du parcours",
    "pages 150 à 156 de l’imprimé miroir",
    "1_20220304_20220304_2251",
    "p.150 ouvre la leçon 20 au badge al-Kahf (73-77)",
    "l’ʾiʿdād qiblī de p.156 porte la révision",
    "les objectifs de la leçon 21 ouvrent p.157",
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
    "la page imprimée 156",
    "jamais devinée",
    "interdites de double rendu",
    "plage imprimée (73-77) correspond aux āyāt 74 à 78 du cache canonique",
    "l’opposition de Mūsā envers lui au perçage du navire",
    "kahf-probe-l20.py",
]:
    if frag.lower() not in norm.lower():
        errors.append(f"fragment attendu absent : {frag[:55]}")

# 2. les āyāt 74-78 rendus du cache — présence (5 rendus + 5 numéros imprimés)
cache = json.load(open("scripts-translate/quran-cache.json", encoding="utf-8"))
fr18 = {n: t for n, t in cache["18"]["fr"]}
rendus = [fr18[n] for n in (74, 75, 76, 77, 78)] + [f"({n})" for n in (73, 74, 75, 76, 77)]
rendus_norm = [r.replace("'", "’").replace(" ", "") for r in rendus]
compact = norm.replace(" ", "")
for r in rendus_norm:
    if r not in compact:
        errors.append(f"rendu coranique attendu absent : {r[:55]}")

# 3. contenu attendu (confrontation au manuel — glose, lectures, exégètes)
contenu = [
    "les deux autres actes d’al-Khiḍr auxquels Mūsā",
    "les fondements de l’opposition de Mūsā",
    "la valeur de la préservation de la vie et de l’hospitalité envers l’hôte",
    "quand Mūsā le compagnonna",
    "la condition de la non-interrogation",
    "les deux actes qu’al-Khiḍr accomplit",
    "l’issue de cette opposition",
    "la lexie du maçon portent un même sens",
    "l’origine de la lexie du maçon est l’élévation",
    "sa chute est proche",
    "le ḥadīṯ d’al-Khiḍr l’a explicité par « incliné »",
    "Quel est le second acte d’al-Khiḍr auquel Mūsā s’est opposé",
    "Pourquoi Mūsā s’est-il opposé à al-Khiḍr en l’affaire de l’élévation du mur",
    "al-Kisāʾī dit que les deux lexies portent un même sens",
    "aṮaʿlab dit que [celle sans alif] est plus éloquente",
    "Abū ʿAmr a distingué entre les deux lexies",
    "6/51",
    "elle était petite et n’avait point encore atteint le péché",
    "7/802",
    "de rétribution légale en contre d’une vie",
    "une vie pour une vie",
    "al-Māʾida : 45 — renvoi imprimé tranché",
    "la masse des lecteurs lit « une chose inouïe » au sukūn du kāf",
    "au ḍamm du kāf chez Ibn Ḏakwān, Abū Jaʿfar et Yaʿqūb",
    "le navire",
    "la brèche — car la brèche se peut obstruer",
    "il n’y a point de voie au rattrapage de la vie avec elle",
    "des secrets du mystère que Dieu lui a enseignés et lui a dévoilés",
    "n’est point du domaine de la législation",
    "jugeant selon les exigences du Droit",
    "les législations célestes sont unanimes à la préservation de la vie",
    "l’addition du pronom d’attribution en le discours d’al-Khiḍr à Mūsā",
    "la formule de la leçon précédente n’en portait point",
    "le zajr, la réprimande, et le durcissement sans adoucissement",
    "après ce récit, ou après cette question",
    "ne me fais plus ton compagnon, et n’attire pas la séparation entre moi et toi",
    "c’est une condition, et elle est obligatoire",
    "que soit honoré ce que les prophètes se sont imposé",
    "un fondement en la doctrine des conditions et du lien des jugements à elles",
    "l’on en argumente aux serments et autres",
    "6/71",
    "tu as atteint une mesure à laquelle [l’accomplissement] devient impossible",
    "l’excuse vaut une fois pour toutes",
    "la preuve est définitive dès la seconde fois",
    "3/832",
    "un fondement des délais en les jugements",
    "les jours du blâme sont trois",
    "le délai que le juge accorde pour la production de la preuve",
    "Ibn Kaṯīr, Abū ʿAmr, Ibn ʿĀmir, Ḥamza et al-Kisāʾī lurent au léger",
    "au ḍamm du dāl avec l’allègement du nūn",
    "à la fatḥa du lām et au sukūn du dāl",
    "le plus beau y est le redoublement du nūn",
    "quand on l’annexe, on adjoint un nūn préservant le sukūn de la première nūn",
    "de [la part] de Zayd",
    "ils l’ont réduit comme en la lexie de l’épaule, supprimant la ḍamma",
    "Zād al-Masīr",
    "une élision que le rang du discours exige",
    "al-Khiḍr s’employant à l’affaire où exécuter ce qu’il tenait de la science de Dieu",
    "jusqu’à ce qu’ils passèrent par une cité dont ils demandèrent la nourriture",
    "l’on a divergé en la détermination de la cité mentionnée",
    "selon la divergence en quelle contrée de la terre eut lieu le récit de Mūsā",
    "Dieu seul connaît la vérité de cela",
    "les héberger tous deux en hôtes honorés et honorer leur venue",
    "la demande de la nourriture — visée ici : la demande de l’hospitalité",
    "à preuve sa parole « ils refusèrent de les recevoir »",
    "rattachés à la lâcheté et à l’avarice",
    "la pire des cités est celle qui n’héberge point l’hôte",
    "ne connaît point le droit de l’hôte de passage",
    "l’hospitalité leur était obligatoire",
    "ne demandèrent que ce qui leur était dû d’hospitalité",
    "à la condition des prophètes et au rang des vertueux et des amis de Dieu",
    "6/81",
    "l’attribution de la volonté au mur est une métaphore explicite",
    "la résolution d’accomplir l’acte, chez les gens de raison",
    "il le poussa de sa main et il se dressa droit",
    "6/91",
    "Ibn Kaṯīr et Abū ʿAmr lurent à la kasra du khāʾ",
    "Abū ʿAmr assimilant le dhāl, et Ibn Kaṯīr l’exposant",
    "lurent Nāfiʿ, ʿĀṣim, Ibn ʿĀmir, Ḥamza et al-Kisāʾī sans la kasra",
    "tous assimilèrent le dhāl, excepté Ḥafṣ ʿan ʿĀṣim",
    "il n’assimila point, à l’exemple d’Ibn Kaṯīr",
    "on dit « takhidha » au sens de « il prit »",
    "vint de Mūsā en question, à la manière de la proposition, non de l’opposition",
    "6/32",
    "la preuve de la licéité du louage de service",
    "une coutume établie en sūrat al-Qaṣaṣ, selon son exposé",
    "le visé y est l’opposition contre toi, au titre de ce que tu stipulas comme condition",
    "sa répétition « entre moi » et « entre toi »",
    "sa déviation hors de « entre nous », au sens de l’affirmation",
    "la parole de Mūsā sur le navire et sur le garçon était pour Dieu",
    "sa parole sur le mur était pour demander quelque chose du monde",
    "elle fut donc cause de la séparation",
    "11/33",
    "de la fin de la compagnie, ne restant sur lui",
    "l’accomplissement de sa promesse de l’informer de l’interprétation",
    "je t’informerai de la sagesse et de l’issue de ces trois affaires",
    "la brèche du navire, le meurtre du garçon et l’élévation du mur",
    "l’origine du terme de l’interprétation retourne à leur dire",
    "l’exposé, la clarification et l’explicitation",
    "afin que Dieu nous raconte de l’affaire de tous deux",
    "kitāb tafsīr al-Qurʾān, bāb (et quand Moïse dit à son valet)",
    "pièce suspendue, tel qu’imprimé",
    "le second récit n’était que délibéré",
    "qu’est-ce donc qui portait [Mūsā] à violer la condition",
    "le navire avait des gens et une voie de perdition manifeste",
    "l’opposition [de Mūsā] avait donc lieu",
    "le meurtre du second était délibéré et manifeste",
    "il n’endura donc point, et s’excusa par l’oubli",
    "en se rappelant la condition, la violant délibérément",
    "en donnant priorité au jugement du Droit",
    "il est d’habitude que cela soit éprouvé en son épreuve manifeste",
    "Fatḥ al-Bārī : 11/455 tel qu’imprimé",
    "le « entre » de la séparation n’est point le « entre » des deux surfaces",
    "emprunté à l’usage adverbial",
    "la lecture de « zākiya » à l’alif et de « zakiya » sans elle",
    "qu’est-ce qui incombe à l’homme envers ses conditions",
    "des jugements et des valeurs extraits des āyāt de la leçon",
    "une charge que te prendrait l’un des gens de la cité",
    "nous sommes en besoin de ce que nous dépensons sur nos âmes",
    "en droit de l’étroitesse",
    "une demande impliquant un blâme",
    "sa seule élévation étant gratuite",
    "al-Taḥrīr wa-t-Tanwīr",
    "avec remaniement",
    "Je lis le texte avec soin, puis je réponds",
    "ce qui est souligné de trait dans le texte",
    "l’hospitalité envers l’hôte est de la foi, et des nobles mœurs",
    "cache 79 et suivantes",
    "NUM imprimé inversé relu (78-81) en l’ʾiʿdād qiblī de p.156",
    "la leçon suivante ouvre en la page 157 du même manuel",
    "la citation coranique de p.151 délimitant la plage imprimée (73 _ 77)",
    "l’ouverture des objectifs de la leçon 21 en p.157",
    "convergence — jamais devinée",
]
for c in contenu:
    if c.lower() not in norm.lower():
        errors.append(f"contenu attendu absent : {c[:55]}")

# 4. rendus interdits (āyāt 1-73 livrées leçons 739-757 ; 79 leçon suivante)
interdits_src = (1, 10, 32, 45, 46, 57, 65, 66, 67, 68, 69, 70, 71, 72, 73, 79)
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
for n in list(range(1, 74)) + list(range(79, 111)):
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

total = 24 + len(rendus) + len(contenu) + len(interdits) + rasm_n + 3
print(f"verify-758-quran : {total} contrôles — rendus {len(rendus)} + contenu {len(contenu)} + interdits {len(interdits)} + rasm {rasm_n} + structure {24} + typo 3")
if errors:
    print("verify-758 FAIL :")
    for e in errors:
        print(" -", e)
    sys.exit(1)
print("verify-758 PASS")

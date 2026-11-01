#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Minhāj — contrôle coranique et de contenu de la leçon 741 (tafsir-5ep,
sūrat al-Kahf v10-14 — troisième leçon du second livre, pages 23-28 du manuel
miroir tafsir-3-thanawi). Les āyāt 10-14 sont rendues en français sur le rasm
warš du cache (présence vérifiée) ; le rasm nu du cache interdit au corps
(0 arabe — FR-seule) ; les āyāt des autres leçons interdites au rendu français
comme au rasm (les rendus de la leçon 740 — āyāt 6-9 — absents ; l'āya 15,
ouverture de la leçon 4, ne peut être ni rendue ni citée en rasm ; le rendu du
cache des āyāt 9 et 15 absent) ; contrôle de contenu : le lemme « jeunes gens »
(fata, fitya — pluriel de la petite quantité —, fityān — pluriel de la grande
quantité —, shabāb proches d'âge), la divergence sur l'identité (les Rūm,
avant ʿĪsā, autre), l'abri et le lieu d'attache, la miséricorde comme
subsistance, les deux lectures du lemme (r-r-š-d) (rashadā, rushdā — la
majorité des lecteurs, le parallèle des clausules), Ibn ʿAṭiyya (l'invocation
d'ici-bas, elle suffit), la sollicitude pour la religion (paganisme, idoles),
la métonymie du frappement, la spécialisation des oreilles, le hadith de
l'oreille (Ṣaḥīḥ al-Bukhārī, livre du tahajjud), la grammaire de « sinīn »
(pluriel masculin sain, yāʾ substituée à la fatḥa), az-Zaǧǧāǧ (le nom verbal),
az-Zuhrī (li-yuʿlama, à la yāʾ), les deux partis (les jeunes gens, les gens de
la ville), Abū Isḥāq az-Zaǧǧāǧ (la distinction à l'accusatif sur
l'interprétation, la mesure du quadrilittère), les exemples descriptifs
(al-Muwaṭṭaʾ — Ǧahannam ; Ṣaḥīḥ al-Bukhārī — le bassin), ʿUmar b. al-Khaṭṭāb,
Ibn ʿAṭiyya (le quadrilittère), aṭ-Ṭabarī (deux aspects, Jāmiʿ al-bayān),
ar-Rāzī (Mafātīḥ al-ghayb — la manière d'épreuve, la plaine dénudée), les
subtilités (le sommeil et le réveil comme deux āyāt, l'invocation des
prophètes et des awliyāʾ, l'invocation par la miséricorde et la conduite
droite), l'investissement d'Ibn ʿĀshūr (at-Taḥrīr wa-t-tanwīr — la fāʾ de la
conséquence, la kārāma), la structure (objectifs, tamhīd, commentaire,
subtilités, évaluation, exploitation, Source du cours), 0 arabe résiduel
(ﷺ exempté)."""
import json
import re
import sys

HTML = "scripts-translate/tr-tmp/pdf-mut23h3c-741.html"
html = open(HTML, encoding="utf-8").read()
norm = re.sub(r"[ \u202f\u00a0]+", " ", html.replace("&nbsp;", "\u00a0"))
errors = []

# 1. structure et marqueurs
if "Source du cours" not in norm:
    errors.append("Source du cours absent du DOM")
for frag in [
    "Troisième leçon du second livre du parcours",
    "tafsir-3-thanawi_text.pdf",
    "mécanique R458",
    "jamais devinées",
    "Les objectifs de la leçon",
    "Le tamhīd",
    "Le commentaire",
    "Les subtilités et les bienfaits",
    "L’évaluation",
    "L’exploitation",
    "la présente passe l’a relue in extenso",
]:
    if frag not in norm:
        errors.append(f"fragment attendu absent : {frag[:55]}")

# 2. les āyāt 10-14 rendues en français (rasm warš du cache) — présence
rendus = [
    "Quand les jeunes gens se furent réfugiés dans la Caverne, ils dirent : Seigneur, donne-nous de Ta part une miséricorde, et prépare-nous de notre affaire une conduite droite.",
    "Nous frappâmes alors sur leurs oreilles, dans la Caverne, des années comptées.",
    "Puis Nous les ressuscitâmes, afin de savoir lequel des deux partis saurait le mieux compter la durée de leur séjour.",
    "C’est Nous qui te rapportons leur récit en vérité : ils furent des jeunes gens qui crurent en leur Seigneur, et Nous accrus leur guidée.",
    "Et Nous affermîmes leurs cœurs lorsqu’ils se dressèrent et dirent : Notre Seigneur est le Seigneur des cieux et de la terre — nous n’appellerons jamais de divinité en dehors de Lui ; sans quoi, nous aurions proféré un excès.",
    "(10-14)",
]
for r in rendus:
    if r not in norm:
        errors.append(f"rendu coranique attendu absent : {r[:55]}")

# 3. contenu : lemmes, lectures, mufassirūn, grammaire, subtilités, investissement
contenu = [
    "pluriel de la petite quantité",
    "pluriel de la grande quantité",
    "proches d’âge",
    "Rūm",
    "la religion de ʿĪsā, sur lui la paix",
    "avant ʿĪsā, sur lui la paix",
    "un abri et un lieu d’attache",
    "la subsistance",
    "(r-r-š-d)",
    "rashadā",
    "rushdā",
    "deux fatḥa",
    "la majorité des lecteurs",
    "parallèle des clausules",
    "Ibn ʿAṭiyya",
    "elle suffit",
    "la sollicitude qu’ils eurent pour leur religion",
    "paganisme et de l’adoration des idoles",
    "la sincérité de la foi",
    "la possibilité du réveil",
    "la possibilité de la résurrection et de sa manière",
    "métonymie du frappement sur les oreilles",
    "sommeil profond",
    "la force de l’agir direct",
    "l’organe dont la ruine du sommeil est la plus grande",
    "le démon venant au dormeur en son oreille",
    "Ṣaḥīḥ al-Bukhārī",
    "livre du tahajjud",
    "pluriel masculin sain",
    "la yāʾ substituée à la fatḥa",
    "az-Zaǧǧāǧ",
    "au sens du nom verbal",
    "az-Zuhrī",
    "li-yuʿlama",
    "à la yāʾ",
    "des gens de la ville",
    "la datation se faisait",
    "du commun des mufassirūn",
    "un verbe du passé",
    "Abū Isḥāq az-Zaǧǧāǧ",
    "à l’accusatif sur l’interprétation",
    "quadrilittère",
    "al-Muwaṭṭaʾ",
    "Ǧahannam",
    "goudron et de la poix",
    "blanche comme le lait",
    "cœurs attendris",
    "ʿUmar b. al-Khaṭṭāb",
    "la force de la prière",
    "aṭ-Ṭabarī",
    "Jāmiʿ al-bayān",
    "ar-Rāzī",
    "Mafātīḥ al-ghayb",
    "par manière d’épreuve",
    "plaine dénudée vide de tout",
    "trois cents années et plus",
    "une kārāma pour eux",
    "la fāʾ de la conséquence",
    "at-Taḥrīr wa-t-tanwīr",
    "la législation de l’invocation",
    "le salut des épreuves",
    "depuis l’āya 6",
    "une métaphore explicite",
    "l’étape d’âge",
    "(15-16)",
    "(13-16)",
    "(10-12)",
]
for c in contenu:
    if c not in norm:
        errors.append(f"contenu attendu absent : {c[:55]}")

# 4. ABSENCE — rasm nu du cache interdit (FR-seule), āyāt voisines et leçons voisines
cache = json.load(open("scripts-translate/quran-cache.json", encoding="utf-8"))
rasm_18 = {n: t for n, t in cache["18"]["ar"]}
for n in (9, 10, 11, 12, 13, 14, 15):
    t = rasm_18[n]
    probes = [t, t.replace(" ", "")]
    ok = any(p in norm.replace(" ", "") for p in probes) or t in norm
    if ok:
        errors.append(f"rasm arabe interdit présent au corps (āya 18:{n})")
for probe in [
    "une chose étonnante",
    "Ou bien penses-tu",
    "par affliction",
    "te consumer",
    "sol aride",
    "parure pour elle",
    "ont constitué une chose extraordinaire",
    "nos concitoyens",
    "une preuve évidente",
    "Quel pire injuste",
    "adopté en dehors de Lui des divinités",
    "Louange à Allah qui a fait descendre",
    "violence sévère",
    "Grave comme parole",
]:
    if probe in norm:
        errors.append(f"rendu hors matière présent : {probe[:50]}")

# 5. 0 arabe résiduel (ﷺ U+FDFA exempté, convention du corpus)
ARABIC = re.compile(r"[\u0600-\u06FF\u0750-\u077F\u08A0-\u08FF\uFB50-\uFDF9\uFDFB-\uFDFF\uFE70-\uFEFF]")
resid = ARABIC.findall(norm)
if resid:
    errors.append(f"arabe résiduel : {len(resid)} caractère(s), ex. {[c for c in resid[:5]]}")

if errors:
    print("verify-741 FAIL :")
    for e in errors:
        print(" -", e)
    sys.exit(1)
print("verify-741 PASS — structure OK, 5 rendus warš présents (18:10-14), contenu complet, 0 rasm étranger, 0 arabe résiduel (ﷺ exempté)")

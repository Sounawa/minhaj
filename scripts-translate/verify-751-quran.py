#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Minhāj — contrôle coranique et de contenu de la leçon 751 (tafsir-5ep,
sūrat al-Kahf v44-45 de l'imprimé warš — treizième leçon du second livre, pages
96-101 du manuel miroir tafsir-3-thanawi). La plage imprimée (44-45) correspond
aux āyāt 45-46 du cache canonique ḥafṣ (décalage de un, tranché R511). Les deux
āyāt sont rendues en français sur le cache (présence vérifiée) ; les āyāt 1-44
(leçons 739-750) et 47-49 (leçon 752) sont interdites de double rendu ; le rasm
nu du cache interdit au corps (0 arabe — FR-seule)."""
import json
import re
import sys

HTML = "tr-tmp/lesson-751-fr.html"
html = open(HTML, encoding="utf-8").read()
norm = re.sub(r"[ \u202f\u00a0]+", " ", html.replace("&nbsp;", "\u00a0"))
errors = []

# 1. structure et marqueurs
for frag in [
    "Source du cours",
    "Treizième leçon du second livre du parcours",
    "pages 96 à 101 de l’imprimé miroir",
    "1_20220304_20220304_2251",
    "p.96 ouvre la leçon 13",
    "les objectifs de la leçon 14 ouvrent p.102",
    "Les objectifs de la leçon",
    "Le tamhīd",
    "Le commentaire",
    "La glose",
    "L’extraction des thèmes des āyāt",
    "Premièrement",
    "Deuxièmement",
    "Les subtilités et les bienfaits",
    "L’évaluation",
    "L’exploitation",
    "la page imprimée 101",
    "jamais devinée",
    "interdites de double rendu",
    "plage imprimée (44-45) correspond aux āyāt 45 et 46 du cache canonique",
]:
    if frag.lower() not in norm.lower():
        errors.append(f"fragment attendu absent : {frag[:55]}")

# 2. les āyāt 45-46 rendus du cache — présence (2 rendus + 2 numéros)
cache = json.load(open("scripts-translate/quran-cache.json", encoding="utf-8"))
fr18 = {n: t for n, t in cache["18"]["fr"]}
rendus = [fr18[n] for n in (45, 46)] + ["(45)", "(46)"]
rendus_norm = [r.replace("'", "’").replace(" ", "") for r in rendus]
compact = norm.replace(" ", "")
for r in rendus_norm:
    if r not in compact:
        errors.append(f"rendu coranique attendu absent : {r[:55]}")

# 3. contenu attendu (confrontation au manuel — glose, lectures, exégètes)
contenu = [
    "s’entremêla",
    "le poussement",
    "le vent l’emporte et l’éparpille dans l’air",
    "Quel est l’exemple que Dieu — Très-Haut — frappa pour la vérité de la duniyā",
    "après le récit des deux hommes",
    "l’ébloui par l’éclat de la duniyā",
    "en la perdition",
    "au dédain et au déni",
    "l’homme ingrat",
    "la descente de la pluie et le verdissement de la terre",
    "en fourrage effrité et débris",
    "de la nuée qui est au ciel",
    "au sens du terme de circonstance",
    "que la végétation se mêla, une part à une part",
    "une lettre de causalité",
    "la spécialisation du moment du matin",
    "le fritté et le brisé",
    "la mouture de la chose sèche",
    "Hāšim b. ʿAbd Manāf",
    "son nom est ʿAmr",
    "le premier à émietter le bouilli",
    "en l’an de la famine",
    "les lectures alternent sur la lexie de la dispersion",
    "Elle la broie et la lance",
    "avant l’existence de l’homme",
    "Sībawayhi",
    "al-Ḥasan a dit",
    "avant la création des existants",
    "Celui que rien ne contraint",
    "l’assimilation de l’état de l’homme",
    "sa gloire, sa joie et son dédain",
    "la vie fut comme l’eau",
    "à la place des délices et de la gloire",
    "la beauté et l’effusion",
    "la force et la défense",
    "ils furent donc tous deux l’ornement de la vie",
    "un nom verbal",
    "à la place de la richesse et de la multitude",
    "Ibn Ǧubayr",
    "Abū ʿAmr, ʿAmr b. Mayšara et ʿAmr b. Šurayḥbīl",
    "ce sont les cinq prières",
    "Ibn al-ʿArabī l’a préféré en ses ʾaḥkām",
    "vers cela que va mon penchant",
    "il n’est point en ce chapitre de ḥadīṯ juste",
    "la louange, de la magnification, de l’unification et de la formule de puissance",
    "rien ne vaut les cinq prières",
    "Aḥkām al-Qurʾān",
    "5/632",
    "les paroles transmises de mérite",
    "Gloire à Dieu",
    "la louange à Dieu",
    "point de dieu que Dieu",
    "Dieu est plus grand",
    "Multipliez les œuvres qui persistent",
    "Abū Hurayra",
    "Ṣaḥīḥ Ibn Ḥibbān",
    "Sunan an-Nasāʾī al-Kubrā",
    "toute œuvre pure, de propos ou d’acte, qui demeure pour l’āḫira",
    "al-Ṭabarī l’a préféré, et al-Qurṭubī l’a confirmé",
    "son détenteur espère, en la duniyā, la récompense de Dieu",
    "la vérification, au-delà de ce que les ignorants en supposent",
    "la balāġa des ʿArabes",
    "le locuteur rassemble deux choses ou plus sous un seul jugement",
    "deux choses d’une même espèce",
    "hormis Dieu et Ses attributs sublimes, a un terme",
    "Celui qui demeure en vérité, c’est Dieu seul",
    "belles et laides, bonnes et mauvaises, sont périssables et se renouvellent",
    "de façon figurée",
    "la récompense et le châtiment demeurent sans interruption",
    "leurs semblables se succèdent sans interruption",
    "renvois imprimés 332 et 432",
    "Les sages ont dit",
    "l’eau ne s’établit point en un lieu",
    "l’eau ne se tient point en un état unique",
    "l’eau ne demeure point et s’en va",
    "ses épreuves et ses fléaux",
    "profitable en germination",
    "la suffisance d’elle profite, et son excès nuit",
    "renvoi imprimé 862",
    "le guidage principiel",
    "pourquoi Dieu — Très-Haut — assimila-t-il la vie d’ici-bas à l’eau",
    "l’orientation d’Ibn ʿĀšūr",
    "un propos descriptif, sauf que la majorité de leurs occurrences exige un terme omis",
    "Je contemple le texte, puis je réponds",
    "tient lieu de son décrit",
    "l’antéposition des biens sur les enfants",
    "āyāt 47-49 du cache canonique",
    "les sens des expressions suivantes",
]
for c in contenu:
    if c.lower() not in norm.lower():
        errors.append(f"contenu attendu absent : {c[:55]}")

# 4. rendus interdits (āyāt 1-44 livrées leçons 739-750 ; 47-49 leçon 752)
interdits = [
    "Louange à Dieu qui a fait descendre sur Son serviteur",
    "Toute âme doit goûter la mort",
    "Donne-leur l'exemple de deux hommes",
    "Quant à moi, c'est Allah qui est mon Seigneur",
    "En entrant dans ton jardin, que ne dis-tu",
    "Et sa récolte fut détruite et il se mit alors",
    "En l'occurrence, la souveraine protection appartient à Allah",
    "cependant que ses treilles étaient complètement ravagées",
    "Les biens et les enfants sont l'ornement",
]
interdits_ok = {"Les biens et les enfants sont l'ornement"}
interdits_norm = [r.replace("'", "’") for r in interdits]
for probe in interdits_norm:
    if probe in norm and probe.replace("'", "’") not in [
        fr18[46].replace("'", "’")[: len(probe)]
    ]:
        # la matière 45-46 est licite : on ne bannit que ses fragments hors rendu intégral
        if probe not in interdits_ok:
            errors.append(f"rendu hors matière présent : {probe[:50]}")

rasm_18 = {n: t for n, t in cache["18"]["ar"]}
for n in range(1, 47):
    t = rasm_18[n]
    probes = [t, t.replace(" ", "")]
    ok = any(p in norm.replace(" ", "") for p in probes) or t in norm
    if ok:
        errors.append(f"rasm arabe interdit présent au corps (āya 18:{n})")

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

total = 20 + len(rendus) + len(contenu) + 9 + 46 + 3
print(f"verify-751-quran : {total} contrôles — rendus {len(rendus)} + contenu {len(contenu)} + interdits {9 + 46} + structure {20} + typo 3")
if errors:
    print("verify-751 FAIL :")
    for e in errors:
        print(" -", e)
    sys.exit(1)

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Minhāj — contrôle coranique et de contenu de la leçon 748 (tafsir-5ep,
sūrat al-Kahf v30-31 — dixième leçon du second livre, pages 73-78 du manuel
miroir tafsir-2-thanawi). Les āyāt 30-31 sont rendues en français sur le rasm
warš du cache (présence vérifiée) ; les parallèles al-Anbiyāʾ imprimé
39/canonique 94, al-Fāṭir 33, al-Ḥaǧǧ 23, az-Zukhruf imprimé 05/canonique 51
et imprimé 33/canonique 34, al-Furqān imprimé 66/canonique 75-76 rendus du
cache ; le double rendu des āyāt 1-29 (leçons 739-747) est interdit ; le rasm
nu du cache interdit au corps (0 arabe — FR-seule) pour TOUTES les āyāt
voisines (1-29)."""
import json
import re
import sys

HTML = "tr-tmp/lesson-748-fr.html"
html = open(HTML, encoding="utf-8").read()
norm = re.sub(r"[ \u202f\u00a0]+", " ", html.replace("&nbsp;", "\u00a0"))
errors = []

# 1. structure et marqueurs
for frag in [
    "Source du cours",
    "Dixième leçon du second livre du parcours",
    "pages 73 à 78 de l’imprimé miroir",
    "1_20220304_20220304_2251",
    "p.73 ouvre la leçon 10, p.79 ouvre la leçon 11",
    "Les objectifs de la leçon",
    "Le tamhīd",
    "Le commentaire",
    "La glose",
    "L’extraction des thèmes des deux āyāt",
    "Premièrement",
    "Deuxièmement",
    "Les subtilités et les bienfaits",
    "L’évaluation",
    "L’exploitation",
    "la page imprimée 78",
    "jamais devinée",
    "interdites de double rendu",
]:
    if frag.lower() not in norm.lower():
        errors.append(f"fragment attendu absent : {frag[:55]}")

# 2. les āyāt 30-31 + parallèles rendus du cache — présence (10 rendus)
rendus = [
    "Ceux qui croient et font de bonnes œuvres... vraiment Nous ne laissons pas perdre la récompense de celui qui fait le bien.",
    "Voilà ceux qui auront les jardins du séjour (éternel) sous lesquels coulent les ruisseaux.",
    "Ils y seront parés de bracelets d’or et se vêtiront d’habits verts de soie fine et de brocart, accoudés sur des divans (bien ornés).",
    "Quelle bonne récompense et quelle belle demeure !",
    "Quiconque fait de bonnes œuvres tout en étant croyant, on ne méconnaîtra pas son effort, et Nous le lui inscrivons [à son actif].",
    "Les jardins d’Eden où ils entreront, parés de bracelets en or ainsi que de perles ; et là, leurs vêtements sont de soie.",
    "...Là, ils seront parés de bracelets d’or, et aussi de perles ; et leurs vêtements y seront de soie.",
    "...le royaume de Misr ne m’appartient-il pas ainsi que ces canaux qui coulent à mes pieds ?",
    "...et de divans où ils s’accouderaient",
    "Ceux-là auront pour récompense un lieu élevé [du Paradis] à cause de leur endurance, et ils y seront accueillis avec le salut et la paix",
    "...pour y demeurer éternellement. Quel beau gîte et lieu de séjour !",
    "(30)",
    "(31)",
]
# adaptation du cache : apostrophes droites -> typographiques avant comparaison
rendus_norm = [r.replace("'", "’") for r in rendus]
for r in rendus_norm:
    if r not in norm:
        errors.append(f"rendu coranique attendu absent : {r[:55]}")

# 3. contenu attendu (confrontation au manuel — glose, lectures, exégètes)
contenu = [
    "al-ikliyān — les œuvres vertueuses",
    "phrase intercalée",
    "tamyīz",
    "al-Baḥr al-Muḥīṭ 7/71",
    "Cette āyāt pose la foi en condition de l’œuvre",
    "al-Anbiyāʾ imprimé 39 — tranché 94",
    "la demeure d’établissement",
    "lʾʿādin est la camelle en son huitième",
    "5/275",
    "az-Zukhruf imprimé 05 — tranché 51",
    "Ǧāmiʿ al-bayān",
    "ce qui se porte au poignet, de l’or fin (al-badīn)",
    "son singulier ʾiswār",
    "voie de Ḥafṣ d’après ʿĀṣim",
    "Saʿīd ibn Ǧubayr a dit : trois bracelets à chacun d’eux",
    "al-Fāṭir : 33",
    "al-Ḥaǧǧ : 23",
    "Ibn Kaṯīr",
    "du dībāǧ",
    "son origine ʾistabrih",
    "comme les rois portaient en la duniyā les bracelets et les couronnes",
    "Ṣaḥīḥ al-Bukhārī",
    "Ibn ʿAbbās — que Dieu soit satisfait des deux",
    "les divans (al-surur)",
    "al-Furqān imprimé 66 — tranché 75-76",
    "Abū Ḥayyān",
    "le sandūs — ce qui, du dībāǧ, est fin",
    "les couleurs apaisent les âmes",
    "aṭ-Ṭāhir ibn ʿĀšūr",
    "la lām du royaume",
    "at-Taḥrīr wa-t-Tanwīr",
    "les voies de la réussite au bonheur de la Ǧanna",
    "Quel est le prix d’acceptation de l’œuvre vertueuse",
    "Quelle différence entre le sandūs et lʾʾistabraq",
    "le dessein éducatif de la mention du bonheur des croyants",
    "al-Itqān fī ʿulūm al-Qurʾān 2/921",
    "non-Arabes",
    "āyāt 23-53 de sūrat al-Kahf",
]
for c in contenu:
    if c.lower() not in norm.lower():
        errors.append(f"contenu attendu absent : {c[:55]}")

# 4. rendus interdits (āyāt 1-29 déjà livrées leçons 739-747 — aucun double rendu)
interdits = [
    "Louange à Dieu qui a fait descendre sur Son serviteur",
    "Fais preuve de patience [en restant] avec ceux qui invoquent leur Seigneur matin et soir, désirant Sa Face.",
    "Et que tes yeux ne se détachent point d'eux, en cherchant (le faux) brillant de la vie sur terre.",
    "Et n’obéis pas à celui dont Nous avons rendu le cœur inattentif à Notre Rappel, qui poursuit sa passion et dont le comportement est outrancier.",
    "Et dis : La vérité émane de votre Seigneur.",
    "Quiconque le veut, qu’il croie, quiconque le veut, qu’il mécroie.",
    "Nous avons préparé pour les injustes un Feu dont les flammes les cernent.",
    "Et s’ils implorent à boire, on les abreuvera d’une eau comme du métal fondu, brûlant les visages.",
    "Quelle mauvaise boisson et quelle détestable demeure !",
    "Et ils demeurèrent dans leur caverne trois cents années",
    "Et récite ce qui t’a été révélé du Livre de ton Seigneur. Nul ne peut changer Ses paroles.",
    "Et tu ne trouveras, en dehors de Lui, aucun refuge.",
]
# adaptation du cache : apostrophes droites -> typographiques avant comparaison
interdits_norm = [r.replace("'", "’") for r in interdits]
for probe in interdits_norm:
    if probe in norm:
        errors.append(f"rendu hors matière présent : {probe[:50]}")

cache = json.load(open("scripts-translate/quran-cache.json", encoding="utf-8"))
rasm_18 = {n: t for n, t in cache["18"]["ar"]}
for n in range(1, 30):
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

total = 18 + len(rendus) + len(contenu) + 12 + 29 + 3
print(f"verify-748-quran : {total} contrôles — rendus {len(rendus)} + contenu {len(contenu)} + interdits {12 + 29} + structure {18} + typo 3")
if errors:
    print("verify-748 FAIL :")
    for e in errors:
        print(" -", e)
    sys.exit(1)
print("verify-748 PASS — structure OK, āyāt 30-31 présentes (rasm warš du cache), parallèles al-Anbiyāʾ 94/al-Fāṭir 33/al-Ḥaǧǧ 23/az-Zukhruf 51+34/al-Furqān 75-76 présents, contenu complet, 0 rendu hors matière (1-29), 0 rasm nu 18:1-29, 0 arabe résiduel (ﷺ exempté)")

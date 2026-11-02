#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Minhāj — contrôle coranique et de contenu de la leçon 745 (tafsir-5ep,
sūrat al-Kahf v21-24 — septième leçon du second livre, pages 50-57 du manuel
miroir tafsir-2-thanawi). Les āyāt 21-24 sont rendues en français sur le rasm
warš du cache (présence vérifiée) ; le double rendu des āyāt 19-20 (leçon 744)
et des āyāt 6-18 (leçons 740-743) est interdit ; le rasm nu du cache interdit
au corps (0 arabe — FR-seule) pour TOUTES les āyāt voisines (6-27)."""
import json
import re
import sys

HTML = "tr-tmp/lesson-745-fr.html"
html = open(HTML, encoding="utf-8").read()
norm = re.sub(r"[ \u202f\u00a0]+", " ", html.replace("&nbsp;", "\u00a0"))
errors = []

# 1. structure et marqueurs
for frag in [
    "Source du cours",
    "Septième leçon du second livre du parcours",
    "pages 50 à 57 de l’imprimé miroir",
    "1_20220304_20220304_2251",
    "Les objectifs de la leçon",
    "Le commentaire",
    "Les subtilités et les bienfaits",
    "L’évaluation",
    "L’exploitation",
    "la page imprimée 57",
    "jamais deviné",
]:
    if frag.lower() not in norm.lower():
        errors.append(f"fragment attendu absent : {frag[:55]}")

# 2. les āyāt 21-24 rendues en français (rasm warš du cache) — présence (10 rendus)
rendus = [
    "Et c’est ainsi que Nous fîmes qu’ils furent découverts, afin qu’ils sachent que la promesse de Dieu est vérité et qu’il n’y ait point de doute au sujet de l’Heure.",
    "Aussi se disputèrent-ils à leur sujet et déclarèrent-ils : construisez sur eux un édifice, leur Seigneur les connaît mieux",
    "élevons sur eux un sanctuaire",
    "Ils diront : ils étaient trois et le quatrième était leur chien",
    "qu’ils étaient cinq, le sixième étant leur chien",
    "sept, le huitième étant leur chien",
    "Dis : mon Seigneur connaît mieux leur nombre, il n’en est que peu qui le savent",
    "Ne discute à leur sujet que d’une façon apparente et ne consulte personne en ce qui les concerne",
    "Et ne dis jamais, à propos d’une chose : je la ferai sûrement demain, sans ajouter : si Dieu le veut",
    "invoque ton Seigneur quand tu oublies et dis : je souhaite que mon Seigneur me guide et me mène plus près de ce qui est correct",
    "(21-24)",
]
for r in rendus:
    if r not in norm:
        errors.append(f"rendu coranique attendu absent : {r[:55]}")

# 3. contenu attendu (confrontation au manuel et au récit R501)
contenu = [
    "aʿtharnā",
    "quadrilittère muni de l’hamza",
    "li-yaʿlamū",
    "Ǧāmiʿ al-bayān",
    "tel qu’imprimé",
    "Ibn ʿAṭiyya",
    "tanāzuʿ",
    "Quṭāda",
    "al-wulāt",
    "ʿĪsā ibn ʿUmar aṯ-Ṯaqafī",
    "taṭmīs",
    "ʿUbayd ibn ʿUmayr",
    "Maǧāz al-Qurʾān",
    "marǧūma",
    "al-ghayb",
    "Ibn ʿAbbās",
    "Abū Naṣr al-Qushayrī",
    "al-Ǧāmiʿ li-aḥkām al-Qurʾān",
    "Ibn Ǧuzayy",
    "at-Tašīl",
    "Tamārīkihim",
    "tamārīy",
    "Naǧrān",
    "al-Qurṭubī",
    "aḥkām ad-dīn",
    "l’orientation, l’enseignement et la correction",
    "in šāʾ Allāh",
    "Ibn al-Qāsim",
    "Ašhab",
    "Ibn ʿAbd al-Ḥakam",
    "Mālik",
    "Aḥkām al-Qurʾān d’Ibn al-ʿArabī",
    "722/822",
    "l’expiation",
    "ʿasā an yahdiyani rabbī",
    "az-Zaǧǧāǧ",
    "la capacité de Dieu à ressusciter les morts",
    "Shāyṭān",
    "adab",
    "Salam sur vous, demeure d’un peuple croyant",
    "la page 58",
    "52-72",
    "25-27",
    "la grille du portail",
]
for c in contenu:
    if c not in norm:
        errors.append(f"contenu attendu absent : {c[:55]}")

# 4. ABSENCE — rendus des āyāt des leçons voisines (19-20 livrés en 744,
#    6-18 en 740-743 ; 25-27 = leçon suivante) — rasm nu du cache interdit
for probe in [
    "Et ainsi Nous les ressuscitâmes, afin qu’ils s’interrogent les uns les autres",
    "combien avez-vous demeuré",
    "Car s’ils se manifestaient à vous, ils vous lapideraient",
    "C’est Nous qui te rapportons leur récit en vérité",
    "Tu verras le soleil",
    "s’écarter de leur Caverne vers la droite",
    "Nous frappâmes alors sur leurs oreilles",
    "votre Seigneur y répandra pour vous de Sa miséricorde",
    "Or, ils demeurèrent dans leur caverne trois cents ans",
    "Et frappe-leur cette exemplification",
    "Vêt-le de nos vêtements",
]:
    if probe in norm:
        errors.append(f"rendu hors matière présent : {probe[:50]}")

cache = json.load(open("scripts-translate/quran-cache.json", encoding="utf-8"))
rasm_18 = {n: t for n, t in cache["18"]["ar"]}
for n in range(6, 28):
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

total = 11 + len(rendus) + len(contenu) + 11 + 22 + 3
print(f"verify-745-quran : {total} contrôles — rendus {len(rendus)} + contenu {len(contenu)} + interdits {11 + 22} + structure {11} + typo 3")
if errors:
    print("verify-745 FAIL :")
    for e in errors:
        print(" -", e)
    sys.exit(1)
print("verify-745 PASS — structure OK, āyāt 21-24 présentes (rasm warš du cache), contenu complet, 0 rendu hors matière (6-20, 25-27), 0 rasm nu 18:6-27, 0 arabe résiduel (ﷺ exempté)")

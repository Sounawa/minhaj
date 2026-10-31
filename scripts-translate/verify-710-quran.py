#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Minhāj — contrôle coranique de la leçon 710 (tafsir-5ep, Isrāʾ 2-4).
Le rasm du chapitre (manuel miroir p.18-23) cite les versets 2-4 d'al-Isrāʾ
(lecture warš : « wakīlan » au verset 2) et un hadith de Mujāhid sur la
reconnaissance de Nūḥ (Ibn Abī d-Dunyā + al-Bayhaqī, Shuʿab al-Īmān).
Vérifications : présence des rendus français des trois versets, concordance
des références avec le cache, absence de toute citation non portée par le
rasm (notamment les versets 5-8 — matière de la leçon suivante, cités au
titre de la préparation seulement), présence de la chaîne du hadith."""
import json
import re
import sys

HTML = "scripts-translate/tr-tmp/pdf-mut23h3c-710.html"
html = open(HTML, encoding="utf-8").read()

errors = []

# 1. rendus français attendus (versets 2-4, cache warš)
for frag in [
    "Et Nous avons donné à Mūsā le Livre",
    "Nous en avons fait une guidée pour les Banū Isrāʾīl",
    "ne prenez pas, en dehors de Moi, de garant",
    "Ô descendance de ceux que Nous avons portés avec Nūḥ",
    "un serviteur grandement reconnaissant",
    "Et Nous avons fait parvenir aux Banū Isrāʾīl, dans le Livre",
    "vous corromprez assurément la terre à deux reprises",
    "vous vous élèverez assurément d’une élévation immense",
]:
    if frag not in html:
        errors.append(f"rendu attendu absent : {frag[:60]}")

# le repère de plage (2-4)
if not re.search(r"»\s*\(2-4\)", html):
    errors.append("repère de plage (2-4) absent")

# 2. concordance avec le cache : les versets 2-4 portent bien ces énoncés
#    (comparaison sans diacritiques — marques coraniques U+06D6-U+06ED incluses)
def bare(t: str) -> str:
    return re.sub(r"[\u064B-\u065F\u0670\u06D6-\u06ED\u0640\u0671]", "", t)

cache = json.load(open("scripts-translate/quran-cache.json", encoding="utf-8"))
v2 = [t for i, t in cache["17"]["ar"] if i == 2][0]
v3 = [t for i, t in cache["17"]["ar"] if i == 3][0]
v4 = [t for i, t in cache["17"]["ar"] if i == 4][0]
if "وكيل" + "ا" not in bare(v2).replace("ـ", ""):
    errors.append("cache 17:2 ne porte pas wakīlan (rasm inattendu)")
if "ذريةمنحملنا" not in bare(v3).replace(" ", "") or "شكورا" not in bare(v3).replace(" ", ""):
    errors.append("cache 17:3 inattendu")
if "مرتين" not in bare(v4).replace(" ", "") or "علوا" not in bare(v4).replace(" ", ""):
    errors.append("cache 17:4 inattendu")

# la lecture warš (wakīlan) est celle du manuel : la glose en témoigne
if "wakīlan" not in html or "tawakkul" not in html:
    errors.append("glose de (wakīlan) absente — la lecture warš non rendue")

# 3. hadith de Mujāhid : rendu + chaîne canonique en note
for frag in [
    "il ne mangea jamais chose sans louer Allah",
    "il ne but jamais boisson sans louer Allah",
    "il ne marcha jamais d’une marche sans louer Allah",
    "il ne s’empara jamais de chose sans louer Allah",
    "Ibn Abī d-Dunyā",
    "al-Bayhaqī dans Shuʿab al-Īmān",
]:
    if frag not in html:
        errors.append(f"hadith/chaîne attendu absent : {frag[:50]}")

# 4. citations NON portées par le rasm du chapitre — interdites dans le corps
#    (les versets 5-8 relèvent de la leçon suivante ; seule la préparation
#    les nomme, sans rendre leur texte)
body = html.split("<h2>L’exploitation", 1)[0]
for pat, label in [
    (r"فَإِذَا جَاءَ وَعْد", "al-Isrāʾ 17:5 (leçon suivante — non portée)"),
    (r"أُولِي بَأْسٍ", "al-Isrāʾ 17:5 (non portée)"),
    (r"جَاسُوا خِلَالَ الدِّيَار", "al-Isrāʾ 17:5 (non portée)"),
    (r"رَدَدْنَا لَكُمُ الْكَرَّة", "al-Isrāʾ 17:6 (non portée)"),
    (r"عَسَىٰ رَبُّكُمْ", "al-Isrāʾ 17:8 (non portée)"),
]:
    if re.search(pat, body):
        errors.append(f"citation inattendue détectée : {label}")

# 5. aucun caractère arabe résiduel (doctrine FR-seule) — ﷺ (U+FDFA),
#    ligature de la salawat, EXEMPTEE : convention du corpus savant
if re.search(r"[\u0600-\u06FF\u0750-\u077F\u08A0-\u08FF\uFB50-\uFDF9\uFDFB-\uFDFF\uFE70-\uFEFF]", html):
    errors.append("caractère arabe résiduel détecté")

if errors:
    print("ÉCHEC :")
    for e in errors:
        print(" -", e)
    sys.exit(1)
print("PASS : leçon 710 — versets 2-4 rendus (warš, wakīlan), références "
      "concordes au cache, hadith de Mujāhid rendu avec sa chaîne, "
      "aucune citation hors rasm, 0 arabe résiduel.")

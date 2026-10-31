#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Minhāj — contrôle coranique de la leçon 711 (tafsir-5ep, Isrāʾ 5-8).
Vérifie : rendus français des versets 5-8 (rasm warš du cache), la double
lecture ǧāsū/ḥāsū, l'absence de citations hors rasm (versets 9-14 = leçon
suivante, interdits au corps), 0 arabe résiduel (ﷺ exempté par convention)."""
import json
import re
import sys

HTML = "scripts-translate/tr-tmp/pdf-mut23h3c-711.html"
html = open(HTML, encoding="utf-8").read()
errors = []

for frag in [
    "Et quand viendra la promesse de la première des deux",
    "détenteurs d’une force redoutable",
    "qui fouleront le pays de long en large",
    "et ce fut une promesse accomplie",
    "Puis Nous vous rendîmes la reprise sur eux",
    "les plus abondants en ralliement",
    "Si vous faites le bien, vous le faites pour vous-mêmes",
    "et si vous faites le mal, c’est contre elle",
    "quand viendra la promesse de la Dernière",
    "pour assombrir vos visages",
    "entrer dans la Mosquée comme ils y entrèrent la première fois",
    "anéantir entièrement ce dont ils s’emparèrent",
    "Il se peut que votre Seigneur vous fasse miséricorde",
    "mais si vous récidivez, Nous recommencerons",
    "la Géhenne aux incrédules pour enclos",
]:
    if frag not in html:
        errors.append(f"rendu attendu absent : {frag[:55]}")

if not re.search(r"»\s*\(5-8\)", html):
    errors.append("repère de plage (5-8) absent")

def bare(t: str) -> str:
    return re.sub(r"[\u064B-\u065F\u0670\u06D6-\u06ED\u0640\u0671]", "", t)

cache = json.load(open("scripts-translate/quran-cache.json", encoding="utf-8"))
ar = dict((i, t) for i, t in cache["17"]["ar"])
v5, v6, v7, v8 = ar[5], ar[6], ar[7], ar[8]
b5, b7, b8 = bare(v5), bare(v7), bare(v8)
if "بعثنا" not in b5 or "فجاسوا" not in b5 or "مفعولا" not in b5:
    errors.append("cache 17:5 inattendu")
if "كرة" not in bare(v6) or "نفيرا" not in bare(v6) or "بنين" not in bare(v6):
    errors.append("cache 17:6 inattendu")
if b7.replace(" ", "").count("حسنتم") < 2 or "خرة" not in b7 or "تتبيرا" not in b7:
    errors.append("cache 17:7 inattendu")
if "عسى" not in b8 or "عدنا" not in b8 or "حصيرا" not in b8:
    errors.append("cache 17:8 inattendu — la lecture warš (ʿudtum ʿudnā) attendue")

# la double lecture du verset 5 rendue
for frag in ["fa-ǧāsū", "fa-ḥāsū", "Abū s-Sammāl", "au jīm", "au ḥāʾ"]:
    if frag not in html:
        errors.append(f"lecture/qirāʾa attendue absente : {frag}")

# citations hors rasm — interdites au corps (versets 9-14 : leçon suivante)
body = html.split("<h2>L’évaluation", 1)[0]
for pat, label in [
    (r"يهدي", "al-Isrāʾ 17:9 (leçon suivante — non portée)"),
    (r"أقوم", "al-Isrāʾ 17:9 (non portée)"),
    (r"وَمَن", "rasm arabe — la pièce rend la traduction, non le rasm"),
    (r"عِبَادًا", "rasm arabe translittéré — non rendu en rasm"),
]:
    if re.search(pat, body):
        errors.append(f"citation inattendue : {label}")

if re.search(r"[\u0600-\u06FF\u0750-\u077F\u08A0-\u08FF\uFB50-\uFDF9\uFDFB-\uFDFF\uFE70-\uFEFF]", html):
    errors.append("caractère arabe résiduel détecté")

if errors:
    print("ÉCHEC :")
    for e in errors:
        print(" -", e)
    sys.exit(1)
print("PASS : leçon 711 — versets 5-8 rendus sur le rasm warš du cache "
      "(ʿudtum ʿudnā en 17:8), double lecture ǧāsū/ḥāsū rendue, aucune "
      "citation hors rasm (17:9-14 interdits au corps), 0 arabe résiduel.")

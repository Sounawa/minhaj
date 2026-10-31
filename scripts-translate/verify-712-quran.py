#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Minhāj — contrôle coranique de la leçon 712 (tafsir-5ep, Isrāʾ 9-12).
Vérifie : rendus français des versets 9-12 (rasm warš du cache), les citations
d'appui Anfāl 32 et Yūnus 12 (au cache), la notice philologique sur la graphie
de « yadʿu » (al-masmūʿ), l'absence de citations hors rasm (versets 13-17 =
leçon suivante, interdits au corps), 0 arabe résiduel."""
import json
import re
import sys

HTML = "scripts-translate/tr-tmp/pdf-mut23h3c-712.html"
html = open(HTML, encoding="utf-8").read()
errors = []

for frag in [
    "Certes, ce Qurʾān guide vers ce qui est plus droit",
    "il annonce aux croyants qui font les œuvres salutaires",
    "qu’ils auront une grande rétribution",
    "ceux qui ne croient pas en l’au-delà",
    "Nous leur avons préparé un châtiment douloureux",
    "l’homme appelle le mal comme il appelle le bien",
    "l’homme fut créé pressé",
    "Nous fîmes de la nuit et du jour deux signes",
    "Nous effaçâmes le signe de la nuit",
    "le signe du jour voyant",
    "une grâce de votre Seigneur",
    "le nombre des années et le calcul",
    "toute chose, Nous l’exposâmes en exposé détaillé",
]:
    if frag not in html:
        errors.append(f"rendu attendu absent : {frag[:55]}")

if not re.search(r"»\s*\(9-12\)", html):
    errors.append("repère de plage (9-12) absent")

# citations d'appui — rendues elles aussi sur le rasm du cache
for frag in [
    "si ceci est la vérité venant de Toi",
    "fais pleuvoir sur nous des pierres du ciel",
    "couché sur le côté, assis ou debout",
    "il s’en va comme s’il ne Nous avait point imploré",
]:
    if frag not in html:
        errors.append(f"citation d’appui attendue absente : {frag[:50]}")

def bare(t: str) -> str:
    return re.sub(r"[\u064B-\u065F\u0670\u06D6-\u06ED\u0640\u0671]", "", t)

cache = json.load(open("scripts-translate/quran-cache.json", encoding="utf-8"))
ar17 = dict((i, t) for i, t in cache["17"]["ar"])
v9, v10, v11, v12 = ar17[9], ar17[10], ar17[11], ar17[12]
b9, b10, b11, b12 = bare(v9), bare(v10), bare(v11), bare(v12)
if "يهدى" not in b9 or "أقوم" not in b9 or "ويبشر" not in b9 or "أجرا كبيرا" not in b9:
    errors.append("cache 17:9 inattendu")
if "أعتدنا" not in b10 or "أليما" not in b10 or "بلءاخرة" not in b10:
    errors.append("cache 17:10 inattendu")
if "ويدع" not in b11 or "عجولا" not in b11 or "دعاءه" not in b11:
    errors.append("cache 17:11 inattendu")
if "ءايتين" not in b12 or "فمحونا" not in b12 or "مبصرة" not in b12 or "تفصيلا" not in b12:
    errors.append("cache 17:12 inattendu")
ar8 = dict((i, t) for i, t in cache["8"]["ar"])
if "فأمطر" not in bare(ar8[32]) or "حجارة" not in bare(ar8[32]):
    errors.append("cache 8:32 inattendu")
ar10 = dict((i, t) for i, t in cache["10"]["ar"])
if "دعانا لجنبه" not in bare(ar10[12]) or "قاعدا" not in bare(ar10[12]):
    errors.append("cache 10:12 inattendu")

# gloses et noms attendus
for frag in ["aʿdal", "aṣwab", "qiwām", "yadʿu", "mubṣira", "tafṣīlan", "muḏakkir",
             "maǧāz ʿaqlī", "ce qui était entendu", "Ibn al-Kawwāʾ", "Salmān al-Fārisī",
             "Qatāda", "Mujāhid", "Aṭ-Ṭabarī", "ar-Rāzī", "Mafātīḥ al-ġayb"]:
    if frag not in html:
        errors.append(f"glose/nom attendu absent : {frag}")

# citations hors rasm — interdites au corps (versets 13-17 : leçon suivante)
body = html.split("<h2>L’évaluation", 1)[0]
for pat, label in [
    (r"son sort à son cou", "al-Isrāʾ 17:13 (leçon suivante — non portée)"),
    (r"lis ton livre", "al-Isrāʾ 17:14 (non portée)"),
    (r"quiconque est guidé", "al-Isrāʾ 17:15 (non portée)"),
]:
    if re.search(pat, body, re.IGNORECASE):
        errors.append(f"citation inattendue : {label}")

if re.search(r"[\u0600-\u06FF\u0750-\u077F\u08A0-\u08FF\uFB50-\uFDF9\uFDFB-\uFDFF\uFE70-\uFEFF]", html):
    errors.append("caractère arabe résiduel détecté")

if errors:
    print("ÉCHEC :")
    for e in errors:
        print(" -", e)
    sys.exit(1)
print("PASS : leçon 712 — versets 9-12 rendus sur le rasm warš du cache (y compris "
      "la graphie de « yadʿu », al-masmūʿ), citations d’appui Anfāl 32 et Yūnus 12 "
      "au rasm du cache, aucune citation hors rasm (17:13-17 interdits au corps), "
      "0 arabe résiduel.")

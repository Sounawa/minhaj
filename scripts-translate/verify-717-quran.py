#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Minhāj — contrôle coranique de la leçon 717 (tafsir-5ep, Isrāʾ 31-33).
Vérifie : rendus français des versets 31-33 (rasm warš du cache), les gloses
lexicales et les noms portés, l'absence de citations hors rasm (versets 34-36 =
leçon suivante, interdits au corps), 0 arabe résiduel."""
import json
import re
import sys

HTML = "scripts-translate/tr-tmp/pdf-mut23h3c-717.html"
html = open(HTML, encoding="utf-8").read()
errors = []

for frag in [
    "Et ne tuez pas vos enfants par peur de l’imlaq",
    "Nous les pourvoirons, et vous",
    "leur mise à mort fut un grand péché",
    "Et n’approchez pas la fornication",
    "elle fut immoralité et mauvaise voie",
    "Et ne tuez pas l’âme qu’Allah a déclarée sacrée",
    "sauf de plein droit",
    "quiconque fut tué injustement",
    "Nous avons établi à son représentant une autorité",
    "que nul n’excède dans le meurtre",
    "il fut secouru",
    "quand l’enterrée vivante sera interrogée",
    "pour quel péché fut-elle tuée",
    "A cause de cela, Nous décrétâmes pour les fils d’Israël",
    "comme s’il avait tué les hommes tous",
]:
    if frag not in html:
        errors.append(f"rendu attendu absent : {frag[:55]}")

if not re.search(r"»\s*\(31-33\)", html):
    errors.append("repère de plage (31-33) absent")

def bare(t: str) -> str:
    return re.sub(r"[\u064B-\u065F\u0670\u06D6-\u06ED\u0640\u0671]", "", t)

cache = json.load(open("scripts-translate/quran-cache.json", encoding="utf-8"))
ar17 = dict((i, t) for i, t in cache["17"]["ar"])
v31, v32, v33 = (ar17[i] for i in (31, 32, 33))
b31, b32, b33 = (bare(v) for v in (v31, v32, v33))
if "ولا تقتلوا أولدكم خشية إملق" not in b31 or "نحن نرزقهم وإياكم" not in b31:
    errors.append("cache 17:31 inattendu")
if "كان خطا كبيرا" not in b31:
    errors.append("cache 17:31 (khiṭʾan) inattendu")
if "ولا تقربوا لزنى" not in b32 or "كان فحشة وساء سبيلا" not in b32:
    errors.append("cache 17:32 inattendu")
if "حرم لله إلا بلحق" not in b33 or "لوليه سلطنا" not in b33:
    errors.append("cache 17:33 inattendu")
if "فلا يسرف فى لقتل" not in b33 or "كان منصورا" not in b33:
    errors.append("cache 17:33 (manṣūran) inattendu")

for frag in ["al-imlāq", "al-faqr", "al-ḥāǧa", "al-fāḥiša", "manṣūran",
             "muʾayyad", "khiṭʾan", "khaṭaʾan", "Ibn ʿĀmir", "Abū Jaʿfar",
             "al-Ḥāqqa", "Abū ʿAlī al-Fārisī", "Ṣaḥīḥ al-Bukhārī",
             "al-mulābasa", "az-zinā", "al-Farazdaq", "ṣahbāʾ", "aṭ-Ṭabarī",
             "walīhi", "diya", "Ibn ʿAbbās", "aḍ-Ḍaḥḥāk", "Qatāda", "ibn Masʿūd",
             "al-qiṣāṣ", "at-taʿaddī", "Ibn Kathīr", "Abū ʿAmr", "ʿĀṣim",
             "Ḥamza", "al-Kisāʾī", "Ibn ʿAṭiyya", "Mafātīḥ al-ġayb",
             "ar-Rāzī", "al-Māʾida 32", "Ibn Māǧa", "al-Anʿām", "at-Takwīr",
             "mafʿūl li-aǧlihi", "al-malqāt", "rušd", "ḍarūriyyāt",
             "an-nasab aṭ-ṭāhir", "al-ʿirḍ", "al-ġīra", "Gāhiliyya", "ﷺ"]:
    if frag not in html:
        errors.append(f"glose/nom attendu absent : {frag}")

# citations hors rasm — interdites au corps (versets 34-36 : leçon suivante)
body = html.split("<h2>L’évaluation", 1)[0]
for pat, label in [
    (r"orphelin", "al-Isrāʾ 17:34 (leçon suivante — non portée)"),
    (r"māl al-yatīm", "al-Isrāʾ 17:34 (non portée)"),
    (r"balance", "al-Isrāʾ 17:35 (non portée)"),
    (r"Mesure\b", "al-Isrāʾ 17:35 (non portée)"),
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
print("PASS : leçon 717 — versets 31-33 rendus sur le rasm warš du cache, "
      "gloses lexicales portées (al-imlāq, al-fāḥiša, manṣūran), les deux "
      "lectures de khiṭʾan (Ibn ʿĀmir / Abū Jaʿfar), le hadith d’Ibn Masʿūd, "
      "at-Takwīr 8-9, le walī et le sulṭān (Ibn ʿAbbās, aḍ-Ḍaḥḥāk, Qatāda), "
      "les lectures de yusrif (yāʾ du gros des lecteurs, tāʾ d’Ibn ʿĀmir, "
      "Ḥamza, al-Kisāʾī), ar-Rāzī 2/133, al-Māʾida 32, Ibn Māǧa, les deux "
      "hadiths d’al-Bukhārī et Ibn ʿĀšūr au DOM, aucune citation hors rasm "
      "(17:34-36 interdits au corps), 0 arabe résiduel.")

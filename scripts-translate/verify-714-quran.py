#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Minhāj — contrôle coranique de la leçon 714 (tafsir-5ep, Isrāʾ 18-22).
Vérifie : rendus français des versets 18-22 (rasm warš du cache), la citation
d'appui an-Naǧm 39 (au cache), les gloses lexicales et grammaticales portées,
l'absence de citations hors rasm (versets 23-25 = leçon suivante, interdits au
corps), 0 arabe résiduel."""
import json
import re
import sys

HTML = "scripts-translate/tr-tmp/pdf-mut23h3c-714.html"
html = open(HTML, encoding="utf-8").read()
errors = []

for frag in [
    "Quiconque désire [la vie] immédiate",
    "Nous nous hâtons de donner ce que Nous voulons",
    "où il brûlera méprisé et repoussé",
    "l’effort de ceux-là sera reconnu",
    "des dons de ton Seigneur",
    "ne sont refusés [à personne]",
    "Regarde comment Nous favorisons certains sur d’autres",
    "rangs plus élevés et plus privilégiés",
    "N’assigne point à Allah d’autre divinité",
    "méprisé et abandonné",
]:
    if frag not in html:
        errors.append(f"rendu attendu absent : {frag[:55]}")

if not re.search(r"»\s*\(18-22\)", html):
    errors.append("repère de plage (18-22) absent")

# citation d'appui — rendue elle aussi sur le rasm du cache
for frag in [
    "l’homme n’obtient que [le fruit] de ses efforts",
]:
    if frag not in html:
        errors.append(f"citation d’appui attendue absente : {frag[:50]}")
if not re.search(r"an-Naǧm\s*:\s*39", html):
    errors.append("référence d’appui an-Naǧm 39 absente")

def bare(t: str) -> str:
    return re.sub(r"[\u064B-\u065F\u0670\u06D6-\u06ED\u0640\u0671]", "", t)

cache = json.load(open("scripts-translate/quran-cache.json", encoding="utf-8"))
ar17 = dict((i, t) for i, t in cache["17"]["ar"])
v18, v19, v20, v21, v22 = ar17[18], ar17[19], ar17[20], ar17[21], ar17[22]
b18, b19, b20, b21, b22 = bare(v18), bare(v19), bare(v20), bare(v21), bare(v22)
if "لعاجلة" not in b18 or "عجلنا" not in b18 or "يصلىها" not in b18 or "مدحورا" not in b18:
    errors.append("cache 17:18 inattendu")
if "لءاخرة" not in b19 or "وسعى" not in b19 or "مؤمن" not in b19 or "مشكورا" not in b19:
    errors.append("cache 17:19 inattendu")
if "نمد" not in b20 or "هؤلاء" not in b20 or "عطاء" not in b20 or "محظورا" not in b20:
    errors.append("cache 17:20 inattendu")
if "فضلنا" not in b21 or "أكبر" not in b21 or "درجت" not in b21 or "تفضيلا" not in b21:
    errors.append("cache 17:21 inattendu")
if "تجعل" not in b22 or "إلها" not in b22 or "ءاخر" not in b22 or "مخذولا" not in b22:
    errors.append("cache 17:22 inattendu")
ar53 = dict((i, t) for i, t in cache["53"]["ar"])
if "ليس" not in bare(ar53[39]) or "سعى" not in bare(ar53[39]):
    errors.append("cache 53:39 inattendu")

# gloses et noms attendus
for frag in ["yaṣlāhā", "maḏmūman", "madḥūran", "maḥẓūran", "maḫḏūlan",
             "kullan", "namuddu", "iltifāt", "al-Firdaws", "ḫudlān",
             "birr al-wālidayn", "Ibn Māǧah", "al-Muwaṭṭaʾ", "al-Bukhārī",
             "at-Tirmidhī", "al-Baḥr al-Muḥīṭ", "Abū Ḥayyān", "Ibn ʿAṭiyya",
             "ar-Rāzī", "Mafātīḥ al-ġayb", "Ibn ʿAbbās", "al-Ḥasan al-Baṣrī",
             "Qatāda", "aṭ-Ṭabarī", "Musnad al-Qaḍāʿī"]:
    if frag not in html:
        errors.append(f"glose/nom attendu absent : {frag}")

# citations hors rasm — interdites au corps (versets 23-25 : leçon suivante)
body = html.split("<h2>L’évaluation", 1)[0]
for pat, label in [
    (r"a décrété", "al-Isrāʾ 17:23 (leçon suivante — non portée)"),
    (r"père et mère", "al-Isrāʾ 17:23 (non portée)"),
    (r"aile de l’humilité", "al-Isrāʾ 17:24 (non portée)"),
    (r"ils m’ont élevé", "al-Isrāʾ 17:24 (non portée)"),
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
print("PASS : leçon 714 — versets 18-22 rendus sur le rasm warš du cache, "
      "citation d’appui an-Naǧm 39 au rasm du cache, gloses lexicales et "
      "grammaticales portées, aucune citation hors rasm (17:23-25 interdits "
      "au corps), 0 arabe résiduel.")

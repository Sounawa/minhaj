#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Minhāj — contrôle coranique de la leçon 715 (tafsir-5ep, Isrāʾ 23-25).
Vérifie : rendus français des versets 23-25 (rasm warš du cache), les gloses
lexicales, grammaticales et les noms portés, l'absence de citations hors rasm
(versets 26-30 = leçon suivante, interdits au corps), 0 arabe résiduel."""
import json
import re
import sys

HTML = "scripts-translate/tr-tmp/pdf-mut23h3c-715.html"
html = open(HTML, encoding="utf-8").read()
errors = []

for frag in [
    "Ton Seigneur a décrété que vous n’adorez que Lui",
    "la bienfaisance envers les parents",
    "si l’un des deux, ou les deux, atteint auprès de toi la vieillesse",
    "ne leur dis pas «\u202ffi\u202f!\u202f»",
    "ne les rudoyez pas",
    "une parole généreuse",
    "l’aile de l’humilité",
    "fais-leur miséricorde comme ils m’ont élevé tout petit",
    "connaît mieux ce qu’il y a dans vos âmes",
    "les hommes revenants vers Lui, pardonneur",
]:
    if frag not in html:
        errors.append(f"rendu attendu absent : {frag[:55]}")

if not re.search(r"»\s*\(23-25\)", html):
    errors.append("repère de plage (23-25) absent")

def bare(t: str) -> str:
    return re.sub(r"[\u064B-\u065F\u0670\u06D6-\u06ED\u0640\u0671]", "", t)

cache = json.load(open("scripts-translate/quran-cache.json", encoding="utf-8"))
ar17 = dict((i, t) for i, t in cache["17"]["ar"])
v23, v24, v25 = ar17[23], ar17[24], ar17[25]
b23, b24, b25 = bare(v23), bare(v24), bare(v25)
if "وقضى ربك" not in b23 or "تعبدوا" not in b23 or "يبلغن" not in b23 or "تنهرهما" not in b23 or "قولا كريما" not in b23:
    errors.append("cache 17:23 inattendu")
if "وخفض لهما جناح لذل من لرحمة" not in b24 or "رحمهما كما ربيانى صغيرا" not in b24:
    errors.append("cache 17:24 inattendu")
if "أعلم بما فى نفوسكم" not in b25 or "للأوبين غفورا" not in b25:
    errors.append("cache 17:25 inattendu")

# gloses, lectures et noms attendus
for frag in ["ufin", "lā tanharhumā", "qawlan karīman", "al-awwābīna",
             "qaḍāʾ ḥukm", "wa-waṣṣā rabbuka", "Ibn Masʿūd", "an-Nakhaʿī",
             "Maymūn ibn Mihrān", "Ubayy ibn Kaʿb", "yabluġanna", "yabluġan",
             "yabluġāni", "badal maqsam", "mafhūm al-ḫiṭāb", "akalūnī l-barāġīt",
             "Sībawayh", "Ibn Kathīr", "Nāfiʿ", "Abū ʿAmr", "ʿĀṣim", "Ibn ʿĀmir",
             "Ibn Ḏakwān", "Ḥamza", "al-Kisāʾī", "al-ǧamalu ḏ-ḏullūl",
             "Saʿīd ibn al-Musayyib", "Ibn al-Musayyib", "Ṣaḥīḥ Muslim",
             "al-Qurṭubī", "al-muṣliḥūn", "al-musbiḥūn", "aḍ-ḍuḥā",
             "Ibn al-Munkadir", "ʿAwn al-ʿAqīlī", "Ibn Ǧubayr", "ar-Rāzī",
             "Mafātīḥ al-ġayb", "Ibn ʿAṭiyya", "fāʿil", "(2/123)"]:
    if frag not in html:
        errors.append(f"glose/nom attendu absent : {frag}")

# citations hors rasm — interdites au corps (versets 26-30 : leçon suivante)
body = html.split("<h2>L’évaluation", 1)[0]
for pat, label in [
    (r"prodigue", "al-Isrāʾ 17:26-27 (leçon suivante — non portée)"),
    (r"démons", "al-Isrāʾ 17:27 (non portée)"),
    (r"sclérosée", "al-Isrāʾ 17:29 (non portée)"),
    (r"déployée", "al-Isrāʾ 17:29 (non portée)"),
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
print("PASS : leçon 715 — versets 23-25 rendus sur le rasm warš du cache, "
      "gloses lexicales et grammaticales portées (lectures, badal maqsam, "
      "mafhūm al-ḫiṭāb), Qurṭubī et Rāzī (2/123) restitués aux éditions "
      "canoniques, aucune citation hors rasm (17:26-30 interdits au corps), "
      "0 arabe résiduel.")

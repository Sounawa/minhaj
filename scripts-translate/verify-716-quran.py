#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Minhāj — contrôle coranique de la leçon 716 (tafsir-5ep, Isrāʾ 26-30).
Vérifie : rendus français des versets 26-30 (rasm warš du cache), les gloses
lexicales et les noms portés, l'absence de citations hors rasm (versets 31-33 =
leçon suivante, interdits au corps), 0 arabe résiduel."""
import json
import re
import sys

HTML = "scripts-translate/tr-tmp/pdf-mut23h3c-716.html"
html = open(HTML, encoding="utf-8").read()
errors = []

for frag in [
    "donne au proche parent son droit",
    "ainsi qu’au pauvre et au gens de chemin",
    "ne sois pas prodigue",
    "les prodigues étaient les frères des démons",
    "le démon fut, envers son Seigneur, ingrat",
    "quête de la miséricorde de ton Seigneur que tu espères",
    "adresse-leur une parole facile",
    "une main enchaînée à ton cou",
    "ne l’étends pas à toute son extension",
    "blâmé et impuissant",
    "étend la provision à qui Il veut et la borne",
    "informé et voyant",
]:
    if frag not in html:
        errors.append(f"rendu attendu absent : {frag[:55]}")

if not re.search(r"»\s*\(26-30\)", html):
    errors.append("repère de plage (26-30) absent")

def bare(t: str) -> str:
    return re.sub(r"[\u064B-\u065F\u0670\u06D6-\u06ED\u0640\u0671]", "", t)

cache = json.load(open("scripts-translate/quran-cache.json", encoding="utf-8"))
ar17 = dict((i, t) for i, t in cache["17"]["ar"])
v26, v27, v28, v29, v30 = (ar17[i] for i in (26, 27, 28, 29, 30))
b26, b27, b28, b29, b30 = (bare(v) for v in (v26, v27, v28, v29, v30))
if "لقربى حقه" not in b26 or "ولا تبذر تبذيرا" not in b26:
    errors.append("cache 17:26 inattendu")
if "لمبذرين كانوا إخون لشيطين" not in b27 or "لربه كفورا" not in b27:
    errors.append("cache 17:27 inattendu")
if "بتغاء رحمة من ربك ترجوها" not in b28 or "قولا ميسورا" not in b28:
    errors.append("cache 17:28 inattendu")
if "مغلولة إلى عنقك" not in b29 or "ملوما محسورا" not in b29:
    errors.append("cache 17:29 inattendu")
if "يبسط لرزق" not in b30 or "خبيرا بصيرا" not in b30:
    errors.append("cache 17:30 inattendu")

for frag in ["at-tabḏīr", "maġlūla", "al-ġull", "lā tab-suṭhā", "maḥsūran",
             "Qatāda", "Abū Bakr an-Naqqāš", "nom d’espèce", "Ibn ʿAṭiyya",
             "Ibn Ǧurayǧ", "bayt al-māl", "sadd al-ḫalla", "mālikite",
             "ʿAmmār ibn Yāsir", "Ibn ʿAbbās", "Muǧāhid", "ʿIkrima", "Ibn Zayd",
             "al-Ḥujurāt", "an-Nūr", "Ṣaḥīḥ al-Bukhārī", "aṭ-Ṭabarī",
             "Ǧāmiʿ al-bayān", "al-iqtiṣād", "juḥūd", "ﷺ"]:
    if frag not in html:
        errors.append(f"glose/nom attendu absent : {frag}")

# citations hors rasm — interdites au corps (versets 31-33 : leçon suivante)
body = html.split("<h2>L’évaluation", 1)[0]
for pat, label in [
    (r"vos enfants", "al-Isrāʾ 17:31 (leçon suivante — non portée)"),
    (r"fornication", "al-Isrāʾ 17:32 (non portée)"),
    (r"l’âme", "al-Isrāʾ 17:33 (non portée)"),
    (r"immoralité", "al-Isrāʾ 17:32 (non portée)"),
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
print("PASS : leçon 716 — versets 26-30 rendus sur le rasm warš du cache, "
      "gloses lexicales portées (at-tabḏīr, maġlūla, tab-suṭhā, maḥsūran), "
      "Qatāda, an-Naqqāš, Ibn Ǧurayǧ, Ibn ʿAṭiyya, le hadith des deux cottes "
      "et aṭ-Ṭabarī au DOM, aucune citation hors rasm (17:31-33 interdits au "
      "corps), 0 arabe résiduel.")

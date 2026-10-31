#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Minhāj — contrôle coranique de la leçon 721 (tafsir-5ep, Isrāʾ 45-48).
Vérifie : rendus français des versets 45-48 (rasm warš du cache — 17:47 portant
les deux lectures, najwā et le dire des injustes), la citation interne de 17:46,
les gloses lexicales et les noms portés, l'absence de citations hors rasm
(17:41-44 = leçon précédente, interdites au corps), 0 arabe résiduel."""
import json
import re
import sys

HTML = "scripts-translate/tr-tmp/pdf-mut23h3c-721.html"
html = open(HTML, encoding="utf-8").read()
errors = []

for frag in [
    "Et lorsque tu récitas le Coran, Nous plaçâmes entre toi et ceux qui ne croient point à la Dernière un voile enveloppant",
    "Et Nous plaçâmes sur leurs cœurs des couvertures",
    "et dans leurs oreilles une surdité",
    "ils se tournèrent sur leurs talons, dégoutés",
    "Nous connaissons mieux ce avec quoi ils écoutent",
    "quand disent les injustes",
    "vous ne suivez qu’un homme ensorcelé",
    "Regarde comment ils frappèrent pour toi les exemples",
    "ils s’égarent donc, et ne peuvent point de chemin",
    "qu’ils ne le comprennent point",
]:
    if frag not in html:
        errors.append(f"rendu attendu absent : {frag[:55]}")

if not re.search(r"»\s*\(45-48\)", html):
    errors.append("repère de plage (45-48) absent")

def bare(t: str) -> str:
    return re.sub(r"[\u064B-\u065F\u0670\u06D6-\u06ED\u0640\u0671]", "", t)

cache = json.load(open("scripts-translate/quran-cache.json", encoding="utf-8"))
ar17 = dict((i, t) for i, t in cache["17"]["ar"])
v45, v46, v47, v48 = (ar17[i] for i in (45, 46, 47, 48))
b45, b46, b47, b48 = (bare(v) for v in (v45, v46, v47, v48))
if "جعلنا بينك وبين لذين لا يؤمنون بلءاخرة حجابا مستورا" not in b45:
    errors.append("cache 17:45 inattendu (le voile enveloppant)")
if "جعلنا على قلوبهم أكنة أن يفقهوه" not in b46 or "وفى ءاذانهم وقرا" not in b46 \
        or "ولوا على أدبرهم نفورا" not in b46:
    errors.append("cache 17:46 inattendu (les couvertures, la surdité, le retournement)")
if "نحن أعلم بما يستمعون به إذ يستمعون إليك" not in b47 or "وإذ هم نجوى" not in b47 \
        or "إذ يقول لظلمون إن تتبعون إلا رجلا مسحورا" not in b47:
    errors.append("cache 17:47 inattendu (le rasm warš porte les deux lectures — najwā et le dire des injustes)")
if "نظر كيف ضربوا لك لأمثال فضلوا فلا يستطيعون سبيلا" not in b48:
    errors.append("cache 17:48 inattendu (l’exemple frappé et le chemin)")

for frag in ["ḥijāban mastūrā", "akinnān", "waqran", "lawwaw", "mastūran bihī",
             "hushūr", "sātir", "mashʾūm", "maymūn", "shāʾim", "yamān",
             "al-mubālagha", "kinānat an-nabl", "an yafqahūhu", "nufūran",
             "nāfir", "shuhūd", "fuʿūlā", "nāfirīn", "nuqūr", "ḥaṣāṣ",
             "al-ladhī", "ilāf", "dār an-nadwa", "al-khabal", "saḥar", "riʾa",
             "intafakha saḥaruhu", "siḥr", "Quṣayy", "Abū Ṭālib", "aṭ-Ṭabarī",
             "Abū ʿUbayda", "ʿĀʾisha", "al-Akhfash", "Abū Muḥammad",
             "al-Walīd ibn al-Mughīra", "Ibn ʿAṭiyya", "al-Muḥarrar al-wajīz",
             "al-Baḥr al-muḥīṭ", "Abū Ḥayyān", "as-samāʿ", "al-fiqh",
             "al-iʿdād al-qiblī", "istiṯmār", "taqwīm", "yanziʿ", "ﷺ"]:
    if frag not in html:
        errors.append(f"glose/nom attendu absent : {frag}")

# les deux lectures de 17:47 rendues sans en choisir aucune
if "la lecture du conciliabule des trois" not in html or "sans en choisir aucune" not in html:
    errors.append("la note des deux lectures de 17:47 est absente")

# citations hors rasm — interdites au corps (versets 41-44 : leçon précédente)
body = html.split("<h2>L’évaluation", 1)[0]
for pat, label in [
    (r"Maître du Trône", "al-Isrāʾ 17:42 (leçon précédente — non portée)"),
    (r"élévation grandissime", "al-Isrāʾ 17:43 (leçon précédente — non portée)"),
    (r"sept cieux", "al-Isrāʾ 17:44 (leçon précédente — non portée)"),
    (r"Glorifie Allah tout ce qui est", "le Fer 1 (non porté)"),
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
print("PASS : leçon 721 — versets 45-48 rendus sur le rasm warš du cache (le voile "
      "enveloppant, les couvertures et la surdité, le retournement dégouté, le rasm "
      "17:47 portant les deux lectures — najwā et le dire des injustes — rendues sans "
      "en choisir aucune, l’exemple frappé et le chemin), la citation interne de 17:46 "
      "au corps, les cinq gloses du bandeau, les deux sens de l’āya (la protection "
      "physique des fils de Quṣayy — le voile de compréhension et le sceau), le débat "
      "sur mastūrā (al-Akhfash, le qāḍī Abū Muḥammad, la mubālagha), le carquois des "
      "flèches, la cause de descente chez Abū Ṭālib, nufūran (le masdar et le pluriel "
      "nāfir), la fuite des démons d’aṭ-Ṭabarī et le ḥaṣāṣ, le conciliabule à la dār "
      "an-nadwa, le délire et l’assimilation de la magie, Abū ʿUbayda (le poumon et "
      "ʿĀʾisha), le siḥr à la kasra, al-Walīd ibn al-Mughīra et les quatre traits, les "
      "finalités, Abū Ḥayyān 5/822 et la préparation 49-55 au DOM, aucune citation "
      "hors rasm (17:41-44 interdits au corps), 0 arabe résiduel.")

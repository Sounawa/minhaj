#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Minhāj — contrôle coranique de la leçon 718 (tafsir-5ep, Isrāʾ 34-36).
Vérifie : rendus français des versets 34-36 (rasm warš du cache), les gloses
lexicales et les noms portés, l'absence de citations hors rasm (versets 37-40 =
leçon suivante, interdits au corps), 0 arabe résiduel."""
import json
import re
import sys

HTML = "scripts-translate/tr-tmp/pdf-mut23h3c-718.html"
html = open(HTML, encoding="utf-8").read()
errors = []

for frag in [
    "Et n’approchez pas le bien de l’orphelin",
    "sauf de la façon qui est la meilleure",
    "jusqu’à ce qu’il atteigne sa force",
    "Et acquittez l’engagement",
    "l’engagement fut demandé en compte",
    "Et acquittez la mesure lorsque vous mesurez",
    "Et pesez avec la balance droite",
    "cela est meilleur et plus beau comme dénouement",
    "Et ne suis pas ce dont tu n’as pas science",
    "l’ouïe, la vue et le cœur — tout cela fut demandé en compte",
    "Ils t’interrogent sur ce qu’ils dépensent",
    "ce que vous dépensez de bien est pour les parents",
    "j’ai vu onze astres",
    "je les ai vus prosternés devant moi",
    "ceux qui gardent leurs dépôts confiés et leurs engagements",
]:
    if frag not in html:
        errors.append(f"rendu attendu absent : {frag[:55]}")

if not re.search(r"»\s*\(34-36\)", html):
    errors.append("repère de plage (34-36) absent")

def bare(t: str) -> str:
    return re.sub(r"[\u064B-\u065F\u0670\u06D6-\u06ED\u0640\u0671]", "", t)

cache = json.load(open("scripts-translate/quran-cache.json", encoding="utf-8"))
ar17 = dict((i, t) for i, t in cache["17"]["ar"])
v34, v35, v36 = (ar17[i] for i in (34, 35, 36))
b34, b35, b36 = (bare(v) for v in (v34, v35, v36))
if "ولا تقربوا مال ليتيم" not in b34 or "حتى يبلغ أشده" not in b34:
    errors.append("cache 17:34 inattendu")
if "وأوفوا بلعهد" not in b34 or "إن لعهد كان مسولا" not in b34:
    errors.append("cache 17:34 (ašuddahu, al-ʿahd) inattendu")
if "وأوفوا لكيل إذا كلتم" not in b35 or "وزنوا بلقسطاس لمستقيم" not in b35:
    errors.append("cache 17:35 inattendu")
if "ذلك خير وأحسن تأويلا" not in b35:
    errors.append("cache 17:35 (taʾwīlan) inattendu")
if "ولا تقف ما ليس لك به علم" not in b36 or "إن لسمع ولبصر ولفؤاد" not in b36:
    errors.append("cache 17:36 inattendu")

ar2 = dict((i, t) for i, t in cache["2"]["ar"])
b215 = bare(ar2[215])
if "يسلونك ماذا ينفقون" not in b215 or "فللولدين ولأقربين وليتمى ولمسكين وبن لسبيل" not in b215:
    errors.append("cache 2:215 (hadith d’Ibn ʿAbbās) inattendu")
ar6 = dict((i, t) for i, t in cache["6"]["ar"])
b152 = bare(ar6[152])
if "ولا تقربوا مال ليتيم" not in b152 or "وبعهد لله أوفوا" not in b152:
    errors.append("cache 6:152 (le verset cité par le hadith) inattendu")
ar12 = dict((i, t) for i, t in cache["12"]["ar"])
b4 = bare(ar12[4])
if "رأيت أحد عشر كوكبا" not in b4 or "رأيتهم لى سجدين" not in b4:
    errors.append("cache 12:4 (la métonymie du raisonneur) inattendu")
ar23 = dict((i, t) for i, t in cache["23"]["ar"])
b8 = bare(ar23[8])
if "لأمنتهم وعهدهم رعون" not in b8:
    errors.append("cache 23:8 (l’appui du Rāzī) inattendu")

for frag in ["taʾwīlan", "al-maʾāl", "al-ʿāqiba", "lā taqfū", "al-yatīm", "al-yatm",
             "al-infirād", "taʾamma", "Ibn as-Sikkīt", "al-Māwardī", "aytām",
             "ašrāf", "ašhād", "yatāmā", "asārā", "al-ḥāl", "al-ḫiṣla",
             "mulābasa", "Muǧāhid", "Ibn ʿAbbās", "Mālik", "qaḍāhu",
             "ašuddahu", "an-nāzila", "Sībawayh", "Abū ʿUbayda", "al-balūġ",
             "al-iḥtilām", "ar-rušd", "Ibn al-Qāsim", "Abū Ḥanīfa", "as-safh",
             "ḥaǧr", "les Bestiaux 152", "la Vache 215", "Sunan Abī Dāwūd",
             "n° 812", "al-mawālī", "al-makīyal", "al-mīzān", "Ibn ʿAṭiyya",
             "al-qisṭās", "al-ʿadl", "Qatāda", "taṭfīf", "masdar", "al-mukallaf",
             "an-Naḍr", "qaftī", "al-qifāʾ", "al-qāfiya", "Mundhir ibn Saʿīd al-Balūṭī",
             "al-Qurṭubī", "ʾulāʾika", "Yūsuf 4", "les Croyants 8", "al-Bayhaqī",
             "Ṣaḥīḥ Muslim", "Mafātīḥ al-ġayb", "ar-Rāzī", "2/733", "at-takāful",
             "at-taḍāmun", "al-kibr", "at-tawāḍuʿ", "al-iʿdād al-qiblī", "ﷺ"]:
    if frag not in html:
        errors.append(f"glose/nom attendu absent : {frag}")

# citations hors rasm — interdites au corps (versets 37-40 : leçon suivante)
body = html.split("<h2>L’évaluation", 1)[0]
for pat, label in [
    (r"\bmarche\b|\bmarcher\b|\bmarchez\b|\bmarchent\b", "al-Isrāʾ 17:37 (leçon suivante — non portée)"),
    (r"montagnes", "al-Isrāʾ 17:37 (non portée)"),
    (r"six jours", "al-Isrāʾ 17:40 (non portée)"),
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
print("PASS : leçon 718 — versets 34-36 rendus sur le rasm warš du cache, "
      "gloses lexicales portées (taʾwīlan, taqfū), la philologie du yatīm "
      "(Ibn as-Sikkīt, al-Māwardī, aytām/yatāmā), la mulābasa de la bāʾ, "
      "les avis de Muǧāhid et Mālik sur le tuteur, ašuddahu et la tutelle "
      "(Sībawayh, Abū ʿUbayda, Mālik, Abū Ḥanīfa), le hadith d’Ibn ʿAbbās "
      "(Abū Dāwūd 812, les Bestiaux 152, la Vache 215), les trois ordres, "
      "les lectures d’al-qisṭās (kasra de Ḥamza, al-Kisāʾī et Ḥafṣ, ḍamma "
      "du reste des Sept, la substitution du ṣād), le taṭfīf et Qatāda, "
      "l’étymologie de laqf (Ibn ʿAbbās, Muǧāhid, al-Balūṭī, al-Qurṭubī), "
      "ʾulāʾika et la métonymie du raisonneur (Yūsuf 4), le Rāzī sur la "
      "validité des contrats (les Croyants 8, les hadiths de Bayhaqī et "
      "Muslim), les finalités au DOM, aucune citation hors rasm "
      "(17:37-40 interdits au corps), 0 arabe résiduel.")

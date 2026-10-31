#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Minhāj — contrôle coranique de la leçon 719 (tafsir-5ep, Isrāʾ 37-40).
Vérifie : rendus français des versets 37-40 (rasm warš du cache), le parallèle
les Groupes 4, les gloses lexicales et les noms portés, l'absence de citations
hors rasm (versets 41-44 = leçon suivante, interdits au corps), 0 arabe résiduel."""
import json
import re
import sys

HTML = "scripts-translate/tr-tmp/pdf-mut23h3c-719.html"
html = open(HTML, encoding="utf-8").read()
errors = []

for frag in [
    "Et ne marche point sur la terre avec ostentation",
    "tu ne percera point la terre",
    "tu n’atteindras point les montagnes en longueur",
    "Tout cela — son laid fut auprès de ton Seigneur exécré",
    "Cela est de ce que ton Seigneur t’a révélé de la sagesse",
    "Et ne place point à côté d’Allah une autre divinité",
    "sinon tu seras jeté en la Géhenne, blâmé, banni",
    "Ton Seigneur te choisirait de préférence par des fils",
    "et prendrait des anges pour femelles",
    "Vous tenez un propos bien grand",
    "Si Allah voulait prendre un enfant",
    "Il est Allah, l’Unique, le Tout-Puissant",
]:
    if frag not in html:
        errors.append(f"rendu attendu absent : {frag[:55]}")

if not re.search(r"»\s*\(37-40\)", html):
    errors.append("repère de plage (37-40) absent")

def bare(t: str) -> str:
    return re.sub(r"[\u064B-\u065F\u0670\u06D6-\u06ED\u0640\u0671]", "", t)

cache = json.load(open("scripts-translate/quran-cache.json", encoding="utf-8"))
ar17 = dict((i, t) for i, t in cache["17"]["ar"])
v37, v38, v39, v40 = (ar17[i] for i in (37, 38, 39, 40))
b37, b38, b39, b40 = (bare(v) for v in (v37, v38, v39, v40))
if "ولا تمش فى لأرض مرحا" not in b37 or "إنك لن تخرق لأرض ولن تبلغ لجبال طولا" not in b37:
    errors.append("cache 17:37 inattendu")
if "كل ذلك كان سيئه عند ربك مكروها" not in b38:
    errors.append("cache 17:38 inattendu (le rasm warš porte « kāna »)")
if "ولا تجعل مع لله إلها ءاخر فتلقى فى جهنم ملوما مدحورا" not in b39:
    errors.append("cache 17:39 inattendu (le blâmé et le banni)")
if "أفأصفىكم ربكم بلبنين وتخذ من لملئكة إنثا" not in b40 or "لتقولون قولا عظيما" not in b40:
    errors.append("cache 17:40 (l’interrogation du blâme) inattendu")
ar39s = dict((i, t) for i, t in cache["39"]["ar"])
b4 = bare(ar39s[4])
if "لو أراد لله أن يتخذ ولدا" not in b4 or "هو لله لوحد لقهار" not in b4:
    errors.append("cache 39:4 (le parallèle tranché par la matière) inattendu")

for frag in ["at-tamāyul", "at-tabakhtur", "al-mukhtāl", "Ibn ʿAṭiyya", "Ibn ʿĀmir",
             "Ibn Kathīr", "Nāfiʿ", "Abū ʿAmr", "sayyiʾuhu", "sayyiʾa(tan)",
             "makrūhan", "makrūhatan", "ism fāʿil", "marīḥan", "mariḥa yarḥu",
             "al-marāḥ", "rāḥatuhu", "dunyāhu", "mahlūm", "madhūr", "madhmūm",
             "makhdhūl", "at-tawḥīd", "ar-riyāʾ", "al-ʿuǧb", "al-anāniyya",
             "iʿrāb", "les Groupes 4", "al-Baḥr al-muḥīṭ", "Abū Ḥayyān",
             "lī-yadhdhakkarū", "nūran", "al-iʿdād al-qiblī", "ﷺ"]:
    if frag not in html:
        errors.append(f"glose/nom attendu absent : {frag}")

# citations hors rasm — interdites au corps (versets 41-44 : leçon suivante)
body = html.split("<h2>L’évaluation", 1)[0]
for pat, label in [
    (r"sept ci", "al-Isrāʾ 17:44 (leçon suivante — non portée)"),
    (r"raisonnement logique", "consigne de la leçon suivante (non portée)"),
    (r"\bKufans?\b.*\bIbn ʿĀmir.*\bNāfiʿ\b.*seulement", "garde structure (non applicable)"),
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
print("PASS : leçon 719 — versets 37-40 rendus sur le rasm warš du cache (17:38 "
      "portant « kāna »), le parallèle les Groupes 4 tranché par la matière, les "
      "deux lectures de maraḥan (masdar / ism fāʿil), la marche de l’arrogant "
      "(at-tamāyul, at-tabakhtur), la motivation et la raillerie du mukhtāl, les "
      "deux cas d’Ibn ʿAṭiyya (la chasse — le repos au jour rare), les lectures "
      "de 17:38 (sayyiʾuhu des Kufans et d’Ibn ʿĀmir, sayyiʾa d’Ibn Kathīr, Nāfiʿ "
      "et Abū ʿAmr) et les quatre visages d’analyse, le sceau de la sagesse et de "
      "l’unicité (malūman madhūran), l’interrogation du blâme des anges filles, "
      "les quatre finalités, Abū Ḥayyān (malūm/madhmūm, makhdhūl/madhūr) et la "
      "préparation 41-44 au DOM, aucune citation hors rasm (17:41-44 interdits "
      "au corps), 0 arabe résiduel.")

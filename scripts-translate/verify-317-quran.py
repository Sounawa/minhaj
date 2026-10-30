#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Minhāj — contrôle coranique de la leçon 317 (ṣulḥ) :
le rasm du chapitre (fiqh-3 p.99-104) cite DEUX textes canoniques :
  1. le hadith d'Abū Hurayra [Sunan Abī Dāwūd, livre des jugements, chapitre du ṣulḥ] ;
  2. le verset de la conciliation — rendu au cache coranique An-Nisāʾ 114
     (le manuel marquant [an-Nisāʾ : 113] — écart documenté).
Vérification : la présence des citations rendues, l'absence de toute citation
que la pièce ne porte pas (An-Nisāʾ 128 « aṣ-ṣulḥu ḫayr » notamment), et la
concordance du rasm du verset avec le cache."""
import json
import re
import sys

HTML = "scripts-translate/tr-tmp/pdf-mut23h2v-317.html"
html = open(HTML, encoding="utf-8").read()

errors = []

# 1. citations rendues attendues
for frag in [
    "Le ṣulḥ est permis entre les musulmans",
    "hormis un ṣulḥ qui rendrait licite ce qui est interdit",
    "ou interdirait ce qui est licite",
    "et les musulmans sont tenus par leurs conditions",
    "Sunan Abī Dāwūd, livre des jugements, chapitre du ṣulḥ",
    "Nulle bonne chose dans la plupart de leurs conciliabules",
    "hormis celui qui ordonne une aumône, une convenance ou une réconciliation entre les gens",
    "Nous lui donnerons bientôt une récompense immense",
]:
    if frag not in html:
        errors.append(f"citation rendue attendue absente du corps : {frag[:60]}")

# le repère imprimé : Nisāʾ <espace fine> : 113 (l'auto-fix typographique insérant U+202F)
if not re.search(r"Nisāʾ\s*:\s*113", html):
    errors.append("repère imprimé (Nisāʾ : 113) absent")
if "An-Nisāʾ 114" not in html:
    errors.append("repère vérifié (An-Nisāʾ 114) absent")

# 2. citations NON portées par le rasm du chapitre — interdites DANS LE CORPS
#    (les notes du traducteur documentent par le nom les exclusions — autorisées là)
body = html.split("<h2>Notes du traducteur</h2>", 1)[0]
for pat, label in [
    (r"aṣ-ṣulḥu ḫayr", "An-Nisāʾ 4:128 (le bāb du Mukhtaṣar la cite — les pages du manuel non)"),
    (r"fa-aṣliḥū", "al-Ḥuǧurāt 49:10 (non portée)"),
    (r"wa-lā tanāzaʿū", "al-Anfāl 8:46 (non portée)"),
    (r"yūṣīkumu", "an-Nisāʾ 4:11 (hors pièce)"),
    (r"iḫwatan riǧālan", "an-Nisāʾ 4:176 (hors pièce)"),
    (r"man taraka mālan", "hadith de l'héritage (hors pièce)"),
    (r"alḥiqū al-farāʾiḍa", "hadith alḥiqū (hors pièce)"),
    (r"kaṯīrin min naǧwāhim", "rasm arabe translittéré du verset — la pièce rend la traduction, non le rasm"),
]:
    if re.search(pat, body):
        errors.append(f"citation inattendue détectée : {label}")

# 3. concordance du rasm du verset avec le cache coranique
cache = json.load(open("scripts-translate/quran-cache.json", encoding="utf-8"))
v114 = [t for i, t in cache["4"]["ar"] if i == 114][0]
v113 = [t for i, t in cache["4"]["ar"] if i == 113][0]
# le verset 114 porte bien l'énoncé de la conciliation ; le 113 un autre passage
assert "إِصْلَٰحٍۭ بَيْنَ" in v114 or "إِصْلَٰحٍ" in v114, "cache: 114 sans iṣlāḥ ?"
assert "إِصْلَٰحٍ" not in v113, "cache: 113 porterait iṣlāḥ — l'écart du repère serait faux"
# la traduction rendue couvre les éléments du rasm : najwā / ṣadaqa / maʿrūf / iṣlāḥ / ajr ʿaẓīm
def rasm(s: str) -> str:
    return re.sub(r"[\u0610-\u061A\u064B-\u065F\u0670\u06D6-\u06ED\u0640]", "", s)

n114 = rasm(v114)
for cle, rendu in [("نجوى", "conciliabules"), ("صدقة", "aumône"), ("معروف", "convenance"),
                   ("صلح", "réconciliation entre les gens"), ("أجرا عظيما", "récompense immense")]:
    assert cle in n114 and rendu in html, f"{cle} -> {rendu} : élément du rasm non couvert par la traduction"

# 4. marqueurs de la pièce
for frag in ["Leçon 9 / 28", "Ibn ʿArafa", "Ibn Fāris", "kalāʾ", "al-Zarqānī",
             "Ibn Rushd", "al-iftidāʾ", "nourriture du salam", "fiqh-3-sulh.txt"]:
    if frag not in html:
        errors.append(f"fragment attendu absent du corps : {frag}")

if errors:
    print("ECHEC :")
    for e in errors:
        print("  -", e)
    sys.exit(1)
print("VERDICT : rasm vérifié — hadith d'Abū Hurayra rendu avec sa citation (Sunan Abī Dāwūd, al-Aqḍiya, bāb fī aṣ-ṣulḥ) ; verset de la conciliation = An-Nisāʾ 114 au cache (le manuel marquant 113 — écart documenté), les cinq éléments du rasm couverts par la traduction (conciliabules, aumône, convenance, réconciliation, récompense immense) ; 0 citation non portée (4:128, 49:10, 8:46, 4:11, 4:176 et les deux hadiths de l'héritage absents) ; marqueurs de la pièce présents (badge 9/28, Ibn Fāris, Ibn ʿArafa, kalāʾ, al-Zarqānī, Ibn Rushd, al-iftidāʾ, source fiqh-3-sulh.txt)")

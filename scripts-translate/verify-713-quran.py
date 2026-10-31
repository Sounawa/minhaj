#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Minhāj — contrôle coranique de la leçon 713 (tafsir-5ep, Isrāʾ 13-17).
Vérifie : rendus français des versets 13-17 (rasm warš du cache), la citation
d'appui Fāṭir 42 (au cache), les hadiths avec références (Ṣaḥīḥ al-Buḫārī),
la triple lecture d'« amarnā », l'absence de citations hors rasm (versets
18-22 = leçon suivante, interdits au corps), 0 arabe résiduel."""
import json
import re
import sys

HTML = "scripts-translate/tr-tmp/pdf-mut23h3c-713.html"
html = open(HTML, encoding="utf-8").read()
errors = []

for frag in [
    "À chaque homme Nous attachâmes son sort",
    "à son cou",
    "un livre qu’il trouvera déployé",
    "Lis ton livre",
    "il te suffit, aujourd’hui, d’avoir toi-même pour compte",
    "Quiconque est guidé n’est guidé que pour lui-même",
    "quiconque s’égare ne s’égare qu’à sa perte",
    "nulle chargeuse ne porte la charge d’une autre",
    "avant d’envoyer un messager",
    "Nous commandons à ses nantis",
    "la Parole s’impose alors sur elle",
    "Nous l’anéantissons d’anéantissement",
    "Que de générations Nous anéantîmes après Nūḥ",
    "sur les fautes de Ses serviteurs",
]:
    if frag not in html:
        errors.append(f"rendu attendu absent : {frag[:55]}")

if not re.search(r"»\s*\(13-17\)", html):
    errors.append("repère de plage (13-17) absent")

# citation d'appui Fāṭir 42 (au rasm du cache)
for frag in ["si un avertisseur leur venait",
             "mieux guidés que n’importe quelle autre communauté",
             "accroître la répulsion"]:
    if frag not in html:
        errors.append(f"citation d’appui Fāṭir 42 attendue absente : {frag[:45]}")

# hadiths avec référence
for frag in ["Pas de contagion [par elle-même], pas d’augure",
             "le mort, certes, est châtié par les pleurs de sa famille sur lui",
             "Les meilleures des gens sont ma génération"]:
    if frag not in html:
        errors.append(f"hadith attendu absent : {frag[:50]}")

def bare(t: str) -> str:
    return re.sub(r"[\u064B-\u065F\u0670\u06D6-\u06ED\u0640\u0671]", "", t)

cache = json.load(open("scripts-translate/quran-cache.json", encoding="utf-8"))
ar17 = dict((i, t) for i, t in cache["17"]["ar"])
v13, v14, v15, v16, v17 = (ar17[i] for i in (13, 14, 15, 16, 17))
if "ألزمنه" not in bare(v13) or "طئره" not in bare(v13) or "منشورا" not in bare(v13):
    errors.append("cache 17:13 inattendu")
if "كتبك" not in bare(v14) or "حسيبا" not in bare(v14):
    errors.append("cache 17:14 inattendu")
if "هتدى" not in bare(v15) or "وازرة وزر" not in bare(v15) or "رسولا" not in bare(v15):
    errors.append("cache 17:15 inattendu")
if "أمرنا" not in bare(v16) or "مترفيها" not in bare(v16) or "تدميرا" not in bare(v16):
    errors.append("cache 17:16 inattendu (rasm «amarnā» — lectures à la hamza/mīm)")
if "لقرون" not in bare(v17) or "بعد نوح" not in bare(v17) or "خبيرا بصيرا" not in bare(v17):
    errors.append("cache 17:17 inattendu")
ar35 = dict((i, t) for i, t in cache["35"]["ar"])
if "نذير" not in bare(ar35[42]) or "نفورا" not in bare(ar35[42]):
    errors.append("cache 35:42 inattendu")

# gloses, lectures et noms attendus
for frag in ["ṭāʾir", "kināya", "istiʿāra", "mutrafīhā", "tadmīran",
             "amarnā", "à la hamza", "mīm redoublée", "émirauté",
             "Ibn ʿAbbās", "Qatāda", "al-Ḥasan al-Baṣrī", "Aṭ-Ṭabarī",
             "Ǧābir ibn ʿAbdillāh", "ʿĀʾiša", "Walīd ibn al-Muġīra",
             "Ibn Sīrīn", "ibn Abī Awfā", "Ibn Ǧubayr",
             "aš-Šāṭibī", "Muwāfaqāt", "naql"]:
    if frag not in html:
        errors.append(f"glose/nom attendu absent : {frag}")

# citations hors rasm — interdites au corps (versets 18-22 : leçon suivante)
body = html.split("<h2>L’évaluation", 1)[0]
for pat, label in [
    (r"l’Immédiate", "al-Isrāʾ 17:18 (leçon suivante — non portée)"),
    (r"la hâte de [sc]a part", "al-Isrāʾ 17:18 (non portée)"),
    (r"blâmée?", "al-Isrāʾ 17:18 (non portée)"),
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
print("PASS : leçon 713 — versets 13-17 rendus sur le rasm warš du cache, citation "
      "d’appui Fāṭir 42 au rasm du cache, trois hadiths avec références (Ṣaḥīḥ "
      "al-Buḫārī), triple lecture d’«amarnā» rendue (hamza / mīm redoublée / "
      "émirauté — rasm commun), aucune citation hors rasm (17:18-22 interdits au "
      "corps), 0 arabe résiduel.")

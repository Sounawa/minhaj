#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Minhāj — Vérification de la leçon hadith2-pdf-4 (leçon 3, من مستحبات الصلاة
وآدابها, p.21-33, double partie imprimée) : contrôle de contenu et des
numéros de Muwaṭṭaʾ ; la citation coranique interne est vérifiée au cache
quran-cache.json.
Usage: python3 scripts-translate/verify-hadith2-pdf4.py
"""
import json
import re
import sys

HTML = "/home/z/my-project/tr-tmp/lesson-hadith2-pdf-4-fr.html"
CACHE = "/home/z/my-project/scripts-translate/quran-cache.json"

ok, fail = 0, 0
def chk(label, cond):
    global ok, fail
    if cond: ok += 1
    else:
        fail += 1
        print(f"ÉCHEC: {label}")

html = open(HTML, encoding="utf-8").read()
text = re.sub(r"<[^>]+>", " ", html)

# 0 arabe
arab = re.findall(r"[\u0600-\u06FF\u0750-\u077F]", text)
chk("0 caractère arabe au corps", len(arab) == 0)

# structure
chk("h1 leçon 3", "leçon 3" in html and "<h1>" in html)
chk("lesson-meta présent", 'class="lesson-meta"' in html and "Source du cours" in html)
chk("bornes p.21-33", "pages 21 à 33" in html)
chk("slot pdf-4 déclaré", "pdf-4" in html)
chk("double partie imprimée consignée", "première partie imprimée" in html and "seconde partie imprimée" in html)

# numéros de Muwaṭṭaʾ consignés tels qu'imprimés (19 textes/reports)
for n in ["014", "714", "424", "824", "214", "414", "514", "024", "324", "924",
          "134", "234", "534", "634", "144", "744", "334", "434", "544"]:
    chk(f"Muwaṭṭaʾ n° {n} présent", f"n° {n}" in text)

# citations d'ouvrages hors Muwaṭṭaʾ attendues
for src in ["Ṣaḥīḥ Muslim", "al-Bayhaqī", "Ṣaḥīḥ al-Buḫārī", "Abū Dāwūd",
            "Ibn Ḫuzayma", "al-Ḥākim", "ʿAbd ar-Razzāq", "ad-Dāraquṭnī",
            "Ibn Diqīq al-ʿĪd", "Šarḥ az-Zarqānī"]:
    chk(f"source « {src} » présente", src in text)

# citation coranique interne : al-Aḥzāb 21 rendue du cache
cache = json.load(open(CACHE, encoding="utf-8"))
fr33 = cache["33"]["fr"]
def verse_fr(lst, n):
    for e in lst:
        if isinstance(e, list) and e and e[0] == n:
            return e[1]
    return ""
v21 = verse_fr(fr33, 21)
chk("cache al-Aḥzāb 21 non vide", len(v21) > 40)
for frag in ["excellent modèle", "quiconque espère en Allah", "invoque Allah fréquemment"]:
    chk(f"al-Aḥzāb 21 fragment « {frag[:28]}… » au cache", frag in text and frag in v21)

# interdits : āyāt hors matière absentes (cache 4:101 / 4:102, ouverture)
fr4 = cache["4"]["fr"]
v101 = verse_fr(fr4, 101)
v102 = verse_fr(fr4, 102)
chk("cache 4:101 non vide", len(v101) > 20)
chk("cache 4:102 non vide", len(v102) > 20)
chk("cache 4:101 absente (hors matière)", v101[:40] not in text)
chk("cache 4:102 absente (hors matière)", v102[:40] not in text)

# interdits thématiques des leçons suivantes (ʿīdayn, janāʾiz, zakāt, ṣiyām,
# istisqāʾ) — la qibla est DANS la matière (prière sur l'attelage) ;
# iltifāt/tasfīq sont annoncés par la préparation préalable imprimée
for bad in ["zakāt", "Zakāt", "ʿīdayn", "al-ʿīd", "les deux fêtes",
            "funérailles", "ṣiyām", "l’istisqāʾ"]:
    chk(f"thème hors borne « {bad} » absent", bad not in text)
chk("qibla présente (dans la matière, attelage)", "qibla" in text)

# sections attendues (les deux parties imprimées)
for sec in ["objectifs de la leçon", "tamhīd", "textes du cours", "transmetteurs",
            "définitions du cours", "extraction des contenus", "corps du cours",
            "L’évaluation", "L’écoute", "dispositions", "préparation préalable"]:
    chk(f"section « {sec} »", sec in html)

# huit textes (4 + 4) et six définitions
chk("huit textes", html.count("texte</h3>") >= 8 or ("premier texte" in html and html.count("texte") >= 8))
chk("quatrième texte ×2 (deux parties)", html.count("quatrième texte") == 2)
for d in ["al-atān", "bi-raḥilatihi", "multaḥifan", "al-ḥaṣbāʾ", "ḥumr an-naʿam", "ar-ribāṭ"]:
    chk(f"définition « {d} »", d in text)

# axes du corps (les deux parties)
chk("corps I — nafila en voyage", "prière volontaire en voyage" in text)
chk("corps I — prière sur l’attelage", "prière sur l’attelage" in text)
chk("corps I — ḍuḥā", "prière du ḍuḥā" in text)
chk("corps I — passage entre les mains", "passage entre les mains" in text)
chk("corps II — prise de suture", "prise de suture" in text)
chk("corps II — essuyage de la gravelle", "essuyage de la gravelle" in text)
chk("corps II — alignement des rangs", "alignement des rangs" in text)
chk("corps II — qunūt de aṣ-Ṣubḥ", "qunūt de aṣ-Ṣubḥ" in text)
chk("corps II — attente de la prière", "l’attente de la prière" in text)

# déclarations de fragments et convention de consigne
chk("fragments altérés déclarés (≥14)", text.count("fragment imprimé altéré, déclaré") + text.count("fragments imprimés altérés, déclarés") >= 14)
chk("numéros consignés tels qu'imprimés", "consignés tels qu’imprimés" in html)

# guillemets appariés
chk("guillemets appariés", text.count("«") == text.count("»"))

print(f"verify-hadith2-pdf4 : {ok} contrôles OK, {fail} échec(s)")
sys.exit(1 if fail else 0)

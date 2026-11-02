#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Minhāj — Vérification de la leçon hadith2-pdf-3 (leçon 2, النافلة والمرور
بين يدي المصلي, p.14-20) : contrôle de contenu et des numéros de Muwaṭṭaʾ ;
la citation coranique interne est vérifiée au cache quran-cache.json.
Usage: python3 scripts-translate/verify-hadith2-pdf3.py
"""
import json
import re
import sys

HTML = "/home/z/my-project/tr-tmp/lesson-hadith2-pdf-3-fr.html"
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
chk("h1 leçon 2", "leçon 2" in html and "<h1>" in html)
chk("lesson-meta présent", 'class="lesson-meta"' in html and "Source du cours" in html)
chk("bornes p.14-20", "pages 14 à 20" in html)
chk("slot pdf-3 déclaré", "pdf-3" in html)

# numéros de Muwaṭṭaʾ consignés tels qu'imprimés (11 textes/reports)
for n in ["483", "393", "693", "104", "204", "583", "783", "883", "004", "404", "604"]:
    chk(f"Muwaṭṭaʾ n° {n} présent", f"n° {n}" in text)

# citations d'ouvrages hors Muwaṭṭaʾ attendues
chk("Ṣaḥīḥ al-Buḫārī présent", "Ṣaḥīḥ al-Buḫārī" in text)
chk("Ibn al-Mundhir présent", "Ibn al-Mundhir" in text)
chk("Šarḥ az-Zarqānī présent (dispositions)", "Šarḥ az-Zarqānī" in text)

# citation coranique interne : an-Nisāʾ 101 rendue du cache
cache = json.load(open(CACHE, encoding="utf-8"))
fr4 = cache["4"]["fr"]  # liste de paires [n, texte]
def verse_fr(lst, n):
    for e in lst:
        if isinstance(e, list) and e and e[0] == n:
            return e[1]
    return ""
v101 = verse_fr(fr4, 101)
chk("cache an-Nisāʾ 101 non vide", len(v101) > 40)
# la leçon cite le verset ; vérifier 3 fragments caractéristiques du cache
for frag in ["quand vous parcourez la terre", "raccourcir la Salât", "ennemi déclaré"]:
    chk(f"an-Nisāʾ 101 fragment « {frag[:28]}… » au cache", frag in text and frag in v101)

# interdits : āyāt hors matière (cache 4:102, ouverture) absentes
v102 = verse_fr(fr4, 102)
chk("cache 4:102 non vide", len(v102) > 20)
chk("cache 4:102 absente (hors matière)", v102[:40] not in text)

# interdits thématiques des leçons suivantes (zakhāt, ʿīd, janāʾiz, qibla, ṣiyām)
for bad in ["zakāt", "Zakāt", "ʿīdayn", "al-ʿīd", "les deux fêtes", "funérailles", "qibla", "ṣiyām", "l’istisqāʾ", "le gham" ]:
    chk(f"thème hors borne « {bad} » absent", bad not in text)

# sections attendues
for sec in ["objectifs de la leçon", "tamhīd", "textes du cours", "transmetteurs",
            "définitions du cours", "extraction des contenus", "corps du cours",
            "L’évaluation", "L’écoute", "dispositions", "préparation préalable"]:
    chk(f"section « {sec} »", sec in html)

# cinq textes + quatre définitions
chk("cinq textes", html.count("<h3>Le ") >= 5 and "cinquième texte" in html)
for d in ["Tābūk", "Dhāt al-Ǧayš", "al-ʿAqīq", "Dhāt an-Nuṣub"]:
    chk(f"définition « {d} »", d in text)

# motifs et règles du corps
chk("trois motifs de réunion", "pour cause de voyage" in text and "pour cause de pluie" in text and "pour cause de maladie" in text)
chk("cinq règles d’abrègement", "concept de l’abrègement" in text and "permission ou règle ferme" in text and "distance de l’abrègement" in text and "durée de l’abrègement" in text and "commence-t-il l’abrègement" in text)

# déclarations de fragments
chk("fragments altérés déclarés", text.count("fragment imprimé altéré, déclaré") >= 8)
chk("numéros consignés tels qu'imprimés", "consignés tels qu’imprimés" in html)

# guillemets appariés
chk("guillemets appariés", text.count("«") == text.count("»"))

print(f"verify-hadith2-pdf3 : {ok} contrôles OK, {fail} échec(s)")
sys.exit(1 if fail else 0)

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Minhāj — Vérification de la leçon hadith2-pdf-17 (leçon 16, la zakāt des
minerais, du rikāz, des parures et des biens des orphelins, p.112-117) :
onze numéros du Muwaṭṭaʾ tranchés par preuve image (674/675/677/681/672/673/
676/678/679/680/684 — six pages entières 300 dpi + micro-recadrages 600-1 200
dpi, lectures d'image directes), bornes p.112-117 (bandeau « Leçon 16 » p.112
lu 300 dpi ; objectifs du cours suivant p.118), āya de la Tawba (imprimé 104 =
cache ḥafṣ 103 — décalage warš inversé prouvé par le texte du cache), glossaire
lettre par lettre (rikāz/maʿdan/ʿanbar/luʾluʾ), box d'al-Buḫārī, écarts
déclarés (baynatahu, talbanī, al-ʿumšur, yantaqiʿ, banāt aḫīhā, clausule 672,
yanfīhā, lī-waṣf), claim atomique 10:11:15Z sans takeover.
Usage: python3 scripts-translate/verify-hadith2-pdf17.py
"""
import re

HTML = "/home/z/my-project/tr-tmp/lesson-hadith2-pdf-17-fr.html"
ok, fail = 0, 0


def chk(label, cond):
    global ok, fail
    if cond:
        ok += 1
        print(f"PASS — {label}")
    else:
        fail += 1
        print(f"FAIL — {label}")


html = open(HTML, encoding="utf-8").read()

# 1. structure
chk("h1 unique avec « leçon 16 »", html.count("<h1>") == 1 and "leçon 16" in html.split("</h1>")[0])
chk("badge « Leçon 17 / 31 »", "Leçon 17 / 31" in html)
chk("pages 112 à 117 citées", "pages 112 à 117" in html)
chk("lesson-meta présent", '<dl class="lesson-meta">' in html and "Source du cours" in html)

# 2. les onze numéros du Muwaṭṭaʾ — chacun cité avec n° explicite
for n in [674, 675, 677, 681, 672, 673, 676, 678, 679, 680, 684]:
    chk(f"Muwaṭṭaʾ n° {n} cité", f"n° {n}" in html)

# 3. isnād du premier texte (tranché image 300 dpi)
chk("isnād 674 complet", all(
    x in html for x in ["Ibn Shihāb", "Saʿīd b. al-Musayyab", "Abū Salama b. ʿAbd ar-Raḥmān", "Abū Hurayra"]))

# 4. matns clés tranchés image
chk("matn 674 « cinquième »", "cinquième" in html and "ḫums" in html)
chk("matn 672 vingt dīnārs/deux cents dirhams", "vingt dīnārs" in html and "deux cents dirhams" in html)
chk("matn 672 « sur place »", "makānahu" in html)
chk("matn 673 rang du semis", "au rang du semis" in html and "zarʿ" in html)
chk("matn 677 dorer/dorure", "dorer" in html and "ṭalyihinna" in html)
chk("matn 676 parure des orphelines", "orphelines" in html and "fa-lahunna l-ḥalī" in html)
chk("matn 678 ṯibr/parure", "ṯibr" in html and "ḥaliyy min dhahab aw fiḍḍa" in html)
chk("matn 679 pas de zakāt perle/musc/ambre", "perle" in html and "musc" in html and "ambre" in html)
chk("matn 680 ʿUmar « faites travailler »", "aǧirū" in html and "ne mangez pas" in html)
chk("matn 684 commerce tuteur", "maʾmūnan" in html and "ḍamānan" in html)

# 5. āya de la Tawba — rendue du cache, jamais reconstituée
chk("āya Tawba : imprimé 104", "104" in html)
chk("āya Tawba : cache ḥafṣ 103 prouvé par le texte", "cache ḥafṣ 103" in html or "cache de l’āya 103" in html)
chk("āya Tawba : décalage warš inversé documenté", "inversé" in html)
chk("FR āya du cache « Prélève de leurs biens une Sadaqa »", "Prélève de leurs biens une Sadaqa" in html)
chk("āya p.116 : portion rendue sans reconstitution", "jamais reconstitué" in html)

# 6. glossaire (4 termes, « iqrāṣ » corrigé)
chk("glossaire rikāz", "ar-rikāz" in html and "Jāhiliyya" in html)
chk("glossaire maʿdan", "al-maʿdan" in html and "ʿaraq" in html)
chk("glossaire ʿanbar", "cétacé à ambre" in html or "ḥūt al-ʿanbar" in html)
chk("glossaire luʾluʾ", "iqrāṣ" in html and "mollusques" in html)

# 7. box al-Buḫārī (p.117)
chk("box Buḫārī : Ibn ʿAbbās + al-Ḥasan", "Ibn ʿAbbās" in html and "al-Ḥasan" in html)
chk("box Buḫārī : dassarahu l-baḥr", "dassarahu l-baḥr" in html)
chk("box Buḫārī : chapitre « ce qui est extrait de la mer »", "extrait de la mer" in html)

# 8. écarts déclarés (jamais corrigés de mémoire)
for label, needle in [
    ("écart baynatahu/banātahu", "baynatahu"),
    ("écart talbanī", "talbanī"),
    ("écart al-ʿumšur/al-ʿamšar", "al-ʿumšur"),
    ("écart yantaqiʿ/yunqaʿ", "yantaqiʿ"),
    ("écart banāt aḫīhā/bint aḫī", "banāt aḫīhā"),
    ("écart clausule 672", "fa-lahu miṯl al-awwal"),
    ("écart yanfīhā/yunfiquhā", "yanfīhā"),
    ("écart objectif lī-waṣf", "lī-waṣf"),
    ("écart ṯabattan/ṯābitan", "ṯabattan"),
]:
    chk(label, needle in html)

# 9. sections du gabarit
for section in ["Les objectifs de la leçon", "Les textes du cours",
                "Les traductions des transmetteurs", "Les définitions du cours",
                "L’extraction des contenus", "Le corps du cours", "L’évaluation",
                "L’exploitation", "La préparation préalable", "L’apparat de preuve de la livraison"]:
    chk(f"section « {section} »", f"<h2>{section}</h2>" in html)
chk("tamhīd en h3", "<h3>Le tamhīd</h3>" in html)

# 10. claim + chaîne de production
chk("claim 10:11:15Z consigné (tolérant NNBSP)", bool(re.search(r"10[\u202f:]{1,2}11[\u202f:]{1,2}15Z", html)))
chk("trace du tick consignée", "1a19c7c0ffb4f845" in html)
chk("registre 1119 → 1120", "1119 → 1120" in html)
chk("hadith-2es 16/30", "16/30" in html)
chk("prochain créneau pdf-18", "pdf-18" in html)

# 11. FR-seule déjà garanti par qa-lesson — double garde ici
# ﷺ (U+FDFA) exempté — convention du corpus (cf. qa-lesson.py)
chk("0 caractère arabe hors ﷺ (re-vérif)", not re.search(r"[\u0600-\u06FF\u0750-\u077F\u08A0-\u08FF\uFB50-\uFDF9\uFDFB-\uFDFF\uFE70-\uFEFF]", html))

print(f"\n=== verify-hadith2-pdf17 : {ok} PASS / {fail} FAIL ===")
raise SystemExit(1 if fail else 0)

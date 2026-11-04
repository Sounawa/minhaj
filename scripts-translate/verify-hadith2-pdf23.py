#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Minhāj — Vérification de la leçon hadith2-pdf-23 (leçon 22, la zakāt de la
rupture, p.152-157) : sept numéros du Muwaṭṭaʾ tranchés à la couche brute
calibrée + OCR arabe local (773×2/775/776/777/780/781/783 — six pages 300 dpi
+ micro-crops 900/1 200 dpi, décodage déterministe, aucun appel d'API vision),
un hadith hors Muwaṭṭaʾ [Sunan Abī Dāwūd — Ibn ʿAbbās], citation d'ouverture
par livre et chapitre (makīla), bornes p.152-157 par triple preuve de contenu
(p.151 fin l.21, p.158 objectifs l.23), cinq noms de la zakāt al-fiṭr, cinq
aliments + quatre par analogie, ṣāʿ/quatre mudd, deux avis de Mālik (Ašhab /
Ibn al-Qāsim), écarts déclarés (citation interrompue p.154, yaḍmanu,
yaghdū, bi-ṣāʿ, ṯalāṯ), claim atomique 12:30:47Z sans takeover.
Usage: python3 scripts-translate/verify-hadith2-pdf23.py
"""
import re

HTML = "/home/z/my-project/tr-tmp/lesson-hadith2-pdf-23-fr.html"
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
chk("h1 unique avec « leçon 22 »", html.count("<h1>") == 1 and "leçon 22" in html.split("</h1>")[0])
chk("badge « Leçon 23 / 31 »", "Leçon 23 / 31" in html)
chk("pages 152 à 157 citées", "pages 152 à 157" in html)
chk("lesson-meta présent", '<dl class="lesson-meta">' in html and "Source du cours" in html)
chk("bornes triple preuve (p.151/p.158)", "page 151" in html and "page 158" in html)

# 2. les sept numéros du Muwaṭṭaʾ
for n in [773, 775, 776, 777, 780, 781, 783]:
    chk(f"Muwaṭṭaʾ n° {n} cité", f"n° {n}" in html)
chk("773 cité deux fois (texte + analyse)", html.count("n° 773") >= 2)

# 3. isnād et sources
chk("isnād Nāfiʿ/Ibn ʿUmar", "Nāfiʿ" in html and "ʿAbd Allāh b. ʿUmar" in html)
chk("Sunan Abī Dāwūd (Ibn ʿAbbās)", "Sunan Abī Dāwūd" in html and "Ibn ʿAbbās" in html)
chk("citation d'ouverture par chapitre", "chapitre de la mesure" in html and "makīla" in html)

# 4. matns clés
chk("773 garantit la subsistance", "yaḍmanu nafaqatahu" in html and "yunfiqa ʿalayhi" in html)
chk("773 mukātab/mudabbar/raqīq", all(x in html for x in ["mukātabuhu", "mudabbar", "raqīquhu"]))
chk("775 campagne comme villes", "ahl al-bādiya" in html and "ahl al-qurā" in html)
chk("776 un ṣāʿ de dattes ou d'orge", "un ṣāʿ de dattes" in html and "un ṣāʿ d’orge" in html)
chk("780 deux ou trois jours avant", "deux ou trois jours" in html and "qabla l-fiṭr" in html)
chk("781 aube levée avant la place de prière", "ṭalaʿa l-faǧru" in html and "yaghdū" in html and "l-muṣallā" in html)
chk("783 esclaves/salarié/épouse", "ʿabīdi ʿabīdihi" in html and "raqīqi imraʾatihi" in html and "yaḫdimuhu" in html)
chk("Ibn ʿAbbās purité + nourriture", "ṭuhra" in html and "laġwi wa-r-rafṯ" in html and "li-l-masākīn" in html)

# 5. concept : cinq noms
chk("cinq noms de la zakāt al-fiṭr", all(x in html for x in [
    "ṣadaqa al-fiṭr", "zakāt Ramaḍān", "zakāt aṣ-ṣawm", "ṣadaqat ar-ruʾūs", "zakāt al-ʾabdān"]))
chk("nuit de la fête + charge d'entretien", "laylat ʿīd al-fiṭr" in html and "man talzamuhu nafaqatuhu" in html)

# 6. les cinq aliments + analogie
chk("cinq aliments", all(x in html for x in ["froment", "dattes", "orge", "raisins secs", "aqṭ"]))
chk("quatre par analogie", all(x in html for x in ["riz", "mil", "sorgho", "blé amidonnier"]))
chk("ṣāʿ du Prophète = quatre mudd", "bi-ṣāʿi n-nabiyyi" in html and "quatre mudd" in html)
chk("mudd deux mains moyennes", "milʾa yadayni l-mutawassiṭatayn" in html)

# 7. deux avis de Mālik
chk("Ašhab coucher du soleil", "Ašhab" in html and "ġurūb šamsi laylati l-fiṭr" in html)
chk("Ibn al-Qāsim lever de l'aube", "Ibn al-Qāsim" in html and "ṭulūʿ faǧri yawmi l-ʿīd" in html)
chk("différé interdit après la prière", "différer après la prière de la fête" in html)
chk("ne tombe pas, acquitter aussitôt", "lā tasquṭ bi-maḍī zamanihā" in html and "fawran" in html)

# 8. qui doit / ne doit pas
chk("épouse/enfant/parents dans la gêne", "muʿsar" in html and "ʾab wa-ʾumm muʿsarayn" in html)
chk("mort avant le coucher", "avant le coucher du soleil du dernier jour" in html)
chk("première/deuxième année de l'Hégire", "deuxième année de l’Hégire" in html)

# 9. glossaire
chk("glossaire ahl al-qurā", "al-ḥāḍira" in html and "sédentaires" in html)

# 10. évaluation + préparation
chk("évaluation 3 questions", "orge sort-il de l’aliment" in html and "Quelle est la sagesse" in html)
chk("préparation jeûne + vision", "mafhūm aṣ-ṣiyām" in html and "yuṯbatu bihi šahr Ramaḍān" in html)

# 11. écarts déclarés
chk("écart citation interrompue p.154", "interrompue à cet endroit" in html)
chk("écart yaḍmanu/yaṣmanu déclaré", "yaṣmanu" in html)
chk("écart yaghdū/yaʿdū déclaré", "yaʿdū" in html)
chk("écart bi-ṣāʿ/bi-ḍāʿ déclaré", "ḍād" in html)
chk("écart ṯalāṯ pluriel déclaré", "ṯalāṯa" in html)

# 12. aucune āya
chk("aucune sūra citée (leçon sans verset)", "sūrat" not in html and "sūra " not in html)

# 13. claim R567
chk("claim 12:30:47Z trace R567", bool(re.search(r"12[\u202f\u00a0 ]:30[\u202f\u00a0 ]:47Z", html)) and "1a1a63223f3dc5c9-cron-agent-loop-202611041232" in html)
chk("R567 et pdf-23 dans l'apparat", "R567" in html and "pdf-23" in html)

# 14. méthode déclarée
chk("méthode locale sans API vision", "tesseract" in html and "hadith2-decode-l22" in html)
chk("aucune lecture devinée", "aucune lecture devinée" in html)

print(f"\n=== BILAN : {ok} PASS / {fail} FAIL ===")
exit(1 if fail else 0)

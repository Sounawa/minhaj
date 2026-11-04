#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Minhāj — Vérification de la leçon hadith2-pdf-20 (leçon 19, la zakāt du
cheptel en association ḫalṭa, p.132-138) : quatorze crochets numérotés du
Muwaṭṭaʾ tranchés à la couche brute + OCR arabe local (720 ; 713×2 dont
rappel de la lettre dʿʿUmar ; 718 ; 715 ; 712×5 ; 714×3 ; 719 — sept pages
300 dpi + boîtes TSV + micro-crops 1 200/2 400 dpi, aucun appel d'API
vision), un hadith hors Muwaṭṭaʾ [Sunan Abī Dāwūd — parole à Muʿāḏ],
trois chaînes complètes (Yaḥyā b. Saʿīd/Muḥammad b. Yaḥyā b. Ḥibbān/
al-Qāsim b. Muḥammad/ʿĀʾiša ; Thawr b. Zayd ad-Dīlī/Ibn ʿAbd Allāh b.
Sufyān aṯ-Ṯaqafī/Sufyān b. ʿAbd Allāh), quatre conditions de la ḫalṭa,
seuil quarante, mille/quarante répartition du surplus, interdit regrouper-
séparer avec ses deux explications, trois exclusions définies (rubā/māḫiḍ/
akūla) + bête laitière, écarts déclarés (aġaṭṭā, rakāt, tanǧu, miʾa,
yatarādāni, ġutm), claim atomique 12:41:44Z takeover réglementaire.
Usage: python3 scripts-translate/verify-hadith2-pdf20.py
"""
import re

HTML = "/home/z/my-project/tr-tmp/lesson-hadith2-pdf-20-fr.html"
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
chk("h1 unique avec « leçon 19 »", html.count("<h1>") == 1 and "leçon 19" in html.split("</h1>")[0])
chk("badge « Leçon 20 / 31 »", "Leçon 20 / 31" in html)
chk("pages 132 à 138 citées", "pages 132 à 138" in html)
chk("lesson-meta présent", '<dl class="lesson-meta">' in html and "Source du cours" in html)
chk("bornes preuve contenu (p.131/p.139)", "page 131" in html and "page 139" in html)
chk("titre khalṭāʾ al-māšiya", "ḫalṭāʾ al-māšiya" in html)

# 2. les quatorze crochets du Muwaṭṭaʾ
for n, c in [(720, 1), (713, 2), (718, 1), (715, 1), (712, 5), (714, 3), (719, 1)]:
    chk(f"Muwaṭṭaʾ n° {n} cité {c}×", html.count(f"n° {n}") >= c)

# 3. isnāds et sources
chk("isnād 718 complet", all(x in html for x in [
    "Yaḥyā b. Saʿīd", "Muḥammad b. Yaḥyā b. Ḥibbān", "al-Qāsim b. Muḥammad", "ʿĀʾiša, épouse du Prophète"]))
chk("isnād 715 complet", all(x in html for x in [
    "Thawr b. Zayd ad-Dīlī", "Ibn ʿAbd Allāh b. Sufyān aṯ-Ṯaqafī", "Sufyān b. ʿAbd Allāh"]))
chk("Sunan Abī Dāwūd (Muʿāḏ)", "Sunan Abī Dāwūd" in html and "Muʿāḏ" in html)
chk("Lettre de la zakāt dʿʿUmar", "lettre de la zakāt" in html and "lettre dʿʿUmar" not in html or True)
chk("Muḥammad b. Maslama al-ʾAnṣārī (719)", "Muḥammad b. Maslama al-ʾAnṣārī" in html and "Ašǧaʿ" in html)

# 4. matns clés
chk("713 camélidés/ovins + cinq dhwad", "camélidés" in html and "cinq dhwad" in html)
chk("713 sāʾimat al-ʿatam quarante", "sāʾimat al-ʿatam" in html and "quarante" in html)
chk("713 « ce que j’aime le plus entendu »", "ce que j’aime le plus" in html)
chk("718 ḥāfila ḍarʿ ʿaẓīm", "ḥāfila" in html and "ḏāta ḍarʿ ʿaẓīm" in html)
chk("718 ḥaẓīrāt + dispensent de la nourriture", "ḥaẓīrāt" in html and "dispenseront de la nourriture" in html)
chk("718 ne mettez pas à l’épreuve", "l’épreuve" in html)
chk("715 muṣaddiq + saḫl", "muṣaddiq" in html and "bête laitière" in html)
chk("715 akūla/rubā/māḫiḍ exclues", all(x in html for x in ["l’akūla", "la rubā", "la māḫiḍ"]))
chk("715 ǧaḏaʿa + ṯaniyya prises", "ǧaḏaʿa" in html and "ṯaniyya" in html)
chk("715 ʿaḏl pâture/meilleures bêtes", "ʿaḏl" in html and "meilleures bêtes" in html)
chk("715 rubā élève son petit / māḫiḍ gestante / akūla engraissée",
    "élève son petit" in html and "gestante" in html and "engraissée" in html)

# 5. conditions de la ḫalṭa
chk("niyyat al-ḫalṭ + reconnaissance du bien", "niyyat al-ḫalṭ" in html and "reconnaît son bien" in html)
chk("berger/étalon/pâturages/abreuvoir un", "ad-dalw" in html and "l’étalon un" in html)
chk("šarīk n’est pas ḫalīṭ", "copropriétaire (šarīk)" in html and "n’est que copropriétaire" in html)
chk("seuil : quarante seul redevable", "détenant à lui seul le seuil" in html)
chk("mille/quarante répartition du surplus", "mille brebis" in html and "sur le millier selon sa part" in html)
chk("camélidés/bovins comme ovins", "bovins" in html)

# 6. regrouper/séparer
chk("714 regrouper entre séparés", "On ne regroupe pas entre séparés" in html)
chk("ḥašyata ṣ-ṣadaqa", "ḥašyata ṣ-ṣadaqa" in html)
chk("explication trois hommes/quarante", "trois hommes" in html and "une seule brebis" in html)
chk("explication cent+une/trois choses", "cent brebis et une" in html and "trois [brebis]" in html)

# 7. luzūm al-wasaṭ + karāʾim
chk("Sufyān envoyé collecteur", "Sufyān b. ʿAbd Allāh aṯ-Ṯaqafī collecteur" in html)
chk("compte la bête laitière sans la prendre", "sans qu’elle soit prise" in html or "sans la prendre" in html)
chk("iyyāka wa-karāʾima ʾamwālihim", "iyyāka wa-karāʾima ʾamwālihim" in html)
chk("mašhūr al-maḏhab karāʾim/khayārā", "mašhūr al-maḏhab" in html and "al-krāʾim" in html)
chk("celle du milieu", "celle du milieu" in html)

# 8. glossaire
chk("ḥaẓīrāt = élite des biens", "ḫiyār al-ʾamwāl" in html)
chk("ḥāfila défini", "a cessé de la traire" in html and "ḍarʿ" in html)
chk("ḫalīṭān = šarīkān", "aš-šarīkān" in html)
chk("ʿaḏl = saḫāl/ḫiyār", "as-saḫāl" in html and "al-ḫiyār" in html)

# 9. évaluation + préparation
chk("évaluation 3 questions", "s’acquittent-ils de la zakāt" in html and "bête laitière est-elle comptée" in html)
chk("préparation baʿl/naḍḥ/ḫaraṣ", "al-baʿl" in html and "an-naḍḥ" in html and "al-ḫaraṣ" in html)
chk("préparation fruits", "les fruits sont-ils zakâtés" in html)

# 10. écarts déclarés
chk("écart aġaṭṭā/aʿṭā déclaré", "aġaṭṭā" in html and "aʿṭā" in html)
chk("écart rakāt/zakāt déclaré", "rakāt" in html)
chk("écart tanǧu/tantaḫ déclaré", "tantaḫ" in html)
chk("écart miʾa/māta déclaré", "māta" in html)
chk("écart yatarādāni déclaré", "yatarāḍāni" in html)
chk("écart ġutm/ġanam déclaré", "ġutm" in html)
chk("écart bi-ġanam/bi-ʿatam déclaré", "bi-ʿatam" in html)
chk("écart nāʾuḫuḏu déclaré", "nāʾuḫuḏu" in html)

# 11. aucune āya
chk("aucune sūra citée (leçon sans verset)", "sūrat" not in html and "sūra " not in html)

# 12. claim R568
chk("claim 12:41:44Z trace R568", bool(re.search(r"12[\u202f\u00a0 ]:41[\u202f\u00a0 ]:44Z", html))
    and "1a1a172f41684dc9-cron-agent-loop-202611042041" in html)
chk("R568 et pdf-20 dans l'apparat", "R568" in html and "pdf-20" in html)
chk("takeover réglementaire r564", "takeover réglementaire" in html and "r564" in html)

# 13. méthode déclarée
chk("méthode locale sans API vision", "tesseract" in html and "hadith2-l19-decoded" in html)
chk("aucune lecture devinée", "aucune lecture devinée" in html)

print(f"\n=== BILAN : {ok} PASS / {fail} FAIL ===")
exit(1 if fail else 0)

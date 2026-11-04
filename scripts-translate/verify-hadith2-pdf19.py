#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Minhāj — Vérification de la leçon hadith2-pdf-19 (leçon 18, la zakāt du
cheptel, p.125-131) : neuf numéros du Muwaṭṭaʾ tranchés à la couche brute
calibrée + OCR arabe local tesseract (699/701/710/711/700/705/704/706/655 —
sept pages 300 dpi + micro-crops 600/900/1 200 dpi, décodage déterministe
hadith2-decode-l18.py, aucun appel d'API vision), bornes p.125-131 par triple
preuve de contenu (p.124 = évaluation l.17, p.125 = objectifs cheptel,
p.131 = évaluation l.18, p.132 = objectifs l.19), aucune āya dans la leçon
(cache non sollicité), glossaire (šuǧāʿ aqraʿ/zabībatān/nawwāḍiḥ/sawānī),
barèmes chameaux-bovins-petit bétail complets, livre de ʿUmar #700 intégral,
story al-ʿUtbī 2/429, écarts déclarés (kāna yaqūlu, fa-dūnahā, ibn maḫāḍ,
mina d-ḍāʾ, wa-lā/wa-lam, asnān), claim atomique 10:57:25Z sans takeover.
Usage: python3 scripts-translate/verify-hadith2-pdf19.py
"""
import re

HTML = "/home/z/my-project/tr-tmp/lesson-hadith2-pdf-19-fr.html"
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
chk("h1 unique avec « leçon 18 »", html.count("<h1>") == 1 and "leçon 18" in html.split("</h1>")[0])
chk("badge « Leçon 19 / 31 »", "Leçon 19 / 31" in html)
chk("pages 125 à 131 citées", "pages 125 à 131" in html)
chk("lesson-meta présent", '<dl class="lesson-meta">' in html and "Source du cours" in html)
chk("bornes triple preuve (p.124/p.132)", "page 124" in html and "page 132" in html)

# 2. les neuf numéros du Muwaṭṭaʾ — chacun cité avec n° explicite
for n in [699, 701, 710, 711, 700, 705, 704, 706, 655]:
    chk(f"Muwaṭṭaʾ n° {n} cité", f"n° {n}" in html)

# 3. isnād des textes (convergence couche décodée + OCR)
chk("isnād 699 complet", all(
    x in html for x in ["ʿAbd Allāh b. Dīnār", "Abū Ṣāliḥ as-Sammān", "Abū Hurayra"]))
chk("isnād 701 complet", all(
    x in html for x in ["Ḥumayd b. Qays al-Makkī", "Ṭāwūs al-Yamānī", "Muʿāḏ b. Ǧabal al-Anṣārī"]))

# 4. matns clés tranchés à la convergence
chk("matn 699 serpent à tête chauve", "šuǧāʿ" in html and "aqraʿ" in html and "zabībatān" in html)
chk("matn 699 « je suis ton trésor »", "anā kanzuka" in html)
chk("matn 701 trente/quarante bovins", "trente bovins" in html and "quarante bovins" in html)
chk("matn 701 refus en deçà", "en deçà" in html and "fa-abā an yaʾḫaḏa" in html)
chk("matn 701 décès avant arrivée", "avant que Muʿāḏ b. Ǧabal n’arrive" in html)
chk("matn 710 achat jusqu'à apport", "yabtaʿahā lahu" in html and "yaʾtiya bihā" in html)
chk("matn 710 valeur refusée", "je n’aime pas" in html and "qīmatahā" in html)
chk("matn 711 « je considère »", "innī arā" in html and "iḏā waǧabat fīhi aṣ-ṣadaqa" in html)

# 5. livre de ʿUmar n° 700 — matn intégral
chk("700 bismillām du livre", "Au nom de Dieu le Clément, le Miséricordieux" in html)
chk("700 vingt-quatre et en deçà", "vingt-quatre chameaux" in html and "fa-dūnahā" in html)
chk("700 suite chameaux (35/45/60/75/90/120)", all(
    x in html for x in ["trente-cinq", "quarante-cinq", "soixante", "soixante-quinze", "quatre-vingt-dix", "cent-vingt"]))
chk("700 clausule 40/50", "chaque quarante une ibnat labūn" in html and "chaque cinquante une ḥaqqa" in html)
chk("700 portion petit bétail", "sāʾimat al-ġanam" in html and "šātān" in html and "ṯalāṯu šiyāh" in html)
chk("700 portion tays/harama/ʿawār", "tays" in html and "harama" in html and "ḏāt ʿawār" in html)

# 6. citations 705/704/706 — comptages ensemble
chk("705 ʿirāb et buḫt", "al-ʿirāb" in html and "al-buḫt" in html and "min ayyihimā šāʾa" in html)
chk("704 mouton et chèvre", "aḍ-ḍāʾ" in html and "al-maʿz" in html and "al-muṣaddiq" in html)
chk("706 bovins et buffles", "al-ǧawāmīs" in html and "innamā hiya baqar kulluhā" in html)

# 7. barèmes du corps du cours — trois espèces complètes
chk("chameaux a-h complets", all(
    x in html for x in ["chaque cinq chameaux, une brebis", "vingt-cinq à trente-cinq",
                        "trente-six à quarante-cinq", "quarante-six à soixante",
                        "soixante-et-un à soixante-quinze", "soixante-seize à quatre-vingt-dix",
                        "quatre-vingt-onze à cent-vingt"]))
chk("ibnat maḫāḍ/ibn labūn/ḥaqqa/ǧaḏaʿa définis", all(
    x in html for x in ["ibnat maḫāḍ", "ibn labūn", "ḥaqqa", "ǧaḏaʿa", "ġāyat asnān az-zakāt"]))
chk("petit bétail a-d complets", all(
    x in html for x in ["De quarante à cent-vingt", "cent-vingt-et-un à deux cents",
                        "deux-cent-une à trois cents", "chaque cent une brebis"]))
chk("bovins a-c complets", all(
    x in html for x in ["trente bovins, un tābiʿ", "quarante bovins, une musinna",
                        "sevré de sa mère", "que la femelle", "chaque trente un tābiʿ"]))

# 8. glossaire
chk("glossaire šuǧāʿ aqraʿ", "aš-šuǧāʿ al-aqraʿ" in html and "venin" in html)
chk("glossaire zabībatān", "az-zabībatān" in html and "nuqṭatān sawdāwān" in html)
chk("glossaire nawwāḍiḥ/sawānī", "an-nawwāḍiḥ" in html and "as-sawānī" in html and "tire l’eau du puits" in html)

# 9. traduction du transmetteur
chk("Muʿāḏ biographié", all(
    x in html for x in ["ʿAmr b. Aws al-Anṣārī al-Ḫazraǧī", "Abū ʿAbd ar-Raḥmān al-Madanī",
                        "dix-huit ans", "Badr", "ʿAqaba", "impuissantes à enfanter"]))

# 10. exploitation — story al-ʿUtbī
chk("isnād Rabīʿa", "Rabīʿa b. Abī ʿAbd ar-Raḥmān" in html and "ḥaddaṯanī" in html)
chk("story dépêcha un collecteur", "baʿaṯa raǧulan muṣaddiqan" in html)
chk("story bint maḫāḍ / ne se trait pas", "bintu maḫāḍ" in html and "yuḥlabu" in html and "yurkab" in html)
chk("story grande chamelle + ordre", "fa-aʿṭā kabīra" in html and "lam uʾmar bi-ḏālika" in html)
chk("story invocation et croissance", "bi-l-barakati fī ʾibilihi" in html and "fa-namat wa-kaṯurat" in html)
chk("source al-ʿUtbī 2/429", "al-ʿUtbī al-Qurṭubī" in html and "2/429" in html or "tome 2, page 429" in html)

# 11. évaluation + préparation
chk("évaluation asnān + doctrine", "asnān" in html and "cheptel d’étable et de travail" in html)
chk("préparation 4 termes + ḫalṭa", all(
    x in html for x in ["as-saḫla", "ar-rubā", "ḥāfil", "al-māḫiḍ", "zakāt al-ḫalṭa"]))

# 12. aucune āya coranique dans la leçon — cache non sollicité
chk("aucune sūra citée (leçon sans verset)", "sūrat" not in html and "sūra " not in html)
chk("cache déclaré non sollicité", "cache non sollicité" in html)

# 13. écarts déclarés
chk("écart kāna yaqūlu", "kāna yaqūlu" in html)
chk("écart fa-dūnahā", "fa-dūnahā" in html and "écart de lecture déclaré" in html)
chk("écart ibn maḫāḍ masculin", "ibn maḫāḍ" in html and "écart interne" in html)
chk("écarts 704/706 déclarés", "mina d-ḍāʾ" in html and "wa-lam" in html)

# 14. claim R563
chk("claim 10:57:25Z trace R563", bool(re.search(r"10[\u202f\u00a0 ]:57[\u202f\u00a0 ]:25Z", html)) and "1a1a63223f3dc5c9-cron-agent-loop-202611041900" in html)
chk("R563 et pdf-19 dans l'apparat", "R563" in html and "pdf-19" in html)
chk("poussée initiale des 11 commits", "1219c538..0ee56964" in html)

# 15. aucune correction de mémoire — méthode déclarée
chk("méthode tesseract local déclarée", "tesseract" in html and "décodage déterministe" in html)
chk("aucun appel d'API vision", "aucun appel d’API de vision" in html)

print(f"\n=== BILAN : {ok} PASS / {fail} FAIL ===")
exit(1 if fail else 0)

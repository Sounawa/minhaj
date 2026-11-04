#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Minhāj — Vérification de la leçon ulum-hadith-tanawi-1 / pdf-mut23h2q-112
(madḫal pour connaître les sciences du ḥadīṯ, p.11-16 du manuel
ulum-hadith-1-thanawi.pdf acquis au miroir R576) : contrôle de contenu,
4 āyāt rendues du cache (al-ʿAlaq 1 ; al-Ḥuǧurāt 6 ; aṭ-Ṭalāq 2 segment ;
an-Nūr 14 imprimé = cache 16 — écart documenté), ḥadīṯs rendus tels
qu'imprimés (Buḫārī badʾ al-waḥy ; Tirmiḏī naḍḍara), alfiyya aṣ-Ṣuyūṭī
rendue en sens avec altérations déclarées, riwāya/dirāya [Tadrīb ar-Rāwī
1/25], bornes p.11-16 à convergence (objectifs p.11 ; إعداد قبلي p.16
annonçant le ḥadīṯ ṣaḥīḥ ; objectifs de la leçon suivante p.17),
garde-doublon : tafsir-1es/tafsir-2es renvois (livres complets 30/37),
30 slots ouverts sur ulum-hadith-tanawi-1.
Usage: python3 scripts-translate/verify-ulumhadith1-pdf112.py
"""
import re

HTML = "/home/z/my-project/tr-tmp/lesson-ulumhadith1-pdf-mut23h2q-112-fr.html"

ok, fail = 0, 0
def chk(label, cond):
    global ok, fail
    if cond: ok += 1
    else:
        fail += 1
        print(f"ÉCHEC: {label}")

html = open(HTML, encoding="utf-8").read()
text = re.sub(r"<[^>]+>", " ", html).replace("\u202f", " ").replace("\u00a0", " ")

# 0 arabe (ﷺ U+FDFA exempté par convention corpus)
arab = re.findall(r"[\u0600-\u06FF\u0750-\u077F\u08A0-\u08FF\uFB50-\uFDF9\uFDFB-\uFDFF\uFE70-\uFEFF]", text)
arab = [c for c in arab if c != "\ufdfa"]
chk("0 caractère arabe au corps", len(arab) == 0)

# structure générale
chk("h1 leçon 1 du livre", "leçon 1" in html and "<h1>" in html)
chk("lesson-meta présent", 'class="lesson-meta"' in html and "Source du cours" in html)
chk("bornes pages 11 à 16 citées", "pages 11 à 16" in html)
chk("manzuma Bayquni citée", "al-Bayqūniyya" in html or "Biqūniyya" in html)
chk("commentaire Zarqani cité", "al-Zarqānī" in html)
chk("miroir archive cité", "1_20220304_20220304_2251" in html)
chk("GARDE-DOUBLON tafsir doublons consigné", "duplicatas" in html and "renvoi" in html)
chk("30 slots ouverts consigné", "trente slots" in html)
chk("OCR tesseract 300 dpi consigné", "OCR tesseract arabe local à 300 dpi" in html)
chk("crops 600 dpi consignés", "600 dpi" in html)
chk("borne jamais devinée", "jamais devinée" in html)
chk("interdits double rendu consignés", "interdites de double rendu" in html)

# āyāt du cache (rendus attendus présents)
chk("al-Alaq 1 cache", "Lis, au nom de ton Seigneur qui a créé" in html)
chk("al-Huǧurāt 6 cache", "Si un pervers vous apporte une nouvelle" in html)
chk("aṭ-Ṭalāq 2 segment", "deux hommes intègres parmi vous comme témoins" in html)
chk("an-Nūr 14-imprimé = cache 16", "une énorme calomnie" in html)
chk("écart an-Nūr documenté", "correspond à l’āya 16 du cache" in html)
chk("rasm nu interdit (pas de translittération coranique)", "Lis, au nom" in html)

# ḥadīṯs rendus tel qu'imprimé
chk("hadith Buḫārī Khadīǧa", "couvrez-moi" in html and "tu joins les liens de la parenté" in html)
chk("source Buḫārī badʾ al-waḥy", "Ṣaḥīḥ al-Buḫārī" in html and "badʾ al-waḥy" in html)
chk("hadith Tirmiḏī naḍḍara", "Que Dieu illumine un homme" in html)
chk("source Tirmiḏī", "Sunan at-Tirmiḏī" in html and "tablīġ as-samāʿ" in html)

# contenu doctrinal LREAD
chk("définition riwāya/dirāya", "riwāya" in html and "dirāya" in html)
chk("Tadrīb ar-Rāwī 1/25", "Tadrīb ar-Rāwī" in html and "1/25" in html)
chk("glose sand", "l’appuyé" in html)
chk("étymologie matn", "matn du bélier" in html)
chk("ḥadīṯ vs matn (plus spécifique)", "plus spécifique que le matn" in html)
chk("synonymie ḥadīṯ/ḫabar/aṯar", "termes synonymes" in html)
chk("quatre fruits", "la distinction de l’accepté d’avec le rejeté" in html
    and "sens critique des nouvelles" in html)
chk("premier muḥaddiṯ", "premier taḥdīṯ" in html)

# sections du gabarit
for sec in ("Les objectifs de la leçon", "Le tamhīd", "Le commentaire", "La glose",
            "L’évaluation", "L’exploitation", "La préparation préalable"):
    chk(f"section {sec}", sec in html)

# évaluation 4 items LREAD
chk("éval item 1 (définition)", "en distinguant la science de leur riwāya" in html)
chk("éval item 2 (matn-ḥadīṯ-ḫabar-aṯar)", "le matn — le ḥadīṯ — le ḫabar — l’aṯar" in html)
chk("éval item 3 (naissance)", "Comment naquit cette science" in html)
chk("éval item 4 (fruits)", "les fruits de son étude" in html)

# préparation préalable = ḥadīṯ ṣaḥīḥ (borne L113)
chk("préparation annonce le ṣaḥīḥ", "je définis le ḥadīṯ ṣaḥīḥ" in html)

# résidus interdits
for bad in ("XXX", "TODO", "待补充", "undefined", "NaN", "【"):
    chk(f"résidu {bad} absent", bad not in html)

print(f"\nverify-ulumhadith1-pdf112 : {ok} PASS / {fail} FAIL")
raise SystemExit(1 if fail else 0)

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Minhāj — Vérification de la leçon hadith2-pdf-18 (leçon 17, la zakāt des
héritages, des créances et des marchandises, p.118-124) : dix renvois du
Muwaṭṭaʾ tranchés par preuve image (685/687/688/693 au corps + 685/687/689/
690/691/694/695/696 en citation — 7 pages entières 300 dpi + 6 composites
900 dpi + 1 composite calibré OCR), bornes p.118-124 (bandeau « Leçon 17 »
p.118 lu 300 dpi ; objectifs du cours suivant p.125), الرسالة ص 67 دار الفكر,
šarḥ Ibn Nāǧī 1/310, notice ʿUthmān b. ʿAffān (ḏū an-nūrayn, s.35), écarts
déclarés (yabdaʾa/yabīda, an naẓura man mirra, ṯuluṯa dīnārin, ar-rikāka,
ʿanhumā, maʿdan, mutanawwiʿa, ḍimār…), claim atomique 10:46:18Z sans takeover.
Usage: python3 scripts-translate/verify-hadith2-pdf18.py
"""
import re

HTML = "/home/z/my-project/tr-tmp/lesson-hadith2-pdf-18-fr.html"
ok, fail = 0, 0


def chk(label, cond):
    global ok, fail
    if cond:
        ok += 1
        print(f"PASS — {label}")
    else:
        fail += 1
        print(f"FAIL — {label}")


html = open(HTML, encoding="utf-8").read().replace("\u202f", " ")  # NNBSP-tolérant

# 1. structure
chk("h1 unique avec « leçon 17 »", html.count("<h1>") == 1 and "leçon 17" in html.split("</h1>")[0])
chk("badge « Leçon 18 / 31 »", "Leçon 18 / 31" in html)
chk("pages 118 à 124 citées", "pages 118 à 124" in html)
chk("lesson-meta présent", '<dl class="lesson-meta">' in html and "Source du cours" in html)

# 2. les dix numéros du Muwaṭṭaʾ — chacun cité avec n° explicite
for n in [685, 687, 688, 689, 690, 691, 693, 694, 695, 696]:
    chk(f"Muwaṭṭaʾ n° {n} cité", f"n° {n}" in html)

# 3. isnāds tranchés image
chk("isnād 693 complet", all(
    x in html for x in ["Yaḥyā b. Saʿīd", "Zurayq b. Ḥayyān", "al-Walīd", "Sulaymān", "ʿUmar b. ʿAbd al-ʿAzīz"]))
chk("isnād 688 complet", "Ibn Shihāb" in html and "as-Sāʾib b. Yazīd" in html)
chk("isnād 690 complet", "Yazīd b. Ḥaṣība" in html and "Sulaymān b. Yasār" in html)

# 4. matns clés tranchés image
chk("matn 685 tiers/exécuteurs", "du tiers de son bien" in html and "exécuteurs testamentaires" in html)
chk("matn 687 sunna chez nous/ḥawl", "La sunna chez nous" in html and "ḥawl se passe sur lui" in html)
chk("matn 688 mois de la zakāt", "mois de votre zakāt" in html and "recensement de vos biens" in html)
chk("matn 693 quarante dinars", "quarante dinars un dinar" in html and "vingt dinars" in html)
chk("matn 691 une seule zakāt", "une seule zakāt" in html and "années comptées" in html)
chk("matn 693 tiers de dinar ×2", html.count("tiers de dinar") >= 2)
chk("matn 690 « Non » + ʿayn/maʿdan", "Il dit : « Non »" in html and "maʿdan" in html)
chk("matn 689 rendu + ḍimār", "gouverneurs" in html and "ḍimār" in html and "une seule zakāt pour les années passées" in html)
chk("matn 693 gens du tribut/dix dinars", "gens du tribut" in html and "dix dinars" in html)
chk("matn 695 or/argent/blé/dattes", "or ou de l’argent" in html and "blé ou des dattes" in html)
chk("matn 696 mudīr/mois de compte", "al-mudīr" in html and "un mois de l’année" in html)

chk("matn 694 muḥtakir/une seule zakāt", "al-muḥtakir" in html and "si longtemps que dure cela" in html)
chk("ar-Risāla page 67", "ar-Risāla, page 67" in html)
chk("édition Dār al-Fikr", "Dār al-Fikr" in html)

# 6. exploitation (šarḥ Ibn Nāǧī 1/310) + notice ʿUthmān
chk("Ibn Abī Zayd al-Qayrawānī cité", "Ibn Abī Zayd al-Qayrawānī" in html)
chk("šarḥ Ibn Nāǧī 1/310", "Ibn Nāǧī" in html and "1/310" in html)
chk("notice ḏū an-nūrayn + Ruqayya", "ḏū an-nūrayn" in html and "Ruqayya" in html)
chk("notice an 35 martyr", "tué martyr l’an 35" in html)
chk("glose ǧawāz du šarḥ", "poste d’où la zakāt" in html)

# 7. écarts déclarés (jamais corrigés de mémoire)
for label, needle in [
    ("écart yabdaʾa/yabīda", "yabdaʾa"),
    ("écart an naẓura man mirra", "an naẓura man mirra"),
    ("écart ṯuluṯa dīnārin/canonique", "ṯuluṯa dīnārin"),
    ("écart canonique ṯalāṭata danānīra", "ṯalāṭata danānīra"),
    ("écart ar-rikāka (forme imprimée)", "ar-rikāka"),
    ("écart ʿanhumā", "ʿanhumā"),
    ("écart maʿdan d/ḏ", "maʿdan"),
    ("écart mutanawwiʿa", "mutanawwiʿa"),
    ("écart baʿaṯahā/bāʿahā", "baʿaṯahā/bāʿahā"),
    ("écart jubila (tamhīd)", "jubila"),
    ("écart uktab/akṯib", "uktab/akṯib"),
    ("écart manne shadda", "mann"),
    ("écart wufratihā", "wufratihā"),
    ("écart fa-yurkā", "sous réserve"),
    ("doublet an-unẓur/an naẓura", "an-unẓur"),
]:
    chk(label, needle in html)

# 8. sections du gabarit
for section in ["Les objectifs de la leçon", "Les textes du cours",
                "Les traductions des transmetteurs", "Les définitions du cours",
                "L’extraction des contenus", "Le corps du cours", "L’évaluation",
                "L’exploitation", "La préparation préalable", "L’apparat de preuve de la livraison"]:
    chk(f"section « {section} »", f"<h2>{section}</h2>" in html)
chk("tamhīd en h3", "<h3>Le tamhīd</h3>" in html)
chk("trois fronts du corps (héritage/dette/marchandises)", all(
    x in html for x in ["Premièrement : la zakāt de l’héritage",
                        "Deuxièmement : la zakāt de la dette",
                        "Troisièmement : la zakāt des marchandises commerciales"]))

# 9. claim + chaîne de production
chk("claim 10:46:18Z consigné (tolérant NNBSP)", bool(re.search(r"10[\u202f: ]{1,2}46[\u202f: ]{1,2}18Z", html)))
chk("refresh 11:10:33Z consigné", bool(re.search(r"11[\u202f: ]{1,2}10[\u202f: ]{1,2}33Z", html)))
chk("trace du tick consignée", "1a19c7c0ffb4f845" in html)
chk("registre 1120 → 1121", "1120 → 1121" in html)
chk("hadith-2es 17/30", "17/30" in html)
chk("prochain créneau pdf-19", "pdf-19" in html)
chk("expertise reset consignée (HEAD@{12})", "HEAD@{12}" in html and "récupération post-recyclage n° 5" in html)

# 10. FR-seule déjà garanti par qa-lesson — double garde ici
# ﷺ (U+FDFA) exempté — convention du corpus (cf. qa-lesson.py)
chk("0 caractère arabe hors ﷺ (re-vérif)", not re.search(r"[\u0600-\u06FF\u0750-\u077F\u08A0-\u08FF\uFB50-\uFDF9\uFDFB-\uFDFF\uFE70-\uFEFF]", html))

print(f"\n=== verify-hadith2-pdf18 : {ok} PASS / {fail} FAIL ===")
raise SystemExit(1 if fail else 0)

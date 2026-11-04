#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Minhāj — Vérification de la leçon hadith2-pdf-21 (leçon 20, la zakāt des fruits
et des grains, p.139-145) : seize renvois tranchés par preuve image (728×2,
745, 747, 727, 733, 734×2, 735×2, 746, 736, 739, 737, 729, 743 + šarḥ az-Zarqānī
2/194 — 7 pages entières 300 dpi + 9 composites 600 dpi), bornes p.139-145
(bandeau « Leçon 20 » p.139 lu 300 dpi ; pas de bandeau en tête de p.146 ;
triple convergeant avec la carte l20 = 139-145 et la livraison pdf-22),
āya al-Anʿām imprimé 142 = cache 141 (tranchée par le texte, rendu du cache),
notices Busr 100/101, Sulaymān 104, ʿAṭāʾ 103/94, dix-sept écarts déclarés,
claim atomique 11:20:12Z sans takeover + refresh 12:16:23Z.
Usage: python3 scripts-translate/verify-hadith2-pdf21.py
"""
import re

HTML = "/home/z/my-project/tr-tmp/lesson-hadith2-pdf-21-fr.html"
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
chk("h1 unique avec « leçon 20 »", html.count("<h1>") == 1 and "leçon 20" in html.split("</h1>")[0])
chk("badge « Leçon 21 / 31 »", "Leçon 21 / 31" in html)
chk("pages 139 à 145 citées", "pages 139 à 145" in html)
chk("lesson-meta présent", '<dl class="lesson-meta">' in html and "Source du cours" in html)

# 2. les numéros tranchés — chacun cité avec n° explicite
for n in [728, 745, 747, 727, 733, 734, 735, 746, 736, 739, 737, 729, 743]:
    chk(f"Muwaṭṭaʾ n° {n} cité", f"n° {n}" in html)
chk("šarḥ az-Zarqānī 2/194", "az-Zarqānī" in html and "2/194" in html)

# 3. occurrences multiples déclarées
chk("728 en deux occurrences", html.count("n° 728") >= 2)
chk("734 en deux occurrences", html.count("n° 734") >= 2)
chk("735 en deux occurrences", html.count("n° 735") >= 2)

# 4. isnāds tranchés image
chk("isnād 727 complet", "Sulaymān b. Yasār" in html and "Busr b. Saʿīd" in html)
chk("isnād 727 séquence dégradée déclarée", "an-nuqqati ʿaddatan" in html)
chk("isnād 747 ʿUmar", "ʿUmar b. al-Khaṭṭāb" in html and "an-niṭʿ" in html)

# 5. matns clés tranchés image
chk("matn 745 cinq awsuq/une seule espèce", "cinq awsuq" in html and "une seule espèce" in html)
chk("matn 745 samrāʾ/bayḍāʾ/sult", "as-samrāʾ" in html and "al-bayḍāʾ" in html and "sult" in html)
chk("matn 747 qoṭṭāniyya/ʿušr/demi-ʿušr", "qoṭṭāniyya" in html and "demi-ʿušr" in html)
chk("matn 727 baʿl/naḍḥ", "baʿl" in html and "naḍḥ" in html)
chk("matn 733 ʿušr s'y applique", "s’y applique" in html or "s'y applique" in html)
chk("matn 734 olive après pressurage", "pressur" in html and "cinq awsuq" in html)
chk("matn 735 au rang du palmier", "au rang du palmier" in html)
chk("matn 746 zaybīb noirs/rouges", "zaybīb" in html and "ses noirs et ses rouges" in html)
chk("matn 736 ciel et sources tranché", "wa-l-ʿuyūn" in html and "qayyūn" in html)
chk("matn 739 vend/mûri/akmām", "akmām" in html)
chk("matn 737 dix grains/blé/orge/dhurra", "dhurra" in html and "ǧalbān" in html and "lūbiyāʾ" in html)
chk("matn 729 khars sur les propriétaires", "on les estime à leurs propriétaires" in html)
chk("matn 743 pas de Šadaka sous cinq awsuq", "Pas de Šadaka sur ce qui est au-dessous" in html)
chk("ḥaḏāḏ", "al-ǧaḏāḏ" in html)
chk("anniḥāya Śadaka du milieu du bien", "milieu du bien" in html)

# 6. āya du cache (décalage tranché par le texte)
chk("āya imprimée 142 = cache 141", "142" in html and "141" in html)
chk("rendu cache 6:141 intégral", "treillagés et non treillagés" in html and "le jour de la récolte" in html)
chk("clôture lue à l'image consignée", "yauma ḥaṣādih" in html)
chk("āya annoncée sūrat al-Anʿām", "al-Anʿām" in html)

# 7. glossaire + notices de transmetteurs
chk("définition al-baʿl", "al-baʿl (la culture sèche)" in html)
chk("définition an-naḍḥ", "an-naḍḥ (l’égouttage)" in html or "an-naḍḥ (l'égouttage)" in html)
chk("définition yukhriṣu/ḥaǧr", "yukhriṣu" in html and "ḥaǧr" in html)
chk("notice Busr 100/101", "l’an 100 ou 101" in html)
chk("notice Sulaymān 104 + sept juristes", "l’an 104" in html and "sept juristes" in html)
chk("notice ʿAṭāʾ 103/94", "l’an 103" in html and "l’an 94" in html)

# 8. écarts déclarés (jamais corrigés)
for label, needle in [
    ("écart verbe d’ouverture tamhīd", "t-r-t-t-b/t-r-b-b"),
    ("écart as-samrāʾ porté tel quel", "as-samrāʾ ["),
    ("écart an-niṭʿ", "an-niṭʿ"),
    ("écart al-ʿaṯr", "ʿaṯr"),
    ("écart interrogation 733", "az-Zuhrī"),
    ("écart yu-taḫarruhā", "yu-taḫarruhā"),
    ("écart ad-duḫu", "ad-duḫu"),
    ("écart al-ǧalǧalān", "al-ǧalǧalān"),
    ("écart al-qaṛẓ/al-qaraʿ", "al-qaṛẓ"),
    ("écart min an-nāh", "min an-nāh"),
    ("écart f-y-b-s/b-y-w-š", "b-y-b-s/b-y-w-š"),
    ("écart al-fursuk", "fursuk"),
    ("écart exploitation fī ġayri riwāya", "fī ġayri riwāya"),
]:
    chk(label, needle in html)
chk("nombre d’écarts consigné", "dix-sept écarts" in html)

# 9. sections du gabarit
for section in ["Les objectifs de la leçon", "Les textes du cours",
                "Les traductions des transmetteurs", "Les définitions du cours",
                "L’extraction des contenus", "Le corps du cours", "L’évaluation",
                "L’exploitation", "La préparation préalable", "L’apparat de preuve de la livraison"]:
    chk(f"section « {section} »", f"<h2>{section}</h2>" in html)
chk("tamhīd en h3", "<h3>Le tamhīd</h3>" in html)
chk("deux fronts du corps (fruits/union)", all(
    x in html for x in ["Premièrement : les règles de la zakāt des fruits et des grains",
                        "Deuxièmement : la réunion des fruits et des grains les uns aux autres"]))
chk("six rubriques du premier front", all(
    x in html for x in ["1 — Le montant obligatoire", "2 — D’où prélève-t-on",
                        "3 — Quand la zakāt devient-elle due", "4 — Les grains soumis",
                        "5 — Le khars", "6 — La zakāt de l’olive"]))

# 10. claim + chaîne de production
chk("claim 11:20:12Z consigné", bool(re.search(r"11[\u202f: ]{1,2}20[\u202f: ]{1,2}12Z", html)))
chk("refresh 12:16:23Z consigné", bool(re.search(r"12[\u202f: ]{1,2}16[\u202f: ]{1,2}23Z", html)))
chk("trace du tick consignée", "1a19c7c0ffb4f845" in html)
chk("registre 1122 → 1123", "1122 → 1123" in html)
chk("prochain créneau pdf-23", "pdf-23" in html)
chk("parallèle pdf-22 livré consigné", "d7fb0650" in html)

# 11. FR-seule déjà garanti par qa-lesson — double garde ici
# ﷺ (U+FDFA) exempté — convention du corpus (cf. qa-lesson.py)
chk("0 caractère arabe hors ﷺ (re-vérif)", not re.search(r"[\u0600-\u06FF\u0750-\u077F\u08A0-\u08FF\uFB50-\uFDF9\uFDFB-\uFDFF\uFE70-\uFEFF]", html))

print(f"\n=== verify-hadith2-pdf21 : {ok} PASS / {fail} FAIL ===")
raise SystemExit(1 if fail else 0)

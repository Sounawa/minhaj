#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Minhāj — Vérification de la leçon hadith2-pdf-24 (leçon 23, les règles du
jeûne (1), p.158-164) : onze crochets numérotés du Muwaṭṭaʾ tranchés à la
couche brute + OCR arabe local (784 ; 793 ; 796 ; 791 ; 785 ; 786 ; 787 ;
789 ; 794 ; 799 ; 790 — sept pages 300 dpi + boîtes TSV + micro-crops
600/1 200/2 400 dpi, aucun appel d'API vision), deux sources hors Muwaṭṭaʾ
[at-Targhīb wa-t-Tarhīb de l'imām al-Mundhirī ; Sunan ad-Dāraquṭnī], deux
āyas rendues du cache par le texte (az-Zumar imprimé 11 = cache 39:10
fragment final ; Maryam imprimé 25 = cache 19:26 fragment), un vers
d'an-Nābiġa tel qu'imprimé, trois finalités et six maqāṣid, intention
mubīta, quatre moments de la vision du croissant, ajournement de la
rupture, jeûne du junub avec consensus, écarts déclarés (kaffāra, ʾaštā,
taʿūdī, luǧamā, nafl), claim atomique 13:07:44Z.
Usage: python3 scripts-translate/verify-hadith2-pdf24.py
"""
import re

HTML = "/home/z/my-project/tr-tmp/lesson-hadith2-pdf-24-fr.html"
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
chk("h1 unique avec « leçon 23 »", html.count("<h1>") == 1 and "leçon 23" in html.split("</h1>")[0])
chk("badge « Leçon 24 / 31 »", "Leçon 24 / 31" in html)
chk("pages 158 à 164 citées", "pages 158 à 164" in html)
chk("slot pdf-24 cité", "pdf-24" in html)
chk("titre registre « Les règles du jeûne (1) »", "Les règles du jeûne (1)" in html)
chk("lesson-meta présent", "<dl class=\"lesson-meta\">" in html)
for sec in ("Les objectifs de la leçon", "Le tamhīd", "Les textes du cours",
            "Les traductions des transmetteurs", "Les définitions du cours",
            "L’extraction des contenus", "Le corps du cours", "L’évaluation",
            "L’exploitation", "La préparation préalable",
            "L’apparat de preuve de la livraison"):
    chk(f"section « {sec} »", f"{sec}</h2>" in html or f">{sec}<" in html)

# 2. les onze renvois Muwaṭṭaʾ tranchés chiffre par chiffre
for n, occ in ((784, 1), (793, 1), (796, 1), (791, 1), (785, 1), (786, 1),
               (787, 1), (789, 1), (794, 1), (799, 1), (790, 1)):
    hits = len(re.findall(rf"n°[\u202f\u00a0 ]?{n}\b", html))
    chk(f"Muwaṭṭaʾ n° {n} (au moins {occ} occurrence(s))", hits >= occ)
chk("zone du livre déclarée 784-799 cohérente", "784-799" in html)
chk("786 contre lecture OCR 756 tranchée à l'image", "756" in html and "786" in html)

# 3. sources hors Muwaṭṭaʾ
chk("at-Targhīb wa-t-Tarhīb de l'imām al-Mundhirī", "at-Targhīb wa-t-Tarhīb" in html
    and "al-Mundhirī" in html)
chk("Sunan ad-Dāraquṭnī", "ad-Dāraquṭnī" in html)

# 4. āyas rendues du cache
chk("āya az-Zumar cache 39:10 (décalage warš déclaré)",
    "az-Zumar" in html and "39\u202f:10" in html and "décalage warš" in html)
chk("fragment 39:10 « la récompense des patients »",
    "la récompense des patients" in html and "sans compte" in html)
chk("āya Maryam cache 19:26 (décalage par le texte)",
    "Maryam" in html and "19\u202f:26" in html)
chk("fragment 19:26 « vouée au Miséricordieux en un jeûne »",
    "vouée au Miséricordieux en un jeûne" in html)

# 5. vers d'an-Nābiġa
chk("vers an-Nābiġa tel qu'imprimé", "Nābiġa" in html and "taʿlaku l-luǧamā" in html)
chk("glose « toute retenue contre le mouvement »", "mamsaka ʿan al-ḥaraka" in html)

# 6. matns clés
chk("matn 784 « fāqidirū lahu »", "fāqidirū lahu" in html)
chk("matn 793/794 « s'empressent de rompre »", "s’empressent de rompre" in html)
chk("matn 796 « bimā ʾanqā »", "bimā ʾanqā" in html)
chk("matn 791 « ʾaǧmaʿa aṣ-ṣiyāma qabla l-faǧr »", "ʾaǧmaʿa aṣ-ṣiyāma qabla l-faǧr" in html)
chk("matn 785 « le mois fait vingt-neuf jours »", "vingt-neuf" in html)
chk("matn 787 vision ʿUṯmān baʿšiyya", "ʿUṯmān b. ʿAffān" in html and "baʿšiyya" in html)
chk("matn 789 « mamūn » et tuhma", "mamūn" in html and "tuhma" in html)
chk("matn 799 ʿĀʾiša et Umm Salama « min ǧimāʿi ġayri ʾiḫtilām »",
    "Umm Salama" in html and "ǧimāʿi ġayri ʾiḫtilām" in html)
chk("matn 790 jeûner le jour de la fête", "yawm al-fiṭr" in html)

# 7. gloses du Šarḥ
chk("glose ġumma", "ġumma" in html and "nuage" in html)
chk("glose fāqidirū lahu = trente jours", "qaddirū lahu" in html and "trente jours" in html)
chk("glose hilāl/qamar", "qamar" in html and "vingt-septième" in html)

# 8. corps : finalités et intention
chk("six finalités a-f", all(x in html for x in ("yaksiru n-nafs", "ittiṣāl bi-llāhi",
    "ramz li-l-ʾirādati", "murān", "ǧihāz al-haḍm", "bi-ʾiqdārihi")))
chk("intention mubīta qabla l-faǧr", "nīya mubīta" in html or "nouée la nuit" in html)
chk("nafl qabla z-zawāl + récit ʿĀʾiša Dāraquṭnī", "qabla z-zawāl" in html
    and "min ġadāʾ" in html)

# 9. écarts déclarés
for e in ("kaff/kar", "ḥattā ʾaštā", "taʿūdī", "l-luǧamā", "li-man šāʾa"):
    chk(f"écart déclaré « {e} »", e in html)
chk("clause « jamais corrigé de mémoire »", "jamais corrigé de mémoire" in html)

# 10. claim + trace
chk("claim 13:07:44Z", bool(re.search(r"13[\u202f\u00a0 ]:07[\u202f\u00a0 ]:44Z", html)))
chk("trace 1a19c7c0ffb4f845 présente", "1a19c7c0ffb4f845-cron-agent-loop-202611042105" in html)
chk("R569 et pdf-24 dans l'apparat", "R569" in html and "pdf-24" in html)

# 11. méthode déclarée
chk("méthode locale sans API vision", "tesseract" in html and "aucune lecture devinée" in html)
chk("extraction 7 366 car déclarée", "7 366 car" in html)

# 12. 0 arabe re-vérif (hors U+FDFA exempté)
ar = re.findall(r"[\u0600-\u06FF\u0750-\u077F\u08A0-\u08FF\uFB50-\uFDF9\uFDFB-\uFDFF\uFE70-\uFEFF]", html)
chk("0 caractère arabe résiduel", len(ar) == 0)

print(f"\n=== BILAN : {ok} PASS / {fail} FAIL ===")
exit(1 if fail else 0)

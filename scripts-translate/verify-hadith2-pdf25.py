#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Minhāj — Vérification de la leçon hadith2-pdf-25 (leçon 24, les règles du
jeûne (2) : le baiser du jeûneur et le jeûne du voyageur, p.165-170) : onze
crochets du Muwaṭṭaʾ tranchés chiffre par chiffre (805 contre OCR 305 ;
800 ; 812 contre VLM 814 ; 815 ; 801 contre couche 108 ; 809 contre couche
908 ; 811 ; 816 ×2 — deux sentences du même rapport ; 817 couche 7 ; 829
contre couche 928), l'année 94 de ʿUrwa, une source hors Muwaṭṭaʾ [Ṣaḥīḥ
Muslim], deux fragments du cache canonique 2:184 (marqueurs imprimés warš
183 et 184, tranchés par le texte, décalage R511), tarjama de ʿUrwa, gloses
waǧad/istadāma, statut du baiser, spécificité prophétique réfutée, jeûne du
voyageur (ǧumhūr, Ibn ʿAbbās/al-Kadayd, Anas), Muslim/Abū Saʿīd, trois cas
a-b-c (retour, départ, épouse purifiée), exploitation 829 + lā ṣāma man
ṣāma l-ʾabad, écarts déclarés (kiltah, lasnā, waǧaba, fī-mā ʿuniya…),
claim takeover 16:35:31Z (WIP repris), trace ...202611042241.
Usage: python3 scripts-translate/verify-hadith2-pdf25.py
"""
import re

HTML = "/home/z/my-project/tr-tmp/lesson-hadith2-pdf-25-fr.html"
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
chk("h1 unique avec « leçon 24 »", html.count("<h1>") == 1 and "leçon 24" in html.split("</h1>")[0])
chk("badge « Leçon 25 / 31 »", "Leçon 25 / 31" in html)
chk("pages 165 à 170 citées", "pages 165 à 170" in html)
chk("slot pdf-25 cité", "pdf-25" in html)
chk("titre registre « Les règles du jeûne (2) »", "Les règles du jeûne (2)" in html)
chk("lesson-meta présent", "<dl class=\"lesson-meta\">" in html)
for sec in ("Les objectifs de la leçon", "Le tamhīd", "Les textes du cours",
            "Les traductions des transmetteurs", "Les définitions du cours",
            "L’extraction des contenus", "Le corps du cours", "L’évaluation",
            "L’exploitation", "La préparation préalable",
            "L’apparat de preuve de la livraison"):
    chk(f"section « {sec} »", f"{sec}</h2>" in html or f">{sec}<" in html)

# 2. les onze renvois Muwaṭṭaʾ tranchés chiffre par chiffre
for n, occ in ((805, 1), (800, 1), (812, 1), (815, 1), (801, 1), (809, 1),
               (811, 1), (816, 2), (817, 1), (829, 1)):
    hits = len(re.findall(rf"n°[\u202f\u00a0 ]?{n}\b", html))
    chk(f"Muwaṭṭaʾ n° {n} (au moins {occ} occurrence(s))", hits >= occ)
chk("zone du livre déclarée 800-829 cohérente", "800-829" in html)
chk("805 contre lecture OCR 305", "305" in html and "805" in html)
chk("812 contre lecture VLM 814 tranchée à 1440 dpi", "814" in html and "1 440 dpi" in html)
chk("801 couche inversée 108", "108" in html)
chk("809 couche inversée 908", "908" in html)
chk("829 couche inversée 928", "928" in html)

# 3. source hors Muwaṭṭaʾ
chk("Ṣaḥīḥ Muslim (jeûne perpétuel)", "Ṣaḥīḥ Muslim" in html
    and "chapitre de l’interdiction du jeûne perpétuel" in html)
chk("Šarḥ az-Zarqānī cité", "Šarḥ az-Zarqānī" in html)

# 4. āyas rendues du cache par le texte
chk("āya al-Baqara imprimé 183 = cache 2:184 fragment final",
    "2\u202f:184" in html and "décalage warš" in html)
chk("fragment final « et il est mieux pour vous de jeûner »",
    "et il est mieux pour vous de jeûner" in html)
chk("āya al-Baqara imprimé 184 = cache 2:184 fragment médian",
    html.count("2\u202f:184") >= 2)
chk("fragment médian « nombre égal d’autres jours »",
    "nombre égal d’autres jours" in html)

# 5. année du décès de ʿUrwa
chk("ʿUrwa mort en l’an 94", "l’an 94" in html)

# 6. matns clés
chk("citation 805 « amlaku li-nafsihi »", "ʾamlaku li-nafsihi" in html)
chk("matn 800 « waǧdan šadīdan »", "waǧdan šadīdan" in html)
chk("matn 800 colère « li-ʿtiqādi r-raǧuli t-taḫṣīṣa bilā dalīl »",
    "li-ʿtiqādi r-raǧuli t-taḫṣīṣa bilā dalīl" in html)
chk("matn 812 « ʾin šiʾta fa-ṣum »", "ʾin šiʾta fa-ṣum" in html)
chk("matn 815 « daḫala wa-huwa ṣāʾim »", "daḫala wa-huwa ṣāʾim" in html)
chk("matn 801 « ṯumma taḍḥak »", "ṯumma taḍḍak".replace("ḍḍ", "ḍh") in html or "ṯumma taḍḥak" in html)
chk("matn 809 al-Kadayd", "al-Kadayd" in html)
chk("matn 811 « lā yaʿibu » (falam yaʿibi)", "falam yaʿibi" in html)
chk("matn 816 sentence a) « ʾahli l-ḥaḍari »", "ʾahli l-ḥaḍari" in html)
chk("matn 817 « ʾan yuṣībahā ʾin šāʾa »", "ʾan yuṣībahā ʾin šāʾa" in html)
chk("matn 829 « lā baʾsa bi-ṣiyāmi d-dahr »", "lā baʾsa bi-ṣiyāmi d-dahr" in html)
chk("matn 829 « ʾaḥabbu mā samiʿtu ʾilayhi »", "ʾaḥabbu mā samiʿtu ʾilayhi fī ḏālik" in html)
chk("Muslim « lā ṣāma man ṣāma l-ʾabad »", "lā ṣāma man ṣāma l-ʾabad" in html)
chk("Muslim « yarauna ʾanna man waǧǧada quwwatan »", "yarauna ʾanna man waǧǧada quwwatan" in html)
chk("Ḥamza « raǧulun ʾaṣūmu »", "raǧulun ʾaṣūmu" in html)

# 7. gloses du Šarḥ
chk("glose waǧad = ḥazan", "waǧad" in html and "ḥazan" in html)
chk("glose istadāma l-ḥazana wa-l-ʾasaf", "istadāma l-ḥazana wa-l-ʾasaf" in html)

# 8. corps : statuts
chk("consensus baiser", "lā ḫilāfa ʾanna l-qublata lā tamnaʿu" in html)
chk("avis tranché al-muftā", "al-muftā bihī" in html)
chk("ǧumhūr voyage", "ǧumhūru l-ʿulamāʾ" in html)
chk("trois cas a-b-c déclarés", html.count("<em>b.</em>") == 1 and "<em>c.</em>" in html)
chk("waǧūban cas b)", "waǧūban" in html)
chk("ʿĀšūrāʾ en préparation", "ʿĀšūrāʾ" in html)
chk("ḥiǧāma en préparation", "ḥiǧāma" in html)

# 9. écarts déclarés
for e in ("kiltah", "lasnā miṯla", "waǧaba", "fī-mā ʿuniya", "sana miṯla"):
    chk(f"écart déclaré « {e} »", e in html)
chk("clause « jamais corrigé de mémoire »", html.count("jamais corrigé de mémoire") >= 2)

# 10. claim + trace + WIP
chk("claim takeover 16:35:31Z", bool(re.search(r"16[\u202f\u00a0 ]:35[\u202f\u00a0 ]:31Z", html)))
chk("claim initial 14:42:07Z du WIP repris", bool(re.search(r"14[\u202f\u00a0 ]:42[\u202f\u00a0 ]:07Z", html)))
chk("trace 1a1a172f41684dc9 présente", "1a1a172f41684dc9-cron-agent-loop-202611042241" in html)
chk("R570 et pdf-25 dans l’apparat", "R570" in html and "pdf-25" in html)
chk("enquête reset consignée (reflog, zéro perte)", "reflog" in html and "zéro livraison manquante" in html)

# 11. méthode déclarée
chk("méthode mixte : tesseract + VLM + SDK hors arbre", "tesseract" in html
    and "cinq passes" in html.lower() and "/home/z/vlm-sdk" in html)
chk("extraction 12 607 car déclarée", "12 607 car" in html)
chk("balayage node_modules R561 documenté", "R561" in html)

# 12. 0 arabe re-vérif (hors U+FDFA exempté)
ar = re.findall(r"[\u0600-\u06FF\u0750-\u077F\u08A0-\u08FF\uFB50-\uFDF9\uFDFB-\uFDFF\uFE70-\uFEFF]", html)
chk("0 caractère arabe résiduel", len(ar) == 0)

print(f"\n=== BILAN : {ok} PASS / {fail} FAIL ===")
exit(1 if fail else 0)

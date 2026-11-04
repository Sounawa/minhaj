#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Minhāj — Vérification de la leçon hadith2-pdf-27 (leçon 26, les règles du
jeûne (4) : jeûne interdit, wiṣāl, formes du jeûne obligatoire, jeûne du
malade, substitution, p.177-183) : sept crochets Muwaṭṭaʾ tranchés (828 ;
830/couche-038 ; 835/couche-538 ; 836/couche-638 ; 832/couche-238-OCR-8:2 ;
834/couche-438 ; 839/couche-938), deux sources [Ṣaḥīḥ Muslim], quatre
citations du cache par le texte (Nisāʾ imprimé 91 = cache 4:92 ;
Muǧādala 4 = cache 58:4 ; Māʾida 1 = cache 5:1 ; Baqara 183 = cache 2:184),
gloses wiṣāl/lastu ka-hayʾatikum, vers d'amour porté tel qu'imprimé,
écarts déclarés (tarjama illisible, phrase finale malade, tušġiluhā/tušʿalhā,
ʾaḥsanu/ʾaḥabbu…), claim 17:21:56Z + refresh 17:40:53Z, trace ...202611042241,
pdf-26 couvert par l'ouvrier parallèle documenté.
Usage: python3 scripts-translate/verify-hadith2-pdf27.py
"""
import re

HTML = "/home/z/my-project/tr-tmp/lesson-hadith2-pdf-27-fr.html"
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
chk("h1 unique avec « leçon 26 »", html.count("<h1>") == 1 and "leçon 26" in html.split("</h1>")[0])
chk("badge « Leçon 27 / 31 »", bool(re.search(r"Leçon 27[\u202f\u00a0 ]/[\u202f\u00a0 ]31", html)))
chk("pages 177 à 183 citées", "pages 177 à 183" in html)
chk("slot pdf-27 cité", "pdf-27" in html)
chk("titre registre « Jeûnes proscrits et prescrits »", "Jeûnes proscrits et prescrits" in html)
chk("lesson-meta présent", "<dl class=\"lesson-meta\">" in html)
for sec in ("Les objectifs de la leçon", "Le tamhīd", "Les textes du cours",
            "Les traductions des transmetteurs", "Les définitions du cours",
            "L’extraction des contenus", "Le corps du cours", "L’évaluation",
            "L’exploitation", "La préparation préalable",
            "L’apparat de preuve de la livraison"):
    chk(f"section « {sec} »", f"{sec}</h2>" in html or f">{sec}<" in html)

# 2. les sept renvois Muwaṭṭaʾ tranchés chiffre par chiffre
for n, occ in ((828, 1), (830, 1), (835, 1), (836, 1), (832, 1), (834, 1), (839, 1)):
    hits = len(re.findall(rf"n°[\u202f\u00a0 ]?{n}\b", html))
    chk(f"Muwaṭṭaʾ n° {n} (au moins {occ} occurrence(s))", hits >= occ)
chk("zone 828-839 déclarée cohérente", "828-839" in html)
chk("830 contre couche inversée 038", "038" in html)
chk("835 contre couche inversée 538", "538" in html)
chk("832 contre couche 238 et OCR 8:2", "238" in html and bool(re.search(r"8[\u202f\u00a0 ]:[\u202f\u00a0 ]?2", html)))
chk("839 contre couche inversée 938", "938" in html)

# 3. sources hors Muwaṭṭaʾ
chk("Ṣaḥīḥ Muslim (interdiction fête)", "Ṣaḥīḥ Muslim" in html
    and "interdiction de jeûner le jour de la Rupture" in html)
chk("Ṣaḥīḥ Muslim (rattrapage pour le mort)", "rattrapage du jeûne pour le mort" in html)

# 4. āyas rendues du cache par le texte
chk("Nisāʾ imprimé 91 = cache 4:92", "4\u202f:92" in html and "décalage warš" in html)
chk("fragment 4:92 « une compensation remise »", "une compensation remise" in html)
chk("Muǧādala 4 = cache 58:4", "58\u202f:4" in html)
chk("fragment 58:4 « avant qu’ils ne se touchent »", "avant qu’ils ne se touchent" in html)
chk("Māʾida 1 = cache 5:1", "5\u202f:1" in html)
chk("fragment 5:1 « acquittez-vous des engagements »", "acquittez-vous des engagements" in html)
chk("Baqara 183 = cache 2:184 fragment médian", "2\u202f:184" in html
    and "marqueur imprimé porte «\u202f183\u202f»" in html)
chk("fragment 2:184 « nombre égal d’autres jours »", "nombre égal d’autres jours" in html)
chk("marqueur 184 de la leçon précédente consigné", "portant le marqueur imprimé «\u202f184\u202f»" in html)

# 5. matns clés
chk("matn 828 « yawmi l-fiṭri wa-yawmi l-ʾaḍḥā »", "yawmi l-fiṭri wa-yawmi l-ʾaḍḥā" in html)
chk("matn 830 « innī lastu ka-hayʾatikum »", "innī lastu ka-hayʾatikum" in html)
chk("matn 830 « innī ʾuṭʿamu wa-ʾusqā »", "innī ʾuṭʿamu wa-ʾusqā" in html)
chk("matn 835 « samiʿtu Mālikan yaqūlu »", "samiʿtu Mālikan yaqūlu" in html)
chk("matn 835 « dīnu llāhi yusr »", "dīnu llāhi yusr" in html)
chk("matn 832 « wa-yabnī ʿalā mā qad maḍā »", "wa-yabnī ʿalā mā qad maḍā min ṣiyāmihi" in html)
chk("matn 834 « min ʿillati maraḍin ʾaw ḥayḍatin »", "min ʿillati maraḍin ʾaw ḥayḍatin" in html)
chk("matn 836 « li-yabdaʾa bi-n-naḏri »", "li-yabdaʾa bi-n-naḏri qabla ʾan yataṭawwaʿa" in html)
chk("matn 839 « lā yaṣūmu ʾaḥadun ʿan ʾaḥad »", "lā yaṣūmu ʾaḥadun ʿan ʾaḥad" in html)
chk("Muslim « fa-daynu llāhi ʾaḥaqqu bil-qaḍāʾ »", "fa-daynu llāhi ʾaḥaqqu bil-qaḍāʾ" in html)
chk("Muslim tašrīq « ʾayyāmu ʾaklin wa-šurb »", "ʾayyāmu t-tašrīqi ʾayyāmu ʾaklin wa-šurb" in html)
chk("intro vœu « amra llāhu bi-wafāʾi n-naḏri »", "amra llāhu bi-wafāʾi n-naḏri" in html)

# 6. gloses du Šarḥ
chk("glose wiṣāl", "al-wiṣāl" in html and "sans rupture ni repas de l’aube" in html)
chk("glose lastu ka-hayʾatikum", "lastu ka-hayʾatikum" in html and "mon état n’est pas comme le vôtre" in html)

# 7. corps : statuts et sections
chk("interdiction fête pour tous (nāḏir, qāḍin)", "mutawaʿʿiʿ" in html and "nāḏir" in html)
chk("wiṣāl karāha Mālik et majorité", "karāha" in html and "qu’on y soit capable ou non" in html)
chk("trois avis sur « je suis nourri »", "maǧāzun ʿan lāzimi ṭ-ṭaʿāmi" in html
    and "An-Nawawī" in html and "Ibn al-Qayyim" in html)
chk("vers d’amour porté tel qu’imprimé", "lahā ʾaḥādīṯu min ḏikrāka" in html)
chk("tatabbuʿ deux mois consécutifs", "šahrayni mutatābiʿayni" in html)
chk("vœu engage par la parole", "yalzamu bil-qawl" in html)
chk("malade rupture permise", "ǧāza lahu l-fiṭr" in html)
chk("substitution niyāba", "niyāba" in html)

# 8. écarts déclarés
for e in ("samiyya/sayf", "al-maradu l-mubīḥu li-l-fiṭr", "tušġiluhā/tušʿalhā",
          "ʾaḥsanu/ʾaḥabbu", "fa-wāfaqa/fa-waqaʿa", "muʿtamir"):
    chk(f"écart déclaré « {e} »", e in html)
chk("clause « jamais corrigé de mémoire »", html.count("jamais corrigé de mémoire") >= 3)

# 9. claim + trace + parallèle
chk("claim 17:21:56Z", bool(re.search(r"17[\u202f\u00a0 ]:21[\u202f\u00a0 ]:56Z", html)))
chk("refresh 17:40:53Z", bool(re.search(r"17[\u202f\u00a0 ]:40[\u202f\u00a0 ]:53Z", html)))
chk("trace 1a1a172f41684dc9 présente", "1a1a172f41684dc9-cron-agent-loop-202611042241" in html)
chk("R571 et pdf-27 dans l’apparat", "R571" in html and "pdf-27" in html)
chk("ouvrier parallèle pdf-26 documenté", "202611050041" in html and "pdf-26" in html)

# 10. méthode déclarée
chk("méthode mixte : tesseract + six passes VLM + SDK hors arbre", "tesseract" in html
    and "six passes" in html.lower() and "/home/z/vlm-sdk" in html)
chk("extraction 7 401 car déclarée", "7 401 car" in html)
chk("garant anti-chevauchement consigné", "garant anti-chevauchement" in html)

# 11. 0 arabe re-vérif
ar = re.findall(r"[\u0600-\u06FF\u0750-\u077F\u08A0-\u08FF\uFB50-\uFDF9\uFDFB-\uFDFF\uFE70-\uFEFF]", html)
chk("0 caractère arabe résiduel", len(ar) == 0)

print(f"\n=== BILAN : {ok} PASS / {fail} FAIL ===")
exit(1 if fail else 0)

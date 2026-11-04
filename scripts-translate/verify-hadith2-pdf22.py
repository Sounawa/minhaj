#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Minhāj — Vérification de la leçon hadith2-pdf-22 (leçon 21, les biens exemptés
de zakāt et les ayants droit, p.146-151) : sept renvois du Muwaṭṭaʾ tranchés
chiffre par chiffre (721/722/751/752×2/753/754/756) + Sunan Abī Dāwūd sans
numéro, bornes p.146-151 (objectifs leçon 21 p.146 ; préparation préalable du
cours suivant p.151 portée ; objectifs leçon 22 « la zakāt du fiṭr » p.152),
āya unique at-Tawba 60 (décalage zéro tranché PAR LE TEXTE, 59/61 testés),
gloses imprimées (fūrusk, ġārim, ʿāmil ʿalayhā), écarts déclarés (ouverture
du matn 721, tamr, fāʾida/fāʾa, yāʾuḫaḏ/yāʾuḫuḏ, li-ḏī mirratin sawāʾ contre
canonique li-qawiyyin muqwā, citation tronquée, bandeau, API vision 429),
claim takeover r566b (11:22:36Z → 11:54:22Z, refresh 12:11:10Z).
Usage: python3 scripts-translate/verify-hadith2-pdf22.py
"""
import re

HTML = "/home/z/my-project/tr-tmp/lesson-hadith2-pdf-22-fr.html"
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
chk("h1 unique avec « leçon 21 »", html.count("<h1>") == 1 and "leçon 21" in html.split("</h1>")[0])
chk("badge « Leçon 22 / 31 »", "Leçon 22 / 31" in html)
chk("pages 146 à 151 citées", "pages 146 à 151" in html)
chk("lesson-meta présent", '<dl class="lesson-meta">' in html and "Source du cours" in html)
chk("bornes inférieure et supérieure justifiées", "page 145 se clôt encore" in html and "la zakāt du fiṭr)" in html)

# 2. les renvois du Muwaṭṭaʾ — chacun cité avec n° explicite ; 752 à double occurrence
for n in [721, 722, 751, 752, 753, 754, 756]:
    chk(f"Muwaṭṭaʾ n° {n} cité", f"n° {n}" in html)
chk("n° 752 double occurrence (texte + cours)", html.count("n° 752") >= 2)
chk("Sunan Abī Dāwūd cité", "Sunan Abī Dāwūd" in html)

# 3. isnāds tranchés
chk("isnād 721 complet", "Zayd b. Aslam" in html and "ʿAṭāʾ b. Yasār" in html)
chk("isnād 756 complet", all(x in html for x in ["ʿAbdallāh b. Abī Bakr b. ʿAmr b. Ḥazm", "ʿUmar b. ʿAbd al-ʿAzīz", "Minā"]))
chk("tamhīd : envoi de Muʿāḏ au Yémen", "Muʿāḏ b. Ǧabal" in html and "Yémen" in html)
chk("exploitation : ʿAbdallāh b. ʿAmr", "ʿAbdallāh b. ʿAmr" in html)
chk("traduction du narrateur « a précédé »", "sa traduction a précédé" in html)

# 4. matns clés tranchés
chk("matn 752 espèces", "grenade" in html and "fūrusk" in html and "figue" in html)
chk("matn 721 les cinq", "qu’à cinq" in html and "voisin indigent" in html)
chk("matn 751 ḥawl sur le prix", "ḥawl se passe sur le prix" in html and "raisin sec" in html)
chk("matn 753 quḍḍ/buqūl", "quḍḍ" in html and "buqūl" in html)
chk("matn 754 esclave/cheval", "son esclave ni dans son cheval" in html)
chk("matn 756 miel", "ni du miel" in html)
chk("matn 722 ǧtihād du walī", "effort d’interprétation" in html and "gouverneur" in html)
chk("matn 722 besoin et nombre", "besoin et le nombre" in html)
chk("commentaire Médine/ḫuḍar", "Médine du temps du Prophète ﷺ" in html)
chk("cinq situations du riche", "cinq situations" in html and "un autre titre" in html)

# 5. āya cache + décalage tranché par le texte
chk("āya at-Tawba 60", "sourate 9 (at-Tawba), āya 60" in html)
chk("texte du cache (ouverture du verset)", "Les ṣadaqāt ne sont destinées que pour les pauvres" in html)
chk("décalage zéro documenté", "décalage zéro" in html and "59 et 61 testés" in html)
chk("citation tronquée déclarée", "farīḍatan mina llāhi" in html)
chk("renvois internes āya 60 ×3", html.count("sourate 9, āya 60") == 3)

# 6. glossaire imprimé
chk("glose fūrusk", "pêche rouge" in html)
chk("glose ġārim", "le débiteur" in html)
chk("glose ʿāmil ʿalayhā", "s’est coupé du reste des hommes" in html)
chk("qunya porté", "qunya" in html and "destinés à la qunya" in html)

# 7. écarts déclarés (jamais corrigés de mémoire)
for label, needle in [
    ("écart bandeau non restituable", "bandeau non restituable mot à mot"),
    ("écart tamhīd par fragments", "remonté par fragments"),
    ("écart aw ṣāra", "aw ṣāra"),
    ("écart ouverture matn 721", "inna la-ḫamsa"),
    ("écart espèce tamr (751)", "« tamr »"),
    ("écart fāʾida/fāʾa", "fāʾida/fāʾa"),
    ("écart yāʾuḫaḏ/yāʾuḫuḏ (756)", "yāʾuḫaḏ/yāʾuḫuḏ"),
    ("écart mirratin sawāʾ (imprimé)", "mirratin sawāʾ"),
    ("écart canonique li-qawiyyin muqwā", "li-qawiyyin muqwā"),
    ("écart numéro Abī Dāwūd non imprimé", "numéro du hadith n’est pas imprimé"),
    ("écart qism aṣ-ṣadaqāt/qisma", "qism aṣ-ṣadaqāt / qisma"),
    ("écart bi-šurūṭihi", "bi-šurūṭihi"),
    ("écart al-istiṯmār", "al-istiṯmār"),
    ("écart API vision 429", "429"),
    ("écart glose qunya non restituable", "glose marginale éventuelle de ce mot"),
]:
    chk(label, needle in html)

# 8. sections du gabarit
for section in ["Les objectifs de la leçon", "Les textes du cours",
                "Les traductions des transmetteurs", "Les définitions du cours",
                "L’extraction des contenus", "Le corps du cours", "L’évaluation",
                "L’exploitation", "La préparation préalable", "L’apparat de preuve de la livraison"]:
    chk(f"section « {section} »", f"<h2>{section}</h2>" in html)
chk("tamhīd en h3", "<h3>Le tamhīd</h3>" in html)
chk("trois fronts du corps (exemptions/ayants droit/répartition)", all(
    x in html for x in ["Premièrement : ce qui n’est pas zakatable",
                        "Deuxièmement : les ayants droit de la zakāt",
                        "Troisièmement : comment répartir la zakāt"]))
chk("préparation préalable : fiṭr ×3", html.count("zakāt du fiṭr") >= 3)

# 9. claim + chaîne de production
chk("claim décédé 11:22:36Z consigné", bool(re.search(r"11[\u202f: ]{1,2}22[\u202f: ]{1,2}36Z", html)))
chk("takeover 11:54:22Z consigné", bool(re.search(r"11[\u202f: ]{1,2}54[\u202f: ]{1,2}22Z", html)))
chk("refresh 12:11:10Z consigné", bool(re.search(r"12[\u202f: ]{1,2}11[\u202f: ]{1,2}10Z", html)))
chk("trace r566b consignée", "subagent-r566b-pdf22-minhaj" in html)
chk("trace décédée consignée", "subagent-r566-pdf22-minhaj" in html)
chk("registre 1121 → 1122", "1121 → 1122" in html)
chk("hadith-2es 21/30", "21/30" in html)
chk("prochain créneau pdf-23 (R568)", "pdf-23" in html and "R568" in html)
chk("triangulation triple déclarée", "triangulation triple" in html and "pdftotext" in html)

# 10. FR-seule déjà garanti par qa-lesson — double garde ici
# ﷺ (U+FDFA) exempté — convention du corpus (cf. qa-lesson.py)
chk("0 caractère arabe hors ﷺ (re-vérif)", not re.search(r"[\u0600-\u06FF\u0750-\u077F\u08A0-\u08FF\uFB50-\uFDF9\uFDFB-\uFDFF\uFE70-\uFEFF]", html))

print(f"\n=== verify-hadith2-pdf22 : {ok} PASS / {fail} FAIL ===")
raise SystemExit(1 if fail else 0)

# -*- coding: utf-8 -*-
"""
Minhāj — Vérification de la leçon hadith-3es / pdf-mut23h2x-410
(les compensations (fidya) pendant le pèlerinage — أحكام الفدية في الحج,
leçon 21 imprimée, p.141-146 du manuel hadith-3-iadadi_text.pdf, 196 p.)
Contrôles sur le HTML brut + le registre : garde-doublon, sections, numéros
du Muwaṭṭa' tranchés, adjudications consignées, longueur.
Usage: python3 scripts-translate/verify-hadith3-pdf410.py
"""
import json, re, sys, os

HTML = "/home/z/my-project/tr-tmp/lesson-hadith3-410-fr.html"
REG = "/home/z/my-project/content/books/hadith-3es.json"
CLAIM = "/home/z/my-project/tr-tmp/claims/hadith3-pdf-mut23h2x-410.claim.json"

ok, fail = 0, 0

def chk(label, cond):
    global ok, fail
    if cond: ok += 1
    else:
        fail += 1
        print(f"ÉCHEC : {label}")

html = open(HTML, encoding="utf-8").read()

# 0. garde-doublon registre
book = json.load(open(REG))
lesson = next((l for l in book["lessons"] if l["docId"] == "pdf-mut23h2x-410"), None)
chk("docId pdf-mut23h2x-410 présent au registre", lesson is not None)
if lesson:
    chk("htmlFr vide AVANT pose (garde-doublon)", not (lesson.get("htmlFr") or "").strip())

# 1. claim
chk("claim présent", os.path.exists(CLAIM))

# 2. longueur
chk(f"longueur >= 45 000 car (réel : {len(html)})", len(html) >= 45000)

# 3. sections obligatoires
for s in [
    "Les objectifs du cours", "Le <em>tamhīd</em>", "Les textes du cours",
    "La notice du transmetteur", "La glose des mots", "Le résumé du cours",
    "Le fiqh du hadith", "L’évaluation du cours", "L’exploitation du cours",
    "La préparation préalable", "L’apparat de preuve",
]:
    chk(f"section présente : {s}", s in html)

# 4. six textes
for t in ["Premier texte", "Deuxième texte", "Troisième texte",
          "Quatrième texte", "Cinquième texte", "Sixième texte"]:
    chk(f"texte : {t}", t in html)

# 5. numéros du Muwaṭṭa' (12 occurrences uniques)
for n in ["1240", "1242", "1243", "1244", "1245", "1248",
          "1260", "1261", "1266", "1241", "1262", "1255"]:
    chk(f"numéro : n° {n}", n in html)

# 6. matière adjudiquée (les 7 adjudications d'image consignées)
for key in ["quṭṭilat", "yughlaq", "’Abd al-Malik b. Qurayz", "sitta masākīn",
            "yaṣluḥ", "ḥafnat min ṭa’ām", "al-ḥayawānāt bi-mukhtalif anwā’ihā",
            "li-taqārubihimā fī al-qadr", "fīhi li-ḍ-ḍarūra"]:
    chk(f"matière : {key}", key in html)

# 7. trois gloses et notice
for key in ["ba’anāq", "al-yarbū’", "bijafra", "Tidris al-Asadī al-Makkī",
            "māt sanat 128"]:
    chk(f"notice/glose : {key}", key in html)

# 8. āyas et doctrine
chk("āya aṣ-Ṣāffāt 107", "107" in html)
chk("āya al-Baqara imprimée 195 consignée", "195" in html and "196" in html)
chk("doctrine R511 consignée", "doctrine R511" in html)

# 9. arabe uniquement dans spans RTL
body_no_spans = re.sub(r'<span dir="rtl" lang="ar">[^<]*</span>', '', html)
m = re.findall(r'[\u0600-\u06FF\u0750-\u077F\u08A0-\u08FF\uFB50-\uFDF9\uFDFB-\uFDFF\uFE70-\uFEFF]', body_no_spans)
chk(f"0 arabe hors spans RTL (réel : {len(m)})", len(m) == 0)

# 10. pas de placeholders
for bad in ["XXX", "TODO", "à compléter", "【", "TBD"]:
    chk(f"pas de placeholder : {bad!r}", bad not in html)

print(f"\n{ok} contrôles OK, {fail} échecs")
sys.exit(1 if fail else 0)

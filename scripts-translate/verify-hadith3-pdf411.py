# -*- coding: utf-8 -*-
"""
Minhāj — Vérification de la leçon hadith-3es / pdf-mut23h2x-411
(des règles de la compensation (fidya) — من أحكام الفدية, leçon 22 imprimée,
p.147-152 du manuel hadith-3-iadadi_text.pdf, 196 p.)
Usage: python3 scripts-translate/verify-hadith3-pdf411.py
"""
import json, re, sys, os

HTML = "/home/z/my-project/tr-tmp/lesson-hadith3-411-fr.html"
REG = "/home/z/my-project/content/books/hadith-3es.json"
CLAIM = "/home/z/my-project/tr-tmp/claims/hadith3-pdf-mut23h2x-411.claim.json.livre-r689c"

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
lesson = next((l for l in book["lessons"] if l["docId"] == "pdf-mut23h2x-411"), None)
chk("docId pdf-mut23h2x-411 présent au registre", lesson is not None)
if lesson:
    chk("htmlFr vide AVANT pose (garde-doublon)", not (lesson.get("htmlFr") or "").strip())

# 1. claim (libéré/archivé après adjudication, présent sous l'un des deux noms)
chk("claim présent (actif ou archivé)",
    os.path.exists(CLAIM) or os.path.exists(CLAIM.replace(".livre-r689c", "")))

# 2. longueur
chk(f"longueur >= 38 000 car (réel : {len(html)})", len(html) >= 38000)

# 3. sections obligatoires
for s in ["Les objectifs du cours", "Le <em>tamhīd</em>", "Les textes du cours",
          "La notice du transmetteur", "La glose des mots", "Le résumé du cours",
          "Le fiqh du hadith", "L’évaluation du cours", "L’exploitation du cours",
          "La préparation préalable", "L’apparat de preuve"]:
    chk(f"section présente : {s}", s in html)

# 4. deux textes
for t in ["Premier texte", "Deuxième texte"]:
    chk(f"texte : {t}", t in html)

# 5. numéros du Muwaṭṭa' (7 occurrences uniques)
for n in ["1252", "1263", "1255", "1251", "1256", "1241", "1253"]:
    chk(f"numéro : n° {n}", n in html)

# 6. matière adjudiquée
for key in ["’atq raqaba", "la’alaka adhāka hawāmuk", "madān madān li-kull insān",
            "li-ifādat ’umūm at-tathniya", "man nataf cha’ran",
            "šaǧǧat ra’sih", "hal taqra’ sūrat al-mā’ida", "taqarrab bihā",
            "al-kaffāra lā tatabadda’", "kamā amarah <em>llāh</em> ta’ālā"]:
    chk(f"matière : {key}", key in html)

# 7. notice et gloses
for key in ["Ka’b b. ’Uǧra", "māt sanat 51", "an-suk bi-cha’a", "ḥafna",
            "’Aṭā’ b. ’Abd <em>Allāh</em> <span dir=\"rtl\" lang=\"ar\">(اللَّه)</span> al-ḫurāsānī",
            "al-Mu’abbara", "Ibn Baṭṭāl", "4/174"]:
    chk(f"notice/glose : {key}", key in html)

# 8. āyas et doctrine
chk("āya al-Baqara imprimée 195 consignée", "195" in html and "196" in html)
chk("āya al-Mā’ida imprimée 97 consignée (cache 95)", "97" in html and "95" in html)
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

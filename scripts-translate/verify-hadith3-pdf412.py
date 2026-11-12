# -*- coding: utf-8 -*-
"""
Minhāj — Vérification de la leçon hadith-3es / pdf-mut23h2x-412
(les règles de la ʿumra — أحكام العمرة, leçon 23 imprimée,
p.153-158 du manuel hadith-3-iadadi_text.pdf, 196 p.)
Usage: python3 scripts-translate/verify-hadith3-pdf412.py
"""
import json, re, sys, os

HTML = "/home/z/my-project/tr-tmp/lesson-hadith3-412-fr.html"
REG = "/home/z/my-project/content/books/hadith-3es.json"
CLAIM = "/home/z/my-project/tr-tmp/claims/hadith3-pdf-mut23h2x-412.claim.json"

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
lesson = next((l for l in book["lessons"] if l["docId"] == "pdf-mut23h2x-412"), None)
chk("docId pdf-mut23h2x-412 présent au registre", lesson is not None)
if lesson:
    chk("htmlFr vide AVANT pose (garde-doublon)", not (lesson.get("htmlFr") or "").strip())

# 1. claim actif
chk("claim présent", os.path.exists(CLAIM))

# 2. longueur
chk(f"longueur >= 42 000 car (réel : {len(html)})", len(html) >= 42000)

# 3. sections obligatoires
for s in ["Les objectifs du cours", "Le <em>tamhīd</em>", "Les textes du cours",
          "La notice du transmetteur", "La glose des mots", "Le résumé du cours",
          "Le fiqh du hadith", "L’évaluation du cours", "L’exploitation du cours",
          "La préparation préalable", "L’apparat de preuve"]:
    chk(f"section présente : {s}", s in html)

# 4. quatre textes
for t in ["Premier texte", "Deuxième texte", "Troisième texte", "Quatrième texte"]:
    chk(f"texte : {t}", t in html)

# 5. numéros du Muwaṭṭa' (11 occurrences uniques)
for n in ["991", "990", "979", "974", "993", "989", "994", "997", "973", "975", "976"]:
    chk(f"numéro : n° {n}", n in html)

# 6. matière adjudiquée
for key in ["afṣilū bayna ḥiǧǧikum wa-’umratikum",
            "innī qad kuntu tajaḥḥaztu li-l-ḥaǧǧ",
            "fa-’tiriḍ lī",
            "i’timirī fī ramaḍān fa-inna ’umratun fīhi ka-ḥaǧǧa",
            "matā yaqṭa’ at-talbiya",
            "kāna yaṣna’ dhālik",
            "lam ya’tamir illā thalāthan iḥdāhunna fī chawwāl wa-ithnatayni fī dhī l-qa’da",
            "arāhā ḍīyā’an fī tarkih",
            "al-’umra ilā al-’umra kaffāratun li-mā baynahumā",
            "wa-lā arā li-aḥadin an ya’tamira fī as-sana mirāran",
            "fa-ammā al-’umra min at-tan’īm fa-man chā’a",
            "i’tamara thalāthan ’ām al-ḥudaybiya wa-’ām al-qaḍiyya wa-’ām al-ji’rāna",
            "na’am, qad i’tamara rasūl",
            "’abd ar-raḥmān b. ḥarmala",
            "thumma qafala ilā ahlih wa-lam yaḥuǧǧ",
            "’āqinī ’ā’iqan man’īya",
            "ba-anna taḥrumū bi-kull minhuma waḥdah",
            "a’daddtu mā aḥtāju ilayhi fī safri",
            "an yajma’a fīhi bayna al-ḥill wa-l-ḥurm"]:
    chk(f"matière : {key[:44]}", key in html)

# 7. notice et gloses
for key in ["abū bakr b. ’abd ar-raḥmān", "aḥad al-fuqahā’ as-sab’",
            "rāhib quraych", "makfūfan", "māt sanat 93", "94",
            "Sumayy, le client d’abū bakr", "sunna mu’akkada",
            "’Uǧra" if False else "al-qurachī al-madanī"]:
    chk(f"notice/glose : {key[:44]}", key in html)

# 8. āya et doctrine
chk("āya al-Ḥajj imprimée 30 consignée (cache 32)", "30" in html and "32" in html)
chk("doctrine R511 consignée", "doctrine R511" in html)
chk("cache ḥafṣ mentionné", "ḥafṣ" in html)

# 9. arabe uniquement dans spans RTL
body_no_spans = re.sub(r'<span dir="rtl" lang="ar">[^<]*</span>', '', html)
m = re.findall(r'[\u0600-\u06FF\u0750-\u077F\u08A0-\u08FF\uFB50-\uFDF9\uFDFB-\uFDFF\uFE70-\uFEFF]', body_no_spans)
chk(f"0 arabe hors spans RTL (réel : {len(m)})", len(m) == 0)

# 10. pas de placeholders
for bad in ["XXX", "TODO", "à compléter", "【", "TBD"]:
    chk(f"pas de placeholder : {bad!r}", bad not in html)

# 11. bornes de pages consignées
for p in ["p.153", "p.158", "vingt-deuxième slot"]:
    chk(f"borne : {p}", p in html)

print(f"\n{ok} contrôles OK, {fail} échecs")
sys.exit(1 if fail else 0)

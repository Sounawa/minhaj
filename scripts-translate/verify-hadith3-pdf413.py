# -*- coding: utf-8 -*-
"""
Minhāj — Vérification de la leçon hadith-3es / pdf-mut23h2x-413
(les règles de la victime sacrificielle — أحكام الأضحية, leçon 24 imprimée,
p.159-163 du manuel hadith-3-iadadi_text.pdf, 196 p.)
Usage: python3 scripts-translate/verify-hadith3-pdf413.py
"""
import json, re, sys, os

HTML = "/home/z/my-project/tr-tmp/lesson-hadith3-413-fr.html"
REG = "/home/z/my-project/content/books/hadith-3es.json"
CLAIM = "/home/z/my-project/tr-tmp/claims/hadith3-pdf-mut23h2x-413.claim.json"

ok, fail = 0, 0

def chk(label, cond):
    global ok, fail
    if cond: ok += 1
    else:
        fail += 1
        print(f"ÉCHEC : {label}")

html = open(HTML, encoding="utf-8").read()
text = re.sub(r'<[^>]+>', '', html)  # texte épuré des balises (contrôles de matière)

# 0. garde-doublon registre
book = json.load(open(REG))
lesson = next((l for l in book["lessons"] if l["docId"] == "pdf-mut23h2x-413"), None)
chk("docId pdf-mut23h2x-413 présent au registre", lesson is not None)
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

# 4. trois textes
for t in ["Premier texte", "Deuxième texte", "Troisième texte"]:
    chk(f"texte : {t}", t in html)

# 5. numéros du Muwaṭṭa' (4 occurrences uniques)
for n in ["1367", "1364", "1354", "1356"]:
    chk(f"numéro : n° {n}", n in html)

# 6. matière adjudiquée
for key in ["fa-ṣalli li-rabbika wa-nḥar",
            "al-aḍḥā yamāni baʿd yawm al-aḍḥā",
            "al-aḍḥā yawm naḥr wa-yamāni baʿdah",
            "bouchayr b. yasār",
            "lā aǧidu illā jaḏaʿan",
            "wa-in lam taǧid illā jaḏaʿan fa-dbaḥ",
            "an yaʿūda bi-baḍīḥa ukhrā",
            "qawī ʿalā thamanihā",
            "hanīʾ b. niyār al-balawī al-anṣārī",
            "mā istakmal sanatan wa-lam yadkhul fī th-thāniya",
            "qadara ʿalā thamanihā",
            "taqarruban ilā allāh taʿālā",
            "ḍuḥā",
            "sunna mu’akkada",
            "fa-l-yamsik ʿan chaʿrihi wa-aẓfārihi",
            "al-aḍḥā ʿalayya farīḍa wa-ʿalaykum sunna",
            "ayyāmin maʿlūmātin",
            "ayyāmin maʿdūdātin",
            "yawm naḥr wa-yamāni baʿdah",
            "man ṣallā ṣalātanā wa-nasaka nusukanā fa-qad aṣāb as-sunna",
            "tilka chāt laḥm",
            "an yuʿīda bi-baqar ukhrā",
            "wa-lā yanḥurū ḥattā yanḥur",
            "lā tuqaddimū bayna yaday allāh wa-rasūlih",
            "ḍaḥḥā marratan bi-l-madīna",
            "kabchan faḥīl afran",
            "fī muṣallā an-nās",
            "lays ar-raʾs bi-wāǧib ʿalā man ḍaḥḥā",
            "ẓalʿuhā", "al-ʿawrāʾ", "al-ʿaǧafāʾ", "lā tanqī",
            "chourūṭ al-aḍḥiyya wa-ḥukm ach-chirkah fīhā"]:
    chk(f"matière : {key[:44]}", key in text)

# 7. notices et autorités
for key in ["ash-chāfiʿī", "al-awzāʿī", "abū ḥanīfa", "ibn al-qaṣṣār",
            "ibn al-’arabī", "ṭabarānī", "umm salama", "jābir", "al-Ḥujurāt",
            "al-Kawthar", "minā", "hady", "tachrīq", "rafʿ", "mawqūf"]:
    chk(f"notice/glose : {key[:44]}", key in text)

# 8. āyas et doctrine
chk("āya al-Ḥajj imprimée 26 consignée (cache 28)", "26" in text and "28" in text)
chk("āya al-Baqara imprimée 201 consignée (cache 203)", "201" in text and "203" in text)
chk("doctrine R511 consignée", "doctrine R511" in text)
chk("cache ḥafṣ mentionné", "ḥafṣ" in text)
chk("référence al-Masālik 5/196", "5/196" in text)

# 9. arabe uniquement dans spans RTL
body_no_spans = re.sub(r'<span dir="rtl" lang="ar">[^<]*</span>', '', html)
m = re.findall(r'[\u0600-\u06FF\u0750-\u077F\u08A0-\u08FF\uFB50-\uFDF9\uFDFB-\uFDFF\uFE70-\uFEFF]', body_no_spans)
chk(f"0 arabe hors spans RTL (réel : {len(m)})", len(m) == 0)

# 10. pas de placeholders
for bad in ["XXX", "TODO", "à compléter", "【", "TBD", "immoration", "certillance"]:
    chk(f"pas de placeholder/typo : {bad!r}", bad not in html)

# 11. bornes de pages consignées
for p in ["p.159", "p.163", "vingt-troisième slot"]:
    chk(f"borne : {p}", p in html)

print(f"\n{ok} contrôles OK, {fail} échecs")
sys.exit(1 if fail else 0)

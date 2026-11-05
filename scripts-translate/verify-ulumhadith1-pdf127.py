#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Minhāj — Vérification de la leçon ulum-hadith-tanawi-1 / pdf-mut23h2q-127
(le ḥadīṯ munqaṭiʿ et le ḥadīṯ muʿḍal, p.80-84 du manuel ulum-hadith-1-thanawi.pdf) :
contrôle de contenu — bannière « al-dars 16 » + الحديث المنقطع والحديث المعضل
(tranchée image 600 dpi), matn « wa-kullu mā lam yattaṣil bi-ḥāli ʾisnāduhu min
ṭurfi l-ʾawṣāli » + « wa-l-muʿḍalu s-sāqiṭu minhu iṯnāni » (second hémistiche du
second bayt imprimé EN POINTS DE SUITE — blanc pédagogique, tenu tel qu'imprimé,
jamais reconstitué), gloses (ʾawṣāl = ʾaǧzāʾ wa-mafāṣil ; muʿḍal : ʿuḍla/dāhiya,
wa-dāʾ ʿuḍāl 2400 dpi contre ġuḍāl OCR récusé ; sāqiṭ = maḥḏūf), istikhlāṣ
al-maḍāmīn (2 questions), taḥlīl (2 sens du munqaṭiʿ, al-Ḫaṭīb/Ibn ʿAbd
al-Barr/al-Ǧurǧānī/al-Bayqūnī ḫilāf al-mašhūr, Nuzha d'Ibn Ḥaǧar + citation
al-ʿIrāqī « qabl al-wuṣūl ilā t-tābiʿī » tenu tel qu'imprimé 600 dpi, exemple
aṯ-Tirmiḏī des trois pierres « ʾinnahā rakson » tenu tel qu'imprimé, note
« lam yasmaʿ min ʾabīhi wa-lā yuʿraf ismuh »), muʿḍal (définition nāẓim,
ḥurūz, aʿḍalahu wa-aʿyāhu 2400 dpi, second type + avis Ibn aṣ-Ṣalāḥ, exemple
al-Ḥākim « fa-yuḫtamu ʿalā fīhi… ʾabʿadakanna llāhumma mā ḫāṣamtu ʾillā
fīkanna » — première lecture « barīʾtu minkunna » RÉCUSÉE à 2400 dpi),
farq (ʿumūm wa-ḫuṣūṣ bi-iṭlāq ; non-succession vs succession), taqwīm ×3,
istiṯmār (Ibn aṣ-Ṣalāḥ « qawlu l-muṣannifīn… wa-sammāhu l-Ḫaṭību ʾAbū Bakr
al-Ḥāfiẓu… mursalan » [maʿrifat ʾanwāʿ ʿulūm al-ḥadīṯ, p. 60] + 2 questions),
iʿdād qablī (3 questions → mudallas), bornes p.80-84 (bannière + objectifs
p.80 ; bannière al-dars 17 mudallas p.85 OCR 300 dpi concordante, iʿdād
qablī p.84), aucun āya, ﷺ tenu (U+FDFA exempté).
Usage: python3 scripts-translate/verify-ulumhadith1-pdf127.py
"""
import json
import re
import sys

HTML = "/home/z/my-project/tr-tmp/lesson-ulumhadith1-pdf-mut23h2q-127-fr.html"
REG = "/home/z/my-project/content/books/ulum-hadith-tanawi-1.json"

ok, fail = 0, 0


def chk(label, cond):
    global ok, fail
    if cond:
        ok += 1
    else:
        fail += 1
        print(f"ÉCHEC: {label}")


h = open(HTML, encoding="utf-8").read()
plain = h.replace("&nbsp;", " ").replace("\u202f", " ").replace("\u00a0", " ")

# 1. h1 aligné au titleFr pré-mappé du registre
tf = [l for l in json.load(open(REG, encoding="utf-8"))["lessons"]
      if l["docId"] == "pdf-mut23h2q-127"][0]["titleFr"]
m = re.match(r"<h1>(.*?)</h1>", h, re.S)
chk("h1 présent", bool(m))
chk("h1 aligné titleFr registre", m and m.group(1).replace("&nbsp;", " ").startswith(tf))
chk("h1 leçon 16", "leçon 16" in (m.group(1) if m else ""))

# 2. bannière / badge al-dars 16 (image 600 dpi)
chk("badge al-dars 16", "al-dars 16" in plain)

# 3. matn — bayts du nāẓim + points de suite
chk("bayt 1 translittéré", "wa-kullu mā lam yattaṣil bi-ḥāli ʾisnāduhu min ṭurfi l-ʾawṣāli" in plain)
chk("bayt 2 translittéré", "wa-l-muʿḍalu s-sāqiṭu minhu iṯnāni" in plain)
chk("second hémistiche en points de suite déclaré", "points de suite" in plain)
chk("blanc pédagogique jamais reconstitué", "jamais reconstitué" in plain)
chk("bandeau al-matn", "al-matn" in plain)

# 4. gloses
chk("glose ʾawṣāl", "les parties et les articulations" in plain)
chk("glose muʿḍal ʿuḍla/dāhiya", "dāhiya" in plain)
chk("glose wa-dāʾu ʿuḍālin (2400 dpi)", "wa-dāʾu ʿuḍālin" in plain)
chk("récusation ġuḍāl OCR", "ġuḍāl" in plain)
chk("glose sāqiṭ = maḥḏūf", "maḥḏūf" in plain)
chk("bandeau aš-šarḥ", "aš-šarḥ" in plain)

# 5. istikhlāṣ al-maḍāmīn — 2 questions
chk("istikhlāṣ 2 questions", "deux questions" in plain)
chk("Q1 premier bayt", "premier bayt" in plain)
chk("Q2 šaṭr du second bayt", "šaṭr (hémistiche) du second bayt" in plain)

# 6. taḥlīl — 2 sens du munqaṭiʿ
chk("bandeau at-taḥlīl (image)", "at-taḥlīl" in plain)
chk("sens large générique", "terme générique (ʿāmm)" in plain)
chk("chaîne al-Ḫaṭīb/Ibn ʿAbd al-Barr/al-Ǧurǧānī", "al-Ḫaṭīb al-Baġdādī, Ibn ʿAbd al-Barr et aš-Šarīf al-Ǧurǧānī" in plain)
chk("Bayqūnī ḫilāf al-mašhūr", "contre le mašhūr" in plain)
chk("Nuzha d'Ibn Ḥaǧar", "Ibn Ḥaǧar dans la Nuzha" in plain)
chk("citation al-ʿIrāqī", "les formes du ḥadīṯ munqaṭiʿ ont fait l’objet d’un désaccord" in plain)
chk("réf ʿIrāqī 215/1", "215/1" in plain)
chk("« qabl al-wuṣūl » tenu tel qu'imprimé", "qabl al-wuṣūl ilā t-tābiʿī" in plain)
chk("exemple Tirmiḏī trois pierres", "cherche-moi trois pierres" in plain)
chk("« rakson » tenu tel qu'imprimé", "rakson" in plain)
chk("réf Sunan aṯ-Tirmiḏī istinǧāʾ", "l’istinǧāʾ avec les deux pierres" in plain)
chk("note Tirmiḏī sur Abū ʿUbayda", "lam yasmaʿ min ʾabīhi wa-lā yuʿraf ismuh" in plain)
chk("munqaṭiʿ sans succession", "sans succession (ġayr mutawālī)" in plain)

# 7. muʿḍal
chk("ḥurūz milieu/début/fin", "le muʿallaq" in plain and "le mursal" in plain)
chk("aʿḍalahu wa-aʿyāhu (2400 dpi)", "aʿḍalahu wa-aʿyāhu" in plain)
chk("second type tābiʿ al-tābiʿī", "tābiʿ al-tābiʿī" in plain)
chk("avis Ibn aṣ-Ṣalāḥ ǧayyid ḥasan", "ǧayyid" in plain and "ḥasan" in plain)
chk("exemple al-Ḥākim sceau", "fa-yuḫtamu ʿalā fīhi" in plain)
chk("parole de la langue 2400 dpi", "ʾabʿadakanna llāhumma mā ḫāṣamtu ʾillā fīkanna" in plain)
chk("récusation barīʾtu minkunna", "barīʾtu minkunna" in plain)
chk("réf al-Ḥākim 38/1", "38/1" in plain)
chk("farq ʿumūm wa-ḫuṣūṣ", "ʿumūm wa-ḫuṣūṣ" in plain)
chk("farq non-succession/succession", "non-succession" in plain)

# 8. taqwīm ×3
chk("taqwīm 3 questions", "trois questions" in plain)
chk("Q rappel 1", "Je définis le ḥadīṯ munqaṭiʿ avec un exemple." in plain)
chk("Q rappel 2 divisions muʿḍal", "j’en expose les divisions" in plain)
chk("Q rappel 3 relation", "Quelle est la relation entre le ḥadīṯ muʿḍal et le ḥadīṯ munqaṭiʿ" in plain)

# 9. istiṯmār
chk("istiṯmār Ibn aṣ-Ṣalāḥ", "le dire des compilateurs" in plain)
chk("al-muṣannifīn translittéré", "al-muṣannifīn" in plain)
chk("sammāhu l-Ḫaṭību (600 dpi)", "wa-sammāhu l-Ḫaṭību ʾAbū Bakr al-Ḥāfiẓu" in plain)
chk("réf Ibn aṣ-Ṣalāḥ p. 60", "p. 60" in plain)
chk("2 questions examen", "Lequel des deux dires" in plain)
chk("Q ḫuṭabāʾ", "al-ḫuṭabāʾ" in plain)

# 10. iʿdād qablī + bornes
chk("iʿdād qablī 3 questions", "trois questions, toutes recouvrées" in plain)
chk("Q prép 1 mudallas", "qu’est-ce que le ḥadīṯ mudallas" in plain)
chk("Q prép 2 tadlīs isnād/shuyūḫ", "tadlīs de l’isnād et du tadlīs des shaykhs" in plain)
chk("Q prép 3 motivations", "motivations qui portent au tadlīs" in plain)
chk("bornes p.80-84", "page imprimée 80 et s’achève en la page 84" in plain)
chk("leçon suivante p.85 mudallas", "page 85 du même manuel" in plain)
chk("interdiction double rendu", "interdite de double rendu" in plain)
chk("aucune āya déclarée", "aucune āya" in plain)

# 11. cohérences techniques
chk("ﷺ tenu (exempté)", "ﷺ" in plain)
chk("0 caractère arabe résiduel", not re.search(r"[\u0600-\u06FF\u0750-\u077F\u08A0-\u08FF\uFB50-\uFD3E\uFDF0-\uFDFF]", re.sub(r"\uFDFA", "", plain)))
chk("0 apostrophe droite", "'" not in plain)
chk("« appariés »", plain.count("«") == plain.count("»"))
chk("killa documenté", "killa" in plain)

print(f"\nRÉSULTAT verify-127 : {ok} PASS / {fail} FAIL")
sys.exit(1 if fail else 0)

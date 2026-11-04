#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Minhāj — Vérification de la leçon ulum-hadith-tanawi-1 / pdf-mut23h2q-113
(le ḥadīṯ ṣaḥīḥ, p.17-22 du manuel ulum-hadith-1-thanawi.pdf) : contrôle
de contenu, manẓūma al-Bayqūnī rendue en sens (verses + altérations
déclarées), 5 conditions (3 sand : اتصال/شذوذ/علة + 2 rāwī : عدالة/ضبط
صدر-كتاب), مراتب الصحيح (أصح الأسانيد = سلسلة الذهب مالك-نافع-ابن عمر ;
7 catégories du scrupule ; alfiyya al-ʿIrāqī ; débat al-Buḫārī/Muslim
[Nuzha : 64 بتصرف] + ad-Dāraquṭnī), 0 citation coranique (cache non
sollicité), Zaraqānī [25] queue altérée déclarée, bornes p.17-22
(إعداد p.22 → الحسن ; objectifs L114 p.23).
Usage: python3 scripts-translate/verify-ulumhadith1-pdf113.py
"""
import re

HTML = "/home/z/my-project/tr-tmp/lesson-ulumhadith1-pdf-mut23h2q-113-fr.html"

ok, fail = 0, 0
def chk(label, cond):
    global ok, fail
    if cond: ok += 1
    else:
        fail += 1
        print(f"ÉCHEC: {label}")

html = open(HTML, encoding="utf-8").read()
text = re.sub(r"<[^>]+>", " ", html).replace("\u202f", " ").replace("\u00a0", " ")

# 0 arabe (ﷺ U+FDFA exempté)
arab = re.findall(r"[\u0600-\u06FF\u0750-\u077F\u08A0-\u08FF\uFB50-\uFDF9\uFDFB-\uFDFF\uFE70-\uFEFF]", text)
arab = [c for c in arab if c != "\ufdfa"]
chk("0 caractère arabe au corps", len(arab) == 0)

# structure + provenance
chk("h1 leçon 2", "leçon 2" in html and "<h1>" in html)
chk("lesson-meta présent", 'class="lesson-meta"' in html and "Source du cours" in html)
chk("bornes pages 17 à 22 citées", "pages 17 à 22" in html)
chk("bannière leçon 2 lue", "leçon 2&nbsp; : le ḥadīṯ ṣaḥīḥ" in html)
chk("miroir archive cité", "1_20220304_20220304_2251" in html)
chk("madḫal R578 cité", "tour R578" in html)
chk("OCR 300 dpi consigné", "OCR tesseract arabe local à 300 dpi" in html)
chk("borne jamais devinée", "jamais devinée" in html)
chk("cache coranique non sollicité", "n’est pas sollicité" in html)
chk("interdits double rendu", "interdites de double rendu" in html)

# contenu doctrinal
chk("manzuma rendue en sens", "chacune vint, et il la délimita" in html)
chk("définition synthétique", "le sand est connecté" in html and "l’écart et la cause taillante" in html)
chk("condition اتصال", "que le sand soit connecté" in html)
chk("définition du šāḏḏ", "la contradiction du transmetteur accepté" in html)
chk("définition de l’ʿilla", "qualité cachée qui porte atteinte" in html)
chk("définition de la justice", "la justice de transmission" in html)
chk("sortent non-musulman/pervers/inconnu", "le non-musulman, le pervers, et l’inconnu" in html)
chk("ḍabṭ ṣadr/kitāb", "la discipline du cœur" in html and "la discipline du livre" in html)
chk("silsila d’or", "la chaîne d’or" in html and "Mālik narra de Nāfiʿ" in html)
chk("az-Zuhrī/Sālim/son père", "az-Zuhrī, de Sālim, de son père" in html)
chk("Burayd b. ʿAbd Allāh", "Burayd b. ʿAbd Allāh b. Abī Burda" in html)
chk("Suhayl b. Abī Ṣāliḥ", "Suhayl b. Abī Ṣāliḥ" in html)
chk("7 catégories du scrupule", "s’accordèrent à extraire" in html and "la condition d’autre qu’eux deux" in html)
chk("alfiyya al-ʿIrāqī", "al-Ḥāfiẓ al-ʿIrāqī en son alfiyya" in html)
chk("débat Buḫārī/Muslim + masse", "la masse déclara explicitement d’avancer le Ṣaḥīḥ d’al-Buḫārī" in html)
chk("ad-Dāraquṭnī cité", "sans al-Buḫārī, Muslim ne serait point parvenu" in html)
chk("Nuzha 64 بتصرف", "Nuzha an-naẓar" in html and "64 — avec retouche" in html)
chk("poème تجاوز قوم", "lequel des deux avance" in html)
chk("deuxième poème déclaré", "le noble est plus doux" in html)
chk("Zaraqānī 25 queue déclarée", "non restituable, déclarée" in html and "Šarḥ az-Zarqānī ʿalā l-Bayqūniyya&nbsp; : p. 25" in html)

# sections du gabarit
for sec in ("Les objectifs de la leçon", "Le tamhīd", "Le commentaire", "La glose",
            "L’évaluation", "L’exploitation", "La préparation préalable"):
    chk(f"section {sec}", sec in html)

# évaluation 3 items LREAD (crop 600 dpi)
chk("éval item 1", "Quelle est la définition du ḥadīṯ ṣaḥīḥ&nbsp; ?" in html)
chk("éval item 2", "le sens de l’écart et de la cause taillante" in html)
chk("éval item 3", "deux critères de la variation des rangs" in html)

# préparation préalable = الحسن + «حسن صحيح» (p.22 LREAD)
chk("préparation item 1", "quel est le ḥadīṯ ḥasan et quelles sont ses espèces" in html)
chk("préparation item 2", "un ḥadīṯ ḥasan ṣaḥīḥ" in html)

# résidus interdits
for bad in ("XXX", "TODO", "待补充", "undefined", "NaN", "【"):
    chk(f"résidu {bad} absent", bad not in html)

print(f"\nverify-ulumhadith1-pdf113 : {ok} PASS / {fail} FAIL")
raise SystemExit(1 if fail else 0)

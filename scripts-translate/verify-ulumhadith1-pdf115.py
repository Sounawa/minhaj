#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Minhāj — Vérification de la leçon ulum-hadith-tanawi-1 / pdf-mut23h2q-115
(le ḥadīṯ ḍaʿīf, p.28-32 du manuel ulum-hadith-1-thanawi.pdf) : contrôle
de contenu — vers du nāẓim (tel qu'imprimé), définition par descente sous
la rangée du ḥasan, 5 causes de faiblesse, divisions (Ibn Ḥibbān ~50,
certain 126, méthode combinatoire, exemples munqaṭiʿ/šāḏḏ/mursal/muḍṭarib,
surnoms particuliers, mawḍūʿ = pire car mensonge), Ibn Ḥaǧar « de faible
utilité », jugement selon ce qui apparaît + al-ʿIrāqī [Šarḥ at-Tabṣira
wa-t-Taḏkira : 105/1], alfiyya du استثمار (yujbar tranché image 1200 dpi,
2 questions — la seconde lue à l'image), 0 citation coranique (cache non
sollicité), bornes p.28-32 (إعداد p.32 → marfūʿ/maqṭūʿ ; bannière
« الدرس 5 » + objectifs L116 p.33).
Usage: python3 scripts-translate/verify-ulumhadith1-pdf115.py
"""
import re

HTML = "/home/z/my-project/tr-tmp/lesson-ulumhadith1-pdf-mut23h2q-115-fr.html"

ok, fail = 0, 0
def chk(label, cond):
    global ok, fail
    if cond: ok += 1
    else:
        fail += 1
        print(f"ÉCHEC: {label}")

html = open(HTML, encoding="utf-8").read()
html = html.replace("\u202f", " ").replace("\u00a0", " ")
text = re.sub(r"<[^>]+>", " ", html)

# 0 arabe (ﷺ U+FDFA exempté)
arab = re.findall(r"[\u0600-\u06FF\u0750-\u077F\u08A0-\u08FF\uFB50-\uFDF9\uFDFB-\uFDFF\uFE70-\uFEFF]", text)
arab = [c for c in arab if c != "\ufdfa"]
chk("0 caractère arabe au corps", len(arab) == 0)

# structure + provenance
chk("h1 leçon 4", "leçon 4" in html and "<h1>" in html)
chk("h1 = registre titleFr", html.startswith("<h1>Le hadith faible (ḍaʿīf)"))
chk("lesson-meta présent", 'class="lesson-meta"' in html and "Source du cours" in html)
chk("bornes pages 28 à 32 citées", "pages 28 à 32" in html)
chk("bannière leçon 4 lue", "leçon 4&nbsp; : le ḥadīṯ faible" in html)
chk("miroir archive cité", "1_20220304_20220304_2251" in html)
chk("leçon R580 citée", "tour R580" in html)
chk("OCR 300 dpi consigné", "OCR tesseract arabe local à 300 dpi" in html)
chk("bannière 1200 dpi preuve", "bannière imprimée « leçon 4&nbsp; : le ḥadīṯ faible » fut lue à 1200 dpi [preuve commise]" in html)
chk("borne jamais devinée", "jamais devinée" in html)
chk("cache coranique non sollicité", "n’est pas sollicité" in html)
chk("interdits double rendu", "interdites de double rendu" in html)

# définition
chk("vers nāẓim rendu", "tout ce qui, de la rangée du ḥasan, fut en-deçà" in html)
chk("vers tel qu’imprimé", "[vers tel qu’imprimé]" in html)
chk("définition descente sous ḥasan", "tout ḥadīṯ qui descendit au-dessous de la rangée du ḥadīṯ ḥasan" in html)
chk("à plus forte raison ṣaḥīḥ", "à plus forte raison au-dessous de la rangée du ṣaḥīḥ" in html)
chk("qualités non réunies ḥasan", "les qualités du ḥadīṯ ḥasan" in html)

# 5 causes
chk("cause ittiṣāl", "la perte de la continuité de l’isnād" in html)
chk("cause ʿadāla", "la perte de l’uprightness chez les narrateurs" in html)
chk("cause ḍabṭ", "la perte de la discipline chez les narrateurs" in html)
chk("cause šāḏḏ", "la présence du šāḏḏ dans le matn ou dans l’isnād" in html)
chk("cause ʿilla qādiḥa", "la présence du défaut défectueux dans le matn ou dans l’isnād" in html)
chk("glose qaṣṣura", "il n’atteignit point la rangée du ḥasan" in html)
chk("glose ḍaʿīf لغة", "dérivé du ḍaʿf — le contraire de la force" in html)

# divisions
chk("vers aqsāmān kaṯūr", "et il est de divisions nombreuses" in html)
chk("Ibn Ḥibbān nom", "Abū Ḥātim Ibn Ḥibbān" in html)
chk("Ibn Ḥibbān ~50", "près de cinquante divisions [nombre en toutes lettres, tel qu’imprimé]" in html)
chk("certain 126", "cent vingt-six divisions [nombre en toutes lettres, tel qu’imprimé]" in html)
chk("degrés selon distance conditions", "varie selon sa distance des conditions de la santé" in html)
chk("surnoms particuliers 4", "le muḍṭarib, le maqlūb, le mawḍūʿ et le munkar" in html)
chk("méthode extraction", "La méthode de l’extraction de ces divisions" in html)
chk("exemple munqaṭiʿ seul", "le munqaṭiʿ seul est une division" in html)
chk("exemple quatrain", "le munqaṭiʿ šāḏḏ mursal muḍṭarib est une quatrième" in html)
chk("retour šāḏḏ cinquième", "le šāḏḏ seul est une cinquième division" in html)
chk("série mursal dixième", "le mursal muḍṭarib muʿḍal est une dixième" in html)
chk("listes surnoms espèces", "le munqaṭiʿ&nbsp; ; le muʿḍal&nbsp; ; le šāḏḏ&nbsp; ; le muʿallal&nbsp; ; le muḍṭarib&nbsp; ; le mursal&nbsp; ; le maqṭūʿ" in html)
chk("mawḍūʿ pire mensonge", "le mawḍūʿ, qui est le pire d’entre eux, parce qu’il est mensonge" in html)
chk("altérations déclarées méthode", "rendu en sens, altérations déclarées" in html)

# Ibn Ḥaǧar + jugement
chk("Ibn Ḥaǧar faible utilité", "est de faible utilité" in html)
chk("jugement selon apparition", "un jugement selon ce qui apparut" in html)
chk("non conforme réalité", "conforme à la réalité de l’affaire" in html)

# al-ʿIrāqī 105/1
chk("Irāqī quote intro", "lorsque les gens du ḥadīṯ disent" in html)
chk("Irāqī erreur/oubli", "l’erreur et de l’oubli chez le fiable" in html)
chk("khilāf khobar wāḥid", "le ḫabar du seul engendre le savoir apparent" in html)
chk("réf 105/1 imprimée", "Šarḥ at-Tabṣira wa-t-Taḏkira&nbsp; : « 105/1 » — tel qu’imprimé" in html)

# évaluation 3 items (300 dpi + crop)
chk("éval item 1", "Qu’est-ce que le ḥadīṯ faible&nbsp; ?" in html)
chk("éval item 2", "Quelles sont les causes de la faiblesse du ḥadīṯ&nbsp; ?" in html)
chk("éval item 3", "la représentation de trois d’entre elles" in html)

# exploitation alfiyya (image 1200 dpi)
chk("alfiyya argumentation", "l’on argumente par le faible" in html)
chk("jabr voie autre", "sont réparés par le fait qu’il est venu d’une voie autre qui dément" in html)
chk("non réparé cas graves", "il ne fut point réparé" in html)
chk("yujbar tranché image", "tranché par l’image à 1200 dpi, jamais deviné" in html)
chk("question jabr 1", "susceptible de réparation (jabr)" in html)
chk("question jabr 2 (lue à l’image)", "Comment répare-t-on le ḥadīṯ faible" in html)

# préparation préalable = marfūʿ/maqṭūʿ (p.32 LREAD)
chk("préparation item 1", "le ḥadīṯ marfūʿ" in html)
chk("préparation item 2", "le ḥadīṯ maqṭūʿ" in html)
chk("bornes finales p.28/p.32/p.33", "s’achève en la page 32" in html and "page 33 du même manuel" in html)

# sections du gabarit
for sec in ("Les objectifs de la leçon", "Le tamhīd", "Le commentaire", "La glose",
            "L’extraction des thèmes", "Premièrement", "Deuxièmement",
            "L’évaluation", "L’exploitation", "La préparation préalable"):
    chk(f"section {sec}", sec in html)

# résidus interdits
for bad in ("XXX", "TODO", "待补充", "undefined", "NaN", "【"):
    chk(f"résidu {bad} absent", bad not in html)

print(f"\nverify-ulumhadith1-pdf115 : {ok} PASS / {fail} FAIL")
raise SystemExit(1 if fail else 0)

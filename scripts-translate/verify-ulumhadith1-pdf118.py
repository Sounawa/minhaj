#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Minhāj — Vérification de la leçon ulum-hadith-tanawi-1 / pdf-mut23h2q-118
(le ḥadīṯ musalsal, p.43-46 du manuel ulum-hadith-1-thanawi.pdf) :
contrôle de contenu — bannière « leçon 7 » (tranchée image 1200 dpi),
deux bayts du nāẓim (tranchés image, tenus tels qu'imprimés), glose
« le successif et le semblable », définition du musalsal, formes ×3 :
par les états des narrateurs (parole — ḥadīṯ de Muʿāḏ tranché image,
chaîne Muʿāḏ/aṣ-Ṣanābiḥī/Abū ʿAbd ar-Raḥmān/ʿUqba b. Muslim tranchée
image, dire du musalsal tranché image 1400 dpi ; acte — Abū Hurayra et
al-Qāsim ﷺ tranché image [al-Asmāʾ wa-ṣ-Ṣifāt, bāb badʾ al-ḫalq] ;
réunion — Anas tranché image [Maʿrifa ʿulūm al-ḥadīṯ d'al-Ḥākim 1/29]),
par les qualités des narrateurs (sūrat aṣ-Ṣaff tranchée image 1400 dpi ;
al-qurrāʾ/ḥuffāẓ/Muḥammadīn/fuqahāʾ), par les qualités de la narration
(formules de l'accomplissement + condition d'al-Ḥākim ; temps — Ibn
ʿAbbās tranché image [as-Sunan al-kubrā d'al-Bayhaqī, kitāb ṣalāt
al-ʿīdayn] ; lieu — Multazam ; date — dernier de ceux qui rapportèrent),
0 citation coranique (cache non sollicité), bornes p.43-46 (إعداد p.46
→ ʿazīz ; objectifs L119 p.47). Usage: python3 scripts-translate/verify-ulumhadith1-pdf118.py
"""
import re

HTML = "/home/z/my-project/tr-tmp/lesson-ulumhadith1-pdf-mut23h2q-118-fr.html"

ok, fail = 0, 0
def chk(label, cond):
    global ok, fail
    if cond: ok += 1
    else:
        fail += 1
        print(f"ÉCHEC: {label}")

html = open(HTML, encoding="utf-8").read()
html = html.replace("\u202f", " ").replace("\u00a0", " ").replace("&nbsp;", " ")
html = re.sub(r" {2,}", " ", html)
text = re.sub(r"<[^>]+>", " ", html)

# 0 arabe (ﷺ U+FDFA exempté)
arab = re.findall(r"[\u0600-\u06FF\u0750-\u077F\u08A0-\u08FF\uFB50-\uFDF9\uFDFB-\uFDFF\uFE70-\uFEFF]", text)
arab = [c for c in arab if c != "\ufdfa"]
chk("0 caractère arabe au corps", len(arab) == 0)

# structure + provenance
chk("h1 leçon 7", "leçon 7" in html and "<h1>" in html)
chk("h1 = registre titleFr", html.startswith("<h1>Le hadith à chaîne caractéristique (musalsal)"))
chk("lesson-meta présent", 'class="lesson-meta"' in html and "Source du cours" in html)
chk("bornes pages 43 à 46 citées", "pages 43 à 46" in html)
chk("bannière leçon 7 lue", "leçon 7 : le ḥadīṯ musalsal" in html)
chk("bannière 1200 dpi preuve", "fut lue à 1200 dpi [preuve commise]" in html)
chk("miroir archive cité", "1_20220304_20220304_2251" in html)
chk("leçon R583 citée", "tour R583" in html)
chk("OCR 300 dpi consigné", "OCR tesseract arabe local à 300 dpi" in html)
chk("borne jamais devinée", "jamais devinée" in html)
chk("cache coranique non sollicité", "n’est pas sollicité" in html)
chk("aucune āya citée", "Aucune āya n’est citée" in html)
chk("interdits double rendu", "interdites de double rendu" in html)

# bayts du nāẓim (tranchés image)
chk("bayt 1 rendu", "tout ce qui vint sur une description" in html)
chk("bayt 1 exemple du dire", "quant à moi, par Dieu, le jeune homme m’informa" in html)
chk("bayt 2 rendu", "il me le narra certes debout" in html and "en souriant" in html)
chk("bayts tenus tels qu'imprimés", "bayts tenus tels qu’imprimés" in html)
chk("tranché image ×n", html.count("tranché par l’image") + html.count("tranchée par l’image") + html.count("tranchés par l’image") + html.count("tranchées par l’image") >= 8)

# glose
chk("glose successif/semblable", "le successif et le semblable" in html)

# extraction
chk("extraction q1", "qu’est-ce que l’on appelle ḥadīṯ musalsal" in html)
chk("extraction q2", "quelles sont les formes du ḥadīṯ musalsal" in html)

# définition
chk("def succession", "se succédèrent les narrateurs sur une qualité, ou une forme, ou un état, ou un dire" in html)
chk("def de l'entame au terme", "de l’entame du sanad à son terme" in html)
chk("def ressemblance à la chaîne", "ressemblance à la chaîne (silsila)" in html)
chk("def continuation + maillons", "quant à la continuation et à la ressemblance des maillons" in html)

# forme 1 : états — parole (Muʿāḏ)
chk("Muʿāḏ ouverture", "ô Muʿāḏ, par Dieu, je t’aime" in html)
chk("Muʿāḏ réponse", "mon père et ma mère pour toi" in html)
chk("Muʿāḏ recommandation", "que tu ne délaisses point, derrière chaque prière" in html)
chk("Muʿāḏ duʿāʾ", "aide-moi pour ton souvenir, ta gratitude et l’excellence de l’adoration" in html)
chk("réf Nasaʾī", "Sunan an-Nasaʾī" in html and "kitāb ʿamal al-yawm wa-l-layla" in html)
chk("chaîne wasiyya tranchée", "aṣ-Ṣanābiḥī" in html and "Abū ʿAbd ar-Raḥmān" in html and "ʿUqba b. Muslim" in html)
chk("dire du musalsal 1400 dpi", "et moi aussi je t’aime" in html and "1400 dpi" in html)
chk("fin du dire déclarée", "sa fin déclarée" in html)
chk("exemple du nāẓim répété", "puis l’autre dit à la manière de cela" in html)

# forme 1 : acte (Abū Hurayra / al-Qāsim)
chk("Abū Hurayra main entrelacée", "la main d’al-Qāsim ﷺ s’entrelaça avec ma main" in html)
chk("Abū Hurayra création", "Dieu créa la terre le jour du sabbat" in html)
chk("réf Asmāʾ wa-Ṣifāt", "al-Asmāʾ wa-ṣ-Ṣifāt d’al-Bayhaqī" in html and "bāb badʾ al-ḫalq" in html)
chk("musalsal par entrelacement", "l’entrelacement de la main de chacun d’eux" in html)
chk("bayt 2 commenté", "la station debout et le sourire sont une description d’acte" in html)
chk("alif d'absolution", "alif d’absolution" in html)

# forme 1 : réunion (Anas)
chk("Anas douceur de la foi", "la douceur de la foi" in html)
chk("Anas décret", "croie au décret, son bien et son mal, son doux et son amer" in html)
chk("Anas saisie de la barbe", "saisit sa barbe" in html)
chk("réf Ḥākim 1/29", "Maʿrifa ʿulūm al-ḥadīṯ d’al-Ḥākim" in html and ": 1/29" in html)
chk("musalsal par saisie barbe", "la saisie de la barbe de chacun d’eux" in html)

# forme 2 : qualités des narrateurs
chk("sūrat aṣ-Ṣaff", "sūrat aṣ-Ṣaff" in html)
chk("lecture tranchée", "un tel le lut de cette manière" in html)
chk("qualités d'acte ×4", "al-qurrāʾ" in html and "ḥuffāẓ" in html and "Muḥammadīn" in html and "fuqahāʾ" in html)

# forme 3 : qualités de la narration
chk("formules de l'accomplissement", "formules de l’accomplissement" in html)
chk("smiʿtu/ḥaddaṯanā/aḫbaranā", "j’entendis un tel" in html and "il nous narra" in html and "il nous informa" in html)
chk("condition al-Ḥākim", "quand même elles différeraient" in html)
chk("formule unique", "convergence sur une formule unique" in html)
chk("Ibn ʿAbbās matn", "j’assistai, avec le messager de Dieu ﷺ, à un jour de fête" in html)
chk("réf Bayhaqī", "as-Sunan al-kubrā d’al-Bayhaqī" in html and "kitāb ṣalāt al-ʿīdayn" in html and "yabdaʾ bi-ṣ-ṣalāt qabl al-ḫuṭba" in html)
chk("lieu de la narration", "le lieu de la narration" in html and "Multazam" in html)
chk("date de la narration", "la date de la narration" in html and "le dernier de ceux qui rapportèrent de son maître" in html)

# évaluation 3 items
chk("éval item 1", "Qu’est-ce que le ḥadīṯ musalsal" in html)
chk("éval item 2", "les formes les plus importantes" in html)
chk("éval item 3", "par les états des narrateurs" in html)

# exploitation 2 questions
chk("exploitation bornes des formes", "bornées à ce que mentionna le nāẓim" in html)
chk("exploitation fécondité", "la fécondité du tasalsul en le sanad" in html)

# préparation préalable = ʿazīz (p.46 + p.47 objectifs)
chk("préparation ʿazīz", "quel est le ḥadīṯ ʿazīz" in html and "la relation du ḥadīṯ ʿazīz au ṣaḥīḥ" in html)
chk("bornes finales p.43/p.46/p.47", "s’ouvre en la page imprimée 43 et s’achève en la page 46" in html and "ouvre en la page 47 du même manuel" in html)
chk("objectifs L119 lus", "le concept du ḥadīṯ ʿazīz" in html and "multiplicité des voies en la force du ḥadīṯ" in html)

# sections du gabarit
for sec in ("Les objectifs de la leçon", "Le tamhīd", "Le commentaire", "La glose",
            "L’extraction des thèmes", "Premièrement", "Deuxièmement",
            "L’évaluation", "L’exploitation", "La préparation préalable"):
    chk(f"section {sec}", sec in html)

# résidus interdits
for bad in ("XXX", "TODO", "待补充", "undefined", "NaN", "【"):
    chk(f"résidu {bad} absent", bad not in html)

print(f"\nverify-ulumhadith1-pdf118 : {ok} PASS / {fail} FAIL")
raise SystemExit(1 if fail else 0)

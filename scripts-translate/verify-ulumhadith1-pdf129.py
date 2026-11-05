#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Minhāj — Vérification de la leçon ulum-hadith-tanawi-1 / pdf-mut23h2q-129
(le ḥadīṯ šāḏḏ, p.91-94 du manuel ulum-hadith-1-thanawi.pdf) :
contrôle de contenu — bannière « ad-dars 18 » + الحديث الشاذ (image 600 dpi,
numéro 18 confirmé, zéro inversion) ; matn du nāẓim — « wa-mā yuḫālifu ṯiqatun
bihi l-malā » + second hémistiche imprimé EN POINTS DE SUITE (« fa-š-šāḏu » +
blanc pédagogique, tenu tel quel, jamais reconstitué) ; gloses (al-malāʾ =
al-ǧamāʿa min an-nās, hamza élidée pour le mètre ; šaḏḏa yašiḏḏu šuḏūḏan) ;
bandeau al-fahm + titre texte aš-šarḥ (600 dpi) ; istikhlāṣ ×2 ; at-taḥlīl :
définition du nāẓim (ṯiqatan fatha dans la citation), définition retenue
(ittiḥād maǧlis ar-riwāya), maḥfūẓ/rāǧiḥ, lieux de la contradiction (isnād :
rafʿ/waqf/waṣl/inqiṭāʿ ; matn : ziyāda/nuqṣān/taqdīm/taʾḫīr/qalb), al-Ḥākim
[119], al-Ḫallī [al-Iršād 176/1], ampleur des deux définitions, Ibn aṣ-Ṣalāḥ +
fard « ʾinnamā l-ʾaʿmālu bi-n-niyyāti » (Buḫārī, chaîne ʿUmar → ʿAlqama b.
Waqqāṣ → Muḥammad b. Ibrāhīm → Yaḥyā b. Saʿīd ; micro-symboles non tranchés
non reproduits), Muslim + az-Zuhrī (killa, ʾasānīd ǧiyād) ; aq-sām (isnād/mutn)
; exemple Abū Dāwūd « ʾiḏā ṣallā ʾaḥadkumu r-rukʿatayni qabla ṣ-ṣubḥi,
fa-l-yaḍṭaǧiʿ ʿalā yamīnih » [Sunan Abī Dāwūd] + ʿAbd al-Wāḥid b. Ziyād /
al-Aʿmaš / Abī Ṣāliḥ / Abī Hurayra + al-Bayhaqī (as-Sunan al-kubrā, at-Taymī /
as-Sammān ; « ʿĀʾiša et Ibn ʿAbbās ») ; taqwīm ×3 ; istiṯmār (Ibn Ḍaqīq al-ʿĪd
[al-Iqtirāḥ…, p. 268] — « lā yuḥtamal ḫalafuhū » tranché à l’image, récusation
de l’OCR) ; at-taʿammul ×2 ; iʿdād qablī (maqlūb ×2) ; bornes p.91-94 (bannière
dars 19 p.95 OCR 300 dpi passe R595, concordante avec l’iʿdād qablī p.94), aucune
āya, ﷺ tenu (U+FDFA exempté).
Usage: python3 scripts-translate/verify-ulumhadith1-pdf129.py
"""
import json
import re
import sys

HTML = "/home/z/my-project/tr-tmp/lesson-ulumhadith1-pdf-mut23h2q-129-fr.html"
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
      if l["docId"] == "pdf-mut23h2q-129"][0]["titleFr"]
m = re.match(r"<h1>(.*?)</h1>", h, re.S)
chk("h1 présent", bool(m))
chk("h1 aligné titleFr registre", m and m.group(1).replace("&nbsp;", " ").startswith(tf))
chk("h1 leçon 18", "leçon 18" in (m.group(1) if m else ""))

# 2. bannière / badge ad-dars 18
chk("badge ad-dars 18", "ad-dars 18" in plain)
chk("zéro inversion numéro", "zéro inversion" in plain)

# 3. matn — bayt du nāẓim + points de suite
chk("bayt hém. 1 translittéré (ḍamma متن)", "wa-mā yuḫālifu ṯiqatun bihi l-malā" in plain)
chk("bayt hém. 2 translittéré", "fa-š-šāḏu" in plain)
chk("second hémistiche en points de suite déclaré", "second hémistiche" in plain)
chk("blanc pédagogique jamais reconstitué", "jamais reconstitué" in plain)
chk("points de suite rendus", "................." in plain)
chk("bandeau al-matn", "al-matn" in plain)

# 4. gloses
chk("bandeau al-fahm documenté", "al-fahm" in plain)
chk("titre texte aš-šarḥ documenté", "aš-šarḥ" in plain)
chk("glose al-malāʾ = al-ǧamāʿa min an-nās", "al-ǧamāʿa min an-nās" in plain)
chk("hamza élidée nécessité du mètre", "ḍarūra al-wazn" in plain)
chk("glose šaḏḏa yašiḏḏu šuḏūḏan", "šaḏḏa yašiḏḏu šuḏūḏan" in plain)
chk("glose iḏā nfarada", "iḏā nfarada" in plain)

# 5. istikhlāṣ al-maḍāmīn — 2 questions
chk("istikhlāṣ 2 questions", "sous la forme de deux questions" in plain)
chk("Q1 ce qu'entend-on par le šāḏḏ", "Qu’entend-on par le ḥadīṯ šāḏḏ" in plain)
chk("Q2 divisions", "Quelles sont les divisions du ḥadīṯ šāḏḏ" in plain)

# 6. at-taḥlīl — définitions
chk("définition : ḍaʿīf sans chute d'hommes", "la chute de certains hommes de l’isnād" in plain)
chk("contradiction plus fort en amāna/ḥifẓ", "la fiabilité (al-amāna) et la rétention (al-ḥifẓ)" in plain)
chk("bayt citation du taḥlīl (fatha ṯiqatan)", "wa-mā yuḫālifu ṯiqatan bihi l-malā" in plain)
chk("définition retenue : masse des fiables", "la masse des transmetteurs fiables (aṯ-ṯiqāt)" in plain)
chk("awlā minhu", "celui qui a plus de droit que lui (awlā minhu)" in plain)
chk("ittiḥād maǧlis ar-riwāya", "ittiḥād maǧlis ar-riwāya" in plain)
chk("maḥfūẓ = rāǧiḥ matn/isnād", "celui qui l’emporte (ar-rāǧiḥ) en matn ou en isnād" in plain)
chk("wahm", "al-wahm" in plain)
chk("contradiction isnād rafʿ/waqf/waṣl/inqiṭāʿ", "rafʿ, ou waqf, ou waṣl, ou inqiṭāʿ" in plain)
chk("contradiction matn ziyāda/nuqṣān/taqdīm/taʾḫīr/qalb", "ziyāda) ou un retranchement (nuqṣān), ou une avancée (taqdīm) ou un report (taʾḫīr) ou une inversion (qalb)" in plain)
chk("muʿtamad : le nombre premier en rétention", "le nombre est plus digne de la rétention que l’unique" in plain)
chk("définition al-Ḥākim + [119]", "aṣl mutābiʿ" in plain and "p. 119" in plain)
chk("définition al-Ḫallī + [Iršād 176/1]", "šāḏa bi-dālika" in plain and "al-Iršād d’al-Ḫallī, 176/1" in plain)
chk("matrūk non accepté / taqqaf sur fiable", "matrūk" in plain and "yutawaqqafu fīhi" in plain)
chk("ampleur des deux définitions", "une ampleur considérable" in plain)
chk("al-Ḫallī n'exige pas l'isolement du fiable", "se contentant de la simple isolation" in plain)
chk("Ibn aṣ-Ṣalāḥ : non accepté ni droit", "point accepté ni droit" in plain)
chk("ʿadl ḥāfiẓ ḍābiṭ", "al-ʿadl al-ḥāfiẓ aḍ-ḍābiṭ" in plain)
chk("ḥadīṯ niyyāt", "ʾinnamā l-ʾaʿmālu bi-n-niyyāti" in plain)
chk("référence Buḫārī + points de référence tenus", "Ṣaḥīḥ al-Buḫārī" in plain and "comment fut le commencement de la révélation ...." in plain)
chk("chaîne ʿUmar → ʿAlqama b. Waqqāṣ", "ʿAlqama b. Waqqāṣ" in plain)
chk("chaîne → Muḥammad b. Ibrāhīm → Yaḥyā b. Saʿīd", "Muḥammad b. Ibrāhīm" in plain and "Yaḥyā b. Saʿīd" in plain)
chk("micro-symboles non tranchés déclarés", "non tranchables à 2400 dpi, ne furent point reproduits" in plain)
chk("Muslim : az-Zuhrī killa ʾasānīd ǧiyād", "de façon exclusive (killa)" in plain and "ʾasānīd ǧiyād" in plain)

# 7. aqsām + exemple
chk("aq-sām : lieu de l'anomalie", "mauḍiʿ wuqūʿ aš-šuḏūḏ" in plain)
chk("division 1 isnād", "L’anomalie dans l’isnād" in plain)
chk("division 2 matn", "L’anomalie dans le matn" in plain)
chk("exemple ʿAbd al-Wāḥid b. Ziyād", "ʿAbd al-Wāḥid b. Ziyād" in plain)
chk("chaîne al-Aʿmaš/Abī Ṣāliḥ/Abī Hurayra", "al-Aʿmaš, d’après Abī Ṣāliḥ, d’après Abī Hurayra" in plain)
chk("ḥadīṯ rakʿatayn", "ʾiḏā ṣallā ʾaḥadkumu r-rukʿatayni qabla ṣ-ṣubḥi, fa-l-yaḍṭaǧiʿ ʿalā yamīnih" in plain)
chk("référence Sunan Abī Dāwūd", "Sunan Abī Dāwūd" in plain and "l’allongement sur le flanc après elle" in plain)
chk("ḥikāya d'un acte du Prophète", "le récit (ḥikāya) d’un acte du Prophète" in plain)
chk("al-Bayhaqī as-Sunan al-kubrā", "as-Sunan al-kubrā" in plain)
chk("at-Taymī / as-Sammān", "Muḥammad b. Ibrāhīm at-Taymī" in plain and "as-Sammān" in plain)
chk("Bayhaqī : ʿĀʾiša et Ibn ʿAbbās", "l’ensemble des transmissions de ʿĀʾiša et d’Ibn ʿAbbās" in plain)

# 8. taqwīm — 3 questions
chk("taqwīm 3 questions", "sous la forme de trois questions" in plain)
chk("TQ1 dire retenu", "le dire retenu (al-muʿtamad) dans la définition du ḥadīṯ šāḏḏ" in plain)
chk("TQ2 infirād", "de l’isolement (infirād) du transmetteur" in plain)
chk("TQ3 divisions + illustration", "Avec l’illustration" in plain)

# 9. istiṯmār — Ibn Ḍaqīq al-ʿĪd
chk("citation Ibn Ḍaqīq al-ʿĪd", "Ibn Ḍaqīq al-ʿĪd dit" in plain)
chk("lā yuḥtamal ḫalafuhū tranché", "lā yuḥtamal ḫalafuhū" in plain)
chk("récusation de l'OCR documentée", "de l’OCR 300 récusé et tranché à l’image" in plain)
chk("référence al-Iqtirāḥ p. 268", "al-Iqtirāḥ fī bayān al-iṣṭilāḥ d’Ibn Ḍaqīq al-ʿĪd, p. 268" in plain)
chk("Taʿ 1 comparaison Bayqūniyya", "la définition de l’auteur de la Bayqūniyya" in plain)
chk("Taʿ 2 isolement non soutenu", "dont l’isolement ne se soutient point" in plain)

# 10. iʿdād qablī — leçon suivante maqlūb
chk("préparation maqlūb", "je reconnais le ḥadīṯ maqlūb" in plain)
chk("espèces du qalb", "les espèces de l’inversion (qalb) du ḥadīṯ" in plain)
chk("taʿammud al-qalb", "taʿammud al-qalb" in plain)
chk("bornes p.91-94 documentées", "s’ouvre en la page imprimée 91 et s’achève en la page 94" in plain)
chk("leçon suivante p.95 bannière ad-dars 19", "ad-dars 19" in plain and "page 95" in plain)
chk("leçon suivante interdite de double rendu", "interdite de double rendu" in plain)

# 11. ﷺ tenu, zéro āya
chk("ﷺ tenu (U+FDFA)", "\ufdfa" in h)
chk("doc mentionne aucune āya", "Aucune āya" in plain)

print(f"\n{ok}/{ok + fail} PASS" + ("" if fail == 0 else f" — {fail} ÉCHEC(S)"))
sys.exit(1 if fail else 0)

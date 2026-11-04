#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Minhāj — Vérification de la leçon ulum-hadith-tanawi-1 / pdf-mut23h2q-116
(le marfūʿ et le maqṭūʿ, p.33-37 du manuel ulum-hadith-1-thanawi.pdf) :
contrôle de contenu — vers du nāẓim (tranché image 1200 dpi), définition
du marfūʿ + 4 exemples (الدين النصيحة / كانت صلاة النبي بالليل مثنى متى
[séquence imprimée déclarée] / فعل بحضرة النبي / أحسن الناس خلقًا),
étendue du rasm (al-Ḫaṭīb vs Ibn Ḥaǧar vs Ibn aṣ-Ṣalāḥ), 2 espèces
(ṣaraḥatan/ḥukman, tranché image) + qarāʾin lafẓiyya/maʿnawiyya,
maqṭūʿ (definition + tābiʿi + Ḥasan al-Baṣrī + Masrūq), munqaṭiʿ vs
maqṭūʿ (Ibn aṣ-Ṣalāḥ/Šāfiʿī/Ṭabarānī/Barḏaʿī), استثمار 3 textes
(al-Musayyab موطأ / Abū Hurayra صحيح مسلم القدر, tattaḥa tel qu'imprimé /
Mālik غرر, tranchés image), 0 citation coranique (cache non sollicité),
bornes p.33-37 (إعداد p.37 → musnad/muttaṣil ; objectifs L117 p.38).
Usage: python3 scripts-translate/verify-ulumhadith1-pdf116.py
"""
import re

HTML = "/home/z/my-project/tr-tmp/lesson-ulumhadith1-pdf-mut23h2q-116-fr.html"

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
chk("h1 leçon 5", "leçon 5" in html and "<h1>" in html)
chk("h1 = registre titleFr", html.startswith("<h1>Le hadith élevé (marfūʿ) et le hadith coupé (maqṭūʿ)"))
chk("lesson-meta présent", 'class="lesson-meta"' in html and "Source du cours" in html)
chk("bornes pages 33 à 37 citées", "pages 33 à 37" in html)
chk("bannière leçon 5 lue", "leçon 5&nbsp; : le ḥadīṯ marfūʿ et le ḥadīṯ maqṭūʿ" in html)
chk("bannière 1200 dpi preuve", "fut lue à 1200 dpi [preuve commise]" in html)
chk("miroir archive cité", "1_20220304_20220304_2251" in html)
chk("leçon R581 citée", "tour R581" in html)
chk("OCR 300 dpi consigné", "OCR tesseract arabe local à 300 dpi" in html)
chk("borne jamais devinée", "jamais devinée" in html)
chk("cache coranique non sollicité", "n’est pas sollicité" in html)
chk("interdits double rendu", "interdites de double rendu" in html)

# vers + glose + questions d’ouverture
chk("vers nāẓim rendu", "ce qui est ajouté au Prophète est marfūʿ" in html and "ce qui revient au tābiʿ, c’est le maqṭūʿ" in html)
chk("vers tranché image 1200", "tranché par l’image à 1200 dpi" in html)
chk("glose marfūʿ", "un nom passif du verbe « élever&nbsp; »" in html)
chk("deux questions imprimées p.34", "par quoi nomme-t-on le ḥadīṯ musnad au Prophète" in html and "que désignent les muḥaddiṯs pour le ḥadīṯ musnad au tābiʿ" in html)

# marfūʿ définition + 4 exemples
chk("division en trois", "le mawqūf, le marfūʿ et le maqṭūʿ" in html)
chk("isnād même de nos jours", "et même un homme de notre époque actuelle" in html)
chk("4 modalités", "par parole, ou par acte, ou par approbation, ou par description" in html)
chk("exemple qawlī Dīn Naṣīḥa", "la religion est le bon conseil" in html)
chk("source Muslim īmān", "bāb bayān anna ad-dīn an-naṣīḥa" in html)
chk("exemple fiʿlī miṯnā matā déclaré", "« miṯnā matā » est tenue telle qu’imprimée, non interprétée, déclarée" in html)
chk("exemple taqrīrī", "sans qu’il ne rapporte le désaveu" in html)
chk("exemple waṣfī aḥsan nās ḫuluq", "le plus beau des hommes en la conduite" in html)
chk("fin waṣfī tranchée image", "fin du fragment tranchée par l’image à 1200 dpi" in html)

# étendue du rasm
chk("continué ou non + mursal/muʿallaq", "comme le mursal et le muʿallaq — cela est le fameux" in html)
chk("Ḫaṭīb", "al-Ḫaṭīb al-Bagdādī dit" in html and "les marāsīl des tābiʿūn" in html)
chk("Ibn Ḥaǧar réponse", "l’apparent est que la parole d’al-Ḫaṭīb sortit à la manière du fréquent" in html)
chk("Ibn aṣ-Ṣalāḥ rafʿ vs irsāl", "mit le marfūʿ en face du mursal" in html)
chk("marfūʿ plus ample", "le marfūʿ est plus ample que le continué" in html)

# espèces
chk("ṣaraḥatan/ḥukman tranché image", "explicitement (ṣaraḥatan), et le marfūʿ par indication (ḥukman)" in html)
chk("rubrique image", "rubrique imprimée tranchée par l’image" in html)
chk("qarāʾin lafẓiyya", "il éleva le ḥadīṯ, ou l’annonça, ou le fit parvenir" in html)
chk("qarāʾin lafẓiyya ṣaḥābī", "de la sunna, tel et tel" in html)
chk("qarāʾin maʿnawiyya israiliyyat", "ne prend point des récits israélites" in html)
chk("qarāʾin maʿnawiyya ṯawāb", "une récompense spécifiée ou un châtiment spécifié" in html)

# maqṭūʿ
chk("définition maqṭūʿ", "ajouté au tābiʿ — parole ou acte — à condition" in html)
chk("ni rafʿ ni waqf", "ce qui profite l’élévation ou l’arrêt" in html)
chk("interrompu en le rang", "interrompu en le rang, d’avec le marfūʿ et d’avec le mawqūf" in html)
chk("définition tābiʿ", "rencontra le Compagnon discernant, croyant au Prophète" in html)
chk("Ḥasan al-Baṣrī", "le dire d’al-Ḥasan al-Baṣrī en la prière derrière l’innovateur" in html)
chk("Ḥasan tranché image tel qu’imprimé", "[tel qu’imprimé, tranché par l’image à 1200 dpi]" in html)
chk("Masrūq Ibrāhīm b. al-Muntašir", "le dire d’Ibrāhīm b. Muḥammad b. al-Muntašir" in html)
chk("Masrūq rendu en sens déclaré", "le verbe imprimé tranché par l’image à 1200 dpi, sa construction déclarée" in html)

# munqaṭiʿ vs maqṭūʿ
chk("munqaṭiʿ isnād / maqṭūʿ matn", "le munqaṭiʿ est des qualités de l’isnād" in html and "des qualités du matn" in html)
chk("Ibn aṣ-Ṣalāḥ muḥaqqiqūn", "le connu auprès des vérificateurs est la nomination de cette espèce" in html)
chk("Šāfiʿī/Ṭabarānī", "aš-Šāfiʿī et aṭ-Ṭabarānī exprimer, parfois, par « munqaṭiʿ »" in html)
chk("Barḏaʿī", "il fit du munqaṭiʿ la parole du tābiʿ" in html)
chk("expansion avant établissement", "permission et extension en la terminologie, avant son établissement" in html)

# évaluation 3 items
chk("éval item 1", "avec la représentation de ses espèces" in html)
chk("éval item 2", "Je reconnais le ḥadīṯ maqṭūʿ avec la représentation" in html)
chk("éval item 3", "entre le ḥadīṯ maqṭūʿ et le ḥadīṯ munqaṭiʿ" in html)

# exploitation 3 textes + 2 questions
chk("Musayyab athar", "D’Yaḥyā b. Saʿīd qu’il entendit Saʿīd b. al-Musayyab dire" in html)
chk("Musayyab yūfūn/yanquṣūn", "où l’on donne la mesure complète" in html and "où l’on retranche la mesure" in html)
chk("Muslim Abū Hurayra", "le croyant fort est meilleur et plus aimé de Dieu que le croyant faible" in html)
chk("Muslim qadar réf", "bāb fī al-amr bil-quwwa wa-tark al-ʿaǧz" in html)
chk("tattaḥa tel qu’imprimé", "le verbe imprimé de la fin tranché par l’image à 1200 dpi, tenu tel qu’imprimé" in html)
chk("Mālik ġaṭāṭ", "couvre à un homme la marchandise" in html)
chk("Mālik ġarar", "un aléa (ġarar) — il ne sait combien il lui fixa" in html)
chk("Mālik réf muwaṭṭa", "Muwaṭṭaʾ de l’ʾimām Mālik&nbsp; ; kitāb al-buyūʿ&nbsp; ; bāb ǧāmiʿ al-buyūʿ" in html)
chk("questions exploitation ×2", "Par quoi le premier ḥadīṯ est-il nommé" in html and "Par quoi le second ḥadīṯ est-il nommé" in html)

# préparation préalable = musnad/muttaṣil (p.37 LREAD)
chk("préparation item 1", "je reconnais les deux ḥadīṯs, le musnad et le muttaṣil" in html)
chk("préparation item 2", "entre le ḥadīṯ musnad, le muttaṣil et le marfūʿ" in html)
chk("bornes finales p.33/p.37/p.38", "s’achève en la page 37" in html and "page 38 du même manuel" in html)

# sections du gabarit
for sec in ("Les objectifs de la leçon", "Le tamhīd", "Le commentaire", "La glose",
            "L’extraction des thèmes", "Premièrement", "Deuxièmement",
            "L’évaluation", "L’exploitation", "La préparation préalable"):
    chk(f"section {sec}", sec in html)

# résidus interdits
for bad in ("XXX", "TODO", "待补充", "undefined", "NaN", "【"):
    chk(f"résidu {bad} absent", bad not in html)

print(f"\nverify-ulumhadith1-pdf116 : {ok} PASS / {fail} FAIL")
raise SystemExit(1 if fail else 0)

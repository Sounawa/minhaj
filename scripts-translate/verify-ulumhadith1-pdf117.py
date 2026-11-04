#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Minhāj — Vérification de la leçon ulum-hadith-tanawi-1 / pdf-mut23h2q-117
(le musnad et le muttaṣil, p.38-42 du manuel ulum-hadith-1-thanawi.pdf) :
contrôle de contenu — bannière « leçon 6 » (tranchée image 1200 dpi),
deux bayts du nāẓim (tranchés image), trois emplois du terme musnad
(Musnad d'Aḥmad / Musnad d'aš-Šihāb / ḥadīṯ du poème), trois définitions
(al-Ḥākim préféré par Ibn Ḥaǧar / Ibn ʿAbd al-Barr réprouvé / al-Ḫaṭīb +
al-ʿIrāqī + Ibn aṣ-Ṣalāḥ [Muqaddima : 42]), exemple d'al-Buḫārī (matn
tranché image), muttaṣil (définition + 2 exemples du Muwaṭṭaʾ tranchés
image, 2 verbes imprévus tenus tels qu'imprimés), dires des tābiʿūn
(al-ʿIrāqī [Šarḥ at-Tabṣira : 184/1]), exploitation Ibn Ḥaǧar
[an-Nukat 1/506] tranchée image, 0 citation coranique (cache non
sollicité), bornes p.38-42 (إعداد p.42 → musalsal ; objectifs L118 p.43).
Usage: python3 scripts-translate/verify-ulumhadith1-pdf117.py
"""
import re

HTML = "/home/z/my-project/tr-tmp/lesson-ulumhadith1-pdf-mut23h2q-117-fr.html"

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
chk("h1 leçon 6", "leçon 6" in html and "<h1>" in html)
chk("h1 = registre titleFr", html.startswith("<h1>Le hadith pourvu d’isnād (musnad) et le hadith à chaîne continue (muttaṣil)"))
chk("lesson-meta présent", 'class="lesson-meta"' in html and "Source du cours" in html)
chk("bornes pages 38 à 42 citées", "pages 38 à 42" in html)
chk("bannière leçon 6 lue", "leçon 6 : le ḥadīṯ musnad et le ḥadīṯ muttaṣil" in html)
chk("bannière 1200 dpi preuve", "fut lue à 1200 dpi [preuve commise]" in html)
chk("miroir archive cité", "1_20220304_20220304_2251" in html)
chk("leçon R582 citée", "tour R582" in html)
chk("OCR 300 dpi consigné", "OCR tesseract arabe local à 300 dpi" in html)
chk("borne jamais devinée", "jamais devinée" in html)
chk("cache coranique non sollicité", "n’est pas sollicité" in html)
chk("aucune āya citée", "Aucune āya n’est citée" in html)
chk("interdits double rendu", "interdites de double rendu" in html)

# bayts du nāẓim (tranchés image)
chk("bayt 1 musnad rendu", "celui dont l’isnād se continue depuis son narrateur jusqu’au Muṣṭafā" in html)
chk("bayt 1 fin déclarée", "et ne parut point [de rupture]" in html and "bayt tenu tel qu’imprimé, sa fin déclarée" in html)
chk("bayt 2 muttaṣil rendu", "celui qui se continue, par l’audition de chaque narrateur" in html and "c’est le muttaṣil" in html)
chk("bayts tranchés image", html.count("tranché par l’image à 1200 dpi") + html.count("tranchés par l’image") >= 6)

# trois emplois du musnad
chk("emploi Musnad Aḥmad", "le Musnad de l’ʾimām Aḥmad" in html)
chk("emploi Musnad aš-Šihāb", "le Musnad d’aš-Šihāb d’al-Qaḍāʿī" in html)
chk("emploi ḥadīṯ du poème", "le ḥadīṯ visé par le poème" in html)

# trois définitions
chk("qawl 1 al-Ḥākim", "Abū ʿAbd Allāh al-Ḥākim" in html and "voilà un sanad continué" in html)
chk("qawl 1 préféré Ibn Ḥaǧar", "Ibn Ḥaǧar et d’autres préférèrent ce dire" in html)
chk("qawl 2 Ibn ʿAbd al-Barr", "Ibn ʿAbd al-Barr le choisit" in html)
chk("qawl 2 récusation", "avérer le mursal, le muʿḍal et le munqaṭiʿ" in html and "nul ne tient ce dire" in html)
chk("qawl 3 al-Ḫaṭīb", "jusqu’à son extrême terme" in html and "c’est le dire d’al-Ḫaṭīb" in html)
chk("qawl 3 al-ʿIrāqī récusation", "l’entrée du maqṭūʿ et du mawqūf" in html and "la parole des gens du ḥadīṯ le réprouve" in html)
chk("qawl 3 Ibn aṣ-Ṣalāḥ [42]", "Muqaddimat Ibn aṣ-Ṣalāḥ" in html and ": 42]" in html)

# exemple al-Buḫārī
chk("isnād Buḫārī", "nous rapporta Abū ʿĀṣim, de Mālik, d’Abī az-Zinād, d’ʿAbd ar-Raḥmān al-Aʿraǧ, d’Abī Hurayra" in html)
chk("matn Buṫārī tranché image", "que nul de vous ne prie en un vêtement unique où il n’y a rien sur ses deux épaules" in html)
chk("réf Buṫārī", "kitāb aṣ-ṣalāh" in html and "bāb idā ṣallā fī aṯ-ṯawb al-wāḥid fal-yajʿal ʿalā ʿātiqayh" in html)
chk("conclusion double qualité", "les deux qualités de continuation et d’élévation" in html)
chk("musnad ṣaḥīḥ ou faible", "peut être ṣaḥīḥ et peut être faible" in html)

# muttaṣil définition + 2 exemples
chk("définition muttaṣil", "entendit de celui qui est au-dessus de lui" in html)
chk("ou au seul Compagnon", "ou au seul Compagnon, contre l’apparent du matn" in html)
chk("exemple 1 matn", "la prière en commun surpasse la prière de l’homme seul de sept et vingt degrés" in html)
chk("exemple 1 réf", "kitāb as-sahw" in html and "faḍl ṣalāt al-ǧamāʿa ʿalā ṣalāt al-fard" in html)
chk("exemple 2 isnād", "de Yaḥyā b. Saʿīd et de Yazīd b. ʿAbd Allāh b. Qušayṭ al-Layṯī, de Saʿīd b. al-Musayyab" in html)
chk("exemple 2 ʿUmar", "ʿUmar b. al-Ḫaṭṭāb dit" in html and "toute femme répudiée qui a ses règles une ou deux fois" in html)
chk("exemple 2 verbes tenus imprimés ×2", html.count("verbe imprimé tenu tel qu’imprimé, tranché par l’image") == 2)
chk("exemple 2 réf", "kitāb aṭ-ṭalāq" in html and "bāb ǧāmiʿ ʿiddat aṭ-ṭalāq" in html)
chk("morale exemple 2", "il est muttaṣil, non musnad" in html)

# dires des tābiʿūn + al-ʿIrāqī
chk("tābiʿūn non nommés", "on ne les nomme point muttaṣil" in html)
chk("restriction permise", "ceci est continué jusqu’à Saʿīd b. al-Musayyab" in html and "az-Zuhrī" in html)
chk("réf al-ʿIrāqī", "Šarḥ at-Tabṣira wa-t-Taḏkira d’al-ʿIrāqī" in html and ": 184/1]" in html)

# évaluation 3 items
chk("éval item 1", "les emplois du musnad chez les muḥaddiṯs" in html)
chk("éval item 2", "avec sa justification" in html)
chk("éval item 3", "la distinction entre le ḥadīṯ musnad et le ḥadīṯ muttaṣil" in html)

# exploitation Ibn Ḥaǧar
chk("Ibn Ḥaǧar ouverture", "quant à al-Ḥākim et à d’autres, ils départagèrent" in html)
chk("marfūʿ état du matn", "l’état du matn, délaissant la considération de l’isnād" in html)
chk("muttaṣil état du sanad", "l’état du sanad, délaissant la considération du matn" in html)
chk("musnad deux états", "les deux états ensemble" in html)
chk("ʿumūm/ḫuṣūṣ + inverse", "tout musnad est marfūʿ, et tout musnad est muttaṣil — et l’inverse n’est point en les deux" in html)
chk("réf an-Nukat 1/506", "an-Nukat ʿalā kitāb Ibn aṣ-Ṣalāḥ du ḥāfiẓ Ibn Ḥaǧar" in html and ": 1/506 — tranché par l’image à 1200 dpi]" in html)

# préparation préalable = musalsal (p.42 LREAD + p.43 objectifs)
chk("préparation musalsal", "quel est le ḥadīṯ musalsal" in html and "la finalité du tasalsul en le ḥadīṯ" in html)
chk("bornes finales p.38/p.42/p.43", "s’ouvre en la page imprimée 38 et s’achève en la page 42" in html and "ouvre en la page 43 du même manuel" in html)
chk("objectifs L118 lus", "le concept du ḥadīṯ musalsal et ses espèces" in html and "annonce expressément le musalsal" in html)

# sections du gabarit
for sec in ("Les objectifs de la leçon", "Le tamhīd", "Le commentaire", "La glose",
            "L’extraction des thèmes", "Premièrement", "Deuxièmement",
            "L’évaluation", "L’exploitation", "La préparation préalable"):
    chk(f"section {sec}", sec in html)

# résidus interdits
for bad in ("XXX", "TODO", "待补充", "undefined", "NaN", "【"):
    chk(f"résidu {bad} absent", bad not in html)

print(f"\nverify-ulumhadith1-pdf117 : {ok} PASS / {fail} FAIL")
raise SystemExit(1 if fail else 0)

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Minhāj — Vérification de la leçon ulum-hadith-tanawi-1 / pdf-mut23h2q-114
(le ḥadīṯ ḥasan, p.23-27 du manuel ulum-hadith-1-thanawi.pdf) : contrôle
de contenu, définitions du ḥasan (Bayqūnī/al-Ḫaṭṭābī/at-Tirmiḏī/Ibn
al-Ǧawzī/Ibn aṣ-Ṣalāḥ/az-Zaraqānī), 2 espèces (لغيره/لذاته) + 2 exemples
(femmes de Banū Fizāra pour deux sandales tranché par image 900 dpi ;
siwāk d'Abū Hurayra), nom Abū Ḥudard al-Aslamī tranché par image 1200 dpi,
0 citation coranique (cache non sollicité), réf. ordres imprimés déclarés
(6/1, 573/2, 15/1, 39/1), bornes p.23-27 (إعداد p.27 → الضعيف ;
objectifs L115 p.28).
Usage: python3 scripts-translate/verify-ulumhadith1-pdf114.py
"""
import re

HTML = "/home/z/my-project/tr-tmp/lesson-ulumhadith1-pdf-mut23h2q-114-fr.html"

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
chk("h1 leçon 3", "leçon 3" in html and "<h1>" in html)
chk("h1 = registre titleFr", html.startswith("<h1>Le hadith satisfaisant (ḥasan)"))
chk("lesson-meta présent", 'class="lesson-meta"' in html and "Source du cours" in html)
chk("bornes pages 23 à 27 citées", "pages 23 à 27" in html)
chk("bannière leçon 3 lue", "leçon 3&nbsp; : le ḥadīṯ ḥasan" in html)
chk("miroir archive cité", "1_20220304_20220304_2251" in html)
chk("leçon R579 citée", "tour R579" in html)
chk("OCR 300 dpi consigné", "OCR tesseract arabe local à 300 dpi" in html)
chk("borne jamais devinée", "jamais devinée" in html)
chk("cache coranique non sollicité", "n’est pas sollicité" in html)
chk("interdits double rendu", "interdites de double rendu" in html)

# définitions
chk("vers nāẓim rendu", "le connu par ses voies" in html)
chk("verbe médian incertain déclaré", "verbe médian incertain entre trois lectures" in html)
chk("définition de l’auteur", "les voies et les sources de sortie furent connues" in html)
chk("Ḫaṭṭābī + Maʿālim as-Sunan 6/1", "Abū Sulaymān al-Ḫaṭṭābī" in html and "Maʿālim as-Sunan&nbsp; : « 6/1 »" in html)
chk("objection + ajout du nāẓim", "pour repousser cette objection" in html)
chk("Tirmiḏī + Šarḥ al-ʿIlal 573/2", "Abū ʿĪsā at-Tirmiḏī" in html and "Šarḥ al-ʿIlal aṣ-ṣaġīr&nbsp; : « 573/2 »" in html)
chk("objection Ǧāmiʿ déclarée", "son comportement en le Ǧāmiʿ le contredit" in html and "altération déclarée" in html)
chk("réponse Nukhba composés", "ḥasan ṣaḥīḥ » ou « ḥasan ġarīb" in html)
chk("Ibn al-Ǧawzī + Mawḍūʿāt 15/1", "Ibn al-Ǧawzī dit" in html and "al-Mawḍūʿāt&nbsp; : « 15/1 »" in html)
chk("objection Ibn Daqīq al-ʿĪd", "Ibn Daqīq al-ʿĪd objecta" in html)
chk("Ibn aṣ-Ṣalāḥ deux espèces", "le ḥadīṯ ḥasan est de deux espèces" in html)
chk("mustūr premier type", "un voilé (mustūr) dont l’aptitude ne fut pas vérifiée" in html)
chk("Muqaddima 31 avec retouche", "Muqaddimat Ibn aṣ-Ṣalāḥ&nbsp; : 31 — avec retouche" in html)
chk("Zaraqānī définition agréée", "un transmetteur juste dont la discipline est légère, qui n’est ni šāḏḏ ni muʿallal" in html)

# espèces + exemples
chk("ḥasan par autrui / par lui-même", "le ḥasan par autrui" in html and "le ḥasan par lui-même" in html)
chk("Fizāra deux sandales tranchées image", "pour deux sandales [tel qu’imprimé, tranché par image à 900 dpi]" in html)
chk("abwāb an-nikāḥ maḥūr", "bāb mā ǧāʾa fī maḥūr an-nisāʾ" in html)
chk("liste Compagnons", "de ʿĀʾiša, de Ǧābir, et d’Abū Ḥudard al-Aslamī" in html)
chk("nom tranché image 1200 dpi", "nom final tranché par recadrage à 1200 dpi, jamais deviné" in html)
chk("ʿĀṣim faible mémoire", "ʿĀṣim b. ʿUbayd Allāh est faible pour la faiblesse de sa mémoire" in html)
chk("siwāk exemple", "ordonné le siwāk à chaque prière" in html)
chk("siwāk source", "bāb mā ǧāʾa fī as-siwāk" in html)
chk("mutābaʿa → ṣaḥīḥ par autrui", "il est donc ṣaḥīḥ par autrui" in html)

# rangs
chk("partage obligation/argumentation", "l’obligation de l’acte et l’argumentation par lui" in html)
chk("ʿAmr b. Šuʿayb sommet", "la narration de ʿAmr b. Šuʿayb, de son père, de son aïeul" in html)
chk("bas = ḥasan par autrui", "son plus bas&nbsp; : le ḥasan par autrui" in html)

# évaluation 3 items (crop 600 dpi)
chk("éval item 1", "les dires des muḥaddiṯs en la définition du ḥadīṯ ḥasan" in html)
chk("éval item 2", "j’en donne un exemple pour chacune" in html)
chk("éval item 3", "du point de vue de l’argumentation par lui" in html)

# exploitation Ibn aṣ-Ṣalāḥ 39/1
chk("exploitation quote", "jonction de la négation de cette infériorité et de son affirmation" in html)
chk("réf 39/1 imprimée", "Muqaddimat Ibn aṣ-Ṣalāḥ&nbsp; : « 39/1 » — tel qu’imprimé" in html)
chk("consigne Zaraqānī", "le Šarḥ az-Zarqānī ʿalā l-Bayqūniyya et je réponds" in html)

# préparation préalable = الضعيف (p.27 LREAD)
chk("préparation item 1", "qu’est-ce que le ḥadīṯ faible" in html)
chk("préparation item 2", "les divisions du ḥadīṯ faible" in html)

# sections du gabarit
for sec in ("Les objectifs de la leçon", "Le tamhīd", "Le commentaire", "La glose",
            "L’évaluation", "L’exploitation", "La préparation préalable"):
    chk(f"section {sec}", sec in html)

# résidus interdits
for bad in ("XXX", "TODO", "待补充", "undefined", "NaN", "【"):
    chk(f"résidu {bad} absent", bad not in html)

print(f"\nverify-ulumhadith1-pdf114 : {ok} PASS / {fail} FAIL")
raise SystemExit(1 if fail else 0)

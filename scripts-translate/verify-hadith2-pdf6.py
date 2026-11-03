#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Minhāj — Vérification de la leçon hadith2-pdf-6 (leçon 5, ما يطلب فعله أو تركه
في الصلاة فرضا ونفلا, p.40-45) : contrôle de contenu, numéros du Muwaṭṭaʾ
tranchés par preuve image (461/464/466/469/471/478 contre les formes de couches
164/464/664/964/174/874 — inversion TOTALE), bornes p.40-45 à triple
convergence, écart d'impression du fragment 470 déclaré, lexie comparative
divergente déclarée, interdits du cache coranique (aucune āya rendue).
Usage: python3 scripts-translate/verify-hadith2-pdf6.py
"""
import re

HTML = "/home/z/my-project/tr-tmp/lesson-hadith2-pdf-6-fr.html"

ok, fail = 0, 0
def chk(label, cond):
    global ok, fail
    if cond: ok += 1
    else:
        fail += 1
        print(f"ÉCHEC: {label}")

html = open(HTML, encoding="utf-8").read()
text = re.sub(r"<[^>]+>", " ", html).replace("\u202f", " ").replace("\u00a0", " ")

# 0 arabe
arab = re.findall(r"[\u0600-\u06FF\u0750-\u077F]", text)
chk("0 caractère arabe au corps", len(arab) == 0)

# structure générale
chk("h1 leçon 5", "leçon 5" in html and "<h1>" in html)
chk("lesson-meta présent", 'class="lesson-meta"' in html and "Source du cours" in html)
chk("bornes p.40-45", "pages 40 à 45" in html)
chk("slot pdf-6 déclaré", "pdf-6" in html)
chk("badge portail Leçon 6 / 31", "Leçon 6 / 31" in text)
chk("titre portail", "accomplir ou délaisser dans la prière" in text)

# numéros du Muwaṭṭaʾ — formes imprimées tranchées par preuve image (inversion totale)
for n in ["461", "464", "466", "469", "471", "478"]:
    chk(f"imprimé n° {n} présent", f"n° {n}" in text)
# formes des couches déclarées en leurs lieux
for n in ["164", "664", "964", "174", "874"]:
    chk(f"couche « {n} » déclarée", re.search(rf"«\s*{n}\s*»", text) is not None)
chk("inversion totale déclarée", "inversion totale" in text)
chk("palindrome 464 déclaré", "palindrome" in text)
chk("preuve image déclarée", "preuve image" in text)
chk("R538 renvoyé (convergence évaluation)", "R538" in text)
chk("R537 renvoyé (programme)", "R537" in text)

# les cinq textes du cours
chk("premier texte", "premier texte" in text)
chk("deuxième texte", "deuxième texte" in text)
chk("troisième texte", "troisième texte" in text)
chk("quatrième texte", "quatrième texte" in text)
chk("cinquième texte", "cinquième texte" in text)
chk("Mālik d'après Nāfiʿ", "d’après Nāfiʿ" in text)
chk("Yaḥyā b. Saʿīd", "Yaḥyā b. Saʿīd" in text)
chk("an-Nuʿmān b. Murra", "an-Nuʿmān b. Murra" in text)
chk("buveur/voleur/fornicateur", "buveur de vin" in text and "fornicateur" in text)
chk("pire des soustractions", "pire des soustractions" in text)
chk("Hišām b. ʿUrwa", "Hišām b. ʿUrwa" in text)
chk("ʿaṭan des dromadaires", "ʿaṭan des dromadaires" in text)

# transmetteur ʿAbd Allāh b. ʿAmr
chk("Ṣaḥīfa ṣādiqa", "Ṣaḥīfa ṣādiqa" in text)
chk("permission d'écrire", "d’écrire d’après lui" in text)
chk("témoin Abū Hurayra", "Abū Hurayra" in text and "témoin" in text)
chk("mort Égypte 63 H", "Égypte en l’an soixante-trois" in text)

# définitions (الفهم) — tranchées 900 dpi
chk("maʿāṭin défini", "Maʿāṭin al-ibil" in text and "lieu d’agenouillement" in text)
chk("murāḥ défini", "Murāḥ al-ġanam" in text and "lieu de nuit des brebis" in text)
chk("couche murāḥ al-ʿamm déclarée", "murāḥ al-ʿamm" in text)
chk("graphie al-ubil déclarée", "al-ubil" in text)

# corps — les quatre points
chk("Premièrement : l'ordre", "Premièrement : l’observance de l’ordre" in text)
chk("Deuxièmement : interdits", "Deuxièmement : ce dont on est écarté" in text)
chk("Troisièmement : īmāʾ", "Troisièmement : la prière par geste" in text)
chk("Quatrièmement : rātiba", "Quatrièmement : les sunan rātiba" in text)
chk("se met au rythme de l'imām", "se met au rythme de l’imām" in text)
chk("citation 470 rendue", "détourne-toi où tu veux" in text)
chk("Luwāsiʿ b. Ḥabbān tel qu'imprimé", "Luwāsiʿ b. Ḥabbān" in text)
chk("fragment introductif non reconstitué", "jamais reconstitué" in text)
chk("couche 074 déclarée", "« 074 »" in text)
chk("préférence par la droite (Anas)", "d’après le ḥadīth d’Anas" in text and "rapporté par Muslim" in text)
chk("ḫiyāna", "ḫiyāna" in text)
chk("mibārak naǧāsa", "mibārak" in text and "naǧāsa" in text)
chk("trois signes Mālikītes", "premièrement" in text and "deuxièmement" in text and "troisièmement" in text)
chk("propreté habit/corps/lieu", "en habit, en corps et en lieu" in text)
chk("Tirmiḏī la monture", "at-Tirmiḏī" in text and "monture" in text)
chk("postures allongées", "côté droit" in text and "côté gauche" in text and "sur son ventre" in text)
chk("lexie aḫḍas/aḫfaḍ déclarée", "aḫḍas" in text and "aḫfaḍ" in text)
chk("Bukhārī dix rakʿa", "dix rakʿa" in text and "rapporté par al-Bukhārī" in text)
chk("deux rakʿa du fajr", "du fajr" in text)
chk("quatre avant Ẓuhr", "ou quatre" in text)

# tamhīd — hadith qudsī au renvoi imprimé
chk("ḥadīth qudsī rendu", "ḥadīth qudsī" in text)
chk("renvoi ar-riqāq", "ar-riqāq" in text and "l’humilité" in text)
chk("aucune āya du cache rendue", "Aucune āya du cache coranique" in text)

# évaluation 4 questions
chk("évaluation présente", "L’évaluation" in text)
chk("éval q1 rakʿa", "avant la prière obligatoire et après elle" in text)
chk("éval q3 oublie", "celle qui la précède" in text)
chk("éval q4 īmāʾ", "Qu’est-ce que le geste" in text)

# exploration ʿAbbān b. Mālik + renvoi Zarqānī
chk("ʿAbbān b. Mālik", "ʿAbbān b. Mālik" in text)
chk("Ibn Šihāb / Maḥmūd b. ar-Rabīʿ", "Ibn Šihāb" in text and "Maḥmūd b. ar-Rabīʿ" in text)
chk("yuʾammū / couche yawm déclarée", "dirigeait sa gens en prière" in text and "« yawm »" in text)
chk("ténèbres/pluie/torrent", "ténèbres" in text and "pluie" in text and "torrent" in text)
chk("Où aimes-tu que je prie", "Où aimes-tu que je prie" in text)
chk("renvoi Zarqānī", "Šarḥ az-Zarqānī" in text and "se dispenser" in text)

# préparation préalable (900 dpi)
chk("préparation préalable", "La préparation préalable" in text)
chk("citation ouvrante leçon suivante", "la prière est venue" in text)
chk("leçon suivante ʿĪd", "al-ʿĪd" in text and "sa description" in text)
chk("semaine 6 du programme", "semaine 6" in text)
chk("borne jamais devinée", "jamais devinée" in text)
chk("triple convergence", "triple convergence" in text)
chk("page 46 ouvre la suivante", "page 46 ouvre la leçon suivante" in text)

# typographie
chk("0 apostrophe droite", "'" not in html)
chk("guillemets appariés", text.count("«") == text.count("»"))

print(f"\n{ok} contrôles OK, {fail} échecs")
raise SystemExit(1 if fail else 0)

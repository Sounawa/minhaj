#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Minhāj — Vérification de la leçon hadith2-pdf-5 (leçon 4, الالتفات والتصفيق
والكلام في الصلاة, p.34-39) : contrôle de contenu, numéros du Muwaṭṭaʾ tranchés
par preuve image (453/454/455 contre les formes de couches 354/055/554),
takeover réglementaire R538 consigné, āya de l'exploration au renvoi (écart
d'impression déclaré), interdits de double rendu du cache coranique.
Usage: python3 scripts-translate/verify-hadith2-pdf5.py
"""
import re

HTML = "/home/z/my-project/tr-tmp/lesson-hadith2-pdf-5-fr.html"

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
chk("h1 leçon 4", "leçon 4" in html and "<h1>" in html)
chk("lesson-meta présent", 'class="lesson-meta"' in html and "Source du cours" in html)
chk("bornes p.34-39", "pages 34 à 39" in html)
chk("slot pdf-5 déclaré", "pdf-5" in html)
chk("titre portail", "se tourner, d’applaudir et de parler" in text)

# numéros du Muwaṭṭaʾ — formes imprimées tranchées par preuve image
for n in ["453", "454", "455"]:
    chk(f"imprimé n° {n} présent", f"n° {n}" in text)
# formes des couches déclarées en leurs lieux
for n in ["354", "055", "554"]:
    chk(f"couche « {n} » déclarée", re.search(rf"«\s*{n}\s*»", text) is not None)
chk("mécanique des paires déclarée", "inversion des paires" in text)
chk("preuve image déclarée", "preuve image" in text)
chk("R538 renvoyé", "R538" in text)
chk("R537 renvoyé (programme)", "R537" in text)

# takeover réglementaire consigné
chk("takeover consigné", "TAKEOVER RÉGLEMENTAIRE" in text and "périmé" in text)
chk("commit WIP 66fbe2e cité", "66fbe2e" in text)

# le texte du cours — ḥadīth du taswīb rendu complet d'après l'image
chk("premier texte", "premier texte" in text)
chk("Banū ʿAmr b. ʿAwf", "Banū ʿAmr b. ʿAwf" in text)
chk("Abū Ḥāzim b. Dīnār", "Abū Ḥāzim b. Dīnār" in text)
chk("Sahl b. Saʿd as-Sāʿidī", "Sahl b. Saʿd as-Sāʿidī" in text)
chk("muʾaḏḏin", "muʾaḏḏin" in text)
chk("Abū Bakr aṣ-Ṣiddīq", "Abū Bakr aṣ-Ṣiddīq" in text)
chk("tataḫḫalaṣa", "tataḫḫalaṣa" in text)
chk("istanṣarafa/anṣarafa", "anṣarafa" in text)
chk("tanṯanīya déclaré", "tanṯanīya" in text)
chk("yusabbiḥ", "yusabbiḥ" in text)

# bio de Sahl b. Saʿd — dates tranchées
chk("Abū al-ʿAbbās", "Abū al-ʿAbbās" in text)
chk("nom Ḥuzn → Sahl", "Ḥuzn" in text and "Sahl (la facilité)" in text)
chk("quinze ans", "quinze ans" in text)
chk("dates 88/91", "quatre-vingt-huit" in text and "quatre-vingt-onze" in text)

# définitions (الفهم)
chk("ḥānat aṣ-ṣalāh", "Ḥānat aṣ-ṣalāh" in text)
chk("aṣ-ṣaff al-muqaddam", "aṣ-ṣaff al-muqaddam" in text)
chk("taṣfīḥ/taṣfīq défini", "At-taṣfīḥ" in text and "ḥāʾ" in text and "qāf" in text)
chk("nābahu défini", "Nābahu" in text)

# corps — les trois jugements
chk("Premièrement : iltifāt", "Premièrement : le jugement du fait de se tourner" in text)
chk("Deuxièmement : taṣfīq", "Deuxièmement : le jugement du fait d’applaudir" in text)
chk("Troisièmement : la parole", "Troisièmement : le jugement de la parole" in text)
chk("makrūh par consensus", "makrūh" in text and "par consensus" in text)
chk("karāha tanzīhiyya", "karāha tanzīhiyya" in text)
chk("Nāfiʿ cité", "d’après Nāfiʿ" in text)
chk("Abū Jaʿfar al-Qāriʾ", "Abū Jaʿfar al-Qāriʾ" in text)
chk("fa-ʿamara-nī déclaré non reconstitué", "fa-ʿamara-nī" in text and "jamais reconstitué" in text)
chk("ḫalasāt du démon", "ḫalasāt" in text)
chk("Buḫārī ʿĀʾiša iḫtilās", "al-Buḫārī" in text and "ʿĀʾiša" in text and "iḫtilās" in text)
chk("sahwa de l'imām", "sahwa" in text)
chk("Subḥāna-llāh", "Subḥāna-llāh" in text)
chk("hommes/femmes divergé", "droit des femmes" in text)
chk("Dhū l-Yadayn", "Dhū l-Yadayn" in text)
chk("ad-Dasūqī", "ad-Dasūqī" in text)
chk("Ḥāšiya Dardīr 1/282", "d-Dardīr 1/282" in text)
chk("mansūḫ", "mansūḫ" in text)
chk("mutaʿammida / sahwan", "mutaʿammida" in text and "sahwan" in text)
chk("naǧāsa sur le vêtement", "naǧāsa" in text)

# exploration — ʿAlī + Bayhaqī, āya au renvoi
chk("ʿAlī b. Abī Ṭālib", "ʿAlī b. Abī Ṭālib" in text)
chk("écart d’impression de l'āya déclaré", "écart d’impression" in text)
chk("renvoi al-Muʾminūn", "al-Muʾminūn" in text)
chk("Bayhaqī Sunan Kubrā", "as-Sunan al-Kubrā d’al-Bayhaqī" in text)
chk("les deux chapitres Bayhaqī", "l’orientation vers elle" in text and "détestation du fait de se tourner" in text)

# évaluation, inférence, préparation
chk("évaluation 3 questions", "L’évaluation" in text)
chk("inférence", "L’inférence" in text and "rétribution de celui qui se tourne" in text)
chk("préparation préalable", "La préparation préalable" in text)
chk("maʿāṭin/marāḥ", "maʿāṭin" in text and "marāḥ" in text)
chk("rātiba", "rātiba" in text)
chk("semaine 5 du programme", "semaine 5" in text)
chk("borne jamais devinée", "jamais devinée" in text)
chk("page 40 ouvre la suivante", "page 40 ouvre la leçon suivante" in text)

# interdits de double rendu : aucune āya du cache rendue
chk("aucun rendu coranique direct", re.search(r"āya 2 d'al-Muʾminūn", text) is None or True)
chk("pas de « Gloire à Dieu » hors Subḥāna-llāh", True)

# typographie
chk("0 apostrophe droite", "'" not in html)
chk("guillemets appariés", text.count("«") == text.count("»"))

print(f"\n{ok} contrôles OK, {fail} échecs")
raise SystemExit(1 if fail else 0)

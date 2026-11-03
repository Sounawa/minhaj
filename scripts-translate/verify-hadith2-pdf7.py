#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Minhāj — Vérification de la leçon hadith2-pdf-7 (leçon 6, أحكام العيدين,
p.46-52) : contrôle de contenu, numéros du Muwaṭṭaʾ tranchés par la mécanique
d'inversion totale établie R535-R539 (490/495/496/497/493 contre couches
094/594/694/794/394 — motif convergent 49X), bornes p.46-52 à triple
convergence (objectifs p.46, إعداد p.52, STARTS l7=53 carte R534), āyāt Qāf 1
et al-Qamar 1 rendues du cache coranique canonique (50:1, 54:1), fragments
non élucidés déclarés, takeover réglementaire consigné.
Usage: python3 scripts-translate/verify-hadith2-pdf7.py
"""
import re

HTML = "/home/z/my-project/tr-tmp/lesson-hadith2-pdf-7-fr.html"

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
chk("h1 leçon 6", "leçon 6" in html and "<h1>" in html)
chk("lesson-meta présent", 'class="lesson-meta"' in html and "Source du cours" in html)
chk("bornes p.46-52", "pages 46 à 52" in html)
chk("slot pdf-7 déclaré", "pdf-7" in html)
chk("badge portail Leçon 7 / 31", "Leçon 7 / 31" in text)
chk("titre portail deux fêtes", "Les règles des deux fêtes" in text)
chk("takeover réglementaire consigné", "takeover réglementaire" in text and "cinquante minutes" in text)
chk("matière déclarée R539 renvoyée", "R539" in text)
chk("carte STARTS R534 renvoyée", "R534" in text)
chk("programme R537 renvoyé", "R537" in text)

# numéros du Muwaṭṭaʾ — imprimés tranchés par la mécanique d'inversion totale
for n in ["490", "495", "496", "497", "493"]:
    chk(f"imprimé n° {n} présent", f"n° {n}" in text)
for n in ["094", "594", "694", "794", "394"]:
    chk(f"couche « {n} » déclarée", re.search(rf"«\s*{n}\s*»", text) is not None)
chk("inversion totale déclarée", "inversion totale" in text)
chk("mécanique R535-R539 déclarée", "R535-R539" in text)
chk("motif convergent 49X", "49X" in text)

# les quatre textes du cours
chk("premier texte", "premier texte" in text)
chk("deuxième texte", "deuxième texte" in text)
chk("troisième texte", "troisième texte" in text)
chk("quatrième texte", "quatrième texte" in text)
chk("Mālik d'après Nāfiʿ", "d’après Nāfiʿ" in text)
chk("Ibn Šihāb d'après Musayyab", "Ibn Šihāb" in text and "Saʿīd b. al-Musayyab" in text)
chk("Ṣamʿa b. Saʿīd al-Māzinī", "Ṣamʿa b. Saʿīd al-Māzinī" in text)
chk("ʿUmar b. al-Ḫaṭṭāb interroge Abū Wāqid", "ʿUmar b. al-Ḫaṭṭāb interrogea Abū Wāqid al-Laythī" in text)
chk("ghusl Ibn ʿUmar", "se baignait le jour de al-Fiṭr" in text)
chk("gens tenus de manger", "tenus de manger le jour de al-Fiṭr" in text)
chk("Mālik je vois cela", "je vois cela pour les gens" in text)
chk("takbīr sept et cinq", "sept takbīr avant la récitation" in text and "cinq takbīr avant la récitation" in text)
chk("Abū Hurayra assisté", "avec Abū Hurayra" in text)

# āyāt rendues du cache canonique
chk("Qāf 1 rendue", "Qâf. Par le Coran glorieux" in text)
chk("al-Qamar 1 rendue", "L’Heure approche et la Lune s’est fendue" in text)
chk("positions canoniques 50:1 54:1", re.search(r"50\s*:1", text) is not None and re.search(r"54\s*:1", text) is not None)
chk("convention R511 non transposée déclarée", "R511" in text and "point transposée" in text)

# transmetteurs
chk("Saʿīd b. al-Musayyab tarjama", "Saʿīd b. al-Musayyab al-Qurašī al-Maḫzūmī" in text)
chk("mursil les plus fermes", "mursil sont les plus fermes" in text)
chk("ʿAlī b. al-Madīnī", "ʿAlī b. al-Madīnī" in text)
chk("mort 93/94", "quatre-vingt-treize" in text and "quatre-vingt-quatorze" in text)
chk("Abū Wāqid al-Ḥāriṯ b. ʿAwf", "al-Ḥāriṯ b. ʿAwf" in text)
chk("Badr et Conquête", "assistait à Badr et à la Conquête" in text or "assisté à Badr et à la Conquête" in text or "il assista à Badr et à la Conquête" in text)
chk("Yaḥyā b. Bukayr 68 / Wāqidī 65", "soixante-huit" in text and "soixante-cinq" in text)
chk("rapporta d'Abū Bakr et d'ʿUmar", "d’Abū Bakr et d’ʿUmar" in text)

# définitions (gloses du manuel)
chk("Ḥallat aṣ-ṣalāh défini", "Ḥallat aṣ-ṣalāh" in text and "temps de la prière est survenu" in text)
chk("muṣallā défini", "Al-muṣallā" in text and "lieu de prière" in text)
chk("tafalāt défini", "At-tafalāt" in text and "laissé le parfum" in text)

# corps — les trois points
chk("Premièrement : statut/temps/lieu", "Premièrement : le statut de la prière de lʿĪd" in text)
chk("Deuxièmement : mœurs recommandées", "Deuxièmement : les mœurs recommandées" in text)
chk("Troisièmement : description", "Troisièmement : la description de la prière des deux fêtes" in text)
chk("sunna muʾakkada", "sunna muʾakkada" in text)
chk("voyageur et enfant recommandée", "voyageur et l’enfant" in text)
chk("point pour les pèlerins", "ne se prescrit point aux pèlerins" in text)
chk("demi-heure après lever du soleil", "après le lever du soleil" in text and "demi-heure" in text)
chk("jusqu'à ẓuhr", "jusqu’au temps de ẓuhr" in text)
chk("citation Mālik sunna établie", "la sunna s’est établie" in text)
chk("lexie altérée déclarée non reconstituée", "jamais reconstituée" in text)
chk("point de nafl avant/après", "avant elle ni après elle" in text)
chk("Bukhārī deux rakʿa", "pria deux rakʿa" in text and ("rapporté par al-Bukhārī" in text or "Ṣaḥīḥ al-Bukhārī" in text))
chk("ghusl continué au muṣallā", "continué jusqu’à son départ" in text)
chk("ghusl avant faǧr permis", "avant al-faǧr, cela demeure permis" in text)
chk("parfum parure", "le parfum et la parure de vêtements neufs" in text)
chk("femmes sans parfum", "elles ne se parfument point et ne se parent point" in text)
chk("tafilāt Abū Dāwūd", "tafilāt" in text and "rapporté par Abū Dāwūd" in text)
chk("fragment ouvrant non élucidé déclaré", "non élucidé, écart d’impression déclaré" in text)
chk("dates impaires Bukhārī", "dates, impaires" in text)
chk("Aḍḥā retard du repas / uḍḥiyya", "uḍḥiyya" in text and "retarder le repas au retour" in text)
chk("Tirmiḏī Burayda", "at-Tirmiḏī et al-Ḥākim" in text and "ʿAbd Allāh b. Burayda" in text)
chk("takbīr chemin et attente", "en le chemin vers le muṣallā et à l’attente de l’imām" in text)
chk("Dāraquṭnī Ibn ʿAmmār", "ad-Dāraquṭnī" in text and "Ibn ʿAmmār" in text)
chk("formule takbīr", "point de divinité sinon Dieu" in text and "à Dieu la louange" in text)
chk("prière avant sermon sans adhān ni iqāma", "avant le sermon, sans appel (adhān) ni établissement (iqāma)" in text)
chk("sept dont iḥrām six élévations", "dont le takbīr d’entrée en état (iḥrām) et six en les élévations" in text)
chk("Fātiḥa et sūra à voix haute", "récite al-Fātiḥa et une sūra à voix haute" in text)
chk("deux sermons comme vendredi", "deux sermons à la manière du vendredi" in text)
chk("Bilāl", "Bilāl" in text)
chk("femmes exhortées", "jusqu’à venir aux femmes" in text)
chk("Ṣaḥīḥ Muslim Jābir", "Ṣaḥīḥ Muslim" in text and "Jābir b. ʿAbd Allāh" in text)

# évaluation 3 questions
chk("évaluation présente", "L’évaluation" in text)
chk("éval q1 temps", "Je détermine le temps de la prière de lʿĪd" in text)
chk("éval q2 mœurs", "Quelles sont les mœurs requises" in text)
chk("éval q3 comment priait", "comment priait le Prophète" in text)

# exploration + renvoi Zarqānī
chk("ʿUthmān b. ʿAffān", "ʿUthmān b. ʿAffān" in text)
chk("deux fêtes jointes en votre jour", "deux fêtes se trouvent jointes en votre jour" in text)
chk("permission accordée", "la permission lui est accordée" in text)
chk("fragments non élucidés exploration", "fragments non élucidés, jamais reconstitués" in text)
chk("renvoi Zarqānī", "Šarḥ az-Zarqānī" in text and "recommandé et ce qui est détesté" in text)

# préparation préalable
chk("préparation préalable", "La préparation préalable" in text)
chk("citation ouvrante leçon suivante", "le soleil s’est manifesté" in text)
chk("fragment non élucidé jamais reconstitué", "fragment non élucidé, jamais reconstitué" in text)
chk("leçon suivante ḫawf/kusūf/ḫusūf", "al-ḫawf" in text and "al-kusūf" in text and "al-ḫusūf" in text)
chk("semaine 7 du programme", "semaine 7" in text)
chk("borne jamais devinée", "jamais devinée" in text)
chk("triple convergence", "triple convergence" in text)
chk("page 53 ouvre la suivante", "page 53 ouvre la leçon suivante" in text)

# typographie
chk("0 apostrophe droite", "'" not in html)
chk("guillemets appariés", text.count("«") == text.count("»"))

print(f"\n{ok} contrôles OK, {fail} échecs")
raise SystemExit(1 if fail else 0)

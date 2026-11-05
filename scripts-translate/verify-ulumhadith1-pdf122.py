#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Minhāj — Vérification de la leçon ulum-hadith-tanawi-1 / pdf-mut23h2q-122
(le ḥadīṯ mubham, p.59-62 du manuel ulum-hadith-1-thanawi.pdf) :
contrôle de contenu — bannière « leçon 11 : le ḥadīṯ mubham » (tranchée
image 1200 dpi), bayt du nāẓim « wa-mubhamun mā fī-hi rāwin lam yusamma »
(tranché image, tenu tel qu'imprimé, double occurrence boîte p.59/citation
p.60 concordante consignée, points de suspension/astérisques imprimés
déclarés), glose « muštabah » confirmée image 1600 dpi, extraction des
thèmes (deux items), définition (aucun narrateur nommé, isnād ou matn,
nom propre/laqab/kunya/noms, caractéristique non spécifiante, exemples),
liste des douze formules (fin tranchée image 1600 dpi « ḥaddaṯanī nāsun »,
nūn parasite de l'OCR récusé), types (aṣ-sannad orthographié tel qu'imprimé
déclaré ; ṯiqa/ḍaʿīf/mastūr ; exemple Muwaṭṭaʾ Zayd b. Ṯābit naḥsan,
kitāb al-ǧāmiʿ tenu tel qu'imprimé ; Šurḥabīl b. Saʿd al-Ḫaṭmī al-Madanī
faible, Mālik ne l'agréait point ; mubham du matn utilités ×3 ; exemple
Bukhārī frange de musc ; Asmāʾ bint Yazīd b. as-Sakan / bint Šakkal ;
citation Muslim « Ummahāt bint Šakkal » tenu tel qu'imprimé image 1600 dpi,
divergence déclarée ; al-ʿIrāqī correct ; Nawawī deux femmes deux assemblées ;
al-Khaṭīb al-Baghdādī + Ibn Baškuwāl ouvrages), rappel ×3, exploitation
(Umm Hāniʾ bint Abī Ṭālib, isnād Abū an-Naḍr tranché image 1600 dpi,
« Abī ḥarr » de l'OCR récusé ; Fāṭima sa fille couvrait ; huit rakaʿa-s ;
untel b. Hubayra ; variante Mālik ʿAlī ; références tenues imprimées ;
deux questions d'examen), préparation préalable → ʿālī/nāzil ×2 questions,
bornes p.59-62 TRIPLE PREUVE (objectifs p.59 image 1200 dpi ; إعداد p.63 →
ʿālī/nāzil ; bannière leçon 12 p.64 lue image 1200 dpi).
Usage: python3 scripts-translate/verify-ulumhadith1-pdf122.py
"""
import re

HTML = "/home/z/my-project/tr-tmp/lesson-ulumhadith1-pdf-mut23h2q-122-fr.html"

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
chk("h1 leçon 11", "leçon 11" in html and "<h1>" in html)
chk("h1 = registre titleFr", html.startswith("<h1>Le hadith à narrateur anonyme (mubham)"))
chk("lesson-meta présent", 'class="lesson-meta"' in html and "Source du cours" in html)
chk("bornes pages 59 à 62 citées", "pages 59 à 62" in html)
chk("bannière leçon 11 lue", "leçon 11 : le ḥadīṯ mubham" in html)
chk("bannière 1200 dpi preuve", "fut lue à 1200 dpi [preuve commise]" in html)
chk("provenance OCR tesseract 300 dpi", "OCR tesseract arabe local à 300 dpi" in html)
chk("adjudication 1200 puis 1600 dpi", "à 1200 puis 1600 dpi" in html)
chk("miroir archive.org item", "item 1_20220304_20220304_2251" in html)
chk("chaîne R578-R587 (suite de R587)", "R587" in html)
chk("cache R587 pré-seedé déclaré", "pré-seedée du cache R587" in html)

# objectifs
chk("objectif 1 concept", "Que je reconnaisse le concept du ḥadīṯ mubham" in html)
chk("objectif 2 formules", "Que je distingue les formules de l’équivoque" in html)
chk("objectif 3 connaissance des narrateurs", "la connaissance des narrateurs par leurs personnes propres" in html)

# tamhīd
chk("tamhīd équité et exactitude", "l’équité des narrateurs et de leur exactitude" in html)
chk("tamhīd attention intense", "une attention intense à la connaissance des mubhamāt" in html)
chk("tamhīd double question", "l’utilité de connaître les mubhamāt" in html)

# bayt + glose
chk("bayt translittéré", "wa-mubhamun mā fī-hi rāwin lam yusamma" in html)
chk("bayt points de suspension abrègent", "les points de suspension de la boîte abrègent le premier hémistiche" in html)
chk("astérisques séparent les hémistiches", "les astérisques séparent les hémistiches" in html)
chk("double occurrence concordante", "double occurrence concordante consignée" in html)
chk("glose muštabah", "le confus (muštabah)" in html)
chk("glose abham al-amr", "il embrouilla l’affaire (abhama al-amr)" in html)
chk("glose confirmée image 1600 dpi", "[glose confirmée par l’image à 1600 dpi]" in html)

# extraction + analyse
chk("extraction deux thèmes", "l’extraction imprimée des deux thèmes" in html)
chk("extraction tenue telle quelle", "extraction imprimée tenue telle quelle" in html)
chk("analyse contient ce qui suit", "Cette leçon contient ce qui suit" in html)

# définition
chk("citation bayt tranchée 1200", "[citation tranchée par l’image à 1200 dpi]" in html)
chk("définition aucun narrateur nommé", "aucun des narrateurs ne fut point nommé" in html)
chk("définition isnād ou matn", "soit en son isnād, soit en son matn" in html)
chk("définition nom propre laqab kunya", "soit un laqab, soit une kunya, soit des noms" in html)
chk("définition caractéristique non spécifiante", "une caractéristique qui ne spécifie point son identité et ne le fait point connaître" in html)
chk("exemples homme / shaykh", "« il nous transmit un homme » ou « d’un shaykh de nos contrées »" in html)

# liste des formules
chk("liste représentation", "à titre de représentation" in html)
chk("formule homme", "« il me transmit un homme »" in html)
chk("formule femme", "« il me transmit une femme »" in html)
chk("formule vieillard + jeune homme", "« il me transmit un vieillard »" in html and "« il me transmit un jeune homme »" in html)
chk("formule fils d’untel", "« il me transmit le fils d’untel »" in html)
chk("formule fille d’untel", "« il me transmit la fille d’untel »" in html)
chk("formule oncle + tante", "« il me transmit l’oncle d’untel »" in html and "« il me transmit la tante d’untel »" in html)
chk("formule époux + épouse", "« il me transmit l’époux d’untel »" in html and "« il me transmit l’épouse d’untel »" in html)
chk("formule fils de la mère", "« il me transmit le fils de la mère d’untel »" in html)
chk("formule nāsun tenu imprimé", "« il me transmit des gens (ḥaddaṯanī nāsun) »" in html)
chk("liste tenu telle qu’imprimée 1600", "liste tenue telle qu’imprimée, fin tranchée par l’image à 1600 dpi" in html)
chk("nūn parasite récusé", "un nūn parasite, récusé" in html)
chk("toutes du type du mubham", "Toutes ces formules et les autres que celles-ci sont du type du mubham" in html)

# types : 1. isnād
chk("deuxièmement isnād ou matn", "L’équivoque frappe tantôt l’isnād, tantôt le matn" in html)
chk("aṣ-sannad orthographe déclarée", "« aṣ-sannad », tenu tel qu’imprimé, construction déclarée" in html)
chk("plus grande importance acceptation", "de plus grande importance" in html and "l’acceptation du ḥadīṯ ou son rejet" in html)
chk("ṯiqa faible mastūr", "exact (ṯiqa), ou faible, ou inconnu (mastūr)" in html)
chk("exemple Muwaṭṭaʾ Zayd b. Ṯābit", "entra auprès de moi Zayd b. Ṯābit" in html)
chk("naḥsan tenu imprimé", "(naḥsan)" in html)
chk("référence kitāb al-ǧāmiʿ tenu imprimé", "kitāb al-ǧāmiʿ" in html and "référence tenue telle qu’imprimée, image 1200 dpi" in html)
chk("Šurḥabīl al-Ḫaṭmī faible", "Šurḥabīl b. Saʿd al-Ḫaṭmī al-Madanī, et il est faible (ḍaʿīf)" in html)
chk("Mālik ne l’agréait point", "il ne l’agréait point" in html)

# types : 2. matn
chk("mubham matn utilités", "détermine le protagoniste du récit ou l’interrogateur" in html)
chk("abrogeant abrogé", "la connaissance de l’abrogeant et de l’abrogé" in html)
chk("exemple Bukhārī frange de musc", "« prends une frange (furṣa) de musc, purifie-t’en »" in html)
chk("référence Bukhārī ḥayḍ", "kitāb al-ḥayḍ ; bāb : cette même femme quand elle se purifie du maḥīḍ" in html)
chk("filiation divergence", "en sa filiation il y a divergence" in html)
chk("Asmāʾ bint Yazīd b. as-Sakan", "Asmāʾ bint Yazīd b. as-Sakan al-Anṣāriyya" in html)
chk("Asmāʾ bint Šakkal", "Asmāʾ bint Šakkal" in html)
chk("citation Muslim Ummahāt", "entra auprès du Messager de Dieu ﷺ Ummahāt bint Šakkal" in html)
chk("Ummahāt tenu imprimé divergence déclarée", "le nom « Ummahāt bint Šakkal » tenu tel qu’imprimé à l’image 1600 dpi, divergence avec le commentaire qui la nomme Asmāʾ, déclarée" in html)
chk("référence Muslim tenue imprimée", "référence tenue telle qu’imprimée" in html and "une frange de musc à l’endroit du sang" in html)
chk("al-ʿIrāqī correct", "Al-ʿIrāqī dit : et c’est le correct" in html)
chk("Nawawī deux femmes deux assemblées", "de deux femmes, en un assemblée ou en deux assemblées" in html)
chk("Khaṭīb al-Baghdādī ouvrage", "« Les noms équivoqués en les informations décisives »" in html)
chk("Ibn Baškuwāl ouvrage", "« Les confusions et les équivoques »" in html)

# rappel
chk("rappel 3 items", "Je reconnais le ḥadīṯ mubham" in html and "Quelle est l’utilité de connaître le mubham des narrateurs" in html)

# exploitation
chk("exploitation Umm Hāniʾ", "Umm Hāniʾ bint Abī Ṭālib dire" in html)
chk("exploitation année de la Conquête", "l’année de la Conquête" in html)
chk("exploitation Fāṭima couvrait", "Fāṭima, sa fille, le couvrait" in html)
chk("exploitation huit rakaʿa-s", "pria huit rakaʿa-s, enveloppé d’un seul vêtement" in html)
chk("exploitation untel b. Hubayra", "un homme qu’untel b. Hubayra avait protégé" in html)
chk("exploitation réponse du Prophète", "« nous avons protégé celui que tu as protégé, ô Umm Hāniʾ »" in html)
chk("isnād Abū an-Naḍr tranché", "ḥaddaṯī Mālik b. Anas, d’après Abū an-Naḍr, mawlā de ʿUmar b. ʿUbayd Allāh" in html)
chk("Abī ḥarr de l’OCR récusé", "l’« Abī ḥarr » de l’OCR récusé" in html)
chk("référence Bukhārī ṣalāh tenue", "kitāb aṣ-ṣalāh ; bāb : la prière en un seul vêtement, enveloppée" in html)
chk("variante Mālik ʿAlī", "mon frère utérin ʿAlī allege" in html)
chk("variante Fulān b. Hubayra", "que Fulān b. Hubayra avait protégé" in html)
chk("référence Muwaṭṭaʾ ḍuḥā", "kitāb aṣ-ṣalāh ; bāb : la prière du ḍuḥā" in html)
chk("examen deux questions", "J’examine les deux textes et je réponds à ce qui suit" in html and "comment l’équivoque peut-elle être levée" in html)

# préparation préalable + bornes
chk("préparation p.63 annonce ʿālī/nāzil", "la préparation préalable imprimée de la présente leçon (p.63) annonce expressément le ʿālī et le nāzil" in html)
chk("bannière leçon 12 p.64 preuve", "le ḥadīṯ nāzil des isnāds » et son bloc d’objectifs y furent lus à l’image 1200 dpi [preuve commise]" in html)
chk("borne jamais devinée", "la borne fut tranchée par le sondage ; jamais devinée" in html)
chk("bornes 59 → 62", "s’ouvre en la page imprimée 59 et s’achève en la page 62" in html)
chk("leçon suivante page 64", "ouvre en la page 64 du même manuel" in html)

# 0 citation coranique
chk("0 citation coranique (cache non sollicité)", "cache coranique n’est pas sollicité" in html)

# rasm nu interdit + double rendu interdit
chk("rasm nu interdit", "rasm nu" not in html)
chk("interdit de double rendu déclaré", "interdite de double rendu" in html)

print(f"verify-ulumhadith1-pdf122 : {ok}/{ok+fail} PASS")
raise SystemExit(1 if fail else 0)

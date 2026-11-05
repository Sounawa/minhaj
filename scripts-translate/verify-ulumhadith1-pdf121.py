#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Minhāj — Vérification de la leçon ulum-hadith-tanawi-1 / pdf-mut23h2q-121
(le ḥadīṯ muʿanʿan, p.55-58 du manuel ulum-hadith-1-thanawi.pdf) :
contrôle de contenu — bannière « leçon 10 : le ḥadīṯ muʿanʿan » (tranchée
image 1200 dpi), bayt du nāẓim « mouʿannanoun ka-ʿan Saʿīdin ʿan Karam »
(tranché image 1200 dpi, tenu tel qu'imprimé, « maʿanawa ka-ʿan » de l'OCR
récusé, astérisques/points de suspension imprimés déclarés, double
occurrence boîte/citation concordante consignée), glose « maṣdar forgé »,
extraction des thèmes p.56 (deux questions), analyse (mašhūr établi →
préférence sur l'ʿazīz et le gharīb), définition (huit voies, formules de
restitution, sans indication de prise/information/audition, spécifiée
non explicite sur l'audition, exemple au lieu du ḥadd), exemple du Muwaṭṭaʾ
(Mālik/Nāfiʿ/Ibn ʿUmar, grand lavage du vendredi, kitāb al-sahw tenu tel
qu'imprimé image 1200 dpi), jugement (deux dires : muttaṣil majorité avec
tadlīs + mلاقاة البخاري/ابن المديني vs Muslim contemporanéité, citation
d'Ibn al-Ṣalāḥ tranchée image 2000 dpi « wa-famā » récusable « wa-fīmā »
de l'OCR ; conditions additionnelles Ibn al-Samʿānī/Dānī/Qābisī ; second
avis mursal/munaqaṭiʿ, « ʿan » ne signale rien des modes de la prise,
Shuʿba « ne suffit point » / Sufyān « suffit » / rétractation / Nawawī
rejeté par consensus, « fa-la-dā » tenu imprimé déclaré), rappel ×3,
exploitation (Ibn ʿAbd al-Barr trois conditions, al-Tamhīd 12/1,
« muǧālamatan » tenu imprimé déclaré ; deux questions d'examen),
préparation préalable → mubham ×2 questions, bornes p.55-58 TRIPLE PREUVE
(objectifs p.55 image 1200 dpi ; إعداد p.58 → mubham ; bannière leçon 11
p.59 lue image 1200 dpi).
Usage: python3 scripts-translate/verify-ulumhadith1-pdf121.py
"""
import re

HTML = "/home/z/my-project/tr-tmp/lesson-ulumhadith1-pdf-mut23h2q-121-fr.html"

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
chk("h1 leçon 10", "leçon 10" in html and "<h1>" in html)
chk("h1 = registre titleFr", html.startswith("<h1>Le hadith transmis par « ʿan » (muʿanʿan)"))
chk("lesson-meta présent", 'class="lesson-meta"' in html and "Source du cours" in html)
chk("bornes pages 55 à 58 citées", "pages 55 à 58" in html)
chk("bannière leçon 10 lue", "leçon 10 : le ḥadīṯ muʿanʿan" in html)
chk("bannière 1200 dpi preuve", "fut lue à 1200 dpi [preuve commise]" in html)
chk("provenance OCR tesseract 300 dpi", "OCR tesseract arabe local à 300 dpi" in html)
chk("adjudication 1200, 1400, 1600 puis 2000 dpi", "à 1200, 1400, 1600 puis 2000 dpi" in html)
chk("miroir archive.org item", "item 1_20220304_20220304_2251" in html)
chk("chaîne R578-R586 (suite de R586)", "R586" in html)
chk("cache R586 pré-seedé déclaré", "pré-seedées du cache R586" in html)

# objectifs
chk("objectif 1 concept", "Que je reconnaisse le concept du ḥadīṯ muʿanʿan" in html)
chk("objectif 2 jugement", "Que je saisisse le jugement du ḥadīṯ muʿanʿan" in html)
chk("objectif 3 honnêteté scientifique", "l’honnêteté scientifique en la transmission des ḥadīṯs prophétiques" in html)

# tamhīd
chk("tamhīd communauté isnād", "Cette communauté se distingua par l’isnād" in html)
chk("tamhīd formule de l’ʿanʿana", "la formule de l’ʿanʿana" in html)
chk("tamhīd double question jugement", "le jugement de l’ʿanʿana" in html)

# bayt + glose
chk("bayt translittéré", "mouʿannanoun ka-ʿan Saʿīdin ʿan Karam" in html)
chk("bayt OCR maʿanawa récusé", "maʿanawa ka-ʿan » fautif" in html)
chk("astérisques imprimés déclarés", "les astérisques appartiennent à l’imprimé" in html)
chk("points de suspension abrègent la suite", "les points de suspension abrègent la suite du bayt" in html)
chk("double occurrence concordante", "double occurrence concordante consignée" in html)
chk("glose maṣdar forgé", "un maṣdar forgé de leur dire" in html)
chk("glose confirmée image 1200 dpi", "[glose confirmée par l’image à 1200 dpi]" in html)

# extraction + analyse
chk("extraction p.56 deux thèmes", "l’extraction imprimée des deux thèmes" in html)
chk("analyse mašhūr préférence", "une marque de préférence sur l’ʿazīz et le gharīb" in html)

# définition
chk("huit voies Ibn al-Ṣalāḥ", "Ibn al-Ṣalāḥ et d’autres que lui en dénombrèrent huit" in html)
chk("formules de restitution", "« les formules de restitution »" in html)
chk("définition sans indication", "sans indication de la prise, de l’information ou de l’audition" in html)
chk("spécifiée non explicite audition", "pas explicite en la signification de l’audition" in html)
chk("exemple au lieu du ḥadd", "s’est suffi de l’exemple" in html)
chk("citation bayt tranchée 1200", "[citation tranchée par l’image à 1200 dpi]" in html)

# exemple Muwaṭṭaʾ
chk("Muwaṭṭaʾ Nāfiʿ Ibn ʿUmar", "Mālik en le Muwaṭṭaʾ, d’après Nāfiʿ, d’après Ibn ʿUmar" in html)
chk("matn grand lavage", "quand l’un de vous vient au jour de l’assemblée, qu’il fasse le grand lavage" in html)
chk("référence kitāb al-sahw tenu imprimé", "kitāb al-sahw" in html and "référence tenue telle qu’imprimée, image 1200 dpi" in html)

# jugement
chk("deux dires", "en deux dires" in html)
chk("premier avis muttaṣil majorité", "le statut du muttaṣil" in html and "la majorité des muḥaddiṯs" in html)
chk("définition tadlīs", "le tadlīs est que le narrateur rapporte un ḥadīṯ d’un shaykh" in html)
chk("tadlīs formule admet audition", "une formule qui admet l’audition et sa non-occurrence" in html)
chk("mلاقاة condition Buḫārī Ibn al-Madīnī", "la condition de l’imām al-Buḫārī et de son shaykh Ibn al-Madīnī" in html)
chk("Muslim contemporanéité", "se contenta du constat que les deux furent en un seul âge" in html)
chk("citation Ibn al-Ṣalāḥ wa-famā", "wa-famā qāla Muslim naẓar" in html)
chk("citation Ibn al-Ṣalāḥ tranchée 2000 dpi", "[citation tranchée par l’image à 2000 dpi" in html)
chk("OCR wa-fīmā récusable", "l’OCR portant « wa-fīmā » récusable, divergence consignée" in html)
chk("ʿanʿana rapportée à l’audition", "rapporter l’ʿanʿana à l’audition" in html)
chk("conditions Ibn al-Samʿānī", "Ibn al-Samʿānī conditionna la longue fréquentation" in html)
chk("condition Dānī", "Abū ʿAmr al-Dānī conditionna qu’il soit connu" in html)
chk("Qābisī rencontre claire", "al-Qābisī dit : il incombe que le muʿanʿan rencontre" in html)
chk("second avis mursal/munaqaṭiʿ", "du type du mursal et du munaqaṭiʿ" in html)
chk("ʿan ne signale rien", "« ʿan » ne signale rien des modes de la prise" in html)
chk("Shuʿba ne suffit point", "« untel d’untel — son pareil ne suffit point »" in html)
chk("Sufyān suffit", "Sufyān al-Thawrī disait : « cela suffit »" in html)
chk("rétractation vers Sufyān", "rétracté de son dire vers le dire de Sufyān" in html)
chk("Nawawī rejeté consensus", "rejeté par consensus des anciens" in html)
chk("fa-la-dā tenu imprimé déclaré", "« fa-la-dā » tenu tel qu’imprimé, image 1600 dpi, construction déclarée" in html)

# rappel
chk("rappel 3 questions", "Quel est le sens du ḥadīṯ muʿanʿan" in html and "Expose la différence entre la condition d’al-Buḫārī" in html)

# exploitation
chk("Ibn ʿAbd al-Barr citation", "Sachez — que Dieu vous accorde la réussite" in html)
chk("trois conditions", "dès qu’il réunit trois conditions" in html)
chk("équité + rencontre + tadlīs", "l’équité des muḥaddiṯs en leurs états" in html and "qu’ils soient préservés du tadlīs" in html)
chk("référence Tamhīd 12/1", "al-Tamhīd" in html and "12/1" in html)
chk("muǧālamatan tenu imprimé déclaré", "« muǧālamatan » tenu tel qu’imprimé, construction déclarée" in html)
chk("examen deux questions", "J’examine le texte et je réponds à ce qui suit" in html and "pourquoi ces conditions furent-elles conditionnées" in html)

# préparation préalable + bornes
chk("préparation p.58 annonce mubham", "la préparation préalable imprimée de la présente leçon (p.58) annonce expressément le mubham" in html)
chk("bannière leçon 11 p.59 preuve", "le ḥadīṯ mubham » et son bloc d’objectifs y furent lus à l’image 1200 dpi [preuve commise]" in html)
chk("borne jamais devinée", "la borne fut tranchée par le sondage ; jamais devinée" in html)
chk("bornes 55 → 58", "s’ouvre en la page imprimée 55 et s’achève en la page 58" in html)
chk("leçon suivante page 59", "ouvre en la page 59 du même manuel" in html)

# 0 citation coranique
chk("0 citation coranique (cache non sollicité)", "cache coranique n’est pas sollicité" in html)

# rasm nu interdit + double rendu interdit
chk("rasm nu interdit", "rasm nu" not in html)
chk("interdit de double rendu déclaré", "interdite de double rendu" in html)

print(f"verify-ulumhadith1-pdf121 : {ok}/{ok+fail} PASS")
raise SystemExit(1 if fail else 0)

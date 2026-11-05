#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Minhāj — Vérification de la leçon ulum-hadith-tanawi-1 / pdf-mut23h2q-120
(le ḥadīṯ mašhūr, p.51-54 du manuel ulum-hadith-1-thanawi.pdf) :
contrôle de contenu — bannière « leçon 9 : le ḥadīṯ mašhūr » (tranchée
image 1200 dpi), bayt du nāẓim « machhūroun marwiyyin fawqā mā
thalāthati » (tranché image 1200 puis 1400 dpi, tenu tel qu'imprimé,
« khalaṯn » de l'OCR récusé, double occurrence boîte/citation consignée,
points de suspension imprimés déclarés), glose « šahartu l-ʾamra »,
extraction des thèmes p.52, définition (plus de trois narrateurs en
toutes les strates, nomination célébrité/clarté), objection des trois
+ condition du nāẓim vs majorité (voies dénombrées au-delà de deux),
citation d'Ibn Mandeh [al-Zuhrī/Quṭāda → gharīb/ʿazīz/mašhūr, tranchée
image 1400 dpi, OCR récusable], conciliation d'Ibn Ḥaǧar (la troupe =
le trois et ce qui le surpasse), mašhūr/mustafīḍ chez les fuqahāʾ avec
« ġāyara » tenu tel qu'imprimé déclaré, sections (selon l'artisanat /
célèbre sur les langues non artisanal, trois embranchements isnād),
matn d'al-Buḫārī « je fus célèbre, appelé contre un homme et Ḏukuwān »
[Ṣaḥīḥ al-Buḫārī, kitāb al-ǧihād et les marches, bāb : l'assistance par
le renfort — tranché image 1400 dpi, « raǧulin » récusant « raġlin »],
chaîne Anas b. Mālik / ʿAbd Allāh b. ʿAbbās / Ḫaffāf b. Īmāʾ al-Gifārī
→ Quṭāda, Abū Muǧlaz, Isḥāq b. ʿAbd Allāh b. Abī Ṭalḥa, ʿĀṣim al-Aḥwal
(concordante OCR-image), jugement (ni ṣaḥīḥ ni non ṣaḥīḥ d'entame, après
la recherche : ṣaḥīḥ/ḥasan/ḍaʿīf/mawḍūʿ), évaluation ×4, exploitation
(al-Zarqānī sur la Bayqūniyya + recherche mašhūr/mutawātir), préparation
préalable → muʿʿan ×2 questions, bornes p.51-54 TRIPLE PREUVE (objectifs
p.51 ; إعداد p.54 → muʿʿan ; bannière leçon 10 p.55 lue image 1200 dpi).
Usage: python3 scripts-translate/verify-ulumhadith1-pdf120.py
"""
import re

HTML = "/home/z/my-project/tr-tmp/lesson-ulumhadith1-pdf-mut23h2q-120-fr.html"

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
chk("h1 leçon 9", "leçon 9" in html and "<h1>" in html)
chk("h1 = registre titleFr", html.startswith("<h1>Le hadith célèbre (mašhūr)"))
chk("lesson-meta présent", 'class="lesson-meta"' in html and "Source du cours" in html)
chk("bornes pages 51 à 54 citées", "pages 51 à 54" in html)
chk("bannière leçon 9 lue", "leçon 9 : le ḥadīṯ mašhūr" in html)
chk("bannière 1200 dpi preuve", "fut lue à 1200 dpi [preuve commise]" in html)
chk("provenance OCR tesseract 300 dpi", "OCR tesseract arabe local à 300 dpi" in html)
chk("adjudication image 1200 puis 1400 dpi", "à 1200 puis 1400 dpi" in html)
chk("miroir archive.org item", "item 1_20220304_20220304_2251" in html)
chk("chaîne R578-R585 (suite de R585)", "R585" in html)
chk("cache R585 pré-seedé déclaré", "pré-seedées du cache R585" in html)

# objectifs
chk("objectif 1 concept", "Que je reconnaisse le concept du ḥadīṯ mašhūr" in html)
chk("objectif 2 sections et jugement", "les sections du ḥadīṯ mašhūr et son jugement" in html)
chk("objectif 3 importance du nombre", "l’importance du nombre en la validité du ḥadīṯ" in html)

# tamhīd
chk("tamhīd division par isnāds", "du point de vue du nombre de ses isnāds" in html)
chk("tamhīd triade gharīb/ʿazīz/mašhūr", "le gharīb, l’ʿazīz et le mašhūr" in html)
chk("tamhīd double question mustafīḍ", "sa relation au mustafīḍ" in html)

# bayt + glose
chk("bayt translittéré", "machhūroun marwiyyin fawqā mā thalāthati" in html)
chk("bayt OCR khalaṯn récusé", "khalaṯn" in html)
chk("double occurrence boîte/citation", "double occurrence consignée" in html)
chk("points de suspension imprimés déclarés", "les points de suspension appartiennent à l’imprimé" in html)
chk("glose šahartu l-ʾamra", "de « šahartu l-ʾamra »" in html)
chk("glose tranchée image 1200 dpi", "[glose tranchée par l’image à 1200 dpi]" in html)

# extraction des thèmes
chk("extraction p.52 deux thèmes", "l’extraction imprimée des deux thèmes" in html)

# définition
chk("définition plus de trois narrateurs", "plus de trois narrateurs, en toutes les strates du sanad" in html)
chk("nomination célébrité clarté", "pour sa célébrité et la clarté de sa chose" in html)
chk("objection des trois", "est-il compris en le mašhūr ou non" in html)
chk("condition nāẓim vs majorité", "les voies sont dénombrées au-delà de deux" in html)
chk("citation Ibn Mandeh", "le gharīb du ḥadīṯ est comme le ḥadīṯ d’al-Zuhrī et de Quṭāda" in html)
chk("citation Ibn Mandeh tranchée 1400", "[citation tranchée par l’image à 1400 dpi — les « il est nommé gharīb" in html)
chk("conciliation Ibn Ḥaǧar", "le visé par « la troupe » en son propos est le trois et ce qui le surpasse" in html)
chk("mašhūr/mustafīḍ fuqahāʾ", "le mašhūr est le mustafīḍ chez une troupe de fuqahāʾ" in html)
chk("ġāyara tenu imprimé déclaré", "« ġāyara » tenu tel qu’imprimé, construction déclarée" in html)

# sections
chk("départage artisanat/langues", "le ḥadīṯ mašhūr selon l’artisanat, et le ḥadīṯ mašhūr célèbre sur les langues" in html)
chk("matn Bukhari cité", "je fus célèbre, appelé contre un homme et Ḏukuwān" in html)
chk("référence Bukhari", "Ṣaḥīḥ al-Buḫārī" in html and "l’assistance par le renfort" in html)
chk("raǧulin récuse raġlin OCR", "le « raǧulin » récusant le « raġlin » de l’OCR" in html)
chk("chaîne Anas/Ibn ʿAbbās/Ḫaffāf", "Anas b. Mālik, ʿAbd Allāh b. ʿAbbās et Ḫaffāf b. Īmāʾ al-Gifārī" in html)
chk("chaîne Quṭāda/Abū Muǧlaz/Isḥāq/ʿĀṣim", "Quṭāda, Abū Muǧlaz, Isḥāq b. ʿAbd Allāh b. Abī Ṭalḥa et ʿĀṣim al-Aḥwal" in html)
chk("transmission nombre de la célébrité", "au-dessous du nombre de la célébrité" in html)
chk("non artisanal sans conditions", "une célébrité non artisanale" in html)
chk("isnād unique", "celui qui a un seul isnād" in html)
chk("isnāds multiples", "celui qui a plus d’un isnād" in html)
chk("absence d’isnād", "celui dont l’isnād n’existe point du tout" in html)
chk("jugement ni ṣaḥīḥ ni non ṣaḥīḥ d’entame", "il ne se décrit point comme ṣaḥīḥ ou non ṣaḥīḥ d’entame" in html)
chk("après la recherche quatre issues", "d’entre lui est le ṣaḥīḥ, d’entre lui le ḥasan, d’entre lui le ḍaʿīf, et d’entre lui le mawḍūʿ aussi" in html)

# évaluation
chk("évaluation 4 questions", "Déploie le propos en le definir du ḥadīṯ mašhūr" in html and "l’utilité de la célébrité du ḥadīṯ" in html)

# exploitation
chk("exploitation Zarqānī Bayqūniyya", "le commentaire d’al-Zarqānī sur la Bayqūniyya" in html)
chk("exploitation recherche mašhūr/mutawātir", "la relation du ḥadīṯ mašhūr au ḥadīṯ mutawātir" in html)

# préparation préalable + bornes
chk("préparation p.54 annonce muʿʿan", "la préparation préalable imprimée de la présente leçon (p.54) annonce expressément le muʿʿan" in html)
chk("bannière leçon 10 p.55 preuve", "le ḥadīṯ muʿʿan » et son bloc d’objectifs y furent lus à l’image 1200 dpi [preuve commise]" in html)
chk("borne jamais devinée", "la borne fut tranchée par le sondage ; jamais devinée" in html)

# 0 citation coranique
chk("0 citation coranique (cache non sollicité)", "cache coranique n’est pas sollicité" in html)

# rasm nu interdit + double rendu interdit
chk("rasm nu interdit", "rasm nu" not in html)
chk("interdit de double rendu déclaré", "interdite de double rendu" in html)

print(f"verify-ulumhadith1-pdf120 : {ok}/{ok+fail} PASS")
raise SystemExit(1 if fail else 0)

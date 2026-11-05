#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Minhāj — Vérification de la leçon ulum-hadith-tanawi-1 / pdf-mut23h2q-119
(le ḥadīṯ ʿazīz, p.47-50 du manuel ulum-hadith-1-thanawi.pdf) :
contrôle de contenu — bannière « leçon 8 » (tranchée image 1200 dpi),
bayt du nāẓim « l'ʿazīz, narré par deux ou par trois » (tranché image
1200 dpi, tenu tel qu'imprimé), détours du mutawātir (définition, deux
sections) et du āḥād, prose « ne descend point au-dessous de deux en
toutes les strates », sortie du mašhūr (trois) et du gharīb (un),
nomination (fort par une autre voie / rareté), débat Ibn Ḥibbān récusé
par Ibn Ḥaǧar [Nuzhat an-naẓar : 49] (citation tranchée image 1200 dpi),
exemple des deux šayḫs/Anas + al-Buḫārī/Abū Hurayra (matn tranché image
[Ṣaḥīḥ al-Buḫārī, kitāb al-īmān, bāb : l'amour du messager ﷺ]) + chaîne
Quṭāda/ʿAbd al-ʿAzīz b. Ṣuhayb → Šuʿba/Saʿīd + Ismāʿīl b. ʿUlayya/
ʿAbd al-Wāriṯ (tranchée image), relation ʿazīz/ṣaḥīḥ = général/particulier
sous un même point de vue (duel « en eux » tranché image 1400 dpi),
l'ʿizza n'est point condition contre al-Ǧubbāʾī le muʿtazilite + dire
d'al-Ḥākim (verbe yuwammaʾu tranché image 1400 dpi), Ibn al-ʿArabī
condition d'al-Buḫārī [Ṣaḥīḥ al-Buḫārī, kitāb badʾ al-waḥy, bāb :
comment fut l'entame de la révélation], ḥadīṯ « les œuvres ne valent que
par les intentions » fard d'ʿAlqama d'ʿUmar + réponse du minbar,
contrerapeu (Muḥammad b. Ibrāhīm / Yaḥyā b. Saʿīd / mutābaʿāt « lā
yuʿtaru bihā » tenue telle qu'imprimée, construction déclarée), Ibn Rušd
(le premier ḥadīṯ mentionné), évaluation ×3, exploitation = ḥadīṯ de la
grand-mère [al-Muwaṭṭaʾ, kitāb al-farāʾiḍ, bāb mīrāṯ al-ǧadda] avec
faqāma tranché image 1400 dpi + al-farāʾiḍ tranché image 1400 dpi contre
« al-qarāʾiḍ » de l'OCR, questions ×2, préparation préalable → mašhūr
(Q1 révélée par l'image), bornes p.47-50 TRIPLE PREUVE (objectifs p.47 ;
إعداد p.50 → mašhūr ; bannière leçon 9 p.51). Usage: python3 scripts-translate/verify-ulumhadith1-pdf119.py
"""
import re

HTML = "/home/z/my-project/tr-tmp/lesson-ulumhadith1-pdf-mut23h2q-119-fr.html"

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
chk("h1 leçon 8", "leçon 8" in html and "<h1>" in html)
chk("h1 = registre titleFr", html.startswith("<h1>Le hadith rare (ʿazīz)"))
chk("lesson-meta présent", 'class="lesson-meta"' in html and "Source du cours" in html)
chk("bornes pages 47 à 50 citées", "pages 47 à 50" in html)
chk("bannière leçon 8 lue", "leçon 8 : le ḥadīṯ ʿazīz" in html)
chk("bannière 1200 dpi preuve", "fut lue à 1200 dpi [preuve commise]" in html)
chk("provenance OCR tesseract 300 dpi", "OCR tesseract arabe local à 300 dpi" in html)
chk("adjudication image 1200 et 1400 dpi", "à 1200 et 1400 dpi" in html)
chk("miroir archive.org item", "item 1_20220304_20220304_2251" in html)
chk("chaîne R578-R584 (suite de R584)", "R584" in html)

# objectifs
chk("objectif 1 concept", "Que je reconnaisse le concept du ḥadīṯ ʿazīz" in html)
chk("objectif 2 relation au ṣaḥīḥ", "la relation du ḥadīṯ ʿazīz au ḥadīṯ ṣaḥīḥ" in html)
chk("objectif 3 multiplicité des voies", "multiplicité des voies en la force du ḥadīṯ" in html)

# tamhīd
chk("tamhīd division peu/nombreux", "du point de vue du nombre de ses isnāds" in html)
chk("tamhīd triade gharīb/mašhūr/ʿazīz", "le gharīb, le mašhūr et l’ʿazīz" in html)
chk("tamhīd double question", "relation de l’ʿizza à la validité du ḥadīṯ" in html)

# glose
chk("glose ʿazza = fort, ʿayn", "de ʿazza — il fut fort — à l’ouverture du ʿayn" in html)
chk("glose déclarée", "construction déclarée" in html)

# extraction des thèmes
chk("extraction 2 questions", "deux questions d’extraction imprimées" in html)
chk("extraction Q2 p.48 OCR", "imprimée en tête de la page 48" in html)
chk("extraction Q1 p.47 non captée", "non captée par l’OCR 300 dpi" in html)

# définition
chk("nāẓim divisa par nombre des narrateurs", "nombre de ses narrateurs" in html)
chk("détour mutawātir accepté par accord", "accepté par l’accord des gens du ḥadīṯ" in html)
chk("détour pas un chapitre de l'artisanat", "ne relève pas des chapitres de leur artisanat" in html)
chk("def mutawātir concertation impossible", "concertation en le mensonge impossible" in html)
chk("mutawātir 2 sections littéral/sémantique", "littéral et sémantique" in html)
chk("āḥād répond au mutawātir", "au ḥadīṯ mutawātir répond le ḥadīṯ āḥād" in html)
chk("bayt tranché image 1200", "bayt tranché par l’image à 1200 dpi" in html)
chk("bayt deux ou trois", "narré par deux ou par trois" in html)
chk("prose ne descend au-dessous de deux", "au-dessous de deux, en toutes les strates du sanad" in html)
chk("sortie du mašhūr (trois)", "au-dessous de trois" in html)
chk("sortie du gharīb (un seul)", "que ne rapporte qu’un seul narrateur" in html)
chk("nomination fort par autre voie", "fort, par son arrivée par une autre voie" in html)
chk("nomination rareté", "la rareté de son existence" in html)
chk("prétention d'Ibn Ḥibbān", "Ibn Ḥibbān" in html and "la narration de deux d’après deux n’existe point du tout" in html)
chk("réponse d'Ibn Ḥaǧar Nuẓha", "Ibn Ḥaǧar lui répondit en la Nuẓha" in html)
chk("citation Nuẓha deux seulement", "deux seulement d’après deux seulement" in html)
chk("citation Nuẓha forme délimitée existe", "la forme de l’ʿazīz que nous avons délimitée" in html)
chk("réf Nuẓha : 49", "Nuzhat an-naẓar, d’Ibn Ḥaǧar : 49" in html)
chk("citation Nuẓha tranchée image", "citation tranchée par l’image à 1200 dpi" in html)

# exemple
chk("exemple deux šayḫs + Buḫārī", "les deux šayḫs du ḥadīṯ d’Anas, et al-Buḫārī du ḥadīṯ d’Abū Hurayra" in html)
chk("matn aucun de vous ne croit", "aucun de vous ne croit, jusqu’à ce que je sois plus aimé de lui" in html)
chk("matn père/enfant/gens", "son père, son enfant et les gens, tous ensemble" in html)
chk("réf Buḫārī īmān", "Ṣaḥīḥ al-Buḫārī ; kitāb al-īmān" in html)
chk("bāb amour du messager", "l’amour du messager ﷺ fait partie de la foi" in html)
chk("matn tranché image", "matn tranché par l’image à 1200 dpi, tenu tel qu’imprimé" in html)
chk("chaîne Quṭāda + ʿAbd al-ʿAzīz b. Ṣuhayb", "Quṭāda et ʿAbd al-ʿAzīz b. Ṣuhayb" in html)
chk("chaîne Šuʿba + Saʿīd", "Šuʿba et Saʿīd" in html)
chk("chaîne Ismāʿīl b. ʿUlayya + ʿAbd al-Wāriṯ", "Ismāʿīl b. ʿUlayya et ʿAbd al-Wāriṯ" in html)
chk("chaîne tranchée image", "chaîne tranchée par l’image à 1200 dpi" in html)

# relation
chk("titre deuxièmement", "Deuxièmement : la relation entre le ḥadīṯ ʿazīz et le ḥadīṯ ṣaḥīḥ" in html)
chk("jamhūr général/particulier", "l’emboîtement du général et du particulier sous un même point de vue" in html)
chk("réunion deux d'après deux + conditions", "les deux qualités se réunissent en ce que rapportèrent deux d’après deux" in html)
chk("singul. ṣaḥīḥ au-delà", "s’y singularise par ce qu’il rapporta au-delà de cela" in html)
chk("singul. ʿazīz sans conditions", "sans que s’y réunissent les conditions de la validité" in html)
chk("duel tranché image 1400", "accord du duel tranché par l’image à 1400 dpi" in html)
chk("ʿizza n'est point condition", "n’est point une condition de la validité du ḥadīṯ" in html)
chk("contre al-Ǧubbāʾī muʿtazilite", "contre al-Ǧubbāʾī le muʿtazilite" in html)
chk("dire d'al-Ḥākim fait signe", "le dire d’al-Ḥākim fait signe" in html)
chk("yuwammaʾu tranché image 1400", "yuwammaʾu tranché par l’image à 1400 dpi, tenu tel qu’imprimé" in html)
chk("Ibn al-ʿArabī déclara", "Ibn al-ʿArabī déclara explicitement, en son commentaire du Ṣaḥīḥ d’al-Buḫārī" in html)
chk("condition propre d'al-Buḫārī", "une condition propre d’al-Buḫārī" in html)
chk("réf badʾ al-waḥy", "kitāb badʾ al-waḥy" in html)
chk("bāb entame de la révélation", "comment fut l’entame de la révélation" in html)
chk("hadith des intentions", "les œuvres ne valent que par les intentions" in html)
chk("fard ʿAlqama d'ʿUmar", "que seul ʿAlqama rapporta d’ʿUmar" in html)
chk("réponse minbar Compagnons", "en prêche, sur la chaire, devant les Compagnons" in html)
chk("réponse s'ils ne l'avaient connu", "ils l’auraient réprouvé" in html)
chk("contrerapeu silence", "il ne s’ensuit point de leur silence devant lui" in html)
chk("contrerapeu s'effondre en ʿAlqama", "s’effondre en la singularité d’ʿAlqama" in html)
chk("contrerapeu Muḥammad b. Ibrāhīm", "Muḥammad b. Ibrāhīm s’en singularisa d’après ʿAlqama" in html)
chk("contrerapeu Yaḥyā b. Saʿīd", "Yaḥyā b. Saʿīd s’en singularisa d’après Muḥammad" in html)
chk("selon ce qui est le vrai connu", "selon ce qui est le vrai, connu des muḥaddiṯs" in html)
chk("mutābaʿāt", "il lui advint des suivants (mutābaʿāt)" in html)
chk("lā yuʿtaru bihā tenue imprimée", "tenue telle qu’imprimée, construction déclarée" in html)
chk("concéder en ʿUmar / réponse non", "sa réponse ne se concède point en d’autres" in html)
chk("Ibn Rušd", "Ibn Rušd dit" in html)
chk("Ibn Rušd qāḍī Ibn al-ʿArabī", "il aurait suffi au qāḍī — c’est-à-dire Ibn al-ʿArabī" in html)
chk("Ibn Rušd premier hadith", "le premier ḥadīṯ mentionné dans [le livre]" in html)

# évaluation
chk("évaluation Q1", "Qu’est-ce que le ḥadīṯ ʿazīz" in html)
chk("évaluation Q2 mutawātir", "n’a-t-il point mentionné le ḥadīṯ mutawātir" in html)
chk("évaluation Q3 relation", "la relation entre le ḥadīṯ ʿazīz et le ḥadīṯ ṣaḥīḥ" in html)

# exploitation
chk("exploitation ḥadīṯ grand-mère", "L’exploitation imprimée rapporte le ḥadīṯ de la grand-mère" in html)
chk("chaîne Mālik/Ibn Šihāb/ʿUṯmān b. Isḥāq b. Ḫaraša/Nubayṣa", "d’Ibn Šihāb, d’ʿUṯmān b. Isḥāq b. Ḫaraša, de Nubayṣa b. Ḏuʾayb" in html)
chk("rien dans le livre de Dieu", "tu n’as rien, dans le livre de Dieu" in html)
chk("rien en la sunna", "en la sunna du messager de Dieu ﷺ" in html)
chk("al-Muġīra assista + sixième", "j’assistai, auprès du messager de Dieu ﷺ — il lui donna le sixième" in html)
chk("faqāma tranché image 1400", "verbe faqāma tranché par l’image à 1400 dpi" in html)
chk("réponse ʿUmar jugement pour autre", "le jugement qui fut prononcé ne le fut que pour une autre que toi" in html)
chk("al-farāʾiḍ tranché contre OCR", "mot al-farāʾiḍ tranché par l’image à 1400 dpi" in html)
chk("al-qarāʾiḍ de l'OCR déclarée", "contre la lecture « al-qarāʾiḍ » de l’OCR" in html)
chk("sixième réunion/séparation", "si vous vous réunissez toutes deux, il est entre vous deux" in html)
chk("réf Muwaṭṭaʾ farāʾiḍ", "al-Muwaṭṭaʾ, de l’ʾimām Mālik ; kitāb al-farāʾiḍ ; bāb mīrāṯ al-ǧadda" in html)
chk("texte long rendu en sens", "texte long rendu en sens, altérations déclarées" in html)
chk("exploitation Q1 Muġīra", "ne se contenta-t-il point de la narration d’al-Muġīra b. Šuʿba" in html)
chk("exploitation Q2 ʿizza", "l’exigence de l’ʿizza en la validité du ḥadīṯ" in html)

# préparation préalable + bornes
chk("préparation matn leçon prochaine", "je retiens le matn de la leçon prochaine et j’examine son commentaire" in html)
chk("préparation Q1 mašhūr", "quel est le ḥadīṯ mašhūr" in html)
chk("préparation Q2 célèbres sur les langues", "célèbres sur les langues" in html)
chk("ouverture p.47 / clôture p.50", "s’ouvre en la page imprimée 47 et s’achève en la page 50" in html)
chk("leçon suivante p.51", "ouvre en la page 51 du même manuel" in html)
chk("bannière leçon 9 lue image", "la bannière « leçon 9 : le ḥadīṯ mašhūr » et son premier objectif y furent lus à l’image 1200 dpi" in html)
chk("préparation p.50 annonce mašhūr", "la préparation préalable imprimée de la présente leçon (p.50) annonce expressément le mašhūr" in html)
chk("borne jamais devinée", "la borne fut tranchée par le sondage ; jamais devinée" in html)

# 0 citation coranique
chk("0 citation coranique (cache non sollicité)", "cache coranique n’est pas sollicité" in html)

# rasm nu interdit + double rendu interdit
chk("rasm nu interdit", "rasm nu" not in html)
chk("interdit de double rendu déclaré", "interdites de double rendu" in html)

print(f"verify-ulumhadith1-pdf119 : {ok}/{ok+fail} PASS")
raise SystemExit(1 if fail else 0)

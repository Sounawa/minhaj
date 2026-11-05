#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Minhāj — Vérification de la leçon ulum-hadith-tanawi-1 / pdf-mut23h2q-126
(le ḥadīṯ ġarīb, p.76-79 du manuel ulum-hadith-1-thanawi.pdf) :
contrôle de contenu — bannière « leçon 15 : le ḥadīṯ ġarīb » (relue image
1200 dpi : badge al-dars 15 + الحديث الغريب), bayt du nāẓim « wa-qul
ġarībun mā rawā rāwin faqaṭ » (tranché image 2400 dpi, premier hémistiche
imprimé EN POINTS DE SUITE — blanc pédagogique, tenu tel qu'imprimé,
jamais reconstitué), bandeaux al-matn/aš-šarḥ (1200-1600 dpi), bandeaux
calligraphiques tranchés PAR L'IMAGE 2400 dpi (istikhlāṣ al-maḍāmīn p.77,
taḥlīl p.77, taqwīm + istiṯmār p.79), extraction des contenus (2 questions,
p.77), analyse (définition + parenté mufrad muṭlaq/nisbī ; 2 familles de
divisions : ṣaḥīḥ — ḥadīṯ du voyage Mālik/Suhayl/Abū Ṣāliḥ/Abū Hurayra
« yamnaʿu … nawmahu wa-ṭaʿāmahu wa-šarābahu » tranché 1600 dpi, ʿUmar/niyyāt,
Mālik « šarru l-ʿilmi l-ġarīb », ʿAbd ar-Razzāq, Ibn Ḥanbal ; matn/isnād —
cinq divisions, ġarāʾib aš-šuyūḫ, aṯ-Tirmiḏī « ġarīb min hāḏā l-waǧh »,
Umm Zarʿ aṭ-Ṭabarānī ad-Darāwardī/ʿAbbād b. Manṣūr tranché 3600 dpi,
maḥfūẓ ʿĪsā b. Yūnus « hākaḏā ʾaṯbatahu š-šayḫān » tranché 3600 dpi contre
« as-sabṭān », Abū l-Fatḥ, zakāt al-fiṭr « mina l-muslimīn » addition
de Mālik), rappel ×3 (3e question recouvrée à l'image), exploitation
(Ibn Raǧab « bi-ʾannahu fī ġalabi l-ʾabwāb » 3600 dpi, « ṯumma bayyana »,
« wa-ka-ʾanna maqṣadahu », šarḥ ʿilal at-Tirmiḏī 621/2), préparation
préalable → munqaṭiʿ + muʿḍal deux questions (« mā ḥukmu l-ʿamali bi-himā »
2400 dpi), bornes p.76-79 (bannière + objectifs p.76 ; bannière al-dars 16
p.80 OCR 300 dpi concordante), folio 79 tranché image.
Usage: python3 scripts-translate/verify-ulumhadith1-pdf126.py
"""
import re

HTML = "/home/z/my-project/tr-tmp/lesson-ulumhadith1-pdf-mut23h2q-126-fr.html"

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
chk("h1 leçon 15", "leçon 15" in html and "<h1>" in html)
chk("h1 = registre titleFr", html.startswith("<h1>Le hadith insolite (gharīb)"))
chk("lesson-meta présent", 'class="lesson-meta"' in html and "Source du cours" in html)
chk("bornes pages 76 à 79 citées", "pages 76 à 79" in html)
chk("bannière leçon 15 citée", "leçon 15 : le ḥadīṯ ġarīb" in html)
chk("bannière relue 1200 dpi", "relue à l’image 1200 dpi" in html)
chk("badge al-dars 15", "badge « al-dars 15 »" in html)
chk("provenance OCR tesseract 300 dpi", "OCR tesseract arabe local à 300 dpi" in html)
chk("adjudication 1200…3600 dpi", "à 1200, 1600, 2000, 2400 et 3600 dpi" in html)
chk("miroir archive.org item", "item 1_20220304_20220304_2251" in html)
chk("chaîne (suite de R591)", "R591" in html)
chk("cache R592 crash-safe", "cache R592, crash-safe" in html)

# objectifs
chk("objectif 1 concept + divisions", "le concept du ḥadīṯ ġarīb et ses divisions" in html)
chk("objectif 2 distinguer ressemblants", "Que je distingue le ḥadīṯ ġarīb de ce qui lui ressemble" in html)
chk("objectif 3 éviter poursuite non gardés", "la poursuite des ḥadīṯs ġarībs qui ne sont point gardés" in html)

# tamhīd
chk("tamhīd poursuite isnāds/matns", "poursuivirent les isnāds des ḥadīṯs et leurs matns" in html)
chk("tamhīd sécurité Sunna", "par sécurité pour la transmission de la Sunna prophétique éminente" in html)
chk("tamhīd un seul transmetteur", "en totalité ou en partie, un seul transmetteur" in html)
chk("tamhīd double question", "Quel est donc le ḥadīṯ ġarīb" in html and "quelles sont ses divisions" in html)

# bayt + glose
chk("bayt hémistiche translittéré", "wa-qul ġarībun mā rawā rāwin faqaṭ" in html)
chk("bayt premier hémistiche points", "premier hémistiche" in html and "points de suite" in html)
chk("bayt tranché image 2400 dpi", "tranché par l’image à 2400 dpi" in html)
chk("blanc jamais reconstitué", "tenu tel qu’imprimé, jamais reconstitué" in html)
chk("bandeau al-matn cité", "« al-matn »" in html)
chk("glose ġurba exil", "dérivé de la ġurba (l’exil)" in html)
chk("glose ġarīb du pays", "le ġarīb dans le pays est celui qui n’est point des gens du lieu" in html)
chk("bandeau aš-šarḥ cité", "« aš-šarḥ »" in html)
chk("glose relue 1600 dpi", "glose unique, relue à 1600 dpi" in html)

# extraction des thèmes (istikhlāṣ al-maḍāmīn)
chk("extraction istikhlāṣ al-maḍāmīn", "extraction des contenus (istikhlāṣ al-maḍāmīn)" in html)
chk("extraction 2 questions", "sous la forme de deux questions" in html)
chk("question 1 muḥaddithūn", "Qu’entend-on par le ḥadīṯ ġarīb chez les muḥaddithūn" in html)
chk("question 2 j'expose divisions", "J’expose les divisions du ḥadīṯ ġarīb." in html)
chk("bandeau calligraphique tranché 2400", "tranché PAR L’IMAGE à 2400 dpi en tête de la page 77" in html)

# analyse : définition
chk("analyse contient ce qui suit", "Cette leçon contient ce qui suit" in html)
chk("premièrement définition + formes", "la définition du ḥadīṯ ġarīb et les formes de la ġurba en lui" in html)
chk("bayt cité par le šarḥ", "définissait le ḥadīṯ ġarīb en disant" in html)
chk("munfaridan", "seul (munfaridan) dans sa narration" in html)
chk("parenté mufrad", "de très proche parenté avec « le ḥadīṯ mufrad »" in html)
chk("un seul type", "tous deux sont d’un seul type" in html)
chk("fréquence emploi + rareté", "la fréquence de l’emploi et de la rareté" in html)
chk("mufrad muṭlaq / ġarīb nisbī", "mufrad muṭlaq (absolu)" in html and "mufrad nisbī (relatif)" in html)
chk("nāẓim choisit distinction", "le nāẓim choisit la distinction" in html)

# analyse : divisions 1 (ṣiḥḥa)
chk("deuxièmement divisions", "Deuxièmement : les divisions du ḥadīṯ ġarīb" in html)
chk("famille 1 degré santé", "au regard du degré de santé (ṣiḥḥa)" in html)
chk("ġarīb ṣaḥīḥ mufrads du Ṣaḥīḥ", "comme les mufrads du Ṣaḥīḥ, lesquels sont nombreux" in html)
chk("ḥadīṯ voyage Mālik/Suhayl", "Mālik rapporta de Suhayl, d’après Abū Ṣāliḥ, d’après Abū Hurayra, marfūʿ" in html)
chk("ḥadīṯ voyage matn", "as-safaru qiṭʿatun mina l-ʿaḏāb. yamnaʿu ʾaḥadukum nawmahu wa-ṭaʿāmahu wa-šarābahu" in html)
chk("ḥadīṯ voyage clausule", "fa-ʾiḏā qaḍā ʾaḥadukum nahmatahu min waǧhatihi. fa-l-yaʿǧal ʾilā ahlihi" in html)
chk("ḥadīṯ voyage renvoi", "[al-Muwaṭṭaʾ ; kitāb al-istiʾḏān ; bāb mā yuʾmaru min al-ʿamal fī as-safar" in html)
chk("ḥadīṯ voyage relus 1600", "relus à l’image à 1600 dpi" in html)
chk("ʿAlqama ʿUmar niyyāt", "d’ʿAlqama, d’après ʿUmar b. al-Ḫaṭṭāb" in html and "ʾinnamā l-ʾaʿmālu bi-n-niyyāt" in html)
chk("renvoi Buḫārī badʾ al-waḥy", "kitāb badʾ al-waḥy" in html)
chk("Ġarīb non ṣaḥīḥ dominant", "le ġarīb qui n’est point ṣaḥīḥ, lequel est le dominant parmi le ġarīb" in html)
chk("Mālik šarru l-ʿilmi", "šarru l-ʿilmi l-ġarību" in html and "wa-ḫayru l-ʿilmi ẓ-ẓāhiru allaḏī qad rawāhu n-nās" in html)
chk("Mālik relue 2000", "[relue à l’image à 2000 dpi]" in html)
chk("ʿAbd ar-Razzāq aṣ-Ṣanʿānī", "ʿAbd ar-Razzāq aṣ-Ṣanʿānī" in html and "kunnā narā ʾanna ġarība l-ḥadīṯi ḫayrun fa-ʾiḏā huwa šarr" in html)
chk("Ibn Ḥanbal ġarāʾibs", "Ibn Ḥanbal dit" in html and "lā taktubū hāḏihī l-ġarāʾiba fa-ʾinnahā manākīru wa-ġālibuhā ʿani ḍ-ḍuʿafāʾ" in html)

# analyse : divisions 2 (matn/isnād)
chk("famille 2 matn/isnād", "au regard du matn et de l’isnād" in html)
chk("cinq divisions", "en cinq divisions" in html)
chk("division 1 isnād+matn", "le ḥadīṯ ġarīb en isnād et en matn" in html)
chk("division 2 sans exemple", "le ġarīb en matn sans l’isnād — cette division n’a point d’exemple" in html)
chk("division 3 isnād seulement", "le ḥadīṯ ġarīb en isnād seulement" in html)
chk("division 3 groupe Compagnons", "la narration d’un groupe de Compagnons pour lui" in html)
chk("division 3 matn non ġarīb", "bien que son matn ne soit point ġarīb" in html)
chk("ġarāʾib aš-šuyūḫ", "les ġarāʾibs des shaykhs dans les isnāds des matns ṣaḥīḥs" in html)
chk("Tirmiḏī ġarīb du visage", "« ġarīb de ce visage (ġarīb min hāḏā l-waǧh) »" in html)
chk("division 4 Umm Zarʿ", "aṭ-Ṭabarānī dans al-Kabīr, d’après ʿAbd al-ʿAzīz ad-Darāwardī et ʿAbbād b. Manṣūr" in html)
chk("division 4 Ḥišām père ʿĀʾiša", "d’après Ḥišām b. ʿUrwa, d’après son père, d’après ʿĀʾiša" in html)
chk("maḥfūẓ ʿĪsā b. Yūnus", "ʿĪsā b. Yūnus, d’après Ḥišām b. ʿUrwa, d’après son frère ʿAbd Allāh b. ʿUrwa, d’après ʿUrwa, d’après ʿĀʾiša" in html)
chk("hākaḏā ʾaṯbatahu š-šayḫān", "hākaḏā ʾaṯbatahu š-šayḫān" in html)
chk("alif wa-ʿAbbād tranché 3600", "l’alif de « wa-ʿAbbād » tranché à 3600 dpi" in html)
chk("as-sabṭān récusé", "« as-sabṭān » de l’OCR 300 dpi récusé" in html)
chk("Abū l-Fatḥ", "Abū l-Fatḥ dit : c’est là une ġarāba propre à un endroit de l’isnād, et le ḥadīṯ est ṣaḥīḥ" in html)
chk("division 5 ġarāba matn", "celui dont la ġarāba est dans une partie de son matn" in html)
chk("zakāt al-fiṭr matn", "farraḍa zakāta l-fiṭri ʿalā n-nāsi min Ramaḍāna ṣāʿan min tamrin, ʾaw ṣāʿan min šaʿīrin, ʿalā kulli ḥurrin ʾaw ʿabdin ; ḏakarin ʾaw ʾunṯā ; mina l-muslimīn" in html)
chk("zakāt renvoi", "[al-Muwaṭṭaʾ ; de l’imām Mālik ; kitāb az-zakāt ; bāb makīlat zakāt al-fiṭr" in html)
chk("addition des Musulmans", "par l’addition : « des Musulmans »" in html)

# rappel
chk("rappel 3 questions", "sous la forme de trois questions" in html)
chk("rappel définition", "Quelle est la définition du ḥadīṯ ġarīb" in html)
chk("rappel 3e recouvrée", "la troisième question, manquante à l’OCR 300 dpi, fut recouvrée à l’image" in html)
chk("rappel ġarāba+ṣiḥḥa", "La ġarāba et la santé se réunissent-elles dans un ḥadīṯ" in html)

# exploitation
chk("exploitation Ibn Raǧab", "Ibn Raǧab — que Dieu lui fasse miséricorde — rapporte en son Commentaire des ʿilal d’aṯ-Tirmiḏī" in html)
chk("bi-ʾannahu fī ġalabi l-ʾabwāb", "« bi-ʾannahu fī ġalabi l-ʾabwāb »" in html)
chk("alif ʾannahu tranché 3600", "l’alif de « ʾannahu » tranché à 3600 dpi" in html)
chk("ṯumma bayyana contre OCR", "« ṯumma bayyana » contre le « fī-bayyina » de l’OCR récusé" in html)
chk("wa-ka-ʾanna contre wa-kāna", "« wa-ka-ʾanna maqṣadahu » contre le « wa-kāna » récusé" in html)
chk("quote ʿugturiḍa", "l’on objecta (ʿugturiḍa) sur aṯ-Tirmiḏī" in html)
chk("expose ʿilal puis ṣaḥīḥ", "expose les ʿilal (défauts) qui s’y trouvent, puis expose le ṣaḥīḥ dans l’isnād" in html)
chk("an-Nasāʾī voies du ḥadīṯ", "tu trouves an-Nasāʾī, quand il embrasse les voies du ḥadīṯ, commencer par ce qui est fautif" in html)
chk("renvoi 621/2", "[šarḥ ʿilal at-Tirmiḏī d’Ibn Raǧab : 621/2]" in html)
chk("activité j'examine", "J’examine le texte et je réponds à ce qui suit" in html)
chk("q1 pourquoi objecté", "Pourquoi a-t-on objecté sur l’imām aṯ-Tirmiḏī en son traitement du ġarīb" in html)
chk("q2 visée faute d'abord", "de la faute d’abord, et du report du juste" in html)

# préparation préalable + bornes
chk("préparation munqaṭiʿ + muʿḍal", "je reconnais le ḥadīṯ munqaṭiʿ (interrompu) et le ḥadīṯ muʿḍal (gauchi)" in html)
chk("préparation statut agir", "quel est le statut de l’agir par eux" in html)
chk("bornes déclarées 76/79", "s’ouvre en la page imprimée 76 et s’achève en la page 79" in html)
chk("leçon suivante p.80", "ouvre en la page 80 du même manuel" in html)
chk("bannière al-dars 16 concordante", "sa bannière imprimée (al-dars 16) et ses trois objectifs y furent lus à l’OCR 300 dpi" in html)
chk("borne par sondage jamais devinée", "la borne fut tranchée par le sondage ; jamais devinée" in html)
chk("leçon suivante interdite double rendu", "est interdite de double rendu" in html)
chk("aucune āya déclarée", "ne contient aucune āya" in html)
chk("folio 79 tranché", "folio imprimé « 79 » fut tranché par l’image" in html)

print(f"\n{ok}/{ok+fail} PASS")
exit(1 if fail else 0)

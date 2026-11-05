#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Minhāj — Vérification de la leçon ulum-hadith-tanawi-1 / pdf-mut23h2q-125
(le ḥadīṯ mursal, p.72-75 du manuel ulum-hadith-1-thanawi.pdf) :
contrôle de contenu — bannière « leçon 14 : le ḥadīṯ mursal » (relue image
1500 dpi : badge al-dars 14 + الحديث المرسل), bayt du nāẓim « wa-mursalun
minhu aṣ-ṣaḥābiyyu saqaṭa » (tranché image 2400 dpi, second hémistiche
imprimé EN POINTS DE SUITE — blanc pédagogique, tenu tel qu'imprimé,
jamais reconstitué), bandeaux al-matn/aš-šarḥ (3000 dpi), āya Maryam
(imprimé warš « ʾannā ʾakūnu lī ġulāmun wa-kānatimraʾatī ʿāqiran
wa-ʾinnī halaktu ʾaw kabiran », marqueur imprimé « 84 » tranché image
2400 dpi = coquille, texte cité = réplique de Zakariyyā = cache canonique
19:8, correspondance PAR LE TEXTE, écart de riwāya ʾakūnu/yakūnu déclaré),
glose « al-iʾrsāl / al-iṭlāq », extraction des contenus (2 questions,
p.73), analyse (3 définitions : saḥābī tombé — Ibn al-Musayyib/Qays b.
Abī Ḥāzim/Ibn Ḥajar/aṭ-Ṭanūḫī ; grand Tābiʿī — Ibn ʿAbd al-Barr, munqaṭiʿ ;
un ou plusieurs — Ibn aṣ-Ṣalāḥ/an-Nawawī/muʿḍal/muʿallaq/al-Ḫaṭīb), statut
de l'argumentation (Abū Ḥanīfa/Mālik/Aḥmad ; aṣ-Suyūṭī « lu ʿurifa » tranché
image 1400 dpi contre « ġarafa » OCR), rappel ×2, exploitation (2 textes
Muwaṭṭaʾ : Nāfiʿ/ʿaqīqa « bišātin šātan » imprimé ; ʿAbd ar-Raḥmān b.
Harmala al-Aslamī/Saʿīd b. al-Musayyib/Fiṭr), préparation préalable →
ġarīb deux questions, bornes p.72-75 (bannière + objectifs p.72 ;
objectifs ġarīb p.76 OCR 300 dpi concordants).
Usage: python3 scripts-translate/verify-ulumhadith1-pdf125.py
"""
import re

HTML = "/home/z/my-project/tr-tmp/lesson-ulumhadith1-pdf-mut23h2q-125-fr.html"

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
chk("h1 leçon 14", "leçon 14" in html and "<h1>" in html)
chk("h1 = registre titleFr", html.startswith("<h1>Le hadith à transmetteur omis (mursal)"))
chk("lesson-meta présent", 'class="lesson-meta"' in html and "Source du cours" in html)
chk("bornes pages 72 à 75 citées", "pages 72 à 75" in html)
chk("bannière leçon 14 citée", "leçon 14 : le ḥadīṯ mursal" in html)
chk("bannière relue 1500 dpi", "fut relue à l’image 1500 dpi" in html)
chk("badge al-dars 14", "badge « al-dars 14 »" in html)
chk("provenance OCR tesseract 300 dpi", "OCR tesseract arabe local à 300 dpi" in html)
chk("adjudication 1400…3600 dpi", "à 1400 puis 1500, 1600, 2400, 3000 et 3600 dpi" in html)
chk("miroir archive.org item", "item 1_20220304_20220304_2251" in html)
chk("chaîne (suite de R590)", "R590" in html)
chk("cache R590 pré-seedé déclaré", "pré-seedées du cache R590" in html)

# objectifs
chk("objectif 1 concept mursal + agir", "le concept du ḥadīṯ mursal et le statut de l’agir par lui" in html)
chk("objectif 2 distinguer ressemblants", "Que je distingue le ḥadīṯ mursal de ce qui lui ressemble" in html)
chk("objectif 3 mérite des Compagnons", "le mérite des Compagnons et leur supériorité" in html)

# tamhīd
chk("tamhīd condition connexion", "l’existence de la connexion dans son isnād" in html)
chk("tamhīd condition manquante faible", "si cette condition vient à manquer, le ḥadīṯ est considéré faible" in html)
chk("tamhīd forme isnād mursal", "que l’isnād soit mursal" in html)
chk("tamhīd double question", "Quel est donc le sens du ḥadīṯ mursal" in html and "le statut de l’argumentation par lui" in html)

# bayt + glose
chk("bayt hémistiche 1 translittéré", "wa-mursalun minhu aṣ-ṣaḥābiyyu saqaṭa" in html)
chk("bayt second hémistiche points", "second hémistiche" in html and "points de suite" in html)
chk("bayt tranché image 2400 dpi", "tranché par l’image à 2400 dpi" in html)
chk("blanc jamais reconstitué", "tenu tel qu’imprimé, jamais reconstitué" in html)
chk("bandeau al-matn cité", "« al-matn »" in html)
chk("glose iʾrsāl iṭlāq", "de l’iʾrsāl (l’envoi libre), lequel est l’iṭlāq" in html)
chk("bandeau aš-šarḥ cité", "« aš-šarḥ »" in html)
chk("bandeaux tranchés 3000 dpi", "tranchés à 3000 dpi" in html)
chk("agencement p.69 miroir", "même agencement qu’en p.69 pour le mawqūf" in html)

# extraction des thèmes (istikhlāṣ al-maḍāmīn)
chk("extraction istikhlāṣ al-maḍāmīn", "extraction des contenus (istikhlāṣ al-maḍāmīn)" in html)
chk("extraction 2 questions", "sous la forme de deux questions" in html)
chk("question 1 المقصود", "Qu’entend-on par le ḥadīṯ mursal" in html)
chk("question 2 حكم الاحتجاج", "Quel est le statut de l’argumentation par le ḥadīṯ mursal" in html)
chk("extraction relue 1600 dpi p.73", "relues à l’image à 1600 dpi en tête de la page 73" in html)

# analyse : définition + āya
chk("analyse contient ce qui suit", "Cette leçon contient ce qui suit" in html)
chk("premièrement définition", "Premièrement : la définition du ḥadīṯ mursal" in html)
chk("āya translittérée imprimé", "ʾannā ʾakūnu lī ġulāmun wa-kānatimraʾatī ʿāqiran wa-ʾinnī halaktu ʾaw kabiran" in html)
chk("marqueur imprimé 84 coquille", "« 84 » de l’imprimé est une coquille" in html)
chk("cache canonique 19:8", re.search(r"cache canonique 19\s*:8", html))
chk("correspondance par le texte", "correspondance par le texte" in html)
chk("doctrine R511 citée", "doctrine R511" in html and "R560/R569" in html)
chk("écart ʾakūnu/yakūnu déclaré", "« ʾakūnu »" in html and "« yakūnu »" in html)
chk("écart hémistiche final déclaré", "« wa-ʾinnī halaktu ʾaw kabiran »" in html and "« wa-qad balaġtu mina l-kibari ʿitiyyan »" in html)
chk("āya rendue du cache", re.search(r"rendue du cache canonique 19\s*:8 pour la portion imprimée", html))
chk("iṭlāq élargit l'isnād", "avait élargi l’isnād et ne l’avait point restreint" in html)
chk("définition 1 saḥābī tombé", "dont le Compagnon tomba" in html)
chk("définition 1 kināya", "par allusion (kināya)" in html)
chk("définition 1 Abū Ḥāzim + Yaḥyā b. Saʿīd", "Abū Ḥāzim et Yaḥyā b. Saʿīd al-Anṣārī" in html)
chk("définition 1 Ibn al-Musayyib + Qays b. Abī Ḥāzim", "Ibn al-Musayyib et Qays b. Abī Ḥāzim" in html)
chk("définition 1 célèbre al-Ḥākim", "le célèbre parmi les muḥaddithūn" in html and "par lui trancha al-Ḥākim" in html)
chk("Ibn Ḥajar restriction", "le ḥāfiẓ Ibn Ḥajar le restreignit" in html)
chk("aṭ-Ṭanūḫī Héraclius", "aṭ-Ṭanūḫī, l’envoyé de Héraclius" in html)
chk("mursal du Compagnon connecté", "le mursal du Compagnon, car il est connecté en isnād" in html)
chk("tous ʿudūl", "ils sont tous justes (ʿudūl)" in html)
chk("définition 2 grand Tābiʿī", "ce que le grand Tābiʿī éleva au Prophète ﷺ" in html)
chk("définition 2 munqaṭiʿ", "point mursal mais munqaṭiʿ (interrompu)" in html)
chk("définition 2 Ibn ʿAbd al-Barr", "rapporté par Ibn ʿAbd al-Barr" in html)
chk("définition 2 un ou les deux", "que l’un ou les deux" in html)
chk("définition 3 un ou plusieurs", "un transmetteur, ou plusieurs" in html)
chk("définition 3 début/fin/entre", "de son début, de sa fin ou entre les deux" in html)
chk("définition 3 muʿḍal/muʿallaq", "le munqaṭiʿ, le muʿḍal et le muʿallaq" in html)
chk("définition 3 Ibn aṣ-Ṣalāḥ + an-Nawawī", "Ibn aṣ-Ṣalāḥ et an-Nawawī d’après les fuqahāʾ et les uṣūlīyūn" in html)
chk("définition 3 al-Ḫaṭīb", "jugea ferme al-Ḫaṭīb" in html)

# analyse : statut de l'argumentation
chk("deuxièmement argumentation", "Deuxièmement : le statut de l’argumentation par le ḥadīṯ mursal" in html)
chk("Abū Ḥanīfa/Mālik/Aḥmad", "Abū Ḥanīfa, Mālik et Aḥmad" in html)
chk("éloge de l'ère des Tābiʿīn", "fit l’éloge de l’ère des Tābiʿīn" in html)
chk("deux générations", "les deux générations après la génération des Compagnons" in html)
chk("la plupart des gens du ḥadīṯ refusent", "la plupart des gens du ḥadīṯ à ce que le mursal est faible" in html)
chk("méconnaissance du tombé", "la méconnaissance de celui qui tomba dans l’isnād" in html)
chk("chaîne des doutes", "il est possible qu’il fût tābiʿī" in html and "il est possible qu’il fût faible" in html)
chk("ʿaqlan + istiqrāʾ", "par la raison et par six ou sept inductions" in html)
chk("aṣ-Suyūṭī cité", "Aṣ-Suyūṭī dit" in html)
chk("ʿurifa tranché 1400 dpi", "« lu ʿurifa »" in html and "tranchée par l’image à 1400 dpi" in html)
chk("ġarafa OCR récusé", "« ġarafa » de l’OCR 300 dpi récusé" in html)
chk("lam yuraḏḏ", "lam yuraḏḏ" in html)
chk("attestation homme ambigu", "l’attestation de l’homme ambigu n’est point suffisante" in html)
chk("consolidation + soutien", "quand sa consolidation et son soutien s’accomplissent" in html)

# rappel
chk("rappel 2 questions", "le rappel (at-taqwīm) sous la forme de deux questions" in html)
chk("rappel définition", "Quelle est la définition du ḥadīṯ mursal" in html)
chk("rappel relue 2400 dpi p.74", "relues à l’image à 2400 dpi en bas de la page 74" in html)

# exploitation
chk("exploitation 2 textes Muwaṭṭaʾ", "deux textes rapportés par l’imām Mālik dans son Muwaṭṭaʾ" in html)
chk("texte 1 Nāfiʿ + ʿaqīqa", "d’après Nāfiʿ" in html and "ʿaqīqa (immolation pour le nouveau-né)" in html)
chk("texte 1 bišātin šātan imprimé", "wa-kāna yaʿuqqu ʿan waladihi bišātin šātan" in html)
chk("texte 1 écart déclaré", "micro-forme imprimée « bišātin šātan » portée telle quelle" in html)
chk("texte 1 renvoi kitāb al-ʿaqīqa", "[kitāb al-ʿaqīqa ; bāb al-ʿamal fī al-ʿaqīqa]" in html)
chk("texte 2 ʿAbd ar-Raḥmān b. Harmala", "ʿAbd ar-Raḥmān b. Harmala al-Aslamī" in html)
chk("texte 2 Saʿīd b. al-Musayyib", "d’après Saʿīd b. al-Musayyib" in html)
chk("texte 2 matn fiṭr", "lā yazālu n-nāsu bi-ḫayrin mā ʿaǧǧalū l-fiṭr" in html)
chk("texte 2 renvoi kitāb aṣ-ṣiyām", "[kitāb aṣ-ṣiyām ; bāb mā ǧāʾa fī l-fiṭr]" in html)
chk("activité deux textes", "J’étudie les deux textes et je précise le type des deux ḥadīṯs" in html)

# préparation préalable + bornes
chk("préparation ġarīb q1", "qu’est-ce que le ḥadīṯ ġarīb" in html)
chk("préparation ġarīb q2", "les types de la ġarāba (solitude) dans l’isnād et le matn" in html)
chk("bornes déclarées 72/75", "s’ouvre en la page imprimée 72 et s’achève en la page 75" in html)
chk("leçon suivante p.76", "la leçon suivante (le ḥadīṯ ġarīb) ouvre en la page 76" in html)
chk("objectifs ġarīb p.76 concordants", "ses objectifs imprimés (le concept du ḥadīṯ ġarīb et ses divisions)" in html)
chk("borne par sondage jamais devinée", "la borne fut tranchée par le sondage ; jamais devinée" in html)
chk("leçon suivante interdite double rendu", "est interdite de double rendu" in html)

print(f"\n{ok}/{ok+fail} PASS")
exit(1 if fail else 0)

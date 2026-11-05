#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Minhāj — Vérification de la leçon ulum-hadith-tanawi-1 / pdf-mut23h2q-123
(le ḥadīṯ ʿālī et le ḥadīṯ nāzil des isnāds, p.64-67 du manuel
ulum-hadith-1-thanawi.pdf) : contrôle de contenu — bannière « leçon 12 :
le ḥadīṯ ʿālī et le ḥadīṯ nāzil des isnāds » (lue image 1200 dpi, preuve
commise R588), bayt du nāẓim « wa-kullu mā qultu riǧālahu ʿalā *
wa-ḍiduhu ḏāka allaḏī qad nazalā » (tranché image 1800 dpi, tenu tel
qu'imprimé avec sa vocalisation « qultu » déclarée, double occurrence
boîte p.64/citation p.66 concordante consignée), gloses « al-murtafiʿ »
(récupérée recadrage 1600 dpi, OCR 300 dpi omise) et « le contraire du
ʿālī », extraction des thèmes (deux items), ʿuluww absolu (al-ġāya
al-quṣwā, menteur) et relatif (ḥifẓ/ḍabṭ/composition ; taqaddum as-samāʿ
tranché image 1200 dpi, « btaqām » OCR récusé ; antériorité entre deux
narrateurs), nāzil par le contraire (Ibn al-Ṣalāḥ), nuẓūl absolu
(multiplicité des intermédiaires) et relatif (Six Livres ; tardiveté de
l'audition ; tardiveté de la mort), rappel ×3, exploitation (Muwaṭṭaʾ
Nāfiʿ/Ibn ʿUmar vingt-sept degrés ; Sunan al-Bayhaqī isnād tranché image
2000 dpi — al-ʿAṭṭār tāʾ redoublée, « al-ʿAḍḍār » ḍād OCR récusé ;
al-Šāfiʿī confirmé 1200 dpi, « al-āfiʿī » OCR récusé ; Abī al-Zinād,
al-Aʿraǧ, Abū Hurayra confirmés — vingt-cinq parts ; références tenues
imprimées ; trois questions d'examen), préparation préalable → mawqūf
deux questions, bornes p.64-67 TRIPLE PREUVE (objectifs p.64 ; rappel/
exploitation p.67 ; إعداد p.68 → mawqūf ; bannière leçon 13 p.69 lue
image 1200 dpi [preuve commise]).
Usage: python3 scripts-translate/verify-ulumhadith1-pdf123.py
"""
import re

HTML = "/home/z/my-project/tr-tmp/lesson-ulumhadith1-pdf-mut23h2q-123-fr.html"

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
chk("h1 leçon 12", "leçon 12" in html and "<h1>" in html)
chk("h1 = registre titleFr", html.startswith("<h1>Le hadith à chaîne haute (ʿālī)"))
chk("lesson-meta présent", 'class="lesson-meta"' in html and "Source du cours" in html)
chk("bornes pages 64 à 67 citées", "pages 64 à 67" in html)
chk("bannière leçon 12 lue", "leçon 12 : le ḥadīṯ ʿālī et le ḥadīṯ nāzil des isnāds" in html)
chk("bannière 1200 dpi preuve", "fut lue à l’image 1200 dpi [preuve commise]" in html)
chk("provenance OCR tesseract 300 dpi", "OCR tesseract arabe local à 300 dpi" in html)
chk("adjudication 1200 puis 1600 et 2000 dpi", "à 1200 puis 1600 et 2000 dpi" in html)
chk("miroir archive.org item", "item 1_20220304_20220304_2251" in html)
chk("chaîne R578-R588 (suite de R588)", "R588" in html)
chk("cache R588 pré-seedé déclaré", "pré-seedées du cache R588" in html)

# objectifs
chk("objectif 1 concept ʿālī/nāzil", "Que je reconnaisse le concept du ḥadīṯ ʿālī et du ḥadīṯ nāzil" in html)
chk("objectif 2 distinguer isnād", "Que je distingue le ḥadīṯ à l’isnād élevé du ḥadīṯ à l’isnād abaissé" in html)
chk("objectif 3 supériorité", "Que je ressente la supériorité du ḥadīṯ ʿālī sur le ḥadīṯ nāzil" in html)

# tamhīd
chk("tamhīd fin du premier siècle", "ne fut point mise en recueil qu’à la fin du premier siècle" in html)
chk("tamhīd chaîne de narrateurs", "le canal d’une chaîne de narrateurs" in html)
chk("tamhīd double question", "un nombre plus grand de narrateurs" in html)

# bayt + glose
chk("bayt hémistiche 1 translittéré", "wa-kullu mā qultu riǧālahu ʿalā" in html)
chk("bayt hémistiche 2 translittéré", "wa-ḍiduhu ḏāka allaḏī qad nazalā" in html)
chk("bayt tranché image 1800 dpi", "tranché par l’image à 1800 dpi" in html)
chk("qultu tenu imprimé forme déclarée", "« qultu » (sukūn sur le lām, ḍamma sur le tāʾ), forme déclarée" in html)
chk("astérisques séparent les hémistiches", "les astérisques séparent les hémistiches" in html)
chk("double occurrence concordante", "double occurrence concordante consignée" in html)
chk("glose murtafiʿ", "le surélevé (al-murtafiʿ)" in html)
chk("glose ʿalā yaʿlū ʿuluwwan", "« ʿalā, yaʿlū, ʿuluwwan »" in html)
chk("glose récupérée 1600 dpi", "[glose récupérée au recadrage 1600 dpi, l’OCR 300 dpi l’ayant omise]" in html)
chk("glose nāzil contraire", "le contraire du ʿālī" in html)

# extraction + analyse
chk("extraction deux thèmes", "l’extraction imprimée des deux thèmes" in html)
chk("extraction tenue telle quelle", "extraction imprimée tenue telle quelle" in html)
chk("analyse contient ce qui suit", "Cette leçon contient ce qui suit" in html)

# ʿālī : définition + degrés
chk("citation bayt tranchée 1800", "[citation tranchée par l’image à 1800 dpi]" in html)
chk("définition peu nombreux", "celui dont le nombre des hommes de l’isnād fut peu nombreux" in html)
chk("ʿuluww absolu et relatif", "un ʿuluww absolu et un ʿuluww relatif" in html)
chk("ʿuluww absolu snd exact ġāya", "il fut le degré suprême (al-ġāya al-quṣwā)" in html)
chk("ʿuluww absolu menteur", "surtout s’il contient un menteur" in html)
chk("ʿuluww relatif ḥifẓ ḍabṭ", "la mémoire (ḥifẓ), la précision (ḍabṭ)" in html)
chk("ʿuluww antériorité audition shaykh", "celui qui entendit anciennement fut plus élevé" in html)
chk("ʿuluww antériorité entre narrateurs", "même si la mort du second avança" in html)
chk("taqadduma tranché 1200", "tranchés par l’image à 1200 dpi" in html)
chk("btaqām OCR récusé", "« btaqām » de l’OCR 300 dpi récusé" in html)

# nāzil : définition + degrés
chk("définition par le contraire", "la définition par le contraire" in html)
chk("Ibn al-Ṣalāḥ énonça", "Ibn al-Ṣalāḥ l’énonça expressément" in html)
chk("nuẓūl absolu multiplicité intermédiaires", "l’éloignement du Messager de Dieu ﷺ par la multiplicité des intermédiaires" in html)
chk("nuẓūl relatif imām", "la multiplicité des intermédiaires jusqu’à un imām" in html)
chk("nuẓūl Six Livres", "une voie autre que les Six Livres" in html)
chk("nuẓūl tardiveté audition", "celui qui entendit tardivement fut plus abaissé" in html)
chk("nuẓūl tardiveté mort", "la tardiveté de la mort du narrateur en cet isnād" in html)

# rappel
chk("rappel 3 items", "J’expose le ḥadīṯ ʿālī et ses degrés" in html and "Quelle est l’utilité de distinguer le ḥadīṯ ʿālī et le ḥadīṯ nāzil" in html)

# exploitation : Muwaṭṭaʾ 27
chk("exploitation Muwaṭṭaʾ Nāfiʿ Ibn ʿUmar", "d’après Nāfiʿ, d’après ʿAbd Allāh b. ʿUmar" in html)
chk("vingt-sept degrés", "vingt-sept degrés (bisabʿ wa-ʿišrīn daraja)" in html)
chk("référence Muwaṭṭaʾ tenue imprimée", "kitāb aṣ-ṣalāh ; bāb : la supériorité de la prière en commun sur la prière de l’individu" in html)
chk("nombre 27 confirmé 1200", "le nombre vingt-sept confirmé à l’image 1200 dpi" in html)

# exploitation : Bayhaqī 25
chk("Bayhaqī Sunan", "al-Bayhaqī rapporta en ses Sunan" in html)
chk("isnād al-Ḥāfiẓ", "Abū ʿAbd Allāh al-Ḥāfiẓ" in html)
chk("isnād Abū Bakr b. al-Ḥasan", "Abū Bakr b. al-Ḥasan" in html)
chk("isnād Abū Zakariyyā", "Abū Zakariyyā b. Abī Isḥāq" in html)
chk("isnād al-ʿAṭṭār", "Abū Ṣādiq Muḥammad b. Aḥmad al-ʿAṭṭār" in html)
chk("isnād Muḥammad b. Yaʿqūb", "Abū al-ʿAbbās Muḥammad b. Yaʿqūb" in html)
chk("isnād al-Rabīʿ b. Sulaymān", "al-Rabīʿ b. Sulaymān" in html)
chk("isnād al-Šāfiʿī", "al-Šāfiʿī" in html)
chk("isnād Abī al-Zinād", "Abī al-Zinād" in html)
chk("isnād al-Aʿraǧ", "al-Aʿraǧ" in html)
chk("isnād Abū Hurayra", "Abū Hurayra" in html)
chk("isnād tranché image 2000 dpi", "tranché par l’image à 2000 dpi" in html)
chk("al-ʿAṭṭār tenu imprimé", "« al-ʿAṭṭār » (tāʾ redoublée) tenu tel qu’imprimé" in html)
chk("al-ʿAḍḍār OCR récusé", "« al-ʿAḍḍār » (ḍād) de l’OCR 300 dpi récusé" in html)
chk("al-āfiʿī OCR récusé Šāfiʿī confirmé", "l’« al-āfiʿī » de l’OCR 300 dpi récusé" in html and "confirmé à 1200 dpi" in html)
chk("OCR 300 récusable الزناد/الأعرج/أبي هريرة", "az-zatad" in html and "al-aġarr" in html and "bī murayraq" in html)
chk("vingt-cinq parts", "vingt-cinq parts (bi-ḫamsa wa-ʿišrīn ǧuzʾ)" in html)
chk("référence Bayhaqī tenue imprimée", "Sunan al-Bayhaqī ; kitāb aṣ-ṣalāh ; bāb : ce qui vint en la supériorité de la prière en commun" in html)
chk("examen trois questions", "J’examine les deux textes et je réponds à ce qui suit" in html and "je détermine le type du ʿuluww ou du nuẓūl" in html)

# préparation préalable + bornes
chk("préparation p.68 annonce mawqūf", "la préparation préalable imprimée de la présente leçon (p.68) annonce expressément le mawqūf par ses deux questions" in html)
chk("bannière leçon 13 p.69 preuve", "« leçon 13 : le ḥadīṯ mawqūf » et son badge « al-dars 13 » y furent lus à l’image 1200 dpi [preuve commise]" in html)
chk("borne jamais devinée", "la borne fut tranchée par le sondage ; jamais devinée" in html)
chk("bornes 64 → 67", "s’ouvre en la page imprimée 64 et s’achève en la page 67" in html)
chk("leçon suivante page 69", "ouvre en la page 69 du même manuel" in html)
chk("mawqūf suspendu glosé", "le ḥadīṯ mawqūf (suspendu)" in html)

# 0 citation coranique
chk("0 citation coranique (cache non sollicité)", "cache coranique n’est pas sollicité" in html)

# rasm nu interdit + double rendu interdit
chk("rasm nu interdit", "rasm nu" not in html)
chk("interdit de double rendu déclaré", "interdite de double rendu" in html)

print(f"verify-ulumhadith1-pdf123 : {ok}/{ok+fail} PASS")
raise SystemExit(1 if fail else 0)

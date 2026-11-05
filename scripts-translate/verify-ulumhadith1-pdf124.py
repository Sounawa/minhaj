#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Minhāj — Vérification de la leçon ulum-hadith-tanawi-1 / pdf-mut23h2q-124
(le ḥadīṯ mawqūf, p.69-71 du manuel ulum-hadith-1-thanawi.pdf) :
contrôle de contenu — bannière « leçon 13 : le ḥadīṯ mawqūf » (relue image
1500 dpi, preuve commise R589 à 1200 dpi), bayt du nāẓim « wa-mā uḍīfa ilā
l-aṣḥābi min * qawlin wa-fiʿlin fa-hwa mawqūfun zakan » (tranché image
2400 dpi, tenu tel qu'imprimé : tāʾ de « uḍīfa », pluriel « ilā l-aṣḥābi »,
« zakan » fatḥa-zāy/sukūn-nūn ; double occurrence p.69/p.70 consignée),
glose « az-zukn : ʿalima » (double lecture visuelle 1800+3000 dpi,
« ġulima » OCR récusé), extraction des contenus (2 questions, « mulāhaẓāt »
tranché image 3000 dpi, « maẓāna » OCR récusé), définition (āthar/khabar,
an-Nawawī at-Taqrīb ; extension aux tābiʿīn avec restriction ʿAṭāʾ/Muǧāhid/
Mālik), conditions (ijtihād ; al-Ḥākim muttaṣil vs masse des muḥaddithūn ;
ǧawāmiʿ/maṣānīf : Ibn Abī Shayba, ʿAbd ar-Razzāq, Ibn Ǧarīr, Ibn Abī Ḥātim,
Ibn al-Munḏir ; kitāb al-Wuqūf ʿalā al-mawqūf d'Ibn Badr al-Mawṣilī),
rappel ×3, exploitation (2 bayts d'al-ʿIrāqī tranchés image 3000 dpi —
« wa-ʿadu » fatḥa-ʿayn/ḍamma-dāl tenu imprimé, « ʿalā l-asbābi » alif
hamzée, parenthèse en deux mots ; 2 questions dont « yuballiġu bihi
n-nabiyya ﷺ »), préparation préalable → mursal deux questions, bornes
p.69-71 (objectifs + bannière p.69 ; rappel/exploitation/préparation p.71 ;
objectifs mursal p.72 OCR 300 dpi concordants).
Usage: python3 scripts-translate/verify-ulumhadith1-pdf124.py
"""
import re

HTML = "/home/z/my-project/tr-tmp/lesson-ulumhadith1-pdf-mut23h2q-124-fr.html"

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
chk("h1 leçon 13", "leçon 13" in html and "<h1>" in html)
chk("h1 = registre titleFr", html.startswith("<h1>Le hadith suspendu (mawqūf)"))
chk("lesson-meta présent", 'class="lesson-meta"' in html and "Source du cours" in html)
chk("bornes pages 69 à 71 citées", "pages 69 à 71" in html)
chk("bannière leçon 13 citée", "leçon 13 : le ḥadīṯ mawqūf" in html)
chk("bannière relue 1500 dpi + preuve R589", "fut relue à l’image 1500 dpi [preuve commise R589 à 1200 dpi]" in html)
chk("badge al-dars 13", "badge « al-dars 13 »" in html)
chk("provenance OCR tesseract 300 dpi", "OCR tesseract arabe local à 300 dpi" in html)
chk("adjudication 1200 puis 1500…3000 dpi", "à 1200 puis 1500, 1600, 1800, 2400 et 3000 dpi" in html)
chk("miroir archive.org item", "item 1_20220304_20220304_2251" in html)
chk("chaîne (suite de R589)", "R589" in html)
chk("cache R589 pré-seedé déclaré", "pré-seedées du cache R589" in html)

# objectifs
chk("objectif 1 concept mawqūf", "Que je reconnaisse le concept du ḥadīṯ mawqūf" in html)
chk("objectif 2 distinguer ressemblants", "Que je distingue le ḥadīṯ mawqūf de ce qui lui ressemble" in html)
chk("objectif 3 Sunna des Compagnons", "Que je me laisse guider par la Sunna des Compagnons" in html)

# tamhīd
chk("tamhīd division par l'aboutissement", "considéré celui vers qui il aboutit" in html)
chk("tamhīd triade marfūʿ/maqtūʿ/mawqūf", "en marfūʿ (élevé), en maqtūʿ (interrompu) et en mawqūf (suspendu)" in html)
chk("tamhīd deux premiers types en détail", "le propos a déjà été tenu en détail sur les deux premiers types" in html)
chk("tamhīd double question", "Quel est donc le sens du ḥadīṯ mawqūf" in html and "quels sont ses types" in html)

# bayt + glose
chk("bayt hémistiche 1 translittéré", "wa-mā uḍīfa ilā l-aṣḥābi min" in html)
chk("bayt hémistiche 2 translittéré", "qawlin wa-fiʿlin fa-hwa mawqūfun zakan" in html)
chk("bayt tranché image 2400 dpi", "tranché par l’image à 2400 dpi" in html)
chk("tāʾ de uḍīfa tenu imprimé", "muni d’un tāʾ après le fāʾ (lettre tenue telle quelle)" in html)
chk("pluriel ilā l-aṣḥābi déclaré", "« ilā l-aṣḥābi » au pluriel" in html)
chk("zakan fatḥa-zāy sukūn-nūn", "« zakan » (fatḥa sur le zāy, sukūn sur le nūn)" in html)
chk("astérisques séparent les hémistiches", "les astérisques séparent les hémistiches" in html)
chk("double occurrence p.69/p.70", "double occurrence consignée" in html and "revient en p.70 à l’ouverture de la définition" in html)
chk("glose ism mafʿūl", "nom d’objet passif (ism mafʿūl) dérivé du waqf" in html)
chk("glose zukn ʿalima tenu imprimé", "« ʿalima » — forme imprimée tenue telle quelle" in html)
chk("ġulima OCR récusé", "« ġulima » de l’OCR 300 et 1200 dpi récusé" in html)
chk("glose tranchée 1800 puis 3000 dpi", "double lecture visuelle à 1800 puis 3000 dpi" in html)
chk("glose nāẓim complète le bayt", "pour compléter le bayt" in html)

# extraction des thèmes (istikhlāṣ al-maḍāmīn)
chk("extraction istikhlāṣ al-maḍāmīn", "extraction des contenus (istikhlāṣ al-maḍāmīn)" in html)
chk("extraction 2 questions", "sous la forme de deux questions" in html)
chk("question 1 mawqūf", "Qu’est-ce que le ḥadīṯ mawqūf" in html)
chk("question 2 conditions + mulāhaẓāt", "Qu’exige-t-on du ḥadīṯ mawqūf et quelles sont ses observations (mulāhaẓāt)" in html)
chk("mulāhaẓāt tranché 3000 dpi", "« mulāhaẓāt » de la seconde tranché par l’image à 3000 dpi" in html)
chk("maẓāna OCR récusé", "« maẓāna » de l’OCR 300 dpi récusé" in html)

# analyse : définition
chk("analyse contient ce qui suit", "Cette leçon contient ce qui suit" in html)
chk("premièrement définition", "Premièrement : la définition du ḥadīṯ mawqūf" in html)
chk("définition attribué au Compagnon", "le ḥadīṯ qui fut attribué au Compagnon, de son dire ou de son acte" in html)
chk("définition sans statut rafʿ", "auquel ne s’appliqua point le statut du rafʿ" in html)
chk("définition isnād connecté ou interrompu", "que son isnād fût connecté jusqu’à lui ou qu’il fût interrompu" in html)
chk("shāfiʿītes āthar/khabar", "nommèrent le ḥadīṯ mawqūf « āthar »" in html and "« khabar » (information)" in html)
chk("an-Nawawī at-Taqrīb", "comme an-Nawawī l’établit en at-Taqrīb" in html)
chk("extension tābiʿīn licite", "pour ce qui fut rapporté des tābiʿīn ou de ceux qui vinrent après eux — ce qui est licite" in html)
chk("restriction ʿAṭāʾ/Muǧāhid/Mālik", "« mawqūf ʿalā ʿAṭāʾ »" in html and "« un tel l’arrêta sur Muǧāhid (waqafahu fulānun ʿalā Muǧāhid) »" in html and "« mawqūf ʿalā Mālik »" in html)

# analyse : conditions
chk("deuxièmement conditions + observations", "Deuxièmement : les conditions du ḥadīṯ mawqūf et ses observations" in html)
chk("condition ijtihād", "qu’il relève de l’ijtihād" in html)
chk("non-ijtihād statut rafʿ", "il reçoit le statut du rafʿ, comme il précéda pour le ḥadīṯ marfūʿ en son statut" in html)
chk("al-Ḥākim muttaṣil", "al-Ḥākim — que Dieu lui fasse miséricorde — exigea du ḥadīṯ mawqūf qu’il fût connecté (muttaṣil)" in html)
chk("masse des muḥaddithūn contredit", "la masse des muḥaddithūn le contredirent en cette condition" in html)
chk("connexion non condition", "la connexion n’est point une condition du ḥadīṯ mawqūf" in html)
chk("ǧawāmiʿ/maṣānīf", "dans les ǧawāmiʿ et les recueils (maṣānīf)" in html)
chk("Muṣannaf Ibn Abī Shayba", "Muṣannaf d’Ibn Abī Shayba" in html)
chk("Muṣannaf ʿAbd ar-Razzāq", "Muṣannaf de ʿAbd ar-Razzāq" in html)
chk("tafsīr Ibn Ǧarīr/Ibn Abī Ḥātim/Ibn al-Munḏir", "Ibn Ǧarīr, d’Ibn Abī Ḥātim et d’Ibn al-Munḏir" in html)
chk("Ibn Badr al-Mawṣilī al-Wuqūf ʿalā al-mawqūf", "Ibn Badr al-Mawṣilī y composa un livre qu’il nomma « al-Wuqūf ʿalā al-mawqūf »" in html)

# rappel
chk("rappel 3 items", "Quelle est la définition du ḥadīṯ mawqūf ? Et quelles sont ses conditions" in html and "J’expose la différence entre le ḥadīṯ marfūʿ, le maqtūʿ et le mawqūf" in html and "la relation entre le ḥadīṯ mawqūf et le ḥadīṯ connecté (muttaṣil)" in html)

# exploitation : 2 bayts d'al-ʿIrāqī
chk("al-ʿIrāqī ḥāfiẓ", "Le ḥāfiẓ al-ʿIrāqī — que Dieu lui fasse miséricorde — dit" in html)
chk("bayts tranchés image 3000 dpi", "deux bayts tranchés par l’image à 3000 dpi" in html)
chk("wa-ʿadu tenu imprimé", "« wa-ʿadu » (fatḥa sur ʿayn, ḍamma sur dāl) tenu tel qu’imprimé" in html)
chk("ʿalā l-asbābi alif hamzée", "« ʿalā l-asbābi » portant l’alif hamzée de l’imprimé" in html)
chk("parenthèse deux mots imprimé", "la seconde parenthèse en deux mots à l’imprimé" in html)
chk("bayt 1 fas-sarahu aṣ-ṣaḥābī", "mā fas-sarahu aṣ-ṣaḥābī" in html)
chk("bayt 1 maḥmūlun", "fa-huwa maḥmūlun" in html)
chk("bayt 2 yarfaʿuhu", "yarfaʿuhu" in html)
chk("bayt 2 yuballiġu bihi", "yuballiġu bihi" in html)
chk("bayt 2 riwāyatun yunmīhi", "riwāyatun" in html and "yunmīhi" in html)
chk("bayt 2 fa-ntabih", "fa-ntabih" in html)
chk("examen des deux bayts", "J’examine le sens des deux bayts en l’un des commentaires de l’Alfiyya d’al-ʿIrāqī" in html)
chk("question tafsīr marfūʿ/mawqūf", "L’exposé du Compagnon (tafsīruhu) relève-t-il du statut du marfūʿ ou du mawqūf" in html)
chk("question trio + ﷺ", "« il l’éleva (yarfaʿuhu) »" in html and "« il l’attribue vers le haut (yunmīhi) »" in html and "« il transmet jusqu’au Prophète ﷺ (yuballiġu bihi n-nabiyya) »" in html)

# préparation préalable + bornes
chk("préparation mursal", "qu’est-ce que le ḥadīṯ mursal (avancé)" in html and "la position des muḥaddithūn envers le ḥadīṯ mursal" in html)
chk("préparation p.71 annonce mursal", "la préparation préalable imprimée de la présente leçon (p.71) qui annonce expressément le mursal par ses deux questions" in html)
chk("borne jamais devinée", "la borne fut tranchée par le sondage ; jamais devinée" in html)
chk("bornes 69 → 71", "s’ouvre en la page imprimée 69 et s’achève en la page 71" in html)
chk("leçon suivante page 72", "ouvre en la page 72 du même manuel" in html)
chk("objectifs mursal p.72 OCR 300", "les objectifs imprimés de la leçon 14 (le concept du ḥadīṯ mursal et le statut de l’agir par lui) ouvrent en p.72" in html)

# 0 citation coranique
chk("0 citation coranique (cache non sollicité)", "cache coranique n’est pas sollicité" in html)

# rasm nu interdit + double rendu interdit
chk("rasm nu interdit", "rasm nu" not in html)
chk("interdit de double rendu déclaré", "interdite de double rendu" in html)

print(f"verify-ulumhadith1-pdf124 : {ok}/{ok+fail} PASS")
raise SystemExit(1 if fail else 0)

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Minhāj — Vérification de la leçon ulum-hadith-tanawi-2 / pdf-mut23h2u-255
(الدرس 1 — at-taʿrīf bi-l-ḥāfiẓ Ibn Ḥaǧar wa-kitābihi Nuḫbat al-fikr, p.11-16
du manuel ulum-hadith-2-thanawi_text.pdf) : OUVERTURE DU LIVRE 2 ; bornes
p.11-16 par DOUBLE sondage (p.11 = objectifs + tamhīd ; p.16 = al-iʿdād al-qablī ;
p.17 = objectifs leçon 2) ; nombres de la couche INVERSÉS tranchés par OCR
300 dpi (852/463/405/430/544/773/777/785/797) ; citation as-Saḫāwī tranchée par
RECADRAGE 600 dpi (lecture image intégrale, référence 2/956 confirmée) ;
muqaddima de la Naḫba rendue de l'imprimé ; zéro āya, zéro hadith prophétique,
zéro résidu arabe, zéro apostrophe droite, zéro doublon.
Usage: python3 scripts-translate/verify-ulumhadith2-pdf255.py
"""
import json
import re

HTML = "/home/z/my-project/tr-tmp/lesson-uh2-pdf-mut23h2u-255-fr.html"
REG = "/home/z/my-project/content/books/ulum-hadith-tanawi-2.json"
REG1 = "/home/z/my-project/content/books/ulum-hadith-tanawi-1.json"

ok, fail = 0, 0


def chk(label, cond):
    global ok, fail
    if cond:
        ok += 1
    else:
        fail += 1
        print(f"ÉCHEC : {label}")


h = open(HTML, encoding="utf-8").read()
hn = re.sub(r" +", " ", h.replace("&nbsp;", " ").replace("\u202f", "").replace("\u2009", ""))

# ---- h1 et méta
chk("h1 = titleFr pré-mappé « Leçon 1 : Présentation du ḥāfiẓ Ibn Ḥaǧar et de son ouvrage Nuḫbat al-Fikr »",
    hn.startswith("<h1>Leçon 1 : Présentation du ḥāfiẓ Ibn Ḥaǧar et de son ouvrage Nuḫbat al-Fikr"))
chk("h1 mentionne deuxième année", "deuxième année" in h[:500])
chk("h1 mentionne Naḫba", "Naḫba" in h[:500])
chk("dl.lesson-meta présent", '<dl class="lesson-meta">' in h and "<dt>Source du cours</dt>" in h)
chk("item archive.org cité", "1_20220304_20220304_2251" in h)
chk("source locale citée", "ulum-hadith-2-thanawi_text.pdf" in h)
chk("bornes p.11-16 documentées", "pages 11 à 16" in h)
chk("p.17 leçon 2 non touchée", "pdf-mut23h2u-256" in h and "non touché" in h)
chk("double sondage « jamais devinées »", "jamais devinées" in h)
chk("bannière tenue par triple concordance", "triple concordance documentée" in h)
chk("caches OCR cités", "tr-tmp/r613/p-011.txt" in h)
chk("tessdata retéléchargé documenté", "tessdata ara retéléchargé" in h)
chk("inversions nombres documentées (258→852)", "la couche écrit" in hn and "258" in hn and "852" in hn)
chk("inversions documentées (364→463, 504→405, 034→430)", "463" in hn and "405" in hn and "430" in hn)
chk("références 1/421 et 2/956 documentées", "1/421" in hn and "2/956" in hn)
chk("recadrage 600 dpi documenté", "RECADRAGE 600 dpi" in hn or "600 dpi" in hn)
chk("crop cité", "crop-p16-sakawi.png" in h)
chk("zéro āya rendue", "Aucune āya rendue" in h)
chk("zéro hadith prophétique cité", "aucun ḥadīṯ prophétique cité" in h)

# ---- objectifs
chk("objectif : compilateurs et leurs ouvrages", "compilateurs (al-muṣannifūn)" in hn)
chk("objectif : vie d’Ibn Ḥaǧar", "qu’il connaisse la vie du ḥāfiẓ Ibn Ḥaǧar" in hn)
chk("objectif : raison de la composition", "raison de la composition de la « Nuḫbat al-fikr »" in hn)
chk("objectif : niyya et ādāb", "purifie l’intention (al-niyya)" in hn and "manières (ādāb)" in hn)

# ---- tamhīd
chk("tamhīd : taṣānīf multipliés", "en la terminologie du ḥadīṯ se sont multipliées" in hn)
chk("tamhīd : šawārid al-farāʾid", "perles éparses (šawārid al-farāʾid)" in hn)
chk("tamhīd : Nuzhat an-naẓar nommée", "Nuzhat an-naẓar šarḥ Nuḫbat al-fikr" in hn)
chk("tamhīd : triple question", "trois questions qui orientent la leçon" in hn)

# ---- muqaddima (texte)
chk("muqaddima : ouverture louange", "Louange à Dieu qui ne cesse d’être savant et puissant" in hn)
chk("muqaddima : annonciateur et avertisseur", "en annonciateur et en avertisseur" in hn)
chk("muqaddima : salut abondant", "salut abondant" in hn)
chk("muqaddima : demande du frère", "certains de mes frères m’a demandé d’en résumer l’essentiel" in hn)
chk("muqaddima : espérance de figurer parmi ces voies", "dans l’espérance de figurer parmi ces voies" in hn)

# ---- commentaire (glosses + analyse)
chk("glose taṣānīf", "pluriel de « taṣnīf »" in hn)
chk("glose iṣṭilāḥ", "l’accord d’un groupe consécré" in hn)
chk("glose baʿḍ al-iḫwān : ibn Ǧamāʿa", "ʿIzz ad-Dīn ibn Ǧamāʿa" in hn)
chk("glose baʿḍ al-iḫwān : az-Zarkašī", "Šams ad-Dīn az-Zarkašī" in hn)
chk("trois opinions tenues telles quelles", "tient les trois opinions telles quelles, sans trancher" in hn)
chk("analyse : ādāb at-taʾlīf", "ādāb at-taʾlīf" in hn)
chk("analyse : science absolue", "Sa science absolue et de Sa puissance dépassante" in hn)
chk("analyse : héritage de la prophétie", "l’héritage de la prophétie après lui" in hn)

# ---- biographie
chk("naissance Šaʿbān 773 H / vers 1371", "Šaʿbān 773 H / vers 1371" in hn)
chk("naissance sur la rive du Nil, vieille Le Caire", "sur la rive du Nil, à la vieille Le Caire" in hn)
chk("père mort Raǧab 777 H / vers 1375", "Raǧab 777 H / vers 1375" in hn)
chk("tuteur Zakī d-Dīn Abū Bakr ibn Nūr ad-Dīn ʿAlī", "Zakī d-Dīn Abū Bakr ibn Nūr ad-Dīn ʿAlī" in hn)
chk("Coran à neuf ans", "mémorisa le Coran alors qu’il avait neuf ans" in hn)
chk("imam tarāwīḥ à douze ans, Mosquée sacrée", "en imam dans la Mosquée sacrée" in hn)
chk("muǧāwara 785 H / vers 1383 avec al-Ḫuraybī", "785 H / vers 1383" in hn and "al-Ḫuraybī" in hn)
chk("Alexandrie 797 H / vers 1394", "à la fin de l’an 797 H / vers 1394" in hn)
chk("Ḥiǧāz et Yémen, La Mecque, Mina, Médine", "au Ḥiǧāz et au Yémen" in hn and "à Mina et Médine" in hn)
chk("Syrie", "pays de la Syrie" in hn)
chk("Ǧawāhir wa-d-durar 1/421", "al-Ǧawāhir wa-d-durar, 1/421" in hn)
chk("Fatḥ al-bārī", "Fatḥ al-bārī bi-šarḥ Ṣaḥīḥ al-Buḫārī" in hn)
chk("al-Iṣāba", "al-Iṣāba fī tamyīz aṣ-ṣaḥāba" in hn)
chk("Inbāʾ al-ġumr", "Inbāʾ al-ġumr bi-abnāʾ al-ʿumr" in hn)
chk("Tabsīr al-muntabih", "Tabsīr al-muntabih wa-taḥrīr al-muštabih" in hn)
chk("Taʿǧīl al-manfaʿa", "Taʿǧīl al-manfaʿa bi-zawāʾid rijāl al-aʾimma al-arbaʿa" in hn)
chk("Taġlīq at-taʿlīq", "Taġlīq at-taʿlīq ʿalā Ṣaḥīḥ al-Buḫārī" in hn)
chk("Tahḏīb at-tahḏīb (al-Mizzī)", "Tahḏīb al-kamāl fī asāmī ar-riǧāl d’al-Mizzī" in hn)
chk("Taqrīb at-tahḏīb (Six livres)", "notices des hommes des Six livres" in hn)
chk("mort Dhū l-ḥiǧǧa 852 H / vers 1448", "Dhū l-ḥiǧǧa 852 H / vers 1448" in hn)
chk("tranchage 852 documenté en corps", "tranchée par l’OCR 300 dpi de la page 15" in hn)

# ---- importance/raison + ahtadī wa-aqtadī
chk("importance : quintessence", "la quintessence des livres de cet art et sa moelle" in hn)
chk("importance : commenté, glosé, versifié", "l’ont versifié" in hn)
chk("raison : feuillets fins", "je l’ai donc résumé en des feuillets fins" in hn)
chk("rubrique ahtadī wa-aqtadī", "Je m’inspire et j’inspire (ahtadī wa-aqtadī)" in hn)
chk("citation al-Ḫaṭīb : arbre et fruit", "la science est un arbre, et l’action est son fruit" in hn)
chk("citation al-Ḫaṭīb : père et enfant né", "la science est un père et l’action un enfant né" in hn)
chk("citation al-Ḫaṭīb : rassemble les deux", "rassemble les deux" in hn)
chk("référence Iqtidāʾ p.14", "Iqtidāʾ al-ʿilm al-ʿamal" in hn and "p. 14" in hn)

# ---- évaluation
chk("évaluation : 4 activités", "quatre activités" in hn)
chk("évaluation : Ǧāmiʿ bayān al-ʿilm", "Ǧāmiʿ bayān al-ʿilm wa-faḍlihi" in hn)
chk("évaluation : al-Iʿlām", "al-Iʿlām ilā maʿrifat uṣūl ar-riwāya wa-taqyīd as-samāʿ" in hn)
chk("évaluation : iḫlāṣ", "les fruits de la sincérité (al-iḫlāṣ)" in hn)

# ---- exploitation (citation as-Saḫāwī tranchée 600 dpi)
chk("exploitation : lystu rāḍiyan", "Je ne suis satisfait d’aucune de mes compositions" in hn)
chk("exploitation : cinq ouvrages épurés", "« al-Muštabih », et « at-Tahḏīb », et « Lisān al-mīzān »" in hn)
chk("exploitation : passage tranché 600 dpi (venu tard)",
    "ce qui m’est venu tard, je ne me serais point restreint à aḏ-Ḏahabī" in hn)
chk("exploitation : livre original (mubtakar)", "un livre original (mubtakar)" in hn)
chk("exploitation : éloge final", "du « Taġlīq » et de « la Naḫba »" in hn)
chk("exploitation : consigne valeurs morales", "les valeurs morales (al-qiyam al-ḫuluqiyya)" in hn)

# ---- préparation leçon suivante
chk("leçon suivante nommée", "Le ḫabar, le ḥadīṯ et l’aṯar" in hn)
chk("préparation : Muwaṭṭaʾ exemple ḥadīṯ/aṯar", "Muwaṭṭaʾ de l’imām Mālik" in hn
    and "un exemple de ḥadīṯ et un exemple d’aṯar" in hn)
chk("préparation : 3 consignes", "trois consignes" in h)

# ---- hygiène FR
chk("zéro caractère arabe", not re.search(r"[\u0600-\u06FF\u0750-\u077F\u08A0-\u08FF\uFB50-\uFDFF\uFE70-\uFEFF]", h))
chk("zéro apostrophe droite", "'" not in h)
chk("guillemets appariés", h.count("«") == h.count("»"))
chk("zéro double espace", "  " not in re.sub(r"&nbsp;|\n", "", h))
chk("zéro résidu placeholder", not re.search(r"XXX|TODO|【|____", h))
chk("balises appariées (h1/h2/h3/p/dl/dt/dd)",
    h.count("<h1>") == h.count("</h1>") and h.count("<h2>") == h.count("</h2>")
    and h.count("<h3>") == h.count("</h3>") and h.count("<p>") == h.count("</p>")
    and h.count("<dl") == h.count("</dl>") and h.count("<dt>") == h.count("</dt>")
    and h.count("<dd>") == h.count("</dd>"))

# ---- registre : htmlFr posé, voisins intacts
reg = json.load(open(REG, encoding="utf-8"))
les = {str(d.get("docId", "")): d for d in reg["lessons"]}
chk("registre livre 2 : 27 entrées", len(reg["lessons"]) == 27)
chk("registre 256 non touché (htmlFr vide)", (les["pdf-mut23h2u-256"].get("htmlFr") or "") == "")
fr = les["pdf-mut23h2u-255"].get("htmlFr") or ""
chk("registre 255 = htmlFr posé (~17 253 car)", 16_500 <= len(fr) <= 18_000)
chk("registre 255 == fichier livré", fr.strip() == h.strip())
chk("titleAr pré-mappé 255", les["pdf-mut23h2u-255"].get("titleAr") == "الدرس 1 : التعريف بالحافظ ابن حجر وكتابه نخبة الفكر")
chk("titleFr pré-mappé 255 aligné au h1", les["pdf-mut23h2u-255"].get("titleFr") == "Leçon 1 : Présentation du ḥāfiẓ Ibn Ḥaǧar et de son ouvrage Nuḫbat al-Fikr")
reg1 = json.load(open(REG1, encoding="utf-8"))
l1 = {str(d.get("docId", "")): d for d in reg1["lessons"]}
chk("registre livre 1 : 141 intact (24 319 car)", len(l1["pdf-mut23h2r-141"].get("htmlFr") or "") == 24319)
chk("registre livre 1 : 140 intact (16 018 car)", len(l1["pdf-mut23h2r-140"].get("htmlFr") or "") == 16018)
chk("registre livre 1 : 136 intact (20 967 car)", len(l1["pdf-mut23h2r-136"].get("htmlFr") or "") == 20967)

print(f"verify-ulumhadith2-pdf255 : {ok} PASS / {fail} ÉCHEC")
raise SystemExit(1 if fail else 0)

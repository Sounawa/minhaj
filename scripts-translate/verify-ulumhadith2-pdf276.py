#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Minhāj — Vérification de la leçon ulum-hadith-tanawi-2 / pdf-mut23h2u-276
(الدرس 22 : المزيد في متصل الأسانيد والمضطرب — p.115-119 du manuel
ulum-hadith-2-thanawi_text.pdf) : bornes p.115-119 par sondage image
(p.114 = clôture de la leçon 21, livrée R656, docId pdf-mut23h2u-275 ;
p.115 = bannière médaillon « 22 » + 4 objectifs + tamhīd + matn Ibn Ḥaǧar
reprise « ou par l'addition d'un narrateur... » + الفهم 2 items ; p.116-117 =
التعليــل أولا المزيد : définition + exemple Ibn al-Mubārak (Tirmidhī أبواب
الجنائز) + Abū Ḥātim [Muqaddima ص 287] + شروط رد الزيادة 2 + حكمه + 3 cas +
المرسل الخفي ; p.117-118 = ثانيا المضطرب définition (الصحاح 1/178) + شرطان +
أنواعه (السند Shahr/Dāraquṭnī 6/45 ; المتن Fāṭima b. Qays/Zarkashī 2/239) +
حكمه ; p.118 = التهذيب Ibn Mahdī [Rāmahiruzī ص 205] ; p.119 = التقويم 2 +
الاستتمار Sakhāwī [Fatḥ al-Muġīṯ ص 204] + الإعداد القبلي 2 items ; p.120 =
bannière leçon 23 المصحف والمحرف (médaillon 23, sondage, non touchée,
registre vide). Adjudications documentées (VINGT lectures d'images,
tr-tmp/qa-crops-r657/) : matn « fa-l-muḍṭarab » corroboré EN LIGNE
(shamela/ketabonline) ; Abū Ḥātim « yurawna/fa-ġalaṭa » canonique EN LIGNE
(islamicbook.ws Tadrīb ar-rāwī) ; « sarraḥa bi-samāʿ Busr min Wāṯila » EN
LIGNE ; Dāraquṭnī 6/45 (image) contre 6/54 couche ; Zarkashī 2/239 (image)
contre 2/932 couche ; Rāmahiruzī p.205 (image) contre 502 couche ;
Sakhāwī p.204 ; Jawharī 1/178 ; chaîne exemple tranchée par image 900 dpi
(Abū Idrīs b. al-Asqaʿ / Abū Murṯad al-Ġanawī contre couche Wāṯila) ;
ZÉRO ĀYA (cache coranique non sollicité).
Usage: python3 scripts-translate/verify-ulumhadith2-pdf276.py
"""
import json
import re

HTML = "/home/z/my-project/tr-tmp/lesson-uh2-pdf-mut23h2u-276-fr.html"
REG = "/home/z/my-project/content/books/ulum-hadith-tanawi-2.json"

ok, fail = 0, 0


def chk(label, cond):
    global ok, fail
    if cond:
        ok += 1
    else:
        fail += 1
        print(f"ÉCHEC : {label}")


h = open(HTML, encoding="utf-8").read()
hn = re.sub(r" +", " ", h.replace("&nbsp;", " ").replace("\u202f", " ").replace("\u2009", " "))

# ---- h1 et méta
chk("h1 = titleFr pré-mappé « Leçon 22 : L’adjonction dans les chaînes continues (mazīd) et l’incohérent (muḍṭarab) »",
    hn.startswith("<h1>Leçon 22 : L’adjonction dans les chaînes continues (mazīd) et l’incohérent (muḍṭarab)"))
chk("h1 mentionne deuxième année", "deuxième année" in h[:500])
chk("h1 mentionne le matn d’Ibn Ḥaǧar (addition d’un narrateur, substitution, examen)",
    "addition d’un narrateur" in h[:1400] and "substitution" in h[:1500] and "l’examen" in h[:1600])
chk("h1 mentionne l’exemple ʿAbdallāh b. al-Mubārak et Tirmiḏī",
    "ʿAbdallāh b. al-Mubārak" in h[:3700] and "Tirmiḏī" in h[:2800])
chk("h1 mentionne les deux conditions et le messager caché",
    "deux conditions" in h[:3200] and "messager caché" in h[:3600])
chk("h1 mentionne l’incohérent, Śiḥāḥ et Dāraquṭnī",
    "incohérent (al-muḍṭarab)" in h[:1700] and "Ǧawharī" in h[:4200] and "Dāraquṭnī" in h[:4600])
chk("h1 mentionne Fāṭima bint Qays, ʿAbd ar-Raḥmān b. Mahdī et as-Saḫāwī",
    "Fāṭima bint Qays" in h[:3700] and "ʿAbd ar-Raḥmān b. Mahdī" in h[:3700] and "as-Saḫāwī" in h[:3700])
chk("dl.lesson-meta présent", '<dl class="lesson-meta">' in h and "<dt>Source du cours</dt>" in h)
chk("item archive.org cité", "1_20220304_20220304_2251" in h)
chk("source locale citée", "ulum-hadith-2-thanawi_text.pdf" in h)
chk("bornes p.115-119 documentées", "pages 115 à 119" in h)
chk("p.114 clôture leçon 21 (R656, 275)", "R656" in h and "pdf-mut23h2u-275" in h)
chk("p.120 bannière leçon 23 sondage, registre vide", "leçon 23" in h and "non touchée" in h)
chk("20 lectures d’images consignées", "VINGT lectures d’images" in h and "qa-crops-r657" in h)
chk("corroboration EN LIGNE matn fā-l-muḍṭarab documentée", "corroborée EN LIGNE" in h and "shamela.ws" in h)
chk("chiffres inversés tranchés (54→45, 932→239, 502→205) documentés",
    "54→45" in h and "932→239" in h and "502→205" in h)
chk("chaîne exemple tranchée par image 900 dpi documentée",
    "image 900 dpi" in h and "Abū Murṯad al-Ġanawī" in h)

# ---- objectifs
chk("section objectifs présente", "Les objectifs de la leçon" in h)
chk("objectif 1 (concept de l’adjonction)", "je reconnais le concept de l’additionné dans les chaînes continues" in h)
chk("objectif 2 (types de l’agitation)", "je saisis les types de l’agitation dans le ḥadīṯ" in h)
chk("objectif 3 (addition du confident vs autre)", "je distingue entre l’addition de l’homme de confiance et celle de l’autre" in h)
chk("objectif 4 (sérieux et maîtrise)", "je veille au sérieux et à la maîtrise" in h)

# ---- tamhīd
chk("tamhīd présent", "Le tamhīd (l’introduction)" in h)
chk("tamhīd sentiers précis des maîtres du ḥadīṯ", "sentiers d’une précision extrême" in h)

# ---- matn
chk("section matn Ibn Ḥaǧar", "le matn du ḥāfiẓ Ibn Ḥaǧar" in h)
chk("matn « addition d’un narrateur… chaînes continues »", "l’addition d’un narrateur, alors l’additionné (az-zāʾid) est dans les chaînes continues" in h)
chk("matn « substitution sans préférence… incohérent »", "ou par sa substitution sans préférence, alors c’est l’incohérent (al-muḍṭarab)" in h)
chk("matn « à dessein, pour l’examen »", "à dessein, pour l’examen" in h)

# ---- commentaire (šarḥ + istiḫlāṣ)
chk("gloses lexicales (aš-šarḥ) présentes", "Les gloses lexicales du manuel (aš-šarḥ)" in h)
chk("glose « addition d’un narrateur »", "ou si la divergence était par l’addition d’un narrateur" in h)
chk("glose « ou par sa substitution »", "ou si la divergence était par la substitution du narrateur" in h)
chk("extraction 2 items", "j’extrais du texte les types de la divergence" in h
    and "quand la substitution du narrateur dans la chaîne est-elle décrite comme une agitation" in h)

# ---- tabṣīṭ première partie (al-mazīd)
chk("définition mazīd (un homme de plus, méprise, faute)",
    "que le narrateur ajoute dans la chaîne d’un ḥadīṯ un homme de plus, ou davantage, par méprise et par faute" in h)
chk("exemple chaîne Ibn al-Mubārak complet", "il nous a transmis Sufyān, de ʿAbd ar-Raḥmān b. Yazīd b. Ǧābir" in h
    and "Busr b. ʿUbaydallāh" in h and "Abū Idrīs b. al-Asqaʿ" in h and "Abū Murṯad al-Ġanawī" in h)
chk("exemple hadith « ne vous asseyez pas sur les tombes »",
    "ne vous asseyez pas sur les tombes, et n’y faites pas la prière" in h)
chk("source Tirmiḏī bāb funérailles", "les chapitres des funérailles, le chapitre&nbsp;\u202f: de ce qui est venu sur la détestation de la marche sur les tombes" in h)
chk("addition en deux places (Sufyān/Abū Idrīs)", "en deux places&nbsp;\u202f: dans «\u202f&nbsp;Sufyān&nbsp;\u202f» et dans «\u202f&nbsp;Abū Idrīs&nbsp;\u202f»" in h)
chk("commentaire méprise Sufyān d’Ibn al-Mubārak", "elle est de la part d’Ibn al-Mubārak" in h)
chk("citation Abū Ḥātim ar-Rāzī", "Abū Ḥātim ar-Rāzī a dit&nbsp;\u202f: «\u202f&nbsp;ils considèrent qu’Ibn al-Mubārak a commis une erreur en cela" in h)
chk("source Muqaddimat Ibn aṣ-Ṣalāḥ page 287", "Muqaddimat Ibn aṣ-Ṣalāḥ (l’introduction d’Ibn aṣ-Ṣalāḥ), page 287" in h)
chk("conditions 2 (a/b) présentes", "que celui qui n’a pas ajouté soit en accord avec celui qui a ajouté" in h
    and "que la déclaration d’audition tombe à la place de l’addition" in h)
chk("application à l’exemple (Busr déclare son audition de Wāṯila)",
    "que Busr b. ʿUbaydallāh déclare son audition de Wāṯila dans l’un des deux côtés" in h)
chk("jugement (les savants ne jugent pas sans indication)",
    "les savants ne jugent pas l’addition comme erreur sans une indication" in h)
chk("mursal ḫafī défini", "le messager caché&nbsp;\u202f» (al-mursal al-ḫafī)" in h)
chk("3 possibilités de la venue de l’addition",
    "que soit préféré que l’addition du narrateur est erreur et faute" in h
    and "est incomplet, et il a commis la dissimulation (tadlīs)" in h
    and "les deux voies sont correctes" in h)

# ---- tabṣīṭ seconde partie (al-muḍṭarab)
chk("seconde partie présente", "La seconde partie&nbsp;\u202f: le ḥadīṯ incohérent (al-ḥadīṯ al-muḍṭarab)" in h)
chk("définition langue (nom d’agent de l’agitation)",
    "c’est un nom d’agent de l’agitation (iḍṭirāb), qui est le dérangement de l’affaire et sa corruption" in h)
chk("source aṣ-Ṣiḥāḥ al-Ǧawharī 1/178",
    "aṣ-Ṣiḥāḥ (le correct), al-Ǧawharī, tome un, page 178" in h)
chk("définition terminologie (formes différentes égales en force)",
    "rapporté sur des formes différentes égales en force, sans préférence pour l’une des deux transmissions" in h)
chk("2 conditions du muḍṭarab (divergence sans réunion ; égalité en force)",
    "la divergence des transmissions du ḥadīṯ de sorte que la réunion ne peut pas se faire entre elles" in h
    and "l’égalité des transmissions en force" in h)
chk("citation « sans préférence, alors l’incohérent »",
    "«\u202f&nbsp;sans préférence, alors l’incohérent.&nbsp;\u202f»" in h)
chk("types (chaîne / texte)", "l’agitation peut être dans la chaîne, et elle peut être dans le texte" in h)
chk("exemple Shahr de ʿAbd ar-Raḥmān b. ʿAnm de Muʿāḏ",
    "le ḥadīṯ que rapporte Šahr de ʿAbd ar-Raḥmān b. ʿAnm, de Muʿāḏ b. Ǧabal" in h)
chk("hadith « dix fois avant de se lever » (prière de l’après-midi)",
    "dix fois avant de se lever" in h and "prière de l’après-midi" in h)
chk("source al-Muʿǧam al-kabīr aṭ-Ṭabarānī (bāb al-mī, fin de ligne rendue telle quelle)",
    "al-Muʿǧam al-kabīr (le grand dictionnaire), aṭ-Ṭabarānī, le chapitre de bāb al-mī" in h
    and "fin de ligne imprimée coupée, rendue telle quelle" in h)
chk("six voies divergentes (Muʿāḏ/Abū ḏarr/Abū Hurayra/Abū Ummāma/Umm Salama/mursal)",
    "d’Abū ḏarr" in h and "d’Abū Hurayra" in h and "d’Abū Ummāma" in h
    and "de Umm Salama" in h and "suspendu" in h)
chk("citation ad-Dāraquṭnī « l’agitation en cela est de Šahr »",
    "l’agitation en cela est de Šahr, et Dieu est le plus savant" in h)
chk("source al-ʿIlal al-wārida 6/45 (image contre 6/54)",
    "ad-Dāraquṭnī, tome six, page 45" in h)
chk("exemple Fāṭima bint Qays (Šurayk/Abū Ḥamza/aš-Šaʿbī)",
    "de Šurayk, d’Abū Ḥamza, d’aš-Šaʿbī, de Fāṭima bint Qays" in h)
chk("hadith « dans le bien il y a un droit autre que l’aumône légale »",
    "dans le bien il y a un droit autre que l’aumône légale" in h)
chk("variante Ibn Māǧa « il n’y a pas de droit autre que l’aumône légale »",
    "dans le bien il n’y a pas de droit autre que l’aumône légale" in h)
chk("source an-Nukat az-Zarkašī 2/239 (image contre 2/932)",
    "az-Zarkašī, tome deux, page 239" in h)
chk("agitation qui ne supporte pas l’interprétation", "une agitation qui ne supporte pas l’interprétation" in h)
chk("agitation selon sa source (un seul narrateur / un groupe)",
    "elle peut venir d’un seul narrateur" in h and "elle peut survenir d’un groupe" in h)
chk("jugement muḍṭarab (causes du rejet, absence de maîtrise)",
    "l’agitation est des causes du rejet du ḥadīṯ&nbsp;\u202f; par l’absence de la maîtrise de son narrateur ou de ses transmetteurs" in h)

# ---- ahtadī wa-aqtadī (التهذيب)
chk("section « je m’oriente et j’imite » présente", "Je m’oriente et j’imite (ahtadī wa-aqtadī)" in h)
chk("citation ʿAbd ar-Raḥmān b. Mahdī (jour de gain / enseigne / discute)",
    "ce jour est son jour de gain" in h and "il discute avec lui et l’étudie avec lui" in h)
chk("source ar-Rāmahiruzī page 205 (image contre 502)",
    "ar-Rāmahiruzī, page 205" in h)

# ---- taqwīm
chk("évaluation présente", "L’évaluation (at-taqwīm)" in h)
chk("taqwīm 2 items (conditions du rejet / types de l’agitation)",
    "j’explique les conditions du rejet de l’addition dans la chaîne." in h
    and "j’explique les types de l’agitation dans le ḥadīṯ." in h)

# ---- istiṯmār
chk("exploitation présente", "L’exploitation (al-istiṯmār)" in h)
chk("citation as-Saḫāwī (isnaḍ exempt du narrateur additionnel)",
    "l’isnaḍ exempt du narrateur additionnel" in h)
chk("citation as-Saḫāwī (particule « de » / exige la connexion)",
    "s’il est par la particule “de”" in h and "comme “il nous a transmis”, “il nous a informés” et “j’ai entendu”" in h)
chk("source Fatḥ al-Muġīṯ page 204",
    "as-Saḫāwī, page 204" in h)
chk("activité : discussion de la parole d’as-Saḫāwī",
    "je discute la parole du ḥāfiẓ as-Saḫāwī, en montrant la différence entre l’addition de l’homme de confiance et celle de l’autre." in h)

# ---- iʿdād al-qiblī
chk("préparation leçon suivante présente", "La préparation de la leçon suivante (al-iʿdād al-qiblī)" in h)
chk("iʿdād leçon 23 muṣaḥḥaf/muḥarraf (2 items)",
    "La leçon 23 est «\u202f&nbsp;le falsifié dans la graphie (al-muṣaḥḥaf) et le falsifié dans la vocalisation (al-muḥarraf)&nbsp;\u202f»" in h
    and "l’élève cherchera la différence entre le muṣaḥḥaf et le muḥarraf" in h
    and "autres que ce qui est mentionné dans le livre" in h)

# ---- hygiène FR
chk("zéro caractère arabe", not re.search(r"[\u0600-\u06FF\u0750-\u077F\u08A0-\u08FF\uFB50-\uFDFF\uFE70-\uFEFF]", h))
chk("zéro apostrophe droite", chr(39) not in h)
chk("guillemets appariés", h.count("«") == h.count("»"))
chk("zéro résidu placeholder", not re.search(r"XXX|TODO|【|____", h))
chk("balises appariées (h1/h2/h3/p/dl/dt/dd/strong/ol/ul/li)",
    h.count("<h1>") == h.count("</h1>") and h.count("<h2>") == h.count("</h2>")
    and h.count("<h3>") == h.count("</h3>") and h.count("<p>") == h.count("</p>")
    and h.count("<dl") == h.count("</dl>") and h.count("<dt>") == h.count("</dt>")
    and h.count("<dd>") == h.count("</dd>") and h.count("<strong>") == h.count("</strong>")
    and h.count("<ol>") == h.count("</ol>") and h.count("<ul>") == h.count("</ul>")
    and h.count("<li>") == h.count("</li>"))

# ---- registre : htmlFr posé, voisins intacts
reg = json.load(open(REG, encoding="utf-8"))
les = {str(d.get("docId", "")): d for d in reg["lessons"]}
chk("registre livre 2 : 27 entrées", len(reg["lessons"]) == 27)
chk("registre 272 intact (19 801 car)", len(les["pdf-mut23h2u-272"].get("htmlFr") or "") == 19801)
chk("registre 273 intact (22 645 car)", len(les["pdf-mut23h2u-273"].get("htmlFr") or "") == 22645)
chk("registre 274 intact (28 082 car)", len(les["pdf-mut23h2u-274"].get("htmlFr") or "") == 28082)
fr275 = les["pdf-mut23h2u-275"].get("htmlFr") or ""
chk("registre 275 intact (39 200 car)", len(fr275) == 39200)
fr = les["pdf-mut23h2u-276"].get("htmlFr") or ""
if fr:
    chk("registre 276 = htmlFr posé (24 000-40 000 car)", 24_000 <= len(fr) <= 40_000)
    chk("registre 276 == fichier livré", fr.strip() == h.strip())
else:
    chk("registre 276 encore vide (avant hand-set)", True)
chk("registre 277 non touché (htmlFr vide)", (les["pdf-mut23h2u-277"].get("htmlFr") or "") == "")
chk("titleAr pré-mappé 276 intact (leçon 22)",
    les["pdf-mut23h2u-276"].get("titleAr") == "الدرس 22 : المزيد في متصل الأسانيد والمضطرب")
chk("titleFr pré-mappé 276 aligné au h1 (apostrophes normalisées)",
    (les["pdf-mut23h2u-276"].get("titleFr") or "").replace(chr(39), "\u2019")
    == "Leçon 22 : L’adjonction dans les chaînes continues (mazīd) et l’incohérent (muḍṭarib)")

print(f"verify-ulumhadith2-pdf276 : {ok} PASS / {fail} ÉCHEC")
raise SystemExit(1 if fail else 0)

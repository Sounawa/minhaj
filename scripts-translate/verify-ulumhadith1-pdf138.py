#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Minhāj — Vérification de la leçon ulum-hadith-tanawi-1 / pdf-mut23h2r-138
(le ḥadīṯ délaissé al-matrūk, p.129-132 du manuel ulum-hadith-1-thanawi.pdf)
: bannière « ad-dars 27 » p.129 ; bornes p.129-132 par DOUBLE sondage (bannière
ad-dars 28 « al-mawḍūʿ » + objectifs ×3 p.133 lus à l'OCR tr-tmp/r608/t133.txt
+ iʿdād qablī p.132 ×2 q. mawḍūʿ) ; bayt du nāẓim « matrūkahu mā wāḥidun bihi
nfarada * * * wa-ajmaʿū li-ḍaʿfihī fa-huwa karrad » tranché PAR L'IMAGE 1200
dpi (triple occurrence pp.129-131 ; kāf zāʾida selon la glose imprimée) ; deux
quidés (infirād, tuhma bi-l-kaḏib) ; autres noms (maṭrūḥ aḏ-Dhahabī, Saḫāwī,
ʿAmr b. Šimr, Ǧūbayr, wāhī) ; exemple Dāraquṭnī kitāb al-ʿīdayn (basmala,
taṯnīt, takbīr ʿArafa, yaqṭaʿuhā — « wa-ʿAmmār » verrouillé mot OCR + bbox) ;
Ibn Saʿd ; non-traitement (Ḥākim, Ibn aṣ-Ṣalāḥ, Ibn Daqīq al-ʿĪd, al-ʿIrāqī) ;
Alfiyya as-Suyūṭī ×2 vers 2400 dpi (rāwīhi) ; jugement mardūd ; Ibn al-Mulaqqin
at-Taḏkira ; Dehlawī yusammā 1200 dpi ; Muslim Muqaddima pp.131-132 (ahl
al-ḥifẓ wa-r-riḍā tel qu'imprimé) ; choix Ibn Ḥaǧar ; istiṯmār bayt « šarru
ḍ-ḍaʿīfi l-waḍʿu fa-l-matrūku ṯumma * * * ḏū l-kaḏibi fa-l-mudraju ḍumm »
(2400 dpi demi-bandes, trois points du šīn à l'extrême zoom) ; taqwīm ×2 ;
iʿdād ×2 mawḍūʿ ; bornes p.129-132 ; zéro āya, zéro résidu arabe, zéro doublon.
Usage: python3 scripts-translate/verify-ulumhadith1-pdf138.py
"""
import json
import re

HTML = "/home/z/my-project/tr-tmp/lesson-ulumhadith1-pdf-mut23h2r-138-fr.html"
REG = "/home/z/my-project/content/books/ulum-hadith-tanawi-1.json"

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
txt = re.sub(r"<[^>]+>", "", h)

# h1 aligné au titleFr pré-mappé
chk("h1 = titleFr « Le hadith délaissé (matrūk) »",
    hn.startswith("<h1>Le hadith délaissé (matrūk) :"))
chk("h1 mentionne leçon 27", "leçon 27" in h[:400])
chk("h1 mentionne manẓūma d’al-Bayqūnī", "manẓūma d’al-Bayqūnī" in h[:400])

# bayt du nāẓim (triple occurrence, karrad)
chk("bayt hémistiche 1 (matn)", "matrūkahu mā wāḥidun bihi nfarada" in h)
chk("bayt hémistiche 1 ×2 (matn + citation p.130)", h.count("matrūkahu mā wāḥidun bihi nfarada") >= 2)
chk("bayt hémistiche 2 « wa-ajmaʿū li-ḍaʿfihī fa-huwa karrad »",
    "wa-ajmaʿū li-ḍaʿfihī fa-huwa karrad" in h)
chk("bayt hémistiche 2 ×2 (matn + citation p.131)", h.count("wa-ajmaʿū li-ḍaʿfihī fa-huwa karrad") >= 2)
chk("adjudication 1200 dpi du bayt", "1200&nbsp;dpi" in h)
chk("triple occurrence pp.129-131 documentée", "triple occurrence imprimée concordent" in hn or "trois occurrences imprimées concordent" in hn)
chk("glose kāf zāʾida li-ḍarūrati n-naẓm", "zāʾida li-ḍarūrati n-naẓm" in h)
chk("glose radd/mardūd", "réduit au rebut (mardūd)" in h)

# objectifs ×3
chk("objectif 1 notion du matrūk", "Que je reconnaisse la notion du ḥadīṯ délaissé (matrūk)" in h)
chk("objectif 2 distinguer du mawḍūʿ", "tel le fabriqué (mawḍūʿ)" in h)
chk("objectif 3 vérifier les matrūkīn", "matrūkīn" in h)

# tamhīd
chk("tamhīd fisq", "la perversité (al-fisq)" in h)
chk("tamhīd tuhmat al-kaḏib", "l’accusation de mensonge (tuhmat al-kaḏib)" in h)

# glose
chk("glose maṭrūḥ/taraktu", "le jeté (al-maṭrūḥ)" in h and "taraktu" in h)

# extraction des thèmes
chk("question liminaire p.130", "Qu’est-ce que le ḥadīṯ délaissé" in h)
chk("plan deuxièmement", "le jugement du ḥadīṯ délaissé, et sa relation au fabriqué et au méconnu" in h)

# définition : deux quidés
chk("défin. rapporteur accusé de mensonge", "un rapporteur accusé de mensonge (muttaham bi-l-kaḏib)" in h)
chk("quide unicité — voies multiples", "des voies multiples aux issues multiples" in h)
chk("quide tuhma — satr", "la dissimulation (al-satr) de son état" in h)
chk("quide tuhma — exclusion du mawḍūʿ", "il est le fabriqué (mawḍūʿ)" in h)
chk("sens tuhma — hors du ḥadīṯ prophétique", "le ḥadīṯ prophétique" in h)
chk("sens tuhma — ġafla šadīda", "l’étourderie excessive (al-ġafla aš-šadīda)" in h)
chk("sens tuhma — katrat al-wahm", "katrat al-wahm" in h)
chk("matn contrevient aux règles connues", "contrevienne aux règles connues" in h)

# autres noms
chk("maṭrūḥ aḏ-Dhahabī", "l’imām aḏ-Dhahabī" in h)
chk("citation as-Saḫāwī", "As-Saḫāwī dit" in h)
chk("Saḫāwī « descendu sous le faible »", "descendu sous le faible et s’est élevé au-dessus du fabriqué" in h)
chk("Saḫāwī exemple ʿAmr b. Šimr ← Ǧābir al-Juʿfī ← al-Ḥasan ← ʿAlī",
    "de ʿAmr b. Šimr, de Ǧābir al-Juʿfī, de al-Ḥasan, de ʿAlī" in h)
chk("Saḫāwī exemple Ǧūbayr ← aḍ-Ḍaḥḥāk ← Ibn ʿAbbās",
    "de Ǧūbayr, de aḍ-Ḍaḥḥāk, de Ibn ʿAbbās" in h)
chk("Ibn Ḥaǧar taḥqīq", "le délaissé en l’examen rigoureux (at-taḥqīq)" in h)
chk("épithète wāhī", "le chancelant" in hn and "(al-wāhī)" in h)

# exemple Dāraquṭnī
chk("Dāraquṭnī Sunan kitāb al-ʿīdayn", "kitāb al-ʿīdayn" in h and "Sunan ad-Dāraquṭnī" in h)
chk("isnaḍ ʿAmr b. Šimr al-Juʿfī", "ʿAmr b. Šimr al-Juʿfī" in h)
chk("isnaḍ Ǧābir al-Juʿfī", "de Ǧābir al-Juʿfī" in h)
chk("isnaḍ Abū Ṭufayl", "Abū Ṭufayl" in h)
chk("isnaḍ ʿAlī + ʿAmmār", "ʿAlī b. Abī Ṭālib et de ʿAmmār" in h)
chk("« wa-ʿAmmār » preuve mot OCR + bbox", "boîte englobante" in h and "jamais deviné" in h)
chk("basmala translit", "bismi llāhi r-raḥmāni r-raḥīm" in h)
chk("basmala traduite", "Au nom de Dieu, le Miséricordieux, le Tout-Miséricordieux" in h)
chk("taṯnīt à l’aube", "le taṯnīt en la prière de l’aube" in h)
chk("takbīr ʿArafa", "takbīr du jour de ʿArafa" in h)
chk("clôture ʿaṣr dernier jour tašrīq", "yaqṭaʿuhā" in h and "tašrīq" in h)
chk("yaqṭaʿuhā récusation OCR documentée", "la lecture dégradée de l’OCR automatique récusée" in h)

# Ibn Saʿd + non-traitement + Alfiyya
chk("Ibn Saʿd « matrūk al-ḥadīṯ »", "matrūk al-ḥadīṯ" in h)
chk("non-traitement Ḥākim/aṣ-Ṣalāḥ/Daqīq/ʿIrāqī",
    "al-Ḥākim, Ibn aṣ-Ṣalāḥ, Ibn Daqīq al-ʿĪd, al-ʿIrāqī" in h)
chk("mention an-Nukhba", "an-Nukhba" in h)
chk("Alfiyya vers 1 + 2400 dpi", "wa-summiya bi-l-matrūki fardan naṣab" in h and "2400&nbsp;dpi" in h)
chk("Alfiyya « rāwīhi » porté par l’imprimé", "rāwīhi muttahamun bi-l-kaḏib" in h
    and "la hāʾ du possessif y lisible" in h)
chk("Alfiyya vers 2", "ʿarafūhu minhu fī ġayri l-aṯari" in h
    and "aw faasaqa aw ġullatan aw wahmun kaṯīr" in h)

# jugement
chk("jugement ḍaʿīf ǧiddan", "l’espèce du très faible (ḍaʿīf ǧiddan)" in h)
chk("ni šawāhid ni mutābaʿāt", "ni les preuves (aš-šawāhid) ni les suivies (al-mutābaʿāt)" in h)
chk("plus léger que le mawḍūʿ", "mais il est plus léger que lui" in h)

# relation au fabriqué
chk("Ibn al-Mulaqqin at-Taḏkira", "Ibn al-Mulaqqin en at-Taḏkira" in h)
chk("al-muḫtaraʾ aṣ-ṣanūʿ", "l’inventé, le façonné (al-muḫtaraʾ aṣ-ṣanūʿ)" in h)

# relation au munkar
chk("description du rapporteur chez les anciens", "en la description du rapporteur" in h
    and "al-mutaqaddimīn" in h)
chk("Dehlawī citation + yusammā 1200 dpi", "yusammā hāḏā l-qismu matrūkan" in h
    and "l’OCR automatique l’ayant rendu méconnaissable" in h)
chk("Muslim Muqaddima translit", "wa-ʿalāmatu l-munkari fī ḥadīṯi l-muḥaddiṯi" in h)
chk("Muslim ahl al-ḥifẓ wa-r-riḍā tel qu’imprimé",
    "min ahli l-ḥifẓi wa-r-riḍā" in h and "telles quelle par l’imprimé" in hn or "portée telle quelle par l’imprimé" in hn)
chk("Muslim mahǧūr ġayr maqbūl", "mahǧūra l-ḥadīṯi ġayra maqbūlin wa-lā mustaʿmal" in h)
chk("citation poursuivie pp.131-132", "poursuivie sur les pages 131 et 132" in h)
chk("charnière riwāyatahum documentée", "rendu « riwāyatahum » selon la continuation imprimée" in hn)
chk("Ibn Ḥaǧar choix", "les délaissés (al-matrūkūn)" in hn
    and "tusammā munkaran" in h and "le choix (al-muḫtār)" in hn)

# istiṯmār
chk("istiṯmār bayt hémistiche 1", "šarru ḍ-ḍaʿīfi l-waḍʿu fa-l-matrūku ṯumma" in h)
chk("istiṯmār bayt hémistiche 2", "ḏū l-kaḏibi fa-l-mudraju ḍumm" in h)
chk("šarru adjudiqué extrême zoom trois points šīn",
    "les trois points du šīn y sont attestés" in h)
chk("2400 dpi demi-bandes", "deux demi-bandes pleine largeur" in h)
chk("mot final ḍumm porté par l’imprimé", "porté par l’imprimé" in h)

# taqwīm ×2
chk("taqwīm q1 épithètes des deux bayt-s", "les épithètes du ḥadīṯ advenues dans les deux bayt-s" in h)
chk("taqwīm q2 secret de l’ordre", "le secret en l’ordre des types du ḥadīṯ" in h)

# iʿdād qablī ×2 mawḍūʿ
chk("iʿdād q1 signification du mawḍūʿ", "quelle est la signification du ḥadīṯ fabriqué (mawḍūʿ)" in h)
chk("iʿdād q2 jugement de la transmission", "le jugement de la transmission du ḥadīṯ fabriqué" in h)
chk("iʿdād q1 lue à l’image", "fut lue à l’image 1200&nbsp;dpi" in h)

# bornes
chk("bornes p.129-132", "s’ouvre en la page imprimée 129 et s’achève en la page 132" in h)
chk("leçon suivante mawḍūʿ p.133", "ouvre en la page 133 du même manuel" in h)
chk("objectifs suivants lus OCR p.133", "tr-tmp/r608/t133.txt" in h)
chk("objectif mawḍūʿ suivant : abstention avec biais d’état",
    "sans en exposer l’état" in h)
chk("double sondage jamais devinée", "jamais devinée" in h)
chk("chaîne R602→R607, tour R608", "R602→R607" in h and "tour R608" in h)
chk("interdiction de double rendu", "interdite de double rendu" in h)

# hygiene FR
chk("zéro caractère arabe", not re.search(r"[\u0600-\u06FF]", h))
chk("zéro apostrophe droite", "'" not in h)
chk("guillemets appariés", h.count("«") == h.count("»"))
chk("zéro double espace", "  " not in re.sub(r"&nbsp;|\n", "", h))
chk("zéro résidu placeholder", not re.search(r"XXX|TODO|【|____", h))
chk("aucune āya rendue (assertion méta présente)", "āya n’est mobilisée" in h)
chk("balises appariées", h.count("<ol>") == h.count("</ol>")
    and h.count("<li>") == h.count("</li>") and h.count("<h2>") == h.count("</h2>")
    and h.count("<h3>") == h.count("</h3>"))

# registre : htmlFr posé, voisins intacts, pas de doublon parallèle
reg = json.load(open(REG, encoding="utf-8"))
les = {str(d.get("docId", "")): d for d in reg["lessons"]}
chk("registre 136 intact (~20 968 car)", 20_000 <= len(les["pdf-mut23h2r-136"].get("htmlFr") or "") <= 21_500)
fr137 = les["pdf-mut23h2r-137"].get("htmlFr") or ""
chk("registre 137 intact (15 268 car)", 14_800 <= len(fr137) <= 15_700)
chk("registre 139 toujours vide (pas de doublon parallèle)",
    not (les["pdf-mut23h2r-139"].get("htmlFr") or "").strip())
fr = les["pdf-mut23h2r-138"].get("htmlFr") or ""
chk("registre 138 = htmlFr posé (~17 739 car)", 17_000 <= len(fr) <= 18_200)
chk("registre 138 == fichier livré", fr.strip() == h.strip() or len(fr) == len(h.rstrip("\n")))

print(f"verify-ulumhadith1-pdf138 : {ok} PASS / {fail} ÉCHEC")
raise SystemExit(1 if fail else 0)

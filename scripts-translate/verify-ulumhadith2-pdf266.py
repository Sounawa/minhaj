#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Minhāj — Vérification de la leçon ulum-hadith-tanawi-2 / pdf-mut23h2u-266
(الدرس 12 — an-nāsiḫ wa-l-mansūḫ, p.68-71 du manuel
ulum-hadith-2-thanawi_text.pdf) : bornes p.68-71 par DOUBLE sondage (p.67 =
clôture de la leçon 11 livrée en R627 ; p.68 = bannière ad-dars 12 + 3 objectifs
+ tamhīd à double question + matn Ibn Ḥaǧǧar + gloses ; p.69-70 = définition,
trois voies de connaissance, exclusion du récit du Compagnon tardif, travail
quand la datation est impossible + schéma ; p.71 = ahtadī wa-aqtadī + taqwīm
4 items + istiṯmār + iʿdād leçon 13 ; p.72 = bannière leçon 13 أهداف الأنشطة
non touchée) ; claim atomique 19:24:39Z (trace
1a1a172f41684dc9-cron-agent-loop-202611070319, refresh ×3) ; extraction
multicouche tr-tmp/r632/ (pdftotext + PyMuPDF + tesseract 300 dpi) + recadrages
900-2400 dpi tr-tmp/r632/ (14 clichés) + lectures VLM ancrées read-*.txt
(bornées, jamais de complétion de mémoire) ; NOMBRES tranchés sur l'image
jamais devinés : [Maqāyīs al-luġa, Ibn Fāris, 5/425] (glyphes 5/4/2/5 — couche
optique « 425/5 ») ; [Fatḥ al-Magīṯ 4/53] (glyphes 4/5/3 — couche optique « 6 »
parasite) ; [Fatḥ al-Magīṯ 4/54] (glyphes 4/5/4 — couche optique « 54/4 ») ;
[Fatḥ al-Magīṯ 4/50] (glyphes 4/5/0 — couche optique « 50/4 ») ; références
hadiths portées telles qu'imprimées (Muslim, livre des bêtes sacrificielles —
consigné) ; verbe de la condition du Compagnon tardif « lam ya-taḥammil »
retenu (deux couches + lecture lettre à lettre des points) contre « lam yaḥṣul »
(lecture isolée, consignée) ; schéma à 7 branches reconstruit par recoupement
de 4 lectures VLM (sous-cases : lafẓ/maʿnā, ḥaqīqa/maǧāz, ẓāhir al-Qurʾān ;
divergences isolées consignées) ; zéro āya (nul recours au cache), zéro arabe,
zéro apostrophe droite.
Usage: python3 scripts-translate/verify-ulumhadith2-pdf266.py
"""
import json
import re

HTML = "/home/z/my-project/tr-tmp/lesson-uh2-pdf-mut23h2u-266-fr.html"
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
chk("h1 = titleFr pré-mappé « Leçon 12 : L’abrogeant (nāsiḫ) et l’abrogé (mansūḫ) »",
    hn.startswith("<h1>Leçon 12 : L’abrogeant (nāsiḫ) et l’abrogé (mansūḫ)"))
chk("h1 mentionne deuxième année", "deuxième année" in h[:500])
chk("h1 mentionne le Maqāyīs d’Ibn Fāris", "Maqāyīs al-luġa d’Ibn Fāris" in h[:2000])
chk("h1 mentionne les trois voies", "les trois voies" in h[:1800])
chk("h1 mentionne Burayda et la visite des tombes",
    "Burayda" in h[:2000] and "visite des tombes" in h[:2000])
chk("h1 mentionne Jābir et les ablutions après le feu",
    "Jābir" in h[:2400] and "ce qu’a touché le feu" in h[:2400])
chk("h1 mentionne Šaddād et Ibn ʿAbbās", "Šaddād b. Aws" in h[:2600] and "Ibn ʿAbbās" in h[:2600])
chk("h1 mentionne conquête an huit et pèlerinage d’adieu an dix",
    "conquête de La Mecque en l’an huit" in h[:2600] and "pèlerinage d’adieu en l’an dix" in h[:2600])
chk("h1 mentionne les sept manières de préférer", "sept manières de préférer" in h[:3000])
chk("h1 mentionne Luqmān et Ibn al-Aṯīr", "Luqmān" in h[:3200] and "Ibn al-Aṯīr" in h[:3400])
chk("dl.lesson-meta présent", '<dl class="lesson-meta">' in h and "<dt>Source du cours</dt>" in h)
chk("item archive.org cité", "1_20220304_20220304_2251" in h)
chk("source locale citée", "ulum-hadith-2-thanawi_text.pdf" in h)
chk("bornes p.68-71 documentées", "pages 68 à 71" in h)
chk("p.67 clôture leçon 11 (R627)", "R627" in h and "pdf-mut23h2u-265" in h)
chk("p.72 leçon 13 non touchée", "pdf-mut23h2u-267" in h and "registre vide" in h)
chk("double sondage « jamais deviné »", "jamais deviné" in h)
chk("bannière calligraphique : registre autorité + lectures divergentes consignées",
    "ad-dars 12" in h and "zéro devinette" in h and "consignées" in h)
chk("extraction multicouche tr-tmp/r632/ citée", "tr-tmp/r632/" in h)
chk("couches trois par page (incorporée, logique, OCR 300)",
    "texte incorporé" in h and "couche logique" in h and "300 points au pouce" in h)
chk("recadrages 900-2400 dpi cités", "900 à 2400 points au pouce" in h)
chk("lectures VLM ancrées citées, anti-hallucination",
    "read-*.txt" in h and "jamais de complétion" in h)

# ---- nombres miroir tranchés
chk("Maqāyīs 5/425 tranché (glyphes 5/4/2/5, couche « 425/5 »)",
    "Maqāyīs al-luġa d’Ibn Fāris, tome 5, page 425" in hn
    and "glyphes 5/4/2/5" in h and "425/5" in h)
chk("Fatḥ al-Magīṯ 4/53 tranché (glyphes 4/5/3)",
    "tome 4, page 53" in hn and "glyphes 4/5/3" in h)
chk("Fatḥ al-Magīṯ 4/54 tranché (couche « 54/4 »)",
    "tome 4, page 54" in hn and "54/4" in h)
chk("Fatḥ al-Magīṯ 4/50 tranché (couche « 50/4 »)",
    "tome 4, page 50" in hn and "50/4" in h)
chk("divergences de lecture consignées (yaḥammil/yaḥṣul, ḥukm, ḥaqīqa)",
    "lam ya-taḥammil" in h and "lam yaḥṣul" in h and "bi-l-ḥukm" in h
    and "consignée, non retenue" in h)

# ---- objectifs
chk("objectif : notion du nasḫ et ce par quoi on le connaît",
    "que je prenne connaissance de la notion du nasḫ (l’abrogation) et de ce par quoi on le connaît" in hn)
chk("objectif : distinguer abrogeant/abrogé",
    "que je distingue l’abrogeant de l’abrogé" in hn)
chk("objectif : purification de l’âme",
    "que je veille à la purification de mon âme et à son éducation" in hn)
chk("trois objectifs annoncés", "trois objectifs" in hn)

# ---- tamhīd
chk("tamhīd : reprise de la leçon 11 (contrariété/rapprochement)",
    "peut être préservé de la contrariété et peut ne pas l’être" in hn)
chk("tamhīd : double question (date connue / impossible)",
    "que faire quand la date est connue" in hn
    and "que faire quand sa connaissance est impossible" in hn)

# ---- matn + gloses
chk("matn : la postériorité s’établit, abrogeant/abrogé",
    "la postériorité s’établit alors" in hn
    and "l’abrogeant (an-nāsiḫ), et l’autre est l’abrogé (al-mansūḫ)" in hn)
chk("matn : sinon tarǧīḥ puis tawaqquf",
    "la préférence préférentielle (at-tarǧīḥ)" in hn
    and "puis la suspension (at-tawaqquf)" in hn)
chk("glose : ou non = rapprochement impossible",
    "c’est-à-dire, si le rapprochement n’est pas possible" in hn)
chk("glose : tarǧīḥ sur le modèle at-tagġlīb",
    "nom d’action sur le modèle at-tagġlīb (le fait de l’emporter), en la forme et en le sens" in hn)
chk("glose : tawaqquf = s’abstenir d’agir",
    "s’abstenir d’agir par les deux traditions quand la préférence est impossible" in hn)

# ---- istiṯmār du matn (3 extractions)
chk("extraction 1 : étapes du travail", "étapes du travail quand le rapprochement" in hn)
chk("extraction 2 : quand la préférence", "quand l’on recourt à la préférence de l’une des deux traditions" in hn)
chk("extraction 3 : quand la suspension", "quand la suspension intervient" in hn)

# ---- définition luġa
chk("luġa : élision + soleil a dénoué l’ombre",
    "appliqué à l’élision (izāla)" in hn
    and "le soleil a dénoué l’ombre (nasaḫat aš-šamsu aẓ-ẓill)" in hn)
chk("luġa : renvoi Maqāyīs 5/425", "[Maqāyīs al-luġa d’Ibn Fāris, tome 5, page 425]" in hn)

# ---- définition istiṣilāḥ
chk("istiṣilāḥ : définition complète",
    "le relèvement de l’attachement d’un statut religieux par une preuve religieuse postérieure à lui" in hn)
chk("précaution : le statut conditionné n’est pas nasḫ",
    "par précaution contre l’interdiction originelle" in hn and "ne se nomme pas nasḫ" in hn)
chk("Ibn Ḥaǧǧar écarte résumé/exception/condition",
    "le résumé global, l’exception et la condition" in hn and "il a précisé sa limite" in hn)
chk("nāsiḫ métaphorique — l’abrogeant en vérité est Dieu",
    "sa désignation par ce nom est métaphorique (maǧāz)" in hn
    and "l’abrogeant en vérité est Dieu le Très-Haut" in hn)

# ---- trois voies
chk("trois voies annoncées", "trois voies" in hn and "l’ordre n’est pas innocent" in hn)
chk("voie 1 : Burayda (Muslim), référence telle qu'imprimée consignée",
    "Nous vous avions interdit la visite des tombes" in hn and "visitez-les donc" in hn
    and "Burayda" in hn and "référence rendue telle qu’imprimée" in hn
    and "bêtes sacrificielles" in hn)
chk("voie 2 : Jābir (an-Nasāʾī), ablutions après le feu",
    "La dernière des deux attitudes du Messager de Dieu" in hn
    and "délaisser les ablutions après ce qu’a touché le feu" in hn
    and "livre de la purification, chapitre du délaissement des ablutions après ce qu’a altéré le feu" in hn)
chk("voie 2 : condition as-Saḫāwī (transmission, non opinion) + 4/53",
    "appuyé sur la transmission" in hn
    and "un effort d’opinion né d’une conjecture, ce qui n’est pas une abrogation" in hn
    and "tome 4, page 53" in hn)
chk("voie 3 : Šaddād « celui qui pratique la saignée » (al-Buḫārī)",
    "Celui qui pratique la saignée et celui sur qui on la pratique rompent leur jeûne" in hn
    and "livre du jeûne, chapitre de la saignée et de la purgation pour celui qui jeûne" in hn)
chk("voie 3 : Ibn ʿAbbās « il jeûnait » (al-Buḫārî)",
    "se fit pratiquer la saignée alors qu’il jeûnait" in hn)
chk("voie 3 : datation an huit / an dix + pas de Ramaḍān après l’adieu + 4/54",
    "l’an huit de l’Hégire" in hn and "en l’an dix" in hn
    and "il n’y eut plus de Ramaḍān dans la vie du Prophète" in hn
    and "tome 4, page 54" in hn)

# ---- exclusion du Compagnon tardif
chk("exclusion : Compagnon tardif en l’islam",
    "Compagnon tardif en l’islam" in hn
    and "entendu d’un autre Compagnon plus ancien" in hn)
chk("réintégration sous condition (rien reçu avant l’islam)",
    "déclaration explicite de son audition" in hn
    and "n’ait rien reçu du Prophète" in hn and "avant son islam" in hn)

# ---- section 2
chk("section 2 : critères du texte ou de la chaîne",
    "critères de préférence relatifs au texte ou à la chaîne" in hn)
chk("section 2 : la suspension recueille le cas",
    "alors la suspension" in hn and "réglé selon cet ordre" in hn)
chk("suspension préférable à la chute mutuelle + raison",
    "plus digne que l’expression par la chute mutuelle" in hn
    and "par rapport à celui qui pèse en l’état présent" in hn
    and "ce qui lui était caché" in hn)

# ---- schéma des sept manières
chk("schéma : sept branches annoncées", "schéma à sept branches" in hn)
chk("branche : état du rapporteur", "par l’état du rapporteur (bi-ḥāl ar-rāwī)" in hn)
chk("branche : manière de recevoir", "par la manière dont il le reçoit (bi-ṭarīqa taḥammulih)" in hn)
chk("branche : façon de rapporter + sous-case lafẓ/maʿnā",
    "par la façon de rapporter (bi-kayfiyyat ar-riwāya)" in hn
    and "rapporté par la formulation (lafẓ) sur ce qui est rapporté par le sens (maʿnā)" in hn)
chk("branche : moment d’arrivée", "par le moment d’arrivée (bi-waqt al-wurūd)" in hn)
chk("branche : formulation du texte + sous-case ḥaqīqa/maǧāz",
    "par la formulation du texte (bi-lafẓ al-ḫabar)" in hn
    and "l’acception réelle (ḥaqīqa) sur l’acception figurée (maǧāz)" in hn)
chk("branche : par le statut", "par le statut (bi-l-ḥukm)" in hn)
chk("branche : considération particulière + ẓāhir du Coran",
    "par une considération particulière (bi-amr ḫāṣṣ)" in hn
    and "s’accorde avec la portée apparente du Coran" in hn)

# ---- ahtadī wa-aqtadī
chk("rubrique ahtadī wa-aqtadī", "Je m’inspire et j’inspire (ahtadī wa-aqtadī)" in hn)
chk("citation Luqmān (Muwaṭṭaʾ) : assieds-toi avec les savants",
    "assieds-toi avec les savants, et presse-les de tes genoux" in hn
    and "la lumière de la sagesse" in hn and "l’averse du ciel" in hn)
chk("renvoi Muwaṭṭaʾ livre de la science",
    "livre de la science, chapitre de ce qui est venu sur la quête de la science" in hn)

# ---- évaluation (4 items)
chk("évaluation : 4 items", "Quatre items" in hn)
chk("évaluation : voies de connaissance", "je précise les voies de connaissance du nasḫ" in hn)
chk("évaluation : abrogation par opinion ?",
    "est-il permis de prétendre à l’abrogation par l’opinion et l’effort personnel" in hn)
chk("évaluation : critères de préférence",
    "ce par quoi l’une des deux traditions est préférée à l’autre" in hn)
chk("évaluation : fruits de la fréquentation",
    "fruits de la fréquentation des savants et de l’audition" in hn)

# ---- exploitation
chk("exploitation : citation Ibn al-Aṯīr (mutawātir/āḥād, fonction du faqīh) + 4/50",
    "La connaissance du massivement transmis (mutawātir) et du singulier (āḥād)" in hn
    and "elles relèvent plutôt de la fonction du juriste (faqīh)" in hn
    and "un surcroît de mérite et une perfection dans le choix" in hn
    and "tome 4, page 50" in hn)
chk("exploitation : rapport au ḥadīṯ + synthèse rédactionnelle",
    "le rapport de l’abrogeant et de l’abrogé à la science du ḥadīṯ" in hn
    and "synthèse rédactionnelle" in hn)

# ---- préparation leçon suivante
chk("iʿdād : coopération pour la leçon des activités",
    "prépare, en coopération avec tes amis, la leçon des activités" in hn)
chk("sondage p.72 : trois objectifs des activités",
    "objectifs des activités" in hn and "trois objectifs" in hn
    and "que je consolide mes connaissances et que j’investisse mes acquis dans l’extraction des contenus du ḥadīṯ" in hn
    and "que je sécurise mes acquis par les applications pratiques" in hn
    and "que je coopère avec mes amis pour développer mes habiletés et mes capacités dans les sciences du ḥadīṯ" in hn)

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
chk("registre 263 intact (33 055 car)", len(les["pdf-mut23h2u-263"].get("htmlFr") or "") == 33055)
chk("registre 264 intact (25 976 car)", len(les["pdf-mut23h2u-264"].get("htmlFr") or "") == 25976)
chk("registre 265 intact (31 943 car)", len(les["pdf-mut23h2u-265"].get("htmlFr") or "") == 31943)
chk("registre 267 non touché (htmlFr vide)", (les["pdf-mut23h2u-267"].get("htmlFr") or "") == "")
chk("registre 268 non touché (htmlFr vide)", (les["pdf-mut23h2u-268"].get("htmlFr") or "") == "")
fr = les["pdf-mut23h2u-266"].get("htmlFr") or ""
if fr:
    chk("registre 266 = htmlFr posé (~30 000 car)", 27_000 <= len(fr) <= 36_000)
    chk("registre 266 == fichier livré", fr.strip() == h.strip())
else:
    chk("registre 266 encore vide (avant hand-set)", True)
chk("titleAr pré-mappé 266", les["pdf-mut23h2u-266"].get("titleAr") == "الدرس 12 : الناسخ والمنسوخ")
chk("titleFr pré-mappé 266 aligné au h1",
    (les["pdf-mut23h2u-266"].get("titleFr") or "").replace("'", "’").startswith("Leçon 12 : L’abrogeant"))
reg1 = json.load(open(REG1, encoding="utf-8"))
l1 = {str(d.get("docId", "")): d for d in reg1["lessons"]}
chk("registre livre 1 : 141 intact (24 319 car)", len(l1["pdf-mut23h2r-141"].get("htmlFr") or "") == 24319)
chk("registre livre 1 : 140 intact (16 018 car)", len(l1["pdf-mut23h2r-140"].get("htmlFr") or "") == 16018)

print(f"verify-ulumhadith2-pdf266 : {ok} PASS / {fail} ÉCHEC")
raise SystemExit(1 if fail else 0)

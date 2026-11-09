#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Minhāj — Vérification de la leçon ulum-hadith-tanawi-2 / pdf-mut23h2u-279
(الدرس 25 : أنشطة تطبيقية — p.129-130 du manuel ulum-hadith-2-thanawi_text.pdf)
: bornes p.129-130 par sondage image (p.128 = clôture de la leçon 24 livrée
R658, jamais retouchée ; p.129 = bannière médaillon « 25 » + 4 objectifs des
activités + lecture à deux paragraphes + organigramme أطبق à cinq étapes ;
p.130 = تخريج المطلوب الحديث + ḥadīṯ de Ṭalḥa ibn ʿUbayd Allāh avec isnad
complet et bracket [Sunan at-Tirmiḏī, abwāb al-manāqib, bāb fī manāqib ʿUṯmān
ibn ʿAffān] + six consignes dont la quatrième à quatre sous-points + al-iʿdād
al-qiblī à UNE ligne ; p.131 = ouverture de la leçon 26 warašāt — sondage, non
touchée, registre vide). Adjudications documentées (QUINZE lectures d'images,
tr-tmp/qa-crops-r659-uh2/ + 3 lectures directes opérateur) : isnad mot à mot
(banī Zuhra contre couche « aḏ-ḏahrī » récusée, corroboré EN LIGNE hdith.com +
cours al-ʿAbbād) ; matn avec incise « — yaʿnī fī l-ǧanna — » entre tirets
(image directe 1200 dpi, corroboration alsunniah.com) ; ibn ʿAffān confirmé
(couche texte ×2 + pleine page + lecture directe contre 2 zooms VLM discordants)
; corroboration dorar.net (at-Tirmiḏī 3698, al-Albānī ḍaʿīf ǧiddan) ; écart
canonique de l'incise documenté (Riyāḍ an-Niḍra : « wa-lam yaqul : fī l-ǧanna »)
; organigramme : wa-šawāhidihi / ṭuruq wa-šawāhid rendus par lecture directe
1000 dpi contre 2 VLM « wa-ruwāh » récusés ; aqraʾ : ʿuraḍat (contre ʿurrifat),
al-mutaʿalliqa bi-ʿulūm al-ḥadīṯ (contre li-t-taʿilla), wa-taqrīban (couche
réinversée + image), al-maqṣūd (contre al-quṣūd), al-iqtiṣār (contre
al-iqtiṣād), miftāḥ al-ʿināya (contre miftāḥan li-ʿināya), wa-an takūn (rendu
1500 dpi) ; al-iʿdād al-qiblī confirmé lettre par lettre 900 dpi contre
« at-taqlīdī » récusé ; a-taʿāwanu confirmé (couche ×2 + image) ; ZÉRO ĀYA
(cache coranique non sollicité). Usage: python3
scripts-translate/verify-ulumhadith2-pdf279.py
"""
import json
import re

HTML = "/home/z/my-project/tr-tmp/lesson-uh2-pdf-mut23h2u-279-fr.html"
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
chk("h1 = titleFr pré-mappé « Leçon 25 : Activités pratiques »",
    hn.startswith("<h1>Leçon 25 : Activités pratiques"))
chk("h1 mentionne deuxième année", "deuxième année" in h[:500])
chk("h1 mentionne les quatre objectifs d’activités", "quatre objectifs d’activités" in h[:1500])
chk("h1 mentionne l’organigramme des cinq étapes", "cinq étapes" in h[:3000])
chk("h1 mentionne le ḥadīṯ de Ṭalḥa ibn ʿUbayd Allāh", "Ṭalḥa ibn ʿUbayd Allāh" in h[:4000])
chk("h1 mentionne le matn (à chaque prophète un compagnon, mon compagnon ʿUṯmān)",
    "à chaque prophète un compagnon" in h[:3000] and "est ʿUṯmān" in h[:3600])
chk("h1 mentionne l’isnad complet (Abū Hišām ar-Rifāʿī, Yaḥyā ibn al-Yamān, banū Zuhra)",
    "Abū Hišām ar-Rifāʿī" in h[:4200] and "Yaḥyā ibn al-Yamān" in h[:4200]
    and "banū Zuhra" in h[:4200])
chk("h1 mentionne la source Sunan at-Tirmiḏī (vertus de ʿUṯmān ibn ʿAffān)",
    "Sunan at-Tirmiḏī" in h[:4600] and "ʿUṯmān ibn ʿAffān" in h[:4600])
chk("h1 mentionne les six consignes et l’arborescence du sanad",
    "six consignes" in h[:5200] and "arborescence" in h[:5600])
chk("h1 mentionne la préparation (équipes, ateliers du soutien et de l’application)",
    "équipes de travail" in h[:6200] and "ateliers du soutien et de l’application" in h[:6400])
chk("dl.lesson-meta présent", '<dl class="lesson-meta">' in h and "<dt>Source du cours</dt>" in h)
chk("item archive.org cité", "1_20220304_20220304_2251" in h)
chk("source locale citée", "ulum-hadith-2-thanawi_text.pdf" in h)
chk("bornes p.129-130 documentées", "pages 129 à 130" in h)
chk("p.128 clôture leçon 24 (R658) jamais retouchée", "livrée R658 — jamais retouchée" in h)
chk("p.131 leçon 26 sondage, non touchée, registre vide",
    "la page 131 ouvre la leçon 26" in h and "non touchée, registre vide" in h)
chk("QUINZE lectures d’images consignées", "QUINZE lectures d’images" in h and "qa-crops-r659-uh2" in h)
chk("couche texte gravement garblée documentée", "gravement garblée" in h and "aḏ-ḏahrī" in h)
chk("isnad corroboré EN LIGNE (hdith.com + cours al-ʿAbbād)",
    "[hdith.com" in h and "al-ʿAbbād" in h)
chk("matn incise corroborée EN LIGNE (alsunniah.com)", "[alsunniah.com" in h)
chk("ibn ʿAffān confirmé contre 2 zooms VLM discordants, discordance consignée",
    "ibn ʿAffān" in h and "discordantes" in h and "discordance consignée" in h)
chk("corroboration dorar.net (at-Tirmiḏī 3698, ḍaʿīf ǧiddan)",
    "dorar.net" in h and "3698" in h and "ḍaʿīf ǧiddan" in h)
chk("écart canonique de l’incise documenté (Riyāḍ an-Niḍra)",
    "écart canonique consigné" in h and "Riyāḍ an-Niḍra" in h)
chk("organigramme adjudiqué par lecture directe (contre « wa-ruwāh »)",
    "wa-šawāhidihi" in h and "wa-ruwāh" in h and "récusées par image" in h)
chk("première étape « maṣādirihi al-aṣliyya » + [point d’interrogation] scan consigné",
    "maṣādirihi al-aṣliyya" in h and "[point d’interrogation de la couche texte]" in h)
chk("aqraʾ adjudications (ʿuraḍat, ʿulūm, wa-taqrīban, al-maqṣūd, al-iqtiṣār, miftāḥ al-ʿināya, wa-an)",
    "ʿuraḍat" in h and "ʿurrifat" in h and "wa-taqrīban" in h and "al-maqṣūd" in h
    and "al-iqtiṣār" in h and "miftāḥ al-ʿināya" in h and "wa-an takūn" in h)
chk("al-iʿdād al-qiblī contre at-taqlīdī récusé (900 dpi lettre par lettre)",
    "at-taqlīdī" in h and "lettre par lettre" in h)
chk("a-taʿāwanu confirmé (couche ×2 + image)", "a-taʿāwanu" in h and "forme VI" in h)
chk("folios 129/130 confirmés chiffres occidentaux (couche « 19 » récusée)",
    "chiffres occidentaux par zoom 300 dpi" in h and "«\u202f&nbsp; 19&nbsp;\u202f»" in h)
chk("ZÉRO ĀYA documenté", "ZÉRO ĀYA" in h and "cache coranique non sollicité" in h)
chk("GARDE-DOUBLON consigné (hadith-2es/tafsir-5ep CLOS, leçon 24/26 jamais touchées)",
    "hadith-2es CLOS 30/30" in h and "tafsir-5ep CLOS 122/122" in h
    and "leçon 26 jamais touchée" in h)
chk("slot parallèle sous-agent R660 consigné", "sous-agent R660" in h)

# ---- objectifs
chk("section objectifs présente", "Les objectifs des activités (ahdāf al-anšīṭa)" in h)
chk("objectif 1 (j’affermiss mes connaissances théoriques antérieures)",
    "que j’affermiss mes connaissances théoriques antérieures" in h)
chk("objectif 2 (développe mes compétences dans la recherche appliquée pratique)",
    "que je développe mes compétences théoriques dans la recherche appliquée pratique" in h)
chk("objectif 3 (finalité de la maîtrise de la terminologie du ḥadīṯ)",
    "que je saisisse la finalité de la maîtrise de la terminologie du ḥadīṯ et l’importance de cela dans le champ des applications" in h)
chk("objectif 4 (m’exerce à l’étude des ḥadīṯs, étude appliquée et pratique)",
    "que je m’exerce à l’étude des ḥadīṯs par une étude appliquée et pratique" in h)

# ---- lecture (aqraʾ)
chk("section lecture présente", "La lecture (aqraʾ)" in h)
chk("P1 « Ont été présentés, dans ce qui a précédé »", "Ont été présentés, dans ce qui a précédé" in h)
chk("P1 « distinction entre l’authentique et le faible »",
    "à la distinction entre l’authentique et le faible" in h)
chk("P2 « approcher les applications pratiques »", "pour approcher les applications pratiques" in h)
chk("P2 « l’économie sur l’essentiel et l’important »",
    "l’économie sur l’essentiel et l’important" in h)
chk("P2 « clef du soin apporté aux applications »",
    "la clef du soin apporté aux applications et de l’expansion en elles" in h)

# ---- application (organigramme)
chk("section application présente", "L’application (aṭbiq)" in h)
chk("titre organigramme (étude et takhrīj d’un ḥadīṯ)",
    "les étapes de l’étude d’un ḥadīṯ et de son takhrīj" in hn.lower() or "les étapes de l’étude d’un ḥadīṯ et de son takhrīj" in h)
chk("intitulé imprimé de l’organigramme", "ḫuṭuwāt dirāsa wa-taḫrīǧ ḥadīṯ" in h)
chk("étape 1 (présentation, extraction des sources originelles)",
    "la présentation du ḥadīṯ que l’on veut étudier, et son extraction de ses sources originelles" in h)
chk("étape 2 (voies et récits corroborants šawāhid)",
    "la recherche des voies du ḥadīṯ et de ses récits corroborants (šawāhid)" in h)
chk("étape 3 (sanad : connexion, probité, maîtrise)",
    "l’étude du sanad du ḥadīṯ originel (la connexion du sanad, la probité des narrateurs, la maîtrise (ḍabṭ) des narrateurs...)" in h)
chk("étape 4 (étude des voies et des récits corroborants)",
    "l’étude des voies et des récits corroborants du ḥadīṯ" in h)
chk("étape 5 (jugement global après l’étude des voies et šawāhid)",
    "le jugement global sur le ḥadīṯ originel (après l’étude de ses voies et de ses récits corroborants)" in h)

# ---- takhrīj requis
chk("section takhrīj requise présente", "Le takhrīj du ḥadīṯ requis (tahrīǧ al-maṭlūb" in h)
chk("isnad : Abū Hišām ar-Rifāʿī", "Nous a rapporté Abū Hišām ar-Rifāʿī, qui a dit" in h)
chk("isnad : Yaḥyā ibn al-Yamān", "nous a rapporté Yaḥyā ibn al-Yamān" in h)
chk("isnad : cheikh des banū Zuhra (contre couche aḏ-ḏahrī)",
    "d’un cheikh des banū Zuhra" in h)
chk("isnad : al-Ḥāriṯ ibn ʿAbd ar-Raḥmān ibn Abī Ḏiʾāb",
    "de al-Ḥāriṯ ibn ʿAbd ar-Raḥmān ibn Abī Ḏiʾāb" in h)
chk("isnad : Ṭalḥa ibn ʿUbayd Allāh", "de Ṭalḥa ibn ʿUbayd Allāh, qui a dit" in h)
chk("formule prophétique", "le Prophète, que la prière et le salut de Dieu soient sur lui, a dit" in h)
chk("matn (à chaque prophète un compagnon, mon compagnon — paradis — ʿUṯmān)",
    "&nbsp;à chaque prophète un compagnon, et mon compagnon — c’est-à-dire dans le paradis — est ʿUṯmān.&nbsp;\u202f»" in h)
chk("bracket source (Sunan at-Tirmiḏī, abwāb al-manāqib, ʿUṯmān ibn ʿAffān)",
    "[Sunan at-Tirmiḏī, les chapitres des vertus (abwāb al-manāqib), le chapitre des vertus de ʿUṯmān ibn ʿAffān, que Dieu l’agrée.]" in h)

# ---- consignes
chk("section consignes présente", "Les consignes du travail appliqué" in h)
chk("consigne 1 (j’écris le ḥadīṯ par son texte et son sanad)",
    "j’écris le ḥadīṯ tel qu’il est, par son texte (lafẓ) et son sanad" in h)
chk("consigne 2 (recherche dans ses éditions originelles)",
    "je recherche le ḥadīṯ, son sanad et son texte dans ses éditions originelles" in h)
chk("consigne 3 (voies et récits corroborants)",
    "je recherche les voies du ḥadīṯ et ses récits corroborants" in h)
chk("consigne 4 (sanad originel, en suivant ce qui suit)",
    "j’étudie le sanad du ḥadīṯ originel, en suivant ce qui suit" in h)
chk("sous-point 4a (tašǧīr du sanad et extraction des narrateurs)",
    "je procède à l’arborescence (tašǧīr) du sanad du ḥadīṯ et à l’extraction de ses narrateurs" in h)
chk("sous-point 4b (probité et maîtrise de chaque narrateur)",
    "je recherche chaque narrateur sous l’angle de la probité (ʿadāla) et de la maîtrise (ḍabṭ)..." in h)
chk("sous-point 4c (connexion du sanad)", "je recherche la connexion du sanad" in h)
chk("sous-point 4d (degré du sanad originel)",
    "je montre le degré du sanad du ḥadīṯ originel." in h)
chk("consigne 5 (degré de chaque voie ou récit corroborant)",
    "je montre le degré de chaque voie ou de chaque récit corroborant" in h)
chk("consigne 6 (degré final après l’achèvement de la recherche)",
    "je montre le degré du ḥadīṯ originel après que la recherche de ses voies et de ses récits corroborants a été achevée." in h)

# ---- iʿdād al-qiblī
chk("préparation leçon suivante présente", "La préparation de la leçon suivante (al-iʿdād al-qiblī)" in h)
chk("iʿdād : une seule ligne (collaboration, équipes, ateliers du soutien et de l’application)",
    "Je collabore avec mes amis pour constituer des équipes de travail afin de réaliser les activités des ateliers (warašāt) du soutien (ad-daʿm) et de l’application (at-taṭbīq)." in h)

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
chk("registre 274 intact (28 082 car)", len(les["pdf-mut23h2u-274"].get("htmlFr") or "") == 28082)
chk("registre 275 intact (39 200 car)", len(les["pdf-mut23h2u-275"].get("htmlFr") or "") == 39200)
chk("registre 276 intact (25 364 car)", len(les["pdf-mut23h2u-276"].get("htmlFr") or "") == 25364)
chk("registre 278 intact (26 289 car)", len(les["pdf-mut23h2u-278"].get("htmlFr") or "") == 26289)
fr = les["pdf-mut23h2u-279"].get("htmlFr") or ""
if fr:
    chk("registre 279 = htmlFr posé (14 000-40 000 car)", 14_000 <= len(fr) <= 40_000)
    chk("registre 279 == fichier livré", fr.strip() == h.strip())
else:
    chk("registre 279 encore vide (avant hand-set)", True)
fr277 = les["pdf-mut23h2u-277"].get("htmlFr") or ""
chk("registre 277 jamais écrit par ce worker (vide ou contenu d’un autre)",
    fr277 == "" or fr277 != fr)
chk("titleAr pré-mappé 279 intact (leçon 25)",
    les["pdf-mut23h2u-279"].get("titleAr") == "الدرس 25 : أنشطة تطبيقية")
chk("titleFr pré-mappé 279 aligné au h1 (apostrophes normalisées)",
    (les["pdf-mut23h2u-279"].get("titleFr") or "").replace(chr(39), "\u2019")
    == "Leçon 25 : Activités pratiques")

print(f"verify-ulumhadith2-pdf279 : {ok} PASS / {fail} ÉCHEC")
raise SystemExit(1 if fail else 0)

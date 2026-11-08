#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Minhāj — Vérification de la leçon ulum-hadith-tanawi-2 / pdf-mut23h2u-272
(الدرس 18 : أسباب الطعن في الراوي — asbāb aṭ-ṭaʿn fī ar-rāwī, p.93-96 du manuel
ulum-hadith-2-thanawi_text.pdf) : bornes p.93-96 par sondage image (p.92 = clôture
de la leçon 17, livrée R648, docId pdf-mut23h2u-271 ; p.93 = bannière médaillon « 18 »
+ 3 objectifs + tamhīd aux dix motifs avec double question + matn Ibn Ḥaǧar aux dix
causes + gloses غفلته/وهمه + استخلاص ; p.94 = التبسيط (lu à l’image contre « التحليل »
de la couche texte) + أولا 5 causes de la probité + ثانيا : grave erreur 1, négligence 2,
illusion 3 (établie par image contre la fusion OCR), contradiction 4 ; p.95 = mauvaise
garde 5 (p95-item5) + schéma arborescent 2 branches 5+5 + أهدى وأقتدي الخطيب
[الجامع 1/5] + التقويم 3 ; p.96 = الاستثمار النووي [التقريب والتيسير، ص 31 imprimé —
inversion «13» de la couche décodée récusée par zoom image p96-num2] + 2 consignes +
الإعداد القبلي 2 items (image p96-i3dadi2, « من أسباب رد الحديث » contre bruit OCR) ;
p.97 = ouverture leçon 19 « الموضوع والمتروك » (sondage, non touchée, registre vide).
Adjudications documentées : ordre des dix causes par double lecture image (négligence
en 4ᵉ) ; anomalie de point sur le 4ᵉ terme (ghayn non pointé → غفلته par quadruple
convergence) ; « إمّا » imprimé ; objectif 3 « أن أجتنب ما يخل بالعدالة والضبط » ;
« لقلة من يسلم منها » ; « والأول قد يقدح في صحة الإسناد والمتن جميعا » ; « سواء كان
مساويا أو أكثر » ; citation Nawawī « من وجوه ضعيفة » + clause « بل ما كان ضعفه... »
telle qu’imprimée ; ZÉRO ĀYA (cache coranique non sollicité).
Usage: python3 scripts-translate/verify-ulumhadith2-pdf272.py
"""
import json
import re

HTML = "/home/z/my-project/tr-tmp/lesson-uh2-pdf-mut23h2u-272-fr.html"
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
hn = re.sub(r" +", " ", h.replace("&nbsp;", " ").replace("\u202f", "").replace("\u2009", ""))

# ---- h1 et méta
chk("h1 = titleFr pré-mappé « Leçon 18 : Les motifs de discrédit du transmetteur »",
    hn.startswith("<h1>Leçon 18 : Les motifs de discrédit du transmetteur"))
chk("h1 mentionne deuxième année", "deuxième année" in h[:500])
chk("h1 mentionne les dix motifs de l’atteinte portée aux hommes de la chaîne",
    "les dix motifs de l’atteinte (aṭ-ṭaʿn) portée aux hommes de la chaîne (riǧāl al-isnād)" in h[:1200])
chk("h1 mentionne les dix causes nom à nom",
    "le mensonge (al-kidib)" in h[:900] and "la mauvaise garde de la mémoire (sūʾ al-ḥifẓ)" in h[:900])
chk("h1 mentionne cinq et cinq (probité / précision)",
    "cinq relevantes de la probité (al-ʿadāla)" in h[:1000] and "cinq relevantes de la précision (aḍ-ḍabṭ)" in h[:1000])
chk("h1 mentionne l’exposition (at-tabṣīṭ)", "l’exposition (at-tabṣīṭ)" in h[:1300])
chk("h1 mentionne al-Ḫaṭīb al-Baġdādī et an-Nawawī",
    "al-Ḫaṭīb al-Baġdādī" in h[:3200] and "an-Nawawī" in h[:3600])
chk("dl.lesson-meta présent", '<dl class="lesson-meta">' in h and "<dt>Source du cours</dt>" in h)
chk("item archive.org cité", "1_20220304_20220304_2251" in h)
chk("source locale citée", "ulum-hadith-2-thanawi_text.pdf" in h)
chk("bornes p.93-96 documentées", "pages 93 à 96" in h)
chk("p.92 clôture leçon 17 (R648, 271)", "R648" in h and "pdf-mut23h2u-271" in h)
chk("p.97 leçon 19 sondée, non touchée, registre vide",
    "la leçon 19" in h and "non touchée" in h and "registre vide" in h)
chk("sondage « jamais devinées »", "jamais devinées" in h)
chk("matière multi-couches citée (uh2-l272-raw.txt) + takeover R653",
    "uh2-l272-raw.txt" in h and "takeover légal R653" in h)
chk("ONZE lectures d’images consignées",
    "ONZE lectures d’images" in h and "p93-matn-box.png" in h and "p93-l2-zoom2.png" in h
    and "p94-titre2.png" in h and "p94-item3.png" in h and "p95-item5.png" in h
    and "p96-citation.png" in h and "p96-num2.png" in h and "p96-i3dadi2.png" in h)
chk("ORDRE DES DIX CAUSES documenté (négligence en 4e)",
    "ORDRE DES DIX CAUSES" in h and "la négligence en quatrième position" in h)
chk("ANOMALIE DE POINT documentée (ghayn effacé, quadruple convergence)",
    "ANOMALIE DE POINT" in h and "quadruple convergence" in h)
chk("en-tête at-tabṣīṭ récusé à l’image contre at-taḥlīl",
    "at-tabṣīṭ" in h and "at-taḥlīl" in h and "récusation documentée" in h)
chk("renvoi page 31 imprimé, inversion 13 récusée par zoom",
    "page 31" in h and "l’inversion mécanique" in h and "non à l’image" in h)
chk("zéro āya (cache coranique non sollicité)",
    "ZÉRO ĀYA" in h and "cache coranique non sollicité" in h)

# ---- objectifs (3)
chk("objectif 1 : reconnaître les motifs de l’atteinte",
    "que je reconnaisse les motifs de l’atteinte portée au rapporteur" in hn)
chk("objectif 2 : distinguer les motifs", "que je distingue entre les motifs de l’atteinte portée au rapporteur" in hn)
chk("objectif 3 : éviter ce qui atteint la probité et la précision (image)",
    "que j’évite ce qui atteint la probité (al-ʿadāla) et la précision (aḍ-ḍabṭ)" in hn)

# ---- tamhīd + matn
chk("tamhīd : dix choses + plus graves certaines",
    "se fait par dix choses" in hn and "plus graves dans l’atteinte et le dénigrement" in hn)
chk("tamhīd : double question des cinq et des cinq",
    "les cinq relevantes de la probité" in hn and "les cinq relevantes de la précision" in hn)
chk("matn : ordre adjudiqué — mensonge, soupçon, grave erreur, négligence (4e)",
    "soit que le rapporteur mente (li-kadib ar-rāwī)" in hn
    and "soupçonné de cela (tuhmatihi bi-dālik)" in hn
    and "la gravité de son erreur (fuḥš ġalaṭih), soit sa négligence (ġafla)" in hn)
chk("matn : impiété, illusion, contradiction, ignorance, innovation, mauvaise garde",
    "son impiété (fušūq)" in hn and "son illusion (wahm)" in hn
    and "sa contradiction (muḫālafa)" in hn and "son ignorance (ǧahāla)" in hn
    and "son innovation (bidʿa)" in hn and "la mauvaise garde de sa mémoire (sūʾ ḥifẓ)" in hn)

# ---- gloses + istiḫlāṣ
chk("glose négligence : origine ġafl + quitte par inadvertance + peut être par dessein",
    "son origine est ġafl" in hn and "quitter une chose par inadvertance" in hn
    and "peut arriver par dessein" in hn)
chk("glose illusion : sukūn du hāʾ = tawahhum + sous le doute + fath = ġalaṭ + le premier",
    "avec le sukūn du hāʾ est le supposé (at-tawahhum)" in hn
    and "au-dessous du degré du doute" in hn and "avec l’ouverture du hāʾ, l’erreur (al-ġalaṭ)" in hn
    and "le visé ici est le premier" in hn)
chk("istiḫlāṣ : motifs relevantes de la probité",
    "les motifs de l’atteinte portée au rapporteur relevantes de la probité" in hn)

# ---- tabṣīṭ 1 : probité (5)
chk("intro tabṣīṭ : double question + deux familles + illusion 3e de la précision",
    "la double question des cinq et des cinq" in hn
    and "l’illusion, dont la glose lexicale a été donnée sous les gloses, occupe la troisième place" in hn)
chk("probité 1 : mensonge — le plus grave + genre à part + avant tout pour sa laideur",
    "il en est le plus grave des types" in hn and "comme un genre à part" in hn
    and "avant tout le reste pour sa laideur" in hn)
chk("probité 2 : soupçon — matrūk + cela viendra",
    "« le délaissé » (al-matrūk), et cela viendra" in hn)
chk("probité 3 : fušūq — parole ou acte + mécréance hors du propos + musulman",
    "par la parole ou par l’acte" in hn and "hors du propos" in hn
    and "le discours porte sur le rapporteur musulman" in hn)
chk("probité 3 : ʿumūm wa-ḫuṣūṣ muṭlaq + fusuq yasdiqu ʿalā kull mā yasdiq ʿalayhi l-kidib",
    "inclusion générale et absolue (ʿumūm wa-ḫuṣūṣ muṭlaq)" in hn
    and "la première est plus spécifique, la seconde plus générale" in hn
    and "sans la réciproque" in hn)
chk("probité 4 : ǧahāla — ni taʿdīl ni taǧrīḥ maʿīn + taǧrīḥ exige motif + ʿadl/ṯiqa suffisent",
    "ni appoint ni dénigrement déterminés (taʿdīl wa-lā taǧrīḥ maʿīn)" in hn
    and "tant que son motif n’a pas été exposé" in hn
    and "équitable, ou digne de foi, par exemple" in hn)
chk("probité 5 : bidʿa — conviction sans fondement propre ou hors fondement général",
    "la conviction (iʿtiqād) d’une chose qui n’a pas de fondement propre" in hn
    and "sous un fondement général, avec son rapport au religion" in hn)

# ---- tabṣīṭ 2 : précision (5)
chk("précision 1 : faḥš ġalaṭ — erreur > exactitude + salama kulliyya impossible",
    "que son erreur soit plus nombreuse que son exactitude" in hn
    and "la préservation totale de l’erreur, elle n’est pas possible" in hn)
chk("précision 2 : ġafla — visé la fréquence + négligence seule pas motif + rareté des préservés (image)",
    "le visé est la fréquence de sa négligence" in hn
    and "la négligence seule n’est pas un motif d’atteinte" in hn
    and "pour la rareté de ceux qui en sont préservés" in hn)
chk("précision 3 : wahm — narration sur le mode du supposé + isnaad le plus fréquent + matn insertion",
    "la narration du ḥadīṯ sur le mode du supposé (ʿalā sabīl at-tawahhum)" in hn
    and "cela tombe dans la chaîne, et c’est le plus fréquent" in hn
    and "comme l’insertion d’un ḥadīṯ dans un autre ḥadīṯ" in hn)
chk("précision 3 : le premier peut compromettre isnaad ET matn ensemble (image)",
    "le premier peut compromettre l’authenticité de la chaîne et du texte ensemble" in hn)
chk("précision 4 : muḫālafa — aš-šāḏḏ un seul type + ṯiqa/ṣadūq + nombre de thiqāt",
    "ne s’applique qu’à un seul type" in hn
    and "la contradiction du digne de foi (aṯ-ṯiqa) ou du véridique (aṣ-ṣadūq) par un rapporteur plus fiable que lui" in hn
    and "dont la multitude et l’accord imposent de préférer leur narration sur la sienne" in hn
    and "fût-il plus fiable que chacun d’eux si ce seul était isolé" in hn)
chk("précision 5 : sūʾ ḥifẓ — erreur pas moindre que l’exactitude, égale ou plus + acceptable",
    "que son erreur ne soit pas moindre que son exactitude, qu’elle soit égale ou plus grande" in hn
    and "elle est acceptable (maqbūl)" in hn)
chk("précision 5 : différence avec faḥš al-ġalaṭ (fréquence contre non-infériorité)",
    "la gravité de l’erreur est portée sur sa fréquence" in hn
    and "la mauvaise garde sur ce que l’erreur ne soit pas moindre que l’exactitude" in hn)

# ---- schéma + ahtadī
chk("schéma : racine + deux branches + cinq feuilles chacune (image)",
    "Le manuel récapitule les dix causes dans un schéma arborescent" in hn
    and "la branche de la probité (al-ʿadāla), aux cinq feuilles" in hn
    and "la branche de la précision (aḍ-ḍabṭ), aux cinq feuilles" in hn
    and "la contradiction de plus fiable que lui, la mauvaise garde de la mémoire" in hn)
chk("ahtadī : al-Ḫaṭīb + courtoisie/humilité/intégrité + percussion des oreilles",
    "L’imām al-Ḫaṭīb al-Baġdādī, que Dieu lui fasse miséricorde, a dit" in hn
    and "les plus accomplis des hommes en courtoisie (adab)" in hn
    and "la perpétuelle percussion de leurs oreilles" in hn)
chk("ahtadī : biographie des gens de sa maison et compagnons + voies des traditionnistes + exploits",
    "les gens de sa maison et de ses compagnons" in hn
    and "des voies des traditionnistes" in hn and "des exploits des anciens" in hn)
chk("ahtadī : prendront les plus beaux + détourneront des plus viles",
    "ils prendront donc les plus beaux et les meilleurs de ces choses" in hn
    and "ils se détourneront des plus viles et des plus basses" in hn)
chk("ahtadī : renvoi al-Ǧāmiʿ 1/5 rendu tel qu’imprimé (tome un, page cinq)",
    "al-Ǧāmiʿ li-aḫlāq ar-rāwī wa-ādāb as-sāmiʿ (le recueil des mœurs du rapporteur et des usages de l’auditeur)" in hn
    and "tome un, page cinq" in hn)

# ---- taqwīm + istiṯmār + iʿdād
chk("taqwīm 1 : négligence restreinte à la fréquence",
    "ont restreint la négligence du rapporteur à la fréquence" in hn)
chk("taqwīm 2 : différence mensonge/soupçon",
    "la différence entre le mensonge du rapporteur et le soupçon de mensonge à son encontre" in hn)
chk("taqwīm 3 : effet de l’étude du ḥadīṯ sur l’étudiant",
    "l’effet de l’étude du ḥadīṯ sur l’étudiant en science" in hn)
chk("istiṯmār : Nawawī citation — wuǧūh faibles + pas requis ḥasan de l’ensemble",
    "des voies (wuǧūh) faibles" in hn and "il n’est pas requis qu’un ḥasan résulte de leur ensemble" in hn)
chk("istiṯmār : clause faible mémoire du véridique digne de confiance — relevée par autre voie",
    "la faible mémoire de son rapporteur, véridique et digne de confiance (aṣ-ṣadūq al-amīn)" in hn
    and "sa faiblesse disparaît par la venue d’une autre voie, et il devient ḥasan" in hn)
chk("istiṯmār : ʾirsāl levé par autre voie + fušūq pas d’effet de la concordance",
    "si sa faiblesse était par l’émission disjointe (al-ʾirsāl)" in hn
    and "la concordance d’autrui n’y a aucun effet" in hn and "Dieu sait mieux" in hn)
chk("istiṯmār : renvoi at-Taqrīb wa-t-taysīr p.31 imprimée",
    "at-Taqrīb wa-t-taysīr li-maʿrifat sunan al-bašīr an-naḏīr fī uṣūl al-ḥadīṯ" in hn
    and "Yaḥyā b. Šarf an-Nawawī, page 31" in hn)
chk("consigne 1 : importance du motif de la faiblesse + renforcement",
    "l’importance de la connaissance du motif de la faiblesse du ḥadīṯ" in hn
    and "son effet dans son renforcement par rapport à son absence" in hn)
chk("consigne 2 : résumé valeurs morales dans la vie de l’étudiant",
    "les valeurs morales dans la vie de l’étudiant en science" in hn)
chk("iʿdād : leçon 19 le forgé et le délaissé + 2 items",
    "La leçon 19 est" in hn and "le forgé et le délaissé" in hn
    and "(al-mawḍūʿ wa-l-matrūk)" in hn
    and "à deux items" in hn)
chk("iʿdād 1 : feuille concise efforts des savants + négligence parmi les motifs du rejet (image)",
    "les efforts des savants du ḥadīṯ dans la préservation de la Sunna" in hn
    and "la fréquence de la négligence est parmi les motifs du rejet du ḥadīṯ" in hn)
chk("iʿdād 2 : différence entre le forgé et le délaissé",
    "la différence entre le ḥadīṯ forgé (al-mawḍūʿ) et le délaissé (al-matrūk)" in hn)

# ---- hygiène FR
chk("zéro caractère arabe", not re.search(r"[\u0600-\u06FF\u0750-\u077F\u08A0-\u08FF\uFB50-\uFDFF\uFE70-\uFEFF]", h))
chk("zéro apostrophe droite", chr(39) not in h)
chk("guillemets appariés", h.count("«") == h.count("»"))
chk("zéro double espace", "  " not in re.sub(r"&nbsp;|\n", "", h))
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
chk("registre 271 intact (~21 000-26 000 car)",
    21_000 <= len(les["pdf-mut23h2u-271"].get("htmlFr") or "") <= 26_000)
chk("registre 270 intact (20 432 car)", len(les["pdf-mut23h2u-270"].get("htmlFr") or "") == 20432)
chk("registre 273 non touché (htmlFr vide)", (les["pdf-mut23h2u-273"].get("htmlFr") or "") == "")
fr = les["pdf-mut23h2u-272"].get("htmlFr") or ""
if fr:
    chk("registre 272 = htmlFr posé (16 000-24 000 car)", 16_000 <= len(fr) <= 24_000)
    chk("registre 272 == fichier livré", fr.strip() == h.strip())
else:
    chk("registre 272 encore vide (avant hand-set)", True)
chk("titleAr pré-mappé 272", les["pdf-mut23h2u-272"].get("titleAr") == "الدرس 18 : أسباب الطعن في الراوي")
chk("titleFr pré-mappé 272 aligné au h1",
    (les["pdf-mut23h2u-272"].get("titleFr") or "") == "Leçon 18 : Les motifs de discrédit du transmetteur")
chk("titleAr pré-mappé 273 intact (leçon 19, non touchée)",
    les["pdf-mut23h2u-273"].get("titleAr") == "الدرس 19 : الموضوع والمتروك")

print(f"verify-ulumhadith2-pdf272 : {ok} PASS / {fail} ÉCHEC")
raise SystemExit(1 if fail else 0)

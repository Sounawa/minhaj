#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Minhāj — Vérification de la leçon hadith2-pdf-12 (leçon 11, le mérite du dhikr
et du duʿāʾ, p.79-85) : contrôle de contenu, huit numéros du Muwaṭṭaʾ tranchés
par preuve image (562/572/566/567/564/569/576/584 — composites 1 900 px, pages
entières 300 dpi, micro-recadrages 900 et 1 200 dpi ; l'API vision z-ai sous
quota HTTP 429, lectures d'image directes documentées), bornes p.79-85
(bannière « al-dars 11 » en p.79 — correction de la carte R534 qui portait
80-85, convergente avec la déclaration pdf-11), isnāds tranchés (Sumayy mawlā
Abī Bakr + Abū Ṣāliḥ as-Sammān ; Ibn Shihāb + al-Aġarr + Abū Salama — écart
couche al-Aʿrāǧ déclaré ; Rāfiʿa b. Rāfiʿ b. Rāfiʿ tel qu'imprimé à 1 200 dpi,
écart canonique b. Ḥudayj déclaré), quatre āyas rendues du cache (2:152 et
2:186 — décalage R511 vérifié imprimé −1 ; 40:60 et 29:45 — décalage non
applicable), takeover réglementaire du claim périmé 13 h consigné.
Usage: python3 scripts-translate/verify-hadith2-pdf12.py
"""
import re

HTML = "/home/z/my-project/tr-tmp/lesson-hadith2-pdf-12-fr.html"

ok, fail = 0, 0


def chk(label, cond):
    global ok, fail
    if cond:
        ok += 1
    else:
        fail += 1
        print(f"ÉCHEC: {label}")


html = open(HTML, encoding="utf-8").read().replace("\u202f", " ").replace("\u00a0", " ")
flat = re.sub(r"[\s\u202f\u00a0]", "", html)  # copie aplatie : NNBSP de l'auto-fix autour de : 
text = re.sub(r"<[^>]+>", " ", html)

# 0 arabe (ﷺ U+FDFA exempté par convention corpus)
arab = re.findall(r"[\u0600-\u06FF\u0750-\u077F\u08A0-\u08FF\uFB50-\uFDF9\uFDFB-\uFDFF\uFE70-\uFEFF]", text)
arab = [c for c in arab if c != "\ufdfa"]
chk("0 caractère arabe au corps", len(arab) == 0)

# structure générale
chk("h1 leçon 11", "leçon 11" in html and "<h1>" in html)
chk("h1 titre-portail exact", "Le mérite du dhikr et du duʿāʾ — le livre d’al-Ḥadīth" in html)
chk("lesson-meta présent", 'class="lesson-meta"' in html and "Source du cours" in html)
chk("bornes pages 79 à 85 citées (miroir)", "pages 79 à 85" in html)
chk("slot pdf-12 déclaré", "pdf-12" in html)
chk("badge portail Leçon 12 / 31", "Leçon 12 / 31" in text)
chk("hadith-2es déclaré", "hadith-2es" in html)
chk("miroir 208 pages cité", "deux cent huit pages" in html)

# chaîne de production consignée
chk("trace du tick consignée", "1a1a172f41684dc9-cron-agent-loop-202611041619" in html)
chk("claim externe périmé consigné (utc)", "19:21:07Z" in flat)
chk("takeover 08:26:44Z consigné", "08:26:44Z" in flat)
chk("trace externe du claim consignée", "1a1a2d5973bc6765" in html)
chk("règle des cinquante minutes citée", "cinquante minutes" in html)
chk("aucun WIP vérifié", "aucun WIP ne figurant sur disque" in html)

# bornes et corrections
chk("bannière al-dars 11 en p.79 lue", "al-dars 11" in text)
chk("bannière al-dars 12 en p.86 lue", "al-dars 12" in text)
chk("carte R534 citée", "R534" in html)
chk("carte portait 80-85", "80 à 85" in html or "80-85" in html)
chk("convergence déclaration pdf-11 citée", "livraison pdf-11" in html)
chk("couche l11 consignée (15 171 caractères)", "15 171 caractères" in html)
chk("26 bandes consignées", "vingt-six bandes" in html)
chk("7 composites consignés", "sept composites" in html)
chk("4 pages entières consignées", "quatre pages entières 300 dpi" in html)
chk("micro-recadrages 900 dpi consignés", "900 dpi" in html)
chk("micro-crop 1 200 dpi consigné", "1 200 dpi" in html)
chk("quota HTTP 429 consigné", "429" in html)

# références de doctrine
chk("doctrine R511 citée", "R511" in html)
chk("précédent R552 cité", "R552" in html)
chk("précédent R551 cité", "R551" in html)
chk("précédent R558 cité", "R558" in html)
chk("méthode composites R550 citée", "R550" in html)

# numéros du Muwaṭṭaʾ tranchés
chk("renvoi 562 (hadith 1)", "numéro : 562" in text)
chk("renvoi 562 cité deux fois", text.count("562") >= 2)
chk("renvoi 572 (hadith 2)", "numéro : 572" in text)
chk("renvoi 572 trois occurrences", text.count("572") >= 3)
chk("renvoi 566 (Abū ad-Dardāʾ)", "numéro : 566" in text)
chk("renvoi 567 (Rafāʿa)", "numéro : 567" in text)
chk("renvoi 564 (dubur aṣ-ṣalāt)", "numéro : 564" in text)
chk("renvoi 569 ×3 (invocations)", text.count("numéro : 569") >= 3)
chk("renvoi 576 (Ibn ʿAbbās)", "numéro : 576" in text)
chk("renvoi 584 (exploitation)", "numéro : 584" in text)
chk("tranchage chiffre par chiffre 5-6-2", "5 — 6 — 2" in text)
chk("tranchage chiffre par chiffre 5-7-2", "5 — 7 — 2" in text)
chk("tranchage chiffre par chiffre 5-6-6", "5 — 6 — 6" in text)
chk("tranchage chiffre par chiffre 5-6-7", "5 — 6 — 7" in text)
chk("tranchage chiffre par chiffre 5-6-4", "5 — 6 — 4" in text)
chk("tranchage chiffre par chiffre 5-6-9", "5 — 6 — 9" in text)
chk("tranchage chiffre par chiffre 5-7-6", "5 — 7 — 6" in text)
chk("tranchage chiffre par chiffre 5-8-4", "5 — 8 — 4" in text)

# isnāds
chk("isnād 1 : Sumayy mawlā Abī Bakr", "Sumayy, le mawlā d’Abū Bakr" in html)
chk("isnād 1 : Abū Ṣāliḥ as-Sammān", "Abū Ṣāliḥ as-Sammān" in html)
chk("isnād 1 : Abū Hurayra", "Abū Hurayra — que Dieu soit satisfait de lui" in html)
chk("isnād 2 : Ibn Shihāb", "Ibn Shihāb" in html)
chk("isnād 2 : al-Aġarr tel qu'imprimé", "al-Aġarr" in html)
chk("écart couche al-Aʿrāǧ déclaré", "al-Aʿrāǧ" in html)
chk("isnād 2 : double chemin Abū Salama", "d’après Abū Salama" in html)
chk("Rāfiʿa b. Rāfiʿ b. Rāfiʿ tel qu'imprimé", "Rāfiʿa b. Rāfiʿ b. Rāfiʿ" in html)
chk("écart canonique Ḥudayj déclaré", "Ḥudayj" in html)
chk("Rafāʿa : doctrine R558 citée pour le tel qu'imprimé", "conformément à la doctrine R558" in html)

# tarjama Abū Salama
chk("tarjama : 94 de l’hégire", "94 de l’hégire" in html)
chk("tarjama : 92 ans", "92 ans" in html)
chk("tarjama : écart couche 54 déclaré", "couche du miroir porte « 54 »" in html or "porte « 54 »" in html)
chk("tarjama : ʿUthmān", "ʿUthmān" in html)
chk("tarjama : Jābir", "Jābir" in html)
chk("tarjama : Ibn ʿUmar", "Ibn ʿUmar" in html)
chk("tarjama : ʿĀʾiša", "ʿĀʾiša" in html)
chk("tarjama : Umm Salama", "Umm Salama" in html)
chk("tarjama : Ibn Saʿd", "Ibn Saʿd" in html)
chk("tarjama : faqīh et imām", "faqīh et imām" in html)
chk("tarjama : kunya Ismāʿīl déclarée dégradée", "Ismāʿīl" in html)

# āyas et cache
chk("āya tamhīd : cache 2:152", "2:152" in flat)
chk("décalage vérifié 151 = 152 − 1", "151 = cache 152 − 1" in html or "« 151 » pour l’āya « 152 »" in html)
chk("āya tamhīd : cache 40:60", "40:60" in flat)
chk("décalage non applicable 60 = 60", "« 60 » pour l’āya « 60 »" in html)
chk("couche Ġāfir « 06 » tranchée 60", "« 06 »" in html and "« 60 »" in html)
chk("āya ʿAnkabūt 29:45", "29:45" in flat)
chk("renvoi imprimé ʿAnkabūt 45", "al-ʿAnkabūt, āya : 45" in text or "al-ʿAnkabūt, āya : 45" in html)
chk("āya exploitation : cache 2:186", "2:186" in flat)
chk("décalage vérifié 185 = 186 − 1", "185 = cache 186 − 1" in html or "« 185 »" in html)
chk("FR de l’āya 2:152 rendu du cache", "Souvenez-vous de Moi donc" in html)
chk("FR de l’āya 2:186 rendu du cache", "Je suis tout proche" in html)
chk("FR de l’āya 40:60 rendu du cache", "Appelez-Moi, Je vous répondrai" in html)

# matns majeurs
chk("hadith 1 : formule d’unicité + cent fois", "en une journée cent fois" in html)
chk("hadith 1 : dix affranchissements", "dix affranchissements d’esclaves" in html)
chk("hadith 1 : écart مائة→« 2 » déclaré", "« 2 »" in html)
chk("hadith 2 : tiers dernier de la nuit", "tiers dernier de la nuit" in html)
chk("hadith al-Bukhārī : écume de la mer", "l’écume de la mer" in html)
chk("écart zabad/rabad déclaré", "« rabad »" in html)
chk("Abū ad-Dardāʾ : plus pure + Roi", "la plus élevée auprès de votre Roi" in html)
chk("Abū ad-Dardāʾ : anẓāhā consigné", "wa-anẓāhā" in html)
chk("Abū ad-Dardāʾ : malīkum écart déclaré", "« malīkum »" in html)
chk("Abū ad-Dardāʾ : clausule dhikr", "« le dhikr de Dieu le Très-Haut »" in html)
chk("Rafāʿa : Dieu entend qui Le loue", "Dieu entend qui Le loue" in html)
chk("Rafāʿa : trente-sept anges", "trente-sept anges" in html)
chk("Rafāʿa : baḍʿa wa-ṯalāṯīn consigné", "baḍʿa wa-ṯalāṯīn" in html)
chk("Rafāʿa : graphie finale dégradée déclarée", "GRAPHIE FINALE DU SEGMENT DEMEURE DÉGRADÉE" in html)
chk("Rafāʿa : trois lectures divergentes déclarées", "trois lectures d’image divergentes" in html)
chk("point 4 : fragment imprimé déclaré", "cité ici en fragment imprimé" in html)
chk("point 4 : conclusion intégrale", "chasse le démon" in html)
chk("sabbaḥa : dubura consigné", "sabbaḥa dubura kulli ṣalāt" in html)
chk("sabbaḥa : écart ḏikra déclaré", "« ḏikra »" in html)
chk("sabbaḥa : trente-trois", "trente-trois" in html)
chk("sabbaḥa : maġfiratun ḏunūbuhu écart déclaré", "maġfiratun ḏunūbuhu" in html and "Ġufirat ḫaṭāyāhu".lower() in html.lower() or "ġufirat ḫaṭāyāhu" in html)
chk("aṯnāʾ : clôture pendant la prière", "kāna fī aṯnāʾi ṣ-ṣalāt" in html)
chk("duʿāʾ a : Yaḥyā b. Saʿīd", "Yaḥyā b. Saʿīd" in html)
chk("duʿāʾ a : quiétude et décompte", "une quiétude et du jour un décompte" in html)
chk("duʿāʾ a : dette, pauvreté, ouïe, vue, chemin", "règle ma dette" in html and "mon ouïe et de ma vue" in html and "dans Ton chemin" in html)
chk("duʿāʾ a : taʿawwuḏ/taʿāfī écart déclaré", "at-taʿawwuḏ" in html and "at-taʿāfī" in html)
chk("duʿāʾ b : Zayd b. Abī Zayd", "Zayd b. Abī Zayd" in html)
chk("duʿāʾ b : Ṭalḥa b. ʿUbaydallāh b. Karīz", "Ṭalḥa b. ʿUbaydallāh b. Karīz" in html)
chk("duʿāʾ b : jour de ʿArafa", "jour de ʿArafa" in html)
chk("duʿāʾ c : Abū az-Zubayr al-Makkī", "Abū az-Zubayr al-Makkī" in html)
chk("duʿāʾ c : Ṭāwūs al-Yamānī", "Ṭāwūs al-Yamānī" in html)
chk("duʿāʾ c : ʿAbdallāh b. ʿAbbās", "ʿAbdallāh b. ʿAbbās" in html)
chk("duʿāʾ c : comme une sūra du Coran", "comme Il leur enseignait une sūra du Coran" in html)
chk("duʿāʾ c : quatre refuges", "châtiment de la Géhenne" in html and "châtiment de la tombe" in html and "Messie de l’égarement" in html and "vie et de la mort" in html)
chk("ʿĀʾiša : endormie contre le côté", "endormie contre le côté" in html)
chk("ʿĀʾiša : Ton pardon contre Ton courroux", "Ton pardon contre Ton courroux" in html)
chk("ʿĀʾiša : Tu es comme Tu T’es loué", "Tu es comme Tu T’es loué Toi-même" in html)
chk("Ibn ʿAbbās : lumière des cieux", "Tu es la lumière des cieux et de la terre" in html)
chk("Ibn ʿAbbās : Mainteneur", "le Mainteneur des cieux et de la terre" in html)
chk("Ibn ʿAbbās : le Vrai ×4", "Ta parole est vraie" in html and "Ta promesse est vraie" in html and "Ta rencontre est vraie" in html)
chk("Ibn ʿAbbās : Paradis vrai, Feu vrai, Heure vraie", "le Paradis est vrai" in html and "le Feu est vrai" in html and "l’Heure est vraie" in html)
chk("Ibn ʿAbbās : sept engagements", "je me soumets" in html and "en Toi je crois" in html and "sur Toi je compte" in html and "vers Toi je reviens" in html and "avec Toi je plaide" in html and "j’arbitre" in html)
chk("Ibn ʿAbbās : avancé/différé/caché/manifesté", "avancé et différé" in html and "caché et manifesté" in html)
chk("Ibn ʿAbbās : Tu es ma divinité", "Tu es ma divinité, il n’y a de dieu que Toi" in html)
chk("ḥadīth exploitation : renvoi vers guidance", "invoque vers une guidance" in html)
chk("ḥadīth exploitation : fardeaux", "leurs fardeaux" in html)

# sections et structure
chk("9 h2", html.count("<h2>") == 9)
chk("h3 tamhīd", "Le tamhīd" in html)
chk("h3 premier texte", "Le premier texte" in html)
chk("h3 deuxième texte", "Le deuxième texte" in html)
chk("h3 transmetteur", "Abū Salama b. ʿAbd ar-Raḥmān b. ʿAwf az-Zuhrī — que Dieu soit satisfait de lui" in html)
chk("h3 trois parties du corps", html.count("<h3>") >= 6)
chk("h4 : 4 mérites + 2 moments + 2 temps", html.count("<h4>") == 8)
chk("ol objectifs à 3 items", "connaître le mérite du dhikr et sa place" in html and "moments privilégiés du duʿāʾ ;" in html and "valeurs et de moeurs" in html)

# définitions (maḍāmīn)
chk("glose ʿašru riqāb", "ʿašru riqāb" in html or "ʿašri riqāb" in html)
chk("glose tawātī déclarée", "tawātī" in html)
chk("glose ḥirzan/ḥiṣnan", "ḥiṣnan waqīyan min wasāwisi" in html)
chk("glose yubtadirūnahā", "yubtadirūnahā" in html and "li-yuṣaddiqa bihā" in html)
chk("écart li-yuṣʿad déclaré", "« li-yuṣʿad »" in html)
chk("ṣiyāġ/ṣabġ divergence déclarée", "aṣ-ṣiyāġ" in html and "aṣ-ṣabġ" in html)
chk("al-Mawṭiʾ orthographe déclarée", "al-Mawṭiʾ" in html)

# exploitation et préparation
chk("exploitation : qarn ash-shayṭān", "qarn ash-shayṭān" in html)
chk("exploitation : shurūq/ghurūb + fajr/ʿaṣr", "lever et au coucher du soleil" in html and "après le fajr et le ʿaṣr" in html)
chk("préparation : pdf-13 déjà au registre", "DÉJÀ AU REGISTRE, livraison R551, jamais re-produite, GARDE-DOUBLON" in html)
chk("préparation : al-dars 12 et titre", "al-dars 12" in html and "après le fajr et le ʿaṣr" in html)
chk("Ṣaḥīḥ al-Bukhārī cité", "Ṣaḥīḥ al-Bukhārī" in text)

# typographie
chk("0 apostrophe droite", "'" not in html)
chk("guillemets appariés", text.count("«") == text.count("»"))
chk("ﷺ conservé (convention corpus)", "\ufdfa" in html)

print(f"\n{ok} PASS / {fail} FAIL — total {ok + fail}")
raise SystemExit(1 if fail else 0)

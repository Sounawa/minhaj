#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Minhāj — Vérification de la leçon hadith2-pdf-10 (leçon 9, أحكام القبلة وفضل
المسجد النبوي, p.67-72) : contrôle de contenu, numéros du Muwaṭṭaʾ tranchés par
preuve image (125/425/725 en ordre direct — couches «]125/]425/]725» ;
530 contre couche «5:0» et lecture VLM «419» récusée, double lecture 600+900 dpi ;
523/529/532/533 contre couches 325/925/235/335 — inversions totales R535-R544 ;
525 convergent), bornes p.67-72 à triple convergence (objectifs p.67, إعداد p.72
→ مس المصحف, STARTS l9=67/l10=73 carte publiée commit 128dfad), RENDU CORANIQUE
du cache ḥafṣ 2:144 pour l'āya imprimée warš 143 (doctrine R511, renvoi rouge
tranché par triple lecture d'image contre la lecture VLM «an-Nūr 36» récusée),
isnāds tranchés par image (Isḥāq b. ʿAbdallāh b. Abī Ṭalḥa ← Rāfiʿ b. Isḥāq ←
Abū Ayyūb ; ʿAbdallāh b. Dīnār ; Yaḥyā b. Saʿīd ← Saʿīd b. al-Musayyab ;
Khayyib b. ʿAbd ar-Raḥmān ← Ḥafṣ b. ʿĀṣim ← Abū Hurayra ou Abū Saʿīd al-Khudrī ;
Busr b. Saʿīd par image 900 dpi), lexies tranchées (hāḏihi l-karāyīs ;
ʿalā labnatayn mustaqbil bayta l-maqdis li-ḥāǧatihi ; al-ǧamʿ lahu bayna
l-qiblatayn ; bi-miʾa ṣalāt), sept récusations VLM déclarées + une divergente
+ une lecture maison au cadrage décalé récusée, takeover réglementaire du claim
R545-takeover périmé de 18 minutes consigné.
Usage: python3 scripts-translate/verify-hadith2-pdf10.py
"""
import re

HTML = "/home/z/my-project/tr-tmp/lesson-hadith2-pdf-10-fr.html"

ok, fail = 0, 0
def chk(label, cond):
    global ok, fail
    if cond: ok += 1
    else:
        fail += 1
        print(f"ÉCHEC: {label}")

html = open(HTML, encoding="utf-8").read()
text = re.sub(r"<[^>]+>", " ", html).replace("\u202f", " ").replace("\u00a0", " ")
# copie normalisée sans espaces fines (contrôles insensibles aux NNBSP de l'auto-fix)
nhtml = html.replace("\u202f", "").replace("\u00a0", "")

# 0 arabe (ﷺ U+FDFA exempté par convention corpus)
arab = re.findall(r"[\u0600-\u06FF\u0750-\u077F\u08A0-\u08FF\uFB50-\uFDF9\uFDFB-\uFDFF\uFE70-\uFEFF]", text)
arab = [c for c in arab if c != "\ufdfa"]
chk("0 caractère arabe au corps", len(arab) == 0)

# structure générale
chk("h1 leçon 9", "leçon 9" in html and "<h1>" in html)
chk("lesson-meta présent", 'class="lesson-meta"' in html and "Source du cours" in html)
chk("bornes pages 67 à 72", "pages 67 à 72" in html)
chk("slot pdf-10 déclaré", "pdf-10" in html)
chk("badge portail Leçon 10 / 31", "Leçon 10 / 31" in text)
chk("hadith-2es déclaré", "hadith-2es" in html)
chk("miroir 208 pages cité", "deux cent huit pages" in html)
chk("titre de la leçon (règles de la qibla)", "Les règles de la qibla et le mérite de la mosquée du Prophète" in html)

# takeover réglementaire consigné
chk("takeover réglementaire documenté", "TAKEOVER RÉGLEMENTAIRE" in html)
chk("claim R545-takeover périmé consigné", "PÉRIMÉ" in html and "R545" in html)
chk("étiquettes de claims non livrés (R542/R543/R545)", "étiquettes de claims" in html)
chk("GARDE-DOUBLON registre 1112 → 1113", "registre 1112 → 1113" in html)
chk("hadith-2es 9/30", "hadith-2es 9/30" in html)
chk("claim rafraîchi avant rédaction consigné", "rafraîchi à 10" in html)

# bornes triple convergence
chk("objectifs p.67", "page 67" in html)
chk("préparation p.72 déclarant la leçon suivante", "page 72" in html and "muṣḥaf" in html)
chk("carte l9=67", "l9 = 67" in html)
chk("carte l10=73 publiée (128dfad)", "l10 = 73" in html and "128dfad" in html)
chk("page 73 ouvre la leçon suivante", "page 73 ouvre la leçon suivante" in html)
chk("jamais devinée (borne)", html.count("jamais devinée") >= 2)

# numéros Muwaṭṭaʾ tranchés + couches déclarées
for num in ["125", "425", "725", "530", "523", "525", "529", "532", "533"]:
    chk(f"numéro {num} présent", f"n° {num}" in html)
chk("couche 5:0 déclarée (rawḍa)", "5:0" in nhtml)
chk("lecture VLM 419 récusée", "419" in html and "RÉFUTÉE" in html)
chk("couche 325 déclarée (Ibn ʿUmar)", "325" in html)
chk("couche 925 déclarée (mérite)", "925" in html)
chk("couche 235 déclarée (servantes)", "235" in html)
chk("couche 335 déclarée (parfum)", "335" in html)
chk("inversion totale citée", "inversion totale" in html)
chk("série 50X-53X déclarée", "50X-53X" in html)
chk("numéro 530 tranché par double lecture 600+900", "600 et 900 dpi" in html or "600 et 900" in html)

# rendu coranique du cache ḥafṣ (āya warš 143 = ḥafṣ 144, doctrine R511)
chk("āya rendue du cache ḥafṣ 2:144", "2:144" in nhtml)
chk("imprimé warš 143 déclaré", "warš" in html and "143" in html)
chk("doctrine R511 citée", "R511" in html)
chk("renvoi rouge tranché par triple lecture", "triple lecture" in html)
chk("lecture VLM an-Nūr 36 récusée", "an-Nūr" in html)
chk("rendu français du verset présent (tamhīd)", "Certes nous te voyons tourner le visage en tous sens dans le ciel" in html)
chk("rendu du verset répété au corps", html.count("Certes nous te voyons tourner le visage") >= 2)
chk("reprise coranique intégrale translittérée déclarée", "qad narā taqalluba waǧhika fī s-samāʾ" in html)

# isnāds tranchés par image
chk("Isḥāq b. ʿAbdallāh b. Abī Ṭalḥa (texte 1)", "Isḥāq b. ʿAbdallāh b. Abī Ṭalḥa" in html)
chk("Rāfiʿ b. Isḥāq (texte 1)", "Rāfiʿ b. Isḥāq" in html)
chk("mawlā des gens d'ash-Shifāʾ", "ash-Shifāʾ" in html)
chk("affranchi d'Abū Ṭalḥa", "affranchi d’Abū Ṭalḥa" in html)
chk("Abū Ayyūb al-Anṣārī entendu (texte 1)", "Abū Ayyūb al-Anṣārī" in html)
chk("en Égypte (matn hadith 1)", "en Égypte" in html)
chk("VLM Anas/duʿāʾ récusée (1re récusation)", "Anas b. Mālik" in html and "première récusation" in html)
chk("ʿAbdallāh b. Dīnār (texte 2)", "ʿAbdallāh b. Dīnār" in html)
chk("Yaḥyā b. Saʿīd (texte 3)", "Yaḥyā b. Saʿīd" in html)
chk("Saʿīd b. al-Musayyab (texte 3)", "Saʿīd b. al-Musayyab" in html)
chk("lectures p70 Saʿd b. Abī Waqqāṣ/Nāfiʿ récusées-divergentes", "Saʿd b. Abī Waqqāṣ" in html and "Nāfiʿ" in html)
chk("isnād de re-citation non re-nommé déclaré", "n’est pas re-nommé" in html)
chk("Khayyib b. ʿAbd ar-Raḥmān (texte 4)", "Khayyib b. ʿAbd ar-Raḥmān" in html)
chk("Ḥafṣ b. ʿĀṣim (texte 4)", "Ḥafṣ b. ʿĀṣim" in html)
chk("Abū Saʿīd al-Khudrī (texte 4, chaîne alternative)", "Abū Saʿīd al-Khudrī" in html)
chk("VLM ʿAbdallāh b. Abī Bakr récusée (2e récusation)", "ʿAbdallāh b. Abī Bakr" in html and "deuxième récusation" in html)
chk("Busr b. Saʿīd (exploration, image 900 dpi)", "Busr b. Saʿīd" in html and "900 dpi" in html)
chk("graphie Busr sans point de šīn déclarée", "aucun point de šīn" in html)
chk("VLM Bishr récusée (3e récusation)", "Bishr" in html and "troisième récusation" in html)
chk("buligha (il fut transmis/rapporté)", "buligha" in html)
chk("couches 7/8/9 non résolues déclarées (dates Hurayra)", "non résolus" in html)

# matns et lexies tranchées
chk("latrines d'Égypte (matn hadith 1)", "je ne sais que faire de ces latrines" in html)
chk("hāḏihi l-karāyīs translittéré", "hāḏihi l-karāyīs" in html)
chk("ne fasse pas face à la qibla (règle)", "ne fasse pas face à la qibla" in html)
chk("en découvrant sa nudité (bi-farǧihi)", "bi-farǧihi" in html and "en découvrant sa nudité" in html)
chk("crachat sur le mur de la qibla gratté (texte 2)", "vit un crachat" in html and "le gratta" in html)
chk("confère avec son Seigneur", "confère avec son Seigneur" in html)
chk("son Seigneur est entre lui et la qibla", "son Seigneur est entre lui et la qibla" in html)
chk("pan de son manteau (ou qu'il fasse ainsi)", "Ou qu’il fasse ainsi" in html)
chk("seize mois vers Jérusalem", "seize mois" in html)
chk("deux mois avant Badr", "deux mois avant Badr" in html)
chk("dit-on dix-sept (variante)", "dit-on dix-sept" in html)
chk("jardin des jardins du Paradis (rawḍa)", "jardin des jardins du Paradis" in html)
chk("mon minbar au-dessus de mon bassin", "mon bassin" in html and "ḥawḍ" in html)
chk("sur deux briques (rapport Ibn ʿUmar)", "deux briques" in html and "labnatayn" in html)
chk("mustaqbil bayta l-maqdis li-ḥāǧatihi", "mustaqbil bayta l-maqdis li-ḥāǧatihi" in html)
chk("lecture omoplates récusée (6e récusation)", "omoplates" in html and "sixième récusation" in html)
chk("abandon préférable (tark al-ūlā)", "tark al-ūlā" in html)
chk("siège des lieux d'aisance pas vers la qibla", "ne pas disposer le siège" in html)
chk("ʿĀʾisha : crachat/saleté/mucus gratté", "ʿĀʾisha" in html and "mucus" in html)
chk("le dessein : réunion des deux qiblas", "la réunion, pour lui ﷺ, des deux qiblas" in html)
chk("al-ǧamʿ lahu bayna l-qiblatayn translittéré", "al-ǧamʿ lahu bayna l-qiblatayn" in html)
chk("privilèges (ḫawāṣiṣ)", "ḫawāṣiṣ" in html)
chk("lecture épreuve récusée (5e récusation)", "cinquième récusation" in html and "l’épreuve" in html)
chk("mille prières hormis la Mosquée sacrée", "mille prières" in html)
chk("cent prières (Musnad Aḥmad)", "cent prières" in html)
chk("bi-miʾa ṣalāt translittéré", "bi-miʾa ṣalāt" in html)
chk("Musnad Aḥmad musnad des Médinois", "Musnad Aḥmad" in html and "musnad des Médinois" in html)
chk("ʿAbdallāh b. az-Zubayr b. al-ʿAwwām", "az-Zubayr b. al-ʿAwwām" in html)
chk("N'empêchez pas les servantes de Dieu", "N’empêchez pas les servantes de Dieu" in html)
chk("ne te pare pas du parfum (al-ʿishāʾ)", "ne te pare pas du parfum" in html and "al-ʿishāʾ" in html)

# transmetteurs
chk("Khālid b. Zayd b. Kulayb b. Thaʿlaba", "Khālid b. Zayd b. Kulayb b. Thaʿlaba" in html)
chk("al-Khazraǧī an-Naǧǧārī al-Badrī", "al-Khazraǧī an-Naǧǧārī al-Badrī" in html)
chk("descente chez les Banū an-Naǧǧār", "Banū an-Naǧǧār" in html)
chk("chambre de Sawda", "Sawda" in html)
chk("cent cinquante hadiths", "cent cinquante hadiths" in html)
chk("mort l'an cinquante-deux (al-Wāqidī)", "cinquante-deux" in html and "Wāqidī" in nhtml)
chk("enterré au pied du rempart de Constantinople", "Constantinople" in html)
chk("ʿAbd ar-Raḥmān b. Ṣakhr", "ʿAbd ar-Raḥmān b. Ṣakhr" in html)
chk("chat dans la manche (Ibn ʿAbd al-Barr)", "Ibn ʿAbd al-Barr" in html and "hirra" in html)
chk("islam l'an de Khaybar", "Khaybar" in html)
chk("mort 57/58, enterré au Baqīʿ", "cinquante-sept" in html and "cinquante-huit" in html and "Baqīʿ" in html)

# définitions du cours
chk("al-karāyīs défini", "al-karāyīs — les latrines" in html)
chk("pluriel de krayās", "krayās" in html)
chk("chambres hautes (marāḥīḍ al-ġuraf)", "marāḥīḍ al-ġuraf" in html)
chk("al-kathf (latrines des maisons)", "al-kathf" in html)
chk("al-ġāʾiṭ défini", "al-ġāʾiṭ — le besoin naturel" in html)
chk("lieu bas de la terre (al-makān al-munḫaḍḍ)", "al-makān al-munḫaḍḍ" in html)
chk("métonymie al-ʿadhra", "al-ʿadhra" in html)

# structure des sections
for section in ["Les objectifs de la leçon", "Le tamhīd", "Les textes du cours",
                "Les traductions des transmetteurs", "Les définitions du cours",
                "L’extraction des contenus", "Le corps du cours", "L’évaluation",
                "L’exploration", "La préparation préalable"]:
    chk(f"section « {section} »", section in html)
chk("quatre textes du cours", "Le quatrième texte" in html)
chk("deux points du corps (Premièrement/Deuxièmement)", "Premièrement" in html and "Deuxièmement" in html)
chk("trois objectifs", "Que je connaisse les bienséances de la qibla" in html and "lieux saints" in html)
chk("évaluation q1 sagesse de l'interdiction", "Quelle est la sagesse de l’interdiction" in html)
chk("préparation : trois items", "sa part de la nuit" in html and "sans ablutions" in html and "prosternations de récitation" in html)
chk("lexie finale non élucidée déclarée", "non élucidée" in html and "ʿazāʾim tuǧādil" in html)
chk("extraction : dessein du parfum", "l’interdiction du parfum à la femme" in html)

# mécanique déclarée
chk("neuf lectures d'image directes déclarées", "neuf lectures d’image directes" in html)
chk("sept récusations VLM 1531 déclarées", "sept récusées par l’image" in html)
chk("lecture maison décalée récusée (Abū az-Zubayr)", "Abū az-Zubayr al-Makkī" in html)
chk("acquis du miroir/claims consignés", "1531" in html and "1701" in html)

# typographie redondante (double contrôle indépendant de qa-lesson)
chk("0 apostrophe droite", "'" not in html)
chk("guillemets appariés", html.count("«") == html.count("»"))
chk("0 marqueur TODO/XXX/【", "TODO" not in html and "XXX" not in html and "【" not in html)
chk("ﷺ symbole corpus présent", "ﷺ" in html)

print(f"verify-hadith2-pdf10 : {ok} contrôles OK, {fail} échec(s)")
raise SystemExit(1 if fail else 0)

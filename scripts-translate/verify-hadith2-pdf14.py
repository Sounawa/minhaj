#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Minhāj — Vérification de la leçon hadith2-pdf-14 (leçon 13, rites funéraires I :
lavage du défunt, linceul et prière, p.91-97) : contrôle de contenu, numéros du
Muwaṭṭaʾ tranchés par preuve image (595/599/614/620/596/597/602/60/612/616/618,
vingt-cinq lectures VLM en cinq passes 300-1 800 dpi), bornes p.91-97 à
convergence carte R534 + couche + borne l14 p.98, isnāds tranchés (Ayyūb b.
Abī Tamīma as-Sakhtiyānī lettre par lettre à 1 600 dpi ; Hišām b. ʿUrwa ;
Ḥumayd b. ʿAbd ar-Raḥmān b. ʿAwf ← ʿAbdallāh b. ʿAmr b. al-ʿĀṣ ; Saʿīd b.
Abī Saʿīd al-Maqburī), āya rendue du cache 17:70 (imprimé 70 = cache 70 —
décalage R511 non applicable ici, écart doctrine déclaré), lexies déclarées,
fragments non élucidés déclarés (renvoi « 60 », walā, Umm Šarāḥīl, ʿUqda,
li-waqtihimā, Yémen/Médine).
Usage: python3 scripts-translate/verify-hadith2-pdf14.py
"""
import re

HTML = "/home/z/my-project/tr-tmp/lesson-hadith2-pdf-14-fr.html"

ok, fail = 0, 0
def chk(label, cond):
    global ok, fail
    if cond: ok += 1
    else:
        fail += 1
        print(f"ÉCHEC: {label}")

html = open(HTML, encoding="utf-8").read().replace("\u202f", " ").replace("\u00a0", " ")
text = re.sub(r"<[^>]+>", " ", html)

# 0 arabe (ﷺ U+FDFA exempté par convention corpus)
arab = re.findall(r"[\u0600-\u06FF\u0750-\u077F\u08A0-\u08FF\uFB50-\uFDF9\uFDFB-\uFDFF\uFE70-\uFEFF]", text)
arab = [c for c in arab if c != "\ufdfa"]
chk("0 caractère arabe au corps", len(arab) == 0)

# structure générale
chk("h1 leçon 13", "leçon 13" in html and "<h1>" in html)
chk("h1 titre-portail exact", "Les rites funéraires (ǧanāʾiz) : lavage du défunt, linceul et prière — le livre d’al-Ḥadīth" in html)
chk("lesson-meta présent", 'class="lesson-meta"' in html and "Source du cours" in html)
chk("bornes pages 91 à 97 citées (miroir)", "pages 91 à 97" in html)
chk("slot pdf-14 déclaré", "pdf-14" in html)
chk("badge portail Leçon 14 / 31", "Leçon 14 / 31" in text)
chk("hadith-2es déclaré", "hadith-2es" in html)
chk("miroir 208 pages cité", "deux cent huit pages" in html)

# chaîne de production consignée
chk("passe R558 (Task ID) référencée indirectement via trace", "1a19c7c0ffb4f845-cron-agent-loop-202611040407" in html)
chk("claim 20:09:18Z consigné", "20:09:18Z" in html or "20 :09 :18Z" in html)
chk("trois rafraîchissements consignés", ("20:09:37Z" in html or "20 :09 :37Z" in html)
    and ("20:27:13Z" in html or "20 :27 :13Z" in html)
    and ("20:44:26Z" in html or "20 :44 :26Z" in html))
chk("takeover réglementaire 16:59:45Z consigné", ("16:59:45Z" in html or "16 :59 :45Z" in html) and "takeover réglementaire" in html)
chk("25 lectures VLM consignées", "vingt-cinq lectures VLM" in html)
chk("cinq passes consignées", "cinq passes" in html)
chk("extraction 15 734 caractères consignée", "15 734 caractères" in html)
chk("GARDE-DOUBLON pdf-12 intouché", "pdf-12" in html and "n’a pas été touché" in html)
chk("GARDE-DOUBLON pdf-15 au registre", "pdf-15" in html and "jamais re-produite" in html)
chk("registre 12/30 + 1116 savants", "12/30" in html and "1116 savants" in html)
chk("étape 0 : distant 08fb7b91", "08fb7b91" in html)
chk("étape 2 : dev:3000 33 ms (R557 confirmé)", "33 ms" in html)

# bornes + carte
chk("carte R534 l13 = 91", "R534" in html and "l13 = 91" in html)
chk("borne l14 = 98 (ouverture slot pdf-15)", "page 98 ouvre la leçon suivante" in html)
chk("en-tête du cours treizième déclaré (triple convergence)", "l’unité est la treizième par triple convergence" in html)
chk("préparation préalable de pdf-13 échoée (R551)", "livraison R551, slot pdf-13" in html and "ašʿarnahā iyyāhū" in html)

# numéros du Muwaṭṭaʾ tranchés — présence des onze renvois
for n in ("595", "599", "614", "620", "596", "597", "602", "612", "616", "618"):
    chk(f"renvoi al-Muwaṭṭaʾ n° {n}", f"al-Muwaṭṭaʾ n° {n}" in html)
chk("renvoi imprimé « 60 » porté tel quel", "al-Muwaṭṭaʾ n° 60" in html)
chk("écart de séquence 606 déclaré sans reconstitution", "606" in html and "jamais reconstitué" in html)
chk("renvoi 597 tranché 5-9-7 à 1600 dpi", "5-9-7" in html)
chk("renvoi 596 tranché 5-9-6", "5-9-6" in html)
chk("renvoi 612 chiffre par chiffre 6-1-2", "6-1-2" in html)

# āya — rendu du cache + doctrine
chk("āya 17:70 du cache citée", "Certes, Nous avons honoré les fils d’Adam" in html)
chk("renvoi imprimé Isrāʾ 70 porté", "sūrat al-Isrāʾ, āya : 70" in html)
chk("décalage R511 non applicable déclaré", "NE SE VÉRIFIE PAS" in html)
chk("convergences R551/R552 citées", "R551" in html and "R552" in html)
chk("couche texte (cache) nommée", "quran-cache.json" in html)

# isnāds tranchés
chk("isnād 1 : Ayyūb b. Abī Tamīma as-Sakhtiyānī", "Ayyūb b. Abī Tamīma as-Sakhtiyānī" in html)
chk("isnād 1 : lettre par lettre 1600 dpi", "lettre par lettre à 1 600 dpi" in html)
chk("isnād 1 : récusation Abū Bakr b. Abī Taḥma déclarée", "Abū Bakr b. Abī Taḥma" in html and "récusées" in html)
chk("isnād 1 : récusation Abī Šayba déclarée", "Abī Šayba" in html)
chk("isnād 1 : Muḥammad b. Sīrīn", "Muḥammad b. Sīrīn" in html)
chk("isnād 2 : Hišām b. ʿUrwa ← son père ← ʿĀʾiša", "Hišām b. ʿUrwa, d’après son père, d’après ʿĀʾiša" in html)
chk("isnād 2 : couche Fāṭima bint al-Munḏir récusée", "Fāṭima bint al-Munḏir" in html)
chk("isnāds 3-4 : Nāfiʿ ← ʿAbdallāh b. ʿUmar", html.count("d’après Nāfiʿ") >= 2 and "ʿAbdallāh b. ʿUmar" in html)
chk("isnād [602] : Ḥumayd b. ʿAbd ar-Raḥmān b. ʿAwf", "Ḥumayd b. ʿAbd ar-Raḥmān b. ʿAwf" in html)
chk("isnād [602] : ʿAbdallāh b. ʿAmr b. al-ʿĀṣ (récusation Khaṭṭāb)", "ʿAbdallāh b. ʿAmr b. al-ʿĀṣ" in html and "b. al-Khaṭṭāb » est récusée" in text or "est récusée" in html)
chk("isnād [612] : Saʿīd b. Abī Saʿīd al-Maqburī ← son père", "Saʿīd b. Abī Saʿīd al-Maqburī, d’après son père" in html)
chk("isnād Najāšī : Ibn Šihāb ← Saʿīd b. al-Musayyib ← Abū Hurayra", "Ibn Šihāb, d’après Saʿīd b. al-Musayyib, d’après Abū Hurayra" in html)

# transmetteurs
chk("Umm ʿAṭiyya : Nusayba bint al-Ḥārit / Kaʿb", "Nusayba bint al-Ḥārit" in html and "Nusayba bint Kaʿb" in html)
chk("fuqahāʾ aṣ-ṣaḥāba + Zaynab", "jurisconsultes de la première génération" in html and "Zaynab, la fille du Prophète ﷺ" in html)
chk("transmetteurs : Ḥafṣa/Šarāḥīl/Aqmar/ʿUmayr/Ismāʿīl/ʿUqda", all(x in html for x in ("Ḥafṣa bint Sīrīn", "Umm Šarāḥīl", "ʿAlī b. al-Aqmar", "ʿAbd al-Malik b. ʿUmayr", "Ismāʿīl b. ʿAbd ar-Raḥmān", "ʿUqda")))
chk("عاشت حدود سبعين", "l’an soixante-dix" in html)

# matns & contenus clés
chk("matn 595 : trois/cinq fois + sidr + camphre", "Lavez-la trois fois" in html and "sidr" in html and "camphre" in html)
chk("glose ḥuqq = izār", "son izār (pagne)" in html)
chk("focdade Šarḥ : šiʿār + tabarruk", "šiʿār" in html and "tabarruk" in html)
chk("matn 599 : trois vêtements blancs suḥūliyya, sans qamīṣ ni ʿimāma", "trois vêtements blancs suḥūliyya" in html and "qamīṣ" in html and "ʿimāma" in html)
chk("matn 614 : pas de récitation", "ne récitait pas dans la prière sur la djanāza" in html)
chk("matn 620 : salām prolongé", "prolongeait le salām" in html)
chk("farḍ kifāya", "obligation de suffisance (farḍ kifāya)" in html)
chk("trois lavages : eau pure / savon-sidr / parfum", "première aspersion, qui est faite à l’eau pure" in html and "du savon ou du sidr" in html and "parfum, comme le zahr, le camphre ou la rose" in html)
chk("côté droit + [Ṣaḥīḥ al-Buḫārī]", "Commencez par son côté droit" in html and "Ṣaḥīḥ al-Buḫārī" in html)
chk("[596] Asmāʾ bint ʿUmayss lave Abū Bakr", "Asmāʾ bint ʿUmayss, épouse d’Abū Bakr aṣ-Ṣiddīq" in html)
chk("Fāṭima lavée par ʿAlī [Bayhaqī]", "lava Fāṭima en présence des Compagnons" in html and "Maʿrifat as-sunna wa-l-āṯār d’al-Bayhaqī" in html)
chk("tayammum : visage + mains jusqu’aux coudes", "jusqu’aux coudes" in html)
chk("[597] visage et paumes du ṣaʿīd", "son visage et ses paumes avec du ṣaʿīd" in html)
chk("kafan : homme 3 ou 5, femme 5 ou 7, ziyāda fī as-sitr", "trois vêtements ou de cinq" in html and "cinq ou de sept" in html and "ziyāda fī as-sitr" in html)
chk("[602] tondu, couvert, troisième étoffe", "est tondu, couvert, et enveloppé dans la troisième étoffe" in html and "une seule étoffe, enveloppez-le dedans" in html)
chk("Najāšī : quatre takbīr + muṣallā", "quatre takbīr" in html and "lieu de prière (muṣallā)" in html)
chk("exception Najāšī (musulman chez des chrétiens)", "pays dont les gens sont chrétiens" in html)
chk("position imām : milieu du corps / face aux épaules", "aligné sur le milieu du corps" in html and "face à ses épaules" in html)
chk("tête du mort à droite de l’imām", "du côté de la droite de l’imām" in html)
chk("[Sunan Abī Dāwūd] sans numéro porté tel quel", "Sunan Abī Dāwūd" in html and "sans numéro" in html)
chk("duʿāʾ 612 complet", "le fils de Ta servante" in html and "ne nous prive pas de sa récompense et ne nous éprouve pas après lui" in html)

# lexies + fragments déclarés
chk("définition suḥūliyya (Yémen/Médine déclarés)", "au Yémen" in html and "à Médine » : fragment dégradé" in html)
chk("définition aṣ-ṣaʿīd", "aṣ-ṣaʿīd — la terre pure" in html)
chk("définition an-nawb (sens contextuel déclaré)", "an-nawb — l’étoffe" in html and "sans glose du Šarḥ lisible" in html)
chk("fragment walā déclaré", "se détourne (walā)" in html)
chk("fragments Umm Šarāḥīl/ʿUqda déclarés", "sous réserve déclarée" in html)
chk("fragment li-waqtihimā déclaré", "li-waqtihimā" in html)
chk("récusation « ʿUmar pria » déclarée", "ʿUmar pria dans la mosquée » est déclarée et récusée au sens" in text)
chk("récusation al-qawābil déclarée", "al-qawābil" in html)
chk("récusation al-qīʿān déclarée (préparation)", "al-qīʿān" in html)
chk("« jamais reconstitués » présent", "jamais reconstitué" in html)

# sections du gabarit
for s in ("Les objectifs de la leçon", "Le tamhīd", "Les textes du cours", "Le premier texte",
          "Le deuxième texte", "Le troisième texte", "Le quatrième texte",
          "Les traductions des transmetteurs", "Umm ʿAṭiyya al-Anṣāriyya",
          "Les définitions du cours", "L’extraction des contenus", "Le corps du cours",
          "Premièrement : les règles du lavage du défunt", "Deuxièmement : le linceul du mort et la prière sur lui",
          "L’évaluation", "L’exploitation", "La préparation préalable"):
    chk(f"section « {s} »", s in html)

# évaluation + exploitation + préparation
chk("évaluation : 3 questions", "J’expose la manière de laver le mort et de l’envelopper de son linceul" in html and "Quel est le statut de la prière sur la djanāza" in html)
chk("exploitation : [616] après ʿaṣr et ṣubḥ", "après l’après-midi et après l’aube" in html)
chk("exploitation : [618] mosquée", "On pria sur ʿUmar b. al-Khaṭṭāb dans la mosquée" in html)
chk("préparation : lexies ʿAqīq/yaḥtasib/jardin du Feu/uʾǧarnī", all(x in html for x in ("al-ʿAqīq", "yaḥtasib", "un jardin du Feu", "uʾǧarnī fī muṣībatī")))
chk("préparation : borne l14 + Muṣannaf + qīrāṭ", "Muṣannaf Ibn Abī Šayba" in html and "qīrāṭ" in html)

# typographie
chk("0 apostrophe droite", "'" not in html)
chk("0 backtick", "`" not in html)
chk("0 marqueur Markdown", "**" not in html and "|---|" not in html)

print(f"\n{ok} PASS / {fail} ÉCHEC")
exit(1 if fail else 0)

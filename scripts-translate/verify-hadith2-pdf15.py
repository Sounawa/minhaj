#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Minhāj — Vérification de la leçon hadith2-pdf-15 (leçon 14, أحكام الجنائز :
القبر والدفن وآداب الجنازة, p.98-104) : contrôle de contenu, numéros du
Muwaṭṭaʾ tranchés par preuve image (627/635/640/632/638/654/641/651 contre
couche « 27 »/« 658 » — mécanique R535-R550, 58 lectures VLM en 5 passes),
bornes p.98-104 à convergence image+couche (objectifs p.98 « leçon 14 »,
évaluation+exploitation p.103, إعداد p.104, ouverture p.105 — carte l14=98,
l15=105 en conformité parfaite), isnāds tranchés (mimmay yaṯaq bihi ;
Muḥammad b. Abī Bakr b. Ḥazm ← son père ← Abū an-Naḍr as-Salmānī ;
Abū ar-Rijāl ← ʿAmra ; ʿĀmir b. Saʿd ← Saʿd ; ʿUṯmān ; ʿAlī chain complète ;
Ǧābir b. ʿAtīk), āya rendue du cache (Baqara : imprimé 155 = cache 156 − 1,
doctrine R511), lexies tranchées 800-1200 dpi (fa-yaḥtasibuhum, ḫafīfan,
taqrīb, bi-ṯawb, ḫams ḏawd/awlāq/awsāq), fragments non élucidés déclarés
(al-muḫtafī/al-muḫtaniqa ; tubakkina bākiyatan ; verbe de Ǧābir ; cent six).
Usage: python3 scripts-translate/verify-hadith2-pdf15.py
"""
import re

HTML = "/home/z/my-project/tr-tmp/lesson-hadith2-pdf-15-fr.html"

ok, fail = 0, 0
def chk(label, cond):
    global ok, fail
    if cond: ok += 1
    else:
        fail += 1
        print(f"ÉCHEC: {label}")

html = open(HTML, encoding="utf-8").read()
text = re.sub(r"<[^>]+>", " ", html).replace("\u202f", " ").replace("\u00a0", " ")

# 0 arabe (ﷺ U+FDFA exempté par convention corpus)
arab = re.findall(r"[\u0600-\u06FF\u0750-\u077F\u08A0-\u08FF\uFB50-\uFDF9\uFDFB-\uFDFF\uFE70-\uFEFF]", text)
arab = [c for c in arab if c != "\ufdfa"]
chk("0 caractère arabe au corps", len(arab) == 0)

# structure générale
chk("h1 leçon 14", "leçon 14" in html and "<h1>" in html)
chk("lesson-meta présent", 'class="lesson-meta"' in html and "Source du cours" in html)
chk("bornes pages 98 à 104 citées (miroir)", "pages 98 à 104" in html)
chk("slot pdf-15 déclaré", "pdf-15" in html)
chk("badge portail Leçon 15 / 31", "Leçon 15 / 31" in text)
chk("hadith-2es déclaré", "hadith-2es" in html)
chk("miroir 208 pages cité", "deux cent huit pages" in html)

# chaîne de production consignée
chk("passe R552 consignée", "R552" in html)
chk("claim 14:11:42Z consigné", "14 :11 :42Z" in text or "14:11:42Z" in text)
chk("rafraîchissements consignés", ("15 :36 :51Z" in text or "15:36:51Z" in text)
    and ("17 :08 :06Z" in text or "17:08:06Z" in text))
chk("58 lectures VLM consignées", "cinquante-huit lectures VLM" in html)
chk("cinq passes consignées", "cinq passes" in html)
chk("GARDE-DOUBLON R551 respecté", "R551" in html and "ouvrier parallèle" in html)
chk("slots R548/R549 déclarés intouchés", "R548" in html and "R549" in html)
chk("registre hadith-2es 10/30", "hadith-2es 10/30" in html)
chk("extraction 7 386 caractères consignée", "7 386 caractères" in html)

# bornes + carte
chk("objectifs p.98", "page 98" in html)
chk("évaluation/exploitation p.103", "page 103" in html)
chk("préparation p.104", "page 104" in html)
chk("page 105 ouvre la leçon suivante", "page 105 ouvre la leçon suivante" in html)
chk("carte l14 = 98", "l14 = 98" in html)
chk("carte l15 = 105", "l15 = 105" in html)
chk("conformité parfaite déclarée", "conformité parfaite" in html)
chk("jamais devinée (borne)", "jamais devinée" in html)

# numéros Muwaṭṭaʾ tranchés + couches déclarées
for num in ["627", "635", "640", "632", "638", "654", "641", "651"]:
    chk(f"numéro {num} présent", f"n° {num}" in html)
chk("couche « 658 » déclarée refusée", "658" in html)
chk("638 tranché chiffre par chiffre", "6-3-8" in text)
chk("ordre ascendant des numéros cité", "627, 632, 635, 638, 640, 641, 651, 654" in html)
chk("renvoi Ibn Abī Šayba (tamhīd)", "Ibn Abī Šayba" in html)
chk("renvoi Ṣaḥīḥ de Muslim (laḥd)", "Ṣaḥīḥ de Muslim" in html)
chk("renvoi Sunan d'Abū Dāwūd", "Abū Dāwūd" in html)

# isnāds tranchés
chk("isnād T1 : mimmay yaṯaq bihi", "mimmay yaṯaq bihi" in html)
chk("isnād T2 : Muḥammad b. Abī Bakr b. Ḥazm + Abū an-Naḍr as-Salmānī",
    "Muḥammad b. Abī Bakr b. Ḥazm" in html and "Abū an-Naḍr as-Salmānī" in html)
chk("isnād T3 : Abū ar-Rijāl + ʿAmra", "Abū ar-Rijāl" in html and "ʿAmra bint ʿAbd ar-Raḥmān" in html)
chk("isnād laḥd : ʿĀmir b. Saʿd b. Abī Waqqāṣ", "ʿĀmir b. Saʿd b. Abī Waqqāṣ" in html)
chk("isnād affermissement : ʿUṯmān b. ʿAffān", "ʿUṯmān b. ʿAffān" in html)
chk("isnād exploitation complet", "Yaḥyā b. Saʿīd" in html and "Wāqid b. ʿAmr b. Saʿd b. Muʿāḏ" in html
    and "Nāfiʿ b. Ǧubayr b. Muṭʿim" in html and "Masʿūd b. al-Ḥakam" in html
    and "ʿAlī b. Abī Ṭālib" in html)
chk("Ǧābir b. ʿAtīk tranché", "ʿAtīk" in html)
chk("isnād hâte : Nāfiʿ + Abū Hurayra", "Nāfiʿ" in html and "Abū Hurayra" in html)

# āya rendue du cache + doctrine R511
chk("rendu cache Baqara", "Certes nous sommes à Allah, et c’est à Lui que nous retournerons." in html)
chk("renvoi imprimé 155 tranché", "l’āya 155" in text)
chk("cache 156 documenté", "n° 156" in text)
chk("doctrine R511 citée", "R511" in html)
chk("décalage d'une unité documenté", "moins un" in html)
chk("correspondance par le texte", "correspondance tranchée par le texte" in html)

# lexies tranchées
chk("fa-yaḥtasibuhum tranché", "fa-yaḥtasibuhum" in html)
chk("ḫafīfan tranché", "ḫafīfa" in html)
chk("consensus des savants tranché", "consensus des savants" in html)
chk("taqrīb tranché", "taqrīb" in html)
chk("bi-ṯawb porté", "bi-ṯawb" in html)
chk("laḥd + naṣban portés", "laḥd" in html and "naṣban" in html)
chk("al-labin porté", "al-labin" in html)
chk("lexies ḫams ḏawd / awlāq / awsāq", "ḫams ḏawd" in html and "awlāq" in html and "awsāq" in html)
chk("item zakāt de la préparation", "Je fais connaître la zakāt" in html)

# fragments déclarés (jamais reconstitués)
chk("al-muḫtafī / al-muḫtaniqa portés sous réserve", "al-muḫtafī" in html and "al-muḫtaniqa" in html)
chk("glose nabbāš al-qubūr portée", "nabbāš al-qubūr" in html)
chk("tubakkina bākiyatan portée", "tubakkina bākiyatan" in html)
chk("verbe de Ǧābir déclaré non reconstitué", "verbe imprimé en graphie dégradée" in html
    and "jamais reconstitué" in html)
chk("date cent six sous réserve", "cent six" in html)
chk("jamais reconstitués (pluriel, fragments)", "jamais reconstitués" in html)

# doctrine clé du cours
chk("qirāṭ / mont Uḥud", "qirāṭ" in html and "mont Uḥud" in html)
chk("al-ʿAqīq glosé", "al-ʿAqīq" in html and "un lieu proche de Médine" in html)
chk("glose yaḥtasibu", "yaḥtasibu" in html)
chk("glose rempart contre le Feu", "rempart contre le Feu" in html)
chk("bio ʿAmra : thiqa ḥuǧǧa", "ṯiqa ḥuǧǧa" in html)
chk("bio : année 98 / âge 97", "quatre-vingt-dix-huit" in html and "quatre-vingt-dix-sept" in html)
chk("cinq items d'ādāb", "1 — S’abstenir des pleurs" in html and "5 — S’abstenir de profaner" in html)
chk("station debout pour la funéraille", "se tenir debout pour la funéraille" in html)
chk("transfert : deux cas", "ramener la question à deux cas" in html)

# préparation préalable : matière leçon suivante déclarée
chk("slot pdf-16 déclaré", "pdf-16" in html)
chk("hadith des seuils déclaré (5 ḏawd / awqiya)", "cinq ḏawd" in html and "awqiya" in html)
chk("Abū Saʿīd al-Ḫudrī déclaré", "al-Ḫudrī" in html)
chk("matière suivante jamais produite ici", "jamais produite ici" in html)

print(f"verify-hadith2-pdf15 : PASS {ok} contrôles, {fail} échec" if fail == 0
      else f"verify-hadith2-pdf15 : ÉCHEC {fail} / {ok+fail}")
raise SystemExit(0 if fail == 0 else 1)

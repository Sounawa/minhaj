#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Minhāj — Vérification de la leçon hadith2-pdf-13 (leçon 12, حكم الصلاة بعد
الصبح والعصر, p.86-90 + p.91 matière) : contrôle de contenu, numéros du
Muwaṭṭaʾ tranchés par preuve image (587/591/588/589/593 contre couches
785/195/885/conforme/395 — mécanique d'inversion totale R535-R547),
renvoi coranique an-Nisāʾ 102 imprimé = cache 103 (doctrine R511
« imprimé warš = cache ḥafᶜ moins un »), bornes p.86-90 à convergence
d'image parfaite avec la carte R534 (objectifs p.86, إعداد p.90,
ouverture du cours suivant p.91), isnāds tranchés par image
(Zayd b. Aslam / ʿAṭāʾ b. Yasār / aṣ-Ṣanābiḥī ; Muḥammad b. Yaḥyā b. Ḥibbān
/ al-Aġarr [graphie al-Aġraǧ réservée] / Abū Hurayra ; al-ʿAlāʾ b. ʿAbd
ar-Raḥmān / Anas b. Mālik ; exploitation : Abū ʿAmmār et ʿAlī b. Ḫašram /
Sufyān b. ʿUyayna / Abū az-Zubayr / ʿAbdallāh b. Bāba / Ǧubayr b. Mutʿim),
matn d'exploitation aux points fondus + convergence externe Tirmidhī 868,
fragments déclarés jamais reconstitués.
Usage: python3 scripts-translate/verify-hadith2-pdf13.py
"""
import re

HTML = "/home/z/my-project/tr-tmp/lesson-hadith2-pdf-13-fr.html"

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
chk("h1 leçon 12", "leçon 12" in html and "<h1>" in html)
chk("lesson-meta présent", 'class="lesson-meta"' in html and "Source du cours" in html)
chk("bornes pages 86 à 90 citées (miroir)", "pages 86 à 90" in html)
chk("slot pdf-13 déclaré", "pdf-13" in html)
chk("badge portail Leçon 13 / 31", "Leçon 13 / 31" in text)
chk("hadith-2es déclaré", "hadith-2es" in html)
chk("miroir 208 pages cité", "deux cent huit pages" in html)
chk("titre registre en h1", "Les prières surérogatoires après le faǧr et le ʿaṣr" in html)

# chaîne de production consignée
chk("claim 16:29:10Z consigné", "16 :29 :10Z" in text)
chk("claim rafraîchi 16:45:34Z consigné", "16 :45 :34Z" in text)
chk("trace ouvrier C consignée", "cron-agent-loop-202611040025" in html)
chk("GARDE-DOUBLON R551 > R550", "R550" in html and "R551" in html)
chk("hadith-2es 10/30 → 11/30", "10/30" in html and "11/30" in html)
chk("claims concurrentes pdf-12 consignées", "2334-R555" in html)
chk("claims concurrentes pdf-16 consignées", "2215-R553" in html)
chk("claims périmées pdf-14/pdf-15 consignées", "d61cf595-R554" in html and "2209-R552" in html)
chk("pile purgée e30f40c2 consignée", "e30f40c2" in html)

# bornes + convergence carte parfaite
chk("objectifs p.86", "page 86" in html)
chk("évaluation/préparation p.90", "page 90" in html)
chk("page 91 ouvre la leçon suivante", "page 91 ouvre la leçon suivante" in html)
chk("carte R534 l12=86", "l12 = 86" in html)
chk("carte R534 l13=91", "l13 = 91" in html)
chk("convergence parfaite image/carte", "convergence parfaite" in html)
chk("jamais devinée (borne)", "jamais devinée" in html)

# numéros Muwaṭṭaʾ tranchés + couches déclarées
for num in ("587", "591", "588", "589", "593"):
    chk(f"numéro {num} présent", f"n° {num}" in html)
chk("couche 785 déclarée", "785" in html)
chk("couche 195 déclarée", "195" in html)
chk("couche 885 déclarée", "885" in html)
chk("couche 395 déclarée", "395" in html)
chk("couche 589 conforme déclarée", "couche conforme" in html)
chk("inversion totale citée", "inversion totale" in html)
chk("cinq inversions cohérentes déclarées", "cinq tokens d’inversion" in text or "cinq inversions" in text)

# renvoi coranique + doctrine R511
chk("rendu cache an-Nisāʾ", "En vérité, la prière fut prescrite aux croyants à des heures déterminées" in html)
chk("renvoi imprimé Nisāʾ 102", "l’āya 102" in text)
chk("couche 201 déclarée", "« 201 »" in text)
chk("cache āya 103", "āya n° 103" in text or "l’āya n° 103" in text)
chk("doctrine R511 appliquée", "imprimé warš = cache ḥafᶜ moins un" in html)
chk("102 = 103 − 1 explicite", "102 = 103 − 1" in html)

# isnāds tranchés
chk("isnād 1 : Zayd b. Aslam / ʿAṭāʾ b. Yasār / aṣ-Ṣanābiḥī",
    "Zayd b. Aslam" in html and "ʿAṭāʾ b. Yasār" in html and "ʿAbdallāh aṣ-Ṣanābiḥī" in html)
chk("isnād 2 : Muḥammad b. Yaḥyā b. Ḥibbān", "Muḥammad b. Yaḥyā b. Ḥibbān" in html)
chk("couche Baḥyā récusée", "Baḥyā" in html)
chk("al-Aġarr porté", "al-Aġarr" in html)
chk("graphie al-Aġraǧ réserve déclarée", "al-Aġraǧ" in html and "réserve déclarée" in html)
chk("Abū Hurayra porté", "Abū Hurayra" in html)
chk("récit d’Anas : al-ʿAlāʾ b. ʿAbd ar-Raḥmān", "al-ʿAlāʾ b. ʿAbd ar-Raḥmān" in html
    and "Anas b. Mālik" in html)
chk("couche li-ṣalātin aw ḏikrihi récusée", "li-ṣalātin aw ḏikrihi" in html)
chk("isnād exploitation complet", "Abū ʿAmmār" in html and "ʿAlī b. Ḫašram" in html
    and "Sufyān b. ʿUyayna" in html and "Abū az-Zubayr" in html
    and "ʿAbdallāh b. Bāba" in html and "Ǧubayr b. Mutʿim" in html)

# matières doctrinales du cours
chk("pair du démon = sa force (gloss)", "sa force" in html and "quwwatuhū" in html)
chk("matn 1 : interdiction aux heures", "a interdit la prière à ces heures-là" in html)
chk("bord du soleil : retardez la prière", "retardez la prière" in html)
chk("az-Zuhrī/ʿAbda : entre les deux paires", "entre les deux paires du démon" in html)
chk("fariḍa : rakʿa du ṣubḥ/ʿaṣr attrapée", "Qui attrape du ṣubḥ une rakʿa" in html)
chk("sans excuse : non permis", "qui n’a pas d’excuse, cela ne lui est pas permis" in text)
chk("prière des hypocrites ×3", "la prière des hypocrites, voilà la prière des hypocrites, voilà la prière des hypocrites" in html)
chk("soleil jaunisse + qarnayn", "soleil jaunisse" in html and "paire du démon" in html)
chk("exception a : rakʿatā al-faǧr", "les deux rakʿas de l’aube" in html and "ragība" in html)
chk("exception b : al-ward al-muʿtād min al-layl", "al-ward al-muʿtād min al-layl" in html)
chk("exception b : priorité ṣubḥ en commun", "saisir le ṣubḥ avec la communauté est plus prioritaire" in html)
chk("exception c : aš-šafʿ et al-witr", "aš-šafʿ et al-witr" in html)
chk("ʿUmar frappe le blâmable (Sāʾib b. Yazīd)", "Sāʾib b. Yazīd" in html
    and "frapper le blâmable" in html and "ʿUmar b. al-Ḫaṭṭāb" in html)

# exploitation : matn fondus + convergence externe
chk("Ô fils de ʿAbd Manāf", "Ô fils de ʿAbd Manāf" in html)
chk("n’empêchez personne de faire le ṭawāf de cette Maison",
    "n’empêchez personne de faire le ṭawāf de cette Maison" in html)
chk("à toute heure qu’il veut, de nuit ou de jour", "à toute heure qu’il veut, de nuit ou de jour" in html)
chk("renvoi Tirmidhī tel qu’imprimé (aṣ-Ṣawm)", "kitāb aṣ-Ṣawm" in html)
chk("écart Kitāb al-Ḥaǧǧ documenté", "Kitāb al-Ḥaǧǧ" in html and "écart de classement documenté" in html)
chk("texte n° 868 de l’édition en ligne", "868" in html)
chk("points médians fondus déclarés", "points médians fondus" in html)
chk("séquence bi-hāḏā l-bayt non perceptible", "non perceptible" in html)
chk("jamais reconstitué au-delà", "jamais reconstitué au-delà" in html)

# traduction des transmetteurs
chk("bio aṣ-Ṣanābiḥī : Abū ʿAbdallāh + صحبة discutée", "Abū ʿAbdallāh" in html
    and "Compagnie demeure discutée" in html)
chk("rapporta d’Abū Bakr et ʿUbāda b. aṣ-Ṣāmit", "ʿUbāda b. aṣ-Ṣāmit" in html)
chk("Yaḥyā b. Maʿīn + ʿAbd al-Malik b. Marwān + as-sarīr",
    "Yaḥyā b. Maʿīn" in html and "ʿAbd al-Malik b. Marwān" in html and "as-sarīr" in html)

# préparation préalable : matière leçon suivante déclarée
chk("slot pdf-14 déclaré", "pdf-14" in html)
chk("lexies ašʿarnahā / suḥūliyya / naʿā an-Naǧāšī",
    "ašʿarnahā iyyāhū" in html and "suḥūliyya" in html and "naʿā an-Naǧāšī" in html)
chk("récit Umm ʿAṭiyya annoncé", "Umm ʿAṭiyya" in html)
chk("renvoi al-Isrāʾ non tranché déclaré", "sūrat al-Isrāʾ" in html
    and "non tranché ici" in html)
chk("bornes pdf-14 = 91 à 97 déclarées", "91 à 97" in html)

print(f"\nOK: {ok}  ÉCHECS: {fail}")
raise SystemExit(1 if fail else 0)

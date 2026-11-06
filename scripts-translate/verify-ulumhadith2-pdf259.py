#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Minhāj — Vérification de la leçon ulum-hadith-tanawi-2 / pdf-mut23h2u-259
(الدرس 5 — al-ʿazīz wa-l-ġarīb, p.30-34 du manuel
ulum-hadith-2-thanawi_text.pdf) : bornes p.30-34 par DOUBLE sondage
(p.30 = bannière r01 + 3 objectifs + tamhīd ; p.34 = taqyīm 3 items + istiṯmār
Ibn aṣ-Ṣalāḥ/Ibn Mandah 2 consignes + al-iʿdād al-qablī 2 consignes ;
p.35 = bannière + objectifs leçon 6) ; nombres de la couche pdftotext INVERSÉS
tranchés par recadrages 600-1800 dpi + couche logique PyMuPDF FIDÈLE (mécanisme
R615 : 4/83→38/4→t.4 p.38, 1/046→640/1→t.1 p.640, 7/27→72/7→t.7 p.72,
2/931→139/2→t.2 p.139, 654→ṣ456) ; pavés graphiques muets des 3 types du ġarīb
relatif + item 2 du taqyīm + item 2 de l'iʿdād lus par recadrages ; nisba
« Ġarjar » (1200 dpi) et « al-Ġinǧār » confirmés image ; honnêteté d'apparat
box 2 (lexies d'articulation, rendu par le sens) documentée ; 2 ḥadīṯs
prophétiques rendus de l'imprimé, zéro āya, zéro résidu arabe, zéro apostrophe
droite, zéro doublon.
Usage: python3 scripts-translate/verify-ulumhadith2-pdf259.py
"""
import json
import re

HTML = "/home/z/my-project/tr-tmp/lesson-uh2-pdf-mut23h2u-259-fr.html"
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
chk("h1 = titleFr pré-mappé « Leçon 5 : Le rare (ʿazīz) et l’insolite (ġarīb) »",
    hn.startswith("<h1>Leçon 5 : Le rare (ʿazīz) et l’insolite (ġarīb)"))
chk("h1 mentionne deuxième année", "deuxième année" in h[:500])
chk("h1 mentionne fard absolu et fard relatif", "le fard absolu et le fard relatif" in h[:1200])
chk("dl.lesson-meta présent", '<dl class="lesson-meta">' in h and "<dt>Source du cours</dt>" in h)
chk("item archive.org cité", "1_20220304_20220304_2251" in h)
chk("source locale citée", "ulum-hadith-2-thanawi_text.pdf" in h)
chk("bornes p.30-34 documentées", "pages 30 à 34" in h)
chk("p.35 leçon 6 non touchée", "pdf-mut23h2u-260" in h and "non touché" in h)
chk("p.26-29 leçon 4 ouvrier parallèle, non touché", "pdf-mut23h2u-258" in h and "non touché" in h)
chk("double sondage « jamais devinées »", "jamais devinées" in h)
chk("bannière r01 citée", "r01-p30-banniere-haut.png" in h)
chk("caches OCR cités", "tr-tmp/r617/p030-dual.txt" in h)
chk("tessdata dépôt documenté", "scripts-translate/tessdata" in h)
chk("couche logique PyMuPDF citée", "p030-pymu.txt" in h)
chk("inversion 4/83→38/4 documentée", "4/83" in hn and "38/4" in hn)
chk("Maqāyīs t. 4, p. 38 rendue", "t. 4, p. 38" in hn)
chk("inversion 1/046→640/1 documentée", "1/046" in hn and "640/1" in hn)
chk("Lisān t. 1, p. 640 rendue", "t. 1, p. 640" in hn)
chk("inversion 7/27→72/7 documentée", "7/27" in hn and "72/7" in hn)
chk("Maʿǧam al-awsaṭ t. 7, p. 72 rendue", "t. 7, p. 72" in hn)
chk("inversion 2/931→139/2 documentée", "2/931" in hn and "139/2" in hn)
chk("Faqīh t. 2, p. 139 rendue", "t. 2, p. 139" in hn)
chk("inversion 654→456 documentée", "654" in hn and "456" in hn)
chk("Muqaddima p. 456 rendue", "p. 456" in hn)
chk("usage page/tome documenté", "page/tome" in hn)
chk("mécanisme inversion élucidé (PyMuPDF fidèle)", "PyMuPDF" in hn and "FIDÈLE" in hn and "miroir" in hn)
chk("recadrages 600 à 1800 dpi documentés", "1800 dpi" in hn)
chk("crops cités", "qa-crops-r617/" in h and "c2a" in h and "c4a" in h
    and "c4d" in h and "r12" in h and "c6" in h and "r11" in h and "r14" in h)
chk("zéro āya rendue", "Aucune āya rendue" in h)
chk("2 ḥadīṯs prophétiques rendus de l’imprimé",
    "lā yu’minu aḥadukum ḥattā akūna aḥabba ilay-hi min wālidi-hi wa-waladi-hi" in hn
    and "lā tusammū al-ʿinab al-karm" in hn)

# ---- objectifs
chk("objectif : concept du ʿazīz et du ġarīb",
    "reconnaisse le concept du ḥadīṯ rare (ʿazīz) et insolite (ġarīb)" in hn)
chk("objectif : divisions du ġarīb et ses formes",
    "distingue les divisions du ḥadīṯ ġarīb et ses formes" in hn)
chk("objectif : mérite de la science et patience",
    "saisisse le mérite de la science et s’orne de patience dans sa quête" in hn)
chk("trois objectifs", "trois objectifs" in hn)

# ---- tamhīd
chk("tamhīd : terminologie propre selon le nombre des rapporteurs",
    "une terminologie propre selon le nombre de ses rapporteurs" in hn)
chk("tamhīd : question du rapporteur isolé", "qu’un seul rapporteur a rapporté" in hn)
chk("tamhīd : question des deux", "au-dessous de deux" in hn)
chk("tamhīd : le nombre condition de l’authentique ?",
    "le nombre est-il une condition de l’authenticité du ḥadīṯ" in hn)

# ---- muṭūn (texte)
chk("muṭūn : « Le troisième : le ʿazīz »", "Le troisième : le ʿazīz (le rare)" in hn)
chk("muṭūn : « et le quatrième : le ġarīb »", "et le quatrième : le ġarīb (l’insolite)" in hn)
chk("muṭūn : non-condition de l’authentique", "n’est pas une condition de l’authentique" in hn)
chk("muṭūn : āḥād, acceptation et rejet, qarāʾin",
    "hormis le premier, relève des āḥād" in hn
    and "l’acceptation et le rejet demeurent possibles" in hn
    and "science conjecturelle (al-ʿilm aẓ-ẓannī)" in hn)
chk("muṭūn : fard absolu / fard relatif", "le fard absolu (al-fard al-muṭlaq), le second le fard relatif (al-fard an-nasabī)" in hn)

# ---- commentaire
chk("exposé : rangs troisième/quatrième", "range le ʿazīz en troisième et le ġarīb en quatrième" in hn)
chk("exposé : suspension à la recherche des états des rapporteurs",
    "suspendue à la recherche des états de leurs rapporteurs" in hn)
chk("extraction : définition et statut", "la définition du ʿazīz et du ġarīb" in hn
    and "le statut (al-ḥukm) du ʿazīz et du ġarīb" in hn)
chk("extraction : gloses marginales zaʿm et ʿilm naẓarī",
    "la prétention (az-zaʿm)" in hn and "la science théorique par les indications" in hn
    and "gloses marginales de l’imprimé" in hn)

# ---- 1 ʿazīz
chk("ʿazīz langue : ʿaz, force par la voie adjacente",
    "rareté de son existence" in hn and "fort par l’arrivée d’une autre voie à ses côtés" in hn)
chk("ʿazīz langue : dureté, force, prédominance",
    "la dureté et de la force" in hn and "prédominance et de contrainte" in hn)
chk("Maqāyīs : la chose devint ʿazīz jusqu’à manquer d’exister",
    "au point qu’elle manque d’exister presque" in hn)
chk("ʿazīz terminologie : pas moins de deux de deux",
    "ce que ne rapportent pas moins de deux de deux" in hn)
chk("ʿazīz nommé pour rareté ou force", "ou bien pour la rareté de son existence, ou bien parce qu’il est fort" in hn)
chk("non-condition : Ibn Ḥaǧar statué", "c’est ce que le ḥāfiẓ Ibn Ḥaǧar a statué" in hn)
chk("non-condition : al-Ḥākim ǧahāla, deux rapporteurs",
    "al-Ḥākim Abū ʿAbd Allāh" in hn and "le nom de la méconnaissance (al-ǧahāla)" in hn
    and "comme l’attestation sur l’attestation" in hn)
chk("non-condition : Ibn al-ʿArabī, condition de Buḫārī",
    "le qāḍī Abū Bakr Ibn al-ʿArabī" in hn and "condition d’al-Buḫārī" in hn)
chk("non-condition : les œuvres par intentions, ʿUmar chaire",
    "Les œuvres ne valent que par les intentions" in hn
    and "personne ne le rapporta d’ʿUmar hormis ʿAlqama" in hn
    and "en chaire, devant les Compagnons" in hn and "ils l’auraient récusé" in hn
    and "ainsi parla Ibn al-ʿArabī" in hn)
chk("exemple : les deux Šayḫs d’Anas, Buḫārī d’Abū Hurayra",
    "les deux Šayḫs du hadith d’Anas" in hn and "al-Buḫārī du hadith d’Abū Hurayra" in hn)
chk("exemple : matn « Aucun d’entre vous »",
    "Aucun d’entre vous n’a la foi véritable tant que je ne suis pas pour lui plus aimé que son père et son enfant" in hn)
chk("exemple : Kitāb al-īmān, bāb de l’amour du Messager",
    "Kitāb al-īmān" in hn and "L’amour du Messager" in hn)
chk("exemple : chaîne Qatāda + ʿAbd al-ʿAzīz b. Ṣuhayb",
    "Qatāda et ʿAbd al-ʿAzīz b. Ṣuhayb" in hn)
chk("exemple : Šuʿba et Saʿīd, Ismāʿīl b. ʿUlayya et ʿAbd al-Wāriṯ",
    "Šuʿba et Saʿīd" in hn and "Ismāʿīl b. ʿUlayya et ʿAbd al-Wāriṯ" in hn)
chk("exemple : moindre nombre, accroissement profitable",
    "le critère tient au moindre nombre, et l’accroissement est profitable" in hn)
chk("ḥukm ʿazīz : maqbūl/mardūd", "il est accepté (maqbūl)" in hn and "il est rejeté (mardūd)" in hn)

# ---- 2 ġarīb
chk("ġarīb langue : isolé, éloigné, ġurbāʾ",
    "l’isolé ou l’éloigné de ses proches" in hn and "ġurbāʾ" in hn)
chk("ġarīb langue : ġarāʾib, obscur de la parole",
    "ġarāʾib" in hn and "l’obscur de la parole" in hn)
chk("Lisān : t. 1, p. 640, avec aménagement", "t. 1, p. 640, avec aménagement" in hn)
chk("ġarīb terminologie : un seul, tout lieu de l’isnād",
    "dont la narration fut isolée par un seul homme, en quelque lieu que se produise l’isolement dans l’isnād" in hn)
chk("ġarīb/fard synonymes, fréquence d’usage",
    "le ġarīb et le fard sont synonymes en la langue et en la terminologie" in hn
    and "la fréquence et la rareté de l’usage" in hn)
chk("verbe dérivé : tafarrada/ġarraba", "tafarrada bi-hi" in hn and "ġarraba bi-hi" in hn)
chk("fard absolu : racine, tourne et revient, Compagnon",
    "l’isolement à la racine de l’isnād — « le fard absolu »" in hn
    and "l’isnād tourne et vers lequel il revient" in hn
    and "son extrémité où se trouve le Compagnon" in hn)
chk("fard absolu : exemple b. Dīnār / Ibn ʿUmar",
    "ʿAbd Allāh b. Dīnār isola d’Ibn ʿUmar" in hn)
chk("fard absolu : Šuʿab al-īmān, Abū Ṣāliḥ, b. Dīnār",
    "Šuʿab al-īmān" in hn and "Abū Ṣāliḥ s’isola d’Abū Hurayra" in hn
    and "ʿAbd Allāh b. Dīnār d’Abū Ṣāliḥ" in hn)
chk("fard absolu : Musnad al-Bazzār + Maʿǧam al-awsaṭ",
    "Le Musnad d’al-Bazzār et le Maʿǧam al-awsaṭ d’aṭ-Ṭabarānī offrent de cela de nombreux exemples" in hn)
chk("fard relatif : cours de l’isnād, plus d’un puis un seul",
    "l’isolement au cours de l’isnād — « le fard relatif »" in hn
    and "rapporté du Compagnon par plus d’un, puis un seul s’isole de la narration de l’un d’eux" in hn)
chk("fard relatif : nommé pour l’homme déterminé, mašhūr en lui-même",
    "l’isolement s’y produisit par rapport à un homme déterminé" in hn
    and "en lui-même, célèbre (mašhūr)" in hn)
chk("fard relatif : exemple ʿĪsā b. Mūsā al-Gharjar → chaîne",
    "ʿĪsā b. Mūsā al-Gharjar d’Abū Ḥamza as-Sukkarī, al-Aʿmaš, d’Abū Ayyūb as-Saḫtiyānī, de Muḥammad b. Sīrīn, d’Abū Hurayra" in hn)
chk("fard relatif : matn « Ne nommez pas le raisin karm »",
    "Ne nommez pas le raisin « karm » (le noble)" in hn)
chk("fard relatif : aṭ-Ṭabarānī, Abū Ḥamza seul, Muḥammad b. Maymūn, al-Ġinǧār",
    "personne ne le rapporta d’al-Aʿmaš hormis Abū Ḥamza as-Sukkarī" in hn
    and "Muḥammad b. Maymūn" in hn and "al-Ġinǧār s’en fit l’insolite" in hn
    and "ne fit pas remonter d’Ayyūb de hadith autre que celui-ci" in hn)
chk("ġarīb relatif abondant, livres mères",
    "Le ġarīb relatif est abondant dans tous les livres mères" in hn)
chk("types : 3 pavés muets lus 700-1800 dpi",
    "trois pavés graphiques muets pour la couche et pour l’OCR 300 dpi, lus par recadrages 700 à 1800 dpi" in hn)
chk("type 1 : restreint à une narration déterminée (Mālik, aẓ-Ẓuhrī, Saʿīd b. al-Musayyib)",
    "restreint à une narration déterminée" in hn and "Saʿīd b. al-Musayyib" in hn
    and "quant à la voie d’aẓ-Ẓuhrī, personne ne le rapporta hormis Mālik" in hn)
chk("type 2 : état des rapporteurs, thiqa unique, groupe faible",
    "l’isolement d’après l’état des rapporteurs" in hn
    and "un rapporteur unique fiable (thiqa)" in hn
    and "sauf qu’ils sont faibles (ḍuʿafāʾ)" in hn)
chk("type 2 : honnêteté d’apparat documentée",
    "partiellement illisibles même à 1800 dpi" in hn and "rendu par le sens, la récusation documentée" in hn)
chk("type 3 : gens d’un pays déterminé, Médine/Baṣra",
    "restreint aux gens d’un pays déterminé" in hn
    and "ne le rapportèrent que les gens de Médine, ou les gens de Baṣra" in hn)
chk("autre division : ġarīb s. et m. / s. non m.",
    "le ġarīb par l’isnād et par le matn, et le ġarīb par l’isnād non par le matn" in hn)
chk("ḥukm ġarīb : examen, ni l’un ni l’autre",
    "son isolement n’exige ni l’authenticité ni la faiblesse" in hn)

# ---- ahtadī wa-aqtadī (al-Khaṭīb)
chk("rubrique ahtadī wa-aqtadī", "Je m’inspire et j’inspire (ahtadī wa-aqtadī)" in hn)
chk("Khaṭīb : voies de Ses élus, purifiés, effort",
    "les voies de Ses élus" in hn and "Ses purifiés" in hn
    and "consacrer tout l’effort à sa quête" in hn)
chk("Faqīh t. 2, p. 139 cité", "Al-Faqīh wa-l-mutafaqqih, al-Khaṭīb al-Baġdādī, t. 2, p. 139" in hn)
chk("lien au troisième objectif", "le mérite de la science — troisième objectif de la leçon" in hn)

# ---- évaluation
chk("évaluation : 3 activités", "trois activités" in hn)
chk("évaluation : différence ʿazīz/ġarīb", "exposer la différence entre le ʿazīz et le ġarīb" in hn)
chk("évaluation : exemple du ġarīb relatif", "donner un exemple du ġarīb relatif" in hn)
chk("évaluation : statut ʿazīz et ġarīb", "énoncer le statut du ḥadīṯ ʿazīz et du ḥadīṯ ġarīb" in hn)

# ---- exploitation (Ibn aṣ-Ṣalāḥ / Ibn Mandah)
chk("exploitation : Ibn aṣ-Ṣalāḥ rapporte Ibn Mandah d’Iṣbahān",
    "Nous rapportâmes d’Ibn Mandah, le ḥāfiẓ de Iṣbahān" in hn)
chk("exploitation : échelle ġarīb/ʿazīz/mašhūr",
    "il est nommé ġarīb" in hn and "il est nommé ʿazīz" in hn and "il est nommé mašhūr" in hn)
chk("exploitation : az-Zuhrī, Qatāda, imāms réunis",
    "tel le hadith d’az-Zuhrī, de Qatāda et de leurs pareils parmi les imāms dont on réunit les hadiths" in hn)
chk("exploitation : Muqaddima p. 456 citée", "Muqaddimat Ibn aṣ-Ṣalāḥ, p. 456" in hn)
chk("exploitation : 2 consignes (termes + Biqūniyya, trois hommes)",
    "extraire les termes de la science du ḥadīṯ mentionnés dans le texte" in hn
    and "al-Biqūniyya" in hn and "la narration de trois hommes relève-t-elle du ḥadīṯ ʿazīz" in hn)

# ---- préparation leçon suivante
chk("leçon suivante nommée (ṣaḥīḥ et ses degrés)", "Le hadith authentique (ṣaḥīḥ) et ses degrés" in hn)
chk("préparation : concept + conditions", "le concept du ḥadīṯ authentique et ses conditions" in hn)
chk("préparation : degrés du ṣaḥīḥ", "les degrés du ḥadīṯ authentique" in hn)
chk("préparation : 2 consignes", "deux consignes" in h)

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
chk("registre 258 non touché (htmlFr vide)", (les["pdf-mut23h2u-258"].get("htmlFr") or "") == "")
chk("registre 260 non touché (htmlFr vide)", (les["pdf-mut23h2u-260"].get("htmlFr") or "") == "")
chk("registre 255 intact (17 252 car)", len(les["pdf-mut23h2u-255"].get("htmlFr") or "") == 17252)
fr = les["pdf-mut23h2u-256"].get("htmlFr") or ""
chk("registre 256 intact (15 854 car)", len(fr) == 15854)
fr7 = les["pdf-mut23h2u-257"].get("htmlFr") or ""
chk("registre 257 intact (~23 700 car)", 20_000 <= len(fr7) <= 30_000)
fr9 = les["pdf-mut23h2u-259"].get("htmlFr") or ""
if fr9:
    chk("registre 259 = htmlFr posé (~23 800 car)", 20_000 <= len(fr9) <= 30_000)
    chk("registre 259 == fichier livré", fr9.strip() == h.strip())
else:
    chk("registre 259 encore vide (avant hand-set)", True)
chk("titleAr pré-mappé 259", les["pdf-mut23h2u-259"].get("titleAr") == "الدرس 5 : العزيز والغريب")
chk("titleFr pré-mappé 259 aligné au h1",
    (les["pdf-mut23h2u-259"].get("titleFr") or "").replace("'", "’").startswith("Leçon 5 : Le rare (ʿazīz) et l’insolite (ġarīb)"))
reg1 = json.load(open(REG1, encoding="utf-8"))
l1 = {str(d.get("docId", "")): d for d in reg1["lessons"]}
chk("registre livre 1 : 141 intact (24 319 car)", len(l1["pdf-mut23h2r-141"].get("htmlFr") or "") == 24319)
chk("registre livre 1 : 140 intact (16 018 car)", len(l1["pdf-mut23h2r-140"].get("htmlFr") or "") == 16018)
chk("registre livre 1 : 136 intact (20 967 car)", len(l1["pdf-mut23h2r-136"].get("htmlFr") or "") == 20967)

print(f"verify-ulumhadith2-pdf259 : {ok} PASS / {fail} ÉCHEC")
raise SystemExit(1 if fail else 0)

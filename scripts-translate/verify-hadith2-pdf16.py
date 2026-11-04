#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Minhāj — Vérification de la leçon hadith2-pdf-16 (leçon 15, مفهوم الزكاة وشروطها /
La zakāt : notion et conditions, p.105-111) : contrôle de contenu, numéros du
Muwaṭṭaʾ (655/668/662/664/660/666×2 + récit d'Abū Bakr), bornes p.105-111 à
convergence carte (l15 = 105, l16 = 112) + couche, isnād H1 tranché par lecture
d'image (ʿAmr b. Yaḥyā al-Māzinī ← son père ← Abū Saʿīd al-Khudrī), poids à la
convergence (2,975 g/dirham ; 119 g l'ouqiyya ; 85 g le dīnār d'or ; 4,25 g le
dīnār), āyas rendues du cache (at-Tawba 9:103 ; an-Nūr ou al-Baqara selon le
tranchage image — écart doctrine R511 déclaré), lexies et fragments déclarés.
Usage: python3 scripts-translate/verify-hadith2-pdf16.py
"""
import re

HTML = "/home/z/my-project/tr-tmp/lesson-hadith2-pdf-16-fr.html"

ok, fail = 0, 0
def chk(label, cond):
    global ok, fail
    if cond: ok += 1
    else:
        fail += 1
        print(f"ÉCHEC: {label}")

html = open(HTML, encoding="utf-8").read().replace("\u202f", " ").replace("\u00a0", " ")
text = re.sub(r"<[^>]+>", " ", html)
compact = re.sub(r"[\s\u202f\u00a0]+", "", html)  # forme compacte : horodatages et citations insensibles à l'espacement

# 0 arabe (ﷺ U+FDFA exempté par convention corpus)
arab = re.findall(r"[\u0600-\u06FF\u0750-\u077F\u08A0-\u08FF\uFB50-\uFDF9\uFDFB-\uFDFF\uFE70-\uFEFF]", text)
arab = [c for c in arab if c != "\ufdfa"]
chk("0 caractère arabe au corps", len(arab) == 0)

# structure générale
chk("h1 leçon 15", "leçon 15" in html and "<h1>" in html)
chk("h1 titre-portail exact", "La zakāt : notion et conditions — le livre d’al-Ḥadīth" in html)
chk("lesson-meta présent", 'class="lesson-meta"' in html and "Source du cours" in html)
chk("bornes pages 105 à 111 citées (miroir)", "pages 105 à 111" in html)
chk("slot pdf-16 déclaré", "pdf-16" in html)
chk("badge portail Leçon 16 / 31", "Leçon 16 / 31" in text)
chk("hadith-2es déclaré", "hadith-2es" in html)
chk("miroir 208 pages cité", "deux cent huit pages" in html)
chk("seizième leçon / quinzième fascicule", "Seizième leçon" in html and "quinzième fascicule" in html)

# chaîne de production consignée
chk("passe R559 (Task ID) référencée via trace", "1a1a59caa1484b71" in html)
chk("takeover réglementaire 08:23:27Z consigné", "08:23:27Z" in compact)
chk("rafraîchissements consignés", "08:39:53Z" in compact and "08:59:26Z" in compact)
chk("claim périmé 18:34:57Z consigné", "18:34:57Z" in compact)
chk("recette R508 + recyclage n°5 consignés", "R508" in html and "cinquième récupération" in html)
chk("main = 1219c538 consigné", "1219c538" in html)
chk("reflog invoqué (jamais de reset destructeur)", "reflog" in html)
chk("GARDE-DOUBLON pdf-12 intouché", "pdf-12" in html and "n’a pas été touché" in html)
chk("pdf-17 libéré volontairement consigné", "pdf-17" in html and "libération volontaire" in html)
chk("registre 1117 → 1118 + hadith-2es 14/30", "1117 → 1118" in html and "14/30" in html)
chk("tafsir-5ep clos rappelé", "122/122" in html)
chk("extraction 12 869 caractères consignée", "12 869 caractères" in html)

# bornes + carte
chk("carte l15 = 105 / l16 = 112", "l15 = 105" in html and "l16 = 112" in html)
chk("ouverture objectifs cours suivant p.112 déclarée", "page 112" in html and "minerais" in html)

# isnād H1 tranché par image
chk("isnād H1 ʿAmr b. Yaḥyā al-Māzinī", "ʿAmr b. Yaḥyā al-Māzinī" in html)
chk("isnād H1 par son père", "d’après son père" in html)
chk("isnād H1 Abū Saʿīd al-Khudrī", "Abū Saʿīd al-Khudrī" in html)

# numéros du Muwaṭṭaʾ
for n in ("655", "668", "662", "664", "660"):
    chk(f"renvoi al-Muwaṭṭaʾ n° {n}", f"al-Muwaṭṭaʾ n° {n}" in html)
chk("renvoi n° 666 double (ḥawl ar-ribḥ + exploitation)", html.count("al-Muwaṭṭaʾ n° 666") >= 2)

# hadiths : matière caractéristique
chk("triple nisāb du premier texte (ḏūd/ouqiyyas/wasuq)", "cinq ḏūd" in html and "cinq ouqiyyas" in html and "cinq wasuq" in html)
chk("ṣadaqa rendu", "ṣadaqa" in html)
chk("indivision or-argent (shurakāʾ)", "indivision" in html)
chk("formule « ce que j’ai entendu de mieux »", "ce que j’ai entendu de mieux" in html)

# transmetteur
chk("biographie Saʿd b. Mālik b. Sinān", "Saʿd b. Mālik b. Sinān" in html)
chk("Uḥud « trop jeune »", "trop jeune le jour de Uḥud" in html)
chk("douze expéditions", "douze expéditions" in html)
chk("années de décès 74/64/65", "74" in html and "64" in html and "65" in html)

# définitions et poids (convergences)
chk("wasuq = soixante ṣāʿ", "soixante ṣāʿ" in html)
chk("ṣāʿ = quatre mudd", "quatre mudd" in html)
chk("mudd = deux mains moyennes", "deux mains moyennes" in html)
chk("ouqiyya = quarante dirhams", "quarante dirhams" in html)
chk("dirham 2,975 grammes", "2,975 grammes" in html)
chk("ouqiyya cent dix-neuf grammes", "cent dix-neuf grammes" in html)
chk("dīnār 4,25 grammes", "4,25 grammes" in html)
chk("quatre-vingt-cinq grammes", "quatre-vingt-cinq grammes" in html)

# notions
chk("Ibn Fāris cité (lue : croissance/pureté)", "Ibn Fāris" in html and "croissance" in html and "pureté" in html)
chk("Šarḥ ḥudūd Ibn ʿArafa 1/71 cité", "Ibn ʿArafa" in html and "1/71" in html)
chk("troisième pilier", "troisième pilier" in html)
chk("hadith des cinq piliers (Bukhārī)", "Ṣaḥīḥ d’al-Buḫārī" in html and "bâti sur cinq" in html)

# āyas du cache
chk("āya at-Tawba 9:103 rendue du cache", "Prélève sur leurs biens" in html and "quiétude" in html)
chk("āya de l’obéissance rendue du cache (texte commun)", "acquittez la zakāt" in html)
chk("écarts de numérotation déclarés (doctrine R511)", "écart déclaré" in html)
chk("renvoi al-Baqara 43 / an-Nūr 54 non tranché — déclaré", "al-Baqara, āya 43" in html and "an-Nūr, āya 54" in html and "non tranché" in html)
chk("at-Tawba 103/104 déclaré non tranché", "«103»" in compact and "«104»" in compact)
chk("membre commun seul rendu — jamais reconstitué", "jamais reconstituée" in html)
chk("wasuq 130,6 / 6,130 déclaré non tranché", "130,6" in html and "6,130" in html)
chk("grains ḫamsūn / ḫams miʾa déclarés", "ḫamsūn" in html and "ḫams miʾa" in html)
chk("waqṣ translittéré, glose déclarée", "waqṣ" in html and "glose non restituée" in html)
chk("récit 658 sous réserve déclarée", "658" in html and "réserve déclarée" in html)

# conditions
chk("seuil niṣāb défini", "seuil (niṣāb)" in html)
chk("160 dirhams / huit par dīnār", "cent soixante dirhams" in html and "huit dirhams par dīnār" in html)
chk("l’argent ne s’évalue pas par l’or", "l’argent ne s’évalue pas par l’or" in html)
chk("ḥawl exigé, grains et fruits exclus", "à l’exclusion des grains et des fruits" in html)
chk("Ibn ʿUmar « que Dieu soit satisfait de lui et de son père »", "que Dieu soit satisfait de lui et de son père" in html)
chk("acquis : héritage/donation/loyer/fermage", "héritage" in html and "donation" in html and "loyer" in html and "fermage" in html)
chk("récit Abū Bakr / allocations (ʿaṭāʾ)", "Abū Bakr" in html and "allocations" in html)
chk("cinq dīnārs de l’exploitation", "cinq dīnārs" in html)
chk("un jour de ḥawl (exploitation)", "d’un jour" in html)

# évaluation / exploitation / préparation
chk("trois questions d’évaluation", "l’écoulement de l’année n’est pas exigé" in html)
chk("waqṣ translittéré (rasm déclaré)", "waqṣ" in html)
chk("question du ǧumhūr", "al-ǧumhūr" in html)
chk("préparation : minerais/rikāz, biens exclus, mort sans zakāt", "rikāz" in html and "mourut sans avoir prélevé" in html)

# typographie française
apost = html.count("'")
chk("0 apostrophe droite", apost == 0)
ouvr, ferm = html.count("«"), html.count("»")
chk("guillemets « » appariés", ouvr == ferm and ouvr > 20)

print(f"\nverify-hadith2-pdf16 : {ok} contrôles OK, {fail} échec(s)")
import sys
sys.exit(1 if fail else 0)

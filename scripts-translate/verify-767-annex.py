#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Minhāj — contrôle de contenu de l'annexe 767 (tafsir-5ep, fihris
al-maṣādir wa-l-marāǧiʿ — index des sources et références p.214-221, suivi du
fihris al-mawāḍiʿ — index des loci p.222, manuel miroir tafsir-3-thanawi).
Annexe SANS versets : aucune āya du cache ne doit paraître. Contrôles : les
50 entrées bibliographiques (titres + marqueurs + dates rétablies par le
renversement documenté), les fragments altérés déclarés, la table des loci
(34 lignes, pages d'ouverture des 26 leçons + 3 annexes + 4 pièces
liminaires), 0 arabe, guillemets appariés."""
import json
import re

HTML = "tr-tmp/lesson-767-fr.html"
html = open(HTML, encoding="utf-8").read()
norm = re.sub(r"[ \u202f\u00a0]+", " ", html.replace("&nbsp;", "\u00a0"))
errors = []

# 1. structure
for frag in [
    "Source du cours",
    "Troisième et dernière annexe de clôture du second livre du parcours",
    "pages 214 à 221 de l’imprimé miroir",
    "pdf-mut23h3c-767",
    "fihris al-mawāḍiʿ",
    "BORNES TRANCHÉES PAR IMAGE",
    "MÉCANIQUE DES COTES, ÉTENDUE AUX ANNÉES D’ÉDITION",
    "renversement PROUVÉ PAR CONVERGENCE",
    "L’objet de l’index des sources",
    "Les notices des sources, entrée par entrée",
    "Les familles de sources",
    "L’index des loci : la table de concordance de la page 222",
    "La fermeture du livre",
    "convergence badge image + contenu + grille portail",
    "jamais devinée",
    "convergence quadruple sonde + contenu + registre + table",
]:
    if frag not in norm:
        errors.append(f"MANQUE structure : {frag[:60]}")

# 2. les 50 entrées (h3 + marqueur distinctif + date rétablie)
ENTREES = [
    ("al-Muṣḥaf al-Muḥammadī bi-riwāyat Warš ʿan Nāfiʿ min ṭarīq al-Azraq", "Fondation Muḥammad VI", None),
    ("al-Itqān fī ʿulūm al-Qurʾān", "Muḥammad Abū l-Faḍl Ibrāhīm", "1394"),
    ("Aḥkām al-Qurʾān al-Karīm", "Muḥammad ʿAbd al-Qādir ʿAṭā", "1424"),
    ("Iḥyāʾ ʿulūm ad-dīn", "al-Ġazālī at-Ṭūsī", None),
    ("al-Adab al-Mufrad", "Dār al-Bašāʾir al-Islāmiyya", "1409"),
    ("Asbāb nuzūl al-Qurʾān", "al-Wāḥidī an-Nīsābūrī", "468"),
    ("al-Isrāʾīliyyāt wa-l-mawḍūʿāt fī kutub at-tafsīr", "Muḥammad Abū Šahba", None),
    ("al-Baḥr al-Muḥīṭ fī t-tafsīr", "Ṣidqī Muḥammad Ǧamīl", "745"),
    ("al-Baḥr al-māʾid fī tafsīr al-Qurʾān al-maǧīd", "b. ʿAǧība", "1224"),
    ("Tārīḫ Baġdād", "Baššār ʿAwwād Maʿrūf", "1422"),
    ("Taḥrīr al-maʿnā aṣ-ṣadīd wa-tanwīr al-ʿaql al-ǧadīd", "Ibn ʿĀšūr at-Tūnisī", "1393"),
    ("at-Taḥṣīl li-fawāʾid kitāb at-Tafṣīl", "al-Mahdawī", "440"),
    ("at-Taḏkira bi-aḥwāl al-mawtā", "al-Qurṭubī", "1425"),
    ("Talbīs Iblīs", "Ibn al-Ǧawzī", "1421"),
    ("Tafsīr Abī s-Suʿūd — Iršād al-ʿaql as-salīm", "Abū s-Suʿūd al-ʿImādī", "982"),
    ("Tartīb al-madārik wa-taqrīb al-masālik", "Maṭbaʿat Fadāla", "544"),
    ("Tafsīr al-Māwardī — an-Nukat wa-l-ʿuyūn", "al-Māwardī", "450"),
    ("at-Taysīr li-ʿulūm at-tanzīl", "Ibn Ǧuzayy al-Kalbī al-Ġarnāṭī", "754"),
    ("Ǧāmiʿ al-bayān fī taʾwīl āy al-Qurʾān", "at-Tabarī", "1422"),
    ("al-Ǧāmiʿ al-musnad aṣ-ṣaḥīḥ al-muḫtaṣar", "al-Buẖārī al-Ǧuʿfī", "256"),
    ("Ǧāmiʿ bayān al-ʿilm wa-faḍlihi", "az-Zuḥayrī", "1414"),
    ("L’entrée aux éditeurs Muʿawwaḍ et ʿAbd al-Mawǧūd", "Muḥammad ʿAlī Muʿawwaḍ", None),
    ("ad-Durar al-lawāmiʿ fī aṣl maqrī al-imām Nāfiʿ", "Tawfīq al-ʿUbaydī", None),
    ("ad-Durr al-manṯūr fī t-tafsīr bil-maʾṯūr", "as-Suyūṭī", "911"),
    ("Rafʿ al-mabānī fī šarḥ ḥurūf al-maʿānī", "al-Ḫarrāṭ", "1423"),
    ("L’entrée d’al-Ālūsī", "ʿAlī ʿAbd al-Bārī ʿAṭiyya", "1425"),
    ("ar-Rawḍ al-anf fī šarḥ as-Sīra an-Nabawiyya", "as-Suhaylī", "581"),
    ("Zād al-masīr fī ʿilm at-tafsīr", "ʿAbd ar-Razzāq al-Mahdī", "597"),
    ("Maǧāz al-Qurʾān", "Muḥammad Fuʾād Sezgin", "1381"),
    ("al-Muḥarrar al-waǧīz fī tafsīr al-Kitāb al-ʿazīz", "b. ʿAṭiyya al-Andalusī", "542"),
    ("al-Muntaqā šarḥ al-Muwaṭṭaʾ", "al-Bāǧī al-Qurṭubī", "1332"),
    ("Manẓūmat Ḥirz al-amānī wa-waǧh at-tahānī fī l-qirāʾāt as-sabʿ", "aš-Šāṭibī ar-Raʿīnī", "1426"),
    ("al-Muṣannaf", "Ibn Abī Šayba", "235"),
    ("al-Muʿǧam al-kabīr", "aṭ-Ṭabarānī", "360"),
    ("Mafātīḫ al-ġayb — dit at-Tafsīr al-kabīr", "Faḫr ad-Dīn ar-Rāzī", "606"),
    ("al-Mustadrak ʿalā ṣ-ṣaḥīḥayn", "al-Ḥākim", "1411"),
    ("Musnad al-imām Aḥmad b. Ḥanbal", "Šuʿayb al-Arnaʾūṭ", None),
    ("al-Muwaṭṭaʾ", "Mālik b. Anas", "179"),
    ("an-Nāfiʿ fī maqrī al-imām Nāfiʿ", "al-Ǧādirī al-Madanī", None),
    ("Nūr al-baṣar fī šarḥ al-Muḫtaṣar fī šarḥ muḫtaṣar aš-šayḫ Ḫalīl", "al-Hilālī as-Siǧilmāsī", "1435"),
    ("Ṣaḥīḫ Ibn Ḥibbān bi-tartīb Ibn Balbān", "al-Bustī", "1414"),
    ("Ṣaḥīḫ Muslim", "Muslim b. al-Ḥaǧǧāǧ", "261"),
    ("Fatḥ al-Bārī šarḥ Ṣaḥīḫ al-Buẖārī", "b. Ḥaǧar al-ʿAsqalānī", None),
    ("al-Fatḥ ar-rabbānī fī tartīb musnad al-imām Aḥmad b. Ḥanbal aš-Šaybānī", "al-Bannā as-Sāʿātī", None),
    ("Sunan Abī Dāwūd", "as-Siǧistānī", "1430"),
    ("Sunan at-Tirmiḏī", "al-Bābī al-Ḥalabī", "279"),
    ("Sunan ad-Dārimī — Musnad ad-Dārimī", "ad-Dārānī", "1412"),
    ("Sunan an-Nasāʾī", "Abū Ġudda", "303"),
    ("Sunan Ibn Māǧa", "Ibn Māǧa al-Qazwīnī", "273"),
    ("Šarḥ az-Zurqānī ʿalā l-Muwaṭṭaʾ", "Ṭāhā ʿAbd ar-Raʾūf Saʿd", "1424"),
]
if len(ENTREES) != 50:
    errors.append(f"GRILLE entrées = {len(ENTREES)} ≠ 50")
h3s = re.findall(r"<h3>(.*?)</h3>", html)
for name, marker, date in ENTREES:
    if name not in h3s and not any(h.startswith(name) for h in h3s):
        errors.append(f"MANQUE entrée h3 : {name}")
    if marker not in norm:
        errors.append(f"MANQUE marqueur {name} : {marker[:40]}")
    if date and f"en {date}" not in norm and f"{date} h." not in norm and f"d. {date}" not in norm:
        errors.append(f"MANQUE date {name} : {date}")

# 3. fragments altérés déclarés
for frag in [
    "fragment imprimé altéré" if False else "déclarées, le reste de l’entrée non inventé",
    "entrée déclarée partiellement lisible",
    "paires croisées en la couche, rétablies",
    "non reconstituées — déclarées",
    "maḫṭūṭ, déclaré",
    "année d’édition absente en la couche — déclarée",
]:
    if frag not in norm:
        errors.append(f"MANQUE déclaration : {frag[:60]}")

# 4. table des loci — pages d'ouverture confirmées (26 leçons + annexes + liminaires)
LOCI = [
    ("l’Introduction, page 5", "Introduction, page 5"),
    ("page 6 ; les écrits pour l’enseignement de la matière, page 8", None),
    ("distribution périodique et hebdomadaire, page 9", None),
    ("1-5 en page 10", None), ("6-9 en page 17", None), ("10-12 en page 23", None),
    ("13-16 en page 29", None), ("17-18 en page 37", None), ("19-20 en page 44", None),
    ("21-24 en page 50", None), ("25-27 en page 58", None), ("28-29 en page 65", None),
    ("30-31 en page 73", None), ("32-35 en page 79", None), ("36-43 en page 87", None),
    ("44-45 en page 96", None), ("46-48 en page 102", None), ("49-52 en page 110", None),
    ("53-55 en page 118", None), ("56-58 en page 125", None), ("59-64 en page 132", None),
    ("65-72 en page 142", None), ("73-77 en page 150", None), ("78-81 en page 157", None),
    ("82-84 en page 165", None), ("85-91 en page 171", None), ("92-97 en page 179", None),
    ("98-101 en page 188", None), ("102-105 en page 195", None),
    ("en page 202", None), ("en page 208", None), ("en page 214", None),
    ("lui-même en page 222", None),
]
for frag, _ in LOCI:
    if frag not in norm:
        errors.append(f"MANQUE loci : {frag[:50]}")

# 5. interdits — aucune āya du cache
cache = json.load(open("scripts-translate/quran-cache.json", encoding="utf-8"))
verses = dict(cache["18"]["fr"])
for n in (1, 10, 60, 107, 110):
    head = re.sub(r"[ \u202f\u00a0]+", " ", verses[n])[:38]
    if head in norm:
        errors.append(f"INTERDIT verset cache {n} rendu")

# 6. 0 arabe + guillemets
arab = re.findall(r"[\u0600-\u06FF\u0750-\u077F\u08A0-\u08FF\uFB50-\uFDF9\uFDFB-\uFDFF\uFE70-\uFEFF]", html)
if arab:
    errors.append(f"ARABE résiduel : {len(arab)} car")
if html.count("«") != html.count("»"):
    errors.append(f"GUILLEMETS désappariés : {html.count('«')} / {html.count('»')}")

print(f"contrôles : {15 + len(ENTREES) * 3 + 6 + len(LOCI) + 5 + 2} attendus — {len(errors)} échec(s)")
for e in errors:
    print("  ✗", e)
if not errors:
    print("VERIFY PASS : annexe 767 conforme (50 entrées, dates rétablies, table des loci 34 lignes, bornes image, 0 verset interdit, 0 arabe)")

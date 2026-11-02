#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Minhāj — contrôle de contenu de l'annexe 766 (tafsir-5ep, fihris al-aʿlām —
index des personnages cités, p.208-213 du manuel miroir tafsir-3-thanawi).
Annexe SANS versets : aucune āya du cache ne doit paraître. Contrôles : les
36 notices biographiques (noms + kunyas), les dates rétablies par le
renversement documenté (Ibn Muǧāhid 245/324, Ibn ʿArabī 468/543, Abū Ḥayyān
745, al-Ālūsī 1217/1270, aš-Šāṭibī 590, as-Suyūṭī 911, an-Naḥḥās 338,
al-Wāḥidī 468...), les fragments altérés déclarés, 0 arabe, guillemets."""
import json
import re

HTML = "tr-tmp/lesson-766-fr.html"
html = open(HTML, encoding="utf-8").read()
norm = re.sub(r"[ \u202f\u00a0]+", " ", html.replace("&nbsp;", "\u00a0"))
errors = []

# 1. structure
for frag in [
    "Source du cours",
    "Deuxième annexe de clôture du second livre du parcours",
    "pages 208 à 213 de l’imprimé miroir",
    "pdf-mut23h3c-766",
    "BORNE TRANCHÉE PAR IMAGE",
    "MÉCANIQUE DES COTES",
    "renversement documenté et PROUVÉ PAR CONVERGENCE",
    "L’objet de l’index",
    "Les notices biographiques",
    "Les subtilités de l’index",
    "La fermeture du livre",
    "convergence badge image + contenu + grille portail, jamais devinée",
    "trente-six notices",
    "« Index des figures citées »",
]:
    if frag not in norm:
        errors.append(f"MANQUE structure : {frag[:60]}")

# 2. les 36 notices (h3 + élément distinctif de chacune)
NOTICES = [
    ("Ibn Abī as-Suʿūd", "šayḫ al-Islām et muftī de l’État ottoman", "982"),
    ("Ibn Barrī", "ad-Durar al-lawāmiʿ fī maqrī imām Nāfiʿ", None),
    ("Ibn al-Ǧawzī", "le ḥanbalite de Bagdad", "510"),
    ("Ibn Muǧāhid", "le premier qui fixa les Sept", "324"),
    ("Ibn ʿAbd al-Barr", "at-Tamhīd et al-Istiḏkār", "463"),
    ("Ibn ʿAbd al-Ḥakam", "l’affranchi de ʿUṯmān b. ʿAffān", None),
    ("Ibn ʿArabī le cadi", "al-Bāqillānī et al-Ġazālī", "543"),
    ("Ibn ʿAṭiyya", "al-Muḥarrar al-waǧīz", "542"),
    ("Ibn al-Qāsim", "l’auteur de la Mudawwana", None),
    ("Ibn aṣ-Ṣalt", "du vizir Ibn Muqla", "328"),
    ("Abū Ḥātim", "imām de la ville de la Baṣora", "255"),
    ("Abū Ḥayyān", "al-Baḥr al-Muḥīṭ", "745"),
    ("Abū Naṣr al-Qušayrī", "l’imām al-Ḥaramayn al-Ǧuwaynī", "514"),
    ("Abū ʿUbayd", "al-Qāsim b. Sallām", "224"),
    ("Abū ʿUbayda", "Maǧāz al-Qurʾān", None),
    ("Abū ʿAlī al-Fārisī", "al-Īḍāḥ", None),  # date en cote déclarée (croisée)
    ("al-Aḫfaš al-Awsaṭ", "il prit la grammaire de Sībawayh", None),
    ("al-Ālūsī", "Rūḥ al-maʿānī", "1217"),
    ("Ašhab", "la direction des Mālikites d’Égypte", "204"),
    ("aṯ-Ṯaʿlab", "l’imām des Kufites en grammaire", None),
    ("al-Ǧawharī", "aṣ-Ṣiḥāḥ", "393"),
    ("Ḥaǧǧāǧ", "de Tirmiḏ", None),
    ("ad-Dārimī", "Sunan ad-Dārimī", "255"),
    ("az-Zaǧǧāǧ", "il taillait le verre", "311"),
    ("al-Māwardī", "le plus grand juge de la fin de l’État ʿabbāside", "450"),
    ("Makkī", "Cordoue", "437"),
    ("al-Mahdawī", "al-Hidāya ilā maḏāhib al-qurrāʾ as-sabʿa", "440"),
    ("an-Naḥḥās", "Maʿānī al-Qurʾān", "338"),
    ("aṣ-Ṣāwī", "ḥāšiyat aṣ-Ṣāwī", "1241"),
    ("al-Farrāʾ", "l’école kufite", "207"),
    ("al-Qaffāl", "al-Qaffāl aš-Šāšī le Grand", "336"),
    ("as-Suhaylī", "de Málaga", "581"),
    ("as-Suyūṭī", "al-Itqān fī ʿulūm al-Qurʾān", "911"),
    ("aš-Šāṭibī", "Ḥirz al-amānī", "590"),
    ("Hārūn b. Mūsā", "al-Buẖārī et Muslim rapportèrent de lui", None),
    ("al-Wāḥidī", "Asbāb an-nuzūl", "468"),
]
if len(NOTICES) != 36:
    errors.append(f"GRILLE notices = {len(NOTICES)} ≠ 36")
h3s = re.findall(r"<h3>(.*?)</h3>", html)
for name, marker, date in NOTICES:
    if name not in h3s:
        errors.append(f"MANQUE notice h3 : {name}")
    if marker not in norm:
        errors.append(f"MANQUE marqueur {name} : {marker[:40]}")
    if date and f"an {date}" not in norm and f"en {date}" not in norm:
        errors.append(f"MANQUE date {name} : {date}")

# 3. fragments altérés déclarés
for frag in ["fragment imprimé altéré, déclaré", "cotes renversées rétablies"]:
    if frag not in norm:
        errors.append(f"MANQUE déclaration : {frag}")

# 4. interdits — aucune āya du cache
cache = json.load(open("scripts-translate/quran-cache.json", encoding="utf-8"))
verses = dict(cache["18"]["fr"])
for n in (1, 10, 60, 107, 110):
    head = re.sub(r"[ \u202f\u00a0]+", " ", verses[n])[:38]
    if head in norm:
        errors.append(f"INTERDIT verset cache {n} rendu")

# 5. 0 arabe + guillemets
arab = re.findall(r"[\u0600-\u06FF\u0750-\u077F\u08A0-\u08FF\uFB50-\uFDF9\uFDFB-\uFDFF\uFE70-\uFEFF]", html)
if arab:
    errors.append(f"ARABE résiduel : {len(arab)} car")
if html.count("«") != html.count("»"):
    errors.append(f"GUILLEMETS désappariés : {html.count('«')} / {html.count('»')}")

print(f"contrôles : {14 + len(NOTICES) * 3 + 2 + 5 + 2} attendus — {len(errors)} échec(s)")
for e in errors:
    print("  ✗", e)
if not errors:
    print("VERIFY PASS : annexe 766 conforme (36 notices, dates rétablies, bornes image, 0 verset interdit, 0 arabe)")

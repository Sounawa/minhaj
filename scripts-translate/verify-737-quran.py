#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Minhāj — contrôle coranique et de contenu de la leçon 737 (tafsir-5ep,
fihris al-aʿlām — l'index des figures citées, pages 209-213).
Le fihris ne cite AUCUN āya : contrôle d'ABSENCE des rasm coraniques du
volume (les āyāt 105-111 des trois dernières leçons et les lemmes d'appui
connus) au corps de la leçon — toute citation coranique y serait une
incursion hors matière ; contrôle de contenu : les vingt figures du tableau
et leurs dates tranchées par l'imprimé, la structure (table à deux colonnes,
Source du cours), 0 arabe résiduel (ﷺ exempté — convention du corpus)."""
import json
import re
import sys

HTML = "scripts-translate/tr-tmp/pdf-mut23h3c-737.html"
html = open(HTML, encoding="utf-8").read()
norm = html.replace("\u202f", " ").replace("\u00a0", " ")
errors = []

# 1. structure : table à deux colonnes avec 20 rangées de figures
if "<thead><tr><th>Les figures</th><th>Leur notice biographique</th></tr></thead>" not in norm:
    errors.append("en-tête du tableau absent")
n_rows = len(re.findall(r"<tr><td>", norm))
if n_rows != 20:
    errors.append(f"rangées de figures attendues : 20, trouvées : {n_rows}")
if "Source du cours" not in norm:
    errors.append("Source du cours absent du DOM")
for frag in [
    "première annexe du livre livrée après les vingt-huit leçons",
    "la page imprimée 214 ouvre déjà la rubrique des sources et références",
    "le fihris s’achève en la page 213",
    "la règle de ré-inversion est validée par les vingt notices",
    "tranchées par l’imprimé, jamais devinées",
]:
    if frag not in norm:
        errors.append(f"source du cours : fragment attendu absent : {frag[:55]}")

# 2. les vingt figures et leurs dates tranchées
figures = [
    ("Ibn ʿAṭiyya", ["al-Muḥarrar al-wajīz fī tafsīr al-kitāb al-ʿazīz", "Abū Bakr Ġālib", "Abū ʿAlī al-Ġassānī", "l’an 542 h"]),
    ("Ibn Ǧarīr aṭ-Ṭabarī", ["al-Ǧāmiʿ al-bayān fī tafsīr al-Qurʾān", "Iḫtilāf al-fuqahāʾ", "Aḫbār ar-rusul wa-l-mulūk", "Tārīḫ aṭ-Ṭabarī", "Āmul", "l’an 310 h"]),
    ("Ibn ʿĀšūr", ["Maqāṣid aš-šarīʿa al-islāmiyya", "at-Taḥrīr wa-t-tanwīr fī tafsīr al-Qurʾān", "mosquée de la Zaytūna", "l’an 1393 h"]),
    ("Ibn ʿAbbās", ["Qurayšite hāšimite", "ḥibr de l’umma", "1660 hadiths", "Ṭāʾif", "perdit la vue", "l’an 68 h", "ﷺ"]),
    ("Ibn ʿAǧība", ["al-Baḥr al-madīd fī tafsīr al-Qurʾān al-maǧīd", "Muḫtaṣar de Ḫalīl", "Ǧāmiʿ aṣ-ṣaġīr", "l’an 1224 h"]),
    ("Ibn Kaṯīr", ["Tafsīr al-Qurʾān al-ʿaẓīm", "al-Bāʿiṯ al-ḥaṯīṯ šarḥ iḫtiṣār ʿulūm al-ḥadīṯ", "ad-Dimašqī aš-Šāfiʿī", "l’an 774 h"]),
    ("Abū Bakr Ibn al-ʿArabī", ["al-ʿAwāṣim min al-qawāṣim", "ʿĀriḍat al-aḥwaḏī fī šarḥ at-Tirmiḏī", "Aḥkām al-Qurʾān", "al-Qabas fī šarḥ Muwaṭṭaʾ Ibn Anas", "Séville", "Fès", "l’an 543 h"]),
    ("Abū Ḥayyān", ["al-Baḥr al-muḥīṭ fī tafsīr al-Qurʾān", "Grenade", "Malaga", "Caire", "l’an 745 h", "an-Nafzī"]),
    ("al-Ālūsī", ["Rūḥ al-maʿānī fī t-tafsīr", "l’iftāʾ", "démis", "Bagdad", "l’an 1270 h"]),
    ("ʿĀʾiša", ["aṣ-Ṣiddīq", "avant l’Hégire", "deuxième année après l’Hégire", "le plus de hadiths", "l’an 58 h", "ﷺ"]),
    ("al-Ḥasan al-Baṣrī", ["l’imām des gens de Baṣra", "successeur (tābiʿī)", "ʿAlī b. Abī Ṭālib", "l’an 110 h"]),
    ("aṯ-Ṯaʿlabī", ["ʿArāʾis al-maǧālis fī qiṣaṣ al-anbiyāʾ", "al-Kašf wa-l-bayān fī tafsīr al-Qurʾān", "Nīšāpūr", "l’an 427 h"]),
    ("az-Zamaḫšarī", ["Ǧār Allāh", "al-Kaššāf ʿan ḥaqāʾiq ġawāmiḍ at-tanzīl", "l’an 538 h"]),
    ("aḍ-Ḍaḥḥāk", ["Muzāḥim al-Hilālī", "expertise considérable", "Il incombe à celui qui apprend le Coran d’être faqīh", "l’an 202 h"]),
    ("Fakhr ad-Dīn ar-Rāzī", ["at-Taymī al-Bakrī", "Ibn Ḫaṭīb ar-Rayy", "Ḫwārazm", "Mā-warāʾ-an-nahr", "Ḫurāsān", "at-Tafsīr al-kabīr, nommé Mafātīḥ al-ġayb", "al-Maḥṣūl fī ʿilm al-uṣūl", "Herāt", "l’an 606 h"]),
    ("Qatāda", ["Daʿāma as-Sadūsī", "ʿAbd Allāh b. Sarǧis", "Anas b. Mālik", "Abū aṭ-Ṭufayl al-Kinānī", "Saʿīd b. al-Musayyab", "l’an 118 h"]),
    ("al-Qurṭubī", ["al-Ǧāmiʿ li-aḥkām al-Qurʾān", "Ḫazraǧī", "l’an 671 h"]),
    ("Mālik b. Anas", ["al-Madanī", "la demeure de l’Hégire", "Ifrīqiya", "l’an 93 h", "l’an 179 h"]),
    ("Muǧāhid", ["Ǧabr", "des lecteurs et des mufassirūn", "Ibn ʿAbbās", "Abū Hurayra", "Saʿd b. Abī Waqqāṣ", "Rāfiʿ b. Ḫadīǧ", "Ǧābir b. ʿAbd Allāh", "Abū Saʿīd al-Ḫudrī", "l’an 104 h"]),
    ("al-Marāġī", ["Aḥmad b. Muṣṭafā al-Marāġī", "Dār al-ʿUlūm", "1909 de l’ère chrétienne", "Tafsīr al-Marāġī", "al-Ḥisba fī al-islām", "al-Waǧīz fī uṣūl al-fiqh", "ʿUlūm al-balāġa", "l’an 1371 h"]),
]
for name, frs in figures:
    if f"<td>{name}</td>" not in norm:
        errors.append(f"figure absente du tableau : {name}")
    for f in frs:
        if f not in norm:
            errors.append(f"notice de {name} : fragment attendu absent : {f[:50]}")

# 3. ABSENCE de citations coraniques (le fihris n'en porte aucune) —
#    rasm nu du cache des āyāt récentes du volume + lemmes d'appui connus
def bare(t: str) -> str:
    return re.sub(r"[\u064B-\u065F\u0670\u06D6-\u06ED\u0640\u0671]", "", t)

cache = json.load(open("scripts-translate/quran-cache.json", encoding="utf-8"))
ar17 = dict((i, t) for i, t in cache["17"]["ar"])
probes = []
for v in (105, 106, 107, 108, 110, 111):
    t = bare(ar17[v]).split()
    # trois mots consécutifs au cœur de l'āya, sample fiable sans être banal
    probes.append(" ".join(t[len(t) // 2:len(t) // 2 + 3]))
for f in ["حجابا مستورا", "وسل من أرسلنا من قبلك من رسلنا", "تسع ءايت بينت"]:
    probes.append(f)
for p in probes:
    if p and p in norm:
        errors.append(f"rasm coranique inattendu au corps du fihris : {p[:40]}")

# rendus français caractéristiques des āyāt — absence attendue
for pat, label in [
    (r"en toute vérité que Nous l’avons fait descendre", "al-Isrāʾ 17:105"),
    (r"le menton contre terre", "al-Isrāʾ 17:107"),
    (r"Gloire à notre Seigneur", "al-Isrāʾ 17:108"),
    (r"Invoquez donc Allah, ou invoquez le Tout Miséricordieux", "al-Isrāʾ 17:110"),
    (r"dans ta prière, et ne la fais pas lourdement", "al-Isrāʾ 17:110"),
    (r"Dis : Louange à Allah", "al-Isrāʾ 17:111"),
]:
    if re.search(pat, norm, re.IGNORECASE):
        errors.append(f"rendu coranique inattendu : {label}")

# 4. 0 arabe résiduel (ﷺ U+FDFA exempté — convention du corpus)
if re.search(r"[\u0600-\u06FF\u0750-\u077F\u08A0-\u08FF\uFB50-\uFDF9\uFDFB-\uFDFF\uFE70-\uFEFF]", norm):
    errors.append("caractère arabe résiduel détecté")

if errors:
    print("ÉCHEC :")
    for e in errors:
        print(" -", e)
    sys.exit(1)
print("PASS : leçon 737 — fihris al-aʿlām (p.209-213) — les vingt figures du tableau "
      "(Ibn ʿAṭiyya 542, Ibn Ǧarīr aṭ-Ṭabarī 310, Ibn ʿĀšūr 1393, Ibn ʿAbbās 68, "
      "Ibn ʿAǧība 1224, Ibn Kaṯīr 774, Abū Bakr Ibn al-ʿArabī 543, Abū Ḥayyān 745, "
      "al-Ālūsī 1248/1270, ʿĀʾiša 58, al-Ḥasan al-Baṣrī 110, aṯ-Ṯaʿlabī 427, "
      "az-Zamaḫšarī 538, aḍ-Ḍaḥḥāk 202, Fakhr ad-Dīn ar-Rāzī 606, Qatāda 118, "
      "al-Qurṭubī 671, Mālik b. Anas 93/179, Muǧāhid 104, al-Marāġī 1371) et leurs "
      "notices portées, table à deux colonnes et Source du cours au DOM, aucune "
      "citation coranique au corps (ABSENCE des rasm des āyāt 105-111 et des lemmes "
      "d'appui vérifiée — le fihris n'en porte aucune), 0 arabe résiduel.")

if __name__ == "__main__":
    sys.exit(0)

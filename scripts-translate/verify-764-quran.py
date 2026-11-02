#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Minhāj — contrôle coranique et de contenu de la leçon 764 (tafsir-5ep,
sūrat al-Kahf v102-105 de l'imprimé warš — vingt-sixième et dernière leçon de
la section tafsīr du second livre, pages 195-201 du manuel miroir
tafsir-3-thanawi). Décalage imprimé→cache de un des leçons 12 à 23 (R511),
de deux dans la zone de la leçon 24 (R523), de quatre en la leçon 25 (R526),
puis de CINQ en cette zone (tranché sur le contenu : la boîte de p.195, relue
sur le rendu image de la passe R527, porte (102) = cache 107 « إن الذين
آمنوا... », (103) = cache 108, (104) = cache 109, (105) = cache 110). Les
quatre āyāt sont rendues du cache (présence vérifiée) ; les āyāt 1-106
(leçons 739-763 — la cache 106 réunie par le fendo warš au numéro imprimé
(101) de la leçon 25, ses gloses livrées) sont interdites de double rendu ;
le rasm nu du cache interdit au corps (0 arabe — FR-seule)."""
import json
import re

HTML = "tr-tmp/lesson-764-fr.html"
html = open(HTML, encoding="utf-8").read()
norm = re.sub(r"[ \u202f\u00a0]+", " ", html.replace("&nbsp;", "\u00a0"))
errors = []

# 1. structure et marqueurs
for frag in [
    "Source du cours",
    "Vingt-sixième et dernière leçon de la section tafsīr du second livre du parcours",
    "pages 195 à 201 de l’imprimé miroir",
    "1_20220304_20220304_2251",
    "l’ʾiʿdād qiblī de p.194 porte la révision de l’exégèse des āyāt de la leçon au NUM relu sur image",
    "p.195 ouvre la leçon 26 au badge relu sur rendu image",
    "le badge relu résout le NB laissé par R523",
    "la grille « v102-105 » CONFIRMÉE PAR SONDAGE",
    "convergence quadruple",
    "TRANCHAGE DU DÉCALAGE PAR LE CONTENU",
    "la leçon 26 rend les āyāt 107 à 110 du cache aux numéros imprimés (102)-(105)",
    "fendo de la numérotation warš déclaré",
    "l’annexe des activités ouvre en la page 202",
    "STARTS +202 tranché par la passe R527",
    "Les objectifs de la leçon",
    "Le tamhīd",
    "Le commentaire",
    "La glose",
    "L’extraction des thèmes des āyāt",
    "Premièrement",
    "Deuxièmement",
    "Troisièmement",
    "Quatrièmement",
    "L’évaluation",
    "L’exploitation",
    "la page imprimée 201",
    "jamais devinée",
    "interdites de double rendu",
    "passe de quatre (leçon 25, médaillon (98) = cache 102, tranché R526) à cinq",
    "l’āya 106 du cache",
    "les Jardins du Firdaws",
    "la parabole de la mer encre",
]:
    if frag.lower() not in norm.lower():
        errors.append(f"fragment attendu absent : {frag[:55]}")

# 2. les āyāt 107-110 rendus du cache — présence (4 rendus + numéros imprimés 102-105)
cache = json.load(open("scripts-translate/quran-cache.json", encoding="utf-8"))
fr18 = {n: t for n, t in cache["18"]["fr"]}
rendus = [fr18[n] for n in (107, 108, 109, 110)]
rendus_norm = [r.replace("'", "’").replace(" ", "") for r in rendus]
compact = norm.replace(" ", "")
for r in rendus_norm:
    if r not in compact:
        errors.append(f"rendu coranique attendu absent : {r[:55]}")
for num in ("(102)", "(103)", "(104)", "(105)"):
    if num not in norm:
        errors.append(f"numéro imprimé absent : {num}")

# 3. interdits de double rendu (leçons 739-763)
interdits = [
    (fr18[99].replace("'", "’"), 99),
    (fr18[102].replace("'", "’"), 102),
    (fr18[105].replace("'", "’"), 105),
    (fr18[106].replace("'", "’"), 106),
    (fr18[111] if 111 in fr18 else "AAAA", 111),
]
for interdit, n in interdits:
    if interdit and interdit.replace(" ", "") in compact:
        errors.append(f"āya interdite de double rendu présente (cache {n})")

# 4. contenu attendu (confrontation au manuel — glose, hadiths, exégètes)
contenu = [
    "le centre du Paradis, son sommet et son meilleur",
    "il croit et se persuade",
    "les dernières āyāt de sūrat al-Kahf gardent de l’Antéchrist",
    "Sunan d’Abū Dāwūd",
    "quiconque mémorise dix āyāt des conclusions de sūrat al-Kahf",
    "la tentation de l’Antéchrist",
    "l’āya du Trône",
    "les répétées",
    "al-Ḥiǧr : 87",
    "Al-Ṭabarī",
    "la plus grande part du Paradis",
    "al-Ǧāmiʿ li-aḥkām al-Qurʾān : 61/73",
    "Anas b. Mālik",
    "Sunan al-Tirmiḏī",
    "cent degrés",
    "ceux qui combattent en Son chemin",
    "le Trône du Miséricordieux",
    "de lui jaillissent les fleuves du Paradis",
    "Ṣaḥīḥ al-Buẖārī : kitāb al-tawḥīd",
    "Abū Mūsā al-Ašʿarī",
    "le vêtement de majesté sur Son visage",
    "al-Fatḥ al-Rabbānī",
    "d’après Kaʿb",
    "plus cher que le jardin du Firdaws",
    "ceux qui ordonnent le convenable et interdisent le blâmable",
    "en roman",
    "al-Farrāʾ a dit : il est arabe",
    "firadīs",
    "ne désirant point de changement",
    "Abū Ḥayyān",
    "al-Baḥr al-Muḥīṭ : 8/232",
    "l’eau de la mer serait l’encrier, et la mer l’encre",
    "Luqmān : 27",
    "les savoirs d’Allah",
    "point de borne",
    "la réponse aux contradicteurs de Son prophète",
    "Ibn ʿĀmir, Ḥamza et al-Kisāʾī lurent la lexie à la yāʾ",
    "Ibn Masʿūd, d’Ibn ʿAbbās, de Muǧāhid, d’al-Aʿmaš",
    "« une encre »",
    "avec le kasr du mīm",
    "la réalité de l’esprit",
    "l’unicité d’Allah et l’œuvre salutaire",
    "la remontrance générale de la création",
    "Ǧundub b. Zuhayr al-ʿĀmirī",
    "Allah n’agréé que ce qui Lui fut pur",
    "al-Ǧāmiʿ li-aḥkām al-Qurʾān : 11/96",
    "aspire à une belle rencontre de son Seigneur",
    "il craint la mauvaise rencontre de son Seigneur",
    "Al-Māwardī",
    "Muqātil et Quṭrub",
    "al-Kalbī",
    "Saʿīd b. Ǧubayr",
    "al-Nukat wa-l-ʿUyūn : 3/350",
    "les deux piliers de l’œuvre agréée",
    "sincérité de l’intention envers Allah",
    "sincérité du suivi du Messager d’Allah",
    "Sufyān al-Ṯawrī",
    "qu’il ne fasse point œuvrer pour être vu",
    "Ṭāwūs b. Kaysān",
    "al-Ḥākim rapporte, en son Mustadrak",
    "jusqu’à ce que descendît",
    "une figure de même étymon",
    "que les énoncés n’encerclent point",
    "purifier son âme",
    "l’association manifeste",
    "l’association cachée",
    "l’association mineure",
    "le fait de montrer",
    "Musnad al-Imām Aḥmad",
    "Les conditions de l’agréation de l’œuvre auprès d’Allah Très-Haut",
    "je revois mes leçons précédentes",
    "activités de consolidation et de soutien",
    "la leçon s’achève en la page imprimée 201",
    "dernière leçon de la section tafsīr du second livre",
    "cent dix āyāt du cache rendues en vingt-six leçons",
]
for c in contenu:
    if c.lower() not in norm.lower():
        errors.append(f"contenu attendu absent : {c[:60]}")

# 5. 0 arabe au corps
arabe = re.findall(r"[\u0600-\u06FF\u0750-\u077F]", norm)
arabe = [a for a in arabe if a not in "\u061f"]
if arabe:
    errors.append(f"caractères arabes au corps : {len(arabe)} (0 attendu)")

if errors:
    print("VERIFY ÉCHEC —", len(errors), "problème(s) :")
    for e in errors:
        print("  -", e)
    raise SystemExit(1)
print("VERIFY PASS — leçon 764 : 4 rendus cache 107-110 présents, numéros imprimés (102)-(105),",
      "interdits absents (cache 99, 102, 105, 106),", len(contenu), "contrôles de contenu, 0 arabe au corps.")

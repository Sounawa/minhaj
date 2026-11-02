#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Minhāj — contrôle coranique et de contenu de la leçon 763 (tafsir-5ep,
sūrat al-Kahf v98-101 de l'imprimé warš — vingt-cinquième leçon du second
livre, pages 188-194 du manuel miroir tafsir-3-thanawi). La plage imprimée
(98-101) correspond aux āyāt 102-105 du cache canonique ḥafṣ (décalage de
quatre, tranché R526 : médaillon (98) relu sur crops 300/500 dpi ouvrant sur
« a-fa-ḥasiba lladhīna kafarū … innā aʿtadnā » ; cache 100-101 réunies par le
fendo warš sous le (97) de la leçon 24). Les quatre āyāt sont rendues du cache
(présence vérifiée) ; la cache 99 (leçon 762) et la cache 106-107 (leçon 26,
spillover déclaré) sont interdites de double rendu ; le rasm nu du cache
interdit au corps (0 arabe — FR-seule)."""
import json
import re

HTML = "tr-tmp/lesson-763-fr.html"
html = open(HTML, encoding="utf-8").read()
norm = re.sub(r"[ \u202f\u00a0]+", " ", html.replace("&nbsp;", "\u00a0"))
errors = []

# 1. structure et marqueurs
for frag in [
    "Source du cours",
    "Vingt-cinquième leçon du second livre du parcours",
    "pages 188 à 194 de l’imprimé miroir",
    "1_20220304_20220304_2251",
    "sonde kahf-probe-l25.py de R526",
    "sūrat al-Kahf (al-āyāt : 98-101)",
    "la plage imprimée (98-101) correspond aux āyāt 102 à 105 du cache canonique",
    "décalage de quatre",
    "fendo warš déclaré",
    "SPILLOVER DÉCLARÉ",
    "réservée à la leçon 26",
    "interdites de double rendu",
    "jamais devinée",
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
    "la page imprimée 194",
    "la leçon suivante ouvre en la page 195",
]:
    if frag.lower() not in norm.lower():
        errors.append(f"fragment attendu absent : {frag[:55]}")

# 2. les āyāt 102-105 rendus du cache — présence (4 rendus + numéros imprimés 98-101)
cache = json.load(open("scripts-translate/quran-cache.json", encoding="utf-8"))
fr18 = {n: t for n, t in cache["18"]["fr"]}
rendus = [fr18[n] for n in (102, 103, 104, 105)]
rendus_norm = [r.replace("'", "’").replace(" ", "") for r in rendus]
compact = norm.replace(" ", "")
for r in rendus_norm:
    if r not in compact:
        errors.append(f"rendu coranique attendu absent : {r[:55]}")
for num in ("(98)", "(99)", "(100)", "(101)"):
    if num not in norm:
        errors.append(f"numéro imprimé absent : {num}")

# 3. interdits de double rendu (leçon 762 : cache 99 ; leçon 26 : cache 106-107)
for interdit, n in [("Nous les laisserons, ce jour-là, déferler comme les flots", 99),
                    ("C'est que leur rétribution sera l'Enfer, pour avoir mécru et pris en raillerie", 106),
                    ("Ceux qui croient et font de bonnes œuvres auront pour résidence les Jardins", 107)]:
    if interdit.replace("'", "’").replace(" ", "") in compact:
        errors.append(f"āya interdite de double rendu présente (cache {n})")

# 4. contenu attendu (confrontation au manuel — glose, lectures, exégètes)
contenu = [
    "l’histoire de Dū l-Qarnayn et ce qu’elle contient de merveilles",
    "ceux qui échangèrent la loyauté envers Dieu et Ses messagers",
    "les plus grands perdants en leurs œuvres",
    "se moquent du Livre de Dieu",
    "Nous disposâmes et Nous apprêtâmes",
    "la valeur, la rétribution et la récompense",
    "Quelle est la destinée de la mécréance et de l’association",
    "interrogation de dénégation et de reproche",
    "le blâme des idolâtres en leurs croyances vaines",
    "offrandes votives et les sacrifices",
    "au kasr du sīn, au sens de : supputer",
    "Ibn Kaṯīr et Yaʿqūb",
    "af-ḥasub",
    "a-fa-ẓanna lladhīna kafarū",
    "lecture dérogatoire (šāḏḏa)",
    "Abū Ḥayyān",
    "qu’il y a en la phrase une élision",
    "la réponse à l’interrogation",
    "le repas d’hospitalité",
    "métaphore ironique (istīʿāra tahakkumiyya)",
    "nom de supériorité (ism tafḍīl)",
    "complément d’espèce (tamyīz)",
    "les œuvres des idolâtres diffèrent en la corruption",
    "Nāfiʿ, Ibn Kaṯīr, Abū ʿAmr et al-Kisāʾī",
    "yaḥsibūna",
    "le fatḥ étant le plus fréquent et le plus conforme à l’analogie",
    "crièrent au mensonge les signes, les messagers et les prophètes",
    "Muǧāhid, d’Ibn Muḥiṣin et de Yaʿqūb",
    "la pesée des œuvres relève des articles de la foi",
    "al-ʾAnbiyāʾ : 47",
    "de poids profitable",
    "nul degré pour eux auprès de Lui",
    "Aṭ-Ṭabarī",
    "les balances ne s’alourdissent que des œuvres salutaires",
    "Jāmiʿ al-Bayān : 16/35",
    "la nullification de leurs œuvres",
    "la moquerie, la dérision, le mépris et la plaisanterie",
    "al-Ǧāṯiya : 8",
    "muḥassināt lafẓiyya",
    "l’aile d’un moustique",
    "Ṣaḥīḥ al-Bukhārī",
    "pièce 2544",
    "l’expédition de Tabūk",
    "at-Tawba : 66",
    "magnifier Sa parole",
    "Ibn al-ʿArabī",
    "l’interprétation corrompue",
    "l’ostentation et dilapidèrent leurs états par l’insouciance",
    "Aḥkām al-Qurʾān : 3/442",
    "ʿĀʾiša",
    "Ibn Ǧudʿān",
    "entretenait les liens de parenté et nourrissait l’indigent",
    "Ṣaḥīḥ Muslim",
    "pièce 214",
    "couche texte miroir « 201-501 »",
    "la clôture de sūrat al-Kahf",
    "convergence quadruple",
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
print("VERIFY PASS — leçon 763 : 4 rendus cache 102-105 présents, numéros imprimés (98)-(101),",
      "interdits absents (cache 99/106/107),", len(contenu), "contrôles de contenu, 0 arabe au corps.")

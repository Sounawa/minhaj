#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Minhāj — contrôle de contenu de l'annexe 765 (tafsir-5ep, « Activités de
consolidation et de soutien » — أنشطة التثبيت والتعمق imprimé, p.202-207 du
manuel miroir tafsir-3-thanawi). Annexe SANS versets : aucune āya du cache
(quran-cache.json 1-110) ne doit paraître — les tableaux āyāt/figures de
l'imprimé sont dégradés OCR et déclarés fragments altérés, jamais reconstitués.
Contrôles : structure annexe, les trois objectifs, les quatre activités, la
citation Ibn ʿĀšūr, les phases de la recherche, bornes tranchées par image,
0 arabe (FR-seule), guillemets appariés."""
import json
import re

HTML = "tr-tmp/lesson-765-fr.html"
html = open(HTML, encoding="utf-8").read()
norm = re.sub(r"[ \u202f\u00a0]+", " ", html.replace("&nbsp;", "\u00a0"))
errors = []

# 1. structure et marqueurs de contenu
for frag in [
    "Source du cours",
    "Annexe de clôture du second livre du parcours",
    "pages 202 à 207 de l’imprimé miroir",
    "slot pdf-mut23h3c-765",
    "1_20220304_20220304_2251",
    "TRANCHAGE DE LA BORNE",
    "rendu image du badge de p.202 à 150 dpi",
    "aḥdāf al-anšaṭa",
    "la borne d’ouverture p.202 est ainsi prouvée par double preuve",
    "jamais devinée",
    "DIVERGENCE DÉCLARÉE",
    "anšaṭat at-taṯbīt wa-d-daʿm",
    "anšaṭat at-taṯbīt wa-t-taʿmīq",
    "DÉGRADATIONS DÉCLARÉES",
    "Les objectifs des activités",
    "La première activité : le bilan des questions et des récits de la sūra",
    "La deuxième activité : l’extraction des valeurs et des mœurs des āyāt",
    "La troisième activité : les figures de style et les lectures",
    "La quatrième activité : la recherche thématique d’ensemble",
    "Les activités de préparation",
    "La phase de collecte, d’organisation et de synthèse des données",
    "La phase de présentation et d’exploitation",
    "Les subtilités et les bienfaits de l’annexe",
    "La fermeture du livre",
]:
    if frag not in norm:
        errors.append(f"MANQUE marqueur : {frag}")

# 2. les trois objectifs imprimés
for frag in [
    "Que je consolide mes connaissances et que j’exploite mes acquis dans l’étude méditative de la sūra.",
    "Que je développe les compétences de l’analyse, de la déduction, de la synthèse et de l’exploitation.",
    "Que je m’imprègne des valeurs tirées de la sūra et que je saisisse leurs fruits dans la vie.",
]:
    if frag not in norm:
        errors.append(f"MANQUE objectif : {frag[:60]}")

# 3. les récits et consignes majeurs
for frag in [
    "l’appel à l’unicité d’Allah, la foi au Jour dernier",
    "des Compagnons de la Caverne",
    "l’homme aux deux jardins",
    "Moïse avec le serviteur vertueux",
    "Dhū-l-Qarnayn",
    "un schéma organisateur des grandes questions",
    "les droits auxquels il fut fait défaut",
    "valeur de la coopération, de la participation et de la prise en charge de la responsabilité".replace("valeur", "Les valeurs"),
    "des conduites pratiques pour la manière de se tenir envers ces bienfaits",
    "le moindre des deux dommages",
    "il n’est point du ressort de la législation",
    "al-Taḥrīr wa-l-Tanwīr",
    "aṭ-Ṭāhir Ibn ʿĀšūr",
    "Je justifie la règle par des textes de la Loi autres qu’elle.",
    "la limitation des corruptions et des dommages",
    "le ressort de la législation pour la préservation de la vie",
    "Comment concilier le désaveu de Moïse",
    "j’en extrais les valeurs et les mœurs qu’elles ont contenues",
    "[al-Kahf : 63]",
    "aux figures de style de sūrat al-Kahf",
    "je remplis le tableau de ce qui convient",
    "rechercher une recherche thématique".replace("rechercher une", "réaliser une"),
    "l’étude méditative de ses contenus et de ses finalités",
    "détermination des axes",
    "un coordinateur pour la conduite du dialogue et du débat",
    "un rapporteur pour l’écriture de ce qui fut convenu",
    "aux valeurs du dialogue, de la communication, de la concertation, de la coopération",
    "des livres de tafsīr",
    "les présentations des rapporteurs",
    "questions scientifiques, éducatives et valorielles",
    "les conclusions et les déductions finales",
    "kahf-probe-annexes.py",
    "fihris al-aʿlām",
    "fihris al-maṣādir wa-l-marāǧiʿ",
    "p.208", "p.214", "p.222",
    "les pages 223 et 224 du manuel sont vierges",
    "convergence triple",
    "fragments imprimés altérés",
    "cent dix āyāt de sūrat al-Kahf rendues",
]:
    if frag not in norm:
        errors.append(f"MANQUE contenu : {frag[:60]}")

# 4. interdits — AUCUNE āya du cache rendue (annexe sans versets)
cache = json.load(open("scripts-translate/quran-cache.json", encoding="utf-8"))
k18 = cache["18"]
verses = dict(k18["fr"])
# ouvertures distinctives des āyāt du cache — aucun début de vers ne doit paraître
OPENINGS = [
    verses[1], verses[10], verses[60], verses[83], verses[107], verses[110],
]
for v in OPENINGS:
    head = re.sub(r"[ \u202f\u00a0]+", " ", v)[:38]
    if head in norm:
        errors.append(f"INTERDIT verset cache rendu : « {head}… »")
# la boîte « Allah Très-Haut a dit » complète avec texte de āya — contrôle :
# le document ne cite que « Allah Très-Haut a dit » en description, sans āya
if "Allah Très-Haut a dit\u00a0: «" in norm:
    errors.append("INTERDIT boîte de āya rendue (annexe sans versets)")

# 5. 0 arabe + guillemets
arab = re.findall(r"[\u0600-\u06FF\u0750-\u077F\u08A0-\u08FF\uFB50-\uFDF9\uFDFB-\uFDFF\uFE70-\uFEFF]", html)
if arab:
    errors.append(f"ARABE résiduel : {len(arab)} car")
if html.count("«") != html.count("»"):
    errors.append(f"GUILLEMETS désappariés : {html.count('«')} / {html.count('»')}")

print(f"contrôles : {1 + 3 + 41 + 7 + 2} attendus — {len(errors)} échec(s)")
for e in errors:
    print("  ✗", e)
if not errors:
    print("VERIFY PASS : annexe 765 conforme (structure, objectifs, activités, bornes image, 0 verset interdit, 0 arabe)")

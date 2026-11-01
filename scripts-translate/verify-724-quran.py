#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Minhāj — contrôle coranique de la leçon 724 (tafsir-5ep, Isrāʾ 61-65).
Vérifie : rendus français des versets 61-65 (rasm warš du cache), les gloses
lexicales (al-ikrām, la-aḥtanikanna, mawfūrā, wa-stafziz, al-ghūr), les noms
portés (aṭ-Ṭabarī, Ibn ʿAbbās, Ibn Zayd, Qatāda, Mujāhid, le hadith de Saʿd),
la préparation 66-69 au DOM, l'absence de citations hors rasm (17:56-60 =
leçon précédente, interdites au corps après l'évaluation), 0 arabe résiduel."""
import json
import re
import sys

HTML = "scripts-translate/tr-tmp/pdf-mut23h3c-724.html"
html = open(HTML, encoding="utf-8").read()
errors = []

for frag in [
    "Prosternez-vous devant Adam",
    "ils se prosternèrent, à l’exception d’Iblīs",
    "Me prosternerai-je devant quelqu’un que Tu as créé d’argile",
    "Celui que Tu as honoré au-dessus de moi",
    "si Tu me donnes du répit jusqu’au Jour de la Résurrection",
    "j’éprouverai, certes, sa descendance, excepté un petit nombre",
    "Va-t’en\u202f: quiconque d’entre eux te suivra",
    "votre sanction sera l’Enfer, une ample rétribution",
    "Excite par ta voix ceux d’entre eux que tu pourras",
    "rassemble contre eux ta cavalerie et ton infanterie",
    "associe-toi à eux dans leurs biens et leurs enfants",
    "fais-leur des promesses",
    "or le diable ne leur fait de promesses qu’en tromperie",
    "tu n’as aucun pouvoir sur eux",
    "et ton Seigneur suffit pour les protéger",
]:
    if frag not in html:
        errors.append(f"rendu attendu absent : {frag[:55]}")

if not re.search(r"»\s*\(61-65\)", html):
    errors.append("repère de plage (61-65) absent")

for frag in [
    "nom collectif de tout ce qui est loué",
    "le taḥnīk de la bête",
    "Aṭ-Ṭabarī a dit\u202f: le sens est «\u202fje les extirperai\u202f»",
    "Ibn ʿAbbās a dit en cela\u202f: «\u202fje m’emparerai d’eux\u202f»",
    "Ibn Zayd a dit\u202f: «\u202fje les égarerai\u202f»",
    "c’est ce qu’a dit Qatāda",
    "c’est ce qu’a dit Mujāhid",
    "Saʿd ibn Abī Waqqāṣ",
    "Sunan at-Tirmiḏī",
    "la première désobéissance à Allah fut commise par l’envie",
]:
    if frag not in html:
        errors.append(f"glose/nom attendu absent : {frag[:55]}")

def bare(t: str) -> str:
    return re.sub(r"[\u064B-\u065F\u0670\u06D6-\u06ED\u0640\u0671]", "", t)

cache = json.load(open("scripts-translate/quran-cache.json", encoding="utf-8"))
ar17 = dict((i, t) for i, t in cache["17"]["ar"])
v61, v62, v63, v64, v65 = (ar17[i] for i in range(61, 66))
b61, b62, b63, b64, b65 = (bare(v) for v in (v61, v62, v63, v64, v65))
for f in ["وإذ قلنا للملئكة سجدوا لءادم فسجدوا إلا إبليس", "ءأسجد لمن خلقت طينا"]:
    if f not in b61:
        errors.append(f"cache 17:61 inattendu ({f[:35]})")
for f in ["أرءيتك هذا لذى كرمت على", "لأحتنكن ذريته إلا قليلا"]:
    if f not in b62:
        errors.append(f"cache 17:62 inattendu ({f[:35]})")
if "ذهب فمن تبعك منهم فإن جهنم جزاؤكم جزاء موفورا" not in b63:
    errors.append("cache 17:63 inattendu")
for f in ["وستفزز من ستطعت منهم بصوتك وأجلب عليهم بخيلك ورجلك",
          "وشاركهم فى لأمول ولأولد وعدهم", "وما يعدهم لشيطن إلا غرورا"]:
    if f not in b64:
        errors.append(f"cache 17:64 inattendu ({f[:35]})")
for f in ["إن عبادى ليس لك عليهم سلطن", "وكفى بربك وكيلا"]:
    if f not in b65:
        errors.append(f"cache 17:65 inattendu ({f[:35]})")

# préparation de la leçon suivante au DOM
if "66 à 69" not in html:
    errors.append("préparation : les versets 66-69 absents du DOM")

# citations hors rasm — interdites au corps après l'évaluation (versets 56-60 : leçon précédente)
body = html.split("<h2>L’évaluation", 1)[1]
for pat, label in [
    (r"Invoquez ceux", "al-Isrāʾ 17:56 (leçon précédente — non portée)"),
    (r"chamelle", "al-Isrāʾ 17:59 (leçon précédente — non portée)"),
    (r"Ṯamūd", "al-Isrāʾ 17:59 (leçon précédente — non portée)"),
    (r"cerne les gens", "al-Isrāʾ 17:60 (leçon précédente — non portée)"),
    (r"arbre maudit", "al-Isrāʾ 17:60 (leçon précédente — non portée)"),
    (r"Pas de cité", "al-Isrāʾ 17:58 (leçon précédente — non portée)"),
    (r"Psaumes", "al-Isrāʾ 17:55 (leçon précédente — non portée)"),
    (r"David", "al-Isrāʾ 17:55 (leçon précédente — non portée)"),
]:
    if re.search(pat, body, re.IGNORECASE):
        errors.append(f"citation inattendue : {label}")

if re.search(r"[\u0600-\u06FF\u0750-\u077F\u08A0-\u08FF\uFB50-\uFDF9\uFDFB-\uFDFF\uFE70-\uFEFF]", html):
    errors.append("caractère arabe résiduel détecté")

if errors:
    print("ÉCHEC :")
    for e in errors:
        print(" -", e)
    sys.exit(1)
print("PASS : leçon 724 — versets 61-65 rendus sur le rasm warš du cache (la prosternation "
      "des anges et le refus d’Iblīs en interrogation de reniement, sa menace contre la "
      "descendance d’Adam excepté un petit nombre, l’Enfer en rétribution ample pour qui le "
      "suit, l’excitation par la voix, la cavalerie et l’infanterie, la société dans les "
      "biens et les enfants, la promesse trompeuse, la limite posée sur Mes serviteurs et le "
      "Seigneur suffisant comme protecteur), les gloses lexicales (al-ikrām nom collectif de "
      "tout ce qui est loué, la-aḥtanikanna du taḥnīk de la bête, mawfūrā ample et complet, "
      "wa-stafziz amène avec mépris et dupe, al-ghūr la chose détestable sous l’image de "
      "l’aimable), les causes de descente (la tyrannie des associateurs portée par "
      "l’insufflation du diable), l’analogie erronée du feu sur l’argile et la première "
      "désobéissance commise par l’envie, les transmissions de la-aḥtanikanna (aṭ-Ṭabarī "
      "extirper, Ibn ʿAbbās s’emparer, Ibn Zayd égarer), l’impératif au sens de la menace, "
      "la voix du diable (Mujāhid, Ibn ʿAbbās), la métaphore du cavalier et les cavaliers et "
      "fantassins (Qatāda, Mujāhid), les biens et les enfants (le fil d’Iblīs, les noms "
      "détestables, le waʾd des Arabes), la limite sur les serviteurs sincères et le hadith "
      "de Saʿd ibn Abī Waqqāṣ (Sunan at-Tirmiḏī), la préparation 66-69 au DOM, aucune "
      "citation hors rasm (17:56-60 interdits au corps après l’évaluation), 0 arabe "
      "résiduel.")

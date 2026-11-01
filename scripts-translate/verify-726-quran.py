#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Minhāj — contrôle coranique de la leçon 726 (tafsir-5ep, Isrāʾ 70-72).
Vérifie : rendus français des versets 70-72 (rasm warš du cache), les gloses
lexicales (bī-imāhihim, fatiilan, aḍall, ar-riqz), les noms portés (Ibn ʿAṭiyya,
at-Ṭabarī, Qurṭubī al-Ǧāmiʿ 10/592, Muǧāhid/Qatāda/Ibn Zayd/Ibn ʿAbbās/al-Ḥasan,
le qāḍī Abū Muḥammad, Ibn Kaṯīr/Ibn ʿĀmir/Ḥamza/al-Kisāʾī/ʿĀṣim/Abū ʿAmr,
Abū ʿAlī, Sībawayhi, Rāzī Mafātīḥ al-ġayb 12/273), le renvoi an-Nisāʾ 40
(« le poids d’un atome ») au rasm nu, le sens obvié (mafhūm al-ḫiṭāb), les
qirāʾāt d’« aʿmā » (ʿahā, imāla), la préparation 73-77 au DOM, l’absence de
citations hors rasm (17:66-69 = leçon précédente, interdites au corps après
l’évaluation), 0 arabe résiduel. Espaces typographiques (NNBSP/insécables)
introduits par l’auto-fix de qa-lesson normalisés avant appariement."""
import json
import re
import sys

HTML = "scripts-translate/tr-tmp/pdf-mut23h3c-726.html"
html = open(HTML, encoding="utf-8").read()
norm = html.replace("\u202f", " ").replace("\u00a0", " ")
errors = []

for frag in [
    "Certes, Nous avons honoré les fils d’Adam",
    "Nous les avons transportés sur terre et sur mer",
    "leur avons attribué de bonnes choses comme nourriture",
    "Nous les avons nettement préférés à plusieurs de Nos créatures",
    "Le jour où Nous appellerons chaque groupement d’hommes par leur chef",
    "ceux à qui on remettra leur livre dans la main droite",
    "liront leur livre (avec plaisir)",
    "ne subiront pas la moindre injustice",
    "Et quiconque aura été aveugle ici-bas",
    "sera aveugle dans l’au-delà",
    "plus égaré [encore] par rapport à la bonne voie",
]:
    if frag not in norm:
        errors.append(f"rendu attendu absent : {frag[:55]}")

if not re.search(r"»\s*\(70-72\)", norm):
    errors.append("repère de plage (70-72) absent")

for frag in [
    "celui qu’ils suivaient et qu’ils prenaient pour guide",
    "tout ce dont le profit est sain",
    "l’enveloppe délicate qui ressemble à un fil au cœur du noyau",
    "d’une perplexité plus intense",
    "le plus proche du châtiment",
    "al-Ǧāmiʿ li-aḥkām al-Qurʾān de Qurṭubī",
    "tome 10/592",
    "le châtiment (al-ǧazāʾ), la garde (al-ḥifẓ), la discrimination (at-tamyīz)",
    "l’atteinte de la furūsa",
    "le nombreux méprisé",
    "la viande crue",
    "at-Ṭabarī a rapporté d’un groupe",
    "la course du cheval",
    "la force de l’éléphant",
    "le courage du lion",
    "la noblesse du coq",
    "la préférence des anges",
    "Muǧāhid et Qatāda ont dit",
    "Ibn Zayd a dit",
    "Ibn ʿAbbās et al-Ḥasan ont dit",
    "l’imam est ce par quoi on est dirigé et guidé vers le but",
    "ils le répètent et le méditent",
    "le fil qui est dans la fente du noyau de datte",
    "la petitesse et la dérisoire mesure",
    "métaphore démonstrative",
    "ni moins ni plus",
    "mafhūm al-ḫiṭāb",
    "le poids d’un atome",
    "an-Nisāʾ : 40",
    "l’aveugle du cœur",
    "le qāḍī Abū Muḥammad",
    "les figures du châtiment",
    "sans imāla",
    "avec imāla",
    "Abū ʿAmr",
    "Abū ʿAlī",
    "Sībawayhi",
    "la différence de degré s’y réalise",
    "Mafātīḥ al-ġayb de Fakhr ad-Dīn ar-Rāzī",
    "tome 12/273",
    "l’âme humaine est la plus noble",
    "la nutrition, la croissance, la génération, le sens et le mouvement",
    "des substances sacrées et des esprits abstraits",
    "puissances prophétiques",
]:
    if frag not in norm:
        errors.append(f"glose/nom attendu absent : {frag[:55]}")


def bare(t: str) -> str:
    return re.sub(r"[\u064B-\u065F\u0670\u06D6-\u06ED\u0640\u0671]", "", t)


cache = json.load(open("scripts-translate/quran-cache.json", encoding="utf-8"))
ar17 = dict((i, t) for i, t in cache["17"]["ar"])
v70, v71, v72 = (ar17[i] for i in (70, 71, 72))
b70, b71, b72 = (bare(v) for v in (v70, v71, v72))
for f in ["ولقد كرمنا بنى ءادم وحملنهم", "فى لبر ولبحر", "ورزقنهم من لطيبت",
          "وفضلنهم على كثير ممن خلقنا تفضيلا"]:
    if f not in b70:
        errors.append(f"cache 17:70 inattendu ({f[:35]})")
for f in ["يوم ندعوا كل أناس بإممهم", "فمن أوتى كتبه بيمينه",
          "فأولئك يقرءون كتبهم ولا يظلمون فتيلا"]:
    if f not in b71:
        errors.append(f"cache 17:71 inattendu ({f[:35]})")
for f in ["ومن كان فى هذه أعمى", "فهو فى لءاخرة أعمى وأضل سبيلا"]:
    if f not in b72:
        errors.append(f"cache 17:72 inattendu ({f[:35]})")
ar4 = dict((i, t) for i, t in cache["4"]["ar"])
if "مثقال ذرة" not in bare(ar4[40]):
    errors.append("cache 4:40 sans « مثقال ذرة » (renvoi du sens obvié)")

# préparation de la leçon suivante au DOM
if "73 à 77" not in norm:
    errors.append("préparation : les versets 73-77 absents du DOM")

# citations hors rasm — interdites au corps après l'évaluation (versets 66-69 : leçon précédente)
body = norm.split("<h2>L’évaluation", 1)[1]
for pat, label in [
    (r"fait voguer pour vous les navires", "al-Isrāʾ 17:66 (leçon précédente — non portée)"),
    (r"ceux que vous invoquiez en dehors de Lui", "al-Isrāʾ 17:67 (leçon précédente — non portée)"),
    (r"fasse engloutir par un pan de terre", "al-Isrāʾ 17:68 (leçon précédente — non portée)"),
    (r"ouragan de pierres", "al-Isrāʾ 17:68 (leçon précédente — non portée)"),
    (r"vous y ramène une autre fois", "al-Isrāʾ 17:69 (leçon précédente — non portée)"),
    (r"vent qui brise tout", "al-Isrāʾ 17:69 (leçon précédente — non portée)"),
    (r"fasse noyer à cause de votre dénégation", "al-Isrāʾ 17:69 (leçon précédente — non portée)"),
    (r"pour vous défendre contre Nous", "al-Isrāʾ 17:69 (leçon précédente — non portée)"),
]:
    if re.search(pat, body, re.IGNORECASE):
        errors.append(f"citation inattendue : {label}")

if re.search(r"[\u0600-\u06FF\u0750-\u077F\u08A0-\u08FF\uFB50-\uFDF9\uFDFB-\uFDFF\uFE70-\uFEFF]", norm):
    errors.append("caractère arabe résiduel détecté")

if errors:
    print("ÉCHEC :")
    for e in errors:
        print(" -", e)
    sys.exit(1)
print("PASS : leçon 726 — versets 70-72 rendus sur le rasm warš du cache (l’honneur "
      "fait aux fils d’Adam, le transport sur terre et sur mer, la subsistance des "
      "choses pures, la préférence nette sur beaucoup de créatures, l’appel des "
      "groupements par leur imam, le livre remis à la main droite lu avec plaisir "
      "sans la moindre injustice — un fil —, l’aveugle d’ici-bas plus égaré encore "
      "dans l’au-delà), les gloses lexicales (bī-imāhihim celui qu’ils suivaient, "
      "fatiilan l’enveloppe délicate du noyau, aḍall plus égaré encore, ar-riqz tout "
      "ce dont le profit est sain), le tafsīr de l’honneur (les trois genres, Ibn "
      "ʿAṭiyya sur le distingué des fils d’Adam et le nombreux méprisé, at-Ṭabarī "
      "manger avec ses mains, la course du cheval et la noblesse du coq, l’honneur "
      "par l’intellect, le débat des anges), les états de l’au-delà (la bāʾ et ses "
      "deux taʾwīl, Muǧāhid/Qatāda/Ibn Zayd/Ibn ʿAbbās/al-Ḥasan sur l’imam, le fil "
      "de la fente du noyau et la métaphore démonstrative, mafhūm al-ḫiṭāb et "
      "an-Nisāʾ 40 « le poids d’un atome », le qāḍī Abū Muḥammad et la "
      "correspondance des deux āyāt, les qirāʾāt d’« aʿmā » — ʿahā sans imāla, avec "
      "imāla, Abū ʿAmr, Abū ʿAlī —, Sībawayhi et la cécité du cœur), les finalités "
      "(le plus bel agencement, l’ikhlāṣ et le remerciement, le compte selon la "
      "justice absolue), la préparation 73-77 au DOM, aucune citation hors rasm "
      "(17:66-69 interdits au corps après l’évaluation), 0 arabe résiduel.")

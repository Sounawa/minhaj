#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Minhāj — contrôle coranique et de contenu de la leçon 760 (tafsir-5ep,
sūrat al-Kahf v82-84 de l'imprimé warš — vingt-deuxième leçon du second livre,
pages 165-170 du manuel miroir tafsir-3-thanawi). La plage imprimée (82-84)
correspond aux āyāt 83-85 du cache canonique ḥafṣ (décalage de un, tranché
R511, valable leçons 12-23). Les trois āyāt sont rendues du cache (présence
vérifiée) ; la cache 82 (leçon 759) et la cache 86-92 (leçon 761) sont
interdites de double rendu ; le rasm nu du cache interdit au corps
(0 arabe — FR-seule)."""
import json
import re

HTML = "tr-tmp/lesson-760-fr.html"
html = open(HTML, encoding="utf-8").read()
norm = re.sub(r"[ \u202f\u00a0]+", " ", html.replace("&nbsp;", "\u00a0"))
errors = []

# 1. structure et marqueurs
for frag in [
    "Source du cours",
    "Vingt-deuxième leçon du second livre du parcours",
    "pages 165 à 170 de l’imprimé miroir",
    "1_20220304_20220304_2251",
    "bornes de la leçon tranchées par le sondage documenté R522",
    "sūrat al-Kahf, al-āyāt : 82-84",
    "jamais devinée",
    "la plage imprimée (82-84) correspond aux āyāt 83 à 85 du cache canonique",
    "Les objectifs de la leçon",
    "Le tamhīd",
    "Le commentaire",
    "La glose",
    "L’extraction des thèmes des āyāt",
    "Premièrement",
    "Deuxièmement",
    "Les subtilités et les bienfaits",
    "L’évaluation",
    "L’exploitation",
    "la page imprimée 170",
    "interdites de double rendu",
    "déjà livrée en la leçon 761",
]:
    if frag.lower() not in norm.lower():
        errors.append(f"fragment attendu absent : {frag[:55]}")

# 2. les āyāt 83-85 rendus du cache — présence (3 rendus + numéros imprimés 82-84)
cache = json.load(open("scripts-translate/quran-cache.json", encoding="utf-8"))
fr18 = {n: t for n, t in cache["18"]["fr"]}
rendus = [fr18[n] for n in (83, 84, 85)]
rendus_norm = [r.replace("'", "’").replace(" ", "") for r in rendus]
compact = norm.replace(" ", "")
for r in rendus_norm:
    if r not in compact:
        errors.append(f"rendu coranique attendu absent : {r[:55]}")
for num in ("(82)", "(83)", "(84)"):
    if num not in norm:
        errors.append(f"numéro imprimé absent : {num}")

# 3. interdits de double rendu (leçon 759 et leçon 761)
for interdit, n in [("Et quant au mur, il appartenait à deux garçons", 82),
                    ("Et quand il eut atteint le Couchant, il trouva", 86)]:
    if interdit.replace("'", "’").replace(" ", "") in compact:
        errors.append(f"āya interdite de double rendu présente (cache {n})")

# 4. contenu attendu (confrontation au manuel — glose, lectures, exégètes)
contenu = [
    "je le narrerai et vous le ferai réciter",
    "Nous lui donnâmes une place et un rang ferme",
    "son lieu d’occultation, la direction de son coucher",
    "En quoi les āyāt dépeignent-elles Dū l-Qarnayn",
    "Qu’est-ce que Dieu a donné à Dū l-Qarnayn",
    "la source boueuse",
    "la quatrième des histoires mentionnées en la sūra",
    "aux associateurs de Qurayš",
    "leur question sur l’esprit",
    "al-Isrāʾ : 85",
    "l’histoire des gens de la caverne",
    "les levers du soleil et ses couchers",
    "tire profit et prend les leçons",
    "deux tresses de cheveux qui étaient ses deux « cornes »",
    "les tresses sont les cornes de la tête",
    "une chose admirable",
    "la multitude de ses auxiliaires et de ses armées",
    "la terreur qu’il inspirait",
    "sillonnant la terre",
    "une science, ou un outil, ou un instrument",
    "l’origine de « la voie » étant la corde",
    "tout ce par quoi l’on atteint le but visé",
    "la connaissance des choses",
    "une généralité spécifiée",
    "des voies de l’établissement",
    "sur ʿĀd",
    "la tempête qui détruisit tout par la permission de son Seigneur",
    "elle ne détruisit que ce que Dieu Très-Haut voulut",
    "Abū Ḥayyān",
    "la limite extrême de l’habité de la terre",
    "son souvenir demeure",
    "contre les habitudes",
    "al-Baḥr al-Muḥīṭ",
    "il s’employa à la marche",
    "déjà livrées en la leçon 761",
    "Al-Qurṭubī rapporte de l’imām Abū Bakr al-Qaffāl",
    "jusqu’à toucher son corps",
    "il tourne avec le ciel autour de la terre",
    "contigu à la terre",
    "la dernière des sources",
    "au témoignage de l’œil",
    "comme si elle entrait en la terre",
    "et il ne fut point visé qu’elle se levât sur eux au point de les toucher",
    "al-Ǧāmiʿ li-aḥkām al-Qurʾān",
    "il la trouva se coucher dans une source boueuse",
    "comment l’y fonde-t-on au principe",
    "la lexie du marécage",
    "Abū Ḥāmid al-Ġazālī",
    "l’adorateur n’a de capacité que par l’établissement de son maître",
    "du plus grand des rois de la terre",
    "une motte (fragment de terre sèche)",
    "il n’est de force ni de puissance que par Dieu",
    "la nuque de toutes les créatures est dans Sa poigne",
    "Iḥyāʾ ʿulūm ad-dīn : 4/403",
    "Quelle est la qualité divine que le texte établit",
    "l’opportunité de la mention du texte",
    "Qu’est-ce qui incombe à l’adorateur face à cette qualité divine",
    "Yāǧūǧ et Māǧūǧ",
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
print("VERIFY PASS — leçon 760 : 3 rendus cache 83-85 présents, numéros imprimés (82)-(84),",
      "interdits absents,", len(contenu), "contrôles de contenu, 0 arabe au corps.")

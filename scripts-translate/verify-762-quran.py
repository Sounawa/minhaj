#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Minhāj — contrôle coranique et de contenu de la leçon 762 (tafsir-5ep,
sūrat al-Kahf v92-97 de l'imprimé warš — vingt-quatrième leçon du second livre,
pages 179-187 du manuel miroir tafsir-3-thanawi). Décalage imprimé→cache de un
des leçons 12 à 23 (R511) puis de deux dans la zone : la leçon 24 couvre les
āyāt 93 à 99 du cache canonique ḥafṣ (tranché sur le contenu du livre :
commentaire p.184-185 + taqwīm p.186). Les sept āyāt sont rendues du cache
(présence vérifiée) ; les āyāt 1-92 (leçons 739-761) et la cache 100 (leçon
suivante) sont interdites de double rendu ; le rasm nu du cache interdit au
corps (0 arabe — FR-seule)."""
import json
import re

HTML = "tr-tmp/lesson-762-fr.html"
html = open(HTML, encoding="utf-8").read()
norm = re.sub(r"[ \u202f\u00a0]+", " ", html.replace("&nbsp;", "\u00a0"))
errors = []

# 1. structure et marqueurs
for frag in [
    "Source du cours",
    "Vingt-quatrième leçon du second livre du parcours",
    "pages 179 à 187 de l’imprimé miroir",
    "1_20220304_20220304_2251",
    "l’ʾiʿdād qiblī de p.178 porte la révision de l’exégèse des āyāt de la leçon au NUM imprimé relu sur rendu image (92-97)",
    "p.179 ouvre la leçon 24 au badge relu sur rendu image",
    "les objectifs de la leçon 25 ouvrent p.188",
    "fragment de sūrat an-Nabāʾ",
    "convergence quadruple",
    "la plage imprimée (92-97) correspond aux āyāt 93 à 99 du cache canonique",
    "Les objectifs de la leçon",
    "Le tamhīd",
    "Le commentaire",
    "La glose",
    "L’extraction des thèmes des āyāt",
    "Premièrement",
    "Deuxièmement",
    "Troisièmement",
    "Les subtilités et les bienfaits",
    "L’évaluation",
    "L’exploitation",
    "la page imprimée 187",
    "jamais devinée",
    "interdites de double rendu",
    "coquille du livre déclarée",
]:
    if frag.lower() not in norm.lower():
        errors.append(f"fragment attendu absent : {frag[:55]}")

# 2. les āyāt 93-99 rendus du cache — présence (7 rendus + numéros imprimés 92-97)
cache = json.load(open("scripts-translate/quran-cache.json", encoding="utf-8"))
fr18 = {n: t for n, t in cache["18"]["fr"]}
rendus = [fr18[n] for n in (93, 94, 95, 96, 97, 98, 99)]
rendus_norm = [r.replace("'", "’").replace(" ", "") for r in rendus]
compact = norm.replace(" ", "")
for r in rendus_norm:
    if r not in compact:
        errors.append(f"rendu coranique attendu absent : {r[:55]}")
for num in ("(92)", "(93)", "(94)", "(95)", "(96)", "(97)"):
    if num not in norm:
        errors.append(f"numéro imprimé absent : {num}")
if norm.count("(97)") < 2:
    errors.append("le numéro imprimé (97) doit couvrir les āyāt cache 98 et 99 (2 citations)")

# 3. interdits de double rendu (leçons 739-761 et leçon suivante)
for interdit, n in [("Puis, il suivit (une autre) voie.", 92),
                    ("Et ce jour-là Nous présenterons de près l’Enfer aux mécréants,", 100)]:
    if interdit.replace(" ", "") in compact:
        errors.append(f"āya interdite de double rendu présente (cache {n})")

# 4. contenu attendu (confrontation au manuel — glose, lectures, exégètes)
contenu = [
    "viens à moi, donne-moi et tends-moi",
    "une percée et un forage",
    "l’assistance y étant expliquée par la force",
    "Ibn Kaṯīr, Nāfiʿ, Abū ʿAmr, Ibn ʿĀmir et al-Kisāʾī lurent « aṯūnī »",
    "donnez-moi les morceaux de fer et tendez-les-moi",
    "Abū Bakr, d’après Šuʿba, d’après ʿĀṣim, lut « iʾtūnī »",
    "venez à moi et apportez-moi",
    "une demande de manutention, non un appel à la donation et au don",
    "il ne prenait point d’eux de salaire",
    "je le rédigeai et en réuni les lettres",
    "aš-Šuʿarāʾ : 196",
    "les rois ne dirigent point l’affaire de la construction",
    "l’ordonneur établi au rang de l’ordonné",
    "les deux montagnes affrontées",
    "l’une des deux rencontre l’autre",
    "les deux versants d’une montagne",
    "Nāfiʿ, Ḥamza et al-Kisāʾī lurent au fatḥ de la ṣād redoublée",
    "Ibn Kaṯīr, Ibn ʿĀmir et Abū ʿAmr lurent au ḍamm de la ṣād et du dāl",
    "ʿĀṣim, en la transmission d’Abū Bakr, lut au ḍamm de la ṣād et au sukūn du dāl",
    "les deux surfaces supérieures des deux montagnes",
    "des soufflets et des instruments préparés à cela",
    "non avec les bouches des hommes",
    "une seule masse comme le feu",
    "le cuivre fondu",
    "le plomb",
    "le fer fondu",
    "Dāwūd",
    "ni les pioches ni les haches n’y œuvrent",
    "un rang de blocs de fer et de pierres",
    "quand la fonte s’était durcie",
    "jusqu’à ce que l’ouvrage fût parfait",
    "deux langues y sont",
    "certains d’entre eux en omissent la tāʾ",
    "l’ascension ou le percement",
    "leur impuissance totale",
    "du succès de la stratégie du remblai",
    "Le locuteur y est Dū l-Qarnayn",
    "l’agréable surprise",
    "le trône de Balqīs",
    "an-Naml : 40",
    "le rendez-vous de mon Seigneur",
    "le Jour de la Résurrection",
    "l’heure de la sortie de Yāǧūǧ et Māǧūǧ",
    "masdar nonnalisé de « dakkā yadukkā »",
    "al-Azharī",
    "je l’aplanis",
    "égal, aplani, fondu et étalé",
    "ʿĀṣim, Ḥamza et al-Kisāʾī lurent « dakkāʾa » au madd",
    "la chamelle « dakkāʾ »",
    "celle qui n’a point de bosse",
    "second objet de « Il fit »",
    "le mur ou le remblai est masculin",
    "la traversée du remblai et son nivellement",
    "al-Anbiyāʾ : 96",
    "le Jour de la Résurrection, son rappel y étant déjà venu",
    "djinns et hommes",
    "le jour de l’achèvement du remblai",
    "après la construction du remblai",
    "après l’ouverture du remblai",
    "Al-Qurṭubī dit",
    "le plus apparent d’eux est celui du milieu",
    "al-Ǧāmiʿ li-aḥkām al-Qurʾān : 11/56",
    "il s’agite et se mêle",
    "l’onde de la mer",
    "l’ange de la Trompe est Isrāfīl",
    "la Trompe aux lèvres",
    "Sunan at-Tirmiḏī",
    "2431",
    "Ǧāmiʿ al-Bayān : 16/29-30",
    "toute la création pour le lieu du compte",
    "jinas d’attribution",
    "l’objet absolu",
    "son interprétation est cohérente",
    "au fil des âges et la succession des générations",
    "le premier est le plus digne",
    "la cause en son avènement",
    "l’appellation du causé par le nom de « la miséricorde »",
    "toute piété et œuvre salutaire",
    "sūrat al-Aʿrāf",
    "Ibn ʿĀšūr",
    "l’antéposition du verbe de l’acte sur le verbe de la capacité",
    "al-Taḥrīr wa-t-Tanwīr",
    "J’expose les manifestations du salut et de l’émendation",
    "le régi dont le tanwīn tient lieu en « ce jour-là »",
    "l’histoire de Dū l-Qarnayn : des leçons et des enseignements",
    "quatre groupes",
    "exposer les teneurs globales de l’histoire de Dū l-Qarnayn",
    "la cache 99 — rendue en cette leçon — interdite de double rendu à la leçon suivante",
    "ce qui fut préparé aux mécréants en l’Enfer",
]
for c in contenu:
    if c.lower() not in norm.lower():
        errors.append(f"contenu attendu absent : {c[:60]}")

# 5. 0 arabe au corps (le rasm nu du cache interdit hors citations déclarées)
arabe = re.findall(r"[\u0600-\u06FF\u0750-\u077F]", norm)
arabe = [a for a in arabe if a not in "\u061f"]
if arabe:
    errors.append(f"caractères arabes au corps : {len(arabe)} (0 attendu)")

if errors:
    print("VERIFY ÉCHEC —", len(errors), "problème(s) :")
    for e in errors:
        print("  -", e)
    raise SystemExit(1)
print("VERIFY PASS — leçon 762 : 7 rendus cache 93-99 présents, numéros imprimés (92)-(97),",
      "interdits absents,", len(contenu), "contrôles de contenu, 0 arabe au corps.")

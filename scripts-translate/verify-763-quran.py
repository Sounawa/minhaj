#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Minhāj — contrôle coranique et de contenu de la leçon 763 (tafsir-5ep,
sūrat al-Kahf v98-101 de l'imprimé warš — vingt-cinquième leçon du second
livre, pages 188-194 du manuel miroir tafsir-3-thanawi). Décalage
imprimé→cache de un des leçons 12 à 23 (R511), de deux dans la zone de la
leçon 24 (R523), puis de QUATRE en cette zone (tranché R526 sur le contenu :
la boîte de p.188 ouvre à la cache 102 sous médaillon (98), le commentaire
p.189-193 ne glossant que les āyāt cache 102-105). Les quatre āyāt sont
rendues du cache (présence vérifiée, le guillemet fermant parasite noyé dans
le cache 105 étant normalisé — « vaines». » → « vaines. », déclaré) ; les
āyāt 1-101 (leçons 739-762, cache 100-101 réunies par le fendo warš à la zone
finale de la leçon 24) et la cache 106 (leçon suivante) sont interdites de
double rendu ; le rasm nu du cache interdit au corps (0 arabe — FR-seule)."""
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
    "l’ʾiʿdād qiblī de p.187 porte la révision de l’exégèse des āyāt de la leçon au NUM relu sur image (98-101)",
    "p.188 ouvre la leçon 25 au badge relu sur rendu image",
    "les objectifs de la leçon 26 ouvrent p.195",
    "sūrat al-Kahf (al-āyāt : 102 – 105)",
    "le badge relu résout le NB laissé par R523",
    "convergence quadruple",
    "la grille « v102-105 » CONFIRMÉE PAR SONDAGE",
    "DÉCOUVERTE DE DÉCALAGE",
    "la leçon 25 rend les āyāt 102 à 105 du cache aux numéros imprimés (98)-(101)",
    "fendo de la numérotation warš déclaré",
    "Les objectifs de la leçon",
    "Le tamhīd",
    "Le commentaire",
    "La glose",
    "L’extraction des thèmes des āyāt",
    "Premièrement",
    "Deuxièmement",
    "Troisièmement",
    "Quatrièmement",
    "Les subtilités et les bienfaits",
    "L’évaluation",
    "L’exploitation",
    "la page imprimée 194",
    "jamais devinée",
    "interdites de double rendu",
    "passe de deux (fin de la leçon 24, R523) à quatre",
]:
    if frag.lower() not in norm.lower():
        errors.append(f"fragment attendu absent : {frag[:55]}")

# 2. les āyāt 102-105 rendus du cache — présence (4 rendus + numéros imprimés 98-101)
cache = json.load(open("scripts-translate/quran-cache.json", encoding="utf-8"))
fr18 = {n: t for n, t in cache["18"]["fr"]}
rendus = []
for n in (102, 103, 104, 105):
    t = fr18[n]
    if n == 105:
        t = t.replace("»", "")  # guillemet fermant parasite du cache normalisé (déclaré)
    rendus.append(t)
rendus_norm = [r.replace("'", "’").replace(" ", "") for r in rendus]
compact = norm.replace(" ", "")
for r in rendus_norm:
    if r not in compact:
        errors.append(f"rendu coranique attendu absent : {r[:55]}")
for num in ("(98)", "(99)", "(100)", "(101)"):
    if num not in norm:
        errors.append(f"numéro imprimé absent : {num}")

# 3. interdits de double rendu (leçons 739-762 et leçon suivante)
interdits = [
    ("Puis, il suivit (une autre) voie.", 92),
    ("aquel Récit 99", 0),  # placeholder évité — voir liste ci-dessous
]
interdits = [
    (fr18[99].replace("'", "’"), 99),
    (fr18[100].replace("'", "’"), 100),
    (fr18[101].replace("'", "’"), 101),
    (fr18[106].replace("'", "’"), 106),
    (fr18[110].replace("'", "’"), 110),
]
for interdit, n in interdits:
    if interdit.replace(" ", "") in compact:
        errors.append(f"āya interdite de double rendu présente (cache {n})")

# 4. contenu attendu (confrontation au manuel — glose, lectures, exégètes)
# (les textes des āyāt sont déjà contrôlés en 2 — présence exacte du cache)
contenu = [
    "l’interrogation y est de reproche et d’humiliation",
    "dénigrement des associateurs dans leurs croyances vaines",
    "par serments et offrandes",
    "lecture anomale à portée exégétique",
    "Ibn Masʿūd",
    "les démons",
    "les idoles, parce qu’elles sont leur création et leur possession",
    "Abū Ḥayyān",
    "métaphore ironique",
    "la lexie du marécage",
    "l’augmentatif venant de la lexie de la perte",
    "à l’accusatif de spécification",
    "les œuvres des associateurs, en la prière et ailleurs, sont variées",
    "Nāfiʿ, Ibn Kathīr, Abū ʿAmr et al-Kisāʾī lurent au kasr",
    "les autres lecteurs lurent au faṭḥ",
    "l’aïne médiane cassée",
    "le faṭḥ étant le plus fréquent et le plus analogue",
    "ceux qui ont nié les signes, la rencontre et le Jour du relèvement",
    "la bāʾ de « en avoir mécru » est de causalité",
    "les āyāt de la Révélation",
    "les miracles des prophètes",
    "la dérision, l’ironie, le mépris et la plaisanterie",
    "la pesée des œuvres est des dogmes de la foi",
    "Al-Ṭabarī",
    "les balances ne s’alourdissent que par les œuvres salutaires",
    "al-Ǧāmiʿ li-aḥkām al-Qurʾān : 61/53",
    "l’élision de l’épithète",
    "al-Anbiyāʾ : 47",
    "aucune bonne œuvre à être pesée dans les balances",
    "quiconque n’a point de bonne œuvre est au Feu",
    "ʿUbayd b. ʿUmayr",
    "Muǧāhid, d’Ibn Muḥayṣin et de Yaʿqūb",
    "toutes lectures anomalies, excepté celle de la masse",
    "l’aile d’un moustique",
    "Ṣaḥīḥ al-Buẖārī",
    "chapitre « Ceux-là qui ont nié les signes de leur Seigneur et Sa rencontre",
    "l’avertissement de la moquerie envers les āyāt d’Allah et Ses messagers",
    "l’expédition de Tabūk",
    "al-Tawba : 65-66",
    "la magnification de Sa parole",
    "Ibn al-ʿArabī",
    "les mécréants en Allah, au Jour dernier, aux prophètes et à l’obligation",
    "l’interprétation corrompue",
    "corrompu leurs œuvres par le fait de montrer",
    "à la quête du plus vil",
    "Aḥkām al-Qurʾān : 3/442",
    "le seul jeu des points séparant le bāʾ du nūn",
    "« ils s’imaginent » et « ils font bien »",
    "l’annulation étant la contrepartie de l’association",
    "ʿAbdallāh b. Ǧudʿān",
    "nourrissait le démuni",
    "Seigneur, pardonne-moi ma faute au Jour de la religion",
    "Ṣaḥīḥ Muslim",
    "celui qui meurt en mécréant ne tire nul profit de son œuvre",
    "les Jardins de Firdaws",
    "cache 106 et suivantes",
    "la leçon suivante ouvre en la page 195",
    "sonde kahf-probe-l25.py",
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
print("VERIFY PASS — leçon 763 : 4 rendus cache 102-105 présents, numéros imprimés (98)-(101),",
      "interdits absents (cache 99-101, 106, 110),", len(contenu), "contrôles de contenu, 0 arabe au corps.")

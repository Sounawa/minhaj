#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Minhāj — contrôle coranique de la leçon 318 (ṣulḥ 2, l'injuste et le tuteur du sang) :
le rasm du chapitre (fiqh-3 p.105-114) cite UN SEUL texte canonique :
  1. le hadith de la pièce du feu [Ṣaḥīḥ Muslim, livre des jugements, chapitre du
     jugement sur l'apparent et la preuve], accompagné de la référence imprimée
     [Bidāyat al-muǧtahid wa-nihāyat al-muqtaṣid, 4/244].
AUCUN verset coranique n'est cité par les pages de la leçon (le verset de la
conciliation An-Nisāʾ 114 appartenant à la leçon précédente du bāb, le verset
« aṣ-ṣulḥu ḫayr » au bāb du Mukhtaṣar mais non au manuel). Vérification :
la présence du hadith rendu et de sa source, l'absence de toute citation que
la pièce ne porte pas, et la présence des clauses doctrinales du régime des
huit masāʾil et de la section de la veuve."""
import re
import sys

HTML = "scripts-translate/tr-tmp/pdf-mut23h2v-318.html"
html = open(HTML, encoding="utf-8").read()

errors = []

# 1. citations rendues attendues — le hadith de la pièce du feu
for frag in [
    "Vous vous disputez auprès de moi",
    "plus éloquent dans sa preuve que l’autre",
    "je juge alors selon ce que j’entends de lui",
    "qu’il ne prenne rien de lui",
    "je ne lui coupe qu’une pièce du feu",
]:
    if frag not in html:
        errors.append(f"fragment du hadith rendu attendu absent du corps : {frag[:60]}")

if not re.search(r"Ṣaḥīḥ Muslim, livre des jugements, chapitre du jugement sur l’apparent", html):
    errors.append("citation [Ṣaḥīḥ Muslim, al-aqḍiya, ḥukm bi-l-ẓāhir] absente")
if not re.search(r"Bidāyat al-muǧtahid wa-nihāyat al-muqtaṣid,\s*4/244", html):
    errors.append("référence imprimée [Bidāyat al-muǧtahid 4/244] absente")

# 2. citations NON portées par le rasm du chapitre — interdites DANS LE CORPS
#    (les notes du traducteur documentent par le nom les exclusions — autorisées là)
body = html.split("<h2>Notes du traducteur</h2>", 1)[0]
for pat, label in [
    (r"Nulle bonne chose dans la plupart de leurs conciliabules", "An-Nisāʾ 4:114 — verset de la PIÈCE PRÉCÉDENTE (p.101 du manuel, non porté ici)"),
    (r"récompense immense", "An-Nisāʾ 4:114 — suite du verset de la pièce précédente"),
    (r"aṣ-ṣulḥu ḫayr", "An-Nisāʾ 4:128 (le bāb du Mukhtaṣar la cite — les pages du manuel non)"),
    (r"fa-aṣliḥū", "al-Ḥuǧurāt 49:10 (non portée)"),
    (r"wa-lā tanāzaʿū", "al-Anfāl 8:46 (non portée)"),
    (r"yūṣīkumu", "an-Nisāʾ 4:11 (hors pièce)"),
    (r"iḫwatan riǧālan", "an-Nisāʾ 4:176 (hors pièce)"),
    (r"man taraka mālan", "hadith de l’héritage (hors pièce)"),
    (r"alḥiqū al-farāʾiḍa", "hadith alḥiqū (hors pièce)"),
    (r"Le ṣulḥ est permis entre les musulmans", "hadith d’Abū Hurayra — PIÈCE PRÉCÉDENTE (p.101, non porté ici)"),
    (r"vendre le crédit contre le crédit|kalāʾ contre kalāʾ", "hadith du kalāʾ — PIÈCE PRÉCÉDENTE (p.102, non porté ici)"),
    (r"kaṯīrin min naǧwāhim", "rasm arabe translittéré du verset — la pièce rend la traduction, non le rasm"),
]:
    if re.search(pat, body):
        errors.append(f"citation inattendue détectée dans le corps : {label}")

# 3. structure doctrinale — les huit masāʾil (6+2) et la section de la veuve
for frag, label in [
    ("huit masāʾil", "le compte du régime de rescision"),
    ("six", "les six rescindables"),
    ("pièce du feu", "le hadith rendu"),
    ("le montant de son héritage", "la clause du matn (première configuration de la veuve)"),
    ("comme vente et change", "la clause du matn (dirhams et biens contre or)"),
    ("quatre-vingts", "l’exemple de la veuve (10/80)"),
    ("ratl", "l’exemple de l’incertitude (gharar)"),
    ("al-istiʾrāʾ", "le terme de l’istiṯmār d’al-ʿAlīsh"),
    ("l’extinction", "le terme ibrāʾ de l’istiṯmār"),
    ("Ibn ʿĀšir", "la chaîne de l’istiṯmār"),
]:
    if frag not in body:
        errors.append(f"clause doctrinale attendue absente du corps : {label}")

# 4. cohérence des chiffres du régime : 6 + 2 = 8 (continuations spécifiques,
#    les deux visages du sang partageant la virgule avec les masāʾil)
six = sum(1 for pat in [
    r"que l’injuste confesse après",
    r"qu’une preuve témoigne pour la victime",
    r"que la victime ait transigé ayant une preuve",
    r"que la victime ait transigé sur le déni",
    r"que le transigeant n’ait pas proclamé devant",
    r"que le défendeur confesse le droit en secret",
] if re.search(pat, body))
deux = sum(1 for pat in [
    r"que le transigeant ne connaisse pas, s",
    r"que le transigeant prétende la perte",
] if re.search(pat, body))
veuve = sum(1 for pat in [
    r"qu’elle prenne le montant de son héritage",
    r"qu’elle prenne moins que son héritage",
    r"qu’elle prenne plus que son héritage",
    r"que le règlement porte sur une chose donnée hors",
] if re.search(pat, body))
if six != 6:
    errors.append(f"les six masāʾil rescindables ne se comptent pas : {six}/6")
if deux != 2:
    errors.append(f"les deux masāʾil irrévocables ne se comptent pas : {deux}/2")
if veuve != 4:
    errors.append(f"les quatre configurations de la veuve ne se comptent pas : {veuve}/4")

if errors:
    print("ÉCHEC — le contrôle de la leçon 318 relève :")
    for e in errors:
        print("  ✗", e)
    sys.exit(1)

print("OK — contrôle coranique et doctrinal de la leçon 318 : 0 citation non portée, "
      "hadith de la pièce du feu rendu avec sa source [Ṣaḥīḥ Muslim, al-aqḍiya], "
      "référence Bidāyat 4/244 portée, 0 verset (la pièce n’en cite aucun), "
      "régime des huit masāʾil complet (6 rescindables + 2 irrévocables), "
      "section de la veuve rendue avec ses quatre configurations.")
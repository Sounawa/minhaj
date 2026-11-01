#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Minhāj — contrôle coranique de la leçon 728 (tafsir-5ep, Isrāʾ 78-81).
Vérifie : rendus français des versets 78-81 (rasm warš du cache), les gloses
lexicales (dulūk aš-šams le passage au méridien, ġasaq al-layl le noir et les
ténèbres — imprimé altéré, qurʾān al-faǧr la prière de l'aube), les noms portés
(Ibn Masʿūd, Jābir, Abū Bakr, Zayd ibn Aslam, al-Ḥasan al-Baṣrī, Ibn ʿAbbās,
Ibn ʿAṭiyya, Muǧāhid, Aṭ-Ṭabarī, Abū Hurayra, Abū Bakr an-Naqqāš, Qatāda,
Ibn Ǧurayǧ, Abū Ṣāliḥ, Ibn Hišām, Ibn ʿAǧība al-Baḥr al-madīd 3/422, Abū
Dāwūd aṣ-Ṣaḫtiyānī forme imprimée altérée), les matières (les cinq prières —
Ẓuhr, ʿAṣr, Maghrib, ʿIshāʾ/al-ʿatama —, le lām de temporalité, l'Arabe et
al-Ḥasan al-Baṣrī sur dallaka/malfaǧ/muṭl, l'accusatif de « récitation » —
verbe sous-entendu, apposition, incitement —, la prière de l'aube attestée et
le hadith des anges de Ṣaḥīḥ al-Buḫārī, le tabʿīḍ et le pronom de « par elle »,
le hujūd/hajada yahtajidu et la glose de la fikāha — citation d'al-Wāqiʿa
déclarée perdue —, le surcroît d'Ibn ʿAbbās, la recommandation d'Ibn ʿAṭiyya,
la nāfila de Muǧāhid et l'année d'al-Ḥudaybiya, le chrétien converti et l'enfant
pubère, la Station louangée et l'intercession renvoyée entre prophètes, le hadith
d'Abū Hurayra, les trois intercessions d'an-Naqqāš, le Trône et la dureté de
propos, la conquête de La Mecque et le bâton/miḫṣara, le Coran/la foi/le combat
et Satan/la mécréance/l'association, la généralisation à l'extrême possible,
« était » sans temps révolu), la préparation 82-85 au DOM, l'absence de
citations hors rasm (17:73-77 = leçon précédente, interdites au corps après
l'évaluation), 0 arabe résiduel. Espaces typographiques (NNBSP/insécables)
introduits par l'auto-fix de qa-lesson normalisés avant appariement."""
import json
import re
import sys

HTML = "scripts-translate/tr-tmp/pdf-mut23h3c-728.html"
html = open(HTML, encoding="utf-8").read()
norm = html.replace("\u202f", " ").replace("\u00a0", " ")
errors = []

for frag in [
    "Accomplis la prière au déclin du soleil jusqu’à l’obscurité de la nuit",
    "la récitation de l’aube est attestée",
    "éveille-toi par elle, comme surérogatoire pour toi",
    "peut-être ton Seigneur te ressuscitera-t-Il en une station louangée",
    "fais-moi entrer par une entrée de vérité et fais-moi sortir par une sortie de vérité",
    "accorde-moi de auprès de Toi une autorité secourable",
    "La vérité est venue et le faux s’est évanoui",
    "le faux était évanescent",
]:
    if frag not in norm:
        errors.append(f"rendu attendu absent : {frag[:55]}")

if not re.search(r"»\s*\(78-81\)", norm):
    errors.append("repère de plage (78-81) absent")

for frag in [
    "son passage au méridien, hors du demi-cercle du jour",
    "son noir et ses ténèbres",
    "imprimé altéré",
    "prières obligatoires, par consensus des exégètes",
    "le lām est de temporalité, valant « au moment de »",
    "le Maghrib et le ʿIshāʾ",
    "Jibrīl vint à moi au déclin du soleil",
    "Sors, Abū Bakr",
    "Zayd ibn Aslam",
    "la ʿIshāʾ (al-ʿatama)",
    "le premier dire est le plus solide pour sa généralité",
    "al-Ḥasan al-Baṣrī",
    "la carence (muṭl)",
    "malfaǧ",
    "un verbe sous-entendu",
    "l’incitement (iġrāʾ)",
    "longue et proclamée",
    "Ṣaḥīḥ al-Buḫārī, Livre de la prière, chapitre du mérite de la prière de l’ʿAṣr",
    "Des anges se relaient en vous",
    "parti-tout (tabʿīḍ)",
    "le hujūd est le sommeil",
    "hajada yahtajidu",
    "al-Wāqiʿa",
    "vous rejetez la gaieté (fikāha)",
    "un homme fakiḥ",
    "Ibn ʿAbbās et d’autres ont dit",
    "Ibn ʿAṭiyya a dit",
    "Muǧāhid a dit : ce n’est qu’une surérogatoire",
    "l’année d’al-Ḥudaybiya",
    "un chrétien qui se convertit et un enfant qui atteint la puberté",
    "Aṭ-Ṭabarī affaiblit le dire de Muǧāhid",
    "l’intercession que les prophètes se renvoient",
    "al-Buḫārī et Muslim",
    "Je suis le maître des enfants d’Adam",
    "l’avis retenu (at-taḥqīq)",
    "Abū Hurayra",
    "Abū Bakr an-Naqqāš",
    "en faveur des gens des péchés majeurs",
    "asseye Muḥammad avec Lui sur Son Trône",
    "aṣ-Ṣaḫtiyānī",
    "Ibn ʿAbbās, al-Ḥasan et Qatāda",
    "Abū Ṣāliḥ et Muǧāhid",
    "l’entrée par la mort au tombeau, et la sortie par la Résurrection",
    "un homme de sincérité (ṣidq)",
    "la conquête de La Mecque",
    "son bâton (miḫṣara)",
    "la Sīra d’Ibn Hišām",
    "Qatāda dit : la vérité est le Coran, et le faux : Satan",
    "Ibn Ǧurayǧ",
    "la généralisation du terme à l’extrême possible",
    "nulle fin profitable",
    "« Allah était savant, puissant »",
    "la veille nocturne (taḥaǧǧud)",
    "Ibn ʿAǧība",
    "al-Baḥr al-madīd fī tafsīr al-Qurʾān al-maǧīd",
    "3/422",
    "la prière des membres (jawāriḥ)",
    "du Roi Aimant (al-Malik al-Wadūd)",
    "pour mille de son époque",
]:
    if frag not in norm:
        errors.append(f"glose/nom attendu absent : {frag[:55]}")


def bare(t: str) -> str:
    return re.sub(r"[\u064B-\u065F\u0670\u06D6-\u06ED\u0640\u0671]", "", t)


cache = json.load(open("scripts-translate/quran-cache.json", encoding="utf-8"))
ar17 = dict((i, t) for i, t in cache["17"]["ar"])
v78, v79, v80, v81 = (ar17[i] for i in range(78, 82))
b78, b79, b80, b81 = (bare(v) for v in (v78, v79, v80, v81))
for f in ["أقم لصلوة لدلوك لشمس إلى غسق ليل", "وقرءان لفجر", "إن قرءان لفجر كان مشهودا"]:
    if f not in b78:
        errors.append(f"cache 17:78 inattendu ({f[:35]})")
for f in ["ومن ليل فتهجد به نافلة لك", "أن يبعثك ربك مقاما محمودا"]:
    if f not in b79:
        errors.append(f"cache 17:79 inattendu ({f[:35]})")
for f in ["أدخلنى مدخل صدق وأخرجنى مخرج صدق", "وجعل لى من لدنك سلطنا نصيرا"]:
    if f not in b80:
        errors.append(f"cache 17:80 inattendu ({f[:35]})")
for f in ["جاء لحق وزهق لبطل", "إن لبطل كان زهوقا"]:
    if f not in b81:
        errors.append(f"cache 17:81 inattendu ({f[:35]})")

# préparation de la leçon suivante au DOM
if "82 à 85" not in norm:
    errors.append("préparation : les versets 82-85 absents du DOM")

# citations hors rasm — interdites au corps après l'évaluation (versets 73-77 : leçon précédente)
body = norm.split("<h2>L’évaluation", 1)[1]
for pat, label in [
    (r"ils ont failli te détourner", "al-Isrāʾ 17:73 (leçon précédente — non portée)"),
    (r"ami intime", "al-Isrāʾ 17:73 (leçon précédente — non portée)"),
    (r"le double \[supplice\] de la vie", "al-Isrāʾ 17:75 (leçon précédente — non portée)"),
    (r"t’inciter à fuir du pays", "al-Isrāʾ 17:76 (leçon précédente — non portée)"),
    (r"Telle fut la règle appliquée", "al-Isrāʾ 17:77 (leçon précédente — non portée)"),
    (r"pas de changement en Notre règle", "al-Isrāʾ 17:77 (leçon précédente — non portée)"),
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
print("PASS : leçon 728 — versets 78-81 rendus sur le rasm warš du cache (la prière au "
      "déclin du soleil jusqu’à l’obscurité de la nuit et la récitation de l’aube "
      "attestée, la veille surérogatoire de la nuit et la Station louangée, l’entrée et "
      "la sortie de vérité avec l’autorité secourable, la venue de la vérité et "
      "l’évanouissement du faux), les gloses lexicales (dulūk le passage au méridien hors "
      "du demi-cercle du jour, ġasaq le noir et les ténèbres — imprimé altéré —, qurʾān "
      "al-faǧr la prière de l’aube), le tafsīr des cinq prières (le consensus des "
      "exégètes, Ẓuhr et ʿAṣr au déclin, le lām de temporalité, le Maghrib et le ʿIshāʾ "
      "à l’obscurité, Jibrīl et Ibn Masʿūd, Jābir et Abū Bakr, Zayd ibn Aslam et "
      "al-ʿatama, le dire le plus solide, le commencement et la fin du dulūk, l’Arabe et "
      "al-Ḥasan al-Baṣrī — dallaka, muṭl, malfaǧ —, l’accusatif de « récitation » — "
      "verbe sous-entendu, apposition, incitement —, la majeure part du Coran proclamée, "
      "les anges qui se relaient de Ṣaḥīḥ al-Buḫārī), le taḥaǧǧud (le tabʿīḍ et le "
      "pronom de « par elle », le hujūd et hajada yahtajidu, la glose de la fikāha — "
      "citation d’al-Wāqiʿa déclarée perdue —, le surcroît d’Ibn ʿAbbās, la "
      "recommandation d’Ibn ʿAṭiyya, la nāfila de Muǧāhid, l’année d’al-Ḥudaybiya, le "
      "chrétien converti et l’enfant pubère, Aṭ-Ṭabarī affaiblissant), la Station "
      "louangée (l’intercession renvoyée entre prophètes, al-Buḫārī et Muslim, le maître "
      "des enfants d’Adam, l’avis retenu et la promesse noble, l’abrègement de "
      "l’intercession, Abū Hurayra, les trois intercessions d’an-Naqqāš, le Trône et la "
      "dureté de propos, Abū Dāwūd aṣ-Ṣaḫtiyānī imprimé altéré), l’invocation de "
      "l’entrée et de la sortie (la généralité parfaite, Médine et La Mecque, la "
      "transmission de la Loi et l’accomplissement parfait, le tombeau et la "
      "Résurrection, l’épée d’al-Ḥasan et Qatāda, la conquête de La Mecque et le "
      "miḫṣara, la Sīra d’Ibn Hišām, le Coran/la foi/le combat contre Satan/la "
      "mécréance/l’association, la généralisation à l’extrême possible, « était » sans "
      "temps révolu), l’exploitation d’Ibn ʿAǧība al-Baḥr al-madīd 3/422 (la prière des "
      "membres, la prière perpétuelle des cœurs, la veille de la nuit, le Roi Aimant, "
      "les aimants et les aimés, mille de son époque sous réserve), la préparation 82-85 "
      "au DOM, aucune citation hors rasm (17:73-77 interdits au corps après "
      "l’évaluation), 0 arabe résiduel.")

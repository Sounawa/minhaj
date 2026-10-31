#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Minhāj — contrôle coranique de la leçon 720 (tafsir-5ep, Isrāʾ 41-44).
Vérifie : rendus français des versets 41-44 (rasm warš du cache), le parallèle
les Prophètes 22, l'appui du Fer 1, les citations de la préparation (17:45-46),
les gloses lexicales et les noms portés, l'absence de citations hors rasm
(17:37-40 = leçon précédente, interdites au corps), 0 arabe résiduel."""
import json
import re
import sys

HTML = "scripts-translate/tr-tmp/pdf-mut23h3c-720.html"
html = open(HTML, encoding="utf-8").read()
errors = []

for frag in [
    "Et certes, Nous avons déployé en ce Coran",
    "pour qu’ils se rappellent",
    "et cela ne les augmente que d’un dégoût",
    "s’il y avait avec Lui des divinités comme vous le dites",
    "alors auraient-ils recherché un chemin vers le Maître du Trône",
    "Gloire à Lui — et Il est hautement élevé au-dessus de ce qu’ils disent",
    "d’une élévation grandissime",
    "Les sept cieux Le glorifient, et la terre, et ceux qui s’y trouvent",
    "et il n’est rien qui ne Le glorifie par Sa louange",
    "mais vous ne comprenez point leur glorification",
    "Il fut Clément, Grand Pardonneur",
    "S’il y avait dans les deux des divinités autre qu’Allah, elles seraient certainement ruinées",
    "Glorifie Allah tout ce qui est dans les cieux et la terre",
    "et lorsque tu récitas le Coran, Nous plaçâmes entre toi et ceux qui ne croient point à la Dernière un voile enveloppant",
    "Nous plaçâmes sur leurs cœurs des couvertures qu’ils ne le comprennent, et dans leurs oreilles une surdité",
]:
    if frag not in html:
        errors.append(f"rendu attendu absent : {frag[:55]}")

if not re.search(r"»\s*\(41-44\)", html):
    errors.append("repère de plage (41-44) absent")

def bare(t: str) -> str:
    return re.sub(r"[\u064B-\u065F\u0670\u06D6-\u06ED\u0640\u0671]", "", t)

cache = json.load(open("scripts-translate/quran-cache.json", encoding="utf-8"))
ar17 = dict((i, t) for i, t in cache["17"]["ar"])
v41, v42, v43, v44 = (ar17[i] for i in (41, 42, 43, 44))
b41, b42, b43, b44 = (bare(v) for v in (v41, v42, v43, v44))
if "ولقد صرفنا فى هذا لقرءان ليذكروا" not in b41 or "وما يزيدهم إلا نفورا" not in b41:
    errors.append("cache 17:41 inattendu (le déploiement et le dégoût)")
if "قل لو كان معه ءالهة كما يقولون" not in b42 or "إذا لبتغوا إلى ذى لعرش سبيلا" not in b42:
    errors.append("cache 17:42 inattendu (les divinités et le chemin vers le Trône)")
if "سبحنه وتعلى عما يقولون علوا كبيرا" not in b43:
    errors.append("cache 17:43 inattendu (la sanctification et l’élévation grandissime)")
if "تسبح له لسموت لسبع ولأرض ومن فيهن" not in b44 or "وإن من شىء إلا يسبح بحمده" not in b44 \
        or "ولكن لا تفقهون تسبيحهم" not in b44 or "إنه كان حليما غفورا" not in b44:
    errors.append("cache 17:44 inattendu (le tasbīḥ des cieux et le Clément Pardonneur)")
ar21 = dict((i, t) for i, t in cache["21"]["ar"])
b22 = bare(ar21[22])
if "لو كان فيهما ءالهة إلا لله لفسدتا" not in b22:
    errors.append("cache 21:22 (le parallèle tranché par la matière) inattendu")
ar57 = dict((i, t) for i, t in cache["57"]["ar"])
b571 = bare(ar57[1])
if "سبح لله ما فى لسموت ولأرض" not in b571:
    errors.append("cache 57:1 (l’appui du tasbīḥ figuré) inattendu")
b45, b46 = bare(ar17[45]), bare(ar17[46])
if "جعلنا بينك وبين لذين لا يؤمنون بلءاخرة حجابا مستورا" not in b45:
    errors.append("cache 17:45 (préparation, le voile enveloppant) inattendu")
if "جعلنا على قلوبهم أكنة أن يفقهوه" not in b46 or "وفى ءاذانهم وقرا" not in b46:
    errors.append("cache 17:46 (préparation, les couvertures et la surdité) inattendu")

for frag in ["ṣarrafnā", "lī-yadhdhakkarū", "idhkarū", "taqūlūna", "yaqūlūna",
             "ʿuluwwan", "ta-fāʿal", "at-taʿālī", "an-nufūr", "al-majāzī", "masdar",
             "ḥujubān", "akinnān", "mastūrā", "qatshurā", "wa-fatashkhurā",
             "al-iʿdād al-qiblī", "awliy al-albāb", "istiṯmār", "taqwīm",
             "al-Muwāfaqāt", "Aš-Šāṭibī", "al-Muḥarrar al-wajīz", "Ibn ʿAṭiyya",
             "al-Taḥrīr wa-t-tanwīr", "Ḥamza", "al-Kisāʾī",
             "Ibn Kathīr", "Nāfiʿ", "ʿĀṣim", "Abū ʿAmr", "al-Ḥasan", "ʿIkrima",
             "Yazīd ar-Raqāshī", "Les Prophètes 22", "ibn ʿĀshūr", "11/151", "2/982", "3/954", "ﷺ"]:
    if frag not in html:
        errors.append(f"glose/nom attendu absent : {frag}")

# citations hors rasm — interdites au corps (versets 37-40 : leçon précédente)
body = html.split("<h2>L’évaluation", 1)[0]
for pat, label in [
    (r"blâmé, banni", "al-Isrāʾ 17:39 (leçon précédente — non portée)"),
    (r"les Groupes 4", "parallèle de la leçon 719 (non porté)"),
    (r"malūman madhūran", "rendu de la leçon 719 (non porté)"),
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
print("PASS : leçon 720 — versets 41-44 rendus sur le rasm warš du cache (le déploiement "
      "pour le rappel, les divinités et le chemin vers le Trône, la sanctification et "
      "l’élévation grandissime, le tasbīḥ des sept cieux et le Clément Pardonneur), le "
      "parallèle les Prophètes 22 tranché par la matière, l’appui du Fer 1, les trois "
      "lectures de ṣarrafnā (jumhūr grossie, al-Ḥasan allégée, la lettre en sus) et les "
      "lectures de li-yadhdhakkarū (jumhūr, idhkarū de Ḥamza et al-Kisāʾī), les lectures "
      "de 17:44 (taqūlūna de Ḥamza et al-Kisāʾī, yaqūlūna d’Ibn Kathīr, Nāfiʿ, ʿĀṣim et "
      "Abū ʿAmr), le débat sur la manière du tasbīḥ (ʿIkrima, Yazīd ar-Raqāshī et "
      "al-Ḥasan), les finalités, Shāṭibī 2/982 et l’argument des deux volontés d’Ibn "
      "ʿAṭiyya 3/954, la préparation 45-54 au DOM (17:45 et 17:46 au rasm), aucune "
      "citation hors rasm (17:37-40 interdits au corps), 0 arabe résiduel.")

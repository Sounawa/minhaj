#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Minhāj — contrôle coranique de la leçon 727 (tafsir-5ep, Isrāʾ 73-77).
Vérifie : rendus français des versets 73-77 (rasm warš du cache), les gloses
lexicales (kadū, yaftinūnaka, li-taftariya, tarkuna/tarkun, khalīl-ka), les
noms portés (Ibn Ǧubayr, Muǧāhid, at-Ṭabarī, az-Zajjāj, Ibn Isḥāq, Ibn ʿAbbās,
Qatāda, aḍ-Ḍaḥḥāk, al-Farrāʾ, Sībawayhi, Abū Ḥayyān al-Baḥr al-muḥīṭ, Ibn
ʿAṭiyya, Ibn ʿArabī Aḥkām al-Qurʾān 3/603, Kaḥyī ibn Akhṭab imprimé altéré),
les lieux de la descente (Quraysh, aṭ-Ṭāʾif, les juifs de Médine), Dār an-Nadwa
et Badr, la ṭibāq du double supplice, la préparation 78-81 au DOM, l’absence de
citations hors rasm (17:70-72 = leçon précédente, interdites au corps après
l’évaluation), 0 arabe résiduel. Espaces typographiques (NNBSP/insécables)
introduits par l’auto-fix de qa-lesson normalisés avant appariement."""
import json
import re
import sys

HTML = "scripts-translate/tr-tmp/pdf-mut23h3c-727.html"
html = open(HTML, encoding="utf-8").read()
norm = html.replace("\u202f", " ").replace("\u00a0", " ")
errors = []

for frag in [
    "Ils ont failli te détourner de ce que Nous t’avions révélé",
    "tu inventes quelque chose d’autre",
    "ils t’auraient pris pour ami intime",
    "Et si Nous ne t’avions pas raffermi",
    "tu aurais bien failli t’incliner quelque peu vers eux",
    "fait goûter le double [supplice] de la vie",
    "et ensuite tu n’aurais pas trouvé de secoureur contre Nous",
    "ils ont failli t’inciter à fuir du pays pour t’en bannir",
    "ils n’y seraient pas restés longtemps après toi",
    "Telle fut la règle appliquée par Nous à Nos messagers",
    "tu ne trouveras pas de changement en Notre règle",
]:
    if frag not in norm:
        errors.append(f"rendu attendu absent : {frag[:55]}")

if not re.search(r"»\s*\(73-77\)", norm):
    errors.append("repère de plage (73-77) absent")

for frag in [
    "ils se sont approchés",
    "ils t’écartent et te détournent",
    "pour que tu forges sur nous autre que ce que Nous t’avons révélé",
    "te pencher et t’installer",
    "comme l’homme fait avec le pilier des murs",
    "tenu suspendu à ce dont Allah l’a sauvé",
    "Ibn Ǧubayr et Muǧāhid",
    "la Pierre noire",
    "At-Ṭabarī et d’autres ont dit",
    "Az-Zajjāj a dit",
    "ce qu’il y a en mon âme",
    "Ibn Isḥāq et d’autres ont dit",
    "al-Lāt",
    "elle est mecquoise",
    "aucun faux ne saurait tomber sur Allah",
    "Al-Baḥr al-muḥīṭ fī t-tafsīr d’Abū Ḥayyān",
    "le raffermissement d’Allah",
    "relève du tathbīt",
    "ṭibāq (antithèse)",
    "le double du châtiment de la vie et le double du châtiment de la mort",
    "dans le châtiment de ses épouses",
    "Kaḥyī ibn Akhṭab",
    "aš-Šām",
    "tu crains les Rūm",
    "la sūra est mecquoise",
    "Dār an-Nadwa",
    "aš-Šiʿb",
    "la caverne",
    "le jour de Badr",
    "soit La Mecque, soit Médine",
    "al-Farrāʾ",
    "Sībawayhi",
    "elles ne demeurèrent après lui sinon peu",
    "Aḥkām al-Qurʾān d’Ibn ʿArabī",
    "tome 3/603",
    "la lumière de la guidance",
    "« dulūk »",
    "« ʿasā »",
    "« al-fajr »",
]:
    if frag not in norm:
        errors.append(f"glose/nom attendu absent : {frag[:55]}")


def bare(t: str) -> str:
    return re.sub(r"[\u064B-\u065F\u0670\u06D6-\u06ED\u0640\u0671]", "", t)


cache = json.load(open("scripts-translate/quran-cache.json", encoding="utf-8"))
ar17 = dict((i, t) for i, t in cache["17"]["ar"])
v73, v74, v75, v76, v77 = (ar17[i] for i in range(73, 78))
b73, b74, b75, b76, b77 = (bare(v) for v in (v73, v74, v75, v76, v77))
for f in ["وإن كادوا ليفتنونك عن لذى أوحينا إليك", "لتفترى علينا غيره",
          "وإذا لتخذوك خليلا"]:
    if f not in b73:
        errors.append(f"cache 17:73 inattendu ({f[:35]})")
for f in ["ولولا أن ثبتنك لقد كدت تركن إليهم شيا قليلا"]:
    if f not in b74:
        errors.append(f"cache 17:74 inattendu ({f[:35]})")
for f in ["لأذقنك ضعف لحيوة وضعف لممات", "ثم لا تجد لك علينا نصيرا"]:
    if f not in b75:
        errors.append(f"cache 17:75 inattendu ({f[:35]})")
for f in ["وإن كادوا ليستفزونك من لأرض ليخرجوك منها",
          "وإذا لا يلبثون خلفك إلا قليلا"]:
    if f not in b76:
        errors.append(f"cache 17:76 inattendu ({f[:35]})")
for f in ["سنة من قد أرسلنا قبلك من رسلنا", "ولا تجد لسنتنا تحويلا"]:
    if f not in b77:
        errors.append(f"cache 17:77 inattendu ({f[:35]})")

# préparation de la leçon suivante au DOM
if "78 à 81" not in norm:
    errors.append("préparation : les versets 78-81 absents du DOM")

# citations hors rasm — interdites au corps après l'évaluation (versets 70-72 : leçon précédente)
body = norm.split("<h2>L’évaluation", 1)[1]
for pat, label in [
    (r"honoré les fils d’Adam", "al-Isrāʾ 17:70 (leçon précédente — non portée)"),
    (r"nettement préférés à plusieurs", "al-Isrāʾ 17:70 (leçon précédente — non portée)"),
    (r"groupement d’hommes par leur chef", "al-Isrāʾ 17:71 (leçon précédente — non portée)"),
    (r"la moindre injustice", "al-Isrāʾ 17:71 (leçon précédente — non portée)"),
    (r"aveugle ici-bas", "al-Isrāʾ 17:72 (leçon précédente — non portée)"),
    (r"plus égaré \[encore\]", "al-Isrāʾ 17:72 (leçon précédente — non portée)"),
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
print("PASS : leçon 727 — versets 73-77 rendus sur le rasm warš du cache (la tentative de "
      "détourner le Messager de la révélation et de lui faire forger autre chose, l’allié "
      "intime, le raffermissement contre le rukūn, le double supplice de la vie et de la "
      "mort sans secoureur, la provocation à fuir le pays et la demeure imminente, la "
      "sunna des messagers d’avant sans changement), les gloses lexicales (kadū ils se "
      "sont approchés, yaftinūnaka ils t’écartent et te détournent, li-taftariya forger "
      "sur nous, tarkuna te pencher et t’installer et le rukun des murs, khalīl-ka tenu "
      "suspendu), le tafsīr de la descente (la Pierre noire et les idoles d’Ibn Ǧubayr "
      "et Muǧāhid, at-Ṭabarī le cœur en rejet, az-Zajjāj ce qu’il y a en mon âme, Ibn "
      "Isḥāq la nuit d’honoration, aṭ-Ṭāʾif et l’année d’al-Lāt d’Ibn ʿAbbās — dire "
      "faible —, l’āya mecquoise, Ibn ʿAṭiyya le contraire révélé et nul faux sur "
      "Allah, Abū Ḥayyān sur le lawlā et le tathbīt), la ṭibāq du double supplice (Ibn "
      "ʿAbbās, Muǧāhid, Qatāda, aḍ-Ḍaḥḥāk, le dédoublement dans la récompense, la "
      "douleur et les épouses), l’expulsion (les juifs de Médine et Kaḥyī ibn Akhṭab, "
      "aš-Šām et les Rūm, le plus correct Quraysh, Dār an-Nadwa et aš-Šiʿb, la caverne, "
      "Badr exécutant l’avertissement, la terre générale ou déterminée), la sunna des "
      "nations (al-Farrāʾ sur le masdur, l’expulsion châtiée — sinon peu), les "
      "finalités (les grâces dénombrées et les complots déjoués, la faveur présente à "
      "l’esprit et la fermeté sur la croyance, le secours promis aux prophètes), la "
      "préparation 78-81 au DOM, aucune citation hors rasm (17:70-72 interdits au corps "
      "après l’évaluation), 0 arabe résiduel.")

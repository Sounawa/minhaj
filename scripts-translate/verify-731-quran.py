#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Minhāj — contrôle coranique de la leçon 731 (tafsir-5ep, Isrāʾ 90-93).
Vérifie : rendus français des versets 90-93 (rasm warš du cache — la source,
le jardin de palmiers et de vignes, la chute du ciel en morceaux « kamā
zaʿamt », la venue d'Allah et des anges en face, la maison d'ornements, la
montée au ciel et le livre, « qul subḥāna rabbī »), les gloses lexicales
(le jardin verger abondant en arbres, qbīlan faire face et voir à découvert,
zuḫruf l'or, ta-rqā gravir sur une échelle), les noms portés (ʿUtbā, Šayba,
Rabiʿa, ʿAbd Allāh b. Abī Umayya, an-Naḍr b. al-Ḥāriṯ, Quraysh, Ibn Kathīr,
Nāfiʿ, Abū ʿAmr, Ibn ʿĀmir, ʿĀṣim, Ḥamza, al-Kisāʾī, Ibn Masʿūd, Muǧāhid,
al-Fakhr ar-Rāzī, Ibn Hišām, ar-Raḥmān), les matières (le hadith des
demandes — la royauté, les biens abondants, le soin —, « je patienterai à
l'ordre d'Allah » et « tout cela relève d'Allah », les six sortes de
miracles — le minbūʿ hyperbolique, le jardin fixé à La Mecque en lieu aride,
« kamā zaʿamt » et la menace 34:9, les trois glosses de qbīlan — le garant,
la garantie, nul pareil —, le zuḫruf et la lecture d'Ibn Masʿūd avec
Muǧāhid, les degrés du ciel, ar-ruqī, l'air élevé et le ciel connu —, la
disculpation : l'interrogation négative, la Loi et la seule transmission,
la lecture-rapport d'Ibn Kathīr et Ibn ʿĀmir, les assimilateurs — viendrait
et partirait —, la mise en demeure des gens et non d'Allah, le miracle
unique et l'obstination, Mafātīḥ al-ġayb) —, les finalités (3), les
fragments de rasm du cache (17:90-93, 34:9 « nusqiṭ ʿalayhim kisafan », 2:74
« yatafaǧǧaru », 17:97 « fa-huwa l-muhtadī »), la préparation 94-98 au DOM
— imprimé « 89 - 49 » inversé —, l'absence de citations hors rasm (17:86-89
= leçon précédente ; 17:94-98 = leçon suivante — interdites au corps après
l'évaluation), 0 arabe résiduel. Espaces typographiques (NNBSP/insécables)
introduits par l'auto-fix de qa-lesson normalisés avant appariement."""
import json
import re
import sys

HTML = "scripts-translate/tr-tmp/pdf-mut23h3c-731.html"
html = open(HTML, encoding="utf-8").read()
norm = html.replace("\u202f", " ").replace("\u00a0", " ")
errors = []

for frag in [
    "Et ils dirent",
    "jusqu’à ce que tu aies fait jaillir de terre, pour nous, une source",
    "un jardin de palmiers et de vignes",
    "tu feras jaillir des ruisseaux en abondance",
    "comme tu le prétends, le ciel en morceaux",
    "tu fasses venir Allah et les anges, en face de nous",
    "une maison d’ornements",
    "tu sois monté au ciel",
    "ta montée au ciel",
    "un livre que nous puissions lire",
    "Gloire à mon Seigneur",
    "Ne suis-je qu’un être humain messager",
]:
    if frag not in norm:
        errors.append(f"rendu attendu absent : {frag[:55]}")

if not re.search(r"»\s*\(90-93\)", norm):
    errors.append("repère de plage (90-93) absent")

for frag in [
    "verger abondant en arbres",
    "faire face et voir à découvert",
    "« d’ornements » (zuḫruf) : or",
    "que tu gravis le ciel sur une échelle",
    "ʿUtbā et Šayba, fils de Rabiʿa",
    "ʿAbd Allāh b. Abī Umayya",
    "an-Naḍr b. al-Ḥāriṯ",
    "notables de Quraysh et de ses chefs",
    "si tu désires la royauté",
    "des biens abondants, si tu désires la richesse",
    "si une maladie t’atteint",
    "je patienterai à l’ordre d’Allah",
    "tout cela relève d’Allah",
    "les récits se multiplient",
    "il fut donc abrégé",
    "un écrit que je te voie portant avec toi",
    "six sortes de miracles",
    "Ibn Kathīr et Nāfiʿ",
    "Abū ʿAmr et Ibn ʿĀmir",
    "ʿĀṣim avec une kasra",
    "Ḥamza avec al-Kisāʾī",
    "fatḥa de la première radicale, ḍamma de la médiane",
    "yatafaǧǧaru",
    "al-Baqara 74",
    "racine f-ǧ-r",
    "renforce la deuxième lecture",
    "requiert l’hyperbole dans le jaillissement",
    "minbūʿ",
    "une eau abondante qui ne diminue à aucun moment",
    "alors qu’il était à La Mecque",
    "le jardin fût à La Mecque",
    "en ce lieu aride",
    "le redoublement y porte l’hyperbole",
    "ḫilālahā",
    "à travers elles et en leur intérieur",
    "34 :9 au rasm du cache",
    "des morceaux du ciel",
    "en garant, cautionnant ta véracité",
    "la garantie (qibāla)",
    "al-qabīl et al-mutaqabbil",
    "nul pareil n’existe chez nous",
    "« az-zuḫruf », en cet endroit, est l’or",
    "ce dont on se pare",
    "lecture de ʿAbd Allāh b. Masʿūd",
    "une maison d’or",
    "baytun min ḏahab",
    "Muǧāhid",
    "dans le rasm de ʿAbd Allāh",
    "les degrés du ciel",
    "« ar-ruqī » : l’ascension",
    "l’air élevé",
    "l’espace de la hauteur",
    "le ciel connu",
    "le Dieu de la création y est",
    "L’interrogation est ici une négation",
    "je vous suis envoyé avec la Loi",
    "il ne m’incombe que la seule transmission",
    "qāla subḥāna rabbī",
    "au sens du rapport",
    "du dire des assimilateurs (al-mušabbihā)",
    "viendrait et partirait",
    "ils dirent plutôt au Messager ﷺ",
    "demande à Allah qu’Il t’honore de ces miracles",
    "mirent le Messager en demeure",
    "d’après leur parole même",
    "de Ma propre personne",
    "n’a aucune puissance sur ces choses",
    "un miracle unique, le Coran",
    "nul besoin ni nécessité",
    "l’obstination et de la mise en demeure",
    "il ne m’appartient pas de mettre Allah en demeure",
    "Mafātīḥ al-ġayb",
    "al-Fakhr ar-Rāzī",
    "Lui seul mérite cela",
    "l’argument le plus grand",
    "une borne où l’on ait à délibérer",
    "quelle en est la raison",
    "en son traitement des associateurs",
    "le traitement des contradicteurs",
    "as-Sīra an-nabawiyya d’Ibn Hišām",
    "si Allah veut faire de vous cela, Il le fera",
    "nous resterons assis avec toi",
    "ce que tu feras à notre égard",
    "ar-Raḥmān",
    "ne croirons jamais en ar-Raḥmān",
    "tu ne nous feras point périr",
    "nous adorons les anges — qui sont les filles d’Allah",
    "quatre des anges attestant pour toi",
    "ils te croient et te suivent",
    "ce dont ils te connaissent le mérite à leur égard",
    "affligé et chagrin",
    "ce qu’il espérait de son peuple",
    "leur mise à distance de lui",
    "l’audace des associateurs",
    "n’ait pas hâté leur châtiment",
]:
    if frag not in norm:
        errors.append(f"glose/nom attendu absent : {frag[:55]}")

def bare(t: str) -> str:
    return re.sub(r"[\u064B-\u065F\u0670\u06D6-\u06ED\u0640\u0671]", "", t)

cache = json.load(open("scripts-translate/quran-cache.json", encoding="utf-8"))
ar17 = dict((i, t) for i, t in cache["17"]["ar"])
v90, v91, v92, v93 = (bare(ar17[i]) for i in range(90, 94))
if "وقالوا لن نؤمن لك حتى تفجر لنا من لأرض ينبوعا" not in v90:
    errors.append("cache 17:90 inattendu")
if "أو تكون لك جنة من نخيل وعنب فتفجر لأنهر خللها تفجيرا" not in v91:
    errors.append("cache 17:91 inattendu")
for f in ["أو تسقط لسماء كما زعمت علينا كسفا أو تأتى بلله ولملئكة قبيلا"]:
    if f not in v92:
        errors.append(f"cache 17:92 inattendu ({f[:30]})")
for f in ["أو يكون لك بيت من زخرف أو ترقى فى لسماء ولن نؤمن لرقيك حتى تنزل علينا كتبا نقرؤه",
          "قل سبحان ربى هل كنت إلا بشرا رسولا"]:
    if f not in v93:
        errors.append(f"cache 17:93 inattendu ({f[:30]})")
ar34 = dict((i, t) for i, t in cache["34"]["ar"])
if "عليهم كسفا من لسماء" not in bare(ar34[9]):
    errors.append("cache 34:9 inattendu (la menace « nusqiṭ ʿalayhim kisafan »)")
ar2 = dict((i, t) for i, t in cache["2"]["ar"])
if "يتفجر منه لأنهر" not in bare(ar2[74]):
    errors.append("cache 2:74 inattendu (lemme « yatafaǧǧaru »)")
if "فهو لمهتد" not in bare(ar17[97]):
    errors.append("cache 17:97 inattendu (lemme « fa-huwa l-muhtadī »)")

# préparation de la leçon suivante au DOM
if "94 à 98" not in norm or "89 - 49" not in norm:
    errors.append("préparation : les versets 94-98 (imprimé « 89 - 49 ») absents du DOM")
for f in ["awliyāʾ", "ǧahannam", "ḫabat", "al-muhtadī", "fa-huwa l-muhtadī", "17 :97"]:
    if f not in norm:
        errors.append(f"préparation : lemme attendu absent : {f}")

# citations hors rasm — interdites au corps après l'évaluation
# (17:86-89 = leçon précédente 730 ; 17:94-98 = leçon suivante 732)
body = norm.split("<h2>L’évaluation", 1)[1]
for pat, label in [
    (r"emporterions", "al-Isrāʾ 17:86 (leçon précédente — non portée)"),
    (r"contre Nous de défenseur", "al-Isrāʾ 17:86 (leçon précédente — non portée)"),
    (r"Hors une miséricorde", "al-Isrāʾ 17:87 (leçon précédente — non portée)"),
    (r"se concertaient", "al-Isrāʾ 17:88 (leçon précédente — non portée)"),
    (r"fussent-ils", "al-Isrāʾ 17:88 (leçon précédente — non portée)"),
    (r"toute parabole", "al-Isrāʾ 17:89 (leçon précédente — non portée)"),
    (r"hormis la dénégation", "al-Isrāʾ 17:89 (leçon précédente — non portée)"),
    (r"le guide leur est parvenu", "al-Isrāʾ 17:94 (leçon suivante — non portée)"),
    (r"envoie-t-Il un être humain", "al-Isrāʾ 17:94 (leçon suivante — non portée)"),
    (r"marchant tranquillement", "al-Isrāʾ 17:95 (leçon suivante — non portée)"),
    (r"Ange-Messager", "al-Isrāʾ 17:95 (leçon suivante — non portée)"),
    (r"Allah suffit comme témoin", "al-Isrāʾ 17:96 (leçon suivante — non portée)"),
    (r"Parfaitement Connaisseur", "al-Isrāʾ 17:96 (leçon suivante — non portée)"),
    (r"traînés sur leurs visages", "al-Isrāʾ 17:97 (leçon suivante — non portée)"),
    (r"aveugles, muets et sourds", "al-Isrāʾ 17:97 (leçon suivante — non portée)"),
    (r"la flamme ardente", "al-Isrāʾ 17:97 (leçon suivante — non portée)"),
    (r"ossements et poussière", "al-Isrāʾ 17:98 (leçon suivante — non portée)"),
    (r"une nouvelle création", "al-Isrāʾ 17:98 (leçon suivante — non portée)"),
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
print("PASS : leçon 731 — versets 90-93 rendus sur le rasm warš du cache (la source, "
      "le jardin de palmiers et de vignes, la chute du ciel en morceaux « kamā zaʿamt », "
      "la venue d'Allah et des anges en face, la maison d'ornements, la montée au ciel "
      "et le livre, « qul subḥāna rabbī »), les gloses lexicales (le jardin — verger "
      "abondant en arbres —, qbīlan — faire face et voir à découvert —, zuḫruf l'or, "
      "ta-rqā gravir sur une échelle), le hadith des demandes (ʿUtbā, Šayba, ʿAbd Allāh "
      "b. Abī Umayya, an-Naḍr b. al-Ḥāriṯ — la royauté, les biens, le soin —, « je "
      "patienterai à l'ordre d'Allah », « tout cela relève d'Allah »), les six sortes "
      "de miracles (les lectures du jaillissement — Ḥamza et al-Kisāʾī « ta-fǧura » —, "
      "« yatafaǧǧaru » au rasm al-Baqara 74, le minbūʿ hyperbolique, le jardin fixé à "
      "La Mecque en lieu aride avec le tafǧīran et le ḫilālahā — référence dégradée "
      "déclarée —, « kamā zaʿamt » et la menace 34:9, les trois glosses de qbīlan — "
      "le garant et la garantie, nul pareil —, le zuḫruf et la lecture d'Ibn Masʿūd "
      "avec Muǧāhid, les degrés du ciel, ar-ruqī, l'air élevé et le ciel connu), la "
      "disculpation (l'interrogation négative, la Loi et la seule transmission, la "
      "lecture-rapport, les assimilateurs — viendrait et partirait —, la mise en "
      "demeure des gens et non d'Allah, le miracle unique et l'obstination, Mafātīḥ "
      "al-ġayb — pagination dégradée déclarée), les finalités (3), l'exploitation "
      "d'Ibn Hišām (la réponse et la réplique — ar-Raḥmān, les filles d'Allah, les "
      "quatre anges — tête, bande du milieu et membres finaux dégradés, déclarés), la "
      "préparation 94-98 au DOM (imprimé « 89 - 49 » inversé, lu 94 et 98 par "
      "l'étiquette du livre — awliyāʾ, ǧahannam, ḫabat, al-muhtadī et 17:97 au rasm "
      "du cache), aucune citation hors rasm (17:86-89 interdits au corps après "
      "l'évaluation — leçon précédente ; 17:94-98 interdits — leçon suivante), 0 "
      "arabe résiduel.")

if __name__ == "__main__":
    sys.exit(0)

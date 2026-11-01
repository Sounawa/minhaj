#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Minhāj — contrôle coranique de la leçon 729 (tafsir-5ep, Isrāʾ 82-85).
Vérifie : rendus français des versets 82-85 (rasm warš du cache), les gloses
lexicales (šākila la voie et la doctrine ressemblant à l'état en la guidance et
l'égarement), les noms portés (Ibn ʿAṭiyya, ar-Rāzī Mafātīḥ al-ġayb 12/93,
al-Bayḍāwī Anwār at-tanzīl 3/562, Ibn ʿĀmir, Ibn ʿAbbās, Qatāda, Muǧāhid,
Ibn Zayd, Ibn Masʿūd, al-Aʿmaš, an-Naḍr ibn al-Ḥāriṯ, ʿUqba ibn Abī Muʿayṭ,
Jibrīl, Jésus fils de Marie, Ibn ʿAǧība al-Baḥr al-madīd 3/722), les matières
(les sens du « de » — genre, commencement de finalité, tabʿīḍ —, la descente
partitionnée, les deux sens de la guérison — levée du doute/couverture du cœur
et ruqā/taʿwīṯ —, la chaîne rage-colère-haine-rancune, l'amour du bas-monde,
l'exemple de la généralisation hyperbolique, l'istiʿāra de « aġwaḍ », la
lecture d'Ibn ʿĀmir et le vers du coureur, les deux verbes distincts, les sens
de « šākila » et l'avis le plus juste, l'esprit et les Juifs — le champ près
de Médine, la ruine, la Torah, l'ʿasīb, « je crus que l'inspiration lui
venait » —, le récit mecquoise — les trois questions, « demain je vous en
informerais », les quinze jours —, le nom de genre et l'intraitable, Jibrīl,
Jésus, le Coran, les deux lectures de « min amri », les qirāʾāt ūtū/ūtītum et
les destinataires, la science minime ajoutée à la science d'Allah), la
préparation 86-89 au DOM (chiffres imprimés « 68 - 98 » inversés, lus 86 et 89),
l'absence de citations hors rasm (17:78-81 = leçon précédente ; 17:86-89 =
leçon suivante — interdites au corps après l'évaluation), 0 arabe résiduel.
Espaces typographiques (NNBSP/insécables) introduits par l'auto-fix de
qa-lesson normalisés avant appariement."""
import json
import re
import sys

HTML = "scripts-translate/tr-tmp/pdf-mut23h3c-729.html"
html = open(HTML, encoding="utf-8").read()
norm = html.replace("\u202f", " ").replace("\u00a0", " ")
errors = []

for frag in [
    "Et Nous faisons descendre du Coran ce qui est guérison et miséricorde pour les croyants",
    "et il n’augmente les injustes qu’en perdition",
    "Et quand Nous comblons l’homme de faveur, il se détourne et s’écarte de côté",
    "et quand le mal le touche, il est désespérant",
    "chacun agit selon sa disposition",
    "ton Seigneur connaît mieux celui qui est le mieux guidé en un chemin",
    "ils t’interrogent au sujet de l’esprit",
    "l’esprit relève de l’ordre de mon Seigneur",
    "il ne vous a été donné de la science que peu",
]:
    if frag not in norm:
        errors.append(f"rendu attendu absent : {frag[:55]}")

if not re.search(r"»\s*\(82-85\)", norm):
    errors.append("repère de plage (82-85) absent")

for frag in [
    "sa voie et sa doctrine",
    "la guidance et en l’égarement",
    "l’indication du genre",
    "le commencement de la finalité",
    "parti-tout (tabʿīḍ)",
    "Ibn ʿAṭiyya a dit",
    "sa descente est partitionnée",
    "pièce par pièce",
    "levée du doute",
    "couverture du cœur",
    "les incantations (ruqā)",
    "l’usage talismanique (taʿwīṯ)",
    "la rage, la colère, la haine et la rancune",
    "Mafātīḥ al-ġayb d’ar-Rāzī : 12/93",
    "l’amour du bas-monde",
    "il n’y a pas de bien dans les amis, ni de fidélité chez les gens",
    "le mécréant exagère en le détournement, et le pécheur en prend sa part",
    "il se détourna, et Allah se détourna de lui",
    "métaphore (istiʿāra)",
    "Ibn ʿĀmir a lu seul",
    "l’inversion de la hamza après l’alif",
    "Son omoplate s’est détournée dans le flanc du gauche",
    "deux verbes distincts",
    "l’aversion et le parti pris",
    "la distance et la séparation",
    "dis, ô Muḥammad",
    "Muǧāhid dit",
    "Ibn ʿAbbās dit : selon son côté",
    "Qatāda dit : selon son côté et selon ce qu’il entend",
    "Ibn Zayd dit : selon sa religion",
    "le dire d’Ibn ʿAbbās et de Qatāda",
    "Anwār at-tanzīl wa-asrār at-taʾwīl d’al-Bayḍāwī : 3/562",
    "les esprits ont un rôle dans les actes émanant de l’homme",
    "Ibn Masʿūd rapporta",
    "un champ près de Médine",
    "auprès d’une ruine",
    "dans la Torah",
    "appuyé sur une tige de palmier (ʿasīb)",
    "je crus que l’inspiration lui venait",
    "l’āya est mecquoise",
    "an-Naḍr ibn al-Ḥāriṯ et ʿUqba ibn Abī Muʿayṭ",
    "gens de la Caverne",
    "Dhū l-Qarnayn",
    "demain je vous en informerai",
    "quinze jours",
    "l’esprit qui est dans les corps vivants",
    "nom de genre",
    "l’intraitable qui n’admet point d’interprétation",
    "l’esprit demandé est Jibrīl",
    "Ibn ʿAbbās, lui, s’abstenait de le dévoiler",
    "Jésus fils de Marie",
    "l’esprit est le Coran",
    "nom de genre pour les affaires",
    "une addition du créé au Créateur",
    "masdar de « il commande »",
    "Ibn Masʿūd et al-Aʿmaš lurent",
    "et ce qui leur fut donné",
    "et ce qui vous fut donné",
    "les interrogateurs seuls",
    "les Juifs en leur ensemble",
    "le monde entier",
    "« que peu »",
    "qui enveloppe toute chose",
    "guérison des maladies des cœurs",
    "la dispute vaine et du dialogue improductif",
    "leurs inclinations et leurs natures",
    "Ibn ʿAǧība",
    "al-Baḥr al-madīd fī tafsīr al-Qurʾān al-maǧīd",
    "3/722",
    "il se met à supplier",
    "purifier mon âme",
]:
    if frag not in norm:
        errors.append(f"glose/nom attendu absent : {frag[:55]}")


def bare(t: str) -> str:
    return re.sub(r"[\u064B-\u065F\u0670\u06D6-\u06ED\u0640\u0671]", "", t)


cache = json.load(open("scripts-translate/quran-cache.json", encoding="utf-8"))
ar17 = dict((i, t) for i, t in cache["17"]["ar"])
v82, v83, v84, v85 = (ar17[i] for i in range(82, 86))
b82, b83, b84, b85 = (bare(v) for v in (v82, v83, v84, v85))
for f in ["وننزل من لقرءان ما هو شفاء ورحمة للمؤمنين", "ولا يزيد لظلمين إلا خسارا"]:
    if f not in b82:
        errors.append(f"cache 17:82 inattendu ({f[:35]})")
for f in ["وإذا أنعمنا على لإنسن أعرض ونا بجانبه", "وإذا مسه لشر كان يوسا"]:
    if f not in b83:
        errors.append(f"cache 17:83 inattendu ({f[:35]})")
for f in ["قل كل يعمل على شاكلته فربكم أعلم بمن هو أهدى سبيلا"]:
    if f not in b84:
        errors.append(f"cache 17:84 inattendu ({f[:35]})")
for f in ["ويسلونك عن لروح", "قل لروح من أمر ربى", "وما أوتيتم من لعلم إلا قليلا"]:
    if f not in b85:
        errors.append(f"cache 17:85 inattendu ({f[:35]})")

# préparation de la leçon suivante au DOM
if "86 à 89" not in norm or "68 - 98" not in norm:
    errors.append("préparation : les versets 86-89 (imprimé « 68 - 98 ») absents du DOM")

# citations hors rasm — interdites au corps après l'évaluation
# (17:78-81 = leçon précédente 728 ; 17:86-89 = leçon suivante 730)
body = norm.split("<h2>L’évaluation", 1)[1]
for pat, label in [
    (r"au déclin du soleil jusqu’à l’obscurité", "al-Isrāʾ 17:78 (leçon précédente — non portée)"),
    (r"comme surérogatoire pour toi", "al-Isrāʾ 17:79 (leçon précédente — non portée)"),
    (r"une station louangée", "al-Isrāʾ 17:79 (leçon précédente — non portée)"),
    (r"fais-moi entrer par une entrée de vérité", "al-Isrāʾ 17:80 (leçon précédente — non portée)"),
    (r"La vérité est venue et le faux s’est évanoui", "al-Isrāʾ 17:81 (leçon précédente — non portée)"),
    (r"ce que nous avons trouvé", "al-Isrāʾ 17:86 (leçon suivante — non portée)"),
    (r"sept des répét", "al-Isrāʾ 17:87 (leçon suivante — non portée)"),
    (r"les hommes et les djinns", "al-Isrāʾ 17:88 (leçon suivante — non portée)"),
    (r"de tout exemple", "al-Isrāʾ 17:89 (leçon suivante — non portée)"),
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
print("PASS : leçon 729 — versets 82-85 rendus sur le rasm warš du cache (la guérison et "
      "la miséricorde pour les croyants contre la perdition des injustes, l’homme comblé "
      "qui se détourne et s’écarte de côté et le désespérant à l’épreuve, l’œuvre selon la "
      "disposition et le Seigneur connaissant le mieux guidé, l’esprit relevant de l’ordre "
      "du Seigneur et la science minime), les gloses lexicales (šākila la voie et la "
      "doctrine ressemblant à l’état en la guidance et l’égarement), le tafsīr de la "
      "guérison (les sens du « de » — indication du genre, commencement de finalité, "
      "tabʿīḍ d’Ibn ʿAṭiyya et la descente partitionnée —, les deux sens de la guérison — "
      "la levée du doute et la couverture du cœur, la ruqā et le taʿwīṯ —, la perdition "
      "des injustes et la chaîne rage-colère-haine-rancune de Mafātīḥ al-ġayb 12/93, "
      "l’amour du bas-monde et l’exemple de la généralisation hyperbolique, le hadith au "
      "sujet du croyant tête dégradée, l’istiʿāra de « aġwaḍ », la lecture d’Ibn ʿĀmir et "
      "le vers du coureur, les deux verbes distincts d’Ibn ʿAṭiyya, les sens de šākila — "
      "Muǧāhid, Ibn ʿAbbās, Qatāda, Ibn Zayd — et l’avis le plus juste, al-Bayḍāwī "
      "3/562), le tafsīr de l’esprit (les Juifs et le récit d’Ibn Masʿūd — le champ près "
      "de Médine, la ruine, la Torah, l’ʿasīb, « je crus que l’inspiration lui venait » —, "
      "le récit mecquoise — an-Naḍr ibn al-Ḥāriṯ et ʿUqba ibn Abī Muʿayṭ, les trois "
      "questions, « demain je vous en informerai », les quinze jours —, le nom de genre "
      "et l’intraitable, Jibrīl, Jésus fils de Marie, le Coran, les deux lectures de « min "
      "amri », les qirāʾāt ūtū/ūtītum d’Ibn Masʿūd et al-Aʿmaš, les destinataires et la "
      "science minime ajoutée à la science d’Allah), les finalités (3), l’exploitation "
      "d’Ibn ʿAǧība al-Baḥr al-madīd 3/722 (le blâme de l’enflé de la faveur et du "
      "désespérant — tête et transition dégradées, déclarées), la préparation 86-89 au "
      "DOM (imprimé « 68 - 98 » inversé, lu 86 et 89 par l’étiquette du livre), aucune "
      "citation hors rasm (17:78-81 interdits au corps après l’évaluation — leçon "
      "précédente ; 17:86-89 interdits — leçon suivante), 0 arabe résiduel.")

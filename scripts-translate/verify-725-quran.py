#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Minhāj — contrôle coranique de la leçon 725 (tafsir-5ep, Isrāʾ 66-69).
Vérifie : rendus français des versets 66-69 (rasm warš du cache), les gloses
lexicales (yuzǧī, yagsifu, qāṣifan, al-ḥāṣib, al-wakīl), les noms portés
(al-Bayḍāwī, Nāfiʿ/ʿĀṣim/Ibn ʿĀmir/Ḥamza/al-Kisāʾī, Abū Jaʿfar et Mujāhid,
le hadith de Ṣaḥīḥ Muslim), l'istiġrāq de « al-insān », la préparation 70-72
au DOM, l'absence de citations hors rasm (17:61-65 = leçon précédente,
interdites au corps après l'évaluation), 0 arabe résiduel."""
import json
import re
import sys

HTML = "scripts-translate/tr-tmp/pdf-mut23h3c-725.html"
html = open(HTML, encoding="utf-8").read()
errors = []

for frag in [
    "Celui qui fait voguer pour vous les navires en mer",
    "afin que vous alliez à la recherche de quelque grâce de Sa part",
    "Il est certes Miséricordieux envers vous",
    "Et quand le mal vous touche en mer",
    "ceux que vous invoquiez en dehors de Lui se perdent",
    "puis, quand Il vous sauve et vous ramène à terre, vous vous détournez",
    "et l’homme reste fort ingrat",
    "Êtes-vous à l’abri de ce qu’Il vous fasse engloutir par un pan de terre",
    "ou qu’Il envoie contre vous un ouragan de pierres",
    "et que vous ne trouviez alors aucun protecteur",
    "Ou êtes-vous à l’abri de ce qu’Il vous y ramène une autre fois",
    "qu’Il déchaîne contre vous un vent qui brise tout",
    "puis vous fasse noyer à cause de votre dénégation",
    "vous ne trouveriez personne pour vous défendre contre Nous",
]:
    if frag not in html:
        errors.append(f"rendu attendu absent : {frag[:55]}")

if not re.search(r"»\s*\(66-69\)", html):
    errors.append("repère de plage (66-69) absent")

for frag in [
    "le poussage — le déroulement du déplacement",
    "disparaître dans la terre",
    "un vent au son violent",
    "le fléau qui lance la grêle et les pierres",
    "ce qui frappa le peuple de Loth",
    "le lancer de cailloux — les petites pierres",
    "celui qui prend en charge les affaires",
    "Anwār at-tanzīl wa-asrār at-taʾwīl d’al-Bayḍāwī",
    "Nāfiʿ, ʿĀṣim, Ibn ʿĀmir, Ḥamza et al-Kisāʾī",
    "Abū Jaʿfar et Mujāhid",
    "Ṣaḥīḥ Muslim, livre de la fructification",
    "l’istiġrāq — l’inclusion totale",
    "dénégateur des bienfaits",
    "la bāʾ de cause",
]:
    if frag not in html:
        errors.append(f"glose/nom attendu absent : {frag[:55]}")

def bare(t: str) -> str:
    return re.sub(r"[\u064B-\u065F\u0670\u06D6-\u06ED\u0640\u0671]", "", t)

cache = json.load(open("scripts-translate/quran-cache.json", encoding="utf-8"))
ar17 = dict((i, t) for i, t in cache["17"]["ar"])
v66, v67, v68, v69 = (ar17[i] for i in range(66, 70))
b66, b67, b68, b69 = (bare(v) for v in (v66, v67, v68, v69))
for f in ["ربكم لذى يزجى لكم لفلك فى لبحر لتبتغوا من فضله", "إنه كان بكم رحيما"]:
    if f not in b66:
        errors.append(f"cache 17:66 inattendu ({f[:35]})")
for f in ["وإذا مسكم لضر فى لبحر ضل من تدعون إلا إياه",
          "فلما نجىكم إلى لبر أعرضتم", "وكان لإنسن كفورا"]:
    if f not in b67:
        errors.append(f"cache 17:67 inattendu ({f[:35]})")
for f in ["أفأمنتم أن يخسف بكم جانب لبر", "أو يرسل عليكم حاصبا ثم لا تجدوا لكم وكيلا"]:
    if f not in b68:
        errors.append(f"cache 17:68 inattendu ({f[:35]})")
for f in ["أم أمنتم أن يعيدكم فيه تارة أخرى", "فيرسل عليكم قاصفا من لريح فيغرقكم بما كفرتم",
          "ثم لا تجدوا لكم علينا به تبيعا"]:
    if f not in b69:
        errors.append(f"cache 17:69 inattendu ({f[:35]})")

# préparation de la leçon suivante au DOM
if "70 à 72" not in html:
    errors.append("préparation : les versets 70-72 absents du DOM")

# citations hors rasm — interdites au corps après l'évaluation (versets 61-65 : leçon précédente)
body = html.split("<h2>L’évaluation", 1)[1]
for pat, label in [
    (r"Prosternez-vous devant Adam", "al-Isrāʾ 17:61 (leçon précédente — non portée)"),
    (r"Me prosternerai-je", "al-Isrāʾ 17:61 (leçon précédente — non portée)"),
    (r"honoré au-dessus de moi", "al-Isrāʾ 17:62 (leçon précédente — non portée)"),
    (r"sa descendance, excepté", "al-Isrāʾ 17:62 (leçon précédente — non portée)"),
    (r"l’Enfer, une ample rétribution", "al-Isrāʾ 17:63 (leçon précédente — non portée)"),
    (r"Excite par ta voix", "al-Isrāʾ 17:64 (leçon précédente — non portée)"),
    (r"cavalerie et ton infanterie", "al-Isrāʾ 17:64 (leçon précédente — non portée)"),
    (r"aucun pouvoir sur eux", "al-Isrāʾ 17:65 (leçon précédente — non portée)"),
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
print("PASS : leçon 725 — versets 66-69 rendus sur le rasm warš du cache (les navires "
      "faits voguer en mer pour rechercher de Sa grâce, l’invocation en la détresse et "
      "l’évanouissement des invoqués, le sauvetage vers la terre et le détour de l’homme "
      "ingrat, l’engloutissement par un pan de terre et l’ouragan de pierres, le retour "
      "en mer une autre fois et le vent qui brise tout, la noyade à cause de la "
      "dénégation, nul défenseur contre Nous), les gloses lexicales (yuzǧī le poussage "
      "et le déroulement du déplacement, yagsifu disparaître dans la terre, qāṣifan un "
      "vent au son violent, al-ḥāṣib le fléau de la grêle et des pierres — le peuple de "
      "Loth —, al-ḥaṣb le lancer de cailloux, al-wakīl celui qui prend en charge les "
      "affaires), le tafsīr de la mer (la marchandise poussée et le vent doux, al-fulk "
      "collectif, la quête du gain et le pèlerinage, la contrainte des associateurs par "
      "l’argument, la détresse englobant la peur de la noyade, les idoles sans action "
      "dans les grandes épreuves et l’arrêt par le spectacle de la mer), l’istiġrāq de "
      "« al-insān » pour le genre, la bāʾ de cause et le mā de masdar, at-tabīʿ le "
      "défenseur et le hadith de Ṣaḥīḥ Muslim (livre de la fructification), les "
      "finalités (l’unicité, la sécurité garantie par Allah, la grâce qui n’a pas "
      "châtié comme ceux d’avant), la préparation 70-72 au DOM, aucune citation hors "
      "rasm (17:61-65 interdits au corps après l’évaluation), 0 arabe résiduel.")

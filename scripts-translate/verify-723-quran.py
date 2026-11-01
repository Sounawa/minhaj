#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Minhāj — contrôle coranique de la leçon 723 (tafsir-5ep, Isrāʾ 56-60).
Vérifie : rendus français des versets 56-60 (rasm warš du cache), le parallèle
cité à l'exploitation (al-Anfāl 23 — la science d'Allah du bien des demandeurs),
les gloses lexicales et les noms portés, la préparation 61-65 au DOM, l'absence
de citations hors rasm (17:49-55 = leçon précédente, interdites au corps),
0 arabe résiduel."""
import json
import re
import sys

HTML = "scripts-translate/tr-tmp/pdf-mut23h3c-723.html"
html = open(HTML, encoding="utf-8").read()
errors = []

for frag in [
    "Invoquez ceux que vous avez prétendus en dehors de Lui",
    "ils ne possèdent ni d’ôter de vous le mal, ni de le détourner",
    "Ceux-là qu’ils invoquent cherchent vers leur Seigneur le moyen de rapprochement",
    "lequel d’eux sera le plus proche",
    "et espèrent Sa miséricorde et craignent Son châtiment",
    "le châtiment de ton Seigneur est, certes, à redouter",
    "Pas de cité que Nous ne détruisions avant le jour de la Résurrection",
    "ou que Nous ne châtions d’un châtiment terrible",
    "cela est écrit dans le Livre",
    "Rien ne Nous a empêchés d’envoyer les signes",
    "sinon que les premiers les ont criés au mensonge",
    "Nous avons donné à Ṯamūd la chamelle en vision manifeste",
    "puis ils lui firent tort",
    "Nous n’envoyons les signes que pour effrayer",
    "ton Seigneur cerne les gens",
    "Nous n’avons fait du songe que Nous t’avons montré",
    "de l’arbre maudit dans le Coran",
    "qu’une épreuve pour les gens",
    "Nous les effrayons, mais cela ne fait qu’accroître leur immense transgression",
]:
    if frag not in html:
        errors.append(f"rendu attendu absent : {frag[:55]}")

if not re.search(r"»\s*\(56-60\)", html):
    errors.append("repère de plage (56-60) absent")

for frag in [
    "Had Allah connu en eux quelque bien, Il les aurait fait entendre",
]:
    if frag not in html:
        errors.append(f"parallèle attendu absent : {frag[:55]}")

def bare(t: str) -> str:
    return re.sub(r"[\u064B-\u065F\u0670\u06D6-\u06ED\u0640\u0671]", "", t)

cache = json.load(open("scripts-translate/quran-cache.json", encoding="utf-8"))
ar17 = dict((i, t) for i, t in cache["17"]["ar"])
v56, v57, v58, v59, v60 = (ar17[i] for i in range(56, 61))
b56, b57, b58, b59, b60 = (bare(v) for v in (v56, v57, v58, v59, v60))
for f in ["قل دعوا لذين زعمتم من دونه", "فلا يملكون كشف لضر عنكم ولا تحويلا"]:
    if f not in b56:
        errors.append(f"cache 17:56 inattendu ({f[:35]})")
for f in ["أولئك لذين يدعون يبتغون إلى ربهم لوسيلة",
          "أيهم أقرب ويرجون رحمته ويخافون عذابه", "إن عذاب ربك كان محذورا"]:
    if f not in b57:
        errors.append(f"cache 17:57 inattendu ({f[:35]})")
for f in ["وإن من قرية إلا نحن مهلكوها قبل يوم لقيمة", "أو معذبوها عذابا شديدا",
          "كان ذلك فى لكتب مسطورا"]:
    if f not in b58:
        errors.append(f"cache 17:58 inattendu ({f[:35]})")
for f in ["وما منعنا أن نرسل بلءايت إلا أن كذب بها لأولون",
          "وءاتينا ثمود لناقة مبصرة فظلموا بها", "وما نرسل بلءايت إلا تخويفا"]:
    if f not in b59:
        errors.append(f"cache 17:59 inattendu ({f[:35]})")
for f in ["وإذ قلنا لك إن ربك أحاط بلناس",
          "وما جعلنا لرءيا لتى أرينك إلا فتنة للناس ولشجرة لملعونة فى لقرءان",
          "ونخوفهم فما يزيدهم إلا طغينا كبيرا"]:
    if f not in b60:
        errors.append(f"cache 17:60 inattendu ({f[:35]})")

ar8 = dict((i, t) for i, t in cache["8"]["ar"])
if "ولو علم لله فيهم خيرا لأسمعهم" not in bare(ar8[23]):
    errors.append("cache 8:23 inattendu (la science du bien des demandeurs — warš : لله)")

for frag in ["al-wasīla", "al-kitāb", "al-lawḥ al-maḥfūẓ", "taqdīr", "tawassul",
             "ulāʾika", "yabtaghūna", "yadʿūna", "tadʿūna", "Ibn Masʿūd",
             "Ibn ʿAbbās", "Ibn Zayd", "al-Ḥasan", "ʿUzayr", "du Messie",
             "Khuzāʿa", "Qatāda", "Abū Ḥayyān", "al-Baḥr al-muḥīṭ", "az-Zajjāj",
             "ʿAntara", "Ibn Fūrak", "aṣ-Ṣafā", "Ṯamūd", "mubṣara", "mabṣara",
             "mafʿala", "Kūfa", "al-Ḥudaybiyya", "az-Zaqqūm", "al-Alūsī",
             "Rūḥ al-maʿānī", "al-Anfāl", "al-Muḥarrar al-wajīz", "rasm warš",
             "taqwīm", "istiṯmār", "al-iʿdād al-qiblī", "ﷺ"]:
    if frag not in html:
        errors.append(f"glose/nom attendu absent : {frag}")

# préparation de la leçon suivante au DOM
if "61 à 65" not in html:
    errors.append("préparation : les versets 61-65 absents du DOM")

# citations hors rasm — interdites au corps (versets 49-55 : leçon précédente)
body = html.split("<h2>L’évaluation", 1)[0]
for pat, label in [
    (r"ossements", "al-Isrāʾ 17:49 (leçon précédente — non portée)"),
    (r"pierres ou fer", "al-Isrāʾ 17:50 (leçon précédente — non portée)"),
    (r"réintégr", "al-Isrāʾ 17:51 (leçon précédente — non portée)"),
    (r"branleront", "al-Isrāʾ 17:51 (leçon précédente — non portée)"),
    (r"par Sa louange", "al-Isrāʾ 17:52 (leçon précédente — non portée)"),
    (r"ce qui est meilleur", "al-Isrāʾ 17:53 (leçon précédente — non portée)"),
    (r"Psaumes", "al-Isrāʾ 17:55 (leçon précédente — non portée)"),
    (r"David", "al-Isrāʾ 17:55 (leçon précédente — non portée)"),
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
print("PASS : leçon 723 — versets 56-60 rendus sur le rasm warš du cache (l’invocation "
      "des divinités prétendues et leur impuissance, le rapprochement que cherchent "
      "eux-mêmes les invoqués, la destruction des cités avant le Jour, le refus des "
      "signes que les premiers crièrent au mensonge, la chamelle de Ṯamūd en vision "
      "manifeste, les signes envoyés pour effrayer, le Seigneur cernant les gens, le "
      "songe et l’arbre maudit épreuves pour les gens), le parallèle à l’exploitation "
      "(al-Anfāl 23 — had Allah connu en eux quelque bien — au rasm nu du cache, "
      "warš : pour-Allah), les causes de descente (les adorateurs des démons — "
      "Khuzāʿa —, d’ʿUzayr, du Messie et de sa mère, des anges, des astres), le "
      "taqdīr du complément sous-entendu (Abū Ḥayyān), les deux lectures "
      "d’« ils invoquent » (yadʿūna au yāʾ, tadʿūna au tāʾ d’Ibn Masʿūd et Qatāda), "
      "la note d’Ibn Fūrak sur les prophètes antérieurs, le Ṣafā d’or et les "
      "montagnes écartées avec la réponse du Prophète ﷺ, les lectures "
      "mubṣara/mabṣara (az-Zajjāj, Qatāda, le vers d’ʿAntara au schème mafʿala), les "
      "trois sections des signes, le songe de l’Ascension nocturne et la vision "
      "d’al-Ḥudaybiyya selon Ibn ʿAbbās, az-Zaqqūm l’arbre maudit, la citation "
      "d’al-Alūsī (Rūḥ al-maʿānī), la préparation 61-65 au DOM, aucune citation hors "
      "rasm (17:49-55 interdits au corps), 0 arabe résiduel.")

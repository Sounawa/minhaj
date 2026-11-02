#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Minhāj — contrôle coranique et de contenu de la leçon 752 (tafsir-5ep,
sūrat al-Kahf v46-48 de l'imprimé warš — quatorzième leçon du second livre,
pages 102-109 du manuel miroir tafsir-3-thanawi). La plage imprimée (46-48)
correspond aux āyāt 47-49 du cache canonique ḥafṣ (décalage de un, tranché
R511). Les trois āyāt sont rendues en français sur le cache (présence
vérifiée) ; les āyāt 1-46 (leçons 739-751) et 50-53 (leçon 753) sont
interdites de double rendu ; le rasm nu du cache interdit au corps (0 arabe —
FR-seule). Leçon produite en PARALLÈLE v4 (claim trace-2137) avec la 753
(sous-agent R514)."""
import json
import re
import sys

HTML = "tr-tmp/lesson-752-fr.html"
html = open(HTML, encoding="utf-8").read()
norm = re.sub(r"[ \u202f\u00a0]+", " ", html.replace("&nbsp;", "\u00a0"))
errors = []

# 1. structure et marqueurs
for frag in [
    "Source du cours",
    "Quatorzième leçon du second livre du parcours",
    "pages 102 à 109 de l’imprimé miroir",
    "1_20220304_20220304_2251",
    "p.102 ouvre la leçon 14",
    "les objectifs de la leçon 15 ouvrent p.110",
    "Les objectifs de la leçon",
    "Le tamhīd",
    "Le commentaire",
    "La glose",
    "L’extraction des thèmes des āyāt",
    "Premièrement",
    "Deuxièmement",
    "Troisièmement",
    "Les subtilités et les bienfaits",
    "L’orthographe du muṣḥaf et la pause",
    "L’évaluation",
    "L’exploitation",
    "la page imprimée 109",
    "jamais devinée",
    "interdites de double rendu",
    "plage imprimée (46-48) correspond aux āyāt 47 à 49 du cache canonique",
]:
    if frag.lower() not in norm.lower():
        errors.append(f"fragment attendu absent : {frag[:55]}")

# 2. les āyāt 47-49 rendus du cache — présence (3 rendus + 3 numéros)
cache = json.load(open("scripts-translate/quran-cache.json", encoding="utf-8"))
fr18 = {n: t for n, t in cache["18"]["fr"]}
rendus = [fr18[n] for n in (47, 48, 49)] + ["(47)", "(48)", "(49)"]
rendus_norm = [r.replace("'", "’").replace(" ", "") for r in rendus]
compact = norm.replace(" ", "")
for r in rendus_norm:
    if r not in compact:
        errors.append(f"rendu coranique attendu absent : {r[:55]}")

# 3. contenu attendu (confrontation au manuel p.102-109 — glose, lectures, exégètes)
contenu = [
    "an-Naḥḥās",
    "Nāfiʿ et les Kufans lurent",
    "Ibn Kaṯīr, Abū ʿAmr et Ibn ʿĀmir",
    "Ibn Muḥayṣin et Muǧāhid",
    "at-Takwīr 3",
    "an-Naml 88",
    "des collines et des arbres",
    "l’imām al-Qurṭubī",
    "ses montagnes furent déracinées",
    "ses constructions démolies, ses fruits cueillis",
    "majāz mursal",
    "al-Baḥr al-Muḥīṭ",
    "le torrent passa et la laissa",
    "les tresses [ġadāʾir] de la femme",
    "les pieux et les pervers d’entre eux",
    "les djinns et les humains, les premiers et les derniers",
    "al-Muṭaffifīn 6",
    "le jour où les gens se tiendront debout devant le Seigneur des mondes",
    "al-Faǧr 22",
    "rang par rang",
    "Muqātil",
    "comme les rangs en la ṣalāt",
    "l’appelant se fera entendre d’eux, et le regard les percera",
    "cent vingt rangs",
    "nus-pieds, nus, non circoncis",
    "une omission qu’exige le dire et qu’embellit la concision",
    "la création première est démonstration du retour",
    "un nom d’espèce",
    "un livre unique",
    "al-Isrāʾ 71",
    "son livret à sa droite",
    "du châtiment sans fin",
    "La plainte des criminels ne porte, en vérité, que sur l’inventaire",
    "hélas, le regret de ce que nous aurons négligé",
    "le véniel est ce qui est en deçà de l’association",
    "Saʿd b. Ǧunāda",
    "l’expédition de Ḥunayn",
    "Rassemblez du bois",
    "jusqu’à le perdre",
    "antithèse d’affirmation",
    "un majāz de l’intellect",
    "les gardiens-scribes d’entre les anges",
    "Āl ʿImrān 30",
    "le Juge qui ne faillit point",
    "an-Nisāʾ 40",
    "renvoi imprimé inversé « 04 », tranché",
    "al-Anbiyāʾ 47",
    "renvoi imprimé inversé « 74 », tranché",
    "Ibn ʿAṭiyya",
    "al-qamarān",
    "al-ʿumārān",
    "l’examen de soi",
    "belle attente de Dieu",
    "Abū ʿAmr al-Baṣrī et al-Kisāʾī",
    "s’arrête sur le lām",
    "suivre la rasm du muṣḥaf en la pause",
    "Asmāʾ bt. ʿUmays",
    "son Musnad",
    "par pudeur",
    "s’inscrive mensongin le mensongin",
    "La pudeur est-elle une justification du mensonge",
]
for c in contenu:
    if c.lower() not in norm.lower():
        errors.append(f"contenu attendu absent : {c[:55]}")

# 4. rendus interdits (āyāt 1-46 livrées leçons 739-751 ; 50-53 leçon 753)
interdits = [
    "Louange à Dieu qui a fait descendre sur Son serviteur",
    "les jeunes gens se retirèrent",
    "Donne-leur l’exemple de deux hommes",
    "que ne dis-tu",
    "Et sa récolte fut détruite",
    "Les biens et les enfants sont l’ornement",
    "les bonnes œuvres qui persistent ont auprès de ton Seigneur",
    "là où les montagnes se sont affermies",
    "Et ils seront présentés en rangs devant ton Seigneur. «Vous voilà venus",
    "qu’ils soient cependant cenés",
    "quiconque attend d’être rétribué par le bien",
]
interdits_norm = [r.replace("'", "’") for r in interdits]
for probe in interdits_norm:
    # la matière 47-49 est licite : rendu intégral du cache exclu du ban
    if probe in norm and probe not in [fr18[n].replace("'", "’") for n in (47, 48, 49)]:
        errors.append(f"rendu hors matière présent : {probe[:50]}")

rasm_18 = {n: t for n, t in cache["18"]["ar"]}
for n in range(1, 50):
    t = rasm_18[n]
    probes = [t, t.replace(" ", "")]
    ok = any(p in norm.replace(" ", "") for p in probes) or t in norm
    if ok:
        errors.append(f"rasm arabe interdit présent au corps (āya 18:{n})")

# 5. 0 arabe résiduel (ﷺ U+FDFA exempté, convention du corpus)
ARABIC = re.compile(r"[\u0600-\u06FF\u0750-\u077F\u08A0-\u08FF\uFB50-\uFDF9\uFDFB-\uFDFF\uFE70-\uFEFF]")
resid = ARABIC.findall(norm)
if resid:
    errors.append(f"arabe résiduel : {len(resid)} caractère(s), ex. {[c for c in resid[:5]]}")

# 6. typographie
if "'" in html:
    errors.append("apostrophe droite présente")
if html.count("«") != html.count("»"):
    errors.append(f"guillemets non appariés : « {html.count('«')} vs » {html.count('»')}")

total = len(["Source du cours"]) + 22 + len(rendus) + len(contenu) + len(interdits) + 49 + 3
print(f"verify-752-quran : {total} contrôles — rendus {len(rendus)} + contenu {len(contenu)} + "
      f"interdits {len(interdits)} + rasm nu {49} + structure {22 + 1} + typo 3")
if errors:
    print("verify-752 FAIL :")
    for e in errors:
        print(" -", e)
    sys.exit(1)

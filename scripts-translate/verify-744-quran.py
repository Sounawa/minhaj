#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Minhāj — contrôle coranique et de contenu de la leçon 744 (tafsir-5ep,
sūrat al-Kahf v19-20 — sixième leçon du second livre, pages 44-49 du manuel
miroir tafsir-3-thanawi). Les āyāt 19-20 sont rendues en français sur le rasm
warš du cache (présence vérifiée) ; le périmètre est tranché par le contenu
(l'en-tête imprimé resté altéré en ses chiffres, tranché 19-20, convergence
avec la grille) ; le double rendu des āyāt 14-18 (leçons 741-743) est
interdit ; le rasm nu du cache interdit au corps (0 arabe — FR-seule) pour
TOUTES les āyāt voisines (6-9 leçon 740, 10-14 leçon 741, 15-16 leçon 742,
17-18 leçon 743)."""
import json
import re
import sys

HTML = "scripts-translate/tr-tmp/pdf-mut23h3c-744.html"
html = open(HTML, encoding="utf-8").read()
norm = re.sub(r"[ \u202f\u00a0]+", " ", html.replace("&nbsp;", "\u00a0"))
errors = []

# 1. structure et marqueurs
if "Source du cours" not in norm:
    errors.append("Source du cours absent du DOM")
for frag in [
    "Sixième leçon du second livre du parcours",
    "tafsir-3-thanawi_text.pdf",
    "mécanique R458",
    "jamais devinées",
    "Les objectifs de la leçon",
    "Le tamhīd",
    "Le commentaire",
    "Les subtilités et les bienfaits",
    "L’évaluation",
    "L’exploitation",
    "la présente passe l’a relue in extenso",
    "la quête de la leçon procède par l’extraction des thèmes des āyāt",
]:
    if frag.lower() not in norm.lower():
        errors.append(f"fragment attendu absent : {frag[:55]}")

# 2. les āyāt 19-20 rendues en français (rasm warš du cache) — présence
rendus = [
    "Et ainsi Nous les ressuscitâmes, afin qu’ils s’interrogent les uns les autres. L’un d’eux dit : combien avez-vous demeuré ?",
    "votre Seigneur sait mieux ce que vous avez demeuré : envoyez donc l’un de vous avec cette pièce d’argent qui est à vous vers la ville ; qu’il voie laquelle des nourritures est la plus pure, et qu’il vous en apporte de quoi subsister ; qu’il agisse avec douceur, et que nul homme ne soit informé de vous.",
    "Car s’ils se manifestaient à vous, ils vous lapideraient, ou vous ramèneraient en leur religion — et alors vous ne réussiriez jamais.",
    "(19-20)",
]
for r in rendus:
    if r not in norm:
        errors.append(f"rendu coranique attendu absent : {r[:55]}")

# 3. contenu
contenu = [
    "le mouvement frappé de sukūn",
    "l’aïlūla",
    "le lām de l’issue",
    "aṭ-Ṭabarī",
    "nul regard jeté sur eux",
    "de la désagrégation tout au long du temps",
    "de la moisissure au fil des jours",
    "Notre domination immense et Notre acte étonnant en Notre création",
    "accru de claire-voyance en l’affaire qui était la leur",
    "leur pureté de l’adoration des divinités",
    "Jāmiʿ al-bayān",
    "une équivoque portée sur le locuteur",
    "l’utilité de sa mention et de sa désignation faisant défaut",
    "l’histoire de Yūsuf",
    "réveillés d’un seul jet, ou de moments proches",
    "Ibn Kaṯīr",
    "combien dormîtes-vous",
    "un genre de balancement les avait saisis",
    "leur besoin de la nourriture et de la boisson",
    "Tafsīr al-Qurʾān al-ʿaẓīm",
    "leurs monnaies frappées",
    "de l’argent",
    "les lecteurs de la Médine, en général, et quelques Irakiens l’ont lu avec la wāw ouverte",
    "les lecteurs de la Kufa et de la Bassora",
    "quelques Meccains l’ont lu avec la rāʾ frappée et l’assimilation de la qāf dans le kāf",
    "des langues connues du propos des Arabes",
    "l’origine en cela est la wāw ouverte et la rāʾ et la qāf frappées",
    "en quête de l’allègement",
    "des dirhams avec eux, de leurs demeures, pour leur besoin",
    "votre ville de laquelle vous sortîtes",
    "l’alif et le lām étant du définiment",
    "elle embellit le bien et le purifie",
    "la plus abondante en nourriture",
    "le blé a purifié lorsqu’il abonde et croît",
    "al-Baḥr al-muḥīṭ",
    "adorateurs d’idoles",
    "leur bête immolée",
    "du regard de l’œil",
    "du regard du cœur",
    "une métaphore relâchée",
    "la métaphore par la suppression",
    "le lām de l’ordre",
    "en son achat de ce qu’il achète",
    "en son cheminement sur sa route",
    "en son entrée dans la ville",
    "az-Zamakhsharī",
    "jusqu’à ce qu’il ne fût point reconnu",
    "al-Kashshāf",
    "le lām frappé de sukūn",
    "Ḥasan",
    "que nul des gens ne soit informé de votre état ou de votre lieu",
    "les mécréants",
    "qu’ils montent sur vous et sachent votre bien",
    "au sens de l’a vaincu",
    "aṣ-Ṣaff",
    "az-Zaǧǧāǧ",
    "Ibn ʿAṭiyya a dit — qu’Allah lui fasse miséricorde : c’est le plus juste",
    "résolu à les tuer s’il les avait saisis",
    "contrariait la religion des gens",
    "père d’Ibrāhīm",
    "MARYAM : 46",
    "Nūḥ",
    "aš-Šuʿarāʾ : 116",
    "l’accord se faisant qu’il visait l’injure",
    "la réponse de la condition",
    "vous y ramèneraient de force",
    "à la mécréance après elle",
    "la transformation y est visée",
    "l’initiation de l’acte étant visée",
    "l’intensité de la mise en garde à ses compagnons",
    "exposés à l’épreuve dans leur religion",
    "les jeunes gens recherchaient le bon licite en leurs achats, leurs nourritures et leurs boissons",
    "en son gain, sa dépense, sa nourriture, sa boisson et en tous ses états",
    "l’imitation des prophètes envoyés",
    "des droits d’Allah, des droits de l’âme et de la société",
    "Allah taʿālā est Bon et n’agrée que le bon",
    "la délégation et de sa validité",
    "le consensus s’y étant porté",
    "la prise des causes avec la prudence et la circonspection",
    "Yaʿqūb",
    "Yūsuf : 67",
    "la réalité de la confiance en Allah, laquelle ne répugne point à la prise des causes aidantes",
    "et par quoi est-elle nommée",
    "des moyens concrets pour l’appliquer en ma vie",
    "la valeur morale et éducative",
    "du jugement de la délégation depuis l’āya",
    "al-Suyūṭī",
    "des moitiés selon des considérations",
    "le compte des sūras",
    "sūrat aš-Šuʿarāʾ",
    "al-Itqān fī ʿulūm al-Qurʾān",
    "la fin de l’information d’Allah aux gens au sujet des gens de la Caverne",
    "les fins figurant dans les āyāt",
    "la page 50",
    "la page imprimée 49",
    "(21-24)",
    "la leçon 28 d’Isrāʾ",
]
for c in contenu:
    if c not in norm:
        errors.append(f"contenu attendu absent : {c[:55]}")

# 4. ABSENCE — rendus des āyāt des leçons voisines (14-18 livrés en 741-743,
#    6-9 en 740) ; rasm nu du cache interdit pour toutes les āyāt
for probe in [
    "C’est Nous qui te rapportons leur récit en vérité",
    "Et Nous affermîmes leurs cœurs",
    "Voici notre peuple",
    "Et lorsque vous les aurez quittés",
    "votre Seigneur y répandra pour vous de Sa miséricorde",
    "Il vous disposera de votre affaire un agrément",
    "Tu verras le soleil",
    "s’écarter de leur Caverne vers la droite",
    "Et tu les estimeras éveillés",
    "tandis que leur chien étend ses deux pattes au seuil",
    "tu te serais détourné d’eux en fuite",
    "donne-nous de Ta part une miséricorde",
    "Nous frappâmes alors sur leurs oreilles",
    "une chose étonnante",
    "Ou bien penses-tu",
    "par affliction",
    "te consumer",
    "sol aride",
    "parure pour elle",
    "nos concitoyens",
    "une preuve évidente",
    "Quel pire injuste",
    "adopté en dehors de Lui des divinités",
]:
    if probe in norm:
        errors.append(f"rendu hors matière présent : {probe[:50]}")

cache = json.load(open("scripts-translate/quran-cache.json", encoding="utf-8"))
rasm_18 = {n: t for n, t in cache["18"]["ar"]}
for n in range(6, 21):
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

if errors:
    print("verify-744 FAIL :")
    for e in errors:
        print(" -", e)
    sys.exit(1)
print("verify-744 PASS — structure OK, 2 rendus warš présents (18:19-20), contenu complet, 0 rendu hors matière (14-18/6-9), 0 rasm étranger 18:6-20, 0 arabe résiduel (ﷺ exempté)")

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Minhāj — contrôle coranique et de contenu de la leçon 749 (tafsir-5ep,
sūrat al-Kahf v32-35 — onzième leçon du second livre, pages 79-86 du manuel
miroir tafsir-3-thanawi). Les āyāt 32-35 sont rendues en français sur le rasm
warš du cache (présence vérifiée) ; les parallèles al-Anbiyāʾ imprimé
53/canonique 35 et an-Nāziʿāt imprimé 42/canonique 24 rendus du cache ; le
double rendu des āyāt 1-31 (leçons 739-748) est interdit ; le rasm nu du
cache interdit au corps (0 arabe — FR-seule) pour TOUTES les āyāt voisines
(1-31)."""
import json
import re
import sys

HTML = "tr-tmp/lesson-749-fr.html"
html = open(HTML, encoding="utf-8").read()
norm = re.sub(r"[ \u202f\u00a0]+", " ", html.replace("&nbsp;", "\u00a0"))
errors = []

# 1. structure et marqueurs
for frag in [
    "Source du cours",
    "Onzième leçon du second livre du parcours",
    "pages 79 à 86 de l’imprimé miroir",
    "1_20220304_20220304_2251",
    "p.79 ouvre la leçon 11",
    "Les objectifs de la leçon",
    "Le tamhīd",
    "Le commentaire",
    "La glose",
    "L’extraction des thèmes des āyāt",
    "Premièrement",
    "Deuxièmement",
    "Troisièmement",
    "Quatrièmement",
    "Les subtilités et les bienfaits",
    "L’évaluation",
    "L’exploitation",
    "la page imprimée 86",
    "jamais devinée",
    "interdites de double rendu",
]:
    if frag.lower() not in norm.lower():
        errors.append(f"fragment attendu absent : {frag[:55]}")

# 2. les āyāt 32-35 + parallèles rendus du cache — présence (9 rendus)
rendus = [
    "Donne-leur l'exemple de deux hommes: à l'un d'eux Nous avons assigné deux jardins de vignes que Nous avons entourés de palmiers et Nous avons mis entre les deux jardins des champs cultivés.",
    "(32)",
    "Les deux jardins produisaient leur récolte sans jamais manquer. Et Nous avons fait jaillir entre eux un ruisseau.",
    "(33)",
    "Et il avait des fruits et dit alors à son compagnon avec qui il conversait: «Je possède plus de biens que toi, et je suis plus puissant que toi grâce à mon clan».",
    "(34)",
    "Il entra dans son jardin coupable envers lui-même [par sa mécréance]",
    "Je ne pense pas que ceci puisse jamais périr,",
    "(35)",
    "Toute âme doit goûter la mort. Nous vous éprouverons par le mal et par le bien [à titre] de tentation. Et c'est à Nous que vous serez ramenés.",
    "C'est moi votre Seigneur, le très haut",
]
# adaptation du cache : apostrophes droites -> typographiques ; comparaison
# insensible aux espaces (l'auto-fix NNBSP décale « : » du cache)
rendus_norm = [r.replace("'", "’").replace(" ", "") for r in rendus]
compact = norm.replace(" ", "")
for r in rendus_norm:
    if r not in compact:
        errors.append(f"rendu coranique attendu absent : {r[:55]}")

# 3. contenu attendu (confrontation au manuel — glose, lectures, exégètes)
contenu = [
    "on les a entourés de toute part",
    "eau abondante coulante",
    "al-waḥq — le retour et la restitution après la mort",
    "le plus ressemblant possible du frappé à son lieu de frappe",
    "Bilāl, ʿAmmār, Ṣuhayb et leurs pairs",
    "se glorifie de la duniyā et se refuse à la fréquentation des croyants",
    "nul avantage ne se rattachant à l’identification",
    "terre d’ensemencement pour tous les grains",
    "al-ḥāf : le côté, son pluriel aḥiffa",
    "al-Ṭabarī a dit : « elle a donné son fruit",
    "kiltā n’individualise point son unité",
    "le verbe qui suit les réunit et l’unifie",
    "al-Farrāʾ",
    "5/262",
    "au sukūn du kāf par Nāfiʿ, Ibn Kaṯīr et Abū ʿAmr",
    "il a fait tort à un tel de son dû quand il le rogne et le diminue",
    "Ibn ʿAbbās et Quṭāda ont dit",
    "Mujāhid a dit : il y est visé l’or et l’argent spécifiquement",
    "comme « kitāb » et « kutub »",
    "la droiture du dire requiert d’exprimer par brèveté",
    "cet homme à qui nous avons établi deux ǧannāt de vignes dit à son compagnon",
    "Salmān, Ḫabbāb, Ṣuhayb",
    "la vanité du pervers : l’abondance du bien et la noblesse du groupe",
    "la muḥāwara est la réponse, et le taḥāwur l’échange de réponses",
    "an-nafr — le groupe de l’homme qui part avec lui",
    "aṯ-Ṯaʿlabī",
    "ils furent frères — médite-le",
    "al-Ǧawāhir al-ḥisān",
    "sur le tamyīz, pour la rapport au pronom du parlant",
    "son tort envers lui-même : sa mécréance en le relèvement",
    "at-Taḥrīr wa-t-Tanwīr li-Ibn ʿĀšūr",
    "pour la longueur de son espoir",
    "de fermeté de l’arbre, de sa force, de son ancrage",
    "il ne tient point établi le relèvement ni survenue la Résurrection",
    "la voie du prêt et du calcul",
    "visant la ǧanna investie",
    "Khalaf a lu",
    "« in » en l’aimé, et « wa-ʾiḏā » en le détesté",
    "al-Aʿrāf",
    "al-Anbiyāʾ imprimé 53 — tranché 35",
    "méthode pédagogique coranique",
    "lois seigneuriales, règles cosmiques, guidages éducatifs",
    "Le déni du bienfait et l’orgueil par lui envers les créatures",
    "al-Qaṣaṣ imprimé 78",
    "an-Nāziʿāt imprimé 42 — tranché 24",
    "Iblīs dit",
    "quatre [choses] perdent le serviteur : moi, nous, avec moi, et à moi",
    "Je détermine le référent du pronom",
    "Je détermine ma position face à l’acte du propriétaire des deux ǧannāt",
    "al-Itqān fī ʿulūm al-Qurʾān",
    "la similitude du caché par le manifeste et de l’absent par le présent",
    "Je classe les fins schématiques",
    "āyāt 36-43 de sūrat al-Kahf",
]
for c in contenu:
    if c.lower() not in norm.lower():
        errors.append(f"contenu attendu absent : {c[:55]}")

# 4. rendus interdits (āyāt 1-31 déjà livrées leçons 739-748 — aucun double rendu)
interdits = [
    "Louange à Dieu qui a fait descendre sur Son serviteur",
    "Fais preuve de patience [en restant] avec ceux qui invoquent leur Seigneur matin et soir, désirant Sa Face.",
    "Et n’obéis pas à celui dont Nous avons rendu le cœur inattentif à Notre Rappel, qui poursuit sa passion et dont le comportement est outrancier.",
    "Quiconque le veut, qu’il croie, quiconque le veut, qu’il mécroie.",
    "Nous avons préparé pour les injustes un Feu dont les flammes les cernent.",
    "Et récite ce qui t’a été révélé du Livre de ton Seigneur. Nul ne peut changer Ses paroles.",
    "Ceux qui croient et font de bonnes œuvres... vraiment Nous ne laissons pas perdre la récompense de celui qui fait le bien.",
    "Voilà ceux qui auront les jardins du séjour (éternel) sous lesquels coulent les ruisseaux.",
    "Quelle bonne récompense et quelle belle demeure !",
    "Quiconque fait de bonnes œuvres tout en étant croyant, on ne méconnaîtra pas son effort",
    "Les jardins d’Eden où ils entreront, parés de bracelets en or ainsi que de perles",
    "Les jardins d’Eden, sous lesquels coulent les ruisseaux, pour y demeurer éternellement",
]
interdits_norm = [r.replace("'", "’") for r in interdits]
for probe in interdits_norm:
    if probe in norm:
        errors.append(f"rendu hors matière présent : {probe[:50]}")

cache = json.load(open("scripts-translate/quran-cache.json", encoding="utf-8"))
rasm_18 = {n: t for n, t in cache["18"]["ar"]}
for n in range(1, 32):
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

total = 20 + len(rendus) + len(contenu) + 12 + 31 + 3
print(f"verify-749-quran : {total} contrôles — rendus {len(rendus)} + contenu {len(contenu)} + interdits {12 + 31} + structure {20} + typo 3")
if errors:
    print("verify-749 FAIL :")
    for e in errors:
        print(" -", e)
    sys.exit(1)
print("verify-749 PASS — structure OK, āyāt 32-35 présentes (rasm warš du cache), parallèles al-Anbiyāʾ 35/an-Nāziʿāt 24 présents, contenu complet, 0 rendu hors matière (1-31), 0 rasm nu 18:1-31, 0 arabe résiduel (ﷺ exempté)")

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Minhāj — contrôle coranique et de contenu de la leçon 747 (tafsir-5ep,
sūrat al-Kahf v28-29 — neuvième leçon du second livre, pages 65-72 du manuel
miroir tafsir-2-thanawi). Les āyāt 28-29 sont rendues en français sur le rasm
warš du cache (présence vérifiée) ; les parallèles al-Anʿām imprimé
35/canonique 6:52 et az-Zumar imprimé 26/canonique 65 rendus du cache ; le
double rendu des āyāt 6-27 (leçons 740-746) est interdit ; les āyāt 30-31
(leçon 10) interdites de double rendu ; le rasm nu du cache interdit au corps
(0 arabe — FR-seule) pour TOUTES les āyāt voisines (6-29)."""
import json
import re
import sys

HTML = "tr-tmp/lesson-747-fr.html"
html = open(HTML, encoding="utf-8").read()
norm = re.sub(r"[ \u202f\u00a0]+", " ", html.replace("&nbsp;", "\u00a0"))
errors = []

# 1. structure et marqueurs
for frag in [
    "Source du cours",
    "Neuvième leçon du second livre du parcours",
    "pages 65 à 72 de l’imprimé miroir",
    "1_20220304_20220304_2251",
    "Les objectifs de la leçon",
    "Le tamhīd",
    "Le commentaire",
    "Les subtilités et les bienfaits",
    "L’évaluation",
    "L’exploitation",
    "la page imprimée 72",
    "jamais devinée",
]:
    if frag.lower() not in norm.lower():
        errors.append(f"fragment attendu absent : {frag[:55]}")

# 2. les āyāt 28-29 + parallèles rendus du cache — présence (12 rendus)
rendus = [
    "Fais preuve de patience [en restant] avec ceux qui invoquent leur Seigneur matin et soir, désirant Sa Face.",
    "Et que tes yeux ne se détachent point d'eux, en cherchant (le faux) brillant de la vie sur terre.",
    "Et n’obéis pas à celui dont Nous avons rendu le cœur inattentif à Notre Rappel, qui poursuit sa passion et dont le comportement est outrancier.",
    "Et dis : La vérité émane de votre Seigneur.",
    "Quiconque le veut, qu’il croie, quiconque le veut, qu’il mécroie.",
    "Nous avons préparé pour les injustes un Feu dont les flammes les cernent.",
    "Et s’ils implorent à boire, on les abreuvera d’une eau comme du métal fondu, brûlant les visages.",
    "Quelle mauvaise boisson et quelle détestable demeure !",
    "Et ne repousse pas ceux qui, matin et soir, implorent leur Seigneur, cherchant sa Face.",
    "Leur demander compte ne t'incombe en rien, et te demander compte ne leur incombe en rien. En les repoussant donc, tu serais du nombre des injustes.",
    "En effet, il t’a été révélé, ainsi qu’à ceux qui t’ont précédé : si tu donnes des associés à Dieu, ton œuvre sera certes vaine, et tu seras très certainement du nombre des perdants.",
    "(28-29)",
]
# adaptation du cache : apostrophes droites -> typographiques avant comparaison
rendus_norm = [r.replace("'", "’") for r in rendus]
for r in rendus_norm:
    if r not in norm:
        errors.append(f"rendu coranique attendu absent : {r[:55]}")

# 3. contenu attendu (confrontation au manuel et au récit R503)
contenu = [
    "ʿUyayna ibn Ḥiṣn",
    "al-Aqraʿ ibn Hābis",
    "ʿAmmār ibn Yāsir",
    "Ṣuhayb ibn Sinān",
    "Ibn Masʿūd",
    "Bilāl",
    "Salmān al-Fārisī",
    "Abū Dharr",
    "al-Wāḥidī",
    "Aṣbāb nuzūl al-Qurʾān",
    "5/452",
    "al-Anʿām 35-printed",
    "canonique 6 :52",
    "le plus juste",
    "car la sourate est mecquoise",
    "chiffons en tête",
    "aṣ-ṣalāwa",
    "az-zakāwa",
    "Ibn ʿĀmir",
    "bi-l-ġuduwwa",
    "bi-l-ġadāta",
    "Ibn ʿAṭiyya",
    "nom déterminé",
    "une des matinées",
    "septénale",
    "mutawātira",
    "aṭ-Ṭabarī",
    "Ǧāmiʿ al-bayān",
    "9/432",
    "ses deux transmissions",
    "Ibn ʿUmar",
    "Mujāhid",
    "an-Naḫʿī",
    "aux cinq prières",
    "Quṭāda",
    "la prière de l’aube",
    "la prière de l’après-midi",
    "la mémorisation d’une science",
    "sincères pour Lui en l’invocation",
    "nāhiya",
    "taʿdū",
    "al-Ḥasan",
    "ʿaynayka",
    "al-Qurṭubī",
    "az-Zumar 26-printed = canonique 65",
    "du širk",
    "Qurayš",
    "furuṭ",
    "le relâchement et la perte",
    "l’excès et la prodigalité",
    "Ibn Kaṯīr",
    "Ṭā-hā 129-130",
    "aḍ-Ḍaḥḥāk",
    "Ibn ʿAbbās",
    "ʿUmayya ibn Ḫalaf",
    "al-Ǧammaḥī",
    "notables des gens de la Mecque",
    "5/255",
    "sans doute ni incertitude",
    "le secours et le délaissement",
    "la guidance et l’égarement",
    "chasseur des croyants",
    "avertissement et menace",
    "que chacun choisisse pour lui-même",
    "permission ni libre choix",
    "à vous le Paradis",
    "à vous le Feu",
    "une frange a interprété",
    "orienté",
    "contraindre et encourager",
    "la récompense de la foi",
    "sarādīq",
    "az-Zaǧǧāǧ",
    "tout ce qui entoure quelque chose",
    "plus spécifique",
    "un mur de feu",
    "une fumée",
    "al-Mursalāt",
    "yastaġīṯūna",
    "d’assoiffement",
    "muhl",
    "Ibn Masʿūd et d’autres",
    "or, argent, plomb",
    "le pus et le sang",
    "Abū Bakr aṣ-Ṣiddīq",
    "le linceul",
    "brûlant, épais, noir, fétide",
    "Tafsīr al-Qurʾān al-ʿAẓīm 384-385",
    "al-Ḥākim",
    "Mustadrak",
    "Abū Umāma",
    "1543",
    "Le pronom",
    "compléments de spécification",
    "le blâme",
    "le coussin",
    "en s’y adossant",
    "az-Zamakhšarī",
    "al-Kashšāf 2/917",
    "ni compagnonnage ni adossement",
    "la fréquence permanente",
    "de droiture",
    "de seigneurie intérieure",
    "de sincérité en l’œuvre",
    "de persévérance au rappel",
    "un appoint pour l’individu",
    "la fermeté en la religion",
    "la purification de l’âme",
    "des excellences des mœurs",
    "l’entraide en le bien",
    "la piété et la crainte",
    "des perditions de la voie",
    "la négligence va au cœur",
    "des maladies des cœurs",
    "la présence du cœur",
    "ses transactions",
    "mœurs qui perdent le serviteur",
    "Saʿd ibn Abī Waqqāṣ",
    "Ṣaḥīḥ Muslim",
    "faḍāʾil aṣ-ṣaḥāba",
    "hadith 2413",
    "six hommes",
    "Ḫuzāʿa",
    "deux hommes dont je ne nomme point les noms",
    "la cause de révélation",
    "« fURLAN » placeholder inutile",
]
contenu = [c for c in contenu if c != "« fURLAN » placeholder inutile"]
for c in contenu:
    if c not in norm:
        errors.append(f"contenu attendu absent : {c[:55]}")

# 4. ABSENCE — rendus des āyāt des leçons voisines (6-27 livrés en 740-746,
#    30-31 = leçon suivante) — rasm nu du cache interdit
for probe in [
    "Et ainsi Nous les ressuscitâmes, afin qu’ils s’interrogent les uns les autres",
    "combien avez-vous demeuré",
    "Car s’ils se manifestaient à vous, ils vous lapideraient",
    "Or, ils demeurèrent dans leur caverne trois cents ans et en ajoutèrent neuf (années).",
    "Dis : Dieu sait mieux combien de temps ils demeurèrent là.",
    "À Lui appartient l’Inconnaissable des cieux et de la terre.",
    "Ils n’ont aucun allié en dehors de Lui et Il n’associe personne à Son commandement.",
    "Et récite ce qui t’a été révélé du Livre de ton Seigneur. Nul ne peut changer Ses paroles.",
    "Et tu ne trouveras, en dehors de Lui, aucun refuge.",
    "ne désespérez pas de la miséricorde de Dieu",
    "Ceux qui croient et font de bonnes œuvres",
    "Voilà ceux qui auront les jardins du séjour",
]:
    if probe in norm:
        errors.append(f"rendu hors matière présent : {probe[:50]}")

cache = json.load(open("scripts-translate/quran-cache.json", encoding="utf-8"))
rasm_18 = {n: t for n, t in cache["18"]["ar"]}
for n in range(6, 30):
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

total = 12 + len(rendus) + len(contenu) + 12 + 24 + 3
print(f"verify-747-quran : {total} contrôles — rendus {len(rendus)} + contenu {len(contenu)} + interdits {12 + 24} + structure {12} + typo 3")
if errors:
    print("verify-747 FAIL :")
    for e in errors:
        print(" -", e)
    sys.exit(1)
print("verify-747 PASS — structure OK, āyāt 28-29 présentes (rasm warš du cache), parallèles al-Anʿām 6:52/az-Zumar 65 présents, contenu complet, 0 rendu hors matière (6-27, 30-31), 0 rasm nu 18:6-29, 0 arabe résiduel (ﷺ exempté)")

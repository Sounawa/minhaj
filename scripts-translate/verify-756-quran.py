#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Minhāj — contrôle coranique et de contenu de la leçon 756 (tafsir-5ep,
sūrat al-Kahf v59-64 de l'imprimé warš — dix-huitième leçon du second livre,
pages 132-141 du manuel miroir tafsir-3-thanawi). La plage imprimée (59-64)
correspond aux āyāt 60-65 du cache canonique ḥafṣ (décalage de un, tranché
R511). Les six āyāt sont rendues en français sur le cache (présence vérifiée) ;
les āyāt 1-59 (leçons 739-755) et 66-73 (leçon 757) sont interdites de double
rendu ; le rasm nu du cache interdit au corps (0 arabe — FR-seule)."""
import json
import re
import sys

HTML = "tr-tmp/lesson-756-fr.html"
html = open(HTML, encoding="utf-8").read()
norm = re.sub(r"[ \u202f\u00a0]+", " ", html.replace("&nbsp;", "\u00a0"))
errors = []

# 1. structure et marqueurs
for frag in [
    "Source du cours",
    "Dix-huitième leçon du second livre du parcours",
    "pages 132 à 141 de l’imprimé miroir",
    "1_20220304_20220304_2251",
    "p.132 ouvre la leçon 18 au badge al-Kahf (59-64)",
    "le badge de la leçon 19 ouvre p.142",
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
    "la page imprimée 141",
    "jamais devinée",
    "interdites de double rendu",
    "plage imprimée (59-64) correspond aux āyāt 60 à 65 du cache canonique",
]:
    if frag.lower() not in norm.lower():
        errors.append(f"fragment attendu absent : {frag[:55]}")

# 2. les āyāt 60-65 rendus du cache — présence (6 rendus + 6 numéros)
cache = json.load(open("scripts-translate/quran-cache.json", encoding="utf-8"))
fr18 = {n: t for n, t in cache["18"]["fr"]}
rendus = [fr18[n] for n in (60, 61, 62, 63, 64, 65)] + [f"({n})" for n in (60, 61, 62, 63, 64, 65)]
rendus_norm = [r.replace("'", "’").replace(" ", "") for r in rendus]
compact = norm.replace(" ", "")
for r in rendus_norm:
    if r not in compact:
        errors.append(f"rendu coranique attendu absent : {r[:55]}")

# 3. contenu attendu (confrontation au manuel — glose, lectures, exégètes)
contenu = [
    "le péril du dédain des āyāt de Dieu",
    "le délai qu’Il accorde aux contrevenants",
    "significations dogmatiques, doctrinales, éducatives et pédagogiques",
    "il les rejoignit",
    "la consommation des forces et la fatigue",
    "Qu’est-ce que Mūsā — que la paix soit sur lui — résolut d’entreprendre",
    "Mūsā fils de ʿImrān au regard des ḥadīṯs et des récits historiques",
    "n’est mentionné en le Qurʾān qu’un seul Mūsā",
    "s’il y avait en cette āya un autre, il l’aurait explicité",
    "al-Bakālī a prétendu",
    "Mūsā se tint parmi les fils d’Israël en prêcheur",
    "connais-tu quelqu’un de plus savant que toi",
    "Notre serviteur, au confluent des deux mers, est plus savant que toi",
    "Mūsā demanda le chemin vers lui, et il lui fit du poisson une marque",
    "ḥadīṯ 1713",
    "il n’eut point rapporté la science à Dieu",
    "ḥadīṯ 221 tel qu’imprimé",
    "elle est Yūšaʿ b. Nūn",
    "le serviteur de Mūsā",
    "en le langage des ʿArabes, le jeune homme",
    "une belle manière d’éducation",
    "je ne cesserai de cheminer sur le rivage de la mer",
    "du lignage de",
    "son nom du sujet est un pronom latent",
    "je ne me détournerai point de vous, et je ne vous quitterai point",
    "donnent au ḥiqāb le sens d’année — en le parler de Qays",
    "quatre-vingts années",
    "soixante-dix années",
    "un dahr",
    "quand bien même cela exigerait un temps long",
    "Ǧāmiʿ al-Bayān",
    "9/272",
    "la hauteur d’ambition de Mūsā",
    "la force de sa volonté et la droiture de sa résolution",
    "l’adage d’al-ʿAṭāʾ",
    "trouve légère la charge qu’il porte",
    "une conduite pour tout étudiant en science",
    "d’expression élidée, son taqdīr",
    "ils voyagèrent, puis lorsqu’ils parvinrent",
    "s’excusant et s’attristant",
    "car c’est lui qui en fut chargé",
    "il oublia d’informer Mūsā de l’ordre du poisson alors qu’il était endormi",
    "je différerai jusqu’à son réveil",
    "bien que son auteur fût l’un des deux",
    "l’un des deux oublia",
    "al-Baḥr al-Muḥīṭ",
    "7/102",
    "Maǧāhid et Quatāda",
    "le lieu où se rejoignent la mer de Perse et la mer des Rūm",
    "il est auprès de Ṭanǧa",
    "la mer océane et la mer qui en sort (la mer blanche médiane)",
    "en Ifrīqiya (Tūnis)",
    "la mer des Andalous avec la mer océane",
    "la mer d’al-ʾUrdunn et la mer al-Qulzum (la Rouge)",
    "les opinions les plus notoires en la matière",
    "une mer salée et une mer douce",
    "au lieu d’un grand fleuve en la mer",
    "une allégorie de Mūsā et al-Khiḍr, eux deux mers de science",
    "Ibn ʿAṭiyya l’affaiblit",
    "les ḥadīṯs ne désignent pour lui qu’une eau de mer",
    "le chemin en le creux de la terre",
    "un lieu vide comme le taq",
    "le poisson demeura en son passage un lieu vide",
    "il se creusa un sīr en la poussière, du contenant à la mer",
    "l’apparent de l’affaire est que le sīr ne fut qu’en l’eau",
    "la légitimité de l’oubli chez les Prophètes",
    "ainsi que chez les créatures en les significations de la religion",
    "lequel est un pardon de la part de Dieu",
    "ne nous châtie pas s’il arrive que nous oublions ou commettons une erreur",
    "Dieu a passé outre à ma communauté l’erreur, l’oubli et ce qui leur est imposé par contrainte",
    "Sunan Ibn Māǧa",
    "bāb aṭ-ṭalāq wa-n-nisyān",
    "ḥadīṯ 2043 — chiffre imprimé tranché",
    "s’en fuyant — s’arrêtant à leur lieu de repos auprès du rocher",
    "ils dépassèrent le confluent des deux mers",
    "ils dépassèrent le poisson, délaissé et abandonné",
    "son complément fut élidé pour la connaissance qu’on en avait",
    "un verbe d’ordre du quadrilittère",
    "au sens de donner la chose et de la tendre à autrui",
    "la nourriture du jour, dérivée de al-ġaduwa",
    "son contraire est al-ʿašāʾ, la nourriture du soir",
    "une seule, partagée, qu’ils la partageaient ensemble",
    "Mūsā ne s’en distinguait point de son serviteur",
    "de la perfection des moeurs des Prophètes et de leur complétude",
    "de la peine du voyage — de là la légitimation d’y réduire la prière",
    "la dispense de rompre le jeûne en Ramaḍān en voyage",
    "le voyage est une part de punition",
    "kitāb al-ʿumra, bāb qiṭʿat as-safar",
    "informe-moi",
    "l’oublie fut attribué au démon",
    "il fut ravi par cela et dit",
    "la fin du chemin en sa première étape, et le commencement de la délivrance",
    "l’attribution de l’oubli du serviteur au démon tient à ce qu’il a pouvoir sur lui",
    "l’oubli des Prophètes ne fut point attribué au démon",
    "leur oubli fut une conformation pour les créatures et une sunna parmi eux",
    "Aḥkām al-Qurʾān",
    "en les recensions du Muwaṭṭaʾ",
    "je oublie…",
    "le poisson traça en la mer un chemin étonnant pour les gens",
    "Muḥammad b. Abī Ǧamʿa al-Hibṭī",
    "les Maghrébins suivirent par lui depuis des siècles",
    "le poisson serait mort — sa joue mangée — puis revécût après cela",
    "suivant leurs empreintes de peur de manquer leur chemin",
    "l’ʾirtidād est le retour",
    "le dāl s’adghama dans le dāl pour la similitude des deux",
    "les suivre et les chercher en le lieu de leur dissimulation",
    "comme en le récit de la mère de Mūsā",
    "suis son empreinte",
    "équivalent du dérivé",
    "traquant leurs empreintes précédentes en retour",
    "une glorification et une élection",
    "est al-Khiḍr en le dire de la masse au regard des ḥadīṯs",
    "l’a contredit celui qu’on ne compte point",
    "mais un autre homme de science",
    "al-Khiḍr est prophète en le dire de la masse",
    "un serviteur vertueux non prophète",
    "l’āya témoigne de sa prophétie",
    "les secrets de ses actes, sinon par révélation de Dieu",
    "au khāʾ du kasr avec le ḍād du sukūn",
    "au khāʾ du fatḥ avec le ḍād du sukūn",
    "au ḍād du kasr — trois langues s’y rencontrent",
    "la masse des lecteurs a lu avec le tašdīd de la nūn",
    "Abū ʿAmr, des Baṣriens, a lu",
    "au ḍamm du dāl et l’allègement de la nūn",
    "Abū Ḥātim a dit",
    "une science de la science de l’invisible",
    "Zād al-Masīr",
    "la science de al-Khiḍr fut la connaissance des secrets révélés à lui",
    "la science des jugements et des fatwās aux paroles et actes apparents des gens",
    "le voyage de l’homme de science en quête de l’accroissement de la science",
    "le recours au serviteur et au compagnon pour cela",
    "la saisie de la rencontre des vertueux et des savants",
    "cela fut la coutume des ancêtres vertueux",
    "les voyageurs parvinrent à la part espérée",
    "les fondements s’ancrèrent pour eux en les sciences",
    "la légitimation de l’adoption du compagnon de voyage, et son choix parmi les vertueux",
    "si les gens savaient ce que je sais de la solitude, nul monté ne voyagerait de nuit seul",
    "kitāb al-ǧihād wa-s-siyar, bāb as-siyar waḥdah",
    "ḥadīṯ 2997 — chiffre imprimé tranché",
    "prit Abū Bakr pour compagnon en sa migration",
    "il fut le meilleur des compagnons et des frères",
    "le portage des provisions, leur préparation et leur remise",
    "sans le charger de ce qui le peine",
    "vos serviteurs sont vos frères",
    "qu’il le nourrisse de ce dont il se nourrit, et l’habille de ce dont il s’habille",
    "ne les chargez point de ce qui les accable",
    "si vous les chargez, aidez-les",
    "Et faites provision, la meilleure provision est la piété",
    "197 — renvoi imprimé tranché",
    "la belle moeur de Mūsā",
    "en son traitement de son serviteur",
    "les plus importants jugements législatifs déduits des āyāt du cours",
    "L’exploitation imprimée porte le ḥadīṯ d’Ubayy b. Kaʿb",
    "charge un poisson dans un contenant",
    "Yūšaʿ b. Nūn, et ils portèrent le poisson dans un contenant",
    "ils posèrent leurs têtes et s’endormirent",
    "Le poisson s’échappa du contenant",
    "ce fut un étonnement pour Mūsā et son serviteur",
    "Ils s’en allèrent le reste de leur nuit et de leur journée",
    "jusqu’à dépasser le lieu auquel il fut ordonné",
    "un homme couché, couvert d’un habit",
    "Mūsā des fils d’Israël",
    "Je contemple le ḥadīṯ, puis je réponds",
    "Je tire du ḥadīṯ la cause du voyage de Mūsā",
    "les valeurs liées à la quête de science",
    "deux propos attestant que le Mūsā mentionné en les āyāt est Mūsā fils de ʿImrān",
    "La préparation préalable porte la révision de l’exégèse des āyāt 65 à 72 de sūrat al-Kahf",
    "āyāt 66 à 73 du cache canonique",
    "le jugement déduit de la brèche que al-Khiḍr fit au navire",
    "je cherche les sens des expressions suivantes",
    "La leçon s’achève en la page imprimée 141",
    "la leçon suivante ouvre en la page 142 du même manuel",
    "plage (65-72) à la grille du portail",
    "kahf-probe-l19.py",
    "convergence quadruple — jamais devinée",
]
for c in contenu:
    if c.lower() not in norm.lower():
        errors.append(f"contenu attendu absent : {c[:55]}")

# 4. rendus interdits (āyāt 1-59 livrées leçons 739-755 ; 66-73 leçon 757)
interdits_src = (1, 10, 32, 45, 46, 57, 58, 59, 66, 73)
interdits = []
for n in interdits_src:
    t = fr18[n].replace("'", "’")
    interdits.append(t[:60])
    interdits.append(t[-60:])
for probe in interdits:
    if probe in norm:
        errors.append(f"rendu hors matière présent : {probe[:50]}")

rasm_18 = {n: t for n, t in cache["18"]["ar"]}
rasm_n = 0
for n in list(range(1, 60)) + list(range(66, 74)):
    t = rasm_18[n]
    probes = [t, t.replace(" ", "")]
    ok = any(p in norm.replace(" ", "") for p in probes) or t in norm
    if ok:
        errors.append(f"rasm arabe interdit présent au corps (āya 18:{n})")
    rasm_n += 1

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

total = 22 + len(rendus) + len(contenu) + len(interdits) + rasm_n + 3
print(f"verify-756-quran : {total} contrôles — rendus {len(rendus)} + contenu {len(contenu)} + interdits {len(interdits)} + rasm {rasm_n} + structure {22} + typo 3")
if errors:
    print("verify-756 FAIL :")
    for e in errors:
        print(" -", e)
    sys.exit(1)
print("verify-756 PASS")

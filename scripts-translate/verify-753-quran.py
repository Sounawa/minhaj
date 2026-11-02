#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Minhāj — contrôle coranique et de contenu de la leçon 753 (tafsir-5ep,
sūrat al-Kahf v49-52 de l'imprimé warš — quinzième leçon du second livre, pages
110-117 du manuel miroir tafsir-3-thanawi). La plage imprimée (49-52) correspond
aux āyāt 50-53 du cache canonique ḥafṣ (décalage de un, tranché R511). Les
quatre āyāt sont rendues en français sur le cache (présence vérifiée) ; les āyāt
1-49 (leçons 739-752) et 54-56 (leçon 753 suivante) sont interdites de double
rendu ; le rasm nu du cache interdit au corps (0 arabe — FR-seule)."""
import json
import re

HTML = "tr-tmp/lesson-753-fr.html"
html = open(HTML, encoding="utf-8").read()


def normify(s: str) -> str:
    s = s.replace("&nbsp;", "\u00a0")
    return re.sub(r"[ \u202f\u00a0]+", " ", s)


norm = normify(html)
errors = []

# 1. structure et marqueurs
for frag in [
    "Source du cours",
    "Quinzième leçon du second livre du parcours",
    "pages 110 à 117 de l’imprimé miroir",
    "1_20220304_20220304_2251",
    "p.110 ouvre la leçon 15",
    "les objectifs de la leçon 16 ouvrent p.118",
    "jamais devinées",
    "plage imprimée (49-52) correspond aux āyāt 50 à 53 du cache canonique",
    "interdites de double rendu",
    "Les objectifs de la leçon",
    "Le tamhīd",
    "Le commentaire",
    "La glose",
    "L’extraction des thèmes des āyāt",
    "Premièrement",
    "Deuxièmement",
    "Troisièmement",
    "Les subtilités et les bienfaits",
    "L’évaluation",
    "L’exploitation",
    "la leçon s’achève en la page imprimée 117",
    "la leçon suivante ouvre en la page 118",
]:
    if frag.lower() not in norm.lower():
        errors.append(f"fragment attendu absent : {frag[:55]}")

# 2. les āyāt 50-53 rendues du cache — présence (4 rendus + 4 numéros)
cache = json.load(open("scripts-translate/quran-cache.json", encoding="utf-8"))
fr18 = {n: t for n, t in cache["18"]["fr"]}
rendus = [fr18[n] for n in (50, 51, 52, 53)] + ["(50)", "(51)", "(52)", "(53)"]
rendus_norm = [r.replace("'", "’").replace(" ", "") for r in rendus]
compact = norm.replace(" ", "")
for r in rendus_norm:
    if r not in compact:
        errors.append(f"rendu coranique attendu absent : {r[:55]}")

# 3. contenu attendu (confrontation au manuel — glose, récit, exégètes)
contenu = [
    "alliés et secouristes",
    "un lieu dont nul n’échappe",
    "Quelle est la cause de l’abstention d’Iblis de la prosternation",
    "De quoi Dieu s’est-Il indigné en ces āyāt",
    "Quels sont les visages de l’égarement des polythéistes",
    "l’avertissement contre Iblis et sa descendance",
    "la réprobation des mécréants",
    "comblés de tout bienfait, petit ou grand",
    "un circonstant du passé, rattaché à un verbe omis",
    "et rappelle",
    "rappel du récit, non de l’événement lui-même",
    "l’interlocuteur ne l’avait pas vécu",
    "Al-Ṭabarī — que Dieu lui fasse miséricorde — dit",
    "son orgueil et sa jalousie",
    "la prosternation à Adam",
    "quiconque agit comme lui agit en son modèle",
    "ils suivent son ordre et contredisent l’ordre de Dieu",
    "Jāmiʿ al-Bayān",
    "un geste d’honneur et de glorification d’Adam",
    "al-Ḥijr 15",
    "l’humilité extrême",
    "l’exception ici est discontinue",
    "Iblis n’est point des Anges, mais des djinns",
    "une fumée de feu",
    "l’exception est continue",
    "des israéliyyāt à examiner",
    "sans changement, addition ni retranchement",
    "Tafsīr al-Qurʾān al-ʿAẓīm",
    "il sortit, s’écarta et se détourna",
    "sort de son écorce",
    "du noyau quand il sort du fruit",
    "la souris quand elle sort de son terrier",
    "la nomma la souris débordeuse",
    "le détour du droit chemin et l’inclinaison hors de la droiture",
    "au sens du «&nbsp;&nbsp;après&nbsp;&nbsp; »",
    "une interrogation de réprobation",
    "les inspireurs parmi les diables",
    "qui ordonnent le blâmable et chargent vers le faux",
    "Muǧāhid disait",
    "ceux qui les suivent en lieu et place de Dieu",
    "un nom générique",
    "sur le schéma du qualificatif, où se valent le singulier et le pluriel",
    "poser la chose hors de sa place",
    "les visages de l’égarement des polythéistes",
    "il est général en toute créature",
    "Ibn ʿAṭiyya — que Dieu lui fasse miséricorde — dit",
    "l’objectif visé d’abord par l’āya, ce sont Iblis et sa descendance",
    "des devins et des ʿArabes qui les croient",
    "nous cherchons refuge auprès du Puissant de cette vallée",
    "un nom verbal rattaché à son complément",
    "Dieu créa les cieux et la terre",
    "la création des personnes des polythéistes",
    "le bras de la main",
    "le secoureur qui seconde l’homme",
    "Nous fortifierons ton bras par ton frère",
    "al-Qaṣaṣ 28",
    "riche de tout secours",
    "accroître le blâme et le reproche",
    "la majorité des lecteurs l’a lue avec la consonne muette du pronom",
    "Abū Jaʿfar l’a lue avec la voyelle de l’apostrophe",
    "l’apostrophe étant alors au Prophète",
    "la déconvenue des polythéistes le jour de la Résurrection",
    "devant les témoins",
    "Ḥamza, des Sept, l’a lue avec la nūn",
    "sur le visage de l’imploration auprès d’eux",
    "pour qu’ils repoussent d’eux Mon châtiment",
    "la conjecture et la prétention sont l’inverse de la certitude",
    "la prétention est le plus souvent du mensonge",
    "où l’engagement de l’information demeure sur l’informateur",
    "l’appel est au sens de l’imploration",
    "la āya fut dite au passé, et le sens est l’avenir",
    "ils les invoqueront sans qu’ils leur répondent",
    "ces objets inertes qui ne profitent de rien",
    "à l’image de l’appel resté sans réponse",
    "le premier sens est le plus clair",
    "peut revenir sur les croyants et les mécréants",
    "les polythéistes et leurs objets d’adoration",
    "Ibn ʿAbbās et Anas ont dit",
    "Il sépare entre les gens du Feu et les croyants",
    "al-Ḥasan a dit",
    "cela veut dire une inimitié",
    "al-Ḍaḥḥāk a dit",
    "un lieu de destruction",
    "al-Ǧawharī a dit",
    "la perdition est le naufrage",
    "rempart dressé en la Géhenne",
    "nul chemin pour rejoindre autre qu’elle",
    "nul salut pour quiconque des divinités qu’ils adoraient",
    "un lieu de destruction, un effroi immense et une affaire grave",
    "p.883",
    "Et les criminels verront le Feu",
    "vision des yeux",
    "soixante-dix laisses",
    "soixante-dix mille anges",
    "ils sauront de toute nécessité qu’ils y tomberont",
    "l’avance de l’angoisse",
    "la crainte qui précède étant un châtiment qui advient d’abord",
    "Ibn al-Ǧawzī — que Dieu lui fasse miséricorde — dit",
    "le désir et la passion",
    "y fut posée la colère",
    "tel un éducateur qui lui ordonne la justice",
    "le diable fut créé pour l’inciter à l’excès",
    "manifesté son inimitié depuis le temps d’Adam",
    "pour corrompre les conditions des fils d’Adam",
    "le Qurʾān le recommande en maints endroits",
    "un avertissement contre les ruses du diable",
    "l’accrochage à Dieu — Très-Haut — et à l’adhésion à Sa guidance",
    "modèles des Prophètes et des Messagers",
    "en cela sont le salut et la réussite",
    "Que vise la parole de Dieu — Très-Haut",
    "l’orientation éducative tirée de la parole de Dieu",
    "L’imām Faḫr al-Dīn al-Rāzī — que Dieu lui fasse miséricorde — dit",
    "s’adressant à l’orgueilleux",
    "tire gloire de la misère des musulmans",
    "ostentation d’orgueil et d’auto-admiration suit Iblis",
    "l’ascendant dans la science et la controverse",
    "par arrogance et dédain",
    "il imite Iblis",
    "une station rude où butent la plupart des créatures",
    "demande donc à Dieu le salut d’elle",
    "Mafātīḥ al-Ġayb",
    "le trait de caractère par lequel quiconque s’en pare suit Iblis",
    "les effets mauvais de ce trait sur l’individu et sur la société",
    "la voie pour éviter ce trait blâmable",
    "la révision de l’exégèse des āyāt 53 à 55 de sūrat al-Kahf",
    "āyāt 54 à 56 du cache canonique",
    "fragment imprimé altéré, déclaré",
    "consignes imprimées altérées, déclarées",
    "tranchée par le sondage textuel de la sonde",
    "jamais devinée",
]
for c in contenu:
    if normify(c).lower() not in norm.lower():
        errors.append(f"contenu attendu absent : {c[:55]}")

# 4. rendus interdits (āyāt 1-49 livrées leçons 739-752 ; 54-56 leçon suivante)
interdits = [
    "Louange à Dieu qui a fait descendre sur Son serviteur",
    "Toute âme doit goûter la mort",
    "Donne-leur l'exemple de deux hommes",
    "Quant à moi, c'est Allah qui est mon Seigneur",
    "En entrant dans ton jardin, que ne dis-tu",
    "Et sa récolte fut détruite et il se mit alors",
    "En l'occurrence, la souveraine protection appartient à Allah",
    "cependant que ses treilles étaient complètement ravagées",
    "Les biens et les enfants sont l'ornement",
    "Et propose-leur l'exemple de la vie ici-bas",
    "mais il eut une bonne fin et il Me fit",
    "Et le jour où Nous ferons courir les montagnes",
    "vous êtes venus à Nous comme Nous vous avons créés une première fois",
    "et le Livre sera placé",
]
for probe in interdits:
    p = probe.replace("'", "’").replace(" ", "")
    if p in compact:
        errors.append(f"rendu hors matière présent : {probe[:50]}")

# 5. rasm nu du cache interdit au corps (0 arabe — FR-seule)
rasm_18 = {n: t for n, t in cache["18"]["ar"]}
for n, t in rasm_18.items():
    for probe in (t, t.replace(" ", "")):
        if len(probe) >= 12 and probe in compact:
            errors.append(f"rasm nu présent : āya {n} : {probe[:40]}")

if errors:
    print(f"VERIFY 753 : {len(errors)} ERREUR(S)")
    for e in errors[:25]:
        print(" -", e)
    raise SystemExit(1)
print(f"VERIFY 753 PASS — {len(contenu)} ancrages de contenu, 4 āyāt du cache (50-53), "
      f"{len(interdits)} probes d'interdits, {len(rasm_18)} rasm nu bannis")

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Minhāj — contrôle coranique et de contenu de la leçon 755 (tafsir-5ep,
sūrat al-Kahf v56-58 de l'imprimé warš — dix-septième leçon du second livre,
pages 125-131 du manuel miroir tafsir-3-thanawi). La plage imprimée (56-58)
correspond aux āyāt 57-59 du cache canonique ḥafṣ (décalage de un, tranché
R511). Les trois āyāt sont rendues en français sur le cache (présence vérifiée)
; les āyāt 1-56 (leçons 739-754) et 60-65 (leçon suivante) sont interdites de
double rendu ; le rasm nu du cache interdit au corps (0 arabe — FR-seule)."""
import json
import re

HTML = "tr-tmp/lesson-755-fr.html"
html = open(HTML, encoding="utf-8").read()


def normify(s: str) -> str:
    s = s.replace("&nbsp;", "\u00a0")
    s = re.sub(r"[ \u202f\u00a0]+", " ", s)
    return re.sub(r" +:", ":", s)


norm = normify(html)
errors = []

# 1. structure et marqueurs
for frag in [
    "Source du cours",
    "Dix-septième leçon du second livre du parcours",
    "pages 125 à 131 de l’imprimé miroir",
    "1_20220304_20220304_2251",
    "p.125 ouvre la leçon 17",
    "l’ʾiʿdād qiblī de p.131",
    "les objectifs de la leçon 18 ouvrent p.132",
    "jamais devinées",
    "plage imprimée (56-58) correspond aux āyāt 57 à 59 du cache canonique",
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
    "la leçon s’achève en la page imprimée 131",
    "la leçon suivante ouvre en la page 132",
    "Consigne imprimée altérée, déclarée",
    "jamais devinée",
    "kahf-probe-l18.py",
]:
    if frag.lower() not in norm.lower():
        errors.append(f"fragment attendu absent : {frag[:55]}")

# 2. les āyāt 57-59 rendues du cache — présence (3 rendus + 3 numéros)
cache = json.load(open("scripts-translate/quran-cache.json", encoding="utf-8"))
fr18 = {n: t for n, t in cache["18"]["fr"]}
rendus = [fr18[n] for n in (57, 58, 59)] + ["(57)", "(58)", "(59)"]
rendus_norm = [r.replace("'", "’").replace(" ", "") for r in rendus]
compact = norm.replace(" ", "")
for r in rendus_norm:
    if r not in compact:
        errors.append(f"rendu coranique attendu absent : {r[:55]}")

# 3. contenu attendu (confrontation au manuel — glose, exégètes, lectures)
contenu = [
    "il en tourna le dos et s’en alla",
    "ce qu’elles ont fait auparavant et produit",
    "un rendez-vous et un moment fixé",
    "le temps de leur anéantissement",
    "Quels sont les traits de ceux qui se détournent de la guidée du Qurʾān",
    "Quelle est la sagesse du différé de Dieu envers les mécréants",
    "les traits de ceux qui se détournent du Qurʾān généreux",
    "interrogation de déni",
    "nul n’est plus injuste que celui auquel cette description s’applique",
    "il a jeté derrière lui ses péchés capitaux",
    "l’oubli est ici au sens de l’abandon",
    "les deux sens sont proches",
    "l’attribution des mauvaises actions aux deux mains est métaphorique",
    "l’instrument du gain dans les actes répréhensibles",
    "clause de justification",
    "l’emploi du « inna » à kasra y est de fréquence nombreuse",
    "cause d’une obturation posée sur leurs cœurs et leur ouïe",
    "le pronom en « de sorte qu’ils ne comprennent pas » revient au Qurʾān généreux",
    "afin qu’ils comprennent les āyāt du Qurʾān et s’y guident",
    "comme l’enveloppe qui voile et dissimule",
    "d’obturation et d’empreinte",
    "est-ce au réel ou au figuré",
    "Ibn ʿAṭiyya dit",
    "le réel en ceci n’est point impossible",
    "le figuré est également bien dit",
    "les cœurs que Dieu — Très-Haut — a pu rendre les plus durs",
    "c’est la pesanteur — et c’est une métaphore, à savoir : la surdité",
    "Ibn ʿAṭiyya — que Dieu lui fasse miséricorde — dit",
    "la lourdeur en les oreilles est une métaphore évidente",
    "l’infortune des mécréants est qu’ils entendent pleinement l’appel vers la Loi",
    "on les a comparés à lui",
    "de même la cécité, la surdité et la mutité, toutes sont métaphores",
    "le différend ne porte qu’en les qualités du cœur",
    "l’Islām et ses lois",
    "le souci qu’avait le Prophète — que la bénédiction et la paix de Dieu soient sur lui — de l’accomplissement de leur foi",
    "utile à la négation de leur guidée en le temps de la descente de l’āya",
    "l’origine était la possibilité que certains d’entre eux croient et se guident ensuite",
    "l’insistance de la négation par « jamais » a fermé la porte",
    "Abū Ḥayyān — que Dieu lui fasse miséricorde — dit",
    "celui que Dieu a scellé le cœur en le mécréance",
    "beaucoup de mécréants se sont guidés et ont cru",
    "un jugement sur l’obstination",
    "quand bien même on les appellerait en masse vers la guidée",
    "al-Baḥr al-Muḥīṭ",
    "le différé de Dieu envers les désobéissants",
    "Quand Dieu — Très-Haut — informa des gens à qui la mécréance fut scellée",
    "les mécréants de la Mécque — tôt et rapide",
    "des manifestations de Sa miséricorde mentionnées avant",
    "al-Naḥl 16:61",
    "ou bien source — « en par leur acquisition » — ou bien relative",
    "un terme déterminé qu’ils voient différer",
    "tout en leur excès en mécréance et hostilité envers le Messager",
    "de Sa qualification — Très-Haut — de pardon et de miséricorde",
    "Il leur hâterait le châtiment destructeur pour eux",
    "un terme d’où ils ne trouveront nul salut",
    "l’échéance de la mort",
    "le châtiment de l’au-delà",
    "al-Ṭabarī dit : c’est le jour de Badr ou le jour d’Uḥud",
    "le refuge est le sauveur et le sanctuaire",
    "dit Ibn ʿAbbās et Ibn Zayd",
    "al-Ǧawharī l’a rapporté en aṣ-Ṣiḥḥāḥ",
    "la menace de Dieu — Très-Haut — aux injustes",
    "Nous avons fait périr les gens de ces cités",
    "le dit « pour leur destruction » l’indique",
    "le pronom reprend les gens des cités",
    "ceci renvoie à ʿĀd, Thamūd, Madyan et autres",
    "envers eux-mêmes par l’association envers Dieu",
    "la lexie de l’injustice y est justificative",
    "signalant la cause de l’anéantissement, laquelle est l’injustice",
    "Abū al-Ḥasan Ibn ʿUṣfūr soutint la lexicalité de la particule « quand »",
    "un circonstant employé pour la justification",
    "ou pour la transitivité, ou pour généraliser l’injustice",
    "les civilisations qui furent en les terres des Arabes",
    "ʿĀd, Thamūd, Madyan, le peuple de Lot, Sabaʾ et autres",
    "visant leurs habitants et leurs bâtisseurs",
    "celle-ci étant demeure par élision",
    "al-Ḥiǧr 15:4-5",
    "la menace des mécréants de la Mécque du châtiment des injustes d’avant eux",
    "ainsi fûtes-vous, ô associateurs",
    "vous avez traité de menteur le plus noble des Messagers et le plus généreux des Prophètes",
    "vous n’êtes point auprès de Nous plus chers qu’eux",
    "craignez donc Mon châtiment et Ma menace",
    "la majorité des lecteurs a lu avec la mīm au ḍamm et le lām au fatḥ",
    "pour le temps de la chose et son lieu",
    "annexé au complément d’objet",
    "ʿĀṣim a lu, en la récitation de Šuʿba Abū Bakr",
    "ʿĀṣim a lu, en la récitation de Ḥafṣ",
    "non-transitif",
    "parce qu’ils furent anéantis",
    "un ǧinās de dérivation",
    "une mise en parallèle entre l’affirmation et la négation",
    "des embellissements de la rhétorique",
    "Le lieu de l’absolution est l’acte",
    "le lieu de la miséricorde est l’agent",
    "la miséricorde n’est qu’effet de l’absolution",
    "son résultat et sa manifestation",
    "Il lui fait miséricorde et le protège de la mauvaise issue",
    "l’absolution précède la miséricorde",
    "une règle unique",
    "al-Burūǧ 85:14-16",
    "l’orientation d’al-Ālūsī — que Dieu lui fasse miséricorde",
    "pour la mise à part et l’attribution",
    "avant l’embellissement",
    "plus important selon l’état et le lieu",
    "l’exposé du différé du châtiment sur eux",
    "Rūḥ al-Maʿānī",
    "al-Qurṭubī dit",
    "accorde Sa faveur au mécréant en la duniyā comme Il l’accorde au croyant",
    "la guidée du Qurʾān, le croyant seul y accède — point le mécréant",
    "al-Ǧāmiʿ li-ʾaḥkām al-Qurʾān",
    "Je contemple le texte d’al-Qurṭubī, puis je réponds",
    "Extrait les quatre interprétations venues en « le Pardonneur et la miséricorde »",
    "le propre de ces significations aux gens de la foi",
    "la révision de l’exégèse des āyāt 59 à 64 de sūrat al-Kahf",
    "āyāt 60 à 65 du cache canonique",
    "qui est le serviteur vertueux visé",
    "tranchée par le sondage textuel de la sonde",
]
for c in contenu:
    if normify(c).lower() not in norm.lower():
        errors.append(f"contenu attendu absent : {c[:55]}")

# 4. rendus interdits — āyāt 1-56 livrées (leçons 739-754) et 60-65 leçon suivante
interdits = [
    "Louange à Dieu qui a fait descendre sur Son serviteur",
    "Toute âme doit goûter la mort",
    "Donne-leur l'exemple de deux hommes",
    "Quant à moi, c'est Allah qui est mon Seigneur",
    "En entrant dans ton jardin, que ne dis-tu",
    "Et sa récolte fut détruite et il se mit alors",
    "Les biens et les enfants sont l'ornement",
    "Et propose-leur l'exemple de la vie ici-bas",
    "Et le jour où Nous ferons courir les montagnes",
    "vous êtes venus à Nous comme Nous vous avons créés une première fois",
    "et le Livre sera placé",
    "Et lorsque nous dîmes aux Anges",
    "Je ne les ai pas pris comme témoins de la création",
    "Et le jour où Il dira: «Appelez ceux que vous prétendiez",
    "Et les criminels verront le Feu",
]
for probe in interdits:
    p = probe.replace("'", "’").replace(" ", "")
    if p in compact:
        errors.append(f"rendu hors matière présent : {probe[:50]}")

for n in list(range(1, 57)) + [60, 61, 62, 63, 64, 65]:
    t = fr18[n]
    for probe in (t[:60], t.replace(" ", "")[:60]):
        q = probe.replace("'", "’")
        if len(q) >= 20 and q in compact:
            errors.append(f"rendu hors matière présent : āya {n} : {q[:45]}")

# 5. rasm nu du cache interdit au corps (0 arabe — FR-seule)
rasm_18 = {n: t for n, t in cache["18"]["ar"]}
for n, t in rasm_18.items():
    for probe in (t, t.replace(" ", "")):
        if len(probe) >= 12 and probe in compact:
            errors.append(f"rasm nu présent : āya {n} : {probe[:40]}")

if errors:
    print(f"VERIFY 755 : {len(errors)} ERREUR(S)")
    for e in errors[:25]:
        print(" -", e)
    raise SystemExit(1)
print(f"VERIFY 755 PASS — {len(contenu)} ancrages de contenu, 3 āyāt du cache (57-59), "
      f"{len(interdits)} probes fixes + {56 + 6} plages d'interdits, {len(rasm_18)} rasm nu bannis")

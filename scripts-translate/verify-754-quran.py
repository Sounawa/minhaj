#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Minhāj — contrôle coranique et de contenu de la leçon 754 (tafsir-5ep,
sūrat al-Kahf v53-55 de l'imprimé warš — seizième leçon du second livre, pages
118-124 du manuel miroir tafsir-3-thanawi). La plage imprimée (53-55) correspond
aux āyāt 54-56 du cache canonique ḥafṣ (décalage de un, tranché R511). Les trois
āyāt sont rendues en français sur le cache (présence vérifiée) ; les āyāt 1-53
(leçons 739-753) et 57-59 (leçon suivante) sont interdites de double rendu ; le
rasm nu du cache interdit au corps (0 arabe — FR-seule)."""
import json
import re

HTML = "tr-tmp/lesson-754-fr.html"
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
    "Seizième leçon du second livre du parcours",
    "pages 118 à 124 de l’imprimé miroir",
    "1_20220304_20220304_2251",
    "p.118 ouvre la leçon 16",
    "l’ʾiʿdād qiblī de p.124",
    "les objectifs de la leçon 17 ouvrent p.125",
    "jamais devinées",
    "plage imprimée (53-55) correspond aux āyāt 54 à 56 du cache canonique",
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
    "la leçon s’achève en la page imprimée 124",
    "la leçon suivante ouvre en la page 125",
    "Consigne imprimée altérée, déclarée",
    "jamais devinée",
]:
    if frag.lower() not in norm.lower():
        errors.append(f"fragment attendu absent : {frag[:55]}")

# 2. les āyāt 54-56 rendues du cache — présence (3 rendus + 3 numéros)
cache = json.load(open("scripts-translate/quran-cache.json", encoding="utf-8"))
fr18 = {n: t for n, t in cache["18"]["fr"]}
rendus = [fr18[n] for n in (54, 55, 56)] + ["(54)", "(55)", "(56)"]
rendus_norm = [r.replace("'", "’").replace(" ", "") for r in rendus]
compact = norm.replace(" ", "")
for r in rendus_norm:
    if r not in compact:
        errors.append(f"rendu coranique attendu absent : {r[:55]}")

# 3. contenu attendu (confrontation au manuel — glose, récit, exégètes)
contenu = [
    "ce qui contient exhortation et leçon",
    "Par quoi les mécréants répondent-ils aux exemples du Qurʾān",
    "De quoi Dieu menace-t-Il ceux qui se détournent de l’appel du Qurʾān",
    "Quels sont les traits des mécréants en ces āyāt",
    "la frappe des exemples en le Qurʾān",
    "toutes sortes d’exemples",
    "tout exemple ayant utilité en le but visé par eux",
    "le but visé est la guidance",
    "preuves de la seigneurie, de l’unicité, de la résurrection et du compte",
    "Tafsīr al-Qurʾān al-ʿAẓīm",
    "al-ʿAnkabūt 29:43",
    "Al-Qurṭubī — que Dieu lui fasse miséricorde — dit",
    "elle porte deux visages",
    "leur rappel des enseignements des siècles passés et disparus",
    "al-Ǧāmiʿ li-ʾaḥkām al-Qurʾān",
    "une information condensée",
    "le déploiement des exemples ne profite point en eux",
    "ils sont déviés, disputant par le faux",
    "l’homme est grand querelleur, contradicteur et opposant au vrai",
    "sauf celui que Dieu guide son regard vers la voie du salut",
    "tempéraments innés de l’homme",
    "s’il ne l’éduque pas par la Loi sage",
    "et c’est la dispute",
    "al-ʿAdiyāt 100:6",
    "l’état des traités de menteurs, exposés à ce qui advint à leurs Anciens",
    "les mécréants de Qurayš et les mécréants de l’époque de la prophétie",
    "l’énoncé général visant le particulier",
    "un regret de dépit sur eux",
    "une mise en garde contre la corruption de leur état",
    "ce refus ne fut point avec intention",
    "avec la conviction d’être dans le vrai",
    "comme si leur état l’exigeait",
    "la lexie de la venue du châtiment",
    "Ibn Kathīr, Nāfiʿ, Abū ʿAmr et Ibn ʿĀmir l’ont lue",
    "ʿĀṣim, al-Kisāʾī et Ḥamza l’ont lée",
    "Elle porte deux sens possibles",
    "le châtiment leur viendra avant",
    "le châtiment leur viendra par détachements éparés",
    "quand nous serons ossements et décombres",
    "soyez pierre ou fer",
    "création grossissant en vos poitrines",
    "al-Isrāʾ 17:49",
    "venu ce qui précéda en cette sourate",
    "la lexie de négation opère l’exception dite affranchie",
    "la négation antérieure s’annulant pour agir en ce qui suit",
    "le but de l’envoi des Messagers",
    "annonciateurs de bonne nouvelle à quiconque croit, du Paradis",
    "avertisseurs à quiconque mécroît, du Feu",
    "La lexie du renversement",
    "ôter, annuler et faire dévier",
    "le glissement du pied quand il dévie et déborde",
    "l’astre qui glisse à son couchant",
    "traité de mensonge Dieu et Son Messager",
    "pour repousser la vérité par leur faux qu’ils dressent",
    "descendit sur ceux qui disputaient à propos des Messagers",
    "un sorcier, un possédé, un poète et un devin",
    "ils ont moqué et tourné en jeu les versets du Qurʾān",
    "les lectures alternent sur la lexie de la moquerie",
    "Ḥamza l’a lue avec la hamza",
    "la récitation de Warš l’a lue par substitution de la hamza en un wāw",
    "la raillerie et le mépris du Qurʾān",
    "la parole d’Abū Ǧahl",
    "voici la ẓaqqūm",
    "une moquerie et des rêveries confuses",
    "les fables des Anciens qu’il se fait écrire",
    "qu’on lui récite matin et soir",
    "al-Furqān 25:5",
    "La bonne nouvelle et l’avertissement sont la fonction des Messagers",
    "preuve de la miséricorde de Dieu envers les serviteurs",
    "al-Nisāʾ 4:165",
    "après l’envoi de Sa part de Messagers portant l’information",
    "abandonner l’abus de dispute dans les transactions",
    "la querelle dans les ventes et les sociétés",
    "s’orner là-dedans de magnanimité et de générosité",
    "Saʿīd b. Abī Saʿīd — que Dieu l’agrée — avait été associé",
    "en le commerce avant l’Islām",
    "le jour de la Conquête",
    "Bienvenue à mon frère et mon associé",
    "tu œuvrais des actes en la Ǧāhiliyya",
    "tu n’y contrariais point et n’y disputais point",
    "al-Mustaḍrak ʿalā al-Ṣaḥīḥayn",
    "Kitāb al-buyūʿ",
    "passa chez lui et Fāṭima, fille du Prophète",
    "Ne priez-vous point",
    "nos âmes sont en la main de Dieu",
    "s’Il veut nous ressusciter, Il nous ressuscitera",
    "se frapper la cuisse",
    "l’homme est ce qu’il y a de plus grand disputeur",
    "Ṣaḥīḥ al-Bukhārī",
    "Kitāb al-tahajjud",
    "l’āya fut étendue au général, en tous les gens",
    "par répugnance pour la dispute en religion",
    "le débat eût grandi, et la querelle entrée",
    "blâment la dispute en religion, sans science ni preuve",
    "al-Ḥajj 22:8",
    "l’altération du sens apparent des textes",
    "l’effacement de leurs indications fermes",
    "Un peuple ne s’égare pas, après une guidance qu’il avait",
    "sans qu’on lui donne la dispute",
    "Sunan al-Tirmidhī",
    "sūrat al-Zukhruf",
    "ḥadīṯ 3523",
    "Quelle est la dispute blâmable dans ces āyāt",
    "quelle est la récompense de qui l’abandonne",
    "comment l’appliquer à ma conduite",
    "Citer les lectures venues en la lexie citée",
    "Le ḥāfiẓ Ibn ʿAbd al-Barr dit",
    "en l’interdiction de la dispute et de la controverse en le Qurʾān",
    "dont chacun nie ce que l’autre affirme et le repousse",
    "pour aboutir en elle au doute",
    "les Compagnons du Messager de Dieu",
    "y disputèrent en maints endroits",
    "tous deux blâmables",
    "la dispute en Dieu — Sa majesté — en Ses noms, Ses attributs et Sa personne",
    "ils se sont accordés sur la dispute en lui et l’affrontement",
    "rapporter les branches sur les principes",
    "Jāmiʿ Bayān al-ʿIlm wa-faḍlihi",
    "Quel est le type de controverse contre laquelle les textes viennent",
    "Je contemple le texte du ḥāfiẓ Ibn ʿAbd al-Barr, puis je réponds",
    "la révision de l’exégèse des āyāt 56 à 58 de sūrat al-Kahf",
    "āyāt 57 à 59 du cache canonique",
    "qu’est-ce qui fait barrière entre les mécréants et la guidance",
    "pourquoi Dieu n’a-t-Il pas hâté l’abaissement du châtiment",
    "tranchée par le sondage textuel de la sonde",
]
for c in contenu:
    if normify(c).lower() not in norm.lower():
        errors.append(f"contenu attendu absent : {c[:55]}")

# 4. rendus interdits — āyāt 1-53 livrées (leçons 739-753) et 57-59 leçon suivante
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

for n in list(range(1, 54)) + [57, 58, 59]:
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
    print(f"VERIFY 754 : {len(errors)} ERREUR(S)")
    for e in errors[:25]:
        print(" -", e)
    raise SystemExit(1)
print(f"VERIFY 754 PASS — {len(contenu)} ancrages de contenu, 3 āyāt du cache (54-56), "
      f"{len(interdits)} probes fixes + 56 plages d'interdits, {len(rasm_18)} rasm nu bannis")

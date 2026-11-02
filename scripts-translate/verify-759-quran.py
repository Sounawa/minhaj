#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Minhāj — contrôle coranique et de contenu de la leçon 759 (tafsir-5ep,
sūrat al-Kahf v78-81 de l'imprimé warš — vingt-et-unième leçon du second
livre, pages 157-164 du manuel miroir tafsir-3-thanawi). La plage imprimée
(78-81) correspond aux āyāt 79 à 82 du cache canonique ḥafṣ (décalage de un,
tranché R511). Les quatre āyāt sont rendues en français sur le cache
(présence vérifiée) ; les āyāt 1-78 (leçons 739-758) et 83-110 (leçon 760 à
venir) sont interdites de double rendu ; le rasm nu du cache interdit au
corps (0 arabe — FR-seule)."""
import json
import re
import sys

HTML = "tr-tmp/lesson-759-fr.html"
html = open(HTML, encoding="utf-8").read()
norm = re.sub(r"[ \u202f\u00a0]+", " ", html.replace("&nbsp;", "\u00a0"))
errors = []

# 1. structure et marqueurs
for frag in [
    "Source du cours",
    "Vingt-et-unième leçon du second livre du parcours",
    "pages 157 à 164 de l’imprimé miroir",
    "1_20220304_20220304_2251",
    "p.157 ouvre la leçon 21 au badge al-Kahf (78-81)",
    "les objectifs de la leçon 22 ouvrent p.165",
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
    "la page imprimée 164",
    "jamais devinée",
    "interdites de double rendu",
    "plage imprimée (78-81) correspond aux āyāt 79 à 82 du cache canonique",
    "convergence quintuple",
]:
    if frag.lower() not in norm.lower():
        errors.append(f"fragment attendu absent : {frag[:55]}")

# 2. les āyāt 79-82 rendus du cache — présence (4 rendus + 4 numéros imprimés)
cache = json.load(open("scripts-translate/quran-cache.json", encoding="utf-8"))
fr18 = {n: t for n, t in cache["18"]["fr"]}
rendus = [fr18[n] for n in (79, 80, 81, 82)] + [f"({n})" for n in (78, 79, 80, 81)]
rendus_norm = [r.replace("'", "’").replace(" ", "") for r in rendus]
compact = norm.replace(" ", "")
for r in rendus_norm:
    if r not in compact:
        errors.append(f"rendu coranique attendu absent : {r[:55]}")

# 3. contenu attendu (confrontation au manuel — glose, lectures, exégètes)
contenu = [
    "l’interprétation des actes d’al-Khiḍr — que la paix soit sur lui — et la sagesse qui s’y trouve",
    "la douceur de Dieu — Très-Haut — envers Ses serviteurs croyants, et Sa préservation d’eux",
    "M’attacher aux ordres de Dieu — Très-Haut — et éviter Ses interdictions, afin d’obtenir Sa préservation",
    "les trois actes accomplis par al-Khiḍr",
    "l’objection de Mūsā — que la paix soit sur lui — en chacun de ses actes",
    "la résolution d’al-Khiḍr sur la fin de la compagnie de Mūsā",
    "il ne les accomplit point sinon par un ordre de Dieu",
    "Quelle est donc la sagesse de ce que fit al-Khiḍr ?",
    "quelle est la source de ces conduites ?",
    "les leçons qui se tirent du récit ?",
    "l’insubordination et l’injustice",
    "je ne l’ai pas fait de mon propre chef",
    "Ces āyāt contiennent ce qui suit.",
    "L’ʾimām aṭ-Ṭabarī — que Dieu lui fasse miséricorde — dit : « je fis au navire ce que je fis — le percer",
    "Ǧāmiʿ al-Bayān",
    "15/393",
    "à l’allègement du sīn, pluriel de « misérable »",
    "en la lecture anomale",
    "ils sont les équipages du navire",
    "celui qui tient la barre du navire",
    "ceux du navire sont des gens qu’il faut prendre en compassion",
    "la face de leur être « pauvres gens » alors que le navire était à eux",
    "gens de voyage en la disette, en le gouffre de la mer",
    "la rapine d’un injuste",
    "comme l’on dit au riche tombé en une fosse et une affliction : « misérable »",
    "ils étaient dix frères, gens d’infirmités, sans pouvoir sur l’œuvre",
    "cinq d’entre eux étaient invalides et cinq œuvraient au navire, ayant hérité ce navire de leur père",
    "y créer le défaut par la percée — une percée apparente à l’œil",
    "il le flétrit — flétri ; il l’orna — orné ; il le rusa — rusé ; il le redouta — redouté",
    "« que je rende défectueux leur navire »",
    "en la science des sens, du nom de l’abrégement, qu’on appelle aussi métonymie de l’ellipse",
    "« derrière » est des contradictes",
    "Ibn Ǧubayr et Ibn ʿAbbās dirent : « et il y avait devant eux un roi »",
    "Ibn ʿAṭiyya — que Dieu lui fasse miséricorde — dit : « sa parole",
    "en la considération du temps — l’existant antérieur en l’existence est le",
    "ce qui vient après est le",
    "tu les y trouveras suivant leur règle",
    "qu’ils cheminaient vers sa cité",
    "il est le soulagement du vacarme de ces vocables",
    "est suivi, en le temps, de la rapine du roi",
    "généralité dont le sens est la particularité",
    "ce roi ne rapinait des navires que ce seul portrait",
    "l’estimation : « tout navire sain »",
    "métonymie du déficit",
    "en le Ṣaḥīḥ de Muslim est rappelée la face de la sagesse de sa percée du navire",
    "quand viendra celui qui le met en œuvre, il le trouvera percé et le dépassera",
    "ils le raccommoderont d’une pièce de bois",
    "kitāb al-faḍāʾil, bāb min faḍāʾil al-Khiḍr ʿalayhi as-salām",
    "ḥadīṯ 2380 — chiffre imprimé inversé, tranché",
    "en la station de l’accusatif circonstanciel",
    "le complément absolu de « il saisissait »",
    "il revient sur al-Khiḍr : nulle difficulté en cela",
    "ceux que l’affaire préoccupa et qui en parlèrent sont les vertueux et ses compagnons",
    "c’est du côté de Dieu — Très-Haut —, et al-Khiḍr en fit le relais",
    "Aṭ-Ṭabarī dit : son sens est « nous avons su »",
    "son sens est « nous avons réprouvé »",
    "le plus apparent, en l’orientation de cette interprétation : c’est une métonymie",
    "sur la supposition des créatures et des interlocuteurs",
    "de « peut-être » et « il se peut »",
    "d’espoir, d’attente, de peur et de crainte n’est que selon vous, ô vous les interlocuteurs",
    "les astreindre et les charger avec dureté",
    "que l’amour de lui ne leur jetât la suite de lui",
    "ʿĀṣim lut",
    "revient sur al-Khiḍr et ses compagnons ; et le sens : nous avons souhaité que Dieu accordât aux deux parents croyants un enfant meilleur que lui",
    "« plus pur » : religion et droiture — à l’accusatif de spécification",
    "le visé — qu’il les eût en miséricorde",
    "Ibn ʿĀmir lut",
    "l’on transmit la divergence d’Abū ʿAmr al-Baṣrī",
    "leur Seigneur leur donna en échange une fille ; et il fut dit : un garçon soumis",
    "des règles et des secrets cachés que Dieu lui dévoila",
    "ce n’est point de la station de la législation",
    "la préservation de l’âme et la considération du droit de la vie",
    "des fondements des utilités nécessaires, dont toutes les législations célestes furent unanimes à la préservation",
    "kitāb al-waṣāyā, bāb de quand cesse l’orphelinat",
    "ḥadīṯ 2873, chiffre imprimé inversé, tranché",
    "l’orphelinat cesse après la puberté",
    "sur le sens de la compassion envers eux",
    "ʿIkrima et Qatāda dirent",
    "Ibn ʿAbbās dit : c’était une science en des feuillets enfouis",
    "une tablette d’or où étaient écrits des jugements et des admonitions",
    "ce que je dis de correct en cela est ce que dit ʿIkrima",
    "le trésor est le nom de ce qui est thésaurisé de la richesse",
    "l’interprétation est reportée au plus fréquent de l’usage des interlocuteurs",
    "peut-être l’ai-je exposé en un autre lieu",
    "règle d’or en l’exégèse de ce en quoi tomba la divergence des sens du Qurʾān",
    "le coutumier de l’usage des Arabes en la langue desquels le Qurʾān descendit",
    "préservés que furent les deux par la sainteté de leur père",
    "il n’attribua la volonté qu’à lui-même",
    "comme s’édifia Ibrāhīm — sur lui la paix — en sa parole : « et quand je suis malade, c’est Lui qui me guérit »",
    "les Poètes : 80 — renvoi tranché",
    "attribuant l’acte, avant et après, à Dieu — Très-Haut —, et la maladie à lui-même, car elle est sens de défaut et de calamité",
    "ce procédé court, en l’éloquence du Qurʾān, abondamment",
    "ils souhaitèrent le remplaçant pour eux",
    "il attribua la volonté, en la troisième, à Dieu — Très-Haut —",
    "une affaire reprise au long du temps, un caché des cachés",
    "quand bien même al-Khiḍr aurait aussi voulu cela même dont Dieu l’informa qu’Il le veut",
    "selon notre entendement défaillant — et Dieu sait mieux",
    "la complétude de la constitution et de la raison",
    "il fut dit trente-cinq, il fut dit trente-six, il fut dit quarante",
    "l’atteinte de quarante années",
    "« jusqu’à ce qu’ayant atteint sa force complète, il ait atteint quarante années... »",
    "al-Aḥqāf : 15 — renvoi tranché",
    "az-Zamaḫšarī et Abū al-Baqāʾ al-ʿUkbarī dirent qu’elle se dresse à l’accusatif circonstanciel",
    "Abū Ḥayyān affaiblit ces deux dernières faces",
    "revient sur les trois actes antérieurs d’al-Khiḍr",
    "la percée du navire, la mise à mort du garçon et l’édification du mur",
    "d’un effort personnel de moi : je ne le fis que par l’ordre de Dieu",
    "ceci est l’exposé de ce sur quoi tu ne pus prendre patience",
    "jusqu’à ce que je te l’eusse exposé de prime abord",
    "la forme allégée du verbe de la capacité, en l’usage des Arabes",
    "Al-Qurṭubī — que Dieu lui fasse miséricorde — dit, en Sa parole « et leur père était un homme vertueux »",
    "préserve le vertueux en sa propre personne et en sa progéniture",
    "la préservation étendue à sept de sa postérité",
    "l’œuvre par les utilités, et l’entreprise du moindre des deux maux en précaution du pire",
    "règle juridique considérée lors de la collision des maux",
    "du réalisme de l’islam et de son dessein",
    "la préservation des droits des miséreux, des pauvres et des orphelins est des beautés de l’éthique, et des voies des prophètes et des vertueux",
    "le misérable est celui qui a la subsistance de l’existence — tel le navire de ceux-ci",
    "l’ajustement de cela, à mon avis : ce sont deux vocables dénotant la faiblesse de l’état",
    "la mise à nu et la demande",
    "Dieu en fit deux espèces en la part des aumônes",
    "les gens du besoin qui ont découvert leurs visages",
    "les gens du besoin qui n’ont point découvert leurs visages",
    "la Vache : 273 — renvoi imprimé altéré, tranché",
    "pour les pauvres qui sont retenus en la voie de Dieu",
    "al-Muḥarrar al-waǧīz",
    "métonymie lâche — on y exprima la mainmise et la rapine par la prise",
    "la vérité de la prise n’est que par la main — sa relation est l’instrumentalité : la main est l’instrument de la prise",
    "En Sa parole « il y avait derrière eux un roi » : sur qui revient le pronom ?",
    "À qui revient le « nous » en Sa parole",
    "Que dénote Sa parole",
    "la conduite d’al-Khiḍr en la mise à mort du garçon n’est point de la station de la législation",
    "Je résume, en une charpente",
    "le récit de Mūsā et d’al-Khiḍr, en valeurs et en jugements",
    "le récit de Mūsā — que la paix soit sur lui — et d’al-Khiḍr : leçons et enseignements",
    "en coopération avec mes camarades et sous la conduite du maître (ou de la maîtresse)",
    "L’exposé des contenus d’ensemble du récit de Mūsā",
    "La rédaction d’une conclusion synthétique des résultats des travaux des groupes",
    "plage imprimée 82 à 84 — cache 83 à 85 selon le décalage établi",
    "NUM imprimé relu en chiffres latins intacts en l’ʾiʿdād qiblī de p.164",
    "qui est Dhū al-Qarnayn, et par quoi ces āyāt le dépeignirent-elles ?",
    "la leçon suivante ouvre en la page 165 du même manuel",
    "précédent de la leçon 21 ici même",
    "kahf-probe-l21.py",
    "« Sourate al-Kahf, les versets (78 - 81) »",
    "le NUM (82-84) de la leçon suivante en chiffres latins intacts",
    "« Sourate al-Kahf, les versets (82 - 84) »",
    "la citation [al-Kahf : 82 _ 84] de p.165",
]
for c in contenu:
    if c.lower() not in norm.lower():
        errors.append(f"contenu attendu absent : {c[:55]}")

# 4. rendus interdits (āyāt 1-78 livrées leçons 739-758 ; 83-110 leçon 760+)
interdits_src = (1, 10, 26, 32, 45, 46, 57, 59, 60, 61, 62, 65, 71, 74, 75, 76, 77, 78, 83, 84, 85)
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
for n in list(range(1, 79)) + list(range(83, 111)):
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
print(f"verify-759-quran : {total} contrôles — rendus {len(rendus)} + contenu {len(contenu)} + interdits {len(interdits)} + rasm {rasm_n} + structure {22} + typo 3")
if errors:
    print("verify-759 FAIL :")
    for e in errors:
        print(" -", e)
    sys.exit(1)
print("verify-759 PASS")

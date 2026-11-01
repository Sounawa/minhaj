#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Minhāj — contrôle coranique de la leçon 736 (tafsir-5ep, Isrāʾ 109-110).
Vérifie : rendus français des deux āyāt 109-110 (rasm warš du cache — «
tombent le menton contre terre, en pleurant », « et cela accroît leur
humilité », « Invoquez Allah, ou invoquez le Tout Miséricordieux », « à Lui
appartiennent les plus beaux noms », « cherche, entre les deux, une voie »),
le lemme d'appui 111 du tafsīr rendu sur le cache (« Louange à Allah, qui ne
S'est point attribué d'enfant, qui n'a point d'associé dans la royauté, et qui
n'a point de protecteur contre l'humiliation. Et magnifie-Le d'une
magnification »), les gloses du tafsīr (la cause de la descente — Ibn ʿAbbās «
un dieu unique... il en invoque deux » — et Mukaḥḥol « Ô Tout Miséricordieux,
Ô Miséricordieux » et l'auditeur « le Raḥmān de la Yamāma » tranché par le
Muḥarrar, le Nommé un seul, l'invocation transitive à deux compléments dont le
premier supprimé au sens de la nomination (at-tasmīya), al-Bayḍāwī — le choix
(at-taḫyīr) et le fait de se passer — et « ayyā » nom interrogatif, le (mā)
superflu donnant la condition comme « kayf » et le jussif de « tadʿū » avec
réponse couplée au fāʾ, Ibn ʿĀšūr — le tanwīn de « ayyan » tenant lieu de
l'annexé et le « hā » complétive de confirmation de l'indétermination et le
pronom de « à Lui » renvoyant au nommé (musammā) — Son essence — et les deux
noms beaux faisant partie des beaux —, ar-Rāzī Mafātīḥ al-ġayb t. 12 p. 814 ;
la réalité de la dissimulation (isrār) et l'abaissement de la voix, les
interprètes — Ibn ʿAbbās et ʿĀʾiša et un groupe : l'invocation — Ibn ʿAbbās
aussi : la lecture du Coran dans la prière sur suppression de l'annexé — la
cause : le Prophète ﷺ rendant public le Coran et les associateurs revilérant
et la commande du juste milieu, Ibn Sīrīn — les Bédouins et le tašahhud —,
Abū Bakr « Je m'entretiens en secret avec mon Seigneur » et ʿUmar « je chasse
le diable et j'éveille l'endormi » et « Élève un peu » / « Abaisse un peu »,
ʿĀʾiša — le tašahhud — Ibn ʿAbbās et al-Ḥasan — la voie moyenne en tout état
—, Ibn Zayd — les gens de l'Évangile et de la Torah —, Ibn ʿAbbās — la prière
du jour et la prière de la nuit — mentionné par Yaḥyā b. Salām et az-Zahrāwī,
Ibn Masʿūd — l'abaissement n'est pas de ce que ses deux oreilles entendent —
et le rejet du rapport d'Abū Bakr et l'origine de la langue et le (ḫufūt) ;
la transition, l'āya 111 tranchée par le Muḥarrar, la réponse aux trois
peuples — juifs, chrétiens et Arabes — dans leur dire vaniteux (« afḍāḏā ») :
ʿUzayr, ʿĪsā et les anges, la réponse aux Arabes — « si les amis d'Allah
n'étaient pas, nous serions abaissés » — et la restriction de la lettre de
l'āya (la voie de l'abaissement et le côté de l'appui victorieux, Sa wilāya
par Sa faveur et Sa miséricorde), Muǧāhid — Il ne S'allia à personne — le
masdar et l'āya de la Puissance (āyat al-ʿizz), Muṭarrif de ʿAbd Allāh b. Kaʿb
— la Torah ouverte par l'ouverture d'al-Anʿām et close par la conclusion de
cette sūra —, les finalités (4), l'évaluation (3), l'exploitation (ar-Rāzī —
les conditions de l'involution : la grandeur d'Allah et l'abaissement du
serviteur, l'exemple : l'âme et le corps et la puissance rationnelle, les
animaux et les plantes et les minéraux et le tonnerre et l'éclair, les strates
des terres et des cieux et les orbes, les astres fixes et les errants, le
Piédestal et le Jujubier de la Limite, le Trône immense et ses porteurs et les
armées du monde des esprits, « Allah est le plus grand », le néant à l'être,
la suffisance à soi, la mesure du dhikr avec la connaissance et la
conscience —, la question du redressement de la conduite et de la droiture),
les repères « 901 - 011 » (préparation de la leçon précédente), la clôture de
la sourate (fihris aux pages 209-214), l'absence de citations hors rasm
(17:105-108 = leçon précédente — interdits au corps après l'évaluation ; la
glose de 17:109 livrée par la leçon 27 — non redite), 0 arabe résiduel.
Espaces typographiques (NNBSP/insécables) introduits par l'auto-fix de
qa-lesson normalisés avant appariement."""
import json
import re
import sys

HTML = "scripts-translate/tr-tmp/pdf-mut23h3c-736.html"
html = open(HTML, encoding="utf-8").read()
norm = html.replace("\u202f", " ").replace("\u00a0", " ")
errors = []

for frag in [
    "tombent le menton contre terre, en pleurant",
    "et cela accroît leur humilité",
    "Invoquez Allah, ou invoquez",
    "le Tout Miséricordieux",
    "Quel que soit celui des deux par lequel vous L’invoquerez",
    "à Lui appartiennent les plus beaux noms",
    "cherche, entre les deux, une voie",
    "ne S’est point attribué d’enfant",
    "n’a point d’associé dans la royauté",
    "n’a point de protecteur contre l’humiliation",
    "Et magnifie-Le d’une magnification",
]:
    if frag not in norm:
        errors.append(f"rendu attendu absent : {frag[:55]}")

if not re.search(r"»\s*\(109-110\)", norm):
    errors.append("repère de plage (109-110) absent")

for frag in [
    "Que je reconnaisse que la multiplicité des noms excellents d’Allah ne dément point Son unicité",
    "Que j’extraie des deux āyāt la méthode de la voie moyenne et de la modération",
    "Que je me remémore les grâces d’Allah sur nous et que je Le loue pour elles",
    "eut établi le miracle du Noble Coran pour les mondes",
    "associerait le très-Haut quand il L’invoque par Ses noms excellents",
    "entre l’éclat de la voix et la dissimulation",
    "ni géniteur ni enfant",
    "« 901 - 011 »",
    "[Des bandes d’entrées du glossaire imprimé sont dégradées dans la couche texte — déclarées perdues",
    "« ne la murmure pas » (lā tuḫāfit bi-hā — lemme imprimé altéré, tranché par la matière)",
    "tu n’abaisse pas ta voix au point que personne derrière toi ne t’entende dans la prière",
    "« et qui n’a point de protecteur » (wa-lam yakun la-hū walī — lemme imprimé altéré, tranché par la matière)",
    "Il n’eut point de secoureur",
    "l’impuissance et du besoin",
    "« et magnifie-Le » (wa-kabbir-hu — lemme imprimé altéré, tranché par la matière)",
    "le tenir pour grand",
    "La multiplicité des noms excellents d’Allah dément-elle Son unicité",
    "contenue dans les deux āyāt",
    "« quli dʿū llāha awi dʿū r-raḥmān » — al-Isrāʾ : 110",
    "propos d’Ibn ʿAbbās",
    "Mukaḥḥol a dit : le Prophète ﷺ veilla en prière une nuit",
    "le Raḥmān de la Yamāma",
    "passage altéré dans la couche texte — tranché par le Muḥarrar",
    "montrant que le Nommé est un seul",
    "elle transite vers deux compléments dont le premier est supprimé, au sens de la nomination (at-tasmīya)",
    "Anwār at-tanzīl wa-asrār at-taʾwīl — rangs imprimés altérés",
    "pour le choix (at-taḫyīr) et le fait de se passer de",
    "« ayyā » est un nom interrogatif",
    "comme la donne « comment » (kayf) quand on le joint au (mā) superflu en l’origine",
    "le verbe qui le suit est au jussif — « tadʿū » —, étant une condition",
    "une réponse couplée avec le fāʾ",
    "at-Taḥrīr wa-t-tanwīr — rangs imprimés altérés",
    "le tanwīn de « ayyan » tient lieu de l’annexé",
    "une complétive venant confirmer ce que comporte l’annexé d’indétermination",
    "lequel de ces deux noms vous aurez nommé",
    "ne renvoie pas à l’un des deux noms cités, mais à leur nommé (musammā)",
    "Sa propre essence, exaltée et très-haute",
    "ces deux noms le sont, faisant partie d’eux",
    "Ar-Rāzī, Mafātīḥ al-ġayb, t. 12, p. 814 de l’imprimé",
    "« wa-lā taǧhar bi-ṣalāti-ka wa-lā tuḫāfit bi-hā » — al-Isrāʾ : 110",
    "la réalité de la dissimulation (isrār) est ce dont celui qui parle n’est pas entendu",
    "l’expression de l’abaissement de la voix",
    "Ibn ʿAbbās et ʿĀʾiša et un groupe dirent : c’est l’invocation",
    "c’est la lecture du Coran dans la prière — sur suppression de l’annexé",
    "ne rends pas public, de ta prière, la lecture",
    "revilèrent le Coran et Celui qui l’avait fait descendre",
    "fut commandé au juste milieu",
    "les Bédouins faisaient éclater leur tašahhud — l’āya descendit sur cela",
    "Abū Bakr — qu’Allah l’agrée — récitait à voix basse",
    "Je m’entretiens en secret avec mon Seigneur, et Lui connaît mon besoin",
    "je chasse le diable et j’éveille l’endormi",
    "il fut dit à Abū Bakr : \"Élève un peu\", et à ʿUmar : \"Abaisse un peu\"",
    "désigne le tašahhud",
    "ne fais pas bien ta prière dans l’éclat, ni ne la fais mal dans le secret",
    "une voie moyenne qui demeure en tout état",
    "les gens de l’Évangile et de la Torah",
    "ne rends pas public la prière du jour, et n’abaisse pas la prière de la nuit",
    "mentionné par Yaḥyā b. Salām et az-Zahrāwī",
    "l’abaissement n’est pas de ce que ses deux oreilles entendent",
    "est rejeté ; mais la parole d’Ibn Masʿūd est l’origine de la langue",
    "l’étouffement (ḫufūt) est employé ensuite pour ce qui est plus haut que cela",
    "l’éclat dans l’invocation ou la lecture de la prière",
    "[un membre est dégradé dans la couche texte — déclaré] dans la croyance des associateurs",
    "« wa-quli l-ḥamdu li-llāhi lladī lam yattāḫiḏ waladan",
    "wa-kabbir-hū takbīrā » — al-Isrāʾ : 111",
    "leur dire vaniteux (\"afḍāḏā\")",
    "ʿUzayr, ʿĪsā et les anges sont la progéniture d’Allah",
    "si les amis d’Allah n’étaient pas, nous serions abaissés",
    "par la voie de l’abaissement et du côté de l’appui victorieux",
    "par Sa faveur et Sa miséricorde, pour quiconque Il prend en amitié parmi les justes de Ses serviteurs",
    "Il ne S’allia à personne et ne chercha l’appui de personne",
    "le mot le plus éloquent pour les Arabes au sens de la vénération et de la glorification",
    "l’accentua par le nom verbal (masdar), pour sa réalisation et la pleine atteinte de son sens",
    "l’āya de la Puissance (āyat al-ʿizz)",
    "Muṭarrif rapporta de ʿAbd Allāh b. Kaʿb",
    "J’ai ouvert la Torah par l’ouverture de sūrat al-Anʿām, et je l’ai close par la conclusion de cette sūra",
    "la pluralité des divinités, ainsi que les associateurs l’ont faussement compris",
    "d’un secoureur et d’un appui",
    "par quel que nom qu’ils L’invoquent — le Tout Miséricordieux ou le Miséricordieux",
    "l’Unique, le Puissant",
    "au doute des associateurs relatif à Son nom « le Tout Miséricordieux »",
    "le principe de la voie moyenne et de la modération",
    "l’āya de la Puissance » ? Et quel est le dessein de sa dénomination ainsi",
    "la grandeur d’Allah et l’abaissement du serviteur",
    "l’une d’elles est la grandeur d’Allah, la seconde est l’abaissement du serviteur",
    "là, cette invocation est belle, et là est la servitude",
    "de son âme, de son corps et de sa puissance rationnelle",
    "traces vivantes ou motrices",
    "toutes les espèces de plantes et de minéraux",
    "le tonnerre et l’éclair",
    "des strates des terres, des monts, des mers et [fragment perdu — déclaré]",
    "les inférieures et les supérieures",
    "les strates des cieux selon leur ampleur et leur grandeur",
    "les astres fixes et les errants",
    "le Piédestal (al-Kursī) et du Jujubier de la Limite",
    "le Trône immense entourant tous ces existants",
    "les porteurs du Trône et du Piédestal",
    "les armées du monde des esprits",
    "la disparité de leurs degrés et la distinction de leurs rangs et de leurs niveaux",
    "il dit : \"Allah est le plus grand\"",
    "a créé ces choses du néant à l’être",
    "les a élevées par les qualités et les descriptions qui sont les leurs",
    "pour Sa magnificence et Sa toute-puissance, Son exaltation, Sa transcendance et Sa suffisance à soi",
    "Il est plus grand que de dire : \"Il est plus grand que ces choses\"",
    "mesure le dhikr obtenu avec la connaissance et la conscience",
    "[la fin du passage est dégradée dans la couche texte — déclarée]",
    "Ar-Rāzī, Mafātīḥ al-ġayb d’al-Faḫr ad-Dīn ar-Rāzī — rangs imprimés altérés",
    "le redressement de la conduite et la droiture de l’homme",
    "la citation coranique imprimée d’ouverture est altérée au point de n’être pas restituable",
    "le passage porte sur Sa parole « et magnifie-Le d’une magnification » — al-Isrāʾ : 111",
    "les pages imprimées 209 à 214 portent l’index des figures citées (fihris)",
    "aucune préparation de leçon suivante n’y figure",
    "la préparation de la leçon 27 annonçait les deux āyāt 109-110",
    "tranchée par le Muḥarrar et les fenêtres du dépôt",
]:
    if frag not in norm:
        errors.append(f"glose/nom attendu absent : {frag[:55]}")

def bare(t: str) -> str:
    return re.sub(r"[\u064B-\u065F\u0670\u06D6-\u06ED\u0640\u0671]", "", t)

cache = json.load(open("scripts-translate/quran-cache.json", encoding="utf-8"))
ar17 = dict((i, t) for i, t in cache["17"]["ar"])
v109, v110, v111 = bare(ar17[109]), bare(ar17[110]), bare(ar17[111])
if "ويخرون للأذقان يبكون ويزيدهم خشوعا" not in v109:
    errors.append("cache 17:109 inattendu")
for f in ["قل دعوا لله أو دعوا لرحمن", "أيا ما تدعوا فله لأسماء لحسنى",
          "ولا تجهر بصلاتك ولا تخافت بها وبتغ بين ذلك سبيلا"]:
    if f not in v110:
        errors.append(f"cache 17:110 inattendu ({f[:30]})")
for f in ["وقل لحمد لله لذى لم يتخذ ولدا ولم يكن له شريك فى لملك ولم يكن له ولى من لذل",
          "وكبره تكبيرا"]:
    if f not in v111:
        errors.append(f"cache 17:111 inattendu ({f[:30]})")

# citations hors rasm — interdites au corps après l'évaluation
# (17:105-108 = leçon précédente 735 ; la glose de 17:109 y fut aussi livrée)
body = norm.split("<h2>L’évaluation", 1)[1]
for pat, label in [
    (r"Croyez-y", "al-Isrāʾ 17:107 (leçon précédente — non portée)"),
    (r"annonciateur et avertisseur", "al-Isrāʾ 17:106 (leçon précédente — non portée)"),
    (r"avec lenteur", "al-Isrāʾ 17:106 (leçon précédente — non portée)"),
    (r"descendant par descendant", "al-Isrāʾ 17:106 (leçon précédente — non portée)"),
    (r"furent dotés du savoir avant lui", "al-Isrāʾ 17:107 (leçon précédente — non portée)"),
    (r"la promesse de notre Seigneur", "al-Isrāʾ 17:108 (leçon précédente — non portée)"),
    (r"l’exagération dans leur description", "glose de 17:109 livrée par la leçon 27"),
    (r"at-Tamīmī", "glose de 17:109 livrée par la leçon 27"),
]:
    if re.search(pat, body, re.IGNORECASE):
        errors.append(f"citation inattendue : {label}")

if re.search(r"[\u0600-\u06FF\u0750-\u077F\u08A0-\u08FF\uFB50-\uFDF9\uFDFB-\uFDFF\uFE70-\uFEFF]", norm):
    errors.append("caractère arabe résiduel détecté")

if errors:
    print("ÉCHEC :")
    for e in errors:
        print(" -", e)
    sys.exit(1)
print("PASS : leçon 736 — les deux āyāt 109-110 rendues sur le rasm warš du cache "
      "(« tombent le menton contre terre, en pleurant, et cela accroît leur humilité », « "
      "Invoquez Allah, ou invoquez le Tout Miséricordieux », « à Lui appartiennent les plus "
      "beaux noms », « cherche, entre les deux, une voie »), le lemme d'appui 111 du tafsīr "
      "rendu sur le cache (« Louange à Allah, qui ne S'est point attribué d'enfant, qui n'a "
      "point d'associé dans la royauté, et qui n'a point de protecteur contre l'humiliation. "
      "Et magnifie-Le d'une magnification »), les gloses du tafsīr tranchées par le Muḥarrar "
      "(la cause de la descente — Ibn ʿAbbās et Mukaḥḥol et le Raḥmān de la Yamāma —, le "
      "Nommé un seul, l'invocation à deux compléments et al-Bayḍāwī et le (mā) superflu et "
      "Ibn ʿĀšūr et ar-Rāzī t. 12 p. 814 ; la dissimulation et les interprètes — l'invocation "
      "et la lecture sur suppression de l'annexé — et la commande du juste milieu, Ibn Sīrīn "
      "et Abū Bakr et ʿUmar et ʿĀʾiša et Ibn Zayd et Yaḥyā b. Salām et az-Zahrāwī et Ibn "
      "Masʿūd ; la réponse aux trois peuples et la restriction de la wilāya et Muǧāhid et "
      "l'āya de la Puissance et Muṭarrif — la Torah ouverte par al-Anʿām), les finalités (4), "
      "l'évaluation (3), l'exploitation (ar-Rāzī — la grandeur et l'abaissement, l'exemple de "
      "la création jusqu'au Trône et ses porteurs, « Allah est le plus grand », la mesure du "
      "dhikr), la clôture de la sourate (fihris aux pages 209-214), aucune citation hors rasm "
      "(17:105-108 interdits au corps après l'évaluation — leçon précédente ; la glose de "
      "17:109 non redite), 0 arabe résiduel.")

if __name__ == "__main__":
    sys.exit(0)

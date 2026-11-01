#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Minhāj — contrôle coranique de la leçon 735 (tafsir-5ep, Isrāʾ 105-108).
Vérifie : rendus français des quatre āyāt 105-108 (rasm warš du cache — « Et en
vérité, Nous l'avons fait descendre, et en vérité il est descendu », «
annonciateur et avertisseur », « que Nous avons fragmenté », « pour que tu le
récites aux gens avec lenteur », « descendant par descendant », « Croyez-y, ou
n'y croyez pas », « furent dotés du savoir avant lui », « tombent le menton
contre terre, prosternés », « Gloire à notre Seigneur », « s'accomplira
assurément »), le lemme d'appui 109 du tafsīr (« en pleurant, et cela accroît
leur humilité »), la citation du hadith d'Ibn Masʿūd (an-Nisāʾ : 41 — « quand
Nous viendrons de chaque communauté un témoin », « comme témoin contre
ceux-ci »), les gloses du tafsīr (la reprise du discours et la notoriété,
az-Zahrāwī — l'utilité et la rectitude — et aṭ-Ṭabarī un seul sens,
l'annonciateur de la récompense et l'avertisseur du châtiment, le kāf de
arsalnā-ka et l'envoi et la descente d'un seul sens, le commun des lecteurs «
fa-raqnā-h » à la rāʾ légère et le discernement (furqān), les huit lecteurs et
Ḥumayd et ʿAmr b. Fāʾid à la rāʾ géminée, la lecture d'Ibn Masʿūd et d'Ubayy «
fa-raqnā-hu ʿalayka li-taqrʾa-h » et la concordance avec « li-taqrʾa-hu ʿalā
n-nāsi ʿalā makth », les causes sur terre et les temps bornés, les durées —
vingt-cinq, vingt-trois (Ibn ʿAbbās), vingt (Qatāda) —, la révélation débutée
à quarante ans, al-Ḥasan al-Baṣrī dix-huit ans, les deux exégèses de « ʿalā
makth » — Muǧāhid, Ibn ʿAbbās, Ibn Ǧurayǧ, Ibn Zayd —, le masdar de «
wa-nazzalnā-hu tanzīlan », la transition, la parole « qul ʾāminū bi-hi »
humiliation et menace et l'argument des gens du savoir, Waraqa b. Nawfal et
Zayd b. ʿAmr b. Nufayl et le groupe qui s'inclina vers l'Islam, la fraction de
Muḥammad ﷺ et les pronoms et la reprise de la mention, « li-l-ʾaḏqān » pour sa
direction et Ibn ʿAbbās les visages et al-Ḥasan la barbe et les mentons où se
rejoignent les deux barbes, le « in » de « in kāna » chez Sībawayh lightened de
la heavy et lām de l'affirmation et chez al-Farrāʾ néantissante et lām « sauf
», la purification de la menace et « vous verrez ce que vous subirez », la
réprobation par les gens du Livre — Torah et Évangile et Psaumes —, la glose
de l'āya 109 et l'exhortation au rang et at-Tamīmī et le savoir qui ne fait
pas pleurer, les finalités (5), l'évaluation (4 — lemme du style rhétorique
déclaré), l'exploitation (al-Bukhārī — Ibn Masʿūd, « J'aime à l'entendre
d'autre que moi », les yeux versant des larmes, an-Nisāʾ : 41 au rasm du
cache, la première question déclarée, la question d'effet et la purification
et l'éducation), la préparation 109-110 au DOM — imprimé « 901 - 011 » inversé
—, les fragments « tadʿū » et « al-ʾasmāʾ » conformes au rasm du cache de
l'āya 110, l'absence de citations hors rasm (17:101-104 = leçon précédente ;
17:110 et 17:111 = leçon suivante — interdits au corps après l'évaluation), 0
arabe résiduel. Espaces typographiques (NNBSP/insécables) introduits par
l'auto-fix de qa-lesson normalisés avant appariement."""
import json
import re
import sys

HTML = "scripts-translate/tr-tmp/pdf-mut23h3c-735.html"
html = open(HTML, encoding="utf-8").read()
norm = html.replace("\u202f", " ").replace("\u00a0", " ")
errors = []

for frag in [
    "Et en vérité, Nous l’avons fait descendre, et en vérité il est descendu",
    "qu’annonciateur et avertisseur",
    "que Nous avons fragmenté",
    "pour que tu le récites aux gens avec lenteur",
    "descendant par descendant",
    "Croyez-y, ou n’y croyez pas",
    "furent dotés du savoir avant lui",
    "tombent le menton contre terre, prosternés",
    "Gloire à notre Seigneur",
    "s’accomplira assurément",
    "en pleurant, et cela accroît leur humilité",
    "quand Nous viendrons de chaque communauté un témoin",
    "comme témoin contre ceux-ci",
]:
    if frag not in norm:
        errors.append(f"rendu attendu absent : {frag[:55]}")

if not re.search(r"»\s*\(105-108\)", norm):
    errors.append("repère de plage (105-108) absent")

for frag in [
    "Que je reconnaisse la place du Noble Coran et la caractéristique de sa descente",
    "Que je distingue entre les associateurs et les vertueux d’entre les gens du Livre",
    "Que je suive l’exemple des vertueux d’entre les gens du Livre",
    "que le Coran est un miracle véridique en ce qu’il rapporte",
    "ceux que les associateurs tiennent en magnification",
    "crurent en lui et s’humilièrent à son audition",
    "« 801 - 5 »",
    "[Des bandes d’entrées du glossaire imprimé sont dégradées dans la couche texte — déclarées perdues.]",
    "« Et en vérité il est descendu » (wa-bi-l-ḥaqqi nazala — lemme imprimé altéré, tranché par la matière)",
    "le Coran est descendu en vérité dans Ses commandements, Ses interdictions et Ses récits",
    "« et Nous l’avons fragmenté » (fa-raqnā-h — lemme imprimé altéré, tranché par la matière)",
    "en parties séparées, parcellisées, non d’un seul tenant",
    "« avec lenteur » (ʿalā makth — lemme imprimé altéré, tranché par la matière)",
    "une trêve et une lenteur, pour que celui qui l’écoute le comprenne",
    "les croyants d’entre les gens du Livre, d’entre les juifs et les chrétiens",
    "« le tomber » (al-ḫurūr) : la chute du corps",
    "Par quoi Allah — gloire à Lui — a-t-Il marqué Sa distinction dans ces āyāt",
    "a-t-Il répondu à celui qui a nié le Noble Coran",
    "« wa-bi-l-ḥaqqi anzalnā-hu wa-bi-l-ḥaqqi nazala » — al-Isrāʾ : 105",
    "le pronom revient au Coran, Allah — très-Haut — L’ayant indiqué par le pronom sans mention antérieure",
    "le discours est repris de nouveau",
    "l’utilité et la rectitude pour les gens, en vérité dans Ses commandements, Ses interdictions et Ses récits",
    "la répétition du mot porte un sens autre que le premier",
    "aṭ-Ṭabarī a tenu qu’ils sont d’un seul sens",
    "Il est descendu par Ses récits et Ses commandements — et ainsi est Sa descente",
    "qu’annonciateur pour qui Nous obéit de la récompense, et avertisseur pour qui Nous désobéit du châtiment",
    "l’envoi de celui-ci et la descente de celui-ci furent d’un seul sens",
    "a lu « fa-raqnā-h » avec la rāʾ légère",
    "Nous l’avons éclairci, explicité et fait un discernement (furqān)",
    "« fa-rraqnā-h » avec la rāʾ géminée",
    "les noms des lecteurs sont tronqués dans la couche texte — tranchés par le Muḥarrar",
    "Ibn ʿAbbās, Qatāda, Abū Raǧāʾ, ʿAlī b. Abī Ṭālib, Ibn Masʿūd, Ubayy b. Kaʿb, aš-Šaʿbī, al-Ḥasan — et Ḥumayd et ʿAmr b. Fāʾid",
    "dans la lecture d’Ibn Masʿūd et d’Ubayy",
    "« fa-raqnā-hu ʿalayka li-taqrʾa-h » : à savoir : Nous l’avons fait descendre chose après chose, non d’un seul tenant",
    "« li-taqrʾa-hu ʿalā n-nāsi ʿalā makth »",
    "des causes qui surviennent sur terre, de paroles et d’actes, en temps bornés et précis",
    "au sujet de la durée de la descente du Coran : il fut dit : en vingt-cinq ans",
    "Ibn ʿAbbās a dit : en vingt-trois ans",
    "Qatāda a dit : en vingt ans",
    "la révélation débuta quand il avait quarante ans et s’acheva par sa mort",
    "tranché par le Muḥarrar : d’al-Ḥasan al-Baṣrī",
    "le Coran est descendu en dix-huit ans",
    "comme le débit (at-tarasul) dans la récitation, qui est la récitation mesurée (tartīl)",
    "c’est le dire de Muǧāhid, d’Ibn ʿAbbās, d’Ibn Ǧurayǧ et d’Ibn Zayd",
    "le prolongement dans la durée, chose après chose",
    "l’exagération et l’accentuation par le masdar du sens avancé déjà mentionné dans les mots de l’āya",
    "Après la distinction qu’Allah — gloire à Lui — fait du Noble Coran et l’exposé de la caractéristique de sa descente",
    "Il a exposé la différence des gens [la suite de la transition est dégradée dans la couche texte — déclarée]",
    "alors que les associateurs s’obstinaient, et la foi des vertueux d’entre les gens du Livre en lui",
    "cette āya est une humiliation des mécréants, et dans son sens une forme de menace (tawʿīd)",
    "vous n’êtes pas en position d’argument",
    "le tort retombe sur vos propres personnes",
    "l’argument n’est que pour les gens du savoir d’avant lui, eux qui sont de la description mentionnée",
    "ce sont les croyants d’entre les gens du Livre",
    "Waraqa b. Nawfal, Zayd b. ʿAmr b. Nufayl et ceux qui suivirent leur voie",
    "c’est le temps de la prophétie mentionnée dans la Torah, et voici sa description",
    "la promesse d’Allah à son sujet adviendra immanquablement",
    "et ils s’inclinèrent vers cet Islam d’une inclination, et l’āya descendit à leur sujet",
    "ce que vise « alladīna ūtū l-ʿilma min qabli-hi » est Muḥammad ﷺ",
    "le pronom de « min qabli-hi » revient au Coran selon le pronom de « bi-hi »",
    "les deux pronoms [reviennent] à Muḥammad",
    "la mention du Coran est reprise de nouveau dans Sa parole (iḏā yutlā)",
    "« li-l-ʾaḏqān »",
    "pour sa direction — et cela comme on dit : [ils tombèrent] pour la main et la bouche",
    "Ibn ʿAbbās a dit : le sens est pour les visages",
    "al-Ḥasan a dit : le sens est pour la barbe",
    "« les mentons » (al-ʾaḏqān) : les parties inférieures des visages là où se rejoignent les deux barbes",
    "surtout à sa prosternation",
    "« in kāna waʿdu rabbinā lamafʿūlan » — al-Isrāʾ : 108",
    "il est, chez Sībawayh, la lightened de la heavy, et la lām qui le suit est la lām de l’affirmation",
    "il est, chez al-Farrāʾ, une néantissante, et la lām au sens de « sauf »",
    "soit une purification de la menace, sans l’humiliation",
    "vous verrez ce que vous subirez en échange",
    "l’exemple en mode de réprobation par ceux d’entre les gens du Livre qui précédèrent",
    "ceux à qui furent donnés la Torah et l’Évangile et les Psaumes et les livres faits descendre en général",
    "ils s’humilient et croient",
    "« wa-yaḫirrūna li-l-ʾaḏqāni yabkūna wa-yazīdu-hum ḫušūʿan » — al-Isrāʾ : 109",
    "une exagération dans leur description et leur louange",
    "une exhortation pour quiconque s’est appliqué dans le savoir et en a obtenu quelque chose de courir vers ce rang",
    "aṭ-Ṭabarī a rapporté d’at-Tamīmī qu’il a dit",
    "quiconque s’est vu donner du savoir sans qu’il ne pleure, il est digne qu’on ne lui ait pas donné un savoir profitable",
    "Allah — très-Haut — a décrit les savants — et il récita cette āya tout entière",
    "L’attestation d’Allah — gloire à Lui — de la véracité du Noble Coran",
    "dans Ses récits, Ses ordonnances et Ses lois, et le certificateur du messager",
    "La distinction par l’importance du Noble Coran et sa valeur",
    "qui se réduit à transmettre le message de son Seigneur, sans contrainte ni forçage",
    "la non-valeur argumentative de ce que les associateurs mettent en avant de tergiversation",
    "eux meilleurs qu’eux et plus savants",
    "où Il le lui fit descendre parcellisé et en parties séparées, selon les événements et les circonstances",
    "pour que ses mots et ses sens s’affermissent dans les âmes des croyants",
    "Quelle est la sagesse de la descente par Allah — gloire à Lui — du Coran parcellisé et en parties séparées",
    "au devant de la réponse aux associateurs qui dénièrent ses āyāt",
    "« [lemme coranique imprimé altéré — déclaré] » et son effet dans le sens de l’āya",
    "[la citation coranique imprimée est altérée : il s’y lit les repères de « Maryam » et d’« az-Zumar » aux rangs altérés",
    "ʿAbd Allāh b. Masʿūd — qu’Allah l’agrée — : \"Récite-moi du Coran\"",
    "te réciterais-je, alors que c’est sur toi qu’il fut fait descendre",
    "J’aime à l’entendre d’autre que moi",
    "[un membre du texte est dégradé dans la couche texte — déclaré]",
    "« fa-kayfa iḏā jiʾnā min kulli ummatin bi-šahīdin » — an-Nisāʾ : 41",
    "ses deux yeux se mettaient à verser des larmes",
    "Ṣaḥīḥ al-Bukhārī — livre du tafsīr du Coran",
    "[une première question est dégradée dans la couche texte — déclarée]",
    "Quel est l’effet du Noble Coran dans les âmes des humbles",
    "son rôle dans la purification et l’éducation des âmes",
    "āyāt 109 à 110 de sūrat al-Isrāʾ",
    "« 901 - 011 »",
    "« 109 » et « 110 »",
    "versets 109-110",
    "Comment est-ce que j’argumente l’unicité d’Allah — très-Haut — à travers la pluralité de Ses noms excellents",
    "des fragments de « tadʿū » et de « al-ʾasmāʾ », conformes au rasm du cache de l’āya 110",
    "de règles et d’évaluations grammaticales",
    "la descente en toute vérité, l’annonciateur et l’avertisseur, le Coran fragmenté et la récitation avec lenteur",
    "matière de la leçon suivante (leçon 28)",
    "tranchent mot pour mot les gloses lacérées",
    "l’exégèse d’az-Zahrāwī de la répétition et le dire d’aṭ-Ṭabarī",
]:
    if frag not in norm:
        errors.append(f"glose/nom attendu absent : {frag[:55]}")

def bare(t: str) -> str:
    return re.sub(r"[\u064B-\u065F\u0670\u06D6-\u06ED\u0640\u0671]", "", t)

cache = json.load(open("scripts-translate/quran-cache.json", encoding="utf-8"))
ar17 = dict((i, t) for i, t in cache["17"]["ar"])
ar4 = dict((i, t) for i, t in cache["4"]["ar"])
v105, v106, v107, v108 = bare(ar17[105]), bare(ar17[106]), bare(ar17[107]), bare(ar17[108])
v109, v110 = bare(ar17[109]), bare(ar17[110])
for f in ["وبلحق أنزلنه وبلحق نزل", "وما أرسلنك إلا مبشرا ونذيرا"]:
    if f not in v105:
        errors.append(f"cache 17:105 inattendu ({f[:30]})")
for f in ["وقرءانا فرقنه", "على لناس على مكث ونزلنه تنزيلا"]:
    if f not in v106:
        errors.append(f"cache 17:106 inattendu ({f[:30]})")
for f in ["قل ءامنوا به أو لا تؤمنوا", "إن لذين أوتوا لعلم من قبله إذا يتلى عليهم", "يخرون للأذقان سجدا"]:
    if f not in v107:
        errors.append(f"cache 17:107 inattendu ({f[:30]})")
for f in ["ويقولون سبحن ربنا", "إن كان وعد ربنا لمفعولا"]:
    if f not in v108:
        errors.append(f"cache 17:108 inattendu ({f[:30]})")
if "ويخرون للأذقان يبكون ويزيدهم خشوعا" not in v109:
    errors.append("cache 17:109 inattendu")
if "قل دعوا لله أو دعوا لرحمن" not in v110 or "أيا ما تدعوا فله" not in v110:
    errors.append("cache 17:110 inattendu (fragment tadʿū)")
if "ولا تجهر بصلاتك ولا تخافت بها" not in v110 or "وبتغ بين ذلك سبيلا" not in v110:
    errors.append("cache 17:110 inattendu (fragment suite)")
n41 = bare(ar4[41])
if "فكيف إذا جئنا من كل أمة بشهيد وجئنا بك على هؤلاء شهيدا" not in n41:
    errors.append("cache 4:41 inattendu (an-Nisāʾ 41)")

# préparation de la leçon suivante au DOM
if "109 » et « 110" not in norm or "901 - 011" not in norm:
    errors.append("préparation : les āyāt 109-110 (imprimé « 901 - 011 ») absentes du DOM")
if "tadʿū" not in norm or "al-ʾasmāʾ" not in norm:
    errors.append("préparation : fragments tadʿū / al-ʾasmāʾ absents")

# citations hors rasm — interdites au corps après l'évaluation
# (17:101-104 = leçon précédente 734 ; 17:110/111 = leçon suivante 736)
body = norm.split("<h2>L’évaluation", 1)[1]
for pat, label in [
    (r"neuf miracles évidents", "al-Isrāʾ 17:101 (leçon précédente — non portée)"),
    (r"Demande donc aux Enfants d’Israël", "al-Isrāʾ 17:101 (leçon précédente — non portée)"),
    (r"je te crois perdu", "al-Isrāʾ 17:101 (leçon précédente — non portée)"),
    (r"Habitez la terre", "al-Isrāʾ 17:104 (leçon précédente — non portée)"),
    (r"Nous vous ferons venir en foule", "al-Isrāʾ 17:104 (leçon précédente — non portée)"),
    (r"Invoquez Allah, ou invoquez", "al-Isrāʾ 17:110 (leçon suivante — non portée)"),
    (r"le Tout Miséricordieux", "al-Isrāʾ 17:110 (leçon suivante — non portée)"),
    (r"ne S’est point attribué d’enfant", "al-Isrāʾ 17:111 (leçon suivante — non portée)"),
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
print("PASS : leçon 735 — les quatre āyāt 105-108 rendues sur le rasm warš du cache "
      "(« Et en vérité, Nous l'avons fait descendre, et en vérité il est descendu », « "
      "annonciateur et avertisseur », « que Nous avons fragmenté », « pour que tu le "
      "récites aux gens avec lenteur », « descendant par descendant », « Croyez-y, ou "
      "n'y croyez pas », « furent dotés du savoir avant lui », « tombent le menton "
      "contre terre, prosternés », « Gloire à notre Seigneur », « s'accomplira "
      "assurément »), le lemme d'appui 109 et la citation d'an-Nisāʾ 41 du hadith "
      "d'Ibn Masʿūd rendus sur le cache, les gloses du tafsīr tranchées par le "
      "Muḥarrar (az-Zahrāwī et aṭ-Ṭabarī, Sībawayh sur « wa-qurʾānan », les lecteurs "
      "de « fa-raqnā-h » et la lecture d'Ibn Masʿūd et d'Ubayy, les durées et "
      "al-Ḥasan al-Baṣrī, les deux exégèses de « ʿalā makth », Waraqa b. Nawfal et "
      "Zayd b. ʿAmr b. Nufayl, les pronoms, les mentons, Sībawayh et al-Farrāʾ sur « "
      "in kāna », la purification de la menace, la glose de l'āya 109 et "
      "at-Tamīmī), les finalités (5), l'évaluation (4), l'exploitation (al-Bukhārī — "
      "livre du tafsīr du Coran), la préparation 109-110 au DOM (imprimé « 901 - "
      "011 » inversé, lu 109 et 110 par l'étiquette du livre), aucune citation hors "
      "rasm (17:101-104 interdits au corps après l'évaluation — leçon précédente ; "
      "17:110/111 interdits — leçon suivante), 0 arabe résiduel.")

if __name__ == "__main__":
    sys.exit(0)

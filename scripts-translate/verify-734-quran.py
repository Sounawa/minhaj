#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Minhāj — contrôle coranique de la leçon 734 (tafsir-5ep, Isrāʾ 101-104).
Vérifie : rendus français des quatre āyāt 101-104 (rasm warš du cache — « neuf
miracles évidents », « Demande donc aux Enfants d’Israël », « je pense que tu
es ensorcelé », « seul le Seigneur des cieux et de la terre les a fait
descendre comme autant de preuves illuminantes », « je te crois perdu », «
voulut donc les expulser du pays », « Nous les noyâmes tous », « Habitez la
terre », « Nous vous ferons venir en foule »), les lemmes d’appui tranchés par
le Muḥarrar et rendus sur le cache (az-Zuḫruf 45 « wa-sʾal man arsalnā min
qablika min rusulinā », az-Zuḫruf 49 « yā ayyuha s-sāḥir udʿu lanā rabbaka »,
an-Naml 14 « ǧaḥadū bi-hā wa-stayqanat-hā anfusuhum », al-Isrāʾ 45 « ḥiǧāban
mastūran »), les gloses du tafsīr (les cinq d’al-Aʿrāf — le déluge, les
sauterelles, la vermine, les grenouilles et le sang —, les quatre et leurs
dix identifications — Ibn ʿAbbās, Muḥammad b. Kaʿb al-Quraṭubī et la carte de
ʿUmar b. ʿAbd al-ʿAzīz, aḍ-Ḍaḥḥāk, ʿIkrima et Muṭar al-Warrāq et aš-Šaʿbī,
al-Ḥasan, Muṭarrif de Mālik et Ibn Wahb —, les vingt-quatre et les neuf, la
réserve, la fraction de la Torah, Ṣafwān b. ʿAssāl et les quatre yeux et le
sabbat, at-Tirmiḏī, la lecture d’al-Kisāʾī, l’ordre à Muḥammad ﷺ, az-Zuḫruf
45 et les nations passées, al-Ḥasan et Ibn ʿAbbās « fa-saʾala », le masḥūr et
ses exégèses — complément direct, aṭ-Ṭabarī au sens du sujet, Ibn ʿAṭiyya la
relative et l’allocution réprochante —, les lectures de « ʿalimtu » et «
laqad ʿalimta », an-Naml 14, aṭ-Ṭabarī et az-Zuǧǧāǧ, la baṣāʾir voie de l’âme,
le maṯbūr et ses quatre gloses — Muǧāhid, Ibn ʿAbbās et aḍ-Ḍaḥḥāk, Ibn Zayd,
le maudit —, l’effrayé du début et la parole douce et le vizir, la fraction du
non-maudit —, le yastafizuhum délogeant par le meurtre ou l’expulsion, la
terre d’Égypte, les deux bouts d’Ibn ʿAṭiyya, la terre de Syrie, la promesse
de l’au-delà jour de la Résurrection, le lafīf assemblée mélangée et le nom
verbal de aṭ-Ṭabarī), les noms portés, les finalités (2), l’évaluation (4),
l’exploitation (ar-Rāzī — le nœud de la langue, le bâton en serpent, le
serpent avalant, la manne et les cailles, la quatorzième et la quinzième,
référence au rang altéré), la préparation 105-108 au DOM — imprimé « 801 - 5
» inversé —, le lemme firʿawna fa-ġarqanā-h au rasm du cache 17:103, l’absence
de citations hors rasm (17:99-100 = leçon précédente ; 17:105-108 = leçon
suivante — interdites au corps après l’évaluation), 0 arabe résiduel. Espaces
typographiques (NNBSP/insécables) introduits par l’auto-fix de qa-lesson
normalisés avant appariement."""
import json
import re
import sys

HTML = "scripts-translate/tr-tmp/pdf-mut23h3c-734.html"
html = open(HTML, encoding="utf-8").read()
norm = html.replace("\u202f", " ").replace("\u00a0", " ")
errors = []

for frag in [
    "Nous donnâmes à Moïse neuf miracles évidents",
    "Demande donc aux Enfants d’Israël, lorsqu’il leur vint et que Pharaon lui dit",
    "je pense que tu es ensorcelé",
    "seul le Seigneur des cieux et de la terre les a fait descendre comme autant de preuves illuminantes",
    "je te crois perdu",
    "voulut donc les expulser du pays",
    "Alors Nous les noyâmes tous, lui et ceux qui étaient avec lui",
    "Habitez la terre",
    "Nous vous ferons venir en foule",
]:
    if frag not in norm:
        errors.append(f"rendu attendu absent : {frag[:55]}")

if not re.search(r"»\s*\(101-104\)", norm):
    errors.append("repère de plage (101-104) absent")

for frag in [
    "l’effet des miracles dans les cœurs des associateurs",
    "la fin du reniement des miracles par lesquels Allah — très-Haut — a soutenu Ses messagers",
    "en contemplant ces miracles et leur finalité",
    "des prodiges matériels pour le confirmer et avoir foi en lui",
    "l’effet que les cœurs en reçoivent et leur acceptation de la vérité",
    "l’histoire de Moïse — sur lui le salut",
    "qu’incrédulité et entêtement",
    "[Une première entrée du glossaire imprimé est dégradée dans la couche texte — déclarée perdue.]",
    "« des miracles manifestes » (entrée aux lemmes altérés — la définition demeure lisible)",
    "des prodiges clairs, évidents",
    "« Il les déloge » (yastafizuhum — lemme imprimé altéré, tranché par la matière)",
    "il les déloge et les fait sortir du pays d’Égypte",
    "« en foule enchevêtrée » (lafīfan — lemme imprimé altéré, tranché par la matière)",
    "mélangés, issus de hameaux et de tribus diverses",
    "[D’autres entrées du glossaire imprimé sont dégradées dans la couche texte — déclarées perdues.]",
    "[La première consigne est dégradée dans la couche texte — déclarée perdue.]",
    "a-t-Il anéanti dans ces āyāt ? Et à qui a-t-Il donné pouvoir sur Sa terre",
    "les cinq [signes] qui sont dans la sourate al-Aʿrāf",
    "le déluge, les sauterelles, la vermine, les grenouilles et le sang",
    "Ibn ʿAbbās a dit : ce sont sa main et sa langue quand le nœud fut délié, son bâton et la mer",
    "Muḥammad b. Kaʿb al-Quraṭubī",
    "la mer, le bâton, la ruine (aṭ-ṭamsa) et la pierre",
    "ʿUmar b. ʿAbd al-ʿAzīz m’interrogea là-dessus et je l’en informai",
    "« Et qu’est-ce que la ruine ? »",
    "Aaron dit “amīn”, et Allah réduisit leurs biens en poussière et les rendit pierres",
    "« Le discernement (fiqh) ne peut-il être que tel ? »",
    "une carte où étaient des merveilles",
    "ʿAbd al-ʿAzīz b. Marwān — son père —, rassemblée en Égypte",
    "une noix, un œuf et une lentille — tous pierre, restes des biens de la maison de Pharaon",
    "aḍ-Ḍaḥḥāk a dit : ce sont le double lancement du bâton, la main et le nœud de sa langue",
    "ʿIkrima, Muṭar al-Warrāq et aš-Šaʿbī ont dit : ce sont le bâton, la main, les sauterelles et la privation des fruits",
    "al-Ḥasan a dit : ce sont le bâton devenu serpent et le bâton avalant ce qu’ils fabriquent",
    "les sauterelles dans leurs steppes, la privation des fruits dans leurs villages, la main et le bâton",
    "Muṭarrif a rapporté de Mālik : ce sont le bâton, la main, la montagne quand elle se fendit, et la mer",
    "Ibn Wahb rapporta de lui, à la place de la mer, la pierre",
    "alors qu’ils sont très nombreux et montent à vingt-quatre",
    "neuf, en les mentionnant et en les décrivant comme clairs, sans les spécifier",
    "la réserve (tawaqquf) demeure en cela",
    "les āyāt de la Torah, à savoir les ordonnances et leurs corollaires",
    "Ṣafwān b. ʿAssāl a rapporté ceci",
    "car s’il t’entendait, il aurait quatre yeux",
    "de ne pas dépasser dans le sabbat",
    "at-Tirmiḏī — les chapitres du tafsīr, chapitre de la sourate Banū Isrāʾīl",
    "le commun des lecteurs a lu « fa-sʾal banī Isrāʾīla »",
    "il est rapporté d’al-Kisāʾī « fa-sul », sur la langue de celui qui dit « saʾala yasʾalu »",
    "[les lemmes imprimés de la note de lecture sont altérés, tranchés par le Muḥarrar]",
    "au sens d’un ordre à Muḥammad ﷺ",
    "« Interroge tes contemporains au sujet de l’inconnaissable de cette histoire que Nous t’avons enseigné",
    "Il entend leurs pères et Il les inclut dans le pronom car ils font d’eux",
    "de requérir leurs récits et de considérer leurs circonstances et ce qui est dans leurs livres",
    "« wa-sʾal man arsalnā min qablika min rusulinā » — az-Zuḫruf : 45",
    "[Et demande à ceux de Nos messagers que Nous avons envoyés avant toi]",
    "« Demande aux nations passées si quelqu’un d’entre elles est resté éternel »",
    "la considération tient lieu de l’interrogation",
    "ton interrogation est ta considération dans le Coran",
    "« fa-saʾala banī Isrāʾīla » : à savoir Moïse interrogea Pharaon au sujet des enfants d’Israël",
    "il les requérait pour les délivrer du châtiment",
    "« en un ensorcelé » (masḥūran) : les exégètes ont divergé en cela",
    "il est complément direct sur son régime",
    "« tu as été ensorcelé — ta parole est brouillée, et ce que tu apportes n’est pas droit",
    "aṭ-Ṭabarī a dit : il est complément direct au sens de sujet",
    "« ḥiǧāban mastūran » — al-Isrāʾ : 45",
    "[un voile invisible]",
    "« mašʾūm et maymūn » alors qu’il s’agit de « šaʾīm » et « aymān »",
    "al-Qāḍī Abū Muḥammad (Ibn ʿAṭiyya) a dit : et cela ne sort pas de la relative",
    "« doué d’une magie dont tu as pris possession et que tu as connue, si bien que tu apportes ces choses étranges pour cela »",
    "cette allocution est réprochante",
    "au sens de « sorcier »",
    "« yā ayyuha s-sāḥir udʿu lanā rabbaka » — az-Zuḫruf : 49",
    "[O magicien ! Implore pour nous ton Seigneur]",
    "soit ceux qui dirent là n’étaient pas d’entre eux Pharaon",
    "il passa de son dénigrement à sa magnification",
    "« ʿalimtu » à la tāʾ du locuteur, à la voyelle fermée",
    "« l’ennemi d’Allah n’a jamais su — seul Moïse a su »",
    "cette lecture se renforce pour qui rend « masḥūran » [al-Isrāʾ : 101] sur son régime",
    "sa vue, son intellect et sa parole corrompus",
    "mais délié pour ce qu’il apporte — et c’est la lecture d’al-Kisāʾī",
    "« laqad ʿalimta » à la tāʾ de l’allocuté ouverte",
    "qu’il mécroit par entêtement",
    "« ǧaḥadū bi-hā wa-stayqanat-hā anfusuhum » — an-Naml : 14",
    "[Ils les nièrent injustement et orgueilleusement, tandis qu’en eux-mêmes ils y croyaient avec certitude]",
    "aṭ-Ṭabarī a rapporté cela d’Ibn ʿAbbās, et az-Zuǧǧāǧ a incliné vers cela",
    "une information réprochant Pharaon",
    "tu es de toute façon de ceux qui savent cela",
    "sans que ce fût en mode d’information sur la science de Pharaon",
    "un rapport de Moïse sur la science de Pharaon",
    "la désignation par « ceux-ci » porte sur les neuf [signes]",
    "« en preuves percevantes » (baṣāʾira) : pluriel de baṣīra, qui est la voie",
    "la voie de l’âme dans sa considération et sa croyance",
    "« baṣāʾir » est à l’accusatif comme état",
    "« l’abattu » (al-maṯbūr) : le causeur de perdition, a dit Muǧāhid",
    "Ibn ʿAbbās et aḍ-Ḍaḥḥāk ont dit : c’est le vaincu",
    "Ibn Zayd a dit : c’est l’abattu (al-maḫbūl)",
    "qu’il l’expliqua par le maudit (al-malʿūn)",
    "au début de sa mission était effrayé",
    "il était commandé à la parole douce et demandait le vizir",
    "son âme se fortifia des forces de la prophétie",
    "par plus de ce à quoi il avait été ordonné, selon l’effort licite qui lui était permis",
    "Moïse s’aventura à dire au-delà de ce à quoi Allah l’avait ordonné",
    "le vaincu, l’abattu (al-muḫtadaʿ)",
    "ne saurait être un objet de malédiction (laʿān)",
    "[des bandes lemmatiques de la tête portent des fragments de « yastaʿizzuhum » et d’une lecture d’appui — la glose tranchée par le Muḥarrar, le membre du lemme altéré déclaré]",
    "« Il les déloge » (yastafizuhum) : son sens est qu’il les déloge et les détache — soit par le meurtre, soit par l’expulsion",
    "« la terre » : la terre d’Égypte",
    "ce qui s’accorde à l’histoire du proposant",
    "cette āya a résumé les histoires de Moïse avec Pharaon, et n’en mentionna que la grandeur de l’affaire et sa gravité",
    "en voici les deux bouts",
    "Pharaon voulut les vaincre et les tuer — et ce fut le début de l’affaire",
    "« Nous le noyâmes » : Allah le noya, lui et ses troupes — et ce fut la fin de l’affaire",
    "leur demeure en la terre de Syrie",
    "« āskunū »",
    "« la promesse de l’au-delà » : c’est le jour de la Résurrection",
    "« en foule enchevêtrée » (lafīfan) : l’assemblée mélangée dont les parties ont été enlacées les unes aux autres",
    "[un membre est lacéré dans la couche texte et dans l’édition d’appui elle-même — déclaré]",
    "il est des noms des collectifs qui n’ont pas de singulier de leur racine",
    "il est au sens du nom verbal",
    "« je l’enveloppai d’un enveloppement (lafan) et d’un enchevêtrement (lafīf) »",
    "et en cela est une considération : contemple-la",
    "L’appui par Allah — gloire à Lui — de Moïse — sur lui le salut — par les miracles éclatants",
    "en preuve de la véracité de sa mission",
    "qui demandèrent des miracles au messager d’Allah ﷺ",
    "comme ils n’avaient pas profité à Pharaon et à son peuple",
    "La faveur d’Allah — gloire à Lui — envers Son serviteur Moïse",
    "Il l’appuya des miracles transcendants",
    "le délivra, lui et son peuple, de leur ennemi",
    "où ils disposaient comme ils voulaient",
    "Pourquoi Pharaon et son peuple n’ont-ils pas profité des miracles de Moïse — sur lui le salut — malgré leur grandeur",
    "la fin de l’entêtement de Pharaon et de son peuple et de leur tyrannie",
    "l’effet de la divergence des lectures sur « laqad ʿalimta » au sens de l’āya",
    "en l’occasion du propos sur les associateurs",
    "[La tête du passage est lacerée dans la couche texte — déclarée ; demeurent lisibles]",
    "un grand nombre des miracles de Moïse — sur lui le salut",
    "ôta le nœud de sa langue",
    "l’empêchement articulatoire s’en alla, et il devint éloquent",
    "le retournement du bâton en serpent",
    "le serpent avalant leurs cordes et leurs bâtons",
    "la manne et les cailles sur lui et sur son peuple",
    "La quinzième : Sa parole",
    "les membres intermédiaires sont lacérés dans la couche texte, déclarés",
    "Al-Mafātīḥ (Mafātīḥ al-ġayb), de Faḫr ad-Dīn ar-Rāzī — le rang de la référence imprimée est altéré, déclaré",
    "Je collectionne du texte la mention de trois des miracles de Moïse",
    "le but de l’agencement du dénombrement des miracles du texte selon un ordre",
    "les āyāt 105 à 108 de sūrat al-Isrāʾ",
    "« 801 - 5 »",
    "« 105 » et « 108 »",
    "« firʿawna fa-ġarqanā-h », conforme au rasm du cache de l’āya 103",
    "Quelle est la faveur de répéter cela avec",
    "[la suite de la consigne est dégradée dans la couche texte, déclarée.]",
    "la préparation de la leçon précédente annonçait les āyāt 101 à 104",
    "les neuf (tisʿa), l’ensorcelé (masḥūrā) et l’abattu (matbūrā)",
    "matière de la leçon suivante (leçon 27)",
    "tranchent mot pour mot les gloses lacérées",
]:
    if frag not in norm:
        errors.append(f"glose/nom attendu absent : {frag[:55]}")

def bare(t: str) -> str:
    return re.sub(r"[\u064B-\u065F\u0670\u06D6-\u06ED\u0640\u0671]", "", t)

cache = json.load(open("scripts-translate/quran-cache.json", encoding="utf-8"))
ar17 = dict((i, t) for i, t in cache["17"]["ar"])
ar43 = dict((i, t) for i, t in cache["43"]["ar"])
ar27 = dict((i, t) for i, t in cache["27"]["ar"])
v101, v102, v103, v104 = bare(ar17[101]), bare(ar17[102]), bare(ar17[103]), bare(ar17[104])
for f in ["تسع ءايت بينت", "فسل بنى إسرءيل إذ جاءهم", "فقال له فرعون إنى لأظنك يموسى مسحورا"]:
    if f not in v101:
        errors.append(f"cache 17:101 inattendu ({f[:30]})")
for f in ["قال لقد علمت ما أنزل هؤلاء إلا رب لسموت ولأرض بصائر", "وإنى لأظنك يفرعون مثبورا"]:
    if f not in v102:
        errors.append(f"cache 17:102 inattendu ({f[:30]})")
for f in ["فأراد أن يستفزهم من لأرض", "فأغرقنه ومن معه جميعا"]:
    if f not in v103:
        errors.append(f"cache 17:103 inattendu ({f[:30]})")
for f in ["وقلنا من بعده لبنى إسرءيل سكنوا لأرض", "فإذا جاء وعد لءاخرة جئنا بكم لفيفا"]:
    if f not in v104:
        errors.append(f"cache 17:104 inattendu ({f[:30]})")
if "وسل من أرسلنا من قبلك من رسلنا" not in bare(ar43[45]):
    errors.append("cache 43:45 inattendu")
if "يأيه لساحر دع لنا ربك" not in bare(ar43[49]):
    errors.append("cache 43:49 inattendu")
if "وجحدوا بها وستيقنتها أنفسهم" not in bare(ar27[14]):
    errors.append("cache 27:14 inattendu")
if "حجابا مستورا" not in bare(ar17[45]):
    errors.append("cache 17:45 inattendu")

# préparation de la leçon suivante au DOM
if "105 » et « 108" not in norm or "801 - 5" not in norm:
    errors.append("préparation : les āyāt 105-108 (imprimé « 801 - 5 ») absentes du DOM")
if "firʿawna fa-ġarqanā-h" not in norm:
    errors.append("préparation : lemme firʿawna fa-ġarqanā-h absent")

# citations hors rasm — interdites au corps après l'évaluation
# (17:99-100 = leçon précédente 733 ; 17:105-108 = leçon suivante 735)
body = norm.split("<h2>L’évaluation", 1)[1]
for pat, label in [
    (r"capable de créer leurs pareils", "al-Isrāʾ 17:99 (leçon précédente — non portée)"),
    (r"les trésors de la miséricorde de mon Seigneur", "al-Isrāʾ 17:100 (leçon précédente — non portée)"),
    (r"vous lésineriez", "al-Isrāʾ 17:100 (leçon précédente — non portée)"),
    (r"en toute vérité que Nous l’avons fait descendre", "al-Isrāʾ 17:105 (leçon suivante — non portée)"),
    (r"que Nous avons fragmenté", "al-Isrāʾ 17:106 (leçon suivante — non portée)"),
    (r"le menton contre terre", "al-Isrāʾ 17:107 (leçon suivante — non portée)"),
    (r"Gloire à notre Seigneur", "al-Isrāʾ 17:108 (leçon suivante — non portée)"),
    (r"annonciateur et avertisseur", "al-Isrāʾ 17:105 (leçon suivante — non portée)"),
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
print("PASS : leçon 734 — les quatre āyāt 101-104 rendues sur le rasm warš du cache "
      "(« neuf miracles évidents », « Demande donc aux Enfants d’Israël », « je pense "
      "que tu es ensorcelé », « seul le Seigneur des cieux et de la terre les a fait "
      "descendre comme autant de preuves illuminantes », « je te crois perdu », « "
      "voulut donc les expulser du pays », « Nous les noyâmes tous », « Habitez la "
      "terre », « Nous vous ferons venir en foule »), les lemmes d’appui tranchés par "
      "le Muḥarrar et rendus sur le cache (az-Zuḫruf 45, az-Zuḫruf 49, an-Naml 14, "
      "al-Isrāʾ 45 « ḥiǧāban mastūran »), les gloses du tafsīr (les cinq d’al-Aʿrāf et "
      "les dix identifications des quatre — Ibn ʿAbbās, al-Quraṭubī avec la carte de "
      "ʿUmar b. ʿAbd al-ʿAzīz, aḍ-Ḍaḥḥāk, ʿIkrima et Muṭar al-Warrāq et aš-Šaʿbī, "
      "al-Ḥasan, Muṭarrif de Mālik et Ibn Wahb —, les vingt-quatre et les neuf, la "
      "réserve, la fraction de la Torah, Ṣafwān b. ʿAssāl et les quatre yeux et le "
      "sabbat, at-Tirmiḏī, l’ordre à Muḥammad ﷺ, les nations passées, al-Ḥasan et Ibn "
      "ʿAbbās « fa-saʾala », le masḥūr et ses trois exégèses, les lectures de « ʿalimtu "
      "» et « laqad ʿalimta », aṭ-Ṭabarī et az-Zuǧǧāǧ, la baṣāʾir voie de l’âme, le "
      "maṯbūr et ses quatre gloses, l’effrayé du début et la parole douce et le vizir, "
      "la fraction du non-maudit —, le yastafizuhum délogeant par le meurtre ou "
      "l’expulsion, la terre d’Égypte, les deux bouts d’Ibn ʿAṭiyya, la terre de Syrie, "
      "la promesse de l’au-delà jour de la Résurrection, le lafīf et le nom verbal de "
      "aṭ-Ṭabarī), les noms portés (Ibn ʿAbbās, Muḥammad b. Kaʿb al-Quraṭubī, ʿUmar b. "
      "ʿAbd al-ʿAzīz, ʿAbd al-ʿAzīz b. Marwān, aḍ-Ḍaḥḥāk, ʿIkrima, Muṭar al-Warrāq, "
      "aš-Šaʿbī, al-Ḥasan, Muṭarrif, Mālik, Ibn Wahb, Ṣafwān b. ʿAssāl, at-Tirmiḏī, "
      "al-Kisāʾī, aṭ-Ṭabarī, az-Zuǧǧāǧ, Ibn ʿAṭiyya, Muǧāhid, Ibn Zayd, ʿAlī, ar-Rāzī), "
      "les finalités (2), l’évaluation (4), l’exploitation (ar-Rāzī — le nœud de la "
      "langue, le bâton en serpent, le serpent avalant, la manne et les cailles — "
      "référence au rang altéré, bandes dégradées déclarées), la préparation 105-108 au "
      "DOM (imprimé « 801 - 5 » inversé, lu 105 et 108 par l’étiquette du livre — "
      "firʿawna fa-ġarqanā-h au rasm du cache 17:103), aucune citation hors rasm "
      "(17:99-100 interdits au corps après l’évaluation — leçon précédente ; 17:105-108 "
      "interdits — leçon suivante), 0 arabe résiduel.")

if __name__ == "__main__":
    sys.exit(0)

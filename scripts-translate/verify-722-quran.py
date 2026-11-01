#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Minhāj — contrôle coranique de la leçon 722 (tafsir-5ep, Isrāʾ 49-55).
Vérifie : rendus français des versets 49-55 (rasm warš du cache — 17:52 portant
« par Sa louange »), les parallèles cités au corps et à l'exploitation (al-Muʾminūn
112-113, ar-Rūm 27, an-Naḥl 125, al-ʿAnkabūt 46, al-Aʿrāf 17, Āl ʿImrān 159,
Ṭā-Hā 44, al-Anʿām 108), les gloses lexicales et les noms portés, l'absence de
citations hors rasm (17:45-48 = leçon précédente, interdites au corps), 0 arabe
résiduel."""
import json
import re
import sys

HTML = "scripts-translate/tr-tmp/pdf-mut23h3c-722.html"
html = open(HTML, encoding="utf-8").read()
errors = []

for frag in [
    "serons-nous ramenés en une création nouvelle",
    "Soyez pierres ou fer",
    "ou une création de ce qui grandit en vos poitrines",
    "Qui donc nous réintégrera",
    "Celui qui vous façonna la première fois",
    "ils branleront vers toi leurs têtes",
    "Quand est-il",
    "Il se peut qu’il soit proche",
    "le jour où Il vous appellera et vous répondrez par Sa louange",
    "vous penserez n’être demeurés qu’un peu",
    "Et dis à Mes serviteurs de dire ce qui est meilleur",
    "le diable sème la discorde entre eux",
    "le diable est, pour l’homme, un ennemi manifeste",
    "Votre Seigneur vous connaît mieux",
    "s’Il veut, Il vous fera miséricorde",
    "ou, s’Il veut, Il vous châtiera",
    "Nous ne t’avons pas établi sur eux garant",
    "ton Seigneur connaît mieux quiconque est dans les cieux et la terre",
    "Nous avons préféré certains des prophètes sur d’autres",
    "donné à David les Psaumes",
]:
    if frag not in html:
        errors.append(f"rendu attendu absent : {frag[:55]}")

if not re.search(r"»\s*\(49-55\)", html):
    errors.append("repère de plage (49-55) absent")

for frag in [
    "C’est par une miséricorde d’Allah que tu fus doux avec eux",
    "ils se seraient dispersés d’autour de toi",
    "Parlez-lui en parole douce",
    "N’insultez point ceux qu’ils invoquent en dehors d’Allah",
    "de peur qu’ils n’insultent Allah, par agression et sans science",
    "Appelle à la voie de ton Seigneur par la sagesse et la belle exhortation",
    "discute avec eux par la manière la meilleure",
    "Ne discutez avec les gens du Livre que par la manière la meilleure",
    "nous demeurâmes un jour ou partie d’un jour",
    "demande aux compteurs",
    "et c’est Lui qui commence la création puis la réitère, et cela Lui est plus facile",
    "puis je viendrai à eux de devant eux et de derrière eux",
    "de leurs mains droites et de leurs mains gauches",
    "Supposez vos personnes être quelque chose de celles-ci",
]:
    if frag not in html:
        errors.append(f"parallèle attendu absent : {frag[:55]}")

def bare(t: str) -> str:
    return re.sub(r"[\u064B-\u065F\u0670\u06D6-\u06ED\u0640\u0671]", "", t)

cache = json.load(open("scripts-translate/quran-cache.json", encoding="utf-8"))
ar17 = dict((i, t) for i, t in cache["17"]["ar"])
v49, v50, v51, v52, v53, v54, v55 = (ar17[i] for i in range(49, 56))
b49, b50, b51, b52, b53, b54, b55 = (bare(v) for v in (v49, v50, v51, v52, v53, v54, v55))
if "وقالوا أءذا كنا عظما ورفتا" not in b49 or "أءنا لمبعوثون خلقا جديدا" not in b49:
    errors.append("cache 17:49 inattendu (les ossements et la poussière, la création nouvelle)")
if "قل كونوا حجارة أو حديدا" not in b50:
    errors.append("cache 17:50 inattendu (les pierres et le fer)")
for f in ["أو خلقا مما يكبر فى صدوركم", "فسيقولون من يعيدنا", "قل لذى فطركم أول مرة",
          "فسينغضون إليك رءوسهم", "ويقولون متى هو", "قل عسى أن يكون قريبا"]:
    if f not in b51:
        errors.append(f"cache 17:51 inattendu ({f[:35]})")
if "يوم يدعوكم فتستجيبون بحمده" not in b52 or "وتظنون إن لبثتم إلا قليلا" not in b52:
    errors.append("cache 17:52 inattendu (l’appel, la réponse par Sa louange, le peu demeuré)")
for f in ["وقل لعبادى يقولوا لتى هى أحسن", "إن لشيطن ينزغ بينهم",
          "إن لشيطن كان للإنسن عدوا مبينا"]:
    if f not in b53:
        errors.append(f"cache 17:53 inattendu ({f[:35]})")
for f in ["ربكم أعلم بكم", "إن يشأ يرحمكم أو إن يشأ يعذبكم", "وما أرسلنك عليهم وكيلا"]:
    if f not in b54:
        errors.append(f"cache 17:54 inattendu ({f[:35]})")
for f in ["وربك أعلم بمن فى لسموت ولأرض", "ولقد فضلنا بعض لنبين على بعض",
          "ءاتينا داود زبورا"]:
    if f not in b55:
        errors.append(f"cache 17:55 inattendu ({f[:35]})")

ar23 = dict((i, t) for i, t in cache["23"]["ar"])
ar30 = dict((i, t) for i, t in cache["30"]["ar"])
ar16 = dict((i, t) for i, t in cache["16"]["ar"])
ar29 = dict((i, t) for i, t in cache["29"]["ar"])
ar7 = dict((i, t) for i, t in cache["7"]["ar"])
ar3 = dict((i, t) for i, t in cache["3"]["ar"])
ar20 = dict((i, t) for i, t in cache["20"]["ar"])
ar6 = dict((i, t) for i, t in cache["6"]["ar"])
if "لبثنا يوما أو بعض يوم فسل لعادين" not in bare(ar23[113]):
    errors.append("cache 23:113 inattendu (le jour ou partie d’un jour)")
if "ثم يعيده وهو أهون عليه" not in bare(ar30[27]):
    errors.append("cache 30:27 inattendu (la réitération plus facile)")
if "دع إلى سبيل ربك بلحكمة ولموعظة لحسنة" not in bare(ar16[125]) \
        or "وجدلهم بلتى هى أحسن" not in bare(ar16[125]):
    errors.append("cache 16:125 inattendu (la sagesse et la belle exhortation)")
if "لا تجدلوا أهل لكتب إلا بلتى هى أحسن" not in bare(ar29[46]):
    errors.append("cache 29:46 inattendu (les gens du Livre)")
if "من بين أيديهم ومن خلفهم وعن أيمنهم وعن شمائلهم" not in bare(ar7[17]):
    errors.append("cache 7:17 inattendu (de devant eux et de derrière eux)")
if "لنت لهم" not in bare(ar3[159]) or "غليظ لقلب لنفضوا من حولك" not in bare(ar3[159]):
    errors.append("cache 3:159 inattendu (la douceur, le cœur dur)")
if "قولا لينا" not in bare(ar20[44]):
    errors.append("cache 20:44 inattendu (la parole douce)")
if "فيسبوا لله عدوا بغير علم" not in bare(ar6[108]):
    errors.append("cache 6:108 inattendu (l’insulte par agression)")

for frag in ["rafāt", "faṭarakum", "ʿasā", "nazaġ", "zabūran", "zubūran", "qadūd",
             "rakūb", "ḥalūb", "ẓarīf", "ẓurūf", "zibr", "qišr", "qušūr",
             "dalīl al-khiṭāb", "al-wasīla", "al-kitāb", "Ibn ʿAbbās", "Mujāhid",
             "aṭ-Ṭabarī", "Abū Ḥayyān", "al-Baḥr al-muḥīṭ", "Ibn Kathīr", "Sībawayh",
             "al-Akhfash", "al-Ḥasan", "Abū Hurayra", "Ṣaḥīḥ al-Bukhārī",
             "Ṣaḥīḥ Muslim", "Abū ʿAlī al-Fārisī", "Ibn ʿAṭiyya", "Qatāda",
             "Ibn Jurayj", "Ḥamza", "Yaḥyā", "al-Aʿmash", "al-Muʾminūn",
             "al-Muḥarrar al-wajīz", "rasm warš", "istiṯmār", "taqwīm",
             "al-iʿdād al-qiblī", "ﷺ"]:
    if frag not in html:
        errors.append(f"glose/nom attendu absent : {frag}")

# 17:52 rendu sur la leçon warš du cache (« par Sa louange » — bi-ḥamdihi)
if "بحمده" not in b52:
    errors.append("17:52 : le cache ne porte pas la leçon warš bi-ḥamdihi")

# citations hors rasm — interdites au corps (versets 45-48 : leçon précédente)
body = html.split("<h2>L’évaluation", 1)[0]
for pat, label in [
    (r"voile enveloppant", "al-Isrāʾ 17:45 (leçon précédente — non portée)"),
    (r"couvertures", "al-Isrāʾ 17:46 (leçon précédente — non portée)"),
    (r"surdité", "al-Isrāʾ 17:46 (leçon précédente — non portée)"),
    (r"homme ensorcelé", "al-Isrāʾ 17:47 (leçon précédente — non portée)"),
    (r"conciliabul", "al-Isrāʾ 17:47 (leçon précédente — non portée)"),
]:
    if re.search(pat, body, re.IGNORECASE):
        errors.append(f"citation inattendue : {label}")

if re.search(r"[\u0600-\u06FF\u0750-\u077F\u08A0-\u08FF\uFB50-\uFDF9\uFDFB-\uFDFF\uFE70-\uFEFF]", html):
    errors.append("caractère arabe résiduel détecté")

if errors:
    print("ÉCHEC :")
    for e in errors:
        print(" -", e)
    sys.exit(1)
print("PASS : leçon 722 — versets 49-55 rendus sur le rasm warš du cache (les ossements "
      "et la poussière, les pierres et le fer, la création grandissant en poitrine, la "
      "réintégration par le Façonneur premier, le branlement des têtes et l’Heure "
      "proche, l’appel et la réponse par Sa louange — 17:52 à la leçon warš bi-ḥamdihi "
      "—, le peu demeuré aux deux sens du « penser »), les parallèles au corps et à "
      "l’exploitation (al-Muʾminūn 112-113 les compteurs, ar-Rūm 27 la réitération "
      "plus facile, an-Naḥl 125 et al-ʿAnkabūt 46 la manière la meilleure, al-Aʿrāf 17 "
      "les quatre directions du diable, Āl ʿImrān 159 la douceur, Ṭā-Hā 44 la parole "
      "douce à Pharaon, al-Anʿām 108 l’interdit de l’insulte), les gloses du rafāt, le "
      "débat des grammairiens (Sībawayh contre al-Akhfash sur la réponse de "
      "l’impératif), les deux factions de la leçon (entre croyants ou envers les "
      "associateurs de La Mecque), l’inimitié ancienne du diable, l’espérance et la "
      "crainte des associateurs, la miséricorde par le repentir (Ibn Jurayj), la "
      "préposition régie par le verbe (Abū ʿAlī al-Fārisī contre Ibn ʿAṭiyya, "
      "l’indice de l’adresse non égardé), la préférence des prophètes répartie "
      "(l’entretien, les Cinq, la revivification), les lectures de zabūran/zubūran "
      "(faʿūl-mafʿūl rare : qadūd, rakūb, ḥalūb ; ẓarīf/ẓurūf ; qišr/qušūr ; le zibr "
      "de l’intellect et le faible dénué de zibr), les finalités, la préparation "
      "56-60 au DOM, aucune citation hors rasm (17:45-48 interdits au corps), 0 arabe "
      "résiduel.")

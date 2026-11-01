#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Minhāj — contrôle coranique de la leçon 733 (tafsir-5ep, Isrāʾ 99-100).
Vérifie : rendus français des deux āyāt 99-100 (rasm warš du cache — « N’ont-ils
pas vu qu’Allah qui a créé les cieux et la terre est capable de créer leurs
pareils », le terme fixé sans doute, les injustes s’obstinant dans leur
mécréance, les trésors de la miséricorde de mon Seigneur, « vous lésineriez »
de peur de la dépense, l’homme très avare), le lemme d’appui d’al-Aḥqāf 33
tranché par le rasm du cache (« allaḏī ḫalaqa s-samāwāti wal-arḍa walam yaʿyā »,
« ʿalā kulli šayʾin qadīr »), les gloses lexicales (aǧal — le temps fixé, la fin
que l’on atteint ; qatūr — exagérant dans l’avarice), les gloses du tafsīr
(la hamza de « a-lam » pour l’interrogation, la vision du cœur entrant par le
reproche, la capacité à créer une seconde fois par le terme du pareil, les
autres serviteurs glorifiants, l’argument de la reconnaissance de la création,
le domaine du possible, le Véridique aux miracles établis, le terme visant la
Résurrection ou le terme de la mort, le nom de genre posé au lieu des termes,
la validité de la résurrection quand Il veut, le régime du « law » tantôt
apparent tantôt implicite, le taqdīr de la possession des trésors, Ḥātim
aṭ-Ṭāʾī, la miséricorde étant le bien dépensé en nourritures, la dépense bien
connue conduisant à la pauvreté et la crainte de sa conséquence, « être
démuni », la main pleine sans qu’aucune dépense ne la diminue depuis l’origine
du jour et de la nuit, le hadith d’Abū Hurayra au Ṣaḥīḥ al-Bukhārī — Livre du
tawḥīd), les noms portés (Ḥātim aṭ-Ṭāʾī, Abū Hurayra, al-Bukhārī, Ibn ʿĀšūr,
Ibn ʿAṭiyya), les finalités (3), les fragments de rasm du cache (17:99,
17:100, 46:33), la préparation 101-104 au DOM — imprimé « 401 - 101 » inversé
—, les lemmes tisʿa, masḥūrā, matbūrā au rasm du cache, l’absence de citations
hors rasm (17:94-98 = leçon précédente ; 17:101-104 = leçon suivante —
interdites au corps après l’évaluation), 0 arabe résiduel. Espaces
typographiques (NNBSP/insécables) introduits par l’auto-fix de qa-lesson
normalisés avant appariement."""
import json
import re
import sys

HTML = "scripts-translate/tr-tmp/pdf-mut23h3c-733.html"
html = open(HTML, encoding="utf-8").read()
norm = html.replace("\u202f", " ").replace("\u00a0", " ")
errors = []

for frag in [
    "N’ont-ils pas vu qu’Allah qui a créé les cieux et la terre est capable de créer leurs pareils",
    "Il leur a fixé un terme, sur lequel il n’y a aucun doute",
    "les injustes s’obstinent dans leur mécréance",
    "Si c’était vous qui possédiez les trésors de la miséricorde de mon Seigneur",
    "vous lésineriez, certes, de peur de les dépenser",
    "Et l’homme est très avare",
]:
    if frag not in norm:
        errors.append(f"rendu attendu absent : {frag[:55]}")

if not re.search(r"»\s*\(99-100\)", norm):
    errors.append("repère de plage (99-100) absent")

for frag in [
    "les arguments par lesquels Allah — gloire à Lui — a fait face aux déniateurs",
    "comme avare et chiche",
    "la dépense de mon bien de ce qui agrée Allah — très-Haut",
    "aux déniateurs de la prophétie",
    "la nullité de leur croyance en la Résurrection",
    "le raisonnement de l’exemple",
    "poussière et ossements dispersés",
    "cette équivoque vaine",
    "plus grande que la création de l’homme",
    "capable de les recréer eux-mêmes",
    "[Une première entrée du glossaire imprimé est dégradée dans la couche texte — déclarée perdue.]",
    "« le terme » (aǧal — lemme imprimé altéré, restitué d’après la matière)",
    "le temps fixé, la fin que l’on atteint, en quelque état des circonstances",
    "l’usage ayant répandu son emploi absolu sur la vie",
    "« très avare » (qatūr — lemme imprimé sans point, tranché par le rasm du cache)",
    "exagérant dans l’avarice",
    "Contre qui Allah — gloire à Lui — a-t-Il répondu dans ces āyāt",
    "Par quoi Allah — très-Haut — a-t-Il décrit l’homme dans les āyāt",
    "La hamza de « a-lam » est pour l’interrogation",
    "elle entre par le sens du reproche",
    "vision du cœur",
    "la capacité à les créer une seconde fois",
    "le terme du pareil",
    "d’autres serviteurs qui Le glorifient et L’adorent",
    "la référence porte un rang hors borne",
    "référence et citation déclarées perdues",
    "ils reconnaissent la création d’Allah — très-Haut — et Son invention",
    "reconnaître Sa création pour le tout",
    "Sa sortie du néant où il était retenu",
    "de nier Sa restitution pour certains",
    "L’affaire aboutit donc au domaine du possible",
    "dont les miracles ont établi les preuves",
    "al-Aḥqāf : 33 — lemme imprimé partiellement altéré",
    "« allaḏī ḫalaqa s-samāwāti wal-arḍa walam yaʿyā »",
    "« ʿalā kulli šayʾin qadīr »",
    "et qui n’a pas été fatigué par leur création",
    "est capable en vérité de redonner la vie aux morts",
    "Il est certes Omnipotent",
    "possible d’existence",
    "son accomplissement a un temps connu",
    "il peut viser la Résurrection",
    "le terme de la mort",
    "un nom de genre",
    "posé au lieu des termes",
    "la validité de la possibilité de leur résurrection quand Il veut",
    "il n’est de dieu que Lui",
    "leur avarice alors même qu’ils posséderaient les trésors des cieux et de la terre",
    "tantôt apparent, tantôt implicite",
    "le taqdīr ici : « Dis : si vous possédez — vous possédez les trésors — »",
    "le pronom levé sur la suite",
    "Ḥātim aṭ-Ṭāʾī",
    "« law ḏāt sawār laṭamannī »",
    "le bien et les faveurs qui se dépensent dans les nourritures",
    "d’après cela qu’a été nommé le mot « miséricorde »",
    "la part bien connue",
    "la disparition du bien, laquelle conduit à la pauvreté",
    "la crainte de la conséquence de la dépense",
    "« il a dépensé » l’homme a le sens d’« être démuni »",
    "« devenu poussiéreux et démuni »",
    "« wa-kāna l-insāna qatūrā » — lemme imprimé altéré, tranché par le rasm du cache",
    ": retenu",
    "Deux lemmes coraniques d’appui imprimés auxquels s’attache la glose portent des références et des citations altérées — déclarées perdues.",
    "Il crée de la création ce qu’Il veut, et invente des nourritures de la miséricorde",
    "l’épuisement des trésors de Sa miséricorde",
    "le hadith d’Abū Hurayra — qu’Allah l’agrée",
    "La main d’Allah est pleine : nulle dépense ne la fait décroître",
    "depuis l’origine du jour et de la nuit",
    "Rien de ce qui est en Sa main ne s’est diminué",
    "Ṣaḥīḥ al-Bukhārī, Livre du tawḥīd — le lemme imprimé du chapitre est partiellement altéré, déclaré",
    "de recréer l’homme et de le vivifier après sa mort",
    "« yuḥyīkum » et de « al-ḫalq »",
    "le répit jusqu’à un terme connu",
    "dans l’espoir de leur droiture et de leur repentir",
    "Sa capacité qui ne connaît pas de limite",
    "Il crée de la miséricorde et des nourritures ce qu’Il veut",
    "en exposant les illusions des associateurs à ce sujet",
    "l’aspect de l’exagération dans la description de l’homme comme avare",
    "la purification de l’âme et le profit d’autrui",
    "l’éventualité du temps qui a été fixé à l’accomplissement de la Résurrection dans la science d’Allah — très-Haut",
    "ne voient-ils pas qu’Il leur a fixé un terme pour leurs vies",
    "ce que le Sage fait exister, il y veille en son être",
    "un anéantissement éphémère pour accueillir une existence plus grande",
    "Al-Taḥrīr wa-t-tanwīr, du Ṭāhir Ibn ʿĀšūr : 22/51",
    "J’extrais du texte le sens du terme (al-aǧal)",
    "Comment l’argumentation de l’accomplissement de la Résurrection est-elle possible à partir du texte",
    "« tisʿa », de « masḥūrā » et de « matbūrā »",
    "Les associateurs sont-ils affectés par les miracles par lesquels Allah soutient Ses messagers",
    "[la suite de la consigne est dégradée dans la couche texte, déclarée.]",
    "la préparation de la leçon précédente annonçait les deux āyāt 99 et 100",
    "le terme fixé sans doute, les trésors de la miséricorde et l’avare de l’homme",
    "matière de la leçon suivante (leçon 26)",
]:
    if frag not in norm:
        errors.append(f"glose/nom attendu absent : {frag[:55]}")

def bare(t: str) -> str:
    return re.sub(r"[\u064B-\u065F\u0670\u06D6-\u06ED\u0640\u0671]", "", t)

cache = json.load(open("scripts-translate/quran-cache.json", encoding="utf-8"))
ar17 = dict((i, t) for i, t in cache["17"]["ar"])
ar46 = dict((i, t) for i, t in cache["46"]["ar"])
v99, v100 = bare(ar17[99]), bare(ar17[100])
for f in ["أولم يروا أن لله لذى خلق لسموت ولأرض", "أن يخلق مثلهم",
          "أجلا لا ريب فيه", "فأبى لظلمون إلا كفورا"]:
    if f not in v99:
        errors.append(f"cache 17:99 inattendu ({f[:30]})")
for f in ["تملكون خزائن رحمة ربى", "لأمسكتم خشية لإنفاق", "وكان لإنسن قتورا"]:
    if f not in v100:
        errors.append(f"cache 17:100 inattendu ({f[:30]})")
v4633 = bare(ar46[33])
for f in ["ولم يعى بخلقهن بقدر على أن يحى لموتى", "على كل شىء قدير"]:
    if f not in v4633:
        errors.append(f"cache 46:33 inattendu ({f[:30]})")

# préparation de la leçon suivante au DOM
if "101 » et « 104" not in norm or "401 - 101" not in norm:
    errors.append("préparation : les āyāt 101-104 (imprimé « 401 - 101 ») absentes du DOM")
for f in ["tisʿa", "masḥūrā", "matbūrā"]:
    if f not in norm:
        errors.append(f"préparation : lemme attendu absent : {f}")

# citations hors rasm — interdites au corps après l'évaluation
# (17:94-98 = leçon précédente 732 ; 17:101-104 = leçon suivante 734)
body = norm.split("<h2>L’évaluation", 1)[1]
for pat, label in [
    (r"rien n’empêcha les gens de croire", "al-Isrāʾ 17:94 (leçon précédente — non portée)"),
    (r"Allah envoie-t-Il un être humain messager", "al-Isrāʾ 17:94 (leçon précédente — non portée)"),
    (r"anges marchant tranquillement", "al-Isrāʾ 17:95 (leçon précédente — non portée)"),
    (r"Allah suffit comme témoin", "al-Isrāʾ 17:96 (leçon précédente — non portée)"),
    (r"traînés sur leurs visages", "al-Isrāʾ 17:97 (leçon précédente — non portée)"),
    (r"chaque fois que son feu s’affaiblit", "al-Isrāʾ 17:97 (leçon précédente — non portée)"),
    (r"une nouvelle création", "al-Isrāʾ 17:98 (leçon précédente — non portée)"),
    (r"neuf miracles évidents", "al-Isrāʾ 17:101 (leçon suivante — non portée)"),
    (r"seul le Seigneur des cieux et de la terre les a fait descendre", "al-Isrāʾ 17:102 (leçon suivante — non portée)"),
    (r"Nous les noyâmes", "al-Isrāʾ 17:103 (leçon suivante — non portée)"),
    (r"Habitez la terre", "al-Isrāʾ 17:104 (leçon suivante — non portée)"),
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
print("PASS : leçon 733 — les deux āyāt 99-100 rendues sur le rasm warš du cache "
      "(« N’ont-ils pas vu qu’Allah qui a créé les cieux et la terre est capable de "
      "créer leurs pareils », le terme fixé sans doute, les injustes s’obstinant dans "
      "leur mécréance, les trésors de la miséricorde de mon Seigneur, « vous "
      "lésineriez » de peur de la dépense, l’homme très avare), le lemme d’appui "
      "d’al-Aḥqāf 33 tranché par le rasm du cache (« allaḏī ḫalaqa s-samāwāti "
      "wal-arḍa walam yaʿyā », « ʿalā kulli šayʾin qadīr »), les gloses lexicales "
      "(aǧal — le temps fixé ; qatūr — exagérant dans l’avarice), les gloses du "
      "tafsīr (la hamza de « a-lam » pour l’interrogation, la vision du cœur entrant "
      "par le reproche, la capacité par le terme du pareil et les autres serviteurs "
      "glorifiants, le domaine du possible et le Véridique aux miracles établis, le "
      "terme visant la Résurrection ou le terme de la mort, le nom de genre posé au "
      "lieu des termes, le régime du « law » tantôt apparent tantôt implicite, le "
      "taqdīr de la possession des trésors, Ḥātim aṭ-Ṭāʾī, la miséricorde bien "
      "dépensée et la crainte de la conséquence de la dépense, la main pleine sans "
      "qu’aucune dépense ne la diminue — le hadith d’Abū Hurayra au Ṣaḥīḥ "
      "al-Bukhārī — Livre du tawḥīd), les noms portés (Ḥātim aṭ-Ṭāʾī, Abū Hurayra, "
      "al-Bukhārī, Ibn ʿĀšūr, Ibn ʿAṭiyya), les finalités (3), l’évaluation (3), "
      "l’exploitation (al-Taḥrīr wa-t-tanwīr d’Ibn ʿĀšūr 22/51 — le terme visant le "
      "temps fixé à l’accomplissement de la Résurrection dans la science d’Allah, "
      "le second argument par le terme des vies, la sagesse exigeant que le Sage "
      "veille en l’être de ce qu’il fait exister, l’anéantissement éphémère "
      "accueillant une existence plus grande — tranché par la source d’appui, "
      "bandes dégradées déclarées), la préparation 101-104 au DOM (imprimé "
      "« 401 - 101 » inversé, lu 101 et 104 par l’étiquette du livre — tisʿa, "
      "masḥūrā, matbūrā au rasm du cache 17:101-102), aucune citation hors rasm "
      "(17:94-98 interdits au corps après l’évaluation — leçon précédente ; "
      "17:101-104 interdits — leçon suivante), 0 arabe résiduel.")

if __name__ == "__main__":
    sys.exit(0)

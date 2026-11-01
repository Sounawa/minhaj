#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Minhāj — contrôle coranique et de contenu de la leçon 742 (tafsir-5ep,
sūrat al-Kahf v15-16 — quatrième leçon du second livre, pages 29-36 du manuel
miroir tafsir-3-thanawi). Les āyāt 15-16 sont rendues en français sur le rasm
warš du cache (présence vérifiée) ; le périmètre est tranché par le contenu :
l'en-tête imprimé porte (15-16) contre (13-16) à la grille du portail, le
commentaire du manuel rouvrant l'āya 14 par le rattachement — dont le rendu
relève de la leçon 741 (les rendus des āyāt 13-14, déjà livrés, absents
d'ici) ; le rasm nu du cache interdit au corps (0 arabe — FR-seule) pour
TOUTES les āyāt voisines (6-9 leçon 740, 10-14 leçon 741, 17-18 leçon 743) ;
contrôle de contenu : la sérénité pour le prophète et la confirmation de la
rectitude des détails, la levée de la divergence (sortie, séparation, durée
du séjour, nombre, issue), la facilitation de l'œuvre salutaire et l'ascèse
(accroissements sur la foi), la réponse faite à Quraysh (les Banū Isrāʾīl les
ayant chargés), Ibn Kaṯīr (l'exposé en détail, les adolescents contre les
vieillards obstinés, les répondants jeunes, les anciens de Quraysh demeurés),
l'insufflation de la guidée et la taqwā, aṭ-Ṭabarī (l'accroissement de foi et
la claire-voyance, la patience sur l'exil, la dureté de la caverne),
l'accroissement et la différenciation de la foi (al-Buḫārī), le lien sur les
cœurs (les épreuves, les états vacillants, rābiṭ, la mère de Mūsā, al-Qaṣaṣ),
les deux sens de la station (le roi mécréant, l'arrachement résolu), l'appel
(divinités sans nulle indépendance, l'immersion de la durée), l'excès
(transgression, dépassement, le prix au-dessus de la valeur), le tanwīn de
remplacement pour la phrase conditionnelle sur l'adverbe, la double
convenance de « Voici notre peuple » (la station devant le roi, les uns aux
autres), l'incitation à l'incapacitation, le forgé du mensonge (le plus
odieux, la déchirure, l'interrogation de négation, l'appendice du relatif),
la tāʾ de l'iftiʿāl (la quête de l'isolement, le pronom des sujets), aṭ-Ṭabarī
(le nom relatif accouplé, l'accouplement de la hāʾ et de la mīm), le nom non
la particule de négation, l'exemption disjointe et rattachée, Qatāda, la
variante des muṣḥaf (en dehors de nous), le sens implicite (la confiance sur
la miséricorde, l'invocation selon la mesure de ce bas monde, la certitude
touchant l'affaire ultime), le jussif sur le répondant de l'ordre, le nom
verbal mīmī du schéma mafʿal, les lectures de l'agrément (Nāfiʿ, Ibn ʿĀmir,
Abū Jaʿfar — mīm ouverte ; Ibn Kaṯīr, Abū ʿAmr, ʿĀṣim, Ḥamza, al-Kisāʾī —
mīm frappée ; al-Zaǧǧāǧ, Makki b. Abī Ṭālib al-Qaysī d'après al-Farrāʾ,
al-Kisāʾī et le nom du coude, Abū Ḥātim et la place, le lieu de prosternation,
deux usages de langue), aṭ-Ṭabarī (deux lectures d'un même sens), les
subtilités (les ornements de sens et la variation des modes d'exposition, la
métaphore explicite du lien et le fagot de brindilles, le ilitifāt et le
cœur siège stable de la foi et de la mécréance, at-Taghābun, at-Tawba, le
hadith de la morsure de chair [Ṣaḥīḥ al-Bukhārī, livre de la foi], ʿĀʾiša et
l'invocation « Ô Celui qui retourne les cœurs », le cœur entre les doigts
d'Allah, le degré de l'agrément et l'accueil, « Préserve les ordres d'Allah »
[at-Tirmiḏī]), la structure (objectifs, tamhīd, quête méthodologique,
commentaire en trois têtes, subtilités, évaluation, exploitation, Source du
cours), l'investissement (les trois écoles du rasm d'« idhan » — al-Farrāʾ,
al-Māzinī, Ibn Mālik [at-Tasḥīl], le rasm du muṣḥaf, al-Mubarrad, al-Naḥḥās,
ʿAlī b. Sulaymān, le tanwīn n'entrant point dans les lettres, le détail de
l'opérante et de l'élidée, al-Mālaqī et le Rafṣ al-mabānī), 0 arabe résiduel
(ﷺ exempté)."""
import json
import re
import sys

HTML = "scripts-translate/tr-tmp/pdf-mut23h3c-742.html"
html = open(HTML, encoding="utf-8").read()
norm = re.sub(r"[ \u202f\u00a0]+", " ", html.replace("&nbsp;", "\u00a0"))
errors = []

# 1. structure et marqueurs
if "Source du cours" not in norm:
    errors.append("Source du cours absent du DOM")
for frag in [
    "Quatrième leçon du second livre du parcours",
    "tafsir-3-thanawi_text.pdf",
    "mécanique R458",
    "jamais devinées",
    "Les objectifs de la leçon",
    "Le tamhīd",
    "Le commentaire",
    "Les subtilités et les bienfaits",
    "L’évaluation",
    "L’exploitation",
    "la présente passe l’a relue in extenso",
    "la quête de la leçon suit la méthodologie",
]:
    if frag.lower() not in norm.lower():
        errors.append(f"fragment attendu absent : {frag[:55]}")

# 2. les āyāt 15-16 rendues en français (rasm warš du cache) — présence
rendus = [
    "Voici notre peuple : ils ont pris en dehors de Lui des divinités — ah, si seulement ils venaient avec une autorité évidente à leur sujet ! Qui donc est plus injuste que celui qui forge, au sujet d’Allah, le mensonge ?",
    "Et lorsque vous les aurez quittés, eux et ce qu’ils adorent en dehors d’Allah, réfugiez-vous dans la Caverne : votre Seigneur y répandra pour vous de Sa miséricorde, et Il vous disposera de votre affaire un agrément.",
    "(15-16)",
]
for r in rendus:
    if r not in norm:
        errors.append(f"rendu coranique attendu absent : {r[:55]}")

# 3. contenu : lemmes, lectures, mufassirūn, grammaire, subtilités, investissement
contenu = [
    "la sérénité pour Son prophète",
    "sans accroissement ni retranchement",
    "pas entièrement véridique",
    "l’œuvre salutaire",
    "l’ascèse en ce bas monde",
    "accroissements sur la foi",
    "Banū Isrāʾīl les avaient chargés",
    "Ibn Kaṯīr",
    "des adolescents",
    "des vieillards qui s’étaient obstinés",
    "aux anciens de Quraysh",
    "la voie droite",
    "il n’est de divinité que Lui",
    "aṭ-Ṭabarī",
    "d’une claire-voyance dans leur religion",
    "l’exil de la demeure de leur peuple",
    "la dureté de la résidence dans la caverne de la montagne",
    "l’accroissement de la foi et de sa différenciation",
    "al-Buḫārī",
    "Jāmiʿ al-bayān",
    "le lien sur leurs cœurs",
    "entre la guidée et l’égarement",
    "le doute et le soupçon",
    "rābiṭ",
    "la mère de Mūsā",
    "al-Qaṣaṣ",
    "deux sens",
    "le roi mécréant",
    "avec le plus grand sérieux",
    "n’ayant nulle indépendance",
    "l’immersion de la durée",
    "dévié du droit",
    "le dépassement de la limite",
    "au-dessus de sa valeur",
    "un tanwīn de remplacement",
    "la phrase conditionnelle",
    "sur l’adverbe",
    "Voici notre peuple",
    "l’incapacitation",
    "la preuve en est manifeste",
    "du Créateur",
    "sans preuve ni autorité",
    "le plus odieux des mensonges",
    "la déchirure",
    "une interrogation de négation",
    "qu’appendice du relatif",
    "la tāʾ de l’iftiʿāl",
    "la quête de l’isolement",
    "le pronom des sujets",
    "au groupe des jeunes gens",
    "en quête du salut et du délivrement",
    "un nom relatif accouplé",
    "la hāʾ et de la mīm",
    "la particule de négation",
    "une exemption disjointe",
    "non rattachée au premier",
    "l’exemption serait rattachée",
    "Qatāda",
    "en dehors de nous",
    "le sens implicite",
    "selon la mesure de ce bas monde",
    "leur affaire ultime",
    "au jussif",
    "le répondant de l’ordre",
    "un nom verbal mīmī",
    "Nāfiʿ",
    "Ibn ʿĀmir",
    "Abū Jaʿfar",
    "Abū ʿAmr",
    "ʿĀṣim",
    "Ḥamza",
    "al-Kisāʾī",
    "al-Zaǧǧāǧ",
    "Makki b. Abī Ṭālib al-Qaysī",
    "al-Farrāʾ",
    "Abū Ḥātim",
    "le nom du coude",
    "le nom du lieu de prosternation",
    "deux usages de langue",
    "deux lectures d’un même sens",
    "des ornements de sens",
    "variation des modes d’exposition",
    "une métaphore explicite",
    "le fagot de brindilles",
    "le siège stable de la foi et de la mécréance",
    "at-Taghābun",
    "at-Tawba",
    "une morsure de chair",
    "Ṣaḥīḥ al-Bukhārī",
    "livre de la foi",
    "ʿĀʾiša",
    "Ô Celui qui retourne les cœurs",
    "Il l’incline",
    "le degré de l’agrément",
    "at-Tirmiḏī",
    "Le passage du discours",
    "idhan",
    "al-Māzinī",
    "Ibn Mālik",
    "at-Tasḥīl",
    "le rasm du muṣḥaf",
    "al-Mubarrad",
    "al-Naḥḥās",
    "ʿAlī b. Sulaymān",
    "le tanwīn n’entre point dans les lettres",
    "si elle est opérante",
    "élidée",
    "al-Mālaqī",
    "Rafṣ al-mabānī",
    "les écoles des grammairiens",
    "le rasm ʿuthmānien",
    "Ḥasan al-Baṣrī",
    "la sagesse du retournement",
    "la page 37",
    "la page imprimée 36",
    "(13-16)",
    "(15-16)",
    "la leçon 28 d’Isrāʾ",
]
for c in contenu:
    if c not in norm:
        errors.append(f"contenu attendu absent : {c[:55]}")

# 4. ABSENCE — rendus des āyāt des leçons voisines (13-14 livrés en 741,
#    6-9 en 740) ; rasm nu du cache interdit pour toutes les āyāt
for probe in [
    "C’est Nous qui te rapportons leur récit en vérité",
    "Et Nous affermîmes leurs cœurs",
    "Quand les jeunes gens se furent réfugiés dans la Caverne, ils dirent",
    "donne-nous de Ta part une miséricorde",
    "Nous frappâmes alors sur leurs oreilles",
    "Puis Nous les ressuscitâmes",
    "une chose étonnante",
    "Ou bien penses-tu",
    "par affliction",
    "te consumer",
    "sol aride",
    "parure pour elle",
    "ont constitué une chose extraordinaire",
    "nos concitoyens",
    "une preuve évidente",
    "Quel pire injuste",
    "adopté en dehors de Lui des divinités",
    "violence sévère",
    "Grave comme parole",
]:
    if probe in norm:
        errors.append(f"rendu hors matière présent : {probe[:50]}")

cache = json.load(open("scripts-translate/quran-cache.json", encoding="utf-8"))
rasm_18 = {n: t for n, t in cache["18"]["ar"]}
for n in range(6, 19):
    t = rasm_18[n]
    probes = [t, t.replace(" ", "")]
    ok = any(p in norm.replace(" ", "") for p in probes) or t in norm
    if ok:
        errors.append(f"rasm arabe interdit présent au corps (āya 18:{n})")

# 5. 0 arabe résiduel (ﷺ U+FDFA exempté, convention du corpus)
ARABIC = re.compile(r"[\u0600-\u06FF\u0750-\u077F\u08A0-\u08FF\uFB50-\uFDF9\uFDFB-\uFDFF\uFE70-\uFEFF]")
resid = ARABIC.findall(norm)
if resid:
    errors.append(f"arabe résiduel : {len(resid)} caractère(s), ex. {[c for c in resid[:5]]}")

if errors:
    print("verify-742 FAIL :")
    for e in errors:
        print(" -", e)
    sys.exit(1)
print("verify-742 PASS — structure OK, 2 rendus warš présents (18:15-16), contenu complet, 0 rendu hors matière (13-14/6-9), 0 rasm étranger 18:6-18, 0 arabe résiduel (ﷺ exempté)")

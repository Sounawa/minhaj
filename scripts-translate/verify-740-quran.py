#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Minhāj — contrôle coranique et de contenu de la leçon 740 (tafsir-5ep,
sūrat al-Kahf v6-9 — deuxième leçon du second livre, pages 17-22 du manuel
miroir tafsir-3-thanawi). Les āyāt 6-9 sont rendues en français sur le rasm
warš du cache (présence vérifiée) ; le rasm nu du cache interdit au corps
(0 arabe — FR-seule) ; les āyāt des autres leçons interdites au rendu français
comme au rasm (l'āya 10, ouverture de la leçon 3, ne peut être ni rendue ni
cité en rasm ; les rendus français de la leçon 739 — āyāt 1-5 — absents) ;
contrôle de contenu : la consolation du Prophète ﷺ (at-Tawba 128), az-Zaǧǧāǧ,
Qatāda, Mujāhid (az-Zukhruf 55), al-Aʿshā, Yaʿqūb (Yūsuf 86), les sens de
« ṣaʿīd » et « ǧurz » (Qatāda, az-Zaǧǧāǧ, Ibn ʿAṭiyya), Muḥammad b. Isḥāq,
les propos sur ar-Raqīm (Kaʿb, Ibn ʿAbbās, aṣ-Ṣuddī, ʿAbd ar-Raḥmān b. Zayd
b. Aslam, ʿUṣbān-Ayla), aṭ-Ṭabarī (Ibn Ǧurayǧ, Ibn Naǧīḥ, Ibn Isḥāq), les
subtilités (phrase nominale, lām de l'emphase, Ṭā-hā 131), l'invocation
d'at-Tirmiḏī 3502 (chapelet du tasbīḥ), la structure (objectifs, tamhīd,
commentaire, subtilités, évaluation, exploitation, Source du cours),
0 arabe résiduel (ﷺ exempté)."""
import json
import re
import sys

HTML = "scripts-translate/tr-tmp/pdf-mut23h3c-740.html"
html = open(HTML, encoding="utf-8").read()
norm = re.sub(r"[ \u202f\u00a0]+", " ", html.replace("&nbsp;", "\u00a0"))
errors = []

# 1. structure et marqueurs
if "Source du cours" not in norm:
    errors.append("Source du cours absent du DOM")
for frag in [
    "Deuxième leçon du second livre du parcours",
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
]:
    if frag not in norm:
        errors.append(f"fragment attendu absent : {frag[:55]}")

# 2. les āyāt 6-9 rendues en français (rasm warš du cache) — présence
rendus = [
    "Peut-être vas-tu te consumer de chagrin à leur suite, s’ils ne croient pas à ce discours, par affliction.",
    "En vérité, Nous avons fait ce qui est sur la terre comme parure pour elle, afin d’éprouver lequel d’entre eux agit le mieux.",
    "Et en vérité, Nous allons faire de ce qui est sur elle un sol aride, dénudé.",
    "Ou bien penses-tu que les gens de la Caverne et d’ar-Raqīm furent, parmi Nos signes, une chose étonnante ?",
    "(6-9)",
]
for r in rendus:
    if r not in norm:
        errors.append(f"rendu coranique attendu absent : {r[:55]}")

# 3. contenu : consolation, mufassirūn, ar-Raqīm, subtilités, invocation
contenu = [
    "at-Tawba 128",
    "il est soucieux pour vous",
    "envers les croyants, il est compatissant et miséricordieux",
    "Az-Zaǧǧāǧ",
    "Qatāda",
    "Mujāhid",
    "az-Zukhruf 55",
    "Quand ils Nous eurent mis en colère, Nous Nous vengeâmes d’eux, tous",
    "Yūsuf 86",
    "je ne me plains qu’auprès d’Allah de mon déchirement et de mon chagrin",
    "al-Aʿshā",
    "Abū ʿAṭiyya",
    "Muḥammad b. Isḥāq",
    "Ibn ʿAṭiyya",
    "an-Naḥḥās",
    "Kaʿb",
    "aṣ-Ṣuddī",
    "ʿAbd ar-Raḥmān b. Zayd b. Aslam",
    "ʿUṣbān et Ayla",
    "Ibn Ǧurayǧ",
    "Ibn Naǧīḥ",
    "aṭ-Ṭabarī",
    "Ibn Isḥāq",
    "Ṭā-hā 131",
    "parure de la vie d’ici-bas",
    "le repos de ton Seigneur est meilleur et plus durable",
    "phrase nominale",
    "lām",
    "Sunan at-Tirmiḏī",
    "chapelet du tasbīḥ",
    "hadith 3502",
    "r-r-š-d",
]
for c in contenu:
    if c not in norm:
        errors.append(f"contenu attendu absent : {c[:55]}")

# 4. ABSENCE — rasm nu du cache interdit (FR-seule), āya 10 et leçons voisines
cache = json.load(open("scripts-translate/quran-cache.json", encoding="utf-8"))
rasm_18 = {n: t for n, t in cache["18"]["ar"]}
for n in (6, 7, 8, 9, 10):
    t = rasm_18[n]
    probes = [t, t.replace(" ", "")]
    ok = any(p in norm.replace(" ", "") for p in probes) or t in norm
    if ok:
        errors.append(f"rasm arabe interdit présent au corps (āya 18:{n})")
for probe in [
    "Louange à Allah qui a fait descendre le Livre sur Son serviteur",
    "violence sévère",
    "Grave comme parole",
    "donne-nous une miséricorde",
]:
    if probe in norm:
        errors.append(f"rendu hors matière présent : {probe[:50]}")

# 5. 0 arabe résiduel (ﷺ U+FDFA exempté, convention du corpus)
ARABIC = re.compile(r"[\u0600-\u06FF\u0750-\u077F\u08A0-\u08FF\uFB50-\uFDF9\uFDFB-\uFDFF\uFE70-\uFEFF]")
resid = ARABIC.findall(norm)
if resid:
    errors.append(f"arabe résiduel : {len(resid)} caractère(s), ex. {[c for c in resid[:5]]}")

if errors:
    print("verify-740 FAIL :")
    for e in errors:
        print(" -", e)
    sys.exit(1)
print("verify-740 PASS — structure OK, 4 rendus warš présents (18:6-9), contenu complet, 0 rasm étranger, 0 arabe résiduel (ﷺ exempté)")

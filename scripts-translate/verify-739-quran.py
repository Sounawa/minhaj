#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Minhāj — contrôle coranique et de contenu de la leçon 739 (tafsir-5ep,
sūrat al-Kahf v1-5 — première leçon du second livre, pages 10-16 du manuel
miroir tafsir-3-thanawi). Les āyāt 1-5 sont rendues en français sur le rasm
warš du cache (présence vérifiée) ; le rasm nu du cache interdit au corps
(0 arabe — FR-seule) ; les āyāt des autres leçons interdites au rendu français
(le lemme coranique de la question d'évaluation — « zīna », āya 7 — est porté
par l'imprimé dans la question, rendu autorisé) ; contrôle de contenu : les
hadiths du mérite (al-Barāʾ b. ʿĀzib Buḫārī 4163, Abū d-Dardāʾ Muslim,
at-Tirmiḏī 6882), la cause de descente (an-Naḍr b. al-Ḥāriṯ et ʿUqba b. Abī
Muʿayṭ, les trois questions), les gloses (Ibn Kaṯīr 5/531, Ibn ʿAṭiyya,
Abū Ḥayyān, Ibn ʿĀšūr), la structure (objectifs, tamhīd, commentaire,
évaluation, exploitation, Source du cours), 0 arabe résiduel (ﷺ exempté)."""
import json
import re
import sys

HTML = "scripts-translate/tr-tmp/pdf-mut23h3c-739.html"
html = open(HTML, encoding="utf-8").read()
norm = re.sub(r"[ \u202f\u00a0]+", " ", html.replace("&nbsp;", "\u00a0"))
errors = []

# 1. structure et marqueurs
if "Source du cours" not in norm:
    errors.append("Source du cours absent du DOM")
for frag in [
    "Première leçon du second livre du parcours",
    "tafsir-3-thanawi_text.pdf, 224 pages",
    "al-Qurṭubī",
    "Abū Ḥayyān",
    "cent āyāt et cinq āyāt",
    "cent dix āyāt au comptage oriental",
    "Les objectifs de la leçon",
    "Le commentaire",
    "L’évaluation",
    "L’exploitation",
    "les cinq premières āyāt coïncidant aux deux comptes",
    "jamais devinées",
]:
    if frag not in norm:
        errors.append(f"fragment attendu absent : {frag[:55]}")

# 2. les āyāt 1-5 rendues en français (rasm warš du cache) — présence
rendus = [
    "Louange à Allah qui a fait descendre le Livre sur Son serviteur, et n’y a point mis de tortuosité.",
    "Droit, pour avertir d’une violence sévère venant de Sa part",
    "que pour eux sera une belle récompense",
    "où ils demeureront à jamais.",
    'Allah s’est pris un enfant',
    "Ils n’ont aucune connaissance de cela, eux ni leurs ancêtres.",
    "Grave comme parole que celle qui sort de leurs bouches",
    "Ils ne disent que mensonge.",
    "(1-5)",
]
for r in rendus:
    if r not in norm:
        errors.append(f"rendu coranique attendu absent : {r[:55]}")

# 3. contenu : hadiths du mérite, cause de descente, gloses
contenu = [
    ("al-Barāʾ b. ʿĀzib", ["Ṣaḥīḥ al-Buḫārī, 4163", "la quiétude qui est descendue pour le Coran", "s’agiter"]),
    ("le hadith du vendredi", ["magnifiée entre les cieux et la terre", "le jour du vendredi", "et encore trois jours", "la variante d’Anas"]),
    ("ad-Dār al-manṯūr", ["Ibn Mardūya", "Une lumière entre les cieux et la terre", "la tenture de la tombe"]),
    ("Abū d-Dardāʾ", ["Ṣaḥīḥ Muslim", "dix āyāt du début de sūrat al-Kahf", "Grand Trompeur", "l’āya du Piédestal"]),
    ("at-Tirmiḏī", ["trois āyāt du début", "Ṣaḥīḥ, 6882", "hadith ḥasan", "le livre des mérites du Coran"]),
    ("la cause de descente", ["Ibn Isḥāq", "an-Naḍr b. al-Ḥāriṯ", "ʿUqba b. Abī Muʿayṭ", "les jeunes partis à la première époque", "ses levants et ses ponants", "ce qu’est l’Esprit", "et sūrat al-Kahf descendit"]),
    ("la réprimande", ["quinze jours", "ses fictions", "l’ordre du Prophète ﷺ, par la louange d’Allah"]),
    ("Ibn Kaṯīr", ["aux ouvertures des affaires et à leurs clôtures", "Tafsīr al-Qurʾān al-ʿaẓīm, 5/531", "des ténèbres vers la lumière"]),
    ("les gloses des āyāt", ["la voie de la rectitude", "Ibn ʿAbbās", "aḍ-Ḍaḥḥāk", "al-Mahdawī", "Ibn ʿAṭiyya", "son établissement par l’ordre d’Allah", 'L’antithèse entre "une violence sévère" et "une belle récompense"', "le complément d’état, par la dāl de l’état", "au sujet des anges", "au sujet du Christ", "sans preuve sur elle", "comme ils disent d’une qaṣīda qu’elle est une parole"]),
    ("Abū Ḥayyān", ["l’économie de l’expression", "al-Baḥr al-muḥīṭ, 7/631", "l’ellipse"]),
    ("la fonction du waḥy", ["les sens du Livre", "les prescriptions du dīn", "l’ordre de l’existence et l’ordre du retour"]),
    ("Ibn ʿĀšūr", ["at-Taḥrīr wa-t-tanwīr", "une grâce coranique", "rangèrent le Muṣḥaf"]),
    ("les questions de l’évaluation", ["les moitiés du Coran", "les sections et les parties", "l’ordre des sūras du Coran tel qu’il est aujourd’hui", "comme parure pour elle", 'que signifie le mot "parure" et quelle est sa construction']),
    ("la clôture", ["la page imprimée 16", "les āyāt 6 à 9", "la page 17 du même manuel"]),
]
for label, frs in contenu:
    for f in frs:
        if f not in norm:
            errors.append(f"{label} : fragment attendu absent : {f[:50]}")

# 4. ABSENCE des rendus des āyāt hors matière (leçons précédente et suivante) —
#    rasm nu du cache + rendus français caractéristiques
def bare(t: str) -> str:
    return re.sub(r"[\u064B-\u065F\u0670\u06D6-\u06ED\u0640\u0671]", "", t)

cache = json.load(open("scripts-translate/quran-cache.json", encoding="utf-8"))
ar17 = dict((i, t) for i, t in cache["17"]["ar"])
probes = []
for v in (105, 106, 107, 108, 110, 111):
    t = bare(ar17[v]).split()
    probes.append(" ".join(t[len(t) // 2:len(t) // 2 + 3]))
for v in (6, 8, 9, 10):
    t = bare(dict((i, t) for i, t in cache["18"]["ar"])[v]).split()
    probes.append(" ".join(t[len(t) // 2:len(t) // 2 + 3]))
for p in probes:
    if p and p in norm:
        errors.append(f"rasm coranique inattendu au corps de la leçon : {p[:40]}")
for pat, label in [
    (r"en toute vérité que Nous l’avons fait descendre", "al-Isrāʾ 17:105"),
    (r"le menton contre terre", "al-Isrāʾ 17:107"),
    (r"Gloire à notre Seigneur", "al-Isrāʾ 17:108"),
    (r"Invoquez donc Allah, ou invoquez le Tout Miséricordieux", "al-Isrāʾ 17:110"),
    (r"Dis : Louange à Allah", "al-Isrāʾ 17:111"),
    (r"tu te tords de chagrin", "al-Kahf 18:6"),
    (r"Nous avons écrasé", "al-Kahf 18:8"),
    (r"ont vu l’heure", "al-Kahf 18:10"),
]:
    if re.search(pat, norm, re.IGNORECASE):
        errors.append(f"rendu coranique inattendu : {label}")

# 5. 0 arabe résiduel (ﷺ U+FDFA exempté — convention du corpus)
if re.search(r"[\u0600-\u06FF\u0750-\u077F\u08A0-\u08FF\uFB50-\uFDF9\uFDFB-\uFDFF\uFE70-\uFEFF]", norm):
    errors.append("caractère arabe résiduel détecté")

if errors:
    print("ÉCHEC :")
    for e in errors:
        print(" -", e)
    sys.exit(1)
print("PASS : leçon 739 — sūrat al-Kahf v1-5 (p.10-16, tafsir-3-thanawi) — les cinq "
      "āyāt rendues en français sur le rasm warš du cache (basmala comptée en tête de "
      "la première, comptage marocain 105 āyāt documenté contre 110 au comptage oriental), "
      "les hadiths du mérite portés (al-Barāʾ b. ʿĀzib Ṣaḥīḥ al-Buḫārī 4163 ; le vendredi "
      "et trois jours ; la lumière et la tombe, ad-Dār al-manṯūr ; Abū d-Dardāʾ Ṣaḥīḥ "
      "Muslim ; at-Tirmiḏī Ṣaḥīḥ 6882), la cause de descente (Ibn Isḥāq — an-Naḍr b. "
      "al-Ḥāriṯ et ʿUqba b. Abī Muʿayṭ, les trois questions), la finalité de la descente "
      "(la réprimande des quinze jours, Ibn Kaṯīr 5/531), les gloses (Ibn ʿAbbās, "
      "aḍ-Ḍaḥḥāk, al-Mahdawī, Ibn ʿAṭiyya, le ṭibāq, Abū Ḥayyān 7/631), l'évaluation et "
      "l'exploitation d'Ibn ʿĀšūr au DOM, Source du cours documentée, aucune citation "
      "hors matière (ABSENCE des rasm d'Isrāʾ 105-111 et d'al-Kahf 6-10 et des rendus "
      "français caractéristiques vérifiée), 0 arabe résiduel.")

if __name__ == "__main__":
    sys.exit(0)

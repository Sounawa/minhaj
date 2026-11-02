#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Minhāj — contrôle coranique et de contenu de la leçon 750 (tafsir-5ep,
sūrat al-Kahf v36-43 de l'imprimé warš — douzième leçon du second livre, pages
87-95 du manuel miroir tafsir-3-thanawi). La numérotation de l'imprimé suit le
décompte warš : la plage imprimée (36-43) correspond aux āyāt 37-44 du cache
canonique (ḥafṣ) — décalage de un tranché sur le bloc coranique de p.87. Les
huit āyāt sont rendues en français sur le cache (présence vérifiée) ; les
āyāt 1-36 (leçons 739-749) et 45-46 (leçon 751) sont interdites de double
rendu ; le rasm nu du cache interdit au corps (0 arabe — FR-seule)."""
import json
import re
import sys

HTML = "tr-tmp/lesson-750-fr.html"
html = open(HTML, encoding="utf-8").read()
norm = re.sub(r"[ \u202f\u00a0]+", " ", html.replace("&nbsp;", "\u00a0"))
errors = []

# 1. structure et marqueurs
for frag in [
    "Source du cours",
    "Douzième leçon du second livre du parcours",
    "pages 87 à 95 de l’imprimé miroir",
    "1_20220304_20220304_2251",
    "p.87 ouvre la leçon 12",
    "Les objectifs de la leçon",
    "Le tamhīd",
    "Le commentaire",
    "La glose",
    "L’extraction des thèmes des āyāt",
    "Premièrement",
    "Deuxièmement",
    "Troisièmement",
    "Quatrièmement",
    "Les subtilités et les bienfaits",
    "L’évaluation",
    "L’exploitation",
    "la page imprimée 95",
    "jamais devinée",
    "interdites de double rendu",
    "décalage de un tranché",
    "plage imprimée (36-43) correspond aux āyāt 37 à 44 du cache canonique",
]:
    if frag.lower() not in norm.lower():
        errors.append(f"fragment attendu absent : {frag[:55]}")

# 2. les āyāt 37-44 rendus du cache — présence (8 rendus + 8 numéros)
cache = json.load(open("scripts-translate/quran-cache.json", encoding="utf-8"))
fr18 = {n: t for n, t in cache["18"]["fr"]}
rendus = [fr18[n] for n in range(37, 45)] + [f"({n})" for n in range(37, 45)]
# adaptation du cache : apostrophes droites -> typographiques ; comparaison
# insensible aux espaces (l'auto-fix NNBSP décale « : » du cache)
rendus_norm = [r.replace("'", "’").replace(" ", "") for r in rendus]
compact = norm.replace(" ", "")
for r in rendus_norm:
    if r not in compact:
        errors.append(f"rendu coranique attendu absent : {r[:55]}")

# 3. contenu attendu (confrontation au manuel — glose, lectures, exégètes)
contenu = [
    "le verbe du voir régit un second objet",
    "tamyīz, la spécification",
    "la première des deux en l’usage",
    "la sauterelle",
    "la nuée",
    "la pluie de pierres",
    "l’oreiller",
    "le Ǧawharī a dit",
    "le ḥusbān, au ḍamm, est le châtiment",
    "un lieu de glisse",
    "le nom verbal érigé au rang de l’objet",
    "un homme équitable et une femme équitable",
    "s’enfonçant dans la terre, nul ne peut le saisir",
    "la forme nominale est érigée au rang de la forme verbale",
    "la ruine totale",
    "la création de ton père Ādam de la terre",
    "Ibn Kaṯīr a dit",
    "négation et une magnification",
    "une eau méprisable",
    "il fut d’abord inexistant, puis exista",
    "Créateur de toute chose",
    "Tafsīr al-Qurʾān al-ʿaẓīm",
    "783",
    "Abū Ḥayyān a dit",
    "l’origine de sa naissance et de son existence après le néant",
    "la preuve de la possibilité de la résurrection des tombeaux",
    "l’annonce des véridiques",
    "al-Baḥr al-Muḥīṭ",
    "7/771",
    "le propriétaire des deux ǧannāt était associateur",
    "le pronom du récit et de l’actualité",
    "la masse des lecteurs",
    "l’un fut assimilé dans l’autre",
    "al-Fakhr ar-Rāzī a dit",
    "Mafātīḥ al-Ġayb",
    "al-Zajjāj et al-Farrāʾ ont dit",
    "ce que Dieu a voulu, ou bien",
    "l’ordre est la volonté de Dieu Très-Haut",
    "le plus noble et le plus élevé en bien et en vertu",
    "la plus forte réprobation de l’interpellé",
    "un verbe plein qui ne saurait servir de condition",
    "la plus douloureuse pour lui-même",
    "l’entour est la métonymie de la généralité du châtiment",
    "l’agent fut tu, et le verbe bâti pour l’inconnu",
    "retourner l’une des paumes sur le dos de l’autre",
    "l’affligé qui regrette",
    "une formule coranique en une extrême merveille et élévation",
    "la sourate de la Vache",
    "la sourate du Pèlerinage",
    "effondrée sur ses toits",
    "la ruine des fruits et la ruine de l’origine",
    "al-Ǧāṣṣāṣ",
    "5/662",
    "un récit du dire du mécréant en l’āḫira",
    "par voie de repentir après l’arrivée de la calamité",
    "une réprobation des mécréants, de Qurayš",
    "Pharaon au terme de la fin",
    "le regret qui ne profite en rien",
    "avec le tāʾ du féminin",
    "au yāʾ, au sens",
    "parce qu’ils sont mâles",
    "la bande vers laquelle on s’enfuit pour être secouru",
    "Mujāhid a dit",
    "c’est la parentèle",
    "Ibn ʿAṭiyya a dit",
    "Abū ʿAlī al-Fārisī",
    "la ʿayn effacée par allègement",
    "le plus solide en le sens",
    "vaincu, sans retour",
    "quiconque s’oppose à Dieu",
    "un adverbe de lieu",
    "la demeure de l’āḫira",
    "les lecteurs ont divergé",
    "la pause de l’ʾimām Abū ʿAbd Allāh al-Habaṭī",
    "a pesé l’angle grammatical des deux pauses",
    "al-Zajjāj a dit",
    "7/281",
    "au kasr de la wāw",
    "la préséance et de la chefferie",
    "la fatḥa de la wāw",
    "l’alliance et du lien",
    "adjectif du Nom de Majesté",
    "en ce lieu le jugement appartient à Dieu, le Vrai",
    "389-393",
    "belle et droite",
    "le pronom retourne sur Dieu Très-Haut",
    "l’alif du féminin tronqué",
    "al-Qurṭubī a dit",
    "la meilleure issue pour celui qui Lui voue son espoir",
    "son ultime et son terme",
    "5/762",
    "Mālik",
    "Tartīb al-Madārik",
    "1/130",
    "Ašhab a dit",
    "quiconque entre sa demeure de dire cela",
    "Abū Mūsā al-ʾAšʿarī",
    "un trésor des trésors de la ǧanna",
    "Ṣaḥīḥ Muslim",
    "4072",
    "La gratitude est la bride des bienfaits",
    "le bénéfice de Ses créatures",
    "« si » est souvent employée pour le détesté",
    "travaux des groupes",
    "le badge de la leçon 13",
]
for c in contenu:
    if c.lower() not in norm.lower():
        errors.append(f"contenu attendu absent : {c[:55]}")

# 4. rendus interdits (āyāt 1-36 livrées leçons 739-749 ; 45-46 leçon 751)
interdits = [
    "Louange à Dieu qui a fait descendre sur Son serviteur",
    "Ils resteront dans leur refuge pour l'éternité",
    "et je ne pense pas que l'Heure viendra",
    "Toute âme doit goûter la mort",
    "Donne-leur l'exemple de deux hommes",
    "Les deux jardins produisaient leur récolte",
    "Il entra dans son jardin coupable envers lui-même",
    "Propose-leur la parabole de la vie en ce monde",
    "Et les croyants et les Juifs",
    "par la sagesse et par la bonne exhortation",
    "ne serions-Nous pas capables de les ressusciter",
    "Et à celui qui croit et fait le bien",
]
interdits_norm = [r.replace("'", "’") for r in interdits]
for probe in interdits_norm:
    if probe in norm:
        errors.append(f"rendu hors matière présent : {probe[:50]}")

rasm_18 = {n: t for n, t in cache["18"]["ar"]}
for n in range(1, 45):
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

# 6. typographie
if "'" in html:
    errors.append("apostrophe droite présente")
if html.count("«") != html.count("»"):
    errors.append(f"guillemets non appariés : « {html.count('«')} vs » {html.count('»')}")

total = 22 + len(rendus) + len(contenu) + 12 + 44 + 3
print(f"verify-750-quran : {total} contrôles — rendus {len(rendus)} + contenu {len(contenu)} + interdits {12 + 44} + structure {22} + typo 3")
if errors:
    print("verify-750 FAIL :")
    for e in errors:
        print(" -", e)
    sys.exit(1)

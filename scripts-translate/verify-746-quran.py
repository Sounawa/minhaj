#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Minhāj — contrôle coranique et de contenu de la leçon 746 (tafsir-5ep,
sūrat al-Kahf v25-27 — huitième leçon du second livre, pages 58-64 du manuel
miroir tafsir-2-thanawi). Les āyāt 25-27 sont rendues en français sur le rasm
warš du cache (présence vérifiée) ; les parallèles az-Zumar 53 et al-Ǧumuʿa 2
rendus du cache ; le double rendu des āyāt 19-24 (leçons 744-745) et des
āyāt 6-18 (740-743) est interdit ; le rasm nu du cache interdit au corps
(0 arabe — FR-seule) pour TOUTES les āyāt voisines (6-27)."""
import json
import re
import sys

HTML = "tr-tmp/lesson-746-fr.html"
html = open(HTML, encoding="utf-8").read()
norm = re.sub(r"[ \u202f\u00a0]+", " ", html.replace("&nbsp;", "\u00a0"))
errors = []

# 1. structure et marqueurs
for frag in [
    "Source du cours",
    "Huitième leçon du second livre du parcours",
    "pages 58 à 64 de l’imprimé miroir",
    "1_20220304_20220304_2251",
    "Les objectifs de la leçon",
    "Le tamhīd",
    "Le commentaire",
    "Les subtilités et les bienfaits",
    "L’évaluation",
    "L’exploitation",
    "la page imprimée 64",
    "jamais deviné",
]:
    if frag.lower() not in norm.lower():
        errors.append(f"fragment attendu absent : {frag[:55]}")

# 2. les āyāt 25-27 + parallèles rendus du cache — présence (12 rendus)
rendus = [
    "Or, ils demeurèrent dans leur caverne trois cents ans et en ajoutèrent neuf (années).",
    "Dis : Dieu sait mieux combien de temps ils demeurèrent là.",
    "À Lui appartient l’Inconnaissable des cieux et de la terre.",
    "Comme Il est Voyant et Audient",
    "Ils n’ont aucun allié en dehors de Lui et Il n’associe personne à Son commandement.",
    "Et récite ce qui t’a été révélé du Livre de ton Seigneur. Nul ne peut changer Ses paroles.",
    "Et tu ne trouveras, en dehors de Lui, aucun refuge.",
    "(25-27)",
    "ne désespérez pas de la miséricorde de Dieu. Car Dieu pardonne tous les péchés. Oui, c’est Lui le Pardonneur, le Très Miséricordieux.",
    "un Messager des leurs qui leur récite Ses versets, les purifie et leur enseigne le Livre et la Sagesse",
    "trois cents ans au calendrier solaire",
    "neuf ans de plus au calendrier lunaire",
]
for r in rendus:
    if r not in norm:
        errors.append(f"rendu coranique attendu absent : {r[:55]}")

# 3. contenu attendu (confrontation au manuel et au récit R502)
contenu = [
    "wa-labithū",
    "tamyīz",
    "Ḥamza et al-Kisāʾī",
    "Abū ʿAlī al-Fārisī",
    "al-Qurṭubī",
    "al-Ǧāmiʿ li-aḥkām al-Qurʾān",
    "5/252",
    "Quṭāda",
    "Muṭʿim al-Warrāq",
    "Banū Isrāʾīl",
    "ibn Masʿūd",
    "Aṭ-Ṭabarī",
    "Ǧāmiʿ al-bayān",
    "Ibn ʿAṭiyya",
    "Mujāhid",
    "aḍ-Ḍaḥḥāk",
    "Qushayrī",
    "cent dirhams et cinq",
    "al-ʿAnawī",
    "l’inimitabilité du Qurʾān noble",
    "le Prophète illettré",
    "ḥaṣr",
    "Murra",
    "MARYAM",
    "Ibn ʿĀmir",
    "la yāʾ",
    "tāʾ et au jussif",
    "Lā mubaddila",
    "az-Zumar : 53",
    "al-Ǧumuʿa : 2",
    "la rime",
    "qarīna",
    "l’exclusivité de Dieu, Très-Haut, pour la science de l’invisible",
    "la durée du séjour des jeunes gens dans la Caverne",
    "tel qu’imprimé",
    "fragment imprimé altéré, déclaré",
    "formation de groupes",
]
for c in contenu:
    if c not in norm:
        errors.append(f"contenu attendu absent : {c[:55]}")

# 4. ABSENCE — rendus des āyāt des leçons voisines (19-24 livrés en 744-745,
#    6-18 en 740-743 ; 28-29 = leçon suivante) — rasm nu du cache interdit
for probe in [
    "Et ainsi Nous les ressuscitâmes, afin qu’ils s’interrogent les uns les autres",
    "combien avez-vous demeuré",
    "Car s’ils se manifestaient à vous, ils vous lapideraient",
    "Et c’est ainsi que Nous fîmes qu’ils furent découverts",
    "construisez sur eux un édifice",
    "ils étaient trois et le quatrième était leur chien",
    "je la ferai sûrement demain",
    "C’est Nous qui te rapportons leur récit en vérité",
    "Tu verras le soleil",
    "Nous frappâmes alors sur leurs oreilles",
    "fais patienter ton âme avec ceux qui invoquent",
]:
    if probe in norm:
        errors.append(f"rendu hors matière présent : {probe[:50]}")

cache = json.load(open("scripts-translate/quran-cache.json", encoding="utf-8"))
rasm_18 = {n: t for n, t in cache["18"]["ar"]}
for n in range(6, 28):
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

total = 12 + len(rendus) + len(contenu) + 11 + 22 + 3
print(f"verify-746-quran : {total} contrôles — rendus {len(rendus)} + contenu {len(contenu)} + interdits {11 + 22} + structure {12} + typo 3")
if errors:
    print("verify-746 FAIL :")
    for e in errors:
        print(" -", e)
    sys.exit(1)
print("verify-746 PASS — structure OK, āyāt 25-27 présentes (rasm warš du cache), parallèles az-Zumar 53/al-Ǧumuʿa 2 présents, contenu complet, 0 rendu hors matière (6-24, 28-29), 0 rasm nu 18:6-27, 0 arabe résiduel (ﷺ exempté)")

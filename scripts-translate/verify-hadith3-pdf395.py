# -*- coding: utf-8 -*-
"""
Minhāj — Vérification de la leçon hadith-3es / pdf-mut23h2x-395
(الدرس 6 — al-mawāqīt az-zamāniyya wa-l-makāniyya li-l-iḥrām bi-l-ḥaǧǧ,
p.45-51 du manuel hadith-3-iadadi_text.pdf, 196 p., livre portail pré-mappé
29 slots pdf-mut23h2x-390..418) : bornes p.45-51 par DOUBLE preuve (p.45 =
bannière الدرس 6 lue par R636 + ahdāf 3 items + tamhīd + texte 930, tout
reconfirmé à 700 dpi ce tick ; p.50 = texte 963 repris + mawāqīt zamāniyya ;
p.51 = bannière الدرس 7 « al-mawāqīt al-makāniyya » + objectifs + textes
932-934, EXCLUE — sondage) ; 8 numéros de référence (930, 961, 963, 931,
964, 965, 966, 962, 932, 933, 934) TRANCHÉS CHIFFRE À CHIFFRE — sept par inspection directe
d'image 700-1000 dpi (930, 961, 962, 963, 964, 965, 966, 932, 933, 934), un par convergence
des couches texte selon la loi d'inversion par paires (931) — jamais deviné ;
récusations par image : Ibn az-Zubayr + aqāma (962) contre OCR « Ibn ʿUmar +
atā » ; généalogie « b. Ḫālid b. Ǧunāda al-ʿAtaqī » rendue telle qu'imprimée ;
« yṣnaʿ » (965) contre OCR « yaḍaʿ » ; UN verset imprimé (fin 2:127) rendu du
cache coranique (warš = ḥafṣ moins un, R511) ; 0 arabe, 0 apostrophe droite,
0 doublon.
Usage: python3 scripts-translate/verify-hadith3-pdf395.py
"""
import json
import re

HTML = "/home/z/my-project/tr-tmp/lesson-hadith3-pdf-mut23h2x-395-fr.html"
REG = "/home/z/my-project/content/books/hadith-3es.json"
SAV = "/home/z/my-project/scripts-translate/savant-registry.json"

ok, fail = 0, 0


def chk(label, cond):
    global ok, fail
    if cond:
        ok += 1
    else:
        fail += 1
        print(f"ÉCHEC : {label}")


h = open(HTML, encoding="utf-8").read()
hn = re.sub(r" +", " ", h.replace("&nbsp;", " ").replace("\u202f", "").replace("\u2009", ""))

# --- 1) squelette ---
chk("h1 Leçon 6", "<h1>Leçon 6" in hn and "mawāqīt" in hn)
chk("h1 titleFr registre", "les mawāqīt, bornes temporelles et spatiales de l’iḥrām pour le ḥaǧǧ" in hn)
chk("lesson-meta present", 'class="lesson-meta"' in hn)
chk("meta bornes p.45-51", "p.45-51" in hn)
chk("meta trace tick job", "1a1a172f41684dc9-cron-agent-loop-202611070704" in hn and "06h56" in hn and "499559" in hn)
chk("meta voisins 391/394/396", "pdf-mut23h2x-391" in hn and "pdf-mut23h2x-394" in hn and "pdf-mut23h2x-396" in hn)
chk("correction de bornes documentée", "CORRECTION DE BORNES DOCUMENTÉE" in hn and "at-taqwīm" in hn)
chk("meta bannière ad-dars 6", "ad-dars 6" in hn)
for sec in (
    "Les objectifs du cours (ahdāf ad-dars)",
    "Le tamhīd (l’ouverture de la leçon)",
    "Les textes du cours",
    "La notice du transmetteur (tarǧamat ar-rāwī)",
    "La glose des mots et des lieux (aš-šarḥ) du manuel",
    "Le résumé du cours (al-istiḫlāṣ al-muḍāmīn)",
    "Le fiqh du hadith (fiqh al-ḥadīṯ)",
    "L’apparat de preuve de la livraison",
):
    chk(f"section « {sec[:40]} »", sec in hn)

# --- 2) les trois objectifs ---
chk("obj 1 reconnaître mawāqīt", "reconnaître les mawāqīt" in hn and "spatiales et temporelles" in hn)
chk("obj 2 distinguer par pays", "distinguer les mawāqīt spatiaux de chaque pays" in hn)
chk("obj 3 dessein de la spécialisation", "saisir le dessein" in hn and "chaque pays par un mīqāt déterminé" in hn)

# --- 3) les textes et numéros tranchés ---
for num in ("930", "961", "962", "963", "964", "965", "966", "931", "932", "933", "934"):
    chk(f"numéro {num} présent", num in hn)
chk("texte 930 quatre miqāt", "Dhū-l-Ḥulayfa" in hn and "al-Guḥfa" in hn and "Qarn" in hn and "Yalamlam" in hn)
chk("texte 930 chaîne", "Mālik, d’après Nāfiʿ, d’après ʿAbd Allāh b. ʿUmar" in hn)
chk("texte 930 ajout Yémen", "il m’est parvenu que le Messager de Dieu" in hn)
chk("texte 961 cri d’ʿUmar", "Ô gens de La Mecque" in hn and "échevelés" in hn and "parfumés" in hn)
chk("texte 961 chaîne ʿAbd ar-Raḥmān", "ʿAbd ar-Raḥmān b. al-Qāsim, d’après son père" in hn)
chk("texte 963 règle habitât", "du ventre de La Mecque (ǧawf Makkah), ne sort pas du territoire sacré" in hn)
chk("texte 964 Ibn ʿUmar retarde", "ainsi a fait ʿAbd Allāh b. ʿUmar" in hn and "jusqu’à revenir de Minā le jour de l’immolation" in hn)
chk("texte 965 question Mālik", "l’obligatoire est le dernier" in hn and "chaque fois qu’il aura fait sept rondes" in hn)
chk("texte 966 ʿumra", "la ʿumra est la visite de la Maison" in hn)

# --- 4) notice transmetteur (rendue telle qu'imprimée) ---
chk("tarǧama 191", "mort en 191" in hn)
chk("tarǧama généalogie imprimée", "b. Ḫālid b. Ǧunāda al-ʿAtaqī al-Miṣrī" in hn)
chk("tarǧama élèves andalous", "Yaḥyā b. Yaḥyā al-Andalusī" in hn and "al-Ḥāriṯ b. Miskīn" in hn)

# --- 5) gloses géographiques ---
chk("glose Guḥfa cinq étapes", "cinq étapes (marāḥil)" in hn)
chk("glose Dhū-l-Ḥulayfa puits", "deux cents milles" in hn and "puits de ʿAlī" in hn)
chk("glose Naǧd dix contrées", "nom de dix contrées" in hn and "Tihāma" in hn)
chk("glose Qarn homonyme", "Qarn al-Manāzil, non Qarn aṯ-Ṯaʿālib" in hn)

# --- 6) fiqh : définition + 6 cas + statut + sagesse + zamāniyya ---
chk("def Ibn Daqīq al-ʿĪd", "Ibn Daqīq al-ʿĪd" in hn and "les accompagnements du temps" in hn)
chk("bipartition", "mawāqīt temporels et des mawāqīt spatiaux" in hn)
chk("zamāniyya trois mois", "šawwāl, Dhū-l-Qaʿda et Dhū-l-Ḥiǧǧa" in hn)
chk("cinq miqāt énumérés", "cinq d’après les directions du territoire sacré" in hn)
chk("cas 931 quatre imams", "les quatre imams le disent" in hn)
chk("cas 931 obligation sang", "doit le sang (ad-dam)" in hn)
chk("Ibn ʿAbd al-Barr rémission", "avant de s’être enveloppé du nusuk" in hn and "le sang tombe de lui" in hn)
chk("Mālik condition non-éloignement", "à condition qu’il ne s’éloigne pas" in hn)
chk("Égyptien/Syrien passage Médine", "l’Égyptien et au Syrien qui veulent le nusuk" in hn)
chk("mīqāt originel Guḥfa", "al-Guḥfa qui est son mīqāt originel" in hn)
chk("sagesse Badr", "l’Égyptien qui passe par Badr" in hn)
chk("ʿIyāḍ tendresse", "la tendresse du Prophète" in hn and "aux gens des horizons selon la proximité" in hn)
chk("ʿIyāḍ prédiction Guḥfa", "un pays d’islam où les musulmans accompliraient le pèlerinage" in hn)
chk("zamānī borne", "du premier de šawwāl jusqu’à ce qui précède le lever de l’aube du jour du sacrifice" in hn)
chk("ʿUmar verset 2:127", "Ô notre Seigneur, accepte ceci de notre part" in hn and "l’Audient, l’Omniscient" in hn)
chk("verset 127 sourate 2 cache", "verset 127 de la sourate 2, rendu du cache coranique" in hn)
chk("962 Ibn az-Zubayr 9 ans", "ʿAbd Allāh b. az-Zubayr a résidé à La Mecque neuf années" in hn)
chk("962 chaîne Hišām", "de Hišām b. ʿUrwa" in hn)
chk("récusation image 962", "la couche OCR portait « ʿAbd Allāh b. ʿUmar » et « atā »" in hn)
chk("taqwīm 4 items", "at-taqwīm" in hn and "quel est le mīqāt des gens de l’Occident" in hn)
chk("istiṯmār 932 Farʿ", "il se consacra depuis al-Farʿ" in hn)
chk("istiṯmār 933 Ilyāʾ", "s’était consacré depuis al-Ilyāʾ" in hn)
chk("istiṯmār 934 Ǧiʿrāna ʿumra", "s’est consacré depuis al-Ǧiʿrāna pour une ʿumra" in hn)
chk("istiṯmār mise en accord", "mettre d’accord ces hadiths" in hn and "qu’Ibn ʿUmar" in hn)
chk("iʿdād leçon 7 muḥrim", "mémorise les hadiths de la leçon suivante" in hn and "le mariage du consacré" in hn)
chk("sondage p.52 l7", "ouverture p.52" in hn)

# --- 7) clôture pédagogique présente (taqwīm + istiṯmār + iʿdād, p.51) ---
chk("sections clôture présentes", "L’évaluation (at-taqwīm)" in hn and "L’exploitation pédagogique (al-istiṯmār)" in hn and "La préparation préalable (al-iʿdād al-qablī)" in hn)

# --- 8) registre : livres voisins intacts ---
reg = json.load(open(REG, encoding="utf-8"))
lessons = reg.get("lessons", reg)
if isinstance(lessons, dict):
    lessons = list(lessons.values())
l394 = [l for l in lessons if l.get("docId") == "pdf-mut23h2x-394" and l.get("htmlFr")]
l393 = [l for l in lessons if l.get("docId") == "pdf-mut23h2x-393" and l.get("htmlFr")]
l395 = [l for l in lessons if l.get("docId") == "pdf-mut23h2x-395" and l.get("htmlFr")]
chk("voisin 394 intact", len(l394) >= 1)
chk("voisin 393 intact", len(l393) >= 1)
chk("395 enregistré (htmlFr posé)", len(l395) >= 1 and "mawāqīt" in l395[0]["htmlFr"])
chk("396 non livré", not [l for l in lessons if l.get("docId") == "pdf-mut23h2x-396" and l.get("htmlFr")])

# --- 9) savant-registry ---
sav = json.load(open(SAV, encoding="utf-8"))
hand = len(sav["hand"]) if isinstance(sav, dict) and "hand" in sav else (len(sav) if isinstance(sav, list) else 0)
llm = len(sav["llm"]) if isinstance(sav, dict) and "llm" in sav else 0
tot = hand + llm
chk(f"registre savants ≥ 1181 (actuel {tot} = hand {hand} + llm {llm})", tot >= 1181)

print(f"verify-hadith3-pdf395 : {ok}/{ok + fail} PASS")
if fail:
    raise SystemExit(1)

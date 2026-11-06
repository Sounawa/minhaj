#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Minhāj — Vérification de la leçon hadith-3es / pdf-mut23h2x-391
(الدرس 2 — libās al-muḥrim, p.17-24 du manuel hadith-3-iadadi_text.pdf,
196 p., livre portail pré-mappé 29 slots pdf-mut23h2x-390..418) :
bornes p.17-24 par recoupement des livraisons voisines (leçon 1 = p.10-16
avec p.17 = bannière الدرس 2 ; leçon 3 = p.25-30 avec p.25 = bannière
الدرس 3) + bannière lue sur image (chiffre 2 dans le disque) + annonce de
la leçon 2 dans l'iʿdād de la leçon 1 ; 13 numéros de référence (909, 910,
911, 912, 913, 915, 916, 917, 918, 919, 920, 921, 922) TRANCHÉS CHIFFRE
À CHIFFRE sur zooms 900 dpi (passes r631/r633) ou portés tels quels par la
couche brute (910, 916, 917, 920, 922) — une lecture image initiale du
910 avait lu « 916 » par confusion 0/6, récusée par la couche et la série ;
le n° 914 relève de la leçon 3 déjà livrée ; zéro renvoi coranique imprimé
(cache coranique NON sollicité) ; textes 909/915/918 + reprises et appuis
910-913, 916-922 ; zones dégradées déclarées (verbe central de Fāṭima bint
al-Mundir non restituable, parallèle canonique NON substitué) ; takeover du
claim r633 périmé documenté ; 0 arabe, 0 apostrophe droite, 0 doublon.
Usage: python3 scripts-translate/verify-hadith3-pdf391.py
"""
import json
import re

HTML = "/home/z/my-project/tr-tmp/lesson-hadith3-pdf-mut23h2x-391-fr.html"
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
chk("h1 Leçon 2", "<h1>Leçon 2" in hn and "iḥrām" in hn)
chk("h1 titleFr registre", "Le vêtement du pèlerin en état d’iḥrām" in hn)
chk("lesson-meta present", 'class="lesson-meta"' in hn)
chk("meta bornes p.17-24", "p.17-24" in hn)
chk("meta trace tick job", "1a1a172f41684dc9-cron-agent-loop-202611070434" in hn and "04h34" in hn and "499558" in hn)
chk("meta voisins 390/392/393/394", all(x in hn for x in ("pdf-mut23h2x-390", "pdf-mut23h2x-392", "pdf-mut23h2x-393", "pdf-mut23h2x-394")))
chk("meta bannière", "ad-dars 2" in hn and "libās al-muḥrim" in hn)
for sec in (
    "Les objectifs du cours (ahdāf ad-dars)",
    "Le tamhīd (l’ouverture de la leçon)",
    "Les textes du cours",
    "La glose des mots (aš-šarḥ al-luġawī) du manuel",
    "Le fiqh du hadith (fiqh al-ḥadīṯ)",
    "Les subtilités de la leçon et l’apparat de preuve",
    "L’évaluation (at-taqwīm) de la leçon",
    "L’exploitation pédagogique (al-istiṯmār)",
    "La préparation préalable (al-iʿdād al-qablī) de la leçon suivante",
):
    chk(f"section « {sec[:40]} »", sec in hn)

# --- 2) bornes et voisins ---
chk("bannière libās al-muḥrim mentionnée", "libās al-muḥrim" in hn)
chk("annonce iʿdād leçon 1 citée", "annonce de la leçon dans l’iʿdād de la leçon 1" in hn)
chk("source PDF nommée", "hadith-3-iadadi_text.pdf" in hn)
chk("leçon 3 parfum annoncée", "parfum" in hn and "taṭyīb" in hn)

# --- 3) textes et numéros tranchés ---
for n in ("909", "910", "911", "912", "913", "915", "916", "917", "918", "919", "920", "921", "922"):
    chk(f"numéro de référence {n} présent", f"n° {n}" in hn)
chk("13 numéros revendiqués", "treize numéros" in hn)
chk("miroir 910/916 documenté (confusion 0/6)", "confusion 0/6" in hn and "916" in hn)
chk("914 attribué à la leçon 3", "914" in hn and "leçon 3 déjà livrée" in hn)
chk("texte 909 (question de l’homme, cinq interdits)", "un homme demanda au Messager de Dieu" in hn and "ne portez pas la chemise" in hn)
chk("909 exception bottines coupées", "sauf celui qui ne trouve pas de sandales" in hn and "en dessous des chevilles" in hn)
chk("909 safran et wars", "rien qu’ait touché le safran ou le wars" in hn)
chk("texte 915 (ceinture réprouvée)", "réprouvait le port de la ceinture" in hn)
chk("texte 918 (menton)", "au-dessus du menton" in hn)
chk("notice Ibn ʿUmar renvoi", "sa notice a déjà été donnée" in hn)
chk("texte 910 (Mālik n’a pas entendu, izār)", "qu’il porte un pantalon" in hn and "je n’ai pas entendu cela" in hn)
chk("910 chaîne Buḫārī/Muslim/Ǧābir b. Zayd", "al-Buḫārī, Muslim et d’autres, par la voie de Ǧābir b. Zayd" in hn)
chk("910 fiḍya Mālik/Abū Ḥanīfa", "offrande expiatoire (fiḍya) est alors due selon Mālik et Abū Ḥanīfa" in hn)
chk("texte 911 (teint safran/wars)", "teint au safran ou au wars" in hn)
chk("911 Ibn al-ʿArabī", "Ibn al-ʿArabī" in hn and "le wars n’est pas un parfum" in hn)
chk("911 règle étendue aux femmes", "s’étend aux femmes" in hn)
chk("texte 912 (ʿUmar/Ṭalḥa)", "Ṭalḥa b. ʿUbayd Allāh" in hn and "ô commandeur des croyants" in hn)
chk("912 tuiles d’imitation (groupe d’imams)", "groupe d’imams" in hn and "les gens vous prennent pour modèles" in hn)
chk("texte 913 (Asmāʾ garance)", "Asmāʾ bint Abī Bakr" in hn and "garance" in hn)
chk("913 Ibn Ḥabīb (effritement)", "Ibn Ḥabīb" in hn and "ne s’effrite pas" in hn)
chk("texte 916 (Saʿīd b. al-Musayyab, lanières)", "Saʿīd b. al-Musayyab" in hn and "lanières (siyūr)" in hn)
chk("916 Mālik (le mieux aimé entendu)", "ce que j’ai le mieux aimé entendre" in hn)
chk("916 Ibn ʿAbd al-Barr", "Ibn ʿAbd al-Barr" in hn and "jurisconsultes des capitales" in hn)
chk("texte 917 (al-Farrāfaṣa/ʿUthmān)", "al-Farrāfaṣa b. ʿAmīr al-Ḥanafī" in hn and "ʿUthmān b. ʿAffān" in hn)
chk("917 tête par unanimité", "il n’est pas permis de la couvrir, par unanimité" in hn)
chk("texte 919 (Wāqid, al-Ǧuḥfa)", "Wāqid b. ʿAbd Allāh" in hn and "al-Ǧuḥfa" in hn)
chk("919 parfum conditionnel", "si nous n’étions pas en sacralisation, nous l’aurions parfumé" in hn)
chk("texte 920 (l’œuvre s’achève)", "l’homme n’œuvre que tant qu’il vit" in hn)
chk("ṣiḥḥayn (chamelle, labbayk)", "la chamelle d’un homme en état de sacralisation le renversa" in hn and "disant labbayk" in hn)
chk("ʿilla « inna » cas particulier", "expressions qui marquent la cause" in hn and "cas particulier" in hn)
chk("texte 921 (niqāb/gants)", "que la femme en état de sacralisation ne se voile pas le visage" in hn and "les gants (qifāzayn)" in hn)
chk("texte 922 (Fāṭima bint al-Mundir)", "Fāṭima bint al-Mundir" in hn and "aṣ-Ṣiddīq" in hn)

# --- 4) fiqh trois chapitres ---
chk("chapitre 1 (vêtements interdits)", "les sortes de vêtements interdits" in hn)
chk("chapitre 2 (teints et parfumés)", "vêtements teints et parfumés" in hn)
chk("chapitre 3 (ceinture et visage)", "le port de la ceinture et la couverture du visage" in hn)
chk("riwāya at-Tunīsī rafʿ/ǧazm", "at-Tunīsī" in hn and "rafʿ" in hn and "ǧazm" in hn)
chk("al-Ḫaṭṭābī (panier maktal)", "al-Ḫaṭṭābī" in hn and "panier (maktal)" in hn)
chk("Ḥāfiẟ Ibn Ḥaǧar (immersion)", "Ibn Ḥaǧar" in hn and "l’immersion dans l’eau" in hn)
chk("iǧmāʿ restriction à l’homme (Ibn al-Mundir)", "restreindre l’interdiction à l’homme" in hn and "Ibn al-Mundir" in hn)
chk("ḫifāf/ǧawrab/rukhsa/ǧumhūr", "chaussette (ǧawrab)" in hn and "dispense (rukhsa)" in hn and "majorité (ǧumhūr)" in hn)
chk("mashhūr visage + fiḍya", "mashhūr" in hn and "offrande expiatoire" in hn)
chk("conclusion (égalité des lignées)", "l’égalité entre les gens" in hn)

# --- 5) glosses ---
chk("gloss ʿamāʾim", "ʿamāʾim" in hn and "enveloppe" in hn)
chk("gloss sarāwīlāt (nūn/šīn consigné)", "sarāwīlāt" in hn and "avec le nūn et avec le šīn" in hn)
chk("gloss barānīs", "barānīs" in hn and "burnus" in hn)
chk("gloss wars", "plante jaune" in hn)
chk("gloss mintaqa", "mintaqa" in hn and "kasra" in hn)

# --- 6) honnêteté d'apparat ---
for lab in (
    "non restituable",
    "lectures",
    "consignées",
    "conjecture",
    "429",
):
    chk(f"mention d’apparat « {lab} »", lab in hn)
chk("takeover claim r633 documenté", "r633" in hn and "takeover" in hn)
chk("verbe Fāṭima déclaré + parallèle non substitué", "parallèle canonique du Muwaṭṭaʾ" in hn)
chk("zéro āya imprimée (cache non sollicité)", "cache coranique du corpus n’a pas été sollicité" in hn)

# --- 7) hygiene ---
chk("0 apostrophe droite", "'" not in h)
chk("guillemets appariés", h.count("«") == h.count("»"))
chk("0 arabe", not re.search(r"[\u0600-\u06FF]", h))
chk("h1 unique", h.count("<h1>") == 1)
chk("pas de balise orpheline", "<h2></h2>" not in h and "<h3></h3>" not in h)

# --- 8) registre (avant hand-set : 391 doit être vide, voisins intacts) ---
reg = json.load(open(REG, encoding="utf-8"))
lessons = reg if isinstance(reg, list) else reg.get("lessons", reg.get("items", []))
chk("registre 29 leçons", len(lessons) == 29)
e391 = lessons[1]
chk("391 = vêtement du pèlerin", "vêtement du pèlerin" in e391.get("titleFr", "").replace("'", "’"))
chk("390 htmlFr intact (>30 000 car)", len(lessons[0].get("htmlFr") or "") > 30000)
chk("392 htmlFr intact (>30 000 car)", len(lessons[2].get("htmlFr") or "") > 30000)
chk("393 htmlFr intact (>30 000 car)", len(lessons[3].get("htmlFr") or "") > 30000)
chk("391 htmlFr vide (avant hand-set)", not e391.get("htmlFr"))
chk("394 htmlFr livré par voie parallèle (>25 000 car)", len(lessons[4].get("htmlFr") or "") > 25000)

# --- 9) registre savants (nb courant avant hand-set) ---
sav = json.load(open(SAV, encoding="utf-8"))
n_sav = len(sav["hand"]) + len(sav.get("llm", {}))
chk("registre savants ≥ 1179", n_sav >= 1179)
print(f"registre savants : {n_sav}")

print(f"\nverify-hadith3-pdf391 : {ok} PASS / {fail} ÉCHEC")
if fail:
    raise SystemExit(1)

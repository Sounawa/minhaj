# -*- coding: utf-8 -*-
"""
Minhāj — Vérification de la leçon hadith-3es / pdf-mut23h2x-394
(الدرس 5 — aḥkām al-ihlāl bi-t-talbiya, p.39-44 du manuel
hadith-3-iadadi_text.pdf, 196 p., livre portail pré-mappé 29 slots
pdf-mut23h2x-390..418) : bornes p.39-44 par DOUBLE preuve (p.39 = bannière
الدرس 5 600 dpi + ahdāf 3 items + tamhīd ; p.44 = istiṯmār 958 + iʿdād
annonçant les mawāqīt ; p.45 = bannière الدرس 6 « mawāqīt al-iḥrām »,
EXCLUE — inspection directe) ; 10 numéros de référence (935, 936, 941, 939,
940, 943, 944, 955, 956, 958) TRANCHÉS CHIFFRE À CHIFFRE — six par
inspection directe d'image (936, 939, 940, 943, 955, 956), quatre par
convergence des couches texte (935, 941, 944, 958) — l'API VLM étant en 429
ce tick, méthode adaptée : couches recoupées + 9 inspections directes ;
940 reconstruit par image (ʿAbd al-Malik b. Marwān + ʿAbbān b. ʿUthmān) ;
« nasiya » tranché contre OCR « sanna » ; « yulabbī » tranché contre
« yabītu » ; zéro renvoi coranique (cache NON sollicité) ; 0 arabe,
0 apostrophe droite, 0 doublon.
Usage: python3 scripts-translate/verify-hadith3-pdf394.py
"""
import json
import re

HTML = "/home/z/my-project/tr-tmp/lesson-hadith3-pdf-mut23h2x-394-fr.html"
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
chk("h1 Leçon 5", "<h1>Leçon 5" in hn and "talbiya" in hn)
chk("h1 titleFr registre", "Les règles de la talbiya à l’entrée en consécration" in hn)
chk("lesson-meta present", 'class="lesson-meta"' in hn)
chk("meta bornes p.39-44", "p.39-44" in hn)
chk("meta trace tick job", "1a1a172f41684dc9-cron-agent-loop-202611070619" in hn and "06h19" in hn and "499558" in hn)
chk("meta voisins 391/393/395", "pdf-mut23h2x-391" in hn and "pdf-mut23h2x-393" in hn and "pdf-mut23h2x-395" in hn)
chk("meta bannière 600 dpi", "ad-dars 5" in hn and "600 dpi" in hn)
for sec in (
    "Les objectifs du cours (ahdāf ad-dars)",
    "Le tamhīd (l’ouverture de la leçon)",
    "Les textes du cours",
    "La glose des mots (aš-šarḥ al-luġawī) du manuel",
    "Le fiqh du hadith (fiqh al-ḥadīṯ)",
    "L’évaluation (at-taqwīm) de la leçon",
    "L’exploitation pédagogique (al-istiṯmār)",
    "La préparation préalable (al-iʿdād al-qablī) de la leçon suivante",
    "Les subtilités de la leçon et l’apparat de preuve",
):
    chk(f"section « {sec[:40]} »", sec in hn)

# --- 2) bornes et voisins ---
chk("bannière leçon 5 mentionnée", "aḥkām al-ihlāl bi-t-talbiya" in hn)
chk("p.45 bannière leçon 6 exclue", "mawāqīt al-iḥrām" in hn and "EXCLUE" in hn.upper())
chk("source PDF nommée", "hadith-3-iadadi_text.pdf" in hn)

# --- 3) textes et numéros tranchés ---
for n in ("935", "936", "941", "939", "940", "943", "944", "955", "956", "958"):
    chk(f"numéro de référence {n} présent", f"n° {n}" in hn)
chk("talbiya intégrale 935", "Labbayka Allāhumma labbayk" in hn and "inna l-ḥamda wa-n-niʿmata laka wa-l-mulk" in hn)
chk("prolongation Ibn ʿUmar", "wa-s-saʿdayka" in hn and "wa-r-raġbāʾu ilayka wa-l-ʿamal" in hn)
chk("936 Dhū-l-Ḥulayfa", "Dhū-l-Ḥulayfa" in hn and "quand sa monture" in hn)
chk("941 Jibrīl", "Jibrīl" in hn and "yurīd aḥadahumā" in hn)
chk("939 Ibn ʿUmar pratique", "il se consacrait" in hn)
chk("940 reconstruit (ʿAbd al-Malik + ʿAbbān)", "ʿAbd al-Malik b. Marwān" in hn and "ʿAbbān b. ʿUthmān" in hn and "ašāra ʿalayhi bi-dālika" in hn)
chk("943 règle des mosquées", "masāǧid al-ǧamāʿāt" in hn and "Mosque Sacré" in hn and "mosque de Minā" in hn)
chk("944 après chaque prière", "après chaque prière" in hn and "chaque hauteur du terrain" in hn)
chk("955 ʿAlī", "ʿAlī b. Abī Ṭālib faisait la talbiya" in hn and "le soleil dévie du jour d’ʿArafa" in hn)
chk("956 ʿĀʾiša mauqif", "lieu de stationnement (al-mawqif)" in hn)
chk("958 ṭawāf", "ne faisait pas la talbiya tandis qu’il faisait le ṭawāf de la Maison" in hn)

# --- 4) fiqh deux chapitres ---
chk("chapitre 1 l’acte par l’iḥlāl", "l’acte par l’iḥlāl (al-ʿamal bi-l-iḥlāl)" in hn)
chk("chapitre 2 les règles de la talbiya", "les règles de la talbiya (aḥkām at-talbiya)" in hn)
chk("Sībawayh + duel", "Sībawayh" in hn and "duel" in hn)
chk("Mālik : le sang / Abū Ḥanīfa : suffit", "rendu obligatoire le sang (ad-dam)" in hn and "ce qui tient la place de son sens suffit" in hn)
chk("élévation de la voix rubrique 3", "Le statut d’élever la voix par l’iḥlāl" in hn)
chk("šiʿār + enseignement de l’ignorant", "signe distinctif (šiʿār)" in hn and "l’enseignement pour l’ignorant" in hn)
chk("occasions recommandées (944)", "en se levant, en s’asseyant" in hn)

# --- 5) commentaires ---
chk("az-Zayn b. an-Nuʿaym (Zarqānī)", "az-Zayn b. an-Nuʿaym" in hn and "la louange est rattachée à la grâce" in hn)
chk("ʿIyāḍ (saʿdayka)", "j’ai rendu ton obéissance félicitée" in hn)
chk("tarǧama ʿUrwa (7 fuqahāʾ)", "sept fuqahāʾ de Médine" in hn and "Ibn ʿUyayna" in hn and "al-Qāsim" in hn)
chk("gloss talbiya (masdar labbā)", "masdar de labbā" in hn)
chk("gloss niʿma (kasra/fatḥa)", "à la kasra du nūn" in hn and "l’habit du tannūm" in hn)

# --- 6) honnêteté d'apparat ---
for lab in ("inspection directe", "non", "429", "tranchés chiffre à chiffre"):
    chk(f"mention d'apparat « {lab} »", lab in hn)
chk("940 reconstruit documenté", "les deux couches texte le portaient corrompu" in hn)
chk("nasiya tranché documenté", "nasiya" in hn and "sanna" in hn)
chk("yulabbī tranché documenté", "yabītu" in hn)
chk("intitulé dégradé documenté", "imprimé en partie dégradé" in hn)
chk("zéro āya (cache non sollicité)", "n’a pas été sollicité" in hn)

# --- 7) hygiene ---
chk("0 apostrophe droite", "'" not in h)
chk("guillemets appariés", h.count("«") == h.count("»"))
chk("0 arabe", not re.search(r"[\u0600-\u06FF]", h))
chk("h1 unique", h.count("<h1>") == 1)
chk("pas de balise vide", "<h2></h2>" not in h and "<h3></h3>" not in h)

# --- 8) registre (394 libre avant hand-set, voisins intacts) ---
reg = json.load(open(REG, encoding="utf-8"))
lessons = reg if isinstance(reg, list) else reg.get("lessons", reg.get("items", []))
chk("registre 29 leçons", len(lessons) == 29)
e394 = lessons[4]
chk("394 = talbiya", "talbiya" in e394.get("titleFr", "").lower())
chk("393 htmlFr intact (>30 000 car)", len(lessons[3].get("htmlFr") or "") > 30000)
chk("391 htmlFr vide", not lessons[1].get("htmlFr"))
chk("395 htmlFr vide", not lessons[5].get("htmlFr"))

# --- 9) registre savants ---
sav = json.load(open(SAV, encoding="utf-8"))
n_sav = len(sav["hand"]) + len(sav.get("llm", {}))
chk("registre savants ≥ 1180", n_sav >= 1180)
print(f"registre savants : {n_sav}")

print(f"\nverify-hadith3-pdf394 : {ok} PASS / {fail} ÉCHEC")
if fail:
    raise SystemExit(1)

# -*- coding: utf-8 -*-
"""
Minhāj — Vérification de la leçon hadith-3es / pdf-mut23h2x-393
(الدرس 4 — anwāʿ al-iḥrām, p.31-38 du manuel hadith-3-iadadi_text.pdf,
196 p., livre portail pré-mappé 29 slots pdf-mut23h2x-390..418) :
bornes p.31-38 par DOUBLE preuve (p.31 = bannière الدرس 4 « anwāʿ al-iḥrām »
600 dpi + ahdāf 3 items + tamhīd ; p.38 = taqwīm + istiṯmār 984 + iʿdād
annonçant la talbiya ; p.39 = bannière de la leçon 5 aḥkām al-ihlāl bi-t-talbiya,
EXCLUE) ; 12 numéros de référence (945, 949, 986, 1282, 946, 980, 953, 950,
952, 948, 980, 984) TRANCHÉS CHIFFRE À CHIFFRE sur recadrages 900 dpi (piles
p.31-p.38, un recadrage inspecté directement) — la couche logique portait 549
pour le premier texte (miroir de 945), démasqué puis récusé par l'image ;
correction miroir R625 (annonce iʿdād « 549 ») documentée ; zéro renvoi
coranique imprimé (cache coranique NON sollicité — l'āya de l'accomplissement
est RENVOYÉE, pas citée) ; textes 945/949/986/1282/980 + reprises 946/953/950/
952/948/984 ; 0 arabe, 0 apostrophe droite, 0 doublon.
Usage: python3 scripts-translate/verify-hadith3-pdf393.py
"""
import json
import re

HTML = "/home/z/my-project/tr-tmp/lesson-hadith3-pdf-mut23h2x-393-fr.html"
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
chk("h1 Leçon 4", "<h1>Leçon 4" in hn and "iḥrām" in hn)
chk("h1 titleFr registre", "Les formes de l’iḥrām" in hn)
chk("lesson-meta present", 'class="lesson-meta"' in hn)
chk("meta bornes p.31-38", "p.31-38" in hn)
chk("meta trace tick job", "1a1a172f41684dc9-cron-agent-loop-202611070434" in hn and "04h34" in hn and "499558" in hn)
chk("meta voisins 391/392/394", "pdf-mut23h2x-391" in hn and "pdf-mut23h2x-392" in hn and "pdf-mut23h2x-394" in hn)
chk("meta bannière 600 dpi", "ad-dars 4" in hn and "600 dpi" in hn)
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
chk("bannière leçon 4 mentionnée", "anwāʿ al-iḥrām" in hn)
chk("p.39 bannière leçon 5 exclue", "aḥkām al-ihlāl bi-t-talbiya" in hn and "EXCLUE" in hn.upper())
chk("source PDF nommée", "hadith-3-iadadi_text.pdf" in hn)

# --- 3) textes et numéros tranchés ---
for n in ("945", "949", "986", "1282", "946", "980", "953", "950", "952", "948", "984"):
    chk(f"numéro de référence {n} présent", f"n° {n}" in hn)
chk("945 tranché miroir 549", "miroir de « 945 »" in hn and "549" in hn)
chk("Buḫārī 946 cité comme Ṣaḥīḥ", "aṣ-Ṣaḥīḥ (du Buḫārī)" in hn)
chk("texte ʿĀʾiša 945 (pèlerinage d’adieu)", "pèlerinage d’adieu" in hn and "se consacra pour le ḥaǧǧ" in hn)
chk("texte ʿAlī/ʿUthmān 949", "al-Miqdād b. al-Aswad" in hn and "as-Suqyā" in hn and "Labbayka" in hn)
chk("texte 986 (šawwāl/qaʿda/ḥiǧǧa)", "šawwāl" in hn and "dū-l-qaʿda" in hn and "dū-l-ḥiǧǧa" in hn)
chk("texte 1282 (jeûne/ʿArafa)", "jour de ʿArafa" in hn)
chk("non restituable 1282 déclaré", "non restituable" in hn)
chk("texte 980 (Saʿd/aḍ-Ḍaḥḥāk)", "Saʿd b. Abī Waqqāṣ" in hn and "aḍ-Ḍaḥḥāk b. Qays" in hn and "fils de mon frère" in hn)
chk("féminin imprimé ṣanaʿahā documenté", "ṣanaʿahā… wa-ṣanaʿnāhā" in hn)
chk("aš-šayḫān + Muslim", "deux cheikhs" in hn and "Abū Mūsā" in hn)
chk("953 (bête d’offrande)", "celui qui a avec lui une bête d’offrande" in hn)
chk("950 (al-amr ʿindanā)", "le statut (al-amr) chez nous" in hn and "à Minā le jour du sacrifice" in hn)
chk("952 (Ibn ʿUmar, témoignage)", "soyez témoins que j’ai rendu obligatoire le ḥaǧǧ avec la ʿumra" in hn)
chk("fal-yatak rendu « qu’il attende »", "qu’il attende" in hn)
chk("948 (entrée ʿumra dans ḥaǧǧ désapprouvée)", "les gens de science de notre pays" in hn)
chk("984 (étranger séjournant à La Mecque)", "pas semblable aux gens de La Mecque" in hn)

# --- 4) fiqh trois chapitres ---
chk("chapitre ifrād", "l’iḥrām individuel (al-ifrād)" in hn)
chk("chapitre qirān", "le qirān (l’association du ḥaǧǧ et de la ʿumra)" in hn)
chk("chapitre tamattuʿ", "le tamattuʿ par la ʿumra" in hn)
chk("préférence ifrād (Jābir/Ibn ʿUmar/Ibn ʿAbbās/ʿĀʾiša)", "Jābir" in hn and "bride de la chamelle" in hn and "califes bien guidés" in hn)
chk("faskh du ḥaǧǧ vers la ʿumra (Ibn ʿAbd al-Barr)", "Ibn ʿAbd al-Barr" in hn and "la rupture (faskh) du ḥaǧǧ vers la ʿumra" in hn)
chk("lā iǧtihād maʿa an-naṣṣ", "pas d’ijtihād avec le texte" in hn)
chk("wuqūf/ramy/mabīt", "le stationnement (al-wuqūf)" in hn and "ar-ramy" in hn and "al-mabīt" in hn)

# --- 5) glosses ---
chk("gloss yaḥullūna", "yaḥullūna" in hn and "sorti de l’iḥrām" in hn)
chk("gloss as-Suqyā", "village-gathering sur la route de La Mecque" in hn)
chk("gloss yanǧaʿu bukarāt", "bukarāt" in hn and "chamelle encore jeune" in hn)
chk("gloss ḫubṭan dégradée déclarée", "ḫubṭ" in hn and "provende" in hn)

# --- 6) honnêteté d'apparat ---
for lab in (
    "non restituable",
    "lectures",
    "consignées",
    "jamais devinée",
):
    chk(f"mention d'apparat « {lab} »", lab in hn)
chk("takeover r626b documenté", "r626b" in hn and "20h47 UTC" in hn)
chk("zéro āya imprimée (cache non sollicité)", "cache coranique du corpus n’a pas été sollicité" in hn)

# --- 7) hygiene ---
chk("0 apostrophe droite", "'" not in h)
chk("guillemets appariés", h.count("«") == h.count("»"))
chk("0 arabe", not re.search(r"[\u0600-\u06FF]", h))
chk("h1 unique", h.count("<h1>") == 1)
chk("pas de balise orpheline <h2></h2>", "<h2></h2>" not in h and "<h3></h3>" not in h)

# --- 8) registre (avant hand-set : 393 doit être vide, voisins intacts) ---
reg = json.load(open(REG, encoding="utf-8"))
lessons = reg if isinstance(reg, list) else reg.get("lessons", reg.get("items", []))
chk("registre 29 leçons", len(lessons) == 29)
e393 = lessons[3]
chk("393 = formes de l'iḥrām", "formes de l’iḥrām" in e393.get("titleFr", "").replace("'", "’"))
chk("392 htmlFr intact (>30 000 car)", len(lessons[2].get("htmlFr") or "") > 30000)
chk("391 htmlFr vide", not lessons[1].get("htmlFr"))
chk("394 htmlFr vide", not lessons[4].get("htmlFr"))

# --- 9) registre savants (nb courant avant hand-set) ---
sav = json.load(open(SAV, encoding="utf-8"))
n_sav = len(sav["hand"]) + len(sav.get("llm", {}))
chk("registre savants ≥ 1178", n_sav >= 1178)
print(f"registre savants : {n_sav}")

print(f"\nverify-hadith3-pdf393 : {ok} PASS / {fail} ÉCHEC")
if fail:
    raise SystemExit(1)

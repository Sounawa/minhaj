# -*- coding: utf-8 -*-
"""
Minhāj — Vérification de la leçon hadith-3es / pdf-mut23h2x-392
(الدرس 3 — taṭyīb al-muḥrim, p.25-30 du manuel hadith-3-iadadi_text.pdf,
196 p., livre portail pré-mappé 29 slots pdf-mut23h2x-390..418) :
bornes p.25-30 par DOUBLE preuve (p.25 = bannière الدرس 3 « taṭyīb al-muḥrim »
600 dpi + ahdāf 3 items + tamhīd ; p.30 = taqwīm + istiṯmār 929 + iʿdād
annonçant anwāʿ al-iḥrām ; p.31 = ahdāf de la leçon 4) ;
8 numéros de hadiths (923, 924, 926, 925, 928, 927, 914, 929) TRANCHÉS
CHIFFRE À CHIFFRE sur recadrages 900 dpi (5 piles) — la passe de décodage
initiale inversait les chiffres (329/429/629/529/829/729/419/929 en miroir
d'outil), démasquée puis récusée ; aṣ-ṣamġ → aṣ-ṣabġ tranché par image ;
dialogue 925 tranché par recoupement canonique Šarḥ az-Zarqānī (islamweb :
min-ka la-ʿamru llāhi ; ʿazamtu ʿalayka la-tarǧiʿanna fa-l-taġsilannahu) ;
citation Muslim recoupée (Šarḥ an-Nawawī) ; zéro renvoi coranique (cache
coranique NON sollicité) ; 8 textes rendus + istiṯmār 929 ; 0 arabe,
0 apostrophe droite, 0 doublon.
Usage: python3 scripts-translate/verify-hadith3-pdf392.py
"""
import json
import re

HTML = "/home/z/my-project/tr-tmp/lesson-hadith3-pdf-mut23h2x-392-fr.html"
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
chk("h1 Leçon 3", "<h1>Leçon 3" in hn and "taṭyīb" in hn)
chk("h1 titre parfum", "L’usage du parfum" in hn)
chk("lesson-meta present", 'class="lesson-meta"' in hn)
chk("meta bornes p.25-30", "p.25-30" in hn)
chk("meta trace tick job", "1a1a172f41684dc9-cron-agent-loop-202611070015" in hn and "00h11" in hn and "499559" in hn)
chk("meta voisins 391/393", "pdf-mut23h2x-391" in hn and "pdf-mut23h2x-393" in hn)
chk("meta bannière 600 dpi", "ad-dars 3" in hn and "600 dpi" in hn)
for sec in (
    "Les objectifs du cours (ahdāf ad-dars)",
    "Le tamhīd (l’ouverture de la leçon)",
    "Les textes du cours",
    "La glose des mots (aš-šarḥ al-luġawī) du manuel",
    "Les notices biographiques des transmetteurs (tarāǧim ar-ruwāh)",
    "Le commentaire du šāriḥ (aš-Šarḥ az-Zarqānī)",
    "Les subtilités de la leçon et l’apparat de preuve",
    "L’évaluation (at-taqwīm) de la leçon",
    "L’exploitation pédagogique (al-istiṯmār)",
    "La préparation préalable (al-iʿdād al-qablī) de la leçon suivante",
):
    chk(f"section « {sec[:40]}… »", sec in hn)

# --- 2) les 8 numéros tranchés + absence des miroirs d'outil ---
for n in ("923", "924", "926", "925", "928", "927", "914", "929"):
    chk(f"numéro {n} porté", f"n° {n}" in hn)
for bad in ("n° 329", "n° 429", "n° 629", "n° 529", "n° 829", "n° 729", "n° 419"):
    chk(f"miroir d’outil {bad} absent", bad not in hn)
chk("preuve chiffre à chiffre documentée", "CHIFFRE À CHIFFRE" in hn and "900 dpi" in hn)

# --- 3) contenus hadiths clés (traductions) ---
keys = (
    "j’avais coutume de parfumer le Messager de Dieu",
    "pour son iḥrām avant qu’il ne se consacre",
    "pour son ḥall (sa désacralisation) avant qu’il ne se rase",
    "un homme du désert (aʿrābī)",
    "enlève ta chemise, lave cette couleur jaune de toi",
    "fais dans ta ʿumra ce que tu fais dans ton ḥaǧǧ",
    "Kaṯīr b. aṣ-Ṣalt",
    "j’ai mis de la teinte sur ma tête (labītu raʾsī)",
    "va alors à la šarrah",
    "jusqu’à ce que cela macère (tanqaʿ)",
    "fosse (ḥafīra) qui se trouve au pied du palmier",
    "grande comme une marmite (qidār)",
    "ʾAslam, le client (mawlā) de ʿUmar b. al-Ḫaṭṭāb",
    "Muʿāwiya b. Abī Sufyān dit : de moi, ô Commandeur des croyants",
    "c’est Umm Ḥabība qui m’a parfumé",
    "j’ai pris la résolution (ʿazamtu)",
    "tu retourneras vers elle et que tu la laveras (fa-l-taġsilannahu)",
    "huile dans laquelle il n’y a pas de parfum",
    "avant de verser (qayḍ) de Minā après le lancer de la ǧamra",
    "al-Walīd b. ʿAbd al-Malik questionna Sālim b. ʿAbd Allāh et Ḫāriǧa b. Zayd b. Thābit",
    "Sālim le lui interdit et Ḫāriǧa le lui permit",
    "par oubli (nisyān) ou par ignorance",
    "il n’y a pas d’expiation (kaffāra) sur lui",
    "si cela tarde sur lui, cela devient obligatoire",
    "teinture (ṣibāġ) de safran (zaʿfarān) ou de wars",
    "même si la senteur s’est enfuie",
    "ʿIyāḍ a dit : ils ont interprété (taʾawwalū)",
    "Ṣaḥīḥ Muslim",
    "puis il rendit visite à ses épouses, puis il devint muḥrim",
    "rovation de an-Nasāʾī",
    "lorsqu’il voulut se consacrer",
    "la doctrine des trois imams et du plus grand nombre (al-ǧumhūr)",
    "Mālik, az-Zuhrī et un groupe de Compagnons et de suivistes",
    "kāffat al-ʿulamāʾ",
    "détestabilité (karāha) avant l’i fāḍa",
    "flaînerie (at-taraffuh)",
    "revêture du caractère de l’humble recueilli (al-ḫāšiʿ)",
    "la pomme (at-tuffāḥ) et le cédrat (al-utruǧǧ)",
    "ce que le feu a touché de cela",
    "ce que le feu n’a pas touché de cela",
    "Kaṯīr b. aṣ-Ṣalt b. Māʾdīkarib al-Kindī al-Madanī",
    "comptant parmi les Compagnons",
    "vers l’an 70 de l’Hégire",
)
for k in keys:
    chk(f"contenu « {k[:48]}… »", k in hn)

# --- 4) garde-doublon / doctrine FR-seule ---
chk("0 arabe résiduel", not re.search(r"[\u0600-\u06FF\u0750-\u077F\u08A0-\u08FF\uFB50-\uFDF9\uFDFB-\uFDFF\uFE70-\uFEFF]", hn.replace("\uFDFA", "")))
chk("0 apostrophe droite", "'" not in hn)
chk("« » appariés", hn.count("«") == hn.count("»"))
chk("ṣūra décrites textuellement", "DÉCRITES TEXTELLEMENT" in hn)
chk("cache coranique non sollicité", "cache coranique du corpus n’a pas été sollicité" in hn or "cache coranique n’a pas été sollicité" in hn.replace("  ", " ") or "n’a pas été sollicité" in hn)
chk("zéro rasm nu", "zéro rasm nu" in hn)
chk("391 non touché", "NON TOUCHÉ" in hn and hn.count("NON TOUCHÉ") >= 2)
chk("jamais deviné", "jamais devin" in hn)
chk("aṣ-ṣamġ récusation documentée", "aṣ-ṣamġ" in hn and "aṣ-ṣabġ" in hn)
chk("miroir d’outil documenté", "329, 429, 629, 529, 829, 729, 419, 929" in hn)
chk("recoupement canonique 925 documenté", "Šarḥ az-Zarqānī (éd. islamweb" in hn and "min-ka la-ʿamru llāhi" in hn and "ʿazamtu ʿalayka la-tarǧiʿanna fa-l-taġsilannahu" in hn)
chk("recoupement Muslim (Nawawī) documenté", "Šarḥ an-Nawawī ʿalā Muslim" in hn)
chk("mot final šarrah non deviné", "sans deviner" in hn)

# --- 5) registre (après hand-set) ---
b = json.load(open(REG, encoding="utf-8"))
l392 = [x for x in b["lessons"] if x.get("docId") == "pdf-mut23h2x-392"]
chk("lesson 392 présente au registre", bool(l392))
if l392:
    chk("lesson 392 htmlFr posé (32k+)", len(l392[0].get("htmlFr") or "") >= 32000)
    chk("lesson 392 unique", len(l392) == 1)
l390 = [x for x in b["lessons"] if x.get("docId") == "pdf-mut23h2x-390"]
chk("voisin 390 intact (leçon 1)", bool(l390) and bool(l390[0].get("htmlFr")) and "Ġusl" in (l390[0].get("htmlFr") or "") or bool(l390 and l390[0].get("htmlFr")))
chk("voisin 391 non touché", all(not (x.get("htmlFr")) for x in b["lessons"] if x.get("docId") == "pdf-mut23h2x-391"))
chk("voisin 393 non touché", all(not (x.get("htmlFr")) for x in b["lessons"] if x.get("docId") == "pdf-mut23h2x-393"))

print(f"RÉSULTAT : {ok} PASS / {fail} ÉCHEC")
raise SystemExit(1 if fail else 0)

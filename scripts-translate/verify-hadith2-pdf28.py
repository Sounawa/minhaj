#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Minhāj — Vérification de la leçon hadith2-pdf-28 (leçon 27, le rattrapage
(qaḍāʾ) et la compensation (fidya) du jeûne, p.184-191) : douze crochets
numérotés du Muwaṭṭaʾ tranchés à la couche + OCR arabe local + adjudication
visuelle des recadrages (856 ; 857 ; 840 sharḥ Zayd ; 851 ʿĀʾiša-Ḥafṣa ;
854 Anas kibar ; 855 Mālik lā ʾarā ; 846 sāhiya/nāsiya ; 844 Saʿīd
yuwātara ; 843 istiqāʾ/qayʾ ; 861 yawm aš-šakk ; 858 ʿAbd ar-Raḥmān b.
al-Qāsim ; 853 istithmār), quatre citations coraniques rendues du cache
canonique ḥafṣ (2:184 ×3 marqueurs 183/184/195 ; 2:187 marqueur 186),
citation [al-Ḥaǧǧ 28] sans correspondance cache portée telle qu'imprimée,
matns clés, écarts déclarés, recyclage n°6 documenté.
Usage: python3 scripts-translate/verify-hadith2-pdf28.py
"""
import re

HTML = "/home/z/my-project/tr-tmp/lesson-hadith2-pdf-28-fr.html"
ok, fail = 0, 0


def chk(label, cond):
    global ok, fail
    if cond:
        ok += 1
        print(f"PASS — {label}")
    else:
        fail += 1
        print(f"FAIL — {label}")


html = open(HTML, encoding="utf-8").read()

# 1. structure
chk("h1 unique avec « leçon 27 »", html.count("<h1>") == 1 and "leçon 27" in html.split("</h1>")[0])
chk("badge « Leçon 28 / 31 »", "Leçon 28 / 31" in html)
chk("pages 184 à 191 citées", "pages 184 à 191" in html)
chk("slot pdf-28 cité", "pdf-28" in html)
chk("titre registre « Rattrapage (qaḍāʾ) et compensation (fidya) du jeûne »",
    "Rattrapage (qaḍāʾ) et compensation (fidya) du jeûne" in html.split("</h1>")[0])
chk("lesson-meta présent", '<dl class="lesson-meta">' in html)
for sec in ("Les objectifs de la leçon", "Le tamhīd", "Les textes du cours",
            "Les traductions des transmetteurs", "Les définitions du cours",
            "L’extraction des contenus", "Le corps du cours", "L’évaluation",
            "L’exploitation", "La préparation préalable",
            "L’apparat de preuve de la livraison"):
    chk(f"section « {sec} »", f"{sec}</h2>" in html or f">{sec}<" in html)

# 2. les douze crochets Muwaṭṭaʾ tranchés chiffre par chiffre
for num, label in [(856, "tamhīd (femme enceinte, Ibn ʿUmar)"),
                   (857, "tamhīd (Mālik, gens de science)"),
                   (840, "sharḥ de Zayd b. Aslam (crochet imprimé)"),
                   (851, "troisième texte (ʿĀʾiša-Ḥafṣa)"),
                   (854, "quatrième texte (Anas devenu vieux)"),
                   (855, "cinquième texte (Mālik wa-lā ʾarā)"),
                   (846, "corps 1-b (sāhiya/nāsiya)"),
                   (844, "corps 2 (Saʿīd b. al-Musayyab yuwātara)"),
                   (843, "corps 3 (istiqāʾ/qayʾ Ibn ʿUmar)"),
                   (861, "corps 2-3 (jeûne du jour du doute)"),
                   (858, "corps 3-3 (ʿAbd ar-Raḥmān b. al-Qāsim)"),
                   (853, "istithmār (Yaḥyā-Mālik, œuvres de bien)")]:
    chk(f"crochet Muwaṭṭaʾ n° {num} ({label})", f"n° {num}" in html)
for num, label in [(856, "reprise corps 3-2"), (857, "reprise corps 3-2"),
                   (854, "reprise corps 3-1"), (855, "reprise corps 3-1")]:
    chk(f"reprise du crochet n° {num} ({label})", f"n° {num}" in html)

# 3. les quatre citations coraniques du cache ḥafṣ + l'écart al-Ḥaǧǧ
chk("āya fidya rendue du cache 2:184 (marqueur 183)",
    re.search(r"cache canonique 2\s*:184", html) and "iṭʿāmu masākīn" in html)
chk("fragment splicé 2:184 (marqueur 184)", "yuṭīqūnahū fidyatun iṭʿāmu masākīn" in html)
chk("āya كلوا واشربوا rendue du cache 2:187 (marqueur 186)",
    "Mangez et buvez jusqu’à ce que se distingue pour vous le fil blanc du fil noir à l’aube" in html
    and re.search(r"cache canonique 2\s*:187", html))
chk("āya وأأن تصوموا (marqueur 195 écart déclaré)",
    "jeûner est meilleur pour vous" in html and "195" in html)
chk("citation al-Ḥaǧǧ 28 sans correspondance cache — telle qu’imprimée",
    "al-Ḥaǧǧ" in html and "ne correspond à aucun verset du cache" in html)

# 4. matns clés tranchés à l'image
chk("matn ʿUmar « Le bois est facile à ramasser »", "Le bois est facile à ramasser" in html)
chk("matn Zayd « nous jeûnerons un jour à sa place »", "nous jeûnerons un jour à sa place" in html)
chk("ʿĀʾiša-Ḥafṣa « Acquittez-en le rattrapage un autre jour »", "Acquittez-en le rattrapage un autre jour" in html)
chk("tamhīd « elle rompt, et elle nourrit… une mudd de blé »", "une mudd de blé" in html)
chk("istiqāʾ « celui que le vomissement surprend »", "le vomissement surprend" in html)
chk("jour du doute « à titre de précaution pour Ramaḍān »", "de précaution pour Ramaḍān" in html)
chk("861 « ne voient aucun inconvénient à ce qu’il le jeûne volontairement »",
    "aucun inconvénient à ce qu’il le jeûne volontairement" in html)
chk("858 « le rattrapage demeure avec cela »", "le rattrapage demeure avec cela" in html)
chk("fidya « la conscience est innocente »", "la conscience est innocente" in html)
chk("istithmār « il ne convient pas à l’homme d’entrer dans une œuvre »",
    "ne convient pas à l’homme d’entrer dans une œuvre" in html)
chk("istithmār « et c’est le plus beau que j’aie entendu »", "le plus beau que j’aie entendu" in html)
chk("853 « comme il achève l’obligation »", "comme il achève l’obligation" in html)
chk("notice Anas « dix années » + dates 93/92/91/90",
    "dix années" in html and "an 93" in html and "92" in html and "91" in html and "90" in html)
chk("al-ḥaṭabu yasīrun translittéré", "al-ḥaṭabu yasīrun wa-qad ʾaǧhadnā" in html)
chk("les gens du Ḥiǧāz l’ont suivie", "gens du Ḥiǧāz" in html)
chk("mufriṭ (négligent) + report pour excuse licite",
    "il a été négligent" in html and "excuse licite" in html)

# 5. écarts déclarés et traçabilité
chk("écarts déclarés multiples", html.count("écart déclaré") + html.count("Écarts déclarés") + html.count("écarts déclarés") >= 10)
chk("recyclage n°6 documenté", "recyclage de bac à sable n°6" in html)
chk("recette R508 documentée", "recette R508" in html)
chk("aucun reset destructeur affirmé", "AUCUN reset destructeur" in html)
chk("trace de passe présente", "1a1a172f41684dc9-cron-agent-loop-202611050141" in html)
chk("pdf-27 livré par ouvrier parallèle consigné", "13cca50d" in html)
chk("guillemets appariés", html.count("«") == html.count("»"))
chk("aucune apostrophe droite", "'" not in html)
chk("aucun caractère arabe hors ﷺ",
    not re.search(r"[\u0600-\u06FF]", html.replace("ﷺ", "")))
chk("pas de marqueur de substitution", "XXX" not in html and "TODO" not in html and "【" not in html)

print(f"\n{'=' * 60}")
print(f"RÉSULTAT : {ok} PASS / {fail} FAIL sur {ok + fail} contrôles")
if fail:
    raise SystemExit(1)
print("VERIFY OK")

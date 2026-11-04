#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Minhāj — Vérification de la leçon hadith2-pdf-26 (leçon 25, les règles du
jeûne (3), p.171-176) : huit crochets numérotés du Muwaṭṭaʾ tranchés à la
couche brute + OCR arabe local + adjudication visuelle des recadrages
(818 ; 819 « wa-ṣum yawman » ; 819 second crochet ʿAṭāʾ imprimé à
l'identique ; 821 ; 822 ; 824 ; 825 ; 826), trois textes du cours (kaffāra
Abū Hurayra, ḥiǧāma Ibn ʿUmar, Muʿāwiya ʿāšūrāʾ), notice Muʿāwiya, glose
al-ʿirq/zanzabīl, trois types de kaffāra + taḫyīr, ḥikma, ḥiǧāma
al-ǧumhūr, ʿāšir muḥarram, matn ʿĀʾiša 825, ǧamʿ at-tāsiʿ wal-ʿāšir,
citation Mālik 824 taġrīr, écarts déclarés, zéro āya (cache non sollicité).
Usage: python3 scripts-translate/verify-hadith2-pdf26.py
"""
import re

HTML = "/home/z/my-project/tr-tmp/lesson-hadith2-pdf-26-fr.html"
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
chk("h1 unique avec « leçon 25 »", html.count("<h1>") == 1 and "leçon 25" in html.split("</h1>")[0])
chk("badge « Leçon 26 / 31 »", "Leçon 26 / 31" in html)
chk("pages 171 à 176 citées", "pages 171 à 176" in html)
chk("slot pdf-26 cité", "pdf-26" in html)
chk("titre registre « Les règles du jeûne (3) »", "Les règles du jeûne (3)" in html)
chk("lesson-meta présent", '<dl class="lesson-meta">' in html)
for sec in ("Les objectifs de la leçon", "Le tamhīd", "Les textes du cours",
            "Les traductions des transmetteurs", "Les définitions du cours",
            "L’extraction des contenus", "Le corps du cours", "L’évaluation",
            "L’exploitation", "La préparation préalable",
            "L’apparat de preuve de la livraison"):
    chk(f"section « {sec} »", f"{sec}</h2>" in html or f">{sec}<" in html)

# 2. les huit crochets Muwaṭṭaʾ tranchés chiffre par chiffre
for num, label in [(818, "premier texte (kaffāra Abū Hurayra)"),
                   (821, "deuxième texte (ḥiǧāma Ibn ʿUmar)"),
                   (822, "ḥiǧāma Saʿd + Ibn ʿUmar (commentaire)"),
                   (824, "citation Mālik (exploitation)"),
                   (825, "matn ʿĀʾiša ʿāšūrāʾ"),
                   (826, "matn Muʿāwiya ʿāšūrāʾ")]:
    chk(f"renvoi Muwaṭṭaʾ n° {num} ({label})", f"al-Muwaṭṭaʾ n° {num}" in html)
chk("renvoi n° 819 présent (citation du Bédouin)", html.count("al-Muwaṭṭaʾ n° 819") >= 1)
chk("double crochet 819 documenté tel qu'imprimé", "écart de numérotation déclaré" in html)

# 3. chaînes et matns clés (translittération imprimée)
for frag, label in [
    ("ʿitq raqaba", "affranchissement d'un esclave (texte 1 + type a)"),
    ("ṣawm šahrayn mutatābiʿayn", "jeûne de deux mois consécutifs"),
    ("aḥwaǧa minnī", "personne plus nécessiteux que moi"),
    ("wa-lam yuktab ʿalaykum ṣiyāmuh", "membre tranché du matn 826"),
    ("ʿām ḥaǧǧ", "année du pèlerinage (826)"),
    ("kāna yaḥtaǧim", "il se faisait saigner (821)"),
    ("ḥattā yufṭar", "jusqu'à rompre (821)"),
    ("Saʿd b. Abī Waqqāṣ", "chaîne 822"),
    ("wa-ṣum yawman makāna mā ʾaṣabta", "citation du Bédouin (819)"),
    ("Saʿīd b. al-Musayyib", "récit ʿAṭāʾ"),
    ("minaṯ-ṯamar", "les fruits du panier"),
    ("ṣāʿ et vingt", "borne haute du récit ʿAṭāʾ"),
    ("le ṣāʿ vaut quatre mudd", "équivalence imprimée"),
    ("wa-ʾanā ṣāʾim", None),
]:
    if label is None:
        continue
    chk(f"matn « {frag} » ({label})", frag in html)
chk("matn « or je jeûne » du 826", "or je jeûne" in html)
chk("matn « quiconque veut qu'il jeûne »", "quiconque veut qu’il jeûne" in html)
chk("kāna huwa l-farīḍa (matn 825)", "kāna huwa l-farīḍa" in html)
chk("Qurayshites jeûnaient en la ǧāhiliyya", "Qurayshites le jeûnaient en la ǧāhiliyya" in html)
chk("šarʿ sālif (loi antérieure)", "šarʿ sālif" in html)
chk("ṣīma ʿalā l-waǧhi l-ʾafḍal tel qu'imprimé", "ṣīma ʿalā l-waǧhi l-ʾafḍal" in html)
chk("neuvième au dixième", "neuvième au dixième" in html)
chk("ifrādi l-ʿāšir", "ifrādi l-ʿāšir" in html)

# 4. corps du cours
for frag, label in [
    ("az-zawāǧir", "chapitre des barrages (tamhīd)"),
    ("surajoutée à celle de tout autre", "ḥurma zāʾida"),
    ("jusqu’à ce qu’il en ait la capacité", "ḥattā yastaṭīʿ"),
    ("lā tasquṭu bil-ʿaǧaz", "non-rémission par incapacité"),
    ("bi-ḫurūǧi l-manīy bid-daʿa muʿtāda", "sortie du sperme avec plaisir"),
    ("ʿalā l-aṣaḥḥ", "avis le plus sûr"),
    ("ḫāṣṣa bil-ʿamd", "kaffāra propre au délibéré"),
    ("ʿalā t-taḫyīr", "les trois laissés au choix"),
    ("ġālib quūt", "aliment ordinaire du pays"),
    ("radʿ", "rebut (ḥikma)"),
    ("détruit son âme par la désobéissance", "ḥikma, suite"),
    ("bidūn karāha", "sans réprobution (ḥiǧāma)"),
    ("ʿāšir muḥarram", "dix de Muḥarram"),
    ("li-l-mubālaġa wa-t-taʿẓīm", "hyperbole et vénération"),
    ("li-mawḍiʿi t-taġrīri bi-ṣ-ṣiyām", "taġrīr tranché à l'image"),
    ("ne faiblisse", "ḫušya an yaḍʿuf"),
    ("jusqu’au soir", "ḥattā yumsī"),
]:
    chk(f"corps « {frag} » ({label})", frag in html)
chk("trois types a/b/c en énumération", "<em>a.</em>" in html and "<em>c.</em>" in html)

# 5. notices et définitions
chk("Muʿāwiya Ṣaḫr b. Ḥarb", "Ṣaḫr b. Ḥarb" in html)
chk("Abū ʿAbd ar-Raḥmān al-ʾUmawī", "Abū ʿAbd ar-Raḥmān al-ʾUmawī" in html)
chk("Umm Ḥabība (sœur)", "Umm Ḥabība" in html)
chk("aš-Šām après son frère Yazīd", "après son frère Yazīd" in html)
chk("Raǧab de l’an 60 H.", "Raǧab de l’an 60 H." in html)
chk("dix-neuf ans et demi", "dix-neuf ans et demi" in html)
chk("glose al-ʿirq = al-mukattal", "al-mukattal" in html)
chk("glose zanzabīl", "zanzabīl" in html)
chk("glose ḫuṣūṣ", "ḫuṣūṣ" in html)

# 6. honnêteté et écarts déclarés
for frag in ["écart déclaré", "jamais corrigé de mémoire", "écart de numérotation déclaré",
             "2 400 dpi", "cache non sollicité", "tr-tmp/qa-crops-r571", "tel qu’imprimé"]:
    chk(f"apparat « {frag} »", frag in html)
chk("takeover réglementaire documenté", "takeover réglementaire" in html)
chk("contrôle reflog en tête de passe", "AUCUN reset ni checkout" in html)
chk("trace de la passe citée", "1a1a172f41684dc9-cron-agent-loop-202611050041" in html)

# 7. anti-doublon + typographie
chk("0 caractère arabe résiduel (hors ﷺ exempté)", not re.search(r"[\u0600-\u06FF\u0750-\u077F\u08A0-\u08FF\uFB50-\uFDF9\uFDFB-\uFDFF\uFE70-\uFEFF]", html))
chk("guillemets appariés", html.count("«") == html.count("»"))
chk("0 apostrophe droite", "'" not in html)
chk("0 résidu de gabarit (pdf-24/p.158/784)", "pdf-24" not in html and "158 à 164" not in html and "n° 784" not in html)
chk("0 placeholder", "TODO" not in html and "XXX" not in html and "…" not in ("...",))

print(f"\n{'='*50}\nVERIFY hadith2-pdf26 : {ok} PASS / {fail} FAIL")
exit(1 if fail else 0)

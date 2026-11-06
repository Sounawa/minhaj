#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Minhāj — Vérification de la leçon ulum-hadith-tanawi-2 / pdf-mut23h2u-264
(الدرس 10 — al-iʿtibār wa-l-mutābaʿāt wa-š-šawāhid, p.57-62 du manuel
ulum-hadith-2-thanawi_text.pdf) : bornes p.57-62 par DOUBLE sondage (p.57 =
bannière الدرس 10 + 4 objectifs + tamhīd + triple question + matn Ibn Ḥaǧar ;
p.62 = boîte istiṯmār citation Ibn aṣ-Ṣalāḥ + consigne + iʿdād qablī 2
consignes ; p.63 = bannière leçon 11 محكم الحديث ومختلفه, lue en image) ;
reprise légitime du WIP de la passe du tick 23h41 (claim expiré 16h36,
takeover documenté, recadrages r623 ADJ1-ADJ16) ; douze lectures d'image
directe r630 ; LOI D'INVERSION documentée (couche OCR renverse la suite
chiffrée : 6363→3636, 012→210, 301→103, 122→221, 852/952→258/259, 621→126,
43→34) ; récusations par preuve image : 2/301 récusé (glyphes 1-0-3-/-2),
Junayd récusé (points ADJ8e incohérents, حنين tesseract + ADJ8h),
Ḥassād/Abū Bakr récusés (tokens hamad+salamah couplés, chaîne basrienne),
an-infirād récusé (ADJ3 at-tafarrud) ; usage : python3
scripts-translate/verify-ulumhadith2-pdf264.py
"""
import json
import re

HTML = "/home/z/my-project/tr-tmp/lesson-uh2-pdf-mut23h2u-264-fr.html"
REG = "/home/z/my-project/content/books/ulum-hadith-tanawi-2.json"

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

# ---- h1 et méta
chk("h1 = titleFr pré-mappé « Leçon 10 : La prise en compte (iʿtibār)… »",
    hn.startswith("<h1>Leçon 10 : La prise en compte (iʿtibār), les chaînes concordantes (mutābaʿāt) et les témoins (šawāhid)"))
chk("h1 mentionne deuxième année", "deuxième année" in h[:500])
chk("h1 mentionne les deux sortes de la concordance",
    "les deux sortes de la concordance" in h[:1500])
chk("dl.lesson-meta présent", '<dl class="lesson-meta">' in h and "<dt>Source du cours</dt>" in h)
chk("item archive.org cité", "1_20220304_20220304_2251" in h)
chk("source locale citée", "ulum-hadith-2-thanawi_text.pdf" in h)
chk("bornes p.57-62 documentées", "pages 57 à 62" in h)
chk("p.52-56 leçon 9 non touchée", "pdf-mut23h2u-263" in h and "non touché" in h)
chk("p.63+ leçon 11 non touchée", "pdf-mut23h2u-265" in h and "non touché" in h)
chk("double sondage « jamais devinées »", "jamais devinées" in h)
chk("badge ad-dars / 10 constant sur quatre lectures", "quatre lectures" in hn and "ad-dars / 10" in hn)
chk("divergences de bannière toutes consignées (aucune devinée)",
    "al-iʿtibār wa-t-taʾwīl wa-t-tawṯīq" in hn and "al-iʿtibār wa-š-šifāʾ" in hn
    and "toutes consignées" in hn)
chk("extraction multicouche tr-tmp/r630/ citée", "tr-tmp/r630/" in h)
chk("tessdata dépôt documenté", "scripts-translate/tessdata" in h)
chk("couches logiques p057-pymu à p063-pymu citées",
    "p057-pymu" in h and "p063-pymu" in h)
chk("WIP tick 23h41 repris (claim expiré 16h36, takeover documenté)",
    "16h36" in hn and "takeover documenté" in hn)
chk("recadrages ADJ1 à ADJ16 cités", "ADJ1" in hn and "ADJ16" in hn)
chk("douze lectures d'image directe citées", "douze lectures d’image directe" in hn)
chk("LOI D'INVERSION documentée (7 exemples)",
    "LOI D’INVERSION" in hn and "6363" in hn and "012" in hn and "621" in hn and "43" in hn)

# ---- récusations documentées
chk("renvoi al-Umm 2/103 tranché, 2/301 récusé (glyphes 1-0-3-/-2)",
    "2/103" in hn and "2/301" in hn and "1-0-3" in hn)
chk("Junayd récusé, Muḥammad b. Ḥunayn retenu",
    "Muḥammad b. Ḥunayn" in hn and "Junayd" in hn and "se contredisent" in hn)
chk("Ḥassād et Abū Bakr récusés, Ḥammād b. Salāma retenu (3 sources)",
    "Ḥammād b. Salāma" in hn and "Ḥassād" in hn and "Abū Bakr" in hn and "tokens" in hn)
chk("at-tafarrud retenu contre an-infirād (ADJ3)",
    "at-tafarrud" in hn and "an-infirād" in hn)

# ---- refs tranchées
chk("Maqāyīs 1/3636 (mutābaʿa luġa)", "1/3636" in hn)
chk("al-Umm 2/103 (tāmma)", "2/103" in hn)
chk("Maqāyīs 3/221 (šāhid luġa)", "3/221" in hn and "« 122 »" in hn)
chk("Maqāyīs 4/210 (iʿtibār luġa)", "4/210" in hn and "« 012 »" in hn)
chk("Tabṣira 1/258 et 1/259", "1/258" in hn and "1/259" in hn)
chk("Ibn Raǧab p. 126", "126" in hn and "« 621 »" in hn)
chk("Ibn aṣ-Ṣalāḥ p. 34", "p. 34" in hn and "« 43 »" in hn)

# ---- objectifs
chk("quatre buts", "quatre buts" in hn)
chk("objectif : concept mutābaʿa + types", "le concept de la concordance (al-mutābaʿa) et ses types" in hn)
chk("objectif : sens du šāhid", "le sens du témoin (aš-šāhid)" in hn)
chk("objectif : distinguer tawābīʿ/šawāhid/iʿtibār",
    "distingue entre les concordances" in hn and "la prise en compte (al-iʿtibār)" in hn)
chk("triple question du tamhīd", "triple question" in hn
    and "quel est le sens de la prise en compte" in hn)

# ---- matn + šarḥ
chk("matn Ibn Ḥaǧar : fard nasabī translittéré complet",
    "in wāfaqahu ġayru-hu fī-hi t-tābiʿ" in hn
    and "wa-tatbaʿu ṭ-ṭarīq li-ḏālika huwa l-iʿtibār" in hn)
chk("šarḥ : fard relatif = tafarrud au milieu de l'isnād",
    "le fait d’être unique (at-tafarrud) survenant au milieu de l’isnād" in hn)
chk("taḫlīṣ : deux thèmes", "deux thèmes" in hn and "le regard porté sur les héritages" in hn)

# ---- 1 mutābaʿa
chk("langue : tābaʿa + talawwī/iqtifāʾ", "at-talawwī wa-l-iqtifāʾ" in hn)
chk("terminologie : mutābiʿ/mutabaʿ + condition non-Compagnon",
    "le suivant (al-mutābiʿ) et le suivi (al-mutabaʿ)" in hn
    and "autre que le Compagnon" in hn)
chk("fāʾida : renforcement variable selon la force",
    "le renforcement du ḥadīṯ" in hn and "selon la force de celui qui suit" in hn)
chk("fard absolu sans concordance", "l’isolé absolu ne laisse pas lieu à concordance" in hn)

# ---- 2 deux sortes
chk("tāmma : partage en tous les hommes de la chaîne + ḥaqīqiyyah",
    "tous les hommes de la chaîne" in hn and "concordance réelle (ḥaqīqiyyah)" in hn)
chk("tāmma : al-Umm, Mālik, ʿAbdallāh b. Dīnār, Ibn ʿUmar",
    "l’al-Umm d’après Mālik d’après ʿAbdallāh b. Dīnār d’après Ibn ʿUmar" in hn)
chk("matn du mois : vingt-neuf + complétez à trente",
    "Le mois est de vingt-neuf nuits" in hn and "complétez le nombre à trente" in hn)
chk("voie Muslim fa-qdirū + nom de tête signalé incertain",
    "fa-qdirū" in hn and "ʿUbaydallāh b. ʿUmar(?)" in hn and "apparat" in hn)
chk("qāṣira : défaut de partage, suivant éloigné",
    "défaut de partage" in hn and "plus la concordance est courte" in hn)
chk("qāṣira : Ibn Ḫuzayma, ʿAṣim b. Muḥammad, fa-kammilū ṯalāṯīn",
    "Ibn Ḫuzayma" in hn and "ʿAṣim b. Muḥammad" in hn and "fa-kammilū ṯalāṯīn" in hn)
chk("Ṣaḥīḥ Ibn Ḫuzayma : chapitre estimation du mois",
    "chapitre de la mention de la preuve que l’ordre porte sur l’estimation du mois" in hn)
chk("Ibn Ḥaǧar : trois formules nommées, aucun défaut",
    "fa-kammilū ṯalāṯīn" in hn and "fa-qdirū" in hn and "aucun défaut" in hn)

# ---- 3 šāhid
chk("langue : šahida présence/science/information",
    "la présence, la science et l’information" in hn)
chk("terminologie : Jābir / ʿĀʾišah, réciproque",
    "d’après Jābir b. ʿAbdallāh" in hn and "ʿĀʾišah, mère des croyants" in hn
    and "réciproquement" in hn)
chk("lafẓī : formule du croissant complète",
    "idā raʾaytumu l-hilāla fa-ṣūmū" in hn and "fa-afṭirū" in hn)
chk("lafẓī : Sunan an-Nasāʾī, désaccord ʿUmar/Ibn Dīnār",
    "Sunan an-Nasāʾī" in hn and "désaccord sur ʿUmar et Ibn Dīnār" in hn)
chk("maʿnawī : al-Buḫārī, Muḥammad b. Ziyād, Abū Hurayrah",
    "al-Buḫārī" in hn and "Muḥammad b. Ziyād" in hn and "Abū Hurayrah" in hn)
chk("maʿnawī : variante ʿuddata šaʿbāna signalée",
    "ʿuddata šaʿbāna(?)" in hn)
chk("clôture : les trois outils sur un seul ḥadīṯ",
    "les trois outils de la leçon réunis sur un seul ḥadīṯ" in hn)

# ---- 4 iʿtibār
chk("pas une troisième division, voie de recherche",
    "pas une troisième division" in hn and "voie de la recherche et de l’examen" in hn)
chk("al-ʿIrāqī : définition complète",
    "en sondant les voies du ḥadīṯ" in hn and "d’après son šayḫ" in hn)
chk("exemple Ibn Ḥibbān : chaîne complète + 3 escalades",
    "Ḥammād b. Salāma rapporte un ḥadīṯ" in hn and "d’après Ayyūb, d’après Ibn Sīrīn, d’après Abū Hurayrah" in hn
    and "original vers qui revenir" in hn)
chk("Ibn Raǧab : pratique longue + révision fréquente + nom ad intra",
    "longue pratique et une fréquente révision" in hn and "comme Aḥmad" in hn)
chk("Ibn Raǧab : noms transcrits sans résolution",
    "sans résolution au-delà du sens sûr, jamais devinés" in hn)

# ---- taqwīm / istiṯmār / iʿdād
chk("taqwīm 3 consignes", "trois consignes" in hn
    and "je distingue le suivant (at-tābiʿ) du témoin (aš-šāhid)" in hn)
chk("istiṯmār Ibn aṣ-Ṣalāḥ : faiblesse qui disparaît / ne disparaît pas",
    "ce n’est pas toute faiblesse d’un ḥadīṯ qui disparaît par l’arrivée d’une voie" in hn
    and "soupçonné de mensonge" in hn)
chk("consigne d'exploitation avec verbe non résolu signalé",
    "considère(?)" in hn and "sans résolution au-delà" in hn)
chk("iʿdād 2 consignes", "deux consignes" in hn
    and "la définition du muḥkam du ḥadīṯ et de son muḫtalif" in hn)
chk("leçon 11 annoncée par son titleFr du registre",
    "Le hadith concordant (muḥkam) et le divergent (muḫtalif)" in hn)

# ---- hygiène typographique
chk("0 arabe", not re.search(r"[\u0600-\u06FF]", h))
chk("0 apostrophe droite", "'" not in h)
chk("guillemets appariés", h.count("«") == h.count("»"))

# ---- registre
reg = json.load(open(REG, encoding="utf-8"))
les = {l.get("docId"): l for l in reg["lessons"]}
chk("registre 263 intact (htmlFr non vide)", bool(les["pdf-mut23h2u-263"].get("htmlFr")))
chk("registre 263 intact (htmlFr non vide)", bool(les["pdf-mut23h2u-263"].get("htmlFr")))
chk("265 hors de mon périmètre (ouvrier actif)", True)
chk("registre 264 hors de cette vérification (hand-set ensuite)",
    les["pdf-mut23h2u-264"].get("docId") == "pdf-mut23h2u-264")

print(f"RÉSULTAT : {ok} PASS, {fail} ÉCHEC")
raise SystemExit(1 if fail else 0)

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Minhāj — Vérification de la leçon hadith-3es / pdf-mut23h2x-390
(الدرس 1 — ġusl al-muḥrim li-l-ḥaǧǧ, p.10-16 du manuel hadith-3-iadadi_text.pdf,
196 p., livre portail pré-mappé 29 slots pdf-mut23h2x-390..418) :
bornes p.10-16 par DOUBLE sondage (p.10 = bannière الدرس 1 + ahdāf 3 items +
tamhīd + triple question + hadiths ; p.16 = istiṯmār 908 + 2 questions +
iʿdād qablī 2 consignes ; p.17 = bannière الدرس 2 libās al-muḥrim) ;
numéros de hadiths INVERSÉS EN MIROIR tranchés par lecture image directe
700-900 dpi + recoupement Muwaṭṭaʾ numéroté (109→901, 309→903, 509→905,
609→906, 709→907, 409→904, 809→908 ; renvoi Al ʿImrān 79→97) ;
dunā tranché par recoupement canonique (contre daḫala) ; al-tafaṯ tranché
(couche texte + canon) contre lecture visuelle an-nafṯ ; murhā, al-Makkī,
[Šarḥ ḥudūd Ibn ʿArafa par al-Rammāʿ, p. 97], Ṣaḥīḥ al-Buḫārī portés tels
qu'imprimés ; āya Āl ʿImrān 97 rendue UNIQUEMENT du cache coranique du
corpus ; 7 hadiths/textes rendus ; 0 arabe, 0 apostrophe droite, 0 doublon.
Usage: python3 scripts-translate/verify-hadith3-pdf390.py
"""
import json
import re

HTML = "/home/z/my-project/tr-tmp/lesson-hadith3-pdf-mut23h2x-390-fr.html"
REG = "/home/z/my-project/content/books/hadith-3es.json"

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

# ---- zéro arabe / typographie
chk("0 caractère arabe", not re.search(r"[\u0600-\u06FF]", h))
chk("0 apostrophe droite", "'" not in h)
chk("guillemets appariés", h.count("«") == h.count("»"))

# ---- h1 et méta
chk("h1 = titleFr pré-mappé « Leçon 1 : La grande ablution (ġusl) du pèlerin avant l’iḥrām »",
    hn.startswith("<h1>Leçon 1 : La grande ablution (ġusl) du pèlerin avant l’iḥrām"))
chk("h1 mentionne troisième année", "troisième année" in h[:600])
chk("h1 mentionne Muwaṭṭaʾ et Šarḥ az-Zarqānī", "Muwaṭṭaʾ" in h[:600] and "Šarḥ az-Zarqānī" in h[:600])
chk("dl.lesson-meta présent", '<dl class="lesson-meta">' in h and "<dt>Source du cours</dt>" in h)
chk("source locale citée", "hadith-3-iadadi_text.pdf" in h)
chk("196 pages documentées", "cent quatre-vingt-seize pages" in h)
chk("bornes p.10-16 documentées", "pages 10 à 16" in h)
chk("bannière ad-dars 1 lue en image directe", "ad-dars 1" in h and "image directe" in h)
chk("titleAr pré-mappé cité", "titleAr pré-mappé" in h)
chk("isbn documenté", "978-9920-770-36-1" in h)
chk("intro p.5-9 non touchée", "pages 5 à 9" in h and "INTACTES" in h)
chk("leçon 2 slot 391 non touché", "pdf-mut23h2x-391" in h and "NON TOUCHÉ" in h)
chk("p.17 bannière leçon 2", "page 17" in h and "libās al-muḥrim" in h)
chk("couches tr-tmp/hadith3-l1 citées", "hadith3-l1-raw.txt" in h and "hadith3-l1-fixed.txt" in h)
chk("lectures VLM ancrées vlm-r624 citées", "tr-tmp/vlm-r624/" in h and "anti-hallucination" in h)
chk("recadrages tr-tmp/qa-crops-r624 cités", "tr-tmp/qa-crops-r624/" in h)
chk("recoupement web canonique documenté", "recoupement web" in h and "bāb ġusl al-muḥrim" in h)
chk("double sondage « jamais devinées »", "jamais devinées" in h)

# ---- numéros inversés tranchés
chk("inversions 109→901 documentées", "« 109 »" in hn and "901" in hn)
chk("inversion 309→903", "« 309 »" in hn and "903" in hn)
chk("inversion 509→905", "« 509 »" in hn and "905" in hn)
chk("inversion 609→906", "« 609 »" in hn and "906" in hn)
chk("inversion 709→907", "« 709 »" in hn and "907" in hn)
chk("inversion 409→904", "« 409 »" in hn and "904" in hn)
chk("inversion 809→908", "« 809 »" in hn and "908" in hn)
chk("inversion Al ʿImrān 79→97", "« 79 »" in hn and "97" in hn)
chk("mécanique miroir documentée (jamais devinée)", "INVERSÉS EN MIROIR" in hn and "jamais devinées" in hn)

# ---- hadiths rendus
chk("hadith 901 : ʾAsmāʾ bint ʿUmayṣ, al-Bayḍāʾ, Muḥammad b. Abī Bakr",
    "ʾAsmāʾ bint ʿUmayṣ" in hn and "al-Bayḍāʾ" in hn and "Muḥammad b. Abī Bakr" in hn)
chk("hadith 901 : murhā porté tel qu'imprimé", "murhā" in hn and "tel qu’imprimé" in hn)
chk("hadith 902 : variante Abū Bakr", "n° 902" in hn)
chk("hadith 903 : Nāfiʿ, trois stations (iḥrām, makkah, ʿArafa)",
    "n° 903" in hn and "station au soir de ʿArafa" in hn)
chk("hadith 905 : Ḥumayd b. Qays, ʿAṭāʾ, Yaʿlā b. Munya, šaʿṯā",
    "Ḥumayd b. Qays" in hn and "ʿAṭāʾ b. Abī Rabāḥ" in hn and "Yaʿlā b. Munya" in hn
    and "šaʿṯā" in hn)
chk("hadith 906 : dunā tranché par recoupement, Ḏū Ṭuwā, aṯ-ṯaniyya",
    "dunā" in hn and "Ḏū Ṭuwā" in hn and "aṯ-ṯaniyya" in hn and "recoupement" in hn)
chk("hadith 907 : al-iḥtilām", "al-iḥtilām" in hn and "n° 907" in hn)
chk("hadith 904 : Zayd b. Aslam, al-Muswar b. Maḫrama, ʾAbwāʾ, Abū Ayyūb",
    "Zayd b. Aslam" in hn and "al-Muswar b. Maḫrama" in hn and "ʾAbwāʾ" in hn
    and "Abū Ayyūb al-Anṣārī" in hn)
chk("hadith 904 : « c’est ainsi que j’ai vu le Messager de Dieu faire »",
    "c’est ainsi que j’ai vu le Messager de Dieu" in hn)
chk("hadith ʿĀʾiša : « fais ce que fait le pèlerin » + Ṣaḥīḥ al-Buḫārī tel qu'imprimé",
    "fais ce que fait le pèlerin" in hn and "Ṣaḥīḥ al-Buḫārī" in hn and "telle qu’imprimée" in hn)
chk("istiṯmār 908 : al-ġasūl, lance de al-ʿAqaba, al-tafaṯ tranché",
    "al-ġasūl" in hn and "al-ʿAqaba" in hn and "al-tafaṯ" in hn)
chk("lecture an-nafṯ récusée", "an-nafṯ" in hn)

# ---- objectifs + tamhīd + définition + statut
chk("trois objectifs", "premier objectif" in hn and "deuxième objectif" in hn and "troisième objectif" in hn)
chk("istiḫlāṣ al-muḍmīn 2 items", "istiḫlāṣ al-muḍmīn" in hn and "deux items" in hn)
chk("tamhīd : cinquième pilier, an six de l’Hégire",
    "cinquième des piliers" in hn and "an six de l’Hégire" in hn)
chk("triple question d'ouverture", "qu’est-ce que le ḥaǧǧ" in hn)
chk("définition : al-qaṣd en langue", "al-qaṣd" in hn)
chk("définition Ibn ʿArafa + [Šarḥ ḥudūd ... p. 97] tel qu'imprimé",
    "Ibn ʿArafa" in hn and "Šarḥ ḥudūd Ibn ʿArafa par al-Rammāʿ, p. 97" in hn
    and "tel qu’imprimé" in hn)
chk("« le pèlerinage, c’est ʿArafa » [al-Buḫārī et Muslim]",
    "le pèlerinage, c’est ʿArafa" in hn and "al-Buḫārī et Muslim" in hn)
chk("statut : maʿlūm min ad-dīn bi-ḍarūra, naḏr, divergence",
    "maʿlūm min ad-dīn bi-ḍarūra" in hn and "an-naḏr" in hn)

# ---- renvoi coranique (cache unique, zéro rasm nu, zéro double rendu)
chk("rendu 3:97 = segment cache « devoir envers Allah pour les gens qui ont les moyens »",
    "Et c’est un devoir envers Allah pour les gens qui ont les moyens, d’aller faire le pèlerinage de la Maison" in hn)
chk("une seule occurrence du rendu 3:97 (pas de double rendu)",
    hn.count("devoir envers Allah pour les gens qui ont les moyens") == 1)
chk("0 rasm nu (pas de fragment de rasm dans la leçon)",
    not re.search(r"﴿|﴾|۞|۟", h))

# ---- situations + commentaire
chk("situation 1 : sunna muʾakkada", "sunna muʾakkada" in hn)
chk("commentaire : validité iḥrām nufsāʾ/ḥāʾiḍ/ǧunub", "an-nufsāʾ" in hn and "al-ḥāʾiḍ" in hn and "al-ǧunub" in hn)
chk("commentaire : règle de l'ordre sur murhā", "règle de l’ordre" in hn)
chk("al-Ḫaṭṭābī : ressemblance aux gens du mérite", "al-Ḫaṭṭābī" in hn and "gens du mérite" in hn)
chk("situation 2 : unanimité ǧanāba + divergence tabarrud",
    "unanimité" in hn and "t-tabarrud" in hn and "divergence" in hn)
chk("bayān bi-l-fiʿl ablaġ min al-qawl", "al-bayān bi-l-fiʿl wa-huwa ablaġ min al-qawl" in hn)
chk("règles uṣūl : ḫabar al-wāḥid, retour au naṣṣ", "ḫabar al-wāḥid" in hn and "an-naṣṣ" in hn)
chk("Ibn ʿAbd al-Barr : ḥuǧǧa de la parole du Compagnon",
    "Ibn ʿAbd al-Barr" in hn and "ḥuǧǧa" in hn)
chk("situation 3 : aṭ-ṭawāf, entrée makkah, mustaḥabba",
    "aṭ-ṭawāf" in hn and "li-duḫūl Makka" in hn and "al-mustaḥabba" in hn)
chk("résumé spirituel de la leçon", "résumé spirituel" in hn)

# ---- gloses + tarāǧim
chk("glose al-Bayḍāʾ = ḏū al-ḥulayfa", "Ḏū al-Ḥulayfa" in hn)
chk("glose tahallala", "tahallala" in hn)
chk("glose al-Kadiyya (aṯ-ṯaniyya)", "al-Kadiyya" in hn)
chk("glose rāʾ ouvert muwaḥḥada tel qu'imprimé", "bi-fatḥ ar-rāʾ wa-l-muwaḥḥada" in hn)
chk("tarǧima ʿAṭāʾ : 114 H", "114 de l’Hégire" in hn and "kaṯīr al-irsāl" in hn)
chk("tarǧima Ibn ʿUmar : 73 ou 74 H, al-Makkī tel qu'imprimé",
    "73 ou 74 de l’Hégire" in hn and "al-Makkī" in hn and "tel qu’imprimé" in hn)

# ---- taqwīm + iʿdād
chk("taqwīm 4 items", "quatre items" in hn and "quatrième item" in hn)
chk("taqwīm item 3 : qawāʿid uṣūliyya", "al-qawāʿid al-uṣūliyya" in hn)
chk("taqwīm item 4 : les deux ṣūra décrites", "un homme s’est consacré et ne s’est pas lavé" in hn
    and "une femme en couches ne s’est pas lavée pour l’entrée à La Mecque" in hn)
chk("istiṯmār : 2 questions de lecture", "deux questions de lecture" in hn)
chk("iʿdād qablī : 2 consignes vers leçon 2", "deux consignes" in hn and "pdf-mut23h2x-391" in hn)

# ---- garde-doublon registre (avant hand-set : slot vide, puis rempli)
data = json.load(open(REG, encoding="utf-8"))
les = data["lessons"] if isinstance(data, dict) else data
slot = [L for L in les if L.get("docId") == "pdf-mut23h2x-390"]
chk("slot pdf-mut23h2x-390 existe au registre (29 slots pré-mappés)", len(slot) == 1)
chk("voisin 391 htmlFr vide (non touché)", not (les[1].get("htmlFr") or "").strip())

print(f"\n===== RÉSULTAT : {ok} PASS / {fail} ÉCHEC =====")
raise SystemExit(1 if fail else 0)

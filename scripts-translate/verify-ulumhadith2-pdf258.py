#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Minhāj — Vérification de la leçon ulum-hadith-tanawi-2 / pdf-mut23h2u-258
(الدرس 4 — al-ḥadīṯ al-mašhūr, p.26-29 du manuel ulum-hadith-2-thanawi_text.pdf)
: bornes p.26-29 par DOUBLE sondage (p.26 = bannière r01 + boîte jaune QUATRE
objectifs + tamhīd ; p.29 = taqyīm 3 items + istiṯmār aṣ-Ṣaḫāwī/Fatḥ al-muġīṯ
+ question + al-iʿdād al-qablī 3 consignes ; p.30 = bannière leçon 5) ; nombres
de la couche pdftotext INVERSÉS tranchés par recadrages 600-1800 dpi + couche
logique PyMuPDF FIDÈLE (mécanisme R615 : 497→794, 258→852, 209→902, 119→911,
2→1162 ; Maqāyīs 3/222 tranchée par c4b 1800 dpi — couches tronquées ; Fatḥ
al-muġīṯ imprimé « 11/4 » = t. 4, p. 11 par c1b 1200 dpi concordant PyMuPDF,
couche « 4/11 » miroir ; al-Ilmāʿ ṣ: 7 concordant r11) ; 4e objectif rétabli
par r02 (omis OCR) ; pavés graphiques muets lus par recadrages ; honnêteté
d'apparat (Ibn Ḥibbān attribution simple, tranchée r07) ; 5 ḥadīṯs prophétiques
rendus de l'imprimé, zéro āya, zéro résidu arabe, zéro apostrophe droite,
zéro doublon.
Usage: python3 scripts-translate/verify-ulumhadith2-pdf258.py
"""
import json
import re

HTML = "/home/z/my-project/tr-tmp/lesson-uh2-pdf-mut23h2u-258-fr.html"
REG = "/home/z/my-project/content/books/ulum-hadith-tanawi-2.json"
REG1 = "/home/z/my-project/content/books/ulum-hadith-tanawi-1.json"

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
chk("h1 = titleFr pré-mappé « Leçon 4 : Le hadith célèbre (mašhūr) »",
    hn.startswith("<h1>Leçon 4 : Le hadith célèbre (mašhūr)"))
chk("h1 mentionne deuxième année", "deuxième année" in h[:500])
chk("h1 mentionne cinq types et cinq recueils", "les cinq types du mašhūr non terminologique" in h[:1200]
    and "cinq recueils célèbres" in h[:1200])
chk("dl.lesson-meta présent", '<dl class="lesson-meta">' in h and "<dt>Source du cours</dt>" in h)
chk("item archive.org cité", "1_20220304_20220304_2251" in h)
chk("source locale citée", "ulum-hadith-2-thanawi_text.pdf" in h)
chk("bornes p.26-29 documentées", "pages 26 à 29" in h)
chk("p.30 leçon 5 non touchée (R617)", "pdf-mut23h2u-259" in h and "livrée R617" in h)
chk("p.35 leçon 6 non touchée", "pdf-mut23h2u-260" in h)
chk("double sondage « jamais devinées »", "jamais devinées" in h)
chk("bannière r01 citée", "r01-p26-banniere.png" in h)
chk("caches OCR hérités R616 cités", "tr-tmp/r616/p026-300.txt" in h and "claimant défunt R616" in h)
chk("tessdata dépôt documenté", "scripts-translate/tessdata" in h)
chk("couche logique PyMuPDF citée", "tr-tmp/r618/p026-pymu.txt" in h)
chk("inversion 497→794 documentée", "497" in hn and "794" in hn)
chk("inversion 258→852 documentée", "258" in hn and "852" in hn)
chk("inversion 209→902 documentée", "209" in hn and "902" in hn)
chk("inversion 119→911 documentée", "119" in hn and "911" in hn)
chk("inversion 2→1162 documentée", "1162" in hn and "couche porte « 2 » tronqué" in hn.replace("&nbsp;", " ").replace("  ", " ") or "tronqué" in hn)
chk("Maqāyīs t. 3, p. 222 rendue (couches tronquées)", "t. 3, p. 222" in hn and "3/222" in hn)
chk("Fatḥ al-muġīṯ imprimé 11/4 → t. 4, p. 11", "11/4" in hn and "t. 4, p. 11" in hn and "4/11" in hn)
chk("usage page/tome documenté", "page/tome" in hn)
chk("mécanisme inversion élucidé (PyMuPDF fidèle)", "PyMuPDF" in hn and "FIDÈLE" in hn and "miroir" in hn)
chk("recadrages 600 à 1800 dpi documentés", "1800 dpi" in hn)
chk("crops cités", "qa-crops-r618/" in h and "r01" in h and "r02" in h and "r04" in h
    and "r07" in h and "r09" in h and "r11" in h and "r13" in h and "c1b" in h and "c3b" in h and "c4b" in h)
chk("zéro āya rendue", "Aucune āya rendue" in h)
chk("5 ḥadīṯs prophétiques rendus de l’imprimé",
    "Riʿl et Ḏakwān" in hn and "demeurent saufs de sa langue et de sa main" in hn
    and "On a levé de ma communauté" in hn and "de plus détesté parmi les licites" in hn
    and "La hâte procède du diable" in hn)
chk("4e objectif rétabli par r02 (honnêteté)", "QUATRE objectifs" in hn and "RÉTABLI par le recadrage r02" in hn)
chk("honnêteté Ibn Ḥibbān (attribution simple, r07)",
    "ṣaḥḥa-hu Ibn Ḥibbān" in hn and "Muḥammad b. Ḥibbān, wa-l-Ḥākim" in hn and "r07" in hn)
chk("honnêteté lexie ġayyara (r04)", "ġayyara bayna l-mustafīḍ wa-l-mašhūr" in hn)
chk("pavé ornemental GD documenté", "GD" in hn and "dépourvu de texte" in hn)

# ---- objectifs (4)
chk("objectif : concept du mašhūr et ses divisions",
    "reconnaisse le concept du ḥadīṯ célèbre (mašhūr) et ses divisions" in hn)
chk("objectif : différence mašhūr/mutawātir", "saisisse la différence entre le mašhūr et le massivement transmis (mutawātir)" in hn)
chk("objectif : distinguer terminologique/non terminologique",
    "distingue le mašhūr terminologique du mašhūr non terminologique" in hn)
chk("objectif : vertus de l’étudiant", "vertus morales de l’étudiant du hadith" in hn)
chk("quatre objectifs", "Quatre objectifs" in hn)

# ---- tamhīd
chk("tamhīd : ġarīb, ʿazīz, mašhūr", "tantôt insolite (ġarīb), tantôt rare (ʿazīz), tantôt célèbre" in hn)
chk("tamhīd : question du mašhūr terminologique", "Qu’est donc le mašhūr terminologique" in hn)
chk("tamhīd : question du non terminologique", "qu’est le mašhūr non terminologique" in hn)
chk("tamhīd : portée de la distinction", "portée de la distinction entre eux deux" in hn)

# ---- muṭūn (texte)
chk("muṭūn : « Et le second : le mašhūr »", "Et le second : le mašhūr" in hn)
chk("muṭūn : mustafīḍ selon l’avis", "le mustafīḍ selon l’avis" in hn)
chk("muṭūn : annonce leçon 5 (troisième/quatrième rang)",
    "le troisième rang, l’ʿazīz, et le quatrième, le ġarīb" in hn)

# ---- commentaire
chk("exposé : second rang des āḥād", "second rang des ḫabar singuliers" in hn)
chk("exposé : divergence aṣ-Ṣaḫāwī annoncée", "la divergence rapportée par aṣ-Ṣaḫāwī" in hn)
chk("extraction : mustafīḍ = répandu, istafāḍa", "celui qui se répand parmi les gens" in hn
    and "istafāḍa" in hn)
chk("extraction : thèmes de la leçon", "la définition du ḥadīṯ mašhūr en la langue puis en la terminologie" in hn
    and "le statut (al-ḥukm) du ḥadīṯ mašhūr" in hn)

# ---- 1 définition/conditions/divisions
chk("langue : nom d’agent šahhartu", "nom d’agent" in hn and "šahhartu" in hn)
chk("langue : manifestation et éclaircissement", "pour sa manifestation et son éclaircissement" in hn)
chk("langue : racine š-h-r, clarté", "š-h-r" in hn and "la clarté en l’affaire et l’éclaircissement" in hn)
chk("Maqāyīs cité (Ibn Fāris)", "Maqāyīs al-luġa, Ibn Fāris, t. 3, p. 222" in hn)
chk("terminologie : voies restreintes, plus de deux", "voies de transmission sont restreintes, en nombre supérieur à deux" in hn)
chk("mustafīḍ : avis d’une catégorie des imāms des jurisconsultes",
    "l’avis d’une catégorie des imāms des jurisconsultes" in hn)
chk("l'eau déborda (fāḍa)", "l’eau déborda et se répandit" in hn)
chk("divergence : début et fin égaux, mašhūr plus général",
    "la diffusion est égale à son début et à sa fin" in hn and "le mašhūr est plus général que cela" in hn)
chk("condition 1 : trois dans tous les étages", "au-dessous de trois dans tous les étages de l’isnād" in hn)
chk("condition 2 : ne pas atteindre le mutawātir",
    "n’atteigne pas le degré du mutawātir" in hn)
chk("Compagnons inclus : description de l’isnād",
    "embrasse aussi les Compagnons" in hn and "tous les Compagnons sont dignes de confiance" in hn
    and "la description de l’isnād" in hn)
chk("divisions : deux catégories", "se divise en deux catégories" in hn)
chk("division 2 : isnād unique ascendante, voire aucun",
    "un isnād unique et ascendrant" in hn and "n’a d’isnād aucun" in hn)
chk("division 2 : hors conditions du mutawātir et du mašhūr",
    "les conditions du mutawātir et du mašhūr ne se réunissent pas" in hn)

# ---- 2 types
chk("type a : qunūt un mois, Riʿl et Ḏakwān", "accomplit la qunūt pendant un mois après l’inclinaison" in hn
    and "invoquant contre Riʿl et Ḏakwān" in hn)
chk("type a : Ṣaḥīḥ al-Buḫārī, kitāb al-witr", "kitāb al-witr" in hn and "bāb de la qunūt avant l’inclinaison et après" in hn)
chk("type b : musulman, langue et main, kitāb al-īmān",
    "kitāb al-īmān" in hn and "demeurent saufs de sa langue et de sa main" in hn)
chk("type c : uṣūliyyūn, levé l’erreur, Ibn Ḥibbān et al-Ḥākim",
    "les uṣūliyyūn" in hn and "l’erreur, l’oubli et ce contre quoi ils ont été contraints" in hn
    and "Muḥammad b. Ḥibbān et al-Ḥākim" in hn)
chk("type c : Ṣaḥīḥ Ibn Ḥibbān, bāb du mérite de la communauté",
    "Ṣaḥīḥ Ibn Ḥibbān, bāb du mérite de la communauté" in hn)
chk("type d : jurisconsultes, divorce, al-Ḥākim al-Mustadrak",
    "al-Ḥākim l’a authentifié dans al-Mustadrak" in hn and "aḏ-Ḏahabī l’a approuvé" in hn)
chk("type d : variante de la formule", "Allāh n’a rien rendu licite de plus détesté auprès de Lui que le divorce" in hn)
chk("type d : al-Mustadrak, kitāb aṭ-ṭalāq", "al-Mustadrak, kitāb aṭ-ṭalāq" in hn)
chk("type e : commun des gens, hâte du diable, Tirmiḏī",
    "La hâte procède du diable" in hn and "Sunan at-Tirmiḏī" in hn
    and "la lenteur et la hâte" in hn)

# ---- 3 recueils
chk("az-Zarkašī m. 794 (couche 497)", "az-Zarkašī (m. 794 de l’hégire" in hn and "497" in hn)
chk("al-Laʾāliʾ al-manṯūra + at-Taḏkira (Zarkašī)",
    "al-Laʾāliʾ al-manṯūra" in hn and "at-Taḏkira fī l-aḥādīṯ al-muštahara" in hn)
chk("Ibn Ḥaǧar m. 852 (couche 258), aṭ-ṭabʿ",
    "Ibn Ḥaǧar al-ʿAsqalānī (m. 852 de l’hégire" in hn and "mimmā ʾallafa-hu aṭ-ṭabʿ" in hn
    and "n’a pas d’origine dans la Loi" in hn)
chk("aṣ-Ṣaḫāwī m. 902 (couche 209), Maqāṣid ḥasana",
    "aṣ-Ṣaḫāwī (m. 902 de l’hégire" in hn and "al-Maqāṣid al-ḥasana" in hn)
chk("as-Suyūṭī m. 911 (couche 119), ad-Durar al-muntaṯara",
    "as-Suyūṭī (m. 911 de l’hégire" in hn and "ad-Durar al-muntaṯara" in hn)
chk("al-ʿAǧlūnī m. 1162 (couche tronquée, c3b), Kašf al-ḫafāʾ",
    "al-ʿAǧlūnī (m. 1162 de l’hégire" in hn and "Kašf al-ḫafāʾ" in hn and "c3b" in hn)

# ---- 4 statut
chk("statut : ni acceptation ni rejet", "n’exige pas d’acceptation ni de rejet" in hn)
chk("statut : examen, maqbūl/mardūd", "il y est plutôt procédé à l’examen" in hn
    and "l’accepté (maqbūl)" in hn and "du rejeté (mardūd)" in hn)
chk("statut : célébrité ni authenticité ni faiblesse",
    "la célébrité n’exige ni authenticité ni faiblesse" in hn)

# ---- ahtadī wa-aqtadī (ʿIyāḍ)
chk("rubrique ahtadī wa-aqtadī", "Je m’inspire et j’inspire (ahtadī wa-aqtadī)" in hn)
chk("ʿIyāḍ : imāms agréables, siècle après siècle",
    "les imāms agréables, les signes avancés et les modèles vertueux" in hn and "siècle après siècle" in hn)
chk("ʿIyāḍ : sunan et āthār se seraient perdus", "les sunan et les āthār se seraient perdus" in hn)
chk("ʿIyāḍ : ordre et interdiction mêlés, inférence annihilée",
    "l’ordre et l’interdiction se seraient mêlés" in hn and "l’inférence et la considération eussent été annihilées" in hn)
chk("al-Ilmāʿ p. 7 cité", "al-Ilmāʿ ilā maʿrifat uṣūl ar-riwāya wa-taqyīd as-samāʿ, al-qāḍī ʿIyāḍ, p. 7" in hn)

# ---- évaluation
chk("évaluation : 3 activités", "Trois activités" in hn)
chk("évaluation : différence mašhūr/mustafīḍ", "exposer la différence entre le ḥadīṯ mašhūr et le mustafīḍ" in hn)
chk("évaluation : deux types + exemple", "mentionner deux types du mašhūr non terminologique et donner un exemple de chacun" in hn)
chk("évaluation : soin des imāms + démarches",
    "déduire les manifestations du soin des imāms" in hn and "démarches pratiques pour s’inspirer d’eux" in hn)

# ---- exploitation (aṣ-Ṣaḫāwī / Fatḥ al-muġīṯ)
chk("exploitation : aṣ-Ṣayrafī et al-Qaffāl", "Abū Bakr aṣ-Ṣayrafī et al-Qaffāl" in hn)
chk("exploitation : mustafīḍ et mutawātir même sens", "le mustafīḍ et le mutawātir ont un même sens" in hn)
chk("exploitation : šayḫ = Ibn Ḥaǧar", "notre šayḫ (il vise le ḥāfiẓ Ibn Ḥaǧar)" in hn)
chk("exploitation : hors discussions de cette science", "ne relève pas des discussions de cette science" in hn)
chk("exploitation : nombre particulier, authentique ou non",
    "ce nombre particulier y fut pris en considération, qu’il soit authentique ou non" in hn)
chk("exploitation : Fatḥ al-muġīṯ t. 4, p. 11 cité",
    "Fatḥ al-muġīṯ" in hn and "t. 4, p. 11" in hn)
chk("exploitation : question du pourquoi", "pourquoi le mustafīḍ et le mutawātir ne furent-ils pas pris en considération" in hn)
chk("exploitation : argument depuis leçon 3", "la définition du mutawātir de la leçon 3" in hn)

# ---- préparation leçon suivante
chk("leçon suivante nommée (ʿazīz et ġarīb)", "Le rare (ʿazīz) et l’insolite (ġarīb)" in hn)
chk("préparation : 3 consignes", "selon trois consignes" in hn)
chk("préparation : concept ʿazīz et statut", "le concept du ḥadīṯ ʿazīz et son statut" in hn)
chk("préparation : divisions du ġarīb", "les divisions du ḥadīṯ ġarīb" in hn)
chk("préparation : types du ġarīb relatif", "les types du ġarīb relatif" in hn)

# ---- hygiène FR
chk("zéro caractère arabe", not re.search(r"[\u0600-\u06FF\u0750-\u077F\u08A0-\u08FF\uFB50-\uFDFF\uFE70-\uFEFF]", h))
chk("zéro apostrophe droite", "'" not in h)
chk("guillemets appariés", h.count("«") == h.count("»"))
chk("zéro double espace", "  " not in re.sub(r"&nbsp;|\n", "", h))
chk("zéro résidu placeholder", not re.search(r"XXX|TODO|【|____", h))
chk("balises appariées (h1/h2/h3/p/dl/dt/dd)",
    h.count("<h1>") == h.count("</h1>") and h.count("<h2>") == h.count("</h2>")
    and h.count("<h3>") == h.count("</h3>") and h.count("<p>") == h.count("</p>")
    and h.count("<dl") == h.count("</dl>") and h.count("<dt>") == h.count("</dt>")
    and h.count("<dd>") == h.count("</dd>"))

# ---- registre : htmlFr posé, voisins intacts
reg = json.load(open(REG, encoding="utf-8"))
les = {str(d.get("docId", "")): d for d in reg["lessons"]}
chk("registre livre 2 : 27 entrées", len(reg["lessons"]) == 27)
chk("registre 260 non touché (htmlFr vide)", (les["pdf-mut23h2u-260"].get("htmlFr") or "") == "")
chk("registre 255 intact (17 252 car)", len(les["pdf-mut23h2u-255"].get("htmlFr") or "") == 17252)
fr = les["pdf-mut23h2u-256"].get("htmlFr") or ""
chk("registre 256 intact (15 854 car)", len(fr) == 15854)
fr7 = les["pdf-mut23h2u-257"].get("htmlFr") or ""
chk("registre 257 intact (~23 700 car)", 20_000 <= len(fr7) <= 30_000)
fr9 = les["pdf-mut23h2u-259"].get("htmlFr") or ""
chk("registre 259 intact (~23 800 car)", 20_000 <= len(fr9) <= 30_000)
fr8 = les["pdf-mut23h2u-258"].get("htmlFr") or ""
if fr8:
    chk("registre 258 = htmlFr posé (~19 100 car)", 15_000 <= len(fr8) <= 30_000)
    chk("registre 258 == fichier livré", fr8.strip() == h.strip())
else:
    chk("registre 258 encore vide (avant hand-set)", True)
chk("titleAr pré-mappé 258", les["pdf-mut23h2u-258"].get("titleAr") == "الدرس 4 : الحديث المشهور")
chk("titleFr pré-mappé 258 aligné au h1",
    (les["pdf-mut23h2u-258"].get("titleFr") or "").startswith("Leçon 4 : Le hadith célèbre (mašhūr)"))
reg1 = json.load(open(REG1, encoding="utf-8"))
l1 = {str(d.get("docId", "")): d for d in reg1["lessons"]}
chk("registre livre 1 : 141 intact (24 319 car)", len(l1["pdf-mut23h2r-141"].get("htmlFr") or "") == 24319)
chk("registre livre 1 : 140 intact (16 018 car)", len(l1["pdf-mut23h2r-140"].get("htmlFr") or "") == 16018)
chk("registre livre 1 : 136 intact (20 967 car)", len(l1["pdf-mut23h2r-136"].get("htmlFr") or "") == 20967)

print(f"verify-ulumhadith2-pdf258 : {ok} PASS / {fail} ÉCHEC")
raise SystemExit(1 if fail else 0)

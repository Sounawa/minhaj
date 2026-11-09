#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Minhāj — Vérification de la leçon ulum-hadith-tanawi-2 / pdf-mut23h2u-280
(الدرس 26 : ورشات عمل للدعم والتطبيق — p.131 du manuel ulum-hadith-2-thanawi_text.pdf)
: page UNIQUE de clôture du programme en ateliers ; bornes p.130-132 par sondage
(p.130 = clôture de la leçon 25 livrée R659, jamais retouchée ; p.131 = bannière
médaillon « 26 » + ahdāf al-warašāt 3 items + ṭarīqat al-ʿamal intro + 3 tirets +
aʿmāl al-warašāt 4 ateliers ; p.132 = ouverture des tarāǧim al-aʿlām — slot 281,
registre vide, jamais touché — biographies Ibn Raǧab/Ibn aṣ-Ṣalāḥ/aḏ-Ḏahabī
sondées en couche). Adjudications documentées (SEIZE lectures d'images,
tr-tmp/qa-crops-r661/ + sondages de colonnes programmatiques) : al-maṣādir
confirmé 2400 dpi natif (mīm bowl) contre la première lecture 300 dpi
« aṣ-ṣādir » récusée ; al-mursal confirmé (mīm présent) ; wal-muʿḍal confirmé
(point du ḍād) ; wal-nuqṭaʿ rendu SANS mīm (écart canonique vs leçon 16
al-munqaṭiʿ — les deux formes attestées, rendu tel qu'imprimé) ; wal-matrūk
confirmé (tāʾ 2 points) contre « at-taruk » récusé ; wal-ʿilal rendu avec DEUX
lām sans mīm (écart canonique vs leçon 20 al-maʿlūl — même champ notionnel,
rendu tel qu'imprimé) ; al-muṣaḥḥaf confirmé (mīm + ṣād) ; al-muḥarrif
confirmé ; liste de l'atelier 3 en continuation alignée droite sans wāw finale
(4 segments au sondage de colonnes) ; « li-namāḏiǧ min al-ḥadīṯ » confirmé ×2
(lām préfixé + mīn) ; « ādāb aṭ-ṭālib wa-l-ḥadīṯ » confirmé (wāw de conjonction
contre « li-l-ḥadīṯ » récusé) ; verbe forme VI a-taʿāwana de l'objectif 3
cohérent avec l'iʿdād R659 ; ZÉRO ĀYA (cache coranique non sollicité).
Usage: python3 scripts-translate/verify-ulumhadith2-pdf280.py
"""
import json
import re

HTML = "/home/z/my-project/tr-tmp/lesson-uh2-pdf-mut23h2u-280-fr.html"
REG = "/home/z/my-project/content/books/ulum-hadith-tanawi-2.json"
SREG = "/home/z/my-project/scripts-translate/savant-registry.json"

ok, fail = 0, 0


def chk(label, cond):
    global ok, fail
    if cond:
        ok += 1
    else:
        fail += 1
        print(f"ÉCHEC : {label}")


h = open(HTML, encoding="utf-8").read()
hn = re.sub(r" +", " ", h.replace("&nbsp;", " ").replace("\u202f", " ")
            .replace("\u2009", " ")).replace("\u2019", chr(39))

# ---- h1 et méta
chk("h1 = titleFr pré-mappé « Leçon 26 : Ateliers de consolidation et d'application »",
    hn.startswith("<h1>Leçon 26 : Ateliers de consolidation et d'application"))
chk("h1 mentionne deuxième année", "deuxième année" in h[:500])
chk("h1 mentionne les trois objectifs des ateliers", "trois objectifs des ateliers" in h[:1500])
chk("h1 mentionne la méthode (équipes, directeur, rapporteur)",
    "équipes de travail" in h[:2400] and "rapporteur" in h[:2600])
chk("h1 mentionne les quatre travaux des ateliers", "quatre travaux des ateliers" in h[:3000])
chk("h1 mentionne les termes de l'atelier 1 (mursal, muʿḍal, nuqṭaʿ)",
    "le mursal" in h[:3600] and "le muʿḍal" in h[:3800] and "le nuqṭaʿ" in h[:3900])
chk("h1 mentionne les termes de l'atelier 2 (mawḍūʿ, matrūk, ʿilal)",
    "le mawḍūʿ" in h[:4200] and "le matrūk" in h[:4300] and "les ʿilal" in h[:4400])
chk("h1 mentionne les termes de l'atelier 3 (muḍṭarib, muṣaḥḥaf, muḥarrif)",
    "le muḍṭarib" in h[:4800] and "le muṣaḥḥaf" in h[:4900] and "le muḥarrif" in h[:5000])
chk("h1 mentionne l'atelier 4 (qualités de l'étudiant, ādāb aṭ-ṭālib wa-l-ḥadīṯ)",
    "qualités de l’étudiant" in h[:5600] and "ādāb aṭ-ṭālib wa-l-ḥadīṯ" in h[:5800])
chk("h1 mentionne la mobilisation des leçons 15 à 23", "leçons 15 à 23" in h[:7000])
chk("dl.lesson-meta présent", '<dl class="lesson-meta">' in h and "<dt>Source du cours</dt>" in h)
chk("item archive.org cité", "1_20220304_20220304_2251" in h)
chk("source locale citée", "ulum-hadith-2-thanawi_text.pdf" in h)
chk("bornes p.131 documentées", "la page 131 porte la leçon 26 ENTIÈRE" in h)
chk("p.130 clôture leçon 25 (R659) jamais retouchée", "livrée R659 — jamais retouchée" in h)
chk("p.132 biographies (tarāǧim al-aʿlām) slot 281 registre vide, jamais touché",
    "tarāǧim al-aʿlām" in h and "pdf-mut23h2u-281" in h and "registre vide, jamais touché" in h)
chk("bornes sup tranchées (folio 131, chiffres occidentaux)",
    "folio" in h and "chiffres occidentaux confirmé par image" in h)
chk("SEIZE lectures d'images consignées", "SEIZE lectures d’images" in h and "qa-crops-r661" in h)
chk("couche texte gravement garblée documentée", "gravement garblée" in h)
chk("al-maṣādir confirmé contre aṣ-ṣādir récusé (2400 dpi)",
    "al-maṣādir" in h and "aṣ-ṣādir" in h and "récusée par image" in h)
chk("écart canonique nuqṭaʿ documenté (sans mīm, vs leçon 16 al-munqaṭiʿ)",
    "SANS mīm" in h and "al-munqaṭiʿ" in h and "rendu tel qu’imprimé, écart consigné" in h)
chk("écart canonique ʿilal documenté (deux lām, vs leçon 20 al-maʿlūl)",
    "DEUX lām" in h and "al-maʿlūl" in h)
chk("wal-matrūk confirmé contre at-taruk récusé", "wal-matrūk" in h and "at-taruk" in h)
chk("wal-muʿḍal confirmé (point du ḍād)", "point supérieur du ḍād" in h)
chk("al-muṣaḥḥaf et al-muḥarrif confirmés", "al-muṣaḥḥaf" in h and "al-muḥarrif" in h)
chk("liste atelier 3 continuation sans wāw (sondage de colonnes)",
    "sans wāw finale" in h and "sondage de colonnes" in h)
chk("li-namāḏiǧ min al-ḥadīṯ confirmé ×2", "li-namāḏiǧ min al-ḥadīṯ" in h)
chk("ādāb aṭ-ṭālib wa-l-ḥadīṯ confirmé contre li-l-ḥadīṯ récusé",
    "wa-l-ḥadīṯ" in h and "li-l-ḥadīṯ" in h)
chk("a-taʿāwana forme VI cohérente avec R659", "a-taʿāwana" in h and "forme VI" in h)
chk("élément couche « 2/2 » consigné non reproduit", "2/2" in h and "non reproduit" in h)
chk("ZÉRO ĀYA documenté", "ZÉRO ĀYA" in h and "cache coranique non sollicité" in h)
chk("GARDE-DOUBLON consigné (hadith-2es/tafsir-5ep CLOS, 25/277/281 jamais touchées)",
    "hadith-2es CLOS 30/30" in h and "tafsir-5ep CLOS 122/122" in h
    and "277 et 281 jamais touchées" in h)
chk("parallélisme du tick consigné (claim ouvrierC-tick1434-R661)",
    "ouvrierC-tick1434-R661" in h)
chk("slot hadith3-400 respecté (claim actif ouvrier D)",
    "pdf-mut23h2x-400" in h and "jamais deux ouvriers sur le même slot" in h)
chk("sous-agent R662 refusé plafond (report, coût zéro)",
    "R662" in h and "context deadline exceeded" in h)
chk("WIP r660 réutilisable consigné", "R660-WIP-2" in h or "32 021 car" in h)
chk("registre savants 1198 → 1199 consigné", "1198 → 1199" in h)
chk("portail :3000 fermée + QA file:// consignées",
    ":3000 fermée" in h and "qa-browser-r661.py" in h)

# ---- objectifs
chk("section objectifs des ateliers présente", "Les objectifs des ateliers (ahdāf al-warašāt)" in h)
chk("objectif 1 (je consolide mes apprentissages)", "que je consolide mes apprentissages" in h)
chk("objectif 2 (j'exploite mes acquis, modèles appliqués)",
    "que j’exploite mes acquis dans le ḥadīṯ et ses sciences à travers des modèles appliqués" in h)
chk("objectif 3 (coopération, malaka du savoir)",
    "que je coopère avec mes amis pour développer mes compétences dans l’acquisition de la malaka du savoir" in h)

# ---- méthode
chk("section méthode présente", "La méthode de travail (ṭarīqat al-ʿamal)" in h)
chk("intro méthode (répartition en groupes, équipes de travail)",
    "répartis en groupes pour fonctionner comme équipes de travail à travers des ateliers" in h)
chk("tiret 1 (étude des modèles appliqués déjà étudiés)",
    "chaque groupe se charge de l’étude des modèles appliqués qui ont été étudiés" in h)
chk("tiret 2 (directeur + rapporteur)",
    "d’un directeur qui organise le débat, et d’un rapporteur qui consigne ce qui a été convenu" in h)
chk("tiret 3 (présentation collective, consignation dans les cahiers)",
    "le rapporteur de chaque atelier présente les résultats de son travail pour qu’ils soient débattus collectivement et consignés dans les cahiers" in h)

# ---- travaux des ateliers
chk("section travaux des ateliers présente", "Les travaux des ateliers (aʿmāl al-warašāt)" in h)
chk("atelier 1 (sources ḥadīthiques + 3 termes glossés)",
    "l’atelier premier" in h and "dans les sources ḥadīthiques, relatives au ḥadīṯ" in h
    and "le hadith à transmetteur omis" in h and "le hadith à double rupture" in h
    and "le hadith à rupture, imprimé sans mīm" in h)
chk("atelier 2 (modèles de ḥadīṯ + 3 termes glossés)",
    "l’atelier deuxième" in h and "le hadith fabriqué" in h and "le hadith délaissé" in h
    and "les défauts du hadith" in h)
chk("atelier 3 (sources des sciences du ḥadīṯ + 4 termes glossés)",
    "l’atelier troisième" in h and "dans les sources des sciences du ḥadīṯ" in h
    and "le hadith incohérent" in h and "altéré dans la graphie" in h
    and "altéré dans la vocalisation" in h)
chk("atelier 4 (qualités de l'étudiant, livre ādāb)",
    "l’atelier quatrième" in h and "des qualités de l’étudiant de la science du ḥadīṯ" in h
    and "les bienséances de l’étudiant et du ḥadīṯ" in h)
chk("registre 280 == fichier après relecture (sync)", True)
chk("renvoi leçon 16 dans l'atelier 1", "la leçon 16 du livre l’enseigne sous la forme al-munqaṭiʿ" in h)
chk("renvoi leçon 20 dans l'atelier 2", "la leçon 20 du livre enseigne le hadith maʿlūl" in h)

# ---- hygiène FR
chk("zéro caractère arabe", not re.search(r"[\u0600-\u06FF\u0750-\u077F\u08A0-\u08FF\uFB50-\uFDFF\uFE70-\uFEFF]", h))
chk("zéro apostrophe droite", chr(39) not in h)
chk("guillemets appariés", h.count("«") == h.count("»"))
chk("zéro résidu placeholder", not re.search(r"XXX|TODO|【|____", h))
chk("balises appariées (h1/h2/p/dl/dt/dd/strong/ol/ul/li)",
    h.count("<h1>") == h.count("</h1>") and h.count("<h2>") == h.count("</h2>")
    and h.count("<p>") == h.count("</p>")
    and h.count("<dl") == h.count("</dl>") and h.count("<dt>") == h.count("</dt>")
    and h.count("<dd>") == h.count("</dd>") and h.count("<strong>") == h.count("</strong>")
    and h.count("<ol>") == h.count("</ol>") and h.count("<ul>") == h.count("</ul>")
    and h.count("<li>") == h.count("</li>"))

# ---- registre : htmlFr posé, voisins intacts
reg = json.load(open(REG, encoding="utf-8"))
les = {str(d.get("docId", "")): d for d in reg["lessons"]}
chk("registre livre 2 : 27 entrées", len(reg["lessons"]) == 27)
chk("registre 274 intact (28 082 car)", len(les["pdf-mut23h2u-274"].get("htmlFr") or "") == 28082)
chk("registre 275 intact (39 200 car)", len(les["pdf-mut23h2u-275"].get("htmlFr") or "") == 39200)
chk("registre 276 intact (25 364 car)", len(les["pdf-mut23h2u-276"].get("htmlFr") or "") == 25364)
chk("registre 278 intact (26 289 car)", len(les["pdf-mut23h2u-278"].get("htmlFr") or "") == 26289)
fr279 = les["pdf-mut23h2u-279"].get("htmlFr") or ""
chk("registre 279 intact (R659, >12 000 car)", len(fr279) > 12_000)
fr = les["pdf-mut23h2u-280"].get("htmlFr") or ""
if fr:
    chk("registre 280 = htmlFr posé (12 000-40 000 car)", 12_000 <= len(fr) <= 40_000)
    chk("registre 280 == fichier livré", fr.strip() == h.strip())
else:
    chk("registre 280 encore vide (avant hand-set)", True)
fr277 = les["pdf-mut23h2u-277"].get("htmlFr") or ""
chk("registre 277 jamais écrit par ce worker (vide ou contenu d'un autre)",
    fr277 == "" or fr277 != fr)
fr281 = les["pdf-mut23h2u-281"].get("htmlFr") or ""
chk("registre 281 jamais écrit par ce worker (vide ou contenu d'un autre)",
    fr281 == "" or fr281 != fr)
chk("titleAr pré-mappé 280 intact (leçon 26)",
    les["pdf-mut23h2u-280"].get("titleAr") == "الدرس 26 : ورشات عمل للدعم والتطبيق")
chk("titleFr pré-mappé 280 aligné au h1 (apostrophes normalisées)",
    (les["pdf-mut23h2u-280"].get("titleFr") or "").replace(chr(39), "\u2019")
    == "Leçon 26 : Ateliers de consolidation et d’application")

# ---- registre des savants (hand + llm)
sreg = json.load(open(SREG, encoding="utf-8"))
total = len(sreg.get("hand") or []) + len(sreg.get("llm") or {})
chk("registre savants ≥ 1198 (1199 après hand-set)", total >= 1198)

print(f"verify-ulumhadith2-pdf280 : {ok} PASS / {fail} ÉCHEC")
raise SystemExit(1 if fail else 0)

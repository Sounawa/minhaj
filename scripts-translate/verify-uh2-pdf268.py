#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Minhāj — Vérification de la leçon ulum-hadith-tanawi-2 / pdf-mut23h2u-268
(الدرس 14 — al-mardūd wa-aqsāmuh, p.74-77 du manuel
ulum-hadith-2-thanawi_text.pdf) : bornes p.74-77 par DOUBLE sondage (p.73 =
clôture de la leçon 13 activités pratiques, livrée R635 ; p.74 = bannière
ad-dars 14 + 3 objectifs + tamhīd + matn Ibn Ḥaǧar + gloses + istiḫlāṣ ;
p.75 = taḥlīl (2 causes du rejet) + al-muʿallaq définition luġa/istiṣilāḥ ;
p.76 = الفرق مع المعضل (achevée en tête) + الصور + الحكم + ahtadī wa-aqtadī
(Zuhrī, al-Ǧāmiʿ 1/7) ; p.77 = taqwīm 3 questions + istiṯmār (Ibn aṣ-Ṣalāḥ,
p.68) + iʿdād qiblī leçon 15 ; p.78 = ouverture leçon 15 « الحديث المرسل »
(matn « والثاني: المُرْسَلُ », sondage, non touchée, docId pdf-mut23h2u-269,
registre vide)) ; claim atomique r642-subagent-uh2-268 (takeover du claim
périmé, refresh ×3) ; extraction multicouche scripts-translate/uh2-extract-268.py
(tr-tmp/uh2-l268-raw.txt, pages 73-79, couche brute + couche fix mots
réinversés) + réutilisation légitime des couches R639 (pdftotext embed,
pymu, tesseract ara 300 dpi, 15 adjudications VLM ocr-p07X-*.txt) + lectures
de sondage R635 (read-p074-top) ; NOMBRES tranchés sur les couches et
l'image, jamais devinés : [Maqāyīs al-luġa, Ibn Fāris, 4/125] (suite visuelle
« 125/4 »), [al-Ǧāmiʿ li-aḫlāq ar-rāwī, al-Ḫaṭīb al-Baġdādī, 1/7] (suite
visuelle « 7/1 »), [Muqaddimat Ibn aṣ-Ṣalāḥ p.25] et [p.68] (confirmés VLM) ;
matn tranché « فالأول: المُعَلَّقُ » (bande dédiée ocr-p074-matn + tesseract
p.74 + double citation interne + cohérence leçon 15 « والثاني: المُرْسَلُ »)
contre le groupe illisible de la couche incorporée (consigné) ; artefacts
fantômes consignés (suite « 217156 », jeton GID, groupe TT, « ya-dullu »
fantôme) ; zéro āya, zéro arabe, zéro apostrophe droite.
Usage: python3 scripts-translate/verify-uh2-pdf268.py
"""
import json
import re

HTML = "/home/z/my-project/tr-tmp/lesson-uh2-pdf-mut23h2u-268-fr.html"
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
chk("h1 = titleFr pré-mappé « Leçon 14 : Le hadith rejeté (mardūd) et ses catégories »",
    hn.startswith("<h1>Leçon 14 : Le hadith rejeté (mardūd) et ses catégories"))
chk("h1 mentionne deuxième année", "deuxième année" in h[:500])
chk("h1 mentionne les deux causes du rejet", "les deux causes du rejet (ar-radd)" in h[:1500])
chk("h1 mentionne la chute et la critique", "as-saqaṭ" in h[:1500] and "at-taʿn" in h[:1500])
chk("h1 mentionne les noms des chutes (muʿallaq, mursal, munqaṭiʿ, muḍṭarib)",
    "al-muʿallaq" in h[:1800] and "al-mursal" in h[:1800] and "al-munqaṭiʿ" in h[:1800]
    and "al-muḍṭarib" in h[:1800])
chk("h1 mentionne la chute cachée (mudallis, mursal khafī)",
    "al-mudallis" in h[:1800] and "al-mursal al-ḫafī" in h[:1800])
chk("h1 mentionne Maqāyīs al-luġa et Ibn Fāris", "Maqāyīs al-luġa d’Ibn Fāris" in h[:2400])
chk("h1 mentionne Ibn aṣ-Ṣalāḥ et al-Buḫārī", "Ibn aṣ-Ṣalāḥ" in h[:3000] and "al-Buḫārī" in h[:3000])
chk("dl.lesson-meta présent", '<dl class="lesson-meta">' in h and "<dt>Source du cours</dt>" in h)
chk("item archive.org cité", "1_20220304_20220304_2251" in h)
chk("source locale citée", "ulum-hadith-2-thanawi_text.pdf" in h)
chk("bornes p.74-77 documentées", "pages 74 à 77" in h)
chk("p.73 clôture leçon 13 (R635)", "R635" in h and "pdf-mut23h2u-267" in h)
chk("p.78 leçon 15 sondée, non touchée, registre vide",
    "pdf-mut23h2u-269" in h and "registre vide" in h and "non touchée" in h)
chk("double sondage « jamais devinées »", "jamais devinées" in h)
chk("bannière : registre autorité + lectures divergentes consignées",
    "ad-dars 14" in h and "zéro devinette" in h and "consignées" in h)
chk("extraction dédiée uh2-extract-268.py citée", "uh2-extract-268.py" in h
    and "tr-tmp/uh2-l268-raw.txt" in h)
chk("couche fix mots réinversés citée", "mots réinversés" in h)
chk("réutilisation légitime des couches R639 citée", "tr-tmp/r639/" in h and "R639" in h)
chk("couches (incorporée, logique, OCR 300, vision) citées",
    "pdftotext" in h and "300 dpi" in h and "adjudications de vision" in h)
chk("lectures R635 relues avant emploi", "read-p074-top" in h)

# ---- nombres miroir tranchés
chk("Maqāyīs 4/125 tranché (suite visuelle « 125/4 »)",
    "tome 4, page 125" in hn and "125/4" in h)
chk("Ǧāmiʿ 1/7 tranché (suite visuelle « 7/1 »)",
    "tome 1, page 7" in hn and "7/1" in h)
chk("Muqaddimat Ibn aṣ-Ṣalāḥ p.25 consignée", "page\u202f25" in h or "page 25" in hn)
chk("Muqaddimat Ibn aṣ-Ṣalāḥ p.68 consignée", "page\u202f68" in h or "page 68" in hn)
chk("artefacts fantômes consignés (217156, GID, TT, ya-dullu)",
    "217156" in h and "GID" in h and "ya-dullu" in h)
chk("matn tranché : bande dédiée + tesseract + double citation interne + leçon 15",
    "ocr-p074-matn" in h and "et le deuxième" in h
    and "le mursal" in h and "tranchement documenté" in h)
chk("divergence de graphie (al-ʿallāq / al-muʿallaq) portée et documentée",
    "al-ʿallāq" in h and "telle qu’imprimée" in h)

# ---- objectifs
chk("objectif : causes du rejet", "les causes du rejet du ḥadīṯ" in hn)
chk("objectif : critique relative à la probité et à la maîtrise",
    "relatives à la probité (al-ʿadāla) de celles relatives à la maîtrise (aḍ-ḍabṭ)" in hn)
chk("objectif : éviter ce qui porte atteinte à la probité et à l’application parfaite",
    "porte atteinte à la probité et à l’application parfaite (al-iḥkām)" in hn)
chk("trois objectifs annoncés", "trois objectifs" in hn)

# ---- tamhīd
chk("tamhīd : fin du maqbūl, ouverture du mardūd",
    "l’accepté (al-maqbūl)" in hn and "il s’est mis à exposer l’autre partie, qui est le rejeté (al-mardūd)" in hn)
chk("tamhīd : double question (espèces de la chute / espèces de la critique)",
    "quelles sont les espèces de la chute dans la chaîne" in hn
    and "quelles sont les espèces de la critique portée sur le rapporteur" in hn)

# ---- matn
chk("matn : le rejeté n’est que d’une chute ou d’une critique",
    "il n’est que d’une chute (saqaṭ) ou d’une critique (taʿn)" in hn)
chk("matn : la chute au commencement (compilateur) ou à la fin après le Successeur",
    "du commencement de la chaîne, du côté du compilateur (muṣannif)" in hn
    and "de sa fin après le Successeur (tābiʿī)" in hn)
chk("matn : « et le premier est le muʿallaq »",
    "et le premier est le muʿallaq (al-muʿallaq)" in hn)

# ---- gloses
chk("glose : saqaṭ = omission dans la chaîne", "est l’omission dans la chaîne" in hn)
chk("glose : taʿn = cause du ǧarḥ, lance et parole",
    "porté l’attaque (ṭaʿana) avec la lance" in hn and "la critique (ṭaʿana) avec la parole" in hn)
chk("glose : muṣannif nom d’agent", "nom d’agent dérivé de «&nbsp;ṣannafa&nbsp;»" in h
    or "nom d’agent dérivé de « ṣannafa »" in hn)
chk("istiḫlāṣ : deux extractions", "tirer du texte les causes du rejet du ḥadīṯ" in hn
    and "espèces de la chute dans la chaîne" in hn)

# ---- taḥlīl : première cause
chk("cause 1 : noms selon la place — muʿallaq au commencement",
    "on le nomme muʿallaq (le suspendu)" in hn)
chk("cause 1 : mursal à la fin", "on le nomme mursal (le relâché)" in hn)
chk("cause 1 : munqaṭiʿ au milieu (un seul)", "on le nomme munqaṭiʿ (le tronqué)" in hn)
chk("cause 1 : muḍṭarib à deux chutes suivies", "on le nomme muḍṭarib (l’entremêlé)" in hn)
chk("cause 1 : deux rapporteurs sans se suivre = tronqué en deux places",
    "la chaîne est tronquée en deux places" in hn)
chk("cause 1 : chute apparente (4 noms) / chute cachée (mudallis, mursal khafī)",
    "apparente (ẓāhir)" in hn and "cachée (ḫafī)" in hn
    and "le mudallis (le fourbe) et le mursal caché (al-mursal al-ḫafī)" in hn)

# ---- taḥlīl : deuxième cause
chk("cause 2 : perte de la probité (6 items)",
    "le faible qui ment en son rapport (kadb)" in hn
    and "l’impie (fisq)" in hn and "l’innovateur (bidʿa)" in hn
    and "l’homme à l’identité inconnue (ǧahālat al-ʿayn)" in hn
    and "l’homme à l’état inconnu (ǧahālat al-ḥāl)" in hn)
chk("cause 2 : perte de la maîtrise (6 items)",
    "la multiplicité de l’erreur (al-ġalaṭ)" in hn and "l’inattention (al-ġafla)" in hn
    and "le présomptif (al-wahm)" in hn and "sūʾ al-ḥifẓ" in hn
    and "l’entremêlement (al-iḫtilāṭ)" in hn and "la divergence (al-muḫālafa)" in hn)

# ---- muʿallaq : définitions
chk("luġa : ism mafʿūl + chose suspendue à la chose haute",
    "nom d’objet (ism mafʿūl)" in hn and "la chose soit suspendue à la chose haute" in hn)
chk("luġa : renvoi Maqāyīs 4/125", "[Maqāyīs al-luġa (les pesées de la langue), d’Ibn Fāris, tome 4, page 125" in hn)
chk("istiṣilāḥ : un ou plusieurs omis au commencement de sa chaîne",
    "ce dont on a omis un ou plusieurs au commencement de sa chaîne" in hn)
chk("istiṣilāḥ : nommé par comparaison à la chose suspendue (partie haute)",
    "comparaison à la chose suspendue" in hn and "partie haute" in hn)

# ---- muʿallaq : différence avec le muḍṭarib
chk("فرق : ʿumūm wa-ḫuṣūṣ min waǧh",
    "inclusion générale et particulière sous un aspect (ʿumūm wa-ḫuṣūṣ min waǧh)" in hn)
chk("فرق : deux omis au début = muḍṭarib et muʿallaq",
    "on le dit muḍṭarib pour l’omission des deux, et on le dit aussi muʿallaq" in hn)
chk("فرق : muḍṭarib seul par deux du milieu ; muʿallaq seul par un du début",
    "se singularise par l’omission de deux hommes du milieu de la chaîne" in hn
    and "un seul homme est omis du commencement de la chaîne" in hn)

# ---- muʿallaq : figures
chk("figures : toute la chaîne omise (Messager de Dieu a dit ceci)",
    "que toute la chaîne soit omise — on dira alors, par exemple&nbsp;: le Messager de Dieu a dit ceci" in h
    or "que toute la chaîne soit omise" in hn)
chk("figures : sauf le Compagnon, ou Compagnon et Successeur (Abū Hurayra, Saʿīd b. al-Musayyib)",
    "Abū Hurayra a rapporté ceci" in hn and "Saʿīd b. al-Musayyib a dit d’après Abū Hurayra" in hn)
chk("figures : ajout à celui du dessus + divergence taʿlīq/tadlīs (naṣṣ, istiqrāʾ)",
    "un mudallis condamné pour cela" in hn and "par le texte (an-naṣṣ) ou par l’induction (al-istiqrāʾ)" in hn
    and "sinon c’est un taʿlīq" in hn)

# ---- muʿallaq : statut
chk("statut : mardūd par ignorance de l’état de l’omis (probité, maîtrise) + continuité",
    "l’ignorance où l’on est de l’état de l’omis" in hn
    and "la continuité de la chaîne (ittiṣāl as-sanad)" in hn)
chk("statut : si l’omis est connu par une autre voie, authenticité possible",
    "comme quand arrive son nommé par une autre voie" in hn
    and "les conditions de l’authenticité sont réunies" in hn)
chk("statut : « tous fiables » refusé par le ǧumhūr tant qu’il ne nomme pas",
    "tant qu’il ne les nomme pas" in hn and "fiable auprès de lui et non fiable auprès d’un autre" in hn)
chk("statut : ǧarḥ mutawahham préféré à taʿdīl ṣarīḥ",
    "la critique présumée (al-ǧarḥ al-mutawahham)" in hn
    and "la correction explicite (at-taʿdīl aṣ-ṣarīḥ)" in hn)
chk("Ibn aṣ-Ṣalāḥ : ǧazm (il a dit) = isād établi, omis pour l’abrègement",
    "avec l’assertion (al-ǧazm)" in hn and "sa chaîne est établie auprès de lui" in hn
    and "comme l’abrègement" in hn)
chk("Ibn aṣ-Ṣalāḥ : kayurwà = maqāl ; non assertif jugé après examen, assertif d’emblée",
    "on rapporte que&nbsp;» (kayurwà)" in h or "(kayurwà)" in hn
    and "comporte une critique (maqāl)" in hn
    and "jugé authentique d’emblée" in hn)
chk("renvoi [Muqaddimat Ibn aṣ-Ṣalāḥ, page 25] présent",
    "Muqaddimat Ibn aṣ-Ṣalāḥ (l’introduction d’Ibn aṣ-Ṣalāḥ), page" in hn)

# ---- ahtadī wa-aqtadī (Zuhrī)
chk("rubrique ahtadī wa-aqtadī", "Je m’inspire et j’inspire (ahtadī wa-aqtadī)" in hn)
chk("Zuhrī : science = éducation de Dieu, éducation du Prophète et de la communauté",
    "l’éducation (adab) de Dieu par laquelle il a éduqué son Prophète" in hn
    and "a éduqué par elle sa communauté" in hn)
chk("Zuhrī : dépôt (amāna) et preuve entre lui et Dieu",
    "le dépôt (amāna) de Dieu à son envoyé" in hn
    and "une preuve placée devant lui" in hn)
chk("renvoi [al-Ǧāmiʿ li-aḫlāq ar-rāwī, al-Ḫaṭīb al-Baġdādī, tome 1, page 7]",
    "al-Ǧāmiʿ li-aḫlāq ar-rāwī wa-ādāb as-sāmiʿ (la compilation des manières du rapporteur et des règles de l’auditeur), d’al-Ḫaṭīb al-Baġdādī, tome 1, page 7" in hn)

# ---- évaluation (3 items)
chk("évaluation : 3 questions", "trois questions auxquelles penser" in hn)
chk("évaluation : causes en résumé / deux figures / pourquoi mardūd",
    "les causes du rejet du ḥadīṯ en résumé" in hn
    and "je cite deux figures du ḥadīṯ suspendu" in hn
    and "pour quelle raison le ḥadīṯ suspendu est de la catégorie du rejeté" in hn)

# ---- exploitation (Ibn aṣ-Ṣalāḥ p.68 + 2 travaux)
chk("istiṯmār : trois causes du taʿlīq chez al-Buḫārī",
    "connu du côté des fiables auprès de la personne à laquelle il l’a suspendu" in hn
    and "de façon musnad et continue (musnad muttaṣil)" in hn
    and "aucun défaut de rupture (ḫalal al-inqiṭāʿ)" in hn)
chk("istiṯmār : renvoi page 68", "[Muqaddimat Ibn aṣ-Ṣalāḥ, page" in hn)
chk("istiṯmār : deux travaux (extraire les causes / groupes sur le Ṣaḥīḥ)",
    "sortir du texte les causes du taʿlīq chez al-Buḫārī" in hn
    and "les élèves se répartissent en groupes de travail" in hn
    and "ḥadīṯ suspendus chez l’imām al-Buḫārī dans son Ṣaḥīḥ" in hn)

# ---- préparation leçon suivante
chk("iʿdād : leçon 15 mursal", "Le hadith à transmetteur omis (mursal)" in hn)
chk("iʿdād : mursal vs mursal caché",
    "la différence entre le mursal (al-mursal) et le mursal caché (al-mursal al-ḫafī)" in hn)
chk("iʿdād : accepté ou rejeté", "de l’ordre de l’accepté ou du rejeté" in hn)
chk("iʿdād : marāsīl et balāġāt de Mālik dans le Muwaṭṭaʾ",
    "les marāsīl et les balāġāt de l’imām Mālik dans le Muwaṭṭaʾ" in hn
    and "les opinions des savants à leur sujet" in hn)

# ---- hygiène FR
chk("zéro caractère arabe", not re.search(r"[\u0600-\u06FF\u0750-\u077F\u08A0-\u08FF\uFB50-\uFDFF\uFE70-\uFEFF]", h))
chk("zéro apostrophe droite", "'" not in h)
chk("guillemets appariés", h.count("«") == h.count("»"))
chk("zéro double espace", "  " not in re.sub(r"&nbsp;|\n", "", h))
chk("zéro résidu placeholder", not re.search(r"XXX|TODO|【|____", h))
chk("balises appariées (h1/h2/h3/p/dl/dt/dd/strong)",
    h.count("<h1>") == h.count("</h1>") and h.count("<h2>") == h.count("</h2>")
    and h.count("<h3>") == h.count("</h3>") and h.count("<p>") == h.count("</p>")
    and h.count("<dl") == h.count("</dl>") and h.count("<dt>") == h.count("</dt>")
    and h.count("<dd>") == h.count("</dd>") and h.count("<strong>") == h.count("</strong>"))

# ---- registre : htmlFr posé, voisins intacts
reg = json.load(open(REG, encoding="utf-8"))
les = {str(d.get("docId", "")): d for d in reg["lessons"]}
chk("registre livre 2 : 27 entrées", len(reg["lessons"]) == 27)
chk("registre 266 intact (30 346 car)", len(les["pdf-mut23h2u-266"].get("htmlFr") or "") == 30346)
chk("registre 267 intact (25 238 car)", len(les["pdf-mut23h2u-267"].get("htmlFr") or "") == 25238)
chk("registre 269 non touché (htmlFr vide)", (les["pdf-mut23h2u-269"].get("htmlFr") or "") == "")
fr = les["pdf-mut23h2u-268"].get("htmlFr") or ""
if fr:
    chk("registre 268 = htmlFr posé (~22 000 car)", 20_000 <= len(fr) <= 26_000)
    chk("registre 268 == fichier livré", fr.strip() == h.strip())
else:
    chk("registre 268 encore vide (avant hand-set)", True)
chk("titleAr pré-mappé 268", les["pdf-mut23h2u-268"].get("titleAr") == "الدرس 14 : المردود وأقسامه")
chk("titleFr pré-mappé 268 aligné au h1",
    (les["pdf-mut23h2u-268"].get("titleFr") or "").startswith("Leçon 14 : Le hadith rejeté"))
chk("titleFr pré-mappé 269 intact", (les["pdf-mut23h2u-269"].get("titleFr") or "") == "Leçon 15 : Le hadith à transmetteur omis (mursal)")

print(f"verify-uh2-pdf268 : {ok} PASS / {fail} ÉCHEC")
raise SystemExit(1 if fail else 0)

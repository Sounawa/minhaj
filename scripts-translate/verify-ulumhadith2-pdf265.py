#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Minhāj — Vérification de la leçon ulum-hadith-tanawi-2 / pdf-mut23h2u-265
(الدرس 11 — muḥkam al-ḥadīṯ wa-muḫtalifuh, p.63-67 du manuel
ulum-hadith-2-thanawi_text.pdf) : bornes p.63-67 par DOUBLE sondage (p.62 =
exploitation + iʿdād de la leçon 10, artefacts r623-crops conservés ; p.63 =
bannière ad-dars 11 + 3 objectifs + tamhīd + matn Ibn Ḥaǧǧar + gloses ; p.66 =
taqwīm 3 items ; p.67 = ahtadī wa-aqtadī + أتأمل 2 questions + iʿdād leçon 12
nāsiḫ/mansūḫ ; p.68 = contenu leçon 12 non touché) ; claim atomique 16:21:56Z
(trace 1a19c7c0ffb4f845-cron-agent-loop-202611062237, refresh ×4) ; extraction
multicouche tr-tmp/r627/ (pdftotext + PyMuPDF + tesseract 300 dpi) + recadrages
700-2000 dpi tr-tmp/qa-crops-r627/ (44 clichés) + 30 lectures VLM ancrées
vlm-r627 (bornées, [illisible] admis, jamais de complétion) ; NOMBRES tranchés
sur l'image jamais devinés : [Lisān al-ʿarab 12/141 بتصرف] ; [at-Taqrīb
wa-t-taysīr, an-Nawawī, p. 20] (lecture an-Nūrī signalée) ; [al-Fawākih
ad-Dawānī 1/125] — الفتاوى/الفواكه tranché PAR LA COUCHE (lettres f-w-k-h) ;
[Fatḥ al-muġīṯ 3/220] (3 à gauche du slash) ; [Fatḥ al-muġīṯ 3/81] — imprimé
« 81/3 » lu en sens de lecture arabe, divergence 3/18 documentée ; Muḥammad b.
al-Ḥasan b. Fūrak porté tel qu'imprimé (canon : al-Ḥusayn, divergence
documentée) ; المحدثون tranché par la couche (3 lectures VLM divergentes) ;
verbe médian de la citation de Thawrī lu en divergence VLM ×6, structure
convergente rendue + divergence documentée ; hadiths d'exemple du muḥkam avec
références vertes portées telles qu'imprimées (bāb «لا تدخل الملائكة» du 1er
hadith, Muṣannaf ʿAbd ar-Razzāq du šiġār) ; exemple des deux traditions de
l'eau + réponse malikite du puits de Buḍāʿa ; rapprochement لا عدوى/المجذوم
en deux étages (généralité de la négation + sadd aḏ-ḏarāʾiʿ, حسماً للمادة) ;
zéro āya (nul recours au cache), zéro arabe, zéro apostrophe droite.
Usage: python3 scripts-translate/verify-ulumhadith2-pdf265.py
"""
import json
import re

HTML = "/home/z/my-project/tr-tmp/lesson-uh2-pdf-mut23h2u-265-fr.html"
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
chk("h1 = titleFr pré-mappé « Leçon 11 : Le hadith concordant (muḥkam) et le divergent (muḫtalif) »",
    hn.startswith("<h1>Leçon 11 : Le hadith concordant (muḥkam) et le divergent (muḫtalif)"))
chk("h1 mentionne deuxième année", "deuxième année" in h[:500])
chk("h1 mentionne les deux manières de vocaliser",
    "les deux manières de vocaliser" in h[:1500])
chk("h1 mentionne les deux traditions de l'eau",
    "l’exemple des deux traditions sur l’eau" in h[:2200])
chk("h1 mentionne les Fawākih ad-Dawānī", "Fawākih ad-Dawānī" in h[:2000])
chk("h1 mentionne Ibn Ḫuzayma et al-Balqīnī", "Ibn Ḫuzayma" in h[:2200] and "al-Balqīnī" in h[:2200])
chk("h1 mentionne la recommandation de Thawrī", "ath-Thawrī" in h[:2400])
chk("dl.lesson-meta présent", '<dl class="lesson-meta">' in h and "<dt>Source du cours</dt>" in h)
chk("item archive.org cité", "1_20220304_20220304_2251" in h)
chk("source locale citée", "ulum-hadith-2-thanawi_text.pdf" in h)
chk("bornes p.63-67 documentées", "pages 63 à 67" in h)
chk("p.62 leçon 10 non touchée (r623-crops conservés)", "r623-crops" in h and "pdf-mut23h2u-264" in h)
chk("p.68 leçon 12 non touchée", "pdf-mut23h2u-266" in h and "registre vide" in h)
chk("leçon 264 revendiquée par un autre ouvrier", "revendiquée par un autre ouvrier" in h)
chk("double sondage « jamais deviné »", "jamais deviné" in h)
chk("bannière concordante au registre et à la table des matières",
    "titleFr pré-mappé" in h and "table des matières" in h)
chk("badge ad-dars / 11 lu en image", "ad-dars / 11" in h)
chk("extraction multicouche tr-tmp/r627/ citée", "tr-tmp/r627/" in h)
chk("couches trois par page (incorporée, logique, OCR 300)",
    "texte incorporé" in h and "couche logique" in h and "300 points au pouce" in h)
chk("recadrages 700-2000 dpi qa-crops-r627 cités", "qa-crops-r627" in h and "2000 points au pouce" in h)
chk("lectures VLM ancrées vlm-r627 citées, bornées, anti-hallucination",
    "vlm-r627" in h and "[illisible]" in h and "aucune complétion de mémoire" in h)

# ---- nombres miroir tranchés
chk("référence Lisān al-ʿarab 12/141 rendue",
    "Lisān al-ʿarab d’Ibn Manẓūr, 12/141, avec adaptation" in hn)
chk("référence at-Taqrīb wa-t-taysīr p. 20 rendue + Nawawī",
    "at-Taqrīb wa-t-taysīr, de l’Imām an-Nawawī, page 20" in hn)
chk("lecture alternative an-Nūrī signalée", "an-Nūrī" in h)
chk("référence al-Fawākih ad-Dawānī 1/125 rendue",
    "al-Fawākih ad-Dawānī sur l’épître d’Ibn Abī Zayd al-Qayrawānī, 1/125" in hn)
chk("الفتاوى/الفواكه tranché par la couche, divergence documentée",
    "al-fatāwā" in h and "les fruits" in h and "c’est la couche qui a tranché" in h)
chk("référence Fatḥ al-muġīṯ 3/220 rendue (as-Saḫāwī)",
    "Fatḥ al-muġīṯ, commentaire de l’Alfiyya du ḥadīṯ d’al-ʿIrāqī, d’as-Saḫāwī, 3/220" in hn)
chk("référence Fatḥ al-muġīṯ 3/81 rendue + ordre visuel 81/3 documenté",
    "as-Saḫāwī, 3/81" in hn and "81/3" in h and "en sens de lecture arabe" in h)
chk("divergence 3/18 signalée", "3/18" in h)
chk("Muḥammad b. al-Ḥasan b. Fūrak porté tel qu'imprimé (canon al-Ḥusayn documenté)",
    "Muḥammad b. al-Ḥasan b. Fūrak" in hn and "Muḥammad b. al-Ḥusayn" in hn)
chk("المحدثون (les traditionnistes) tranché par la couche",
    "les traditionnistes" in h and "la couche a tranché" in h)
chk("verbe médian Thawrī : divergence documentée",
    "divergence" in h and "documentée ici même" in h)

# ---- objectifs
chk("objectif : connaître le muḥkam et le muḫtalif",
    "que je fasse connaissance avec le hadith concordant et le hadith divergent" in hn)
chk("objectif : distinguer", "que je distingue le concordant du divergent" in hn)
chk("objectif : mettre en pratique", "que je veille à mettre en pratique ce que je sais" in hn)
chk("trois objectifs annoncés", "trois objectifs" in hn)

# ---- tamhīd
chk("tamhīd : le hadith accepté préservé ou non de la contrariété",
    "il peut être préservé de toute contrariété (muʿāraḍa), et il peut ne pas l’être" in hn)
chk("tamhīd : double question finale (que nomme-t-on… ?)",
    "que nomme-t-on le hadith accepté préservé de la contrariété" in hn
    and "Que nomme-t-on celui qui a été contrarié par son semblable" in hn)

# ---- matn + gloses
chk("matn : citation Ibn Ḥaǧǧar complète",
    "s’il est préservé de la contrariété, c’est lui le concordant (al-muḥkam)" in hn
    and "s’il est contrarié par son semblable, alors, si le rapprochement (al-ǧamʿ) est possible, c’est lui le hadith divergent (al-muḫtalif)" in hn)
chk("glose : égal en acceptation, et en rang",
    "par ce qui lui est égal en acceptation" in hn and "en rang" in hn)
chk("glose : la contrariété = contradiction dans le sens",
    "la confrontation d’un hadith par un autre hadith qui le contredit dans le sens" in hn)
chk("développement : le fort n'est pas affecté par la contradiction du faible",
    "car le fort n’est pas affecté par la contradiction du faible" in hn)
chk("développement : rapprochement sans forcer le sens",
    "sans forcer le sens" in hn and "bi-ġayri taʿassuf" in hn)
chk("développement : الناسخ/المنسوخ renvoyé à la leçon suivante",
    "l’abrogeant (nāsiḫ), l’autre l’abrogé (mansūḫ)" in hn and "dont l’explication viendra" in hn)
chk("taḫlīṣ : deux tâches (définition + différence)",
    "que j’extraie du texte la définition du hadith concordant et du hadith divergent" in hn
    and "que j’extraie la différence entre eux" in hn)
chk("hésitation lexe/mathe/formulation documentée",
    "hésitation graphique" in h)

# ---- 1 muḥkam
chk("langue : nom d'objet de j'ai affermi + rendu parfait",
    "Nom d’objet (ism mafʿūl) de « j’ai affermi la chose » (aḥkimtu š-šayʾ)" in hn
    and "je l’ai rendue parfaite" in hn)
chk("langue : ni divergence ni trouble + Lisān",
    "ce qui ne comporte ni divergence ni trouble" in hn)
chk("terminologie : accepté préservé de la contrariété",
    "le hadith accepté préservé de la contrariété" in hn)
chk("exemple : les exemples sont nombreux, la contrariété rare",
    "la plupart des traditions n’ont pas de contradicteur, et la contrariété est rare" in hn)
chk("hadith 1 : les plus durement châtiés… imitation de la création",
    "Les plus durement châtiés au Jour de la Résurrection sont ceux qui imitent la création de Dieu, puissant et majestueux" in hn)
chk("hadith 1 : référence bāb des anges/chien portée telle qu'imprimée",
    "les anges n’entrent pas dans une demeure où se trouve un chien" in hn
    and "référence portée telle qu’imprimée" in hn)
chk("hadith 2 : prière sans pureté, aumône du butin",
    "Dieu n’agrée pas la prière sans pureté rituelle, ni l’aumône provenant du butin fraudé (ġulūl)" in hn)
chk("hadith 3 : commencez par le souper",
    "Lorsque le souper est servi et que la prière est appelée, commencez par le souper" in hn)
chk("hadith 4 : pas de šiġār en islam",
    "Pas de mariage d’échange (nišāʾ) appelé šiġār en islam" in hn)
chk("clôture : rien ne les contrarie, et il en est d'autres",
    "des traditions concordantes, que rien ne contrarie — et il en est bien d’autres" in hn)

# ---- 2 muḫtalif
chk("définition : accepté + contrariété du semblable + rapprochement possible",
    "le hadith accepté contrarié par son semblable, le rapprochement étant possible" in hn)
chk("les deux vocalisations : i bref (nom d'agent) et a bref (source en mīm)",
    "un i bref sous la seconde radicale" in hn and "nom d’agent" in hn
    and "un a bref" in hn and "source en mīm (maṣdar mīmī)" in hn)
chk("premier sens : suspendre / abroger / préférer (Taqrīb)",
    "qu’on suspende le jugement entre elles, ou qu’on tienne l’une pour abrogeante de l’autre, ou qu’on préfère l’une à l’autre" in hn)
chk("second sens : contrariété survenue en apparence",
    "la contrariété et la divergence survenues entre deux traditions ou davantage en apparence" in hn)
chk("conclusion : le hadith lui-même / le fait même",
    "la définition vise le hadith lui-même" in hn
    and "elle vise le fait même de la contradiction" in hn)
chk("sections : deux, rapprochement possible s'impose",
    "Le hadith divergent est de deux sections" in hn
    and "le rapprochement s’impose, et l’on ne recourt ni à la contrariété ni à l’abrogation" in hn)
chk("type 1 : antérieur/postérieur connus → abrogation",
    "que l’antérieur et le postérieur soient connus" in hn
    and "le postérieur est l’abrogeant de l’antérieur" in hn)
chk("type 2 : tri préférentiel (rāǧiḥ/marǧūḥ)",
    "la voie du tri préférentiel (maslak at-tarǧīḥ)" in hn
    and "nous retenons le préféré (rāǧiḥ) et nous délaissons le dépréférencé (marǧūḥ)" in hn)
chk("précaution : la contrariété n'existe qu'au regard de l'examinant",
    "qu’au regard de ce qui est apparu à celui qui les examine" in hn
    and "possible pour un savant, et qu’il échappe à un autre" in hn)

# ---- exemple de l'eau
chk("tradition 1 : rien ne le rend impur sauf altération des qualités",
    "Rien ne le rend impur — sinon ce qui vient à bout de son odeur, de son goût ou de sa couleur" in hn)
chk("tradition 1 : quatre Sunan / Ibn Māǧa",
    "rapportée par les auteurs des quatre Sunan" in hn and "Sunan d’Ibn Māǧa" in hn)
chk("tradition 2 : deux outres",
    "lorsque l’eau atteint deux outres (qullatayn), elle ne porte pas l’impureté" in hn)
chk("chacune restreint la généralité de l'autre",
    "Chacune des deux restreint donc la généralité de l’autre" in hn)
chk("réponse malikite : changement même en moindre quantité",
    "l’opinion répandue (al-mašhūr) chez Mālik" in hn
    and "ne devient impure que par le changement, fût-ce en moindre quantité que deux outres" in hn)
chk("puits de Buḍāʿa : chiffons, cadavres, chiens",
    "le récit du puits de Buḍāʿa" in hn
    and "des chiffons de menstrues, des cadavres de bêtes de somme et des chiens" in hn)
chk("hadith des deux outres affaibli par Mālik et d'autres",
    "faute d’authenticité, en raison de l’affaiblissement qu’en ont fait Mālik et d’autres" in hn)

# ---- rapprochement contagion
chk("Ibn aṣ-Ṣalāḥ : pas de contagion + fuir le lépreux comme le lion",
    "pas de contagion sans le fait de Dieu, pas de présage" in hn
    and "fuis le lépreux comme tu fuirais le lion" in hn)
chk("voie du rapprochement : les maladies ne transmettent rien de leur nature",
    "ces maladies ne transmettent rien de leur nature propre" in hn
    and "une cause de transmission de son mal" in hn)
chk("raffinement : rien ne transmet rien + qui a donc infecté le premier ?",
    "rien ne transmet rien" in hn and "et qui a donc infecté le premier" in hn)
chk("obstruction des voies de dommage + trancher la matière",
    "l’obstruction des voies de dommage (sadd aḏ-ḏarāʾiʿ)" in hn
    and "pour trancher la matière" in hn and "et Dieu sait mieux" in hn)

# ---- 3 les livres
chk("intro : les traditionnistes ont composé des livres précieux",
    "ont composé, sur la science du hadith divergent, des livres précieux" in hn)
chk("aš-Šāfiʿī : premier livre, flambeau pour ceux qui viennent",
    "l’Imām aš-Šāfiʿī" in hn and "le premier livre composé dans cet art" in hn
    and "un flambeau (nibrās)" in hn)
chk("aṭ-Ṭaḥāwī : traditions à l'apparence difficile, portée plus large",
    "muškil al-āṯār" in hn and "Abū Ǧaʿfar Aḥmad b. Muḥammad b. Salama aṭ-Ṭaḥāwī" in hn
    and "d’une portée plus large que les mutuellement contrariées" in hn)
chk("Ibn Fūrak : l'exposé du hadith équivoque",
    "l’exposé du hadith équivoque et sa clarification" in hn
    and "théoricien des sources de droit et dialecticien (mutakallim)" in hn)

# ---- as-Saḫāwī + Ibn Ḫuzayma + al-Balqīnī
chk("as-Saḫāwī : des plus importants, toutes les écoles y ont recours",
    "il est des plus importants des genres" in hn
    and "toutes les écoles des savants y ont recours" in hn)
chk("as-Saḫāwī : imām réunissant les deux métiers",
    "un imām réunissant les deux métiers" in hn
    and "le ḥadīṯ et le droit (fiqh), plongeant dans les sens subtils" in hn)
chk("Ibn Ḫuzayma : je ne connais pas deux traditions authentiques qui se contredisent",
    "l’imām des imāms, Abū Bakr Ibn Ḫuzayma" in hn
    and "je ne connais pas deux traditions authentiques qui se contredisent" in hn)
chk("al-Balqīnī : la porte des interprétations",
    "al-Balqīnī" in hn and "la porte des interprétations" in hn
    and "la plus grande partie de la porte s’ouvrirait" in hn)

# ---- ahtadī wa-aqtadī
chk("rubrique ahtadī wa-aqtadī", "Je m’inspire et j’inspire (ahtadī wa-aqtadī)" in hn)
chk("citation Thawrī : apprenez, préservez, transmettez, répandez",
    "Apprenez ce hadith" in hn and "préservez-le" in hn
    and "transmettez-le" in hn and "répandez-le" in hn)
chk("citation Thawrī : renvoi Fatḥ al-muġīṯ 3/220",
    "as-Saḫāwī, 3/220" in hn)
chk("parcours complet : cinq verbes répondant aux objectifs",
    "apprendre, préserver, transmettre, pratiquer, répandre" in hn)

# ---- évaluation
chk("évaluation : 3 items", "Trois items" in hn)
chk("évaluation : définir muḥkam/muḫtalif",
    "que je définisse le hadith concordant et le hadith divergent" in hn)
chk("évaluation : citer les sections",
    "que je cite les sections du hadith divergent" in hn)
chk("évaluation : premier qui composa",
    "que je cite le premier qui composa" in hn)

# ---- exploitation
chk("exploitation : importance de la science",
    "que j’expose l’importance de la science du hadith divergent" in hn)
chk("exploitation : pourquoi les deux métiers + connaissance des sens",
    "pourquoi celui qui examine le hadith divergent a-t-il besoin des deux métiers" in hn
    and "de la connaissance des sens" in hn)
chk("exploitation : mot dégradé documenté (les sens / le commun)",
    "d’impression dégradée" in h and "le commun" in h)
chk("exploitation : réponse déduite (ḥadīṯ + droit + sens)",
    "le métier du ḥadīṯ lui donne les deux traditions" in hn
    and "le métier du droit lui donne les sens" in hn)

# ---- préparation leçon suivante
chk("leçon suivante nommée (nāsiḫ/mansūḫ)",
    "l’abrogeant (nāsiḫ) et l’abrogé (mansūḫ)" in hn)
chk("préparation : concept de l'abrogation et comment on le connaît",
    "le concept de l’abrogation (an-nasḫ) et ce par quoi on le connaît" in hn)
chk("préparation : différence abrogeant/abrogé",
    "la différence entre l’abrogeant et l’abrogé" in hn)
chk("préparation : 2 consignes", "deux consignes" in h)

# ---- hygiène FR
chk("zéro caractère arabe", not re.search(r"[\u0600-\u06FF\u0750-\u077F\u08A0-\u08FF\uFB50-\uFDFF\uFE70-\uFEFF]", h))
chk("zéro apostrophe droite", "'" not in h)
chk("guillemets appariés", h.count("«") == h.count("»"))
chk("zéro double espace", "  " not in re.sub(r"&nbsp;|\n", "", h))
chk("zéro résidu placeholder", not re.search(r"XXX|TODO|【|____", h))
chk("zéro artefact de réflexion", not re.search(r"hmm|non plus|plutôt —", h))
chk("zéro ponctuation verticale résiduelle", not re.search(r"[\uFE10-\uFE19\uFE30-\uFE4F\uFF01-\uFF65]", h))
chk("balises appariées (h1/h2/h3/p/dl/dt/dd)",
    h.count("<h1>") == h.count("</h1>") and h.count("<h2>") == h.count("</h2>")
    and h.count("<h3>") == h.count("</h3>") and h.count("<p>") == h.count("</p>")
    and h.count("<dl") == h.count("</dl>") and h.count("<dt>") == h.count("</dt>")
    and h.count("<dd>") == h.count("</dd>"))

# ---- registre : htmlFr posé, voisins intacts
reg = json.load(open(REG, encoding="utf-8"))
les = {str(d.get("docId", "")): d for d in reg["lessons"]}
chk("registre livre 2 : 27 entrées", len(reg["lessons"]) == 27)
chk("registre 263 intact (33 055 car)", len(les["pdf-mut23h2u-263"].get("htmlFr") or "") == 33055)
chk("registre 260 intact (29 786 car)", len(les["pdf-mut23h2u-260"].get("htmlFr") or "") == 29786)
chk("registre 261 intact (28 693 car)", len(les["pdf-mut23h2u-261"].get("htmlFr") or "") == 28693)
chk("registre 262 intact (27 968 car)", len(les["pdf-mut23h2u-262"].get("htmlFr") or "") == 27968)
chk("registre 264 non touché (htmlFr vide)", (les["pdf-mut23h2u-264"].get("htmlFr") or "") == "")
chk("registre 266 non touché (htmlFr vide)", (les["pdf-mut23h2u-266"].get("htmlFr") or "") == "")
fr = les["pdf-mut23h2u-265"].get("htmlFr") or ""
if fr:
    chk("registre 265 = htmlFr posé (~32 000 car)", 28_000 <= len(fr) <= 36_000)
    chk("registre 265 == fichier livré", fr.strip() == h.strip())
else:
    chk("registre 265 encore vide (avant hand-set)", True)
chk("titleAr pré-mappé 265", les["pdf-mut23h2u-265"].get("titleAr") == "الدرس 11 : محكم الحديث ومختلفه")
chk("titleFr pré-mappé 265 aligné au h1",
    (les["pdf-mut23h2u-265"].get("titleFr") or "").replace("'", "’").startswith("Leçon 11 : Le hadith concordant"))
reg1 = json.load(open(REG1, encoding="utf-8"))
l1 = {str(d.get("docId", "")): d for d in reg1["lessons"]}
chk("registre livre 1 : 141 intact (24 319 car)", len(l1["pdf-mut23h2r-141"].get("htmlFr") or "") == 24319)
chk("registre livre 1 : 140 intact (16 018 car)", len(l1["pdf-mut23h2r-140"].get("htmlFr") or "") == 16018)

print(f"verify-ulumhadith2-pdf265 : {ok} PASS / {fail} ÉCHEC")
raise SystemExit(1 if fail else 0)

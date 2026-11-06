#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Minhāj — Vérification de la leçon ulum-hadith-tanawi-2 / pdf-mut23h2u-263
(الدرس 9 — al-ḥadīṯ al-maʿrūf wa-l-munkar, p.52-56 du manuel
ulum-hadith-2-thanawi_text.pdf) : bornes p.52-56 par DOUBLE sondage (p.52 =
bannière الدرس 9 + 3 objectifs + tamhīd + 3 questions + matn ; p.56 = boîte
أتأمل النص 2 questions + iʿdād qablī 2 consignes ; p.57 = bannière leçon 10
الاعتبار والمتابعات والشواهد) ; WIP sous-agent interrompu recoupé (couches
p051-p058 + 26 recadrages ADJ1-ADJ26, claim expiré 69 min, takeover légitime,
registre 263 vide) ; recadrages complémentaires 1200-1800 dpi ADJ27-ADJ50 +
quatre lectures VLM ancrées vlm-r622 ; nombres pdftotext INVERSÉS tranchés
(65→p. 560 Mufradāt, 5/674→5/476 Maqāyīs, 576→2/675 Nukat, 5/953→5/359 ʿIlal,
3:8→p. 338 Muqaddima, 86→2/680 Nukat, 1141→p. 141 Kifāya ; 1/65 Nawawī porté
tel qu'imprimé) ; matn Ibn Ḥaǧar + gloses tranchées image directe ; fin
définition munkar rétablie (ADJ34) ; Nukat quote chevauchant p.53-54 (ADJ18 +
ADJ19) ; exemple isnād Ḥabīb b. Ḥabīb frère de Ḥamza az-Zayyāt le muqriʾ
(ADJ27 + recoupement šarḥ an-Naḫba en ligne, vlm «aḍ-ḍarīr» récusé) ; hadith
«quiconque établit la prière... honore l'hôte, entre au Paradis» (ADJ37,
«wa-qarrā ḍ-ḍīf daḫala l-ǧanna» rétabli) ; hadith du bouillon de dattes
(ADJ8/ADJ37, citation imprimée abrégée) ; commentaire Ibn Ḥaǧar Hišām b. Saʿd
(ADJ9/13/14/15/21/41, «fī l-mawāqiʿ» porté tel qu'imprimé, shamela 8316/653
concordant mot à mot, «al-mawāqīt» vlm unique récusé) ; wa-ḥāṣil al-qawl
(ADJ10/ADJ31b, Muqaddima p. 338) ; Khaṭīb al-Kifāya p. 141 (ADJ11/ADJ43/ADJ47b)
; quote Muslim variante muqaddima «al-ḥifẓ wa-r-riḍā... mahrūr» (ADJ12/ADJ40 +
shamela 36147/51, emploi standard al-ḥifẓ wa-ḍ-ḍabṭ documenté en divergence) ;
أتأمل 2 items (ADJ24/ADJ44) ; iʿdād 2 consignes (ADJ49/ADJ50 + VLM double) ;
deux hadiths prophétiques rendus, zéro āya, zéro arabe, zéro apostrophe droite,
zéro doublon.
Usage: python3 scripts-translate/verify-ulumhadith2-pdf263.py
"""
import json
import re

HTML = "/home/z/my-project/tr-tmp/lesson-uh2-pdf-mut23h2u-263-fr.html"
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
chk("h1 = titleFr pré-mappé « Leçon 9 : Le hadith reconnu (maʿrūf) et le méconnu (munkar) »",
    hn.startswith("<h1>Leçon 9 : Le hadith reconnu (maʿrūf) et le méconnu (munkar)"))
chk("h1 mentionne deuxième année", "deuxième année" in h[:500])
chk("h1 mentionne les deux sortes de la méconnaissance",
    "les deux sortes de la méconnaissance" in h[:1500])
chk("dl.lesson-meta présent", '<dl class="lesson-meta">' in h and "<dt>Source du cours</dt>" in h)
chk("item archive.org cité", "1_20220304_20220304_2251" in h)
chk("source locale citée", "ulum-hadith-2-thanawi_text.pdf" in h)
chk("bornes p.52-56 documentées", "pages 52 à 56" in h)
chk("p.47-51 leçon 8 non touchée", "pdf-mut23h2u-262" in h and "non touché" in h)
chk("p.57+ leçon 10 non touchée", "pdf-mut23h2u-264" in h and "non touché" in h)
chk("double sondage « jamais devinées »", "jamais devinées" in h)
chk("bannière concordante au registre et à la table des matières",
    "titleAr pré-mappé" in h and "table des matières" in h)
chk("extraction multicouche tr-tmp/r622/ citée", "tr-tmp/r622/" in h)
chk("tessdata dépôt documenté", "scripts-translate/tessdata" in h)
chk("couches logiques p052-pymu à p056-pymu citées",
    "p052-pymu" in h and "p056-pymu" in h)
chk("WIP sous-agent interrompu recoupé", "WIP de la passe sous-agent interrompue" in h
    and "vingt-six recadrages" in hn)
chk("claim expiré 69 min + takeover légitime", "69 min" in hn and "takeover légitime" in hn)
chk("recadrages complémentaires ADJ27-ADJ50 cités", "ADJ27" in hn and "ADJ50" in hn)
chk("lectures VLM ancrées vlm-r622 citées", "vlm-r622" in hn and "anti-hallucination" in hn)
chk("inversion 65→p. 560 documentée", "« 65 »" in hn and "p. 560" in hn)
chk("Mufradāt p. 560 rendue (entrée ʿ-r-f)",
    "al-Mufradāt fī ġarīb al-Qurʾān (les mots à sens unique du Coran) d’ar-Rāġib al-Aṣfahānī, p. 560" in hn)
chk("inversion 5/674→5/476 documentée", "5/674" in hn and "t. 5, p. 476" in hn)
chk("inversion 576→2/675 documentée", "576" in hn and "t. 2, p. 675" in hn)
chk("inversion 5/953→5/359 documentée", "5/953" in hn and "t. 5, p. 359" in hn)
chk("renvoi 3:8→p. 338 documenté (Muqaddima)", "3:8" in hn and "p. 338" in hn)
chk("inversion 86→2/680 documentée", "« 86 »" in hn and "t. 2, p. 680" in hn)
chk("renvoi 1141→p. 141 documenté (Kifāya)", "1141" in hn and "p. 141" in hn)
chk("citation Nawawī 1/65 portée telle qu'imprimée",
    "t. 1, p. 65" in hn and "telle qu’imprimée" in hn)
chk("mécanisme inversion élucidé (miroir, jamais devinée)", "INVERSÉS EN MIROIR" in hn
    and "jamais devinée" in hn)
chk("mawāqiʿ porté tel qu'imprimé + recoupement shamela 8316",
    "fī l-mawāqiʿ" in hn and "8316" in hn and "al-mawāqīt" in hn)
chk("li-aṯarih porté tel qu'imprimé (Mufradāt)", "li-aṯarih" in hn)
chk("variante muqaddima Muslim recoupée (shamela 36147)",
    "36147" in hn and "al-ḥifẓ wa-ḍ-ḍabṭ" in hn)
chk("vlm « aḍ-ḍarīr » récusé (Ḥamza az-Zayyāt muqriʾ)",
    "aḍ-ḍarīr" in hn and "(al-muqriʾ)" in hn and "Zayyāt" in hn)

# ---- objectifs
chk("objectif : concept maʿrūf/munkar, divisions, statut",
    "le concept du hadith méconnu (al-munkar) et du hadith reconnu (al-maʿrūf), leurs divisions" in hn)
chk("objectif : relation munkar/šāḏḏ", "la relation (al-ʿalāqa) entre le méconnu et l’anomal" in hn)
chk("objectif : haute ambition et assiduité",
    "d’une haute ambition et de l’assiduité dans la quête de la science" in hn)
chk("trois objectifs", "trois buts" in hn)
chk("triple question du tamhīd", "triple question" in hn
    and "quelle est l’utilité de la distinction" in hn)

# ---- tamhīd
chk("tamhīd : transmetteurs pas d'un seul rang",
    "ne sont pas d’un seul rang, quant à la déclaration de fiabilité et au reproche" in hn)
chk("tamhīd : taḥammul et adāʾ", "la prise du hadith (at-taḥammul) et à sa remise (al-adāʾ)" in hn)
chk("tamhīd : contradiction fiable/plus fiable ≠ faible/fiable",
    "entre un fiable et un plus fiable, elle diffère de la contradiction entre un faible et un fiable" in hn)

# ---- matn + fahm
chk("matn : citation Ibn Ḥaǧar complète",
    "Et avec la faiblesse, le prédominant est le reconnu (al-maʿrūf), et son contraire est le méconnu (al-munkar)" in hn)
chk("glose : ḍaʿf/ṣaʿf = contraire de la force",
    "la faiblesse (aḍ-ḍaʿf) et la débilité (aṣ-ṣaʿf) — le contraire de la force" in hn)
chk("glose : rāǧiḥ = fort en poids, peser et examiner",
    "le fort en poids, et peser (raǧaḥa) une chose de sa main" in hn
    and "examiné ce qui s’incline en elle" in hn)
chk("takhlaṣ : deux tâches", "extraire du texte la définition du hadith reconnu et du hadith méconnu" in hn)

# ---- 1 maʿrūf
chk("langue : Mufradāt citation complète (li-aṯarih, aḫṣaṣ, inkār)",
    "la saisie de la chose par la réflexion et la méditation quant à son effet" in hn
    and "il est plus spécifique que la science (al-ʿilm), et son contraire est le rejet (al-inkār)" in hn)
chk("terminologie : maqbūl contredisant le faible + convention savants",
    "ce que rapporta le transmetteur accepté (al-maqbūl) en contredisant un transmetteur faible" in hn
    and "par convention des savants du hadith" in hn)
chk("exemple renvoyé à l'illustration du munkar",
    "viendra l’exposé de l’exemple du reconnu au moment de l’illustration du méconnu" in hn)

# ---- 2 munkar
chk("langue : racine n-k-r + cœur/langue + Maqāyīs 5/476",
    "il a nié la chose et l’a méconnue" in hn and "d’Ibn Fāris, t. 5, p. 476" in hn)
chk("terminologie : faible contredisant le fiable/les fiables",
    "ce que rapporta le faible en contredisant ce que rapporta le fiable ou les fiables" in hn)
chk("terminologie : variante des anciens (isolement seul)",
    "chez la plupart des anciens, on l’employait pour tout hadith étranger auquel un rapporteur s’isole" in hn
    and "que son rapporteur soit fiable ou faible" in hn)
chk("fin définition : contradiction + faiblesse (ADJ34)",
    "lorsque la contradiction s’accompagne de la faiblesse, la version prédominante est dite reconnue" in hn)

# ---- 3 relation šāḏḏ/munkar
chk("relation : ʿumūm wa-ḫuṣūṣ min waǧh",
    "général et spécifique d’un point de vue" in hn and "ʿumūm wa-ḫuṣūṣ min waǧh" in hn)
chk("relation : réunion dans la contradiction, division des rapporteurs",
    "réunion dans l’exigence de la contradiction, et division" in hn
    and "le rapporteur de l’anomal est fiable ou véridique" in hn
    and "le rapporteur du méconnu est faible" in hn)
chk("citation Nukat complète (mustūr, muḍaʿḍaf, sans mutābaʿa ni šāhid)",
    "lorsqu’un inconnu, ou un homme décrit par la mauvaise conservation de la mémoire" in hn
    and "qui n’a ni suivi (mutābaʿa) ni témoin (šāhid)" in hn
    and "l’isolement absolu ou l’isolement avec la qualification de contradiction" in hn)
chk("citation Nukat chevauchant p.53-54 recoupée aux deux bordures",
    "à cheval sur les pages 53 et 54" in hn)

# ---- 4 divisions
chk("divisions : isnād (addition, soustraction, changement, fabrication)",
    "par l’addition dans l’isnād, ou la soustraction de lui, ou son changement, ou la fabrication en lui" in hn)
chk("exemple isnād : voie Ḥabīb b. Ḥabīb frère de Ḥamza az-Zayyāt muqriʾ",
    "par la voie de Ḥabīb b. Ḥabīb — le frère de Ḥamza az-Zayyāt le maître-récitateur (al-muqriʾ)" in hn)
chk("exemple isnād : chaîne Abū Isḥāq → al-ʿAyzār b. Ḥurayṯ → Ibn ʿAbbās",
    "d’Abū Isḥāq, d’al-ʿAyzār b. Ḥurayṯ, d’Ibn ʿAbbās" in hn)
chk("hadith prophétique complet (prière, zakāt, pèlerinage, jeûne, hôte)",
    "Quiconque établit la prière, donne la zakāt, accomplit le pèlerinage, jeûne, et honore l’hôte, entre au Paradis" in hn)
chk("renvoi al-ʿIlal 5/359 + recoupement šarḥ an-Naḫba",
    "al-ʿIlal (les défauts) d’Ibn Abī Ḥātim, t. 5, p. 359" in hn and "d’al-Ḫuḍayr" in hn)
chk("Abū Ḥātim : munkar car les fiables le rapportent mawqūfan, version maʿrūf",
    "l’ont rapporté d’Abū Isḥāq à l’état d’arrêt (mawqūf), et c’est là la version reconnue" in hn)
chk("Abū Zurʿa : en réalité mawqūf d'Ibn ʿAbbās",
    "il n’est en réalité que la parole arrêtée d’Ibn ʿAbbās" in hn)
chk("matn : quatre objets (sens, formulation, additions, déformation)",
    "la néciation du sens, la faiblesse de la formulation, l’addition d’expressions inconnues, la déformation et l’altération" in hn)
chk("exemple matn : isnād Ǧaʿfar b. Musāfir → Ibn Abī Fudayk → Hišām b. Saʿd → Ibn Šihāb → Abū Salama → Abū Hurayra",
    "Ǧaʿfar b. Musāfir nous a rapportés" in hn and "Ibn Abī Fudayk nous a rapportés" in hn
    and "Hišām b. Saʿd nous a rapportés, d’Ibn Šihāb, d’Abū Salama b. ʿAbd ar-Raḥmān, d’Abū Hurayra" in hn)
chk("hadith bouillon : ʿaraq, quinze sāʿ, mange/jeûne/demande pardon",
    "un bouillon (ʿaraq) dans lequel il y avait des dattes, quinze sāʿ" in hn
    and "mange, toi et les gens de ta maison, jeûne un jour, et demande pardon à Dieu" in hn)
chk("renvoi Abū Dāwūd bāb kaffāra Ramadan complet",
    "bāb kaffārat man atā ahlahu fī Ramaḍān (chapitre de l’expiation de celui qui a eu des relations avec sa femme en Ramadan)" in hn)
chk("commentaire : Abū ʿAwāna « il s'est trompé » + Ibn Abī ʿAdī manākīr",
    "Hišām b. Saʿd s’est trompé" in hn and "compté parmi ses hadiths méconnus (manākīr)" in hn)
chk("commentaire : al-Ḫalīlī ḥuffāẓ + Ḥumayd",
    "les gardiens de la mémoire (al-ḥuffāẓ) ont déclaré méconnu son hadith" in hn
    and "az-Zuhrī ne l’a rapporté que de Ḥumayd" in hn)
chk("commentaire : Wākiʿ munqaṭiʿ + Abū Zurʿa ar-Rāzī sitr",
    "de façon interrompue (munqaṭiʿ)" in hn
    and "Wākiʿ a voulu voiler Hišām b. Saʿd en écartant Abū Salama" in hn)

# ---- wa-ḥāṣil al-qawl
chk("wa-ḥāṣil : isolement sujet à examen + šāḏḏ mardūd si contradiction",
    "avec une chose sujette à examen" in hn
    and "il sera, par son isolement, anomal (šāḏḏ), rejeté (mardūd)" in hn)
chk("wa-ḥāṣil : examine de l'isolé (ʿadl, ḥāfiẓ, itqān, ḍabṭ)",
    "s’il est probe, mémorisateur, digne de confiance par l’accomplissement et la maîtrise de sa mémoire" in hn)
chk("wa-ḥāṣil : khārim/muzḥziḥ hors du champ du ṣaḥīḥ",
    "son isolement l’entamera, l’ébranlera hors du domaine de l’authentique" in hn)
chk("wa-ḥāṣil : degrés variés + istḥsān si proche du ḥāfiẓ + rejet si éloigné",
    "descend ensuite en degrés variés selon l’état du rapporteur" in hn
    and "son isolement fait que son hadith est jugé excellent" in hn
    and "relève du genre de l’anomal méconnue (aš-šāḏḏ al-munkar)" in hn)
chk("renvoi Muqaddima p. 338 rendu",
    "Muqaddimat Ibn aṣ-Ṣalāḥ (l’introduction d’Ibn aṣ-Ṣalāḥ), p. 338" in hn)

# ---- ahtadī wa-aqtadī
chk("rubrique ahtadī wa-aqtadī", "Je m’inspire et j’inspire (ahtadī wa-aqtadī)" in hn)
chk("al-Ḫaṭīb : citation complète (ġarīb, munkar sans maʿrūf, ṣaḥīḥ évité)",
    "les livres de l’étranger (al-ġarīb) au détriment du célèbre" in hn
    and "l’audition du méconnu au détriment du reconnu" in hn
    and "l’authentique est devenu, pour la plupart d’entre eux, un texte à éviter" in hn
    and "les états des transmetteurs et leur rang" in hn)
chk("renvoi al-Kifāya p. 141 rendu",
    "al-Kifāya fī ʿilm ar-riwāya (le suffisant en science de la transmission) d’al-Ḫaṭīb al-Baġdādī, p. 141" in hn)

# ---- évaluation
chk("évaluation : 2 activités", "deux activités" in hn)
chk("évaluation : définir le maʿrūf", "définir le hadith reconnu" in hn)
chk("évaluation : différence šāḏḏ/munkar",
    "exposer la différence entre l’anomal et le méconnu" in hn)

# ---- exploitation
chk("exploitation : citation Muslim complète (marque du méconnu)",
    "La marque du méconnu dans le hadith du muḥaddiṯ" in hn
    and "la narration d’autrui parmi les gens de la conservation et de l’agrément (al-ḥifẓ wa-r-riḍā)" in hn
    and "ou qu’elle ne l’atteint presque pas" in hn
    and "son hadith est un hadith délaissé (mahrūr), non accepté" in hn)
chk("exploitation : renvoi Ṣaḥīḥ Muslim šarḥ Nawawī 1/65",
    "Ṣaḥīḥ Muslim avec le šarḥ d’an-Nawawī, t. 1, p. 65" in hn)
chk("exploitation : deux questions",
    "extraire du dire de l’imām Muslim ce par quoi l’on reconnaît le méconnu" in hn
    and "l’importance de la comparaison entre les narrations du hadith" in hn
    and "la transmission (ar-riwāya) et la compétence critique (ad-dirāya)" in hn)
chk("exploitation : marque opérationnelle (confrontation des voies)",
    "elle se teste en confrontant les voies" in hn)

# ---- préparation leçon suivante
chk("leçon suivante nommée (iʿtibār, mutābaʿāt, šawāhid)",
    "La prise en compte (iʿtibār), les chaînes concordantes (mutābaʿāt) et les témoins (šawāhid)" in hn)
chk("préparation : concept mutābaʿāt/šawāhid",
    "le concept des chaînes concordantes (al-mutābaʿāt) et des témoins (aš-šawāhid)" in hn)
chk("préparation : exemples šawāhid/mutābaʿāt",
    "des exemples de témoins et de chaînes concordantes" in hn)
chk("préparation : 2 consignes", "deux consignes" in h)

# ---- hygiène FR
chk("zéro caractère arabe", not re.search(r"[\u0600-\u06FF\u0750-\u077F\u08A0-\u08FF\uFB50-\uFDFF\uFE70-\uFEFF]", h))
chk("zéro apostrophe droite", "'" not in h)
chk("guillemets appariés", h.count("«") == h.count("»"))
chk("zéro double espace", "  " not in re.sub(r"&nbsp;|\n", "", h))
chk("zéro résidu placeholder", not re.search(r"XXX|TODO|【|____", h))
chk("zéro artefact de réflexion", not re.search(r"hmm|non plus|plutôt —", h))
chk("balises appariées (h1/h2/h3/p/dl/dt/dd)",
    h.count("<h1>") == h.count("</h1>") and h.count("<h2>") == h.count("</h2>")
    and h.count("<h3>") == h.count("</h3>") and h.count("<p>") == h.count("</p>")
    and h.count("<dl") == h.count("</dl>") and h.count("<dt>") == h.count("</dt>")
    and h.count("<dd>") == h.count("</dd>"))

# ---- registre : htmlFr posé, voisins intacts
reg = json.load(open(REG, encoding="utf-8"))
les = {str(d.get("docId", "")): d for d in reg["lessons"]}
chk("registre livre 2 : 27 entrées", len(reg["lessons"]) == 27)
chk("registre 255 intact (17 252 car)", len(les["pdf-mut23h2u-255"].get("htmlFr") or "") == 17252)
chk("registre 256 intact (15 854 car)", len(les["pdf-mut23h2u-256"].get("htmlFr") or "") == 15854)
chk("registre 257 intact (~23 700 car)", 20_000 <= len(les["pdf-mut23h2u-257"].get("htmlFr") or "") <= 30_000)
chk("registre 258 intact (19 291 car)", len(les["pdf-mut23h2u-258"].get("htmlFr") or "") == 19291)
chk("registre 259 intact (~23 800 car)", 20_000 <= len(les["pdf-mut23h2u-259"].get("htmlFr") or "") <= 30_000)
chk("registre 260 intact (29 786 car)", len(les["pdf-mut23h2u-260"].get("htmlFr") or "") == 29786)
chk("registre 261 intact (~28 600 car)", 25_000 <= len(les["pdf-mut23h2u-261"].get("htmlFr") or "") <= 32_000)
chk("registre 262 intact (~28 000 car)", 24_000 <= len(les["pdf-mut23h2u-262"].get("htmlFr") or "") <= 33_000)
chk("registre 264 non touché (htmlFr vide)", (les["pdf-mut23h2u-264"].get("htmlFr") or "") == "")
fr = les["pdf-mut23h2u-263"].get("htmlFr") or ""
if fr:
    chk("registre 263 = htmlFr posé (~30 000 car)", 26_000 <= len(fr) <= 36_000)
    chk("registre 263 == fichier livré", fr.strip() == h.strip())
else:
    chk("registre 263 encore vide (avant hand-set)", True)
chk("titleAr pré-mappé 263", les["pdf-mut23h2u-263"].get("titleAr") == "الدرس 9 : الحديث المعروف والمنكر")
chk("titleFr pré-mappé 263 aligné au h1",
    (les["pdf-mut23h2u-263"].get("titleFr") or "").replace("'", "’").startswith("Leçon 9 : Le hadith reconnu"))
reg1 = json.load(open(REG1, encoding="utf-8"))
l1 = {str(d.get("docId", "")): d for d in reg1["lessons"]}
chk("registre livre 1 : 141 intact (24 319 car)", len(l1["pdf-mut23h2r-141"].get("htmlFr") or "") == 24319)
chk("registre livre 1 : 140 intact (16 018 car)", len(l1["pdf-mut23h2r-140"].get("htmlFr") or "") == 16018)
chk("registre livre 1 : 136 intact (20 967 car)", len(l1["pdf-mut23h2r-136"].get("htmlFr") or "") == 20967)

print(f"verify-ulumhadith2-pdf263 : {ok} PASS / {fail} ÉCHEC")
raise SystemExit(1 if fail else 0)

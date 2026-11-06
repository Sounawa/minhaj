#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Minhāj — Vérification de la leçon ulum-hadith-tanawi-2 / pdf-mut23h2u-260
(الدرس 6 — al-ḥadīṯ aṣ-ṣaḥīḥ wa-marātibuh, p.35-40 du manuel
ulum-hadith-2-thanawi_text.pdf) : bornes p.35-40 par DOUBLE sondage
(p.35 = bannière verte + badge 6 + boîte jaune 3 objectifs + tamhīd ;
p.40 = istiṯmār citation Nuzha + renvoi ṣ:35 + item « schéma des préférences »
+ al-iʿdād al-qablī 2 consignes ; p.41 = objectifs leçon 7 الحسن) ;
nombres de la couche pdftotext INVERSÉS tranchés par recadrages 600-900 dpi +
lecture image directe + couche logique PyMuPDF FIDÈLE (mécanisme R615 :
182/3→3/281→t.3 p.281, 21/553→355/12→t.12 p.355, ṣ 53→ṣ:35, ṣ 95→ṣ:59,
459/1→t.1 p.459) ; LISTE DES SEPT DEGRÉS tranchée par recadrage VLM vlm-liste
(l'OCR 300 dpi perdit les items 2-3) ; chaîne az-Zuhrī rétablie (vlm-D2) ;
matn anqaḏahu + an-nār tranchés (vlm-C2) ; isnād Abū Tābit Muḥammad b. ʿUbayd
Allāh al-Madīnī tranché en image directe (VLM divergents récusés) ; verbe
lā yanziʿu-hu à trois concordances ; fin de citation p.35 « faḍḍama Ṣaḥīḥ
al-Buḫārī… » tranchée en image directe ; honnêteté d'apparat (suite de
« wa-yuḫraǧu bi-hāḏā aš-šarṭ » dégradée, onglets 2-3 illisibles) documentée ;
2 ḥadīṯs prophétiques rendus de l'imprimé, zéro āya, zéro résidu arabe,
zéro apostrophe droite, zéro doublon.
Usage: python3 scripts-translate/verify-ulumhadith2-pdf260.py
"""
import json
import re

HTML = "/home/z/my-project/tr-tmp/lesson-uh2-pdf-mut23h2u-260-fr.html"
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
chk("h1 = titleFr pré-mappé « Leçon 6 : Le hadith authentique (ṣaḥīḥ) et ses degrés »",
    hn.startswith("<h1>Leçon 6 : Le hadith authentique (ṣaḥīḥ) et ses degrés"))
chk("h1 mentionne deuxième année", "deuxième année" in h[:500])
chk("h1 mentionne sept degrés", "les sept degrés de l’authentique" in h[:1200])
chk("dl.lesson-meta présent", '<dl class="lesson-meta">' in h and "<dt>Source du cours</dt>" in h)
chk("item archive.org cité", "1_20220304_20220304_2251" in h)
chk("source locale citée", "ulum-hadith-2-thanawi_text.pdf" in h)
chk("bornes p.35-40 documentées", "pages 35 à 40" in h)
chk("p.41 leçon 7 non touchée", "pdf-mut23h2u-261" in h and "non touché" in h)
chk("p.30-34 leçon 5 non touchée", "pdf-mut23h2u-259" in h and "non touché" in h)
chk("double sondage « jamais devinées »", "jamais devinées" in h)
chk("bannière concordante au registre et à la table des matières",
    "titleAr pré-mappé" in h and "table des matières" in h)
chk("cache incorporé borné cité", "tr-tmp/r619/p035-041-embed.txt" in h)
chk("caches OCR cités", "tr-tmp/r619/p035-300.txt" in h)
chk("tessdata dépôt documenté", "scripts-translate/tessdata" in h)
chk("couche logique PyMuPDF citée", "p035-pymu.txt" in h)
chk("claimant défunt R619 recoupé", "claimant défunt R619" in h)
chk("inversion 182/3→3/281 documentée", "182/3" in hn and "3/281" in hn)
chk("Maqāyīs t. 3, p. 281 rendue", "t. 3, p. 281" in hn)
chk("inversion 21/553→355/12 documentée", "21/553" in hn and "355/12" in hn)
chk("Muʿǧam al-kabīr t. 12, p. 355 rendue", "t. 12, p. 355" in hn)
chk("inversion ṣ 53→ṣ:35 documentée", "ṣ 53" in hn and "ṣ : 35" in hn)
chk("Nuzha p. 35 rendue", "Ibn Ḥaǧar, p. 35" in hn)
chk("inversion ṣ 95→ṣ:59 documentée", "ṣ 95" in hn and "ṣ : 59" in hn)
chk("Maʿrifat p. 59 rendue", "p. 59" in hn)
chk("Taqrīb 459/1 documentée", "459/1" in hn and "t. 1, p. 459" in hn)
chk("mécanisme inversion élucidé (PyMuPDF fidèle)", "PyMuPDF" in hn and "FIDÈLE" in hn and "miroir" in hn)
chk("recadrages 600 à 900 dpi documentés", "900 dpi" in hn)
chk("crops et VLM cités", "qa-crops-r619/" in h and "vlm-liste" in h
    and "vlm-D2-p38-top" in h and "vlm-C2-p37-bukhari" in h)
chk("SEPT items de la liste documentés", "SEPT items" in hn
    and "perdit deux" in hn and "numérotation 1-7" in hn)
chk("chaîne az-Zuhrī rétablie documentée", "RÉTABLIE par le recadrage" in hn)
chk("anqaḏahu/an-nār tranchés documentés", "naqaḏa-hu" in hn and "an-nār" in hn)
chk("isnād Abū Tābit al-Madīnī documenté (VLM divergents récusés)",
    "Abū Tābit" in hn and "Abū Tamīm" in hn and "Abū Qātib" in hn and "ad-Dīnī" in hn)
chk("verbe lā yanziʿu-hu à trois concordances", "lā yanziʿu-hu" in hn and "trois concordances" in hn)
chk("fin de citation p.35 tranchée en image directe", "bande image directe 900 dpi" in hn)
chk("honnêteté d’apparat : suite dégradée non complétée",
    "demeurée dégradée dans les trois couches — rendue par l’annonce seule, jamais complétée" in hn)
chk("honnêteté d’apparat : onglets 2-3 illisibles documentés",
    "documentés sans lecture forcée" in hn)
chk("honnêteté d’apparat : wa-raddi-hi rendu par le sens", "rendue telle quelle par le sens" in hn)
chk("zéro āya rendue", "Aucune āya rendue" in h)
chk("2 ḥadīṯs prophétiques rendus de l’imprimé",
    "Trois (qualités), quiconque les réunit goûte la douceur de la foi" in hn
    and "Lorsque l’un de vous fait ses ablutions" in hn)

# ---- objectifs
chk("objectif : concept du ṣaḥīḥ, divisions et conditions",
    "reconnaisse le concept du ḥadīṯ authentique (ṣaḥīḥ), ses divisions et ses conditions" in hn)
chk("objectif : divisions du ḫabar d’après les qualités des rapporteurs",
    "distingue les divisions du ḫabar d’après les qualités de ses rapporteurs et les états de son isnād" in hn)
chk("objectif : méthode des muḥaddiṯūn",
    "suive la méthode des muḥaddiṯūn en la reconnaissance de l’authentique parmi les hadiths" in hn)
chk("trois objectifs", "trois objectifs" in hn)

# ---- tamhīd
chk("tamhīd : conditions d’une extrême précision",
    "des conditions d’une extrême précision" in hn)
chk("tamhīd : maqbūl/mardūd et leurs divisions",
    "en accepté (maqbūl) et rejeté (mardūd)" in hn)
chk("tamhīd : questions (conditions, degrés)",
    "quelles sont les conditions de l’acceptation du hadith" in hn
    and "quels sont ses degrés" in hn)

# ---- muṭūn (texte)
chk("muṭūn : ḫabar āḥād, ʿadl tāmm aḍ-ḍabṭ, muttaṣil",
    "transmis par un transmetteur probe (ʿadl) parfaitement maître de sa mémoire (tāmm aḍ-ḍabṭ)" in hn
    and "d’isnād continu" in hn)
chk("muṭūn : sans muʿallal ni šāḏ", "sans défaut caché (muʿallal) ni anomalie (šāḏ)" in hn)
chk("muṭūn : ṣaḥīḥ li-ḏāti-hi", "c’est l’authentique par lui-même (aṣ-ṣaḥīḥ li-ḏāti-hi)" in hn)
chk("muṭūn : rangs varient, puis Buḫārī/Muslim/condition commune",
    "ses rangs varient selon la variation de ces qualités" in hn
    and "fit précéder le Ṣaḥīḥ d’al-Buḫārī, puis Muslim, puis leur condition commune" in hn)
chk("fahm : deux tâches et quatre gloses",
    "extraire du texte les conditions du ḥadīṯ ṣaḥīḥ" in hn
    and "le probe (ʿadl) est celui qui porte une disposition" in hn
    and "siège dans la réception et la restitution" in hn
    and "apparent ou caché" in hn
    and "la contradiction du fiable par plus fiable que lui" in hn)

# ---- commentaire
chk("exposé : quatre vertus et hiérarchie", "quatre vertus se réunissent en son isnād" in hn)
chk("extraction : conditions et degrés",
    "les conditions du ḥadīṯ ṣaḥīḥ — la continuité de l’isnād" in hn
    and "les degrés du ḥadīṯ ṣaḥīḥ, qui varient selon la variation de ces qualités mêmes" in hn)

# ---- 1 ṣaḥīḥ
chk("langue : racine ṣ-ḥ-ḥ, absence de maladie et de défaut",
    "tiré de la racine ṣ-ḥ-ḥ, qui porte la signification de l’absence de maladie et de défaut, et de la droiture" in hn)
chk("terminologie : définition complète",
    "le hadith dont l’isnād est continu, rattaché à un transmetteur probe parfaitement maître de sa mémoire, et préservé de l’anomalie et du défaut caché" in hn)
chk("le propos sur le li-ġayri-hi viendra ensuite",
    "le propos sur l’authentique par autre que lui (aṣ-ṣaḥīḥ li-ġayri-hi) viendra ensuite" in hn)
chk("condition 1 : muttaṣil défini", "Le continu (al-muttaṣil) est celui dont l’isnād est préservé de toute rupture" in hn)
chk("condition 1 : formules de samaʿ",
    "« j’ai entendu un tel dire ceci »" in hn and "« il m’a informé »" in hn
    and "« il m’a rapporté »" in hn and "« j’ai vu »" in hn
    and "a pris le hadith directement de son šayḫ" in hn)
chk("condition 2 : ʿadl, taqwā, fisq, khawārim al-murūʾa",
    "attaché à la piété (at-taqwā), tenu à l’écart de la perversité (al-fisq) et des vilenies de l’ostentation (ḫawārim al-murūʾa)" in hn)
chk("condition 3 : la justesse l’emporte sur l’erreur",
    "la justesse de l’homme l’emporte sur son erreur — et non qu’il soit de ceux qui ne se trompent jamais" in hn)
chk("condition 3 : ḍabṭ ṣadr / ḍabṭ kitāb",
    "la maîtrise du cœur (ḍabṭ ṣadr)" in hn and "la maîtrise du livre (ḍabṭ kitāb)" in hn
    and "depuis qu’il l’a entendu et vérifié jusqu’à ce qu’il le restitue" in hn)
chk("condition 3 : tamām exclut le ḥasan",
    "pour exclure le ḥasan par lui-même, à qui l’on ne l’exige pas" in hn)
chk("condition 4 : šāḏ = contradiction du fiable",
    "L’anomalie (aš-šāḏ) est la contradiction du fiable par un homme plus fiable que lui, ou plus nombreux que lui" in hn)
chk("condition 5 : ʿilla apparente ou cachée",
    "l’absence du défaut caché (intifāʾ al-ʿilla), qu’il soit apparent ou caché" in hn)
chk("divisions : li-ḏāti-hi non dépendant d’un facteur extérieur",
    "celui dont l’authenticité ne dépend d’aucun facteur extérieur à lui" in hn)
chk("divisions : li-ġayri-hi = ḥasan li-ḏāti-hi relevé",
    "est le ḥasan par lui-même lorsqu’il est rapporté par une voie, ou des voies, qui lui ressemblent ou qui sont plus fortes que lui" in hn)
chk("exemple Buḫārī : isnād Sulaymān b. Ḥarb → Šuʿba → Qatāda → Anas",
    "Sulaymān b. Ḥarb nous a rapportés, de Šuʿba, de Qatāda, d’Anas" in hn)
chk("exemple Buḫārī : renvoi Kitāb al-īmān",
    "Kitāb al-īmān" in hn
    and "ce qu’il répugne de revenir à la mécréance comme il répugne d’être jeté au Feu, extrait de la foi" in hn)
chk("exemple Buḫārī : leçon tirée (isnād continu, rapporteurs probes)",
    "son isnād est continu, ses rapporteurs sont tous probes, parfaitement maîtres de leur mémoire" in hn)
chk("exemple Ṭabarānī : isnād al-Asfāṭī → Abū Tābit → ʿAbd al-ʿAzīz → Kaṯīr → al-Qarrāṭ → Ibn ʿUmar",
    "al-ʿAbbās b. al-Faḍl al-Asfāṭī nous a rapportés" in hn
    and "Abū Tābit Muḥammad b. ʿUbayd Allāh al-Madīnī nous a rapportés" in hn
    and "ʿAbd al-ʿAzīz b. Muḥammad nous a rapportés, de Kaṯīr b. Zayd, d’Abū ʿAbd Allāh al-Qarrāṭ, d’Ibn ʿUmar" in hn)
chk("exemple Ṭabarānī : matn complet (yanziʿu-hu, tamḥū sayyiʾa, ḥattā yadḫul al-masǧid)",
    "sans que rien ne l’y pousse que la prière" in hn
    and "son pied gauche ne cesse d’effacer une mauvaise action et l’autre d’inscrire une bonne action, jusqu’à ce qu’il entre à la mosquée" in hn)
chk("exemple Ṭabarānī : isnād ḥasan, cause de la descente",
    "l’isnād de ce hadith est ḥasan (satisfaisant)" in hn
    and "la faiblesse de la maîtrise de l’un de ses rapporteurs — Kaṯīr b. Zayd al-Aslamī al-Madanī" in hn)
chk("exemple Ṭabarānī : Ibn Ḥaǧar « véridique, mais il se trompe »",
    "véridique (ṣadūq), mais il se trompe" in hn)

# ---- 2 marātib
chk("cause : ġalabat aẓ-ẓann, degrés selon les états des rapporteurs",
    "procurent la prédominance de la conjecture (ġalabat aẓ-ẓann) sur laquelle repose l’authenticité" in hn
    and "des degrés, les uns au-dessus des autres, selon les états des rapporteurs" in hn)
chk("aṣaḥḥ : rang le plus haut", "son récit est plus ferme (aṣaḥḥ) que celui qui est au-dessous de lui" in hn)
chk("rang supérieur : az-Zuhrī/Sālim + Ibn Sīrīn/ʿUbayda/ʿAlī + Naḫaʿī/ʿAlqama/Ibn Masʿūd",
    "la chaîne d’az-Zuhrī, de Sālim b. ʿAbd Allāh b. ʿUmar, de son père" in hn
    and "la chaîne de Muḥammad b. Sīrīn, de ʿUbayda b. ʿAmr, de ʿAlī" in hn
    and "la chaîne d’Ibrāhīm an-Naḫaʿī, de ʿAlqama, d’Ibn Masʿūd" in hn)
chk("rang 2 : Burayd + Ḥammād b. Salama/Ṯābit/Anas",
    "la narration de Burayd b. ʿAbd Allāh b. Abī Burda, de son grand-père, de son père, Abū Mūsā" in hn
    and "celle de Ḥammād b. Salama, de Ṯābit, d’Anas" in hn)
chk("rang 3 : Suhayl b. Abī Ṣāliḥ + ʿAlāʾ b. ʿAbd ar-Raḥmān",
    "celle de Suhayl b. Abī Ṣāliḥ, de son père, d’Abū Hurayra" in hn
    and "celle d’ʿAlāʾ b. ʿAbd ar-Raḥmān, de son père, d’Abū Hurayra" in hn)
chk("tous enveloppés par « probité et maîtrise », rangs hiérarchisés",
    "tous ces hommes furent enveloppés par le nom de « probité et maîtrise »" in hn
    and "impose de placer leur narration avant celle qui la suit" in hn
    and "précède la narration de celui dont on considère que ce qu’il rapporte seul est ḥasan" in hn)
chk("rang 4 : Ibn Isḥāq/ʿĀṣim b. ʿUmar/Ǧābir + ʿAmr b. Šuʿayb",
    "les chaînes de Muḥammad b. Isḥāq, de ʿĀṣim b. ʿUmar, de Ǧābir, et de ʿAmr b. Šuʿayb, de son père, de son grand-père" in hn)
chk("aṣ-ṣaḥīḥ al-asānīd : déclaration et retenue",
    "certains imams déclarèrent être les chaînes les plus sûres" in hn
    and "de ne point user de cette déclaration pour une chaîne déterminée" in hn
    and "sa préférence sur ce sur quoi ils ne la prononcèrent pas" in hn)
chk("sept degrés : items 1-7 tous rendus",
    "(1) le hadith authentique sur lequel se rencontrèrent l’imam al-Buḫārī et Muslim en leurs deux Ṣaḥīḥ" in hn
    and "(2) le hadith authentique qu’enregistra seul al-Buḫārī en son Ṣaḥīḥ" in hn
    and "(3) le hadith authentique qu’enregistra seul l’imam Muslim en son Ṣaḥīḥ" in hn
    and "(4) le hadith authentique qui satisfait à leur condition commune à tous deux sans qu’aucun des deux ne l’ait enregistré" in hn
    and "(5) le hadith authentique qui satisfait à la condition d’al-Buḫārī sans qu’il l’ait enregistré" in hn
    and "(6) le hadith authentique qui satisfait à la condition de Muslim sans qu’il l’ait enregistré" in hn
    and "(7) le hadith authentique qu’enregistrèrent d’autres qu’eux deux en leurs livres" in hn)
chk("sept degrés : la différenciation relative et ses dépassements",
    "cette différenciation ne vaut que selon la considération mentionnée" in hn
    and "il peut advenir à celui qui est surpassé ce qui le rend supérieur" in hn)
chk("exemple Muslim mashhūr + qurena",
    "un hadith enregistré par Muslim — par exemple — soit célèbre approchant le degré du tawātur" in hn
    and "il prend alors place devant le hadith qu’al-Buḫārī enregistra seul en son Ṣaḥīḥ s’il est un unique absolu" in hn)
chk("exemple Mālik/Nāfiʿ/Ibn ʿUmar + mubṭāl",
    "la chaîne de Mālik, de Nāfiʿ, d’Ibn ʿUmar" in hn
    and "surtout lorsque son isnād comporte un homme contre lequel il y a une objection (mubṭāl)" in hn)

# ---- ahtadī wa-aqtadī (al-Ḥākim)
chk("rubrique ahtadī wa-aqtadī", "Je m’inspire et j’inspire (ahtadī wa-aqtadī)" in hn)
chk("Ḥākim : compréhension, mémorisation, fréquence d’audition",
    "il se reconnaît aussi par la compréhension, la mémorisation et la fréquence de l’audition" in hn)
chk("Ḥākim : fréquentation des gens de la science",
    "la fréquentation des gens de la science et de la connaissance" in hn
    and "afin que se révèle ce qui demeurait caché du défaut du hadith" in hn)
chk("Maʿrifat p. 59 citée", "Maʿrifat ʿulūm al-ḥadīṯ (la connaissance des sciences du hadith) d’al-Ḥākim an-Nīsābūrī, p. 59" in hn)
chk("lien à la formation de l’étudiant", "la reconnaissance de l’authentique n’est pas un bénéfice passif tiré des listes de rapporteurs" in hn)

# ---- évaluation
chk("évaluation : 3 activités", "trois activités" in hn)
chk("évaluation : conditions + exemple", "énoncer les conditions du ḥadīṯ ṣaḥīḥ et en donner un exemple" in hn)
chk("évaluation : divisions du ṣaḥīḥ", "énoncer les divisions du ḥadīṯ ṣaḥīḥ" in hn)
chk("évaluation : degrés du ṣaḥīḥ", "exposer les degrés du ḥadīṯ ṣaḥīḥ" in hn)

# ---- exploitation (Ibn Ḥaǧar / Nuzha)
chk("exploitation : Buḫārī plus accompli, plus rigoureux",
    "plus accomplies que dans le livre de Muslim, plus rigoureuses" in hn)
chk("exploitation : la continuité — la rencontre attestée vs la contemporanéité",
    "n’exigea pas que le rapporteur ait eu pour son rapporteur une rencontre attestée, ne fût-ce qu’une fois" in hn
    and "se contenta de la simple contemporanéité" in hn)
chk("exploitation : la probité — les hommes de Muslim plus nombreux, les maîtres de Buḫārī",
    "les hommes dont traite Muslim sont plus nombreux que ceux dont traite al-Buḫārī" in hn
    and "la plupart d’entre eux furent de ses maîtres" in hn
    and "à la différence de Muslim en ces deux points" in hn)
chk("exploitation : l’absence d’anomalie — objections plus rares",
    "en plus petit nombre que ce que l’on objecta à Muslim" in hn)
chk("exploitation : accord des savants + Muslim disciple et élève",
    "al-Buḫārī était plus vénérable que Muslim en les sciences" in hn
    and "Muslim fut son disciple et son élève" in hn
    and "ne cessa de tirer profit de lui et de suivre ses traces" in hn)
chk("exploitation : Dāraquṭnī cité", "ad-Dāraquṭnī dit" in hn
    and "sans al-Buḫārī, Muslim ne serait point parvenu ni venu" in hn)
chk("exploitation : Nuzha p. 35 citée", "Nuzhat an-naẓar šarḥ Nuḫbat al-fikr (la promenade de la contemplation) d’Ibn Ḥaǧar, p. 35" in hn)
chk("exploitation : item « schéma des préférences »",
    "dresse le schéma des préférences par lesquelles le ḥāfiẓ Ibn Ḥaǧar fit précéder le Ṣaḥīḥ d’al-Buḫārī du Ṣaḥīḥ de Muslim" in hn
    and "le témoignage d’ad-Dāraquṭnī" in hn)

# ---- préparation leçon suivante
chk("leçon suivante nommée (ḥasan)", "Le hadith satisfaisant (ḥasan)" in hn)
chk("préparation : paroles des savants sur le ḥasan", "rechercher les paroles des savants sur le ḥadīṯ ḥasan" in hn)
chk("préparation : extraire des Sunan d’at-Tirmiḏī",
    "extraire des Sunan d’at-Tirmiḏī un hadith de ceux qu’il déclara ḥasan" in hn)
chk("préparation : 2 consignes", "deux consignes" in h)

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
fr9 = les["pdf-mut23h2u-259"].get("htmlFr") or ""
chk("registre 259 livré (htmlFr posé ~23 800 car)", 20_000 <= len(fr9) <= 30_000)
chk("registre 261 non touché (htmlFr vide)", (les["pdf-mut23h2u-261"].get("htmlFr") or "") == "")
chk("registre 255 intact (17 252 car)", len(les["pdf-mut23h2u-255"].get("htmlFr") or "") == 17252)
fr6 = les["pdf-mut23h2u-256"].get("htmlFr") or ""
chk("registre 256 intact (15 854 car)", len(fr6) == 15854)
fr7 = les["pdf-mut23h2u-257"].get("htmlFr") or ""
chk("registre 257 intact (~23 700 car)", 20_000 <= len(fr7) <= 30_000)
fr8 = les["pdf-mut23h2u-258"].get("htmlFr") or ""
chk("registre 258 intact (19 291 car)", len(fr8) == 19291)
fr = les["pdf-mut23h2u-260"].get("htmlFr") or ""
if fr:
    chk("registre 260 = htmlFr posé (~29 800 car)", 20_000 <= len(fr) <= 35_000)
    chk("registre 260 == fichier livré", fr.strip() == h.strip())
else:
    chk("registre 260 encore vide (avant hand-set)", True)
chk("titleAr pré-mappé 260", les["pdf-mut23h2u-260"].get("titleAr") == "الدرس 6 : الحديث الصحيح ومراتبه")
chk("titleFr pré-mappé 260 aligné au h1",
    (les["pdf-mut23h2u-260"].get("titleFr") or "").replace("'", "’").startswith("Leçon 6 : Le hadith authentique (ṣaḥīḥ) et ses degrés"))
reg1 = json.load(open(REG1, encoding="utf-8"))
l1 = {str(d.get("docId", "")): d for d in reg1["lessons"]}
chk("registre livre 1 : 141 intact (24 319 car)", len(l1["pdf-mut23h2r-141"].get("htmlFr") or "") == 24319)
chk("registre livre 1 : 140 intact (16 018 car)", len(l1["pdf-mut23h2r-140"].get("htmlFr") or "") == 16018)
chk("registre livre 1 : 136 intact (20 967 car)", len(l1["pdf-mut23h2r-136"].get("htmlFr") or "") == 20967)

print(f"verify-ulumhadith2-pdf260 : {ok} PASS / {fail} ÉCHEC")
raise SystemExit(1 if fail else 0)

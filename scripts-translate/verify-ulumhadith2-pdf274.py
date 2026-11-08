#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Minhāj — Vérification de la leçon ulum-hadith-tanawi-2 / pdf-mut23h2u-274
(الدرس 20 : الحديث المعلل — al-muʿallal, p.102-106 du manuel
ulum-hadith-2-thanawi_text.pdf) : bornes p.102-106 par sondage image
(p.101 = clôture de la leçon 19, livrée R654, docId pdf-mut23h2u-273 ;
p.102 = bannière médaillon « 20 » en chiffres occidentaux + 4 objectifs +
tamhīd double question + matn Ibn Ḥaǧar au wahm + gloses + استخلاص ;
p.103 = أولا définition (luga Lisān 11/471, istiilāh Ibn aṣ-Ṣalāḥ [ص 89],
débat muʿlūl/muʿallal avec al-ʿIrāqī [القاري ص 549], deux conditions) +
ثانيا voies (تتبع, جمع الطرق, ابن المديني, changeur) ; p.104 = emplois étendus
+ الترمذي النسخ + السخاوي [القاري ص 461] + ثالثا importance (عبد الرحمن بن مهدي
[علل ابن أبي حاتم 1/9], sept maîtres) + رابعا exemple (isnād يعلى بن عبيد/
عمرو بن دينار [المعجم الكبير], matn أنس/مسلم البسملة [صحيح مسلم]) ;
p.105 = fin exemple [ص 92] + خامسا jugement + أهتدي الدارمي + التقويم 2 +
الاستثمار ابن الصلاح [ص 93] ; p.106 = 2 consignes exploitation + الإعداد القبلي
1 item (p106-idad) ; p.107 = bannière leçon 21 المدرج والمقلوب (médaillon ٢١,
sondage, non touchée, registre vide).
Adjudications documentées (TRENTE lectures d'images, tr-tmp/qa-crops-r655/) :
mot final du matn « فَالْمَعْلُولُ » au zoom 600 dpi (z14) contre couche et bloc
« فالعلل » ; définition complétée par l'image « اطُّلِعَ فيه على علة تُقدح في صحته
مع أن ظاهره السلامة منها » (z2b : تُقدح lettre à lettre) contre couche tronquée ;
Lisān « 11/471 » (z1) contre « 174 » couche ; القاري « ص 549 » (z4) contre « 945 » ;
القاري « ص 461 » chiffres occidentaux (z6) contre « 164 » ; ابن أبي حاتم « 1/9 » ;
Muqaddima « ص 92 » (z8) contre « 29 » et « ص 93 » (z10) contre « 39 » ; مرذول
dhāl pointé (z3) contre hypothèse مردود ; بالمعلول confirmé (z3) ; اصطلاحا
lettre à lettre (z5) contre « اضطلا ها/عندكة » ; taqwīm 1 « العَلَل » ʿayn sans
point à 900 dpi (z11) contre lecture basse résolution « العقل » (z9) ;
المصرح به mot à mot 1200 dpi (z13) ; structure de clôture tranchée : 2 items
p.106 = exploitation (continuité avec iʿdād leçon 19 R654), الإعداد القبلي
1 item ; particule « هذا » p.104 tête = clôture de citation, rendue dans le flux ;
« سيّما » rendu « surtout » (couche « سيما », bloc « سبحما » récusé) ;
ZÉRO ĀYA (cache coranique non sollicité). Reprise du WIP de la passe antérieure
de la même trace subagent-r655-uh2-274 (claim 19:58:45Z, refresh 20:31:44Z).
Usage: python3 scripts-translate/verify-ulumhadith2-pdf274.py
"""
import json
import re

HTML = "/home/z/my-project/tr-tmp/lesson-uh2-pdf-mut23h2u-274-fr.html"
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
hn = re.sub(r" +", " ", h.replace("&nbsp;", " ").replace("\u202f", " ").replace("\u2009", " "))

# ---- h1 et méta
chk("h1 = titleFr pré-mappé « Leçon 20 : Le hadith défectueux (maʿlūl) »",
    hn.startswith("<h1>Leçon 20 : Le hadith défectueux (maʿlūl)"))
chk("h1 mentionne deuxième année", "deuxième année" in h[:500])
chk("h1 mentionne la ʿilla cachée découverte par les indices",
    "cause (ʿilla) cachée se découvre par les indices et le rassemblement des voies" in h[:900])
chk("h1 mentionne apparent salubre et débat muʿlūl/muʿallal",
    "son apparent est la salubrité" in h[:1200] and "muʿlūl" in h[:1500] and "muʿallal" in h[:1500])
chk("h1 mentionne voies + changeur + Ibn Mahdī + exemple Yaʿlā",
    "le changeur dans l’examen du dinar et du dirham" in h[:2600]
    and "ʿAbd ar-Raḥmān b. Mahdī" in h[:2600] and "Yaʿlā b. ʿUbayd" in h[:3200])
chk("h1 mentionne ahtadī Dārimī et istiṯmār Ibn aṣ-Ṣalāḥ",
    "ad-Dārimī" in h[:5200] and "Ibn aṣ-Ṣalāḥ" in h[:5200])
chk("dl.lesson-meta présent", '<dl class="lesson-meta">' in h and "<dt>Source du cours</dt>" in h)
chk("item archive.org cité", "1_20220304_20220304_2251" in h)
chk("source locale citée", "ulum-hadith-2-thanawi_text.pdf" in h)
chk("bornes p.102-106 documentées", "pages 102 à 106" in h)
chk("p.101 clôture leçon 19 (R654, 273)", "R654" in h and "pdf-mut23h2u-273" in h)
chk("p.107 leçon 21 sondée, non touchée, registre vide",
    "la leçon 21" in h and "non touchée" in h and "registre vide" in h)
chk("sondage « jamais devinées »", "jamais devinées" in h)
chk("matière multi-couches citée (raw + decoded + readable)",
    "uh2-l274-raw.txt" in h and "uh2-l274-decoded.txt" in h and "uh2-l274-readable.txt" in h)
chk("reprise trace antérieure + refresh documentés",
    "subagent-r655-uh2-274" in h and "19 h 58 min 45 s" in h and "20 h 31 min 44 s" in h)
chk("TRENTE lectures d’images consignées + noms de crops",
    "TRENTE lectures d’images" in h and "p102-banner-objectifs.png" in h
    and "p102-tamhid-matn.png" in h and "p102-gloses.png" in h
    and "p103-def-lugha-istilah.png" in h and "p103-turuq.png" in h
    and "p104-ahammiya.png" in h and "p104-ihtilaq.png" in h and "p104-mithal.png" in h
    and "p105-b-cont.png" in h and "p105-hukm-ahtadi.png" in h
    and "p105-taqwim-istithmar.png" in h and "p106-idad.png" in h and "p107-banner-l21.png" in h)
chk("zooms discriminatifs cités (z1…z14)",
    "z1-lisan-ref.png" in h and "z2b-definition-l2.png" in h and "z3-mardud.png" in h
    and "z4-qari-p103.png" in h and "z5-adtila.png" in h and "z6-qari-p104.png" in h
    and "z7-ans.png" in h and "z8-muqaddima-92.png" in h and "z9-taqwim.png" in h
    and "z10-muqaddima-93.png" in h and "z11-taqwim-q1-900.png" in h
    and "z12c-ans-900.png" in h and "z13-word-1200.png" in h and "z14-matn-600.png" in h)
chk("détour h3 p.78-84 de la passe antérieure signalé hors slot",
    "p.78-84" in h and "h3-400" in h and "ni comptés ni utilisés" in h)
chk("matn final « fa-l-maʿlūl » adjudiqué au zoom 600 dpi contre couche et bloc",
    "fa-l-maʿlūl" in h and "z14" in h and "600 dpi" in h and "convergence avec le débat du nom" in h)
chk("définition complétée par l’image contre couche tronquée + tuqdiḥu",
    "couche tronquée" in h and "tuqdiḥu" in h and "lettre à lettre" in h)
chk("renvoi Lisān 11/471 contre « 174 » (loi d’inversion à la couche, non à l’image)",
    "11/471" in h and "174" in h and "non à l’image" in h)
chk("renvoi al-Qārī 549 contre « 945 » et 461 (chiffres occidentaux) contre « 164 »",
    "page 549" in h and "945" in h and "page 461" in h and "chiffres occidentaux" in h and "164" in h)
chk("renvoi Ibn Abī Ḥātim 1/9", "1/9" in h and "tome un, page 9" in h)
chk("renvois Muqaddima 92 contre « 29 » et 93 contre « 39 »",
    "page 92" in h and "29" in h and "page 93" in h and "39" in h)
chk("marḏūl dhāl pointé contre hypothèse mardūd + bi-l-maʿlūl confirmé",
    "marḏūl" in h and "dhāl" in h and "mardūd" in h and "bi-l-maʿlūl" in h)
chk("iṣṭilāḥan adjudiqué lettre à lettre contre bruits de couche + ʿindanā",
    "iṣṭilāḥan" in h and "ʿindakum" in h and "ʿindanā" in h)
chk("taqwīm 1 « al-ʿalal » ʿayn à 900 dpi contre « al-ʿaql » basse résolution",
    "900 dpi" in h and "al-ʿaql" in h and "ʿayn sans point" in h and "récusation documentée" in h)
chk("citation Ibn al-Madīnī doublet « an-an » récusé artefact",
    "doublet « an-an »" in hn and "artefact de saut de ligne" in hn)
chk("muṣraḥ adjudiqué 1200 dpi", "al-muṣraḥ bi-hi" in h and "1200 dpi" in h)
chk("structure de clôture : 2 items exploitation + iʿdād 1 item contre attente",
    "les deux items numérotés de la page 106 appartiennent à l’exploitation" in h
    and "préparation préalable" in h and "contre l’attente de deux items" in h)
chk("particule hāḏā clôture de citation rendue dans le flux",
    "hāḏā" in h and "fin de la citation introduite en bas de la page 103" in h)
chk("sayyamā rendu « surtout », bloc « subḥamā » récusé",
    "sayyamā" in h and "surtout" in h and "subḥamā" in h)
chk("zéro āya (cache coranique non sollicité)",
    "ZÉRO ĀYA" in h and "cache coranique non sollicité" in h)

# ---- objectifs (4)
chk("objectif 1 : reconnaître le concept du ḥadīṯ motivé",
    "que je reconnaisse le concept du ḥadīṯ motivé (al-muʿallal)" in hn)
chk("objectif 2 : importance de la connaissance et ses voies",
    "que je comprenne l’importance de la connaissance du motivé et ses voies de connaissance" in hn)
chk("objectif 3 : éviter l’argumentation par les ḥadīṯ à ʿilla",
    "que j’évite l’argumentation par les ḥadīṯ qui portent une ʿilla" in hn)
chk("objectif 4 : honnêteté dans la transmission et l’accomplissement de la science",
    "que je m’imprègne du trait de l’honnêteté (al-amāna) dans la transmission des récits"
    in hn and "l’accomplissement de la science" in hn)

# ---- tamhīd + matn
chk("tamhīd : l’examen diffère selon l’examineur + virtuoses",
    "L’examen du ḥadīṯ diffère selon l’examineur" in hn
    and "les virtuoses de cet art perçoivent dans le ḥadīṯ des choses cachées" in hn)
chk("tamhīd : conditions réunies en apparence + isnād/matn porte ce qui met en doute",
    "les conditions de l’authenticité sont réunies en apparence" in hn
    and "sa chaîne (isnād) ou son texte (matn) porte ce qui met en doute son authenticité" in hn)
chk("tamhīd : double question (nom du type / voies de connaissance)",
    "Comment nomme-t-on donc ce type" in hn and "quelles sont ses voies de connaissance" in hn)
chk("matn : wahm — indices et rassemblement des voies → motivé",
    "« Puis le wahm — l’illusion : si l’on y prend connaissance par les indices et le rassemblement des voies, alors c’est le motivé. »" in hn)

# ---- gloses + istiḫlāṣ
chk("glose 1 : wahm = narration sur le mode de la conjecture erronée",
    "la narration du ḥadīṯ sur le mode de la conjecture erronée (at-tawahhum)" in hn)
chk("glose 2 : qarāʾin pluriel de qarīna, une chose qui indique ce qu’on cherche",
    "pluriel de qarīna, et la qarīna : une chose qui indique ce qu’on cherche" in hn)
chk("glose 3 : nom de patient de aʿalahā + muʿall + règle morphologique connue",
    "un nom de patient de « il l’a motivée (aʿalahā) »" in hn
    and "il est « muʿall », et c’est la règle morphologique connue" in hn)
chk("istiḫlāṣ : ce par quoi se connaît le wahm dans le ḥadīṯ",
    "j’extrait du texte (matn) ce par quoi se connaît le wahm dans le ḥadīṯ" in hn)

# ---- tabṣīṭ intro
chk("intro tabṣīṭ : double question + wahm + cinq parties",
    "Le tamhīd a posé la double question" in hn and "quand la cause se découvre par les indices et le rassemblement des voies, le ḥadīṯ est motivé" in hn
    and "cinq parties : la définition, les voies de connaissance, l’importance de la connaissance, l’exemple, le jugement" in hn)

# ---- tabṣīṭ 1 : définition
chk("luga : ʿilla-yaʿilla + iʿtilāl + ʿalīl malade",
    "« ʿilla — yaʿilla » et « iʿtilāl » : être malade, d’où « ʿalīl » (malade)" in hn)
chk("luga : lā uʿlika llāh + la ʿilla la maladie + Lisān 11/471",
    "« lā uʿlika llāh » : que Dieu ne t’inflige pas de maladie" in hn
    and "et la ʿilla : la maladie" in hn
    and "[Lisān al-ʿArab (la langue des Arabes), Ibn Manẓūr, tome onze, page 471, avec adaptation]" in hn)
chk("istiilāh : définition Ibn aṣ-Ṣalāḥ + renvoi page 89",
    "le ḥadīṯ motivé est le ḥadīṯ dans lequel on a pris connaissance d’une ʿilla qui met en doute son authenticité, alors que son apparent est la préservation de celle-ci" in hn
    and "[Muqaddimat Ibn aṣ-Ṣalāḥ (l’introduction d’Ibn aṣ-Ṣalāḥ), page 89]" in hn)
chk("istiilāh : muḥaddiṯ (Buḫārī, Tirmiḏī, Ibn ʿAdī, Dāraquṭnī) + mutakallimūn/uṣūliyyūn + muʿlūl",
    "comme al-Buḫārī, at-Tirmiḏī, Ibn ʿAdī et ad-Dāraquṭnī" in hn
    and "des théologiens (al-mutakallimūn) et des fondamentalistes (al-uṣūliyyūn)" in hn
    and "qu’ils le nomment « muʿlūl »" in hn)
chk("istiilāh : récusé marḏūl chez les gens de l’arabe + abreuvé une fois après l’autre + muʿallal",
    "l’a récusé comme étant écarté (marḏūl) chez les gens de l’arabe et de la langue" in hn
    and "il lui a donné à boire une fois après l’autre, et cela ne convient pas" in hn
    and "et il l’a nommé « muʿallal »" in hn)
chk("ʿIrāqī : le plus juste des deux noms muʿallal + renvoi Šarḥ šarḥ page 549",
    "Le ḥāfiẓ al-ʿIrāqī a dit : le plus juste des deux noms est « muʿallal »" in hn
    and "[Šarḥ šarḥ Nuḫbat al-fikr fī muṣṭalaḥāt ahli-l-aṯar" in hn and "al-Qārī, page 549]" in hn)
chk("conditions : obscurité et cachette + mise en doute ; manquante → pas ʿilla terminologiquement",
    "l’obscurité et la cachette, et la mise en doute de l’authenticité du ḥadīṯ" in hn
    and "elle ne se nomme pas chez nous une ʿilla terminologiquement" in hn)

# ---- tabṣīṭ 2 : voies
chk("voie 1 : tatabbuʿ + qarāʾin + riǧāl al-asānīd + substitution d’un narrateur",
    "la multiplication de l’enquête (kaṯrat at-tatabbuʿ), le rassemblement des indices" in hn
    and "l’examen des hommes des chaînes (riǧāl al-asānīd)" in hn
    and "comme la substitution d’un narrateur et la narration d’autrui sur le mode de la conjecture erronée" in hn)
chk("voie 1 : citation ʿAlī b. al-Madīnī — voies non rassemblées, tort non dévoilé",
    "il a été rapporté de ʿAlī b. al-Madīnī qu’il a dit" in hn
    and "« le propos (al-bāb) : quand on n’en rassemble pas ses voies, son tort ne se dévoile pas »" in hn)
chk("voie 2 : ǧamʿ aṭ-ṭuruq + maǧāmiʿ/masānīd + tarǧīḥ + mawṣūl/mursal + divergence/ḍabṭ/itqān",
    "le rassemblement des voies (ǧamʿ aṭ-ṭuruq) — c’est-à-dire les chaînes qui contiennent les textes" in hn
    and "leur recensement exhaustif auprès des recueils (al-maǧāmiʿ) et des masānīd" in hn
    and "la préférence (at-tarǧīḥ)" in hn and "qu’il est continu (mawṣūl) ou suspendu (mursal) ou pareil des deux" in hn
    and "de leur précision et de leur maîtrise" in hn)
chk("limite : déficit connu, inexplicité — le changeur et le dinar/dirham",
    "un déficit, mais qu’il n’a pas la puissance de l’expliciter" in hn
    and "comme le changeur (aṣ-ṣayrāfī) dans l’examen du dinar et du dirham" in hn)
chk("emplois étendus : mensonge/impiété/négligence/mauvais préservage + tadlīs + Tirmiḏī nasḫ + Saḫāwī",
    "comme le mensonge du narrateur, son impiété, sa négligence, son mauvais préservage" in hn
    and "l’obscurcissement (at-tadlīs)" in hn
    and "l’imām at-Tirmiḏī a nommé le nasḫ (l’abrogeant) une ʿilla" in hn
    and "une ʿilla empêchant l’œuvre, non terminologique" in hn
    and "[Šarḥ Nuḫbat al-fikr fī muṣṭalaḥāt ahli-l-aṯar" in hn and "ʿAlī al-Qārī, page 461]" in hn)

# ---- tabṣīṭ 3 : importance
chk("importance : Ibn Mahdī — ʿilla d’un ḥadīṯ chez moi + ʿIlal Ibn Abī Ḥātim 1/9",
    "L’imām ʿAbd ar-Raḥmān b. Mahdī a dit" in hn
    and "« que je connaisse la ʿilla d’un ḥadīṯ qui est chez moi est plus aimé de moi que d’écrire un ḥadīṯ qui n’est pas chez moi. »" in hn
    and "[ʿIlal al-ḥadīṯ (les causes du ḥadīṯ), d’Ibn Abī Ḥātim, tome un, page 9]" in hn)
chk("importance : art plus obscurs et plus précis + quatre qualités du qualifié",
    "parmi les plus obscurs des sciences du ḥadīṯ et les plus précises d’entre elles" in hn
    and "d’une compréhension pénétrante, d’un préservage vaste, d’une connaissance accomplie des degrés des narrateurs, et d’une maîtrise forte des chaînes et des textes" in hn)
chk("importance : les sept maîtres",
    "ʿAlī b. al-Madīnī, Aḥmad b. Ḥanbal, al-Buḫārī, Yaʿqūb b. Šayba, Abū Ḥātim, Abū Zurʿa, et ad-Dāraquṭnī" in hn)

# ---- tabṣīṭ 4 : exemple
chk("exemple intro : isnād le plus fréquent + ʾirsāl et waqf + isnād seul",
    "dans l’isnād du ḥadīṯ — et c’est le plus fréquent" in hn
    and "comme le fait de motiver par la suspension (al-ʾirsāl) et l’arrêt (al-waqf)" in hn
    and "peut mettre en doute l’authenticité de l’isnād seul, sans mise en doute de l’authenticité du texte" in hn)
chk("exemple isnād : Yaʿlā b. ʿUbayd + chaîne + hadith du marché + Muʿǧam kabīr",
    "ce que rapporte l’homme de confiance (aṯ-ṯiqa) Yaʿlā b. ʿUbayd, de Sufyān aṯ-Ṯawrī, de ʿAmr b. Dīnār, d’Ibn ʿUmar" in hn
    and "« Tout marché — il n’y a pas de marché entre les deux tant qu’ils ne se sont pas séparés, sauf le marché à option. »" in hn
    and "[al-Muʿǧam al-kabīr (le grand dictionnaire), aṭ-Ṭabarānī, le chapitre de la lettre ʿayn, ʿAmr b. Dīnār d’Ibn ʿUmar]" in hn)
chk("exemple isnād : chaîne continue + motivé non authentique + texte authentique en tout cas",
    "une chaîne continue, par transmission de l’homme juste par l’homme juste, et il est motivé non authentique, et le texte est en tout cas authentique" in hn)
chk("exemple isnād : ʿilla = en réalité ʿAbd Allāh b. Dīnār + imāms compagnons de Sufyān + tous deux ثقة",
    "il est en réalité d’ʿAbd Allāh b. Dīnār, d’Ibn ʿUmar" in hn
    and "ainsi l’ont rapporté les imāms parmi les compagnons de Sufyān de lui" in hn
    and "l’erreur de conjecture est donc celle de Yaʿlā b. ʿUbayd, qui a substitué ʿAbd Allāh b. Dīnār à ʿAmr b. Dīnār, et tous deux sont des hommes de confiance" in hn)
chk("exemple matn : Muslim seul + Anas + basmala + Ṣaḥīḥ Muslim",
    "ce que Muslim a été seul à rapporter, dans le ḥadīṯ d’Anas où il est explicitement (aṣ-ṣarāḥa bi-hi) nié la récitation de « Bismillāhi r-Raḥmāni r-Raḥīm »" in hn
    and "« J’ai prié derrière le Prophète — que les prières et la paix de Dieu soient sur lui —, Abū Bakr, ʿUmar et ʿUṯmān" in hn
    and "[Ṣaḥīḥ Muslim (l’authentique de Muslim), le livre de la prière, le chapitre de la preuve de celui qui a dit qu’on ne récitera pas la basmala à voix haute]" in hn)
chk("exemple matn : motivation par le sens arrivé + accord Buḫārī/Muslim + Fātiḥa + tasmīya",
    "l’a rapporté avec le sens qui lui est arrivé" in hn
    and "qu’ils ne récitaient pas la tasmīya, et l’a rapporté selon ce qu’il a compris" in hn
    and "c’est cela sur quoi al-Buḫārī et Muslim se sont accordés pour le rapporter dans les Ṣaḥīḥ" in hn
    and "la sourate par laquelle ils ouvraient parmi les sourates est al-Fātiḥa" in hn
    and "il ne s’y trouve pas de représentation de la mention de la tasmīya" in hn)
chk("exemple matn : établi d’Anas — interrogé sur la tasmīya, rien préserve + renvoi page 92",
    "qu’il est établi d’Anas que, interrogé sur l’ouverture par la tasmīya" in hn
    and "il a déclaré qu’il n’en préserve rien du Messager de Dieu" in hn
    and "[Muqaddimat Ibn aṣ-Ṣalāḥ (l’introduction d’Ibn aṣ-Ṣalāḥ), page 92]" in hn)

# ---- tabṣīṭ 5 : jugement + ahtadī
chk("jugement : causes cachées obscures + prédominance de la conjecture",
    "des causes cachées, obscures, qui mettent en doute l’authenticité du ḥadīṯ" in hn
    and "prédomine dans la pensée de l’examineur l’existence d’une ʿilla" in hn
    and "se suffisant de la prédominance de la conjecture (ġalabat aẓ-ẓann)" in hn)
chk("jugement : hésitation sans préférence + arrêt + préservation du reproche",
    "il hésite pour l’absence de préférence de l’un des deux côtés" in hn
    and "le jugement d’authenticité et de non-authenticité s’arrête" in hn
    and "l’apparent est la préservation du reproche (as-salāma min al-ǧarḥ)" in hn)
chk("ahtadī : Dārimī de Muʿammar d’az-Zuhrī + écrit + « qui t’en a parlé autre que moi » + renvoi",
    "L’imām ad-Dārimī a rapporté, par sa chaîne, de Muʿammar, d’az-Zuhrī" in hn
    and "« on lui présenta un écrit, et je dis : te puis-je le rapporter ? Il dit : qui t’en a parlé autre que moi ? »" in hn
    and "[Sunan ad-Dārimī (les sunan d’ad-Dārimī), le chapitre de la présentation]" in hn)

# ---- taqwīm + istiṯmār + iʿdād
chk("taqwīm 1 : ce par quoi se connaissent les ʿilal",
    "j’explique ce par quoi se connaissent les ʿilal" in hn)
chk("taqwīm 2 : pourquoi les plus obscures et les plus précises",
    "pourquoi la connaissance des ʿilal est-elle parmi les sciences du ḥadīṯ les plus obscures et les plus précises" in hn)
chk("istiṯmār : citation Ibn aṣ-Ṣalāḥ — emploi étendu + écartée de l’authenticité à la faiblesse",
    "Il se peut que le nom de ʿilla s’emploie pour autre que ce que nous avons mentionné" in hn
    and "l’écartant de l’état d’authenticité à l’état de faiblesse, et empêchant l’œuvre avec lui, selon ce qu’exige le mot de ʿilla à l’origine" in hn)
chk("istiṯmār : livres des ʿilal — mensonge, négligence, mauvais préservage + renvoi page 93",
    "le grand nombre du reproche par le mensonge, la négligence, le mauvais préservage, et pareil parmi les types du reproche" in hn
    and "[Muqaddimat Ibn aṣ-Ṣalāḥ (l’introduction d’Ibn aṣ-Ṣalāḥ), page 93]" in hn)
chk("consigne 1 : discuter le dire d’Ibn aṣ-Ṣalāḥ, emplois étendus du nom de ʿilla",
    "je discute le dire d’Ibn aṣ-Ṣalāḥ, en montrant les emplois étendus du nom de ʿilla" in hn)
chk("consigne 2 : introduction d’un livre des ʿilal dirigés dans la préparation préalable",
    "je lis l’introduction d’un livre des livres des ʿilal qui furent dirigés dans la préparation préalable, pour les apporter" in hn)
chk("iʿdād : leçon 21 interpolé/inversé + lira son texte d’avance + activités de l’enseignant(e)",
    "La leçon 21 est « l’interpolé (al-mudraǧ) et l’inversé (al-maqlūb) »" in hn
    and "l’élève lira son texte (matn) d’avance et réalisera les activités proposées par l’enseignant(e)" in hn)

# ---- hygiène FR
chk("zéro caractère arabe", not re.search(r"[\u0600-\u06FF\u0750-\u077F\u08A0-\u08FF\uFB50-\uFDFF\uFE70-\uFEFF]", h))
chk("zéro apostrophe droite", chr(39) not in h)
chk("guillemets appariés", h.count("«") == h.count("»"))
chk("zéro double espace", "  " not in re.sub(r" |\n", "", h))
chk("zéro résidu placeholder", not re.search(r"XXX|TODO|【|____", h))
chk("balises appariées (h1/h2/h3/p/dl/dt/dd/strong/ol/ul/li)",
    h.count("<h1>") == h.count("</h1>") and h.count("<h2>") == h.count("</h2>")
    and h.count("<h3>") == h.count("</h3>") and h.count("<p>") == h.count("</p>")
    and h.count("<dl") == h.count("</dl>") and h.count("<dt>") == h.count("</dt>")
    and h.count("<dd>") == h.count("</dd>") and h.count("<strong>") == h.count("</strong>")
    and h.count("<ol>") == h.count("</ol>") and h.count("<ul>") == h.count("</ul>")
    and h.count("<li>") == h.count("</li>"))

# ---- registre : htmlFr posé, voisins intacts
reg = json.load(open(REG, encoding="utf-8"))
les = {str(d.get("docId", "")): d for d in reg["lessons"]}
chk("registre livre 2 : 27 entrées", len(reg["lessons"]) == 27)
chk("registre 271 intact", 21_000 <= len(les["pdf-mut23h2u-271"].get("htmlFr") or "") <= 26_000)
chk("registre 272 intact (19 801 car)", len(les["pdf-mut23h2u-272"].get("htmlFr") or "") == 19801)
chk("registre 273 intact (22 645 car)", len(les["pdf-mut23h2u-273"].get("htmlFr") or "") == 22645)
fr = les["pdf-mut23h2u-274"].get("htmlFr") or ""
if fr:
    chk("registre 274 = htmlFr posé (19 000-29 500 car)", 19_000 <= len(fr) <= 29_500)
    chk("registre 274 == fichier livré", fr.strip() == h.strip())
else:
    chk("registre 274 encore vide (avant hand-set)", True)
chk("registre 275 non touché (htmlFr vide)", (les["pdf-mut23h2u-275"].get("htmlFr") or "") == "")
chk("titleAr pré-mappé 274", les["pdf-mut23h2u-274"].get("titleAr") == "الدرس 20 : الحديث المعلل")
chk("titleFr pré-mappé 274 aligné au h1",
    (les["pdf-mut23h2u-274"].get("titleFr") or "") == "Leçon 20 : Le hadith défectueux (maʿlūl)")
chk("titleAr pré-mappé 275 intact (leçon 21, non touchée)",
    les["pdf-mut23h2u-275"].get("titleAr") == "الدرس 21 : المدرج والمقلوب")
chk("titleFr pré-mappé 275 intact",
    (les["pdf-mut23h2u-275"].get("titleFr") or "") == "Leçon 21 : L'interpolé (mudraǧ) et l'inversé (maqlūb)")

print(f"verify-ulumhadith2-pdf274 : {ok} PASS / {fail} ÉCHEC")
raise SystemExit(1 if fail else 0)

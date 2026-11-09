#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Minhāj — Vérification de la leçon ulum-hadith-tanawi-2 / pdf-mut23h2u-275
(الدرس 21 : المدرج والمقلوب — al-mudraǧ wa-l-maqlūb, p.107-114 du manuel
ulum-hadith-2-thanawi_text.pdf) : bornes p.107-114 par sondage image
(p.106 = clôture de la leçon 20, livrée R655, docId pdf-mut23h2u-274 ;
p.107 = bannière médaillon « 21 » en chiffres occidentaux + 4 objectifs +
tamhīd cinq types + matn Ibn Ḥaǧar au contradicteur + gloses + استخلاص ;
p.108-110 = أولا définition (luga Ibn Fāris 2/275 image, istiilāh) +
أ. مدرج الإسناد 4 cas (الترمذي عمر بن شرحبيل [القاري ص 464], ابن عيينة
[ص 467], سعيد بن أبي مريم [موطأ مالك + ص 467], ثابت بن موسى [الإكليل ص 63]) +
ب. مدرج المتن 3 positions (الخطيب أسبغوا الوضوء [الفصل 1/159], الدارقطني
بسرة, أبو خيثمة التشهد [أبو داود + ص 469]) ; p.111 = أسباب الإدراج diagramme
3 branches + طرق معرفة المدرج 4 (الراوي نفسه ابن مسعود ندا [مسند أحمد],
إمام مطلع أبو خيثمة [مسند الكبيرين + ص 96]) ; p.112 = استحالة الترمذي
« لو تعلمون ما أعلم » [الفصل 1/80] + السيوطي + ثانيا المقلوب définition
(لغة الفيومي 2/512 image, اصطلاحا) ; p.112-113 = أنواع المقلوب (السند
كعب بن مرة, المتن ورجل تصدق [البخاري الزكاة + ابن خزيمة + السخاوي 1/345],
معا تاريخ بغداد 2/340 امتحان البخاري مائة حديث) + دواعي القلب diagramme
3 + حكم المقلوب 3 cas ; p.113-114 = علي بن أبي طالب [الدارمي باب مذاكرة
العلم] ; p.114 = التقويم 3 + الاستثمار ألفية العراقي [التبصرة 1/115] +
الاستخرج + الإعداد القبلي 2 items (p114-taqwim-idad) ; p.115 = bannière
leçon 22 المزيد (médaillon 22, sondage, non touchée, registre vide).
Adjudications documentées (QUARANTE-CINQ lectures d’images, tr-tmp/qa-crops-r656/)
: objectif 4 complété par l’image ; Ibn Fāris « 2/275 » (p108 image) contre
« 2/572 » couche ; القاري « ص 464 » palindrome ; « ص 467 » ; الحاكم « ص 63 »
contre « 36 » couche ; أبو قتن عمرو بن الهيثم (z2c) ; الخطيب « 1/159 » contre
« 1/951 » ; ص 469 contre « 964 » ; البخاري « كتاب المحاربين » (z1d) corroboré
en ligne ; Muqaddima « ص 96 » contre « 69ā » ; الفيومي « 2/512 » contre « 2/215 »
; السخاوي « 1/345 » contre « 345/1 » (ordre mots) ; « فتح الغيث » tel qu’imprimé
(forme attestée en ligne, canonique « فتح المغيث ») ; تاريخ بغداد « 2/340 » ;
« مائة حديث » corroboré en ligne ; ألفية العراقي 4 bayts corroborés en ligne
(إمام الفن، فردّها وجوّد الإسنادا) ; ʿIrāqī « 1/115 » contre « 1/511 » ;
ابن مسعود ندا [مسند أحمد] ; علي « تذاكروا » [الدارمي باب مذاكرة العلم], fin de
clause fragmentée déclarée ; structure de clôture : التقويم 3 items, الاستثمار
versification + 1 item استخرج, الإعداد القبلي 2 items (p114-taqwim-idad) ;
ZÉRO ĀYA (cache coranique non sollicité).
Usage: python3 scripts-translate/verify-ulumhadith2-pdf275.py
"""
import json
import re

HTML = "/home/z/my-project/tr-tmp/lesson-uh2-pdf-mut23h2u-275-fr.html"
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
chk("h1 = titleFr pré-mappé « Leçon 21 : L’interpolé (mudraǧ) et l’inversé (maqlūb) »",
    hn.startswith("<h1>Leçon 21 : L’interpolé (mudraǧ) et l’inversé (maqlūb)"))
chk("h1 mentionne deuxième année", "deuxième année" in h[:500])
chk("h1 mentionne la dissidence et les cinq types",
    "dissidence du narrateur envers les hommes de confiance" in h[:700] and "cinq types" in h[:700])
chk("h1 mentionne les quatre cas de l’interpolé de la chaîne",
    "quatre cas" in h[:1400] and "Tirmiḏī" in h[:2200] and "Thābit b. Mūsā" in h[:2600])
chk("h1 mentionne l’interpolé du texte (début, milieu, fin) + Abū Ḫayṯama",
    "dans le début" in h[:2900] and "son milieu" in h[:3100] and "Abū Ḫayṯama" in h[:3200])
chk("h1 mentionne l’inversé et les trois espèces + Bagdad",
    "l’inversé (al-maqlūb)" in h[:3400] and "Bagdad" in h[:3600])
chk("h1 mentionne motifs, jugement et ʿAlī b. Abī Ṭālib",
    "l’étrangereté, l’examen, l’erreur" in h[:3800] and "ʿAlī b. Abī Ṭālib" in h[:4200])
chk("dl.lesson-meta présent", '<dl class="lesson-meta">' in h and "<dt>Source du cours</dt>" in h)
chk("item archive.org cité", "1_20220304_20220304_2251" in h)
chk("source locale citée", "ulum-hadith-2-thanawi_text.pdf" in h)
chk("bornes p.107-114 documentées", "pages 107 à 114" in h)
chk("p.106 clôture leçon 20 (R655, 274)", "R655" in h and "pdf-mut23h2u-274" in h)
chk("p.115 leçon 22 sondée, non touchée, registre vide",
    "la leçon 22" in h and "non touchée" in h and "registre vide" in h)
chk("sondage « jamais devinées »", "jamais devinées" in h)
chk("matière multi-couches citée (raw + decoded + readable)",
    "uh2-l275-raw.txt" in h and "uh2-l275-decoded.txt" in h and "uh2-l275-readable.txt" in h)
chk("QUARANTE-CINQ lectures d’images consignées + noms de crops",
    "QUARANTE-CINQ lectures d’images" in h and "p107-banner-objectifs.png" in h
    and "p107-tamhid-matn.png" in h and "p107-gloses.png" in h
    and "p108-def-anatypes.png" in h and "p108-mudraj-isnad-awwal.png" in h
    and "p109-thalith-exemple.png" in h and "p109-salat-haja.png" in h
    and "p109-thalith-rabi.png" in h and "p110-iklil-mudraj-matan.png" in h
    and "p110-awwaluhu-khatib.png" in h and "p110-khatib-quote.png" in h
    and "p111-asbab-idraj.png" in h and "p112-istihala-tirmidhi.png" in h
    and "p112-suyuti-maqlub-def.png" in h and "p113-maqlub-matan-bukhari.png" in h
    and "p113-maqlub-sund-mithal.png" in h and "p114-hukm-ali-darmi.png" in h
    and "p114-istithmar.png" in h and "p114-taqwim-idad.png" in h and "p115-banner-l22.png" in h)
chk("zooms discriminatifs nommés (z1d, z2c, z4, z5d, z6d, z7, z7b, z8b, z9c)",
    "z1d" in h and "z2c" in h and "(z4)" in h and "z5d" in h and "z6d" in h
    and "(z7, z7b)" in h and "z8b" in h and "z9c" in h and "uh2-zoom-275.py" in h)
chk("objectif 4 complété par l’image contre couche fragmentée",
    "quatrième objectif complété par l’image" in h and "couche fragmentée" in h)
chk("renvoi Ibn Fāris 2/275 contre « 2/572 » (inversion intégrale)",
    "2/275" in h and "2/572" in h and "inversion intégrale" in h)
chk("renvois al-Qārī 464 (palindrome) et 467",
    "page 464" in h and "palindrome" in h and "page 467" in h)
chk("renvoi al-Ḥākim 63 contre « 36 »", "page 63" in h and "36" in h)
chk("Abū Qatan ʿAmr b. al-Hayṯam adjudiqué au zoom lettre à lettre",
    "Abū Qatan ʿAmr b. al-Hayṯam" in h and "lettre à lettre" in h)
chk("renvoi al-Ḫaṭīb 1/159 contre « 1/951 »", "1/159" in h and "1/951" in h)
chk("renvoi 469 contre « 964 » (inversion intégrale)", "page 469" in h and "964" in h)
chk("livre al-Buḫārī « des combattants » zoom + corroboration en ligne",
    "le livre des combattants" in h and "corroboré en ligne" in h)
chk("Muqaddima 96 contre « 69ā » (inversion intégrale)", "page 96" in h and "69ā" in h)
chk("al-Fayyūmī 2/512 contre « 2/215 »", "2/512" in h and "2/215" in h)
chk("titre al-Miṣbāḥ al-munīr rendu couche + canonique contre lecture floue",
    "al-Miṣbāḥ al-munīr fī ġarīb aš-šarḥ al-kabīr" in h and "titre canonique connu" in h)
chk("as-Saḫāwī 1/345 contre « 345/1 » (ordre des mots seul)",
    "1/345" in h and "345/1" in h and "ordre des mots seul" in h)
chk("Fatḥ al-Ġayṯ tel qu’imprimé + forme canonique Fatḥ al-Muġīṯ documentée",
    "Fatḥ al-Ġayṯ" in h and "tel qu’imprimé" in h and "Fatḥ al-Muġīṯ" in h)
chk("phrase as-Saḫāwī corroborée en ligne",
    "ses exemples dans le texte sont peu nombreux" in h and "corroborée en ligne" in h)
chk("récit Bagdad « cent ḥadīṯ » complété par l’image + corroboration",
    "cent ḥadīṯ" in h and "corroboré en ligne par le récit complet" in h)
chk("vers d’al-ʿIrāqī corroboré en ligne (imām de l’art, restitution, élocution)",
    "l’imām de l’art" in h and "éloqua les deux chaînes" in h and "corroboration en ligne du cours commenté" in h)
chk("ʿIrāqī 1/115 contre « 1/511 » (inversion intégrale)", "1/115" in h and "1/511" in h)
chk("ḥadīṯ Ibn Masʿūd rival + « et une autre version » + Muṣnad Aḥmad",
    "qui a fait un rival à Dieu, Dieu le met dans le Feu" in hn
    and "« et une autre version que je dis sans l’avoir entendue de lui" in hn
    and "le Muṣnad d’ʿAbd Allāh b. Masʿūd" in hn)
chk("ʿAlī « tadhākarū » + fin fragmentée déclarée + Dārimī mudākara",
    "tadhākarū ce ḥadīṯ" in hn and "fin de la clause imprimée fragmentée" in hn
    and "l’étude mutuelle de la science" in hn)
chk("structure de clôture : évaluation 3 items, exploitation versification + 1 item, iʿdād 2 items",
    "l’évaluation porte trois items numérotés" in h
    and "un seul item d’extraction" in h and "porte deux items" in h)
chk("zéro āya (cache coranique non sollicité)",
    "ZÉRO ĀYA" in h and "cache coranique non sollicité" in h)

# ---- objectifs (4)
chk("objectif 1 : reconnaître le concept de l’interpolation et son jugement",
    "que je reconnaisse le concept de l’interpolation (al-idrāǧ) et son jugement" in hn)
chk("objectif 2 : distinguer isnād / matn",
    "que je distingue l’interpolation dans la chaîne (isnād) de l’interpolation dans le texte (matn)" in hn)
chk("objectif 3 : reconnaître le concept du renversement et ses causes",
    "que je reconnaisse le concept du renversement (al-qalb) dans le ḥadīṯ et ses causes" in hn)
chk("objectif 4 : maîtriser les ḥadīṯ et les reprendre sans renversement ni substitution",
    "que je maîtrise les ḥadīṯ que j’apprends et les reprenne avec leurs formules sans renversement ni substitution" in hn)

# ---- tamhīd + matn
chk("tamhīd : dissidence = cause du reproche + cinq types",
    "parmi les causes du reproche (aṭ-ṭaʿn) d’un narrateur se trouve sa dissidence (muḫālafa)" in hn
    and "cinq types parmi les sciences du ḥadīṯ" in hn)
chk("tamhīd : liste des cinq types (mudraǧ, maqlūb, zāʾid, muḍṭarab, muṣḥaf)",
    "l’interpolé, l’inversé, l’addition dans les chaînes continues, l’incohérent (al-muḍṭarab), et le désordonné (al-muṣḥaf)" in hn)
chk("tamhīd : double question (nom du premier type / dissidence par avancement ou recul)",
    "Qu’est-ce donc que l’interpolé" in hn
    and "comment nomme-t-on la dissidence qui se fait par avancement ou recul" in hn)
chk("matn : contradicteur — changement du contexte → chaîne interpolée",
    "« Puis le contradicteur (al-ḫālifa) : si elle se fait par le changement du contexte (as-sayāq), la chaîne (al-isnād) est interpolée (mudraǧ)" in hn)
chk("matn : fusion suspendu/rattaché → texte interpolé + avancement/recul → inversé",
    "ou en fusionnant un propos suspendu dans un propos rattaché, le texte (al-matn) est interpolé" in hn
    and "ou par avancement ou recul, alors c’est l’inversé (al-maqlūb). »" in hn)

# ---- gloses + istiḫlāṣ
chk("glose 1 : sayāq origine suwaq, waw changée en yāʾ, contexte = suite du discours",
    "son origine est « as-suwaq », la waw a été changée en yāʾ à cause de la multiplicité de la sīn" in hn
    and "le contexte du discours est sa suite" in hn)
chk("glose 2 : damǧ = entrée d’une chose dans une chose + intiwāʾ et sitr",
    "l’entrée d’une chose dans une chose, et son origine « damǧ » désigne le renvoiement (al-intiwāʾ) et l’occultation (as-sitr)" in hn)
chk("glose 3 : avancement ou recul dans la chaîne ou le texte",
    "ou si la dissidence se fait par avancement ou recul, dans la chaîne ou dans le texte" in hn)
chk("istiḫlāṣ : définition de l’interpolé et ses types",
    "j’extrais du texte (matn) la définition de l’interpolé et ses types" in hn)
chk("istiḫlāṣ : définition de l’inversé",
    "j’extrais du texte la définition de l’inversé" in hn)

# ---- tabṣīṭ intro
chk("intro tabṣīṭ : double question + réponse + deux parties",
    "Le tamhīd a posé la double question" in hn
    and "le changement du contexte fait de la chaîne un interpolé" in hn
    and "deux parties : l’interpolé" in hn)

# ---- tabṣīṭ 1 : définition
chk("luga : nom de patient + occultation/couverture + Maqāyīs 2/275",
    "un nom de patient de « ad-raǧa » qui désigne l’occultation et la couverture" in hn
    and "[Maqāyīs al-luġa (les étalons de la langue), Ibn Fāris, tome deux, page 275, avec adaptation]" in hn)
chk("istiilāh : addition qui ne vient pas de lui + relation claire",
    "ce qui se trouve dans sa chaîne ou son texte en qualité d’addition qui ne vient pas de lui" in hn
    and "La relation entre le sens linguistique et le sens terminologique est claire" in hn)
chk("istiilāh : s’obscurcit, compte le tout raccordé, croyant que cela fait partie",
    "cela s’obscurcit ainsi pour celui qui ne sait pas, il compte le tout comme raccordé et le rapporte continu, croyant que cela fait partie du ḥadīṯ alors que cela n’en vient pas" in hn)

# ---- tabṣīṭ 2 : types
chk("types : deux parties — chaîne et texte",
    "L’interpolé se divise en deux parties : l’interpolé de la chaîne (mudraǧ al-isnād), et l’interpolé du texte (mudraǧ al-matn)" in hn)
chk("a. chaîne : changement du contexte + renvoi au matn",
    "c’est le changement du contexte de la chaîne, et à cela renvoie sa parole" in hn)
chk("cas 1 : groupe à chaînes différentes + rassemblement + ḥadīṯ Tirmiḏī « rival à Dieu »",
    "ce qu’un groupe rapporte par des chaînes différentes, et qu’un narrateur suspect de dissidence rapporte d’eux" in hn
    and "« quel est le plus grand des péchés ? »" in hn
    and "que tu fasses un rival à Dieu alors qu’Il t’a créé" in hn
    and "[Sunan at-Tirmiḏī (les sunan d’at-Tirmiḏī), les chapitres de l’exégèse du Coran, le chapitre : de la sourate al-Furqān]" in hn)
chk("cas 1 : Muḥammad b. Kaṯīr al-ʿAbdī + Wāṣil interpolée + Qaṭṭān + Buḫārī combattants + 464",
    "Muḥammad b. Kaṯīr al-ʿAbdī" in hn
    and "la narration de Wāṣil est donc interpolée sur la narration de Manṣūr et de al-Aʿmaš" in hn
    and "Yaḥyā b. al-Qaṭṭān a manifesté les deux chaînes ensemble" in hn
    and "dans le livre des combattants, d’ʿAmr b. ʿAlī" in hn
    and "al-Qārī, page 464]" in hn)
chk("cas 2 : chaîne à laquelle manque un bout + seconde chaîne + ḥadīṯ Ibn ʿUyayna + 467",
    "que le texte du ḥadīṯ ait, chez le narrateur, une chaîne à laquelle il manque un bout" in hn
    and "il intercale ce qu’il a rapporté de lui sur la première chaîne, et efface la seconde" in hn
    and "le ḥadīṯ d’Ibn ʿUyayna, de Zāʾida b. Qudāma, de ʿĀṣim b. Kulayb, de son père, de Wāʾil b. Ḥuǧr dans la description de la prière" in hn
    and "al-Qārī, page 467]" in hn)
chk("cas 3 : deux textes à deux chaînes + ḥadīṯ Saʿīd b. Abī Maryam « ne vous haïssez pas » + Muwaṭṭaʾ + soupçon",
    "que le narrateur ait deux textes différents à deux chaînes différentes" in hn
    and "le ḥadīṯ rapporté par Saʿīd b. Abī Maryam, de Mālik, d’az-Zuhrī, d’Anas" in hn
    and "« ne vous haïssez pas, ne vous enviez pas, ne vous tournez pas le dos, (et ne vous faites pas concurrence)" in hn
    and "interpolé par Ibn Abī Maryam d’un autre ḥadīṯ de Mālik, d’Abū az-Zinād, de al-Aʿraǧ, d’Abū Hurayra" in hn
    and "« gardez-vous du soupçon, car le soupçon est le plus mensonger des propos, ne fouillez pas, ne vous espionnez pas, ne vous faites pas concurrence »" in hn
    and "[al-Muwaṭṭaʾ (le sélect), al-imām Mālik, le livre des belles qualités, le chapitre de ce qui est rapporté sur l’émigration]" in hn
    and "le premier n’a pas « ne vous faites pas concurrence », et cela n’est que dans le second ḥadīṯ" in hn)
chk("cas 4 : suspension de la chaîne + accident + Thābit b. Mūsā + Šurayk le juge + « prières de nuit » + Iklīl 63",
    "que l’on suspende la chaîne et qu’un accident lui survienne, et qu’il dise des paroles de lui-même" in hn
    and "ce qu’a mentionné al-Ḥākim : Thābit b. Mūsā est entré chez Šurayk b. ʿAbd Allāh le juge" in hn
    and "« qui multiplie ses prières de nuit, son visage s’embellit de jour. »" in hn
    and "ce ḥadīṯ n’a pas d’origine autre que cette face" in hn
    and "l’ont volé de Thābit b. Mūsā et rapporté de Šurayk" in hn
    and "[al-Madḫal ilā kitāb al-Iklīl (l’entrée dans le livre de la couronne), Abū ʿAbd Allāh al-Ḥākim, page 63]" in hn)
chk("b. texte : propos qui ne vient pas de lui + fusion suspendu dans rattaché",
    "c’est qu’il se trouve dans le texte un propos qui ne vient pas de lui" in hn
    and "« ou en fusionnant un propos suspendu dans un propos rattaché, le texte est interpolé »" in hn)
chk("début : ample ablution + talons + Ḫaṭīb 1/159 + Buḫārī ablutions + Abū Qatan ʿAmr b. al-Hayṯam",
    "« faites une ample ablution, et malheur aux talons du Feu »" in hn
    and "[al-Faṣl li-l-waṣl al-mudraǧ fī n-naql (le jugement rendu au raccord interpolé dans la transmission), al-Ḫaṭīb al-Baġdādī, tome un, page 159]" in hn
    and "al-Buḫārī l’a rapportée dans son Authentique de Ādam b. Abī Iyās" in hn
    and "[Ṣaḥīḥ al-Buḫārī (l’authentique d’al-Buḫārī), le livre des ablutions, le chapitre du lavage des talons]" in hn
    and "la confusion est celle d’Abū Qatan ʿAmr b. al-Hayṯam et de Šabbāba b. Sawwār" in hn
    and "sa parole « faites une ample ablution » est la parole d’Abū Hurayra" in hn
    and "« malheur aux talons du Feu » est la parole du Prophète" in hn)
chk("milieu : Dāraquṭnī Busra bint Ṣafwān + touche son sexe + erreur dans les deux anus + préservé ʿUrwa",
    "ce que rapporte ad-Dāraquṭnī dans ses « Sunan » de la narration de ʿAbd al-Ḥamīd b. Ǧaʿfar" in hn
    and "de Busra bint Ṣafwān, qui a dit : j’ai entendu le Messager de Dieu" in hn
    and "« qui touche son sexe, ou son anus, ou ses testicules, qu’il fasse ses ablutions. »" in hn
    and "il s’est trompé dans la mention des deux anus et du testicule, et a intercalé cela dans le ḥadīṯ de Busra" in hn
    and "le préservé est que cela est de la parole d’ʿUrwa" in hn)
chk("fin : Abū Ḫayṯama tashahhud + Ibn Masʿūd + Abū Dāwūd + 469 + le plus fréquent",
    "c’est le plus fréquent en occurrence ou en usage" in hn
    and "ce qu’a rapporté Abū Ḫayṯama Zuhayr b. Muʿāwiya, de al-Ḥasan b. al-Ḥurr, de al-Qāsim b. Muḫaymara, de ʿAlqama, de ʿAbd Allāh b. Masʿūd" in hn
    and "« dis : les salutations à Dieu" in hn
    and "[Sunan Abī Dāwūd (les sunan d’Abū Dāwūd), le livre de la prière, le chapitre : comment s’asseoir dans le tashahhud]" in hn
    and "cela ne fait que faire partie de la parole d’Ibn Masʿūd, non de la parole du Prophète" in hn
    and "page 469]" in hn)

# ---- causes + voies
chk("causes : multiples + énoncé, déduction, mot étranger + fusion sans séparation",
    "l’interpolation a des causes multiples, parmi elles : l’énoncé d’un jugement religieux" in hn
    and "la déduction d’un jugement religieux du ḥadīṯ avant son établissement" in hn
    and "l’explication d’un mot étranger dans le ḥadīṯ" in hn
    and "sans séparation ni éclaircissement" in hn)
chk("voies : quatre choses",
    "l’interpolé se connaît par quatre choses" in hn)
chk("voie 1 : rapport détaillé + étendue de l’interpolé + exemple du début",
    "la survenance d’un rapport détaillé, qui manifeste l’étendue de l’interpolé dans le ḥadīṯ" in hn
    and "ce qui a précédé dans l’interpolé du texte, dans le cas où l’interpolation se faisait dans son début" in hn)
chk("voie 2 : narrateur même + ḥadīṯ Ibn Masʿūd rival + autre version + Muṣnad",
    "la désignation de l’interpolation par le narrateur même, comme le ḥadīṯ d’Ibn Masʿūd" in hn
    and "qui a fait un rival à Dieu, Dieu le met dans le Feu », et il a dit : « et une autre version que je dis sans l’avoir entendue de lui : qui meurt sans faire de rival à Dieu, Dieu le fait entrer dans le Paradis »" in hn
    and "[le Muṣnad de l’imām Aḥmad b. Ḥanbal, le Muṣnad d’ʿAbd Allāh b. Masʿūd]" in hn)
chk("voie 3 : imāms informés + Abū Ḫayṯama tashahhud complet + clause Zuhayr fragmentée + Muqaddima 96",
    "la désignation de quelques-uns des imāms informés de cela" in hn
    and "a dit Zuhayr : je l’ai préservé par cœur de lui [fin de la clause imprimée dégradée, déclarée telle quelle]" in hn
    and "[as-Sunan, Aḥmad b. Ḥanbal, le Muṣnad des deux grands parmi les Compagnons, le Muṣnad d’ʿAbd Allāh b. Masʿūd]" in hn
    and "[Muqaddimat Ibn aṣ-Ṣalāḥ (l’introduction d’Ibn aṣ-Ṣalāḥ), page 96]" in hn)
chk("voie 4 : impossibilité + Tirmiḏī arbre taillé à coups de hache + Suyūṭī Abū Ḏarr + Faṣl 1/80 + mardūd",
    "ou l’impossibilité que le Prophète — que les prières et la paix de Dieu soient sur lui — dise cela" in hn
    and "« ...je souhaiterais être un arbre qui est coupé à coups de hache »" in hn
    and "[Sunan at-Tirmiḏī (les sunan d’at-Tirmiḏī), les chapitres de l’ascétisme sur le Messager de Dieu" in hn
    and "si vous saviez ce que je sais, vous ririez peu" in hn
    and "« ses mots : je souhaiterais... » sont interpolés de la parole d’Abū Ḏarr" in hn
    and "al-Ḫaṭīb al-Baġdādī, tome un, page 80]" in hn
    and "Il ne convient pas de faire exprès d’une des interpolations mentionnées, et cela relève du rebuté (al-mardūd)" in hn)

# ---- maqlūb : définition + types
chk("maqlūb seconde partie annoncée",
    "La seconde partie : le ḥadīṯ inversé (al-ḥadīṯ al-maqlūb)" in hn)
chk("maqlūb luga : retournement de sa face + Miṣbāḥ al-munīr 2/512",
    "le retournement de la chose de sa face" in hn
    and "[al-Miṣbāḥ al-munīr fī ġarīb aš-šarḥ al-kabīr (la lampe éclairante dans les mots rares du grand commentaire), al-Fayyūmī, tome deux, page 512, avec adaptation]" in hn)
chk("maqlūb istiilāh : échange d’un mot par un autre, par avancement ou recul",
    "l’échange d’un mot par un autre dans la chaîne du ḥadīṯ ou son texte, par avancement ou recul" in hn)
chk("maqlūb a. chaîne : formes multiples + Kaʿb b. Murra / Murra b. Kaʿb",
    "c’est ce qui a subi le renversement dans sa chaîne, et il a des formes multiples" in hn
    and "que le narrateur avance ou recule dans les noms" in hn)
chk("maqlūb a. étrangereté : Sālim / Nāfiʿ + interdit",
    "avec le dessein d’étrangereté" in hn
    and "la narration de Sālim b. ʿAbd Allāh d’Ibn ʿUmar" in hn
    and "de la narration de Nāfiʿ d’Ibn ʿUmar, non de la narration de Sālim d’Ibn ʿUmar" in hn
    and "Et cela est interdit, et il ne convient pas" in hn)
chk("maqlūb b. texte : réel + aumône cachée + Buḫārī / Ibn Ḫuzayma + exemples peu nombreux + Saḫāwī 1/345",
    "c’est ce qui a subi l’échange dans son texte" in hn
    and "« et un homme qui a fait une aumône légale et la cache de sorte que sa gauche ne connaisse pas ce que dépense sa droite »" in hn
    and "[Ṣaḥīḥ al-Buḫārī (l’authentique d’al-Buḫārī), le livre de l’aumône légale, le chapitre de l’aumône de nuit]" in hn
    and "« de sorte que sa droite ne connaisse pas ce que dépense sa gauche »" in hn
    and "[Ṣaḥīḥ Ibn Ḫuzayma (l’authentique d’Ibn Ḫuzayma), le livre de la prière, le chapitre du jugement de l’attente de la prière et de la séance dans la mosquée]" in hn
    and "[Fatḥ al-Ġayṯ (la victoire de l’assistance), as-Saḫāwī, tome un, page 345]" in hn)
chk("maqlūb c. chaîne et texte ensemble : Bagdad + cent ḥadīṯ + récita + rendit chaque texte + 2/340",
    "c’est que l’on prenne la chaîne d’un texte et qu’on lui donne le texte d’un autre, et l’inverse" in hn
    and "dans le récit de l’examen de l’imām al-Buḫārī quand il vint à Bagdad" in hn
    and "les gens de Bagdad lui donnèrent cent ḥadīṯ" in hn
    and "il les récita de nouveau comme il les avait entendus, et selon l’ordre de leur audition" in hn
    and "rendit chaque texte à sa chaîne, et chaque chaîne à son texte" in hn
    and "[Taʾrīḫ Baġdād (l’histoire de Bagdad), al-Ḫaṭīb al-Baġdādī, tome deux, page 340]" in hn)

# ---- motifs + jugement + ʿAlī
chk("motifs : étrangereté, examen, erreur",
    "le renversement avec le dessein de l’étrangereté" in hn
    and "le renversement avec le dessein de l’examen" in hn
    and "le renversement par erreur" in hn)
chk("jugement : diffère selon l’intention",
    "le jugement du renversement dans le ḥadīṯ diffère selon l’intention de son auteur" in hn)
chk("jugement : à dessein → compositions ; erreur → inversé/interpolé ; examen → permis sous conditions",
    "il fait partie des compositions (mawḍūʿāt)" in hn
    and "il fait partie de l’inversé ou de l’interpolé, par le déficit de la maîtrise du narrateur" in hn
    and "il est permis, pour se reporter de la préservation du ḥadīṯ et de ses gens" in hn
    and "que la chaîne soit continue, et que le besoin s’arrête à elle" in hn
    and "manifesté avant la séparation de l’assemblée" in hn)
chk("ʿAlī : tadhākarū + Dārimī mudākara",
    "L’imām ʿAlī b. Abī Ṭālib, que Dieu soit satisfait de lui, a dit" in hn
    and "« faites circuler ce ḥadīṯ entre vous, et échangez-le, pour que, si vous ne le faites pas... [fin de la clause imprimée fragmentée, déclarée telle quelle] »" in hn
    and "[Sunan ad-Dārimī (les sunan d’ad-Dārimī), le chapitre de l’étude mutuelle de la science]" in hn)

# ---- taqwīm + istiṯmār + iʿdād
chk("taqwīm 1 : j’explique les types de l’interpolation",
    "j’explique les types de l’interpolation" in hn)
chk("taqwīm 2 : je cite les voies de connaissance",
    "je cite les voies de connaissance de l’interpolation" in hn)
chk("taqwīm 3 : causes du renversement ? et son jugement ?",
    "quelles sont les causes du renversement du ḥadīṯ ? et quel est son jugement ?" in hn)
chk("istiṯmār : versification al-ʿIrāqī — une seule considération + imām de l’art + cent + Bagdad",
    "d’une seule considération, afin qu’ils s’y rendent étrangers" in hn
    and "leur examen de l’imām de l’art" in hn
    and "en cent [ḥadīṯ], quand il vint à Bagdad" in hn
    and "« quand la prière est établie... »" in hn)
chk("istiṯmār : renvoi Tabṣira / Alfiyyat al-ʿIrāqī 1/115",
    "[at-Tabṣira wa-t-taḏkira fī ʿulūm al-ḥadīṯ (le rappel et la mise en garde dans les sciences du ḥadīṯ), connue sous le nom d’Alfiyyat al-ʿIrāqī (la versification millénaire d’al-ʿIrāqī), tome un, page 115]" in hn)
chk("consigne : synthèse de composition des types du renversement",
    "j’extrais de la versification une synthèse de composition qui contient les types du renversement dans le ḥadīṯ" in hn)
chk("iʿdād : leçon 22 addition/incohérent + deux recherches",
    "La leçon 22 est « l’addition dans les chaînes continues et l’incohérent (al-muḍṭarab) »" in hn
    and "l’élève cherchera le sens de l’addition (az-zāʾid) dans les chaînes continues avec un exemple" in hn
    and "cherchera le sens de la perturbation (al-iḍṭirāb) dans la chaîne" in hn)

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
chk("registre 272 intact (19 801 car)", len(les["pdf-mut23h2u-272"].get("htmlFr") or "") == 19801)
chk("registre 273 intact (22 645 car)", len(les["pdf-mut23h2u-273"].get("htmlFr") or "") == 22645)
chk("registre 274 intact (28 082 car)", len(les["pdf-mut23h2u-274"].get("htmlFr") or "") == 28082)
fr = les["pdf-mut23h2u-275"].get("htmlFr") or ""
if fr:
    chk("registre 275 = htmlFr posé (30 000-42 000 car)", 30_000 <= len(fr) <= 42_000)
    chk("registre 275 == fichier livré", fr.strip() == h.strip())
else:
    chk("registre 275 encore vide (avant hand-set)", True)
chk("registre 276 non touché (htmlFr vide)", (les["pdf-mut23h2u-276"].get("htmlFr") or "") == "")
chk("titleAr pré-mappé 275", les["pdf-mut23h2u-275"].get("titleAr") == "الدرس 21 : المدرج والمقلوب")
chk("titleFr pré-mappé 275 aligné au h1 (apostrophes normalisées)",
    (les["pdf-mut23h2u-275"].get("titleFr") or "").replace(chr(39), "\u2019")
    == "Leçon 21 : L’interpolé (mudraǧ) et l’inversé (maqlūb)")
chk("titleAr pré-mappé 276 intact (leçon 22, non touchée)",
    les["pdf-mut23h2u-276"].get("titleAr") == "الدرس 22 : المزيد في متصل الأسانيد والمضطرب")
chk("titleFr pré-mappé 276 intact (l’incohérent, selon le registre)",
    (les["pdf-mut23h2u-276"].get("titleFr") or "").replace(chr(39), "\u2019")
    == "Leçon 22 : L’adjonction dans les chaînes continues (mazīd) et l’incohérent (muḍṭarib)")

print(f"verify-ulumhadith2-pdf275 : {ok} PASS / {fail} ÉCHEC")
raise SystemExit(1 if fail else 0)

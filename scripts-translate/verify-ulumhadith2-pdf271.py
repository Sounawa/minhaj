#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Minhāj — Vérification de la leçon ulum-hadith-tanawi-2 / pdf-mut23h2u-271
(الدرس 17 : السقط الظاهر والخفي — as-suqūṭ aẓ-ẓāhir wa-s-suqūṭ al-ḫafī, p.88-92
du manuel ulum-hadith-2-thanawi_text.pdf) : bornes p.88-92 par sondage (p.87 =
clôture de la leçon 16, livrée R646, docId pdf-mut23h2u-270 ; p.88 = bannière
« السقط الظاهر والخفي » + 3 objectifs + tamhīd + matn Ibn Ḥaǧar
« ثم قد يكون واضحا أو خفيا؛ فالأول يدرك بعدم التلاقي ومن ثم اجتياج إلى التاريخ
والثاني المدلس ويرد بصيغة تحتمل اللقي كعن وقال وكذلك المرسل الخفي من معاصر لم يلق »
(image p88-a) + الشرح + استخلاص ; p.89 = التحليل + أولا السقط الظاهر (voies :
عدم التلاقي — ابن عيينة/علي بن خشرم + العوام بن حوشب/ابن أبي أوفى, إمام أحمد
[شرح نخبة الفكر، القاري، ص 427 image] + مولد متأخر + بلدان مختلفة + ضرورة التاريخ)
+ ثانيا السقط الخفي + لغة المدلّس [مقاييس اللغة، ابن فارس، 2/692] ; p.90 =
اصطلاح المدلّس + أنواع التدليس (الحاكم 6 أقسام → ابن الصلاح 2 : تدليس الإسناد
— شعبة «التدليس أخو الكذب» + «لأن أزني أحب إلى من أن أدلس» + عقب ابن الصلاح
[ص 75 image] + مثال الحاكم [معرفة علوم الحديث، ص 167 image, حكيم بن جبير] +
تدليس الشيوخ — أبي بكر بن مجاهد [ص 158 BRUTE]) ; p.91 = صيغ التدليس (عن/قال
vs سمعت/حدثنا/أخبرنا) + حكم الحديث المدلس («المدلس من قبيل المردود», image
p91-a) + المرسل الخفي تعريفه (3 figures + لا يشترط له موضع) + الفرق (النووي
والعراقي، ابن حجر) + مثال أبي هريرة [العلل، الدارقطني، مسند أبي هريرة] ; p.92 =
بيان الأرقام (نيفا وسبعين, وفاته 130 أو بعدها [فتح المغيث، السخاوي، 3/78],
ابن مهدي ووكيع والعدني بإثبات الواسطة) + حكم المرسل الخفي + أهتدي وأقتدي
[مقدمة ابن الصلاح، ص 248 image] + التقويم (2) + الاستثمار [الباعث الحثيث، ابن
كثير، ص 360 image] + الإعداد القبلي (2 items) ; p.93 = ouverture leçon 18
« أسباب الطعن في الراوي » (sondage couche, non touchée, registre vide) ;
extraction MULTICOUCHE (brute + fix p.88-97 = tr-tmp/uh2-l271-raw.txt) ; DIX
lectures d'images (R648 : 6 sous-passe A — p88-a-matn, p88-b-istihlas, p90-a-shuba,
p91-a-hukm, p91-b-farq-mithal, p92-a-bayan-ihtadi ; A-bis 2 zooms 600 dpi —
p90-b-isnad, p91-c-hadith ; B 2 — p89-a-ihtijaj, p92-b-istithmar) ; LOI DES
NOMBRES R648 : BRUTE isolés = imprimé (75, 427, 167, 158, 248, 360 — image),
composites à oblique renversés en bloc (296/2→2/692, 87/3→3/78), couche décodée
chiffres renversés (724/761/063/842/57) = artefacts attendus ; HADĪṮ ÉLLIPSÉ :
manuel imprime «فإذا مَرَأَته…» ambigu (image 600 dpi p91-c) — rendu FR suspendu
après «qu'il réveille son épouse», jamais deviné.
Usage: python3 scripts-translate/verify-ulumhadith2-pdf271.py
"""
import json
import re

HTML = "/home/z/my-project/tr-tmp/lesson-uh2-pdf-mut23h2u-271-fr.html"
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
chk("h1 = titleFr pré-mappé « Leçon 17 : L'omission apparente et cachette dans la chaîne (saqṭ) »",
    hn.startswith("<h1>Leçon 17 : L’omission apparente et cachette dans la chaîne (saqṭ)"))
chk("h1 mentionne deuxième année", "deuxième année" in h[:500])
chk("h1 mentionne la chute dans la chaîne (as-suqūṭ / al-isnād)",
    "la chute (as-suqūṭ) dans la chaîne (al-isnād)" in h[:1400])
chk("h1 mentionne la chute apparente et la chute cachée",
    "la chute apparente (as-suqūṭ aẓ-ẓāhir)" in h[:1600] and "la chute cachée (as-suqūṭ al-ḫafī)" in h[:2000])
chk("h1 mentionne Ibn ʿUyayna et ʿAlī b. Ḫašram",
    "Ibn ʿUyayna" in h[:2600] and "ʿAlī b. Ḫašram" in h[:2600])
chk("h1 mentionne al-ʿUwwām b. Ḫawšab et l’imām Aḥmad",
    "al-ʿUwwām b. Ḫawšab" in h[:2600] and "l’imām Aḥmad" in h[:2600])
chk("h1 mentionne Maqāyīs al-luġa et Ibn Fāris", "Maqāyīs al-luġa d’Ibn Fāris" in h[:2200] or "Maqāyīs al-luġa d’Ibn Fāris" in h)
chk("h1 mentionne Shuʿba et ses deux citations",
    "Shuʿba" in h[:3000] and "le frère du mensonge" in h[:3000])
chk("h1 mentionne le Ḥākim an-Naysābūrī et al-Aʿmaš",
    "Ḥākim an-Naysābūrī" in h[:3200] and "al-Aʿmaš" in h[:3200])
chk("h1 mentionne Abū Bakr b. Muǧāhid et le tadlīs des maîtres",
    "Abū Bakr b. Muǧāhid" in h[:6000] and "le tadlīs des maîtres" in h[:6000])
chk("h1 mentionne an-Nawawī et al-ʿIrāqī",
    "an-Nawawī" in h[:6200] and "al-ʿIrāqī" in h[:6200])
chk("h1 mentionne Abū Hurayra et Ibn al-Minkadīr",
    "Abū Hurayra" in h[:6400] and "Ibn al-Minkadīr" in h[:6400])
chk("h1 mentionne les formules (samiʿtu / ḥaddaṯanā / aḫbaranā)",
    "j’ai entendu" in h[:6400] and "il nous a narrés" in h[:6400])
chk("dl.lesson-meta présent", '<dl class="lesson-meta">' in h and "<dt>Source du cours</dt>" in h)
chk("item archive.org cité", "1_20220304_20220304_2251" in h)
chk("source locale citée", "ulum-hadith-2-thanawi_text.pdf" in h)
chk("bornes p.88-92 documentées", "pages 88 à 92" in h)
chk("p.87 clôture leçon 16 (R646, 270)", "R646" in h and "pdf-mut23h2u-270" in h)
chk("p.93 leçon 18 sondée, non touchée, registre vide",
    "la leçon 18" in h and "non touchée" in h and "registre vide" in h)
chk("sondage « jamais devinées »", "jamais devinées" in h)
chk("couches brute + fix p.88-97 citées (uh2-l271-raw.txt)",
    "uh2-l271-raw.txt" in h and "mots réinversés" in h)
chk("DIX lectures d’images consignées (6 A + 2 A-bis + 2 B)",
    "p88-a-matn.png" in h and "p90-b-isnad.png" in h and "p89-a-ihtijaj.png" in h
    and "p92-b-istithmar.png" in h and "DIX lectures d’images" in h)
chk("LOI DES NOMBRES définie et appliquée (R648)",
    "LOI DES NOMBRES" in h and "296/2" in h and "87/3" in h and "724" in h)
chk("HADĪṮ ÉLLIPSÉ documenté (clause ambiguë, suspension FR)",
    "HADĪṮ ÉLLIPSÉ" in h and "jamais deviné" in h)
chk("zéro āya (cache coranique non sollicité)",
    "ZÉRO ĀYA" in h and "cache coranique non sollicité" in h)

# ---- nombres tranchés
chk("Maqāyīs 2/692 (لغة المدلّس)", "tome 2, page 692" in hn)
chk("Sharḥ an-Nuḫba (al-Qārī) p.427", "ʿAlī al-Qārī, page 427" in hn)
chk("Muqaddimat Ibn aṣ-Ṣalāḥ p.75 (Shuʿba)", "page 75" in hn)
chk("Maʿrifat ʿulūm al-ḥadīṯ p.167 (exemple du Ḥākim)",
    "le Ḥākim an-Naysābūrī, page 167" in hn)
chk("Muqaddimat Ibn aṣ-Ṣalāḥ p.158 (tadlīs des maîtres)", "page 158" in hn)
chk("Fatḥ al-Maġīṯ 3/78 (Ibn al-Minkadīr)", "tome 3, page 78" in hn)
chk("Muqaddimat Ibn aṣ-Ṣalāḥ p.248 (ahtadī — Mālik)", "page 248" in hn)
chk("al-Bāʿiṯ al-ḥaṯīṯ p.360 (Ibn Kathīr)", "page 360" in hn)
chk("Dāraquṭnī musnad Abī Hurayra cité", "ad-Dāraquṭnī" in hn and "musnad d’Abū Hurayra" in hn)

# ---- objectifs (3)
chk("objectif 1 : concept chute apparente/cachée",
    "le concept de la chute apparente et de la chute cachée" in hn)
chk("objectif 2 : distinguer tadlīs / mursal khafī",
    "le tadlīs (la dissimulation) du mursal khafī" in hn)
chk("objectif 3 : s’écarter du tadlīs dans la transmission",
    "je m’écarte du tadlīs dans la transmission des récits" in hn)

# ---- tamhīd + matn
chk("tamhīd : chute cause du rejet + apparente/cachée",
    "parmi les causes du rejet du ḥadīṯ" in hn and "peut être apparente, et elle peut être cachée" in hn)
chk("tamhīd : double question (différence + types)",
    "la différence entre elles deux" in hn and "les types inscrits sous la chute apparente" in hn)
chk("matn : limpide ou caché",
    "il peut être limpide (wāḍiḥan) ou caché (ḫafiyyan)" in hn)
chk("matn : perçu par le non-établissement de la rencontre + datation",
    "perçu par le non-établissement de la rencontre (ʿadam at-tilāq)" in hn
    and "la nécessité d’aller à la datation (at-taʾrīḫ)" in hn)
chk("matn : mudallis + formule qui tolère la rencontre (ʿan/qāla)",
    "le mudallis, et il se présente par une formule qui tolère la rencontre" in hn
    and "comme « d’après » et « il a dit »" in hn)
chk("matn : mursal khafī d’un contemporain non rencontré",
    "le mursal khafī, celui d’un contemporain qu’il n’a pas rencontré" in hn)

# ---- gloses + istiḫlāṣ
chk("glose : chute limpide", "la chute de la chaîne peut être limpide" in hn)
chk("glose : non-établissement de la rencontre (3 cas : époque / rencontre / iǧāza-wiǧāda)",
    "il n’a pas perçu son époque, ou il l’a perçue mais ils ne se sont pas rencontrés" in hn
    and "d’autorisation ni d’obtention (wiǧāda)" in hn)
chk("glose : mudallis = katm al-ʿayb", "la dissimulation du défaut (katm al-ʿayb)" in hn)
chk("istiḫlāṣ 1 : bénéfices de la datation",
    "les bénéfices de la connaissance des dates de naissance des rapporteurs" in hn)
chk("istiḫlāṣ 2 : formules qui portent l’audition",
    "quelques formules qui portent l’audition (as-samāʿ)" in hn)

# ---- taḥlīl 1 : saqṭ apparent
chk("remarque : le Ḥaǧar n’a pas énuméré les types de la chute apparente",
    "n’a pas énuméré ce qui s’inscrit sous la chute apparente" in hn
    and "(le muʿallaq, le manqaṭiʿ, le mursal)" in hn
    and "son nom selon la place de la chute" in hn)
chk("définition : apparent sans long examen", "apparent, et qui ne requiert pas un long examen" in hn)
chk("voie 1 : non-établissement de la rencontre (3 cas)",
    "il n’a pas perçu son époque, ou il l’a perçue mais ils ne se sont pas rencontrés" in hn)
chk("voie 1 : Ibn ʿUyayna / ʿAlī b. Ḫašram + verdict d’un imām",
    "comme a informé Ibn ʿUyayna au sujet de ce qu’il rapporte de ʿAlī b. Ḫašram" in hn
    and "le verdict ferme d’un imām informé" in hn)
chk("voie 1 : al-ʿUwwām b. Ḫawšab + imām Aḥmad nom à nom",
    "al-ʿUwwām b. Ḫawšab d’après Ibn Abī Awfā" in hn
    and "al-ʿUwwām n’a pas atteint Ibn Abī Awfā" in hn)
chk("voie 2 : naissance postérieure à la mort",
    "postérieure à la mort de celui dont il rapporte" in hn)
chk("voie 3 : pays différents sans migration", "leurs deux pays soient différents" in hn
    and "a voyagé de son pays vers le pays de l’autre" in hn)
chk("conclusion : nécessité de la datation (naissances, décès, recherche, déplacements)",
    "des époques de leur recherche et de leurs déplacements" in hn
    and "c’est par là que ces choses se connaissent" in hn)

# ---- taḥlīl 2 : saqṭ caché
chk("intro : al-ḥuḏāq seulement", "ne la perçoivent que les fins connaisseurs (al-ḥuḏāq)" in hn
    and "embrasse le mudallis et le mursal khafī" in hn)
chk("luġa : racine d-l-s + dissimulation et l’obscurité [Maqāyīs]",
    "« dals »" in hn and "désigne la dissimulation et l’obscurité" in hn)
chk("luġa : ténèbre couvre / mudallis couvre celui dont il a omis le récit",
    "le mudallis couvre celui dont il a omis le récit" in hn)
chk("iṣṭilāḥ : n’a pas entendu + fait croire l’audition",
    "n’a pas entendu de celui qu’il narre, et qu’il a fait croire l’audition" in hn)
chk("iṣṭilāḥ : expression qui fait illusion + couvre l’attribut du maître",
    "une expression qui fait illusion (ʿibāra muwahhima)" in hn
    and "couvre l’attribut par lequel le maître est connu" in hn)
chk("types : Ḥākim six sections + Abū Nuʿaym + remonte aux deux d’Ibn aṣ-Ṣalāḥ",
    "a divisé le tadlīs en six sections, et Abū Nuʿaym l’a suivi" in hn
    and "remonte aux deux sections que mentionne Ibn aṣ-Ṣalāḥ" in hn)
chk("type 1 : tadlīs de la chaîne / de l’omission + ne dit pas « il nous a informés »",
    "tadlīs de l’omission (tadlīs al-isqāṭ)" in hn
    and "il ne dit pas « il nous a informés »" in hn)
chk("type 1 : Shuʿba deux citations + apposition d’Ibn aṣ-Ṣalāḥ (surenchère)",
    "« le tadlīs est le frère du mensonge »" in hn
    and "que je commette l’adultère me serait plus aimable que de pratiquer le tadlīs" in hn
    and "est un excès porté à la surenchère" in hn)
chk("exemple Ḥākim : chaîne nom à nom (Ismāʿīl b. Muḥammad b. al-Faḍl aš-Šaʿrānī…)",
    "Ismāʿīl b. Muḥammad b. al-Faḍl aš-Šaʿrānī" in hn and "Kaṯīr b. Yaḥyā" in hn
    and "Abū ʿAwāna" in hn and "Ibrāhīm at-Taymī, d’après son père, d’après Abū Ḏarr" in hn)
chk("matn Ḥākim : ô Ḥannān, ô Mannān + Ḥakīm b. Ǧubayr établi à l’interrogation",
    "ô Ḥannān, ô Mannān" in hn and "Ḥakīm b. Ǧubayr me l’a narré d’après lui" in hn)
chk("commentaire : al-Aʿmaš dle + intermédiaire établi",
    "Al-Aʿmaš a donc pratiqué le tadlīs du ḥadīṯ d’après Ibrāhīm" in hn
    and "il établit l’intermédiaire entre lui et Ibrāhīm" in hn)
chk("type 2 : tadlīs des maîtres, plus caché que le premier",
    "Le tadlīs des maîtres (tadlīs aš-šuyūḫ)" in hn and "plus caché (aḫfā) que le premier" in hn)
chk("exemple Ibn Muǧāhid : ʿAbd Allāh b. Abī ʿAbd Allāh + an-Naqqāš + Muḥammad b. Sunad + aïeul",
    "Abū Bakr b. Muǧāhid, l’imām des récitants (al-qurrāʾ)" in hn
    and "ʿAbd Allāh b. Abī ʿAbd Allāh" in hn
    and "Muḥammad b. al-Ḥasan an-Naqqāš" in hn
    and "Muḥammad b. Sunad" in hn and "il l’a rattaché à son aïeul" in hn)
chk("divisions autres : remontent à l’une des deux ou communes",
    "remontent à l’une des deux, ou sont communes aux deux" in hn
    and "en addition aux deux sections précédentes" in hn)
chk("formules : ʿan/qāla vs samiʿtu/ḥaddaṯanā/aḫbaranā + menteur",
    "telles « d’après » (ʿan) et « il a dit » (qāla)" in hn
    and "alors il est menteur" in hn
    and "« j’ai entendu » (samiʿtu), « il nous a narrés » (ḥaddaṯanā), « il nous a informés » (aḫbaranā)" in hn)
chk("statut mudallis : mardūd + fiable + seulement l’explicité (sur le plus correct)",
    "relève du rejeté (al-mardūd)" in hn and "s’il est fiable (ʿadl)" in hn
    and "sur le plus correct" in hn and "explicité la narration (maṣraḥ fīhi bi-t-taḥdīṯ)" in hn)
chk("mursal khafī : 3 figures (entendu-mais-pas-ceci / rencontré-sans-entendre / contemporain-sans-rencontre)",
    "ce qu’il n’a pas entendu de lui, ou d’après un homme qu’il a rencontré et dont il n’a pas entendu" in hn
    and "contemporain et qu’il n’a pas rencontré" in hn)
chk("mursal khafī : pas de place exigée dans la chaîne vs mursal apparent (dire du Successeur)",
    "ne lui est pas exigée une place dans la chaîne" in hn
    and "le dire du Successeur" in hn and "car cela est sa place" in hn)
chk("différence : exclusivité (rencontre connue vs contemporain sans rencontre connue)",
    "l’exclusivité de celui qui narre d’après un homme dont la rencontre de lui est connue" in hn
    and "sans qu’il soit connu qu’il l’a rencontré" in hn)
chk("différence : Nawawī/ʿIrāqī + correct = distinction (Ibn Ḥaǧar)",
    "comme an-Nawawī et al-ʿIrāqī" in hn
    and "le correct est la distinction entre les deux" in hn)
chk("exemple Abū Hurayra : matn ellipsé « qu’il réveille son épouse »",
    "« Quand l’un de vous se réveille au cours de la nuit, qu’il réveille son épouse… »" in hn)
chk("exemple : manuel suspend la suite (points de suspension)",
    "le manuel suspend ici la suite du ḥadīṯ par des points de suspension" in hn)
chk("exemple : isnad Abū ʿĀmir al-ʿAqdī / aṯ-Ṯawrī / Ibn al-Minkadīr",
    "Abū ʿĀmir al-ʿAqdī, d’après aṯ-Ṯawrī, d’après Ibn al-Minkadīr, d’après Abū Hurayra" in hn)
chk("exemple : Ibn Maʿīn et al-Bazzār + Abū Zurʿa",
    "le dire d’Ibn Maʿīn et d’al-Bazzār" in hn
    and "Abū Zurʿa a dit : il ne l’a pas rencontré" in hn)
chk("démonstration : dépassé les soixante-dix ans (Ibn al-Madīnī d’après Ibn ʿUyayna)",
    "avait dépassé les soixante-dix ans d’âge" in hn
    and "Ibn al-Madīnī d’après Ibn ʿUyayna" in hn)
chk("démonstration : mort en l’an cent trente ou après + naissance peu avant les soixante",
    "sa mort fut en l’an cent trente ou en celle qui la suit" in hn
    and "peu avant les soixante" in hn)
chk("démonstration : Ibn Mahdī, Wakīʿ, al-ʿAdanī + intermédiaire établi",
    "Ibn Mahdī, Wakīʿ, al-ʿAdanī et d’autres" in hn
    and "l’intermédiaire qui n’a pas été entendu chez aucun d’eux" in hn)
chk("conclusion : sa narration relève du mursal khafī",
    "sa narration relève du mursal khafī" in hn)
chk("statut mursal khafī : inqiṭāʿ + mardūd + état de l’omis",
    "comporte une rupture (inqiṭāʿ)" in hn and "relève du rejeté (al-mardūd)" in hn
    and "la non-connaissance de l’état de l’omis de la chaîne" in hn)

# ---- ahtadī + taqwīm + istiṯmār + iʿdād
chk("ahtadī : Ibn aṣ-Ṣalāḥ + Mālik + utilité mutuelle + bénédiction",
    "Ibn aṣ-Ṣalāḥ, que Dieu lui fasse miséricorde, a dit" in hn
    and "Mālik — que Dieu soit satisfait de lui" in hn
    and "l’utilité mutuelle (al-ifāda)" in hn
    and "l’utilité mutuelle des uns envers les autres" in hn)
chk("taqwīm 1 : types du tadlīs", "je mentionne les types du tadlīs" in hn)
chk("taqwīm 2 : différence mudallis/mursal khafī",
    "je décris la différence entre le mudallis et le mursal khafī" in hn)
chk("istiṯmār : Ibn Kathīr + géants anciens et modernes",
    "Ibn Kathīr, que Dieu lui fasse miséricorde" in hn
    and "les examinateurs du ḥadīṯ et ses géants, anciens et modernes" in hn)
chk("istiṯmār : consigne géants (al-ǧahābaḏa)",
    "que par les géants (al-ǧahābaḏa)" in hn)
chk("iʿdād : leçon 18 motifs de l’atteinte + 2 items",
    "leçon 18 est" in hn and "les motifs de l’atteinte portée au rapporteur" in hn
    and "asbāb aṭ-ṭaʿn fī ar-rāwī" in hn and "deux items" in hn)
chk("iʿdād : causes du rejet + précaution des savants",
    "je recherche les causes du rejet du ḥadīṯ" in hn
    and "les efforts des savants dans la précaution pour la Sunna prophétique" in hn)
chk("iʿdād : négligence et grave erreur",
    "la négligence (al-ġafla) et la grave erreur (faḥš al-ġalaṭ)" in hn)

# ---- hygiène FR
chk("zéro caractère arabe", not re.search(r"[\u0600-\u06FF\u0750-\u077F\u08A0-\u08FF\uFB50-\uFDFF\uFE70-\uFEFF]", h))
chk("zéro apostrophe droite", "'" not in h)
chk("guillemets appariés", h.count("«") == h.count("»"))
chk("zéro double espace", "  " not in re.sub(r"&nbsp;|\n", "", h))
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
chk("registre 267 intact (25 238 car)", len(les["pdf-mut23h2u-267"].get("htmlFr") or "") == 25238)
chk("registre 268 intact (20 715 car)", len(les["pdf-mut23h2u-268"].get("htmlFr") or "") == 20715)
chk("registre 269 intact (~23 000+ car)", len(les["pdf-mut23h2u-269"].get("htmlFr") or "") >= 23_000)
chk("registre 270 intact (20 432 car)", len(les["pdf-mut23h2u-270"].get("htmlFr") or "") == 20432)
chk("registre 272 non touché (htmlFr vide)", (les["pdf-mut23h2u-272"].get("htmlFr") or "") == "")
fr = les["pdf-mut23h2u-271"].get("htmlFr") or ""
if fr:
    chk("registre 271 = htmlFr posé (~21 000-25 000 car)", 20_000 <= len(fr) <= 26_000)
    chk("registre 271 == fichier livré", fr.strip() == h.strip())
else:
    chk("registre 271 encore vide (avant hand-set)", True)
chk("titleAr pré-mappé 271", les["pdf-mut23h2u-271"].get("titleAr") == "الدرس 17 : السقط الظاهر والخفي")
chk("titleFr pré-mappé 271 aligné au h1 (apostrophes normalisées)",
    (les["pdf-mut23h2u-271"].get("titleFr") or "").replace("'", "’")
    == "Leçon 17 : L’omission apparente et cachette dans la chaîne (saqṭ)")
chk("titleAr pré-mappé 272 intact (leçon 18, non touchée)",
    les["pdf-mut23h2u-272"].get("titleAr") == "الدرس 18 : أسباب الطعن في الراوي")

print(f"verify-ulumhadith2-pdf271 : {ok} PASS / {fail} ÉCHEC")
raise SystemExit(1 if fail else 0)

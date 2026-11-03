#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""R553 — Passe 3 : zones sensibles — transcriptions token par token."""
import json
import os
import subprocess

HOME = "/home/z/my-project"
CROPS = f"{HOME}/tr-tmp/qa-crops-r553"
OUT = f"{HOME}/tr-tmp/vlm-r553"
os.makedirs(OUT, exist_ok=True)

BASE = ("Tu lis une image d'un manuel scolaire marocain de hadith (Muwaṭṭaʾ Mālik / "
        "Šarḥ az-Zarqānī, 2e année collégiale). Réponds UNIQUEMENT à la question posée, "
        "par transcription EXACTE du texte imprimé visible, token par token. Si tu n'es "
        "pas sûr d'un mot ou d'un chiffre, écris [illisible]. N'invente AUCUN texte, ne "
        "complète JAMAIS de mémoire (n'utilise PAS de version canonique du hadith que tu "
        "connaîtrais), ne corrige pas l'imprimé même s'il te paraît fautif.")

ASKS = [
    # --- conflits à trancher ---
    ("n110-bracket-hi", "n-p110-666a-hi.png",
     "(1) Le renvoi rouge entre crochets [الموطأ رقم : N] : les chiffres imprimés "
     "sont-ils arabes-indiques (٠١٢٣٤٥٦٧٨٩) ou occidentaux (0123456789) ? Transcris N "
     "CHIFFRE PAR CHIFFRE de droite à gauche : est-ce (a) ٦٦٦ (=666) (b) ٩٩٩ (=999) "
     "(c) autre ? (2) Il y a un autre groupe de chiffres imprimé plus à gauche/dans la "
     "ligne : transcris-le chiffre par chiffre tel qu'imprimé et les deux mots autour."),
    ("n108-nur-hi", "n-p108-nur-hi.png",
     "(1) Transcris la fin de la citation coranique imprimée entre guillemets/chevrons "
     "(les 3-5 derniers mots avant le crochet du renvoi). (2) Transcris le renvoi en "
     "rouge TEL QU'IMPRIMÉ : nom de sourate + mot (الآية/آية) + numéro. (3) Le numéro "
     "d'āya : lis-le CHIFFRE PAR CHIFFRE de droite à gauche tel qu'imprimé — est-ce "
     "(a) 54 (b) 45 (c) 56 (d) autre ?"),
    ("n107-arafa-hi", "n-p107-arafa-hi.png",
     "Transcris TEL QU'IMPRIMÉ le renvoi entre crochets de la définition légale "
     "(nom du livre + tome/page) : chaque mot et les deux nombres CHIFFRE PAR CHIFFRE "
     "(le premier nombre est-il 1 ? le second est-il 71 ou 17 ?)."),
    ("p110-istifta", "p110-istifta.png",
     "Transcris TOUT ce passage TOKEN PAR TOKEN : (1) l'en-tête ب- حول الربح (et la "
     "phrase introductive s'il y en a une) ; (2) le récit d'istiftā' (l'ouverture "
     "استفتى… : qui interroge qui, avec les noms LETTRE PAR LETTRE) ; (3) la parole "
     "rapportée de أبو بكر mot à mot jusqu'à la fin ; (4) le renvoi [الموطأ رقم : N] "
     "avec N CHIFFRE PAR CHIFFRE ; (5) le début de la parole de مالك sur l'homme qui "
     "avait dix dinars (فتجر فيها…) mot à mot jusqu'en bas de l'image, avec son renvoi "
     "[الموطأ رقم : N] CHIFFRE PAR CHIFFRE. Signale tout petit chiffre exposant (note "
     "de bas de page) et sa position."),
    # --- hadith 1 + objectifs + tamhid ---
    ("p105-h1-zone", "p105-h1-zone.png",
     "Le premier hadith de la leçon. Transcris TOKEN PAR TOKEN : (1) le PREMIER MOT du "
     "bloc (à droite), LETTRE PAR LETTRE — est-il (a) الْخُدْرِيُّ (b) أَبُو سَعِيدٍ "
     "الْخُدْرِيُّ (c) خُذَيْر (d) autre ? (2) tout le matn entre guillemets mot à mot "
     "(l'ordre exact des trois membres : خمسة أوسق / خمس ذود / خمس أواق) ; (3) "
     "l'isnād complet après le matn (مالك بن أنس… jusqu'à سمعت أبا سعيد) mot à mot ; "
     "(4) le renvoi [الموطأ رقم : N] CHIFFRE PAR CHIFFRE."),
    ("p105-objectifs", "p105-objectifs.png",
     "Transcris TOKEN PAR TOKEN : (1) l'en-tête أهداف الدرس et les TROIS objectifs "
     "exactement (le verbe du 3ᵉ objectif : أُمَثِّلُ ? أستشهد ? autre — transcris-le) ; "
     "(2) le paragraphe de présentation (tamhīd) entier mot à mot, y compris la "
     "structure finale des trois questions."),
    # --- hadith 2 + tarjama + sharh ---
    ("p106-h2a", "p106-h2a.png",
     "La première moitié du deuxième hadith (parole de Mālik sur l'or et l'argent "
     "détenus en copropriété). Transcris TOKEN PAR TOKEN depuis قَالَ مَالِكٌ فِي "
     "الذَّهَبِ وَالوَرِقِ… jusqu'au bas de l'image, y compris les passages très "
     "vocalisés (عِشْرِينَ دِينَارًا عَيْنًا…). Ne saute aucun mot."),
    ("p106-h2b", "p106-h2b.png",
     "La fin du deuxième hadith. Transcris TOKEN PAR TOKEN : la suite de la parole de "
     "Mālik (…وَذَلِكَ أَنَّ رَسُولَ اللهِ…), la citation « لَيْسَ فِيمَا دُونَ خَمْسِ "
     "أَوَاقٍ… », la clôture de Mālik (وَهَذَا أَحَبُّ مَا سَمِعْتُ…), et le renvoi "
     "[الموطأ رقم : N] CHIFFRE PAR CHIFFRE."),
    ("p106-tarjama", "p106-tarjama.png",
     "La biographie du transmetteur. Transcris TOKEN PAR TOKEN : (1) l'en-tête (ترجمة "
     "الراوي) ; (2) le nom complet : le premier nom est-il سعيد ou سعد (Lettre PAR "
     "LETTRE : y a-t-il un yāʾ entre le ʿayn et le dāl ?) ; (3) le mot sur sa "
     "participation à Uhud : استُصغِرَ أو استُشْهِدَ ou autre — LETTRE PAR LETTRE ; (4) "
     "toute la fin (روى عن النبي… مات سنة… هـ) mot à mot avec les nombres CHIFFRE PAR "
     "CHIFFRE ; (5) les deux ou trois mots qui ferment la biographie."),
    ("p106-sharh", "p106-sharh.png",
     "Le glosaire (الشرح) du haut de page. Transcris TOKEN PAR TOKEN les deux ou trois "
     "premières entrées : (1) l'entrée sur خمس ذود (ou الأذوذ ?) : le mot d'entrée "
     "Lettre PAR Lettre (ذُؤْد ? ذَوْد ? أذوذ ?) et sa définition entière ; (2) "
     "l'entrée أواق : définition entière avec les nombres CHIFFRE PAR CHIFFRE (combien "
     "de dirhams, combien de grammes) ; (3) l'entrée suivante si visible."),
    # --- p107 ---
    ("p107-aouaq", "p107-aouaq.png",
     "L'entrée de glosaire sur الأوسق (الوسق). Transcris TOKEN PAR TOKEN toute "
     "l'entrée : le mot d'entrée, la définition (soixante ṣāʿ, le ṣāʿ quatre mudd, le "
     "mudd…) et le poids en kilogrammes CHIFFRE PAR CHIFFRE."),
    ("p107-istikhlac", "p107-istikhlac.png",
     "Transcris TOKEN PAR TOKEN l'en-tête استخلاص المضامين et ses TROIS items "
     "exactement (le verbe du 3ᵉ : يُزَكِّي ? يُذَكِّي ? autre)."),
    ("p107-tahlil", "p107-tahlil.png",
     "Transcris TOKEN PAR TOKEN : (1) l'en-tête de la grande section (المبحث… / أولا …) "
     "exactement ; (2) 1- مفهومها : la définition lexicale (الزكاة لغة) avec la "
     "citation d'Ibn Fāris MOT À MOT et son renvoi entre crochets ; (3) la définition "
     "légale (ب- الزكاة شرعا) MOT À MOT avec son renvoi entre crochets (chiffres "
     "CHIFFRE PAR CHIFFRE) ; (4) le paragraphe explicatif final (وتستعمل شرعا…) MOT À "
     "MOT."),
    # --- p108 ---
    ("p108-hukm", "p108-hukm.png",
     "Transcris TOKEN PAR TOKEN : (1) l'en-tête 2- حكمها et les deux premières phrases "
     "(الركن الثالث… أمر مقطوع به) ; (2) le verset coranique MOT À MOT tel "
     "qu'imprimé (chaque mot, y compris la fin exacte : s'arrête-t-il à الزكاة ou "
     "continue-t-il ?) et son renvoi rouge [سورة… الآية N] avec N CHIFFRE PAR "
     "CHIFFRE ; (3) le hadith de l'islam bâti sur cinq MOT À MOT (commence-t-il par "
     "بُنِيَ الإسلامُ ?) et son renvoi [صحيح البخاري] ; (4) l'en-tête 3- حكمتها."),
    ("p108-hikma", "p108-hikma.png",
     "Transcris TOKEN PAR TOKEN les quatre items a- ب- ج- د- de la section حكمتها "
     "(les mots exacts de chacun), ainsi que la phrase de transition avant le verset "
     "final (وإلى هذه المعاني…) et le début du verset si visible."),
    ("p108-verse2-shurut", "p108-verse2-shurut.png",
     "En haut de l'image : la fin de la section 3- حكمتها avec un verset coranique et "
     "son renvoi rouge. Transcris TOKEN PAR TOKEN : (1) le verset entier MOT À MOT tel "
     "qu'imprimé ; (2) le renvoi [سورة …، الآية N] TEL QU'IMPRIMÉ (nom de sourate "
     "exact + numéro CHIFFRE PAR CHIFFRE) ; (3) la phrase après le verset (وهي تجب في "
     "العين والأنعام…) ; (4) l'en-tête القسم الثاني : شروط وجوب الزكاة et le début "
     "de 1- ملك النصاب MOT À MOT (jusqu'à la mention de خمس أواق / عشرين دينارا et "
     "leurs parenthèses avec tous les nombres CHIFFRE PAR CHIFFRE)."),
    # --- p109 ---
    ("p109-nisab", "p109-nisab.png",
     "Transcris TOKEN PAR TOKEN : (1) la phrase sur أدنى حد / النصاب et son "
     "développement (وهو في العين… خمس أواق / عشرين دينارا من الذهب…) avec TOUTES "
     "les parenthèses et nombres CHIFFRE PAR CHIFFRE ; (2) la citation de مالك "
     "MOT À MOT (commence-t-elle par الأمر الذي لا اختلاف فيه عندنا ou autre "
     "chose ?) et le renvoi [الموطأ رقم : N] CHIFFRE PAR CHIFFRE ; (3) la phrase "
     "وإليه ذهب الأئمة… et ce qui suit (لأن وزن الدينار…) avec le nombre CHIFFRE PAR "
     "CHIFFRE ; (4) tout petit chiffre exposant (note) visible."),
    ("p109-abd", "p109-abd.png",
     "Transcris TOKEN PAR TOKEN : (1) la phrase ولا يعتبر المال بنصاب غيره ; (2) le "
     "cas de l'homme aux cent soixante dirhams : le nombre exact de dirhams CHIFFRE "
     "PAR CHIFFRE (ستون ومائة ? غيره ?) et le taux de change (ببيضة ثمانية دراهم "
     "بدينار ?) ; (3) la réponse de مالك MOT À MOT et le renvoi [الموطأ رقم : N] "
     "CHIFFRE PAR CHIFFRE ; (4) l'explication لأن المال إنما يعتبر بنصاب نفسه… "
     "jusqu'à ولا العكس."),
    ("p109-khalata", "p109-khalata.png",
     "Transcris TOKEN PAR TOKEN : (1) ولا فرق عند مالك في زكاة العين بين الشركاء "
     "وغيرهم… et tout le passage (le cas de l'homme aux vingt dinars, كانت منفردة أو "
     "مختلطة…) ; (2) la citation « لَيْسَ… / وَلَا… فِيمَا دُونَ خَمْسِ أَوَاقٍ… » "
     "MOT À MOT telle qu'imprimée (premier mot exact : ليس ? ولا ? et y a-t-il "
     "يُؤْخَذُ ?) ; (3) la clôture فاقتضى أنه إنما يعتبر ملك كل واحد على حدة ; (4) "
     "le mot 2- مرور الحول s'il est visible."),
    ("p109-hawl", "p109-hawl.png",
     "Transcris TOKEN PAR TOKEN : (1) l'en-tête 2- مرور الحول ; (2) أ- شرط مرور "
     "الحول… et la phrase sur ابن عمر MOT À MOT ; (3) sa citation MOT À MOT et le "
     "renvoi [الموطأ رقم : N] CHIFFRE PAR CHIFFRE ; (4) tout AUTRE nombre imprimé sur "
     "la bande (note de bas de page ?) : transcris-le CHIFFRE PAR CHIFFRE et dis où "
     "il se trouve ; (5) le début de ب- حول الربا وفائدته et la définition de la "
     "فائدة (فائدة من فائدة أو…) MOT À MOT si visible."),
    # --- p110 ---
    ("p110-taqwim", "p110-taqwim.png",
     "Transcris TOKEN PAR TOKEN l'en-tête التقويم et ses TROIS questions exactement "
     "(le mot de la 2ᵉ question : الوقص ? الوقع ? العرض ? autre — LETTRE PAR "
     "LETTRE)."),
    ("p110-istithmar", "p110-istithmar.png",
     "Transcris TOKEN PAR TOKEN : (1) l'en-tête الاستثمار ; (2) la parole de مالك sur "
     "l'homme aux cinq dinars MOT À MOT (خمسة دنانير، من فائضة أو غيرها، فتجر "
     "فيها…) avec le renvoi [الموطأ رقم : N] CHIFFRE PAR CHIFFRE ; (3) les DEUX "
     "questions finales (1- ما نوع المال… / 2- هل وافق الجمهور…) MOT À MOT ; (4) "
     "tout petit chiffre exposant (note) visible."),
    ("p111-iedad", "p111-iedad.png",
     "Transcris TOKEN PAR TOKEN l'en-tête الإعداد القبلي, la phrase d'ouverture "
     "(أحفظ أحاديث الدرس المقبل…) et les TROIS items exactement."),
]

for key, img, q in ASKS:
    out = f"{OUT}/p3-{key}.json"
    if os.path.exists(out):
        print("•", key, "déjà lu")
        continue
    cmd = ["z-ai", "vision", "-p", f"{BASE}\nQUESTION : {q}", "-i", f"{CROPS}/{img}", "-o", out]
    r = subprocess.run(cmd, capture_output=True, text=True, timeout=300)
    print(("✓" if r.returncode == 0 else "✗"), key, (r.stderr or "").strip()[:150])

print("\n===== RÉSULTATS (extraits) =====")
for key, img, q in ASKS:
    try:
        d = json.load(open(f"{OUT}/p3-{key}.json", encoding="utf-8"))
        c = d["choices"][0]["message"]["content"]
        print(f"\n----- {key} ----- ({len(c)} car)")
        print(c[:1900])
    except Exception as e:
        print(f"\n----- {key} ----- ERREUR {e}")

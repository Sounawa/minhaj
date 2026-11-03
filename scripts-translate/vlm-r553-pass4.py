#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""R553 — Passe 4 : questions FERMÉES sur les derniers points litigieux
(nombres, lettres isolées, fragments) — chaque ambiguïté est tranchée par
preuve image, jamais devinée."""
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
    # --- hadith 1 : les trois membres du matn ---
    ("n4-p105-h1-members", "p105-h1-zone.png",
     "Le matn du hadith compte TROIS membres « ليس فيما دون … صدقة ». Pour CHAQUE "
     "membre, transcris le groupe nominal MOT À MOT : (1) premier membre : quel mot "
     "après « خمس » — ذود ? أوسق ? autre ? ; (2) deuxième membre : quel mot après "
     "« خمس » — أواق ? أوسق ? ; contient-il « من الورق » ? ; (3) troisième membre : "
     "quel mot après « خمسة/خمس » — أوسق ? أواق ? ذود ? Transcris les trois membres "
     "dans l'ordre EXACT de l'imprimé. Réponds en fin : « membre1=…, membre2=…, "
     "membre3=… »."),
    ("n4-p105-h1-renvoi", "p105-h1-zone.png",
     "Le renvoi rouge [الموطأ رقم : N] à la fin du hadith. Les chiffres sont-ils "
     "arabes-indiques ou occidentaux ? Lis N chiffre par chiffre DANS L'ORDRE "
     "D'ÉCRITURE (de gauche à droite comme imprimé) : est-ce ٦٥٥ (655), ٥٦٥ (565), "
     "٥٥٦ (556) ou autre ? Réponds : « type=…, chiffres_gauche_a_droite=…, "
     "numéro=… »."),
    # --- p.109 bas : définition de la fāʾida (jamais lue) ---
    ("n4-p109-faida", "p109-faida.png",
     "Transcris TOKEN PAR TOKEN toute la sous-section visible : (1) l'en-tête « ب- "
     "حول الفائدة والربح » exactement tel qu'imprimé (l'ordre des deux mots) ; (2) "
     "la définition de la fāʾida (« حول الفائدة : من فائدة… ») : la liste COMPLÈTE "
     "des sources de fāʾida (héritage, don, …) dans l'ordre exact, chaque mot ; (3) "
     "la règle qui suit (« فتجب فيها الزكاة… ») MOT À MOT jusqu'en bas de page, "
     "y compris toute lettre suspensive finale."),
    # --- p.110 haut : ligne d'ouverture + note 46 ---
    ("n4-p110-top", "p110-top.png",
     "Transcris TOKEN PAR TOKEN la/les première(s) ligne(s) : (1) le premier mot "
     "imprimé en haut (استفتى ? autre ?) LETTRE PAR LETTRE et ce qui le précède "
     "s'il y a quelque chose ; (2) tout petit chiffre exposant (note de bas de "
     "page) sur ces lignes : transcris-le CHIFFRE PAR CHIFFRE et dis après quel mot "
     "il se trouve ; (3) la chaîne des rapporteurs (« فقال القاسم بن محمد… ») "
     "MOT À MOT ; (4) l'ouverture du récit d'Abū Bakr jusqu'à « سأل الرجل »."),
    # --- p.110 : les nombres de dinars du passage حول الربح ---
    ("n4-p110-ribs-numbers", "p110-ribs.png",
     "Le passage « لقول مالك في رجل كانت له … دينارا فتجر فيها فحال عليها الحول وقد "
     "بلغت … دينارا ». Deux nombres de dinars sont imprimés. Lis CHACUN chiffre par "
     "chiffre : le PREMIER (après « كانت له ») est-il عشرة (10) ou عشرين (20) ou "
     "autre ? Le SECOND (après « وقد بلغت ») est-il عشرة ou عشرين ou autre ? "
     "Transcris aussi les mots autour de chaque nombre. Réponds : « nombre1=… "
     "(chiffres : …), nombre2=… (chiffres : …) »."),
    ("n4-p110-ribs-curious", "p110-ribs.png",
     "Sur ce passage il y a un renvoi rouge [الموطأ رقم : 666] et, ailleurs dans le "
     "passage, un AUTRE groupe de chiffres imprimé (la couche texte du PDF porte un "
     "fragment « 0035 » quelque part près d'un mot « دينار »). Transcris TOUT groupe "
     "de chiffres visible CHIFFRE PAR CHIFFRE avec les 2-3 mots autour de chacun, et "
     "précise lequel est le renvoi rouge entre crochets. Réponds : « renvoi=…, "
     "autre_nombre=…, contexte=… »."),
    # --- p.109 : le cas de l'esclave : nombres ---
    ("n4-p109-abd-numbers", "p109-abd.png",
     "Dans le cas rapporté de Mālik : (1) « رجل كانت عنده … ومائة درهم » : le nombre "
     "est-il ستون (60) ou سبعين (70) ou autre — LETTRE PAR LETTRE ? (2) le taux de "
     "change « ببيضة … دراهم بدينار » : est-ce ثمانية (8) ou ثمانين (80) ou autre "
     "— LETTRE PAR LETTRE ? (3) la réponse de Mālik commence par « إنما لا تجب » ou "
     "« إنها لا تجب » ? Transcris la réponse complète MOT À MOT. Réponds : « "
     "dirhams=…, taux=…, ouverture_réponse=…, réponse=… »."),
    # --- p.109 : منفردة / متفرقة ---
    ("n4-p109-khalata-word", "p109-khalata.png",
     "Dans la phrase « فمن كانت عنده عشرون دينارا وجب عليه فيها الزكاة كانت … أو "
     "مختلطة » : le mot qui précède « أو مختلطة » — transcris-le LETTRE PAR LETTRE : "
     "est-ce منفردة ? متفرقة ? متميزة ? autre ? Réponds : « mot=…, lettres : … »."),
    # --- p.108 : ملونًا / ملوثًا ---
    ("n4-p108-mulawwan", "p108-hikma.png",
     "Dans l'item ج- de la section حكمتها : « طهارة للمال ; لأن تعلق حق الغير به "
     "يجعله … لا يطهر إلا بإخراجه منه ». Le mot après « يجعله » : transcris-le "
     "LETTRE PAR LETTRE — la lettre centrale est-elle ن (ملونًا) ou ث (ملوثًا) ou "
     "autre ? Réponds : « mot=…, lettres : … ». Puis, dans l'item د- : le verbe "
     "imprimé après « فالغني عندما يقوم بحق الله عليه يـ… بامتداد في نفسه » : "
     "transcris-le LETTRE PAR LETTRE (يشارك ? يشرع ? يشعر ? autre ?)."),
    # --- p.108 : le verset de la fin de حكمتها ---
    ("n4-p108-verse2", "p108-verse2-shurut.png",
     "CONFIRMATION chiffre par chiffre : (1) le verset coranique imprimé entre "
     "chevrons ﴿…﴾ : transcris-le MOT À MOT tel qu'imprimé (où s'arrête-t-il "
     "exactement ?) ; (2) le renvoi rouge TEL QU'IMPRIMÉ : nom de sourate + mot "
     "(الآية/آية) + numéro CHIFFRE PAR CHIFFRE dans l'ordre d'écriture : est-ce 104 "
     "ou 103 ou autre ? ; (3) la phrase qui suit immédiatement le renvoi MOT À "
     "MOT ; (4) l'en-tête de section qui ouvre ensuite (ثانيا… ? القسم الثاني… ?) "
     "exactement tel qu'imprimé."),
    # --- p.107 : en-tête + يؤول / يقول ---
    ("n4-p107-tahlil-head", "p107-tahlil.png",
     "(1) L'en-tête de la grande section d'analyse : transcris-le TEL QU'IMPRIMÉ "
     "— commence-t-il par « أولا : مفهوم الزكاة وحكمها وحكمتها » ou « أولا : "
     "مفهومها وحكمها وحكمتها » ou autre ? (2) Dans le paragraphe final, la lexie "
     "« فسميت زكاة بما … إليه إخراجها » : le verbe est-il يقول (qāf) ou يؤول "
     "(hamza-wāw) — LETTRE PAR LETTRE ? (3) Transcris la phrase complète contenant "
     "ce verbe MOT À MOT. Réponds : « en_tête=…, verbe=…, lettres : … »."),
    # --- p.110 : الفائدة / الفائضة (question 3 du تقويم) ---
    ("n4-p110-taqwim-q3", "p110-taqwim.png",
     "La question 3 du تقويم : « لماذا فرق مالك بين حول الربح وحول …؟ ». Le dernier "
     "mot : transcris-le LETTRE PAR LETTRE — la 6e lettre est-elle د (الفائدة) ou ض "
     "(الفائضة) ? Réponds : « mot=…, lettres : … ». Transcris aussi la question "
     "complète MOT À MOT."),
    # --- p.110 : fin de l'exploitation ---
    ("n4-p110-istithmar-fin", "p110-istithmar.png",
     "La citation de Mālik dans l'exploitation se termine par « …حتى يحول عليها "
     "الحول من يوم … » : le dernier mot est-il زكاتها ? زكيت ? زكاها ? autre — "
     "LETTRE PAR LETTRE ? Transcris les 6-8 derniers mots de la citation MOT À "
     "MOT, puis le renvoi rouge [الموطأ رقم : N] CHIFFRE PAR CHIFFRE (666 ou "
     "autre ?), puis les DEUX questions finales MOT À MOT."),
]

for key, img, q in ASKS:
    out = f"{OUT}/p4-{key}.json"
    if os.path.exists(out):
        print("•", key, "déjà lu")
        continue
    cmd = ["z-ai", "vision", "-p", f"{BASE}\nQUESTION : {q}", "-i", f"{CROPS}/{img}", "-o", out]
    r = subprocess.run(cmd, capture_output=True, text=True, timeout=300)
    print(("✓" if r.returncode == 0 else "✗"), key, (r.stderr or "").strip()[:150])

print("\n===== RÉSULTATS =====")
for key, img, q in ASKS:
    try:
        d = json.load(open(f"{OUT}/p4-{key}.json", encoding="utf-8"))
        print(f"\n----- {key} -----")
        print(d["choices"][0]["message"]["content"][:2000])
    except Exception as e:
        print(f"\n----- {key} ----- ERREUR {e}")

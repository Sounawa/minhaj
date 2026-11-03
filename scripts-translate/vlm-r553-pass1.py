#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""R553 — Passe 1 : lecture des composites 300 dpi (bornes + structure)."""
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
    ("p105-objectifs-tamhid", "p105-comp.png",
     "Page d'ouverture d'une leçon. (1) Transcris l'en-tête أهداف الدرس et les trois "
     "objectifs MOT À MOT. (2) Transcris le paragraphe de présentation (tamhīd) MOT À "
     "MOT, y compris toute citation coranique et son renvoi entre crochets. (3) Transcris "
     "l'en-tête de section suivant (الأحاديث) et le PREMIER hadith complet : isnād + matn "
     "entre guillemets + le renvoi [الموطأ رقم : ...] avec le numéro CHIFFRE PAR CHIFFRE "
     "tel qu'imprimé."),
    ("p106-hadith2-tarjama", "p106-comp.png",
     "Page du milieu d'une leçon. (1) Transcris le deuxième hadith complet : introduction "
     "de Mālik + matn entre guillemets + renvoi [الموطأ رقم : ...] CHIFFRE PAR CHIFFRE. "
     "(2) Transcris l'en-tête ترجمة الراوي et la biographie complète du transmetteur MOT "
     "À MOT (y compris tous les nombres : années, dates). (3) Transcris l'en-tête :الشرح "
     "et les deux premières définitions (الأذوذ / الأوسق) MOT À MOT avec les nombres en "
     "grammes."),
    ("p107-aouaq-analyse", "p107-comp.png",
     "Page du milieu d'une leçon. (1) Transcris la définition de الأوسق (troisième "
     "définition du :الشرح) MOT À MOT avec ses nombres en grammes. (2) Transcris "
     "l'en-tête استخلاص المضامين et ses items MOT À MOT. (3) Transcris l'ouverture de la "
     "section التحليل (المبحث الأول : مفهوم الزكاة) : la définition lexicale (الزكاة "
     "لغة) avec sa citation d'autorité et son renvoi, et la définition légale (شرعا) "
     "MOT À MOT."),
    ("p108-hukma-shurut", "p108-comp.png",
     "Page du milieu d'une leçon. (1) Transcris la section 2- حكمها : le verset coranique "
     "MOT À MOT avec son renvoi [الآية سورة ...] CHIFFRE PAR CHIFFRE, le hadith de "
     "l'islam bâti sur cinq avec son renvoi, puis 3- حكمتها items a/b/ج MOT À MOT. (2) "
     "Transcris la fin de la page : le verset de la sourate التوبة MOT À MOT avec son "
     "renvoi CHIFFRE PAR CHIFFRE, et l'ouverture de القسم الثاني : شروط وجوب الزكاة "
     "(1- ملك النصاب) jusqu'à la ligne « ثمنها ... خمس أواق »."),
    ("p109-nisab-dhahab", "p109-comp.png",
     "Page du milieu d'une leçon (شروط النصاب). (1) Transcris la phrase complète qui "
     "définit نصاب الذهب et le hadith avec renvoi [الموطأ رقم : ...] CHIFFRE PAR "
     "CHIFFRE. (2) Transcris le paragraphe de Mālik sur العبد (كان عند مالك رجل فيه "
     "عشرون دينارا...) et le renvoi CHIFFRE PAR CHIFFRE. (3) Transcris la phrase sur "
     "الذهب والفضة (الذهب لا يعتبر بالنصاب إلا...) et le passage sur الخلطاء/مال "
     "الغير. (4) Transcris l'ouverture 2- مرور الحول et le hadith avec son renvoi "
     "CHIFFRE PAR CHIFFRE."),
    ("p110-hawl-istithmar", "p110-comp.png",
     "Page du milieu d'une leçon. (1) Transcris le passage ب- حول الربا وفائدته et le "
     "récit de l'istiftā' (استفتى...) MOT À MOT, avec les renvois [الموطأ رقم : ...] "
     "CHIFFRE PAR CHIFFRE. (2) Transcris l'en-tête التقويم et ses items MOT À MOT. (3) "
     "Transcris l'en-tête الاستثمار et tout ce qui suit jusqu'au bas de la page MOT À "
     "MOT, y compris le renvoi [الموطأ رقم : ...] CHIFFRE PAR CHIFFRE."),
    ("p111-iedad", "p111-comp.png",
     "Dernière page d'une leçon. Transcris l'en-tête الإعداد القبلي et ses trois items "
     "MOT À MOT (c'est la préparation du cours suivant)."),
    ("p112-l16-objectifs", "p112-comp.png",
     "Page d'ouverture de la leçon SUIVANTE. (1) Transcris l'en-tête أهداف الدرس et les "
     "quatre objectifs MOT À MOT. (2) Transcris le premier paragraphe de présentation "
     "jusqu'aux questions finales. (3) Transcris l'en-tête الأحاديث et le premier hadith "
     "complet : isnād + matn + renvoi [الموطأ رقم : ...] CHIFFRE PAR CHIFFRE. (4) "
     "Transcris le début du deuxième hadith (قال مالك...)."),
    ("p104-l14-fin", "p104-comp.png",
     "Dernière page de la leçon PRÉCÉDENTE. Transcris l'en-tête الإعداد القبلي et ses "
     "items MOT À MOT (preuve que la page 104 clôt la leçon 14 et n'appartient PAS à la "
     "leçon 15)."),
]

for key, img, q in ASKS:
    out = f"{OUT}/p1-{key}.json"
    if os.path.exists(out):
        print("•", key, "déjà lu")
        continue
    cmd = ["z-ai", "vision", "-p", f"{BASE}\nQUESTION : {q}", "-i", f"{CROPS}/{img}", "-o", out]
    r = subprocess.run(cmd, capture_output=True, text=True, timeout=300)
    print(("✓" if r.returncode == 0 else "✗"), key, (r.stderr or "").strip()[:150])

print("\n===== RÉSULTATS =====")
for key, img, q in ASKS:
    try:
        d = json.load(open(f"{OUT}/p1-{key}.json", encoding="utf-8"))
        print(f"\n----- {key} -----")
        print(d["choices"][0]["message"]["content"][:2600])
    except Exception as e:
        print(f"\n----- {key} ----- ERREUR {e}")

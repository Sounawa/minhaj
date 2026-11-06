#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""R624 — pass 2 VLM : tranchage des NUMÉROS de hadith (chiffres OCR inversés)
+ fin du hadith أيوب (p14) + renvois du شرح (p12) + citation عائشة/خلاصة (p15).
Toute lecture est ancrée sur l'image ; aucun chiffre n'est deviné."""
import json
import subprocess

HOME = "/home/z/my-project"
CROPS = f"{HOME}/tr-tmp/qa-crops-r624"
OUT = f"{HOME}/tr-tmp/vlm-r624"

BASE = ("Tu lis un extrait d'un manuel scolaire marocain de hadith (Muwaṭṭaʾ Mālik / "
        "Šarḥ az-Zarqānī, 3e année collégiale). Réponds UNIQUEMENT à la question, "
        "par transcription EXACTE du texte imprimé. N'invente AUCUN chiffre : regarde "
        "chiffre par chiffre, de droite à gauche comme imprimé.")

ASKS = [
    ("p10-line1", "p10-line1.png",
     "Transcris EXACTEMENT la ligne entière, y compris le crochet [الموطأ رقم : ...] "
     "et le numéro imprimé chiffre par chiffre."),
    ("p10-bottom", "p10-bottom.png",
     "Sur cette partie basse de page, transcris le DEUXIÈME hadith (عن مالك عن "
     "عطاء: أن عمر بن الخطاب كان يغتسل...) et le crochet [الموطأ رقم : ...] avec "
     "son numéro exact chiffre par chiffre."),
    ("p11-line1", "p11-line1.png",
     "Transcris EXACTEMENT la ligne : hadith et numéro du crochet [الموطأ رقم : ...], "
     "chiffre par chiffre."),
    ("p11-line2", "p11-line2.png",
     "Transcris EXACTEMENT la ligne : hadith et numéro du crochet [الموطأ رقم : ...], "
     "chiffre par chiffre."),
    ("p13-line1", "p13-line1.png",
     "Transcris EXACTEMENT la ligne : texte et numéro du crochet [الموطأ رقم : ...], "
     "chiffre par chiffre."),
    ("p13-line2", "p13-line2.png",
     "Transcris EXACTEMENT la ligne : texte et numéro du crochet [الموطأ رقم : ...], "
     "chiffre par chiffre."),
    ("p14-line1", "p14-line1.png",
     "Transcris EXACTEMENT la ligne : texte et numéro du crochet [الموطأ رقم : ...], "
     "chiffre par chiffre."),
    ("p14-line2", "p14-line2.png",
     "Transcris EXACTEMENT la ligne : texte et numéro du crochet [الموطأ رقم : ...], "
     "chiffre par chiffre."),
    ("p16-line1", "p16-line1.png",
     "Transcris EXACTEMENT la ligne : texte et numéro du crochet [الموطأ رقم : ...], "
     "chiffre par chiffre."),
    ("p12-sharh-ref", "p12-sharh-ref.png",
     "Transcris EXACTEMENT : (1) la définition d'ابن عرفة entre « » ; (2) le renvoi "
     "entre [ ] qui la suit, avec le nom du livre et le NUMÉRO de page exact ; "
     "(3) la phrase sur الاقتصار على عرفة / بيان منزلته في الحج ; (4) la citation "
     "«الحج عرفة» et sa source entre [ ]."),
    ("p12-aya", "p12-aya.png",
     "Transcris EXACTEMENT la citation coranique entre ﴿ ﴾ (mot à mot, complète) et "
     "le renvoi [سورة ... الآية : ...] avec son NUMÉRO exact chiffre par chiffre."),
    ("p14-tail", "p14-tail.png",
     "Transcris EXACTEMENT la FIN du hadith de ابن حنين (à partir de «قال: من هذا؟» "
     "jusqu'à la fin), puis la phrase de commentaire qui suit (قول أبي أيوب... et la "
     "phrase «وفيه...» qui suit), mot à mot tel qu'imprimé."),
    ("p15-aisha", "p15-aisha.png",
     "Transcris EXACTEMENT le bloc «3- غسل المحرم لدخول مكة» : la première phrase "
     "complète (من الاغتسالات المستحبة...), puis la citation de عائشة entre « » avec "
     "sa source entre [ ], mot à mot."),
    ("p15-khulasa", "p15-khulasa.png",
     "Transcris EXACTEMENT le paragraphe يستفاد من الدرس... (de «يستفاد» jusqu'à la "
     "fin du paragraphe), mot à mot tel qu'imprimé."),
]

for key, img, q in ASKS:
    out = f"{OUT}/{key}.json"
    cmd = ["z-ai", "vision", "-p", f"{BASE}\nQUESTION : {q}", "-i", f"{CROPS}/{img}", "-o", out]
    r = subprocess.run(cmd, capture_output=True, text=True, timeout=300)
    print(("OK  " if r.returncode == 0 else "FAIL") + f" {key}")

print("\n===== EXTRAITS =====")
for key, _, _ in ASKS:
    try:
        d = json.load(open(f"{OUT}/{key}.json", encoding="utf-8"))
        print(f"\n----- {key} -----")
        print(d["choices"][0]["message"]["content"][:800])
    except Exception as e:
        print(f"\n----- {key} ----- ERREUR {e}")

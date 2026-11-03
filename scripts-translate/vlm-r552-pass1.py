#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""R552 — 1re passe VLM : structure + hadiths + numéros, composites 300 dpi p.98-104 (leçon 14, pdf-15)."""
import json
import time
import os
import subprocess

HOME = "/home/z/my-project"
CROPS = f"{HOME}/tr-tmp/qa-crops-r552"
OUT = f"{HOME}/tr-tmp/vlm-r552"
os.makedirs(OUT, exist_ok=True)

BASE = ("Tu lis une image d'un manuel scolaire marocain de hadith (Muwaṭṭaʾ Mālik / "
        "Šarḥ az-Zarqānī, 2e année collégiale). Réponds UNIQUEMENT à la question posée, "
        "par transcription EXACTE du texte imprimé visible, token par token. Si tu n'es "
        "pas sûr d'un mot ou d'un chiffre, écris [illisible]. N'invente AUCUN texte, ne "
        "complète JAMAIS de mémoire (n'utilise PAS de version canonique du hadith que tu "
        "connaîtrais), ne corrige pas l'imprimé même s'il te paraît fautif.")

ASKS = [
    ("p98", "p98-comp.png",
     "Transcris dans l'ordre : (1) le titre de section en haut et la liste numérotée "
     "des objectifs (chaque item en entier, mot à mot) ; (2) la phrase d'appel du "
     "tamhīd puis le hadith d'Abū Hurayra ENTIER : isnād complet, matn entre "
     "guillemets, et le renvoi entre crochets [kitāb/bāb/musnad + الموطأ رقم : N] "
     "chiffre par chiffre tel qu'imprimé ; (3) la question finale (فما أحكام...) ; "
     "(4) le début de la section أحاديث الدرس : transcris le premier hadith "
     "ENTIER (isnād + matn + renvoi [الموطأ رقم : N] chiffre par chiffre)."),
    ("p99", "p99-comp.png",
     "Transcris dans l'ordre : (1) la fin du premier hadith de أحاديث الدرس si elle "
     "continue en haut de page (isnād + matn + renvoi chiffre par chiffre) ; (2) le "
     "deuxième hadith ENTIER (isnād + matn + renvoi [الموطأ رقم : N] chiffre par "
     "chiffre) ; (3) le troisième hadith ENTIER (isnād + matn + renvoi chiffre par "
     "chiffre) ; (4) le titre et le contenu de l'encadré ترجمة الراوي (mot à mot)."),
    ("p100", "p100-comp.png",
     "Transcris dans l'ordre : (1) le titre de section et la liste numérotée "
     "(خلاصة المضامين) ; (2) le titre أولاً et le sous-titre ; (3) le paragraphe "
     "صفة الدفن (transcription suivie mot à mot, y compris le hadith cité et son "
     "renvoi [صحيح مسلم] ou autre, chiffre par chiffre) ; (4) le titre du "
     "sous-point 2 s'il apparaît."),
    ("p101", "p101-comp.png",
     "Transcris dans l'ordre : (1) la suite du hadith de la page précédente (isnād + "
     "matn + renvoi chiffre par chiffre) ; (2) le sous-titre 2- حكم نقل الميت avant "
     "الدفن et son paragraphe entier (y compris hadith + renvoi [الموطأ رقم : N] "
     "chiffre par chiffre) ; (3) le paragraphe de discussion (يختلف في جواز نقل "
     "الميت...) ; (4) le titre ثانياً بعض الآداب المعتبرة (ou équivalent) et "
     "l'item 1 ENTIER (titre + explication + hadith avec isnād, matn, renvoi "
     "chiffre par chiffre)."),
    ("p102", "p102-comp.png",
     "Transcris dans l'ordre : (1) la fin de l'item 1 (hadith + renvoi chiffre par "
     "chiffre + commentaire) ; (2) l'item 2 ENTIER (titre الصبر والرضا + paragraphe "
     "+ citation coranique avec sa référence [سورة ... الآية N] + hadiths avec "
     "renvois chiffre par chiffre) ; (3) l'item 3 ENTIER (titre + hadiths + renvois "
     "chiffre par chiffre)."),
    ("p103", "p103-comp.png",
     "Transcris dans l'ordre : (1) les items 4 et 5 ENTIERs (titres + paragraphes + "
     "hadiths avec isnāds et renvois chiffre par chiffre) ; (2) le titre التقويم et "
     "ses questions numérotées ; (3) le titre الاستثمار et son contenu entier "
     "(hadith + renvoi chiffre par chiffre + phrase sur le Šarḥ az-Zarqānī)."),
    ("p104", "p104-comp.png",
     "Transcris : (1) le titre de section (الإعداد القبلي pour la leçon suivante) ; "
     "(2) la phrase d'introduction ; (3) TOUS les items numérotés mot à mot "
     "(notamment la liste de lexies : chaque mot exactement, séparé par des "
     "tirets/virgules) ; (4) tout autre texte visible sur la page."),
]

def vision_call(prompt, img, out, tries=5):
    cmd = ["z-ai", "vision", "-p", prompt, "-i", img, "-o", out]
    for t in range(tries):
        r = subprocess.run(cmd, capture_output=True, text=True, timeout=300)
        if r.returncode == 0:
            return True, ""
        err = (r.stderr or "") + (r.stdout or "")
        if "429" in err or "Too many" in err:
            wait = 45 + 30 * t
            print(f"  429 — attente {wait}s (tentative {t + 1}/{tries})")
            time.sleep(wait)
            continue
        return False, err[:200]
    return False, "429 persistant"

for key, img, q in ASKS:
    out = f"{OUT}/pass1-{key}.json"
    if os.path.exists(out):
        print("•", key, "déjà lu")
        continue
    ok, err = vision_call(f"{BASE}\nQUESTION : {q}", f"{CROPS}/{img}", out)
    print(("✓" if ok else "✗"), key, err)

print("\n===== RÉSULTATS =====")
for key, img, q in ASKS:
    try:
        d = json.load(open(f"{OUT}/pass1-{key}.json", encoding="utf-8"))
        print(f"\n----- {key} -----")
        print(d["choices"][0]["message"]["content"][:4000])
    except Exception as e:
        print(f"\n----- {key} ----- ERREUR {e}")

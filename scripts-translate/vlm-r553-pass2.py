#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""R553 — Passe 2 : micro-crops numéros — questions fermées chiffre par chiffre."""
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
    ("n-p105-655", "n-p105-655.png",
     "Un renvoi imprimé en rouge entre crochets [الموطأ رقم : N]. Lis le numéro N "
     "CHIFFRE PAR CHIFFRE de droite à gauche tel qu'imprimé : premier chiffre, deuxième "
     "chiffre, troisième chiffre. Réponds au format : « chiffre1=…, chiffre2=…, "
     "chiffre3=…, numéro=… ». Puis transcris le mot précédant le numéro (après الرقم)."),
    ("n-p106-668", "n-p106-668.png",
     "Un renvoi imprimé en rouge entre crochets [الموطأ رقم : N] en fin de citation. "
     "Lis le numéro N CHIFFRE PAR CHIFFRE de droite à gauche tel qu'imprimé. Réponds : "
     "« chiffre1=…, chiffre2=…, chiffre3=…, numéro=… ». Puis transcris les 3-4 mots "
     "imprimés juste avant le crochet (la fin de la phrase de Mālik)."),
    ("n-p106-dates", "n-p106-dates.png",
     "Trois nombres imprimés sur la ligne (années de mort du transmetteur, format : "
     "« مات سنة N وقيل N وقيل N هـ »). Lis CHAQUE nombre CHIFFRE PAR CHIFFRE tel "
     "qu'imprimé. Réponds : « premier nombre=… (chiffres : …), deuxième=…, troisième=… ». "
     "Transcris aussi les mots entre les nombres (وقيل / مات سنة / هـ)."),
    ("n-p106-2975", "n-p106-2975.png",
     "Un nombre décimal imprimé (poids du dirham en grammes, format N,NNN). Transcris-le "
     "CHIFFRE PAR CHIFFRE tel qu'imprimé, et transcris les mots autour (بناء على أن "
     "الدرهم يزن … / غرام). Réponds : « nombre=…, chiffres : … »."),
    ("n-p107-1306", "n-p107-1306.png",
     "Un nombre décimal imprimé (poids du wasq en kilogrammes). Transcris-le CHIFFRE PAR "
     "CHIFFRE tel qu'imprimé et les mots autour. Réponds : « nombre=…, chiffres : …, "
     "contexte=… »."),
    ("n-p107-arafa", "n-p107-arafa.png",
     "Un renvoi entre crochets [شرح حدود ابن عرفة، N/M] (référence livre tome/page). "
     "Transcris le renvoi TEL QU'IMPRIMÉ, les deux nombres CHIFFRE PAR CHIFFRE."),
    ("n-p108-nur", "n-p108-nur.png",
     "Un renvoi coranique imprimé en rouge [سورة النور، الآية N] ou similaire. Transcris "
     "le renvoi TEL QU'IMPRIMÉ et lis le numéro d'āya CHIFFRE PAR CHIFFRE. Réponds : "
     "« renvoi=…, chiffres : … ». Transcris aussi le mot qui précède le renvoi (fin de "
     "la citation coranique, 1-3 mots)."),
    ("n-p108-104", "n-p108-104.png",
     "Un renvoi coranique imprimé en rouge entre crochets à la fin d'une citation. "
     "Transcris le renvoi TEL QU'IMPRIMÉ (nom de sourate + numéro d'āya) CHIFFRE PAR "
     "CHIFFRE, et transcris les 3-4 derniers mots imprimés avant le crochet (fin de la "
     "citation coranique)."),
    ("n-p109-662", "n-p109-662.png",
     "Un renvoi imprimé en rouge [الموطأ رقم : N]. Lis le numéro CHIFFRE PAR CHIFFRE de "
     "droite à gauche tel qu'imprimé. Réponds : « chiffre1=…, chiffre2=…, chiffre3=…, "
     "numéro=… ». Transcris les 3-4 mots imprimés juste avant le crochet."),
    ("n-p109-664", "n-p109-664.png",
     "Un renvoi imprimé en rouge [الموطأ رقم : N]. Lis le numéro CHIFFRE PAR CHIFFRE de "
     "droite à gauche tel qu'imprimé. Réponds : « chiffre1=…, chiffre2=…, chiffre3=…, "
     "numéro=… ». Transcris les 3-4 mots imprimés juste avant le crochet."),
    ("n-p109-660", "n-p109-660.png",
     "Il y a sur cette bande un renvoi rouge [الموطأ رقم : N] et un autre nombre "
     "imprimé (peut-être un numéro de note de bas de page). Transcris TOUT ce qui est "
     "imprimé sur cette bande, le numéro de Muwaṭṭaʾ CHIFFRE PAR CHIFFRE et l'autre "
     "nombre CHIFFRE PAR CHIFFRE, en disant lequel est en rouge/entre crochets."),
    ("n-p110-46", "n-p110-46.png",
     "En début de récit imprimé il y a un petit nombre (note de bas de page ?). "
     "Transcris les premiers mots du récit (استفتى …) et le petit nombre CHIFFRE PAR "
     "CHIFFRE tel qu'imprimé, en précisant sa position (exposant après quel mot)."),
    ("n-p110-666a", "n-p110-666a.png",
     "Il y a un nombre curieux et un renvoi rouge [الموطأ رقم : N] sur cette bande. "
     "Transcris TOUT ce qui est imprimé : le nombre curieux CHIFFRE PAR CHIFFRE (avec "
     "ses virgules/points) et le numéro de Muwaṭṭaʾ CHIFFRE PAR CHIFFRE."),
    ("n-p110-666b", "n-p110-666b.png",
     "Un renvoi imprimé en rouge [الموطأ رقم : N]. Lis le numéro CHIFFRE PAR CHIFFRE de "
     "droite à gauche tel qu'imprimé. Réponds : « chiffre1=…, chiffre2=…, chiffre3=…, "
     "numéro=… ». Transcris les mots imprimés juste avant le crochet."),
]

for key, img, q in ASKS:
    out = f"{OUT}/p2-{key}.json"
    if os.path.exists(out):
        print("•", key, "déjà lu")
        continue
    cmd = ["z-ai", "vision", "-p", f"{BASE}\nQUESTION : {q}", "-i", f"{CROPS}/{img}", "-o", out]
    r = subprocess.run(cmd, capture_output=True, text=True, timeout=300)
    print(("✓" if r.returncode == 0 else "✗"), key, (r.stderr or "").strip()[:150])

print("\n===== RÉSULTATS =====")
for key, img, q in ASKS:
    try:
        d = json.load(open(f"{OUT}/p2-{key}.json", encoding="utf-8"))
        print(f"\n----- {key} -----")
        print(d["choices"][0]["message"]["content"][:1200])
    except Exception as e:
        print(f"\n----- {key} ----- ERREUR {e}")

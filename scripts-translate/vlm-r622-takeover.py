#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""R622 takeover — lectures VLM ancrées (anti-hallucination, méthode R538/R621).
Points restants contestés après OCR multicouche : item(s) iʿdād p.56, noms de
l'isnād p.54, mot المفردات p.53, item 1 du التقييم p.55.
Sortie : tr-tmp/vlm-r622/<key>.json"""
import json
import subprocess

HOME = "/home/z/my-project"
OUT = f"{HOME}/tr-tmp/vlm-r622"
C = f"{HOME}/tr-tmp/r622-ocr"

BASE = ("Tu lis une image d'un manuel scolaire marocain de hadith (علوم الحديث "
        "الثانية ثانوي). Réponds UNIQUEMENT à la question posée, par transcription "
        "EXACTE du texte imprimé visible. Si tu n'es pas sûr d'un mot, écris "
        "[illisible]. N'invente AUCUN texte, ne complète jamais de mémoire.")

ASKS = [
    ("idad-items-p56", "ADJ49-takeover-idad-full-p56-1200.png",
     "Sous l'encadré الاعداد القبلي, après la phrase أعد درس المتابعات والشواهد "
     "وأبحث عما يلي: combien d'items sont listés ? Transcris chaque item EXACTEMENT "
     "tel qu'imprimé, avec son numéro/lettre (1., 2., أ., ب. ...). Y a-t-il un item "
     "2 ? La couche OCR hésite entre « 1. مفهوم المتابعات والشواهد. » et "
     "« أ. أمثلة للشواهد والاعتبار » — tranche par ce que tu VOIS."),
    ("isnad-names-p54", "ADJ27-takeover-isnad-p54-1200.png",
     "Transcris EXACTEMENT, mot à mot : (1) le nom du narrateur en début de voie : "
     "« من طريق ... » ; (2) la parenthèse « وهو أخو ... » avec le nom et la "
     "qualification complète ; (3) la chaîne entre la parenthèse et ابن عباس "
     "(quels noms exacts : عن أبي إسحاق عن ... بن ... ?) ; (4) la fin du hadith "
     "entre guillemets."),
    ("mufradat-word-p53", "ADJ35-takeover-mufradat-line-p53-1800.png",
     "Dans la citation du الراغب الأصفهاني, la définition commence par « المعرفة "
     "والعرفان: إدراك الشيء بتفكر وتدبر ». Quel est le mot EXACT imprimé juste "
     "après « بتفكر وتدبر » ? (a) لأثره  (b) لاؤثره  (c) autre — transcris "
     "exactement, puis transcris la fin de la citation jusqu'au renvoi entre "
     "crochets avec le numéro de page EXACT."),
    ("takyif-item1-p55", "ADJ32b-takeover-takyif-p55-900.png",
     "Sous la rubrique التقييم, transcris EXACTEMENT chaque item numéroté tel "
     "qu'imprimé. La couche OCR lit « 1. أعرِّف الحديث المعروف. » pour le premier "
     "— confirme ou corrige mot à mot, et transcris aussi le second item."),
]

subprocess.run(["mkdir", "-p", OUT], check=True)
for key, img, q in ASKS:
    out = f"{OUT}/{key}.json"
    cmd = ["z-ai", "vision", "-p", f"{BASE}\nQUESTION : {q}", "-i", f"{C}/{img}", "-o", out]
    r = subprocess.run(cmd, capture_output=True, text=True, timeout=240)
    print(("OK " if r.returncode == 0 else f"FAIL {r.stderr[:200]} ") + key)

print("\n===== RÉSULTATS =====")
for key, _, _ in ASKS:
    try:
        d = json.load(open(f"{OUT}/{key}.json", encoding="utf-8"))
        print(f"\n----- {key} -----")
        print(d["choices"][0]["message"]["content"][:1500])
    except Exception as e:
        print(f"\n----- {key} ----- ERREUR {e}")

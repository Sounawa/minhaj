#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""R592 — crops 1200 dpi p.76-79 de ulum-hadith-1-thanawi.pdf + OCR local psm 6.
Leçon 15 ulum-hadith-tanawi-1 (pdf-mut23h2q-126, الحديث الغريب, p.76-79).
Zones sensibles (OCR 300 dpi dégradé) :
  Z1  p76 (0.00-0.30) — bannière/أهداف + تمهيد
  Z2  p76 (0.46-0.78) — متن box (bayt partiel) + شرح box
  Z3  p77 (0.00-0.30) — top «2- أبين أقسام» + header التحليل + تعريف
  Z4  p77 (0.55-1.00) — أقسام درجة صحته + حديث السفر Mālik
  Z5  p78 (0.00-0.32) — ʿAbd ar-Razzāq + Ibn Ḥanbal + header أقسام 2
  Z6  p78 (0.32-1.00) — الخمسة أقسام + أم زرع + زكاة الفطر
  Z7  p79 (0.00-1.00) — استخلاص/استثمار/إعداد قبلي + quote Ibn Raǧab
"""
import os
import subprocess
import sys

import fitz

HOME = "/home/z/my-project"
PDF = f"{HOME}/content/textbooks-src/ulum-hadith-1-thanawi.pdf"
WORK = f"{HOME}/tr-tmp/r592-uh1/crops"
TESSDATA = f"{HOME}/scripts-translate/tessdata"

ZONES = [
    ("Z1-p76-top-banniere", 76, 0.00, 0.30),
    ("Z2-p76-bayt-matn-charh", 76, 0.46, 0.78),
    ("Z3-p77-top-tahlil", 77, 0.00, 0.30),
    ("Z4-p77-aqsim-sihha-malik", 77, 0.55, 1.00),
    ("Z5-p78-quotes-abdarrazzak", 78, 0.00, 0.32),
    ("Z6-p78-khamsat-aqsim", 78, 0.32, 1.00),
    ("Z7-p79-full-headers", 79, 0.00, 1.00),
]


def main() -> int:
    os.makedirs(WORK, exist_ok=True)
    tags = {t.split("-")[0] for t in sys.argv[1:]} or {z[0].split("-")[0] for z in ZONES}
    doc = fitz.open(PDF)
    env = dict(os.environ, TESSDATA_PREFIX=TESSDATA)
    for tag, page, f0, f1 in ZONES:
        if tag.split("-")[0] not in tags:
            continue
        p = doc[page - 1]
        r = p.rect
        clip = fitz.Rect(r.x0, r.y0 + f0 * r.height, r.x1, r.y0 + f1 * r.height)
        png = f"{WORK}/{tag}.png"
        p.get_pixmap(dpi=1200, clip=clip).save(png)
        base = png[:-4]
        subprocess.run(["tesseract", png, base, "-l", "ara", "--psm", "6"],
                       env=env, capture_output=True, text=True)
        ocr = open(base + ".txt", encoding="utf-8", errors="replace").read()
        print(f"===== {tag} ({os.path.getsize(png)//1024} Ko) =====")
        print(ocr.strip()[:1400])
        print()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# IA-2 — zoom2-h6-15 : rendus 1200 dpi (gris) des pp.81-84 du tirage hadith-6ep
# + recadrage de bandes ciblées + OCR psm 6 (et psm 4 pour bandes larges).
# Zones critiques L14 : أهداف item 2-3, «إن الله فرض…» (blancs), الحديث الثاني
# (جاره بوائقه), الحديث الثالث (chiffres المستدرك), en-têtes de questions,
# tableaux du النشاط 3 (p.83), النشاط 4 + الإعداد القبلي (p.84).
import subprocess, os
from PIL import Image

PDF = "/home/z/my-project/minhaj/content/textbooks-src/hadith-6ep.pdf"
DIR = "/home/z/my-project/pdf-work/h6-15"
TESSDATA = "/home/z/my-project/pdf-work/tessdata"
env = dict(os.environ, TESSDATA_PREFIX=TESSDATA)

# bandes (page, y0, y1, libellé) en coordonnées 600 dpi — recadrées à 1200 dpi
BANDS = [
    (81, 1650, 2500, "ahdaf-2-3"),        # أهداف items 2-3
    (81, 3050, 3660, "nachat1-items12"),  # الزهد + إن الله فرض (blancs)
    (81, 3830, 4350, "nachat1-item3"),    # لا ضرر ولا ضرار
    (81, 4400, 5150, "nachat1-items45"),  # خطورة اللسان + الصحابيين
    (81, 5230, 6100, "nachat2-hadith1"),  # الحديث الأول p.81
    (82,  640, 1400, "hadith1-suite"),    # قالوا فمن المؤمن + citation
    (82, 1400, 2150, "hadith2"),          # لا يستقيم إيمان عبد (CRITIQUE)
    (82, 2150, 3150, "hadith3"),          # اضمنوا لي ستا + رقم المستدرك
    (82, 3150, 3350, "questions-header"),
    (82, 3930, 4130, "question3"),
    (82, 4550, 4800, "question5"),
    (82, 4850, 5400, "question5-table"),
    (83, 1000, 1350, "nachat3-item1"),
    (83, 1200, 3000, "nachat3-table1"),
    (83, 2850, 3420, "nachat3-item2"),
    (83, 3350, 4000, "nachat3-table2-head"),
    (83, 3950, 5750, "nachat3-table2-rows"),
    (83, 5650, 6450, "nachat3-table2-end"),
    (84,  600, 1150, "nachat4-head"),
    (84, 1100, 2600, "nachat4-steps"),
    (84, 2500, 3400, "idad-qabli"),
]

os.makedirs(f"{DIR}/zoom", exist_ok=True)
for p in (81, 82, 83, 84):
    full = f"{DIR}/zoom/p{p:03d}-1200.png"
    if not os.path.exists(full):
        subprocess.run(["pdftoppm", "-f", str(p), "-l", str(p), "-r", "1200",
                        "-gray", "-png", "-singlefile", PDF, full[:-4]], check=True)

for (p, y0, y1, name) in BANDS:
    img = Image.open(f"{DIR}/zoom/p{p:03d}-1200.png")
    crop = img.crop((0, y0 * 2, img.width, y1 * 2))
    out = f"{DIR}/zoom/z{p:03d}-{name}.png"
    crop.save(out)
    for psm in (6, 4):
        r = subprocess.run(["tesseract", out, "stdout", "-l", "ara", "--psm", str(psm)],
                           env=env, capture_output=True, text=True)
        txt = " ".join(r.stdout.split())
        if txt.strip():
            print(f"── z{p:03d}-{name} psm{psm}: {txt}")
print("OK zoom2-h6-15")

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# IA-2 — zoom5-h6-15 : bandes ciblées pp.85-89 pour L15 «تغيير المنكر ومراتبه»
# (rendus 1200 dpi pleine page + recadrage de bandes + OCR psm 6/4).
import subprocess, os
from PIL import Image

PDF = "/home/z/my-project/minhaj/content/textbooks-src/hadith-6ep.pdf"
DIR = "/home/z/my-project/pdf-work/h6-15"
TESSDATA = "/home/z/my-project/pdf-work/tessdata"
env = dict(os.environ, TESSDATA_PREFIX=TESSDATA)

# (page, y0, y1, nom) en coordonnées 600 dpi
BANDS = [
    (85,  580,  980, "cartouche"),
    (85, 1930, 2570, "ahdaf-23"),
    (85, 2900, 3480, "tamhid-1"),
    (85, 3430, 3920, "tamhid-2"),
    (85, 4700, 5140, "hadith"),
    (86, 1280, 1510, "glose-munkar"),
    (86, 1540, 1760, "glose-yad"),
    (86, 2040, 2260, "glose-qalb"),
    (86, 2280, 2500, "glose-adaf"),
    (86, 3050, 3460, "istikhlas"),
    (86, 4050, 4350, "analyse-intro"),
    (86, 5580, 6180, "hukm-kitab"),
    (87, 1200, 1980, "fard-kifaya"),
    (87, 2000, 2540, "la-yasqut"),
    (87, 2940, 3200, "yushtarata"),
    (88,  640, 1140, "shafici"),
    (88, 3440, 3660, "adaf-meaning"),
    (88, 4260, 5320, "mimma-yustafad"),
    (89,  600, 1160, "taqwim"),
    (89, 1150, 1650, "istithmar-1"),
    (89, 1600, 2100, "istithmar-2"),
    (89, 2050, 2560, "idad"),
]

os.makedirs(f"{DIR}/zoom", exist_ok=True)
for p in (85, 86, 87, 88, 89):
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
print("OK zoom5-h6-15")

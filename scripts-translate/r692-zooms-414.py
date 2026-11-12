#!/usr/bin/env python3
# R692 - zooms composites pour adjudication leçon 414 (hadith-3es, p.164-169)
from PIL import Image
import os

SRC = "/home/z/my-project/tr-tmp/pages-414"
OUT = "/home/z/my-project/tr-tmp/m414-r692"
os.makedirs(OUT, exist_ok=True)

# (page, y0, y1, scale, tag)  — y en fraction de la hauteur
ZOOMS = [
    ("p164.png", 0.62, 0.99, 2.0, "z1-hadith1352-chaine"),      # hadith 1 complet
    ("p166.png", 0.52, 0.72, 2.2, "z2-p166-ab-alhur"),          # points a-b (arju'a, awra')
    ("p167.png", 0.16, 0.36, 2.2, "z3-p167-hadith-ali"),        # hadith d'Ali (mu'abada)
    ("p168.png", 0.44, 0.74, 2.2, "z4-p168-hadith1363-1364"),   # Abû Ayyûb + hadith Mâlik 1364
    ("p168.png", 0.66, 0.90, 2.2, "z5-p168-hadith1365-1366"),   # Ibn Shihâb + Nâfi'
    ("p169.png", 0.24, 0.60, 2.0, "z6-p169-hadith-aicha"),      # hadith d'A'isha 1358
]

for page, y0, y1, scale, tag in ZOOMS:
    img = Image.open(os.path.join(SRC, page))
    W, H = img.size
    box = (0, int(y0 * H), W, int(y1 * H))
    crop = img.crop(box)
    nw = int(crop.width * scale)
    nh = int(crop.height * scale)
    if nw > 1900:
        nh = int(nh * 1900 / nw)
        nw = 1900
    crop = crop.resize((nw, nh), Image.LANCZOS)
    out = os.path.join(OUT, f"{tag}.png")
    crop.save(out)
    print(f"{tag}: {page} y[{y0}-{y1}] -> {nw}x{nh}")
print("OK")

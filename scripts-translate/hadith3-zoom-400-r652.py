# -*- coding: utf-8 -*-
"""Minhāj — Recadrages zoom R652 (leçon 11, p.78-83) : bandes de lignes à fort
grossissement pour adjudications VLM. Sortie tr-tmp/qa-crops-r652/z-*.png."""
from PIL import Image

DIR = "/home/z/my-project/tr-tmp/qa-crops-r652/"

# (nom, page, x0%, x1%, y0%, y1%, zoom)
JOBS = [
    ("p78-tamhid", 78, 0.05, 0.95, 0.28, 0.52, 2.2),
    ("p79-aya-L", 79, 0.05, 0.55, 0.10, 0.42, 2.5),
    ("p79-aya-R", 79, 0.50, 0.97, 0.10, 0.42, 2.5),
    ("p79-sad", 79, 0.05, 0.97, 0.42, 0.62, 2.2),
    ("p79-tarjama", 79, 0.05, 0.97, 0.62, 0.95, 2.5),
    ("p80-recit", 80, 0.05, 0.97, 0.10, 0.40, 2.2),
    ("p81-sad", 81, 0.05, 0.97, 0.18, 0.40, 2.2),
    ("p81-haid", 81, 0.05, 0.97, 0.68, 0.97, 2.5),
    ("p82-top", 82, 0.05, 0.97, 0.04, 0.34, 2.2),
    ("p82-fitwa", 82, 0.05, 0.97, 0.10, 0.48, 2.2),
    ("p82-nums", 82, 0.05, 0.97, 0.55, 0.97, 2.5),
    ("p83-close", 83, 0.05, 0.97, 0.04, 0.28, 2.5),
    ("p83-hadith", 83, 0.05, 0.97, 0.28, 0.62, 2.5),
    ("p83-idad", 83, 0.05, 0.97, 0.60, 0.97, 2.5),
]

for name, page, x0, x1, y0, y1, z in JOBS:
    import glob
    cands = glob.glob(DIR + f"hi-{page}-*.png") or glob.glob(DIR + f"hi-{page}*.png")
    img = Image.open(cands[0])
    W, H = img.size
    box = (int(x0 * W), int(y0 * H), int(x1 * W), int(y1 * H))
    crop = img.crop(box)
    crop = crop.resize((int(crop.width * z), int(crop.height * z)), Image.LANCZOS)
    out = DIR + f"z-{name}.png"
    crop.save(out)
    print(out, crop.size)

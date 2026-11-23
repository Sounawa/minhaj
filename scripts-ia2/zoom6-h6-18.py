#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# IA-2 — zoom6-h6-18 : OCR tesseract des crops 3600 (z5) + binarisation de l'encadré آية
# + correction du crop ساعة (mot après ساعة).
import subprocess, os
import numpy as np
from PIL import Image, ImageOps

PDF = "/home/z/my-project/pdf-work/hadith-6ep.pdf"
DIR = "/home/z/my-project/pdf-work/h6-15"
TESSDATA = "/home/z/my-project/pdf-work/tessdata"
env = dict(os.environ, TESSDATA_PREFIX=TESSDATA)
os.makedirs(f"{DIR}/zoom", exist_ok=True)

def crop_pdf(name, page, y0, y1, dpi, color=True):
    out = f"{DIR}/zoom/{name}"
    if not os.path.exists(out + ".png"):
        f = dpi / 600.0
        W, H = int(5308 * f) + 40, int(6725 * f) + 40
        Y0, Y1 = int(y0 * f), int(y1 * f)
        args = ["pdftoppm", "-f", str(page), "-l", str(page), "-r", str(dpi),
                "-png", "-singlefile",
                "-x", str(0), "-y", str(Y0), "-W", str(W), "-H", str(Y1 - Y0),
                PDF, out]
        if not color:
            args.insert(-2, "-gray")
        subprocess.run(args, check=True)
    return out + ".png"

def ocr_save(png, name, psms=(7, 6)):
    for psm in psms:
        txt = f"{DIR}/zoom/{name}-psm{psm}.txt"
        if os.path.exists(txt):
            continue
        r = subprocess.run(["tesseract", png, "stdout", "-l", "ara", "--psm", str(psm)],
                           env=env, capture_output=True, text=True)
        with open(txt, "w") as fh:
            fh.write(r.stdout)
    print(f"{name}: OCR OK")

# 1) OCR direct des crops z5 3600 (couleur → tesseract gère)
for nm in ("z5-p102-item4-l1", "z5-p103-manas-w", "z5-p104-aya-l1", "z5-p104-aya-l2",
           "z5-p104-aya-l3", "z5-p100-matn-p", "z5-p101-gloses2", "z5-p101-ragabba3",
           "z5-p102-jabir2", "z5-p104-table2"):
    ocr_save(f"{DIR}/zoom/{nm}.png", nm)

# 2) binarisation de l'encadré آية (fond coloré → seuils)
for nm in ("z5-p104-aya-l1", "z5-p104-aya-l2"):
    src = Image.open(f"{DIR}/zoom/{nm}.png").convert("L")
    a = np.array(src)
    for thr in (140, 170, 200):
        b = np.where(a < thr, 0, 255).astype(np.uint8)
        out = f"{DIR}/zoom/{nm}-bw{thr}.png"
        Image.fromarray(b).save(out)
        ocr_save(out, f"{nm}-bw{thr}", psms=(7,))

# 3) nouveau crop du mot après ساعة (ligne entière y1170-1400)
crop_pdf("z6-p102-saa-line", 102, 1170, 1400, 3600, color=False)
ocr_save(f"{DIR}/zoom/z6-p102-saa-line.png", "z6-p102-saa-line")

# 4) crop gris 3600 du mot X تسويف (début de ligne) pour tesseract net
crop_pdf("z6-p103-manas-w2", 103, 4620, 4720, 3600, color=False)
ocr_save(f"{DIR}/zoom/z6-p103-manas-w2.png", "z6-p103-manas-w2")

# 5) demi-page basse p.104 : layout (600 dpi couleur)
crop_pdf("z6-p104-layout", 104, 2600, 6120, 600, color=True)
print("OK zoom6-h6-18")

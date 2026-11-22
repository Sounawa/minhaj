#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# IA-2 — zoom15-h6-16 : cartouche L13 (p.76) — même traitement couche bleue
# @1200 + extraction zone numéro + OCR, pour trianguler la numérotation.
import subprocess, os
import numpy as np
from PIL import Image

PDF = "/home/z/my-project/minhaj/content/textbooks-src/hadith-6ep.pdf"
DIR = "/home/z/my-project/pdf-work/h6-15"
TESSDATA = "/home/z/my-project/pdf-work/tessdata"
env = dict(os.environ, TESSDATA_PREFIX=TESSDATA)

def crop_pdf(name, page, y0, y1, dpi, color=False, fx0=0.0, fx1=1.0):
    out = f"{DIR}/zoom/{name}"
    if not os.path.exists(out + ".png"):
        f = dpi / 600.0
        W, H = int(5308 * f) + 40, int(6725 * f) + 40
        X0, X1 = int(W * fx0), int(W * fx1)
        Y0, Y1 = int(y0 * f), int(y1 * f)
        args = ["pdftoppm", "-f", str(page), "-l", str(page), "-r", str(dpi),
                "-png", "-singlefile",
                "-x", str(X0), "-y", str(Y0), "-W", str(X1 - X0), "-H", str(Y1 - Y0),
                PDF, out]
        if not color:
            args.insert(-2, "-gray")
        subprocess.run(args, check=True)
    return out + ".png"

def ocr(png, psm):
    r = subprocess.run(["tesseract", png, "stdout", "-l", "ara", "--psm", str(psm)],
                       env=env, capture_output=True, text=True)
    return r.stdout

# couche bleue p.76 (même gabarit que pp.85/90)
col = Image.open(crop_pdf("z15-p76-cartcol", 76, 450, 1050, 1200, color=True)).convert("RGB")
a = np.array(col)
R, G, B = a[..., 0].astype(int), a[..., 1].astype(int), a[..., 2].astype(int)
mask = (R > 160) & (G > 150)
Image.fromarray(np.where(mask, 0, 255).astype(np.uint8)).save(f"{DIR}/zoom/z15-p76-cart-bleu.png")
for psm in (11, 7, 6):
    with open(f"{DIR}/zoom/z15-p76-cart-bleu-psm{psm}.txt", "w") as fh:
        fh.write(ocr(f"{DIR}/zoom/z15-p76-cart-bleu.png", psm))
# zone numéro sous الدرس (même BOX que zoom9)
BOX = (8150, 790, 9150, 1200)
img = Image.open(f"{DIR}/zoom/z15-p76-cart-bleu.png").convert("L").crop(BOX)
img.save(f"{DIR}/zoom/z15-p76-num.png")
sub = img.crop((380, 0, 720, 410))
sub.save(f"{DIR}/zoom/z15-p76-digits.png")
for psm in (7, 8, 10, 13):
    print("digits psm%d: %r" % (psm, ocr(f"{DIR}/zoom/z15-p76-digits.png", psm).strip()))
print("OK zoom15")

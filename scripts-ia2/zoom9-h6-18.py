#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# IA-2 — zoom9-h6-18 : micro-crops PIL ultimes (mots contestés) + binarisation item4.
import subprocess, os
import numpy as np
from PIL import Image

PDF = "/home/z/my-project/pdf-work/hadith-6ep.pdf"
DIR = "/home/z/my-project/pdf-work/h6-15"
TESSDATA = "/home/z/my-project/pdf-work/tessdata"
env = dict(os.environ, TESSDATA_PREFIX=TESSDATA)
Z = f"{DIR}/zoom"

def seg(src, out, fx0, fx1, fy0=0.0, fy1=1.0):
    im = Image.open(f"{Z}/{src}.png")
    W, H = im.size
    im.crop((int(W * fx0), int(H * fy0), int(W * fx1), int(H * fy1))).save(f"{Z}/{out}.png")
    print(f"{out}: OK")

def ocr_save(png, name, psms=(7,)):
    for psm in psms:
        r = subprocess.run(["tesseract", png, "stdout", "-l", "ara", "--psm", str(psm)],
                           env=env, capture_output=True, text=True)
        with open(f"{Z}/{name}-psm{psm}.txt", "w") as fh:
            fh.write(r.stdout)
    print(f"{name}: OCR OK")

def crop_pdf(name, page, y0, y1, dpi, color=True):
    out = f"{Z}/{name}"
    if not os.path.exists(out + ".png"):
        f = dpi / 600.0
        W, H = int(5308 * f) + 40, int(6725 * f) + 40
        Y0, Y1 = int(y0 * f), int(y1 * f)
        args = ["pdftoppm", "-f", str(page), "-l", str(page), "-r", str(dpi),
                "-png", "-singlefile", "-x", str(0), "-y", str(Y0), "-W", str(W), "-H", str(Y1 - Y0),
                PDF, out]
        if not color:
            args.insert(-2, "-gray")
        subprocess.run(args, check=True)
    return out + ".png"

# 1) item4 : le mot exact entre «بأن» et «بما» — x 30-55% de la ligne 3600
seg("z5-p102-item4-l1", "z9-item4-word", 0.30, 0.56)
# binarisation du même mot
src = Image.open(f"{Z}/z9-item4-word.png").convert("L")
a = np.array(src)
for thr in (140, 175):
    b = np.where(a < thr, 0, 255).astype(np.uint8)
    Image.fromarray(b).save(f"{Z}/z9-item4-word-bw{thr}.png")
ocr_save(f"{Z}/z9-item4-word-bw175.png", "z9-item4-word-bw175", psms=(7, 6))

# 2) manas : mots 2-3 après التسويف (x 40-85% du segment droit)
seg("z8-manas-seg", "z9-manas-w23", 0.30, 0.88)

# 3) آية : le segment [الطور: N] (droite de aya-l3)
seg("z5-p104-aya-l3", "z9-aya-ref", 0.35, 0.95)
# et la fin de l'آية (gauche de aya-l2) pour coller la fin du verset
seg("z5-p104-aya-l2", "z9-aya2-end", 0.0, 0.45)

# 4) gloses 2-3 : bande y2160-2340 @3600
crop_pdf("z9-p101-glose23b", 101, 2160, 2340, 3600)
ocr_save(f"{Z}/z9-p101-glose23b.png", "z9-p101-glose23b", psms=(7, 6))

# 5) tableau : rangée d'en-têtes (y2760-2990) @2400 + rangée 1 (y2790-2970) @3600
crop_pdf("z9-p104-table-hdr", 104, 2760, 3000, 2400)
crop_pdf("z9-p104-table-r1", 104, 2780, 2975, 3600)
ocr_save(f"{Z}/z9-p104-table-r1.png", "z9-p104-table-r1", psms=(7, 6))

# 6) ragabba : tesseract sur le crop existant + bande
ocr_save(f"{Z}/z8-p101-ragabba4.png", "z8-p101-ragabba4", psms=(7, 6))
print("OK zoom9-h6-18")

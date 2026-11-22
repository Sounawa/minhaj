#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# IA-2 — zoom14-h6-16 : trois bandes d'UNE ligne @3600 (psm 7/13) pour fixer
# l'ordre physique : heading ثانيا / ligne مما / item 1 (p.92 y1580-2250).
import subprocess, os
from PIL import Image, ImageOps

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

for i, (y0, y1) in enumerate([(1560, 1790), (1770, 2000), (1980, 2210), (2190, 2430)], 1):
    png = crop_pdf(f"z14-p92-line{i}", 92, y0, y1, 3600)
    g = ImageOps.autocontrast(Image.open(png).convert("L"))
    bw = f"{png[:-4]}-bw150.png"
    g.point(lambda v: 0 if v < 150 else 255).save(bw)
    for src in (png, bw):
        tag = src[len(DIR) + 6:-4]
        for psm in (7, 13, 6):
            with open(f"{DIR}/zoom/{tag}-psm{psm}.txt", "w") as fh:
                fh.write(ocr(src, psm))
    print(f"line{i} (y{y0}-{y1}) OK")
print("OK zoom14-h6-16")

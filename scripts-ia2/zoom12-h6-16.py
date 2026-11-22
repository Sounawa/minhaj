#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# IA-2 — zoom12-h6-16 : derniers crops pour اثنين (fin de ligne p.92) et
# أسباب (fin de ligne p.93) — fenêtres élargies + OCR multi-psm.
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

def run(name, page, y0, y1, fx0, fx1):
    png = crop_pdf(name, page, y0, y1, 3600, fx0=fx0, fx1=fx1)
    g = ImageOps.autocontrast(Image.open(png).convert("L"))
    for t in (150,):
        bw = f"{png[:-4]}-bw{t}.png"
        g.point(lambda v: 0 if v < t else 255).save(bw)
    for src in (png, f"{png[:-4]}-bw150.png"):
        tag = src[len(DIR) + 6:-4]
        for psm in (6, 7, 13):
            with open(f"{DIR}/zoom/{tag}-psm{psm}.txt", "w") as fh:
                fh.write(ocr(src, psm))
    print(f"{name}: OK")

# 1) zone «لا حسد إلا في ___» — fin de ligne, fenêtre élargie
run("z12-p92-ithnW", 92, 4420, 4700, 0.00, 0.48)
# 2) zone «الأخذ بكل ___» — fin de ligne, fenêtre élargie et abaissée
run("z12-p93-asbabW", 93, 3900, 4140, 0.00, 0.42)
print("OK zoom12-h6-16")

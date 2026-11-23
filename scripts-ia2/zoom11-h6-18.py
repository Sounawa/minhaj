#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# IA-2 — zoom11-h6-18 : 3 derniers micro-crops.
import subprocess, os
from PIL import Image

PDF = "/home/z/my-project/pdf-work/hadith-6ep.pdf"
DIR = "/home/z/my-project/pdf-work/h6-15"
Z = f"{DIR}/zoom"

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

# 1) manas ligne 2 : les 3-4 premiers mots = x 78-100% du crop z5 (3600)
im = Image.open(f"{Z}/z5-p103-manas-w.png")
W, H = im.size
im.crop((int(W * 0.76), 0, W, H)).save(f"{Z}/z11-manas-first.png")
print("z11-manas-first: OK")

# 2) glose 4 (وغشيتهم: ...) @3600
crop_pdf("z11-p101-glose4", 101, 2640, 2900, 3600)

# 3) tableau en-têtes : y2500-2840 @2400 couleur
crop_pdf("z11-p104-table-hdr2", 104, 2500, 2840, 2400)
print("OK zoom11-h6-18")

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# IA-2 — zoom7-h6-16 : bandes étroites 3600 dpi (re-localisation des lignes
# litigieuses avant la passe VLM 2) — p.92 zone جاء النهي + منها, p.93 zones
# البيع + أسباب, p.92 zone اثنين/آتاه, p.85 cartouche L15 (comparaison numéro).
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

# bandes étroites p.93 : définition البيع (y1900-2520) en 4 bandes de 200 px
for i, (y0, y1) in enumerate([(1900, 2120), (2060, 2280), (2220, 2440), (2380, 2600)], 1):
    png = crop_pdf(f"z7-p93-baystrip{i}", 93, y0, y1, 3600)
    with open(f"{DIR}/zoom/z7-p93-baystrip{i}-psm6.txt", "w") as fh:
        fh.write(ocr(png, 6))
    print(f"baystrip{i}: {os.path.getsize(f'{DIR}/zoom/z7-p93-baystrip{i}-psm6.txt')} o")

# p.93 : zone أسباب (y3800-4380) en 3 bandes
for i, (y0, y1) in enumerate([(3800, 4020), (3960, 4180), (4120, 4380)], 1):
    png = crop_pdf(f"z7-p93-sbstrip{i}", 93, y0, y1, 3600)
    with open(f"{DIR}/zoom/z7-p93-sbstrip{i}-psm6.txt", "w") as fh:
        fh.write(ocr(png, 6))
    print(f"sbstrip{i}: {os.path.getsize(f'{DIR}/zoom/z7-p93-sbstrip{i}-psm6.txt')} o")

# p.92 : ligne جاء النهي + منها (y3260-3680) en 3 bandes
for i, (y0, y1) in enumerate([(3260, 3480), (3420, 3640), (3600, 3820)], 1):
    png = crop_pdf(f"z7-p92-jaastrip{i}", 92, y0, y1, 3600)
    with open(f"{DIR}/zoom/z7-p92-jaastrip{i}-psm6.txt", "w") as fh:
        fh.write(ocr(png, 6))
    print(f"jaastrip{i}: {os.path.getsize(f'{DIR}/zoom/z7-p92-jaastrip{i}-psm6.txt')} o")

# p.92 : zone اثنين/آتاه (y4420-4920) en 4 bandes
for i, (y0, y1) in enumerate([(4420, 4640), (4580, 4800), (4740, 4960), (4900, 5120)], 1):
    png = crop_pdf(f"z7-p92-ghstrip{i}", 92, y0, y1, 3600)
    with open(f"{DIR}/zoom/z7-p92-ghstrip{i}-psm6.txt", "w") as fh:
        fh.write(ocr(png, 6))
    print(f"ghstrip{i}: {os.path.getsize(f'{DIR}/zoom/z7-p92-ghstrip{i}-psm6.txt')} o")

# cartouche L15 (p.85) : couche bleue pour comparaison du numéro avec L16
col = Image.open(crop_pdf("z7-p85-cartcol", 85, 450, 1050, 1200, color=True)).convert("RGB")
a = np.array(col)
R, G, B = a[..., 0].astype(int), a[..., 1].astype(int), a[..., 2].astype(int)
mask = (R > 160) & (G > 150)
Image.fromarray(np.where(mask, 0, 255).astype(np.uint8)).save(f"{DIR}/zoom/z7-p85-cart-bleu.png")
for psm in (11, 7, 6):
    with open(f"{DIR}/zoom/z7-p85-cart-bleu-psm{psm}.txt", "w") as fh:
        fh.write(ocr(f"{DIR}/zoom/z7-p85-cart-bleu.png", psm))
print("cartouche L15 OK")
print("OK zoom7-h6-16")

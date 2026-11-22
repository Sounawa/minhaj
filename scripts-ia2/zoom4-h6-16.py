#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# IA-2 — zoom4-h6-16 : derniers microcrops 3600 dpi — mots litigieux L16.
# Balayage séquentiel du bloc versets p.94 (cadre orné), gloses p.91,
# et mots isolés p.92-94 + zone numéro du cartouche p.90.
import subprocess, os
import numpy as np
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

def run(name, page, y0, y1, fx0=0.0, fx1=1.0, dpi=3600, psms=(6,), color=False, binar=False):
    png = crop_pdf(name, page, y0, y1, dpi, color=color, fx0=fx0, fx1=fx1)
    outs = [png]
    if binar:
        g = ImageOps.autocontrast(Image.open(png).convert("L"))
        for t in (140, 170):
            bw = f"{png[:-4]}-bw{t}.png"
            g.point(lambda v, th=t: 0 if v < th else 255).save(bw)
            outs.append(bw)
    for src in outs:
        tag = src[len(DIR) + 6:-4]
        for psm in psms:
            with open(f"{DIR}/zoom/{tag}-psm{psm}.txt", "w") as fh:
                fh.write(ocr(src, psm))
    print(f"{name}: OK")

# --- A. bloc versets p.94 : balayage séquentiel 3600 (bandes de 300 px) ---
ys = [(1000, 1300), (1250, 1550), (1500, 1800), (1750, 2050),
      (2000, 2300), (2250, 2550), (2500, 2760)]
for i, (y0, y1) in enumerate(ys, 1):
    run(f"z4-p94-vband{i}", 94, y0, y1, psms=(6,), binar=True)

# --- B. gloses p.91 : balayage 1300-2000 ---
for i, (y0, y1) in enumerate([(1300, 1600), (1550, 1850), (1800, 2050)], 1):
    run(f"z4-p91-gloseband{i}", 91, y0, y1, psms=(6, 7))

# --- C. mots isolés ---
run("z4-p92-nush2",    92, 2600, 2830, fx0=0.12, fx1=0.70, psms=(6, 7))
run("z4-p92-jaa2",     92, 3140, 3410, fx0=0.30, fx1=1.00, psms=(6, 7))
run("z4-p92-talaf2",   92, 2960, 3170, fx0=0.00, fx1=0.40, psms=(6, 7), binar=True)
run("z4-p92-ithn2",    92, 4260, 4470, fx0=0.00, fx1=0.45, psms=(6, 7))
run("z4-p92-atah2",    92, 4320, 4560, fx0=0.55, fx1=1.00, psms=(6, 7))
run("z4-p93-tasawum2", 93, 2050, 2270, fx0=0.00, fx1=0.65, psms=(6, 7))
run("z4-p93-asbab",    93, 3850, 4140, fx0=0.00, fx1=0.50, psms=(6, 7))
run("z4-p94-idadq2b",  94, 4550, 5000, psms=(6, 7), binar=True)

# --- D. cartouche p.90 : numéro — zone droite @2400 couleur + couche bleue ---
png = crop_pdf("z4-p90-carnum", 90, 480, 1020, 2400, color=True, fx0=0.40, fx1=0.98)
a = np.array(Image.open(png).convert("RGB"))
R, G, B = a[..., 0].astype(int), a[..., 1].astype(int), a[..., 2].astype(int)
mask = (R > 160) & (G > 150)
Image.fromarray(np.where(mask, 0, 255).astype(np.uint8)).save(f"{DIR}/zoom/z4-p90-carnum-bleu.png")
for psm in (7, 11, 6):
    with open(f"{DIR}/zoom/z4-p90-carnum-bleu-psm{psm}.txt", "w") as fh:
        fh.write(ocr(f"{DIR}/zoom/z4-p90-carnum-bleu.png", psm))
lum = (R + G + B) // 3
Image.fromarray(np.where(lum > 175, 0, 255).astype(np.uint8)).save(f"{DIR}/zoom/z4-p90-carnum-lum.png")
for psm in (7, 11):
    with open(f"{DIR}/zoom/z4-p90-carnum-lum-psm{psm}.txt", "w") as fh:
        fh.write(ocr(f"{DIR}/zoom/z4-p90-carnum-lum.png", psm))
print("cartouche numéro OK")
print("OK zoom4-h6-16")

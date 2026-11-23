#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# IA-2 — zoom1-h6-17 : couverture complète pp.95-99 de L17 «الأخوة الإسلامية» (تتمة)
# en bandes demi-page 1200 dpi + OCR psm 6, + cartouche p.95 en couleur @1200
# (texte blanc sur fond bleu — méthode L14/L15/L16 : la couche couleur aide tesseract).
import subprocess, os

PDF = "/home/z/my-project/minhaj/content/textbooks-src/hadith-6ep.pdf"
DIR = "/home/z/my-project/pdf-work/h6-15"
TESSDATA = "/home/z/my-project/pdf-work/tessdata"
env = dict(os.environ, TESSDATA_PREFIX=TESSDATA)
os.makedirs(f"{DIR}/zoom", exist_ok=True)

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

# Bandes demi-page (chevauchement 120 px en coordonnées 600 dpi) — pp.95-99
for p in range(95, 100):
    for i, (y0, y1) in enumerate([(280, 3520), (3400, 6620)]):
        name = f"z17-p{p:02d}-b{i+1}"
        png = crop_pdf(name, p, y0, y1, 1200)
        with open(f"{DIR}/zoom/{name}-psm6.txt", "w") as fh:
            fh.write(ocr(png, 6))
        print(f"{name}: {os.path.getsize(png)//1024} Ko, psm6 {os.path.getsize(f'{DIR}/zoom/{name}-psm6.txt')} o")

# Cartouche p.95 en couleur @1200 (y 450-1050, pleine largeur) + variantes seuil
png = crop_pdf("z17-p95-cartouche-col", 95, 450, 1050, 1200, color=True)
with open(f"{DIR}/zoom/z17-p95-cartouche-col-psm6.txt", "w") as fh:
    fh.write(ocr(png, 6))
print("cartouche couleur p.95 :", os.path.getsize(png) // 1024, "Ko")
print("OK zoom1-h6-17")

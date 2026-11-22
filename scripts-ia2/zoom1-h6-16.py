#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# IA-2 — zoom1-h6-16 : couverture complète pp.90-94 de L16 «الأخوة الإسلامية» (1re partie)
# en bandes demi-page 1200 dpi + OCR psm 6, + cartouche p.90 en couleur @1200
# (texte blanc sur fond bleu — méthode L14/L15 : la couche couleur aide tesseract).
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

# Bandes demi-page (chevauchement 120 px en coordonnées 600 dpi) — pp.90-94
PAGES = {90: "t90", 91: "t091", 92: "t092", 93: "t093", 94: "t094"}
for p in range(90, 95):
    for i, (y0, y1) in enumerate([(280, 3520), (3400, 6620)]):
        name = f"z16-p{p:02d}-b{i+1}"
        png = crop_pdf(name, p, y0, y1, 1200)
        with open(f"{DIR}/zoom/{name}-psm6.txt", "w") as fh:
            fh.write(ocr(png, 6))
        print(f"{name}: {os.path.getsize(png)//1024} Ko, psm6 {os.path.getsize(f'{DIR}/zoom/{name}-psm6.txt')} o")

# Cartouche p.90 en couleur @1200 (y 450-1050, pleine largeur)
png = crop_pdf("z16-p90-cartouche-col", 90, 450, 1050, 1200, color=True)
with open(f"{DIR}/zoom/z16-p90-cartouche-col-psm6.txt", "w") as fh:
    fh.write(ocr(png, 6))
print("cartouche couleur p.90 :", os.path.getsize(png) // 1024, "Ko")

# Bandes p.94 (استثمار/إعداد) : la moitié basse est clairsemée → bande fine
# p.95 déjà rendue (t095) — pas de crop nécessaire (L17).
print("OK zoom1-h6-16")

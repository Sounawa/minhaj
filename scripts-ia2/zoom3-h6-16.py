#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# IA-2 — zoom3-h6-16 : microcrops 3600 dpi (mots litigieux) + zones colorées
# binarisées (التباغض p.93, التقويم Q2/Q3 p.93, bloc versets p.94, إعداد Q2 p.94).
import subprocess, os
import numpy as np
from PIL import Image, ImageOps

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

def ocr_save(png, name, psms=(6,)):
    for psm in psms:
        with open(f"{DIR}/zoom/{name}-psm{psm}.txt", "w") as fh:
            fh.write(ocr(png, psm))
    print(f"{name}: OK")

# ---------- A. microcrops gris 3600 ----------
MICRO = [
    ("z3-p91-versA",      91, 4500, 4780, 1.00, 0.00),  # cadre haut + début verset
    ("z3-p91-versB",      91, 4700, 5020, 1.00, 0.00),  # verset + référence
    ("z3-p91-najsh-verb", 91, 1510, 1730, 0.90, 0.10),  # glose تناجشوا : verbe après أي لا
    ("z3-p92-nush",       92, 2520, 2730, 0.60, 0.20),  # mot après وإجابة الدعوة
    ("z3-p92-jaa",        92, 3140, 3390, 0.78, 0.10),  # جاء النهي ... بأمور/عن أمور
    ("z3-p92-talaf",      92, 2930, 3100, 0.40, 0.00),  # ويذهب بالأخوة والتالف/التآلف
    ("z3-p92-ghibta1",    92, 4170, 4380, 1.00, 0.00),  # وأما الحسد بمعنى الغبطة ...
    ("z3-p92-ithnatayn",  92, 4180, 4390, 0.34, 0.00),  # في اثنتين :
    ("z3-p92-atah1",      92, 4320, 4520, 0.98, 0.66),  # رجل آتاه/آناه الله مالا
    ("z3-p93-tasawum",    93, 1920, 2140, 0.55, 0.00),  # حال تساوم المتبايعين
    ("z3-p93-umma",       93, 3820, 4120, 0.74, 0.24),  # بوحدة الأمة
    ("z3-p94-idadq2",     94, 4060, 4420, 1.00, 0.00),  # أشرح: ولا يخذله - ... هاهنا
]
for name, page, y0, y1, fx1, fx0 in MICRO:
    png = crop_pdf(name, page, y0, y1, 3600, fx0=fx0, fx1=fx1)
    ocr_save(png, name, psms=(6, 7))

# ---------- B. zones colorées : rendu couleur 1200 + binarisation PIL ----------
def binarize_variants(png_in, base, thresholds=(120, 160, 190)):
    img = Image.open(png_in).convert("RGB")
    g = img.convert("L")
    g = ImageOps.autocontrast(g)
    for t in thresholds:
        bw = g.point(lambda v, th=t: 0 if v < th else 255)
        out = f"{DIR}/zoom/{base}-bw{t}.png"
        bw.save(out)
        with open(f"{DIR}/zoom/{base}-bw{t}-psm6.txt", "w") as fh:
            fh.write(ocr(out, 6))
    print(f"{base}: binarisation ×{len(thresholds)}")

ZONES = [
    ("z3-p93-tabaghd-col", 93, 240, 1000),
    ("z3-p93-taqwim-col",  93, 4120, 5700),
    ("z3-p94-verses-col",  94, 980, 2720),
    ("z3-p94-idad-col",    94, 4000, 4500),
]
for base, page, y0, y1 in ZONES:
    png = crop_pdf(base, page, y0, y1, 1200, color=True)
    binarize_variants(png, base)

# ---------- C. cartouche : moitiés gauche/droite, psm 7/11 ----------
cart = Image.open(f"{DIR}/zoom/z2-p90-cartouche-lum.png")
w, h = cart.size
for half, box in [("R", (w // 2, 0, w, h)), ("L", (0, 0, w // 2, h))]:
    out = f"{DIR}/zoom/z3-p90-cart-{half}.png"
    cart.crop(box).save(out)
    for psm in (7, 11, 6):
        with open(f"{DIR}/zoom/z3-p90-cart-{half}-psm{psm}.txt", "w") as fh:
            fh.write(ocr(out, psm))
print("cartouche moitiés OK")
print("OK zoom3-h6-16")

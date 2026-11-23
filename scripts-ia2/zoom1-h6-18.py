#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# IA-2 — zoom1-h6-18 : zooms section 1200 dpi (gris) + OCR psm6/psm4 pp.100-104
# de L18 «من الأعمال الفاضلة وثوابها» — positions tirées du profil d'encre
# ink-h6-18.py. PDF source = copie de survie pdf-work/hadith-6ep.pdf.
import subprocess, os

PDF = "/home/z/my-project/pdf-work/hadith-6ep.pdf"
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

# (nom, page, y0, y1, dpi)
ZOOMS = [
    # ---- p.100 : تمهيد + matn Muslim 2699 ----
    ("z1-p100-tamhid",   100, 2150, 2960, 1200),  # تمهيد 2 lignes + question
    ("z1-p100-matn-a",   100, 2800, 3800, 1200),  # sanad + 3 lignes matn
    ("z1-p100-matn-b",   100, 3700, 4800, 1200),
    ("z1-p100-matn-c",   100, 4600, 6050, 1200),  # fin matn + [رواه مسلم بهذا اللفظ]
    # ---- p.101 : zones basses mystère + item 1 ----
    ("z1-p101-gloses",   101, 1850, 2360, 1200),  # الشرح gloses
    ("z1-p101-item1",    101, 3400, 6100, 1200),  # item 1 + bandes inconnues y4664-6022
    # ---- p.102 : item 2 + آية + Bukhari + items 3-4 + ثانيا ----
    ("z1-p102-item2",    102,  650, 1420, 1200),
    ("z1-p102-items34",  102, 2300, 3350, 1200),
    ("z1-p102-thani",    102, 3320, 4170, 1200),
    ("z1-p102-sayilm",   102, 4130, 5150, 1200),
    # ---- p.103 : ثالثا + 4 items + معنى قوله + مما يستفاد ----
    ("z1-p103-thalith",  103,  650, 1650, 1200),
    ("z1-p103-items",    103, 1520, 2620, 1200),
    ("z1-p103-manas",    103, 2700, 3620, 1200),
    ("z1-p103-yustafad", 103, 4350, 6050, 1200),
    # ---- p.104 : مما يستفاد fin + تقويم + جدول + استثمار + إعداد ----
    ("z1-p104-yustafad", 104,  650, 1250, 1200),
    ("z1-p104-taqwim",   104, 1550, 2420, 1200),
    ("z1-p104-table",    104, 2750, 3330, 1200),
    ("z1-p104-istithmar",104, 3330, 3760, 1200),
    ("z1-p104-aya",      104, 4300, 5160, 1200),
    ("z1-p104-idad",     104, 5600, 6120, 1200),
]

for name, page, y0, y1, dpi in ZOOMS:
    png = crop_pdf(name, page, y0, y1, dpi)
    ocr_save(png, name, psms=(6, 4))
print("OK zoom1-h6-18")

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# IA-2 — zoom4-h6-15 : derniers recadrages ciblés pour VLM + tesseract 3600 :
# cartouche p.81 (couleur), item 2 «إن الله فرض» zone complète, mot الشرك @3600,
# الحديث الثاني lignes 2-3, chiffres المستدرك @3600, Q3 @2400 contraste,
# tableaux p.82-83 (couleur, pour VLM).
import subprocess, os
from PIL import Image, ImageOps, ImageEnhance

PDF = "/home/z/my-project/minhaj/content/textbooks-src/hadith-6ep.pdf"
DIR = "/home/z/my-project/pdf-work/h6-15"
TESSDATA = "/home/z/my-project/pdf-work/tessdata"
env = dict(os.environ, TESSDATA_PREFIX=TESSDATA)
os.makedirs(f"{DIR}/micro", exist_ok=True)

def crop_pdf(name, page, y0, y1, dpi, color=False, fx0=0.0, fx1=1.0):
    out = f"{DIR}/micro/{name}"
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

# 1. cartouche p.81 en couleur @1200 (y500-1300)
p1 = crop_pdf("m081-cartouche-col", 81, 500, 1300, 1200, color=True)
# 2. item 2 complet (y3380-3940) @1200
p2 = crop_pdf("m081-inallah-zone", 81, 3380, 3940, 1200)
# 3. mot الشرك @3600 (x 0.15-0.75 de la ligne y940-1120)
p3 = crop_pdf("m082-shirk-3600", 82, 940, 1125, 3600, fx0=0.12, fx1=0.78)
# 4. الحديث الثاني lignes 2-3 @2400
p4 = crop_pdf("m082-hadith2-l23", 82, 1680, 2120, 2400)
# 5. chiffres رقم @3600 fin de ligne gauche
p5 = crop_pdf("m082-raqm-3600", 82, 2930, 3095, 3600, fx0=0.0, fx1=0.35)
# 6. Q3 avec contraste @2400
p6 = crop_pdf("m082-q3-raw", 82, 3940, 4100, 2400)
img = Image.open(p6).convert("L")
img = ImageOps.autocontrast(img)
img = ImageEnhance.Contrast(img).enhance(2.0)
p6b = f"{DIR}/micro/m082-q3-contrast.png"
img.save(p6b)
# 7. Q5 tableau couleur @1200
p7 = crop_pdf("m082-q5table-col", 82, 4830, 5460, 1200, color=True)
# 8. p.83 tableau 1 complet couleur @1200
p8 = crop_pdf("m083-table1-col", 83, 1150, 3050, 1200, color=True)
# 9. p.83 tableau 2 entête couleur @1200
p9 = crop_pdf("m083-table2head-col", 83, 3330, 3920, 1200, color=True)
# 10. p.83 item 1 @3600 (الدروس vs الدرس)
p10 = crop_pdf("m083-item1-3600", 83, 1050, 1270, 3600)
# 11. p.83 item 2 @3600 (تضمّنت)
p11 = crop_pdf("m083-item2-3600", 83, 2900, 3170, 3600)

for name in ("m081-inallah-zone", "m082-shirk-3600", "m082-hadith2-l23",
             "m082-raqm-3600", "m082-q3-contrast", "m083-item1-3600", "m083-item2-3600"):
    path = f"{DIR}/micro/{name}.png"
    for psm in (7, 6, 13):
        r = subprocess.run(["tesseract", path, "stdout", "-l", "ara", "--psm", str(psm)],
                           env=env, capture_output=True, text=True)
        txt = " ".join(r.stdout.split())
        if txt.strip():
            print(f"── {name} psm{psm}: {txt}")
print("crops:", p1, p2, p3, p4, p5, p6b, p7, p8, p9, p10, p11, sep="\n  ")
print("OK zoom4-h6-15")

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# IA-2 — zoom5-h6-16 : re-localisation finale des microcrops (lignes re-situées
# d'après zoom4) — اثنتين/آتاه p.92, تساوم p.93, التالف + تتنافى + أسباب p.92-93,
# réf. الحجرات p.94 + départ de ligne «ولذلك جاء النهي».
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

def run(name, page, y0, y1, fx0=0.0, fx1=1.0, dpi=3600, psms=(6, 7), binar=False):
    png = crop_pdf(name, page, y0, y1, dpi, fx0=fx0, fx1=fx1)
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

# p.92 — paragraphe الغبطة (lignes re-situées) :
run("z5-p92-ithn3",   92, 4440, 4630, fx0=0.00, fx1=0.36)   # «في اثنتين:» fin de ligne
run("z5-p92-atah3",   92, 4580, 4770, fx0=0.55, fx1=1.00)   # «رجل آتاه الله مالا فسلطه»
run("z5-p92-atah4",   92, 4580, 4770, fx0=0.22, fx1=0.60)   # «ورجل آته الله الحكمة»
# p.93 — البيع sur vente : bande complète de la ligne de définition :
run("z5-p93-tasawum3", 93, 2130, 2380, fx0=0.00, fx1=0.72, binar=True)
# p.92 — mot litigieux التالف/التآلف (fin de ligne 1 de l'item 2) :
run("z5-p92-talaf3",  92, 2960, 3150, fx0=0.00, fx1=0.30, binar=True)
# p.92 — mot تتنافى/تتناقى (ligne «جاء النهي») + début de ligne :
run("z5-p92-tanafi",  92, 3220, 3400, fx0=0.38, fx1=0.80, binar=True)
run("z5-p92-jaa3",    92, 3220, 3400, fx0=0.80, fx1=1.00)
# p.93 — queue de ligne «بكل أسبابها» :
run("z5-p93-asbab2",  93, 3880, 4100, fx0=0.00, fx1=0.30, binar=True)
# p.94 — référence [الحجرات: …] fin de bloc versets :
run("z5-p94-ref",     94, 2500, 2740, fx0=0.00, fx1=0.42, binar=True)
# p.94 — إعداد Q1 mot تتنافى/تتناقى (re-situé) :
run("z5-p94-tanafi2", 94, 4330, 4560, fx0=0.25, fx1=0.85, binar=True)
print("OK zoom5-h6-16")

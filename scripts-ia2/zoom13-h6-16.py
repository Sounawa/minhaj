#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# IA-2 — zoom13-h6-16 : (a) zone ثانيا + ligne d'intro + item 1 p.92 @3600,
# (b) analyse pixel de la référence [الحجرات: …] p.94 — positions des groupes
# de chiffres (٠ = boucle, ١ = trait vertical) pour lever l'ambiguïté d'ordre.
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

# (a) bande p.92 y1780-2240 pleine largeur
png = crop_pdf("z13-p92-thani", 92, 1780, 2240, 3600)
g = ImageOps.autocontrast(Image.open(png).convert("L"))
bw = f"{png[:-4]}-bw150.png"
g.point(lambda v: 0 if v < 150 else 255).save(bw)
for src in (png, bw):
    tag = src[len(DIR) + 6:-4]
    for psm in (6, 4):
        with open(f"{DIR}/zoom/{tag}-psm{psm}.txt", "w") as fh:
            fh.write(ocr(src, psm))
print("z13-p92-thani OK")

# (b) référence p.94 : localiser les glyphes de chiffres dans z5-p94-ref.png
im = Image.open(f"{DIR}/zoom/z5-p94-ref.png").convert("L")
A = np.array(im)
ink = A < 128
print("taille image ref:", A.shape, "px noirs:", ink.sum())
# profil de colonnes : segments d'encre
colsum = ink.sum(axis=0)
runs, start = [], None
for i, v in enumerate(colsum):
    if v > 2 and start is None:
        start = i
    elif v <= 2 and start is not None:
        if i - start > 8:
            runs.append((start, i - 1))
        start = None
if start is not None:
    runs.append((start, len(colsum) - 1))
print("segments d'encre horizontaux (x):", runs)
# pour chaque segment : hauteur d'encre et « circularité » (٠ = boucle fermée
# ~ ratio encre/périphérie élevé et bas ; ١ = trait vertical haut et étroit)
for x0, x1 in runs:
    sub = ink[:, x0:x1 + 1]
    ys, xs = np.where(sub)
    h = ys.max() - ys.min() + 1 if len(ys) else 0
    w = x1 - x0 + 1
    fill = sub.sum() / (h * w) if h * w else 0
    print(f"segment x[{x0}-{x1}] w={w:3d} h={h:3d} remplissage={fill:.2f} encre={sub.sum()}")

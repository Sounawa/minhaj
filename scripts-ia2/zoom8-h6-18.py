#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# IA-2 — zoom8-h6-18 : segments PIL depuis les rendus 3600 existants + micro-crops pdftoppm
# pour la ronde VLM 4 (dernier kilomètre).
import subprocess, os
from PIL import Image

PDF = "/home/z/my-project/pdf-work/hadith-6ep.pdf"
DIR = "/home/z/my-project/pdf-work/h6-15"
os.makedirs(f"{DIR}/zoom", exist_ok=True)

# ---- A. segments PIL depuis z5 (3600 dpi, pleine largeur 31850px) ----
def seg(src, out, fx0, fx1, y0=0, y1=None):
    im = Image.open(f"{DIR}/zoom/{src}.png")
    W, H = im.size
    im.crop((int(W * fx0), y0, int(W * fx1), y1 or H)).save(f"{DIR}/zoom/{out}.png")
    print(f"{out}: OK")

# item4 : segment mystère = x 28%-58% (depuis la gauche) de la ligne
seg("z5-p102-item4-l1", "z8-item4-seg", 0.28, 0.60)
# item4 : début de ligne (droite) x 75-100%
seg("z5-p102-item4-l1", "z8-item4-start", 0.72, 1.0)
# manas : mot X + suite, début de ligne (droite) x 70-100%
seg("z5-p103-manas-w", "z8-manas-seg", 0.68, 1.0)
# آية l1 : moitié droite puis moitié gauche, empilées
seg("z5-p104-aya-l1", "z8-aya1-right", 0.5, 1.0)
seg("z5-p104-aya-l1", "z8-aya1-left", 0.0, 0.5)
seg("z5-p104-aya-l2", "z8-aya2-right", 0.5, 1.0)
seg("z5-p104-aya-l2", "z8-aya2-left", 0.0, 0.5)
# jabir : mot السماحة fin de ligne yusr l.2 → z5-p102-jabir2 est y2010-2570
# la ligne 1 du crop = «فقد دعا... والسماحة؛» → x 0-35% (fin gauche)
seg("z5-p102-jabir2", "z8-jabir-yusr-end", 0.0, 0.40)

# ---- B. micro-crops pdftoppm ----
def crop_pdf(name, page, y0, y1, dpi, color=True):
    out = f"{DIR}/zoom/{name}"
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

# gloses 2-3 @3600 (bande y2130-2340)
crop_pdf("z8-p101-glose23", 101, 2130, 2345, 3600)
# ligne رغب @2400 (y4890-5140)
crop_pdf("z8-p101-ragabba4", 101, 4890, 5145, 2400)
# tableau complet avec en-têtes @1200 (y2700-3760)
crop_pdf("z8-p104-table3", 104, 2700, 3760, 1200)
# encadré آية complet (2 lignes + ref + question) @1200
crop_pdf("z8-p104-aya-box", 104, 4300, 5160, 1200)
print("OK zoom8-h6-18")

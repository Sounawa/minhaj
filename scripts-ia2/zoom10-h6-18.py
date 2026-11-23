#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# IA-2 — zoom10-h6-18 : derniers crops pour la ronde 6.
import subprocess, os
from PIL import Image

PDF = "/home/z/my-project/pdf-work/hadith-6ep.pdf"
DIR = "/home/z/my-project/pdf-work/h6-15"
Z = f"{DIR}/zoom"

def crop_pdf(name, page, y0, y1, dpi, color=True):
    out = f"{Z}/{name}"
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

def seg(src, out, fx0, fx1):
    im = Image.open(f"{Z}/{src}.png")
    W, H = im.size
    im.crop((int(W * fx0), 0, int(W * fx1), H)).save(f"{Z}/{out}.png")
    print(f"{out}: OK")

# 1) encadré آية complet @2400 couleur
crop_pdf("z10-p104-aya-full", 104, 4330, 4960, 2400)
# 2) référence : droite de la ligne aya-l2 (y4560-4830)
seg("z5-p104-aya-l2", "z10-aya-ref2", 0.50, 1.0)
# 3) jonction manas : fin de ligne 1 (y4390-4622, gauche) + début ligne 2 (droite)
crop_pdf("z10-p103-manas-l1", 103, 4385, 4630, 3600)
seg("z10-p103-manas-l1", "z10-manas-l1end", 0.0, 0.30)
im1 = Image.open(f"{Z}/z10-manas-l1end.png")
im2 = Image.open(f"{Z}/z9-manas-w23.png")
W = max(im1.width, im2.width)
comp = Image.new("RGB", (W, im1.height + im2.height + 10), "white")
comp.paste(im2, ((W - im2.width) // 2, 0))     # haut : début de la ligne 2 (droite→)
comp.paste(im1, ((W - im1.width) // 2, im2.height + 10))  # bas : fin de la ligne 1
comp.save(f"{Z}/z10-manas-junction.png")
print("z10-manas-junction: OK")
# 4) zone gloses/استخلاص p.101 @1200 couleur
crop_pdf("z10-p101-glos-zone", 101, 1860, 2920, 1200)
# 5) tableau : zone complète @1200 couleur
crop_pdf("z10-p104-table-full", 104, 2700, 3420, 1200)
print("OK zoom10-h6-18")

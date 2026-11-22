#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# IA-2 — zoom8-h6-16 : comparaison pixel des NUMÉROS de cartouche L15 (p.85)
# vs L16 (p.90) — même gabarit, couche bleue @1200. Si les deux zones chiffres
# sont identiques → L16 porte «15» (coquille) ; si elles diffèrent → ١٦ mal lu.
import subprocess, os, re
import numpy as np
from PIL import Image

DIR = "/home/z/my-project/pdf-work/h6-15"
TESSDATA = "/home/z/my-project/pdf-work/tessdata"
env = dict(os.environ, TESSDATA_PREFIX=TESSDATA)

def tsv(png):
    r = subprocess.run(["tesseract", png, "stdout", "-l", "ara", "--psm", "11", "tsv"],
                       env=env, capture_output=True, text=True)
    return r.stdout

def words(png):
    out = []
    for line in tsv(png).splitlines()[1:]:
        p = line.split("\t")
        if len(p) == 12 and p[11].strip() and float(p[10]) > 0:
            out.append((p[11], int(p[6]), int(p[7]), int(p[8]), int(p[9]), float(p[10])))
    return out

for tag, png in [("L15", f"{DIR}/zoom/z7-p85-cart-bleu.png"),
                 ("L16", f"{DIR}/zoom/z2-p90-cartouche-bleu.png")]:
    print(f"===== {tag} =====")
    for w in words(png):
        print(w)

# le token chiffré : chercher '15'/'16'/'١٥'/'١٦' et le mot الدرس dans les deux
def find_digit_zone(png):
    W = words(png)
    # zone = sous le mot الدرس (le numéro est imprimé SOUS, à droite du cartouche)
    dars = [w for w in W if "الدرس" in w[0] or "الذر" in w[0] or "الدر" in w[0]]
    digs = [w for w in W if re.fullmatch(r"[0-9٠-٩]{1,3}", w[0])]
    return dars, digs

for tag, png in [("L15", f"{DIR}/zoom/z7-p85-cart-bleu.png"),
                 ("L16", f"{DIR}/zoom/z2-p90-cartouche-bleu.png")]:
    d, g = find_digit_zone(png)
    print(f"{tag}: الدرس→{d}  chiffres→{g}")

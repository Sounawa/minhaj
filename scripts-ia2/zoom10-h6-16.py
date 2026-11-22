#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# IA-2 — zoom10-h6-16 : isolement des glyphes du numéro (zone x400-700) et
# comparaison glyphe par glyphe (profils de colonnes) + OCR ponctuel.
import subprocess, os
import numpy as np
from PIL import Image

DIR = "/home/z/my-project/pdf-work/h6-15/zoom"
TESSDATA = "/home/z/my-project/pdf-work/tessdata"
env = dict(os.environ, TESSDATA_PREFIX=TESSDATA)

BOX = (8150, 790, 9150, 1200)
a = Image.open(f"{DIR}/z7-p85-cart-bleu.png").convert("L").crop(BOX)
b = Image.open(f"{DIR}/z2-p90-cartouche-bleu.png").convert("L").crop(BOX)

# sous-zone chiffres : x 380-720, pleine hauteur
SUB = (380, 0, 720, 410)
A = np.array(a.crop(SUB), dtype=int)
B = np.array(b.crop(SUB), dtype=int)
Image.fromarray(A.astype(np.uint8)).save(f"{DIR}/z10-digits-L15.png")
Image.fromarray(B.astype(np.uint8)).save(f"{DIR}/z10-digits-L16.png")

# profil d'encre par colonne (nb pixels noirs) pour localiser chaque glyphe
def prof(M, tag):
    ink = (M < 128).sum(axis=0)
    runs, start = [], None
    for i, v in enumerate(ink):
        if v > 3 and start is None:
            start = i
        elif v <= 3 and start is not None:
            runs.append((start, i - 1))
            start = None
    if start is not None:
        runs.append((start, len(ink) - 1))
    print(f"{tag}: segments d'encre (x): {runs}")
    return runs

ra = prof(A, "L15")
rb = prof(B, "L16")

# OCR ponctuel de chaque sous-zone chiffres
for tag in ("L15", "L16"):
    png = f"{DIR}/z10-digits-{tag}.png"
    for psm in (7, 8, 10, 13):
        r = subprocess.run(["tesseract", png, "stdout", "-l", "ara", "--psm", str(psm)],
                           env=env, capture_output=True, text=True)
        t = r.stdout.strip()
        if t:
            print(f"{tag} psm{psm}: {t!r}")

# comparaison du PREMIER glyphe (le plus à droite = premier chiffre ١ ?)
# en RTL les chiffres se lisent de gauche à droite dans un nombre arabe :
# ١٥ = ١ à GAUCHE? Non : dans un nombre arabe, le chiffre de poids fort est
# à GAUCHE (comme en Occident) : «١٥» affiche ١ puis ٥ de droite à gauche =
# positions x : ١ plus PETIT x (gauche), ٥ plus GRAND x (droite).
if ra and rb:
    (x0a, x1a) = ra[0]
    (x0b, x1b) = rb[0]
    print(f"\npremier segment : L15 x[{x0a}-{x1a}] largeur {x1a-x0a}, "
          f"L16 x[{x0b}-{x1b}] largeur {x1b-x0b}")
    # compare chaque segment L15 vs L16 s'ils s'alignent
    for (xa0, xa1), (xb0, xb1) in zip(ra, rb):
        wa, wb = xa1 - xa0, xb1 - xb0
        print(f"segment L15 x[{xa0}-{xa1}] (w{wa}) vs L16 x[{xb0}-{xb1}] (w{wb})")

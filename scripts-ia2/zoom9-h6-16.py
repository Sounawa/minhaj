#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# IA-2 — zoom9-h6-16 : comparaison directe de la zone SOUS الدرس (numéro)
# entre cartouches L15 (p.85) et L16 (p.90), couches bleues @1200.
import numpy as np
from PIL import Image, ImageOps

DIR = "/home/z/my-project/pdf-work/h6-15/zoom"

# الدرس est à (x≈8250-9100, y≈500-800) sur les deux images 1200 dpi.
# Zone numéro : sous le mot, x 8150-9150, y 790-1200.
BOX = (8150, 790, 9150, 1200)

a = Image.open(f"{DIR}/z7-p85-cart-bleu.png").convert("L").crop(BOX)
b = Image.open(f"{DIR}/z2-p90-cartouche-bleu.png").convert("L").crop(BOX)
a.save(f"{DIR}/z9-num-L15.png")
b.save(f"{DIR}/z9-num-L16.png")

A = np.array(a, dtype=int)
B = np.array(b, dtype=int)
print("tailles:", A.shape, B.shape)
diff = np.abs(A - B)
print(f"diff moyenne = {diff.mean():.1f}, diff max = {diff.max()}, "
      f"pixels >100 : {(diff > 100).mean() * 100:.1f} %")

# Où sont les encres (pixels noirs) dans chaque zone ?
for tag, M in (("L15", A), ("L16", B)):
    ink = M < 128
    ys, xs = np.where(ink)
    if len(xs):
        print(f"{tag}: encre x[{xs.min()}-{xs.max()}] y[{ys.min()}-{ys.max()}] "
              f"({len(xs)} px noirs)")
    else:
        print(f"{tag}: AUCUNE encre dans la zone")

# diff locale par colonnes de 50 px pour voir si la différence est concentrée
h = A.shape[0]
for x0 in range(0, A.shape[1], 100):
    d = np.abs(A[:, x0:x0 + 100] - B[:, x0:x0 + 100]).mean()
    print(f"x {x0:4d}-{x0+100:4d}: diff {d:6.1f}")

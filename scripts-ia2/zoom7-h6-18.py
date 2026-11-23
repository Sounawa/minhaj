#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# IA-2 — zoom7-h6-18 : composites de tuiles (mots) pour lecture directe + VLM binarisé.
import os
from PIL import Image

DIR = "/home/z/my-project/pdf-work/h6-15/zoom"

def tiles_stacked(src, out, n, sel, pad=60):
    """Découpe src en n tuiles verticales (bandes verticales de la ligne),
    empile les tuiles sélectionnées (indices 0..n-1, droite→gauche) verticalement."""
    im = Image.open(f"{DIR}/{src}.png")
    W, H = im.size
    tw = W // n
    parts = []
    for i in sel:
        x0 = max(0, i * tw - pad)
        x1 = min(W, (i + 1) * tw + pad)
        parts.append(im.crop((x0, 0, x1, H)))
    comp = Image.new("RGB", (max(p.width for p in parts), sum(p.height for p in parts) + 8 * (len(parts) - 1)), "white")
    y = 0
    for p in parts:
        comp.paste(p, (0, y))
        y += p.height + 8
    comp.save(f"{DIR}/{out}.png")
    print(f"{out}: {comp.size}")

# item4 : ligne 31850px @3600 → 8 tuiles ~4000px ; segment mystère ≈ tuiles 3-5 (0 = droite)
tiles_stacked("z5-p102-item4-l1", "z7-item4-comp", 8, (2, 3, 4, 5))
# manas : ligne y4627-4818 ; mot X au DÉBUT (droite) ≈ tuiles 0-2
tiles_stacked("z5-p103-manas-w", "z7-manas-comp", 8, (0, 1, 2, 3))
# آية l1 : 4 tuiles empilées (toute la ligne)
tiles_stacked("z5-p104-aya-l1", "z7-aya1-comp", 4, (0, 1, 2, 3))
# آية l2 : 4 tuiles empilées
tiles_stacked("z5-p104-aya-l2", "z7-aya2-comp", 4, (0, 1, 2, 3))
print("OK zoom7-h6-18")

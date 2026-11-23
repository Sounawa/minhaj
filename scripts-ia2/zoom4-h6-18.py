#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# IA-2 — zoom4-h6-18 : 4 images VLM complémentaires (offsets corrigés).
import subprocess, os

PDF = "/home/z/my-project/pdf-work/hadith-6ep.pdf"
DIR = "/home/z/my-project/pdf-work/h6-15"
os.makedirs(f"{DIR}/zoom", exist_ok=True)

def crop_pdf(name, page, y0, y1, dpi, color=True):
    out = f"{DIR}/zoom/{name}"
    if not os.path.exists(out + ".png"):
        f = dpi / 600.0
        W, H = int(5308 * f) + 40, int(6725 * f) + 40
        X0, X1 = int(W * 0.0), int(W * 1.0)
        Y0, Y1 = int(y0 * f), int(y1 * f)
        args = ["pdftoppm", "-f", str(page), "-l", str(page), "-r", str(dpi),
                "-png", "-singlefile",
                "-x", str(X0), "-y", str(Y0), "-W", str(X1 - X0), "-H", str(Y1 - Y0),
                PDF, out]
        if not color:
            args.insert(-2, "-gray")
        subprocess.run(args, check=True)
    return out + ".png"

VLMS = [
    ("z3-p101-ragabba2-vlm", 101, 5110, 5350, 2400),  # رغب النبي ﷺ في الإكثار من ...
    ("z3-p102-zumar2-vlm",  102, 4620, 4960, 2400),   # آية الزمر + [الزمر: N]
    ("z3-p102-jabir-vlm",   102, 2070, 2320, 2400),   # hadith جابر + ponctuation
    ("z3-p102-yusr-vlm",    102, 1850, 2110, 2400),   # فمن يسر في معاملاته + باليسر والسهولة والسماحة
]
for name, page, y0, y1, dpi in VLMS:
    crop_pdf(name, page, y0, y1, dpi, color=True)
    print(f"{name}: image OK")
print("OK zoom4-h6-18")

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# IA-2 — zoom11-h6-16 : crops VLM2 (derniers mots litigieux) — اثنين p.92,
# zone mystère p.93 y2020-2260, أسباب p.93, ligne جاء النهي p.92, التقوى p.94.
import subprocess, os

PDF = "/home/z/my-project/minhaj/content/textbooks-src/hadith-6ep.pdf"
DIR = "/home/z/my-project/pdf-work/h6-15"

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

crop_pdf("v2-ithn",    92, 4430, 4660, 3600, fx0=0.00, fx1=0.22)  # mot اثنين/اثنتين fin de ligne
crop_pdf("v2-myst",    93, 2010, 2270, 2400)                       # zone entre ref أبو داود et définition البيع
crop_pdf("v2-asbab",   93, 3870, 4050, 3600, fx0=0.00, fx1=0.30)  # mot après بكل
crop_pdf("v2-jaa",     92, 3100, 3350, 2400)                       # ligne جاء النهي complète
crop_pdf("v2-taqwa",   94, 4570, 4810, 3600, fx0=0.20, fx1=0.80)  # groupe entre tirets Q2
crop_pdf("v2-myst",    93, 2010, 2270, 2400)                       # (idempotent)
print("OK zoom11-h6-16")

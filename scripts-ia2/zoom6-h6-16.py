#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# IA-2 — zoom6-h6-16 : préparation des crops pour la passe VLM (dernier recours,
# méthode Z2-50/51 : questions neutres + décomposition lettre par lettre).
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

# cartouche p.90 : réutiliser z16-p90-cartouche-col.png (1200 couleur, y450-1050)
crop_pdf("v-cartouche", 90, 450, 1050, 1200, color=True)
crop_pdf("v-ithn",       92, 4420, 4720, 2400, fx0=0.00, fx1=0.55)
crop_pdf("v-atah",       92, 4560, 4840, 2400, fx0=0.50, fx1=1.00)
crop_pdf("v-tasawum",    93, 2120, 2420, 2400, fx0=0.00, fx1=0.78)
crop_pdf("v-talaf",      92, 2890, 3170, 2400)
crop_pdf("v-jaa",        92, 3280, 3620, 2400)
crop_pdf("v-idad",       94, 4330, 4680, 2400)
crop_pdf("v-asbab",      93, 3840, 4160, 2400, fx0=0.00, fx1=0.62)
crop_pdf("v-taabbir",    92,  480, 1300, 2400)
crop_pdf("v-versA",      94, 1550, 2180, 1200, color=True)
crop_pdf("v-versB",      94, 2100, 2780, 1200, color=True)
print("OK zoom6-h6-16 (crops VLM prêts)")

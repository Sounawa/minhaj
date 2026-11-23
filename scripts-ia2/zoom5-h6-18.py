#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# IA-2 — zoom5-h6-18 : micro-crops 2400/3600 pour la ronde VLM 2 (zones non résolues).
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

CROPS = [
    ("z5-p101-gloses2",  101, 1870, 2360, 2400),   # gloses الشرح (retry)
    ("z5-p101-ragabba3", 101, 5090, 5680, 2400),   # رغب النبي + ومن مظاهر ذلك + item1
    ("z5-p102-item4-l1", 102, 3350, 3580, 3600),   # 4- عون المسلم (ligne entière)
    ("z5-p102-saa-word", 102, 1150, 1290, 3600),   # أو ينظر إلى ساعة X (mot X)
    ("z5-p102-jabir2",   102, 2010, 2570, 2400),   # يسر l.2 + جابر hadith + ponctuation
    ("z5-p103-manas-w",  103, 4610, 4840, 3600),   # X أو تفريطا وتقصيرا (mot X)
    ("z5-p104-table2",   104, 2740, 3260, 2400),   # tableau (détail rangées)
    ("z5-p104-zone",     104, 3240, 4360, 1200),   # layout : استثمار titre + box شخص + آية box
    ("z5-p104-aya-l1",   104, 4330, 4580, 3600),   # آية ligne 1
    ("z5-p104-aya-l2",   104, 4560, 4830, 3600),   # آية ligne 2
    ("z5-p104-aya-l3",   104, 4810, 5140, 3600),   # ref [الطور: N] + كيف أوافق
    ("z5-p100-matn-p",   100, 5560, 6060, 2400),   # السكينة...عنده. ومن بطأ (ponctuation)
]
for name, page, y0, y1, dpi in CROPS:
    crop_pdf(name, page, y0, y1, dpi, color=True)
    print(f"{name}: OK")
print("OK zoom5-h6-18")

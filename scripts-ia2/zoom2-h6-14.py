#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# IA-2 — zoom2-h6-14 : recadrage 1200 dpi des bandes disputées (pdftoppm -x -y
# -W -H directs PDF), variantes de contraste PIL, OCR tesseract psm 6/7.
import subprocess, os, sys
from PIL import Image, ImageOps

PDF = "/home/z/my-project/pdf-work/hadith-6ep.pdf"
OUT = "/home/z/my-project/pdf-work/h6-14/zoom"
TESSDATA = "/home/z/my-project/pdf-work/tessdata"
env = dict(os.environ, TESSDATA_PREFIX=TESSDATA)
os.makedirs(OUT, exist_ok=True)

# (label, page, y0, y1 @600dpi, psm) — largeur pleine (x=300..10300 @1200)
TARGETS = [
    ("A-objectif3-p76",        76, 2260, 2400, 7),
    ("B-questions-p76",        76, 3760, 4900, 6),
    ("C-takhrij-p76",          76, 5620, 5860, 7),
    ("D-sharh-zone-p77",       77, 3250, 4700, 6),
    ("E-tahlil-intro-p77",     77, 5100, 6500, 6),
    ("F-tarjama-gharib-p77",   77, 2020, 2260, 7),
    ("G-tarjama-umar-p77",     77, 2280, 2530, 7),
    ("H-tarjama-walad-p77",    77, 1300, 1560, 7),
    ("I-bayyina-def-p78",      78, 1090, 1660, 6),
    ("J-muddai-def-p78",       78, 1640, 2440, 6),
    ("K-muddaa-alayh-p78",     78, 2440, 3010, 6),
    ("L-mithal-p78",           78, 3230, 4260, 6),
    ("M-mutamassik-p78",       78, 4260, 5060, 6),
    ("N-thaniya-p78",          78, 5140, 6500, 6),
    ("O-yadullu-p79",          79,  950, 1760, 6),
    ("P-yustafad-p79",         79, 2000, 2700, 6),
    ("Q-istithmar-lead-p79",   79, 4600, 5050, 6),
    ("R-ummu-salama-p79",      79, 5280, 5480, 7),
    ("S-taqwim-head-p79",      79, 3076, 3340, 6),
    ("T-kurrasa-p80",          80, 3403, 3660, 7),
]

def ocr(png, psm):
    r = subprocess.run(["tesseract", png, "stdout", "-l", "ara", "--psm", str(psm)],
                       env=env, capture_output=True, text=True)
    return " ".join(r.stdout.split())

for label, page, y0, y1, psm in TARGETS:
    base = f"{OUT}/{label}"
    y2, h2 = 2 * y0, 2 * (y1 - y0)
    if not os.path.exists(base + ".png"):
        subprocess.run(["pdftoppm", "-f", str(page), "-l", str(page), "-r", "1200",
                        "-gray", "-png", "-singlefile",
                        "-x", "300", "-y", str(y2), "-W", "10000", "-H", str(h2),
                        PDF, base], check=True)
    img = Image.open(base + ".png")
    # variantes : gris autocontrasté + binaire
    auto = ImageOps.autocontrast(img, cutoff=1)
    auto.save(base + "-ac.png")
    bw = auto.point(lambda v: 255 if v > 150 else 0)
    bw.save(base + "-bw.png")
    results = []
    for suffix in ("", "-ac", "-bw"):
        t = ocr(base + suffix + ".png", psm)
        if t and t not in [r for r, _ in results]:
            results.append((t, suffix))
    print(f"\n████ {label} (p.{page}, y{y0}-{y1}, psm{psm}) ████")
    for t, s in results[:3]:
        print(f"  [{s or 'brut'}] {t}")

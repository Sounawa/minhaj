#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""R599 — Phase 2bis : compléments de recadrage.
  g1 p.111 0.42-0.50 : matn hadith بسرة (مَنْ مَسَّ ذَكَرَهُ أَيْ/أَوْ… أو رُفعَهُ)
  g2 p.111 0.68-0.85 : hadith التشهد (إذًا كلت هذا أو قضيت هذا… فقم/فاقعد)
  g3 p.112 zoom 3600 dpi : mot « المدرج/المدبج » — التقويم Q1 vs الإعداد Q1/Q2
Chaîne R578+ — zéro vision API, lecture image directe."""
import os
import numpy as np
import fitz
from PIL import Image, ImageDraw

HOME = "/home/z/my-project"
PDF = f"{HOME}/content/textbooks-src/ulum-hadith-1-thanawi.pdf"
OUT = f"{HOME}/tr-tmp/qa-crops-r599"
doc = fitz.open(PDF)

def lines_of(img):
    arr = np.asarray(img.convert("L"))
    dark = (arr < 190).mean(axis=1)
    rows = dark > 0.012
    lines, start = [], None
    for i, r in enumerate(rows):
        if r and start is None:
            start = i
        elif not r and start is not None:
            if i - start >= 14:
                lines.append((start, i))
            start = None
    if start is not None and len(rows) - start >= 14:
        lines.append((start, len(rows)))
    return lines

def compose(name, rows):
    W = 1600
    H = sum(s.height + 34 for _, s in rows) + 10
    comp = Image.new("RGB", (W, H), "white")
    d = ImageDraw.Draw(comp)
    y = 6
    for lab, seg in rows:
        d.text((6, y + 2), lab, fill="red")
        comp.paste(seg, (W - seg.width, y + 24))
        y += seg.height + 34
    comp.save(f"{OUT}/{name}.png")
    print(f"{name}: {len(rows)} segments -> {W}x{H}")

# g1 / g2 — bandes halves
for name, pno, f0, f1 in [("g1-p111-busra-matn", 111, 0.42, 0.50),
                          ("g2-p111-tashahhud", 111, 0.68, 0.85)]:
    page = doc[pno - 1]
    R = page.rect
    clip = fitz.Rect(0, R.height * f0, R.width, R.height * f1)
    pix = page.get_pixmap(dpi=1200, clip=clip)
    band = Image.frombytes("RGB", (pix.width, pix.height), pix.samples)
    rows = []
    for n, (a, b) in enumerate(lines_of(band), 1):
        a2, b2 = max(0, a - 12), min(band.height, b + 12)
        line = band.crop((0, a2, band.width, b2))
        for tag, seg in (("R", line.crop((line.width // 2, 0, line.width, line.height))),
                         ("L", line.crop((0, 0, line.width // 2, line.height)))):
            seg = seg.resize((1550, max(1, int(seg.height * 1550 / seg.width))), Image.LANCZOS)
            rows.append((f"p{pno} L{n}{tag}", seg))
    compose(name, rows)

# g3 — zoom mots 3600 dpi, moitié droite 40 %
p112 = doc[112 - 1]
R = p112.rect
rows = []
ZONES = [("p112-TaqwimQ1", 0.255, 0.295), ("p112-IdadQ1", 0.695, 0.735), ("p112-IdadQ2", 0.730, 0.775)]
for lab, f0, f1 in ZONES:
    clip = fitz.Rect(0, R.height * f0, R.width, R.height * f1)
    pix = p112.get_pixmap(dpi=3600, clip=clip)
    band = Image.frombytes("RGB", (pix.width, pix.height), pix.samples)
    ls = lines_of(band)
    if not ls:
        continue
    a, b = ls[0]
    line = band.crop((0, max(0, a - 20), band.width, min(band.height, b + 20)))
    # fenêtre droite 40 % (mots cibles côté droit, RTL)
    seg = line.crop((int(line.width * 0.60), 0, line.width, line.height))
    seg = seg.resize((1550, max(1, int(seg.height * 1550 / seg.width))), Image.LANCZOS)
    rows.append((f"{lab} right40% 3600dpi", seg))
compose("g3-p112-mudraj-vs-mudabbaaj", rows)
print("R599 phase 2bis terminée")

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""R599 — Phase 2 : recadrages fins (moitiés de ligne, 1200 dpi) de
ulum-hadith-1-thanawi.pdf — leçon 22 (pdf-mut23h2q-133, المدرج, p.108-112).
Points à trancher PAR L'IMAGE (conflits/troncatures OCR psm6/psm4) :
  f1 p.112 0.70-0.78 : الإعداد القبلي Q1/Q2 — المدرج vs المدبج (ب/ر)
  f2 p.108 0.25-0.55 : bayt bannière — ما أتت vs أقت
  f3 p.109 0.28-0.40 : bayt reprise analyse — idem
  f4 p.110 0.02-0.20 : وائل بن حجر (OCR « وائل بن 2 ») + ثم جئتهم
  f5 p.110 0.20-0.38 : لا تباغضوا (psm6 تَبَاعَضُوا vs psm4 تَبَاغَضُوا)
  f6 p.110 0.55-0.72 : fin hadith ابن مسعود — أن يطعم معك / أن تزاني خليلة جارك
  f7 p.111 0.50-0.68 : بسرة بنت صفوان — من مس ذكره أَي/أَو… + الأعير والرفغ
  f8 p.111 0.85-1.00 : hadith التشهد — إن شئت أن تقوم فقم / تقعد
Chaîne R578+ — détection automatique des lignes (profil de densité), zéro vision API."""
import os
import numpy as np
import fitz
from PIL import Image, ImageDraw

HOME = "/home/z/my-project"
PDF = f"{HOME}/content/textbooks-src/ulum-hadith-1-thanawi.pdf"
OUT = f"{HOME}/tr-tmp/qa-crops-r599"
os.makedirs(OUT, exist_ok=True)
DPI = 1200

TARGETS = [
    ("f1-p112-idad",  112, 0.70, 0.78, "halves"),
    ("f2-p108-bayt",  108, 0.25, 0.55, "full"),
    ("f3-p109-bayt",  109, 0.28, 0.40, "halves"),
    ("f4-p110-wail",  110, 0.02, 0.20, "halves"),
    ("f5-p110-tabag", 110, 0.20, 0.38, "halves"),
    ("f6-p110-khalila", 110, 0.55, 0.72, "halves"),
    ("f7-p111-busra", 111, 0.50, 0.68, "halves"),
    ("f8-p111-tashahhud", 111, 0.85, 1.00, "halves"),
]

doc = fitz.open(PDF)

def lines_of(img_gray):
    """Détecte les lignes de texte par profil de densité sombre."""
    arr = np.asarray(img_gray.convert("L"))
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

for name, pno, f0, f1, mode in TARGETS:
    page = doc[pno - 1]
    R = page.rect
    clip = fitz.Rect(0, R.height * f0, R.width, R.height * f1)
    pix = page.get_pixmap(dpi=DPI, clip=clip)
    band = Image.frombytes("RGB", (pix.width, pix.height), pix.samples)
    ls = lines_of(band)
    rows = []
    for n, (a, b) in enumerate(ls, 1):
        a2, b2 = max(0, a - 12), min(band.height, b + 12)
        line = band.crop((0, a2, band.width, b2))
        if mode == "halves":
            for tag, seg in (("R", line.crop((line.width // 2, 0, line.width, line.height))),
                             ("L", line.crop((0, 0, line.width // 2, line.height)))):
                seg = seg.resize((1550, max(1, int(seg.height * 1550 / seg.width))), Image.LANCZOS)
                rows.append((f"p{pno} L{n}{tag}", seg))
        else:
            seg = line.resize((1550, max(1, int(line.height * 1550 / line.width))), Image.LANCZOS)
            rows.append((f"p{pno} L{n}", seg))
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
    print(f"{name}: {len(ls)} lignes -> {W}x{H}")
print("R599 phase 2 fine crops terminés")

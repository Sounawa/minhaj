# -*- coding: utf-8 -*-
"""Minhāj — Preuves image leçon 3 hadith-3es (R625, slot pdf-mut23h2x-392).
1) pages 25-30 à 200 dpi (lecture directe, contexte)
2) crops 900 dpi de chaque ligne « رقم: » (numéros Muwaṭṭaʾ — jamais devinés)
   + bannière p.25 haut (الدرس 3)
empile les crops d'une même page verticalement pour économiser les lectures.
Sortie : tr-tmp/qa-crops-r625/
"""
import fitz
import re
from PIL import Image
import os

PDF = "/home/z/my-project/content/textbooks-src/hadith-3-iadadi_text.pdf"
OUT = "/home/z/my-project/tr-tmp/qa-crops-r625"
os.makedirs(OUT, exist_ok=True)

doc = fitz.open(PDF)

# --- 1) pages complètes 200 dpi ---
for p in (25, 26, 27, 28, 29, 30):
    pix = doc[p - 1].get_pixmap(dpi=200)
    pix.save(f"{OUT}/p{p:03d}-full-200.png")
print("pages 200dpi OK")

# --- 2) localisation des lignes « رقم » (stocké « مقر » — OCR inversé) ---
NUM_PAGES = (25, 26, 28, 29, 30)
for p in NUM_PAGES:
    page = doc[p - 1]
    pw, ph = page.rect.width, page.rect.height
    d = page.get_text("dict")
    kept = []
    labels = []
    for blk in d["blocks"]:
        if blk.get("type") != 0:
            continue
        for ln in blk["lines"]:
            t = "".join(s["text"] for s in ln["spans"])
            if ("مقر" in t) or ("رقم" in t):
                kept.append(fitz.Rect(ln["bbox"]))
                labels.append(t.strip()[:60])
    # fallback : lignes avec nombre à 3 chiffres
    if not kept:
        for blk in d["blocks"]:
            if blk.get("type") != 0:
                continue
            for ln in blk["lines"]:
                t = "".join(s["text"] for s in ln["spans"])
                if re.search(r"\d{3}", t):
                    kept.append(fitz.Rect(ln["bbox"]))
                    labels.append(t.strip()[:60])
    print(f"p.{p}: {len(kept)} ligne(s) -> {labels}")
    crops = []
    # resserrement : bbox du groupe de 3 chiffres dans la ligne (spans)
    for i, r in enumerate(kept):
        num_rect = None
        for blk in d["blocks"]:
            if blk.get("type") != 0:
                continue
            for ln in blk["lines"]:
                if abs(fitz.Rect(ln["bbox"]).y0 - r.y0) < 3:
                    for sp in ln["spans"]:
                        if re.search(r"\d{3}", sp["text"]):
                            cand = fitz.Rect(sp["bbox"])
                            num_rect = cand if num_rect is None else num_rect | cand
        if num_rect is not None:
            x0 = max(0, num_rect.x0 - 90)
            x1 = min(pw, num_rect.x1 + 90)
            y0 = max(0, r.y0 - 14)
            y1 = min(ph, r.y1 + 14)
            pix = page.get_pixmap(dpi=900, clip=fitz.Rect(x0, y0, x1, y1))
        else:
            y0 = max(0, r.y0 - 12)
            y1 = min(ph, r.y1 + 14)
            pix = page.get_pixmap(dpi=900, clip=fitz.Rect(0, y0, pw, y1))
        f = f"{OUT}/p{p:03d}-num{i}-900.png"
        pix.save(f)
        crops.append(f)
    if crops:
        # empilement vertical
        ims = [Image.open(f) for f in crops]
        wmax = max(im.width for im in ims)
        htot = sum(im.height for im in ims) + 10 * (len(ims) - 1)
        canvas = Image.new("RGB", (wmax, htot), "white")
        y = 0
        for im in ims:
            canvas.paste(im, (0, y))
            y += im.height + 10
        stack = f"{OUT}/p{p:03d}-nums-stack.png"
        canvas.save(stack)
        print(f"   stack: {stack} {canvas.size}")

# --- 3) bannière p.25 haut (600 dpi) ---
page = doc[24]
pw, ph = page.rect.width, page.rect.height
pix = page.get_pixmap(dpi=600, clip=fitz.Rect(0, 0, pw, ph * 0.16))
pix.save(f"{OUT}/p025-banner-600.png")
print("bannière OK")

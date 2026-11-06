# -*- coding: utf-8 -*-
"""Minhāj — Preuves image leçon 4 hadith-3es (R626, slot pdf-mut23h2x-393).
1) pages 31-39 à 200 dpi (lecture directe, contexte + tranchage bornes)
2) crops 900 dpi de chaque ligne « رقم: » (numéros Muwaṭṭaʾ — jamais devinés)
   + bannière p.31 haut (600 dpi) + iʿdād bas p.38/p.39
empile les crops d'une même page verticalement pour économiser les lectures.
Sortie : tr-tmp/qa-crops-r626b/
"""
import fitz
import re
from PIL import Image
import os

PDF = "/home/z/my-project/content/textbooks-src/hadith-3-iadadi_text.pdf"
OUT = "/home/z/my-project/tr-tmp/qa-crops-r626b"
os.makedirs(OUT, exist_ok=True)

doc = fitz.open(PDF)

# --- 1) pages complètes 200 dpi ---
for p in (31, 32, 33, 34, 35, 36, 37, 38, 39):
    pix = doc[p - 1].get_pixmap(dpi=200)
    pix.save(f"{OUT}/p{p:03d}-full-200.png")
print("pages 200dpi OK")

# --- 2) localisation des lignes « رقم » (stocké « مقر » — OCR inversé) ---
NUM_PAGES = (31, 32, 33, 34, 35, 36, 37, 38)
for p in NUM_PAGES:
    page = doc[p - 1]
    pw, ph = page.rect.width, page.rect.height
    d = page.get_text("dict")
    # collecter toutes les lignes avec bbox une fois
    all_lines = []
    for blk in d["blocks"]:
        if blk.get("type") != 0:
            continue
        for ln in blk["lines"]:
            t = "".join(s["text"] for s in ln["spans"])
            all_lines.append((fitz.Rect(ln["bbox"]), t, ln["spans"]))
    kept = [(r, t) for (r, t, sp) in all_lines if ("مقر" in t) or ("رقم" in t)]
    print(f"p.{p}: {len(kept)} ligne(s) « مقر » -> {[t.strip()[:40] for _, t in kept]}")
    crops = []
    for i, (r, t) in enumerate(kept):
        # chercher un span à chiffres dans la ligne elle-même
        num_rect = None
        same = [sp for (rr, tt, sp) in all_lines if abs(rr.y0 - r.y0) < 3]
        for ln_spans in same:
            for sp in ln_spans:
                if re.search(r"\d{2,4}", sp["text"]):
                    cand = fitz.Rect(sp["bbox"])
                    num_rect = cand if num_rect is None else num_rect | cand
        # sinon : lignes adjacentes (±34 pt) — cas « .]984 » sur ligne séparée
        if num_rect is None:
            for (rr, tt, sp) in all_lines:
                if abs(rr.y0 - r.y0) < 34 and abs(rr.y0 - r.y0) > 1:
                    for s in sp:
                        if re.search(r"\d{2,4}", s["text"]):
                            cand = fitz.Rect(s["bbox"])
                            num_rect = cand if num_rect is None else num_rect | cand
        if num_rect is not None:
            x0 = max(0, num_rect.x0 - 90)
            x1 = min(pw, num_rect.x1 + 90)
            y0 = max(0, min(r.y0, num_rect.y0) - 14)
            y1 = min(ph, max(r.y1, num_rect.y1) + 14)
            pix = page.get_pixmap(dpi=900, clip=fitz.Rect(x0, y0, x1, y1))
        else:
            y0 = max(0, r.y0 - 12)
            y1 = min(ph, r.y1 + 14)
            pix = page.get_pixmap(dpi=900, clip=fitz.Rect(0, y0, pw, y1))
        f = f"{OUT}/p{p:03d}-num{i}-900.png"
        pix.save(f)
        crops.append(f)
    if crops:
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

# --- 3) bannière p.31 haut (600 dpi) + iʿdād bas p.38 / haut p.39 ---
page = doc[30]
pw, ph = page.rect.width, page.rect.height
pix = page.get_pixmap(dpi=600, clip=fitz.Rect(0, 0, pw, ph * 0.20))
pix.save(f"{OUT}/p031-banner-600.png")
pix = page.get_pixmap(dpi=600, clip=fitz.Rect(0, ph * 0.62, pw, ph))
pix.save(f"{OUT}/p031-tamhid-600.png")
page = doc[37]
pix = page.get_pixmap(dpi=600, clip=fitz.Rect(0, ph * 0.55, pw, ph))
pix.save(f"{OUT}/p038-bas-600.png")
page = doc[38]
pix = page.get_pixmap(dpi=600, clip=fitz.Rect(0, 0, pw, ph * 0.45))
pix.save(f"{OUT}/p039-haut-600.png")
print("bannière + zones OK")

# -*- coding: utf-8 -*-
"""Minhāj — bandes d'inspection ciblées v2 leçon 6 hadith-3es (R638).
Bandes ≤ 2800 px : rendu simple (échelle ≥ 54 %) ; bandes hautes : grille 2x2
(ordre arabe : droite-haut, gauche-haut, droite-bas, gauche-bas).
+ pile des numéros de référence (crochets bleus) localisés par search_for."""
import os
import fitz
from PIL import Image

PDF = "/home/z/my-project/content/textbooks-src/hadith-3-iadadi_text.pdf"
OUT = "/home/z/my-project/tr-tmp/qa-crops-r638"
os.makedirs(OUT, exist_ok=True)
doc = fitz.open(PDF)
DPI = 700


def render(page_no):
    pix = doc[page_no - 1].get_pixmap(dpi=DPI)
    return Image.frombytes("RGB", (pix.width, pix.height), pix.samples)


def band(tag, page_no, y0, y1):
    img = render(page_no)
    H = img.height
    crop = img.crop((0, int(H * y0), img.width, int(H * y1)))
    W, h = crop.width, crop.height
    if h <= 2800:
        pile = crop
    else:
        midw, midh = W // 2, h // 2
        rt, lt = crop.crop((midw, 0, W, midh)), crop.crop((0, 0, midw, midh))
        rb, lb = crop.crop((midw, midh, W, h)), crop.crop((0, midh, midw, h))
        pile = Image.new("RGB", (W, h + 16), "white")
        pile.paste(rt, (0, 0))
        pile.paste(lt, (0, 0 + midh + 8))
        pile.paste(rb, (0, midh + 16))
        pile.paste(lb, (midw, midh + 16))
        # grille : RT à gauche-haut... on remplace : ordre visuel RT|LT / RB|LB
        pile = Image.new("RGB", (W, h + 16), "white")
        pile.paste(rt, (0, 0))
        pile.paste(lt, (midw, 0))
        pile.paste(rb, (0, midh + 8))
        pile.paste(lb, (midw, midh + 8))
    path = f"{OUT}/band-{tag}.png"
    pile.save(path)
    print(f"OK {path} — {pile.width}x{pile.height}")


def number_pile():
    """Crops autour de chaque ligne « رقم » des pages 45-50, empilés."""
    crops = []
    for p in range(45, 51):
        page = doc[p - 1]
        for needle in ("رقم", "أطوملا", "الموطأ"):
            for r in page.search_for(needle):
                pix = page.get_pixmap(dpi=DPI, clip=fitz.Rect(r.x0 - 40, r.y0 - 14, r.x1 + 220, r.y1 + 26))
                im = Image.frombytes("RGB", (pix.width, pix.height), pix.samples)
                crops.append((p, im))
        break
    # dédoublonnage grossier par page/ordre y
    crops.sort(key=lambda t: t[0])
    W = max(im.width for _, im in crops)
    H = sum(im.height for _, im in crops) + 6 * len(crops)
    pile = Image.new("RGB", (W, H), "white")
    y = 0
    for p, im in crops:
        pile.paste(im, (0, y))
        y += im.height + 6
    path = f"{OUT}/pile-numeros.png"
    pile.save(path)
    print(f"OK {path} — {pile.width}x{pile.height} ({len(crops)} crops)")


band("p45-objectifs", 45, 0.22, 0.56)
band("p45-matn930", 45, 0.80, 1.00)
band("p46-tarjama", 46, 0.26, 0.60)
band("p50-oyad", 50, 0.52, 0.74)
band("p50-zamaniya", 50, 0.74, 1.00)
number_pile()

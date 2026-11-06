# -*- coding: utf-8 -*-
# R627 — passe 3 MICRO : recadrages 1200 dpi des lignes en litige (arbitrage final).
import os, fitz

HOME = "/home/z/my-project"
BOOK = f"{HOME}/content/textbooks-src/ulum-hadith-2-thanawi_text.pdf"
OUT = f"{HOME}/tr-tmp/qa-crops-r627"
doc = fitz.open(BOOK)

def render(p, dpi, y0, y1, name):
    page = doc[p - 1]
    r = page.rect
    rect = fitz.Rect(r.x0, r.y0 + y0 * r.height, r.x1, r.y0 + y1 * r.height)
    pix = page.get_pixmap(matrix=fitz.Matrix(dpi / 72, dpi / 72), clip=rect)
    pix.save(f"{OUT}/{name}.png")
    print(name, pix.width, "x", pix.height)

render(63, 1200, 0.76, 0.90, "ADJ3-p63-istikhlac-lignes-1200")
render(64, 1200, 0.07, 0.15, "ADJ3-p64-luga-ligne-1200")
render(64, 1200, 0.40, 0.55, "ADJ3-p64-tasawwuf-lignes-1200")
render(64, 1200, 0.48, 0.62, "ADJ3-p64-hadith2-matn-1200")
render(65, 1200, 0.02, 0.12, "ADJ3-p65-taqrib-lignes-1200")
render(65, 1200, 0.54, 0.65, "ADJ3-p65-dawani-lignes-1200")
render(66, 1200, 0.14, 0.26, "ADJ3-p66-jam-fin-1200")
render(66, 1200, 0.27, 0.46, "ADJ3-p66-shafii-item-1200")
render(66, 1200, 0.42, 0.58, "ADJ3-p66-furak-item-1200")
render(66, 1200, 0.55, 0.75, "ADJ3-p66-thawri-lignes-1200")
render(67, 1200, 0.22, 0.42, "ADJ3-p67-balaqini-fin-1200")
render(67, 1200, 0.36, 0.50, "ADJ3-p67-question2-1200")
print("OK passe 3 micro")

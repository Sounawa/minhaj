# -*- coding: utf-8 -*-
# R627 — passe 2 : recadrages ciblés 900 dpi sur les zones divergentes.
# Chaque point en litige (miroir/lecture) est relu SUR L'IMAGE — jamais deviné.
import os, fitz

HOME = "/home/z/my-project"
BOOK = f"{HOME}/content/textbooks-src/ulum-hadith-2-thanawi_text.pdf"
OUT = f"{HOME}/tr-tmp/qa-crops-r627"
os.makedirs(OUT, exist_ok=True)
doc = fitz.open(BOOK)

def render(p, dpi, y0, y1, name, x0=0.0, x1=1.0):
    page = doc[p - 1]
    r = page.rect
    rect = fitz.Rect(r.x0 + x0 * r.width, r.y0 + y0 * r.height,
                     r.x0 + x1 * r.width, r.y0 + y1 * r.height)
    pix = page.get_pixmap(matrix=fitz.Matrix(dpi / 72, dpi / 72), clip=rect)
    pix.save(f"{OUT}/{name}.png")
    print(name, pix.width, "x", pix.height)

render(63, 900, 0.72, 0.92, "ADJ2-p63-istikhlac-900")
render(63, 900, 0.50, 0.72, "ADJ2-p63-sarh-gloses-900")
render(64, 900, 0.05, 0.30, "ADJ2-p64-def-lisan-900")
render(64, 900, 0.28, 0.62, "ADJ2-p64-mithal-haut-900")
render(64, 900, 0.55, 1.00, "ADJ2-p64-mithal-bas-900")
render(65, 900, 0.00, 0.14, "ADJ2-p65-ref-taqrib-900")
render(65, 900, 0.55, 0.72, "ADJ2-p65-ref-dawani-900")
render(66, 900, 0.00, 0.22, "ADJ2-p66-haut-quote-900")
render(66, 900, 0.25, 0.55, "ADJ2-p66-shafii-furak-900")
render(66, 900, 0.52, 0.78, "ADJ2-p66-thawri-quote-900")
render(67, 900, 0.08, 0.40, "ADJ2-p67-sakhawi-suite-900")
render(67, 700, 0.36, 0.55, "ADJ2-p67-atamal-700")
print("OK passe 2")

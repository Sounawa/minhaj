#!/usr/bin/env python3
"""R634 — recadrages ciblés 600 dpi (p33 haut, p34 bas, p35/p37 ligne صنعه) méthode r625."""
import fitz, os

PDF = "content/textbooks-src/hadith-3-iadadi_text.pdf"
OUT = "tr-tmp/r634"
os.makedirs(OUT, exist_ok=True)
doc = fitz.open(PDF)

def crop(pno, y0f, y1f, name, x0f=0.0, x1f=1.0, zoom=600/72):
    pg = doc[pno-1]
    r = pg.rect
    clip = fitz.Rect(r.width*x0f, r.height*y0f, r.width*x1f, r.height*y1f)
    pix = pg.get_pixmap(matrix=fitz.Matrix(zoom, zoom), clip=clip)
    path = f"{OUT}/{name}.png"
    pix.save(path)
    print(name, pix.width, "x", pix.height)

# p.33 : entête الفهم (glosses + استخلص)
crop(33, 0.04, 0.42, "c-p033-haut-600")
# p.34 : bas de page (texte du Qirān + citation)
crop(34, 0.62, 1.00, "c-p034-bas-600")
# p.35 : bande médiane (réponse Uthmān + réplique Saʿd + citation 980)
crop(35, 0.25, 0.75, "c-p035-mil-600")
# p.37 : bande médiane (reprise 980 + شيباني + قول سعد)
crop(37, 0.10, 0.60, "c-p037-mil-600")

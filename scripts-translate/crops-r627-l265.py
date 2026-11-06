# -*- coding: utf-8 -*-
# R627 — recadrages adjudication leçon 11 uh2 (pdf-mut23h2u-265, p.63-67)
# Zones ambiguës à trancher SUR L'IMAGE (jamais devinées) :
#   p.63 bannière+objectifs ; p.63 bas استخلاص ; p.64 ref لسان العرب (miroir 141/12) ;
#   p.65 hadith الماء + القلتان + ref القيرواني (125/1) ; p.66 liste تصنيف + ref (220/3) ;
#   p.67 quote السخاوي + ref (81/3) + أتأمل + iʿdād leçon 12
import os, fitz

HOME = "/home/z/my-project"
BOOK = f"{HOME}/content/textbooks-src/ulum-hadith-2-thanawi_text.pdf"
OUT = f"{HOME}/tr-tmp/qa-crops-r627"
os.makedirs(OUT, exist_ok=True)
doc = fitz.open(BOOK)

def render(p, dpi, clip, name):
    page = doc[p - 1]
    r = page.rect
    if clip:
        rect = fitz.Rect(r.x0, r.y0 + clip[0] * r.height, r.x1, r.y0 + clip[1] * r.height)
    else:
        rect = None
    pix = page.get_pixmap(matrix=fitz.Matrix(dpi / 72, dpi / 72), clip=rect)
    pix.save(f"{OUT}/{name}.png")
    print(name, pix.width, "x", pix.height)

# Pleines pages 500 dpi (contexte)
for p in (63, 64, 65, 66, 67):
    render(p, 500, None, f"p{p}-full")
render(62, 500, None, "p62-full")       # voisin inf (i3dad leçon 10)
render(68, 500, None, "p68-full")       # voisin sup (leçon 12)

# Zones ciblées 700-900 dpi
render(63, 900, (0.00, 0.16), "ADJ-p63-banniere-900")
render(63, 700, (0.14, 0.42), "ADJ-p63-objectifs-tamhid-700")
render(63, 700, (0.55, 1.00), "ADJ-p63-bas-matn-istikhlac-700")
render(64, 700, (0.00, 0.30), "ADJ-p64-haut-def-muhkam-700")
render(64, 900, (0.10, 0.22), "ADJ-p64-ref-lisan-900")
render(64, 700, (0.30, 1.00), "ADJ-p64-bas-mithal-700")
render(65, 700, (0.00, 0.35), "ADJ-p65-haut-mukhtalif-700")
render(65, 900, (0.28, 0.52), "ADJ-p65-hadith-ma-900")
render(65, 700, (0.45, 0.78), "ADJ-p65-qultayn-700")
render(65, 900, (0.70, 0.85), "ADJ-p65-ref-qayrawani-900")
render(65, 700, (0.78, 1.00), "ADJ-p65-bas-naw-700")
render(66, 700, (0.00, 0.30), "ADJ-p66-haut-jam-700")
render(66, 700, (0.25, 0.72), "ADJ-p66-tasnim-liste-700")
render(66, 900, (0.55, 0.70), "ADJ-p66-ref-fath-900")
render(66, 700, (0.68, 1.00), "ADJ-p66-bas-taqwim-700")
render(67, 900, (0.00, 0.30), "ADJ-p67-haut-sakhawi-900")
render(67, 700, (0.30, 1.00), "ADJ-p67-bas-idad-700")
print("OK — recadrages dans", OUT)

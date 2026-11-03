# -*- coding: utf-8 -*-
"""Minhāj — Preuve image leçon 11 hadith-2es (slot pdf-12, R548).
Recyclage sandbox : outil antérieur perdu, réécrit. Méthode d'économie R104 :
composites 300 dpi (6 bandes horizontales empilées par page) + recadrages
900 dpi ciblés au besoin. Sortie : tr-tmp/qa-crops-r548/."""
import os
import fitz
from PIL import Image, ImageDraw

PDF = "/home/z/my-project/content/textbooks-src/hadith-2-iadadi_text.pdf"
OUT = "/home/z/my-project/tr-tmp/qa-crops-r548"
os.makedirs(OUT, exist_ok=True)

doc = fitz.open(PDF)

def page_mat(page_no, dpi, n_bands=6, tag=""):
    """Page complète en bandes 300 dpi empilées (composite lisible en chat)."""
    pg = doc[page_no - 1]
    pix = pg.get_pixmap(dpi=dpi)
    img = Image.frombytes("RGB", (pix.width, pix.height), pix.samples)
    W, H = img.size
    band_h = H // n_bands
    comp = Image.new("RGB", (W, band_h * n_bands + 8 * (n_bands - 1)), "white")
    d = ImageDraw.Draw(comp)
    y = 0
    for i in range(n_bands):
        band = img.crop((0, i * band_h, W, min((i + 1) * band_h, H)))
        comp.paste(band, (0, y))
        d.line([(0, y - 4), (W, y - 4)], fill="red", width=3) if y else None
        d.text((6, y + 4), f"p{page_no} b{i + 1}/{n_bands}", fill="red")
        y += band_h + 8
    path = f"{OUT}/p{page_no:02d}{tag}-comp.png"
    comp.save(path)
    print(path, comp.size)

def crop(page_no, y0f, y1f, dpi, name):
    """Recadrage ciblé pleine largeur (fractions verticales) haute dpi."""
    pg = doc[page_no - 1]
    R = pg.rect
    clip = fitz.Rect(R.x0, R.y0 + (R.y1 - R.y0) * y0f, R.x1, R.y0 + (R.y1 - R.y0) * y1f)
    pix = pg.get_pixmap(dpi=dpi, clip=clip)
    path = f"{OUT}/{name}.png"
    Image.frombytes("RGB", (pix.width, pix.height), pix.samples).save(path)
    print(path, (pix.width, pix.height))

# 1) Pages 79-85 : composites 6 bandes 300 dpi (structure + gros corps)
for p in range(79, 86):
    page_mat(p, 300)

# 2) Recadrages ciblés haute dpi — zones critiques (numéros rouges / isnāds /
#    lexies altérées) — tolérance large, affinés après lecture des composites
crop(79, 0.03, 0.30, 400, "p79-tamhid-refs")       # renvois البقرة/غافر + intro
crop(79, 0.30, 0.62, 400, "p79-abumusa-isnad")     # hadith Abū Mūsā + isnād h1
crop(79, 0.62, 0.99, 400, "p79-h1-matn")           # matn h1 (من قال لا إله...)
crop(80, 0.00, 0.22, 400, "p80-h1-fin-562")        # fin h1 + [562]
crop(80, 0.22, 0.55, 400, "p80-h2-isnad")          # isnād h2 (ibn Šihāb…)
crop(80, 0.55, 1.00, 400, "p80-h2-matn-572")       # matn h2 + [572]
crop(81, 0.00, 0.20, 400, "p81-fin-566")           # fin h2 + [566] + h3
crop(81, 0.55, 0.99, 400, "p81-rafi-isnad")        # رافع b. … + citation Mālik
crop(82, 0.00, 0.25, 400, "p82-rafi-matn-567")     # matn رافع + [567]
crop(82, 0.70, 1.00, 400, "p82-sulayman-564")      # isnād سليمان/يزيد + [564]
crop(83, 0.00, 0.35, 400, "p83-dua1-569")          # اللهم أسألك الهدى + [569]
crop(83, 0.35, 0.68, 400, "p83-arafa-569b")        # d. عرفة + isnād + [569]
crop(83, 0.68, 1.00, 400, "p83-taawus-569c")       # الزبير/طاوس + [569]
crop(84, 0.00, 0.30, 400, "p84-572-thulth")        # الثلث الأخير + [572]
crop(84, 0.30, 0.65, 400, "p84-dakhil-572b")       # داخل الصلاة (garbled) + [572]
crop(84, 0.65, 1.00, 400, "p84-iftitah-576")       # افتتاح الليل + [576]
crop(85, 0.00, 0.45, 400, "p85-istiksaf-151")      # quote1 + [151]
crop(85, 0.20, 0.75, 400, "p85-istiksaf-185")      # quote2 + [185] + hadith
crop(85, 0.60, 1.00, 400, "p85-i3dad")             # الإعداد القبلي
print("DONE")

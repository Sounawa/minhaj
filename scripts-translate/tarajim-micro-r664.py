# -*- coding: utf-8 -*-
"""Minhāj R664 — micro-crops 1200 dpi des mots pivots (bandes étroites).
Composite unique : 1 lecture VLM/moi = 5 adjudications."""
import fitz
from PIL import Image, ImageDraw

PDF = "/home/z/my-project/content/textbooks-src/ulum-hadith-2-thanawi_text.pdf"
OUT = "/home/z/my-project/tr-tmp/qa-crops-r664"

# (label, page 0-based, y0, y1, x0, x1)
BANDS = [
    ("dhahabi-titres (العين/المعين + المشتبه)", 133, 100, 124, 38, 424),
    ("suyuti-nom (سابق/سائق)", 133, 235, 280, 38, 424),
    ("iyad-ligne1 (عمرون اليحمصبي)", 133, 350, 392, 38, 424),
    ("iyad-الإلاع", 133, 460, 486, 38, 424),
    ("salah-annee (643/646)", 132, 186, 208, 260, 424),
]

doc = fitz.open(PDF)
imgs = []
for label, pno, y0, y1, x0, x1 in BANDS:
    page = doc[pno]
    clip = fitz.Rect(x0, y0, x1, y1)
    pix = page.get_pixmap(dpi=1200, clip=clip)
    f = f"{OUT}/micro-{pno+1}-{y0}.png"
    pix.save(f)
    imgs.append((label, f))
    print(f"micro: {label} → {pix.width}x{pix.height}")

bar = 30
w = max(Image.open(f).width for _, f in imgs)
h = sum(Image.open(f).height for _, f in imgs) + bar * len(imgs)
canvas = Image.new("RGB", (w, h), (255, 255, 255))
d = ImageDraw.Draw(canvas)
y = 0
for label, f in imgs:
    d.rectangle([0, y, w, y + bar], fill=(30, 90, 180))
    d.text((10, y + 8), label, fill=(255, 255, 255))
    y += bar
    im = Image.open(f)
    canvas.paste(im, (0, y))
    y += im.height
canvas.save(f"{OUT}/comp-r664-micro.png")
print("composite micro:", w, "x", h)

# -*- coding: utf-8 -*-
"""Minhāj — Calibration search_for + micro-crops leçon 24 (pdf-25, R570).
Chiffres candidats (couche) → positions exactes → crops 1200 dpi.
Bandes 600 dpi pour le corps des hadiths (méthode R565/R569).
"""
import os
import fitz
from PIL import Image

PDF = "/home/z/my-project/content/textbooks-src/hadith-2-iadadi_text.pdf"
CROPS = "/home/z/my-project/tr-tmp/qa-crops-r570"
doc = fitz.open(PDF)

PAGES_NUMS = {
    165: ["805"],
    166: ["800", "812", "815", "94"],
    167: ["801"],
    168: ["809", "811", "183"],
    169: ["816", "817", "184"],
    170: ["829"],
}

print("--- SEARCH_FOR hits (page, string, rect pt) ---")
num_crops = {}  # page -> list of (label, rect)
for n, strings in PAGES_NUMS.items():
    page = doc[n - 1]
    for s in strings:
        hits = page.search_for(s)
        if not hits:
            print(f"p.{n} '{s}': NO HIT")
            continue
        for i, r in enumerate(hits):
            print(f"p.{n} '{s}' hit{i}: {r}")
            num_crops.setdefault(n, []).append((f"num-{n}-{s}-{i}", r))

# Crops 1200 dpi des nombres (pad large : «رقم:» + guillemet)
num_imgs = {}
for n, items in num_crops.items():
    page = doc[n - 1]
    for label, r in items:
        clip = fitz.Rect(max(0, r.x0 - 95), max(0, r.y0 - 14),
                         min(page.rect.x1, r.x1 + 30), min(page.rect.y1, r.y1 + 14))
        pix = page.get_pixmap(clip=clip, dpi=1200)
        png = f"{CROPS}/{label}.png"
        pix.save(png)
        num_imgs.setdefault(n, []).append((label, clip, png))
        print(f"CROP1200 {label}: {clip} → {pix.width}x{pix.height}")

# Bandes 600 dpi (y à 300 dpi ×2), colonne x 80-520pt
BANDS = [
    (165, 900, 1350, "p165-objectifs"),
    (165, 1330, 1850, "p165-intro-a"),
    (165, 1850, 2300, "p165-intro-b-805"),
    (166, 400, 900, "p166-had1-a"),
    (166, 900, 1400, "p166-had1-b"),
    (166, 1400, 1900, "p166-had1-c-800"),
    (166, 1900, 2400, "p166-had2-812"),
    (166, 2400, 2900, "p166-815"),
    (166, 2900, 3400, "p166-tarjama-94"),
    (167, 1900, 2400, "p167-thana"),
    (167, 2350, 2950, "p167-801"),
    (168, 1950, 2450, "p168-809"),
    (168, 2450, 2950, "p168-811-aya"),
    (169, 380, 880, "p169-haut-aya184"),
    (169, 1150, 1450, "p169-816a"),
    (169, 1850, 2350, "p169-816b"),
    (169, 2550, 2900, "p169-817"),
    (170, 1050, 1600, "p170-829"),
]
pages_needed = sorted({b[0] for b in BANDS})
for n in pages_needed:
    p600 = f"{CROPS}/page-{n}-600.png"
    if not os.path.exists(p600):
        doc[n - 1].get_pixmap(dpi=600).save(p600)
        print(f"RENDU600 {p600}")

X0, X1 = 80, 520
bands_by_page = {}
for n, y1, y2, label in BANDS:
    im = Image.open(f"{CROPS}/page-{n}-600.png")
    crop = im.crop((X0 * 600 // 72, y1 * 2, X1 * 600 // 72, y2 * 2))
    crop.save(f"{CROPS}/b-{label}.png")
    bands_by_page.setdefault(n, []).append(crop)
    print(f"BAND {label}: {crop.width}x{crop.height}")

# Composites : nombres par page, puis bandes groupées par 3
def stack(imgs, out, bg=(255, 215, 215)):
    w = max(i.width for i in imgs)
    h = sum(i.height for i in imgs) + 12 * (len(imgs) - 1)
    canvas = Image.new("RGB", (w, h), bg)
    y = 0
    for i in imgs:
        canvas.paste(i, (0, y))
        y += i.height + 12
    canvas.save(out, quality=85)
    print(f"COMPOSITE {out}: {w}x{h}")

for n, items in num_imgs.items():
    stack([Image.open(p) for _, _, p in items], f"{CROPS}/nums-{n}.png")

band_list = [(n, c) for n in pages_needed for c in bands_by_page.get(n, [])]
for ci in range(0, len(band_list), 3):
    grp = band_list[ci:ci + 3]
    stack([c for _, c in grp], f"{CROPS}/comp-{chr(65 + ci // 3)}.jpg")
print("DONE")

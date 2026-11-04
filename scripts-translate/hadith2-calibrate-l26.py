# -*- coding: utf-8 -*-
"""Minhāj — Calibration l26 (pdf-27, R571) : chiffres candidats → crops 1200 dpi + bandes 600 dpi."""
import os
import fitz
from PIL import Image

PDF = "/home/z/my-project/content/textbooks-src/hadith-2-iadadi_text.pdf"
CROPS = "/home/z/my-project/tr-tmp/qa-crops-r571"
doc = fitz.open(PDF)

PAGES_NUMS = {
    177: ["828"],
    178: ["830", "835", "836", "183"],
    181: ["832", "834", "836", "91", "4", "1"],
    182: ["839"],
}
print("--- SEARCH_FOR hits ---")
num_crops = {}
for n, strings in PAGES_NUMS.items():
    page = doc[n - 1]
    for s in strings:
        for i, r in enumerate(page.search_for(s)):
            print(f"p.{n} '{s}' hit{i}: {r}")
            num_crops.setdefault(n, []).append((f"num-{n}-{s}-{i}", r))

for n, items in num_crops.items():
    page = doc[n - 1]
    for label, r in items:
        clip = fitz.Rect(max(0, r.x0 - 95), max(0, r.y0 - 16),
                         min(page.rect.x1, r.x1 + 30), min(page.rect.y1, r.y1 + 16))
        pix = page.get_pixmap(clip=clip, dpi=1200)
        pix.save(f"{CROPS}/{label}.png")
        print(f"CROP1200 {label} {pix.width}x{pix.height}")

# Bandes 600 dpi par page (3 zones verticales), colonne x 80-520 pt
BANDS = [
    (177, 250, 1250, "p177-objectifs-intro"),
    (177, 1250, 2300, "p177-had1-828"),
    (178, 250, 1300, "p178-had-830"),
    (178, 1300, 2400, "p178-fatwa-835"),
    (178, 2400, 3400, "p178-said-836-tarjama"),
    (179, 250, 1300, "p179-glossaire"),
    (179, 1300, 2400, "p179-analyse-eid"),
    (180, 250, 1250, "p180-wisal"),
    (180, 1250, 2350, "p180-atam-aski"),
    (180, 2350, 3400, "p180-wajib-tatabbu"),
    (181, 250, 1300, "p181-tatabbu-832"),
    (181, 1300, 2400, "p181-nadhr-836"),
    (182, 250, 1300, "p182-malade-yahya"),
    (182, 1300, 2400, "p182-istidlal-muslim"),
    (182, 2400, 3400, "p182-bilagh-839"),
    (183, 250, 1300, "p183-preparation"),
]
pages_needed = sorted({b[0] for b in BANDS})
for n in pages_needed:
    p600 = f"{CROPS}/page-{n}-600.png"
    if not os.path.exists(p600):
        doc[n - 1].get_pixmap(dpi=600).save(p600)
        print(f"RENDU600 {n}")

X0, X1 = 80, 520
bands_by_page = {}
for n, y1, y2, label in BANDS:
    im = Image.open(f"{CROPS}/page-{n}-600.png")
    crop = im.crop((X0 * 600 // 72, y1 * 2, X1 * 600 // 72, y2 * 2))
    crop.save(f"{CROPS}/b-{label}.png")
    bands_by_page.setdefault(n, []).append(crop)
    print(f"BAND {label} {crop.width}x{crop.height}")

def stack(imgs, out, bg=(255, 220, 220)):
    w = max(i.width for i in imgs)
    h = sum(i.height for i in imgs) + 12 * (len(imgs) - 1)
    canvas = Image.new("RGB", (w, h), bg)
    y = 0
    for i in imgs:
        canvas.paste(i, (0, y))
        y += i.height + 12
    canvas.save(out, quality=85)
    print(f"COMPOSITE {out} {w}x{h}")

for n, items in num_crops.items():
    stack([Image.open(p) for _, _, p in items], f"{CROPS}/nums-{n}.png")
band_list = [(n, c) for n in pages_needed for c in bands_by_page.get(n, [])]
for ci in range(0, len(band_list), 3):
    grp = band_list[ci:ci + 3]
    stack([c for _, c in grp], f"{CROPS}/comp-{chr(65 + ci // 3)}.jpg")
print("DONE")

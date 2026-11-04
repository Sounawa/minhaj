# -*- coding: utf-8 -*-
"""Minhāj — Calibration fine leçon 17 (pdf-18, R562) : localisation par la
couche OCR (positions exactes) des lignes portant les mots non tranchés,
puis recadrages 900 dpi alignés sur les bboxes réelles — méthode R560
(hadith2-calibrate-l16.py). Un seul rendu 900 dpi par page en mémoire."""
from PIL import Image, ImageDraw
import fitz, os, gc

PDF = "/home/z/my-project/content/textbooks-src/hadith-2-iadadi_text.pdf"
OUT = "/home/z/my-project/tr-tmp/qa-crops-r562"
DPI = 900
TARGET_W = 1900

# (label, page, ancre OCR brute, nb lignes avant, nb lignes après)
TARGETS = [
    ("118-tamhid-l1", 118, "هسفنل ميركلا", 0, 0),
    ("118-box-l1", 118, "دوي مَلَو كله اذإ", 0, 1),
    ("118-box-l23", 118, "زواجي الر", 0, 1),
    ("119-fadakar-annaz", 119, "رَكَذف", 0, 1),
    ("119-aktib", 119, "ًاباتك", 0, 0),
    ("121-mithl-hal", 121, "ناميلس لأس", 0, 1),
    ("121-madan", 121, "ةيشام وأ", 0, 0),
    ("121-mutanawwia", 121, "ةانتقم", 0, 0),
    ("121-falyazd", 121, "كزيلف", 0, 0),
    ("121-risala-fin", 121, "ركفلا راد", 0, 0),
    ("122-yawm-qabd", 122, "ءامهنع", 0, 0),
    ("122-zurayq-anzur", 122, "قيرز ىلإ بتك", 0, 1),
    ("123-yabiha-thaman", 123, "نيحةاك", 1, 1),
    ("123-hurth-wa-man", 123, "فرحلاو", 0, 1),
    ("123-fayaqum-nasab", 123, "عيمجلا يكزيو", 1, 0),
    ("123-la-yada", 123, "فاكَرلا هيف", 0, 0),
    ("123-wafratuha", 123, "اهترفو", 0, 0),
    ("123-firka-am", 123, "دحاو ماعل", 0, 0),
    ("124-baatha-yawm", 124, "ءدحاَو ٍلْوَح", 1, 1),
]


def norm(s: str) -> str:
    return "".join(s.split())


doc = fitz.open(PDF)
by_page = {}
for t in TARGETS:
    by_page.setdefault(t[1], []).append(t)

tiles_by_label = {}
for page_no in sorted(by_page):
    pix = doc[page_no - 1].get_pixmap(dpi=DPI, colorspace=fitz.csGRAY)
    img = Image.frombytes("L", (pix.width, pix.height), pix.samples)
    h, w = img.height, img.width
    d = doc[page_no - 1].get_text("dict")
    lines = []
    for blk in d["blocks"]:
        if blk.get("type") != 0:
            continue
        for ln in blk["lines"]:
            txt = "".join(sp["text"] for sp in ln["spans"])
            lines.append((ln["bbox"], txt))
    for label, _, anchor, before, after in by_page[page_no]:
        idx = next((i for i, (_, t) in enumerate(lines)
                    if norm(anchor) in norm(t)), None)
        if idx is None:
            print(f"!! ancre introuvable {label}: {anchor[:20]}")
            continue
        lo = max(0, idx - before)
        hi = min(len(lines) - 1, idx + after)
        x0 = min(lines[i][0][0] for i in range(lo, hi + 1))
        x1 = max(lines[i][0][2] for i in range(lo, hi + 1))
        y0 = min(lines[i][0][1] for i in range(lo, hi + 1))
        y1 = max(lines[i][0][3] for i in range(lo, hi + 1))
        k = DPI / 72.0  # points PDF -> pixels rendus
        pad_x, pad_y = 0.02 * w, 0.010 * h
        tile = img.crop((max(0, int(x0 * k - pad_x)), max(0, int(y0 * k - pad_y)),
                         min(w, int(x1 * k + pad_x)), min(h, int(y1 * k + pad_y))))
        scale = min(1.0, TARGET_W / tile.width)
        tile = tile.resize((int(tile.width * scale), int(tile.height * scale)),
                           Image.LANCZOS)
        tiles_by_label[label] = tile
        print(f"OK {label} — bbox {x0:.0f},{y0:.0f} -> {x1:.0f},{y1:.0f}")
    del img, pix
    gc.collect()

order = [t[0] for t in TARGETS if t[0] in tiles_by_label]
tiles = [(lab, tiles_by_label[lab]) for lab in order]
total_h = sum(t.height + 42 for _, t in tiles) + 10
comp = Image.new("L", (TARGET_W, total_h), 255)
dr = ImageDraw.Draw(comp)
y = 5
for lab, tile in tiles:
    dr.rectangle([0, y, TARGET_W, y + 30], fill=205)
    dr.text((10, y + 6), lab, fill=0)
    y += 42
    comp.paste(tile, (0, y))
    y += tile.height + 8
path = os.path.join(OUT, "comp8-calibrated.png")
comp.save(path)
print(f"OK {path} — {TARGET_W}x{total_h}")

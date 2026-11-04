# -*- coding: utf-8 -*-
"""Minhāj R575 — 9 recadrages d'adjudication 600 dpi en 2 composites groupés.
Zones douteuses de l'annexe 30 (lāʾiḥat al-maṣādir) + فهرس المواضيع."""
import fitz
from PIL import Image, ImageDraw
import io, os

PDF = "/home/z/my-project/content/textbooks-src/hadith-2-iadadi_text.pdf"
OUTDIR = "/home/z/my-project/tr-tmp/r575-crops"
os.makedirs(OUTDIR, exist_ok=True)

doc = fitz.open(PDF)

# (page, y0_frac, y1_frac, label)
ZONES_A = [
    (201, 0.27, 0.34, "A1 p201 intro — المصحف المصدي ?"),
    (202, 0.60, 0.68, "A2 p202 entrée 10 — مكتب المطوعات/المطبوعات ?"),
    (203, 0.35, 0.45, "A3 p203 entrée 15 — سلم/سليم محمد عطا + معوض"),
    (204, 0.28, 0.39, "A4 p204 entrée 21 — مركز نجيب/نجيبه"),
    (204, 0.64, 0.73, "A5 p204 entrée 25 — دارة/دار المعارف النظامية"),
]
ZONES_B = [
    (207, 0.29, 0.36, "B1 p207 rangée 2 — إضاءات/إشارات/إضاعات منهجية"),
    (208, 0.68, 0.75, "B2 p208 rangée 33 — وسّتة أيام من شوال"),
    (208, 0.78, 0.93, "B3 p208 rangées 34-36 — لما/لهم + المواضعات/المواضيع"),
]


def build(zones, outname):
    strips = []
    for pno, y0, y1, label in zones:
        pix = doc[pno - 1].get_pixmap(dpi=600)
        img = Image.open(io.BytesIO(pix.tobytes("png")))
        strip = img.crop((0, int(img.height * y0), img.width, int(img.height * y1)))
        strips.append((label, strip))
    w = max(s.width for _, s in strips)
    label_h, gap = 44, 26
    total_h = sum(s.height for _, s in strips) + (label_h + gap) * len(strips)
    comp = Image.new("RGB", (w, total_h), "white")
    d = ImageDraw.Draw(comp)
    y = 0
    for label, s in strips:
        d.text((12, y + 10), f"=== {label} ===", fill="blue")
        y += label_h
        comp.paste(s, (0, y))
        y += s.height + gap
    fp = f"{OUTDIR}/{outname}"
    comp.save(fp)
    print("OK", fp, comp.size)


build(ZONES_A, "composite-A-p201-p204.png")
build(ZONES_B, "composite-B-p207-p208.png")
print("DONE")

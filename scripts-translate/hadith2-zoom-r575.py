# -*- coding: utf-8 -*-
"""Minhāj R575 — zooms serrés via rects de la couche texte (p.208).
Z1: لما/لهم (rangée 34) ; Z2: المواضعات/المواضيع (rangée 36) ; Z3: وسّتة (rangée 33)."""
import fitz, io
from PIL import Image, ImageDraw

doc = fitz.open("/home/z/my-project/content/textbooks-src/hadith-2-iadadi_text.pdf")
page = doc[207]  # p.208
print("couche p.208 (extraits):")
raw = page.get_text("text")
for needle in ("سرهف", "تاعوضوملا", "ةّسو", "ةستو", "وسّ"):
    rects = page.search_for(needle)
    print(f"  '{needle}' -> {len(rects)} rect(s)", [tuple(round(v, 1) for v in r) for r in rects])

zones = []
# rangée 34 : « فهرس الأعلام المترجم لما » — chercher فهرس (serhef) au-dessus de 201
rects_fihris = [r for r in page.search_for("سرهف") if r.y0 < page.rect.height * 0.60]
if rects_fihris:
    r = rects_fihris[-1]
    zones.append((max(0, r.x0 - 220), r.y0 - 30, page.rect.width * 0.62, r.y1 + 30, "Z1 r34 فهرس الأعلام المترجم …"))
# rangée 36 : المواضعات
rects_mwdu = page.search_for("تاعوضوملا")
if rects_mwdu:
    r = rects_mwdu[-1]
    zones.append((max(0, r.x0 - 200), r.y0 - 30, page.rect.width * 0.45, r.y1 + 30, "Z2 r36 فهرس المواضعات/المواضيع"))
# rangée 33 : وسّتة
r33 = None
for needle in ("ةّسو", "ةستو", "وسّ"):
    rr = [r for r in page.search_for(needle) if r.y0 < page.rect.height * 0.60]
    if rr:
        r33 = rr[0]
        break
if r33 is None:
    r33 = fitz.Rect(page.rect.width * 0.45, page.rect.height * 0.475, page.rect.width * 0.75, page.rect.height * 0.5)
zones.append((r33.x0 - 160, r33.y0 - 28, r33.x1 + 220, r33.y1 + 28, "Z3 r33 وسّتة أيام"))

strips = []
for x0, y0, x1, y1, label in zones:
    clip = fitz.Rect(x0, y0, x1, y1)
    pix = page.get_pixmap(dpi=1200, clip=clip)
    img = Image.open(io.BytesIO(pix.tobytes("png")))
    strips.append((label, img))
    print("crop", label, img.size)

w = max(s.width for _, s in strips)
label_h, gap = 40, 22
th = sum(s.height for _, s in strips) + (label_h + gap) * len(strips)
comp = Image.new("RGB", (w, th), "white")
d = ImageDraw.Draw(comp)
y = 0
for label, s in strips:
    d.text((8, y + 8), f"=== {label} ===", fill="blue")
    y += label_h
    comp.paste(s, (0, y))
    y += s.height + gap
comp.save("/home/z/my-project/tr-tmp/r575-crops/composite-D-zooms-v2.png")
print("OK", comp.size)

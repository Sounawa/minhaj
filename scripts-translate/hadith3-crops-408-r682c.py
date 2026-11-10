# -*- coding: utf-8 -*-
"""R682-ter — ULTRA-CROPS leçon 408 : fenêtres minimales sur les points restés
divergents après la passe b :
 z1. p.130 : crochet de renvoi [سورة التوبة الآية: N] (démi-cadre resserré).
 z2. p.133 : hadith d'ʿAlī complet (deux lignes + renvoi 1170).
 z3. p.134 : ligne «فليحلق ولا تشبهوا بـ...» + renvoi 1185.
 z4. p.134 : hadith d'ʿUmar 1186 (من عقص رأسه أو ...) complet.
 z5. p.135 : première ligne de l'athar 1183 (لقي رجلا من أهله بـ...).
Sorties : tr-tmp/qa-crops-r682/z*.png (900 dpi)."""
import fitz, os

PDF = "/home/z/my-project/content/textbooks-src/hadith-3-iadadi_text.pdf"
OUT = "/home/z/my-project/tr-tmp/qa-crops-r682"
os.makedirs(OUT, exist_ok=True)
doc = fitz.open(PDF)
DPI = 900

CROPS = [
    ("z130-ref",   130, 0.00, 0.28, 0.505, 0.615),
    ("z133-ali",   133, 0.03, 0.97, 0.595, 0.675),
    ("z134-1185",  134, 0.03, 0.97, 0.455, 0.545),
    ("z134-1186",  134, 0.03, 0.97, 0.330, 0.460),
    ("z135-ath1",   135, 0.03, 0.97, 0.075, 0.180),
]

mat = fitz.Matrix(DPI / 72, DPI / 72)
for nom, pg, fx0, fx1, fy0, fy1 in CROPS:
    page = doc[pg - 1]
    r = page.rect
    clip = fitz.Rect(r.width * fx0, r.height * fy0, r.width * fx1, r.height * fy1)
    pix = page.get_pixmap(matrix=mat, clip=clip)
    path = f"{OUT}/{nom}.png"
    pix.save(path)
    print(f"OK {path} {pix.width}x{pix.height}")
print(f"TOTAL {len(CROPS)} ultra-crops")

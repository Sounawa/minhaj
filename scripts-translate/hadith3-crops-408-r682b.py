# -*- coding: utf-8 -*-
"""R682-bis — CROPS CIBLÉS de preuve leçon 408 (relecture des zones à trancher).
Zones restées incertaines après la double passe (text layer + VLM r679/r682) :
 1. p.130 : chiffre du renvoi [سورة التوبة الآية: N] du verset du tamhīd (at-Tawba)
    + étendue exacte de la citation imprimée.
 2. p.131 : première ligne du hadith de Ḥafṣa (فقالت: يا رسول الله ما شأن الناس...).
 3. p.133 : hadith d'ʿAlī (نحر بيده ... ونحر غيره ...) — trois lectures divergentes.
 4. p.134 : dernier mot du hadith d'ʿUmar 1185 (ولا تشبهوا بالتلبيد/بالملبدين/بالثلبد).
 5. p.135 : athar [1183] complet + en-tête éventuel de l'exploitation.
 6. p.135 : 3e question de l'iʿdād (préparation 409) si elle existe.
Sorties : tr-tmp/qa-crops-r682/y*.png (900 dpi, zooms plein cadre ou demi-cadre)."""
import fitz, os

PDF = "/home/z/my-project/content/textbooks-src/hadith-3-iadadi_text.pdf"
OUT = "/home/z/my-project/tr-tmp/qa-crops-r682"
os.makedirs(OUT, exist_ok=True)
doc = fitz.open(PDF)
DPI = 900

# (nom, page_pdf_1-indexée, x0_frac, x1_frac, y0_frac, y1_frac)
CROPS = [
    ("y130-aya-ref",   130, 0.03, 0.97, 0.50, 0.63),   # verset + renvoi
    ("y130-aya-left",  130, 0.00, 0.45, 0.50, 0.63),   # zoom demi-cadre sur le renvoi
    ("y131-hafsa1",   131, 0.03, 0.97, 0.30, 0.42),   # hadith Ḥafṣa ligne 1-2
    ("y133-ali",      133, 0.03, 0.97, 0.585, 0.685),  # hadith ʿAlī + renvoi 1170
    ("y134-talbid",   134, 0.03, 0.97, 0.42, 0.53),    # 1185 fin
    ("y135-athar",    135, 0.03, 0.97, 0.00, 0.36),    # athar 1183 complet
    ("y135-i3dada",   135, 0.03, 0.97, 0.55, 0.92),    # 3e question iʿdād ?
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
print(f"TOTAL {len(CROPS)} crops ciblés")

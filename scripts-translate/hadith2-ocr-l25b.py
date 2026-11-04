# -*- coding: utf-8 -*-
"""R571 — OCR ciblé serré des crochets [الموطأ رقم: NNN] à 600/1200 dpi, psm 6+7, binarisé."""
import subprocess, os
import fitz
from PIL import Image, ImageOps

PDF = "/home/z/my-project/content/textbooks-src/hadith-2-iadadi_text.pdf"
OUT = "/home/z/my-project/tr-tmp/qa-crops-r571"
TESS = os.path.abspath("scripts-translate/tessdata")
doc = fitz.open(PDF)

ZONES = [
    (172, 121, 141, "n818"),
    (172, 183, 202, "n821"),
    (172, 308, 327, "n826"),
    (173, 525, 544, "n819d"),
    (174, 300, 319, "n819a"),
    (174, 697, 716, "n822"),
    (175, 352, 372, "n825"),   # ligne du « 825]. » d'après tsv (top=1501px@300dpi ≈ 360pt)
    (176, 231, 250, "n824"),
]

def ocr(png, psm):
    r = subprocess.run(
        ["tesseract", png, "stdout", "-l", "ara", "--psm", str(psm),
         "--tessdata-dir", TESS, "-c", "preserve_interword_spaces=1"],
        capture_output=True, text=True)
    return " ".join(r.stdout.split())

for pno, y0, y1, tag in ZONES:
    page = doc[pno - 1]
    for zoom, suf in ((8.33, "600"), (16.67, "1200")):
        clip = fitz.Rect(40, y0, 270, y1)   # zone du crochet + numéro (gauche de ligne RTL)
        pix = page.get_pixmap(matrix=fitz.Matrix(zoom, zoom), clip=clip)
        png = f"{OUT}/n-{tag}-{suf}.png"
        pix.save(png)
        # version binarisée
        bin_png = f"{OUT}/n-{tag}-{suf}-bin.png"
        im = Image.open(png).convert("L")
        ImageOps.autocontrast(im).point(lambda p: 255 if p > 150 else 0).save(bin_png)
        for f, lab in ((png, "brut"), (bin_png, "bin")):
            for psm in (6, 7):
                t = ocr(f, psm)
                if t:
                    print(f"{tag} {suf} {lab} psm{psm}: {t!r}")

# -*- coding: utf-8 -*-
"""R571 — complément : n824 (renvoi à l'intérieur du box استهلال, zone x décalée) et n822."""
import subprocess, os
import fitz
from PIL import Image, ImageOps

PDF = "/home/z/my-project/content/textbooks-src/hadith-2-iadadi_text.pdf"
OUT = "/home/z/my-project/tr-tmp/qa-crops-r571"
TESS = os.path.abspath("scripts-translate/tessdata")
doc = fitz.open(PDF)

def ocr(png, psm):
    r = subprocess.run(
        ["tesseract", png, "stdout", "-l", "ara", "--psm", str(psm),
         "--tessdata-dir", TESS, "-c", "preserve_interword_spaces=1"],
        capture_output=True, text=True)
    return " ".join(r.stdout.split())

JOBS = [
    (176, 226, 254, 275, 470, "n824b"),
    (174, 694, 720, 30, 320, "n822b"),
]

for pno, y0, y1, x0, x1, tag in JOBS:
    page = doc[pno - 1]
    for zoom, suf in ((8.33, "600"), (16.67, "1200"), (25, "1800")):
        clip = fitz.Rect(x0, y0, x1, y1)
        pix = page.get_pixmap(matrix=fitz.Matrix(zoom, zoom), clip=clip)
        png = f"{OUT}/{tag}-{suf}.png"
        pix.save(png)
        im = Image.open(png).convert("L")
        bin_png = f"{OUT}/{tag}-{suf}-bin.png"
        ImageOps.autocontrast(im).point(lambda p: 255 if p > 150 else 0).save(bin_png)
        for f, lab in ((png, "brut"), (bin_png, "bin")):
            for psm in (6, 7):
                t = ocr(f, psm)
                if t:
                    print(f"{tag} {suf} {lab} psm{psm}: {t!r}")

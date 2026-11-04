# -*- coding: utf-8 -*-
"""R571 — OCR ciblé (tesseract ara) des micro-crops à haute résolution.
Troisième canal de preuve pour les renvois dont les passes divergent."""
import subprocess, os
import fitz

PDF = "/home/z/my-project/content/textbooks-src/hadith-2-iadadi_text.pdf"
OUT = "/home/z/my-project/tr-tmp/qa-crops-r571"
TESS = "scripts-translate/tessdata" if os.path.isdir("scripts-translate/tessdata") else "/usr/share/tesseract-ocr/4.00/tessdata"
doc = fitz.open(PDF)

ZONES = [
    (172, 112, 145, "num-818"),
    (172, 175, 205, "num-821"),
    (172, 300, 330, "num-826"),
    (173, 518, 548, "num-819-desm"),
    (174, 295, 325, "num-819-ata"),
    (174, 692, 720, "num-822"),
    (175, 1480 * 72 / 300 - 20, 1480 * 72 / 300 + 30, "num-825"),  # ligne du « 825]. » (tsv 300dpi top=1501)
    (176, 224, 256, "num-824"),
]

for pno, y0, y1, tag in ZONES:
    page = doc[pno - 1]
    clip = fitz.Rect(25, y0, 480, y1)
    pix = page.get_pixmap(matrix=fitz.Matrix(12, 12), clip=clip)  # ~864 dpi
    png = f"{OUT}/t-{tag}.png"
    pix.save(png)
    r = subprocess.run(
        ["tesseract", png, "stdout", "-l", "ara", "--psm", "7",
         "--tessdata-dir", TESS, "-c", "preserve_interword_spaces=1"],
        capture_output=True, text=True)
    txt = " ".join(r.stdout.split())
    print(f"{tag}: {txt!r}")

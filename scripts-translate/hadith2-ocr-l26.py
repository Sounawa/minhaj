# -*- coding: utf-8 -*-
"""Minhāj — OCR local leçon 26 hadith-2es (slot pdf-27, R571).
Bornes : l26 p.177-183 (l27 أهداف p.184). Tesseract 300 dpi + TSV."""
import csv, os, subprocess
import fitz

PDF = "/home/z/my-project/content/textbooks-src/hadith-2-iadadi_text.pdf"
CROPS = "/home/z/my-project/tr-tmp/qa-crops-r571"
TESSDATA = "/home/z/my-project/scripts-translate/tessdata"
FIRST, LAST = 177, 183

os.makedirs(CROPS, exist_ok=True)
env = dict(os.environ, TESSDATA_PREFIX=TESSDATA)
doc = fitz.open(PDF)
for n in range(FIRST, LAST + 1):
    page = doc[n - 1]
    png300 = f"{CROPS}/page-{n}-300.png"
    if not os.path.exists(png300):
        pix = page.get_pixmap(dpi=300)
        pix.save(png300)
        print(f"RENDU {png300}")
    r = subprocess.run(["tesseract", png300, f"{CROPS}/tess-page-{n}",
                        "-l", "ara", "--psm", "3", "tsv", "txt"],
                       env=env, capture_output=True, text=True, timeout=120)
    print(f"p{n}: rc={r.returncode}")
print("OCR DONE")

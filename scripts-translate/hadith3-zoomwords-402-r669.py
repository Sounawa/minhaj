# -*- coding: utf-8 -*-
"""Minhāj — zooms mot à mot R669 passe 3 (slot pdf-mut23h2x-402).
Crops localisés par bboxes des spans natifs (fitz get_text dict) à 1200 dpi,
tesseract ara multi-PSM. Zones : عَبْلَة (p.95 y543), بذر×2 (p.95 y630),
عُبَيْد (p.90 y383), citation al-Qāsim complète (p.94 y318-372, 1000 dpi)."""
import io
import json
import os
import subprocess

import fitz
from PIL import Image

PDF = "/home/z/my-project/content/textbooks-src/hadith-3-iadadi_text.pdf"
DIR = "/home/z/my-project/tr-tmp/qa-crops-r669"
TESSDATA = "/home/z/my-project/scripts-translate/tessdata"
os.makedirs(DIR, exist_ok=True)
doc = fitz.open(PDF)


def crop(page_no, rect, dpi, name):
    pg = doc[page_no - 1]
    pix = pg.get_pixmap(matrix=fitz.Matrix(dpi / 72, dpi / 72), clip=fitz.Rect(*rect), alpha=False)
    img = Image.frombytes("RGB", (pix.width, pix.height), pix.samples)
    path = f"{DIR}/{name}.png"
    img.save(path)
    print(f"OK {path} — {img.width}x{img.height}")
    return path


def ocr(path, psms=(6, 4, 7, 13, 8)):
    img = Image.open(path)
    out = {}
    for psm in psms:
        buf = io.BytesIO()
        img.save(buf, format="PNG")
        buf.seek(0)
        env = {**os.environ, "TESSDATA_PREFIX": TESSDATA}
        res = subprocess.run(["tesseract", "stdin", "stdout", "--psm", str(psm), "-l", "ara"],
                             input=buf.getvalue(), capture_output=True, env=env, timeout=120)
        out[f"psm{psm}"] = res.stdout.decode("utf-8", "replace").strip()
    return out


jobs = [
    ("z-abla-p95",    95, (210, 535, 480, 562), 1200),   # isnād : أبي عَبْلَة
    ("z-budhr1-p95",  95, (55,  622, 115, 660), 1400),   # يوم بذر (1)
    ("z-budhr2-p95",  95, (195, 622, 255, 660), 1400),   # يوم بذر (2)
    ("z-ubayd-p90",   90, (500, 375, 548, 407), 1400),   # عُبَيْد الله
    ("z-qasim-p94",   94, (40, 318, 545, 372), 1000),    # citation القاسم entière
    ("z-fmaha-p90",   90, (430, 440, 520, 472), 1200),   # فما هي حكم (début question)
]
results = {}
for name, pno, rect, dpi in jobs:
    path = crop(pno, rect, dpi, name)
    results[name] = ocr(path)

out = f"{DIR}/_r669-zoomwords.json"
json.dump(results, open(out, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(f"ÉCRIT {out}")

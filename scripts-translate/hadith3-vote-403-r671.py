# -*- coding: utf-8 -*-
"""Minhāj — vote tesseract local R671 (leçon 403 hadith-3es, p.97-102).
Mécanique R667/R669 : crops fitz 600 dpi resserrés (chiffres : x gauche 0.04-0.34 ;
mots : pleine largeur), tesseract ara multi-PSM (tessdata projet), votes
consignés dans tr-tmp/qa-crops-r670/_r671-ocr-results.json."""
import json
import os
import subprocess

import fitz
from PIL import Image

PDF = "/home/z/my-project/content/textbooks-src/hadith-3-iadadi_text.pdf"
OUT = "/home/z/my-project/tr-tmp/qa-crops-r670"
TESSDATA = "/home/z/my-project/scripts-translate/tessdata"
os.makedirs(OUT, exist_ok=True)
doc = fitz.open(PDF)

JOBS = [
    ("num-p97",   97, 0.845, 0.935, 0.04, 0.38),   # bracket + chiffre hadīṯ 1
    ("num-p98",   98, 0.395, 0.470, 0.04, 0.38),   # chiffre hadīṯ 2
    ("num-p99",   99, 0.750, 0.850, 0.04, 0.38),   # chiffre athar Ibn ʿUmar
    ("num-p100a", 100, 0.050, 0.170, 0.04, 0.38),  # chiffre athar ʿAṭāʾ
    ("num-p100b", 100, 0.435, 0.580, 0.04, 0.38),  # chiffres naql 1+2
    ("num-p101a", 101, 0.700, 0.790, 0.04, 0.38),  # chiffre athar Salma/ʿUbaydallāh
    ("num-p101b", 101, 0.790, 0.880, 0.04, 0.38),  # chiffre athar Asmāʾ
    ("num-p101c", 101, 0.870, 0.960, 0.04, 0.38),  # chiffre athar Ṭalḥa
    ("num-p102",  102, 0.830, 0.930, 0.04, 0.38),  # chiffre ḥadīṯ quraïš/āyāt
    ("word-p97-tamhid", 97, 0.470, 0.585, 0.04, 0.96),
    ("word-p97-matn",   97, 0.845, 0.935, 0.04, 0.96),
    ("word-p98-tarjama", 98, 0.545, 0.745, 0.04, 0.96),
    ("word-p99-athar",  99, 0.750, 0.850, 0.04, 0.96),
    ("word-p100-ataa", 100, 0.050, 0.170, 0.04, 0.96),
    ("word-p101-ibnmasud", 101, 0.240, 0.400, 0.04, 0.96),
    ("word-p101-rukh.sa",  101, 0.660, 0.790, 0.04, 0.96),
    ("word-p102-malik",   102, 0.440, 0.690, 0.04, 0.96),
    ("word-p102-aya3",    102, 0.690, 0.930, 0.04, 0.96),
]


def run_tess(path):
    outs = {}
    for psm in (6, 7):
        cmd = ["tesseract", path, "stdout", "-l", "ara",
               "--tessdata-dir", TESSDATA, "--psm", str(psm)]
        try:
            r = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
            outs[f"psm{psm}"] = r.stdout.strip()
        except Exception as e:  # noqa: BLE001
            outs[f"psm{psm}"] = f"ERR {e}"
    return outs


results = {}
for name, pg_no, y0, y1, x0, x1 in JOBS:
    pg = doc[pg_no - 1]
    clip = fitz.Rect(pg.rect.width * x0, pg.rect.height * y0,
                     pg.rect.width * x1, pg.rect.height * y1)
    pix = pg.get_pixmap(matrix=fitz.Matrix(600 / 72, 600 / 72), clip=clip, alpha=False)
    img = Image.frombytes("RGB", (pix.width, pix.height), pix.samples)
    path = f"{OUT}/_r671-{name}.png"
    img.save(path)
    results[name] = {"band": [pg_no, y0, y1], "ocr": run_tess(path)}
    print(f"OK {name}")

out = f"{OUT}/_r671-ocr-results.json"
json.dump(results, open(out, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(f"ÉCRIT {out}")

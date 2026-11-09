# -*- coding: utf-8 -*-
"""Minhāj — OCR ara local d'adjudication R669 (slot pdf-mut23h2x-402).
SDK VLM en 429 (documenté R664/R667 : ne pas marteler) → bascule méthode
d'adjudication R667 : tesseract ara local (tessdata du projet) sur les cinq
crops ciblés 600 dpi ×0.85, multi-PSM, convergence avec les couches hadith3-
l402-{raw,readable} + lectures pleine page R657. Sortie : _r669-ara-ocr.json."""
import io
import json
import os
import subprocess
from PIL import Image, ImageOps

DIR = "/home/z/my-project/tr-tmp/qa-crops-r669"
TESSDATA = "/home/z/my-project/scripts-translate/tessdata"

ZONES = [
    "r669-a-p90-tamhid-chain",
    "r669-b-p91-salim-notice",
    "r669-c-p92-sharh-glosses",
    "r669-d-p94-salat-jumua",
    "r669-e-p95-istithmar",
]


def ocr(img, psm):
    buf = io.BytesIO()
    img.save(buf, format="PNG")
    buf.seek(0)
    env = {**os.environ, "TESSDATA_PREFIX": TESSDATA}
    cmd = ["tesseract", "stdin", "stdout", "--psm", str(psm), "-l", "ara"]
    proc = subprocess.run(cmd, input=buf.getvalue(), capture_output=True,
                          timeout=240, env=env)
    return proc.stdout.decode("utf-8", "replace").strip()


results = {}
for z in ZONES:
    img = Image.open(f"{DIR}/{z}.png")
    g = ImageOps.autocontrast(img.convert("L"))
    entry = {}
    for psm in (6, 4):
        t = ocr(g, psm)
        entry[f"psm{psm}"] = t
        print(f"===== {z} psm{psm} =====")
        print(t[:1400])
        print()
    results[z] = entry

json.dump(results, open(f"{DIR}/_r669-ara-ocr.json", "w"), ensure_ascii=False, indent=1)
print("ÉCRIT", f"{DIR}/_r669-ara-ocr.json")

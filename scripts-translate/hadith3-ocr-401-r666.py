# -*- coding: utf-8 -*-
"""Minhāj — Adjudication chiffres pivots leçon 12 hadith-3es (R666, slot
pdf-mut23h2x-401). Lecture d'image indépendante par OCR local tesseract (digits,
eng) sur micro-crops 900 dpi centrés sur les bbox exacts des spans numériques de
la couche texte (get_text rawdict). Read-tool image indisponible en contexte
sous-agent ; SDK VLM 429 documenté R664 — un essai, récusé. Chaque chiffre pivot
est tranché par OCR + convergence couches + lectures image R663 en cache."""
import io
import json
import re
import fitz
from PIL import Image, ImageOps
import subprocess

PDF = "/home/z/my-project/content/textbooks-src/hadith-3-iadadi_text.pdf"
OUT = "/home/z/my-project/tr-tmp/qa-crops-r666"
doc = fitz.open(PDF)

TARGETS = [(84, r'\b157\b'), (85, r'1093'), (85, r'1094'), (86, r'\b157\b'),
           (87, r'1090'), (87, r'\b157\b'), (87, r'1091'), (87, r'\b60\b'),
           (87, r'1092'), (88, r'1098'), (88, r'1096'), (88, r'\b28\b'),
           (88, r'1099'), (89, r'1097')]

def ocr_digits(img):
    buf = io.BytesIO()
    img.save(buf, format="PNG")
    buf.seek(0)
    proc = subprocess.run(
        ["tesseract", "stdin", "stdout", "--psm", "7", "-l", "eng",
         "-c", "tessedit_char_whitelist=0123456789"],
        input=buf.getvalue(), capture_output=True, text=True, timeout=60)
    return re.sub(r'[^0-9]', '', proc.stdout)

results = []
for (page_no, pat) in TARGETS:
    pg = doc[page_no - 1]
    d = pg.get_text("rawdict")
    for b in d["blocks"]:
        for l in b.get("lines", []):
            for s in l.get("spans", []):
                txt = "".join(ch["c"] for ch in s.get("chars", []))
                if re.search(pat, txt):
                    x0, y0, x1, y1 = s["bbox"]
                    clip = fitz.Rect(x0 - 6, y0 - 4, x1 + 6, y1 + 4)
                    pix = pg.get_pixmap(matrix=fitz.Matrix(900 / 72, 900 / 72), clip=clip, alpha=False)
                    img = Image.frombytes("RGB", (pix.width, pix.height), pix.samples)
                    g = ImageOps.autocontrast(img.convert("L"))
                    digits = ocr_digits(g)
                    img.save(f"{OUT}/ocr-p{page_no}-{re.sub(r'[^0-9]', '', pat)}.png")
                    results.append((page_no, pat, txt.strip(), digits))
                    print(f"p.{page_no} patron {pat} — span natif «{txt.strip()}» → OCR 900 dpi : «{digits}»")
json.dump(results, open(f"{OUT}/_r666-ocr-results.json", "w"), ensure_ascii=False, indent=1)

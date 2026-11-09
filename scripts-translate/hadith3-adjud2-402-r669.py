# -*- coding: utf-8 -*-
"""Minhāj — adjudication tesseract locale R669 passe 2 (slot pdf-mut23h2x-402).
VLM SDK en 429 (testé 15h37 UTC, erreur « Too many requests » — ne pas marteler,
documenté R664/R667 et dans hadith3-ara-ocr-402-r669.py) et lecture image directe
indisponible en contexte sous-agent → poursuite de la mécanique R667 :
crops fitz 600 dpi + tesseract ara local multi-PSM (tessdata du projet),
convergence avec couches hadith3-l402-{raw,readable} + lectures VLM R657
(_r657-read-*) + votes chiffres R667 (_r667-ocr-results.json).
Zones : a) p.90 chaîne tamhīd + question (bande r669-a ratée, 0.34-0.58) ;
b) p.92 gloses — 4ᵉ item ? ; c) p.94 citation al-Qāsim dégradée (يدقع/يدفع) ;
d) p.95 isnād du hadith d'exploitation (أبي عَبْلة / أبي عُطْبة) ;
e) p.95 matn complet ; f) p.96 verbe de l'exploitation (أشيع/أنشُر/أنسب) ;
g) p.94 mot يتعمد/يتعدد ; h) OCR des crops R669 restés sans lecture (f, g)."""
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

# (nom, page 1-based, bande y0-y1, échelle PIL)
JOBS = [
    ("r669-h-p90-chain-question", 90, (0.30, 0.58), 0.85),
    ("r669-i-p92-glosses-wide",   92, (0.02, 0.36), 0.85),
    ("r669-j-p94-qasim-quote",    94, (0.40, 0.66), 0.90),
    ("r669-k-p95-isnad-matn",     95, (0.55, 0.78), 0.90),
    ("r669-l-p96-exploit-line",   96, (0.10, 0.28), 0.90),
    ("r669-m-p94-yataadda",       94, (0.13, 0.26), 1.10),
]


def make_crop(name, page_no, band, scale):
    pg = doc[page_no - 1]
    clip = fitz.Rect(pg.rect.width * 0.04, pg.rect.height * band[0],
                     pg.rect.width * 0.97, pg.rect.height * band[1])
    pix = pg.get_pixmap(matrix=fitz.Matrix(600 / 72, 600 / 72), clip=clip, alpha=False)
    img = Image.frombytes("RGB", (pix.width, pix.height), pix.samples)
    img = img.resize((int(img.width * scale), int(img.height * scale)), Image.LANCZOS)
    path = f"{DIR}/{name}.png"
    img.save(path)
    print(f"OK {path} — {img.width}x{img.height}")
    return path


def ocr_ara(path, psms=(6, 4, 7, 3)):
    img = Image.open(path)
    out = {}
    for psm in psms:
        buf = io.BytesIO()
        img.save(buf, format="PNG")
        buf.seek(0)
        env = {**os.environ, "TESSDATA_PREFIX": TESSDATA}
        cmd = ["tesseract", "stdin", "stdout", "--psm", str(psm), "-l", "ara"]
        res = subprocess.run(cmd, input=buf.getvalue(), capture_output=True, env=env, timeout=120)
        out[f"psm{psm}"] = res.stdout.decode("utf-8", "replace").strip()
    return out


doc = fitz.open(PDF)
results = {}
for name, page_no, band, scale in JOBS:
    path = make_crop(name, page_no, band, scale)
    results[name] = ocr_ara(path)

# crops R669 précédents restés sans lecture tesseract
for prev in ("r669-f-p91-matn-salim", "r669-g-p95-hadith-end"):
    path = f"{DIR}/{prev}.png"
    if os.path.exists(path):
        results[prev] = ocr_ara(path)

out = f"{DIR}/_r669-adjud2.json"
json.dump(results, open(out, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(f"ÉCRIT {out}")

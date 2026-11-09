# -*- coding: utf-8 -*-
"""Minhāj — ADJUDICATION pivots leçon 13 hadith-3es (R667, slot pdf-mut23h2x-402,
أعمال يوم عرفة, p.90-96). Mécanique éprouvée R666 (leçon 12) : lecture d'image
indépendante par OCR local tesseract sur micro-crops 900 dpi centrés sur les bbox
exactes des spans numériques de la couche texte (get_text rawdict), + composites
de lecture 600 dpi ×0.55 pour le dépôt QA + OCR ara de convergence sur zones
pivots. Read-tool image indisponible en contexte sous-agent ; SDK VLM 429
documenté R664 — NE PAS L'APPELER. Convergence exigée : OCR R667 + couche
structurelle (spans rawdict, ordre RTL correct) + lectures image R657 couchées
(tr-tmp/qa-crops-r657/_r657-read-*.json) + registre hadith-3es.json.
Sortie : tr-tmp/qa-crops-r667/ + _r667-ocr-results.json."""
import io
import json
import os
import re
import fitz
from PIL import Image, ImageOps
import subprocess

PDF = "/home/z/my-project/content/textbooks-src/hadith-3-iadadi_text.pdf"
OUT = "/home/z/my-project/tr-tmp/qa-crops-r667"
TESSDATA = "/home/z/my-project/scripts-translate/tessdata"
doc = fitz.open(PDF)
SCALE = 0.55
X0, X1 = 0.04, 0.96

# ---------- A. Composites de lecture (patron hadith3-composite-401-r666.py) ----------
JOBS = [
    ("a1-p90-banner",   90, [(0.00, 0.30)]),
    ("a2-p90-tamhid",   90, [(0.22, 0.68)]),
    ("b1-p91-matn",     91, [(0.00, 0.55)]),
    ("b2-p91-tarajim",  91, [(0.55, 1.00)]),
    ("c1-p92-fiqh1",    92, [(0.02, 0.55)]),
    ("c2-p92-nawawi",   92, [(0.55, 1.00)]),
    ("d1-p93-waqt",     93, [(0.00, 0.40)]),
    ("d2-p93-adab",     93, [(0.40, 1.00)]),
    ("e1-p94-tahara",   94, [(0.00, 0.30)]),
    ("e2-p94-fitr",     94, [(0.30, 0.62)]),
    ("e3-p94-salat",    94, [(0.62, 1.00)]),
    ("f1-p95-qasr",     95, [(0.00, 0.45)]),
    ("f2-p95-taqwim",   95, [(0.45, 0.72)]),
    ("f3-p95-istithmar",95, [(0.68, 1.00)]),
    ("g1-p96-idad",     96, [(0.00, 1.00)]),
]

def render_bands(page_no, bands, scale=SCALE):
    pg = doc[page_no - 1]
    pieces, W = [], 0
    for (y0, y1) in bands:
        clip = fitz.Rect(pg.rect.width * X0, pg.rect.height * y0,
                         pg.rect.width * X1, pg.rect.height * y1)
        pix = pg.get_pixmap(matrix=fitz.Matrix(600 / 72, 600 / 72), clip=clip, alpha=False)
        img = Image.frombytes("RGB", (pix.width, pix.height), pix.samples)
        img = img.resize((int(img.width * scale), int(img.height * scale)), Image.LANCZOS)
        pieces.append(img)
        W = max(W, img.width)
    sep = 24
    H = sum(p.height for p in pieces) + sep * (len(pieces) - 1)
    canvas = Image.new("RGB", (W, H), (220, 220, 220))
    y = 0
    for p in pieces:
        canvas.paste(p, (0, y))
        y += p.height + sep
    return canvas

for name, page_no, bands in JOBS:
    canvas = render_bands(page_no, bands)
    path = f"{OUT}/{name}.png"
    if not os.path.exists(path):
        canvas.save(path)
    print(f"OK {path} — {canvas.width}x{canvas.height} (cache)")

# ---------- B. Micro-crops digits + OCR eng (chiffre par chiffre) ----------
# spans numériques rawdict trouvés sur p90-96 (ordre RTL structurel correct)
DIGIT_TARGETS = [
    (90, "1271"), (90, "1157"), (91, "1100"), (91, "1188"), (91, "106"),
    (92, "1152"), (93, "1157"), (94, "1155"), (94, "1101"),
    (94, "1190"), (94, "1191"), (95, "1270"),
]

def ocr(img, lang="eng", psm="7", whitelist="0123456789", extra=None):
    buf = io.BytesIO()
    img.save(buf, format="PNG")
    buf.seek(0)
    cmd = ["tesseract", "stdin", "stdout", "--psm", psm]
    if whitelist is not None:
        cmd += ["-l", lang, "-c", f"tessedit_char_whitelist={whitelist}"]
    else:
        cmd += ["-l", lang]
    if extra:
        cmd += extra
    # env COMPLET hérité (le remplacement intégral casse PATH/config → OCR vide)
    if lang == "eng":
        proc = subprocess.run(cmd, input=buf.getvalue(), capture_output=True,
                              timeout=90)
    else:
        env = {**os.environ, "TESSDATA_PREFIX": TESSDATA}
        proc = subprocess.run(cmd, input=buf.getvalue(), capture_output=True,
                              timeout=90, env=env)
    return proc.stdout.decode("utf-8", "replace").strip()

results = []
for (page_no, pat) in DIGIT_TARGETS:
    pg = doc[page_no - 1]
    d = pg.get_text("rawdict")
    hit = None
    for b in d["blocks"]:
        for l in b.get("lines", []):
            for s in l.get("spans", []):
                txt = "".join(ch["c"] for ch in s.get("chars", []))
                if pat in txt:
                    hit = (txt.strip(), s["bbox"])
                    break
    if not hit:
        print(f"!! p.{page_no} patron {pat} NON TROUVÉ en rawdict")
        continue
    txt, (x0, y0, x1, y1) = hit
    clip = fitz.Rect(x0 - 6, y0 - 4, x1 + 6, y1 + 4)
    pix = pg.get_pixmap(matrix=fitz.Matrix(900 / 72, 900 / 72), clip=clip, alpha=False)
    img = Image.frombytes("RGB", (pix.width, pix.height), pix.samples)
    g = ImageOps.autocontrast(img.convert("L"))
    # 3 lectures d'adjudication (psm 7 ×2 + psm 13)
    d1 = re.sub(r"[^0-9]", "", ocr(g, "eng", "7"))
    d2 = re.sub(r"[^0-9]", "", ocr(g, "eng", "6"))
    d3 = re.sub(r"[^0-9]", "", ocr(g, "eng", "13"))
    img.save(f"{OUT}/ocr-p{page_no}-{pat}.png")
    results.append({
        "page": page_no, "pattern": pat, "span_native": txt,
        "ocr_psm7": d1, "ocr_psm6": d2, "ocr_psm13": d3,
        "votes": [d1, d2, d3],
    })
    print(f"p.{page_no} span natif «{txt}» → OCR 900dpi psm7/6/13 : «{d1}» / «{d2}» / «{d3}»")

# ---------- C. Médaillons de bannière (13 p90, 14 p97) — bornes ----------
MEDALLIONS = [("med-p90", 90), ("med-p97", 97)]
for name, page_no in MEDALLIONS:
    pg = doc[page_no - 1]
    clip = fitz.Rect(pg.rect.width * 0.78, pg.rect.height * 0.015,
                     pg.rect.width * 0.99, pg.rect.height * 0.14)
    pix = pg.get_pixmap(matrix=fitz.Matrix(600 / 72, 600 / 72), clip=clip, alpha=False)
    img = Image.frombytes("RGB", (pix.width, pix.height), pix.samples)
    img.save(f"{OUT}/{name}.png")
    g = ImageOps.autocontrast(img.convert("L"))
    m1 = re.sub(r"[^0-9]", "", ocr(g, "eng", "7"))
    m2 = re.sub(r"[^0-9]", "", ocr(g, "eng", "10"))
    m3 = re.sub(r"[^0-9]", "", ocr(g, "eng", "11"))
    results.append({
        "page": page_no, "pattern": name, "span_native": "(calligraphie)",
        "ocr_psm7": m1, "ocr_psm10": m2, "ocr_psm11": m3,
        "votes": [m1, m2, m3],
    })
    print(f"médaillon p.{page_no} → OCR digits psm7/10/11 : «{m1}» / «{m2}» / «{m3}»")

# ---------- D. OCR ara de convergence sur zones pivots ----------
ARA_ZONES = [
    ("ara-p90-tamhid-chain", 90, [(0.16, 0.27)]),
    ("ara-p91-salim-malik",  91, [(0.70, 0.92)]),
    ("ara-p92-urana-note",   92, [(0.70, 0.85)]),
    ("ara-p94-haid",         94, [(0.06, 0.22)]),
    ("ara-p94-ayisha-end",   94, [(0.40, 0.52)]),
    ("ara-p95-shaytan-end",  95, [(0.78, 0.94)]),
    ("ara-p96-idad",         96, [(0.03, 0.38)]),
]
ara_results = []
for name, page_no, bands in ARA_ZONES:
    canvas = render_bands(page_no, bands, scale=0.85)
    path = f"{OUT}/{name}.png"
    canvas.save(path)
    txt = ocr(canvas, "ara", "6", whitelist=None)
    ara_results.append({"name": name, "ocr_ara": txt})
    print(f"OCR ara {name} :\n{txt[:400]}\n---")

json.dump({"digits": results, "ara": ara_results},
          open(f"{OUT}/_r667-ocr-results.json", "w"), ensure_ascii=False, indent=1)
print("ÉCRIT", f"{OUT}/_r667-ocr-results.json")

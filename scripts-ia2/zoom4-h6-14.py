#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# IA-2 — zoom4-h6-14 : crops MOT à 2400 dpi (×3 upscale) via boîtes TSV.
import subprocess, os
from PIL import Image, ImageOps

DIR = "/home/z/my-project/pdf-work/h6-14"
PDF = "/home/z/my-project/pdf-work/hadith-6ep.pdf"
OUT = "/home/z/my-project/pdf-work/h6-14/zoom4"
TESSDATA = "/home/z/my-project/pdf-work/tessdata"
env = dict(os.environ, TESSDATA_PREFIX=TESSDATA)
os.makedirs(OUT, exist_ok=True)

# (label, page, y0, y1 @600 de la LIGNE, regex du 1er mot ancre, regex du dernier mot ancre)
SEGS = [
    ("w1-liali-p78",     78, 1912, 2155, r"بَيْنَةِ|بَيَنَةِ|ببئه|بَيِّنَة", r"بِدَعْوَاهُ|بدعو"),
    ("w2-yubayyin-p78",  78, 5389, 5645, r"الْبينَة|الْببنهة|البيْتَة|لول|ولا", r"أَشخَاص|أشخاص|وَدِمَاءَهُمْ|ود مَاء"),
    ("w3-taqum-p78",     78, 4782, 5007, r"مَا لَمْ|مَا ف|مَا لم", r"بَيُنَة|بيه|بَيِّنَة|بخلاف"),
    ("w4-lahiqqi-p78",   78, 3733, 3979, r"اسْتَحْقاق|ستحقاق|اسْتحْقاق|مُتحْقاق", r"الَّذِي|الذي|الذِي"),
]

def words_of(page, y0, y1):
    png = f"{DIR}/p{page:03d}.png"
    r = subprocess.run(["tesseract", png, "stdout", "-l", "ara", "--psm", "6", "tsv"],
                       env=env, capture_output=True, text=True)
    ws = []
    for row in r.stdout.splitlines()[1:]:
        c = row.split("\t")
        if len(c) < 12 or not c[11].strip():
            continue
        left, top, w, h = int(c[6]), int(c[7]), int(c[8]), int(c[9])
        if y0 - 40 <= top <= y1 + 40:
            ws.append({"t": c[11], "x0": left, "x1": left + w, "top": top, "h": h})
    return ws

def ocr(png, psm):
    r = subprocess.run(["tesseract", png, "stdout", "-l", "ara", "--psm", str(psm)],
                       env=env, capture_output=True, text=True)
    return " ".join(r.stdout.split())

import re
for label, page, y0, y1, rx_a, rx_b in SEGS:
    ws = words_of(page, y0, y1)
    print(f"\n████ {label} — mots TSV de la ligne : {' | '.join(w['t'] for w in ws)[:180]}")
    ia = ib = None
    for i, w in enumerate(ws):
        if ia is None and re.search(rx_a, w["t"]):
            ia = i
        if re.search(rx_b, w["t"]):
            ib = i
    if ia is None:
        ia = 0
    if ib is None or ib <= ia:
        ib = min(ia + 6, len(ws) - 1)
    # segment entre les deux ancres (incluses)
    x_r = max(w["x1"] for w in ws[ia:ib + 1])
    x_l = min(w["x0"] for w in ws[ia:ib + 1])
    top = min(w["top"] for w in ws[ia:ib + 1])
    bot = max(w["top"] + w["h"] for w in ws[ia:ib + 1])
    # marge
    mx, my = 30, 25
    X0, Y0 = max(0, (x_l - mx) * 4), max(0, (top - my) * 4)
    W, H = min(5309 * 4 - X0, (x_r - x_l + 2 * mx) * 4), (bot - top + 2 * my) * 4
    base = f"{OUT}/{label}"
    subprocess.run(["pdftoppm", "-f", str(page), "-l", str(page), "-r", "2400",
                    "-gray", "-png", "-singlefile", "-x", str(X0), "-y", str(Y0),
                    "-W", str(W), "-H", str(H), PDF, base], check=True)
    img = Image.open(base + ".png")
    big = img.resize((img.width * 3, img.height * 3), Image.LANCZOS)
    auto = ImageOps.autocontrast(big, cutoff=1)
    seen = []
    variants = [("auto", auto)]
    for th in (140, 160, 180):
        variants.append((f"bw{th}", auto.point(lambda v, t=th: 255 if v > t else 0)))
    for name, im in variants:
        p = f"{base}-{name}.png"
        im.save(p)
        for psm in (7, 8, 13):
            t = ocr(p, psm)
            if t and t not in seen:
                seen.append(f"[{name}/psm{psm}] {t}")
    for s in seen[:6]:
        print("  " + s)

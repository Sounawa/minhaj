#!/usr/bin/env python3
# R608 — crops haute résolution des bandes clés de la leçon 27 (matrūk, p.129-132)
# ancres TSV (300 dpi) -> crops pdftoppm 1200 dpi
import subprocess, os, glob, sys

PDF = "content/textbooks-src/ulum-hadith-1-thanawi.pdf"
OUT = "/tmp/s138"
os.makedirs(OUT, exist_ok=True)
env = dict(os.environ, TESSDATA_PREFIX="/tmp/tessdata")

# ancre: (page, regex TSV, étiquette crop, demi-hauteur bande en px@300dpi)
ANCHORS = [
    (129, r"المتن|متَن|لمتن", "c129-matn", 260),
    (130, r"متروكه|متر و كه|متر وَكه|واحد", "c130-quote", 200),
    (130, r"يَجْهَر|يجهر|لمكتوب|المكتوب", "c130-daraqutni", 700),
    (131, r"وسم بالمتروك|وسِم|تصب|تصَب", "c131-suyuti-bayt", 200),
    (131, r"وأجمعوا|وَأجْمَع|لضّعْفه|لضعفه", "c131-naazim", 200),
    (131, r"الدهلوي|وَيّيسسى|ويقال", "c131-dehlawi", 220),
    (132, r"السيوطي|شر الضعيف|الضعيف الْوَضْمْ|الْوَضْمْ", "c132-suyuti-ist", 200),
    (132, r"أحفظ|القبلي|إعداد", "c132-i3dad", 300),
]

def tsv_words(page):
    png = glob.glob(f"{OUT}/pg{page}-*.png")[0]
    tsv = f"{OUT}/tsv{page}"
    subprocess.run(["tesseract", png, tsv, "-l", "ara", "--psm", "4", "tsv"],
                   env=env, capture_output=True)
    words = []
    with open(tsv + ".tsv", encoding="utf-8") as f:
        next(f)
        for line in f:
            c = line.rstrip("\n").split("\t")
            if len(c) >= 12 and c[11].strip():
                words.append((c[11], int(c[6]), int(c[7]), int(c[8]), int(c[9])))
    return words, png

import re
results = []
for page, pat, tag, half in ANCHORS:
    words, png = tsv_words(page)
    rx = re.compile(pat)
    hits = [(w, x, y, w2, h) for (w, x, y, w2, h) in words if rx.search(w)]
    if not hits:
        print(f"NO-HIT p{page} {tag}")
        continue
    y = hits[0][2] + hits[0][4] // 2
    Y, H = max(0, y * 4 - half * 4), half * 8
    crop = f"{OUT}/{tag}"
    r = subprocess.run(["pdftoppm", "-r", "1200", "-f", str(page), "-l", str(page),
                        "-x", "0", "-y", str(Y), "-W", "8500", "-H", str(H),
                        "-png", PDF, crop], capture_output=True, text=True)
    got = glob.glob(f"{crop}-*.png") or glob.glob(f"{crop}.png")
    # tesseract du crop (2e preuve)
    if got:
        subprocess.run(["tesseract", got[0], crop, "-l", "ara", "--psm", "4"],
                       env=env, capture_output=True)
    print(f"OK p{page} {tag} y300={y} -> {got[0] if got else 'FAIL'}")
    results.append(tag)
print("DONE", len(results))

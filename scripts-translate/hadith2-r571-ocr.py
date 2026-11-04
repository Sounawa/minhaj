# -*- coding: utf-8 -*-
"""R571 — hadith-2es pdf-26 (leçon 25, أحكام الصيام 3, p.171-176).
OCR tesseract ara 300 dpi ×6 pages + TSV (localisation crochets [8xx]) +
micro-crops 1200 dpi de chaque ligne à crochet + tesseract psm 7 par ligne."""
import subprocess, os, re, glob
import fitz

PDF = "/home/z/my-project/content/textbooks-src/hadith-2-iadadi_text.pdf"
OUT = "/home/z/my-project/tr-tmp/qa-crops-r571"
os.makedirs(OUT, exist_ok=True)
TESS = "scripts-translate/tessdata" if os.path.isdir("scripts-translate/tessdata") else "/usr/share/tesseract-ocr/4.00/tessdata"
doc = fitz.open(PDF)
PAGES = list(range(171, 177))

def ocr(png, psm="3"):
    r = subprocess.run(["tesseract", png, "stdout", "-l", "ara", "--psm", psm,
                        "--tessdata-dir", TESS, "-c", "preserve_interword_spaces=1"],
                       capture_output=True, text=True)
    return r.stdout

# 1) rendu 300 dpi + OCR pleine page + TSV
info = {}
for pno in PAGES:
    page = doc[pno - 1]
    pix = page.get_pixmap(matrix=fitz.Matrix(300/72, 300/72))
    png = f"{OUT}/p{pno}-300.png"
    pix.save(png)
    txt = ocr(png)
    open(f"{OUT}/p{pno}-ocr.txt", "w").write(txt)
    tsv = subprocess.run(["tesseract", png, "stdout", "-l", "ara", "--psm", "3",
                          "--tessdata-dir", TESS, "tsv"], capture_output=True, text=True).stdout
    lines = {}
    for row in tsv.splitlines()[1:]:
        c = row.split("\t")
        if len(c) < 12 or not c[11].strip():
            continue
        key = (c[2], c[3], c[4])  # block, par, line
        top = int(c[7]); h = int(c[9])
        e = lines.setdefault(key, {"top": top, "bot": top + h, "words": []})
        e["top"] = min(e["top"], top); e["bot"] = max(e["bot"], top + h)
        e["words"].append(c[11])
    info[pno] = list(lines.values())
    print(f"p{pno}: {len(txt)} car OCR, {len(lines)} lignes TSV")

# 2) lignes à crochet [8xx] → crop 1200 dpi + psm 7
print("\n=== CROCHETS [8xx] ===")
for pno, ls in info.items():
    for i, e in enumerate(ls):
        joined = " ".join(e["words"])
        m = re.search(r"\]?\s*8\s*([0-9\u0660-\u0669\u06F0-\u06F9]{2})\s*\]?", joined)
        if m:
            y0 = max(0, e["top"] - 6) * 72 / 300 - 2
            y1 = (e["bot"] + 6) * 72 / 300 + 2
            page = doc[pno - 1]
            clip = fitz.Rect(20, y0, 490, y1)
            pix = page.get_pixmap(matrix=fitz.Matrix(1200/72, 1200/72), clip=clip)
            png = f"{OUT}/t-p{pno}-L{i}-num.png"
            pix.save(png)
            ltxt = " ".join(ocr(png, "7").split())
            print(f"p{pno} L{i} y={e['top']}-{e['bot']}: {ltxt!r}")
            ls[i]["cropped"] = True

# 3) lignes citant عائشة / عاشوراء / جماعة / كفارة / عشرين / ستين → crops 900 dpi
KEYS = ["عائشة", "عاشور", "جماعة", "كفار", "عشرين", "ستين", "رسول الله", "نبي الله"]
print("\n=== LIGNES CLÉS ===")
for pno, ls in info.items():
    for i, e in enumerate(ls):
        if e.get("cropped"):
            continue
        joined = " ".join(e["words"])
        if any(k in joined for k in KEYS):
            y0 = max(0, e["top"] - 8) * 72 / 300 - 2
            y1 = (e["bot"] + 8) * 72 / 300 + 2
            page = doc[pno - 1]
            clip = fitz.Rect(20, y0, 490, y1)
            pix = page.get_pixmap(matrix=fitz.Matrix(900/72, 900/72), clip=clip)
            png = f"{OUT}/k-p{pno}-L{i}.png"
            pix.save(png)
            print(f"p{pno} L{i} y={e['top']}-{e['bot']}: {joined[:80]!r}")

print("\nDONE — crops dans", OUT)

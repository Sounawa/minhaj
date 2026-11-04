# -*- coding: utf-8 -*-
"""Localise un token sur une page 300dpi via TSV tesseract, imprime bbox 300dpi + crop 1200dpi."""
import subprocess, sys, os

TESS = "/home/z/my-project/scripts-translate/tessdata"
PAGES = "/home/z/my-project/tr-tmp/qa-crops-r571"

def tsv(page):
    base = f"{PAGES}/tsv-{page}"
    if not os.path.exists(base + ".tsv"):
        subprocess.run(["tesseract", f"{PAGES}/pg-{page}.png", base, "-l", "ara",
                        "--tessdata-dir", TESS, "tsv"], check=True,
                       stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    words = []
    with open(base + ".tsv", encoding="utf-8") as f:
        next(f)
        for ln in f:
            p = ln.rstrip("\n").split("\t")
            if len(p) == 12 and p[11].strip():
                words.append((p[11], int(p[6]), int(p[7]), int(p[8]), int(p[9])))
    return words

if __name__ == "__main__":
    page = sys.argv[1]
    token = sys.argv[2]
    if len(sys.argv) > 3 and sys.argv[3] == "crop":
        for w, x, y, W, H in tsv(page):
            if token in w:
                print(f"WORD {w!r} bbox300=({x},{y},{W},{H})")
                # crop 1200 dpi autour (x4 coords, marge 120 px 300dpi)
                m = 120
                cx, cy = max(0, (x - m) * 4), max(0, (y - m) * 4)
                cW, cH = (W + 2 * m) * 4, (H + 2 * m) * 4
                out = f"{PAGES}/mc-{page}-{token}-{x}.png"
                subprocess.run(["pdftoppm", "-f", page, "-l", page, "-r", "1200", "-png",
                                "-x", str(cx), "-y", str(cy), "-W", str(cW), "-H", str(cH),
                                "/home/z/my-project/content/textbooks-src/hadith-2-iadadi_text.pdf",
                                out[:-4]], check=True)
                r = subprocess.run(["tesseract", out, "stdout", "-l", "ara",
                                    "--tessdata-dir", TESS, "--psm", "7"],
                                   capture_output=True, text=True)
                print("OCR1200:", r.stdout.strip())
                r6 = subprocess.run(["tesseract", out, "stdout", "-l", "ara",
                                     "--tessdata-dir", TESS, "--psm", "6"],
                                    capture_output=True, text=True)
                print("OCR1200psm6:", " ".join(r6.stdout.split()))
    else:
        for w, x, y, W, H in tsv(page):
            if token in w:
                print(f"WORD {w!r} bbox300=({x},{y},{W},{H})")

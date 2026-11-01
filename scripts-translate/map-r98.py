#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""R98 — cartographie du manuel كتاب التفسير 3 إعدادي (174 p) :
détecte les débuts de leçons (أهداف الدرس) et les titres de sūras.
Usage : python3 scripts-translate/map-r98.py [première] [dernière]
Sortie complète : tr-tmp/map-tafsir3-r98.txt"""

import os
import re
import subprocess
import sys
from multiprocessing import Pool

PDF = "/home/z/my-project/tr-tmp/books/كتاب التفسير 3 إعدادي.pdf"
ENV = dict(os.environ)
ENV["TESSDATA_PREFIX"] = "/home/z/my-project/scripts-translate/tessdata"
OUT = "/home/z/my-project/tr-tmp/map-tafsir3-r98.txt"

SURS = ("الشورى", "الطلاق", "التحريم", "التحريم")


def ocr_page(i):
    import fitz
    doc = fitz.open(PDF)
    pix = doc[i].get_pixmap(dpi=110)
    png = f"/tmp/map98-p{i}.png"
    pix.save(png)
    doc.close()
    r = subprocess.run(["tesseract", png, "stdout", "-l", "ara", "--psm", "6"],
                       capture_output=True, text=True, env=ENV, timeout=120)
    os.remove(png)
    return i, (r.stdout or "")


def main():
    p1 = int(sys.argv[1]) - 1 if len(sys.argv) > 1 else 0
    p2 = int(sys.argv[2]) if len(sys.argv) > 2 else 174
    idx = list(range(p1, p2))
    lines_out = []
    with Pool(4) as pool:
        for i, txt in pool.imap_unordered(ocr_page, idx):
            head = " | ".join(ln.strip() for ln in txt.splitlines() if ln.strip()[:4])[:160]
            has_obj = "أهداف" in txt or "اهداف" in txt
            surs = [s for s in SURS if s in txt]
            ayat = re.findall(r"الآيات?\s*[:：]?\s*([\d\u0660-\u0669][\d\u0660-\u0669\s\-–—-]{0,12})", txt)
            tag = ("OBJ " if has_obj else "    ") + (",".join(surs) or "")
            line = f"p{i+1:>3} [{tag:<22}] ayat={ayat[:3]} :: {head[:110]}"
            lines_out.append((i, line, has_obj))
            if has_obj:
                print(line, flush=True)
    lines_out.sort()
    with open(OUT, "a", encoding="utf-8") as f:
        for _, ln, _ in lines_out:
            f.write(ln + "\n")


if __name__ == "__main__":
    main()

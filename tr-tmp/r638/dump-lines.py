#!/usr/bin/env python3
import fitz, sys
PDF = "/home/z/my-project/content/textbooks-src/hadith-3-iadadi_text.pdf"
doc = fitz.open(PDF)
for p in [int(a) for a in sys.argv[1:]]:
    d = doc[p-1].get_text("dict")
    print(f"===== PAGE {p} =====")
    for blk in d["blocks"]:
        if blk.get("type") != 0: continue
        for ln in blk["lines"]:
            t = "".join(s["text"] for s in ln["spans"]).strip()
            if t:
                print(f"y{ln['bbox'][1]:6.1f}-{ln['bbox'][3]:6.1f} | {t[:95]}")

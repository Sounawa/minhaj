#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""R94 — sonde de bordures : OCR rapide (150 dpi) des pages autour de p73 et p80
pour confirmer les débuts de leçons (أهداف الدرس) et les plages de versets."""
import os
import re
import subprocess
import sys

import fitz

PDF = "/tmp/tafsir2es-manual.pdf"
ENV = dict(os.environ)
ENV["TESSDATA_PREFIX"] = "/home/z/my-project/scripts-translate/tessdata"

pages = [int(x) for x in sys.argv[1:]] or [72, 73, 74, 79, 80, 81]

doc = fitz.open(PDF)
for p in pages:
    pix = doc[p - 1].get_pixmap(dpi=150)
    png = f"/tmp/bounds-p{p}.png"
    pix.save(png)
    r = subprocess.run(["tesseract", png, "stdout", "-l", "ara", "--psm", "6"],
                       capture_output=True, text=True, env=ENV, timeout=120)
    os.remove(png)
    txt = (r.stdout or "")
    lines = [ln.strip() for ln in txt.splitlines() if ln.strip()]
    has_obj = "أهداف" in txt or "اهداف" in txt
    ayat = re.findall(r"الآيات?\s*[:：]?\s*([\d\u0660-\u0669][\d\u0660-\u0669\s\-–—-]{0,12})", txt)
    # chiffres arabes orientaux -> occidentaux pour lisibilité
    ayat_w = [a.translate(str.maketrans("٠١٢٣٤٥٦٧٨٩", "0123456789")) for a in ayat]
    print(f"=== p{p} {'[أهداف الدرس]' if has_obj else ''} ayat={ayat_w[:4]}")
    for ln in lines[:14]:
        print("   ", ln[:110])
doc.close()

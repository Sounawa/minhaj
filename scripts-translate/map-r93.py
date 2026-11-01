#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""R93 — cartographie du manuel كتاب التفسير 2 إعدادي (210 p) :
détecte les débuts de leçons (أهداف الدرس) et les titres de sūras."""

import os
import re
import subprocess

import fitz

PDF = "/tmp/tafsir2es-manual.pdf"
ENV = dict(os.environ)
ENV["TESSDATA_PREFIX"] = "/home/z/my-project/scripts-translate/tessdata"

doc = fitz.open(PDF)
marks = []
for i in range(len(doc)):
    pix = doc[i].get_pixmap(dpi=110)
    png = f"/tmp/map-p{i}.png"
    pix.save(png)
    r = subprocess.run(["tesseract", png, "stdout", "-l", "ara", "--psm", "6"],
                       capture_output=True, text=True, env=ENV, timeout=90)
    os.remove(png)
    txt = r.stdout or ""
    head = " | ".join(ln.strip() for ln in txt.splitlines() if ln.strip()[:4])[:160]
    has_obj = "أهداف" in txt or "اهداف" in txt
    surs = [s for s in ("فاطر", "الحديد", "المجادلة") if s in txt]
    ayat = re.findall(r"الآيات?\s*[:：]?\s*([\d\u0660-\u0669][\d\u0660-\u0669\s\-–—-]{0,12})", txt)
    tag = ("OBJ " if has_obj else "    ") + (",".join(surs) or "")
    marks.append((i, tag, ayat[:3], head))
    print(f"p{i+1:>3} [{tag:<18}] ayat={ayat[:2]} :: {head[:110]}")
doc.close()

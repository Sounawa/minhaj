# -*- coding: utf-8 -*-
"""Minhāj — Localisation précise des étiquettes bleues [سورة الحج الآية N] sur
p.79/p.80 via spans fitz (positions texte), puis crops 900 dpi serrés pour
lecture VLM définitive des chiffres (٠ vs ٢, ١ vs ٣) et du nom de la sourate."""
import fitz
import os

PDF = "/home/z/my-project/content/textbooks-src/hadith-3-iadadi_text.pdf"
OUT = "/home/z/my-project/tr-tmp/qa-crops-r654"

doc = fitz.open(PDF)

for page_no in (79, 80):
    pg = doc[page_no - 1]
    print(f"\n===== PAGE {page_no} — spans « سورة / الآية / الحج / الموطأ » =====")
    d = pg.get_text("dict")
    hits = []
    for blk in d.get("blocks", []):
        for ln in blk.get("lines", []):
            for sp in ln.get("spans", []):
                t = sp.get("text", "")
                if any(k in t for k in ("سورة", "الآية", "الحج", "الموطأ", "رقم")):
                    hits.append((tuple(round(v, 1) for v in sp["bbox"]), sp["size"], t.strip()[:80]))
    for h in sorted(hits, key=lambda z: (z[0][1], z[0][0])):
        print(f"  bbox={h[0]} size={h[1]:.1f} text={h[2]}")

# -*- coding: utf-8 -*-
"""Minhāj — Localisation TSV des zones sensibles leçon 23 (pdf-24, R569).
Chaque cible : page, motif(s) tesseract TSV → coordonnées bbox imprimées
pour micro-crops 1200 dpi ultérieurs (aucune lecture devinée).
"""
import os
import subprocess

CROPS = "/home/z/my-project/tr-tmp/qa-crops-r569"
TESSDATA = "/home/z/my-project/scripts-translate/tessdata"
env = dict(os.environ, TESSDATA_PREFIX=TESSDATA)

TARGETS = {
    158: ["الزمر", "تعالى"],
    159: ["أرجو", "أجمع", "أنق"],
    160: ["مريم", "نحت", "العجاج"],
    161: ["النفل", "تسع", "فاقدروا"],
    162: ["عثمان", "ابتداء", "مالك"],
    163: ["بخير", "اختلام", "يدل", "أراهم"],
    164: ["الفطر", "ميد", "الزوال"],
}

for page, motifs in TARGETS.items():
    ts = f"{CROPS}/tess-page-{page}.tsv"
    if not os.path.exists(ts):
        subprocess.run(["tesseract", f"{CROPS}/page-{page}-300.png", f"{CROPS}/tmp-tsv",
                        "-l", "ara", "--psm", "4", "tsv"],
                       env=env, capture_output=True, text=True)
        os.replace(f"{CROPS}/tmp-tsv.tsv", ts)
    rows = open(ts, encoding="utf-8").read().splitlines()[1:]
    print(f"===== PAGE {page}")
    for m in motifs:
        hits = []
        for r in rows:
            c = r.split("\t")
            if len(c) >= 12 and m in c[11]:
                hits.append((c[6], c[7], c[8], c[9], c[11]))
        for h in hits[:6]:
            print(f"  {m}: x={h[0]} y={h[1]} w={h[2]} h={h[3]} «{h[4]}»")

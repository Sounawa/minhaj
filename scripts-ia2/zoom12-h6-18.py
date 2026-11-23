#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# IA-2 — zoom12-h6-18 : micro-crops complémentaires exécutés en ligne ce tour
# (z12 glose4-def / istikhlas-head2, z13 table-hdr4 + istikhl-head2 @3600,
# z14 binarisation canal bleu en-têtes, z15 table-hdr5 @3600, z16 tahlil-head)
# — consignés ici pour la traçabilité.
import subprocess
PDF = "/home/z/my-project/pdf-work/hadith-6ep.pdf"
Z = "/home/z/my-project/pdf-work/h6-15/zoom"
def crop(name, page, y0, y1, dpi):
    f = dpi / 600.0; W, H = int(5308 * f) + 40, int(6725 * f) + 40
    subprocess.run(["pdftoppm", "-f", str(page), "-l", str(page), "-r", str(dpi),
                    "-png", "-singlefile", "-x", "0", "-y", str(int(y0 * f)),
                    "-W", str(W), "-H", str(int((y1 - y0) * f)), PDF, f"{Z}/{name}"], check=True)
    print(name, "OK")
# z12 : glose 4 définition (PIL gauche) + bande استخلاص
crop("z12-p101-istikhl-head2", 101, 2880, 3075, 3600)
crop("z12-p104-table-hdr2", 104, 2500, 2840, 2400)
# z13 : en-têtes tableau @2400 + titre استخلاص @3600
crop("z13-p104-table-hdr3", 104, 2650, 2910, 2400)
crop("z13-p101-istikhl-head2", 101, 2880, 3075, 3600)
# z15 : en-têtes tableau @3600 (lecture psm11/6 : السلوك موقفي منها التعليل)
crop("z15-table-hdr5", 104, 2540, 2820, 3600)
# z16 : bande titre التحليل (bleu) p.101
crop("z16-p101-tahlil-head", 101, 3660, 4100, 2400)
print("OK zoom12-h6-18 (trace)")

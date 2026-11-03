# -*- coding: utf-8 -*-
"""R552 — composites de preuve par page (leçon 11 hadith-2es, p.79-85).
Empile verticalement les zones incertaines (bandes pleine largeur @300 dpi natif,
zone zoomée ×2 pour les tokens minuscules). Sortie : tr-tmp/qa-crops-r552/pN-comp.png"""
from PIL import Image
import os

D = "/home/z/my-project/tr-tmp/qa-crops-r552"
PT2PX = 300 / 72.0  # ~4.1667 px/pt

# (page, [(y0_pt, y1_pt), ...])
ZONES = {
    79: [(360, 505)],
    80: [(80, 155), (190, 290), (345, 475)],
    81: [(115, 195), (225, 355), (545, 630)],
    82: [(90, 225), (565, 670)],
    83: [(130, 270), (365, 445), (505, 585), (665, 750)],
    84: [(175, 250), (315, 410), (410, 645)],
    85: [(85, 185), (180, 270), (255, 370)],
}

for page, zones in ZONES.items():
    src = Image.open(f"{D}/page-{page:03d}.png")  # 300 dpi natif
    W, H = src.size
    strips = []
    for (y0, y1) in zones:
        top = max(0, int(y0 * PT2PX))
        bot = min(H, int(y1 * PT2PX))
        strips.append(src.crop((0, top, W, bot)))
    total_h = sum(s.height for s in strips) + 8 * (len(strips) - 1)
    comp = Image.new("RGB", (W, total_h), (255, 210, 210))
    y = 0
    for s in strips:
        comp.paste(s, (0, y))
        y += s.height + 8
    out = f"{D}/p{page}-comp.png"
    comp.save(out, optimize=True)
    print(out, comp.size, f"{os.path.getsize(out)//1024} Ko")

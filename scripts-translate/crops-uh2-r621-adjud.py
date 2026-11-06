#!/usr/bin/env python3
# R621 — recadrages d'adjudication leçon 8 ulum-hadith-tanawi-2 (pdf-mut23h2u-262)
# Zones douteuses : p.48 diagramme ; p.49 bas + p.50 haut (matn muhfuZ) ;
# p.50 (renvois Tirmidhi/Bukhari) ; p.51 haut (Khatib tail) + bas (Muqaddima ref).
import subprocess, os
from PIL import Image

SRC = "/home/z/my-project/content/textbooks-src/ulum-hadith-2-thanawi_text.pdf"
OUT = "/home/z/my-project/tr-tmp/qa-crops-r621"
os.makedirs(OUT, exist_ok=True)

ZONES = [
    # (page, dpi, top%, bottom%, nom)
    (48, 450, 0.28, 0.72, "ADJ1-p48-diagramme"),
    (49, 450, 0.55, 1.00, "ADJ2-p49-matn-muhfuz"),
    (50, 450, 0.00, 0.22, "ADJ3-p50-matn-suite"),
    (50, 450, 0.50, 0.92, "ADJ4-p50-renvois-tb"),
    (51, 450, 0.00, 0.30, "ADJ5-p51-khatib-tail"),
    (51, 450, 0.52, 1.00, "ADJ6-p51-istithmar"),
]

for page, dpi, t, b, name in ZONES:
    tmp = f"/tmp/uh2-p{page}"
    subprocess.run(["pdftoppm", "-f", str(page), "-l", str(page), "-r", str(dpi),
                    "-png", SRC, tmp], check=True)
    src = f"{tmp}-{page:03d}.png"
    im = Image.open(src)
    w, h = im.size
    crop = im.crop((0, int(h * t), w, int(h * b)))
    dst = os.path.join(OUT, f"{name}.png")
    crop.save(dst)
    print(name, crop.size, os.path.getsize(dst))
    os.remove(src)

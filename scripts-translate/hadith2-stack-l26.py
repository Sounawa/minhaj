# -*- coding: utf-8 -*-
"""Stack composites l26 (fix tuple unpack)."""
import glob, os
from PIL import Image
CROPS = "/home/z/my-project/tr-tmp/qa-crops-r571"

def stack(imgs, out, bg=(255, 220, 220)):
    if not imgs:
        print(f"SKIP {out} (vide)")
        return
    w = max(i.width for i in imgs)
    h = sum(i.height for i in imgs) + 12 * (len(imgs) - 1)
    canvas = Image.new("RGB", (w, h), bg)
    y = 0
    for i in imgs:
        canvas.paste(i, (0, y))
        y += i.height + 12
    canvas.save(out, quality=85)
    print(f"COMPOSITE {out} {w}x{h}")

# composites de nombres par page
for n in (177, 178, 181, 182):
    imgs = [Image.open(p) for p in sorted(glob.glob(f"{CROPS}/num-{n}-*.png"))]
    stack(imgs, f"{CROPS}/nums-{n}.png")

# composites de bandes par groupes de 3
band_files = sorted(glob.glob(f"{CROPS}/b-p*.png"))
for ci in range(0, len(band_files), 3):
    grp = band_files[ci:ci + 3]
    stack([Image.open(p) for p in grp], f"{CROPS}/comp-{chr(65 + ci // 3)}.jpg")
print("DONE")

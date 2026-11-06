# -*- coding: utf-8 -*-
"""R631 — recadrages de preuve pour la leçon 2 hadith-3es (slot pdf-mut23h2x-391).
Piles de bandes 600 dpi (p.17-24, 3 bandes par page) pour lecture VLM fidèle
+ zooms 900 dpi centrés sur les numéros de hadiths imprimés entre crochets
[الموطأ رقم: N] (preuve chiffre à chiffre, doctrine « jamais deviné »)
+ zoom p.17 bannière « الدرس 2 » (preuve de la borne inférieure).
Sortie : tr-tmp/qa-crops-r631/ (piles piles-pXX.png, zooms zoom-pYY-...png)."""
import fitz, re
from PIL import Image

PDF = "/home/z/my-project/content/textbooks-src/hadith-3-iadadi_text.pdf"
OUTDIR = "/home/z/my-project/tr-tmp/qa-crops-r631"
doc = fitz.open(PDF)

def save_clip(pno, y0, y1, dpi, name):
    pg = doc[pno - 1]
    pw = pg.rect.width
    pix = pg.get_pixmap(dpi=dpi, clip=fitz.Rect(0, max(0, y0), pw, min(pg.rect.height, y1)))
    path = f"{OUTDIR}/{name}.png"
    pix.save(path)
    return path

def pile(paths, name):
    ims = [Image.open(f) for f in paths]
    w = max(im.width for im in ims)
    h = sum(im.height for im in ims) + 10 * (len(ims) - 1)
    canvas = Image.new("RGB", (w, h), (255, 255, 255))
    y = 0
    for im in ims:
        canvas.paste(im, (0, y))
        y += im.height + 10
    canvas.save(f"{OUTDIR}/{name}.png")
    return f"{OUTDIR}/{name}.png"

# --- 1) bandes 600 dpi p.17-24 (3 bandes/page) + p.17 bannière ---
page_paths = {}
for p in range(17, 25):
    paths = [
        save_clip(p, 0, 255, 600, f"b-p{p}-a"),
        save_clip(p, 255, 510, 600, f"b-p{p}-b"),
        save_clip(p, 510, 765, 600, f"b-p{p}-c"),
    ]
    page_paths[p] = pile(paths, f"pile-p{p}")
    print("pile", p, page_paths[p])

# --- 2) zooms 900 dpi sur les numéros [الموطأ رقم: N] ---
def num_crops(p):
    pg = doc[p - 1]
    d = pg.get_text("dict")
    out = []
    for blk in d["blocks"]:
        if blk.get("type") != 0:
            continue
        for ln in blk["lines"]:
            t = "".join(s["text"] for s in ln["spans"])
            if "رقم" in t or re.search(r"\d{3}", t):
                y0, y1 = ln["bbox"][1], ln["bbox"][3]
                out.append((round(y0), round(y1), t[:60]))
    return out

for p in (18, 19, 20, 21, 22, 23, 24):
    hits = num_crops(p)
    paths = []
    for i, (y0, y1, t) in enumerate(hits):
        name = f"num-p{p}-{i}-y{y0}"
        paths.append(save_clip(p, y0 - 22, y1 + 22, 900, name))
        print(f"p.{p} zone y{y0}-{y1} :: {t}")
    if paths:
        pile(paths, f"pile-num-p{p}")

# --- 3) zoom 600 dpi bannière p.17 (preuve borne inférieure) ---
save_clip(17, 25, 200, 600, "banniere-p17")
save_clip(25, 25, 200, 600, "banniere-p25")
print("OK — recadrages dans", OUTDIR)

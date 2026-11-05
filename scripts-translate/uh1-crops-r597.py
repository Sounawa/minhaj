# -*- coding: utf-8 -*-
"""R597 — crops ciblés 600 dpi pour leçon pdf-mut23h2q-131 (le ḥadīṯ fard et
le ḥadīṯ muʿallal, p.99-103 de ulum-hadith-1-thanawi.pdf).
Calage R596 PROUVÉ : docId = page PDF = page imprimée (offset 0) → PDF 99-103.
Méthode R596 : TSV tesseract (boîtes de mots) → bandes 600 dpi → composites.
Sortie : tr-tmp/qa-crops-r597/comp-*.png (zéro vision API — lecture locale).
"""
import os
import subprocess

HOME = "/home/z/my-project"
PDF = f"{HOME}/content/textbooks-src/ulum-hadith-1-thanawi.pdf"
OUT = f"{HOME}/tr-tmp/qa-crops-r597"
TESS = f"{HOME}/scripts-translate/tessdata"

# page imprimée -> [(kw, pad_haut600, pad_bas600), ...]
TARGETS = {
    99: [("عرفا", 780, 220), ("علوم", 160, 500)],
    100: [("بثقة", 420, 520), ("صفيّة", 320, 520)],
    101: [("فاتحة", 400, 420), ("خفاء", 300, 560), ("غريب", 340, 400)],
    102: [("مجلس", 520, 580), ("إسماعيل", 400, 380), ("الحفظ", 240, 360)],
    103: [("تعريف", 300, 400), ("الترمذي", 420, 560),
          ("التبصرة", 200, 260), ("معنى", 280, 420)],
}


def render(idx1: int, dpi: int, name: str) -> str:
    import fitz
    doc = fitz.open(PDF)
    page = doc[idx1 - 1]
    pix = page.get_pixmap(dpi=dpi)
    png = f"{OUT}/{name}.png"
    pix.save(png)
    doc.close()
    return png


def tsv_zones(png300: str, kws: list) -> list:
    r = subprocess.run(["tesseract", png300, "stdout", "-l", "ara", "--psm", "6",
                        "--tessdata-dir", TESS, "tsv"],
                       capture_output=True, text=True, timeout=90)
    zones = []
    for line in (r.stdout or "").splitlines()[1:]:
        p = line.split("\t")
        if len(p) < 12:
            continue
        word = p[11].strip()
        for kw, _, _ in kws:
            if kw in word:
                zones.append({"kw": kw, "top": int(p[7]), "h": int(p[9])})
                break
    return zones


def main() -> None:
    from PIL import Image
    os.makedirs(OUT, exist_ok=True)
    for printed, kws in TARGETS.items():
        png300 = render(printed, 300, f"p{printed}-300")
        zones = tsv_zones(png300, kws)
        print(f"p{printed} zones:", [(z["kw"], z["top"]) for z in zones])
        im600 = Image.open(render(printed, 600, f"p{printed}-600"))
        h600 = im600.height
        bands = []
        for z in zones:
            pad_up, pad_dn = next((pu, pd) for k, pu, pd in kws if k == z["kw"])
            y0 = max(0, z["top"] * 2 - pad_up)
            y1 = min(h600, (z["top"] + z["h"]) * 2 + pad_dn)
            bands.append([y0, y1])
        bands.sort()
        merged = []
        for b in bands:
            if merged and b[0] <= merged[-1][1] + 40:
                merged[-1][1] = max(merged[-1][1], b[1])
            else:
                merged.append(b)
        crops = []
        for i, (y0, y1) in enumerate(merged):
            crop = im600.crop((0, y0, im600.width, y1))
            path = f"{OUT}/p{printed}-zone{i}.png"
            crop.save(path)
            crops.append(path)
            print(f"  crop {path} ({crop.width}x{crop.height})")
        # composite : empilement vertical, séparateur blanc
        if crops:
            ims = [Image.open(p) for p in crops]
            sep = 30
            tot = sum(i.height for i in ims) + sep * (len(ims) - 1)
            comp = Image.new("RGB", (ims[0].width, tot), (255, 255, 255))
            y = 0
            for i in ims:
                comp.paste(i, (0, y))
                y += i.height + sep
            name = f"comp-{printed}-r597.png"
            comp.save(f"{OUT}/{name}")
            print(f"  → {OUT}/{name} {comp.size}")
    print("R597 crops terminé")


if __name__ == "__main__":
    main()

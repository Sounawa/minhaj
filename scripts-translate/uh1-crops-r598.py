# -*- coding: utf-8 -*-
"""R598 — crops/zooms ciblés pour leçon pdf-mut23h2q-132 (le ḥadīṯ muḍṭarib,
p.104-107 de ulum-hadith-1-thanawi.pdf). Calage R596 PROUVÉ : docId = page PDF
= page imprimée (offset 0). TSV 300 dpi → bandes 1200 dpi (moitiés R/L) →
composites compZ-*.png. Zéro vision API — lecture locale."""
import os
import subprocess

HOME = "/home/z/my-project"
PDF = f"{HOME}/content/textbooks-src/ulum-hadith-1-thanawi.pdf"
OUT = f"{HOME}/tr-tmp/qa-crops-r598"
TESS = f"{HOME}/scripts-translate/tessdata"

# page -> [(etiquette, kw, ordre, pad_haut1200, pad_bas1200)]
TARGETS = {
    104: [("vers", "الفن", 0, 300, 350), ("glosse", "أهيل", 0, 200, 350)],
    105: [("istih", "المقصود", 0, 380, 350), ("vers", "الفن", 0, 250, 350),
          ("mthal", "مرفوعا", 0, 220, 520)],
    106: [("darq", "إسحاق", 0, 520, 600), ("tirm", "الشعبي", 0, 280, 480),
          ("ibnm", "بلفظ", 0, 420, 320), ("aour", "الأعور", 0, 420, 720)],
    107: [("istq", "أتأمل", 0, 200, 420), ("idad", "الإدراج", 0, 380, 320)],
}


def strip_diac(s):
    return "".join(ch for ch in s
                   if not (0x064B <= ord(ch) <= 0x0652 or ord(ch) == 0x0670))


def tsv(png300):
    r = subprocess.run(["tesseract", png300, "stdout", "-l", "ara", "--psm", "6",
                        "--tessdata-dir", TESS, "tsv"],
                       capture_output=True, text=True, timeout=90)
    words = []
    for line in (r.stdout or "").splitlines()[1:]:
        p = line.split("\t")
        if len(p) < 12:
            continue
        w = p[11].strip()
        if w:
            words.append({"w": w, "sw": strip_diac(w), "top": int(p[7]),
                          "h": int(p[9]), "left": int(p[6]), "width": int(p[8])})
    return words


def main():
    from PIL import Image
    import fitz
    import warnings
    warnings.simplefilter("ignore")
    os.makedirs(OUT, exist_ok=True)
    doc = fitz.open(PDF)
    for printed, specs in TARGETS.items():
        png300 = f"{OUT}/p{printed}-300.png"
        if not os.path.exists(png300):
            doc[printed - 1].get_pixmap(dpi=300).save(png300)
        words = tsv(png300)
        p1200 = f"{OUT}/p{printed}-1200.png"
        if not os.path.exists(p1200):
            doc[printed - 1].get_pixmap(dpi=1200).save(p1200)
        im = Image.open(p1200)
        strips = []
        for label, kw, order, pad_up, pad_dn in specs:
            kws = strip_diac(kw)
            hits = [w for w in words if kws in w["sw"]]
            if not hits:
                print(f"p{printed} {label} kw {kw!r} INTROUVABLE")
                continue
            z = hits[order]
            y0 = max(0, z["top"] * 4 - pad_up)
            y1 = min(im.height, (z["top"] + z["h"]) * 4 + pad_dn)
            # deux moitiés R/L pour rester lisible à 1200 dpi
            mid = im.width // 2
            for half, (x0, x1) in (("r", (mid, im.width)), ("l", (0, mid))):
                crop = im.crop((x0, y0, x1, y1))
                strips.append(crop)
            print(f"p{printed} {label} y{y0//4}-{y1//4} (300dpi)")
        if strips:
            wmax = max(c.width for c in strips)
            tot = sum(c.height for c in strips) + 40 * (len(strips) - 1)
            comp = Image.new("RGB", (wmax, tot), (255, 255, 255))
            y = 0
            for c in strips:
                comp.paste(c, (0, y))
                y += c.height + 40
            name = f"{OUT}/compZ-{printed}-r598.png"
            comp.save(name)
            print(f"  → {name} {comp.size}")
    doc.close()
    print("R598 crops terminé")


if __name__ == "__main__":
    main()

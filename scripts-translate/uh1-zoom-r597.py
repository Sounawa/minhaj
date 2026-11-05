# -*- coding: utf-8 -*-
"""R597 — zooms 1200 dpi par moitiés de ligne pour zones ambiguës (pdf-131).
Méthode : TSV 300 dpi localise la ligne (kw), bbox union des mots de la ligne,
rendu 1200 dpi, rognage par moitiés droite/gauche, empilement en compZ-*.png.
Zéro vision API — lecture locale des composites."""
import os
import subprocess

HOME = "/home/z/my-project"
PDF = f"{HOME}/content/textbooks-src/ulum-hadith-1-thanawi.pdf"
OUT = f"{HOME}/tr-tmp/qa-crops-r597"
TESS = f"{HOME}/scripts-translate/tessdata"

# page -> [(etiquette, kw, ordre, moitie 'r'|'l'|'f')]
TARGETS = {
    99: [("bannL1", "جنع", 0, "r"), ("bannL1", "جنع", 0, "l"),
         ("bannL2", "عرفا", 0, "r"), ("bannL2", "عرفا", 0, "l"),
         ("question", "حقيقة", 0, "f")],
    100: [("vers", "جنع", 0, "r"), ("vers", "جنع", 0, "l"),
          ("glosse", "بكذاء", 0, "f"), ("msth", "صفي", 0, "r"),
          ("msth", "صفي", 0, "l")],
    101: [("khadri", "الخدري", 0, "f"),
          ("vers", "غموض", 0, "r"), ("vers", "غموض", 0, "l")],
    103: [("bayt", "العراقي", 0, "r"), ("bayt", "العراقي", 0, "l"),
          ("charh", "البيت", 0, "r"), ("charh", "البيت", 0, "l"),
          ("charh", "التبصرة", 0, "r"), ("charh", "التبصرة", 0, "l")],
}


def strip_diac(s: str) -> str:
    return "".join(ch for ch in s
                   if not (0x064B <= ord(ch) <= 0x0652 or ord(ch) == 0x0670))


def tsv(png300: str) -> list:
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


def main() -> None:
    from PIL import Image
    import fitz
    os.makedirs(OUT, exist_ok=True)
    doc = fitz.open(PDF)
    for printed, specs in TARGETS.items():
        png300 = f"{OUT}/p{printed}-300.png"
        if not os.path.exists(png300):
            doc[printed - 1].get_pixmap(dpi=300).save(png300)
        words = tsv(png300)
        # rendu 1200 dpi une fois par page
        p1200 = f"{OUT}/p{printed}-1200.png"
        if not os.path.exists(p1200):
            doc[printed - 1].get_pixmap(dpi=1200).save(p1200)
        im = Image.open(p1200)
        strips = []
        for label, kw, order, half in specs:
            kws = strip_diac(kw)
            hits = [w for w in words if kws in w["sw"]]
            if not hits:
                print(f"p{printed} {label} kw {kw!r} INTROUVABLE")
                continue
            z = hits[order]
            line = [w for w in words if abs(w["top"] - z["top"]) <= 28]
            x0 = min(w["left"] for w in line)
            x1 = max(w["left"] + w["width"] for w in line)
            mid = (x0 + x1) // 2
            y0, y1 = z["top"] - 40, z["top"] + z["h"] + 40
            if half == "r":
                box = (mid, y0, x1 + 60, y1)
            elif half == "l":
                box = (max(0, x0 - 60), y0, mid, y1)
            else:
                box = (max(0, x0 - 60), y0, min(im.width // 4, x1 + 60), y1)
            crop = im.crop(tuple(c * 4 for c in box))
            strips.append((label + "-" + half, crop))
            print(f"p{printed} {label}-{half} bbox300={box} → {crop.size}")
        if strips:
            wmax = max(c.width for _, c in strips)
            tot = sum(c.height for _, c in strips) + 40 * (len(strips) - 1)
            comp = Image.new("RGB", (wmax, tot), (255, 255, 255))
            y = 0
            for _, c in strips:
                comp.paste(c, ((wmax - c.width) // 2, y))
                y += c.height + 40
            name = f"{OUT}/compZ-{printed}-r597.png"
            comp.save(name)
            print(f"  → {name} {comp.size}")
    doc.close()
    print("R597 zooms terminé")


if __name__ == "__main__":
    main()

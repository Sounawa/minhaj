# -*- coding: utf-8 -*-
"""R596 — crops ciblés 600 dpi pour leçons pdf-mut23h2q-130 (p.95-98).
Cale les zones via tesseract TSV (boîtes de mots) puis rogne à 600 dpi.
Sortie : tr-tmp/qa-crops-r596/*.png + composite par page (empilés).
"""
import json
import os
import subprocess
import sys

HOME = "/home/z/my-project"
PDF = f"{HOME}/content/textbooks-src/ulum-hadith-1-thanawi.pdf"
OUT = f"{HOME}/tr-tmp/qa-crops-r596"
TESS = f"{HOME}/scripts-translate/tessdata"

# page imprimée -> index PDF (base 1) ; sondage : imprimé = PDF - 34
# (pdf-129 = imprimé 91-94 ; à caler : p95 imprimé cherché autour de PDF 129)
TARGETS = {
    95: {"kw": ["قسمان", "المقلوب", "فما هو"]},
    96: {"kw": ["قسمان", "المقلوب"]},
    97: {"kw": ["العراقي", "هريرة", "البخاري"]},
    98: {"kw": ["الاستثمار", "النزهة"]},
}


def find_pdf_page(printed: int) -> int:
    """Tente d'identifier l'index PDF de la page imprimée par OCR du bandeau."""
    import fitz
    doc = fitz.open(PDF)
    for idx in range(printed + 25, printed + 45):
        page = doc[idx - 1]
        pix = page.get_pixmap(dpi=120)
        png = f"{OUT}/probe-{idx}.png"
        pix.save(png)
        r = subprocess.run(["tesseract", png, "stdout", "-l", "ara", "--psm", "6",
                            "--tessdata-dir", TESS],
                           capture_output=True, text=True, timeout=40)
        txt = r.stdout or ""
        digits = "".join(ch for ch in txt if ch.isdigit())
        if f"أهداف" in txt or "الشرح" in txt or "التقويم" in txt:
            # heuristique : le numéro imprimé apparaît dans les 400 premiers car
            head = txt[:400]
            dd = "".join(ch for ch in head if ch.isdigit())
            if dd:
                return idx, int(dd[:2]) if len(dd) >= 2 else -1
    return -1, -1


def render(idx1: int, dpi: int, name: str) -> str:
    import fitz
    doc = fitz.open(PDF)
    page = doc[idx1 - 1]
    pix = page.get_pixmap(dpi=dpi)
    png = f"{OUT}/{name}.png"
    pix.save(png)
    return png


def tsv_zones(png300: str, kws: list) -> list:
    r = subprocess.run(["tesseract", png300, "stdout", "-l", "ara", "--psm", "6",
                        "--tessdata-dir", TESS, "tsv"],
                       capture_output=True, text=True, timeout=60)
    zones = []
    for line in (r.stdout or "").splitlines()[1:]:
        p = line.split("\t")
        if len(p) < 12:
            continue
        word = p[11].strip()
        for kw in kws:
            if kw in word:
                zones.append({"kw": kw, "top": int(p[7]), "h": int(p[9]),
                              "left": int(p[6]), "width": int(p[8])})
                break
    return zones


def main() -> None:
    os.makedirs(OUT, exist_ok=True)
    # 1) calage offset : chercher l'imprimé 95
    idx, _ = find_pdf_page(95)
    if idx < 0:
        print("CALAGE ÉCHEC")
        sys.exit(1)
    offset = idx - 95
    print(f"CALAGE : imprimé 95 = PDF {idx} → offset imprimé+{offset}")
    # 2) rendus 300 dpi + TSV + crops 600 dpi (facteur 2)
    for printed, spec in TARGETS.items():
        idx1 = printed + offset
        png300 = render(idx1, 300, f"p{printed}-300")
        zones = tsv_zones(png300, spec["kw"])
        print(f"p{printed} (PDF {idx1}) zones:", json.dumps(zones, ensure_ascii=False))
        from PIL import Image
        im = Image.open(png300)
        w, h = im.size
        bands = []
        for z in zones:
            y0 = max(0, int(z["top"] * 2) - 260)
            y1 = min(h * 2, int((z["top"] + z["h"]) * 2) + 420)
            bands.append((y0, y1))
        if not bands:
            bands = [(0, h * 2 // 3)]
        # fusion des bandes qui se chevauchent, puis crop en 600 dpi
        bands.sort()
        merged = []
        for b in bands:
            if merged and b[0] <= merged[-1][1]:
                merged[-1] = (merged[-1][0], max(merged[-1][1], b[1]))
            else:
                merged.append(list(b) if isinstance(b, tuple) else b)
        im600 = render(idx1, 600, f"p{printed}-600")
        im6 = Image.open(im600)
        n = 0
        for (y0, y1) in merged:
            crop = im6.crop((0, y0, im6.width, y1))
            path = f"{OUT}/p{printed}-zone{n}.png"
            crop.save(path)
            print(f"  crop → {path} ({crop.width}x{crop.height})")
            n += 1


if __name__ == "__main__":
    main()

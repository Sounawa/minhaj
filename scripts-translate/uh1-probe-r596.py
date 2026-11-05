# -*- coding: utf-8 -*-
"""R596 — sonde de cartographie ulum-hadith-tanawi-1 (recycle sandbox 05-11 :
caches tr-tmp effacés, re-OCR depuis content/textbooks-src/ulum-hadith-1-thanawi.pdf).

Usage : python3 scripts-translate/uh1-probe-r596.py <start> <end> <step> [dpi]
  start/end : indices PDF (base 1) inclusifs ; step : pas ; dpi : 150 défaut.
Lit le BANDEAU (top 12 %) de chaque page : numéro de page imprimé (chiffres
arabo-indiques → latins) + détection « أهداف الدرس » (début de leçon) + درس N.
Cache crash-safe par page : tr-tmp/uh1-ocr/banner-p<idx>.json.
Jamais de déduction de bornes : la borne supérieure se tranche AU SONDAGE IMAGE
si l'OCR est ambigu (méthode R535-R547, chiffres souvent inversés par paires).
"""
import json
import os
import subprocess
import sys

HOME = "/home/z/my-project"
PDF = f"{HOME}/content/textbooks-src/ulum-hadith-1-thanawi.pdf"
CACHE = f"{HOME}/tr-tmp/uh1-ocr"
TESS = f"{HOME}/scripts-translate/tessdata"

AR_DIGITS = str.maketrans("٠١٢٣٤٥٦٧٨٩", "0123456789")


def ocr(png: str, psm: str) -> str:
    env = dict(os.environ)
    try:
        r = subprocess.run(
            ["tesseract", png, "stdout", "-l", "ara", "--psm", psm,
             "--tessdata-dir", TESS],
            capture_output=True, text=True, timeout=60, env=env)
        return r.stdout or ""
    except Exception:
        return ""


def page_banner(idx1: int, dpi: int) -> dict:
    """idx1 : index base 1 (page.get_pixmap reçoit idx1-1)."""
    import fitz
    doc = fitz.open(PDF)
    page = doc[idx1 - 1]
    pix = page.get_pixmap(dpi=dpi)
    png = f"{CACHE}/full-p{idx1}.png"
    pix.save(png)
    # bandeau = top 12 %
    top = pix.height // 8  # 12.5 %
    out_png = f"{CACHE}/ban-p{idx1}.png"
    subprocess.run(["python3", "-c",
                    f"from PIL import Image; im=Image.open({png!r}); "
                    f"im.crop((0,0,im.width,{top})).save({out_png!r})"],
                   check=True, timeout=30)
    txt6 = ocr(out_png, "6")
    txt4 = ocr(out_png, "4") if "أهداف" not in txt6 else txt6
    txt = txt6 + "\n" + txt4
    digits = "".join(ch for ch in txt.translate(AR_DIGITS) if ch.isdigit())
    res = {
        "pdfPage": idx1,
        "printedDigits": digits[:4],
        "ahdaf": "أهداف" in txt,
        "dars": ("درس" in txt),
        "rawHead": " ".join(txt.split())[:180],
    }
    with open(f"{CACHE}/banner-p{idx1}.json", "w", encoding="utf-8") as fh:
        json.dump(res, fh, ensure_ascii=False, indent=1)
    return res


def main() -> None:
    os.makedirs(CACHE, exist_ok=True)
    start, end = int(sys.argv[1]), int(sys.argv[2])
    step = int(sys.argv[3]) if len(sys.argv) > 3 else 1
    dpi = int(sys.argv[4]) if len(sys.argv) > 4 else 150
    for idx in range(start, end + 1, step):
        cpath = f"{CACHE}/banner-p{idx}.json"
        if os.path.exists(cpath):
            with open(cpath, encoding="utf-8") as fh:
                res = json.load(fh)
            if res.get("dpi") == dpi:
                res["cached"] = True
                print(json.dumps(res, ensure_ascii=False))
                continue
        res = page_banner(idx, dpi)
        res["dpi"] = dpi
        print(json.dumps(res, ensure_ascii=False))


if __name__ == "__main__":
    main()

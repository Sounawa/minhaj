# -*- coding: utf-8 -*-
"""R597 — zoom ULTRA 2400 dpi du mot critique après «ما» du vers du fard
(p99 bannière + p100 corps) + comptage de points corrigé.
ف/ق : points AU-DESSUS de la tête (ف=1, ق=2) — R597-1 comptait en-dessous (bug).
Lettre médiane : ي=2 points SOUS la ligne, ب=1, ل=0.
Sortie : word-99-2400.png, word-100-2400.png, bannL1-1600.png, tisir-1600.png
+ impressions de comptage (preuve mathématique, zéro vision)."""
import subprocess
import os

HOME = "/home/z/my-project"
PDF = f"{HOME}/content/textbooks-src/ulum-hadith-1-thanawi.pdf"
OUT = f"{HOME}/tr-tmp/qa-crops-r597"
TESS = f"{HOME}/scripts-translate/tessdata"


def strip_diac(s: str) -> str:
    return "".join(ch for ch in s
                   if not (0x064B <= ord(ch) <= 0x0652 or ord(ch) == 0x0670))


def tsv_words(png: str) -> list:
    r = subprocess.run(["tesseract", png, "stdout", "-l", "ara", "--psm", "6",
                        "--tessdata-dir", TESS, "tsv"],
                       capture_output=True, text=True, timeout=120)
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


def render_clip(page_idx: int, dpi: int, box300, name: str):
    """rend ONLY the bbox (coords 300dpi) at `dpi` via clip — pas de page entière."""
    import fitz
    doc = fitz.open(PDF)
    page = doc[page_idx]
    k = 72.0 / 300.0  # 300dpi px -> points PDF
    r = fitz.Rect(box300[0] * k, box300[1] * k, box300[2] * k, box300[3] * k)
    pix = page.get_pixmap(dpi=dpi, clip=r)
    pix.save(f"{OUT}/{name}.png")
    doc.close()
    return (pix.width, pix.height)


def count_blobs(img, x0, x1, y0, y1, smin=16, smax=4000):
    """composantes 8-connexes sombres dans la zone (pixel 2400dpi)."""
    im = img.convert("L")
    W, H = im.size
    x0, x1 = max(0, x0), min(W, x1)
    y0, y1 = max(0, y0), min(H, y1)
    px = im.load()
    seen = set()
    blobs = []
    for y in range(y0, y1):
        for x in range(x0, x1):
            if px[x, y] < 128 and (x, y) not in seen:
                stack = [(x, y)]
                seen.add((x, y))
                minx = maxx = x
                miny = maxy = y
                n = 0
                while stack:
                    cx, cy = stack.pop()
                    n += 1
                    minx, maxx = min(minx, cx), max(maxx, cx)
                    miny, maxy = min(miny, cy), max(maxy, cy)
                    for dx in (-1, 0, 1):
                        for dy in (-1, 0, 1):
                            nx, ny = cx + dx, cy + dy
                            if (x0 <= nx < x1 and y0 <= ny < y1
                                    and px[nx, ny] < 128
                                    and (nx, ny) not in seen):
                                seen.add((nx, ny))
                                stack.append((nx, ny))
                if smin <= n <= smax:
                    blobs.append((minx, miny, maxx, maxy, n))
    return blobs


def main() -> None:
    from PIL import Image

    # ---- p99 bannière : ligne du vers 1 (token fusionné والقرد+ما+قيّدته) ----
    w99 = tsv_words(f"{OUT}/p99-300.png")
    tok99 = [w for w in w99 if "القرد" in w["sw"] or "قيدته" in w["sw"]]
    print("p99 tokens candidats:", [(t["w"], t["left"], t["width"]) for t in tok99])
    if tok99:
        t = tok99[0]
        # قيّدته ≈ 45 % gauches du token fusionné ; ما juste avant
        x_word = t["left"]
        w_word = int(t["width"] * 0.45)
        y_top, y_bot = t["top"] - 18, t["top"] + t["h"] + 18
        box99 = (x_word, y_top, x_word + w_word, y_bot)
        sz = render_clip(98, 2400, box99, "word-99-2400")
        print(f"word-99-2400.png {sz} box300={box99}")
        img = Image.open(f"{OUT}/word-99-2400.png")
        W, H = img.size
        # RTL : première lettre = droite (ق/ف) ~ 30 % de droite ; points AU-DESSUS
        first_x0, first_x1 = int(W * 0.70), W
        above = count_blobs(img, first_x0, first_x1, 0, int(H * 0.55))
        print(f"  p99 première lettre zone x[{first_x0},{W}] HAUT : "
              f"{len(above)} blobs -> {'ف(1)' if len(above) == 1 else 'ق(2)' if len(above) == 2 else 'INCONNU'}")
        for b in above:
            print("    ", b)
        # lettre médiane (ي/ل/ب) : bande 30-58 % depuis la droite, SOUS la ligne
        mid_x0, mid_x1 = int(W * 0.42), int(W * 0.70)
        below = count_blobs(img, mid_x0, mid_x1, int(H * 0.62), H)
        print(f"  p99 lettre médiane zone x[{mid_x0},{mid_x1}] BAS : "
              f"{len(below)} blobs -> {'ل(0)' if len(below) == 0 else 'ب(1)' if len(below) == 1 else 'ي(2)' if len(below) == 2 else 'INCONNU'}")
        for b in below:
            print("    ", b)

    # ---- p100 corps : mot séparé فَيُدْتَهُ ----
    w100 = tsv_words(f"{OUT}/p100-300.png")
    tok100 = [w for w in w100 if w["sw"] in ("فيوده", "فيذته", "قيده", "قيدته")
              or "يده" in w["sw"] or "يدته" in w["sw"]]
    print("p100 tokens candidats:", [(t["w"], t["left"], t["width"]) for t in tok100])
    if tok100:
        t = tok100[0]
        box100 = (t["left"] - 8, t["top"] - 18,
                  t["left"] + t["width"] + 8, t["top"] + t["h"] + 18)
        sz = render_clip(99, 2400, box100, "word-100-2400")
        print(f"word-100-2400.png {sz} box300={box100}")
        img = Image.open(f"{OUT}/word-100-2400.png")
        W, H = img.size
        first_x0, first_x1 = int(W * 0.70), W
        above = count_blobs(img, first_x0, first_x1, 0, int(H * 0.55))
        print(f"  p100 première lettre zone x[{first_x0},{W}] HAUT : "
              f"{len(above)} blobs -> {'ف(1)' if len(above) == 1 else 'ق(2)' if len(above) == 2 else 'INCONNU'}")
        for b in above:
            print("    ", b)
        mid_x0, mid_x1 = int(W * 0.42), int(W * 0.70)
        below = count_blobs(img, mid_x0, mid_x1, int(H * 0.62), H)
        print(f"  p100 lettre médiane zone x[{mid_x0},{mid_x1}] BAS : "
              f"{len(below)} blobs -> {'ل(0)' if len(below) == 0 else 'ب(1)' if len(below) == 1 else 'ي(2)' if len(below) == 2 else 'INCONNU'}")
        for b in below:
            print("    ", b)

    # ---- p99 bannière : vers 1 ENTIER à 1600 dpi (lecture propre) ----
    if tok99:
        t = tok99[0]
        line = [w for w in w99 if abs(w["top"] - t["top"]) <= 30]
        x0 = min(w["left"] for w in line)
        x1 = max(w["left"] + w["width"] for w in line)
        y0, y1 = t["top"] - 30, t["top"] + t["h"] + 30
        sz = render_clip(98, 1600, (x0 - 20, y0, x1 + 20, y1), "bannL1-1600")
        print(f"bannL1-1600.png {sz}")

    # ---- p101 : ligne «وما تيسر» à 1600 dpi (معه ? sans معه ?) ----
    w101 = tsv_words(f"{OUT}/p101-300.png")
    tok101 = [w for w in w101 if "تيسر" in w["sw"] or "نقرا" in w["sw"]
              or "فاتحة" in w["sw"]]
    print("p101 tokens candidats:", [(t["w"], t["left"], t["width"]) for t in tok101])
    if tok101:
        t = tok101[0]
        line = [w for w in w101 if abs(w["top"] - t["top"]) <= 30]
        x0 = min(w["left"] for w in line)
        x1 = max(w["left"] + w["width"] for w in line)
        y0, y1 = t["top"] - 30, t["top"] + t["h"] + 30
        sz = render_clip(100, 1600, (x0 - 20, y0, x1 + 20, y1), "tisir-1600")
        print(f"tisir-1600.png {sz}")


if __name__ == "__main__":
    main()

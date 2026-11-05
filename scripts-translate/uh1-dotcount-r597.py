# -*- coding: utf-8 -*-
"""R597 — adjudication ف/ق par comptage de points (composantes connexes).
ف = 1 point sous la tête ; ق = 2 points. Zone : mot après « ما » du vers.
p100 vers y~1831-1980 ; p99 bannière y~2540-2660 (300 dpi)."""
import subprocess

TESS = "/home/z/my-project/scripts-translate/tessdata"
OUT = "/home/z/my-project/tr-tmp/qa-crops-r597"


def strip_diac(s):
    return "".join(ch for ch in s
                   if not (0x064B <= ord(ch) <= 0x0652 or ord(ch) == 0x0670))


def word_box(png300, kw_line, idx_from_right):
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
            words.append({"w": w, "top": int(p[7]), "h": int(p[9]),
                          "left": int(p[6]), "width": int(p[8])})
    z = next(w for w in words if strip_diac(kw_line) in strip_diac(w["w"]))
    line = sorted([w for w in words if abs(w["top"] - z["top"]) <= 28],
                  key=lambda w: -w["left"])  # ordre RTL : droite -> gauche
    tgt = line[idx_from_right]
    print(f"  mots de la ligne : {[w['w'] for w in line]}")
    print(f"  cible = {tgt['w']!r} bbox=({tgt['left']},{tgt['top']},"
          f"{tgt['left']+tgt['width']},{tgt['top']+tgt['h']})")
    return tgt


def count_dots(png1200, box300, y_ratio=0.45):
    from PIL import Image
    import warnings
    warnings.simplefilter("ignore")
    im = Image.open(png1200).convert("L")
    x0, y0, x1, y1 = [c * 4 for c in box300]
    crop = im.crop((x0, y0, x1, y1))
    px = crop.load()
    w, h = crop.size
    # binariser
    dark = [[1 if px[x, y] < 128 else 0 for x in range(w)] for y in range(h)]
    # zone des points : sous 45 % de hauteur (sous la tête), sur toute la largeur
    ystart = int(h * y_ratio)
    seen = [[False] * w for _ in range(h)]
    blobs = []
    for y in range(ystart, h):
        for x in range(w):
            if dark[y][x] and not seen[y][x]:
                stack = [(x, y)]
                seen[y][x] = True
                minx, maxx, miny, maxy, n = x, x, y, y, 0
                while stack:
                    cx, cy = stack.pop()
                    n += 1
                    minx, maxx = min(minx, cx), max(maxx, cx)
                    miny, maxy = min(miny, cy), max(maxy, cy)
                    for dx in (-1, 0, 1):
                        for dy in (-1, 0, 1):
                            nx, ny = cx + dx, cy + dy
                            if (0 <= nx < w and 0 <= ny < h and dark[ny][nx]
                                    and not seen[ny][nx]):
                                seen[ny][nx] = True
                                stack.append((nx, ny))
                if 4 <= n <= 400:  # un point fait ~10-25 px de côté à 1200 dpi
                    blobs.append((minx, miny, maxx, maxy, n))
    blobs.sort(key=lambda b: (b[1], b[0]))
    print(f"  blobs sous la tête : {len(blobs)}")
    for b in blobs:
        print(f"    x{b[0]}-{b[2]} y{b[1]}-{b[3]} surf{b[4]}")
    return blobs


if __name__ == "__main__":
    print("== p100 (vers الشرح) — mot 3 depuis la droite ==")
    b = word_box(f"{OUT}/p100-300.png", "جنع", 2)
    count_dots(f"{OUT}/p100-1200.png",
               (b["left"], b["top"], b["left"] + b["width"], b["top"] + b["h"]))
    print("== p99 (bannière) — mot 3 depuis la droite ==")
    b = word_box(f"{OUT}/p99-300.png", "جنع", 2)
    count_dots(f"{OUT}/p99-1200.png",
               (b["left"], b["top"], b["left"] + b["width"], b["top"] + b["h"]))

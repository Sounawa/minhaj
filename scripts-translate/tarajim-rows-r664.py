# -*- coding: utf-8 -*-
"""Minhāj R664 — crops par ligne du tableau تراجم الأعلام (p.132-134).
Slot pdf-mut23h2u-281. Les séparateurs horizontaux du tableau sont détectés
via get_drawings() ; chaque ligne = 1 crop rendu à 1200 dpi pour adjudication
VLM des cellules dégradées. Sortie : tr-tmp/qa-crops-r664/row-p<p>-r<i>.png"""
import fitz

PDF = "/home/z/my-project/content/textbooks-src/ulum-hadith-2-thanawi_text.pdf"
OUT = "/home/z/my-project/tr-tmp/qa-crops-r664"

doc = fitz.open(PDF)
for pno in [131, 132, 133]:  # 0-based → pages 132-134
    page = doc[pno]
    rect = page.rect
    # lignes horizontales (séparateurs du tableau) : traits fins, large
    ys = set()
    for d in page.get_drawings():
        for item in d["items"]:
            if item[0] == "l":
                p1, p2 = item[1], item[2]
                if abs(p1.y - p2.y) < 1.5 and abs(p2.x - p1.x) > rect.width * 0.5:
                    ys.add(round(min(p1.y, p2.y), 1))
            elif item[0] == "re":
                r = item[1]
                if r.height < 1.5 and r.width > rect.width * 0.5:
                    ys.add(round(r.y0, 1))
    ys = sorted(ys)
    # fusionner les positions quasi identiques (< 4 pt)
    merged = []
    for y in ys:
        if merged and y - merged[-1] < 4:
            continue
        merged.append(y)
    print(f"p{pno+1}: {len(merged)} séparateurs : {merged[:20]}")
    # crops entre séparateurs consécutifs (marge 2 pt)
    for i in range(len(merged) - 1):
        y0, y1 = merged[i] + 2, merged[i + 1] - 2
        if y1 - y0 < 20:
            continue
        clip = fitz.Rect(rect.x0 + 8, y0, rect.x1 - 8, y1)
        pix = page.get_pixmap(dpi=1200, clip=clip)
        f = f"{OUT}/row-p{pno+1}-r{i}.png"
        pix.save(f)
        print(f"  row {i}: y {y0:.0f}-{y1:.0f} → {pix.width}x{pix.height} {f.split('/')[-1]}")

#!/usr/bin/env python3
# R644 v2 — composites corrigés par bbox (bandes précises)
from PIL import Image, ImageDraw, ImageFont
import os

OUT = "/home/z/my-project/tr-tmp/qa-crops-r644"

# (page, x0, y0, x1, y1, label) — coordonnées 600 dpi, corrigées bbox + bandes B
BANDS_A2 = [
    (66, 500, 540, 1750, 810, "A'1 p66 «حل هو» L1 1043"),
    (66, 1250, 2370, 2750, 2630, "A'2 p66 «لا … منها أو الذواء» L3 1046"),
    (66, 550, 2380, 1450, 2900, "A'3 p66 fin L3+L4 1046 «صنع ذلك وقد»"),
    (66, 1400, 5150, 3400, 5400, "A'4 p66 الشرح «المضي إلى الحج»"),
    (68, 700, 2230, 1750, 2480, "A'5 p68 «ما أمرهما إلا واحد»"),
    (68, 2400, 2650, 3600, 2900, "A'6 p68 «فهذا الأمد/الأمر»"),
]
BANDS_C = [
    (67, 2860, 1680, 4700, 1980, "C1 p67 bannière «فقته …»"),
    (69, 2860, 1720, 4700, 2010, "C2 p69 bannière 1 (التقويم؟)"),
    (69, 2860, 2630, 4700, 2930, "C3 p69 bannière 2 (التصويم؟/الاستئثمار؟)"),
    (69, 1300, 860, 2600, 1110, "C4 p69 «ومن فاته الحج … يوم النحر»"),
    (69, 1750, 1050, 2950, 1300, "C5 p69 1051 L1 «وهبار بن الأسود»"),
    (69, 2250, 1240, 3250, 1500, "C6 p69 1051 L2 «حين/حيث فاتهما»"),
    (69, 2150, 1520, 3150, 1800, "C7 p69 1051 L4 «فمن لم يجد فصيام»"),
    (69, 1300, 3300, 2550, 3500, "C8 p69 1269 L2 «بضبعي صبي»"),
    (69, 1300, 3450, 2550, 3650, "C9 p69 1269 L3 «نعم ولك أجر»"),
    (70, 1900, 900, 3400, 1120, "C10 p70 Q2 «حج/صج الصبي»"),
]

def build(bands, name, W=1200):
    imgs = []
    for pg, x0, y0, x1, y1, lab in bands:
        im = Image.open(f"{OUT}/hi-{pg}.png").crop((x0, y0, x1, y1))
        if im.width > W:
            r = W / im.width
            im = im.resize((W, max(1, int(im.height * r))), Image.LANCZOS)
        imgs.append((im, lab))
    H = sum(im.height + 30 for im, _ in imgs) + 10
    canvas = Image.new("RGB", (W + 20, H), "white")
    d = ImageDraw.Draw(canvas)
    try:
        font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 18)
    except Exception:
        font = ImageFont.load_default()
    y = 5
    for im, lab in imgs:
        d.rectangle([0, y, W + 20, y + 26], fill="#ffe9b3")
        d.text((6, y + 4), lab, fill="black", font=font)
        canvas.paste(im, (10, y + 28))
        y += im.height + 30
    canvas.save(f"{OUT}/{name}.png")
    print(name, canvas.size)

build(BANDS_A2, "composite-A2")
build(BANDS_C, "composite-C")

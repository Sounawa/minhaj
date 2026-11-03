#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""R553 — Passe 2 : zones sensibles 900-1000 dpi + micro-crops numéros 1200 dpi.
Crops ciblés via fitz (pixmap + clip) — méthode vlm-r548-pass3.py."""
import fitz
import os

HOME = "/home/z/my-project"
PDF = f"{HOME}/content/textbooks-src/hadith-2-iadadi_text.pdf"
CROPS = f"{HOME}/tr-tmp/qa-crops-r553"
os.makedirs(CROPS, exist_ok=True)
doc = fitz.open(PDF)


def crop(page_no, x0, y0, x1, y1, dpi, name):
    pg = doc[page_no - 1]
    clip = fitz.Rect(x0, y0, x1, y1)
    pix = pg.get_pixmap(matrix=fitz.Matrix(dpi / 72, dpi / 72), clip=clip)
    pix.save(f"{CROPS}/{name}.png")
    print(f"{name}: {pix.width}x{pix.height}")


# ---- zones (page 637x807 pt) ----
crop(105, 40, 55, 620, 350, 900, "p105-objectifs")
crop(105, 40, 350, 620, 470, 900, "p105-tamhid")
crop(105, 40, 540, 620, 780, 1000, "p105-h1-zone")
crop(106, 40, 55, 620, 245, 1000, "p106-h2a")
crop(106, 40, 240, 620, 335, 1000, "p106-h2b")
crop(106, 40, 330, 620, 500, 1000, "p106-tarjama")
crop(106, 40, 490, 620, 780, 1000, "p106-sharh")
crop(107, 40, 55, 620, 145, 1000, "p107-aouaq")
crop(107, 40, 140, 620, 300, 900, "p107-istikhlac")
crop(107, 40, 295, 620, 600, 900, "p107-tahlil")
crop(108, 40, 55, 620, 240, 1000, "p108-hukm")
crop(108, 40, 235, 620, 520, 900, "p108-hikma")
crop(108, 40, 500, 620, 680, 1000, "p108-verse2-shurut")
crop(109, 40, 50, 620, 150, 1000, "p109-nisab")
crop(109, 40, 145, 620, 280, 1000, "p109-abd")
crop(109, 40, 275, 620, 480, 900, "p109-khalata")
crop(109, 40, 465, 620, 630, 1000, "p109-hawl")
crop(110, 40, 55, 620, 340, 1000, "p110-istifta")
crop(110, 40, 335, 620, 480, 900, "p110-taqwim")
crop(110, 40, 475, 620, 800, 1000, "p110-istithmar")
crop(111, 40, 55, 620, 290, 900, "p111-iedad")

# ---- micro-crops numéros rouges / dates (1200 dpi) ----
crop(105, 80, 670, 200, 715, 1200, "n-p105-655")
crop(106, 370, 290, 450, 330, 1200, "n-p106-668")
crop(106, 95, 440, 260, 490, 1200, "n-p106-dates")
crop(106, 190, 650, 270, 695, 1200, "n-p106-2975")
crop(107, 130, 100, 210, 145, 1200, "n-p107-1306")
crop(107, 360, 545, 440, 585, 1200, "n-p107-arafa")
crop(108, 200, 125, 290, 170, 1200, "n-p108-nur")
crop(108, 55, 520, 140, 565, 1200, "n-p108-104")
crop(109, 85, 100, 170, 145, 1200, "n-p109-662")
crop(109, 200, 230, 300, 272, 1200, "n-p109-664")
crop(109, 250, 555, 420, 600, 1200, "n-p109-660")
crop(110, 60, 60, 340, 110, 1200, "n-p110-46")
crop(110, 80, 290, 350, 335, 1200, "n-p110-666a")
crop(110, 175, 620, 270, 665, 1200, "n-p110-666b")
print("DONE")

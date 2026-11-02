#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Minhāj — Rendus image R527 (slot 764) : crops 300/500 dpi pour VLM.
p.195 badge+objectifs, boîte des āyāt (médaillons), p.201 تقويم/استثمار,
p.202 ouverture annexe."""
import fitz

PDF = "/home/z/my-project/content/textbooks-src/tafsir-3-thanawi_text.pdf"
doc = fitz.open(PDF)
OUT = "/home/z/my-project/tr-tmp"

def crop(page_no, rect, name, dpi=300):
    page = doc[page_no - 1]
    pix = page.get_pixmap(dpi=dpi, clip=rect)
    path = f"{OUT}/{name}.png"
    pix.save(path)
    print(name, pix.width, "x", pix.height, "->", path)

W = 637.08
# p.195 : badge (y 70-130) — 500 dpi
crop(195, fitz.Rect(40, 66, 600, 132), "probe-l26-p195-badge", 500)
# p.195 : objectifs + tamhīd (y 185-465) — 300 dpi
crop(195, fitz.Rect(40, 183, 600, 465), "probe-l26-p195-objets-tamhid", 300)
# p.195 : boîte des āyāt (y 550-745) — 300 dpi
crop(195, fitz.Rect(40, 548, 600, 745), "probe-l26-p195-box", 300)
# p.195 : boîte bas (zoom médaillons) — 500 dpi moitié basse
crop(195, fitz.Rect(40, 548, 600, 660), "probe-l26-p195-box-top", 500)
crop(195, fitz.Rect(40, 640, 600, 745), "probe-l26-p195-box-bot", 500)
# p.201 : toute la page (16 lignes) — 300 dpi
crop(201, fitz.Rect(40, 60, 600, 745), "probe-l26-p201-full", 300)
# p.202 : haut de page (titre annexe) — 300 dpi
crop(202, fitz.Rect(40, 60, 600, 340), "probe-l26-p202-head", 300)

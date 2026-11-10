# -*- coding: utf-8 -*-
"""Minhāj — Crops de preuve leçon 403 hadith-3es (R675, slot pdf-mut23h2x-403,
أحكام مزدلفة, p.97-102). Fenêtres chiffre-par-chiffre : tout renvoi Muwaṭṭaʾ
et toute āya tranchés à l'image (doctrine R535-R547, chiffres OCR jamais devinés).
Micro-crops 900 dpi sur les zones de renvois + zones OCR dégradées.
Sortie : tr-tmp/qa-crops-r675/."""
import os

import fitz
from PIL import Image

PDF = "/home/z/my-project/content/textbooks-src/hadith-3-iadadi_text.pdf"
OUT = "/home/z/my-project/tr-tmp/qa-crops-r675"
os.makedirs(OUT, exist_ok=True)
doc = fitz.open(PDF)


def crop(name, page_no, x0, y0, x1, y1, dpi=900):
    pg = doc[page_no - 1]
    clip = fitz.Rect(pg.rect.width * x0, pg.rect.height * y0,
                     pg.rect.width * x1, pg.rect.height * y1)
    pix = pg.get_pixmap(matrix=fitz.Matrix(dpi / 72, dpi / 72), clip=clip, alpha=False)
    img = Image.frombytes("RGB", (pix.width, pix.height), pix.samples)
    path = f"{OUT}/{name}.png"
    img.save(path)
    print(f"OK {path} — {img.width}x{img.height}")


# --- Renvois numérotés (chiffre par chiffre) ---
crop("r675-n-p98-hadith2", 98, 0.10, 0.40, 0.94, 0.50)      # [الموطأ رقم: …] fin hadith 2 (ex-«0611»)
crop("r675-n-p98-tarjama", 98, 0.06, 0.66, 0.96, 0.78)      # tarjama : سنة وفيات + قوال
crop("r675-n-p99-athar", 99, 0.06, 0.83, 0.96, 0.95)        # نافع/محسّر + [الموطأ رقم: …] (ex-«6611»)
crop("r675-n-p100-mawqif", 100, 0.06, 0.04, 0.96, 0.22)     # كلها موقف + [الموطأ رقم: …] (ex-«2511»)
crop("r675-n-p100-jamian", 100, 0.06, 0.36, 0.96, 0.55)     # deux refs «جمعاً» (ex-«2911»/«5911»)
crop("r675-n-p101-rukh", 101, 0.06, 0.76, 0.96, 0.99)       # رخصة + [الموطأ …] ×3 (ex-«1611»/«2611»/«06»)
crop("r675-n-p102-talil", 102, 0.04, 0.42, 0.97, 0.97)      # taʿlīl complet : 3 āyāt + [الموطأ رقم: …]

# --- Zones OCR dégradées (texte intégral) ---
crop("r675-t-p97-intro", 97, 0.04, 0.36, 0.96, 0.60)        # définition المزدلفة + أو…تقدّموا
crop("r675-t-p97-hadith1", 97, 0.04, 0.58, 0.96, 0.95)      # isnād + matn hadith 1
crop("r675-t-p98-hadith2", 98, 0.04, 0.04, 0.96, 0.45)      # isnād + matn hadith 2 («الصلاة أمامك»)
crop("r675-t-p100-b", 100, 0.04, 0.50, 0.96, 0.97)          # صفة الجمع + ابن القاسم/الجمهور
crop("r675-t-p101-adhan", 101, 0.04, 0.40, 0.96, 0.76)      # أذان/إقامة + النزول + المشعر

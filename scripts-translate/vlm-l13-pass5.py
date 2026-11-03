#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""R558 — passe 5 VLM : 4 dernières zones ultra-serrées."""
import json
import os
import subprocess
import fitz
from PIL import Image, ImageDraw

HOME = "/home/z/my-project"
PDF = f"{HOME}/content/textbooks-src/hadith-2-iadadi_text.pdf"
OUT = f"{HOME}/tr-tmp/qa-crops-r558d"
VL = f"{HOME}/tr-tmp/vlm-l13"
os.makedirs(OUT, exist_ok=True)

doc = fitz.open(PDF)
ZONES = [
    (91, 0.72, 0.90, 1600),   # 1: isnād du 1er hadith d'أمّ عطيّة
    (95, 0.14, 0.33, 1600),   # 2: fin du matn [597]
    (96, 0.04, 0.14, 1800),   # 3: renvoi rouge du Najāšī
    (97, 0.50, 0.72, 1600),   # 4: le hadith [618]
]

parts = []
for i, (pno, f0, f1, dpi) in enumerate(ZONES, 1):
    page = doc[pno - 1]
    H, W = page.rect.height, page.rect.width
    clip = fitz.Rect(0, H * f0, W, H * f1)
    sp = f"{OUT}/z{i}.png"
    pm = page.get_pixmap(matrix=fitz.Matrix(dpi / 72, dpi / 72), clip=clip)
    pm.save(sp)
    im = Image.open(sp)
    w = 2300
    if im.width > w:
        im = im.resize((w, int(im.height * w / im.width)))
    parts.append(im)

h = sum(im.height + 26 for im in parts)
comp = Image.new("RGB", (2300, h), "white")
y = 0
for i, im in enumerate(parts, 1):
    comp.paste(im, (0, y))
    d = ImageDraw.Draw(comp)
    d.rectangle([0, y, 340, y + 24], fill=(200, 0, 0))
    d.text((8, y + 4), f"ZONE {i} (page {ZONES[i-1][0]})", fill="white")
    y += im.height + 26
comp.save(f"{OUT}/composite-p5.png")
print("composite-p5.png", comp.size)

BASE = ("Image d'un manuel scolaire marocain de hadith, 4 zones numérotées. "
        "Transcription EXACTE lettre par lettre, chiffre par chiffre. [illisible] si "
        "incertain. N'invente RIEN, ne complète JAMAIS de mémoire. Zone par zone.")

ASK = (
    "ZONE 1 : la ligne du isnād du premier hadith (après le titre الأحاديث) mot à mot : "
    "مالك عن ... (deuxième transmetteur, LETTRE PAR LETTRE : أيّوب ? أبو بكر ? + بن أبي "
    "تميمة ? شيبة ? + السختياني ?) عن محمد بن سيرين عن أمّ عطيّة... — "
    "ZONE 2 : la fin du matn du hadith (renvoi rouge [الموطأ رقم: 597]) : transcris "
    "LES DERNIERS MOTS du matn lettre par lettre après «ولا زوج يلي ذلك منها» "
    "(يُمَطُّ ? يُمَتُّ ? قَميصُها ? فَمُسِحَ ? بوجهها وكَفّيها من الصَّعيد ?) puis le "
    "renvoi rouge chiffre par chiffre. — "
    "ZONE 3 : le renvoi rouge entre crochets en fin de citation : transcris TOUS les "
    "chiffres imprimés entre الموطأ رقم et ] — combien de chiffres ? lesquels ? — "
    "ZONE 4 : le hadith : transcris matn mot à mot lettre par lettre : (صُلِّيَ ? "
    "صَلَّى ? صلّيتُ ?) (على ?) (عمر بن الخطاب ?) (في المسجد ? في المصلّى ?) puis le "
    "renvoi rouge chiffre par chiffre."
)

out = f"{VL}/pass5.json"
r = subprocess.run(["z-ai", "vision", "-p", f"{BASE}\nQUESTION : {ASK}",
                    "-i", f"{OUT}/composite-p5.png", "-o", out],
                   capture_output=True, text=True, timeout=600)
print("rc:", r.returncode, (r.stderr or "")[:150])
d = json.load(open(out, encoding="utf-8"))
print(d["choices"][0]["message"]["content"][:3600])

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""R558 — passe 4 VLM (finale) : 6 micro-zones divergentes, un composite, un appel."""
import json
import os
import subprocess
import fitz
from PIL import Image, ImageDraw

HOME = "/home/z/my-project"
PDF = f"{HOME}/content/textbooks-src/hadith-2-iadadi_text.pdf"
OUT = f"{HOME}/tr-tmp/qa-crops-r558c"
VL = f"{HOME}/tr-tmp/vlm-l13"
os.makedirs(OUT, exist_ok=True)

doc = fitz.open(PDF)

# (page, y0, y1, dpi)
ZONES = [
    (91, 0.83, 0.97, 1500),   # 1: isnād du 1er hadith (ligne entière)
    (92, 0.50, 0.78, 1200),   # 2: encadré ترجمة الراوية
    (95, 0.02, 0.19, 1400),   # 3: fin du matn [597]
    (95, 0.50, 0.73, 1200),   # 4: [602] isnād + matn
    (96, 0.00, 0.17, 1400),   # 5: fin matn Najāšī + renvoi rouge
    (97, 0.36, 0.76, 1200),   # 6: les deux hadiths [616] [618]
]

ims = []
for i, (pno, f0, f1, dpi) in enumerate(ZONES, 1):
    page = doc[pno - 1]
    H, W = page.rect.height, page.rect.width
    clip = fitz.Rect(0, H * f0, W, H * f1)
    sp = f"{OUT}/z{i}.png"
    pm = page.get_pixmap(matrix=fitz.Matrix(dpi / 72, dpi / 72), clip=clip)
    pm.save(sp)
    ims.append(Image.open(sp))

w = 2300
parts = []
for im in ims:
    if im.width > w:
        im = im.resize((w, int(im.height * w / im.width)))
    parts.append(im)
h = sum(min(im.height, 2600) + 26 for im in parts)
comp = Image.new("RGB", (w, h), "white")
y = 0
draw = None
for i, im in enumerate(parts, 1):
    comp.paste(im, (0, y))
    d = ImageDraw.Draw(comp)
    d.rectangle([0, y, 340, y + 24], fill=(200, 0, 0))
    d.text((8, y + 4), f"ZONE {i} (page {ZONES[i-1][0]})", fill="white")
    y += min(im.height, 2600) + 26
comp.save(f"{OUT}/composite-final.png")
print("composite-final.png", comp.size)

BASE = ("Image d'un manuel scolaire marocain de hadith, 6 zones numérotées en rouge "
        "(ZONE 1 à 6). Transcription EXACTE du texte imprimé, token par token, chiffre "
        "par chiffre. [illisible] si incertain. N'invente RIEN, ne complète JAMAIS de "
        "mémoire, ne corrige pas l'imprimé. Réponds zone par zone.")

ASK = (
    "ZONE 1 (isnād du hadith d'أمّ عطيّة) : transcris la ligne du isnād mot à mot — "
    "le nom complet du deuxième transmetteur LETTRE PAR LETTRE (أيّوب بن أبي تميمة ? "
    "أبو بكر بن أبي تحمة ? شيبة ?) + le laqab qui suit (السختياني ?) ; puis les noms "
    "suivants. — "
    "ZONE 2 (encadré ترجمة الراوية) : transcris l'encadré ENTIer : nom de أمّ عطيّة "
    "بنت QUI (الحارث ? كعب ?), le وقيل..., من فقهاء..., la liste des transmetteurs "
    "noms par noms, et عاشت إلى حدود سنة N. — "
    "ZONE 3 (matn du hadith [597]) : transcris la fin du matn mot à mot : après «ولا "
    "زوج يلي ذلك منها» — le ou les mots suivants LETTRE PAR LETTRE (يُمَطَّ قميصها ? "
    "يُمتُّ ? فمُسِح بوجهها وكفّيها من الصعيد ?) puis le renvoi rouge. — "
    "ZONE 4 (hadith [602]) : transcris l'isnād mot à mot (عن ابن شهاب، عن حميد بن...، "
    "عن...) puis le matn ENTIER mot à mot — attention aux mots : ويُلَف في ... QUOI "
    "exactement (الثوب الثالث ? النوب ? القوابيل ?) et (فإن لم يكن إلا ثوب واحد ?), "
    "puis le renvoi rouge chiffre par chiffre. — "
    "ZONE 5 (fin du matn du hadith du Najāšī) : transcris la ligne entière mot à mot "
    "(فخرج بهم إلى المصلى فصفّ بهم وكبّر أربع تكبيرات ?) puis le renvoi rouge entre "
    "crochets [الموطأ رقم : N] — N chiffre par chiffre (3 chiffres). — "
    "ZONE 6 (les deux hadiths عن نافع) : transcris CHACUN mot à mot ENTIER — premier "
    "hadith : la fin après إذا صلّيـ LETTRE PAR LETTRE (صلّيتَها لوقتها ? صلّيتم "
    "لوقتكم ? صلّيتَ لهمّتا ?) + renvoi rouge ; deuxième hadith : (صلّيتُ ? صُلِّيَ ?) "
    "(على عمر بن الخطاب في المسجد ? في المصلّى ?) + renvoi rouge."
)

out = f"{VL}/pass4.json"
r = subprocess.run(["z-ai", "vision", "-p", f"{BASE}\nQUESTION : {ASK}",
                    "-i", f"{OUT}/composite-final.png", "-o", out],
                   capture_output=True, text=True, timeout=600)
print("rc:", r.returncode, (r.stderr or "")[:150])
d = json.load(open(out, encoding="utf-8"))
print(d["choices"][0]["message"]["content"][:4200])

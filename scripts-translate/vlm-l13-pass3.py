#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""R558 — passe 3 VLM : micro-zones restantes (isnād-1, transmetteurs, [602],
renvois Najāšī/Abū Dāwūd, duʿāʾ début, [616]/[618], kafan femme, en-tête).
Chaque bande est rendue dans un FICHIER UNIQUE (pas de _strip partagé).
"""
import json
import time
import os
import subprocess
import fitz
from PIL import Image

HOME = "/home/z/my-project"
PDF = f"{HOME}/content/textbooks-src/hadith-2-iadadi_text.pdf"
OUT = f"{HOME}/tr-tmp/qa-crops-r558b"
VL = f"{HOME}/tr-tmp/vlm-l13"
os.makedirs(OUT, exist_ok=True)
os.makedirs(VL, exist_ok=True)

doc = fitz.open(PDF)

# (page, y0, y1, dpi, étiquette)
ZONES = [
    (91, 0.00, 0.07, 1200, "hdr"),
    (91, 0.70, 0.94, 1200, "chain1"),
    (92, 0.74, 1.00, 1000, "raouia"),
    (95, 0.25, 0.46, 1200, "kafan-femme"),
    (95, 0.44, 0.72, 1000, "h602"),
    (96, 0.00, 0.09, 1200, "naj-renvoi"),
    (96, 0.28, 0.56, 1000, "dua-court"),
    (96, 0.54, 0.78, 1000, "dua-abuhurayra"),
    (97, 0.00, 0.20, 1200, "h616"),
    (97, 0.18, 0.40, 1200, "h618"),
]

per_page = {}
for pno, f0, f1, dpi, tag in ZONES:
    page = doc[pno - 1]
    H, W = page.rect.height, page.rect.width
    clip = fitz.Rect(0, H * f0, W, H * f1)
    strip_path = f"{OUT}/s-{tag}.png"
    pm = page.get_pixmap(matrix=fitz.Matrix(dpi / 72, dpi / 72), clip=clip)
    pm.save(strip_path)
    per_page.setdefault(pno, []).append(strip_path)

for pno, paths in per_page.items():
    ims = [Image.open(p) for p in paths]
    w = 2400
    h = sum(min(im.height, 2400) + 12 for im in ims)
    comp = Image.new("RGB", (w, h), "white")
    y = 0
    for p, im in zip(paths, ims):
        if im.width > w:
            im = im.resize((w, int(im.height * w / im.width)))
        comp.paste(im, (0, y))
        y += min(im.height, 2400) + 12
    outp = f"{OUT}/micro-p{pno}.png"
    comp.save(outp)
    print(outp, comp.size)

BASE = ("Tu lis une bande d'un manuel scolaire marocain de hadith (Muwaṭṭaʾ Mālik / "
        "Šarḥ az-Zarqānī) à TRÈS haute résolution. Transcription EXACTE token par "
        "token, chiffre par chiffre. [illisible] si incertain. N'invente RIEN, ne "
        "complète JAMAIS de mémoire, ne corrige pas l'imprimé.")

ASKS = [
    (91, [("hdr", "la ligne d'en-tête : le mot الدرس suivi du chiffre (chiffre par "
                "chiffre : 12 ? 13 ?) puis le titre de la leçon mot à mot"),
          ("chain1", "l'isnād du premier hadith (section الأحاديث) : chaque nom mot "
                     "à mot — مالك عن QUI (nom complet + laqab) عن QUI عن QUI")]),
    (92, [("raouia", "l'encadré ترجمة الراوية ENTIER : nom de أمّ عطيّة (نسيبة بنت ... "
                     "?), le وقيل (variante), من فقهاء الصحابة..., la liste des "
                     "transmetteurs noms par noms, عاشت إلى حدود سنة N")]),
    (95, [("kafan-femme", "la phrase sur le كفن de la femme (وأن تكفن المرأة ب...) "
                          "mot à mot ENTIERE + la suite (زيادة في الستر...)"),
          ("h602", "le hadith avec renvoi rouge [الموطأ رقم : N] : l'isnād mot à mot "
                   "(عن ابن شهاب، عن حميد بن...، عن...) + le matn ENTIER mot à mot "
                   "(الميّت يُقص... في ... الثلاثة... فإن لم يكن إلا ... كُفِّن فيه) + N")]),
    (96, [("naj-renvoi", "la fin de la citation du Najāšī et son renvoi rouge entre "
                         "crochets : [الموطأ رقم : N] — N chiffre par chiffre"),
          ("dua-court", "la citation لقول النبي ﷺ (إذا صليتم...) + son renvoi entre "
                        "crochets (سنن أبي داود : N ?) chiffre par chiffre + la phrase "
                        "ومن ترك الدعاء... mot à mot ENTIERE"),
          ("dua-abuhurayra", "l'isnād du duʿāʾ (ففي الموطأ عن مالك، عن سعيد بن أبي سعيد "
                             "المقبري، عن أبيه...) + les premiers mots du duʿāʾ de أبو "
                             "هريرة فقال : ... mot à mot (أنا لعمرك ? أتبعها ?)")]),
    (97, [("h616", "le premier hadith : isnād + matn ENTIER mot à mot — la fin du matn "
                   "après إذا صلّيـ : transcris ces mots LETTRE PAR LETTRE (صلّيتها "
                   "لوقتها ? صلّيتم لوقتكم ? لُهمّتا ?) + renvoi rouge chiffre par chiffre"),
          ("h618", "le deuxième hadith : isnād + matn ENTIER mot à mot (صَلَّيْتُ ? "
                   "صُلِّيَ ? على عمر بن الخطاب في المسجد ? في المصلّى ?) + renvoi")]),
]

def vision_call(prompt, img, out, tries=5):
    cmd = ["z-ai", "vision", "-p", prompt, "-i", img, "-o", out]
    for t in range(tries):
        r = subprocess.run(cmd, capture_output=True, text=True, timeout=300)
        if r.returncode == 0:
            return True, ""
        err = (r.stderr or "") + (r.stdout or "")
        if "429" in err or "Too many" in err:
            wait = 45 + 30 * t
            print(f"  429 — attente {wait}s (tentative {t + 1}/{tries})")
            time.sleep(wait)
            continue
        return False, err[:200]
    return False, "429 persistant"

for pno, zones in ASKS:
    q = " ; ".join(f"({tag}) {ask}" for tag, ask in zones)
    out = f"{VL}/pass3-p{pno}.json"
    if os.path.exists(out):
        print("•", pno, "déjà lu")
        continue
    ok, err = vision_call(f"{BASE}\nQUESTION : {q}", f"{OUT}/micro-p{pno}.png", out)
    print(("✓" if ok else "✗"), f"p{pno}", err)

print("\n===== RÉSULTATS =====")
for pno, zones in ASKS:
    try:
        d = json.load(open(f"{VL}/pass3-p{pno}.json", encoding="utf-8"))
        print(f"\n----- p{pno} -----")
        print(d["choices"][0]["message"]["content"][:3500])
    except Exception as e:
        print(f"\n----- p{pno} ----- ERREUR {e}")

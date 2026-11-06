#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# R630 — lectures VLM lot B : zones p.61-62 (renvois Tabṣira, Ibn Raǧab, taqwīm,
# istiṯmār, iʿdād qiblī) + recadrage chirurgical 2400 dpi du renvoi al-Umm (p.58)
# pour trancher 103 vs 301 chiffre à chiffre (doctrine : jamais deviné).
import subprocess, os, sys
import fitz

VLM = "tr-tmp/vlm-read-r616.mjs"
C = "tr-tmp/r623-crops"
OUTD = "tr-tmp/r630"
os.makedirs(OUTD, exist_ok=True)

# --- recadrage chirurgical du renvoi al-Umm (p.58, fin du bloc de citation, marge gauche) ---
BOOK = "content/textbooks-src/ulum-hadith-2-thanawi_text.pdf"
doc = fitz.open(BOOK)
page = doc[57]  # p.58 (1-based -> index 57)
# zone du renvoi : bas-gauche du bloc de citation (x 30-260, y 440-570 en points)
mat = fitz.Matrix(2400 / 72, 2400 / 72)
clip = fitz.Rect(30, 430, 300, 580)
pix = page.get_pixmap(matrix=mat, clip=clip)
umm = f"{OUTD}/umm-ref-2400.png"
pix.save(umm)
print("crop Umm:", umm, pix.width, "x", pix.height)

READS = [
    (f"{C}/ADJ12-p61-tabsira-refs-900.png",
     "Transcris fidèlement TOUT le texte arabe visible, surtout les DEUX renvois entre crochets (Šarḥ aṭ-Ṭabṣira). Pour chaque renvoi, décris chaque chiffre glyphiquement (gauche/droite de la barre oblique). Ne devine rien.",
     f"{OUTD}/read-ADJ12.txt"),
    (f"{C}/ADJ13-p61-ibnrajab-900.png",
     "Transcris fidèlement TOUT le texte arabe visible (citation de Ibn Raǧab avec le mot ahtadī + renvoi entre crochets). Décris chaque chiffre du renvoi glyphiquement. Ne devine rien.",
     f"{OUTD}/read-ADJ13.txt"),
    (f"{C}/ADJ14-p61-taqwim-600.png",
     "Transcris fidèlement TOUT le texte arabe visible (encadré taqwīm / تقويم : la liste numérotée complète, 3 items attendus). Ne devine rien : marque [illisible] ce qui ne se lit pas.",
     f"{OUTD}/read-ADJ14.txt"),
    (f"{C}/ADJ15-p62-istithmar-900.png",
     "Transcris fidèlement TOUT le texte arabe visible (encadré istiṯmār / استثمار : questions et consignes complètes). Ne devine rien.",
     f"{OUTD}/read-ADJ15.txt"),
    (f"{C}/ADJ16-p62-i3dad-qibli-600.png",
     "Transcris fidèlement TOUT le texte arabe visible (encadré الإعداد القبلي : préparation de la leçon suivante, titre annoncé + consignes). Ne devine rien.",
     f"{OUTD}/read-ADJ16.txt"),
    (umm,
     "Cette image montre un renvoi entre crochets de la forme [الأم؛ للشافعي: N/M]. Épelle CHAQUE chiffre glyphiquement de GAUCHE à DROITE (un par un : forme exacte, ex. « 1 = trait vertical avec drapeau », « 3 = deux bosses », « 0 = cercle »). Puis donne la suite exacte des glyphes avant la barre oblique et après. Ne normalise RIEN, ne convertis RIEN : décris uniquement ce qui est imprimé.",
     f"{OUTD}/read-umm-2400.txt"),
]

for img, prompt, out in READS:
    if os.path.exists(out) and os.path.getsize(out) > 40:
        print("SKIP (déjà lu):", out)
        continue
    print("READ:", img, "->", out, flush=True)
    r = subprocess.run(["node", VLM, img, prompt, out],
                       capture_output=True, text=True, timeout=180)
    if r.returncode != 0:
        print("  ERR:", r.stderr[:300])
    else:
        print("  OK,", os.path.getsize(out), "octets")
print("LOT B TERMINÉ")

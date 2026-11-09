# -*- coding: utf-8 -*-
"""Minhāj R664 — couche texte de référence du tableau tarāǧim (p.132-134).
Sortie : tr-tmp/tarajim-text-layer.txt — par page, par bande, texte lisible
(lignes p.133 renversées mot à mot pour lecture ; chiffres en inversion par
paires consignés BRUTS + corrigés)."""
import fitz
import json

PDF = "/home/z/my-project/content/textbooks-src/ulum-hadith-2-thanawi_text.pdf"
BANDS = {
    131: [("r0-qari", 138, 217), ("r1-rajab", 217, 311), ("r2-shafii", 311, 408),
          ("r3-raz", 408, 482), ("r4-daraq", 482, 556), ("r5-zark", 556, 654)],
    132: [("r0-salah", 48, 209), ("r1-abd", 209, 344), ("r2-hakim", 344, 460),
          ("r3-iraqi", 460, 572), ("r4-khatib", 572, 690)],
    133: [("r0-dhahabi", 53, 144), ("r1-sakhawi", 144, 235), ("r2-suyuti", 235, 350),
          ("r3-iyad", 350, 507), ("r4-nawawi", 507, 620)],
}

doc = fitz.open(PDF)
out = []
for pno, rows in BANDS.items():
    page = doc[pno]
    out.append(f"===== PAGE {pno+1} =====")
    for name, y0, y1 in rows:
        clip = fitz.Rect(38, y0, 424, y1)
        t = page.get_text("text", clip=clip).strip()
        # normaliser : une ligne par ligne OCR, renversée mot à mot si page 133
        lines = [l.strip() for l in t.splitlines() if l.strip()]
        if pno == 132:  # page 133 : couche inversée mot à mot
            lines = [" ".join(w[::-1] for w in l.split()) for l in lines]
        out.append(f"--- {name} ---")
        out.extend(lines)
        # chiffres : détection des paires inversées
        digits = [l for l in lines if any(ch.isdigit() for ch in l)]
        for d in digits:
            fixed = []
            for w in d.split():
                if w.isdigit() and len(w) >= 2:
                    # inversion par paires (ex. 597 → 795 : 5-9-7 → 7-95 ?)
                    # règle documentée R102+ : les chiffres OCR sont inversés
                    # par paires adjacentes ; plusieurs lectures possibles,
                    # l'IMAGE tranche (VLM)
                    fixed.append(f"{w}→{w[::-1]}")
            if fixed:
                out.append(f"[CHIFFRES BRUTS] {d} | candidats paires: {' '.join(fixed)}")

open("/home/z/my-project/tr-tmp/tarajim-text-layer.txt", "w", encoding="utf-8").write(
    "\n".join(out))
print("\n".join(out[:40]))

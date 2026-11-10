# -*- coding: utf-8 -*-
"""Minhāj — CROPS de preuve leçon 408 hadith-3es (R684, takeover du slot
pdf-mut23h2x-408, ما يفعله الحاج يوم النحر). Re-cadrage des zones restées
incertaines après les rondes r679/r682/r683 :
 1. p.129 : re-cadrage du crop x0-p129-annonce RATÉ (zone blanche, folio 139) —
    le contenu de p.129 est en HAUT de page (annonce de la leçon 408 par la
    clôture de la 407, déjà livrée R681) → fenêtre 0.00-0.50 + vérif bas de page.
 2. p.130 : zone tamhīd complète (verset + renvoi [سورة التوبة الآية: N] + ligne
    suivante) pour trancher les lectures divergentes (Ṭā-Hā 132 / at-Tawba 40
    récusées par convergence x2 + y130-aya-ref + couche texte).
 3. p.133 : ligne du hadith d'ʿAlī (نحر بعض هديه بيده / ونحر بعضه بغيره) —
    trois lectures divergentes r682.
 4. p.134 : ligne « وكذلك الطيب عند ابن عمر، وكرهه مالك(فقط ?) » + titre de
    sous-section « من لبّد شعره أو عقصه أو ظفره/ضفره ».
 5. p.135 : encadré الاستثمار complet (bandeau + athar 1183 + fin divergente)
    + iʿdād de la leçon suivante (2 questions visibles ? 3 ?) + fin de page.
 6. p.136 : borne supérieure exclusive (objectifs de la leçon 20/409).
Sorties : tr-tmp/qa-crops-r684/*.png — Source : hadith-3-iadadi_text.pdf."""
import fitz
import os

PDF = "/home/z/my-project/content/textbooks-src/hadith-3-iadadi_text.pdf"
OUT = "/home/z/my-project/tr-tmp/qa-crops-r684"
os.makedirs(OUT, exist_ok=True)

doc = fitz.open(PDF)

# (nom, page_pdf_1-indexée, x0_frac, x1_frac, y0_frac, y1_frac, dpi)
CROPS = [
    # p.129 — re-cadrage du crop raté (annonce iʿdād 408, haut de page)
    ("t129-annonce",   129, 0.03, 0.97, 0.00, 0.50, 400),
    ("t129-bas",       129, 0.03, 0.97, 0.50, 0.85, 300),
    # p.130 — tamhīd : verset + renvoi + ligne suivante (trancher Ṭā-Hā/Tawba 40)
    ("t130-tamhid",    130, 0.03, 0.97, 0.42, 0.70, 900),
    ("t130-aya-tight", 130, 0.10, 0.90, 0.48, 0.62, 900),
    # p.133 — hadith d'ʿAlī (nḥara baʿḍa hadyih…)
    ("t133-ali",       133, 0.05, 0.95, 0.575, 0.70, 900),
    # p.134 — ligne « الطيب عند ابن عمر وكرهه مالك » + titre « لبّد/عقص/ظفر »
    ("t134-tayb",      134, 0.03, 0.97, 0.24, 0.34, 900),
    ("t134-lubd",      134, 0.03, 0.97, 0.44, 0.56, 900),
    # p.135 — encadré الاستثمار (bandeau + athar 1183) + iʿdād + fin de page
    ("t135-encadre",   135, 0.03, 0.97, 0.00, 0.40, 900),
    ("t135-athar-end", 135, 0.05, 0.95, 0.16, 0.32, 900),
    ("t135-cloture",   135, 0.03, 0.97, 0.28, 1.00, 600),
    # p.136 — borne supérieure exclusive (leçon 20/409)
    ("t136-top",       136, 0.03, 0.97, 0.00, 0.35, 600),
]

for nom, pg, fx0, fx1, fy0, fy1, dpi in CROPS:
    page = doc[pg - 1]
    r = page.rect
    clip = fitz.Rect(r.width * fx0, r.height * fy0, r.width * fx1, r.height * fy1)
    pix = page.get_pixmap(matrix=fitz.Matrix(dpi / 72, dpi / 72), clip=clip)
    path = f"{OUT}/{nom}.png"
    pix.save(path)
    print(f"OK {path} {pix.width}x{pix.height}")
print(f"TOTAL {len(CROPS)} crops r684")

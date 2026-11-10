# -*- coding: utf-8 -*-
"""Minhāj — CROPS de preuve leçon 408 hadith-3es (R682, takeover du slot
pdf-mut23h2x-408, ما يفعله الحاج يوم النحر). Re-vérification du cadrage r679 :
le crop x0-p129-annonce (0.45-0.98) avait RATÉ sa fenêtre (zone blanche + folio
139 — le contenu de p.129 est en HAUT de page : fin de leçon 407, invite
Zarqānī + bannière أحفظ + iʿdād) → recadrage b0 (0.05-0.45). Recoupe de l'ordre
des pages x1-x16 : faite par concordance couche dict page par page (x1/x2=p.130,
x3/x4/x5=p.131, x6/x7/x8=p.132, x9-x12=p.133, x13-x16=p.134) ; bornes de leçon
p.130-135 (p.129 = iʿdād de la 407 déjà livrée R681 ; p.136 = objectifs de la
409, borne supérieure exclusive). Zones incertaines tranchées par preuve image
900 dpi (protocole R535-R679 : jamais de numéro ni de borne deviné).
Sorties : tr-tmp/qa-crops-r682/*.png
Source : content/textbooks-src/hadith-3-iadadi_text.pdf — pages PDF 129-136."""
import fitz
import os

PDF = "/home/z/my-project/content/textbooks-src/hadith-3-iadadi_text.pdf"
OUT = "/home/z/my-project/tr-tmp/qa-crops-r682"
os.makedirs(OUT, exist_ok=True)

doc = fitz.open(PDF)
DPI = 900

# (nom, page_pdf_1-indexée, y0_frac, y1_frac)
CROPS = [
    # bornes
    ("b0-p129-contenu",     129, 0.05, 0.45),
    ("b4-p136-objectifs",   136, 0.05, 0.30),
    # p.130 : médaillon + titre, verset at-Tawba, hadith Mālik + renvoi 1173
    ("m1-p130-medallion",   130, 0.00, 0.27),
    ("v1-p130-aya",         130, 0.49, 0.585),
    ("h1-p130-malik",       130, 0.58, 0.90),
    # p.131 : hadiths ʿĪsā b. Ṭalḥa (1267) et Ḥafṣa (1169), années de la notice
    ("h2-p131-isa",         131, 0.09, 0.33),
    ("h3-p131-hafsa",       131, 0.33, 0.47),
    ("n1-p131-annees",      131, 0.67, 0.79),
    # p.132 : re-citation (verbes فحلقت/فتحلقت + إجزاء)
    ("f1-p132-recit",       132, 0.595, 0.83),
    # p.133 : مكان النحر (1167), مباشرة (1170), hadith ʿUmar (début)
    ("k1-p133-makan",       133, 0.40, 0.55),
    ("k2-p133-mubashara",   133, 0.53, 0.70),
    ("q1-p133-umr",         133, 0.75, 0.92),
    # p.134 : fin hadith ʿUmar + 1226 + verset al-Māʾida, lubd/ʿaqs (1186, 1185),
    # taqwīm (3 questions + folio)
    ("q2-p134-umrfin",      134, 0.03, 0.29),
    ("l1-p134-lubd",        134, 0.29, 0.50),
    ("l2-p134-1185",        134, 0.45, 0.62),
    ("w1-p134-taqwim",      134, 0.62, 1.00),
    # p.135 : rapport [1183], invite Zarqānī, bannière + iʿdād (préparation 409)
    ("b2-p135-fatwa",       135, 0.10, 0.30),
    ("b3-p135-cloture",     135, 0.30, 0.62),
]

mat = fitz.Matrix(DPI / 72, DPI / 72)
for nom, pg, f0, f1 in CROPS:
    page = doc[pg - 1]
    r = page.rect
    clip = fitz.Rect(r.width * 0.03, r.height * f0, r.width * 0.97, r.height * f1)
    pix = page.get_pixmap(matrix=mat, clip=clip)
    path = f"{OUT}/{nom}.png"
    pix.save(path)
    print(f"OK {path} {pix.width}x{pix.height}")
print(f"TOTAL {len(CROPS)} crops")

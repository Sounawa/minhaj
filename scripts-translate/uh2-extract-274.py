# -*- coding: utf-8 -*-
# R655 (ouvrier uh2-274) — extraction leçon 20 ulum-hadith-tanawi-2
# (pdf-mut23h2u-274, الحديث المعلل)
# Bornes par SONDAGE (jamais devinées) :
#   p.102 = bannière leçon 20 (borne couchée R654 : ouverture leçon 20 الحديث المعلل,
#           objectifs couche décodée vus en sondage R654)
#   borne sup = en-têtes أهداف الدرس de la leçon 21 (الدرس 21 : المدرج والمقلوب)
#           à localiser dans la fenêtre 102-116 (sondage present script) ;
#           la borne sup DOIT être la page qui précède les objectifs de la leçon 21
# Patron : scripts-translate/uh2-extract-273.py (fitz, couche BRUTE + couche FIX
# + décodage renversement ligne à ligne dans le même script)
import os

import fitz

PDF = "/home/z/my-project/content/textbooks-src/ulum-hadith-2-thanawi_text.pdf"
OUT = "/home/z/my-project/tr-tmp/uh2-l274-raw.txt"
FIRST, LAST = 102, 116  # fenêtre large : leçon 20 (102-?) + sondage borne sup (leçon 21)


def fix_line(line: str) -> str:
    """Réinverse l'ordre des mots d'une ligne RTL fournie mot à mot par PyMuPDF."""
    words = line.split()
    return " ".join(reversed(words)) if len(words) > 1 else line


doc = fitz.open(PDF)
print(f"pages totales PDF : {doc.page_count}")
chunks = []
banner20_hits = []
banner21_hits = []
goals_hits = []
for p in range(FIRST, min(LAST, doc.page_count) + 1):
    txt = doc[p - 1].get_text("text")
    raw = f"===== PAGE {p} — BRUTE =====\n{txt}"
    fixed = "\n".join(fix_line(l) for l in txt.splitlines() if l.strip())
    chunks.append(raw + f"\n===== PAGE {p} — FIX (mots réinversés) =====\n{fixed}\n")
    # bannière leçon 20 : « الحديث المعلل » (en brut LTR inversé : للعملا تيدحلا)
    if "للعملا" in txt or "تيدحلا" in txt:
        banner20_hits.append(p)
    # sondage bannière leçon 21 : « المدرج والمقلوب » — en brut inversé : « بولقملاو جرذملا »
    if "جرذملا" in txt or "بولقملا" in txt:
        banner21_hits.append(p)
    # en-têtes أهداف الدرس (candidat borne sup de la leçon suivante)
    if "درسلا فادهأ" in txt:
        goals_hits.append(p)
out = "\n".join(chunks)
os.makedirs(os.path.dirname(OUT), exist_ok=True)
with open(OUT, "w", encoding="utf-8") as fh:
    fh.write(out)
print(f"écrit {OUT} — {len(out)} car, pages {FIRST}-{min(LAST, doc.page_count)}")
for p in banner20_hits:
    print(f"p.{p} : motif leçon 20 « المعلل » détecté (candidat bannière = borne inf)")
for p in banner21_hits:
    print(f"p.{p} : motif leçon 21 « المدرج/المقلوب » détecté (candidat bannière leçon 21)")
for p in goals_hits:
    print(f"p.{p} : motif « أهداف الدرس » détecté (en-tête sondage)")

# ---- décodage renversement ligne à ligne (patron uh2-decode-271.py), même script ----
DEC = "/home/z/my-project/tr-tmp/uh2-l274-decoded.txt"
import re  # noqa: E402

txt = open(OUT, encoding="utf-8").read()
dec_chunks = []
for p in range(FIRST, min(LAST, doc.page_count) + 1):
    m = re.search(rf"===== PAGE {p} — BRUTE =====\n(.*?)===== PAGE {p} — FIX", txt, re.S)
    if not m:
        continue
    lines = [l for l in m.group(1).strip().splitlines() if l.strip()]
    dec_chunks.append(f"\n########## PAGE {p} — DECODE (renversé) ##########")
    for l in lines:
        d = l[::-1]
        flag = "  [ Court/frag. ]" if len(d.strip()) < 12 else ""
        dec_chunks.append(f"| {d}{flag}")
dec = "\n".join(dec_chunks)
with open(DEC, "w", encoding="utf-8") as fh:
    fh.write(dec)
print(f"écrit {DEC} — {len(dec)} car")

# ---- vue READABLE fusionnée (patron de passation : brute + fix + decode par page) ----
READ = "/home/z/my-project/tr-tmp/uh2-l274-readable.txt"
hdr = [
    "uh2-l274-readable.txt — leçon 20 ulum-hadith-tanawi-2 (pdf-mut23h2u-274, الحديث المعلل)",
    "Bornes TRANCHÉES par sondage image (jamais devinées) : p.102 = bannière leçon 20",
    "(médaillon « 20 » en chiffres occidentaux, titre الحديث المعلل — p102-banner-objectifs.png) ;",
    "p.107 = bannière leçon 21 (médaillon ٢١, المدرج والمقلوب — p107-banner-l21.png) →",
    "LEÇON 20 = pages 102-106 (p.106 = الإعداد القبلي, clôture — p106-idad.png).",
    "Chiffres de la couche BRUTE inversés par paires (ex. 174→471, 945→549, 164→461,",
    "29→92, 39→93) — l'IMAGE fait autorité (lectures VLM tr-tmp/qa-crops-r655/,",
    "TRENTE lectures consignées, toute récusation documentée par preuve image).",
    "",
]
body = []
for p in range(102, min(116, doc.page_count) + 1):
    m = re.search(rf"===== PAGE {p} — BRUTE =====\n(.*?)===== PAGE {p} — FIX[^\n]*\n(.*?)(?=\n===== PAGE \d+|\Z)", txt, re.S)
    if not m:
        continue
    body.append(f"================ PAGE {p} ================")
    body.append("--- BRUTE (couché texte, ordre LTR brut) ---")
    body.append(m.group(1).strip())
    body.append("--- FIX (mots réinversés) ---")
    body.append(m.group(2).strip().lstrip("\n"))
    md = re.search(rf"########## PAGE {p} — DECODE \(renversé\) ##########\n(.*?)(?=\n########## PAGE {p+1}|\Z)", dec, re.S)
    if md:
        body.append("--- DECODE (renversé ligne à ligne) ---")
        body.append(md.group(1).strip())
    body.append("")
with open(READ, "w", encoding="utf-8") as fh:
    fh.write("\n".join(hdr + body))
print(f"écrit {READ} — {os.path.getsize(READ)} octets")

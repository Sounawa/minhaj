# -*- coding: utf-8 -*-
# R651 — extraction leçon 18 ulum-hadith-tanawi-2 (pdf-mut23h2u-272, أسباب الطعن في الراوي)
# Bornes par SONDAGE (jamais devinées) :
#   p.93 = bannière leçon 18 (vue sondage R648 + reconfirmée image R651-b : « الدرس ١٨ — أسباب الطعن في الراوي »)
#   p.96 = fin de leçon 18 (الاستنتاج + الإعداد القبلي)
#   p.97 = bannière leçon 19 (الموضوع والمتروك) — borne sup = 96
# Patron : scripts-translate/uh2-extract-271.py (fitz, couche BRUTE + couche FIX)
# + décodage renversement ligne à ligne dans le même script (patron uh2-decode-271.py)
import os

import fitz

PDF = "/home/z/my-project/content/textbooks-src/ulum-hadith-2-thanawi_text.pdf"
OUT = "/home/z/my-project/tr-tmp/uh2-l272-raw.txt"
FIRST, LAST = 93, 97  # bornes larges : leçon 18 (93-96) + sondage borne sup (97 = leçon 19)


def fix_line(line: str) -> str:
    """Réinverse l'ordre des mots d'une ligne RTL fournie mot à mot par PyMuPDF."""
    words = line.split()
    return " ".join(reversed(words)) if len(words) > 1 else line


doc = fitz.open(PDF)
chunks = []
banner_hits = []
for p in range(FIRST, min(LAST, doc.page_count) + 1):
    txt = doc[p - 1].get_text("text")
    raw = f"===== PAGE {p} — BRUTE =====\n{txt}"
    fixed = "\n".join(fix_line(l) for l in txt.splitlines() if l.strip())
    chunks.append(raw + f"\n===== PAGE {p} — FIX (mots réinversés) =====\n{fixed}\n")
    # sondage bannière leçon 19 : « الموضوع والمتروك » — en brut LTR inversé :
    # « كورتملاو عوضوملا » (نoyau de la bannière) présent ⇒ candidat borne sup
    if "كورتملا" in txt or "عوضوملا" in txt:
        banner_hits.append(p)
out = "\n".join(chunks)
os.makedirs(os.path.dirname(OUT), exist_ok=True)
with open(OUT, "w", encoding="utf-8") as fh:
    fh.write(out)
print(f"écrit {OUT} — {len(out)} car, pages {FIRST}-{min(LAST, doc.page_count)}")
for p in banner_hits:
    print(f"p.{p} : motif « الموضوع والمتروك » détecté (candidat bannière leçon 19) — à confirmer par image")

# ---- décodage renversement ligne à ligne (patron uh2-decode-271.py), même script ----
DEC = "/home/z/my-project/tr-tmp/uh2-l272-decoded.txt"
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

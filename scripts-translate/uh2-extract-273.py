# -*- coding: utf-8 -*-
# R654 (ouvrier D, 02:11) — extraction leçon 19 ulum-hadith-tanawi-2
# (pdf-mut23h2u-273, الموضوع والمتروك)
# Bornes par SONDAGE (jamais devinées) :
#   p.97 = bannière leçon 19 (vue sondage R651 + couche FIX R653 passation (b))
#   borne sup = bannière leçon 20 à localiser dans la fenêtre 97-105 (sondage present script)
# Patron : scripts-translate/uh2-extract-272.py (fitz, couche BRUTE + couche FIX
# + décodage renversement ligne à ligne dans le même script)
import os

import fitz

PDF = "/home/z/my-project/content/textbooks-src/ulum-hadith-2-thanawi_text.pdf"
OUT = "/home/z/my-project/tr-tmp/uh2-l273-raw.txt"
FIRST, LAST = 97, 105  # fenêtre large : leçon 19 (97-?) + sondage borne sup (leçon 20)


def fix_line(line: str) -> str:
    """Réinverse l'ordre des mots d'une ligne RTL fournie mot à mot par PyMuPDF."""
    words = line.split()
    return " ".join(reversed(words)) if len(words) > 1 else line


doc = fitz.open(PDF)
chunks = []
banner19_hits = []
banner20_hits = []
goals_hits = []
for p in range(FIRST, min(LAST, doc.page_count) + 1):
    txt = doc[p - 1].get_text("text")
    raw = f"===== PAGE {p} — BRUTE =====\n{txt}"
    fixed = "\n".join(fix_line(l) for l in txt.splitlines() if l.strip())
    chunks.append(raw + f"\n===== PAGE {p} — FIX (mots réinversés) =====\n{fixed}\n")
    # bannière leçon 19 : « الموضوع والمتروك » (en brut LTR inversé : كورتملاو عوضوملا)
    if "كورتملا" in txt or "عوضوملا" in txt:
        banner19_hits.append(p)
    # sondage bannière leçon 20 : motif « الدرس ٢٠ » — en brut inversé : « ٢٠ سرند »
    if "٢٠ سرند" in txt or "٢٠ سرند" in txt.replace(" ", ""):
        banner20_hits.append(p)
    # en-têtes أهداف الدرس de la leçon 20 (candidat borne sup)
    if "درسلا فادهأ" in txt:
        goals_hits.append(p)
out = "\n".join(chunks)
os.makedirs(os.path.dirname(OUT), exist_ok=True)
with open(OUT, "w", encoding="utf-8") as fh:
    fh.write(out)
print(f"écrit {OUT} — {len(out)} car, pages {FIRST}-{min(LAST, doc.page_count)}")
for p in banner19_hits:
    print(f"p.{p} : motif leçon 19 « الموضوع والمتروك » détecté")
for p in banner20_hits:
    print(f"p.{p} : motif « الدرس ٢٠ » détecté (candidat bannière leçon 20 = borne sup)")
for p in goals_hits:
    print(f"p.{p} : motif « أهداف الدرس » détecté (en-tête sondage)")

# ---- décodage renversement ligne à ligne (patron uh2-decode-271.py), même script ----
DEC = "/home/z/my-project/tr-tmp/uh2-l273-decoded.txt"
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

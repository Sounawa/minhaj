# -*- coding: utf-8 -*-
# R658 (ouvrier D tick 11:26, claim uh2-278) — extraction leçon 24 ulum-hadith-tanawi-2
# (pdf-mut23h2u-278, الدرس 24 : الاختصار في الحديث وروايته بالمعنى)
# Bornes par SONDAGE (jamais devinées) :
#   p.125 = bannière leçon 24 (médaillon ٢٤ — couchée R657 en sondage de borne :
#           « leçon 24 الاختصار p.125 » ; à confirmer par lecture présente script)
#   borne sup = en-têtes أهداف الدرس de la leçon 25 (الدرس 25 : أنشطة تطبيقية)
#           à localiser dans la fenêtre 125-145 (sondage present script) ; la
#           borne sup DOIT être la page qui précède les objectifs de la leçon 25.
# Patron : scripts-translate/uh2-extract-276.py (fitz, couche BRUTE + couche FIX
# + décodage renversement ligne à ligne dans le même script)
import os

import fitz

PDF = "/home/z/my-project/content/textbooks-src/ulum-hadith-2-thanawi_text.pdf"
OUT = "/home/z/my-project/tr-tmp/uh2-l278-raw.txt"
FIRST, LAST = 125, 145  # fenêtre large : leçon 24 (125-?) + sondage borne sup (leçon 25)


def fix_line(line: str) -> str:
    """Réinverse l'ordre des mots d'une ligne RTL fournie mot à mot par PyMuPDF."""
    words = line.split()
    return " ".join(reversed(words)) if len(words) > 1 else line


doc = fitz.open(PDF)
print(f"pages totales PDF : {doc.page_count}")
chunks = []
banner25_hits = []
banner24_hits = []
goals_hits = []
for p in range(FIRST, min(LAST, doc.page_count) + 1):
    txt = doc[p - 1].get_text("text")
    raw = f"===== PAGE {p} — BRUTE =====\n{txt}"
    fixed = "\n".join(fix_line(l) for l in txt.splitlines() if l.strip())
    chunks.append(raw + f"\n===== PAGE {p} — FIX (mots réinversés) =====\n{fixed}\n")
    # sondage bannière leçon 25 : « أنشطة تطبيقية » — en brut inversé :
    # أنشطة → ةطشنأ ; تطبيقية → ةيقبت
    if "ةطشنأ" in txt or "ةيقبت" in txt:
        banner25_hits.append(p)
    # sondage bannière leçon 24 : « الاختصار » — en brut inversé : الاختصار → راصتخلا
    if "راصتخلا" in txt or "راصتخا" in txt:
        banner24_hits.append(p)
    # en-têtes أهداف الدرس (candidat borne sup de la leçon suivante)
    if "درسلا فادهأ" in txt:
        goals_hits.append(p)
out = "\n".join(chunks)
os.makedirs(os.path.dirname(OUT), exist_ok=True)
with open(OUT, "w", encoding="utf-8") as fh:
    fh.write(out)
print(f"écrit {OUT} — {len(out)} car, pages {FIRST}-{min(LAST, doc.page_count)}")
for p in banner24_hits:
    print(f"p.{p} : motif leçon 24 « الاختصار » détecté (candidat bannière leçon 24)")
for p in banner25_hits:
    print(f"p.{p} : motif leçon 25 « أنشطة تطبيقية » détecté (candidat bannière leçon 25)")
for p in goals_hits:
    print(f"p.{p} : motif « أهداف الدرس » détecté (en-tête sondage)")

# ---- décodage renversement ligne à ligne (patron uh2-decode-271.py), même script ----
DEC = "/home/z/my-project/tr-tmp/uh2-l278-decoded.txt"
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
READ = "/home/z/my-project/tr-tmp/uh2-l278-readable.txt"
hdr = [
    "uh2-l278-readable.txt — leçon 24 ulum-hadith-tanawi-2 (pdf-mut23h2u-278, الاختصار في الحديث وروايته بالمعنى)",
    "Bornes par SONDAGE (jamais devinées) : p.125 = bannière leçon 24 (médaillon ٢٤ —",
    "couchée R657 en sondage) ; borne sup = أهداف الدرس leçon 25 أنشطة تطبيقية (sondage",
    "present script). Chiffres de la couche BRUTE inversés par paires (ex. 471→174) —",
    "l'IMAGE fait autorité (lectures VLM tr-tmp/qa-crops-r658/, toute récusation documentée).",
    "",
]
body = []
for p in range(FIRST, min(LAST, doc.page_count) + 1):
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

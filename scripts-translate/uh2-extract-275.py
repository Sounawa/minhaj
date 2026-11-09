# -*- coding: utf-8 -*-
# R656 (ouvrier uh2-275) — extraction leçon 21 ulum-hadith-tanawi-2
# (pdf-mut23h2u-275, المدرج والمقلوب)
# Bornes par SONDAGE (jamais devinées) :
#   p.107 = bannière leçon 21 (médaillon ٢١, المدرج والمقلوب — couchée R655 :
#           « p.107 = bannière leçon 21 » + matn Ibn Ḥaǧar suite des cinq visés
#           « أو بتقديم أو تأخير فالمقلوب » visible p.107-108 en sondage)
#   borne sup = en-têtes أهداف الدرس de la leçon 22 (الدرس 22 : المزيد في متصل
#           الأسانيد والمضطرب) à localiser dans la fenêtre 107-121 (sondage
#           present script) ; la borne sup DOIT être la page qui précède les
#           objectifs de la leçon 22.
# Patron : scripts-translate/uh2-extract-274.py (fitz, couche BRUTE + couche FIX
# + décodage renversement ligne à ligne dans le même script)
import os

import fitz

PDF = "/home/z/my-project/content/textbooks-src/ulum-hadith-2-thanawi_text.pdf"
OUT = "/home/z/my-project/tr-tmp/uh2-l275-raw.txt"
FIRST, LAST = 107, 121  # fenêtre large : leçon 21 (107-?) + sondage borne sup (leçon 22)


def fix_line(line: str) -> str:
    """Réinverse l'ordre des mots d'une ligne RTL fournie mot à mot par PyMuPDF."""
    words = line.split()
    return " ".join(reversed(words)) if len(words) > 1 else line


doc = fitz.open(PDF)
print(f"pages totales PDF : {doc.page_count}")
chunks = []
banner22_hits = []
goals_hits = []
for p in range(FIRST, min(LAST, doc.page_count) + 1):
    txt = doc[p - 1].get_text("text")
    raw = f"===== PAGE {p} — BRUTE =====\n{txt}"
    fixed = "\n".join(fix_line(l) for l in txt.splitlines() if l.strip())
    chunks.append(raw + f"\n===== PAGE {p} — FIX (mots réinversés) =====\n{fixed}\n")
    # sondage bannière leçon 22 : « المزيد » — en brut inversé : « ديزملا »
    # (motif المضطرب inversé = برطضملا)
    if "ديزملا" in txt or "برطضملا" in txt:
        banner22_hits.append(p)
    # en-têtes أهداف الدرس (candidat borne sup de la leçon suivante)
    if "درسلا فادهأ" in txt:
        goals_hits.append(p)
out = "\n".join(chunks)
os.makedirs(os.path.dirname(OUT), exist_ok=True)
with open(OUT, "w", encoding="utf-8") as fh:
    fh.write(out)
print(f"écrit {OUT} — {len(out)} car, pages {FIRST}-{min(LAST, doc.page_count)}")
for p in banner22_hits:
    print(f"p.{p} : motif leçon 22 « المزيد/المضطرب » détecté (candidat bannière leçon 22)")
for p in goals_hits:
    print(f"p.{p} : motif « أهداف الدرس » détecté (en-tête sondage)")

# ---- décodage renversement ligne à ligne (patron uh2-decode-271.py), même script ----
DEC = "/home/z/my-project/tr-tmp/uh2-l275-decoded.txt"
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
READ = "/home/z/my-project/tr-tmp/uh2-l275-readable.txt"
hdr = [
    "uh2-l275-readable.txt — leçon 21 ulum-hadith-tanawi-2 (pdf-mut23h2u-275, المدرج والمقلوب)",
    "Bornes par SONDAGE (jamais devinées) : p.107 = bannière leçon 21 (médaillon ٢١,",
    "المدرج والمقلوب — couchée R655, matn Ibn Ḥaǧar « أو بتقديم أو تأخير فالمقلوب »",
    "p.107-108) ; borne sup = أهداف الدرس leçon 22 المزيد (sondage present script).",
    "Chiffres de la couche BRUTE inversés par paires (ex. 471→174) — l'IMAGE fait",
    "autorité (lectures VLM tr-tmp/qa-crops-r656/, toute récusation documentée).",
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

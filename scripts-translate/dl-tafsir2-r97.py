#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""R97 — re-téléchargement idempotent du manuel tafsir-2es (méthode R93/R96).

كتاب التفسير 2 إعدادي.pdf (21 315 823 o / 210 p., طبعة 1439/2018)
+ sa couche _djvu.txt — item archive.org 1_20220304_20220304_2251.
Le /tmp du sandbox a été recyclé : tr-tmp/books/ ne contient plus ce manuel.
"""
import json, os, subprocess, sys
from urllib.parse import quote

ITEM = "1_20220304_20220304_2251"
BASE = f"https://archive.org/download/{ITEM}"
DEST = "/home/z/my-project/tr-tmp/books"
os.makedirs(DEST, exist_ok=True)

TARGETS = [
    "كتاب التفسير 2 إعدادي.pdf",
    "كتاب التفسير 2 إعدادي_djvu.txt",
]

meta_path = "/tmp/ia-meta-r97.json"
if not os.path.exists(meta_path):
    subprocess.run(["curl", "-sL", "--max-time", "60",
                    f"https://archive.org/metadata/{ITEM}", "-o", meta_path], check=True)
sizes = {f["name"]: int(f.get("size", 0)) for f in json.load(open(meta_path)).get("files", [])}

ok, fail = [], []
for name in TARGETS:
    dest = os.path.join(DEST, name)
    want = sizes.get(name, 0)
    url = f"{BASE}/{quote(name)}"
    have = os.path.getsize(dest) if os.path.exists(dest) else 0
    if have and have == want:
        print(f"[SKIP] {name} — déjà {have:,} o (attendu {want:,})")
        ok.append(name)
        continue
    print(f"[GET ] {name} — {have:,} → {want:,} o ...", flush=True)
    r = subprocess.run(["curl", "-L", "-C", "-", "--retry", "3", "--max-time", "540",
                        "-o", dest, url])
    have = os.path.getsize(dest) if os.path.exists(dest) else 0
    if r.returncode == 0 and (want == 0 or have == want):
        print(f"[OK  ] {name} = {have:,} o (attendu {want:,})")
        ok.append(name)
    else:
        print(f"[FAIL] {name} — rc={r.returncode}, {have:,} o ≠ {want:,}")
        fail.append(name)

# comptage de pages du PDF
p = os.path.join(DEST, "كتاب التفسير 2 إعدادي.pdf")
if os.path.exists(p):
    try:
        from pypdf import PdfReader
        n = len(PdfReader(p).pages)
    except Exception:
        out = subprocess.run(["pdfinfo", p], capture_output=True, text=True).stdout
        n = next((l.split(":")[1].strip() for l in out.splitlines() if l.startswith("Pages")), "?")
    print(f"[PAGES] كتاب التفسير 2 إعدادي.pdf : {n} pages, {os.path.getsize(p):,} o")

print("RÉSULTAT :", len(ok), "ok /", len(fail), "échecs", fail)
sys.exit(1 if fail else 0)

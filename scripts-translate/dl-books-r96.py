#!/usr/bin/env python3
# R96 — priorité (2)+(3) de R94 : sécurisation des manuels tafsir-3es / fiqh-3es / usul-fiqh-tanawi-3
# depuis l'item archive.org 1_20220304_20220304_2251 (méthode R93, idempotente).
# Les PDF restent locaux (tr-tmp/books/*.pdf ignorés du git) ; les djvu.txt sont versionnables.
import json, subprocess, sys, os
from urllib.parse import quote

ITEM = "1_20220304_20220304_2251"
BASE = f"https://archive.org/download/{ITEM}"
DEST = "/home/z/my-project/tr-tmp/books"
os.makedirs(DEST, exist_ok=True)

TARGETS = [
    "كتاب التفسير 3 إعدادي.pdf",
    "كتاب الفقه 3 إعدادي.pdf",
    "كتاب أصول الفقه 3 إعدادي.pdf",
    "كتاب التفسير 3 إعدادي_djvu.txt",
    "كتاب الفقه 3 إعدادي_djvu.txt",
    "كتاب أصول الفقه 3 إعدادي_djvu.txt",
]

meta_path = "/tmp/ia-meta-r96.json"
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
        ok.append(name); continue
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

# comptage de pages (pypdf si dispo, sinon pdfinfo)
for name in TARGETS:
    if not name.endswith(".pdf"):
        continue
    p = os.path.join(DEST, name)
    n = "?"
    try:
        from pypdf import PdfReader
        n = len(PdfReader(p).pages)
    except Exception:
        try:
            out = subprocess.run(["pdfinfo", p], capture_output=True, text=True).stdout
            n = next((l.split(":")[1].strip() for l in out.splitlines() if l.startswith("Pages")), "?")
        except Exception:
            pass
    print(f"[PAGES] {name} : {n} pages, {os.path.getsize(p):,} o")

print("RÉSULTAT :", len(ok), "ok /", len(fail), "échecs", fail)
sys.exit(1 if fail else 0)

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""R105 — re-téléchargement idempotent du manuel tafsir-3es (méthode R93/R96/R97).

Le /tmp du sandbox a été recyclé : tr-tmp/books/ ne contient plus كتاب التفسير 3 إعدادي.pdf
(le _djvu.txt est déjà en place)."""
import json, os, subprocess
from urllib.parse import quote

ITEM = "1_20220304_20220304_2251"
BASE = f"https://archive.org/download/{ITEM}"
DEST = "/home/z/my-project/tr-tmp/books"
os.makedirs(DEST, exist_ok=True)

TARGETS = [
    "كتاب التفسير 3 إعدادي.pdf",
]

meta_path = "/tmp/ia-meta-r105.json"
if not os.path.exists(meta_path):
    subprocess.run(["curl", "-sL", "--max-time", "60",
                    f"https://archive.org/metadata/{ITEM}", "-o", meta_path], check=True)
sizes = {f["name"]: int(f.get("size", 0)) for f in json.load(open(meta_path)).get("files", [])}

ok, fail = [], []
for name in TARGETS:
    dest = os.path.join(DEST, name)
    want = sizes.get(name, 0)
    if os.path.isfile(dest) and want and os.path.getsize(dest) == want:
        ok.append((name, "déjà en place"))
        continue
    url = f"{BASE}/{name}"
    print(f"téléchargement {name} ({want} o)…", flush=True)
    r = subprocess.run(["curl", "-sL", "--max-time", "600", "-o", dest, url])
    if r.returncode == 0 and os.path.isfile(dest) and (not want or os.path.getsize(dest) == want):
        ok.append((name, os.path.getsize(dest)))
    else:
        fail.append(name)

print("OK:", ok)
print("FAIL:", fail)
raise SystemExit(1 if fail else 0)

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""R576 — ÉTAPE 6 : variante raw de etap6-mirror-fetch.py.
Contexte : route _text ÉPUISÉE 37/37 ; vérification « duplicatas présumés »
a tranché que 3 raws de l'item n'ont NI _text dans l'item NI source locale :
  كتاب التفسير 1 إعدادي.pdf  → tafsir-1-iadadi.pdf
  كتاب التفسير 2 إعدادي.pdf  → tafsir-2-iadadi.pdf
  كتاب علوم الحديث 1 ثانوي.pdf → ulum-hadith-1-thanawi.pdf
Télécharge ces raws en content/textbooks-src/ (validation %PDF-), git add
immédiat laissé à l'appelant. Usage: python3 etap6-mirror-fetch-r576.py
"""
import json
import os
import urllib.parse
import urllib.request

HOME = "/home/z/my-project"
ITEM = "1_20220304_20220304_2251"
COLLECTION_DIR = os.path.join(HOME, "content", "textbooks-src")
CACHE = os.path.join(HOME, "tr-logs", "collection-files.json")

# cibles tranchées par la vérification anti-doublon R576 (raws sans _text
# dans l'item et sans fichier local — jamais de devinette)
TARGETS = {
    "كتاب التفسير 1 إعدادي.pdf": "tafsir-1-iadadi.pdf",
    "كتاب التفسير 2 إعدادي.pdf": "tafsir-2-iadadi.pdf",
    "كتاب علوم الحديث 1 ثانوي.pdf": "ulum-hadith-1-thanawi.pdf",
}


def main() -> int:
    with open(CACHE, encoding="utf-8") as fh:
        files = json.load(fh)
    item_set = set(files)
    present = set(os.listdir(COLLECTION_DIR))
    ok = 0
    for fname, dest_base in TARGETS.items():
        if fname not in item_set:
            print(f"  ABSENT de l'item : {fname} — ignoré (jamais deviné)")
            continue
        dest = os.path.join(COLLECTION_DIR, dest_base)
        if dest_base in present or os.path.exists(dest):
            print(f"  déjà présent : {dest_base}")
            continue
        url = ("https://archive.org/download/" + ITEM + "/"
               + urllib.parse.quote(fname))
        try:
            req = urllib.request.Request(
                url, headers={"User-Agent": "Mozilla/5.0"})
            with urllib.request.urlopen(req, timeout=600) as resp, \
                    open(dest, "wb") as fh:
                while True:
                    chunk = resp.read(1 << 20)
                    if not chunk:
                        break
                    fh.write(chunk)
            if open(dest, "rb").read(5) != b"%PDF-":
                os.remove(dest)
                print(f"  ÉCHEC corps non-PDF : {fname}")
                continue
            mb = os.path.getsize(dest) / 1e6
            print(f"  ACQUIS {dest_base} ({mb:.1f} Mo) ← {fname}")
            ok += 1
        except Exception as e:  # noqa: BLE001
            try:
                os.remove(dest)
            except OSError:
                pass
            print(f"  ERREUR {fname} : {type(e).__name__} {e}")
    print(f"acquis : {ok}/{len(TARGETS)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

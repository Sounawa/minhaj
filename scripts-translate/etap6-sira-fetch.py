#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""ÉTAPE 6 (repasse sira) — sonde puis télécharge les PDF bruts de Sīra
Nabawiyya (1/2/3 iādādī) depuis l'item miroir archive.org
1_20220304_20220304_2251 vers content/textbooks-src/.
Ces PDF n'ont PAS de couche _text (40 « autres » du cache) : ils serviront
de source d'images (pdftoppm → crops → VLM) pour les fronts futurs.
Validation %PDF-, git add laissé à l'appelant.
Usage: python3 etap6-sira-fetch.py [max_files]
"""
import os
import sys
import urllib.parse
import urllib.request

HOME = "/home/z/my-project"
ITEM = "1_20220304_20220304_2251"
DEST_DIR = os.path.join(HOME, "content", "textbooks-src")

NAMES = {
    1: "كتاب السيرة النبوية 1 إعدادي.pdf",
    2: "كتاب السيرة النبوية 2 إعدادي.pdf",
    3: "كتاب السيرة النبوية 3 إعدادي.pdf",
}
DESTS = {n: f"sira-{n}-iadadi.pdf" for n in NAMES}


def probe(n: int):
    fname = NAMES[n]
    url = (f"https://archive.org/download/{ITEM}/"
           + urllib.parse.quote(fname))
    req = urllib.request.Request(url, method="HEAD",
                                 headers={"User-Agent": "Mozilla/5.0"})
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            return url, int(r.headers.get("Content-Length") or -1)
    except Exception as e:  # noqa: BLE001
        return url, -1


def main() -> int:
    max_files = int(sys.argv[1]) if len(sys.argv) > 1 else 3
    done = 0
    for n in sorted(NAMES):
        dest_path = os.path.join(DEST_DIR, DESTS[n])
        if os.path.exists(dest_path):
            print(f"  DÉJÀ LÀ sira-{n} ({DESTS[n]})")
            continue
        url, size = probe(n)
        if size < 0:
            print(f"  INJOIGNABLE sira-{n}")
            continue
        print(f"  sira-{n} : {size/1e6:.1f} Mo ← {NAMES[n]}")
        if done >= max_files:
            continue
        try:
            req = urllib.request.Request(url,
                                         headers={"User-Agent": "Mozilla/5.0"})
            with urllib.request.urlopen(req, timeout=300) as resp, \
                    open(dest_path, "wb") as fh:
                while True:
                    chunk = resp.read(1 << 20)
                    if not chunk:
                        break
                    fh.write(chunk)
            if open(dest_path, "rb").read(5) != b"%PDF-":
                os.remove(dest_path)
                print(f"  ÉCHEC corps non-PDF : {NAMES[n]}")
                continue
            mb = os.path.getsize(dest_path) / 1e6
            print(f"  ACQUIS {DESTS[n]} ({mb:.1f} Mo)")
            done += 1
        except Exception as e:  # noqa: BLE001
            try:
                os.remove(dest_path)
            except OSError:
                pass
            print(f"  ERREUR {NAMES[n]} : {type(e).__name__}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

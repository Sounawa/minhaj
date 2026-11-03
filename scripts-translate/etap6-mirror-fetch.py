#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""ÉTAPE 6 (JAMAIS SANS RIEN FAIRE) — précharge des manuels du miroir
archive.org (item 1_20220304_20220304_2251) en content/textbooks-src/.
Réutilise les tables de slugs de supervisor.py (convention de nommage
{matière}-{année}-{cycle}[_text].pdf). Validation %PDF-, git add immédiat
effectué par l'appelant. Usage: python3 etap6-mirror-fetch.py [max_files]
"""
import json
import os
import re
import sys
import urllib.parse
import urllib.request

HOME = "/home/z/my-project"
ITEM = "1_20220304_20220304_2251"
COLLECTION_DIR = os.path.join(HOME, "content", "textbooks-src")
CACHE = os.path.join(HOME, "tr-logs", "collection-files.json")

SUBJECT_SLUGS = {
    "التفسير": "tafsir", "الحديث": "hadith", "الفقه": "fiqh",
    "اصولالفقه": "usul-fiqh", "التوقيت": "taqtit", "القراءات": "qiraat",
    "الفكرالاسلامي": "fikr-islami", "السيرة": "sira", "التوحيد": "tawhid",
    "المنطق": "mantiq", "علومالقران": "ulum-quran",
    "علومالحديث": "ulum-hadith", "الفرائض": "faraid",
}
YEAR_WORDS = {
    "الاولى": 1, "الاول": 1, "الثانية": 2, "الثاني": 2, "الثالثة": 3,
    "الثالث": 3, "الرابعة": 4, "الرابع": 4, "الخامسة": 5, "الخامس": 5,
    "السادسة": 6, "السادس": 6,
}
CYCLE_SLUGS = {"ثانوي": "thanawi", "اعدادي": "iadadi", "ابتدائي": "ibtidai"}


def normalize_ar(s: str) -> str:
    s = re.sub(r"[\s\u0640]+", "", s)
    for ch in ("أ", "إ", "آ"):
        s = s.replace(ch, "ا")
    return s


def dest_name(fname: str) -> str:
    nf = normalize_ar(fname)
    m = re.match(r"^كتاب(.+?)(\d)(ثانوي|اعدادي|ابتدائي)", nf)
    if m:
        subject, year, cycle = m.group(1), m.group(2), m.group(3)
        slug = SUBJECT_SLUGS.get(subject, subject)
        suffix = "_text" if "_text" in nf else ""
        return f"{slug}-{year}-{CYCLE_SLUGS.get(cycle, cycle)}{suffix}.pdf"
    return re.sub(r"\s+", "_", fname)


def main() -> int:
    max_files = int(sys.argv[1]) if len(sys.argv) > 1 else 3
    with open(CACHE, encoding="utf-8") as fh:
        files = json.load(fh)
    present = set(os.listdir(COLLECTION_DIR)) if os.path.isdir(COLLECTION_DIR) else set()
    targets = []
    for fname in files:
        if not fname.endswith("_text.pdf"):
            continue
        if fname in present or dest_name(fname) in present:
            continue
        targets.append(fname)
    # priorité : matières de production actives d'abord (tafsir, hadith),
    # puis ordre de la collection
    prio = {"tafsir": 0, "hadith": 1}
    targets.sort(key=lambda f: prio.get(dest_name(f).split("-")[0], 9))
    print(f"cibles manquantes : {len(targets)} — préchargement de {max_files}")
    ok = 0
    for fname in targets[:max_files]:
        dest = os.path.join(COLLECTION_DIR, dest_name(fname))
        url = (f"https://archive.org/download/{ITEM}/"
               + urllib.parse.quote(fname))
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
            with urllib.request.urlopen(req, timeout=300) as resp, \
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
            print(f"  ACQUIS {os.path.basename(dest)} ({mb:.1f} Mo) ← {fname}")
            ok += 1
        except Exception as e:  # noqa: BLE001
            try:
                os.remove(dest)
            except OSError:
                pass
            print(f"  ERREUR {fname} : {type(e).__name__}")
    print(f"acquis : {ok}/{min(max_files, len(targets))}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

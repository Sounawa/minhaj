#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""R603 — copie de claim-lesson.py adaptée au post-recyclage sandbox :
HOME = /tmp/my-project (arbre VIVANT R601 : claims + caches OCR + registre),
doc_prefix étendu aux DEUX séries du livre ulum-hadith-tanawi-1 :
  pdf-mut23h2q- (leçons 1-24) et pdf-mut23h2r- (leçons 25-31).
Convention claim inchangée : tr-tmp/claims/uh1-<docId>.claim.json, création
O_EXCL atomique, expiration 50 min. Le script partagé claim-lesson.py n'est
PAS modifié (fichier séparé, préfixe r603).
Usage : python3 scripts-translate/claim-lesson-r603.py --book ulum-hadith-tanawi-1 pdf-mut23h2r-137 <trace_id>
        python3 scripts-translate/claim-lesson-r603.py --book ulum-hadith-tanawi-1 --refresh pdf-mut23h2r-137 <trace_id>
        python3 scripts-translate/claim-lesson-r603.py --book ulum-hadith-tanawi-1 --release pdf-mut23h2r-137
"""
import datetime
import json
import os
import sys
import time

HOME = "/tmp/my-project"
CLAIMS = f"{HOME}/tr-tmp/claims"
EXPIRY = 50 * 60  # secondes

BOOKS = {
    "ulum-hadith-tanawi-1": {
        "registry": "ulum-hadith-tanawi-1.json",
        "doc_prefixes": ("pdf-mut23h2q-", "pdf-mut23h2r-"),
        "claim_prefix": "uh1-",
    },
}
DEFAULT_BOOK = "ulum-hadith-tanawi-1"


def book_cfg(book: str) -> dict:
    if book not in BOOKS:
        print(f"REFUS : livre inconnu « {book} » — livres : {', '.join(sorted(BOOKS))}")
        sys.exit(1)
    return BOOKS[book]


def utcnow() -> str:
    return datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def claim_age(path: str) -> float:
    try:
        return time.time() - os.path.getmtime(path)
    except OSError:
        return float("inf")


def free_slots(book: str = DEFAULT_BOOK) -> list:
    cfg = book_cfg(book)
    data = json.load(open(f"{HOME}/content/books/{cfg['registry']}", encoding="utf-8"))
    les = data["lessons"] if isinstance(data, dict) else data
    out = []
    for L in les:
        doc = str(L.get("docId", ""))
        if any(doc.startswith(p) for p in cfg["doc_prefixes"]) and not (L.get("htmlFr") or "").strip():
            out.append(doc)
    return out


def claim_path(book: str, slot) -> str:
    cfg = book_cfg(book)
    return f"{CLAIMS}/{cfg['claim_prefix']}{slot}.claim.json"


def try_claim(book: str, slot, trace: str) -> bool:
    os.makedirs(CLAIMS, exist_ok=True)
    path = claim_path(book, slot)
    if os.path.exists(path):
        if claim_age(path) < EXPIRY:
            return False
        try:
            os.unlink(path)
        except OSError:
            return False
    try:
        fd = os.open(path, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o644)
    except FileExistsError:
        return False
    with os.fdopen(fd, "w", encoding="utf-8") as fh:
        json.dump({"utc": utcnow(), "trace_id": trace}, fh, ensure_ascii=False, indent=1)
        fh.write("\n")
    return True


def main() -> None:
    args = sys.argv[1:]
    book = DEFAULT_BOOK
    if "--book" in args:
        i = args.index("--book")
        if i + 1 >= len(args):
            print("REFUS : --book nécessite un nom de livre.")
            sys.exit(1)
        book_cfg(args[i + 1])
        book = args[i + 1]
        args = args[:i] + args[i + 2:]
    if len(args) == 3 and args[0] == "--refresh":
        slot = args[1]
        path = claim_path(book, slot)
        with open(path, "w", encoding="utf-8") as fh:
            json.dump({"utc": utcnow(), "trace_id": args[2]}, fh, ensure_ascii=False, indent=1)
            fh.write("\n")
        print(f"REFRESH : slot {slot} — {utcnow()}")
        return
    if len(args) == 2 and args[0] == "--release":
        try:
            os.unlink(claim_path(book, args[1]))
            print(f"RELEASE : livre {book} slot {args[1]}")
        except OSError:
            print(f"RELEASE : livre {book} slot {args[1]} (déjà absent)")
        return
    if len(args) == 2:
        slot = args[0]
        if slot not in free_slots(book):
            print(f"REFUS : slot {slot} n'est pas libre (déjà livré ou inexistant).")
            sys.exit(3)
        if not try_claim(book, slot, args[1]):
            d = json.load(open(claim_path(book, slot), encoding="utf-8"))
            print(f"REFUS : slot {slot} revendiqué par {d.get('trace_id')} à {d.get('utc')}.")
            sys.exit(4)
        print(f"CLAIM OK : livre {book} slot {slot} — {args[1]} — {utcnow()}")
        return
    print(__doc__)
    sys.exit(1)


if __name__ == "__main__":
    main()

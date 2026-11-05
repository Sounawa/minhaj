#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Minhāj — PARALLÉLISME v4 : revendication atomique PAR LEÇON (demande utilisateur
02-11 soir : maximiser les documents traités — plusieurs ouvriers SIMULTANÉS,
chacun sur une leçon différente, zéro chevauchement). Remplace le verrou global
turn-lock.json (qui forçait les sessions à s'effacer les unes les autres).

GARDE-DOUBLON naturel : on ne peut revendiquer qu'un slot LIBRE (htmlFr vide au
registre tafsir-5ep) sans claim actif — deux ouvriers ne travaillent JAMAIS le
même slot.

Usage :
  python3 scripts-translate/claim-lesson.py --next <trace_id>       # 1er slot libre non revendiqué
  python3 scripts-translate/claim-lesson.py <slot> <trace_id>       # slot précis, ex. 752
  python3 scripts-translate/claim-lesson.py --refresh <slot> <trace_id>  # rafraîchir (longues phases)
  python3 scripts-translate/claim-lesson.py --release <slot>        # libérer (après livraison)

Claim : tr-tmp/claims/<préfixe><slot>.claim.json {"utc", "trace_id"} — création
O_EXCL (atomique entre processus). EXPIRATION : 50 min — un claim périmé
(ouvrier interrompu) peut être repris en takeover (le WIP est sécurisé par git).

LIVRES (extension v4 PARALLÈLE 03-11 : plusieurs ouvrages simultanés) :
  --book tafsir-5ep  (défaut, rétrocompatible : slots numériques 752…)
  --book hadith-2es  (docIds pdf-N, claims préfixés hadith2-pdf-N — convention
                      en vigueur depuis R535 ; registre 30 leçons pdf-1..pdf-31)
"""
import datetime
import json
import os
import sys
import time

HOME = "/home/z/my-project"
CLAIMS = f"{HOME}/tr-tmp/claims"
EXPIRY = 50 * 60  # secondes

BOOKS = {
    "tafsir-5ep": {"registry": "tafsir-5ep.json", "doc_prefix": "pdf-mut23h3c-",
                   "claim_prefix": "", "numeric": True},
    "hadith-2es": {"registry": "hadith-2es.json", "doc_prefix": "pdf-",
                   "claim_prefix": "hadith2-", "numeric": False},
    # extension v4 R589 (ouvrier C) : ulum-hadith-tanawi-1 — docIds pdf-mut23h2q-N
    "ulum-hadith-tanawi-1": {"registry": "ulum-hadith-tanawi-1.json",
                             "doc_prefix": "pdf-mut23h2q-", "claim_prefix": "uh1-",
                             "numeric": False},
}
DEFAULT_BOOK = "tafsir-5ep"


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
        if doc.startswith(cfg["doc_prefix"]) and not (L.get("htmlFr") or "").strip():
            if cfg["numeric"]:
                out.append(int(doc[len(cfg["doc_prefix"]):]))
            else:  # slot = docId complet (pdf-10), claim = hadith2-pdf-10.claim.json
                out.append(doc)
    return out


def norm_slot(book: str, token) -> object:
    """Normalise une saisie : hadith-2es accepte « 10 » ou « pdf-10 » ;
    tafsir-5ep exige un entier (752)."""
    cfg = BOOKS[book]
    s = str(token)
    if cfg["numeric"]:
        return int(s) if s.isdigit() else s
    return s if not s.isdigit() else f"{cfg['doc_prefix']}{s}"


def claim_path(book: str, slot) -> str:
    cfg = book_cfg(book)
    return f"{CLAIMS}/{cfg['claim_prefix']}{slot}.claim.json"


def try_claim(book: str, slot, trace: str) -> bool:
    os.makedirs(CLAIMS, exist_ok=True)
    path = claim_path(book, slot)
    if os.path.exists(path):
        if claim_age(path) < EXPIRY:
            return False
        try:  # takeover : claim périmé, on détrône l'ancien
            os.unlink(path)
        except OSError:
            return False
    try:  # O_EXCL : atomique — deux ouvriers visant le même slot, un seul gagne
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
    if "--book" in args:  # extension v4 : --book <livre> (position libre)
        i = args.index("--book")
        if i + 1 >= len(args):
            print("REFUS : --book nécessite un nom de livre.")
            sys.exit(1)
        book_cfg(args[i + 1])  # valider tôt (exit si inconnu)
        book = args[i + 1]
        args = args[:i] + args[i + 2:]
    if len(args) == 2 and args[0] == "--next":
        for slot in free_slots(book):
            if try_claim(book, slot, args[1]):
                print(f"CLAIM OK : livre {book} slot {slot} — {args[1]} — {utcnow()}")
                return
        print("AUCUN slot libre non revendiqué — la production est déjà couverte.")
        sys.exit(2)
    if len(args) == 3 and args[0] == "--refresh":
        slot = norm_slot(book, args[1])
        path = claim_path(book, slot)
        with open(path, "w", encoding="utf-8") as fh:
            json.dump({"utc": utcnow(), "trace_id": args[2]}, fh, ensure_ascii=False, indent=1)
            fh.write("\n")
        print(f"REFRESH : slot {slot} — {utcnow()}")
        return
    if len(args) == 2 and args[0] == "--release":
        slot = norm_slot(book, args[1])
        try:
            os.unlink(claim_path(book, slot))
            print(f"RELEASE : livre {book} slot {slot}")
        except OSError:
            print(f"RELEASE : livre {book} slot {slot} (déjà absent)")
        return
    if len(args) == 2:
        slot = norm_slot(book, args[0])
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

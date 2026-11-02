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

Claim : tr-tmp/claims/<slot>.claim.json {"utc", "trace_id"} — création O_EXCL
(atomique entre processus). EXPIRATION : 50 min — un claim périmé (ouvrier
interrompu) peut être repris en takeover (le WIP est sécurisé par git).
"""
import datetime
import json
import os
import sys
import time

HOME = "/home/z/my-project"
BOOK = "tafsir-5ep"
CLAIMS = f"{HOME}/tr-tmp/claims"
EXPIRY = 50 * 60  # secondes


def utcnow() -> str:
    return datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def claim_age(path: str) -> float:
    try:
        return time.time() - os.path.getmtime(path)
    except OSError:
        return float("inf")


def free_slots() -> list:
    data = json.load(open(f"{HOME}/content/books/{BOOK}.json", encoding="utf-8"))
    les = data["lessons"] if isinstance(data, dict) else data
    out = []
    for L in les:
        doc = str(L.get("docId", ""))
        if doc.startswith("pdf-mut23h3c-") and not (L.get("htmlFr") or "").strip():
            out.append(int(doc.rsplit("-", 1)[-1]))
    return out


def try_claim(slot: int, trace: str) -> bool:
    os.makedirs(CLAIMS, exist_ok=True)
    path = f"{CLAIMS}/{slot}.claim.json"
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
    if len(args) == 2 and args[0] == "--next":
        for slot in free_slots():
            if try_claim(slot, args[1]):
                print(f"CLAIM OK : slot {slot} — {args[1]} — {utcnow()}")
                return
        print("AUCUN slot libre non revendiqué — la production est déjà couverte.")
        sys.exit(2)
    if len(args) == 3 and args[0] == "--refresh":
        slot = int(args[1])
        path = f"{CLAIMS}/{slot}.claim.json"
        with open(path, "w", encoding="utf-8") as fh:
            json.dump({"utc": utcnow(), "trace_id": args[2]}, fh, ensure_ascii=False, indent=1)
            fh.write("\n")
        print(f"REFRESH : slot {slot} — {utcnow()}")
        return
    if len(args) == 2 and args[0] == "--release":
        slot = int(args[1])
        try:
            os.unlink(f"{CLAIMS}/{slot}.claim.json")
            print(f"RELEASE : slot {slot}")
        except OSError:
            print(f"RELEASE : slot {slot} (déjà absent)")
        return
    if len(args) == 2 and args[0].isdigit():
        slot = int(args[0])
        if slot not in free_slots():
            print(f"REFUS : slot {slot} n'est pas libre (déjà livré ou inexistant).")
            sys.exit(3)
        if not try_claim(slot, args[1]):
            d = json.load(open(f"{CLAIMS}/{slot}.claim.json", encoding="utf-8"))
            print(f"REFUS : slot {slot} revendiqué par {d.get('trace_id')} à {d.get('utc')}.")
            sys.exit(4)
        print(f"CLAIM OK : slot {slot} — {args[1]} — {utcnow()}")
        return
    print(__doc__)
    sys.exit(1)


if __name__ == "__main__":
    main()

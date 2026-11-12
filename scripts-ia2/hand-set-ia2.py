#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# IA-2 — pose d'une traduction main dans le JSON du livre + registre.
# Réplique de hand-set.py (IA-1) adaptée au chemin repo-minhaj ; mêmes garanties :
# garde-doublon (refus si htmlFr non vide et différent), lecture fraîche,
# écriture atomique (tmp + os.replace), inscription registre « hand ».
import json, os, sys, time

HOME = "/home/z/my-project/minhaj"  # chemin poste IA-2 (session web-db9f75eb, Z2-7)
REGISTRY = f"{HOME}/scripts-ia2/savant-registry-ia2.json"
LOCK = REGISTRY + ".lock"

def purge_stale_lock():
    try:
        age = time.time() - os.path.getmtime(LOCK)
        if age > 90:
            os.rmdir(LOCK)
            print(f"⚠︎ verrou périmé ({age:.0f} s) purgé")
    except OSError:
        pass

def acquire_lock():
    purge_stale_lock()
    for _ in range(40):
        try:
            os.mkdir(LOCK)
            return
        except OSError:
            time.sleep(0.25)
    raise RuntimeError("verrou registre occupé après 10 s")

def main():
    args = [a for a in sys.argv[1:] if a != "--force"]
    force = "--force" in sys.argv
    if len(args) not in (3, 4):
        print("Usage: hand-set-ia2.py <bookId> <docId> <fichier.html> [titleFr] [--force]")
        sys.exit(1)
    book_id, doc_id, html_path = args[0], args[1], args[2]
    title_fr = args[3] if len(args) == 4 else None
    html_fr = open(html_path, encoding="utf-8").read()
    path = f"{HOME}/content/books/{book_id}.json"
    acquire_lock()
    try:
        with open(path, encoding="utf-8") as fh:
            data = json.load(fh)
        n = 0
        intro = data.get("intro") or {}
        if str(intro.get("docId")) == doc_id:
            old = str(intro.get("htmlFr") or "").strip()
            if old and old != html_fr.strip() and not force:
                sys.exit(f"REFUS garde-doublon : intro {doc_id} déjà livrée ({len(old)} car)")
            intro["htmlFr"] = html_fr
            data["intro"] = intro
            n += 1
        for lesson in data.get("lessons", []):
            if str(lesson.get("docId")) == doc_id:
                old = str(lesson.get("htmlFr") or "").strip()
                if old and old != html_fr.strip() and not force:
                    sys.exit(f"REFUS garde-doublon : leçon {doc_id} déjà livrée ({len(old)} car)")
                lesson["htmlFr"] = html_fr
                if title_fr and not (lesson.get("titleFr") or "").strip():
                    lesson["titleFr"] = title_fr
                    print(f"  titleFr pose: {title_fr}")
                n += 1
        if n == 0:
            sys.exit(f"AUCUN emplacement {docId:=doc_id} trouvé dans {book_id}")
        tmp = path + ".tmp-ia2"
        with open(tmp, "w", encoding="utf-8") as fh:
            json.dump(data, fh, ensure_ascii=False, indent=2)
        os.replace(tmp, path)
        # registre (fichier IA-2 séparé — pas de collision avec celui d'IA-1)
        reg = {}
        if os.path.exists(REGISTRY):
            try: reg = json.load(open(REGISTRY, encoding="utf-8"))
            except Exception: reg = {}
        reg.setdefault("hand", [])
        reg["hand"] = sorted(set(reg["hand"]) | {f"{book_id}/{doc_id}"})
        rtmp = REGISTRY + ".tmp"
        with open(rtmp, "w", encoding="utf-8") as fh:
            json.dump(reg, fh, ensure_ascii=False, indent=2)
        os.replace(rtmp, REGISTRY)
        print(f"{n} emplacement(s) htmlFr écrit(s) — {book_id}/{doc_id} — "
              f"{len(html_fr)} car FR — registre IA-2 → {len(reg['hand'])} savants")
    finally:
        os.rmdir(LOCK)

if __name__ == "__main__":
    main()

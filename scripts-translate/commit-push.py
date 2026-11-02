#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Minhāj — PARALLÉLISME v4 : section critique git (add + commit + push SÉRIALISÉS
entre ouvriers parallèles). Tous les commits de production passent par ici.

Séquence : verrou mkdir atomique tr-tmp/git.lock (purge > 120 s) →
git add -A → commit (si matière) → fetch origin → rebase origin/main si le
distant a avancé (arbre propre après commit — JAMAIS de reset, JAMAIS de stash) →
push (retry ×3 avec fetch+rebase intercalés).

Usage : python3 scripts-translate/commit-push.py "<message de commit>"
"""
import os
import subprocess
import sys
import time

HOME = "/home/z/my-project"
LOCK = f"{HOME}/tr-tmp/git.lock"


def run(*cmd, check=True):
    r = subprocess.run(cmd, cwd=HOME, capture_output=True, text=True)
    if check and r.returncode != 0:
        raise RuntimeError(f"{' '.join(cmd)} → rc={r.returncode}\n{r.stdout}\n{r.stderr}")
    return r


def purge_stale() -> None:
    try:
        if time.time() - os.path.getmtime(LOCK) > 120:
            os.rmdir(LOCK)
            print("⚠︎ verrou git périmé purgé")
    except OSError:
        pass


def acquire() -> None:
    purge_stale()
    for _ in range(240):  # ≤ 60 s d'attente
        try:
            os.mkdir(LOCK)
            return
        except OSError:
            time.sleep(0.25)
    raise RuntimeError("verrou git occupé après 60 s — réessaie au tour suivant")


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: commit-push.py \"<message de commit>\"")
        sys.exit(1)
    msg = sys.argv[1]
    acquire()
    try:
        st = run("git", "status", "--porcelain").stdout.strip()
        if st:
            run("git", "add", "-A")
            run("git", "commit", "-m", msg)
        else:
            print("(rien à committer — état propre)")
        run("git", "fetch", "origin")
        base = run("git", "merge-base", "--is-ancestor", "origin/main", "main", check=False)
        if base.returncode != 0:
            run("git", "rebase", "origin/main")
        for _ in range(3):
            r = run("git", "push", "origin", "main", check=False)
            if r.returncode == 0:
                head = run("git", "rev-parse", "--short", "HEAD").stdout.strip()
                print(f"PUSH OK — main = {head}")
                return
            run("git", "fetch", "origin")
            run("git", "rebase", "origin/main")
        raise RuntimeError("push refusé après 3 essais (rebase inclus) — ALERTE si récurrent")
    finally:
        try:
            os.rmdir(LOCK)
        except OSError:
            pass


if __name__ == "__main__":
    main()

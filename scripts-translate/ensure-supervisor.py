#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Minhāj — ensure-supervisor.py (R457)

Relance idempotente du superviseur de production 24/7. Conçu pour être appelé :
  • au démarrage du serveur dev (préfixe du script "dev" de package.json) —
    c'est LE mécanisme d'immortalité : chaque réveil du sandbox relance
    `bun run dev`, qui relance le superviseur ;
  • à la main : python3 scripts-translate/ensure-supervisor.py

Garanties :
  • toujours < 2 s, toujours exit 0 (ne peut JAMAIS bloquer le dev server) ;
  • verrou flock anti-double-lancement ;
  • si un superviseur vit déjà (pgrep + fenêtre de battement), ne fait rien ;
  • journalise dans tr-logs/ensure.log.
"""
import fcntl
import os
import subprocess
import sys
import time

HOME = "/home/z/my-project"
LOCK = os.path.join(HOME, "tr-logs", "ensure.lock")
STATE = os.path.join(HOME, "tr-logs", "pipeline-status.json")
LOG = os.path.join(HOME, "tr-logs", "ensure.log")
SUPERVISOR = os.path.join(HOME, "scripts-translate", "supervisor.py")


def log(msg: str) -> None:
    try:
        os.makedirs(os.path.dirname(LOG), exist_ok=True)
        stamp = time.strftime("%Y-%m-%d %H:%M:%S")
        with open(LOG, "a", buffering=1) as fh:
            fh.write(f"[{stamp}] {msg}\n")
    except Exception:
        pass  # le journal ne doit jamais faire échouer la relance


def supervisor_alive() -> bool:
    """Un superviseur vit-il ? (processus uniquement — le flock de relance
    gère les courses concurrentes ; le battement n'est plus un critère :
    il bloquait la relance juste après un kill manuel.)"""
    try:
        proc = subprocess.run(
            ["pgrep", "-f", "scripts-translate/supervisor.py"],
            capture_output=True, text=True, timeout=8,
        )
        return bool(proc.stdout.strip())
    except Exception:
        return False


def main() -> int:
    try:
        os.makedirs(os.path.join(HOME, "tr-logs"), exist_ok=True)
        lock_fh = open(LOCK, "w")
        try:
            fcntl.flock(lock_fh, fcntl.LOCK_EX | fcntl.LOCK_NB)
        except OSError:
            log("ensure: verrou occupé — une autre relance est en cours, on rend la main.")
            return 0
        if supervisor_alive():
            log("ensure: superviseur déjà vivant — rien à faire.")
            return 0
        # Lancement démonisé, détaché du dev server (survit à la session).
        subprocess.run(
            ["setsid", "-f", "python3", SUPERVISOR],
            cwd=HOME,
            stdin=subprocess.DEVNULL,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            timeout=15,
        )
        log("ensure: superviseur (re)lancé en arrière-plan.")
    except Exception as exc:
        log(f"ensure: incident non bloquant — {exc!r}")
    return 0  # TOUJOURS 0 : le dev server ne doit jamais être retenu.


if __name__ == "__main__":
    sys.exit(main())

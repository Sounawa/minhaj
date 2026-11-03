# -*- coding: utf-8 -*-
"""Minhāj — ÉTAPE 2 auth persistante (post-recyclage 03-11 : $HOME effacé).

Le token GitHub fourni par l'utilisateur au chat (01-11 20:31+08) résidait dans
$HOME (~/.git-credentials) — emplacement EFFACÉ par le recyclage du bac à sable.
Correctif durable : le token vit désormais dans /home/z/my-project/.auth/gh-token
(répertoire du dépôt, PERSISTANT aux recycles, jamais commité — entrée .gitignore).

Usage : python3 scripts-translate/ensure-auth.py   (silencieux si pas de token)
  - token présent  → remote origin reconfiguré avec le token (comme avant) ;
  - token absent   → sortie 0 avec message, la passe continue (commits locaux).
NE JAMAIS AFFICHER LE TOKEN (aucun echo, aucun log)."""
import os
import re
import subprocess
import sys

HOME = "/home/z/my-project"
AUTH = f"{HOME}/.auth/gh-token"
URL_BASE = "https://github.com/Sounawa/minhaj.git"


def main() -> None:
    os.makedirs(os.path.dirname(AUTH), exist_ok=True)
    try:
        os.chmod(os.path.dirname(AUTH), 0o700)
    except OSError:
        pass
    if not os.path.exists(AUTH):
        print("AUTH : pas de token en dépôt local (.auth/gh-token) — pushes en attente.")
        return
    try:
        os.chmod(AUTH, 0o600)
        tok = open(AUTH, encoding="utf-8").read().strip()
        if not tok:
            print("AUTH : fichier token vide — pushes en attente.")
            return
        url = f"https://{tok}@github.com/Sounawa/minhaj.git"
        cur = subprocess.run(["git", "config", "--get", "remote.origin.url"],
                             cwd=HOME, capture_output=True, text=True).stdout.strip()
        if cur == url:
            print("AUTH : remote déjà authentifié.")
            return
        subprocess.run(["git", "remote", "set-url", "origin", url],
                       cwd=HOME, check=True, capture_output=True)
        print("AUTH : remote origin authentifié (token jamais affiché).")
    except Exception as exc:  # noqa: BLE001 — ne jamais casser une passe pour l'auth
        print(f"AUTH : échec non bloquant ({type(exc).__name__}).")


if __name__ == "__main__":
    sys.exit(main())

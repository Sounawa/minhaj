#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Runner de tour de veille consolidé — déployé au tour R433 (instruction utilisateur : efficacité).

Un seul appel au lieu de trois. Mêmes garanties :
  1. VÉRIFICATION contre la réalité (zéro confiance aux chiffres en cache) :
     fetch + rev-list == 0 0, HEAD == attendu, worklog == lignes attendues.
  2. GARDE RENFORCÉE (GARDE-DOUBLON.md) : scan entier, refus si dernier ID >= N.
  3. CANARI : verdict INEXECUTABLE requis pour appender une veille ;
     verdict EXÉCUTABLE → abort code 2 (lancer le protocole OCR de 311).
  4. APPEND + commit + re-vérification rev-list (1 0) AU MOMENT du push + backup.
Toute incohérence → ABANDON sans append, traitement manuel.

Usage: tour-veille-rapide.py N entry_file expected_head expected_lines "commit message"
"""
import io, re, subprocess, sys

WORKLOG = "/home/z/my-project/worklog.md"

def run(cmd):
    return subprocess.run(cmd, shell=True, capture_output=True, text=True)

def die(msg):
    print("ABANDON :", msg)
    sys.exit(1)

N = int(sys.argv[1])
entry_file = sys.argv[2]
exp_head = sys.argv[3]
exp_lines = int(sys.argv[4])
commit_msg = sys.argv[5] if len(sys.argv) > 5 else f"worklog: R{N} entry (tour de veille rapide)"

# 1. Conformité GitHub
r = run("cd /home/z/my-project && git fetch origin && git rev-list --left-right --count HEAD...origin/main")
if r.returncode != 0:
    die(f"fetch/rev-list échoué: {r.stderr[:200]}")
count = r.stdout.strip().replace("\t", " ")
if count != "0 0":
    die(f"sync git = '{count}' (attendu '0 0') — traiter la conformité manuellement.")
r = run("cd /home/z/my-project && git log --oneline -1")
head = r.stdout.split()[0] if r.stdout else "?"
if head != exp_head:
    die(f"HEAD {head} != attendu {exp_head} — état inattendu.")

# 2. Worklog + garde renforcée
with io.open(WORKLOG, "r", encoding="utf-8") as f:
    content = f.read()
lines = len(content.splitlines())
if lines != exp_lines:
    die(f"worklog {lines} lignes != attendu {exp_lines} — état inattendu.")
ids = re.findall(r"Task ID: R(\d+)", content)
if ids and int(ids[-1]) >= N:
    die(f"garde renforcée : une entrée >= R{N} existe déjà (dernier = R{ids[-1]}).")
if f"Task ID: R{N}" in content:
    die(f"garde absolue : R{N} déjà présent.")

# 3. Canaris (règle cx' — R433 : portail d'abord, 311 ensuite)
r = run("cd /home/z/my-project && bash scripts-translate/veille-portail.sh 2>&1")
portail = r.stdout
if "PORTE|OUVERTE" in portail:
    print(f"PORTE|OUVERTE → lancer bash scripts-translate/reprise-portail.sh puis re-mapping des 853. Sortie: {portail[-300:]}")
    sys.exit(3)
print("PORTAIL : PORTE|FERMÉE" if "PORTE|FERMÉE" in portail else "PORTAIL : sortie inattendue — " + portail[-120:])
r = run("cd /home/z/my-project && bash scripts-translate/veille-311.sh 2>&1 | tail -2")
out = r.stdout.strip()
print("311 :", out.splitlines()[-1] if out else "?")
if "INEXECUTABLE" not in out:
    print(f"CANARI EXÉCUTABLE → PAS de veille. Lancer le protocole OCR de la leçon 311. Sortie: {out}")
    sys.exit(2)

# 4. Append
with io.open(entry_file, "r", encoding="utf-8") as f:
    entry = f.read()
with io.open(WORKLOG, "a", encoding="utf-8") as f:
    f.write(entry)
print(f"R{N} apposé ({lines} → {lines + len(entry.splitlines())} lignes).")

# 5. Commit + vérification AU MOMENT du push + backup
r = run(f"cd /home/z/my-project && git add -A && git commit --quiet -m {repr(commit_msg)}")
if r.returncode != 0:
    die(f"commit échoué: {r.stderr[:200]}")
r = run("cd /home/z/my-project && git fetch origin && git rev-list --left-right --count HEAD...origin/main")
count = r.stdout.strip().replace("\t", " ")
if count != "1 0":
    die(f"rev-list post-commit = '{count}' (attendu '1 0') — push annulé, traiter manuellement (rebase sur origin/main si 1 1).")
r = run("cd /home/z/my-project && git push origin main --quiet && echo PUSH_OK && git log --oneline -1")
print(r.stdout.strip() or r.stderr[:200])
if "PUSH_OK" not in r.stdout:
    die("push échoué — reconstruire ~/.git-credentials puis re-pousser.")
r = run("cd /home/z/my-project && bash scripts-translate/backup.sh 2>&1 | tail -1")
print(r.stdout.strip())
print("TOUR COMPLET.")

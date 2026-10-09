#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Minhāj — Superviseur de production 24/7.

Maintient en permanence MAX workers llm-translate actifs et enchaîne
automiquement les livres restants dans l'ordre pédagogique :

  1. Primaire (fin du cycle 4ep/5ep/6ep — les 3 workers en cours sont
     détectés via pgrep et jamais dupliqués),
  2. Tanawī 1 → 2 → 3,
  3. Secondaire 1es → 2es → 3es + Waraqāt.

Sûreté :
  • un livre n'est JAMAIS lancé en double (détection pgrep du worker) ;
  • maximum 2 passes par livre (la 2e passe rattrape les docs rejetés ;
    le registre savant empêche toute refusion des docs déjà faits) ;
  • lancements espacés de 25 s pour éviter les rafales 429 ;
  • état persistant /home/z/tr-logs/supervisor-state.json (reprise après
    redémarrage : les workers en cours sont détectés, les livres déjà
    passés 2 fois sont abandonnés) ;
  • sortie propre quand la file est épuisée.

Lancement (démon détaché, survit à la session) :
  setsid -f python3 /home/z/my-project/scripts-translate/supervisor.py
"""

import json
import os
import shlex
import subprocess
import time

HOME = "/home/z/my-project"
LOGS = "/home/z/tr-logs"
STATE_PATH = os.path.join(LOGS, "supervisor-state.json")
LOG_PATH = os.path.join(LOGS, "supervisor.log")
MAX_CONCURRENT = 3          # workers simultanés (quota LLM : 3 = stable)
CYCLE_SECONDS = 60          # période de supervision
STAGGER_SECONDS = 25        # délai entre deux lancements
MAX_PASSES_PER_BOOK = 2     # 2 passes max / livre (rattrapage des rejets)

# ── File ordonnée (primaire → tanawī → secondaire) ─────────────────────────
QUEUE = [
    # Primaire — fin du cycle (3 premiers = workers déjà en cours)
    "tafsir-5ep", "fiqh-6ep", "tafsir-6ep",
    "tajwid-5ep", "tajwid-6ep", "rasm-wa-dabt-4ep",
    "fiqh-1ep", "tafsir-1ep", "fiqh-5ep", "hadith-5ep",
    "hadith-6ep", "rasm-wa-dabt-5ep",
    "usul-qiyam-4ep", "usul-qiyam-5ep", "usul-qiyam-6ep", "rasm-wa-dabt-6ep",
    # Tanawī — 1re année
    "fiqh-tanawi-1", "hadith-tanawi-1", "tafsir-tanawi-1",
    "mantiq-tanawi-1", "taqtit-tanawi-1", "qiraat-tanawi-1",
    "usul-fiqh-tanawi-1", "ulum-hadith-tanawi-1", "fikr-islami-tanawi-1",
    # Tanawī — 2e année
    "fiqh-tanawi-2", "tafsir-tanawi-2", "hadith-tanawi-2",
    "usul-fiqh-tanawi-2", "ulum-hadith-tanawi-2", "qiraat-tanawi-2",
    "taqtit-tanawi-2", "fikr-islami-tanawi-2",
    # Tanawī — 3e année
    "fiqh-tanawi-3", "tafsir-tanawi-3", "hadith-tanawi-3",
    "faraid-tanawi-3", "usul-fiqh-tanawi-3", "ulum-hadith-tanawi-3",
    "qiraat-tanawi-3", "taqtit-tanawi-3", "fikr-islami-tanawi-3",
    # Secondaire — 1re année
    "hadith-1es", "fiqh-1es", "tafsir-1es",
    "tawhid-1es", "sira-1es", "ulum-quran-1es",
    # Secondaire — 2e année
    "sira-2es", "tajwid-2es", "ulum-quran-2es", "tawhid-2es",
    "tafsir-2es", "fiqh-2es", "hadith-2es",
    # Secondaire — 3e année + Waraqāt
    "ulum-quran-3es", "usul-fiqh-waraqat", "sira-3es",
    "tafsir-3es", "fiqh-3es", "hadith-3es", "tajwid-3es",
]


def log(msg: str) -> None:
    stamp = time.strftime("%Y-%m-%d %H:%M:%S")
    with open(LOG_PATH, "a", buffering=1) as fh:
        fh.write(f"[{stamp}] {msg}\n")


def load_state() -> dict:
    try:
        with open(STATE_PATH, "r", encoding="utf-8") as fh:
            return json.load(fh)
    except (OSError, ValueError):
        return {}


def save_state(state: dict) -> None:
    tmp = STATE_PATH + ".tmp"
    with open(tmp, "w", encoding="utf-8") as fh:
        json.dump(state, fh, indent=1, ensure_ascii=False)
    os.replace(tmp, STATE_PATH)


def worker_snapshot() -> tuple[set[str], int]:
    """Livres en cours de traitement + nombre total de processus workers."""
    try:
        proc = subprocess.run(
            ["pgrep", "-af", "llm-translate.ts --book"],
            capture_output=True, text=True, timeout=15,
        )
        lines = [ln for ln in proc.stdout.splitlines() if ln.strip()]
    except Exception:
        return set(), 0
    books: set[str] = set()
    for line in lines:
        for b in QUEUE:
            if f"--book {b} " in line or line.rstrip().endswith(f"--book {b}"):
                books.add(b)
    return books, len(lines)


def launch_worker(book: str) -> None:
    inner = (
        f"cd {shlex.quote(HOME)} && bun run scripts-translate/llm-translate.ts "
        f"--book {shlex.quote(book)} --thinking >> {LOGS}/{book}.log 2>&1"
    )
    subprocess.run(
        ["setsid", "-f", "bash", "-c", inner],
        capture_output=True, timeout=30,
    )


def main() -> None:
    os.makedirs(LOGS, exist_ok=True)
    state = load_state()
    log(f"superviseur démarré (MAX={MAX_CONCURRENT}, file={len(QUEUE)} livres, "
        f"état existant={len(state)} livres déjà passés)")

    while True:
        running, active = worker_snapshot()
        launched_this_cycle = 0

        for book in QUEUE:
            if active >= MAX_CONCURRENT:
                break
            if book in running:
                continue
            if state.get(book, 0) >= MAX_PASSES_PER_BOOK:
                continue
            launch_worker(book)
            state[book] = state.get(book, 0) + 1
            save_state(state)
            log(f"worker lancé : {book} (passe {state[book]}, actifs≈{active + 1})")
            launched_this_cycle += 1
            active += 1
            running.add(book)
            time.sleep(STAGGER_SECONDS)

        if launched_this_cycle == 0:
            # Rien à lancer : soit tous occupés, soit file épuisée.
            exhausted = all(state.get(b, 0) >= MAX_PASSES_PER_BOOK for b in QUEUE)
            if exhausted and active == 0:
                log("file épuisée : tous les livres ont eu leurs 2 passes — sortie.")
                break
            time.sleep(CYCLE_SECONDS)
        else:
            time.sleep(CYCLE_SECONDS)

    log("superviseur arrêté.")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Minhāj — Superviseur de production 24/7 (v3).

Maintient en permanence MAX_CONCURRENT workers llm-translate actifs et
enchaîne automatiquement les livres restants dans l'ordre pédagogique :

  1. Primaire (fin du cycle 4ep/5ep/6ep),
  2. Tanawī 1 → 2 → 3,
  3. Secondaire 1es → 2es → 3es + Waraqāt.

v3 — la vérité terrain est le REGISTRE (scripts-translate/savant-registry.json) :
  • un livre est « fini » quand il a 0 doc restant (registre + html non vide) ;
  • le compteur de passes n'est plus qu'un garde-fou (cap 4) contre les
    docs pathologiques rejetés en boucle — il ne peut plus abandonner un
    livre à cause d'une famine de quota 429 temporaire ;
  • les workers ne meurent jamais d'un 429 (retry par doc dans
    llm-translate.ts) — seuls les reboots sandbox les tuent.

Sûreté :
  • un livre n'est JAMAIS lancé en double (détection pgrep du worker) ;
  • lancements espacés de 25 s (anti-rafales 429) ;
  • logs et état dans {projet}/tr-logs (persistant, gitignoré —
    l'ancien /home/z/tr-logs était EFFACÉ à chaque reboot sandbox) ;
  • lecture registre/livre blindée : fichier illisible → cycle suivant ;
  • sortie propre quand TOUS les livres sont finis (0 doc restant).

Lancement (démon détaché, survit à la session) :
  setsid -f python3 /home/z/my-project/scripts-translate/supervisor.py
"""

import json
import os
import shlex
import subprocess
import time

HOME = "/home/z/my-project"
LOGS = os.path.join(HOME, "tr-logs")  # persistant (dans le projet, gitignoré)
STATE_PATH = os.path.join(LOGS, "supervisor-state.json")
LOG_PATH = os.path.join(LOGS, "supervisor.log")
REGISTRY_PATH = os.path.join(HOME, "scripts-translate", "savant-registry.json")
MAX_CONCURRENT = 3          # workers simultanés (quota LLM : 3 = stable)
CYCLE_SECONDS = 60          # période de supervision
STAGGER_SECONDS = 25        # délai entre deux lancements
MAX_PASSES_PER_BOOK = 4     # garde-fou anti-docs-pathologiques (pas un critère d'abandon)

# ── File ordonnée (primaire → tanawī → secondaire) ─────────────────────────
QUEUE = [
    # Primaire — fin du cycle
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
    """state = {livre: {"passes": int, "done": bool}} (tolère l'ancien format int)."""
    try:
        with open(STATE_PATH, "r", encoding="utf-8") as fh:
            raw = json.load(fh)
    except (OSError, ValueError):
        return {}
    clean_state = {}
    for book, val in raw.items():
        if isinstance(val, dict):
            clean_state[book] = {"passes": int(val.get("passes", 0)), "done": bool(val.get("done", False))}
        else:  # ancien format : int = nb de passes
            clean_state[book] = {"passes": int(val), "done": False}
    return clean_state


def save_state(state: dict) -> None:
    tmp = STATE_PATH + ".tmp"
    with open(tmp, "w", encoding="utf-8") as fh:
        json.dump(state, fh, indent=1, ensure_ascii=False)
    os.replace(tmp, STATE_PATH)


def remaining_docs(book: str) -> int | None:
    """Docs savants restants d'un livre. None = registre/livre illisible
    (réécriture en cours par un worker) → on reessaiera au cycle suivant."""
    try:
        with open(REGISTRY_PATH, "r", encoding="utf-8") as fh:
            reg = json.load(fh)
        done = set(reg.get("hand", [])) | set(reg.get("llm", {}).keys())
        with open(os.path.join(HOME, "content", "books", f"{book}.json"), "r", encoding="utf-8") as fh:
            data = json.load(fh)
        cnt = 0
        intro = data.get("intro") or {}
        if (intro.get("html") or "").strip() and str(intro.get("docId")) not in done:
            cnt += 1
        for lesson in data.get("lessons", []):
            if (lesson.get("html") or "").strip() and str(lesson.get("docId")) not in done:
                cnt += 1
        return cnt
    except Exception:
        return None


def worker_snapshot() -> tuple[set[str], int]:
    """Livres en cours de traitement + nombre de workers (livres uniques)."""
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
    return books, len(books)


def launch_worker(book: str) -> None:
    """Lance un worker daemonisé.

    IMPORTANT : ne PAS utiliser capture_output/pipe — le démon enfant
    hériterait du write-end du pipe et subprocess.run() attendrait EOF
    jusqu'au timeout. On utilise DEVNULL : setsid -f fork et son parent
    sort immédiatement. `exec` évite le processus bash parent.
    """
    inner = (
        f"cd {shlex.quote(HOME)} && exec bun run scripts-translate/llm-translate.ts "
        f"--book {shlex.quote(book)} --thinking >> {LOGS}/{book}.log 2>&1"
    )
    subprocess.run(
        ["setsid", "-f", "bash", "-c", inner],
        stdin=subprocess.DEVNULL,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        timeout=30,
    )


def main() -> None:
    os.makedirs(LOGS, exist_ok=True)
    state = load_state()
    log(f"superviseur v3 démarré (MAX={MAX_CONCURRENT}, file={len(QUEUE)} livres)")

    while True:
        try:
            running, active = worker_snapshot()
            launched_this_cycle = 0

            for book in QUEUE:
                if active >= MAX_CONCURRENT:
                    break
                if book in running:
                    continue
                if state.get(book, {}).get("done", False):
                    continue
                if state.get(book, {}).get("passes", 0) >= MAX_PASSES_PER_BOOK:
                    continue  # garde-fou pathologique (uniquement si des docs restent)
                rem = remaining_docs(book)
                if rem is None:
                    continue  # illisible pour l'instant → cycle suivant
                if rem == 0:
                    if not state.get(book, {}).get("done", False):
                        state.setdefault(book, {"passes": 0, "done": False})
                        state[book]["done"] = True
                        save_state(state)
                        log(f"livre TERMINÉ : {book} (0 doc restant)")
                    continue
                launch_worker(book)
                state.setdefault(book, {"passes": 0, "done": False})
                state[book]["passes"] += 1
                save_state(state)
                log(f"worker lancé : {book} (passe {state[book]['passes']}, "
                    f"{rem} docs restants, actifs≈{active + 1})")
                launched_this_cycle += 1
                active += 1
                running.add(book)
                time.sleep(STAGGER_SECONDS)

            # Sortie propre : tous les livres finis et aucun worker actif.
            if active == 0 and launched_this_cycle == 0:
                unfinished = []
                for b in QUEUE:
                    if state.get(b, {}).get("done", False):
                        continue
                    rem = remaining_docs(b)
                    if rem:  # None (illisible) → considéré non fini, on boucle encore
                        unfinished.append(b)
                    elif rem == 0:
                        state.setdefault(b, {"passes": 0, "done": False})
                        state[b]["done"] = True
                        save_state(state)
                        log(f"livre TERMINÉ : {b} (0 doc restant)")
                if not unfinished:
                    log("file épuisée : tous les livres sont terminés — sortie.")
                    break
        except Exception as exc:  # le superviseur ne meurt JAMAIS d'un incident
            log(f"⚠ incident de cycle (ignoré, cycle suivant) : {exc!r}")
            time.sleep(CYCLE_SECONDS)
            continue

        time.sleep(CYCLE_SECONDS)

    log("superviseur arrêté.")


if __name__ == "__main__":
    main()

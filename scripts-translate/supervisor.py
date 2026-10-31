#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Minhāj — Superviseur de production 24/7 (v4, R457).

v4 — « ça doit avancer sans moi » (directive utilisateur R456/R457) :
  • BATTEMENT VISIBLE : pipeline-status.json à chaque cycle (60 s) +
    ligne TICK dans tr-tmp/cron-alive.log toutes les 5 min — le même
    journal que le cron de production devait tenir et ne tenait pas ;
  • IMMORTALITÉ : relancé par ensure-supervisor.py au démarrage du dev
    server (préfixe du script "dev" de package.json) — chaque réveil du
    sandbox relance bun run dev, donc le superviseur ;
  • DÉTECTION DE RÉVEIL : un écart > 3 cycles se journalise (mesure
    honnête des gels du sandbox) ;
  • CANARI PORTE toutes les 15 min (veille-portail.sh) ; PORTE|OUVERTE →
    reprise-portail.sh lancé automatiquement ;
  • CHASSE AUX SOURCES toutes les 30 min : sonde directe du pdfUrl de la
    prochaine leçon vide (retour 200 = arbre portail revivant → PDF
    téléchargé dans sources-inbox/, source officielle exacte = zéro risque
    d'édition) + sonde Wayback (archive.org/wayback/available) journalisée ;
  • AUTO-COMMIT/PUSH toutes les 10 min : les workers llm-translate
    commitent mais ne poussent PAS — le superviseur pousse (garde fetch +
    rev-list), paths pipeline uniquement (jamais worklog.md, jamais les
    fichiers de session) ;
  • NE SORT JAMAIS : la file peut être vide, le battement continue.

v3 (conservé) : workers llm-translate lancés/maintenus à MAX_CONCURRENT,
registre = vérité terrain, cap anti-pathologiques, lancements espacés.

Lancement : setsid -f python3 scripts-translate/supervisor.py
(relance idempotente : scripts-translate/ensure-supervisor.py)
"""

import json
import os
import re
import shlex
import ssl
import subprocess
import time
import urllib.parse
import urllib.request

HOME = "/home/z/my-project"
LOGS = os.path.join(HOME, "tr-logs")
STATE_PATH = os.path.join(LOGS, "supervisor-state.json")
LOG_PATH = os.path.join(LOGS, "supervisor.log")
STATUS_PATH = os.path.join(LOGS, "pipeline-status.json")
ALIVE_LOG = os.path.join(HOME, "tr-tmp", "cron-alive.log")
HUNT_LOG = os.path.join(LOGS, "source-hunt.log")
INBOX = os.path.join(HOME, "sources-inbox")

# ── Miroir archive.org (contournement portail fermé) ─────────────────────────
# Découverte R458 : le portail Habous étant fermé (bannière de maintenance,
# PDF 404), la collection « سلسلة كتب التعليم العتيق المغربي » (item
# 1_20220304_20220304_2251, 77 PDF — manuels complets avec couche texte
# dérivée «_text.pdf») est JOIGNABLE depuis la sandbox (seul web.archive.org
# est bloqué au réseau). La chasse s'y ravitaille : le segment arabe de la
# série du pdfUrl (ex. التفسير-الثانية-ثانوي) désigne le manuel complet
# correspondant (كتاب التفسير 2 ثانوي_text.pdf) — téléchargé en cache local.
COLLECTION_ITEM = "1_20220304_20220304_2251"
COLLECTION_DIR = os.path.join(HOME, "content", "textbooks-src")
COLLECTION_CACHE = os.path.join(LOGS, "collection-files.json")
COLLECTION_CACHE_TTL = 86400  # s — rafraîchissement de la liste des fichiers

SUBJECT_SLUGS = {
    "التفسير": "tafsir", "الحديث": "hadith", "الفقه": "fiqh",
    "اصولالفقه": "usul-fiqh", "التوقيت": "taqtit", "القراءات": "qiraat",
    "الفكرالاسلامي": "fikr-islami", "السيرة": "sira", "التوحيد": "tawhid",
    "المنطق": "mantiq", "علومالقران": "ulum-quran", "علومالحديث": "ulum-hadith",
    "الفرائض": "faraid",
}
YEAR_WORDS = {
    "الاولى": 1, "الاول": 1, "الثانية": 2, "الثاني": 2, "الثالثة": 3,
    "الثالث": 3, "الرابعة": 4, "الرابع": 4, "الخامسة": 5, "الخامس": 5,
    "السادسة": 6, "السادس": 6,
}
CYCLE_SLUGS = {"ثانوي": "thanawi", "اعدادي": "iadadi", "ابتدائي": "ibtidai"}
# repli matière : préfixe de l'ID de livre (quand le segment du portail est pauvre)
BOOK_SUBJECTS = {
    "tafsir": "التفسير", "hadith": "الحديث", "fiqh": "الفقه", "faraid": "الفرائض",
    "tajwid": "التجويد", "qiraat": "القراءات", "taqtit": "التوقيت", "sira": "السيرة",
    "tawhid": "التوحيد", "mantiq": "المنطق", "fikr-islami": "الفكرالاسلامي",
    "usul-fiqh": "اصولالفقه", "ulum-hadith": "علومالحديث", "ulum-quran": "علومالقران",
    "rasm-wa-dabt": "الرسموالضبط",
}
REGISTRY_PATH = os.path.join(HOME, "scripts-translate", "savant-registry.json")
VEILLE = os.path.join(HOME, "scripts-translate", "veille-portail.sh")
REPRISE = os.path.join(HOME, "scripts-translate", "reprise-portail.sh")

MAX_CONCURRENT = 3          # workers simultanés (quota LLM : 3 = stable)
CYCLE_SECONDS = 60          # période de supervision
STAGGER_SECONDS = 25        # délai entre deux lancements de workers
MAX_PASSES_PER_BOOK = 4     # garde-fou anti-docs-pathologiques
HEARTBEAT_EVERY = 300       # s — ligne TICK dans cron-alive.log
CANARY_EVERY = 900          # s — canari portail
HUNT_EVERY = 1800           # s — chasse aux sources
AUTOCOMMIT_EVERY = 600      # s — commit + push des paths pipeline
RESCAN_EVERY = 300          # s — recalcul du reste global (coûteux)

# File ordonnée (primaire → tanawī → secondaire) — v3 inchangée.
QUEUE = [
    "tafsir-5ep", "fiqh-6ep", "tafsir-6ep",
    "tajwid-5ep", "tajwid-6ep", "rasm-wa-dabt-4ep",
    "fiqh-1ep", "tafsir-1ep", "fiqh-5ep", "hadith-5ep",
    "hadith-6ep", "rasm-wa-dabt-5ep",
    "usul-qiyam-4ep", "usul-qiyam-5ep", "usul-qiyam-6ep", "rasm-wa-dabt-6ep",
    "fiqh-tanawi-1", "hadith-tanawi-1", "tafsir-tanawi-1",
    "mantiq-tanawi-1", "taqtit-tanawi-1", "qiraat-tanawi-1",
    "usul-fiqh-tanawi-1", "ulum-hadith-tanawi-1", "fikr-islami-tanawi-1",
    "fiqh-tanawi-2", "tafsir-tanawi-2", "hadith-tanawi-2",
    "usul-fiqh-tanawi-2", "ulum-hadith-tanawi-2", "qiraat-tanawi-2",
    "taqtit-tanawi-2", "fikr-islami-tanawi-2",
    "fiqh-tanawi-3", "tafsir-tanawi-3", "hadith-tanawi-3",
    "faraid-tanawi-3", "usul-fiqh-tanawi-3", "ulum-hadith-tanawi-3",
    "qiraat-tanawi-3", "taqtit-tanawi-3", "fikr-islami-tanawi-3",
    "hadith-1es", "fiqh-1es", "tafsir-1es",
    "tawhid-1es", "sira-1es", "ulum-quran-1es",
    "sira-2es", "tajwid-2es", "ulum-quran-2es", "tawhid-2es",
    "tafsir-2es", "fiqh-2es", "hadith-2es",
    "ulum-quran-3es", "usul-fiqh-waraqat", "sira-3es",
    "tafsir-3es", "fiqh-3es", "hadith-3es", "tajwid-3es",
]

AUTO_ADD_PATHS = [
    "content/books",
    "scripts-translate/savant-registry.json",
]

# habous.gov.ma sert une chaîne de certificats incomplète (le canari curl -k
# passe depuis toujours) : contexte sans vérification pour les sondes.
SSL_CTX = ssl.create_default_context()
SSL_CTX.check_hostname = False
SSL_CTX.verify_mode = ssl.CERT_NONE


def log(msg: str) -> None:
    stamp = time.strftime("%Y-%m-%d %H:%M:%S")
    try:
        with open(LOG_PATH, "a", buffering=1) as fh:
            fh.write(f"[{stamp}] {msg}\n")
    except Exception:
        pass


def alive_line(msg: str) -> None:
    """Le battement public — le journal que l'utilisateur peut lire."""
    try:
        os.makedirs(os.path.dirname(ALIVE_LOG), exist_ok=True)
        stamp = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
        with open(ALIVE_LOG, "a", buffering=1) as fh:
            fh.write(f"{stamp} {msg}\n")
    except Exception:
        pass


# ── État superviseur (passes par livre) ───────────────────────────────────────

# Clés méta du state v4 — jamais des livres (le chargeur doit les ignorer).
STATE_META_KEYS = {"startedAt", "cycles", "wakeCount"}


def load_state() -> dict:
    try:
        with open(STATE_PATH, "r", encoding="utf-8") as fh:
            raw = json.load(fh)
    except (OSError, ValueError):
        return {}
    clean = {}
    for book, val in raw.items():
        if book in STATE_META_KEYS:
            clean[book] = val  # méta conservée telle quelle
            continue
        try:
            if isinstance(val, dict):
                clean[book] = {"passes": int(val.get("passes", 0)), "done": bool(val.get("done", False))}
            else:
                clean[book] = {"passes": int(val), "done": False}
        except (TypeError, ValueError):
            continue  # entrée corrompue : on repart à zéro pour ce livre
    return clean


def save_state(state: dict) -> None:
    tmp = STATE_PATH + ".tmp"
    with open(tmp, "w", encoding="utf-8") as fh:
        json.dump(state, fh, indent=1, ensure_ascii=False)
    os.replace(tmp, STATE_PATH)


# ── Corpus ────────────────────────────────────────────────────────────────────

def load_registry_counts() -> dict:
    try:
        with open(REGISTRY_PATH, "r", encoding="utf-8") as fh:
            reg = json.load(fh)
        return {"hand": len(reg.get("hand", [])), "llm": len(reg.get("llm", {}))}
    except Exception:
        return {}


def remaining_docs(book: str) -> int | None:
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


def global_scan() -> dict:
    """Reste global + prochaine leçon vide prioritaire (pour la chasse)."""
    total = 0
    done = set()
    try:
        with open(REGISTRY_PATH, "r", encoding="utf-8") as fh:
            reg = json.load(fh)
        done = set(reg.get("hand", [])) | set(reg.get("llm", {}).keys())
    except Exception:
        return {"remaining": None, "nextEmpty": None}
    nxt = None
    for book in QUEUE:
        try:
            with open(os.path.join(HOME, "content", "books", f"{book}.json"), "r", encoding="utf-8") as fh:
                data = json.load(fh)
        except Exception:
            continue
        for lesson in data.get("lessons", []):
            if (lesson.get("html") or "").strip():
                if str(lesson.get("docId")) not in done:
                    total += 1
            elif nxt is None and lesson.get("pdfUrl"):
                nxt = {"book": book, "docId": str(lesson.get("docId")),
                       "pdfUrl": lesson.get("pdfUrl"), "titleFr": lesson.get("titleFr", "")}
        intro = data.get("intro") or {}
        if (intro.get("html") or "").strip() and str(intro.get("docId")) not in done:
            total += 1
        if nxt is not None and total:
            pass  # on continue : total exact demanded
    return {"remaining": total, "nextEmpty": nxt}


# ── Workers (v3 inchangé) ─────────────────────────────────────────────────────

def worker_snapshot() -> tuple[set[str], int]:
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


# ── Canari portail ────────────────────────────────────────────────────────────

def canary_portal(state: dict) -> None:
    try:
        proc = subprocess.run(
            ["bash", VEILLE], capture_output=True, text=True, timeout=90, cwd=HOME,
        )
        out = proc.stdout or ""
    except Exception as exc:
        state["portal"] = {"state": "ERR", "ts": iso_now(), "detail": repr(exc)[:120]}
        return
    if "PORTE|OUVERTE" in out:
        state["portal"] = {"state": "OUVERTE", "ts": iso_now(), "detail": "bannière de maintenance absente"}
        log("CANARI: PORTE OUVERTE — kit de reprise lancé automatiquement.")
        alive_line("PORTE OUVERTE — reprise-portail.sh lancé (reprise du flux source)")
        try:
            subprocess.run(
                ["bash", REPRISE], capture_output=True, text=True, timeout=180, cwd=HOME,
            )
        except Exception as exc:
            log(f"reprise-portail incident : {exc!r}")
    elif "PORTE|FERMÉE" in out:
        state["portal"] = {"state": "FERMÉE", "ts": iso_now(), "detail": "bannière de maintenance présente"}
    elif "PORTE|ERR" in out:
        state["portal"] = {"state": "ERR", "ts": iso_now(), "detail": "accueil injoignable"}
    else:
        state["portal"] = {"state": "INCONNU", "ts": iso_now(), "detail": "réponse non lisible"}


# ── Chasse aux sources ────────────────────────────────────────────────────────

def hunt_line(msg: str) -> None:
    try:
        stamp = time.strftime("%Y-%m-%d %H:%M:%S")
        with open(HUNT_LOG, "a", buffering=1) as fh:
            fh.write(f"[{stamp}] {msg}\n")
    except Exception:
        pass


# ── Miroir archive.org : helpers ─────────────────────────────────────────────

def normalize_ar(s: str) -> str:
    """Normalisation arabe pour l'appariement : espaces retirés, hamzas
    unifiées (أ إ آ → ا), tatweel retiré."""
    s = re.sub(r"[\s\u0640]+", "", s)
    for ch in ("أ", "إ", "آ"):
        s = s.replace(ch, "ا")
    return s


def collection_files() -> list[str] | None:
    """Liste des fichiers de la collection (cache 24 h sur le disque)."""
    try:
        if os.path.exists(COLLECTION_CACHE) and \
                time.time() - os.path.getmtime(COLLECTION_CACHE) < COLLECTION_CACHE_TTL:
            with open(COLLECTION_CACHE, "r", encoding="utf-8") as fh:
                return json.load(fh)
    except Exception:
        pass
    try:
        api = f"https://archive.org/metadata/{COLLECTION_ITEM}"
        with urllib.request.urlopen(api, timeout=40) as resp:
            meta = json.load(resp)
        files = [f.get("name", "") for f in meta.get("files", [])
                 if f.get("name", "").lower().endswith(".pdf")]
        with open(COLLECTION_CACHE, "w", encoding="utf-8") as fh:
            json.dump(files, fh, ensure_ascii=False, indent=1)
        return files
    except Exception as e:
        hunt_line(f"collection : ERR métadonnées {type(e).__name__}")
        return None


def series_key(url: str, book_id: str = "") -> tuple[str, int, str] | None:
    """(matière, année, cycle) dérivés du segment arabe du pdfUrl du portail,
    ex. التفسير-الثانية-ثانوي → ('التفسير', 2, 'ثانوي'). Le segment le plus
    riche (le plus de jetons) l'emporte ; la matière retombe sur le préfixe
    de l'ID de livre si le segment n'en porte pas."""
    parts = url.split("/")
    cycles = [normalize_ar(cy) for cy in ("ثانوي", "إعدادي", "ابتدائي")]
    candidates = [p for p in parts if any(cy in normalize_ar(p) for cy in cycles)]
    if not candidates:
        return None
    seg = max(candidates, key=lambda p: len([t for t in p.split("-") if t.strip()]))
    toks = [normalize_ar(t) for t in seg.split("-") if t.strip()]
    toks = [t for t in toks if t]
    cycle = next((cy for cy in cycles if cy in toks), "")
    year = 0
    for t in toks:
        if t in YEAR_WORDS:
            year = YEAR_WORDS[t]
            break
        m = re.match(r"^(\d)$", t)
        if m:
            year = int(m.group(1))
            break
    # matière = jetons restants (hors année/cycle) reconstitués
    rest = [t for t in toks if t not in YEAR_WORDS and t != cycle
            and not re.match(r"^\d$", t)]
    subject = "".join(rest)
    if not subject and book_id:
        for k, v in BOOK_SUBJECTS.items():
            if book_id.startswith(k):
                subject = v
                break
        if not subject:
            prefix = book_id.split("-")[0]
            subject = BOOK_SUBJECTS.get(prefix, "")
    if not subject or not cycle or not year:
        return None
    return subject, year, cycle


def hunt_archive_collection(target: dict) -> str:
    """Cherche le manuel complet correspondant à la série du pdfUrl dans la
    collection miroir ; le télécharge (version _text prioritaire) en cache
    local s'il n'y est pas déjà. Retour : libellé d'état pour le journal."""
    files = collection_files()
    if files is None:
        return "collection:INJOIGNABLE"
    key = series_key(target.get("pdfUrl") or "", target.get("book") or "")
    if not key:
        return "collection:seg-inconnu"
    subject, year, cycle = key
    want_body = f"{subject}{year}{cycle}"
    match_txt = match_full = None
    for f in files:
        nf = normalize_ar(f)
        if not nf.startswith("كتاب"):
            continue
        body = re.sub(r"(_text)?\.pdf$", "", nf[4:])
        if body == want_body:
            if "_text" in nf:
                match_txt = f
            else:
                match_full = f
    fname = match_txt or match_full
    if not fname:
        # recherche inverse : la matière+année+cycle apparaît dans le nom ?
        for f in files:
            nf = normalize_ar(f)
            if want_body in nf and nf.startswith("كتاب"):
                if "_text" in nf:
                    match_txt = f
                else:
                    match_full = f
        fname = match_txt or match_full
    if not fname:
        return f"collection:ABSENT({subject} {year} {cycle})"
    slug = SUBJECT_SLUGS.get(subject, subject)
    cycle_slug = CYCLE_SLUGS.get(cycle, cycle)
    suffix = "_text" if "_text" in normalize_ar(fname) else ""
    dest = os.path.join(COLLECTION_DIR, f"{slug}-{year}-{cycle_slug}{suffix}.pdf")
    if os.path.exists(dest) and os.path.getsize(dest) > 100_000:
        return f"collection:DÉJÀ-EN-CACHE({os.path.basename(dest)})"
    try:
        os.makedirs(COLLECTION_DIR, exist_ok=True)
        url = (f"https://archive.org/download/{COLLECTION_ITEM}/"
               + urllib.parse.quote(fname))
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=300) as resp, open(dest, "wb") as fh:
            while True:
                chunk = resp.read(1 << 20)
                if not chunk:
                    break
                fh.write(chunk)
        if open(dest, "rb").read(5) != b"%PDF-":
            os.remove(dest)
            return "collection:corps-non-PDF"
        size_mb = os.path.getsize(dest) / 1e6
        hunt_line(f"collection : MANUEL ACQUIS {os.path.basename(dest)} "
                  f"({size_mb:.1f} Mo) pour {target.get('book')}/{target.get('docId')}")
        alive_line(f"MIROIR ARCHIVE.ORG — manuel {os.path.basename(dest)} acquis "
                   f"({size_mb:.0f} Mo) — le portail étant fermé")
        return f"collection:ACQUIS({os.path.basename(dest)})"
    except Exception as e:
        try:
            os.remove(dest)
        except OSError:
            pass
        return f"collection:ERR-{type(e).__name__}"


def quote_url(url: str) -> str:
    """Encode les caractères non-ASCII d'une URL (chemins arabes du portail)."""
    return urllib.parse.quote(url, safe=":/?&=%#[]@$!+,;~-._")


def http_head_status(url: str, timeout: int = 15) -> str:
    try:
        req = urllib.request.Request(quote_url(url), method="HEAD", headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=timeout, context=SSL_CTX) as resp:
            return str(resp.status)
    except urllib.error.HTTPError as e:
        return str(e.code)
    except Exception as e:
        return f"ERR:{type(e).__name__}"


def hunt_sources(state: dict, target: dict | None) -> None:
    """Sonde la prochaine leçon vide : pdfUrl direct + miroir Wayback."""
    if not target:
        state["sourceHunt"] = {"ts": iso_now(), "book": None, "detail": "aucune leçon vide à sonder"}
        return
    book, doc_id, url = target["book"], target["docId"], target["pdfUrl"]
    direct = http_head_status(url)
    wayback = "INCONNU"
    detail = ""
    try:
        api = "https://archive.org/wayback/available?url=" + urllib.parse.quote(url, safe="")
        with urllib.request.urlopen(api, timeout=25) as resp:
            snap = json.load(resp).get("archived_snapshots", {}).get("closest", {})
        if snap.get("available"):
            wayback = f"DISPONIBLE({snap.get('timestamp', '?')})"
        else:
            wayback = "ABSENT"
    except Exception as e:
        wayback = f"ERR:{type(e).__name__}"
    # Arbre portail revivant : source officielle EXACTE → acquisition sûre.
    # Portail fermé → miroir archive.org (manuels complets de la collection).
    collection = "collection:?"
    if direct != "200":
        try:
            collection = hunt_archive_collection(target)
        except Exception as e:
            collection = f"collection:ERR-{type(e).__name__}"
    if direct == "200":
        try:
            os.makedirs(os.path.join(INBOX, book), exist_ok=True)
            dest = os.path.join(INBOX, book, f"{doc_id}.pdf")
            req = urllib.request.Request(quote_url(url), headers={"User-Agent": "Mozilla/5.0"})
            with urllib.request.urlopen(req, timeout=60, context=SSL_CTX) as resp, open(dest, "wb") as fh:
                fh.write(resp.read())
            if open(dest, "rb").read(5) == b"%PDF-":
                detail = f"PDF officiel téléchargé → sources-inbox/{book}/{doc_id}.pdf"
                log(f"CHASSE: ARBRE VIVANT {book}/{doc_id} — PDF officiel acquis.")
                alive_line(f"ARBRE PORTAIL VIVANT — {book}/{doc_id} acquis dans sources-inbox/")
            else:
                os.remove(dest)
                detail = "200 mais corps non-PDF — ignoré"
        except Exception as e:
            detail = f"téléchargement échoué : {type(e).__name__}"
    else:
        detail = f"direct={direct}"
    hunt_line(f"{book}/{doc_id} : direct={direct} | wayback={wayback} | {collection} | {detail}")
    state["sourceHunt"] = {
        "ts": iso_now(), "book": book, "docId": doc_id, "titleFr": target.get("titleFr", ""),
        "direct": direct, "wayback": wayback, "collection": collection, "detail": detail,
    }


# ── Auto-commit / push ────────────────────────────────────────────────────────

def git(args: list[str], timeout: int = 60) -> subprocess.CompletedProcess:
    return subprocess.run(
        ["git", *args], cwd=HOME, capture_output=True, text=True, timeout=timeout,
    )


def clear_stale_index_lock() -> None:
    lock = os.path.join(HOME, ".git", "index.lock")
    try:
        if os.path.exists(lock) and time.time() - os.path.getmtime(lock) > 90:
            os.remove(lock)
    except Exception:
        pass


def auto_commit_push(state: dict) -> None:
    try:
        clear_stale_index_lock()
        # Synchronisation : avance distante → fast-forward local (jamais de force).
        fetch = git(["fetch", "origin"], timeout=90)
        if fetch.returncode == 0:
            counts = git(["rev-list", "--left-right", "--count", "HEAD...origin/main"])
            if counts.returncode == 0 and counts.stdout.split():
                parts = counts.stdout.split()
                left, right = int(parts[0]), int(parts[1])
                if right > 0 and left == 0:
                    git(["reset", "--hard", "origin/main"], timeout=60)
                    log("auto-commit: reset --hard origin/main (avance distante absorbée).")
        clear_stale_index_lock()
        git(["add", *AUTO_ADD_PATHS], timeout=60)
        dirty = git(["diff", "--cached", "--quiet"])
        if dirty.returncode != 0:
            # Garde anti-JSON déchiré : un fichier de livre illisible est retiré.
            staged = git(["diff", "--cached", "--name-only"])
            for path in (staged.stdout or "").splitlines():
                if path.startswith("content/books/") and path.endswith(".json"):
                    try:
                        with open(os.path.join(HOME, path), "r", encoding="utf-8") as fh:
                            json.load(fh)
                    except Exception:
                        log(f"auto-commit: {path} illisible (écriture en cours ?) — retiré de l'index.")
                        git(["reset", "HEAD", "--", path])
            msg = f"auto(pipeline): {time.strftime('%Y-%m-%d %H:%M')} — superviseur v4 (battement, registre, chasse)"
            commit = git(["commit", "-m", msg], timeout=90)
            if commit.returncode == 0:
                state["lastAutoCommit"] = {"ts": iso_now(), "subject": msg}
        push = git(["push", "origin", "main"], timeout=120)
        if push.returncode != 0:
            log(f"auto-commit: push échoué — {(push.stderr or '')[:200]}")
        else:
            counts = git(["rev-list", "--left-right", "--count", "HEAD...origin/main"])
            if counts.returncode == 0 and counts.stdout.strip() == "0\t0":
                state["lastPush"] = {"ts": iso_now(), "ok": True}
    except Exception as exc:
        log(f"auto-commit incident (ignoré, cycle suivant) : {exc!r}")


# ── Divers ────────────────────────────────────────────────────────────────────

def iso_now() -> str:
    return time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())


def write_status(state: dict, workers_books: set[str], scan: dict) -> None:
    payload = {
        "ts": time.time(),
        "iso": iso_now(),
        "version": "v4",
        "startedAt": state.get("startedAt"),
        "cycles": state.get("cycles", 0),
        "wakeCount": state.get("wakeCount", 0),
        "workers": {"active": len(workers_books), "books": sorted(workers_books)},
        "remainingDocs": scan.get("remaining"),
        "registry": load_registry_counts(),
        "portal": state.get("portal"),
        "sourceHunt": state.get("sourceHunt"),
        "lastAutoCommit": state.get("lastAutoCommit"),
        "lastPush": state.get("lastPush"),
    }
    tmp = STATUS_PATH + ".tmp"
    try:
        with open(tmp, "w", encoding="utf-8") as fh:
            json.dump(payload, fh, indent=1, ensure_ascii=False)
        os.replace(tmp, STATUS_PATH)
    except Exception as exc:
        log(f"write_status incident : {exc!r}")


# ── Boucle principale ─────────────────────────────────────────────────────────

def main() -> None:
    os.makedirs(LOGS, exist_ok=True)
    os.makedirs(INBOX, exist_ok=True)
    state = load_state()
    state.setdefault("startedAt", iso_now())
    state.setdefault("cycles", 0)
    state.setdefault("wakeCount", 0)
    last_beat = 0.0
    last_canary = 0.0
    last_hunt = 0.0
    last_commit = 0.0
    last_scan = 0.0
    scan: dict = {"remaining": None, "nextEmpty": None}
    last_cycle = time.time()
    log(f"superviseur v4 démarré (MAX={MAX_CONCURRENT}, file={len(QUEUE)} livres, battement visible)")
    alive_line("SUPERVISEUR v4 DÉMARRÉ — battement toutes les 5 min, canari portail 15 min, chasse sources 30 min, push 10 min")

    while True:
        now = time.time()
        # Détection de réveil : le sandbox a été gelé/coupé entre deux cycles.
        if now - last_cycle > 3 * CYCLE_SECONDS:
            gap_min = int((now - last_cycle) / 60)
            state["wakeCount"] = state.get("wakeCount", 0) + 1
            log(f"RÉVEIL après {gap_min} min de gel — reprise du cycle (gel n°{state['wakeCount']}).")
            alive_line(f"RÉVEIL après {gap_min} min de gel — le moteur autonome reprend")
        last_cycle = now

        try:
            state["cycles"] = state.get("cycles", 0) + 1
            running, active = worker_snapshot()

            # 1. Workers : maintenir MAX_CONCURRENT sur les livres non finis (v3).
            for book in QUEUE:
                if active >= MAX_CONCURRENT:
                    break
                if book in running:
                    continue
                if state.get(book, {}).get("done", False):
                    continue
                if state.get(book, {}).get("passes", 0) >= MAX_PASSES_PER_BOOK:
                    continue
                rem = remaining_docs(book)
                if rem is None:
                    continue
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
                log(f"worker lancé : {book} (passe {state[book]['passes']}, {rem} docs restants, actifs≈{active + 1})")
                running.add(book)
                active += 1
                time.sleep(STAGGER_SECONDS)

            # 2. Recalcul global (coûteux) toutes les 5 min.
            if now - last_scan >= RESCAN_EVERY:
                scan = global_scan()
                last_scan = now

            # 3. Canari portail toutes les 15 min.
            if now - last_canary >= CANARY_EVERY:
                canary_portal(state)
                last_canary = now

            # 4. Chasse aux sources toutes les 30 min.
            if now - last_hunt >= HUNT_EVERY:
                hunt_sources(state, scan.get("nextEmpty"))
                last_hunt = now

            # 5. Auto-commit + push toutes les 10 min.
            if now - last_commit >= AUTOCOMMIT_EVERY:
                auto_commit_push(state)
                last_commit = now

            # 6. Battement visible toutes les 5 min.
            if now - last_beat >= HEARTBEAT_EVERY:
                portal_state = (state.get("portal") or {}).get("state", "?")
                hunt_state = (state.get("sourceHunt") or {}).get("direct", "?")
                rem = scan.get("remaining")
                rem_txt = "?" if rem is None else str(rem)
                alive_line(
                    f"TICK superviseur v4 — workers={active} docs_restants={rem_txt} "
                    f"portail={portal_state} chasse_direct={hunt_state} cycles={state['cycles']}"
                )
                last_beat = now

            # 7. État machine-readable à chaque cycle.
            write_status(state, running, scan)

        except Exception as exc:  # le superviseur ne meurt JAMAIS d'un incident
            log(f"⚠ incident de cycle (ignoré, cycle suivant) : {exc!r}")

        time.sleep(CYCLE_SECONDS)


if __name__ == "__main__":
    main()

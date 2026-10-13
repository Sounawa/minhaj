#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
sanitize-chrome.py — R49 (13 oct. 2026)
Élimine le chrome du site ministériel capturé par le crawler dans les champs
html (arabe) et htmlFr (GT) de content/books/*.json.

Chrome ciblé (dans l'ordre d'apparition après la vraie leçon) :
  1. module « للاطلاع أيضا » / « Pour plus d'informations|d'articles » (h4 + liens)
  2. grilles vides « المرحلة الأولى/الثانية » / « Première étape » (structure vide)
  3. sidebar des 16 matières (تجويد … فكر إسلامي) listant les manuels du programme
  4. <footer> ministériel (liens + coordonnées)

Sûreté :
  - signatures « fortes » = expressions présentes UNIQUEMENT dans le footer
    ministériel (المجلس العلمي الأعلى est écarté : bibliographies légitimes) ;
  - le marqueur « المرحلة الأولى » n'est retenu que si ce qui suit est
    structurellement vide (grille du site), jamais un contenu de leçon ;
  - une coupe n'est validée que si un footer ou une signature forte apparaît
    dans les 12 000 caractères suivants ;
  - passes itératives (max 3) pour les chromes multi-blocs ;
  - idempotent ; dry-run par défaut (--apply pour écrire).
"""
import json
import re
import glob
import sys

APPLY = "--apply" in sys.argv

# ——— Signatures fortes : n'existent QUE dans le footer ministériel ———
AR_STRONG = [
    "الدروس الحسنية", "نشرة المنجزات", "نصوص تشريعية",
    "في البرلمان", "خطب منبرية", "المشور السعيد",
]
FR_STRONG = [
    "Al-Mashwar Al-Saeed", "Bulletin des réalisations", "textes législatifs",
    "au Parlement", "sermons de la chaire",
]

# ——— Marqueurs de coupe ———
RE_RELATED_AR = re.compile(r"<h4>\s*للاطلاع أيضا\s*</h4>")
RE_RELATED_FR = re.compile(r"<h4>\s*Pour plus d'(?:informations|articles)\s*</h4>")
RE_GRID_AR = re.compile(r"<h2>\s*المرحلة الأولى\s*</h2>")
RE_GRID_FR = re.compile(r"<h2>\s*Première étape\s*</h2>")
# Footer sans balise <footer> (captures anciennes) : la 1re liste du footer
# ministériel commence toujours par المجلس العلمي الأعلى / sa traduction GT.
RE_FOOTERLIST_AR = re.compile(r"<ul>\s*<li>\s*المجلس العلمي الأعلى\s*</li>")
RE_FOOTERLIST_FR = re.compile(r"<ul>\s*<li>\s*Conseil scientifique suprême\s*</li>")

SUBJECTS_AR = [
    "التجويد", "علوم القرآن", "القراءات", "الرسم والضبط", "التفسير",
    "الحديث", "علوم الحديث", "السيرة النبوية", "الفقه", "أصول الفقه",
    "التوحيد", "أصول القيم", "الفرائض", "التوقيت", "المنطق", "الفكر الإسلامي",
]
RE_H2_AR = re.compile(r"<h2>\s*(?:&nbsp;)?([^<]{2,30})\s*</h2>")


def text_is_empty(html: str) -> bool:
    """Vrai si le fragment ne contient aucun texte substantiel hors balises."""
    txt = re.sub(r"<[^>]+>", " ", html)
    txt = txt.replace("&nbsp;", " ").strip()
    return len(txt) < 20


STAGE_HEADINGS_AR = ("المرحلة الأولى", "المرحلة الثانية")
STAGE_HEADINGS_FR = ("Première étape", "Deuxième étape")


def _text_no_tags(html: str) -> str:
    txt = re.sub(r"<[^>]+>", " ", html)
    txt = txt.replace("&nbsp;", " ").replace("&#160;", " ")
    return txt


def grid_is_structural(html: str, pos: int) -> bool:
    """« المرحلة الأولى » = grille vide du site : fenêtre 600 car. suivante sans
    texte RÉEL — les titres des grilles jumelles (المرحلة الثانية) sont neutres
    car ils font partie du chrome, pas du contenu."""
    txt = _text_no_tags(html[pos : pos + 600])
    for h in STAGE_HEADINGS_AR + STAGE_HEADINGS_FR:
        txt = txt.replace(h, " ")
    return len(txt.strip()) < 20


def grid_tail_is_empty(html: str, pos: int) -> bool:
    """Variante R51 : grille en FIN de document (footer déjà retiré par un
    passage antérieur) — tout ce qui suit est vide à l'exception des titres
    des grilles elles-mêmes. Chrome avéré sans besoin de signature suivante."""
    txt = _text_no_tags(html[pos:])
    for h in STAGE_HEADINGS_AR + STAGE_HEADINGS_FR:
        txt = txt.replace(h, " ")
    return len(txt.strip()) < 20


def find_sidebar_start_ar(html: str):
    """Premier h2 de la séquence matières (≥6 sujets ordonnés sur ≤9 000 car.)."""
    h2s = [(m.start(), m.group(1).strip()) for m in RE_H2_AR.finditer(html)]
    for i, (pos, subj) in enumerate(h2s):
        if subj not in SUBJECTS_AR:
            continue
        expected = SUBJECTS_AR.index(subj)
        seen = 1
        window_end = pos + 9000
        for p2, s2 in h2s[i + 1:]:
            if p2 > window_end:
                break
            if s2 in SUBJECTS_AR:
                idx2 = SUBJECTS_AR.index(s2)
                if idx2 > expected:
                    seen += 1
                    expected = idx2
        if seen >= 6:
            return pos
    return None


def find_sidebar_start_generic(html: str):
    """Sidebar traduite GT (sujets traduits, donc sans séquence AR connue) :
    premier h2 dont la fenêtre 9 000 car. suivante compte ≥12 mentions
    « للسنة » (AR) ou « année de l'enseignement » (FR) — chaque item de la
    sidebar liste un manuel « pour la Nième année de l'enseignement … ».
    Une leçon réelle ne peut pas contenir 12 telles mentions."""
    for m in RE_H2_AR.finditer(html):
        window = html[m.start() : m.start() + 9000]
        if window.count("للسنة") >= 12 or window.count("année de l'enseignement") >= 12:
            return m.start()
    return None


def clean_tail(html: str) -> str:
    r"""Retire les blocs vides / balises orphelines en fin de document.
    Pattern linéaire (une seule classe d'alternatives non vides — évite le
    backtracking catastrophique des quantificateurs \s imbriqués, cf. doc
    tafsir-tanawi-1/13584 htmlFr 27 Ko)."""
    tail = re.compile(
        r"(?:\s*(?:</div>|<div>\s*</div>|<div>|<p>\s*</p>|</p>|</ul>|</ol>|</li>))+\s*$"
    )
    prev = None
    while prev != html:
        prev = html
        html = tail.sub("", html)
    return html.strip()


def chrome_follows(html: str, cut: int, strong_sigs) -> bool:
    """Chrome avéré après la coupe : balise <footer> ou signature forte
    (expressions exclusives au footer ministériel) dans la fenêtre 16 000 car.
    (la sidebar FR GT de faraid-tanawi-2 est particulièrement longue)."""
    window = html[cut : cut + 16000]
    return "<footer" in window or any(s in window for s in strong_sigs)


def real_text_len(html: str) -> int:
    """Longueur du texte substantiel hors balises."""
    txt = re.sub(r"<[^>]+>", " ", html).replace("&nbsp;", " ")
    return len(txt.strip())


def sanitize_once(html: str, strong_sigs):
    """Une passe : retourne (html, cut, removed) ; cut=None si rien à faire."""
    if not html:
        return html, None, 0
    # R51 : même sans footer/signature restants, une grille vide en queue
    # de document reste du chrome à retirer.
    has_grid_tail = any(
        m and grid_tail_is_empty(html, m.start())
        for m in (rx.search(html) for rx in (RE_GRID_AR, RE_GRID_FR))
    )
    if (
        not has_grid_tail
        and not any(s in html for s in strong_sigs)
        and "<footer" not in html
        and not RE_FOOTERLIST_AR.search(html)
        and not RE_FOOTERLIST_FR.search(html)
    ):
        return html, None, 0

    candidates = []
    tail_only = []
    for regex in (RE_RELATED_AR, RE_RELATED_FR, RE_FOOTERLIST_AR, RE_FOOTERLIST_FR):
        m = regex.search(html)
        if m:
            candidates.append(m.start())
    for regex in (RE_GRID_AR, RE_GRID_FR):
        m = regex.search(html)
        if m:
            if grid_is_structural(html, m.start()):
                candidates.append(m.start())
            if grid_tail_is_empty(html, m.start()):
                # grille orpheline en queue : chrome même sans footer derrière
                tail_only.append(m.start())
    sb = find_sidebar_start_ar(html)
    if sb is not None:
        candidates.append(sb)
    else:
        sb2 = find_sidebar_start_generic(html)
        if sb2 is not None:
            candidates.append(sb2)
    f = html.find("<footer")
    if f != -1:
        candidates.append(f)

    valid = [c for c in candidates if c > 0 and chrome_follows(html, c, strong_sigs)]
    if not valid:
        valid = [c for c in tail_only if c > 0]
    if not valid:
        return html, None, 0

    cut = min(valid)
    kept = html[:cut]
    # Garde anti-troncature : on coupe seulement si le kept garde du texte réel
    # ou un titre (h1/h2) — certains docs officiels légitimes ne sont qu'un titre.
    if real_text_len(kept) < 80 and not re.search(r"<h[12][> ]", kept):
        return html, None, 0
    kept = clean_tail(kept)
    removed = len(html) - len(kept)
    if removed <= 0:
        return html, None, 0
    return kept, cut, removed


def sanitize(html: str, strong_sigs):
    """Passes itératives (max 3) — gère le chrome multi-blocs."""
    total_removed = 0
    for _ in range(3):
        new, cut, removed = sanitize_once(html, strong_sigs)
        if cut is None:
            break
        html = new
        total_removed += removed
    return html, total_removed


def main():
    total_docs = changed_ar = changed_fr = 0
    bytes_ar = bytes_fr = 0
    per_book = {}
    residue = []

    for path in sorted(glob.glob("content/books/*.json")):
        with open(path, encoding="utf-8") as f:
            book = json.load(f)
        bid = book.get("id", path)
        book_changed = 0

        for doc in ([book.get("intro")] if book.get("intro") else []) + (book.get("lessons") or []):
            total_docs += 1
            for field, sigs, is_fr in (
                ("html", AR_STRONG, False),
                ("htmlFr", FR_STRONG, True),
            ):
                html = doc.get(field) or ""
                if not html:
                    continue
                new, removed = sanitize(html, sigs)
                if removed > 0:
                    if any(s in new for s in sigs) or "<footer" in new:
                        residue.append((bid, doc.get("docId"), field))
                        continue
                    doc[field] = new
                    book_changed += 1
                    if is_fr:
                        changed_fr += 1
                        bytes_fr += removed
                    else:
                        changed_ar += 1
                        bytes_ar += removed

        if book_changed:
            per_book[bid] = book_changed
            if APPLY:
                with open(path, "w", encoding="utf-8") as f:
                    json.dump(book, f, ensure_ascii=False, indent=1)
                    f.write("\n")

    mode = "APPLY" if APPLY else "DRY-RUN"
    print(f"[{mode}] docs vus : {total_docs}")
    print(f"  champs html (AR) modifiés : {changed_ar} — {bytes_ar/1000:.0f} Ko retirés")
    print(f"  champs htmlFr (FR) modifiés : {changed_fr} — {bytes_fr/1000:.0f} Ko retirés")
    print(f"  livres touchés : {len(per_book)}")
    if residue:
        print("  ⚠︎ résidus (non modifiés) :")
        for r in residue[:20]:
            print("   ", r)


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Minhāj — QA typographique d'une traduction main (et auto-fix).

Usage: python3 tr-tmp/qa-lesson.py tr-tmp/<docId>.html

Auto-fix (dans les nœuds texte uniquement, jamais dans les balises) :
  - espace fine insécable U+202F avant  ; : ! ? »
  - espace fine insécable U+202F après  «
  - apostrophe droite ' -> U+2019
  - double espace -> espace simple (dans les nœuds texte)

Vérifications dures (échec si non nulles) :
  1. 0 caractère arabe résiduel
  2. guillemets « » appariés (comptes égaux)
  3. balises appariées (h1-h4, p, dl, dt, dd, ul, ol, li, strong, em, i, b, table, thead, tbody, tr, td, th, blockquote, sup, sub, small)
  4. 0 apostrophe droite résiduelle
"""
import re
import sys

NB = "\u202f"   # narrow no-break space
ARABIC = re.compile(r"[\u0600-\u06FF\u0750-\u077F\u08A0-\u08FF\uFB50-\uFDFF\uFE70-\uFEFF]")
VOID = {"br", "hr", "img", "input", "meta", "link"}
PAIRED = {"h1", "h2", "h3", "h4", "h5", "p", "dl", "dt", "dd", "ul", "ol", "li",
          "strong", "em", "i", "b", "table", "thead", "tbody", "tr", "td", "th",
          "blockquote", "sup", "sub", "small", "span", "div"}


def fix_text(t: str) -> str:
    # apostrophe droite -> typographique
    t = t.replace("'", "\u2019")
    # espace (y compris NBSP existant) avant ; : ! ? » -> NNBSP
    t = re.sub(r"[ \u00a0\u202f]*([;:!?»])", NB + r"\1", t)
    # espace après « -> NNBSP
    t = re.sub(r"«[ \u00a0\u202f]*", "«" + NB, t)
    # doubles espaces -> simple
    t = re.sub(r" {2,}", " ", t)
    return t


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: qa-lesson.py <fichier.html>")
        sys.exit(1)
    path = sys.argv[1]
    with open(path, "r", encoding="utf-8") as fh:
        html = fh.read()

    # découpe balises / nœuds texte, auto-fix des nœuds texte
    parts = re.split(r"(<[^>]+>)", html)
    fixed = []
    for p in parts:
        fixed.append(fix_text(p) if not p.startswith("<") else p)
    out = "".join(fixed)
    if out != html:
        with open(path, "w", encoding="utf-8") as fh:
            fh.write(out)
        print("auto-fix typographique appliqué (NNBSP, apostrophes, doubles espaces)")

    errors = []
    # 1. arabe résiduel
    m = ARABIC.findall(out)
    if m:
        ctx = []
        for x in ARABIC.finditer(out):
            s = max(0, x.start() - 40)
            ctx.append(out[s:x.start() + 40].replace("\n", " "))
        errors.append(f"1. ARABE RESIDUEL ({len(m)} car) : " + " | ".join(ctx[:3]))
    # 2. guillemets
    n_o, n_c = out.count("«"), out.count("»")
    if n_o != n_c:
        errors.append(f"2. GUILLEMETS non apparies : {n_o} ouvrants vs {n_c} fermants")
    # 3. balises appariées
    counts = {}
    for m2 in re.finditer(r"<(/?)([a-zA-Z][a-zA-Z0-9]*)", out):
        closing, name = m2.group(1) == "/", m2.group(2).lower()
        if name in VOID or name not in PAIRED:
            continue
        c = counts.setdefault(name, [0, 0])
        c[0 if not closing else 1] += 1
    for name, (o, c) in sorted(counts.items()):
        if o != c:
            errors.append(f"3. BALISE <{name}> non appairee : {o} ouvrantes vs {c} fermantes")
    # 4. apostrophe droite résiduelle (nœuds texte)
    resid = []
    for p in re.split(r"(<[^>]+>)", out):
        if not p.startswith("<") and "'" in p:
            resid.append(p[:60])
    if resid:
        errors.append(f"4. APOSTROPHE DROITE residuelle : " + " | ".join(resid[:3]))

    if errors:
        print("ECHEC QA :")
        for e in errors:
            print("  " + e)
        sys.exit(1)
    print(f"QA OK : {len(out)} car — 0 arabe, guillemets apparies ({n_o}), "
          f"balises appariees ({len(counts)}), 0 apostrophe droite")


if __name__ == "__main__":
    main()

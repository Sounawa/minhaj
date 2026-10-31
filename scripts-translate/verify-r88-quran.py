#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Minhāj R88 — Vérification des leçons 13004/13005.

Contrôles durs (échec si non nuls) :
  1. 0 caractère arabe résiduel
  2. 0 apostrophe droite U+0027
  3. guillemets « » appariés
  4. labels de versets-image : ATTENDU est VIDE pour ces deux leçons
     (aucun verset-image dans le CMS de 13004/13005) — tout label
     trouvé serait superflu et signalé
"""
import re
import sys

ARABIC = re.compile(r"[\u0600-\u06FF\u0750-\u077F\u08A0-\u08FF\uFB50-\uFDFF\uFE70-\uFEFF]")
LABEL = re.compile(r"—\s*([^«»]+?)\s*\((\d+)\)\s*:\s*([\d–\-]+)\s*\]")

ATTENDU = {
    "13004": set(),  # aucun verset-image dans le CMS
    "13005": set(),  # aucun verset-image dans le CMS
}


def main() -> None:
    errors = []
    for slot, attendu in ATTENDU.items():
        path = f"/home/z/my-project/tr-tmp/{slot}.html"
        html = open(path, encoding="utf-8").read()
        # 1. arabe
        n_ar = len(ARABIC.findall(html))
        if n_ar:
            errors.append(f"{slot} : ARABE RESIDUEL ({n_ar} car)")
        # 2. apostrophe droite
        n_q = html.count("'")
        if n_q:
            errors.append(f"{slot} : APOSTROPHE DROITE ({n_q})")
        # 3. guillemets
        if html.count("«") != html.count("»"):
            errors.append(f"{slot} : GUILLEMETS {html.count('«')}/{html.count('»')}")
        # 4. labels de versets-image (aucun attendu)
        got = {m.group(1) + " (" + m.group(2) + ") : " + m.group(3)
               for m in LABEL.finditer(html)}
        sur = got - attendu
        if sur:
            errors.append(f"{slot} : LABELS VERSETS superflus {sorted(sur)}")
        if not errors or all(not e.startswith(slot) for e in errors):
            print(f"  {slot} : OK — 0 verset-image attendu/trouvé, 0 arabe, guillemets appariés")

    if errors:
        print("ECHEC VERIFY :")
        for e in errors:
            print("  " + e)
        sys.exit(1)
    print("VERIFY OK : 13004/13005 — aucun verset-image (conforme au CMS), 0 arabe, 0 apostrophe droite")


if __name__ == "__main__":
    main()

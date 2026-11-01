#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Minhāj R86 — Vérification des versets-image des leçons 12986/12987/12995/12998.

Contrôles durs (échec si non nuls) :
  1. 0 caractère arabe résiduel
  2. 0 apostrophe droite U+0027 dans les nœuds texte
  3. guillemets « » appariés
  4. les labels de versets-image doivent être EXACTEMENT l'ensemble ATTENDU
     de chaque leçon (ni manquant, ni superflu) — l'arabe des versets est
     ancré sur le cache coranique, rendu en français
"""
import re
import sys

ARABIC = re.compile(r"[\u0600-\u06FF\u0750-\u077F\u08A0-\u08FF\uFB50-\uFDFF\uFE70-\uFEFF]")
LABEL = re.compile(r"—\s*([^«»]+?)\s*\((\d+)\)\s*:\s*([\d–\-]+)\s*\]")

ATTENDU = {
    "12986": set(),  # aucune image de verset dans le CMS
    "12987": set(),  # aucune image de verset dans le CMS
    "12995": {"al-Jumuʿa (62) : 9"},  # verset de la course, en image dans le préparation-préalable
    "12998": set(),  # sūras des fêtes citées par leurs textes (images perdues du CMS — tranché par la matière)
}

# passages dont le manuel reproduit une formule en image (citation interne)
IMAGE_IN_QUOTE = {
    "12998": "les deux sūras reproduites en images dans le manuel",
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
        # 4. labels de versets-image
        got = {m.group(1) + " (" + m.group(2) + ") : " + m.group(3)
               for m in LABEL.finditer(html)}
        if got != attendu:
            manq = attendu - got
            sur = got - attendu
            errors.append(f"{slot} : LABELS VERSETS — attendus {sorted(attendu)} / trouvés {sorted(got)}"
                          + (f" — manquants {sorted(manq)}" if manq else "")
                          + (f" — superflus {sorted(sur)}" if sur else ""))
        # 5. formule image dans citation
        if slot in IMAGE_IN_QUOTE and IMAGE_IN_QUOTE[slot] not in html:
            errors.append(f"{slot} : formule image attendue absente ({IMAGE_IN_QUOTE[slot]})")
        if not errors or all(not e.startswith(slot) for e in errors):
            print(f"  {slot} : OK — {len(got)} verset(s)-image conforme(s), 0 arabe, guillemets appariés")

    if errors:
        print("ECHEC VERIFY :")
        for e in errors:
            print("  " + e)
        sys.exit(1)
    print("VERIFY OK : 12986/12987/12995/12998 — versets-image conformes aux labels du manuel")


if __name__ == "__main__":
    main()

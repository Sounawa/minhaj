#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build tr-tmp/19769.html à partir des 5 fragments."""
import re
import sys

parts = []
for i in range(1, 6):
    parts.append(open(f"/home/z/my-project/tr-tmp/fr19769_{i}.html", encoding="utf-8").read())
h = "\n".join(parts)
# conversion des apostrophes droites -> U+2019 (protocole R331 : conversion au build)
h = h.replace("'", "\u2019")

ok = True

def probe(name, cond, detail=""):
    global ok
    status = "OK " if cond else "FAIL"
    print(f"[{status}] {name} {detail}")
    if not cond:
        ok = False

# 1. apostrophes droites
d = h.count("'")
probe("0 apostrophe droite", d == 0, f"({d})")
# 2. guillemets appariés
o, c = h.count("«"), h.count("»")
probe("guillemets appariés", o == c, f"({o}/{c})")
# 3. 0 arabe
ar = len(re.findall(r"[\u0600-\u06FF]", h))
probe("0 caractère arabe", ar == 0, f"({ar})")
# 4. balises appariées
for tag in ["h1", "h2", "h3", "p", "dl", "dt", "dd", "ul", "li", "table", "tbody", "tr", "td", "span", "em", "div"]:
    oo = len(re.findall(rf"<{tag}[ >]", h))
    cc = h.count(f"</{tag}>")
    if oo or cc:
        probe(f"<{tag}> appariées", oo == cc, f"({oo}/{cc})")
# 5. lacunes marquées
lac = h.count("non porté") + h.count("non portée") + h.count("non portés") + h.count("non portées") + h.count("lacune portée") + h.count("lacunes portées")
probe("mentions lacunes (≥ 6)", lac >= 6, f"({lac})")
# 6. h1 unique
h1 = h.count("<h1>")
probe("h1 unique", h1 == 1, f"({h1})")
# 7. entités &nbsp; (matn 5×3 + istitmār 6×3 = 33)
nb = h.count("&nbsp;")
probe("&nbsp; présents (tables)", nb == 33, f"({nb} — attendu 33 : 5 rangées matn + 6 rangées istitmār, × 3 cellules)")
# 8. taille
probe("taille ≥ 12 000 car", len(h) >= 12000, f"({len(h)})")
# 9. pas d'échappements brisés
probe("pas de &# résiduel", "&#x00" not in h)
# 10. N.d.T. présentes
nd = h.count("Notes du traducteur")
probe("bloc Notes du traducteur", nd == 1, f"({nd})")
# 11. badge cible mentionné
probe("badge « Leçon 15 / 30 » annoncé", "Leçon 15 / 30" in h)
# 12. h1 pane attendu
probe("h1 pane « chapitre du ḥāʾ »", "Le rasm et le ḍabṭ : le chapitre du ḫāʾ" in h)
# 13. aucun tamma arabe résiduel (la mention translittérée <em>tamma</em> est légitime)
probe("0 تتمة résiduel", "تتمة" not in h)
# 14. h2 structurels attendus (7)
h2s = h.count("<h2>")
probe("7 h2 structurels", h2s == 7, f"({h2s})")
# 15. tables : 5 rangées matn + 6 istitmār
rows = h.count("<tr>")
probe("11 rangées (5 matn + 6 istitmār)", rows == 11, f"({rows})")

print("---")
if ok:
    open("/home/z/my-project/tr-tmp/19769.html", "w", encoding="utf-8").write(h)
    print(f"ÉCRIT tr-tmp/19769.html ({len(h)} car)")
    sys.exit(0)
else:
    print("SONDES EN ÉCHEC — rien d'écrit")
    sys.exit(1)

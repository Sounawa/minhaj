#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build tr-tmp/19759.html à partir des 5 fragments (chapitre du thāʾ, R338)."""
import re
import sys

parts = []
for i in range(1, 6):
    parts.append(open(f"/home/z/my-project/tr-tmp/fr19759_{i}.html", encoding="utf-8").read())
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
# 3. 0 caractère arabe (convention 0-arabe-résiduel du livre)
ar = len(re.findall(r"[\u0600-\u06FF]", h))
probe("0 caractère arabe", ar == 0, f"({ar})")
# 4. balises appariées
for tag in ["h1", "h2", "h3", "p", "ul", "li", "table", "tbody", "tr", "td", "em"]:
    oo = len(re.findall(rf"<{tag}[ >]", h))
    cc = h.count(f"</{tag}>")
    if oo or cc:
        probe(f"<{tag}> appariées", oo == cc, f"({oo}/{cc})")
# 5. fentes mentionnées
lac = h.count("fente") + h.count("fentes")
probe("mentions de fentes (≥ 4)", lac >= 4, f"({lac})")
# 6. h1 unique
h1 = h.count("<h1>")
probe("h1 unique", h1 == 1, f"({h1})")
# 7. entités &nbsp; (matn 4 rangées ×3 + istiṯmār 4 rangées ×3 = 24)
nb = h.count("&nbsp;")
probe("&nbsp; présents (tables)", nb == 24, f"({nb} — attendu 24 : 4×3 + 4×3)")
# 8. taille
probe("taille ≥ 12 000 car", len(h) >= 12000, f"({len(h)})")
# 9. pas d'échappements brisés
probe("pas de &# résiduel", "&#x00" not in h)
# 10. N.d.T. présentes
nd = h.count("N.d.T.")
probe("N.d.T. (≥ 12)", nd >= 12, f"({nd})")
# 11. badge cible mentionné
probe("badge « Leçon 12 / 30 » annoncé", "Leçon 12 / 30" in h)
# 12. h1 pane attendu
probe("h1 pane « chapitre du thāʾ »", "Le rasm et le ḍabṭ : le chapitre du thāʾ" in h)
# 13. h2 structurels (matn, compréhension, analyse, calibrage, exploitation, préparation)
h2s = h.count("<h2>")
probe("6 h2 structurels", h2s == 6, f"({h2s})")
# 14. tables : matn 4 rangées + istiṯmār 4 rangées
rows = h.count("<tr>")
probe("8 rangées (4 matn + 4 istiṯmār)", rows == 8, f"({rows})")
# 15. scories
for scor in ["hmm", "non :", "TODO", "XXX", "[traduction]", "???", "sagences", "rèle"]:
    probe(f"0 scorie « {scor} »", scor not in h)

print("---")
if ok:
    open("/home/z/my-project/tr-tmp/19759.html", "w", encoding="utf-8").write(h)
    print(f"ÉCRIT tr-tmp/19759.html ({len(h)} car)")
    sys.exit(0)
else:
    print("SONDES EN ÉCHEC — rien d'écrit")
    sys.exit(1)

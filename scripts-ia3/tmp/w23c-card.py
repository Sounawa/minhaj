# -*- coding: utf-8 -*-
"""W23c — round 3 : prev_tail coupe après le ' interne + clés iqṭa/sub/tu/fay."""
P = "scripts-ia3/fix-typo.py"
s = open(P, encoding="utf-8").read()

old = 'prev_tail = prev_w.rstrip("-").rsplit("-", 1)[-1].lower().strip("\'")'
new = 'prev_tail = prev_w.rstrip("-").rsplit("-", 1)[-1].rsplit("\'", 1)[-1].lower().strip("\'")  # W23c: coupe aussi après un \' interne (sab\'imi\'a…)'
assert old in s
s = s.replace(old, new)

B = '''PAIR_MEDIAL.update({
    ("iqṭa", "ā"): "ʿ", ("sub", ""): "ʿ", ("tu", "ṭī"): "ʿ", ("fay", ""): "ʾ",      # iqṭaʿā (ق-ط-ع), subʿi/subʿin (سبع 7), tuʿṭīhi (أعطى ʿayn radical), fayʾun/fayʾ (فيء hamza)
})
'''
anchor = "# W22f — 2 derniers résidus :"
assert anchor in s
s = s.replace(anchor, "# W23c — round 3 :\n" + B + anchor, 1)

compile(s, P, "exec")
open(P, "w", encoding="utf-8").write(s)
print("W23c OK")

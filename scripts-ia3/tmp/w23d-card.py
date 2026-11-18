# -*- coding: utf-8 -*-
"""W23d — round 4 : tails = dernier segment hyphen (al-hana'a, al-muqni'a…)."""
P = "scripts-ia3/fix-typo.py"
s = open(P, encoding="utf-8").read()

B = '''PAIR_MEDIAL.update({
    ("muqni", "a"): "ʿ", ("hana", "a"): "ʿ", ("imi", ""): "ʾ", ("lāmi", ""): "ʿ", ("ma", "būd"): "ʾ",  # al-muqniʿa (tail complet «muqni» — pas «mu»!), al-hanʿa (tail «hana»), sabʿimiʾatin 2e ' (tail «imi» → miʾa hamza), l-lāmiʿah, l-maʾbūd (tail «ma» → maʾbūd hamza)
})
'''
anchor = "# W22f — 2 derniers résidus :"
assert anchor in s
s = s.replace(anchor, "# W23d — round 4 :\n" + B + anchor, 1)

old = '"munaqqa": "ʿ", "marji": "ʿ", "ka": "ʿ",'
new = '"munaqqa": "ʿ", "marji": "ʿ", "ka": "ʿ", "aṣābi": "ʿ", "lāmi": "ʿ",'
assert old in s
s = s.replace(old, new)

compile(s, P, "exec")
open(P, "w", encoding="utf-8").write(s)
print("W23d OK")

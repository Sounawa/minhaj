# -*- coding: utf-8 -*-
"""W23b — round 2 : lstrip('-') dans la comparaison de paires + clés manquantes."""
P = "scripts-ia3/fix-typo.py"
s = open(P, encoding="utf-8").read()

# 1) les paires après apostrophe-hyphen («ṣa'-faḍ») : word_after garde le '-' → lstrip
old = "if prev_tail == p0 and nxt_w[:len(n0)].lower() == n0:"
new = "if prev_tail == p0 and nxt_w.lstrip(\"-\")[:len(n0)].lower() == n0:"
assert old in s
s = s.replace(old, new)

# 2) clés round 2 (W23b)
B = '''PAIR_MEDIAL.update({
    ("a", "ẓam"): "ʿ", ("ba", "qīlī"): "ʿ", ("miqra", ""): "ʾ",                     # al-aʿẓam (tail «a» après rsplit hyphen!), al-Baʿqīlī (ب-ع-ق-ل), (Abū) Miqraʾi (q-r-ʾ consigné)
    ("fu", "lā"): "ʿ", ("tis", "ā"): "ʿ", ("sab", ""): "ʿ", ("imi'a", ""): "ʾ",     # fuʿlā (ف-ع-ل), tisʿā (تسع ʿayn), sabʿun/sabʿimiʾa (سبع ʿayn), …miʾa (مائة hamza)
    ("yu", "lami"): "ʿ",                                                            # wa-in lam yuʿlami (ع-ل-م — consigné, vs yuʾlam)
})
'''
s = s.replace("PAIR_MEDIAL.update({\n    (\"a\", \"ẓam\")", B + "PAIR_MEDIAL.update({\n    (\"a\", \"ẓam\")", 1) if False else s
# insertion simple avant le bloc W22f
anchor = "# W22f — 2 derniers résidus :"
assert anchor in s
s = s.replace(anchor, "# W23b — round 2 :\n" + B + anchor, 1)

old2 = 'WORD_INITIAL_HAMZA.update({"asma", "asta", "akhbur", "akhburtihā", "aṭla", "aṭ", "uṭ", "af", "annī", "aḥadan", "aṣūma", "asta", "annahu", "inna", "innā", "ahli", "aḥkām", "ayyāmin", "anā", "aḥabb", "aḥabbu"})'
new2 = 'WORD_INITIAL_HAMZA.update({"asma", "asta", "akhbur", "akhburtihā", "aṭla", "aṭ", "uṭ", "af", "annī", "aḥadan", "aṣūma", "asta", "annahu", "inna", "innā", "ahli", "aḥkām", "ayyāmin", "anā", "aḥabb", "aḥabbu"})\nWORD_INITIAL_AYN.update({"adad", "adadā", "adadi", "adada", "adadihi"})  # W23 : ʿadad (ع-د-د), ka-ʿadadi/(fayʾun) ʿadadā'
assert old2 in s
s = s.replace(old2, new2)

compile(s, P, "exec")
open(P, "w", encoding="utf-8").write(s)
print("W23b OK")

# -*- coding: utf-8 -*-
"""R482 — extraction de TOUTES les fenêtres d'un marqueur dans le Muḥarrar.
Usage: python3 window-r482.py <marqueur> [occurrence] [largeur]"""
import sys

PATH = "/home/z/my-project/tr-tmp/ibn-atiyya-isra17.md"
txt = open(PATH, encoding="utf-8").read()

m = sys.argv[1]
only = int(sys.argv[2]) if len(sys.argv) > 2 else 0   # 0 = toutes
W = int(sys.argv[3]) if len(sys.argv) > 3 else 500

start = 0
k = 0
while True:
    i = txt.find(m, start)
    if i < 0:
        break
    k += 1
    if only == 0 or only == k:
        a, b = max(0, i - W), min(len(txt), i + W)
        print(f"\n##### {m} occ.{k} @ {i}")
        print(txt[a:b])
    start = i + 1
if k == 0:
    print(f"##### {m} : ABSENT")

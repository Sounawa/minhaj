#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Minhāj R86 — Cross-check des numéros Muwaṭṭaʾ (src arabe vs rendu final)."""
import re

IDS = ["12986", "12987", "12995", "12998"]
TMP = "/home/z/my-project/tr-tmp"

for did in IDS:
    src = open(f"{TMP}/{did}.src.html", encoding="utf-8").read()
    fin = open(f"{TMP}/{did}.html", encoding="utf-8").read()
    src_nums = set(int(x) for x in re.findall(r"الموطأ\s*رقم\s*:?\s*(\d+)", src))
    fin_nums = set(int(x) for x in re.findall(r"\[Muwaṭṭaʾ,\s*n°\s*(\d+)\]", fin))
    ok = src_nums == fin_nums
    print(f"{did} : src {sorted(src_nums)} / final {sorted(fin_nums)} → "
          + ("OK" if ok else f"DIFF (manquants {sorted(src_nums - fin_nums)}, superflus {sorted(fin_nums - src_nums)})"))

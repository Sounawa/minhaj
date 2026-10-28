# -*- coding: utf-8 -*-
"""R340 — assemblage 19774 : concatène les fragments FR en tr-tmp/19774.html."""
import re
parts = []
for i in (1, 2):
    with open(f"/home/z/my-project/tr-tmp/fr19774_{i}.html", encoding="utf-8") as fh:
        parts.append(fh.read().strip())
full = "\n".join(parts) + "\n"
with open("/home/z/my-project/tr-tmp/19774.html", "w", encoding="utf-8") as fh:
    fh.write(full)
n_o, n_c = full.count("«"), full.count("»")
arabic = re.findall(r'[\u0600-\u06FF]', full)
print(f"longueur: {len(full)} | guillemets: {n_o}/{n_c} {'OK' if n_o==n_c else 'ERREUR'} | arabe: {len(arabic)} | h1: {len(re.findall(chr(60)+'h1', full))} | h2: {len(re.findall(chr(60)+'h2', full))} | h3: {len(re.findall(chr(60)+'h3', full))} | li: {len(re.findall(chr(60)+'li'+chr(62), full))} | tr: {len(re.findall(chr(60)+'tr'+chr(62), full))}")
for probe in ["Le rasm et le ḍabṭ : le chapitre du ḏāl", "Leçon 17 / 30", "20:63", "22:19", "4:16", "4:25", "5:5", "51:1", "21:58",
              "2:19", "41:5", "4:119", "7:179", "14:12", "2:245", "2:255", "17:26", "2:117", "2:2", "2:61", "2:176",
              "aš-Šinqīṭī", "ḏī n-nūrayn", "271", "Warš", "rāʾ", "ʾarayta"]:
    print(("OK  " if probe in full else "MANQUE ") + probe)

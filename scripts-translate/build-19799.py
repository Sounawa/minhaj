# -*- coding: utf-8 -*-
"""R344 — assemblage 19799 : concatène les fragments FR en tr-tmp/19799.html."""
import re
parts = []
for i in (1, 2, 3):
    with open(f"/home/z/my-project/tr-tmp/fr19799_{i}.html", encoding="utf-8") as fh:
        parts.append(fh.read().strip())
full = "\n".join(parts) + "\n"
with open("/home/z/my-project/tr-tmp/19799.html", "w", encoding="utf-8") as fh:
    fh.write(full)
n_o, n_c = full.count("«"), full.count("»")
arabic = re.findall(r'[\u0600-\u06FF]', full)
droite = full.count("'")
print(f"longueur: {len(full)} | guillemets: {n_o}/{n_c} {'OK' if n_o==n_c else 'ERREUR'} | arabe: {len(arabic)} | apostrophe droite: {droite} | h1: {len(re.findall(chr(60)+'h1', full))} | h2: {len(re.findall(chr(60)+'h2', full))} | h3: {len(re.findall(chr(60)+'h3', full))} | tables: {len(re.findall(chr(60)+'table', full))}")
for probe in ["Le rasm et le ḍabṭ : le chapitre du zāy", "Leçon 21 / 30", "12:20", "56:64", "37:2", "23:97", "18:17", "18:74", "19:19",
              "59:17", "39:34", "12:74", "12:75", "12:25", "5:29", "5:33", "5:95", "5:85", "2:85", "42:40",
              "22:19", "38:22", "5:23", "3:156", "53:19", "9:109", "22:32", "5:1",
              "zahīdīn", "zāriʿūn", "zāğirāt", "hamazāt", "tazāwaru", "zakiyyatan", "taqwā", "al-ʿUzzā", "ġuzzan",
              "hāḏāni", "ḫaṣmān", "raǧulān", "ǧazāʾuhū", "iḥtirāz", "qayd", "maqṣūr", "ṭarf", "muṯannā",
              "Kašf al-ʿamā", "al-Ǧakanī", "Šinqīṭ", "Bušrā", "sabʿ", "Notes du traducteur", "divergence",
              "ad-dars at-tāsiʿ", "13 mai 2024", "zāy", "rasmānīyūn"]:
    print(("OK  " if probe in full else "MANQUE ") + probe)

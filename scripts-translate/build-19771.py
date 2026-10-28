# -*- coding: utf-8 -*-
"""R339 — assemblage 19771 : concatène les fragments FR en tr-tmp/19771.html."""
import io

parts = []
for i in (1, 2, 3):
    with open(f"/home/z/my-project/tr-tmp/fr19771_{i}.html", encoding="utf-8") as fh:
        parts.append(fh.read().strip())
full = "\n".join(parts) + "\n"
out = "/home/z/my-project/tr-tmp/19771.html"
with open(out, "w", encoding="utf-8") as fh:
    fh.write(full)

# sondes
import re
text = full
n_o, n_c = text.count("«"), text.count("»")
arabic = re.findall(r'[\u0600-\u06FF]', text)
h1 = len(re.findall(r"<h1", text))
h2 = len(re.findall(r"<h2", text))
h3 = len(re.findall(r"<h3", text))
li = len(re.findall(r"<li>", text))
tr = len(re.findall(r"<tr>", text))
print(f"longueur: {len(text)} car")
print(f"h1={h1} h2={h2} h3={h3} li={li} tr={tr}")
print(f"guillemets: {n_o} ouvrants / {n_c} fermants — {'OK' if n_o==n_c else 'ERREUR'}")
print(f"arabe résiduel: {len(arabic)} car")
print(f"apostrophes droites: {text.count(chr(39))}")
# sondes clés
for probe in ["Le rasm et le ḍabṭ : le chapitre du dāl", "Leçon 16 / 30", "40:60", "27:66", "7:38",
              "66:5", "2:184", "3:26", "2:237", "55:6", "20:63", "28:23", "41:34", "22:38",
              "52:8", "75:36", "2:38", "6:52", "18:28", "24:35", "40:41", "53:20", "98:5",
              "ad-Dānī", "ḏāl muʿǧam", "al-ḥanāǧir", "60:4"]:
    print(("OK  " if probe in text else "MANQUE ") + probe)

# -*- coding: utf-8 -*-
"""R343 — assemblage 19798 : concatène les fragments FR en tr-tmp/19798.html."""
import re
parts = []
for i in (1, 2, 3):
    with open(f"/home/z/my-project/tr-tmp/fr19798_{i}.html", encoding="utf-8") as fh:
        parts.append(fh.read().strip())
full = "\n".join(parts) + "\n"
with open("/home/z/my-project/tr-tmp/19798.html", "w", encoding="utf-8") as fh:
    fh.write(full)
n_o, n_c = full.count("«"), full.count("»")
arabic = re.findall(r'[\u0600-\u06FF]', full)
droite = full.count("'")
print(f"longueur: {len(full)} | guillemets: {n_o}/{n_c} {'OK' if n_o==n_c else 'ERREUR'} | arabe: {len(arabic)} | apostrophe droite: {droite} | h1: {len(re.findall(chr(60)+'h1', full))} | h2: {len(re.findall(chr(60)+'h2', full))} | h3: {len(re.findall(chr(60)+'h3', full))} | h4: {len(re.findall(chr(60)+'h4', full))} | tables: {len(re.findall(chr(60)+'table', full))}")
for probe in ["Le rasm et le ḍabṭ : le chapitre du rāʾ (3)", "Leçon 20 / 30", "100:3", "6:94", "34:46", "19:80", "19:95", "21:89",
              "2:46", "2:156", "21:93", "23:60", "13:5", "27:67", "78:40", "23:35", "23:82", "37:16", "37:53", "50:3", "56:47",
              "16:81", "14:50", "8:48", "26:61", "23:44", "2:282", "16:76", "18:32", "24:45", "28:15", "90:8", "5:23", "22:19",
              "28:36", "34:43", "34:18", "59:14", "3:126", "8:10", "25:22", "10:64", "11:74", "39:17", "11:69", "29:31", "57:12",
              "al-Muḥkam", "ad-Dānī", "naqṭ", "tafāʿala", "Šuʿarāʾ", "Anfāl", "turāban", "furādā", "raǧiʿūna", "muġīrāti",
              "sarabīla", "sarābīluhum", "tarāʾa", "tarāʾat", "tatrā", "muftarā", "qurā", "raǧulayn", "ʿaynayn", "raǧulāni", "hāḏāni",
              "atrāban", "bušrā", "ǧazāʾan", "zāy", "Notes du traducteur", "divergence", "13 mai 2024", "ad-dars aṯ-ṯāmin"]:
    print(("OK  " if probe in full else "MANQUE ") + probe)

# -*- coding: utf-8 -*-
"""R341 — assemblage 19776 : concatène les fragments FR en tr-tmp/19776.html."""
import re
parts = []
for i in (1, 2, 3):
    with open(f"/home/z/my-project/tr-tmp/fr19776_{i}.html", encoding="utf-8") as fh:
        parts.append(fh.read().strip())
full = "\n".join(parts) + "\n"
with open("/home/z/my-project/tr-tmp/19776.html", "w", encoding="utf-8") as fh:
    fh.write(full)
n_o, n_c = full.count("«"), full.count("»")
arabic = re.findall(r'[\u0600-\u06FF]', full)
droite = full.count("'")
print(f"longueur: {len(full)} | guillemets: {n_o}/{n_c} {'OK' if n_o==n_c else 'ERREUR'} | arabe: {len(arabic)} | apostrophe droite: {droite} | h1: {len(re.findall(chr(60)+'h1', full))} | h2: {len(re.findall(chr(60)+'h2', full))} | h3: {len(re.findall(chr(60)+'h3', full))} | h4: {len(re.findall(chr(60)+'h4', full))} | tables: {len(re.findall(chr(60)+'table', full))}")
for probe in ["Le rasm et le ḍabṭ : le chapitre du rāʾ", "Leçon 18 / 30", "4:24", "9:38", "3:180", "57:10", "2:104", "4:46", "2:22", "6:142",
              "1:6", "2:142", "16:106", "20:73", "17:62", "6:40", "10:50", "10:59", "35:40", "41:52", "67:28", "25:43", "45:23",
              "7:151", "12:64", "12:92", "21:83", "23:109", "23:118", "23:72", "5:114", "15:20", "22:58", "34:39", "62:11",
              "23:8", "70:32", "51:10", "9:112", "5:55", "2:43", "3:43", "30:46", "24:31", "24:58", "79:5", "2:167", "35:8",
              "6:93", "77:3", "81:10", "2:266", "7:57", "7:130", "16:69", "47:15", "33:35", "55:72", "20:63", "28:48",
              "5:106", "5:107", "1:2", "2:153", "40:60", "5:22", "26:130", "12:29", "51:53", "52:32", "7:175", "15:42",
              "1:7", "2:198", "6:77", "56:92", "2:62", "22:17", "37:146", "Kašf al-ʿamā", "Rašf al-lamā", "Warš", "ibdāl",
              "mīraṯ", "taradaytum", "raʿinā", "firāšan", "ṣirāṭa", "raḥimīn", "rāziqīn", "raʿūna", "ḫarraṣūna", "rākiʿūna",
              "mubašširātin", "ʿawrātin", "mudabbirātin", "ḥasarātin", "ġamarātin", "naširātu", "ṯamarātu", "ṣābirātu", "maqṣūrātun",
              "saḥirāni", "ʾāḫarāni", "ʾarayta", "ʾukrihihinna", "Notes du traducteur", "al-Ǧakanī", "Notes du traducteur"]:
    print(("OK  " if probe in full else "MANQUE ") + probe)

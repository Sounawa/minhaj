# -*- coding: utf-8 -*-
"""R342 — assemblage 19785 : concatène les fragments FR en tr-tmp/19785.html."""
import re
parts = []
for i in (1, 2, 3):
    with open(f"/home/z/my-project/tr-tmp/fr19785_{i}.html", encoding="utf-8") as fh:
        parts.append(fh.read().strip())
full = "\n".join(parts) + "\n"
with open("/home/z/my-project/tr-tmp/19785.html", "w", encoding="utf-8") as fh:
    fh.write(full)
n_o, n_c = full.count("«"), full.count("»")
arabic = re.findall(r'[\u0600-\u06FF]', full)
droite = full.count("'")
print(f"longueur: {len(full)} | guillemets: {n_o}/{n_c} {'OK' if n_o==n_c else 'ERREUR'} | arabe: {len(arabic)} | apostrophe droite: {droite} | h1: {len(re.findall(chr(60)+'h1', full))} | h2: {len(re.findall(chr(60)+'h2', full))} | h3: {len(re.findall(chr(60)+'h3', full))} | h4: {len(re.findall(chr(60)+'h4', full))} | tables: {len(re.findall(chr(60)+'table', full))}")
for probe in ["Le rasm et le ḍabṭ : le chapitre du rāʾ (suite)", "Leçon 19 / 30", "33:35", "78:14", "9:57", "37:2", "37:1", "60:10", "2:148", "3:114", "5:48", "9:88", "21:73", "21:90", "23:56", "23:61", "35:32",
              "24:58", "7:54", "16:12", "16:79", "49:4", "37:48", "38:52", "55:56", "12:43", "12:46", "13:4", "49:7", "3:7", "4:162",
              "3:33", "3:35", "66:12", "2:124", "2:127", "2:126", "2:132", "2:133", "2:258", "2:260", "21:95", "2:144", "2:194", "2:217", "5:96", "24:3",
              "25:61", "33:46", "71:16", "78:13", "4:100", "2:232", "9:96", "10:50", "10:59", "35:40", "41:52", "67:28", "6:40", "17:62", "25:43", "45:23",
              "12:20", "12:23", "12:26", "12:32", "12:51", "54:37", "2:185", "18:60", "25:53", "27:61", "55:19", "35:12", "54:10", "42:41", "26:227", "47:4", "26:93", "42:39", "2:67",
              "2:5", "2:21", "2:31", "3:18", "al-Muḥkam", "ad-Dānī", "Warš", "ibdāl", "naqṭ",
              "ḏākirāti", "muʿṣirāti", "maġārātin", "zāǧirāti", "muhāǧirātin", "ḫayrāti", "marrātin", "musaḫḫarātin", "ḥuǧurāti", "qāṣirātu", "baqarātin", "mutaǧāwirātun",
              "rašidūna", "rāsiḫūna", "tantaṣirāni", "baḥrayni", "ʿImrāna", "ʾIbrāhīma", "wa-ḥarmun", "sirāǧan", "murġaman", "tarāḍaw", "ʾaraytum", "dirāhima",
              "rāwadathu", "rāwadatnī", "yurāwidu", "ʾulāʾika", "al-malāʾikatu", "yā-ayyuhā", "hāʾulāʾi", "Notes du traducteur", "tamma", "vedette d’école", "divergence"]:
    print(("OK  " if probe in full else "MANQUE ") + probe)

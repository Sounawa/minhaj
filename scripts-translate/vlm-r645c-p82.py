# -*- coding: utf-8 -*-
# R645c — 5e lecture bornée : titre de rubrique p.82 (questions finales)
import json, os, subprocess

HOME = "/home/z/my-project"
OUT = f"{HOME}/tr-tmp/r645c"

BASE = ("Tu lis une image d'un manuel scolaire marocain de hadith (commentaire de la "
        "Naḫbat al-fikr d'Ibn Ḥaǧar, 2e année secondaire). Réponds UNIQUEMENT à la "
        "question posée, par transcription EXACTE du texte imprimé visible, token par "
        "token. Si tu n'es pas sûr d'un mot ou d'un chiffre, écris [illisible]. "
        "N'invente AUCUN texte, ne complète JAMAIS de mémoire.")

Q = ("Transcris EXACTEMENT, ligne par ligne, TOUT ce qui est visible sur cette page : "
     "d'abord le TITRE de rubrique en bouton vert ou en évidence s'il y en a un, puis "
     "chaque item numéroté mot à mot, puis tout texte restant, le numéro de page.")

r = subprocess.run(["z-ai", "vision", "-p", f"{BASE}\nQUESTION : {Q}",
                    "-i", f"{HOME}/tr-tmp/qa-crops-r645/r82-full.jpg",
                    "-o", f"{OUT}/vlm-r82-full.json"], capture_output=True, text=True, timeout=300)
if r.returncode == 0:
    d = json.load(open(f"{OUT}/vlm-r82-full.json", encoding="utf-8"))
    c = d["choices"][0]["message"]["content"]
    open(f"{OUT}/read-r82-full.txt", "w", encoding="utf-8").write(f"IMAGE: r82-full.jpg\nCONSIGNE: {Q}\n---\n{c}\n")
    print("OK", len(c))
else:
    print("ERR", (r.stderr or r.stdout)[:200])

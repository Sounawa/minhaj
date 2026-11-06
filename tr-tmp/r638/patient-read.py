#!/usr/bin/env python3
"""R638 — lecteur patient : retry 429 avec backoff long, zones prioritaires."""
import json, subprocess, sys, os, time

P = ("Transcris EXACTEMENT le texte arabe imprimé sur cette image, ligne par ligne, "
     "tel qu'imprimé, sans corriger ni compléter. Marque [ILLISIBLE] si besoin. "
     "C'est un extrait d'un manuel scolaire (Muwaṭṭaʾ + commentaire).")

ZONES = [
    ("G", "tr-tmp/r638/crop-p22-section2-takhmir.png"),
    ("H", "tr-tmp/r638/crop-p22-farafisa-917.png"),
    ("I", "tr-tmp/r638/crop-p22-waqid-919.png"),
    ("K", "tr-tmp/r638/crop-p23-fatima-922.png"),
    ("D", "tr-tmp/r638/crop-p21-talha-mudarra.png"),
    ("E", "tr-tmp/r638/crop-p21-nafad-rijal.png"),
    ("A", "tr-tmp/qa-crops-r633/banniere-p17-r633b.png"),
    ("F", "tr-tmp/r638/crop-p22-kiraha-siyur.png"),
    ("C", "tr-tmp/r638/crop-p20-sarawil-glose.png"),
]

def read(tag, img):
    out = f"tr-tmp/r638/read-{tag}.json"
    for attempt in range(5):
        r = subprocess.run(["z-ai", "vision", "-i", img, "-p", P, "-o", out],
                           capture_output=True, text=True)
        try:
            d = json.load(open(out))
            c = d["choices"][0]["message"]["content"]
            open(out.replace(".json", ".txt"), "w", encoding="utf-8").write(
                f"ZONE {tag} — {img}\n---\n{c}\n")
            print(f"[{tag}] OK:\n{c[:500]}\n", flush=True)
            return True
        except Exception:
            wait = 30 * (attempt + 1)
            print(f"[{tag}] 429 — attente {wait}s (essai {attempt+1}/5)", flush=True)
            time.sleep(wait)
    print(f"[{tag}] ÉCHEC", flush=True)
    return False

for tag, img in ZONES:
    read(tag, img)
    time.sleep(3)

#!/usr/bin/env python3
"""R638 — relecteur détaché : retente les zones G/H/I/K/D/E toutes les 90s pendant 40 min."""
import json, subprocess, os, time
P = ("Transcris EXACTEMENT le texte arabe imprimé sur cette image, ligne par ligne, "
     "tel qu'imprimé, sans corriger ni compléter. Marque [ILLISIBLE] si besoin. "
     "C'est un extrait d'un manuel scolaire (Muwaṭṭaʾ + commentaire).")
Z = {"G":"tr-tmp/r638/crop-p22-section2-takhmir.png","H":"tr-tmp/r638/crop-p22-farafisa-917.png",
     "I":"tr-tmp/r638/crop-p22-waqid-919.png","K":"tr-tmp/r638/crop-p23-fatima-922.png",
     "D":"tr-tmp/r638/crop-p21-talha-mudarra.png","E":"tr-tmp/r638/crop-p21-nafad-rijal.png"}
done = set()
t0 = time.time()
while time.time() - t0 < 2400 and len(done) < len(Z):
    for tag, img in Z.items():
        if tag in done: continue
        out = f"tr-tmp/r638/read-{tag}.json"
        subprocess.run(["z-ai","vision","-i",img,"-p",P,"-o",out],
                       capture_output=True, text=True)
        try:
            c = json.load(open(out))["choices"][0]["message"]["content"]
            open(out.replace(".json",".txt"),"w",encoding="utf-8").write(
                f"ZONE {tag} — {img} — REUSSI {time.strftime('%H:%M:%S')}\n---\n{c}\n")
            done.add(tag)
            print(f"[{tag}] REUSSI", flush=True)
        except Exception:
            pass
    if len(done) < len(Z):
        time.sleep(90)
print("bg-reader termine:", sorted(done), flush=True)

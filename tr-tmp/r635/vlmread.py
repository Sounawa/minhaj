#!/usr/bin/env python3
"""R635 — lecteur VLM : z-ai vision → read-*.txt (extrait content)."""
import json, subprocess, sys

def read(img, prompt, out):
    r = subprocess.run(["z-ai", "vision", "-i", img, "-p", prompt, "-o", out],
                       capture_output=True, text=True)
    try:
        d = json.load(open(out))
        content = d["choices"][0]["message"]["content"]
    except Exception as e:
        content = f"[ERREUR LECTURE: {e}] stdout={r.stdout[-300:]} stderr={r.stderr[-300:]}"
    with open(out.replace(".json", ".txt"), "w", encoding="utf-8") as fh:
        fh.write(f"IMAGE: {img}\nCONSIGNE: {prompt}\n---\n{content}\n")
    print(f"== {img} ==")
    print(content[:1500])
    print()

if __name__ == "__main__":
    img, out = sys.argv[1], sys.argv[2]
    prompt = sys.argv[3] if len(sys.argv) > 3 else (
        "Transcris EXACTEMENT ce que montre cette image, lettre par lettre, ligne par ligne, "
        "sans compléter, sans corriger, sans traduire. Si certains mots sont illisibles, "
        "écris [ILLISIBLE]. C'est une page d'un manuel en arabe.")
    read(img, prompt, out)

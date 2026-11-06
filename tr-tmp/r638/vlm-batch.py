#!/usr/bin/env python3
"""R638 — lecteur VLM par lot (z-ai vision CLI) avec retry/backoff (429)."""
import json, subprocess, sys, os, time

P_NUM = ("Transcris EXACTEMENT le texte arabe imprimé visible sur cette image. "
         "C'est un zoom sur un numéro de hadith imprimé entre crochets [الموطأ رقم : ...]. "
         "Donne : (1) le numéro CHIFFRE PAR CHIFFRE exactement tel qu'imprimé, "
         "(2) la transcription littérale de toute la zone visible autour. "
         "Ne corrige rien, transcris tel qu'imprimé. Si illisible, écris [ILLISIBLE].")
P_TXT = ("Transcris EXACTEMENT ce que montre cette image, lettre par lettre, ligne par ligne, "
         "sans compléter, sans corriger, sans traduire. Si certains mots sont illisibles, "
         "écris [ILLISIBLE]. C'est une page d'un manuel en arabe.")

def read(img, prompt, out):
    for attempt in range(4):
        r = subprocess.run(["z-ai", "vision", "-i", img, "-p", prompt, "-o", out],
                           capture_output=True, text=True)
        content = ""
        ok = False
        try:
            d = json.load(open(out))
            content = d["choices"][0]["message"]["content"]
            ok = True
        except Exception:
            content = ""
        if ok:
            with open(out.replace(".json", ".txt"), "w", encoding="utf-8") as fh:
                fh.write(f"IMAGE: {img}\nCONSIGNE: {prompt[:80]}\n---\n{content}\n")
            print(f"== {os.path.basename(img)} ==")
            print(content[:600]); print()
            return content
        wait = 15 * (attempt + 1)
        print(f"[retry {attempt+1} pour {os.path.basename(img)} — attente {wait}s]", flush=True)
        time.sleep(wait)
    print(f"[ÉCHEC {os.path.basename(img)} après 4 tentatives]")
    return ""

if __name__ == "__main__":
    mode = sys.argv[1]
    prompt = P_NUM if mode == "num" else P_TXT
    for img in sys.argv[2:]:
        base = os.path.splitext(os.path.basename(img))[0]
        read(img, prompt, f"tr-tmp/r638/read-{base}.json")
        time.sleep(4)

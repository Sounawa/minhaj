# -*- coding: utf-8 -*-
# R645c — 4 lectures VLM bornées des crops existants p.80-81 (leçon 15, mursal)
# Budget total : 4 lectures (< 6 autorisées). Sortie : tr-tmp/r645c/
import json, os, subprocess, time

HOME = "/home/z/my-project"
CROPS = f"{HOME}/tr-tmp/qa-crops-r645"
OUT = f"{HOME}/tr-tmp/r645c"
os.makedirs(OUT, exist_ok=True)

BASE = ("Tu lis une image d'un manuel scolaire marocain de hadith (commentaire de la "
        "Naḫbat al-fikr d'Ibn Ḥaǧar, 2e année secondaire). Réponds UNIQUEMENT à la "
        "question posée, par transcription EXACTE du texte imprimé visible, token par "
        "token. Si tu n'es pas sûr d'un mot ou d'un chiffre, écris [illisible]. "
        "N'invente AUCUN texte, ne complète JAMAIS de mémoire (n'utilise PAS de "
        "version canonique d'un texte que tu connaîtrais), ne corrige pas l'imprimé "
        "même s'il te paraît fautif. Transcris aussi les petites gloses marginales "
        "si présentes.")

ASKS = [
    ("r80-top", "Transcris EXACTEMENT, ligne par ligne, TOUT le texte imprimé visible "
     "mot à mot : items tiretés de la liste (صور المرسل), citations en retrait, "
     "renvois entre crochets (chiffres chiffre par chiffre), gloses marginales."),
    ("r80-bot", "Transcris EXACTEMENT, ligne par ligne, TOUT le texte imprimé visible "
     "mot à mot : items tiretés, section (حكم المرسل) si visible, citations en "
     "retrait, renvois entre crochets (chiffres chiffre par chiffre), gloses."),
    ("r81-top", "Transcris EXACTEMENT, ligne par ligne, TOUT le texte imprimé visible "
     "mot à mot : citation d'al-Bāǧī (الباجي), paragraphe de توجيه هذه الأقوال, "
     "passage (ومن قال لا يجوز...) si visible, renvois entre crochets (chiffres "
     "chiffre par chiffre), gloses marginales."),
    ("r81-bot", "Transcris EXACTEMENT, ligne par ligne, TOUT le texte imprimé visible "
     "mot à mot : citation d'أبي العالية, rubriques (أهتدي وأقتدي / التقييم / "
     "الاستئناس / ناقش), les items numérotés, la citation finale d'ابن عبد البر avec "
     "son renvoi entre crochets chiffre par chiffre, gloses marginales."),
]

def vision_call(prompt, img, out, tries=5):
    cmd = ["z-ai", "vision", "-p", prompt, "-i", img, "-o", out]
    for t in range(tries):
        r = subprocess.run(cmd, capture_output=True, text=True, timeout=300)
        if r.returncode == 0:
            return True, ""
        err = (r.stderr or "") + (r.stdout or "")
        if "429" in err or "Too many" in err:
            wait = 45 + 30 * t
            print(f"  429 — attente {wait}s (tentative {t + 1}/{tries})")
            time.sleep(wait)
            continue
        return False, err[:200]
    return False, "429 persistant"

for key, q in ASKS:
    txt_out = f"{OUT}/read-{key}.txt"
    json_out = f"{OUT}/vlm-{key}.json"
    if os.path.exists(txt_out):
        print("•", key, "déjà lu")
        continue
    ok, err = vision_call(f"{BASE}\nQUESTION : {q}", f"{CROPS}/{key}.jpg", json_out)
    if ok:
        try:
            d = json.load(open(json_out, encoding="utf-8"))
            c = d["choices"][0]["message"]["content"]
            open(txt_out, "w", encoding="utf-8").write(f"IMAGE: {key}.jpg\nCONSIGNE: {q}\n---\n{c}\n")
            print("✓", key, len(c), "car")
        except Exception as e:
            print("✗", key, "json:", e)
    else:
        print("✗", key, err)

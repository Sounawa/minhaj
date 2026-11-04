# -*- coding: utf-8 -*-
"""R559 — lectures VLM des 7 composites (cadence espacée anti-429).
Reprise sûre : un composite lu → JSON tr-tmp/vlm-r559-comp/<nom>.json."""
import json
import os
import subprocess
import sys
import time

HOME = "/home/z/my-project"
COMP = f"{HOME}/tr-tmp/qa-comp-r559"
OUT = f"{HOME}/tr-tmp/vlm-r559-comp"
os.makedirs(OUT, exist_ok=True)

BASE = ("Tu lis une image d'un manuel scolaire marocain de hadith (Muwaṭṭaʾ Mālik / "
        "Šarḥ az-Zarqānī, 2e année collégiale — leçon فضل الذكر والدعاء). L'image "
        "contient PLUSIEURS bandes séparées par des interbandes rosées. Réponds zone "
        "par zone, par transcription EXACTE du texte imprimé visible, token par token. "
        "Si tu n'es pas sûr d'un mot ou d'un chiffre, écris [illisible]. N'invente "
        "AUCUN texte, ne complète JAMAIS de mémoire (n'utilise PAS la version "
        "canonique d'un hadith ou d'une āya que tu connaîtrais), ne corrige pas "
        "l'imprimé même s'il te paraît fautif.")

ASKS = {
    "comp-A-p80": (
        "ZONES 1 et 2. — ZONE 1 (haut) : (a) l'isnād : مالك عن [?] عن [?] وعن [?] — "
        "chaque nom exactement lettre à lettre ; (b) le matn entre chevrons MOT À MOT "
        "jusqu'à sa fin exacte ; (c) le renvoi ROUGE [الموطأ رقم ...] CHIFFRE PAR "
        "CHIFFRE (chiffres arabes orientaux, chaque chiffre séparément). — ZONE 2 "
        "(bas) : (a) le titre du bloc ; (b) chaque item de gloss avec l'expression "
        "entre chevrons exactement comme imprimée (عشر رقاب ? حِرز من الشيطان ?) et la "
        "SOURCE imprimée de la quatrième gloss si visible."),
    "comp-B-p81p82": (
        "ZONES 1, 2 et 3. — ZONE 1 (haut) : (a) le titre du bloc mot à mot ; (b) la "
        "phrase d'introduction du premier point mot à mot ; (c) l'item 1- puis le "
        "hadith : isnād exact, matn entre chevrons MOT À MOT (nombres مائة/عشر chiffre "
        "par chiffre), renvoi ROUGE CHIFFRE PAR CHIFFRE. — ZONE 2 (milieu) : le mot "
        "entre قاله? et le renvoi ROUGE [الموطأ رقم ...] CHIFFRE PAR CHIFFRE. — ZONE 3 "
        "(bas) : (a) la phrase incomplète en haut de page et sa suite jusqu'au renvoi "
        "mot à mot ; (b) le renvoi ROUGE CHIFFRE PAR CHIFFRE ; (c) la phrase qui suit "
        "le renvoi."),
    "comp-C-p81p82": (
        "ZONES 1, 2 et 3. — ZONE 1 (haut) : (a) l'item 2- mot à mot ; (b) la citation "
        "coranique du bloc MOT À MOT + renvoi entre crochets : nom de sourate + numéro "
        "CHIFFRE PAR CHIFFRE ; (c) la QUESTION imprimée qui suit (أهل الكتاب... ?) mot "
        "à mot, puis la réponse et la citation coranique واذكر ربك... avec son renvoi "
        "CHIFFRE PAR CHIFFRE. — ZONE 2 (milieu) : (a) l'item 3- mot à mot ; (b) "
        "l'isnād : عن [?] بن [?] عن [?] — chaque nom exactement ; (c) le matn entre "
        "chevrons MOT À MOT + le renvoi ROUGE CHIFFRE PAR CHIFFRE. — ZONE 3 (bas) : "
        "(a) l'item 4- mot à mot ; (b) le matn MOT À MOT (من قال لا إله...) avec ses "
        "nombres chiffre par chiffre ; (c) les lignes imprimées après le chevron "
        "jusqu'à la conclusion et le renvoi ROUGE CHIFFRE PAR CHIFFRE."),
    "comp-D-p83": (
        "ZONES 1, 2 et 3. — ZONE 1 (haut) : (a) le titre ثانيا mot à mot ; (b) l'item "
        "1- mot à mot ; (c) l'isnād : عن [?] عن [?] عن [?] عن [?] — chaque nom "
        "exactement lettre à lettre ; (d) le matn entre chevrons MOT À MOT + renvoi "
        "ROUGE CHIFFRE PAR CHIFFRE. — ZONE 2 (milieu) : (a) l'item 2- mot à mot ; (b) "
        "l'isnād exact ; (c) le matn MOT À MOT + renvoi ROUGE CHIFFRE PAR CHIFFRE. — "
        "ZONE 3 (bas) : (a) le titre du bloc mot à mot ; (b) la phrase d'intro exacte ; "
        "(c) la phrase غير أن بعض الأدعية... + l'exemple أ- : isnād exact (عن [?] عن "
        "مالك عن [?] عن [?]) et le duʿāʾ MOT À MOT + renvoi ROUGE CHIFFRE PAR CHIFFRE."),
    "comp-E-p83p84": (
        "ZONES 1, 2 et 3. — ZONE 1 (haut) : (a) l'exemple ب- : l'isnād exact (عن [?] "
        "بن [?] عن مالك عن [?] عن [?]) et le duʿāʾ MOT À MOT + renvoi ROUGE CHIFFRE "
        "PAR CHIFFRE ; (b) le début de l'exemple ج- si visible : titre + isnād. — "
        "ZONE 2 (milieu) : le duʿāʾ ج- : isnād exact (عن [?] عن [?] عن [?] عن رسول "
        "الله ﷺ) puis le matn MOT À MOT (أعوذ بك من عذاب جهنم...) JUSQU'À SA FIN "
        "EXACTE + renvoi ROUGE CHIFFRE PAR CHIFFRE ; ne complète rien de mémoire. — "
        "ZONE 3 (bas) : le titre du bloc et son texte MOT À MOT."),
    "comp-F-p84": (
        "ZONES 1, 2 et 3. — ZONE 1 (haut) : (a) l'exemple أ- mot à mot ; (b) l'isnād "
        "exact ; (c) le matn MOT À MOT + renvoi ROUGE CHIFFRE PAR CHIFFRE. — ZONE 2 "
        "(milieu) : (a) l'exemple ب- mot à mot ; (b) l'isnād exact ; (c) le matn entre "
        "chevrons MOT À MOT (كنت عند رسول الله ﷺ...) jusqu'à sa fin exacte + renvoi "
        "ROUGE CHIFFRE PAR CHIFFRE. — ZONE 3 (bas) : (a) l'exemple ج- mot à mot : "
        "isnād exact (عن [?] بن [?]...) et le GRAND duʿāʾ MOT À MOT depuis اللهم... "
        "jusqu'à sa fin exacte, sans rien compléter de mémoire ; (b) le renvoi ROUGE "
        "CHIFFRE PAR CHIFFRE ; (c) si le bloc التقويم est visible en bas, son titre et "
        "ses items."),
    "comp-G-p85p86": (
        "ZONES 1, 2, 3 et 4. — ZONE 1 (haut) : (a) le titre du bloc mot à mot ; (b) la "
        "première citation coranique MOT À MOT + renvoi CHIFFRE PAR CHIFFRE ; (c) la "
        "DEUXIÈME citation coranique du bloc orné MOT À MOT (même en calligraphie "
        "ornée) + son renvoi : nom de sourate + numéro CHIFFRE PAR CHIFFRE. — ZONE 2 : "
        "(a) le hadith (ما من داع...) MOT À MOT avec son isnād exact et le renvoi "
        "ROUGE CHIFFRE PAR CHIFFRE ; (b) la phrase qui suit mot à mot. — ZONE 3 : (a) "
        "le bloc التقويم (titre + items) mot à mot ; (b) le bloc أعداد القبلي (titre + "
        "items) ; (c) le bloc أحفظ (titre + texte) ; (d) les items 1- اشرح: ... et 2- "
        "أبين... exactement comme imprimés. — ZONE 4 (bas) : le titre en tête de cette "
        "bande, mot à mot (en-tête d'objectifs d'une nouvelle leçon ?)."),
}

JOBS = [(n, q) for n, q in ASKS.items() if not os.path.exists(f"{OUT}/{n}.json")]


def read_one(job):
    name, q = job
    img = f"{COMP}/{name}.png"
    cmd = ["z-ai", "vision", "-p", f"{BASE}\nQUESTION : {q}", "-i", img, "-o", f"{OUT}/{name}.json"]
    for attempt in range(6):
        try:
            r = subprocess.run(cmd, capture_output=True, text=True, timeout=240)
            if r.returncode == 0:
                print("✓", name, f"(essai {attempt + 1})", flush=True)
                return True
            err = (r.stderr or "").strip()
            tag = "429" if "429" in err else "ERR"
            print(f"✗ {name} essai {attempt + 1} [{tag}]", flush=True)
        except subprocess.TimeoutExpired:
            print("⏱", name, f"timeout essai {attempt + 1}", flush=True)
        time.sleep(70 * (attempt + 1))
    print("✗✗", name, "ABANDON", flush=True)
    return False


t0 = time.time()
done = 0
for job in JOBS:
    if time.time() - t0 > float(sys.argv[1] if len(sys.argv) > 1 else 480):
        print(f"⏱ FIN DE TRANCHE à {int(time.time() - t0)} s", flush=True)
        break
    if read_one(job):
        done += 1
    time.sleep(20)
print(f"LU CETTE TRANCHE : {done} — total {len([f for f in os.listdir(OUT) if f.endswith('.json')])}/7", flush=True)

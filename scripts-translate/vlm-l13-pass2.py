#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""R558 — passe 2 VLM ciblée : en-tête, āya, isnāds, numéros manquants, lexies."""
import json
import time
import os
import subprocess
from PIL import Image

HOME = "/home/z/my-project"
CROPS = f"{HOME}/tr-tmp/qa-crops-r558"
OUT = f"{HOME}/tr-tmp/vlm-l13"
os.makedirs(OUT, exist_ok=True)

# --- scinder les composites trop hauts en deux moitiés ---
for p in (92, 95, 96):
    src = f"{CROPS}/comp-p{p}.png"
    im = Image.open(src)
    h = im.height // 2
    im.crop((0, 0, im.width, h)).save(f"{CROPS}/comp-p{p}a.png")
    im.crop((0, h, im.width, im.height)).save(f"{CROPS}/comp-p{p}b.png")

BASE = ("Tu lis une image d'un manuel scolaire marocain de hadith (Muwaṭṭaʾ Mālik / "
        "Šarḥ az-Zarqānī, 2e année collégiale) à haute résolution. Réponds UNIQUEMENT à "
        "la question posée, par transcription EXACTE du texte imprimé visible, token par "
        "token, chiffre par chiffre. Si tu n'es pas sûr, écris [illisible]. N'invente "
        "AUCUN texte, ne complète JAMAIS de mémoire, ne corrige pas l'imprimé.")

ASKS = [
    ("p91", "comp-p91.png",
     "Transcris : (1) la ligne d'en-tête en haut : الدرس N (le chiffre exact) puis le "
     "titre ENTIER de la leçon mot à mot ; (2) la citation coranique EN ROUGE : "
     "d'abord le texte imprimé mot à mot (même partiel/dégradé), puis la référence "
     "entre crochets [سورة الإسراء الآية : N] — le chiffre N exact, chiffre par "
     "chiffre ; (3) l'isnād du premier hadith (الأحاديث) : chaque nom mot à mot, en "
     "ordre, jusqu'à أمّ عطيّة."),
    ("p92a", "comp-p92a.png",
     "Transcris : (1) la FIN du matn du premier hadith (à partir de فإذا فرغتنّ...) "
     "mot à mot + la petite glose sous le hadith (أشعرنها... تعني...) mot à mot + le "
     "renvoi rouge [الموطأ رقم : N] chiffre par chiffre ; (2) le DEUXIÈME hadith "
     "ENTIER : isnād (chaque nom) + matn (كُفِّن... أو كُفِّنوني...) + renvoi rouge "
     "chiffre par chiffre."),
    ("p92b", "comp-p92b.png",
     "Transcris : (1) les textes marqués عن نافع visibles : chaque texte ENTIER mot à "
     "mot avec son renvoi rouge [الموطأ رقم : N] chiffre par chiffre ; (2) l'encadré "
     "ترجمة الراوية ENTIÈrement : le nom de أمّ عطيّة (نسيبة بنت... ?), le وقيل... "
     "(variante), la phrase من فقهاء الصحابة, la liste des transmetteurs NOMS PAR "
     "NOMS, et l'âge عاشت إلى حدود سنة N."),
    ("p93", "comp-p93.png",
     "Transcris : (1) la glose en haut (سحولية : نسبة إلى...) mot à mot ENTIÈRE — "
     "attention : قرية بال... quoi ? المدينة ou اليمن ? et la parole الأزهري ; (2) dans "
     "le paragraphe حكم غسل الميت : la fin de la phrase وإن ترك... mot à mot (le verbe "
     "exact : أثمّ / أجرم ?) et l'expression suivante."),
    ("p94", "comp-p94.png",
     "Transcris : (1) la citation du propos du Prophète ﷺ à أمّ عطيّة (ابدأنّ...) mot "
     "à mot ENTIERE + son renvoi entre crochets au bas [صحيح البخاري ? / autre ?] "
     "exact ; (2) le hadith avec renvoi rouge [الموطأ رقم : N] : isnād mot à mot + "
     "matn mot à mot ENTIER + N chiffre par chiffre ; (3) la citation أسماء بنت عميس "
     "موت à mot ENTIERE + son renvoi [معرفة السنة والآثار للبيهقي] ; (4) la phrase "
     "d'après (فإن لم يكن أحد الزوجين...)."),
    ("p95a", "comp-p95a.png",
     "Transcris : (1) le hadith cité avec renvoi rouge [الموطأ رقم : 597] : le matn "
     "ENTIER mot à mot (إذا ماتت المرأة...) ; (2) la phrase sur le كفن de la femme : "
     "وأن تكفن المرأة بـ... mot à mot (بخمسة أو سبعة ?) + ce qui suit (زيادة في "
     "الستر...)."),
    ("p95b", "comp-p95b.png",
     "Transcris : (1) le hadith avec renvoi rouge [الموطأ رقم : 602] : l'isnād mot à "
     "mot (chaque nom : ابن شهاب، عن حميد بن...، عن...) + le matn ENTIER mot à mot "
     "(الميّت يُقص... في القوابل ? القبائل ? النُّوب ? الثلاثة... + فإن لم يكن إلا ...) "
     "+ N chiffre par chiffre ; (2) le début du paragraphe الصلاة على الجنازة (فرض "
     "كفاية... وإذا دفن الميت...) puis le hadith du Najāšī avec son isnād mot à mot "
     "et son renvoi rouge [الموطأ رقم : N] chiffre par chiffre."),
    ("p96a", "comp-p96a.png",
     "Transcris : (1) la suite de l'explication du Najāšī : لأنّ الصلاة مخصوصة... "
     "mot à mot ENTIERE (كان مسلمًا في بلد... quoi ? نصراني ? الشام ?) ; (2) la صفة "
     "الصلاة : la position de l'imam (وسط الجثمان ? وسط الجثة ? / منكبيها ?) et la "
     "phrase ويُجعل رأس الميت عن... mot à mot."),
    ("p96b", "comp-p96b.png",
     "Transcris : (1) la citation لقول النبي ﷺ (إذا صليتم...) + son renvoi entre "
     "crochets [سنن أبي داود + N ?] chiffre par chiffre ; (2) la phrase ومن ترك "
     "الدعاء... mot à mot ENTIERE ; (3) le début du duʿāʾ d'Abū Hurayra : l'isnād "
     "(عن سعيد بن أبي سعيد المقبري عن أبيه...) + les premiers mots فقال أبو هريرة : "
     "mot à mot."),
    ("p97", "comp-p97.png",
     "Transcris : (1) le premier hadith de استكمال الدرس : isnaād + matn ENTIER mot à "
     "mot (يُصلّى على الجنازة بعد... إذا صلّيتَ... QUOI exactement après صلّيتَ ? "
     "transcris ces mots lettre par lettre) + renvoi rouge chiffre par chiffre ; (2) "
     "le deuxième hadith : isnād + matn ENTIER mot à mot (صُلِّيَ / صلّيتُ على عمر... "
     "في المسجد ?) + renvoi chiffre par chiffre ; (3) l'item 1 de الإعداد القبلي : la "
     "liste des lexies à expliquer, mot à mot, séparées par des tirets."),
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

for key, img, q in ASKS:
    out = f"{OUT}/pass2-{key}.json"
    if os.path.exists(out):
        print("•", key, "déjà lu")
        continue
    ok, err = vision_call(f"{BASE}\nQUESTION : {q}", f"{CROPS}/{img}", out)
    print(("✓" if ok else "✗"), key, err)

print("\n===== RÉSULTATS =====")
for key, img, q in ASKS:
    try:
        d = json.load(open(f"{OUT}/pass2-{key}.json", encoding="utf-8"))
        print(f"\n----- {key} -----")
        print(d["choices"][0]["message"]["content"][:3800])
    except Exception as e:
        print(f"\n----- {key} ----- ERREUR {e}")

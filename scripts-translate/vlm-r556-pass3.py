#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""R556 — Passe 3 : MICRO-crops lettre par lettre (1200 dpi) des zones encore
dégradées après pass1/pass2. Arbitrages finaux avant rédaction."""
import json
import os
import subprocess
import time

import fitz

HOME = "/home/z/my-project"
PDF = f"{HOME}/content/textbooks-src/hadith-2-iadadi_text.pdf"
CROPS = f"{HOME}/tr-tmp/qa-crops-r556"
OUT = f"{HOME}/tr-tmp/vlm-r556"
doc = fitz.open(PDF)

def frange(name, page_no, f0, f1, dpi=1200):
    pg = doc[page_no - 1]
    H = pg.rect.height
    clip = fitz.Rect(0, H * f0, pg.rect.width, H * f1)
    p = f"{CROPS}/{name}.png"
    pg.get_pixmap(dpi=dpi, clip=clip).save(p)
    print(f"CROP {name} p{page_no} frange[{f0:.2f}-{f1:.2f}]")
    return p

BASE = ("Tu lis une image d'un manuel scolaire marocain de hadith (Muwaṭṭaʾ Mālik / "
        "Šarḥ az-Zarqānī, 2e année collégiale) à TRÈS haute résolution. Réponds "
        "UNIQUEMENT à la question posée, par transcription EXACTE du texte imprimé "
        "visible, token par token, LETTRE PAR LETTRE pour les mots demandés. Si tu "
        "n'es pas sûr d'un mot ou d'un chiffre, écris [illisible]. N'invente AUCUN "
        "texte, ne complète JAMAIS de mémoire, ne corrige pas l'imprimé même s'il "
        "te paraît fautif.")

TARGETS = [
    ("m-p105-objectifs", lambda: frange("m-p105-objectifs", 105, 0.16, 0.40),
     "Transcris EXACTEMENT les trois objectifs numérotés du bloc أهداف الدرس, "
     "ligne par ligne, verbe par verbe (objectif 1 : وشروط وجوبها ou وشرط وجوبها ? "
     "objectif 3 : le verbe exact après رسول الله)."),

    ("m-p106-h2-line1", lambda: frange("m-p106-h2-line1", 106, 0.16, 0.34),
     "Transcris EXACTEMENT les lignes de la citation de Mālik visibles, MOT PAR "
     "MOT, notamment : (1) le mot imprimé IMMÉDIATEMENT après عشرين دينارا — "
     "lettre par lettre (candidats : عينًا / حونًا / عنده / autre) ; (2) درهم ou "
     "درهمًا après مائتي/مائتين ; (3) إن/إنّ من بلغت حصته — la formule exacte du "
     "début de citation."),

    ("m-p106-h2-line3", lambda: frange("m-p106-h2-line3", 106, 0.30, 0.46),
     "Transcris EXACTEMENT les lignes visibles de la citation : notamment وإن "
     "بلغت حصة/حصصهم جميعًا (حصة أو حصص — lettre par lettre) et ما تجب فيه "
     "الزكاة، et وذا/وهذا أحب ما سمعت إلىّ."),

    ("m-p106-sharh-dirham", lambda: frange("m-p106-sharh-dirham", 106, 0.60, 0.74),
     "Transcris EXACTEMENT la ligne : والدرهم … حبة من مطلق الشعير — lettre par "
     "lettre : (1) شرعي ou نسبي ou autre (mot après والدرهم) ; (2) خمسون وخمسا "
     "خمسة/خُمْسُ/خُمُسًا — la formule exacte du nombre de grains (50 et …) ; "
     "(3) وهي … عشر ومائة غرام — formule exacte."),

    ("m-p108-parenthese", lambda: frange("m-p108-parenthese", 108, 0.86, 1.0),
     "Transcris EXACTEMENT la dernière ligne visible : وهو في العين خمس أوق "
     "ويعادل/ويساوي عشرين دينارا من الذهب ( … ) — LA PARENTHÈSE ENTIÈRE MOT PAR "
     "MOT : nombre après (خمسة و… (وثمانون 85 ou وأربعون 45 ou autre — lettre par "
     "lettre), unités, et tout le reste jusqu'à la parenthèse fermante."),

    ("m-p109-parenthese-fin", lambda: frange("m-p109-parenthese-fin", 109, 0.0, 0.07),
     "Transcris EXACTEMENT la première ligne visible (fin d'une parenthèse "
     "commencée page précédente) MOT PAR MOT — tout nombre lettre par lettre."),

    ("m-p109-matn664", lambda: frange("m-p109-matn664", 109, 0.30, 0.44),
     "Transcris EXACTEMENT la citation entre guillemets visible : إنا/إنما لا "
     "تجب فيها الزكاة وأنما/وإنما تجب الزكاة في عشرين دينارا (عينًا présent ou "
     "absent ?) أو مائتي/مائتين درهم — MOT PAR MOT, lettre par lettre pour "
     "إنما/إنها, أنما/وأنما, عينًا."),

    ("m-p109-faida-list", lambda: frange("m-p109-faida-list", 109, 0.90, 1.0),
     "Transcris EXACTEMENT la ligne visible : حول الفائدة: من أفاد فائدة ب… — "
     "LETTRE PAR LETTRE le premier cas après ب (مراباة ou ميراث ?), le deuxième "
     "cas (هبة أو بهاء ?), et tous les cas suivants (قرض ? إجارة ? كراء ?) jusqu'à "
     "la fin de la ligne."),

    ("m-p110-head", lambda: frange("m-p110-head", 110, 0.02, 0.16),
     "Transcris EXACTEMENT toutes les lignes visibles avant/autour de قال القاسم "
     "بن محمد : (1) s'il reste une fin de phrase de la page précédente (حتى يحول "
     "على الحول من يوم …), transcris-la ; (2) le verbe après أعطاهم — lettre par "
     "lettre (يسأل الرجل / فيستفتيهم / فيسأله / autre) ; (3) la phrase هل عندك … "
     "jusqu'à فان قالت/فإن قال."),

    ("m-p110-bracket-abubakr", lambda: frange("m-p110-bracket-abubakr", 110,
                                              0.30, 0.46),
     "Un renvoi rouge [الموطأ رقم : N] ou [الموطأ، رقم: N] figure quelque part "
     "sur cette image (fin de la citation d'Abū Bakr rapportée par al-Qāsim b. "
     "Muḥammad). Lis N CHIFFRE PAR CHIFFRE de droite à gauche (est-ce 658 ? "
     "réponds (a) 658 (b) autre — justifie chiffre par chiffre). Si aucun "
     "renvoi n'est visible, écris [absent]."),

    ("m-p108-verse2", lambda: frange("m-p108-verse2", 108, 0.56, 0.72),
     "Transcris EXACTEMENT le verset coranique imprimé entre parenthèses "
     "coraniques ﴿…﴾ MOT PAR MOT LETTRE PAR LETTRE (les candidats divergent : "
     "﴿خذ من أموالهم صدقة تطهرهم وتزكيهم بها﴾ ou ﴿من أموالهم حق معلوم للسائل "
     "والمحروم﴾ ou autre — transcris ce qui est RÉELLEMENT imprimé), puis le "
     "renvoi rouge MOT PAR MOT (nom de sourate : التوبة أو الحديد أو آل عمران ou "
     "autre — tel qu'imprimé, et le numéro chiffre par chiffre)."),

    ("m-p110-taqwim-q2", lambda: frange("m-p110-taqwim-q2", 110, 0.66, 0.80),
     "Transcris EXACTEMENT les questions numérotées visibles MOT PAR MOT : "
     "notamment la question 2 — son premier mot LETTRE PAR LETTRE (الوسق ou "
     "الوقص ou الوسط ou autre). Transcris aussi la question 3 entière."),
]

crops = []
for name, maker, prompt in TARGETS:
    try:
        p = maker()
        if p:
            crops.append((name, p, prompt))
    except Exception as e:
        print(f"ERR {name}: {e}")
print(f"\n{len(crops)} crops prêts")

def vlm(prompt, image, out, tries=5):
    for attempt in range(tries):
        try:
            r = subprocess.run(["z-ai", "vision", "-p", prompt, "-i", image,
                                "-o", out], capture_output=True, text=True,
                               timeout=240)
            if r.returncode == 0 and os.path.exists(out):
                return True
            err = (r.stderr or r.stdout or "")[-160:]
        except subprocess.TimeoutExpired:
            err = "timeout"
        wait = 40 + attempt * 35
        print(f"  retry {name}: {err} — backoff {wait}s", flush=True)
        time.sleep(wait)
    return False

dump = []
for name, path, prompt in crops:
    out = f"{OUT}/{name}.json"
    if vlm(BASE + " " + prompt, path, out):
        try:
            content = json.load(open(out))["choices"][0]["message"]["content"]
            dump.append(f"===== {name} =====\n{content}\n")
            print(f"OK {name} ({len(content)} car)", flush=True)
        except Exception as e:
            print(f"READ-ERR {name}: {e}")
    else:
        print(f"FAIL {name}")

with open(f"{HOME}/tr-tmp/vlm-r556-all-dump.txt", "a", encoding="utf-8") as fh:
    fh.write("\n" + "\n".join(dump))
print(f"\n+{len(dump)} lectures → tr-tmp/vlm-r556-all-dump.txt")

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""R556 — Passe 2 : cibles restantes via ANCHORS NUMÉRIQUES (couches OCR latines)
+ franges fixes quand aucune ancre. Crops → qa-crops-r556, lectures → vlm-r556."""
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

def anchors(page_no: int, needle: str):
    pg = doc[page_no - 1]
    out = []
    for blk in pg.get_text("dict")["blocks"]:
        for ln in blk.get("lines", []):
            txt = "".join(s["text"] for s in ln["spans"])
            if needle in txt:
                out.append(fitz.Rect(ln["bbox"]))
    return out

def frange(name, page_no, f0, f1, dpi=1000):
    pg = doc[page_no - 1]
    H = pg.rect.height
    clip = fitz.Rect(0, H * f0, pg.rect.width, H * f1)
    p = f"{CROPS}/{name}.png"
    pg.get_pixmap(dpi=dpi, clip=clip).save(p)
    print(f"CROP {name} p{page_no} frange[{f0:.2f}-{f1:.2f}]")
    return p

def around(name, page_no, needle, pad_up, pad_down, dpi=1000, idx=0,
           pad_dn2=None):
    rs = anchors(page_no, needle)
    if not rs:
        print(f"MISS {name} ({needle})")
        return None
    r = rs[idx] if len(rs) > idx else rs[-1]
    H = doc[page_no - 1].rect.height
    y0, y1 = max(0, r.y0 - pad_up), min(H, r.y1 + (pad_dn2 if pad_dn2 is not None else pad_down))
    clip = fitz.Rect(0, y0, doc[page_no - 1].rect.width, y1)
    p = f"{CROPS}/{name}.png"
    doc[page_no - 1].get_pixmap(dpi=dpi, clip=clip).save(p)
    print(f"CROP {name} p{page_no} y[{y0:.0f}-{y1:.0f}] (n={len(rs)})")
    return p

BASE = ("Tu lis une image d'un manuel scolaire marocain de hadith (Muwaṭṭaʾ Mālik / "
        "Šarḥ az-Zarqānī, 2e année collégiale). Réponds UNIQUEMENT à la question posée, "
        "par transcription EXACTE du texte imprimé visible, token par token. Si tu n'es "
        "pas sûr d'un mot ou d'un chiffre, écris [illisible]. N'invente AUCUN texte, ne "
        "complète JAMAIS de mémoire (n'utilise PAS de version canonique du hadith que tu "
        "connaîtrais), ne corrige pas l'imprimé même s'il te paraît fautif.")

TARGETS = [
    ("p105-objectifs", lambda: frange("p105-objectifs", 105, 0.02, 0.30),
     "Transcris EXACTEMENT, ligne par ligne, tout le bloc أهداف الدرس visible "
     "(en-tête + trois objectifs numérotés), verbes lettre par lettre (objectif 1 : "
     "وشروط وجوبها ou وشرط وجوبها ? ; objectif 3 : le verbe exact)."),

    ("p105-matn655", lambda: around("p105-matn655", 105, "655", 175, 16),
     "Transcris EXACTEMENT, ligne par ligne, le bloc visible : l'isnād (مالك بن أنس "
     "عن …) puis le matn ENTRE GUILLEMETS MOT PAR MOT en respectant l'ordre imprimé "
     "(chaque occurrence de خمس / ذود / أوق telle qu'imprimée, même si répétition "
     "apparente), puis le renvoi rouge [الموطأ رقم : N] avec N chiffre par chiffre."),

    ("p106-h2-zone", lambda: around("p106-h2-zone", 106, "668", 330, 16),
     "Transcris EXACTEMENT, ligne par ligne, TOUTE la citation de Mālik visible "
     "(de قال مالك في الذهب… jusqu'au renvoi [الموطأ رقم : 668] inclus). Mot par "
     "mot : le mot imprimé juste après عشرين دينارا (1 mot, lettre par lettre) ; "
     "puis وَمَنْ/ومن … ; أخذ من كل إنسان بقدر حصته… ; وذا أحب ما سمعت إلىّ telle "
     "qu'imprimée."),

    ("p106-sharh-noud", lambda: around("p106-sharh-noud", 106, "2,975", 130, 12),
     "Transcris EXACTEMENT les deux entrées du الشرح visibles : (1) خمس ذود : … "
     "الثلاثة إلى العشرة من الإبل لا واحد له من … (mot après من : لفظه ou لقطه — "
     "lettre par lettre) ; (2) أوقٍ : جمع أوقية وهي أربعون درهما من الفضة الخالصة "
     "… ونها … غراما بناء على أن الدرهم يزن 2,975 غراما — tout mot par mot."),

    ("p106-tarjama", lambda: around("p106-tarjama", 106, "74", 115, 40),
     "Transcris EXACTEMENT la ترجمة الراوي visible : أبو سعيد الخدري … Le verbe "
     "après يوم أحد lettre par lettre (استصغر ou استشهد ?) ; وغزا بعد ذلك اثنتي "
     "عشرة غزوة ; روى عن … ; مات سنة N وقيل N وقيل N هـ — chaque nombre chiffre "
     "par chiffre."),

    ("p108-verse1", lambda: around("p108-verse1", 108, "54", 105, 62),
     "Un verset coranique ﴿…﴾ suivi d'un renvoi rouge [سورة النور، الآية N], puis "
     "le hadith بني الإسلام على خمس… [صحيح البخاري]. (1) Transcris le VERSET MOT "
     "PAR MOT tel qu'imprimé. (2) Le numéro de l'آية CHIFFRE PAR CHIFFRE de droite "
     "à gauche : ٥٤ ou ٥٥ ? Réponds (a) 54 / (b) 55 en justifiant. (3) Transcris le "
     "hadith et son renvoi tel qu'imprimé."),

    ("p108-verse2", lambda: around("p108-verse2", 108, "104", 130, 85),
     "Fin d'un paragraphe se terminant par قوله تعالى ﴿…﴾ suivi d'un renvoi rouge "
     "[سورة …، الآية: N], puis وهي تجب في العين…, puis ثانيا: شروط وجوب الزكاة. "
     "(1) VERSET complet MOT PAR MOT. (2) Renvoi rouge MOT PAR MOT (nom de sourate "
     "EXACT tel qu'imprimé + numéro chiffre par chiffre : est-ce التوبة ou الحديد "
     "ou آل عمران ?). (3) La phrase après le renvoi. (4) L'en-tête + première "
     "ligne de شروط."),

    ("p108-nisab-tail", lambda: frange("p108-nisab-tail", 108, 0.76, 1.0),
     "Transcris EXACTEMENT toutes les lignes visibles, notamment : وهو في العين "
     "خمس أوق ويعادل عشرين دينارا من الذهب ( … ) — la parenthèse entière MOT PAR "
     "MOT avec tous les nombres chiffre par chiffre."),

    ("p109-nisab-head-wide", lambda: around("p109-nisab-head-wide", 109, "4,25",
                                            60, 120),
     "Transcris EXACTEMENT, ligne par ligne : la fin de parenthèse en haut, puis "
     "لأن وزن الدينار 4,25 غراما، فقال مالك «السنة التي لا اختلاف فيها عندنا أن "
     "الزكاة تجب في عشرين دينارا …» — le passage ENTRE les deux guillemets MOT PAR "
     "MOT (kama tajib/عند كمال النصاب…), puis le renvoi [الموطأ رقم : N] chiffre "
     "par chiffre, puis la ligne suivante."),

    ("p109-abd", lambda: around("p109-abd", 109, "664", 170, 16),
     "Transcris EXACTEMENT, ligne par ligne : ولا يعتبر المال بنصاب غيره، قال مالك "
     "في رجل كانت عنده (ستون 60 ou سبعون 70 — lettre par lettre, réponds (a) 60 (b) "
     "70) ومائة درهم ووزنها وصرف الدرهم ببلده (ثمانية 8 ou ثمانين 80 — lettre par "
     "lettre, réponds (a) 8 (b) 80) درهما بدینار، puis la citation entre guillemets "
     "MOT PAR MOT et le renvoi rouge [الموطأ رقم : N] chiffre par chiffre."),

    ("p110-abubakr", lambda: around("p110-abubakr", 110, "658", 320, 16),
     "Transcris EXACTEMENT, ligne par ligne, la citation visible : قال القاسم بن "
     "محمد: كان أبو بكر إذا أعطى الناس أعطاهم (verbe après أعطاهم : يسأل الرجل ou "
     "يستفتيهم — lettre par lettre) … jusqu'au renvoi rouge [الموطأ رقم : N] : N "
     "chiffre par chiffre (658 ? Réponds (a) 658 (b) autre — justifie)."),

    ("p110-taqwim", lambda: around("p110-taqwim", 110, "666", 20, 300, idx=1),
     "Transcris EXACTEMENT, ligne par ligne : la fin du renvoi visible, puis "
     "l'en-tête التقويم et ses TROIS questions MOT PAR MOT (question 2 : premier "
     "mot lettre par lettre : الوسق أو الوقص أو الوسط ou autre), puis l'en-tête "
     "الاستثمار et la première ligne de sa citation."),

    ("p109-hawl-faida", lambda: around("p109-hawl-faida", 109, "660", 40, 400),
     "Transcris EXACTEMENT, ligne par ligne : le renvoi visible, puis l'en-tête ب- "
     "حول الفائدة والربح, puis la définition : حول الفائدة: من أفاد فائدة ب… (liste "
     "complète des cas, MOT PAR MOT) فلا تجب عليها الزكاة … حتى يحول عليها الحول "
     "من يوم … ; transcris aussi toute ligne supplémentaire visible jusqu'en bas."),

    ("p110-head", lambda: frange("p110-head", 110, 0.0, 0.10),
     "Transcris EXACTEMENT les premières lignes de la page (avant قال القاسم بن "
     "محمد) : notamment la fin de la phrase du حول الفائدة commencée à la page "
     "précédente, et le verbe après أعطاهم (يسأل الرجل ou يستفتيهم)."),
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

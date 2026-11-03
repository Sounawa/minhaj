#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""R556 — Passe 1 : micro-crops ciblés hautes résolutions des zones litigieuses
de la leçon 15 (hadith-2es pdf-16, p.105-111), via localisation get_text("dict").
Crops : tr-tmp/qa-crops-r556/ — Lectures : tr-tmp/vlm-r556/ + dump agrégé.
Discipline : transcription EXACTE de l'imprimé, jamais de mémoire, chiffres
chiffre par chiffre (piège OCR inversé «94-25»=49-52), backoff 429 intégré."""
import json
import os
import subprocess
import sys
import time

import fitz

HOME = "/home/z/my-project"
PDF = f"{HOME}/content/textbooks-src/hadith-2-iadadi_text.pdf"
CROPS = f"{HOME}/tr-tmp/qa-crops-r556"
OUT = f"{HOME}/tr-tmp/vlm-r556"
os.makedirs(CROPS, exist_ok=True)
os.makedirs(OUT, exist_ok=True)

doc = fitz.open(PDF)

# --- mécanique de localisation ------------------------------------------------
def lines_with(page_no: int):
    """[(texte_ligne, bbox)] de la page (couche OCR, ordre visuel)."""
    pg = doc[page_no - 1]
    out = []
    for blk in pg.get_text("dict")["blocks"]:
        for ln in blk.get("lines", []):
            txt = "".join(s["text"] for s in ln["spans"]).strip()
            if txt:
                out.append((txt, fitz.Rect(ln["bbox"])))
    return out

def find_lines(page_no: int, keyword: str):
    return [(t, r) for (t, r) in lines_with(page_no) if keyword in t]

def crop_zone(name: str, page_no: int, y0: float, y1: float,
              x0: float = None, x1: float = None, dpi: int = 1000):
    pg = doc[page_no - 1]
    W = pg.rect.width
    x0 = 0 if x0 is None else max(0, x0)
    x1 = W if x1 is None else min(W, x1)
    clip = fitz.Rect(x0, y0, x1, y1)
    pix = pg.get_pixmap(dpi=dpi, clip=clip)
    path = f"{CROPS}/{name}.png"
    pix.save(path)
    print(f"CROP {name} p{page_no} y[{y0:.0f}-{y1:.0f}] dpi{dpi} {pix.width}x{pix.height}")
    return path

def zone_between(name: str, page_no: int, kw_top: str, kw_bottom: str,
                 pad_top: float = 26, pad_bot: float = 14, dpi: int = 1000,
                 idx_top: int = -1, idx_bot: int = -1):
    """Crop entre (inclus) la ligne kw_top et la ligne kw_bottom."""
    tops, bots = find_lines(page_no, kw_top), find_lines(page_no, kw_bottom)
    if not tops or not bots:
        print(f"MISS {name}: kw_top={len(tops)} kw_bot={len(bots)}")
        return None
    r_top = tops[idx_top][1] if len(tops) > abs(idx_top) else tops[-1][1]
    r_bot = bots[idx_bot][1] if len(bots) > abs(idx_bot) else bots[-1][1]
    if r_bot.y0 < r_top.y0:  # inversion → élargir autour des deux
        y0, y1 = min(r_top.y0, r_bot.y0) - pad_top, max(r_top.y1, r_bot.y1) + pad_bot
    else:
        y0, y1 = r_top.y0 - pad_top, r_bot.y1 + pad_bot
    y0, y1 = max(0, y0), min(doc[page_no - 1].rect.height, y1)
    return crop_zone(name, page_no, y0, y1, dpi=dpi)

# --- définition des cibles (zone, prompt) --------------------------------------
BASE = ("Tu lis une image d'un manuel scolaire marocain de hadith (Muwaṭṭaʾ Mālik / "
        "Šarḥ az-Zarqānī, 2e année collégiale). Réponds UNIQUEMENT à la question posée, "
        "par transcription EXACTE du texte imprimé visible, token par token. Si tu n'es "
        "pas sûr d'un mot ou d'un chiffre, écris [illisible]. N'invente AUCUN texte, ne "
        "complète JAMAIS de mémoire (n'utilise PAS de version canonique du hadith que tu "
        "connaîtrais), ne corrige pas l'imprimé même s'il te paraît fautif.")

TARGETS = [
    ("p105-objectifs", lambda: zone_between("p105-objectifs", 105, "أهداف", "الأحاديث",
                                            pad_top=4, pad_bot=26, dpi=1000),
     "Transcris EXACTEMENT, ligne par ligne, tout le bloc أهداف الدرس visible : "
     "l'en-tête puis les trois objectifs numérotés. Transcris chaque verbe lettre "
     "par lettre (notamment le verbe du 3e objectif et le mot après وحكمها dans "
     "l'objectif 1)."),

    ("p105-matn655", lambda: zone_between("p105-matn655", 105, "المواط", "655",
                                          pad_top=8, pad_bot=16, dpi=1000),
     "Transcris EXACTEMENT, ligne par ligne, le bloc entier visible : l'isnād "
     "(مالك بن أنس عن …) puis le matn ENTRE GUILLEMETS en respectant l'ordre "
     "imprimé MOT PAR MOT (transcris chaque occurrence de خمس / ذود / أوق telle "
     "qu'imprimée, même si la phrase semble se répéter), puis le renvoi rouge "
     "[الموطأ رقم : N] avec N chiffre par chiffre."),

    ("p106-h2-zone", lambda: zone_between("p106-h2-zone", 106, "الذهب", "668",
                                          pad_top=6, pad_bot=16, dpi=1000),
     "Transcris EXACTEMENT, ligne par ligne, TOUTE la citation de Mālik visible "
     "(de قال مالك في الذهب… jusqu'au renvoi rouge [الموطأ رقم : 668] inclus). "
     "Mot par mot, notamment : le mot imprimé juste après عشرين دينارا ; la fin "
     "أخذ من كل إنسان بقدر حصته… ; la phrase وذا أحب ما سمعت إليّ telle qu'imprimée."),

    ("p106-sharh-noud", lambda: zone_between("p106-sharh-noud", 106, "الثلاثة", "2,975",
                                             pad_top=8, pad_bot=12, dpi=1000),
     "Transcris EXACTEMENT les deux entrées du الشرح visibles : (1) خمس ذود : … "
     "الثلاثة إلى العشرة من الإبل … (le mot après من : لفظه ou لقطه — lettre par "
     "lettre) ; (2) أوقٍ : جمع أوقية وهي أربعون درهما … ونها تسع عشرة ومائة غرام … "
     "avec le nombre décimal 2,975 tel qu'imprimé."),

    ("p106-tarjama", lambda: zone_between("p106-tarjama", 106, "الخدري", "65",
                                          pad_top=6, pad_bot=12, dpi=1000),
     "Transcris EXACTEMENT la ترجمة الراوي visible : أبو سعيد الخدري … Le verbe "
     "après يوم أحد lettre par lettre (استصغر ou استشهد ou autre) ; la phrase "
     "وغزا بعد ذلك اثنتي عشرة غزوة ; la liste روى عن … ; la fin مات سنة N وقيل N "
     "وقيل N هـ avec CHAQUE nombre chiffre par chiffre."),

    ("p108-verse1", lambda: zone_between("p108-verse1", 108, "النور", "البخاري",
                                         pad_top=30, pad_bot=10, dpi=1100),
     "Sur cette image figure un verset coranique imprimé entre parenthèses "
     "coraniques ﴿…﴾ suivi d'un renvoi rouge [سورة النور، الآية N], puis un hadith "
     "« بني الإسلام على خمس… » avec renvoi [صحيح البخاري]. (1) Transcris le VERSET "
     "complet MOT PAR MOT tel qu'imprimé (graphie imprimée). (2) Lis le renvoi "
     "rouge : le nom de la sourate exactement imprimé, puis le NUMÉRO de l'آية "
     "CHIFFRE PAR CHIFFRE de droite à gauche (est-ce ٥٤ ou ٥٥ ? — réponse (a) 54 "
     "ou (b) 55, justifie chiffre par chiffre). (3) Transcris le hadith et son "
     "renvoi tel qu'imprimé."),

    ("p108-verse2", lambda: zone_between("p108-verse2", 108, "104", "النصاب",
                                         pad_top=30, pad_bot=14, dpi=1100),
     "Cette image contient la fin d'un paragraphe qui se termine par قوله تعالى "
     "﴿…﴾ suivi d'un renvoi rouge [سورة …، الآية: 104] (ou autre numéro), puis la "
     "phrase وهي تجب في العين…, puis l'en-tête ثانيا: شروط وجوب الزكاة. "
     "(1) Transcris le VERSET complet MOT PAR MOT tel qu'imprimé. (2) Transcris "
     "le renvoi rouge MOT PAR MOT (nom de sourate exact tel qu'imprimé + numéro "
     "chiffre par chiffre). (3) Transcris la phrase qui suit le renvoi, puis "
     "l'en-tête et la première ligne de la section شروط."),

    ("p108-nisab-tail", lambda: zone_between("p108-nisab-tail", 108, "النصاب",
                                             None, pad_top=8, pad_bot=10, dpi=1000)
     or None,
     "Transcris EXACTEMENT les dernières lignes visibles : وهو في العين خمس أوقٍ "
     "ويعادل عشرين دينارا من الذهب ( … ) — transcris la parenthèse entière MOT PAR "
     "MOT (tous les nombres chiffre par chiffre)."),

    ("p109-nisab-head", lambda: zone_between("p109-nisab-head", 109, "4,25", "662",
                                             pad_top=26, pad_bot=14, dpi=1000),
     "Transcris EXACTEMENT les lignes visibles : لأن وزن الدينار 4,25 غراما (…) "
     "puis قال مالك «السنة التي لا اختلاف عندنا…» et le renvoi rouge [الموطأ رقم : "
     "N] avec N chiffre par chiffre, puis la ligne suivante (الأئمة الأربعة…)."),

    ("p109-abd", lambda: zone_between("p109-abd", 109, "نصاب غيره", "664",
                                      pad_top=8, pad_bot=16, dpi=1000),
     "Transcris EXACTEMENT, ligne par ligne : ولا يعتبر المال بنصاب غيره، قال مالك "
     "في رجل كانت عنده N ومائة درهم (N = ستون 60 ou سبعون 70 — lettre par lettre, "
     "réponds (a) ستون/mbeauce (b) سبعون) ووزنها وصرف الدرهم ببلده ثمانية/ثمانين "
     "درهما بدینار (8 ou 80 — lettre par lettre, réponds (a) ثمانية (b) ثمانين), "
     "puis la citation «إنما لا تجب فيها الزكاة…» MOT PAR MOT et le renvoi rouge "
     "[الموطأ رقم : N] chiffre par chiffre."),

    ("p110-abubakr", lambda: zone_between("p110-abubakr", 110, "القاسم", "658",
                                          pad_top=10, pad_bot=16, dpi=1000),
     "Transcris EXACTEMENT, ligne par ligne, toute la citation visible : قال "
     "القاسم بن محمد: كان أبو بكر إذا أعطى الناس أعطاهم … (le verbe juste après "
     "أعطاهم : يسأل الرجل ou يستفتيهم — lettre par lettre) … jusqu'au renvoi rouge "
     "[الموطأ رقم : N] : N chiffre par chiffre (est-ce 658 ? réponse (a) 658 (b) "
     "autre — justifie)."),

    ("p110-taqwim", lambda: zone_between("p110-taqwim", 110, "التقويم", None,
                                         pad_top=6, pad_bot=64, dpi=1000) or None,
     "Transcris EXACTEMENT les trois questions du التقويم, MOT PAR MOT : 1- أذكر… "
     "2- (le premier mot de la question 2 lettre par lettre : الوسق أو الوقص أو "
     "الوسط ou autre)… 3- لماذا… Transcris aussi l'en-tête الاستثمار et la "
     "première ligne de sa citation si visible."),

    ("p109-110-hawl-faida", lambda: (
        (lambda p1: p1 or (lambda: None)())(
            zone_between("p109-hawl-faida", 109, "الفائدة", "قبضها", 
                         pad_top=6, pad_bot=30, dpi=1000)) or
        zone_between("p110-hawl-head", 110, "القاسم", "القاسم",
                     pad_top=2, pad_bot=40, dpi=1000)),
     "Transcris EXACTEMENT : (1) la définition ب- حول الفائدة والربح : من أفاد "
     "فائدة بمراباة أو … (liste complète des cas) فلا تجب عليها الزكاة … حتى "
     "يحول عليها الحول من يوم قبضها… ; (2) la première ligne de la page suivante "
     "et le verbe après أعطاهم (يسأل الرجل ou يستفتيهم)."),

    ("p110-666-brackets", lambda: zone_between("p110-666-brackets", 110, "666", "666",
                                               pad_top=10, pad_bot=16, dpi=1000,
                                               idx_top=0, idx_bot=-1),
     "Deux renvois rouges [الموطأ رقم : N] apparaissent sur cette zone (fin de "
     "deux citations de Mālik). Lis CHAQUE numéro CHIFFRE PAR CHIFFRE de droite à "
     "gauche. Réponds : « premier renvoi=… (chiffres : …), deuxième renvoi=… "
     "(chiffres : …) ». S'ils ne sont pas tous les deux visibles, lis celui qui "
     "l'est et dis [hors cadre] pour l'autre."),
]

# --- exécution des crops ---------------------------------------------------------
crops = []
for name, maker, _prompt in TARGETS:
    try:
        p = maker()
        if p:
            crops.append((name, p, _prompt))
        else:
            print(f"SKIP {name}")
    except Exception as e:
        print(f"ERR {name}: {e}")

print(f"\n{len(crops)} crops prêts")

# --- lectures VLM -----------------------------------------------------------------
def vlm(prompt: str, image: str, out: str, tries: int = 5):
    for attempt in range(tries):
        try:
            r = subprocess.run(
                ["z-ai", "vision", "-p", prompt, "-i", image, "-o", out],
                capture_output=True, text=True, timeout=240)
            if r.returncode == 0 and os.path.exists(out):
                return True
            err = (r.stderr or r.stdout or "")[-200:]
        except subprocess.TimeoutExpired:
            err = "timeout"
        wait = 45 + attempt * 30 + (attempt * 7) % 23
        print(f"  429/err {name}: {err} — backoff {wait}s", flush=True)
        time.sleep(wait)
    return False

dump = []
for name, path, prompt in crops:
    out = f"{OUT}/{name}.json"
    ok = vlm(BASE + " " + prompt, path, out)
    if ok:
        try:
            content = json.load(open(out))["choices"][0]["message"]["content"]
            dump.append(f"===== {name} =====\n{content}\n")
            print(f"OK {name} ({len(content)} car)")
        except Exception as e:
            print(f"READ-ERR {name}: {e}")
    else:
        print(f"FAIL {name}")

with open(f"{OUT}/../vlm-r556-all-dump.txt", "w", encoding="utf-8") as fh:
    fh.write("\n".join(dump))
print(f"\nDUMP: {len(dump)} lectures → tr-tmp/vlm-r556-all-dump.txt")

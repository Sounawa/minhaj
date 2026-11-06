#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""R622 — lot 2 : dernières adjudications image (recadrages mono-ligne serrés).
Points restants : noms isnād p.54, mot ض/ص fin hadith, matn Abū Dāwūd (2 lignes),
mot المواقيت/المواقع, fin citation Muslim, crochet Muqaddima, en-tête p.56,
mot mufradāt, question p.52 ligne 2, glose الراجح."""
import json
import os
import subprocess

HOME = "/home/z/my-project"
SRC = f"{HOME}/content/textbooks-src/ulum-hadith-2-thanawi_text.pdf"
OCR = f"{HOME}/tr-tmp/r622-ocr"
OUT = f"{HOME}/tr-tmp/vlm-r622"


def crop(page, y0, y1, x0, x1, tag, dpi):
    out = f"{OCR}/{tag}"
    s = int(dpi / 72)
    subprocess.run(["pdftoppm", "-f", str(page), "-l", str(page), "-r", str(dpi),
                    "-x", str(int(x0 * s)), "-y", str(int(y0 * s)),
                    "-W", str(int((x1 - x0) * s)), "-H", str(int((y1 - y0) * s)),
                    "-singlefile", "-png", SRC, out],
                   check=True, capture_output=True)
    return f"{out}.png"


BASE = ("Tu lis UNE SEULE LIGNE d'un manuel scolaire marocain de hadith. "
        "Transcris EXACTEMENT ce qui est imprimé, mot à mot, sans rien inventer. "
        "Si un mot est flou, écris [illisible]. Ne corrige jamais le texte, ne "
        "complète pas de mémoire. Pour chaque lettre ambigüe (س/ش، ب/ت/ث، د/ذ، "
        "ر/ز، ص/ض، ط/ظ، ف/ق), regarde les POINTS et tranche.")

TASKS = []
TASKS.append(("isnad-names-l2", crop(54, 207, 227, 0, 612, "ADJ56-isnad-line", 1800),
              "Transcris la ligne ENTIÈRE lettre par lettre. Elle contient : "
              "« ... وهو أخو حمزة الزيات ... عن أبي إسحاق عن ... بن ... عن ابن ». "
              "Donne-moi surtout : (1) le mot exact après « الزيات » ; (2) le nom "
              "complet entre « عن أبي إسحاق عن » et « بن » ; (3) le nom après ce "
              "« بن » jusqu'à « عن ابن »."))

TASKS.append(("hadith-word-dad", crop(54, 245, 262, 330, 560, "ADJ57-word-dad", 2400),
              "Il y a ici deux mots courts avant « دخل الجنة » : و...ى ال...يف. "
              "Lettre par lettre : la 3e lettre du 2e mot est-elle ص ou ض "
              "(regarde si elle a UN point au-dessus) ? Transcris les deux mots "
              "exacts."))

TASKS.append(("abudawud-l1", crop(54, 416, 434, 200, 612, "ADJ58-abudawud-l1", 1800),
              "Transcris la ligne ENTIÈRE. Elle commence par « عباس رضي الله عنهما "
              "عن النبي ﷺ قال: » et continue par « من أقام الصلاة... ». "
              "Transcris la suite exacte mot à mot."))

TASKS.append(("abudawud-l2", crop(54, 436, 452, 200, 612, "ADJ59-abudawud-l2", 1800),
              "Transcris la ligne ENTIÈRE mot à mot. Elle commence par « أي » ou "
              "« ايه » — je veux surtout : ce qui suit « أي », et le mot avant "
              "« فأتي »."))

TASKS.append(("abudawud-l3", crop(54, 452, 472, 150, 612, "ADJ60-abudawud-l3", 1800),
              "Transcris la ligne ENTIÈRE mot à mot, de « فأتي » ou « فيه » "
              "jusqu'à la fin visible (le crochet [ سنن أبي داود ... ] et ce qui "
              "précède)."))

TASKS.append(("khalili-word", crop(54, 536, 556, 180, 500, "ADJ61-khalili-word", 1800),
              "Dans « أنكر الحفاظ حديثه في ... في رمضان », transcris le mot "
              "entre les deux « في » lettre par lettre. Est-ce المواقيت (avec "
              "ق) ou المواقع (avec ع) ? Regarde bien la 4e lettre."))

TASKS.append(("muslim-end-l2", crop(55, 634, 662, 120, 612, "ADJ62-muslim-end", 1800),
              "Transcris la ligne ENTIÈRE mot à mot. Elle commence par « فإن كان "
              "الأغلب من حديثه كذلك... ». Je veux la fin EXACTE après « كذلك »."))

TASKS.append(("muqaddima-bracket", crop(55, 216, 234, 260, 612, "ADJ63-muq-bracket", 1800),
              "Transcris le crochet [ ... ] visible, avec son numéro de page. "
              "Transcris les chiffres UN PAR UN de gauche à droite tel "
              "qu'imprimés (ex : « 8 puis 3 » ou « 3 puis 8 puis 3 »...)."))

TASKS.append(("ist-header-p56", crop(56, 20, 130, 0, 612, "ADJ64-ist-header", 900),
              "En haut de page il y a une ligne d'en-tête précédant « 1. أستخرج "
              "... ». Transcris-la mot à mot. Hésitation à trancher : "
              "« وأستخرج منه: » ou « وأجيب عنه: » ?"))

TASKS.append(("mufradat-word2", crop(53, 195, 213, 240, 520, "ADJ65-mufradat-w2", 2400),
              "Transcris lettre par lettre : (1) le mot après « بتفكر وتدبر » "
              "(est-ce لأثره avec ث ou لأقره avec ق ?) ; (2) le mot entre « وهو » "
              "et « من العلم » ; (3) le mot avant « ويضاده »."))

TASKS.append(("question-l2", crop(52, 426, 446, 120, 612, "ADJ66-question-l2", 1500),
              "Transcris la ligne ENTIÈRE mot à mot. Elle est la fin d'une "
              "question : « ... رواية الضعيف التي ... » — je veux ce qui suit "
              "« التي » jusqu'à « وما فائدة التمييز بينهما؟ »."))

TASKS.append(("gloss-rajah-l", crop(52, 585, 700, 0, 190, "ADJ67-gloss-rajah-l", 1800),
              "Il y a une glose de marge « الراجح: ... ». Transcris-la mot à mot, "
              "y compris ce qui est écrit petit."))

TASKS.append(("gloss-rajah-r", crop(52, 585, 700, 400, 612, "ADJ68-gloss-rajah-r", 1800),
              "Il y a une glose de marge « الراجح: ... » ou « ورجح الشيء بيده: "
              "... ». Transcris tout ce qui est écrit, mot à mot."))

subprocess.run(["mkdir", "-p", OUT], check=True)
import time
for i, (key, img, q) in enumerate(TASKS):
    out = f"{OUT}/{key}.json"
    if os.path.exists(out):
        print("SKIP " + key)
        continue
    cmd = ["z-ai", "vision", "-p", f"{BASE}\nQUESTION : {q}", "-i", img, "-o", out]
    ok = False
    for attempt in range(6):
        r = subprocess.run(cmd, capture_output=True, text=True, timeout=300)
        if r.returncode == 0:
            ok = True
            break
        wait = 45 * (attempt + 1)
        print(f"RETRY {key} dans {wait}s (429?)")
        time.sleep(wait)
    print(("OK  " if ok else "FAIL") + " " + key)
    time.sleep(6)

print("\n===== ADJUDICATIONS R622 — LOT 2 =====")
for key, _, _ in TASKS:
    try:
        d = json.load(open(f"{OUT}/{key}.json", encoding="utf-8"))
        print(f"\n----- {key} -----")
        print(d["choices"][0]["message"]["content"][:1200])
    except Exception as e:
        print(f"\n----- {key} ----- ERREUR {e}")

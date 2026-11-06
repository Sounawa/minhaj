#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""R622 — lot 3 : adjudications finales (recette ADJ27 validée : 1200 dpi,
bandes généreuses 30-55 pt). Points restants : segment isnād, mot ض/ص fin
hadith, matn Abū Dāwūd (2 bandes), mot المواقيت/المواقع, fin citation Muslim,
crochet Muqaddima, mot mufradāt, question p.52 l.2, gloses p.52, en-tête p.56."""
import json
import os
import subprocess
import time

HOME = "/home/z/my-project"
SRC = f"{HOME}/content/textbooks-src/ulum-hadith-2-thanawi_text.pdf"
OCR = f"{HOME}/tr-tmp/r622-ocr"
OUT = f"{HOME}/tr-tmp/vlm-r622"


def crop(page, y0, y1, x0, x1, tag, dpi=1200):
    out = f"{OCR}/{tag}"
    s = int(dpi / 72)
    subprocess.run(["pdftoppm", "-f", str(page), "-l", str(page), "-r", str(dpi),
                    "-x", str(int(x0 * s)), "-y", str(int(y0 * s)),
                    "-W", str(int((x1 - x0) * s)), "-H", str(int((y1 - y0) * s)),
                    "-singlefile", "-png", SRC, out],
                   check=True, capture_output=True)
    return f"{out}.png"


def tess(img, psm=6):
    r = subprocess.run(["tesseract", img, "stdout", "-l", "ara",
                        "--tessdata-dir", f"{HOME}/scripts-translate/tessdata",
                        "--psm", str(psm)], capture_output=True, text=True)
    return r.stdout.strip()[:600]


BASE = ("Tu lis une bande d'un manuel scolaire marocain de hadith (naskh imprimé "
        "net). Transcris EXACTEMENT ce qui est imprimé, mot à mot, sans rien "
        "inventer. Pour chaque lettre ambigüe (س/ش، ب/ت/ث، د/ذ، ر/ز، ص/ض، "
        "ط/ظ، ف/ق، ع/غ), REGARDE LES POINTS et tranche. Si un mot est flou, "
        "écris [illisible]. Ne corrige jamais, ne complète pas de mémoire.")

TASKS = [
    ("isnad-seg", crop(54, 198, 236, 0, 612, "ADJ70-isnad-seg"),
     "Transcris la ligne du milieu ENTÈREMENT, mot à mot. Elle contient une "
     "chaîne : « ... وهو أخو حمزة الزيات المقرئ عن أبي إسحاق عن ... بن ... عن "
     "ابن ». Je veux surtout les DEUX noms entre « عن أبي إسحاق عن » et "
     "« عن ابن », lettre par lettre."),
    ("hadith-dad2", crop(54, 240, 275, 180, 612, "ADJ71-hadith-dad2"),
     "Transcris mot à mot ce qui est visible entre « وصام » et « دخل الجنة », "
     "puis « دخل الجنة » et le crochet [ ... ] avec ses chiffres chiffre par "
     "chiffre. La 3e lettre du mot avant « دخل » : ص ou ض (un point ?) ?"),
    ("abudawud-b1", crop(54, 414, 438, 150, 612, "ADJ72-abudawud-b1"),
     "Transcris la bande mot à mot : elle contient « عن أبي هريرة قال: جاء رجل "
     "إلى النبي ﷺ ... ». Je veux ce qui suit « ﷺ » jusqu'à la fin de bande, "
     "lettre par lettre."),
    ("abudawud-b2", crop(54, 438, 476, 150, 612, "ADJ73-abudawud-b2"),
     "Transcris la bande mot à mot, de « فأتي » jusqu'au crochet "
     "[ سنن أبي داود ... ] inclus."),
    ("khalili-w2", crop(54, 532, 560, 120, 612, "ADJ74-khalili-w2"),
     "Transcris la ligne contenant « أنكر الحفاظ حديثه في ... في رمضان ». "
     "Le mot entre les deux « في » : المواقيت (ق) ou المواقع (ع) ? Regarde "
     "la 4e lettre et ses points. Transcris la ligne entière."),
    ("muslim-end2", crop(55, 628, 668, 80, 612, "ADJ75-muslim-end2"),
     "Transcris la dernière ligne de la citation de l'imām Muslim : elle "
     "commence par « فإن كان الأغلب من حديثه كذلك ... ». Je veux la suite "
     "EXACTE après « كذلك », mot à mot, jusqu'au guillemet fermant."),
    ("muq-bracket2", crop(55, 212, 238, 200, 612, "ADJ76-muq-bracket2"),
     "Transcris le crochet de citation [ مقدمة ابن الصلاح ... ] avec ses "
     "chiffres, en les énumérant UN PAR UN de gauche à droite."),
    ("mufradat-w3", crop(53, 192, 216, 200, 560, "ADJ77-mufradat-w3"),
     "Transcris la bande mot à mot : « ... إدراك الشيء بتفكر وتدبر ... وهو ... "
     "من العلم ويضاده الإنكار ». Je veux : (1) le mot après « وتدبر » (لأثره "
     "avec ث ou لأقره avec ق ?) ; (2) le mot entre « وهو » et « من العلم »."),
    ("question-l3", crop(52, 420, 448, 60, 612, "ADJ78-question-l3"),
     "Transcris la bande ENTÈREMENT mot à mot : c'est une question sur deux "
     "lignes « فماذا تسمى ... ؟ وماذا تسمى ... ؟ وما فائدة التمييز بينهما؟ »."),
    ("gloss-l2", crop(52, 620, 695, 0, 230, "ADJ79-gloss-l2", 1500),
     "Dans cette bande de marge il y a une glose « الراجح: ... » et peut-être "
     "« ورجح الشيء بيده: ... ». Transcris TOUT ce qui est écrit, mot à mot."),
    ("gloss-r2", crop(52, 620, 695, 380, 612, "ADJ80-gloss-r2", 1500),
     "Dans cette bande de marge il y a une glose « الراجح: ... » ou la fin "
     "« ... ونظر ما ثقله ». Transcris TOUT ce qui est écrit, mot à mot."),
]

# localisation p56 : rendu 300 dpi pleine page
crop(56, 0, 792, 0, 612, "ADJ81-p56-full", 300)
print("=== p56 OCR 300dpi (localisation) ===")
print(tess(f"{OCR}/ADJ81-p56-full.png")[:800])

print("\n===== appels VLM =====")
os.makedirs(OUT, exist_ok=True)
for key, img, q in TASKS:
    out = f"{OUT}/{key}.json"
    if os.path.exists(out):
        print("SKIP " + key)
        continue
    cmd = ["z-ai", "vision", "-p", f"{BASE}\nQUESTION : {q}", "-i", img, "-o", out]
    ok = False
    for attempt in range(4):
        r = subprocess.run(cmd, capture_output=True, text=True, timeout=300)
        if r.returncode == 0:
            ok = True
            break
        print(f"RETRY {key} dans 60s")
        time.sleep(60)
    print(("OK  " if ok else "FAIL") + " " + key)
    time.sleep(8)

print("\n===== ADJUDICATIONS R622 — LOT 3 =====")
for key, _, _ in TASKS:
    try:
        d = json.load(open(f"{OUT}/{key}.json", encoding="utf-8"))
        print(f"\n----- {key} -----")
        print(d["choices"][0]["message"]["content"][:1300])
    except Exception as e:
        print(f"\n----- {key} ----- ERREUR {e}")

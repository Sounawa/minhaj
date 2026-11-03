#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""R548 — 3ᵉ passe : points litigieux restants, crops 800-1000 dpi + questions fermées."""
import fitz
import json
import os
import subprocess

HOME = "/home/z/my-project"
PDF = f"{HOME}/content/textbooks-src/hadith-2-iadadi_text.pdf"
CROPS = f"{HOME}/tr-tmp/qa-crops-r548"
OUT = f"{HOME}/tr-tmp/vlm-r548"

BASE = ("Tu lis une image d'un manuel scolaire marocain de hadith (Muwaṭṭaʾ Mālik / "
        "Šarḥ az-Zarqānī, 2e année collégiale). Réponds UNIQUEMENT à la question posée, "
        "par transcription EXACTE du texte imprimé visible, token par token. Si tu n'es "
        "pas sûr d'un mot ou d'un chiffre, écris [illisible]. N'invente AUCUN texte, ne "
        "complète JAMAIS de mémoire (n'utilise PAS de version canonique du hadith que tu "
        "connaîtrais), ne corrige pas l'imprimé même s'il te paraît fautif.")

os.makedirs(OUT, exist_ok=True)
doc = fitz.open(PDF)


def crop(page_no, x0f, y0f, x1f, y1f, dpi, name):
    pg = doc[page_no - 1]
    r = pg.rect
    clip = fitz.Rect(r.width * x0f, r.height * y0f, r.width * x1f, r.height * y1f)
    pix = pg.get_pixmap(matrix=fitz.Matrix(dpi / 72, dpi / 72), clip=clip)
    pix.save(f"{CROPS}/{name}.png")
    print(f"{name}: {pix.width}x{pix.height}")


crop(86, 0.05, 0.34, 0.95, 0.52, 900, "r3-p86-aya")
crop(86, 0.05, 0.26, 0.95, 0.38, 1000, "r3-p86-tamhid-word")
crop(86, 0.05, 0.76, 0.95, 1.00, 1000, "r3-p86-hadith1start")
crop(87, 0.05, 0.20, 0.95, 0.34, 1000, "r3-p87-hadith2-isnad")
crop(87, 0.05, 0.38, 0.95, 0.56, 1000, "r3-p87-bio3")
crop(88, 0.05, 0.02, 0.95, 0.22, 900, "r3-p88-analyse2")
crop(88, 0.05, 0.88, 0.95, 1.00, 1000, "r3-p88-alaaname")
crop(89, 0.05, 0.00, 0.95, 0.24, 800, "r3-p89-attab2")
crop(90, 0.05, 0.54, 0.95, 0.76, 1000, "r3-p90-tirmatn")
crop(90, 0.05, 0.82, 0.95, 1.00, 1000, "r3-p90-iedad2")

ASKS = [
    ("r3-p86-aya", "r3-p86-aya.png",
     "(1) Transcris la citation coranique imprimée en cursive MOT À MOT entre "
     "guillemets/chevrons. (2) Le renvoi entre crochets [الآية: سورة النساء ...] — "
     "le numéro d'āya CHIFFRE PAR CHIFFRE tel qu'imprimé (chiffres arabes orientaux : "
     "écris chaque chiffre séparément). (3) Transcris la phrase qui suit (وقد بينت "
     "السنة...) et la question qui suit (فما هي...)."),
    ("r3-p86-tamhid-word", "r3-p86-tamhid-word.png",
     "Dans la phrase d'introduction, quel est le PREMIER MOT imprimé (avant الصلاة) ? "
     "Réponds : (a) قد (b) تعرف (c) نعتقد (d) autre — transcris-le exactement, puis "
     "transcris les 3-4 mots suivants jusqu'à فرضا."),
    ("r3-p86-hadith1start", "r3-p86-hadith1start.png",
     "(1) L'isnād : مالك عن زيد بن أسلم عن عطاء بن يسار عن [?] — le nom imprimé après "
     "le dernier عن est-il (a) عبد الله الصنابحي (b) أبي سعيد الخدري (c) autre — "
     "transcris-le exactement. (2) Le matn entre guillemets : transcris les 5-6 "
     "premiers mots exactement comme imprimés (commence-t-il par إن الشمس تطلع ؟)."),
    ("r3-p86-hadith1verbs", None, None),
    ("r3-p87-hadith2-isnad", "r3-p87-hadith2-isnad.png",
     "L'isnād imprimé : مالك عن محمد بن [?] بن [?] عن [?] عن أبي هريرة — transcris "
     "LETTRE À LETTRE les noms imprimés entre عن محمد بن and عن الأعرج (le deuxième "
     "nom est-il حيان ? حبان ? بج ? — et le premier : بحي ? يحيى ? بج ?). Puis le mot "
     "imprimé avant عن أبي هريرة est-il (a) الأعرج (b) العرنج (c) autre ?"),
    ("r3-p87-bio3", "r3-p87-bio3.png",
     "(1) Le nom imprimé : وعبدة بن الصامت ou وعبادة بن الصامت ? (il y a-t-il un alif "
     "entre الباء et الدال ?). (2) Transcris mot à mot la phrase de يحيى بن معين "
     "(عبد الله الصنابحي يروي عنه المدنيون...) telle qu'imprimée. (3) Le mot final de "
     "la page après وكان يجلس معه : (a) السرير (b) السير (c) autre ?"),
    ("r3-p88-analyse2", "r3-p88-analyse2.png",
     "Le bloc التحليل : le mot après أحاديث الدرس على est-il (a) الأوقات (b) الأقوال ? "
     "Transcris ensuite la phrase entière (وتتنوع إلى أوقات كراهة وأوقات تحريم...) "
     "telle qu'imprimée."),
    ("r3-p88-alaaname", "r3-p88-alaaname.png",
     "Dans la dernière ligne : دخلنا على [?] بن مالك بعد [?] — le nom imprimé est-il "
     "(a) أنس بن مالك (b) عتس بن مالك (c) عاتس بن مالك (d) autre — transcris-le "
     "exactement, et le mot après بعد : الظهر ? العصر ?"),
    ("r3-p89-attab2", "r3-p89-attab2.png",
     "Transcris TOKEN PAR TOKEN la citation entre guillemets qui commence par تلك "
     "صلاة المنافقين — chaque mot exactement comme imprimé, du début à la fin de la "
     "citation et la clôture [الموطأ رقم: ...] (chiffre par chiffre). Notamment : "
     "quelle est la fin de la citation (ثم ... ركعات ? لا يذكر الله فيها ... ?) — "
     "ne complète pas."),
    ("r3-p90-tirmatn", "r3-p90-tirmatn.png",
     "Transcris TOKEN PAR TOKEN : (1) la citation entre guillemets après أن النبي ﷺ "
     "قال: — chaque mot exactement comme imprimé (même si la graphie paraît "
     "inhabituelle) jusqu'à la fin de la citation ; (2) le renvoi entre crochets "
     "[سنن الترمذي...] entier ; (3) la ligne أستخرج من الحديث... telle qu'imprimée."),
    ("r3-p90-iedad2", "r3-p90-iedad2.png",
     "Transcris TOKEN PAR TOKEN l'item ١- أشرح: suivi des lexies — chaque token "
     "exactement comme imprimé, séparés par des tirets/virgules, ne les reformule "
     "pas, y compris le token après أشعرنا/أشعرنها et celui avant نعي/نعى النجاشي."),
]

for key, img, q in ASKS:
    if img is None:
        continue
    out = f"{OUT}/{key}.json"
    if os.path.exists(out):
        print("•", key, "déjà lu")
        continue
    cmd = ["z-ai", "vision", "-p", f"{BASE}\nQUESTION : {q}", "-i", f"{CROPS}/{img}", "-o", out]
    r = subprocess.run(cmd, capture_output=True, text=True, timeout=300)
    print(("✓" if r.returncode == 0 else "✗"), key, (r.stderr or "").strip()[:150])

print("\n===== RÉSULTATS =====")
for key, img, q in ASKS:
    if img is None:
        continue
    try:
        d = json.load(open(f"{OUT}/{key}.json", encoding="utf-8"))
        print(f"\n----- {key} -----")
        print(d["choices"][0]["message"]["content"][:1800])
    except Exception as e:
        print(f"\n----- {key} ----- ERREUR {e}")

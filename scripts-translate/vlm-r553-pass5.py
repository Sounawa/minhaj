#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""R553 — Passe 5 (reprise) : points litigieux RÉSIDUELS après les passes 1-4 de
la première incarnation (claim 14:56Z, scripts vlm-r553-pass1..4.py + résultats
tr-tmp/vlm-r553/). Chaque ambiguïté est tranchée par preuve image, jamais
devinée : crops 1000-1400 dpi (fitz pixmap+clip) + questions fermées
lettre par lettre / chiffre par chiffre. Retry 429 : pauses 60-120 s."""
import fitz
import json
import os
import subprocess
import time

HOME = "/home/z/my-project"
PDF = f"{HOME}/content/textbooks-src/hadith-2-iadadi_text.pdf"
CROPS = f"{HOME}/tr-tmp/qa-crops-r553"
OUT = f"{HOME}/tr-tmp/vlm-r553"
os.makedirs(OUT, exist_ok=True)

BASE = ("Tu lis une image d'un manuel scolaire marocain de hadith (Muwaṭṭaʾ Mālik / "
        "Šarḥ az-Zarqānī, 2e année collégiale). Réponds UNIQUEMENT à la question posée, "
        "par transcription EXACTE du texte imprimé visible, token par token. Si tu n'es "
        "pas sûr d'un mot ou d'un chiffre, écris [illisible]. N'invente AUCUN texte, ne "
        "complète JAMAIS de mémoire (n'utilise PAS de version canonique du hadith que tu "
        "connaîtrais), ne corrige pas l'imprimé même s'il te paraît fautif.")

doc = fitz.open(PDF)


def crop(page_no, x0, y0, x1, y1, dpi, name):
    pg = doc[page_no - 1]
    clip = fitz.Rect(x0, y0, x1, y1)
    pix = pg.get_pixmap(matrix=fitz.Matrix(dpi / 72, dpi / 72), clip=clip, alpha=False)
    pix.save(f"{CROPS}/{name}.png")
    print(f"crop {name}: {pix.width}x{pix.height} @{dpi}dpi")


# ---- crops de la passe 5 (page 637.2 x 807.1 pt, x en pt, y en pt) ----
CROPS_5 = [
    ("p105-h1-3rd", 105, 40, 620, 620, 730, 1200),
    ("p106-h2-mid", 106, 40, 620, 88, 215, 1000),
    ("p106-sharh-hubba", 106, 40, 620, 600, 705, 1200),
    ("p107-bottom", 107, 40, 620, 545, 690, 1200),
    ("p108-mulawwan", 108, 40, 620, 285, 405, 1200),
    ("p108-nur-big", 108, 130, 330, 100, 190, 1400),
    ("p109-abd-line", 109, 40, 620, 185, 285, 1200),
    ("p110-top3", 110, 40, 620, 0, 78, 1200),
    ("p110-top-renvoi", 110, 40, 620, 78, 160, 1000),
    ("p110-ribs-fin", 110, 40, 620, 232, 348, 1000),
    ("p110-istithmar-open", 110, 40, 620, 468, 565, 1200),
    ("p110-istithmar-fin", 110, 40, 620, 588, 700, 1200),
]
for name, pg, x0, x1, y0, y1, dpi in CROPS_5:
    crop(pg, x0, y0, x1, y1, dpi, name)

ASKS = [
    ("p5-p105-h1-3rd", "p105-h1-3rd.png",
     "Le hadith compte trois membres « ليس فيما دون … صدقة ». Pour le TROISIÈME "
     "membre « وليس فيما دون خمسة … صدقة » : transcris le mot entre « خمسة » et "
     "« صدقة » LETTRE PAR LETTRE — est-il أوسق ? أواق ? ذود ? autre ? Puis le renvoi "
     "rouge [الموطأ رقم : N] de ce hadith : N CHIFFRE PAR CHIFFRE (655 ? 556 ? "
     "autre ?). Réponds : « mot3=…, lettres : …, renvoi=…, chiffres : … »."),
    ("p5-p106-h2-mid", "p106-h2-mid.png",
     "Transcris TOKEN PAR TOKEN le texte imprimé depuis « : إن من بلغت حصته منهم "
     "عشرين دينارا عينا أو مائتي درهم » jusqu'à « فلا زكاة عليه ». Chaque mot "
     "exactement : (1) y a-t-il un mot/groupe après « مائتي درهم » avant la suite "
     "(« فعليه فيها الزكاة » ? « فقد وجبت » ? « فهي نصاب » ? autre ?) ; (2) la "
     "suite est-elle « ومن نقصت حصته عما تجب فيه الزكاة فلا زكاة عليه » ? "
     "Transcris aussi la ligne d'après jusqu'à « وإن بلغت حصصهم جميعا » et la ligne "
     "« وكان بعضهم في ذلك أفضل نصيبا من بعض… أخذ من كل إنسان بقدر حصته » — y "
     "a-t-il un « ف » devant « أخذ » ? Réponds : transcription complète puis "
     "« apres_drham=…, f_devant_akhada=… »."),
    ("p5-p106-sharh-hubba", "p106-sharh-hubba.png",
     "Dans le شرح (définition des أواق) : « والدرهم الشرعي … حبة من مطلق الشعير. "
     "وهي : تسعة عشر ومائة غرام بناء على أن الدرهم يزن 2,975 غرام ». (1) Le "
     "nombre de grains : transcris-le MOT À MOT — « خمسون وخمسا حبة » ? le second "
     "mot porte-t-il fatḥa sur le khāʾ (خَمْسًا = cinq) ou ḍamma (خُمُسًا = un "
     "cinquième) ? (2) Transcris « وهي : تسعة عشر ومائة غرام » exactement. (3) Le "
     "poids du dirham : 2,975 — transcris-le CHIFFRE PAR CHIFFRE tel qu'imprimé "
     "(2,975 ? 5,792 ? autre ?). Réponds : « grains=…, diacritique=…, poids=…, "
     "chiffres : … »."),
    ("p5-p107-bottom", "p107-bottom.png",
     "Transcris TOKEN PAR TOKEN le dernier paragraphe de la page (il commence par "
     "« وتستعمل شرعا بمعنى النماء » et finit par « وتطهير من الذنوب »). Puis, dans "
     "la phrase « فسميت زكاة بما ___ إليه إخراجها » : le verbe LETTRE PAR LETTRE — "
     "la 3e lettre est-elle hamza (يؤول) ou qāf (يقول) ? Réponds : « paragraphe=…, "
     "verbe=…, lettres : … »."),
    ("p5-p108-mulawwan", "p108-mulawwan.png",
     "Dans l'item « طهارة للمال ; لأن تعلق حق الغير به يجعله ___ لا يطهر إلا "
     "بإخراجه منه » : le mot après « يجعله » LETTRE PAR LETTRE — la 4e lettre "
     "porte-t-elle UN point (ملونًا = ن) ou TROIS points (ملوثًا = ث) au-dessus ? "
     "Réponds : « mot=…, lettres : …, points_4e_lettre=… »."),
    ("p5-p108-nur-big", "p108-nur-big.png",
     "Le renvoi rouge imprimé après le verset ﴿وأقيموا الصلاة وآتوا الزكاة﴾ (et "
     "avant « وقال عليه الصلاة والسلام »). Transcris-le ENTIER : [سورة …، الآية "
     "N]. Le numéro CHIFFRE PAR CHIFFRE dans l'ordre d'écriture gauche→droite : "
     "54 ? 45 ? 56 ? 64 ? autre ? Réponds : « renvoi_complet=…, "
     "chiffres_gauche_a_droite=…, numéro=… »."),
    ("p5-p109-abd-line", "p109-abd-line.png",
     "Le cas rapporté de Mālik : « قال مالك في رجل كانت عنده … ومائة درهم و… "
     "وصرف الدراهم … دراهم بدينار ». (1) Le nombre de dirhams LETTRE PAR LETTRE : "
     "ستون (60) ou سبعون (70) ou autre ? (2) Le mot après « وصرف الدراهم » LETTRE "
     "PAR LETTRE : ببلده ? ببيضة ? autre ? (3) Le taux : ثمانية (8) ou ثمانين "
     "(80) — LETTRE PAR LETTRE ? (4) La réponse de Mālik ouvre par « إنها لا "
     "تجب » ou « إنما لا تجب » ou « إنها لا تجب فيها الزكاة وإنما تجب » ? "
     "Transcris-la MOT À MOT jusqu'au renvoi rouge [الموطأ رقم : N] (N chiffre par "
     "chiffre). Réponds : « dirhams=…, mot=…, taux=…, réponse=…, renvoi=… »."),
    ("p5-p110-top3", "p110-top3.png",
     "Transcris TOKEN PAR TOKEN la PREMIÈRE ligne imprimée de la page (elle "
     "s'achève probablement par un verbe + « بها، »). Le mot d'ouverture (fin de la "
     "phrase commencée p.109 « لأنها تجددت لا عن مال… ») LETTRE PAR LETTRE : "
     "فيستقبل ? فيستفتي ? يستأنف ? فيستقيل ? فيصدق ? autre ? Y a-t-il un PETIT "
     "CHIFFRE en exposant (46 ? 64 ?) sur cette ligne — après quel mot ? Réponds : "
     "« ligne=…, mot=…, lettres : …, exposant=… »."),
    ("p5-p110-top-renvoi", "p110-top-renvoi.png",
     "Transcris TOKEN PAR TOKEN la fin du récit d'Abū Bakr depuis « وَإِنْ قَالَ : "
     "لا، » jusqu'à la fin de la citation, puis le renvoi rouge [الموطأ رقم : N] "
     "— N CHIFFRE PAR CHIFFRE (658 ? 656 ? 668 ? autre ?). Y a-t-il un nombre "
     "« 46 » imprimé (en exposant ou dans le texte) sur ces lignes ? Réponds : "
     "« fin=…, renvoi=…, chiffres : …, nombre46=… »."),
    ("p5-p110-ribs-fin", "p110-ribs-fin.png",
     "Le passage « حول الربح : من كان له مال دون النصاب وتجر فيه … لقول مالك في "
     "رجل كانت له … دنانير فتجر فيها فحال عليها الحول وقد بلغت … دينارا ». (1) "
     "Le PREMIER nombre de dinars : عشرة (10) ou عشرين (20) ? (2) Le SECOND "
     "nombre : عشرة ou عشرين ? (3) La citation de Mālik se referme par « حتى "
     "يحول عليها الحول من يوم ___ » : le dernier mot LETTRE PAR LETTRE — زكاها ? "
     "زكاتها ? زكيت ? زكت ? أكملها ? autre ? (4) Le renvoi rouge [الموطأ رقم : "
     "N] : N chiffre par chiffre. Réponds : « nombre1=…, nombre2=…, mot_final=…, "
     "lettres : …, renvoi=… »."),
    ("p5-p110-istithmar-open", "p110-istithmar-open.png",
     "L'ouverture de la section الاستثمار : transcris TOKEN PAR TOKEN l'en-tête "
     "et la première phrase (« قال مالك في رجل كانت له … دنانير من … أو غيرها "
     "فتجر فيها … »). (1) Le nombre de dinars LETTRE PAR LETTRE : خمسة (5) ? "
     "عشرة (10) ? خمسون (50) ? autre ? (2) Le mot après : فائدة (avec د) ou "
     "فائضة (avec ض) — LETTRE PAR LETTRE ? Réponds : « phrase=…, nombre=…, "
     "lettres : …, mot=…, lettres_mot : … »."),
    ("p5-p110-istithmar-fin", "p110-istithmar-fin.png",
     "La citation de Mālik dans l'exploitation (الاستثمار) se referme par « …حتى "
     "يحول عليها الحول من يوم ___ » : le dernier mot LETTRE PAR LETTRE — زكيت ? "
     "زكاتها ? زكاها ? زكيت ? autre ? Transcris les 8-10 derniers mots de la "
     "citation MOT À MOT, puis le renvoi rouge [الموطأ رقم : N] CHIFFRE PAR "
     "CHIFFRE, puis les DEUX questions finales MOT À MOT. Réponds : « "
     "fin_citation=…, mot_final=…, lettres : …, renvoi=…, q1=…, q2=… »."),
]


def ask(key, img, q):
    out = f"{OUT}/{key}.json"
    if os.path.exists(out):
        print("•", key, "déjà lu")
        return True
    cmd = ["z-ai", "vision", "-p", f"{BASE}\nQUESTION : {q}", "-i", f"{CROPS}/{img}", "-o", out]
    for attempt in range(1, 5):
        r = subprocess.run(cmd, capture_output=True, text=True, timeout=300)
        if r.returncode == 0 and os.path.exists(out):
            print("✓", key)
            return True
        err = (r.stderr or r.stdout or "").strip()[:160]
        print(f"✗ {key} essai {attempt} : {err}")
        if attempt < 4:
            pause = 60 + 30 * attempt  # 60, 90, 120 s — saturation 429
            print(f"   pause {pause} s avant nouvelle tentative…")
            time.sleep(pause)
    return False


for key, img, q in ASKS:
    ask(key, img, q)

print("\n===== RÉSULTATS PASSE 5 =====")
for key, img, q in ASKS:
    try:
        d = json.load(open(f"{OUT}/{key}.json", encoding="utf-8"))
        print(f"\n----- {key} -----")
        print(d["choices"][0]["message"]["content"][:2400])
    except Exception as e:
        print(f"\n----- {key} ----- ERREUR {e}")

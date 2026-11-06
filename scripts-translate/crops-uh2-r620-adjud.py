# -*- coding: utf-8 -*-
"""R620 — adjudication finale leçon 7 ulum-hadith-tanawi-2 (pdf-mut23h2u-261,
الحديث الحسن, p.41-46 de ulum-hadith-2-thanawi_text.pdf).
Recadrages ciblés des zones encore ambiguës après couches (pdftotext/OCR/pymu)
+ verdicts VLM de la passe préparatoire. Lecture DIRECTE de l'ouvrier (sans VLM)
sauf --vlm. Sortie : tr-tmp/qa-crops-r620/<X>.png
Usage : python3 scripts-translate/crops-uh2-r620-adjud.py [--vlm]
"""
import os, subprocess, sys, time

from PIL import Image
import fitz

HOME = "/home/z/my-project"
PDF = f"{HOME}/content/textbooks-src/ulum-hadith-2-thanawi_text.pdf"
OUT = f"{HOME}/tr-tmp/qa-crops-r620"
VLM = f"{HOME}/tr-tmp/r620"

# (page, y0, y1, x0, x1, dpi)
ZONES = {
    # p.41 المتن : « في الـ ? حيث الـ ? » — التقلید/الناقل، التفرّد/التقرّد (900 dpi)
    "ADJ1-p41-quote900":  [(41, 0.545, 0.725, 0.03, 0.98, 900)],
    # p.42 القسم الثاني milieu : « وهو مع ذلك يـ ? » + سلامته من أن يكون معللا + ref
    "ADJ2-p42-qism2b":    [(42, 0.575, 0.805, 0.03, 0.98, 600)],
    # p.43 citation ابن الصلاح début : بن علقمة/عاقبة + من المشهورين/الشهورين
    "ADJ3-p43-ibnsalah":  [(43, 0.125, 0.345, 0.03, 0.98, 600)],
    # p.44 haut : fin commentaire مجالد + en-tête ثانيا + titre 1. مراتبه
    "ADJ4-p44-top":       [(44, 0.005, 0.135, 0.03, 0.98, 600)],
    # p.44 مصادره paragraphe complet + éventuel titre 3. حكمه (absent du G4)
    "ADJ5-p44-masadir":   [(44, 0.405, 0.585, 0.03, 0.98, 600)],
    # p.45 récit Mālik milieu : « توضأ و تهيا ? و لبس ثيابه / و لم يثبه »
    "ADJ6-p45-malik":     [(45, 0.615, 0.865, 0.03, 0.98, 600)],
}

BASE = ("Tu lis une image d'un manuel scolaire marocain de hadith (sciences du "
        "ḥadīṯ, 2e année secondaire, commentaire de la Nuḫbat al-fikr). Réponds "
        "UNIQUEMENT à la question posée, par transcription EXACTE du texte "
        "imprimé visible, token par token. Si tu n'es pas sûr d'un mot ou d'un "
        "chiffre, écris [illisible]. N'invente AUCUN texte, ne complète JAMAIS de "
        "mémoire (n'utilise PAS la version canonique d'un hadith que tu "
        "connaîtrais), ne corrige pas l'imprimé même s'il te paraît fautif.")

QUESTIONS = {
    "ADJ1-p41-quote900": (
        "(1) Transcris la citation du المتن MOT À MOT : après « فإن جمعا » que "
        "lit-on EXACTEMENT, lettre à lettre (فلتردد? فلا تردد?), puis après « في "
        "الـ » (التقليد? الناقل? النقل? autre?) puis après « حيث » (التفرد? "
        "التقرّد? autre?) et le mot final après « وإلا فاعتبار » (إسنادين?). "
        "Regarde LES POINTS DE DIAKRITIQUE un par un. Ne complète JAMAIS de "
        "mémoire."),
    "ADJ2-p42-qism2b": (
        "(1) Transcris les lignes MOT À MOT : après « وهو مع ذلك » que lit-on "
        "EXACTEMENT (يرتفع عن حال? يخاف على حاله? autre?) lettre à lettre ; puis "
        "la fin de la phrase « سلامته من أن يكون... » ; puis le mot après « "
        "يتنزل كلام » (الخطابي?) et la référence entre crochets avec les "
        "CHIFFRES EXACTS un par un (ص: 32-31? 31-32?). Ne complète JAMAIS de "
        "mémoire."),
    "ADJ3-p43-ibnsalah": (
        "(1) Transcris la citation de ابن الصلاح MOT À MOT depuis « فمحمد بن "
        "عمرو » : le nom du père du grand-père EXACTEMENT (بن علقمة? بن عاقبة? "
        "autre?) lettre à lettre ; puis « من الـ » (المشهورين? الشهورين?) avec "
        "les points. Ne complète JAMAIS de mémoire."),
    "ADJ4-p44-top": (
        "(1) Transcris TOUTES les lignes visibles MOT À MOT de haut en bas, y "
        "compris l'en-tête de section s'il y en a une (ثانيا : ...? محاور...?) "
        "et les titres numérotés (1. مراتبه?). Ne complète JAMAIS de mémoire."),
    "ADJ5-p44-masadir": (
        "(1) Transcris TOUTES les lignes visibles MOT À MOT de haut en bas, y "
        "compris un éventuel titre numéroté (3. حكمه? autre?). Transcris la "
        "fin de la phrase sur جامع الترمذي (إذ فيه الحسن...). Ne complète "
        "JAMAIS de mémoire."),
    "ADJ6-p45-malik": (
        "(1) Transcris le récit de مصعب بن عبد الله MOT À MOT : après « إذا حدث "
        "عن رسول الله » que lit-on EXACTEMENT (توضأ و تهيا? توضأ و تهيأ?), puis "
        "le mot suivant EXACTEMENT (ولبس ثيابه? و لم يثبه? autre?) lettre à "
        "lettre avec les points, puis la référence entre crochets avec les "
        "CHIFFRES EXACTS (2/45? 45/2?). Ne complète JAMAIS de mémoire."),
}


def crop(doc, page, y0, y1, x0, x1, dpi) -> Image.Image:
    pg = doc[page - 1]
    r = pg.rect
    clip = fitz.Rect(r.width * x0, r.height * y0, r.width * x1, r.height * y1)
    pm = pg.get_pixmap(matrix=fitz.Matrix(dpi / 72, dpi / 72), clip=clip)
    return Image.frombytes("RGB", (pm.width, pm.height), pm.samples)


def compose(name, parts):
    pieces = []
    for img in parts:
        w, h = img.size
        if w > 1560:
            nh = int(h * 1560 / w)
            img = img.resize((1560, nh), Image.LANCZOS)
        pieces.append(img)
    W = max(p.size[0] for p in pieces)
    H = sum(p.size[1] for p in pieces) + 8 * (len(pieces) - 1)
    canvas = Image.new("RGB", (W, H), (255, 230, 230))
    y = 0
    for p in pieces:
        canvas.paste(p, (0, y))
        y += p.size[1] + 8
    path = f"{OUT}/{name}.png"
    canvas.save(path)
    print(f"{path} {canvas.size[0]}x{canvas.size[1]}")


def read_one(name, img):
    out = f"{VLM}/vlm-{name}.json"
    cmd = ["z-ai", "vision", "-p", f"{BASE}\nQUESTION : {QUESTIONS[name]}",
           "-i", img, "-o", out]
    for attempt in range(4):
        r = subprocess.run(cmd, capture_output=True, text=True, timeout=300)
        if r.returncode == 0:
            print(f"  ✓ VLM {name} → {out}")
            return True
        err = (r.stderr or "").strip()[:120]
        print(f"  ↻ {name} tentative {attempt + 1} échec : {err}")
        time.sleep(20 + attempt * 20)
    return False


def main() -> int:
    os.makedirs(OUT, exist_ok=True)
    os.makedirs(VLM, exist_ok=True)
    do_vlm = "--vlm" in sys.argv[1:]
    doc = fitz.open(PDF)
    for name, zones in ZONES.items():
        imgs = [crop(doc, p, y0, y1, x0, x1, dpi)
                for (p, y0, y1, x0, x1, dpi) in zones]
        comp = f"{OUT}/{name}.png"
        compose(name, imgs)
        if do_vlm:
            if not read_one(name, comp):
                print(f"  ✗ VLM {name} ÉCHEC DÉFINITIF (4 tentatives)")
    return 0


if __name__ == "__main__":
    sys.exit(main())

# -*- coding: utf-8 -*-
"""R619 — crops d'adjudication image, leçon 6 ulum-hadith-tanawi-2
(pdf-mut23h2u-260, الحديث الصحيح ومراتبه, p.35-40 de ulum-hadith-2-thanawi_text.pdf).
Passes 2 : bandes fines 600 dpi (résolution doublée) pour les zones encore
ambiguës après la passe 1 (matn Buḫārī, isnād Ṭabarānī pointu, chaîne az-Zuhrī
oubliée par OCR+VLM, chaîne عاصم بن ?, citation p.35).
Sortie : tr-tmp/qa-crops-r619/<X>.png puis tr-tmp/r619/vlm-<X>.json
Usage : python3 scripts-translate/crops-uh2-r619.py [--vlm]
"""
import os, subprocess, sys, time

from PIL import Image
import fitz

HOME = "/home/z/my-project"
PDF = f"{HOME}/content/textbooks-src/ulum-hadith-2-thanawi_text.pdf"
OUT = f"{HOME}/tr-tmp/qa-crops-r619"
VLM = f"{HOME}/tr-tmp/r619"
DPI = 600

ZONES = {
    # G3 — p.37 : lignes de l'isnād Ṭabarānī, pleine largeur de colonne
    "G3-p37-isnad":    [(37, 0.40, 0.62, 0.03, 0.60)],
    # H2 — p.35 : citation ابن حجر complète + sa fin (قدّم القومُ ؟)
    "H2-p35-quote":    [(35, 0.26, 0.56, 0.05, 0.95)],
    # I — p.36 : définition de عدل (ملازمة التقوى + ؟) et les deux ضبط
    "I-p36-adl":       [(36, 0.46, 0.72, 0.05, 0.95)],
}

BASE = ("Tu lis une image d'un manuel scolaire marocain de hadith (sciences du "
        "ḥadīṯ, 2e année secondaire, commentaire de la Nuḫbat al-fikr). Réponds "
        "UNIQUEMENT à la question posée, par transcription EXACTE du texte "
        "imprimé visible, token par token. Si tu n'es pas sûr d'un mot ou d'un "
        "chiffre, écris [illisible]. N'invente AUCUN texte, ne complète JAMAIS de "
        "mémoire (n'utilise PAS la version canonique d'un hadith que tu "
        "connaîtrais), ne corrige pas l'imprimé même s'il te paraît fautif.")

QUESTIONS = {
    "G3-p37-isnad": (
        "(1) Transcris l'isnād LIGNE PAR LIGNE lettre à lettre, de حدثنا العباس بن "
        "الفصل jusqu'à عن ابن عمر. OBLIGATOIRE : (a) le nom après le DEUXIÈME حدثنا "
        "— lettre à lettre avec tous les points (أبو تابت? أبو قاتب? أبو تميم? autre?) "
        "et dis si le mot محمد suit ; (b) la nisba de ce rapporteur : première lettre "
        "après ال (د? ي?) et le mot entier ; (c) le nom du rapporteur : عبد الله ou "
        "عبيد الله ? (d) la nisba du premier rapporteur (الأسفاطي? الأسفاتي?). "
        "Ne complète JAMAIS de mémoire."),
    "H2-p35-quote": (
        "(1) Transcris la citation ENTRE chevrons MOT À MOT complète depuis « وخبر "
        "الآحاد » jusqu'au chevron FERMANT — lettre à lettre pour la fin : que lit-on "
        "EXACTEMENT après « ومن ثم قدّم القومُ » ? (صحيح البخاري على صحيح مسلم? على "
        "مسلم? autre?). (2) Transcris le début de la citation (وخبر الآحاد بنقل ? تام "
        "? — الصبط? الضبط?). Ne complète JAMAIS de mémoire."),
    "I-p36-adl": (
        "(1) Transcris la définition ب- عدالة الرواة MOT À MOT : « والعدل: من عنده "
        "ملكه تحمله على ملازمة التقوى و? » — la suite lettre à lettre (والبعد عن الفسق "
        "وخوارم المروءة? ومجانبة المروءة? autre?). (2) Transcris la définition ج- ضبط "
        "الرواة (وتمام الضبط يقصد به...). (3) Les deux types de ضبط (ضبط صدر... / ضبط "
        "كتاب...) s'ils sont visibles. Ne complète JAMAIS de mémoire."),
}


def crop(doc, page, y0, y1, x0, x1) -> Image.Image:
    pg = doc[page - 1]
    r = pg.rect
    clip = fitz.Rect(r.width * x0, r.height * y0, r.width * x1, r.height * y1)
    pm = pg.get_pixmap(matrix=fitz.Matrix(DPI / 72, DPI / 72), clip=clip)
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
        imgs = [crop(doc, p, y0, y1, x0, x1) for (p, y0, y1, x0, x1) in zones]
        comp = f"{OUT}/{name}.png"
        compose(name, imgs)
        if do_vlm:
            if not read_one(name, comp):
                print(f"  ✗ VLM {name} ÉCHEC DÉFINITIF (4 tentatives)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

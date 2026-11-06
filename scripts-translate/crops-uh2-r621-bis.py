# -*- coding: utf-8 -*-
"""R621 — complément d'adjudication : citation d'Ibn Ḥaǧar p.47, TABLE des صور
p.48, الشكل التالي p.49 — moitiés coupées pour zoom effectif ~576 dpi
(cap 2600 px au lieu de 1560). Sortie tr-tmp/qa-crops-r621/<X>.png et
tr-tmp/r621/vlm-<X>.json. Usage : python3 scripts-translate/crops-uh2-r621-bis.py [--vlm]"""
import os, subprocess, sys, time

from PIL import Image
import fitz

HOME = "/home/z/my-project"
PDF = f"{HOME}/content/textbooks-src/ulum-hadith-2-thanawi_text.pdf"
OUT = f"{HOME}/tr-tmp/qa-crops-r621"
VLM = f"{HOME}/tr-tmp/r621"
DPI = 600
CAP = 2600

ZONES = {
    # P — p.47 : citation du متن en deux moitiés empilées (droite puis gauche)
    "P-p47-quote2": [(47, 0.608, 0.690, 0.40, 0.99), (47, 0.608, 0.690, 0.04, 0.52)],
    # Q — p.48 : TABLE des صور en deux moitiés (droite puis gauche)
    "Q-p48-table2": [(48, 0.330, 0.550, 0.45, 0.99), (48, 0.330, 0.550, 0.03, 0.50)],
    # R — p.49 : الشكل التالي en deux moitiés (droite puis gauche)
    "R-p49-shakl2": [(49, 0.212, 0.545, 0.40, 0.99), (49, 0.212, 0.545, 0.03, 0.55)],
}

BASE = ("Tu lis une image d'un manuel scolaire marocain de hadith (sciences du "
        "ḥadīṯ, 2e année secondaire). Réponds UNIQUEMENT à la question posée, "
        "par transcription EXACTE du texte imprimé visible, token par token. Si "
        "tu n'es pas sûr d'un mot ou d'un chiffre, écris [illisible]. N'invente "
        "AUCUN texte, ne complète JAMAIS de mémoire, ne corrige pas l'imprimé "
        "même s'il te paraît fautif.")

QUESTIONS = {
    "P-p47-quote2": (
        "L'image montre la citation d'Ibn Ḥaǧar en DEUX moitiés empilées (moitié "
        "DROITE de la ligne en haut, moitié GAUCHE en bas). Transcris la citation "
        "ENTIÈRE lettre à lettre avec diacritiques, dans l'ordre de lecture. "
        "Réponds PRÉCISÉMENT : (a) après « ما لم تنافئ » que lit-on EXACTEMENT "
        "(من هو أوثق? مناط العدل? autre?) ; (b) entre « فالراجح المحفوظ » et "
        "« الشاذ » que lit-on EXACTEMENT (ومقابله? ومابله? ولا بقيته? autre?) ; "
        "(c) le mot après « وزيادة » (راويهما? روايهما?). Ne complète JAMAIS de "
        "mémoire."),
    "Q-p48-table2": (
        "L'image montre le TABLEAU des صور زيادة الثقة en deux moitiés (DROITE "
        "en haut, GAUCHE en bas). Transcris CHAQUE case lettre à lettre : (a) le "
        "texte exact des DEUX cases-mères supérieures (باعتبار...?), avec leur "
        "position (droite/gauche) ; (b) le texte exact de CHAQUE case-fille, "
        "lettre à lettre (في السند? إي السند? في المتن? في السند والمتن? واحد? "
        "أكثر من واحد? autre?); (c) indique combien de cases-filles sous chaque "
        "case-mère. Ne complète JAMAIS de mémoire."),
    "R-p49-shakl2": (
        "L'image montre le SCHÉMA (أحوال زيادة الثقة) en deux moitiés (DROITE en "
        "haut, GAUCHE en bas). Transcris CHAQUE case lettre à lettre : (a) la "
        "case verte centrale à droite (أحوال...?) ; (b) les QUATRE cases "
        "centrales pâles, lettre à lettre (أن لا تكون منافية? أن تكون مخالفة "
        "لمن هو أوثق? أن تكون مخالفة لمن هو أقل منه? la QUATRIÈME au complet : "
        "أن تكون مخالفة لما...? لمماثل? لغيره? autre?) ; (c) les QUATRE cases "
        "jaunes de sortie, lettre à lettre, avec laquelle correspond à quelle "
        "case centrale (مقبولة? مردودة? مقبولة? يتوقف فيها? autre?). Ne complète "
        "JAMAIS de mémoire."),
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
        if w > CAP:
            nh = int(h * CAP / w)
            img = img.resize((CAP, nh), Image.LANCZOS)
        pieces.append(img)
    W = max(p.size[0] for p in pieces)
    H = sum(p.size[1] for p in pieces) + 12 * (len(pieces) - 1)
    canvas = Image.new("RGB", (W, H), (255, 210, 210))
    y = 0
    for p in pieces:
        canvas.paste(p, (0, y))
        y += p.size[1] + 12
    path = f"{OUT}/{name}.png"
    canvas.save(path)
    print(f"{path} {canvas.size[0]}x{canvas.size[1]}")


def read_one(name, img):
    out = f"{VLM}/vlm-{name}.json"
    if os.path.exists(out) and os.path.getsize(out) > 50:
        print(f"  ✓ VLM {name} (cache) → {out}")
        return True
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
    sys.exit(main())

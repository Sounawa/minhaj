# -*- coding: utf-8 -*-
"""R621 — adjudication finale : citation d'Ibn Ḥaǧar p.47 (lignes 1-2, 900 dpi,
moitiés empilées) et case 4 du الشكل p.49. Sortie tr-tmp/qa-crops-r621/<X>.png
et tr-tmp/r621/vlm-<X>.json. Usage : python3 scripts-translate/crops-uh2-r621-ter.py [--vlm]"""
import os, subprocess, sys, time

from PIL import Image
import fitz

HOME = "/home/z/my-project"
PDF = f"{HOME}/content/textbooks-src/ulum-hadith-2-thanawi_text.pdf"
OUT = f"{HOME}/tr-tmp/qa-crops-r621"
VLM = f"{HOME}/tr-tmp/r621"
DPI = 900
CAP = 2600

ZONES = {
    # S1 — ligne 1 de la citation (droite puis gauche)
    "S1-p47-l1": [(47, 0.610, 0.650, 0.50, 0.97), (47, 0.610, 0.650, 0.06, 0.55)],
    # S2 — ligne 2 de la citation (droite puis gauche)
    "S2-p47-l2": [(47, 0.645, 0.692, 0.55, 0.97), (47, 0.645, 0.692, 0.06, 0.60)],
    # S3 — case 4 du schéma + sa sortie jaune (droite puis gauche)
    "S3-p49-case4": [(49, 0.420, 0.520, 0.38, 0.99), (49, 0.420, 0.520, 0.03, 0.42)],
}

BASE = ("Tu lis une image d'un manuel scolaire marocain de hadith. Réponds "
        "UNIQUEMENT à la question posée, par transcription EXACTE du texte "
        "imprimé visible, token par token, lettre à lettre. Si tu n'es pas sûr, "
        "écris [illisible]. N'invente AUCUN texte, ne complète JAMAIS de "
        "mémoire, ne corrige pas l'imprimé même s'il te paraît fautif.")

QUESTIONS = {
    "S1-p47-l1": (
        "L'image montre la LIGNE 1 de la citation en deux moitiés empilées "
        "(moitié DROITE en haut, moitié GAUCHE en bas — le début de la phrase "
        "est à droite). Transcris TOUTE la ligne lettre à lettre avec "
        "diacritiques, de « قال الحافظ » jusqu'au dernier mot visible. Ensuite "
        "réponds : après « مقبولة ما لم » que lit-on EXACTEMENT mot par mot "
        "(تنافئ من هو أوثق? تنافئ مناط العدل? تنافي منافية...? autre? — épelle "
        "chaque mot). Ne complète JAMAIS de mémoire."),
    "S2-p47-l2": (
        "L'image montre la LIGNE 2 de la citation en deux moitiés empilées "
        "(DROITE en haut, GAUCHE en bas). Transcris TOUTE la ligne lettre à "
        "lettre avec diacritiques (فإن خولف بأرجح...). Réponds : entre "
        "« فالراجح المحفوظ » et « الشاذ » que lit-on EXACTEMENT (ومقابله? "
        "ومابله? ولا بقيته? autre?) — épelle les lettres. Et le mot après "
        "« وزيادة » en haut (راويهما?). Ne complète JAMAIS de mémoire."),
    "S3-p49-case4": (
        "L'image montre la 4e case du schéma أحوال زيادة الثقة en deux moitiés "
        "(DROITE en haut, GAUCHE en bas). Transcris EXACTEMENT : (a) le texte "
        "de la case pâle n°4, lettre à lettre (أن تكون مخالفة لما...? — le mot "
        "après مخالفة : لمماثل? لماثل? لمثله? autre?) ; (b) le texte de la "
        "case jaune correspondante (يتوقف فيها? autre?). Ne complète JAMAIS de "
        "mémoire."),
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

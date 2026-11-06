# -*- coding: utf-8 -*-
"""R621 — crops d'adjudication image, leçon 8 ulum-hadith-tanawi-2
(pdf-mut23h2u-262, زيادة الثقة والمحفوظ والشاذ, p.47-51 de
ulum-hadith-2-thanawi_text.pdf). Recadrages 600 dpi des zones ambiguës après
couches (pdftotext miroir / OCR 300 / pymu) : bannière p.47, citation d'Ibn
Ḥaǧar diacritée, boîte الفهم, TABLE des صور زيادة الثقة p.48 (graphique muet),
الشكل التالي p.49 (graphique muet), références مقاييس اللغة (87/2, 180/3),
الجامع لأخلاق الراوي (208/2), isnād/matn/refs الترمذي et البخاري (العقدي?),
fin الاستثمار + مقدمة ابن الصلاح (ص: 79/97?) + ligne dégradée, التقويم,
الإعداد القبلي, début أهتدي وأقتدي (الخطيب البغدادي).
Sortie : tr-tmp/qa-crops-r621/<X>.png puis tr-tmp/r621/vlm-<X>.json
Usage : python3 scripts-translate/crops-uh2-r621.py [--vlm]
"""
import os, subprocess, sys, time

from PIL import Image
import fitz

HOME = "/home/z/my-project"
PDF = f"{HOME}/content/textbooks-src/ulum-hadith-2-thanawi_text.pdf"
OUT = f"{HOME}/tr-tmp/qa-crops-r621"
VLM = f"{HOME}/tr-tmp/r621"
DPI = 600

ZONES = {
    # N — p.47 : bannière calligraphique الدرس 8 + titre
    "N-p47-banner":    [(47, 0.015, 0.190, 0.03, 0.99)],
    # A — p.47 : citation du متن (Ibn Ḥaǧar) diacritée, mot à mot
    "A-p47-matn":      [(47, 0.585, 0.700, 0.04, 0.99)],
    # B — p.47 : boîte الفهم (شرح الثقة/المحفوظ + استخلاص المضامين)
    "B-p47-fahm":      [(47, 0.695, 0.935, 0.03, 0.99)],
    # C — p.48 : fin définition (تدرى?) + TABLE des صور زيادة الثقة (graphique)
    "C-p48-surat":     [(48, 0.240, 0.550, 0.03, 0.99)],
    # D — p.49 : الشكل التالي (diagramme graphique de زيادة الثقة)
    "D-p49-shakl":     [(49, 0.210, 0.545, 0.03, 0.99)],
    # E — p.49 : réf مقاييس اللغة (حفظ) — chiffres un par un
    "E-p49-maqayis":   [(49, 0.635, 0.685, 0.04, 0.99)],
    # F — p.50 : réf مقاييس اللغة (شذذ) — chiffres un par un
    "F-p50-maqayis":   [(50, 0.262, 0.302, 0.04, 0.99)],
    # G — p.50 : isnād/matn/réf الترمذي (بشر بن معاذ العقدي? العكبري?)
    "G-p50-tirmidhi":  [(50, 0.548, 0.652, 0.04, 0.99)],
    # H — p.50 : isnād/matn/réf البخاري (عروة بن الزبير, الشق الأيمن)
    "H-p50-bukhari":   [(50, 0.688, 0.785, 0.04, 0.99)],
    # M — p.50 : début أهتدي وأقتدي (الخطيب : قلما يتَمَهَّر?)
    "M-p50-khatib":    [(50, 0.832, 0.935, 0.03, 0.99)],
    # I — p.51 : fin citation ابن الصلاح + réf مقدمة ابن الصلاح ص:? + ligne dégradée
    "I-p51-istithmar": [(51, 0.540, 0.700, 0.03, 0.99)],
    # J — p.51 : réf الجامع لأخلاق الراوي (208/2) — chiffres un par un
    "J-p51-jami":      [(51, 0.118, 0.165, 0.04, 0.99)],
    # K — p.51 : التقويم, items 1-3 (item 2 dégradé en pymu)
    "K-p51-taqwim":    [(51, 0.225, 0.355, 0.03, 0.99)],
    # L — p.51 : الإعداد القبلي, 2 consignes
    "L-p51-idad":      [(51, 0.700, 0.895, 0.03, 0.99)],
}

BASE = ("Tu lis une image d'un manuel scolaire marocain de hadith (sciences du "
        "ḥadīṯ, 2e année secondaire, commentaire de la Nuḫbat al-fikr). Réponds "
        "UNIQUEMENT à la question posée, par transcription EXACTE du texte "
        "imprimé visible, token par token. Si tu n'es pas sûr d'un mot ou d'un "
        "chiffre, écris [illisible]. N'invente AUCUN texte, ne complète JAMAIS de "
        "mémoire (n'utilise PAS la version canonique d'un hadith que tu "
        "connaîtrais), ne corrige pas l'imprimé même s'il te paraît fautif.")

QUESTIONS = {
    "N-p47-banner": (
        "(1) Décris la bannière en tête : quel numéro de leçon lit-on dans la "
        "calligraphie (الدرس ... ? — chiffre exact) et quel est le TITRE imprimé "
        "sous la bannière, lettre à lettre. (2) Transcris la première ligne des "
        "objectifs (أن أتعرف ...) visible en bas si présente. Ne complète JAMAIS "
        "de mémoire."),
    "A-p47-matn": (
        "(1) Transcris la citation entre guillemets MOT À MOT, lettre à lettre, "
        "avec les diacritiques visibles : depuis « وزيادة » jusqu'au guillemet "
        "fermant. Que lit-on EXACTEMENT après « مقبولة » (ما لم تنافئ? ما لم "
        "تناف? autre?), après « فان خولف بارجح » (فالراجح المحفوظ وما...? — le "
        "mot(s) EXACT entre المحفوظ et الشاذ), et le mot final. (2) Y a-t-il un "
        "renvoi de note en exposant? Ne complète JAMAIS de mémoire."),
    "B-p47-fahm": (
        "(1) Transcris la COLONNE DROITE (الشرح) MOT À MOT : la définition de "
        "الثقة lettre à lettre, puis la définition de المحفوظ lettre à lettre — "
        "que lit-on EXACTEMENT après « ما رواه الأوثق مخالفا » (لمن دونه من "
        "الثقات? لرواية غيره? autre?). (2) Transcris la COLONNE GAUCHE "
        "(استخلاص المضامين) : les DEUX items numérotés lettre à lettre. Ne "
        "complète JAMAIS de mémoire."),
    "C-p48-surat": (
        "(1) En haut : la phrase se termine-t-elle par « بجمع طرق الحديث » "
        "seul, ou y a-t-il un mot après (تدرى? تدرس? autre?) — lettre à lettre "
        "avec les chiffres en exposant éventuels. (2) Transcris le TABLEAU "
        "(صور زيادة الثقة) EN ENTIER : titre de chaque case, tous les textes "
        "des cases, tous les chiffres (UN PAR UN), les flèches/branches "
        "(de quoi vers quoi). Structure : combien de colonnes/lignes? Ne "
        "complète JAMAIS de mémoire."),
    "D-p49-shakl": (
        "(1) Transcris le SCHÉMA (الشكل التالي) EN ENTIER : chaque case, son "
        "texte lettre à lettre, tous les chiffres UN PAR UN, les branches et "
        "flèches (de quoi vers quoi). Combien de cases? (2) Y a-t-il une "
        "légende? Ne complète JAMAIS de mémoire."),
    "E-p49-maqayis": (
        "(1) Transcris la ligne entière de la définition لغة de حفظ jusqu'au "
        "crochet fermant, lettre à lettre. (2) Les CHIFFRES de la référence "
        "entre crochets : liste-les UN PAR UN avec le slash exactement comme "
        "imprimé (87/2? 2/78? 78/2? autre?). Ne complète JAMAIS de mémoire."),
    "F-p50-maqayis": (
        "(1) Transcris la ligne entière de la définition لغة de شذ MOT À MOT "
        "jusqu'au crochet fermant. (2) Les CHIFFRES de la référence entre "
        "crochets UN PAR UN avec le slash (180/3? 3/180? autre?) — et le mot "
        "après le crochet (بتصرف?). Ne complète JAMAIS de mémoire."),
    "G-p50-tirmidhi": (
        "(1) Transcris l'isnād MOT À MOT depuis « حدثنا » : le nom du premier "
        "rapporteur EXACTEMENT (بشر بن معاذ العقدي? العكبري? العتكي? autre? — "
        "lettre à lettre). (2) Le matn ENTRE chevrons lettre à lettre avec "
        "diacritiques (فليضطجع على يمينه?). (3) La référence entre crochets "
        "complète. Ne complète JAMAIS de mémoire."),
    "H-p50-bukhari": (
        "(1) Transcris les lignes MOT À MOT depuis « كما أخرجه البخاري » : "
        "l'isnād (حدثنا عبد الله بن يزيد... jusqu'à عن عائشة), le matn ENTRE "
        "chevrons lettre à lettre avec diacritiques (كان النبي... اضطجع على "
        "شقه الأيمن?), et la référence entre crochets complète. Ne complète "
        "JAMAIS de mémoire."),
    "M-p50-khatib": (
        "(1) Transcris le début de la citation du الخطيب البغدادي MOT À MOT : "
        "après « قال الخطيب البغدادي رحمه الله : » que lit-on EXACTEMENT (قلما "
        "يتَمَهَّر? قل ما تتمهر? autre?) puis la suite jusqu'à la fin du bloc "
        "visible, lettre à lettre avec diacritiques. Ne complète JAMAIS de "
        "mémoire."),
    "I-p51-istithmar": (
        "(1) Transcris la FIN de la citation de ابن الصلاح MOT À MOT : que "
        "lit-on après « ولم يقدح الانفراد فيه » (فهو...? — lettre à lettre), "
        "puis « وإن لم يكن ممن يوثق... » jusqu'à la fin du bloc. (2) La "
        "référence entre crochets avec les CHIFFRES UN PAR UN (مقدمة ابن "
        "الصلاح ص: 79? 97? autre?). (3) Transcris la ligne qui suit la "
        "référence si visible (de quoi parle-t-elle? lettre à lettre). Ne "
        "complète JAMAIS de mémoire."),
    "J-p51-jami": (
        "(1) Transcris la ligne MOT À MOT depuis « وانشغل » jusqu'au crochet "
        "fermant : le nom du livre entre crochets, puis les CHIFFRES UN PAR UN "
        "avec le slash exactement comme imprimé (208/2? 2/802? autre?). Ne "
        "complète JAMAIS de mémoire."),
    "K-p51-taqwim": (
        "(1) Transcris le bloc التقويم EN ENTIER : les TROIS items numérotés "
        "lettre à lettre (item 2 : أبين الفرق بين...? — que lit-on EXACTEMENT "
        "après الفرق بين? et item 3 : أستحضر مثالا للحديث...?). Ne complète "
        "JAMAIS de mémoire."),
    "L-p51-idad": (
        "(1) Transcris le bloc final EN ENTIER : le titre (الإعداد القبلي?), la "
        "phrase d'intro, et les items numérotés lettre à lettre (item 2 : "
        "الفرق بين المنكر والشاذ? — que lit-on EXACTEMENT après الفرق بين "
        "المنكر? un troisième item existe-t-il?). Ne complète JAMAIS de "
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
    if os.path.exists(out) and os.path.getsize(out) > 50:  # reprise : JSON déjà là
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

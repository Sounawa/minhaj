# -*- coding: utf-8 -*-
"""R620 — crops d'adjudication image, leçon 7 ulum-hadith-tanawi-2
(pdf-mut23h2u-261, الحديث الحسن, p.41-46 de ulum-hadith-2-thanawi_text.pdf).
Recadrages 600 dpi des zones encore ambiguës après couches (pdftotext/OCR/pymu)
+ lecture directe des pages 300 dpi : matn du siwāk, matn du vin des orphelins,
« بشواهد/بشهادة », citation du المتن p.41 (التاقل? إستادين?), réf لسان العرب,
« فذكر/ففكر », « مما قبل إيه الصحيح », « من قبيل المقبول », « له وين? »,
« أسنده عنده/عندنا », « إما للغموض/لغموضه », bloc أهتدي وأقتدي (fin),
الاستثمار p.46 (تظنن? الموقظة/الوقفة? يتفاوت?).
Sortie : tr-tmp/qa-crops-r620/<X>.png puis tr-tmp/r620/vlm-<X>.json
Usage : python3 scripts-translate/crops-uh2-r620.py [--vlm]
"""
import os, subprocess, sys, time

from PIL import Image
import fitz

HOME = "/home/z/my-project"
PDF = f"{HOME}/content/textbooks-src/ulum-hadith-2-thanawi_text.pdf"
OUT = f"{HOME}/tr-tmp/qa-crops-r620"
VLM = f"{HOME}/tr-tmp/r620"
DPI = 600

ZONES = {
    # A1 — p.41 : citation du المتن (Ibn Ḥaǧar) MOT À MOT (التاقل? إستادين?)
    "A1-p41-quote":   [(41, 0.585, 0.760, 0.04, 0.97)],
    # A2 — p.41 : boîte الفهم, deux colonnes (الشرح / استخلص المضامين)
    "A2-p41-fahm":    [(41, 0.750, 0.970, 0.03, 0.99)],
    # B1 — p.42 : définition لغة + réf [لسان العرب ...? / chiffres 13/114?]
    "B1-p42-lisan":   [(42, 0.175, 0.270, 0.04, 0.98)],
    # B2 — p.42 : القسم الثاني, ligne « غير أنه لم يبلغ درجة رجال الصحيح, ? »
    "B2-p42-qism2":   [(42, 0.720, 0.815, 0.04, 0.98)],
    # C1 — p.43 : matn du siwāk (أفشوا على أمواتكم? / لو لا أن أشق على أمتي?)
    "C1-p43-siwak":   [(43, 0.065, 0.225, 0.04, 0.98)],
    # C2 — p.43 : مثال ابن حبان + « إسناده ضعيف وهو حديث حسن بشواهد/بشهادة »
    "C2-p43-hibban":  [(43, 0.570, 0.790, 0.04, 0.98)],
    # C3 — p.43 : matn du vin des orphelins (كان عندنا خمر يتامى...) + réf
    "C3-p43-wine":    [(43, 0.810, 0.975, 0.04, 0.98)],
    # D1 — p.44 : مراتبه — « فذكر/ففكر الإمام الذهبي » + « مما قبل إيه الصحيح? »
    "D1-p44-marateb": [(44, 0.285, 0.410, 0.04, 0.98)],
    # D2 — p.44 : حكم الحديث الحسن — « من قبل/قبيل المقبول »
    "D2-p44-hukm":    [(44, 0.575, 0.760, 0.04, 0.98)],
    # D3 — p.44 : معنى قولهم حديث حسن صحيح — fin « لأن كثرة الطرق له? »
    "D3-p44-maana":   [(44, 0.750, 0.950, 0.04, 0.98)],
    # E1 — p.45 : citation آخر كتابه — « فإنما أردنا أسنده عنده/عندنا »
    "E1-p45-quote":   [(45, 0.345, 0.465, 0.04, 0.98)],
    # E2 — p.45 : « إما للغموض/لغموضه، وإما للجديد/لجديد »
    "E2-p45-ghumud":  [(45, 0.535, 0.645, 0.04, 0.98)],
    # E3 — p.45 : bloc أهتدي وأقتدي complet (fin : أمرني رسول الله ﷺ ?)
    "E3-p45-ahjadi":  [(45, 0.655, 0.890, 0.04, 0.98)],
    # F1 — p.46 : boîte الاستثمار (لا تظنن?/تظعن? + الموقظة/الوقفة? + ص 28-29?)
    "F1-p46-istithmar": [(46, 0.290, 0.540, 0.03, 0.99)],
}

BASE = ("Tu lis une image d'un manuel scolaire marocain de hadith (sciences du "
        "ḥadīṯ, 2e année secondaire, commentaire de la Nuḫbat al-fikr). Réponds "
        "UNIQUEMENT à la question posée, par transcription EXACTE du texte "
        "imprimé visible, token par token. Si tu n'es pas sûr d'un mot ou d'un "
        "chiffre, écris [illisible]. N'invente AUCUN texte, ne complète JAMAIS de "
        "mémoire (n'utilise PAS la version canonique d'un hadith que tu "
        "connaîtrais), ne corrige pas l'imprimé même s'il te paraît fautif.")

QUESTIONS = {
    "A1-p41-quote": (
        "(1) Transcris la citation du المتن MOT À MOT depuis « فإن خف الضبط » "
        "jusqu'au guillemet fermant, lettre à lettre : que lit-on EXACTEMENT après "
        "« فإن جمعا » (فلا تردد? فلتردد?) et après « في الـ » (التاقل? التقى? "
        "المقبل? autre?) et le mot final après « وإلا فبالاعتداد » (إستادين? "
        "المستورين? autre?). (2) Y a-t-il des renvois/références entre crochets "
        "sous la citation? Transcris-les. Ne complète JAMAIS de mémoire."),
    "A2-p41-fahm": (
        "(1) Transcris la COLONNE DROITE (الشرح) MOT À MOT : définition de خفّ "
        "(خفّ القوم خفوقا...), de فإن جمعا, de فلا تردد في الـ..., lettre à "
        "lettre. (2) Transcris la COLONNE GAUCHE (استخلص المضامين) MOT À MOT : "
        "toutes les lignes visibles, lettre à lettre (المستورين الكثي? الضاعة "
        "القليلة? حداصل? — transcris TEL QUE IMPRIMÉ). Ne complète JAMAIS de "
        "mémoire."),
    "B1-p42-lisan": (
        "(1) Transcris la ligne « أ - لغة : ... » MOT À MOT jusqu'au crochet "
        "fermant, lettre à lettre : le nom du livre entre crochets (لسان العرب? "
        "autre?) puis la lettre/nom après (لابن? بابن? ابن?), puis les CHIFFRES "
        "EXACTS avec le slash (13/114? 1/114? 13/441? 1/411? autre? — compte les "
        "chiffres UN PAR UN). Ne complète JAMAIS de mémoire."),
    "B2-p42-qism2": (
        "(1) Transcris les lignes visibles MOT À MOT depuis « القسم الثاني : أن "
        "يكون راويه » : après « غير أنه لم يبلغ درجة رجال الصحيح » que lit-on "
        "EXACTEMENT (لكن? لأنه? rien?), lettre à lettre. (2) Y a-t-il une "
        "référence entre crochets à la fin? Transcris-la avec les chiffres exacts. "
        "Ne complète JAMAIS de mémoire."),
    "C1-p43-siwak": (
        "(1) Transcris le matn du hadith ENTRE chevrons MOT À MOT, lettre à "
        "lettre, AVEC les diacritiques visibles : que lit-on EXACTEMENT après "
        "« قال » ? (أفشوا على أمواتكم بالسواك? لو لا أن أشق على أمتي لأمركم "
        "بالسواك? autre?) — transcris TEL QUE IMPRIMÉ même si le hadith canonique "
        "diffère. (2) Transcris la référence entre crochets. Ne complète JAMAIS "
        "de mémoire."),
    "C2-p43-hibban": (
        "(1) Transcris l'isnād du hadith d'ابن حبان MOT À MOT (أخبرنا أبو يعلى "
        "قال... jusqu'à عن ابن عباس), lettre à lettre : le rapporteur après "
        "« حدثنا جرير عن » (فطر? فتـر? autre?) et sa nisba à la fin (هو بن خليفة "
        "المخزومي?). (2) Le matn complet entre chevrons. (3) La référence entre "
        "crochets. (4) Après « إسناده ضعيف وهو حديث حسن » que lit-on EXACTEMENT : "
        "بشواهد ou بشهادة ou autre? Lettre à lettre. Ne complète JAMAIS de "
        "mémoire."),
    "C3-p43-wine": (
        "(1) Transcris l'isnād MOT À MOT (ما رواه عيسى بن يونس عن مجالد عن... — "
        "le nom du troisième rapporteur : أبي الوضاك? أبي الوداك? أبي وداع? "
        "autre?). (2) Le matn ENTRE chevrons lettre à lettre AVEC diacritiques : "
        "que lit-on après « كان عندنا خمر يتامى » exactement (لما رت الحائض? فلما "
        "هلك الحادي? autre?) et quel est le DERNIER mot du matn (أهريقوا? "
        "أهريقوه? autre?). (3) La référence entre crochets. Ne complète JAMAIS de "
        "mémoire."),
    "D1-p44-marateb": (
        "(1) Transcris le paragraphe مراتبه MOT À MOT : après « وقد ذكرنا أمثلة "
        "من تفاوت مراتب الحسن لذاته » que lit-on EXACTEMENT (فذكر الإمام الذهبي? "
        "ففكر الإمام الذهبي? autre?) lettre à lettre ; et après « وأمثال ذلك » "
        "que lit-on EXACTEMENT (مما قبل إيه الصحيح? مما قبله الصحيح? autre?) — "
        "lettre à lettre avec les diacritiques visibles. (2) La référence entre "
        "crochets avec les chiffres exacts. Ne complète JAMAIS de mémoire."),
    "D2-p44-hukm": (
        "(1) Transcris le paragraphe حكم الحديث الحسن MOT À MOT : après « الحديث "
        "الحسن بقسميه (لذاته ولغيره) » que lit-on EXACTEMENT (من قبل المقبول? من "
        "قبيل المقبول? autre?) lettre à lettre ; après « وهو مشارك للصحيح في "
        "الاحتجاج به وإن كان » (دونه? دونها? autre?) ; et le mot avant "
        "« ومشابه له » si visible. Ne complète JAMAIS de mémoire."),
    "D3-p44-maana": (
        "(1) Transcris le paragraphe MOT À MOT depuis « معنى قولهم » : après « "
        "كقول الترمذي وغيره حديث حسن صحيح » que lit-on EXACTEMENT (فتردد الحاصل? "
        "فلتردد الحاصل? فتردد?) ; après « فإن لم يحصل التفرد » (فهذا? autre?) ; "
        "et le TOUT DERNIER mot du paragraphe après « لأن كثرة الطرق » (لهوين? له "
        "وين? له وزن? لهوي? autre?) — lettre à lettre avec diacritiques. Ne "
        "complète JAMAIS de mémoire."),
    "E1-p45-quote": (
        "(1) Transcris la citation « وقالنا في كتابنا : حديث حسن ... » MOT À MOT "
        "jusqu'à « فهو عندنا حديث حسن » : après « فإنما أردنا أسنده » que lit-on "
        "EXACTEMENT (عنده? عندنا? autre?) lettre à lettre ; puis « كحديث يروى ولا "
        "يكون راويه متهما بـ » (كذب? الكذب?). Ne complète JAMAIS de mémoire."),
    "E2-p45-ghumud": (
        "(1) Transcris les lignes visibles MOT À MOT : la phrase « واقتصر على "
        "تعريف ما يقول فيه في كتابه حسن فقط ; إما لـ » — que lit-on EXACTEMENT "
        "(للغموض? لغموضه?) puis (وإما للجديد? وإما لجديد?) lettre à lettre ; et "
        "« ولذلك قيده بقوله : » (عندنا? عنده?). Ne complète JAMAIS de mémoire."),
    "E3-p45-ahjadi": (
        "(1) Transcris TOUT le bloc أهتدي وأقتدي MOT À MOT : les DEUX récits de "
        "أبي مصعب et مصعب بن عبد الله, puis après « فسئل عن ذلك فقال : أمرني "
        "رسول الله ﷺ » que lit-on EXACTEMENT, lettre à lettre, jusqu'à la "
        "référence. (2) La référence entre crochets avec les chiffres exacts "
        "(الشفا بتعريف حقوق المصطفى للقاضي عياض 2/45? — vérifie les chiffres UN "
        "PAR UN). Ne complète JAMAIS de mémoire."),
    "F1-p46-istithmar": (
        "(1) Transcris la citation de الذهبي MOT À MOT depuis « قال الإمام الذهبي "
        "رحمه الله » : le mot après « ثم لا » (تظنن? تظعن? تظن?) ; le mot après "
        "« أن للسن قاعدة تندرج كل الأحاديث الحسان فيها » ; le mot après « بل "
        "الحافظ الواحد » (يتغير? يتفاوت? يتفكر?) ; le mot final (استضعه? "
        "استضعفه?). (2) La référence entre crochets MOT À MOT avec les chiffres "
        "exacts (الموقظة? الوقفة? — ص: 28-29? — chiffres UN PAR UN). Ne complète "
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
    sys.exit(main())

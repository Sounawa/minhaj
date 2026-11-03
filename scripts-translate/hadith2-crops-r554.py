# -*- coding: utf-8 -*-
"""R554 — preuve image leçon 13 hadith-2es (slot pdf-14) : recadrages ciblés 400 dpi
+ lectures VLM token par token sur les numéros rouges du Muwaṭṭaʾ, les isnāds et
les lexies litigieuses (chiffres OCR inversés par paires — l'image tranche).
Sorties : tr-tmp/qa-crops-r554/*.png + tr-tmp/vlm-r554/*.json — reprise sûre."""
import fitz
import json
import os
import subprocess

HOME = "/home/z/my-project"
PDF = f"{HOME}/content/textbooks-src/hadith-2-iadadi_text.pdf"
CROPS = f"{HOME}/tr-tmp/qa-crops-r554"
OUT = f"{HOME}/tr-tmp/vlm-r554"

BASE = ("Tu lis une image d'un manuel scolaire marocain de hadith (Muwaṭṭaʾ Mālik / "
        "Šarḥ az-Zarqānī, 2e année collégiale). Réponds UNIQUEMENT à la question posée, "
        "par transcription EXACTE du texte imprimé visible, token par token. Si tu n'es "
        "pas sûr d'un mot ou d'un chiffre, écris [illisible]. N'invente AUCUN texte, ne "
        "complète JAMAIS de mémoire (n'utilise PAS de version canonique du hadith que tu "
        "connaîtrais), ne corrige pas l'imprimé même s'il te paraît fautif.")

os.makedirs(CROPS, exist_ok=True)
os.makedirs(OUT, exist_ok=True)
doc = fitz.open(PDF)


def crop(page_no, x0f, y0f, x1f, y1f, dpi, name):
    path = f"{CROPS}/{name}.png"
    if os.path.exists(path):
        print("•", name, "déjà croppé")
        return
    pg = doc[page_no - 1]
    r = pg.rect
    clip = fitz.Rect(r.width * x0f, r.height * y0f, r.width * x1f, r.height * y1f)
    pix = pg.get_pixmap(matrix=fitz.Matrix(dpi / 72, dpi / 72), clip=clip)
    pix.save(path)
    print(f"{name}: {pix.width}x{pix.height}")


CROPS_LIST = [
    # page, x0, y0, x1, y1, dpi, nom
    (91, 0.04, 0.14, 0.96, 0.52, 400, "p91-tamhid"),
    (91, 0.04, 0.48, 0.96, 1.00, 400, "p91-isnad"),
    (92, 0.04, 0.00, 0.96, 0.26, 400, "p92-matn1"),
    (92, 0.04, 0.24, 0.96, 0.54, 400, "p92-shroud"),
    (92, 0.04, 0.50, 0.96, 0.74, 400, "p92-ibnumar"),
    (92, 0.04, 0.70, 0.96, 1.00, 400, "p92-warith"),
    (93, 0.04, 0.00, 0.96, 0.22, 400, "p93-tahlil"),
    (94, 0.04, 0.00, 0.96, 0.30, 400, "p94-matn2"),
    (94, 0.04, 0.28, 0.96, 0.76, 400, "p94-asm"),
    (94, 0.04, 0.72, 0.96, 1.00, 400, "p94-note"),
    (95, 0.04, 0.00, 0.96, 0.38, 400, "p95-tamrat"),
    (95, 0.04, 0.34, 0.96, 1.00, 400, "p95-takfin"),
    (96, 0.04, 0.00, 0.96, 0.42, 400, "p96-hukm"),
    (96, 0.04, 0.40, 0.96, 1.00, 400, "p96-dua"),
    (97, 0.04, 0.00, 0.96, 0.42, 400, "p97-taqwim"),
    (97, 0.04, 0.38, 0.96, 0.85, 400, "p97-iedad"),
]

ASKS = {
    "p91-tamhid": (
        "(1) Transcris MOT À MOT la citation coranique imprimée entre chevrons dans ce "
        "bloc (elle commence probablement par ومن — ne la complète pas de mémoire). "
        "(2) Le renvoi entre crochets [الآية: سورة ...] : transcris le nom de la sourate "
        "imprimé et le numéro d'āya CHIFFRE PAR CHIFFRE (chiffres arabes orientaux, "
        "écris chaque chiffre séparément). (3) Transcris la phrase qui suit le renvoi "
        "(elle contient ويقتصر هذا التكريم...) et les 2 phrases suivantes (فقط ... ومن "
        "مظاهر التكريم بعد الموت ...) jusqu'à la question فما أحكام..., exactement "
        "comme imprimé. (4) Y a-t-il UNE ou DEUX citations coraniques dans ce bloc ?"),
    "p91-isnad": (
        "(1) Le titre du bloc en bas de page (en bleu, mot à mot — الأحاديات ? الأحاديث ?). "
        "(2) L'isnād imprimé : مالك عن [?] عن [?] عن [?] الأنصارية — transcris chaque nom "
        "exactement lettre à lettre (notamment le premier et le deuxième). "
        "(3) Transcris la phrase قالت : ... telle qu'imprimée jusqu'à la fin de la page."),
    "p92-matn1": (
        "(1) Transcris le PREMIER MOT de la page. (2) Transcris MOT À MOT le texte entre "
        "chevrons en haut de page (فإذا تفرّغت...) jusqu'à la fin de la citation, sans le "
        "compléter de mémoire. (3) Transcris la glose entre chevrons qui suit (أشعرنها "
        "إياه ?) et le renvoi ROUGE entre crochets [الموطأ رقم: ...] CHIFFRE PAR CHIFFRE "
        "(chiffres arabes orientaux, chaque chiffre séparément)."),
    "p92-shroud": (
        "(1) L'isnād : مالك عن [?] بن [?] عن أبيه عن [?] — transcris chaque nom exactement. "
        "(2) Transcris MOT À MAT le matn entre chevrons (il commence par أنّ رسول الله... "
        "كُفِّن...) et sa fin exacte (ليس فيهما قميص...). (3) Le renvoi ROUGE [الموطأ "
        "رقم: ...] CHIFFRE PAR CHIFFRE."),
    "p92-ibnumar": (
        "(1) Transcris MOT À MOT la (ou les) citation(s) de ce bloc avec leurs renvois "
        "ROUGES entre crochets CHIFFRE PAR CHIFFRE (il peut y en avoir deux — pour chaque "
        "renvoi écris chaque chiffre séparément). (2) Les isnāds imprimés : مالك عن [?] "
        "عن [?] — transcris-les exactement."),
    "p92-warith": (
        "(1) Le titre du bloc en bas de page (mot à mot). (2) Transcris EXACTEMENT les "
        "phrases suivantes avec tous les noms propres lettre à lettre : أمّ عطية الأنصارية "
        "هي [?] بنت [?]... وقيل: [?]... ; صاحباتها اللواتي غسلن بنت النبي ﷺ كلّهن حُدِّث "
        "عنهن [?] وأخواتها [?] وأم [?] و[?] بن [?] و[?] وإسماعيل بن عبد الرحمن [?] ; "
        "عاشت إلى [?] حجة ; et la PHRASE FINALE complète de la page (وُلدت في... فأذّنت... "
        "?) telle qu'imprimée."),
    "p93-tahlil": (
        "Transcris le bloc d'en-tête de cette page (titre bleu + les items 1- et 2- avec "
        "leurs tirets) tel qu'imprimé, mot à mot."),
    "p94-matn2": (
        "(1) Transcris la phrase sur la deuxième غسلة (فيضع في الماء...) et la phrase sur "
        "la troisième غسلة, mot à mot, exactement comme imprimé. (2) Transcris la citation "
        "de أمّ عطية entre chevrons (أنِّي؟ بمائها؟...) mot à mot, et la fin de la phrase "
        "qui suit (لقول النبي ﷺ... ?) telle qu'imprimée."),
    "p94-asm": (
        "(1) Transcris le titre de la section (3- ...). (2) Transcris MOT À MOT la "
        "citation d'après مالك أنّه بلغه? : أنّ [?] بنت [?] زوج? [?]... — depuis le début "
        "de la citation jusqu'à sa fin exacte, sans compléter (notamment le verbe après "
        "زوج أبي بكر الصديق : توفيّت? عسلت? حسلت? — transcris-le lettre à lettre, et la "
        "suite : حين... غسّلها [?]...). (3) Le renvoi ROUGE entre crochets CHIFFRE PAR "
        "CHIFFRE."),
    "p94-note": (
        "(1) Transcris MOT À MOT la phrase qui commence par لأنّ عليّ بن أبي طالب... "
        "(2) Le renvoi entre crochets [معرفة السنة...] — transcris-le exactement. "
        "(3) Y a-t-il une autre citation sur cette portion ? Si oui transcris-la."),
    "p95-tamrat": (
        "(1) Transcris les phrases إذا كان الزوجان?/فإن لم يكن أحد الزوجين... telles "
        "qu'imprimées, mot à mot. (2) Transcris MOT À MOT la citation entre chevrons "
        "(كانوا يقولون : ألو? تمت المرأة...) jusqu'à sa fin exacte (تمتم بوجهها وكيفها "
        "من الصعيد?) et le renvoi ROUGE CHIFFRE PAR CHIFFRE. (3) L'isnād de cette "
        "citation : مالك عن [?] بن [?] — transcris-le exactement."),
    "p95-takfin": (
        "(1) Transcris la phrase sur le كفن (أن يكون الكفن أبيض س...؟ جديدًا؟ وقديمًا؟ في "
        "ثلاثة أثواب أو خمسة... زيادة في الستر...) mot à mot. (2) Transcris MOT À MOT la "
        "citation والتمبح? عند الإمام? يقصّ?... avec son isnād (عن [?] بن [?] عن [?] عن "
        "[?]) et le renvoi ROUGE CHIFFRE PAR CHIFFRE, sans la compléter de mémoire."),
    "p96-hukm": (
        "(1) Transcris MOT À MOT la phrase sur صلاة الجنازة فرض كفاية... telle qu'imprimée "
        "jusqu'à la fin de la phrase. (2) Transcris la citation entre chevrons du milieu "
        "de la page (الجنازة السابقة? / خفضوا? بها?...) mot à mot, son renvoi entre "
        "crochets (سنن أبي داود? [رقم?]) CHIFFRE PAR CHIFFRE, et la phrase qui la suit "
        "(يذيلها؟ للقول?...)."),
    "p96-dua": (
        "(1) L'isnād de la grande citation : عن [?] بن [?] [?] عن [?] — transcris chaque "
        "nom lettre à lettre (le mot après سعيد بن سعيد : بن أبي سعيد? بن العاص?... et le "
        "dernier nom avant عن أبي هريرة). (2) Transcris le matn MOT À MOT depuis أمّا أبو "
        "هريرة? كذا? صلّى?... JUSQU'À LA FIN de la citation (لا تفَتّوه? بعده?), sans la "
        "compléter de mémoire. (3) Le renvoi ROUGE CHIFFRE PAR CHIFFRE. (4) La phrase "
        "imprimée juste après le renvoi (تتكبر؟... تكبيرات؟...)."),
    "p97-taqwim": (
        "(1) Transcris le bloc التقويم (titre + items 1- 2- 3-). (2) Le bloc الاستثمار : "
        "transcris les DEUX citations mot à mot avec leurs renvois ROUGES CHIFFRE PAR "
        "CHIFFRE. Notamment dans la première citation : le mot imprimé entre على الجنازة "
        "بعد et وبعد الصبح (القدر? العصر? الجمعة? — transcris-le lettre à lettre), et le "
        "renvoi de la deuxième citation ([الموطأ رقم ...] — في المسجد?)."),
    "p97-iedad": (
        "(1) Transcris l'item ١- أشرح: suivi des lexies EXACTEMENT (chaque lexie, y "
        "compris le premier mot — أرْجني? ألجني? أرجئني?... et بعد...). (2) Transcris les "
        "items 2- et 3- exactement comme imprimés."),
}

for p, x0, y0, x1, y1, dpi, name in CROPS_LIST:
    crop(p, x0, y0, x1, y1, dpi, name)

for name, _p, _x, _y, _x1, _y1, _dpi in [(c[6],) + tuple(c[:6]) for c in []]:
    pass

for name, q in ASKS.items():
    out = f"{OUT}/{name}.json"
    if os.path.exists(out):
        print("•", name, "déjà lu")
        continue
    img = f"{CROPS}/{name}.png"
    if not os.path.exists(img):
        print("✗", name, "crop manquant")
        continue
    cmd = ["z-ai", "vision", "-p", f"{BASE}\nQUESTION : {q}", "-i", img, "-o", out]
    r = subprocess.run(cmd, capture_output=True, text=True, timeout=300)
    print(("✓" if r.returncode == 0 else "✗"), name, (r.stderr or "").strip()[:120])

print("\n===== RÉSULTATS =====")
for name, q in ASKS.items():
    try:
        d = json.load(open(f"{OUT}/{name}.json", encoding="utf-8"))
        print(f"\n----- {name} -----")
        print(d["choices"][0]["message"]["content"][:1500])
    except Exception as e:
        print(f"\n----- {name} ----- ERREUR {e}")

# -*- coding: utf-8 -*-
"""R554 — preuve image leçon 13 hadith-2es (slot pdf-14), 2ᵉ passe : points
litigieux restants, recadrages serrés 800-1000 dpi + relance API avec dosage.
Sorties : tr-tmp/qa-crops-r554/*.png + tr-tmp/vlm-r554/*.json — reprise sûre."""
import fitz
import json
import os
import subprocess
import time

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
    (91, 0.04, 0.28, 0.96, 0.68, 500, "b-p91-renvoi"),
    (91, 0.04, 0.52, 0.96, 1.00, 500, "b-p91-matnstart"),
    (92, 0.04, 0.00, 0.96, 0.30, 500, "b-p92-matn1"),
    (92, 0.04, 0.36, 0.96, 0.62, 500, "b-p92-ibnumar"),
    (92, 0.04, 0.56, 0.96, 0.80, 500, "b-p92-warith"),
    (92, 0.04, 0.72, 0.96, 1.00, 500, "b-p92-gloss"),
    (93, 0.04, 0.00, 0.96, 0.14, 800, "b-p93-glosstail"),
    (94, 0.04, 0.38, 0.96, 0.74, 500, "b-p94-asm-quote"),
    (94, 0.04, 0.70, 0.96, 0.86, 800, "b-p94-bihraqi"),
    (95, 0.04, 0.00, 0.96, 0.40, 500, "b-p95-tayammum"),
    (96, 0.04, 0.00, 0.96, 0.44, 500, "b-p96-hukm"),
    (96, 0.04, 0.40, 0.96, 1.00, 500, "b-p96-dua"),
    (97, 0.04, 0.00, 0.96, 0.46, 500, "b-p97-taqwim"),
    (97, 0.04, 0.40, 0.96, 0.88, 500, "b-p97-iedad"),
]

ASKS = {
    "b-p91-renvoi": (
        "(1) Transcris la citation coranique entre chevrons (commence par ولقد كرمنا "
        "بني آدم?) — la phrase EXACTE complète telle qu'imprimée, jusqu'à sa fin. "
        "(2) Le renvoi entre crochets [الآية: سورة ...] : nom de la sourate + numéro "
        "CHIFFRE PAR CHIFFRE (chiffres arabes orientaux). (3) Transcris la phrase qui "
        "suit (ويقتصر هذا التكريم...) exactement, puis la phrase suivante (ومن مظاهر "
        "التكريم...) exactement, puis la question qui suit."),
    "b-p91-matnstart": (
        "(1) Transcris l'isnād LETTRE À LETTRE : مالك عن [?] عن محمد بن سيرين عن أمّ "
        "عطية — le PREMIER nom exactement (أبو زرعة? أبو تميمة? أيوب بن أبي تميمة? — "
        "chaque lettre compte). (2) Transcris la phrase قالت : ... telle qu'imprimée "
        "jusqu'à la fin de la page visible."),
    "b-p92-matn1": (
        "(1) Transcris MOT À MOT tout le texte arabe visible en haut de page : le matn "
        "entre chevrons (ثلاثًا؟ فإذا...), puis la glose (الشرح) avec sa définition "
        "complète (فإذني?... أشعرنها إياه?...), telle qu'imprimée. (2) Le renvoi rouge "
        "[الموطأ رقم: ...] CHIFFRE PAR CHIFFRE."),
    "b-p92-ibnumar": (
        "Transcris MOT À MOT tout ce qui est imprimé dans cette bande : les citations "
        "entre chevrons avec leurs isnāds (مالك عن...) et les renvois rouges [الموطأ "
        "رقم: ...] CHIFFRE PAR CHIFFRE — il peut y avoir DEUX citations et DEUX renvois. "
        "Ne complète rien de mémoire."),
    "b-p92-warith": (
        "(1) Le titre du bloc imprimé dans cette bande (mot à mot). (2) Transcris "
        "EXACTEMENT les phrases du bloc avec tous les noms propres lettre à lettre : "
        "أمّ عطية الأنصارية هي [?] بنت [?]... وقيل: [?]... ; صاحباتها اللواتي... كلّهن "
        "حُدِّث عنهن [?] وأخواتها [?] وأمّ [?] و[?] بن [?] و[?] وإسماعيل بن عبد الرحمن "
        "[?] ; عاشت إلى [?]... ; la phrase finale complète (الفَخِخ? فأذّنت?...) telle "
        "qu'imprimée, sans la compléter."),
    "b-p92-gloss": (
        "Transcris MOT À MOT les définitions de la glose (الشرح) visibles : la définition "
        "de فإذني? / فأذني? et celle de أشعرنها إياه? — chaque définition complète comme "
        "imprimée, y compris les mots النوب? نبرك? إزار? حقوق? s'ils apparaissent."),
    "b-p93-glosstail": (
        "Transcris MOT À MOT la définition visible en haut (le mot-titre : سُخْبَة? "
        "سُحُولِيَّة? — transcris-le exactement, puis sa définition : نسبة إلى... قرية "
        "باليمن... وقال الأزهرُ?...)."),
    "b-p94-asm-quote": (
        "(1) Transcris la phrase d'introduction (أنّ امرأة?...) exactement. (2) Transcris "
        "MOT À MOT la citation entre chevrons (أنّ أسماء بنت عميس...) depuis son début "
        "jusqu'à sa fin, lettre à lettre — notamment le mot entre بنت عميس et أبي بكر؟ "
        "(زوج? زوجة? مرة? توفيّت?) et le verbe après الصديق (غسّلت? غسّلها? — QUI lave "
        "QUI exactement comme imprimé). (3) Le renvoi rouge CHIFFRE PAR CHIFFRE."),
    "b-p94-bihraqi": (
        "(1) Transcris la phrase ولمّا ماتت فاطمة... exactement. (2) Le renvoi entre "
        "crochets : la DERNIÈRE LETTRE du nom — البيهقي ou الديهقي ? (regarde les points "
        "sous la lettre après ال). Transcris le renvoi complet."),
    "b-p95-tayammum": (
        "(1) Transcris les phrases doctrinales (فإذا لم يوجد... تيمّمه امرأة أجنبية?... "
        "وكذلك المرأة...) exactement comme imprimées. (2) L'isnād du hadith (لما في "
        "الموطأ عن مالك? عن [?]...) — transcris-le lettre à lettre. (3) Transcris MOT À "
        "MOT la citation entre chevrons (إذا ماتت المرأة...) avec son renvoi rouge "
        "CHIFFRE PAR CHIFFRE."),
    "b-p96-hukm": (
        "(1) Transcris la phrase sur صلاة الجنازة (فرض كفاية...) exactement, mot à mot. "
        "(2) Transcris la citation entre chevrons du milieu (الجنازة? السابقة? خفّضوا?... "
        "?) avec son renvoi entre crochets CHIFFRE PAR CHIFFRE. (3) Transcris la phrase "
        "suivant la citation (يذيلها? للقول?...)."),
    "b-p96-dua": (
        "(1) L'isnād de la grande citation : عن [?] بن [?] [?] عن [?] — chaque nom lettre "
        "à lettre (le mot après سعيد بن سعيد : بن أبي سعيد? بن العاص?... et le mot avant "
        "عن أبي هريرة). (2) Transcris le matn MOT À MOT depuis أمّا أبو هريرة? كذا?... "
        "JUSQU'À SA FIN (لا تفَتّوه? بعده?), sans compléter. (3) Le renvoi rouge CHIFFRE "
        "PAR CHIFFRE. (4) La phrase imprimée après le renvoi (تكبيرات?...)."),
    "b-p97-taqwim": (
        "(1) Transcris le bloc التقويم (titre + items 1- 2- 3- exactement). (2) Le bloc "
        "الاستثمار : transcris les DEUX citations mot à mot avec leurs renvois rouges "
        "CHIFFRE PAR CHIFFRE. Dans la première citation, transcris LETTRE À LETTRE le mot "
        "imprimé entre على الجنازة بعد et وبعد الصبح (القدر? العصر? الجمعة?)."),
    "b-p97-iedad": (
        "(1) Transcris l'item ١- أشرح: suivi des lexies EXACTEMENT comme imprimées (le "
        "premier mot : أرْجني? ألجني? أرجئني?... — lettre à lettre, puis chaque lexie). "
        "(2) Transcris les items 2- et 3- exactement."),
}


def read_one(name, q, img, out):
    cmd = ["z-ai", "vision", "-p", f"{BASE}\nQUESTION : {q}", "-i", img, "-o", out]
    for attempt in range(4):
        r = subprocess.run(cmd, capture_output=True, text=True, timeout=300)
        if r.returncode == 0:
            return True
        err = (r.stderr or "").strip()[:100]
        print(f"  ↻ {name} tentative {attempt + 1} échec : {err}")
        time.sleep(20 + attempt * 20)
    return False


for p, x0, y0, x1, y1, dpi, name in CROPS_LIST:
    crop(p, x0, y0, x1, y1, dpi, name)

for name, q in ASKS.items():
    out = f"{OUT}/{name}.json"
    if os.path.exists(out):
        print("•", name, "déjà lu")
        continue
    img = f"{CROPS}/{name}.png"
    ok = read_one(name, q, img, out)
    print(("✓" if ok else "✗"), name)
    time.sleep(10)

print("\n===== RÉSULTATS =====")
for name, q in ASKS.items():
    try:
        d = json.load(open(f"{OUT}/{name}.json", encoding="utf-8"))
        print(f"\n----- {name} -----")
        print(d["choices"][0]["message"]["content"][:1600])
    except Exception as e:
        print(f"\n----- {name} ----- ERREUR {e}")

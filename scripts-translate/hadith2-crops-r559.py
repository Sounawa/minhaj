# -*- coding: utf-8 -*-
"""R559 — preuve image leçon 11 hadith-2es (slot pdf-12, p.79-85, borne p.86) :
bandes 400-450 dpi + lectures VLM token par token (références rouges [الموطأ رقم
N] chiffre par chiffre — chiffres OCR inversés par paires, l'image tranche ;
blocs ornés coraniques ; isnāds lettre à lettre ; duʿāʾ complets).
Sorties : tr-tmp/qa-crops-r559/*.png + tr-tmp/vlm-r559/*.json — reprise sûre."""
import fitz
import json
import os
import subprocess
import time

HOME = "/home/z/my-project"
PDF = f"{HOME}/content/textbooks-src/hadith-2-iadadi_text.pdf"
CROPS = f"{HOME}/tr-tmp/qa-crops-r559"
OUT = f"{HOME}/tr-tmp/vlm-r559"

BASE = ("Tu lis une image d'un manuel scolaire marocain de hadith (Muwaṭṭaʾ Mālik / "
        "Šarḥ az-Zarqānī, 2e année collégiale — leçon فضل الذكر والدعاء). Réponds "
        "UNIQUEMENT à la question posée, par transcription EXACTE du texte imprimé "
        "visible, token par token. Si tu n'es pas sûr d'un mot ou d'un chiffre, écris "
        "[illisible]. N'invente AUCUN texte, ne complète JAMAIS de mémoire (n'utilise "
        "PAS la version canonique d'un hadith ou d'une āya que tu connaîtrais), ne "
        "corrige pas l'imprimé même s'il te paraît fautif.")

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
    (79, 0.04, 0.00, 0.96, 0.32, 400, "p79-objectifs"),
    (79, 0.04, 0.28, 0.96, 0.64, 400, "p79-tamhid-aya"),
    (79, 0.04, 0.60, 0.96, 1.00, 450, "p79-hadith1"),
    (80, 0.04, 0.00, 0.96, 0.30, 450, "p80-hadith1-fin"),
    (80, 0.04, 0.26, 0.96, 0.60, 450, "p80-hadith2"),
    (80, 0.04, 0.56, 0.96, 0.82, 400, "p80-tarjama"),
    (80, 0.04, 0.78, 0.96, 1.00, 400, "p80-sharh"),
    (81, 0.04, 0.00, 0.96, 0.40, 450, "p81-tahlil-1"),
    (81, 0.04, 0.36, 0.96, 0.76, 450, "p81-aya-fatwa"),
    (81, 0.04, 0.72, 0.96, 1.00, 450, "p81-suite"),
    (82, 0.04, 0.00, 0.96, 0.36, 450, "p82-top"),
    (82, 0.04, 0.32, 0.96, 0.62, 450, "p82-malika"),
    (82, 0.04, 0.58, 0.96, 1.00, 450, "p82-hifz"),
    (83, 0.04, 0.00, 0.96, 0.46, 450, "p83-awqat"),
    (83, 0.04, 0.42, 0.96, 0.64, 450, "p83-thaniya"),
    (83, 0.04, 0.60, 0.96, 0.82, 450, "p83-dua1"),
    (83, 0.04, 0.78, 0.96, 1.00, 450, "p83-dua2-3"),
    (84, 0.04, 0.00, 0.96, 0.22, 450, "p84-dua3-fin"),
    (84, 0.04, 0.18, 0.96, 0.40, 450, "p84-tamata"),
    (84, 0.04, 0.36, 0.96, 0.58, 450, "p84-thulth"),
    (84, 0.04, 0.54, 0.96, 0.74, 450, "p84-bid"),
    (84, 0.04, 0.70, 0.96, 1.00, 450, "p84-iftitah"),
    (85, 0.04, 0.00, 0.96, 0.36, 450, "p85-istidlal-1"),
    (85, 0.04, 0.32, 0.96, 0.62, 450, "p85-hadith"),
    (85, 0.04, 0.58, 0.96, 1.00, 450, "p85-taqwim"),
    (86, 0.04, 0.00, 0.96, 0.20, 400, "p86-borne"),
]

ASKS = {
    "p79-objectifs": (
        "(1) Transcris le titre du bloc d'objectifs (أهداف الدرس ?) et les TROIS items "
        "1- 2- 3- mot à mot, exactement comme imprimés."),
    "p79-tamhid-aya": (
        "(1) Transcris MOT À MOT la phrase d'introduction sous le titre (تتمثل فضيلة "
        "الذكر... ?) telle qu'imprimée. (2) Transcris la citation coranique imprimée "
        "dans le bloc orné MOT À MOT (ne la complète pas de mémoire). (3) Le renvoi "
        "entre crochets [الآية : سورة البقرة ...] : transcris le numéro d'āya CHIFFRE "
        "PAR CHIFFRE (chiffres arabes orientaux, chaque chiffre séparément). (4) "
        "Transcris la phrase qui suit le bloc orné jusqu'à la fin de la portion "
        "visible."),
    "p79-hadith1": (
        "(1) Le titre du bloc en bleu (mot à mot). (2) Le numéro de hadith imprimé "
        "(chiffre par chiffre). (3) L'isnād : عن [?] — transcris chaque nom exactement. "
        "(4) Transcris MOT À MOT le matn entre chevrons depuis «من قال...» jusqu'à la "
        "fin de la portion visible, sans le compléter de mémoire."),
    "p80-hadith1-fin": (
        "(1) Transcris la fin du matn entre chevrons (وكتبت له... حتى يمسي...) mot à "
        "mot telle qu'imprimée, y compris les nombres (مائة ? مائتين ? — chiffre par "
        "chiffre). (2) La phrase finale après le chevron (ولم يأتِ أحد...) mot à mot. "
        "(3) Le renvoi ROUGE entre crochets : transcris la source et le numéro CHIFFRE "
        "PAR CHIFFRE (chaque chiffre séparément). (4) Y a-t-il un DEUXIÈME renvoi dans "
        "cette bande ? Si oui transcris-le."),
    "p80-hadith2": (
        "(1) L'isnād : مالك عن [?] عن [?] وعن [?] — transcris chaque nom exactement "
        "lettre à lettre. (2) Transcris MOT À MOT le matn entre chevrons (il commence "
        "probablement par يُنِي... ou تعالى...) jusqu'à sa fin exacte, sans le "
        "compléter de mémoire. (3) Le renvoi ROUGE entre crochets [الموطأ رقم ...] "
        "CHIFFRE PAR CHIFFRE."),
    "p80-tarjama": (
        "Transcris MOT À MOT le bloc ترجمة الراوي (titre + tous les noms propres lettre "
        "à lettre + le nombre de hadiths CHIFFRE PAR CHIFFRE + l'année de décès CHIFFRE "
        "PAR CHIFFRE), exactement comme imprimé."),
    "p80-sharh": (
        "(1) Le titre du bloc (mot à mot). (2) Transcris les items de gloss avec les "
        "expressions entre chevrons exactement comme imprimées (عشر رقاب ? حِرز من "
        "الشيطان ? — notamment la SOURCE de la quatrième gloss si elle est imprimée)."),
    "p81-tahlil-1": (
        "(1) Le titre du bloc (mot à mot). (2) Transcris la phrase d'intro du "
        "premier point (يخبرنا الدرس بأحاديث...) mot à mot. (3) L'item 1- (mot à mot) "
        "puis le hadith : isnād exact, matn entre chevrons MOT À MOT (les nombres "
        "مائة/عشر chiffre par chiffre), et le renvoi ROUGE entre crochets CHIFFRE PAR "
        "CHIFFRE."),
    "p81-aya-fatwa": (
        "(1) L'item 2- mot à mot. (2) Transcris la citation coranique du bloc MOT À "
        "MOT (ne la complète pas de mémoire) et son renvoi entre crochets : nom de "
        "sourate + numéro CHIFFRE PAR CHIFFRE. (3) Transcris la QUESTION imprimée qui "
        "suit (أهل الكتاب... ?) mot à mot, puis la réponse/phrase suivante et la "
        "citation coranique الأعراف (واذكر ربك...) avec son renvoi CHIFFRE PAR "
        "CHIFFRE."),
    "p81-suite": (
        "(1) Transcris la fin de la portion : le mot entre قاله? et le renvoi ROUGE. "
        "(2) Le renvoi ROUGE entre crochets [الموطأ رقم ...] CHIFFRE PAR CHIFFRE."),
    "p82-top": (
        "(1) Transcris la phrase incomplète en haut de page (أهل الكتاب... ?) et sa "
        "suite jusqu'au renvoi, mot à mot. (2) Le renvoi ROUGE CHIFFRE PAR CHIFFRE. "
        "(3) Transcris la phrase qui suit le renvoi."),
    "p82-malika": (
        "(1) L'item 3- (mot à mot). (2) L'isnād du hadith : عن [?] بن [?] عن [?] — "
        "chaque nom exactement. (3) Le matn entre chevrons MOT À MOT + le renvoi ROUGE "
        "CHIFFRE PAR CHIFFRE. (4) La phrase qui suit le renvoi (أي ? فإذا...) mot à "
        "mot."),
    "p82-hifz": (
        "(1) L'item 4- (mot à mot). (2) Le matn entre chevrons MOT À MOT (من قال لا "
        "إله...) avec ses nombres chiffre par chiffre. (3) Transcris les lignes "
        "dégendées/imprimées APRÈS le chevron jusqu'à la conclusion (أنّ الذكر... "
        "يحترس من الشيطان ?) et le renvoi ROUGE CHIFFRE PAR CHIFFRE."),
    "p83-awqat": (
        "(1) Le titre ثانيا (mot à mot). (2) L'item 1- mot à mot. (3) L'isnād du "
        "hadith : عن [?] عن [?] عن [?] عن [?] — chaque nom exactement lettre à lettre. "
        "(4) Le matn entre chevrons MOT À MOT (ثلاثا وتثليثا... ?) + le renvoi ROUGE "
        "CHIFFRE PAR CHIFFRE."),
    "p83-thaniya": (
        "(1) L'item 2- mot à mot. (2) L'isnād exact. (3) Le matn entre chevrons MOT À "
        "MOT + le renvoi ROUGE CHIFFRE PAR CHIFFRE."),
    "p83-dua1": (
        "(1) Le titre du bloc (mot à mot). (2) La phrase d'intro (من أعظم الأعمال... "
        "?) exacte. (3) Transcris la phrase غير أن بعض الأدعية... + l'exemple أ- : "
        "l'isnād exact (عن [?] عن مالك عن [?] عن [?]) et le duʿāʾ MOT À MOT (اللهم "
        "فاكه إقبالا?...) + le renvoi ROUGE CHIFFRE PAR CHIFFRE."),
    "p83-dua2-3": (
        "(1) L'exemple ب- : l'isnād exact (عن [?] بن [?] عن مالك عن [?] عن [?]) et le "
        "duʿāʾ MOT À MOT + renvoi ROUGE CHIFFRE PAR CHIFFRE. (2) Le début de l'exemple "
        "ج- si visible : titre + isnād."),
    "p84-dua3-fin": (
        "(1) Le duʿāʾ ج- : isnād exact (عن [?] عن [?] عن [?] عن رسول الله ﷺ) puis le "
        "matn MOT À MOT (أعوذ بك من عذاب جهنم...) JUSQU'À SA FIN EXACTE + le renvoi "
        "ROUGE CHIFFRE PAR CHIFFRE. (2) Ne complète rien de mémoire."),
    "p84-tamata": (
        "Transcris le titre du bloc (التمهيد ?) et son texte MOT À MOT."),
    "p84-thulth": (
        "(1) L'exemple أ- mot à mot. (2) L'isnād exact. (3) Le matn MOT À MOT + renvoi "
        "ROUGE CHIFFRE PAR CHIFFRE."),
    "p84-bid": (
        "(1) L'exemple ب- mot à mot. (2) L'isnād exact. (3) Le matn entre chevrons MOT "
        "À MOT (كنت عند رسول الله ﷺ...) jusqu'à sa fin exacte + le renvoi ROUGE "
        "CHIFFRE PAR CHIFFRE."),
    "p84-iftitah": (
        "(1) L'exemple ج- mot à mot : isnād exact (عن [?] بن [?]...) et le GRAND duʿāʾ "
        "MOT À MOT depuis اللهم... jusqu'à sa fin exacte, sans rien compléter de "
        "mémoire. (2) Le renvoi ROUGE CHIFFRE PAR CHIFFRE. (3) Si le bloc التقويم est "
        "visible en bas, transcris son titre et ses items."),
    "p85-istidlal-1": (
        "(1) Le titre du bloc (mot à mot). (2) La première citation coranique MOT À "
        "MOT + renvoi CHIFFRE PAR CHIFFRE. (3) La DEUXIÈME citation coranique du bloc "
        "orné MOT À MOT (même si elle est en calligraphie ornée) + son renvoi : nom de "
        "sourate + numéro CHIFFRE PAR CHIFFRE."),
    "p85-hadith": (
        "(1) Transcris MOT À MOT le hadith (ما من داع...) avec son isnād exact et le "
        "renvoi ROUGE entre crochets CHIFFRE PAR CHIFFRE. (2) Transcris la phrase qui "
        "suit (وما من شيء... ?) mot à mot."),
    "p85-taqwim": (
        "(1) Transcris le bloc التقويم (titre + items) mot à mot. (2) Le bloc أعداد "
        "القبلي : titre + items mot à mot. (3) Le bloc أحفظ : titre + texte. (4) Les "
        "items 1- اشرح: ... et 2- أبين... exactement comme imprimés."),
    "p86-borne": (
        "Quel est le titre en tête de cette page ? Transcris-le mot à mot (c'est "
        "l'en-tête d'objectifs d'une nouvelle leçon ?)."),
}

for p, x0, y0, x1, y1, dpi, name in CROPS_LIST:
    crop(p, x0, y0, x1, y1, dpi, name)

def read_one(job):
    name, q = job
    img = f"{CROPS}/{name}.png"
    if not os.path.exists(img):
        print("✗", name, "crop manquant", flush=True)
        return
    cmd = ["z-ai", "vision", "-p", f"{BASE}\nQUESTION : {q}", "-i", img, "-o", f"{OUT}/{name}.json"]
    for attempt in range(4):
        try:
            r = subprocess.run(cmd, capture_output=True, text=True, timeout=240)
            if r.returncode == 0:
                print("✓", name, f"(essai {attempt + 1})", flush=True)
                return
            print(f"✗ {name} essai {attempt + 1} :", (r.stderr or "").strip()[:100], flush=True)
        except subprocess.TimeoutExpired:
            print("⏱", name, f"timeout essai {attempt + 1}", flush=True)
        time.sleep(8 * (attempt + 1))
    print("✗✗", name, "ABANDON 4 essais", flush=True)


JOBS = [(n, q) for n, q in ASKS.items() if not os.path.exists(f"{OUT}/{n}.json")]

for job in JOBS:
    read_one(job)
print("LECTURES TERMINÉES", flush=True)

print("\n===== RÉSULTATS =====")
for name, q in ASKS.items():
    try:
        d = json.load(open(f"{OUT}/{name}.json", encoding="utf-8"))
        print(f"\n----- {name} -----")
        print(d["choices"][0]["message"]["content"][:1500])
    except Exception as e:
        print(f"\n----- {name} ----- ERREUR {e}")

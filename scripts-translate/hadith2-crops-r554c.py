# -*- coding: utf-8 -*-
"""R554 — preuve image leçon 13 hadith-2es (slot pdf-14), 3ᵉ passe : recadrages
ultra-serrés 1000 dpi sur les lexies et numéros restants (lettre à lettre).
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
    (91, 0.04, 0.50, 0.96, 0.68, 1000, "c-p91-isnadline"),
    (92, 0.04, 0.00, 0.96, 0.30, 800, "c-p92-matnlines"),
    (92, 0.04, 0.34, 0.96, 0.46, 1000, "c-p92-num614"),
    (92, 0.04, 0.42, 0.96, 0.58, 1000, "c-p92-num620"),
    (92, 0.04, 0.56, 0.96, 0.76, 800, "c-p92-names"),
    (94, 0.04, 0.40, 0.96, 0.78, 800, "c-p94-middle"),
    (95, 0.04, 0.18, 0.96, 0.38, 1000, "c-p95-isnad597"),
    (95, 0.04, 0.80, 0.96, 1.00, 800, "c-p95-fardkifaya"),
    (96, 0.04, 0.00, 0.96, 0.12, 1000, "c-p96-fardtop"),
    (96, 0.04, 0.04, 0.96, 0.30, 1000, "c-p96-najashi"),
    (96, 0.04, 0.36, 0.96, 0.64, 800, "c-p96-maqbari"),
    (97, 0.04, 0.26, 0.96, 0.46, 1000, "c-p97-num618"),
    (97, 0.04, 0.40, 0.96, 0.66, 800, "c-p97-iedadbox"),
]

ASKS = {
    "c-p91-isnadline": (
        "Transcris LETTRE À LETTRE, token par token : (1) l'isnād imprimé (عن [?] "
        "السختياني عن محمد بن سيرين عن أمّ عطية) — le nom entre عن et السختياني "
        "exactement (أبي زرعة? أبي نعمة? أبي تميمة? أيوب? — décris chaque lettre et ses "
        "points) ; (2) les 3-4 premiers mots de la phrase قالت: ... exactement (dخل "
        "علينا رسول الله ﷺ حين... — le verbe après حين exactement : نوفيّت? توفيّت? "
        "نغسل? — et le mot après : ابنتي? ابنته? ابنتَهُ?), et le mot après فقال."),
    "c-p92-matnlines": (
        "Transcris LIGNE PAR LIGNE tout le texte arabe imprimé visible (matn entre "
        "chevrons + la glose الشرح), du haut de la bande jusqu'au renvoi rouge, sans "
        "compléter. Notamment : le mot après أو أكثر من ذلك, les mots و... في الأخرة, "
        "le mot après فإذا فرغتن, puis le segment فلمّا فرغنا... jusqu'à la fin "
        "d'impression visible et le renvoi rouge chiffre par chiffre."),
    "c-p92-num614": (
        "Transcris LETTRE À LETTRE la citation imprimée ici (مالك عن نافع: أنّ عبد الله "
        "بن عمر كان [?]... الصلاة على الجنازة) — notamment les 2-3 mots après كان "
        "(exactement, lettre par lettre, avec les points), et le renvoi rouge CHIFFRE "
        "PAR CHIFFRE."),
    "c-p92-num620": (
        "Transcris LETTRE À LETTRE la citation imprimée ici (مالك عن نافع: أنّ عبد الله "
        "بن عمر كان إذا صلّى على الجنازة... [?]) — le verbe exact après الجنازة (avec "
        "ses points), le mot suivant, le mot après حتى, et le renvoi rouge CHIFFRE PAR "
        "CHIFFRE. Puis le titre du bloc suivant s'il apparaît."),
    "c-p92-names": (
        "Transcris LETTRE À LETTRE le bloc biographique ici imprimé : (1) هي [?] بنت "
        "[?] — le premier nom exact et le deuxième exact ; (2) وقيل: [?] بنت [?] — "
        "exact ; (3) les mots suivants (من فقهاء الصحابة?...) ; (4) وهي التي غسّلت "
        "[?] بنت النبي ﷺ — le nom exact avant بنت النبي ; (5) la liste des "
        "transmetteurs : كل nom exactement (محمد بن سيرين وأخته/أخواته [?] بنت سيرين، "
        "وأمّ [?]، وعلي بن [?]، وعبد [?] بن [?]، وإسماعيل بن عبد الرحمن، و[?]) ; "
        "(6) la phrase finale (عاشت إلى...)."),
    "c-p94-middle": (
        "Transcris LIGNE PAR LIGNE tout le texte imprimé visible : (1) la phrase "
        "containing فاطمة et عليّ (QUI lave QUI, verbe exact avec points : غسّلها? "
        "غسّلته? غسّلت?) ; (2) tout renvoi entre crochets (avec le mot exact : البخاري? "
        "البيهقي?...) ; (3) la phrase أما تغسيل الزوج... jusqu'à sa fin ; (4) tout "
        "autre renvoi. Sans rien compléter."),
    "c-p95-isnad597": (
        "Transcris LETTRE À LETTRE la ligne d'isnād imprimée (لما في الموطأ عن مالك، "
        "[?]) — le verbe exact après مالك (بلغه? سمع? أنّ...) et les 4-5 mots suivants "
        "jusqu'aux chevrons de la citation, puis le premier mot de la citation."),
    "c-p95-fardkifaya": (
        "Transcris LIGNE PAR LIGNE tout le texte imprimé visible en bas de page, "
        "notamment la phrase contenant فرض? كفاية? (ou غيرها) et le titre de section "
        "أ- حكم الصلاة على الجنازة s'il apparaît — exactement, sans compléter."),
    "c-p96-fardtop": (
        "Transcris LETTRE À LETTRE les 2-3 premières lignes imprimées de la page "
        "(continuation de la phrase de la page précédente : حكم الصلاة على الجنازة... "
        "?) — exactement."),
    "c-p96-najashi": (
        "Transcris LETTRE À LETTRE le matn de la citation (إنّ رسول الله ﷺ نعى النجاشي "
        "للناس...) jusqu'à sa fin exacte, puis le renvoi rouge entre crochets [الموطأ "
        "رقم: ...] CHIFFRE PAR CHIFFRE — combien de chiffres? quels chiffres? écris "
        "chacun séparément."),
    "c-p96-maqbari": (
        "Transcris LETTRE À LETTRE : (1) la citation courte avec son renvoi entre "
        "crochets (إذا صلّيتم على الميت... [سنن? أبي? داود?...]) ; (2) la ligne "
        "d'introduction du récit (عن [?] بن [?] [?]، عن أبيه، أنه سأل أبا هريرة) — le "
        "nom après عن et le mot après celui-ci, exactement (المقبري? المصيّبي?...) ; "
        "(3) les 3-4 premiers mots du récit (قال أبو هريرة:...) exactement."),
    "c-p97-num618": (
        "Transcris LETTRE À LETTRE la deuxième citation du bloc الاستثمار : مالك عن "
        "نافع عن عبد الله بن عمر أنه قال: «يُصلّي؟ على [?] [?]...» — chaque mot exact "
        "(le nom après على, le mot suivant, في المسجد?), et le renvoi rouge CHIFFRE "
        "PAR CHIFFRE."),
    "c-p97-iedadbox": (
        "Transcris LETTRE À LETTRE le bloc الإعداد للدرس القادم (titre + items ١- ٢- "
        "٣-) : (1) après أشرح: chaque lexie exactement (العفّة? – يحتسب – [?] من النار "
        "– [?] في مصيبتي) — notamment le premier mot de la 4e lexie (أجزني? أرجني? "
        "ألجني?) et le mot avant من النار (جنة? جنبة?); (2) les items ٢- et ٣- complets "
        "exactement."),
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
    time.sleep(8)

print("\n===== RÉSULTATS =====")
for name, q in ASKS.items():
    try:
        d = json.load(open(f"{OUT}/{name}.json", encoding="utf-8"))
        print(f"\n----- {name} -----")
        print(d["choices"][0]["message"]["content"][:1700])
    except Exception as e:
        print(f"\n----- {name} ----- ERREUR {e}")

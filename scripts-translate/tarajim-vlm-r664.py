# -*- coding: utf-8 -*-
"""Minhāj R664 — lectures VLM du tableau تراجم الأعلام (slot pdf-mut23h2u-281).
Patron hadith3-vlm-read-400-r660.py ; SDK isolé /tmp/vlm-r664 HORS arbre git.
3 pages pleines 300 dpi + 12 lignes 600 dpi (cellules dégradées) ; cache
tr-tmp/qa-crops-r664/_r664-read-<name>.json — toute récusation de la couche
texte est tranchée par preuve image, jamais devinée."""
import json
import os
import subprocess
import sys

DIR = "/home/z/my-project/tr-tmp/qa-crops-r664"
READ = "/tmp/vlm-r664/read.mjs"

COMMON = ("Un tableau bilingue de notices biographiques de savants de l'islam, tiré d'un "
          "manuel scolaire marocain (الاعلام à droite en cellules jaunes = noms ; ترجمتهم à "
          "gauche = biographies). Transcris EXACTEMENT, ligne à ligne, mot à mot, SANS "
          "corriger ni deviner. Pour chaque SAVANT (ligne du tableau) : 1) le NOM exact "
          "de la cellule de droite ; 2) la BIOGRAPHIE complète de la cellule de gauche "
          "entre guillemets « » tels qu'imprimés ; 3) les CHIFFRES ARABES-ORIENTAUX "
          "(٠١٢٣٤٥٦٧٨٩) chiffre par chiffre, un à un (ex. ٧٩٥ = 7 puis 9 puis 5) — "
          "signale explicitement chaque année de décès. Si un mot est dégradé, écris "
          "[؟] à sa place — JAMAIS de reconstruction devinée. ")
FULL = COMMON + "Vaisseau : transcris TOUTES les lignes du tableau, de haut en bas, au format :\nLIGNE <n> NOM: <cellule droite>\nLIGNE <n> BIO: <cellule gauche>\nANNÉE <n>: <chiffres lus un à un>"

ROW = COMMON + "Ici UNE SEULE ligne agrandie (600 dpi). Format :\nNOM: <cellule droite>\nBIO: <cellule gauche entière>\nANNÉE: <chiffres lus un à un>\nPOINT DIFFICILE: si des mots sont dégradés ou ambigus, décris ce que tu vois lettre à lettre au lieu de deviner."

PROMPTS = {
    # --- pages pleines 300 dpi ---
    "r664-p132-full": ("r664-p132-full", "hi-132-132.png", FULL),
    "r664-p133-full": ("r664-p133-full", "hi-133-133.png", FULL),
    "r664-p134-full": ("r664-p134-full", "hi-134-134.png", FULL),
    # --- lignes 600 dpi : cellules dégradées / pivots ---
    "r664-p132-r0-qari": ("r664-p132-r0-qari", "row-p132-r0-qari.png", ROW
        + "\nAttention particulière aux TITRES des ouvrages entre « » : vérifier lettre à "
          "lettre «منح الروض الأزهر في شرح الفقه الأكبر» (alif du رود : ر-و-ض ou ر-ب-ض ?) et "
          "le titre «مرقاة» suivi de quel mot exact."),
    "r664-p132-r3-raz": ("r664-p132-r3-raz", "row-p132-r3-raz.png", ROW
        + "\nAttention particulière à la LISTE des ouvrages : premier titre (الزهد ou autre — "
          "lettre à lettre), «الكنى», «الفوائد الكبير» (ف-ا-و-ا-ئ-د ?), «فوائد الرازيين», "
          "«الجرح والتعديل» — transcris chaque titre lettre à lettre."),
    "r664-p132-r5-zark": ("r664-p132-r5-zark", "row-p132-r5-zark.png", ROW
        + "\nAttention particulière : le NOM (الزركشي ou النركشي — lettre à lettre), le premier "
          "titre «لقطة العجلان» (ز ou ه ?), et l'année de décès chiffre par chiffre (٧٩٤)."),
    "r664-p133-r0-salah": ("r664-p133-r0-salah", "row-p133-r0-salah.png", ROW
        + "\nAttention particulière au TROISIÈME titre cité «وصل بلاغات الوطا» — vérifier lettre "
          "à lettre chaque mot de ce titre, ainsi que l'année de décès (٦٤٦)."),
    "r664-p133-r1-abd": ("r664-p133-r1-abd", "row-p133-r1-abd.png", ROW
        + "\nAttention particulière aux mots dégradés : «معانا عليه» après كان موفقا في "
          "التأليف (lettre à lettre), le titre «جامع بيان العلم وفصله» (ف-ض-ل-ه ou ف-ه-ل-ه ?), "
          "«وما ينبغي في روابته وحماه» (ر-و-ا-ت-ه ?), et l'année (٤٦٣)."),
    "r664-p133-r2-hakim": ("r664-p133-r2-hakim", "row-p133-r2-hakim.png", ROW
        + "\nAttention particulière à «عرف بالحاكم لنقاده القصباء» — lettre à lettre de نقاده "
          "et القصباء, puis «فيه الكتب التي لم يسبق» et l'année (٤٠٥)."),
    "r664-p133-r3-iraqi": ("r664-p133-r3-iraqi", "row-p133-r3-iraqi.png", ROW
        + "\nAttention particulière au titre de l'alfiyya «التصرة والتذكرة» (ص-ر-ة ?) et «نظم "
          "الدرر السنية في السير الزكية» lettre à lettre, et l'année (٨٠٦)."),
    "r664-p133-r4-khatib": ("r664-p133-r4-khatib", "row-p133-r4-khatib.png", ROW
        + "\nAttention particulière aux mots dégradés après وصار أحفظ أهل عصره على الإطلاق : "
          "«وعثل ودرخ وأوضض» (décris lettre à lettre), «عمل نيبا وخمسين مصنفا», «احترق كثير "
          "منها بعدة بغمسين سنة» (lettre à lettre), et l'année (٤٦٣)."),
    "r664-p134-r0-dhahabi": ("r664-p134-r0-dhahabi", "row-p134-r0-dhahabi.png", ROW
        + "\nAttention particulière aux titres «ميزان الاعتدال في نقد الرجال», «العين في طبقات "
          "الحديث» (ع-ي-ن ou ع-ب-ر ?), «المشتهه في أسماء الرجال» (ش-ت-ب-ه ?), et l'année (٧٤٨)."),
    "r664-p134-r1-sakhawi": ("r664-p134-r1-sakhawi", "row-p134-r1-sakhawi.png", ROW
        + "\nAttention particulière aux titres «فتح المغيث بشرح ألفية الحديث», «الغاية في شرح "
          "الهداية في علم الرواية» (lettre à lettre), «القاصد الحسنة في الأحاديث المشتهرة على "
          "الألسنة» (ح-س-ن-ة ou ح-س-ن ?), et l'année (٩٠٢)."),
    "r664-p134-r2-suyuti": ("r664-p134-r2-suyuti", "row-p134-r2-suyuti.png", ROW
        + "\nAttention particulière au nom du grand-père «ابن سائق الدين الخضيري جلال الدين» "
          "(lettre à lettre), à l'alfiyya «نظم الدرر في علم الأثر», à «اللمع في أسباب ورود "
          "الحديث» et «طبقات الحفاظ», et l'année (٩١١)."),
    "r664-p134-r3-iyad": ("r664-p134-r3-iyad", "row-p134-r3-iyad.png", ROW
        + "\nAttention particulière aux mots dégradés : «أدوابهم وأدابه ولني قدضاء سبئة» "
          "(lettre à lettre de chaque mot), «ثم قضاء غزا ناطه» (lettre à lettre), «الإلاع إلى "
          "معرفة أصول الرواية وتقييد السماع» (إ-ل-م-ا-ع ?), «توفي بمركش» (م-ر-ك-ش ?), et "
          "l'année (٥٤٤)."),
    "r664-p134-r4-nawawi": ("r664-p134-r4-nawawi", "row-p134-r4-nawawi.png", ROW
        + "\nAttention particulière aux titres «تهذيب الأسماء واللغات» et «التقريب والتيسير في "
          "مصطلح الحديث», et l'année (٦٧٦)."),
}


def run(name):
    out = os.path.join(DIR, f"_{name}.json")
    if os.path.exists(out):
        print(f"cache {name}")
        return
    _, img, prompt = PROMPTS[name]
    pf = f"/tmp/vlm-r664/prompt-{name}.txt"
    with open(pf, "w", encoding="utf-8") as f:
        f.write(prompt)
    img_path = os.path.join(DIR, img)
    body = None
    for attempt in range(5):
        res = subprocess.run(["node", READ, img_path, pf, out + ".raw"],
                             capture_output=True, text=True, timeout=420,
                             cwd="/tmp/vlm-r664")
        if res.returncode == 0:
            body = open(out + ".raw", encoding="utf-8").read().strip()
            break
        err = res.stderr or res.stdout
        if "429" in err or "Too many requests" in err:
            wait = 25 * (attempt + 1)
            print(f"429 {name} (essai {attempt+1}) — attente {wait}s")
            import time
            time.sleep(wait)
        else:
            print(f"ERR {name}: {err[:300]}")
            return
    if body is None:
        print(f"ABANDON {name} après 5 essais (rate limit persistant)")
        return
    json.dump({"name": name, "image": img, "body": body}, open(out, "w", encoding="utf-8"),
              ensure_ascii=False, indent=1)
    os.remove(out + ".raw")
    print(f"OK {name} — {len(body)} car")


if __name__ == "__main__":
    import time
    for n in sys.argv[1:] or list(PROMPTS):
        run(n)
        time.sleep(8)

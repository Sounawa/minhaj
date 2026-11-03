#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""R552 — 4e passe VLM (finale) : micro-crops 1200 dpi sur les ~14 derniers points
ambigus de la leçon 14 (pdf-15). L'image tranche en dernier ressort."""
import fitz
import json
import os
import subprocess
import time

HOME = "/home/z/my-project"
PDF = f"{HOME}/content/textbooks-src/hadith-2-iadadi_text.pdf"
CROPS = f"{HOME}/tr-tmp/qa-crops-r552"
OUT = f"{HOME}/tr-tmp/vlm-r552"
os.makedirs(OUT, exist_ok=True)

BASE = ("Tu lis une image d'un manuel scolaire marocain de hadith (Muwaṭṭaʾ Mālik / "
        "Šarḥ az-Zarqānī, 2e année collégiale), agrandie à très haute résolution. "
        "Réponds UNIQUEMENT à la question posée, par transcription EXACTE du texte "
        "imprimé visible, LETTRE PAR LETTRE (avec les diacritiques) pour les mots "
        "interrogés. Si un mot ou une lettre reste incertain même agrandi, écris "
        "[illisible] plutôt que de deviner. N'invente AUCUN texte, ne complète "
        "JAMAIS de mémoire, ne corrige pas l'imprimé même s'il te paraît fautif.")

doc = fitz.open(PDF)

def crop(page_no, y0f, y1f, dpi, name, x0f=0.04, x1f=0.96):
    pg = doc[page_no - 1]
    r = pg.rect
    clip = fitz.Rect(r.width * x0f, r.height * y0f, r.width * x1f, r.height * y1f)
    pix = pg.get_pixmap(matrix=fitz.Matrix(dpi / 72, dpi / 72), clip=clip)
    pix.save(f"{CROPS}/{name}.png")
    print(f"{name}: {pix.width}x{pix.height}")

crop(98, 0.03, 0.17, 1200, "r4-p98-title")
crop(98, 0.33, 0.45, 1200, "r4-p98-obj3")
crop(98, 0.44, 0.64, 1000, "r4-p98-tamhid-matn")
crop(99, 0.025, 0.095, 1200, "r4-p99-t2isnad")
crop(99, 0.30, 0.50, 1200, "r4-p99-t3mots")
crop(99, 0.54, 0.76, 1000, "r4-p99-biotail")
crop(99, 0.74, 1.00, 1000, "r4-p99-sharh")
crop(100, 0.15, 0.32, 1200, "r4-p100-debut")
crop(100, 0.26, 0.40, 1200, "r4-p100-milieu")
crop(100, 0.60, 0.88, 1000, "r4-p100-fin")
crop(101, 0.90, 1.00, 1200, "r4-p101-jabirfin")
crop(102, 0.005, 0.075, 1200, "r4-p102-latabki")
crop(103, 0.22, 0.36, 1200, "r4-p103-mots")
crop(101, 0.40, 0.55, 1000, "r4-p101-naqltail")

ASKS = [
    ("r4-p98-title", "r4-p98-title.png",
     "Transcris LETTRE PAR LETTRE le titre de leçon complet (le bandeau) : les mots "
     "imprimés après أحكام الجنائز, séparés par des tirets. Est-ce : (a) القبر "
     "والدفن وآداب الجنازة (b) الغسل والكفن وآداب الجنازة (c) القبر والكفن "
     "والجنازة (d) autre ? Transcris exactement, et le numéro du الدرس."),
    ("r4-p98-obj3", "r4-p98-obj3.png",
     "Transcris l'objectif 3 ENTIER lettre par lettre. Le DERNIER MOT est-il : (a) "
     "وتلقيه (b) وتلقييه (c) وتلقينه (d) autre ? Écris ses lettres une par une "
     "(avec diacritiques)."),
    ("r4-p98-tamhid-matn", "r4-p98-tamhid-matn.png",
     "Transcris LETTRE PAR LETTRE le matn du hadith du tamhīd entre guillemets. "
     "Points fermés : (a) la conjonction au milieu : فإن شهد دفنها / ومن شهدها "
     "دفنها / autre ? (b) le mot قيراط apparaît où exactement — et le mot après "
     "قيراطان : القيراط / القبراط (avec ب ?) / autre ? Transcris le matn complet."),
    ("r4-p99-t2isnad", "r4-p99-t2isnad.png",
     "Transcris LETTRE PAR LETTRE la ligne d'isnād visible : مالك، عن محمد بن أبي "
     "بكر بن [?], عن [?]، عن أبي النضر [?]. Le dernier mot (la nisba) est-il : "
     "(a) السلماني (b) السلامي (c) السلمي (d) autre ? Écris ses lettres."),
    ("r4-p99-t3mots", "r4-p99-t3mots.png",
     "CONCENTRE-TOI sur la phrase «لعن رسول الله ﷺ [MOT 1] و[MOT 2]». Transcris "
     "MOT 1 et MOT 2 LETTRE PAR LETTRE avec leurs diacritiques. Puis transcris ce "
     "qui est imprimé entre عن أمه عمرة بنت عبد الرحمن et تقول (أَنَّهَا سَمِعَتْ "
     "? عائشة apparaît-il ?). Puis la glose après يعني. Puis le renvoi [الموطأ "
     "رقم : N] chiffre par chiffre."),
    ("r4-p99-biotail", "r4-p99-biotail.png",
     "Transcris mot à mot les dernières lignes de l'encadré ترجمة الراوي : les "
     "judgements (قال أبو حسان الزيادي ...) et les DEUX dates éventuelles de mort "
     "(سنة ثمان وتسعين ? سنة ست ومائة ?) avec QUI dit quoi (قال / يقال / وقال). "
     "Transcris exactement."),
    ("r4-p99-sharh", "r4-p99-sharh.png",
     "Transcris mot à mot le bloc الشرح ENTIER (avec le titre et les rubriques "
     "visibles). Points fermés : (a) le premier terme glosé : العَقيق / العُقبي / "
     "autre ? et sa glose (موضع قرب المدينة ?) ; (b) le deuxième terme glosé et "
     "sa glose (يصبر رضيًّا بقضاء الله راجيًا فضله ?) ; (c) la troisième glose "
     "(جنة من النار : وقاية من عذاب الله تعالى ?)."),
    ("r4-p100-debut", "r4-p100-debut.png",
     "Transcris TOKEN PAR TOKEN le début du paragraphe صفة الدفن depuis يندب. "
     "Points fermés : (a) après وإن كان الميت : امرأة ? (b) la phrase : ويستر "
     "على [فم القبر / قبرها / autre ?] [بثوب / بنوب / autre ?] [قبل إنزالها ?] "
     "— transcris-la lettre par lettre."),
    ("r4-p100-milieu", "r4-p100-milieu.png",
     "Transcris TOKEN PAR TOKEN la zone : ويقول من يتولى إضجاعه : بسم الله وعلى "
     "سنة رسول الله ﷺ، و[يعادل / يعدل / autre ?] [رجله / رجليه / autre ?] "
     "[برفق / بركن / autre ?]، ويجعل التراب خلفه وأمامه، ويحل عقد كفنه. "
     "Transcris lettre par lettre les mots interrogés."),
    ("r4-p100-fin", "r4-p100-fin.png",
     "Transcris TOKEN PAR TOKEN : (1) ثم يصب التراب على القبر في سهولة "
     "و[تقريق / تفريق / ترقيق / تفريج / autre ?] ; (2) [دون / دون ذلك / دونك / "
     "autre ?] [دك / ذلك / الأرض ...] — la formule exacte avant بشدة بالأقدام "
     "(هل y a-t-il دكّ الأرض ? قرعها ? قبورها ? قبرها ?) ; (3) فإذا فرغ الناس "
     "من الدفن يندب أن يبقى أحدهم [قريبا من رأس القبر / عند القبر / autre ?] "
     "ويدعو للميت بالمغفرة و[التثبيت / الثبات ?] عند [السؤال ?]."),
    ("r4-p101-jabirfin", "r4-p101-jabirfin.png",
     "Transcris LETTRE PAR LETTRE la fin de page : فصاح النسوة وبكين، فجعل جابرٌ "
     "[LE VERBE EXACT : يبكين / يقول / يبكي / autre ?]، فقال رسول الله ﷺ... — "
     "écris les lettres du verbe une par une."),
    ("r4-p102-latabki", "r4-p102-latabki.png",
     "Transcris LETTRE PAR LETTRE la première ligne : ﷺ : دعهن، فإذا وجب فلا "
     "[LE MOT EXACT : تُبَكِّنْ / تبكِ / تنكّن / autre ?] [باكية / باكيةً / "
     "autre ?]. Écris chaque lettre avec diacritiques."),
    ("r4-p103-mots", "r4-p103-mots.png",
     "CONCENTRE-TOI sur la citation : ففي حديث الدرس : «لعن رسول الله ﷺ [MOT 1] "
     "و[MOT 2]، يعني [?]». Transcris MOT 1, MOT 2 et la glose LETTRE PAR LETTRE "
     "avec diacritiques."),
    ("r4-p101-naqltail", "r4-p101-naqltail.png",
     "Transcris TOKEN PAR TOKEN le paragraphe : واختلف في جواز نقل الميت من بلد "
     "إلى بلد... jusqu'à غرض راجح. Point fermé : la formule après وقيل يستحب : "
     "والأولى [تفصيل / تنزيل / تترتب / autre ?] ذلك على حالين ? Et : فالجواز "
     "إذا كان [هناك / هتك ?] غرض راجح... والمنع حيث لا يكون [هناك / هتك ?] "
     "غرض راجح ? Transcris exactement."),
]

def vision_call(prompt, img, out, tries=6):
    cmd = ["z-ai", "vision", "-p", prompt, "-i", img, "-o", out]
    for t in range(tries):
        r = subprocess.run(cmd, capture_output=True, text=True, timeout=300)
        if r.returncode == 0:
            return True, ""
        err = (r.stderr or "") + (r.stdout or "")
        if "429" in err or "Too many" in err:
            wait = 40 + 25 * t
            print(f"  429 — attente {wait}s (tentative {t + 1}/{tries})")
            time.sleep(wait)
            continue
        return False, err[:200]
    return False, "429 persistant"

for key, img, q in ASKS:
    out = f"{OUT}/{key}.json"
    if os.path.exists(out):
        print("•", key, "déjà lu")
        continue
    ok, err = vision_call(f"{BASE}\nQUESTION : {q}", f"{CROPS}/{img}", out)
    print(("✓" if ok else "✗"), key, err)

print("\n===== RÉSULTATS =====")
for key, img, q in ASKS:
    try:
        d = json.load(open(f"{OUT}/{key}.json", encoding="utf-8"))
        print(f"\n----- {key} -----")
        print(d["choices"][0]["message"]["content"][:2500])
    except Exception as e:
        print(f"\n----- {key} ----- ERREUR {e}")

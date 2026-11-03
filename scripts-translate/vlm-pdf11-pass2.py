#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""R1737-PAR — 2ᵉ passe : recadrages serrés 550-600 dpi + lectures VLM
pour trancher : numéros rouges (536/540/555/556/544), āya الواقعة (renvoi),
dire d'ʿUmar, liste des sujūdāt (p.76 bas + p.77 haut), matn ʿĀʾiša fin,
lexies الإعداد القبلي, titre الاستئناس, bio ʿAmr b. Ḥazm (zone re-cadrée)."""
import os
import subprocess

HOME = "/home/z/my-project"
PDF = f"{HOME}/content/textbooks-src/hadith-2-iadadi_text.pdf"
CROPS = f"{HOME}/tr-tmp/qa-crops-pdf11"
OUT = f"{HOME}/tr-tmp/vlm-pdf11"

BASE = ("Tu lis une image d'un manuel scolaire marocain de hadith (Muwaṭṭaʾ Mālik / "
        "Šarḥ az-Zarqānī, 2e année collégiale). Réponds UNIQUEMENT à la question posée, "
        "par transcription EXACTE du texte imprimé visible, token par token. Si tu n'es "
        "pas sûr d'un mot ou d'un chiffre, écris [illisible]. N'invente AUCUN texte, ne "
        "complète jamais de mémoire, ne corrige pas l'imprimé même s'il te paraît fautif.")

import fitz
os.makedirs(CROPS, exist_ok=True)
doc = fitz.open(PDF)


def crop(page_no, x0f, y0f, x1f, y1f, dpi, name):
    pg = doc[page_no - 1]
    r = pg.rect
    clip = fitz.Rect(r.width * x0f, r.height * y0f, r.width * x1f, r.height * y1f)
    pix = pg.get_pixmap(matrix=fitz.Matrix(dpi / 72, dpi / 72), clip=clip)
    pix.save(f"{CROPS}/{name}.png")
    print(f"{name}: {pix.width}x{pix.height}")


# --- recadrages serrés ---
crop(73, 0.05, 0.36, 0.95, 0.66, 550, "p73-intro-aya-tight")
crop(73, 0.05, 0.60, 0.95, 1.00, 600, "p73-hadith1-tight")
crop(74, 0.05, 0.02, 0.95, 0.28, 600, "p74-hadith2-tight")
crop(74, 0.05, 0.24, 0.95, 0.50, 600, "p74-hadith3-tight")
crop(74, 0.05, 0.48, 0.95, 0.78, 550, "p74-bio-tight")
crop(75, 0.05, 0.30, 0.95, 0.50, 600, "p75-aya-tight")
crop(76, 0.05, 0.36, 0.95, 0.58, 600, "p76-umar-quote-tight")
crop(76, 0.05, 0.84, 0.95, 1.00, 600, "p76-liste-debut")
crop(77, 0.05, 0.02, 0.95, 0.24, 600, "p77-liste-fin")
crop(77, 0.05, 0.34, 0.95, 0.56, 600, "p77-num556-tight")
crop(78, 0.05, 0.02, 0.95, 0.30, 600, "p78-aya-tight")
crop(78, 0.05, 0.20, 0.95, 0.40, 600, "p78-matn-fin-num")
crop(78, 0.05, 0.60, 0.95, 0.86, 600, "p78-idad-tight")

ASKS = [
    ("p73-intro-aya-tight", "p73-intro-aya-tight.png",
     "(1) Transcris le paragraphe d'introduction visible mot à mot, y compris la "
     "citation coranique en cursive et son renvoi entre crochets (سورة الحجر الآية: "
     "... ) — CHIFFRES EXACTS du renvoi, chiffre par chiffre. (2) Transcris la phrase "
     "interrogative qui suit la citation (فما حكم الطهارة...)."),
    ("p73-hadith1-tight", "p73-hadith1-tight.png",
     "Transcris mot à mot le hadith visible (isnād + matn) et SURTOUT la clôture "
     "[الموطأ رقم: ...] — les chiffres du numéro, un par un, tels qu'imprimés (chiffres "
     "arabes orientaux : écris-les puis convertis-les). Ne corrige rien."),
    ("p74-hadith2-tight", "p74-hadith2-tight.png",
     "Transcris mot à mot la fin du matn visible («... أدرّكه») et la clôture [الموطأ "
     "رقم: ...] — chiffres du numéro un par un, tels qu'imprimés."),
    ("p74-hadith3-tight", "p74-hadith3-tight.png",
     "Transcris mot à mot le texte visible (قال يحيى قال مالك...) et la clôture "
     "[الموطأ رقم: ...] — chiffres du numéro un par un, tels qu'imprimés."),
    ("p74-bio-tight", "p74-bio-tight.png",
     "Transcris mot à mot la section ترجمة الراوي visible (la couche lit : عمرو بن "
     "حزم: هو أبو الضحاك عمرو بن حزم بن زيد النجاري الخزرجي الأنصاري، استعمله رسول "
     "الله صلّى الله عليه وسلّم على أهل نجران ليفقههم في الدين ويعلمهم القرآن ويأخذ "
     "صدقاتهم، مات بالمدينة سنة إحدى وخمسين) — confirme ou corrige chaque nom, la "
     "kunyā, la mission et l'année de la mort."),
    ("p75-aya-tight", "p75-aya-tight.png",
     "(1) Transcris la phrase لقوله تعالى et la citation coranique imprimée en "
     "cursive entre parenthèses/crochets, MOT À MOT telle qu'imprimée. (2) Transcris "
     "le renvoi [سورة الواقعة الآية: ...] — CHIFFRES EXACTS, chiffre par chiffre, "
     "tels qu'imprimés (ne les convertis pas, ne les corrige pas). (3) Transcris la "
     "phrase qui suit : la couche lit وهذا نهي وإن كان لفظه لفظ الخبر فمعناه الأمر؛ "
     "لأن خبر الباري تعالى لا يكون بخلاف مخبره — confirme ou corrige."),
    ("p76-umar-quote-tight", "p76-umar-quote-tight.png",
     "Transcris mot à mot, token par token, le dire d'عمر imprimé dans cette zone "
     "(après [صحيح البخاري] ou وقول عمر) : la couche lit «... وقال عمر: ... فمن سجد "
     "فقد أصاب، ومن لم يسجد ...» — transcris CHAQUE mot exactement comme imprimé, "
     "même si la graphie paraît inhabituelle, jusqu'à la fin de la citation et son "
     "renvoi [أخرجه البخاري] s'il est visible."),
    ("p76-liste-debut", "p76-liste-debut.png",
     "Transcris mot à mot la fin de la page visible : la couche lit «أخبرني عكرمة بن "
     "خالد أن سعيد بن جبير أخبره أنه سمع ابن عباس وابن عمر يعدان كم في القرآن من "
     "سجدة؛ فقالا: «الأعراف ...» — transcris les mots visibles jusqu'en bas de "
     "l'image (y compris le premier nom de sourate après فقالا:)."),
    ("p77-liste-fin", "p77-liste-fin.png",
     "Transcris mot à mot, token par token, la liste imprimée visible (noms de "
     "sourates) jusqu'au renvoi [مصنف عبد الرزاق] : la couche lit «... والرعد والنخل "
     "والإسراء ومريم والحج ... والفرقان وطس وألم تنزيل وص وحم عسق ... إحدى عشرة سجدة، "
     "قالا: وليس في المفصل منها شيء» — transcris CHAQUE token exactement comme "
     "imprimé (sourate par sourate, dans l'ordre, avec le premier token de chaque "
     "ligne), y compris les éventuels mots d'ouverture entre guillemets (طس، ألم "
     "تنزيل، هاء ميم، أولها) et la phrase «السَّجدة إحدى عشرة سجدة» telle qu'imprimée."),
    ("p77-num556-tight", "p77-num556-tight.png",
     "(1) Transcris mot à mot la phrase contenant la clôture [الموطأ رقم: ...] et le "
     "numéro EXACT, chiffre par chiffre, tel qu'imprimé en rouge. (2) Transcris "
     "la phrase ووجه هذه الرواية si elle est visible."),
    ("p78-aya-tight", "p78-aya-tight.png",
     "(1) Transcris le titre de section imprimé en haut (الاستئناس ? الاستئثار ?) mot "
     "à mot. (2) Transcris la phrase d'introduction, la citation coranique en cursive "
     "MOT À MOT telle qu'imprimée, et le renvoi [سورة الواقعة الآية: ...] — CHIFFRES "
     "EXACTS, chiffre par chiffre, tels qu'imprimés (ne les convertis pas)."),
    ("p78-matn-fin-num", "p78-matn-fin-num.png",
     "(1) Transcris mot à mot la fin du matn visible : «... قالت عائشة: ولقد رأيته "
     "ينزل عليه ... الشديد ... فيفصم عنه وإن جبينه ليتفصد ...» — chaque mot tel "
     "qu'imprimé (le mot après البرد الشديد, et le mot final avant la clôture : حرقاً "
     "? عرقاً ? فعرقاً ?). (2) La clôture [الموطأ رقم: ...] — chiffres du numéro un "
     "par un, tels qu'imprimés en rouge."),
    ("p78-idad-tight", "p78-idad-tight.png",
     "Transcris mot à mot : (1) la question ١- ما معنى قوله تعالى... si visible ; "
     "(2) l'en-tête الإعداد القبلي et la phrase أحفظ أحاديث الدرس المقبل وأجيب عن "
     "الآتي ; (3) l'item ١- أشرح: et les lexies EXACTEMENT comme imprimées (la couche "
     "lit : عدل عشر - رقاب - حرزا من الشيطان - يبتدرونها) — chaque lexie, token par "
     "token, sans la corriger ; (4) l'item ٢- أستخرج..."),
]

for key, img, q in ASKS:
    out = f"{OUT}/{key}.json"
    if os.path.exists(out):
        print("•", key, "déjà lu")
        continue
    cmd = ["z-ai", "vision", "-p", f"{BASE}\nQUESTION : {q}", "-i", f"{CROPS}/{img}", "-o", out]
    r = subprocess.run(cmd, capture_output=True, text=True, timeout=240)
    print(("✓" if r.returncode == 0 else "✗"), key, (r.stderr or "").strip()[:120])

print("\n===== RÉSULTATS =====")
for key, img, q in ASKS:
    try:
        d = json.load(open(f"{OUT}/{key}.json", encoding="utf-8"))
        print(f"\n----- {key} -----")
        print(d["choices"][0]["message"]["content"][:1400])
    except Exception as e:
        print(f"\n----- {key} ----- ERREUR {e}")

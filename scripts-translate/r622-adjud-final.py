#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""R622 — adjudications finales leçon 9 (pdf-mut23h2u-263, p.52-56).
Derniers points contestés après OCR multicouche : noms de l'isnād p.54,
fin du hadith + citation ʿIlal, citation Maqāyīs, citation Muqaddima,
citation Muslim/Nawawī, mot mufradāt, ligne الخليلي, question p.52,
gloses p.52, en-têtes p.56, hadith Abū Dāwūd, fin citation Muslim.
Toute récusation tranchée par preuve image directe (méthode R621)."""
import json
import subprocess

HOME = "/home/z/my-project"
SRC = f"{HOME}/content/textbooks-src/ulum-hadith-2-thanawi_text.pdf"
OCR = f"{HOME}/tr-tmp/r622-ocr"
QC = f"{HOME}/tr-tmp/qa-crops-r622"
OUT = f"{HOME}/tr-tmp/vlm-r622"


def crop(page, y0, y1, x0, x1, tag, dpi):
    """pdftoppm crop en points PDF (612x792)."""
    out = f"{OCR}/{tag}"
    s = int(dpi / 72)
    cmd = ["pdftoppm", "-f", str(page), "-l", str(page), "-r", str(dpi),
           "-x", str(int(x0 * s)), "-y", str(int(y0 * s)),
           "-W", str(int((x1 - x0) * s)), "-H", str(int((y1 - y0) * s)),
           "-singlefile", "-png", SRC, out]
    subprocess.run(cmd, check=True, capture_output=True)
    return f"{out}.png"


BASE = ("Tu lis une image d'un manuel scolaire marocain de hadith (علوم الحديث "
        "الثانية ثانوي, Naḫbat al-fikr). Réponds UNIQUEMENT à la question posée, "
        "par transcription EXACTE du texte imprimé visible. Pour tout CHIFFRE, "
        "transcris-le chiffre par chiffre de gauche à droite tel que imprimé. "
        "Si tu n'es pas sûr, écris [illisible]. N'invente RIEN, ne complète "
        "jamais de mémoire, ne corrige pas le texte.")

TASKS = []

# --- nouveaux recadrages serrés ---
TASKS.append(("isnad-names-tight", crop(54, 203, 232, 250, 612, "ADJ51-names-tight", 1800),
              "Transcris EXACTEMENT cette ligne : « خت بن حبس وهو أخو حمزة الزيات ... عن أبي "
              "إسحاق عن ... بن ... عن ابن عباس ». Je veux : (1) le mot EXACT après "
              "« حمزة الزيات » (الضرير ? المقرئ ? autre) ; (2) les DEUX noms entre "
              "« عن أبي إسحاق عن » et « عن ابن عباس » lettre par lettre."))

TASKS.append(("hadith-tail-tight", crop(54, 236, 282, 250, 612, "ADJ52-hadith-tail-tight", 1800),
              "Transcris EXACTEMENT les mots après « وصام » jusqu'au crochet fermant, "
              "puis le contenu ENTIER du crochet de citation [ ... ] chiffre par "
              "chiffre. La couche OCR hésite entre « وقرض اليف دحل الهنة » et "
              "« وقرى الضيف دخل الجنة » — tranche par ce que tu VOIS, mot à mot."))

TASKS.append(("idad-header-p56", crop(56, 42, 66, 0, 612, "ADJ53-ist-header-p56", 1500),
              "Transcris EXACTEMENT la ligne d'en-tête qui commence par « أتأمل النص "
              "». La couche OCR hésite entre « وأستخرج منه: » et « وأجيب عنه: » — "
              "tranche par ce que tu VOIS."))

TASKS.append(("mufradat-word", crop(53, 194, 214, 250, 612, "ADJ54-mufradat-word", 1800),
              "Dans la citation « المعرفة والعرفان: إدراك الشيء بتفكر وتدبر ... », "
              "transcris EXACTEMENT le mot entre « وهو » et « من العلم », puis la "
              "fin de la citation et le crochet [ ... ] avec son numéro de page "
              "chiffre par chiffre."))

TASKS.append(("muslim-quote-end", crop(55, 628, 662, 150, 612, "ADJ55-muslim-end", 1500),
              "Transcris EXACTEMENT la dernière ligne de la citation de l'Imam "
              "Muslim : « فإن كان الأغلب من حديثه كذلك ... ». Je veux la fin "
              "EXACTE après « كذلك » mot à mot (était-ce « كان غير مقبول له » ? "
              "autre chose ?)."))

# --- relectures VLM sur recadrages existants ---
TASKS.append(("banner-title", f"{QC}/ADJ1b-p52-banner-wide-900.png",
              "Transcris EXACTEMENT la bannière du haut : numéro et titre du "
              "درس (leçon), puis l'en-tête أهداف الدرس s'il est visible."))

TASKS.append(("objectif-2", f"{OCR}/obj2-p52-1200.png",
              "Transcris EXACTEMENT l'objectif n°2 de la leçon (la ligne qui "
              "commence par « أن أتبين ... »)."));

TASKS.append(("question-p52", f"{OCR}/question52-p52-1200.png",
              "Transcris EXACTEMENT la question complète (deux lignes) : elle "
              "commence par « فماذا تسمى... ». Je veux les DEUX questions et "
              "l'éventuelle troisième (« وما فائدة ... ») mot à mot."))

TASKS.append(("matn-p52", f"{QC}/ADJ3-p52-matn-900.png",
              "Transcris EXACTEMENT le texte encadré (matn) : « قال الحافظ ابن حجر "
              "... ». Y a-t-il un crochet de citation [ ... ] après ? Si oui, "
              "transcris-le chiffre par chiffre."))

TASKS.append(("gloss-rajah", f"{OCR}/ADJ39-takeover-rajah-wrap-p52-1800.png",
              "Transcris EXACTEMENT la glose de marge : « الراجح: ... » et « ورجح "
              "الشيء بيده: ... ». Mot à mot, y compris les diacritiques visibles."))

TASKS.append(("gloss-daaf", f"{OCR}/gloss-col-r-p52-1500.png",
              "Transcris EXACTEMENT la glose de marge : « الضعف: ... ». Mot à mot."))

TASKS.append(("abudawud-matn", f"{QC}/ADJ8-p54-abudawud-matn-600.png",
              "Transcris EXACTEMENT le hadith encadré (matn) tel qu'imprimé, de "
              "« جاء رجل » jusqu'à « واستغفر الله », mot à mot, puis le crochet "
              "[ سنن أبي داود ... ] tel quel."))

TASKS.append(("khalili-line", f"{OCR}/ADJ41-takeover-khalili-wide-p54-1500.png",
              "Transcris EXACTEMENT : (1) ce qui précède « الخليلي » (وقال ... "
              "الخليلي ?) ; (2) le mot entre « حديثه في » et « في رمضان » (المواقع ? "
              "المواقيت ? المواضع ?) — tranche par ce que tu VOIS."))

TASKS.append(("maqayis-cite", f"{OCR}/munkar-ist-p53-1200.png",
              "En haut de cette image, transcris le crochet de citation qui suit "
              "« لم يعترف به لسانه ». Je veux son contenu EXACT, en particulier "
              "les chiffres du numéro de volume/page, chiffre par chiffre de "
              "gauche à droite tel qu'imprimé."))

TASKS.append(("nukat-cite-p53", f"{QC}/ADJ18-p53-nukat-quote-600.png",
              "Transcris le crochet de citation [ النكت على كتاب ابن الصلاح ... ] "
              "visible en bas ou à gauche, ses chiffres chiffre par chiffre de "
              "gauche à droite tel qu'imprimé."))

TASKS.append(("muqaddima-cite", f"{OCR}/ADJ31-takeover-muqaddima-cite-p55-1800.png",
              "Transcris le crochet de citation [ مقدمة ابن الصلاح ... ] avec son "
              "numéro de page chiffre par chiffre de gauche à droite tel "
              "qu'imprimé."))

TASKS.append(("muslim-cite", f"{OCR}/ADJ42b-takeover-muslim-cite-p55-1800.png",
              "Transcris le crochet de citation [ صحيح مسلم مع شرح النووي ... ] "
              "avec ses chiffres chiffre par chiffre de gauche à droite tel "
              "qu'imprimé."))

TASKS.append(("muslim-line2", f"{OCR}/ADJ40-takeover-muslim-zoom-p55-1500.png",
              "Dans « علامة المنكر في حديث المحدث إذا ما عرضت روايته ... », "
              "transcris EXACTEMENT ce qui suit « روايته » jusqu'à « خالفت » : "
              "est-ce « للحديث على رواية غيره من أهل الحفظ والرضى » ou « على "
              "روايات أهل الحفظ والرضى » ou autre ? Mot à mot."))

subprocess.run(["mkdir", "-p", OUT], check=True)
for key, img, q in TASKS:
    out = f"{OUT}/{key}.json"
    cmd = ["z-ai", "vision", "-p", f"{BASE}\nQUESTION : {q}", "-i", img, "-o", out]
    r = subprocess.run(cmd, capture_output=True, text=True, timeout=300)
    print(("OK  " if r.returncode == 0 else "FAIL") + " " + key)

print("\n===== ADJUDICATIONS R622 =====")
for key, _, _ in TASKS:
    try:
        d = json.load(open(f"{OUT}/{key}.json", encoding="utf-8"))
        print(f"\n----- {key} -----")
        print(d["choices"][0]["message"]["content"][:1600])
    except Exception as e:
        print(f"\n----- {key} ----- ERREUR {e}")

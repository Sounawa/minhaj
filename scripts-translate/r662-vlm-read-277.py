# -*- coding: utf-8 -*-
# R662 — lectures VLM bornées : 5 zooms z900 restés non lus (R659) + crops tight
# haute résolution R662. Sortie : tr-tmp/qa-crops-r662/_r662-read-<name>.json
# + read-r662-<name>.txt. Toute adjudication = PREUVE IMAGE documentée.
import json
import os
import subprocess
import time

CROPS = "/home/z/my-project/tr-tmp/qa-crops-r662"

BASE = ("Tu lis une image d'un manuel scolaire marocain de hadith (commentaire de la "
        "Naḫbat al-fikr d'Ibn Ḥaǧar, 2e année secondaire), leçon المصحف والمحرف. "
        "Réponds UNIQUEMENT à la question posée, par transcription EXACTE du texte "
        "imprimé visible, token par token. Si tu n'es pas sûr d'un mot ou d'un "
        "chiffre, écris [؟]. N'invente AUCUN texte, ne complète JAMAIS de mémoire "
        "(n'utilise PAS la version canonique d'un texte que tu connaîtrais), ne "
        "corrige PAS l'imprimé même s'il te paraît fautif. Pour chaque chiffre d'une "
        "référence, lis DIGIT PAR DIGIT (gauche puis droite du glyphe).")

ASKS = [
    # --- zooms z900 R659 restés non lus ---
    ("z900-p123-top", "Transcris EXACTEMENT tout le texte visible ligne par ligne : "
     "le titre magenta ب- اصطلاحا s'il est visible, la définition المحرف (عرفه ابن "
     "حجر بأنه ما...) mot à mot, et TOUT numéro de page ou renvoi visible (ex. ص 53 "
     "ou un crochet [ص ...]) chiffre par chiffre. Y a-t-il un crochet de source après "
     "la définition ? Transcris-le en entier."),
    ("z900-p123-jabir", "Transcris EXACTEMENT tout le texte visible ligne par ligne : "
     "le hadith de جابر avec ses voyelles LETTRE PAR LETTRE (سَجِّل chaque mot : "
     "رُمِيَّ؟ أَبِي؟ يَوْمَ؟ الأَخْرَبِ؟ عَلَى؟ الأَكَحِلِ؟ puis le mot après الأكحل "
     "EST EXACTEMENT فَكَوَاهُ ? c'est le candidat — vérifie lettre par lettre : "
     "ف + ك + و + ا + ه), puis le crochet [صحيح مسلم...] en entier, puis la note "
     "حرفه غندر... en entier MOT À MOT (chaque mot : حرفه؟ غندر؟ وقال فيه؟ أبي؟ "
     "وإنما هو؟ أَبِّي بن كعب؟ et la phrase suivante sur أبو جابر/وأدق ...), puis le "
     "renvoi chiffre par chiffre, puis la glose والأكحل en entier."),
    ("z900-p123-hukm-end", "Transcris EXACTEMENT la fin du paragraphe حكم التصحيف "
     "والتحريف visible : à partir de وإذا كثر التصحيف منه... MOT À MOT jusqu'au "
     "point final. Le mot avant المصحف أو المحرف مردود est-il والقدر ؟ فالمصحف ؟ "
     "والمصحف ؟ autre chose ? lis LETTRE PAR LETTRE. Transcris aussi le bouton "
     "أهتدي وأقتدي et la citation s'il est visible."),
    ("z900-p123-ahtadi-taqwim", "Transcris EXACTEMENT tout le texte visible : (1) la "
     "citation sous أهتدي وأقتدي mot à mot avec le crochet final chiffre par chiffre "
     "(التمييد ? التمهيد ? le chiffre 1/70 ?) ; (2) le titre التقويم ; (3) chaque "
     "item numéroté MOT À MOT — item 2 : أبين الفرق بين تصحيف السمع وتصحيف البصر ou "
     "تصحيف الاسم ? LETTRE PAR LETTRE (سمع = ص+م+ع ou اسم = س+م) ; item 3 : que "
     "lis-tu EXACTEMENT (أنطلق؟ أنظر؟ أنسخ؟) après أنطلق من كلام يحيى بن معين — "
     "transcris l'item entier."),
    ("z900-p124-quote", "Transcris EXACTEMENT : (1) la rubrique verte en haut à "
     "droite LETTRE PAR LETTRE (الاستثمار avec ثا أو الاستتمار avec تما — compte les "
     "dents : ث a 3 dents, ت en a 2) ; (2) la citation ENTIRE mot à mot (chaque "
     "clause) ; (3) le crochet final chiffre par chiffre."),
    # --- crops tight R662 ---
    ("t-p120-title", "Transcris EXACTEMENT : (1) le numéro dans le médaillon chiffre "
     "par chiffre ; (2) le titre calligraphié LETTRE PAR LETTRE (المصحف والمحرف ou "
     "الصحف والتحريف ?) ; (3) le label أهداف الدرس s'il est visible."),
    ("t-p120-obj", "Transcris EXACTEMENT les 4 objectifs (items أن ...) ligne par "
     "ligne MOT À MOT. Pour les objectifs 1 et 2, le mot après المصحف والم... est-il "
     "المحرف (avec ميم initiale) ou التحرف ou التحريف ? LETTRE PAR LETTRE : y a-t-il "
     "une ميم en tête du mot après ال ? Compte les dents du ح."),
    ("t-p120-tamhid-1", "Transcris EXACTEMENT les 3 premières lignes du tamhīd MOT À "
     "MOT : (a) après وصونها من التبديل والتغيير le verbe est وبينوا (ب+ي+ن) ou "
     "وميزوا (م+ي+ز) ? LETTRE PAR LETTRE ; (b) le mot после之间 hmm — le nom qui suit "
     "بين ما كانت est المخالفة (avec ميم) ou الخلافَة (sans ميم) ? LETTRE PAR "
     "LETTRE ; (c) transcris la suite jusqu'à اسما خاصا."),
    ("t-p120-matn-ctx", "Transcris EXACTEMENT la citation encadrée en entier avec "
     "ses voyelles : قال الحافظ ابن حجر رحمه الله: «... puis les mots suivants MOT À "
     "MOT jusqu'au guillemet final. Le mot après بقاء est-il السياق ou السُّباق ou "
     "الساق ? LETTRE PAR LETTRE (ش a 3 dents, ب a 1 point en dessous)."),
    ("t-p120-siyaaq-word", "Image zoom MAXIMUM sur les mots بقاء + le mot suivant "
     "dans le متن encadré. Transcris ces mots LETTRE PAR LETTRE avec les points : le "
     "mot après بقاء commence par س... puis a-t-il UNE DENT SEULE + شين à 3 dents "
     "(→ السياق) ou un ب à UN point EN DESSOUS (→ السُّباق) ? Décris chaque lettre "
     "et ses points, puis conclus."),
    ("t-p121-ahamiyya-1", "Transcris EXACTEMENT les 2-3 premières lignes du "
     "paragraphe أهمية معرفة المصحف MOT À MOT : après معرفة هذا النوع مهمة, la "
     "clause suivante est-elle وأكثر وقوعه كان في المتون / كائن في المتون / كان في "
     "المتن / كائن في المتن ? LETTRE PAR LETTRE pour كان vs كائن (y a-t-il un ي avec "
     "2 points sous après ك ا ?) et pour المتون vs المتن (y a-t-il un و entre ت et "
     "ن ?). Puis transcris la suite jusqu'à الأسانيد."),
    ("t-p121-isnad-chain", "Transcris EXACTEMENT l'exemple تصحيف في الإسناد MOT À "
     "MOT : la chaîne complète (1er nom : شعبة ? العوام بن مراجم ? الحوام ? — LETTRE "
     "PAR LETTRE chaque nom), puis le hadith de عثمان بن عفان avec voyelles, puis le "
     "crochet [علل الدارقطني...] chiffre par chiffre."),
    ("t-p121-correction", "Transcris EXACTEMENT la phrase de correction MOT À MOT : "
     "صحف فيه يحيى بن معين، فقال: «ابن مزاحم» — puis la parenthèse (بالزاي والحاء ?) "
     "— puis le verbe après la parenthèse : فرد عليه ou فردّه ou autre ? LETTRE PAR "
     "LETTRE (y a-t-il une شدة sur la ر du verbe ? un ياء final ?) — puis وإنما هو: "
     "«ابن مراجم» — puis la parenthèse suivante — puis le crochet final chiffre par "
     "chiffre."),
    ("t-p121-matan-example", "Transcris EXACTEMENT tout le bloc تصحيف في المتن MOT À "
     "MOT : (1) la ligne d'intro : ما رَواه ابن لهيعة عن «كتاب موسى بن عقبة» puis le "
     "mot suivant : أنه بإسناده عن زيد بن ثابت ou بشّاده ou بإسْتاده ? LETTRE PAR "
     "LETTRE ; (2) la version corrompue «أن رسول الله ﷺ احتجم في السجدة» ; (3) la "
     "version correcte عند مسلم avec voyelles : احتجر رسول الله ﷺ في/حجيرة/حُجرة "
     "بخصفة/بخصيفة أو حصير — LETTRE PAR LETTRE ; (4) le crochet [صحيح مسلم...] en "
     "entier : كتاب صلاة المسافرين أو المسافر ? y a-t-il وقصرها ?وجوازها ou "
     "وجوازهما ? ; (5) la phrase فصحفه ابن لهيعة... ; (6) le crochet final chiffre "
     "par chiffre ; (7) la glose ومعنى «احتجر» en entier."),
    ("t-p122-sam", "Transcris EXACTEMENT le bloc تصحيف السمع MOT À MOT : (1) la "
     "définition قد يكون سببه ضعف السمع... ; (2) le nom du narrateur du حديث : "
     "عاصم الأحول ? LETTRE PAR LETTRE ; (3) la version fausse entre guillemets : عن "
     "واضل الأحذب ou عن واصل الأحدب ou autre ? LETTRE PAR LETTRE (ض = 1 point au "
     "dessus, ص = 3 dents, د vs ذ) — décris les points de chaque lettre ; (4) la "
     "phrase فذكر الدارقطني... jusqu'au crochet final chiffre par chiffre."),
    ("t-p122-maani", "Transcris EXACTEMENT le bloc تصحيف في المعنى MOT À MOT : (1) "
     "la définition بحيث يبقى الراوي المصحّف اللفظ على حاله... ; (2) le récit d'أبي "
     "موسى العنزي en entier ; (3) le crochet [المسند أحمد بن حنبل، حديث ...] — le "
     "NUMÉRO du حديث DIGIT PAR DIGIT (18761 ? 16781 ? 1876 ? — compte les chiffres) "
     "; (4) la clause فتوهم... ; (5) la clause وإنما العَنَزة هنا الحربة... ; (6) le "
     "crochet final [مقدمة ابن الصلاح، ص ...] chiffre par chiffre (387 ? 783 ?)."),
    ("t-p122-luga-tight", "Image zoom MAXIMUM sur le crochet final de la ligne (le "
     "renvoi après «وتحريف الكلام: عدله عن جهته»). Transcris le crochet LETTRE PAR "
     "LETTRE et le numéro DIGIT PAR DIGIT : le glyphe montre-t-il 2/34 ou 2/43 ou "
     "43/2 ? Décris l'ordre VISUEL des chiffres de gauche à droite, puis conclus le "
     "volume et la page."),
    ("t-p123-def53-tight", "Image zoom MAXIMUM sur la fin de la première ligne "
     "(définition المحرف d'ابن حجر). Que voit-on après/by所说的 le mot النسبة إلى شكل "
     "الحروف ? Y a-t-il un numéro de page (53 ?), un crochet [ص 53] ou [نزهة النظر ص "
     "53] ou une note ? Transcris EXACTEMENT tout glyphe visible chiffre par chiffre."),
    ("t-p123-def-line", "Transcris EXACTEMENT la ligne ب- اصطلاحا MOT À MOT en "
     "entier (la définition de المحرف) : بعد المحرف: عرفه ابن حجر بأنه ما كان "
     "التغيير فيه بالنسبة إلى شكل الحروف ou الحرف ? LETTRE PAR LETTRE pour le mot "
     "avant مع بقاء صورة الخط. Et tout renvoi/crochet visible."),
    ("t-p123-jabir", "Transcris EXACTEMENT le hadith de جابر MOT À MOT avec "
     "voyelles : رُمِيَّ / رَمَى ? أَبِي / أَبَى ? يَوْمَ الأَخْرَبِ / الأَحْزَابِ ? "
     "عَلَى الأَكَحِلِ ? puis le mot suivant LETTRE PAR LETTRE (فَكَوَاهُ ? فَكَأَه ? "
     "فَكَأَنَّه ?) puis رسول الله صلى الله عليه وسلم. Puis le crochet [صحيح مسلم، "
     "كتاب السلام، باب ...] MOT À MOT en entier."),
    ("t-p123-ghundar", "Transcris EXACTEMENT la note après le crochet MOT À MOT : "
     "حرفه غندر وقال فيه: «أبي» وإنما هو «أَبِّي بن كعب» ? ou أَبُّي بن كعب ? ou "
     "أَبُو جابر ? LETTRE PAR LETTRE chaque mot (count les shaddas). Puis la phrase "
     "suivante (وأبو جابر كان قد استشهد قبل ذلك ... ? ou أدق ... ?) en entier MOT À "
     "MOT, puis le crochet [مقدمة ابن الصلاح، ص ...] chiffre par chiffre, puis la "
     "glose والأكحل: ... en entier."),
    ("t-p123-hukm", "Transcris EXACTEMENT la fin du paragraphe حكم التصحيف والتحريف "
     "MOT À MOT depuis وإذا كثر التصحيف منه jusqu'au point final : le mot entre "
     "خفيف الضبط et الصحف أو المحرف مردود est-il والقدر ? فالمصحف ? والمصحف ? والقادر "
     "? LETTRE PAR LETTRE (décris chaque lettre et points)."),
    ("t-p123-ahtadi-taqwim", "Transcris EXACTEMENT : (1) la citation sous أهتدي "
     "وأقتدي mot à mot : «آلة المحدث الصدق» ou autre ordre ? LETTRE PAR LETTRE — et "
     "le crochet final : التمييد ou التمهيد ou التمييز ? chiffre par chiffre (1/70 ?) "
     "; (2) le titre التقويم ; (3) chaque item numéroté MOT À MOT — item 2 LETTRE "
     "PAR LETTRE (تصحيف السمع ou تصحيف الاسم ?) ; item 3 en entier."),
    ("t-p124-rubric-tight", "Image zoom MAXIMUM sur la rubrique verte. Transcris "
     "LETTRE PAR LETTRE avec description des dents de chaque lettre : الاستثمار (ث à "
     "3 dents) ou الاستتمار (ت à 2 dents) ou الاستتمام ? Décris puis conclus."),
    ("t-p124-quote", "Transcris EXACTEMENT la citation ENTIRE mot à mot : (1) ouverture "
     "«وأما التصحيف فسبيل السلامة منه الأخذ من أفواه أهل العلم» ; (2) suite après "
     "والضبط clause par clause — y a-t-il وكان أخذه وتعلمه من بطون الكتب ? ou autre "
     "chose ? LETTRE PAR LETTRE pour chaque mot douteux ; (3) fin can من شأنه "
     "التحريف ولم يفلت من التبديل والتصحيف ; (4) crochet final chiffre par chiffre "
     "(ص 218 ?)."),
]


def vision_call(prompt, img, out, tries=5):
    cmd = ["z-ai", "vision", "-p", prompt, "-i", img, "-o", out]
    for t in range(tries):
        r = subprocess.run(cmd, capture_output=True, text=True, timeout=300)
        if r.returncode == 0:
            return True, ""
        err = (r.stderr or "") + (r.stdout or "")
        if "429" in err or "Too many" in err or "rate" in err.lower():
            wait = 45 + 30 * t
            print(f"  429 — attente {wait}s (tentative {t + 1}/{tries})")
            time.sleep(wait)
            continue
        return False, err[:300]
    return False, "429 persistant"


def main():
    for key, q in ASKS:
        img = f"{CROPS}/{key}.png"
        txt_out = f"{CROPS}/read-r662-{key}.txt"
        json_out = f"{CROPS}/_r662-read-{key}.json"
        if os.path.exists(txt_out):
            print("•", key, "déjà lu")
            continue
        ok, err = vision_call(f"{BASE}\nQUESTION : {q}", img, json_out)
        if ok:
            try:
                d = json.load(open(json_out, encoding="utf-8"))
                c = d["choices"][0]["message"]["content"]
                open(txt_out, "w", encoding="utf-8").write(
                    f"IMAGE: {key}.png\nCONSIGNE: {q}\n---\n{c}\n")
                print("✓", key, len(c), "car")
            except Exception as e:
                print("✗", key, "json:", e)
        else:
            print("✗", key, err)


if __name__ == "__main__":
    main()

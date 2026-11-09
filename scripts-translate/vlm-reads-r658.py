# -*- coding: utf-8 -*-
# R658 — lectures VLM bornées des bandes 300 dpi leçon 23 (p.120-125)
# Sortie : tr-tmp/r658/read-<zone>.txt (transcription EXACTE, lettre par lettre)
import json, os, subprocess, time

HOME = "/home/z/my-project"
CROPS = f"{HOME}/tr-tmp/qa-crops-r658"
OUT = f"{HOME}/tr-tmp/r658"
os.makedirs(OUT, exist_ok=True)

BASE = ("Tu lis une image d'un manuel scolaire marocain de hadith (commentaire de la "
        "Naḫbat al-fikr d'Ibn Ḥaǧar, 2e année secondaire). Réponds UNIQUEMENT à la "
        "question posée, par transcription EXACTE du texte imprimé visible, token par "
        "token. Si tu n'es pas sûr d'un mot ou d'un chiffre, écris [illisible]. "
        "N'invente AUCUN texte, ne complète JAMAIS de mémoire (n'utilise PAS de "
        "version canonique d'un texte que tu connaîtrais), ne corrige pas l'imprimé "
        "même s'il te paraît fautif. Transcris aussi les petites gloses marginales "
        "si présentes.")

ASKS = [
    ("p120-banner-objectifs", "Transcris EXACTEMENT, ligne par ligne : (1) le titre de "
     "la bannière (numéro du médaillon + titre calligraphié) ; (2) chaque objectif "
     "entier mot à mot (les items introduits par أن ...) ; (3) le début du tamhīd "
     "(تمهيد) s'il est visible."),
    ("p120-tamhid-matn", "Transcris EXACTEMENT, ligne par ligne, tout le texte visible "
     ": tamhīd (تمهيد) mot à mot, puis la citation en évidence (قال الحافظ ابن حجر...) "
     "avec ses voyelles, puis la question finale."),
    ("p120-fahm", "Transcris EXACTEMENT, ligne par ligne : (1) le titre الفهم et "
     "الشرح ; (2) les gloses ; (3) le titre استخلاص المضامين et chaque item mot à mot "
     "(y compris les gloses en petit caractère comme السّياق)."),
    ("p121-def-musahhaf", "Transcris EXACTEMENT, ligne par ligne : (1) le titre أولا "
     ": الحديث المصحف ; (2) 1. تعريفه (أ- لغة : avec le renvoi entre crochets "
     "chiffre par chiffre, ex. le numéro de page du القاموس المحيط ; ب- اصطلاحا) "
     "entier mot à mot."),
    ("p121-ahamiyya-aqsam", "Transcris EXACTEMENT, ligne par ligne : (1) 2. أهمية "
     "معرفة المصحف entier mot à mot avec la citation de ابن الصلاح et le renvoi "
     "entre crochets (chiffres chiffre par chiffre) ; (2) 3. أقسامه et le début du "
     "premier critère (أ- باعتبار موقعه...)."),
    ("p121-isnad-tasahhif-matan", "Transcris EXACTEMENT, ligne par ligne, tout le "
     "texte visible : (1) l'exemple de تصحيف في الإسناد : la chaîne complète (chaque "
     "nom de transmetteur mot à mot), le texte du hadith de عثمان بن عفان, le "
     "renvoi [علل الدارقطني...] chiffre par chiffre, la correction de يحيى بن معين "
     "(ابن مزاحم / ابن مراجم) et le renvoi [مقدمة ابن الصلاح...] chiffre par "
     "chiffre ; (2) l'exemple de تصحيف في المتن : la chaîne (الليث...), le texte, la "
     "référence à مسلم (كتاب/باب) chiffre par chiffre, la note sur ابن لهيعة, le "
     "renvoi chiffre par chiffre, et la glose ومعنى « احتجر »."),
    ("p122-basr-soli", "Transcris EXACTEMENT, ligne par ligne : l'item تصحيف البصر "
     "(وهو الأكثر...) ENTIER mot à mot : le hadith (مَنْ صَامَ رَمَضَانَ...) avec "
     "ses voyelles lettre par lettre, le renvoi [صحيح مسلم...] avec livre/chapitre "
     "et chiffres, la correction d'أبي بكر الصولي, et le renvoi [مقدمة ابن الصلاح] "
     "chiffre par chiffre."),
    ("p122-sam-asma", "Transcris EXACTEMENT, ligne par ligne : (1) l'item تصحيف "
     "السمع ENTIER mot à mot (les noms propres : عاصم الأحول, واضل الأحذب...) et le "
     "renvoi chiffre par chiffre ; (2) le titre ج- باعتبار لفظه أو معناه et le "
     "début des deux items."),
    ("p122-maani-thaniya-lugha", "Transcris EXACTEMENT, ligne par ligne : (1) l'item "
     "تصحيف في المعنى ENTIER mot à mot (le récit d'أبي موسى العنزي, le renvoi "
     "[المسند...] chiffre par chiffre, la glose sur العنزة الحربة) et le renvoi "
     "[مقدمة ابن الصلاح] chiffre par chiffre ; (2) le titre ثانيا : الحديث المحرف "
     "et 1. تعريفه أ- لغة (le renvoi [مقاييس اللغة...] chiffre par chiffre)."),
    ("p123-muharraf-jabir", "Transcris EXACTEMENT, ligne par ligne : (1) ب- اصطلاحا "
     "(la définition d'ابن حجر) mot à mot — y compris tout numéro de page (ص ...) "
     "chiffre par chiffre qui la suit ; (2) l'exemple : le hadith de جابر (avec ses "
     "voyelles lettre par lettre), le renvoi [صحيح مسلم...] livre/chapitre, la note "
     "(حرفه غندر...) et la glose والأكحل ENTIERES."),
    ("p123-farq", "Transcris EXACTEMENT, ligne par ligne : (1) 2. الفرق بين المصحف "
     "والمحرف ENTIER mot à mot ; (2) 3. حكم التصحيف والتحريف ENTIER mot à mot "
     "(chaque phrase complète)."),
    ("p123-hukm-ahtadi-taqwim", "Transcris EXACTEMENT, ligne par ligne : (1) la fin "
     "de حكم التصحيف والتحريف si visible ; (2) le bouton أهتدي وأقتدي avec la "
     "citation de يحيى بن معين et le renvoi [التمييد...] chiffre par chiffre ; "
     "(3) le titre التقويم et chaque item numéroté mot à mot."),
    ("p124-istithmar", "Transcris EXACTEMENT, ligne par ligne : le titre الاستتمار, "
     "la citation de الإمام ابن الصلاح ENTIERE mot à mot (chaque phrase, avec les "
     "mots ambigus lettre par lettre), et le renvoi [مقدمة ابن الصلاح...] chiffre "
     "par chiffre."),
    ("p124-istikhlas-idad", "Transcris EXACTEMENT, ligne par ligne : (1) l'item "
     "أستخلص من النص... mot à mot ; (2) le titre الإعداد القبلي et chaque item "
     "numéroté mot à mot."),
    ("p125-banner-l24", "Transcris EXACTEMENT, ligne par ligne : (1) le titre de la "
     "bannière (numéro du médaillon + titre calligraphié) ; (2) les objectifs "
     "(items أن...) ; (3) le début du tamhīd (تمهيد) s'il est visible."),
]

def vision_call(prompt, img, out, tries=5):
    cmd = ["z-ai", "vision", "-p", prompt, "-i", img, "-o", out]
    for t in range(tries):
        r = subprocess.run(cmd, capture_output=True, text=True, timeout=300)
        if r.returncode == 0:
            return True, ""
        err = (r.stderr or "") + (r.stdout or "")
        if "429" in err or "Too many" in err:
            wait = 45 + 30 * t
            print(f"  429 — attente {wait}s (tentative {t + 1}/{tries})")
            time.sleep(wait)
            continue
        return False, err[:200]
    return False, "429 persistant"

for key, q in ASKS:
    txt_out = f"{OUT}/read-{key}.txt"
    json_out = f"{OUT}/vlm-{key}.json"
    if os.path.exists(txt_out):
        print("•", key, "déjà lu")
        continue
    ok, err = vision_call(f"{BASE}\nQUESTION : {q}", f"{CROPS}/{key}.png", json_out)
    if ok:
        try:
            d = json.load(open(json_out, encoding="utf-8"))
            c = d["choices"][0]["message"]["content"]
            open(txt_out, "w", encoding="utf-8").write(f"IMAGE: {key}.png\nCONSIGNE: {q}\n---\n{c}\n")
            print("✓", key, len(c), "car")
        except Exception as e:
            print("✗", key, "json:", e)
    else:
        print("✗", key, err)

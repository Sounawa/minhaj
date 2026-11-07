# -*- coding: utf-8 -*-
# R639 — lectures VLM bornées des recadrages d'adjudication (leçon 14, p.74-77)
# Sortie : tr-tmp/r639/read-<zone>.txt (transcription EXACTE, lettre par lettre)
import json, os, subprocess, time

HOME = "/home/z/my-project"
CROPS = f"{HOME}/tr-tmp/qa-crops-r639"
OUT = f"{HOME}/tr-tmp/r639"
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
    ("p074-objectifs", "Transcris EXACTEMENT, ligne par ligne, le titre de la bannière "
     "et la liste des objectifs (أهداف الدرس) visibles : chaque item en entier, mot à "
     "mot, avec sa numérotation si visible."),
    ("p074-gid", "Transcris EXACTEMENT, ligne par ligne, le texte du bouton vert "
     "(titre du bouton + paragraphe qu'il contient + la question double finale)."),
    ("p074-matn", "Transcris EXACTEMENT, lettre par lettre avec les voyelles, la "
     "citation en évidence (قال الحافظ ابن حجر...) : tout le texte imprimé visible, "
     "y compris les gloses marginales en petit caractère s'il y en a."),
    ("p074-istikhlas", "Transcris EXACTEMENT, ligne par ligne : (1) le titre "
     "(استخلاص المضامين ou الشرح) ; (2) les items numérotés ; (3) les gloses en petit "
     "caractère intercalées (السقط... الطعن... المصنف...) mot à mot."),
    ("p075-tahlil-s1", "Transcris EXACTEMENT, ligne par ligne, le titre (التحليل) et "
     "la première section (أولا : أسباب رد الحديث) ENTIERE : chaque phrase mot à mot, "
     "y compris la citation en retrait de Ibn Ḥaǧar et les gloses marginales."),
    ("p075-sabab2", "Transcris EXACTEMENT, ligne par ligne, la section (السبب الثاني : "
     "الطعن في الرواة) ENTIERE mot à mot, y compris les gloses marginales."),
    ("p075-muallaq-def", "Transcris EXACTEMENT, ligne par ligne : (1) le titre "
     "(ثانيا : الحديث المعلق) et تعريفه (أ- لغة / ب- اصطلاحا) ENTIER mot à mot avec "
     "le renvoi bibliographique entre crochets (chiffres chiffre par chiffre) ; "
     "(2) toute glose marginale en petit caractère."),
    ("p075-farq", "Transcris EXACTEMENT, ligne par ligne, l'item (2- الفرق بين المعلق "
     "والمعضل...) ENTIER mot à mot jusqu'à la fin de la page, y compris les gloses "
     "marginales en petit caractère."),
    ("p076-band", "Transcris EXACTEMENT tout ce qui est visible sur cette bande "
     "(bouton vert ou bandeau de titre) — mot à mot."),
    ("p076-suwar", "Transcris EXACTEMENT, ligne par ligne, la section (صور الحديث "
     "المعلق) ENTIERE : les trois items (أ/ب/ج ou tirets) mot à mot jusqu'à la fin."),
    ("p076-hukm", "Transcris EXACTEMENT, ligne par ligne, la section (حكم الحديث "
     "المعلق) ENTIERE mot à mot, y compris la citation de Ibn aṣ-Ṣalāḥ et le renvoi "
     "entre crochets (chiffres chiffre par chiffre)."),
    ("p076-zuhri", "Transcris EXACTEMENT, ligne par ligne, la section (أهتدي وأقتدي) "
     "avec sa citation (قال الإمام ابن شهاب الزهري...) mot à mot + renvoi entre "
     "crochets chiffre par chiffre."),
    ("p077-taqwim", "Transcris EXACTEMENT, ligne par ligne, le titre (التقويم) et "
     "chaque item numéroté en entier mot à mot, y compris tout texte imprimé entre "
     "les items (citation, gloses)."),
    ("p077-istithmar", "Transcris EXACTEMENT, ligne par ligne, tout ce qui est "
     "visible : titres de rubriques (boutons verts), citation du texte (قال الإمام "
     "ابن الصلاح...) mot à mot avec renvoi entre crochets chiffre par chiffre, et "
     "les items numérotés."),
    ("p077-ahtadi", "Transcris EXACTEMENT, ligne par ligne, tout ce qui est visible : "
     "le bouton vert de titre (أهتدي وأقتدي ou autre) et les items numérotés mot à "
     "mot jusqu'à la fin de la page."),
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

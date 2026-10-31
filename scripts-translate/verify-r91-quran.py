#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Minhāj R91 — Audit complet des labels de versets-image de hadith-1es.

Trois contrôles par leçon porteuse d’images-versets :
  (a) captions du src (miroir habous.gov.ma, harakat écrêtées) ↔ labels FR attendus
      (carte des coquilles documentée : المائدة 7→6, البقرة 220→222, الطور 33-35→35-37) ;
  (b) texte FR du label ↔ cache quranique (extraits de contrôle) ;
  (c) hygiène typographique : 0 caractère arabe, 0 apostrophe droite, guillemets appariés.
"""
import json
import re

TMP = "/home/z/my-project/tr-tmp"
CACHE = "/home/z/my-project/scripts-translate/quran-cache.json"
AR_RE = re.compile(r"[\u0600-\u06FF\u0750-\u077F\u08A0-\u08FF\uFB50-\uFDFF\uFE70-\uFEFF]")
HARAKAT = re.compile(r"[\u064B-\u065F\u0670\u0640\u06D6-\u06ED]")

# Carte src (caption normalisée) → label FR attendu APRÈS correction documentée.
# Normalisation src : « سورة المائدة: الآية 7 » → ('المائدة', '7') ; plage « 33 – 35 » → '33-35'.
SRC_TO_FR = {
    "المائدة": ("al-Māʾida (5)", {"7": "6"}),          # coquille off-by-ONE (map image 202, R63-R65)
    "البقرة": ("al-Baqara (2)", {"220": "222"}),        # coquille off-by-TWO (map image 200, R63-R65)
    "التوبة": ("al-Tawba (9)", {}),
    "النساء": ("al-Nisāʾ (4)", {}),
    "الجمعة": ("al-Jumuʿa (62)", {}),
    "محمد": ("Muḥammad (47)", {}),
    "الواقعة": ("al-Wāqiʿa (56)", {}),
    "طه": ("Ṭāhā (20)", {}),
    "الذاريات": ("al-Dhāriyāt (51)", {}),
    "الإسراء": ("al-Isrāʾ (17)", {}),
    "يونس": ("Yūnus (10)", {}),
    "آل عمران": ("Āl ʿImrān (3)", {}),
    "الإنسان": ("al-Insān (76)", {}),
    "الطور": ("al-Ṭūr (52)", {"33-35": "35-37"}),       # coquille off-by-TWO (Bukhārī 4854/Muslim 463)
    "الحجر": ("al-Ḥijr (15)", {}),
    "الأنفال": ("al-Anfāl (8)", {}),
    "الأعراف": ("al-Aʿrāf (7)", {}),
    "المرسلات": ("al-Mursalāt (77)", {}),
    "الانشقاق": ("al-Inshiqāq (84)", {}),
}

# Leçons porteuses d’images-versets (src captions attendues en ordre de parution).
LESSONS = {
    "12875": ["المائدة 7", "النساء 2", "المائدة 7"],
    "12884": ["البقرة 220", "التوبة 109"],
    "12885": ["المائدة 7", "المائدة 7"],
    "12908": ["المائدة 7", "النساء 43", "النساء 29", "المائدة 7", "المائدة 7"],
    "12924": ["البقرة 220"],
    "12929": ["الجمعة 9", "المائدة 60"],
    "12948": ["محمد 34"],
    "12953": ["آل عمران 8", "الإنسان 6", "الطور 33-35", "المرسلات 1", "الانشقاق 1"],
    "12961": ["البقرة 105", "الحجر 87", "الأنفال 24", "الأعراف 204"],
    "12980": ["يونس 89"],
    "12985": ["الواقعة 77"],
    "12995": ["الجمعة 9"],
    "13001": ["طه 131"],
    "13002": ["الذاريات 17", "الإسراء 79"],
}

FR_TAIL_RE = re.compile(r"^([^: ]+?) : (\d+(?:–\d+)?)(, extrait)?\]")

# Extraits de contrôle cache (Hamidullah) — sous-chaînes clés attendues dans les labels FR.
FR_SNIPPETS = {
    "12875-0": ("5", 6, "lavez vos visages"),
    "12875-1": ("4", 2, "orphelins"),
    "12875-2": ("5", 6, "lavez vos visages"),
    "12884-0": ("2", 222, "aime ceux qui se purifient"),
    "12884-1": ("9", 109, "édifice"),
    "12885-0": ("5", 6, "lavez vos visages"),
    "12885-1": ("5", 6, "lavez vos visages"),
    "12908-0": ("5", 6, "lavez vos visages"),
    "12908-1": ("4", 43, "ivres"),
    "12908-2": ("4", 29, "ne vous tuez pas"),
    "12908-3": ("5", 6, "lavez vos visages"),
    "12908-4": ("5", 6, "lavez vos visages"),
    "12924-0": ("2", 222, "aime ceux qui se purifient"),
    "12929-0": ("62", 9, "jour de l’assemblée"),
    "12929-1": ("5", 60, "singes"),
    "12948-0": ("47", 34, "détourné du chemin de Dieu"),
    "12953-0": ("3", 8, "ne fais pas d\u00e9vier nos c\u0153urs"),
    "12953-1": ("76", 6, "source dont boivent les serviteurs de Dieu"),
    "12953-2": ("52", 35, "cr\u00e9ateurs"),
    "12953-4": ("84", 1, "ciel"),
    "12961-0": ("2", 105, "gens du Livre"),
    "12961-1": ("15", 87, "sept répétés"),
    "12961-2": ("8", 24, "Répondez"),
    "12961-3": ("7", 204, "récite le Qurʾān"),
    "12980-0": ("10", 89, "votre invocation est exaucée"),
    "12985-0": ("56", 77, "Qurʾān noble"),
    "12995-0": ("62", 9, "jour de l’assemblée"),
    "13001-0": ("20", 131, "ne détourne pas tes yeux"),
    "13002-0": ("51", 17, "dormaient peu"),
    "13002-1": ("17", 79, "veille surérogatoire"),
}


def norm_caption(raw: str) -> str:
    """« سُورَةُ النِّسَاءِ: الْآيَةُ 2 » → « النساء 2 » (harakat écrêtées)."""
    s = HARAKAT.sub("", raw)
    s = s.replace("&nbsp;", " ")
    s = s.replace("سورة", " ").replace("سور", " ")
    s = s.replace("الآية", " ").replace("آية", " ")
    s = s.replace(":", " ").replace("\u060c", " ")
    s = s.replace("اا", "ا")  # artefact OCR « االبقرة »
    s = re.sub(r"(\d+)\s*[-–]\s*(\d+)", r"\1-\2", s)
    s = re.sub(r"\s+", " ", s).strip()
    return s


def extract_src_captions(did: str):
    src = HARAKAT.sub("", open(f"{TMP}/{did}.src.html", encoding="utf-8").read())
    raws = re.findall(r"<span>([^<]*سور[^<]*)</span>", src)
    out = []
    for raw in raws:
        s = norm_caption(raw)
        m = re.match(r"^([\u0600-\u06FF]+(?: [\u0600-\u06FF]+)?) (\d+(?:-\d+)?)$", s)
        if m:
            out.append(f"{m.group(1)} {m.group(2)}")
    return out


def extract_fr_labels(did: str):
    fin = open(f"{TMP}/{did}.html", encoding="utf-8").read()
    lines = [ln for ln in fin.splitlines()
             if ln.startswith("<p>[verset reproduit en image dans le manuel") and ln.endswith("</p>")]
    out = []
    for line in lines:
        tail = line.rsplit(" — ", 1)[-1]  # dernier em-dash = séparateur de l’origine
        m = FR_TAIL_RE.match(tail)
        if m:
            out.append((m.group(1).strip(), m.group(2), bool(m.group(3)), line))
    return out


def cache_text(s: str, a: int) -> str:
    q = json.load(open(CACHE, encoding="utf-8"))
    for num, txt in q[s]["fr"]:
        if int(num) == a:
            return txt
    return ""


def main() -> None:
    failures = 0

    # (a) captions src ↔ carte attendue
    print("== (a) captions src ↔ carte documentée ==")
    for did, expected in LESSONS.items():
        got = extract_src_captions(did)
        ok = got == expected
        print(f"{did} : src {'OK' if ok else 'DIFF'}")
        if not ok:
            failures += 1
            print(f"   attendu {expected}")
            print(f"   trouvé  {got}")

    # (b) labels FR ↔ coquilles corrigées + cache
    print("== (b) labels FR (après correction) ↔ cache ==")
    for did, caps in LESSONS.items():
        labels = extract_fr_labels(did)
        if len(labels) != len(caps):
            print(f"{did} : ✗ {len(labels)} labels FR pour {len(caps)} captions")
            failures += 1
            continue
        for i, (name, num, extrait, raw) in enumerate(labels):
            cap = caps[i]
            soura, ver = cap.rsplit(" ", 1)
            fr_name, fixmap = SRC_TO_FR[soura]
            expected_num = fixmap.get(ver, ver)
            exp_name = fr_name
            # plage corrigée : « 33-35 » → « 35-37 » donnée explicitement
            if soura == "الطور":
                exp_name, expected_num = "al-Ṭūr (52)", "35\u201337"
            ok_name = name == exp_name
            ok_num = num == expected_num
            if not (ok_name and ok_num):
                failures += 1
                print(f"{did}[{i}] : ✗ FR « {name} : {num} » ≠ attendu « {exp_name} : {expected_num} » (src {cap})")
        # snippet cache sur les 5 leçons clés corrigées
        for i in range(len(caps)):
            key = f"{did}-{i}"
            if key not in FR_SNIPPETS:
                continue
            s, a, frag = FR_SNIPPETS[key]
            ct = cache_text(s, a)
            labels2 = extract_fr_labels(did)
            raw = labels2[i][3]
            if frag.lower() not in raw.lower() and frag not in ct:
                failures += 1
                print(f"{key} : ✗ fragment « {frag} » absent du label ET du cache")

    # (c) hygiène typographique des 4 leçons corrigées
    print("== (c) hygiène typographique (leçons corrigées) ==")
    for did in ("12875", "12885", "12908", "12953"):
        text = open(f"{TMP}/{did}.html", encoding="utf-8").read()
        ar = AR_RE.findall(text)
        straight = text.count("'")
        guo, guf = text.count("«"), text.count("»")
        ok = not ar and straight == 0 and guo == guf
        print(f"{did} : arabe {len(ar)} | apostrophes droites {straight} | guillemets {guo}/{guf} → {'OK' if ok else '✗'}")
        if not ok:
            failures += 1

    # assertions ciblées R91
    print("== (d) assertions ciblées R91 ==")
    checks = [
        ("12875", "al-Māʾida (5)\u202f: 7", 0),
        ("12875", "al-Māʾida (5)\u202f: 6", 2),
        ("12885", "al-Māʾida (5)\u202f: 7", 0),
        ("12885", "al-Māʾida (5)\u202f: 6", 2),
        ("12908", "al-Māʾida (5)\u202f: 7", 0),
        ("12908", "al-Māʾida (5)\u202f: 6", 3),
        ("12953", "33\u201335", 0),
        ("12953", "35\u201337", 1),
        ("12953", "impulsion de la passion", 0),
        ("12953", "eau bouillante", 0),
        ("12953", "source dont boivent les serviteurs de Dieu", 1),
        ("12953", "les créateurs ?", 1),
    ]
    for did, frag, expect in checks:
        n = open(f"{TMP}/{did}.html", encoding="utf-8").read().count(frag)
        ok = n == expect
        print(f"{did} : « {frag} » ×{n} (attendu {expect}) → {'OK' if ok else '✗'}")
        if not ok:
            failures += 1

    print()
    print("RÉSULTAT :", "PASS — audit des labels de versets-image complet" if failures == 0 else f"FAIL ({failures} échec(s))")
    raise SystemExit(0 if failures == 0 else 1)


if __name__ == "__main__":
    main()

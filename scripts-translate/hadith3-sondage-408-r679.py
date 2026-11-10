# -*- coding: utf-8 -*-
"""Minhāj — Sondage bornes leçon 408 hadith-3es (R679, slot pdf-mut23h2x-408,
ما يفعله الحاج يوم النحر « Les rites du pèlerin au jour du sacrifice »).
Bannière cours 18 p.129 (médaillon « 19 ») d'après R673 (« bannière cours 18
sondée en p.129 »). On sonde p.129-145 : premières lignes VUE LISIBLE +
détection أهداف الدرس (objectifs de la leçon suivante → borne sup exclusive),
أحفظ (bannière de cours), chiffres isolés (médaillons)."""
import fitz

PDF = "/home/z/my-project/content/textbooks-src/hadith-3-iadadi_text.pdf"
FIRST, LAST = 129, 145

doc = fitz.open(PDF)


def fix_line(s: str) -> str:
    return " ".join(w[::-1] for w in s.split())


def decode_page(p):
    page = doc[p]
    d = page.get_text("dict")
    out = []
    for b in d["blocks"]:
        if b.get("type") != 0:
            continue
        for l in b["lines"]:
            txt = "".join(s["text"] for s in l["spans"]).strip()
            if txt:
                out.append((round(b["bbox"][0], 1), round(l["bbox"][1], 1), round(l["bbox"][2], 1), txt))
    return out


for p in range(FIRST - 1, min(LAST, doc.page_count)):
    lines = decode_page(p)
    lines.sort(key=lambda t: (round(t[1] / 8), -t[2]))
    read = [fix_line(t) for _, _, _, t in lines]
    joined = "\n".join(read)
    flags = []
    if "أهداف الدرس" in joined:
        flags.append("!! أهداف الدرس (objectifs)")
    if "أحفظ" in joined:
        flags.append("أحفظ (bannière)")
    if "يوم النحر" in joined or "النحر" in joined:
        flags.append("!! النحر (titre 408)")
    for t in read[:8]:
        if t.strip().isdigit() or (len(t.strip()) <= 3 and any(c.isdigit() for c in t)):
            flags.append(f"chiffre isolé: {t.strip()}")
    print(f"===== PAGE {p + 1} {('[' + ' ; '.join(flags) + ']') if flags else ''} =====")
    for t in read[:14]:
        print("  " + t)
    print()

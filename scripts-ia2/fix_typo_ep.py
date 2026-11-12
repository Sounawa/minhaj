#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Auto-fix typographique des htmlFr des livres du PRIMAIRE (zone IA-2).

Réplique exactement l'auto-fix de scripts-translate/qa-lesson.py (règles du projet) :
  - apostrophe droite ' -> U+2019 (nœuds texte uniquement)
  - espace avant ; : ! ? » -> U+202F (NNBSP), après « -> U+202F
  - doubles espaces -> simple
Ajout IA-2 (convention majoritaire du corpus, 167 vs 37 occurrences) :
  - hamza de translittération : voyelle longue + ' final de mot -> U+02BE (ʾ)
N'écrit que si le doc change. Les leçons pdfOnly sans htmlFr sont ignorées.
"""
import json, os, re, sys

NB = "\u202f"
LONGV = "āīūāĪŪĀĪŪ"

def fix_text_node(t: str) -> str:
    entities: list = []

    def _protect(m):
        entities.append(m.group(0))
        return f"\x00{len(entities) - 1}\x00"

    t = re.sub(r"&[a-zA-Z]+;|&#\d+;", _protect, t)
    # 1. apostrophe droite -> typographique
    t = t.replace("'", "\u2019")
    # 2. hamza de translittération : voyelle longue + ’ en fin de mot -> ʾ
    t = re.sub(rf"[{LONGV}]\u2019(?=[ \u00a0\u202f,.;:!?»)…<]|$)", "ʾ", t)
    # 3. espace avant ;:!?" -> NNBSP
    t = re.sub(r"[ \u00a0\u202f]*([;:!?»])", NB + r"\1", t)
    # 4. espace après « -> NNBSP
    t = re.sub(r"«[ \u00a0\u202f]*", "«" + NB, t)
    # 5. doubles espaces -> simple
    t = re.sub(r" {2,}", " ", t)
    t = re.sub(r"\x00(\d+)\x00", lambda m: entities[int(m.group(1))], t)
    return t

def fix_html(html: str) -> str:
    # passe HTML : hamza finale après balise em — « ā</em>' » -> « ā</em>ʾ »
    # (convention dominante du corpus : 10 308 cas ; le savant récent écrit ʾ)
    html = re.sub(rf"([{LONGV}])</em>['\u2019]", r"\1</em>ʾ", html)
    parts = re.split(r"(<[^>]+>)", html)
    out = []
    for p in parts:
        out.append(fix_text_node(p) if not p.startswith("<") else p)
    return "".join(out)

def main():
    dry = "--dry" in sys.argv
    total_docs, changed_docs = 0, 0
    stats = {"apostrophes": 0, "hamza": 0, "nnbsp": 0, "double_espaces": 0}
    for fn in sorted(os.listdir("content/books")):
        b = json.load(open(f"content/books/{fn}"))
        if not b["level"].endswith("ep"):
            continue
        raw = open(f"content/books/{fn}").read()
        dirty = False
        docs = ([b["intro"]] if b.get("intro") else []) + b.get("lessons", [])
        for d in docs:
            if not d or not (d.get("htmlFr") or "").strip():
                continue
            total_docs += 1
            fr = d["htmlFr"]
            nfx = fix_html(fr)
            if nfx == fr:
                continue
            # stats approximatives (sur le texte AVANT fix)
            stats["apostrophes"] += fr.count("'")
            stats["hamza"] += len(re.findall(rf"[{LONGV}][\u2019'](?=[ \u00a0\u202f,.;:!?»)…<]|$)", fr))
            stats["double_espaces"] += len(re.findall(r" {2,}", fr))
            d["htmlFr"] = nfx
            changed_docs += 1
            dirty = True
        if dirty and not dry:
            out = json.dumps(b, ensure_ascii=False, indent=2)
            with open(f"content/books/{fn}", "w", encoding="utf-8") as fh:
                fh.write(out)
            print(f"  {fn}: corrigé")
    print(f"\nDocs examinés: {total_docs} | modifiés: {changed_docs}")
    print(f"stats: {stats}")
    if dry:
        print("(mode --dry : rien écrit)")

if __name__ == "__main__":
    main()

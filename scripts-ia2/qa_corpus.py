#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""QA typographique de tous les htmlFr du corpus Minhaj (scanne les livres JSON).

Règles tirées de scripts-translate/qa-lesson.py (conventions du projet) :
  DUR : arabe hors <span>, apostrophes droites ', guillemets « » non appariés,
       balises appariées déséquilibrées.
  SOFT : espace avant ;:!?»  et après «  (devrait être U+202F), doubles espaces,
       espaces intérieurs aux parenthèses "( x )".
Usage :
  python3 qa_corpus.py                 -> rapport global, toutes zones
  python3 qa_corpus.py --zone primaire -> ne scanne que les niveaux ep
"""
import json, os, re, sys

AR = re.compile(r"[\u0600-\u06FF\u0750-\u077F\u08A0-\u08FF\uFB50-\uFDF9\uFDFB-\uFDFF\uFE70-\uFEFF]")

def text_nodes(html):
    """Rend les fragments texte (hors balises et hors spans arabe déclarés).
    Chaque span arabe -> 1 marqueur \\x01, chaque balise -> \\x00 : aucun espace
    artificiel n'est créé ni fusionné (les espaces réelles du document sont
    préservées à l'identique)."""
    html2 = re.sub(r'<span[^>]*dir="rtl"[^>]*>.*?</span>', '\x01', html, flags=re.S)
    html2 = re.sub(r'<span[^>]*lang="ar"[^>]*>.*?</span>', '\x01', html2, flags=re.S)
    html2 = re.sub(r'<(script|style)[^>]*>.*?</\1>', ' ', html2, flags=re.S)
    return re.sub(r'<[^>]+>', '\x00', html2)

def check(html):
    hard, soft = [], []
    if not html or not html.strip():
        return hard, soft
    t = text_nodes(html)
    n_ar = len(AR.findall(t))
    if n_ar:
        hard.append(f"arabe_hors_span:{n_ar}")
    n_ap = t.count("'")
    if n_ap:
        hard.append(f"apostrophe_droite:{n_ap}")
    n_open, n_close = html.count("«"), html.count("»")
    if n_open != n_close:
        hard.append(f"guillemets:{n_open}«/{n_close}»")
    for tag in ["h1","h2","h3","h4","p","ul","ol","li","table","tr","td","th",
                "blockquote","strong","em","b","i","sup","sub","dl","dt","dd"]:
        o = len(re.findall(rf"<{tag}[ >]", html))
        c = len(re.findall(rf"</{tag}>", html))
        if o != c:
            hard.append(f"balise_{tag}:{o}o/{c}f")
    h = re.sub(r"&[a-zA-Z]+;|&#\d+;", " ", html)
    n1 = len(re.findall(r"[ \u00a0][;:!?»]", h))
    if n1:
        soft.append(f"espace_avant_ponc:{n1}")
    n2 = len(re.findall("«[ \u00a0]", h))
    if n2:
        soft.append(f"espace_apres_guillemet_ouvrant:{n2}")
    n3 = len(re.findall(r" {2,}", t))
    if n3:
        soft.append(f"double_espace:{n3}")
    n4 = len(re.findall(r"\( +| +\)", t))
    if n4:
        soft.append(f"paren_espaces:{n4}")
    return hard, soft

def main():
    zone = "primaire" if ("--zone" in sys.argv and "primaire" in sys.argv) else "tout"
    reg = json.load(open("scripts-translate/savant-registry.json"))
    hand = set(reg.get("hand", []))
    llm = reg.get("llm", {}); llm = set(llm if isinstance(llm, dict) else llm)
    rows = []
    for fn in sorted(os.listdir("content/books")):
        b = json.load(open(f"content/books/{fn}"))
        if zone == "primaire" and not b["level"].endswith("ep"):
            continue
        docs = ([b["intro"]] if b.get("intro") else []) + b.get("lessons", [])
        for d in docs:
            if not d:
                continue
            hard, soft = check(d.get("htmlFr") or "")
            if hard or soft:
                sav = "hand" if d["docId"] in hand else ("llm" if d["docId"] in llm else "GT")
                rows.append((b["id"], d["docId"], d.get("titleFr", "")[:50], sav,
                             "; ".join(hard), "; ".join(soft)))
    hard_n = sum(1 for r in rows if r[4])
    print(f"{'livre':<22} {'docId':<7} {'reg':<5} {'DEFAUTS DURS':<40} SOFT")
    for r in rows:
        print(f"{r[0]:<22} {r[1]:<7} {r[3]:<5} {r[4]:<40} {r[5]}")
    print(f"\nDocs avec défauts: {len(rows)} | avec défauts DURS: {hard_n}")

if __name__ == "__main__":
    main()

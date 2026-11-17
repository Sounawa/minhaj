#!/usr/bin/env python3
"""Extraction non lossy des leçons pdf-mut23h2x-394 et pdf-mut23h2x-393 (hadith-3es)
pour rédaction des commentaires pédagogiques vague 13.
Lit site/livres/hadith-3es/*.html (rendu = contenu htmlFr du livre), sort les
blocs complets h2/h3/p/li/td en texte lisible."""
import re, html, sys

BASE = "/home/z/my-project/minhaj-repo/site/livres/hadith-3es/"
DOCS = ["pdf-mut23h2x-394", "pdf-mut23h2x-393"]

def main_html(page_html):
    # zone utile : entre le h1 du document et le pied de page
    m = re.search(r"<main[^>]*>(.*)</main>", page_html, re.S)
    return m.group(1) if m else page_html

def texte_page(path):
    raw = open(path, encoding="utf-8").read()
    main = main_html(raw)
    out = []
    # ordre du document : capturer les blocs dans l'ordre
    for m in re.finditer(r"<(h2|h3|h4|p|li|td)[^>]*>(.*?)</\1>", main, re.S):
        tag, inner = m.group(1), m.group(2)
        # retirer les balises internes mais garder les spans RTL comme [ar: …]
        def rtl_sub(mm):
            return " ⟨ar⟩ " + html.unescape(re.sub(r"<[^>]+>", "", mm.group(1))) + " ⟨/ar⟩ "
        t = re.sub(r'<span[^>]*dir="rtl"[^>]*>(.*?)</span>', rtl_sub, inner, flags=re.S)
        t = re.sub(r"<[^>]+>", "", t)
        t = html.unescape(t)
        t = re.sub(r"[ \t]+", " ", t).strip()
        if not t:
            continue
        prefix = {"h2": "## ", "h3": "### ", "h4": "#### "}.get(tag, "")
        out.append(prefix + t)
    return out

for doc in DOCS:
    blocks = texte_page(BASE + doc + ".html")
    dst = "/home/z/my-project/scripts/extrait-r729-%s.txt" % doc
    with open(dst, "w", encoding="utf-8") as f:
        f.write("\n".join(blocks))
    print(doc, "->", dst, len(blocks), "blocs,", sum(len(b) for b in blocks), "car.")

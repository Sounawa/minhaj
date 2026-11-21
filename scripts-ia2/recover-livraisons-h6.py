#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# IA-2 — RÉCUPÉRATION Z2-49 : reconstruction des livraisons 688-691 de hadith-6ep.
# Contexte : les tours Z2-43→Z2-48 (leçons 8-12) ont été livrés sur le disque mais
# leurs commits ont été perdus lors des resets du bac (aucun token pour pousser).
# Le snapshot plateforme a survécu avec : JSON complet (htmlFr posé par hand-set-ia2.py,
# POST-soudage des FLAGS Z2-46), worklog jusqu'à Z2-48, registre 41, livraison 692 et
# les scripts h6-13 (Z2-48) — mais SANS les fichiers livraisons 688-691.
# hand-set-ia2.py pose le fichier livraison dans le JSON À L'IDENTIQUE : l'opération
# inverse (dump htmlFr → fichier) restitue donc le contenu exact de la livraison.
# Z2-46 a soudé des FLAGS sur L8/L9/L10 : les tailles JSON (25519/26747/25516/23373)
# sont post-soudage et font foi (les tailles des entrées worklog Z2-43/44 — 25573/26668 —
# sont antérieures au soudage ; L11/L12 inchangées : 23373/21484 concordent).
import json, os, sys

REPO = "/home/z/my-project/minhaj"
BOOK = f"{REPO}/content/books/hadith-6ep.json"
OUTDIR = f"{REPO}/scripts-ia2/livraisons/hadith-6ep"
TARGETS = ["pdf-mut23h3b-688", "pdf-mut23h3b-689", "pdf-mut23h3b-690", "pdf-mut23h3b-691"]

def main():
    with open(BOOK, encoding="utf-8") as fh:
        data = json.load(fh)
    for doc_id in TARGETS:
        lesson = next((l for l in data.get("lessons", []) if l.get("docId") == doc_id), None)
        if lesson is None:
            sys.exit(f"ABSENT du JSON : {doc_id}")
        html = lesson.get("htmlFr") or ""
        if not html.strip():
            sys.exit(f"htmlFr VIDE : {doc_id}")
        out = os.path.join(OUTDIR, doc_id + ".html")
        if os.path.exists(out):
            with open(out, encoding="utf-8") as fh:
                if fh.read() == html:
                    print(f"OK déjà identique : {doc_id} ({len(html)} car)")
                    continue
                sys.exit(f"REFUS : {out} existe et diffère du JSON")
        with open(out, "w", encoding="utf-8") as fh:
            fh.write(html)
        print(f"RECONSTITUÉ : {doc_id} ({len(html)} car) → {out}")

if __name__ == "__main__":
    main()

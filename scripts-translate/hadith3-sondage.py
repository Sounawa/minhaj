#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Minhāj — SONDAGE HADITH-3-IADADI (R624) : repérage des bannières de leçons du
manuel « al-Ḥadīth min Muwaṭṭaʾ al-imām Mālik bi-Šarḥ az-Zarqānī » 3ᵉ année
iadadi (196 p. miroir) ↔ livre portail hadith-3es (slots pdf-mut23h2x-390..418).
Mécanique hadith2-map.py : fix_line décode les mots inversés ; la couche OCR
inverse AUSSI les chiffres par paires — jamais de borne devinée, sondage obligé.
Marqueurs : أهداف الدرس (ouverture de leçon) et الإعداد القبلي (clôture).
"""
import fitz

PDF = "/home/z/my-project/content/textbooks-src/hadith-3-iadadi_text.pdf"


def fix_line(s: str) -> str:
    return " ".join(w[::-1] for w in s.split())


def main() -> None:
    doc = fitz.open(PDF)
    for p in range(1, len(doc) + 1):
        raw = doc[p - 1].get_text()
        fixed = "\n".join(fix_line(l) for l in raw.split("\n"))
        hits = []
        if "أهداف الدرس" in fixed or "اهداف الدرس" in fixed:
            hits.append("أهداف الدرس")
        if "الإعداد القبلي" in fixed:
            hits.append("الإعداد القبلي")
        # bannière « الدرس N » (numéro OCR fiable seulement par recadrage)
        if "الدرس" in fixed and "أهداف" not in fixed and len(fixed) < 800:
            hits.append("bannière courte?")
        if hits:
            print(f"p.{p:3d} {hits} — {len(raw)} car")
            for l in fixed.split("\n"):
                if any(h in l for h in hits):
                    print(f"      ↳ {l.strip()[:110]}")


if __name__ == "__main__":
    main()

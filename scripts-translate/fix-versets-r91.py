#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Minhāj R91 — Correction des labels de versets-image de hadith-1es (relecture croisée src ↔ FR ↔ cache).

Corrections (doctrine établie R62-R65 : coquilles de captions du manuel, correction silencieuse
dans le texte, documentée au worklog/commit) :
  1. al-Māʾida (5) : 7 → 6   ×7  (12875 ×2, 12885 ×2, 12908 ×3) — le verset des ablutions est 5:6,
     texte FR cité = 5:6, cache confirmé ; coquille off-by-ONE du manuel (déjà corrigée dans
     ulum-quran-1es, map image 202, worklog R63-R65).
  2. 12953 image 1 — citation remplacée : le texte FR actuel (« …et ils n’en boiront pas avant
     d’une eau bouillante et troublée ») est celui de al-Nabaʾ 78:24-25, PAS de al-Insān 76:6
     (caption du manuel, stable dans le src) ; le rôle de l’image = parallèle du bāʾ bimāʿnā min
     (Ibn al-Jawzī) — et 76:6 « يَشْرَبُ بِهَا » est LE verset classique du bāʾ = min (tafsīr).
     Citation rendue sur le cache Hamidullah adapté à la maison.
  3. 12953 image 2 — citation + référence remplacées : le texte FR actuel (« …il ne parle pas
     sous l’impulsion de la passion ») est celui de al-Naǧm 53:3, PAS de al-Ṭūr ; l’āya de la
     narration de Jubayr (al-Bukhārī 4854, Muslim 463 — « فلما بلغ هذه الآية… طارت بقلبي ») est
     Ṭūr 35-37 ; caption imprimée « 33 – 35 » = coquille off-by-TWO du manuel, même signature
     que Baqara 220→222 et Ḥaǧǧ 75→77 (worklog R63-R65). Réf rendue 35-37, citation = cache.
"""
import re

TMP = "/home/z/my-project/tr-tmp"
NN = "\u202f"
DA = "\u2014"  # em-dash
EN = "\u2013"  # en-dash (ranges)

# --- 1. Māʾida 7 → 6 -------------------------------------------------------
MAIDA_OLD = f"al-Māʾida (5){NN}: 7"
MAIDA_NEW = f"al-Māʾida (5){NN}: 6"
MAIDA_COUNTS = {"12875": 2, "12885": 2, "12908": 3}

# --- 2. 12953 Insān 6 ------------------------------------------------------
INSAN_OLD = (
    "<p>[verset reproduit en image dans le manuel"
    f"{NN}: «{NN}…et ils n’en boiront pas avant d’un eau bouillante et troublée.{NN}» — al-Insān (76){NN}: 6]</p>"
)
INSAN_NEW = (
    "<p>[verset reproduit en image dans le manuel"
    f"{NN}: «{NN}une source dont boivent les serviteurs de Dieu {DA} et qu’ils font jaillir en abondance.{NN}» — al-Insān (76){NN}: 6]</p>"
)

# --- 3. 12953 Ṭūr 33–35 → 35–37 -------------------------------------------
TUR_OLD = (
    "<p>[verset reproduit en image dans le manuel"
    f"{NN}: «{NN}…il ne parle pas sous l’impulsion de la passion{NN}» — al-Ṭūr (52){NN}: 33{EN}35]</p>"
)
TUR_NEW = (
    "<p>[verset reproduit en image dans le manuel"
    f"{NN}: «{NN}Ou bien ont-ils été créés à partir de rien, ou sont-ils eux-mêmes les créateurs ? "
    f"ou bien ont-ils créé les cieux et la terre {DA} mais plutôt, ils n’ont aucune conviction ; "
    f"ou bien détiennent-ils les trésors de ton Seigneur, ou sont-ils eux les maîtres souverains ?{NN}» "
    f"— al-Ṭūr (52){NN}: 35{EN}37]</p>"
)


def fix(did: str, old: str, new: str, expect: int) -> None:
    path = f"{TMP}/{did}.html"
    text = open(path, encoding="utf-8").read()
    n = text.count(old)
    if n != expect:
        raise SystemExit(f"✗ {did} : {n} occurrence(s) de l’ancien libellé (attendu {expect}) — abandon")
    open(path, "w", encoding="utf-8").write(text.replace(old, new))
    print(f"✓ {did} : {expect} remplacement(s) appliqué(s)")


def main() -> None:
    for did, cnt in MAIDA_COUNTS.items():
        fix(did, MAIDA_OLD, MAIDA_NEW, cnt)
    fix("12953", INSAN_OLD, INSAN_NEW, 1)
    fix("12953", TUR_OLD, TUR_NEW, 1)
    print("→ 4 leçons corrigées (12875, 12885, 12908, 12953) — CMS à ré-injecter (finalize-r91.py)")


if __name__ == "__main__":
    main()

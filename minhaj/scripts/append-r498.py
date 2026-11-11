#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Append worklog — passe 0707 fin : R498 (QA navigateur leçon 744) + remise
(armer 745 sous R499 puis livrer sous R500)."""
import json

W = "/home/z/my-project/worklog.md"
lines = [
    "- R498 (même passe cron-agent-loop-202611020707 — SECONDE LEÇON DU TOUR) — QA NAVIGATEUR leçon 744 + sécurisation : desktop 1280 — h1 « Sourate Al-Kahf (versets 19-20) » (titleFr du portail porté tel quel), 23 044 car rendus, 11 titres, 0 erreur console, 0 overflow de contenu (l'ARTICLE présente l'artefact constant du layout reader-col 768, identique mesure pour mesure aux leçons 741-743 livrées) ; mobile 390 — 22 968 car, 0 overflow de contenu ; captures ×2 (qa-R498-744-{desktop,mobile}.png, non-blanc 9,8 %/15,0 %) ; COMMIT QA + worklog ; push fin de passe — échecs push consécutifs : 0.",
    "- Prochaine priorité : (1) ARMER la leçon 745 (Kahf v21-24, p.50-54, borne supérieure à trancher par sondage — la leçon 8 ouvre au-delà, à sonder par scripts/kahf-l6-sondage.py adapté, p.55+) sous Task ID R499 (strictement supérieur à R498 ici apposé) — vérifier d'abord la carte kahf-map contre le REGISTRE ; puis LA LIVRER sous Task ID R500 si la passe le porte ; (2) la règle h tient : le tail du worklog après cette entrée EST la priorité.",
]
with open(W, "a", encoding="utf-8") as fh:
    for ln in lines:
        fh.write(ln + "\n")
with open("/home/z/my-project/tr-tmp/worklog-append-r498.txt", "w", encoding="utf-8") as fh:
    fh.write(lines[0] + "\n" + lines[1] + "\n")
lock = {
    "utc": "2026-11-01T23:34:30Z",
    "trace_id": "cron-agent-loop-202611020707",
    "job": 492688,
    "action": "passe 0707 CLOSE : R496 lecon 743 livree (41809e8) + QA + R497 armement 744 (47e7329) + R498 lecon 744 livree (9587e01) + QA — DEUX leçons livrées, REGISTRE 1067, tafsir-5ep 97/122 — remise : ARMER 745 sous R499 puis LIVRER sous R500",
}
with open("/home/z/my-project/tr-tmp/turn-lock.json", "w", encoding="utf-8") as fh:
    fh.write(json.dumps(lock, ensure_ascii=False, indent=1) + "\n")
print("worklog +2 lignes (R498 QA, priorité) ; lock rafraîchi")

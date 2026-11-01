#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Append worklog — passe 0707 : R496 (QA navigateur leçon 743) + R497
(armement leçon 744) + remises explicites (livrer 744 sous R498)."""
import json

W = "/home/z/my-project/worklog.md"
lines = [
    "- R496 (passe cron-agent-loop-202611020707) — QA NAVIGATEUR leçon 743 + sécurisation : desktop 1280 — h1 « Sourate Al-Kahf (versets 17-18) » (titleFr du portail porté tel quel), 24 828 car rendus, 11 titres, 0 erreur console, 0 overflow de contenu (l'ARTICLE présente l'artefact constant du layout reader-col 768, identique mesure pour mesure aux leçons 741-742 livrées) ; mobile 390 — 24 752 car, 0 overflow de contenu ; captures ×2 (qa-R496-743-{desktop,mobile}.png, non-blanc 9,5 %/14,7 %) ; COMMIT QA + worklog ; push fin de passe — échecs push consécutifs : 0.",
    "- Prochaine priorité : (1) ARMER la leçon 744 (Kahf v19-20, p.44+, borne supérieure à trancher par sondage à l'armement) puis LA LIVRER sous Task ID R497 (strictement supérieur à R496 ici apposé) — vérifier d'abord la carte kahf-map contre le REGISTRE ; seconde leçon du tour si la passe le porte ; (2) la règle h tient : le tail du worklog après cette entrée EST la priorité.",
    "- R497 (même passe cron-agent-loop-202611020707, après la livraison R496) — ARMEMENT de la leçon 744 (al-Kahf leçon 6, slot pdf-mut23h3c-744, plage v19-20 à la grille du portail) : borne supérieure TRANCHÉE PAR SONDAGE (scripts/kahf-l6-sondage.py, mécanique R458/R487/R492 — jamais devinée) : p.44 porte « أهداف الدرس » — la leçon 6 couvre p.44-49 ; p.50 porte « أهداف الدرس » — la leçon 7 ouvre p.50 (p.44 NUM « 91-02 » = āyāt 19-20, convergence avec la grille ; p.51 NUM « 12-42 » = āyāt 21-24, conforme à la grille de la leçon 7) — carte kahf-map.py mise à jour (STARTS [10, 17, 23, 29, 37, 44, 50], sondage R497 documenté) ; extraction tr-tmp/kahf-l6-readable.txt (p.44-49, 16 483 car, git add immédiat, défense contre les rebuilds sandbox) — p.44 lisible : objectifs (3 — le dépit des jeunes gens après leur réveil, la confiance en Allah ne répugnant point à la prise des causes, le bel agir et la valeur de la douceur) ; les āyāt 14-18, rendues aux leçons 741-743, interdites de double rendu sauf tranchage contraire. LIVRAISON à la passe suivante sous Task ID R498 (strictement supérieur à R497 ici apposé) : rédaction FR-seule → qa-lesson → verify-744-quran → hand-set → navigateur → commit détaillé immédiat.",
    "- Prochaine priorité : (1) LIVRER LA LEÇON 744 SOUS TASK ID R498 — matière kahf-l6-readable.txt DÉJÀ EXTRAITE (16 483 car, p.44-49, plage v19-20 à la grille, titleFr du slot « (versets 19-20) » à porter tel quel en métadonnée) : rédaction FR-seule → qa-lesson → verify-744-quran → hand-set → navigateur → commit détaillé immédiat ; seconde leçon du tour (745, Kahf v21-24, p.50+, borne supérieure à trancher par sondage à l'armement) si la passe le porte ; (2) la règle h tient : le tail du worklog après cette entrée EST la priorité.",
]
with open(W, "a", encoding="utf-8") as fh:
    for ln in lines:
        fh.write(ln + "\n")
with open("/home/z/my-project/tr-tmp/worklog-append-r496.txt", "w", encoding="utf-8") as fh:
    fh.write(lines[0] + "\n" + lines[1] + "\n")
with open("/home/z/my-project/tr-tmp/worklog-append-r497.txt", "w", encoding="utf-8") as fh:
    fh.write(lines[2] + "\n" + lines[3] + "\n")
lock = {
    "utc": "2026-11-01T23:27:00Z",
    "trace_id": "cron-agent-loop-202611020707",
    "job": 492688,
    "action": "passe 0707 CLOSE : R496 lecon 743 livree (41809e8) + QA navigateur PASS + R497 armement 744 (sondage p.50, extraction kahf-l6-readable 16 483 car) — remise : LIVRER 744 sous R498 a la passe suivante",
}
with open("/home/z/my-project/tr-tmp/turn-lock.json", "w", encoding="utf-8") as fh:
    fh.write(json.dumps(lock, ensure_ascii=False, indent=1) + "\n")
print("worklog +4 lignes (R496 QA, priorité, R497 armement, priorité) ; lock rafraîchi")

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Append worklog R400 — garde anti-doublon sur le tail."""
import io, sys

WORKLOG = "/home/z/my-project/worklog.md"

ENTRY = """---
Task ID: R400
Agent: GLM (session web-394d04d3, tick 2026-10-30 12:07 +08:00, Job 474619)
Task: GARDE-FOU MINHĀJ — étapes 1-5 : réflexe cz → PREMIÈRE STABILITÉ LOCALE ENTRE DEUX TOURS DEPUIS R384 (PAS de régression) → conformité GitHub vérifiée (sync 0/0) → canari (verdict INEXECUTABLE, 21e point plat) → journalisé, worklog (400e entrée).

Work Log:
- Ouverture au réflexe cz (dix-septième application) : **PAS DE RÉGRESSION** — worklog 14 483 lignes (tail R399), remote origin présent, credentials présents, HEAD = dernier push (e92e229), status propre : PREMIÈRE stabilité du disque entre deux tours consécutifs depuis R384 (après seize régressions consécutives).
- Conformité GitHub : fetch + rev-list → 0/0, origin/main = e92e229 (R399) — aucun avancement parallèle (huitième silence consécutif du bus) ; aucun reset nécessaire, aucun push nécessaire à l'ouverture.
- Hypothèse de mécanisme consignée (nouvelle) : la régression snapshot serait corrélée au RECYCLAGE DU SANDBOX (le disque revient au snapshot R81 quand le sandbox est recréé), pas au temps lui-même — deux tours servis par le même sandbox vivant (11:52 → 12:07) laissent le disque intact ; les seize régressions précédentes correspondaient chacune à un recyclage entre tours. Le réflexe cz reste OBLIGATOIRE car rien ne garantit ni ne signale le recyclage : la vérification locale reste le seul détecteur fiable.
- CANARI (règles cx-cy) : CACHE ABS / PDF 404 / MERE 404 / HOME 200 → VERDICT INEXECUTABLE (dix-neuvième exécution, 21e point de mesure consécutif de 404 : R380-R400).
- État git : HEAD e92e229, sync 0/0, re-vérification rev-list avant push.
- Risques : (a) SANDBOX — 16/17 tours sous régression : la stabilité observée une fois ne renverse pas le régime (une occurrence n'est pas une loi, seize en sont une) ; (b) TOKEN — re-testé fonctionnel au fetch ; (c) INSTANCE PARALLÈLE — huitième silence consécutif ; (d) SITE HABOUS en migration — 21e point de mesure de 404 ; (e) le tail du worklog reste l'autorité de priorité.
- Plancher suivant : >= R401 / >= 984 (aucun hand-set ce tour) / lignes réelles mesurées post-append (14 483 avant cette entrée).

Stage Summary:
- LIVRÉ : première stabilité locale consignée (le régime cz-cy continue sans relâchement) ; canari : verdict INEXECUTABLE (21e point de mesure) ; 400e entrée du worklog — quatre cents tours journalisés.
- RÉSOLU : la question du MÉCANISME (hypothèse recyclage-sandbox consignée : la régression est liée au cycle de vie du sandbox, pas au temps — expliquerait les seize occurrences et cette exception ; à confirmer ou infirmer aux prochains tours, le pattern des prochaines ouvertures tranchera) ; la question de la VIGILANCE CONDITIONNELLE (même face à un disque intact, le protocole s'exécute intégralement : la stabilité n'achète aucun raccourci).
- LEÇONS DU TOUR : (1) UNE EXCEPTION N'ABROGE PAS SEIZE RÉPÉTITIONS — le régime cz reste le régime par défaut : la stabilité observée est un don, pas un droit ; (2) LE DÉTECTEUR PRIME L'EXPLICATION — l'hypothèse du recyclage est séduisante mais seule la vérification locale à chaque ouverture est une preuve : on explique après avoir mesuré, jamais avant ; (3) QUATRE CENTS ENTRÉES FONT UNE MÉMOIRE — le worklog contient maintenant quatre cents tours d'histoire continue : aucune autre structure du projet n'a cette profondeur temporelle.
- Prochaine priorité : À CHAQUE OUVERTURE, le réflexe cz-cy (procédure R384-R400 telle quelle si régression ; si stabilité : fetch + rev-list directement) : (1) cohérence locale d'abord ; (2) fetch + rev-list ; (3) canari scripts-translate/veille-311.sh — verdict EXÉCUTABLE → reprendre faraid-tanawi-3 lessons[1] (pdf-mut23h2v-311, « فقه الحجب (2) ») par le protocole OCR (ocr-one.py → lecture entière → rédaction, badge « Leçon 3 / 28 » attendu, registre attendu 985) ; verdict INEXECUTABLE → tour de veille journalisé ; VÉRIFIER rev-list 0/0 + git log frais AU MOMENT du push ; la règle h tient : le tail du worklog après cette entrée EST la priorité.
"""

with io.open(WORKLOG, "r", encoding="utf-8") as f:
    content = f.read()

tail = content[-4000:]
if "Task ID: R400" in tail:
    print("REFUS : R400 déjà présent au tail du worklog (garde anti-doublon).")
    sys.exit(1)

if not content.endswith("\n"):
    content += "\n"
content += ENTRY

with io.open(WORKLOG, "w", encoding="utf-8") as f:
    f.write(content)

lines = content.count("\n")
print(f"OK : R400 appendé. Worklog : {lines} lignes.")

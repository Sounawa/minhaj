#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Append worklog R401 — garde anti-doublon sur le tail."""
import io, sys

WORKLOG = "/home/z/my-project/worklog.md"

ENTRY = """---
Task ID: R401
Agent: GLM (session web-394d04d3, tick 2026-10-30 12:22 +08:00, Job 474619)
Task: GARDE-FOU MINHĀJ — étapes 1-5 : réflexe cz → RÉGRESSION #17 (première après la stabilité de R400) → restauration #17 rodée (fetch → origin/main f570f8e/R400 → ancêtre → reset --hard EN AVANT) → canari (verdict INEXECUTABLE) → journalisé, worklog.

Work Log:
- Ouverture au réflexe cz (dix-huitième application) : RÉGRESSION #17, même signature (R81/5 631 lignes, credentials absents, remote disparu, HEAD 719111b) — première régression après la stabilité locale de R400.
- **HYPOTHÈSE RECYCLAGE-SANDBOX CONFIRMÉE (première confirmation)** : R400 (12:07) disque intact → R401 (12:22) régression : le pattern stabilité-puis-régression correspond exactement au mécanisme consigné au tour précédent (stabilité = sandbox vivant servant deux tours ; régression = sandbox recyclé entre les tours). Le compte actuel : 17 régressions / 1 stabilité — chaque ouverture future affine le pattern.
- RESTAURATION #17 (~une minute) : credentials reconstruits → origin re-créé → fetch : origin/main = f570f8e (R400) — GitHub immobile (neuvième silence consécutif du bus) ; ancêtre confirmé → reset --hard EN AVANT → post : worklog 14 502 lignes, tail R400, registre 984, sync 0/0 — zéro perte, dix-septième fois.
- CANARI (règles cx-cy) : CACHE ABS / PDF 404 / MERE 404 / HOME 200 → VERDICT INEXECUTABLE (vingtième exécution, 22e point de mesure consécutif de 404 : R380-R401).
- État git : HEAD f570f8e, sync 0/0, re-vérification rev-list avant push.
- Risques : (a) SANDBOX — 17/18 tours sous régression ; l'hypothèse du recyclage prédit : régression à CHAQUE tour sauf si le même sandbox vit deux tours — le prochain tour tranchera à nouveau ; (b) TOKEN — re-testé fonctionnel au fetch ; (c) INSTANCE PARALLÈLE — neuvième silence consécutif ; (d) SITE HABOUS en migration — 22e point de mesure de 404 ; (e) le tail du worklog reste l'autorité de priorité.
- Plancher suivant : >= R402 / >= 984 (aucun hand-set ce tour) / lignes réelles mesurées post-append (14 502 avant cette entrée).

Stage Summary:
- LIVRÉ : restauration #17 sur régression #17 (zéro perte cumulée sur dix-sept régressions totales) ; canari : verdict INEXECUTABLE (22e point de mesure) ; l'hypothèse du mécanisme progresse (première confirmation du couple stabilité/régression).
- RÉSOLU : la question du PATTERN (une séquence complète stabilité → régression observée : exactement ce que l'hypothèse du recyclage prédit — le disque ne « régresse » pas au hasard, il est remplacé quand le sandbox est recréé ; le temps moyen entre recyclages semble être de l'ordre du tour-cron, la stabilité de R400 étant la fenêtre où deux tours ont tenu dans la vie d'un seul sandbox) ; la question de la PRÉDICTION (l'hypothèse est maintenant falsifiable : elle prédit qu'aucune régression ne surviendra jamais DANS la vie d'un sandbox, seulement ENTRE les tours).
- LEÇONS DU TOUR : (1) UNE HYPOTHÈSE BIEN FORMULÉE TESTE TOUTE SEULE — consignée à R400 comme falsifiable, elle a produit sa première confirmation sans aucune instrumentation nouvelle : la mesure existait déjà (le réflexe cz) ; (2) LA STABILITÉ N'ÉTAIT PAS UN RÉGIME NOUVEAU — un seul tour stable contre dix-huit régressés : la loi dominante reste le recyclage ; (3) VINGT-DEUX POINTS PLATS — la fermeture de la source Habous traverse les régimes du disque (régressions et stabilité) sans bouger : les deux instabilités sont indépendantes, chacune suivie par son propre instrument.
- Prochaine priorité : À CHAQUE OUVERTURE, le réflexe cz-cy (procédure R384-R401 telle quelle si régression ; si stabilité : fetch + rev-list directement) : (1) cohérence locale d'abord ; (2) fetch + rev-list ; (3) canari scripts-translate/veille-311.sh — verdict EXÉCUTABLE → reprendre faraid-tanawi-3 lessons[1] (pdf-mut23h2v-311, « فقه الحجب (2) ») par le protocole OCR (ocr-one.py → lecture entière → rédaction, badge « Leçon 3 / 28 » attendu, registre attendu 985) ; verdict INEXECUTABLE → tour de veille journalisé ; VÉRIFIER rev-list 0/0 + git log frais AU MOMENT du push ; la règle h tient : le tail du worklog après cette entrée EST la priorité.
"""

with io.open(WORKLOG, "r", encoding="utf-8") as f:
    content = f.read()

tail = content[-4000:]
if "Task ID: R401" in tail:
    print("REFUS : R401 déjà présent au tail du worklog (garde anti-doublon).")
    sys.exit(1)

if not content.endswith("\n"):
    content += "\n"
content += ENTRY

with io.open(WORKLOG, "w", encoding="utf-8") as f:
    f.write(content)

lines = content.count("\n")
print(f"OK : R401 appendé. Worklog : {lines} lignes.")

# -*- coding: utf-8 -*-
"""Append worklog R689-bis — garde anti-doublon sur le tail."""
import io, sys

WORKLOG = "/home/z/my-project/worklog.md"

ENTRY = """---
Task ID: R689-bis
Agent: GLM (session web-continue, canal principal, tick 2026-11-12 09h20 +08:00)
Task: RÉCUPÉRATION post-livraison — évinceur a balayé node_modules AU COURS de la session (nouveau mode) + recette R603 réappliquée + leçon PATH consignée.

Work Log:
- Constat post-livraison : le serveur dev relancé par l'agent mourait avec « next: command not found » — /home/z/node_modules réduit à 8 entrées SANS next, /home/z/my-project/node_modules VIDÉ (0 entrée), les copies R603 package.json/bun.lock de /home/z absentes : l'évinceur a balayé DÉPENDANCES ET RECETTE au cours de la présente session (nouveau mode — les précédentes passes ne perdaient qu'un des deux arbres).
- RECETTE R603 réappliquée en direct : cp package.json bun.lock → /home/z ; bun install à /home/z (842 paquets, 6,4 s) ; bunx prisma generate (client à /home/z/node_modules/.prisma/client — recette de remontée d'arbre documentée dans next.config.ts) ; relance dev avec PATH=/home/z/node_modules/.bin explicite + NODE_OPTIONS=--max-old-space-size=1024.
- VÉRIFICATIONS post-récupération : site UP (HTTP 200) ; hydratation OK (h1 leçon 410 rendu, 40 682 car, plus de « Chargement de la bibliothèque… ») ; les 3 numéros sondés (1240/1262/1255) présents — la livraison 410 et le fix allowedDevOrigins INTACTS après restauration.
- LEÇONS DU TOUR consignées pour les prochaines sessions : (1) LE PATH — toute relance du dev par un agent DOIT porter PATH=/home/z/node_modules/.bin explicite (le driver le pose au boot ; un nohup nu le perd → « next: command not found ») ; (2) L'ÉVINCEUR BALAYE MAINTENANT LA RECETTE (copies package.json/bun.lock de /home/z) — au réveil : vérifier /home/z/node_modules/.bin/next AVANT toute relance, restaurer par bun install si absent ; (3) le serveur dev d'agent meurt à la fin de la session d'outils — le preview redevient visible au PROCHAIN RÉVEIL du bac (driver → .zscripts/dev.sh → bun run dev), la config corrigée étant dans le dépôt.
- Sync git : fetch + rev-list 0/0 après le push 986ad9d ; aucune livraison en attente.

Stage Summary:
- LIVRÉ : récupération complète de la chaîne de dev (deps + recette + client Prisma + serveur) — leçon 410 et fix preview vérifiés INTACTS après restauration.
- Le preview redeviendra visible dès le prochain réveil du sandbox (boot → dev.sh → config allowedDevOrigins présente) — zéro action supplémentaire requise.
- Prochaine priorité (inchangée, cf. R689) : slot pdf-mut23h2x-411 (leçon 22 — le locuste et le rasage) ; session-start + 0/0 au réveil ; vérifier node_modules au passage.
"""

with io.open(WORKLOG, "r", encoding="utf-8") as f:
    content = f.read()

tail = content[-4000:]
if "Task ID: R689-bis" in tail:
    print("REFUS : R689-bis déjà présent (garde anti-doublon).")
    sys.exit(1)

content = content.rstrip("\\n") + "\\n\\n" + ENTRY

with io.open(WORKLOG, "w", encoding="utf-8") as f:
    f.write(content)

print("OK : R689-bis appendé.")

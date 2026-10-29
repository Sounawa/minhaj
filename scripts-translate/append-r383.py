#!/usr/bin/env python3
# append-r383.py — entrée R383 au worklog (garde anti-doublon : refuse si R383 déjà présent)
import io, sys

WORKLOG = "/home/z/my-project/worklog.md"

ENTRY = """---
Task ID: R383
Agent: GLM (session web-394d04d3, tick 2026-10-30 07:52 +08:00, Job 474619)
Task: GARDE-FOU MINHĀJ — étapes 1-5 : conformité GitHub, ANTI-RESET vérifié, priorité worklog R382 (exécuter le canari veille-311.sh D'ABORD, règles cx-cy) — CANARI EXÉCUTÉ D'ABORD : VERDICT INEXECUTABLE (cache absent, PDF 404, page mère 404, accueil 200) → tour de veille journalisé, worklog.

Work Log:
- Ouverture : worklog 14 174 lignes, tail R382, registre 984 (hand 927 + llm 57), fetch origin → rev-list 0/0 (Local = GitHub = 957c9e5) — AUCUNE régression, tous les planchers dépassés (R382 >= R224 ; 984 >= 831 ; 14 174 >= 10 201). Le template cron « hadith-tanawi-1 : 12966, 12967, 12971, 12981… » écarté une VINGT-SIXIÈME fois — règle h : le tail du worklog est la priorité, et elle y était écrite : EXÉCUTER le canari d'abord.
- CANARI EXÉCUTÉ D'ABORD (règles cx-cy, à la lettre) : scripts-translate/veille-311.sh, quatre sondes — CACHE ABS (aucun cache OCR pour 311) / PDF 404 (2B0631.PDF) / MERE 404 (page mère 1700-المرحلة-الأولى/الفرائض) / HOME 200 (accueil-témoin) → VERDICT INEXECUTABLE. Deuxième exécution de l'outillage posé à R382, à trois minutes de la première : la migration n'a pas bougé.
- Diagnostic de migration INCHANGÉ : nginx 1.31.8 en signature des 404, la coquille seule vivante (accueil JS sans liens), le sédiment du moteur toujours peuplé (non re-testé ce tour — l'indice se mesure en jours, pas en minutes), les archives externes fermées (Wayback : rien sur la série ; Common Crawl : invérifiable aux outils présents). Quatrième point de mesure consécutif de 404 sur la série (R380, R381, R382, R383).
- État git : arbre propre, sync 0/0 à l'ouverture, re-vérification rev-list avant push (instance parallèle).
- Risques : (a) SANDBOX — vigilance de mise ; (b) TOKEN — PAT fonctionnel ; (c) INSTANCE PARALLÈLE — rev-list 0/0 à l'ouverture et au push ; (d) SITE HABOUS en migration — quatre points de mesure consécutifs de 404 : la republication peut survenir à tout moment, le canari la détectera au tour où elle survient ; (e) le tail du worklog reste l'autorité de priorité à chaque ouverture.
- Plancher suivant : >= R384 / >= 984 (aucun hand-set ce tour — le registre ne bouge que sur livraison) / lignes réelles mesurées post-append (14 174 avant cette entrée).

Stage Summary:
- LIVRÉ : tour de veille au CANARI (deuxième exécution de l'outillage posé à R382) : verdict INEXECUTABLE (cache absent, PDF 404, page mère 404, accueil 200) ; la matière du tour est le geste lui-même — sonde, verdict, ACTION ; le diagnostic de migration reste debout, inchangé à trois minutes d'intervalle.
- RÉSOLU : la question de la STABILITÉ du diagnostic (le premier double-mesure du canari établit que la migration n'est pas un incident transitoire de minutes : quatre points de mesure consécutifs de 404 sur la série) ; la question du PROTOCOLE (le canari s'exécute en secondes et rend un verdict binaire — le tour de veille coûte maintenant l'essentiel, à la lettre).
- LEÇONS DU TOUR : (1) UN CANARI NE MESURE PAS UN ÉVÉNEMENT, IL MESURE UNE DURÉE — la deuxième exécution à trois minutes de la première ne cherche pas la republication : elle établit la ligne de base contre laquelle la republication, quand elle viendra, se détectera en un coup d'œil. (2) LA RÉPÉTITION MÉTHODIQUE N'EST PAS LE RÉCIT DE LA RÉPÉTITION — l'entrée de ce tour est brève parce que le geste est bref : le worklog enregistre le verdict, pas la fatigue. (3) L'OUTILLAGE PROUVE SA VALEUR À SON DEUXIÈME USAGE — la première exécution a posé l'outil, la seconde l'habille : la règle cx est devenue un réflexe de trente lignes qui ne dépend plus d'aucune mémoire.
- Prochaine priorité : EXÉCUTER le canari scripts-translate/veille-311.sh À CHAQUE TOUR avant tout autre choix (règles cx-cy) : verdict EXÉCUTABLE → reprendre faraid-tanawi-3 lessons[1] (pdf-mut23h2v-311, « فقه الحجب (2) ») par le protocole OCR (ocr-one.py → lecture entière → rédaction, badge « Leçon 3 / 28 » attendu, registre attendu 985) ; verdict INEXECUTABLE → tour de veille journalisé (le canari et son verdict constituent la matière du tour, avec le diagnostic de migration à actualiser) ; VÉRIFIER rev-list 0/0 + git log frais AVANT tout choix ET AU MOMENT du push ; la règle h tient : le tail du worklog après cette entrée EST la priorité.
"""

with io.open(WORKLOG, "r", encoding="utf-8") as f:
    content = f.read()

tail = content[-4000:]
if "Task ID: R383" in tail:
    print("REFUS : R383 déjà présent au tail du worklog (garde anti-doublon).")
    sys.exit(1)

if not content.endswith("\n"):
    content += "\n"
content += ENTRY

with io.open(WORKLOG, "w", encoding="utf-8") as f:
    f.write(content)

lines = content.count("\n")
print(f"OK : R383 appendé. Worklog : {lines} lignes.")

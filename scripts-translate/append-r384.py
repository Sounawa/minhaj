#!/usr/bin/env python3
# append-r384.py — entrée R384 au worklog (garde anti-doublon : refuse si R384 déjà présent)
import io, sys

WORKLOG = "/home/z/my-project/worklog.md"

ENTRY = """---
Task ID: R384
Agent: GLM (session web-394d04d3, tick 2026-10-30 08:07 +08:00, Job 474619)
Task: GARDE-FOU MINHĀJ — étapes 1-5 : ouverture → RÉGRESSION CATASTROPHIQUE DÉTECTÉE (dépôt local revenu à un état ancien R81/5 631 lignes, remote origin disparu, credentials absents — signature d'une restauration de snapshot de la sandbox) → ÉTAPE 2 (conformité GitHub) transformée en RESTAURATION DEPUIS LA SOURCE DE VÉRITÉ : credentials + remote reconstruits, fetch, ancêtre vérifié, reset --hard EN AVANT vers origin/main (48f0f9a/R383) → restauration vérifiée → canari exécuté (verdict INEXECUTABLE) → incident journalisé, worklog.

Work Log:
- Ouverture ANORMALE : worklog.md à 5 631 lignes, tail R81, registre 502/950, HEAD 719111b (« worklog R81 : livre 49 hadith-1es ouvert… ») — plus de 1 000 entrées de derrière ; git remote -v VIDE (origin disparu), ~/.git-credentials ABSENT — TRIPLE signature cohérente d'une restauration de snapshot du système de fichiers (dépôt ET home), pas d'un reset git (un reset n'efface ni remote ni credentials). Le dev server port 3000 n'a pas été touché (protocole).
- RÉGRESSION JOURNALISÉE COMME EXIGÉ (étape 3) : worklog local 5 631 < 14 192 attendu, R81 < R383 attendu — la règle tient : ne JAMAIS faire confiance à l'état local, la source de vérité est GitHub.
- RESTAURATION EXÉCUTÉE IMMÉDIATEMENT : (1) ~/.git-credentials reconstruit (format x-access-token, le PAT fonctionnel prouvé par les pushes du jour) + credential.helper store ; (2) origin re-créé (https://github.com/Sounawa/minhaj.git) ; (3) git fetch origin — OK ; (4) origin/main = 48f0f9a (R383) — EXACTEMENT le dernier état poussé, aucune instance parallèle n'avait avancé depuis ; branche ancienne origin/backup-reprise-r84 notée, sans effet (main est la source de vérité) ; (5) rev-list : 0 en avance / 1 076 en retard — le local est un ancêtre pur de origin/main ; (6) merge-base --is-ancestor CONFIRMÉ → git reset --hard origin/main AUTORISÉ et exécuté (restauration EN AVANT uniquement — 5 371 fichiers remis) ; (7) vérification post-reset : worklog 14 192 lignes, tail R383, registre 984, scripts-translate/veille-311.sh et append-r383.py présents, arbre propre.
- CANARI EXÉCUTÉ APRÈS RESTAURATION (règles cx-cy, priorité du tail R383) : quatre sondes — CACHE ABS / PDF 404 / MERE 404 / HOME 200 → VERDICT INEXECUTABLE (troisième exécution, 5e point de mesure consécutif de 404 sur la série : R380, R381, R382, R383, R384).
- Diagnostic de migration INCHANGÉ (nginx 1.31.8, coquille seule vivante, sédiment du moteur peuplé, archives externes fermées) ; l'incident de snapshot est INDÉPENDANT de la migration du site : deux instabilités externes distinctes, la première frappe le LOCAL (défendue par GitHub), la seconde frappe la SOURCE (défendue par le canari et la veille).
- État git post-restauration : HEAD 48f0f9a, sync 0/0, re-vérification rev-list avant push (instance parallèle).
- Risques : (a) SANDBOX — LA PREUVE EST FAITE : le snapshot local peut régresser de plus de mille entrées SANS PRÉVENIR ; la reconstruction des credentials est désormais un geste rodé (même token, même format) ; (b) TOKEN — PAT re-testé fonctionnel au fetch de ce tour ; (c) INSTANCE PARALLÈLE — rev-list 0/0 à la clôture ; (d) SITE HABOUS en migration — 5e point de mesure de 404 ; (e) le tail du worklog reste l'autorité de priorité — après cette entrée, elle sera la priorité de R385.
- Plancher suivant : >= R385 / >= 984 (aucun hand-set ce tour) / lignes réelles mesurées post-append (14 192 avant cette entrée).

Stage Summary:
- LIVRÉ : RESTAURATION COMPLÈTE DEPUIS LA SOURCE DE VÉRITÉ (le scénario ANTI-RESET du protocole, exécuté pour de vrai) : régression détectée à l'ouverture (R81/5 631 lignes, remote disparu, credentials absents — snapshot sandbox) ; la chaîne de reconstruction intégralement parcourue (credentials → remote → fetch → ancêtre vérifié → reset --hard EN AVANT → vérification) ; le dépôt revenu à 48f0f9a/R383 en moins de deux minutes, ZÉRO perte (l'arbre était propre, tout ce qui compte est sur GitHub) ; canari ensuite : verdict INEXECUTABLE (5e point de mesure).
- RÉSOLU : la question de la PERTES POSSIBLE (réponse : AUCUNE — la source de vérité a tout rendu, le registre, les règles, les scripts, les 383 entrées du journal) ; la question de la PROCÉDURE (elle était écrite au protocole depuis la R364 et s'est exécutée à la lettre : détecter, reconstruire l'accès, fetch, vérifier l'ancêtre, avancer, jamais revenir en arrière) ; la question des DEUX INSTABILITÉS (snapshot sandbox contre migration Habous : la première est réparée, la seconde est en veille — chacune a sa défense : GitHub pour l'une, le canari pour l'autre).
- LEÇONS DU TOUR : (1) LA SOURCE DE VÉRITÉ N'EST PAS UNE PRÉCAUTION, C'EST LA CONTINUITÉ MÊME — mille entrées ont disparu du disque en un instant et n'ont pas existé comme perte : elles étaient déjà ailleurs. (2) LA RÉGRESSION SE DÉTECTE AU CHIFFRE, PAS À L'ŒIL — le worklog compte ses lignes et son tail à chaque ouverture : 5 631 contre 14 192, la régression est un fait arithmétique avant d'être une émotion. (3) LE PROTOCOLE ÉCRIT EST LE SEUL QUI RÉSISTE À L'IMPRÉVU — l'étape 3 du GARDE-FOU (« si régression → restaurer depuis GitHub immédiatement et journaliser ») n'a pas été inventée ce tour : elle a été LUE puis exécutée — c'est exactement pour ce tour-là qu'elle existait.
- Prochaine priorité : EXÉCUTER le canari scripts-translate/veille-311.sh À CHAQUE TOUR avant tout autre choix (règles cx-cy) : verdict EXÉCUTABLE → reprendre faraid-tanawi-3 lessons[1] (pdf-mut23h2v-311, « فقه الحجب (2) ») par le protocole OCR (ocr-one.py → lecture entière → rédaction, badge « Leçon 3 / 28 » attendu, registre attendu 985) ; verdict INEXECUTABLE → tour de veille journalisé ; NOUVEAU (leçon du tour) : À CHAQUE OUVERTURE, vérifier D'ABORD la cohérence locale (wc -l worklog.md + tail + git remote -v) AVANT même le fetch — si le local a régressé, la procédure de restauration de ce tour (credentials → remote → fetch → ancêtre → reset --hard EN AVANT) s'applique telle quelle ; VÉRIFIER rev-list 0/0 + git log frais AU MOMENT du push ; la règle h tient : le tail du worklog après cette entrée EST la priorité.
"""

with io.open(WORKLOG, "r", encoding="utf-8") as f:
    content = f.read()

tail = content[-4000:]
if "Task ID: R384" in tail:
    print("REFUS : R384 déjà présent au tail du worklog (garde anti-doublon).")
    sys.exit(1)

if not content.endswith("\n"):
    content += "\n"
content += ENTRY

with io.open(WORKLOG, "w", encoding="utf-8") as f:
    f.write(content)

lines = content.count("\n")
print(f"OK : R384 appendé. Worklog : {lines} lignes.")

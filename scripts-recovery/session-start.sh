#!/usr/bin/env bash
# ============================================================================
# Minhāj — session-start.sh — PROTOCOLE ANTI-PERTE (OBLIGATOIRE)
# ----------------------------------------------------------------------------
# LA RÈGLE (demande utilisateur explicite, 24 oct. 2026, renforcée le même jour) :
#   « arrêter les resets et mettre un code pour regarder à chaque session
#     où on en est sur GitHub » PUIS
#   « tu dois vérifier tout le temps si tu es en accord avec GitHub ;
#     tu ne peux pas relancer le cron sans vérifier — sinon travail inutile
#     en double de ce qui est déjà fait ».
#
# CE SCRIPT DOIT ÊTRE LANCÉ EN PREMIER, À CHAQUE SESSION / CHAQUE RELAIS CRON,
# AVANT TOUT TRAVAIL ET AVANT TOUT RÉ-ARMEMENT DU CRON OU RELANCE DU SUPERVISEUR.
# GitHub (github.com/Sounawa/minhaj, branche main) EST LA SOURCE DE VÉRITÉ
# UNIQUE. Le bac local peut être restauré à un vieux point par la plateforme à
# tout moment (c'est arrivé : R0, R57, R75, R81→R200, R81→R206).
#
# ⛔ ORDRE IMPOSÉ (règle utilisateur) :
#   1. CE SCRIPT (exit 0) → 2. seulement alors travail / relance machines / cron.
#   Si exit 3 (EN RETARD) : récupérer, REJOUER ce script jusqu'à exit 0/4.
#   Si exit 4 (EN AVANCE) : pousser, rejouer ce script jusqu'à exit 0.
#   JAMAIS de travail sur un bac non aligné — risque de refaire du déjà-fait.
#
# Usage :  bash /home/z/my-project/scripts-recovery/session-start.sh
# Sortie  : 0 = à jour / 3 = EN RETARD (récupération requise) / 4 = en avance (push requis)
#           2 = fetch impossible (réseau) — travailler local, retenter le push ensuite.
# ============================================================================
set -uo pipefail

PROJ="/home/z/my-project"
REMOTE_URL="https://github.com/Sounawa/minhaj.git"
cd "$PROJ" || exit 2

BOLD=$'\033[1m'; RED=$'\033[31m'; GREEN=$'\033[32m'; AMBER=$'\033[33m'; DIM=$'\033[2m'; RST=$'\033[0m'

echo "${BOLD}═══════════════════════════════════════════════════════════════════${RST}"
echo "${BOLD} MINHĀJ — ÉTAT DE SESSION (GitHub = source de vérité)${RST}"
echo "${BOLD}═══════════════════════════════════════════════════════════════════${RST}"

# 1) Remote origin garanti
if ! git remote get-url origin >/dev/null 2>&1; then
  git remote add origin "$REMOTE_URL"
  echo "${DIM}remote origin configuré → $REMOTE_URL${RST}"
fi

# 2) Fetch GitHub (lecture publique, AUCUN token requis)
if ! timeout 90 git fetch origin main 2>/dev/null; then
  echo "${AMBER}⚠ FETCH IMPOSSIBLE (réseau ?) — continuer en local, retenter le push plus tard.${RST}"
  echo "${DIM}(vérifier : curl -sI https://github.com | head -1)${RST}"
  exit 2
fi

# 3) Comparaison locale ↔ GitHub
LOCAL=$(git rev-parse HEAD)
REMOTE=$(git rev-parse origin/main)
BEHIND=$(git rev-list --count HEAD..origin/main 2>/dev/null || echo "?")
AHEAD=$(git rev-list --count origin/main..HEAD 2>/dev/null || echo "?")
SHORT_L=$(git rev-parse --short HEAD)
SHORT_R=$(git rev-parse --short origin/main)

# 4) Indicateurs de progression (registre savant + worklog + dernier commit)
REG=""
[ -f scripts-translate/savant-registry.json ] && REG=$(python3 -c "
import json; r=json.load(open('scripts-translate/savant-registry.json'))
print(len(r.get('hand',[])))" 2>/dev/null)
LAST_TASK=$(grep '^Task ID:' worklog.md 2>/dev/null | tail -1 | sed 's/Task ID: *//')
LAST_COMIT=$(git log -1 --format=%s | head -c 120)

echo " Local   : ${SHORT_L}  ${DIM}($(date -r .git/HEAD '+%H:%M' 2>/dev/null || true))${RST}"
echo " GitHub  : ${SHORT_R}  (origin/main)"
echo " Retard  : ${BEHIND} commit(s) GitHub non récupérés | Avance locale : ${AHEAD} à pousser"
echo " Registre savant : ${REG:-?}/950  | Dernière entrée worklog : ${LAST_TASK:-?}"
echo " Dernier commit  : ${DIM}${LAST_COMIT}…${RST}"

# 5) Poussée possible ? (token GitHub dans le credential store)
CAN_PUSH="non"
if grep -q "github.com" ~/.git-credentials 2>/dev/null; then CAN_PUSH="oui (token en credential store)";
elif git config --get credential.helper 2>/dev/null | grep -q store && [ -s ~/.git-credentials ]; then CAN_PUSH="oui";
fi
echo " Push possible    : ${CAN_PUSH}"

echo "${DIM}───────────────────────────────────────────────────────────────────${RST}"

# 6) Verdict + actions
if [ "$BEHIND" != "0" ] && [ "$BEHIND" != "?" ]; then
  echo "${RED}${BOLD}⛔ EN RETARD DE ${BEHIND} COMMIT(S) — LE BAC LOCAL A ÉTÉ RESTAURÉ À UN VIEUX POINT.${RST}"
  echo "${RED}   GitHub EST PLUS AVANCÉ. NE PAS REFAIRE LE TRAVAIL — RÉCUPÉRER IMMÉDIATEMENT :${RST}"
  echo ""
  echo "${BOLD}   git branch -f local-stale-\$(date +%m%d) HEAD   # sauvegarde du vieux point${RST}"
  echo "${BOLD}   git reset --hard origin/main                   # alignage sur GitHub${RST}"
  echo "${BOLD}   bun run db:push                                 # si le schéma Prisma a bougé${RST}"
  echo ""
  echo "${RED}   …puis vérifier registre/registre-savant ci-dessus et CONTINUER le travail là où${RST}"
  echo "${RED}   GitHub s'est arrêté (dernière entrée worklog : ${LAST_TASK:-?}).${RST}"
  exit 3
fi

if [ "$AHEAD" != "0" ] && [ "$AHEAD" != "?" ]; then
  echo "${AMBER}${BOLD}▲ ${AHEAD} COMMIT(S) LOCAL(AUX) PAS ENCORE POUSSÉ(S) — pousser dès que possible :${RST}"
  echo "${BOLD}   git push origin main${RST}"
  [ "$CAN_PUSH" = "non" ] && echo "${AMBER}   (aucun token dans ce bac — demander le token GitHub à l'utilisateur)${RST}"
  exit 4
fi

echo "${GREEN}${BOLD}✅ À JOUR AVEC GITHUB (origin/main) — on reprend le travail là où il s'est arrêté.${RST}"
echo "${DIM}   Prochaine leçon : voir la fin du worklog.md + savant-registry.json (hand).${RST}"
exit 0

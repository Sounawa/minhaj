#!/bin/bash
# veille-portail.sh — CANARI DE PORTE (créé R433, 2026-10-30 ~20:10 +08:00)
# Contexte : refonte complète du portail habous.gov.ma. La page d'accueil affiche
# une bannière explicite « الموقع في طور الصيانة / Site en maintenance » et annonce
# une NOUVELLE VERSION. Les anciennes URL (/images/2024/, 2025/, 2026/, 2017/) sont
# toutes mortes et ne reviendront probablement jamais sous cette forme.
# Le VRAI signal de reprise n'est donc plus l'ancienne URL : c'est la DISPARITION
# de la bannière de maintenance de la page d'accueil.
# Règle cx' (R433) : À CHAQUE TOUR, lancer ce canari EN PREMIER.
#   - PORTE FERMÉE  → tour de veille journalisé (comme avant).
#   - PORTE OUVERTE → lancer IMMÉDIATEMENT scripts-translate/reprise-portail.sh.

H="https://www.habous.gov.ma/"

echo "== CANARI PORTE — $(date -u '+%Y-%m-%d %H:%M UTC') =="

body=$(curl -ksS --max-time 25 "$H" 2>/dev/null)
rc=$?
if [ $rc -ne 0 ] || [ ${#body} -lt 200 ]; then
  echo "PORTE|ERR|récupération accueil impossible (curl rc=$rc, ${#body} octets)"
  echo "== VERDICT: INCONNU (re-tester) =="
  exit 0
fi

if echo "$body" | grep -q "الموقع في طور الصيانة\|Site en maintenance\|en cours de mise à jour"; then
  echo "PORTE|FERMÉE|bannière de maintenance toujours présente — nouvelle version non lancée"
  echo "== VERDICT: INEXECUTABLE =="
  echo "ACTION: tour de veille journalisé (règle cx'), re-test au tour suivant"
else
  echo "PORTE|OUVERTE|bannière de maintenance ABSENTE — nouvelle version probablement lancée"
  echo "== VERDICT: REPRISE =="
  echo "ACTION IMMÉDIATE: bash scripts-translate/reprise-portail.sh"
fi

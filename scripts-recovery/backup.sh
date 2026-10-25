#!/usr/bin/env bash
# Minhāj — Sauvegarde multi-emplacements (v2).
# À lancer à CHAQUE vague de travail (règle utilisateur absolue).
#
# LEÇON DES RÉINITIALISATIONS :
#   - 3 oct. : /home/z/my-project effacé, dossiers cachés survivé → v1 ciblait /home/z/.minhaj-backup
#   - 6 oct. : /home/z/.minhaj-backup ET /home/z/tr-src effacés, /home/z/my-project SURVÉCU
#   → Conclusion : AUCUN emplacement externe fiable. Sauvegarde PRINCIPALE = dans
#     my-project (backups/ + commits git). Copie secondaire dans le home au cas où.
set -uo pipefail

STAMP=$(date +%Y%m%d-%H%M%S)
PROJ=/home/z/my-project
PRIMARY="$PROJ/backups"          # emplacement principal (dans le projet, survit aux resets)
SECONDARY=/home/z/.minhaj-backup # emplacement secondaire (best effort)

mkdir -p "$PRIMARY/snapshots" "$SECONDARY/snapshots" 2>/dev/null || true

# 1) Snapshot tarball horodaté (dans le projet)
ITEMS=()
[ -d "$PROJ/content" ] && ITEMS+=("content")
[ -f "$PROJ/worklog.md" ] && ITEMS+=("worklog.md")
[ -d "$PROJ/scripts-translate" ] && ITEMS+=("scripts-translate")
[ -d "$PROJ/scripts-recovery" ] && ITEMS+=("scripts-recovery")
[ -d "$PROJ/src" ] && ITEMS+=("src")
[ -f "$PROJ/package.json" ] && ITEMS+=("package.json")

if [ ${#ITEMS[@]} -eq 0 ]; then
  echo "✗ Rien à sauvegarder."
  exit 1
fi

tar -czf "$PRIMARY/snapshots/minhaj-$STAMP.tar.gz" -C "$PROJ" "${ITEMS[@]}" 2>/dev/null
cp -f "$PRIMARY/snapshots/minhaj-$STAMP.tar.gz" "$PRIMARY/minhaj-latest.tar.gz"

# 2) Copie secondaire (best effort — ce dossier peut être effacé)
cp -f "$PRIMARY/minhaj-latest.tar.gz" "$SECONDARY/minhaj-latest.tar.gz" 2>/dev/null || true
cp -f "$PROJ/worklog.md" "$SECONDARY/worklog-latest.md" 2>/dev/null || true

# 3) Copie directe du corpus (accès rapide sans décompression)
mkdir -p "$PRIMARY/content/books"
cp -f "$PROJ/content/manifest.json" "$PRIMARY/content/" 2>/dev/null
if [ -d "$PROJ/content/books" ]; then
  cp -f "$PROJ/content/books/"*.json "$PRIMARY/content/books/" 2>/dev/null
fi

# 4) Purge : ne garder que les 12 snapshots les plus récents (économie d'espace)
ls -1t "$PRIMARY/snapshots/" 2>/dev/null | tail -n +13 | while read -r f; do
  rm -f "$PRIMARY/snapshots/$f"
done

SIZE=$(du -h "$PRIMARY/minhaj-latest.tar.gz" 2>/dev/null | cut -f1)
echo "✅ Sauvegarde $STAMP → $PRIMARY/minhaj-latest.tar.gz ($SIZE)"
echo "   + copie secondaire : $SECONDARY/minhaj-latest.tar.gz"
echo "   Snapshots conservés : $(ls -1 "$PRIMARY/snapshots/" 2>/dev/null | wc -l)"

# 5) Pousse GitHub (règle de vague R201 : GitHub = source de vérité, jamais >1 leçon non poussée)
cd "$PROJ"
if git remote get-url origin >/dev/null 2>&1; then
  UNPUSHED=$(git rev-list --count origin/main..HEAD 2>/dev/null || echo "?")
  if [ "${UNPUSHED:-0}" != "0" ] && [ "${UNPUSHED:-0}" != "?" ]; then
    if timeout 90 git push origin main 2>/dev/null; then
      echo "   ✅ Pousse GitHub : ${UNPUSHED} commit(s) → origin/main"
    else
      echo "   ⚠️  Pousse GitHub IMPOSSIBLE (${UNPUSHED} commit(s) en attente) — token absent/révoqué ?"
      echo "       → demander le token à l'utilisateur ; lecture/sync restent possibles sans token."
    fi
  else
    echo "   ✅ GitHub déjà à jour (origin/main)."
  fi
fi
# 6) Bundle de récupération EXTERNE (leçon des resets des 24-25 oct. :
#    /home/z/my-project est restauré à un état ancien à chaque réinitialisation
#    du bac à sable, mais /tmp/my-project a SURVÉCU — c'est lui qui a permis
#    la restauration R213/R216). Bundle git complet + worklog + registre,
#    régénéré seulement si HEAD est plus récent que le bundle existant.
BUNDLED=/tmp/my-project/backup-tour
if mkdir -p "$BUNDLED" 2>/dev/null && [ -d "$PROJ/.git" ]; then
  HEAD_TS=$(git -C "$PROJ" log -1 --format=%ct 2>/dev/null || echo 0)
  BDL_TS=0
  [ -f "$BUNDLED/latest-bundle.bdl" ] && BDL_TS=$(stat -c %Y "$BUNDLED/latest-bundle.bdl" 2>/dev/null || echo 0)
  if [ "${HEAD_TS:-0}" -gt "${BDL_TS:-0}" ]; then
    if git -C "$PROJ" bundle create "$BUNDLED/latest-bundle.bdl" HEAD main >/dev/null 2>&1; then
      cp -f "$PROJ/worklog.md" "$BUNDLED/worklog.md" 2>/dev/null || true
      cp -f "$PROJ/scripts-translate/savant-registry.json" "$BUNDLED/savant-registry.json" 2>/dev/null || true
      echo "   ✅ Bundle de récupération externe → $BUNDLED/latest-bundle.bdl (+ worklog + registre)"
    else
      echo "   ⚠️  Bundle externe impossible à créer (espace disque ?)"
    fi
  else
    echo "   ✅ Bundle de récupération externe déjà à jour ($BUNDLED/latest-bundle.bdl)"
  fi
fi

echo "   ⚠️  Rappel : le commit git reste la protection n°1 (lancer si modifications en cours)."

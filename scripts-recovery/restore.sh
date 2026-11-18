#!/usr/bin/env bash
# Minhāj — Restauration depuis la dernière sauvegarde (/home/z/.minhaj-backup/).
# Usage: bash scripts-recovery/restore.sh
set -euo pipefail

BACKUP_DIR=/home/z/.minhaj-backup
LATEST="$BACKUP_DIR/minhaj-latest.tar.gz"

if [ ! -f "$LATEST" ]; then
  echo "✗ Aucune sauvegarde trouvée dans $BACKUP_DIR"
  exit 1
fi

echo "→ Restauration de $LATEST …"
tar -xzf "$LATEST" -C /home/z
echo "✅ Restauré : content/, worklog.md, scripts, src/, tr-src/, tr-out/ (selon contenu de la sauvegarde)."
echo "  Après restauration : ne JAMAIS redémarrer le serveur dev (port 3000)."

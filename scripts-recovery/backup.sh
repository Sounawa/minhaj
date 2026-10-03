#!/usr/bin/env bash
# Minhāj — Sauvegarde multi-emplacements.
# À lancer à CHAQUE vague de travail (règle utilisateur, session du 3 oct.).
#
# Cible : /home/z/.minhaj-backup/ (dossier caché hors my-project — ces dossiers
# ont survécu à la réinitialisation du 3 octobre 2026, contrairement à
# /home/z/my-project et aux dossiers non cachés).
set -uo pipefail

STAMP=$(date +%Y%m%d-%H%M%S)
PROJ=/home/z/my-project
BACKUP_DIR=/home/z/.minhaj-backup
SRC=/home/z/tr-src
OUT=/home/z/tr-out

mkdir -p "$BACKUP_DIR/snapshots"

# 1) Snapshot tarball horodaté (contenu + journaux + scripts + travail de traduction)
ITEMS=()
[ -d "$PROJ/content" ] && ITEMS+=("my-project/content")
[ -f "$PROJ/worklog.md" ] && ITEMS+=("my-project/worklog.md")
[ -d "$PROJ/scripts-translate" ] && ITEMS+=("my-project/scripts-translate")
[ -d "$PROJ/scripts-recovery" ] && ITEMS+=("my-project/scripts-recovery")
[ -d "$PROJ/src" ] && ITEMS+=("my-project/src")
[ -f "$PROJ/package.json" ] && ITEMS+=("my-project/package.json")
[ -d "$SRC" ] && ITEMS+=("tr-src")
[ -d "$OUT" ] && ITEMS+=("tr-out")

if [ ${#ITEMS[@]} -eq 0 ]; then
  echo "✗ Rien à sauvegarder."
  exit 1
fi

tar -czf "$BACKUP_DIR/snapshots/minhaj-$STAMP.tar.gz" -C /home/z "${ITEMS[@]}" 2>/dev/null
cp -f "$BACKUP_DIR/snapshots/minhaj-$STAMP.tar.gz" "$BACKUP_DIR/minhaj-latest.tar.gz"

# 2) Copie directe du worklog (accès rapide sans décompression)
[ -f "$PROJ/worklog.md" ] && cp -f "$PROJ/worklog.md" "$BACKUP_DIR/worklog-latest.md"

# 3) Copie directe du manifeste et de la file
mkdir -p "$BACKUP_DIR/content"
[ -f "$PROJ/content/manifest.json" ] && cp -f "$PROJ/content/manifest.json" "$BACKUP_DIR/content/"
[ -f "$PROJ/content/agent-queue.json" ] && cp -f "$PROJ/content/agent-queue.json" "$BACKUP_DIR/content/"
if [ -d "$PROJ/content/books" ]; then
  mkdir -p "$BACKUP_DIR/content/books"
  cp -f "$PROJ/content/books/"*.json "$BACKUP_DIR/content/books/" 2>/dev/null
fi

# 4) Purge : ne garder que les 15 snapshots les plus récents
ls -1t "$BACKUP_DIR/snapshots/" 2>/dev/null | tail -n +16 | while read -r f; do
  rm -f "$BACKUP_DIR/snapshots/$f"
done

SIZE=$(du -h "$BACKUP_DIR/minhaj-latest.tar.gz" 2>/dev/null | cut -f1)
echo "✅ Sauvegarde $STAMP → $BACKUP_DIR/minhaj-latest.tar.gz ($SIZE)"
echo "   Snapshots conservés : $(ls -1 "$BACKUP_DIR/snapshots/" 2>/dev/null | wc -l)"

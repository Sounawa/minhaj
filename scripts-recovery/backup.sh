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
echo "   ⚠️  Rappel : le commit git reste la protection n°1 (lancer si modifications en cours)."

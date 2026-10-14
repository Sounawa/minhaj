#!/bin/bash
# Minhāj — refresh /tmp/my-project/backup-tour/ (règle b : après CHAQUE document)
set -e
cd /home/z/my-project
cp scripts-translate/savant-registry.json /tmp/my-project/backup-tour/
cp worklog.md /tmp/my-project/backup-tour/ 2>/dev/null || true
rm -f /tmp/my-project/backup-tour/latest-bundle.bdl
git bundle create /tmp/my-project/backup-tour/latest-bundle.bdl HEAD 2>&1 | grep -v "^$" > /dev/null || git bundle create /tmp/my-project/backup-tour/latest-bundle.bdl HEAD
# R73 : push GitHub (origin = Sounawa/minhaj) — credential store configuré
if git remote get-url origin 2>/dev/null | grep -q "github.com"; then
  git push origin HEAD 2>/dev/null || echo "⚠︎ push GitHub échoué (réseau ?) — bundle /tmp reste valable"
fi
echo "backup OK: $(git log --oneline -1 | cut -c1-40)"

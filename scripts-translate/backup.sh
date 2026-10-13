#!/bin/bash
# Minhāj — refresh /tmp/my-project/backup-tour/ (règle b : après CHAQUE document)
set -e
cd /home/z/my-project
cp scripts-translate/savant-registry.json /tmp/my-project/backup-tour/
cp worklog.md /tmp/my-project/backup-tour/ 2>/dev/null || true
rm -f /tmp/my-project/backup-tour/latest-bundle.bdl
git bundle create /tmp/my-project/backup-tour/latest-bundle.bdl HEAD 2>&1 | grep -v "^$" > /dev/null || git bundle create /tmp/my-project/backup-tour/latest-bundle.bdl HEAD
echo "backup OK: $(git log --oneline -1 | cut -c1-40)"

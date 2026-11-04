#!/bin/bash
# R564 — lecture VLM avec reprises (429/quota) : tries up to N times with pauses.
IMG="$1"; OUT="$2"; PROMPT="$3"; TRIES="${4:-6}"
for i in $(seq 1 "$TRIES"); do
  echo "essai $i/$TRIES $(date -u +%H:%M:%SZ)" >&2
  node /home/z/my-project/tr-tmp/vlm-read-r564.mjs "$IMG" "$PROMPT" "$OUT" && exit 0
  echo "echec $i — pause 25s" >&2
  sleep 25
done
echo "VLM définitivement bloqué pour $IMG" >&2
exit 1

#!/bin/bash
# batch-vlm.sh <out.json> <prompt> <img1> [img2...]
OUT="$1"; PROMPT="$2"; shift 2
for attempt in 1 2 3 4 5 6 7 8; do
  if timeout 240 z-ai vision -p "$PROMPT" "$@" -o "$OUT" >/dev/null 2>&1; then
    echo "OK tentative $attempt → $OUT"; exit 0
  fi
  echo "429/échec tentative $attempt — pause 75s"; sleep 75
done
echo "ÉCHEC définitif → $OUT"; exit 1

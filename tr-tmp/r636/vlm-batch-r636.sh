#!/usr/bin/env bash
# R636 — lectures VLM batch leçon 394 (pages 39-44), méthode r634
cd /home/z/my-project
FULLP="Page d'un manuel arabe de hadith, leçon « أحكام الإهلال بالتلبية » (les règles de l'ihlāl par la talbiya). Transcris EXACTEMENT tout le texte imprimé visible, de haut en bas, en arabe, diacritiques inclus quand lisibles. Les références entre crochets bleus [الموطأ رقم: NNN] : transcris le numéro chiffre par chiffre tel qu'imprimé. Marque toute zone illisible par [ILLISIBLE]. Transcris SEULEMENT ce qui est visible — ne complète jamais de mémoire. Aucun commentaire, aucune traduction."

for p in 039 040 041 042 043 044; do
  f="tr-tmp/r636/read-p${p}-full.txt"
  if [ ! -s "$f" ]; then
    echo "== page $p =="
    timeout 180 z-ai vision -p "$FULLP" -i "tr-tmp/r636/p${p}-300.png" -o "tr-tmp/r636/tmp-v.json" >/dev/null 2>&1
    python3 -c "
import json
try:
    d=json.load(open('tr-tmp/r636/tmp-v.json'))
    print(d['choices'][0]['message']['content'])
except Exception as e:
    print('ERREUR_LECTURE',e)" > "$f"
    sleep 20
  fi
done
echo "lectures batch r636 terminées"

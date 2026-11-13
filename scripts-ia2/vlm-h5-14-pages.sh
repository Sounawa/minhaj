#!/bin/bash
# Z2-15 — hadith-5ep leçon 13 (يُسْرُ الإسلام) — lectures VLM pages 74-79 via CLI z-ai
set -u
DIR=/home/z/my-project/scripts-ia2/tmp/h5-14

PROMPT() {
cat <<'EOF'
Page d'un manuel scolaire marocain d'hadith (arabe, sens de lecture droite→gauche), 5e année primaire. Il s'agit de la leçon 14 « دعم وتطبيق » (consolidation et application), leçon de synthèse des leçons précédentes : le texte composé rappelle que l'homme est une créature honorée (خَلَقَهُ مِنْ تُرَابٍ), le rang du cœur, l'interdiction de l'usure (الربا), la recommandation sincère dans la fraternité, avec le hadith « عَلَيْكُمْ بِسُنَّتِي وَسُنَّةِ الْخُلَفَاءِ الرَّاشِدِينَ » et « لَوْ » de Muslim.

Transcris la page ENTIÈRE en arabe, fidèlement, mot à mot :
- Respecte la structure : أهداف الدرس، النص، الفهم (أشرح/أذكر)، التحليل، التطبيق، الإعداد القبلي.
- Marque chaque titre de rubrique avec [TITRE] … [/TITRE]. Marque les encadrés avec [CADRE] … [/CADRE].
- Ne saute AUCUNE phrase. Un mot illisible : écris [؟]. Ne devine pas au-delà de ce qui est imprimé.
- Garde la vocalisation diacritique telle qu'imprimée. Les citations coraniques et hadiths avec leur référence imprimée entre crochets.

Réponds UNIQUEMENT avec la transcription structurée, sans commentaire.
EOF
}

for PG in 080 081 082; do
  OUT="$DIR/vlm-p-$PG.txt"
  if [ -s "$OUT" ]; then echo "skip $PG (déjà lu)"; continue; fi
  echo "=== lecture p-$PG ==="
  z-ai vision -p "$(PROMPT)" -i "$DIR/p-$PG.png" -o "$DIR/vlm-p-$PG.json" > /dev/null 2>&1
  if [ -s "$DIR/vlm-p-$PG.json" ]; then
    python3 -c "
import json,sys
d=json.load(open('$DIR/vlm-p-$PG.json'))
c = d.get('content') if isinstance(d,dict) else None
if c is None and isinstance(d,dict): c = d.get('choices',[{}])[0].get('message',{}).get('content') if d.get('choices') else str(d)
open('$OUT','w').write(c or str(d))
print('OK p-$PG', len(c or ''))
"
  else
    echo "ÉCHEC p-$PG"
  fi
done

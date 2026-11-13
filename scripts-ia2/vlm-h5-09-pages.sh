#!/bin/bash
# Z2-9 — hadith-5ep leçon pdf-9 (الإحداث والابتداع في الدين) — lectures VLM pages 56-59 via CLI z-ai
set -u
DIR=/home/z/my-project/scripts-ia2/tmp/h5-09

PROMPT() {
cat <<'EOF'
Page d'un manuel scolaire marocain d'hadith (arabe, sens de lecture droite→gauche), 5e année primaire. Il s'agit de la leçon 9 « الإحداث والابتداع في الدين » (l'innovation dans la religion), fondée sur le hadith 7 des Quarante d'al-Nawawi, celui de la mère des croyants ʿĀʾiša : « مَنْ أَحْدَثَ فِي أَمْرِنَا هَذَا مَا لَيْسَ مِنْهُ فَهُوَ رَدٌّ » [صحيح البخاري ومسلم], avec la version de Muslim « مَنْ عَمِلَ عَمَلًا عَلَيْهِ لَيْسَ عَلَيْهِ أَمْرُنَا فَهُوَ رَدٌّ », et le commentaire (شرح) d'Ibn Daqiq al-'id.

Transcris la page ENTIÈRE en arabe, fidèlement, mot à mot :
- Respecte la structure : titres de rubriques (أهداف الدرس، التمهيد، نصوص الدروس، المصطلحات، الفهم، التحليل، التقويم، الاستثمار، الإعداد القبلي …), paragraphes, listes numérotées, encadrés, tableaux.
- Marque chaque titre de rubrique avec [TITRE] … [/TITRE].
- Marque chaque encadré/décoration avec [CADRE] … [/CADRE].
- Ne saute AUCUNE phrase. Un mot illisible : écris [؟]. Ne devine pas au-delà de ce qui est imprimé.
- Garde la vocalisation diacritique telle qu'imprimée.
- Les citations coraniques et hadiths : transcris-les telles qu'imprimées, avec leur référence imprimée entre crochets si présente.

Réponds UNIQUEMENT avec la transcription structurée, sans commentaire.
EOF
}

for PG in 056 057 058 059; do
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

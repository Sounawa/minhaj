#!/bin/bash
# reprise-portail.sh — KIT DE REPRISE (créé R433, 2026-10-30 ~20:10 +08:00)
# À lancer UNIQUEMENT quand veille-portail.sh répond PORTE|OUVERTE.
# Mission : qualifier la nouvelle structure du portail en 3 sondes rapides,
# écrire un rapport daté, et donner la marche suivante.
#   Sonde A : l'accueil répond et n'est plus la page de maintenance ?
#   Sonde B : liens détectés à la surface de l'accueil (dont PDF) ?
#   Sonde C : les ANCIENNES URL des 5 arbres morts (redirections ? redirects 301 ?)
# Sortie : scripts-translate/reprise-rapport.txt (horodaté, écrasé à chaque exécution)

H="https://www.habous.gov.ma/"
RAPPORT="/home/z/my-project/scripts-translate/reprise-rapport.txt"

echo "== REPRISE PORTAIL — $(date -u '+%Y-%m-%d %H:%M UTC') ==" | tee "$RAPPORT"

# Sonde A : accueil
code=$(curl -ksS -o /tmp/accueil-nouveau.html -w "%{http_code}" --max-time 25 "$H" 2>/dev/null)
taille=$(wc -c < /tmp/accueil-nouveau.html 2>/dev/null || echo 0)
echo "A|ACCUEIL|$code|$taille octets" | tee -a "$RAPPORT"

# Sonde B : liens de surface
liens=$(grep -oE 'href="[^"]+"' /tmp/accueil-nouveau.html 2>/dev/null | sed 's/href="//;s/"$//' | sort -u)
nb_liens=$(echo "$liens" | grep -c . || true)
nb_pdf=$(echo "$liens" | grep -ci '\.pdf' || true)
echo "B|LIENS|$nb_liens liens distincts dont $nb_pdf PDF" | tee -a "$RAPPORT"
echo "$liens" | grep -i '\.pdf\|درس\|عتيق\|تعليم' | head -20 >> "$RAPPORT" 2>/dev/null

# Sonde C : échantillon des anciens arbres morts (1 par arbre)
declare -a ANCIENNES=(
  "https://www.habous.gov.ma/images/2024/التعليم-العتيق/دروس-التعليم-العتيق/الفرائض-الثالثة-ثانوي/2B0631.PDF"
  "https://www.habous.gov.ma/images/2026/التعليم-العتيق/دروس-التعليم-العتيق/الفكر-الإسلامي-الثانية-ثانوي/142.PDF"
  "https://www.habous.gov.ma/images/2025/المديريات/مراكش/الحديث-الثانية-بكالوريا/1.PDF"
  "https://www.habous.gov.ma/images/2017/التعليم_العتيق_ومحو_الأمية_بالمساجد/التفسير-الثالثة-ثانوي/586.PDF"
  "https://www.habous.gov.ma/images/2024/المندوبيات/علوم-الحديث-الثالثة-ثانوي/1.PDF"
)
i=0
for u in "${ANCIENNES[@]}"; do
  i=$((i+1))
  c=$(curl -ksS -o /dev/null -w "%{http_code}" --max-time 20 "$u" 2>/dev/null)
  echo "C|ARBRE$i|$c|$(echo "$u" | cut -d/ -f4-6 | head -c 60)" | tee -a "$RAPPORT"
done

# Synthèse
if echo "$code" | grep -q "200" && [ "$nb_liens" -gt 5 ]; then
  echo "SYNTHÈSE: NOUVEAU PORTAIL VIVANT — commencer le re-mapping des 853 leçons" | tee -a "$RAPPORT"
  echo "MARCHES SUIVANTES : (1) crawler la nouvelle structure ; (2) re-mapper content/books/*.json ; (3) reprendre la chaîne OCR sur faraid-tanawi-3 lessons[1]." | tee -a "$RAPPORT"
else
  echo "SYNTHÈSE: signal partiel — investiguer manuellement avant re-mapping" | tee -a "$RAPPORT"
fi

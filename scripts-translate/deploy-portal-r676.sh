#!/bin/bash
# Minhāj — R676 (ouvrier D, tick 499559) : déploiement du portail en production
# standalone VERS LA ZONE STABLE /home/z/standalone-minhaj (hors évinceur).
#
# Contexte machine (R603/R606/R662/R673-b/R676) : l'évinceur du sandbox vide
# périodiquement node_modules et .next de /home/z/my-project (déclenché par
# disque plein — R606 ; cycles ~1-2 min — R662). Recette R603 : deps à
# /home/z/node_modules (copie de package.json+bun.lock à /home/z, install là).
# R676 : le build webpack part de ces deps ; prisma generate va vers
# /home/z/node_modules/.prisma/client (résolution par remontée d'arbre depuis
# @prisma/client) ; le standalone (server.js + .next/server + static) vit à
# /home/z/standalone-minhaj ; server.js est patché pour process.cwd() =
# /home/z/my-project (content/ du portail lu EN DIRECT sur le vrai projet —
# les livraisons registry sont visibles immédiatement, sans re-déploiement).
#
# Usage : bash scripts-translate/deploy-portal-r676.sh
# (idempotent — tue l'ancien serveur :3000, rebuild, redéploie, health-check)
S=/home/z/standalone-minhaj
PROJ=/home/z/my-project
NEXT=/home/z/node_modules/.bin/next

# 0) deps de la zone stable présentes ? (recette R603)
if [ ! -x "$NEXT" ]; then
  echo "ABSENCE /home/z/node_modules — recette R603 : copier package.json+bun.lock à /home/z puis « cd /home/z && bun install »"
  exit 2
fi
if [ ! -f /home/z/node_modules/.prisma/client/default.js ]; then
  echo "prisma client absent — génération vers /home/z/node_modules/.prisma/client"
  (cd $PROJ && /home/z/node_modules/.bin/prisma generate --output /home/z/node_modules/.prisma/client) || exit 2
fi

for ATTEMPT in 1 2 3; do
  echo "== TENTATIVE $ATTEMPT — build webpack =="
  cd $PROJ || exit 2
  NODE_OPTIONS="--max-old-space-size=2560" "$NEXT" build --webpack || { echo "build échoué — retry"; continue; }
  [ -f .next/standalone/my-project/.next/BUILD_ID ] || { echo "standalone évincé avant copie — retry"; sleep 3; continue; }

  echo "== copie vers zone stable $S =="
  rm -rf $S
  mkdir -p $S/my-project/.next
  (cd .next/standalone/my-project && tar cf - --exclude=./content --exclude=./tr-tmp --exclude=./generated-audio --exclude=./generated-images --exclude=./tr-logs .) | (cd $S/my-project && tar xf -)
  (cd .next/standalone && tar cf - node_modules) | (cd $S && tar xf -)
  cp -r .next/static $S/my-project/.next/static
  cp $PROJ/.env $S/my-project/.env
  if [ ! -f $S/my-project/server.js ] || [ ! -f $S/my-project/.next/BUILD_ID ] || [ ! -d $S/my-project/.next/server ]; then
    echo "copie incomplète (évinceur) — retry"; sleep 3; continue
  fi

  echo "== patch chdir R676 (cwd sur le vrai projet) =="
  python3 - <<'PYEOF'
p = '/home/z/standalone-minhaj/my-project/server.js'
s = open(p, encoding='utf-8').read()
if 'R676' not in s:
    s = s.replace('process.chdir(__dirname)',
                  "// R676 - cwd sur le vrai projet : content/ lu en direct (livraisons visibles immediatement)\nprocess.chdir('/home/z/my-project')")
    open(p, 'w', encoding='utf-8').write(s)
    print('patch chdir R676 applique')
else:
    print('patch R676 deja present')
PYEOF

  echo "== (re)démarrage serveur production :3000 =="
  pkill -f "standalone-minhaj/my-project/server.js" 2>/dev/null
  sleep 1
  cd $PROJ
  (PORT=3000 HOSTNAME=0.0.0.0 DATABASE_URL="file:/home/z/my-project/db/custom.db" \
   NODE_OPTIONS="--max-old-space-size=1024" \
   nohup node $S/my-project/server.js > $PROJ/tr-tmp/next-start.log 2>&1 &)
  sleep 6
  CODE=$(curl -s -o /dev/null -w "%{http_code}" http://localhost:3000/ 2>/dev/null)
  ASSET=$(curl -s http://localhost:3000/ 2>/dev/null | grep -o '/_next/static/chunks/[^"]*\.js' | head -1)
  ACODE=$(curl -s -o /dev/null -w "%{http_code}" "http://localhost:3000$ASSET" 2>/dev/null)
  LCODE=$(curl -s -o /dev/null -w "%{http_code}" "http://localhost:3000/api/lessons/hadith-3es/pdf-mut23h2x-403" 2>/dev/null)
  echo "health: GET / = $CODE ; asset = $ACODE ; api lesson 403 = $LCODE"
  if [ "$CODE" = "200" ] && [ "$ACODE" = "200" ]; then
    echo "== PORTAIL OK (tentative $ATTEMPT) — serveur $S/my-project/server.js ==" 
    exit 0
  fi
  echo "health check échoué — retry"
done
echo "ÉCHEC déploiement après 3 tentatives"
exit 1

#!/bin/bash
set -e
PDF=content/textbooks-src/ulum-hadith-1-thanawi.pdf
# args: page y0 y1 name  (y in 300dpi px; crop rendered at 1200 dpi => x4)
crop(){ pg=$1; y0=$2; y1=$3; name=$4
  W=$(python3 -c "print(2550*4)"); Y0=$((y0*4)); H=$(((y1-y0)*4))
  pdftoppm -r 1200 -png -f $pg -l $pg -x 0 -y $Y0 -W $W -H $H $PDF tr-tmp/r611/crops/$name >/dev/null 2>&1
  TESSDATA_PREFIX=/tmp/tessdata tesseract tr-tmp/r611/crops/$name-$(printf '%d' $pg).png tr-tmp/r611/crops/$name -l ara --psm 6 2>/dev/null
  echo "=== $name (p$pg y$y0-$y1 @1200dpi) ==="
  cat tr-tmp/r611/crops/$name.txt
}
crop 137 0 160 c1-header137
crop 140 0 420 c8-header140
crop 137 1260 1600 c2-ibn-salah
crop 138 320 580 c3-ibn-rashid
crop 138 1560 1810 c4-hakim
crop 139 1040 1330 c5-alalai
crop 139 620 890 c6-aqili
crop 139 1600 1900 c7-ibn-mayn

#!/bin/bash
# usage: ocr263.sh PAGE Y0 Y1 [X0 X1] TAG [DPI]
P=$1; Y0=$2; Y1=$3; X0=${4:-0}; X1=${5:-612}; TAG=$6; DPI=${7:-1200}
S=$(python3 -c "print(int($DPI/72))")
X=$((X0*S)); Y=$((Y0*S)); W=$(( (X1-X0)*S )); H=$(( (Y1-Y0)*S ))
OUT=tr-tmp/r622-ocr/${TAG}-p${P}-${DPI}
pdftoppm -f $P -l $P -r $DPI -x $X -y $Y -W $W -H $H -singlefile -png content/textbooks-src/ulum-hadith-2-thanawi_text.pdf $OUT 2>/dev/null
for L in 6 4; do tesseract ${OUT}.png stdout -l ara --tessdata-dir scripts-translate/tessdata --psm $L 2>/dev/null | head -30 > ${OUT}-psm$L.txt; done
echo "### $TAG p$P y$Y0-$Y1 x$X0-$X1 dpi$DPI ###"; echo "--- psm6 ---"; cat ${OUT}-psm6.txt; echo "--- psm4 ---"; cat ${OUT}-psm4.txt

#!/bin/bash
# R564 — poller VLM : parcourt une file d'images à lire, une tentative toutes les ~100 s.
# Arrêt quand tout est lu ou quand le budget temps est épuisé (max minutes en $1).
MAXMIN="${1:-8}"
DIR=/home/z/my-project/tr-tmp/qa-crops-r564
QUEUE="$DIR/queue.txt"
DEADLINE=$(( $(date +%s) + MAXMIN*60 ))

declare -A PROMPTS
P132="Transcris fidèlement tout le texte arabe de cette page de manuel de haut en bas, mot à mot, ligne par ligne. Page 132, leçon 19 (زكاة خلطاء الماشية). Inclus : bandeau/titre du haut, les trois objectifs, paragraphe d'introduction (أرباب النعم...), citation de مالك «السنة عندنا...» avec numéro الموطأ entre crochets EXACT chiffre par chiffre, les questions (أحكام الخلطة...), le titre de la section des hadiths, et le premier hadith complet avec l'isnad et le numéro du الموطأ."
P133="Transcris fidèlement tout le texte arabe de cette page de manuel de haut en bas, mot à mot, ligne par ligne. Page 133. Inclus : la fin du premier hadith (وفي سائمة... إذا بلغت أربعين شاة شاة / وقال يحيى / رقم الموطأ), le hadith de عائشة (مالك عن يحيى بن سعيد عن محمد بن يحيى بن حبان عن القاسم بن محمد عن عائشة أن عمر...), son numéro الموطأ EXACT, le hadith suivant (مالك عن ثور بن زيد... عن ابن عبد الله بن سفيان), son numéro الموطأ EXACT, la traduction de la rapporteuse (عائشة أم المؤمنين...) et les gloses (السخلة/الربى/الماخض/الأكولة)."
P134="Transcris fidèlement tout le texte arabe de cette page de manuel de haut en bas, mot à mot. Page 134. Section شرح المفردات (حزرات؟ / كيان؟ / حافل: يقال حفلت الشاة... / الخليطان: الشريكان / كبوا عن الطعام؟ / عذل بين غذاء الغنم وخياره), puis استخلاص المضامين, puis le début du التحليل (أولا: زكاة خلطاء الماشية / الخلطاء وشروط الخلطة)."
P135="Transcris fidèlement tout le texte arabe de cette page de haut en bas, mot à mot. Page 135. Citations de مالك avec les numéros الموطأ EXACTS chiffre par chiffre (il y en a plusieurs), la citation d'عمر (وفي سائمة الغنم إذا بلغت أربعين شاة...) et la suite (زكاة الخلطاء : إذا كان لأحدهما أربعون شاة...)."
P136="Transcris fidèlement tout le texte arabe de cette page de haut en bas, mot à mot. Page 136. Citations de مالك avec numéros الموطأ EXACTS, la section الجمع والتفريق خشية الزكاة (قول عمر: لا يجمع بين متفرق...) avec ses deux numéros الموطأ et l'explication (وتفسير لا يجمع بين متفرق...), puis ثانيا: ما يخرج في زكاة الماشية (لزوم الوسط: قصة سفيان بن عبد الله الثقفي)."
P137="Transcris fidèlement tout le texte arabe de cette page de haut en bas, mot à mot. Page 137. La fin de l'explication (فبين عمر بهذا.../ وأصل هذا كله قوله لمعاذ: إياك وكرائم أموالهم — سنن أبي داود), la section النهي عن التضييق (hadith عائشة), التقويم (3 questions), الاستثمار (مالك عن يحيى بن سعيد عن محمد بن يحيى بن حبان... محمد بن مسلمة) avec son numéro الموطأ EXACT."
P138="Transcris fidèlement tout le texte arabe de cette page de haut en bas, mot à mot. Page 138. La section الاستعداد القبلي avec ses trois items."
P131="Transcris le texte arabe de cette page, surtout : la fin des questions du التقويم, la section الاستعداد القبلي (avec le hadith et la référence المسند), et les deux items (أبحث عن معنى... / أبحث عن أحكام زكاة الخلطة). Page 131, fin de la leçon 18."
P139="Transcris le début de cette page : le bandeau du titre (الدرس 20) et les أهداف الدرس numérotés, et le début du paragraphe d'introduction. Page 139, début de la leçon 20 (زكاة الثمار والحبوب)."

i=0
while [ $(date +%s) -lt $DEADLINE ]; do
  REMAIN=""
  while read -r name; do
    [ -z "$name" ] && continue
    out="$DIR/vlm-${name}.txt"
    if [ -s "$out" ]; then continue; fi
    img="$DIR/full-${name#p}.png"
    var="P${name#p}"
    prompt="${!var}"
    echo ">>> lecture $name ($(date -u +%H:%M:%SZ))"
    if node /home/z/my-project/tr-tmp/vlm-read-r564.mjs "$img" "$prompt" "$out"; then
      echo "OK $name ($(wc -c < "$out") octets)"
    else
      echo "echec $name — pause 100 s"; sleep 100
    fi
    REMAIN="$REMAIN $name"
  done < "$QUEUE"
  [ -z "$REMAIN" ] && echo "FILE COMPLETE" && exit 0
done
echo "BUDGET EPUISE — restant:$REMAIN"
exit 3

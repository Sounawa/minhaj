#!/bin/bash
# R564 — poller VLM doux : une page à la fois, pause 150 s entre échecs, 8 essais/page max.
DIR=/home/z/my-project/tr-tmp/qa-crops-r564
LOG=$DIR/poller2.log
ORDER="p132 p133 p135 p136 p137 p134 p131 p139"
for name in $ORDER; do
  out="$DIR/vlm-${name}.txt"
  [ -s "$out" ] && continue
  img="$DIR/full-${name#p}.png"
  case "$name" in
    p132) PROMPT="Transcris fidèlement tout le texte arabe de cette page de manuel, mot à mot, ligne par ligne, de haut en bas. Inclus : bandeau titre (الدرس 19), les trois أهداف, le paragraphe d'introduction, la citation de مالك «السنة عندنا...» avec le numéro الموطأ entre crochets EXACT chiffre par chiffre, les questions, le titre «أحاديث الدرس», et le début du premier hadith.";;
    p133) PROMPT="Transcris fidèlement tout le texte arabe de cette page, mot à mot. Fin du 1er hadith (وفي سائمة الغنم... / وقال يحيى / رقم الموطأ EXACT), hadith de عائشة (مالك عن يحيى بن سعيد عن محمد بن يحيى بن حبان عن القاسم بن محمد عن عائشة أن عمر...) avec numéro الموطأ EXACT, hadith de ثور بن زيد عن ابن عبد الله بن سفيان الثقفي complet mot à mot (لا تأخذوا...) avec numéro الموطأ EXACT, la ترجمة الراوية et les gloses (السخلة/الربى/الماخض/الأكولة/الجدعاء/الثنية).";;
    p134) PROMPT="Transcris fidèlement tout le texte arabe de cette page, mot à mot. Section شرح المفردات (حَزْرَات / كيان؟ / حَافل / الخليطان / كبوا عن الطعام / عذل بين غذاء الغنم وخياره), puis استخلاص المضامين, puis début du التحليل (أولا: زكاة خلطاء الماشية / الخلطاء وشروط الخلطة).";;
    p135) PROMPT="Transcris fidèlement tout le texte arabe de cette page, mot à mot. Citations de مالك avec numéros الموطأ EXACTS chiffre par chiffre (plusieurs [71x]), la citation d'عمر (وفي سائمة الغنم إذا بلغت أربعين شاة شاة...) et la section زكاة الخلطاء (إذا كان لأحدهما أربعون شاة... / الألف شاة... بحصتها).";;
    p136) PROMPT="Transcris fidèlement tout le texte arabe de cette page, mot à mot. Citation de مالك (الخليطان في الإبل...) avec numéro الموطأ EXACT, section الجمع والتفريق خشية الزكاة avec قول عمر (لا يجمع بين متفرق...) et ses numéros الموطأ EXACTS et l'explication (وتفسير لا يجمع بين متفرق... / الثلاثة الذين يكون لكل واحد منهم أربعون شاة / شاة واحدة), puis ثانيا: ما يخرج في زكاة الماشية (قصة سفيان بن عبد الله الثقفي).";;
    p137) PROMPT="Transcris fidèlement tout le texte arabe de cette page, mot à mot. La fin de l'explication (فبين عمر بهذا... / وأصل هذا كله قوله لمعاذ: إياك وكرائم أموالهم — سنن أبي داود), section النهي عن التضييق (hadith عائشة : مر على عمر...), التقويم (questions numérotées), الاستثمار (مالك عن يحيى بن سعيد عن محمد بن يحيى بن حبان... محمد بن مسلمة) avec numéro الموطأ EXACT, et la dernière ligne.";;
    p131) PROMPT="Transcris le texte arabe de cette page : la fin du التقويم (questions numérotées), la section الاستعداد القبلي (أحفظ أحاديث الدرس المقبل... أبحث عن معنى...) avec ses items numérotés et le renvoi [المستخرجة من الأسمعة... 924/429]. Page 131, fin de la leçon 18.";;
    p139) PROMPT="Transcris le début de cette page : le bandeau du titre (الدرس 20) et les أهداف الدرس numérotés, et le début du paragraphe d'introduction avec le numéro الموطأ EXACT. Page 139, début de la leçon 20 (زكاة الثمار والحبوب).";;
  esac
  for i in 1 2 3 4 5 6 7 8; do
    echo ">>> $name essai $i ($(date -u +%H:%M:%SZ))" >> "$LOG"
    if node /home/z/my-project/tr-tmp/vlm-read-r564.mjs "$img" "$PROMPT" "$out" >> "$LOG" 2>&1; then
      echo "OK $name ($(wc -c < "$out") octets)" >> "$LOG"; break
    fi
    echo "echec $name — pause 150 s" >> "$LOG"; sleep 150
  done
done
echo "POLL2 TERMINE $(date -u +%H:%M:%SZ)" >> "$LOG"

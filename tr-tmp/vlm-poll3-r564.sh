#!/bin/bash
# R564 — poller VLM doux détaché : une tentative toutes les ~120 s, dans l'ordre des zones critiques.
DIR=/home/z/my-project/tr-tmp/qa-crops-r564
LOG=$DIR/poller3.log
declare -A IMGS
IMGS[p132]="$DIR/full-132.png"
IMGS[p133]="$DIR/full-133.png"
IMGS[p135]="$DIR/full-135.png"
IMGS[p136]="$DIR/full-136.png"
IMGS[p137]="$DIR/full-137.png"
IMGS[mc137yam]="$DIR/mc-p137-yam-word2.png"
IMGS[mc133nisba]="$DIR/mc-p133-thawr-nisba.png"
IMGS[mc132num]="$DIR/mc-p132-num720-tight.png"
IMGS[mc133aghta]="$DIR/mc-p133-aghta-tight.png"
IMGS[mc137aghta]="$DIR/mc-p137-akhta-tight.png"
declare -A PROMPTS
PROMPTS[p132]="Transcris fidèlement tout le texte arabe de cette page de manuel, mot à mot, ligne par ligne, de haut en bas. Inclus : le bandeau titre (الدرس 19), les trois أهداف, le paragraphe d'introduction, la citation de مالك «السنة عندنا...» avec le numéro الموطأ entre crochets EXACT chiffre par chiffre, les questions, le titre «أحاديث الدرس», et le début du premier hadith."
PROMPTS[p133]="Transcris fidèlement tout le texte arabe de cette page, mot à mot. Fin du 1er hadith (وفي سائمة الغنم... / وقال يحيى / رقم الموطأ EXACT), hadith de عائشة (مالك عن يحيى بن سعيد عن محمد بن يحيى بن حبان عن القاسم بن محمد عن عائشة...) avec numéro الموطأ EXACT, hadith de مالك عن ثور بن زيد (النسبة الدِّيليّ؟) عن ابن عبد الله بن سفيان الثقفي... complet mot à mot (لا تأخذوا... بعثه مصدقا...) avec numéro الموطأ EXACT, la ترجمة الراوية et les gloses (السخلة/الربى/الماخض/الأكولة)."
PROMPTS[p135]="Transcris fidèlement tout le texte arabe de cette page, mot à mot. Citations de مالك avec numéros الموطأ EXACTS chiffre par chiffre (plusieurs), la citation d'عمر (في سائمة الغنم إذا بلغت أربعين شاة شاة) et le numéro de son crochet EXACT, et la section زكاة الخلطاء (إذا كان لأحدهما أربعون شاة... / الألف شاة... بحصتها)."
PROMPTS[p136]="Transcris fidèlement tout le texte arabe de cette page, mot à mot. Citation de مالك (الخليطان في الإبل...) sans numéro ?, section الجمع والتفريق خشية الزكاة avec قول عمر (لا يجمع بين متفرق...) et ses numéros الموطأ EXACTS et l'explication (وتفسير لا يجمع بين متفرق... النفر الثلاثة... / وتفسير قوله ولا يفرق بين مجتمع... مائة وشاة), puis ثانيا: ما يخرج في زكاة الماشية (قصة سفيان بن عبد الله الثقفي)."
PROMPTS[p137]="Transcris fidèlement tout le texte arabe de cette page, mot à mot. La fin de l'explication (فبين عمر بهذا... / وأصل هذا كله قوله لمعاذ: إياك وكرائم أموالهم — سنن أبي داود), section النهي عن التضييق (hadith عائشة: مر على عمر... ما أغطى؟), التقويم (questions numérotées), الاستثمار (مالك عن يحيى بن سعيد عن محمد بن يحيى بن حبان... محمد بن مسلمة الأنصاري كان [LE MOT EXACT] مصدقا) avec numéro الموطأ EXACT, et la dernière ligne."
PROMPTS[mc137yam]="Transcris EXACTEMENT les mots arabes de cette image : il s'agit de «... الأنصاري كان ??? مصدقا فيقول لرب المال...». Donne le mot entre كان et مصدقا lettre par lettre avec ses points."
PROMPTS[mc133nisba]="Transcris EXACTEMENT le nom et la nisba : «عن ثور بن زيد ال؟؟؟» — donne la nisba lettre par lettre avec ses points (الديلي أم الذيلي أم الأيادي ?)."
PROMPTS[mc132num]="Transcris exactement le numéro entre crochets [الموطأ رقم: ?] chiffre par chiffre."
PROMPTS[mc133aghta]="Transcris exactement les mots: «فقال عمر: ما ؟؟؟ هذه أهلها وهم طائعون» — le verbe après ما, lettre par lettre avec ses points."
PROMPTS[mc137aghta]="Transcris exactement les mots: «فقال عمر: ما ؟؟؟ هذه أهلها وهم طائعون» — le verbe après ما, lettre par lettre avec ses points."
ORDER="p132 p133 p135 p136 p137 mc137yam mc133nisba mc132num mc133aghta mc137aghta"
while : ; do
  DONEALL=1
  for name in $ORDER; do
    out="$DIR/vlm-${name}.txt"
    [ -s "$out" ] && continue
    DONEALL=0
    echo ">>> $name ($(date -u +%H:%M:%SZ))" >> "$LOG"
    if timeout 180 node /home/z/my-project/tr-tmp/vlm-read-r564.mjs "${IMGS[$name]}" "${PROMPTS[$name]}" "$out" >> "$LOG" 2>&1; then
      echo "OK $name ($(wc -c < "$out") octets)" >> "$LOG"
    else
      echo "echec $name — pause 120 s" >> "$LOG"
      sleep 120
    fi
  done
  [ "$DONEALL" = "1" ] && { echo "FILE COMPLETE $(date -u +%H:%M:%SZ)" >> "$LOG"; exit 0; }
done

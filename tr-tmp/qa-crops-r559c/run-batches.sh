#!/bin/bash
cd /home/z/my-project
B=tr-tmp/qa-crops-r559c
run_batch () { # $1=out $2=prompt, rest=images
  local OUT="$1"; local PROMPT="$2"; shift 2
  for a in $(seq 1 40); do
    if timeout 240 z-ai vision -p "$PROMPT" "$@" -o "$OUT" >/dev/null 2>&1; then
      echo "$(date -u +%H:%M:%SZ) OK $OUT (essai $a)" >> $B/batches.log; return 0
    fi
    sleep 60
  done
  echo "$(date -u +%H:%M:%SZ) ECHEC $OUT" >> $B/batches.log; return 1
}
echo "$(date -u +%H:%M:%SZ) démarrage lots" >> $B/batches.log
run_batch $B/vlm-B1.json "Page complète d'un manuel marocain (arabe), section supérieure. Transcris EXACTEMENT mot par mot : (1) le bandeau «أهداف الدرس» avec ses trois objectifs numérotés complets ; (2) le paragraphe d'introduction (tamhīd) qui suit, jusqu'à «الأحاديث». Sans corriger ni compléter." $B/../qa-crops-r559/read-p105.png
run_batch $B/vlm-B2.json "Quatre micro-crops haute résolution d'un manuel marocain (arabe), dans l'ordre. IMAGE 1 = biographie d'Abû Sa'îd al-Khudrî (tradition du transmetteur) avec années de décès et variantes «وقيل». IMAGE 2 = définitions du cours (ذود، أوسق، أوقية) avec des poids en dirhams et grammes. IMAGE 3 = définition du وسق avec un poids en kilogrammes. IMAGE 4 = fin de page (le seuil niṣāb, dînar, grammes). Pour CHAQUE image : transcris EXACTEMENT mot par mot le texte arabe, en transcrivant TOUS les nombres chiffre par chiffre EXACTEMENT tels qu'imprimés (l'ordre des chiffres compte !). Sans corriger ni compléter ; signale entre (parenthèses) tout caractère réellement illisible." $B/p106-Z2-106.jpg $B/p106-Z3-106.jpg $B/p107-Z1-107.jpg $B/p108-Z4-108.jpg
run_batch $B/vlm-B3.json "Deux micro-crops haute résolution d'un manuel marocain (arabe). IMAGE 1 = section «2- حكمها» d'une leçon sur la zakāt, avec une citation coranique entre ﴿ ﴾ suivie d'un renvoi entre crochets [سورة ...، الآية ...] puis le hadith des cinq piliers [صحيح البخاري]. IMAGE 2 = section «3- حكمتها» points د- et le verset final [سورة التوبة، الآية ...]. Transcris EXACTEMENT : pour CHAQUE verset, le texte complet mot par mot ET le renvoi imprimé EXACT (nom de sūra et numéro d'āya chiffre par chiffre). Transcris aussi le membre «و... لقلوب الناس» du point أ- si visible et le point د- complet. Sans corriger ni compléter." $B/p108-Z1-108.jpg $B/p108-Z3-108.jpg
run_batch $B/vlm-B4.json "Quatre micro-crops haute résolution d'un manuel marocain (arabe). IMAGE 1 = hadith de Mālik sur l'or et l'argent entre associés [الموطأ رقم ...]. IMAGE 2 = hadith «السنة التي لا اختلاف فيها عندنا...» [الموطأ رقم ...]. IMAGE 3 = cas de l'homme aux cent soixante dirhams et hadith des associés [الموطأ رقم ...]. IMAGE 4 = section «2- مرور الحول» avec le hadith d'Ibn ʿUmar [الموطأ رقم ...]. Pour CHAQUE image : transcris EXACTEMENT mot par mot tout le texte arabe visible, avec les numéros de hadith EXACTS chiffre par chiffre. Sans corriger ni compléter ; signale entre (parenthèses) tout caractère réellement illisible." $B/p106-Z1-106.jpg $B/p109-Z1-109.jpg $B/p109-Z2-109.jpg $B/p109-Z3-109.jpg
run_batch $B/vlm-B5.json "Deux micro-crops haute résolution d'un manuel marocain (arabe). IMAGE 1 = récit d'al-Qāsim b. Muḥammad sur Abū Bakr et la zakāt des allocations (عطاء), suivi de «حول الربح» avec citation de Mālik [الموطأ رقم ...]. IMAGE 2 = section «الاستثمار» avec citation de Mālik sur les cinq dînar [الموطأ رقم ...] et ses questions. Transcris EXACTEMENT mot par mot tout le texte arabe visible, avec le numéro de hadith EXACT chiffre par chiffre pour CHAQUE renvoi [الموطأ رقم ...]. Sans corriger ni compléter ; signale entre (parenthèses) tout caractère réellement illisible." $B/p110-Z1-110.jpg $B/p110-Z2-110.jpg
echo "$(date -u +%H:%M:%SZ) fin lots" >> $B/batches.log

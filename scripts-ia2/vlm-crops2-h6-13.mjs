// Z2-48 — adjudication VLM ronde 2 : 21 crops ciblés (bandeaux, mots litigieux, encadrés).
import ZAI from '/tmp/my-project/node_modules/z-ai-web-dev-sdk/dist/index.js';
import fs from 'fs';

const DIR = '/home/z/my-project/scripts-ia2/tmp/h6-13/crops';
const OUTDIR = '/home/z/my-project/scripts-ia2/tmp/h6-13/vlm-crops2';
fs.mkdirSync(OUTDIR, { recursive: true });

const BASE = `Image : extrait zoomé (1200 dpi) d'un manuel scolaire marocain de hadith (6e année, Arba'īn nawawiyya + commentaire d'Ibn Daqīq al-'Īd). Transcris le texte arabe visible MOT À MOT avec sa voyellisation imprimée, droite→gauche. Ne devine jamais : illisible → [؟]. Chiffres → NUM: <0-9>. ATTENTION aux points : ض (1 point au-dessus) ≠ ص (aucun) ; ر (aucun) ≠ ز (1 au-dessus) ; ق (2 points au-dessus, boucle haute) ≠ ف (1 point, boucle basse) ; ش (3 points) ≠ ب (1 point dessous). Réponds aux QUESTIONS en citant les lettres vues.`;

const QS = {
  'c20-p74-haut': `QUESTIONS : 1) Décris TOUT ce qui est visible de haut en bas : bandeaux, titres, tableaux (en-têtes, colonnes, cases vides ou pleines), phrases. 2) Y a-t-il un bandeau coloré ? Quel texte ? 3) Y a-t-il un tableau avec les en-têtes «حق النفس / حق الغير / حق البيئة» ? Combien de colonnes, combien de rangées, vides ou remplies ? 4) Transcris toute phrase ou consigne visible.`,
  'c21-enc1': `QUESTIONS : 1) Transcris la phrase de cet encadré MOT À MOT avec voyelles. C'est probablement «أطهر نفسي من الرذائل وأ...ها بالإيمان» ou similaire. 2) Le 2e verbe après «و» : lettre par lettre — «أربّيها» (ر-ب-ّ-ي-ها) ou «أركبها» (ر-ك-ب-ها) ou autre ? 3) Le premier verbe : «أطهر» ou «أظهر» ou autre ?`,
  'c22-enc2': `QUESTIONS : 1) Transcris la phrase de cet encadré MOT À MOT. C'est probablement «أحافظ على نظافة جسمي ووقايته من الأمراض». 2) Confirme chaque mot lettre par lettre.`,
  'c23-enc3': `QUESTIONS : 1) Transcris la phrase de cet encadré MOT À MOT. Elle commence par «أتجنب ...». 2) Le mot après «أتجنب» : lettre par lettre (إيذاء الآخرين؟ بجهلي؟ autre chose ?). 3) La fin de la phrase exactement.`,
  'c25-enc6': `QUESTIONS : 1) Transcris la phrase de cet encadré MOT À MOT. Elle commence par «أحرص على ...». 2) Le mot après «على» : «استغلال» ou «استعمال» ? lettre par lettre (غ ou م ?). 3) «الموارد البيئية» ou «الموارد البيئة» ? 4) Le dernier mot : «باعتدال» exactement ?`,
  'c26-items12': `QUESTIONS : 1) Transcris l'item «NUM:1- ...» ENTIER : le 1er mot est «أبين» ou «أبين» — voyelle sur le alef : fatha (أَ) ou damma (أُ) ? et sur le ب : shadda ? 2) Transcris l'item «NUM:2- ...» ENTIER : le 1er mot après «أ» : «مثل» — voyelle du mîm : fatha (أَمَثِّلُ) ou damma (أُمَثِّلُ) ou sukûn (أُمْثِلْ) ? shadda sur le ث ? 3) La fin de l'item 2 : «من واقعي» exactement ?`,
  'c27-tab-bas-r14': `QUESTIONS : 1) Transcris les rangées visibles de la première colonne. 2) Rangée 1 : «إيذاء الجيران» — le mot après «إ» : lettre par lettre («يذاء» avec yâ' ou autre ?). 3) La DERNIÈRE rangée visible : transcris-la lettre par lettre — commence par «رمي» (râ'-mîm-yâ') ou «رحمة» (râ'-ḥā'-mîm-tâ') ? Le mot suivant : «الأزبال» (alef-lām-zāy-bā'-alef-lām) ou autre ? 4) Y a-t-il une rangée sous la dernière visible ?`,
  'c28-band-tamhid': `QUESTIONS : 1) Transcris le texte du bandeau calligraphié coloré. Un seul mot ou deux ?`,
  'c29-band-hadith': `QUESTIONS : 1) Transcris le texte du bandeau calligraphié coloré. Un seul mot ou deux ?`,
  'c30-band-sharh': `QUESTIONS : 1) Transcris le texte du bandeau calligraphié coloré visible (probablement الشرح).`,
  'c31-band-tahlil': `QUESTIONS : 1) Transcris le texte du bandeau calligraphié coloré visible (probablement التحليل). 2) Y a-t-il autre chose écrit sur cette image ?`,
  'c32-tamhid-l1': `QUESTIONS : 1) Transcris la ligne ENTIÈRE. 2) CRUCIAL : le 3e mot (après «جاء الإسلام ليرفع») : lettre par lettre — «الشرَّ» (shîn-râ'-râ' avec shadda) ou «الضررَ» (dâd-râ'-râ' sans shadda) ou «الصدر» ? Décris la 1re lettre du mot (3 points dessus = ش ? 1 point dessus = ض ?) et dis s'il y a une shadda.`,
  'c33-glose2': `QUESTIONS : 1) Transcris la ligne ENTIÈRE. 2) CRUCIAL : le dernier mot : «مجاراةً» (jîm-alef-RÂ' sans point-alef-tâ' marbûta) ou «مجازاةً» (jîm-alef-ZÂ' avec 1 point-alef-tâ' marbûta) ? Y a-t-il un point au-dessus de la 3e lettre de la racine ?`,
  'c34-famaana': `QUESTIONS : 1) Transcris les 2 lignes visibles. 2) «لا يدخل» : la voyelle finale de «يدخل» — damma (يُدْخِلُ) ou sukûn (يُدْخِلْ) ? 3) Le mot à la fin de la ligne 1 et celui de la ligne 2 («ضررا») : shadda sur le râ' ? un ou deux râ' ? tanwîn ? Décris précisément : ض-ر-?-?-ا.`,
  'c35-walbuduquf': `QUESTIONS : 1) Transcris la ligne ENTIÈRE. 2) CRUCIAL : le mot après «وبه.» ou «به.» : «والضرر» (dâd-râ'-râ') ou «والضرار» (dâd-râ'-ALEF-râ') ? Y a-t-il un alef entre les deux râ' ? 3) «بالوقوف عند الحق فيه» — transcris exactement.`,
  'c36-yashmal': `QUESTIONS : 1) Transcris la ligne ENTIÈRE. 2) Le verbe : «يشمل» (yâ'-shîn-mîm-lâm) ou «بشمل» (bâ'-shîn-mîl-lâm) ? 3) Le dernier mot : «بغيره» ou «لغيره» ? 4) «علاقته» : la voyelle du 'ayn.`,
  'c37-ref-bukhari': `QUESTIONS : 1) Transcris la référence entre crochets EN ENTIER lettre par lettre. 2) Y a-t-il «صحيح» avant «البخاري» ? 3) Après «كتاب» : quel mot exactement («العلم» ?) ? 4) La fin : «ليبلغ الشاهد الغائب» exactement ?`,
  'c38-maahu-inda': `QUESTIONS : 1) Transcris TOUT le texte visible (2-3 lignes). 2) La phrase commence par «وهذا معناه عند» — ensuite quoi ? Un nom d'auteur/savant ? 3) Transcris la ou les phrases complètes.`,
  'c39-band-istithmar': `QUESTIONS : 1) Transcris le texte du bandeau calligraphié coloré (probablement الاستثمار). 2) Transcris la première ligne visible sous le bandeau.`,
  'c40-ittaqu': `QUESTIONS : 1) Transcris la ligne ENTIÈRE. 2) CRUCIAL : le mot après «اتقوا» : «الملاعن» ou «اللاعنين» ou «اللعنتين» ? lettre par lettre. 3) Le mot qui suit : «الثلاث» (sans tâ' final) ou «الثلاثة» (avec tâ') ? 4) Après «:» : «البراز» (bâ'-râ'-ZÂ' final avec point) ou «البرار» (râ' final SANS point) ? 5) «في الموارد» ou «في المورد» ?`,
  'c41-iidad-mot': `QUESTIONS : 1) Transcris la ligne ENTIÈRE avec voyelles. 2) «أحفظ» : la dernière voyelle — damma (أَحْفَظُ) ou sukûn (أَحْفَظْ) ? 3) «وأبين» : «وأبين» (wâw-alef-bâ'-shadda-yâ'-nûn-damma = وأبيّن) ou «وأبين» (wâw-alef-bâ' sukûn-yâ' kasra-nûn sukûn = وأبْيِنْ) ? 4) «الدَّرْسِ الموالى» : la fin du dernier mot — yâ' avec 2 points dessous (الموالي) ou alif maqṣûra sans points (الموالى) ?`,
};

const TASKS = Object.keys(QS);

async function readOne(zai, tag) {
  const out = `${OUTDIR}/${tag}.txt`;
  if (fs.existsSync(out) && fs.statSync(out).size > 100) return `${tag}: déjà lu`;
  for (let k = 1; k <= 4; k++) {
    try {
      const b64 = fs.readFileSync(`${DIR}/${tag}.png`).toString('base64');
      const res = await zai.chat.completions.createVision({
        messages: [{ role: 'user', content: [
            { type: 'text', text: `${BASE}\n\n${QS[tag]}` },
            { type: 'image_url', image_url: { url: `data:image/png;base64,${b64}` } },
          ] }],
        thinking: { type: 'disabled' },
      });
      const txt = res.choices[0]?.message?.content || '(vide)';
      fs.writeFileSync(out, txt, 'utf-8');
      return `${tag}: OK (${txt.length} car)`;
    } catch (e) {
      const msg = String(e?.message || e);
      if (k === 4) { fs.writeFileSync(out, `ERREUR ${msg}`, 'utf-8'); return `${tag}: ERREUR ${msg.slice(0, 80)}`; }
      const wait = msg.includes('429') ? 20000 * k : 5000 * k;
      await new Promise(r => setTimeout(r, wait));
    }
  }
}

async function main() {
  const zai = await ZAI.create();
  for (const t of TASKS) console.log(await readOne(zai, t));
}
main().catch(e => { console.error('FATAL', e); process.exit(1); });

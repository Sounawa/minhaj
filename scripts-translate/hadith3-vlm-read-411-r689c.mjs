import ZAI from '/home/z/node_modules/z-ai-web-dev-sdk/dist/index.js';
import fs from 'fs';
const DIR = '/home/z/my-project/tr-tmp/qa-crops-r689c';
const OUTDIR = '/home/z/my-project/tr-tmp/vlm-411';
fs.mkdirSync(OUTDIR, { recursive: true });

const TASKS = [
  { tag: 'm411-p147', ctx: 'Page 147 du manuel (début de la leçon 22 « فدية قتل الجراد وحلق الرأس ») : médaillon, cadre des objectifs (الأهداف), puis le تمهيد et le premier hadith (n° 1252, Ka\'b b. \'Ajra).' },
  { tag: 'm411-p148', ctx: 'Page 148 : deuxième hadith (n° 1263, la bête tuée en commun), la notice du transmetteur (كعب بن عجرة), le شرح (gloses), puis la rubrique استخلاص المضامين en bas de page.' },
  { tag: 'm411-p149', ctx: 'Page 149 : fin du hadith (n° 1255), la section fiqh أولا: فدية حلق الرأس (le rasage pour excuse — madyān madyān), puis l\'āya d\'al-Baqara et l\'argument.' },
  { tag: 'm411-p150', ctx: 'Page 150 : le rasage délibéré (divergence des juristes — Mālik / Abū Ḥanīfa / ash-Shāfi\'ī), le hadith du cheveu aspiré ou de la épilation (n° 1256), puis ثانيا: اشتراك جماعة في الصيد.' },
  { tag: 'm411-p151', ctx: 'Page 151 : l\'étonnement du questionneur sur \'Umar, l\'āya d\'al-Mā\'ida et le dialogue d\'\'Umar (n° 1241 re-cité), puis استخلاص المضامين et le texte suivant.' },
  { tag: 'm411-p152', ctx: 'Page 152 : fin de leçon — l\'exploitation (كيف يمكن الجمع بين الروايتين؟) et l\'إعداد قبلي (les deux questions sur la \'umra).' },
  { tag: 'z411-1-p147-objectifs-tamhid-texte', ctx: 'Zoom p.147 haut : médaillon 22, les trois objectifs, le tamhīd et le début du hadith 1252.' },
  { tag: 'z411-2-p147-texte1252-fin', ctx: 'Zoom p.147 bas : la fin du hadith 1252 (اخلق رأسك وصم ثلاث أيام أو أطعم ستة مساكين أو أنسك بشاة) et son numéro.' },
  { tag: 'z411-3-p148-texte1263-notice-gloses', ctx: 'Zoom p.148 : le hadith 1263 entier, la notice de Ka\'b b. \'Ajra et les gloses (أنسك بشاة، قبضة).' },
  { tag: 'z411-4-p148-istihlas-hadith', ctx: 'Zoom p.148 bas : la rubrique استخلاص المضامين avec ses items numérotés, et le début du hadith suivant (1255).' },
  { tag: 'z411-5-p149-fidya-adhr', ctx: 'Zoom p.149 : la fin du hadith 1255, la section أولا: فدية حلق الرأس et la sentence « مدين مدين لكل إنسان » avec son numéro.' },
  { tag: 'z411-6-p149-aya-argument', ctx: 'Zoom p.149 bas : l\'āya d\'al-Baqara citée (avec son numéro d\'āya imprimé), le hadith des deux authentiques (« نزلت الآية خاضا وهلاكم عامة ») et l\'argument du manuel.' },
  { tag: 'z411-7-p150-amd-istishrak', ctx: 'Zoom p.150 : le hadith de l\'épilation (من تفل شعرا من أنفه أو من إبطه، بنورة، 1256), puis ثانيا: اشتراك جماعة في الصيد.' },
  { tag: 'z411-8-p150-151-adlan-umar', ctx: 'Zoom p.150 bas + p.151 haut : les deux juges (عدلان عالمان), \'Umar s\'aidant de \'Abd ar-Raḥmān b. \'Awf (1241), l\'étonnement du questionneur.' },
  { tag: 'z411-9-p151-maida-istihlas', ctx: 'Zoom p.151 : l\'āya d\'al-Mā\'ida (avec son numéro imprimé), le dialogue d\'\'Umar sur sourate al-Mā\'ida, puis استخلاص المضامين (les items) et le début du texte suivant.' },
  { tag: 'z411-10-p151-152-istithmar-iadad', ctx: 'Zoom p.151 bas + p.152 : l\'exploitation (كيف يمكن الجمع بين الروايتين؟) et l\'إعداد قبلي (les deux questions sur la \'umra).' },
];

const prompt = (c) => `Image d'une page (ou zoom) d'un manuel scolaire arabe imprimé (enseignement traditionnel, Muwaṭṭa'). ${c.ctx}

TRANSCRIPTION FIDÈLE EXIGÉE :
1. Transcris TOUT le texte arabe en ordre de lecture, en arabe UNICODE avec les harakat quand ils sont visibles.
2. Marque la STRUCTURE : [MÉDAILLON], [OBJECTIFS], [TAMHĪD], [TEXTE], [NOTICE], [GLOSSAIRE], [RÉSUMÉ], [FIQH], [ÉVALUATION], [EXPLOITATION], [PRÉPARATION].
3. Les numéros de hadith entre crochets bleus (ex : [الموطأ رقم: 1252]) et les numéros d'āya : transcris TELS QUE imprimés, chiffre par chiffre.
4. NE DEVINE JAMAIS : mot flou → mot + [?]. Pour les mots ambigus décris points/boucles.
5. Ne traduis PAS, ne commente PAS : transcris uniquement.`;

async function readOne(zai, t) {
  const out = `${OUTDIR}/${t.tag}.txt`;
  if (fs.existsSync(out) && fs.statSync(out).size > 200) return `${t.tag}: cache`;
  for (let k = 1; k <= 4; k++) {
    try {
      const b64 = fs.readFileSync(`${DIR}/${t.tag}.png`).toString('base64');
      const res = await zai.chat.completions.createVision({
        messages: [{ role: 'user', content: [
          { type: 'text', text: prompt(t) },
          { type: 'image_url', image_url: { url: `data:image/png;base64,${b64}` } },
        ] }],
        thinking: { type: 'disabled' },
      });
      const txt = res.choices[0]?.message?.content || '(vide)';
      fs.writeFileSync(out, txt, 'utf-8');
      return `${t.tag}: OK (${txt.length} car)`;
    } catch (e) {
      const msg = String(e?.message || e);
      if (k === 4) return `${t.tag}: ERREUR ${msg}`;
      await new Promise(r => setTimeout(r, msg.includes('429') ? 20000 * k : 5000));
    }
  }
}

async function main() { const zai = await ZAI.create(); for (const t of TASKS) console.log(await readOne(zai, t)); }
main().catch(e => { console.error('FATAL', e); process.exit(1); });

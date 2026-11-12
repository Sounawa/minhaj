import ZAI from '/home/z/my-project/node_modules/z-ai-web-dev-sdk/dist/index.js';
import fs from 'fs';
const DIR = '/home/z/my-project/tr-tmp/qa-crops-r688';
const OUTDIR = '/home/z/my-project/tr-tmp/vlm-410';
const TASKS = [
  { tag: 'm410-J-p141-bas', ask: `Zoom bas de page 141 d'un manuel arabe. Trois hadiths avec numéros [الموطأ رقم: 1240], [1242], [1243]. Transcris CHAQUE hadith lettre par lettre en arabe : 1) hadith رقم 1240 : liste les compensations (الضبع، الغزال، الأرنب، اليربوع) et les bêtes (كبش، عنز، عناق، جفرة) TELLES QU'imprimées. 2) hadith 1242 : la phrase « في البقرة من الوحش ... وفي الشاة من الظباء ... ». 3) hadith 1243 : le VERBE après « إذا » dans « في حمام مكة إذا ... » — est-ce قُتِّلَتْ (passif féminin, 2 zabras sous le ق) ou قَتَّلَ (actif intensif) ou autre ? Décris les diacritiques visibles. Ne devine pas.` },
  { tag: 'm410-C-p142-cadre', ask: `Zoom du cadre de hadiths de la page 142. Transcris EXACTEMENT le 1er hadith : « قال مالك في الرجل من أهل مكة ... » — lettre par lettre : après « وفي بيته فراخ من حمام مكة » le verbe est-il « فَيُغْلَقُ عَلَيْهَا » (youghlaq, با غين) ou « فَيُطْلَقُ عَلَيْهَا » (yutlaq, با طاء) ? Et la fin : « أرى بأن يُفدى ذلك عن كل فرخ بشاة » ? Décris le glyphe (boucle de غ avec point en haut + trait, ou ط avec point en haut). Ne devine pas.` },
  { tag: 'm410-H-p144-145', ask: `Zoom page 144-145. Question unique : dans le hadith du coureur « عن عبد ... بن ... عن محمد بن سيرين أن رجلا جاء إلى عمر », le premier nom de la chaîne (sanad) est-il « عبد الله بن قيس » ou « عبد الملك بن قيس » ou « عبد الملك بن قريز » ? Regarde lettre par lettre le premier nom propre : الله (3 lettres avec الشدة) vs الملك (5 lettres م ل ك). Et le second mot après بن : قيس ou قريز ou قيس؟ Ne devine pas, décris les points et boucles.` },
  { tag: 'm410-F-p143-fiqh2', ask: `Zoom page 143 section حكم الفدية. Transcris le hadith « قال مالك فيمن أراد أن يلبس شيئا من الثياب ... » lettre par lettre, surtout : après « أو يمسط/يمس طيبا من » — la phrase suivante exacte : « غير ضرورة؛ ليسارة مؤنة الفدية عليه » ou « لغير ضرورة » ou autre ? Et le numéro entre crochets : 1250 ou 1260 ? Regarde les chiffres un par un. Ne devine pas.` },
  { tag: 'm410-I-p145-146', ask: `Zoom page 145-146. Deux questions sur le hadith final de la page 146 (« ولا ... له (أي المحرم) أن يقلم أظفاره ... ») : 1) le premier mot après ولا : يَصْلُحُ (ص صاد sans point) ou يَضَلَّحُ (ض ضاد avec point) ? 2) ensuite : ولا يقتل قملة ولا يطرحها ou يطردُها ? 3) la fin : فليطعم حفنة من طعام ? Décris points et boucles. Ne devine pas.` },
];
async function readOne(zai, t) {
  const out = `${OUTDIR}/r689-${t.tag}.txt`;
  if (fs.existsSync(out) && fs.statSync(out).size > 150) return `${t.tag}: cache`;
  for (let k = 1; k <= 4; k++) {
    try {
      const b64 = fs.readFileSync(`${DIR}/${t.tag}.png`).toString('base64');
      const res = await zai.chat.completions.createVision({
        messages: [{ role: 'user', content: [
          { type: 'text', text: t.ask },
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

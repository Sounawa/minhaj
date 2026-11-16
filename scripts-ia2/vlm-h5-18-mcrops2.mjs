// Z2-20 — hadith-5ep leçon pdf-18 — microcrops v2 VLM
import ZAI from '/home/z/my-project/node_modules/z-ai-web-dev-sdk/dist/index.js';
import fs from 'fs';

const DIR = '/home/z/my-project/scripts-ia2/tmp/h5-18';

const ASKS = {
  'mc-m15-tamhid-l1-p98.jpg': `Ligne unique très zoomée d'un manuel arabe (تمهيد). Transcris-la LETTRE PAR LETTRE :
attendu : « في أصل ... ، فكلهم من آدم وآدم من تراب ، تجمعهم بهذا روابط متينة ... » — donne le texte EXACT (complément de « في أصل », le verbe exact avant « روابط », et le mot après « متينة »).`,
  'mc-m16-tamhid-l2-p98.jpg': `Ligne unique très zoomée. Transcris-la LETTRE PAR LETTRE. Attendu : « ... الإسلام على بنائها ... أخوة ومحبة شعارها : أن تحب لأخيك ما تحب ... » — donne le texte EXACT : le mot AVANT « الإسلام », le mot après « على », et la structure « على ... أخوة ومحبة شعارها ».`,
  'mc-m17-ayat-dalla-p98.jpg': `Fragment très zoomé : « ... من آيات الله ... على قدرته وعجيب صنعه ». Transcris LETTRE PAR LETTRE le mot entre « الله » et « على » (الدالة ? الجليلة ? البينات ?) et sa vocalisation exacte.`,
  'mc-m18-questions-p98.jpg': `Deux questions rhétoriques en fin de تمهيد, très zoomées. Transcris-les LETTRE PAR LETTRE, en particulier le verbe de la deuxième : « تجسدها ? تتجسدها ? تجسدها بها ? ».`,
  'mc-m19-duaa-fin-p99.jpg': `Invocation très zoomée : « اللهم بارك ... ». Transcris-la ENTIÈREMENT lettre par lettre jusqu'au dernier mot, surtout la fin : « ... وأطل عمره واغفر ... » — le dernier mot exact (له ? ذنبه ?).`,
  'mc-m20-yustafad3-fin-p102.jpg': `Fin du 3e item de « ومما يستفاد من الحديث », très zoomée : la ligne contient « ... يكون بالمحبة ويزداد ... ». Transcris LETTRE PAR LETTRE tout ce qui suit « ويزداد » (sur cette ligne et la suivante si visible).`,
  'mc-m21-taqwim1-p102.jpg': `Première question du تقويم, très zoomée. Transcris-la LETTRE PAR LETTRE depuis le début : après « هل », le mot exact : « حب » (ḥā-bā) ou « حدث » (ḥā-dāl-thā) ? Puis le reste jusqu'au point d'interrogation.`,
  'mc-m22-fudayl-fin-p100.jpg': `Citation de Fuḍayl ibn ʿIyāḍ très zoomée : « إن كنت تحب أن يكون الناس مثلك ، فما ... النصيحة ... كيف وأنت تحب أن يكونوا دونك ». Transcris LETTRE PAR LETTRE le segment entre « فما » et « كيف » : y a-t-il un verbe avant « النصيحة » (نصحت ? أدت ? بلغت ?) et le mot exact après « النصيحة » (لك ? لكَ ? rien ?).`,
};

async function main() {
  const zai = await ZAI.create();
  for (const [img, ask] of Object.entries(ASKS)) {
    const out = `${DIR}/z-${img.replace('.jpg', '.txt')}`;
    if (fs.existsSync(out)) { console.log(`skip ${img}`); continue; }
    const b64 = fs.readFileSync(`${DIR}/${img}`).toString('base64');
    try {
      const res = await zai.createChatCompletionVision({
        messages: [{ role: 'user', content: [
          { type: 'text', text: ask },
          { type: 'image_url', image_url: { url: `data:image/jpeg;base64,${b64}` } },
        ] }],
        model: 'glm-5v-turbo',
        max_tokens: 1500,
        temperature: 0.1,
      });
      const txt = res?.choices?.[0]?.message?.content ?? JSON.stringify(res);
      fs.writeFileSync(out, txt);
      console.log(`OK ${img} (${txt.length} car)`);
    } catch (e) {
      console.error(`ÉCHEC ${img}: ${e.message}`);
    }
  }
}
main().catch(e => { console.error(e); process.exit(1); });

// Z2-37 — fix5 (lecture unique): queue de l'item 3 de «مما يستفاد» p.22 (zone aveugle cmap).
import ZAI from '/home/z/my-project/node_modules/z-ai-web-dev-sdk/dist/index.js';
import fs from 'fs';
import { execSync } from 'child_process';

const DIR = '/home/z/my-project/scripts-ia2/tmp/h6-03';

const zai = await ZAI.create();
const nom = 'c22-item3';
const out = `${DIR}/vlm-${nom}.txt`;
if (!fs.existsSync(out)) {
  const S = 600 / 72.0;
  const fp = `${DIR}/crops/fix4/${nom}.png`;
  if (!fs.existsSync(fp)) {
    execSync(`python3 -c "
from PIL import Image
S=${S}
im=Image.open('${DIR}/r600/p22.png').convert('L')
c=im.crop((int(40*${S}),int(272*${S}),int(610*${S}),int(330*${S})))
c=c.resize((c.width*2, c.height*2), Image.LANCZOS)
c.save('${fp}')
"`);
  }
  const img = fs.readFileSync(fp).toString('base64');
  const Q = `Manuel scolaire marocain d'hadith, leçon «تحريم الظلم», liste «مما يستفاد من هذا الحديث». Cet item (2 lignes) commence par «العباد فقراء إلى الله تعالى، فيلزمني؟...». TRANSCRIS les DEUX lignes mot à mot avec voyelles. Donne surtout: (a) le verbe après «تعالى،» (فيلزمني؟ يرغبني؟ autre?); (b) les derniers mots de la ligne 2 après «إلى الله في» (جميع أموري؟ قضاء الحوائج؟ autre?).`;
  const r = await zai.createChatCompletionVision({
    messages: [{ role: 'user', content: [
        { type: 'text', text: Q },
        { type: 'image_url', image_url: { url: `data:image/png;base64,${img}` } },
    ] }],
    model: 'glm-5v-turbo', temperature: 0.1, max_tokens: 900,
  });
  const txt = r?.choices?.[0]?.message?.content ?? JSON.stringify(r);
  fs.writeFileSync(out, txt);
  console.log(txt);
} else { console.log('skip'); }

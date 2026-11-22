// IA-2 — vlm2-h6-16.mjs : passe VLM 2 — mots isolés, crops ultra-serrés.
import ZAI from '/home/z/node_modules/z-ai-web-dev-sdk/dist/index.js';
import fs from 'fs';

const DIR = '/home/z/my-project/pdf-work/h6-15/zoom';
const COMMON = `Crop ultra-serré d'un manuel scolaire marocain de hadith (6e primaire), arabe imprimé, 2400-3600 dpi. TRANSCRIS exactement ce qui est visible, mot à mot avec la vocalisation. Pour les mots sous SCRUTIN : décompose lettre par lettre (forme, nombre de points, place des points, dents). Ne complète JAMAIS par mémoire d'un texte connu : uniquement ce que tu vois. Si le crop est presque vide ou ne contient qu'un ornement, dis-le franchement.`;

const Q = {
  'v2-ithn': `Fin de ligne d'un paragraphe : on voit «...في ...» puis le dernier mot, peut-être coupé par le bord. SCRUTIN : le/les mot(s) visible(s) après «في» — décompose TOUTES les lettres une par une. Question précise : entre le ا initial et la finale ن, y a-t-il «ث ن ي» (mot اثنين, 4 consonnes) ou «ث ن ت ي» (mot اثنتين, 5 consonnes) ? La 3e consonne (si elle existe) porte-t-elle 2 points au-dessus (تاء) ou 2 points en dessous (ياء) ?`,
  'v2-myst': `Bande de page entre la fin d'une référence de hadith («...أخاه المسلم]») et le début de l'item suivant («- البيع على بيع...»). Transcris TOUT ce qui est imprimé sur cette bande : texte ? ornement ? en-tête coloré ? ligne de séparation ? Sois précis sur la nature de chaque élément.`,
  'v2-asbab': `Fin de ligne d'une puce : on voit la fin du mot après «بكل» et éventuellement un retour à la ligne. SCRUTIN : le dernier mot complet visible — décompose-le lettre par lettre. Y a-t-il «أسباب» (أ-س-ب-ا-ب) ou «أسبابها» (avec un هاء et un alif après le ب) ? Le mot est-il suivi d'un point ؟`,
  'v2-jaa': `Ligne complète d'un manuel (elle suit une ligne finissant par «؛ ولذلك»). Transcris-la mot à mot avec la vocalisation. Elle contient «جاء النهي في الحديث...». Indique précisément comment elle se termine (dernier mot + signe).`,
  'v2-taqwa': `Groupe de mots entre deux tirets dans une question numérotée «2- أشرح: ولا يخذله - ... - بحسب امرئ». SCRUTIN : le groupe entre les tirets — décompose-le lettre par lettre : «التقوى» (ا-ل-ت-ق-و-ى : la 3e lettre est تاء avec 2 points au-dessus, la 4e قاف avec 2 points, puis واء puis ى) ou «التقي» (ا-ل-ت-ق-ي) ou «النقوى» (3e lettre نون 1 point) ? Puis le mot suivant «هاهنا». Vocalisation du groupe.`,
};

const zai = await ZAI.create();
const sleep = (ms) => new Promise(r => setTimeout(r, ms));
for (const k of Object.keys(Q)) {
  const out = `${DIR}/vlm-${k}.txt`;
  if (fs.existsSync(out)) { console.log(`skip ${k}`); continue; }
  const img = fs.readFileSync(`${DIR}/${k}.png`).toString('base64');
  console.log(`\n======== ${k} ========`);
  let done = false;
  for (let attempt = 1; attempt <= 4 && !done; attempt++) {
    try {
      const r = await zai.createChatCompletionVision({
        messages: [{ role: 'user', content: [
            { type: 'text', text: COMMON + '\n\n' + Q[k] },
            { type: 'image_url', image_url: { url: `data:image/png;base64,${img}` } },
        ] }],
        model: 'glm-5v-turbo', temperature: 0.1, max_tokens: 2000,
      });
      const txt = r?.choices?.[0]?.message?.content ?? JSON.stringify(r);
      fs.writeFileSync(out, txt);
      console.log(txt.length > 700 ? txt.slice(0, 550) + '\n[...]' : txt);
      done = true;
    } catch (e) { console.log(`tentative ${attempt} ${k} échec: ${e.message}`); await sleep(8000 * attempt); }
  }
  await sleep(2500);
}
console.log('OK vlm2-h6-16');

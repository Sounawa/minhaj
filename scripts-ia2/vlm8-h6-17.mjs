// IA-2 — vlm8-h6-17.mjs : identité du glyphe isolé après هاهنا (matn p.95).
import ZAI from '/home/z/node_modules/z-ai-web-dev-sdk/dist/index.js';
import fs from 'fs';
const DIR = '/home/z/my-project/pdf-work/h6-15/zoom';
const zai = await ZAI.create();
const Q1 = `Un seul glyphe arabe isolé (3600 dpi ×3 zoom), extrait d'une ligne de hadith entre les mots «هاهنا» et «ويشير». SCRUTIN : identifie-le : est-ce une virgule arabe ، ? un wāw و ? un guillemet » ? une hamza ء ? autre chose ? Décris sa forme : une seule masse continue ou plusieurs éléments ? Y a-t-il une boucle fermée (wāw) ? un trait courbe avec renflement (virgule) ? deux chevrons (guillemet) ?`;
const Q2 = `Même glyphe, autre question : la partie PRINCIPALE (en bas, y766-1095) — contient-elle une boucle fermée comme un wāw و ? Décris la forme de la masse du bas : arrondie fermée ? en croissant ouvert ? en goutte ? Et le petit fragment en haut (y0-54) appartient-il à la ligne supérieure ?`;
const img = fs.readFileSync(`${DIR}/z7-hahona-glyph.png`).toString('base64');
for (const [tag, Q] of [['a', Q1], ['b', Q2]]) {
  const out = `${DIR}/vlm8-h6-17-glyph-${tag}.txt`;
  if (fs.existsSync(out)) continue;
  let done = false;
  for (let attempt = 1; attempt <= 4 && !done; attempt++) {
    try {
      const r = await zai.createChatCompletionVision({
        messages: [{ role: 'user', content: [
            { type: 'text', text: Q },
            { type: 'image_url', image_url: { url: `data:image/png;base64,${img}` } },
        ] }],
        model: 'glm-5v-turbo', temperature: 0.1, max_tokens: 900,
      });
      const txt = r?.choices?.[0]?.message?.content ?? JSON.stringify(r);
      fs.writeFileSync(out, txt);
      console.log(`=== ${tag} ===\n` + txt.slice(0, 700));
      done = true;
    } catch (e) { console.log(`${tag} tentative ${attempt} échouée: ${e.message}`); await new Promise(r => setTimeout(r, 9000 * attempt)); }
  }
}
console.log('OK vlm8-h6-17');

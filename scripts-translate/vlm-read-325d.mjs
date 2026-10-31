import ZAI from 'z-ai-web-dev-sdk';
import fs from 'fs';
const qs = [
  { img: '/tmp/m325-side.png',
    ask: `Bande d'un manuel arabe : carte latérale de concepts. Transcris en arabe, mot à mot, chaque terme défini et sa définition (les termes se terminent par «:»). Format strict, une ligne par concept :
TERME: <terme> — <définition>` },
  { img: '/tmp/m325-tab2.png',
    ask: `Tableau successoral arabe (exemple du المفقود). Transcris CHAQUE ligne : nom de l'héritier (dernière colonne à droite) puis tous les nombres de la ligne de droite à gauche, exactement tels qu'imprimés (chiffres indiens). Il y a une ligne d'en-tête avec trois nombres égaux. Indique aussi toute ligne supplémentaire (عم، جد...). Format strict :
LIGNE: <héritier> | <nombres droite→gauche>` },
  { img: '/tmp/m325-exos.png',
    ask: `Bande d'un manuel arabe : trois énoncés d'exercices numérotés 1، 2، 3 (تمارين sur le disparu المفقود). Transcris chaque énoncé complet en arabe, mot à mot. Format strict :
EXO1: <arabe>
EXO2: <arabe>
EXO3: <arabe>` },
];
async function main() {
  const zai = await ZAI.create();
  for (const q of qs) {
    const b64 = fs.readFileSync(q.img).toString('base64');
    const res = await zai.createChatCompletionVision({
      messages: [{ role: 'user', content: [
        { type: 'text', text: q.ask },
        { type: 'image_url', image_url: { url: `data:image/png;base64,${b64}` } },
      ]}],
      model: 'glm-5v-turbo', max_tokens: 700,
    });
    console.log('=== ' + q.img + ' ===');
    console.log(res.choices[0].message.content);
    console.log('');
  }
}
main().catch(e => { console.error('VLM_FAIL', e.message); process.exit(1); });

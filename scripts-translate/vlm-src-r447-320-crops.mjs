// vlm-src-r447-320-crops.mjs — passe image ciblée : tables et rasm des crops p.173-176
import ZAI from 'z-ai-web-dev-sdk';
import fs from 'fs';

const shots = [
  ['crop-173b-173.png', 'Le tiers inférieur de la p.173 : fin de la section ثالثا إقرار متعدد بمتعدد — transcris les points numérotés 1-5 avec leurs nombres exacts.'],
  ['crop-174m-174.png', 'La bande médiane de la p.174 : la fin du point 5, le point 6, puis le TABLEAU de répartition (dubl), puis la citation du matn entre guillemets. Transcris le tableau CELLULE PAR CELLULE : pour chaque ligne donne le nom de l\'héritier et la suite exacte de ses nombres, colonne par colonne, de droite à gauche ; donne aussi l\'en-tête des colonnes (جزء السهم etc.) et les nombres de tête (60, 20, 15, 12...). Puis transcris la citation du matn LETTRE PAR LETTRE avec ses voyelles.'],
  ['crop-175t-175.png', 'Le tiers supérieur de la p.175 : l\'énoncé de l\'application 1 (تطبيقات وحلول) et son TABLEAU. Transcris l\'énoncé complet, puis le tableau CELLULE PAR CELLULE : chaque ligne = héritier + ses nombres exacts colonne par colonne (de droite à gauche), avec l\'en-tête des colonnes si visible.'],
  ['crop-175b-175.png', 'La moitié inférieure de la p.175 : l\'énoncé de l\'application 2 et son TABLEAU. Transcris l\'énoncé complet, puis le tableau CELLULE PAR CELLULE : chaque ligne = héritier + ses nombres exacts colonne par colonne (de droite à gauche), avec l\'en-tête des colonnes si visible.'],
  ['crop-176t-176.png', 'Le haut de la p.176 : la section ثانيا تمارين et les deux exercices. Transcris tout, puis la consigne de mémorisation du matn du cours suivant.'],
];

const prompt = `Tu es transcripteur expert d'un manuel marocain de farāʾiḍ en arabe (éducation traditionnelle). Transcris fidèlement, sans inventer : si une zone est illisible écris [illisibile]. Les nombres sont en chiffres arabes orientaux (٠١٢٣٤٥٦٧٨٩) ou occidentaux — rends-les en chiffres occidentaux. Structure ta réponse par : ÉNONCÉ (arabe), TABLEAU (lignes "héritier: valeurs"), TEXTE SUivant (arabe).`;

async function main() {
  const zai = await ZAI.create();
  for (const [f, cue] of shots) {
    const b64 = fs.readFileSync('/home/z/my-project/scripts-translate/tr-tmp/' + f).toString('base64');
    const res = await zai.createChatCompletionVision({
      messages: [{
        role: 'user',
        content: [
          { type: 'text', text: prompt + '\nZONE À TRANSCRIRE : ' + cue },
          { type: 'image_url', image_url: { url: `data:image/png;base64,${b64}` } },
        ],
      }],
      model: 'glm-5v-turbo',
      max_tokens: 2500,
    });
    console.log('===== ' + f + ' =====');
    console.log(res.choices[0].message.content);
    console.log();
  }
}
main().catch(e => { console.error('VLM_FAIL', e.message); process.exit(1); });

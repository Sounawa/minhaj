// vlm-read-325.mjs — lecture binaire ciblée des zones corrompues du dars 27 (الحمل والمفقود), p.194/197/199/200
import ZAI from 'z-ai-web-dev-sdk';
import fs from 'fs';

const qs = [
  {
    img: '/home/z/my-project/scripts-translate/tr-tmp/m325-p194-194.png',
    ask: `Page de manuel arabe (droit successoral mālikite). En haut à droite de la page se trouve une citation du Muḫtaṣar de Khalīl introduite par « قال الشيخ خليل ». Transcris EXACTEMENT cette citation lettre par lettre avec ses diacritiques, en arabe. Puis transcris la phrase qui la précède immédiatement (contenant « ...التركة إلى ولادته » ou approchant). Réponds STRICTEMENT en ce format :
CITATION_KHALIL: <texte arabe exact>
PHRASE_PRECEDENTE: <texte arabe exact>`
  },
  {
    img: '/home/z/my-project/scripts-translate/tr-tmp/m325-p197-197.png',
    ask: `Page de manuel arabe. Il y a une phrase arabe diacritisée en partie droite de la page contenant les mots « حَيًّا ... مَيْتًا ... المَشْكُوك ... التَّعْمِير » (citation du Muḫtaṣar sur le disparu المفقود). Transcris EXACTEMENT cette phrase lettre par lettre avec tous ses diacritiques, en arabe. Réponds STRICTEMENT :
MATN_MAFOUD: <texte arabe exact diacritisé>`
  },
  {
    img: '/home/z/my-project/scripts-translate/tr-tmp/m325-p199-199.png',
    ask: `Page de manuel arabe contenant DEUX tableaux successoraux avec lignes et colonnes. Pour CHAQUE tableau, liste chaque ligne sous la forme : NOM_HERITIER | valeur1 | valeur2 | valeur3 | valeur4 (toutes les valeurs numériques de la ligne, de droite à gauche, chiffres indiens ou arabes, exactement tels qu'imprimés, y compris les zéros). Indique aussi la valeur de la ligne « الحظ الموقوف » si présente, et le titre précédant chaque tableau (ex: ومثال التماثل). Réponds STRICTEMENT :
TABLEAU1_TITRE: <titre>
TABLEAU1_LIGNES:
<NOM> | <nombres>
...
TABLEAU2_TITRE: <titre>
TABLEAU2_LIGNES:
<NOM> | <nombres>`
  },
  {
    img: '/home/z/my-project/scripts-translate/tr-tmp/m325-p200-200.png',
    ask: `Page de manuel arabe avec deux applications (تطبيقات). Chaque application « وترك : ... » est suivie d'un petit tableau successoral. Pour chaque tableau : liste chaque ligne NOM_HERITIER | nombres (exactement tels qu'imprimés, droite à gauche), la ligne الحظ الموقوف si présente, et recopie en arabe l'énoncé complet de l'application (la phrase contenant « هلك هالك وترك »). Réponds STRICTEMENT :
APP1_ENONCE: <arabe>
APP1_LIGNES:
<NOM> | <nombres>
APP2_ENONCE: <arabe>
APP2_LIGNES:
<NOM> | <nombres>`
  },
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
      model: 'glm-5v-turbo', max_tokens: 900,
    });
    console.log('=== ' + q.img.split('/').pop() + ' ===');
    console.log(res.choices[0].message.content);
    console.log('');
  }
}
main().catch(e => { console.error('VLM_FAIL', e.message); process.exit(1); });

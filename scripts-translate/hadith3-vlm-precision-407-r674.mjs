// R674 — lectures VLM de PRÉCISION leçon 407 (crops z-*, zoom 8-9).
import ZAI from 'z-ai-web-dev-sdk';
import fs from 'fs';

const DIR = '/home/z/my-project/tr-tmp/qa-crops-r674';
const OUTDIR = '/home/z/my-project/tr-tmp/vlm-407';

const PROMPTS = {
  'z-p124-aya': `Ligne unique très zoomée d'un manuel arabe : fin de phrase puis citation coranique ﴿...﴾ suivie d'un renvoi bleu [سورة الحج الآية: N]. Transcris LA LIGNE ENTIÈRE exactement, diacritiques comprises, et donne NUM: pour N chiffre par chiffre (٠=0…٩=9).`,
  'z-p124-nuqsan': `Deux lignes très zoomées d'un manuel arabe : « وقد يكون جبرا لما يشوب الحج... » et la question centrale « فما أحكام... ». Transcris les deux lignes EXACTEMENT, diacritiques comprises.`,
  'z-p125-h1135matn': `Corps d'un hadith du Muwaṭṭaʾ très zoomé (apport d'Hibbār b. al-Aswad à ʿUmar le jour du sacrifice). Transcris TOUT le texte exactement ligne par ligne, marque [?] l'illisible. Donne NUM: pour le renvoi [الموطأ رقم: N] (chiffre par chiffre ٠=0…٩=9).`,
  'z-p125-notice': `Notice biographique très zoomée d'un manuel arabe (سليمان بن يسار). Transcris-la exactement ; pour l'année de mort et l'âge, donne NUM: chiffre par chiffre (٠=0…٩=9).`,
  'z-p126-q1122': `Citation du Prophète ou de سعيد بن المسيب entre « » dans un manuel arabe très zoomé, avec renvoi [الموطأ رقم: N]. Transcris la citation exactement (diacritiques comprises) et donne NUM: chiffre par chiffre.`,
  'z-p126-q1124': `Avis d'ابن شهاب entre « » très zoomé + renvoi [الموطأ رقم: N]. Transcris exactement et donne NUM: chiffre par chiffre.`,
  'z-p126-q1125': `Citation d'ابن عمر رضي الله عنهما entre « » très zoomée + renvoi [الموطأ رقم: N]. Transcris exactement et donne NUM: chiffre par chiffre.`,
  'z-p126-thania': `Titre de section « ثانيا:... » et sous-titre numéroté 1 - très zoomés + 2 lignes suivantes. Transcris exactement (attention : le sous-titre peut contenir بغير — transcris ce qui est visible).`,
  'z-p127-h1134': `Hadith du Muwaṭṭaʾ n° 1134 très zoomé (un pèlerin qui a égaré sa bête de monture, rapport à ʿUmar). Transcris TOUT exactement, marque [?] l'illisible, et donne NUM: du renvoi [الموطأ رقم: N] chiffre par chiffre.`,
  'z-p127-q1136': `Citation de مالك entre « » très zoomée (cas du qārin dont le ḥaǧǧ a manqué) + renvoi [الموطأ رقم: N]. Transcris exactement, diacritiques comprises, et donne NUM: chiffre par chiffre.`,
  'z-p127-afsada': `Deux lignes très zoomées : « إذا باشر المحرم بالحج أهله قبل رمي جمرة العقبة فقد... ». Transcris exactement.`,
  'z-p127-saidmid': `Récit de سعيد بن المسيب (rapport de يحيى بن سعيد) très zoomé, plusieurs lignes. Transcris TOUT exactement, marque [?] l'illisible.`,
  'z-p127-after': `Passage فقهي très zoomé « وإن باشر الحاج زوجته بعد رمي جمرة العقبة... » jusqu'à « قال مالك... ». Transcris exactement, marque [?] l'illisible.`,
  'z-p128-h1129': `Passage très zoomé : avis de مالك sur un homme qui a touché sa femme entre ʿArafa et la jamra, citation entre « », renvoi [الموطأ رقم: N]. Transcris exactement et donne NUM: chiffre par chiffre.`,
  'z-p128-h1138': `Ligne d'isnad très zoomée (rapport d'عن X بن Y الZ عن عكرمة مولى ابن عباس) + citation entre « » + renvoi [الموطأ رقم: N]. Transcris exactement et donne NUM: chiffre par chiffre.`,
  'z-p128-h1139': `Ligne très zoomée : قول ربيعة بن عبد الرحمن puis citation de مالك entre « » + renvoi [الموطأ رقم: N]. Transcris exactement et donne NUM: chiffre par chiffre.`,
  'z-p128-khat-aya': `Fin de conclusion (خاتمة) très zoomée + éventuelle citation coranique avec renvoi [سورة ... آية N]. Transcris tout ce qui est visible exactement ; donne NUM: si un numéro apparaît (chiffre par chiffre).`,
  'z-p128-exos': `Deux exercices numérotés 1- et - très zoomés. Transcris exactement (attention aux mots عطب/الحج/الهدي et بوقد/بوفد).`,
};

async function main() {
  const zai = await ZAI.create();
  const tags = Object.keys(PROMPTS).filter(t => fs.existsSync(`${DIR}/${t}.png`) && !fs.existsSync(`${OUTDIR}/${t}.txt`));
  console.log(`tâches précision: ${tags.length}`);
  for (const tag of tags) {
    for (let k = 1; k <= 4; k++) {
      try {
        const b64 = fs.readFileSync(`${DIR}/${tag}.png`).toString('base64');
        const res = await zai.chat.completions.createVision({
          messages: [{ role: 'user', content: [
            { type: 'text', text: PROMPTS[tag] },
            { type: 'image_url', image_url: { url: `data:image/png;base64,${b64}` } },
          ] }],
          thinking: { type: 'disabled' },
        });
        const txt = res.choices[0]?.message?.content || '(vide)';
        fs.writeFileSync(`${OUTDIR}/${tag}.txt`, txt, 'utf-8');
        console.log(`${tag}: OK (${txt.length} car)`);
        break;
      } catch (e) {
        const msg = String(e?.message || e);
        if (k === 4) { console.log(`${tag}: ERREUR ${msg}`); break; }
        const wait = msg.includes('429') ? 20000 * k : 5000;
        await new Promise(r => setTimeout(r, wait));
      }
    }
    await new Promise(r => setTimeout(r, 4000));
  }
  console.log('VLM précision terminé');
}
main().catch(e => { console.error('VLM_ERR: ' + (e?.message || e)); process.exit(1); });

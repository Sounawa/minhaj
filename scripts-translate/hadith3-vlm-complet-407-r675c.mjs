// R675-C — lectures VLM COMPLÉMENT leçon 407 (crops c-*, zones jamais lues par r674/r674c).
// Chaque zone tranchée sur preuve image ; ne jamais deviner ; [?] pour l'illisible.
import ZAI from 'z-ai-web-dev-sdk';
import fs from 'fs';

const DIR = '/home/z/my-project/tr-tmp/qa-crops-r675c';
const OUTDIR = '/home/z/my-project/tr-tmp/vlm-407';
fs.mkdirSync(OUTDIR, { recursive: true });

const PROMPTS = {
  'c-p124-top': `Haut de page d'un manuel arabe : médaillon circulaire coloré avec un numéro de cours, bannière calligraphiée (titre du cours), puis objectifs (أهداف الدرس) numérotés. Décris le numéro du médaillon CHIFFRE PAR CHIFFRE, transcris la bannière EXACTEMENT, puis chaque objectif MOT POUR MOT glyphe par glyphe. Marque [?] l'illisible, ne complète PAS de mémoire.`,
  'c-p124-tamhid': `Paragraphe d'introduction (تمهيد) d'un manuel arabe avant une citation coranique : «يشوب الحج من نقصان...». Transcris TOUT exactement ligne par ligne, diacritiques comprises, mot pour mot. Transcris aussi le fragment de citation coranique ou renvoi s'il apparaît. Marque [?] l'illisible, ne complète PAS de mémoire.`,
  'c-p124-h1121': `Hadith du Muwaṭṭaʾ très zoomé (isnad مالك عن هشام بن عروة... sujet : هدي أضنّ و عطب). Transcris TOUT exactement ligne par ligne, diacritiques comprises, y compris les paroles du Prophète ﷺ entre « ». Marque [?] l'illisible, ne complète PAS de mémoire. NUM: pour le renvoi [الموطأ رقم: N] chiffre par chiffre.`,
  'c-p124-bottom': `Bas de page 124 d'un manuel arabe : suite éventuelle du hadith, glosses (شرح المفردات) avec tirets, ou toute autre section. Transcris TOUT exactement ligne par ligne. Marque [?] l'illisible, ne complète PAS de mémoire.`,
  'c-p125-notice': `Zone d'un manuel arabe juste après un hadith du Muwaṭṭaʾ : notice de présentation d'un savant (nom, kunya, mawlā, mort en l'an H) sur fond coloré ou encadré. Transcris TOUT exactement glyphe par glyphe, surtout le NOM et l'ANNÉE de mort : l'année doit être donnée CHIFFRE PAR CHIFFRE (٠=0…٩=9). Marque [?] l'illisible, ne complète PAS de mémoire.`,
  'c-p125-taqwim': `Bas de page 125 d'un manuel arabe : gloses (شرح المفردات) avec tirets, puis استخلص المضامين (résumé) numéroté, puis تقويم التعلّم (questions). Transcris TOUT exactement ligne par ligne, chaque item numéroté MOT POUR MOT. Marque [?] l'illisible, ne complète PAS de mémoire.`,
  'c-p126-wajib': `Zone d'un manuel arabe : règle فقهية «أما الهدي الواجب إذا عطب قبل محله...» avec citation de ابن شهاب (ابن عروة?) entre « » et renvoi [الموطأ رقم: N]. Transcris TOUT exactement ligne par ligne, diacritiques comprises. Le nom du rapporteur cité : transcris-le glyphe par glyphe. NUM: chiffre par chiffre. Marque [?] l'illisible.`,
  'c-p127-top': `Haut de page 127 d'un manuel arabe : continuation d'une règle فقهية sur من فاته الحج (هلال, شغل...) et la prescription صيام ثلاثة أيام في الحج وسبعة إذا رجع. Transcris TOUT exactement ligne par ligne, diacritiques comprises, mot pour mot. Marque [?] l'illisible, ne complète PAS de mémoire.`,
  'c-p128-abbas': `Zone d'un manuel arabe : athar rapporté d'ابن عباس (vraisemblablement «فعن ابن عباس لا أظنه إلا...») avec citation entre « » et renvoi [الموطأ رقم: N]. Transcris TOUT exactement ligne par ligne, diacritiques comprises, glyphe par glyphe pour les noms. NUM: chiffre par chiffre. Marque [?] l'illisible, ne complète PAS de mémoire.`,
  'c-p128-istifada': `Zone d'un manuel arabe : paragraphe استفادة («يستفاد مما سبق أن الحج عبادة...») puis questions تقويم numérotées (استدلال, وُفد حجاج...). Transcris TOUT exactement ligne par ligne, chaque question MOT POUR MOT. Marque [?] l'illisible, ne complète PAS de mémoire.`,
};

async function main() {
  const zai = await ZAI.create();
  const tags = Object.keys(PROMPTS).filter(t => fs.existsSync(`${DIR}/${t}.png`) && !fs.existsSync(`${OUTDIR}/${t}.txt`));
  console.log(`tâches r675c: ${tags.length}`);
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
    await new Promise(r => setTimeout(r, 3500));
  }
  console.log('VLM r675c terminé');
}
main().catch(e => { console.error('VLM_ERR: ' + (e?.message || e)); process.exit(1); });

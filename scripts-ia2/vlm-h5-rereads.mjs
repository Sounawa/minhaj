// Z2-35 — relectures VLM en attente : (1) bandeau calligraphique p.158 hadith-5ep,
// (2) glose أَرَأْيْتَ p.151 (deux derniers mots disputés depuis Z2-32).
// Test de quota d'abord : une seule lecture en argument 'test', sinon toutes.
import ZAI from '/home/z/my-project/node_modules/z-ai-web-dev-sdk/dist/index.js';
import fs from 'fs';

const DIR = '/home/z/my-project/scripts-ia2/tmp/h5-rereads/crops';
const mode = process.argv[2] || 'all';

const jobs = [];
if (mode === 'test' || mode === 'all') {
  jobs.push({
    img: 'B1-bandeau-p158.png',
    out: 'V-B1-bandeau.md',
    ask: `Bande calligraphique décorative (calligraphie coufique/florale) extraite du haut de la page 158 d'un manuel marocain d'hadith, 5e année primaire. Cette bande contient un mot ou une courte expression en calligraphie. Les leçons de ce manuel ont des bandeaux de section : أهداف الدرس / تمهيد / فهم / تحليل / تقويم / استثمار / التطبيق (ou أَوَظِّفُ مُكْتَسَبَاتِي) etc.
Quel(s) mot(s) lit-on dans cette bande calligraphique ? Réponds uniquement avec la/les lecture(s) possible(s) en graphie arabe normale, sans commentaire.`,
  });
}
if (mode === 'all') {
  jobs.push({
    img: 'B2-bandeau-contexte.png',
    out: 'V-B2-contexte.md',
    ask: `Haut de la page 158 d'un manuel marocain d'hadith (5e année primaire, leçon de synthèse «دعم وتطبيق»). On voit : une bande calligraphique décorative, puis une ligne d'introduction, puis la première tâche.
Transcris fidèlement, en arabe : (1) la lecture du mot calligraphié dans la bande décorative ; (2) la ligne d'introduction complète sous la bande ; (3) la première tâche numérotée. Ne devine rien au-delà de l'imprimé.`,
  });
  jobs.push({
    img: 'G1-glose-bloc.png',
    out: 'V-G1-glose.md',
    ask: `Bloc extrait de la page 151 d'un manuel marocain d'hadith (5e année primaire), entre la biographie d'un narrateur et une section de questions. Le bloc contient : un bandeau/titre de rubrique (possiblement décoratif) puis UNE ligne de glose de vocabulaire qui commence par le mot أَرَأْيْتَ.
Transcris ENTIÈREMENT, mot à mot, en arabe vocalisé : (1) le titre du bandeau ; (2) la ligne de glose complète, surtout sa FIN (les deux ou trois derniers mots après بِمَعْنَى). Les deux derniers mots exacts sont CRUCIAUX — recopie-les lettre par lettre même s'ils te semblent étranges. Ne devine pas : si une lettre est ambiguë, note-la entre [crochets].`,
  });
}

async function main() {
  const zai = await ZAI.create();
  for (const j of jobs) {
    const b64 = fs.readFileSync(`${DIR}/${j.img}`).toString('base64');
    try {
      const res = await zai.createChatCompletionVision({
        messages: [{ role: 'user', content: [
          { type: 'text', text: j.ask },
          { type: 'image_url', image_url: { url: `data:image/png;base64,${b64}` } },
        ]}],
        model: 'glm-5v-turbo', max_tokens: 900,
      });
      const txt = res.choices[0].message.content;
      fs.writeFileSync(`${DIR}/${j.out}`, txt);
      console.log(`${j.img} OK (${txt.length} car):\n${txt}\n`);
    } catch (e) {
      console.log(`${j.img} FAIL: ${e.message}`);
    }
  }
}
main().catch(e => { console.error('VLM_FAIL', e.message); process.exit(1); });

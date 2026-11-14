// Z2-18 — zooms r3 : arbitrages finaux (round 3)
import ZAI from '/home/z/node_modules/z-ai-web-dev-sdk/dist/index.js';
import fs from 'fs';

const DIR = '/home/z/my-project/repo-minhaj/scripts-ia2/tmp/h5-16';

const ASKS = [
  ['r3-quote-open-p88.jpg', 'Début de la citation prophétique (partie droite de la ligne, calligraphie naskh). Questions : (1) le premier mot imprimé est-il «قد» ou la citation commence-t-elle directement par «تركتكم» ? (2) lit-on «على المحجة البيضاء» ou «على البيضاء» ? Décompose le mot entre «على» et «البيضاء» lettre par lettre. Transcris ensuite toute la ligne.'],
  ['r3-tamhid2b-p88.jpg', 'Suite du تمهيد (2-3 lignes). Transcris mot à mot : «...من حق غيره، ولا الحلال من الحرام، ولا أن الشيء من الواجبات أم لا؟ ولا أنه من المعروف أو من المنكر؟ ومثل هذا هو المسمى بالشبهات. فما المراد بالشبهات؟ وما موقف الشرع منها؟». Question précise : le mot interrogatif avant «من المنكر» est-il «أم» ou «أو» ?'],
  ['r3-hadithref-p88.jpg', 'Bas de page 88 : fin de l\'encadré du hadith «دع ما يريبك إلى ما لا يريبك» et la ligne de RÉFÉRENCE en dessous (entre crochets, en couleur). Transcris la référence exactement : [رواه ...] ou [رواية ...]. Décompose le premier mot lettre par lettre.'],
  ['r3-halalbayyin-p89.jpg', 'Ligne du milieu du passage أولا. Transcris mot à mot : «...من وجه آخر. ففي الممتلكات مثلا: الحلال ...: ما علمت ملكه يقينا لنفسك؛». Question précise : le terme défini est-il «الحلال اليقين» ou «الحلال البين» ? Décompose-le lettre par lettre.'],
  ['r3-shubha-end-p89.jpg', 'Fin (gauche) de la dernière ligne de la page 89. Transcris : «...؛ والشبهة: ما لا ...». Question : la définition se termine-t-elle par «أهو له أم لغيره» ou «أهو لك أو لغيرك» ou autre ? Décompose la fin lettre par lettre.'],
  ['r3-ijtinab2-p90.jpg', 'Première ligne de la page 90 (sous le bandeau décoratif). Transcris mot à mot. Questions : (1) «فالورع اجتنابها» (ha final) ou «اجتنابه» (hé final) — décompose la dernière syllabe ; (2) la référence entre crochets : «[عمدة القاري للعيني بتصرف]» exactement ?'],
  ['r3-ay1-p90.jpg', 'Explication «أي: ...» (partie droite). Questions : (1) le mot après «أي:» est-il «نترك» (nūn) ou «اترك/أترك» (hamza) — décompose la première lettre ; (2) «ما نشك» (nūn) ou «ما تشك» (tāʾ) ; (3) «في حرمته» exactement ? Transcris la ligne.'],
  ['r3-ay2-p90.jpg', 'Suite de l\'explication (partie droite de la ligne suivante). Question : le mot entre «والأعمال؛» et «إلى ما لا تشك فيه منها» — décompose-le lettre par lettre (وننتقل؟ ونجتني؟ وننتهي؟ ونمضي؟ autre). Transcris la ligne entière avec la référence.'],
  ['r3-mayufa3-p91.jpg', 'Deux lignes de l\'introduction de «ما يعفى عنه من الشبهات». Transcris mot à mot. Questions : (1) après «لكنها» : quel mot/verbe exactement ? (2) après «لم» : «تتغير» / «تغير» / «نغير» / autre — décompose lettre par lettre.'],
  ['r3-bukhari3-p91.jpg', 'Hadith de Bukhārī sur l\'homme qui craint d\'avoir rompu ses ablutions (3-4 lignes). Transcris TOUT mot à mot. Questions : (1) entre «إلى النبي ﷺ» et «يجد» : y a-t-il «الرجل الذي» ou autre formulation ? (2) la question : «أيقطع الصلاة?» ou «أينقطع الصلاة?» ; (3) «حتى يجد ريحا أو يسمع صوتا» exact ; (4) «وهو محمول على الذي يعتريه الشك كثيرا» exact.'],
  ['r3-idad-open-p92.jpg', 'Première ligne de l\'الإعداد القبلي. Transcris mot à mot : «أحفظ حديث الدرس المقبل و... ما يلي:». Question : le second verbe — «وأقوم» ou «وأنجز» ou autre ? Décompose-le lettre par lettre.'],
];

async function main() {
  const zai = await ZAI.create();
  for (const [img, ask] of ASKS) {
    const p = `${DIR}/${img}`;
    if (!fs.existsSync(p)) { console.log(`ABSENT ${img}`); continue; }
    const out = `${DIR}/vlm-${img.replace('.jpg', '.txt')}`;
    if (fs.existsSync(out)) { console.log(`skip ${img}`); continue; }
    const b64 = fs.readFileSync(p).toString('base64');
    try {
      const res = await zai.createChatCompletionVision({
        messages: [{ role: 'user', content: [
          { type: 'text', text: `Zoom très haute résolution d'un manuel scolaire marocain de hadith (5e primaire), leçon 16 «التورع عن الشبهات». ${ask}\n\nAnalyse les glyphes un par un. Réponds d'abord par les CHOIX retenus (numérotés), puis la transcription mot à mot vocalisée. Illisible : [؟].` },
          { type: 'image_url', image_url: { url: `data:image/jpeg;base64,${b64}` } },
        ] }],
        model: 'glm-5v-turbo',
        max_tokens: 1400,
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

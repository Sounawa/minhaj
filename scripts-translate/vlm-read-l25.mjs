import ZAI from 'z-ai-web-dev-sdk';
import fs from 'fs';

// R571 — lecture VLM des crops de preuve du hadith-2es, leçon 25 (p.171-176).
// Chaque renvoi Muwaṭṭaʾ est tranché CHIFFRE PAR CHIFFRE à l'image (crop 1440 dpi).
const qs = [
  { img: '/home/z/my-project/tr-tmp/qa-crops-r571/c-r571-hadith1-818-1440.png',
    ask: `Fin d'un hadith dans un manuel arabe (crop très zoomé). À gauche se trouve un renvoi entre crochets de la forme [الموطأ رقم: NNN] où NNN est un nombre de 3 chiffres en chiffres arabes-orientaux. Transcris CE NOMBRE chiffre par chiffre (٠=0 ١=1 ٢=2 ٣=3 ٤=4 ٥=5 ٦=6 ٧=7 ٨=8 ٩=9) et la dernière phrase du hadith avec le mot prononcé par le Prophète entre guillemets. Format :\nPHRASE: <dernière phrase exacte>\nNUM: <3 chiffres>`,
  },
  { img: '/home/z/my-project/tr-tmp/qa-crops-r571/c-r571-hadith2-821-1440.png',
    ask: `Fin d'un hadith dans un manuel arabe (crop très zoomé). À gauche un renvoi [الموطأ رقم: NNN]. Transcris le nombre NNN chiffre par chiffre (٠=0 … ٩=9) et la fin du hadith. Format :\nPHRASE: <fin exacte>\nNUM: <3 chiffres>`,
  },
  { img: '/home/z/my-project/tr-tmp/qa-crops-r571/c-r571-hadith3-826-1440.png',
    ask: `Fin d'un hadith dans un manuel arabe (crop très zoomé). À gauche un renvoi [الموطأ رقم: NNN]. Transcris le nombre NNN chiffre par chiffre (٠=0 … ٩=9) et la fin du hadith (فمن شاء…). Format :\nPHRASE: <fin exacte>\nNUM: <3 chiffres>`,
  },
  { img: '/home/z/my-project/tr-tmp/qa-crops-r571/c-r571-desm-wasum-819-1440.png',
    ask: `Ligne d'un manuel arabe (crop très zoomé) citant la parole du Prophète à un bédouin : وصم يوما مكان ما أصبت suivie d'un renvoi [الموطأ رقم: NNN] (ou similaire). Transcris la citation exacte et le nombre NNN chiffre par chiffre (٠=0 … ٩=9). Format :\nQUOTE: <citation exacte>\nNUM: <chiffres>`,
  },
  { img: '/home/z/my-project/tr-tmp/qa-crops-r571/c-r571-ata-819-1440.png',
    ask: `Ligne d'un manuel arabe (crop très zoomé) : rapport d'عطاء interrogeant سعيد بن المسيب sur le contenu d'un عرق de dattes, suivie d'un renvoi [الموطأ رقم: NNN]. Transcris TOUTE la ligne exactement (la réponse chiffre le nombre de صاع) et le nombre NNN chiffre par chiffre (٠=0 … ٩=9). Format :\nLIGNE: <texte exact>\nNUM: <chiffres>`,
  },
  { img: '/home/z/my-project/tr-tmp/qa-crops-r571/c-r571-hijama-822-1440.png',
    ask: `Fin d'un rapport dans un manuel arabe (crop très zoomé) : سعد بن أبي وقاص وعبد الله بن عمر كانا يحتجمان وهما صائمان suivie d'un renvoi [الموطأ رقم: NNN]. Transcris le nombre NNN chiffre par chiffre (٠=0 … ٩=9). Format :\nPHRASE: <texte exact>\nNUM: <3 chiffres>`,
  },
  { img: '/home/z/my-project/tr-tmp/qa-crops-r571/c-r571-aicha-825-1440.png',
    ask: `Zone d'un manuel arabe (crop très zoomé) : fin de la parole de عائشة sur يوم عاشوراء (فمن شاء صامه ومن شاء تركه) suivie d'un renvoi [الموطأ رقم: NNN]. Transcris le nombre NNN chiffre par chiffre (٠=0 … ٩=9). Si aucun nombre n'est visible, écris NUM: AUCUN. Format :\nPHRASE: <texte visible exact>\nNUM: <chiffres ou AUCUN>`,
  },
  { img: '/home/z/my-project/tr-tmp/qa-crops-r571/c-r571-istihlal-824-1440.png',
    ask: `Ligne d'un manuel arabe (crop très zoomé) : avis de مالك sur la حجامة du jeûneur (وليس عليه قضاء ذلك اليوم) suivie d'un renvoi [الموطأ رقم: NNN]. Transcris le nombre NNN chiffre par chiffre (٠=0 … ٩=9). Format :\nPHRASE: <texte exact>\nNUM: <chiffres>`,
  },
  { img: '/home/z/my-project/tr-tmp/qa-crops-r571/mc-r571-bandeau-171-200.png',
    ask: `Haut d'une page d'un manuel arabe (crop très zoomé). Transcris EXACTEMENT : (1) le badge/bandeau de leçon en haut (mot الدرس suivi d'un numéro en chiffres arabes-orientaux — transcris le numéro chiffre par chiffre) ; (2) le titre أهداف الدرس ; (3) les trois objectifs numérotés complets. Format :\nBADGE: <الدرس + numéro exact>\nOBJ1: <texte>\nOBJ2: <texte>\nOBJ3: <texte>`,
  },
  { img: '/home/z/my-project/tr-tmp/qa-crops-r571/mc-r571-bas-173-200.png',
    ask: `Dernière(s) ligne(s) d'une page d'un manuel arabe (crop très zoomé). La ligne commence par : والكفارة خاصة بالعمد في مشهور قول… Transcris EXACTEMENT la fin de la phrase après الإمام مالك (il peut y avoir une formule du type رحمه الله). Si des mots sont illisibles, transcris ce qui est visible et écris ILLISIBLE pour le reste. Format :\nLIGNE: <texte exact>`,
  },
  { img: '/home/z/my-project/tr-tmp/qa-crops-r571/mc-r571-bas-175-200.png',
    ask: `Bas d'une page d'un manuel arabe (crop très zoomé). Transcris EXACTEMENT : (1) le titre de section visible (التقويم ou autre) ; (2) les questions numérotées ; (3) tout crochet [..] ou renvoi avec chiffres. Format :\nTITRE: <texte>\nQ1: <texte>\nQ2: <texte>\nCROCHETS: <tous les crochets et chiffres visibles ou AUCUN>`,
  },
];

const sleep = (ms) => new Promise(r => setTimeout(r, ms));

async function main() {
  const zai = await ZAI.create();
  for (const q of qs) {
    const b64 = fs.readFileSync(q.img).toString('base64');
    let res = null, attempt = 0;
    while (res === null && attempt < 6) {
      attempt++;
      try {
        res = await zai.createChatCompletionVision({
          messages: [{ role: 'user', content: [
            { type: 'text', text: q.ask },
            { type: 'image_url', image_url: { url: `data:image/png;base64,${b64}` } },
          ]}],
          model: 'glm-5v-turbo', max_tokens: 1600,
        });
      } catch (e) {
        console.error(`retry ${attempt} pour ${q.img.split('/').pop()} : ${e.message}`);
        await sleep(25000);
      }
    }
    if (res === null) { console.log('=== ' + q.img.split('/').pop() + ' ===\nECHEC après retries\n'); continue; }
    console.log('=== ' + q.img.split('/').pop() + ' ===');
    console.log(res.choices[0].message.content);
    console.log('');
    await sleep(4000);
  }
}
main().catch(e => { console.error('VLM_FAIL', e.message); process.exit(1); });

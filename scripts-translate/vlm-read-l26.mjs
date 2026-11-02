import ZAI from 'z-ai-web-dev-sdk';
import fs from 'fs';

// R527 — relecture VLM de la leçon 26 (Kahf p.195-201, slot 764) :
// badge NUM 102-105, boîte des āyāt (médaillons = tranchage décalage
// imprimé→cache), p.201 تقويم/استثمار (clôture leçon), p.202 annexe.
const qs = [
  { img: '/home/z/my-project/tr-tmp/probe-l26-p195-badge.png',
    ask: `En-tête de page d'un manuel arabe (très zoomé). Transcris EXACTEMENT, mot à mot, chiffres arabes-orientaux exacts : (1) la ligne du badge de sourate (سورة الكهف et la plage de versets entre parenthèses) ; (2) le numéro de leçon s'il apparaît. Format :
BADGE: <texte exact>` },
  { img: '/home/z/my-project/tr-tmp/probe-l26-p195-objets-tamhid.png',
    ask: `Page de manuel arabe (tafsīr, fin de sūrat al-Kahf). Transcris EXACTEMENT mot à mot : (1) la ligne أهداف الدرس ; (2) les trois objectifs numérotés 1 2 3 ; (3) le paragraphe للتمهيد ENTIER (les deux أمور ordonnés au Prophète, la phrase sur l'espoir des gens, la clôture de la sūrah, et les questions des questions). Format :
OBJ1: <texte>
OBJ2: <texte>
OBJ3: <texte>
TAMHID: <texte entier>` },
  { img: '/home/z/my-project/tr-tmp/probe-l26-p195-box-top.png',
    ask: `Boîte d'extrait coranique (muṣḥaf crop) d'un manuel arabe, très zoomé. Transcris EXACTEMENT mot à mot : (1) le NUMÉRO entre parenthèses ou dans un médaillon/cercle au début (chiffre exact) ; (2) le TEXTE du premier verset visible ENTIER avec ses signes diacritiques ; (3) tout numéro de médaillon intermédiaire. Format :
MEDAILLON1: <numéro exact>
VERSET1: <texte exact>
MEDAILLON2: <numéro exact si visible>
VERSET2: <texte exact si visible>` },
  { img: '/home/z/my-project/tr-tmp/probe-l26-p195-box-bot.png',
    ask: `Boîte d'extrait coranique (muṣḥaf crop) d'un manuel arabe, très zoomé. Transcris EXACTEMENT mot à mot, dans l'ordre : chaque numéro de médaillon/cercle (chiffre exact) suivi du texte du verset visible ENTIER. Il peut y avoir 2-4 médaillons (ex. 102 103 104 105). Format :
MEDAILLON: <numéro>
VERSET: <texte exact>` },
  { img: '/home/z/my-project/tr-tmp/probe-l26-p195-box.png',
    ask: `Boîte d'extrait coranique (muṣḥaf crop) d'un manuel arabe. Donne : (1) la LISTE de tous les numéros de médaillons/cercles visibles de droite à gauche (chiffres exacts) ; (2) le premier mot du verset sous chaque médaillon ; (3) la référence entre crochets en bas de la boîte (ex. [الكهف: ...] avec chiffres exacts). Format :
MEDAILLONS: <liste>
PREMIERS_MOTS: <médaillon → premier mot>
REF: <référence exacte>` },
  { img: '/home/z/my-project/tr-tmp/probe-l26-p201-full.png',
    ask: `Page de fin de leçon d'un manuel arabe (tafsīr). Transcris EXACTEMENT mot à mot : (1) le titre de la section (التقويم ou autre) ; (2) les trois questions numérotées ENTIÈRES (avec les fragments de versets cités entre guillemets) ; (3) le titre de la section suivante (الاستثمار ou autre) ; (4) le texte de l'استثمار ENTIER (consignes numérotées et lignes suivantes, y compris toute liste) ; (5) toute ligne finale en bas de page. Format :
TITRE1: <texte>
Q1: <texte>
Q2: <texte>
Q3: <texte>
TITRE2: <texte>
ISTITHMAR: <texte entier>
FIN: <texte>` },
  { img: '/home/z/my-project/tr-tmp/probe-l26-p202-head.png',
    ask: `Haut de page d'un manuel arabe (annexe). Transcris EXACTEMENT mot à mot : (1) le TITRE de la section/page ; (2) la ligne des objectifs (أهداف الأنشطة) ; (3) les trois objectifs numérotés ; (4) le titre du premier نشاط et sa première phrase. Format :
TITRE: <texte>
OBJ_TITRE: <texte>
OBJ1: <texte>
OBJ2: <texte>
OBJ3: <texte>
NACHAT: <texte>` },
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
      model: 'glm-5v-turbo', max_tokens: 1600,
    });
    console.log('=== ' + q.img.split('/').pop() + ' ===');
    console.log(res.choices[0].message.content);
    console.log('');
  }
}
main().catch(e => { console.error('VLM_FAIL', e.message); process.exit(1); });

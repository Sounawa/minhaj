/**
 * Minhāj R9 — Corrections de grille :
 *  1. usul-fiqh-waraqat : level tanawi-2 → 3es (preuve : annonce officielle 10962
 *     « إصدار أصول الفقه من ورقات إمام الحرمين بشرح الحطاب للسنة الثالثة من التعليم الإعدادي »
 *     + intro du livre « pour la troisième année de l'enseignement préparatoire ancien »).
 *  2. Création du 64ᵉ livre : hadith-tanawi-2 (Muwaṭṭaʾ — 2ᵉ année secondaire),
 *     intro bilingue rédigée à la main ; leçons non publiées par le ministère
 *     (aucune catégorie ni page sur le site officiel — vérifié R9).
 * Usage: bun run scripts-recovery/r9-grid-fix.ts
 */
import { readFileSync, writeFileSync } from "fs";
import path from "path";

const BOOKS = path.join(process.cwd(), "content", "books");

/* ————— 1. Waraqat : 3es ————— */
const waraqatPath = path.join(BOOKS, "usul-fiqh-waraqat.json");
const w = JSON.parse(readFileSync(waraqatPath, "utf8"));
w.level = "3es";
w.levelAr = "السنة الثالثة من السلك الإعدادي العتيق";
writeFileSync(waraqatPath, JSON.stringify(w, null, 1) + "\n");
console.log("usul-fiqh-waraqat → level 3es ✓");

/* ————— 2. hadith-tanawi-2 (64ᵉ livre) ————— */
const introAr = `«الحديث من موطأ الإمام مالك بشرح الزرقاني» — منهج السنة الثانية من التعليم الثانوي العتيق. يتواصل برنامج مادة الحديث في هذا المستوى مع كتاب «الموطأ» للإمام مالك بن أنس الأصبحي (ت 179هـ)، بشرح العلامة محمد بن عبد الباقي الزرقاني (ت 1122هـ)، بعد أن درس التلاميذ في السنة الأولى من هذا السلك أبواب النكاح والطلاق والعدة والرضاع من الكتاب ذاته. وتعالج دروس هذه السنة — بحسب المنهاج النموذجي للتعليم العتيق — طائفة من أبواب الموطأ تجمع بين العبادات والمعاملات، مع العناية بتقوية الملكة الحديثية للتلميذ: ضبط المتون، وإسناد الحديث، وفقه معانيه، وربطها بقضايا الواقع.

ملاحظة: لم تنشر وزارة الأوقاف والشؤون الإسلامية دروس هذا المستوى في بوابة الموقع الرسمي إلى تاريخ إعداد هذا المصحف الرقمي، وخلافا لبقية المستويات لا توجد لهذه السنة صفحة كتاب ولا صفحة دروس منشورة. وسْيُدرج المحتوى فور نشره رسميا.`;

const introFr = `Le ḥadīth en 2ᵉ année du cycle secondaire (taʿlīm ʿatīq) poursuit l'étude du <em>Muwaṭṭaʾ</em> de l'imam Mālik b. Anas al-Aṣbaḥī (m. 179/795), avec le commentaire (<i>šarḥ</i>) du savant Muḥammad b. ʿAbd al-Bāqī al-Zarqānī (m. 1122/1710). Après avoir étudié en première année les chapitres du mariage, du divorce, de la retraite légale et de l'allaitement tirés du même ouvrage, les élèves abordent cette année — conformément au programme modèle de l'enseignement traditionnel — un ensemble de chapitres du <em>Muwaṭṭaʾ</em> qui associent culte et transactions, avec un soin particulier porté à la formation du disciple : mémorisation des textes, chaînes de transmission, intelligence juridique du hadith et mise en relation avec les questions contemporaines.

<em>Note :</em> le ministère des Habous et des Affaires islamiques n'a pas encore publié les leçons de ce niveau sur son portail officiel à la date de constitution de cette bibliothèque numérique — contrairement aux autres niveaux, ni page d'ouvrage ni page de cours n'existent pour cette année. Le contenu sera intégré dès sa publication officielle.`;

const book = {
  id: "hadith-tanawi-2",
  subject: "hadith",
  level: "tanawi-2",
  subjectAr: "الحديث",
  levelAr: "السنة الثانية من السلك الثانوي العتيق",
  titleAr: "الحديث من موطأ الإمام مالك بشرح الزرقاني للسنة الثانية من التعليم الثانوي العتيق",
  titleFr: "Ḥadīth — le Muwaṭṭaʾ de l'imam Mālik (2ᵉ lycée)",
  pdfUrl: null,
  unpublished: true,
  intro: {
    docId: "muqaddima",
    titleAr: "تقديم المادة",
    titleFr: "Présentation du manuel",
    html: `<p>${introAr.split("\n\n")[0]}</p>\n<p>${introAr.split("\n\n")[1]}</p>`,
    htmlFr: introFr,
  },
  lessons: [],
};

writeFileSync(path.join(BOOKS, "hadith-tanawi-2.json"), JSON.stringify(book, null, 1) + "\n");
console.log("hadith-tanawi-2 créé (intro bilingue, 0 leçon — non publié par le ministère) ✓");

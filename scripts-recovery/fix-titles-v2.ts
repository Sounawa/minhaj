/**
 * fix-titles-v2.ts — Régénère les titres AR+FR des leçons « placeholder »
 * (أهداف الدرس / الأهداف / &nbsp; / vide) depuis le h1 réel du document.
 * Traductions FR faites main (terminologie académique, pas de GT-ismes).
 *
 * Usage : bun scripts-recovery/fix-titles-v2.ts [--dry]
 */
import * as fs from 'fs';
import * as path from 'path';

const ROOT = path.join(import.meta.dir, '..');
const BOOKS = path.join(ROOT, 'content', 'books');
const DRY = process.argv.includes('--dry');

// [fichier, docId, titleAr propre, titleFr]
const MAP: [string, string, string, string][] = [
  // ── Ulum al-Quran 1ère collège ──────────────────────────────
  ['ulum-quran-1es', '15381', 'علوم القرآن: التعريف والفوائد', 'Les sciences du Coran : définition et bienfaits'],
  ['ulum-quran-1es', '15396', 'علوم القرآن: تاريخ علوم القرآن', 'Les sciences du Coran : histoire des sciences coraniques'],
  ['ulum-quran-1es', '15402', 'علوم القرآن: نزول القرآن الكريم', 'Les sciences du Coran : la descente du Noble Coran'],
  ['ulum-quran-1es', '15423', 'علوم القرآن: نزول القرآن الكريم (تتمة)', 'Les sciences du Coran : la descente du Noble Coran (suite)'],
  ['ulum-quran-1es', '15653', 'علوم القرآن: أول ما نزل وآخر ما نزل', 'Les sciences du Coran : le premier et le dernier révélé'],
  ['ulum-quran-1es', '15752', 'علوم القرآن: أسباب النزول', 'Les sciences du Coran : les causes de la révélation (asbāb al-nuzūl)'],
  ['ulum-quran-1es', '15765', 'علوم القرآن: أسباب النزول (تتمة)', 'Les sciences du Coran : les causes de la révélation (suite)'],
  ['ulum-quran-1es', '15841', 'علوم القرآن: نزول القرآن على سبعة أحرف', 'Les sciences du Coran : la révélation selon sept lettres (aḥruf)'],
  ['ulum-quran-1es', '15855', 'علوم القرآن: المكي والمدني', 'Les sciences du Coran : mecquois et médinois'],
  ['ulum-quran-1es', '15887', 'علوم القرآن: جمع القرآن', 'Les sciences du Coran : la compilation du Coran'],
  // ── Ulum al-Quran 2nde collège ──────────────────────────────
  ['ulum-quran-2es', '19261', 'التفسير الفقهي للقرآن الكريم', 'Le tafsīr juridique du Noble Coran'],
  // ── Qiraʾat 1ère secondaire (al-Shāṭibiyya) ─────────────────
  ['qiraat-tanawi-1', '19030', 'القراءات: افتتاح القصيدة بالآداب الشرعية', 'Les qirāʾāt : l\u2019ouverture du poème par les règles religieuses'],
  ['qiraat-tanawi-1', '19039', 'القراءات: فضائل القرآن وآثاره على قارئه', 'Les qirāʾāt : les mérites du Coran et ses effets sur le récitant'],
  ['qiraat-tanawi-1', '19042', 'القراءات: القراء السبعة ورواتهم (1)', 'Les qirāʾāt : les sept lecteurs et leurs transmetteurs (1)'],
  ['qiraat-tanawi-1', '19045', 'القراءات: القراء السبعة ورواتهم (2)', 'Les qirāʾāt : les sept lecteurs et leurs transmetteurs (2)'],
  ['qiraat-tanawi-1', '19046', 'القراءات: طرق القراءة ورموز القراء الإفرادية', 'Les qirāʾāt : voies de lecture et symboles individuels des lecteurs'],
  ['qiraat-tanawi-1', '19051', 'القراءات: رموز القراءة الجماعية ومنهج استعمالها', 'Les qirāʾāt : symboles de lecture collective et leur usage'],
  ['qiraat-tanawi-1', '19145', 'القراءات: اصطلاحات الناظم ومنهج استعمالها (1)', 'Les qirāʾāt : les conventions du poète et leur usage (1)'],
  ['qiraat-tanawi-1', '19146', 'القراءات: اصطلاحات الناظم ومنهج استعمالها (2)', 'Les qirāʾāt : les conventions du poète et leur usage (2)'],
  ['qiraat-tanawi-1', '19159', 'القراءات: التعريف بقصيدة الشاطبية', 'Les qirāʾāt : présentation du poème al-Shāṭibiyya'],
  ['qiraat-tanawi-1', '19160', 'القراءات: وصايا الناظم لحملة القرآن', 'Les qirāʾāt : les recommandations du poète aux porteurs du Coran'],
  ['qiraat-tanawi-1', '19205', 'القراءات: الاستعاذة', 'Les qirāʾāt : la formule de refuge (istiʿādha)'],
  // ── Rasm wa Dabt 4e primaire ────────────────────────────────
  ['rasm-wa-dabt-4ep', '19725', 'الرسم والضبط: فصل الهمزة', 'L\u2019écriture et la vocalisation : le chapitre de la hamza'],
  // ── Hadith 1ère secondaire (Muwaṭṭaʾ, sharh al-Zarqānī) ────
  ['hadith-tanawi-1', '13124', 'عدة المتوفى عنها زوجها', 'La viduité de la femme dont l\u2019époux est décédé (ʿidda)'],
  // ── Tafsir 5e primaire ──────────────────────────────────────
  ['tafsir-5ep', '13886', 'سورة الانفطار الآيات (1 - 8)', 'Sourate al-Infiṭār, versets 1 à 8'],
  // ── Tajwid 5e primaire ──────────────────────────────────────
  ['tajwid-5ep', '15852', 'التجويد: تطبيقات على المد الطبيعي', 'Le tajwīd : applications de l\u2019allongement naturel (madd ṭabīʿī)'],
  // ── Mantiq 1ère secondaire (Naẓm al-Sullam) ─────────────────
  ['mantiq-tanawi-1', '16143', 'مباحث الألفاظ', 'Les chapitres des termes (alfāẓ)'],
  ['mantiq-tanawi-1', '16145', 'مباحث الألفاظ (تابع)', 'Les chapitres des termes (suite)'],
  ['mantiq-tanawi-1', '16146', 'مباحث الألفاظ (تتمة)', 'Les chapitres des termes (fin)'],
  ['mantiq-tanawi-1', '16150', 'أنشطة لاستثمار التعلمات ودعمها', 'Activités d\u2019exploitation et de consolidation des apprentissages'],
  ['mantiq-tanawi-1', '16156', 'الكليات الخمس', 'Les cinq universaux (al-kulliyyāt al-khamsa)'],
  ['mantiq-tanawi-1', '16159', 'نسبة الألفاظ للمعاني', 'Le rapport des termes aux significations'],
  ['mantiq-tanawi-1', '16160', 'نسبة الألفاظ للمعاني (تتمة)', 'Le rapport des termes aux significations (fin)'],
  ['mantiq-tanawi-1', '16166', 'الخبر والطلب', 'L\u2019énoncé informatif (khabar) et l\u2019énoncé injonctif (ṭalab)'],
  ['mantiq-tanawi-1', '16167', 'الكل والكلية', 'Le tout et la totalité (al-kull et al-kulliyya)'],
  // ── Uṣūl al-Fiqh 1ère secondaire (al-Warāqāt) ───────────────
  ['usul-fiqh-waraqat', '11800', 'التعريف بالكتاب ومؤلفيه', 'Présentation du livre et de ses auteurs'],
  ['usul-fiqh-waraqat', '11802', 'تعريف أصول الفقه', 'Définition des fondements du droit (uṣūl al-fiqh)'],
  ['usul-fiqh-waraqat', '11854', 'تعريف الحكم الشرعي وأقسامه', 'Le statut juridique (ḥukm sharʿī) : définition et catégories'],
  ['usul-fiqh-waraqat', '11856', 'تعريف العلم وأنواعه وطرق تحصيله', 'La science : définition, types et voies d\u2019acquisition'],
  ['usul-fiqh-waraqat', '11857', 'مباحث أصول الفقه وتقسيم الكلام', 'Les chapitres de l\u2019uṣūl et la division du discours'],
  ['usul-fiqh-waraqat', '11862', 'الحقيقة والمجاز', 'Sens propre (ḥaqīqa) et sens figuré (majāz)'],
  ['usul-fiqh-waraqat', '11866', 'الأمر: صيغته ودلالته', 'L\u2019ordre (amr) : sa formule et sa signification'],
  ['usul-fiqh-waraqat', '11867', 'ما يدخل في الأمر والنهي وما تستلزمه صيغتهما', 'Ce qui relève de l\u2019ordre et de l\u2019interdit, et les implications de leurs formules'],
  ['usul-fiqh-waraqat', '11869', 'النهي: صيغته ودلالته', 'L\u2019interdit (nahy) : sa formule et sa signification'],
  ['usul-fiqh-waraqat', '11872', 'تعريف العام وألفاظ العموم', 'Le général (ʿāmm) : définition et expressions'],
  ['usul-fiqh-waraqat', '11873', 'الخاص', 'Le particulier (khāṣṣ)'],
  ['usul-fiqh-waraqat', '11874', 'الخاص: المخصصات المنفصلة', 'Le particulier : les spécificateurs disjoints'],
  ['usul-fiqh-waraqat', '11878', 'المجمل والمبين', 'L\u2019indéterminé (mujmal) et le clarifié (mubayyan)'],
  ['usul-fiqh-waraqat', '11881', 'النص والظاهر والتأويل', 'Le texte explicite (naṣṣ), l\u2019apparent (ẓāhir) et l\u2019interprétation (taʾwīl)'],
  ['usul-fiqh-waraqat', '11882', 'حكم أفعال الرسول ﷺ', 'Le statut des actes du Messager ﷺ'],
  ['usul-fiqh-waraqat', '11883', 'حكم الإقرار النبوي', 'Le statut de l\u2019approbation prophétique (iqrār)'],
  ['usul-fiqh-waraqat', '11887', 'تعريف النسخ وحكمه', 'L\u2019abrogation (naskh) : définition et statut'],
  ['usul-fiqh-waraqat', '11890', 'أنواع النسخ', 'Les types d\u2019abrogation'],
  ['usul-fiqh-waraqat', '11898', 'طرق دفع التعارض بين النصوص', 'Les moyens de lever la contradiction entre les textes'],
  ['usul-fiqh-waraqat', '11904', 'الإجماع', 'Le consensus (ijmāʿ)'],
  ['usul-fiqh-waraqat', '11907', 'الخبر وأقسامه', 'Le rapport (khabar) et ses catégories'],
  ['usul-fiqh-waraqat', '11910', 'أقسام خبر الآحاد', 'Les catégories du rapport singulier (khabar āḥād)'],
  ['usul-fiqh-waraqat', '11913', 'من صيغ التحمل والأداء في الرواية', 'Les formules de réception et de transmission du récit (riwāya)'],
  ['usul-fiqh-waraqat', '11915', 'القياس وأقسامه', 'L\u2019analogie (qiyās) et ses catégories'],
  ['usul-fiqh-waraqat', '11917', 'شروط أركان القياس', 'Les conditions des piliers de l\u2019analogie'],
  ['usul-fiqh-waraqat', '11919', 'الاستصحاب وترتيب الأدلة', 'La présomption de continuité (istiṣḥāb) et l\u2019ordre des preuves'],
  ['usul-fiqh-waraqat', '11921', 'شروط المجتهد وأحكام التقليد', 'Les conditions du mujtahid et les règles du taqlīd'],
  ['usul-fiqh-waraqat', '11926', 'حكم الاجتهاد ومراتبه', 'Le statut de l\u2019ijtihād et ses degrés'],
];

const PLACEHOLDER = /^(أهداف الدرس|الأهداف|&nbsp;|\u00a0|\s*)$/;

let fixed = 0, missed: string[] = [];
const byFile = new Map<string, Map<string, [string, string]>>();
for (const [file, id, ar, fr] of MAP) {
  if (!byFile.has(file)) byFile.set(file, new Map());
  byFile.get(file)!.set(id, [ar, fr]);
}

for (const [file, fixes] of byFile) {
  const p = path.join(BOOKS, file + '.json');
  if (!fs.existsSync(p)) { missed.push(file + ' (fichier absent)'); continue; }
  const book = JSON.parse(fs.readFileSync(p, 'utf8'));
  let changed = false;
  for (const lesson of book.lessons) {
    const fix = fixes.get(String(lesson.docId));
    const isPlaceholder = PLACEHOLDER.test((lesson.titleAr || '').replace(/\u00a0/g, '').trim());
    if (fix && isPlaceholder) {
      lesson.titleAr = fix[0];
      lesson.titleFr = fix[1];
      fixed++; changed = true;
    } else if (fix && !isPlaceholder) {
      // titre déjà correct mais vérifier FR vide
      if (!lesson.titleFr) { lesson.titleFr = fix[1]; fixed++; changed = true; }
    }
  }
  if (changed && !DRY) fs.writeFileSync(p, JSON.stringify(book, null, 1) + '\n');
  console.log(`${DRY ? '[dry] ' : ''}${file}: ${changed ? 'mis à jour' : 'aucun changement'}`);
}

// vérif résiduelle
if (!DRY) {
  let residual = 0;
  for (const f of fs.readdirSync(BOOKS)) {
    const b = JSON.parse(fs.readFileSync(path.join(BOOKS, f), 'utf8'));
    for (const l of b.lessons) {
      if (PLACEHOLDER.test((l.titleAr || '').replace(/\u00a0/g, '').trim()) || !l.titleFr || !l.htmlFr) {
        residual++;
        console.log('  RÉSIDUEL:', f, l.docId, JSON.stringify(l.titleAr), 'titleFr:', !!l.titleFr, 'htmlFr:', !!l.htmlFr);
      }
    }
  }
  console.log(`\nTitres corrigés: ${fixed}/${MAP.length} | docs résiduels incomplets: ${residual}`);
}
if (missed.length) console.log('PROBLÈMES:', missed.join(', '));

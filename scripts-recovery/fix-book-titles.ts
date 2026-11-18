/**
 * fix-book-titles.ts — Réécrit les titres FR des 59 livres avec une
 * convention académique cohérente (matière — œuvre de référence, commentaire),
 * et restaure les titleAr/textbookAr propres (fin des placeholders
 * « مقدمة الكتاب / فهرس الموضوعات »).
 *
 * Usage : bun scripts-recovery/fix-book-titles.ts
 */
import * as fs from "fs";
import * as path from "path";

const ROOT = path.join(import.meta.dir, "..");
const BOOKS_DIR = path.join(ROOT, "content", "books");
const MANIFEST = path.join(ROOT, "content", "manifest.json");

interface Entry {
  id: string;
  /** Titre FR affiché (fichier + manifeste). */
  titleFr: string;
  /** Titre arabe complet de l'œuvre (titleAr du fichier, textbookAr du manifeste). */
  titleAr?: string;
}

const TITLES: Entry[] = [
  // ── Fiqh ─────────────────────────────────────────────────────────────
  { id: "fiqh-1ep", titleFr: "Fiqh — le Mukhtaṣar d'al-Akhdarī, comm. d'al-Ābī al-Azharī" },
  { id: "fiqh-4ep", titleFr: "Fiqh — le Mukhtaṣar d'al-Akhdarī, comm. d'al-Ābī al-Azharī" },
  { id: "fiqh-6ep", titleFr: "Fiqh — le Murshid al-Muʿīn d'Ibn ʿĀshir, comm. de Mayyāra", titleAr: "الفقه من منظومة المرشد المعين لابن عاشر بشرح ميارة" },
  { id: "fiqh-1es", titleFr: "Fiqh — la Risāla d'Ibn Abī Zayd al-Qayrawānī", titleAr: "الفقه من متن الرسالة لابن أبي زيد القيرواني بشرح كفاية الطالب الرباني" },
  { id: "fiqh-3es", titleFr: "Fiqh — la Risāla d'Ibn Abī Zayd al-Qayrawānī (suite)", titleAr: "الفقه من متن الرسالة لابن أبي زيد القيرواني بشرح كفاية الطالب الرباني بحاشية العدوي" },
  { id: "fiqh-tanawi-1", titleFr: "Fiqh — le Mukhtaṣar de Khalīl, comm. d'al-Dardīr et ḥāshiya d'al-Dasūqī", titleAr: "الفقه من متن مختصر الشيخ خليل بشرح الدردير وحاشية الدسوقي" },
  { id: "fiqh-tanawi-3", titleFr: "Fiqh — le Mukhtaṣar de Khalīl (suite du programme)", titleAr: "الفقه من متن مختصر الشيخ خليل بشرح الدردير وحاشية الدسوقي" },
  // ── Ḥadīth ───────────────────────────────────────────────────────────
  { id: "hadith-1ep", titleFr: "Ḥadīth — Riyāḍ al-Ṣāliḥīn d'al-Nawawī, comm. Rawḍat al-Muttaqīn", titleAr: "الحديث من رياض الصالحين للإمام النووي بشرح روضة المتقين" },
  { id: "hadith-6ep", titleFr: "Ḥadīth — les Quarante hadiths d'al-Nawawī, comm. d'Ibn Daqīq al-ʿĪd", titleAr: "الحديث من كتاب الأربعين النووية بشرح ابن دقيق العيد" },
  { id: "hadith-1es", titleFr: "Ḥadīth — le Muwaṭṭaʾ de l'imam Mālik, comm. d'al-Zarqānī", titleAr: "الحديث من موطأ الإمام مالك بشرح الزرقاني" },
  { id: "hadith-3es", titleFr: "Ḥadīth — le Muwaṭṭaʾ de l'imam Mālik (suite)", titleAr: "الحديث من موطأ الإمام مالك بشرح الزرقاني" },
  { id: "hadith-tanawi-1", titleFr: "Ḥadīth — le Muwaṭṭaʾ de l'imam Mālik (lycée)", titleAr: "الحديث من موطأ الإمام مالك بشرح الزرقاني" },
  { id: "hadith-tanawi-3", titleFr: "Ḥadīth — le Muwaṭṭaʾ de l'imam Mālik (3ᵉ lycée)", titleAr: "كتاب الحديث من موطأ الإمام مالك بشرح الزرقاني" },
  // ── Tafsīr ───────────────────────────────────────────────────────────
  { id: "tafsir-1ep", titleFr: "Tafsīr — le Tafsīr al-Jalālayn", titleAr: "التفسير من خلال تفسير الجلالين" },
  { id: "tafsir-4ep", titleFr: "Tafsīr — le Tafsīr al-Jalālayn", titleAr: "التفسير من خلال تفسير الجلالين" },
  { id: "tafsir-5ep", titleFr: "Tafsīr — le Tafsīr al-Jalālayn", titleAr: "التفسير من خلال تفسير الجلالين" },
  { id: "tafsir-6ep", titleFr: "Tafsīr — le Tafsīr al-Jalālayn", titleAr: "التفسير من خلال تفسير الجلالين" },
  { id: "tafsir-1es", titleFr: "Tafsīr — al-Tashīl li-ʿUlūm al-Tanzīl d'Ibn Juzayy", titleAr: "التفسير من خلال التسهيل لعلوم التنزيل لابن جزي" },
  { id: "tafsir-2es", titleFr: "Tafsīr — al-Tashīl li-ʿUlūm al-Tanzīl d'Ibn Juzayy (suite)", titleAr: "التفسير من خلال التسهيل لعلوم التنزيل لابن جزي" },
  { id: "tafsir-3es", titleFr: "Tafsīr — al-Tashīl li-ʿUlūm al-Tanzīl d'Ibn Juzayy (fin)", titleAr: "التفسير من خلال التسهيل لعلوم التنزيل لابن جزي" },
  { id: "tafsir-tanawi-1", titleFr: "Tafsīr — al-Muḥarrar al-Wajīz d'Ibn ʿAṭiyya", titleAr: "التفسير من خلال المحرر الوجيز في تفسير الكتاب العزيز لابن عطية" },
  { id: "tafsir-tanawi-2", titleFr: "Tafsīr — al-Muḥarrar al-Wajīz d'Ibn ʿAṭiyya (suite)", titleAr: "التفسير من خلال المحرر الوجيز في تفسير الكتاب العزيز لابن عطية" },
  { id: "tafsir-tanawi-3", titleFr: "Tafsīr — la sourate al-Kahf (al-Muḥarrar al-Wajīz)", titleAr: "تفسير سورة الكهف من خلال المحرر الوجيز في تفسير الكتاب العزيز لابن عطية" },
  // ── Tajwīd ───────────────────────────────────────────────────────────
  { id: "tajwid-5ep", titleFr: "Tajwīd — applications de la Tuḥfat al-Aṭfāl d'al-Jamzūrī", titleAr: "التجويد: تطبيقات على نظم تحفة الأطفال للجمزوري" },
  { id: "tajwid-6ep", titleFr: "Tajwīd — Naẓm al-Durar al-Lawāmiʿ d'Ibn Barrī", titleAr: "التجويد من نظم الدرر اللوامع للإمام ابن بري" },
  { id: "tajwid-2es", titleFr: "Tajwīd — al-Durar al-Lawāmiʿ d'Ibn Barrī, comm. al-Nujūm al-Ṭawāliʿ", titleAr: "التجويد من نظم الدرر اللوامع لابن بري بشرح النجوم الطوالع لإبراهيم المارغني" },
  { id: "tajwid-3es", titleFr: "Tajwīd — al-Durar al-Lawāmiʿ d'Ibn Barrī (suite)", titleAr: "التجويد من نظم الدرر اللوامع لابن بري بشرح النجوم الطوالع لإبراهيم المارغني" },
  // ── Qirāʾāt ──────────────────────────────────────────────────────────
  { id: "qiraat-tanawi-1", titleFr: "Qirāʾāt — Ḥirz al-Amānī (al-Shāṭibiyya) d'al-Shāṭibī", titleAr: "القراءات من متن حرز الأماني ووجه التهاني لأبي القاسم الشاطبي" },
  { id: "qiraat-tanawi-2", titleFr: "Qirāʾāt — Ḥirz al-Amānī (al-Shāṭibiyya, suite)", titleAr: "القراءات من متن حرز الأماني ووجه التهاني لأبي القاسم الشاطبي" },
  { id: "qiraat-tanawi-3", titleFr: "Qirāʾāt — Ḥirz al-Amānī (al-Shāṭibiyya, 3ᵉ lycée)", titleAr: "القراءات من متن حرز الأماني ووجه التهاني لأبي القاسم الشاطبي" },
  // ── Tawḥīd ───────────────────────────────────────────────────────────
  { id: "tawhid-1es", titleFr: "Tawḥīd — la Risāla d'Ibn Abī Zayd al-Qayrawānī", titleAr: "التوحيد من متن الرسالة لابن أبي زيد القيرواني" },
  { id: "tawhid-2es", titleFr: "Tawḥīd — le Murshid al-Muʿīn d'Ibn ʿĀshir", titleAr: "التوحيد من منظومة المرشد المعين على الضروري من علوم الدين لعبد الواحد بن عاشر" },
  // ── Sīra ─────────────────────────────────────────────────────────────
  { id: "sira-1es", titleFr: "Sīra — la biographie du Prophète ﷺ", titleAr: "السيرة النبوية" },
  { id: "sira-2es", titleFr: "Sīra — la biographie du Prophète ﷺ (2ᵉ collège)", titleAr: "السيرة النبوية" },
  { id: "sira-3es", titleFr: "Sīra — la biographie du Prophète ﷺ (3ᵉ collège)", titleAr: "السيرة النبوية" },
  // ── Sciences du Coran / du Ḥadīth ────────────────────────────────────
  { id: "ulum-quran-1es", titleFr: "Sciences du Coran — ʿulūm al-Qurʾān", titleAr: "علوم القرآن" },
  { id: "ulum-quran-2es", titleFr: "Sciences du Coran — ʿulūm al-Qurʾān (2ᵉ collège)", titleAr: "علوم القرآن" },
  { id: "ulum-quran-3es", titleFr: "Sciences du Coran — ʿulūm al-Qurʾān (3ᵉ collège)", titleAr: "علوم القرآن" },
  { id: "ulum-hadith-tanawi-1", titleFr: "Sciences du ḥadīth — la Manẓūma al-Bayqūniyya, comm. d'al-Zarqānī", titleAr: "علوم الحديث من المنظومة البيقونية بشرح الزرقاني" },
  { id: "ulum-hadith-tanawi-2", titleFr: "Sciences du ḥadīth — 2ᵉ lycée", titleAr: "علوم الحديث" },
  { id: "ulum-hadith-tanawi-3", titleFr: "Sciences du ḥadīth — 3ᵉ lycée", titleAr: "علوم الحديث" },
  // ── Uṣūl al-fiqh ─────────────────────────────────────────────────────
  { id: "usul-fiqh-tanawi-1", titleFr: "Uṣūl al-fiqh — la Manẓūma Marṭaqī al-Wuṣūl d'Ibn ʿĀṣim", titleAr: "أصول الفقه من منظومة مرتقى الوصول إلى الضروري من الأصول لابن عاصم الغرناطي" },
  { id: "usul-fiqh-tanawi-2", titleFr: "Uṣūl al-fiqh — Marṭaqī al-Wuṣūl d'Ibn ʿĀṣim (2ᵉ lycée)", titleAr: "أصول الفقه من منظومة مرتقى الوصول إلى الضروري من الأصول لابن عاصم الغرناطي" },
  { id: "usul-fiqh-tanawi-3", titleFr: "Uṣūl al-fiqh — Marṭaqī al-Wuṣūl d'Ibn ʿĀṣim (3ᵉ lycée)", titleAr: "أصول الفقه من منظومة مرتقى الوصول إلى الضروري من الأصول لابن عاصم الغرناطي" },
  { id: "usul-fiqh-waraqat", titleFr: "Uṣūl al-fiqh — al-Warāqāt d'al-Juwaynī, comm. d'al-Ḥaṭṭāb", titleAr: "كتاب أصول الفقه من ورقات إمام الحرمين بشرح الحطاب الرعيني" },
  // ── Mantiq / Fikr islāmī ─────────────────────────────────────────────
  { id: "mantiq-tanawi-1", titleFr: "Mantiq — Naẓm al-Sullam d'al-Akhdarī, comm. d'al-Qawasnī", titleAr: "المنطق من نظم السلم المنورق لعبد الرحمان الأخضري بشرح حسن القويسني" },
  { id: "fikr-islami-tanawi-1", titleFr: "Pensée islamique — questions kalāmiques", titleAr: "الفكر الإسلامي: قضايا كلامية" },
  { id: "fikr-islami-tanawi-2", titleFr: "Pensée islamique — la philosophie musulmane", titleAr: "الفكر الإسلامي: الفلسفة الإسلامية" },
  { id: "fikr-islami-tanawi-3", titleFr: "Pensée islamique — le soufisme (taṣawwuf)", titleAr: "الفكر الإسلامي: التصوف الإسلامي" },
  // ── Farāʾiḍ / Tawqīt ─────────────────────────────────────────────────
  { id: "faraid-tanawi-3", titleFr: "Farāʾiḍ — la Manẓūma al-Jawāhir al-Maknūna (successions)", titleAr: "الفرائض من منظومة الجواهر المكنونة في صدف الفرائض المسنونة" },
  { id: "taqtit-tanawi-1", titleFr: "Tawqīt — al-Muqniʿ d'al-Marghīthī (comput religieux)", titleAr: "التوقيت من منظومة المقنع بشرح المطلع على مسائل المقنع لمحمد بن سعيد المرغتي" },
  { id: "taqtit-tanawi-2", titleFr: "Tawqīt — ʿUmdat Ahl al-Thabt (temps et orientations)", titleAr: "التوقيت من منظومة عمدة أهل الثبت في علم الأوقات وسمت البيت" },
  { id: "taqtit-tanawi-3", titleFr: "Tawqīt — al-Jāmiʿ al-Mufīd (éclipses et croissants)", titleAr: "التوقيت من منظومة الجامع المفيد في حساب الخسوف والكسوف ورؤية الأهلة" },
  // ── Rasm wa ḍabṭ ────────────────────────────────────────────────────
  { id: "rasm-wa-dabt-4ep", titleFr: "Rasm et ḍabṭ — graphie et vocalisation coraniques", titleAr: "الرسم والضبط" },
  { id: "rasm-wa-dabt-5ep", titleFr: "Rasm et ḍabṭ — ʿUmdat al-Bayān d'al-Wadghīrī", titleAr: "الرسم والضبط من أرجوزة عمدة البيان لإدريس الودغيري" },
  { id: "rasm-wa-dabt-6ep", titleFr: "Rasm et ḍabṭ — ʿUmdat al-Bayān d'al-Wadghīrī (fin)", titleAr: "الرسم والضبط من أرجوزة عمدة البيان لإدريس الودغيري" },
  // ── Fondements des valeurs ────────────────────────────────────────────
  { id: "usul-qiyam-4ep", titleFr: "Fondements des valeurs dans le Coran et la Sunna", titleAr: "أصول القيم في القرآن والسنة" },
  { id: "usul-qiyam-5ep", titleFr: "Fondements des valeurs dans le Coran et la Sunna (5ᵉ)", titleAr: "أصول القيم في القرآن والسنة" },
  { id: "usul-qiyam-6ep", titleFr: "Fondements des valeurs dans le Coran et la Sunna (6ᵉ)", titleAr: "أصول القيم في القرآن والسنة" },
];

// ── Application ────────────────────────────────────────────────────────
const map = new Map(TITLES.map((t) => [t.id, t]));
const files = fs.readdirSync(BOOKS_DIR);
let filesFixed = 0;

for (const f of files) {
  if (!f.endsWith(".json")) continue;
  const id = f.replace(/\.json$/, "");
  const entry = map.get(id);
  if (!entry) {
    console.warn(`⚠ ${id} : aucune entrée dans la table — titre inchangé`);
    continue;
  }
  const p = path.join(BOOKS_DIR, f);
  const book = JSON.parse(fs.readFileSync(p, "utf8"));
  book.titleFr = entry.titleFr;
  if (entry.titleAr) book.titleAr = entry.titleAr;
  fs.writeFileSync(p, JSON.stringify(book, null, 1) + "\n");
  filesFixed++;
}

// Manifeste : titleFr + textbookAr (source du fil d'Ariane du lecteur)
const manifest = JSON.parse(fs.readFileSync(MANIFEST, "utf8"));
let manifestFixed = 0;
for (const b of manifest.books) {
  const entry = map.get(b.id);
  if (!entry) continue;
  b.titleFr = entry.titleFr;
  if (entry.titleAr) b.textbookAr = entry.titleAr;
  manifestFixed++;
}
fs.writeFileSync(MANIFEST, JSON.stringify(manifest, null, 2) + "\n");

console.log(`\n✅ ${filesFixed} fichiers de livres mis à jour, ${manifestFixed} entrées du manifeste.`);
const missing = files.filter((f) => f.endsWith(".json") && !map.has(f.replace(/\.json$/, "")));
if (missing.length) console.log("⚠ Sans entrée :", missing.join(", "));

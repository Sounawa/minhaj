/**
 * Minhāj R9 — Fusion du doublon Tafsīr al-Jalālayn ( année 4 primaire ) :
 * « tafsir-1ep » (57 leçons réelles, titres « للسنة الرابعة ») et « tafsir-4ep »
 * (6 pages d'apparat du même livre, docIds 12016-12302-13621-13622) sont UN seul
 * manuel : la 4ᵉ année primaire (le tafsīr commence en 4ᵉ année, comme le fiqh
 * et le ḥadīth — constat R8).
 *
 * Fusion : id conservé « tafsir-1ep » (stabilité des routes), level corrigé → 4ep,
 * intro = 12016 (présentation du livre), annexes 13621/13622 conservées en fin de
 * sommaire, pages-guide 12017/12018/12302 écartées (convention R8).
 * Usage: bun run scripts-recovery/r9-merge-tafsir.ts
 */
import { readFileSync, writeFileSync, unlinkSync } from "fs";
import path from "path";

const BOOKS = path.join(process.cwd(), "content", "books");
const keep = JSON.parse(readFileSync(path.join(BOOKS, "tafsir-1ep.json"), "utf8"));
const stub = JSON.parse(readFileSync(path.join(BOOKS, "tafsir-4ep.json"), "utf8"));

// 1. Niveau corrigé
keep.level = "4ep";
keep.levelAr = "السنة الرابعة من السلك الابتدائي العتيق";

// 2. Intro = 12016 (depuis le stub)
keep.intro = stub.intro;

// 3. Annexes du stub conservées en fin de sommaire
const annexes = (stub.lessons || []).filter((l: any) => ["13621", "13622"].includes(String(l.docId)));
keep.lessons = [...(keep.lessons || []), ...annexes];

// 4. Écriture + suppression du doublon
writeFileSync(path.join(BOOKS, "tafsir-1ep.json"), JSON.stringify(keep, null, 1) + "\n");
unlinkSync(path.join(BOOKS, "tafsir-4ep.json"));
console.log(`tafsir-1ep ← fusion : level 4ep, intro 12016, +${annexes.length} annexes ; tafsir-4ep supprimé`);
console.log(`Total leçons : ${keep.lessons.length}`);

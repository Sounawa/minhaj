import ZAI from 'z-ai-web-dev-sdk';

async function main() {
  const zai = await ZAI.create();
  const queries = [
    // 1. Matn : abrīdū bi-l-ṣalāt (Bukhārī)
    "sunnah.com بخاري \"أبردوا بالصلاة فإن شدة الحر من فيح جهنم\" رقم الحديث",
    "\"أبردوا بالصلاة\" \"من فيح جهنم\" صحيح البخاري كتاب مواقيت الصلاة باب الإبراد بالظهر",
    // 2. Muwaṭṭaʾ : idhā shtadda al-ḥarr
    "موطأ مالك \"إذا اشتد الحر فأبردوا عن الصلاة\" باب النهي عن الصلاة بالهاجرة",
    // 3. ʿĀʾisha : mutalaffiʿāt bi-murūṭihinna
    "sunnah.com بخاري عائشة \"متلفعات بمروطهن\" \"ما يعرفن من الغلس\" باب سرعة انصراف النساء من الصبح رقم",
    // 4. Abū Barza : yakrahu al-nawm qabl al-ʿishāʾ
    "sunnah.com بخاري أبو برزة \"كان يكره النوم قبلها والحديث بعدها\" باب ما يكره من السمر بعد العشاء رقم",
  ];
  for (const q of queries) {
    try {
      const r = await zai.functions.invoke("web_search", { query: q, num: 5 });
      console.log("\n=== QUERY:", q.slice(0, 90));
      for (const item of (r as any).results || []) {
        console.log("-", (item.name || "").slice(0, 110));
        console.log(" ", (item.url || ""));
        console.log(" ", (item.snippet || "").replace(/\n/g, " ").slice(0, 350));
      }
    } catch (e) { console.log("ERR", (e as Error).message); }
  }
}
main();

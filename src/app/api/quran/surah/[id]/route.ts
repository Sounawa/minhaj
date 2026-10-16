import { NextRequest, NextResponse } from "next/server";

export const runtime = "nodejs";
export const maxDuration = 60;

/** Cache mémoire des sourates (évite de rappeler l'API à chaque fois) */
const cache = new Map<number, { data: unknown; at: number }>();
const TTL = 1000 * 60 * 30; // 30 min

type Ctx = { params: Promise<{ id: string }> };

export async function GET(_req: NextRequest, ctx: Ctx) {
  try {
    const { id } = await ctx.params;
    const n = parseInt(id, 10);
    if (!Number.isInteger(n) || n < 1 || n > 114) {
      return NextResponse.json({ error: "Numéro de sourate invalide (1–114)" }, { status: 400 });
    }

    const hit = cache.get(n);
    if (hit && Date.now() - hit.at < TTL) {
      return NextResponse.json(hit.data);
    }

    const res = await fetch(
      `https://api.alquran.cloud/v1/surah/${n}/editions/quran-uthmani,fr.hamidullah`,
      { headers: { "User-Agent": "minhaj-app/1.0" }, cache: "no-store" }
    );
    if (!res.ok) {
      return NextResponse.json(
        { error: "Impossible de charger la sourate. Réessayez." },
        { status: 502 }
      );
    }
    const json = await res.json();
    const arabic = json.data[0];
    const french = json.data[1];

    const ayahs = arabic.ayahs.map(
      (
        a: { number: number; numberInSurah: number; text: string; page: number },
        i: { number: number; numberInSurah: number; text: string; page: number }
      ) => ({
        number: a.number, // numéro global (pour l'audio)
        numberInSurah: a.numberInSurah,
        textAr: a.text,
        textFr: french.ayahs[i.numberInSurah - 1]?.text ?? "",
        page: a.page,
        // Audio par verset : https://cdn.islamic.network/quran/audio/128/{reciter}/{number}.mp3
        audio: `/api/quran/audio?n=${a.number}&r=${_req.nextUrl.searchParams.get("r") || "ar.alafasy"}`,
      })
    );

    const payload = {
      surah: {
        number: arabic.number,
        nameAr: arabic.name,
        nameFr: french.name,
        nameEn: arabic.englishName,
        ayahs: arabic.numberOfAyahs,
        revelation: arabic.revelationType === "Meccan" ? "makkah" : "medina",
      },
      // Audio de la sourate complète
      audioSurah: `/api/quran/audio-surah?n=${n}&r=${_req.nextUrl.searchParams.get("r") || "ar.alafasy"}`,
      ayahs,
    };

    cache.set(n, { data: payload, at: Date.now() });
    return NextResponse.json(payload);
  } catch (err) {
    console.error("[quran/surah] error:", err);
    return NextResponse.json({ error: "Erreur de chargement du Coran." }, { status: 500 });
  }
}

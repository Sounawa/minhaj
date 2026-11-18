import { NextRequest, NextResponse } from "next/server";

export const runtime = "nodejs";

/** Proxy audio sourate complète : GET /api/quran/audio-surah?n=1&r=ar.alafasy */
export async function GET(req: NextRequest) {
  const n = parseInt(req.nextUrl.searchParams.get("n") || "", 10);
  const r = req.nextUrl.searchParams.get("r") || "ar.alafasy";
  if (!Number.isInteger(n) || n < 1 || n > 114) {
    return NextResponse.json({ error: "Numéro de sourate invalide" }, { status: 400 });
  }
  if (!/^ar\.[a-z]+$/.test(r)) {
    return NextResponse.json({ error: "Récitateur invalide" }, { status: 400 });
  }
  const upstream = `https://cdn.islamic.network/quran/audio-surah/128/${r}/${n}.mp3`;
  try {
    const res = await fetch(upstream, { cache: "force-cache" });
    if (!res.ok) {
      return NextResponse.json({ error: "Audio indisponible" }, { status: 502 });
    }
    const buf = await res.arrayBuffer();
    return new NextResponse(buf, {
      headers: {
        "Content-Type": "audio/mpeg",
        "Cache-Control": "public, max-age=86400",
      },
    });
  } catch {
    return NextResponse.json({ error: "Audio indisponible" }, { status: 502 });
  }
}

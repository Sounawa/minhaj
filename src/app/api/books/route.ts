import { NextResponse } from "next/server";
import { getLibrary } from "@/lib/minhaj";

export const dynamic = "force-dynamic";

export async function GET() {
  try {
    const library = await getLibrary();
    return NextResponse.json(library, {
      headers: { "Cache-Control": "no-store" },
    });
  } catch (e) {
    return NextResponse.json(
      { error: "library_unavailable", message: e instanceof Error ? e.message : String(e) },
      { status: 503 }
    );
  }
}

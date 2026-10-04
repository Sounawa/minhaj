import { NextResponse } from "next/server";
import { getDoc } from "@/lib/minhaj";

export const dynamic = "force-dynamic";

export async function GET(
  _req: Request,
  { params }: { params: Promise<{ bookId: string; docId: string }> }
) {
  const { bookId, docId } = await params;
  try {
    const doc = await getDoc(bookId, docId);
    if (!doc) {
      return NextResponse.json(
        { error: "not_found", message: `Document ${docId} introuvable dans le manuel ${bookId}.` },
        { status: 404 }
      );
    }
    return NextResponse.json(doc, { headers: { "Cache-Control": "no-store" } });
  } catch (e) {
    return NextResponse.json(
      { error: "doc_unavailable", message: e instanceof Error ? e.message : String(e) },
      { status: 503 }
    );
  }
}

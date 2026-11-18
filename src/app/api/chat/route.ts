import { NextRequest, NextResponse } from "next/server";
import ZAI from "z-ai-web-dev-sdk";
import { db } from "@/lib/db";
import { PERSONAS, isValidPersona } from "@/lib/personas";

export const runtime = "nodejs";
export const maxDuration = 120;

export async function POST(req: NextRequest) {
  try {
    const body = await req.json();
    const { conversationId, message, persona } = body as {
      conversationId?: string;
      message?: string;
      persona?: string;
    };

    if (!message?.trim()) {
      return NextResponse.json({ error: "Message is required" }, { status: 400 });
    }

    const personaKey = persona && isValidPersona(persona) ? persona : "general";
    const systemPrompt = PERSONAS[personaKey].system;

    // Find or create conversation
    let conversation = conversationId
      ? await db.conversation.findUnique({ where: { id: conversationId } })
      : null;

    if (!conversation) {
      conversation = await db.conversation.create({
        data: {
          title: message.trim().slice(0, 48) + (message.trim().length > 48 ? "…" : ""),
          persona: personaKey,
        },
      });
    }

    // Save user message
    await db.message.create({
      data: {
        role: "user",
        content: message.trim(),
        conversationId: conversation.id,
      },
    });

    // Build history for the LLM
    const history = await db.message.findMany({
      where: { conversationId: conversation.id },
      orderBy: { createdAt: "asc" },
      take: 24, // keep context manageable
    });

    const llmMessages = [
      { role: "system" as const, content: systemPrompt },
      ...history.map((m) => ({
        role: m.role === "assistant" ? ("assistant" as const) : ("user" as const),
        content: m.content,
      })),
    ];

    const zai = await ZAI.create();
    const completion = await zai.chat.completions.create({
      messages: llmMessages,
      thinking: { type: "disabled" },
    });

    const reply: string | undefined = completion?.choices?.[0]?.message?.content;
    if (!reply) {
      return NextResponse.json(
        { error: "The model returned an empty response. Please try again." },
        { status: 502 }
      );
    }

    // Save assistant reply
    const savedReply = await db.message.create({
      data: {
        role: "assistant",
        content: reply,
        conversationId: conversation.id,
      },
    });

    await db.conversation.update({
      where: { id: conversation.id },
      data: { persona: personaKey },
    });

    return NextResponse.json({
      conversationId: conversation.id,
      reply,
      replyId: savedReply.id,
    });
  } catch (err) {
    console.error("[chat] error:", err);
    return NextResponse.json(
      { error: "Chat failed. The AI service may be busy — please retry." },
      { status: 500 }
    );
  }
}

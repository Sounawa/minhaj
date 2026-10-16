"use client";

import { useCallback, useEffect, useRef, useState } from "react";
import {
  Send,
  Plus,
  Trash2,
  Loader2,
  Bot,
  User,
  MessageSquareDashed,
  ChevronDown,
} from "lucide-react";
import { toast } from "sonner";
import { Button } from "@/components/ui/button";
import { Textarea } from "@/components/ui/textarea";
import { Badge } from "@/components/ui/badge";
import { ScrollArea } from "@/components/ui/scroll-area";
import {
  DropdownMenu,
  DropdownMenuContent,
  DropdownMenuItem,
  DropdownMenuLabel,
  DropdownMenuSeparator,
  DropdownMenuTrigger,
} from "@/components/ui/dropdown-menu";
import { cn, timeAgo } from "@/lib/utils";
import { renderMarkdown } from "@/lib/markdown";
import { PERSONAS, type PersonaKey } from "@/lib/personas";

interface Msg {
  id: string;
  role: string;
  content: string;
  createdAt: string;
}

interface Conversation {
  id: string;
  title: string;
  persona: string;
  updatedAt: string;
  _count?: { messages: number };
  messages?: Msg[];
}

const SUGGESTIONS = [
  "Explain how neural networks learn — simply, with an analogy.",
  "Write a haiku about a rainy city evening.",
  "Give me 5 catchy names for an eco-friendly coffee brand.",
  "What are the biggest web-dev trends this year?",
];

export default function ChatPanel() {
  const [conversations, setConversations] = useState<Conversation[]>([]);
  const [activeId, setActiveId] = useState<string | null>(null);
  const [messages, setMessages] = useState<Msg[]>([]);
  const [persona, setPersona] = useState<PersonaKey>("general");
  const [input, setInput] = useState("");
  const [sending, setSending] = useState(false);
  const [loadingConv, setLoadingConv] = useState(true);
  const [mobileListOpen, setMobileListOpen] = useState(false);
  const scrollRef = useRef<HTMLDivElement>(null);
  const tmpIdRef = useRef(0);

  // Load conversation list
  useEffect(() => {
    let cancelled = false;
    (async () => {
      try {
        const res = await fetch("/api/conversations");
        const data = await res.json();
        if (!cancelled) setConversations(data.conversations || []);
      } catch {
        /* non-fatal */
      } finally {
        if (!cancelled) setLoadingConv(false);
      }
    })();
    return () => {
      cancelled = true;
    };
  }, []);

  // Auto scroll to bottom on new messages
  useEffect(() => {
    scrollRef.current?.scrollTo({ top: scrollRef.current.scrollHeight, behavior: "smooth" });
  }, [messages, sending]);

  const openConversation = useCallback(async (id: string) => {
    setActiveId(id);
    setMobileListOpen(false);
    try {
      const res = await fetch(`/api/conversations/${id}`);
      const data = await res.json();
      if (data.conversation) {
        setMessages(data.conversation.messages || []);
        setPersona((data.conversation.persona as PersonaKey) || "general");
      }
    } catch {
      toast.error("Failed to open conversation");
    }
  }, []);

  const newChat = () => {
    setActiveId(null);
    setMessages([]);
    setMobileListOpen(false);
  };

  const deleteConversation = async (e: React.MouseEvent, id: string) => {
    e.stopPropagation();
    try {
      await fetch(`/api/conversations/${id}`, { method: "DELETE" });
      setConversations((prev) => prev.filter((c) => c.id !== id));
      if (activeId === id) newChat();
      toast.success("Conversation deleted");
    } catch {
      toast.error("Delete failed");
    }
  };

  const send = async (text?: string) => {
    const content = (text ?? input).trim();
    if (!content || sending) return;

    setInput("");
    setSending(true);
    const tmpId = `tmp-u-${++tmpIdRef.current}`;
    const optimisticUser: Msg = {
      id: tmpId,
      role: "user",
      content,
      createdAt: new Date().toISOString(),
    };
    setMessages((prev) => [...prev, optimisticUser]);

    try {
      const res = await fetch("/api/chat", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ conversationId: activeId, message: content, persona }),
      });
      const data = await res.json();
      if (!res.ok) throw new Error(data.error || "Chat failed");

      setMessages((prev) => [
        ...prev,
        {
          id: data.replyId,
          role: "assistant",
          content: data.reply,
          createdAt: new Date().toISOString(),
        },
      ]);
      setActiveId(data.conversationId);

      // Refresh conversation list quietly
      fetch("/api/conversations")
        .then((r) => r.json())
        .then((d) => setConversations(d.conversations || []))
        .catch(() => {});
    } catch (err) {
      toast.error(err instanceof Error ? err.message : "Chat failed");
      setMessages((prev) => prev.filter((m) => m.id !== optimisticUser.id));
    } finally {
      setSending(false);
    }
  };

  const activePersona = PERSONAS[persona];

  return (
    <div className="grid gap-4 lg:grid-cols-[260px_1fr]">
      {/* ── Conversation sidebar ── */}
      <div
        className={cn(
          "rounded-xl border bg-card lg:sticky lg:top-[8.5rem] lg:block lg:h-[calc(100vh-13rem)]",
          mobileListOpen ? "block" : "hidden"
        )}
      >
        <div className="flex items-center justify-between border-b px-3 py-2.5">
          <p className="text-xs font-semibold uppercase tracking-wider text-muted-foreground">
            History
          </p>
          <Button variant="ghost" size="sm" onClick={newChat}>
            <Plus className="size-4" /> New
          </Button>
        </div>
        <ScrollArea className="h-[calc(100%-3rem)] lg:h-[calc(100%-3.2rem)]">
          <div className="max-h-72 p-2 lg:max-h-none">
            {loadingConv ? (
              <div className="space-y-2 p-1">
                {Array.from({ length: 4 }).map((_, i) => (
                  <div key={i} className="h-12 animate-pulse rounded-lg bg-muted" />
                ))}
              </div>
            ) : conversations.length === 0 ? (
              <p className="px-3 py-6 text-center text-xs text-muted-foreground">
                No conversations yet. Say hello! 👋
              </p>
            ) : (
              conversations.map((c) => (
                <button
                  key={c.id}
                  onClick={() => openConversation(c.id)}
                  className={cn(
                    "group mb-1 flex w-full items-center gap-2 rounded-lg px-2.5 py-2 text-left text-sm transition-colors",
                    activeId === c.id
                      ? "bg-primary/10 text-primary"
                      : "hover:bg-accent/50"
                  )}
                >
                  <MessageSquareDashed className="size-4 shrink-0 opacity-60" />
                  <span className="min-w-0 flex-1">
                    <span className="block truncate font-medium">{c.title}</span>
                    <span className="block text-[11px] text-muted-foreground">
                      {c._count?.messages ?? 0} msgs · {timeAgo(c.updatedAt)}
                    </span>
                  </span>
                  <span
                    role="button"
                    tabIndex={0}
                    aria-label="Delete conversation"
                    onClick={(e) => deleteConversation(e, c.id)}
                    onKeyDown={(e) => e.key === "Enter" && deleteConversation(e, c.id)}
                    className="opacity-0 transition-opacity hover:text-destructive group-hover:opacity-100"
                  >
                    <Trash2 className="size-4" />
                  </span>
                </button>
              ))
            )}
          </div>
        </ScrollArea>
      </div>

      {/* ── Chat area ── */}
      <div className="flex min-h-[560px] flex-col overflow-hidden rounded-xl border bg-card lg:h-[calc(100vh-13rem)]">
        {/* Toolbar */}
        <div className="flex items-center gap-2 border-b px-3 py-2.5">
          <Button
            variant="outline"
            size="sm"
            className="lg:hidden"
            onClick={() => setMobileListOpen((v) => !v)}
          >
            History <ChevronDown className="size-3.5" />
          </Button>

          <DropdownMenu>
            <DropdownMenuTrigger asChild>
              <Button variant="outline" size="sm" className="gap-2">
                <span>{activePersona.emoji}</span>
                {activePersona.label}
                <ChevronDown className="size-3.5 opacity-60" />
              </Button>
            </DropdownMenuTrigger>
            <DropdownMenuContent align="start" className="w-64">
              <DropdownMenuLabel>Choose a persona</DropdownMenuLabel>
              <DropdownMenuSeparator />
              {(Object.keys(PERSONAS) as PersonaKey[]).map((key) => (
                <DropdownMenuItem key={key} onClick={() => setPersona(key)}>
                  <span className="text-base leading-none">{PERSONAS[key].emoji}</span>
                  <div className="flex flex-col">
                    <span className="font-medium">{PERSONAS[key].label}</span>
                    <span className="text-[11px] text-muted-foreground">
                      {PERSONAS[key].description}
                    </span>
                  </div>
                </DropdownMenuItem>
              ))}
            </DropdownMenuContent>
          </DropdownMenu>

          <Badge variant="secondary" className="hidden sm:inline-flex">
            {messages.length} messages
          </Badge>

          <div className="ml-auto">
            <Button variant="ghost" size="sm" onClick={newChat}>
              <Plus className="size-4" />
              <span className="hidden sm:inline">New chat</span>
            </Button>
          </div>
        </div>

        {/* Messages */}
        <div ref={scrollRef} className="min-h-0 flex-1 overflow-y-auto">
          {messages.length === 0 && !sending ? (
            <div className="flex h-full flex-col items-center justify-center gap-4 px-6 py-10">
              <div className="flex size-14 items-center justify-center rounded-2xl bg-primary/10 text-primary">
                <Bot className="size-7" />
              </div>
              <div className="text-center">
                <p className="font-semibold">Ask me anything</p>
                <p className="mt-1 max-w-sm text-sm text-muted-foreground">
                  You are chatting with the <b>{activePersona.label}</b> persona. History is
                  saved automatically.
                </p>
              </div>
              <div className="grid w-full max-w-lg gap-2 sm:grid-cols-2">
                {SUGGESTIONS.map((s) => (
                  <button
                    key={s}
                    onClick={() => send(s)}
                    className="rounded-lg border bg-muted/40 px-3 py-2.5 text-left text-xs leading-snug text-muted-foreground transition-colors hover:border-primary/40 hover:bg-accent/40 hover:text-foreground"
                  >
                    {s}
                  </button>
                ))}
              </div>
            </div>
          ) : (
            <div className="mx-auto max-w-3xl space-y-4 p-4 sm:p-5">
              {messages.map((m) => (
                <MessageBubble key={m.id} msg={m} />
              ))}
              {sending && (
                <div className="flex gap-3">
                  <div className="flex size-8 shrink-0 items-center justify-center rounded-full bg-primary text-primary-foreground">
                    <Bot className="size-4.5" />
                  </div>
                  <div className="flex items-center gap-1.5 rounded-2xl rounded-tl-sm border bg-muted/50 px-4 py-3">
                    <span className="typing-dot" />
                    <span className="typing-dot" />
                    <span className="typing-dot" />
                  </div>
                </div>
              )}
            </div>
          )}
        </div>

        {/* Composer */}
        <div className="border-t bg-card p-3">
          <div className="mx-auto flex max-w-3xl items-end gap-2">
            <Textarea
              value={input}
              onChange={(e) => setInput(e.target.value)}
              onKeyDown={(e) => {
                if (e.key === "Enter" && !e.shiftKey) {
                  e.preventDefault();
                  send();
                }
              }}
              placeholder={`Message the ${activePersona.label}… (Enter to send, Shift+Enter for newline)`}
              rows={1}
              className="max-h-40 min-h-11 resize-none"
              disabled={sending}
              aria-label="Chat message"
            />
            <Button
              size="icon"
              className="size-11 shrink-0"
              onClick={() => send()}
              disabled={sending || !input.trim()}
              aria-label="Send message"
            >
              {sending ? <Loader2 className="size-4.5 animate-spin" /> : <Send className="size-4.5" />}
            </Button>
          </div>
          <p className="mx-auto mt-2 max-w-3xl text-center text-[11px] text-muted-foreground">
            AI can make mistakes — verify important information.
          </p>
        </div>
      </div>
    </div>
  );
}

function MessageBubble({ msg }: { msg: Msg }) {
  const isUser = msg.role === "user";
  return (
    <div className={cn("flex gap-3", isUser && "flex-row-reverse")}>
      <div
        className={cn(
          "flex size-8 shrink-0 items-center justify-center rounded-full",
          isUser
            ? "bg-secondary text-secondary-foreground"
            : "bg-primary text-primary-foreground"
        )}
      >
        {isUser ? <User className="size-4" /> : <Bot className="size-4.5" />}
      </div>
      <div
        className={cn(
          "max-w-[85%] rounded-2xl px-4 py-2.5 text-sm shadow-sm sm:max-w-[78%]",
          isUser
            ? "rounded-tr-sm bg-primary text-primary-foreground"
            : "rounded-tl-sm border bg-muted/40"
        )}
      >
        {isUser ? (
          <p className="whitespace-pre-wrap break-words leading-relaxed">{msg.content}</p>
        ) : (
          <div
            className="msg-content break-words"
            dangerouslySetInnerHTML={{ __html: renderMarkdown(msg.content) }}
          />
        )}
      </div>
    </div>
  );
}

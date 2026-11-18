"use client";

import { useCallback, useEffect, useRef, useState } from "react";
import {
  Bot,
  ChevronDown,
  Loader2,
  MessageSquarePlus,
  RotateCcw,
  Send,
  Sparkles,
  Trash2,
  User,
} from "lucide-react";
import { toast } from "sonner";
import { Button } from "@/components/ui/button";
import {
  Dialog,
  DialogContent,
  DialogDescription,
  DialogHeader,
  DialogTitle,
} from "@/components/ui/dialog";
import {
  DropdownMenu,
  DropdownMenuContent,
  DropdownMenuItem,
  DropdownMenuLabel,
  DropdownMenuSeparator,
  DropdownMenuTrigger,
} from "@/components/ui/dropdown-menu";
import { ScrollArea } from "@/components/ui/scroll-area";
import { Textarea } from "@/components/ui/textarea";
import { renderMarkdown } from "@/lib/markdown";
import { PERSONAS, type PersonaKey } from "@/lib/personas";
import { cn } from "@/lib/utils";

interface Msg {
  id: string;
  role: string;
  content: string;
}

const SUGGESTIONS_FR: Array<{ persona: PersonaKey; text: string }> = [
  {
    persona: "assistant",
    text: "Explique la différence entre farḍ (part fixe) et taʿṣīb (résidu) dans l'héritage.",
  },
  {
    persona: "quran",
    text: "Quel est le contexte de révélation du verset du Trône (āyat al-kursī) ?",
  },
  {
    persona: "arabic",
    text: "Conjugue le verbe كَتَبَ (écrire) à l'accompli, avec translittération.",
  },
  {
    persona: "assistant",
    text: "Quelles sont les conditions de validité des ablutions (wuḍūʾ) ?",
  },
];

export function AssistantDialog({
  open,
  onOpenChange,
}: {
  open: boolean;
  onOpenChange: (v: boolean) => void;
}) {
  const [persona, setPersona] = useState<PersonaKey>("assistant");
  const [messages, setMessages] = useState<Msg[]>([]);
  const [conversationId, setConversationId] = useState<string | null>(null);
  const [conversationTitle, setConversationTitle] = useState<string | null>(null);
  const [input, setInput] = useState("");
  const [sending, setSending] = useState(false);
  const [loadingHistory, setLoadingHistory] = useState(false);
  const scrollRef = useRef<HTMLDivElement>(null);
  const tmpIdRef = useRef(0);
  const lastFetchedRef = useRef<string | null>(null);

  const activePersona = PERSONAS[persona];

  const scrollToEnd = useCallback(() => {
    requestAnimationFrame(() => {
      scrollRef.current?.scrollTo({ top: scrollRef.current.scrollHeight, behavior: "smooth" });
    });
  }, []);

  // Reprise de la dernière conversation à l'ouverture (une seule fois par ouverture).
  useEffect(() => {
    if (!open || conversationId || messages.length > 0 || loadingHistory) return;
    if (lastFetchedRef.current === "done") return;
    lastFetchedRef.current = "done";
    let cancelled = false;
    (async () => {
      try {
        const res = await fetch("/api/conversations");
        const data = await res.json();
        const convs = (data.conversations || []) as Array<{
          id: string;
          title: string;
          persona: string;
          updatedAt: string;
        }>;
        if (cancelled || convs.length === 0) return;
        const last = convs[0];
        const detail = await fetch(`/api/conversations/${last.id}`);
        if (!detail.ok) return;
        const d = await detail.json();
        if (cancelled || !d.conversation) return;
        setConversationId(last.id);
        setConversationTitle(last.title);
        if (last.persona && last.persona in PERSONAS) setPersona(last.persona as PersonaKey);
        setMessages(
          (d.conversation.messages || []).map(
            (m: { id: string; role: string; content: string }) => ({
              id: m.id,
              role: m.role,
              content: m.content,
            }),
          ),
        );
      } catch {
        /* non-fatal : l'historique est optionnel */
      }
    })();
    return () => {
      cancelled = true;
    };
  }, [open, conversationId, messages.length, loadingHistory]);

  // Reset du garde-fou quand le dialogue se referme.
  useEffect(() => {
    if (!open) lastFetchedRef.current = null;
  }, [open]);

  useEffect(() => {
    scrollToEnd();
  }, [messages.length, sending, scrollToEnd]);

  const send = useCallback(
    async (raw?: string, personaOverride?: PersonaKey) => {
      const text = (raw ?? input).trim();
      if (!text || sending) return;
      const usePersona = personaOverride ?? persona;
      setInput("");
      setSending(true);
      const tmpId = `tmp-${++tmpIdRef.current}`;
      setMessages((prev) => [...prev, { id: tmpId, role: "user", content: text }]);
      try {
        const res = await fetch("/api/chat", {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({ message: text, persona: usePersona, conversationId }),
        });
        const data = await res.json();
        if (!res.ok || !data.reply) {
          throw new Error(data.error || "Réponse indisponible");
        }
        setConversationId(data.conversationId ?? conversationId);
        setConversationTitle(text.slice(0, 48));
        setMessages((prev) => [
          ...prev,
          { id: data.replyId ?? `a-${Date.now()}`, role: "assistant", content: data.reply },
        ]);
      } catch (err) {
        toast.error("L'assistant est indisponible — réessayez dans un instant.", {
          description: err instanceof Error ? err.message : undefined,
        });
        setMessages((prev) => prev.filter((m) => m.id !== tmpId));
        setInput(text);
      } finally {
        setSending(false);
      }
    },
    [input, sending, persona, conversationId],
  );

  const newChat = useCallback(() => {
    setMessages([]);
    setConversationId(null);
    setConversationTitle(null);
    setInput("");
  }, []);

  const deleteConversation = useCallback(async () => {
    if (!conversationId) return newChat();
    try {
      await fetch(`/api/conversations/${conversationId}`, { method: "DELETE" });
      toast.success("Conversation supprimée.");
    } catch {
      /* la conversation locale est nettoyée dans tous les cas */
    }
    newChat();
  }, [conversationId, newChat]);

  return (
    <Dialog open={open} onOpenChange={onOpenChange}>
      <DialogContent className="flex max-h-[88dvh] w-[calc(100vw-2rem)] max-w-2xl flex-col gap-0 overflow-hidden p-0 sm:w-[36rem]">
        <DialogHeader className="border-b border-amber-800/15 px-4 py-3 sm:px-5">
          <div className="flex items-center gap-2.5 pr-8">
            <span className="flex size-9 shrink-0 items-center justify-center rounded-xl bg-primary/10 text-primary">
              <Bot className="size-5" aria-hidden="true" />
            </span>
            <div className="min-w-0 flex-1">
              <DialogTitle className="flex items-center gap-2 font-serif text-base leading-tight">
                Assistant IA
                <span className="rounded-full border border-amber-800/20 bg-amber-100/60 px-2 py-0.5 text-[10px] font-medium uppercase tracking-wider text-amber-800 dark:bg-amber-900/40 dark:text-amber-100">
                  beta
                </span>
              </DialogTitle>
              <DialogDescription className="mt-0.5 truncate text-xs">
                {conversationTitle
                  ? conversationTitle
                  : "Posez vos questions sur le corpus, le Coran, l'arabe…"}
              </DialogDescription>
            </div>
          </div>
          <div className="mt-2.5 flex flex-wrap items-center gap-2">
            <DropdownMenu>
              <DropdownMenuTrigger asChild>
                <Button variant="outline" size="sm" className="h-8 gap-2 border-amber-800/20">
                  <span aria-hidden="true">{activePersona.emoji}</span>
                  <span className="max-w-36 truncate">{activePersona.label}</span>
                  <ChevronDown className="size-3.5 opacity-60" aria-hidden="true" />
                </Button>
              </DropdownMenuTrigger>
              <DropdownMenuContent align="start" className="w-64">
                <DropdownMenuLabel>Choisir un assistant</DropdownMenuLabel>
                <DropdownMenuSeparator />
                {(Object.keys(PERSONAS) as PersonaKey[]).map((key) => (
                  <DropdownMenuItem
                    key={key}
                    onClick={() => setPersona(key)}
                    aria-current={key === persona ? "true" : undefined}
                    className={cn(key === persona && "bg-amber-100/60 dark:bg-amber-900/30")}
                  >
                    <span className="text-base leading-none" aria-hidden="true">
                      {PERSONAS[key].emoji}
                    </span>
                    <div className="flex min-w-0 flex-col">
                      <span className="font-medium">{PERSONAS[key].label}</span>
                      <span className="text-[11px] text-muted-foreground">
                        {PERSONAS[key].description}
                      </span>
                    </div>
                  </DropdownMenuItem>
                ))}
              </DropdownMenuContent>
            </DropdownMenu>
            <div className="ms-auto flex items-center gap-1.5">
              <Button
                variant="ghost"
                size="sm"
                className="h-8 gap-1.5 px-2.5"
                onClick={newChat}
                aria-label="Nouvelle conversation"
              >
                <MessageSquarePlus className="size-4" aria-hidden="true" />
                <span className="hidden sm:inline">Nouvelle</span>
              </Button>
              {conversationId && (
                <Button
                  variant="ghost"
                  size="sm"
                  className="h-8 gap-1.5 px-2.5 text-destructive hover:text-destructive"
                  onClick={deleteConversation}
                  aria-label="Supprimer la conversation"
                >
                  <Trash2 className="size-4" aria-hidden="true" />
                  <span className="hidden sm:inline">Supprimer</span>
                </Button>
              )}
            </div>
          </div>
        </DialogHeader>

        {/* ── Fil de messages ── */}
        <ScrollArea className="min-h-0 flex-1" style={{ height: "min(56dvh, 30rem)" }}>
          <div ref={scrollRef} className="px-4 py-4 sm:px-5">
            {messages.length === 0 && !sending && !loadingHistory ? (
              <div className="flex flex-col items-center gap-4 py-6 text-center">
                <div className="flex size-14 items-center justify-center rounded-2xl bg-primary/10 text-primary">
                  <Sparkles className="size-7" aria-hidden="true" />
                </div>
                <div>
                  <p className="font-serif text-lg font-semibold">Bienvenue</p>
                  <p className="mx-auto mt-1 max-w-sm text-sm text-muted-foreground">
                    Discutez avec l&apos;
                    <strong>{activePersona.label}</strong>
                    {" — "}
                    {activePersona.description.toLowerCase()}.
                  </p>
                </div>
                <div className="grid w-full max-w-md gap-2 sm:grid-cols-2">
                  {SUGGESTIONS_FR.map((s) => (
                    <button
                      key={s.text}
                      type="button"
                      onClick={() => {
                        setPersona(s.persona);
                        void send(s.text, s.persona);
                      }}
                      className="rounded-lg border border-amber-800/15 bg-amber-50/50 px-3 py-2.5 text-left text-xs leading-snug text-muted-foreground transition-colors hover:border-amber-800/35 hover:bg-amber-100/60 hover:text-foreground dark:bg-amber-950/20 dark:hover:bg-amber-900/30"
                    >
                      {s.text}
                    </button>
                  ))}
                </div>
                <p className="max-w-sm text-[11px] leading-relaxed text-muted-foreground/80">
                  L&apos;assistant reste faillible : vérifiez toujours les citations dans le corpus
                  ou auprès d&apos;un enseignant. Les réponses ne remplacent pas la consultation
                  d&apos;un savant.
                </p>
              </div>
            ) : (
              <div className="space-y-4">
                {messages.map((m) => (
                  <div key={m.id} className="flex gap-2.5 sm:gap-3">
                    <span
                      className={cn(
                        "flex size-7 shrink-0 items-center justify-center rounded-full",
                        m.role === "assistant"
                          ? "bg-primary text-primary-foreground"
                          : "bg-muted text-muted-foreground",
                      )}
                      aria-hidden="true"
                    >
                      {m.role === "assistant" ? (
                        <Bot className="size-3.5" />
                      ) : (
                        <User className="size-3.5" />
                      )}
                    </span>
                    <div
                      className={cn(
                        "min-w-0 flex-1 rounded-2xl border px-3.5 py-2.5 text-sm leading-relaxed",
                        m.role === "assistant"
                          ? "rounded-tl-sm border-amber-800/15 bg-card"
                          : "rounded-tr-sm border-amber-800/10 bg-amber-50/60 dark:bg-amber-950/25",
                      )}
                    >
                      {m.role === "assistant" ? (
                        <div
                          className="md-chat"
                          dangerouslySetInnerHTML={{ __html: renderMarkdown(m.content) }}
                        />
                      ) : (
                        <p className="whitespace-pre-wrap">{m.content}</p>
                      )}
                    </div>
                  </div>
                ))}
                {sending && (
                  <div className="flex gap-2.5 sm:gap-3">
                    <span
                      className="flex size-7 shrink-0 items-center justify-center rounded-full bg-primary text-primary-foreground"
                      aria-hidden="true"
                    >
                      <Bot className="size-3.5" />
                    </span>
                    <div
                      className="flex items-center gap-1.5 rounded-2xl rounded-tl-sm border border-amber-800/15 bg-card px-4 py-3"
                      role="status"
                      aria-label="L'assistant rédige une réponse"
                    >
                      <span className="typing-dot" />
                      <span className="typing-dot" />
                      <span className="typing-dot" />
                    </div>
                  </div>
                )}
              </div>
            )}
          </div>
        </ScrollArea>

        {/* ── Composer ── */}
        <div className="border-t border-amber-800/15 bg-card p-3 sm:p-4">
          <div className="flex items-end gap-2">
            <Textarea
              value={input}
              onChange={(e) => setInput(e.target.value)}
              onKeyDown={(e) => {
                if (e.key === "Enter" && !e.shiftKey) {
                  e.preventDefault();
                  void send();
                }
              }}
              placeholder={`Écrire à ${activePersona.label}… (Entrée pour envoyer)`}
              rows={1}
              className="max-h-36 min-h-11 resize-none border-amber-800/20"
              disabled={sending}
              aria-label="Message à l'assistant"
            />
            <Button
              size="icon"
              className="size-11 shrink-0"
              onClick={() => void send()}
              disabled={sending || !input.trim()}
              aria-label="Envoyer le message"
            >
              {sending ? (
                <Loader2 className="size-4 animate-spin" aria-hidden="true" />
              ) : (
                <Send className="size-4" aria-hidden="true" />
              )}
            </Button>
          </div>
          <p className="mt-1.5 flex items-center gap-1.5 text-[10px] text-muted-foreground">
            <RotateCcw className="size-3 shrink-0" aria-hidden="true" />
            Maj+Entrée pour un retour à la ligne · l&apos;historique est conservé sur cet appareil.
          </p>
        </div>
      </DialogContent>
    </Dialog>
  );
}

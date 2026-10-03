"use client";

import { BookOpen, Heart, Star, X } from "lucide-react";
import { Button } from "@/components/ui/button";
import {
  Dialog,
  DialogContent,
  DialogDescription,
  DialogHeader,
  DialogTitle,
} from "@/components/ui/dialog";
import { navigate, useFavorites } from "./hooks";

function formatDate(ts: number): string {
  try {
    return new Intl.DateTimeFormat("fr-FR", { day: "numeric", month: "short", hour: "2-digit", minute: "2-digit" }).format(new Date(ts));
  } catch {
    return "";
  }
}

export function FavoritesDialog({ open, onOpenChange }: { open: boolean; onOpenChange: (o: boolean) => void }) {
  const { favorites, remove } = useFavorites();

  const go = (bookId: string, docId: string) => {
    onOpenChange(false);
    navigate(`/livre/${bookId}/${docId}`);
  };

  return (
    <Dialog open={open} onOpenChange={onOpenChange}>
      <DialogContent className="top-[12%] max-h-[76vh] translate-y-0 overflow-y-auto border-amber-800/20 bg-card p-0 sm:max-w-xl">
        <DialogHeader className="sticky top-0 z-10 border-b border-amber-800/15 bg-card/95 px-5 pb-4 pt-5 backdrop-blur">
          <DialogTitle className="flex items-center gap-2 font-serif text-lg text-amber-950 dark:text-amber-50">
            <Heart className="size-4.5 text-primary" aria-hidden="true" />
            Mes favoris
          </DialogTitle>
          <DialogDescription>
            {favorites.length > 0
              ? `${favorites.length} document${favorites.length > 1 ? "s" : ""} enregistré${favorites.length > 1 ? "s" : ""} sur cet appareil.`
              : "Ajoutez des leçons depuis le lecteur avec le bouton cœur."}
          </DialogDescription>
        </DialogHeader>

        {favorites.length === 0 ? (
          <div className="flex flex-col items-center justify-center gap-3 px-6 py-12 text-center">
            <Star className="size-8 text-primary/40" aria-hidden="true" />
            <p className="font-serif text-base font-medium text-amber-950 dark:text-amber-50">
              Aucun favori pour l&apos;instant
            </p>
            <p className="max-w-sm text-sm leading-relaxed text-muted-foreground">
              Ouvrez une leçon puis touchez le cœur pour la retrouver ici — vos favoris restent
              enregistrés dans ce navigateur.
            </p>
          </div>
        ) : (
          <ul className="px-3 py-3">
            {favorites.map((f) => (
              <li key={`${f.bookId}/${f.docId}`} className="group relative">
                <button
                  type="button"
                  onClick={() => go(f.bookId, f.docId)}
                  className="mb-1 flex w-full items-start gap-3 rounded-xl border border-transparent px-3 py-2.5 text-left transition hover:border-amber-700/25 hover:bg-amber-100/50 dark:hover:border-amber-200/15 dark:hover:bg-amber-900/30"
                >
                  <BookOpen className="mt-1 size-4 shrink-0 text-primary" aria-hidden="true" />
                  <span className="min-w-0 flex-1">
                    <span className="block truncate font-serif text-[15px] font-semibold leading-snug text-amber-950 dark:text-amber-50">
                      {f.titleFr || f.titleAr}
                    </span>
                    <span className="mt-0.5 block truncate text-xs text-muted-foreground">
                      {f.bookTitleFr} · {formatDate(f.ts)}
                    </span>
                  </span>
                </button>
                <Button
                  variant="ghost"
                  size="icon"
                  aria-label={`Retirer ${f.titleFr || f.titleAr} des favoris`}
                  className="absolute end-1.5 top-1.5 size-8 text-muted-foreground/50 opacity-0 transition hover:text-destructive focus-visible:opacity-100 group-hover:opacity-100"
                  onClick={(e) => {
                    e.stopPropagation();
                    remove(f.bookId, f.docId);
                  }}
                >
                  <X className="size-4" aria-hidden="true" />
                </Button>
              </li>
            ))}
          </ul>
        )}
      </DialogContent>
    </Dialog>
  );
}

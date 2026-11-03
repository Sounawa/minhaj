import * as React from "react"

const MOBILE_BREAKPOINT = 768

// useSyncExternalStore : lecture initiale synchrone côté client sans
// setState dans l'effet (évite les cascades de rendu, cf. diagnostic
// performance — la valeur false pendant l'hydratation serveur est
// cohérente avec le rendu initial).
function subscribe(callback: () => void) {
  const mql = window.matchMedia(`(max-width: ${MOBILE_BREAKPOINT - 1}px)`)
  mql.addEventListener("change", callback)
  return () => mql.removeEventListener("change", callback)
}

export function useIsMobile() {
  return React.useSyncExternalStore(
    subscribe,
    () => window.innerWidth < MOBILE_BREAKPOINT,
    () => false,
  )
}

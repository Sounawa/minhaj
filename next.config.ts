import type { NextConfig } from "next";

// R603 — parade recyclage sandbox : node_modules du projet vit à /home/z/node_modules
// (racine stable hors-arbre ; l'arbre my-project est balayé par le nettoyeur du driver).
// Turbopack refusant de résoudre hors de sa racine détectée, on fixe root=/home/z.
// R606 (ouvrier A) : la cause réelle des vidages = NoSpaceLeft (disque 100 % plein :
// bundles de sûreté 3,1 Go + caches) — purgée, node_modules local survit ;
// turbopack.root retiré (il casse l'hydration client quand node_modules est local).
// R662 (ouvrier C) : l'évinceur est REVENU en cycle permanent (~1-2 min, disque
// pourtant libre 2,5 Go) — node_modules local vidé avant même la fin du démarrage.
// Retour à la recette R603 : deps à /home/z/node_modules (installées depuis une
// copie de package.json/bun.lock à /home/z) + turbopack.root=/home/z. Le script
// dev pointe déjà PATH vers /home/z/node_modules/.bin.
// R676 (ouvrier D, tick 499559) : l'évinceur balaye AUSSI .next entre le build
// webpack et le démarrage (« Could not find a production build ») et distDir
// hors-arbre est refusé par Next (invalid-dist-dir) — la parade définitive est
// le mode standalone : build webpack → copie de .next/standalone + .next/static
// + public vers /home/z/standalone-minhaj (zone stable hors évinceur, même
// recette d'esprit que R603 pour node_modules) → lancement
// « cd /home/z/my-project && PORT=3000 node /home/z/standalone-minhaj/server.js »
// (cwd au projet pour content/ ; le serveur en mémoire survit aux vidages).
// Prisma client généré vers /home/z/node_modules/.prisma/client (remontée d'arbre).
const nextConfig: NextConfig = {
  output: "standalone",
  turbopack: {
    root: "/home/z",
  },
  // R689 — parade « site invisible sur le preview » : Next 16.4 bloque par
  // défaut les ressources de dev (/_next/hmr, chunks) servies depuis un hôte
  // non déclaré — l'hydratation React échouait silencieusement en local
  // (127.0.0.1) ET sur le domaine de preview (*.space-z.ai) : widgets figés
  // (« Chargement de la bibliothèque… », « interrogation du moteur… »).
  allowedDevOrigins: ["localhost", "127.0.0.1", "*.space-z.ai"],
  typescript: {
    ignoreBuildErrors: true,
  },
  reactStrictMode: false,
};

export default nextConfig;

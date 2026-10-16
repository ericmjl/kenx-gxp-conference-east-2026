# Site tooling (Quartz v4)

This folder publishes the Obsidian vault as a static site that behaves like
Obsidian Publish: wikilinks, backlinks, search, a file explorer, a per-page
local graph, and a global graph overlay.

Vault markdown is **not** moved or rewritten. At build time the notes are
copied into a pinned [Quartz](https://quartz.jzhao.xyz) v4.5.2 checkout.

## Local build

From the repository root (requires git, Node 22, and npm):

```bash
python3 site/build.py
```

The first run clones Quartz into `~/.cache/kenx-gxp-quartz/v4.5.2` (or
`$QUARTZ_DIR` if set) so Obsidian does not index the generator source.
Output is `<quartz-dir>/public`. Preview:

```bash
python3 -m http.server 8080 --directory "$HOME/.cache/kenx-gxp-quartz/v4.5.2/public"
```

`Home.md` is the landing page (`index.md` is a build-time copy only).

## GitHub Pages

`.github/workflows/deploy.yml` builds on every push to `main` and deploys
to https://ericmjl.github.io/kenx-gxp-conference-east-2026/. The Pages source
must be **GitHub Actions** (Settings → Pages → Source).

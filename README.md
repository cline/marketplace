# Cline Marketplace

A curated catalog of high quality primitives for Cline: **plugins**, **skills**, and **MCP servers**. Each entry carries the metadata our website needs to display it, plus the exact one liner that installs it with the Cline CLI.

The published catalog is a single JSON file the website fetches at runtime:

```
https://cline.github.io/marketplace/catalog.json
```

## What this repo is (and is not)

This repo is **data only**. It is the source of truth for catalog entries plus the pipeline that publishes them. It contains **no UI**.

GitHub Pages here serves static files and nothing else:

- `https://cline.github.io/marketplace/catalog.json` the catalog
- `https://cline.github.io/marketplace/icons/...` the icon assets referenced by absolute URL in the JSON

The marketplace UI lives in a **separate project** (the Cline web app). It just fetches `catalog.json` and renders whatever it wants. The only coupling between the two is the JSON contract below.

Notes for the consuming app:

- **CORS works.** GitHub Pages sends `Access-Control-Allow-Origin: *`, so a browser `fetch` from any origin works without a proxy.
- **It is CDN cached** (Pages sits behind Fastly, roughly 10 minutes). Fine for a listing. If the app wants fresher data or no runtime dependency on GitHub, it can pull `catalog.json` at its own build or deploy time and bake it in. Nothing changes on this side.
- **The shape is stable.** Top level `version`, `generatedAt`, `counts`, `entries[]`. Each entry exposes `install.command` (ready to display) and `install.args` / `install.env` (structured, if the app wants to build its own install UI).

## How it works

- **Source of truth** is one folder per entry under `registry/<type>/<slug>/entry.json`. Concurrent additions never conflict, and every entry is reviewed on its own.
- **CI generates** `dist/catalog.json` from those folders, validates them against the schemas, copies icons, and stamps a version and timestamp.
- **CI publishes** the generated catalog to GitHub Pages on every merge to `main`.

```
registry/
  plugins/<slug>/entry.json   (+ icon.svg)
  skills/<slug>/entry.json
  mcps/<slug>/entry.json
schemas/
  common.schema.json          shared fields + install block
  plugin.schema.json | skill.schema.json | mcp.schema.json
scripts/generate.mjs          validate + build dist/catalog.json
```

## The install model

Every entry stores the argv that comes after `cline <type> install`. The verb is derived from `type`, and the generator renders the full command for the website.

| Type | Verb | `install.args` example | Rendered command |
| --- | --- | --- | --- |
| `plugin` | `cline plugin install` | `["goal"]` | `cline plugin install goal` |
| `skill` | `cline skill install` | `["vercel-labs/agent-skills", "--skill", "web-design-guidelines"]` | `cline skill install vercel-labs/agent-skills --skill web-design-guidelines` |
| `mcp` | `cline mcp install` | `["context7", "--transport", "http", "https://mcp.context7.com/mcp"]` | `cline mcp install context7 --transport http https://mcp.context7.com/mcp` |

Secrets and environment variables that are not part of the command (for example `EXA_API_KEY`) go in `install.env` so the website can prompt for them.

## Published catalog shape

```json
{
  "version": 1,
  "generatedAt": "2026-06-16T00:00:00.000Z",
  "baseUrl": "https://cline.github.io/marketplace",
  "counts": { "total": 3, "plugins": 1, "skills": 1, "mcps": 1 },
  "entries": [
    {
      "id": "context7",
      "type": "mcp",
      "name": "Context7",
      "tagline": "Up-to-date code docs for any library, fetched on demand",
      "icon": "https://cline.github.io/marketplace/icons/mcp/context7.svg",
      "install": {
        "args": ["context7", "--transport", "http", "https://mcp.context7.com/mcp"],
        "command": "cline mcp install context7 --transport http https://mcp.context7.com/mcp"
      }
    }
  ]
}
```

## Contributing

See [CONTRIBUTING.md](./CONTRIBUTING.md). Validate locally before opening a PR:

```bash
npm run validate     # validate every entry against the schemas
npm run generate     # also write dist/catalog.json to inspect the output
```

## License

[Apache 2.0 (c) 2026 Cline Bot Inc.](./LICENSE)

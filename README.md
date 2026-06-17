# Cline Marketplace

A curated catalog of high quality primitives for Cline: **plugins**, **skills**, and **MCP servers**. Each entry carries the metadata our website needs to display it, plus the exact one liner that installs it with the Cline CLI.

This repo is **data only** (no UI). It is the source of truth for entries plus the pipeline that publishes them to GitHub Pages. The marketplace UI lives in a separate project (the Cline web app) that fetches the published JSON. The only coupling between the two is the JSON contract documented below.

## Published URLs (GitHub Pages)

Everything is served from GitHub Pages behind a CDN. The base is:

```
https://cline.github.io/marketplace
```

### Catalog

| Asset | URL |
| --- | --- |
| Catalog JSON | `https://cline.github.io/marketplace/catalog.json` |

This single file is the whole API. Fetch it and you have every entry, the tag vocabulary, and counts.

```js
const catalog = await fetch("https://cline.github.io/marketplace/catalog.json").then((r) => r.json());
```

### Icons

Icons are published per entry. The URL pattern is:

```
https://cline.github.io/marketplace/icons/<type>/<slug>.<ext>
```

`<type>` is singular (`plugin`, `skill`, `mcp`), `<slug>` is the entry id, `<ext>` is whatever the source icon used (usually `svg`). Current examples:

| Entry | Type | Icon URL |
| --- | --- | --- |
| `goal` | plugin | `https://cline.github.io/marketplace/icons/plugin/goal.svg` |
| `web-search` | plugin | `https://cline.github.io/marketplace/icons/plugin/web-search.svg` |
| `web-design-guidelines` | skill | `https://cline.github.io/marketplace/icons/skill/web-design-guidelines.svg` |
| `context7` | mcp | `https://cline.github.io/marketplace/icons/mcp/context7.svg` |

You usually do not build these URLs yourself: every entry in `catalog.json` already has an `icon` field set to the absolute Pages URL. Render `entry.icon` directly.

```jsonc
// inside catalog.json, per entry
"icon": "https://cline.github.io/marketplace/icons/mcp/context7.svg"
```

The `baseUrl` field at the top of `catalog.json` always tells you the host the icons resolve against, so a consumer never has to hardcode it.

### Notes for the consuming app

- **CORS works.** Pages sends `Access-Control-Allow-Origin: *`, so a browser `fetch` from any origin works without a proxy.
- **It is CDN cached** (Pages sits behind Fastly, roughly 10 minutes). Fine for a listing. If the app wants fresher data or no runtime dependency on GitHub, pull `catalog.json` at its own build or deploy time and bake it in. Nothing changes on this side.
- **Custom domain:** set the `MARKETPLACE_BASE_URL` repo variable and the generator rewrites every icon URL and `baseUrl` to it. The catalog and icon paths stay the same, only the host changes.

## The `catalog.json` contract

```json
{
  "version": 1,
  "generatedAt": "2026-06-16T00:00:00.000Z",
  "baseUrl": "https://cline.github.io/marketplace",
  "counts": { "total": 4, "plugins": 2, "skills": 1, "mcps": 1 },
  "tags": [
    { "id": "software", "label": "Software Development", "count": 3 },
    { "id": "research", "label": "Research & Docs", "count": 2 }
  ],
  "entries": [
    {
      "id": "context7",
      "type": "mcp",
      "name": "Context7",
      "tagline": "Up-to-date code docs for any library, fetched on demand",
      "description": "A remote MCP server that pulls version-accurate docs into context.",
      "author": { "name": "Upstash", "url": "https://upstash.com" },
      "homepage": "https://context7.com",
      "repo": "https://github.com/upstash/context7",
      "icon": "https://cline.github.io/marketplace/icons/mcp/context7.svg",
      "tags": ["software", "research"],
      "license": "MIT",
      "verified": false,
      "featured": true,
      "install": {
        "args": ["context7", "--transport", "http", "https://mcp.context7.com/mcp"],
        "command": "cline mcp install context7 --transport http https://mcp.context7.com/mcp",
        "env": [
          { "name": "CONTEXT7_API_KEY", "required": false, "description": "Higher rate limits", "url": "https://context7.com/dashboard" }
        ]
      }
    }
  ]
}
```

Top level: `version`, `generatedAt`, `baseUrl`, `counts`, `tags[]` (full filter vocabulary with counts), `entries[]`. Each entry exposes `tags` (filter), `icon` (absolute Pages URL), `install.command` (ready to display), and `install.args` / `install.env` (structured, if the app builds its own install UI).

## The install model

Every entry stores the argv that comes after `cline <type> install`. The verb is derived from `type`, and the generator renders the full `install.command` for the website.

| Type | Verb | `install.args` example | Rendered command |
| --- | --- | --- | --- |
| `plugin` | `cline plugin install` | `["goal"]` | `cline plugin install goal` |
| `skill` | `cline skill install` | `["vercel-labs/agent-skills", "--skill", "web-design-guidelines"]` | `cline skill install vercel-labs/agent-skills --skill web-design-guidelines` |
| `mcp` | `cline mcp install` | `["context7", "--transport", "http", "https://mcp.context7.com/mcp"]` | `cline mcp install context7 --transport http https://mcp.context7.com/mcp` |

Secrets and environment variables that are not part of the command (for example `EXA_API_KEY`) go in `install.env` so the website can prompt for them.

## Tags

A single canonical tag vocabulary lives in [`tags.json`](./tags.json). Every entry's `tags` array must use only the `id`s from that file (lowercase), and each entry needs at least one tag. The build fails on an unknown tag, so the vocabulary stays the single source of truth.

```json
{ "id": "data", "label": "Data & Analytics" }
```

The generator publishes the full vocabulary into `catalog.json` as a top-level `tags` array, each with a `count` of how many entries use it, in `tags.json` order. The website filter renders this list directly (and may grey out or hide `count: 0` tags). To add a category, add it to `tags.json`; order there is the display order.

## Repo layout

```
registry/
  plugins/<slug>/entry.json   (+ icon.svg)
  skills/<slug>/entry.json
  mcps/<slug>/entry.json
schemas/
  common.schema.json          shared fields + install block
  plugin.schema.json | skill.schema.json | mcp.schema.json
tags.json                     canonical tag vocabulary
scripts/generate.mjs          validate + build dist/catalog.json
```

- **Source of truth** is one folder per entry, so concurrent additions never conflict.
- **CI validates** every entry against the schemas and the tag vocabulary on PRs.
- **CI publishes** the generated `catalog.json` and icons to GitHub Pages on every merge to `main`.

## Local development

```bash
npm run validate     # validate every entry (used in CI on PRs)
npm run generate     # also write dist/catalog.json + dist/icons to inspect output
```

See [CONTRIBUTING.md](./CONTRIBUTING.md) to add an entry.

## License

[Apache 2.0 (c) 2026 Cline Bot Inc.](./LICENSE)

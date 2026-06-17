<img width="1774" height="887" alt="image" src="https://github.com/user-attachments/assets/1e3af17b-fafd-4c02-82b9-8910a320daf1" />

A curated catalog of high quality primitives for Cline: **plugins**, **skills**, and **MCP servers**. Each entry carries the metadata needed to display it, plus the exact one liner that installs it with the Cline CLI. This repo is the source of truth for entries and the pipeline that publishes them as a single JSON file that any client can fetch.

## How it works

1. Open PR to add a primitive. Each entry is one folder under `registry/<type>/<slug>/entry.json`, where `<type>` is `plugins`, `skills`, or `mcps`. The folder name is the entry `id`. Co-located assets (like `icon.svg`) live next to `entry.json`. This keeps every entry independently reviewable and avoids merge conflicts when many are added at once.
2. GitHub Action runs to generate JSON. **`scripts/generate.mjs`** validates every entry, renders each `install.command`, copies icons, rewrites icon URLs to absolute, and writes `dist/catalog.json`.
3. Merging PR to main publishes `dist/` (the catalog plus icons) to GitHub Pages, generating updated assets at `https://cline.github.io/marketplace/*` for various clients displaying our marketplace to use.
4. The published catalog is one JSON file that can be fetched for the latest live marketplace data:

https://cline.github.io/marketplace/catalog.json

```json
{
  "version": 1,
  "generatedAt": "2026-06-16T00:00:00.000Z",
  "baseUrl": "https://cline.github.io/marketplace",
  "counts": { "total": 5, "plugins": 2, "skills": 2, "mcps": 1 },
  "tags": [
    { "id": "software", "label": "Software Development", "count": 4 },
    { "id": "research", "label": "Research & Docs", "count": 3 }
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

## Metadata

### Install commands

Every entry stores the argv that comes after `cline <type> install`. The verb is derived from `type`, and the generator renders the full `install.command` for any client to display.

| Type | Verb | `install.args` example | Rendered command |
| --- | --- | --- | --- |
| `plugin` | `cline plugin install` | `["goal"]` | `cline plugin install goal` |
| `skill` | `cline skill install` | `["cline/sdk-skill"]` | `cline skill install cline/sdk-skill` |
| `mcp` | `cline mcp install` | `["context7", "--transport", "http", "https://mcp.context7.com/mcp"]` | `cline mcp install context7 --transport http https://mcp.context7.com/mcp` |

Skills resolve sources the same way [`npx skills add`](https://github.com/vercel-labs/skills) does (`cline skill install` aliases it): pass `owner/repo` to install a whole repo, or add `--skill <name>` to pick one skill from a multi-skill repo.

Secrets and environment variables that are not part of the command (for example `EXA_API_KEY`) go in `install.env` so a client can prompt for them.

### Icons

Icons are published per entry. Every entry's `icon` field in `catalog.json` is already the absolute URL, so a client renders `entry.icon` directly and never has to build a URL. The underlying pattern is:

```
https://cline.github.io/marketplace/icons/<type>/<slug>.<ext>
```

`<type>` is singular (`plugin`, `skill`, `mcp`), `<slug>` is the entry id, `<ext>` is whatever the source icon used (usually `svg`). Some examples:

| Entry | Type | Icon URL |
| --- | --- | --- |
| `goal` | plugin | `https://cline.github.io/marketplace/icons/plugin/goal.svg` |
| `cline-sdk` | skill | `https://cline.github.io/marketplace/icons/skill/cline-sdk.svg` |
| `context7` | mcp | `https://cline.github.io/marketplace/icons/mcp/context7.svg` |

The `baseUrl` field at the top of `catalog.json` always tells a client which host the icons resolve against, so the host is never hardcoded on the consuming side.

### Tags

A single canonical tag vocabulary lives in [`tags.json`](./tags.json). Every entry's `tags` array must use only the `id`s from that file (lowercase), and each entry needs at least one tag. The build fails on an unknown tag, so the vocabulary stays the single source of truth.

```json
{ "id": "data", "label": "Data & Analytics" }
```

The generator publishes the full vocabulary into `catalog.json` as a top-level `tags` array, each with a `count` of how many entries use it, in `tags.json` order. A filter UI can render this list directly (and grey out or hide `count: 0` tags). To add a category, add it to `tags.json`; order there is the display order.

## Contributing

```bash
npm run validate     # validate every entry (used in CI on PRs)
npm run generate     # also write dist/catalog.json + dist/icons to inspect output
```

See [CONTRIBUTING.md](./CONTRIBUTING.md) to add an entry.

## License

[Apache 2.0 (c) 2026 Cline Bot Inc.](./LICENSE)

# Contributing

Thanks for adding to the Cline Marketplace. Each contribution is a single new folder, which keeps reviews focused and avoids merge conflicts.

## Add an entry

1. Pick the type: `plugin`, `skill`, or `mcp`.
2. Create `registry/<type>s/<slug>/entry.json`. The `<slug>` is kebab-case and must equal the `id` field.
3. Point `$schema` at the matching schema so your editor validates as you type:
   - plugins: `../../../schemas/plugin.schema.json`
   - skills: `../../../schemas/skill.schema.json`
   - mcps: `../../../schemas/mcp.schema.json`
4. Fill in the fields (see an existing entry for reference). The important one is `install.args`: everything after `cline <type> install`.
5. Optionally add an `icon.svg` (or `icon.png`) next to `entry.json` and set `"icon": "./icon.svg"`. Absolute https URLs are also allowed.
6. Run validation:

   ```bash
   npm run validate
   ```

7. Open a PR.

## install.args

Store the tokens exactly as a user would type them after the subcommand. The verb comes from `type`, so you never repeat `cline ... install` in the entry.

- plugin: `["goal"]`
- skill: `["owner/repo", "--skill", "name"]`
- mcp (remote, OAuth): `["name", "--transport", "http", "https://host/mcp"]`
- mcp (remote, static header): `["name", "--transport", "http", "https://host/mcp", "--header", "Authorization: Bearer <token>"]`
- mcp (stdio): `["name", "--", "npx", "-y", "some-mcp-server"]`

Put secrets and runtime environment variables that are not part of the command in `install.env`:

```json
"install": {
  "args": ["web-search"],
  "env": [
    { "name": "EXA_API_KEY", "required": true, "description": "Exa search key", "url": "https://exa.ai" }
  ]
}
```

## Review bar

- Entries should be high quality, maintained, and safe to install.
- `verified: true` is reserved for entries the Cline team has reviewed; leave it `false` in your PR.
- Keep `tagline` short (one sentence). Use `description` for detail.

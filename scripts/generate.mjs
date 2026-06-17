#!/usr/bin/env node
// Validates every registry entry and builds dist/catalog.json (+ copied icons).
//
//   node scripts/generate.mjs           validate + write dist/
//   node scripts/generate.mjs --check   validate only (used in CI on PRs)
//
// Zero dependencies on purpose: this runs in CI without an install step.

import {
  cpSync,
  existsSync,
  mkdirSync,
  readdirSync,
  readFileSync,
  rmSync,
  writeFileSync,
} from "node:fs";
import { basename, extname, join, relative } from "node:path";

const root = new URL("..", import.meta.url).pathname;
const registryRoot = join(root, "registry");
const distRoot = join(root, "dist");

// Where published assets will be served from. Override in CI for a custom domain.
const BASE = (process.env.MARKETPLACE_BASE_URL || "https://cline.github.io/marketplace").replace(/\/+$/, "");

// type -> the `cline <verb> install` the args belong to.
const INSTALL_VERB = {
  plugin: "plugin install",
  skill: "skill install",
  mcp: "mcp install",
};
const TYPE_DIRS = { plugins: "plugin", skills: "skill", mcps: "mcp" };
const SLUG = /^[a-z0-9]+(?:-[a-z0-9]+)*$/;

const checkOnly = process.argv.includes("--check");
const errors = [];
const entries = [];
const seenIds = new Set();

function fail(where, msg) {
  errors.push(`${where}: ${msg}`);
}

function shellQuote(token) {
  if (/^[A-Za-z0-9_@:/.,=+-]+$/.test(token)) return token;
  return `"${token.replace(/(["\\$`])/g, "\\$1")}"`;
}

function isStringArray(v) {
  return Array.isArray(v) && v.every((x) => typeof x === "string");
}

function validateEntry(type, slug, dir, entry) {
  const where = relative(root, join(dir, "entry.json"));
  if (entry.id !== slug) fail(where, `id "${entry.id}" must match directory name "${slug}"`);
  if (!SLUG.test(slug)) fail(where, `invalid slug "${slug}"`);
  if (entry.type !== type) fail(where, `type "${entry.type}" must be "${type}"`);
  for (const field of ["name", "tagline", "description"]) {
    if (typeof entry[field] !== "string" || !entry[field].trim()) {
      fail(where, `missing required string "${field}"`);
    }
  }
  if (seenIds.has(entry.id)) fail(where, `duplicate id "${entry.id}"`);
  seenIds.add(entry.id);

  const install = entry.install;
  if (!install || typeof install !== "object") {
    fail(where, "missing install object");
    return;
  }
  if (!isStringArray(install.args) || install.args.length === 0) {
    fail(where, "install.args must be a non-empty array of strings");
  }
  if (install.env !== undefined) {
    if (!Array.isArray(install.env)) {
      fail(where, "install.env must be an array");
    } else {
      for (const e of install.env) {
        if (!e || typeof e.name !== "string" || !e.name.trim()) {
          fail(where, "install.env[].name is required");
        }
      }
    }
  }

  // Icon must exist if it is a local (relative) path.
  if (typeof entry.icon === "string" && !/^https?:\/\//.test(entry.icon)) {
    if (!existsSync(join(dir, entry.icon))) {
      fail(where, `icon "${entry.icon}" does not exist`);
    }
  }
}

function buildEntry(type, slug, dir, entry) {
  const { $schema, ...rest } = entry;
  const args = entry.install.args;
  const command = `cline ${INSTALL_VERB[type]} ${args.map(shellQuote).join(" ")}`.trim();

  let icon = entry.icon;
  let iconCopy = null;
  if (typeof icon === "string" && !/^https?:\/\//.test(icon)) {
    const ext = extname(icon) || ".svg";
    const dest = `icons/${type}/${slug}${ext}`;
    iconCopy = { from: join(dir, icon), to: join(distRoot, dest) };
    icon = `${BASE}/${dest}`;
  }

  return {
    record: {
      ...rest,
      icon,
      install: { ...entry.install, command },
    },
    iconCopy,
  };
}

if (!existsSync(registryRoot)) {
  console.error("Missing registry directory");
  process.exit(1);
}

const iconCopies = [];

for (const [dirName, type] of Object.entries(TYPE_DIRS)) {
  const typeRoot = join(registryRoot, dirName);
  if (!existsSync(typeRoot)) continue;
  for (const dirent of readdirSync(typeRoot, { withFileTypes: true })) {
    if (!dirent.isDirectory()) continue;
    const slug = dirent.name;
    const dir = join(typeRoot, slug);
    const entryPath = join(dir, "entry.json");
    if (!existsSync(entryPath)) {
      fail(relative(root, dir), "missing entry.json");
      continue;
    }
    let entry;
    try {
      entry = JSON.parse(readFileSync(entryPath, "utf8"));
    } catch (err) {
      fail(relative(root, entryPath), `invalid JSON: ${err.message}`);
      continue;
    }
    validateEntry(type, slug, dir, entry);
    if (errors.length === 0) {
      const { record, iconCopy } = buildEntry(type, slug, dir, entry);
      entries.push(record);
      if (iconCopy) iconCopies.push(iconCopy);
    }
  }
}

if (errors.length > 0) {
  console.error(`Validation failed (${errors.length}):`);
  console.error(errors.join("\n"));
  process.exit(1);
}

entries.sort((a, b) => a.type.localeCompare(b.type) || a.id.localeCompare(b.id));

const counts = { total: entries.length };
for (const e of entries) counts[`${e.type}s`] = (counts[`${e.type}s`] || 0) + 1;

const catalog = {
  version: 1,
  generatedAt: new Date().toISOString(),
  baseUrl: BASE,
  counts,
  entries,
};

if (checkOnly) {
  console.log(`Validation passed: ${entries.length} entries.`);
  process.exit(0);
}

rmSync(distRoot, { recursive: true, force: true });
mkdirSync(distRoot, { recursive: true });
for (const { from, to } of iconCopies) {
  mkdirSync(join(to, ".."), { recursive: true });
  cpSync(from, to);
}
writeFileSync(join(distRoot, "catalog.json"), `${JSON.stringify(catalog, null, 2)}\n`);
console.log(`Wrote ${relative(root, join(distRoot, "catalog.json"))} (${entries.length} entries).`);

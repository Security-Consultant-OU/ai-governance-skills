# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project overview

This repository is an AI governance skills marketplace for Claude Code. It contains Markdown-based skills that make Claude a specialized compliance advisor for major AI regulations and frameworks. There is no application code — all skill content is structured Markdown with YAML frontmatter.

## Plugin directory pattern

```
plugins/<skill-name>/
  .claude-plugin/
    plugin.json          # Plugin metadata (name, version, author, etc.)
  skills/<skill-name>/
    SKILL.md             # Primary skill definition (loaded by Claude Code)
    references/          # Lookup tables and reference documents
      *.md
```

A plugin may contain additional skills under `skills/` (the `iso42001` plugin ships `iso-aisia`, `iso-ai-system-inventory`, `iso-ai-data-inventory`, `iso-ai-resources`, `iso-aims-policy-kit`; the `eu-ai-act` plugin ships `eu-gpai-cop`). Each extra skill still follows the 5-part `SKILL.md` convention and has its own self-contained `references/`.

The root `.claude-plugin/marketplace.json` lists all plugins in the marketplace.

## Skill dispatch

Before answering an AI-compliance question, follow `plugins/ai-governance/skills/using-ai-governance/SKILL.md`. Invoke the matching domain skill (Skill tool or read that skill’s `SKILL.md`). Announce `Using [skill] to [purpose]`. Do not blend EU / ISO / NIST / NYC / Korea / Brazil / CSA answers.

## Skills in this repo

- `ai-governance` — dispatcher (`using-ai-governance`); session-start hook
- `eu-ai-act` — EU AI Act (Regulation 2024/1689); plugin also includes `eu-gpai-cop`
- `nist-ai-rmf` — NIST AI Risk Management Framework
- `iso42001` — ISO/IEC 42001:2023 AI Management System (plugin also includes AISIA, inventories, resources, and AIMS policy-kit companions)
- `nyc-local-law-144` — NYC Local Law 144
- `south-korea-ai-act` — South Korea AI Basic Act
- `brazil-ai-act` — Brazil AI Act (Marco Legal da IA)
- `csa-aicm` — CSA AICM / AI-CAIQ / STAR for AI

## SKILL.md structure convention

Each `SKILL.md` follows a 5-part structure:

1. **Frontmatter** — YAML block with `name`, `description`, `version`, `triggers`, and `references` list
2. **Role and routing** — defines the persona Claude adopts and how to route user requests to the correct workflow
3. **Overview** — regulatory context, scope, key definitions, and applicability rules
4. **Workflows** — numbered, step-by-step procedures for each major compliance task (e.g., gap assessment, document generation, risk classification)
5. **Cross-mapping and gaps** — tables mapping this regulation to other frameworks, plus known gaps and edge cases

## Reference file conventions

Files in `references/` are lookup tables, not prose. Rules:

- One concept per file (e.g., `risk-categories.md`, `annex-iii-use-cases.md`)
- Markdown tables preferred over paragraphs
- Each file must be self-contained — no cross-references to other reference files
- `.md` extension only — no JSON, CSV, or YAML in references

## Severity indicators

Use consistent severity indicators in gap assessment outputs:

- Red (not started) — control or requirement has no evidence of implementation
- Yellow (partial) — some implementation exists but gaps remain
- Green (implemented) — control or requirement is fully met with documented evidence

## Adding a new skill

1. Create the plugin directory: `plugins/<name>/.claude-plugin/` and `plugins/<name>/skills/<name>/references/`
2. Create `plugins/<name>/.claude-plugin/plugin.json` with name, description, version, author, homepage, repository, license, and keywords
3. Create `plugins/<name>/skills/<name>/SKILL.md` following the 5-part structure
4. Add reference files to `plugins/<name>/skills/<name>/references/`
5. Add the plugin entry to `.claude-plugin/marketplace.json`
6. Run `python scripts/pack-skills.py` to refresh `skills/<name>.skill` archives for Claude.ai

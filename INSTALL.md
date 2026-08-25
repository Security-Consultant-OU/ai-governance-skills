# Install

This marketplace is built as a **Claude Code** plugin catalog (`.claude-plugin/marketplace.json`). Other tools load the same `SKILL.md` + `references/` folders, or the packed `.skill` zips in [`skills/`](skills/).

Always install the dispatcher plus the specialists you need. Plugin names: `ai-governance`, `eu-ai-act`, `nist-ai-rmf`, `iso42001`, `nyc-local-law-144`, `south-korea-ai-act`, `brazil-ai-act`, `csa-aicm`.

After editing source skills, rebuild zips with `python scripts/pack-skills.py`.

---

## Claude Code

Native path. In a Claude Code session:

```
/plugin marketplace add Security-Consultant-OU/ai-governance-skills
/plugin install ai-governance@ai-governance-skills
/plugin install eu-ai-act@ai-governance-skills
```

CLI equivalent:

```
claude plugin marketplace add Security-Consultant-OU/ai-governance-skills
claude plugin install ai-governance@ai-governance-skills
claude plugin install eu-ai-act@ai-governance-skills
```

Repeat install for any other plugin. Restart the session if skills do not appear.

---

## Claude.ai and Claude Desktop

Download a file from [`skills/`](skills/) and upload it to a conversation (Claude.ai) or add it as a project/desktop skill (Claude Desktop). Each `.skill` is a zip of one skill folder.

| File | Skill |
|------|--------|
| `skills/using-ai-governance.skill` | Dispatcher |
| `skills/eu-ai-act.skill` | EU AI Act |
| `skills/eu-gpai-cop.skill` | GPAI Code of Practice |
| `skills/nist-ai-rmf.skill` | NIST AI RMF |
| `skills/iso42001.skill` | ISO/IEC 42001 |
| `skills/iso-aisia.skill` | ISO AISIA |
| `skills/iso-ai-system-inventory.skill` | AI system register |
| `skills/iso-ai-data-inventory.skill` | Data-for-AI inventory |
| `skills/iso-ai-resources.skill` | AI resource inventory |
| `skills/iso-aims-policy-kit.skill` | AIMS policy kit |
| `skills/nyc-local-law-144.skill` | NYC Local Law 144 |
| `skills/south-korea-ai-act.skill` | Korea AI Basic Act |
| `skills/brazil-ai-act.skill` | Brazil PL 2338 (not enacted) |
| `skills/csa-aicm.skill` | CSA AICM / AI-CAIQ |

---

## Cursor

Cursor reads Agent Skills from a folder that contains `SKILL.md` (and `references/` next to it).

**This machine (all workspaces):** copy each skill directory into `~/.cursor/skills/<skill-name>/`.

**One repo only:** copy into `.cursor/skills/<skill-name>/` in that repo.

Example (PowerShell), EU Act + dispatcher:

```
git clone --depth 1 https://github.com/Security-Consultant-OU/ai-governance-skills.git $env:TEMP\ai-gov-skills
New-Item -ItemType Directory -Force -Path "$env:USERPROFILE\.cursor\skills" | Out-Null
Copy-Item -Recurse "$env:TEMP\ai-gov-skills\plugins\ai-governance\skills\using-ai-governance" "$env:USERPROFILE\.cursor\skills\using-ai-governance"
Copy-Item -Recurse "$env:TEMP\ai-gov-skills\plugins\eu-ai-act\skills\eu-ai-act" "$env:USERPROFILE\.cursor\skills\eu-ai-act"
```

`SKILL.md` must sit directly in `~/.cursor/skills/<name>/SKILL.md`, not one extra folder down. Restart Agent chat after copying.

Cursor’s plugin marketplace (`/add-plugin`) does **not** currently list this GitHub catalog. Use the copy path above.

---

## Codex (CLI, desktop Codex, ChatGPT Work)

Codex does **not** consume `.claude-plugin/marketplace.json` as a first-class Claude marketplace. It discovers skills as folders:

| Scope | Path |
|-------|------|
| User | `$CODEX_HOME/skills/<name>/` (usually `~/.codex/skills/`) |
| Repo | `.agents/skills/<name>/` (walks from cwd to repo root) |

Copy the same trees as Cursor (`plugins/<plugin>/skills/<skill>/` → that destination).

From a Codex session you can also ask **`$skill-installer`** to pull a GitHub path, for example:

```
Install skills from GitHub repo Security-Consultant-OU/ai-governance-skills
paths:
  plugins/ai-governance/skills/using-ai-governance
  plugins/eu-ai-act/skills/eu-ai-act
```

`AGENTS.md` in this repo is for **contributors editing the marketplace**, not an end-user installer. This catalog is not published as a Codex plugin (no `.codex-plugin/plugin.json` per plugin).

---

## GitHub Copilot (CLI, VS Code Copilot)

Copilot CLI can treat a GitHub repo as a marketplace if it finds `marketplace.json` under `.claude-plugin/` (this repo has that file).

```
copilot plugin marketplace add Security-Consultant-OU/ai-governance-skills
copilot plugin install ai-governance@ai-governance-skills
copilot plugin install eu-ai-act@ai-governance-skills
```

In an interactive Copilot CLI session the same commands work with a leading `/`.

If marketplace install fails (layout mismatch with Agent Plugins 1.0), install a single skill:

```
copilot plugin install --skill https://github.com/Security-Consultant-OU/ai-governance-skills/tree/main/plugins/eu-ai-act/skills/eu-ai-act
```

Or copy folders into `.github/skills/<name>/` (project) using the universal method below.

---

## Other tools (Gemini CLI, OpenCode, Windsurf, Cline, Aider, …)

There is no native marketplace entry for this repo. Use the **universal copy**:

1. Clone https://github.com/Security-Consultant-OU/ai-governance-skills
2. Copy each `plugins/<plugin>/skills/<skill>/` directory (must include `SKILL.md` and `references/`) into that product’s skills directory
3. Restart the agent

Typical skill roots:

| Tool | User / project skills directory |
|------|----------------------------------|
| Gemini CLI | project `.gemini/skills/` or the path your `gemini-extension.json` declares |
| OpenCode | `~/.config/opencode/skills/` or project skills dir from their docs |
| Windsurf / Cline | project skills / custom instructions folder for that product |

Do not unpack a `.skill` zip one folder too deep: the zip already contains `<skill-name>/SKILL.md`.

---

## What “installed” should look like

For folder-based tools, each skill is:

```
<skills-root>/<skill-name>/SKILL.md
<skills-root>/<skill-name>/references/*.md
```

Dispatcher first (`using-ai-governance`), then specialists. Mixed-jurisdiction questions should load **one skill per slice**, not a blend of article numbers.

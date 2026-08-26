# AI governance skills

A [Claude Code](https://claude.com/claude-code) plugin marketplace. Each plugin turns the agent into a **specialist** for one law or framework: classification, 🔴🟡🟢 gap tables, and a copy-ready artefact. Skills **invoke each other** instead of mixing article numbers.

Full “what / when / will not” for every skill: [SKILLS.md](SKILLS.md).

## How routing works

1. Install **`ai-governance`**. A session-start hook loads `using-ai-governance` (the catalog).
2. Install the specialists you need. Mixed-jurisdiction questions run **one skill per slice**.
3. The agent announces `Using [skill] to [purpose]`, then follows that skill. If a skill is missing it names the skill and gives installation guidance for the current client.

Collision terms (`high-risk`, `GPAI`, `FRIA`, `AISIA`, `deployer`) are disambiguated in `using-ai-governance`. Mapping tables are lookup aids, not a substitute for the source skill.

## Install

Per-client steps (Claude Code, Claude.ai / Desktop, Cursor, Codex, Copilot, and a copy-folder fallback): **[INSTALL.md](INSTALL.md)**.

**Claude Code** (native marketplace):

```
/plugin marketplace add Security-Consultant-OU/ai-governance-skills
/plugin install ai-governance@ai-governance-skills
/plugin install eu-ai-act@ai-governance-skills
```

**Claude.ai / Desktop:** upload a file from [`skills/`](skills/). Rebuild zips with `python scripts/pack-skills.py` after editing source skills.

## Plugins

Status notes as of **25 August 2026**.

| Plugin | Version | Skills you get | Use for |
|--------|---------|----------------|---------|
| `ai-governance` | 1.0.0 | `using-ai-governance` | Catalog, session-start routing |
| `eu-ai-act` | 1.3.0 | `eu-ai-act`, `eu-gpai-cop` | Regulation 2024/1689: Art. 5 / Art. 6 / additive Art. 50, operational checklists, FRIA, GPAI, CE / Annex IV. CoP is `eu-gpai-cop` |
| `nist-ai-rmf` | 1.2.0 | `nist-ai-rmf` | NIST AI 100-1 Current vs Target (72 outcomes), Playbook-safe guidance, NIST AI 600-1 overlay |
| `iso42001` | 1.4.0 | `iso42001` plus five companions (below) | ISO/IEC 42001:2023 AIMS: gap, SoA, certification |
| `nyc-local-law-144` | 1.2.0 | `nyc-local-law-144` | NYC AEDT determination, DCWP above-median scoring-rate tables, notices |
| `south-korea-ai-act` | 1.2.0 | `south-korea-ai-act` | In-force Korea AI Basic Act (22 Jan 2026): **고영향 AI**, Arts. 31–36, Decree 36053 |
| `brazil-ai-act` | 1.2.0 | `brazil-ai-act` | **Pending** PL 2338/2023 (Senate substitute). Not law. Always labelled as a bill |
| `csa-aicm` | 1.0.0 | `csa-aicm` | CSA AICM / AI-CAIQ / STAR for AI from **your** workbook. Does not invent control IDs |

### ISO companions (installed with `iso42001`)

| Skill | Artefact |
|-------|----------|
| `iso-aisia` | AISIA record (6.1.4 / 8.4, A.5.2–A.5.5) |
| `iso-ai-system-inventory` | AI system register (Clause 4.3) |
| `iso-ai-data-inventory` | Data-for-AI inventory (A.7, A.4.3) |
| `iso-ai-resources` | Resource pack (A.4, Clause 7.1) |
| `iso-aims-policy-kit` | Policies, SOPs, Stage 1 document master list |

## Defaults and rules

If you omit the document type, each specialist has a default (Annex IV, Current vs Target Profile, gap + SoA, and so on — see [SKILLS.md](SKILLS.md)).

Gap status is always **🔴 not started / 🟡 partial / 🟢 implemented**. Skills do not invent article, Annex A, NIST subcategory, AICM, or Playbook IDs.

Official ISO, EU OJ, and CSA PDFs are **cited, not copied**. AICM / CAIQ IDs come from the user’s workbook.

This repo is Markdown skills plus dependency-free packaging and validation scripts. Validate changes with `python scripts/validate_skills.py`; contributor conventions: [CLAUDE.md](CLAUDE.md).

## License

MIT. Maintained by [Security Consultant OÜ](https://github.com/Security-Consultant-OU/ai-governance-skills).

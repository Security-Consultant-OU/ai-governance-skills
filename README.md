# AI governance skills

A [Claude Code](https://claude.com/claude-code) plugin marketplace. Each plugin turns the agent into a **specialist** for one law or framework: classification, 🔴🟡🟢 gap tables, and a copy-ready artefact. Skills **invoke each other** instead of mixing article numbers.

Full “what / when / will not” for every skill: [SKILLS.md](SKILLS.md).

## How routing works

1. Install **`ai-governance`**. A session-start hook loads `using-ai-governance` (the catalog).
2. Install the specialists you need. Mixed-jurisdiction questions run **one skill per slice**.
3. The agent announces `Using [skill] to [purpose]`, then follows that skill. If a skill is missing it prints `/plugin install <name>@ai-governance-skills`.

Collision terms (`high-risk`, `GPAI`, `FRIA`, `AISIA`, `deployer`) are disambiguated in `using-ai-governance`. Mapping tables are lookup aids, not a substitute for the source skill.

## Install

```
/plugin marketplace add Security-Consultant-OU/ai-governance-skills
/plugin install ai-governance@ai-governance-skills
/plugin install eu-ai-act@ai-governance-skills
```

Repeat `/plugin install <name>@ai-governance-skills` for any other plugin below.

**Claude.ai (web / desktop):** download a `.skill` file from [`skills/`](skills/) and upload it to a conversation. Re-pack after editing source skills with `python scripts/pack-skills.py`.

| Skill file | Skill |
|---|---|
| `skills/using-ai-governance.skill` | Dispatcher / catalog |
| `skills/eu-ai-act.skill` | EU AI Act |
| `skills/eu-gpai-cop.skill` | GPAI Code of Practice (Art. 56) |
| `skills/nist-ai-rmf.skill` | NIST AI RMF |
| `skills/iso42001.skill` | ISO/IEC 42001 AIMS |
| `skills/iso-aisia.skill` | ISO AISIA record |
| `skills/iso-ai-system-inventory.skill` | AI system register |
| `skills/iso-ai-data-inventory.skill` | Data-for-AI inventory |
| `skills/iso-ai-resources.skill` | AI resource inventory |
| `skills/iso-aims-policy-kit.skill` | AIMS policy / SOP kit |
| `skills/nyc-local-law-144.skill` | NYC Local Law 144 |
| `skills/south-korea-ai-act.skill` | Korea AI Basic Act |
| `skills/brazil-ai-act.skill` | Brazil PL 2338 (not enacted) |
| `skills/csa-aicm.skill` | CSA AICM / AI-CAIQ |

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

This repo is Markdown skills only (YAML frontmatter). Conventions for contributors: [CLAUDE.md](CLAUDE.md).

## License

MIT. Maintained by [Security Consultant OÜ](https://github.com/Security-Consultant-OU/ai-governance-skills).

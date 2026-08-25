# Claude Skills for AI Governance

A Claude Code plugin marketplace containing AI governance skills covering major AI regulations and frameworks. Each skill transforms Claude into a specialized compliance advisor capable of gap assessments, document generation, risk classification, and structured guidance — all grounded in the actual regulatory text.

Skills are **aware of each other**. Install the dispatcher, then any specialists. When a question spans jurisdictions, the loaded skill **invokes** the others instead of improvising.

**Marketplace version (25 August 2026):** `ai-governance` **1.0.0**, `eu-ai-act` **1.3.0**, `iso42001` **1.4.0**, `csa-aicm` **1.0.0**; other plugins **1.2.0**.

What each skill does, when to use it, and what it will not do: [SKILLS.md](SKILLS.md).

## Available skills

| Skill | Description |
|---|---|
| `using-ai-governance` | Dispatcher (plugin `ai-governance`): catalog, collision terms, invoke-before-answering. Session-start hook injects it. |
| `eu-ai-act` | EU AI Act (Regulation 2024/1689): non-exclusive classification (Art. 5 / Art. 6 / additive Art. 50), high-risk operational checklists, FRIA gate, GPAI, Art. 43 conformity/CE, Annex IV. Same plugin also installs `eu-gpai-cop` (Art. 56 Code of Practice) |
| `nist-ai-rmf` | NIST AI RMF 1.0: Current vs Target Profile against 72 official subcategory outcomes, Playbook-safe guidance, NIST AI 600-1 overlay |
| `iso42001` | ISO/IEC 42001:2023 AIMS: gap assessment, SoA, certification. Same plugin also installs `iso-aisia`, `iso-ai-system-inventory`, `iso-ai-data-inventory`, `iso-ai-resources`, `iso-aims-policy-kit` |
| `nyc-local-law-144` | NYC Local Law 144: AEDT determination, DCWP bias audit (above-median scoring rate), notices, and gap assessment |
| `south-korea-ai-act` | South Korea AI Basic Act (**in force 22 Jan 2026**; status 25 Aug 2026): high-impact AI (고영향 AI), Arts. 31–36, Art. 35 endeavor AISIA, Art. 36 domestic representative; Decree No. 36053 in force |
| `brazil-ai-act` | Pending PL 2338/2023 (Senate substitute; **not enacted** as of 25 Aug 2026): risk, rights, SIA/ANPD as proposed coordinator, roles — always labelled as a bill |
| `csa-aicm` | CSA AICM / AI-CAIQ: workbook-backed CAIQ answers, AICM gap rows, STAR for AI Level 1. Does not invent control IDs |

Official ISO, EU, and CSA PDFs are **not** copied into this repo. Skills cite and paraphrase; AICM/CAIQ IDs come from the user's workbook.

## Installation

### Claude Code (CLI, IDE extensions)

Add the marketplace, install the dispatcher, then the specialists you need:

```
/plugin marketplace add verifywise-ai/ai-governance-skills
/plugin install ai-governance@ai-governance-skills
/plugin install eu-ai-act@ai-governance-skills
```

`ai-governance` is the Superpowers-style router: a session-start hook loads `using-ai-governance`, which requires invoking the matching specialist before answering. Specialists also name each other and say **invoke**, not guess.

Available plugin names: `ai-governance`, `eu-ai-act`, `nist-ai-rmf`, `iso42001`, `nyc-local-law-144`, `south-korea-ai-act`, `brazil-ai-act`, `csa-aicm`

### Claude.ai (web and desktop app)

This marketplace does not currently ship packaged `.skill` archives. For Claude.ai, copy the contents of `plugins/<name>/skills/<name>/` (the `SKILL.md` plus `references/`) into a project, or install via Claude Code as above. Copy `plugins/ai-governance/skills/using-ai-governance/SKILL.md` as well if you want routing.

## Author

Gorkem Cetin

## License

MIT

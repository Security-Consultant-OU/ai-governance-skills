---
name: eu-gpai-cop
description: >
  Assesses GPAI model-provider adherence to the EU AI Act Article 56 Code of
  Practice (transparency, copyright, safety and security chapters) and fills
  the model documentation form. Use when the user mentions the GPAI Code of
  Practice, Art. 56 CoP, GPAI model card under the CoP, or GPAI copyright
  chapter. Do not use for Brazil PL 2338 GPAI, ISO AISIA, or Art. 50-only
  system labelling without a model-provider CoP question.
version: 1.3.0
triggers:
  - GPAI Code of Practice
  - Article 56
  - EU GPAI CoP
  - GPAI model documentation form
  - GPAI copyright chapter
references:
  - references/cop-chapters.md
---

# EU GPAI Code of Practice advisor (Article 56)

## Role and routing

You advise **GPAI model providers** on the Art. 56 Code of Practice as a route to demonstrate Chapter V (Arts. 51–55) duties. You do not classify AI systems under Art. 5/6 (invoke `eu-ai-act`). You do not treat CoP adherence as mandatory.

If the user omits document type, produce **chapter autoeval + model documentation form** from `references/cop-chapters.md`.

**Do not invent CoP paragraph numbers or Annex XI letters.** If a clause ID is not in context or in the user’s CoP PDF, write “not in context.”

### Out of scope — invoke sister skills

Names in the table are **other skills**. Before answering that slice, **invoke** the named skill (Skill tool, or read its `SKILL.md`). Announce `Using [skill] to [purpose]`. Do not improvise that jurisdiction. If it is missing: `/plugin install <plugin>@ai-governance-skills`. Routing catalog: `using-ai-governance`.

| User need | Skill |
|-----------|-------|
| Art. 5/6/50 system classification, FRIA, CE | `eu-ai-act` |
| Art. 50 AI-generated-content marking only | `eu-ai-act` |
| Brazil GPAI / copyright bill | `brazil-ai-act` |
| ISO 42001 SoA / AISIA | `iso42001` / `iso-aisia` |
| CSA AICM / CAIQ | `csa-aicm` |

### Use cases

| User asks | Skill does | Artefact |
|-----------|------------|----------|
| Should we sign the CoP? | Adherence vs alternative means | Decision + mapped Art. 53/55 duties |
| Fill the model documentation form | Form in cop-chapters.md | Model documentation |
| Copyright chapter only | Art. 53(1)(c) operationalisation | Copyright/TDM row |
| Systemic-risk model + CoP | Keep Art. 55(1)(b) separate from red-team | Chapter + 55 table |

---

## Overview

| Fact | Detail |
|------|--------|
| Legal hook | Art. 56 — codes of practice for GPAI obligations |
| Presumption | Approved-code adherence → presumption of conformity for covered duties |
| Alternative | Adequate means without the CoP still must meet Arts. 53/55 |
| OSS | Art. 53(2) drops only 53(1)(a)–(b) and **not** if systemic-risk |
| Compute presumption | Art. 51 — >10^25 FLOPs |

GPAI CoP chapters in the user’s library typically include: model transparency; copyright; safety and security; plus a separate **system-level** AI-generated-content transparency paper — that last one is Art. 50, not Chapter V.

---

## Workflows

### Workflow 1 — CoP pack (default)

**Output IS:** (1) role = GPAI model provider, (2) systemic-risk yes/no, (3) adhere vs alternative, (4) chapter autoeval, (5) model documentation form.

1. Confirm model vs system. If system-only, invoke `eu-ai-act`.
2. Run Art. 51 / 52 / 53(2) tests.
3. For each chapter, one row: mapped article, status, evidence.
4. Fill the model documentation form. If OSS + not systemic-risk, mark 53(1)(a)–(b) N/A.

### Workflow 2 — Alternative means only

If the user will not adhere: output Art. 53(1)(a)–(d) and, if systemic-risk, Art. 55(1)(a)–(d) with named alternative artefacts. Do not claim a CoP presumption.

---

## Cross-mapping and gaps

CSA AICM and NIST 600-1 are not the CoP. ISO 42001 does not create an Art. 56 presumption.

Common gaps: treating CoP as mandatory; collapsing Art. 55(1)(b) into red-teaming; applying OSS drops to 53(1)(c)–(d) or to systemic-risk models; using the content-transparency CoP paper as a substitute for Art. 53 model docs.

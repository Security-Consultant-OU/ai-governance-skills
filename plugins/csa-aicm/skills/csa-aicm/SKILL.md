---
name: csa-aicm
description: >
  Fills CSA AI-CAIQ answers and AICM control gap tables from the user's AICM
  workbook; supports STAR for AI Level 1 evidence and mappings to ISO 42001
  or NIST AI 600-1 when those sheets exist. Use when the user mentions CSA
  AICM, AI-CAIQ, STAR for AI, CSA AI Controls Matrix, or CAIQ for AI. Do not
  use for ISO 42001 SoA, EU CE marking, or NIST Current vs Target Profiles.
version: 1.0.0
triggers:
  - CSA AICM
  - AI-CAIQ
  - STAR for AI
  - CSA AI Controls Matrix
  - CAIQ for AI
references:
  - references/caiq-templates.md
---

# CSA AICM and AI-CAIQ advisor

## Role and routing

You produce **CSA STAR for AI / AI-CAIQ** artefacts and **AICM** gap rows. Control and question IDs come **only** from the user’s workbook. You are not an ISO 42001 auditor and not an EU notified body. If another marketplace skill applies, invoke it before answering that slice — catalog: `using-ai-governance`.

If the user omits document type, produce a **CAIQ answer table** plus 🔴🟡🟢 gaps (`references/caiq-templates.md`).

**Do not invent AICM or CAIQ IDs.** If the workbook is not in context, ask for it (AICM sheet + AI-CAIQ sheet) and output empty ID columns rather than guessed codes.

### Out of scope — invoke sister skills

Names in the table are **other skills**. Before answering that slice, **invoke** the named skill (Skill tool, or read its `SKILL.md`). Announce `Using [skill] to [purpose]`. Do not improvise that jurisdiction. If it is missing: `/plugin install <plugin>@ai-governance-skills`. Routing catalog: `using-ai-governance`.

| User need | Skill |
|-----------|-------|
| ISO 42001 SoA / certification | `iso42001` |
| ISO AISIA / inventories / policy kit | `iso-aisia` / `iso-ai-system-inventory` / `iso-aims-policy-kit` |
| EU high-risk / CE / Art. 56 CoP | `eu-ai-act` / `eu-gpai-cop` |
| NIST Current vs Target (72 outcomes) | `nist-ai-rmf` |
| BSI AI C4 as the primary catalogue | Stay only for mapping rows if the C4 mapping sheet is present |

### Use cases

| User asks | Skill does | Artefact |
|-----------|------------|----------|
| Fill our AI-CAIQ | Role split; one row per workbook question | CAIQ table |
| STAR for AI Level 1 | Submission gap list against CAIQ | Evidence list |
| Map AICM to ISO 42001 | Use mapping sheet only | Mapping table |
| Buyer vs provider | Customer vs application-provider guidelines | Split autoeval |

---

## Overview

| Piece | Role |
|-------|------|
| AICM | AI control catalogue (CCM-family) |
| AI-CAIQ | Consensus questionnaire for those controls |
| STAR for AI Level 1 | CAIQ-based submission |
| CBRA | Optional CSA risk method — do not replace ISO 6.1.2 or EU Art. 9 |
| LLM taxonomy sheet | Vocabulary — not extra control IDs |

Implementation and auditing PDFs are often **role-split** (AI customer vs application provider). Match the user’s role before answering Yes.

---

## Workflows

### Workflow 1 — CAIQ autoeval (default)

**Output IS:** (1) role, (2) workbook version, (3) CAIQ table, (4) gaps.

1. Confirm customer vs provider vs both.
2. Copy question IDs from the `AI-CAIQ` sheet.
3. Answer Yes / No / N/A with evidence.
4. Link each row to the AICM control ID from the workbook, not from memory.

### Workflow 2 — STAR Level 1 readiness

List missing CAIQ answers and missing evidence. Do not call this ISO certification.

### Workflow 3 — Mapping

Only if the user has a mapping sheet. Output AICM ID → target ID. Never invent ISO A.5.8 or NIST MAP-2.4.

---

## Cross-mapping and gaps

ISO 42001 SoA still needs all **38** Annex A controls with justification — an AICM mapping does not complete the SoA. NIST 600-1 mapping does not replace the 72 Core outcomes.

Common gaps: guessed control IDs; customer answers on a provider questionnaire; treating STAR L1 as AIMS certification; using CBRA as EU Art. 9.

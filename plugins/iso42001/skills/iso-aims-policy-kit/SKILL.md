---
name: iso-aims-policy-kit
description: >
  Use when a request concerns an ISO/IEC 42001 AIMS policy pack, management
  manual, SOPs, forms, document master list, documented-information controls,
  or a Stage 1 certification evidence set.
---

# ISO/IEC 42001 AIMS policy and document kit

## Role and routing

You produce **documented information** for an AIMS: policies, procedures, forms, and a master list. You do not score a full SoA (invoke `iso42001`). You do not fill a detailed AISIA record (invoke `iso-aisia`).

If the user omits document type, produce the **master list scored 🔴🟡🟢** plus the four-policy pack in `references/document-master-list.md`.

**Do not invent Annex A IDs.** AIMS-DOC / SOP / FR numbers are an **example organisation scheme**, not ISO IDs. Map every document to a real clause or selectable control. A.x.1 is an objective. There is no A.5.8. Decommission is not A.10.

Strip client names from any source draft.

### Out of scope — invoke sister skills

Names in the table are **other skills**. Before answering that slice, **invoke** the named skill (Skill tool, or read its `SKILL.md`). Announce `Using [skill] to [purpose]`. Do not improvise that jurisdiction. If it is missing, name it and give installation guidance for the current client; otherwise direct the user to the marketplace `INSTALL.md`. Routing catalog: `using-ai-governance`.

| User need | Skill |
|-----------|-------|
| Gap + SoA of 38 controls | `iso42001` |
| AISIA record | `iso-aisia` |
| AI system register | `iso-ai-system-inventory` |
| Data-for-AI inventory | `iso-ai-data-inventory` |
| A.4 resource pack | `iso-ai-resources` |
| EU high-risk checklists / CE | `eu-ai-act` |
| CSA CAIQ / AICM | `csa-aicm` |

### Use cases

| User asks | Skill does | Artefact |
|-----------|------------|----------|
| What documents do we need for Stage 1? | Master list vs 4.3–9.3 | Scored master list |
| Write the AI policy | 5.2 + A.2.2 recipe | Policy skeleton |
| AISIA procedure vs record | SOP-13 process vs RC-25 record | Two artefacts, split |
| User-only org | Mark A.6 development SOPs N/A with 4.3 | Master list with exclusions |

---

## Overview

Stage 1 auditors ask for controlled documented information, not a slide deck. Clause **7.5** is the control of that information. Annex A policies live under **A.2**; AISIA process under **A.5.2**.

ISO/IEC 42005 may deepen AISIA method; it is not a substitute for 6.1.4.

---

## Workflows

### Workflow 1 — Master list (default)

**Output IS:** (1) role, (2) master list table, (3) Stage 1 gaps, (4) next documents to draft.

### Workflow 2 — Single policy or SOP

**Output IS:** document-control header (ID, version, owner, review date) → purpose/scope → requirements with ISO citations → records → related documents.

### Workflow 3 — Harmonised IMS

If the user already has ISO/IEC 27001: map AIMS docs to existing ISMS docs; do not duplicate 7.5. Keep AI-specific records (AISIA, A.7, A.4) distinct.

---

## Cross-mapping and gaps

EU Art. 17 QMS is not this kit. CSA STAR for AI is not Stage 1.

Common gaps: ethics statement with no A.2.2 objectives; AISIA memo with no A.5.2 procedure; development SOPs in a user-only organisation without 4.3 exclusion; A.10 used for decommission.

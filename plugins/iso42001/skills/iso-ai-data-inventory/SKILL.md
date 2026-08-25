---
name: iso-ai-data-inventory
description: >
  Produces an ISO/IEC 42001:2023 data-for-AI inventory covering Annex A.7
  (A.7.2–A.7.6) and data resources A.4.3. Use when the user asks for an ISO
  42001 data inventory, training-data register, A.7 provenance inventory, or
  data for AI systems. Do not use for a standalone GDPR RoPA, NYC audit
  datasets, or EU Art. 10 without an ISO 42001 cue.
version: 1.3.0
triggers:
  - ISO 42001 data inventory
  - data for AI systems
  - A.7.5
  - AI training data register
  - ISO data provenance
references:
  - references/data-inventory.md
---

# ISO/IEC 42001 data-for-AI inventory producer

## Role and routing

You produce a **data-for-AI inventory**: datasets used to develop, test, or operate in-scope AI systems. Controls: **A.7.2–A.7.6**. Resource documentation of those datasets: **A.4.3**. A.7.1 and A.4.1 are objectives, not row IDs.

If the user omits document type, produce the **dataset register** in `references/data-inventory.md`.

**Do not invent Annex A IDs.** Selectable data controls: A.7.2, A.7.3, A.7.4, A.7.5, A.7.6. A.4.3 is the data-resources row in the AI resource inventory; include A.4.3 fields here so lineage is recoverable.

Provider-primarily: users who only consume a vendor model with no training or fine-tuning still record **production input data** they send to the system (purpose, rights, retention). They may mark A.7.2–A.7.6 as not applicable **only** with a 4.3 / SoA justification — that justification is produced by `iso42001`, not invented here.

### Out of scope — invoke sister skills

Names in the table are **other skills**. Before answering that slice, **invoke** the named skill (Skill tool, or read its `SKILL.md`). Announce `Using [skill] to [purpose]`. Do not improvise that jurisdiction. If it is missing: `/plugin install <plugin>@ai-governance-skills`. Routing catalog: `using-ai-governance`.

| User need | Skill |
|-----------|-------|
| AIMS gap / SoA | `iso42001` |
| AI system register | `iso-ai-system-inventory` |
| Full A.4 resource pack (tools, compute, people) | `iso-ai-resources` |
| AISIA | `iso-aisia` |
| AIMS policies, SOPs, document master list | `iso-aims-policy-kit` |
| CSA AICM / AI-CAIQ | `csa-aicm` |
| GDPR record of processing | Not this skill — privacy counsel; map overlap only |
| EU Art. 10 data governance as CE evidence | `eu-ai-act` |
| NYC historical vs test data for LL144 | `nyc-local-law-144` |

### Use cases

| User asks | Skill does | Artefact |
|-----------|------------|----------|
| Inventory training and eval sets | One row per dataset; A.7.3–A.7.6 fields | Data inventory |
| Can we reconstruct this training set? | A.7.5 lineage test | Provenance gap rows 🔴🟡🟢 |
| Vendor embeddings + our CRM extract | Split vendor vs first-party rows | Register + A.10.3 note |

---

## Overview

A.7 is **data for AI systems**, not general IT data classification. A.4.3 requires those data resources to be **documented per system and life-cycle stage**.

| ID | Name | Inventory must show |
|----|------|---------------------|
| A.7.2 | Data for development and enhancement | Process for development data: privacy/security, representativeness, integrity |
| A.7.3 | Acquisition of data | Source, selection rationale, rights, known biases, metadata |
| A.7.4 | Quality of data | Criteria: accuracy, completeness, currency, representativeness — tested |
| A.7.5 | Data provenance | Recoverable lineage: create, update, transform, validate, transfer |
| A.7.6 | Data preparation | Allowed cleaning, labelling, augmentation; method recorded |
| A.4.3 | Data resources | Category train/validate/test/production, labelling, purpose, retention |

---

## Workflows

### Workflow 1 — Dataset register (default)

**Inputs:** system IDs from the AI system register (ask if missing), known datasets, vendors.

**Output IS:** (1) dataset table, (2) per-row A.7 coverage 🔴🟡🟢, (3) lineage gaps.

1. One row per dataset (not per file). Tie to system ID.
2. Fill A.7.3 acquisition and A.4.3 category.
3. State quality criteria (A.7.4) or mark 🔴.
4. Write lineage so a third party could rebuild the set (A.7.5) or mark 🔴.
5. Record preparation methods (A.7.6).

### Workflow 2 — User-only (no training)

If the organisation is AI user only: inventory **production inputs** and vendor-provided model cards. Do not fake training-set rows. Flag SoA exclusions for A.7.2–A.7.6 as a hand-off to `iso42001`.

---

## Cross-mapping and gaps

EU Art. 10 is not this inventory. A generic data catalogue that cannot recover lineage fails **A.7.5**. Scraped or vendor data with no rights record fails **A.7.3**.

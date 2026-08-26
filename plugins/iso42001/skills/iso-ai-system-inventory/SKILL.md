---
name: iso-ai-system-inventory
description: >
  Use when a request concerns an ISO/IEC 42001 AI system inventory, AIMS
  register, Clause 4.3 scope evidence, or a structured register of AI-system
  owners, roles, purposes, dependencies, and lifecycle status.
---

# ISO/IEC 42001 AI system register producer

## Role and routing

You produce the **AI system register** that Clause **4.3** requires as part of AIMS scope. This is the list of in-scope (and justified out-of-scope) AI systems, not a SoA and not a data inventory.

If the user omits document type, produce the **register table** plus a one-paragraph scope statement using `references/system-register.md`.

**Do not invent clause IDs.** Scope is **4.3**. Context is **4.1**. Interested parties are **4.2** (include people subject to AI decisions). Annex A IDs are not register row IDs.

Clarify: **AI provider**, **AI user**, or **both**. Role drives later SoA exclusions; it does not hide embedded SaaS, pilots, or internal automation unless a written exclusion exists.

### Out of scope — invoke sister skills

Names in the table are **other skills**. Before answering that slice, **invoke** the named skill (Skill tool, or read its `SKILL.md`). Announce `Using [skill] to [purpose]`. Do not improvise that jurisdiction. If it is missing, name it and give installation guidance for the current client; otherwise direct the user to the marketplace `INSTALL.md`. Routing catalog: `using-ai-governance`.

| User need | Skill |
|-----------|-------|
| Gap assessment, SoA, certification | `iso42001` |
| AISIA record | `iso-aisia` |
| Data-for-AI inventory | `iso-ai-data-inventory` |
| Resource inventory (A.4) | `iso-ai-resources` |
| AIMS policies, SOPs, document master list | `iso-aims-policy-kit` |
| CSA AICM / AI-CAIQ | `csa-aicm` |
| NIST Current vs Target / GOVERN inventory | `nist-ai-rmf` |
| NYC AEDT determination | `nyc-local-law-144` |
| Korea 고영향 catalogue | `south-korea-ai-act` |

### Use cases

| User asks | Skill does | Artefact |
|-----------|------------|----------|
| List our AI for ISO 42001 | Register every system; flag missing owners | 4.3 register |
| Copilots and SaaS scoring — in scope? | Include unless 4.3 exclusion with rationale | Row + exclusion log |
| Scope statement for Stage 1 | Scope paragraph + register excerpt | Stage 1 4.3 pack |

---

## Overview

Clause 4.3 requires a defined AIMS scope and an **AI system register**: name, intended purpose, deployment status, responsible owner. Incomplete registers (CRM scoring, email filters, copilots omitted) are a common Stage 1 nonconformity.

| Column | Why |
|--------|-----|
| Name | Unique identifier auditors can trace |
| Intended purpose | 4.3 and later AISIA/risk |
| Provider vs user | Annex A applicability |
| Owner | 5.3 / A.3.2 |
| Life-cycle stage | A.6 evidence later |
| Personal data y/n | Feeds A.7 / privacy policies — not a GDPR RoPA |
| In-scope y/n | Exclusions need rationale |

---

## Workflows

### Workflow 1 — Build or refresh the register (default)

**Inputs:** org units, known products, SaaS list, pilots. If the list is empty, output a blank register and a discovery checklist (interviews, procurement, shadow IT, model hubs).

**Output IS:** (1) scope statement, (2) register table, (3) exclusion log, (4) 🔴🟡🟢 completeness notes.

1. Write AIMS boundaries (processes, locations, AI types included).
2. Add a row per system, including embedded AI and pilots.
3. Record exclusions with rationale (not “we forgot”).
4. Mark rows missing owner, purpose, or in-scope flag as 🟡.

### Workflow 2 — Discovery interview script

If the user does not know what they have: output the discovery questions in `references/system-register.md`, then the empty table to fill live.

---

## Cross-mapping and gaps

NIST GOVERN 1.6 is an inventory analogue, not this register. Do not score NIST subcategory IDs here.

Common gaps: scope too narrow; register not reviewed when a new system is deployed; no owner; SaaS AI treated as “just a vendor.”

---
name: iso-ai-resources
description: >
  Use when a request concerns ISO/IEC 42001 AI resources, Annex A.4 resource
  documentation, Clause 7.1 resource allocation, or inventories of AI data,
  tooling, compute, infrastructure, and human competencies.
---

# ISO/IEC 42001 AI resource inventory producer

## Role and routing

You produce **resource documentation for AI systems** (Annex **A.4**) and **AIMS-level resources** (Clause **7.1**). A.4.1 is the objective, not a row ID. Selectable controls: **A.4.2, A.4.3, A.4.4, A.4.5, A.4.6**.

If the user omits document type, produce the **per-system resource pack** in `references/resource-inventory.md`, then a 7.1 AIMS allocation excerpt.

**Do not invent Annex A IDs.** A.4.3 datasets overlap `iso-ai-data-inventory` — list resource pointers here; do not replace the A.7 inventory.

Provider-primarily for A.4.3–A.4.5 (data, tooling, compute). **A.4.2** and **A.4.6** apply to both provider and user. Users still document the resources they depend on (vendor model name/version, people who oversee use).

### Out of scope — invoke sister skills

Names in the table are **other skills**. Before answering that slice, **invoke** the named skill (Skill tool, or read its `SKILL.md`). Announce `Using [skill] to [purpose]`. Do not improvise that jurisdiction. If it is missing, name it and give installation guidance for the current client; otherwise direct the user to the marketplace `INSTALL.md`. Routing catalog: `using-ai-governance`.

| User need | Skill |
|-----------|-------|
| AIMS gap / SoA / competence matrix detail (7.2) | `iso42001` |
| AI system register | `iso-ai-system-inventory` |
| Full A.7 data inventory | `iso-ai-data-inventory` |
| AISIA | `iso-aisia` |
| AIMS policies, SOPs, document master list | `iso-aims-policy-kit` |
| CSA AICM / AI-CAIQ | `csa-aicm` |
| Cloud cost optimisation only | Not this skill unless tied to A.4.5 capacity/environment |
| NIST Current vs Target | `nist-ai-rmf` |

### Use cases

| User asks | Skill does | Artefact |
|-----------|------------|----------|
| What does this model run on? | A.4.2–A.4.5 rows for that system | Resource pack |
| Who is competent to operate it? | A.4.6 people + pointer to 7.2 | Human-resource table |
| Can we reconstruct after an incident? | A.4.2 completeness test | 🔴🟡🟢 gaps |

---

## Overview

| ID | Name | Applies to | Inventory shows |
|----|------|------------|-----------------|
| A.4.2 | Resource documentation | Both | All resources the system depends on, by life-cycle stage |
| A.4.3 | Data resources | Provider (primarily) | Datasets: category, purpose, quality pointer, retention |
| A.4.4 | Tooling resources | Provider (primarily) | Models, frameworks, libraries, eval and provisioning tools |
| A.4.5 | System and computing resources | Provider (primarily) | Compute, storage, network, hosting, capacity, environmental impact |
| A.4.6 | Human resources | Both | People and competencies across the life cycle |
| 7.1 | Resources (AIMS) | Both | Budget and allocation to establish, run, and improve the AIMS |

A.4.2 fails if the organisation cannot reconstruct the system after an incident. Shadow model hubs fail A.4.4. Competence only for developers fails A.4.6.

---

## Workflows

### Workflow 1 — Per-system pack (default)

**Inputs:** system ID from the AI system register (ask if missing).

**Output IS:** A.4.2 header, then A.4.3–A.4.6 tables, then 7.1 excerpt, then 🔴🟡🟢 completeness.

1. List life-cycle stages in use.
2. Point at datasets (IDs from data inventory) under A.4.3.
3. List models, libraries, eval tools (A.4.4) with versions.
4. List compute/hosting/capacity/environment (A.4.5).
5. List named people and roles, including oversight and retirement (A.4.6).
6. AIMS budget/allocation note (7.1) — ongoing operation, not only project go-live.

### Workflow 2 — User of a vendor model

Fill A.4.2 with vendor model/API, version, subprocessors, and the humans who approve use (A.4.6). Mark A.4.3–A.4.5 fields the vendor must supply. Do not invent GPU inventories you do not have.

---

## Cross-mapping and gaps

Clause 7.2 competence matrix is the deeper people artefact — keep A.4.6 as the system-level roster and hand 7.2 scoring to `iso42001`.

Common gaps: no inventory; data mixed with general IT CMDB; unmanaged libraries; cloud spend without AI capacity or energy; competence defined only for developers.

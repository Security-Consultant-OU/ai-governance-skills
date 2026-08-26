---
name: iso42001
description: >
  Use when a request concerns ISO/IEC 42001:2023, an AI management system
  (AIMS), certification readiness, clauses 4–10, AI risk assessment, the 38
  Annex A controls, or a Statement of Applicability.
---

# ISO/IEC 42001 AI Management System advisor

## Role and routing

You are an expert ISO/IEC 42001:2023 Lead Auditor and AIMS implementation consultant. If another marketplace skill applies, invoke it before answering that slice — catalog: `using-ai-governance`.

Clarify role first: **AI provider** (develops or supplies AI), **AI user** (uses or relies on third-party AI), or **both**. Annex A applicability differs by role.

**Do not invent clause or Annex A control IDs.** Look up IDs in `references/controls-annex-a.md` (38 controls) and `references/clauses-requirements.md` (clauses 4–10). **A.x.1 is the objective**, not a control. There is no A.5.8. **A.10 is suppliers and customers**, not decommission. ISO/IEC 42001 AISIA is **Clause 6.1.4** (process) and **8.4** (perform) — not 6.1.2 and not Korea Art. 35.

If the user omits document type, produce **gap assessment + Statement of Applicability** for in-scope systems. Copy-ready rows: `references/iso-templates.md`. Worked examples: `references/iso-worked-examples.md`.

### Out of scope — invoke sister skills

ISO/IEC 42001 is a certifiable AIMS. It is **not** NYC bias-audit math, **not** EU CE marking, and **not** the NIST AI RMF Playbook.

Names in the table are **other skills**. Before answering that slice, **invoke** the named skill (Skill tool, or read its `SKILL.md`). Announce `Using [skill] to [purpose]`. Do not improvise that jurisdiction. If it is missing, name it and give installation guidance for the current client; otherwise direct the user to the marketplace `INSTALL.md`. Routing catalog: `using-ai-governance`.

| User need | Invoke |
|-----------|--------|
| NYC AEDT determination, above-median scoring rate, candidate notice | `nyc-local-law-144` |
| EU CE marking, Art. 43 conformity assessment, Art. 27 FRIA, GPAI Chapter V | `eu-ai-act` |
| GPAI Code of Practice / Art. 56 model documentation | `eu-gpai-cop` |
| NIST Playbook actions, Current vs Target Profile, NIST AI 600-1 | `nist-ai-rmf` |
| Korea Art. 35 impact endeavor, high-impact AI (고영향) | `south-korea-ai-act` |
| Brazil PL 2338/2023 (not enacted) | `brazil-ai-act` |
| Standalone ISO AISIA record | `iso-aisia` |
| AI system register / inventory (4.3) | `iso-ai-system-inventory` |
| Data-for-AI inventory (A.7 / A.4.3) | `iso-ai-data-inventory` |
| AI resource inventory (A.4 / 7.1) | `iso-ai-resources` |
| AIMS policies, SOPs, document master list | `iso-aims-policy-kit` |
| CSA AICM / AI-CAIQ | `csa-aicm` |

When the user wants **only** one of those artefacts, invoke that companion. When they want gap + SoA + those artefacts together, stay here and follow Workflows 1–2, or produce the companion-shaped tables in the same answer.

### Use cases

| User asks | Skill does | Artefact |
|-----------|------------|----------|
| User-only SoA (no development; internal AI only) | Role-based applicability; exclude only with scope/role justification | SoA with real IDs (e.g. A.6.1.2, A.10.4 excluded) |
| AISIA vs AI risk | Split 6.1.4/8.4 (impacts) from 6.1.2/8.2 (likelihood × severity) | Two records, not one merged memo |
| Stage 1 documents | List required documented information for Stage 1 | Checklist with clause/control citations |
| Supplier due diligence | A.10.3 (and A.10.2 allocation) beyond generic vendor security | Due-diligence pack |

Long walkthroughs → `references/iso-worked-examples.md`.

### Task routing

| Task | Output IS (this order) |
|------|------------------------|
| Default (type omitted) | 1 Scope and role → 2 AI system register excerpt → 3 Gap table → 4 SoA (all 38) → 5 30/60/90-day actions |
| Gap analysis | Gap table: Clause/Control \| Requirement \| Status 🔴🟡🟢 \| Evidence \| Gap |
| AIMS scope | Boundaries, AI system register, roles, exclusions with justification |
| AI risk assessment | Risk register: likelihood × severity, treatment per 6.1.3 |
| ISO/IEC 42001 AISIA | AISIA record per 6.1.4 / 8.4 and A.5.2–A.5.5 |
| Policy / SOP kit / document master list | `iso-aims-policy-kit` unless the user also wants gap + SoA in this pack |
| Policy (single statement) | Document control, scope, statement, roles, requirements, review date |
| Control implementation | Purpose → Requirements → Implementation → Evidence → Audit tips |
| SoA | SoA table: Control ID \| Name \| Applicable? \| Justification \| Status \| Evidence |
| Certification readiness | Stage 1 then Stage 2 checklists with 🔴🟡🟢 |
| General question | Prose with clause/control citations |

---

## Overview

**ISO/IEC 42001:2023** (18 December 2023) is the certifiable AI management system (AIMS) standard. Harmonized Structure — integrates with ISO/IEC 27001 and ISO 9001.

| Element | Content |
|---------|---------|
| Clauses 4–10 | Mandatory AIMS requirements (PDCA) |
| Annex A | 38 reference controls in 9 objectives (A.2–A.10). A.x.1 = objective |
| Annex B | Implementation guidance for Annex A |
| Annex C | Possible AI objectives and risk sources |
| Annex D | Use of the AIMS across domains |

**Who:** providers, users, any size, sector-agnostic.

| Unique element | Citation | Note |
|----------------|----------|------|
| ISO/IEC 42001 AISIA | **6.1.4** process, **8.4** perform, **A.5** controls | Impacts on individuals, groups, society. Not 6.1.2. ISO/IEC 42005 is optional method depth |
| AI risk assessment | **6.1.2 / 8.2** | Likelihood × severity of AI-specific risks |
| Risk treatment + SoA | **6.1.3** | Every one of the 38 controls included or excluded with justification |
| AI policy | **5.2** + **A.2.2** | Clause requirement; A.2.2 is the matching control (review **A.2.4**) |
| Human oversight | **A.9.2** and life-cycle gates in **A.6** | Not a standalone Annex A ID |
| Data for AI | **A.7** (provenance **A.7.5**) | |
| Information for parties | **A.8** | |
| Third parties / customers | **A.10** | Suppliers (**A.10.3**) and customers (**A.10.4**) — not decommission |

Read `references/controls-annex-a.md` for the 38 controls, `references/clauses-requirements.md` for clauses 4–10, `references/ai-risk-assessment.md` for risk + AISIA method, `references/iso-templates.md` for copy-ready rows, `references/cross-framework-mapping.md` for other frameworks.

---

## Workflows

Copy-ready gap row, SoA row, AISIA skeleton, and Stage 1 checklist: `references/iso-templates.md`.

### Workflow 1 — Gap assessment

**Inputs:** Role (provider/user/both), AI systems in scope, current documentation, target certification date.

**Output IS:** (1) scope and role, (2) gap table for clauses 4–10 then the 38 Annex A controls, (3) 30/60/90-day roadmap ordered by certification risk.

1. Score clauses 4–10. Required evidence includes: context, interested parties, **scope + AI system register (4.3)**, AI policy (5.2), roles (5.3), **AI risk assessments (6.1.2 / 8.2)**, **ISO/IEC 42001 AISIA records (6.1.4 / 8.4)**, SoA (6.1.3), objectives (6.2), **planning of changes (6.3)**, competence (7.2), documented information (7.5), operational controls (8.1), internal audit (9.2), management review (9.3).
2. For each of the 38 Annex A controls, determine applicability from role, AISIA, and risk. Cite IDs only from `references/controls-annex-a.md`.
3. Flag SoA gaps: applicable but not implemented, or exclusions without justification.
4. Produce the 30/60/90-day roadmap.

Status icons: 🔴 not started · 🟡 partial · 🟢 implemented. Do not use these icons for risk ratings.

### Workflow 1b — Scope and AI system register

Do this before gap scoring.

**Output IS:** (1) context 4.1, (2) interested parties 4.2 including people subject to AI decisions, (3) scope statement 4.3, (4) AI system register, (5) exclusions with rationale.

Register columns: name, intended purpose, provider vs user role, owner, life-cycle stage, personal data (y/n), in-scope (y/n). Include embedded AI in SaaS, pilots, and internal automation unless a justified exclusion is recorded.

### Workflow 2 — ISO/IEC 42001 AISIA (Clause 6.1.4 / 8.4, A.5)

ISO/IEC 42001 AISIA evaluates impacts on **individuals, groups, and society**. It is **not** Clause 6.1.2 and **not** Korea Art. 35.

**Inputs:** system description, intended purpose, deployment context, affected populations.

**Output IS** the AISIA record in `references/iso-templates.md`: system description → affected populations → impact dimensions → Low/Medium/High classification → required controls → approval.

1. Document the system (purpose, I/O, advisory vs autonomous, environment).
2. Identify affected populations, including vulnerable groups.
3. Assess impact dimensions (nature, severity, breadth, reversibility, consent, oversight, recourse).
4. Classify Low / Medium / High using `references/ai-risk-assessment.md`. That scale is an **acceptable process** under 6.1.4, not the only ISO method. Point to **ISO/IEC 42005** when the user needs deeper methodology.
5. Select proportionate Annex A depth (especially A.5, A.8, A.9.2, A.6.2.6–A.6.2.8).
6. Reassess on change and at planned intervals (perform under **8.4**).

EU Art. 14 high-risk human-oversight language belongs to `eu-ai-act`, not this AIMS.

### Workflow 3 — AI risk assessment (Clause 6.1.2 / 8.2)

Separate from ISO/IEC 42001 AISIA. Likelihood × severity of AI-specific risks.

**Output IS:** risk register (ID, system, category, description, inherent L×S, treatment, Annex A control, residual L×S, owner, review date).

1. Identify risks: model, data, operational, supply chain, regulatory.
2. Score 5×5 (Rare–Almost certain × Negligible–Critical). Use **Low/Medium/High/Critical text**, not 🔴🟡🟢.
3. Treat per **6.1.3**: modify, accept with monitoring, avoid, transfer (accountability stays with the organisation).
4. Feed results into SoA selection.

### Workflow 4 — Statement of Applicability (Clause 6.1.3)

Cover **all 38** Annex A controls. Every exclusion must trace to role, scope, risk, or AISIA.

**Output IS** the SoA table for all 38 IDs from `references/controls-annex-a.md`.

Do not exclude a policy or process control because “nothing is happening right now.” User-only examples (A.6.1.2, A.10.4) → `references/iso-worked-examples.md`.

### Workflow 5 — Policy generation

**Output IS:** document-control header → purpose and scope → policy statement → roles → requirements (cited) → monitoring → related documents → revision history.

| Policy | Primary citation |
|--------|------------------|
| AI policy | **5.2** + **A.2.2** (review **A.2.4**; alignment **A.2.3**) |
| AI risk management | **6.1.2 / 6.1.3 / 8.2** |
| Acceptable / responsible use | **A.9.2**, **A.9.4** |
| Data for AI | **A.7** |
| Incident communication | **A.8.4** (reporting channel **A.8.3**) |
| Life cycle (deployment and retirement practices) | **A.6** |
| Supplier / third-party | **A.10.2**, **A.10.3** |

### Workflow 6 — Certification readiness

**Output IS:** Stage 1 documentation checklist, then Stage 2 implementation checklist, each scored 🔴🟡🟢. Full Stage 1 list: `references/iso-templates.md`.

Stage 1 (documentation): scope + register (4.3); signed AI policy (5.2, A.2.2); roles and concerns channel (5.3, A.3.2, A.3.3); risk process and registers (6.1.2); AISIA process and records (6.1.4, A.5.2–A.5.3); SoA of 38 (6.1.3); objectives and planning of changes (6.2, 6.3); competence and documented information (7.2, 7.5); internal audit programme and management-review template (9.2, 9.3).

Stage 2 (implementation): executed risk and treatment (8.2, 8.3); executed AISIA (**8.4**); competence and awareness records (7.2, 7.3); life-cycle evidence (A.6.2.4–A.6.2.8); supplier / allocation records (A.10.2, A.10.3); incident communication (A.8.4); data quality and provenance (A.7.4, A.7.5); internal audit report, management-review minutes, corrective action (9.2, 9.3, 10.2).

Surveillance annually; recertification every 3 years.

---

## Cross-mapping and gaps

Full crosswalk tables live only in `references/cross-framework-mapping.md`. Do not duplicate them here.

ISO/IEC 42001 AISIA (6.1.4 / 8.4 / A.5) is a management-system impact process. Closest analogues elsewhere: EU Art. 27 FRIA (narrower addressee), NIST MAP 5, Korea Art. 35 (endeavor, not this clause). Invoke those skills when the user needs those artefacts.

### Common gaps

1. **AISIA missing for in-scope systems** — primary system assessed; embedded SaaS AI and pilots ignored (**6.1.4 / 8.4 / A.5**).
2. **AI system register incomplete** — CRM scoring, email filtering, copilots omitted (**4.3**).
3. **Data provenance undocumented** — A.7.4 quality informal; **A.7.5** lineage missing.
4. **Human oversight not evidenced** — practice exists; no records under **A.9.2** / life-cycle gates.
5. **Supplier AI due diligence missing** — **A.10.3**; responsibilities unallocated (**A.10.2**).
6. **No concerns channel** — **A.3.3** not implemented.
7. **Event logs cannot reconstruct AI decisions** — **A.6.2.8**.
8. **AI objectives not measurable** — **6.2** / **A.6.1.2** / **A.9.3**.

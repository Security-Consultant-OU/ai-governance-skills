---
name: iso-aisia
description: >
  Use when a request concerns an ISO/IEC 42001 AI system impact assessment
  (AISIA), Clauses 6.1.4 or 8.4, controls A.5.2–A.5.5, or impacts of an AI
  system on individuals, groups, or society within an AIMS.
---

# ISO/IEC 42001 AISIA record producer

## Role and routing

You produce **ISO/IEC 42001 AISIA** artefacts only: impacts on individuals, groups, and society. Clause **6.1.4** is the process; **8.4** is perform; **A.5.2–A.5.5** are the controls. This is **not** Clause 6.1.2 (AI risk) and **not** Korea Art. 35 or EU Art. 27.

If the user omits document type, produce one **AISIA record** per named system using `references/aisia-record.md`.

**Do not invent clause or Annex A IDs.** Selectable A.5 controls are A.5.2, A.5.3, A.5.4, A.5.5. A.5.1 is the objective, not a record ID. There is no A.5.8. ISO/IEC 42005 is optional method depth, not required by 42001.

### Out of scope — invoke sister skills

Names in the table are **other skills**. Before answering that slice, **invoke** the named skill (Skill tool, or read its `SKILL.md`). Announce `Using [skill] to [purpose]`. Do not improvise that jurisdiction. If it is missing, name it and give installation guidance for the current client; otherwise direct the user to the marketplace `INSTALL.md`. Routing catalog: `using-ai-governance`.

| User need | Skill |
|-----------|-------|
| AIMS gap, SoA, certification | `iso42001` |
| AI system register / inventory | `iso-ai-system-inventory` |
| Data-for-AI inventory | `iso-ai-data-inventory` |
| AI resource inventory | `iso-ai-resources` |
| AIMS policies, SOPs, document master list | `iso-aims-policy-kit` |
| CSA AICM / AI-CAIQ | `csa-aicm` |
| Likelihood × severity risk register | `iso42001` (Workflow 3) |
| EU Art. 27 FRIA | `eu-ai-act` |
| Korea Art. 35 endeavor | `south-korea-ai-act` |
| Brazil AIA (PL 2338, not enacted) | `brazil-ai-act` |

### Use cases

| User asks | Skill does | Artefact |
|-----------|------------|----------|
| Fill an AISIA for this chatbot | Six-step 6.1.4 process; Low/Medium/High | AISIA record |
| Is our risk register enough? | Split: keep 6.1.2 separate; produce AISIA | Two artefacts named as such |
| Vendor model, we are the user | Still run AISIA on in-scope use (A.5.2) | AISIA + A.10.2 allocation note |

---

## Overview

AISIA is mandatory for **every AI system in AIMS scope**. Triggers: new system; change of purpose, population, or context; material model update; incident; planned review (at least annually); legal change.

Low/Medium/High is an **acceptable process** under 6.1.4, not the only ISO method.

| Control | Name | Record must show |
|---------|------|------------------|
| A.5.2 | AISIA process | Triggers, method, roles, feed into design/SoA |
| A.5.3 | Documentation | Versioned written record, updated on change |
| A.5.4 | Individuals or groups | Rights, wellbeing, autonomy, fairness, privacy, safety, accessibility, vulnerable groups |
| A.5.5 | Societal impacts | Environment, labour, democratic processes, public safety, cultural norms, misuse at scale |

---

## Workflows

### Workflow 1 — AISIA record (default)

**Inputs:** system name, intended purpose, I/O, advisory vs autonomous, environment, affected populations. If missing, ask; do not invent populations.

**Output IS** the sections in `references/aisia-record.md` in that order.

1. Describe the system (purpose, I/O, authority, scale, owner).
2. Map users, decision subjects, indirect parties, vulnerable groups.
3. Score dimensions: nature, severity, breadth, reversibility, consent, oversight, recourse.
4. Classify Low / Medium / High using the table in `references/aisia-record.md`.
5. List proportionate controls (A.5, A.8, A.9.2, A.6.2.6–A.6.2.8). Do not add invented IDs.
6. Approval block and next-review trigger (perform under **8.4**).

### Workflow 2 — Process vs record gap

If the user has no procedure: output (1) A.5.2 process skeleton (triggers, roles, SoA feed) then (2) one filled record. Score 🔴🟡🟢 only for process existence, not for impact level.

---

## Cross-mapping and gaps

ISO AISIA is a management-system impact process. EU Art. 27 FRIA has a narrower addressee. Korea Art. 35 is endeavor. Brazil AIA is a pending-bill artefact. Invoke those skills; do not relabel those as 6.1.4.

Common gaps: primary system assessed, embedded SaaS and pilots skipped; privacy-only with A.5.5 skipped; one-time memo with no 8.4 refresh.

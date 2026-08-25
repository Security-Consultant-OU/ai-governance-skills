# ISO/IEC 42001 copy-ready templates

Fill-in rows for AIMS gap assessment, Statement of Applicability, ISO/IEC 42001 AISIA (Clause 6.1.4 / 8.4), and Stage 1 documentation. Use only real clause IDs (4–10) and the 38 Annex A control IDs. **A.x.1 is the objective**, not a SoA line. There is no A.5.8. A.10 is suppliers and customers.

If the user omits document type, produce **gap assessment + SoA** using the Default combined recipe, then these rows.

---

## Contents

- Default combined recipe
- Gap row
- SoA row
- AISIA record skeleton
- Stage 1 document checklist

---

## Default combined recipe

When document type is omitted, the output **IS** these sections in this order:

1. Scope and role (provider / user / both; AIMS boundaries)
2. AI system register excerpt (in-scope systems)
3. Gap table (clauses 4–10, then applicable Annex A controls)
4. Statement of Applicability (all 38 controls)
5. 30/60/90-day actions ordered by certification risk

Status in gap and Stage 1 tables: 🔴 not started · 🟡 partial · 🟢 implemented.

---

## Gap row

| Clause/Control | Requirement | Status 🔴🟡🟢 | Evidence | Gap |
|----------------|-------------|---------------|----------|-----|
| 4.3 | AIMS scope and AI system register | 🔴 Not started | | List every in-scope AI system; record exclusions |
| 6.1.2 | AI risk assessment process | 🟡 Partial | Methodology draft | Registers missing for [system] |
| 6.1.4 | ISO/IEC 42001 AISIA process | 🔴 Not started | | Separate AISIA from 6.1.2 risk |
| A.2.2 | AI policy | 🟢 Implemented | AI-POL-001 signed | Schedule A.2.4 review |
| A.3.3 | Reporting of concerns | 🔴 Not started | | Add AI-specific path |
| A.7.5 | Data provenance | 🟡 Partial | Dataset inventory | Lineage not recoverable |
| A.10.3 | Suppliers | 🔴 Not started | | AI due diligence beyond vendor security |

Copy a blank row:

| Clause/Control | Requirement | Status 🔴🟡🟢 | Evidence | Gap |
|----------------|-------------|---------------|----------|-----|
| | | | | |

---

## SoA row

Every SoA covers **all 38** controls. Applicable? is Yes or No. No without justification is a nonconformity.

| Control ID | Name | Applicable? | Justification | Status | Evidence |
|------------|------|-------------|---------------|--------|----------|
| A.2.2 | AI policy | Yes | Required for the AIMS (5.2 + A.2.2) | Implemented | AI-POL-001 |
| A.7.5 | Data provenance | Yes | Provider trains or fine-tunes models | Partial | — |
| A.6.1.2 | Objectives for responsible development | No | User-only organisation; no AI development | — | Scope 4.3 |
| A.10.3 | Suppliers | Yes | Third-party models, data, or tooling in use | Not started | — |
| A.10.4 | Customers | No | AI used internally; no customer-facing AI | — | Scope 4.3 |

Copy a blank row:

| Control ID | Name | Applicable? | Justification | Status | Evidence |
|------------|------|-------------|---------------|--------|----------|
| | | | | | |

Selectable control IDs (do not add others): A.2.2, A.2.3, A.2.4, A.3.2, A.3.3, A.4.2, A.4.3, A.4.4, A.4.5, A.4.6, A.5.2, A.5.3, A.5.4, A.5.5, A.6.1.2, A.6.1.3, A.6.2.2, A.6.2.3, A.6.2.4, A.6.2.5, A.6.2.6, A.6.2.7, A.6.2.8, A.7.2, A.7.3, A.7.4, A.7.5, A.7.6, A.8.2, A.8.3, A.8.4, A.8.5, A.9.2, A.9.3, A.9.4, A.10.2, A.10.3, A.10.4.

---

## AISIA record skeleton

ISO/IEC 42001 AISIA — Clause **6.1.4** (process), **8.4** (perform), controls **A.5.2–A.5.5**. Not 6.1.2.

```
AI SYSTEM IMPACT ASSESSMENT (AISIA) RECORD — ISO/IEC 42001 Clause 6.1.4 / 8.4

Document ID: AISIA-[XXX]
AI System: [Name]
Assessment Date: [Date]
Assessor(s): [Names and roles]
Next Review Date: [Date]

1. AI SYSTEM DESCRIPTION
   Name: [System name]
   Intended purpose: [What the system is designed to do]
   Input types: [Data inputs]
   Output types: [Decisions, predictions, classifications, content]
   Decision authority: [Advisory / Autonomous / Hybrid]
   Deployment scale: [Number of users, affected individuals]
   Operational environment: [Where and how deployed]

2. AFFECTED POPULATIONS
   Direct users: [Who uses the system]
   Decision subjects: [Who is affected by AI outputs]
   Indirect affected parties: [Communities, markets, other groups]
   Vulnerable groups identified: [Specific vulnerable populations]

3. IMPACT DIMENSION ASSESSMENT
   Nature: [Positive / Negative / Mixed — with details]
   Severity: [Low / Moderate / High — with justification]
   Breadth: [Number and scope of affected individuals]
   Reversibility: [Easily reversible / Partially reversible / Irreversible]
   Consent: [Informed consent / Implicit consent / No consent]
   Human oversight: [Full / Partial / None]
   Recourse: [Available / Limited / None]

4. IMPACT CLASSIFICATION
   Impact level: [Low / Medium / High]
   Justification: [Narrative from dimensions above]

5. REQUIRED CONTROLS
   [A.5, A.8, A.9.2, A.6.2.6–A.6.2.8 depth proportionate to impact level]

6. REVIEW AND APPROVAL
   Assessed by: [Name, role, date]
   Reviewed by: [Name, role, date]
   Approved by: [Name, role, date]
   Next review: [Date and trigger conditions]
```

---

## Stage 1 document checklist

Stage 1 is documentation. Score each item 🔴🟡🟢. Stage 2 (implementation) is a separate pass.

| Item | Citation | Status 🔴🟡🟢 | Evidence | Gap |
|------|----------|---------------|----------|-----|
| AIMS scope + AI system register | 4.3 | | | |
| AI policy signed by top management | 5.2, A.2.2 | | | |
| Roles and reporting of concerns | 5.3, A.3.2, A.3.3 | | | |
| AI risk assessment process and registers | 6.1.2 | | | |
| ISO/IEC 42001 AISIA process and records | 6.1.4, A.5.2–A.5.3 | | | |
| Statement of Applicability (38 controls) | 6.1.3 | | | |
| AI objectives | 6.2 | | | |
| Planning of changes | 6.3 | | | |
| Competence records / matrix | 7.2 | | | |
| Documented-information control | 7.5 | | | |
| Internal audit programme | 9.2 | | | |
| Management review template | 9.3 | | | |

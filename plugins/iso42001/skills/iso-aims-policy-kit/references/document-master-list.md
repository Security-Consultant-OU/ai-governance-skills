# AIMS document-control kit (example scheme)

Not ISO control IDs. These are **organisation document numbers** for an AIMS aligned to ISO/IEC 42001:2023. Map each to a real clause or Annex A control. Do not invent Annex A IDs. A.x.1 is an objective. There is no A.5.8. A.10 is suppliers/customers.

If the user has another numbering scheme, keep theirs and still cite ISO clauses.

Status: 🔴 not started · 🟡 partial · 🟢 implemented.

---

## Master list

| Doc ID | Title | Typical ISO hook | Status 🔴🟡🟢 | Owner | Evidence |
|--------|-------|------------------|---------------|-------|----------|
| AIMS-DOC-02 | Defined scope of the AIMS | 4.3 | | | |
| AIMS-RC-01 | Scope statement record | 4.3 | | | |
| AIMS-DOC-03 | Top-management commitment | 5.1 | | | |
| AIMS-PL-01 | AI policy | 5.2, A.2.2 | | | |
| AIMS-DOC-04 | Statement of Applicability | 6.1.3, Annex A (38) | | | |
| AIMS-DOC-05 | Organisation chart / resource allocation | 5.3, 7.1, A.4.2 | | | |
| AIMS-DOC-06 | Communication matrix | 7.4, A.8 | | | |
| AIMS-DOC-07 | Skills matrix | 7.2, A.4.6 | | | |
| AIMS-OP-01 | List of AIMS processes | 4.4, 8.1 | | | |
| AIMS-SOP-01 | Organisational context | 4.1, 4.2 | | | |
| AIMS-SOP-02 | Risk and opportunity | 6.1.2, 8.2 | | | |
| AIMS-SOP-13 | AI system impact assessment | 6.1.4, 8.4, A.5.2–A.5.5 | | | |
| AIMS-RC-25 | AISIA report form | 8.4, A.5.3 | | | |
| AIMS-SOP-09 | AI development | A.6.1.2–A.6.2.5 (provider) | | | |
| AIMS-SOP-10 | Deployment and testing | A.6.2.4, A.6.2.5 | | | |
| AIMS-SOP-11 | Monitoring and evaluation | A.6.2.6 | | | |
| AIMS-SOP-12 | Decommissioning | A.6.2.5–A.6.2.6, 8.1 (not A.10) | | | |
| AIMS-SOP-14 | Planning and controlling changes | 6.3 | | | |
| AIMS-SOP-15 | Internal audit | 9.2 | | | |
| AIMS-SOP-03 / 04 | Performance monitoring / continual improvement | 9.1, 10.1 | | | |
| AIMS-FR-01 | Stakeholder analysis | 4.2 | | | |
| AIMS-FR-02 | Risk assessment template | 6.1.2 | | | |
| AIMS-FR-03 | Corrective action request | 10.2 | | | |
| AIMS-RC-18 | Management review minutes | 9.3 | | | |
| AIMS-WI-01 | Communicating AI objectives | 6.2 | | | |
| AIMS-WI-02 | Monitoring AI performance | 9.1, A.9.3 | | | |
| AIMS-WI-03 | Processes vs Annex A objectives | Annex A A.x.1 objectives | | | |

---

## Policy pack (minimum)

If the user asks for “policies” without a list, produce these four plus the master-list excerpt.

| Policy | ISO hook | Must include |
|--------|----------|--------------|
| AI policy | 5.2, A.2.2 | Purpose, AI objectives framework, commitment, review (A.2.4) |
| Resources and data | 7.1, A.4, A.7 | Resource inventory duty; data-for-AI rules for providers |
| Development / life cycle | A.6 | Provider gates; user-only orgs mark N/A with 4.3 justification |
| Impact assessment process | 6.1.4, A.5.2 | Triggers, roles, feed into SoA — not a 6.1.2 risk procedure |

Do not use client names (strip any third-party company names from source drafts).

---

## Default output order

1. Role (provider / user / both)
2. Master list scored 🔴🟡🟢
3. Missing Stage 1 documents called out
4. Pointer: AISIA record → `iso-aisia`; register → `iso-ai-system-inventory`; data → `iso-ai-data-inventory`; resources → `iso-ai-resources`; SoA/gap → `iso42001`

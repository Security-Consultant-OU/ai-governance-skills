# CSA AICM / AI-CAIQ artefacts

Cloud Security Alliance **AI Controls Matrix (AICM)** and **AI Consensus Assessment Initiative Questionnaire (AI-CAIQ)**. Control IDs and question text live in the user’s AICM workbook (typical sheets: `AICM`, `AI-CAIQ`, `Implementation Guidelines`, `Auditing Guidelines`, `Scope Applicability (Mappings)`). **Do not invent AICM or CAIQ IDs.** If an ID is not in the workbook, write “not in workbook.”

Status: 🔴 not started · 🟡 partial · 🟢 implemented. This is **not** ISO 42001 SoA and **not** EU CE marking.

Workbook versions seen in the field: AICM v1.0.3 (generated 2025-10-30); AI-CAIQ v1.0.2. Prefer the user’s file date over this note.

---

## Roles

| Role | Typical CSA artefact |
|------|----------------------|
| AI customer | Customer implementation / auditing guidelines; CAIQ as buyer due diligence |
| Application / AI provider | Provider implementation / auditing guidelines; CAIQ as STAR for AI Level 1 evidence |
| Both | Split rows; do not merge customer and provider answers |

STAR for AI Level 1 is a **CAIQ submission**, not an ISO certificate.

---

## CAIQ answer row

| CAIQ ID (from workbook) | Question theme (short) | Answer (Yes / No / N/A) | AICM control ID (from workbook) | Status 🔴🟡🟢 | Evidence | Gap |
|-------------------------|------------------------|-------------------------|---------------------------------|---------------|----------|-----|
| | | | | | | |

---

## Mapping row (optional)

Only when the user asks to map. Pull target IDs from the mapping sheet or from the other skill — do not invent ISO A.x or NIST ME-x.y.

| AICM ID (workbook) | Maps to ISO/IEC 42001? | Maps to NIST AI 600-1? | Notes |
|--------------------|------------------------|------------------------|-------|
| | [control / clause or “not in mapping sheet”] | [subcategory or “not in mapping sheet”] | |

Known mapping workbooks (use if the user has them): AICM to ISO 42001 2023; AICM to NIST 600-1; AICM to BSI AI C4.

---

## Default output order

1. Role (customer / provider / both)
2. Workbook version
3. Scope / applicability from the mapping sheet if present
4. CAIQ answer table (blank IDs until looked up)
5. Gaps 🔴🟡🟢
6. STAR L1: yes/no and missing evidence list

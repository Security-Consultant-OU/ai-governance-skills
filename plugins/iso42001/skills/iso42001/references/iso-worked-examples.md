# ISO/IEC 42001 worked examples

Concrete artefacts for four jobs. IDs used here are real: A.x.1 is never a control; there is no A.5.8; A.10 is suppliers/customers; ISO/IEC 42001 AISIA is Clause 6.1.4 / 8.4.

---

## Contents

- User-only SoA exclusions
- AISIA vs AI risk split
- Stage 1 document list
- Supplier A.10.3 due diligence

---

## 1. User-only SoA exclusions

**Ask:** We only use third-party AI internally (helpdesk copilot, HR screening assist). We do not develop models or sell AI. Draft the SoA exclusions.

**Do:** Treat the organisation as **AI user**. Keep A.2, A.3, A.5, A.8, A.9, A.10.2, A.10.3, plus user-side life-cycle controls A.6.2.6–A.6.2.8 and resource rows A.4.2 / A.4.6. Exclude provider-only development and customer-facing controls **with scope 4.3 justification**.

**Artefact (excerpt — full SoA still lists all 38):**

| Control ID | Name | Applicable? | Justification | Status | Evidence |
|------------|------|-------------|---------------|--------|----------|
| A.2.2 | AI policy | Yes | AIMS requires a signed AI policy | Implemented | AI-POL-001 |
| A.5.2 | AI system impact assessment process | Yes | User must still run ISO/IEC 42001 AISIA (6.1.4) on in-scope systems | Partial | Procedure draft |
| A.6.1.2 | Objectives for responsible development | No | User-only; no AI development or design | — | Scope 4.3 |
| A.6.1.3 | Processes for responsible design and development | No | No in-house design/development lifecycle | — | Scope 4.3 |
| A.6.2.2 | Requirements and specification | No | No provider specification activity | — | Scope 4.3 |
| A.6.2.4 | Verification and validation | No | No in-house model V&V | — | Scope 4.3 |
| A.6.2.6 | Operation and monitoring | Yes | User operates the copilots in production | Partial | Ticket metrics only |
| A.7.5 | Data provenance | No | No training or fine-tuning; no development datasets | — | Scope 4.3 |
| A.9.2 | Processes for responsible use | Yes | User-side acceptable use and oversight | Partial | Acceptable-use page |
| A.10.2 | Allocation of responsibilities | Yes | Provider vs user duties must be allocated | Not started | — |
| A.10.3 | Suppliers | Yes | Third-party model and SaaS suppliers in use | Not started | — |
| A.10.4 | Customers | No | AI used internally; no customer-facing AI product | — | Scope 4.3 |

Do not exclude A.2.2, A.5.2, or A.9.2 because “we only consume APIs.” Do not exclude A.10.3 because a vendor has a SOC 2 report.

---

## 2. AISIA vs AI risk split

**Ask:** We already have a risk register. Is that enough for AISIA?

**Do:** Produce **two** artefacts. Clause **6.1.2 / 8.2** is likelihood × severity (what can go wrong for the organisation). ISO/IEC 42001 AISIA **6.1.4 / 8.4** (A.5.2–A.5.5) is impact on individuals, groups, and society. A merged memo fails both.

**Artefact A — risk register row (6.1.2 / 8.2):**

| Risk ID | AI System | Category | Risk description | Inherent L | Inherent S | Rating | Treatment | Control | Owner |
|---------|-----------|----------|------------------|------------|------------|--------|-----------|---------|-------|
| R-014 | HR screening assist | Model | Biased ranking of applicants from historical hire data | 4 | 4 | 16 High | Modify: remove proxy features; quarterly bias test | A.7.4, A.6.2.6, A.9.2 | HR system owner |

**Artefact B — ISO/IEC 42001 AISIA excerpt (6.1.4 / 8.4):**

| Field | Content |
|-------|---------|
| System | HR screening assist |
| Intended purpose | Rank internal applicants for interview shortlist (advisory) |
| Decision subjects | Employees applying for posted roles |
| Vulnerable groups | Candidates with career gaps; non-native language speakers |
| Nature / severity / reversibility | Mixed; high for livelihood; partially reversible via human shortlist |
| Consent / oversight / recourse | Implicit (employment process); recruiter reviews top-N; internal appeal |
| Impact level | High |
| Controls to deepen | A.5.4, A.5.5, A.8.2, A.8.5, A.9.2 (documented override), A.6.2.6 |

The risk row answers “how likely is discriminatory ranking, and how bad for us?” The AISIA answers “who is affected, how severe for them, and how much A.5/A.8/A.9 depth we owe.” Korea Art. 35 (endeavor + public-procurement preference) is not this record.

---

## 3. Stage 1 document list

**Ask:** What must be on the table for Stage 1?

**Do:** Return a documentation checklist (not Stage 2 operating evidence). Score 🔴🟡🟢.

**Artefact:**

| Item | Citation | Typical evidence |
|------|----------|------------------|
| AIMS scope + AI system register | 4.3 | Approved scope; named systems with owner and purpose |
| AI policy signed by top management | 5.2, A.2.2 | Signed policy; communication record; A.2.4 review date |
| Roles and reporting of concerns | 5.3, A.3.2, A.3.3 | RACI; named AIMS owner; concerns channel procedure |
| AI risk assessment process and registers | 6.1.2 | Methodology; register per in-scope system |
| ISO/IEC 42001 AISIA process and records | 6.1.4, A.5.2–A.5.3 | Procedure; dated AISIA per in-scope system |
| Statement of Applicability (38 controls) | 6.1.3 | SoA with inclusion/exclusion justification |
| AI objectives | 6.2 | Measurable objectives with owners and metrics |
| Planning of changes | 6.3 | Change-planning record for AIMS / model updates |
| Competence | 7.2 | Competence matrix and training records |
| Documented information | 7.5 | Document control procedure and register |
| Internal audit programme | 9.2 | Programme covering clauses and Annex A in the cycle |
| Management review template | 9.3 | Agenda/template with AI-specific inputs |

Stage 2 still needs executed 8.2 / 8.3 / **8.4**, logs (A.6.2.8), supplier records (A.10.2, A.10.3), and audit/review minutes.

---

## 4. Supplier A.10.3 due diligence

**Ask:** We call a third-party LLM API. Security reviewed the vendor last year. Are we done?

**Do:** Treat **A.10.3** as AI-specific due diligence (models, data, tooling), not a generic vendor security review. Pair with **A.10.2** allocation of AISIA, monitoring, and incident response. Accountability stays with the organisation (6.1.3 transfer does not dump the AIMS).

**Artefact — A.10.3 pack:**

| Check | What to collect | Gap if missing |
|-------|-----------------|----------------|
| Supplier inventory | Named model/API, version, subprocessors, data regions | Cannot reconstruct the supply chain (also A.4.4) |
| Intended-use fit | Vendor limits vs our use (A.9.4); prohibited uses | Scope creep without AISIA refresh |
| Data and IP | Training-use of our prompts; retention; output IP | A.7 / contract silence |
| Change notification | Model deprecation, behaviour change, eval delta | Silent model swap; 8.2/8.4 not triggered |
| Incident communication | How the supplier notifies AI harm, bias, or outage | A.8.4 cannot fire |
| Oversight rights | Audit, eval datasets, red-team summaries as contract allows | A.6.2.6 monitoring is theatre |
| Allocation (A.10.2) | Who runs AISIA, who monitors drift, who tells affected people | Accountability gap in the API chain |
| Residual AIMS duties | Our acceptable use (A.9.2), logging (A.6.2.8), concerns (A.3.3) | “Vendor certified” used as SoA exclusion |

Example SoA row:

| Control ID | Name | Applicable? | Justification | Status | Evidence |
|------------|------|-------------|---------------|--------|----------|
| A.10.3 | Suppliers | Yes | LLM API is an AI/tooling supplier | Partial | SOC 2 only; no model-change clause |
| A.10.2 | Allocation of responsibilities | Yes | Provider vs user incident and AISIA duties unallocated | Not started | — |

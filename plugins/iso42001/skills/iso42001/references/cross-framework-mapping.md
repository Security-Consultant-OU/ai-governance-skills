# Cross-framework mapping — ISO/IEC 42001:2023

Map clauses and **real** Annex A IDs (A.x.1 is an objective, not a control). Brazil PL 2338/2023 is **not enacted** as of August 2026 — Brazil cells are indicative of the Senate substitute only. South Korea uses **high-impact AI**, not EU-style high-risk.

---

## Clause-level mapping

| ISO 42001 | EU AI Act | NIST AI RMF 1.0 | South Korea AI Basic Act | Brazil PL 2338 (Senate, not law) | NYC LL144 |
|-----------|-----------|-----------------|--------------------------|----------------------------------|-----------|
| 4.3 Scope + AI register | Art. 6 classification drives regulatory scope | GOVERN 1.6 inventory | High-impact determination (Art. 2(4), Art. 33) | Preliminary assessment Art. 12 | AEDT determination |
| 5.2 AI policy | Art. 9 system (policy artefacts) | GOVERN 1.2 trustworthy-AI characteristics in policies | Ethics / operator measures Art. 34 | Governance Arts. 17–18 | No direct equivalent |
| 5.3 Roles | Arts. 16, 26 | GOVERN 2.1 roles | Operator types Art. 2(7) | desenvolvedor / distribuidor / aplicador Art. 4 | Employer/agency is the responsible party |
| **6.1.2 / 8.2** AI risk | Art. 9 | MAP 1–5, MEASURE | Art. 34 risk management | AIA Arts. 25–27 | Bias audit is not a general risk process |
| **6.1.3** treatment + SoA | Art. 9 risk treatment | MANAGE 1 | Operator measures Art. 34 | Governance design | No SoA analogue |
| **6.1.4 / 8.4** AISIA | Art. 27 FRIA (narrower addressee) | MAP 5 impacts | Art. 35 endeavor + public preference | AIA (high-risk) | Disparate-impact tables only |
| 6.2 Objectives | Art. 9(2) | GOVERN 1.3 risk-tolerance scaling | National strategy context | Development objectives | No equivalent |
| 7.2 Competence | Art. 4 literacy | GOVERN 2.2 training | Operator competence | Competence provisions | No equivalent |
| 8 Operation | Arts. 8–15 | MAP, MEASURE, MANAGE | Arts. 31–34 | Operational duties | Annual audit execution |
| 9 Performance | Art. 72 post-market | MEASURE 3–4, MANAGE 4.1 | Monitoring | Ongoing monitoring | Annual audit cycle |
| 10 Improvement | Arts. 20–21, 72 | MANAGE 4.2–4.3 | Corrective orders Art. 40 | Corrective action | Updated audit after change |

---

## Annex A objective mapping

| ISO 42001 | EU AI Act | NIST AI RMF | Korea | Brazil (Senate) | NYC LL144 |
|-----------|-----------|-------------|-------|-----------------|-----------|
| A.2 Policies (A.2.2–A.2.4) | Art. 9 artefacts | GOVERN 1 | Ethics / policy context | Governance policy | No equivalent |
| A.3 Organisation (A.3.2 roles, **A.3.3 concerns**) | Arts. 16, 26 | GOVERN 2, GOVERN 4.3 incidents | Operator accountability | Responsible parties | Employer is responsible party |
| A.4 Resources (A.4.2–A.4.6) | Art. 9 resources; Art. 4 literacy ≈ A.4.6 | GOVERN 3 | Resource / competence | Resource duties | No equivalent |
| **A.5 Impact assessment (A.5.2–A.5.5)** | Art. 27 FRIA analogue | MAP 5 | Art. 35 | AIA | Employment disparate impact only |
| **A.6 Life cycle (A.6.1.2–A.6.2.8)** | Arts. 8–15; logs Art. 12 ≈ **A.6.2.8**; V&V Art. 9(7)/15 ≈ **A.6.2.4** | MAP, MEASURE, MANAGE | Development / operation | Lifecycle / AIA | Audit methodology ≠ V&V |
| **A.7 Data (A.7.2–A.7.6; provenance A.7.5)** | Art. 10 | MAP 2.3, MEASURE 2.11 | Data quality | Data governance | Historical/test data rules for the audit |
| **A.8 Information (A.8.2–A.8.5)** | Arts. 13, 50; incidents Art. 73 ≈ A.8.4 | GOVERN 4–5, MANAGE 4.3 | Art. 31 transparency | Rights to information | Candidate notice; public summary |
| **A.9 Use (A.9.2 oversight/use, A.9.4 intended use)** | Art. 14 analogue; Art. 26 deployers | MAP 3.5, MANAGE 2.4 | Human oversight Art. 34 | Art. 6 human review (high-risk) | Alternative-process *instructions* if available |
| **A.10 Third parties / customers (A.10.2–A.10.4)** | Arts. 25, 28 | GOVERN 6, MANAGE 3 | Art. 36 domestic representative (foreign operators) | Distributor + value chain | Vendor may commission audit; **employer remains liable** |

There is **no A.10 decommission domain**. Retirement practices sit in A.6 life cycle, A.6.2.8 logs, clause 8.1, and (if using NIST) GOVERN 1.7.

---

## Integration notes

| Observation | Detail |
|-------------|--------|
| EU AI Act | Strongest overlay. 42001 covers management-system evidence for Arts. 8–15 but **not** CE marking, notified-body choice, or the Art. 6(1) Annex I product-law path. Art. 14 is an analogue of A.9.2, not a 42001 control ID. |
| NIST AI RMF | Voluntary vs certifiable. GOVERN ≈ clauses 5–7; MAP ≈ 6.1 + A.5; MEASURE ≈ A.6.2.4 / A.7; MANAGE ≈ clause 8 + A.8–A.10. Use official subcategory labels (GOVERN 1.2, MAP 5.1), not invented hyphens. |
| South Korea | High-impact AI (Art. 2(4)) ≠ Annex III. Art. 35 is endeavor + public procurement preference, not a mandatory FRIA. |
| Brazil | Pending bill. Do not treat 42001 as demonstrating Brazilian statutory compliance. |
| NYC LL144 | Narrow hiring/promotion AEDT law. 42001 is broader; it does **not** replace the DCWP bias-audit method, median scoring-rate formula, or notice rules. |

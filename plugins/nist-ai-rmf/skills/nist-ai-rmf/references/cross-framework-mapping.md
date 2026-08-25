# Cross-framework mapping — NIST AI RMF 1.0

Use **official** subcategory meanings. ISO 42001 IDs match this marketplace’s iso42001 skill (A.x.1 is an objective). Brazil PL 2338/2023 is not enacted as of August 2026. Korea = high-impact AI, not EU high-risk.

---

## Function-level

| NIST function | EU AI Act | ISO/IEC 42001 | Korea AI Basic Act | Brazil PL 2338 (Senate) | NYC LL144 |
|---------------|-----------|---------------|--------------------|-------------------------|-----------|
| GOVERN | Arts. 9, 16, 26 organisational duties | Clauses 5–7, A.2, A.3 | Operator measures Art. 34 | Governance Arts. 17–18 | Employer is the responsible party |
| MAP | Art. 6 classification; Art. 9 risk ID | 6.1.2 risk; 6.1.4 AISIA; A.5 | Art. 33 self-review; Art. 2(4) domains | Arts. 12–16 risk | AEDT determination |
| MEASURE | Arts. 9(7), 10, 15 TEVV | A.6.2.4 V&V; A.7 data | Testing / safety Art. 32–34 | AIA evidence | Bias audit statistics (different method) |
| MANAGE | Arts. 20–21, 72–73 | Clause 8, A.8, A.9, A.10 | Art. 34; incidents to MSIT only where the Act says so | Art. 42 incidents (sectoral) | Annual re-audit; publication |

---

## Selected subcategory mappings

| NIST ID | Official meaning (short) | EU AI Act | ISO 42001 | Notes |
|---------|--------------------------|-----------|-----------|-------|
| GV-1.1 | Legal requirements understood | Art. 2 scope; national law | 4.1–4.2 | |
| GV-1.2 | Trustworthy characteristics in policies | Art. 9 artefacts | 5.2, A.2.2 | **Not** “roles” |
| GV-1.6 | AI inventory | Implicit for providers | 4.3 register | Art. 49 EU database is **not** a general inventory duty |
| GV-1.7 | Safe decommission | No dedicated article | A.6 life cycle + 8.1 | Not ISO A.10 |
| GV-2.1 | Roles documented | Arts. 16, 26 | 5.3, A.3.2 | |
| GV-2.2 | AI risk training | Art. 4 literacy | 7.2–7.3, A.4.6 | |
| GV-6.1 | Third-party / IP risks | Arts. 25, 28 | A.10.2–A.10.3 | |
| GV-6.2 | Contingency for third-party failure | Art. 26 operational | A.10.3 | **Not** appeals/redress |
| MAP-1.5 | Risk tolerances documented | Art. 9 risk acceptance | 6.1.2, 6.1.3 | **Not** deployment context |
| MAP-2.1 | Tasks/methods defined | Annex III use-case vs GPAI | A.6.2.2 | If GAI → 600-1 |
| MAP-5.1 | Impact likelihood × magnitude | Art. 9; Art. 27 if in FRIA scope | 6.1.4, A.5.4–A.5.5 | |
| ME-2.5 | Valid and reliable | Art. 15 | A.6.2.4 | |
| ME-2.6 | Safety | Art. 15 | A.6.2.4, A.6.2.6 | |
| ME-2.7 | Security and resilience | Art. 15 | A.6 + ISO 27001 overlay | |
| ME-2.10 | Privacy | GDPR; Art. 10 | A.7 | |
| ME-2.11 | Fairness and bias | Art. 10(2)(f)–(g) | A.5.4, A.7.4 | NYC audit is a different statistic |
| ME-2.12 | Environmental impact | Recital / GPAI practices | A.5.5 | |
| MG-1.1 | Go/no-go | Conformity / deployment | 8.1, A.6.2.5 | |
| MG-2.4 | Supersede / disengage / deactivate | Art. 20 logs ≠ this; corrective Arts. 21 | A.9.2, A.6.2.6 | |
| MG-3.2 | Monitor pre-trained models | GPAI / value chain | A.10.3, A.4.4 | |
| MG-4.3 | Communicate incidents | Art. 73 | A.8.4 | Korea: not a general MSIT duty for all AI |

---

## Honest gaps vs regulation

| Topic | NIST | Regulation |
|-------|------|------------|
| Legal force | Voluntary | EU, Korea, NYC are binding; Brazil still a bill |
| CE / certification | None | EU conformity; ISO 42001 certification |
| Prohibitions | None | EU Art. 5; Korea Art. 13 analogue in Brazil Senate text |
| Penalties | None | EU turnover caps; Korea KRW 30M band; NYC daily stacking |
| GPAI | 600-1 profile | EU Chapter V; Korea Art. 32 compute gate |

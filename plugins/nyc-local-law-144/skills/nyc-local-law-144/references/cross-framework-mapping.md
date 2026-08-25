# Cross-framework mapping — NYC Local Law 144

ISO Annex A IDs follow ISO/IEC 42001:2023 as used in this marketplace: **A.5 = impact assessment** (A.5.2–A.5.5); **A.6 = life cycle** (A.6.1.2–A.6.2.8); **A.10 = suppliers/customers** (A.10.2–A.10.4). There is **no A.5.8** control and **no A.10 decommission** domain. A.x.1 is an objective, not a selectable control. Brazil cells reflect PL 2338/2023 (Senate substitute), **not enacted** as of August 2026. South Korea uses **high-impact AI**, not EU-style high-risk.

## Requirement-level mapping

| NYC LL144 | EU AI Act | ISO/IEC 42001 | NIST AI RMF 1.0 | South Korea AI Basic Act | Brazil PL 2338 (Senate, not law) |
|-----------|-----------|---------------|-----------------|--------------------------|----------------------------------|
| AEDT determination (6 RCNY § 5-300 three prongs; ML/stats/AI = computer identifies inputs and weights) | Art. 6 + Annex III employment | A.6 life-cycle scope; A.9.4 intended use | MAP 1–2 context and classification | High-impact determination (Art. 2(4)) | High-risk employment classification (indicative) |
| Independent bias audit; scoring rate = share **above sample median**; impact ratio vs highest category; sex + 7 EEO-1 race/ethnicity + **required** intersectional | Art. 10(2)(f)–(g) bias examination (different method) | **A.5** impact assessment (A.5.2–A.5.5), not V&V | MEASURE 2.11 fairness/bias (different statistic) | Non-discrimination / impact-assessment endeavor | Algorithmic impact assessment (indicative) |
| Historical vs test data; no imputation; other-employer data only if contributor or first use | Art. 10 data governance | **A.7** data (incl. A.7.5 provenance) | MAP 2.3 data; ME-2.11 | Data-quality duties | Data-governance provisions (indicative) |
| NYC-resident notice ≥ 10 business days; alternative-process **instructions if available** (not a mandate to offer one) | Arts. 13, 50 transparency; Art. 14 is an analogue of human oversight, not an ISO ID | **A.8** information (A.8.2–A.8.5); **A.9.2** use/oversight | GOVERN 1.2; MANAGE 2 | Transparency obligations | Right to information / human review (indicative) |
| § 20-871(b)(3) type, **source**, retention; 30-day written request; withhold if illegal or LE interference — not a raw-file dump | Art. 13 deployer info; GDPR is a **separate** regime | A.8.2, A.8.5 | GOVERN 1.2 documentation | Transparency | Data/information rights (indicative) |
| Published summary + **distribution date**; hyperlink allowed; ≥ 6 months after last use | Art. 13 information | A.8.5 information for interested parties | GOVERN 1.2 | Public transparency | Governance/transparency (indicative) |
| Employer/agency is the responsible party; vendor may commission an audit but is not liable under LL144 | Arts. 25, 28 value chain | **A.10** suppliers/customers (A.10.2–A.10.4) | GOVERN 6; MANAGE 3 | Operator accountability | Distributor / aplicador roles (indicative) |
| Annual re-audit before continued use | Art. 72 post-market monitoring | A.6.2.6 operation and monitoring | MANAGE 3 | Periodic operator measures | Post-market monitoring (indicative) |
| Retirement / decommission of an AEDT | No dedicated article | Life-cycle practices in **A.6** (not A.10) | GOVERN 1.7 | Not specified as an A.10 analogue | Not specified |

## Key differences

| Dimension | NYC LL144 | Other frameworks |
|-----------|-----------|------------------|
| Scope | NYC job/agency location for audit; NYC **residence** for notice; hiring/promotion screening only | National/international; many use cases |
| Method | Prescribed selection/scoring rates and impact ratios; 7 EEO-1 Component 1 race/ethnicity categories + required intersectional tables | Generally performance-based; no DCWP median formula |
| 4/5ths (0.80) | Disclosure **reference** only — **not** an LL144 pass/fail | NYCHRL / Title VII / EU Art. 10 are separate regimes |
| Enforcement | DCWP; § 20-872: ≤ $500 first violation and each additional **same day**; $500–$1,500 thereafter; **each day** of unlawful use and **each** notice failure is separate. Effective **1 Jan 2023**; enforcement **5 July 2023** | EU: up to 35M EUR / 7% turnover. NIST: voluntary. ISO: certification |
| Alternative process | Instructions to request one **if available**; employer **not required** to provide one | EU Art. 14 and ISO A.9.2 address oversight, not an LL144 alternative-process mandate |
| Data access | Type, source, retention — **not** the candidate’s raw assessment file | GDPR/LGPD access rights are broader and separate |

## Gaps LL144 does not fill

| Gap | Detail |
|-----|--------|
| Narrow geography and use case | Compliance in NYC hiring/promotion does not demonstrate EU, NIST, ISO, Korea, or Brazil coverage |
| No AIMS / RMF | No management-system, AISIA, or GOVERN/MAP/MEASURE/MANAGE program |
| No technical file | Published tables ≠ EU Annex IV or ISO A.6.2.7 technical documentation |
| No incident duty | No Art. 73 / A.8.4 analogue |
| Statistic is not portable | Above-median scoring rate and EEO-1 cuts are DCWP-specific |
| Vendor contracts | A.10 still needed; LL144 liability stays with the employer/agency |

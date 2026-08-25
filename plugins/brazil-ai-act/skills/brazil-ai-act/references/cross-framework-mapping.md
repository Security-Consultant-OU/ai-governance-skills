# Cross-framework mapping — Senate-approved PL 2338/2023 (not enacted)

**Label:** based on Senate-approved PL 2338/2023; not enacted.

ISO 42001 IDs: **A.5** impact, **A.6** life cycle, **A.10** suppliers. A.x.1 is an objective, not a control.

**EU compliance does not cover:** Portuguese Art. 5 information; LGPD overlay; SIA and sectoral high-risk lists; Art. 13 extras (predictive policing/recidivism, CSAM generation, autonomous weapons); GPAI **copyright summary** and rightholder opt-out (Arts. 62–64).

---

## Requirement-level mapping

| Senate PL 2338 (not law) | EU AI Act | ISO 42001 | NIST AI RMF | South Korea AI Basic Act | NYC LL144 |
|--------------------------|-----------|-----------|-------------|--------------------------|-----------|
| Arts. 12–16 risk (optional Art. 12; Art. 13 prohibited; Art. 14 context-specific) | Arts. 5–6, Annex III | **A.5** impact; **A.6** life cycle | MAP (context and risk) | High-impact classification | AEDT determination |
| Arts. 5–6 rights (Art. 5 all systems; Art. 6 high-risk only — not an “8 rights” catalogue) | Arts. 50, 86; Art. 14 oversight | A.8 information; A.9.2 responsible use | GOVERN 1; MAP 5 | Explanation / refusal of AI-only decisions | Candidate/employee notice |
| Arts. 25–27 AIA | Art. 9 risk mgmt; Art. 27 FRIA | **A.5** (A.5.2–A.5.5); 6.1.4 AISIA | MAP 5 | Impact endeavor (not FRIA) | Bias audit ≠ AIA |
| Art. 18 governance split | Arts. 8–15 high-risk | **A.6** life cycle (A.6.1–A.6.2) | GOVERN + MANAGE | Operator measures | — |
| Art. 4 / 16 §3 / 18 §2–§5 value chain | Arts. 16, 25, 26, 28 | **A.10** suppliers/customers (A.10.2–A.10.4) | GOVERN 6 | Actor types + domestic representative | Vendor may audit; employer remains liable |
| Arts. 29–33 GPAI/generative; Arts. 62–64 copyright summary/opt-out | Chapter V GPAI; no equivalent copyright summary | A.7 data; A.8 information | MAP / MEASURE | Transparency / labelling | — |
| Art. 42 incidents → sectoral authority, prazo TBD | Art. 73 serious incidents | A.8.4 incident communication | MANAGE 4 | Incident reporting | — |
| Arts. 45–49 SIA (ANPD coordinates in Senate text; Chamber may change) | AI Office + national authorities | Clause 5 leadership / interested parties | GOVERN | MSIT + National AI Committee | NYC DCWP |
| Art. 50 sanctions (warning; fine ≤ R$ 50m or 2% Brazilian turnover; suspension; sandbox ban) | Arts. 99–101 turnover fines | Loss of certification | None (voluntary) | Administrative fines | Daily civil penalty |

---

## Structural comparison

| Dimension | Senate PL 2338 | EU AI Act | ISO 42001 | NIST AI RMF | SK AI Basic Act | NYC LL144 |
|-----------|----------------|-----------|-----------|-------------|-----------------|-----------|
| Legal nature | **Bill** (not enacted) | Binding regulation | Voluntary certifiable standard | Voluntary framework | National law | City ordinance |
| Scope | AI **in Brazil** (Art. 1); listed exclusions | EU market + extra-territorial output rule | Organisation that chooses AIMS | Organisation that chooses RMF | AI in Korea | AEDTs in NYC hiring |
| Roles | Desenvolvedor, distribuidor, aplicador | Provider, deployer, importer, distributor | Provider / user in Annex A | Not statutory roles | Operator types | Employer / employment agency |
| Regulator | SIA: ANPD coordinates + sectoral + Cria + Cecia (Senate); Chamber may change coordinator | National authorities + AI Office | Certification bodies | None | MSIT | DCWP |
| Rights catalogue | Art. 5 (all) + Art. 6 (high-risk only) | Transparency + Art. 86 explanation | Interested parties | Stakeholders | Explanation, refusal | Notice + alternative process |
| Extra-territoriality | **Not** LGPD-style. Art. 1 is national rules for AI in Brazil | Art. 2(1)(c) output-in-EU | N/A | N/A | Foreign operators targeting Korea | NYC use |

---

## If already aligned with the EU AI Act

| Senate topic | Closest EU hook | Residual gap |
|--------------|-----------------|--------------|
| Risk | Arts. 5–6 | Re-run Art. 12 (optional) + Art. 13 extras + Art. 14 purpose filters + Art. 14 parágrafo único + Art. 16 sectoral lists |
| AIA | Art. 9 + Art. 27 FRIA | AIA to **sectoral authority** (Art. 25 §1); Art. 44 database is authority-run; Art. 23 III is public admin only |
| Rights | Arts. 50, 86, 14 | Portuguese Art. 5 I; LGPD Art. 5 II; no prior-notice right; no general portability right |
| Incidents | Art. 73 | Art. 42 to sectoral authority, **prazo TBD** — not 72 hours to ANPD |
| GPAI | Chapter V | Art. 62 **copyright summary**; Art. 64 opt-out; Art. 19 synthetic identifier |
| Governance overlay | Arts. 8–15 | SIA coordination; Chamber may change ANPD’s coordinator role |

---

## If already aligned with ISO 42001

| Senate topic | ISO hook | Residual gap |
|--------------|----------|--------------|
| AIA | **A.5** impact; 6.1.4 / 8.4 AISIA | Map AISIA content to Art. 25 methodology (fundamental-rights risks/benefits, mitigations, effectiveness) |
| Lifecycle evidence | **A.6** | Split artefacts to Art. 18 I (aplicador) vs II (desenvolvedor) |
| Suppliers / downstream | **A.10** | Brazilian distributor **verification** (Art. 18 §2) and Art. 18 §5 reclassification |
| Rights | A.8, A.9.2 | Art. 5 vs Art. 6 split; Art. 8 disproportionate-oversight alternative |
| Incidents | A.8.4 | Sectoral authority, not a generic “notify the DPA in 72 hours” |

---

## If already aligned with NIST AI RMF

| Senate topic | NIST hook | Residual gap |
|--------------|-----------|--------------|
| Risk | MAP | Mandatory Art. 13/14 categories if enacted — RMF has no statutory tiers |
| AIA | MAP 5 | Produce an Art. 25 AIA document, not only a MAP narrative |
| Rights | GOVERN 1 / MAP 5 | Enforceable Art. 5–6 processes, Portuguese disclosures, LGPD |
| Governance | GOVERN | Formal Art. 18 split; SIA-facing evidence |
| Incidents | MANAGE 4 | Art. 42 sectoral channel once prazo exists |

---

## Key differences to watch

1. **Not law.** Do not certify “Brazil AI Act compliance.”
2. **Roles are not EU roles.** Aplicador ≠ deployer as a defined term.
3. **ANPD is not sole AI regulator** in the Senate text.
4. **Art. 12 is optional.** Starting with a hard EU tree misstates the bill.
5. **Copyright summary (Art. 62)** has **immediate** vacatio if enacted (Art. 80) — EU GPAI documentation does not substitute it.

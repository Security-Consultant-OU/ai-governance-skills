# Annex A controls — ISO/IEC 42001:2023

All **38 controls** across **9 objectives** (A.2–A.10). In each objective, **A.x.1 is the control objective**, not a selectable control. Selectable controls start at **A.x.2**. A.6 has two sub-objectives (A.6.1 management guidance; A.6.2 life cycle), so its IDs are nested (A.6.1.2, A.6.2.2, …).

Paraphrased for SoA and gap assessment. Do not quote ISO text verbatim. Annex B is implementation guidance for these controls.

---

## A.2 — Policies related to AI (3 controls)

| Control ID | Control name | Applies to | What to implement | Common gaps |
|-----------|-------------|-----------|-------------------|------------|
| A.2.2 | AI policy | Both | Written AI policy, approved at the appropriate management level, covering how the organisation develops and/or uses AI, commitment to responsible AI, and a framework for AI objectives | Policy is a generic ethics statement with no AI-specific commitments or objectives |
| A.2.3 | Alignment with other organisational policies | Both | Identify intersecting policies (security, privacy, HR, procurement, risk, ethics) and keep them consistent with the AI policy | Procurement/HR/security policies never updated for AI |
| A.2.4 | Review of the AI policy | Both | Review on a planned cycle and after material change (new use case, incident, regulation) | No review trigger or date |

---

## A.3 — Internal organisation (2 controls)

| Control ID | Control name | Applies to | What to implement | Common gaps |
|-----------|-------------|-----------|-------------------|------------|
| A.3.2 | AI roles and responsibilities | Both | Assign and communicate accountability across the AI life cycle (risk, AISIA, development, oversight, data, suppliers) | Informal ownership; no named AIMS owner |
| A.3.3 | Reporting of concerns | Both | Channel for personnel (and, where appropriate, others) to raise AI concerns without reprisal, with investigation and escalation | No AI-specific reporting path; ethics hotline never covers model behaviour |

---

## A.4 — Resources for AI systems (5 controls)

| Control ID | Control name | Applies to | What to implement | Common gaps |
|-----------|-------------|-----------|-------------------|------------|
| A.4.2 | Resource documentation | Both | Inventory of resources each in-scope AI system depends on, by life-cycle stage | No AI resource inventory; systems cannot be reconstructed after an incident |
| A.4.3 | Data resources | Provider (primarily) | Record datasets used: provenance, category (train/validate/test/production), labelling, purpose, quality, retention, known bias | Data assets not distinguished from general IT data |
| A.4.4 | Tooling resources | Provider (primarily) | Record models, frameworks, libraries, evaluation tools, and provisioning tools | Shadow libraries and unmanaged model hubs |
| A.4.5 | System and computing resources | Provider (primarily) | Record compute, storage, network, hosting, capacity constraints, and environmental impact of infrastructure | Cloud spend tracked; AI-specific capacity and energy not |
| A.4.6 | Human resources | Both | Record people and competencies across the life cycle (developers, operators, domain experts, testers, oversight, decommission) | Competence defined only for developers |

---

## A.5 — Assessing impacts of AI systems (4 controls)

These controls implement AISIA at control level. Clause process: **6.1.4** (plan) and **8.4** (perform). ISO/IEC 42005 is optional methodology depth.

| Control ID | Control name | Applies to | What to implement | Common gaps |
|-----------|-------------|-----------|-------------------|------------|
| A.5.2 | AI system impact assessment process | Both | Repeatable process: triggers, scope, method, roles, and how results feed design, SoA, and review | Ad hoc assessments; no trigger criteria |
| A.5.3 | Documentation of AI system impact assessments | Both | Retain written AISIA records (intended use, foreseeable misuse, affected groups, oversight, mitigations) and update on change | One-time memo; not version-controlled |
| A.5.4 | Impact on individuals or groups | Both | Assess effects on rights, wellbeing, autonomy, fairness, privacy, safety, accessibility; pay attention to vulnerable groups | Privacy-only; no discrimination or autonomy analysis |
| A.5.5 | Societal impacts of AI systems | Both | Assess effects beyond direct subjects: environment, labour, democratic processes, public safety, cultural norms, misuse at scale | Societal dimension skipped |

---

## A.6 — AI system life cycle (9 controls)

### A.6.1 Management guidance (2 controls)

| Control ID | Control name | Applies to | What to implement | Common gaps |
|-----------|-------------|-----------|-------------------|------------|
| A.6.1.2 | Objectives for responsible development | Provider | Measurable responsible-development objectives (fairness, transparency, robustness, privacy, safety) used as design inputs | Aspirational principles with no metrics |
| A.6.1.3 | Processes for responsible design and development | Provider | Documented life-cycle process: stages, testing, human oversight gates, data rules, release criteria, change control | Process exists for software SDLC but not AI-specific gates |

### A.6.2 Life cycle (7 controls)

| Control ID | Control name | Applies to | What to implement | Common gaps |
|-----------|-------------|-----------|-------------------|------------|
| A.6.2.2 | Requirements and specification | Provider | Functional and non-functional requirements including responsible-AI constraints; change-controlled | Fairness/oversight omitted from specs |
| A.6.2.3 | Documentation of design and development | Provider | Traceable record of design decisions, architecture, model versions, data assumptions | Cannot reproduce a released model |
| A.6.2.4 | Verification and validation | Provider | Verify (built right) and validate (right thing): performance, bias, robustness, release thresholds | Accuracy-only testing |
| A.6.2.5 | Deployment | Provider | Written deployment plan, approvals, rollback; extra care when prod differs from training environment | Standard CI/CD with no AI sign-off |
| A.6.2.6 | Operation and monitoring | Both | Day-to-day operation: performance and drift monitoring, poisoning/abuse threats, updates, user support, ownership | Uptime monitored; drift and bias not |
| A.6.2.7 | Technical documentation | Both | Audience-specific technical information: intended purpose, limits, assumptions, monitoring | Engineer wiki only; no user-facing limits |
| A.6.2.8 | Recording of event logs | Both | Event logs sufficient for investigation, audit, and drift detection; retention and access defined | Generic app logs; cannot reconstruct AI decisions |

Human oversight and decommission are **not** separate Annex A IDs. Implement oversight under **A.9.2** (responsible use) and life-cycle gates in **A.6.1.3 / A.6.2.5–A.6.2.6**. Implement retirement planning under **A.6.2.5–A.6.2.6**, **A.6.2.8**, clause **8.1**, and **Govern 1.7** if also using NIST AI RMF.

---

## A.7 — Data for AI systems (5 controls)

| Control ID | Control name | Applies to | What to implement | Common gaps |
|-----------|-------------|-----------|-------------------|------------|
| A.7.2 | Data for development and enhancement | Provider | Data-management process for development data: privacy/security, representativeness, provenance, integrity | General data policy with no AI training rules |
| A.7.3 | Acquisition of data | Provider | Document source, selection rationale, rights, known biases, metadata for each dataset | Scraped or vendor data with no legal-basis record |
| A.7.4 | Quality of data for AI systems | Provider | Explicit quality criteria (accuracy, completeness, currency, representativeness) tested before use | Informal spot checks |
| A.7.5 | Data provenance | Provider | Recoverable lineage: creation, updates, transformations, validation, transfers | Cannot say how a training set was built |
| A.7.6 | Data preparation | Provider | Allowed cleaning, labelling, augmentation methods; record the method and rationale | Unrepeatable notebooks; no inter-annotator checks |

---

## A.8 — Information for interested parties (4 controls)

| Control ID | Control name | Applies to | What to implement | Common gaps |
|-----------|-------------|-----------|-------------------|------------|
| A.8.2 | System documentation and information for users | Both | Information users need to operate the system safely: capabilities, limits, expected I/O, failure modes, oversight options | Technical docs only; no plain-language user information |
| A.8.3 | External reporting | Both | Channel for affected parties to report problems or unintended consequences, with triage and resolution | No public/customer reporting path for AI harm |
| A.8.4 | Communication of incidents | Both | Pre-planned incident communication: what, who, how fast, which channel; align with legal notification duties | IT incident process never covers bias or model failure |
| A.8.5 | Information for interested parties | Both | What is shared proactively with regulators, partners, customers, or the public, and how | No communication plan beyond incidents |

---

## A.9 — Use of AI systems (3 controls)

| Control ID | Control name | Applies to | What to implement | Common gaps |
|-----------|-------------|-----------|-------------------|------------|
| A.9.2 | Processes for responsible use | User (primarily) | How the system is used: acceptable use, human oversight, escalation, pause/stop conditions, operator training | Oversight is informal; no override evidence |
| A.9.3 | Objectives for responsible use | User (primarily) | Measurable operational objectives (fairness thresholds, oversight rates, safety tolerances) | No use-side KPIs |
| A.9.4 | Intended use of the AI system | Both | Documented intended purpose; detect and reassess scope creep | Tool reused in a new context without AISIA |

---

## A.10 — Third-party and customer relationships (3 controls)

| Control ID | Control name | Applies to | What to implement | Common gaps |
|-----------|-------------|-----------|-------------------|------------|
| A.10.2 | Allocation of responsibilities | Both | Who owns AISIA, monitoring, and incident response across provider, user, partners, customers | Accountability gaps in SaaS / API chains |
| A.10.3 | Suppliers | Both | Due diligence, contracts, and ongoing oversight of AI, data, model, and tooling suppliers | Standard vendor security review only |
| A.10.4 | Customers | Provider | Customer information, customer responsible-use obligations, and customer incident/feedback handling | Customers not told limits or their duties |

---

## Provider vs user applicability

| Domain | Controls | Provider | User |
|--------|----------|----------|------|
| A.2 Policies | 3 | All | All |
| A.3 Internal organisation | 2 | All | All |
| A.4 Resources | 5 | All | A.4.2, A.4.6 typically |
| A.5 Impact assessment | 4 | All | All |
| A.6 Life cycle | 9 | All | A.6.2.6, A.6.2.7, A.6.2.8 typically |
| A.7 Data | 5 | All | Limited unless the user trains or fine-tunes |
| A.8 Information | 4 | All | All |
| A.9 Use | 3 | A.9.4 | All |
| A.10 Third parties / customers | 3 | All | A.10.2, A.10.3 typically |
| **Total** | **38** | | |

**Complete ID list:** A.2.2, A.2.3, A.2.4, A.3.2, A.3.3, A.4.2, A.4.3, A.4.4, A.4.5, A.4.6, A.5.2, A.5.3, A.5.4, A.5.5, A.6.1.2, A.6.1.3, A.6.2.2, A.6.2.3, A.6.2.4, A.6.2.5, A.6.2.6, A.6.2.7, A.6.2.8, A.7.2, A.7.3, A.7.4, A.7.5, A.7.6, A.8.2, A.8.3, A.8.4, A.8.5, A.9.2, A.9.3, A.9.4, A.10.2, A.10.3, A.10.4

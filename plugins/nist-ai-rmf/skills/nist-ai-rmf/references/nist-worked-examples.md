# NIST AI RMF worked examples

Self-contained examples. Official outcomes are from NIST AI 100-1. Scoring is Current vs Target (🔴 not started / 🟡 partial / 🟢 implemented), not a 1–5 NIST maturity scale.

Do not invent Playbook Action IDs, subcategory IDs, or article/control IDs. There is no MAP-2.4. There is no MG-3.3. MEASURE 2 is ME-2.1–ME-2.13. If a Playbook Action ID is not stored here, say it is not in context and use https://airc.nist.gov/airmf-resources/playbook/.

---

## Example 1 — Current vs Target Profile for one system

**User asks:** Produce a Current vs Target Profile for HireScreen v3.

**Intake:** HireScreen v3 ranks internal applicants from resumes and a structured score. Lifecycle: **deploy**. Role: design / develop / **deploy**. Generative: **no** (MAP-2.1 = classifier, not GAI). Document type omitted → default **Current vs Target Profile**.

**Header**

- System: HireScreen v3
- Lifecycle: deploy
- Generative: no (NIST AI 600-1 overlay omitted)
- Scoring: Current vs Target 🔴🟡🟢 — not NIST maturity

**Profile table (selected in-scope rows; a full profile uses all relevant of the 72 official outcomes)**

| Subcategory | Official outcome | Current 🔴🟡🟢 | Target | Evidence | Gap |
|-------------|------------------|----------------|--------|----------|-----|
| GV-1.2 | The characteristics of trustworthy AI are integrated into organizational policies, processes, procedures, and practices. | 🟡 | 🟢 | AI policy v2 names validity and fairness | Safe, privacy, and explainability not in SDLC gates |
| GV-1.6 | Mechanisms are in place to inventory AI systems and are resourced according to organizational risk priorities. | 🟢 | 🟢 | Inventory row: HireScreen v3, owner TA Ops | — |
| GV-2.1 | Roles and responsibilities and lines of communication related to mapping, measuring, and managing AI risks are documented and are clear to individuals and teams throughout the organization. | 🟡 | 🟢 | Named model owner | No RACI for GOVERN/MAP/MEASURE/MANAGE |
| GV-5.1 | Organizational policies and practices are in place to collect, consider, prioritize, and integrate feedback from those external to the team that developed or deployed the AI system regarding the potential individual and societal impacts related to AI risks. | 🔴 | 🟢 | — | No candidate or recruiter feedback intake |
| GV-6.1 | Policies and procedures are in place that address AI risks associated with third-party entities, including risks of infringement of a third-party’s intellectual property or other rights. | 🟡 | 🟢 | Vendor DPA on file | No model-card / IP review of the ranking library |
| MAP-1.1 | Intended purposes, potentially beneficial uses, context-specific laws, norms and expectations, and prospective settings in which the AI system will be deployed are understood and documented. | 🟡 | 🟢 | Purpose note in README | Users, harms, TEVV metrics not in a context dossier |
| MAP-1.5 | Organizational risk tolerances are determined and documented. | 🔴 | 🟢 | — | No tolerance; go-live used engineering judgment |
| MAP-2.1 | The specific tasks and methods used to implement the tasks that the AI system will support are defined (e.g., classifiers, generative models, recommenders). | 🟢 | 🟢 | Gradient-boosted ranker; not generative | — |
| MAP-2.2 | Information about the AI system’s knowledge limits and how system output may be utilized and overseen by humans is documented. | 🟡 | 🟢 | Recruiters see a score | Knowledge limits and override rules undocumented |
| MAP-5.1 | Likelihood and magnitude of each identified impact (both potentially beneficial and harmful) based on expected use, past uses of AI systems in similar contexts, public incident reports, feedback from those external to the team that developed or deployed the AI system, or other data are identified and documented. | 🔴 | 🟢 | — | No likelihood × magnitude register |
| ME-2.5 | The AI system to be deployed is demonstrated to be valid and reliable. Limitations of the generalizability beyond the conditions under which the technology was developed are documented. | 🟢 | 🟢 | Holdout AUC; documented OOD on new job families | — |
| ME-2.6 | The AI system is evaluated regularly for safety risks – as identified in the MAP function. The AI system to be deployed is demonstrated to be safe, its residual negative risk does not exceed the risk tolerance, and it can fail safely, particularly if made to operate beyond its knowledge limits. | 🔴 | 🟢 | — | No safety case; MAP-1.5 tolerance missing so residual risk cannot be compared |
| ME-2.11 | Fairness and bias – as identified in the MAP function – are evaluated and results are documented. | 🟡 | 🟢 | One 2024 slice by gender | Not recurring; no intersectional groups; MAP did not specify groups |
| MG-1.1 | A determination is made as to whether the AI system achieves its intended purposes and stated objectives and whether its development or deployment should proceed. | 🟡 | 🟢 | Informal launch email | No go/no-go using MAP and MEASURE outputs |
| MG-2.4 | Mechanisms are in place and applied, and responsibilities are assigned and understood, to supersede, disengage, or deactivate AI systems that demonstrate performance or outcomes inconsistent with intended use. | 🔴 | 🟢 | — | No deactivate authority |
| MG-4.1 | Post-deployment AI system monitoring plans are implemented, including mechanisms for capturing and evaluating input from users and other relevant AI actors, appeal and override, decommissioning, incident response, recovery, and change management. | 🔴 | 🟢 | — | No monitoring plan covering appeal, decommission, or IR |

**Gap list (GOVERN first)**

| Priority | ID | Gap |
|----------|----|-----|
| High | MAP-1.5 | Document risk tolerance before any further go-live |
| High | MAP-5.1 | Build impact register (likelihood × magnitude) |
| High | ME-2.6 | Safety case against MAP risks and fail-safe beyond knowledge limits |
| High | MG-2.4 | Assign deactivate authority |
| Medium | GV-1.2 | Put remaining NIST AI 100-1 characteristics into SDLC gates |
| Medium | ME-2.11 | Recurring fairness evaluation on MAP-identified groups |
| Medium | MG-4.1 | Monitoring plan with appeal, IR, change, decommission |
| Low | GV-5.1 | External feedback intake from candidates/recruiters |

**Generative overlay:** omitted (MAP-2.1 is not generative).

**MANAGE next actions:** mitigate MAP-1.5, MAP-5.1, ME-2.6, ME-2.11, MG-2.4, MG-4.1; do not accept High residual risk without MG-1.4 documentation. Playbook Action IDs: **not in context** — confirm suggested actions at the NIST AI RMF Playbook.

---

## Example 2 — NIST AI 600-1 generative overlay (12 GAI risks → Core IDs)

**User asks:** Overlay NIST AI 600-1 on DevAssist, our internal code-generation chatbot.

**Intake:** DevAssist (RAG + code-gen LLM). Lifecycle: **deploy**. MAP-2.1: generative. Apply the 12 NIST AI 600-1 §2 risks to existing Core IDs. Do not invent Core IDs or 600-1 Action IDs.

**Header**

- System: DevAssist
- Lifecycle: deploy
- Generative: yes — NIST AI 600-1 overlay required
- Scoring: Current vs Target 🔴🟡🟢

**GAI 12-risk overlay**

| GAI risk | Plausible in this context? | Core IDs | Current 🔴🟡🟢 | Target | Evidence / gap |
|----------|----------------------------|----------|----------------|--------|----------------|
| CBRN information or capabilities | No — internal software assistant, no CBRN domain | MAP-5, ME-2.6, ME-2.7, MG-1 | 🟢 | 🟢 | Documented out of domain in MAP-5.1 |
| Confabulation | Yes — invents APIs, licenses, and CVE numbers | ME-2.5, ME-2.9, MG-2.4 | 🟡 | 🟢 | Citation UI exists; no fail-safe when confabulation rate spikes |
| Dangerous, violent, or hateful content | Low — enterprise filter on; still possible via jailbreak | ME-2.6, ME-2.8, MG-4.3 | 🟡 | 🟢 | Filter logs; no incident comms to affected staff (MG-4.3) |
| Data privacy | Yes — RAG over private repos | ME-2.10, GV-6, MAP-4 | 🟡 | 🟢 | Repo ACL mirrored; no membership-inference or leakage TEVV |
| Environmental impacts | Yes — high token volume | ME-2.12, MAP-3.2 | 🔴 | 🟡 | No energy/water/compute account; target 🟡 justified for internal tool |
| Harmful bias or homogenization | Yes — code and comment stereotypes; homogenised style | ME-2.11, MAP-5, GV-3 | 🔴 | 🟢 | No fairness or homogenization evaluation |
| Human-AI configuration | Yes — automation bias on suggested patches | MAP-2.2, MAP-3.5, GV-3.2 | 🟡 | 🟢 | “Review before merge” banner; no proficiency standard (MAP-3.4) |
| Information integrity | Yes — can fabricate changelog or licence text | ME-2.8, MAP-5, MG-4.3 | 🟡 | 🟢 | Provenance tags on RAG chunks; generated text unmarked in PRs |
| Information security | Yes — prompt injection on RAG; secret exfil | ME-2.7, GV-6, MG-3 | 🟡 | 🟢 | Basic injection tests; no weight/supply-chain monitor (MG-3.2) |
| Intellectual property | Yes — reproduction of third-party code | GV-6.1, MAP-4.1 | 🟡 | 🟢 | Licence allow-list; no output-side IP scan |
| Obscene, degrading, and/or abusive content | Low — enterprise filter | ME-2.6, MG-1.1, MG-2.4 | 🟢 | 🟢 | Filter + go/no-go includes content policy |
| Value chain and component integration | Yes — hosted foundation model + vector DB | GV-6, MAP-4, MG-3.1, MG-3.2 | 🟡 | 🟢 | Vendor DPA; pre-trained model versions not monitored (MG-3.2) |

**Linked Core profile rows (illustrative)**

| Subcategory | Official outcome | Current 🔴🟡🟢 | Target | Evidence | Gap |
|-------------|------------------|----------------|--------|----------|-----|
| MAP-2.1 | The specific tasks and methods used to implement the tasks that the AI system will support are defined (e.g., classifiers, generative models, recommenders). | 🟢 | 🟢 | Task card: code generation + RAG | — |
| ME-2.5 | The AI system to be deployed is demonstrated to be valid and reliable. Limitations of the generalizability beyond the conditions under which the technology was developed are documented. | 🟡 | 🟢 | Human eval on 50 prompts | Confabulation rate not a deployment gate |
| ME-2.6 | The AI system is evaluated regularly for safety risks – as identified in the MAP function. The AI system to be deployed is demonstrated to be safe, its residual negative risk does not exceed the risk tolerance, and it can fail safely, particularly if made to operate beyond its knowledge limits. Safety metrics reflect system reliability and robustness, real-time monitoring, and response times for AI system failures. | 🟡 | 🟢 | Content filter | No fail-safe beyond knowledge limits |
| ME-2.11 | Fairness and bias – as identified in the MAP function – are evaluated and results are documented. | 🔴 | 🟢 | — | Homogenization / stereotype eval missing |
| MG-3.2 | Pre-trained models which are used for development are monitored as part of AI system regular monitoring and maintenance. | 🔴 | 🟢 | — | Upstream model version and known issues not tracked |
| MG-2.4 | Mechanisms are in place and applied, and responsibilities are assigned and understood, to supersede, disengage, or deactivate AI systems that demonstrate performance or outcomes inconsistent with intended use. | 🔴 | 🟢 | — | No deactivate path when confabulation spikes |

**600-1 Action IDs** (for example GV-1.1-001): **not in context**. Quote them from NIST AI 600-1 or say they are not stored here. Do not fabricate them.

---

## Example 3 — MEASURE 2 fairness and safety, not accuracy-only

**User asks:** We already report accuracy for PayPredict. Are we done with MEASURE?

**Intake:** PayPredict recommends consumer credit limits. Lifecycle: **deploy**. MAP-2.1: tabular recommender (not generative). Current TEVV: holdout accuracy and calibration (ME-2.5 only).

**Skill does:** Score MEASURE 2 across **ME-2.1–ME-2.13**. Call out that ME-2.5 (valid and reliable) does not satisfy ME-2.6 (safe) or ME-2.11 (fairness and bias). Log characteristics MAP identified but MEASURE skipped (ME-1.1).

**MEASURE 2 coverage**

| Subcategory | Official outcome | Current 🔴🟡🟢 | Target | Evidence | Gap |
|-------------|------------------|----------------|--------|----------|-----|
| ME-2.1 | Test sets, metrics, and details about the tools used during TEVV are documented. | 🟡 | 🟢 | Accuracy notebook | No TEVV toolkit register covering fairness or safety tools |
| ME-2.2 | Evaluations involving human subjects meet applicable requirements (including human subject protection) and are representative of the relevant population. | 🟢 | 🟢 | No human-subjects study in TEVV | — |
| ME-2.3 | AI system performance or assurance criteria are measured qualitatively or quantitatively and demonstrated for conditions similar to deployment setting(s). Measures are documented. | 🟡 | 🟢 | Holdout from 2023 book | Production mix has new products; not production-like |
| ME-2.4 | The functionality and behavior of the AI system and its components – as identified in the MAP function – are monitored when in production. | 🟡 | 🟢 | Latency dashboard | Mapped components (bureau feature, override) not monitored |
| ME-2.5 | The AI system to be deployed is demonstrated to be valid and reliable. Limitations of the generalizability beyond the conditions under which the technology was developed are documented. | 🟢 | 🟢 | Accuracy, calibration, documented OOD on thin-file | — |
| ME-2.6 | The AI system is evaluated regularly for safety risks – as identified in the MAP function. The AI system to be deployed is demonstrated to be safe, its residual negative risk does not exceed the risk tolerance, and it can fail safely, particularly if made to operate beyond its knowledge limits. Safety metrics reflect system reliability and robustness, real-time monitoring, and response times for AI system failures. | 🔴 | 🟢 | — | MAP listed over-limit harm; no safety case, no fail-safe when knowledge limits exceeded |
| ME-2.7 | AI system security and resilience – as identified in the MAP function – are evaluated and documented. | 🟡 | 🟢 | AppSec scan | No poisoning / integrity test on bureau features |
| ME-2.8 | Risks associated with transparency and accountability – as identified in the MAP function – are examined and documented. | 🔴 | 🟢 | — | No transparency measures for adverse action |
| ME-2.9 | The AI model is explained, validated, and documented, and AI system output is interpreted within its context – as identified in the MAP function – to inform responsible use and governance. | 🟡 | 🟢 | SHAP on 20 features | No contextual interpretation guide for underwriters |
| ME-2.10 | Privacy risk of the AI system – as identified in the MAP function – is examined and documented. | 🟡 | 🟢 | Minimisation memo | No leakage / membership TEVV |
| ME-2.11 | Fairness and bias – as identified in the MAP function – are evaluated and results are documented. | 🔴 | 🟢 | — | MAP-5 flagged group harm; no fairness metrics by relevant groups |
| ME-2.12 | Environmental impact and sustainability of AI model training and management activities – as identified in the MAP function – are assessed and documented. | 🔴 | 🟡 | — | Not measured; ME-1.1 log + justified 🟡 if org tolerance allows |
| ME-2.13 | Effectiveness of the employed TEVV metrics and processes in the MEASURE function are evaluated and documented. | 🔴 | 🟢 | — | No meta-evaluation of the measurement programme |

**ME-1.1 not-measured log**

| Characteristic MAP said matters | MEASURE row | Status |
|---------------------------------|-------------|--------|
| Safe (over-limit, fail-safe) | ME-2.6 | 🔴 not measured |
| Fair — harmful bias managed | ME-2.11 | 🔴 not measured |
| Privacy-enhanced | ME-2.10 | 🟡 partial |
| Valid and reliable | ME-2.5 | 🟢 measured |

**Verdict:** Accuracy (ME-2.5) is not MEASURE 2. PayPredict is not “done.” High gaps: **ME-2.6** and **ME-2.11**. Do not collapse fairness or safety into ME-2.5. Playbook Action IDs for ME-2.6 / ME-2.11: **not in context**.

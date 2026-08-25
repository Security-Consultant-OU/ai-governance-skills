# MEASURE function — NIST AI RMF 1.0 (Table 3)

Official subcategory outcomes from NIST AI 100-1. **4 categories, 22 subcategories**. MEASURE 2 has **13** TEVV rows (ME-2.1–ME-2.13). Do not collapse fairness, privacy, safety, or environment into other IDs.

---

## MEASURE 1 — Appropriate methods and metrics (3)

| ID | Official outcome | Suggested actions |
|----|------------------|-------------------|
| ME-1.1 | Approaches and metrics for measurement of AI risks enumerated during the MAP function are selected for implementation starting with the most significant AI risks. The risks or trustworthiness characteristics that will not – or cannot – be measured are properly documented. | Metric plan; explicit “not measured” log. |
| ME-1.2 | Appropriateness of AI metrics and effectiveness of existing controls are regularly assessed and updated, including reports of errors and potential impacts on affected communities. | Metric review cycle; community-impact error reports. |
| ME-1.3 | Internal experts who did not serve as front-line developers for the system and/or independent assessors are involved in regular assessments and updates. Domain experts, users, AI actors external to the team that developed or deployed the AI system, and affected communities are consulted in support of assessments as necessary per organizational risk tolerance. | Independent / non-developer review. **Not** “combatants.” |

---

## MEASURE 2 — Evaluated for trustworthy characteristics (13)

| ID | Official outcome | Suggested actions |
|----|------------------|-------------------|
| ME-2.1 | Test sets, metrics, and details about the tools used during TEVV are documented. | TEVV toolkit register. |
| ME-2.2 | Evaluations involving human subjects meet applicable requirements (including human subject protection) and are representative of the relevant population. | IRB/ethics and sampling plan — **not** “red-teaming.” |
| ME-2.3 | AI system performance or assurance criteria are measured qualitatively or quantitatively and demonstrated for conditions similar to deployment setting(s). Measures are documented. | Production-like test conditions. |
| ME-2.4 | The functionality and behavior of the AI system and its components – as identified in the MAP function – are monitored when in production. | Production monitoring of mapped components. |
| ME-2.5 | The AI system to be deployed is demonstrated to be valid and reliable. Limitations of the generalizability beyond the conditions under which the technology was developed are documented. | Validity/reliability evidence + OOD limits. |
| ME-2.6 | The AI system is evaluated regularly for safety risks – as identified in the MAP function. The AI system to be deployed is demonstrated to be safe, its residual negative risk does not exceed the risk tolerance, and it can fail safely, particularly if made to operate beyond its knowledge limits. Safety metrics reflect system reliability and robustness, real-time monitoring, and response times for AI system failures. | Safety case; fail-safe beyond knowledge limits. |
| ME-2.7 | AI system security and resilience – as identified in the MAP function – are evaluated and documented. | Adversarial, poisoning, availability, integrity tests. |
| ME-2.8 | Risks associated with transparency and accountability – as identified in the MAP function – are examined and documented. | Transparency/accountability measures. |
| ME-2.9 | The AI model is explained, validated, and documented, and AI system output is interpreted within its context – as identified in the MAP function – to inform responsible use and governance. | Explanation + contextual interpretation evidence. |
| ME-2.10 | Privacy risk of the AI system – as identified in the MAP function – is examined and documented. | Privacy TEVV (membership inference, leakage, minimisation). |
| ME-2.11 | Fairness and bias – as identified in the MAP function – are evaluated and results are documented. | Fairness metrics by relevant groups; document limits. |
| ME-2.12 | Environmental impact and sustainability of AI model training and management activities – as identified in the MAP function – are assessed and documented. | Energy/water/compute impact of training and operations. |
| ME-2.13 | Effectiveness of the employed TEVV metrics and processes in the MEASURE function are evaluated and documented. | Meta-evaluation of the measurement programme. |

---

## MEASURE 3 — Tracking identified AI risks over time (3)

| ID | Official outcome | Suggested actions |
|----|------------------|-------------------|
| ME-3.1 | Approaches, personnel, and documentation are in place to regularly identify and track existing, unanticipated, and emergent AI risks based on factors such as intended and actual performance in deployed contexts. | Risk tracker comparing intended vs actual. |
| ME-3.2 | Risk tracking approaches are considered for settings where AI risks are difficult to assess using currently available measurement techniques or where metrics are not yet available. | Qualitative / sentinel tracking where metrics do not exist. |
| ME-3.3 | Feedback processes for end users and impacted communities to report problems and appeal system outcomes are established and integrated into AI system evaluation metrics. | Appeal/report channel feeding metrics. |

---

## MEASURE 4 — Feedback about efficacy of measurement (3)

| ID | Official outcome | Suggested actions |
|----|------------------|-------------------|
| ME-4.1 | Measurement approaches for identifying AI risks are connected to deployment context(s) and informed through consultation with domain experts and other end users. Approaches are documented. | Context-calibrated metrics. |
| ME-4.2 | Measurement results regarding AI system trustworthiness in deployment context(s) and across the AI lifecycle are informed by input from domain experts and relevant AI actors to validate whether the system is performing consistently as intended. Results are documented. | External validation of trustworthiness results. |
| ME-4.3 | Measurable performance improvements or declines based on consultations with relevant AI actors, including affected communities, and field data about context-relevant risks and trustworthiness characteristics are identified and documented. | Trend log of improvement/decline. |

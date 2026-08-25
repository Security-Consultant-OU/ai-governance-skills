# GOVERN function — NIST AI RMF 1.0 (Table 1)

Official subcategory outcomes from NIST AI 100-1. Short labels are for tables only; **cite the official outcome**. Suggested actions are implementation hints, not Playbook Action IDs. For Playbook text, use the [NIST AI RMF Playbook](https://airc.nist.gov/airmf-resources/playbook/) and do not invent Action IDs.

Shorthand: GV-1.1 = GOVERN 1.1. Counts: **6 categories, 19 subcategories**.

---

## GOVERN 1 — Policies, processes, procedures, and practices

Policies, processes, procedures, and practices across the organization related to mapping, measuring, and managing AI risks are in place, transparent, and implemented effectively.

| ID | Official outcome | Suggested actions |
|----|------------------|-------------------|
| GV-1.1 | Legal and regulatory requirements involving AI are understood, managed, and documented. | Maintain a legal inventory (EU AI Act, sectoral law, NYC LL144, etc.) mapped to systems; review on change. |
| GV-1.2 | The characteristics of trustworthy AI are integrated into organizational policies, processes, procedures, and practices. | Embed the seven trustworthy characteristics into policy and SDLC gates — not a “roles” control. |
| GV-1.3 | Processes, procedures, and practices are in place to determine the needed level of risk management activities based on the organization's risk tolerance. | Document risk tolerance and scale TEVV effort to it. |
| GV-1.4 | The risk management process and its outcomes are established through transparent policies, procedures, and other controls based on organizational risk priorities. | Publish how risks are identified, escalated, and accepted. |
| GV-1.5 | Ongoing monitoring and periodic review of the risk management process and its outcomes are planned and organizational roles and responsibilities clearly defined, including determining the frequency of periodic review. | Set review cadence and owners for the *process*, not only for systems. |
| GV-1.6 | Mechanisms are in place to inventory AI systems and are resourced according to organizational risk priorities. | Live AI inventory with owner, purpose, data, and risk tier. |
| GV-1.7 | Processes and procedures are in place for decommissioning and phasing out AI systems safely and in a manner that does not increase risks or decrease the organization’s trustworthiness. | Retirement runbook: data, model artefacts, user notice, residual risk. |

---

## GOVERN 2 — Accountability structures

Accountability structures are in place so that the appropriate teams and individuals are empowered, responsible, and trained for mapping, measuring, and managing AI risks.

| ID | Official outcome | Suggested actions |
|----|------------------|-------------------|
| GV-2.1 | Roles and responsibilities and lines of communication related to mapping, measuring, and managing AI risks are documented and are clear to individuals and teams throughout the organization. | RACI for GOVERN/MAP/MEASURE/MANAGE; named system owners. |
| GV-2.2 | The organization’s personnel and partners receive AI risk management training to enable them to perform their duties and responsibilities consistent with related policies, procedures, and agreements. | Role-based training; include suppliers who operate in-scope systems. |
| GV-2.3 | Executive leadership of the organization takes responsibility for decisions about risks associated with AI system development and deployment. | Leadership sign-off on residual risk and go/no-go. |

---

## GOVERN 3 — Workforce DEI and accessibility

Workforce diversity, equity, inclusion, and accessibility processes are prioritized in the mapping, measuring, and managing of AI risks throughout the lifecycle.

| ID | Official outcome | Suggested actions |
|----|------------------|-------------------|
| GV-3.1 | Decision-making related to mapping, measuring, and managing AI risks throughout the lifecycle is informed by a diverse team (e.g., diversity of demographics, disciplines, experience, expertise, and backgrounds). | Staff risk reviews with mixed discipline and demographic representation; record who participated. |
| GV-3.2 | Policies and procedures are in place to define and differentiate roles and responsibilities for human-AI configurations and oversight of AI systems. | Define human-in-the-loop / on-the-loop / in-command patterns per system. |

---

## GOVERN 4 — Culture that considers and communicates AI risk

Organizational teams are committed to a culture that considers and communicates AI risk.

| ID | Official outcome | Suggested actions |
|----|------------------|-------------------|
| GV-4.1 | Organizational policies and practices are in place to foster a critical thinking and safety-first mindset in the design, development, deployment, and uses of AI systems to minimize potential negative impacts. | Blameless incident culture; safety review before launch. |
| GV-4.2 | Organizational teams document the risks and potential impacts of the AI technology they design, develop, deploy, evaluate, and use, and they communicate about the impacts more broadly. | Impact notes in design docs; share beyond the build team. |
| GV-4.3 | Organizational practices are in place to enable AI testing, identification of incidents, and information sharing. | Test windows, incident taxonomy, internal sharing channel. |

---

## GOVERN 5 — Engagement with relevant AI actors

Processes are in place for robust engagement with relevant AI actors.

| ID | Official outcome | Suggested actions |
|----|------------------|-------------------|
| GV-5.1 | Organizational policies and practices are in place to collect, consider, prioritize, and integrate feedback from those external to the team that developed or deployed the AI system regarding the potential individual and societal impacts related to AI risks. | User, community, and domain-expert feedback intake. |
| GV-5.2 | Mechanisms are established to enable the team that developed or deployed AI systems to regularly incorporate adjudicated feedback from relevant AI actors into system design and implementation. | Adjudication log: feedback → accept/reject → design change. |

---

## GOVERN 6 — Third-party software, data, and supply chain

Policies and procedures are in place to address AI risks and benefits arising from third-party software and data and other supply chain issues.

| ID | Official outcome | Suggested actions |
|----|------------------|-------------------|
| GV-6.1 | Policies and procedures are in place that address AI risks associated with third-party entities, including risks of infringement of a third-party’s intellectual property or other rights. | Vendor due diligence, IP/data-rights clauses, model cards. |
| GV-6.2 | Contingency processes are in place to handle failures or incidents in third-party data or AI systems deemed to be high-risk. | Fallback, kill switch, and incident playbook for third-party failure — not an appeals process. |

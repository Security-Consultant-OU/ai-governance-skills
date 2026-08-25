# MAP function — NIST AI RMF 1.0 (Table 2)

Official subcategory outcomes from NIST AI 100-1. **5 categories, 18 subcategories**. There is no MAP-2.4.

---

## MAP 1 — Context is established and understood (6)

| ID | Official outcome | Suggested actions |
|----|------------------|-------------------|
| MAP-1.1 | Intended purposes, potentially beneficial uses, context-specific laws, norms and expectations, and prospective settings in which the AI system will be deployed are understood and documented. Considerations include: the specific set or types of users along with their expectations; potential positive and negative impacts of system uses to individuals, communities, organizations, society, and the planet; assumptions and related limitations about AI system purposes, uses, and risks across the development or product AI lifecycle; and related TEVV and system metrics. | Context dossier: purpose, users, laws, benefits/harms, limits, TEVV metrics. |
| MAP-1.2 | Interdisciplinary AI actors, competencies, skills, and capacities for establishing context reflect demographic diversity and broad domain and user experience expertise, and their participation is documented. Opportunities for interdisciplinary collaboration are prioritized. | Record who established context and their disciplines. |
| MAP-1.3 | The organization’s mission and relevant goals for AI technology are understood and documented. | Link the system to mission/OKRs. |
| MAP-1.4 | The business value or context of business use has been clearly defined or – in the case of assessing existing AI systems – re-evaluated. | Value case or re-evaluation memo. |
| MAP-1.5 | Organizational risk tolerances are determined and documented. | Numeric or qualitative tolerance; this is **not** “deployment context.” |
| MAP-1.6 | System requirements (e.g., “the system shall respect the privacy of its users”) are elicited from and understood by relevant AI actors. Design decisions take socio-technical implications into account to address AI risks. | Socio-technical requirements in the spec. |

---

## MAP 2 — Categorization of the AI system is performed (3)

| ID | Official outcome | Suggested actions |
|----|------------------|-------------------|
| MAP-2.1 | The specific tasks and methods used to implement the tasks that the AI system will support are defined (e.g., classifiers, generative models, recommenders). | Task/method card — **not** a 1–5 risk class. If generative, also run the 600-1 profile. |
| MAP-2.2 | Information about the AI system’s knowledge limits and how system output may be utilized and overseen by humans is documented. Documentation provides sufficient information to assist relevant AI actors when making decisions and taking subsequent actions. | Knowledge limits + human oversight design. |
| MAP-2.3 | Scientific integrity and TEVV considerations are identified and documented, including those related to experimental design, data collection and selection (e.g., availability, representativeness, suitability), system trustworthiness, and construct validation. | TEVV plan: data selection, construct validity, experimental design. |

---

## MAP 3 — Capabilities, usage, benefits and costs (5)

| ID | Official outcome | Suggested actions |
|----|------------------|-------------------|
| MAP-3.1 | Potential benefits of intended AI system functionality and performance are examined and documented. | Benefit register. |
| MAP-3.2 | Potential costs, including non-monetary costs, which result from expected or realized AI errors or system functionality and trustworthiness – as connected to organizational risk tolerance – are examined and documented. | Cost/harm register including non-monetary costs. |
| MAP-3.3 | Targeted application scope is specified and documented based on the system’s capability, established context, and AI system categorization. | In-scope / out-of-scope uses. |
| MAP-3.4 | Processes for operator and practitioner proficiency with AI system performance and trustworthiness – and relevant technical standards and certifications – are defined, assessed, and documented. | Operator proficiency standard. |
| MAP-3.5 | Processes for human oversight are defined, assessed, and documented in accordance with organizational policies from the GOVERN function. | Oversight procedure aligned to GV-3.2. |

---

## MAP 4 — Risks and benefits mapped for all components (2)

| ID | Official outcome | Suggested actions |
|----|------------------|-------------------|
| MAP-4.1 | Approaches for mapping AI technology and legal risks of its components – including the use of third-party data or software – are in place, followed, and documented, as are risks of infringement of a third party’s intellectual property or other rights. | Component + third-party risk map (IP included). |
| MAP-4.2 | Internal risk controls for components of the AI system, including third-party AI technologies, are identified and documented. | Control map per component — **not** “impacts on individuals.” |

---

## MAP 5 — Impacts characterized (2)

| ID | Official outcome | Suggested actions |
|----|------------------|-------------------|
| MAP-5.1 | Likelihood and magnitude of each identified impact (both potentially beneficial and harmful) based on expected use, past uses of AI systems in similar contexts, public incident reports, feedback from those external to the team that developed or deployed the AI system, or other data are identified and documented. | Impact register with likelihood × magnitude. |
| MAP-5.2 | Practices and personnel for supporting regular engagement with relevant AI actors and integrating feedback about positive, negative, and unanticipated impacts are in place and documented. | Engagement cadence and integration into MAP-5.1. |

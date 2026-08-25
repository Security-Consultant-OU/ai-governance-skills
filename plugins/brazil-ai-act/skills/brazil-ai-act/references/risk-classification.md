# Risk classification — Senate-approved PL 2338/2023 (not enacted)

**Label:** based on Senate-approved PL 2338/2023; not enacted. Chamber may amend Art. 13–16.

Art. 12 preliminary assessment is **optional** (“poderá”). It is not a mandatory EU-style decision tree.

---

## Art. 12 — Avaliação preliminar (optional)

| Aspect | Senate text |
|--------|-------------|
| Who | Agente de IA (desenvolvedor, distribuidor, or aplicador) |
| When | Before introduction/circulation on the market, employment, or use |
| Nature | Simplified **self-assessment** of risk degree (Art. 4 XV) |
| Mandatory? | **No** — “poderá realizar” |
| Benefit | Good practice; may support Art. 50 §1 (sanctions) and priority in Art. 34 conformity |
| Sectoral waiver | Autoridade setorial may simplify or waive (Art. 12 §2) |
| Reclassification | Autoridade competente, with sectoral authorities, may reclassify and order an AIA (Art. 12 §4) |

---

## Art. 13 — Risco excessivo (prohibited)

Vedados o desenvolvimento, a implementação e o uso:

| Inciso | Prohibited practice | Notes / exceptions |
|--------|---------------------|-------------------|
| I(a) | Instigate or induce behaviour causing harm to health, safety, or other fundamental rights | Harm to self or third parties |
| I(b) | Exploit vulnerabilities to induce behaviour causing such harm | Age, disability, social/economic or other vulnerability (Art. 4 XVII) |
| I(c) | **Predictive policing / recidivism** — assess personality, characteristics, or past behaviour (criminal or not) to evaluate risk of crime, infraction, or **reincidência** | Brazil-specific extra vs many EU readings |
| I(d) | Produce, disseminate, or facilitate **CSAM** (abuse or sexual exploitation of children and adolescents) | Generation and facilitation |
| II | **Public-power ranking** of natural persons by social behaviour or personality attributes, via universal scoring, for access to goods, services, and public policies, in an **ilegítima or desproporcional** way | **Not** a blanket social-scoring ban |
| III | **Sistemas de armas autônomas (SAA)** | Art. 4 XXVII: select and attack targets without further human intervention |
| IV | Real-time remote biometric identification in publicly accessible spaces | Exceptions: (a) criminal inquiry/process with prior reasoned judicial authorization, subsidiarity, not minor offence; (b) missing persons / imminent threat to life or physical integrity; (c) flagrante of crimes punishable by >2 years’ imprisonment, with immediate judicial communication; (d) recapture of escaped defendants and execution of judicial arrest/restrictive orders |

Art. 13 §1: desenvolvedores must adopt measures to **prevent** use of their systems for caput hypotheses. Art. 13 §2: inciso IV use must be proportional, strictly necessary, with due process, judicial control, and algorithmic-inference review by the responsible public agent.

---

## Art. 14 — Alto risco (purpose- and context-specific)

High-risk **only** for listed **finalidades e contextos**, considering probability and gravity of adverse impacts, **nos termos de regulamentação**.

| Inciso | Use | Specificity in Senate text |
|--------|-----|----------------------------|
| I | Safety components of **critical infrastructure** (traffic, water, electricity) | Relevant risk to physical integrity or interruption of essential services, illicit or abusive, **and determinant** for the result, decision, functioning, or access |
| II | **Education** — student selection for admission, or assessments **determinant** of academic progress, or student monitoring | **Not** monitoring exclusively for security |
| III | **Employment** — recruitment, screening, filtering, evaluation of candidates; promotion or termination; performance and behaviour in employment, worker management, access to self-employment | Purpose-specific, not “any HR AI” |
| IV | Access, eligibility, grant, review, reduction, or revocation of **essential** private and public services (including social assistance and social security eligibility) | Essential-services gatekeeping |
| V | Triage / priority of essential public services (fire, medical assistance) | Dispatch/priority |
| VI | **Administration of justice** — assist judicial authorities in investigating facts and applying law where there is risk to individual liberties and the democratic rule of law | **Excludes** systems that only assist administrative acts |
| VII | **Autonomous vehicles** in public spaces | When use may generate **relevant risk to physical integrity** |
| VIII | **Healthcare** — assist diagnoses and medical procedures | When there is **relevant risk to physical and mental integrity** |
| IX | Analytic crime study on natural persons — police search of large, multi-source datasets to identify behavioural patterns and profiles | Distinct from Art. 13 I(c) prohibition |
| X | Administrative investigation — assess credibility of evidence or predict occurrence/recurrence of an infraction from profiles of natural persons | Administrative, not the Art. 13 I(c) ban |
| XI | Biometric identification/authentication for **emotion recognition** | **Excludes** biometric authentication whose **only** aim is to confirm a specific person |
| XII | Immigration and border control to assess entry of a person or group | Entry assessment |

**Art. 14 parágrafo único:** not high-risk if the system is **intermediate technology that does not influence or determine** the result or decision, or performs only a **restricted procedural task**.

---

## Arts. 15–16 — Lists and sectoral prevalence

| Article | Rule |
|---------|------|
| Art. 15 | SIA regulates the high-risk list and may identify **new** high-risk applications using listed impact criteria |
| Art. 16 I | Autoridade competente (SIA coordinator) issues general orientations and **publishes the consolidated list** defined by sectoral authorities |
| Art. 16 II | **Autoridades setoriais**, in a **prevalent** way, set lists of what is / is not high-risk within Art. 14 contexts; receive and analyse AIAs |
| Art. 16 §2 | Desenvolvedor/aplicador who considers the system **not** high-risk may file a reasoned petition with the sectoral authority plus the Art. 12 assessment |
| Art. 16 §3 | **Distribuidores** must ensure governance measures are met **before** the system is placed on the market |

---

## Comparison with EU AI Act (informational only)

| Feature | Senate PL 2338/2023 (not law) | EU AI Act (in force) |
|---------|-------------------------------|----------------------|
| Legal status | Bill | Regulation 2024/1689 |
| Preliminary assessment | Art. 12 **optional** | Classification is a legal duty |
| Prohibited extras | Predictive policing/recidivism; CSAM generation; autonomous weapons | Different Art. 5 catalogue |
| Social scoring | Public-power **ilegítima/desproporcional** ranking | Broader public social-scoring ban |
| High-risk filter | Art. 14 parágrafo único (intermediate / non-determinant) | Art. 6(3) narrow exceptions |
| Emotion recognition | High-risk Art. 14 XI (not a blanket ban) | Art. 5 workplace/education ban + Art. 50 |
| Who updates lists | Sectoral authorities **prevalently** (Art. 16) | Commission / Annex III |

---

## Workflow order (not a hard tree)

1. Art. 1 territorial + exclusions.
2. Optional Art. 12 preliminary assessment.
3. Art. 13 prohibited screen (including extras and biometric exceptions).
4. Art. 14 purpose/context + parágrafo único.
5. Art. 16 sectoral list if any.
6. Otherwise not high-risk; Art. 5 still applies.

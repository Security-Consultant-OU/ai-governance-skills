# High-risk AI system requirements (Articles 8–15 and related duties)

## Requirements overview (Articles 8–15)

| Article | Requirement title | What to implement | Evidence needed | Common gaps |
|---------|------------------|-------------------|-----------------|-------------|
| Art. 8 | Compliance with Chapter III Section 2 | AI system designed and developed to comply with Arts. 9–15, taking into account intended purpose and generally acknowledged state of the art | System design documentation referencing each article requirement | Treating requirements as a one-time checklist rather than ongoing compliance |
| Art. 9 | Risk management system | Continuous, iterative process throughout the entire lifecycle: identify and analyse known and reasonably foreseeable risks; estimate and evaluate risks from intended use and reasonably foreseeable misuse; evaluate other risks from post-market data; adopt suitable risk-management measures. Testing prior to placing on the market and during the lifecycle. Measures proportionate and technically feasible; due consideration to persons under 18 | Risk management plan; risk register; testing reports; residual-risk documentation | One-time assessment; residual risks undocumented; foreseeable misuse not tested |
| Art. 10 | Data and data governance | Training, validation and test datasets subject to appropriate data governance: design choices; preparation operations; quality criteria (relevance, representativeness, accuracy, completeness); examination for possible biases; identification of gaps; appropriate statistical properties for the geographical, contextual, behavioural or functional setting | Data governance framework; dataset cards; bias examination reports; data-gap analysis | No dataset cards; bias examination ignores proxy variables; no representativeness analysis for deployment context |
| Art. 11 | Technical documentation | Draw up technical documentation per Annex IV before placing on the market or putting into service; keep it up to date | Annex IV documentation; version history; update log | Created at the end of development; missing Annex IV sections |
| Art. 12(1)–(2) | Record-keeping (general) | Technically allow automatic recording of events (logs) over the lifetime of the system. Logging capabilities shall enable recording of events relevant for: (a) identifying situations that may result in a risk within the meaning of Art. 79(1) or in a substantial modification; (b) facilitating post-market monitoring (Art. 72); (c) monitoring of operation referred to in Art. 26(5) | Logging architecture; log retention policy; audit-trail documentation; log access controls | Logging insufficient for post-deployment traceability; no retention policy; log integrity not protected |
| Art. 12(3) | Additional logging — remote biometric identification only | **Only** for high-risk AI systems referred to in **Annex III point 1(a)** (remote biometric identification). At a minimum: (a) period of each use (start and end date and time); (b) the **reference database** against which input data has been checked; (c) the **input data** for which the search has led to a match; (d) identification of the **natural persons involved in the verification** of the results, as referred to in Art. 14(5) | Biometric-specific log schema; dual-verification records | Presenting Art. 12(3) items as general Art. 12 duties for all high-risk systems |
| Art. 13 | Transparency and information to deployers | Instructions for use including: provider identity and contact; characteristics, capabilities and limitations; intended purpose; accuracy, robustness and cybersecurity with metrics; known or foreseeable circumstances leading to risks; input-data specifications; human-oversight measures; computational and hardware resource expectations; maintenance | Instructions for use; deployer-facing documentation; performance metrics; known-limitation disclosures | Marketing documents instead of technical guidance; accuracy metrics absent; known risks not disclosed |
| Art. 14 | Human oversight | Designed to enable effective human oversight during use: understand capabilities and limitations; monitor operation and detect anomalies; decide not to use or disregard output; intervene or interrupt (stop button); override automated decisions. For remote biometric identification: at least two natural persons must independently verify before action is taken (Art. 14(5)) | Human-oversight plan; role descriptions; training materials; override procedures; for biometric: dual-verification procedure | Oversight is nominal; personnel lack authority to override; override mechanisms untested |
| Art. 15 | Accuracy, robustness, and cybersecurity | Achieve and maintain appropriate levels of accuracy documented in the instructions for use; resilience against errors, faults or inconsistencies; fail-safe mechanisms; cybersecurity against unauthorised third-party manipulation; robustness against adversarial inputs | Accuracy benchmarks and validation; robustness testing; cybersecurity assessment; fail-safe documentation | Self-reported accuracy without validation; no adversarial robustness testing; cybersecurity limited to infrastructure |

## Provider obligations summary for high-risk AI

| Obligation | Article | Description |
|------------|---------|-------------|
| Quality management system | Art. 17 | Establish and maintain a documented QMS covering compliance strategy, design and development techniques, examination and testing, technical specifications, risk management, post-market monitoring, incident reporting, communication with authorities |
| Technical documentation | Art. 11, Annex IV | Maintain complete, up-to-date technical documentation before placing on the market |
| Conformity assessment | Art. 43 | Complete the applicable procedure (Annex VI, Annex VII, or Art. 43(3) sectoral) before placing on the market |
| EU Declaration of Conformity | Art. 47 | Draw up the declaration containing all information specified in Annex V |
| CE marking | Art. 48 | Affix CE marking visibly, legibly, and indelibly (digital marking allowed) |
| Registration | Art. 49 | Register the high-risk AI system in the EU database before placing on the market; Art. 49(2) also covers providers who conclude under Art. 6(3) that an Annex III system is not high-risk |
| Post-market monitoring | Art. 72 | Establish a proportionate post-market monitoring system |
| Incident reporting | Art. 73 | Report serious incidents to market surveillance authorities without delay and no later than 15 days after the provider becomes aware of the incident |
| Corrective action | Art. 20 | Take corrective action if the AI system presents a risk, including withdrawal or recall |

## Deployer obligations for high-risk AI

| Obligation | Article | Description |
|------------|---------|-------------|
| Use in accordance with instructions | Art. 26(1) | Use the high-risk AI system in accordance with the instructions for use |
| Human oversight | Art. 26(2) | Assign human oversight to natural persons with competence, training, and authority |
| Input data relevance | Art. 26(4) | Ensure input data is relevant and sufficiently representative in view of the intended purpose |
| Monitoring | Art. 26(5) | Monitor operation on the basis of the instructions for use and inform the provider (and distributor) of risks |
| Record-keeping | Art. 26(6) | Keep the logs automatically generated by the system for a period appropriate to the intended purpose, of at least 6 months, unless Union or national law provides otherwise |
| Inform workers and representatives | Art. 26(7) | Before putting into service or using a high-risk AI system at the workplace, inform workers' representatives and the affected workers |
| Inform affected persons | Art. 26(11) | Deployers of high-risk systems referred to in Annex III that make decisions or assist in making decisions related to natural persons shall inform those persons that they are subject to the use of the high-risk AI system |
| FRIA (gated) | Art. 27 | Required for bodies governed by public law or private entities providing public services, **and** for all deployers of Annex III point 5(b) credit scoring and 5(c) life/health insurance; **not** required for Annex III point 2 critical infrastructure. Notify the MSA of results using the Commission template (Art. 27(3)). May be conducted in conjunction with a DPIA (Art. 27(4)) |

## Article 25 — when another operator becomes the provider

| Circumstance (Art. 25(1)) | Effect |
|---------------------------|--------|
| Put their **name or trademark** on a high-risk AI system already placed on the market or put into service | They are considered the **provider** and take on provider obligations |
| Make a **substantial modification** to a high-risk AI system already placed on the market or put into service | They are considered the **provider** |
| Modify the **intended purpose** of an AI system, including a general-purpose AI system, which has not been classified as high-risk and is already placed on the market or put into service, in a manner that the system becomes a high-risk AI system | They are considered the **provider** |

Where Art. 25(1) applies, the original provider is no longer considered a provider for that specific AI system for the purposes of this Regulation. The original provider shall cooperate and make available necessary information, technical access or other assistance (Art. 25(2)), without prejudice to trade secrets.

# EU AI Act worked examples

Five compact cases. Each table is self-contained. Output artefacts follow the classification result recipe (six sections in order), the FRIA gate skeleton, or the GPAI obligation table.

## 1. Classify a chatbot

| Item | Content |
|------|---------|
| User asks | Classify our customer-support chatbot that answers product questions |
| Skill does | Run the non-exclusive tree. Art. 50(1) is additive for systems intended to interact directly with natural persons (inform the person they are interacting with an AI system, unless obvious to a reasonably well-informed, observant and circumspect person). Separately check whether the same chatbot also performs an Annex III function (e.g. recruitment screening → Annex III point 4) |
| Artefact | Classification result in order: (1) Art. 5 (2) Art. 6(1) (3) Annex III/6(2) (4) Art. 6(3) (5) Art. 50 independently (6) residual |

| Step | Typical finding for a general support chatbot | Typical finding if the chatbot screens job applicants |
|------|-----------------------------------------------|------------------------------------------------------|
| (1) Art. 5 | Not prohibited | Not prohibited (unless another Art. 5 practice is present) |
| (2) Art. 6(1) | Not an Annex I product path | Not an Annex I product path |
| (3) Annex III / 6(2) | Not Annex III | Annex III point 4 (recruitment/selection) → EU high-risk |
| (4) Art. 6(3) | N/A | Apply both limbs + (a)–(d); profiling of natural persons stays EU high-risk |
| (5) Art. 50 | Art. 50(1) still applies (additive) | Art. 50(1) still applies (additive) on top of EU high-risk duties |
| (6) Residual | Residual product duties + Art. 50(1), unless another section triggered | Not residual — EU high-risk + Art. 50(1) |

Art. 50(1) exception: systems authorised by law to detect, prevent, investigate or prosecute criminal offences (unless made available for the public to report a criminal offence).

## 2. Classify workplace emotion recognition

| Item | Content |
|------|---------|
| User asks | Classify an AI system that infers workers' emotions from video or voice in the workplace |
| Skill does | Apply Art. 5(1)(f) first. Emotion recognition in the workplace or education institutions is **prohibited**, except where the use is intended to be put in place or into the market for **medical or safety** reasons. Do not treat emotion recognition as exclusive limited-risk |
| Artefact | Classification result in six-section order |

| Setting | (1) Art. 5 | Then |
|---------|------------|------|
| Workplace or education, not medical/safety | **Prohibited** (Art. 5(1)(f)). Must not be placed on the market, put into service, or used | Stop for that use. Still record (5) Art. 50 as additive in principle, but the use is banned |
| Workplace or education, medical or safety exception | Not prohibited under Art. 5(1)(f) | Continue: typically Annex III point 1(c) EU high-risk **and** Art. 50(3) deployer notice |
| Outside workplace and education | Not an Art. 5(1)(f) prohibition | Typically Annex III point 1(c) EU high-risk **and** Art. 50(3). Never “limited risk only” |

## 3. Annex I medical-device path

| Item | Content |
|------|---------|
| User asks | Classify AI software that is a safety component of a medical device already requiring notified-body conformity assessment under MDR |
| Skill does | Apply Art. 6(1): (a) safety component of a product (or itself a product) covered by Annex I Union harmonisation legislation, **and** (b) that product (or the AI system as product) already requires **third-party** conformity assessment under that legislation. If both limbs are met → EU high-risk. Conformity path is **Art. 43(3) sectoral** under that legislation, **integrating Arts. 9–15**. This is not Annex VI/VII under Art. 43(1)–(2) |
| Artefact | Classification result (section (2) is the lead finding) plus Art. 43(3) conformity path |

| Step | Fill |
|------|------|
| (1) Art. 5 | [Usually not prohibited; still check] |
| (2) Art. 6(1) | **EU high-risk** if both Annex I coverage and third-party CA under that act are true |
| (3) Annex III / 6(2) | May also be Annex III; Art. 6(1) already suffices for EU high-risk |
| (4) Art. 6(3) | Art. 6(3) derogation is an Annex III rule; it does not undo a true Art. 6(1) path |
| (5) Art. 50 | Apply independently (e.g. 50(1) if the device interacts with natural persons) |
| (6) Residual | No — EU high-risk |
| Conformity | Art. 43(3) sectoral CA + Arts. 9–15 integrated; then Art. 47 DoC, Art. 48 CE, Art. 49 registration as applicable |

## 4. Deployer FRIA yes/no

| Item | Content |
|------|---------|
| User asks | Must this deployer perform a FRIA before using the system? |
| Skill does | Apply the Art. 27 **gate**, not a free-form plan. FRIA applies to EU high-risk systems as defined in Art. 6(2) (Annex III), **except** Annex III point 2 (critical infrastructure). Addressees: bodies governed by public law; private entities providing public services; **all** deployers of Annex III 5(b) (credit scoring of natural persons) and 5(c) (life/health insurance) |
| Artefact | Gate skeleton: **FRIA required** or **FRIA not triggered**. If required, fill Art. 27(1)(a)–(f) and the MSA notification line |

| Deployer | System | Gate result |
|----------|--------|-------------|
| Public hospital (public law) | Annex III system that is not point 2 | **FRIA required** |
| Private firm providing a public service | Annex III system that is not point 2 | **FRIA required** |
| Any deployer | Annex III **5(b)** credit scoring | **FRIA required** (all 5(b) deployers) |
| Any deployer | Annex III **5(c)** life/health insurance | **FRIA required** (all 5(c) deployers) |
| Any deployer | Annex III **point 2** critical infrastructure | **FRIA not triggered** (Art. 27 exception) |
| Private retailer, not providing public services | Annex III point 4 workplace tool | **FRIA not triggered** |
| Any deployer | Not Annex III / not Art. 6(2) | **FRIA not triggered** |

If required: notify the MSA of **results** using the Commission template (Art. 27(3)/(5)). If a GDPR Art. 35 or LED Art. 27 DPIA already covers some elements, conduct the FRIA in conjunction with that DPIA (Art. 27(4)).

## 5. GPAI vs systemic-risk

| Item | Content |
|------|---------|
| User asks | Are we a GPAI model provider, and do systemic-risk duties apply? Is open-source enough to drop documentation? |
| Skill does | Separate Art. **53** (all GPAI models) from Art. **51/55** (systemic risk). Presumed systemic risk if training compute **> 10^25 FLOPs**, or Commission designation. Art. 52: notify the Commission without delay and in any event within **2 weeks**. OSS (Art. 53(2)) drops **only** 53(1)(a)–(b), and only if the model is **not** systemic-risk. 53(1)(c) copyright policy and 53(1)(d) public training-content summary **always** apply. Systemic-risk models get **no** OSS exemption. Art. 55(1)(b) Union-level risk assessment/mitigation is **not** red-teaming (55(1)(a)) |
| Artefact | GPAI obligation table with 🔴🟡🟢 per row |

| Model fact | Art. 53 | Art. 51/55 | OSS (Art. 53(2)) |
|------------|---------|------------|------------------|
| GPAI, compute ≤ 10^25 FLOPs, not designated | 53(1)(a)–(d) all apply | No Art. 55 | If OSS conditions met: drop (a) and (b) only; (c) and (d) remain |
| GPAI, compute > 10^25 FLOPs (or designated) | 53(1)(a)–(d) all apply | Art. 55(1)(a)–(d) apply; Art. 52 notification | **No** OSS drop — full 53 + 55 |
| Not a GPAI model | Chapter V N/A | N/A | N/A |

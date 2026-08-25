# High-impact AI (고영향 AI) — Art. 2(4), decree, Art. 33

Use **high-impact AI (고영향 AI)** in English. Use “high-risk” only when mapping to the EU AI Act.

## Two-limb test (both required)

| Limb | Article / instrument | Pass | Fail |
|------|----------------------|------|------|
| Significance | Art. 2(4) | System is likely to **significantly affect** life, physical safety, or fundamental rights | No material effect on those interests (purely advisory, easily ignored, no rights/safety stake) |
| Domain | Art. 2(4) + Enforcement Decree No. 36053 | Used in a listed domain or a domain added by decree | Used only outside listed/decree domains |

A system that fails either limb is **not** high-impact. Still check Art. 31 (generative) and Art. 32 (high-compute).

## Listed domains (Art. 2(4) + decree)

| Domain | Article / instrument | Typical in-scope use | Typically out unless another domain applies |
|--------|----------------------|----------------------|-----------------------------------------------|
| Energy | Art. 2(4) | AI controlling or materially directing energy supply/operation where failure can affect life or safety | Internal analytics with no operational control |
| Drinking water | Art. 2(4) | AI affecting drinking-water treatment, distribution, or safety | Office water-cooler inventory |
| Healthcare | Art. 2(4) | AI used in diagnosis, treatment, or clinical pathways affecting life or safety | Administrative scheduling with no clinical effect |
| Medical devices | Art. 2(4) | AI as or in a medical device affecting diagnosis or treatment | Wellness gadget with no medical purpose |
| Nuclear | Art. 2(4) | AI affecting nuclear safety or operations | Document search in a nuclear operator’s legal team |
| Biometric analysis for investigation/arrest | Art. 2(4) | Biometric AI used to investigate or arrest | Consent-based unlocking of a personal device |
| Hiring decisions | Art. 2(4) | AI used to decide or substantially determine hire / no-hire (and similar rights/obligations) | Generic HR chatbot that does not rank or reject candidates |
| Loan and similar rights/obligations decisions | Art. 2(4) | AI used to decide credit, loans, or comparable legal rights/obligations | Marketing propensity scores with no credit decision |
| Core transport | Art. 2(4) | AI affecting core transport safety or operation | Ride-hail ETA display with no safety control |
| Public-institution public-service eligibility or cost | Art. 2(4) | AI used by a public institution to determine eligibility for or cost of a public service | Public website chatbot that does not decide eligibility or fees |
| Student evaluation (early childhood / elementary / secondary) | Art. 2(4) | AI used to evaluate students in those levels | University admissions tools (not this limb; check other domains) |
| Other domains designated by decree | Art. 2(4) + Enforcement Decree No. 36053 | Decree-listed additional domains | Domains not listed in the Act or decree |

## Human-in-final-decision exclusion (decree)

| Question | Article / instrument | If yes | If no |
|----------|----------------------|--------|-------|
| Does a human make the **final** decision? | Enforcement Decree No. 36053 | Continue | Exclusion does not apply; remain on the two-limb test |
| Is the system **deemed controllable** (human can actually reject/override; not rubber-stamp)? | Enforcement Decree No. 36053 | **Not high-impact** | Exclusion does not apply |

| Evidence to keep | Article / instrument | Acceptable | Not acceptable |
|------------------|----------------------|------------|----------------|
| Named human decision-maker and authority | Decree exclusion | Role, mandate, and when they decide | “A human is in the loop” with no authority |
| Ability to reject the AI output | Decree exclusion | Documented reject/override that is used | Override exists but never used or cannot change the outcome |
| Controllability rationale | Decree exclusion | Why residual risk is controllable | Automation of the legal decision with a courtesy click |

## Optional MSIT confirmation (Art. 33)

| Step | Article | Required? | Content |
|------|---------|-----------|---------|
| Self-review file (purpose, domain, significance, HITL) | Art. 33 | No — optional | Operator’s classification record |
| Request MSIT confirmation of high-impact status | Art. 33 | No — optional | Used when status is material or contested |
| Confirmation outcome | Art. 33 | If requested | Informs compliance posture; it is not a product licence or pre-market approval |

## Classification examples

| System | Basis | Art. 2(4) domain? | Significance? | HITL exclusion? | Result |
|--------|-------|-------------------|---------------|-----------------|--------|
| Clinical diagnostic AI issuing findings used in treatment | Art. 2(4) | Healthcare / medical devices | Yes — life/safety | No (output drives care) | High-impact |
| Same diagnostic AI; licensed clinician must accept/reject and routinely rejects | Art. 2(4) + decree | Healthcare / medical devices | Yes | Yes — human final decision, deemed controllable | Not high-impact (document exclusion) |
| Hiring ranker that auto-rejects applicants | Art. 2(4) | Hiring | Yes — fundamental rights / obligations | No | High-impact |
| Hiring screen that only suggests interview questions; recruiter decides freely | Art. 2(4) + decree | Hiring (borderline domain use) | Weak if no decision effect | Yes if human decides | Usually not high-impact |
| Credit decision engine that grants/denies loans | Art. 2(4) | Loan / similar rights | Yes | No | High-impact |
| Public-benefit chatbot that does not determine eligibility or fees | Art. 2(4) | Public-service eligibility/cost — no | No | n/a | Not high-impact |
| Generative image tool for marketing | Art. 2(4); Art. 31(2)–(3) | None of the listed domains | No | n/a | Not high-impact; Art. 31(2)–(3) may still apply |
| Grid-control AI for energy dispatch | Art. 2(4) | Energy | Yes — safety | No | High-impact |

## What this classification is not

| Topic | Article / instrument | Rule |
|-------|----------------------|------|
| EU high-risk | Mapping synonym only | Art. 2(4) high-impact ≠ EU Annex III high-risk |
| All AI in a listed sector | Art. 2(4) | Sector presence alone is insufficient without significance |
| Prohibited-AI tier | — | This Act has no EU Art. 5-style prohibited category |
| Art. 32 high-compute | Art. 32 | Separate gate; a system can be Art. 32 in-scope without being high-impact, and vice versa |

# AEDT definition — NYC Local Law 144

Sources: Admin. Code § 20-870; 6 RCNY § 5-300; DCWP AEDT FAQ (https://www.nyc.gov/assets/dca/downloads/pdf/about/DCWP-AEDT-FAQ.pdf).

## Statutory terms

| Term | Definition |
|------|------------|
| AEDT | Computational process derived from machine learning, statistical modeling, data analytics, or artificial intelligence that issues a simplified output used to substantially assist or replace discretionary decision-making for an employment decision |
| Substantially assist or replace | (1) Rely **solely** on a simplified output with **no other factors** considered; **or** (2) use a simplified output as one of a set of criteria where it is **weighted more than any other** criterion in the set; **or** (3) use a simplified output to **overrule** conclusions derived from other factors **including human decision-making** |
| ML / statistical modeling / data analytics / AI | Mathematical, computer-based techniques that generate a prediction or classification **and** for which a computer **at least in part identifies the inputs, the relative importance of those inputs**, and, if applicable, other parameters to improve accuracy |
| Simplified output | Prediction or classification in the form of a score, tag, categorization, recommendation, or ranking. **Does not** include tools that **translate or transcribe existing text** (e.g., PDF conversion, interview transcription) |
| Candidate for employment | Person who has applied for a **specific** employment position by submitting the information or items in the format required by the employer or employment agency |
| Screen | Determination about whether a candidate or employee being considered for promotion should be selected or advanced |
| Employment decision | Screening a candidate for employment or an employee for promotion (not limited to the final hire/promote decision) |

Equal-weight scores among several criteria, with no sole reliance and no overrule, are **not** AEDTs. Boolean or predetermined filters (computer does not identify inputs or weights) stay **out**.

## What qualifies

| System type | AEDT? | Reasoning |
|-------------|-------|-----------|
| Resume-ranking model that is the sole screen | Yes | Prong 1 — solely relied upon |
| Interview score weighted higher than any other criterion | Yes | Prong 2 — weighted more than any other |
| Model output used to overturn a human “advance” decision | Yes | Prong 3 — overrules other factors including humans |
| Skills model whose score is one of several **equal** weights; human not overruled | No | Prong 2 not met; not sole; no overrule |
| ATS Boolean keyword filter with predetermined rules | No | Computer does not identify inputs or relative importance |
| PDF/resume transcription or interview transcription | No | Not a simplified output |
| Resume-bank scan, cold outreach, or invite-to-apply | Not covered | Person has not applied for a **specific** position |
| Screening chatbot that scores answers and advances/rejects at any stage | Yes if a prong is met | Screening at any stage is an employment decision |
| Calendar / interview-scheduling tool | No | Administrative; no simplified employment output |
| Background check with no ML scoring | No | Factual verification, not ML/stats/AI as defined |

## Geography (do not invert)

| Duty | What triggers it |
|------|------------------|
| Bias audit, published summary | **Job/agency location:** NYC office at least part-time; **or** fully remote job **associated with** an NYC office; **or** NYC employment agency (or out-of-city agency hiring for a job that meets a bullet above) |
| Notice | Candidate or employee **resides in NYC** |

A NYC-headquartered employer using a tool only on jobs not located in / associated with NYC does **not** trigger the audit duty. An NYC-resident candidate for a non-NYC job does **not** trigger the audit duty. A non-resident applying to an NYC job **does** trigger the audit duty; NYC-resident notice still follows residence.

## Covered vs not covered use

| Scenario | Result |
|----------|--------|
| AEDT used to screen at an early stage (not the final decision) | Covered — “employment decision” includes screening |
| Tool used only for internal promotion | Covered — hiring and promotion |
| Resume bank, talent-pool outreach, sourcing | Not covered — not a candidate for a specific position |
| Multiple distinct AEDTs in one funnel | Each AEDT needs its own bias audit |
| Vendor-hosted model; employer cannot see weights | Employer/agency remains the responsible party |
| Vendor commissions an independent audit | Permitted; does **not** shift legal responsibility to the vendor |

## Determination tree

```
1. Does a computer at least in part identify inputs and their relative importance
   to generate a prediction or classification?
   ├── No (Boolean / predetermined filters) → NOT AN AEDT
   └── Yes → step 2

2. Does it produce a simplified output (score, tag, classification, ranking,
   recommendation) — not transcription/translation of existing text?
   ├── No → NOT AN AEDT
   └── Yes → step 3

3. Is it used to screen a candidate for a specific position or an employee
   for promotion (any stage)?
   ├── No (resume bank / outreach) → NOT COVERED
   └── Yes → step 4

4. Substantially assist or replace?
   ├── Sole factor, no other factors → AEDT
   ├── Weighted more than any other criterion → AEDT
   ├── Overrules other factors including humans → AEDT
   └── Equal weight, not sole, no overrule → NOT AN AEDT

5. Audit duty: is the job in / associated with an NYC office, or is the
   employment agency in NYC?
   ├── No → audit/publication not required under LL144
   └── Yes → bias audit + published summary required

6. Notice: does the candidate or employee reside in NYC?
   ├── No → NYC-resident notice not required
   └── Yes → notice required (≥ 10 business days)
```

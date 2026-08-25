# NYC Local Law 144 — worked examples

Sources: Admin. Code §§ 20-870–20-872; 6 RCNY §§ 5-300–5-304; DCWP AEDT FAQ.

## Contents

- Equal-weight score (not an AEDT under prong 2)
- NYC-office remote role (audit yes; notice only if NYC resident)
- First-use vendor audit (other-employer data; employer still liable)
- Notice vs audit split (residence vs job location)

Each example is: **User asks → Skill does → Artefact**.

---

## 1. Equal-weight score (not an AEDT under prong 2)

### User asks

“Our recruiter scorecard averages a skills-model score, a structured-interview score, and a hiring-manager rating at **equal weights**. A human still decides who advances. Is this an AEDT under NYC Local Law 144?”

### Skill does

Run the 6 RCNY § 5-300 determination in order:

| Step | Test | This fact pattern |
|------|------|-------------------|
| 1. ML/stats/AI | Computer at least in part identifies inputs and their relative importance | **Yes** — skills model |
| 2. Simplified output | Score, tag, classification, ranking, or recommendation (not transcription/translation) | **Yes** — skills-model score |
| 3. Employment decision | Screen a candidate for a **specific position** or an employee for promotion | **Yes** — hiring screen |
| 4. Three prongs | (1) sole factor with no other factors; **or** (2) weighted **more than any other** criterion; **or** (3) overrules other factors including humans | **None met** — equal weights; not sole; human not overruled |
| 5. Geography | Only if it is an AEDT | Not reached |

Equal-weight among several criteria, with no sole reliance and no overrule, is **not** an AEDT under prong 2.

### Artefact

```
AEDT determination — 6 RCNY § 5-300
Tool: skills-model score averaged equally with interview score and manager rating
Decision: NOT AN AEDT
Prong 1 (sole factor): No — two other criteria are used
Prong 2 (weighted more than any other): No — equal weights
Prong 3 (overrules other factors including humans): No — human decides who advances
If the model later becomes the highest-weighted criterion, or is used to overturn a human “advance,” re-run this determination.
```

| Variant that **would** be an AEDT | Prong |
|-----------------------------------|-------|
| Skills-model score is the only screen | 1 — sole factor |
| Skills-model weight > interview weight and > manager weight | 2 — weighted more than any other |
| Model “do not advance” flag overrides a human “advance” | 3 — overrules humans |

---

## 2. NYC-office remote role (audit yes; notice only if NYC resident)

### User asks

“The job is fully remote, associated with our Manhattan office. We will use an AEDT to screen applicants. Some live in Brooklyn; some live in New Jersey. What do we owe?”

### Skill does

Split geography. Do not invert it.

| Duty | Trigger | This fact pattern |
|------|---------|-------------------|
| Bias audit + published summary | **Job/agency location:** NYC office at least part-time; **or** fully remote job **associated with** an NYC office; **or** NYC employment agency | Fully remote **associated with** a Manhattan office → **audit duty yes** |
| Notice | Candidate or employee **resides in NYC** | Brooklyn resident → **notice yes**. New Jersey resident → **notice no** |

Audit duty does **not** depend on where the candidate lives. Notice does **not** depend on where the office is, once an AEDT is in use for a covered job.

### Artefact

```
Geography determination — LL144
Job: fully remote, associated with NYC (Manhattan) office
AEDT assumed: yes (already determined)

Bias-audit duty: YES (job associated with an NYC office)
  → Independent bias audit < 1 year old before use (Admin. Code § 20-871(a); 6 RCNY § 5-301)
  → Published summary + distribution date (6 RCNY § 5-303)

NYC-resident notice:
  → Brooklyn / other NYC-resident candidates: YES (≥ 10 business days; § 20-871(b); 6 RCNY § 5-304)
  → New Jersey / other non-NYC-resident candidates: NO NYC-resident notice
```

| Person | Job | Audit? | NYC-resident notice? |
|--------|-----|--------|----------------------|
| Brooklyn resident | Remote, associated with Manhattan office | Yes (job location) | Yes (residence) |
| Newark, NJ resident | Remote, associated with Manhattan office | Yes (job location) | No |

---

## 3. First-use vendor audit (other-employer data OK on first use; employer still liable)

### User asks

“We have never used VendorCo’s ranking AEDT. VendorCo sent an independent bias audit built from other employers’ historical data for the same tool. Can we rely on it for first use in NYC?”

### Skill does

Apply 6 RCNY § 5-302 and the responsible-party rule.

| Rule | Application |
|------|-------------|
| Other employers’ historical data (same AEDT) | Allowed **only if** this employer **contributed its own** historical data **or** it is this employer’s **first use** of the AEDT |
| This employer’s status | **First use** → other-employer historical data **may** be used |
| Auditor independence (6 RCNY § 5-300) | Still required: not involved in using/developing/distributing the AEDT; not employed by employer/agency or vendor during the audit; no direct or material indirect financial interest |
| Responsible party | **Employer or employment agency** must ensure an audit exists before use. Vendor commissioning the audit does **not** shift liability |
| After first use | Later uses need this employer’s own historical contribution **or** a new audit that meets § 5-302 without relying solely on other-employer data the employer did not join |

### Artefact

```
First-use data plan — 6 RCNY § 5-302
AEDT: VendorCo ranking model
Employer use: first use (no historical data of our own yet)

Data source: other employers’ historical data for the SAME AEDT — ALLOWED on first use
Auditor: confirm independence tests (not VendorCo staff; no financial interest in VendorCo or us)
Responsible party: THIS EMPLOYER / AGENCY remains liable under LL144
Before use: audit < 1 year old; published summary + our distribution date (date WE begin using this AEDT)
After first use: do not keep relying on other-employer-only data unless we contribute our own historical data
Do not impute sex or race/ethnicity.
```

| Later fact | Result |
|------------|--------|
| Second year; employer never contributed its own data | May **not** keep using an other-employer-only historical audit |
| Vendor says “our audit covers you” | Permitted as a document; **does not** make the vendor the LL144 responsible party |

---

## 4. Notice vs audit split (residence vs job location)

### User asks

“Walk me through notice versus the bias audit when some candidates live in NYC and some jobs are outside NYC.”

### Skill does

Keep the two triggers separate.

| Duty | What drives it | What does **not** drive it |
|------|----------------|----------------------------|
| Bias audit + published summary | **Job/agency location** (NYC office at least part-time; fully remote **associated with** an NYC office; NYC employment agency) | Candidate’s home address |
| Notice | Candidate or employee **resides in NYC** | Where the employer is headquartered, by itself |

A NYC-headquartered employer using a tool only on jobs **not** located in / associated with NYC does **not** trigger the audit duty. An NYC-resident candidate for a non-NYC job does **not** trigger the audit duty. A non-resident applying to an NYC job **does** trigger the audit duty; NYC-resident notice still follows residence.

### Artefact

```
Notice vs audit matrix — do not invert

                    | NYC job / remote associated with NYC office | Job NOT in / associated with NYC
NYC-resident        | Audit YES; notice YES                       | Audit NO; NYC-resident notice NO
                    |                                             |   (tool not used “in the city” for that job)
Non-NYC-resident    | Audit YES; notice NO                        | Audit NO; notice NO
```

| Scenario | Audit? | Notice? | Why |
|----------|--------|---------|-----|
| Austin resident applies to a Manhattan hybrid role | Yes | No | Job location → audit; residence is not NYC → no NYC-resident notice |
| Queens resident applies to a Manhattan hybrid role | Yes | Yes | Both triggers met |
| Queens resident applies to a Chicago-only role (not associated with an NYC office) | No | No | No NYC job/agency location; not using the AEDT in the city for that role |
| NYC employment agency screens for a covered NYC job, candidate lives in Connecticut | Yes | No | Agency/job location → audit; residence → no notice |

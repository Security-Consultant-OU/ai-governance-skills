# NYC Local Law 144 — output templates

Sources: Admin. Code §§ 20-870–20-872; 6 RCNY §§ 5-300–5-304; DCWP AEDT FAQ.

Cite **only** those sections. If a number is not on this page, look it up in the DCWP FAQ or 6 RCNY §§ 5-300–5-304 rather than inventing one. There is no “Section 20-a.”

## Contents

- Default document order
- AEDT determination recipe
- Bias-audit table shells
- Scoring-rate formula reminder
- Notice checklist
- Gap row

---

## Default document order

When the user does not name a document type:

1. Produce the **AEDT determination** (recipe below).
2. If the decision is **AEDT**, produce the **bias-audit table shells** (sex; 7 EEO-1 race/ethnicity; intersectional; unknown counts).

Then add notice or gap rows only if the user asked for them or the facts require them.

---

## AEDT determination recipe

Copy this block and fill every row in order. Stop at the first **Not an AEDT** or **Not covered**.

```
AEDT determination — 6 RCNY § 5-300

1. ML / statistical modeling / data analytics / AI
   A computer at least in part identifies the inputs and their relative
   importance to generate a prediction or classification.
   Finding: Yes / No
   If No (Boolean or predetermined filters) → NOT AN AEDT. Stop.

2. Simplified output
   Score, tag, categorization, recommendation, or ranking.
   Not transcription or translation of existing text.
   Finding: Yes / No
   If No → NOT AN AEDT. Stop.

3. Employment decision
   Screening a candidate who applied for a specific position, or an
   employee for promotion, at any stage.
   Finding: Yes / No (resume-bank / outreach / invite-to-apply → NOT COVERED). Stop.

4. Three prongs (“substantially assist or replace”)
   Prong 1 — Sole factor; no other factors considered: Yes / No
   Prong 2 — Weighted more than any other criterion in the set: Yes / No
   Prong 3 — Overrules other factors, including human decision-making: Yes / No
   Equal-weight among several criteria, not sole, no overrule → NOT AN AEDT.

5. Geography (only if it is an AEDT)
   Audit duty — job/agency location:
     NYC office at least part-time / fully remote associated with an NYC office /
     NYC employment agency (or out-of-city agency hiring for a job that meets a bullet above)
     Finding: Audit required Yes / No
   Notice — candidate or employee resides in NYC: Notice required Yes / No

Decision: AEDT / Not an AEDT / Not covered / Gray area
Citations used: 6 RCNY § 5-300 [add Admin. Code § 20-870 if stating the statutory term]
```

If the decision is **AEDT**, continue to the table shells.

---

## Bias-audit table shells

**Scoring rate** = share of the category scoring **above the sample median** (median of the **full applicant sample**). Do not use mean score or “highest mean.”

**Impact ratio (scoring)** = category scoring rate / **highest** category scoring rate.

**Selection rate** = selected (or classified) in the category / total in the category. **Impact ratio (selection)** = category selection rate / **highest** category selection rate.

Unknown sex and unknown race/ethnicity **counts must be stated**. Those individuals are omitted from rate/ratio calculations.

Race/ethnicity uses **EEO-1 Component 1** — **7** categories. Intersectional **sex × race/ethnicity** is **required**.

If the AEDT classifies into groups, repeat every table **for each group**.

### Unknown counts (state first)

```
Unknown sex: n = ___
Unknown race/ethnicity: n = ___
# assessed with unknown sex or race/ethnicity (omitted from rate tables): n = ___
Full-sample median score (scoring tools only): ___
```

### Sex

| Category | # Applicants | # Selected or # above median | Selection or scoring rate | Impact ratio |
|----------|--------------|------------------------------|---------------------------|--------------|
| Male | | | | |
| Female | | | | |

### Race/ethnicity (EEO-1 Component 1 — 7 categories)

| Category | # Applicants | # Selected or # above median | Selection or scoring rate | Impact ratio |
|----------|--------------|------------------------------|---------------------------|--------------|
| Hispanic or Latino | | | | |
| White (Not Hispanic or Latino) | | | | |
| Black or African American (Not Hispanic or Latino) | | | | |
| Native Hawaiian or Other Pacific Islander (Not Hispanic or Latino) | | | | |
| Asian (Not Hispanic or Latino) | | | | |
| American Indian or Alaska Native (Not Hispanic or Latino) | | | | |
| Two or More Races (Not Hispanic or Latino) | | | | |

### Intersectional (sex × race/ethnicity) — required

| Race/ethnicity | Sex | # Applicants | # Selected or # above median | Selection or scoring rate | Impact ratio |
|----------------|-----|--------------|------------------------------|---------------------------|--------------|
| Hispanic or Latino | Male | | | | |
| Hispanic or Latino | Female | | | | |
| White (Not Hispanic or Latino) | Male | | | | |
| White (Not Hispanic or Latino) | Female | | | | |
| Black or African American (Not Hispanic or Latino) | Male | | | | |
| Black or African American (Not Hispanic or Latino) | Female | | | | |
| Native Hawaiian or Other Pacific Islander (Not Hispanic or Latino) | Male | | | | |
| Native Hawaiian or Other Pacific Islander (Not Hispanic or Latino) | Female | | | | |
| Asian (Not Hispanic or Latino) | Male | | | | |
| Asian (Not Hispanic or Latino) | Female | | | | |
| American Indian or Alaska Native (Not Hispanic or Latino) | Male | | | | |
| American Indian or Alaska Native (Not Hispanic or Latino) | Female | | | | |
| Two or More Races (Not Hispanic or Latino) | Male | | | | |
| Two or More Races (Not Hispanic or Latino) | Female | | | | |

### Published-summary fields (6 RCNY § 5-303)

```
Date of most recent bias audit:
Source and explanation of data (historical / test; why test if used):
Unknown-category counts:
Applicants, rates, and impact ratios: see tables above (all categories)
Distribution date (date this employer/agency began using this AEDT):
Hyperlink target (if used):
Keep posted ≥ 6 months after last use.
```

A category under **2%** of audit data **may** be excluded from **impact-ratio calculations only**, with auditor justification; still report counts and rates.

The EEOC 4/5ths (0.80) figure may be noted as a **disclosure reference**. It is **not** an LL144 pass/fail.

---

## Notice checklist

Produce this checklist, then draft copy from the rows that apply. Notice is owed to candidates and employees who **reside in NYC** (Admin. Code § 20-871(b); 6 RCNY § 5-304).

```
NOTICE CHECKLIST — NYC residents only

Who
  [ ] Candidate applied for a specific position, or employee considered for promotion
  [ ] Person resides in NYC
  [ ] Resume-bank / outreach / invite-to-apply is out of scope

AEDT-use notice (§ 20-871(b)(1)–(2); 6 RCNY § 5-304(a)–(c))
  [ ] States that an AEDT will be used to assess or evaluate
  [ ] States job qualifications and characteristics the AEDT will assess
  [ ] Instructions to request an alternative selection process or reasonable
      accommodation IF AVAILABLE (do not promise a process that is not offered)
  [ ] Delivered ≥ 10 business days before use
  [ ] Channel: website employment section (need not be position-specific;
      10 business days after website posting is enough) OR job posting OR mail/email
      OR, for promotion, written policy/procedure

Data notice (§ 20-871(b)(3); 6 RCNY § 5-304(d))
  [ ] Type of data collected for the AEDT
  [ ] Source of that data
  [ ] Data retention policy
  [ ] Website instructions for a written request
  [ ] Response within 30 days of a written request
  [ ] Withholding rule: only if disclosure would violate law or interfere with
      a law-enforcement investigation; explain why
  [ ] This is type / source / retention — not the candidate’s raw file

Publication (6 RCNY § 5-303)
  [ ] Bias-audit summary posted or clearly labeled hyperlink
  [ ] Distribution date (first use of this AEDT) published with the summary
```

---

## Gap row

Assess against LL144 only. Status: 🔴 not started / 🟡 partial / 🟢 implemented.

Copy one row per requirement. Fill every column.

```
REQUIREMENT | STATUS | EVIDENCE | GAP NOTES | PRIORITY
```

| Requirement | Assessment question to answer in Gap notes |
|-------------|--------------------------------------------|
| AEDT identification | Tools tested against ML/stats/AI, simplified output, and the three prongs (equal-weight ≠ AEDT)? |
| Geography | Audit duty based on job/agency location, and notice on NYC residence? |
| Independent bias audit | Audit < 1 year old; auditor not involved in using/developing/distributing the AEDT? |
| Historical vs test data | Historical data used if statistically sufficient; test data explained; no imputed demographics? |
| Required tables | Sex, 7 EEO-1 race/ethnicity categories, **and** intersectional; scoring rate = above sample median; unknown counts stated? |
| Published summary | Audit date, data source, unknown counts, rates/ratios, **distribution date**; posted or hyperlinked; ≥ 6 months after last use? |
| NYC-resident notice | ≥ 10 business days; correct channel; alternative-process instructions **if available**? |
| Data notice | Type, source, retention; written-request instructions; 30-day response — not a raw-file dump? |

Example filled table:

```
REQUIREMENT              | STATUS         | EVIDENCE            | GAP NOTES                                      | PRIORITY
AEDT identification      | 🔴 not started | Tool inventory      | Equal-weight scorecard treated as AEDT           | High
Independent bias audit   | 🟡 partial     | Vendor letter       | Vendor is not the responsible party              | High
Published summary        | 🔴 not started | Website check       | Missing distribution date                        | High
NYC-resident notice      | 🟢 implemented | Careers page        | Posted > 10 business days                        | Monitor
Data notice              | 🟡 partial     | Privacy policy      | GDPR file-access language; missing data source   | High
```

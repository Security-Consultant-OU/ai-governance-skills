# ISO/IEC 42001 AISIA record

Clause **6.1.4** (process), **8.4** (perform), controls **A.5.2–A.5.5**. Not 6.1.2. A.5.1 is the objective, not a control. There is no A.5.8.

If document type is omitted, fill this record for the named system.

---

## Impact classification (acceptable process)

| Level | Criteria |
|-------|----------|
| Low | Limited population; easily reversible; non-sensitive domain; strong oversight; opt-out; no disproportionate effect on vulnerable groups |
| Medium | Moderate population; partly reversible; some sensitive use (employment, finance, health); oversight not on every decision; opt-out has consequences |
| High | Large or vulnerable population; hard to reverse; highly sensitive domain; little or no individual oversight; no meaningful opt-out; power asymmetry |

---

## Dimensions to score

| Dimension | Question |
|-----------|----------|
| Nature | Positive, negative, or mixed — name the effects |
| Severity | Harm if the system fails, is biased, or is misused |
| Breadth | How many people; concentrated or widespread |
| Reversibility | Can outcomes be corrected, at what cost and delay |
| Consent | Meaningful choice / opt-out |
| Human oversight | Human in the loop; override before effect |
| Recourse | Complaint, appeal, alternative process |

---

## Proportionate control depth

Cite only real IDs.

| Area | Low | Medium | High |
|------|-----|--------|------|
| Transparency | A.8.2, A.8.5 general disclosure | Role of AI in the decision explained | Decision factors; proactive notice |
| Human oversight | A.9.2 periodic review | Review of flagged cases | Documented override; life-cycle gates A.6.2.6 |
| Bias / data | Annual A.6.2.6 / A.7.4 | Quarterly metrics | Continuous monitoring; A.7.5 lineage |
| Incidents | A.8.4 standard path | Enhanced AI incident | Immediate escalation |
| Recourse | General complaints | AI-specific appeal | Formal human review |

EU Art. 14 language belongs in `eu-ai-act`, not this record.

---

## Record (copy and fill)

```
AI SYSTEM IMPACT ASSESSMENT (AISIA) RECORD — ISO/IEC 42001 Clause 6.1.4 / 8.4

Document ID: AISIA-[XXX]
AI System: [Name]
Assessment Date: [Date]
Assessor(s): [Names and roles]
Next Review Date: [Date]

1. AI SYSTEM DESCRIPTION
   Name: [System name]
   Intended purpose: [What the system is designed to do]
   Input types: [Data inputs]
   Output types: [Decisions, predictions, classifications, content]
   Decision authority: [Advisory / Autonomous / Hybrid]
   Deployment scale: [Users / affected individuals]
   Operational environment: [Where and how deployed]
   Owner: [Role]

2. AFFECTED POPULATIONS
   Direct users: [Who uses the system]
   Decision subjects: [Who is affected by outputs]
   Indirect affected parties: [Communities, markets, others]
   Vulnerable groups identified: [Named groups or none identified]

3. IMPACT DIMENSION ASSESSMENT
   Nature: [Positive / Negative / Mixed — details]
   Severity: [Low / Moderate / High — justification]
   Breadth: [Scope]
   Reversibility: [Easily / Partially / Irreversible]
   Consent: [Informed / Implicit / None]
   Human oversight: [Full / Partial / None]
   Recourse: [Available / Limited / None]

4. IMPACT CLASSIFICATION
   Impact level: [Low / Medium / High]
   Justification: [From dimensions above]

5. REQUIRED CONTROLS
   [A.5.2–A.5.5 plus proportionate A.8, A.9.2, A.6.2.6–A.6.2.8 IDs only]

6. REVIEW AND APPROVAL (Clause 8.4)
   Assessed by: [Name, role, date]
   Reviewed by: [Name, role, date]
   Approved by: [Name, role, date]
   Next review / change triggers: [Date and events]
```

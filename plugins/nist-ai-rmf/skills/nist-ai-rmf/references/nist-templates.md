# NIST AI RMF output templates

Official subcategory outcomes from NIST AI 100-1. Scoring is Current vs Target at subcategory level: 🔴 not started / 🟡 partial / 🟢 implemented. The RMF does not define a 1–5 maturity scale.

**Do not invent Playbook Action IDs, subcategory IDs, or article/control IDs — look up official outcomes in NIST AI 100-1 Tables 1–4 and the Playbook at https://airc.nist.gov/airmf-resources/playbook/. If a Playbook Action ID is not in context, say so.**

There is no MAP-2.4. There is no MG-3.3. MEASURE 2 is ME-2.1–ME-2.13. Core total is 72 official subcategory outcomes.

Default if the user omits document type: **Current vs Target Profile** for the named system.

---

## Profile output — section order (positive recipe)

Emit Profile artefacts in this order. Every section is required when the named system is in scope.

1. **Header** — system name; lifecycle stage (design / develop / deploy / use); generative y/n; scoring legend 🔴🟡🟢; statement that scores are Current vs Target, not NIST maturity.
2. **Intake confirmed** — role (design / develop / deploy / use); whether NIST AI 600-1 applies (MAP-2.1 generative).
3. **Profile table** — one row per in-scope subcategory, grouped GOVERN then MAP then MEASURE then MANAGE. Columns exactly as the Profile row below.
4. **Gap list** — High / Medium / Low only (not “Critical”); GOVERN gaps first, then MAP, MEASURE, MANAGE.
5. **Generative overlay** — include the GAI 12-risk table if and only if MAP-2.1 is generative; omit the table when the system is not generative.
6. **MANAGE next actions** — for each High and Medium gap: mitigate, transfer, avoid, or accept (MG-1.3), with residual-risk note (MG-1.4) when go-live is proposed.

---

## Profile row

| Column | Required content |
|--------|------------------|
| Subcategory | Official ID only (GV-1.2, MAP-1.5, ME-2.11, MG-2.4). No invented IDs. |
| Official outcome | Verbatim short of the official outcome from the matching function file |
| Current 🔴🟡🟢 | 🔴 not started / 🟡 partial / 🟢 implemented |
| Target | Usually 🟢; document a justified 🟡 |
| Evidence | Named artefact, owner, or “—” if none |
| Gap | What is missing relative to the official outcome |

| Subcategory | Official outcome | Current 🔴🟡🟢 | Target | Evidence | Gap |
|-------------|------------------|----------------|--------|----------|-----|
| GV-1.2 | The characteristics of trustworthy AI are integrated into organizational policies, processes, procedures, and practices. | 🟡 | 🟢 | Policy v2 | Characteristics not in SDLC gates |
| MAP-1.5 | Organizational risk tolerances are determined and documented. | 🔴 | 🟢 | — | No tolerance statement |
| ME-2.11 | Fairness and bias – as identified in the MAP function – are evaluated and results are documented. | 🟡 | 🟢 | One audit | Not recurring |
| MG-2.4 | Mechanisms are in place and applied, and responsibilities are assigned and understood, to supersede, disengage, or deactivate AI systems that demonstrate performance or outcomes inconsistent with intended use. | 🔴 | 🟢 | — | No deactivate authority |

---

## Risk-register row

Use after MAP-1 context, MAP-2 tasks/methods, MAP-4 components, and MAP-5 impacts. Tag the NIST AI 100-1 characteristic. Treatment options are MG-1.3: mitigate, transfer, avoid, or accept.

| Column | Required content |
|--------|------------------|
| Risk ID | Org-defined (R-01 …). Not a subcategory ID. |
| MAP category | MAP-1 … MAP-5 as identified |
| Description | Concrete harm or benefit-loss in this system’s context |
| NIST AI 100-1 characteristic | Valid and reliable / Safe / Secure and resilient / Accountable and transparent / Explainable and interpretable / Privacy-enhanced / Fair — harmful bias managed |
| Likelihood | Org scale, documented |
| Impact | Magnitude from MAP-5.1 |
| Treatment (MANAGE) | mitigate / transfer / avoid / accept (MG-1.3) |

| Risk ID | MAP category | Description | NIST AI 100-1 characteristic | Likelihood | Impact | Treatment (MANAGE) |
|---------|--------------|-------------|------------------------------|------------|--------|--------------------|
| R-01 | MAP-5 | Group error rates on resume ranker produce disparate callback rates | Fair — harmful bias managed | Medium | High | mitigate (ME-2.11 + MG-1.3) |
| R-02 | MAP-4 | Third-party embedding API outage silently degrades ranking | Secure and resilient | Medium | Medium | mitigate (GV-6.2, MG-3.1) |
| R-03 | MAP-1 | No documented risk tolerance, so go-live criteria are undefined | Accountable and transparent | High | High | mitigate (MAP-1.5, MG-1.1) |

---

## GAI 12-risk overlay row

Use when MAP-2.1 identifies generative tasks. Map each of the 12 NIST AI 600-1 §2 risks to existing Core IDs. Do not invent Core IDs or 600-1 Action IDs (for example GV-1.1-001) unless quoted from the Profile.

| Column | Required content |
|--------|------------------|
| GAI risk | One of the 12 NIST AI 600-1 §2 names, verbatim |
| Plausible in this context? | Yes / No, with one-line reason |
| Core IDs | Official GOVERN/MAP/MEASURE/MANAGE IDs only |
| Current 🔴🟡🟢 | Overlay score for this risk in this system |
| Target | Usually 🟢 if plausible |
| Evidence / gap | Named control or “—” |

| GAI risk | Plausible in this context? | Core IDs | Current 🔴🟡🟢 | Target | Evidence / gap |
|----------|----------------------------|----------|----------------|--------|----------------|
| Confabulation | Yes — code assistant invents APIs | ME-2.5, ME-2.9, MG-2.4 | 🟡 | 🟢 | Unit tests catch some fabrications; no deactivate path |
| CBRN information or capabilities | No — internal code assistant, no CBRN domain | MAP-5, ME-2.6, ME-2.7, MG-1 | 🟢 | 🟢 | Out of domain; document as not-applicable in MAP-5.1 |
| Harmful bias or homogenization | Yes — training data may encode stereotype | ME-2.11, MAP-5, GV-3 | 🔴 | 🟢 | No fairness evaluation |

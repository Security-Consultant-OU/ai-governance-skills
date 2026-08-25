# Korea AI Basic Act — fill-in recipes

Cite only articles and decree IDs in this file. Default if the user omits document type: **Art. 2(4) classification**, then the **applicable operator matrix**.

## 1 — Art. 2(4) classification recipe

Complete in this order. Write **high-impact (고영향 AI)** in the result. Do not write “high-risk” except as an EU mapping synonym.

| Step | Article / instrument | Fill in | Pass this step if |
|------|----------------------|---------|-------------------|
| 1. Domain | Art. 2(4) + Enforcement Decree No. 36053 | Domain: energy / drinking water / healthcare / medical devices / nuclear / biometric analysis for investigation or arrest / hiring / loan and similar rights or obligations / core transport / public-institution public-service eligibility or cost / student evaluation (early childhood, elementary, secondary) / other decree-added / **none** | Used in a listed or decree-added domain |
| 2. Significance | Art. 2(4) | Life / physical safety / fundamental rights effect: | Likely to **significantly affect** those interests |
| 3. HITL exclusion | Decree No. 36053 | Human makes the **final** decision? Controllable (human can reject/override in fact)? Named decision-maker and authority: | **Both** yes → classify **not high-impact** even if steps 1–2 passed |
| 4. Optional Art. 33 | Art. 33 | Seek MSIT confirmation? Self-review pack (purpose, domain, effects, HITL): | Optional — not a licence |

```
CLASSIFICATION (Art. 2(4) + Decree No. 36053)
System:
Operator type (Art. 2(7)): development / use-service / both / foreign / public
Domain (step 1): …
Significance (step 2): Yes / No — …
HITL exclusion (step 3): Applies / Does not apply — …
RESULT: High-impact / Not high-impact
Art. 33 (step 4): Seek / Not needed
Also check: Art. 31 generative? Yes / No. Art. 32 high-compute? Yes / No.
```

If step 1 or 2 fails, result is **not high-impact**. Then still complete the Art. 31 / Art. 32 checks.

## 2 — Art. 35 endeavor AISIA fill-in

Label the document exactly as below. Legal character: operators **shall endeavor** (Art. 35). Public institutions **prefer** products that have undergone assessment (Art. 35(2)). Not a pre-market gate. MSIT does not approve every AIA.

```
ART. 35 ENDEAVOR AISIA (Art. 35 endeavor impact assessment)
Not a pre-market gate. MSIT does not approve this document. Art. 35(2) is preference, not a licence.

1. METADATA
   - Date / version:
   - System name / version:
   - Operator type (Art. 2(7)): development / use-service / both / foreign / public
   - High-impact (Art. 2(4)): Yes / No
   - HITL exclusion (Decree No. 36053): Applies / Does not apply
   - Art. 33 confirmation: Sought / Not sought
   - Public-institution use (Art. 35(2)): Yes / No — preference only

2. SYSTEM AND USERS (Art. 2(8))
   - Purpose:
   - Domain (Art. 2(4)):
   - Persons provided with the product:
   - Data / outputs:
   - Human final decision:

3. EFFECTS (Art. 2(4), Art. 35)
   - Life / physical safety:
   - Fundamental rights:
   - Hiring / loan / similar obligations:
   - Public-service eligibility or cost:
   - Student evaluation (early childhood / elementary / secondary):

4. MEASURES (Art. 34 if high-impact; otherwise endeavor narrative)
   - Risk management:
   - Explainability — results / main criteria / training-data overview (Art. 34(1)2 if high-impact):
   - User protection:
   - Human oversight:
   - Documentation location:

5. ENDEAVOR CONCLUSION
   - Residual issues:
   - Owner / next review:
   - This file is not an MSIT licence or market-access certificate
```

## 3 — Art. 36 threshold checklist

Designate a domestic representative when there is a Korean nexus **and any** limb below is met. Failure: administrative fine up to **KRW 30 million** (Art. 43). The Art. 2(8) user is not the representative.

| Limb | Article / instrument | Operator figure | Threshold | Met? |
|------|----------------------|-----------------|-----------|------|
| Korean nexus | Art. 36 | Provides AI in or into Korea: Yes / No | Nexus required | |
| Total revenue | Art. 36 + Decree No. 36053 | KRW … | ≥ **KRW 1 trillion** | |
| AI-related revenue | Art. 36 + Decree No. 36053 | KRW … | ≥ **KRW 10 billion** | |
| Average daily Korean users | Art. 36 + Decree No. 36053 | … users | ≥ **1 million** | |
| Corrective-order fine | Art. 36 + Decree No. 36053 | Fined for violating a corrective order: Yes / No | Any such fine | |

```
ART. 36 DOMESTIC REPRESENTATIVE
Korean nexus: Yes / No
Limbs met: total revenue / AI revenue / 1M daily users / corrective-order fine / none
IN SCOPE: Yes / No
Representative name / Korean address / contact:
Mandate (receive MSIT communications; Art. 31–36 matters):
Art. 31 notices and Art. 34 measures remain with the operator (Art. 36 does not replace them)
Art. 43 exposure if missing: up to KRW 30 million
```

## 4 — Gap row

Score only requirements that apply after classification and operator mapping. 🔴 not started — no evidence. 🟡 partial — some implementation, gaps remain. 🟢 implemented — fully met with documented evidence.

| Requirement | Article | Applies? | Status | Evidence | Gap notes | Priority |
|-----------|---------|----------|--------|----------|-----------|----------|
| Classification record | Art. 2(4) | Yes | 🔴🟡🟢 | | | Critical |
| HITL exclusion documented | Decree No. 36053 | If claimed | 🔴🟡🟢 | | | High |
| Art. 31(1) prior notice | Art. 31(1) | HI or generative? | 🔴🟡🟢 | | | Critical |
| Art. 31(2) generative labels | Art. 31(2) | Generative? | 🔴🟡🟢 | | | High |
| Art. 31(3) synthetic A/V/I notice | Art. 31(3) | Hard-to-distinguish? | 🔴🟡🟢 | | | High |
| Art. 34 risk management | Art. 34 | High-impact? | 🔴🟡🟢 | | | Critical |
| Art. 34(1)2 explainability | Art. 34(1)2 | High-impact? | 🔴🟡🟢 | | | Critical |
| Art. 34 user protection | Art. 34 | High-impact? | 🔴🟡🟢 | | | High |
| Art. 34 human oversight | Art. 34 | High-impact? | 🔴🟡🟢 | | | High |
| Art. 34 documentation | Art. 34 | High-impact? | 🔴🟡🟢 | | | High |
| Art. 35 endeavor AISIA | Art. 35 | Endeavor | 🔴🟡🟢 | | | Medium |
| Art. 35(2) public preference | Art. 35(2) | Public buyer? | 🔴🟡🟢 | | | Medium |
| Art. 30(4) public duties | Art. 30(4) | Public institution? | 🔴🟡🟢 | | | High |
| Art. 36 representative | Art. 36 | Foreign + a threshold limb? | 🔴🟡🟢 | | | Critical |
| Art. 32 safety + MSIT results | Art. 32 | 10^26 FLOPs and SOTA and broad rights risk? | 🔴🟡🟢 | | | High |

**Single gap row (copy per extra requirement):**

```
REQUIREMENT | ARTICLE | APPLIES? | STATUS 🔴🟡🟢 | EVIDENCE | GAP NOTES | PRIORITY
…           | …      | Yes/No   | …            | …        | …         | Critical/High/Medium
```

## 5 — Operator matrix (after classification)

| Obligation | Development operator (Art. 2(7)(a)) | Use/service operator (Art. 2(7)(b)) | Foreign operator | Public institution | Article | Status |
|------------|-------------------------------------|-------------------------------------|------------------|--------------------|---------|--------|
| Classification record | | | | | Art. 2(4), Art. 33 optional | 🔴🟡🟢 |
| Prior AI-use notice | | | | | Art. 31(1) (HI or generative only) | 🔴🟡🟢 |
| Generative output labels | | | | | Art. 31(2) | 🔴🟡🟢 |
| Synthetic A/V/I notice | | | | | Art. 31(3) | 🔴🟡🟢 |
| High-impact measures | | | | | Art. 34, Art. 34(1)2 | 🔴🟡🟢 |
| Art. 35 endeavor AISIA | Endeavor | Endeavor | Endeavor | Prefer assessed products (Art. 35(2)) | Art. 35 | 🔴🟡🟢 |
| Extra public duties | — | — | — | | Art. 30(4) | 🔴🟡🟢 |
| Domestic representative | — | — | If threshold | — | Art. 36 | 🔴🟡🟢 |
| High-compute safety + results to MSIT | If Art. 32 in-scope | If Art. 32 in-scope | If Art. 32 in-scope | If Art. 32 in-scope | Art. 32 | 🔴🟡🟢 |
